import 'dart:ffi';
import 'dart:io';

import 'package:ffi/ffi.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_dynamic_icon_plus/flutter_dynamic_icon_plus.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'app_icon_keys.dart';

/// Changes the app's icon to match the language that was studied last: the
/// chameleon stays, the character in his speech bubble changes.
///
/// * Android: the launcher icon is switched with `activity-alias` entries, through
///   the `flutter_dynamic_icon_plus` package. This needs a one-time manifest change
///   (`tools/icon/patch_android_manifest.py`). Android applies the change when the
///   app is closed, not at once, and some launchers take a few seconds.
/// * Windows: the window and taskbar icon is changed while the app runs, by sending
///   WM_SETICON to the app's own window. The .exe file's icon in Explorer, and a
///   pinned shortcut, cannot change and keep the neutral icon.
/// * Everything else: nothing happens.
///
/// Every failure is swallowed: a missing alias, an old launcher or a missing icon
/// file must never get in the way of studying.
class AppIconService {
  AppIconService(this._prefs);

  final SharedPreferences _prefs;

  static const _kAppliedKey = 'app_icon_key';
  String? _applied;
  Future<void> _queue = Future.value();

  /// Point the icon at [deckId]'s language. Calls are run one after another.
  void setForDeck(String deckId) {
    final key = AppIconKeys.forDeck(deckId);
    _queue = _queue.then((_) => _apply(key)).catchError((Object e) {
      debugPrint('AppIconService: $e');
    });
  }

  Future<void> _apply(String key) async {
    if (key == _applied) return;
    _applied = key;
    if (Platform.isAndroid) {
      await _applyAndroid(key);
    } else if (Platform.isWindows) {
      _applyWindows(key);
    }
  }

  // ------------------------------------------------------------------ Android

  Future<void> _applyAndroid(String key) async {
    // Only touch the launcher when the choice changed since last time.
    if (_prefs.getString(_kAppliedKey) == key) return;
    try {
      if (!await FlutterDynamicIconPlus.supportsAlternateIcons) return;
      await FlutterDynamicIconPlus.setAlternateIconName(
        iconName: key == AppIconKeys.defaultKey ? null : 'icon_$key',
      );
      await _prefs.setString(_kAppliedKey, key);
    } catch (e) {
      // Usually: the manifest has not been patched, so there is no such alias.
      debugPrint('AppIconService (Android): $e');
    }
  }

  // ------------------------------------------------------------------ Windows

  static final _WinIcons _win = _WinIcons();

  void _applyWindows(String key) {
    final exeDir = File(Platform.resolvedExecutable).parent.path;
    final sep = Platform.pathSeparator;
    final path = [exeDir, 'data', 'flutter_assets', 'assets', 'icon', 'win', '$key.ico'].join(sep);
    if (!File(path).existsSync()) return;
    _win.setWindowIcon(path);
  }
}

/// Just enough of user32 to give the app's own window a new icon.
class _WinIcons {
  static const _imageIcon = 1;
  static const _lrLoadFromFile = 0x10;
  static const _wmSetIcon = 0x80;
  static const _iconSmall = 0;
  static const _iconBig = 1;
  static const _smCxIcon = 11;
  static const _smCxSmIcon = 49;
  static const _className = 'FLUTTER_RUNNER_WIN32_WINDOW';

  late final DynamicLibrary _user32 = DynamicLibrary.open('user32.dll');
  late final DynamicLibrary _kernel32 = DynamicLibrary.open('kernel32.dll');

  late final int Function(int, Pointer<Utf16>, int, int, int, int) _loadImage = _user32
      .lookupFunction<IntPtr Function(IntPtr, Pointer<Utf16>, Uint32, Int32, Int32, Uint32),
          int Function(int, Pointer<Utf16>, int, int, int, int)>('LoadImageW');
  late final int Function(int, int, int, int) _sendMessage = _user32
      .lookupFunction<IntPtr Function(IntPtr, Uint32, IntPtr, IntPtr),
          int Function(int, int, int, int)>('SendMessageW');
  late final int Function(int, int, Pointer<Utf16>, Pointer<Utf16>) _findWindowEx = _user32
      .lookupFunction<IntPtr Function(IntPtr, IntPtr, Pointer<Utf16>, Pointer<Utf16>),
          int Function(int, int, Pointer<Utf16>, Pointer<Utf16>)>('FindWindowExW');
  late final int Function(int, Pointer<Uint32>) _windowProcessId = _user32
      .lookupFunction<Uint32 Function(IntPtr, Pointer<Uint32>),
          int Function(int, Pointer<Uint32>)>('GetWindowThreadProcessId');
  late final int Function(int) _getSystemMetrics =
      _user32.lookupFunction<Int32 Function(Int32), int Function(int)>('GetSystemMetrics');
  late final int Function(int) _destroyIcon =
      _user32.lookupFunction<Int32 Function(IntPtr), int Function(int)>('DestroyIcon');
  late final int Function() _currentProcessId =
      _kernel32.lookupFunction<Uint32 Function(), int Function()>('GetCurrentProcessId');

  int _bigHandle = 0;
  int _smallHandle = 0;

  /// This process's runner window, or 0. The class name is the Flutter runner's
  /// default; the process id keeps it from picking another Flutter app's window.
  int _findOwnWindow() {
    final cls = _className.toNativeUtf16();
    final pidOut = calloc<Uint32>();
    try {
      final me = _currentProcessId();
      var hwnd = 0;
      for (var i = 0; i < 32; i++) {
        hwnd = _findWindowEx(0, hwnd, cls, nullptr);
        if (hwnd == 0) return 0;
        _windowProcessId(hwnd, pidOut);
        if (pidOut.value == me) return hwnd;
      }
      return 0;
    } finally {
      calloc.free(cls);
      calloc.free(pidOut);
    }
  }

  void setWindowIcon(String icoPath) {
    final hwnd = _findOwnWindow();
    if (hwnd == 0) return;
    final p = icoPath.toNativeUtf16();
    try {
      final big = _loadImage(0, p, _imageIcon, _getSystemMetrics(_smCxIcon), _getSystemMetrics(_smCxIcon), _lrLoadFromFile);
      final small = _loadImage(0, p, _imageIcon, _getSystemMetrics(_smCxSmIcon), _getSystemMetrics(_smCxSmIcon), _lrLoadFromFile);
      if (big == 0 && small == 0) return;
      if (big != 0) _sendMessage(hwnd, _wmSetIcon, _iconBig, big);
      if (small != 0) _sendMessage(hwnd, _wmSetIcon, _iconSmall, small);
      // The window now uses the new handles; the old ones are ours to release.
      if (_bigHandle != 0) _destroyIcon(_bigHandle);
      if (_smallHandle != 0) _destroyIcon(_smallHandle);
      _bigHandle = big;
      _smallHandle = small;
    } finally {
      calloc.free(p);
    }
  }
}

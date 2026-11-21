#!/usr/bin/env python3
"""One-time change to android/app/src/main/AndroidManifest.xml so the launcher icon can follow the
language studied last (flutter_dynamic_icon_plus):

  1. the MAIN/LAUNCHER intent-filter moves from MainActivity to an alias called .DEFAULT,
  2. one disabled alias per language (.icon_ru, .icon_ja, ...) with its own icon,
  3. the plugin's service.

Run it once from the project root, after `flutter create` has made the android folder and the icon
files are in place (extract the zip over the project first):

    python3 tools/icon/patch_android_manifest.py
    python3 tools/icon/patch_android_manifest.py path/to/AndroidManifest.xml   # another file

It keeps a copy as AndroidManifest.xml.bak and does nothing if the file is already patched.
If you would rather edit by hand, run it on a copy and copy the <activity-alias> blocks across.
"""
import os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from icon_keys import VARIANTS  # noqa: E402

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "android", "app", "src", "main", "AndroidManifest.xml")
path = os.path.abspath(path)
if not os.path.exists(path):
    sys.exit(f"{path} not found. Run `flutter create --platforms=android .` first, or pass the manifest's path.")
src = open(path, encoding="utf-8").read()
if "FlutterDynamicIconPlusService" in src:
    sys.exit("Already patched, nothing to do.")

# 1. take the launcher filter off MainActivity
m = re.search(r"<activity\b(?:(?!</activity>).)*?android:name=\"[^\"]*MainActivity\"(?:(?!</activity>).)*</activity>", src, re.S)
if not m:
    sys.exit("Could not find MainActivity in the manifest; nothing changed.")
act = m.group(0)
filt = re.search(r"\s*<intent-filter>(?:(?!</intent-filter>).)*android\.intent\.category\.LAUNCHER(?:(?!</intent-filter>).)*</intent-filter>", act, re.S)
if not filt:
    sys.exit("MainActivity has no LAUNCHER intent-filter; nothing changed.")
new_act = act.replace(filt.group(0), "", 1)
# the plugin's docs ask for singleTop; the Flutter template already has it
if "android:launchMode" not in new_act:
    new_act = new_act.replace("<activity", '<activity\n            android:launchMode="singleTop"', 1)
# a splash drawable on the activity breaks alias launches on new Android versions
new_act = re.sub(r"\s*<meta-data\s+android:name=\"io\.flutter\.embedding\.android\.SplashScreenDrawable\"[^>]*/>", "", new_act)

launcher = """
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>"""


def alias(name, icon, enabled):
    return f"""
        <activity-alias
            android:name=".{name}"
            android:enabled="{'true' if enabled else 'false'}"
            android:exported="true"
            android:icon="@mipmap/{icon}"
            android:targetActivity=".MainActivity">{launcher}
        </activity-alias>"""


blocks = ["""
        <service
            android:name="com.solusibejo.flutter_dynamic_icon_plus.FlutterDynamicIconPlusService"
            android:stopWithTask="false"/>""", alias("DEFAULT", "ic_launcher", True)]
for key, _deck, _glyph, _lang in VARIANTS:
    blocks.append(alias(f"icon_{key}", f"ic_launcher_{key}", False))

out = src.replace(act, new_act, 1)
out = out.replace("</application>", "".join(blocks) + "\n    </application>", 1)
shutil.copy(path, path + ".bak")
open(path, "w", encoding="utf-8").write(out)
print(f"Patched {path} ({len(VARIANTS)} language icons). The old file is {path}.bak")

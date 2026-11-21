"""Generates the four short answer-feedback sounds in assets/sfx/.

Run from the repo root:  python3 tools/sfx/make_sfx.py

The sounds are synthesised here (sine partials with a quick attack and an
exponential decay), so they are original to this project and carry no licence.
16-bit mono PCM, 44.1 kHz, peak level about 0.55 so they sit under the voice.
"""
import math
import os
import struct
import wave

RATE = 44100
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sfx")


def note(total, freq, dur, start, amp=1.0, partials=((1, 1.0), (2, 0.35), (3, 0.12)), decay=7.0, glide=0.0):
    """Mix one decaying note into the sample list `total` beginning at `start` seconds."""
    n = int(dur * RATE)
    s0 = int(start * RATE)
    for i in range(n):
        t = i / RATE
        attack = min(1.0, t / 0.006)
        env = attack * math.exp(-decay * t / dur)
        f = freq * (1 + glide * (t / dur))
        v = 0.0
        for k, a in partials:
            v += a * math.sin(2 * math.pi * f * k * t)
        idx = s0 + i
        if idx < len(total):
            total[idx] += amp * env * v


def render(name, length, notes, peak=0.55):
    total = [0.0] * int(length * RATE)
    for args in notes:
        note(total, *args)
    m = max(abs(x) for x in total) or 1.0
    # fade the last 15 ms so there is never a click at the end
    fade = int(0.015 * RATE)
    for i in range(fade):
        total[-1 - i] *= i / fade
    data = b"".join(struct.pack("<h", int(max(-1, min(1, x / m * peak)) * 32767)) for x in total)
    path = os.path.join(OUT, name)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(data)
    print(name, len(total) / RATE, "s")


os.makedirs(OUT, exist_ok=True)
# Correct: a bright two-note rise (E5 then B5)
render("correct.wav", 0.55, [(659.25, 0.30, 0.00), (987.77, 0.45, 0.11)])
# Easy: a four-note sparkle (C5 E5 G5 C6)
render("easy.wav", 0.75, [(523.25, 0.30, 0.00), (659.25, 0.30, 0.08), (783.99, 0.30, 0.16), (1046.5, 0.50, 0.24)])
# Hard: two soft equal taps (A4), neutral
render("hard.wav", 0.32, [(440.0, 0.14, 0.00), (440.0, 0.16, 0.13)])
# Incorrect: a gentle falling pair, low and rounded rather than a harsh buzz
render("incorrect.wav", 0.50, [(311.13, 0.25, 0.00, 1.0, ((1, 1.0), (2, 0.2)), 6.0, -0.06), (233.08, 0.32, 0.14, 1.0, ((1, 1.0), (2, 0.2)), 6.0, -0.05)])

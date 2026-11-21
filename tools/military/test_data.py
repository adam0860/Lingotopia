"""Checks on assets/military/ru_military.json that mirror test/military_test.dart,
for machines without a Dart SDK. Run:  python3 -I tools/military/test_data.py"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ACUTE = "́"


def fnv1a(s):
    h = 0x811C9DC5
    for ch in s:
        h ^= ord(ch)
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h


def plain(s):
    return s.replace(ACUTE, "")


def np36(n):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    out = ""
    while True:
        n, r = divmod(n, 36)
        out = digits[r] + out
        if n == 0:
            return out


def main():
    d = json.load(open(ROOT / "assets" / "military" / "ru_military.json", encoding="utf-8"))
    bad = []

    def check(cond, msg):
        if not cond:
            bad.append(msg)

    # --- the military cards merged into the Russian flashcard deck ---
    deck = json.load(open(ROOT / "assets" / "decks" / "russian_core.json", encoding="utf-8"))
    cards = deck["cards"]
    check(deck["cardCount"] == len(cards), "cardCount mismatch")
    check(all(c["pos"] in ("mil", "abbr") for c in cards[10000:]), "non-military card after rank 10000")
    check(all(c["pos"] not in ("mil", "abbr") for c in cards[:10000]), "military card inside core 10000")
    lem = [c["lemma"] for c in cards[10000:]]
    check(len(set(lem)) == len(lem), "duplicate military lemma")
    core = {c["lemma"].lower().replace("ё", "е") for c in cards[:10000]}
    check(not any(l.lower().replace("ё", "е") in core for l in lem), "military card duplicates a core word")

    secs = d["sections"]
    terms = [(s["id"], t) for s in secs for g in s["groups"] for t in g["terms"]]
    acr = [a for g in d["acronyms"] for a in g["items"]]
    check(len(secs) >= 20, "sections < 20")
    check(len(terms) > 4000, "terms <= 4000")
    check(len(acr) > 400, "acronyms <= 400")
    for sid in ("infantry", "artillery", "airdefense", "radio", "comms"):
        check(any(s["id"] == sid for s in secs), "missing section " + sid)
    for s in secs:
        n = sum(len(g["terms"]) for g in s["groups"])
        check(n > 20, "small section " + s["id"])

    seen = set()
    for sid, t in terms:
        check(t["r"].strip() and t["e"].strip(), "empty term in " + sid)
        check("'" not in t["r"], "apostrophe in " + t["r"])
        k = (sid, np36(fnv1a(plain(t["r"]) + "|" + t["e"].lower())))
        check(k not in seen, "duplicate key %s %s" % (sid, t["r"]))
        seen.add(k)

    keys = set()
    for a in acr:
        check(a["a"] and a["f"].strip() and a["e"].strip() and a["r"].strip(), "incomplete acronym " + a["a"])
        keys.add("a" + np36(fnv1a(a["a"] + "|" + a["e"].lower())))
    check(len(keys) == len(acr), "acronym key collision")

    byabbr = {a["a"]: plain(a["f"]) for a in acr}
    check(byabbr.get("ВДВ") == "Воздушно-десантные войска", "ВДВ expansion")
    check(byabbr.get("БМП") == "боевая машина пехоты", "БМП expansion")
    check(byabbr.get("РЭБ") == "радиоэлектронная борьба", "РЭБ expansion")
    check(byabbr.get("НАТО") == "Организация Североатлантического договора", "НАТО expansion")
    check(fnv1a("a") == 0xE40C292C and fnv1a("") == 0x811C9DC5, "fnv1a")

    print("sections %d, terms %d, acronyms %d" % (len(secs), len(terms), len(acr)))
    if bad:
        print("%d problem(s):" % len(bad))
        for b in bad[:40]:
            print("  ", b)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())


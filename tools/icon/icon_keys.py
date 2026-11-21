"""The icon variants: one per deck. `key` is the deck id without `_core`; `glyph` is what sits in the
speech bubble above the chameleon. `default` is the neutral icon (文A) used before any language is chosen."""
VARIANTS = [
    # key,  deck id,   glyph, language
    ("ru",  "ru_core",  "Я",   "Russian"),
    ("es",  "es_core",  "Ñ",   "Spanish"),
    ("ja",  "ja_core",  "あ",  "Japanese"),
    ("ar",  "ar_core",  "ع",   "Arabic (MSA)"),
    ("arz", "arz_core", "ج",   "Egyptian Arabic"),
    ("zh",  "zh_core",  "汉",  "Chinese (Mandarin)"),
    ("ko",  "ko_core",  "한",  "Korean"),
    ("it",  "it_core",  "È",   "Italian"),
    ("tl",  "tl_core",  "Ng",  "Tagalog"),
    ("pl",  "pl_core",  "Ł",   "Polish"),
    ("sw",  "sw_core",  "Ng’", "Swahili"),
    ("tr",  "tr_core",  "Ş",   "Turkish"),
    ("pt",  "pt_core",  "Ã",   "Portuguese"),
]
DEFAULT_GLYPH = "文A"

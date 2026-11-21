"""
Authoring helpers and automatic checks for the Spanish lessons.

Lessons are written as Python (tools/lessons/es_unit*.py) and compiled to the
JSON the app ships (assets/lessons/es_lessons.json). The constructors are the
ones the Russian course uses (dsl.py); this file adds what Spanish needs.

Writing conventions
-------------------
Accents are plain Unicode (está, canción, ñ). There is no stress apostrophe.
Inverted marks are required: ¿Cómo estás?  ¡Hola!
Spoken text (example sentences, table cells in a `say=[...]` column) is Spanish
only, with no abbreviations or digits, because the voice reads them literally:
write "usted", "señor", "veinte", not "Ud.", "Sr.", "20". Use the middle dot
(·) between forms in one cell to make the voice pause.
`{...}` in a table cell highlights the ending being taught.

Tables
------
table(headers, rows, say=[0, 2]) marks which columns are Spanish and so
tappable to hear. Columns not listed (English glosses, labels) are not.

What the build checks
---------------------
  * structure: option counts, unique options, one blank per fill-in, highlight
    text really present in its example, table row widths, braces
  * gating: every requiredLemma exists in the deck, with its rank reported
  * spelling: every word in Spanish-only text is a real form of some word;
    in mixed English/Spanish text a word must be Spanish or English
  * punctuation: every ? has its ¿ and every ! its ¡; interrogatives carry
    their accent after ¿ (¿Cómo, ¿Qué, ¿Dónde, ¿De dónde...)
  * gender: an article + noun pair is compared with Wiktionary's noun gender
  * morphology: vf(lemma, form) must be a real form of the lemma; vp(verb, ...)
    and exercises tagged lemma="hablar:yo" are compared with the full present
    -tense paradigm (regular endings plus the irregulars taught in Unit 1)
  * no stray Cyrillic or non-NFC text; no abbreviations in spoken text
"""

import os
import re
import sys
import unicodedata
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsl import (card, compile_course, ex, fb, lesson, load_deck_ranks, mc,  # noqa: E402,F401
                 unit, vf, write_json)

# ------------------------------------------------------------------ constructors


def table(headers, rows, title=None, note=None, say=None):
    d = {"headers": headers, "rows": rows}
    if title:
        d["title"] = title
    if note:
        d["note"] = note
    if say is not None:
        d["speakCols"] = list(say)
    return d


def F(prompt, ans, wrong, why, tr=None, lemma=None):
    """Fill-in-the-blank: right answer first, then the distractors."""
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


def M(prompt, ans, wrong, why, tr=None, lemma=None):
    """Multiple choice: right answer first, then the distractors."""
    return mc(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


def vp(verb, *forms):
    """verify= helper for a present-tense table, in the order
    yo, tú, él/ella/usted, nosotros, vosotros, ellos/ellas/ustedes.
    A None skips that person."""
    return [(verb, i, f) for i, f in enumerate(forms) if f is not None]


def vpp(verb, *forms):
    """Same as vp, for the preterite."""
    return [(verb, i, f, "pret") for i, f in enumerate(forms) if f is not None]


def vpc(verb, usted, ustedes=None):
    """Same, for the formal commands (usted, ustedes)."""
    out = [(verb, 2, usted, "cmd")]
    if ustedes is not None:
        out.append((verb, 5, ustedes, "cmd"))
    return out


def vpf(verb, *forms):
    """Same as vp, for the simple future tense."""
    return [(verb, i, f, "fut") for i, f in enumerate(forms) if f is not None]


# ------------------------------------------------------------------ paradigms

PERSON_IDX = {"yo": 0, "tú": 1, "tu": 1, "él": 2, "el": 2, "ella": 2, "usted": 2, "ud": 2,
              "nosotros": 3, "nos": 3, "vosotros": 4, "vos": 4,
              "ellos": 5, "ellas": 5, "ustedes": 5, "uds": 5}

IRREG = {
    "ser": ["soy", "eres", "es", "somos", "sois", "son"],
    "estar": ["estoy", "estás", "está", "estamos", "estáis", "están"],
    "tener": ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"],
    "hacer": ["hago", "haces", "hace", "hacemos", "hacéis", "hacen"],
    "ir": ["voy", "vas", "va", "vamos", "vais", "van"],
    "dar": ["doy", "das", "da", "damos", "dais", "dan"],
    "saber": ["sé", "sabes", "sabe", "sabemos", "sabéis", "saben"],
    "recoger": ["recojo", "recoges", "recoge", "recogemos", "recogéis", "recogen"],
    "nacer": ["nazco", "naces", "nace", "nacemos", "nacéis", "nacen"],
    "enviar": ["envío", "envías", "envía", "enviamos", "enviáis", "envían"],
    "construir": ["construyo", "construyes", "construye", "construimos", "construís", "construyen"],
    "incluir": ["incluyo", "incluyes", "incluye", "incluimos", "incluís", "incluyen"],
    "vivir": ["vivo", "vives", "vive", "vivimos", "vivís", "viven"],
    "conocer": ["conozco", "conoces", "conoce", "conocemos", "conocéis", "conocen"],
    "ver": ["veo", "ves", "ve", "vemos", "veis", "ven"],
}
_ENDS = {"ar": ["o", "as", "a", "amos", "áis", "an"],
         "er": ["o", "es", "e", "emos", "éis", "en"],
         "ir": ["o", "es", "e", "imos", "ís", "en"]}


# --- Unit 2 additions: stem-changing verbs, -go verbs, -zco verbs, futures, gerunds, vos

STEM = {  # verb: (letters in the stem, replacement)
    "poder": ("o", "ue"), "volver": ("o", "ue"), "dormir": ("o", "ue"), "almorzar": ("o", "ue"),
    "costar": ("o", "ue"), "contar": ("o", "ue"), "encontrar": ("o", "ue"), "soñar": ("o", "ue"),
    "mover": ("o", "ue"), "recordar": ("o", "ue"), "mostrar": ("o", "ue"), "morir": ("o", "ue"),
    "llover": ("o", "ue"), "tronar": ("o", "ue"), "soler": ("o", "ue"), "acostar": ("o", "ue"), "jugar": ("u", "ue"),
    "querer": ("e", "ie"), "pensar": ("e", "ie"), "cerrar": ("e", "ie"), "empezar": ("e", "ie"),
    "comenzar": ("e", "ie"), "entender": ("e", "ie"), "perder": ("e", "ie"), "preferir": ("e", "ie"),
    "mentir": ("e", "ie"), "nevar": ("e", "ie"), "sentir": ("e", "ie"), "despertar": ("e", "ie"),
    "pedir": ("e", "i"), "servir": ("e", "i"), "repetir": ("e", "i"), "vestir": ("e", "i"),
    "competir": ("e", "i"), "seguir": ("e", "i"), "conseguir": ("e", "i"),
    # Unit 21-24 additions
    "doler": ("o", "ue"), "resolver": ("o", "ue"), "devolver": ("o", "ue"), "demostrar": ("o", "ue"),
    "comprobar": ("o", "ue"), "probar": ("o", "ue"), "aprobar": ("o", "ue"), "volar": ("o", "ue"), "colgar": ("o", "ue"),
    "recomendar": ("e", "ie"), "atender": ("e", "ie"), "defender": ("e", "ie"), "encender": ("e", "ie"),
    "sugerir": ("e", "ie"), "advertir": ("e", "ie"), "convertir": ("e", "ie"), "divertir": ("e", "ie"),
    "sembrar": ("e", "ie"), "enterrar": ("e", "ie"), "temblar": ("e", "ie"), "negar": ("e", "ie"),
    "calentar": ("e", "ie"), "descender": ("e", "ie"), "extender": ("e", "ie"), "sentar": ("e", "ie"),
    "atravesar": ("e", "ie"), "invertir": ("e", "ie"),
    # Unit 36-40 additions
    "acordar": ("o", "ue"), "adherir": ("e", "ie"), "cegar": ("e", "ie"), "enmendar": ("e", "ie"),
    "revertir": ("e", "ie"), "encomendar": ("e", "ie"), "envolver": ("o", "ue"), "heder": ("e", "ie"),
    "tender": ("e", "ie"), "conferir": ("e", "ie"), "rodar": ("o", "ue"), "embestir": ("e", "i"),
    "teñir": ("e", "i"), "acertar": ("e", "ie"), "desmentir": ("e", "ie"), "consentir": ("e", "ie"),
    "gobernar": ("e", "ie"), "trascender": ("e", "ie"), "ascender": ("e", "ie"), "concebir": ("e", "i"),
    "reconocer": ("o", "o"),
}
STEM.pop("reconocer")
for _v, (_a, _b) in STEM.items():
    _stem = _v[:-2]
    _i = _stem.rfind(_a)
    _st = _stem[:_i] + _b + _stem[_i + len(_a):]
    _e = _ENDS[_v[-2:]]
    _f = [_st + _e[0], _st + _e[1], _st + _e[2], _stem + _e[3], _stem + _e[4], _st + _e[5]]
    if _v == "seguir":
        _f[0] = "sigo"
    if _v == "conseguir":
        _f[0] = "consigo"
    IRREG[_v] = _f
IRREG.update({
    "poner": ["pongo", "pones", "pone", "ponemos", "ponéis", "ponen"],
    "salir": ["salgo", "sales", "sale", "salimos", "salís", "salen"],
    "venir": ["vengo", "vienes", "viene", "venimos", "venís", "vienen"],
    "decir": ["digo", "dices", "dice", "decimos", "decís", "dicen"],
    "traer": ["traigo", "traes", "trae", "traemos", "traéis", "traen"],
    "caer": ["caigo", "caes", "cae", "caemos", "caéis", "caen"],
    "valer": ["valgo", "vales", "vale", "valemos", "valéis", "valen"],
    "oír": ["oigo", "oyes", "oye", "oímos", "oís", "oyen"],
    "oler": ["huelo", "hueles", "huele", "olemos", "oléis", "huelen"],
    "reír": ["río", "ríes", "ríe", "reímos", "reís", "ríen"],
    "sonreír": ["sonrío", "sonríes", "sonríe", "sonreímos", "sonreís", "sonríen"],
    "elegir": ["elijo", "eliges", "elige", "elegimos", "elegís", "eligen"],
    "contribuir": ["contribuyo", "contribuyes", "contribuye", "contribuimos", "contribuís", "contribuyen"],
    "destruir": ["destruyo", "destruyes", "destruye", "destruimos", "destruís", "destruyen"],
    "huir": ["huyo", "huyes", "huye", "huimos", "huis", "huyen"],
    "influir": ["influyo", "influyes", "influye", "influimos", "influís", "influyen"],
    "haber": ["he", "has", "ha", "hemos", "habéis", "han"],
    "llevar": ["llevo", "llevas", "lleva", "llevamos", "lleváis", "llevan"],
    "enviar": ["envío", "envías", "envía", "enviamos", "enviáis", "envían"],
    "esquiar": ["esquío", "esquías", "esquía", "esquiamos", "esquiáis", "esquían"],
    "prohibir": ["prohíbo", "prohíbes", "prohíbe", "prohibimos", "prohibís", "prohíben"],
    "reunir": ["reúno", "reúnes", "reúne", "reunimos", "reunís", "reúnen"],
    "aislar": ["aíslo", "aíslas", "aísla", "aislamos", "aisláis", "aíslan"],
    "rehusar": ["rehúso", "rehúsas", "rehúsa", "rehusamos", "rehusáis", "rehúsan"],
})
# Unit 26-30: -iar/-uar verbs with a written accent in the stressed forms, and rogar (o→ue)
for _v in ("ansiar", "confiar", "fiar", "guiar", "variar", "enfriar", "criar", "desviar", "actuar",
           "continuar", "graduar", "situar", "evaluar", "efectuar", "insinuar"):
    if _v not in IRREG:
        _st = _v[:-2]
        _a = "í" if _v.endswith("iar") else "ú"
        _b = _st[:-1] + _a
        IRREG[_v] = [_b + "o", _b + "as", _b + "a", _st + "amos", _st + "áis", _b + "an"]
for _v in ("distribuir", "atribuir", "disminuir", "sustituir", "constituir", "concluir", "excluir", "retribuir", "intuir", "diluir", "instruir"):
    if _v not in IRREG:
        _st = _v[:-2]
        IRREG[_v] = [_st + "yo", _st + "yes", _st + "ye", _st + "imos", _st + "ís", _st + "yen"]
IRREG["rogar"] = ["ruego", "ruegas", "ruega", "rogamos", "rogáis", "ruegan"]
_NOZCO = {"hacer", "deshacer", "cocer", "mecer", "escocer"}

FUT_STEM = {"poder": "podr", "poner": "pondr", "salir": "saldr", "tener": "tendr", "valer": "valdr",
            "venir": "vendr", "caber": "cabr", "haber": "habr", "saber": "sabr", "decir": "dir",
            "hacer": "har", "querer": "querr"}
_FUT_END = ["é", "ás", "á", "emos", "éis", "án"]

GERUND_IRREG = {"leer": "leyendo", "creer": "creyendo", "construir": "construyendo", "incluir": "incluyendo",
                "ir": "yendo", "oír": "oyendo", "caer": "cayendo", "traer": "trayendo", "reír": "riendo",
                "sonreír": "sonriendo", "decir": "diciendo", "dormir": "durmiendo", "morir": "muriendo",
                "pedir": "pidiendo", "servir": "sirviendo", "repetir": "repitiendo", "vestir": "vistiendo",
                "preferir": "prefiriendo", "mentir": "mintiendo", "sentir": "sintiendo", "venir": "viniendo",
                "poder": "pudiendo", "seguir": "siguiendo", "competir": "compitiendo", "elegir": "eligiendo",
                "destruir": "destruyendo", "contribuir": "contribuyendo", "huir": "huyendo",
                "influir": "influyendo", "despertar": "despertando"}


def gerund(verb):
    if verb in GERUND_IRREG:
        return GERUND_IRREG[verb]
    if verb.endswith("ar"):
        return verb[:-2] + "ando"
    return verb[:-2] + "iendo"


def _vos(verb):
    if verb == "ser":
        return "sos"
    if verb in ("ir",):
        return "vas"
    if verb == "estar":
        return "estás"
    if verb == "ver":
        return "ves"
    if verb == "dar":
        return "das"
    stem = verb[:-2]
    return stem + {"ar": "ás", "er": "és", "ir": "ís"}[verb[-2:]]


# --- Unit 12-15 additions: the preterite and formal commands

PRET_IRREG = {
    "ser": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
    "ir": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
    "dar": ["di", "diste", "dio", "dimos", "disteis", "dieron"],
    "ver": ["vi", "viste", "vio", "vimos", "visteis", "vieron"],
    "haber": [None, None, "hubo", None, None, None],
    "oír": ["oí", "oíste", "oyó", "oímos", "oísteis", "oyeron"],
}
_PRET_E = ["e", "iste", "o", "imos", "isteis", "ieron"]
PRET_STEM = {  # irregular stems that take -e, -iste, -o, -imos, -isteis, -ieron
    "estar": "estuv", "tener": "tuv", "poder": "pud", "poner": "pus", "saber": "sup", "hacer": "hic",
    "venir": "vin", "querer": "quis", "andar": "anduv", "caber": "cup",
    "decir": "dij", "traer": "traj", "traducir": "traduj", "conducir": "conduj", "producir": "produj",
    "introducir": "introduj", "reducir": "reduj",
    "detener": "detuv", "mantener": "mantuv", "obtener": "obtuv", "contener": "contuv",
    "imponer": "impus", "descomponer": "descompus", "posponer": "pospus", "proponer": "propus", "suponer": "supus", "componer": "compus",
    "deshacer": "deshic", "satisfacer": "satisfic", "contraer": "contraj", "atraer": "atraj",
    "predecir": "predij", "convenir": "convin", "prevenir": "previn",
    "provenir": "provin", "intervenir": "intervin", "disponer": "dispus", "exponer": "expus", "oponer": "opus",
    "retener": "retuv", "sostener": "sostuv", "entretener": "entretuv", "distraer": "distraj", "reproducir": "reproduj",
    "rehacer": "rehic", "contradecir": "contradij", "bendecir": "bendij", "maldecir": "maldij",
}
PRET_STEM_IR = {  # -ir verbs: the vowel changes in the usted and ustedes forms only
    "pedir": "i", "servir": "i", "repetir": "i", "vestir": "i", "seguir": "i", "conseguir": "i",
    "preferir": "i", "sentir": "i", "mentir": "i", "sugerir": "i", "advertir": "i", "divertir": "i",
    "competir": "i", "invertir": "i", "elegir": "i", "despedir": "i", "dormir": "u", "morir": "u", "convertir": "i", "divertir": "i", "perseguir": "i",
    "adherir": "i", "desmentir": "i", "consentir": "i", "revertir": "i", "embestir": "i", "conferir": "i", "referir": "i", "herir": "i",
}


def _pret_regular(verb):
    stem, end = verb[:-2], verb[-2:]
    if end == "ar":
        f = [stem + e for e in ["é", "aste", "ó", "amos", "asteis", "aron"]]
        if stem.endswith("c"):
            f[0] = stem[:-1] + "qué"
        elif stem.endswith("g"):
            f[0] = stem + "ué"
        elif stem.endswith("z"):
            f[0] = stem[:-1] + "cé"
        return f
    f = [stem + e for e in ["í", "iste", "ió", "imos", "isteis", "ieron"]]
    if stem[-1] in "aeoáéíóú" or verb.endswith("uir"):   # leer, creer, caer, oír, construir ...
        if verb.endswith("uir") and not stem.endswith("g"):
            f = [stem + "í", stem + "iste", stem + "yó", stem + "imos", stem + "isteis", stem + "yeron"]
        else:
            f = [stem + "í", stem + "íste", stem + "yó", stem + "ímos", stem + "ísteis", stem + "yeron"]
        f[0] = stem + "í"
        if verb.endswith("uir"):
            f[1], f[3], f[4] = stem + "iste", stem + "imos", stem + "isteis"
    if verb == "huir":
        f[0] = "hui"     # one syllable: no written accent
    if verb in PRET_STEM_IR:
        v = PRET_STEM_IR[verb]
        i = stem.rfind("e" if v == "i" else "o")
        st = stem[:i] + ("i" if v == "i" else "u") + stem[i + 1:]
        if verb == "seguir" or verb == "conseguir" or verb == "elegir":
            pass
        f[2] = st + "ió"
        f[5] = st + "ieron"
    return f


def pret_paradigm(verb):
    if verb in PRET_IRREG:
        return PRET_IRREG[verb]
    if verb in PRET_STEM:
        st = PRET_STEM[verb]
        f = [st + e for e in _PRET_E]
        if st.endswith("j"):
            f[5] = st + "eron"
        if verb in ("hacer", "deshacer", "satisfacer"):
            f[2] = st[:-1] + "z" + "o"
        return f
    if verb[-2:] not in _ENDS:
        return None
    return _pret_regular(verb)


def cmd_paradigm(verb):
    """[None, None, usted, None, None, ustedes] for the formal commands."""
    special = {"dar": ("dé", "den"), "ir": ("vaya", "vayan"), "ser": ("sea", "sean"),
               "estar": ("esté", "estén"), "saber": ("sepa", "sepan")}
    if verb in special:
        u, uu = special[verb]
        return [None, None, u, None, None, uu]
    yo = paradigm(verb, "pres")[0]
    if not yo.endswith("o"):
        return None
    stem = yo[:-1]
    if verb.endswith("ar"):
        if verb.endswith("car"):
            stem = stem[:-1] + "qu"
        elif verb.endswith("gar"):
            stem = stem + "u"
        elif verb.endswith("zar"):
            stem = stem[:-1] + "c"
        return [None, None, stem + "e", None, None, stem + "en"]
    return [None, None, stem + "a", None, None, stem + "an"]


# --- Unit 16-18 additions: the imperfect and the past participle

IMPF_IRREG = {
    "ir": ["iba", "ibas", "iba", "íbamos", "ibais", "iban"],
    "ser": ["era", "eras", "era", "éramos", "erais", "eran"],
    "ver": ["veía", "veías", "veía", "veíamos", "veíais", "veían"],
}
PART_IRREG = {
    "abrir": "abierto", "cubrir": "cubierto", "descubrir": "descubierto", "encubrir": "encubierto",
    "escribir": "escrito", "describir": "descrito", "inscribir": "inscrito", "hacer": "hecho",
    "deshacer": "deshecho", "satisfacer": "satisfecho", "morir": "muerto", "poner": "puesto",
    "componer": "compuesto", "proponer": "propuesto", "suponer": "supuesto", "romper": "roto",
    "ver": "visto", "prever": "previsto", "volver": "vuelto", "devolver": "devuelto",
    "resolver": "resuelto", "decir": "dicho", "freír": "frito", "imprimir": "impreso",
    "imponer": "impuesto", "exponer": "expuesto", "disponer": "dispuesto", "oponer": "opuesto", "posponer": "pospuesto",
    "reponer": "repuesto", "descomponer": "descompuesto", "contradecir": "contradicho", "predecir": "predicho",
    "rehacer": "rehecho", "envolver": "envuelto", "disolver": "disuelto", "absolver": "absuelto", "revolver": "revuelto",
    "reabrir": "reabierto", "entreabrir": "entreabierto", "transcribir": "transcrito", "suscribir": "suscrito",
    "prescribir": "prescrito", "proscribir": "proscrito", "cubrir": "cubierto", "encubrir": "encubierto",
    "proveer": "provisto", "entrever": "entrevisto", "mantener": None,
    "ir": "ido", "ser": "sido", "oír": "oído", "reír": "reído", "sonreír": "sonreído",
}
PART_IRREG.pop("mantener", None)


def impf_paradigm(verb):
    if verb in IMPF_IRREG:
        return IMPF_IRREG[verb]
    if verb[-2:] not in _ENDS:
        return None
    stem = verb[:-2]
    if verb.endswith("ar"):
        return [stem + e for e in ["aba", "abas", "aba", "ábamos", "abais", "aban"]]
    return [stem + e for e in ["ía", "ías", "ía", "íamos", "íais", "ían"]]


def participle(verb):
    if verb in PART_IRREG:
        return PART_IRREG[verb]
    if verb[-2:] not in _ENDS:
        return None
    stem, end = verb[:-2], verb[-2:]
    if end == "ar":
        return stem + "ado"
    if stem[-1] in "aeoáéíóú":      # leer, creer, caer, traer, oír, reír
        return stem + "ído"
    return stem + "ido"


def vpi(verb, *forms):
    """Same as vp, for the imperfect."""
    return [(verb, i, f, "impf") for i, f in enumerate(forms) if f is not None]


def vpa(verb, form):
    """Same as vp, for the past participle (masculine singular)."""
    return [(verb, 0, form, "part")]


# --- Unit 21-24 additions: the conditional, informal and nosotros/vosotros/vos commands

def _fut_base(verb):
    if verb in FUT_STEM:
        return FUT_STEM[verb]
    c = _compound(verb)
    if c and c[1] in FUT_STEM:
        return c[0] + FUT_STEM[c[1]]
    return verb


def cond_paradigm(verb):
    base = _fut_base(verb)
    return [base + e for e in ["ía", "ías", "ía", "íamos", "íais", "ían"]]


T_CMD_IRREG = {"decir": "di", "hacer": "haz", "ir": "ve", "poner": "pon", "salir": "sal",
               "ser": "sé", "tener": "ten", "venir": "ven"}
T_NEG_IRREG = {"dar": "des", "ir": "vayas", "ser": "seas", "estar": "estés", "saber": "sepas"}
N_CMD_SPECIAL = {"ser": "seamos", "estar": "estemos", "dar": "demos", "ir": "vayamos", "saber": "sepamos",
                 "ver": "veamos", "reír": "riamos"}
N_CMD_IR = {"dormir": "durmamos", "morir": "muramos", "pedir": "pidamos", "repetir": "repitamos",
            "sentir": "sintamos", "servir": "sirvamos", "seguir": "sigamos", "elegir": "elijamos",
            "vestir": "vistamos", "divertir": "divirtamos", "preferir": "prefiramos", "mentir": "mintamos",
            "conseguir": "consigamos", "competir": "compitamos", "sugerir": "sugiramos",
            "advertir": "advirtamos", "convertir": "convirtamos"}


def tcmd_paradigm(verb):
    """Affirmative tú command (index 1)."""
    if verb in T_CMD_IRREG:
        f = T_CMD_IRREG[verb]
    else:
        p = paradigm(verb, "pres")
        if p is None:
            return None
        f = p[2]
    return [None, f, None, None, None, None]


def ntcmd_paradigm(verb):
    """Negative tú command (index 1)."""
    if verb in T_NEG_IRREG:
        return [None, T_NEG_IRREG[verb], None, None, None, None]
    c = cmd_paradigm(verb)
    if c is None:
        return None
    return [None, c[2] + "s", None, None, None, None]


def ncmd_paradigm(verb):
    """Nosotros command (index 3)."""
    if verb in N_CMD_SPECIAL:
        f = N_CMD_SPECIAL[verb]
    elif verb in N_CMD_IR:
        f = N_CMD_IR[verb]
    else:
        c = cmd_paradigm(verb)
        if c is None:
            return None
        yo = paradigm(verb, "pres")[0]
        if yo.endswith(("go", "zco", "yo", "oy")) and not verb.endswith("gar"):
            f = c[2] + "mos"
        else:
            stem, end = verb[:-2], verb[-2:]
            if end == "ar":
                if verb.endswith("car"):
                    stem = stem[:-1] + "qu"
                elif verb.endswith("gar"):
                    stem = stem + "u"
                elif verb.endswith("zar"):
                    stem = stem[:-1] + "c"
                f = stem + "emos"
            else:
                if verb.endswith(("ger", "gir")):
                    stem = stem[:-1] + "j"
                elif verb.endswith("guir"):
                    stem = stem[:-1]
                elif verb.endswith(("cer", "cir")):
                    stem = stem[:-1] + "z"
                f = stem + "amos"
    return [None, None, None, f, None, None]


def vcmd_paradigm(verb):
    """Affirmative vosotros command (index 4)."""
    if verb[-2:] not in _ENDS:
        return None
    return [None, None, None, None, verb[:-1] + "d", None]


def nvcmd_paradigm(verb):
    """Negative vosotros command (index 4)."""
    if verb == "dar":
        return [None, None, None, None, "deis", None]
    n = ncmd_paradigm(verb)
    if n is None:
        return None
    f = n[3]
    return [None, None, None, None, f[:-4] + ("éis" if f.endswith("emos") else "áis"), None]


def voscmd_paradigm(verb):
    """Affirmative vos command (index 4)."""
    if verb[-2:] not in _ENDS:
        return None
    return [None, None, None, None, verb[:-2] + {"ar": "á", "er": "é", "ir": "í"}[verb[-2:]], None]


def _vp(mode, idx):
    def f(verb, form):
        return [(verb, idx, form, mode)]
    return f


vpt = _vp("tcmd", 1)        # tú, affirmative
vptn = _vp("ntcmd", 1)      # tú, negative
vpn = _vp("ncmd", 3)        # nosotros command
vpv = _vp("vcmd", 4)        # vosotros, affirmative
vpvn = _vp("nvcmd", 4)      # vosotros, negative
vps = _vp("voscmd", 4)      # vos, affirmative


def vpd(verb, *forms):
    """Same as vp, for the conditional."""
    return [(verb, i, f, "cond") for i, f in enumerate(forms) if f is not None]


_COMPOUND_BASES = ("tener", "venir", "poner", "traer")


def _compound(verb):
    """(prefix, base) for compounds like mantener, convenir, proponer, atraer; else None."""
    for b in _COMPOUND_BASES:
        if verb.endswith(b) and verb != b:
            return verb[:-len(b)], b
    return None


def paradigm(verb, mode="pres"):
    if mode == "cond":
        return cond_paradigm(verb)
    if mode in _MODE_FN:
        return _MODE_FN[mode](verb)
    if mode == "part":
        pp = participle(verb)
        return [pp] * 6 if pp else None
    if mode == "impf":
        return impf_paradigm(verb)
    if mode == "pret":
        return pret_paradigm(verb)
    if mode == "cmd":
        return cmd_paradigm(verb)
    if mode == "fut":
        base = _fut_base(verb)
        return [base + e for e in _FUT_END]
    if verb in IRREG:
        return IRREG[verb]
    c = _compound(verb)
    if c and c[1] in IRREG:
        return [c[0] + f for f in IRREG[c[1]]]
    if verb[-2:] not in _ENDS:
        return None
    stem = verb[:-2]
    f = [stem + e for e in _ENDS[verb[-2:]]]
    # -cer / -cir after a vowel: yo form ends in -zco (conocer, ofrecer, traducir ...)
    if verb not in _NOZCO and len(verb) > 4 and verb[-3:] in ("cer", "cir") and verb[-4] in "aeiouáéíóú":
        f[0] = stem[:-1] + "zco"
    elif verb not in _NOZCO and len(verb) > 4 and verb[-3:] in ("cer", "cir") and verb[-4] not in "aeiouáéíóú":
        f[0] = stem[:-1] + "zo"            # vencer → venzo, convencer → convenzo
    if verb.endswith(("ger", "gir")):      # proteger → protejo, dirigir → dirijo
        f[0] = stem[:-1] + "jo"
    return f


_MODE_FN = {"tcmd": tcmd_paradigm, "ntcmd": ntcmd_paradigm, "ncmd": ncmd_paradigm,
            "vcmd": vcmd_paradigm, "nvcmd": nvcmd_paradigm, "voscmd": voscmd_paradigm}


# --- Unit 26-30 additions: the present subjunctive (all six persons)

N_CMD_IR.update({"referir": "refiramos", "herir": "hiramos", "hervir": "hirvamos", "consentir": "consintamos",
                 "invertir": "invirtamos", "impedir": "impidamos", "medir": "midamos", "despedir": "despidamos",
                 "corregir": "corrijamos", "reñir": "riñamos", "sonreír": "sonriamos", "freír": "friamos"})
N_CMD_IR["herir"] = "hiramos"
N_CMD_IR["hervir"] = "hirvamos"


def subj_paradigm(verb):
    """Present subjunctive: yo, tú, él, nosotros, vosotros, ellos."""
    if verb == "haber":
        return ["haya", "hayas", "haya", "hayamos", "hayáis", "hayan"]
    c, t, n, v = cmd_paradigm(verb), ntcmd_paradigm(verb), ncmd_paradigm(verb), nvcmd_paradigm(verb)
    if None in (c, t, n, v):
        return None
    return [c[2], t[1], c[2], n[3], v[4], c[5]]


_MODE_FN["subj"] = subj_paradigm


def vpj(verb, *forms):
    """Same as vp, for the present subjunctive (yo, tú, él, nosotros, vosotros, ellos)."""
    return [(verb, i, f, "subj") for i, f in enumerate(forms) if f is not None]


# --- Unit 31-35 additions: the imperfect subjunctive (-ra forms and -se forms)

_ACC = {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú"}


def _isubj_stem(verb):
    if verb == "haber":
        return "hubie"
    p = pret_paradigm(verb)
    if p is None or not p[5] or not p[5].endswith("ron"):
        return None
    return p[5][:-3]


def isubj_paradigm(verb):
    """Imperfect subjunctive, -ra forms: yo, tú, él, nosotros, vosotros, ellos."""
    st = _isubj_stem(verb)
    if st is None:
        return None
    nos = st[:-1] + _ACC.get(st[-1], st[-1])
    return [st + "ra", st + "ras", st + "ra", nos + "ramos", st + "rais", st + "ran"]


def isubj_se_paradigm(verb):
    """Imperfect subjunctive, -se forms."""
    st = _isubj_stem(verb)
    if st is None:
        return None
    nos = st[:-1] + _ACC.get(st[-1], st[-1])
    return [st + "se", st + "ses", st + "se", nos + "semos", st + "seis", st + "sen"]


_MODE_FN["isubj"] = isubj_paradigm
_MODE_FN["isubjse"] = isubj_se_paradigm


def vpq(verb, *forms):
    """Same as vp, for the imperfect subjunctive -ra forms (yo, tú, él, nosotros, vosotros, ellos)."""
    return [(verb, i, f, "isubj") for i, f in enumerate(forms) if f is not None]


def vpqs(verb, *forms):
    """Same as vp, for the imperfect subjunctive -se forms."""
    return [(verb, i, f, "isubjse") for i, f in enumerate(forms) if f is not None]


def person_form(verb, who, mode="pres"):
    """The form of verb for person 'who' (a PERSON_IDX key, 'vos', or 'ger')."""
    if who == "ger":
        return gerund(verb)
    if who == "part":
        return participle(verb)
    if who == "vos" and mode == "pres":
        return _vos(verb)
    p = paradigm(verb, mode)
    if p is None or who not in PERSON_IDX:
        return None
    return p[PERSON_IDX[who]]


# ------------------------------------------------------------------ data for checks

WORD = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")


def load_wiktionary_es(path):
    """lemma -> set of forms; all Spanish forms; form -> set of lemmas;
    and the set of words that occur in the English glosses."""
    lemma_forms, all_forms = defaultdict(set), set()
    form_lemmas = defaultdict(set)
    eng = set()
    tag = re.compile(r"<[^>]+>")
    for line in open(path, encoding="utf-8"):
        head, _, gloss = line.partition("\t")
        parts = [p.strip() for p in head.split("|")]
        parts = [p for p in parts if p]
        if not parts:
            continue
        lemma = parts[0].lower()
        for f in parts:
            for w in WORD.findall(f):
                all_forms.add(w.lower())
            fl = f.lower()
            lemma_forms[lemma].add(fl)
            form_lemmas[fl].add(lemma)
            # multi-word headwords also give their words
        for w in WORD.findall(tag.sub(" ", gloss)):
            eng.add(w.lower())
    return lemma_forms, all_forms, form_lemmas, eng


def load_genders(path):
    """surface noun -> set of 'm'/'f' (best effort, from the doozan/Wiktionary data)."""
    g = defaultdict(set)
    if not os.path.exists(path):
        return g
    cur, pos = None, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line == "_____":
            cur, pos = None, None
            continue
        if cur is None:
            cur = line.strip().lower()
            continue
        if line.startswith("pos:"):
            pos = line[4:].strip()
        elif line.startswith("  g:") and pos == "n":
            for tok in re.findall(r"[a-z]+", line[4:]):
                if tok.startswith("mf"):
                    g[cur].update("mf")
                elif tok == "m":
                    g[cur].add("m")
                elif tok == "f":
                    g[cur].add("f")
    return g


# ------------------------------------------------------------------ checks

ARTICLES = {"el": "m", "un": "m", "los": "m", "unos": "m",
            "la": "f", "una": "f", "las": "f", "unas": "f"}

# Feminine nouns that take el/un in the singular (stressed initial a-).
EL_FEM = {"agua", "aula", "alma", "área", "arma", "águila", "hambre", "hada", "ala", "ama",
          "asa", "aya", "arpa", "acta", "ansia", "ave", "hacha", "habla"}

COMMON_GENDER = {"dependiente", "cliente", "estudiante", "periodista", "artista", "joven", "guía", "intérprete",
                 "presidente", "gerente", "representante", "turista", "dentista", "electricista", "policía",
                 "cantante", "taxista", "colega", "testigo", "pianista", "adolescente", "residente", "agente"}

# Words that are fine anywhere: names, abbreviations quoted in explanations,
# fragments such as endings, and a few forms the dictionary files elsewhere.
ALLOW = {
    "salespeople", "shopper", "shoppers",
    "on", "under", "outside", "top", "my", "our", "fem", "masc", "tonight", "this", "that", "these", "those", "near", "over", "there", "farthest", "you", "one", "feminine",
    # names
    "andrea", "aristide", "bertrand", "noriega", "columbus", "gardel", "unesco", "lupe", "fidel", "fulgencio", "menchú", "porfirio", "rigoberta", "toño", "martin", "luther", "king", "kennedy", "john", "mahatma", "sarajevo", "memphis", "dallas", "gandhi", "debayle", "bernardo", "albizu", "somoza", "duarte", "anastasio", "morazán", "higgins", "martí", "hidalgo", "bolívar", "perón", "evita", "juárez", "benito", "miranda", "morales", "evo",
    "pedro", "pedrito", "rosa", "elena", "juan", "carmela", "victoria", "enrique", "maría", "maria",
    "luis", "ana", "carlos", "josé", "jose", "lucía", "lucia", "paco", "lorenzo", "alicia", "miranda",
    "daniel", "claudia", "lisa", "marta", "pablo", "sofía", "sofia", "laura", "rodrigo", "gómez",
    "lópez", "garcía", "pérez", "sánchez", "fernández", "martínez", "rodríguez", "moreno", "ramos",
    "santos", "torres", "ortega", "rivera", "castillo", "mendoza", "vargas", "ruiz", "díaz",
    "alberto", "susana", "francisco", "isabel", "fernando", "antonio", "mariana", "joaquín",
    "mercedes", "ramón", "tomás", "sebastián", "emilio", "raúl", "julia", "josefina", "miguel",
    "javier", "diego", "frida", "gabriela", "andrés", "beatriz", "camila", "mateo", "valentina",
    "hugo", "alba", "eva", "inés", "óscar", "nuria", "sara", "iván", "lola", "manuel", "teresa",
    "cecilia", "gloria", "felipe", "cristina", "roberto", "marcos", "silvia", "ricardo", "irene",
    "esteban", "ernesto", "patricia", "adela", "dolores", "olga", "héctor", "ignacio", "ángel",
    "yolanda", "sergio", "amparo", "nico", "jaime", "lorena", "paula", "natalia", "alejandro",
    "guillermo", "lucas", "bruno", "leonor", "pilar", "rafael", "yoli", "levi", "diane", "zaragoza",
    # abbreviations and fragments quoted in explanations
    "ud", "uds", "sr", "sra", "srta", "dr", "dra", "pm", "am", "etc", "vd", "vds",
    "ar", "er", "ir", "ando", "iendo", "ado", "ido", "ón", "ión", "ción", "ad", "ud", "nte", "ista",
    "ez", "ito", "ita", "ísimo", "ma", "es", "ces", "mente", "ico", "ica", "dad", "tad", "ura",
    "or", "ora", "án", "ín", "ona", "ino", "ina", "ísima", "illo", "illa", "ero", "era", "ez",
    "ces", "eis", "ais",
    # Units 16-18: people and places in the readings
    "picasso", "bolívar", "neruda", "cervantes", "hidalgo", "juárez", "perón", "evita", "kahlo", "márquez",
    "aracataca", "martí", "cusco", "machu", "picchu", "tikal", "copán", "chichén", "itzá", "palenque",
    "tenochtitlán", "texcoco", "ayllu", "ayllus", "quipu", "quipus", "qhapaq", "ñan", "tlatoani", "málaga",
    "oviedo", "parral", "coyoacán", "guelatao", "morazán", "alonso", "caracas", "oaxaca", "toldos",
    "gerardo", "maricela", "mauricio", "omar", "temuco", "memoirs", "fled", "slept", "took", "grew", "knew", "rang", "quijote", "mesoamérica", "morales", "evo", "benito", "simón", "colón", "cristóbal", "mexicas",
    # place names and demonyms Wiktionary files under capitals
    "méxico", "españa", "perú", "colombia", "argentina", "chile", "cuba", "bolivia", "ecuador",
    "venezuela", "uruguay", "paraguay", "honduras", "nicaragua", "panamá", "guatemala",
    "salvador", "costa", "rica", "puerto", "república", "dominicana", "guinea", "ecuatorial",
    "madrid", "bogotá", "lima", "quito", "caracas", "managua", "montevideo", "asunción",
    "tegucigalpa", "malabo", "habana", "paz", "santiago", "buenos", "aires", "san", "josé",
    "juan", "ciudad", "santo", "domingo", "sucre", "brasil", "estados", "unidos", "europa",
    "américa", "centroamérica", "sudamérica", "norteamérica", "caribe", "áfrica", "sevilla",
    "barcelona", "valencia", "cali", "monterrey", "california", "texas", "florida", "colorado",
    "mexicana", "mexicano", "cervantes", "neruda", "bolívar", "picasso", "shakira", "kahlo",
    "iglesias", "banderas", "bardem", "cruz", "penélope", "isabel", "castilla", "andalucía",
    "chiapas", "guadalajara", "barranquilla", "líbano", "roma", "israel", "paris", "parís",
    "alemania", "francia", "inglaterra", "italia", "japón", "china", "rusia", "canadá",
    "inglés", "inglesa", "estadounidense", "dli", "ee", "uu", "tv", "pc", "dvd", "ok",
    "wifi", "email", "internet", "ipad", "iphone", "bookwidgets", "ucat", "quizlet",
    "goldman", "tanya", "chacaltaya", "aconcagua", "berta", "cáceres", "lenca", "lencas", "copinh", "márquez", "valdivia", "darwin", "iberá", "beagle", "crispr", "doudna", "charpentier", "gualcarque", "cauca", "pascua", "rapa", "nui", "chiloé", "lesseps", "suez", "agua", "zarca", "maría", "irma", "mitch", "nobel", "tlatelolco", "galápagos", "riñihue", "tikal", "titicaca", "iguazú", "atacama", "nicaragua", "belice", "mismi", "gualcarque", "cop", "ia", "emmanuelle", "jennifer", "aldrin", "armstrong", "curiosity", "edwin", "gagarin", "neil", "sputnik", "tereshkova", "yuri", "marte", "hans", "pierre", "astra", "godparent", "godparents", "niece", "nephew", "habl", "éis", "estudi", "com", "viv", "ís", "eca", "ense", "eña", "eño", "ño", "ous", "tion", "ty", "negates", "ortiz", "mr", "mrs", "blo", "blan", "blar", "sas", "ciu", "veinti", "nta", "dieci", "nueve", "petra", "monterey", "cambrils", "rambla", "farc", "askatasuna", "euskadi", "eln", "auc", "epl", "guzmán", "abimael", "bacrim", "mara", "maras",
}

# English words the gloss-derived vocabulary may lack.
ALLOW_EN = {
    "cir", "uir", "zco", "esse", "ucir", "uzco", "guir", "vo", "safest",
    "ndo", "rá", "fahrenheit", "cabr", "dir", "habr", "podr", "pondr", "querr", "sabr", "saldr", "tendr", "valdr", "vendr",
    "ser", "usted", "ustedes", "hie", "cincocientos", "nuevecientos", "sietecientos", "tú", "vos", "vosotros", "feminine", "masculine", "gloss", "ie",
    "eg", "vs", "ok", "yall", "cognate", "cognates", "gender", "plural", "singular", "ve", "ll",
    "don", "isn", "aren", "doesn", "didn", "won", "can", "hasn", "haven", "wasn", "weren", "couldn",
    "wouldn", "shouldn", "re", "d", "s", "t", "m", "o", "e", "u", "y", "a", "i", "x", "n", "r", "l",
    "tap", "tapped", "tapping", "quiz", "app", "listen", "lesson", "lessons", "worksheet", "wifi",
    "airman", "airmen", "marines", "marine", "mornings", "afternoon", "evenings", "websites",
    "spelled", "spelling", "unstressed", "stressed", "syllable", "syllables", "pronounce",
    "pronounced", "pronunciation", "infinitive", "infinitives", "conjugate", "conjugated",
    "conjugation", "conjugations", "vowel", "vowels", "consonant", "consonants", "suffix",
    "suffixes", "prefix", "apostrophe", "accent", "accents", "hyphen", "paradigm", "adjectives",
    "adjective", "nouns", "noun", "pronoun", "pronouns", "verbs", "verb", "preposition",
    "prepositions", "article", "articles", "conjunction", "conjunctions", "interrogative",
    "demonstrative", "demonstratives", "possessive", "possessives", "ordinal", "ordinals",
    "cardinal", "cardinals", "periphrastic", "impersonal", "irregular", "regular", "reflexive",
    "agreement", "agree", "agrees", "agreeing", "contraction", "contracts", "masculines",
    "feminines", "formal", "informal", "familiar", "colloquial", "ll", "gonna", "wanna", "okay",
    "cognate", "mnemonic", "hispanic", "latino", "latina", "caribbean", "spanish", "spain",
    "mexican", "american", "english", "european", "colombian", "peruvian", "cuban", "chilean",
    "argentine", "argentinian", "venezuelan", "ecuadorian", "bolivian", "uruguayan", "paraguayan",
    "honduran", "salvadoran", "guatemalan", "nicaraguan", "costa", "rican", "panamanian",
    "dominican", "puerto", "equatorial", "guinean", "guinea", "america", "americas", "latin",
    "dli", "retired", "unemployed", "smartphone", "email", "online", "wifi", "ad", "ads",
}

NUMBER_WORDS = {"cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
                "once", "doce", "trece", "catorce", "quince", "veinte", "treinta", "cuarenta", "cincuenta",
                "sesenta", "setenta", "ochenta", "noventa", "cien", "ciento", "mil", "millón", "millones"}

ABBR = re.compile(r"\b(Sr|Sra|Srta|Ud|Uds|Dr|Dra|Vd|Vds|etc|pág)\.", re.I)
QUESTION_NOACCENT = re.compile(
    r"¿\s*(?:(?:de|a|en|por|para|con|desde|hasta|hacia)\s+)?"
    r"(como|que|cual|cuales|quien|quienes|cuando|donde|adonde|cuanto|cuanta|cuantos|cuantas)\b",
    re.I)
_PUNCT_STRIP = "{}"


def english_ok(w, eng):
    """True if w, or w with a common English ending removed, is an English word."""
    if w in eng:
        return True
    for suf, rep in (("ies", "y"), ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"), ("d", ""),
                     ("ing", ""), ("ing", "e"), ("ly", ""), ("er", ""), ("ers", ""), ("ised", "ize"),
                     ("ise", "ize"), ("ised", "e"), ("ised", "")):
        if w.endswith(suf) and (w[:-len(suf)] + rep) in eng:
            return True
    for suf in ("ing", "ed", "er", "s"):
        if w.endswith(suf) and len(w) > len(suf) + 2 and w[-len(suf) - 1] == w[-len(suf) - 2] \
                and w[:-len(suf) - 1] in eng:
            return True
    return False


def _nfc(s):
    return unicodedata.normalize("NFC", s)


def clean(s):
    return s.replace("{", "").replace("}", "")


def singulars(w):
    """Candidate singular forms of a surface noun, for the gender lookup."""
    out = [w]
    if w.endswith("ces"):
        out.append(w[:-3] + "z")
    if w.endswith("es"):
        out.append(w[:-2])
    if w.endswith("s"):
        out.append(w[:-1])
    return out


def check_es(app, meta, deck_rank, wk, genders):
    errors, warns, info = [], [], []
    lemma_forms, all_forms, form_lemmas, eng = wk if wk else ({}, set(), {}, set())
    have_wk = bool(wk)

    def spanish_only(m):
        """(label, text) pairs that must be pure Spanish."""
        L, bag = m["src"], []
        for c in L["cards"]:
            for e in c["examples"]:
                bag.append(("example", e["text"]))
            for t in c["tables"]:
                for r in t["rows"]:
                    for i in t.get("speakCols", []) or []:
                        if i < len(r):
                            bag.append(("table", r[i]))
        for q in L["exercises"]:
            if q["kind"] == "fillBlank":
                bag.append(("blank", q["prompt"]))
        return bag

    def mixed(m):
        """Text that may mix English and Spanish."""
        L, bag = m["src"], []
        for c in L["cards"]:
            bag += [c["title"], c["body"]]
            for t in c["tables"]:
                bag += t["headers"]
                if t.get("title"):
                    bag.append(t["title"])
                if t.get("note"):
                    bag.append(t["note"])
                sp = set(t.get("speakCols", []) or [])
                for r in t["rows"]:
                    bag += [x for i, x in enumerate(r) if i not in sp]
            for e in c["examples"]:
                bag.append(e["translation"])
        for q in L["exercises"]:
            if q["kind"] == "multipleChoice":
                bag.append(q["prompt"])
            bag += [q["answer"], q["why"]]
            if q["tr"]:
                bag.append(q["tr"])
        return bag

    def all_text(m):
        L, bag = m["src"], []
        for c in L["cards"]:
            bag += [c["title"], c["body"]]
            for e in c["examples"]:
                bag += [e["text"], e["translation"]]
            for t in c["tables"]:
                bag += t["headers"] + [x for r in t["rows"] for x in r]
                bag += [t.get("title") or "", t.get("note") or ""]
        for q in L["exercises"]:
            bag += [q["prompt"], q["answer"], q["why"], q["tr"] or ""]
        return bag

    seen_titles = set()
    for m in meta:
        L, lid = m["src"], m["id"]
        tag = f"{lid} ({L['title']})"
        if L["title"] in seen_titles:
            warns.append(f"{tag}: duplicate lesson title")
        seen_titles.add(L["title"])

        # --- structure
        if not 5 <= len(L["exercises"]) <= 12:
            warns.append(f"{tag}: {len(L['exercises'])} exercises")
        for k, q in enumerate(L["exercises"], 1):
            if not 2 <= len(q["options"]) <= 4:
                errors.append(f"{tag} e{k}: {len(q['options'])} options")
            if q["kind"] == "fillBlank" and q["prompt"].count("___") != 1:
                errors.append(f"{tag} e{k}: fill-blank needs exactly one ___")
            if q["answer"] not in q["options"]:
                errors.append(f"{tag} e{k}: answer not among options")
        for c in L["cards"]:
            for e in c["examples"]:
                if "highlight" in e and e["highlight"] not in e["text"]:
                    errors.append(f"{tag}: highlight {e['highlight']!r} not in {e['text']!r}")
            for t in c["tables"]:
                sp = t.get("speakCols")
                if sp is None:
                    warns.append(f"{tag}: table {t.get('title') or t['headers']} has no say=[...] columns")
                else:
                    for i in sp:
                        if not 0 <= i < len(t["headers"]):
                            errors.append(f"{tag}: speakCols {i} outside table")
                for r in t["rows"]:
                    if len(r) != len(t["headers"]):
                        errors.append(f"{tag}: table row {r} has {len(r)} cells, header has {len(t['headers'])}")
                    for cell in r:
                        if cell.count("{") != cell.count("}"):
                            errors.append(f"{tag}: unbalanced braces in {cell!r}")

        # --- encoding hygiene
        for text in all_text(m) + [o for q in L["exercises"] for o in q["options"]]:
            if _nfc(text) != text:
                errors.append(f"{tag}: text is not NFC-normalised: {text[:40]!r}")
            if re.search("[Ѐ-ӿ]", text):
                errors.append(f"{tag}: Cyrillic letter in {text[:40]!r}")
            if "́" in text:
                errors.append(f"{tag}: combining accent in {text[:40]!r}")

        # --- gating
        ranks = []
        for w in L["requires"]:
            if w not in deck_rank:
                errors.append(f"{tag}: requiredLemma {w!r} is not in the deck")
            else:
                ranks.append(deck_rank[w])
        info.append(f"{lid}  unlock words: {len(ranks)}/{len(L['requires'])} in deck, "
                    f"ranks {sorted(ranks)}")

        # --- punctuation
        spoken = spanish_only(m)
        for label, text in spoken + [("answer", q["answer"]) for q in L["exercises"]]:
            t = clean(text)
            if t.count("¿") != t.count("?"):
                errors.append(f"{tag}: unbalanced ¿ ? in {label}: {t[:60]!r}")
            if t.count("¡") != t.count("!"):
                errors.append(f"{tag}: unbalanced ¡ ! in {label}: {t[:60]!r}")
        for text in all_text(m):
            if QUESTION_NOACCENT.search(text):
                errors.append(f"{tag}: interrogative without accent: {text[:70]!r}")
            if text.count("¿") > text.count("?"):
                errors.append(f"{tag}: ¿ without ?: {text[:70]!r}")
        for label, text in spoken:
            if ABBR.search(text):
                warns.append(f"{tag}: abbreviation in spoken {label}: {text[:50]!r}")
            if re.search(r"\d", text):
                warns.append(f"{tag}: digit in spoken {label}: {text[:50]!r}")
            if "/" in text:
                warns.append(f"{tag}: slash in spoken {label}: {text[:50]!r}")

        # --- gender of article + noun (best effort)
        if genders:
            seen = set()
            short_answers = [q["answer"] for q in L["exercises"] if len(q["answer"].split()) <= 4]
            for label, text in spoken + [("answer", t) for t in short_answers]:
                for part in clean(text).split("___"):
                  toks = WORD.findall(part)
                  for a, n in zip(toks, toks[1:]):
                      al, nl = a.lower(), n.lower()
                      if al not in ARTICLES or nl in ARTICLES:
                          continue
                      if nl in EL_FEM and al in ("el", "un"):
                          continue
                      if nl in NUMBER_WORDS or nl in COMMON_GENDER:
                          continue
                      want = ARTICLES[al]
                      found = set()
                      for cand in singulars(nl):
                          found |= genders.get(cand, set())
                      if found and want not in found and (al, nl) not in seen:
                          seen.add((al, nl))
                          warns.append(f"{tag}: gender? '{a} {n}' (noun is {'/'.join(sorted(found))})")

        if not have_wk:
            continue

        # --- spelling: Spanish-only text
        unknown = set()
        for label, text in spoken:
            for w in WORD.findall(clean(text)):
                lw = w.lower()
                if lw in ALLOW or lw in all_forms:
                    continue
                unknown.add(lw)
        for w in sorted(unknown):
            warns.append(f"{tag}: not a known Spanish word form: {w}")

        # --- spelling: mixed text must be Spanish or English
        unknown = set()
        for text in mixed(m):
            for w in WORD.findall(clean(text)):
                lw = w.lower()
                if lw in ALLOW or lw in ALLOW_EN or lw in all_forms or english_ok(lw, eng):
                    continue
                unknown.add(lw)
        for w in sorted(unknown):
            warns.append(f"{tag}: not Spanish or English: {w}")

        # --- morphology
        for item in L["verify"]:
            if len(item) == 2:
                lem, form = item
                lf = lemma_forms.get(lem.lower())
                if lf is None:
                    warns.append(f"{tag}: verify: {lem!r} is not a dictionary headword")
                elif form.lower() not in lf:
                    errors.append(f"{tag}: {form!r} is not a form of {lem!r}")
            else:
                verb, idx, form = item[:3]
                mode = item[3] if len(item) > 3 else "pres"
                p = paradigm(verb, mode)
                if p is None:
                    errors.append(f"{tag}: no paradigm for {verb!r}")
                elif p[idx] != form:
                    errors.append(f"{tag}: {verb} person {idx} ({mode}): table says {form!r}, paradigm {p[idx]!r}")
                lf = lemma_forms.get(verb)
                if lf is not None and form.lower() not in lf:
                    errors.append(f"{tag}: {form!r} is not in the dictionary entry for {verb!r}")
        for k, q in enumerate(L["exercises"], 1):
            if not 2 <= len(q["options"]) <= 4:
                errors.append(f"{tag} e{k}: {len(q['options'])} options")
            if q["kind"] == "fillBlank" and q["prompt"].count("___") != 1:
                errors.append(f"{tag} e{k}: fill-blank needs exactly one ___")
            if q["answer"] not in q["options"]:
                errors.append(f"{tag} e{k}: answer not among options")
        for c in L["cards"]:
            for e in c["examples"]:
                if "highlight" in e and e["highlight"] not in e["text"]:
                    errors.append(f"{tag}: highlight {e['highlight']!r} not in {e['text']!r}")
            for t in c["tables"]:
                sp = t.get("speakCols")
                if sp is None:
                    warns.append(f"{tag}: table {t.get('title') or t['headers']} has no say=[...] columns")
                else:
                    for i in sp:
                        if not 0 <= i < len(t["headers"]):
                            errors.append(f"{tag}: speakCols {i} outside table")
                for r in t["rows"]:
                    if len(r) != len(t["headers"]):
                        errors.append(f"{tag}: table row {r} has {len(r)} cells, header has {len(t['headers'])}")
                    for cell in r:
                        if cell.count("{") != cell.count("}"):
                            errors.append(f"{tag}: unbalanced braces in {cell!r}")

        # --- encoding hygiene
        for text in all_text(m) + [o for q in L["exercises"] for o in q["options"]]:
            if _nfc(text) != text:
                errors.append(f"{tag}: text is not NFC-normalised: {text[:40]!r}")
            if re.search("[Ѐ-ӿ]", text):
                errors.append(f"{tag}: Cyrillic letter in {text[:40]!r}")
            if "́" in text:
                errors.append(f"{tag}: combining accent in {text[:40]!r}")

        # --- gating
        ranks = []
        for w in L["requires"]:
            if w not in deck_rank:
                errors.append(f"{tag}: requiredLemma {w!r} is not in the deck")
            else:
                ranks.append(deck_rank[w])
        info.append(f"{lid}  unlock words: {len(ranks)}/{len(L['requires'])} in deck, "
                    f"ranks {sorted(ranks)}")

        # --- punctuation
        spoken = spanish_only(m)
        for label, text in spoken + [("answer", q["answer"]) for q in L["exercises"]]:
            t = clean(text)
            if t.count("¿") != t.count("?"):
                errors.append(f"{tag}: unbalanced ¿ ? in {label}: {t[:60]!r}")
            if t.count("¡") != t.count("!"):
                errors.append(f"{tag}: unbalanced ¡ ! in {label}: {t[:60]!r}")
        for text in all_text(m):
            if QUESTION_NOACCENT.search(text):
                errors.append(f"{tag}: interrogative without accent: {text[:70]!r}")
            if text.count("¿") > text.count("?"):
                errors.append(f"{tag}: ¿ without ?: {text[:70]!r}")
        for label, text in spoken:
            if ABBR.search(text):
                warns.append(f"{tag}: abbreviation in spoken {label}: {text[:50]!r}")
            if re.search(r"\d", text):
                warns.append(f"{tag}: digit in spoken {label}: {text[:50]!r}")
            if "/" in text:
                warns.append(f"{tag}: slash in spoken {label}: {text[:50]!r}")

        # --- gender of article + noun (best effort)
        if genders:
            seen = set()
            short_answers = [q["answer"] for q in L["exercises"] if len(q["answer"].split()) <= 4]
            for label, text in spoken + [("answer", t) for t in short_answers]:
                for part in clean(text).split("___"):
                  toks = WORD.findall(part)
                  for a, n in zip(toks, toks[1:]):
                      al, nl = a.lower(), n.lower()
                      if al not in ARTICLES or nl in ARTICLES:
                          continue
                      if nl in EL_FEM and al in ("el", "un"):
                          continue
                      if nl in NUMBER_WORDS or nl in COMMON_GENDER:
                          continue
                      want = ARTICLES[al]
                      found = set()
                      for cand in singulars(nl):
                          found |= genders.get(cand, set())
                      if found and want not in found and (al, nl) not in seen:
                          seen.add((al, nl))
                          warns.append(f"{tag}: gender? '{a} {n}' (noun is {'/'.join(sorted(found))})")

        if not have_wk:
            continue

        # --- spelling: Spanish-only text
        unknown = set()
        for label, text in spoken:
            for w in WORD.findall(clean(text)):
                lw = w.lower()
                if lw in ALLOW or lw in all_forms:
                    continue
                unknown.add(lw)
        for w in sorted(unknown):
            warns.append(f"{tag}: not a known Spanish word form: {w}")

        # --- spelling: mixed text must be Spanish or English
        unknown = set()
        for text in mixed(m):
            for w in WORD.findall(clean(text)):
                lw = w.lower()
                if lw in ALLOW or lw in ALLOW_EN or lw in all_forms or english_ok(lw, eng):
                    continue
                unknown.add(lw)
        for w in sorted(unknown):
            warns.append(f"{tag}: not Spanish or English: {w}")

        # --- morphology
        for item in L["verify"]:
            if len(item) == 2:
                lem, form = item
                lf = lemma_forms.get(lem.lower())
                if lf is None:
                    warns.append(f"{tag}: verify: {lem!r} is not a dictionary headword")
                elif form.lower() not in lf:
                    errors.append(f"{tag}: {form!r} is not a form of {lem!r}")
            else:
                verb, idx, form = item[:3]
                mode = item[3] if len(item) > 3 else "pres"
                p = paradigm(verb, mode)
                if p is None:
                    errors.append(f"{tag}: no paradigm for {verb!r}")
                elif p[idx] != form:
                    errors.append(f"{tag}: {verb} person {idx}: table says {form!r}, paradigm {p[idx]!r}")
                lf = lemma_forms.get(verb)
                if lf is not None and form.lower() not in lf:
                    msg = f"{tag}: {form!r} is not in the dictionary entry for {verb!r}"
                    (errors if mode == "pres" else warns).append(msg)
        for k, q in enumerate(L["exercises"], 1):
            lem = q["lemma"]
            if not lem:
                continue
            if ":" in lem:
                parts_ = lem.split(":")
                verb, who = parts_[0], parts_[1]
                mode = parts_[2] if len(parts_) > 2 else "pres"
                want = person_form(verb, who, mode)
                if want is None:
                    errors.append(f"{tag} e{k}: bad lemma tag {lem!r}")
                    continue
                if q["answer"].lower() != want:
                    errors.append(f"{tag} e{k}: {q['answer']!r} is not {who} of {verb} ({want!r})")
                for o in q["options"]:
                    if o != q["answer"] and o.lower() == want:
                        errors.append(f"{tag} e{k}: distractor {o!r} equals the right form")
            else:
                lf = lemma_forms.get(lem)
                if lf is None:
                    warns.append(f"{tag} e{k}: lemma {lem!r} not a headword")
                elif q["answer"].lower() not in lf:
                    errors.append(f"{tag} e{k}: correct answer {q['answer']!r} is not a form of {lem!r}")
                else:
                    also = [o for o in q["options"] if o != q["answer"] and o.lower() in lf]
                    if also:
                        info.append(f"{lid} e{k}  distractors that are other real forms of {lem}: "
                                    f"{', '.join(also)} (check none is also right)")

        # --- vocabulary load: words outside the 5,000-word deck
        outside = set()
        for label, text in spoken:
            for w in WORD.findall(clean(text)):
                lw = w.lower()
                if lw in ALLOW or lw in deck_rank:
                    continue
                lemmas = form_lemmas.get(lw, set())
                if lemmas and not any(l in deck_rank for l in lemmas) and len(lw) > 2:
                    outside.add(sorted(lemmas)[0])
        if outside:
            info.append(f"{lid}  words outside the 5,000-word deck: {', '.join(sorted(outside))}")

    return errors, warns, info

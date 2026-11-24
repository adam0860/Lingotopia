"""Unit 4: Genki I, Lesson 1 "New Friends" (あたらしい ともだち), pp. 38-57.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, pictures, partner/group work and role plays are left out; the explanations are mine and the
answers to the practice drills are mine too (the book gives them in its separate workbook key)."""
from dsl_ja import *

# ---------------------------------------------------------------- book pairs (Japanese + romaji printed in the book)
rj("すみません。いま なんじですか。", "Sumimasen. Ima nanji desu ka.")
rj("じゅうにじはんです。", "Juuniji han desu.", over={"じゅうにじはんです。": "じゅうにじ はん です。"})
rj("ありがとう ございます。", "Arigatoo gozaimasu.")
rj("いいえ。", "Iie.")
rj("あの、りゅうがくせいですか。", "Ano, ryuugakusee desu ka.", over={"あの、りゅうがくせいですか。": "あの、りゅうがくせい ですか。"})
rj("ええ、アリゾナだいがくの がくせいです。", "Ee, Arizona daigaku no gakusee desu.") if False else None
rj("そうですか。せんこうは なんですか。", "Soo desu ka. Senkoo wa nan desu ka.")
rj("にほんごです。いま にねんせいです。", "Nihongo desu. Ima ninensee desu.")

def three(l):
    return list(dict.fromkeys(l))[:3]


# ================================================================= 1 the dialogue
_D1 = [("メアリー", "すみません。いま なんじですか。", "Excuse me. What time is it now?"),
       ("たけし", "じゅうにじはんです。", "It’s half past twelve."),
       ("メアリー", "ありがとう ございます。", "Thank you."),
       ("たけし", "いいえ。", "You’re welcome.")]
_D2 = [("たけし", "あの、りゅうがくせいですか。", "Um… are you an international student?"),
       ("メアリー", "ええ、アリゾナだいがくの がくせいです。", "Yes, I am a student at the University of Arizona."),
       ("たけし", "そうですか。せんこうは なんですか。", "I see. What is your major?"),
       ("メアリー", "にほんごです。いま にねんせいです。", "Japanese. I am a sophomore now.")]
L1 = lesson(
    "Dialogue: New Friends",
    "すみません。いま なんじですか。 · りゅうがくせいですか。",
    requires=[],
    cards=[
        card("Dialogue 1: asking the time", "Mary, an international student who just arrived in Japan, talks to a Japanese student, Takeshi. Tap a line to hear it.", examples=dlg(_D1)),
        card("Dialogue 2: getting acquainted", "", examples=dlg(_D2)),
        card("What to notice", "Neither speaker says “I” or “you”: the Japanese leaves out what is clear from the situation. Sentences end with です, and a question is made by adding か. Mary and Takeshi use ありがとう ございます and いいえ, the polite and the “you’re welcome” forms from the Greetings unit.",
             examples=[D("いま なんじですか。", "What time is it now?"), D("にほんごです。", "(It) is Japanese.")]),
    ],
    exercises=uniq(
        [M("What does Mary ask Takeshi first?", "what time it is", ["his name", "his major", "his age"], "いま なんじですか means “What time is it now?”"),
         M("What time is it in the dialogue?", "half past twelve", ["half past one", "twelve o’clock", "nine o’clock"], "じゅうにじはん is 12:30."),
         M("How does Mary thank Takeshi?", "ありがとう ございます。", ["いってきます。", "ただいま。", "いただきます。"], "ありがとう ございます is the polite “Thank you.”"),
         M("What does いいえ mean as Takeshi’s reply?", "You’re welcome.", ["No, I don’t know.", "Yes.", "Excuse me."], "Here いいえ is “Don’t mention it.”"),
         M("Which word does Takeshi use to start his question politely?", "あの", ["そう", "ええ", "はい"], "あの shows he has some reservation about asking."),
         M("What does Takeshi ask in the second dialogue?", "whether Mary is an international student", ["what time it is", "where Mary lives", "how old Mary is"], "りゅうがくせいですか。"),
         M("Which university does Mary attend?", "Arizona", ["Sakura", "Seoul", "London"], "アリゾナだいがく."),
         M("What is Mary’s major?", "Japanese", ["English", "history", "business"], "にほんご."),
         M("What year is Mary?", "second year", ["first year", "third year", "fourth year"], "にねんせい is a sophomore."),
         M("What does そうですか show?", "that you understood what was said", ["that you don’t know", "that you are leaving", "that you are asking the time"], "“I see.” / “Is that so?”"),
         F("いま ___ ですか。 (What time is it now?)", "なんじ", ["なんさい", "なんねんせい", "にほんご"], "いま なんじですか。"),
         F("せんこうは ___ ですか。 (What is your major?)", "なん", ["なんじ", "なんさい", "にほんご"], "せんこうは なんですか。"),
         F("アリゾナだいがくの ___ です。 (a student)", "がくせい", ["せんせい", "ともだち", "ばんごう"], "アリゾナだいがくの がくせいです。"),
         F("じゅうにじ ___ です。 (half past twelve)", "はん", ["さい", "ご", "じん"], "じゅうにじはんです。")]
        + [M("What does メアリー ask in Japanese: “What time is it now?”", "いま なんじですか。", ["せんこうは なんですか。", "りゅうがくせいですか。", "なんさいですか。"], "いま なんじですか。"),
           M("What does たけし ask: “What is your major?”", "せんこうは なんですか。", ["いま なんじですか。", "りゅうがくせいですか。", "なんねんせいですか。"], "せんこうは なんですか。")]
    ),
)

# ================================================================= 2 vocabulary
_V = [("あの", "um…"), ("いま", "now"), ("えいご", "English (language)"), ("ええ", "yes"), ("がくせい", "student"), ("ご", "…language, e.g. にほんご Japanese language"),
      ("こうこう", "high school"), ("ごご", "P.M."), ("ごぜん", "A.M."), ("さい", "…years old"), ("さん", "Mr./Ms. …"), ("じ", "…o’clock, e.g. いちじ one o’clock"),
      ("じん", "…people, e.g. にほんじん Japanese people"), ("せんこう", "major"), ("せんせい", "teacher; Professor …"), ("そうです", "That’s right."), ("そうですか", "I see.; Is that so?"),
      ("だいがく", "college; university"), ("でんわ", "telephone"), ("ともだち", "friend"), ("なまえ", "name"), ("なん", "what (before です or a counter)"), ("なに", "what (before a particle)"),
      ("にほん", "Japan"), ("ねんせい", "…year student, e.g. いちねんせい first-year student"), ("はい", "yes"), ("はん", "half, e.g. にじはん half past two"), ("ばんごう", "number"),
      ("りゅうがくせい", "international student"), ("わたし", "I")]
_VC = [("アメリカ", "U.S.A."), ("イギリス", "Britain"), ("オーストラリア", "Australia"), ("かんこく", "Korea"), ("スウェーデン", "Sweden"), ("ちゅうごく", "China")]
_VM = [("かがく", "science"), ("アジアけんきゅう", "Asian studies"), ("けいざい", "economics"), ("こくさいかんけい", "international relations"), ("コンピューター", "computer"),
       ("じんるいがく", "anthropology"), ("せいじ", "politics"), ("ビジネス", "business"), ("ぶんがく", "literature"), ("れきし", "history")]
_VO = [("しごと", "job; work; occupation"), ("いしゃ", "doctor"), ("かいしゃいん", "office worker"), ("こうこうせい", "high school student"), ("しゅふ", "housewife"),
       ("だいがくいんせい", "graduate student"), ("だいがくせい", "college student"), ("べんごし", "lawyer")]
_VF = [("おかあさん", "mother"), ("おとうさん", "father"), ("おねえさん", "older sister"), ("おにいさん", "older brother"), ("いもうと", "younger sister"), ("おとうと", "younger brother")]
for a, b in [("ええ", "ee"), ("がくせい", "gakusee"), ("こうこう", "kookoo"), ("ごぜん", "gozen"), ("せんこう", "senkoo"), ("せんせい", "sensee"), ("そうです", "soo desu"), ("そうですか", "soo desu ka"),
             ("だいがく", "daigaku"), ("でんわ", "denwa"), ("ともだち", "tomodachi"), ("なまえ", "namae"), ("にほん", "nihon"), ("ばんごう", "bangoo"), ("りゅうがくせい", "ryuugakusee"), ("わたし", "watashi"),
             ("えいご", "eego"), ("ねんせい", "nensee"), ("けいざい", "keezai"), ("こくさいかんけい", "kokusaikankee"), ("コンピューター", "konpyuutaa"), ("じんるいがく", "jinruigaku"),
             ("せいじ", "seeji"), ("ビジネス", "bijinesu"), ("ぶんがく", "bungaku"), ("れきし", "rekishi"), ("しごと", "shigoto"), ("いしゃ", "isha"), ("かいしゃいん", "kaishain"),
             ("こうこうせい", "kookoosee"), ("しゅふ", "shufu"), ("だいがくいんせい", "daigakuinsee"), ("だいがくせい", "daigakusee"), ("べんごし", "bengoshi"), ("おかあさん", "okaasan"),
             ("おとうさん", "otoosan"), ("おねえさん", "oneesan"), ("おにいさん", "oniisan"), ("いもうと", "imooto"), ("おとうと", "otooto"), ("アメリカ", "amerika"), ("イギリス", "igirisu"),
             ("オーストラリア", "oosutoraria"), ("かんこく", "kankoku"), ("スウェーデン", "suweeden"), ("ちゅうごく", "chuugoku"), ("かがく", "kagaku"), ("アジアけんきゅう", "ajia kenkyuu")]:
    rj(a, b)

L2 = lesson(
    "Vocabulary: Lesson 1",
    "わたし · がくせい · せんこう · にほん · ともだち · family, majors, jobs, countries",
    requires=[],
    cards=[
        card("Words of the lesson", "The vocabulary list of Lesson 1. Several entries are suffixes that attach to other words: ご (language), さい (years old), さん (Mr./Ms.), じ (o’clock), じん (people), ねんせい (year student), はん (half).",
             tables=[jtable(_V[:15]), jtable(_V[15:])]),
        card("Additional vocabulary: countries", "", tables=[jtable(_VC)]),
        card("Additional vocabulary: majors", "", tables=[jtable(_VM)]),
        card("Additional vocabulary: occupations", "", tables=[jtable(_VO)]),
        card("Additional vocabulary: family", "These are the words for someone else’s family members (used when talking about the family of the person you are speaking to, and when addressing your own family). Talking about your own family to outsiders uses different words, which come in a later lesson.", tables=[jtable(_VF)]),
        card("Words you can build", "Country + じん makes a nationality, and a number + ねんせい tells the year in school.",
             examples=[D("にほんじん", "a Japanese person"), D("アメリカじん", "an American"), D("かんこくじん", "a Korean"), D("イギリスじん", "a British person"),
                       D("にほんご", "the Japanese language"), D("えいご", "the English language"), D("いちねんせい", "first-year student"), D("にねんせい", "second-year student")]),
    ],
    exercises=uniq(
        tr_q(_V[:10]) + tr_q(_V[10:20]) + tr_q(_V[20:]) + rev_q(_V[:10]) + rev_q(_V[10:20]) + rev_q(_V[20:])
        + tr_q(_VC) + rev_q(_VC) + tr_q(_VM[:5]) + tr_q(_VM[5:]) + rev_q(_VM[:5]) + rev_q(_VM[5:])
        + tr_q(_VO) + rev_q(_VO) + tr_q(_VF) + rev_q(_VF)
        + [M("What does にほんじん mean?", "a Japanese person", ["the Japanese language", "Japan", "a Japanese student"], "じん after a country makes the people."),
           M("What does にほんご mean?", "the Japanese language", ["a Japanese person", "Japan", "a Japanese teacher"], "ご after a country makes the language."),
           M("How do you say “an American”?", "アメリカじん", ["アメリカご", "アメリカせい", "アメリカさい"], "Country + じん."),
           M("How do you say “the English language”?", "えいご", ["えいじん", "いぎりすじん", "えいさい"], "えいご."),
           M("How do you say “a Korean (person)”?", "かんこくじん", ["かんこくご", "ちゅうごくじん", "にほんじん"], "かんこくじん."),
           M("Which suffix counts years in school?", "ねんせい", ["さい", "じ", "ご"], "いちねんせい is a first-year student."),
           M("Which suffix gives a person’s age?", "さい", ["じ", "ねんせい", "さん"], "じゅうきゅうさい is nineteen years old."),
           M("Which suffix gives the hour?", "じ", ["さい", "ご", "じん"], "いちじ is one o’clock."),
           M("Which title follows a name?", "さん", ["じ", "ご", "はん"], "やましたさん is Mr./Ms. Yamashita."),
           M("What is the difference between なん and なに?", "なん is used before です or a counter; なに before a particle", ["なん is polite; なに is rude", "なん is for people; なに for things", "there is none"], "なんじ, なんですか but なにを."),
           M("Which word is used for someone else’s mother?", "おかあさん", ["いもうと", "おとうと", "おとうさん"], "おかあさん is mother."),
           M("Which is the younger sister?", "いもうと", ["おとうと", "おねえさん", "おかあさん"], "いもうと is younger sister.")]
    ),
)

# ================================================================= 3 numbers
_N1 = [("ゼロ", "0"), ("いち", "1"), ("に", "2"), ("さん", "3"), ("よん", "4"), ("ご", "5"), ("ろく", "6"), ("なな", "7"), ("はち", "8"), ("きゅう", "9"), ("じゅう", "10")]
_ONES = {1: "いち", 2: "に", 3: "さん", 4: "よん", 5: "ご", 6: "ろく", 7: "なな", 8: "はち", 9: "きゅう"}


def nk(n):
    """0-100 in kana."""
    if n == 0:
        return "ゼロ"
    if n == 100:
        return "ひゃく"
    t, o = divmod(n, 10)
    s = ""
    if t:
        s = ("" if t == 1 else _ONES[t]) + "じゅう"
    if o:
        s += _ONES[o]
    return s


rj("じゅういち", "juuichi")
rj("にじゅう", "nijuu")
rj("さんじゅう", "sanjuu")
rj("よんじゅう", "yonjuu")
rj("ごじゅう", "gojuu")
rj("ろくじゅう", "rokujuu")
rj("ななじゅう", "nanajuu")
rj("はちじゅう", "hachijuu")
rj("きゅうじゅう", "kyuujuu")
rj("ひゃく", "hyaku")
rj("じゅうなな", "juunana")
rj("じゅうきゅう", "juukyuu")
rj("じゅうろく", "juuroku")
rj("じゅうはち", "juuhachi")

_NUMTAB = [[str(n), nk(n), R.romanize(nk(n)).lower() if n else "zero"] for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
_ALT = [["0", "ゼロ、れい", "zero, ree"], ["4", "よん、し、よ", "yon, shi, yo"], ["7", "なな、しち", "nana, shichi"], ["9", "きゅう、く", "kyuu, ku"],
        ["14", "じゅうよん、じゅうし", "juuyon, juushi"], ["17", "じゅうなな、じゅうしち", "juunana, juushichi"], ["19", "じゅうきゅう、じゅうく", "juukyuu, juuku"]]
_HOURS = [("いちじ", "one o’clock"), ("にじ", "two o’clock"), ("さんじ", "three o’clock"), ("よじ", "four o’clock"), ("ごじ", "five o’clock"), ("ろくじ", "six o’clock"),
          ("しちじ", "seven o’clock"), ("はちじ", "eight o’clock"), ("くじ", "nine o’clock"), ("じゅうじ", "ten o’clock"), ("じゅういちじ", "eleven o’clock"), ("じゅうにじ", "twelve o’clock"),
          ("いちじはん", "half past one")]
for a, b in [("いちじ", "ichiji"), ("にじ", "niji"), ("さんじ", "sanji"), ("よじ", "yoji"), ("ごじ", "goji"), ("ろくじ", "rokuji"), ("しちじ", "shichiji"), ("はちじ", "hachiji"), ("くじ", "kuji"),
             ("じゅうじ", "juuji"), ("じゅういちじ", "juuichiji"), ("じゅうにじ", "juuniji"), ("いちじはん", "ichiji han")]:
    rj(a, b, over={a: a.replace("はん", " はん")} if "はん" in a else None)
_MIN = [("いっぷん", "1"), ("にふん", "2"), ("さんぷん", "3"), ("よんぷん", "4"), ("ごふん", "5"), ("ろっぷん", "6"), ("ななふん", "7"), ("はっぷん、はちふん", "8"), ("きゅうふん", "9"), ("じゅっぷん、じっぷん", "10"),
        ("じゅういっぷん", "11"), ("じゅうにふん", "12"), ("じゅうさんぷん", "13"), ("じゅうよんぷん", "14"), ("じゅうごふん", "15"), ("じゅうろっぷん", "16"), ("じゅうななふん", "17"),
        ("じゅうはっぷん、じゅうはちふん", "18"), ("じゅうきゅうふん", "19"), ("にじゅっぷん、にじっぷん", "20"), ("さんじゅっぷん、さんじっぷん", "30")]
_MINR = ["ippun", "nifun", "sanpun", "yonpun", "gofun", "roppun", "nanafun", "happun, hachifun", "kyuufun", "juppun, jippun", "juuippun", "juunifun", "juusanpun", "juuyonpun", "juugofun",
         "juuroppun", "juunanafun", "juuhappun, juuhachifun", "juukyuufun", "nijuppun, nijippun", "sanjuppun, sanjippun"]
_AGE = [("いっさい", "issai", "1"), ("にさい", "nisai", "2"), ("さんさい", "sansai", "3"), ("よんさい", "yonsai", "4"), ("ごさい", "gosai", "5"), ("ろくさい", "rokusai", "6"), ("ななさい", "nanasai", "7"),
        ("はっさい", "hassai", "8"), ("きゅうさい", "kyuusai", "9"), ("じゅっさい、じっさい", "jussai, jissai", "10"), ("じゅういっさい", "juuissai", "11"), ("はたち", "hatachi", "20")]
for a, b in [("いっさい", "issai"), ("にさい", "nisai"), ("さんさい", "sansai"), ("よんさい", "yonsai"), ("ごさい", "gosai"), ("ろくさい", "rokusai"), ("ななさい", "nanasai"), ("はっさい", "hassai"),
             ("きゅうさい", "kyuusai"), ("じゅういっさい", "juuissai"), ("はたち", "hatachi"), ("ろっぷん", "roppun"), ("ごふん", "gofun"), ("にふん", "nifun"), ("きゅうふん", "kyuufun")]:
    rj(a, b)

L3 = lesson(
    "Numbers, time and age",
    "ゼロ いち に さん … ひゃく · いちじ にじ … · ふん · さい",
    requires=[],
    cards=[
        card("Numbers", "Numbers from zero to one hundred. Above ten, the tens and the ones are put side by side: じゅう (10) + いち (1) = じゅういち (11); に (2) + じゅう (10) = にじゅう (20); にじゅうさん is 23.",
             tables=[table(["Number", "Japanese", "Romaji"], _NUMTAB, say=[1])]),
        card("Other readings", "Some numbers have a second reading. 0 is ゼロ or れい. 4 is usually よん, but し and よ appear in some combinations (よじ, four o’clock; よねんせい, fourth-year student). 7 is なな, but しち in しちじ (seven o’clock). 9 is きゅう, but く in くじ (nine o’clock).",
             tables=[table(["Number", "Japanese", "Romaji"], _ALT, say=[1])]),
        card("Expression Note: numbers with changing sounds", "Many number words have more than one pronunciation. For example: 1 is いち, but いっ in いっぷん (one minute) and いっさい (one year old). 2 is に, but when reading digits one by one (as in a phone number) it may be pronounced with a long vowel, にい. 3 is さん; the part after it may change shape, as in さんぷん, not さんふん. 4 is よん, but よねんせい and よじ; in some later combinations it is し (しがつ, April), and the part after it may change, as in よんぷん. 5 is ご; read out separately, it may be pronounced ごう. 6 is ろく, but ろっ in ろっぷん. 7 is なな, but しちじ for seven o’clock. 8 is はち, but usually はっ in はっぷん and はっさい. 9 is きゅう, but くじ for nine o’clock. 10 is じゅう, but じゅっ or じっ in じゅっぷん/じっぷん and じゅっさい/じっさい."),
        card("Time: hours", "Add じ to the number. ごぜん (A.M.) and ごご (P.M.) go in front of the hour, and はん (half) goes after it.",
             tables=[jtable(_HOURS)],
             examples=[D("いま ごぜん くじです。", "It is nine in the morning now."), D("いま ごご さんじはんです。", "It is half past three in the afternoon now.", over={"いま ごご さんじはんです。": "いま ごご さんじ はん です。"})]),
        card("Time: minutes", "Minutes use ふん or ぷん after the number, with some sound changes. The numbers 1, 3, 4, 6, 8 and 10 take ぷん (with small っ for 1, 6, 8 and 10); the others take ふん. For minutes 11–19 and for 20 and 30, the same endings follow the tens.",
             tables=[table(["Japanese", "Romaji", "Minutes"], [[a, r, n] for (a, n), r in zip(_MIN, _MINR)], say=[0])]),
        card("Age", "Add さい after the number for “…years old.” The question is なんさい (How old are you?); おいくつ is a more polite way to ask. 20 years old is はたち, though にじゅっさい or にじっさい can also be used.",
             tables=[table(["Japanese", "Romaji", "Age"], [[a, b, c] for a, b, c in _AGE], say=[0])],
             examples=[D("なんさいですか。", "How old are you?"), D("おいくつですか。", "How old are you? (polite)")]),
    ],
    exercises=uniq(
        [M(f"How do you say {n} in Japanese?", nk(n), [nk(x) for x in (n + 1, n + 2, n - 1, n + 10) if 0 <= x <= 100 and x != n][:3], f"{n} is {nk(n)} ({R.romanize(nk(n)).lower()}).") for n in
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 24, 30, 38, 40, 45, 50, 52, 60, 61, 70, 76, 80, 83, 90, 97, 100]]
        + [M(f"What number is {nk(n)}?", str(n), [str(x) for x in (n + 1, n + 2, n - 1, n + 10) if 0 <= x <= 100 and x != n][:3], f"{nk(n)} is {n}.") for n in
           [5, 9, 7, 1, 10, 8, 2, 6, 4, 3, 45, 83, 19, 76, 52, 100, 38, 61, 24, 97, 15, 40, 60, 90, 21, 35]]
        + [M("What is 5 + 3 in Japanese?", "はち", ["ろく", "なな", "きゅう"], "5 + 3 = 8, はち."), M("What is 9 + 1 in Japanese?", "じゅう", ["きゅう", "はち", "じゅういち"], "9 + 1 = 10, じゅう."),
           M("What is 3 + 4 in Japanese?", "なな", ["ろく", "はち", "ご"], "3 + 4 = 7, なな."), M("What is 6 − 6 in Japanese?", "ゼロ", ["いち", "ろく", "じゅう"], "6 − 6 = 0, ゼロ (or れい)."),
           M("What is 10 + 9 in Japanese?", "じゅうきゅう", ["じゅうはち", "にじゅう", "きゅうじゅう"], "10 + 9 = 19, じゅうきゅう."), M("What is 8 − 7 in Japanese?", "いち", ["に", "なな", "ゼロ"], "8 − 7 = 1, いち."),
           M("What is 40 − 25 in Japanese?", "じゅうご", ["にじゅうご", "じゅうろく", "ごじゅう"], "40 − 25 = 15, じゅうご.")]
        + [M(f"Which time is {s}?", a, three([x for x, _ in _HOURS if x != a]), f"{a} is {s}.") for a, s in _HOURS]
        + [M(f"What does {a} mean?", s, three([y for _, y in _HOURS if y != s]), f"{a} ({R.romanize(a).lower()}) is {s}.") for a, s in _HOURS]
        + [M("How do you say “9 o’clock”?", "くじ", ["きゅうじ", "ここのじ", "くさい"], "9 o’clock is くじ, not きゅうじ."), M("How do you say “4 o’clock”?", "よじ", ["よんじ", "しじ", "よさい"], "4 o’clock is よじ."),
           M("How do you say “7 o’clock”?", "しちじ", ["ななじ", "ななさい", "しじ"], "7 o’clock is しちじ."),
           M("Which is “P.M.”?", "ごご", ["ごぜん", "はん", "じ"], "ごご is P.M.; ごぜん is A.M."), M("Which is “A.M.”?", "ごぜん", ["ごご", "はん", "じ"], "ごぜん is A.M.")]
        + [M(f"How do you say “{n} minutes”?", a.split("、")[0], three([x.split("、")[0] for x, m in _MIN if m != n]), f"{n} minutes: {a.split('、')[0]}.") for a, n in _MIN[:10]]
        + [M(f"How do you say “{c} years old”?", a.split("、")[0], three([x.split("、")[0] for x, _, y in _AGE if y != c]), f"{c} years old: {a.split('、')[0]}.") for a, b, c in _AGE]
        + [M("How do you say “20 years old”?", "はたち", ["にじゅうさい", "にさい", "じゅっさい"], "20 years old is はたち."), M("How do you ask someone’s age?", "なんさいですか。", ["なんじですか。", "なんですか。", "なんねんせいですか。"], "なんさいですか。")]
    ),
)

# ================================================================= 4 grammar: X wa Y desu, questions
rj("がくせいです。", "Gakusee desu.")
rj("にほんごです。", "Nihongo desu.")
rj("りゅうがくせいです。", "Ryuugakusee desu.")
rj("りゅうがくせいですか。", "Ryuugakusee desu ka.")
rj("せんこうは なんですか。", "Senkoo wa nan desu ka.")
rj("せんこうは えいごです。", "Senkoo wa eego desu.")
rj("わたしは スー・キムです。", "Watashi wa Suu Kimu desu.")
rj("やましたさんは せんせいです。", "Yamashita san wa sensee desu.", over={"やましたさんは せんせいです。": "やました さん は せんせい です。"}) if False else None
rj("いま なんじですか。", "Ima nanji desu ka.")
rj("いま くじです。", "Ima kuji desu.")
rj("なんねんせいですか。", "Nannensee desu ka.")
rj("にねんせいです。", "Ninensee desu.")
L4 = lesson(
    "Grammar 1: X は Y です and questions with か",
    "わたしは がくせいです · りゅうがくせいですか · なん, なんじ, なんさい, なんねんせい",
    requires=[],
    cards=[
        card("です: “It is …”", "“It is 12:30.” “I am a student.” “My major is the Japanese language.” All of these are expressed with a noun and the word です. Note that none of these sentences has a “subject” like the “it,” “I” and “my major” of the English versions. Sentences without subjects are very common in Japanese; speakers tend to omit the subject whenever they think it is clear to the listener what or who they are referring to.",
             examples=[D("じゅうにじはんです。", "(It) is half past twelve."), D("がくせいです。", "(I) am a student."), D("にほんごです。", "(My major) is the Japanese language.")]),
        card("XはYです", "When it is not clear what is being talked about, we can say X は …, where X stands for the thing that is talked about, the “topic.” The pattern X は Y です identifies a person or a thing X as item Y: “X is Y. As for X, it is Y.” は is a particle: it attaches to a phrase and shows how it relates to the rest of the sentence. It is written は but pronounced wa.",
             examples=[D("せんこうは にほんごです。", "(My) major is the Japanese language."), D("わたしは スー・キムです。", "I am Sue Kim."), D("やましたさんは せんせいです。", "Mr. Yamashita is a teacher."),
                       D("メアリーさんは アメリカじんです。", "Mary is an American.")]),
        card("No “a” and no plural", "Nouns like がくせい and せんせい stand alone, unlike the English “student” and “teacher,” which are preceded by “a.” Japanese has no item that corresponds to “a,” nor to the plural “-s.” Without background, a sentence like がくせいです is ambiguous: it may mean “We are / you are / they are students” as well as “I am / you are / she is a student.”"),
        card("Questions: add か", "It is very easy to form questions in Japanese: add か at the end of a statement. It is not customary to write a question mark at the end of a question sentence in Japanese. This is a “yes/no” question:",
             examples=[D("りゅうがくせいです。", "(I am) an international student."), D("りゅうがくせいですか。", "(Are you) an international student?")]),
        card("Question words", "Question sentences can contain a question word like なん (what). In this lesson you learn: なんじ (what time), なんさい (how old), なんねんせい (what year in school). The question word for “what” has two pronunciations: なん is used immediately before です or before a counter like じ (o’clock); なに is used before a particle, and also in the word なにじん (person of what nationality).",
             examples=[D("せんこうは なんですか。", "What is your major?"), D("せんこうは えいごです。", "(My major) is English."), D("いま なんじですか。", "What time is it now?"), D("いま くじです。", "It is nine o’clock."),
                       D("メアリーさんは なんさいですか。", "How old are you, Mary?"), D("じゅうきゅうさいです。", "I’m nineteen years old."), D("なんねんせいですか。", "What year are you in college?"), D("にほんじんですか。", "Are you Japanese?")]),
        card("Telephone numbers", "A telephone number is asked with でんわばんごうは なんですか and answered with the digits read one at a time, with の between the exchange and the last digits.",
             examples=[D("でんわばんごうは なんですか。", "What is your telephone number?"), D("いち はち ろくの なな さん よん さんです。", "It is 186-7343.")]),
    ],
    exercises=uniq(
        [F("わたしは がくせい ___。", "です", ["ですか", "の", "は"], "わたしは がくせいです。", tr="I am a student."),
         F("りゅうがくせいです___", "か", ["は", "の", "です"], "Adding か makes a question: りゅうがくせいですか。"),
         F("せんこう___ にほんごです。", "は", ["の", "か", "です"], "せんこうは にほんごです。", tr="My major is Japanese."),
         F("メアリーさん___ アメリカじんです。", "は", ["の", "か", "です"], "メアリーさんは アメリカじんです。", tr="Mary is an American."),
         F("いま ___ ですか。 (What time?)", "なんじ", ["なんさい", "なんねんせい", "なん"], "いま なんじですか。"),
         F("メアリーさんは ___ ですか。 (How old?)", "なんさい", ["なんじ", "なんねんせい", "なに"], "メアリーさんは なんさいですか。"),
         F("___ ですか。 (What year in school?)", "なんねんせい", ["なんさい", "なんじ", "なんにち"], "なんねんせいですか。"),
         F("せんこうは ___ ですか。 (What?)", "なん", ["なに", "なんじ", "なんさい"], "なん is used right before です."),
         M("In X は Y です, how is は pronounced?", "wa", ["ha", "o", "e"], "The particle は is pronounced “wa.”"),
         M("What do you add to turn a statement into a question?", "か", ["は", "の", "です"], "Add か at the end."),
         M("Is a question mark customary in Japanese questions?", "no", ["yes, always", "only in questions with なん", "only in polite speech"], "It is not customary to write a question mark."),
         M("Does Japanese have a word for “a” or plural “-s”?", "no", ["yes, は", "yes, の", "yes, です"], "Nouns stand alone."),
         M("What does がくせいです mean?", "I am a student. / She is a student. / They are students.", ["Is it a student?", "Where is the student?", "I like students."], "Without context it is ambiguous."),
         M("Why are subjects often left out in Japanese?", "they are omitted when clear from the situation", ["Japanese has no subjects", "it is rude to say them", "they are replaced by か"], "Speakers omit them when it is clear who or what is meant."),
         M("What does メアリーさんは アメリカじんです mean?", "Mary is an American.", ["Mary is a student.", "Is Mary American?", "Mary is nineteen."], "X は Y です."),
         M("What does メアリーさんは なんさいですか mean?", "How old is Mary?", ["What is Mary’s major?", "What year is Mary?", "Where is Mary?"], "なんさい asks age."),
         M("When is なに used instead of なん?", "before a particle", ["before です", "before a counter", "never"], "なに is used before particles, e.g. なにじん."),
         M("What does なにじんですか ask?", "what nationality someone is", ["what time it is", "how old someone is", "what year someone is in"], "なにじん is “person of what nationality”.")]
        + [M(f"What does {a} mean?", b, ["Where is the student?", "I am a teacher.", "Is it a book?"], f"{a}") for a, b in
           [("りゅうがくせいですか。", "Are you an international student?"), ("せんこうは なんですか。", "What is your major?"), ("いま なんじですか。", "What time is it now?"), ("なんねんせいですか。", "What year are you?")]]
        + [M("Answer: メアリーさんは なんさいですか。", "じゅうきゅうさいです。", ["にねんせいです。", "にほんごです。", "くじです。"], "Mary is nineteen."),
           M("Answer: せんこうは なんですか。", "にほんごです。", ["じゅうきゅうさいです。", "くじです。", "にねんせいです。"], "A major is an answer such as にほんご."),
           M("Answer: なんねんせいですか。", "にねんせいです。", ["くじです。", "にほんごです。", "じゅうきゅうさいです。"], "にねんせい is second-year."),
           M("Answer: いま なんじですか。", "くじです。", ["にねんせいです。", "にほんごです。", "じゅうきゅうさいです。"], "くじ is nine o’clock.")]
    ),
)

# ================================================================= 5 grammar: no, expression notes
rj("たけしさんの でんわばんごう", "Takeshi san no denwa bangoo", over={"たけしさんの でんわばんごう": "たけし さん の でんわ ばんごう"})
L5 = lesson(
    "Grammar 2: noun の noun, names, and expression notes",
    "たけしさんの でんわばんごう · だいがくの せんせい · にほんの だいがく · あの · はい / ええ · さん",
    requires=[],
    cards=[
        card("noun の noun", "の is a particle that connects two nouns. The phrase さくらだいがくの がくせい means “a student at Sakura University.” The second noun, がくせい, provides the main idea (being a student), and the first, さくらだいがく, makes it more specific (not a high school but a college student). の is very versatile: in the first example below it acts like the English possessive (’s), but that is not the only role it can play.",
             examples=[D("たけしさんの でんわばんごう", "Takeshi’s phone number"), D("だいがくの せんせい", "a college professor"), D("にほんごの がくせい", "a student of the Japanese language"), D("にほんの だいがく", "a college in Japan")]),
        card("Word order: main idea last", "In the first two examples the English and Japanese words are arranged in the same order; in the last two they are in the opposite order. Japanese is more consistent: the main idea always comes at the end, with any further description placed before it. A phrase of the form “noun の noun” acts more or less like one big noun. You can put it wherever you can put a noun:",
             examples=[D("たけしさんの おかあさんは こうこうの せんせいです。", "Takeshi’s mother is a high school teacher.", over={"たけしさんの おかあさんは こうこうの せんせいです。": "たけし さん の おかあさん は こうこう の せんせい です。"})]),
        card("Culture note: Japanese names", "When Japanese give their name, they say their family name first and their given name last (middle names do not exist). When introducing themselves they often say only their family name. Most Japanese names are written in kanji. For example, たなか is usually written 田中, which means “middle of the rice field.” Family names are often related to nature or geographical features. Because many kanji share the same reading, names with the same pronunciation may be written with different kanji; ゆうこ can be written 優子 or with other characters.",
             tables=[jtable([("さとう", "family name"), ("すずき", "family name"), ("たかはし", "family name"), ("たなか", "family name"), ("いとう", "family name")], title="Family names"),
                     jtable([("たくや", "man’s given name"), ("しょうた", "man’s given name"), ("いちろう", "man’s given name"), ("ひろし", "man’s given name"), ("まさひろ", "man’s given name")], title="Men"),
                     jtable([("えりか", "woman’s given name"), ("あい", "woman’s given name"), ("なおみ", "woman’s given name"), ("ゆうこ", "woman’s given name"), ("みさき", "woman’s given name")], title="Women")]),
        card("あの", "あの indicates that you have some reservations about saying what you are going to say next. You may be worried about interrupting something someone is currently doing, or about sounding rude by asking personal questions, for example.", examples=[D("あの、りゅうがくせいですか。", "Um… are you an international student?")]),
        card("はい / ええ", "Both はい and ええ mean “yes” in response to yes-no questions. Compared to はい, ええ is more conversational and relaxed. In more informal situations, うん is used. はい is also used to respond to a knock at the door or to the calling of one’s name, meaning “Here.” (ええ cannot be used in that case.)",
             examples=dlg([("Teacher", "スミスさん？", "Mr. Smith?"), ("Student", "はい。", "Here.")]) if False else [D("はい。", "Yes. / Here."), D("ええ、そうです。", "Yes, that’s right.")]),
        card("そうですか", "そうですか acknowledges that you have understood what was just said: “Is that so?” or “I see.”", examples=[D("そうですか。", "I see.")]),
        card("Pronunciation of は", "The particle は is pronounced “wa,” not “ha.” It should be written with は. All other instances of “wa” are written with わ. There are a few exceptions, such as こんにちは (good afternoon) and こんばんは (good evening), which are usually written with は.",
             examples=[D("わたしの でんわばんごうは さん なな の はち ろく ろく ななです。", "My telephone number is 37-8667.", over={"わたしの でんわばんごうは さん なな の はち ろく ろく ななです。": "わたし の でんわ ばんごう は さん なな の はち ろく ろく なな です。"})]),
        card("Giving your telephone number", "The particle の is usually placed between the local exchange code and the last four digits. So 012-345-6789 is ゼロ いち に、さん よん ご の ろく なな はち きゅう."),
        card("せんせい", "The word せんせい is usually reserved for describing somebody else’s occupation. わたしは せんせいです makes sense, but may sound slightly arrogant, because せんせい actually means an “honorable master.” If you (or a member of your family) are a teacher and want to be really modest, you can use the word きょうし instead.",
             examples=[D("きょうし", "teacher (modest)")]),
        card("さん", "さん is placed after a name as a generic title. It goes both with a given name and a family name. Children are referred to as ちゃん (and boys in particular as くん) rather than さん. Professors and doctors are usually referred to with the title せんせい. さん and other title words are never used in reference to oneself.",
             examples=[D("やましたさん", "Mr./Ms. Yamashita"), D("ゆうこちゃん", "Yuuko (a girl)"), D("たけしくん", "Takeshi (a boy)"), D("やましたせんせい", "Professor Yamashita")]),
        card("Referring to the person you are talking to", "The word for “you,” あなた, is not very commonly used in Japanese. Instead, we use the name and a title like さん and せんせい to refer to the person we are talking to. So “Ms. Hart, are you Swedish?” should be the first sentence below, not the second.",
             examples=[D("ハートさんは スウェーデンじんですか。", "Ms. Hart, are you Swedish? (natural)"), D("ハートさん、あなたは スウェーデンじんですか。", "Ms. Hart, are you Swedish? (unnatural: avoid あなた)")]),
    ],
    exercises=uniq(
        [M("What does の do in たけしさんの でんわばんごう?", "connects two nouns (“Takeshi’s”)", ["asks a question", "means “is”", "marks the topic"], "の connects nouns."),
         M("In “noun の noun,” which noun is the main idea?", "the second one", ["the first one", "both equally", "neither"], "The main idea comes at the end."),
         M("How do you say “Takeshi’s phone number”?", "たけしさんの でんわばんごう", ["たけしさんは でんわばんごう", "でんわばんごうの たけしさん", "たけしさんか でんわばんごう"], "Description before the main idea."),
         M("How do you say “a college professor”?", "だいがくの せんせい", ["せんせいの だいがく", "だいがくは せんせい", "だいがくか せんせい"], "だいがく の せんせい."),
         M("How do you say “a student of the Japanese language”?", "にほんごの がくせい", ["がくせいの にほんご", "にほんごは がくせい", "にほんごか がくせい"], "にほんご の がくせい."),
         M("How do you say “a college in Japan”?", "にほんの だいがく", ["だいがくの にほん", "にほんは だいがく", "にほんか だいがく"], "にほん の だいがく."),
         M("How do Japanese give their names?", "family name first, given name last", ["given name first", "with a middle name", "only the given name"], "Family name first."),
         M("Do Japanese names have middle names?", "no", ["yes", "only for men", "only for women"], "Middle names do not exist."),
         M("What does たなか (田中) mean as kanji?", "middle of the rice field", ["above the mountain", "by the river", "pine forest"], "田 rice field, 中 middle."),
         M("What does あの signal?", "some reservation about what you will say next", ["a yes answer", "a question", "good-bye"], "あの is like “um…”."),
         M("Which “yes” is more conversational?", "ええ", ["はい", "あの", "さん"], "ええ is more relaxed than はい."),
         M("Which “yes” is used when your name is called (“Here”)?", "はい", ["ええ", "うん", "あの"], "ええ cannot be used there."),
         M("Which “yes” is used in informal situations?", "うん", ["はい", "ええ", "あの"], "うん is informal."),
         M("What does そうですか do?", "acknowledges you understood", ["asks the time", "asks for a name", "says good-bye"], "“Is that so?” / “I see.”"),
         M("Which exceptions are still written with は though pronounced “wa”?", "こんにちは and こんばんは", ["わたし and ともだち", "ありがとう", "せんせい"], "こんにちは and こんばんは."),
         M("Which title is used for boys?", "くん", ["ちゃん", "さん", "せんせい"], "くん is used for boys in particular."),
         M("Which title is used for children in general?", "ちゃん", ["さん", "くん", "せんせい"], "Children are referred to as ちゃん."),
         M("Which title is used for professors and doctors?", "せんせい", ["さん", "ちゃん", "くん"], "せんせい."),
         M("Can you add さん to your own name?", "no", ["yes, always", "only at school", "only in letters"], "Title words are never used for oneself."),
         M("What do Japanese usually say instead of あなた?", "the person’s name and title", ["わたし", "でんわ", "なまえ"], "Use a name + さん or せんせい."),
         M("Which word is the modest way to refer to a teacher in your family?", "きょうし", ["せんせい", "さん", "ともだち"], "きょうし."),
         M("How is a phone number such as 283-9547 read?", "ni hachi san no kyuu go yon nana", ["nihachisan kyuugoyonnana", "ni, hachi, san, kyuu, go", "nihachi kyuugo"], "の goes between the exchange and the last digits."),
         F("たけしさん___ でんわばんごう", "の", ["は", "か", "です"], "たけしさんの でんわばんごう"), F("にほん___ だいがく", "の", ["は", "か", "です"], "にほんの だいがく"),
         F("にほんご___ がくせい", "の", ["は", "か", "です"], "にほんごの がくせい"), F("だいがく___ せんせい", "の", ["は", "か", "です"], "だいがくの せんせい"),
         F("やました___ は せんせいです。 (Mr. Yamashita)", "さん", ["ちゃん", "くん", "なん"], "やましたさん"),
         F("こんにちは の は is pronounced ___", "wa", ["ha", "o", "e"], "こんにちは is konnichiwa.")]
    ),
)

# ================================================================= 6 practice: numbers, time, telephone, の
def digits_kana(s):
    m = {"0": "ゼロ", "1": "いち", "2": "に", "3": "さん", "4": "よん", "5": "ご", "6": "ろく", "7": "なな", "8": "はち", "9": "きゅう"}
    return " ".join(m[c] if c != "-" else "の" for c in s).replace(" の ", " の ")


def phone(s):
    parts = s.split("-")
    return " の ".join(" ".join({"0": "ゼロ", "1": "いち", "2": "に", "3": "さん", "4": "よん", "5": "ご", "6": "ろく", "7": "なな", "8": "はち", "9": "きゅう"}[c] for c in p) for p in parts)


_PH = [("だいがく", "951-0326"), ("せんせい", "362-4519"), ("メアリー", "020-6921-4236"), ("たけし", "030-8522-1032"), ("やました", "283-9547")]
_CITY = [("Tokyo", "ごぜん さんじ", "3:00 A.M."), ("London", "ごご ろくじ", "6:00 P.M."), ("Stockholm", "ごご しちじ", "7:00 P.M."), ("Nairobi", "ごご くじ", "9:00 P.M."),
         ("New Delhi", "ごご じゅういちじはん", "11:30 P.M."), ("Bangkok", "ごぜん いちじ", "1:00 A.M."), ("Sydney", "ごぜん よじ", "4:00 A.M."), ("New York", "ごご いちじ", "1:00 P.M."),
         ("Rio de Janeiro", "ごご さんじ", "3:00 P.M.")]
_NO = [("my teacher", "わたしの せんせい"), ("my telephone number", "わたしの でんわばんごう"), ("my name", "わたしの なまえ"), ("Takashi’s major", "たかしさんの せんこう"), ("Mary’s friend", "メアリーさんの ともだち"),
       ("student of the University of London", "ロンドンだいがくの がくせい"), ("teacher of the Japanese language", "にほんごの せんせい"), ("high school teacher", "こうこうの せんせい")]
L6 = lesson(
    "Practice: numbers, time, telephone numbers and の",
    "Read the numbers · What time is it? · Telephone numbers · の phrases",
    requires=[],
    cards=[
        card("Numbers: answers to the drills", "The book’s Practice (Numbers) A–C asks you to read numbers aloud. Here are the answers for the drills so you can check yourself (the book gives the numbers; the readings and answers are mine).",
             tables=[table(["Practice", "Number", "Reading"], [["A", str(n), nk(n)] for n in [5, 9, 7, 1, 10, 8, 2, 6, 4, 3]] + [["B", str(n), nk(n)] for n in [45, 83, 19, 76, 52, 100, 38, 61, 24, 97]] +
                       [["C", s, nk(v)] for s, v in [("5 + 3", 8), ("9 + 1", 10), ("3 + 4", 7), ("6 − 6", 0), ("10 + 9", 19), ("8 − 7", 1), ("40 − 25", 15)]], say=[2])]),
        card("Time: what time is it in each city?", "Practice B asks “とうきょうは いま なんじですか。” for cities around the world (the map is left out). The times printed on the map, with my answers:",
             examples=[D("とうきょうは いま ごぜん さんじです。", "It is 3:00 A.M. in Tokyo now."), D("ロンドンは いま ごご ろくじです。", "It is 6:00 P.M. in London now.")],
             tables=[table(["City", "Time", "Answer"], [[c, t, ja + "です。"] for c, ja, t in _CITY], say=[2])]),
        card("Telephone numbers", "Practice III A: read these telephone numbers (the first is the book’s example). The exchange and the last digits are joined with の. ", tables=[table(["Whose", "Number", "Reading"], [[w, n, phone(n) + "です。"] for w, n in _PH], say=[2])],
             examples=[D("でんわばんごうは なんですか。", "What is your telephone number?"), D("に はち さんの きゅう ご よん ななです。", "It is 283-9547."), D("に はち さんの きゅう ご よん ななですね。", "It is 283-9547, right?"), D("はい、そうです。", "Yes, that’s right.")]),
        card("ね: “…, right?”", "Adding ね to the end of a statement checks that you have understood, “…, right?”. The answer is はい、そうです (“Yes, that’s right.”)."),
        card("Translate with の", "Practice IV: translate these phrases using の. Answers (mine):", tables=[table(["English", "Japanese"], [[e, j] for e, j in _NO], say=[1])]),
        card("Activities left out", "The pair work and group work (asking classmates their telephone numbers) and the pictured clocks of Practice II A are not included."),
    ],
    exercises=uniq(
        [M(f"Read the number {n}.", nk(n), [nk(x) for x in (n + 1, n - 1, n + 10, n + 2) if 0 <= x <= 100 and x != n][:3], f"{n} = {nk(n)}.") for n in [45, 83, 19, 76, 52, 100, 38, 61, 24, 97, 31, 68, 74, 99, 57]]
        + [M(f"What time is it in {c}? ({t})", ja, three([x for _, x, _ in _CITY if x != ja]), f"{c}: {ja}.") for c, ja, t in _CITY]
        + [M(f"“{e}” in Japanese is…", j, three([x for _, x in _NO if x != j]), f"{e} → {j}") for e, j in _NO]
        + [M(f"Which telephone number is {phone(n)}?", n, three([x for _, x in _PH if x != n]), f"{phone(n)} is {n}.") for w, n in _PH]
        + [M("What does ね at the end of a sentence do?", "checks “…, right?”", ["makes a question", "makes it negative", "marks the topic"], "でんわばんごうは … ですね。"),
           M("How do you confirm: “Yes, that’s right”?", "はい、そうです。", ["いいえ。", "すみません。", "ただいま。"], "はい、そうです。"),
           F("でんわばんごうは ___ ですか。", "なん", ["なに", "なんじ", "なんさい"], "でんわばんごうは なんですか。"),
           F("に はち さん ___ きゅう ご よん なな", "の", ["は", "か", "です"], "の goes between the exchange and the last digits."),
           F("ごご ろく___です。", "じ", ["さい", "ご", "ふん"], "ごご ろくじです。"),
           F("わたし___ なまえ", "の", ["は", "か", "です"], "わたしの なまえ")]
    ),
)

# ================================================================= 7 practice: describing people; family; self-introduction
_P = [("メアリーさん", "アメリカじん", "にねんせい", "じゅうきゅうさい", "アリゾナだいがく", "にほんご"),
      ("たけしさん", "にほんじん", "よねんせい", "にじゅうにさい", "さくらだいがく", "れきし"),
      ("スーさん", "かんこくじん", "さんねんせい", "にじゅっさい", "ソウルだいがく", "コンピューター"),
      ("ロバートさん", "イギリスじん", "よねんせい", "にじゅうにさい", "ロンドンだいがく", "ビジネス"),
      ("やましたせんせい", "にほんじん", "", "よんじゅうななさい", "さくらだいがく", "")]
_FAM = [("おとうさん", "かいしゃいん", "よんじゅうはっさい", "48"), ("おかあさん", "しゅふ", "よんじゅうごさい", "45"), ("おにいさん", "だいがくいんせい", "にじゅうさんさい", "23"), ("いもうと", "こうこうせい", "じゅうろくさい", "16")]
L7 = lesson(
    "Practice: describing people, and self-introductions",
    "メアリーさんは アメリカじんです · おとうさんは かいしゃいんです · じこしょうかい",
    requires=[],
    cards=[
        card("The chart of five people", "Practice VI describes these people with the cues (a) nationality, (b) year in school, (c) age, (d) school, (e) major. Mary and Sue are students at American and Korean universities; Robert is from Britain. Here is the chart in Japanese:",
             tables=[table(["Name", "Nationality", "Year", "Age", "School", "Major"], [list(p) for p in _P], say=[0, 1, 2, 3, 4, 5])]),
        card("Model sentences", "One model sentence for each cue, as the book’s examples show (and the same for the others):",
             examples=[D("メアリーさんは アメリカじんです。", "Mary is an American."), D("メアリーさんは にねんせいです。", "Mary is a sophomore."), D("メアリーさんは じゅうきゅうさいです。", "Mary is nineteen years old."),
                       D("メアリーさんは アリゾナだいがくの がくせいです。", "Mary is a student at the University of Arizona."), D("メアリーさんの せんこうは にほんごです。", "Mary’s major is Japanese."),
                       D("たけしさんは にほんじんです。", "Takeshi is Japanese."), D("スーさんは かんこくじんです。", "Sue is Korean."), D("ロバートさんの せんこうは ビジネスです。", "Robert’s major is business."),
                       D("やましたせんせいは よんじゅうななさいです。", "Professor Yamashita is forty-seven.")]),
        card("Question and answer practice", "Practice B asks yes/no questions about the chart. The answer is ええ、そうです。 when the cue is right, and いいえ、… with the correct information when it is wrong.",
             examples=dlg([("Q", "メアリーさんは アメリカじんですか。", "Is Mary American?"), ("A", "ええ、そうです。", "Yes, that’s right."), ("Q", "メアリーさんは さんねんせいですか。", "Is Mary a junior?"), ("A", "いいえ、にねんせいです。", "No, she is a sophomore.")])),
        card("Mary’s host family", "Practice VII: describe each person in Mary’s host family. The chart (my reading of the book’s picture): father, office worker, 48; mother, housewife, 45; older brother, graduate student, 23; younger sister, high school student, 16.",
             tables=[table(["Family", "Occupation / school", "Age"], [[a, b, c] for a, b, c, d in _FAM], say=[0, 1, 2])],
             examples=[D("おとうさんは かいしゃいんです。", "Her father is an office worker."), D("おとうさんは よんじゅうはっさいです。", "Her father is forty-eight years old.")]),
        card("Questions and answers about the family", "The book asks eight questions about this chart. My answers:",
             tables=[table(["Question", "Answer"], [["おとうさんは かいしゃいんですか。", "ええ、そうです。"], ["おとうさんは なんさいですか。", "よんじゅうはっさいです。"], ["おかあさんは せんせいですか。", "いいえ、しゅふです。"],
                                                      ["おかあさんは なんさいですか。", "よんじゅうごさいです。"], ["おにいさんは かいしゃいんですか。", "いいえ、だいがくいんせいです。"], ["おにいさんは なんさいですか。", "にじゅうさんさいです。"],
                                                      ["いもうとは だいがくせいですか。", "いいえ、こうこうせいです。"], ["いもうとは なんさいですか。", "じゅうろくさいです。"]], say=[0, 1])]),
        card("Review: questions for a classmate", "The book suggests these questions for the class activity (about name, hometown, occupation, year, age and major):",
             tables=[table(["Question", "Meaning", "Model answer"], [["おなまえは？", "What is your name?", "メアリー・ハートです。"], ["ごしゅっしんは？", "Where do you come from?", "アリゾナです。"], ["おしごとは？", "What is your occupation?", "がくせいです。"],
                                                                      ["なんねんせいですか。", "What year are you?", "にねんせいです。"], ["なんさいですか。", "How old are you?", "じゅうきゅうさいです。"], ["せんこうは なんですか。", "What is your major?", "にほんごです。"]], say=[0, 2])]),
        card("Self-introduction", "The book’s model self-introduction, to use as a pattern for your own:",
             examples=[D("はじめまして。", "How do you do?"), D("メアリー・ハートです。", "I am Mary Hart."), D("アリゾナだいがくの がくせいです。", "I am a student at the University of Arizona."), D("いま にねんせいです。", "I am a sophomore now."),
                       D("せんこうは にほんごです。", "My major is Japanese."), D("じゅうきゅうさいです。", "I am nineteen years old."), D("よろしく おねがいします。", "Nice to meet you.")]),
        card("Activities left out", "The class activities (asking classmates, and finding someone with a given major) and the role plays (asking for the time without a watch; getting to know a Japanese person) are left out. Use the dialogue and the self-introduction as models."),
    ],
    exercises=uniq(
        [M(f"What is {p[0]}’s nationality?", p[1], three([x[1] for x in _P if x[1] != p[1]]), f"{p[0]}は {p[1]}です。") for p in _P]
        + [M(f"What year in school is {p[0]}?", p[2], three([x[2] for x in _P if x[2] and x[2] != p[2]]), f"{p[0]}は {p[2]}です。") for p in _P if p[2]]
        + [M(f"How old is {p[0]}?", p[3], three([x[3] for x in _P if x[3] != p[3]]), f"{p[0]}は {p[3]}です。") for p in _P]
        + [M(f"Which school does {p[0]} attend?", p[4], three([x[4] for x in _P if x[4] != p[4]]), f"{p[0]}は {p[4]}の がくせいです。") for p in _P]
        + [M(f"What is {p[0]}’s major?", p[5], three([x[5] for x in _P if x[5] and x[5] != p[5]]), f"{p[0]}の せんこうは {p[5]}です。") for p in _P if p[5]]
        + [M("Is Mary a junior (third-year)? Answer in Japanese.", "いいえ、にねんせいです。", ["ええ、そうです。", "いいえ、よねんせいです。", "ええ、さんねんせいです。"], "She is a sophomore: にねんせい."),
           M("Is Takeshi a Japanese national? Answer in Japanese.", "ええ、そうです。", ["いいえ、かんこくじんです。", "いいえ、アメリカじんです。", "いいえ、イギリスじんです。"], "たけしさんは にほんじん."),
           M("Is Sue British? Answer in Japanese.", "いいえ、かんこくじんです。", ["ええ、そうです。", "いいえ、にほんじんです。", "ええ、イギリスじんです。"], "Sue is Korean."),
           M("Is Robert’s major business? Answer in Japanese.", "ええ、そうです。", ["いいえ、れきしです。", "いいえ、にほんごです。", "いいえ、コンピューターです。"], "ロバートさんの せんこうは ビジネス.")]
        + [M(f"{a}は なんさいですか。", c, [x[2] for x in _FAM if x[2] != c][:3], f"{a}は {c}です。") for a, b, c, d in _FAM]
        + [M(f"{a}は なんですか。 (occupation / school)", b, [x[1] for x in _FAM if x[1] != b][:3], f"{a}は {b}です。") for a, b, c, d in _FAM]
        + [M("What do you say at the start of a self-introduction?", "はじめまして。", ["ただいま。", "さようなら。", "いただきます。"], "はじめまして。"),
           M("What do you say at the end of a self-introduction?", "よろしく おねがいします。", ["ごちそうさまでした。", "いってきます。", "おやすみなさい。"], "よろしく おねがいします。"),
           M("How do you ask “What is your name?” (polite)", "おなまえは？", ["おしごとは？", "ごしゅっしんは？", "なんさいですか。"], "おなまえは？"),
           M("How do you ask “Where do you come from?”", "ごしゅっしんは？", ["おなまえは？", "おしごとは？", "せんこうは なんですか。"], "ごしゅっしんは？"),
           M("How do you ask “What is your occupation?”", "おしごとは？", ["おなまえは？", "ごしゅっしんは？", "なんねんせいですか。"], "おしごとは？")]
    ),
)

UNIT = unit("Genki I, Lesson 1: New Friends", [L1, L2, L3, L4, L5, L6, L7])

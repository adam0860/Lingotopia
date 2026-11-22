"""Unit 13: KBC Semester 1, Unit 2, Chapter 6 - Weather and Hobbies (날씨와 취미).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 2, Student's Edition.
Audio, video clips, pictures, maps, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and leaves the answers to its exercises blank: every translation of a
dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
from ko_kbc import *

import re as _re


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _mc(prompt, ans, pool, why, k=3):
    return M(prompt, ans, [x for x in dict.fromkeys(pool) if x != ans][:k], why)


def _tr(pairs, correct, k=3):
    """'What does X mean?' items taken from (Korean, English) pairs"""
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


# ================================================================== Topic A
_A_PASSAGE = [
    ("한국은 봄, 여름, 가을, 겨울, 사계절이 있습니다.", "Korea has four seasons: spring, summer, fall and winter."),
    ("봄에는 날씨가 따뜻합니다.", "In spring the weather is warm."),
    ("가끔 바람이 불고 비도 조금 내립니다.", "Sometimes the wind blows and it rains a little too."),
    ("여름은 아주 덥습니다.", "Summer is very hot."),
    ("구름이 많이 끼고 비가 자주 옵니다.", "Clouds form a lot and it rains often."),
    ("가을에는 조금 쌀쌀합니다.", "In fall it is a little chilly."),
    ("하늘이 높고 맑습니다.", "The sky is high and clear."),
    ("겨울은 춥고 눈이 자주 옵니다.", "Winter is cold and it snows often."),
]
_A_PAIRS = [
    ("가을", "fall; autumn"), ("겨울", "winter"), ("계절", "a season"), ("구름", "cloud"), ("끼다", "(fog, cloud, dust, etc.) to form"), ("날씨", "weather"), ("내리다", "(rain, snow, etc.) to fall; to come down"),
    ("높다", "to be high"), ("눈", "snow"), ("따뜻하다", "to be warm"), ("덥다", "(weather) to be hot"), ("많이", "a lot; much"), ("맑다", "to be clear"), ("바람", "wind"), ("봄", "spring"), ("불다", "to blow"),
    ("비", "rain"), ("쌀쌀하다", "to be chilly"), ("아주", "very (much); so; extremely"), ("안개", "fog"), ("여름", "summer"), ("춥다", "(weather) to be cold"), ("하늘", "the sky"), ("흐리다", "to be cloudy; to be overcast"),
]
_WX = [("봄", "따뜻합니다", "warm"), ("여름", "덥습니다", "hot"), ("가을", "쌀쌀합니다", "chilly"), ("겨울", "춥습니다", "cold")]
_WX_MODEL = [("안개가 끼었어요.", "It is foggy."), ("흐리고 바람이 불고 비가 옵니다.", "It is cloudy, the wind is blowing and it is raining."), ("오전에 흐리고 오후에는 맑습니다.", "It is cloudy in the morning and clear in the afternoon."),
             ("시애틀은 날씨가 어때요?", "How is the weather in Seattle?"), ("오전에 안개가 끼고 오후에 비가 옵니다.", "In the morning fog forms and in the afternoon it rains."),
             ("눈이 와요.", "It is snowing."), ("눈이 내려요.", "It is snowing. (눈이 오다 / 내리다)")]
_KKI = [("오늘은 안개가 끼었습니다.", "It is foggy today."), ("오늘은 구름이 끼었습니다.", "It is cloudy today."), ("구름이 낍니다.", "Clouds are forming (now).")]
L1 = lesson(
    "Ch 6 · Topic A: The four seasons and the weather",
    "한국에는 사계절이 있습니다 · 봄 · 여름 · 가을 · 겨울 · 날씨 · 비 · 눈 · 바람",
    requires=[],
    cards=[
        card("What Chapter 6 teaches (날씨와 취미)",
             "Chapter 6, “Weather and Hobbies”, has three topic presentations, four grammar points, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: talk about the four seasons and the weather; and talk about hobbies and weekend activities in a simple phrase or sentence.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; -고 싶다 / 싶어하다 (want to; wish to); -(으)러 가다 / 오다 (go/come to do something); ㅂ irregular verbs; and the Sino-Korean syllable 구 (球). (The book’s “Let’s …” section, -(으)ㅂ시다, is in the chapter too.)"),
        card("Reading: Korea has four seasons",
             "Specialist Park is describing Korea’s seasons in class. (The English is mine.)",
             examples=passage(_A_PASSAGE)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s.",
             tables=[ktable(_A_PAIRS)]),
        card("The four seasons and their weather",
             "From the passage (the pairing is mine).",
             tables=[table(["Season", "Weather word", "Meaning"], [list(r) for r in _WX], say=[0, 1])]),
        card("Describing the weather: models",
             "Activity 1 gives the weather phrase 눈이 오다 / 내리다 (to snow) for a picture; Activity 2 asks you to describe the weather icons and gives these models (and the dialog about Seattle). The English is mine; the pictures and icons are not reproduced.",
             tables=[sent_table(_WX_MODEL)]),
        card("A note on 끼었습니다 (past tense for the present weather)",
             "You will hear native speakers say 오늘은 안개가 끼었습니다, “it is foggy today”, or 오늘은 구름이 끼었습니다, “it is cloudy today”. Because 끼었습니다 is the past tense of 끼다, you may wonder why a Korean speaker would use the past tense to describe the present weather. 끼다 literally means “to form”. When you say 구름이 낍니다 (present tense) you are saying that clouds are forming now. When you say 구름이 끼었습니다 the sentence implies that clouds have already formed and, as a result, it is cloudy.",
             examples=[D(a, b) for a, b in _KKI]),
        card("Activities left out",
             "The SMART Board activities, the “creative writer” word-strip activity (writing sentences from pairs of word strips; the model 박 상병은 바닷가에서 영화 보기 / 달리기를 합니다 is from the book’s strips), Follow-up 1 (listening to four short passages about seasons and weather), Follow-up 2 (pair work describing the climate of a country), Activity 1 (writing the weather under nine pictures, then listening) and Activity 2 (the weather icons and the weather maps) are audio, picture, game or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS if k not in ("눈", "비", "많이", "아주", "높다", "끼다", "내리다", "덥다", "춥다")])
        + [mean("눈", "snow", ["rain", "wind", "fog"]), mean("비", "rain", ["snow", "wind", "fog"]), mean("바람", "wind", ["rain", "snow", "cloud"]), mean("안개", "fog", ["cloud", "rain", "wind"]),
           mean("구름", "cloud", ["fog", "rain", "the sky"]), mean("덥다", "(weather) to be hot", ["(weather) to be cold", "to be warm", "to be chilly"]), mean("춥다", "(weather) to be cold", ["(weather) to be hot", "to be warm", "to be clear"]),
           mean("높다", "to be high", ["to be low", "to be clear", "to be cloudy"]), mean("많이", "a lot; much", ["a little", "very", "often"]), mean("아주", "very (much); extremely", ["a little", "often", "always"]),
           mean("끼다", "(fog, cloud, etc.) to form", ["to blow", "to fall", "to be clear"]), mean("내리다", "(rain, snow) to fall; to come down", ["to blow", "to form", "to be clear"])]
        + _tr(_A_PASSAGE, None)
        + [M("Which season is warm?", "봄", ["여름", "가을", "겨울"], "봄에는 날씨가 따뜻합니다."), M("Which season is very hot?", "여름", ["봄", "가을", "겨울"], "여름은 아주 덥습니다."),
           M("Which season is a little chilly with a high, clear sky?", "가을", ["봄", "여름", "겨울"], "가을에는 조금 쌀쌀합니다. 하늘이 높고 맑습니다."), M("Which season is cold with frequent snow?", "겨울", ["봄", "여름", "가을"], "겨울은 춥고 눈이 자주 옵니다."),
           M("In which season do clouds form a lot and it rains often?", "여름", ["봄", "가을", "겨울"], "구름이 많이 끼고 비가 자주 옵니다."), M("How many seasons does Korea have?", "Four (사계절)", ["Two", "Three", "Six"], "사계절 = four seasons."),
           M("Which sentence says the wind blows?", "바람이 붑니다.", ["비가 붑니다.", "눈이 붑니다.", "하늘이 붑니다."], "바람이 불다."), M("Which verb goes with 비 (rain) and 눈 (snow)?", "내리다 / 오다", ["불다", "끼다", "높다"], "비가 내리다 / 오다; 눈이 내리다 / 오다."),
           M("Which verb goes with 안개 and 구름?", "끼다", ["불다", "내리다", "높다"], "안개가 끼다; 구름이 끼다."), M("Which verb goes with 바람?", "불다", ["끼다", "내리다", "높다"], "바람이 불다."),
           M("What does 구름이 끼었습니다 imply?", "Clouds have formed, so it is cloudy now", ["Clouds are about to form", "It was cloudy yesterday", "It is raining"], "끼었습니다 implies the clouds have already formed."),
           M("What does 구름이 낍니다 say?", "Clouds are forming now", ["It is cloudy", "It rained", "The sky is clear"], "The present tense says they are forming now."),
           M("What does 끼다 literally mean?", "to form", ["to fall", "to blow", "to be clear"], "끼다 = to form."),
           M("Which sentence is “It is foggy”?", "안개가 끼었어요.", ["안개가 불어요.", "구름이 높아요.", "하늘이 맑아요."], "안개가 끼었어요."),
           M("What does 오전에 흐리고 오후에는 맑습니다 mean?", "It is cloudy in the morning and clear in the afternoon.", ["It is clear in the morning and cloudy in the afternoon.", "It rains in the morning.", "It is clear all day."], "흐리다 = cloudy; 맑다 = clear."),
           which("spring", "봄", ["여름", "가을", "겨울"]), which("weather", "날씨", ["하늘", "구름", "바람"]), which("the sky", "하늘", ["구름", "날씨", "바람"]), read_q("쌀쌀하다"), read_q("따뜻합니다"), read_q("흐리고")]
    ),
)

# ================================================================== Topic B
_B_DIALOG = [
    ("현준", "영은아, 넌 취미가 뭐야?", "Youngeun, what’s your hobby?"),
    ("영은", "음, 내 취미는 여행이야. 그리고 독서도 좋아해. 넌 취미가 뭐야?", "Hmm, my hobby is traveling. And I like reading too. What’s your hobby?"),
    ("현준", "내 취미는 운동이야. 농구, 축구, 테니스를 좋아해.", "My hobby is sports. I like basketball, soccer and tennis."),
    ("영은", "테니스? 너 테니스 잘 쳐?", "Tennis? Are you good at tennis?"),
    ("현준", "응, 조금 쳐. 너도 테니스 쳐?", "Yeah, I play a little. Do you play tennis too?"),
    ("영은", "아니, 나는 테니스 못 쳐. 하지만 배우고 싶어. 어려워?", "No, I can’t play tennis. But I want to learn. Is it hard?"),
    ("현준", "아니, 쉬워. 그럼, 너는 어떤 운동을 좋아해?", "No, it’s easy. Then what kind of sport do you like?"),
    ("영은", "난 수영을 좋아해. 그리고 겨울에는 스키를 자주 타.", "I like swimming. And in winter I often ski."),
    ("현준", "그래? 스키 재미있어?", "Really? Is skiing fun?"),
    ("영은", "응, 아주 재미있어.", "Yeah, it’s a lot of fun."),
]
_B_PAIRS = [
    ("고 싶다", "want to; wish to; like to"), ("골프", "golf"), ("농구", "basketball"), ("독서", "reading (books)"), ("못", "unable to; cannot (못 + verb)"), ("배구", "volleyball"), ("배우다", "to learn"),
    ("볼링", "bowling"), ("쉽다", "to be easy"), ("스노보드", "snowboard"), ("스케이트", "skate"), ("스키", "ski"), ("야구", "baseball; “field ball”"), ("어떤", "which; what kind"), ("어렵다", "to be difficult"),
    ("여행", "travels"), ("여행하다", "to travel"), ("재미있다", "to be fun; to be enjoyable; “fun exists”"), ("좋아하다", "to like"), ("축구", "soccer; football; “kicking ball”"), ("취미", "a hobby"),
    ("치다", "to hit; to strike; to play (tennis, ping-pong, golf, etc.)"), ("타다", "to ride; to get on"), ("탁구", "table tennis; “high table ball”"), ("테니스", "tennis"), ("하지만", "but; however"),
]
_SPORT = [("하다", ["수영", "농구", "등산", "축구", "야구", "배구"]), ("타다", ["스키", "스노보드", "스케이트", "자전거"]), ("치다", ["골프", "테니스", "볼링", "탁구"])]
_SPORT_V = {s: v for v, ss in [("하다", _SPORT[0][1]), ("타다", _SPORT[1][1]), ("치다", _SPORT[2][1])] for s in ss}
_SPORT_EN = {"수영": "swimming", "농구": "basketball", "등산": "hiking", "축구": "soccer", "야구": "baseball", "배구": "volleyball", "스키": "skiing", "스노보드": "snowboarding", "스케이트": "skating",
             "자전거": "cycling", "골프": "golf", "테니스": "tennis", "볼링": "bowling", "탁구": "table tennis"}
_GUESS_GU = [("농구", "basketball (籠 a basket + 球 a ball)"), ("축구", "soccer; football (蹴 kick + 球)"), ("야구", "baseball (野 a field + 球)")]
L2 = lesson(
    "Ch 6 · Topic B: Hobbies and sports",
    "내 취미는 독서야 · 취미 · 농구 · 축구 · 테니스 · 스키 · 구 (球)",
    requires=[],
    cards=[
        card("Dialog: my hobby is reading books",
             "Hyunjoon is having a conversation with his friend Youngeun about their hobbies. They are friends, so they use the informal blunt style from Chapter 5. The book notes that 넌 is a contracted form of 너는 and 난 is a contracted form of 나는. The English is mine.",
             examples=dlg(_B_DIALOG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s. The book lists -고 싶다 / 고 싶어하다 and 어떤 ~ and 못 + verb here; the endings are explained in the grammar lessons.",
             tables=[ktable(_B_PAIRS)]),
        card("Sino-Korean in use: 구 (球)",
             "This Sino-Korean syllable means a ball or sphere, as in 지구 (the earth; “sphere of earth”) and 전구 (light bulb; “electric ball”). It is also used to mean “-ball”, as in baseball, basketball, volleyball, kickball and so on. The book asks you to guess 농구, 축구 and 야구 (its notes: 농 籠 a basket, 축 蹴 kick, 야 野 a field); the meanings are mine.",
             tables=[ktable([("지구", "the earth; “sphere of earth”"), ("전구", "a light bulb; “electric ball”")] + _GUESS_GU)]),
        card("Which verb goes with which sport?",
             "Depending on the type of sport, Koreans use one of three verbs: ~하다 (to do), ~타다 (to ride) or ~치다 (to hit). The sports in the ~치다 group are also used with the verb 하다, as in 골프를 하다 and 테니스를 하다.",
             tables=[table(["Verb", "Sports"], [[v, ", ".join(ss)] for v, ss in _SPORT], say=[0, 1])],
             examples=[D("저는 수영을 해요.", "I swim."), D("저는 스키를 타요.", "I ski."), D("저는 테니스를 쳐요.", "I play tennis."), D("저는 골프를 해요.", "I play golf. (골프 also works with 하다)")]),
        card("Activities left out",
             "The SMART Board activities, the pair role-play study of Topic B (listing the hobbies of Hyunjoon and Youngeun in a table; key: Hyunjoon likes sports (basketball, soccer, tennis); Youngeun likes traveling, reading and swimming, and skis in winter), Follow-up 1 and Follow-up 2 (listening to dialogs about hobbies) are audio or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS if k not in ("고 싶다", "못", "어떤", "여행하다", "치다", "타다", "하지만", "스키", "스케이트", "스노보드", "볼링", "골프", "테니스")])
        + [mean("치다", "to hit; to play (tennis, golf)", ["to ride", "to do", "to learn"]), mean("타다", "to ride; to get on", ["to hit", "to do", "to learn"]), mean("하지만", "but; however", ["so; therefore", "and", "also"]),
           mean("스키", "ski", ["skate", "snowboard", "bowling"]), mean("스케이트", "skate", ["ski", "snowboard", "bowling"]), mean("스노보드", "snowboard", ["ski", "skate", "bowling"]), mean("볼링", "bowling", ["golf", "tennis", "ski"]),
           mean("골프", "golf", ["tennis", "bowling", "ski"]), mean("테니스", "tennis", ["golf", "bowling", "ski"]), mean("어떤", "which; what kind", ["when", "where", "how"]), mean("못", "unable to; cannot", ["not", "want to", "also"])]
        + [M(f"Which verb goes with {s} ({_SPORT_EN[s]})?", _SPORT_V[s], [x for x in ("하다", "타다", "치다") if x != _SPORT_V[s]], f"{s} takes {_SPORT_V[s]}.") for s in _SPORT_V if s != "자전거"]
        + [M("Which verb goes with 자전거 (bicycle)?", "타다", ["치다", "하다", "먹다"], "자전거를 타다.")]
        + [M(f"What does {a} mean?", b, [x for x in {y for _, y in _GUESS_GU if y != b}][:3], f"{a}: {b}.") for a, b in _GUESS_GU]
        + [M("What does the Sino-Korean syllable 구 (球) mean?", "a ball; a sphere", ["a field", "a basket", "a kick"], "구 (球) = ball: 농구, 축구, 야구."), M("What does 지구 mean?", "the earth; “sphere of earth”", ["a light bulb", "a ball game", "a field"], "지구 = earth."),
           M("What does 전구 mean?", "a light bulb; “electric ball”", ["the earth", "a ball game", "a field"], "전구 = light bulb.")]
        + _tr(_B_DIALOG[:0] and [] or [(a, b) for _, a, b in _B_DIALOG], None)
        + [M("What is Youngeun’s hobby?", "Traveling (and reading)", ["Basketball", "Swimming only", "Golf"], "내 취미는 여행이야. 그리고 독서도 좋아해."), M("What is Hyunjoon’s hobby?", "Sports", ["Traveling", "Reading", "Swimming"], "내 취미는 운동이야."),
           M("Which sports does Hyunjoon like?", "Basketball, soccer and tennis", ["Golf, bowling and skiing", "Swimming and skiing", "Baseball and volleyball"], "농구, 축구, 테니스를 좋아해."),
           M("Why can’t Youngeun play tennis?", "She hasn’t learned it (she wants to learn)", ["She dislikes it", "It is too easy", "She is injured"], "나는 테니스 못 쳐. 하지만 배우고 싶어."), M("Which sport does Youngeun like?", "Swimming (and skiing in winter)", ["Tennis", "Golf", "Bowling"], "난 수영을 좋아해. 그리고 겨울에는 스키를 자주 타."),
           M("What does 스키 재미있어? ask?", "Is skiing fun?", ["Is skiing hard?", "Do you ski?", "Where do you ski?"], "재미있다 = to be fun."), M("What is 넌?", "A contraction of 너는", ["A contraction of 나는", "A contraction of 너도", "A different word"], "넌 = 너는; 난 = 나는."),
           read_q("취미"), read_q("재미있다"), read_q("어렵다"), which("a hobby", "취미", ["여행", "독서", "운동"])]
    ),
)

# ================================================================== Grammar A: ㅂ irregular
_BV = [("춥다", "to be cold"), ("덥다", "to be hot"), ("쉽다", "to be easy"), ("어렵다", "to be difficult"), ("가깝다", "to be close; to be near"), ("고맙다", "to be thankful"), ("반갑다", "to be glad")]
_BEX = [("만나서 반가워요.", "Nice to meet you."), ("날씨가 조금 추워요.", "The weather is a little cold."), ("중국어가 어려워요.", "Chinese is difficult.")]
_BFU2 = [("여기에서 공군 기숙사가 가까워요.", "가깝다", "The Air Force dormitory is close to here."), ("한국의 여름은 아주 더워요.", "덥다", "Summer in Korea is very hot."),
         ("몬트레이의 겨울은 안 춥습니다.", "춥다", "Winter in Monterey is not cold."), ("오늘 저녁 식사 고마워요.", "고맙다", "Thank you for dinner tonight.")]
L3 = lesson(
    "Ch 6 · Grammar A: ㅂ irregular verbs",
    "춥다 → 추워요 · 덥다 → 더워요 · 쉽다 → 쉬워요 · 어렵다 → 어려워요 · 가깝다 · 고맙다 · 반갑다",
    requires=[],
    cards=[
        card("Stative verbs whose stems end in ㅂ",
             "So far you have learned quite a few stative verbs whose stems end in ㅂ: 쉽다 (to be easy), 어렵다 (to be difficult), 춥다 (to be cold), 덥다 (to be hot), 가깝다 (to be close; to be near), 반갑다 (to be glad) and 고맙다 (to be thankful). "
             "These are commonly known as ㅂ irregular verbs, because when the verb stem is followed by a vowel in conjugation, the ㅂ is dropped from the stem and 우 is added.",
             tables=[table(["Condition", "Rule", "Example"], [["The stem ends in ㅂ and is followed by a vowel", "drop ㅂ and add 우", "덥 + 어요 → 더우어요 → 더워요; 쉽 + 어요 → 쉬우어요 → 쉬워요"]])],
             examples=[D(a, b) for a, b in _BEX]),
        card("Follow-up 1: fill in the forms",
             "The book gives the table of seven ㅂ irregular verbs and asks for the -(스)ㅂ니다, -아/어요 and -아/어서 forms (the first row, 춥다, is given). The completed table is my key.",
             tables=[table(["Dictionary form", "Meaning", "-(스)ㅂ니다", "-아/어요", "-아/어서"], [[v, m, *b_irregular(v)] for v, m in _BV], say=[0, 2, 3, 4])]),
        card("Follow-up 2: read and translate",
             "The book gives four sentences containing a ㅂ irregular verb and asks you to write the dictionary form and translate. The sentences are the book’s; the dictionary forms and the English are my key.",
             tables=[table(["Sentence", "Dictionary form", "Meaning"], [list(r) for r in _BFU2], say=[0, 1])]),
    ],
    exercises=uniq(
        [M(f"What does {v} mean?", m, [x for _, x in _BV if x != m][:3], f"{v} = {m}.") for v, m in _BV]
        + [M(f"Which is the -아/어요 form of {v} ({m})?", b_irregular(v)[1], [x for x in {stem(v) + "어요", stem(v)[:-1] + "어요", stem(v) + "아요", stem(v)[:-1] + "우요"} if x != b_irregular(v)[1]][:3], f"{v}: drop ㅂ, add 우 → {b_irregular(v)[1]}.") for v, m in _BV]
        + [M(f"Which is the -아/어서 form of {v} ({m})?", b_irregular(v)[2], [x for x in {stem(v) + "어서", stem(v)[:-1] + "어서", stem(v) + "아서", stem(v) + "고"} if x != b_irregular(v)[2]][:3], f"{v}: drop ㅂ, add 우 → {b_irregular(v)[2]}.") for v, m in _BV]
        + [M(f"Which is the formal polite form of {v} ({m})?", b_irregular(v)[0], [b_irregular(v)[1], stem(v)[:-1] + "습니다", stem(v)[:-1] + "ㅂ니다"], f"Before a consonant the ㅂ stays: {b_irregular(v)[0]}.") for v, m in _BV]
        + [M(f"What does {a} mean?", b, ([x for _, x in _BEX if x != b] + [x for _, _, x in _BFU2])[:3], f"{a} means “{b}”.") for a, b in _BEX]
        + [M(f"What does {a} mean?", c, [x for _, _, x in _BFU2 if x != c][:3], f"{a} means “{c}”.") for a, _, c in _BFU2]
        + [M(f"Which is the dictionary form of the verb in “{a}”?", v, [x for x, _ in _BV if x != v][:3], f"{a} contains {v}.") for a, v, _ in _BFU2]
        + [F("만나서 ___. (Nice to meet you)", "반가워요", ["반갑어요", "반가요"], "반갑다: drop ㅂ, add 우 → 반가워요."), F("날씨가 조금 ___. (cold)", "추워요", ["춥어요", "추요"], "춥다 → 추워요."),
           F("중국어가 ___. (difficult)", "어려워요", ["어렵어요", "어려요"], "어렵다 → 어려워요."), F("한국의 여름은 아주 ___. (hot)", "더워요", ["덥어요", "더요"], "덥다 → 더워요."),
           M("What happens to the ㅂ of a ㅂ irregular stem before a vowel?", "It is dropped and 우 is added", ["It stays", "It becomes ㄹ", "It becomes ㅁ"], "덥 + 어요 → 더워요."),
           M("What happens to the ㅂ before a consonant (as in -습니다)?", "It stays: 춥습니다", ["It is dropped: 추습니다", "It becomes 우", "It becomes ㅁ"], "춥습니다 keeps the ㅂ."),
           read_q("추워요"), read_q("어려워요"), read_q("고마워요"), read_q("반가워요")]
    ),
)

# ================================================================== Grammar B: -고 싶다
_WANT_EX = [("나는 아이스크림을 먹고 싶어요.", "I want to eat ice cream."), ("아이스크림을 먹고 싶어요?", "Do you want to eat ice cream?"), ("제 아내도 아이스크림을 먹고 싶어해요.", "My wife wants to eat ice cream too."),
            ("저는 오늘 농구를 하고 싶어요.", "I want to play basketball today."), ("저는 이번 주말에 등산을 하고 싶어요.", "I want to hike this weekend."), ("제 아내는 피아노를 배우고 싶어해요.", "My wife wants to learn piano."),
            ("제 아이들은 스키를 타고 싶어해요.", "My children want to ski.")]
_LEE = [("이번 크리스마스에 저는 레이크 타호에 가고 싶어요.", "This Christmas I want to go to Lake Tahoe."), ("거기에서 스키를 타고 싶어요.", "I want to ski there."),
        ("하지만 제 아내는 이번 크리스마스에 유럽에 가고 싶어해요.", "But my wife wants to go to Europe this Christmas."), ("제 아들은 친구들과 같이 테니스를 치고 싶어해요.", "My son wants to play tennis with his friends."),
        ("그리고 제 딸은 집에서 비디오 게임을 하고 싶어해요.", "And my daughter wants to play video games at home.")]
_WV = [("먹다", "to eat"), ("공부하다", "to study"), ("가다", "to go"), ("배우다", "to learn"), ("타다", "to ride"), ("치다", "to play (tennis)"), ("만나다", "to meet"), ("보다", "to see; to watch"), ("읽다", "to read"), ("마시다", "to drink")]
L4 = lesson(
    "Ch 6 · Grammar B: expressing wishes with -고 싶다 and -고 싶어하다",
    "먹고 싶어요 · 가고 싶어요 · 먹고 싶어해요 · 배우고 싶어해요",
    requires=[],
    cards=[
        card("Want to, wish to, would like to",
             "In English we use “want to”, “wish to” and “would like to”. In Korean we use -고 싶다 or -고 싶어하다. If the subject is the first person (I, we) or the second person (you), -고 싶다 is used; if the subject is the third person (he, she, John, they and so on), -고 싶어하다 is used. They attach to the stem of an action verb.",
             tables=[table(["Condition", "Rule", "Example"], [["The subject is 1st or 2nd person (I, we, you)", "add 고 싶다 to the verb stem", "먹다 → 먹고 싶다; 공부하다 → 공부하고 싶다"], ["The subject is 3rd person (he, she, they, etc.)", "add 고 싶어하다 to the verb stem", "먹다 → 먹고 싶어하다; 공부하다 → 공부하고 싶어하다"]])],
             examples=[D(a, b) for a, b in _WANT_EX]),
        card("The forms",
             "The forms below are mine; the polite endings follow -아요/어요 (싶다 → 싶어요, 싶어하다 → 싶어해요).",
             tables=[table(["Dictionary form", "Meaning", "I / you want to", "He / she wants to"], [[v, m, want(v)[:-1] + "어요", want(v, True)[:-2] + "해요"] for v, m in _WV], say=[0, 2, 3])]),
        card("Follow-up 3: Mr. Lee’s family’s Christmas wish list",
             "The book prints Mr. Lee’s family’s Christmas wish list and asks you to circle the correct form in each pair of parentheses (고 싶어요 or 고 싶어해요). The text with the right forms is below (the English and the key are mine): the subject is 저 (I) → 고 싶어요; 제 아내 / 제 아들 / 제 딸 (third person) → 고 싶어해요.",
             examples=[D(a, b) for a, b in _LEE]),
        card("Activities left out",
             "Follow-up 4 (two video clips and a listening exercise about what people want to do) and Follow-up 5 (talking with a partner about what you want to do this Christmas, then telling a new partner what the first one wants; the model is 이번 크리스마스에 뭐 하고 싶어요? 저는 부모님과 친구를 만나고 싶어요. 그리고 스노보드를 타고 싶고 영화를 보고 싶어요. / 장 일병은 이번 크리스마스에 부모님과 친구를 만나고 싶어해요) are audio, video or class activities.",
             examples=[D("이번 크리스마스에 뭐 하고 싶어요?", "What do you want to do this Christmas?"), D("저는 부모님과 친구를 만나고 싶어요.", "I want to meet my parents and a friend."),
                       D("장 일병은 이번 크리스마스에 부모님과 친구를 만나고 싶어해요.", "PFC Jang wants to meet his parents and a friend this Christmas.")]),
    ],
    exercises=uniq(
        [M(f"Which means “I want to {m.replace('to ', '', 1).split(';')[0]}” ({v})?", want(v)[:-1] + "어요", [want(v, True)[:-2] + "해요", formal(v), informal(v)], f"First person → -고 싶어요: {want(v)[:-1] + '어요'}.") for v, m in _WV if v not in ("치다",)]
        + [M(f"Which means “my wife wants to {m.replace('to ', '', 1).split(';')[0]}” ({v})?", want(v, True)[:-2] + "해요", [want(v)[:-1] + "어요", stem(v) + "고 싶습니다", informal(v)], f"Third person → -고 싶어해요: {want(v, True)[:-1] + '해요'}.") for v, m in _WV if v not in ("치다",)]
        + [M(f"What does {a} mean?", b, [x for _, x in _WANT_EX + _LEE if x != b][:3], f"{a} means “{b}”.") for a, b in _WANT_EX + _LEE]
        + [F("저는 오늘 농구를 하___ 싶어요.", "고", ["어", "면"], "stem + 고 싶다."), F("제 아내는 피아노를 배우고 ___.", "싶어해요", ["싶어요", "싶습니다"], "Third person → 싶어하다."),
           F("나는 아이스크림을 먹고 ___. (I want)", "싶어요", ["싶어해요", "싶어하다"], "First person → 싶다."), F("이번 크리스마스에 저는 레이크 타호에 가고 ___.", "싶어요", ["싶어해요", "싶습니"], "저 = I → 싶어요."),
           F("제 아들은 친구들과 같이 테니스를 치고 ___.", "싶어해요", ["싶어요", "싶습니"], "제 아들 = third person → 싶어해요."),
           M("When is -고 싶다 used?", "When the subject is I, we or you", ["When the subject is he or she", "Only in questions", "Only with stative verbs"], "-고 싶다 for 1st and 2nd person."),
           M("When is -고 싶어하다 used?", "When the subject is he, she or they", ["When the subject is I or we", "When the subject is you", "Only with 이다"], "-고 싶어하다 for the third person."),
           M("Which sentence asks “Do you want to eat ice cream?”", "아이스크림을 먹고 싶어요?", ["아이스크림을 먹고 싶어해요?", "아이스크림을 먹어요.", "아이스크림이 먹고 싶어요."], "A 2nd-person question → 싶어요?"),
           M("-고 싶다 attaches to the stem of which kind of verb?", "An action verb", ["A stative verb", "Only 이다", "Only 있다"], "action verb stem + 고 싶다.")]
        + [read_q("먹고 싶어요"), read_q("싶어해요"), read_q("배우고 싶어해요")]
    ),
)

# ================================================================== Topic C
_C_DIALOG = [
    ("마이크", "소연 씨는 주말에 보통 뭐 해요?", "Soyeon, what do you usually do on the weekend?"),
    ("강소연", "공원에서 산책해요. 그리고 집에서 음악도 들어요. 마이크 씨는 주말에 뭐 해요?", "I take a walk in the park. And I listen to music at home too. What do you do on weekends, Mike?"),
    ("마이크", "저는 토요일에 달리기를 해요. 그리고 저녁에는 영화를 보러 가요.", "On Saturdays I go running. And in the evening I go to see a movie."),
    ("강소연", "그럼, 일요일에는 뭐 해요?", "Then what do you do on Sundays?"),
    ("마이크", "일요일에는 바닷가에서 자전거를 타요. 그리고 가끔 골프도 쳐요.", "On Sundays I ride a bicycle at the beach. And sometimes I play golf too."),
    ("강소연", "저도 골프를 좋아해요. 그래서 골프장에 자주 가요.", "I like golf too. So I often go to the golf course."),
    ("마이크", "소연 씨는 이번 주말에 무슨 계획 있어요?", "Soyeon, do you have any plans this weekend?"),
    ("강소연", "아니요.", "No."),
    ("마이크", "그럼, 토요일에 같이 골프 칩시다.", "Then let’s play golf together on Saturday."),
    ("강소연", "좋아요. 토요일에 만나요.", "Sure. Let’s meet on Saturday."),
]
_C_PAIRS = [
    ("같이", "(along) with; together"), ("계획", "a plan"), ("계획하다", "to plan"), ("골프장", "a golf course; “golf place”"), ("공원", "a park"), ("구경", "watching; sightseeing"), ("구경하다", "to watch; to sightsee"),
    ("달리기", "running; jogging"), ("만나다", "to meet; to see"), ("바닷가", "the beach; the coast; the seaside"), ("산책", "a walk; a stroll"), ("산책하다", "to take a walk"), ("야영", "camping"), ("야영하다", "to camp"),
    ("영화", "a movie"), ("음악", "music"), ("이번", "this (time)"), ("자전거", "a bicycle"), ("전화", "a telephone; a phone call"), ("전화하다", "to make a phone call"),
]
L5 = lesson(
    "Ch 6 · Topic C: Weekend activities",
    "주말에 보통 뭐 하세요? · 산책 · 달리기 · 영화 · 자전거 · 골프장 · 같이",
    requires=[],
    cards=[
        card("Dialog: what do you usually do on the weekend?",
             "Mike, a DLI student, and his conversation partner Soyeon, a graduate student, are talking about their weekend activities and hobbies. The book’s footnote says the -기 in 달리기 (running) is a “gerund maker” attached to a verb stem; you will learn it in a later chapter. (The English is mine.)",
             examples=dlg(_C_DIALOG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (the book lists 계획(하다), 구경(하다), 산책(하다), 야영(하다) and 전화(하다) with (하다) in parentheses, 이번 ~, and the endings -(으)러 가다/오다 and -(으)ㅂ시다, which are in the grammar lessons).",
             tables=[ktable(_C_PAIRS)]),
        card("Pronunciation guide: 같이",
             "The book’s footnote says 같이 is pronounced /가치/, not /가티/ (palatalization: ㅌ before 이 becomes ㅊ).",
             tables=[ptable([("같이", pr("같이", "가치"), "together")])]),
        card("Activities left out",
             "The SMART Board activity, the group summaries of Mike’s and Soyeon’s hobbies (Presentation Activity b–f; the Venn diagram of their hobbies; key: Mike: running, movies, riding a bicycle at the beach, golf; Soyeon: walking in the park, listening to music, golf), Follow-up 1 (a fill-in e-mail from Jennifer: see the Activities lesson) and Follow-up 2 (listening to suggestions) are class or audio activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS if k not in ("구경", "산책", "야영", "전화", "계획", "이번", "같이", "음악")])
        + [mean("같이", "(along) with; together", ["alone", "early", "often"]), mean("계획", "a plan", ["a hobby", "a phone call", "a weekend"]), mean("이번", "this (time)", ["last", "next", "every"]), mean("음악", "music", ["a movie", "a walk", "a park"]),
           mean("산책", "a walk; a stroll", ["running", "camping", "sightseeing"]), mean("야영", "camping", ["a walk", "running", "sightseeing"]), mean("구경", "watching; sightseeing", ["a walk", "camping", "running"]), mean("전화", "a telephone; a phone call", ["a plan", "music", "a movie"])]
        + _tr([(a, b) for _, a, b in _C_DIALOG], None)
        + [M("What does Soyeon do on weekends?", "Takes a walk in the park and listens to music at home", ["Goes running", "Rides a bicycle", "Plays tennis"], "공원에서 산책해요. 그리고 집에서 음악도 들어요."),
           M("What does Mike do on Saturdays?", "Goes running (and to a movie in the evening)", ["Takes a walk", "Plays golf", "Rides a bicycle"], "토요일에 달리기를 해요. 그리고 저녁에는 영화를 보러 가요."),
           M("What does Mike do on Sundays?", "Rides a bicycle at the beach (and sometimes plays golf)", ["Goes running", "Takes a walk", "Goes to a movie"], "일요일에는 바닷가에서 자전거를 타요."),
           M("Why does Soyeon often go to the golf course?", "She likes golf", ["She works there", "Her family lives there", "She has a plan"], "저도 골프를 좋아해요. 그래서 골프장에 자주 가요."),
           M("What does Mike suggest?", "Playing golf together on Saturday", ["Going to a movie on Sunday", "Going running together", "Meeting at the park"], "토요일에 같이 골프 칩시다."),
           M("Which is the right pronunciation of 같이?", "가치", ["가티", "같이", "갇이"], "ㅌ before 이 → ㅊ: /가치/."),
           M("Which verb goes with 자전거?", "타다", ["치다", "하다", "보다"], "자전거를 타요."), M("Which verb goes with 골프?", "치다", ["타다", "먹다", "듣다"], "골프도 쳐요."),
           read_q("달리기"), read_q("바닷가"), read_q("같이"), said_q("같이")]
    ),
)

# ================================================================== Grammar C: let's
_LETS_EX = [("점심(을) 먹읍시다.", "Let’s eat lunch."), ("커피를 마십시다.", "Let’s drink coffee."), ("열 시에 학교에서 만납시다.", "Let’s meet at school at ten o’clock."), ("한국식당에서 먹읍시다.", "Let’s eat at a Korean restaurant.")]
_LETS_B = [("열 시에 학교에서 만나자.", "Let’s meet at school at ten o’clock."), ("한국식당에서 먹자.", "Let’s eat at a Korean restaurant.")]
_LV = [("먹다", "to eat"), ("가다", "to go"), ("마시다", "to drink"), ("만나다", "to meet"), ("치다", "to play (tennis, golf)"), ("공부하다", "to study"), ("읽다", "to read"), ("보다", "to watch"), ("산책하다", "to take a walk"), ("타다", "to ride"), ("하다", "to do"), ("쉬다", "to rest")]
_LETS_FU = [("테니스를 치다", "테니스를 칩시다", "Let’s play tennis."), ("공원에서 산책하다", "공원에서 산책합시다", "Let’s take a walk in the park.")]
_CIRCLE = [("우리, 이번 주말에 영화 보러 갑시다.", "Let’s go see a movie this weekend."), ("좋아요. 그리고 같이 저녁 먹읍시다.", "Sure. And let’s have dinner together."),
           ("좋아요. 그럼 그 다음에 뭐 할까요?", "Sure. Then what shall we do after that?"), ("글쎄요, 저녁 식사 후에 공부합시다.", "Well, let’s study after dinner.")]
L6 = lesson(
    "Ch 6 · Grammar C: making suggestions with -(으)ㅂ시다 (“Let’s …”)",
    "먹읍시다 · 갑시다 · 만납시다 · 마십시다 · 먹자 · 가자",
    requires=[],
    cards=[
        card("Let’s …",
             "In English we often say “Let’s …” to make suggestions, as in “Let’s eat lunch” or “Let’s drink coffee.” Likewise Koreans make suggestions with -(으)ㅂ시다.",
             tables=[table(["Condition", "Rule", "Example"], [["A verb stem ends in a consonant", "add 읍시다", "먹다 → 먹 + 읍시다 → 먹읍시다"], ["A verb stem ends in a vowel", "add ㅂ시다", "가다 → 가 + ㅂ시다 → 갑시다"]], title="verb stem + (으)ㅂ시다")],
             examples=[D(a, b) for a, b in _LETS_EX]),
        card("The blunt form: -자",
             "The blunt form of -(으)ㅂ시다 is -자 (for use with friends, like the informal blunt style of Chapter 5).",
             examples=[D(a, b) for a, b in _LETS_B],
             tables=[table(["Dictionary form", "Meaning", "Let’s … (-(으)ㅂ시다)", "Blunt (-자)"], [[v, m, lets(v), lets_blunt(v)] for v, m in _LV], title="Forms (mine)", say=[0, 2, 3])]),
        card("Follow-up 1: change the phrase into a suggestion",
             "In the book partners read verbal phrases (Lists A and B, not printed) and the other repeats each as a suggestion. The book’s models: 테니스를 치다 → 테니스를 칩시다; 공원에서 산책하다 → 공원에서 산책합시다.",
             tables=[table(["Phrase", "Suggestion", "Meaning"], [list(r) for r in _LETS_FU], say=[0, 1])]),
        card("Follow-up 4: concentric-circle talk (a model conversation)",
             "In the book, students in two circles suggest weekend activities to each other. The model is below; 할까요 (“shall we?”) is a form the book teaches in Chapter 7. (The English is mine.)",
             examples=dlg([("A", _CIRCLE[0][0], _CIRCLE[0][1]), ("B", _CIRCLE[1][0], _CIRCLE[1][1]), ("A", _CIRCLE[2][0], _CIRCLE[2][1]), ("B", _CIRCLE[3][0], _CIRCLE[3][1])])),
    ],
    exercises=uniq(
        [M(f"Which means “Let’s {m.replace('to ', '', 1).split(';')[0]}” ({v})?", lets(v), [x for x in {stem(v) + "읍시다", stem(v) + "세요", stem(v) + "자요", formal(v)} if x != lets(v)][:3], f"{v} → {lets(v)}.") for v, m in _LV]
        + [M(f"Which is the blunt form (-자) of {lets(v)}?", lets_blunt(v), [lets(v), stem(v) + "세요", formal(v)], f"The blunt form of -(으)ㅂ시다 is -자: {lets_blunt(v)}.") for v, m in _LV[:6]]
        + [M(f"What does {a} mean?", b, [x for _, x in _LETS_EX + _LETS_B + _CIRCLE if x != b][:3], f"{a} means “{b}”.") for a, b in _LETS_EX + _CIRCLE]
        + [F("점심(을) 먹___.", "읍시다", ["ㅂ시다", "자요"], "먹 ends in a consonant → 읍시다."), F("학교에서 만___. (Let’s meet at school)", "납시다", ["나읍시다", "난시다"], "만나다: 만나 + ㅂ시다 = 만납시다."),
           F("테니스를 ___. (Let’s play tennis)", "칩시다", ["치읍시다", "칩니다"], "치 + ㅂ시다 = 칩시다."), F("공원에서 산책___.", "합시다", ["하읍시다", "합니다"], "산책하 + ㅂ시다 → 산책합시다."),
           M("When is 읍시다 added?", "When the verb stem ends in a consonant", ["When it ends in a vowel", "Always", "Never"], "먹읍시다."), M("When is ㅂ시다 added?", "When the verb stem ends in a vowel", ["When it ends in a consonant", "Always", "Never"], "갑시다."),
           M("What is the blunt form of -(으)ㅂ시다?", "-자", ["-어", "-요", "-세요"], "한국식당에서 먹자."), M("-(으)ㅂ시다 is used to…", "make a suggestion (“Let’s …”)", ["make a request", "ask a question", "say you want to"], "Let’s …")]
        + [read_q("먹읍시다"), read_q("칩시다"), read_q("마십시다"), read_q("만납시다")]
    ),
)

# ================================================================== Grammar D: -(으)러 가다/오다
_PUR_EX = [("쇼핑하러 산호세에 갑니다.", "I am going to San Jose to do shopping."), ("공부하러 도서관에 갑니다.", "I am going to the library to study."), ("점심을 먹으러 (식당에) 갑니다.", "I am going (to the restaurant) to eat lunch."),
           ("점심을 먹으러 (식당에) 옵니다.", "I am coming (to the restaurant) to eat lunch."), ("저는 매일 수업 후에 몬트레이 체육관에 수영하러 갑니다.", "Every day after class I go to the Monterey gym to swim."), ("오늘 저녁 먹으러 우리 집에 와.", "Come to my house to eat dinner tonight.")]
_PV = [("먹다", "to eat"), ("공부하다", "to study"), ("보다", "to watch"), ("만나다", "to meet"), ("운동하다", "to exercise"), ("수영하다", "to swim"), ("쇼핑하다", "to shop"), ("읽다", "to read"), ("마시다", "to drink"), ("놀다", "to play")]
_SGT = [("저는 토요일에는 보통 친구를 만나러 친구 집에 갑니다.", "On Saturdays I usually go to a friend’s house to meet a friend."), ("그리고 친구와 함께 영화를 보러 영화관에 갑니다.", "And together with my friend I go to the movie theater to watch a movie."),
        ("가끔 산책하러 공원에 갑니다.", "Sometimes I go to the park to take a walk."), ("산책을 한 후에는 점심을 먹으러 식당에 갑니다.", "After the walk I go to a restaurant to eat lunch."), ("그리고 운동하러 체육관에 갑니다.", "And I go to the gym to work out.")]
L7 = lesson(
    "Ch 6 · Grammar D: the purpose of coming and going, -(으)러 가다/오다",
    "먹으러 가요 · 공부하러 가요 · 영화를 보러 가요 · 수영하러 가요",
    requires=[],
    cards=[
        card("To go to do something",
             "When we go to a restaurant to eat we say “I am going (to the restaurant) to eat.” “To eat” following the verb “is going” shows the purpose of going. Koreans express the purpose of coming and going with -(으)러 가다 or -(으)러 오다, as in 점심을 먹으러 (식당에) 갑니다 or 점심을 먹으러 (식당에) 옵니다.",
             tables=[table(["Condition", "Rule", "Example"], [["A verb stem ends in a consonant other than ㄹ", "add 으러 + 가다 / 오다", "먹다: 먹 + 으러 → 먹으러"], ["A verb stem ends in a vowel or ㄹ", "add 러 + 가다 / 오다", "공부하다: 공부하 + 러 → 공부하러"]], title="verb stem + (으)러 가다 / 오다")],
             examples=[D(a, b) for a, b in _PUR_EX]),
        card("The forms",
             "The forms below are mine.",
             tables=[table(["Dictionary form", "Meaning", "-(으)러"], [[v, m, purpose(v)] for v, m in _PV], say=[0, 2])]),
        card("Follow-up 2: SGT Thompson’s weekend",
             "The book prints a short introduction to SGT Thompson’s weekend with five blanks and asks you to choose a verb from the box (산책하다, 먹다, 만나다, 영화보다, 운동하다) and change it to -(으)러. The completed sentences are my key (the English is mine).",
             examples=[D(a, b) for a, b in _SGT]),
        card("Activities left out",
             "Follow-up 3 (four video clips with -(으)러 가다, -자 or -(으)ㅂ시다), Follow-up 4 (concentric-circle talk) and Activity 3 (using -(으)러 갑시다 / -(으)러 가자 in a long-weekend plan: a flyer made from the Monterey County visitors’ website) are video, web or class activities."),
    ],
    exercises=uniq(
        [M(f"Which is the purpose form (-(으)러) of {v} ({m})?", purpose(v), [x for x in {stem(v) + "으러", stem(v) + "러", stem(v) + "고", stem(v) + "서"} if x != purpose(v)][:3], f"{v} → {purpose(v)}.") for v, m in _PV]
        + [M(f"What does {a} mean?", b, [x for _, x in _PUR_EX + _SGT if x != b][:3], f"{a} means “{b}”.") for a, b in _PUR_EX + _SGT]
        + [F("공부하___ 도서관에 갑니다.", "러", ["으러", "고"], "공부하 ends in a vowel → 러."), F("점심을 먹___ 식당에 갑니다.", "으러", ["러", "고"], "먹 ends in a consonant → 으러."), F("영화를 보___ 영화관에 갑니다.", "러", ["으러", "고"], "보 ends in a vowel → 러."),
           F("친구를 만나___ 친구 집에 갑니다.", "러", ["으러", "고"], "만나 ends in a vowel → 러."), F("저는 매일 수영하러 체육관에 ___.", "갑니다", ["갑니까", "가서"], "-(으)러 + 가다."),
           M("What does -(으)러 가다 express?", "The purpose of going", ["Wanting to go", "Going and then doing", "Not going"], "-(으)러 shows the purpose of going or coming."),
           M("Which verbs follow -(으)러?", "가다 and 오다 (movement verbs)", ["있다 and 없다", "any verb", "하다 only"], "-(으)러 가다 / 오다."),
           M("When is 으러 added?", "When the stem ends in a consonant other than ㄹ", ["When the stem ends in a vowel", "When the stem ends in ㄹ", "Never"], "먹으러."), M("When is 러 added?", "When the stem ends in a vowel or ㄹ", ["When the stem ends in a consonant other than ㄹ", "Never", "Always"], "공부하러.")]
        + [read_q("먹으러"), read_q("공부하러"), read_q("보러")]
    ),
)

# ================================================================== Activities
_HYUN = [
    ("안녕하세요? 저는 이현수입니다.", "Hello. I am Lee Hyunsoo."), ("저는 운동을 아주 좋아합니다.", "I like sports very much."), ("특히 야구와 테니스를 좋아합니다.", "I especially like baseball and tennis."),
    ("저는 누나 한 명과 남동생 한 명이 있습니다.", "I have one older sister and one younger brother."), ("제 누나는 여행과 독서가 취미입니다.", "My older sister’s hobbies are traveling and reading."),
    ("그래서 여행을 자주 가고 책을 많이 읽습니다.", "So she often goes traveling and reads a lot of books."), ("그리고 제 남동생은 농구와 축구를 아주 좋아합니다.", "And my younger brother likes basketball and soccer very much."),
    ("그래서 자주 친구들하고 같이 농구와 축구를 합니다.", "So he often plays basketball and soccer with his friends."),
]
_CAMP = [("이번 주 주말 활동 계획입니다.", "This is the plan for this weekend’s activities."), ("하고 싶은 주말 활동이 있으면 캠프 본부에 전화하세요.", "If there is a weekend activity you want to do, please call the camp headquarters."),
         ("서울 롯데월드타워 구경", "Sightseeing at Lotte World Tower in Seoul"), ("영화 보기", "Watching a movie"), ("골프 치기", "Playing golf"), ("등산과 야영", "Hiking and camping"), ("한강 공원에서 달리기와 자전거 타기", "Running and riding a bicycle at Hangang Park")]
_JEN = [("영수 씨에게,", "To Youngsoo,"), ("주말에 보통 뭐해요?", "What do you usually do on weekends?"), ("저는 금요일 저녁에는 집에서 음악을 들어요.", "On Friday evenings I listen to music at home."),
        ("그리고 가끔 영화를 보러 가요.", "And sometimes I go to see a movie."), ("토요일에는 학교 운동장에서 달리기를 해요.", "On Saturdays I run on the school field."), ("가끔 친구들하고 같이 골프도 쳐요.", "Sometimes I play golf with friends too."),
        ("이번 주말에는 빅서에 야영하러 가요.", "This weekend I am going camping at Big Sur."), ("영수 씨, 다음 주말에 무슨 계획 있어요?", "Youngsoo, do you have any plans next weekend?"), ("한국어 연습하고 싶어요.", "I want to practice Korean."),
        ("주말에 만납시다.", "Let’s meet on the weekend."), ("전화하세요.", "Please call me."), ("그럼, 안녕.", "Well then, goodbye."), ("제니퍼", "Jennifer")]
_YS = [("영화 보기", "watching a movie"), ("야영", "camping"), ("공원산책", "a walk in the park"), ("자전거 타기", "riding a bicycle")]
L8 = lesson(
    "Ch 6 · Activities: hobbies, a camp plan and an e-mail",
    "한국어 활용 · 이현수의 취미 · 주말 활동 계획 · 제니퍼의 이메일",
    requires=[],
    cards=[
        card("Activity 1: Hyunsoo’s story",
             "The book prints Hyunsoo’s story about the hobbies and activities he and his family members enjoy and asks you to fill in a table. The text is the book’s (특히, “especially”, is not in the core list; the English and the table are mine).",
             examples=passage(_HYUN),
             tables=[table(["Family member", "Hobbies and activities"], [["Hyunsoo", "sports, especially baseball and tennis"], ["older sister", "traveling and reading"], ["younger brother", "basketball and soccer (with his friends)"]])]),
        card("Activity 2: weekend activities on a camping website",
             "The book prints part of the information about weekend activities posted on a camping website and asks what kinds of weekend activities students can take part in. The telephone number is left out. The -기 endings (영화 보기, 골프 치기) are the “gerund maker” that the book teaches in a later chapter; the English is mine.",
             tables=[sent_table(_CAMP)]),
        card("Follow-up 1 (Topic C): Jennifer’s e-mail to Youngsoo",
             "Jennifer, PV2, writes to her Korean conversation partner, Youngsoo. The book leaves blanks to be filled from a box of eight words (달리기, 계획, 야영, 자전거, 영화, 음악, 골프, 이번). The completed e-mail is my key: 음악, 영화, 달리기, 골프, 야영 and 계획 fill the blanks; 자전거 and 이번 are not needed. (The English is mine.)",
             examples=passage(_JEN)),
        card("Activity 1 (second set): Youngsoo’s weekend activities",
             "The book lists four of Youngsoo’s weekend activities and asks for the English meanings (the listening part is left out). The key is mine.",
             tables=[ktable(_YS)]),
        card("Activities left out",
             "Activity 2 of the first set (listening to three conversations and a video about hobbies), Activity 3 (a class survey and a flyer for an activity club of Korean and American soldiers) and the second set’s Activity 2b and 3 (a classmate survey and a long-weekend plan flyer) are audio, video, web or class activities."),
    ],
    exercises=uniq(
        _tr(_HYUN[1:], None)
        + _tr(_CAMP, None)
        + _tr(_JEN[1:11], None)
        + [M("Which sports does Hyunsoo especially like?", "Baseball and tennis", ["Basketball and soccer", "Golf and bowling", "Swimming and skiing"], "특히 야구와 테니스를 좋아합니다."),
           M("What are the older sister’s hobbies?", "Traveling and reading", ["Basketball and soccer", "Baseball and tennis", "Swimming"], "제 누나는 여행과 독서가 취미입니다."),
           M("What does the younger brother like?", "Basketball and soccer", ["Baseball and tennis", "Traveling and reading", "Golf"], "제 남동생은 농구와 축구를 아주 좋아합니다."),
           M("How many siblings does Hyunsoo have?", "Two (one older sister and one younger brother)", ["One", "Three", "None"], "누나 한 명과 남동생 한 명이 있습니다."),
           M("Where is Jennifer going camping this weekend?", "Big Sur", ["Seoul", "Lake Tahoe", "Monterey"], "이번 주말에는 빅서에 야영하러 가요."),
           M("What does Jennifer do on Saturdays?", "Runs on the school field", ["Rides a bicycle", "Goes camping", "Listens to music"], "토요일에는 학교 운동장에서 달리기를 해요."),
           M("What does Jennifer want to do with Youngsoo?", "Practice Korean", ["Play golf", "Go camping", "See a movie"], "한국어 연습하고 싶어요."),
           F("저는 금요일 저녁에는 집에서 ___을 들어요.", "음악", ["영화", "달리기"], "음악을 듣다."), F("그리고 가끔 ___를 보러 가요.", "영화", ["음악", "골프"], "영화를 보러 가다."),
           F("토요일에는 학교 운동장에서 ___를 해요.", "달리기", ["골프", "영화"], "달리기를 하다."), F("이번 주말에는 빅서에 ___하러 가요.", "야영", ["달리기", "음악"], "야영하러 가다."),
           F("영수 씨, 다음 주말에 무슨 ___ 있어요?", "계획", ["이번", "자전거"], "계획이 있다."),
           mean("영화 보기", "watching a movie", ["camping", "a walk in the park", "riding a bicycle"]), mean("야영", "camping", ["watching a movie", "a walk in the park", "riding a bicycle"]),
           mean("공원산책", "a walk in the park", ["camping", "watching a movie", "riding a bicycle"]), mean("자전거 타기", "riding a bicycle", ["camping", "a walk in the park", "watching a movie"])]
    ),
)

# ================================================================== Core vocabulary
_CV_WX = [("구름", "cloud", "오늘은 구름이 많이 끼고 흐립니다."), ("끼다", "(fog, cloud, dust, etc.) to form", "몬트레이는 안개가 많이 낍니다."), ("날씨", "weather", "하와이는 날씨가 따뜻해요."),
          ("내리다", "(rain, snow, etc.) to fall; to come down", "오전에는 맑고 오후부터 비가 내리겠습니다."), ("눈", "snow", "알래스카는 겨울에 눈이 많이 와요."), ("덥다", "(weather) to be hot", "한국 여름 날씨는 덥고 비가 많이 와요."),
          ("따뜻하다", "to be warm", "봄에는 날씨가 따뜻해요."), ("맑다", "to be clear", "비가 그친 후에 날씨가 아주 맑아요."), ("바람", "wind", "제주도는 바람이 많이 불어요."), ("불다", "to blow", "요즘 바람이 많이 불고 날씨가 흐려요."),
          ("비", "rain", "몬트레이는 겨울에 비가 많이 와요."), ("쌀쌀하다", "to be chilly", "날씨가 쌀쌀해요. 코트를 입으세요."), ("안개", "fog", "몬트레이는 아침에 안개가 자주 낍니다."), ("춥다", "(weather) to be cold", "오늘은 눈이 오고 날씨가 추워요."),
          ("하늘", "the sky", "오늘은 하늘이 맑습니다."), ("흐리다", "to be cloudy; to be overcast; “to be unclear”", "구름이 많이 끼고 날씨가 흐려요.")]
_CV_SEA = [("가을", "fall; autumn", "한국의 가을은 날씨가 쌀쌀해요."), ("겨울", "winter", "콜로라도는 겨울에 눈이 많이 와요."), ("계절", "a season", "한국은 사계절이 있습니다."), ("봄", "spring", "한국은 봄 날씨가 따뜻해요."), ("여름", "summer", "몬트레이 여름은 안 더워요.")]
_CV_GEO = [("골프장", "a golf course; “golf place”", "제주도에는 골프장이 많습니다."), ("공원", "a park", "뉴욕에 센트럴 공원이 있습니다."), ("바닷가", "the beach; the coast; the seaside", "주말에 보통 바닷가에서 산책해요.")]
_CV_HOB = [("구경", "watching; sightseeing", "샌프란시스코 야구장에 야구 구경하러 가요."), ("구경하다", "to watch; to sightsee", "샌프란시스코 야구장에 야구 구경하러 가요."), ("농구", "basketball", "마이클 조던은 농구를 잘 합니다."),
           ("달리기", "running; jogging", "빅서 마라톤에서 달리기를 해요."), ("독서", "reading (books)", "제 동생 취미는 독서입니다."), ("만나다", "to meet; to see", "주말에 오래간만에 고향 친구를 만나요."), ("배구", "volleyball", "제 취미는 배구하고 볼링입니다."),
           ("산책", "a walk; a stroll", "나는 매일 공원에 가서 산책합니다."), ("산책하다", "to take a walk", "나는 매일 공원에 가서 산책합니다."), ("야구", "baseball; “field ball”", "제가 좋아하는 야구팀은 다저스입니다."),
           ("야영", "camping", "여름에 빅서에는 야영하는 사람들이 많아요."), ("야영하다", "to camp", "여름에 빅서에는 야영하는 사람들이 많아요."), ("여행", "travels", "저희 가족은 여행을 자주 갑니다."), ("여행하다", "to travel", "저희 가족은 여행을 자주 갑니다."),
           ("영화", "a movie", "제 취미는 주말에 영화 보는 것입니다."), ("음악", "music", "저는 한국 음악을 듣습니다."), ("자전거", "a bicycle", "중국에서는 많은 사람들이 자전거를 타요."), ("축구", "soccer; football; “kicking ball”", "브라질 사람들은 축구를 많이 합니다."),
           ("취미", "a hobby", "제 취미는 사진 찍고, 영화 보고, 그리고 음악 듣는 것이에요."), ("치다", "to hit; to strike; to play (tennis, ping-pong, golf, etc.)", "저는 가끔 주말에 테니스 쳐요."),
           ("타다", "to ride; to get on (the road or highway)", "겨울에는 콜로라도에 가서 스키 탑니다."), ("탁구", "table tennis; “high table ball”", "중국 사람들은 탁구를 좋아합니다.")]
_CV_LOAN = [("골프", "golf", "타이거 우즈가 골프를 잘 칩니다."), ("볼링", "bowling", "우리 가족은 이번 주말에 볼링 치러 갑니다."), ("스노보드", "snowboard", "제 친구 영준이는 스노보드를 잘 타요."), ("스케이트", "skate", "겨울에는 스케이트를 타요."),
            ("스키", "ski", "이번 겨울에 스키장에 갑시다."), ("테니스", "tennis", "저는 주말에 테니스 칩니다.")]
_CV_OTH = [("같이", "(along) with; together", "저는 친구하고 같이 숙제를 합니다."), ("계획", "a plan", "이번 주말에 집에서 쉽니다. 계획이 없어요."), ("계획하다", "to plan", "이번 주말에 집에서 쉽니다. 계획이 없어요."), ("높다", "to be high", "저 높은 빌딩이 우리 회사입니다."),
           ("고 싶다", "want to; wish to; like to", "저는 이번 주말에 쇼핑하고 싶어요."), ("고 싶어하다", "want to; wish to; like to (3rd person)", "제 여자친구는 한국에 가고 싶어해요."), ("많이", "a lot; much", "오늘은 바람이 많이 불어요."),
           ("못", "unable to; cannot (못 + verb)", "저는 시간이 없어요. 그래서 운동을 자주 못 합니다."), ("배우다", "to learn", "우리는 디엘아이에서 한국어를 배웁니다."), ("쉽다", "to be easy", "스페인어가 쉬워요."),
           ("아주", "very (much); so; extremely", "한국말은 아주 어려워요."), ("어떤", "which; what kind", "어떤 운동을 좋아하세요?"), ("어렵다", "to be difficult", "한국사람은 영어가 어렵습니다."),
           ("으러 가다", "to go (in order) to …", "저는 매일 수업 후에 몬트레이 체육관에 수영하러 갑니다."), ("으러 오다", "to come (in order) to …", "오늘 저녁 먹으러 우리 집에 와."), ("읍시다", "Let’s … (after a consonant)", "오늘 저녁에 한국식당에서 먹읍시다."),
           ("ㅂ시다", "Let’s … (after a vowel)", "오늘 저녁에 한국식당에 갑시다."), ("이번", "this (time)", "이번에는 누가 하겠습니까?"), ("재미있다", "to be fun; to be enjoyable; “fun exists”", "영화가 아주 재미있어요."), ("전화", "a telephone; a phone call", "주말에 친구한테 전화합니다."),
           ("전화하다", "to make a phone call", "주말에 친구한테 전화합니다."), ("좋아하다", "to like", "저는 한국 영화를 좋아합니다."), ("하지만", "but; however", "한국말을 열심히 배웁니다. 하지만 조금 어려워요.")]
_CV_SINO = [("구", "(球) a ball; sphere", "농구, 축구, 야구, 지구")]
_CV_ALL = _CV_WX + _CV_SEA + _CV_GEO + _CV_HOB + _CV_LOAN + _CV_OTH
L9 = lesson(
    "Ch 6 · Core vocabulary and self-evaluation",
    "주요 단어 · 자기 평가 · 구 (球)",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). Where the book writes a noun with (~하다) the verb is shown on its own row, and the endings -고 싶다/-고 싶어하다, -(으)러 가다/오다 and -(으)ㅂ시다 are written without the leading hyphen and parentheses: 고 싶다, 고 싶어하다, 으러 가다, 으러 오다, 읍시다, ㅂ시다. "
             "In the examples, DLI is written 디엘아이, and four example sentences are my adaptations of the book’s (the book’s 영화가 아주 재미있어요 for 재미있다 is the book’s “007 시리즈가 아주 재미있어요”, with the digits left out; the book’s L.A. Dodgers and “빅서” sentences keep only the Korean words)."),
        card("Weather", "", tables=[vt(_CV_WX)]),
        card("Seasons", "", tables=[vt(_CV_SEA)]),
        card("Geography and places", "", tables=[vt(_CV_GEO)]),
        card("Hobbies and weekend activities", "", tables=[vt(_CV_HOB)]),
        card("Loan words", "", tables=[vt(_CV_LOAN)]),
        card("Other words", "Italicized English words in the book are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTH)]),
        card("Sino-Korean vocabulary", "", tables=[vt(_CV_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so they can offer other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about the four seasons and the weather; talk about hobbies and weekend activities in a simple phrase or sentence.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -고 싶다 / 싶어하다 (want to; wish to); -(으)러 가다 / 오다 (go/come to do something); ㅂ irregular verbs; and the Sino-Korean syllable 구 (球)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _CV_ALL
                         if k not in ("고 싶다", "고 싶어하다", "으러 가다", "으러 오다", "읍시다", "ㅂ시다", "눈", "비", "덥다", "춥다", "끼다", "내리다", "많이", "아주", "높다", "치다", "타다", "하지만", "스키", "스케이트", "스노보드", "볼링", "골프", "테니스",
                                      "구경", "산책", "야영", "전화", "계획", "이번", "같이", "음악", "여행하다", "못", "어떤", "구경하다", "산책하다", "야영하다", "전화하다", "계획하다", "여행", "바닷가", "골프장")])
        + [M("What does the Sino-Korean syllable 구 (球) mean?", "a ball; sphere", ["a field", "a basket", "a kick"], "구 (球): 농구, 축구, 야구, 지구."),
           mean("눈", "snow", ["rain", "wind", "fog"]), mean("비", "rain", ["snow", "wind", "fog"]), mean("덥다", "(weather) to be hot", ["(weather) to be cold", "to be warm", "to be chilly"]), mean("춥다", "(weather) to be cold", ["(weather) to be hot", "to be warm", "to be clear"]),
           mean("많이", "a lot; much", ["a little", "very", "often"]), mean("아주", "very (much); extremely", ["a little", "often", "always"]), mean("높다", "to be high", ["to be low", "to be clear", "to be cloudy"]),
           mean("치다", "to hit; to play (tennis, golf)", ["to ride", "to do", "to learn"]), mean("타다", "to ride; to get on", ["to hit", "to do", "to learn"]), mean("하지만", "but; however", ["so; therefore", "and", "also"]),
           mean("스키", "ski", ["skate", "snowboard", "bowling"]), mean("테니스", "tennis", ["golf", "bowling", "ski"]), mean("같이", "(along) with; together", ["alone", "early", "often"]), mean("계획", "a plan", ["a hobby", "a phone call", "a weekend"]),
           mean("이번", "this (time)", ["last", "next", "every"]), mean("산책", "a walk; a stroll", ["running", "camping", "sightseeing"]), mean("야영", "camping", ["a walk", "running", "sightseeing"]), mean("전화", "a telephone; a phone call", ["a plan", "music", "a movie"]),
           mean("여행", "travels", ["a hobby", "a plan", "a walk"]), mean("바닷가", "the beach; the coast; the seaside", ["a park", "a golf course", "a mountain"]), mean("골프장", "a golf course", ["a park", "the beach", "a gym"]),
           mean("못", "unable to; cannot", ["not", "want to", "also"]), mean("어떤", "which; what kind", ["when", "where", "how"])]
    ),
)

UNIT = unit("Semester 1 · Unit 2 · Chapter 6: Weather and Hobbies (날씨와 취미)", [L1, L2, L3, L4, L5, L6, L7, L8, L9])

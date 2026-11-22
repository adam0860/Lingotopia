"""Unit 35: KBC Semester 1, Unit 7, Chapter 28 - Polite Koreans (예의 바른 한국인).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 7, Student's Edition (2022).
Audio, video clips, pictures, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 28 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_GEN = [
    ("기성세대 / 구세대", "(旣成世代/舊世代) older generation; old generation", "기성세대들은 신세대들이 버릇이 없다고 생각합니다."),
    ("신세대", "(新世代) younger generation; “new generation”", "신세대들은 자기들만의 인터넷 언어를 사용합니다."),
]
_CV_ETI = [
    ("공경", "(恭敬) reverence; respect; honor (~하다: to revere; to respect)", "어른을 공경하는 마음을 가져야 해요."),
    ("공손", "(恭遜) politeness; courteousness (~하다: to be polite; to be courteous)", "웃어른들에게 친절하고 공손하세요."),
    ("굽히다", "to bend", "어른들께는 허리를 굽혀 인사하세요."),
    ("꼬다", "to twist; to cross", "다리를 꼬지 말고 앉으세요."),
    ("들다", "to raise; to lift; to hold", "젓가락과 숟가락을 같이 들고 먹지 마세요."),
    ("바르다", "to be straight; to be right", "앞으로 바른 생각, 바른 생활을 하겠습니다."),
    ("손짓", "a hand gesture (~하다: to make a hand gesture)", "김 선생님이 사무실로 오라고 손짓했어요."),
    ("숙이다", "to bow; to bend one’s head (or upper body) forward", "선생님께 머리를 숙여 부탁드렸습니다."),
    ("악수", "(握手) shaking hands (~하다: to shake hands)", "새로 들어온 동료와 악수하며 인사를 했습니다."),
    ("예의", "(禮儀) manners; courtesy; politeness", "한국 사람들은 예의가 바릅니다."),
    ("예절", "(禮節) etiquette", "살면서 지켜야 할 예절을 배웁니다."),
    ("존경", "(尊敬) respect (~하다: to respect)", "이 분이 제가 가장 존경하는 선생님입니다."),
    ("쳐다보다", "to look at; to stare", "자고 있는 아이를 쳐다봤어요."),
    ("포옹", "(抱擁) a hug (~하다: to hug; to embrace)", "어머니께서 제대하고 돌아온 동생을 포옹해 주셨습니다."),
    ("흔들다", "to shake; to wave", "멀리서 친구를 보고 손을 흔들었어요."),
]
_CV_LAN = [
    ("반말", "(半) blunt language; impolite language; “half language”", "보통 친한 친구끼리는 반말을 사용합니다."),
    ("발음", "(發音) pronunciation (~하다/되다: to pronounce / to be pronounced)", "중국어는 발음하기 어렵습니다."),
    ("사투리 / 방언", "(方言) a dialect; vernacular", "제주도 사투리는 이해하기가 아주 어렵습니다."),
    ("외우다", "to memorize", "단어를 매일 외워도 기억할 수가 없어요."),
    ("존댓말", "(尊待) honorific language; honorific; “honoring language”", "어른들께는 존댓말을 사용합니다."),
    ("표준말", "(標準) a standard language", "티브이 아나운서들과 라디오 아나운서들은 표준말을 사용합니다."),
    ("표현", "(表現) an expression (~하다/되다: to express / to be expressed)", "교실에서 자주 쓰는 표현은 무엇입니까?"),
]
_CV_OTH = [
    ("~간", "(間) between", "가족간에는 대화가 중요합니다."),
    ("강하다", "(强) to be strong", "제 여자 친구는 성격이 강한 편입니다."),
    ("개성", "(個性) individuality", "진수 씨는 사람이 좋지만 개성이 없어요."),
    ("고개", "the head (from the neck up)", "고개를 들어서 저를 보세요."),
    ("-나(요)", "an interrogative ending (see the grammar)", "김 선생님, 우리 점심은 무엇을 먹나요?"),
    ("나이가 들다", "(年歲) to get old; “age gets in” (연세 is the honorific form of 나이)", "나이가 들면 눈이 잘 안 보입니다."),
    ("노력", "(努力) an effort; an endeavor; hard work (~하다: to make an effort)", "앞으로 더 열심히 노력하겠습니다."),
    ("대체로", "(大體) generally; mostly; overall; by and large", "대체로 저희 가족은 주말에 일찍 일어납니다."),
    ("대화", "(對話) a conversation (~하다: to talk with)", "대화가 잘 통하는 친구가 좋아요."),
    ("뜻", "meaning (~하다: to mean)", "표준말의 영어 뜻은 무엇입니까?"),
    ("마음", "heart; mind", "마음이 따뜻한 사람을 만나고 싶어요."),
    ("반", "(班) a class; a section (of a class)", "우리 반에 미국에서 온 학생이 있습니다."),
    ("방식", "(方式) a way; a style", "신세대와 구세대는 생각하는 방식이 달라요."),
    ("버릇", "a habit; manners", "성진 씨는 어려서 버릇이 좀 없어요."),
    ("부르다", "to call; to name", "선생님이 이름을 부르면 손을 드세요."),
    ("부지런하다 / 부지런히", "to be diligent / diligently", "제 친구 길수는 부지런합니다. 한국사람들은 영어를 부지런히 공부합니다."),
    ("솔직", "(率直) frankness; candidness (~하다: to be frank; to be candid; to be straightforward)", "신 선생님은 솔직히 자기 생각을 말하는 편이에요."),
    ("실수", "(失手) a mistake (~하다: to make a mistake)", "실수로 전화 번호를 잘 못 눌렀어요."),
    ("여전히", "still (i.e. continuance of an action/condition)", "김 일병은 여전히 김치를 못 먹습니다."),
    ("우연히", "(偶然) by chance; incidentally", "어제 박 선생님을 영화관에서 우연히 만났습니다."),
    ("웃다", "to smile; to laugh", "김 상병은 코미디 프로그램을 보면서 잘 웃습니다."),
    ("의견", "(意見) an opinion", "정 선생님은 모든 사람들에게 자기 의견을 솔직히 말합니다."),
    ("이해", "(理解) understanding; comprehension (~하다/되다: to understand / to be understood)", "기성세대들은 신세대들을 잘 이해하지 못합니다."),
    ("자연스럽다", "(自然) to be natural", "한국에 오래 살면 한국말을 자연스럽게 합니다."),
    ("-지(요)", "a verb ending expressing intention or suggestion in a friendly manner (see the grammar)", "운전은 제가 하지요."),
    ("지키다", "to keep; to observe; to protect", "우리의 아름다운 전통을 계속 지키고 싶어요."),
    ("주의", "(注意) a care; a caution (~하다: to be careful; to be cautious)", "계단에서 넘어질 수 있으니까 주의하세요."),
    ("통하다", "(通) to communicate with; to be understood; “to flow freely”", "한국에서는 스페인어가 통하지 않습니다."),
    ("틀리다", "to be wrong; to be incorrect", "외국인들은 존댓말을 틀리게 사용할 때가 많습니다."),
]
_CV_LOAN = [("에티켓", "etiquette", "외국에서 지켜야 할 에티켓을 배워요."), ("제스처", "a gesture", "송 이병은 말할 때 제스처를 많이 써요.")]
_CV_SINO = [("례 / 예", "(禮) manners; etiquette; courtesy", "예의, 무례, 실례"), ("음", "(音) sound", "음악, 음성, 발음")]
_ALL = {r[0]: r for r in _CV_GEN + _CV_ETI + _CV_LAN + _CV_OTH + _CV_LOAN + _CV_SINO}
_EXTRA = {"기성세대 / 구세대": "older generation; old generation", "사투리 / 방언": "a dialect; vernacular", "부지런하다 / 부지런히": "to be diligent; diligently", "나이가 들다": "to get old", "-나(요)": "(an interrogative ending)", "-지(요)": "(an ending for intention or suggestion)", "~간": "between", "례 / 예": "manners; etiquette; courtesy",
          "공경": "reverence; respect", "공손": "politeness; courteousness", "손짓": "a hand gesture", "악수": "shaking hands", "존경": "respect", "포옹": "a hug", "발음": "pronunciation", "표현": "an expression", "노력": "an effort", "대화": "a conversation", "뜻": "meaning", "실수": "a mistake", "이해": "understanding", "주의": "a care; a caution", "솔직": "frankness; candidness", "반": "a class; a section",
          "무례": "impoliteness; rudeness; “no manners”", "실례": "rudeness; impoliteness; “loss of manners”", "예의": "courtesy; decorum; civility; etiquette", "예절": "decorum; courtesy; etiquette",
          "고음": "a high-pitched sound; “high sound”", "저음": "a low-pitched sound", "음악": "music; “merry sound”", "음량": "sound volume", "음성": "a voice; a sound", "음속": "the speed of sound; sonic speed; “sound speed”", "음질": "the quality of sound", "음파": "a sound wave",
          "자리를 양보하다": "to give up one’s seat", "신세대들": "the younger generation", "서울말": "the Seoul dialect (the standard)", "평양말": "the Pyongyang dialect (North Korea’s standard)", "제주도 사투리": "the Jeju dialect"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)

# ================================================================== L1: objectives, 례/예 and 음, dialects
_YE = [("무례", "impoliteness; rudeness; “no manners”"), ("실례", "rudeness; impoliteness; “loss of manners”"), ("예의", "courtesy; decorum; civility; etiquette"), ("예절", "decorum; courtesy; etiquette")]
_EUM = [("고음", "a high-pitched sound; “high sound”"), ("저음", "a low-pitched sound"), ("음악", "music; “merry sound”"), ("음량", "sound volume"), ("음성", "a voice; a sound"), ("음속", "the speed of sound; sonic speed; “sound speed”"), ("음질", "the quality of sound"), ("음파", "a sound wave")]
_DIA = [("서울말", "the Seoul dialect, considered the standard dialect (표준말) in South Korea"), ("평양말", "the Pyongyang dialect, the standard dialect in North Korea"), ("강원도 사투리", "the Gangwon-do dialect"), ("충청도 사투리", "the Chungcheong-do dialect"), ("전라도 사투리", "the Jeolla-do dialect"), ("경상도 사투리", "the Gyeongsang-do dialect (a relatively strong accent)"), ("제주도 사투리", "the Jeju-do dialect (a relatively strong accent)")]
L1 = lesson(
    "Ch 28 · What the chapter teaches, 례/예 (禮) and 음 (音), and Korean dialects",
    "예의 바른 한국인 · 무례 · 실례 · 예의 · 예절 · 음악 · 음성 · 표준말 · 사투리",
    requires=[],
    cards=[
        card("What Chapter 28 teaches (예의 바른 한국인)",
             "Chapter 28, “Polite Koreans”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify different generations and talk about them; identify and use two different language registers, 존댓말 and 반말; and identify and talk about Korean manners and etiquette.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; a summary of speech styles; the verb ending –지(요); the interrogative ending –나(요); and the Sino-Korean syllables 례/예 (禮) and 음 (音)."),
        card("Sino-Korean in use: 례/예 (禮)",
             "This Sino-Korean syllable means manners, etiquette, or courtesy, as in 무례 (impoliteness; rudeness; “no manners”), 실례 (rudeness; impoliteness; “loss of manners”), 예의 (courtesy; decorum; civility; etiquette), and 예절 (decorum; courtesy; etiquette). Note that 례 becomes 예 when it is placed at the beginning of a word.",
             tables=[ktable(_YE)]),
        card("Sino-Korean in use: 음 (音)",
             "This Sino-Korean syllable means sound or sonic-, as in 고음 (high-pitched sound; “high sound”), 저음 (low-pitched sound), 음악 (music; “merry sound”), 음량 (sound volume), 음성 (a voice; a sound), 음속 (the speed of sound; sonic speed; “sound speed”), 음질 (the quality of sound), and 음파 (sound wave).",
             tables=[ktable(_EUM)]),
        card("Notes: Korean dialects",
             "Like most languages in the world, Korean has dialects (사투리 or 방언). Korean dialects are not extreme and do not block basic communication the way Mandarin and Cantonese do in China. Differences are found in intonation, verbal endings, and some vocabulary. 서울말 is considered a standard dialect (표준말) in South Korea and 평양말 is a standard dialect in North Korea. South Korean regional dialects include, as you may have guessed, 강원도 사투리, 충청도 사투리, 전라도 사투리, 경상도 사투리 and 제주도 사투리. The last two (경상도 and 제주도) carry a relatively strong accent when compared with 서울 표준말. (The book’s picture shows various words for “dragonfly” in the dialects; the standard Korean word is 잠자리.)",
             tables=[ktable(_DIA)]),
        card("Activities left out", "The vocabulary builder (a PowerPoint presentation with pictures and sounds, Activities 1 and 2 on the SMART Board, the Sino-Korean presentation and the game “Pirates of the Caribbean: Looking for Treasure Island”) is a picture, computer and game activity."),
    ],
    exercises=uniq(
        _tr(_YE + _EUM + _DIA[:2], k=3)
        + [M("What does 례/예 (禮) mean?", "manners; etiquette; courtesy", ["sound", "love", "ceremony"], "예의, 무례, 실례."), M("What does 음 (音) mean?", "sound", ["manners", "congratulation", "a wife"], "음악, 음성."), M("When does 례 become 예?", "At the beginning of a word", ["At the end of a word", "Before a vowel only", "Never"], "예의, but 무례."), M("What is the standard dialect in South Korea?", "서울말", ["제주도 사투리", "평양말", "경상도 사투리"], "서울 표준말."), M("What is the standard dialect in North Korea?", "평양말", ["서울말", "전라도 사투리", "제주도 사투리"], "평양말."),
           M("Which two dialects carry a relatively strong accent?", "경상도 and 제주도", ["서울 and 강원도", "충청도 and 전라도", "평양 and 서울"], "The book’s note."), M("How do Korean dialects differ from Mandarin and Cantonese?", "They are not extreme and do not block basic communication", ["They are completely unintelligible", "They have different scripts", "They have no accents"], "The book’s note."), M("Where are differences found?", "Intonation, verbal endings and some vocabulary", ["Only the alphabet", "Only the numbers", "Only the names"], "The book’s note."),
           F("한국에서는 ___가 바르다고 해요. (courtesy)", "예의", ["음악", "무례"], "예의 = courtesy."), F("남의 집에서 소리를 지르는 것은 ___입니다. (rudeness)", "무례", ["예절", "음질"], "무례 = rudeness."), F("저는 ___을 좋아해요. (music)", "음악", ["예의", "무례"], "음악 = music."),
           read_q("예의"), read_q("무례"), read_q("음악"), read_q("서울말"), read_q("제주도 사투리")]
    ),
)

# ================================================================== L2: Topic A
_A_DLG = [
    ("마이클", "지하철에서 한 고등학생이 나이 드신 분께 자리를 양보했어요.", "On the subway, a high school student gave up his seat to an elderly person."),
    ("김 선생님", "한국에서는 흔한 일이에요. 한국 사람들은 어릴 때부터 어른을 공경해야 한다고 배워요.", "In Korea, that is a common thing. Koreans learn from the time they are young that they should respect their elders."),
    ("마이클", "아, 그래서 한국 사람들이 예의가 바르군요. 근데, 요즘 신세대들도 예전처럼 예의를 잘 지켜요?", "Oh, so that’s why Koreans are polite. By the way, do the younger generation these days also keep good manners like before?"),
    ("김 선생님", "네. 그렇지만 신세대들은 개성이 강해요. 그리고 자기 의견을 솔직하게 말하는 편이에요. 그래서 어떤 기성세대들은 신세대들이 버릇이 없다고 생각해요.", "Yes. But the younger generation has strong individuality. And they tend to state their opinions frankly. So some of the older generation think the younger generation has no manners."),
    ("마이클", "김 선생님은 어떻게 생각하세요?", "What do you think, Mr. Kim?"), ("김 선생님", "글쎄요. 세대간에 생각하는 방식이 좀 다른 것 같아요. 가끔 신세대들이 버릇이 없어 보여요. 그렇지만 어른을 존경하는 마음은 여전히 있는 것 같아요.", "Well. It seems the way of thinking differs a little between generations. Sometimes the younger generation seems to have no manners. But it seems they still have a heart that respects elders."),
    ("마이클", "그렇군요. 그럼, 기성세대와 신세대가 서로를 이해하려고 노력해야겠네요.", "I see. Then the older and younger generations will have to try to understand each other."), ("김 선생님", "그렇죠. 대화가 제일 좋은 방법인 것 같아요.", "That’s right. It seems conversation is the best way."),
]
_A_WORDS = ["~간", "강하다", "개성", "공경", "기성세대 / 구세대", "노력", "나이가 들다", "대화", "마음", "바르다", "반", "방식", "버릇", "솔직", "신세대", "여전히", "예의", "의견", "이해", "존경", "지키다"]
_BLOG = [("글쓴이 김영선", "Writer: Kim Yeongseon"), ("제목 예의 바른 친구 수미", "Title: My polite friend Sumi"), ("수미는 고등학교 때 친구입니다.", "Sumi is a friend from high school."), ("수미는 삼 년 동안 저와 같은 반이었어요.", "Sumi was in the same class as me for three years."), ("수미는 아주 예의가 바르고 어른을 공경하는 친구예요.", "Sumi is a friend who is very polite and respects elders."),
         ("길에서 아는 어른을 만나면 항상 바르게 인사를 합니다.", "When she meets an adult she knows on the street, she always greets them properly."), ("또, 한 달에 한 번 친구들과 같이 혼자 사시는 노인들을 방문합니다.", "Also, once a month she visits elderly people who live alone, together with her friends."), ("그리고 버스나 전철에서도 나이가 드신 분들께 꼭 자리를 양보합니다.", "And even on buses and trains, she always gives up her seat to older people."),
         ("저도 수미처럼 예의 바르고 어른을 공경하는 사람이 되기 위해 노력해야겠어요.", "I, too, will have to make an effort to become a polite person who respects elders like Sumi.")]
L2 = lesson(
    "Ch 28 · Topic A: Korean people seem to be courteous (한국 사람들은 예의가 바른 것 같아요)",
    "한국 사람들은 예의가 바른 것 같아요 · 자리를 양보했어요 · 어른을 공경 · 신세대 · 기성세대",
    requires=[],
    cards=[
        card("Topic A: Korean people seem to be courteous (한국 사람들은 예의가 바른 것 같아요)",
             "Mr. Kim and Michael are talking about the manners of the younger generation after Michael observed a high school student giving his seat to an elderly man on a subway train. (The English is mine; the book gives none. The book writes 아… with an ellipsis; it is left out.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 공경(하다), 노력(하다), 대화(하다), 솔직(하다), 이해(하다/되다) and 존경(하다) can take 하다. 구세대 is the book’s other word for 기성세대.", tables=[ktable(_rows(_A_WORDS))]),
        card("Follow-up 1 (Reading): Youngsun’s blog about her friend Sumi",
             "The book asks you to read the blog entry and to identify Sumi’s characteristics and three specific examples of them, in English, in a table. The text is the book’s (3년 is spelled out); the English is mine.",
             examples=passage(_BLOG)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Characteristics", "Specific examples"], [["She is very polite (예의가 바르다)", "She always greets adults she meets on the street properly"], ["She respects elders (어른을 공경하다)", "Once a month she visits elderly people who live alone, together with friends"], ["She is considerate on public transport", "She always gives up her seat to older people on buses and trains"]])]),
        card("Activities left out", "The SMART Board activities of the Presentation Activity, Follow-up 2 (listening to three statements about generational attitudes), Activity 1 (a SMART Board activity), Activity 2 (listening to three dialogs and noting the topic and the female speakers’ opinions) and Activity 3 (나는 어느 세대?: reading two articles about differing values and lifestyles in groups, texts not in the book’s text) are computer, audio and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not any(c in w for c in "~/")]))
        + _tr(_strip(_A_DLG) + _BLOG, k=3)
        + [M("What did the high school student do?", "Gave up his seat to an elderly person", ["Bowed to a teacher", "Carried a bag", "Sang a song"], "자리를 양보했어요."), M("What do Koreans learn from childhood?", "To respect their elders", ["To work hard", "To speak English", "To save money"], "어른을 공경해야 한다고 배워요."), M("What are the younger generation like?", "Strong in individuality and frank with their opinions", ["Shy and quiet", "Very formal", "Lazy"], "개성이 강해요. 자기 의견을 솔직하게."), M("Why do some of the older generation think the younger has no manners?", "Because the younger state their opinions frankly", ["Because they are late", "Because they dress badly", "Because they don’t study"], "버릇이 없다고 생각해요."),
           M("What does Mr. Kim think differs between generations?", "The way of thinking", ["The language", "The country", "The food"], "생각하는 방식이 좀 다른."), M("What does Mr. Kim think the younger generation still has?", "A heart that respects elders", ["No manners", "No opinions", "No respect"], "어른을 존경하는 마음은 여전히."), M("What is the best way, according to Mr. Kim?", "Conversation", ["Silence", "Rules", "Money"], "대화가 제일 좋은 방법."), M("How long was Sumi in the same class as Youngsun?", "Three years", ["One year", "Five years", "Ten years"], "삼 년 동안."),
           M("What does Sumi do once a month?", "Visits elderly people who live alone", ["Goes hiking", "Studies with friends", "Writes letters"], "혼자 사시는 노인들을 방문."), M("What will Youngsun make an effort to do?", "Become polite and respectful of elders like Sumi", ["Move away", "Learn to cook", "Go abroad"], "수미처럼."),
           F("한국 사람들은 어른을 ___해야 한다고 배워요. (respect)", "공경", ["이해", "지키"], "공경하다 = to respect."), F("신세대들은 ___이 강해요. (individuality)", "개성", ["버릇", "의견"], "개성이 강하다."), F("대화가 제일 좋은 ___인 것 같아요. (way)", "방법", ["방식은", "마음"], "방법 = a method."), F("신세대들은 자기 의견을 ___하게 말하는 편이에요. (frankly)", "솔직", ["공손", "부지런"], "솔직하게."),
           read_q("자리를 양보했어요"), read_q("어른을 공경해야 한다고 배워요"), read_q("신세대들은 개성이 강해요"), read_q("대화가 제일 좋은 방법인 것 같아요"), read_q("예의 바른 친구")]
    ),
)

# ================================================================== L3: Topic B
_B_DLG = [
    ("피터", "정미 씨, 한국말이 지방마다 조금씩 달라요?", "Jungmee, does Korean differ a little by region?"),
    ("정미", "그럼요. 서울말이 표준말이고 지방마다 사투리가 있어요. 근데, 왜요?", "Of course. The Seoul dialect is the standard language and every region has a dialect. But why?"),
    ("피터", "네, 어제 텔레비전에서 우연히 제주도 말을 들었는데 정말 어려웠어요.", "Well, yesterday I happened to hear the Jeju dialect on television and it was really difficult."),
    ("정미", "맞아요. 특히 제주도 말은 이해하기가 힘들어요. 또 발음하기도 어려워요.", "That’s right. In particular, the Jeju dialect is hard to understand. It is also hard to pronounce."),
    ("피터", "아, 그렇군요.", "Oh, I see."),
    ("정미", "그런데, 피터 씨는 존댓말을 아주 잘하시네요?", "By the way, you speak honorific language very well, Peter."),
    ("피터", "아, 그래요? 그래도, 자주 틀려요. 지난번에는 선생님, 잘 잤어요? 라고 말해서 반 친구들이 많이 웃었어요.", "Oh, really? Still, I often get it wrong. Last time I said, “Teacher, did you sleep well?” (in the wrong form) and my classmates laughed a lot."),
    ("정미", "아, 네. 근데, 피터 씨는 반말보다 존댓말이 더 쉬워요?", "Oh, I see. By the way, is honorific language easier for you than blunt language?"),
    ("피터", "네. 저는 존댓말이 더 쉬워요. 그렇지만, 댁이나 연세처럼 단어가 아주 다른 존댓말은 아직 잘 몰라요. 외워야 할 단어가 많은 것 같아요.", "Yes. Honorific language is easier for me. But I still don’t know well the honorific words that are very different, like 댁 and 연세. It seems there are many words to memorize."),
    ("정미", "피터 씨, 걱정하지 마세요. 부지런히 공부하면 그런 표현들도 다 자연스럽게 쓸 수 있어요.", "Don’t worry, Peter. If you study diligently, you will be able to use those expressions all naturally, too."),
]
_B_WORDS = ["뜻", "반말", "발음", "부지런하다 / 부지런히", "사투리 / 방언", "외우다", "우연히", "웃다", "자연스럽다", "존댓말", "통하다", "틀리다", "표준말", "표현"]
_ESS = [
    ("저는 필리핀에서 온 니에베스 쿠발란입니다.", "I am Nieves Cuballan, who came from the Philippines."), ("저는 십 년 전에 한국에 공부하러 왔습니다.", "I came to Korea to study ten years ago."), ("그때 지금의 남편을 만났습니다.", "At that time I met my present husband."), ("그리고 팔 년 전에 결혼했습니다.", "And I got married eight years ago."), ("지금은 제주시에서 시부모님을 모시고 살고 있습니다.", "Now I live in Jeju City with my parents-in-law."),
    ("처음에는 한국말을 잘 몰라서 실수한 적도 많았습니다.", "At first, I did not know Korean well, so there were many times I made mistakes."), ("결혼해서 시댁에 살게 된 첫날이었습니다.", "It was the first day after I got married and came to live at my husband’s family’s home."), ("아침에 일어나서 시부모님께 잘 잤어라고 인사를 했습니다.", "In the morning I got up and greeted my parents-in-law with “Did you sleep well?” (in blunt language)."),
    ("그랬더니 시부모님께서 많이 웃으셨습니다.", "Then my parents-in-law laughed a lot."), ("남편이 어른께는 반말을 써서는 안 된다고 가르쳐 주었습니다.", "My husband taught me that I must not use blunt language to elders."), ("또, 이웃에 사는 초등학생 아이에게 저녁 잡수셨어요라고 존댓말을 써서 웃은 적도 있습니다.", "Also, there was a time people laughed because I used honorific language, saying “Did you have dinner?”, to an elementary school child living nearby."),
    ("지금은 한국말이 많이 늘어서 이런 실수는 안 합니다.", "Now my Korean has improved a lot, so I don’t make this kind of mistake."), ("하지만, 아직도 제주도 사투리는 어렵습니다.", "But the Jeju dialect is still difficult."), ("시부모님께서 제주도 말을 하시면 이해하기 어렵습니다.", "When my parents-in-law speak the Jeju dialect, it is hard to understand."),
    ("한국말이 어려워도 한국말이 참 아름답다는 생각을 저는 자주 합니다.", "Even though Korean is difficult, I often think that Korean is truly beautiful."), ("앞으로도 한국말을 열심히 배워서 더 잘할 수 있도록 노력할 겁니다.", "In the future, too, I will learn Korean hard and make an effort so that I can do it better."),
]
L3 = lesson(
    "Ch 28 · Topic B: You should use an honorific expression (존댓말을 써야 해요)",
    "존댓말을 써야 해요 · 표준말 · 사투리 · 반말 · 실수 · 자연스럽게 쓸 수 있어요",
    requires=[],
    cards=[
        card("Topic B: You should use an honorific expression (존댓말을 써야 해요)",
             "Peter, who is learning Korean in Korea, is talking to Jungmee about his language-learning experience. (The English is mine; the book gives none. The book’s footnote: 자연스럽게 (naturally) is from 자연스럽다 (to be natural). The quotation marks and the stage direction “(웃으면서)”, laughing, are left out of the spoken lines.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). 반말 and 존댓말 are the two registers of the chapter.", tables=[ktable(_rows(_B_WORDS))]),
        card("Follow-up 1 (Reading): an award-winning essay about the challenges of learning Korean",
             "The story won an award in an essay contest; the book asks you to read it and fill in a table in English (the writer’s background, examples of previous language difficulties, what is still difficult). The text is the book’s (10년 and 8년 are spelled out; the quotation marks are left out); the English is mine. The book glosses 실수: an error, a mistake.",
             examples=passage(_ESS)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["Writer’s background", "She is from the Philippines; she came to Korea ten years ago to study, met her husband and married eight years ago; she now lives in Jeju City with her parents-in-law"], ["Examples of previous language difficulties", "On her first morning at her husband’s family home she greeted her parents-in-law in blunt language (잘 잤어?) and they laughed; she used honorific language to an elementary school child (저녁 잡수셨어요?) and people laughed"], ["What is still difficult for the writer", "The Jeju dialect: it is hard to understand when her parents-in-law speak it"]])]),
        card("Activities left out", "The SMART Board activity and Follow-up 2 (listening to two conversations in which a man tells a woman about a language error he made) are computer and audio activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if "/" not in w]))
        + _tr(_strip(_B_DLG) + _ESS, k=3)
        + [M("What did Peter hear on television?", "The Jeju dialect", ["The Seoul dialect", "A song", "The news"], "제주도 말."), M("What is hard about the Jeju dialect?", "It is hard to understand and to pronounce", ["It is too fast", "It has no honorifics", "It is written differently"], "이해하기가 힘들어요. 발음하기도 어려워요."), M("What is the standard language?", "The Seoul dialect", ["The Jeju dialect", "The Busan dialect", "The Pyongyang dialect only"], "서울말이 표준말."), M("What mistake did Peter make last time?", "He used the wrong form to a teacher, and his classmates laughed", ["He forgot a word", "He was late", "He fell"], "선생님, 잘 잤어요?"),
           M("Which is easier for Peter?", "Honorific language", ["Blunt language", "Both are equally easy", "Neither"], "존댓말이 더 쉬워요."), M("What is difficult for Peter in honorific language?", "Words that are very different, like 댁 and 연세", ["The endings", "The pronunciation", "The grammar"], "단어가 아주 다른 존댓말."), M("What does Jungmee advise?", "Study diligently", ["Speak only blunt language", "Move to Seoul", "Avoid honorifics"], "부지런히 공부하면."),
           M("When did the writer come to Korea?", "Ten years ago", ["Eight years ago", "Two years ago", "Last year"], "십 년 전."), M("What mistake did she make on the first morning at her husband’s family home?", "She greeted her parents-in-law in blunt language", ["She slept late", "She cooked badly", "She forgot to bow"], "잘 잤어라고 인사."), M("What did her husband teach her?", "Not to use blunt language to elders", ["To cook Korean food", "To dance", "To drive"], "어른께는 반말을 써서는 안 된다."), M("What is still difficult for her?", "The Jeju dialect", ["The alphabet", "Honorific language", "Pronouncing 한글"], "아직도 제주도 사투리는 어렵습니다."),
           F("서울말이 ___이고 지방마다 사투리가 있어요. (the standard language)", "표준말", ["존댓말", "반말"], "표준말 = the standard language."), F("피터 씨는 ___을 아주 잘하시네요? (honorific language)", "존댓말", ["반말", "사투리"], "존댓말."), F("외워야 할 ___가 많은 것 같아요. (words)", "단어", ["실수", "의견"], "단어 = a word."), F("부지런히 공부하면 자연스럽게 쓸 수 ___. (can)", "있어요", ["없어요", "싶어요"], "쓸 수 있어요."),
           read_q("지방마다 사투리가 있어요"), read_q("제주도 말은 이해하기가 힘들어요"), read_q("존댓말을 아주 잘하시네요"), read_q("부지런히 공부하면"), read_q("어른께는 반말을 써서는 안 됩니다")]
    ),
)

# ================================================================== L4: Grammar: summary of speech styles
_SS = [("Formal polite", "-습니다 / -ㅂ니다", "-습니까 / -ㅂ니까", "-(으)십시오", "-읍시다 / -ㅂ시다"), ("Informal polite", "-아/어요", "-아/어요", "-아/어요", "-아/어요"), ("Formal blunt", "-다", "-냐", "-아/어라", "-자"), ("Informal blunt", "-아/어", "-아/어", "-아/어", "-아/어")]
_ST_WEA = [("오늘의 날씨를 말씀 드리겠습니다.", "I will tell you today’s weather."), ("오늘은 날씨가 맑습니다.", "Today the weather is clear."), ("그러나 중부지방에는 오후에 잠깐 비가 오는 곳이 있겠습니다.", "However, in the central region there will be some places with a brief rain in the afternoon."), ("외출하시려면 우산을 준비해 주시기 바랍니다.", "If you are going out, please prepare an umbrella.")]
_ST_IP = [("선우 씨는 누나가 있어요?", "Sunwoo, do you have an older sister?"), ("누나는 없어요. 저는 형만 있어요.", "I have no older sister. I only have an older brother."), ("그렇군요. 참 오늘 저녁에 학교에서 재즈 콘서트가 있는데 같이 갈래요?", "I see. Oh, there is a jazz concert at school this evening; would you like to go together?"), ("좋아요. 그럼 몇 시에 볼까요?", "Good. Then what time shall we meet?"), ("도서관 앞에서 다섯 시에 봐요.", "Let’s meet in front of the library at five.")]
_ST_FB = [("자, 내일은 유격훈련이 있다.", "Now, tomorrow there is ranger training."), ("오늘 모두 소총을 닦고 훈련을 준비한다.", "Today everyone cleans their rifles and prepares for the training.")]
_ST_IB = [("선우야, 넌 누나가 있어?", "Sunwoo, do you have an older sister?"), ("누나는 없어. 난 형만 있어.", "I have no older sister. I only have an older brother."), ("그렇구나. 참 오늘 저녁에 학교에서 재즈 콘서트가 있는데 같이 갈래?", "I see. Oh, there is a jazz concert at school this evening; do you want to go together?"), ("좋아. 그럼 몇 시에 볼까?", "Good. Then what time shall we meet?"), ("도서관 앞에서 다섯 시에 보자.", "Let’s meet in front of the library at five.")]
_STY = [("가다", "to go"), ("먹다", "to eat"), ("읽다", "to read"), ("하다", "to do"), ("오다", "to come"), ("마시다", "to drink")]


def _plain(v):
    """formal blunt present statement of a regular verb: -ㄴ다 / -는다"""
    st = stem(v)
    l, vv, t = _K.decompose(st[-1])
    return st + "는다" if t else st[:-1] + _K.compose(l, vv, "ㄴ") + "다"


def _bl(v):
    return informal(v)[:-1]


L4 = lesson(
    "Ch 28 · Grammar A: a summary of the four speech styles",
    "존댓말 · 반말 · -습니다 · -아/어요 · -다 · -아/어 · 격식체와 비격식체",
    requires=[],
    cards=[
        card("Summary of speech styles",
             "Recall the four speech styles you have learned in the past chapters: (1) Formal Polite Speech Style; (2) Informal Polite Speech Style; (3) Informal Blunt Speech Style; and (4) Formal Blunt Speech Style. These four styles can be summarized as follows: formal polite –습니다 (from Chapter 1); informal polite –아/어요 (from Chapter 2); formal blunt –다 (from Chapter 15); informal blunt –아/어 (from Chapter 5).",
             tables=[table(["", "Formal", "Informal"], [["Polite", "–습니다 (from Ch. 1)", "–아/어요 (from Ch. 2)"], ["Blunt", "–다 (from Ch. 15)", "–아/어 (from Ch. 5)"]])]),
        card("The verb endings by sentence type",
             "The verb endings of the speech styles can change according to the sentence type.",
             tables=[table(["Speech style", "Statement", "Question", "Request", "Suggestion"], [list(r) for r in _SS])]),
        card("1. Formal polite speech style: -습니다 / -ㅂ니다",
             "This speech style is perceived as formal and polite because it is often used in formal situations and for formal purposes such as radio or television news broadcasting, presentations, and sermons. It is also used when addressing a supervisor or making new acquaintances. The book’s example is a weather forecast (the English is mine):",
             examples=passage(_ST_WEA)),
        card("2. Informal polite speech style: -아/어요",
             "This speech style is perceived as informal and polite because it is often used in situations where the speaker is in casual yet polite relationship with the addressee. You can use –아/어요 for a statement, a question, a command or request, or even a suggestion, without changing its form. The book’s example (5시 is spelled out; the English is mine):",
             examples=passage(_ST_IP)),
        card("3. Formal blunt speech style: -다",
             "This speech style is perceived as formal and blunt because it is used in newspapers, journals, textbooks, etc. In spoken language, this speech style is used among friends or by those of higher status in age or rank. As you learned in Chapter 24, this style is also used as a command form in the military. The book’s example (the English is mine):",
             examples=passage(_ST_FB)),
        card("4. Informal blunt speech style (반말): -아/어",
             "This speech style is perceived as informal and blunt because it is typically used in settings where social distance between speakers need not be maintained (e.g., between friends or siblings). This style is also used by older people when they address younger people with whom they have a close relationship. The conversation presented in the informal polite speech style example can be rewritten in informal blunt speech style as follows (the English is mine):",
             examples=passage(_ST_IB)),
        card("Forms (mine)", "The formal polite, informal polite, formal blunt (plain) and informal blunt statement forms of a few verbs, made by the book’s rules.",
             tables=[table(["Verb", "Meaning", "Formal polite", "Informal polite", "Formal blunt (-다)", "Informal blunt (-아/어)"], [[v, m, formal(v), informal(v), _plain(v), _bl(v)] for v, m in _STY], say=[0, 2, 3, 4, 5])]),
        card("Activities left out", "Follow-up 2 (video clips, identifying the speech style) and Follow-up 4 (a PowerPoint presentation activity) are video and computer activities."),
    ],
    exercises=uniq(
        [M("Which is the formal polite statement ending?", "-습니다 / -ㅂ니다", ["-아/어요", "-다", "-아/어"], "Formal polite from Chapter 1."), M("Which is the informal polite ending?", "-아/어요", ["-습니다", "-다", "-아/어"], "From Chapter 2."), M("Which is the formal blunt statement ending?", "-다", ["-습니다", "-아/어요", "-아/어"], "From Chapter 15."), M("Which is the informal blunt ending (반말)?", "-아/어", ["-습니다", "-다", "-아/어요"], "From Chapter 5."),
         M("Which ending is the formal polite question?", "-습니까 / -ㅂ니까", ["-냐", "-아/어요", "-자"], "Formal polite question."), M("Which ending is the formal blunt question?", "-냐", ["-습니까", "-아/어", "-(으)십시오"], "-냐 = formal blunt question."), M("Which ending is the formal polite suggestion?", "-읍시다 / -ㅂ시다", ["-자", "-아/어요", "-아/어"], "Let’s: formal polite."), M("Which ending is the formal blunt suggestion?", "-자", ["-읍시다", "-아/어요", "-(으)십시오"], "-자 = let’s: blunt."), M("Which ending is the formal polite request?", "-(으)십시오", ["-아/어라", "-아/어요", "-자"], "Formal polite request."), M("Which ending is the formal blunt command?", "-아/어라", ["-(으)십시오", "-아/어요", "-자"], "Formal blunt command."),
         M("Which style is used on news broadcasts and in presentations?", "Formal polite", ["Informal polite", "Formal blunt", "Informal blunt"], "The book’s note."), M("Which style is used in newspapers, journals and textbooks?", "Formal blunt", ["Formal polite", "Informal polite", "Informal blunt"], "-다."), M("Which style is used between friends or siblings?", "Informal blunt (반말)", ["Formal polite", "Formal blunt", "Informal polite"], "반말."), M("Which style can be used for every sentence type with no change?", "Informal polite -아/어요", ["Formal polite", "Formal blunt", "Informal blunt only"], "Statement, question, request, suggestion: -아/어요."), M("Which style is used as a command form in the military?", "Formal blunt", ["Informal blunt", "Informal polite", "Formal polite"], "As you learned in Chapter 24."),
         M("What does 오늘은 날씨가 맑습니다 show?", "Formal polite", ["Informal polite", "Formal blunt", "Informal blunt"], "-습니다."), M("What does 누나는 없어요 show?", "Informal polite", ["Formal polite", "Formal blunt", "Informal blunt"], "-어요."), M("What does 내일은 유격훈련이 있다 show?", "Formal blunt", ["Informal blunt", "Formal polite", "Informal polite"], "-다."), M("What does 누나는 없어 show?", "Informal blunt", ["Formal blunt", "Formal polite", "Informal polite"], "-어."),
         F("도서관 앞에서 다섯 시에 ___. (informal polite “Let’s meet”)", "봐요", ["보자", "봅시다"], "봐요 = informal polite."), F("도서관 앞에서 다섯 시에 ___. (informal blunt “Let’s meet”)", "보자", ["봐요", "봅시다"], "보자 = blunt."), F("누나는 ___. 난 형만 있어. (informal blunt “There is none”)", "없어", ["없어요", "없습니다"], "없어 = blunt."), F("오늘은 날씨가 ___. (formal polite “is clear”)", "맑습니다", ["맑아", "맑다"], "맑습니다."),
         read_q("맑습니다"), read_q("누나는 없어요"), read_q("누나는 없어"), read_q("도서관 앞에서 다섯 시에 봐요"), read_q("도서관 앞에서 다섯 시에 보자")]
        + _tr(_ST_WEA + _ST_IP + _ST_FB + _ST_IB, k=3)
    ),
)

# ================================================================== L5: speech-style practice (scripts, grandfather essay)
_SC1 = [("오늘의 공연소식입니다.", "This is today’s performance news."), ("오늘 대학로에서는 봄 음악 축제가 있습니다.", "Today there is a spring music festival at Daehangno."), ("세계적으로 유명한 바이올리니스트 카라 김이 베토벤 바이올린 협주곡 이 번을 연주합니다.", "The world-famous violinist Kara Kim will play Beethoven’s Violin Concerto No. 2."), ("또한 러시아 국립 발레단이 발레 호두까기 인형을 공연합니다.", "Also, the Russian national ballet company will perform the ballet The Nutcracker.")]
_SC2 = [("내일 일정을 말해 주겠다.", "I will tell you tomorrow’s schedule."), ("아침 여섯 시에 집합한다.", "We assemble at six in the morning."), ("집합 후에, 아침 식사를 하고 일곱 시부터 훈련장까지 행군한다.", "After assembly, we have breakfast and march to the training area from seven."), ("오후에는 유격훈련과 화생방 훈련이 있다.", "In the afternoon there is ranger training and CBR training."), ("이번 훈련에는 특히 따뜻한 옷을 준비하기 바란다.", "For this training, in particular, prepare warm clothes.")]
_SC3 = [("A", "김 과장님, 오늘 저녁에 회식이 있다는데 어디에서 하는지 알아요?", "Manager Kim, I heard there is a company dinner this evening; do you know where it is?"), ("B", "아, 회사 앞 서울 갈비에서 여섯 시에 있어요.", "Oh, it is at Seoul Galbi in front of the company at six."), ("A", "그래요? 전 오늘 친구 결혼식이 있어서 못 갈 것 같아요.", "Is that so? I have a friend’s wedding today, so I don’t think I can go."), ("B", "아, 그럼 영업과 송 과장님께 연락하세요.", "Oh, then contact Manager Song of the sales section."), ("A", "네, 알았어요. 고마워요.", "Yes, I understand. Thank you.")]
_SC4 = [("A", "너 이번 주 토요일에 뭐해?", "What are you doing this Saturday?"), ("B", "응, 나 도서관에 가.", "Yeah, I’m going to the library."), ("A", "토요일인데 도서관에서 공부해?", "It’s Saturday and you’re studying at the library?"), ("B", "어, 다음 주에 시험이 있어.", "Yeah, I have an exam next week.")]
_GR = [("우리 할아버지는 아침 다섯 시쯤 일어납니다.", "일어나십니다", "My grandfather gets up at around five in the morning."), ("그리고 매일 아침마다 동네 뒷산을 등산합니다.", "등산하십니다", "And every morning he hikes the hill behind the neighborhood."), ("그 후에 일곱 시쯤 아침을 먹습니다.", "드십니다", "After that he eats breakfast at around seven."), ("그리고 꼭 신문을 읽습니다.", "읽으십니다", "And he always reads the newspaper."),
       ("오전에는 노인대학에서 강연을 듣습니다.", "들으십니다", "In the morning he listens to lectures at the senior citizens’ college."), ("오후에는 보통 동네를 청소하거나 집에서 책을 읽습니다.", "청소하시거나 읽으십니다", "In the afternoon he usually cleans the neighborhood or reads a book at home."), ("저녁에는 식구들과 같이 밥을 먹고 티브이를 봅니다.", "드시고 보십니다", "In the evening he eats with the family and watches television."), ("그리고 보통 열 시쯤 잡니다.", "주무십니다", "And he usually sleeps at around ten.")]
_GR_H = [("우리 할아버지는 아침 다섯 시쯤 일어나십니다.", "My grandfather gets up (hon.) at around five in the morning."), ("그리고 매일 아침마다 동네 뒷산을 등산하십니다.", "And every morning he hikes (hon.) the hill behind the neighborhood."), ("그 후에 일곱 시쯤 아침을 드십니다.", "After that he eats (hon.) breakfast at around seven."), ("그리고 꼭 신문을 읽으십니다.", "And he always reads (hon.) the newspaper."),
         ("오전에는 노인대학에서 강연을 들으십니다.", "In the morning he listens (hon.) to lectures at the senior citizens’ college."), ("오후에는 보통 동네를 청소하시거나 집에서 책을 읽으십니다.", "In the afternoon he usually cleans (hon.) the neighborhood or reads (hon.) a book at home."), ("저녁에는 식구들과 같이 밥을 드시고 티브이를 보십니다.", "In the evening he eats (hon.) with the family and watches (hon.) television."), ("그리고 보통 열 시쯤 주무십니다.", "And he usually sleeps (hon.) at around ten.")]
L5 = lesson(
    "Ch 28 · Speech styles in practice: scripts and the grandfather essay",
    "공연소식 · 내일 일정 · 회식 · 반말 · 할아버지 · 일어나십니다 · 드십니다 · 주무십니다",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): identify the speech style and the relationship",
             "The book asks you to read four scripts, circle the verb endings, tick the speech style (formal polite, informal polite, formal blunt, informal blunt) and write in English the relationship between the speaker and the listener. The scripts are the book’s (digits and “2번” are spelled out in Hangul; the book’s Script 2 repeats “이번 훈련은 특히” before “이번 훈련에는”, which is written once here); the English is mine.",
             examples=passage(_SC1)),
        card("Script 2", "", examples=passage(_SC2)),
        card("Script 3", "", examples=dlg(_SC3)),
        card("Script 4", "", examples=dlg(_SC4)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Script", "Speech style", "Relationship (mine)"], [["1. 오늘의 공연소식입니다 …", "Formal polite (-ㅂ/습니다)", "A broadcaster and the audience"], ["2. 내일 일정을 말해 주겠다 …", "Formal blunt (-다)", "A superior (a military leader) and subordinates"], ["3. 김 과장님, 오늘 저녁에 …", "Informal polite (-아/어요)", "Co-workers (colleagues at a company)"], ["4. 너 이번 주 토요일에 뭐해?", "Informal blunt (-아/어)", "Close friends"]])]),
        card("Follow-up 3 (Reading and writing): Youngmi’s essay about her grandfather",
             "The book asks you to read Youngmi’s essay about her grandfather and, using 존댓말, to rewrite the underlined words between the lines; the first correction is made for you (일어납니다 → 일어나십니다). The book’s underlines do not survive in the text, so I treat the verbs as the underlined words; the corrections are mine (the digits are spelled out; TV is written 티브이).",
             examples=passage([(a, c) for a, b, c in _GR])),
        card("The verbs rewritten in 존댓말 (mine)", "The honorific forms: –(으)시– after the verb stem; 먹다 → 드시다 and 자다 → 주무시다 are special honorific verbs.",
             tables=[table(["Original", "Rewritten (존댓말)"], [[b0, b] for (a, b, c), b0 in zip(_GR, ["일어납니다", "등산합니다", "먹습니다", "읽습니다", "듣습니다", "청소하거나 읽습니다", "먹고 봅니다", "잡니다"])], say=[0, 1])]),
        card("The whole essay in 존댓말 (mine)", "", examples=passage(_GR_H)),
        card("Activities left out", "Follow-up 2 (video clips), Follow-up 4 (a PowerPoint presentation activity) and Activity 3 of the chapter (a video clip from a TV sitcom in which a man and woman speak in different styles) are video and computer activities."),
    ],
    exercises=uniq(
        _tr(_SC1 + _SC2 + [(k, e) for _, k, e in _SC3 + _SC4] + [(a, c) for a, b, c in _GR], k=3)
        + [M("Which style is used in Script 1 (the performance news)?", "Formal polite", ["Informal polite", "Formal blunt", "Informal blunt"], "-ㅂ/습니다."), M("Which style is used in Script 2 (tomorrow’s schedule)?", "Formal blunt", ["Formal polite", "Informal polite", "Informal blunt"], "-다."), M("Which style is used in Script 3 (the company dinner)?", "Informal polite", ["Formal polite", "Formal blunt", "Informal blunt"], "-아/어요."), M("Which style is used in Script 4 (Saturday plans)?", "Informal blunt", ["Informal polite", "Formal blunt", "Formal polite"], "-아/어."),
           M("What is the relationship in Script 1?", "A broadcaster and the audience", ["Two friends", "A teacher and a student", "Two soldiers"], "공연소식입니다."), M("What is the relationship in Script 2?", "A superior and subordinates", ["Two friends", "A broadcaster and listeners", "Colleagues"], "Military: 집합한다."), M("What is the relationship in Script 3?", "Co-workers", ["Close friends", "A broadcaster and listeners", "A superior and subordinates"], "과장님, 회식."), M("What is the relationship in Script 4?", "Close friends", ["Co-workers", "A teacher and a student", "A broadcaster and listeners"], "너 … 응."),
           M("Where is the company dinner?", "At Seoul Galbi in front of the company", ["At the library", "At a wedding hall", "At home"], "회사 앞 서울 갈비."), M("Why can speaker A not go to the dinner?", "A friend’s wedding", ["An exam", "A trip", "A meeting"], "친구 결혼식."), M("Why will the friend study at the library on Saturday?", "There is an exam next week", ["It is quiet", "To meet a teacher", "To borrow a book"], "다음 주에 시험이 있어."), M("What is the honorific form of 먹다?", "드시다", ["주무시다", "읽으시다", "드리다"], "먹다 → 드시다."), M("What is the honorific form of 자다?", "주무시다", ["드시다", "자시다", "일어나시다"], "자다 → 주무시다."),
           F("우리 할아버지는 아침 다섯 시쯤 ___. (honorific “gets up”)", "일어나십니다", ["일어납니다", "일어나요"], "-(으)시- + ㅂ니다."), F("그 후에 일곱 시쯤 아침을 ___. (honorific “eats”)", "드십니다", ["먹습니다", "먹으십니다"], "드시다."), F("그리고 보통 열 시쯤 ___. (honorific “sleeps”)", "주무십니다", ["잡니다", "자십니다"], "주무시다."), F("오전에는 노인대학에서 강연을 ___. (honorific “listens to”)", "들으십니다", ["듣습니다", "듣니다"], "듣다 → 들으십니다."),
           read_q("오늘의 공연소식입니다"), read_q("내일 일정을 말해 주겠다"), read_q("회식이 있다는데 어디에서 하는지 알아요"), read_q("우리 할아버지는 아침 다섯 시쯤 일어나십니다"), read_q("할아버지께서는 아침을 드십니다")]
    ),
)

# ================================================================== L6: Activity 2 - foreign K-pop idols
_KP = [
    ("미국의 언어학습 플랫폼 듀오링고에 따르면 한국 음악과 영화, 드라마의 세계적인 인기로 한국어를 배우려는 사람의 수가 이천이십일 년 이후 무려 칠십육 퍼센트나 늘어났다고 한다.", "According to the American language-learning platform Duolingo, owing to the worldwide popularity of Korean music, movies and dramas, the number of people who want to learn Korean has increased by a whole 76% since 2021."),
    ("그렇다면 우리나라에서 활동하고 있는 외국인 아이돌들은 어떻게 한국어를 배웠을까?", "Then how did the foreign idols who are active in our country learn Korean?"),
    ("인기 걸그룹 트와이스 멤버 쯔위는 한국어를 배우기 위해 드라마를 자주 본다고 한다.", "Tzuyu, a member of the popular girl group Twice, is said to often watch dramas in order to learn Korean."),
    ("대만에서 온 쯔위는 최근에 한 인터뷰에서 이렇게 말했다.", "Tzuyu, who came from Taiwan, said the following in a recent interview."),
    ("한국어는 아직도 어려운 편이에요. 제가 아직 모르는 단어가 많아요. 특히 방송에 출연했을 때 선배 가수들이 쓰는 단어들이 어렵게 느껴질 때가 많아요.", "Korean is still on the difficult side. There are many words I don’t know yet. In particular, when I appear on a show, there are many times the words that senior singers use feel difficult."),
    ("쯔위는 이렇게도 말했다.", "Tzuyu also said the following."),
    ("주위에서 한국어를 잘 하려면 드라마와 영화를 많이 보라고 해서 자주 보려고 해요. 또 드라마에서 새로운 단어나 표현이 나오면 부지런히 외우려고 해요.", "People around me tell me to watch many dramas and movies if I want to be good at Korean, so I try to watch often. Also, when a new word or expression comes up in a drama, I try to memorize it diligently."),
    ("또 다른 걸그룹 블랙핑크의 멤버인 리사는 태국에서 왔다.", "Lisa, a member of another girl group, Blackpink, came from Thailand."),
    ("데뷔 전부터 매일 한국어 수업을 두 시간씩 받았던 리사는 이렇게 말했다.", "Lisa, who had taken Korean classes for two hours every day since before her debut, said the following."),
    ("제가 멤버들과 같이 숙소 생활을 했어요. 그 때 다른 멤버들과 계속 한국어로 이야기하려고 많이 노력 했어요. 그래서 빨리 배운 것 같아요.", "I lived in the dorm together with the members. At that time I made a lot of effort to keep talking in Korean with the other members. So I think I learned fast."),
    ("한국어를 배울 때 어려운 점에 대해서는 리사는 이렇게 말하며 웃었다.", "About the difficult points when learning Korean, Lisa laughed and said the following."),
    ("멤버들이랑은 반말로 이야기하니까 다른 사람들한테 존댓말을 자연스럽게 쓰기가 어려웠어요. 그래서 실수도 많이 하고 틀린 표현도 많이 썼어요.", "Because I talk in blunt language with the members, it was hard to use honorific language naturally to other people. So I made many mistakes and used many wrong expressions."),
]
L6 = lesson(
    "Ch 28 · Activity 2: how foreign K-pop idols learned Korean (읽기)",
    "듀오링고 · 쯔위 · 리사 · 한국어를 배우는 방법 · 반말 · 존댓말 · 실수",
    requires=[],
    cards=[
        card("Activity 2 (Reading): a newspaper article about foreign K-pop stars learning Korean",
             "The book asks you to read the article about the Korean language learning experiences of some foreign K-pop stars and to answer in English: (1) What statistic is reported by Duolingo? (2) Fill in the table for 쯔위 and 리사: strategies in learning Korean and difficulties in learning Korean. The text is the book’s with the numbers spelled out in Hangul (2021 → 이천이십일 년, 76% → 칠십육 퍼센트) and the quotations set off as separate lines (the quotation marks are left out); the English is mine. The book glosses 방송에 출연하다: to appear on a show; 숙소: housing, accommodation.",
             examples=passage(_KP)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Question", "Answer (mine)"], [["1. What statistic is reported by Duolingo?", "The number of people who want to learn Korean has increased by 76% since 2021"], ["쯔위: strategies in learning Korean", "She often watches dramas; people around her advise watching many dramas and movies; she diligently memorizes new words and expressions from dramas"], ["쯔위: difficulties in learning Korean", "Korean is still on the difficult side; there are many words she doesn’t know; the words senior singers use on shows feel difficult"], ["리사: strategies in learning Korean", "She took a two-hour Korean class every day before her debut; she lived in the dorm with the members and made an effort to keep talking to them in Korean"], ["리사: difficulties in learning Korean", "She speaks blunt language (반말) with the members, so it was hard to use honorific language (존댓말) naturally with others, and she made many mistakes and used wrong expressions"]])]),
        card("Activities left out", "Activity 1 (a SMART Board activity), Activity 3 (a video clip), and Activity 4 (reading, speaking and writing activities with students’ own essays and group work, whose texts are not part of the book’s text) are computer, video and group activities."),
    ],
    exercises=uniq(
        _tr(_KP[:3] + _KP[3:], k=3)
        + [M("What does Duolingo report?", "The number of Korean learners has grown by 76% since 2021", ["Korean is the easiest language", "Korean learners have halved", "Most learners are Thai"], "칠십육 퍼센트 늘어났다."), M("Where does 쯔위 come from?", "Taiwan", ["Thailand", "China", "Japan"], "대만에서 온 쯔위."), M("Which group is 쯔위 a member of?", "Twice", ["Blackpink", "BTS", "Girls’ Generation"], "트와이스."), M("Which group is 리사 a member of?", "Blackpink", ["Twice", "Red Velvet", "BTS"], "블랙핑크."), M("Where does 리사 come from?", "Thailand", ["Taiwan", "Japan", "The Philippines"], "태국에서 왔다."),
           M("How does 쯔위 learn Korean?", "She watches dramas and memorizes new words", ["She reads novels", "She lives in Seoul only", "She takes daily classes"], "드라마를 자주 본다."), M("How long did 리사 take Korean classes every day?", "Two hours", ["One hour", "Four hours", "Thirty minutes"], "두 시간씩."), M("What is hard for 쯔위 on shows?", "The words senior singers use", ["The dancing", "The songs", "The cameras"], "선배 가수들이 쓰는 단어."), M("Why was honorific language hard for 리사?", "She talked in blunt language with the members", ["She never used it", "She was too shy", "Her teacher spoke blunt language"], "반말로 이야기하니까."),
           F("한국어를 배우려는 사람의 수가 ___나 늘어났다. (a whole)", "무려", ["아직", "특히"], "무려 = as many as."), F("새로운 단어나 표현이 나오면 ___ 외우려고 해요. (diligently)", "부지런히", ["우연히", "여전히"], "부지런히."), F("멤버들이랑은 반말로 이야기하니까 존댓말을 ___ 쓰기가 어려웠어요. (naturally)", "자연스럽게", ["솔직하게", "공손하게"], "자연스럽게."),
           read_q("한국어를 배우려는 사람의 수"), read_q("드라마를 자주 본다"), read_q("멤버들과 같이 숙소 생활을 했어요"), read_q("반말로 이야기하니까 존댓말이 어려웠어요")]
    ),
)

# ================================================================== L7: Topic C
_C_DLG = [
    ("마크", "한국에서는 인사하는 방법이 미국과 좀 다른 것 같아요. 그래서 제가 실수를 몇 번 했어요.", "The way of greeting in Korea seems a little different from America. So I made a few mistakes."),
    ("소연", "어떤 실수를 했어요?", "What kind of mistakes did you make?"),
    ("마크", "며칠 전에 친구 집에 갔을 때 인사하면서 할머니를 포옹했어요. 그래서 옆에 있는 사람들이 웃었어요.", "A few days ago when I went to a friend’s house I hugged the grandmother as I greeted her. So the people next to us laughed."),
    ("소연", "그랬어요? 한국에서는 보통 고개를 숙여서 인사해요. 그리고 어른한테는 허리를 굽혀서 공손히 인사하고요.", "Did you? In Korea we usually greet by bowing the head. And to elders we greet politely by bending at the waist."),
    ("마크", "그래요? 미국에서는 인사할 때 손을 흔들거나 악수를 해요. 그리고 포옹도 하고요.", "Is that so? In America when we greet, we wave a hand or shake hands. And we also hug."),
    ("소연", "또 미국사람들은 말하면서 제스처를 많이 쓰지요?", "Also, Americans use many gestures while talking, don’t they?"),
    ("마크", "네, 그렇죠. 한국사람들은 어때요? 한국에서 대화할 때 지켜야 할 에티켓이 있나요?", "Yes, that’s right. What about Koreans? Is there any etiquette that I should observe when talking in Korea?"),
    ("소연", "네, 어른과 대화할 때 보통 눈을 똑바로 쳐다보지 않아요. 또 다리를 꼬거나 흔드는 것도 좋지 않아요. 그리고 제스처를 많이 쓰지 않는 편이에요.", "Yes, when talking with elders, we usually do not stare straight into their eyes. Also, crossing or shaking the legs is not good either. And we tend not to use many gestures."),
    ("마크", "그래요? 미국에서는 대체로 상대방의 눈을 보면서 얘기하는데, 참, 내일 차 교수님 댁에 저녁 초대를 받았어요. 주의해야 할 식사예절이 있어요?", "Is that so? In America we generally talk looking into the other person’s eyes, and, oh, I have been invited to dinner at Professor Cha’s home tomorrow. Is there any table etiquette I should be careful about?"),
    ("소연", "네. 식사할 때는 어른보다 먼저 수저를 들지 않는 것이 좋아요. 그리고 음식을 주시면 두 손으로 받으세요.", "Yes. When eating, it is good not to pick up your spoon and chopsticks before the elders. And when they give you food, please receive it with both hands."),
    ("마크", "네. 소연 씨, 고마워요. 그렇게 하지요.", "Yes. Thank you, Soyeon. I will do that."),
]
_C_WORDS = ["고개", "공손", "굽히다", "꼬다", "-나(요)", "대체로", "들다", "부르다", "손짓", "숙이다", "실수", "악수", "에티켓", "예절", "제스처", "주의", "-지(요)", "쳐다보다", "포옹", "흔들다"]
L7 = lesson(
    "Ch 28 · Topic C: In Korea we bow our heads to greet (한국에서는 고개를 숙여서 인사해요)",
    "한국에서는 고개를 숙여서 인사해요 · 포옹 · 악수 · 에티켓 · 식사예절 · 두 손으로 받으세요",
    requires=[],
    cards=[
        card("Topic C: In Korea we bow our heads to greet (한국에서는 고개를 숙여서 인사해요)",
             "Mark and Soyeon are talking about the different ways of greeting and about etiquette in Korea and America. (The English is mine; the book gives none. The stage direction “(웃으면서)”, laughing, and the ellipsis in “얘기하는데…” are left out.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 공손(하다), 손짓(하다), 실수(하다), 악수(하다), 주의(하다) and 포옹(하다) can take 하다; –나(요) and –지(요) are the grammar of this chapter.",
             tables=[ktable(_rows([k for k in _C_WORDS if not any(c in k for c in "-(")]))]),
        card("Notes: the beckoning gesture",
             "Gestures differ between cultures. In America, to beckon someone toward you, a slightly cupped hand is moved toward you repeatedly. In Korea, to call someone over, the hand is held up with the palm facing down and the fingers are moved back and forth. (The book’s pictures are left out.)"),
        card("Activities left out", "Follow-up 2 (listening to two conversations about etiquette), the “Useful Link” (a website about everyday etiquette in Korea, 한국에서의 생활예절) and the PowerPoint presentation activity are audio, web and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not any(c in w for c in "-(")]))
        + _tr(_strip(_C_DLG), k=3)
        + [M("What mistake did Mark make?", "He hugged a grandmother when greeting her", ["He shook her hand", "He did not bow", "He was late"], "할머니를 포옹했어요."), M("How do Koreans usually greet?", "By bowing the head", ["By hugging", "By waving", "By shaking hands"], "고개를 숙여서 인사해요."), M("How do Koreans greet elders?", "By bending at the waist politely", ["By hugging", "By waving a hand", "By shaking hands"], "허리를 굽혀서 공손히."), M("How do Americans greet, according to Mark?", "They wave a hand, shake hands and hug", ["They bow their heads", "They bend at the waist", "They do not greet"], "손을 흔들거나 악수를 해요. 포옹도."),
           M("What do Koreans not do when talking with elders?", "Stare straight into their eyes", ["Speak politely", "Sit down", "Bow"], "눈을 똑바로 쳐다보지 않아요."), M("What else is not good when talking with elders?", "Crossing or shaking the legs", ["Smiling", "Nodding", "Sitting up straight"], "다리를 꼬거나 흔드는 것."), M("Who is Mark invited to dinner by?", "Professor Cha", ["Mr. Kim", "Soyeon", "A grandmother"], "차 교수님 댁."), M("What should you not do before the elders at the table?", "Pick up the spoon and chopsticks", ["Drink water", "Sit down", "Say thanks"], "먼저 수저를 들지 않는 것."), M("How should you receive food that an elder gives you?", "With both hands", ["With one hand", "With a bow only", "After tasting it"], "두 손으로 받으세요."),
           M("How do Koreans beckon someone?", "Palm down, with the fingers moving back and forth", ["Palm up with a finger", "Waving the whole arm", "Clapping"], "The book’s note."),
           F("한국에서는 보통 고개를 ___ 인사해요. (bowing)", "숙여서", ["굽혀서", "흔들어서"], "고개를 숙이다."), F("어른한테는 허리를 ___ 공손히 인사해요. (bending)", "굽혀서", ["숙여서", "꼬아서"], "허리를 굽히다."), F("다리를 ___ 흔드는 것도 좋지 않아요. (crossing or)", "꼬거나", ["들거나", "굽히거나"], "다리를 꼬다."), F("미국에서는 인사할 때 손을 ___ 악수를 해요. (wave or)", "흔들거나", ["굽히거나", "쳐다보거나"], "손을 흔들다."),
           read_q("고개를 숙여서 인사해요"), read_q("허리를 굽혀서 공손히 인사해요"), read_q("식사할 때는 어른보다 먼저 수저를 들지 않는 것이 좋아요"), read_q("음식을 주시면 두 손으로 받으세요"), read_q("제스처를 많이 쓰지 않는 편이에요")]
    ),
)

# ================================================================== L8: Topic C practice
_KA = [("공손히 고개를 숙여 인사한다.", "K", "Bow the head politely to greet.", "Korean"), ("인사할 때 포옹한다.", "A", "Hug when greeting.", "American"), ("상대방의 눈을 쳐다보며 대화한다.", "A", "Talk looking into the other person’s eyes.", "American"), ("어른 앞에서 다리를 꼬거나 흔들지 않는다.", "K", "Do not cross or shake the legs in front of elders.", "Korean"),
       ("어른보다 먼저 수저를 들지 않는다.", "K", "Do not pick up the spoon and chopsticks before the elders.", "Korean"), ("어른한테 물건을 두 손으로 주고 받는다.", "K", "Give and receive things to and from elders with both hands.", "Korean"), ("말하면서 제스처를 많이 사용한다.", "A", "Use many gestures while talking.", "American")]
_MATCH = [("쳐다보다", "to look at; to stare"), ("악수하다", "to shake hands"), ("실수하다", "to make a mistake"), ("부르다", "to call; to name"), ("꼬다", "to twist; to cross"), ("포옹하다 / 안다", "to hug; to embrace"), ("숙이다", "to bow; to bend (one’s head or upper body part) forward"), ("굽히다", "to bend"), ("흔들다", "to shake; to wave"), ("손짓하다", "to make a hand gesture")]
L8 = lesson(
    "Ch 28 · Topic C practice: Korean or American etiquette, and matching words",
    "한국과 미국의 예절 · 공손히 고개를 숙여 인사한다 · 쳐다보다 · 악수하다 · 실수하다 · 포옹하다",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): Korean (K) or American (A) etiquette?",
             "The book asks you to read the seven statements about forms of etiquette and to mark K for Korean etiquette and A for American etiquette. The statements are the book’s; the English and the answers are mine, from the dialog of Topic C.",
             tables=[table(["No.", "Statement", "K or A (mine)", "English (mine)"], [[str(i + 1), r[0], r[1] + " (" + r[3] + ")", r[2]] for i, r in enumerate(_KA)], say=[1])]),
        card("Activity 1a (Reading): match the Korean words to their English meanings",
             "The book asks you to draw lines between ten Korean words and their English meanings. The pairs below are the book’s Core Vocabulary meanings.",
             tables=[ktable(_MATCH)]),
        card("Activities left out", "Activity 1b (a SMART Board activity), Activity 2 (listening to dialogs), Activity 3 (a reading and speaking activity about two incidents of cultural misunderstanding, whose texts are not part of the book’s text) and Activity 4 (writing and speaking with the students’ own essays) are computer, audio and group activities."),
    ],
    exercises=uniq(
        [M("Is this Korean (K) or American (A) etiquette? " + r[0], r[3], [x for x in ("Korean", "American") if x != r[3]], "The dialog of Topic C.") for r in _KA]
        + _tr(_MATCH[:5] + _MATCH[5:], k=3)
        + [M("Which word means “to bow”?", "숙이다", ["굽히다", "꼬다", "흔들다"], "숙이다 = to bow."), M("Which word means “to cross”?", "꼬다", ["숙이다", "부르다", "흔들다"], "꼬다 = to twist; to cross."), M("Which word means “to wave”?", "흔들다", ["꼬다", "굽히다", "쳐다보다"], "흔들다 = to shake; to wave."), M("Which word means “to stare”?", "쳐다보다", ["부르다", "숙이다", "꼬다"], "쳐다보다 = to look at; to stare."),
           F("어른 앞에서 다리를 ___ 흔들지 않는다. (cross or)", "꼬거나", ["굽히거나", "부르거나"], "꼬다."), F("선생님이 이름을 ___ 손을 드세요. (call)", "부르면", ["숙이면", "굽히면"], "부르다."), F("새로 들어온 동료와 ___ 인사를 했습니다. (shaking hands)", "악수하며", ["포옹하며", "손짓하며"], "악수하다."), F("김 선생님이 사무실로 오라고 ___. (made a hand gesture)", "손짓했어요", ["악수했어요", "포옹했어요"], "손짓하다."),
           read_q("공손히 고개를 숙여 인사한다"), read_q("인사할 때 포옹한다"), read_q("상대방의 눈을 쳐다보며 대화한다"), read_q("어른한테 물건을 두 손으로 주고 받는다"), read_q("말하면서 제스처를 많이 사용한다")]
    ),
)

# ================================================================== L9: Grammar A: -지(요)


def _jiyo(v):
    return stem(v) + "지요"


def _jyo(v):
    return stem(v) + "죠"


_JV = [("청소하다", "to clean"), ("들다", "to lift; to carry"), ("먹다", "to eat"), ("가다", "to go"), ("읽다", "to read"), ("만들다", "to make"), ("가져오다", "to bring"), ("준비하다", "to prepare"), ("요리하다", "to cook"), ("치다", "to play (tennis)")]
_JS = [("교실은 제가 청소하지요.", "I will clean the classroom."), ("이 가방은 제가 들지요.", "I will carry this bag."), ("점심에는 피자를 먹지요.", "Let’s eat pizza for lunch."), ("제 차로 가죠.", "Let’s go in my car.")]
_JP = [("음식은 내가 만들지요.", "I will make the food. (cf. 만들겠어요)"), ("오늘은 한국 식당에서 먹지요.", "Let’s eat at a Korean restaurant today. (cf. 먹읍시다)"), ("음식은 제가 만들죠.", "I will make the food. (contracted)"), ("오늘은 한국 식당으로 가시죠.", "Let’s go to a Korean restaurant today. (contracted, honorific)")]
_JTAG = [("오늘 날씨가 좋지요?", "The weather is nice today, isn’t it?"), ("이 음식이 참 맛있지요?", "This food is really delicious, isn’t it?")]
_PIC = [("A", "서인수 씨, 이번 피크닉에 콜라를 가져올 수 있나요?", "Insu Seo, can you bring cola to this picnic?"), ("서인수", "그럼요. 콜라는 제가 가져오지요. 그럼, 석민우 씨가 농구공을 가져올 수 있나요?", "Of course. I will bring the cola. Then, Minwoo Seok, can you bring a basketball?"), ("석민우", "네, 알겠습니다. 농구공은 제가 준비하지요.", "Yes, understood. I will prepare the basketball.")]
L9 = lesson(
    "Ch 28 · Grammar B: –지(요), intention or suggestion in a friendly manner",
    "-지요 · -죠 · 제가 청소하지요 · 제 차로 가죠 · 오늘은 한국 식당에서 먹지요",
    requires=[],
    cards=[
        card("–지(요): intention or suggestion in a friendly manner",
             "Recall that you have learned –지요 as a tag question: 오늘 날씨가 좋지요? and 이 음식이 참 맛있지요? Now you will learn that –지요 can also be used in statements to express the speaker’s intention (“I will”) or a suggestion (“Let’s”). For example, 음식은 내가 만들지요 (cf. 만들겠어요) = I will make the food; and 오늘은 한국 식당에서 먹지요 (cf. 먹읍시다) = Let’s eat at a Korean restaurant today.\n\n"
             "–지요 is often contracted to –죠: 음식은 제가 만들죠. 오늘은 한국 식당으로 가시죠.",
             examples=passage(_JTAG + _JP)),
        card("The rule",
             "Action verb stem + 지(요). The book’s examples (the English is mine):",
             examples=passage(_JS)),
        card("Forms (mine)", "Verb stem + 지요, and the contracted –죠.",
             tables=[table(["Verb", "Meaning", "-지요", "-죠"], [[v, m, _jiyo(v), _jyo(v)] for v, m in _JV], say=[0, 2, 3])]),
        card("Follow-up 1 (Speaking): the model", "The book asks partners to read phrases from a list, and the partner repeats each using –지요. The book’s model: A: 테니스를 치다. B: 오늘 저녁에 테니스를 치지요. And B: 저녁을 요리하다. A: 오늘 제가 저녁을 요리하지요.",
             examples=dlg([("A", "테니스를 치다.", "To play tennis."), ("B", "오늘 저녁에 테니스를 치지요.", "I will play tennis this evening."), ("B", "저녁을 요리하다.", "To cook dinner."), ("A", "오늘 제가 저녁을 요리하지요.", "I will cook dinner today.")])),
        card("Follow-up 5 (Speaking): 이번 주말에 소풍을 가지요 (let’s go on a picnic this weekend)",
             "Your class is going on a picnic at the beach this weekend, so you discuss what is needed and what you can bring: first list in English what is needed and five things you can bring, then meet at least three classmates to exchange information using –지요 and –나요. The book’s model (the English is mine; the book’s second B is a third speaker here, and 피크닉 is the loan word for “picnic”):",
             examples=dlg(_PIC)),
        card("Activities left out", "Follow-up 2 (listening) and the partner and class speaking activities (Follow-ups 1 and 5) need partners and your teacher’s lists, which are not in the book’s text."),
    ],
    exercises=uniq(
        _tr(_JS + _JP + _JTAG + [(k, e) for _, k, e in _PIC], k=3)
        + [M("What can –지요 express in a statement?", "The speaker’s intention or a suggestion", ["A past action", "A reason", "A comparison"], "I will / Let’s."), M("What is the contracted form of –지요?", "–죠", ["–쥬", "–지", "–져"], "만들죠."), M("What does 음식은 내가 만들지요 mean?", "I will make the food", ["Let’s make the food", "You make the food", "I made the food"], "Intention."), M("What does 오늘은 한국 식당에서 먹지요 mean?", "Let’s eat at a Korean restaurant today", ["I will eat alone", "I ate at a Korean restaurant", "Don’t eat there"], "Suggestion."),
           M("Which verbs take –지요?", "Action verbs", ["Only adjectives", "Only nouns", "Only the copula"], "Action verb stem + 지(요)."), M("What does 오늘 날씨가 좋지요? ask?", "A tag question: nice today, isn’t it?", ["An intention", "A suggestion", "A command"], "–지요? as a tag question."), M("Which is a suggestion “Let’s go in my car”?", "제 차로 가죠.", ["제 차로 갔어요.", "제 차로 가요?", "제 차가 있어요."], "–죠."),
           F("교실은 제가 ___. (I will clean)", "청소하지요", ["청소했지요", "청소하세요"], "청소하다 + 지요."), F("이 가방은 제가 ___. (I will carry)", "들지요", ["드지요", "들어요"], "들다 + 지요."), F("점심에는 피자를 ___. (Let’s eat)", "먹지요", ["먹었지요", "먹으세요"], "먹다 + 지요."), F("콜라는 제가 ___. (I will bring)", "가져오지요", ["가져왔지요", "가져오세요"], "가져오다 + 지요."), F("농구공은 제가 ___. (I will prepare)", "준비하지요", ["준비했지요", "준비하세요"], "준비하다 + 지요."),
           read_q("교실은 제가 청소하지요"), read_q("이 가방은 제가 들지요"), read_q("제 차로 가죠"), read_q("오늘은 한국 식당에서 먹지요"), read_q("콜라는 제가 가져오지요")]
    ),
)

# ================================================================== L10: Grammar C: -나(요)


def _na(v, pst=False):
    st = past(v) if pst else stem(v)
    l, vv, t = _K.decompose(st[-1])
    if t == "ㄹ":
        st = st[:-1] + _K.compose(l, vv, "")
    return st + "나요"


_NV = [("가다", "to go"), ("읽다", "to read"), ("먹다", "to eat"), ("살다", "to live"), ("만들다", "to make"), ("하다", "to do"), ("운동하다", "to exercise"), ("집합하다", "to assemble")]
_NS = [("민기 씨는 체육관에 자주 가나요?", "Does Mingi go to the gym often?"), ("이 책은 누가 읽나요?", "Who reads this book?"), ("한국사람들은 매일 김치를 먹나요?", "Do Koreans eat kimchi every day?"), ("한국사람들은 매일 김치를 먹나?", "Do Koreans eat kimchi every day? (asked to oneself)"), ("어제 저녁은 누가 요리했나?", "Who cooked dinner yesterday? (asked to oneself)"), ("김 일병, 몇 시에 집합하나?", "Private First Class Kim, what time do you have formation? (asked to a subordinate)"), ("김 상병, 어제 어디에서 운동했나?", "Corporal Kim, where did you exercise yesterday? (a military linguist asking a specialist)")]
_NMOD = [("A", "언제 저녁을 먹나요?", "When do you eat dinner?"), ("B", "저는 보통 다섯 시에 저녁을 먹습니다.", "I usually eat dinner at five."), ("B", "이번 주말에 산호세에 가나요?", "Are you going to San Jose this weekend?"), ("A", "네, 이번 주말에 김병장과 함께 산호세에 갑니다.", "Yes, this weekend I am going to San Jose together with Sergeant Kim.")]
L10 = lesson(
    "Ch 28 · Grammar C: –나(요), the interrogative ending",
    "-나요 · 먹나요 · 가나요 · 읽나요 · 집합하나 · 요리했나",
    requires=[],
    cards=[
        card("–나(요): an interrogative ending",
             "한국사람들은 매일 김치를 먹어요? can also be said 한국사람들은 매일 김치를 먹나요? There is no difference in meaning between the two. –나요 is a variation of –아/어요 and is an informal polite ending, but it is used only for questions. It softens the tone of the question and is used more by female speakers.\n\n"
             "The 요 can be dropped in the informal blunt style. –나 is used to direct a question to oneself or to one’s subordinate in a rigid hierarchy, such as the military: 한국사람들은 매일 김치를 먹나? (to oneself); 김 일병, 몇 시에 집합하나? (to a subordinate: Private First Class Kim, what time do you have formation?).",
             examples=passage(_NS[:1] + _NS[2:4] + _NS[5:6])),
        card("The rule", "Verb stem + 나(요)? The book’s examples (the English is mine; the book’s “MLI asking; SPC Kim” means a military language instructor asking a specialist):",
             examples=passage(_NS)),
        card("Forms (mine)", "Verb stem + 나요 (a stem ending in ㄹ drops the ㄹ: 살다 → 사나요, 만들다 → 만드나요), and the past form with –았/었나요.",
             tables=[table(["Verb", "Meaning", "-나요?", "Past: -았/었나요?"], [[v, m, _na(v), _na(v, True)] for v, m in _NV], say=[0, 2, 3])]),
        card("Follow-up 3 (Speaking): the model", "The book asks partners to read phrases using –나요 and the other partner answers. The book’s model (the English is mine; 산호세 is San Jose):",
             examples=dlg(_NMOD)),
        card("Activities left out", "Follow-up 4 (listening) and the partner speaking activity of Follow-up 3 need partners and your teacher’s lists."),
    ],
    exercises=uniq(
        _tr(_NS + [(k, e) for _, k, e in _NMOD], k=3)
        + [M("What is –나요 used for?", "Questions only", ["Statements only", "Commands", "Suggestions"], "Informal polite, only for questions."), M("Is there a difference in meaning between 먹어요? and 먹나요?", "No difference in meaning", ["Yes, it is past tense", "Yes, it is a command", "Yes, it is a statement"], "The book’s note."), M("What does –나요 do to the tone?", "It softens it", ["It makes it harsh", "It makes it formal", "It makes it a command"], "Softer."), M("Who uses –나요 more?", "Female speakers", ["Male speakers", "Children", "Soldiers"], "The book’s note."),
           M("What is –나 (no 요) used for?", "Asking oneself or a subordinate in a rigid hierarchy", ["Talking to elders", "Giving commands", "Making suggestions"], "한국사람들은 매일 김치를 먹나?"), M("Where is –나 used to a subordinate?", "In the military", ["In a school", "In a restaurant", "On television"], "김 일병, 몇 시에 집합하나?"), M("What do you drop from –나요 for informal blunt speech?", "요", ["나", "ㅁ", "–"], "먹나요 → 먹나."),
           F("민기 씨는 체육관에 자주 ___? (go)", "가나요", ["가지요", "갔어요"], "가다 + 나요."), F("이 책은 누가 ___? (reads)", "읽나요", ["읽지요", "읽어요"], "읽다 + 나요."), F("어제 저녁은 누가 ___? (cooked, to oneself)", "요리했나", ["요리하나요", "요리한다"], "요리했나."), F("김 일병, 몇 시에 ___? (do you have formation)", "집합하나", ["집합했어요", "집합한다"], "집합하나."), F("어디에 ___? (do you live)", "사나요", ["살나요", "삽니나요"], "살다 → 사나요."),
           read_q("민기 씨는 체육관에 자주 가나요"), read_q("이 책은 누가 읽나요"), read_q("한국사람들은 매일 김치를 먹나요"), read_q("김 일병, 몇 시에 집합하나"), read_q("언제 저녁을 먹나요")]
    ),
)

# ================================================================== L11: core vocabulary and self-evaluation
_CV_SECS = [("Generations", _CV_GEN), ("Courtesy and etiquette", _CV_ETI), ("Language", _CV_LAN), ("Other words", _CV_OTH), ("Loan words", _CV_LOAN), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:-1] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if "-" not in r[0]]
    ns = [r for r in rows if "-" in r[0]]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L11 = lesson(
    "Ch 28 · Core vocabulary and self-evaluation",
    "주요 단어 · 예의 · 존댓말 · 반말 · 신세대 · 기성세대 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. Where the book writes two forms together (for example 기성세대/구세대 or 사투리/방언), the forms are written with a slash. The book’s related words (the synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify different generations and talk about them; identify and use two different language registers, 존댓말 and 반말; and identify and talk about Korean manners and etiquette.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; a summary of speech styles; the verb ending –지(요); the interrogative ending –나(요); and the Sino-Korean syllables 례/예 (禮) and 음 (音)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does –지(요) express in a statement?", "Intention or suggestion in a friendly manner", ["A past action", "A reason", "A comparison"], "운전은 제가 하지요."), M("What is –나(요) used for?", "Questions", ["Statements", "Commands", "Suggestions"], "우리 점심은 무엇을 먹나요?"), M("What is 반말?", "blunt language; impolite language", ["honorific language", "a standard language", "a dialect"], "반말."), M("What is 존댓말?", "honorific language", ["blunt language", "a dialect", "an expression"], "존댓말."), M("What is 표준말?", "a standard language", ["a dialect", "blunt language", "honorific language"], "표준말."), M("What is 사투리?", "a dialect; vernacular", ["a standard language", "an accent mark", "a proverb"], "사투리 / 방언."),
           M("What is 기성세대?", "the older generation", ["the younger generation", "children", "foreigners"], "기성세대."), M("What is 신세대?", "the younger generation", ["the older generation", "the military", "teachers"], "신세대."), M("What is 예절?", "etiquette", ["a mistake", "a gesture", "a habit"], "예절."), M("What is 제스처?", "a gesture", ["etiquette", "a hug", "a bow"], "제스처."), M("What is 에티켓?", "etiquette", ["a gesture", "an opinion", "a mistake"], "에티켓."),
           F("한국 사람들은 ___가 바릅니다. (courtesy)", "예의", ["의견", "버릇"], "예의가 바르다."), F("신 선생님은 ___ 자기 생각을 말하는 편이에요. (frankly)", "솔직히", ["우연히", "여전히"], "솔직히."), F("어제 박 선생님을 영화관에서 ___ 만났습니다. (by chance)", "우연히", ["솔직히", "부지런히"], "우연히."), F("김 일병은 ___ 김치를 못 먹습니다. (still)", "여전히", ["우연히", "대체로"], "여전히."), F("___ 저희 가족은 주말에 일찍 일어납니다. (generally)", "대체로", ["여전히", "솔직히"], "대체로."),
           read_q("주요 단어"), read_q("예절"), read_q("존댓말"), read_q("반말"), read_q("사투리")]
    ),
)

UNIT = unit("Semester 1 · Unit 7 · Chapter 28: Polite Koreans (예의 바른 한국인)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11])

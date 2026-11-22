"""Unit 33: KBC Semester 1, Unit 7, Chapter 26 - Family Events and Marriage (가정행사와 결혼 문화).
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

# ---- the core vocabulary of Chapter 26 (meanings and examples are the book's; digits respelled)
_CV_ANI = [
    ("말", "a horse", "제주도에는 말이 많습니다."),
    ("뱀", "a snake", "뱀을 싫어하는 사람들이 많습니다."),
    ("용", "(龍) a dragon", "정 선생님은 용띠예요."),
    ("원숭이", "a monkey", "원숭이는 바나나를 좋아해요."),
    ("쥐", "a rat; a mouse", "쥐는 고양이를 무서워해요."),
    ("호랑이", "a tiger", "동물원에서 호랑이를 구경했어요."),
]
_CV_OCC = [
    ("돌", "the first birthday (see the Cultural Note)", "최 선생님 막내 아들은 다음달이 돌입니다. 최 선생님 가족은 집에서 돌잔치를 하려고 합니다."),
    ("떡", "a rice cake", "친구 아들 돌잔치에서 떡과 과일을 많이 먹었습니다."),
    ("백일", "(百日) the 100th day (since birth)", "김 선생님 딸 백일이 다음 주입니다."),
    ("상", "(床) a (floor) table", "아들 돌잡이상에 마이크와 연필과 돈을 놓았어요."),
    ("초대장", "(招待狀) an invitation; “invitation card”", "친구 아들 돌잔치 초대장을 받았습니다."),
    ("칠순", "(七旬) the 70th birthday", "한국사람들은 칠순 잔치를 크게 해요."),
    ("팔순", "(八旬) the 80th birthday", "요즘은 팔순까지 오래 사시는 분들이 많아요."),
]
_CV_MAR = [
    ("결혼식", "(結婚式) a wedding ceremony", "김 병장이 다음 주에 한국호텔에서 결혼식을 합니다."),
    ("결혼정보회사", "(結婚情報會社) a marriage agency; “marriage information company”", "결혼정보회사 소개로 제 아내를 만났습니다."),
    ("맞선", "an arranged meeting with a prospective bride/groom (맞선(을) 보다: to meet one’s prospective bride/groom in an arranged meeting)", "어머니 소개로 내일 호텔 커피숍에서 맞선을 봅니다."),
    ("상대 / 상대방", "(相對(方)) the other party; a counterpart; the opposite party; an opponent", "어제 맞선 상대가 마음에 들었어요."),
    ("소개팅 / 미팅", "a blind date (~하다: to go on a blind date)", "저는 대학 다닐 때 소개팅을 많이 해 봤어요."),
    ("시집", "getting married for a woman; “(woman’s) in-laws’ home” (~가다: to get married) (see the Cultural Notes of Chapter 25)", "김 선생님은 몇 살 때 시집갔습니까?"),
    ("신랑", "(新郞) a groom; “new husband”", "결혼식에서 신랑이 먼저 입장합니다."),
    ("신부", "(新婦) a bride; “new wife”", "신부는 보통 아버지와 함께 결혼식장에 들어갑니다."),
    ("신혼", "(新婚) a new marriage; newly married", "스미스 씨는 지난 달에 결혼했습니다. 신혼 부부입니다."),
    ("약혼", "(約婚) an engagement; “promising a marriage” (~하다: to be engaged)", "제 친구 영희는 작년 겨울에 약혼했고 올해 여름에 결혼할 예정입니다."),
    ("연애", "(戀愛) dating (~하다: to date; to be in a romantic relationship)", "저는 아내와 결혼하기 전에 이 년 동안 연애했습니다."),
    ("예물", "(禮物) a wedding gift exchanged between the bride and groom; “(wedding) ceremony item”", "작년에 아내한테서 결혼 예물로 시계를 받았습니다."),
    ("예식장", "(禮式場) a wedding hall; “(wedding) ceremony place”", "가을에는 결혼하는 사람들이 많아서 예식장을 예약하기 어렵습니다."),
    ("이상형", "(理想型) an ideal type", "어제 맞선에서 이상형의 여자를 만났습니다."),
    ("장가", "(丈家) getting married for a man; “(man’s) in-laws’ home” (~가다 / 들다: to get married) (see the Cultural Notes of Chapter 25)", "김 선생님은 언제 장가가셨습니까?"),
    ("재혼", "(再婚) remarriage; second marriage (~하다: to be remarried)", "결혼정보회사에는 재혼을 원하는 회원들이 많습니다."),
    ("주례", "(主禮) officiating a wedding; marriage officiant; “master of the (wedding) ceremony” (~하다 / 서다: to officiate a wedding)", "제 결혼식에서는 정 교수님께서 주례를 서 주셨습니다."),
    ("중매", "(仲媒) matchmaking (~하다 / 서다: to matchmake; to act as a go-between)", "한국에서는 중매로 결혼하는 사람들이 많아요."),
    ("청첩장", "(請牒狀) a wedding invitation; “wedding invitation card”", "지난 주말에는 결혼 청첩장을 세 장이나 받았습니다."),
    ("축의금", "(祝儀金) gift money; “congratulatory money”", "축의금은 보통 얼마를 내나요?"),
    ("피로연", "(披露宴) a wedding reception (~하다: to give a wedding reception)", "피로연은 예식장 옆 서울식당에서 있습니다."),
]
_CV_LOAN = [
    ("마이크", "a mic(rophone)", "김 일병은 마이크를 잡으면 가수처럼 노래를 잘 부릅니다."),
    ("웨딩드레스", "a wedding dress; a wedding gown", "신부의 웨딩드레스는 흰색이 많습니다."),
]
_CV_OTH = [
    ("강사", "(講師) an instructor", "서울 대학에서 영어 시간 강사를 구합니다."),
    ("공", "a ball", "친구들과 점심 시간에 공놀이를 했어요."),
    ("교수", "(敎授) a professor", "영신 씨 아버님은 대학 교수님이십니다."),
    ("궁금하다", "to be curious; to wonder about", "내일 날씨가 어떨지 궁금합니다."),
    ("-(으)ㄴ / 는 대신(에) / ~ 대신(에)", "(代身) instead of; rather than; in place of (see the grammar on 대신(에))", "병원에 가는 대신에 약을 사서 먹었어요. 커피 대신에 차를 마셔보세요."),
    ("-는 중이다 / ~ 중이다", "in the middle of; in the process of (see the grammar on 중이다)", "김 선생님은 지금 휴가 중입니다."),
    ("단정하다", "(端正) to be neat (in appearance); to be decent (in behavior)", "정인 씨는 항상 단정하게 옷을 입습니다."),
    ("똑똑하다", "to be clever; to be bright", "김 이병은 아주 똑똑한 학생입니다."),
    ("띠", "a birth year of the Asian zodiac", f"{_kn(1988)} 년에 태어난 사람은 무슨 띠입니까?"),
    ("미리", "beforehand; in advance", "생일 선물은 미리 준비하세요."),
    ("사회", "(司會) a master of ceremonies; an emcee (~보다: to conduct a meeting or ceremony)", "결혼식 사회는 보통 신랑 친구가 봅니다."),
    ("실", "thread; yarn; string", "아기가 돌잡이에서 실을 잡았어요."),
    ("쌀", "rice (as a crop); (uncooked) rice", "아시아 사람들은 주로 쌀로 만든 음식을 먹습니다."),
    ("-아 / 어(서) 죽겠다", "expression used to exaggerate feelings about a condition (see the grammar on 죽겠다)", "일이 너무 많아서 힘들어 죽겠어요."),
    ("얼마", "some (amount in money, time, etc.)", "얼마 전에 박 일병 생일이었어요."),
    ("연필", "(鉛筆) a pencil", "시험을 볼 때는 펜 대신에 연필을 사용하세요."),
    ("-(으)ㄹ 생각 / 계획 / 예정이다", "(計劃/豫定) to intend to; to plan to (see the grammar on plans)", "제 생일 파티를 호텔에서 할 예정이에요."),
    ("일시", "(日時) date and time", "광고에 여행 일시가 나와 있습니다."),
    ("자라다", "to grow (up); to be brought up", "한 달 만에 아기가 많이 자랐어요."),
    ("잡다", "to grab; to catch", "우리 아들은 돌잔치 때 연필을 잡았어요."),
    ("장소", "(場所) a place; a location", "많은 사람이 모이기에 그 장소는 좋지 않아요."),
    ("전문적", "(專門的) expert; professional; special", "결혼식 사진은 사진을 전문적으로 찍는 사람에게 합시다."),
    ("조건", "(條件) a condition; a qualification; a requirement", "일등 남편의 조건이 뭐예요?"),
    ("참", "really; truly; truth", "오늘은 날씨가 참 좋아요!"),
    ("참석", "(參席) attendance; presence (~하다: to attend; to be present at)", "회의에 직원 모두가 참석했습니다."),
    ("학원", "(學院) a private institute; an academy", "매일 학교가 끝난 후 영어학원에 가야 합니다."),
    ("행복", "(幸福) happiness; well-being (~하다: to be happy)", "행복은 우리 주변에 있습니다."),
    ("활달하다", "(闊達) to be outgoing; to be lively (in personality); to be broad-minded", "김 병장은 성격이 아주 활달한 편입니다."),
]
_CV_SINO = [("식", "(式) a ceremony; a style; a way", "결혼식, 예식장, 약혼식, 한국식, 자동식, 수동식"), ("애", "(愛) love; loving", "애국, 애인, 애견, 형제애"), ("축", "(祝) congratulation; celebration; wishing", "축하, 축가, 축의금")]
_ALL = {r[0]: r for r in _CV_ANI + _CV_OCC + _CV_MAR + _CV_LOAN + _CV_OTH + _CV_SINO}
_EXTRA = {"상대 / 상대방": "the other party; a counterpart", "소개팅 / 미팅": "a blind date", "맞선": "an arranged meeting with a prospective bride/groom", "시집": "getting married for a woman", "장가": "getting married for a man",
          "-(으)ㄴ / 는 대신(에) / ~ 대신(에)": "instead of; rather than", "-는 중이다 / ~ 중이다": "in the middle of", "-아 / 어(서) 죽겠다": "(an exaggeration of feelings)", "-(으)ㄹ 생각 / 계획 / 예정이다": "to plan to; to intend to",
          "돌": "the first birthday", "초대장": "an invitation", "주례": "officiating a wedding; marriage officiant", "중매": "matchmaking", "연애": "dating", "약혼": "an engagement", "재혼": "remarriage; second marriage", "신혼": "a new marriage; newly married", "행복": "happiness", "참석": "attendance; presence",
          "돌잔치": "a first birthday party", "돌상": "the first birthday table", "돌잡이": "the first birthday grabbing (choosing an item)", "잔치": "a feast; a party", "주문하다": "to order", "골프공": "a golf ball", "첫돌": "the first birthday",
          "소": "an ox; a cow", "토끼": "a rabbit", "양": "a sheep", "닭": "a rooster; a chicken", "개": "a dog", "돼지": "a pig",
          "중매결혼": "an arranged (matchmade) marriage", "연애결혼": "a love marriage", "결혼 정보": "marriage information", "미술학원": "an art institute", "유학": "studying abroad", "혼수": "items needed for marriage (婚需)", "전세": "a large deposit to rent a house (jeonse)",
          "애인": "one’s lover; one’s boyfriend/girlfriend", "애국": "patriotism; love of one’s country", "애연가": "a habitual smoker; a chain smoker; “a person who loves smoking”", "열애": "passionate love", "모성애": "maternal love", "애사심": "love for one’s company",
          "축가": "a song of congratulation; a carol", "축배": "a toast; a celebratory drink; “celebration bowl”", "축복": "blessing; benediction; “wishing [for] fortune”", "축일": "a festival (day); a national holiday; “celebration day”", "축하": "a celebration; congratulations",
          "입학식": "an entrance ceremony; “school entering ceremony”", "한국식": "Korean style; Korean way", "서양식": "Western style", "자동식": "automatic (style); “self-moving style”", "졸업식": "a graduation ceremony", "약혼식": "an engagement ceremony", "수동식": "manual style; hand-operated",
          "가족": "a family"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)

# ================================================================== L1: objectives, zodiac, first birthday
_ZOD = [("쥐띠", 1984, "rat", "a rat; a mouse"), ("소띠", 1985, "ox", "ox; cow"), ("호랑이띠", 1986, "tiger", "a tiger"), ("토끼띠", 1987, "rabbit", "a rabbit"), ("용띠", 1988, "dragon", "a dragon"), ("뱀띠", 1989, "snake", "a snake"),
        ("말띠", 1990, "horse", "a horse"), ("양띠", 1991, "sheep", "a sheep"), ("원숭이띠", 1992, "monkey", "a monkey"), ("닭띠", 1993, "rooster", "a rooster; a chicken"), ("개띠", 1994, "dog", "a dog"), ("돼지띠", 1995, "pig", "a pig")]
_ITEMS = [("돈", "money: wealth"), ("쌀", "rice: wealth"), ("실", "thread (silk thread): longevity"), ("연필", "a pencil: learning"), ("마이크", "a microphone (a modern item)"), ("골프공", "a golf ball (a modern item)")]
_OBJ26 = ("When you finish the chapter you will be able to: identify and talk about important birthdays like the 1st, 70th, and 80th; identify and talk about events related to courting and a wedding, and one’s ideal type of partner; and offer an invitation to an important family event.\n\n"
          "You will become familiar with: the new words and phrases in the Core Vocabulary section; –는 중이다 / ~중이다 (to be in the middle of; to be –ing); –아/어(서) 죽겠다 used to exaggerate feelings about a condition; –(으)ㄴ/는 대신(에) and ~대신(에) (instead of; rather than; in place of); –(으)ㄹ 계획/생각/예정이다 (plan to; intend to; be going to); and the Sino-Korean syllables 애 (愛), 축 (祝) and 식 (式).")
L1 = lesson(
    "Ch 26 · What the chapter teaches, the Asian zodiac and the first birthday",
    "가정행사와 결혼 문화 · 띠 · 돌 · 돌잡이 · 칠순 · 팔순 · 쥐띠 · 용띠",
    requires=[],
    cards=[
        card("What Chapter 26 teaches (가정행사와 결혼 문화)", "Chapter 26, “Family Events and Marriage”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n" + _OBJ26),
        card("New vocabulary: animals, and occasions",
             "The animals of the zodiac and the family occasions of Topic A (the meanings are the book’s).",
             tables=[ktable(_rows([r[0] for r in _CV_ANI])), ktable(_rows([r[0] for r in _CV_OCC]))]),
        card("Notes: the Asian zodiac (띠)",
             "띠 means birth year according to the Asian zodiac. The book’s picture shows the twelve signs with a birth year each (the years are spelled out in the second column; the English animal names of the signs the book does not gloss are mine).",
             tables=[table(["띠", "Birth year (spoken)", "Year", "Animal"], [[z, _kn(y) + " 년", str(y), a] for z, y, a, _ in _ZOD], say=[0, 1])]),
        card("Cultural note: the first birthday",
             "Koreans traditionally have a large celebration, called 첫돌 or 돌, for a child’s first birthday. This practice originates from the fact that in the past many infants did not survive their first year. For their child’s first birthday, parents prepare a 돌상 (first birthday table). This table is laden with various foods, such as rice cakes, fruits, and other items. The table is stacked high, symbolizing the wish for the child’s prosperous future. The highlight of the event is 돌잡이 (“first birthday grabbing”), where people watch what item the child grabs first. The chosen item is believed to predict the child’s future. Parents usually use money or rice to symbolize wealth, silk thread for longevity, and a pencil for learning. These days, many parents use more varied objects, such as a microphone, a golf ball, a computer mouse, or a stethoscope.",
             tables=[ktable(_ITEMS)]),
        card("Activities left out", "The vocabulary builder (a PowerPoint presentation with pictures and sounds, Activities 1 and 3 on the SMART Board, the Sino-Korean presentation and Activity 4, the word lists A and B for pairs) is a picture, computer and partner activity."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([r[0] for r in _CV_ANI] + ["돌", "떡", "백일", "상", "칠순", "팔순"]))
        + _tr([(z, a2) for z, _, _, a2 in _ZOD[:6]], k=3) + _tr(_ITEMS)
        + [M(f"Which sign is the birth year {y} in the book’s zodiac?", z, [x[0] for x in _ZOD if x[0] != z][:3], f"{y} → {z}.") for z, y, _, _ in _ZOD]
        + [M("What does 띠 mean?", "a birth year of the Asian zodiac", ["a first birthday", "a birthday party", "a kind of rice cake"], "띠 = zodiac sign."), M("What is 돌?", "the first birthday", ["the 100th day", "the 70th birthday", "the 80th birthday"], "돌 = first birthday."), M("What is 칠순?", "the 70th birthday", ["the first birthday", "the 80th birthday", "the 100th day"], "칠순 = 70th birthday."), M("What is 팔순?", "the 80th birthday", ["the 70th birthday", "the first birthday", "the 100th day"], "팔순 = 80th birthday."),
           M("Why did Koreans celebrate the first birthday so much?", "Many infants did not survive their first year", ["It was a legal rule", "It was a religious duty", "It was the child’s first walk"], "The book’s cultural note."), M("What is the highlight of the 돌 celebration?", "돌잡이, watching what item the child grabs first", ["The cake", "The songs", "The speech"], "돌잡이."), M("What does a pencil on the 돌상 symbolize?", "learning", ["wealth", "longevity", "health"], "A pencil: learning."), M("What does silk thread symbolize?", "longevity", ["wealth", "learning", "luck"], "Thread: long life."), M("What do money or rice symbolize?", "wealth", ["learning", "longevity", "health"], "Money or rice: wealth."),
           F("한국 사람들은 아기의 첫 생일을 ___이라고 해요. (the first birthday)", "돌", ["백일", "띠"], "돌 = first birthday."), F("우리 아들은 돌잔치 때 연필을 ___. (grabbed)", "잡았어요", ["자랐어요", "놓았어요"], "잡다 = to grab."), F("저는 ___띠예요. (the 1988 sign)", "용", ["뱀", "말"], "용띠 = 1988."),
           read_q("돌"), read_q("백일"), read_q("칠순"), read_q("호랑이"), read_q("원숭이")]
    ),
)

# ================================================================== L2: Topic A
_A_DLG = [
    ("정우 엄마", "윤하가 많이 자랐네!", "Yunha has grown a lot!"),
    ("윤하 엄마", "이 주 후에 윤하 돌이잖아!", "Yunha’s first birthday is in two weeks, you know!"),
    ("정우 엄마", "벌써? 얼마 전에 백일이었는데.", "Already? It was her 100th day only a little while ago."),
    ("윤하 엄마", "맞아, 시간 참 빨리 가.", "Right, time really goes fast."),
    ("정우 엄마", "그럼, 윤하가 올해 돌이니까 쥐띠인가?", "Then, since Yunha’s first birthday is this year, is she a rat-year baby?"),
    ("윤하 엄마", "맞아. 쥐띠야.", "Right. She is a rat-year baby."),
    ("정우 엄마", "그렇구나. 그런데, 돌잔치는 어디서 해?", "I see. By the way, where are you having the first birthday party?"),
    ("윤하 엄마", "집에서 하려고 생각하고 있어.", "I am thinking of having it at home."),
    ("정우 엄마", "그래? 잔치 준비하려면 바쁘겠다.", "Really? You must be busy if you are going to prepare a party."),
    ("윤하 엄마", "응, 좀 바빠. 떡도 주문하고 초대장도 보내야 해. 그런데, 돌상에는 뭘 놓을까?", "Yes, I am a little busy. I have to order the rice cakes and send the invitations, too. By the way, what shall I put on the first birthday table?"),
    ("정우 엄마", "보통 실하고 돈이나 쌀, 연필 같은 것을 놓잖아. 그런데 요즘은 마이크나 골프공도 놔. 윤하 엄마는 윤하가 뭘 잡으면 좋겠어?", "Usually people put things like thread, money or rice, and a pencil, you know. But these days they also put a microphone or a golf ball. What would you like Yunha to grab?"),
    ("윤하 엄마", "음, 연필. 난 윤하가 선생님이 되면 좋겠어.", "Well, the pencil. I would like Yunha to become a teacher."),
]
_A_WORDS = ["공", "돌", "떡", "띠", "마이크", "말", "백일", "뱀", "상", "실", "쌀", "얼마", "연필", "용", "원숭이", "자라다", "잡다", "쥐", "참", "초대장", "칠순", "팔순", "호랑이"]
_JOUR = [
    ("오늘 외할머니의 칠순 잔치에 갔다.", "Today I went to my maternal grandmother’s 70th birthday party."), ("칠순 잔치는 호텔에서 했다.", "The 70th birthday party was held at a hotel."), ("여러 친척 분들과 할머니 친구 분들이 축하해 주러 오셨다.", "Many relatives and my grandmother’s friends came to congratulate her."),
    ("다 같이 외할머니께 생신 축하 노래를 불러 드렸다.", "All together we sang a birthday song for my grandmother."), ("할머니께서 기뻐하셨다.", "My grandmother was pleased."),
]
_JOUR2 = [
    ("오늘 조카 민지의 돌잔치에 갔다.", "Today I went to my niece Minji’s first birthday party."), ("돌잔치는 오빠 집에서 했다.", "The first birthday party was held at my older brother’s house."), ("할아버지와 부모님, 그리고 오빠 친구 분들도 많이 오셨다.", "My grandfather, my parents, and many of my brother’s friends also came."),
    ("다 같이 조카가 돌상에서 마이크를 잡는 것을 보았다.", "All together we watched my niece grab the microphone at the first birthday table."), ("아주 재미있었다.", "It was a lot of fun."),
]
L2 = lesson(
    "Ch 26 · Topic A: It is my daughter’s first birthday (우리 딸 돌이에요)",
    "우리 딸 돌이에요 · 돌잔치 · 돌상 · 돌잡이 · 윤하가 많이 자랐네",
    requires=[],
    cards=[
        card("Topic A: It is my daughter’s first birthday (우리 딸 돌이에요)",
             "Two mothers are talking about the first birthday of one of their daughters, Yunha. (The English is mine; the book gives none. The book writes 2주 as a digit; it is spelled out here. The book’s footnote: 놔 is a short form of 놓아, which comes from 놓다.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=[ktable(_rows(_A_WORDS))]),
        card("More words from the dialog (mine)", "Words the dialog uses that the book does not list (the English is mine).", tables=[ktable([(w, _EXTRA[w]) for w in ["돌잔치", "돌상", "돌잡이", "잔치", "주문하다", "골프공"]])]),
        card("Follow-up 2 (Reading): two journal entries about family occasions",
             "The book asks you to read two journal entries about family occasions attended by Jiho and Hyeyoung and to fill in a table in English (occasion, location of celebration, guests attending, what guests did together). The text is the book’s (the two entries sit side by side in the book); the English is mine.",
             examples=passage([("지호의 일기", "Jiho’s diary")] + _JOUR + [("혜영의 일기", "Hyeyoung’s diary")] + _JOUR2)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["", "Jiho", "Hyeyoung"], [["Occasion", "His maternal grandmother’s 70th birthday party", "Her niece Minji’s first birthday party"], ["Location of celebration", "A hotel", "Her older brother’s house"], ["Guests attending", "Relatives and the grandmother’s friends", "Her grandfather, her parents, and her brother’s friends"], ["What guests did together", "Sang a birthday song to the grandmother", "Watched the niece grab the microphone at the first birthday table"]])]),
        card("Activities left out", "The role-play of the dialog (Yunha’s mom and Jungwoo’s mom) and the SMART Board activity of the Presentation Activity, and Follow-up 1 (listening to three dialogs in which a woman tells a man about preparing for a family occasion) are computer, audio and partner activities. Activity 1 (a SMART Board activity), Activity 2 (listening) and Activity 3 (feedback on an event-planning company’s services, in groups, whose texts are not in the book’s text) are computer, audio and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS]))
        + _tr(_strip(_A_DLG) + _JOUR + _JOUR2)
        + [M("What are the two mothers talking about?", "Yunha’s first birthday", ["A wedding", "A 70th birthday", "A school trip"], "윤하 돌."), M("When is Yunha’s first birthday?", "In two weeks", ["Tomorrow", "Next year", "Last week"], "이 주 후에."), M("What was it a little while ago?", "Yunha’s 100th day", ["Her wedding", "Her 70th birthday", "Her first walk"], "얼마 전에 백일."), M("What zodiac sign is Yunha?", "The rat", ["The dragon", "The tiger", "The horse"], "쥐띠야."),
           M("Where will the party be?", "At home", ["At a hotel", "At a restaurant", "At school"], "집에서 하려고 생각하고 있어."), M("What does Yunha’s mother have to do?", "Order rice cakes and send invitations", ["Cook all the food", "Buy a dress", "Book a hotel"], "떡도 주문하고 초대장도 보내야 해."), M("What do people usually put on the 돌상?", "Thread, money or rice, and a pencil", ["Only fruit", "Only money", "Flowers"], "실하고 돈이나 쌀, 연필."), M("What do people put on it these days besides?", "A microphone or a golf ball", ["A book", "A phone", "A toy car"], "마이크나 골프공도."),
           M("What would Yunha’s mother like Yunha to grab?", "The pencil, so she becomes a teacher", ["The money", "The thread", "The microphone"], "연필. 선생님이 되면 좋겠어."), M("What did Hyeyoung’s niece grab?", "A microphone", ["A pencil", "Money", "Rice"], "돌상에서 마이크를 잡는 것."), M("What did the guests sing at the 70th birthday party?", "A birthday song", ["A wedding song", "A school song", "A carol"], "생신 축하 노래."),
           F("윤하가 많이 ___네! (has grown)", "자랐", ["잡았", "놓았"], "자라다 = to grow up."), F("이 주 후에 윤하 ___이잖아! (the first birthday)", "돌", ["띠", "상"], "돌 = first birthday."), F("돌상에는 뭘 ___까? (put)", "놓을", ["잡을", "자랄"], "놓다 = to put."), F("실하고 돈이나 쌀, 연필 같은 것을 놓___. (you know)", "잖아", ["어요", "네"], "-잖아 = you know."),
           read_q("윤하가 많이 자랐네"), read_q("윤하 돌이잖아"), read_q("돌잔치는 어디서 해"), read_q("떡도 주문하고 초대장도 보내야 해"), read_q("윤하가 뭘 잡으면 좋겠어")]
    ),
)

# ================================================================== L3: Topic A activities: the couple article
_NEWS = [
    ("한류스타 소식", "Hallyu star news (the section)"),
    ("톱스타 커플 현빈 마흔 살과 손예진 마흔 살이 지난 삼 월 삼십일 일 서울 광진구 그랜드워커힐 호텔에서 결혼식을 올렸다.", "The top-star couple Hyun Bin (40) and Son Ye-jin (40) held their wedding on March 31 at the Grand Walkerhill Hotel in Gwangjin-gu, Seoul. (the book writes the ages 40 in parentheses)"),
    ("이천이십 년 삼 월 열애를 시작한 후 이 년 만이다.", "It is two years after they started their passionate love in March 2020."),
    ("현빈과 손예진은 이천십팔 년 영화 협상을 찍을 때 처음 연애 중이라는 기사가 나왔었지만 두 사람 모두 이를 부인했었다.", "When Hyun Bin and Son Ye-jin were filming the movie Negotiation in 2018, an article first appeared saying they were dating, but both of them denied it."),
    ("그 후 두 사람은 이천십구 년 드라마 사랑의 불시착에서 남녀 주연으로 다시 만났다.", "After that, the two met again in 2019 as the male and female leads in the drama Crash Landing on You."),
    ("두 사람은 사랑의 불시착이 끝난 후 약 이 년간 사귀어 왔다고 한다.", "They are said to have been going out for about two years after Crash Landing on You ended."),
    ("국내 뿐 아니라 일본, 인도 등 해외에서도 높은 인기를 얻은 사랑의 불시착은 남한 여자 윤세리가 우연한 사고로 북한에 떨어져 북한 장교 리정혁을 만나 서로 사랑하게 되는 이야기이다.", "Crash Landing on You, which gained great popularity not only in Korea but also abroad in Japan, India and elsewhere, is the story of a South Korean woman, Yoon Seri (Son Ye-jin), who falls into North Korea by an accidental accident, meets a North Korean officer, Ri Jeong-hyeok (Hyun Bin), and they fall in love."),
    ("손예진은 현빈과 연애를 시작할 때 나이도 같고 취미도 비슷해서 같이 있으면 편하고 재미있었다고 한다.", "Son Ye-jin is said to have found it comfortable and fun to be with Hyun Bin when they started dating because they were the same age and had similar hobbies."),
    ("운동이 취미인 현빈은 손예진이 골프를 배울 때 골프 연습장에서 직접 가르쳐 주었다.", "Hyun Bin, whose hobby is sports, taught Son Ye-jin himself at the driving range when she was learning golf."),
    ("두 사람은 시간이 날 때면 강원도의 한 골프장에서 골프를 같이 치거나 주로 서로의 집에서 데이트를 했다고 한다.", "When they had time, the two are said to have played golf together at a golf course in Gangwon-do or mostly dated at each other’s homes."),
]
L3 = lesson(
    "Ch 26 · Topic A Activity 2: a news article about a famous couple’s wedding",
    "한류스타 소식 · 열애 · 결혼식을 올렸다 · 연애 중 · 부인하다 · 데이트",
    requires=[],
    cards=[
        card("Activity 2 (Reading): an article about a famous Korean actor and actress couple",
             "The book asks you to read the article (dated March 31, 2022) and answer four questions in English. The text is the book’s (the digits are spelled out; the parentheses with the ages and the characters’ actors and the quotation marks around the titles are left out); the English is mine. The book glosses 열애: passionate love; 부인하다: to deny.",
             examples=passage(_NEWS)),
        card("The answers (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Question", "Answer (mine)"], [["What is this news report about?", "The wedding of the top-star couple Hyun Bin and Son Ye-jin, held on March 31 at a Seoul hotel"], ["What happened in 2018 and 2019 respectively?", "2018: while filming a movie, reports first appeared that they were dating, and both denied it. 2019: they met again as the male and female leads in a drama"], ["What do the couple have in common?", "They are the same age and have similar hobbies"], ["What did they usually do when dating?", "Played golf together at a golf course in Gangwon-do, or dated mostly at each other’s homes"]])]),
        card("Activities left out", "Activity 3 (배우자를 찾아 드립니다, a matchmaking game in groups, reading three female and three male profiles with pictures) and the rest of the Topic A activities are group and picture activities."),
    ],
    exercises=uniq(
        _tr(_NEWS)
        + [M("When did the couple hold their wedding?", "On March 31", ["On March 1", "In 2018", "In March 2020"], "지난 삼 월 삼십일 일."), M("Where was the wedding?", "At a hotel in Seoul", ["At a church", "In Gangwon-do", "At the actor’s house"], "서울 광진구 그랜드워커힐 호텔."), M("How long after starting their love was the wedding?", "Two years", ["Ten years", "One year", "Six months"], "이 년 만이다."),
           M("What did the couple do about the 2018 article?", "Both denied it", ["Both confirmed it", "Only one denied it", "They ignored it"], "두 사람 모두 이를 부인했었다."), M("In what did they meet again in 2019?", "A drama, as the male and female leads", ["A movie", "A concert", "A talk show"], "드라마 사랑의 불시착."), M("Where did Hyun Bin teach Son Ye-jin golf?", "At a golf driving range", ["At home", "At a hotel", "In Gangwon-do only"], "골프 연습장에서 직접."),
           M("What do the two have in common?", "The same age and similar hobbies", ["The same job only", "The same hometown", "The same school"], "나이도 같고 취미도 비슷해서."), M("What did they usually do when dating?", "Played golf or dated at each other’s homes", ["Went to the movies", "Went abroad", "Shopped"], "골프를 같이 치거나 주로 서로의 집에서 데이트."),
           F("두 사람은 이천이십 년 삼 월 ___를 시작했다. (passionate love)", "열애", ["약혼", "재혼"], "열애 = passionate love."), F("두 사람 모두 이를 ___했었다. (denied)", "부인", ["참석", "약혼"], "부인하다 = to deny."), F("현빈은 손예진이 골프를 ___ 때 가르쳐 주었다. (learned)", "배울", ["가르칠", "칠"], "배우다 = to learn."),
           read_q("결혼식을 올렸다"), read_q("열애를 시작한 후 이 년 만이다"), read_q("서로 사랑하게 되는 이야기이다"), read_q("취미도 비슷해서 같이 있으면 편하고 재미있었다"), read_q("서로의 집에서 데이트를 했다")]
    ),
)

# ================================================================== L4: Topic B
_B_DLG = [
    ("피에르", "선생님, 저 내일 소개팅해요.", "Teacher, I have a blind date tomorrow."),
    ("백 선생님", "아, 그래요? 어떤 여자예요?", "Oh, really? What kind of woman is she?"),
    ("피에르", "나이는 스물세 살이고, 미술학원 강사예요. 지금 프랑스 유학 준비 중이라고 해요.", "She is 23 years old and an instructor at an art institute. They say she is now preparing to study in France."),
    ("백 선생님", "그렇군요. 피에르 씨의 이상형은 어떤 사람이에요?", "I see. What kind of person is your ideal type, Pierre?"),
    ("피에르", "저는 똑똑하고 활달한 여자가 좋아요.", "I like a clever and outgoing woman."),
    ("백 선생님", "피에르 씨는 중매결혼 하고 싶어요? 연애결혼 하고 싶어요?", "Do you want an arranged marriage? Or do you want a love marriage?"),
    ("피에르", "저는 연애결혼 하고 싶어요. 그런데, 한국에서는 아직도 중매결혼을 많이 하지요?", "I want a love marriage. But in Korea, many people still have arranged marriages, right?"),
    ("백 선생님", "네. 그래서 사람들이 아직도 맞선을 많이 봐요. 옛날엔 가족이나 친척, 친구들이 중매를 섰어요. 그런데 요즘엔 전문적으로 중매를 서는 결혼정보회사들이 많아요.", "Yes. So people still go on a lot of arranged meetings. In the old days, family, relatives and friends acted as go-betweens. But these days there are many marriage agencies that professionally act as matchmakers."),
    ("피에르", "결혼정보회사를 이용하면 원하는 조건의 사람을 더 쉽게 만날 수 있을 것 같아요.", "I think if you use a marriage agency you can meet a person with the conditions you want more easily."),
    ("백 선생님", "내일 만나는 소개팅 상대가 피에르 씨 마음에 들면 좋겠네요.", "I hope the blind date partner you meet tomorrow is to your liking, Pierre."),
    ("피에르", "어떤 사람인지 저도 궁금해 죽겠어요. 내일 옷은 어떻게 입어야 해요?", "I am dying to know what kind of person she is, too. How should I dress tomorrow?"),
    ("백 선생님", "깨끗하고 단정하게 입으세요.", "Dress clean and neat."),
]
_B_WORDS = ["강사", "결혼정보회사", "궁금하다", "단정하다", "똑똑하다", "맞선", "상대 / 상대방", "소개팅 / 미팅", "약혼", "연애", "이상형", "재혼", "전문적", "조건", "중매", "학원", "활달하다"]
_AE = [("애인", "one’s lover; one’s boyfriend/girlfriend; “lover”"), ("애국", "patriotism; love of one’s country"), ("애연가", "a habitual smoker; a chain smoker; “a person who loves smoking”"), ("열애", "passionate love (the book’s gloss in the article; mine here)"), ("모성애", "maternal love (mine)"), ("애사심", "love for one’s company (mine)")]
L4 = lesson(
    "Ch 26 · Topic B: I want to marry for love (연애결혼 하고 싶어요)",
    "연애결혼 하고 싶어요 · 소개팅 · 중매결혼 · 맞선 · 이상형 · 결혼정보회사 · 애 (愛)",
    requires=[],
    cards=[
        card("Topic B: I want to marry for love (연애결혼 하고 싶어요)",
             "Pierre, a French student learning Korean, is talking with his Korean instructor, Mr. Baek, about his upcoming blind date. (The English is mine; the book gives none.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The two grammar items of the dialog, –아/어(서) 죽겠다 and ~ 중이다 / –는 중이다, are in the grammar lessons.", tables=[ktable(_rows(_B_WORDS))]),
        card("Cultural note: 미팅, 소개팅 and 맞선",
             "미팅, 소개팅, and 맞선 commonly relate to an arranged meeting between single men and women. 미팅, borrowed from the English word meeting, roughly translates to “a group blind date.” The 미팅 organizer is usually a senior student in college or a senior employee of a company. 소개팅 is a compound word using 소개 (referral; introduction) and the last syllable of 미팅 (meeting). Both 소개팅 and 맞선 mean a one-on-one blind date. 소개팅 is more casual and for those who want to meet a person for a possible relationship. On the other hand, 맞선 is for those who are more serious and looking specifically for a spouse."),
        card("Sino-Korean in use: 애 (愛)",
             "This Sino-Korean syllable means love or loving, as in 애인 (one’s lover; one’s boyfriend/girlfriend; “lover”), 애국 (patriotism; love of one’s country), and 애연가 (a habitual smoker; a chain smoker; “a person who loves smoking”). The book asks you to find out the meanings of 열애, 모성애 and 애사심; the answers are mine (열애: passionate love, as the book glosses it in an article of this chapter).",
             tables=[ktable(_AE)]),
        card("Activities left out", "The SMART Board activity, the pair repetition and translation of selected sentences (from audio) of the Presentation Activity and Follow-up 1 (listening to three conversations about two people’s marriages and ticking love or arranged marriage) are computer, audio and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if "/" not in w]))
        + _tr(_strip(_B_DLG) + _AE)
        + [M("What is Pierre going to do tomorrow?", "Go on a blind date", ["Take a test", "Get married", "Go to a wedding"], "저 내일 소개팅해요."), M("How old is the woman?", "23", ["20", "25", "30"], "스물세 살."), M("What is the woman’s job?", "An instructor at an art institute", ["A teacher at a school", "A nurse", "A student"], "미술학원 강사."), M("What is she preparing for?", "Studying in France", ["A wedding", "A trip to Korea", "A new job"], "프랑스 유학 준비 중."),
           M("What kind of woman does Pierre like?", "A clever and outgoing one", ["A quiet and shy one", "A rich one", "A tall one"], "똑똑하고 활달한 여자."), M("What type of marriage does Pierre want?", "A love marriage", ["An arranged marriage", "No marriage", "A late marriage"], "연애결혼 하고 싶어요."), M("What did family, relatives and friends do in the old days?", "Acted as go-betweens", ["Paid for the wedding", "Hosted the party", "Chose the date"], "중매를 섰어요."), M("What do the marriage agencies do?", "Professionally matchmake", ["Plan weddings", "Sell wedding dresses", "Rent halls"], "전문적으로 중매를 서는."),
           M("How should Pierre dress tomorrow?", "Clean and neat", ["Casually", "Colorfully", "In a suit and tie only"], "깨끗하고 단정하게."), M("What is the difference between 소개팅 and 맞선?", "소개팅 is casual; 맞선 is for those seeking a spouse", ["소개팅 is for groups; 맞선 is casual", "They are the same", "맞선 is only for students"], "The book’s cultural note."), M("What is a 미팅?", "a group blind date", ["a one-on-one date", "a wedding", "an engagement party"], "미팅 = group blind date."), M("What does 애 (愛) mean?", "love; loving", ["a ceremony", "congratulation", "a wife"], "애인, 애국."),
           F("피에르 씨의 ___은 어떤 사람이에요? (ideal type)", "이상형", ["상대", "조건"], "이상형 = ideal type."), F("저는 ___결혼 하고 싶어요. (love)", "연애", ["중매", "재혼"], "연애결혼."), F("그래서 사람들이 아직도 ___을 많이 봐요. (arranged meetings)", "맞선", ["주례", "사회"], "맞선(을) 보다."), F("어떤 사람인지 저도 궁금해 ___어요. (dying)", "죽겠", ["보겠", "하겠"], "궁금해 죽겠어요."),
           read_q("저 내일 소개팅해요"), read_q("저는 똑똑하고 활달한 여자가 좋아요"), read_q("저는 연애결혼 하고 싶어요"), read_q("결혼정보회사를 이용하면"), read_q("깨끗하고 단정하게 입으세요")]
    ),
)

# ================================================================== L5: Topic B follow-up 2
_QA = [
    ("여자들의 이상형은 보통 어떤 사람이에요?", "What kind of person is the ideal type of women usually? (the title of the question)"),
    ("제가 다음 주에 소개팅이 있어요.", "I have a blind date next week."), ("그런데 여자들은 어떤 남자를 좋아하는지 알고 싶어요.", "But I want to know what kind of man women like."),
    ("여자들의 이상형은 먼저 키가 좀 크고 잘생긴 사람입니다.", "First, women’s ideal type is a somewhat tall and handsome person."), ("또 깨끗하고 단정하면 더 좋습니다.", "Also, it is even better if he is clean and neat."), ("그리고 유머감각이 있어야 합니다.", "And he has to have a sense of humor."),
    ("요즘 말을 잘 못하고 센스 없는 남자는 인기가 없습니다.", "These days, men who cannot talk well and have no sense are not popular."), ("또 서로 취미가 비슷하면 같이 재미있는 시간을 가질 수 있을 거예요.", "Also, if your hobbies are similar, you will be able to have a fun time together."),
    ("마지막으로 성격입니다.", "Lastly, personality."), ("성격이 활발하고 밝고 잘 웃는 남자를 좋아합니다.", "They like men whose personality is outgoing and bright and who smile often."), ("도움이 됐기를 바래요.", "I hope this has been helpful."),
]
_VOC_B2 = [("이상형", "an ideal type"), ("상대", "the other party; a counterpart"), ("결혼정보회사", "a marriage agency"), ("연애결혼", "a love marriage"), ("전문적으로", "professionally; expertly"), ("활달하다", "to be outgoing; to be lively"), ("똑똑하다", "to be clever; to be bright"), ("단정하다", "to be neat"), ("약혼", "an engagement"), ("재혼", "remarriage"), ("조건", "a condition; a requirement"), ("궁금하다", "to be curious; to wonder")]
L5 = lesson(
    "Ch 26 · Topic B, Follow-up 2: a blind date question and the answers",
    "여자들의 이상형 · 소개팅 · 키가 크고 잘생긴 사람 · 유머감각 · 취미가 비슷하면",
    requires=[],
    cards=[
        card("Presentation Activity a: the vocabulary of Topic B",
             "The book asks you to complete a vocabulary table with the appropriate Korean and English words (결혼정보회사, 연애결혼, 이상형, 전문적으로, 활달하다, 맞선 보다, 약혼, 재혼, 상대, 똑똑하다, 궁금하다, 조건, ~ 중이다 and the English of “to be neat”, “instructor”, “matchmaking”). The meanings are the core vocabulary’s.",
             tables=[ktable(_VOC_B2)]),
        card("Follow-up 2 (Reading): a Korean college student asks for advice",
             "A Korean college student is going on a blind date. He decides to ask for some advice via an online community; the book asks you to summarize his question and the answers in a table. The text is the book’s (the answerer’s user name and date are left out); the English is mine.",
             examples=passage(_QA)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["", "Summary (mine)"], [["Question", "He has a blind date next week and wants to know what kind of man women like (their ideal type)"], ["Answers", "A somewhat tall and handsome man; clean and neat; a good sense of humor (men who cannot talk well and have no sense are not popular); similar hobbies; an outgoing, bright personality with a ready smile"]])]),
        card("Activities left out", "The 결혼정보회사 link (Useful Link) is a web resource."),
    ],
    exercises=uniq(
        _tr(_VOC_B2[:8] + _QA)
        + [M("What does the student want to know?", "What kind of man women like", ["How to propose", "Where to go for a date", "How to dress"], "여자들은 어떤 남자를 좋아하는지."), M("When is his blind date?", "Next week", ["Tomorrow", "Today", "Next month"], "다음 주에."), M("What does the answerer say first about women’s ideal type?", "Somewhat tall and handsome", ["Rich", "A good cook", "Quiet"], "키가 좀 크고 잘생긴."), M("What else makes a man better?", "Being clean and neat", ["Being famous", "Being loud", "Being strong"], "깨끗하고 단정하면 더 좋습니다."),
           M("What kind of man is not popular these days?", "One who cannot talk well and has no sense", ["One who is tall", "One who laughs often", "One who is neat"], "말을 잘 못하고 센스 없는 남자는 인기가 없습니다."), M("What does the answerer say about hobbies?", "Similar hobbies give a fun time together", ["Hobbies don’t matter", "Different hobbies are better", "Only sports are good"], "서로 취미가 비슷하면."), M("What personality do women like?", "Outgoing, bright and smiling often", ["Quiet and shy", "Serious", "Short-tempered"], "활발하고 밝고 잘 웃는."),
           F("여자들의 이상형은 키가 좀 크고 ___ 사람입니다. (handsome)", "잘생긴", ["못생긴", "작은"], "잘생기다 = to be handsome."), F("요즘 말을 잘 못하고 센스 없는 남자는 ___가 없습니다. (popularity)", "인기", ["취미", "조건"], "인기가 없다."), F("도움이 됐기를 ___요. (I hope)", "바래", ["바빠", "봐"], "바라다 / 바래요 = hope."),
           read_q("제가 다음 주에 소개팅이 있어요"), read_q("키가 좀 크고 잘생긴 사람입니다"), read_q("유머감각이 있어야 합니다"), read_q("서로 취미가 비슷하면"), read_q("성격이 활발하고 밝고 잘 웃는 남자를 좋아합니다")]
    ),
)

# ================================================================== L6: Grammar A: 중이다
def _jung(v):
    return attr(v)[0] + " 중입니다"


_JU_PAIRS = [("학원에 가고 있습니다.", "학원에 가는 중입니다.", "I am going to the academy.", "go"), ("일본을 방문하고 있습니다.", "일본을 방문하는 중입니다.", "I am visiting Japan.", ""), ("친구를 기다리고 있습니다.", "친구를 기다리는 중입니다.", "I am waiting for a friend.", ""), ("영화를 상영하고 있습니다.", "영화를 상영하는 중입니다.", "A movie is being shown.", ""),
             ("아기를 돌보고 있습니다.", "아기를 돌보는 중입니다.", "I am taking care of a baby.", ""), ("식당에서 회식하고 있습니다.", "식당에서 회식하는 중입니다.", "We are having a company dinner at a restaurant.", ""), ("기숙사 방을 청소하고 있습니다.", "기숙사 방을 청소하는 중입니다.", "I am cleaning the dormitory room.", ""), ("가전제품을 싸게 팔고 있습니다.", "가전제품을 싸게 파는 중입니다.", "Home appliances are being sold cheaply.", "")]
_JU_V = [("가다", "to go"), ("방문하다", "to visit"), ("기다리다", "to wait"), ("상영하다", "to show (a movie)"), ("돌보다", "to take care of"), ("청소하다", "to clean"), ("팔다", "to sell"), ("만들다", "to make"), ("먹다", "to eat"), ("읽다", "to read"), ("살다", "to live")]
_JU_N = [("식사", "a meal"), ("공사", "construction"), ("통화", "a phone conversation"), ("회의", "a meeting"), ("휴가", "a vacation"), ("준비", "preparation")]
_JU_EX = [("아침식사를 하는 중입니다.", "I am in the middle of having breakfast, or I am having breakfast."), ("은행에 가는 중입니다.", "I am in the middle of going to the bank, or I am going to the bank."), ("식사 중입니다.", "I am in the middle of a meal, or I am having a meal."), ("이 도로가 공사 중입니다.", "This road is in the middle of construction, or this road is under construction."),
          ("추석에 먹을 음식을 만드는 중입니다.", "We are making food to eat on Chuseok."), ("집을 사기 위해서 저축하는 중입니다.", "I am saving money in order to buy a house."), ("사장님은 통화 중이십니다.", "The president (of the company) is in the middle of a phone conversation, or on the phone."), ("지금 회의 중입니다.", "We are in the middle of a meeting, or in a conference."),
          ("김 선생님은 지금 휴가 중입니다.", "Mr. Kim is on vacation now. (the core vocabulary’s example)")]
_JU_MODEL = [("돈이 없어서 점심을 못 먹었어요. 배고파 죽겠어요. 지금 점심 좀 사 주세요.", "I had no money, so I couldn’t eat lunch. I’m starving to death. Please buy me lunch now. (A, the annoying friend)"), ("어, 제가 지금 병원에 가는 중이에요. 그래서 안 돼요. 미안해요.", "Oh, I am on my way to the hospital now. So I can’t. I’m sorry. (B, the excuse)")]
L6 = lesson(
    "Ch 26 · Grammar A: expressing progressive action with -는 중이다 / ~중이다",
    "아침식사를 하는 중입니다 · 식사 중입니다 · 공사 중입니다 · 통화 중이십니다 · 회의 중입니다",
    requires=[],
    cards=[
        card("A. Expressing progressive action with 중이다",
             "Recall the auxiliary verb –고 있다, which is used to express a progressive (or continuing) action, as in 아침 식사를 하고 있어요 (I am having breakfast) and 은행에 가고 있어요 (I am going to the bank). We can also express a progressive action by using –는 중이다, which literally translates as to be in the middle of. 중이다 can also be preceded by a noun.\n\nExpressing progressive action: action verb stem + 는 중이다; noun + 중이다.",
             examples=passage(_JU_EX[:4])),
        card("More examples", "In the book’s examples (the English is the book’s):", examples=passage(_JU_EX[4:])),
        card("Forms (mine)",
             "The forms are made by the book’s rule: the present attributive form -는 of the action verb (ㄹ stems drop the ㄹ: 팔다 → 파는, 만들다 → 만드는) plus 중이다; a noun takes 중이다 directly.",
             tables=[table(["Verb", "Meaning", "-는 중입니다"], [[v, m, _jung(v)] for v, m in _JU_V], say=[0, 2]), table(["Noun", "Meaning", "Noun + 중입니다"], [[n, m, n + " 중입니다"] for n, m in _JU_N], say=[0, 2])]),
        card("Follow-up 1 (Writing): -고 있다 → -는 중이다",
             "The book asks you to change the –고 있다 sentences into the –는 중이다 or ~ 중이다 form; the first one has been done. The second column is my answer key (the English is mine).",
             tables=[table(["-고 있다", "-는 중이다", "Meaning"], [[a, b, c] for a, b, c, _ in _JU_PAIRS], say=[0, 1])]),
        card("Follow-up 5: the excuse model",
             "You have an annoying acquaintance you want to avoid. When he calls, you make excuses with –는 중이다 or ~ 중이다. The book’s model (the English is mine):",
             examples=passage(_JU_MODEL)),
        card("Activities left out", "The pair reading of Follow-up 1 (b), Follow-up 2 (listening to four short exchanges and translating the sentences with a progressive action) and Follow-up 5 (the situation-card role-play, in class) are audio, partner and class activities."),
    ],
    exercises=uniq(
        _fk(_JU_V, _jung, "-는 중입니다", lambda v: [stem(v) + "고 있습니다", stem(v) + "는 겁니다", stem(v) + "(으)ㄴ 중입니다" if False else stem(v) + "을 중입니다", attr(v)[1] + " 중입니다"])
        + _fk(_JU_N, lambda n: n + " 중입니다", "noun + 중입니다", lambda n: [n + "는 중입니다", n + "이 중입니다", n + "하는 중입니다", n + " 있습니다"])
        + [M(f"Change into -는 중이다: {a}", b, [x[1] for x in _JU_PAIRS if x[1] != b][:3], f"{a} → {b}") for a, b, c, _ in _JU_PAIRS]
        + _tr(_JU_EX + _JU_MODEL)
        + [M("What does 중이다 literally mean?", "to be in the middle of", ["to be about to", "to be finished", "to want to"], "중 = the middle."), M("What does 은행에 가는 중입니다 mean?", "I am on my way to the bank", ["I went to the bank", "I will go to the bank", "I never go to the bank"], "가는 중."), M("What can precede 중이다 besides an action verb?", "A noun", ["An adjective", "A particle", "A number"], "식사 중입니다."), M("What does 이 도로가 공사 중입니다 mean?", "This road is under construction", ["This road is finished", "This road is long", "This road is closed forever"], "공사 중."),
           F("학원에 ___ 중입니다. (going)", "가는", ["간", "갈"], "가는 중입니다."), F("친구를 ___ 중입니다. (waiting)", "기다리는", ["기다린", "기다릴"], "기다리는 중입니다."), F("가전제품을 싸게 ___ 중입니다. (selling)", "파는", ["팔는", "판"], "팔다 → 파는."), F("사장님은 통화 ___이십니다. (in the middle of)", "중", ["때", "후"], "통화 중."), F("지금 회의 ___입니다. (in the middle of)", "중", ["전", "후"], "회의 중."),
           read_q("학원에 가는 중입니다"), read_q("식사 중입니다"), read_q("이 도로가 공사 중입니다"), read_q("사장님은 통화 중이십니다"), read_q("지금 병원에 가는 중이에요")]
    ),
)

# ================================================================== L7: Grammar B: -아/어(서) 죽겠다
_JUG_OV = {"배부르다": "배불러"}


def _jug(v):
    return _JUG_OV.get(v, _base_ao(v)) + " 죽겠어요"


def _jugs(v):
    return _JUG_OV.get(v, _base_ao(v)) + "서 죽겠어요"


_JUG_V = [("피곤하다", "to be tired"), ("배고프다", "to be hungry"), ("행복하다", "to be happy"), ("졸리다", "to be sleepy"), ("춥다", "to be cold"), ("덥다", "to be hot"), ("좋다", "to be good"), ("바쁘다", "to be busy"), ("아프다", "to be sick; to hurt"), ("궁금하다", "to be curious"), ("기쁘다", "to be glad"), ("힘들다", "to be hard; to be tired"), ("배부르다", "to be full (from eating)")]
_JUG_EX = [("피곤해 죽겠어요.", "I am extremely tired."), ("배 고파 죽겠어요.", "I am really hungry."), ("행복해 죽겠어요.", "I am extremely happy."), ("오늘 기분이 좋아서 죽겠어요.", "Today I feel extremely happy."), ("어제 잠을 못 자서 졸려 죽겠어요.", "I didn’t sleep well last night and so I’m “dead sleepy.”"), ("요즘 피곤해서 죽겠어요.", "These days, I feel dead tired."), ("점심을 안 먹어서 배고파 죽겠어요.", "I’m starving to death because I didn’t have lunch."), ("일이 너무 많아서 힘들어 죽겠어요.", "I have too much work, so I’m dead tired. (the core vocabulary’s example)")]
_JUG_C = [("어젯밤에 잠을 못 자서", "졸려 죽겠어요", "I couldn’t sleep last night, so I am dead sleepy."), ("졸업이 가까워서", "바빠 죽겠어요", "Graduation is near, so I am dead busy."), ("코트를 안 입어서", "추워 죽겠어요", "I didn’t wear a coat, so I am freezing to death."), ("컴퓨터 게임을 많이 해서", "눈이 아파 죽겠어요", "I played a lot of computer games, so my eyes hurt like crazy."), ("점심을 너무 많이 먹어서", "배불러 죽겠어요", "I ate too much lunch, so I am stuffed to death."), ("생일 선물을 많이 받아서", "기분이 좋아 죽겠어요", "I received many birthday presents, so I am extremely happy.")]
L7 = lesson(
    "Ch 26 · Grammar B: expressing strong feelings about a condition with -아/어(서) 죽겠다",
    "피곤해 죽겠어요 · 배고파 죽겠어요 · 행복해 죽겠어요 · 졸려 죽겠어요 · 추워 죽겠어요",
    requires=[],
    cards=[
        card("B. Expressing strong feelings about a condition, using -아/어(서) 죽겠다",
             "Koreans often use –아/어(서) 죽겠다 to exaggerate their feelings about a certain condition they are in, as in 피곤해서 죽겠어요 (I am extremely tired), 배 고파서 죽겠어요 (I am really hungry), and 행복해서 죽겠어요 (I am extremely happy). –아/어(서) 죽겠다 literally means “and thus I will die” or “so I will die,” and it is somewhat similar to an English speaker saying, “I am freezing to death.” We can translate the phrase as extremely, really, truly, to death, etc., depending on the context. Note that 서 in –아/어서 죽겠다 can be omitted.",
             examples=passage(_JUG_EX[:3])),
        card("Expressing strong feelings about a condition: -아/어(서) 죽겠다", "The book’s examples (the English is the book’s):", examples=passage(_JUG_EX[3:])),
        card("Forms (mine)", "The forms are made by the book’s rule: the -아/어 form of the stative verb plus 죽겠어요 (with or without 서); the ㅂ irregular verbs change as usual (춥다 → 추워).",
             tables=[table(["Verb", "Meaning", "-아/어 죽겠어요", "-아/어서 죽겠어요"], [[v, m, _jug(v), _jugs(v)] for v, m in _JUG_V], say=[0, 2, 3])]),
        card("Follow-up 3 (Reading and Speaking): connect the reasons and the feelings",
             "The book asks you to connect the phrases that state how a person feels and the reason for the feeling (the answers may vary). The reason phrases are the book’s; the feelings I match are my answer key.",
             tables=[table(["Reason", "Feeling (with 죽겠다)", "Meaning"], [[a, b, c] for a, b, c in _JUG_C], say=[0, 1])]),
        card("Activities left out", "Follow-up 3 (b) (a partner activity in which two sentences are combined and the second changed with –아/어(서) 죽겠다) and Follow-up 4 (listening to four short exchanges and noting the exaggerated feeling and its reason) are partner and audio activities."),
    ],
    exercises=uniq(
        _fk(_JUG_V, _jug, "-아/어 죽겠어요", lambda v: [_base_ao(v) + " 죽었어요", stem(v) + "어 죽겠어요", stem(v) + "고 있어요", _base_ao(v) + "요"])
        + _fk(_JUG_V, _jugs, "-아/어서 죽겠어요", lambda v: [_jug(v), _base_ao(v) + "서 좋아요", stem(v) + "어서 죽겠어요", stem(v) + "고 죽겠어요"])
        + _tr(_JUG_EX + [(a + " " + b, c) for a, b, c in _JUG_C], k=3)
        + [M("What does -아/어(서) 죽겠다 literally mean?", "“and thus I will die”", ["“I want to die”", "“I am dead”", "“I will rest”"], "죽겠다 = will die."), M("What is -아/어(서) 죽겠다 used for?", "To exaggerate feelings about a condition", ["To make a request", "To give an order", "To ask a question"], "Strong feelings."), M("Can 서 be omitted?", "Yes", ["No", "Only in formal speech", "Only in the past"], "피곤해 죽겠어요."), M("What does 점심을 안 먹어서 배고파 죽겠어요 mean?", "I’m starving to death because I didn’t have lunch", ["I’m full", "I ate lunch", "I will eat lunch"], "배고파 죽겠어요."),
           F("피곤___ 죽겠어요. (extremely tired)", "해", ["해서요", "하게"], "피곤하다 → 피곤해."), F("점심을 안 먹어서 배___ 죽겠어요. (hungry)", "고파", ["고프", "고플"], "배고프다 → 배고파."), F("코트를 안 입어서 ___ 죽겠어요. (cold)", "추워", ["춥어", "추우"], "춥다 → 추워."), F("어제 잠을 못 자서 ___ 죽겠어요. (sleepy)", "졸려", ["졸리", "졸린"], "졸리다 → 졸려."), F("일이 너무 많아서 힘들어 ___요. (to death)", "죽겠어", ["죽었어", "죽어"], "죽겠어요."),
           read_q("피곤해 죽겠어요"), read_q("배고파 죽겠어요"), read_q("행복해 죽겠어요"), read_q("졸려 죽겠어요"), read_q("궁금해 죽겠어요")]
    ),
)

# ================================================================== L8: Topic C
_C_TXT = [
    ("저는 어제 친구 정인이의 결혼식에 갔습니다.", "I went to my friend Jeongin’s wedding yesterday."), ("결혼식은 서울 시내에 있는 행복 예식장에서 있었습니다.", "The wedding was at the Happiness Wedding Hall in downtown Seoul."), ("결혼식이 시작되기 전에 신랑과 신부에게 먼저 축하인사를 했습니다.", "Before the wedding began, I first congratulated the groom and the bride."),
    ("저는 정인이에게 축의금 대신에 미리 준비한 선물을 주었습니다.", "I gave Jeongin a gift that I had prepared in advance instead of congratulatory money."), ("그리고 결혼식에 참석하기 위해 결혼식장에 들어갔습니다.", "Then I went into the wedding hall in order to attend the wedding."), ("신랑의 친구가 결혼식 사회를 보았고 우리 대학교 교수님께서 주례를 하셨습니다.", "The groom’s friend was the master of ceremonies, and our university professor officiated the wedding."),
    ("웨딩드레스를 입은 신부는 정말 아름다웠습니다.", "The bride in the wedding dress was really beautiful."), ("결혼 예물로 신랑과 신부는 서로 반지를 교환했습니다.", "As wedding gifts, the groom and bride exchanged rings with each other."), ("결혼식이 끝난 후에 저는 피로연에 참석해서 식사를 했습니다.", "After the wedding ended, I attended the reception and had a meal."),
    ("정인이는 피로연이 끝나자마자 제주도로 신혼여행을 갈 예정이라고 했습니다.", "Jeongin said that she is going to go on a honeymoon to Jeju Island as soon as the reception is over."),
]
_C_WORDS = ["결혼식", "교수", "미리", "사회", "시집", "신랑", "신부", "신혼", "예물", "예식장", "웨딩드레스", "일시", "장가", "장소", "주례", "참석", "청첩장", "축의금", "피로연", "행복"]
_INV = [("저희 두 사람이 이제 하나가 됩니다.", "The two of us now become one."), ("오셔서 축하해 주시면 감사하겠습니다.", "We would be grateful if you came and congratulated us."), ("강상영 윤진서의 장남 현수", "Hyeonsu, the oldest son of Kang Sangyeong and Yun Jinseo (the book separates the parents’ names with a dot)"), ("서진수 민주희의 막내 정인", "Jeongin, the youngest child of Seo Jinsu and Min Juhui"),
        ("일시 삼 월 십육 일 토요일 오후 한 시", "Date and time: Saturday, March 16, 1 p.m."), ("장소 행복 예식장 이 층", "Place: Happiness Wedding Hall, 2nd floor"), ("피로연 초원 회관", "Reception: Chowon Hall")]
_SIK = [("결혼식", "a wedding (ceremony); “marriage ceremony”"), ("입학식", "an entrance ceremony; “school entering ceremony”"), ("한국식", "Korean style; Korean way"), ("서양식", "Western style"), ("자동식", "automatic (style); “self-moving style”"), ("졸업식", "a graduation ceremony (mine)"), ("약혼식", "an engagement ceremony (mine)"), ("수동식", "manual style; hand-operated (mine)")]
_CHUK = [("축가", "a song of congratulation; a carol"), ("축배", "a toast; a celebratory drink; “celebration bowl”"), ("축복", "blessing; benediction; “wishing [for] fortune”"), ("축의금", "congratulatory money"), ("축일", "a festival (day); a national holiday; “celebration day”"), ("축하", "a celebration; congratulations")]
L8 = lesson(
    "Ch 26 · Topic C: I went to my friend’s wedding ceremony yesterday",
    "어제 친구 결혼식에 갔습니다 · 신랑 · 신부 · 주례 · 사회 · 피로연 · 축의금 대신에 · 청첩장 · 축 (祝) · 식 (式)",
    requires=[],
    cards=[
        card("Topic C: I went to my friend’s wedding ceremony yesterday (어제 친구 결혼식에 갔습니다)",
             "A woman is talking about a wedding ceremony she attended. (The English is mine; the book gives none.)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The grammar items of this text, –(으)ㄴ/는 대신(에) / ~ 대신(에) and –(으)ㄹ 계획/생각/예정이다, are in the grammar lessons.", tables=[ktable(_rows(_C_WORDS))]),
        card("The wedding invitation (청첩장)", "The book’s picture of a wedding invitation (the digits are spelled out; the English is mine).", examples=passage(_INV)),
        card("Cultural note: 혼수 (婚需)",
             "The Korean word 혼수 (婚需) means items needed for marriage. This refers to items essential to a marriage ceremony or to marriage expenses. Customarily in the past the bride’s side of family bought everything from large furniture items to kitchenware. On the other hand, the groom’s family traditionally bought or put down a large deposit (전세) to rent a house in which the couple would live after their wedding. However, with the cost of housing expense soaring in Korea recently, more and more couples are focusing their resources on meeting their housing needs together rather than sticking to traditional arrangements of women spending money on 혼수 while men take care of their housing."),
        card("Sino-Korean in use: 축 (祝) and 식 (式)",
             "축 (祝) means congratulation, celebration, or wishing. 식 (式) means ceremony, style, or way. The book asks you to guess the meanings of 졸업식, 약혼식 and 수동식; the answers are mine.",
             tables=[ktable(_CHUK), ktable(_SIK)]),
        card("Activities left out", "The SMART Board activity, Follow-up 2 (listening to two conversations about a wedding ceremony and noting the wedding location, the officiator and the reception location), the Useful Links (예식장, 전통혼례 동영상) and Activity 1’s listening and SMART Board activities are computer and audio activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_C_WORDS))
        + _tr(_C_TXT + _INV + _CHUK + _SIK, k=3)
        + [M("Where did the wedding take place?", "At the Happiness Wedding Hall in downtown Seoul", ["At a church", "At a hotel", "At the bride’s house"], "서울 시내에 있는 행복 예식장."), M("What did the woman give instead of congratulatory money?", "A gift prepared in advance", ["Cash", "Flowers", "A song"], "축의금 대신에 미리 준비한 선물."), M("Who was the master of ceremonies?", "The groom’s friend", ["The professor", "The bride’s father", "The bride"], "신랑의 친구가 결혼식 사회."), M("Who officiated?", "A professor of their university", ["The groom’s father", "A priest", "A friend"], "교수님께서 주례."),
           M("What did the groom and bride exchange?", "Rings", ["Letters", "Watches", "Flowers"], "서로 반지를 교환."), M("What did the woman do after the ceremony?", "Attended the reception and had a meal", ["Went home", "Went on a honeymoon", "Gave a speech"], "피로연에 참석해서 식사."), M("Where will Jeongin go on her honeymoon?", "Jeju Island", ["Hawaii", "Busan", "Europe"], "제주도로 신혼여행."),
           M("What does 혼수 refer to?", "items needed for marriage", ["a wedding dress", "a wedding hall", "a gift of money"], "婚需."), M("What did the bride’s side traditionally buy?", "Furniture and kitchenware", ["A house", "The wedding hall", "The rings"], "large furniture items to kitchenware."), M("What did the groom’s family traditionally provide?", "A house or a large deposit to rent one", ["The kitchenware", "The wedding dress", "The invitations"], "전세."),
           M("What does 축 (祝) mean?", "congratulation; celebration", ["a ceremony", "love", "a wife"], "축하, 축가."), M("What does 식 (式) mean?", "a ceremony; a style; a way", ["congratulation", "love", "a home"], "결혼식, 한국식."), M("What does 졸업식 mean?", "a graduation ceremony", ["an entrance ceremony", "an engagement ceremony", "a wedding"], "졸업 + 식."),
           F("결혼식에 ___하기 위해 결혼식장에 들어갔습니다. (attend)", "참석", ["입장", "준비"], "참석하다 = to attend."), F("저는 축의금 ___에 선물을 주었습니다. (instead of)", "대신", ["때문", "처럼"], "대신에 = instead of."), F("결혼식이 끝난 후에 저는 ___에 참석했습니다. (the reception)", "피로연", ["예식장", "청첩장"], "피로연 = reception."), F("신랑의 친구가 결혼식 ___를 보았습니다. (master of ceremonies)", "사회", ["주례", "예물"], "사회(를) 보다."),
           read_q("결혼식에 갔습니다"), read_q("축의금 대신에 미리 준비한 선물을 주었습니다"), read_q("우리 대학교 교수님께서 주례를 하셨습니다"), read_q("신랑과 신부는 서로 반지를 교환했습니다"), read_q("신혼여행을 갈 예정이라고 했습니다")]
    ),
)

# ================================================================== L9: Topic C follow-ups and activities
_INV2 = [("저희 두 사람이 새 출발의 첫 걸음을 내딛습니다.", "The two of us take the first step of a new start."), ("오셔서 축하해주세요.", "Please come and congratulate us."), ("정영식 박지예의 차남 민수", "Minsu, the second son of Jeong Yeongsik and Park Jiye"), ("조상진 윤연희의 장녀 예슬", "Yeseul, the oldest daughter of Jo Sangjin and Yun Yeonhui"),
         ("일시 팔 월 삼십일 일 일요일 오전 열 시 삼십 분", "Date and time: Sunday, August 31, 10:30 a.m."), ("장소 신라 호텔 삼 층 행복 홀", "Place: Silla Hotel, 3rd floor, Happiness Hall"), ("피로연 신라 회관 신라 호텔 육 층", "Reception: Silla Hall (6th floor of the Silla Hotel)")]
_PLAN = [("이 주 전에 지환 씨와 영미 씨는 약혼했습니다.", "Two weeks ago, Jihwan and Yeongmi got engaged."), ("두 사람은 한 달 후에 결혼할 계획입니다.", "The two plan to marry in a month."), ("그래서 두 사람은 결혼식 준비 때문에 요즘 아주 바쁩니다.", "So the two are very busy these days because of the wedding preparations."),
         ("지난주에는 예식장을 예약하고 백화점에 가서 결혼 예물을 샀습니다.", "Last week they reserved the wedding hall and went to a department store and bought the wedding gifts."), ("이번 주말에는 신혼여행 비행기표를 사고 호텔을 예약할 생각입니다.", "This weekend they intend to buy the honeymoon plane tickets and reserve a hotel."),
         ("지환 씨와 영미 씨는 칠 박 팔 일로 하와이에 신혼여행을 가기로 했습니다.", "Jihwan and Yeongmi have decided to go on a honeymoon to Hawaii for seven nights and eight days."), ("다음 주말에는 청첩장을 만들고 영미 씨 웨딩드레스와 지환 씨 양복을 고를 예정입니다.", "Next weekend they are going to make the wedding invitations and choose Yeongmi’s wedding dress and Jihwan’s suit."),
         ("지환 씨와 영미 씨는 결혼준비로 바쁘지만 다가올 결혼식 때문에 너무 행복합니다.", "Jihwan and Yeongmi are busy with the wedding preparations, but they are very happy because of the coming wedding.")]
_GIFT = [("결혼식 비용과 피로연 음식 값이 오르면서 축의금도 오르고 있는 것으로 나타났다.", "It has been found that as wedding costs and the price of reception food rise, congratulatory money is also rising."), ("조사결과 한국인들이 내는 결혼식 축의금의 평균은 칠만 구천 원인 것으로 조사됐다.", "The survey found that the average congratulatory money Koreans give for a wedding is 79,000 won."),
         ("이는 코로나 유행 전 이천십구 년 평균 칠만 칠천 원에서 이천 원이 늘어난 금액이다.", "This is an amount that has increased by 2,000 won from the average of 77,000 won in 2019, before the spread of COVID."), ("결혼정보회사 듀오가 지난 이천이십이 년 사 월 미혼남녀 삼백여 명을 대상으로 설문조사한 결과 평균 축의금 액수는 칠만 구천 원인 것으로 나타났다.", "In a survey the marriage agency Duo conducted last April 2022 of about 300 unmarried men and women, the average congratulatory money was found to be 79,000 won."),
         ("그 밖에 오만 원 사십팔 퍼센트가 가장 많았고, 그 다음은 십만 원 사십 퍼센트였다.", "Besides that, 50,000 won (48%) was the most common, followed by 100,000 won (40%)."), ("친한 친구나 가족에게는 이십만 원 이상을 한다고 한 답변도 사 퍼센트였다.", "There was also an answer of 4% that said they give 200,000 won or more to close friends or family."),
         ("결혼식장에 어떤 기분으로 가느냐는 질문에 대해서는 오십오 점 칠 퍼센트가 결혼을 축하하러라고, 이십육 점 칠 퍼센트가 돈을 내러라고, 십칠 점 칠 퍼센트가 반반이라고 답했다.", "To the question of what feeling people go to a wedding hall with, 55.7% answered “to congratulate the marriage,” 26.7% “to pay money,” and 17.7% “half and half.”")]
_INV3 = [("친구들아, 우리 결혼한다.", "Friends, we are getting married."), ("꼭 와서 축하해줘!", "Be sure to come and congratulate us!"), ("이동희 백유진의 장남 철수", "Cheolsu, the oldest son of Lee Donghui and Baek Yujin"), ("백송훈 박선희의 차녀 성희", "Seonghui, the second daughter of Baek Songhun and Park Seonhui"),
         ("이천이십삼 년 유 월 이십칠 일 토요일 오후 네 시", "Saturday, June 27, 2023, 4 p.m."), ("서울호텔 십일 층 그랜드 볼룸", "Seoul Hotel, 11th floor, Grand Ballroom (the book prints 볼륨, a misprint of 볼룸)"), ("피로연 서울 호텔 육 층 한식당", "Reception: Seoul Hotel, 6th floor, Korean restaurant")]
L9 = lesson(
    "Ch 26 · Topic C, Follow-up 1 and Activities 2 to 4: invitations, wedding plans and 축의금",
    "청첩장 · 약혼했습니다 · 예식장을 예약하고 · 결혼 예물을 샀습니다 · 결혼 축의금 · 반반",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): a wedding invitation",
             "Read the following wedding invitation and match the Korean word(s) with the correct English word(s) by drawing lines between them. The text is the book’s (the digits are spelled out; the dots between the parents’ names and the heart marks are left out); the English is mine.",
             examples=passage(_INV2)),
        card("The matches (mine)", "The book leaves the matches to be drawn; these are my answers.",
             tables=[table(["Korean", "English"], [["정민수", "bridegroom"], ["신라 회관", "reception location"], ["신라 호텔 행복 홀", "wedding location"], ["조예슬", "bride"]], say=[0])]),
        card("Activity 2 (Reading): a young couple’s wedding plans",
             "The text is about a young couple’s wedding plans. The book asks you to identify what the couple has done and what they will do for their wedding and to complete a table in English. The text is the book’s (2주 and 7박8일 are spelled out); the English is mine.",
             examples=passage(_PLAN)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["What has already been done", "What will be done for the wedding"], [["Got engaged two weeks ago; reserved the wedding hall; bought the wedding gifts at a department store", "Buy the honeymoon plane tickets and reserve the hotel (this weekend); make the invitations and choose Yeongmi’s wedding dress and Jihwan’s suit (next weekend); marry in a month; a honeymoon in Hawaii for seven nights and eight days"]])]),
        card("Activity 3 (Reading): a newspaper article on congratulatory money",
             "Read the article and complete three tasks: choose the best title, mark two statements true or false, and write what each category of the pie chart indicates. The text is the book’s (the digits are spelled out; the quotation marks are left out); the English is mine.",
             examples=passage(_GIFT)),
        card("The answers (mine)", "The book leaves the answers blank; these are my answers.",
             tables=[table(["Task", "Answer (mine)"], [["a. The best title", "4. 결혼 축의금 (congratulatory money for a wedding)"], ["b. 1. The average amount increased by 77,000 won compared with 2019", "False: it increased by 2,000 won (from 77,000 won to 79,000 won)"], ["b. 2. Most people give the couple 50,000 won or more", "True: 48% give 50,000 won, 40% give 100,000 won and 4% give 200,000 won or more"], ["c. A. 55.7%", "People who go to a wedding to congratulate the couple"], ["c. B. 26.7%", "People who go to pay (congratulatory) money"], ["c. C. 17.7%", "People who go half to congratulate and half to pay money"]])]),
        card("Activity 4 (Reading and Writing): your wedding invitation",
             "Your wedding is in a month. You want to create an invitation for your Korean teachers and friends. Read the invitation and complete the table in English. The text is the book’s (the digits are spelled out; the dots between the parents’ names are left out); the English is mine.",
             examples=passage(_INV3)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["Bride", "Seonghui (the second daughter of Baek Songhun and Park Seonhui)"], ["Bridegroom", "Cheolsu (the oldest son of Lee Donghui and Baek Yujin)"], ["Date / wedding location", "Saturday, June 27, 2023, 4 p.m.; the Grand Ballroom on the 11th floor of the Seoul Hotel"], ["Reception location", "The Korean restaurant on the 6th floor of the Seoul Hotel"]])]),
        card("Activities left out", "Writing your own invitation on a blank form (Activity 4, b and c) is a personal writing and sharing activity."),
    ],
    exercises=uniq(
        _tr(_INV2 + _PLAN + _GIFT + _INV3, k=3)
        + [M("In the first invitation, who is the bridegroom?", "정민수", ["조예슬", "정영식", "박지예"], "정영식·박지예의 차남 민수."), M("In the first invitation, where is the reception?", "Silla Hall (the 6th floor of the hotel)", ["Happiness Hall", "A restaurant", "At the groom’s house"], "신라 회관."), M("What have Jihwan and Yeongmi already done?", "Got engaged and reserved the hall, bought gifts", ["Bought the plane tickets", "Made the invitations", "Chosen the dress"], "약혼했습니다, 예식장을 예약하고 예물을 샀습니다."), M("When do they plan to marry?", "In a month", ["In a week", "Next year", "Tomorrow"], "한 달 후에."),
           M("Where will they go on their honeymoon?", "Hawaii, for seven nights and eight days", ["Jeju Island", "Europe", "Busan"], "칠 박 팔 일로 하와이에."), M("What will they do next weekend?", "Make the invitations and choose the dress and the suit", ["Buy the tickets", "Reserve the hall", "Have the wedding"], "청첩장을 만들고 웨딩드레스와 양복을 고를 예정."), M("What is the best title of the article?", "결혼 축의금", ["예물", "결혼식장", "피로연"], "Congratulatory money."),
           M("What is the average congratulatory money in the survey?", "79,000 won", ["50,000 won", "100,000 won", "200,000 won"], "칠만 구천 원."), M("How much has it increased from 2019?", "2,000 won", ["77,000 won", "79,000 won", "20,000 won"], "이천 원이 늘어난."), M("What is the most common amount?", "50,000 won", ["100,000 won", "200,000 won", "30,000 won"], "오만 원 사십팔 퍼센트가 가장 많았고."),
           M("How many answered that they go to a wedding to congratulate?", "55.7%", ["26.7%", "17.7%", "40%"], "오십오 점 칠 퍼센트."), M("Who is the bridegroom in the last invitation?", "Cheolsu", ["Seonghui", "Donghui", "Songhun"], "이동희·백유진의 장남 철수."), M("Where is the reception in the last invitation?", "The Korean restaurant on the 6th floor", ["The Grand Ballroom", "The 11th floor", "A hotel café"], "육 층 한식당."),
           F("지환 씨와 영미 씨는 이 주 전에 ___했습니다. (got engaged)", "약혼", ["재혼", "이혼"], "약혼하다 = to get engaged."), F("지난주에는 예식장을 ___했습니다. (reserved)", "예약", ["참석", "주문"], "예약하다 = to reserve."), F("두 사람은 한 달 후에 결혼할 ___입니다. (plan)", "계획", ["예물", "행복"], "-(으)ㄹ 계획이다."), F("축의금의 평균은 칠만 구천 원인 것으로 ___됐다. (was investigated)", "조사", ["참석", "약혼"], "조사되다 = to be surveyed."),
           read_q("오셔서 축하해주세요"), read_q("약혼했습니다"), read_q("결혼식 준비 때문에 요즘 아주 바쁩니다"), read_q("신혼여행을 가기로 했습니다"), read_q("우리 결혼한다")]
    ),
)

# ================================================================== L10: Grammar C: plans
def _pl(v):
    return attr(v)[2]


_PLN = [("이번 주말에 등산을 ", "가다", "go hiking this weekend"), ("토요일에 한국 음식을 ", "먹다", "eat Korean food on Saturday"), ("오늘 밤에 한국 영화를 ", "보다", "watch a Korean movie tonight"), ("이 년 후에 한국에 ", "가다", "go to Korea in two years"), ("내년에 ", "결혼하다", "get married next year"), ("오후에 도서관에서 숙제를 ", "하다", "do homework at the library in the afternoon")]
_PL_V = [("가다", "to go"), ("먹다", "to eat"), ("읽다", "to read"), ("결혼하다", "to marry"), ("이사하다", "to move"), ("만들다", "to make"), ("살다", "to live"), ("배우다", "to learn"), ("돕다", "to help")]
_PL_EX = [("내년에 유럽 여행을 갈 계획입니다.", "I plan to go sightseeing in Europe next year."), ("한 달 후에 아파트로 이사할 생각입니다.", "I plan to move to an apartment in a month."), ("다음 달에 결혼할 예정입니다.", "I am going to marry next month."), ("삼 년 후에 미국으로 이민 갈 계획이에요.", "I plan to immigrate to the U.S. in three years."),
          ("다음 달에 결혼할 예정이야.", "I am going to marry next month. (casual)"), ("이번 방학에 책을 많이 읽을 생각이다.", "I intend to read a lot of books during this vacation."), ("제 생일 파티를 호텔에서 할 예정이에요.", "I am going to have my birthday party at a hotel. (the core vocabulary’s example)")]
_PL_M = [("김 일병, 이번 주말에 등산을 갈 계획입니까?", "PFC Kim, do you plan to go hiking this weekend? (A, the book’s model)"), ("네, 등산을 갈 생각입니다.", "Yes, I intend to go hiking. (B)"), ("네, 등산을 갈 예정입니다.", "Yes, I am going to go hiking. (B)"), ("저도 등산을 갈 계획입니다.", "I also plan to go hiking. (A)"), ("네, 저도 등산을 갈 예정입니다.", "Yes, I am also going to go hiking. (A)")]
L10 = lesson(
    "Ch 26 · Grammar C: expressing a future plan with -(으)ㄹ 계획 / 생각 / 예정이다",
    "갈 계획입니다 · 이사할 생각입니다 · 결혼할 예정입니다 · 읽을 생각이다",
    requires=[],
    cards=[
        card("A. Expressing a future plan: -(으)ㄹ 계획 / 생각 / 예정이다",
             "Koreans often express a future plan by using one of the following grammar features: –(으)ㄹ 계획 / 생각 / 예정이다, any of which can be translated as plan to, intend to, or be going to. Note that the future attributive form of a verb –(으)ㄹ precedes 계획 / 생각 / 예정.",
             examples=passage(_PL_EX[:3])),
        card("Expressing future plans: -(으)ㄹ 계획 / 생각 / 예정이다", "The book’s examples (the English is the book’s):", examples=passage(_PL_EX[3:])),
        card("Forms (mine)", "The forms are made by the book’s rule: the future attributive form -(으)ㄹ (ㄹ stems keep ㄹ: 만들다 → 만들, 살다 → 살; the ㅂ irregular 돕다 → 도울) plus 계획 / 생각 / 예정이다. The three are used the same way.",
             tables=[table(["Verb", "Meaning", "-(으)ㄹ 계획입니다", "-(으)ㄹ 생각입니다", "-(으)ㄹ 예정입니다"], [[v, m, ("도울" if v == "돕다" else _pl(v)) + " 계획입니다", ("도울" if v == "돕다" else _pl(v)) + " 생각입니다", ("도울" if v == "돕다" else _pl(v)) + " 예정입니다"] for v, m in _PL_V], say=[0, 2, 3, 4])]),
        card("Follow-up 1 (Speaking): the model", "Partner A asks Partner B a question using a phrase from the list and one of the three expressions; Partner B answers affirmatively; Partner A says she has the same plan. The book’s model (the English is mine):", examples=passage(_PL_M)),
        card("The list (with the plan forms, mine)", "The book’s list of phrases; I add the plan form.",
             tables=[table(["Phrase", "Plan (mine)", "Meaning"], [[a + v, a + _pl(v) + " 계획입니다", "plan to " + m] for a, v, m in _PLN], say=[0, 1])]),
        card("Activities left out", "Follow-up 1’s partner exchange, Follow-up 2 (listening to three conversations and noting the male speaker’s plan) and Follow-up 5 (고향에 갈 예정이에요: writing your plans for a period of time on cards passed around the class) are partner, audio and class activities."),
    ],
    exercises=uniq(
        _fk([(v, m) for v, m in _PL_V if v != "돕다"], lambda v: _pl(v) + " 계획입니다", "-(으)ㄹ 계획입니다", lambda v: [attr(v)[0] + " 계획입니다", attr(v)[1] + " 계획입니다", stem(v) + " 계획입니다", attr(v)[2] + " 예정입니다"])
        + _fk([(v, m) for v, m in _PL_V if v != "돕다"], lambda v: _pl(v) + " 예정입니다", "-(으)ㄹ 예정입니다", lambda v: [attr(v)[0] + " 예정입니다", attr(v)[1] + " 예정입니다", stem(v) + " 예정입니다", attr(v)[2] + " 생각입니다"])
        + _tr(_PL_EX + _PL_M, k=3)
        + [M("What do 계획, 생각 and 예정 express?", "A future plan: plan to, intend to, be going to", ["A past action", "A wish", "An order"], "Future plans."), M("Which form precedes 계획 / 생각 / 예정?", "the future attributive form -(으)ㄹ", ["-는", "-(으)ㄴ", "-고"], "갈 계획."), M("What does 다음 달에 결혼할 예정입니다 mean?", "I am going to marry next month", ["I married last month", "I want to marry", "I never marry"], "결혼할 예정."), M("What does 한 달 후에 아파트로 이사할 생각입니다 mean?", "I plan to move to an apartment in a month", ["I moved a month ago", "I will not move", "I am moving now"], "이사할 생각."),
           F("내년에 유럽 여행을 ___ 계획입니다. (go)", "갈", ["가는", "간"], "가다 → 갈."), F("다음 달에 ___ 예정입니다. (marry)", "결혼할", ["결혼하는", "결혼한"], "결혼하다 → 결혼할."), F("이번 방학에 책을 많이 ___ 생각이다. (read)", "읽을", ["읽는", "읽은"], "읽다 → 읽을."), F("삼 년 후에 미국으로 이민 ___ 계획이에요. (go)", "갈", ["가는", "간"], "이민 가다 → 갈."), F("제 생일 파티를 호텔에서 ___ 예정이에요. (hold)", "할", ["하는", "한"], "하다 → 할."),
           read_q("내년에 유럽 여행을 갈 계획입니다"), read_q("한 달 후에 아파트로 이사할 생각입니다"), read_q("다음 달에 결혼할 예정입니다"), read_q("이번 주말에 등산을 갈 계획입니까"), read_q("저도 등산을 갈 계획입니다")]
    ),
)

# ================================================================== L11: Grammar D: 대신(에)
_DS_N = [("생선 대신에 닭고기를 먹겠습니다.", "I will eat chicken rather than fish."), ("콜라 대신에 물을 마실게요.", "I will drink water instead of Coke."), ("병원에 가는 대신에 약을 사서 먹었습니다.", "I bought and took some medicine instead of going to the doctor’s office."),
         ("저 책 대신에 이 펜을 줄게.", "I will give you this pen for that book."), ("이 컴퓨터는 값이 싼 대신 질이 나쁩니다.", "This computer is cheap, but the quality is bad."), ("이메일 대신 전화로 연락합시다.", "Let’s keep in touch by phone instead of e-mail."),
         ("커피 대신에 차를 마셔보세요.", "Try drinking tea instead of coffee. (the core vocabulary’s example)"), ("시험을 볼 때는 펜 대신에 연필을 사용하세요.", "When you take the test, use a pencil instead of a pen. (the core vocabulary’s example)")]
_DS_V = [("가다", "to go"), ("먹다", "to eat"), ("하다", "to do"), ("읽다", "to read"), ("만나다", "to meet"), ("놀다", "to play"), ("사다", "to buy")]
_DS_NN = [("생선", "닭고기", "fish", "chicken"), ("콜라", "물", "Coke", "water"), ("커피", "차", "coffee", "tea"), ("펜", "연필", "a pen", "a pencil"), ("이메일", "전화", "e-mail", "the phone")]
_DS_FU = [("볼링 대신에 테니스를 쳐요.", "(I) play tennis instead of going bowling. (the book’s model)"), ("전화를 하는 대신에 이메일을 보내요.", "(I) send an e-mail rather than calling. (the book’s model)")]
L11 = lesson(
    "Ch 26 · Grammar D: expressing “instead of” with 대신(에)",
    "생선 대신에 닭고기를 · 가는 대신에 · 값이 싼 대신 · 이메일 대신 전화로",
    requires=[],
    cards=[
        card("B. Expressing “instead of”",
             "In English, when we have two available options and choose one over the other, we use expressions like instead of, rather than, or in place of, as in “I will eat chicken rather than fish.” In Korean, this choice of two options is expressed by using 대신(에). Note that 대신(에) can be preceded by a noun, as in 생선 대신에 (instead of fish), or by a verbal phrase in the attributive form, as in 가는 대신에 (instead of going).",
             examples=passage(_DS_N[:3])),
        card("대신(에) in the sense of “in compensation for”",
             "대신(에) is also used to mean in compensation for or to make up for, as in the following examples:",
             examples=passage(_DS_N[3:6])),
        card("More examples", "From the core vocabulary:", examples=passage(_DS_N[6:])),
        card("Forms (mine)", "The forms are made by the book’s rule: a noun + 대신에, or the present attributive form -는 of an action verb + 대신에 (ㄹ stems drop the ㄹ: 놀다 → 노는).",
             tables=[table(["Verb", "Meaning", "-는 대신에"], [[v, m, attr(v)[0] + " 대신에"] for v, m in _DS_V], say=[0, 2]), table(["Noun A", "Noun B", "A 대신에 B", "Meaning"], [[a, b, a + " 대신에 " + b, f"{c} instead of {d}".replace(c + " instead of " + d, d + " instead of " + c)] for a, b, c, d in _DS_NN], say=[0, 1, 2])]),
        card("Follow-up 3 and 4: the models", "Partner A reads a strip of two phrases; Partner B makes a sentence using 대신(에); Partner A translates it into English. The book’s two models (the English is the book’s):", examples=passage(_DS_FU)),
        card("Follow-up 4: Wonhee’s first change", "In Follow-up 4 you listen to Wonhee’s narrative about how her life has changed and identify four things she now does differently; the book gives the first row: before, she drank coffee; now she drinks water. The other three rows depend on the audio and are left out.",
             tables=[table(["Before", "Now"], [["drinks coffee", "drinks water"]])]),
        card("Activities left out", "Follow-up 3’s strips (a partner activity) and Follow-up 4’s listening are audio and partner activities."),
    ],
    exercises=uniq(
        _fk(_DS_V, lambda v: attr(v)[0] + " 대신에", "-는 대신에", lambda v: [attr(v)[1] + " 대신에", attr(v)[2] + " 대신에", stem(v) + " 대신에", attr(v)[0] + " 때문에"])
        + _tr(_DS_N + _DS_FU, k=3)
        + [M("What does 대신(에) mean?", "instead of; rather than; in place of", ["because of", "after", "together with"], "대신 = instead."), M("What can precede 대신(에)?", "A noun, or a verbal phrase in the attributive form", ["Only a noun", "Only a verb stem", "A number"], "생선 대신에, 가는 대신에."), M("What other meaning does 대신(에) have?", "in compensation for; to make up for", ["in the middle of", "before", "because"], "값이 싼 대신 질이 나쁩니다."), M("What does 값이 싼 대신 질이 나쁩니다 mean?", "It is cheap, but the quality is bad", ["It is expensive and good", "It is cheap and good", "It is not for sale"], "싼 대신 = in compensation."),
           F("생선 ___ 닭고기를 먹겠습니다. (instead of)", "대신에", ["때문에", "처럼"], "대신에 = instead of."), F("병원에 가는 ___ 약을 사서 먹었습니다. (instead of)", "대신에", ["때문에", "후에"], "가는 대신에."), F("이메일 대신 ___로 연락합시다. (by phone)", "전화", ["전자", "편지로"], "이메일 대신 전화로."), F("콜라 대신에 ___을 마실게요. (water)", "물", ["콜라", "쌀"], "콜라 대신에 물."), F("볼링 ___ 테니스를 쳐요. (instead of)", "대신에", ["때문에", "후에"], "볼링 대신에 테니스를."),
           read_q("생선 대신에 닭고기를 먹겠습니다"), read_q("병원에 가는 대신에 약을 사서 먹었습니다"), read_q("이 컴퓨터는 값이 싼 대신 질이 나쁩니다"), read_q("이메일 대신 전화로 연락합시다"), read_q("커피 대신에 차를 마셔보세요")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Animals", _CV_ANI), ("Family occasions", _CV_OCC), ("Marriage-related words", _CV_MAR), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:-1] for r in rows if not any(c in r[0] for c in "~(-")]
L12 = lesson(
    "Ch 26 · Core vocabulary and self-evaluation",
    "주요 단어 · 동물 · 가정행사 · 결혼 관련 단어 · 기타 단어 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. Where the book writes two forms together (for example 상대(방) or 소개팅/미팅), the forms are written with a slash.\n\n"
             "The example sentences with digits are respelled in Hangul (1988년 → 천구백팔십팔 년, 3장 → 세 장). The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and talk about important birthdays like the 1st, 70th, and 80th; identify and talk about events related to courting and a wedding, and one’s ideal type of partner; and offer an invitation to an important family event.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; –는 중이다 / ~ 중이다 (to be in the middle of; to be –ing); –아/어(서) 죽겠다 used to exaggerate feelings about a condition; –(으)ㄴ/는 대신(에) and ~ 대신(에) (instead of; rather than; in place of); –(으)ㄹ 계획/생각/예정이다 (plan to; intend to; be going to); and the Sino-Korean syllables 애 (愛), 축 (祝) and 식 (式)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does -는 중이다 mean?", "to be in the middle of", ["to be about to", "to have finished", "to want to"], "가는 중."), M("What does -아/어(서) 죽겠다 do?", "Exaggerates feelings about a condition", ["Negates a verb", "Asks a question", "Makes a request"], "피곤해 죽겠어요."), M("What does 대신(에) mean?", "instead of; rather than", ["because of", "after", "before"], "생선 대신에 닭고기."), M("What do 계획 / 생각 / 예정 express?", "A plan", ["A past action", "A wish to die", "A comparison"], "갈 계획."),
           M("What is a 청첩장?", "a wedding invitation", ["a wedding gift", "a wedding dress", "a wedding hall"], "청첩장."), M("What is a 신랑?", "a groom", ["a bride", "a go-between", "a guest"], "신랑."), M("What is a 신부?", "a bride", ["a groom", "a priest", "a guest"], "신부."), M("What is a 피로연?", "a wedding reception", ["a wedding ceremony", "an engagement", "a honeymoon"], "피로연."), M("What is a 주례?", "a marriage officiant", ["a master of ceremonies", "a groom’s friend", "a photographer"], "주례."),
           M("What is a 맞선?", "an arranged meeting with a prospective spouse", ["a group date", "a wedding", "a honeymoon"], "맞선 보다."), M("What is 돌?", "the first birthday", ["the 100th day", "the 70th birthday", "the 80th birthday"], "돌."),
           F("김 선생님은 지금 휴가 ___입니다. (in the middle of)", "중", ["전", "후"], "휴가 중."), F("저는 아내와 결혼하기 전에 이 년 동안 ___했습니다. (dated)", "연애", ["재혼", "약혼"], "연애하다 = to date."), F("제 친구는 작년 겨울에 ___했습니다. (got engaged)", "약혼", ["재혼", "이혼"], "약혼하다."),
           read_q("주요 단어"), read_q("결혼식"), read_q("청첩장"), read_q("신랑"), read_q("신부")]
    ),
)

UNIT = unit("Semester 1 · Unit 7 · Chapter 26: Family Events and Marriage (가정행사와 결혼 문화)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])

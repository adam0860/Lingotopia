"""Unit 29: KBC Semester 1, Unit 6, Chapter 22 - Home Life (가정 생활).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 6, Student's Edition (2022).
Audio, video clips, pictures, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 22 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_CHORE = [
    ("걸레질", "(~하다) wiping; cleaning with a cloth (to wipe up; to mop up)", "바닥 청소를 할 때 걸레질도 하세요."),
    ("나누다", "to split; to divvy up; to divide; to share", "음식을 친구들과 나누어 먹으면 더 맛있어요."),
    ("놓다", "to put; to place (something on top of something)", "가방과 옷은 저 소파 위에 놓으세요."),
    ("다림질", "(~하다) ironing (to iron)", "저는 보통 토요일에 다림질을 합니다."),
    ("돌보다", "to look after; to take care of", "아기를 돌보는 일은 쉽지 않아요."),
    ("먼지", "dust", "오랫동안 청소를 안 해서 집안에 먼지가 많아요."),
    ("버리다", "to throw away/out; to discard", "쓰레기를 아무 데나 버리면 안돼요."),
    ("살림", "(~하다) running a household; household goods (to run a household)", "김 선생님은 살림을 잘 해요."),
    ("쓰레기", "trash; waste", "집에서 파티를 해서 음식 쓰레기가 많아요."),
    ("쓸다", "to sweep", "방 청소를 할 때 먼저 방을 쓸고 걸레질을 하세요."),
    ("장(을) 보다", "to go (grocery) shopping; “see a market”", "주중에는 바쁘니까 보통 주말에 장을 보러 갑니다."),
    ("떨다 / 털다", "to brush/shake off (dust, sand, etc.)", "청소할 때 텔레비전 위에 먼지를 떨어 주세요."),
]
_CV_HOME = [
    ("관리비", "(管理費) a management fee", "매달 삼십 일까지 관리비를 꼭 내셔야 합니다."),
    ("관리사무소", "(管理事務所) a management office", "수도나 전기가 고장이 나면 관리사무소에 연락하세요."),
    ("난방", "(煖房) heating; “warm room”", "난방이 잘 안 돼서 방이 추워요."),
    ("문제", "(問題) a problem; an issue; a question; trouble", "보일러에 문제가 있는 것 같아요."),
    ("변기", "(便器) a toilet; “excrement tool”", "이번에 화장실 수리할 때 변기도 새로 바꿀 거에요."),
    ("새다", "to leak", "지붕에서 비가 샙니다."),
    ("수도", "(水道) tap water; water service; “water way”", "이번 달 수도 요금이 많이 나왔어요."),
    ("수리", "(修理) (~하다) repair; remodeling (to repair; to fix)", "집을 샀는데 지붕이 새서 수리해야 했어요."),
    ("전기", "(電氣) electricity", "겨울에는 전기 요금이 많이 나옵니다."),
    ("처리", "(處理) (~하다/되다) handling; management; disposal (to handle; to manage; to dispose of/to be handled; to be managed; to be disposed of)", "이 일을 빨리 처리해 주세요."),
]
_CV_EMO = [
    ("기분", "(氣分) a feeling; mood", "김 선생님은 오늘 기분이 아주 좋습니다."),
    ("기쁘다", "to be happy; to feel happy; to be joyful", "좋은 소식을 들어서 아주 기뻤어요."),
    ("나쁘다", "to be bad", "오늘 아침에 나쁜 소식을 들어서 기분이 안 좋아요."),
    ("불친절", "(不親切) (~하다) unkindness (to be unkind; to be unfriendly)", "옷가게 직원이 불친절해서 옷을 안 샀어요."),
    ("슬프다", "to be sad; to be sorrowful", "친구가 아주 슬픈 이야기를 해 주었어요."),
]
_CV_FIN = [
    ("화(가 나다)", "(火) anger; “fire” (to get angry; to be upset)", "수업 시간에 학생들이 떠들어서 선생님이 화가 많이 났어요."),
    ("물가", "(物價) prices (of commodities); “prices of things”", "멕시코는 미국보다 물가가 싸요."),
    ("~비", "(費) expenses", "자동차가 자꾸 고장 나는데 수리비가 너무 비싸 새 차를 사고 싶어요."),
    ("빚", "a debt", "신용카드로 물건을 많이 사서 카드 빚이 많아요."),
    ("식비", "(食費) food expenses", "채소값과 과일 값이 올라서 식비가 많이 들어요."),
    ("아끼다", "to save; to be sparing; to economize; to cherish", "여름에는 사람들이 물을 많이 쓰니까 물을 아껴 써야 해요."),
    ("월급", "(月給) a salary; a monthly paycheck; a wage; “monthly wage”", "우리는 매달 십오 일에 월급을 받습니다."),
    ("저축 / 저금", "(貯蓄/貯金) (~하다) saving (of money for future use); laying (money) aside; storing up (to save; to set aside)", "해외 여행을 하려고 돈을 저축했습니다. 저는 매달 조금씩 저금합니다."),
    ("절약", "(節約) (~하다) frugality; thrift; saving (to economize)", "지난달 전기요금이 많이 나왔으니까 이번 달에는 절약합시다."),
    ("-거나 / 든지", "or (as conjunctive ending)", "저는 주말에 보통 친구를 만나거나 도서관에 갑니다."),
]
_CV_OTH = [
    ("교육", "(敎育) education", "김 선생님은 아이들 교육을 위해 서울로 이사하려고 해요."),
    ("-기 위해(서)", "in order to; so as to", "운동하기 위해서 체육관에 갑니다."),
    ("~네", "refers to one’s family as in “the Johnsons” or “the Browns”", "우리 옆집엔 영미네가 살고 앞집엔 철수네가 살아요."),
    ("막내", "the youngest child of a family", "정연이네 막내는 이번에 초등학교를 졸업했습니다."),
    ("벗다", "to take off (clothes, shoes, etc.)", "한국에서는 보통 집안에서 신발을 벗습니다."),
    ("서로", "each other; mutually", "서로 도우면 집안일도 힘들지 않아요."),
    ("오락", "(娛樂) entertainment; recreation", "미국에서 인기 있는 티브이 오락 프로그램은 뭐예요?"),
    ("오르다", "to go up; to rise; to climb", "요즘 기름값이 올라서 교통비가 많이 들어요."),
    ("외식", "(外食) eating out; dining out; “outside eating”", "저축하기 위해서 외식을 줄였어요."),
    ("~을/를 위해(서)", "for (the sake of); for (the benefit of)", "부모님을 위해서 선물을 샀습니다."),
    ("이미", "already", "그 영화는 이미 상영이 끝났어요."),
    ("자꾸", "repeatedly; again and again (in an annoying manner)", "싫어하는 사람이 자꾸 전화합니다."),
    ("줄이다", "to reduce; to shorten; to cut down", "앞으로 생활비를 줄여야겠어요."),
    ("-지", "the verb ending in an interrogative clause", "한국이 어디에 있는지 알아요."),
    ("항상", "(恒常) always; all the time", "요리 후에는 항상 창문을 열어 놓으세요."),
    ("혼자(서)", "by oneself; alone", "늦은 밤에 집에 혼자 있으면 무서워요."),
]
_CV_LOAN = [("보일러", "a boiler; a water heater", "보일러가 고장이 났어요.")]
_CV_SINO = [("비", "(費) expenses; expenditure; cost; fee", "식비, 학원비, 병원비, 교통비")]
_ALL = {r[0]: r for r in _CV_CHORE + _CV_HOME + _CV_EMO + _CV_FIN + _CV_OTH + _CV_LOAN + _CV_SINO}
_EXTRA = {"비용": "an expense (the book’s example)", "병원비": "medical expenses; “hospital expense”", "학비": "tuition; “expense for schooling”", "치료비": "money for treatment", "교통비": "transportation expenses (mine)", "회비": "a membership fee; dues (mine)", "학원비": "private-academy fees (mine)", "잡비": "miscellaneous expenses (mine)",
          "양치질": "brushing one’s teeth", "도둑질": "theft", "싸움질": "fighting", "화(가) 나다": "to get angry; to be upset", "기분(이) 나쁘다": "to feel bad; to be in a bad mood (mine)",
          "설거지": "washing dishes (mine)", "빨래": "laundry (mine)", "청소기": "a vacuum cleaner (mine)", "마당": "a yard (mine)", "요리": "cooking (mine)", "장보기": "grocery shopping (mine)", "다리미": "an iron (mine)", "걸레": "a rag; a mop cloth (mine)", "경비원": "a security guard", "똑같이": "equally, evenly",
          "난방비": "heating expenses (mine)", "외식비": "eating-out expenses (mine)", "오락비": "entertainment expenses (mine)", "교육비": "education expenses (mine)", "생활비": "living expenses (mine)", "수리비": "repair costs (mine)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)


def _sub(n):
    return n + ("이" if has_final(n) else "가")


# ================================================================== L1: objectives and the notes of Topic A
_JIL = [("걸레질", "mopping; wiping with a cloth"), ("다림질", "ironing"), ("양치질", "brushing one’s teeth"), ("도둑질", "theft (undesirable)"), ("싸움질", "fighting (undesirable)")]
_NAN = [("나눠서 먹다", "to share food; “divide and eat”"), ("나눠서 마시다", "to share a drink; “divide and drink”"), ("집안일을 나눠서 하다", "to share household chores; “divide and do”")]
_CHORES = [("설거지", "washing dishes"), ("빨래", "laundry"), ("장보기", "grocery shopping"), ("다림질", "ironing"), ("요리", "cooking"), ("마당을 쓸다", "sweeping the yard"), ("청소기로 바닥을 청소하다", "vacuuming the floor"), ("쓰레기를 버리다", "taking out the trash"), ("아기를 돌보다", "taking care of the baby"), ("집안 청소", "cleaning the house")]
L1 = lesson(
    "Ch 22 · What the chapter teaches and the notes: 나눠서 and ~질",
    "가정 생활 · 집안일을 나눠서 하다 · 걸레질 · 다림질 · 양치질",
    requires=[],
    cards=[
        card("What Chapter 22 teaches (가정 생활)",
             "Chapter 22, “Home Life”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: talk about common household chores; report malfunctions and request services for home maintenance; express emotions in a simple way; and express concerns and give suggestions on household expenses.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; -지, the verb ending in an interrogative clause; -기 위해(서) (in order to; so as to); the conjunctive ending -거나/-든지 (or); and the Sino-Korean syllable 비 (費)."),
        card("Note 1: expressing “sharing” using 나눠서",
             "Koreans use 나눠서 + an action verb to express sharing something like food, drink or chores: 나눠서 먹다 (to share food), 나눠서 마시다 (to share a drink) and 집안일을 나눠서 하다 (to share household chores). The expression literally means “divide and eat” (or “drink” or “do”).",
             tables=[table(["Expression", "Meaning"], [list(r) for r in _NAN], say=[0])]),
        card("Note 2: ~질",
             "The suffix ~질 (attached to a noun) indicates a repetitive action, as in 걸레질 (mopping), 다림질 (ironing), 양치질 (brushing one’s teeth), etc. It can also indicate an undesirable or socially unacceptable action done repetitively, as in 도둑질 (theft), 싸움질 (fighting), etc.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _JIL], say=[0])]),
        card("The household chores the book lists (Follow-up 1)",
             "The listening activity (Follow-up 1) names these household chores in English. The Korean is mine, except for the core words (걸레질, 다림질, 쓰레기, 장보기, 돌보다, 쓸다).",
             tables=[ktable(_CHORES)]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1 and 2 (SMART Board activities) and Activity 3 (“Typhoon”, a game which the teacher starts) are picture, computer or game activities."),
    ],
    exercises=uniq(
        _tr(_JIL + _NAN + _CHORES)
        + [M("What does 나눠서 먹다 mean?", "to share food; “divide and eat”", ["to cook food", "to eat alone", "to throw away food"], "나누다 = to divide; to share."), M("What does 집안일을 나눠서 하다 mean?", "to share household chores", ["to avoid chores", "to hire a helper", "to do chores alone"], "집안일 = household chores."), M("What does ~질 indicate?", "A repetitive action", ["A place", "A person", "A past event"], "걸레질, 다림질, 양치질."),
           M("Which word means “mopping”?", "걸레질", ["다림질", "양치질", "도둑질"], "걸레질 = mopping."), M("Which word means “ironing”?", "다림질", ["걸레질", "양치질", "싸움질"], "다림질 = ironing."), M("Which word means “brushing one’s teeth”?", "양치질", ["다림질", "걸레질", "도둑질"], "양치질 = brushing one’s teeth."),
           M("Which word means “theft”?", "도둑질", ["양치질", "다림질", "걸레질"], "도둑질 = theft (undesirable)."), M("Which word means “fighting”?", "싸움질", ["도둑질", "양치질", "걸레질"], "싸움질 = fighting (undesirable)."),
           F("우리는 집안일을 ___ 합니다. (share)", "나눠서", ["나눠도", "나누고"], "나눠서 하다 = to share."), F("음식을 나눠서 ___. (eat)", "먹어요", ["먹었어요", "먹으세요"], "나눠서 먹다 = to share food."), F("바닥 청소를 할 때 ___도 하세요. (mopping)", "걸레질", ["다림질", "양치질"], "걸레질 = mopping."),
           read_q("집안일을 나눠서 합니다"), read_q("걸레질"), read_q("다림질"), read_q("양치질"), read_q("쓰레기를 버리다")]
    ),
)

# ================================================================== L2: Topic A
_A_TEXT = [
    ("우리 가족은 집안일을 나눠서 합니다.", "My family shares the household chores."),
    ("어머니께서는 장보기와 요리 등 부엌 살림을 하십니다.", "My mother does the kitchen housework, such as grocery shopping and cooking."),
    ("그리고 아버지는 항상 설거지를 도와 주십니다.", "And my father always helps with washing the dishes."),
    ("형은 집안의 먼지를 떨고 걸레질을 합니다.", "My older brother dusts the house and mops."),
    ("누나는 보통 빨래를 합니다.", "My older sister usually does the laundry."),
    ("그리고 가끔 빨래한 옷을 다림질합니다.", "And sometimes she irons the clothes she has washed."),
    ("그리고 저는 청소기로 바닥을 청소합니다.", "And I clean the floor with a vacuum cleaner."),
    ("남동생은 쓰레기를 버리고, 여동생은 현관에 벗어 놓은 신발을 정리합니다.", "My younger brother takes out the trash, and my younger sister arranges the shoes that have been taken off at the entrance."),
    ("그리고 할아버지께서는 마당을 쓸고 꽃과 나무에 물을 주십니다.", "And my grandfather sweeps the yard and waters the flowers and trees."),
    ("할머니께서는 막내 동생을 돌봐 주십니다.", "My grandmother looks after my youngest sibling."),
    ("우리 가족은 서로 도우면서 집안일을 합니다.", "My family does the household chores while helping each other."),
]
_A_WORDS = ["걸레질", "나누다", "놓다", "다림질", "돌보다", "막내", "먼지", "버리다", "벗다", "살림", "서로", "쓰레기", "쓸다", "장(을) 보다", "떨다 / 털다", "항상", "혼자(서)"]
_WHO = [("어머니", "장보기와 요리 등 부엌 살림", "grocery shopping and cooking (kitchen housework)"), ("아버지", "설거지를 도와 주십니다", "helps wash the dishes"), ("형", "먼지를 떨고 걸레질", "dusts and mops"), ("누나", "빨래, 다림질", "laundry and ironing"), ("저", "청소기로 바닥 청소", "vacuums the floor"), ("남동생", "쓰레기를 버립니다", "takes out the trash"), ("여동생", "신발을 정리합니다", "arranges the shoes"), ("할아버지", "마당을 쓸고 꽃과 나무에 물을 줍니다", "sweeps the yard and waters the flowers and trees"), ("할머니", "막내 동생을 돌봐 주십니다", "looks after the youngest sibling")]
L2 = lesson(
    "Ch 22 · Topic A: We share the household chores",
    "집안일을 나눠서 해요 · 설거지 · 빨래 · 청소기 · 쓰레기 · 마당",
    requires=[],
    cards=[
        card("Topic A: We share the household chores (집안일을 나눠서 해요)",
             "Jungwoo describes each of his family members’ responsibilities for household chores. (The English is mine; the book gives none.)",
             examples=passage(_A_TEXT)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened. The book shows pictures of the chores.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Who does what (mine)",
             "A summary of the passage (the book has the SMART Board activity of Presentation Activity c for this).",
             tables=[table(["Family member", "Chore", "Meaning"], [list(r) for r in _WHO], say=[0, 1])]),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity and the partner retelling are computer or partner activities. Follow-up 1 (listening to two conversations about family members and their chores, circling the chores mentioned and drawing lines) is an audio activity; Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not any(c in w for c in "~(/")]))
        + _tr(_A_TEXT)
        + [M("Who always helps with washing the dishes?", "The father", ["The mother", "The older brother", "The grandmother"], "아버지는 항상 설거지를 도와 주십니다."), M("What does the mother do?", "Grocery shopping, cooking and other kitchen housework", ["Mopping", "Laundry", "Taking out the trash"], "장보기와 요리 등 부엌 살림."), M("What does the older brother do?", "Dusts and mops", ["Does the laundry", "Vacuums the floor", "Sweeps the yard"], "먼지를 떨고 걸레질."),
           M("What does the older sister sometimes do?", "Irons the washed clothes", ["Washes the dishes", "Mops", "Cooks"], "빨래한 옷을 다림질합니다."), M("What does the speaker do?", "Cleans the floor with a vacuum cleaner", ["Takes out the trash", "Mops", "Irons"], "청소기로 바닥을 청소합니다."), M("Who takes out the trash?", "The younger brother", ["The younger sister", "The father", "The grandfather"], "남동생은 쓰레기를 버리고."),
           M("What does the younger sister do?", "Arranges the shoes at the entrance", ["Takes out the trash", "Waters the trees", "Mops"], "현관에 벗어 놓은 신발을 정리합니다."), M("What does the grandfather do?", "Sweeps the yard and waters the flowers and trees", ["Cooks", "Looks after the baby", "Irons"], "마당을 쓸고 꽃과 나무에 물을 주십니다."), M("Who looks after the youngest sibling?", "The grandmother", ["The mother", "The grandfather", "The older sister"], "할머니께서는 막내 동생을 돌봐 주십니다."),
           F("어머니께서는 장보기와 요리 등 부엌 ___을 하십니다. (housework)", "살림", ["걸레질", "다림질"], "살림 = running a household."), F("형은 집안의 ___를 떨고 걸레질을 합니다. (dust)", "먼지", ["쓰레기", "마당"], "먼지 = dust."), F("남동생은 ___를 버립니다. (trash)", "쓰레기", ["먼지", "신발"], "쓰레기 = trash."),
           F("할머니께서는 막내 동생을 ___ 주십니다. (look after)", "돌봐", ["벗어", "놓아"], "돌보다 + 아 주다."), F("현관에 ___ 놓은 신발을 정리합니다. (taken off)", "벗어", ["돌봐", "버려"], "벗다 = to take off."), F("우리 가족은 ___ 도우면서 집안일을 합니다. (each other)", "서로", ["혼자", "항상"], "서로 = each other."),
           read_q("집안일을 나눠서 합니다"), read_q("장보기와 요리"), read_q("항상 설거지를 도와 주십니다"), read_q("청소기로 바닥을 청소합니다"), read_q("막내 동생을 돌봐 주십니다")]
    ),
)

# ================================================================== L3: Follow-up 2, Activities A
_ART = [("집안일, 누가 더 많이 할까?", "Who does more housework?"), ("한 조사에 따르면 집안일을 여성 혼자 다 하는 가족이 칠십 점 오 퍼센트, 그리고 이십육 점 육 퍼센트의 가족은 여성과 남성이 집안일을 똑같이 나누어서 하는 것으로 나타났다.", "According to one survey, in 70.5% of families a woman does all the housework alone, and in 26.6% of families women and men share the housework equally."), ("나머지 이 점 구 퍼센트는 남편이 집안일을 하는 것으로 조사되었다.", "In the remaining 2.9%, the husband was found to do the housework.")]
_COUNSEL = [
    ("안녕하세요? 저는 김수철이라고 합니다.", "Hello? My name is Kim Suchul."), ("삼 년 전에 결혼했고 두 살 된 아이가 하나 있습니다.", "I got married three years ago and have one child who is two years old."), ("저는 아내하고 사이가 좋은데 가끔 집안일 때문에 싸웁니다.", "I get along well with my wife, but sometimes we fight because of the housework."),
    ("결혼 초에는 제가 자주 집안일을 도와주었습니다.", "At the beginning of our marriage I often helped with the housework."), ("하지만 요즘은 제 회사 일이 너무 바빠서 평일에는 집안일을 도와주지 못합니다.", "But these days my work at the company is too busy, so I cannot help with the housework on weekdays."), ("그래서 주말이나 휴일에만 집안청소를 해줍니다.", "So I do the house cleaning only on weekends or holidays."),
    ("그런데 아내는 제가 평일에도 장보기와 설거지, 아이 돌보는 것을 도와주기를 바랍니다.", "But my wife wants me to help with grocery shopping, washing the dishes and looking after the child on weekdays, too."), ("제가 집안일을 너무 안 도와주고 있나요?", "Am I not helping with the housework too little?"),
]
_ASKMODEL = [("일층은 거실하고 부엌, 욕실, 현관을 청소해 주세요.", "On the first floor, please clean the living room, the kitchen, the bathroom and the entrance. (home owner)"), ("거실은 어떻게 청소할까요?", "How shall I clean the living room? (helper)"), ("청소기로 먼저 청소하고 걸레질을 해 주세요.", "Please clean with the vacuum cleaner first and then mop. (home owner)")]
L3 = lesson(
    "Ch 22 · Topic A, Follow-up 2 and Activities A: housework survey and a husband’s worry",
    "집안일, 누가 더 많이 할까? · 김수철 씨의 고민 · 깨끗이 청소해 주세요",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): who does more housework?",
             "The book gives an article about spouses sharing household chores and asks you to write in English what each percentage (70.5%, 26.6%, 2.9%) refers to. The text is the book’s (the percentages are spelled out in Hangul); the English is mine. The book glosses 똑같이: equally, evenly.",
             examples=passage(_ART)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Percentage", "Reference (mine)"], [["70.5%", "Families in which the woman does all the housework alone"], ["26.6%", "Families in which women and men share the housework equally"], ["2.9%", "Families in which the husband does the housework"]])]),
        card("Activity 2 (Reading): a man’s concerns on an online counseling site",
             "The text is from an online counseling site, in which a man is expressing his concerns about household chores. The book asks you to fill in a table in English (personal information about the man, what his spouse wants, the man’s dilemma). The text is the book’s (3년 → 삼 년); the English is mine.",
             examples=passage(_COUNSEL)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Personal information", "What his spouse wants", "The man’s dilemma"], [["Kim Suchul; married three years ago; one two-year-old child", "She wants him to help with grocery shopping, washing the dishes and looking after the child on weekdays, too", "He gets along well with his wife but sometimes they fight about housework; his job is too busy on weekdays, so he can only clean on weekends and holidays"]])]),
        card("Activity 4: “Please clean thoroughly” (the model)",
             "In the role-play of Activity 4 (깨끗이 청소해 주세요: a home owner who needs to hire a helper for an upcoming family event and a domestic helper), the students first write down the chores in Korean and then use -아/어 주다 for requesting services. The book gives this model (the English is mine):",
             examples=passage(_ASKMODEL)),
        card("Activities left out",
             "Activity 1 (a SMART Board activity and a video clip from MBC America in which a household helper is instructed to do chores; one chore, sterilizing baby bottles, is given) is a computer and video activity. Activity 3 (a family meeting at which Jitae’s parents make suggestions about sharing the chores; two listening tables of suggestions, with “feed the dog” and “clean the veranda” given) is an audio activity. Activity 4’s role-play (with situation cards) is a partner activity."),
    ],
    exercises=uniq(
        _tr(_ART + _COUNSEL + _ASKMODEL)
        + [M("In most families, who does all the housework alone?", "The woman (70.5%)", ["The man (2.9%)", "Both equally (26.6%)", "A helper"], "여성 혼자 다 하는 가족이 칠십 점 오 퍼센트."), M("What does 26.6% refer to?", "Families where women and men share the housework equally", ["Families where the woman does it alone", "Families where the husband does it", "Families with a helper"], "똑같이 나누어서."), M("What does 2.9% refer to?", "Families where the husband does the housework", ["Families where the woman does it", "Families that share it", "Families with a helper"], "나머지 이 점 구 퍼센트는 남편이."),
           M("What does 똑같이 mean?", "equally; evenly", ["alone", "always", "repeatedly"], "똑같이 = equally, evenly."), M("How long ago did Kim Suchul get married?", "Three years ago", ["Two years ago", "Last year", "Ten years ago"], "삼 년 전에 결혼했고."), M("How old is his child?", "Two years old", ["Three years old", "One year old", "Fifteen months old"], "두 살 된 아이."), M("Why does he fight with his wife sometimes?", "Because of the housework", ["Because of money", "Because of the child’s name", "Because of her job"], "집안일 때문에 싸웁니다."),
           M("Why can’t he help on weekdays?", "His work is too busy", ["He is ill", "He dislikes housework", "He lives far away"], "회사 일이 너무 바빠서."), M("When does he clean the house?", "On weekends or holidays", ["Every day", "On weekdays", "Never"], "주말이나 휴일에만 집안청소를 해줍니다."), M("What does his wife want?", "Help with shopping, dishes and the child on weekdays", ["More money", "A new house", "A helper"], "평일에도 장보기와 설거지, 아이 돌보는 것."),
           M("What does the owner ask the helper to do in the living room?", "Vacuum first and then mop", ["Only mop", "Only vacuum", "Iron"], "청소기로 먼저 청소하고 걸레질을 해 주세요."),
           F("저는 아내하고 ___가 좋습니다. (get along)", "사이", ["기분", "살림"], "사이가 좋다 = to get along well."), F("요즘은 제 회사 일이 너무 ___ 평일에는 도와주지 못합니다. (busy)", "바빠서", ["기뻐서", "슬퍼서"], "바쁘다 + 아서."), F("거실은 어떻게 청소___요? (shall I)", "할까", ["하려고", "하는"], "-(으)ㄹ까요? = shall I."),
           read_q("집안일, 누가 더 많이 할까"), read_q("똑같이 나누어서 합니다"), read_q("평일에는 집안일을 도와주지 못합니다"), read_q("깨끗이 청소해 주세요"), read_q("걸레질을 해 주세요")]
    ),
)

# ================================================================== L4: Topic B
_B_DLG = [
    ("소장", "어떻게 오셨습니까?", "How can I help you? (the literal meaning is “How did you come?”)"),
    ("선아", "지난주에 제가 백십일 동 천칠 호로 이사 왔는데 화장실에 좀 문제가 있어요.", "Last week I moved into unit 1007 of building 111, and there is a bit of a problem in the bathroom."),
    ("소장", "무슨 문제입니까?", "What kind of problem is it?"), ("선아", "변기에서 물이 새요.", "Water leaks from the toilet."), ("소장", "아, 그래요?", "Oh, really?"),
    ("선아", "그리고 이미 여러 번 관리사무소에 전화했는데 직원들이 전화를 잘 안 받아요. 전화를 받아도 직원들이 불친절해서 기분이 나빠요.", "And I have already called the management office several times, but the staff don’t often answer the phone. Even when they answer, the staff are unfriendly, so I feel bad."),
    ("소장", "정말 죄송합니다. 다른 문제는 없으십니까?", "I am really sorry. Is there no other problem?"),
    ("선아", "보일러도 고장 난 것 같아요. 어젯밤에 난방이 잘 안 돼서 추웠어요.", "The boiler seems to be broken, too. Last night the heating didn’t work well, so it was cold."),
    ("소장", "알겠습니다. 화장실, 보일러 둘 다 곧 수리해 드리겠습니다.", "I understand. We will repair both the bathroom and the boiler soon."),
    ("선아", "참, 관리비는 언제 나오는지 알고 싶어요.", "Oh, I would like to know when the management fee comes out."),
    ("소장", "관리비는 매달 삼십 일에 나옵니다.", "The management fee comes out on the 30th of every month."),
    ("선아", "관리비에 수도요금하고 전기요금이 포함돼요?", "Are the water bill and the electricity bill included in the management fee?"),
    ("소장", "네, 포함됩니다.", "Yes, they are included."),
    ("선아", "알겠습니다. 그럼, 직원 좀 빨리 보내 주세요.", "I see. Then please send a staff member quickly."),
]
_B_WORDS = ["관리비", "관리사무소", "기분", "기쁘다", "나쁘다", "난방", "문제", "변기", "보일러", "불친절", "새다", "수도", "수리", "슬프다", "이미", "-지", "전기", "처리", "화(가 나다)"]
_EMO = [("화(가) 나다", "to get angry; to be upset"), ("슬프다", "to be sad; to be sorrowful"), ("기쁘다", "to be happy; to be joyful"), ("기분(이) 나쁘다", "to feel bad; to be in a bad mood")]
_MGT = [("관리비", "a management fee"), ("수도요금", "a water bill (mine)"), ("전기요금", "an electricity bill (mine)"), ("가스 요금", "a gas bill (mine)")]
L4 = lesson(
    "Ch 22 · Topic B: The toilet leaks",
    "변기에서 물이 새요 · 관리사무소 · 보일러 · 난방 · 관리비 · 감정",
    requires=[],
    cards=[
        card("Topic B: The toilet leaks (변기에서 물이 새요)",
             "Sunah is complaining to the manager of the apartment management office. (The English is mine; the book gives none. The book writes 111동 1007호 and 30일; they are spelled out here. The book’s footnote says the literal translation of 어떻게 오셨습니까? is “How did you come?”; in conversation it is an opening remark meaning “How can I help you?”)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Emotions (감정)",
             "The book shows four faces with the labels below. The English is the book’s (from the Core Vocabulary), except 기분(이) 나쁘다, which is mine.",
             tables=[ktable(_EMO)]),
        card("Cultural note: the management fee",
             "In Korea, those who live in an apartment complex normally pay 관리비 (a management fee) every month to help maintain the apartment complex. This is similar to association fees for condominiums in the U.S. However, when you receive the bill for 관리비, a statement of each unit’s electricity, gas and water expenses is often included on the bill."),
        card("Activities left out",
             "The SMART Board activity and the group role-play (Group A as Sunah and Group B as the manager, with cue cards) of the Presentation Activity are computer or class activities. Follow-up 1 (listening to three dialogs about a maintenance problem) is an audio activity; Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not any(c in w for c in "~(-/")]))
        + _tr(_strip(_B_DLG) + _EMO + _MGT)
        + [M("What is Sunah’s problem in the bathroom?", "Water leaks from the toilet", ["The shower is broken", "There is no water", "The door is broken"], "변기에서 물이 새요."), M("What is the problem with the management office staff?", "They don’t answer the phone well and are unfriendly", ["They are too slow", "They never come", "They are too loud"], "전화를 잘 안 받아요. 불친절해서."), M("What is wrong with the boiler?", "The heating didn’t work well last night", ["It is too loud", "It leaks", "It is too hot"], "난방이 잘 안 돼서 추웠어요."),
           M("What will the manager do?", "Repair both the bathroom and the boiler soon", ["Move her", "Ignore it", "Charge extra"], "둘 다 곧 수리해 드리겠습니다."), M("When does the management fee come out?", "On the 30th of every month", ["On the 1st", "Every week", "On the 15th"], "매달 삼십 일에 나옵니다."), M("What is included in the management fee?", "The water bill and the electricity bill", ["Only the gas bill", "Rent", "Nothing"], "수도요금하고 전기요금이 포함됩니다."),
           M("What does 어떻게 오셨습니까? mean in conversation?", "How can I help you?", ["How did you come?", "Where are you going?", "Who are you?"], "An opening remark."), M("What does 새다 mean?", "to leak", ["to be new", "to sell", "to sweep"], "물이 새요 = water leaks."), M("Which word means “heating”?", "난방", ["수도", "전기", "변기"], "난방 = heating; “warm room”."),
           F("변기에서 물이 ___. (leaks)", "새요", ["써요", "사요"], "새다 = to leak."), F("직원들이 ___해서 기분이 나빠요. (unfriendly)", "불친절", ["친절", "정확"], "불친절하다 = to be unkind."), F("보일러도 ___ 난 것 같아요. (broken)", "고장", ["수리", "처리"], "고장 나다 = to break down."),
           F("관리비는 언제 나오는___ 알고 싶어요. (when)", "지", ["는", "고"], "-지 in an interrogative clause."), F("화장실, 보일러 둘 다 곧 ___ 드리겠습니다. (repair)", "수리해", ["처리해", "정리해"], "수리하다 = to repair."), F("관리사무소에 ___ 전화했는데. (already, several times)", "이미 여러 번", ["벌써 한 번", "아직 한 번"], "이미 = already."),
           read_q("변기에서 물이 새요"), read_q("관리사무소"), read_q("보일러가 고장 났어요"), read_q("관리비는 매달 삼십 일에 나옵니다"), read_q("기분이 나빠요")]
    ),
)

# ================================================================== L5: Follow-up 2 emails and Activities B
_MAIL1 = [("안녕하세요, 저는 오백구 동 육백삼 호에 살고 있는 사람입니다.", "Hello, I am a person living in unit 603 of building 509."), ("위층에서 저희 집 베란다 창문으로 계속 물을 버립니다.", "The upstairs keeps throwing water out through our veranda window."), ("그래서 아파트 경비 아저씨에게 여러 번 이야기를 했는데 아직까지 처리해 주지 않았습니다.", "So I spoke to the apartment security guard several times, but he has not dealt with it yet."),
          ("그리고, 어젯밤부터 뜨거운 물이 안 나와요.", "And since last night there has been no hot water."), ("이 이메일을 보시고 빨리 직원을 보내주세요.", "Please see this e-mail and send a staff member quickly.")]
_MAIL2 = [("죄송합니다.", "I am sorry."), ("저희가 위층 칠백삼 호에 살고 계시는 분께 이미 이야기했습니다.", "We have already spoken to the person living in unit 703 upstairs."), ("더 이상 위층에서 물을 버리지 않을 겁니다.", "They will not throw water out from upstairs any more."), ("뜨거운 물이 안 나오는 것은 보일러 고장 때문인 것 같습니다.", "The reason that no hot water comes out seems to be that the boiler is broken."),
          ("오늘 오후에 저희 직원을 보내드리겠습니다.", "We will send our staff member this afternoon."), ("감사합니다.", "Thank you.")]
_EMO_MODEL = [("지난 생일 때 선물로 노트북 컴퓨터를 받았어요.", "On my last birthday I received a laptop computer as a present."), ("그래서 아주 기뻤어요.", "So I was very happy.")]
_EMO_SENT = [("좋은 소식을 들어서 아주 기뻤어요.", "I heard good news, so I was very happy."), ("친구가 아주 슬픈 이야기를 해 주었어요.", "A friend told me a very sad story."), ("옷가게 직원이 불친절해서 옷을 안 샀어요.", "The clothing store staff were unfriendly, so I didn’t buy clothes."), ("수업 시간에 학생들이 떠들어서 선생님이 화가 많이 났어요.", "The students were noisy during class, so the teacher got very angry.")]
L5 = lesson(
    "Ch 22 · Topic B, Follow-up 2 and Activities B: e-mails to the management office",
    "어떻게 오셨습니까 · 이메일 · 경비 아저씨 · 뜨거운 물 · 기뻤어요 · 슬퍼요",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): an e-mail exchange between a tenant and the management office",
             "The book gives an e-mail exchange (subject 509동 603호) and asks you to fill in a table in English (the complaint or problem; the management’s response). The texts are the book’s (the unit numbers are spelled out in Hangul; the e-mail addresses are left out); the English is mine. The book glosses 경비(원): security guard. The tenant’s e-mail:",
             examples=passage(_MAIL1)),
        card("The management’s reply",
             "The reply (the English is mine):",
             examples=passage(_MAIL2)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Complaint or problem", "Management’s response"], [["Someone upstairs keeps throwing water out onto the tenant’s veranda window; the security guard has not dealt with it; no hot water since last night", "They have already spoken to the person living upstairs, who will not throw water out any more; the hot water problem seems to be caused by a broken boiler; they will send a staff member this afternoon"]])]),
        card("Activity 2 (Speaking): emotions (the model)",
             "In Activity 2 you think about events that made you sad, happy, angry or frustrated, fill in a table in English and tell your partner in Korean. The book gives this model (the English is mine). The sentences after it are the core vocabulary’s examples for the emotions:",
             examples=passage(_EMO_MODEL + _EMO_SENT)),
        card("Activities left out",
             "Follow-up 1 of Topic B and Activity 1 (a SMART Board activity and listening to three phone conversations in which a woman reports a maintenance problem to the management office) are computer and audio activities. Activity 2’s table and partner exchange and Activity 3 (저희 집 수도가 고장 났어요: a role-play between a new tenant and a management office employee, with situation cards) are partner activities."),
    ],
    exercises=uniq(
        _tr(_MAIL1 + _MAIL2 + _EMO_MODEL + _EMO_SENT)
        + [M("Where does the tenant live?", "Unit 603 of building 509", ["Unit 703 of building 509", "Unit 1007 of building 111", "Unit 603 of building 111"], "오백구 동 육백삼 호."), M("What is the upstairs doing?", "Throwing water out through the tenant’s veranda window", ["Playing loud music", "Smoking", "Dropping trash"], "베란다 창문으로 계속 물을 버립니다."), M("Whom did the tenant speak to several times?", "The apartment security guard", ["The manager", "The upstairs neighbor", "The landlord"], "경비 아저씨에게 여러 번 이야기."),
           M("What other problem is there?", "No hot water since last night", ["No electricity", "The toilet leaks", "No heating"], "어젯밤부터 뜨거운 물이 안 나와요."), M("What did the management say about the upstairs?", "They have already spoken to the person living there", ["They will fine them", "They can do nothing", "They will move them"], "이미 이야기했습니다."), M("What is the reason for the missing hot water?", "A broken boiler, it seems", ["A broken pipe", "A broken toilet", "A power cut"], "보일러 고장 때문인 것 같습니다."), M("When will the staff member come?", "This afternoon", ["Tomorrow", "Tonight", "Next week"], "오늘 오후에."),
           M("What present did the speaker receive on the last birthday?", "A laptop computer", ["A phone", "A bag", "A watch"], "노트북 컴퓨터를 받았어요."), M("How did the speaker feel?", "Very happy", ["Very sad", "Angry", "Tired"], "아주 기뻤어요."), M("Why did the teacher get angry?", "The students were noisy during class", ["The students were late", "The students slept", "The students left"], "학생들이 떠들어서."),
           F("위층에서 계속 물을 ___. (throws away)", "버립니다", ["사랍니다", "놓습니다"], "버리다 = to throw away."), F("뜨거운 물이 안 ___. (comes out)", "나와요", ["가요", "와요"], "물이 나오다 = water comes out."), F("저희 직원을 ___ 드리겠습니다. (will send)", "보내", ["받아", "알려"], "보내다 = to send."),
           F("좋은 소식을 들어서 아주 ___. (was happy)", "기뻤어요", ["슬펐어요", "나빴어요"], "기쁘다 → 기뻤어요."), F("친구가 아주 ___ 이야기를 해 주었어요. (sad)", "슬픈", ["기쁜", "나쁜"], "슬프다 + ㄴ = 슬픈."), F("선생님이 ___가 많이 났어요. (anger)", "화", ["빚", "식비"], "화가 나다 = to get angry."),
           read_q("경비 아저씨"), read_q("뜨거운 물이 안 나와요"), read_q("보일러 고장"), read_q("아주 기뻤어요"), read_q("화가 많이 났어요")]
    ),
)

# ================================================================== L6: Grammar: the -지 interrogative clause
def _ji_pres(verb, stative=False):
    return (attr(verb)[1] if stative else attr(verb)[0]) + "지"


def _ji_past(verb):
    return past(verb) + "는지"


def _ji_fut(verb):
    return attr(verb)[2] + "지"


_JI_A = [("가다", "to go"), ("먹다", "to eat"), ("오다", "to come"), ("읽다", "to read"), ("시작하다", "to start"), ("배우다", "to learn"), ("만나다", "to meet"), ("사다", "to buy")]
_JI_S = [("크다", "to be big"), ("작다", "to be small"), ("빠르다", "to be fast"), ("정확하다", "to be accurate"), ("친절하다", "to be kind"), ("싸다", "to be cheap"), ("많다", "to be many")]
_JI_EX = [("데이비드가 어디에서 식사하는지 몰라요.", "I don’t know where David eats."), ("데이비드가 여기에서 식사하는지 몰라요.", "I don’t know if David eats here."), ("데이비드가 어디에서 먹는지 몰라요.", "I don’t know where David eats."), ("데이비드가 어디에서 먹었는지 몰라요.", "I don’t know where David ate."), ("데이비드가 어디에서 먹을지 몰라요.", "I don’t know where David will eat. (the book prints 어디에 먹을지)")]
_JI_EX2 = [("수업이 몇 시에 시작하는지 아세요?", "Do you know when class starts?"), ("어제 무엇을 배웠는지 말해주세요.", "Please tell me what you learned yesterday."), ("델몬티 쇼핑센터가 어디에 있는지 알아요.", "I know where Del Monte Shopping Center is."), ("왜 이 일병이 김치를 안 먹는지 모르겠어요.", "I don’t know why PFC Lee does not eat kimchi.")]
_JI_NOTE = [("책이 교실에 있는지 없는지 몰라요.", "I don’t know whether or not my book is in the classroom."), ("김 일병이 이라크에 갔는지 안 갔는지 아세요?", "Do you know if PFC Kim went to Iraq (or not)?"), ("제 아내가 한국에 갈지 안 갈지 몰라요.", "I don’t know whether or not my wife will go to Korea.")]
_JI_MODEL = [("김 일병 생일이 언제입니까?", "When is PFC Kim’s birthday? (A)"), ("저는 김 일병 생일이 언제인지 알아요.", "I know when PFC Kim’s birthday is. (B)")]
L6 = lesson(
    "Ch 22 · Grammar: the interrogative clause with -지",
    "어디에서 먹는지 몰라요 · 먹었는지 · 먹을지 · 있는지 없는지",
    requires=[],
    cards=[
        card("Expressing an interrogative clause",
             "Look at the following English clauses: I don’t know where David is (derived from Where is David?); I know what you ate last night (derived from What did you eat last night?); I wonder if he lives in Seaside (derived from Does he live in Seaside?). These clauses are all derived from questions but are now part of a sentence. They are called interrogative clauses. When a question becomes an interrogative clause, the typical interrogative word order changes (where is David → where David is), and in a yes/no question, if or whether is added (Does he live in Seaside → if he lives in Seaside).\n\n"
             "In Korean, when a question becomes an interrogative clause, the verb changes to -지. Depending on the tense of the verb, -지 has a different form.",
             examples=passage(_JI_EX[:2])),
        card("The rule: the verb ending in an interrogative clause -지",
             "In the book’s table (the arrow in 가다 → 가았는지 → 갔는지 shows the contraction).",
             tables=[table(["Condition", "Rule", "Example"], [["When the action verb is in present tense", "add 는지 to the verb stem", "가다 → 가는지; 먹다 → 먹는지"], ["When the stative verb is in present tense", "add (으)ㄴ지 to the verb stem", "크다 → 큰지; 작다 → 작은지"], ["When the verb is in past tense", "add 았/었는지 to the verb stem", "가다 → 가았는지 → 갔는지; 먹다 → 먹었는지"], ["When the verb is in future tense", "add (으)ㄹ지 to the verb stem", "가다 → 갈지; 먹다 → 먹을지"]])],
             examples=passage(_JI_EX[2:])),
        card("More examples",
             "The book’s examples:",
             examples=passage(_JI_EX2)),
        card("“Whether or not …” (or “if”)",
             "You can express “whether or not …” (or “if”) in the following way (repeat the verb in its affirmative and negative form):",
             examples=passage(_JI_NOTE)),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Action verb", "Meaning", "present -는지", "past -았/었는지", "future -(으)ㄹ지"], [[v, m, _ji_pres(v), _ji_past(v), _ji_fut(v)] for v, m in _JI_A], say=[0, 2, 3, 4]), table(["Stative verb", "Meaning", "present -(으)ㄴ지"], [[v, m, _ji_pres(v, True)] for v, m in _JI_S], say=[0, 2])]),
        card("Follow-up 1: the model",
             "In Follow-up 1 Partner A reads a question from List A (the lists are not in the book’s text) and Partner B changes it using -지 알아요. The book’s model:",
             examples=passage(_JI_MODEL)),
        card("Activities left out",
             "Follow-up 1’s lists are partner activities. The rest of the follow-ups are in the next lesson."),
    ],
    exercises=uniq(
        _fk(_JI_A, _ji_pres, "present -는지 (whether … does)", lambda v: [stem(v) + "는지", attr(v)[1] + "지", _ji_past(v), _ji_fut(v)])
        + _fk(_JI_A, _ji_past, "past -았/었는지 (whether … did)", lambda v: [_ji_pres(v), stem(v) + "았는지", _ji_fut(v), attr(v)[1] + "지"])
        + _fk(_JI_A, _ji_fut, "future -(으)ㄹ지 (whether … will)", lambda v: [_ji_pres(v), _ji_past(v), stem(v) + "을지" if not has_final(stem(v)) else stem(v) + "ㄹ지", attr(v)[1] + "지"])
        + _fk(_JI_S, lambda v: _ji_pres(v, True), "present -(으)ㄴ지 (whether … is)", lambda v: [stem(v) + "는지", attr(v)[0] + "지", past(v) + "는지", attr(v)[2] + "지"])
        + _tr(_JI_EX + _JI_EX2 + _JI_NOTE + _JI_MODEL)
        + [F("데이비드가 어디에서 먹___ 몰라요. (where he eats)", "는지", ["은지", "을지"], "action verb present: 는지."), F("데이비드가 어디에서 먹었___ 몰라요. (where he ate)", "는지", ["을지", "은지"], "past: 았/었는지."), F("데이비드가 어디에서 먹___ 몰라요. (where he will eat)", "을지", ["는지", "은지"], "future: (으)ㄹ지."),
           F("이 가방이 큰___ 작은지 몰라요. (whether big)", "지", ["는지", "고"], "크다 → 큰지."), F("책이 교실에 있는지 ___ 몰라요. (or not)", "없는지", ["없어요", "없고"], "있는지 없는지."), F("김 일병이 이라크에 갔는지 안 ___ 아세요? (went or not)", "갔는지", ["갈지", "가는지"], "갔는지 안 갔는지."),
           F("제 아내가 한국에 갈지 안 ___ 몰라요. (will go or not)", "갈지", ["갔는지", "가는지"], "갈지 안 갈지."), F("저는 김 일병 생일이 언제___ 알아요. (is)", "인지", ["는지", "을지"], "이다 (noun) + ㄴ지: 언제인지."),
           M("What does the verb ending -지 do?", "Makes a question into an interrogative clause", ["Makes a command", "Makes a past tense", "Makes a wish"], "어디에서 먹는지 몰라요."), M("Which ending is used for a past tense in an interrogative clause?", "았/었는지", ["는지", "(으)ㄴ지", "(으)ㄹ지"], "먹었는지."), M("Which ending is used for a stative verb in present tense?", "(으)ㄴ지", ["는지", "았/었는지", "(으)ㄹ지"], "큰지, 작은지."),
           read_q("어디에서 먹는지 몰라요"), read_q("어디에서 먹었는지 몰라요"), read_q("몇 시에 시작하는지 아세요"), read_q("있는지 없는지 몰라요"), read_q("생일이 언제인지 알아요")]
    ),
)

# ================================================================== L7: -지 follow-ups
_AD = [("한성통운", "Hansung Transport"), ("포장이사 전문", "Specialists in packed moves"), ("이사 계획이 있으세요?", "Do you have a plan to move?"), ("이삿짐 센터를 찾으세요?", "Are you looking for a moving company?"), ("빠른지, 정확한지, 친절한지, 싼지 한성통운과 알아보세요.", "Find out with Hansung Transport whether it is fast, accurate, kind and cheap."), ("전화주세요.", "Please call. (the telephone number is left out)")]
_PARENTS = [("부모님 고향이 어디인지 아세요?", "Do you know where your parents’ hometown is?"), ("부모님 생신이 언제인지 아세요?", "Do you know when your parents’ birthday is? (mine)"), ("부모님 취미가 무엇인지 아세요?", "Do you know what your parents’ hobbies are? (mine)"), ("부모님이 좋아하는 음식이 무엇인지 아세요?", "Do you know what your parents’ favorite food is? (mine)"), ("사촌이 몇 명인지 아세요?", "Do you know how many cousins you have? (mine)")]
_FORMS_Q = [("누가 설거지를 하는지", "who washes the dishes"), ("언제 이사하는지", "when someone moves"), ("어디에 사는지", "where someone lives"), ("무엇을 먹었는지", "what someone ate"), ("왜 안 왔는지", "why someone didn’t come"), ("어떻게 갈지", "how someone will go"), ("얼마인지", "how much it is"), ("누구인지", "who someone is")]
L7 = lesson(
    "Ch 22 · Grammar: the -지 follow-ups, an ad and questions about your parents",
    "빠른지 정확한지 친절한지 싼지 · 부모님 고향이 어디인지 아세요",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): an advertisement of a moving company",
             "The book gives an ad for a moving company and asks you to circle all the interrogative clauses (the clauses that end in 지) and translate them. The text is the book’s (the telephone number is left out); the English is mine.",
             examples=passage(_AD)),
        card("The four clauses (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Clause", "Translation (mine)"], [["빠른지", "whether (it is) fast"], ["정확한지", "whether (it is) accurate"], ["친절한지", "whether (it is) kind"], ["싼지", "whether (it is) cheap"]], say=[0])]),
        card("Follow-up 4: Find out about your partner’s parents (부모님 고향이 어디인지 아세요?)",
             "In Follow-up 4 you note in English your parents’ birth place, birthday, hobbies, favorite food and number of cousins, and exchange the information with your partner in Korean, using -지 알아요? or -지 아세요?. The book’s title question is the first; the others are my questions for the other items:",
             examples=passage(_PARENTS)),
        card("Interrogative clauses (mine)",
             "Some interrogative clauses made by the book’s rule (the question words are the ones you know):",
             tables=[table(["Clause", "Meaning"], [list(r) for r in _FORMS_Q], say=[0])]),
        card("Activities left out",
             "Follow-up 1 (partner question lists) and Follow-up 4’s partner exchange are partner activities; Follow-up 3 (listening to three segments of a conversation between two colleagues and translating the interrogative clause in each) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_AD + _PARENTS + _FORMS_Q)
        + [M("What is advertised?", "A moving company", ["A hotel", "A real estate agent", "A school"], "한성통운, 포장이사 전문."), M("What does the ad say you can find out?", "Whether it is fast, accurate, kind and cheap", ["Where it is", "When it opens", "Who runs it"], "빠른지, 정확한지, 친절한지, 싼지."), M("What does 포장이사 전문 mean?", "Specialists in packed moves", ["Regular moves only", "Small trucks", "Storage"], "포장이사 = a packed move."),
           M("How do you ask “Do you know where your parents’ hometown is?”", "부모님 고향이 어디인지 아세요?", ["부모님 고향이 어디예요?", "부모님 고향을 아세요?", "부모님 고향에 가요?"], "-지 아세요?."), M("Which is “who someone is”?", "누구인지", ["누구예요", "누가", "누구를"], "누구 + 이다 + ㄴ지."), M("Which is “how much it is”?", "얼마인지", ["얼마예요", "얼마나", "얼마를"], "얼마 + 이다 + ㄴ지."),
           F("한성통운과 알아보세요: 친절___. (whether kind)", "한지", ["하는지", "할지"], "친절하다 is stative: 친절한지."), F("한성통운과 알아보세요: 싼___. (whether cheap)", "지", ["는지", "을지"], "싸다 → 싼지."), F("부모님 생신이 언제___ 아세요? (is)", "인지", ["는지", "을지"], "언제 + 이다 + ㄴ지."),
           F("사촌이 몇 명___ 아세요? (how many)", "인지", ["는지", "을지"], "몇 명 + 이다 + ㄴ지."), F("누가 설거지를 하___ 알아요. (who washes)", "는지", ["은지", "을지"], "action verb: 는지."), F("무엇을 먹___ 알아요? (what someone ate)", "었는지", ["는지", "을지"], "past: 었는지."),
           read_q("한성통운"), read_q("포장이사 전문"), read_q("빠른지"), read_q("부모님 고향이 어디인지 아세요"), read_q("사촌이 몇 명인지 아세요")]
    ),
)

# ================================================================== L8: Topic C
_C_DLG = [
    ("정수 엄마", "민지네는 이번 달 관리비가 얼마 나왔어요?", "How much was Minji’s family’s management fee this month?"),
    ("민지 엄마", "삼십오만 원이나 나왔어요. 지난달보다 많이 나왔어요.", "It came to as much as 350,000 won. It was more than last month."),
    ("정수 엄마", "저희도요. 특히 난방비가 많이 나왔어요.", "Ours, too. The heating bill in particular came out high."),
    ("민지 엄마", "남편 월급은 오르지 않는데 물가는 자꾸 오르네요.", "My husband’s salary doesn’t go up, but prices keep going up."),
    ("정수 엄마", "맞아요. 그래서 요즘은 저축도 많이 못 해요.", "That’s right. So these days I can’t save much, either."),
    ("민지 엄마", "정수네는 저금도 해요? 저희는 저축할 돈이 없어요.", "Does Jungsu’s family save, too? We have no money to save."),
    ("정수 엄마", "그래도 아이들을 위해서 조금씩 저축해야 해요.", "Still, we have to save a little at a time for the children."),
    ("민지 엄마", "하지만 어디서 더 아껴야 할지 모르겠어요.", "But I don’t know where we should economize more."),
    ("정수 엄마", "저희 집은 지난달부터 교통비를 많이 줄였어요.", "Our family has cut down a lot on transportation costs since last month."),
    ("민지 엄마", "어떻게요?", "How?"),
    ("정수 엄마", "대중교통을 이용하거나 걸어 다녀요.", "We use public transportation or walk."),
    ("민지 엄마", "그래요? 그럼, 저희도 생활비를 절약하기 위해서 외식을 줄여야겠어요.", "Is that so? Then we should also cut down on eating out in order to save on living expenses."),
]
_C_WORDS = ["-거나 / 든지", "교육", "-기 위해(서)", "~네", "물가", "~비", "빚", "식비", "아끼다", "오락", "오르다", "외식", "월급", "~을/를 위해(서)", "자꾸", "저축 / 저금", "절약", "줄이다"]
_NE = [("정수 엄마", "Jungsu’s mother (the child’s name + mother)"), ("지현이 아빠", "Jihyun’s father (the child’s name + father)"), ("정수네", "Jungsu’s family"), ("지현이네", "Jihyun’s family"), ("김 씨네", "the Kim family"), ("박 선생님네", "Teacher Park’s family"), ("이 중위님네", "Lieutenant Lee’s family")]
_BI = [("교통비", "transportation expenses (the book asks you to guess; mine)"), ("회비", "a membership fee; dues (mine)"), ("학원비", "private-academy fees (mine)"), ("식비", "food expenses (the book’s core word)"), ("관리비", "a management fee (the book’s core word)"), ("잡비", "miscellaneous expenses (mine; 잡 (雜): odds and ends, mixed)"),
       ("비용", "an expense (the book’s example)"), ("병원비", "medical expenses; “hospital expense” (the book’s example)"), ("학비", "tuition; “expense for schooling” (the book’s example)"), ("치료비", "money for treatment (the book’s example)")]
L8 = lesson(
    "Ch 22 · Topic C: We will have to reduce living expenses",
    "생활비를 줄여야겠어요 · 관리비 · 난방비 · 저축 · 외식 · 정수네 · 비 (費)",
    requires=[],
    cards=[
        card("Topic C: We will have to reduce living expenses (생활비를 줄여야겠어요)",
             "Two women are chatting about their household expenses. (The English is mine; the book gives none. The book writes 35만 원; it is spelled out here. The book’s footnotes: 2. ~이나 can be used to express a number or an amount that is more than what the speaker expects. It means as many as or as much as. 3. 저희 집, which literally means “our house”, can be interpreted as my family in this context.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Cultural note: addressing parents and families",
             "The way men and women are addressed often changes once a child is born into the family. Family members or close acquaintances generally address the new parents by their children’s first names instead of their own. For example, in 정수 엄마 and 지현이 아빠, 정수 and 지현 refer to the children’s names. In addition, to refer to the family, Koreans often add ~(이)네 to one of their children’s names, as in 정수네 and 지현이네, or their titles, as in 김 씨네, 박 선생님네 or 이 중위님네.",
             tables=[table(["Expression", "Meaning (mine)"], [list(r) for r in _NE], say=[0])]),
        card("Sino-Korean in use: 비 (費)",
             "This Sino-Korean syllable means expense, cost, fee or expenditure, as in 비용 (expense), 병원비 (medical expenses; “hospital expense”), 학비 (tuition; “expense for schooling”) and 치료비 (money for treatment). The book asks you to guess the meaning of 교통비, 회비, 학원비, 식비, 관리비 and 잡비 (잡 (雜): odds and ends, mixed). The answers are mine, except 식비 and 관리비, which are core words.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _BI], say=[0])]),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity and Follow-up 1 (a SMART Board activity) are computer activities; Follow-up 2 (listening to three conversations in which a married couple discuss their household expenses and ways to reduce them) is an audio activity."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not any(c in w for c in "~(-/")]))
        + _tr(_strip(_C_DLG) + _NE + _BI)
        + [M("How much was Minji’s family’s management fee?", "350,000 won (more than expected)", ["35,000 won", "3,500,000 won", "30,000 won"], "삼십오만 원이나 나왔어요."), M("What was high in Jungsu’s family?", "The heating bill", ["The food bill", "The phone bill", "The school fee"], "특히 난방비가 많이 나왔어요."), M("What does Minji’s mother say about her husband’s salary and prices?", "The salary doesn’t go up but prices keep going up", ["Both go up", "Both go down", "Prices fall"], "월급은 오르지 않는데 물가는 자꾸 오르네요."),
           M("Why does Jungsu’s mother say they must save?", "For the children", ["For a house", "For a trip", "For a car"], "아이들을 위해서 조금씩 저축해야 해요."), M("How did Jungsu’s family cut transportation costs?", "They use public transportation or walk", ["They sold the car", "They moved", "They work from home"], "대중교통을 이용하거나 걸어 다녀요."), M("What will Minji’s family cut down on?", "Eating out", ["Heating", "Education", "Savings"], "외식을 줄여야겠어요."),
           M("What does ~이나 after a number mean?", "as many as; as much as", ["only", "about", "at least"], "삼십오만 원이나."), M("What does 저희 집 mean here?", "my family", ["our house only", "a hotel", "a school"], "The book’s footnote."), M("What does 비 (費) mean?", "expense; cost; fee", ["many", "move", "medicine"], "식비, 학원비, 병원비, 교통비."),
           F("남편 월급은 오르지 않는데 ___는 자꾸 오르네요. (prices)", "물가", ["식비", "월급"], "물가 = prices."), F("저희는 ___할 돈이 없어요. (to save)", "저축", ["절약", "외식"], "저축하다 = to save."), F("교통비를 많이 ___. (cut down)", "줄였어요", ["올랐어요", "나왔어요"], "줄이다 = to reduce."),
           F("어디서 더 아껴야 ___ 모르겠어요. (should)", "할지", ["하는지", "했는지"], "future: (으)ㄹ지."), F("아이들___ 위해서 조금씩 저축해야 해요. (for)", "을", ["이", "도"], "~을/를 위해서."), F("민지네는 이번 달 ___가 얼마 나왔어요? (management fee)", "관리비", ["식비", "빚"], "관리비 = a management fee."),
           read_q("생활비를 줄여야겠어요"), read_q("관리비가 얼마 나왔어요"), read_q("저축도 많이 못 해요"), read_q("대중교통을 이용하거나 걸어 다녀요"), read_q("외식을 줄여야겠어요")]
    ),
)

# ================================================================== L9: Activities C: expenses
_MATCH = [("책값, 과외비, 학원비", "교육비", "education expenses"), ("반찬 값", "식비", "food expenses"), ("레스토랑 음식비", "외식비", "eating-out expenses"), ("영화관람료, 게임비", "오락비", "entertainment expenses"), ("택시비, 지하철 요금, 버스 요금", "교통비", "transportation expenses"), ("식비, 교통비, 난방비", "생활비", "living expenses")]
_Q = [
    ("남편이랑 저랑 매달 오백오십만 원쯤 법니다.", "My husband and I earn about 5,500,000 won every month."), ("남편이랑 삼 년 전에 결혼했고 십오 개월 된 아기가 있어요.", "My husband and I got married three years ago, and we have a 15-month-old baby."), ("지금 저희는 전세 이억 팔천만 원짜리 이십삼 평 아파트에서 살고 있습니다.", "Now we live in a 23-pyeong apartment with a 전세 of 280,000,000 won."),
    ("매달 전기요금, 수도요금, 전화요금, 관리비 등으로 한 구십만 원 정도 들어요.", "Every month about 900,000 won goes to the electricity bill, the water bill, the phone bill, the management fee and so on."), ("또, 교통비 십오만 원, 오락비 이십만 원, 식비와 외식비로 백만 원 정도 들어요.", "Also, 150,000 won for transportation, 200,000 won for entertainment, and about 1,000,000 won for food and eating out."),
    ("그리고 시어머니가 아기를 돌봐 주시기 때문에 시어머니에게 오십만 원 정도 드리고 있어요.", "And because my mother-in-law looks after the baby, I give her about 500,000 won."), ("그리고 매달 팔십만 원 정도 저축하고 있어요.", "And I save about 800,000 won every month."),
    ("집을 사기 위해서 물건도 많이 사지 않으려고 하고 외식도 자주 하지 않으려고 해요.", "In order to buy a house, I try not to buy many things and not to eat out often."), ("하지만 저축을 많이 못 해요.", "But I can’t save much."), ("돈을 많이 쓰는 편은 아니에요.", "I am not on the side of spending a lot of money."),
    ("하지만 저축을 더 많이 하기 위해서 어떻게 해야 하는지 좀 알려주세요.", "But please tell me what I should do in order to save even more. (the request for advice)"), ("그럼, 수고하세요.", "Well, take care."),
]
_SAVE_MODEL = [("지난 달에 저는 택시를 타지 않고 버스를 타서 교통비를 아꼈습니다.", "Last month I didn’t take taxis but took the bus, so I saved on transportation costs."), ("지난달에 저는 비디오 게임을 많이 해서 오락비에 돈을 많이 썼습니다.", "Last month I played a lot of video games, so I spent a lot of money on entertainment expenses.")]
L9 = lesson(
    "Ch 22 · Topic C, Activities C: the expense types and a woman’s home finances",
    "생활비 · 교육비 · 외식비 · 오락비 · 교통비 · 저축 · 무엇을 절약해야 할까요",
    requires=[],
    cards=[
        card("Activity 1a: match the expenses with the types of expense",
             "The book lists six groups of expenses and six types of expense and asks you to draw lines between them. The lists are the book’s; the matches are mine (the book leaves them blank). The English is mine.",
             tables=[table(["Expenses", "Type of expense", "Meaning (mine)"], [list(r) for r in _MATCH], say=[0, 1])]),
        card("Activity 2 (Reading): a woman asks about her home finances",
             "The text is extracted from a Q&A section on a website where a woman asks about her home finances. The book asks you to identify what expense each amount of money is associated with, fill in a table in English, and then underline the woman’s request for advice and translate it into English. The text is the book’s (the amounts are spelled out in Hangul; the book’s 5백50만, 2억 8,000만 etc. are respelled); the English is mine.",
             examples=passage(_Q)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Amount of money", "Associated expense (mine)"], [["5,500,000 won (5백50만 원)", "The couple’s monthly income"], ["280,000,000 won (2억 8,000만 원)", "The 전세 deposit of the apartment"], ["900,000 won (90만 원)", "Electricity, water, phone and management fees"], ["150,000 won (15만 원)", "Transportation"], ["200,000 won (20만 원)", "Entertainment"], ["1,000,000 won (100만 원)", "Food and eating out"], ["500,000 won (50만 원)", "The mother-in-law, for looking after the baby"], ["800,000 won (80만 원)", "Savings"]])]),
        card("Activity 3: What should we save on? (the model)",
             "In Activity 3 (무엇을 절약해야 할까요?) you jot down last month’s expenses in English, categorize them on a form, write in Korean sentences about one area where you spent sparingly or lavishly, and then tell your partner and give advice. The book’s models (the English is mine):",
             examples=passage(_SAVE_MODEL)),
        card("Activities left out",
             "Activity 1b (listening to three conversations between two women sharing their concerns about household expenses) is an audio activity. Activity 3’s expense forms and partner exchange are written and partner activities."),
    ],
    exercises=uniq(
        _tr(_Q + _SAVE_MODEL + [(a, c) for a, b, c in _MATCH])
        + [M(f"Which type of expense includes {a}?", b, [x[1] for x in _MATCH if x[1] != b][:3], f"{a} → {b}.") for a, b, c in _MATCH]
        + [M("How much does the couple earn every month?", "About 5,500,000 won", ["About 550,000 won", "About 55,000,000 won", "About 800,000 won"], "오백오십만 원쯤."), M("How old is the baby?", "15 months", ["15 years", "3 years", "2 months"], "십오 개월 된 아기."), M("How big is the apartment?", "23 pyeong", ["33 pyeong", "12 pyeong", "50 pyeong"], "이십삼 평."), M("What is the 전세 deposit?", "280,000,000 won", ["28,000,000 won", "2,800,000,000 won", "280,000 won"], "이억 팔천만 원짜리."),
           M("How much is spent on utilities and the management fee?", "About 900,000 won", ["About 90,000 won", "About 9,000,000 won", "About 150,000 won"], "한 구십만 원 정도."), M("Who looks after the baby?", "The mother-in-law", ["The mother", "A nanny", "The father"], "시어머니가 아기를 돌봐 주시기 때문에."), M("How much does she save each month?", "About 800,000 won", ["About 80,000 won", "About 8,000,000 won", "About 200,000 won"], "팔십만 원 정도 저축."),
           M("What does she ask in the end?", "What she should do in order to save more", ["How to buy a house", "Where to eat out", "How to earn more"], "저축을 더 많이 하기 위해서 어떻게 해야 하는지 좀 알려주세요."),
           F("매달 ___ 팔십만 원 정도 저축하고 있어요. (every month)", "매달", ["매일", "매주"], "매달 = every month."), F("집을 사기 위해서 외식도 자주 하지 않으___ 해요. (try not to)", "려고", ["는 것", "으면"], "-(으)려고 하다."), F("돈을 많이 쓰는 ___은 아니에요. (side)", "편", ["평", "층"], "-는 편이다."),
           F("어떻게 해야 하는___ 좀 알려주세요. (what to do)", "지", ["고", "서"], "-지 interrogative clause."), F("지난 달에 택시를 타지 않고 버스를 타서 교통비를 ___. (saved)", "아꼈습니다", ["썼습니다", "올랐습니다"], "아끼다 = to save."),
           read_q("교육비"), read_q("외식비"), read_q("오락비"), read_q("생활비"), read_q("교통비를 아꼈습니다")]
    ),
)

# ================================================================== L10: Grammar A: -기 위해(서)
def _wihae(verb):
    return stem(verb) + "기 위해서"


_WI_V = [("사다", "to buy"), ("먹다", "to eat"), ("살다", "to live"), ("배우다", "to learn"), ("공부하다", "to study"), ("저축하다", "to save"), ("운동하다", "to exercise"), ("찾다", "to look for"), ("절약하다", "to economize"), ("읽다", "to read")]
_WI_EX = [("불고기를 먹으러 한국 식당에 갔어요.", "I went to a Korean restaurant to eat bulgogi."), ("불고기를 먹으려고 젓가락을 들었어요.", "I picked up my chopsticks to eat bulgogi."), ("불고기를 먹기 위해서 한국 식당에 갔어요.", "I went to a Korean restaurant (in order) to eat bulgogi."), ("불고기를 먹기 위해서 젓가락을 들었어요.", "I picked up my chopsticks (in order) to eat bulgogi."),
          ("차를 사기 위해 저축을 합니다.", "I am saving money in order to buy a car."), ("살기 위해서 먹습니다.", "I eat in order to live."), ("한국말을 배우기 위해 한국에 갔습니다.", "I went to Korea in order to learn Korean.")]
_WI_VOC = [("운동하기 위해서 체육관에 갑니다.", "I go to the gym in order to exercise."), ("저축하기 위해서 외식을 줄였어요.", "I cut down on eating out in order to save."), ("부모님을 위해서 선물을 샀습니다.", "I bought a present for my parents."), ("김 선생님은 아이들 교육을 위해 서울로 이사하려고 해요.", "Teacher Kim plans to move to Seoul for the children’s education.")]
L10 = lesson(
    "Ch 22 · Grammar A: expressing a purpose with -기 위해(서)",
    "먹기 위해서 · 차를 사기 위해 저축을 합니다 · 살기 위해서 먹습니다",
    requires=[],
    cards=[
        card("Expressing a purpose using -기 위해(서)",
             "Recall the two grammar features -(으)러 and -(으)려고 you learned about in earlier chapters: 불고기를 먹으러 한국 식당에 갔어요 (I went to a Korean restaurant to eat bulgogi) and 불고기를 먹으려고 젓가락을 들었어요 (I picked up my chopsticks to eat bulgogi). Both convey the same purpose: to eat bulgogi. -(으)러, however, works only with verbs like 가다, 오다 and 다니다. We can also express the same purpose by replacing the two grammar features with -기 위해(서).\n\n"
             "Koreans tend to use this grammar feature to emphasize a purpose; -기 위해(서) is often translated as in order to or so as to.",
             examples=passage(_WI_EX[:4])),
        card("“In order to” / “So as to”",
             "verb stem + 기 위해(서).",
             tables=[table(["Pattern", "Example"], [["verb stem + 기 위해(서)", "먹다 → 먹기 위해(서); 사다 → 사기 위해(서)"]])],
             examples=passage(_WI_EX[4:])),
        card("With nouns: ~을/를 위해(서)",
             "The core vocabulary also has ~을/를 위해(서) (for (the sake of); for (the benefit of)) for nouns, and -기 위해(서) for verbs. The book’s examples:",
             examples=passage(_WI_VOC)),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Verb", "Meaning", "-기 위해서"], [[v, m, _wihae(v)] for v, m in _WI_V], say=[0, 2])]),
        card("Activities left out",
             "Follow-up 1 (phrase strips posted on the classroom wall in two groups) is a class activity; Follow-up 2 (listening to three segments of a conversation and checking whether -(으)려고 or -기 위해(서) is used, and translating the phrase) is an audio activity."),
    ],
    exercises=uniq(
        _fk(_WI_V, _wihae, "-기 위해서 (in order to)", lambda v: [stem(v) + "려고", stem(v) + "으러", stem(v) + "는 편", stem(v) + "고 싶어서"])
        + _tr(_WI_EX + _WI_VOC)
        + [F("차를 사___ 위해 저축을 합니다. (in order to)", "기", ["는", "고"], "-기 위해."), F("살기 ___서 먹습니다. (in order to)", "위해", ["때문에", "보다"], "-기 위해서."), F("한국말을 배우기 ___ 한국에 갔습니다. (in order to)", "위해", ["전에", "때문에"], "-기 위해."), F("부모님___ 위해서 선물을 샀습니다. (for)", "을", ["이", "도"], "~을/를 위해서."),
           F("불고기를 먹___ 한국 식당에 갔어요. (to eat; only with 가다)", "으러", ["기 위해", "으려고"], "-(으)러 works with 가다, 오다, 다니다."), F("불고기를 먹___ 젓가락을 들었어요. (to eat)", "으려고", ["으러", "는 편"], "-(으)려고 or -기 위해서."),
           M("Which verbs can -(으)러 be used with?", "가다, 오다, 다니다", ["Any verb", "Only stative verbs", "Only 하다 verbs"], "-(으)러 works only with verbs like 가다, 오다 and 다니다."), M("How is -기 위해(서) translated?", "in order to; so as to", ["because of", "after", "if"], "Emphasizes a purpose."), M("Which pattern emphasizes a purpose?", "-기 위해(서)", ["-(으)러", "-는 편이다", "-지"], "Koreans tend to use it to emphasize a purpose."),
           read_q("먹기 위해서 한국 식당에 갔어요"), read_q("차를 사기 위해 저축을 합니다"), read_q("살기 위해서 먹습니다"), read_q("한국말을 배우기 위해 한국에 갔습니다"), read_q("부모님을 위해서 선물을 샀습니다")]
    ),
)

# ================================================================== L11: Grammar B: -거나/든지
def _gna(verb):
    return stem(verb) + "거나"


def _dji(verb):
    return stem(verb) + "든지"


_GN_V = [("만나다", "to meet"), ("보다", "to see; to watch"), ("치다", "to play (golf)"), ("하다", "to do"), ("놀다", "to play"), ("먹다", "to eat"), ("가다", "to go"), ("공부하다", "to study"), ("쉬다", "to rest"), ("자다", "to sleep"), ("청소하다", "to clean"), ("운동하다", "to exercise")]
_GN_EX = [("오렌지나 바나나를 주세요.", "Please give me an orange or a banana."), ("저는 한국이나 일본에 가고 싶어요.", "I’d like to go to Korea or Japan."), ("이번 주말에 친구를 만나거나 영화를 볼 거예요.", "This weekend I will meet friends or watch a movie."), ("이번 주말에 친구를 만나든지 영화를 볼 거예요.", "This weekend I will meet friends or watch a movie."),
          ("저 분은 일본사람이거나 한국사람일 거예요.", "That person may be Japanese or (may be) Korean."), ("저 분은 일본사람이든지 한국사람일 거예요.", "That person may be Japanese or (may be) Korean."), ("저는 주말에 골프를 치든지 등산을 합니다.", "On weekends I play golf or go hiking."), ("제 아내는 쇼핑을 하거나 집안일을 합니다.", "My wife goes shopping or does household chores."), ("제 아들은 친구와 놀거나 숙제를 합니다.", "My son plays with his friends or does homework."),
          ("저는 주말에 보통 친구를 만나거나 도서관에 갑니다.", "On weekends I usually meet friends or go to the library. (the core vocabulary’s example)")]
_GN_MODEL = [("이번 주말에 뭐 할 거예요?", "What are you going to do this weekend? (A)"), ("쇼핑가거나 영화를 볼 거예요.", "I will go shopping or watch a movie. (B)"), ("쇼핑가든지 영화를 볼 거예요.", "I will go shopping or watch a movie. (B)"), ("남동생하고 같이 야구를 하거나 영화를 보러 갈 거예요.", "I will play baseball with my younger brother or go to see a movie. (the Follow-up 5 model)")]
_GN_BOX = [("친구를 만나다", "to meet a friend"), ("공부하다", "to study"), ("빨래하다", "to do laundry"), ("기숙사에서 쉬다", "to rest in the dormitory"), ("영화를 보다", "to watch a movie"), ("자다", "to sleep"), ("운동하다", "to exercise"), ("도서관에 가다", "to go to the library"), ("쇼핑가다", "to go shopping"), ("청소하다", "to clean"), ("야영하다", "to camp"), ("낚시가다", "to go fishing"), ("공원에 가다", "to go to the park"), ("설거지하다", "to wash the dishes"), ("숙제하다", "to do homework"), ("머리를 자르다", "to get a haircut")]
L11 = lesson(
    "Ch 22 · Grammar B: the conjunctive ending -거나/든지 (or)",
    "친구를 만나거나 영화를 볼 거예요 · 골프를 치든지 등산을 합니다 · 일본사람이거나",
    requires=[],
    cards=[
        card("The conjunctive ending -거나/든지",
             "Recall the noun connector ~(이)나, which translates to or or either…or and is often used to indicate a choice or an alternative. As its name indicates, a noun connector connects only nouns: 오렌지나 바나나를 주세요; 저는 한국이나 일본에 가고 싶어요.\n\n"
             "When we connect verbs, however, we use the conjunctive ending (a.k.a. verb connector) -거나 or -든지 instead. The two are interchangeable in the book’s examples.",
             examples=passage(_GN_EX[:2])),
        card("“Or”",
             "verb stem + 거나 / 든지.",
             tables=[table(["Pattern", "Example"], [["verb stem + 거나 / 든지", "만나다 → 만나거나 / 만나든지; 하다 → 하거나 / 하든지"], ["noun + 이다 + 거나 / 든지", "일본사람이다 → 일본사람이거나 / 일본사람이든지"]], say=[])],
             examples=passage(_GN_EX[2:])),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Verb", "Meaning", "-거나", "-든지"], [[v, m, _gna(v), _dji(v)] for v, m in _GN_V], say=[0, 2, 3])]),
        card("Follow-up 3 and 5: weekend plans",
             "In Follow-up 3 Student A asks what Student B will do over the coming weekend; Student B chooses two actions from the words in the box and answers using -거나/든지. The words (the book’s list; the English is mine) are below. In Follow-up 5 you plan two things to do with each family member. The book’s models:",
             examples=passage(_GN_MODEL)),
        card("The box of phrases (Follow-up 3)",
             "The English is mine.",
             tables=[ktable(_GN_BOX)]),
        card("Activities left out",
             "Follow-up 4 (listening to three conversations about household chores and noting two chores in each) is an audio activity; Follow-up 3 and 5 (partner exchanges and a class presentation) are partner and class activities."),
    ],
    exercises=uniq(
        _fk(_GN_V, _gna, "-거나 (or)", lambda v: [stem(v) + "든지", stem(v) + "고", stem(v) + "나", stem(v) + "면서"])
        + _fk(_GN_V, _dji, "-든지 (or)", lambda v: [stem(v) + "거나", stem(v) + "든", stem(v) + "다가", stem(v) + "더니"])
        + _tr(_GN_EX + _GN_MODEL + _GN_BOX)
        + [F("오렌지___ 바나나를 주세요. (or, between nouns)", "나", ["거나", "든지"], "A noun connector connects nouns: ~(이)나."), F("친구를 만나___ 영화를 볼 거예요. (or, between verbs)", "거나", ["나", "이나"], "A verb connector: -거나."), F("저 분은 일본사람이___ 한국사람일 거예요. (or)", "거나", ["고", "든"], "일본사람이다 + 거나."),
           F("골프를 치___ 등산을 합니다. (or)", "든지", ["든", "나"], "-든지."), F("제 아들은 친구와 놀___ 숙제를 합니다. (or)", "거나", ["고", "으나"], "놀다 + 거나 (ㄹ remains)."), F("쇼핑가___ 영화를 볼 거예요. (or)", "거나", ["고", "나"], "쇼핑가다 + 거나."),
           M("What connects nouns as “or”?", "~(이)나", ["-거나", "-든지", "-지"], "오렌지나 바나나."), M("What connects verbs as “or”?", "-거나 / -든지", ["~(이)나", "-지", "-기 위해"], "Conjunctive ending."), M("Can -거나 and -든지 be used interchangeably in the book’s examples?", "Yes", ["No, never", "Only in questions", "Only in the past"], "만나거나 / 만나든지."),
           read_q("친구를 만나거나 영화를 볼 거예요"), read_q("골프를 치든지 등산을 합니다"), read_q("일본사람이거나 한국사람일 거예요"), read_q("쇼핑을 하거나 집안일을 합니다"), read_q("친구와 놀거나 숙제를 합니다")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Household chores", _CV_CHORE), ("Home management", _CV_HOME), ("Emotions", _CV_EMO), ("Home finance", _CV_FIN), ("Other words", _CV_OTH), ("Loan word", _CV_LOAN), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not any(c in r[0] for c in "~(-/")]
L12 = lesson(
    "Ch 22 · Core vocabulary and self-evaluation",
    "주요 단어 · 집안일 · 가정 관리 · 감정 · 가계 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (30일 → 삼십 일, 15일 → 십오 일, TV → 티브이). The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about common household chores; report malfunctions and request services for home maintenance; express emotions in a simple way; and express concerns and give suggestions on household expenses.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -지, the verb ending in an interrogative clause; -기 위해(서) (in order to; so as to); the conjunctive ending -거나/-든지 (or); and the Sino-Korean syllable 비 (費)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does -지 do at the end of a clause?", "Marks an interrogative clause", ["Marks a purpose", "Marks “or”", "Marks a past tense"], "한국이 어디에 있는지 알아요."), M("What does -기 위해(서) mean?", "in order to; so as to", ["or", "whether", "because"], "운동하기 위해서 체육관에 갑니다."), M("What does -거나 / 든지 mean?", "or (as conjunctive ending)", ["in order to", "whether", "although"], "친구를 만나거나 도서관에 갑니다."),
           M("What is “a management fee”?", "관리비", ["식비", "월급", "빚"], "관리비 = a management fee."), M("What is “a salary; a monthly paycheck”?", "월급", ["물가", "빚", "식비"], "월급 = a monthly wage."), M("What is “prices (of commodities)”?", "물가", ["월급", "빚", "오락"], "물가 = prices of things."), M("What is “a debt”?", "빚", ["월급", "물가", "식비"], "빚 = a debt."),
           M("What is “eating out”?", "외식", ["식비", "오락", "교육"], "외식 = outside eating."), M("What is “to leak”?", "새다", ["쓸다", "놓다", "벗다"], "새다 = to leak."), M("What is “to take off (clothes, shoes)”?", "벗다", ["입다", "놓다", "버리다"], "벗다 = to take off.")]
        + [read_q("주요 단어"), read_q("가정 생활"), read_q("관리사무소"), read_q("생활비를 줄여야겠어요"), read_q("집안일을 나눠서 합니다")]
    ),
)

UNIT = unit("Semester 1 · Unit 6 · Chapter 22: Home Life (가정 생활)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])

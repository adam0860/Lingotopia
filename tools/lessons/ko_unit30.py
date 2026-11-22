"""Unit 30: KBC Semester 1, Unit 6, Chapter 23 - Traditional Korean Holidays and Observances (한국의 명절과 기념일).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 6, Student's Edition (2022).
Audio, video clips, pictures, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the tables of holidays are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk


def _md(m, d):
    return month_ko(m) + " " + day_ko(d)


# ---- the core vocabulary of Chapter 23 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_DAYS = [
    ("공휴일", "(公休日) a legal holiday; an official holiday; “official resting day”", "공휴일에는 학교나 회사에 안 갑니다."),
    ("광복절", "(光復節) Korean Independence Day (from Japanese imperialism); “light-restoring day”", "광복절은 한국이 독립한 것을 기념하는 날입니다."),
    ("국경일", "(國慶日) a national holiday; “national celebration day”", "개천절과 광복절은 국경일입니다."),
    ("국군의 날", "(國軍) Korean Armed Forces day", "국군의 날에는 군인가족에게 공원 입장료가 무료입니다."),
    ("부처님오신날", "Buddha’s birthday; “day when Buddha came”", "부처님오신날에 절에서는 다양한 행사를 합니다."),
    ("스승의 날", "Teacher Appreciation Day", "선생님께 스승의 날 노래를 불러 드렸어요."),
    ("어린이날", "Children’s Day", "오늘은 어린이날이어서 쉽니다."),
    ("어버이날", "Parents’ Day", "어버이날 기념으로 부모님과 식사를 같이 했습니다."),
    ("한글날", "Korean Language Day; Hangeul Day", f"한글날은 {_md(10, 9)}입니다."),
    ("휴일", "(休日) a day off; “a rest day”", "휴일에는 보통 집안 일을 하고 책을 읽습니다."),
]
_CV_CELEB = [
    ("기념", "(記念) (~하다) celebration (to celebrate)", "온 가족이 호텔에서 딸의 고등학교 졸업을 기념했습니다."),
    ("꽃", "a flower", "우리집 정원에는 꽃과 나무가 많아요."),
    ("놀이공원", "(公園) an amusement park; “play park”", "지난 주말에 놀이공원에 갔다 왔어요."),
    ("달다", "to pin something on; to attach; to hang (a flag)", "내일은 광복절이니까 베란다에 태극기를 달 거예요."),
    ("독립", "(獨立) (~하다) independence; “solo standing” (to become independent)", f"인도는 {_kn(1947)} 년에 영국으로부터 독립하였습니다."),
    ("동물원", "(動物園) a zoo; “animal place”", "샌디에고 동물원은 세계에서 가장 큽니다."),
    ("장난감", "a toy; “playing material”", "아기가 자동차 장난감을 가지고 놉니다."),
    ("효도관광", "(孝道觀光) a vacation (for parents, paid for by the children); “filial piety sightseeing”", "저희 여행사에는 효도관광 상품이 많이 있습니다."),
]
_CV_TRAD = [
    ("귀성객", "(歸省客) people heading to their hometown during a holiday season; “homecoming people”", "연휴에는 기차역과 버스터미널에 귀성객이 많습니다."),
    ("놀이", "play; a game; amusement", "설날에는 가족이 모여 여러 가지 놀이를 합니다."),
    ("떡국", "rice cake soup", "아침에 가족들과 함께 떡국을 먹었어요."),
    ("명절", "(名節) a traditional holiday; “a celebration season”", "미국의 가장 큰 명절은 추수감사절과 성탄절입니다."),
    ("묘", "(墓) a grave; a tomb", "할머니 할아버지의 묘는 고향 뒷산에 있습니다."),
    ("복", "(福) fortune; a blessing", "새해 복 많이 받으세요."),
    ("설(날)", "Lunar New Year’s Day", "설날 아침에는 어른들께 세배를 드립니다."),
    ("성묘", "(省墓) (~하다/가다) visiting one’s ancestral grave (to visit one’s ancestral grave)", "설날에 우리 가족은 할아버지 묘에 성묘 갑니다."),
    ("세배", "(歲拜) (~하다) a formal bow of respect to one’s elders on New Year’s Day (to bow)", "새해 첫날에 어른들에게 세배를 드렸어요."),
    ("송편", "a traditional Korean rice cake steamed on a layer of pine needles", "추석에 친척들과 함께 송편을 만들었습니다."),
    ("전통", "(傳統) a tradition", "김치는 한국의 전통 음식입니다."),
    ("조상(님)", "(祖上) ancestors; forefathers", "추석 날에는 보통 조상님의 묘에 성묘 갑니다."),
    ("차례(를 지내다)", "(茶禮) a memorial service for an ancestor (to participate in an ancestor’s memorial service)", "설날 아침에 조상님께 차례를 지냅니다."),
    ("추석", "(秋夕) Harvest (Moon) Festival; “autumnal evening”", "송편은 추석의 대표적 음식입니다."),
]
_CV_CAL = [
    ("달력", "a calendar", "새해에 달력을 선물로 주는 가게가 많습니다."),
    ("~말", "(末) the end (of a week, month, or year)", "보통 칠월 말에 학교 방학이 시작됩니다."),
    ("새해", "a new year", "새해부터는 운동을 열심히 하겠습니다."),
    ("양력", "(陽曆) a solar calendar", "크리스마스는 양력 십이월 이십오일입니다."),
    ("음력", "(陰曆) a lunar calendar", "추석은 음력 팔월 십오일입니다."),
    ("중순", "(中旬) around the middle of the month", "한국에는 십일월 중순부터 눈이 많이 옵니다."),
    ("초순", "(初旬) the beginning of the month", "삼월 초순에 휴가를 쓸 계획입니다."),
]
_CV_LOAN = [("카드", "a card", "친구 생일이어서 생일카드를 샀어요."), ("크리스마스", "Christmas", "요즘은 세계의 많은 사람들이 크리스마스를 기념합니다.")]
_CV_OTH = [
    ("(결)정", "(決定) (~하다/~되다) a decision (to decide/to be decided)", "부모님께 드릴 선물을 아직 결정하지 못했어요."),
    ("글쎄", "“well”; “hmm” (as an interjection used to express thoughtfulness, doubt, hesitation, or perplexity)", "글쎄, 이 지갑은 가격이 너무 비싸다."),
    ("꼭", "without fail; make sure to; no matter what; at any cost", "주말에는 꼭 어머니께 전화를 드리세요."),
    ("-다고/라고 (말)하다", "to say that …; to tell that …", "아버님은 오늘 늦게 오신다고 말했습니다."),
    ("붐비다", "to be crowded; to be congested", "오늘은 금요일 밤입니다. 그래서 극장에 사람들이 붐빕니다."),
    ("생각", "(~하다/나다) thought; idea (to think; to consider/to come to mind; to occur to)", "어머니의 생일 선물로 프랑스제 스카프를 생각하고 있어요."),
    ("-았/었었", "used to (do something)", "전에는 이 학교가 아주 컸었어요."),
    ("이제", "now", "많은 사람들이 이제 인터넷으로 영화를 봅니다."),
    ("자기", "(自己) oneself; one’s own", "많은 학생들이 자기 차로 학교에 옵니다."),
    ("제일", "the first; the most; the -est", "저 남학생이 우리 반에서 키가 제일 큽니다."),
    ("중요", "(重要) (~하다) importance (to be important)", "중요한 기념일은 달력에 써 놓아야 합니다."),
    ("-지(요)", "“tag question” used to ask for confirmation or to seek agreement", "선생님 댁이 여기서 가깝지요?"),
    ("찾아가다", "to visit; “to find and go”", "기차역에는 고향을 찾아가는 사람들이 많아서 복잡했습니다."),
]
_CV_SINO = [("객", "(客) a guest; a visitor", "승객, 고객, 객실"), ("절", "(節) a season; a festival day; day", "광복절, 명절, 성탄절")]
_ALL = {r[0]: r for r in _CV_DAYS + _CV_CELEB + _CV_TRAD + _CV_CAL + _CV_LOAN + _CV_OTH + _CV_SINO}
_EXTRA = {"신정": "New Year’s Day (the solar calendar)", "삼일절": "Independence Movement Day (March 1, 1919)", "식목일": "Arbor Day", "현충일": "Memorial Day", "제헌절": "Constitution Day", "개천절": "National Foundation Day", "성탄절": "Christmas; “sacred birth day”", "석가탄신일": "Buddha’s Birthday", "음절": "a syllable; “sound sect”", "예절": "etiquette; manners; “polite parts”",
          "사계절": "the four seasons (mine)", "승객": "a passenger; “riding guest”", "관객": "a spectator; “viewing visitor”", "여객기": "a passenger plane (mine)", "여객선": "a passenger ship (mine)", "객실": "a guest room (mine)", "객지": "a place away from home (mine)", "세뱃돈": "New Year’s money given after a bow", "한복": "traditional Korean clothes (mine)", "고속도로": "an expressway (mine)",
          "팽이치기": "top spinning", "제기차기": "hacky sack", "연날리기": "kite flying", "널뛰기": "seesaw jumping", "그네뛰기": "swinging", "친척": "relatives (mine)", "고향": "a hometown (mine)", "어른": "an adult; an elder (mine)", "건강식품": "health food (mine)", "현금": "cash (mine)", "특별": "special (mine)", "여행": "a trip (mine)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)

# ================================================================== L1: objectives, the holiday table and the notes
_HOL = [("신정", _md(1, 1), "일월 일일", "New Year’s Day"), ("설날", "음력 " + _md(1, 1), "음력 일월 일일", "Lunar New Year’s Day"), ("삼일절", _md(3, 1), "삼월 일일", "Independence Movement of March 1, 1919"), ("식목일", _md(4, 5), "사월 오일", "Arbor Day"), ("어린이날", _md(5, 5), "오월 오일", "Children’s Day"), ("어버이날", _md(5, 8), "오월 팔일", "Parents’ Day"),
        ("스승의 날", _md(5, 15), "오월 십오일", "Teacher Appreciation Day"), ("부처님오신날 / 석가탄신일", "음력 " + _md(4, 8), "음력 사월 팔일", "Buddha’s Birthday"), ("현충일", _md(6, 6), "유월 육일", "Memorial Day"), ("제헌절", _md(7, 17), "칠월 십칠일", "Constitution Day"), ("광복절", _md(8, 15), "팔월 십오일", "Independence Day of Korea"),
        ("추석", "음력 " + _md(8, 15), "음력 팔월 십오일", "Harvest (Full Moon) Festival"), ("국군의 날", _md(10, 1), "시월 일일", "National Armed Forces Day"), ("개천절", _md(10, 3), "시월 삼일", "National Foundation Day"), ("한글날", _md(10, 9), "시월 구일", "Hangeul Day"), ("성탄절 / 크리스마스", _md(12, 25), "십이월 이십오일", "Christmas")]
_HOL_ROWS = [[a, b, d] for a, b, c, d in _HOL]
_DATES = [("광복절", "팔일오", "August 15 (8·15)"), ("삼일절", "삼일절", "the Independence Movement of March 1 (3·1절)"), ("육이오", "육이오", "June 25, 1950, the day the Korean War broke out (6·25)")]
L1 = lesson(
    "Ch 23 · What the chapter teaches and the Korean holidays table",
    "한국의 명절과 기념일 · 신정 · 설날 · 삼일절 · 광복절 · 추석 · 한글날",
    requires=[],
    cards=[
        card("What Chapter 23 teaches (한국의 명절과 기념일)",
             "Chapter 23, “Traditional Korean Holidays and Observances”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and talk about important Korean holidays and observances; identify and talk about activities done on traditional Korean holidays; and express gratitude to teachers and parents.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; -지요 used to ask for confirmation or to seek agreement; -았었다 or -었었다 (used to [do/not do something]); -다고 하다 or -라고 하다 used to quote indirectly; and the Sino-Korean syllables 객 (客) and 절 (節)."),
        card("Korean national holidays and observances (한국의 국경일과 기념일)",
             "The book’s table of Korean national holidays and observances, with the date and the English meaning. The book’s footnotes: 설날 and 추석 are three-day holidays; 음력: (by the) lunar calendar. (The dates are written 1월 1일 etc. in the book; the Korean reading is in the next card.)",
             tables=[table(["한국의 국경일과 기념일", "날짜", "영어 뜻"], _HOL_ROWS)]),
        card("The dates read aloud (Korean)",
             "How the dates are read (months and days in Sino-Korean; June is 유월 and October is 시월).",
             tables=[table(["Holiday", "Date read aloud"], [[a, c] for a, b, c, d in _HOL], say=[0, 1])]),
        card("Notes: historical events named by their dates",
             "Historical events in Korea are often referred to by the date on which the event occurred. For example, 광복절 (Independence Day) is often called 8·15 (팔일오) and the Independence Movement of March 1 is officially named 3·1절 (삼일절). 6·25 (육이오) refers to June 25, 1950, the day the Korean War broke out.",
             tables=[table(["Name", "Reading", "Meaning"], [list(r) for r in _DATES], say=[1])]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1 and 2 (SMART Board activities) and Activity 3 (“Grab the Word”, a team game with word cards posted on the classroom wall) are picture, computer or game activities."),
    ],
    exercises=uniq(
        _tr([(a, d) for a, b, c, d in _HOL])
        + [M(f"When is {a}?", c, [x[2] for x in _HOL if x[2] != c][:3], f"{a}: {d}.") for a, b, c, d in _HOL[:12]]
        + [M("Which holidays are three-day holidays?", "설날 and 추석", ["삼일절 and 광복절", "어린이날 and 어버이날", "한글날 and 개천절"], "The book’s footnote."), M("What does 음력 mean?", "(by the) lunar calendar", ["the solar calendar", "a holiday", "a day off"], "음력 = lunar calendar."), M("What is 6·25 (육이오)?", "June 25, 1950, the day the Korean War broke out", ["August 15", "March 1", "October 3"], "육이오."),
           M("What is 8·15 (팔일오)?", "Independence Day (광복절)", ["Children’s Day", "Hangeul Day", "Memorial Day"], "팔일오 = August 15."), M("What is 3·1절 (삼일절)?", "The Independence Movement of March 1 (1919)", ["Arbor Day", "Teacher Appreciation Day", "Christmas"], "삼일절."),
           F("광복절은 ___ 십오일입니다. (August)", "팔월", ["칠월", "유월"], "팔월 십오일."), F("한글날은 ___ 구일입니다. (October)", "시월", ["십월", "유월"], "10월 is 시월."), F("현충일은 ___ 육일입니다. (June)", "유월", ["육월", "시월"], "6월 is 유월."),
           read_q("한국의 명절과 기념일"), read_q("광복절"), read_q("추석"), read_q("한글날"), read_q("크리스마스")]
    ),
)

# ================================================================== L2: Topic A
_A_DLG = [
    ("지훈", "다은 씨, 내년 달력이 나왔어요.", "Daeun, next year’s calendar has come out."),
    ("다은", "그래요? 그럼 휴일 좀 확인해 봐요.", "Is that so? Then let’s check the holidays."),
    ("지훈", "네. 이런! 내년에는 설날과 추석연휴가 너무 짧네!", "Yes. Oh my! Next year the Lunar New Year and Chuseok holidays are too short!"),
    ("다은", "어, 정말이군요! 그런데 다른 연휴는 없어요?", "Oh, so they are! But is there no other long holiday?"),
    ("지훈", "다행히 팔월에 하나 있어요. 광복절이 금요일이어서 그때는 사흘 동안 쉴 수 있어요.", "Fortunately there is one in August. Independence Day falls on a Friday, so we can rest for three days then."),
    ("다은", "잘 됐네요! 지훈 씨, 시월 달력 좀 볼까요?", "That’s great! Jihoon, shall we look at the October calendar?"),
    ("지훈", "시월이요? 왜요?", "October? Why?"),
    ("다은", "시월에 중요한 국경일이 많으니까요. 국군의 날, 개천절, 한글날 그리고 또…", "Because there are many important national holidays in October: Armed Forces Day, National Foundation Day, Hangeul Day, and also…"),
    ("지훈", "그렇지만 개천절과 한글날만 공휴일이에요. 국군의 날은 이제 쉬지 않아요.", "But only National Foundation Day and Hangeul Day are legal holidays. We don’t take a day off on Armed Forces Day any more."),
    ("다은", "그렇군요. 그런데 올해는 추석이 언제예요?", "I see. By the way, when is Chuseok this year?"),
    ("지훈", "구월 초순입니다.", "It is in early September."),
    ("다은", "잘 됐다! 우리 아버지 생신도 구월 초순이니까 그때 꼭 고향에 가야겠어요.", "Great! My father’s birthday is also in early September, so I must go to my hometown then."),
]
_A_WORDS = ["공휴일", "광복절", "국경일", "국군의 날", "기념", "꼭", "달력", "독립", "~말", "부처님오신날", "설(날)", "이제", "중순", "중요", "초순", "추석", "크리스마스", "한글날", "휴일"]
L2 = lesson(
    "Ch 23 · Topic A: Korean national holidays and legal holidays",
    "한국의 국경일과 공휴일 · 달력 · 연휴 · 사흘 · 중요한 국경일 · 초순",
    requires=[],
    cards=[
        card("Topic A: Korean national holidays and legal holidays (한국의 국경일과 공휴일)",
             "Two colleagues are talking about holidays on the New Year calendar. (The English is mine; the book gives none. The book’s stage directions “(pause)” are left out. The book’s footnote: 이런 literally translates to “(things) like this”. It is used as an exclamation and has a meaning similar to Oh my! or Darn it! in English.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Activities left out",
             "The SMART Board activity and the sentence strips of the Presentation Activity (arranging the strips of Topic A in a logical order, with the first two numbered) are computer and partner activities. Follow-up 1 (listening to four conversations between a female Korean instructor and her male student and choosing the holiday from a box of Korean Language Day, Buddha’s Birthday, National Armed Forces Day, Independence Day and Memorial Day) is an audio activity. The October calendar, the Follow-up 2 article and the activities are in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not any(c in w for c in "~(-/")]))
        + _tr(_strip(_A_DLG))
        + [M("What has come out?", "Next year’s calendar", ["A new book", "A newspaper", "A holiday list only"], "내년 달력이 나왔어요."), M("What is wrong with next year’s Lunar New Year and Chuseok holidays?", "They are too short", ["They are too long", "They are in winter", "They are cancelled"], "너무 짧네!"), M("Why can they rest for three days in August?", "Independence Day falls on a Friday", ["It is a vacation", "It is Chuseok", "It is a weekend"], "광복절이 금요일이어서 사흘 동안 쉴 수 있어요."),
           M("Which October days are legal holidays?", "National Foundation Day and Hangeul Day", ["Armed Forces Day and Hangeul Day", "Armed Forces Day only", "All three"], "개천절과 한글날만 공휴일."), M("Is Armed Forces Day a day off?", "No, not any more", ["Yes", "Only in October", "Only for soldiers"], "국군의 날은 이제 쉬지 않아요."), M("When is Chuseok this year?", "In early September", ["In late September", "In early October", "In mid-August"], "구월 초순."),
           M("Why will Daeun definitely go to her hometown?", "Her father’s birthday is also in early September", ["It is Chuseok only", "She lives there", "She has a long vacation"], "아버지 생신도 구월 초순."), M("What does 이런 mean?", "Oh my!; Darn it!", ["Hello", "Thank you", "Goodbye"], "The book’s footnote."), M("What does 사흘 mean?", "three days", ["two days", "four days", "a week"], "사흘 동안 쉴 수 있어요."),
           F("내년 ___이 나왔어요. (calendar)", "달력", ["공휴일", "휴일"], "달력 = a calendar."), F("구월 ___입니다. (early)", "초순", ["중순", "말"], "초순 = the beginning of the month."), F("시월에 ___한 국경일이 많으니까요. (important)", "중요", ["특별", "정확"], "중요하다 = to be important."),
           F("그때 ___ 고향에 가야겠어요. (without fail)", "꼭", ["이제", "제일"], "꼭 = without fail."), F("국군의 날은 ___ 쉬지 않아요. (now; any more)", "이제", ["꼭", "제일"], "이제 = now."), F("개천절과 한글날만 ___이에요. (legal holiday)", "공휴일", ["달력", "국경일"], "공휴일 = a legal holiday."),
           read_q("내년 달력이 나왔어요"), read_q("설날과 추석연휴"), read_q("사흘 동안 쉴 수 있어요"), read_q("중요한 국경일이 많으니까요"), read_q("구월 초순입니다")]
    ),
)

# ================================================================== L3: calendar, Follow-up 2 article, Activity 1, North Korea, 절
_CAL = [(1, "국군의 날", "Armed Forces Day"), (2, "엄마 생신", "Mother’s birthday"), (3, "개천절", "National Foundation Day"), (8, "친구와 영화 보기", "Seeing a movie with a friend"), (9, "한글날", "Hangeul Day"), (10, "학원 시험", "A test at the private academy"), (15, "피아노 레슨", "Piano lesson"), (18, "문화의 날", "Culture Day"), (21, "경찰의 날", "Police Day"), (24, "가족들과 외식", "Eating out with the family"), (28, "은행 가기", "Going to the bank"), (29, "저축의 날", "Savings Day")]
_NEWS = [("직장인 육십일 퍼센트 공휴일, 너무 적다", "61% of office workers: “Too few official holidays”"), ("직장인 오문선 씨는 지난해부터 식목일이 공휴일에서 없어지고, 올해 공휴일 중 어린이 날이 토요일이어서 실제 휴일이 너무 적다고 말했다.", "Office worker Oh Moonsun said that since last year Arbor Day has disappeared from the official holidays, and that this year Children’s Day falls on a Saturday, so the actual holidays are too few. (the book’s ages and dates in parentheses are left out here)"),
         ("그렇다면 외국의 경우는 어떨까?", "Then what about foreign countries?"), ("이웃나라 일본, 중국과 비교할 때 우리나라의 공휴일은 적은 편이다.", "Compared with the neighboring countries Japan and China, Korea’s official holidays are on the few side."),
         ("일본과 중국은 공휴일이 십칠 일이다.", "Japan and China have 17 official holidays."), ("따라서 우리나라보다 이 일이 더 많다.", "Therefore they have two more days than Korea."), ("한국의 공휴일은 설날연휴와 추석연휴, 삼일절, 광복절 등을 포함하여 총 십오 일이다.", "Korea’s official holidays, including the Lunar New Year and Chuseok holidays, March 1st, Independence Day and so on, total 15 days."),
         ("내년부터 제헌절도 공휴일에 포함되지 않기 때문에 우리나라의 법정공휴일은 십사 일이 된다.", "From next year Constitution Day will also not be included in the official holidays, so Korea’s legal holidays will be 14 days.")]
_ACT1 = [("국가가 공식적으로 만든 휴일입니다.", "It is a holiday officially made by the state.", "c. 공휴일"), ("설날과 추석 같은 날입니다.", "It is a day like the Lunar New Year and Chuseok.", "b. 명절"), ("이 날은 십이월 말에 있습니다. 캐럴을 부르고 카드나 선물을 주고 받습니다.", "This day is at the end of December. People sing carols and give and receive cards or presents.", "d. 성탄절"),
         ("이 날은 세종대왕이 한글을 만든 것을 기념합니다.", "This day commemorates King Sejong’s creation of Hangeul.", "a. 한글날"), ("이 날은 천구백사십오 년 팔월 십오일 한국이 독립한 것을 기념합니다.", "This day commemorates Korea’s becoming independent on August 15, 1945.", "e. 광복절")]
_NK = [("태양절", "“the Sun Day”: Kim Il-sung’s birthday (April 15)"), ("이월절", "Kim Jung-il’s birthday (written 2월절)"), ("국제 노동자절", "International Labor Day"), ("조국해방 기념일", "Independence Day"), ("인민정권 창건일", "People’s Party Foundation Day"), ("노동당 창건일", "Labor Party Day"), ("사회주의 헌법절", "Communist Constitution Day"), ("설", "New Year’s Day"), ("사회주의 칠대 명절", "Seven Socialists’ National Holidays (written 사회주의 7대 명절)"), ("사일오 명절", "the 4·15 holiday: another name of 태양절")]
_JEOL = [("광복절", "Korea’s Independence Day; “regain light/freedom day”"), ("성탄절", "Christmas; “sacred birth day”"), ("음절", "a syllable; “sound sect”"), ("예절", "etiquette; manners; “polite parts”"), ("명절", "a traditional holiday (mine; 명 (名): name, fame, celebration)"), ("사계절", "the four seasons (mine)")]
L3 = lesson(
    "Ch 23 · Topic A, Follow-up 2 and Activity 1: the October calendar and reading about holidays",
    "시월 달력 · 공휴일, 너무 적다 · 명절 · 공휴일 · 성탄절 · 절 (節) · 북한 보고서",
    requires=[],
    cards=[
        card("The October calendar (10월 달력)",
             "The book shows a calendar for October with handwritten notes. They were read from the page image (the dates are in Hangul here).",
             tables=[table(["Date", "Note", "Meaning (mine)"], [[day_ko(d), k, e] for d, k, e in _CAL], say=[0, 1])]),
        card("Follow-up 2 (Reading): an article about official holidays",
             "The book gives an article and four statements to mark true (T) or false (F). The text is the book’s (the figures and the dates are spelled out in Hangul; the book’s “직장인 오문선 (33) 씨” gives her age in parentheses and “식목일(4월5일)” gives a date; I left the parentheses out here). The English is mine. The book glosses 적다: to be few.",
             examples=passage(_NEWS)),
        card("The statements and the answers (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Statement", "T/F (mine)"], [["1. Mr. Oh Moon Sun says Korea has too many official holidays.", "F: he says there are too few"], ["2. Korea has fewer official holidays than Japan or China.", "T"], ["3. Korea has 17 official holidays per year.", "F: Japan and China have 17; Korea has 15"], ["4. Next year, Constitution Day will not be observed as an official holiday.", "T"]])]),
        card("Activity 1 (Reading): which holiday is it?",
             "The book gives five sentences describing a holiday and a box of the holidays (a. 한글날, b. 명절, c. 공휴일, d. 성탄절, e. 광복절) and asks you to write the matching letter. The sentences are the book’s (the year and the date are spelled out); the English and the matches are mine.",
             tables=[table(["Sentence", "Meaning (mine)", "Match (mine)"], [list(r) for r in _ACT1], say=[0])]),
        card("North Korea Report",
             "North Korea has eight national holidays: Kim Il-sung’s birthday, known as 태양절 (“the Sun Day”), 2월절 (Kim Jung-il’s birthday), 국제 노동자절 (International Labor Day), 조국해방 기념일 (Independence Day), 인민정권 창건일 (People’s Party Foundation Day), 노동당 창건일 (Labor Party Day), 사회주의 헌법절 (Communist Constitution Day) and 설 (New Year’s Day). The first seven holidays are called 사회주의 7대 명절 (Seven Socialists’ National Holidays). Among these holidays, the most important is Kim Il-sung’s birthday on April 15, called either 태양절 or 4·15 명절.",
             tables=[table(["Name (spoken)", "Meaning"], [list(r) for r in _NK], say=[0])]),
        card("Sino-Korean in use: 절 (節)",
             "The original meaning of this Sino-Korean syllable is section or part (of something), as in 음절 (a syllable; “sound sect”) and 예절 (etiquette; manners; “polite parts”). When it is used in the context of time, 절 (節) refers to a section of time, that is, a season or festival day, as in 광복절 (Korea’s Independence day; “regain light/freedom day”) and 성탄절 (Christmas; “sacred birth day”). The book asks you to guess the meaning of 명절 and 사계절 (명 (名): name, fame, celebration); the answers are mine.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _JEOL], say=[0])]),
        card("Activities left out",
             "Activity 2 (listening to three dialogs about commemoration days) is an audio activity; Activity 3 (한국의 국경일과 미국의 국경일을 비교합시다: Text A and Text B, a jigsaw reading, a flip chart and a class presentation) is a group activity whose texts are not in the book’s text."),
    ],
    exercises=uniq(
        _tr(_NEWS + [(a, b) for a, b, c in _ACT1] + _NK + _JEOL + [(k, e) for d, k, e in _CAL])
        + [M("What is on October 3?", "개천절 (National Foundation Day)", ["한글날", "국군의 날", "저축의 날"], "3 → 개천절."), M("What is on October 9?", "한글날 (Hangeul Day)", ["개천절", "문화의 날", "경찰의 날"], "9 → 한글날."), M("What is on October 29?", "저축의 날 (Savings Day)", ["경찰의 날", "문화의 날", "은행 가기"], "29 → 저축의 날."), M("What happens on October 2?", "Mother’s birthday", ["A piano lesson", "A test", "Going to the bank"], "2 → 엄마 생신."),
           M("Which statement matches “It is a holiday officially made by the state”?", "공휴일", ["명절", "성탄절", "한글날"], "국가가 공식적으로 만든 휴일."), M("Which holiday commemorates King Sejong’s creation of Hangeul?", "한글날", ["광복절", "성탄절", "명절"], "세종대왕이 한글을 만든 것."), M("Which holiday commemorates Korea’s independence on August 15, 1945?", "광복절", ["한글날", "삼일절", "개천절"], "천구백사십오 년 팔월 십오일."),
           M("How many official holidays do Japan and China have?", "17", ["15", "14", "12"], "일본과 중국은 공휴일이 십칠 일이다."), M("How many official holidays does Korea have (before the change)?", "15", ["17", "14", "12"], "총 십오 일."), M("What will the number of legal holidays become next year?", "14", ["15", "17", "13"], "법정공휴일은 십사 일이 된다."), M("What does 절 (節) mean in 광복절?", "a festival day; day", ["a temple", "a teacher", "a season only"], "광복절, 성탄절."),
           F("공휴일이 ___ 일이다. (17)", "십칠", ["십오", "십사"], "십칠 일."), F("한국의 공휴일은 총 ___ 일이다. (15)", "십오", ["십칠", "십사"], "십오 일."), F("우리나라의 공휴일은 적은 ___이다. (side)", "편", ["평", "층"], "적은 편이다."),
           read_q("공휴일, 너무 적다"), read_q("식목일이 공휴일에서 없어지고"), read_q("법정공휴일"), read_q("성탄절"), read_q("명절")]
    ),
)

# ================================================================== L4: Topic B
_B_TEXT = [
    ("음력 일월 일일은 설입니다.", "The first day of the first month by the lunar calendar is 설."), ("설은 한국의 가장 큰 명절입니다.", "설 is Korea’s biggest traditional holiday."), ("설에는 가족과 친척들과 함께 시간을 보냅니다.", "On 설 people spend time with their family and relatives."), ("그래서 고향을 찾아가는 사람들이 많습니다.", "So many people visit their hometowns."),
    ("기차역과 고속버스 터미널, 공항 등은 귀성객들로 붐빕니다.", "Train stations, express bus terminals, airports and so on are crowded with people heading to their hometowns."), ("그리고 고속도로도 많이 막힙니다.", "And the expressways are also heavily congested."),
    ("설날 아침에는 가족들이 모두 일찍 일어나서 제일 먼저 한복을 입습니다.", "On the morning of the Lunar New Year, all the family members get up early and first of all put on hanbok."), ("그리고 조상님께 차례를 지내고 어른들께 세배도 드립니다.", "And they hold a memorial service for their ancestors and also make a formal bow to the elders."),
    ("세배를 하면서 보통 새해 복 많이 받으세요 라고 말합니다.", "While bowing, they usually say “Happy New Year!” (literally “Receive many blessings in the new year!”)."), ("그러면 어른들께서는 세뱃돈을 주시면서 한 해 동안 건강하게 잘 지내라고 하십니다.", "Then the elders give New Year’s money and say, “Stay healthy during the year.”"),
    ("세배를 드린 후에는 가족이 다 같이 모여서 떡국을 먹습니다.", "After the bows, the whole family gathers together and eats rice cake soup."), ("설날에는 보통 성묘를 가거나 전통 놀이를 합니다.", "On the Lunar New Year they usually visit ancestral graves or play traditional games."),
]
_B_WORDS = ["귀성객", "놀이", "-다고/라고 (말)하다", "떡국", "명절", "묘", "복", "붐비다", "새해", "성묘", "세배", "송편", "양력", "음력", "자기", "전통", "제일", "조상(님)", "차례(를 지내다)", "찾아가다"]
L4 = lesson(
    "Ch 23 · Topic B: I offered a big bow to my friend’s parents on New Year’s Day",
    "설날에 친구 부모님께 세배를 드렸습니다 · 귀성객 · 차례 · 세배 · 떡국 · 성묘",
    requires=[],
    cards=[
        card("Topic B: I offered a big bow to my friend’s parents on New Year’s Day (설날에 친구 부모님께 세배를 드렸습니다)",
             "Sarah, an American student attending a language school in Korea, is reporting in class about the traditional Korean New Year’s Day. (The English is mine; the book gives none. The book writes 음력 1월 1일; it is spelled out here. The book’s footnotes: 4. When quoting directly, 라고 (말)하다 is added after the quotation. 5. 한 해 동안 잘 지내라 is a common blessing given on New Year’s Day and literally means “stay healthy during the year.” 6. The traditional games introduced in this chapter are also called 전통민속놀이 (traditional folk games).)",
             examples=passage(_B_TEXT)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity are computer activities. Follow-up 1 (listening to three dialogs about 설날 or 추석 and listing the activities the man did) is an audio activity. The notes on 세뱃돈 and the folk games, the Sino-Korean syllable 객 and Follow-up 2 are in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not any(c in w for c in "~(-/")]))
        + _tr(_B_TEXT)
        + [M("What is Korea’s biggest traditional holiday?", "설 (Lunar New Year)", ["추석", "광복절", "한글날"], "설은 한국의 가장 큰 명절입니다."), M("What do people spend time with on 설?", "Family and relatives", ["Friends only", "Colleagues", "Neighbors"], "가족과 친척들과 함께 시간을 보냅니다."), M("What are crowded with people heading to their hometowns?", "Train stations, bus terminals and airports", ["Parks", "Schools", "Department stores"], "귀성객들로 붐빕니다."),
           M("What do the family members put on first on the morning of 설날?", "Hanbok", ["Suits", "Sports clothes", "Uniforms"], "제일 먼저 한복을 입습니다."), M("What do they do for the ancestors?", "Hold a memorial service", ["Cook for guests", "Plant trees", "Sing a song"], "조상님께 차례를 지내고."), M("What do people usually say while bowing?", "새해 복 많이 받으세요!", ["감사합니다", "안녕히 계세요", "수고하세요"], "새해 복 많이 받으세요."),
           M("What do the elders give after the bows?", "세뱃돈 (New Year’s money)", ["Rice cakes", "Flowers", "Cards"], "세뱃돈을 주시면서."), M("What does the whole family eat after the bows?", "떡국 (rice cake soup)", ["송편", "김치", "불고기"], "떡국을 먹습니다."), M("What do people usually do on 설날 besides?", "Visit ancestral graves or play traditional games", ["Go shopping", "Go swimming", "Work"], "성묘를 가거나 전통 놀이를 합니다."),
           F("기차역은 ___들로 붐빕니다. (people heading to their hometowns)", "귀성객", ["승객", "관객"], "귀성객 = homecoming people."), F("가족이 다 같이 모여서 ___을 먹습니다. (rice cake soup)", "떡국", ["송편", "김치"], "떡국 = rice cake soup."), F("조상님께 ___를 지냅니다. (a memorial service)", "차례", ["세배", "성묘"], "차례를 지내다."),
           F("어른들께 ___도 드립니다. (a bow)", "세배", ["차례", "성묘"], "세배를 드리다."), F("설은 한국의 ___ 큰 명절입니다. (the most)", "가장", ["벌써", "이미"], "가장 = the most."), F("설날에는 보통 ___를 가거나 전통 놀이를 합니다. (visiting graves)", "성묘", ["세배", "차례"], "성묘를 가다."),
           read_q("음력 일월 일일은 설입니다"), read_q("귀성객들로 붐빕니다"), read_q("조상님께 차례를 지내고"), read_q("세뱃돈을 주시면서"), read_q("떡국을 먹습니다")]
    ),
)

# ================================================================== L5: notes (세뱃돈, games, 객), Follow-up 2 and Activity 2
_GAMES = [("팽이치기", "top spinning (a favorite for boys, on a frozen river or pond)"), ("제기차기", "hacky sack (popular among boys; the winner is determined by the number of kicks without letting the 제기 hit the ground)"), ("연날리기", "kite flying (young boys and girls; dates back to the Shilla Dynasty)"), ("널뛰기", "seesaw jumping (young women; two people jump on the opposite ends of a long wooden board balanced on a folded bag of straw)"), ("그네뛰기", "swinging (young women)")]
_GAEK = [("승객", "a passenger; “riding guest” (the book’s example)"), ("관객", "a spectator; “viewing visitor” (the book’s example)"), ("고객", "a customer (the core vocabulary’s example; mine)"), ("여객기", "a passenger plane (mine)"), ("여객선", "a passenger ship (mine)"), ("객실", "a guest room (mine; 실 (室): a room)"), ("객지", "a place away from home (mine)")]
_ACTS = [("가족이 모여서 송편을 먹습니다.", "The family gathers and eats songpyeon."), ("어른들에게 세배를 합니다.", "They bow to the elders."), ("성묘 갑니다.", "They go to visit an ancestral grave."), ("여러 가지 전통놀이를 합니다.", "They play various traditional games."), ("조상님께 차례를 지냅니다.", "They hold a memorial service for the ancestors."), ("가족이 모여서 떡국을 먹습니다.", "The family gathers and eats rice cake soup.")]
_MY_ORDER = [("조상님께 차례를 지냅니다.", "1"), ("어른들에게 세배를 합니다.", "2"), ("가족이 모여서 떡국을 먹습니다.", "3"), ("성묘 갑니다.", "4"), ("여러 가지 전통놀이를 합니다.", "5"), ("가족이 모여서 송편을 먹습니다.", "(not a 설날 activity)")]
L5 = lesson(
    "Ch 23 · Topic B notes: New Year’s money, folk games, 객 (客) and Follow-up 2",
    "세뱃돈 · 팽이치기 · 제기차기 · 연날리기 · 널뛰기 · 그네뛰기 · 승객 · 관객",
    requires=[],
    cards=[
        card("Note 1: 세뱃돈",
             "세뱃돈 is the money people receive on 설날 when they bow to their parents or other older family members. 세뱃돈 is a compound noun made of 세배 and 돈."),
        card("Note 2: 전통민속놀이 (traditional folk games)",
             "There are several traditional outdoor games Koreans enjoy during the holiday seasons. 팽이치기 (top spinning) on a frozen river or pond is a favorite for boys. 제기차기 (hacky sack) is another popular game among boys. In 제기차기 contests, the winner is determined by the number of kicks made in succession without letting the 제기 (hacky sack) hit the ground. 연날리기 (kite flying) is a popular activity young boys and girls can enjoy, and it dates back to the Shilla Dynasty. For young women, games like 널뛰기 (seesaw jumping) and 그네뛰기 (swinging) are popular during the holiday seasons. In 널뛰기, two people stand on opposite ends of a long wooden board balanced on a tightly folded bag of straw and take turns jumping on their respective ends of the board.",
             tables=[table(["Game", "Meaning"], [list(r) for r in _GAMES], say=[0])]),
        card("Sino-Korean in use: 객 (客)",
             "The Sino-Korean syllable means guest or visitor, as in 승객 (a passenger; “riding guest”) and 관객 (a spectator; “viewing visitor”). The book asks you to guess the meaning of 여객기, 여객선, 객실 and 객지 (실 (室): a room). The answers are mine; 고객 is in the core vocabulary.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _GAEK], say=[0])]),
        card("Follow-up 2 (Listening and Reading): the six activities",
             "Follow-up 2 asks you to watch a video clip about a traditional Korean holiday, check the activities that occur in it and rank them in the order in which they occur. The six sentences are the book’s (the English is mine). The video is left out; the table below gives my order for 설날 from Topic B (not the video’s order):",
             examples=passage(_ACTS)),
        card("My order (mine)",
             "The book leaves the table blank; the video is not available here, so this is my order for the 설날 activities from Topic B (the songpyeon is for 추석).",
             tables=[table(["Activity", "Order (mine)"], [list(r) for r in _MY_ORDER], say=[0])]),
        card("Activities left out",
             "Follow-up 2’s video clip and the useful link (한국의 전통민속놀이 강강술래) are video and web activities; the book’s photos of the four games are pictures."),
    ],
    exercises=uniq(
        _tr(_GAMES + _GAEK + _ACTS)
        + [M("What is 세뱃돈?", "Money received on 설날 when bowing to elders", ["Money for rent", "A tip", "A salary"], "세배 + 돈."), M("Which game is top spinning?", "팽이치기", ["제기차기", "연날리기", "널뛰기"], "팽이치기 = top spinning."), M("Which game is hacky sack?", "제기차기", ["팽이치기", "그네뛰기", "연날리기"], "제기차기 = hacky sack."), M("Which game is kite flying?", "연날리기", ["널뛰기", "팽이치기", "그네뛰기"], "연날리기 = kite flying."),
           M("Which game is seesaw jumping?", "널뛰기", ["그네뛰기", "연날리기", "제기차기"], "널뛰기 = seesaw jumping."), M("Which game is swinging?", "그네뛰기", ["널뛰기", "팽이치기", "제기차기"], "그네뛰기 = swinging."), M("Which games are popular for young women?", "널뛰기 and 그네뛰기", ["팽이치기 and 제기차기", "연날리기 only", "제기차기 and 널뛰기 only for boys"], "For young women."),
           M("What does 객 (客) mean?", "a guest; a visitor", ["a season", "a room", "a ship"], "승객, 관객."), M("What does 승객 mean?", "a passenger; “riding guest”", ["a spectator", "a customer", "a guest room"], "승객 = a passenger."), M("What does 관객 mean?", "a spectator; “viewing visitor”", ["a passenger", "a customer", "a guide"], "관객 = a spectator."),
           F("두 사람이 ___를 합니다. (seesaw jumping)", "널뛰기", ["팽이치기", "연날리기"], "널뛰기."), F("얼음 위에서 ___를 합니다. (top spinning)", "팽이치기", ["그네뛰기", "널뛰기"], "팽이치기."), F("기차 ___이 많습니다. (passengers)", "승객", ["관객", "객지"], "승객 = passengers."),
           read_q("세뱃돈"), read_q("팽이치기"), read_q("제기차기"), read_q("연날리기"), read_q("전통민속놀이")]
    ),
)

# ================================================================== L6: Topic C
_C_DLG = [
    ("유나", "다음 주 월요일이 어버이날이네! 넌 어버이날에 부모님한테 뭐 해 드릴 거야?", "Next Monday is Parents’ Day! What will you do for your parents on Parents’ Day?"),
    ("진섭", "나는 부모님하고 외식할 거야. 너는 뭐 할 거야?", "I will eat out with my parents. What will you do?"),
    ("유나", "글쎄, 나는 아직 결정 못 했어. 올해는 좀 특별한 선물을 드리고 싶은데", "Well, I haven’t decided yet. This year I’d like to give them a somewhat special present, but…"),
    ("진섭", "그럼, 여행 보내 드려. 난 작년에 효도관광 보내 드렸었는데 부모님이 아주 좋아하셨어.", "Then send them on a trip. Last year I sent my parents on a filial piety vacation, and they liked it a lot."),
    ("유나", "그래, 그거 좋은 생각이다.", "Yes, that’s a good idea."),
    ("진섭", "그런데, 우리 스승의 날에 선생님한테 카드하고 꽃을 드리기로 했지?", "By the way, we decided to give our teacher a card and flowers on Teacher Appreciation Day, right?"),
    ("유나", "응. 카드는 내가 준비하기로 했어. 이번 주말에 카드 사러 갈 거야.", "Yes. I decided to prepare the card. I’m going to buy a card this weekend."),
    ("진섭", "그래? 그럼, 어린이날이 휴일이니까 그날 나랑 같이 사러 가자.", "Really? Then since Children’s Day is a holiday, let’s go buy it together that day."),
    ("유나", "어, 미안. 그날은 우리 조카들 데리고 놀이공원 가기로 했어.", "Oh, sorry. That day I decided to take my nephews and nieces to an amusement park."),
]
_C_WORDS = ["(결)정", "꽃", "글쎄", "놀이공원", "달다", "동물원", "생각", "스승의 날", "-았/었었", "어린이날", "어버이날", "장난감", "카드", "-지(요)", "효도관광"]
_MAY = [("어린이날", "Children’s Day"), ("어버이날", "Parents’ Day"), ("스승의 날", "Teacher Appreciation Day")]
_PA = [("어린이날", "Children’s Day"), ("놀이공원", "an amusement park"), ("효도관광", "“filial piety” (sightseeing)"), ("동물원", "a zoo"), ("휴가", "a vacation (the book’s blank; mine)"), ("장난감", "a toy"), ("스승의 날", "Teacher Appreciation Day"), ("어버이날", "Parents’ Day"), ("카드", "a card"), ("생각하다", "to think"), ("꽃", "a flower"), ("결정하다", "to decide"), ("특별하다", "to be special (mine)")]
L6 = lesson(
    "Ch 23 · Topic C: On Parents’ Day I’m going to send my parents on a vacation",
    "어버이날에 효도관광 보내 드릴 거야 · 스승의 날 · 어린이날 · 카드 · 꽃 · 놀이공원",
    requires=[],
    cards=[
        card("Topic C: On Parents’ Day I’m going to send my parents on a vacation (어버이날에 효도관광 보내 드릴 거야)",
             "Two friends are talking about special occasions that occur in May. The book shows a calendar for May with Children’s Day, Parents’ Day and Teacher Appreciation Day marked. (The English is mine; the book gives none. The book’s “결정 ____ 못 했어” and “카드하고 ____ 꽃을” have an underline where a picture is; I read them as “결정 못 했어” and “카드하고 꽃을”.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Cultural note: 효도 관광",
             "Korea has long been influenced by Confucianism, an ethical and philosophical belief system developed from the teachings of Confucius. According to Confucianism, filial piety (효 or 효도), a respect for parents and ancestors, is considered the most important virtue. Therefore, 효도 is prevalent in Korean society, and 효도 관광 (literally “filial piety sightseeing”) is one way adult children show respect to their parent(s) or grandparent(s). The children arrange a vacation for them and pay all the travel expenses. This is known as 효도관광, and many travel agencies offer various 효도관광 programs."),
        card("Presentation Activity a: the vocabulary table",
             "The book gives a table of the core words of Topic C with blanks to fill in, in both directions (Children’s Day, “filial piety”, a toy, a zoo, a vacation, a flower, to decide, 놀이공원, 스승의 날, 카드, 어버이날, 생각하다, 특별(하다)). The matching of the pairs is mine (the book leaves the blanks), except the core words:",
             tables=[ktable(_PA)]),
        card("Activities left out",
             "The SMART Board activity and the sentence strips (arranging the strips of Topic C in a logical order, with two numbered, and reading the dialog aloud in pairs as Yoonah and Jinsup) are computer and partner activities. Follow-up 1 is in the next lesson; Follow-up 2 (listening to three dialogs between a husband and wife about an occasion and what they will do) is an audio activity, and the useful link (서울대공원) is a web page."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not any(c in w for c in "~(-/")]))
        + _tr(_strip(_C_DLG) + _PA)
        + [M("What is the next Monday?", "Parents’ Day", ["Children’s Day", "Teacher Appreciation Day", "Christmas"], "다음 주 월요일이 어버이날."), M("What will Jinsup do with his parents on Parents’ Day?", "Eat out", ["Go on a trip", "Buy a present", "Stay home"], "부모님하고 외식할 거야."), M("What has Yoona not yet done?", "Decided on the present", ["Called her parents", "Booked a table", "Bought a card"], "아직 결정 못 했어."),
           M("What did Jinsup do last year?", "Sent his parents on a filial piety vacation", ["Gave cash", "Bought a toy", "Visited a zoo"], "작년에 효도관광 보내 드렸었는데."), M("What will they give their teacher on Teacher Appreciation Day?", "A card and flowers", ["A toy", "Cash", "A trip"], "카드하고 꽃을 드리기로 했지?"), M("Who will prepare the card?", "Yoona", ["Jinsup", "Their teacher", "Their parents"], "카드는 내가 준비하기로 했어."),
           M("Why can’t Yoona go to buy the card on Children’s Day?", "She will take her nephews and nieces to an amusement park", ["She has a test", "She is ill", "She will visit her parents"], "조카들 데리고 놀이공원."), M("What is 효도관광?", "A vacation for parents paid for by their children", ["A school trip", "A business trip", "A honeymoon"], "“filial piety sightseeing”."), M("What does Confucianism consider the most important virtue?", "Filial piety (효도)", ["Wealth", "Honesty", "Courage"], "The book’s cultural note."),
           F("나는 아직 ___ 못 했어. (decide)", "결정", ["생각", "기념"], "결정하다 = to decide."), F("카드하고 ___을 드리기로 했지? (flowers)", "꽃", ["장난감", "달력"], "꽃 = a flower."), F("어린이날이 ___이니까 같이 사러 가자. (a day off)", "휴일", ["명절", "국경일"], "휴일 = a day off."),
           F("난 작년에 효도관광 보내 드렸___ 부모님이 좋아하셨어. (used to; had)", "었는데", ["는데", "을 텐데"], "-았/었었는데: 드렸었는데."), F("그날은 놀이공원 가기___ 했어. (decided to)", "로", ["가", "를"], "-기로 하다 = to decide to."), F("그럼, 여행 보내 ___. (give; casual)", "드려", ["드렸어", "주세요"], "보내 드려 = send (for them)."),
           read_q("어버이날"), read_q("스승의 날"), read_q("효도관광"), read_q("놀이공원"), read_q("카드하고 꽃을 드리기로 했지")]
    ),
)

# ================================================================== L7: Follow-up 1 cards, Activity 3 article
_CARD1 = [("보고 싶은 박 선생님께,", "To Teacher Park, whom I miss,"), ("선생님, 그 동안 잘 지내셨어요?", "Teacher, have you been well all this time?"), ("선생님 수업시간이 아직도 생각나요.", "I still remember your class time."), ("선생님 시간은 늘 재미있었어요.", "Your lessons were always fun."), ("잘 가르쳐 주셔서 감사합니다.", "Thank you for teaching me well."),
          ("보고 싶어요. 다음 주에 선생님을 모시고 식사 한번 하고 싶어요.", "I miss you. Next week I would like to take you out for a meal once."), ("전화 드릴게요.", "I will call you."), ("제자 승민 올림", "Your student Seungmin")]
_CARD2 = [("정수야!", "Jungsu!"), ("어린이 날 축하해!", "Happy Children’s Day!"), ("엄마, 아빠가 늘 바빠서 많이 못 놀아줬지? 미안해.", "Mom and Dad are always busy, so we couldn’t play with you much, could we? We’re sorry."), ("그렇지만 엄마·아빠는 우리 정수를 많이 많이 사랑해.", "But Mom and Dad love our Jungsu very, very much."), ("우리 이번 어린이 날에는 어린이 대공원에 같이 가서 놀자.", "This Children’s Day, let’s go to the Children’s Grand Park together and play."), ("사랑해, 우리 아들!", "I love you, our son!"), ("엄마·아빠가", "From Mom and Dad")]
_CARD3 = [("엄마, 아빠", "Mom, Dad,"), ("늘 바빠서 부모님하고 같이 시간을 많이 못 보냈네요. 죄송해요.", "I have always been busy, so I couldn’t spend much time with my parents. I’m sorry."), ("올해는 엄마, 아빠 모시고 좋은 곳에 많이 갈게요.", "This year I will take you, Mom and Dad, to many nice places."), ("엄마, 아빠, 사랑해요!", "Mom, Dad, I love you!"), ("이번 어버이날에는 엄마, 아빠 모시고 좋은 식당에 가서 외식해요.", "This Parents’ Day, let’s take you, Mom and Dad, to a nice restaurant and eat out."), ("소정 올림", "From Sojeong")]
_SURVEY = [
    ("어버이날 선물은 현금이 최고", "Cash is the best Parents’ Day present"), ("한국사람들은 어버이날 부모님에게 어떤 선물을 드리고 싶을까?", "What kind of present do Korean people want to give their parents on Parents’ Day?"), ("그리고 어버이날 어떤 계획이 있을까?", "And what plans do they have for Parents’ Day?"),
    ("한 여론조사에 따르면 현금을 가장 선호한다고 한다.", "According to an opinion poll, they say they prefer cash most."), ("오백 명의 응답자 중 육십사 퍼센트가 어버이날 선물로 부모님에게 현금을 드리고 싶다고 했다.", "Of 500 respondents, 64% said they wanted to give their parents cash as a Parents’ Day present."),
    ("현금에 이어 건강식품 십육 퍼센트, 옷 칠 퍼센트, 꽃 사 퍼센트, 화장품 이 점 이 퍼센트, 넥타이 일 점 팔 퍼센트, 속옷 일 점 오 퍼센트, 상품권 일 점 삼 퍼센트, 여행상품 영 점 팔 퍼센트, 공연티켓 영 점 칠 퍼센트, 지갑 영 점 칠 퍼센트 등으로 조사됐다.", "After cash: health food 16%, clothes 7%, flowers 4%, cosmetics 2.2%, neckties 1.8%, underwear 1.5%, gift certificates 1.3%, travel packages 0.8%, performance tickets 0.7%, wallets 0.7% and so on."),
    ("어버이날 계획에 대해서는 응답자 오십이 점 일 퍼센트가 부모님과 함께 시간을 보내겠다고 응답했다.", "As for Parents’ Day plans, 52.1% of respondents answered that they would spend time with their parents."), ("응답자 이십구 점 구 퍼센트는 선물을 보내겠다고 답했고, 응답자 십오 점 삼 퍼센트는 부모님과 전화통화만 하겠다고 답했으며, 이 점 육 퍼센트는 아무것도 안 하겠다고 했다.", "29.9% of respondents answered that they would send a present, 15.3% answered that they would only talk with their parents by phone, and 2.6% said they would do nothing."),
]
_GIFTS = [("1", "현금", "cash"), ("2", "건강식품", "health food"), ("3", "옷", "clothes"), ("4", "꽃", "flowers"), ("5", "화장품", "cosmetics"), ("6", "넥타이", "neckties"), ("7", "속옷", "underwear (given in the book)"), ("8", "상품권", "gift certificates"), ("9", "여행상품", "travel packages"), ("10", "공연티켓", "performance tickets"), ("11", "지갑", "wallets")]
L7 = lesson(
    "Ch 23 · Topic C, Follow-up 1 and Activity 3: special occasion cards and a Parents’ Day survey",
    "스승의 날 카드 · 어린이날 카드 · 어버이날 카드 · 어버이날 선물은 현금이 최고",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): three special occasion cards",
             "The book shows three handwritten cards and asks you to identify the occasion and, in English, write the occasion and the suggested plans in a table. The book glosses 제자: a student, an apprentice, a disciple; 사랑(하다): love. The texts were read from the page image; the English is mine. Card 1:",
             examples=passage(_CARD1)),
        card("Card 2", "The second card (the English is mine):", examples=passage(_CARD2)),
        card("Card 3", "The third card (the English is mine):", examples=passage(_CARD3)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["", "Occasion", "Suggested plan"], [["1", "Teacher Appreciation Day (스승의 날)", "Take the teacher out for a meal next week; call to arrange it"], ["2", "Children’s Day (어린이날)", "Go to the Children’s Grand Park together and play"], ["3", "Parents’ Day (어버이날)", "Take the parents to a nice restaurant and eat out; take them to nice places this year"]])]),
        card("Activity 3 (Reading): a survey about Parents’ Day",
             "The book gives an article about the results of a survey on a Korean celebration and asks you to (a) skim it and identify the occasion, (b) list the 11 gift items in order of preference in English (one answer is given: underwear is no. 7), and (c) summarize in English the plans of the respondents (52.1%: spending time with parents, given). The text is the book’s (the figures are spelled out in Hangul); the English is mine.",
             examples=passage(_SURVEY)),
        card("The tables filled in (mine)",
             "The book leaves the tables blank except the two given answers; these are my answers.",
             tables=[table(["Rank", "Gift", "English (mine)"], [list(r) for r in _GIFTS], say=[1]), table(["% of respondents", "Plan for the occasion (mine)"], [["52.1%", "spending time with parents (given in the book)"], ["29.9%", "sending a present"], ["15.3%", "only talking with the parents by phone"], ["2.6%", "doing nothing"]])]),
        card("Activities left out",
             "Activity 2 (a video clip from the Korean TV drama 거침없이 하이킥 (MBC America) in which an elderly woman tells her housekeeper what her family members will do for her on Parents’ Day) is a video activity; Activity 1 is a SMART Board activity; Activity 4 (이날에는 무엇을 할까요?: reading three texts about occasions Koreans celebrate and discussing creative ideas, in groups) is a group activity whose texts are not in the book’s text."),
    ],
    exercises=uniq(
        _tr(_CARD1 + _CARD2 + _CARD3 + _SURVEY + [(g[1], g[2]) for g in _GIFTS])
        + [M("Which occasion is card 1 for?", "Teacher Appreciation Day", ["Children’s Day", "Parents’ Day", "Christmas"], "선생님께, 제자 승민 올림."), M("Which occasion is card 2 for?", "Children’s Day", ["Parents’ Day", "Teacher Appreciation Day", "Hangeul Day"], "어린이 날 축하해!"), M("Which occasion is card 3 for?", "Parents’ Day", ["Children’s Day", "Teacher Appreciation Day", "New Year’s Day"], "이번 어버이날에는."),
           M("What does the student want to do next week?", "Take the teacher out for a meal", ["Visit the school", "Send a gift", "Hold a party"], "다음 주에 선생님을 모시고 식사."), M("Where will Jungsu’s parents take him?", "The Children’s Grand Park", ["A zoo", "A school", "A museum"], "어린이 대공원에 같이 가서 놀자."), M("What does Sojeong suggest?", "Eating out at a nice restaurant with her parents", ["Sending a present", "Staying home", "Going to a zoo"], "좋은 식당에 가서 외식해요."),
           M("What present do most respondents want to give?", "Cash", ["Health food", "Flowers", "Clothes"], "현금을 가장 선호한다."), M("What percent want to give cash?", "64%", ["16%", "52.1%", "29.9%"], "오백 명의 응답자 중 육십사 퍼센트."), M("What is the second most popular gift?", "Health food (16%)", ["Clothes (7%)", "Flowers (4%)", "Cash"], "건강식품 십육 퍼센트."), M("How many respondents were there?", "500", ["50", "5,000", "64"], "오백 명의 응답자."),
           M("What percent will only call their parents?", "15.3%", ["52.1%", "29.9%", "2.6%"], "전화통화만 하겠다."), M("What percent will do nothing?", "2.6%", ["15.3%", "29.9%", "52.1%"], "아무것도 안 하겠다."),
           F("어버이날 선물은 ___이 최고 (cash)", "현금", ["꽃", "옷"], "현금 = cash."), F("올해는 엄마, 아빠 ___ 좋은 곳에 많이 갈게요. (take)", "모시고", ["데리고", "받고"], "모시다 = to attend a superior."), F("제자 승민 ___ (from, in a letter)", "올림", ["드림", "받음"], "올림 = respectfully yours."),
           read_q("어버이날 선물은 현금이 최고"), read_q("건강식품"), read_q("부모님과 함께 시간을 보내겠다"), read_q("어린이 날 축하해"), read_q("좋은 식당에 가서 외식해요")]
    ),
)

# ================================================================== L8: Grammar: indirectly quoted statements
def _bl_action(v):
    l, m, t = _K.decompose(stem(v)[-1])
    return (attr(v)[1] if t in ("", "ㄹ") else attr(v)[0]) + "다"


def _q_pres_a(v):
    return _bl_action(v) + "고 해요"


def _q_pres_s(v):
    return stem(v) + "다고 해요"


def _q_past(v):
    return past(v) + "다고 해요"


def _q_fut(v):
    return stem(v) + "겠다고 해요"


_Q_A = [("먹다", "to eat"), ("보다", "to see; to watch"), ("가다", "to go"), ("읽다", "to read"), ("마시다", "to drink"), ("공부하다", "to study"), ("좋아하다", "to like"), ("살다", "to live")]
_Q_S = [("예쁘다", "to be pretty"), ("크다", "to be big"), ("작다", "to be small"), ("좋다", "to be good"), ("비싸다", "to be expensive"), ("많다", "to be many")]
_Q_EX = [("한국말이 쉽다고 해요.", "(Someone) says that Korean is easy."), ("내일 비가 오겠다고 해요.", "(Someone) says that it will rain tomorrow."), ("마크 씨가 군인이라고 합니다.", "(Someone) says that Mark is a serviceman."), ("민재 씨가 의사가 아니라고 합니다.", "(Someone) says that Minjae is not a doctor."), ("김 선생님은 한국말이 쉽다고 해요.", "Mr. Kim says that Korean is easy."),
         ("김 일병이 매일 한국 드라마를 본다고 합니다.", "(Someone) says that PFC Kim watches a Korean soap opera every day."), ("신 선생님의 아기가 예쁘다고 합니다.", "(Someone) says that Mr. Shin’s baby is cute."), ("정수가 열심히 공부했다고 합니다.", "(Someone) says that Jungsoo studied hard."), ("정 이병이 자동차가 있다고 합니다.", "(Someone) says that PV2 Jung has a car."), ("그 컴퓨터는 비싼 것이라고 합니다.", "(Someone) says that the computer is an expensive one."),
         ("아버님은 오늘 늦게 오신다고 말했습니다.", "My father said that he will come late today. (the core vocabulary’s example)"), ("나는 미국이 크다고 생각해요.", "I think that America is big. (the book’s footnote on 고)"), ("신이 있다고 믿습니까?", "Do you believe that there is a god? (the book’s footnote on 고)")]
_Q_MODEL = [("한국말이 재미있습니다.", "Korean is interesting. (A)"), ("뭐라고요?", "What did he say? (B, playing a person who has a problem hearing)"), ("한국말이 재미있다고 합니다.", "He says that Korean is interesting. (C)")]
L8 = lesson(
    "Ch 23 · Grammar A: indirectly quoted statements with -다고 하다 / -라고 하다",
    "한국말이 쉽다고 해요 · 비가 오겠다고 해요 · 군인이라고 합니다 · 의사가 아니라고 합니다",
    requires=[],
    cards=[
        card("Expressing indirectly quoted statements",
             "In English, when we want to report or quote someone else’s statement indirectly, we normally use the phrase (the subject) says [that] …, as in He says [that] Korean is easy or My mom says [that] she is retiring next year. The presence of that can be optional.\n\n"
             "In Korean, when we want to report or quote someone’s statement indirectly, we use the phrase -다고 하다, which is the English equivalent of (the subject) says [that]. Note that the verb in each indirectly quoted statement ends in the formal blunt form -다. (Refer to the Grammar in Focus of Chapter 15 if you feel unfamiliar with the formal blunt form.) The statement is immediately followed by 고 하다, which can be interpreted as to say [that] …, to state [that] …, to comment [that] …, etc. 고 functions as an object marker and indicates that the quoted statement is the object of the verb 하다. (When a declarative clause becomes the object of a verb, it takes 고, not 을/를, as an object marker.)\n\n"
             "When an indirectly quoted statement ends with the verb 이다 or 아니다, however, -다고 하다 changes to -라고 하다.",
             examples=passage(_Q_EX[:4])),
        card("Who says it",
             "Keep in mind that the speaker who is reporting the indirectly quoted statement is usually not named. If you want to be sure the listener understands who the reporting speaker is, you can express it as follows:",
             examples=passage(_Q_EX[4:5])),
        card("The rule: formal blunt form + 고 하다",
             "In the book’s table (the arrows show the change).",
             tables=[table(["Condition", "Rule", "Example"], [["When the quoted statement ends in a verb other than 이다 and 아니다", "add 고 하다", "… 먹는다 → … 먹는다고 하다"], ["When the quoted statement ends with the verb 이다 or 아니다", "change 다 to 라 and add 고 하다", "… 군인이다 → … 군인이라고 하다; … 군인이 아니다 → … 군인이 아니라고 하다"]])],
             examples=passage(_Q_EX[5:10])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (the formal blunt form: an action verb takes ㄴ다/는다, a stative verb takes 다, the past takes 았/었다, and the future takes 겠다).",
             tables=[table(["Action verb", "Meaning", "present", "past", "future"], [[v, m, _q_pres_a(v), _q_past(v), _q_fut(v)] for v, m in _Q_A], say=[0, 2, 3, 4]), table(["Stative verb", "Meaning", "present", "past"], [[v, m, _q_pres_s(v), _q_past(v)] for v, m in _Q_S], say=[0, 2, 3])]),
        card("More examples and the Follow-up 1 model",
             "The core vocabulary’s example and the footnote’s examples with 고, and the model of Follow-up 1 (What does he say?), in which a group of three plays a game: Student A makes a statement, Student B pretends to have a problem hearing and asks Student C what the statement was, and Student C reports it using -다고 합니다:",
             examples=passage(_Q_EX[10:] + _Q_MODEL)),
        card("Activities left out",
             "Follow-up 1 (a group game), Follow-up 4 (“Spread the Rumor!”, a team game) are group and class activities; Follow-up 2 and 3 are in the next lesson."),
    ],
    exercises=uniq(
        _fk(_Q_A, _q_pres_a, "present (says that … does)", lambda v: [stem(v) + "다고 해요" if has_final(stem(v)) else stem(v) + "ㄴ다고 해요", _q_past(v), _q_fut(v), attr(v)[0] + "고 해요"])
        + _fk(_Q_A, _q_past, "past (says that … did)", lambda v: [_q_pres_a(v), stem(v) + "었다고 해요" if past(v).endswith("었") else stem(v) + "았다고 해요", _q_fut(v), stem(v) + "다고 했어요"])
        + _fk(_Q_S, _q_pres_s, "present (says that … is)", lambda v: [attr(v)[1] + "다고 해요", attr(v)[0] + "고 해요", _q_past(v), _q_fut(v)])
        + _tr(_Q_EX + _Q_MODEL)
        + [F("한국말이 쉽___ 해요. (says that)", "다고", ["라고", "고"], "쉽다 + 다고 하다."), F("마크 씨가 군인이___ 합니다. (says that)", "라고", ["다고", "고"], "이다 → 라고 하다."), F("민재 씨가 의사가 아니___ 합니다. (says that)", "라고", ["다고", "고"], "아니다 → 아니라고 하다."), F("내일 비가 오겠___ 해요. (says that)", "다고", ["라고", "는다고"], "오겠다고 하다."),
           F("정수가 열심히 공부했___ 합니다. (says that)", "다고", ["는다고", "라고"], "공부했다고 하다."), F("김 일병이 한국 드라마를 본___ 합니다. (says that, present)", "다고", ["는다고", "라고"], "보다 → 본다 + 고 하다."), F("정 이병이 자동차가 있___ 합니다. (says that)", "다고", ["는다고", "라고"], "있다고 하다."),
           M("What does -다고 하다 mean?", "(the subject) says that …", ["wants to …", "must …", "has finished …"], "한국말이 쉽다고 해요."), M("What does 고 function as in -다고 하다?", "An object marker for the quoted statement", ["A subject marker", "A time marker", "A question marker"], "The book’s explanation."), M("Which ending is used after 이다 and 아니다?", "-라고 하다", ["-다고 하다", "-는다고 하다", "-겠다고 하다"], "군인이라고, 의사가 아니라고."),
           M("Is the reporting speaker usually named?", "No", ["Yes, always", "Only in questions", "Only in the past"], "Usually not named."), M("Which question did Student B ask in the game?", "뭐라고요?", ["어디예요?", "누구예요?", "언제예요?"], "What did he say?"),
           read_q("한국말이 쉽다고 해요"), read_q("내일 비가 오겠다고 해요"), read_q("군인이라고 합니다"), read_q("의사가 아니라고 합니다"), read_q("매일 한국 드라마를 본다고 합니다")]
    ),
)

# ================================================================== L9: -다고 하다 follow-ups
_S2 = [("상미의 옷이 너무 큽니다.", "상미의 옷이 너무 크다고 합니다.", "Sangmi’s clothes are too big."), ("박 상병이 지난 토요일에 도서관에 갔습니다.", "박 상병이 지난 토요일에 도서관에 갔다고 합니다.", "Corporal Park went to the library last Saturday."), ("정우가 지난 주말에 한국에 갔어요.", "정우가 지난 주말에 한국에 갔다고 해요.", "Jungwoo went to Korea last weekend."), ("내일 기욱이하고 공부를 할 거예요.", "내일 기욱이하고 공부를 할 거라고 해요.", "I will study with Giuk tomorrow."),
       ("윤선이가 커피를 좋아합니다.", "윤선이가 커피를 좋아한다고 합니다.", "Yunsun likes coffee."), ("내일은 비가 오겠습니다.", "내일은 비가 오겠다고 합니다.", "It will rain tomorrow."), ("선영이가 책을 읽고 있습니다.", "선영이가 책을 읽고 있다고 합니다.", "Seonyoung is reading a book."), ("정 병장은 형이 없습니다.", "정 병장은 형이 없다고 합니다.", "Sergeant Jung has no older brother."),
       ("재민 씨는 의사가 아닙니다.", "재민 씨는 의사가 아니라고 합니다.", "Jaemin is not a doctor."), ("민지의 취미는 수영입니다.", "민지의 취미는 수영이라고 합니다.", "Minji’s hobby is swimming.")]
_NEWS1 = [("오늘 기아와 엘지의 야구 경기가 열렸습니다.", "Today a baseball game between Kia and LG was held."), ("이 경기에서 기아의 이종범 선수가 이 점 홈런을 쳤습니다.", "In this game Kia’s player Lee Jong-beom hit a two-run home run."), ("그래서 기아는 엘지를 칠 대 오로 이겼습니다.", "So Kia beat LG 7 to 5."), ("기아는 지금까지 사 승 일 패입니다.", "Kia is 4 wins and 1 loss so far.")]
_NEWS2 = [("오늘 기아와 엘지의 야구 경기가 열렸다고 합니다.", "They say that a baseball game between Kia and LG was held today."), ("이 경기에서 기아의 이종범 선수가 이 점 홈런을 쳤다고 합니다.", "They say that in this game Kia’s player Lee Jong-beom hit a two-run home run."), ("그래서 기아는 엘지를 칠 대 오로 이겼다고 합니다.", "They say that Kia beat LG 7 to 5."), ("기아는 지금까지 사 승 일 패라고 합니다.", "They say that Kia is 4 wins and 1 loss so far.")]
L9 = lesson(
    "Ch 23 · Grammar A follow-ups: changing sentences and quoting the news",
    "상미의 옷이 너무 크다고 합니다 · 정 병장은 형이 없다고 합니다 · 기아는 엘지를 이겼다고 합니다",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading and Writing): change the sentences into indirectly quoted statements",
             "The book gives ten sentences and asks you to change each into an indirectly quoted statement using -다고 하다 or -라고 하다. The sentences are the book’s; the answers are mine (the book leaves the blanks); the English is mine.",
             tables=[table(["Sentence", "Indirectly quoted (mine)", "Meaning (mine)"], [list(r) for r in _S2], say=[0, 1])]),
        card("Follow-up 3: the sports news (the audio is left out)",
             "The book gives a sports news segment with four blanks for the audio, and asks you to transcribe the missing words and then change all the verbs to -다고 하다 or -라고 하다, as if quoting the news. The audio is not available here, so the missing words below are my reconstruction (the book’s text writes LG, 2점, 7대 5 and 4승 1패, which are respelled in Hangul). My reconstruction of the sentences:",
             examples=passage(_NEWS1)),
        card("Quoting the news (mine)",
             "My answers for Follow-up 3b (the verbs changed to -다고 하다 or -라고 하다):",
             examples=passage(_NEWS2)),
        card("Activities left out",
             "Follow-up 3a (listening and transcribing the missing words) is an audio activity; Follow-up 4 (“Spread the Rumor!”) is a team game. Activity 1 (윷놀이: the teacher clicks the icon to start the activity) is a computer activity."),
    ],
    exercises=uniq(
        _tr([(a, c) for a, b, c in _S2] + [(b, c) for a, b, c in _S2] + _NEWS1 + _NEWS2)
        + [M(f"Which is the indirectly quoted form of ‘{a}’?", b, [x[0] for x in _S2 if x[0] != a][:3], f"{a} → {b}.") for a, b, c in _S2]
        + [F("정 병장은 형이 ___ 합니다. (says he has none)", "없다고", ["없는다고", "없라고"], "없다 + 고 하다."), F("민지의 취미는 수영이___ 합니다. (says it is)", "라고", ["다고", "는다고"], "이다 → 라고."), F("윤선이가 커피를 좋아한___ 합니다. (says she likes)", "다고", ["라고", "는다고"], "좋아하다 → 좋아한다고."),
           F("내일은 비가 오겠___ 합니다. (says it will rain)", "다고", ["라고", "는다고"], "오겠다고 하다."), F("기아는 지금까지 사 승 일 ___라고 합니다. (loss)", "패", ["승", "점"], "승 = win; 패 = loss."),
           M("Who won the game according to the news?", "Kia", ["LG", "It was a draw", "Neither"], "기아는 엘지를 칠 대 오로 이겼다."), M("What was the score?", "7 to 5", ["5 to 7", "4 to 1", "2 to 0"], "칠 대 오."), M("What did Lee Jong-beom hit?", "A two-run home run", ["A triple", "A single", "A bunt"], "이 점 홈런을 쳤다."),
           read_q("상미의 옷이 너무 크다고 합니다"), read_q("정 병장은 형이 없다고 합니다"), read_q("재민 씨는 의사가 아니라고 합니다"), read_q("민지의 취미는 수영이라고 합니다"), read_q("기아는 엘지를 칠 대 오로 이겼다고 합니다")]
    ),
)

# ================================================================== L10: Grammar B: -지요 tag questions
def _jiyo(v):
    return stem(v) + "지요"


def _jyo(v):
    return stem(v) + "죠"


def _ji(v):
    return stem(v) + "지"


def _jiyo_p(v):
    return past(v) + "지요"


_JY_V = [("좋다", "to be good"), ("가다", "to go"), ("쉽다", "to be easy"), ("살다", "to live"), ("먹다", "to eat"), ("재미있다", "to be entertaining"), ("오다", "to come"), ("공부하다", "to study")]
_JY_EX = [("오늘 날씨가 좋지요?", "Today’s weather is good, isn’t it?"), ("오늘 날씨가 좋죠?", "Today’s weather is good, isn’t it?"), ("한국말이 쉽지 않지요?", "Korean is not easy, is it?"), ("한국말이 쉽지 않죠?", "Korean is not easy, is it?"), ("오늘 날씨가 좋지?", "Today’s weather is good, isn’t it? (among friends)"), ("한국말이 쉽지 않지?", "Korean is not easy, is it? (among friends)"),
          ("내일 뉴욕에 가지요?", "You are going to New York tomorrow, aren’t you?"), ("내일 뉴욕에 가죠?", "You are going to New York tomorrow, aren’t you?"), ("내일 뉴욕에 가지?", "You are going to New York tomorrow, aren’t you? (among friends)"),
          ("내일 한국에 가시죠?", "You are going to Korea tomorrow, right?"), ("오월 오일은 어린이날이죠?", "May 5th is Children’s Day, isn’t it?"), ("한국 음식 먹어 봤지요?", "You have tried Korean food, haven’t you?"), ("이 영화 정말 재미있죠?", "This movie is really entertaining, isn’t it?"), ("김 일병이 기숙사에 살지?", "PFC Kim lives in a dorm, doesn’t he?"), ("한국말이 쉽지?", "Korean is easy, isn’t it?"),
          ("선생님 댁이 여기서 가깝지요?", "Teacher’s home is close from here, isn’t it? (the core vocabulary’s example)")]
_JY_MODEL = [("어제 친구를 방문하다", "(the cue) to visit a friend yesterday"), ("어제 친구를 방문했지요?", "You visited a friend yesterday, didn’t you?"), ("어제 친구를 방문했죠?", "You visited a friend yesterday, didn’t you?"), ("어제 친구를 방문했지?", "You visited a friend yesterday, didn’t you? (among friends)")]
L10 = lesson(
    "Ch 23 · Grammar B: asking for confirmation or seeking agreement with -지요",
    "오늘 날씨가 좋지요? · 좋죠? · 좋지? · 어제 친구를 방문했지요?",
    requires=[],
    cards=[
        card("Asking for confirmation or seeking agreement",
             "In English, we use a tag question to ask for confirmation or to seek agreement, as in “It’s a beautiful day, isn’t it?” and “You are going to New York this summer, aren’t you?”\n\n"
             "In Korean, we use the verb ending -지요 or -죠 (abbreviated form of 지요) to ask for confirmation or to seek agreement. 요 in 지요 is omitted by people who do not maintain social distance. If we were to use the above expressions among friends, the verb ending is shortened to -지.",
             examples=passage(_JY_EX[:6])),
        card("The rule",
             "-지요? or -죠?",
             tables=[table(["Condition", "Rule", "Example"], [["When creating a tag question and social distance needs to be maintained", "use -지요", "1. 오늘 날씨가 좋지요? 2. 내일 뉴욕에 가지요?"], ["To form a contraction of -지요", "use -죠", "1. 오늘 날씨가 좋죠? 2. 내일 뉴욕에 가죠?"], ["When social distance does NOT need to be maintained", "use -지 (요 is dropped from -지요)", "1. 오늘 날씨가 좋지? 2. 내일 뉴욕에 가지?"]])],
             examples=passage(_JY_EX[6:9])),
        card("More examples",
             "The book’s examples (the book writes 5월 5일; it is spelled out here) and the core vocabulary’s example:",
             examples=passage(_JY_EX[9:])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (with the past tense, add 지요 after 았/었: 방문했지요).",
             tables=[table(["Verb", "Meaning", "-지요", "-죠", "-지", "past -았/었지요"], [[v, m, _jiyo(v), _jyo(v), _ji(v), _jiyo_p(v)] for v, m in _JY_V], say=[0, 2, 3, 4, 5])]),
        card("Follow-up 1: the model",
             "In Follow-up 1 Partner A reads a verb phrase from List A and Partner B turns it into a tag question, adding the appropriate tense (the lists are not in the book’s text). The book’s model:",
             examples=passage(_JY_MODEL)),
        card("Activities left out",
             "Follow-up 1 is a partner activity; Follow-up 2 (listening to three conversations between co-workers and translating the female speaker’s tag question) is an audio activity."),
    ],
    exercises=uniq(
        _fk(_JY_V, _jiyo, "-지요 (…, isn’t it?)", lambda v: [stem(v) + "죠", stem(v) + "지", stem(v) + "을까요", stem(v) + "네요"])
        + _fk(_JY_V, _jyo, "-죠 (contraction)", lambda v: [stem(v) + "지요", stem(v) + "지", stem(v) + "을까요", stem(v) + "네요"])
        + _fk(_JY_V, _jiyo_p, "past -았/었지요", lambda v: [_jiyo(v), stem(v) + "았지요" if past(v).endswith("었") else stem(v) + "었지요", past(v) + "어요", past(v) + "죠"])
        + _tr(_JY_EX + _JY_MODEL)
        + [F("오늘 날씨가 좋___? (isn’t it?)", "지요", ["지만", "고"], "좋다 + 지요."), F("내일 뉴욕에 가___? (contraction of 지요)", "죠", ["지요", "고요"], "가다 + 죠."), F("한국말이 쉽___? (among friends)", "지", ["지요", "죠"], "요 is dropped among friends."), F("한국 음식 먹어 ___? (you have tried, haven’t you?)", "봤지요", ["보지요", "봤어요"], "먹어 보다 + 았 + 지요."),
           F("어제 친구를 방문___? (you visited, didn’t you?)", "했지요", ["하지요", "할지요"], "방문하다 past + 지요."), F("오월 오일은 어린이날이___? (isn’t it?)", "죠", ["지요요", "고"], "이다 + 죠."),
           M("What is -지요 used for?", "To ask for confirmation or to seek agreement", ["To give an order", "To express a wish", "To quote someone"], "A tag question."), M("What is -죠?", "A contraction of -지요", ["A past tense", "A command", "A question word"], "지요 → 죠."), M("When is -지 used instead of -지요?", "When social distance does not need to be maintained", ["When speaking to a superior", "In writing only", "In the past only"], "요 is dropped among friends."),
           read_q("오늘 날씨가 좋지요"), read_q("내일 뉴욕에 가죠"), read_q("한국말이 쉽지 않지요"), read_q("한국 음식 먹어 봤지요"), read_q("김 일병이 기숙사에 살지")]
    ),
)

# ================================================================== L11: Grammar C: -았었 "used to"
def _ssoss(v):
    return past(v) + "었어요"


_US_V = [("마시다", "to drink"), ("읽다", "to read"), ("살다", "to live"), ("오다", "to come"), ("수영하다", "to swim"), ("먹다", "to eat"), ("보내다", "to spend; to send"), ("좋아하다", "to like"), ("가다", "to go"), ("공부하다", "to study")]
_US_EX = [("호텔 수영장에서 수영했었어요.", "I used to swim in the hotel swimming pool (but I no longer do that)."), ("날씨가 좋았었어요.", "The weather used to be good (but is not any more)."), ("여기에 극장이 있었어요.", "There was a theater here or There used to be a theater here."), ("여기에 극장이 있었었어요.", "There used to be a theater here. (the book’s contrast)"),
          ("어렸을 때 하와이에 살았었어요.", "I used to live in Hawaii when I was young."), ("김 일병이 사무실에 왔었어요.", "PFC Kim visited the office. (But now he is gone)."), ("채소를 잘 안 먹었었어요.", "I used to not eat vegetables very often."), ("책을 많이 읽었었어요.", "I used to read books a lot."),
          ("전에는 이 학교가 아주 컸었어요.", "This school used to be very big before. (the core vocabulary’s example)"), ("난 작년에 효도관광 보내 드렸었는데 부모님이 아주 좋아하셨어.", "Last year I sent my parents on a filial piety vacation, and they liked it a lot. (Topic C)")]
_US_MODEL = [("커피를 마시다", "(the cue) to drink coffee"), ("커피를 마셨었어요.", "I used to drink coffee."), ("술을 많이 마셨었어요.", "I used to drink a lot of alcohol. (the book’s model)"), ("책을 안 읽었었어요.", "I didn’t use to read books. (the book’s model)"), ("술을 많이 마셨었지요?", "You used to drink a lot, didn’t you? (A)"), ("네, 많이 마셨었어요.", "Yes, I used to drink a lot. (B)"), ("아니요, 안 마셨었어요.", "No, I didn’t. (B)"),
             ("책을 안 읽었었지요?", "You didn’t use to read books, did you? (A)"), ("네, 안 읽었었어요.", "Yes, I didn’t use to read. (B)"), ("아니요, 읽었었어요.", "No, I did read. (B)"), ("우리 반에서 김 일병하고 박 일병은 술을 많이 마셨었어요.", "In our class PFC Kim and PFC Park used to drink a lot. (the report model)")]
L11 = lesson(
    "Ch 23 · Grammar C: “used to” with -았었 / -었었",
    "수영했었어요 · 하와이에 살았었어요 · 책을 많이 읽었었어요 · 입대 전에 게임을 많이 했었지요",
    requires=[],
    cards=[
        card("Expressing “used to”",
             "In English, the expression “used to + verb” implies past actions that no longer occur or past conditions that no longer exist. For example: I used to eat at the chow hall (but I no longer eat there); My brother used to be nice to his girlfriend (but he is no longer nice to her).\n\n"
             "In Korean, adding the syllable 었 to a past tense verb takes care of this. Note that 었 is inserted between the past tense marker 았/었 and the verb ending 어요.",
             examples=passage(_US_EX[:2])),
        card("Stative verbs and 이다, 아니다, 있다, 없다",
             "However, the past tense of stative verbs (e.g., 좋다, 예쁘다, 춥다) and the past tense of the verbs 이다, 아니다, 있다 and 없다 can also imply that past conditions no longer exist. Thus, depending on the context, 날씨가 좋았어요 can simply mean “The weather was good” or “The weather used to be good (but is not any more).”",
             examples=passage(_US_EX[2:4])),
        card("The rule",
             "verb stem + past tense marker 았/었 + 었 (+ 어요).",
             tables=[table(["Pattern", "Example"], [["verb stem + 았었 / 었었", "수영하다 → 수영했었어요; 살다 → 살았었어요"]])],
             examples=passage(_US_EX[4:8])),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Verb", "Meaning", "-았었어요 / -었었어요"], [[v, m, _ssoss(v)] for v, m in _US_V], say=[0, 2])]),
        card("More examples and the models of Follow-up 3 and 5",
             "The core vocabulary’s example and the example from Topic C, and the models of Follow-up 3 (changing a verb phrase into one with -았었 or -었었 and translating it) and Follow-up 5 (입대 전에 게임을 많이 했었지요?: asking and answering about what you used to do or did not use to do before enlisting). The English is mine.",
             examples=passage(_US_EX[8:] + _US_MODEL)),
        card("Activities left out",
             "Follow-up 3 and 5 (partner and class activities) and Follow-up 4 (listening to what Youngsoo used to do at his birthday) are partner and audio activities; Activity 1 is a SMART Board activity."),
    ],
    exercises=uniq(
        _fk(_US_V, _ssoss, "-았었어요 / -었었어요 (used to)", lambda v: [past(v) + "어요", stem(v) + "었어요", stem(v) + "았어요", past(v) + "었지요"])
        + _tr(_US_EX + _US_MODEL)
        + [F("호텔 수영장에서 수영했___어요. (used to)", "었", ["겠", "는"], "수영했었어요."), F("어렸을 때 하와이에 살았___어요. (used to)", "었", ["겠", "는"], "살았었어요."), F("채소를 잘 안 먹었___어요. (used to not)", "었", ["겠", "는"], "먹었었어요."),
           F("책을 많이 읽었___어요. (used to)", "었", ["겠", "는"], "읽었었어요."), F("전에는 이 학교가 아주 컸___어요. (used to be)", "었", ["겠", "는"], "컸었어요."), F("술을 많이 마셨었___? (you used to, didn’t you?)", "지요", ["지만", "고"], "-았었 + 지요."),
           M("What does -았었/-었었 imply?", "A past action or state that no longer holds", ["A future plan", "A guess", "A command"], "I used to …"), M("What is added to a past tense verb to express “used to”?", "었", ["겠", "는", "지"], "Past marker + 었."), M("Can 날씨가 좋았어요 mean “used to be good”?", "Yes, depending on the context", ["Never", "Only with 었었", "Only in the future"], "Stative verbs can imply past conditions."),
           M("What does 김 일병이 사무실에 왔었어요 imply?", "He visited the office and is now gone", ["He is still there", "He will come", "He never came"], "왔었어요."),
           read_q("수영했었어요"), read_q("하와이에 살았었어요"), read_q("채소를 잘 안 먹었었어요"), read_q("책을 많이 읽었었어요"), read_q("술을 많이 마셨었지요")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Korean celebration days and holidays", _CV_DAYS), ("Celebration-related words", _CV_CELEB), ("Traditional holiday-related words", _CV_TRAD), ("Calendar", _CV_CAL), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not any(c in r[0] for c in "~(-/")]
L12 = lesson(
    "Ch 23 · Core vocabulary and self-evaluation",
    "주요 단어 · 국경일 · 기념 · 전통 명절 · 달력 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning.\n\n"
             "The example sentences with digits are respelled in Hangul (1947년 → 천구백사십칠 년, 10월 9일 → 시월 구일, 7월 → 칠월, 12월 25일 → 십이월 이십오일, 8월 15일 → 팔월 십오일, 11월 → 십일월, 3월 → 삼월); the quotation marks of 스승의 날 are left out. The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and talk about important Korean holidays and observances; identify and talk about activities done on traditional Korean holidays; and express gratitude to teachers and parents.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -지요 used to ask for confirmation or seek agreement; -았었다 or -었었다 (used to [do/not do something]); -다고 하다 or -라고 하다 used to quote indirectly; and the Sino-Korean syllables 객 (客) and 절 (節)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does -지요 do?", "Asks for confirmation or seeks agreement", ["Quotes indirectly", "Says “used to”", "Makes an interrogative clause"], "선생님 댁이 여기서 가깝지요?"), M("What does -았/었었 mean?", "used to (do something)", ["says that", "isn’t it", "in order to"], "전에는 이 학교가 아주 컸었어요."), M("What does -다고/라고 (말)하다 mean?", "to say that …; to tell that …", ["used to", "isn’t it", "in order to"], "늦게 오신다고 말했습니다."),
           M("What is “a lunar calendar”?", "음력", ["양력", "달력", "새해"], "음력 = a lunar calendar."), M("What is “a solar calendar”?", "양력", ["음력", "달력", "중순"], "양력 = a solar calendar."), M("What is “the beginning of the month”?", "초순", ["중순", "~말", "새해"], "초순 = the beginning of the month."), M("What is “a memorial service for an ancestor”?", "차례", ["세배", "성묘", "떡국"], "차례 = a memorial service."),
           M("What is “a formal bow of respect to one’s elders”?", "세배", ["차례", "성묘", "송편"], "세배 = a formal bow."), M("What is “a zoo”?", "동물원", ["놀이공원", "식물원", "공원"], "동물원 = a zoo."), M("What is “a toy”?", "장난감", ["카드", "꽃", "선물"], "장난감 = a toy.")]
        + [read_q("주요 단어"), read_q("한국의 명절과 기념일"), read_q("부처님오신날"), read_q("스승의 날"), read_q("새해 복 많이 받으세요")]
    ),
)

UNIT = unit("Semester 1 · Unit 6 · Chapter 23: Traditional Korean Holidays and Observances (한국의 명절과 기념일)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])

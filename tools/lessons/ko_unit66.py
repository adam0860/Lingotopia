"""Unit 66: KBC Semester III, Unit 16, Lesson 1 - Leisure and Sports (여가와 스포츠).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 16, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_SORT = [("음악회", "a concert", "문화공연"), ("뮤지컬", "a musical", "문화공연"), ("발레", "ballet", "문화공연"), ("전시회", "an exhibition", "문화공연"), ("무용", "dance", "문화공연"),
         ("주연배우", "a leading actor", "영화"), ("조조할인", "a morning-show discount", "영화"), ("촬영", "filming; shooting", "영화"), ("상영", "a screening", "영화"), ("액션", "action", "영화"),
         ("낚시", "fishing", "스포츠/레저"), ("등산", "mountain climbing", "스포츠/레저"), ("당구", "billiards", "스포츠/레저"), ("권투", "boxing", "스포츠/레저"), ("육상", "track and field", "스포츠/레저")]
_SYN = [("등산", "등반", "mountain climbing"), ("승리하다", "이기다", "to win"), ("티켓", "표", "a ticket"), ("지다", "패배하다", "to lose"), ("비기다", "무승부", "to draw; a draw"), ("동호회", "동아리", "a club of people with a shared hobby"), ("복싱", "권투", "boxing"), ("판매하다", "팔다", "to sell"), ("나이", "연령", "age"), ("관객", "관중", "an audience")]
_HJ1 = [("勝 승", "win; victory", "승리, 승자"), ("觀 관", "view; look", "관객, 관광"), ("賣 매", "sell", "매진, 매장"), ("演 연", "perform", "연극, 조연"), ("映 영", "light; reflection", "영화, 종영")]
_HJW1 = [("승리", "victory"), ("승자", "a winner"), ("관객", "an audience"), ("관광", "a tour; sightseeing"), ("매진", "a sellout"), ("매장", "a shop; a department"), ("연극", "a play"), ("조연", "a supporting actor"), ("영화", "a movie"), ("종영", "ending (of a movie, TV show, etc.)")]
_OPP1 = [("승리", "패배", "victory: defeat"), ("판매", "구매", "selling: buying"), ("종영", "상영", "ending a run: screening"), ("공연", "관람", "performing: watching")]
_BOX1 = [("승자, 무승부, 패자", "승패", "a winner, a draw, a loser: win or lose"), ("매표, 예매, 매진", "판매", "ticket selling, advance sales, a sellout: sale"), ("극장, 촬영, 상영", "영화", "a theater, filming, a screening: a movie"), ("연극, 영화, 운동경기", "관람", "a play, a movie, a sports game: watching")]
_L1X = [("결승", "the finals"), ("승패", "win or loss"), ("우승", "winning a championship"), ("예매", "advance booking"), ("구매", "buying"), ("매표", "ticket selling"), ("반영", "reflection"), ("연주", "a performance (music)"), ("연기", "acting"), ("관람", "watching (a show)"), ("무승부", "a draw"), ("패자", "a loser"), ("운동경기", "a sports game"), ("패배", "defeat"), ("게임", "a game"), ("악기", "a musical instrument")]
L1 = lesson(
    "U16 L1 · Review: leisure words and Sino-Korean 勝 觀 賣 演 映",
    "여가와 스포츠 · 단어 복습 · 한자어 복습 · 음악회 · 뮤지컬 · 낚시 · 등산 · 권투 · 상영 · 동호회 · 勝 觀 賣 演 映",
    requires=[],
    cards=[
        card("단어 복습 1: sorting the words (my answers)", "The book gives fifteen words and asks which of three groups each is related to (문화공연 = cultural performance, 영화 = movie, 스포츠/레저 = sports and leisure). My answers:", tables=[table(["Group", "Words"], [["문화공연", "음악회, 뮤지컬, 발레, 전시회, 무용"], ["영화", "주연배우, 조조할인, 촬영, 상영, 액션"], ["스포츠/레저", "낚시, 등산, 당구, 권투, 육상"]], say=[0, 1]), ktable([(a, b) for a, b, c in _SORT])]),
        card("단어 복습 2: words with a similar meaning", "The book asks you to connect each word on the left with the word of similar meaning on the right. The pairs:", tables=[table(["Word", "Similar word", "Meaning"], [list(r) for r in _SYN], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ1], say=[2]), ktable(_HJW1)]),
        card("한자어 복습 1: the word with the opposite meaning (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 승리: 결승, 승패, 우승, 패배; B. 판매: 매장, 예매, 구매, 매표; C. 종영: 반영, 촬영, 상영, 영화; D. 공연: 연주, 연기, 관람, 관객).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP1], say=[0, 1])]),
        card("한자어 복습 2: the word that fits the three words (my answers)", "Choose from the box (승패, 게임, 판매, 영화, 관람, 악기) the word most closely related to the three words on each line:", tables=[table(["The three words", "The word from the box (my answer)", "Meaning"], [list(r) for r in _BOX1], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L1X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _SORT], k=3) + _tr([(a, c) for a, b, c in _SYN], k=3) + _tr(_HJW1, k=3) + _tr(_L1X, k=3)
        + [M("What does the syllable 勝 (승) mean?", "win; victory", ["sell", "perform", "view"], "승리."), M("What does the syllable 觀 (관) mean?", "view; look", ["win", "sell", "perform"], "관객."), M("What does the syllable 賣 (매) mean?", "sell", ["win", "view", "perform"], "매진."), M("What does the syllable 演 (연) mean?", "perform", ["win", "view", "sell"], "연극."), M("What does the syllable 映 (영) mean?", "light; reflection", ["win", "sell", "perform"], "영화."),
           M("Which group does 뮤지컬 belong to?", "문화공연", ["영화", "스포츠/레저", "음식"], "A musical."), M("Which group does 조조할인 belong to?", "영화", ["문화공연", "스포츠/레저", "교통"], "A morning-show discount."), M("Which group does 당구 belong to?", "스포츠/레저", ["문화공연", "영화", "교육"], "Billiards."),
           M("Which word is the opposite of 승리?", "패배", ["결승", "승패", "우승"], "Defeat."), M("Which word is the opposite of 판매?", "구매", ["매장", "예매", "매표"], "Buying."), M("Which word is the opposite of 종영?", "상영", ["반영", "촬영", "영화"], "Screening."), M("Which word is the opposite of 공연?", "관람", ["연주", "연기", "관객"], "Watching."),
           M("Which word fits 승자, 무승부, 패자?", "승패", ["게임", "악기", "영화"], "Win or lose."), M("Which word fits 극장, 촬영, 상영?", "영화", ["판매", "관람", "악기"], "A movie."),
           F("우리 팀이 경기에서 ___했습니다. (won)", "승리", ["패배", "무승부"], "승리하다."), F("영화관에서 새 영화를 ___하고 있습니다. (screening)", "상영", ["촬영", "종영"], "상영하다."), F("표가 모두 팔려서 ___되었습니다. (sold out)", "매진", ["관광", "촬영"], "매진."), F("낚시 ___에 가입했습니다. (hobby club)", "동호회", ["동아리방", "연극"], "동호회."), F("주말에 친구와 ___을 갔습니다. (mountain climbing)", "등산", ["당구", "권투"], "등산."),
           read_q("주말에 친구와 등산을 갔습니다"), read_q("영화관에서 새 영화를 상영하고 있습니다"), read_q("표가 모두 팔려서 매진되었습니다"), read_q("우리 팀이 경기에서 승리했습니다"), read_q("낚시 동호회에 가입했습니다")]
    ),
)

# ================================================================== L2 Part 1
_YACHT = [
    ("서울 마리나 클럽 앤 요트는 십육 일부터 요트 무료 시승 행사를 진행한다.", "Seoul Marina Club & Yacht will hold a free yacht trial-ride event starting on the 16th."),
    ("공식 블로그에 휴가를 가지 못한 사연이나 한강에서 있었던 재미있는 에피소드를 댓글로 올리면 추첨을 통해 한강에서 요트를 즐길 수 있는 기회를 제공한다.", "If you post, as a comment on the official blog, a story about not being able to go on vacation or an interesting episode that happened on the Han River, it offers, through a drawing, a chance to enjoy a yacht on the Han River."),
]
_SPEAK1 = [("좋아하는 스포츠나 취미생활이 있으면 친구들과 이야기해 보세요.", "If you have a favorite sport or hobby, talk about it with friends.")]
L2 = lesson(
    "U16 L1 · Part 1 (도입 학습): a yacht trial-ride event",
    "도입 학습 · 요트 시승 행사 · 서울 마리나 · 레저소식 · 추첨 · 에피소드 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 4 (Reading): a newspaper announcement of an event",
             "The following is an announcement of an event from a newspaper (© Yonhapnews), headed 레저소식 (leisure news): 서울 마리나, 요트 시승 행사 (Seoul Marina, yacht trial-ride event). The text is the book’s with 16일 spelled 십육 일 and 클럽&요트 spelled 클럽 앤 요트; the blog address and the telephone number (02-423-7888) are left out because they cannot be read aloud. The English is mine.",
             examples=passage(_YACHT)),
        card("학습활동 4: the questions answered (mine)", "1. The announcement describes a free yacht trial-ride event (a leisure event) run by Seoul Marina Club & Yacht from the 16th.\n\n2. To take part, one posts on the official blog, as a comment, a story about not being able to go on vacation or a funny episode that happened on the Han River; winners are chosen through a drawing and get the chance to enjoy a yacht on the Han River."),
        card("해외토픽 (the book’s footnote)", "해외토픽 (“overseas topic”) refers to any weird, odd, or funny overseas news stories."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK1)),
        card("Activities left out", "학습활동 1 (Listening, track 001): a YTN announcement of an event — what type of event will be held and what the participants will do. 학습활동 2 (Reading · Writing): a cartoon about a male university student’s summer vacation plans — the original plan and the five items he has prepared, drawing the last panel in Korean, then the new plan and the reasons for the change. 학습활동 3 (Listening, tracks 002 and 003): an overseas-topics item from YTN — information about the person and why he or she is on the news. They are audio, video and pictures."),
    ],
    exercises=uniq(
        _tr(_YACHT, k=2) + _tr(_SPEAK1 + [("저는 주말마다 등산을 합니다.", "I go mountain climbing every weekend.")], k=2)
        + [M("What kind of event is announced?", "A free yacht trial ride", ["A concert", "A marathon", "A fishing contest"], "요트 무료 시승 행사."), M("Where can one enjoy the yacht?", "On the Han River", ["On Jeju Island", "In a pool", "On a mountain"], "한강."), M("How does one enter?", "By posting a comment on the official blog", ["By phone only", "By mail only", "By paying a fee"], "공식 블로그에 댓글."), M("How are the winners chosen?", "By a drawing", ["By a race", "By a test", "By age"], "추첨."), M("Which stories can be posted?", "A story about not going on vacation or a funny episode on the Han River", ["A recipe", "A poem", "A news report"], "사연 / 에피소드."),
           F("블로그에 재미있는 ___를 올리면 됩니다. (episode)", "에피소드", ["쿠폰", "자료"], "에피소드."), F("___을 통해 요트를 탈 기회를 제공합니다. (drawing)", "추첨", ["개최", "시승"], "추첨."), F("요트 무료 ___ 행사를 진행한다. (trial ride)", "시승", ["취사", "추첨"], "시승."),
           read_q("요트 무료 시승 행사를 진행합니다"), read_q("한강에서 요트를 즐길 수 있는 기회를 제공합니다"), read_q("좋아하는 스포츠나 취미생활이 있으면 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("개최(하다/되다)", "(開催) holding an event (to hold an event/to be held)", "이번 월드컵이 어디에서 개최됩니까?", "열리다"),
        ("럭비", "rugby", ""),
        ("배드민턴", "badminton", ""),
    ]),
    ("학습활동 2", [
        ("자료", "(資料) materials; data", "다음 주에 환경에 관해 발표를 해야 합니다. 도서관에 가서 자료를 좀 찾아야겠어요."),
        ("쿠폰", "a coupon", "쿠폰을 가지고 오시면 이십오 퍼센트 할인해 드립니다."),
        ("틈틈이", "in one’s spare time (in the middle of a busy schedule); in spare moments; “in [every] cranny”", "저는 직장생활을 하면서 틈틈이 영어공부를 하고 있습니다."),
    ]),
    ("학습활동 3", [
        ("누리꾼", "a netizen; a cybercitizen; a cybernaut", "누리꾼들이 그 홈페이지에 계속 방문하고 있습니다.", "네티즌"),
        ("안착(하다)", "(安着) safe arrival; safe landing (to arrive safely; to land safely)", "우리나라 반도체 제품이 세계 시장 점유율 사십 퍼센트대에 안착했습니다."),
        ("옥상", "(屋上) a rooftop", "잠깐 옥상에 올라가서 바람 좀 쐬고 옵시다."),
    ]),
    ("학습활동 4", [
        ("사연", "(事緣) a story; a situation; circumstances", "김 선생님이 미국에 오신 사연은 아주 재미있습니다.", "사정"),
        ("시승(하다)", "(試乘) a trial ride; a test-drive (to take a trial ride; to test-drive)", "얼마 전 새로 출시된 차를 시승해 봤습니다.", "시식, 시음"),
        ("에피소드", "an episode; an anecdote", "그 사람에 대해서 재미있는 에피소드가 많습니다.", "일화"),
        ("요트", "a yacht", ""),
        ("추첨(하다)", "(抽籤) drawing lots; casting lots (to draw lots)", "이름을 적어 주시면 추첨을 통해 경품을 드립니다.", "뽑다"),
    ]),
]
L3 = lesson(
    "U16 L1 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 개최 · 럭비 · 배드민턴 · 자료 · 쿠폰 · 틈틈이 · 누리꾼 · 안착 · 옥상 · 사연 · 시승 · 에피소드 · 요트 · 추첨",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book prints 배트민턴 for badminton; it is written 배드민턴 here. The book’s examples with digits are spelled in Hangul: 25% → 이십오 퍼센트; 40%대 → 사십 퍼센트대.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=10, nread=8)),
)

# ================================================================== L4 Part 2 texts
_BACK = [
    ("이십 대들의 배낭여행이 여행시장을 이끌던 천구백구십 년대 후반 한국인 배낭여행족들이 핀란드 헬싱키 거리를 걷고 있다.", "In the late 1990s, when backpacking by people in their twenties was leading the travel market, Korean backpackers are walking the streets of Helsinki, Finland. (a photo caption)"),
    ("외환위기 직전인 구십사 년에서 구십칠 년은 배낭여행 전성시대.", "The years 1994 to 1997, just before the foreign exchange crisis, were the golden age of backpacking."),
    ("그 중심에는 이십 대가 있었다.", "At its center were people in their twenties."),
    ("사실 배낭여행에 나선 대부분의 이십 대에게 여행은 고행이나 다름없었다.", "In fact, for most people in their twenties who set out backpacking, traveling was no different from penance."),
    ("열 개국에서 스무 개국을 이십 일에서 오십 일간 돌아보는 일정은 빡빡했고, 변변한 여행가이드북조차 없던 시절이었기 때문이다.", "This is because the schedule of looking around 10 to 20 countries over 20 to 50 days was tight, and it was a time when there were not even decent travel guidebooks."),
    ("호텔 자바 김형렬 이사는 “구십 년대 한국 대학생들의 배낭여행은 저가 패키지 성격이 강했다”고 말했다.", "Kim Hyeong-ryeol, a director of Hotel Java, said, “The backpacking trips of Korean university students in the ’90s had a strong character of low-price packages.”"),
    ("그러나 외환위기를 거치면서 여행 풍속도는 급속도로 달라졌다.", "However, after going through the foreign exchange crisis, the scene of travel customs changed rapidly."),
    ("여행사 트래블게릴라의 최슬기 대표는 “구십 년대식 배낭여행 스타일의 여행은 사라지고 있다”고 했다.", "Choi Seul-gi, the head of the travel agency Travel Guerrilla, said, “Travel in the ’90s-style backpacking style is disappearing.”"),
    ("“저렴한 항공권을 구해서 혼자 개별여행하는 수요가 많고, 인솔자가 있는 배낭여행 패키지도 많이 줄었습니다.”", "“There is a lot of demand for getting a cheap plane ticket and traveling individually alone, and backpacking packages with a tour leader have also decreased a lot.”"),
    ("이천 년대 중반 해외여행이 보편화되면서 해마다 휴가철이면 인천국제공항은 여행객들로 북적거린다.", "As overseas travel became commonplace in the mid-2000s, Incheon International Airport is crowded with travelers every year in the vacation season. (a photo caption)"),
    ("외환위기로 주춤하던 여행시장은 이천 년 이후 부활했다.", "The travel market, which had faltered because of the foreign exchange crisis, revived after 2000."),
    ("해외여행 경험이 많아지고 과거에 비해 여행정보가 흔해지면서 자유여행, 개별여행을 추구하는 여행자들이 점점 더 늘고 있다.", "As overseas travel experience has increased and travel information has become common compared with the past, travelers who pursue free travel and individual travel are increasing more and more."),
    ("이천 년대 들어 인터넷과 디지털카메라의 보급으로 생생한 여행정보를 쉽게 접할 수 있게 되고, 외국의 항공권, 호텔 등을 실시간 예약할 수 있는 온라인 여행서비스가 등장한 것이 한몫했다.", "In the 2000s, the fact that vivid travel information became easy to come by through the spread of the Internet and digital cameras, and that online travel services where one can book foreign flights, hotels and so on in real time appeared, played a part."),
]
_SPEAK1B = [("해외여행 경험이나 특별히 기억에 남는 여행이 있으면 친구들과 이야기해 보세요.", "If you have overseas travel experience or a trip that is especially memorable, talk about it with friends.")]
L4 = lesson(
    "U16 L1 · Part 2 (본 학습): taekwondo, the IMF crisis, and how backpacking changed",
    "본 학습 · 태권도 · 외환위기 · 배낭여행 · 패키지 · 개별여행 · 전성시대 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 1: 태권도 (taekwondo) — the book’s note",
             "태권도 (tae kwon do) is a Korean martial art and the national sport of South Korea. In Korean, 태 (跆) means to strike or break with the foot; 권 (拳) means to strike or break with the fist; and 도 (道) means way, method, or art. Thus, 태권도 loosely translates as the way of the foot and fist or the way of kicking and punching. 태권도 is arguably the world’s most popular martial art, given the number of practitioners. As do other martial arts, 태권도 combines combat techniques, self-defense, sport, exercise, meditation, and philosophy. 태권도 is also used by the South Korean military as part of its training. 겨루기, a type of sparring, has been an Olympic event since 2000. (Image © Kyunghyang.)"),
        card("알아봅시다 2: 외환위기 (the foreign exchange crisis) — the book’s note",
             "The Asian Financial Crisis gripped much of Asia beginning in July 1997. The crisis began in Thailand with the financial collapse of the Thai baht. Indonesia, South Korea, and Thailand were the countries most affected by the crisis. Although most Asian governments had seemingly sound fiscal policies, the International Monetary Fund (IMF) was forced to step in with a $40 billion program to stabilize the currencies of South Korea, Thailand, and Indonesia. The Seoul stock exchange fell by 4% on 7 November 1997. The South Korean won was also affected. It began at around 800 per U.S. dollar and weakened to more than 1,700 per U.S. dollar. Despite an initial sharp economic slowdown and numerous corporate bankruptcies, South Korea has managed to triple its per capita GDP in dollar terms since 1997. In South Korea, the crisis is also commonly referred to as the IMF crisis."),
        card("학습활동 2 (Reading): a magazine article on travel",
             "The following is a travel article from a magazine (Text and images © Kyunghyang). The book asks you to read it and complete the tasks in English. The text is the book’s with the numbers spelled out (20대 → 이십 대; 1990년대 → 천구백구십 년대; 94~97년 → 구십사 년에서 구십칠 년; 10~20개국 → 열 개국에서 스무 개국; 20~50일간 → 이십 일에서 오십 일간; 90년대 → 구십 년대; 2000년대 → 이천 년대; 2000년 → 이천 년); the quotation marks ‘ ’ are removed. The two captions of the photos (► lines) are included. The English is mine.",
             examples=passage(_BACK)),
        card("학습활동 2: the tasks answered (mine)",
             "1. Differences in overseas travel trends. Before the financial crisis (mid-1990s): the golden age of backpacking, led by people in their twenties; trips were tight, hard going (10 to 20 countries in 20 to 50 days, almost like penance), with hardly any decent guidebooks; the style was strongly a “low-price package,” often with a tour leader. Since the financial crisis: the 90s-style backpacking trip is disappearing; many people buy a cheap plane ticket and travel individually alone; backpacking packages with a leader have decreased a lot; the market revived after 2000, and travelers pursue free and individual travel more and more.\n\n"
             "2. Reasons for the new trends: more overseas travel experience; travel information is common compared with the past; the spread of the Internet and digital cameras, which lets people easily come across vivid travel information; and the appearance of online travel services where flights and hotels abroad can be booked in real time."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK1B)),
        card("Activities left out", "학습활동 1 (Listening · Speaking, track 004): a YTN news report on taekwondo — the decision made by public schools in L.A., why it was made, its significance, and what measures would help promote taekwondo to the world. 학습활동 3 (Listening, track 005): a YTN briefing on summer vacation trends — the trend related to lodging and food, what contributed to it, and how it affects the food industry (video). They are audio and video."),
    ],
    exercises=uniq(
        _tr(_BACK[1:9] + _BACK[10:], k=3) + _tr(_SPEAK1B + [("저는 지난 여름에 배낭여행을 다녀왔습니다.", "I went on a backpacking trip last summer.")], k=2)
        + [M("When was the golden age of backpacking per the article?", "1994 to 1997", ["2010 to 2012", "1950 to 1960", "2020 to 2022"], "구십사 년에서 구십칠 년."), M("Who led the backpacking boom?", "People in their twenties", ["Retirees", "Children", "Businessmen"], "이십 대."), M("How many countries did a typical trip cover?", "10 to 20", ["1 or 2", "50 to 60", "100"], "열 개국에서 스무 개국."), M("What was missing at the time?", "Decent travel guidebooks", ["Airplanes", "Passports", "Backpacks"], "변변한 여행가이드북."), M("What did 90s backpacking resemble, per Kim Hyeong-ryeol?", "A low-price package", ["A luxury tour", "A business trip", "A pilgrimage"], "저가 패키지."), M("What is disappearing now, per Choi Seul-gi?", "The 90s-style backpacking trip", ["Airplanes", "The Internet", "Hotels"], "구십 년대식 배낭여행."), M("What is in demand now?", "Individual travel with a cheap ticket", ["Group tours with leaders", "Cruises only", "Staying home"], "개별여행."), M("When did the travel market revive?", "After 2000", ["After 1980", "After 2020", "Never"], "이천 년 이후."), M("What helped provide vivid travel information in the 2000s?", "The Internet and digital cameras", ["Radio", "Telegrams", "Newspapers only"], "인터넷과 디지털카메라."), M("What does 태권도 mean (roughly)?", "The way of the foot and fist", ["The way of the sword", "The way of tea", "The way of the horse"], "The book’s note."), M("Since when has 겨루기 (sparring) been an Olympic event?", "2000", ["1950", "1988", "2020"], "The book’s note."), M("Which crisis began in Thailand in July 1997?", "The Asian Financial Crisis", ["The oil shock", "The Great Depression", "The dot-com bubble"], "The book’s note."),
           F("외환위기 직전은 배낭여행 ___였다. (golden age)", "전성시대", ["고행", "해법"], "전성시대."), F("그 시절 여행은 고행이나 ___없었다. (no different)", "다름", ["차이", "한몫"], "다름없다."), F("인솔자가 있는 배낭여행 ___도 줄었다. (package)", "패키지", ["콘도", "쿠폰"], "패키지."), F("온라인 여행서비스의 등장이 ___했다. (played a part)", "한몫", ["단련", "수련"], "한몫하다."), F("여행시장은 이천 년 이후 ___했다. (revived)", "부활", ["사라", "상징"], "부활하다."),
           read_q("외환위기 직전은 배낭여행 전성시대였습니다"), read_q("저렴한 항공권을 구해서 혼자 개별여행을 합니다"), read_q("인터넷의 보급으로 여행정보를 쉽게 접할 수 있습니다"), read_q("해외여행 경험이 있으면 친구들과 이야기해 보세요"), read_q("여행 풍속도는 급속도로 달라졌습니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("널리", "widely; extensively", "이 제품이 가장 널리 사용되는 제품입니다."),
        ("단련(하다)", "(鍛鍊) strengthening (one’s body or mind) (to strengthen one’s body or mind)", "운동을 하면 몸을 단련할 수 있습니다.", "수련하다"),
        ("보급(하다/되다)", "(普及) dissemination; propagation (to disseminate; to propagate/to be disseminated)", "이천 년대 들어 인터넷이 빠르게 보급되었습니다."),
        ("상징(하다)", "(象徵) a symbol; an emblem (to symbolize)", "우리나라를 상징하는 동물이 무엇입니까?"),
        ("수련(하다)", "(修鍊) training; practicing (to train; to practice)", "요가를 하면서 몸과 마음을 수련하는 사람들이 많습니다. 전문의가 되기 전에 보통 수련과정을 끝내야 합니다.", "단련하다"),
        ("접하다", "(接) to encounter; to come into contact with; to come across", "처음 한국어를 접한 것이 언제였습니까?"),
        ("정규", "(正規) regular; formal", "정규 학교 교육을 받지 않아도 성공할 수 있습니다.", "비정규 | 정식"),
        ("정식", "(定式) formal; official", "저는 이 회사의 정식 직원이 되었습니다."),
        ("진지하게", "(眞摯) seriously; earnestly", "자, 이제 진지하게 이야기해 봅시다."),
    ]),
    ("학습활동 2", [
        ("고행", "(苦行) suffering; penance; (practice of) strict self-denial", "그 사람은 삶을 고행이라고 생각합니다."),
        ("등장(하다)", "(登場) appearance; advent (to appear; to make an appearance)", "인터넷의 등장으로 전세계는 더욱 가까워졌습니다.", "출현하다 | 사라지다"),
        ("변변하다", "to be decent; to be satisfactory", "여기에는 변변한 식당이 하나도 없습니다."),
        ("부활(하다)", "(復活) revival; resurrection (to revive; to resurrect)", "요즘 천구백육십 년대 유행하던 패션이 부활하고 있습니다."),
        ("빡빡하다", "to be tight; to be intensive; to be inflexible", "오늘 일정이 너무 빡빡해서 그 일은 끝내지 못할 것 같아요.", "빠듯하다"),
        ("사라지다", "to disappear; to vanish", "약을 먹었더니 통증이 사라졌어요.", "등장하다, 출현하다"),
        ("시절", "(時節) days; times", "저는 어린 시절에 시골에서 자랐습니다."),
        ("~(이)나 다름없다", "to be no different; to be the same", "저에게 김선생님은 부모나 다름이 없습니다. 저에게 자유가 없다면 죽은 것이나 다름이 없습니다."),
        ("인솔자", "(引率者) a leader; a tour guide; a chaperone; “person who leads and manages”", "저는 해외 여행을 한 번도 해 보지 않아서 여행 인솔자가 꼭 필요합니다."),
        ("저가", "(低價) low price; cheap price", "경기 침체의 영향으로 저가 제품이 인기를 끌고 있습니다.", "염가 | 고가"),
        ("저렴하다", "(低廉) to be cheap; to be inexpensive; to be affordable", "이 가게는 좋은 물건을 저렴하게 구입할 수 있어서 좋습니다.", "싸다 | 비싸다"),
        ("전성시대", "(全盛時代) the golden age; one’s heyday", "요즘은 스마트폰 전성시대입니다."),
        ("추구(하다)", "(追求) pursuing; seeking (to pursue; to seek; to chase)", "사람은 누구나 행복을 추구합니다.", "좇다"),
        ("패키지", "package", ""),
        ("한몫하다", "to play a role; to fulfill one’s role", "깨끗한 환경을 만드는 데 자전거가 한몫하고 있습니다."),
    ]),
    ("학습활동 3", [
        ("겨냥하다", "to aim; to target", "이 제품은 누구를 겨냥한 것입니까?"),
        ("먹거리", "food; “eating material”", "추석 선물로 먹거리를 준비해야겠어요.", "음식 | 마실거리, 구경거리, 볼거리, 놀거리"),
        ("본격적(으로)", "(本格的) (in a) full-scale (way); (in a) full-blown (way); (in a) full-fledged (way); genuine(ly)", "다음주부터 본격적으로 일이 시작됩니다."),
        ("빠듯하다", "to be tight", "이번 주말은 시험 준비에 시간이 빠듯합니다.", "빡빡하다"),
        ("알뜰하게", "frugally", "그 사람은 결혼한 후에 아주 알뜰하게 살고 있어요.", "검소하게"),
        ("업체", "(業體) a (business) enterprise", "연예인들 중에 홈쇼핑 업체를 운영하는 사람이 많습니다.", "회사"),
        ("~을/를 앞두고", "having (an event) ahead; prior to; with (an event) around the corner", "다음 주 졸업시험을 앞두고 우리 반 학생들이 시험 공부를 열심히 하고 있습니다."),
        ("주머니사정", "financial condition; “pocket situation”", "요즘 월급이 깎여서 주머니 사정이 안 좋습니다."),
        ("즉석", "(卽席) instant; impromptu", "그 사람은 즉석에서 연주하는 것을 좋아합니다."),
        ("취사(하다)", "(炊事) cooking (to cook)", "삼 일 동안 캠핑을 하려면 취사 도구가 필요합니다.", "요리(하다)"),
        ("콘도", "a (membership) resort hotel; a condo hotel; a time-share resort; “condo”", "", "펜션"),
    ]),
]
L5 = lesson(
    "U16 L1 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 단련 · 보급 · 상징 · 수련 · 정규 · 고행 · 부활 · 빡빡하다 · 인솔자 · 저렴하다 · 전성시대 · 추구 · 한몫 · 겨냥하다 · 먹거리 · 본격적 · 알뜰하게 · 취사 · 콘도",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul: 2000년대 → 이천 년대; 1960년대 → 천구백육십 년대; 3일 → 삼 일. The book’s two-line examples for 수련하다 and ~(이)나 다름없다 are joined into one example.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=18, nread=14)),
)

# ================================================================== L6 Part 3 texts
_ATV = [
    ("이승렬 (서른여덟 살) 씨가 강원도 원주시 산악오토바이 베이스 캠핑장에서 묘기를 선보이고 있다.", "Mr. Lee Seung-ryeol (38) is showing off stunts at a mountain-motorcycle base camping ground in Wonju, Gangwon-do. (a photo caption)"),
    ("요란한 엔진 소리와 함께 네 개의 바퀴가 동시에 구르기 시작한다.", "With a loud engine sound, four wheels start rolling at the same time."),
    ("웅덩이도, 커다란 바윗돌도 달리면 모두 길이 된다.", "Both puddles and huge boulders all become a road once you ride over them."),
    ("“이렇게 흥미진진한 모터스포츠는 따로 없을 겁니다.”", "“There is probably no other motor sport as thrilling as this.”"),
    ("헬멧에 군복, 중무장한 군인 모습의 이승렬 씨가 엄지손가락을 치켜든다.", "Mr. Lee Seung-ryeol, looking like a heavily armed soldier in a helmet and fatigues, raises his thumb."),
    ("지난 삼 일 만난 이 씨는 경력 삼 년째의 산악오토바이 마니아다.", "Mr. Lee, whom we met on the 3rd, is a mountain-motorcycle enthusiast in his third year of experience."),
    ("매주말 엔진 소리를 듣지 않으면 잠이 안 올 정도다.", "He is to the point that if he does not hear an engine sound every weekend, he cannot fall asleep."),
    ("산악오토바이에 빠져든 뒤 이 씨는 산악오토바이 동호회를 꾸려 팀장을 맡았다.", "After falling for mountain motorcycles, Mr. Lee organized a mountain-motorcycle club and took the post of team leader."),
    ("평일엔 식당을 운영하고, 주말마다 회원들과 연습 코스를 찾는다.", "On weekdays he runs a restaurant, and every weekend he looks for practice courses with the members."),
    ("비포장 산길로 모험 투어를 떠나기도 한다.", "He also goes off on adventure tours on unpaved mountain roads."),
    ("야영까지 하며 산악 코스를 탈 때는 목숨을 걸어야 하는 구간이 곳곳에 있다.", "When riding mountain courses, even camping out, there are sections everywhere where one must risk one’s life."),
    ("인내심과 협동심 없이는 팀을 이룰 수 없다.", "Without patience and teamwork one cannot form a team."),
    ("차가 뒤집히거나 고장이라도 나면 즉시 전원이 달려들어 간단히 해결하고 다음 코스로 이동한다.", "If a vehicle flips over or even breaks down, everyone immediately rushes in, solves it simply and moves on to the next course."),
    ("“손, 팔, 다리, 허리 등 온몸의 근육들을 동시에 써야 하는 운동이죠.", "“It is an exercise in which you must use the muscles of your whole body — hands, arms, legs, waist and so on — at the same time."),
    ("두어 시간쯤 산길을 타면 온몸이 땀으로 흠뻑 젖어요.", "If you ride a mountain road for a couple of hours, your whole body gets soaked with sweat."),
    ("스트레스든 감기든 싹 빠집니다.”", "Stress or a cold, it all goes right out.”"),
    ("산악오토바이를 만난 뒤 이 씨의 주말은 새로운 도전과 모험으로 가득 찬 재충전의 날로 확실히 자리 잡았다.", "After meeting the mountain motorcycle, Mr. Lee’s weekend has firmly settled in as a day of recharging “full of new challenges and adventure.”"),
]
_NAG = [
    ("증상: 목표에 대한 부담으로 일상이 힘겨울 때.", "Symptom: when daily life is hard because of the burden of goals."),
    ("처방: 낡은 도시 나가사키를 방문해 목적 없이 오래 걸을 것.", "Prescription: visit the old city of Nagasaki and walk for a long time without a purpose."),
    ("나가사키 여행을 추천한다.", "I recommend a trip to Nagasaki."),
    ("중요한 것은 방식이다.", "What is important is the way."),
    ("어떠한 사전 정보나 예약 없이 무작정 떠나는 방식으로 나가사키를 여행할 것을 권한다.", "I advise traveling to Nagasaki by setting out with no goal, without any advance information or reservations."),
    ("우리는 여행마저도 강박적으로 해 왔다.", "We have done even traveling compulsively."),
    ("이 도시에서는 이걸 봐야 하고, 몇 시 기차를 타야 하며, 무얼 먹어야만 하는 방식으로 여행을 했다.", "We traveled in the way of: in this city one must see this, one must take the train at such-and-such a time, one must eat what."),
    ("지금 제안하는 나가사키 여행은 다른 방식의 여행이다.", "The Nagasaki trip I am proposing now is a trip of a different kind."),
    ("목표 없이 오래 걷는다.", "You walk a long time without a goal."),
    ("이것 하나만 정해 놓고 무작정 떠나는 산책 같은 여행이다.", "It is a walk-like trip where you decide only this one thing and set out with no plan."),
    ("나가사키 걷기", "Walking in Nagasaki (a subheading)"),
    ("나가사키는 낡은 도시다.", "Nagasaki is an old city."),
    ("그래서 이 도시를 걷는 일은 재미있다.", "So walking this city is fun."),
    ("미리 준비하지 않아도 충분히 흥미롭다.", "It is interesting enough even if you do not prepare in advance."),
    ("사실 이 도시에도 몇몇 관광지가 있다.", "In fact, this city also has a few tourist sites."),
    ("이나사야마 산을 올라가 나가사키 야경을 보는 코스가 세계적으로 유명하다.", "The course of climbing Mt. Inasa to see Nagasaki’s night view is world-famous."),
    ("그러나 이것 역시 목표가 되어서는 곤란하다.", "But it is also not good for this to become a goal."),
    ("여행마저도 강박이 되는 이유는 두 번 다시 못 올 것처럼 여행하기 때문이다.", "The reason even traveling becomes an obsession is that we travel as if we could never come again."),
    ("나가사키의 착한 점 중 하나는 가깝다는 것이다.", "One of Nagasaki’s good points is that it is close."),
    ("언제고 다시 올 수 있다.", "You can come again any time."),
    ("골목이 말해주는 대로", "As the alleys tell you (a subheading)"),
    ("목적 없이 걷는 여행에는 말 그대로 목적이 없다.", "A trip of walking without a purpose literally has no purpose."),
    ("그냥 걷는 것이다.", "You just walk."),
    ("아무 가게에나 들어가 물건들을 만져보고 아무 식당에나 들어가 음식을 먹는 것이다.", "You go into any shop, touch the goods, go into any restaurant and eat the food."),
    ("내가 여행을 이끌고 다니는 것이 아니라 여행이 말해주는 대로 걸음을 옮기는 것이다.", "It is not that I lead the trip around, but that I move my steps as the trip tells me."),
    ("이제껏 우리는 너무 똑똑한 삶을 살았다.", "Until now we have lived too smart a life."),
    ("정교하게 설계한 삶의 코스대로 한 발도 어긋나지 않게 살았다.", "We lived without going astray a single step from the life course we had designed precisely."),
    ("거기서 벗어나면 낙오되어 실패한 인생이라도 되어버릴까 봐.", "For fear that if we left it, we might fall behind and even become a failed life."),
    ("그렇지만 길을 잃는다는 것이 꼭 실패만을 의미하는 것은 아니다.", "But losing one’s way does not necessarily mean only failure."),
    ("나가사키 산책은 그걸 연습하는 여행이다.", "The Nagasaki walk is a trip that practices that."),
    ("낯선 골목으로 불쑥 들어서는 일.", "Stepping suddenly into an unfamiliar alley."),
    ("예정에 없지만, 그냥 들어서는 일.", "Stepping in just because, though it was not planned."),
    ("그리해도 무사하구나, 별일 없구나, 하는 안도감을 느껴보는 일.", "Feeling the relief of “It is fine even if I do this, nothing happens.”"),
    ("나가사키의 낡은 골목들을 그런 마음으로 걸어본다.", "You walk Nagasaki’s old alleys with that kind of mind."),
    ("준비한 계획 없이.", "Without a prepared plan."),
    ("골목이 말해주는 방향으로.", "In the direction the alleys tell you."),
]
_SPEAK1C = [("돈과 시간이 많다면 어떤 여가생활을 하고 싶은지 또 어떤 곳으로 여행을 가고 싶은지 생각해 보고 그 이유도 생각해 보세요.", "If you had a lot of money and time, think about what kind of leisure life you would like to have and what place you would like to travel to, and think about the reasons too."), ("그리고 친구들은 어떤 생각을 하는지 의견을 나눠 보세요.", "And exchange opinions about what your friends think.")]
L6 = lesson(
    "U16 L1 · Part 3 (심화 학습): a mountain-motorcycle enthusiast and a trip to Nagasaki",
    "심화 학습 · 산악오토바이 · 모터스포츠 · 동호회 · 재충전 · 나가사키 · 무작정 · 강박 · 골목 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): an article on a special leisure life",
             "The following is an article introducing a person who enjoys a special leisure life (Text and image © Hankyoreh). The text is the book’s with the numbers spelled out (38 → 서른여덟 살; 3일 → 삼 일; 3년째 → 삼 년째); the dot in 인내심·협동심 and in 손·팔·다리·허리 is written as a comma or 와; the quotation marks “ ” are kept as printed. The English is mine. (The caption of the photo in the book gives the name as 이슬렬, a slip for 이승렬; the text gives 이승렬.)",
             examples=passage(_ATV)),
        card("학습활동 1: the questions answered (mine)",
             "1. Mr. Lee runs a restaurant (on weekdays); his hobby is mountain motorcycling (off-road riding), and he leads a club as its team leader.\n\n"
             "2. On weekends he looks for practice courses with the club members, goes on adventure tours on unpaved mountain roads, and sometimes camps out while riding mountain courses.\n\n"
             "3. He thinks there is no other motor sport as thrilling; he finds it a whole-body exercise that makes him sweat and wipes out stress and colds, requires patience and teamwork, and he regards his weekend as a day of recharging full of new challenges and adventure.\n\n"
             "4. (The underlined sentence is not marked in the text; my best guess is the second sentence.) “Both puddles and huge boulders all become a road once you ride over them.”"),
        card("학습활동 3 (Reading): a magazine essay on a trip to Nagasaki",
             "The following is a piece from the culture column of a magazine (Text and image © Kyunghyang). The text is the book’s. The English is mine.",
             examples=passage(_NAG)),
        card("학습활동 3: the questions answered (mine)",
             "1. B — people who are burdened by pursuing their goals (the “symptom” is daily life made hard by the burden of goals).\n\n"
             "2. The author suggests that readers travel to Nagasaki with no advance information or reservations and no goal, simply walking a long time and following the alleys, to practice not worrying about getting lost.\n\n"
             "3. (The underlined word is not marked in the text; my best guess is 정교하게 설계한 in “정교하게 설계한 삶의 코스”, for which the best substitute is) A. 계획된 (planned)."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK1C)),
        card("Activities left out", "학습활동 2 (Listening, track 006): a commentary on golf from Donga — what happened on the 17th and why, the main issue and its reasons, and the solutions the speaker suggests (the vocabulary of the activity — 규제, 완화, 철폐, 초과, 허용, 해법 — is in the vocabulary lesson that follows). It is audio."),
    ],
    exercises=uniq(
        _tr(_ATV[1:], k=3) + _tr(_NAG, k=3) + _tr(_SPEAK1C, k=2)
        + [M("What does Mr. Lee do on weekdays?", "Runs a restaurant", ["Teaches", "Drives a taxi", "Writes news"], "식당을 운영한다."), M("What is his hobby?", "Mountain motorcycling", ["Golf", "Fishing", "Chess"], "산악오토바이."), M("How long has he been at it?", "In his third year", ["Ten years", "One month", "Twenty years"], "삼 년째."), M("What does he lead?", "A mountain-motorcycle club", ["A company", "A school", "A choir"], "동호회 팀장."), M("What does he say it wipes out?", "Stress and colds", ["Money", "Hunger", "Memories"], "스트레스든 감기든."), M("What does the team need?", "Patience and teamwork", ["Wealth", "Fame", "Silence"], "인내심과 협동심."),
           M("Who is the Nagasaki essay aimed at?", "People burdened by pursuing their goals", ["Overseas travel fans", "People with no goals", "Failed students"], "B."), M("How should one travel to Nagasaki per the essay?", "With no goal, walking long, without reservations", ["With a tight schedule", "By tour package", "With a guidebook only"], "무작정."), M("What is the famous course in Nagasaki?", "Climbing Mt. Inasa to see the night view", ["Skiing", "Surfing", "Hot-air ballooning"], "이나사야마 산."), M("What is one of Nagasaki’s good points?", "It is close, so you can come again", ["It is cheap", "It is empty", "It is warm"], "가깝다."), M("What does the essay say losing one’s way means?", "Not necessarily failure", ["Always failure", "Danger", "Punishment"], "꼭 실패만을 의미하는 것은 아니다."),
           F("산악오토바이는 ___ 없이는 팀을 이룰 수 없다. (patience)", "인내심", ["안도감", "자료"], "인내심."), F("이 씨의 주말은 ___의 날로 자리 잡았다. (recharge)", "재충전", ["단련", "취사"], "재충전."), F("나가사키 여행은 ___ 떠나는 방식이다. (with no plan)", "무작정", ["즉석", "본격적"], "무작정."), F("우리는 여행마저도 ___으로 해 왔다. (obsessively)", "강박적", ["알뜰하게", "진지하게"], "강박적으로."), F("낯선 골목으로 ___ 들어서는 일. (suddenly)", "불쑥", ["널리", "틈틈이"], "불쑥."),
           read_q("산악오토바이에 빠져든 뒤 동호회를 꾸렸습니다"), read_q("주말마다 회원들과 연습 코스를 찾습니다"), read_q("나가사키는 낡은 도시입니다"), read_q("골목이 말해주는 방향으로 걸어 봅시다"), read_q("돈과 시간이 많다면 어떤 여가생활을 하고 싶습니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("구간", "(區間) a section (of a road or railway); an area", "여기는 상습적으로 교통이 정체되는 구간입니다.", "지역"),
        ("구르다", "to roll", "계단에서 넘어져서 굴러 떨어졌어요."),
        ("마니아", "an enthusiast; “mania(c)”", "스포츠카 마니아, 컴퓨터 마니아"),
        ("모험", "(冒險) an adventure", "이 투자는 너무 큰 모험입니다."),
        ("목숨을 걸다", "to risk one’s life; to bet one’s life; “to hang one’s life on”", "김영철 씨가 지하철 역에서 목숨을 걸고 할머니를 구했습니다."),
        ("비포장", "(非鋪裝) unpaved", "여기는 비포장 도로라서 운전하기가 쉽지 않습니다.", "포장 | 비포장도로"),
        ("웅덩이", "a puddle", ""),
        ("인내심", "(忍耐心) patience; endurance; perseverance", "인내심을 가지고 조금만 더 기다려 봅시다.", "참을성, 끈기"),
        ("자리 잡다", "to settle down; to nestle; “to grab a seat”", "태권도는 한국의 상징으로 자리 잡았습니다."),
        ("재충전", "(再充電) recharge", "이번 휴가를 통해 저는 재충전을 하고 싶습니다.", "충전"),
        ("협동심", "(協同心) teamwork; “cooperation mind”", "그 사람은 협동심이 부족해서 같이 일하기 힘들어요."),
    ]),
    ("학습활동 2", [
        ("경비", "(經費) expenses; costs", "여행 경비가 너무 많이 들었어요.", "비용 | 경비 (警備) a guard"),
        ("규제(하다)", "(規制) a regulation; a control; a restriction (to regulate; to control; to restrict)", "정부의 규제가 너무 심해서 기업이 투자를 하지 못하고 있습니다."),
        ("나무라다", "to rebuke; to scold", "아이가 숙제를 하지 않아서 나무랐어요.", "꾸짖다"),
        ("벌어지다", "(fight, war, etc.) to occur; to take place", "시장에서 상인들간에 싸움이 벌어졌습니다.", "일어나다"),
        ("부추기다", "to incite; to instigate", "새로 발표된 제도는 과소비를 부추기는 것입니다."),
        ("세금", "(稅金) a tax; a duty", "정부는 경기를 활성화시키기 위해 세금을 내리겠다고 했습니다."),
        ("숙식비", "(宿食費) cost for board and lodging", "숙식비는 한 달에 얼마입니까?"),
        ("완화(하다/되다)", "(緩和) easing; relaxation; alleviation (to ease/to be eased)", "정부에서 세금 규제를 완화하겠다고 발표했습니다."),
        ("전세기", "(傳貰機) a chartered plane", "", "전세버스"),
        ("중량", "(重量) weight", "비행기에 실으려던 제 짐이 중량을 초과했어요.", "무게"),
        ("채", "a racket; a (golf) club", "", "골프채, 테니스채"),
        ("철폐(하다/되다)", "(撤廢) abolition (to abolish/to be abolished)", "여성을 차별하는 제도는 철폐되어야 합니다.", "폐지"),
        ("초과(하다/되다)", "(超過) exceeding (to exceed/to be exceeded)", "제한속도를 초과해서 딱지를 뗐습니다.", "넘다"),
        ("카트", "a golf cart; a shopping cart; “cart”", ""),
        ("캐디", "a caddy", ""),
        ("해법", "(解法) a solution", "이 문제를 해결할 해법이 생각나지 않습니다.", "해결책"),
        ("해프닝", "a simple incident; “happening”", "이 사건은 단순한 해프닝입니다."),
        ("허용(하다/되다)", "(許容) permission; allowing (to permit; to allow/to be permitted; to be allowed)", "유럽 몇 개국은 안락사를 제한적으로 허용합니다."),
    ]),
    ("학습활동 3", [
        ("강박적으로", "(强迫的) obsessively; compulsively", "매일 너무 강박적으로 살고 있어요. 답답합니다.", "자유롭게"),
        ("낙오(하다/되다)", "(落伍) falling behind; lagging behind (to fall behind; to lag behind)", "변화에 민감하지 않으면 낙오될 수밖에 없습니다."),
        ("낡다", "to be worn out; to be shabby; to be old-fashioned; to be old", "이번에 낡은 차를 팔고 새 차를 사야겠어요."),
        ("낯설다", "to be unfamiliar", "길이 낯설어서 길 찾기가 어렵습니다.", "낯익다"),
        ("무작정", "(無酌定) with no definite goal or plan; blindly; thoughtlessly", "이번 여름에는 아무데로나 무작정 여행을 떠날까 합니다."),
        ("불쑥", "unexpectedly; abruptly; suddenly", "차 앞으로 어린 아이가 불쑥 뛰어들어서 사고가 날 뻔했어요.", "갑자기"),
        ("설계(하다/되다)", "(設計) plan; design; layout; mapping out (to design; to map out/to be designed; to be mapped out)", "이 건물은 지진을 대비해 설계되었습니다.", "계획하다"),
        ("안도감", "(安堵感) a feeling of relief; a sense of security", "가족과 같이 있어서 안도감이 듭니다.", "불안감"),
        ("어긋나다", "to be out of line; to go wrong", "제 계획이 어긋나서 조금 실망했습니다."),
        ("정교하다", "(精巧) to be exquisite; to be delicate; to be fine", "이 기계는 아주 정교하게 설계되어 있습니다."),
        ("힘겹다", "to be hard (to do); to be difficult", "이번 일은 저에게 너무 힘겨운 일입니다."),
    ]),
]
L7 = lesson(
    "U16 L1 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 구간 · 구르다 · 마니아 · 모험 · 비포장 · 인내심 · 자리 잡다 · 재충전 · 협동심 · 규제 · 완화 · 철폐 · 초과 · 해법 · 허용 · 낙오 · 낡다 · 낯설다 · 무작정 · 불쑥 · 설계 · 안도감 · 어긋나다 · 정교하다 · 힘겹다",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the book’s example for 설계 the sentence reads 이 건물을 지진을 대비해 설계되었습니다, a slip for 이 건물은; it is corrected here. The book lists the example of 마니아 as two phrases (스포츠카 마니아, 컴퓨터 마니아); they are kept as the example. The book’s two-line example for 강박적으로 is joined into one example.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=20, nread=16)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 1: Leisure and Sports (여가와 스포츠)", [L1, L2, L3, L4, L5, L6, L7])

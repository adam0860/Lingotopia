"""Unit 39: KBC Semester 2, Unit 8, Chapter 32 - Living a Healthy Life (건강한 생활).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 8, Student's Edition (Validation Edition).
Audio, pictures, pie charts, SMART Board activities, games, role-plays, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 32 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("거르다", "to skip (a meal); to omit", "요즘 직장인들은 보통 아침을 거르거나 간단히 먹습니다."),
    ("낙천적", "(樂天的) optimistic; happy-go-lucky; to be optimistic (~이다)", "낙천적인 사람들은 늘 긍정적으로 생각합니다."),
    ("노인", "(老人) an elderly person; an aged person; the aged; “old person”", "팔십 세 이상의 노인들은 공연을 무료로 관람하실 수 있습니다."),
    ("마을 / 촌", "(村) a village", "이 마을 젊은이들은 마을 행사에 늘 참석합니다."),
    ("보리 / 보리쌀", "barley", "쌀 대신에 보리쌀을 먹으면 살이 빠집니다."),
    ("비결", "(秘訣) a secret; a key; a knack", "한국말을 잘 하는 비결이 무엇입니까?"),
    ("비율", "(比率) a ratio; a percent; a proportion; “compared rate”", "시골에는 결혼하지 않은 남자의 비율이 높습니다."),
    ("섞다", "to mix; to blend; to mingle", "커피에 뜨거운 물을 조금 섞어 주세요."),
    ("소식", "(小食) light eating; “small meal”; to eat little (~하다)", "일본인들은 보통 소식을 한대요."),
    ("움직이다", "to move; to stir; to shift", "사진을 찍을 때는 자꾸 움직이지 마세요."),
    ("육류", "(肉類) meat; flesh; “flesh type”", "소고기나 돼지고기 같은 육류를 너무 자주 드시지 마세요."),
    ("자연", "(自然) nature", "이번 주말에는 야외로 나가 자연을 즐겨보세요."),
    ("잡곡", "(雜穀) cereals; minor grains; any grain but rice; “mixed grains”", "흰 쌀밥만 먹지 말고 잡곡밥도 좀 드세요."),
    ("장수", "(長壽) longevity; “long life”; to live long (~하다)", "어머님 아버님, 건강하시고 장수하세요."),
    ("채식", "(彩食) vegetarian diet; “vegetable eating”; to live on vegetables (~하다)", "저는 육식보다는 채식을 좋아합니다."),
    ("콩", "a bean; a pea; a soybean", "콩에는 단백질이 많습니다."),
    ("태도", "(態度) an attitude", "김 상병은 수업 태도가 참 좋은 학생입니다."),
]
_CV_B = [
    ("간식", "(間食) snacks; “between meals”", "아침을 안 먹어서 점심 식사 전에 간식을 먹습니다."),
    ("거의", "almost", "요즘 다이어트를 해서 밥을 거의 안 먹어요."),
    ("건강관리사", "(健康管理士) a health and nutrition counselor; a health-care specialist; “health-managing specialist”", "건강관리사는 환자에게 맞는 식단과 운동 방법을 알려줍니다."),
    ("골고루", "evenly; equally; a broad variety of ~", "건강을 위해서는 음식을 골고루 먹어야 합니다."),
    ("과자", "(菓子) sweets; confectionary; cookies", "쌀로 만든 전통 한국 과자가 인기가 많습니다."),
    ("군것질", "eating between meals; to eat between meals (~하다)", "쉬는 시간마다 군것질을 했더니 몸무게가 많이 늘었어요."),
    ("균형", "(均衡) balance; to balance (~ 잡다)", "자전거를 탈 때 균형을 잘 잡아야 넘어지지 않습니다."),
    ("땀", "sweat; perspiration; sweat breaks out / to sweat (~[이] 나다 / [을] 흘리다)", "여름에는 땀이 너무 많이 나서 옷을 자주 갈아 입습니다."),
    ("사탕", "(砂糖) candy", "당뇨병 환자들은 사탕을 많이 먹으면 안 됩니다."),
    ("섭취", "(攝取) intake; ingestion; to intake; to ingest (~하다)", "비타민 씨를 섭취하려면 과일을 많이 드세요."),
    ("양 / 량", "(量) an amount; a quantity", "운동량을 늘리고 식사량을 좀 줄여 보세요."),
    ("열량 / 칼로리", "(熱量) a calorie; “heat quantity”", "햄버거 한 개의 열량은 이백 칼로리입니다."),
    ("영양소", "(營養素) a nutrient", "여러 음식에서 다양한 영양소를 섭취하는 것이 좋습니다."),
    ("인스턴트 식품", "(食品) fast food; precooked food; “instant food”", "아이들은 햄버거, 핫도그, 피자 같은 인스턴트 식품을 좋아합니다."),
    ("적어도", "at least", "적어도 하루에 한 번은 과일을 드세요."),
    ("조절", "(調節) regulation; adjustment; control; tuning; to regulate; to adjust; to control; to tune (~하다)", "당뇨병 환자들은 혈당과 콜레스테롤을 잘 조절해야 합니다."),
    ("지방", "(脂肪) fat", "요즘 다이어트 중이어서 지방이 많은 음식은 피하고 있습니다."),
    ("체지방", "(體脂肪) body fat", "마라톤 선수나 사이클리스트는 체지방이 아주 적습니다."),
    ("초콜릿", "chocolate", "발렌타인 데이에 남자친구에게 초콜릿을 받았습니다."),
    ("편식", "(偏食) unhealthy diet; unhealthy dietary preference; poor eating (habit); “skewed eating”", "어릴 때부터 편식을 하지 않도록 잘 가르쳐야 합니다."),
    ("효과", "(效果) effect; effectiveness", "이 진통제는 별로 효과가 없는 것 같아요."),
]
_CV_C = [
    ("개인", "(個人) an individual; a private citizen", "개인마다 잘 하는 것과 좋아하는 것이 있습니다."),
    ("끌다", "to pull; to draw; to tow; to attract; to charm", "주말 농장이 큰 인기를 끌고 있습니다."),
    ("다양", "(多樣) variety; to be various; to be diverse (~하다)", "미국에는 다양한 사람들이 많이 삽니다."),
    ("마련", "preparation; provision; plan; to prepare; to raise money; to plan (~하다)", "요즘 집값이 내려가서 집을 마련하려는 사람들이 많습니다."),
    ("맞이하다", "to meet; to greet; to welcome", "어린이날을 맞이하여 놀이공원에서 많은 행사를 한다."),
    ("문의", "(問議) an inquiry; to inquire (~하다)", "관심 있으신 분은 일이삼에 사오육칠 번으로 문의해 주세요."),
    ("~및", "and (also); as well as", "영화 상영 시간 및 자세한 정보는 인터넷에서 찾으세요."),
    ("벗어나다", "to get out of; to free oneself from", "주말에는 복잡한 도시를 벗어나서 멀리 등산하러 갑니다."),
    ("식단", "(食單) a menu (schedule)", "살을 빼려면 좋은 식단을 짜야 합니다."),
    ("야외", "(野外) outdoors; open air", "겨울에는 야외 활동 대신 보통 실내에서 하는 운동을 합니다."),
    ("여가", "(餘加) leisure; spare time; off hours; “spare adding”", "요즘 많은 한국인들은 주말에 야외에서 여가를 보냅니다."),
    ("오염", "(汚染) contamination; pollution; “dirty dilution”; to be polluted (~되다)", "엘에이는 자동차가 많아서 공기가 오염되어 있습니다."),
    ("오토캠핑", "car camping; “auto(mobile) camping”", "오토캠핑을 가면 편리한 점이 많습니다."),
    ("올바르다", "to be right; to be rightful; to be upright; to be honest", "자세가 올바르지 않으면 허리에 문제가 생깁니다."),
    ("운영", "(運營) operation; management; administration; “operation and management”; to operate; to manage / to be operated (~하다/되다)", "본 센터에서는 다음 주부터 무료 요가 교실을 운영할 예정입니다."),
    ("웰빙", "well-being", "한국에서는 요즘 웰빙 문화가 유행입니다."),
    ("유기농", "(有機農) organic (farming)", "유기농 식품은 값이 비싼 편입니다."),
    ("전문가", "(專門家) a specialist; a professional", "비만이 걱정되면 전문가를 만나 보세요."),
    ("직접", "(直接) directly; firsthand", "이 가구는 제가 직접 골랐어요."),
    ("진단", "(診斷) a diagnosis; to diagnose (~하다)", "의사가 암이라고 진단을 내렸어요."),
    ("참여", "(參與) participation; to participate; to take part in (~하다)", "건강 프로그램에 참여를 원하시는 분들은 빨리 신청하세요."),
    ("프로그램", "a program", "요즘 재미있는 텔레비전 프로그램이 뭔가요?"),
    ("해소", "(解消) a solution; a settlement; a dissolution; to solve; to settle; to dissolve; to release [stress]; “solving and quenching” (~하다)", "스트레스를 해소하는 데는 땀을 많이 흘리는 운동이 최고인 것 같아요."),
]
_CV_GR = [
    ("-게 하다", "have/make … do …", "저는 대학에 가고 싶지 않았어요. 그런데 어머니가 저를 대학에 가게 하셨어요."),
    ("-거든요", "informal sentence ending", "제가 커피를 아주 좋아하거든요."),
    ("-(으)ㄹ 만하다", "be worth (~ing)", "요즘 볼 만한 텔레비전 프로그램이 있어요?"),
    ("-는 데(에)", "for / in / at doing something", "해외여행을 가는 데에 비자와 여권이 필요합니다."),
]
_CV_LOAN = [("오토캠핑", "car camping; “auto(mobile) camping”", "요즘 젊은이들 사이에 오토캠핑이 유행입니다."), ("웰빙", "well-being", "요즘 한국에는 유기농 음식, 친환경 재료 등 웰빙이 인기를 얻고 있습니다."), ("초콜릿", "chocolate", "초콜릿이나 사탕을 너무 많이 먹으면 비만이 되기 쉽습니다."), ("프로그램", "a program", "와이엠시에이에서 다음 주부터 수영 프로그램을 새로 시작한다고 합니다.")]
_CV_SINO = [("노인", "(老人) an aged person; elderly; the aged; “old person”", "노화, 노년, 남녀노소, 외국인, 부인, 성인"), ("직접", "(直接) direct(ly); firsthand; “direct contact”", "직선, 직항, 간접, 대접, 면접"), ("편식", "(偏食) unhealthy diet; unhealthy dietary preference; poor eating (habit); “skewed eating”", "편견, 편두통, 편애, 소식, 식비, 의식주")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_GR}
_EXTRA = {"마을 / 촌": "a village", "보리 / 보리쌀": "barley", "양 / 량": "an amount; a quantity", "열량 / 칼로리": "a calorie; “heat quantity”", "-게 하다": "have/make … do …", "-거든요": "informal sentence ending", "-(으)ㄹ 만하다": "be worth (~ing)", "-는 데(에)": "for / in / at doing something", "~및": "and (also); as well as", "인스턴트 식품": "fast food; precooked food", "건강관리사": "a health and nutrition counselor",
          "햄버거": "a hamburger", "칼로리": "a calorie", "야채": "vegetables", "아이스크림": "ice cream", "쇠고기": "beef", "돼지고기": "pork", "닭고기": "chicken",
          "노화": "aging; “becoming old”", "노년": "old age", "남녀노소": "men and women, old and young", "외국인": "a foreigner", "부인": "a wife", "성인": "an adult", "경로": "respect for the aged",
          "편견": "a bias; “skewed opinion”", "편두통": "migraine", "편애": "partiality (for); favoritism (to); “skewed love”", "식당": "a dining room; a restaurant; “eating house”", "후식": "a dessert; “post food”",
          "직감": "intuition; “direct feeling”", "직선": "a straight line; a beeline", "직언": "straight talk; “direct speech”", "직행": "going/coming straight; nonstop; “direct coming and going”", "접대": "a reception; a warm welcome; “treating and waiting”", "접지": "ground connection; grounding; “contact the ground”", "접촉": "contact; touch; “contact and touch”", "간접": "indirect; secondhand", "간접흡연": "secondhand smoking", "간접선거": "an indirect election",
          "소식": "light eating; “small meal”", "채식": "vegetarian diet; “vegetable eating”", "장수": "longevity; “long life”", "섭취": "intake; ingestion", "조절": "regulation; adjustment; control", "마련": "preparation; provision; plan", "문의": "an inquiry", "참여": "participation", "진단": "a diagnosis", "해소": "a solution; a dissolution", "운영": "operation; management", "오염": "contamination; pollution", "균형": "balance", "군것질": "eating between meals", "다양": "variety"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_RO = [("노화", "aging; “becoming old”"), ("노년", "old age"), ("남녀노소", "men and women, old and young"), ("외국인", "a foreigner"), ("부인", "a wife"), ("성인", "an adult")]
_PY = [("편견", "a bias; “skewed opinion”"), ("편두통", "migraine"), ("편애", "partiality (for); favoritism (to); “skewed love”"), ("식당", "a dining room; a restaurant; “eating house”"), ("후식", "a dessert; “post food”")]
_JJ = [("직감", "intuition; “direct feeling”"), ("직선", "a straight line; a beeline"), ("직언", "straight talk; “direct speech”"), ("직행", "going/coming straight; nonstop; “direct coming and going”"), ("접대", "a reception; a warm welcome; “treating and waiting”"), ("접지", "ground connection; grounding; “contact the ground”"), ("접촉", "contact; touch; “contact and touch”"), ("간접", "indirect; secondhand"), ("간접흡연", "secondhand smoking"), ("간접선거", "an indirect election")]

# ================================================================== L1: objectives and Sino-Korean
L1 = lesson(
    "Ch 32 · What the chapter teaches, 노 (老) 인 (人) · 편 (偏) 식 (食) · 직 (直) 접 (接)",
    "건강한 생활 · 노인 · 편식 · 직접 · 간접 · 노화 · 편견",
    requires=[],
    cards=[
        card("What Chapter 32 teaches (건강한 생활)",
             "Chapter 32, “Living a Healthy Life”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify healthy eating and lifestyle habits; discuss living a healthy, long life; and give and receive advice about health and nutrition.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; the causative construction –게 하다; the informal ending –거든(요); –(으)ㄹ 만하다 (be worth ~ing); the conjunctive ending –는 데(에); and the Sino-Korean syllables within 노인 (老人), 편식 (偏食), and 직접 (直接)."),
        card("Sino-Korean in use: 노인 (老人)",
             "This Sino-Korean word refers to an aged person, the elderly, or the aged; 로/노 (老) means old or aged and 인 (人) means a person. The character 老 reads as 노 when it is placed at the beginning of a word. When placed elsewhere, it reads as 로, as in 경로 (敬老), respect for the aged. 화 (化) means “become”.\n\n"
             "The book asks you to guess the meaning of 노화, 노년, 남녀노소, 외국인, 부인 and 성인 (my answers are in the table).",
             tables=[ktable(_RO)]),
        card("Sino-Korean in use: 편식 (偏食)",
             "This Sino-Korean word means unhealthy diet, unhealthy dietary preference, or poor eating (habit). The first syllable 편 (偏) means skewed or tilted, as in 편견 (a bias; “skewed opinion”), 편두통 (migraine), and 편애 (partiality [for]; favoritism [to]; “skewed love”). The second syllable 식 (食) means food or eating, as in 식당 (a dining room; a restaurant; “eating house”) and 후식 (a dessert; “post food”). Thus the literal meaning of the word 편식 is “skewed eating” or “tilted eating”, and it refers to the unhealthy dietary habit of eating only a limited variety of food.",
             tables=[ktable(_PY)]),
        card("Sino-Korean in use: 직접 (直接)",
             "This Sino-Korean word means direct or firsthand. The first syllable 직 (直) means direct or straight, as in 직감 (intuition; “direct feeling”), 직선 (a straight line; a beeline), 직언 (straight talk; “direct speech”), and 직행 (going/coming straight; nonstop; “direct coming and going”). The second syllable 접 (接) means contact or treat, as in 접대 (a reception; a warm welcome; “treating and waiting”), 접지 (ground connection; grounding; “contact the ground”), and 접촉 (contact; touch; “contact and touch”). Thus the literal meaning of the word 직접 is “direct contact”, and the word means direct or firsthand. The antonym of the word is 간접 (indirect; secondhand), as in 간접흡연 (secondhand smoking) and 간접선거 (indirect election).",
             tables=[ktable(_JJ)]),
    ],
    exercises=uniq(
        _tr(_RO + _PY + _JJ, k=3)
        + [M("What does 노/로 (老) mean?", "old; aged", ["person", "food", "direct"], "노인, 경로."), M("What does 인 (人) mean?", "person", ["old", "food", "poison"], "노인, 외국인."), M("What does 화 (化) mean?", "become", ["old", "person", "contact"], "노화."), M("What does 편 (偏) mean?", "skewed; tilted", ["direct", "food", "old"], "편식, 편견."), M("What does 직 (直) mean?", "direct; straight", ["contact", "food", "skewed"], "직선, 직행."), M("What does 접 (接) mean?", "contact; treat", ["direct", "food", "old"], "접촉, 접대."), M("What does 식 (食) mean in 식당?", "food; eating", ["contact", "skewed", "person"], "식당, 후식."),
           M("What is the literal meaning of 편식?", "“skewed eating”", ["“old person”", "“direct contact”", "“long life”"], "편 + 식."), M("What is the literal meaning of 직접?", "“direct contact”", ["“skewed eating”", "“old person”", "“small meal”"], "직 + 접."), M("What is the antonym of 직접?", "간접 (indirect)", ["직행", "직선", "직감"], "직접 ↔ 간접."),
           F("80세 이상의 ___들은 공연을 무료로 관람하실 수 있습니다. (the elderly)", "노인", ["성인", "외국인"], "노인."), F("어릴 때부터 ___을 하지 않도록 잘 가르쳐야 합니다. (unhealthy diet)", "편식", ["후식", "과식"], "편식."), F("이 가구는 제가 ___ 골랐어요. (firsthand)", "직접", ["간접", "직선"], "직접."),
           read_q("노인"), read_q("편식"), read_q("직접"), read_q("간접"), read_q("노화")]
    ),
)

# ================================================================== L2: Vocabulary Builder
_VB1 = [("햄버거", "a hamburger"), ("노인", "an elderly person; the aged"), ("오토캠핑", "car camping"), ("웰빙", "well-being"), ("장수", "longevity; “long life”"), ("비율", "a ratio; a percent; a proportion"), ("칼로리", "a calorie"), ("야외", "outdoors; open air"), ("체지방", "body fat")]
_HEALTHY = ["소식", "채식", "잡곡", "야채"]
_UNHEALTHY = ["편식", "군것질", "인스턴트 식품", "과자"]
_CLUE = [("돼지고기, 소고기, 닭고기", "육류", "meat"), ("과자, 아이스크림, 초콜릿", "군것질", "eating between meals"), ("쌀과 섞어서 밥을 한다", "잡곡", "mixed grains"), ("맥도널드, 버거킹, 웬디스", "햄버거", "a hamburger"), ("식사할 때 조금씩 먹는다", "소식", "light eating"), ("좋아하는 음식만 골라서 먹는다", "편식", "unhealthy diet"), ("건강하게 오래 산다", "장수", "longevity"), ("야채를 주로 먹는다", "채식", "vegetarian diet")]
_JRN = [("장수마을", "Longevity Village"), ("지난 주말에 가족들이랑 장수마을에 놀러 갔다.", "Last weekend I went to a longevity village with my family."), ("그곳은 다른 곳보다 연세 많은 분들의 비율이 아주 높았다.", "In that place the proportion of elderly people was much higher than in other places."), ("팔십 세 이상 노인분들이 많았고, 가장 연세가 많은 분은 백오 세의 김순례 할머니이셨다.", "There were many elderly people over eighty, and the oldest was Grandmother Kim Sunrye, who was one hundred and five."), ("그곳에 사는 분들은 채식이나 소식을 하셔서 다들 건강하셨다.", "The people who live there eat vegetarian food or eat lightly, so they were all healthy."), ("그리고 야외활동을 많이 하면서 건강을 유지하고 계셨다.", "And they were keeping their health by doing a lot of outdoor activities."), ("나는 거기서 나쁜 내 식습관을 알게 되었다.", "There I came to realize my own bad eating habits."), ("나는 그동안 쇠고기와 돼지고기 같은 육류를 거의 매일 먹고, 칼로리가 높은 음식도 많이 먹었다.", "All this time I ate meat such as beef and pork almost every day, and I also ate a lot of high-calorie food."), ("그리고 식사 외에도 빵이나 아이스크림 등 군것질도 많이 했다.", "And besides meals, I also ate a lot of snacks such as bread and ice cream."), ("장수마을에 다녀온 후 나는 앞으로 건강에 좋은 웰빙식생활을 하기로 결심했다.", "After returning from the longevity village, I decided to live a healthy well-being diet from now on.")]
L2 = lesson(
    "Ch 32 · Vocabulary Builder: loan words, Sino-Korean words, food groups and a journal",
    "햄버거 · 노인 · 오토캠핑 · 웰빙 · 장수 · 비율 · 칼로리 · 야외 · 체지방 · 편식 · 소식 · 채식",
    requires=[],
    cards=[
        card("Part I: study the nine core words",
             "The book gives nine core words (햄버거 노인 오토캠핑 웰빙 장수 비율 칼로리 야외 체지방), asks you to circle the Sino-Korean words and underline the loan words, and to guess their English meanings, compare with a classmate and check with the teacher. The loan words are 햄버거, 오토캠핑, 웰빙 and 칼로리; the Sino-Korean words are 노인, 장수, 비율, 야외 and 체지방. The meanings (the book’s English, in my order):",
             tables=[ktable(_VB1)]),
        card("Part II: healthy and unhealthy eating habits",
             "The book gives eight words and phrases (편식, 소식, 채식, 군것질, 인스턴트 식품, 잡곡, 과자, 야채) and asks you to group them into Healthy Eating Habits and Unhealthy Eating Habits. My grouping:",
             tables=[table(["Healthy eating habits", "Unhealthy eating habits"], [[a, b] for a, b in zip(_HEALTHY, _UNHEALTHY)], say=[0, 1])]),
        card("Activity 1: match the clues with the words",
             "The book gives eight clues and eight words to match by drawing lines (the matches are mine; the English is mine).",
             tables=[table(["Clue", "Word", "English"], [[a, b, c] for a, b, c in _CLUE], say=[0, 1])]),
        card("Activity 3: a journal entry about a trip to a longevity village",
             "The journal entry has eight blanks and a word list (노인 웰빙 칼로리 채식 비율 야외 군것질 육류); the book glosses 결심하다: to decide. The text below is completed with the answers (mine), in this order: 비율, 노인, 채식, 야외, 육류, 칼로리, 군것질, 웰빙; 80세 and 105세 are spelled out. The English is mine.",
             examples=passage(_JRN)),
        card("Activities left out", "Activity 2 and Activity 4 (SMART Board), the PowerPoint presentation on Sino-Korean words and Activity 5 (the 끝말 잇기 word-chain game, played standing in a circle and timed) are computer and game activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w, _ in _VB1] + ["소식", "채식", "잡곡", "편식", "군것질", "과자"]))
        + _tr(_JRN[1:], k=3)
        + [M("Which group is “" + b + "”?", "Healthy eating habits" if b in _HEALTHY else "Unhealthy eating habits", ["Unhealthy eating habits" if b in _HEALTHY else "Healthy eating habits"], "My grouping.") for b in _HEALTHY + _UNHEALTHY[:3]]
        + [M("Which word matches the clue “" + a + "”?", b, [x[1] for x in _CLUE if x[1] != b][:3], "The book’s clue.") for a, b, c in _CLUE]
        + [F("돼지고기, 소고기, 닭고기 = ___ (meat)", "육류", ["채식", "과자"], "육류."), F("건강하게 오래 산다 = ___ (longevity)", "장수", ["비만", "소식"], "장수."), F("좋아하는 음식만 골라서 먹는다 = ___ (unhealthy diet)", "편식", ["소식", "채식"], "편식."), F("그곳은 연세 많은 분들의 ___이 아주 높았다. (proportion)", "비율", ["칼로리", "체지방"], "비율."), F("나는 칼로리가 높은 음식도 많이 먹었다. 그리고 ___도 많이 했다. (snacking)", "군것질", ["채식", "소식"], "군것질."), F("그곳에 사는 분들은 ___이나 소식을 하셨다. (vegetarian diet)", "채식", ["육류", "과자"], "채식."), F("나는 건강에 좋은 ___식생활을 하기로 결심했다. (well-being)", "웰빙", ["오토캠핑", "햄버거"], "웰빙."),
           read_q("장수마을"), read_q("야외활동을 많이 하면서 건강을 유지하고 계셨다"), read_q("나는 거기서 나쁜 내 식습관을 알게 되었다"), read_q("체지방"), read_q("오토캠핑")]
    ),
)

# ================================================================== L3: Topic A
_A_TXT = [
    ("장수의 첫 번째 비결은 좋은 식습관입니다.", "The first secret of longevity is good eating habits."),
    ("장수하는 사람들은 주로 채식을 합니다.", "People who live long mainly eat vegetables."),
    ("그리고 소식을 하고 식사를 거르지 않습니다.", "And they eat lightly and do not skip meals."),
    ("또, 콩과 보리쌀을 섞은 잡곡밥을 매일 먹습니다.", "Also, they eat mixed-grain rice with beans and barley every day."),
    ("쇠고기나 돼지고기는 별로 먹지 않고 생선을 자주 먹습니다.", "They do not eat much beef or pork and often eat fish."),
    ("두 번째는 부지런한 생활습관입니다.", "The second is a diligent lifestyle."),
    ("장수하는 사람들은 항상 일찍 일어나서 부지런히 몸을 움직입니다.", "People who live long always get up early and move their bodies diligently."),
    ("그리고 집안일도 하고 밖에서 일도 합니다.", "And they do housework and also work outside."),
    ("세 번째 장수 비결은 좋은 자연환경에서 다른 사람들과 잘 지내는 것입니다.", "The third secret of longevity is to get along well with other people in a good natural environment."),
    ("장수마을은 주로 아름다운 자연 속에 있습니다.", "Longevity villages are mostly in the midst of beautiful nature."),
    ("장수마을 사람들은 늘 아름다운 자연 속에서 살아서 성격도 낙천적입니다.", "The people of longevity villages always live in beautiful nature, so their personalities are also optimistic."),
    ("마을 사람들과 자주 이야기도 나누고 항상 즐겁게 생활합니다.", "They often chat with the people of the village and always live cheerfully."),
]
_A_WORDS = ["거르다", "낙천적", "노인", "마을 / 촌", "보리 / 보리쌀", "비결", "비율", "섞다", "소식", "움직이다", "육류", "자연", "잡곡", "장수", "채식", "콩", "태도"]
_TIPS = [("깨끗한 자연환경 속에서 삽니다.", "Live in a clean natural environment."), ("적당히 쉬고 매일 여섯 시간에서 여덟 시간 동안 잠을 잡니다.", "Rest adequately and sleep six to eight hours every day."), ("스트레스를 풀 수 있는 취미활동을 합니다.", "Do hobby activities that can relieve stress."), ("채식을 주로 합니다.", "Mainly eat vegetables."), ("소식을 합니다.", "Eat lightly."), ("가벼운 운동을 규칙적으로 합니다.", "Exercise lightly and regularly."), ("공기 좋은 곳에 가서 맑은 공기를 마십니다.", "Go to a place with good air and breathe clean air."), ("부지런히 일을 합니다.", "Work diligently."), ("가족들과 자주 대화합니다.", "Talk often with your family."), ("콩이나 보리쌀 등 잡곡을 섞은 밥을 먹습니다.", "Eat rice mixed with grains such as beans and barley."), ("긍정적인 생각과 낙천적인 태도를 가지고 생활합니다.", "Live with positive thoughts and an optimistic attitude.")]
L3 = lesson(
    "Ch 32 · Topic A: People who live long mainly eat vegetables (장수하는 사람들은 주로 채식을 합니다)",
    "장수의 비결 · 채식 · 소식 · 잡곡밥 · 부지런한 생활습관 · 자연환경 · 낙천적",
    requires=[],
    cards=[
        card("Topic A: People who live long mainly eat vegetables (장수하는 사람들은 주로 채식을 합니다)",
             "A reporter on a radio show is talking about longevity. (The English is mine; the book gives none.)",
             examples=passage(_A_TXT)),
        card("The book’s footnotes", "쇠고기 can be used interchangeably with 소고기. 장수마을 literally means “a longevity village”. This term refers to a community of people whose average lifespan is significantly longer than the national average."),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 소식(하다), 장수(하다) and 채식(하다) take the form in parentheses.", tables=[ktable(_rows(_A_WORDS))]),
        card("Reading and writing: tips for a long, healthy life",
             "The book lists eleven tips (건강한 삶을 위해서…) and asks you to sort them into three categories, writing the numbers in the first row and the key Korean words in the second; the first is done for you (sentence 1: 깨끗한 자연환경; the book glosses 적당하다: to be adequate, to be appropriate). The tips below have 6~8시간 spelled out; the English and my sorting are below.",
             examples=passage(_TIPS)),
        card("The sorting (mine)", "The book leaves the table blank apart from sentence 1; these are my answers.",
             tables=[table(["Category", "Sentence numbers", "Key words / phrases"], [["Environmental elements", "1, 7", "깨끗한 자연환경; 맑은 공기"], ["Eating habits", "4, 5, 10", "채식; 소식; 잡곡을 섞은 밥"], ["Lifestyle and attitudes", "2, 3, 6, 8, 9, 11", "적당히 쉬고 잠을 잠; 취미활동; 가벼운 운동; 부지런히 일을 함; 가족과 대화; 긍정적인 생각과 낙천적인 태도"]])]),
        card("Activities left out", "The SMART Board activities, the reading and listening study of the passage and Follow-up 2 (listening to three question-and-answer segments between a health-care professional and attendees) are computer and audio activities. Activity 1 (Taboo, a PowerPoint game) is a game."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT + _TIPS, k=3)
        + [M("What is the first secret of longevity?", "Good eating habits", ["Exercise", "Medicine", "Money"], "첫 번째 비결은 좋은 식습관."), M("What do people who live long mainly eat?", "Vegetables", ["Meat", "Sweets", "Fast food"], "주로 채식."), M("What do they do about meals?", "Eat lightly and do not skip meals", ["Skip breakfast", "Overeat", "Eat late"], "소식, 식사를 거르지 않습니다."), M("What do they eat every day?", "Mixed-grain rice with beans and barley", ["White rice only", "Noodles", "Bread"], "잡곡밥."), M("What do they eat rarely, and what often?", "Rarely beef and pork; often fish", ["Often beef", "Often pork", "Rarely fish"], "별로 먹지 않고 생선을 자주."), M("What is the second secret?", "A diligent lifestyle", ["Good food", "A good attitude", "Wealth"], "부지런한 생활습관."), M("What is the third secret?", "Getting along well with others in a good natural environment", ["Medicine", "Travel", "Work"], "좋은 자연환경에서 다른 사람들과 잘 지내는 것."), M("Why is the personality of the villagers optimistic?", "They always live in beautiful nature", ["They are rich", "They are young", "They sleep a lot"], "아름다운 자연 속에서 살아서."),
           F("장수하는 사람들은 주로 ___을 합니다. (vegetarian diet)", "채식", ["편식", "과식"], "채식."), F("그리고 소식을 하고 식사를 ___ 않습니다. (skip)", "거르지", ["섞지", "끌지"], "거르다."), F("콩과 보리쌀을 ___ 잡곡밥을 매일 먹습니다. (mixed)", "섞은", ["거른", "끈"], "섞다."), F("장수 ___ 중 첫 번째는 좋은 식습관입니다. (secret)", "비결", ["태도", "비율"], "비결."), F("성격도 ___입니다. (optimistic)", "낙천적", ["부정적", "예민"], "낙천적."),
           read_q("장수의 첫 번째 비결은 좋은 식습관입니다"), read_q("장수하는 사람들은 주로 채식을 합니다"), read_q("부지런히 몸을 움직입니다"), read_q("항상 즐겁게 생활합니다"), read_q("가족들과 자주 대화합니다")]
    ),
)

# ================================================================== L4: Activity 2 survey report
_SRV = [("장수 마을의 장수 비결 조사", "A survey of the secrets of longevity in longevity villages"), ("서울대 고령사회연구소는 전북 순창군 등에서 장수 비결에 대한 조사를 하고 있다.", "The Institute for Aging Society at Seoul National University is conducting a survey on the secrets of longevity in places such as Sunchang County in North Jeolla Province."), ("이 연구소는 국내 대표적인 네 개 장수지역에서 육십오 세 이상 천여 명을 대상으로 조사하고 있다.", "This institute is surveying about one thousand people aged sixty-five or older in four representative longevity regions in Korea."), ("이 연구소는 지난 십오 일부터 다음 달 일 일까지 이 지역 장수노인 가정을 직접 방문한다.", "From the fifteenth of last month to the first of next month, this institute is visiting the homes of the longevity elderly in these regions in person."), ("그리고 장수 노인들의 식습관, 건강상태, 생활방식 등을 조사한다.", "And it surveys the longevity elderly’s eating habits, health condition, lifestyle and so on."), ("이 연구소는 조사를 통해 건강한 노인과 건강하지 않은 노인들의 차이를 비교한다.", "Through the survey, this institute compares the differences between healthy and unhealthy elderly people."), ("그리고 건강과 장수를 위한 식생활 모델을 만들 계획이다.", "And it plans to make a dietary model for health and longevity."), ("순창군은 전국 이백삼십사 개 지역 중 백 세 이상 노인의 비율이 전국에서 가장 높다.", "Among the two hundred and thirty-four regions nationwide, Sunchang County has the highest proportion of elderly people aged one hundred or older in the whole country.")]
L4 = lesson(
    "Ch 32 · Activity 2: a survey report on the secrets of longevity (장수 마을의 장수 비결 조사)",
    "서울대 고령사회연구소 · 순창군 · 장수노인 · 식습관 · 건강상태 · 생활방식 · 식생활 모델",
    requires=[],
    cards=[
        card("Activity 2 (Reading): a survey report on the secrets of longevity",
             "The following survey report, conducted by the 고령사회연구소 (Institute for Aging Society) at Seoul National University, is about living a long, healthy life. The book asks you to circle the words you don’t know and look them up (it glosses 연구소: a research institute; 차이: difference). The text is the book’s with the numbers and dates spelled out in Hangul; the book writes 건강·장수를 and the middle dot is read “and”, so it is written 건강과 장수를 here. The English is mine.",
             examples=passage(_SRV)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Question", "Answer (mine)"], [["1. What is the purpose of the survey?", "To find the secrets of longevity (their eating habits, health and lifestyle), compare healthy and unhealthy elderly people, and make a dietary model for health and longevity"], ["2. Who were the participants?", "About 1,000 people aged 65 or older in four representative longevity regions in Korea (including Sunchang County, North Jeolla Province)"], ["3. How was the survey conducted?", "By visiting the homes of the longevity elderly in person, from the 15th of last month to the 1st of next month"], ["4. What are the survey topics?", "The elderly’s eating habits, health condition and lifestyle"], ["5. What was said about Sunchang County?", "It has the highest proportion of people aged 100 or older among the 234 regions nationwide"]])]),
        card("Activities left out", "Activity 3 (listening to three interviews with senior citizens) and Activity 4 (reading two news articles, Article A and Article B, in two groups and exchanging the information in pairs) need audio, articles that are not in the book’s text, and classmates."),
    ],
    exercises=uniq(
        _tr(_SRV, k=3)
        + [M("Which institute is doing the survey?", "The Institute for Aging Society at Seoul National University", ["A hospital", "The army", "A school"], "서울대 고령사회연구소."), M("Where is the survey being done?", "Four representative longevity regions, including Sunchang County", ["Seoul", "Busan", "One hospital"], "순창군 등."), M("How many people aged 65 or older are surveyed?", "About one thousand", ["About ten", "About a million", "About a hundred"], "천여 명."), M("How is the survey conducted?", "The institute visits the elderly’s homes in person", ["By phone", "By mail", "On the internet"], "직접 방문한다."), M("What does the institute compare?", "Healthy and unhealthy elderly people", ["Young and old", "Cities and villages", "Men and women"], "건강한 노인과 건강하지 않은 노인."), M("What does it plan to make?", "A dietary model for health and longevity", ["A hospital", "A medicine", "A school"], "식생활 모델."), M("What is special about Sunchang County?", "The highest proportion of people over one hundred", ["The most cities", "The most schools", "The biggest hospital"], "백 세 이상 노인의 비율이 가장 높다."),
           F("이 연구소는 장수 노인 가정을 ___ 방문한다. (in person)", "직접", ["간접", "거의"], "직접."), F("장수 노인들의 식습관, 건강상태, ___ 등을 조사한다. (lifestyle)", "생활방식", ["식생활", "비율"], "생활방식."), F("건강한 노인과 건강하지 않은 노인들의 ___를 비교한다. (difference)", "차이", ["효과", "태도"], "차이."), F("순창군은 백 세 이상 노인의 ___이 가장 높다. (proportion)", "비율", ["양", "열량"], "비율."), F("연구소는 장수 비결에 대한 ___를 하고 있다. (survey)", "조사", ["진단", "문의"], "조사."),
           read_q("서울대 고령사회연구소"), read_q("장수 비결에 대한 조사를 하고 있다"), read_q("장수 노인 가정을 직접 방문한다"), read_q("식생활 모델을 만들 계획이다"), read_q("순창군은 백 세 이상 노인의 비율이 가장 높다")]
    ),
)

# ================================================================== L5: Topic B
_B_DLG = [
    ("엄마", "제현이 비만 검사 결과가 나왔어요?", "Have Jehyeon’s obesity test results come out?"),
    ("건강관리사", "네, 체지방이 조금 높네요. 제현이의 식습관이 어떻습니까?", "Yes, his body fat is a little high. What are Jehyeon’s eating habits like?"),
    ("엄마", "제현이는 간식을 너무 좋아해요. 특히 과자나 사탕을 많이 먹어요. 그리고 채소와 생선은 잘 안 먹어요.", "Jehyeon likes snacks too much. He especially eats a lot of cookies and candy. And he doesn’t eat vegetables and fish well."),
    ("건강관리사", "운동은 자주 합니까?", "Does he exercise often?"),
    ("엄마", "아니요, 거의 안 해요. 운동을 아주 싫어하거든요.", "No, he hardly does. He hates exercise a lot, you see."),
    ("건강관리사", "건강에 안 좋은 습관을 가지고 있군요. 그럼, 비만이 되기 쉬워요.", "I see he has habits that are not good for health. Then it is easy for him to become obese."),
    ("엄마", "그래요? 비만을 예방하려면 어떻게 해야 하나요?", "Is that so? What should we do to prevent obesity?"),
    ("건강관리사", "여러 가지 영양소를 균형 있게 섭취해야 해요. 편식을 못 하게 하시고 음식을 골고루 먹이세요.", "You must take in various nutrients in a balanced way. Don’t let him be a picky eater, and feed him a variety of food evenly."),
    ("엄마", "네, 알겠습니다.", "Yes, I understand."),
    ("건강관리사", "그리고 운동도 규칙적으로 하게 하세요. 운동할 때는 땀이 날 때까지 하면 더 좋습니다.", "And also make him exercise regularly. When he exercises, it is better to go on until he sweats."),
    ("엄마", "운동은 얼마나 하는 게 좋아요?", "How much exercise is good?"),
    ("건강관리사", "적어도 일주일에 세 번 이상 하면 비만 예방에 효과가 있습니다.", "If he does it at least three times a week, it is effective in preventing obesity."),
]
_B_WORDS = ["간식", "-거든요", "거의", "건강관리사", "-게 하다", "골고루", "과자", "군것질", "균형", "땀", "사탕", "섭취", "양 / 량", "열량 / 칼로리", "영양소", "인스턴트 식품", "적어도", "조절", "지방", "체지방", "초콜릿", "편식", "효과"]
L5 = lesson(
    "Ch 32 · Topic B: What are Jehyeon’s eating habits like? (제현이의 식습관이 어떻습니까?)",
    "제현이의 식습관이 어떻습니까 · 체지방 · 간식 · 영양소를 균형 있게 · 편식을 못 하게 · 운동도 규칙적으로 하게 하세요",
    requires=[],
    cards=[
        card("Topic B: What are Jehyeon’s eating habits like? (제현이의 식습관이 어떻습니까?)",
             "A health and nutrition counselor is giving advice to the mother of a teenager who has had a childhood obesity checkup. (The English is mine; the book gives none; 3번 is spelled out.)",
             examples=dlg(_B_DLG)),
        card("The book’s footnote", "관리사 in 건강관리사 (health and nutrition counselor; health-care specialist) means a specialist, as in 피부관리사 (a skin-care specialist) or 보험관리사 (an insurance agent)."),
        card("한국에서는: 어린이 군것질 (children’s snacks)",
             "On the way home from school, many Korean children stop for snacks at food stands where street foods, such as 떡볶이 (rice cake cooked in spicy sauce) or 튀김 (deep-fried assortments), are available. Children also stop to eat at fast-food restaurants. According to a survey conducted in 2009 by the Seoul City Administrations, 46% of elementary school students purchase snacks on the way home from school once or twice a week. (The book adds a pie chart of children’s favorite snacks from 데이터뉴스, which is a picture and is left out.)"),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); 군것질(하다), 균형(잡다), 땀(이 나다 / 을 흘리다), 섭취(하다) and 조절(하다) take the forms in parentheses; –게 하다 and –거든요 are explained in the grammar.",
             tables=[ktable(_rows([w for w in _B_WORDS if _HG(w)])), table(["Pattern", "Meaning"], [["-게 하다", "have/make … do …"], ["-거든요", "informal sentence ending"]])]),
        card("Activities left out", "The SMART Board activities, the study with audio and Follow-up 2 (listening to two phone conversations between a client and a health and nutrition counselor) are computer and audio activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG), k=3)
        + [M("What did the obesity test show about 제현이?", "His body fat is a little high", ["He is underweight", "He is healthy", "He has a cold"], "체지방이 조금 높네요."), M("What does 제현이 like too much?", "Snacks, especially cookies and candy", ["Vegetables", "Fish", "Exercise"], "간식을 너무 좋아해요."), M("What does 제현이 not eat well?", "Vegetables and fish", ["Candy", "Cookies", "Rice"], "채소와 생선은 잘 안 먹어요."), M("Why does 제현이 hardly exercise?", "He hates exercise", ["He is sick", "He has no time", "He is lazy at school"], "운동을 아주 싫어하거든요."), M("What should he take in in a balanced way?", "Various nutrients", ["Only protein", "Only vitamins", "Water"], "여러 가지 영양소."), M("What should his mother not let him do?", "Be a picky eater", ["Sleep", "Study", "Play"], "편식을 못 하게 하시고."), M("How long should he exercise?", "Until he sweats", ["One minute", "All day", "Until bedtime"], "땀이 날 때까지."), M("How often should he exercise at least?", "Three times a week or more", ["Once a month", "Once a year", "Every hour"], "일주일에 세 번 이상."),
           F("제현이는 ___을 너무 좋아해요. (snacks)", "간식", ["운동", "채소"], "간식."), F("체___이 조금 높네요. (body fat)", "지방", ["중력", "비율"], "체지방."), F("음식을 ___ 먹이세요. (evenly)", "골고루", ["거의", "적어도"], "골고루."), F("___ 일주일에 세 번 이상 하면 효과가 있습니다. (at least)", "적어도", ["거의", "골고루"], "적어도."), F("영양소를 ___ 있게 섭취해야 해요. (balance)", "균형", ["태도", "효과"], "균형 있게."),
           read_q("제현이의 식습관이 어떻습니까"), read_q("운동을 아주 싫어하거든요"), read_q("여러 가지 영양소를 균형 있게 섭취해야 해요"), read_q("편식을 못 하게 하시고 음식을 골고루 먹이세요"), read_q("운동도 규칙적으로 하게 하세요")]
    ),
)

# ================================================================== L6: self-assessment and news phrases
_SELF = [("식사는 규칙적으로 하는 편이다.", "I tend to eat regularly."), ("하루에 열 가지 이상의 식품을 섭취한다.", "I take in ten or more kinds of food a day."), ("하루에 육류, 생선, 콩으로 된 음식을 세 가지 이상 먹는다.", "I eat three or more kinds of food made of meat, fish or beans a day."), ("김치 이외의 채소를 식사할 때마다 먹는다.", "I eat vegetables other than kimchi at every meal."), ("우유와 같은 유제품을 매일 먹는다.", "I eat dairy products such as milk every day."), ("과일이나 과일주스를 매일 먹는다.", "I eat fruit or fruit juice every day."), ("반찬에 소금이나 간장을 넣는 때가 많다.", "I often put salt or soy sauce in side dishes."), ("튀김이나 볶음요리를 많이 먹는 편이다.", "I tend to eat a lot of fried or stir-fried dishes."), ("간식으로 아이스크림, 단 과자, 스낵류를 많이 먹는다.", "For snacks I eat a lot of ice cream, sweet cookies and snacks."), ("콜라, 사이다 등 탄산음료, 커피 등을 매일 세 번 이상 마신다.", "I drink carbonated drinks such as cola and cider, coffee and so on, three or more times a day.")]
_NEWS = [("운동할 시간이 따로 없어서", "because there is no separate time to exercise"), ("청소년 비만 증가", "an increase in adolescent obesity"), ("아침을 먹지 않는 청소년", "adolescents who don’t eat breakfast"), ("땀을 흘릴 정도의 운동", "exercise to the point of sweating"), ("영양은 높고 칼로리는 낮은 음식", "food that is high in nutrition and low in calories")]
L6 = lesson(
    "Ch 32 · Topic B follow-up: an eating-habits self-assessment and news phrases",
    "식습관 자가진단 · 규칙적으로 · 유제품 · 튀김 · 탄산음료 · 청소년 비만 · 땀을 흘릴 정도의 운동",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): 나의 식습관은 몇 점일까? (a self-assessment of eating habits)",
             "The book gives a self-assessment (식습관 자가진단) of dietary patterns and lifestyle choices: read it, rate how healthy your eating habits are and identify areas that can be improved. The ten statements (the book’s, with the numbers spelled out; the English is mine):",
             examples=passage(_SELF)),
        card("How it is scored, and the results",
             "Scoring (평가방법): for statements 1 to 6, answering “예” (yes) scores +1 and answering “아니요” (no) scores −1; for statements 7 to 10, “예” scores −1 and “아니요” scores +1. Add up the total.",
             tables=[table(["Score", "Result (the book’s Korean, from Korea.kr)", "English (mine)"], [["7~10점", "좋은 식습관, 잘못된 식습관 항목에 대해선 교정 필요", "Good eating habits; the items with wrong habits need correcting"], ["4~6점", "전체적으로 식습관을 고치기 위한 노력 필요", "Effort is needed to correct your eating habits overall"], ["3점 미만", "나쁜 식습관, 식생활 전문가와 상담 필요", "Bad eating habits; consult a dietary specialist"]])]),
        card("Activity 2a (Reading): phrases from a news clip",
             "The book gives five phrases from a news clip you listen to afterwards and asks you to translate them (the English is mine).",
             tables=[table(["Phrase", "English (mine)"], [[a, b] for a, b in _NEWS], say=[0])]),
        card("Activities left out", "Activity 1 (SMART Board), Activity 2b (listening to three YTN news clips and marking the main idea) and Activity 3 (a counseling interview, Text A and Text B, in pairs, ending in a flip-chart presentation) need audio, texts that are not in the book’s text, and classmates."),
    ],
    exercises=uniq(
        _tr(_SELF + _NEWS, k=3)
        + [M("Which answers score +1 for statements 1 to 6?", "“예” (yes)", ["“아니요” (no)", "Neither", "Both"], "The scoring method."), M("Which answers score +1 for statements 7 to 10?", "“아니요” (no)", ["“예” (yes)", "Neither", "Both"], "The scoring method."), M("Why do statements 7 to 10 reverse the scoring?", "They describe unhealthy habits", ["They are easier", "They are about drinks", "They are not important"], "Salt, fried food, sweets, soda."), M("What should a score under 3 do?", "Consult a dietary specialist", ["Eat less", "Ignore it", "Exercise more only"], "식생활 전문가와 상담 필요."), M("What does 땀을 흘릴 정도의 운동 mean?", "exercise to the point of sweating", ["exercise in summer", "sweaty clothes", "no exercise"], "News phrase."),
           F("식사는 규칙적으로 하는 ___이다. (tend to)", "편", ["데", "것"], "-는 편이다."), F("김치 ___의 채소를 식사할 때마다 먹는다. (other than)", "이외", ["이상", "이하"], "이외."), F("우유와 같은 ___를 매일 먹는다. (dairy products)", "유제품", ["육류", "잡곡"], "유제품."), F("___이나 볶음요리를 많이 먹는 편이다. (fried food)", "튀김", ["과일", "채소"], "튀김."), F("___ 비만 증가 (adolescent)", "청소년", ["어린이", "노인"], "청소년."),
           read_q("나의 식습관은 몇 점일까"), read_q("식사는 규칙적으로 하는 편이다"), read_q("과일이나 과일주스를 매일 먹는다"), read_q("반찬에 소금이나 간장을 넣는 때가 많다"), read_q("영양은 높고 칼로리는 낮은 음식")]
    ),
)

# ================================================================== L7: Grammar A: causative -게 하다
_CA1 = [("나는 동생에게 매일 방을 청소하게 했어요.", "I had my younger brother clean the room every day."), ("나는 학생들에게 숙제를 하게 할 거예요.", "I will make the students do their homework."), ("선생님이 저에게 사무실 전화를 사용하게 하셨어요.", "The teacher let me use the office phone.")]
_CA2 = [("반장이 학생 한 명에게 칠판을 지우게 했어요.", "The section leader made a student erase the board."), ("엄마가 동생한테 아침마다 운동을 하게 했어요.", "My mom made my brother work out every morning.")]
_CA3 = [("나는 동생에게 매일 방을 청소하게 했어요.", "I had my younger brother clean the room every day."), ("나는 동생이 매일 방을 청소하게 했어요.", "(the same meaning, with the subject marker 이)"), ("나는 동생을 매일 방을 청소하게 했어요.", "(the same meaning, with the object marker 을)")]
_CA4 = [("제가 진수한테 차를 고치게 했어요.", "I got Jinsoo to fix the car."), ("제가 진수에게 차를 고치도록 했어요.", "I got Jinsoo to fix the car (with –도록 하다).")]
_DUTY = [("교실 문을 열다", "to open the classroom door", "교실 문을 열게"), ("책상을 정리하다", "to arrange the desks", "책상을 정리하게"), ("칠판을 지우다", "to erase the board", "칠판을 지우게"), ("교실을 청소하다", "to clean the classroom", "교실을 청소하게"), ("쓰레기를 버리다", "to throw away the trash", "쓰레기를 버리게")]
_DOC = [("요즘 체중에 문제가 있는 어린이들이 많습니다.", "These days there are many children with weight problems."), ("어릴 때부터 좋은 식습관을 기르는 것이 중요합니다.", "It is important to build good eating habits from childhood."), ("아이들에게 음료수 대신에 물이나 우유를 마시게 하세요.", "Make children drink water or milk instead of soft drinks."), ("또 지방이 많은 음식보다는 신선한 채소를 많이 먹게 하세요.", "Also make them eat a lot of fresh vegetables rather than fatty food."), ("간식은 과자나 케이크보다는 과일이 좋습니다.", "For snacks, fruit is better than cookies or cake."), ("그리고 매일 규칙적으로 운동을 하게 하세요.", "And make them exercise regularly every day."), ("그럼 체중이 크게 늘지 않을 거예요.", "Then their weight will not increase much."), ("체중이 늘면 여러 가지 건강 문제가 생깁니다.", "If weight increases, various health problems arise."), ("아이들에게 어릴 때부터 좋은 생활습관을 갖게 하세요.", "Make children have good lifestyle habits from childhood.")]
_CAV = [("청소하다", "to clean", "청소하게 하세요"), ("마시다", "to drink", "마시게 하세요"), ("먹다", "to eat", "먹게 하세요"), ("갖다", "to have", "갖게 하세요"), ("지우다", "to erase", "지우게 하세요"), ("사용하다", "to use", "사용하게 하세요"), ("고치다", "to fix", "고치게 하세요"), ("하다", "to do", "하게 하세요")]
L7 = lesson(
    "Ch 32 · Grammar A: the causative –게 하다, to have/make/let someone do",
    "~에게 -게 하다 · ~한테 -게 하다 · 청소하게 했어요 · 마시게 하세요 · -도록 하다",
    requires=[],
    cards=[
        card("Expressing a causative",
             "A causative sentence is one in which the subject (or agent) causes or forces the object to perform an action or to be in a certain condition. For example, “The teacher made his students remain silent.” In English we normally express a causative using verbs like have, make, let, or get. In Korean, we express a causative using ~에게/한테 … –게 하다. Note that the object marked by 에게/한테 is followed by the verb –게 하다. Depending on the context, this translates to have, make, or let. The pattern: ~한테/에게 … verb stem + 게 하다. (The English is the book’s.)",
             examples=passage(_CA1)),
        card("More examples", "The book’s further examples (the English is the book’s):", examples=passage(_CA2)),
        card("Notes (참고)",
             "1. ~에게/한테 attached to the object can be replaced by the subject marker 이/가 or the object marker 을/를. However, ~에게/한테 is preferred over ~이/가 and ~을/를.\n\n"
             "2. Recall from Chapter 29 that –도록 하다 means “make sure”. It is also used to imply “have someone do something”.",
             examples=passage(_CA3 + _CA4)),
        card("Forms (mine)", "Verb stem + 게 하다; the table uses the polite request –게 하세요 (“make/have them …”).",
             tables=[table(["Verb", "Meaning", "-게 하세요"], [list(r) for r in _CAV], say=[0, 2])]),
        card("Follow-up 1 (Speaking and listening): who will do each duty?",
             "In pairs, one partner is a section leader who must fairly distribute each assignment to everyone in the class. Partner A asks “누구에게 … –게 할까요?” and Partner B answers “~에게 … –게 합시다.” The book’s model (the English is mine):",
             examples=dlg([("A", "누구에게 칠판을 지우게 할까요?", "Whom shall we make erase the board?"), ("B", "김 일병에게 칠판을 지우게 합시다.", "Let’s make Private First Class Kim erase the board.")]),
             tables=[table(["Duty / assignment", "Meaning"], [[a, b] for a, b, c in _DUTY], say=[0])]),
        card("Follow-up 2 (Reading): a doctor’s advice about nutrition",
             "Read the doctor’s advice, circle the grammar feature –게 하다 and translate the sentences containing it into English (the four sentences with 게 하세요 are the third, fourth, sixth and ninth below; the book glosses 우유: milk). The English is mine.",
             examples=passage(_DOC)),
        card("Activities left out", "Follow-up 5 (a parent and a counselor role-play) needs a partner; the book’s model is: 저희 아들이 요즘 체중이 늘었거든요. 어떻게 해야 해요? — 매일 삼십 분씩 운동을 하게 하세요. 그리고 칼로리가 높은 음식은 피하게 하세요. (The parent’s problem uses –거든요, the next lesson; the counselor’s advice uses –게 하다. 30분 is spelled out.)"),
    ],
    exercises=uniq(
        _tr(_CA1 + _CA2 + _CA4[:1] + _DOC[2:4] + _DOC[5:6] + _DOC[8:], k=3)
        + [M("누구에게 " + c + " 할까요? means:", "Whom shall we make " + b.replace("to ", "") + "?", ["Who will I meet?", "Where shall we go?", "When shall we eat?"], "–게 하다.") for a, b, c in _DUTY]
        + [F("나는 동생에게 매일 방을 청소하___ 했어요. (-게)", "게", ["도록", "는"], "-게 하다."), F("선생님이 저에게 사무실 전화를 사용하게 ___. (made/let me)", "하셨어요", ["보셨어요", "가셨어요"], "하다 + 시 + 었어요."), F("반장이 학생 한 명___ 칠판을 지우게 했어요. (to)", "에게", ["에서", "까지"], "에게."), F("엄마가 동생___ 아침마다 운동을 하게 했어요. (to)", "한테", ["에서", "보다"], "한테."), F("제가 진수에게 차를 고치___ 했어요. (-도록)", "도록", ["거든", "는데"], "-도록 하다."), F("매일 규칙적으로 운동을 하___ 하세요. (-게)", "게", ["고", "면"], "-게 하세요."), F("아이들에게 좋은 생활습관을 갖___ 하세요. (-게)", "게", ["도", "고"], "갖게 하세요."),
           M("What does a causative sentence express?", "The subject makes/has/lets the object do something", ["The subject wants to do something", "The subject tried something", "The subject saw something"], "The book’s note."), M("Which particle marks the person who does the action in a causative?", "에게/한테", ["에서", "까지", "처럼"], "~에게/한테 … –게 하다."), M("Which is preferred: 에게/한테, 이/가 or 을/를?", "에게/한테", ["이/가", "을/를", "All are equal"], "The book’s note."), M("What else can –도록 하다 imply besides “make sure”?", "Have someone do something", ["Try to do", "Want to do", "Be able to do"], "The book’s note."),
           read_q("나는 동생에게 매일 방을 청소하게 했어요"), read_q("선생님이 저에게 사무실 전화를 사용하게 하셨어요"), read_q("누구에게 칠판을 지우게 할까요"), read_q("아이들에게 음료수 대신에 물이나 우유를 마시게 하세요"), read_q("그리고 매일 규칙적으로 운동을 하게 하세요")]
    ),
)

# ================================================================== L8: Grammar B: -거든(요)
_GE1 = [("요즘 왜 체육관에 안 오세요?", "Why aren’t you coming to the gym these days?"), ("제가 좀 바쁘거든요.", "Because I am a little busy."), ("요즘 제가 체육관에 잘 안 가요.", "I don’t go to the gym often these days,"), ("제가 좀 바쁘거든요.", "for I am a little busy.")]
_GE2 = [("시내에 커피숍이 하나 있거든요.", "There is a coffee shop downtown, you know."), ("거기에서 만나요.", "Let’s meet over there."), ("시험 기간이거든요.", "It is exam time, you know."), ("그래서 파티에 못 가요.", "So I cannot go to the party.")]
_GE3 = [("저도 알거든요.", "I know that too (so stop lecturing)."), ("저도 한국말을 잘 할 수 있거든요.", "I too can speak Korean well (so don’t boast).")]
_GE4 = [("이번 주말에 산호세에 왜 가요?", "Why are you going to San Jose this weekend?"), ("음악회가 있거든요.", "Because there is a concert."), ("토요일 오후에 야구경기가 있거든요.", "Because there is a baseball game on Saturday afternoon.")]
_GEF = [("바쁘다", "to be busy", "바쁘거든요"), ("있다", "to exist; to have", "있거든요"), ("좋아하다", "to like", "좋아하거든요"), ("싫어하다", "to hate", "싫어하거든요"), ("시험 기간이다", "to be exam time", "시험 기간이거든요"), ("늘다", "to increase", "늘었거든요"), ("일이 많다", "to have a lot of work", "일이 많거든요")]
L8 = lesson(
    "Ch 32 · Grammar B: the sentence ending –거든(요), a reason or background",
    "-거든요 · 바쁘거든요 · 있거든요 · 시험 기간이거든요 · 이유 · 배경 정보",
    requires=[],
    cards=[
        card("The sentence ending –거든(요)",
             "Like the sentence ending –아/어(요), the sentence ending –거든(요) is used in informal settings. However, –거든(요) is mainly used for one of two situations. First, when providing a reason about the statement or question in a conversation, –거든(요) can be translated as “because” or “for”. (The English is the book’s.)",
             examples=passage(_GE1)),
        card("Giving background information",
             "Second, when providing background information for the remark that will follow, –거든(요) translates to “you know” or “you see”. (The English is the book’s.) Because –거든(요) is used to provide a reason or background information, the ending is used only in a statement, never in a question.",
             examples=passage(_GE2)),
        card("With a raised intonation (the book’s footnote)", "–거든(요) with a raised intonation can be used to express the speaker’s annoyance or cynicism (the book marks the rising pitch with ↗).", examples=passage(_GE3)),
        card("Forms (mine)", "Verb or adjective stem (present or past) + 거든요; a noun + 이다 gives –이거든요.",
             tables=[table(["Phrase", "Meaning", "-거든요"], [list(r) for r in _GEF], say=[0, 2])]),
        card("Follow-up 3 (Listening and speaking): the model", "Sitting in a circle, the teacher asks a question and each student answers with –거든(요). The book’s model (the English is mine):", examples=dlg([("선생님", _GE4[0][0], _GE4[0][1]), ("가", _GE4[1][0], _GE4[1][1]), ("나", _GE4[2][0], _GE4[2][1])])),
        card("Activities left out", "Follow-up 4 (listening to four dialogs and marking whether –거든요 gives a reason or background information) is an audio activity; Follow-up 5 (a parent and a counselor role-play) needs a partner."),
    ],
    exercises=uniq(
        _tr(_GE1[1:2] + _GE2 + _GE3 + _GE4[1:], k=3)
        + [M("How is –거든(요) translated when it gives a reason?", "“because” or “for”", ["“although”", "“if”", "“but”"], "The book’s note."), M("How is –거든(요) translated when it gives background information?", "“you know” or “you see”", ["“because”", "“so that”", "“however”"], "The book’s note."), M("Can –거든(요) be used in a question?", "No, only in a statement", ["Yes, always", "Only with a noun", "Only in the past"], "The book’s note."), M("What can –거든(요) with a raised intonation express?", "The speaker’s annoyance or cynicism", ["Joy", "Surprise", "A question"], "The book’s footnote."), M("Which is a reason: 제가 좀 바쁘거든요 or 시내에 커피숍이 하나 있거든요?", "제가 좀 바쁘거든요", ["시내에 커피숍이 하나 있거든요", "Both", "Neither"], "Answers 왜."), M("What does 시험 기간이거든요 mean?", "It is exam time, you know", ["Are you in exam time?", "It will be exam time", "Exams are over"], "-거든요."),
           F("제가 좀 바쁘___. (because)", "거든요", ["는데요", "니까요"], "-거든요."), F("음악회가 있___. (because)", "거든요", ["는데요", "고요"], "-거든요."), F("시험 기간이___. (it is exam time, you know)", "거든요", ["든요", "는데요"], "이다 + 거든요."), F("운동을 아주 싫어하___. (because he hates)", "거든요", ["는데요", "니까요"], "-거든요."), F("저희 아들이 요즘 체중이 늘었___. (because he has gained)", "거든요", ["는데요", "으니까요"], "past + 거든요."),
           read_q("제가 좀 바쁘거든요"), read_q("시내에 커피숍이 하나 있거든요"), read_q("시험 기간이거든요"), read_q("음악회가 있거든요"), read_q("토요일 오후에 야구경기가 있거든요")]
    ),
)

# ================================================================== L9: Topic C
_C_TXT = [
    ("오늘은 웰빙문화에 대해서 알아 보겠습니다.", "Today we will find out about well-being culture."),
    ("와이엠시에이에서는 여름방학을 맞이하여 다양한 웰빙 문화행사를 마련했습니다.", "For the summer vacation, the YMCA has prepared a variety of well-being cultural events."),
    ("첫 번째 행사는, 웰빙 식생활 및 생활습관 프로그램입니다.", "The first event is a well-being diet and lifestyle program."),
    ("전문가가 각 개인의 식생활과 생활습관을 진단해 줍니다.", "A specialist diagnoses each individual’s diet and lifestyle habits."),
    ("그리고 올바른 식단과 생활습관을 추천해 줍니다.", "And they recommend a proper diet and lifestyle habits."),
    ("또 웰빙 유기농 요리교실과 생활체조 교실도 운영할 예정입니다.", "Also, they plan to run a well-being organic cooking class and a daily gymnastics class."),
    ("두 번째 행사는, 웰빙 여가활동 프로그램입니다.", "The second event is a well-being leisure activity program."),
    ("오염된 도시환경에서 벗어나 자연을 직접 체험할 수 있습니다.", "You can get away from the polluted city environment and experience nature firsthand."),
    ("특히 추천할 만한 여가활동은 오토캠핑 및 암벽등반입니다.", "Leisure activities especially worth recommending are car camping and rock climbing."),
    ("오토캠핑은 가족이 함께 참여할 수 있어 많은 사람들이 관심을 보이고 있습니다.", "Many people are showing interest in car camping because the whole family can take part together."),
    ("암벽등반은 젊은 사람들 사이에서 많은 인기를 끌고 있으며, 특히 스트레스를 해소하는 데 효과가 큽니다.", "Rock climbing is attracting a lot of popularity among young people and is especially effective for relieving stress."),
    ("와이엠시에이 웰빙 문화행사에 관심이 있으신 분은 공이에 삼사오에 육칠팔구로 문의하시기 바랍니다.", "If you are interested in the YMCA well-being cultural events, please inquire at 02-345-6789."),
]
_C_WORDS = ["개인", "끌다", "다양", "마련", "맞이하다", "문의", "~및", "벗어나다", "식단", "야외", "여가", "오염", "오토캠핑", "올바르다", "운영", "웰빙", "유기농", "전문가", "직접", "진단", "참여", "프로그램", "해소"]
_WELL = "웰빙 (well-being) is a buzzword in Korea that refers to a healthy lifestyle trend. You see this term in words like 웰빙식품, 웰빙주택, 웰빙라이프, and 웰빙문화. Korea’s 웰빙 boom goes back to early 2002, when a popular television documentary series highlighted the hidden dangers of everyday foods. The current 웰빙 trend is linked to the rise of middle- and upper-class consumers who value health, personal development, and environmental protection. 웰빙 encompasses not only a change in consumption patterns, but also a change in values, indicating a mature, industrialized economy."
L9 = lesson(
    "Ch 32 · Topic C: Are you interested in well-being cultural events? (웰빙 문화행사에 관심이 있으세요?)",
    "웰빙 문화행사에 관심이 있으세요 · 웰빙 식생활 · 여가활동 · 오토캠핑 · 암벽등반 · 스트레스를 해소하는 데 효과가 큽니다",
    requires=[],
    cards=[
        card("Topic C: Are you interested in well-being cultural events? (웰빙 문화행사에 관심이 있으세요?)",
             "A radio reporter is announcing events about well-being. The events are hosted by the YMCA. (The English is mine; the book gives none. YMCA is spelled out as 와이엠시에이, and the phone number 02-345-6789 is spelled out in Hangul, with the hyphens read 에.)",
             examples=passage(_C_TXT)),
        card("한국에서는: 웰빙 (well-being)", _WELL),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 다양(하다), 마련(하다), 문의(하다), 오염(되다), 운영(하다/되다), 진단(하다), 참여(하다) and 해소(하다) take the forms in parentheses; –(으)ㄹ 만하다 and –는 데(에) are explained in the grammar.",
             tables=[ktable(_rows([w for w in _C_WORDS if _HG(w)])), table(["Pattern", "Meaning"], [["~및", "and (also); as well as"], ["-(으)ㄹ 만하다", "be worth (~ing)"], ["-는 데(에)", "for / in / at doing something"]])]),
        card("Activities left out", "The SMART Board activities and Follow-up 2 (listening to two phone conversations in which a caller asks about the YWCA’s programs) are computer and audio activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT, k=3)
        + [M("Who hosts the well-being events?", "The YMCA", ["A school", "The army", "A hospital"], "와이엠시에이."), M("When are the events held?", "During the summer vacation", ["Winter", "Spring", "Autumn"], "여름방학을 맞이하여."), M("What does the first event offer?", "A diet and lifestyle program, with cooking and gymnastics classes", ["Camping only", "A concert", "A race"], "웰빙 식생활 및 생활습관 프로그램."), M("What does a specialist do in the first event?", "Diagnoses each person’s diet and lifestyle and recommends proper ones", ["Cooks for people", "Sells food", "Teaches Korean"], "진단해 줍니다, 추천해 줍니다."), M("What does the second event offer?", "Leisure activities in nature", ["A diet program", "Cooking classes", "A medical exam"], "웰빙 여가활동 프로그램."), M("Which leisure activities are recommended?", "Car camping and rock climbing", ["Golf and tennis", "Swimming and diving", "Skiing"], "오토캠핑 및 암벽등반."), M("Why is car camping popular?", "The whole family can take part together", ["It is cheap", "It is short", "It is indoors"], "가족이 함께 참여할 수 있어."), M("What is rock climbing especially good for?", "Relieving stress", ["Losing weight only", "Making friends", "Sleeping"], "스트레스를 해소하는 데 효과가 큽니다."),
           F("와이엠시에이에서는 다양한 웰빙 문화행사를 ___했습니다. (prepared)", "마련", ["문의", "진단"], "마련하다."), F("전문가가 각 ___의 식생활과 생활습관을 진단해 줍니다. (individual)", "개인", ["식단", "여가"], "개인."), F("___된 도시환경에서 벗어나 자연을 직접 체험할 수 있습니다. (polluted)", "오염", ["운영", "참여"], "오염되다."), F("암벽등반은 젊은 사람들 사이에서 많은 인기를 ___ 있습니다. (attracting)", "끌고", ["벗고", "섞고"], "인기를 끌다."), F("관심이 있으신 분은 ___하시기 바랍니다. (inquire)", "문의", ["해소", "진단"], "문의하다."),
           read_q("웰빙 문화행사에 관심이 있으세요"), read_q("오늘은 웰빙문화에 대해서 알아 보겠습니다"), read_q("전문가가 각 개인의 식생활과 생활습관을 진단해 줍니다"), read_q("오토캠핑 및 암벽등반"), read_q("스트레스를 해소하는 데 효과가 큽니다")]
    ),
)

# ================================================================== L10: Topic C follow-up: expo announcement
_EXPO = [("천안 웰빙식품엑스포가 구월 십일 일부터 이십 일까지 천안 삼거리공원에서 열립니다.", "The Cheonan Well-being Food Expo will be held at Cheonan Samgeori Park from September 11 to 20."), ("이번 엑스포에서는 우리 전통식품과 웰빙 유기농 건강식품을 전시합니다.", "At this expo, our traditional foods and well-being organic health foods will be displayed."), ("또한, 직접 체험할 수 있는 여러 전시관을 운영합니다.", "Also, several exhibition halls where you can experience things firsthand will be operated."), ("웰빙 친환경 식품전시관, 웰빙 식품체험관, 웰빙 건강체험관", "Well-being eco-friendly food exhibition hall, well-being food experience hall, well-being health experience hall."), ("관심 있으신 분들의 많은 참여 부탁드립니다.", "We ask for the participation of many interested people.")]
_BOOTH = [("채식이나 소식 등 장수 식습관과 식품영양 정보를 소개합니다.", "It introduces longevity eating habits such as vegetarian diets and light eating, and food and nutrition information."), ("각 개인의 건강상태를 진단해 주고 그에 따른 올바른 건강식단을 추천해 줍니다.", "It diagnoses each individual’s health condition and recommends a proper healthy diet accordingly."), ("웰빙식품을 직접 보고 만들 수 있도록 전통 두부 만들기, 치즈 만들기 등 웰빙요리교실을 직접 운영합니다.", "So that you can see and make well-being food yourself, it directly runs well-being cooking classes such as making traditional tofu and making cheese."), ("패스트푸드나 인스턴트 식품의 문제점을 보여주고, 오염되지 않은 유기농 친환경 건강식품을 전시합니다.", "It shows the problems of fast food and instant food and displays unpolluted organic eco-friendly health food.")]
L10 = lesson(
    "Ch 32 · Topic C follow-up: the Cheonan Well-being Food Expo (천안 웰빙식품엑스포)",
    "천안 웰빙식품엑스포 · 전통식품 · 유기농 건강식품 · 전시관 · 체험관 · 친환경",
    requires=[],
    cards=[
        card("Follow-up 1a (Reading): an announcement about an expo",
             "Read the announcement and, in English, identify the type of expo and three specific booths mentioned. The text is the book’s (9월 11일부터 20일까지 is spelled out; the book’s three booths are in parentheses in its sentence and are set apart here). The English is mine.",
             examples=passage(_EXPO)),
        card("Follow-up 1b (Reading): descriptions of the booths",
             "The book gives three booth descriptions and asks you to write the name of each booth in Korean and what it displays or presents in English. The book glosses 친환경: environmentally friendly, eco-friendly, “pro-environment”. The descriptions, in the book’s order (booth 1 is the first two sentences; the English is mine):",
             examples=passage(_BOOTH)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Item", "Answer (mine)"], [["Type of expo", "A well-being food expo: traditional food and organic health food"], ["Three booths", "웰빙 친환경 식품전시관; 웰빙 식품체험관; 웰빙 건강체험관"], ["Booth 1 (채식이나 소식 …)", "웰빙 건강체험관: longevity eating habits and nutrition information; health diagnosis and a recommended healthy diet"], ["Booth 2 (웰빙식품을 직접 보고 만들 수 있도록 …)", "웰빙 식품체험관: hands-on well-being cooking classes such as making tofu and cheese"], ["Booth 3 (패스트푸드나 인스턴트 식품의 …)", "웰빙 친환경 식품전시관: the problems of fast food and instant food, and unpolluted organic eco-friendly health food"]])]),
    ],
    exercises=uniq(
        _tr(_EXPO + _BOOTH, k=3)
        + [M("What kind of expo is the 천안 웰빙식품엑스포?", "A well-being food expo", ["A car expo", "A computer expo", "A book expo"], "웰빙식품엑스포."), M("What does the expo display?", "Traditional foods and organic health foods", ["Cars", "Clothes", "Books"], "전통식품과 웰빙 유기농 건강식품."), M("Where is the expo held?", "Cheonan Samgeori Park", ["Seoul Station", "A school", "The airport"], "천안 삼거리공원."), M("Which booth runs cooking classes such as tofu making?", "웰빙 식품체험관", ["웰빙 건강체험관", "웰빙 친환경 식품전시관", "None"], "전통 두부 만들기, 치즈 만들기."), M("Which booth diagnoses health condition and recommends a diet?", "웰빙 건강체험관", ["웰빙 식품체험관", "웰빙 친환경 식품전시관", "None"], "건강상태를 진단해 주고."), M("Which booth shows the problems of fast food?", "웰빙 친환경 식품전시관", ["웰빙 건강체험관", "웰빙 식품체험관", "None"], "패스트푸드나 인스턴트 식품의 문제점."),
           F("천안 웰빙식품___가 열립니다. (expo)", "엑스포", ["프로그램", "마스크"], "엑스포."), F("우리 ___식품과 웰빙 유기농 건강식품을 전시합니다. (traditional)", "전통", ["인스턴트", "오염"], "전통."), F("직접 ___할 수 있는 여러 전시관을 운영합니다. (experience)", "체험", ["진단", "섭취"], "체험."), F("관심 있으신 분들의 많은 ___ 부탁드립니다. (participation)", "참여", ["문의", "마련"], "참여."), F("오염되지 않은 ___ 친환경 건강식품을 전시합니다. (organic)", "유기농", ["인스턴트", "전문가"], "유기농."),
           read_q("천안 웰빙식품엑스포"), read_q("웰빙 친환경 식품전시관"), read_q("웰빙 식품체험관"), read_q("웰빙 건강체험관"), read_q("관심 있으신 분들의 많은 참여 부탁드립니다")]
    ),
)

# ================================================================== L11: Grammar C: -(으)ㄹ 만하다
_MAN1 = [("그 영화는 볼 만해요.", "That movie is worth watching."), ("몬트레이 수족관은 구경할 만해요.", "The Monterey Bay Aquarium is worth touring."), ("그 한국식당 김치는 먹어볼 만해요.", "The Korean restaurant’s kimchi is worth trying (eating).")]
_MAN2 = [("프랭크는 대통령이 될 만한 사람이에요.", "Frank is qualified to be the president."), ("제인은 상을 받을 만한 학생입니다.", "Jane is a student who is qualified to receive an award. / Jane is a student who deserves to receive an award.")]
_MANV = [("보다", "to watch", "볼 만해요"), ("구경하다", "to tour; to sightsee", "구경할 만해요"), ("먹어 보다", "to try eating", "먹어 볼 만해요"), ("가 보다", "to try going", "가 볼 만해요"), ("읽다", "to read", "읽을 만해요"), ("듣다", "to listen", "들을 만해요"), ("배우다", "to learn", "배울 만해요"), ("되다", "to become", "될 만한 사람"), ("받다", "to receive", "받을 만한 학생")]
_MAN3 = [("몬트레이 수족관이 구경할 만해요.", "The Monterey Bay Aquarium is worth touring."), ("포인트 로보스는 가 볼 만해요.", "Point Lobos is worth going to.")]
L11 = lesson(
    "Ch 32 · Grammar C: –(으)ㄹ 만하다, to be worth ~ing; to deserve",
    "-(으)ㄹ 만하다 · 볼 만해요 · 구경할 만해요 · 먹어볼 만해요 · 될 만한 사람",
    requires=[],
    cards=[
        card("–(으)ㄹ 만하다: worth doing",
             "The grammar feature –(으)ㄹ 만하다, when attached to the stem of an action verb, literally means “to be worth doing”. This expression is used to indicate that a certain action is worth doing. (The English is the book’s.)",
             examples=passage(_MAN1)),
        card("–(으)ㄹ 만하다: qualified; deserving",
             "–(으)ㄹ 만하다 can also be used when someone deserves something (position, award, result, consequence, etc.). In these instances, –(으)ㄹ 만하다 can be translated as “to be qualified to be something” or “to deserve to do something”. (The English is the book’s.)",
             examples=passage(_MAN2)),
        card("Forms (mine)", "Action verb stem + (으)ㄹ 만하다: the future attributive –(으)ㄹ plus 만하다 (만해요 in the polite style; 만한 before a noun). ㄹ-verbs keep the ㄹ (살 만한); ㄷ-irregular verbs change ㄷ to ㄹ (들을).",
             tables=[table(["Verb", "Meaning", "-(으)ㄹ 만하다"], [list(r) for r in _MANV], say=[0, 2])]),
        card("Follow-up 1 (Speaking): things worth doing in the Monterey area",
             "Think about places, activities and restaurants in the Monterey area, fill in a table (places worth seeing; things worth doing; restaurants worth eating at) and tell your partner using –(으)ㄹ 만하다. The book’s model (the English is mine):",
             examples=dlg([("A", _MAN3[0][0], _MAN3[0][1]), ("B", _MAN3[1][0], _MAN3[1][1])])),
        card("Activities left out", "Follow-up 2 (listening to four narrations and writing what was worth doing) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_MAN1 + _MAN2 + _MAN3, k=3)
        + [M("What does –(으)ㄹ 만하다 literally mean when attached to an action verb?", "“to be worth doing”", ["“to want to do”", "“to be able to do”", "“to have done”"], "The book’s note."), M("What else can –(으)ㄹ 만하다 mean?", "To be qualified to be / to deserve to do", ["To be unable to do", "To try doing", "To stop doing"], "The book’s note."), M("What does 그 영화는 볼 만해요 mean?", "That movie is worth watching", ["I want to watch that movie", "I watched that movie", "That movie is long"], "볼 만하다."), M("What does 제인은 상을 받을 만한 학생입니다 mean?", "Jane is a student who deserves to receive an award", ["Jane received a prize", "Jane wants a prize", "Jane is giving a prize"], "받을 만한."), M("What does 프랭크는 대통령이 될 만한 사람이에요 mean?", "Frank is qualified to be the president", ["Frank is the president", "Frank wants to be president", "Frank was the president"], "될 만한."),
           F("그 영화는 ___ 만해요. (watch)", "볼", ["본", "보는"], "보다 → 볼."), F("몬트레이 수족관은 구경___ 만해요. (tour)", "할", ["한", "하는"], "구경하다 → 구경할."), F("그 한국식당 김치는 먹어___ 만해요. (try eating)", "볼", ["본", "보는"], "먹어 보다 → 먹어 볼."), F("프랭크는 대통령이 ___ 만한 사람이에요. (become)", "될", ["된", "되는"], "되다 → 될."), F("제인은 상을 ___ 만한 학생입니다. (receive)", "받을", ["받은", "받는"], "받다 → 받을."),
           read_q("그 영화는 볼 만해요"), read_q("몬트레이 수족관은 구경할 만해요"), read_q("그 한국식당 김치는 먹어볼 만해요"), read_q("프랭크는 대통령이 될 만한 사람이에요"), read_q("포인트 로보스는 가 볼 만해요")]
    ),
)

# ================================================================== L12: Grammar D: -는 데(에)
_DE1 = [("여기가 내가 공부하는 데예요.", "This is (the place) where I study."), ("아직 묵을 데를 못 찾았어요.", "I haven’t yet found a place to stay.")]
_DE2 = [("스트레스를 해소하는 데에 무슨 운동이 좋습니까?", "For relieving stress, what sports are good?"), ("한국에서 자동차를 빌리는 데에 국제면허증이 필요합니다.", "For renting a car in Korea, an international driver’s license is needed.")]
_DE3 = [("차 바퀴를 바꾸는 데에 얼마예요?", "How much is it for replacing tires?"), ("요세미티까지 자동차로 가는 데에 얼마나 걸려요?", "[As for] going to Yosemite by car, how long does [it] take?"), ("인터넷으로 비행기표를 사는 데에 신용카드가 필요해요.", "A credit card is needed for buying a plane ticket online."), ("비만을 예방하는 데에는 야채와 생선이 좋습니다.", "Vegetables and fish are good for preventing obesity.")]
_DE4 = [("해외 여행하는 데에 무엇이 필요합니까?", "What is needed for traveling abroad?"), ("해외 여행하는 데에는 여권이 필요합니다.", "A passport is needed for traveling abroad.")]
_DE5 = [("장거리 여행을 하는 데 뭐가 필요해요?", "What is needed for taking a long trip?"), ("장거리 여행을 하는 데는 지도와 돈, 옷이 필요해요.", "A map, money and clothes are needed for taking a long trip."), ("캠핑을 하는 데 뭐가 필요해요?", "What is needed for camping?")]
_DEV = [("공부하다", "to study", "공부하는 데"), ("묵다", "to stay (overnight)", "묵는 데"), ("해소하다", "to relieve", "해소하는 데"), ("빌리다", "to rent; to borrow", "빌리는 데"), ("바꾸다", "to change", "바꾸는 데"), ("가다", "to go", "가는 데"), ("사다", "to buy", "사는 데"), ("예방하다", "to prevent", "예방하는 데"), ("만들다", "to make", "만드는 데"), ("읽다", "to read", "읽는 데")]
L12 = lesson(
    "Ch 32 · Grammar D: the conjunctive ending –는 데(에), for / in / at doing something",
    "-는 데(에) · 공부하는 데 · 묵을 데 · 해소하는 데 · 빌리는 데 · 예방하는 데에는",
    requires=[],
    cards=[
        card("The dependent noun 데 (a place, a spot)",
             "Recall that the noun 데 (a place, a spot) is a dependent noun. This means it must be accompanied by a modifier: 먹을 데 (a place to eat) or 아픈 데 (a sore spot). Thus, the literal meaning of –는 데(에) is “(at) a place for doing something” or “(at) a spot for doing something”. (The English is the book’s.)",
             examples=passage(_DE1)),
        card("–는 데(에) as a conjunctive ending",
             "However, when –는 데(에) functions as a conjunctive ending, it is used to bring up a topic of doing something in order to seek or provide specific information about the topic. For this reason, the conjunctive ending –는 데(에) can be translated as “for”, “as for”, or “speaking of”. (The English is the book’s.)",
             examples=passage(_DE2)),
        card("Seeking or providing information",
             "The first sentence is an interrogative sentence, so the speaker brings up the topic of relieving stress in order to seek specific information about it. The second sentence is a statement, so the speaker brings up the topic of renting a car in Korea in order to provide specific information about it.\n\n"
             "Expressing a topic of doing something to seek/provide specific information: verb stem + 는 데(에). The book’s examples (the English is the book’s):",
             examples=passage(_DE3)),
        card("Forms (mine)", "Verb stem + 는 데 (an ㄹ-final stem drops the ㄹ: 만들다 → 만드는 데); 에 can be dropped or followed by the topic particle 는 (-는 데에는).",
             tables=[table(["Verb", "Meaning", "-는 데"], [list(r) for r in _DEV], say=[0, 2])]),
        card("Follow-up 3 (Speaking): the model",
             "Sitting in a circle, each student thinks of a topic, writes a Korean question with –는 데(에) and asks the class; classmates answer in Korean. The book’s model (the English is mine):",
             examples=dlg([("A", _DE4[0][0], _DE4[0][1]), ("B", _DE4[1][0], _DE4[1][1])])),
        card("Follow-up 5 (Speaking): things needed for a long trip and camping",
             "You and your partner list three things necessary for each of two categories (장거리 여행을 하는 데; 캠핑을 하는 데), ask each other and report to the class. The book’s model (the English is mine):",
             examples=dlg([("A", _DE5[0][0], _DE5[0][1]), ("B", _DE5[1][0], _DE5[1][1])])),
        card("Activities left out", "Follow-up 4 (listening to five sentences and translating them) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_DE1 + _DE2 + _DE3 + _DE4 + _DE5[:2], k=3)
        + [M("How is the conjunctive ending –는 데(에) translated?", "“for”, “as for” or “speaking of”", ["“because”", "“if”", "“although”"], "The book’s note."), M("What is –는 데(에) used for?", "Bringing up a topic of doing something to seek or provide specific information", ["Giving a command", "Expressing a wish", "Saying a past event"], "The book’s note."), M("What is the literal meaning of –는 데(에)?", "“(at) a place for doing something”", ["“because of doing”", "“after doing”", "“if doing”"], "데 = a place."), M("What kind of noun is 데?", "A dependent noun (it needs a modifier)", ["A proper noun", "A pronoun", "A verb"], "The book’s note."), M("Does 한국에서 자동차를 빌리는 데에 국제면허증이 필요합니다 seek or provide information?", "Provide", ["Seek", "Neither", "Both"], "A statement."), M("Does 스트레스를 해소하는 데에 무슨 운동이 좋습니까 seek or provide information?", "Seek", ["Provide", "Neither", "Both"], "A question."),
           F("스트레스를 해소하___ 데에 무슨 운동이 좋습니까? (-는)", "는", ["은", "을"], "-는 데."), F("한국에서 자동차를 빌리___ 데에 국제면허증이 필요합니다. (-는)", "는", ["은", "을"], "-는 데."), F("인터넷으로 비행기표를 사___ 데에 신용카드가 필요해요. (-는)", "는", ["은", "을"], "-는 데."), F("비만을 예방하는 데에___ 야채와 생선이 좋습니다. (topic particle)", "는", ["도", "가"], "-는 데에는."), F("요세미티까지 자동차로 가는 ___ 얼마나 걸려요? (-데에)", "데에", ["때에", "곳에"], "-는 데에."),
           read_q("여기가 내가 공부하는 데예요"), read_q("아직 묵을 데를 못 찾았어요"), read_q("스트레스를 해소하는 데에 무슨 운동이 좋습니까"), read_q("비만을 예방하는 데에는 야채와 생선이 좋습니다"), read_q("해외 여행하는 데에는 여권이 필요합니다")]
    ),
)

# ================================================================== L13: Activity 3: health report on two well-being seekers
_HR = [("최근 웰빙족들이 점점 더 늘고 있는데요.", "Recently, well-being seekers are increasing more and more."), ("오늘은 특히 웰빙 라이프스타일로 병을 치료한 두 명의 웰빙족을 만나보겠습니다.", "Today we will meet two well-being seekers who in particular treated their illnesses with a well-being lifestyle."), ("김순정 씨는 갑자기 체중이 줄고 소변을 자주 보는 증상이 계속되어 병원을 찾아갔습니다.", "Ms. Kim Sunjeong visited a hospital because her symptoms of sudden weight loss and frequent urination continued."), ("거기에서 당뇨병 진단을 받고 당뇨병을 고치기 위해 잡곡밥과 야채 등 건강 관리사가 추천하는 웰빙 식단을 삼 년째 따르고 있습니다.", "There she was diagnosed with diabetes and, in order to cure diabetes, has been following the well-being diet recommended by a health counselor, with mixed-grain rice and vegetables, for three years."), ("또한 영양소를 균형 있게 섭취하고 있으며 유기농 식품으로만 요리하고 있습니다.", "She also takes in nutrients in a balanced way and cooks only with organic food."), ("박형철 씨는 계속 피로하고 또 소화가 안 돼서 소화제를 육 개월간 복용하다가 병원에 갔습니다.", "Mr. Park Hyeongcheol went to a hospital after taking digestive medicine for six months because he was constantly tired and also could not digest."), ("진찰을 받았는데 병명은 위암이었습니다.", "He had an examination and the name of the illness was stomach cancer."), ("위암 수술을 받은 후 박형철 씨는 제일 먼저 술과 담배에서 벗어나기 위해 노력하고 있습니다.", "After undergoing stomach cancer surgery, Mr. Park is first of all trying to get away from alcohol and cigarettes."), ("일찍 자고 일찍 일어나는 습관도 키워가고 있습니다.", "He is also building the habit of going to bed early and getting up early."), ("또한, 가벼운 산책 등 스트레스를 해소하는 데 도움이 되는 야외 활동에 참여하고 있습니다.", "Also, he takes part in outdoor activities, such as light walks, that help relieve stress.")]
_HEALTH = [("당뇨병", "diabetes"), ("만성피로", "chronic fatigue"), ("불면증", "insomnia"), ("비만", "obesity"), ("식중독", "food poisoning"), ("심장질환", "heart disease"), ("암", "cancer"), ("우울증", "depression"), ("호흡기질환", "respiratory disease")]
L13 = lesson(
    "Ch 32 · Activity 3: a health report on two well-being seekers (웰빙족)",
    "웰빙족 · 당뇨병 진단 · 위암 · 웰빙 식단 · 술과 담배에서 벗어나다 · 야외 활동",
    requires=[],
    cards=[
        card("Activity 3 (Reading): a health report on two patients",
             "The following excerpt is from a health report describing what two patients are doing to overcome their health problems. The book asks you to fill in a table in English (illness and symptoms; recommended lifestyle changes). The book glosses 웰빙족: well-being seekers, “well-being tribe”. The first patient is 김순정 (여, 52), a woman of fifty-two, and the second is 박형철 (남, 65), a man of sixty-five (the ages are in the book’s parentheses and are left out of the spoken text); 3년째 and 6개월간 are spelled out. The English is mine.",
             examples=passage(_HR)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Patient", "Illness and symptoms", "Recommended lifestyle changes"], [["김순정 (woman, 52)", "Diabetes; sudden weight loss and frequent urination", "Has followed the well-being diet recommended by a health counselor (mixed-grain rice, vegetables) for three years; takes in nutrients in a balanced way; cooks only with organic food"], ["박형철 (man, 65)", "Stomach cancer; constant fatigue and indigestion (took digestive medicine for six months)", "After surgery, is trying to quit alcohol and cigarettes; building the habit of going to bed and getting up early; takes part in outdoor activities such as light walks to relieve stress"]])]),
        card("Activity 4 (Writing and speaking): 건강하게 삽시다! (Let’s live healthily!)",
             "The book asks you to review the diseases, symptoms, treatments and healthy lifestyles from Unit 8 and present two of them with your own tips. The illnesses to choose from are:",
             tables=[ktable(_HEALTH)]),
        card("Activities left out", "Activity 1 (SMART Board), Activity 2 (listening to two YTN news segments about the well-being boom: well-being food, kitchenware or dance) and the pairs, flip-chart and presentation steps of Activity 4 need audio, a SMART Board and classmates."),
    ],
    exercises=uniq(
        _tr(_HR[2:], k=3)
        + vocab_exercises(_HEALTH)
        + [M("What symptoms did 김순정 have?", "Sudden weight loss and frequent urination", ["A cough", "A fever", "A headache"], "갑자기 체중이 줄고 소변을 자주."), M("What was 김순정 diagnosed with?", "Diabetes", ["Cancer", "Obesity", "Insomnia"], "당뇨병 진단."), M("What does 김순정 eat now?", "Mixed-grain rice and vegetables, from organic food", ["Fast food", "Only meat", "Only noodles"], "잡곡밥과 야채."), M("How long has she followed the diet?", "Three years", ["Three months", "Ten years", "One week"], "삼 년째."), M("What symptoms did 박형철 have?", "Constant fatigue and indigestion", ["Itching", "Fever", "A rash"], "계속 피로하고 소화가 안 돼서."), M("What was 박형철’s illness?", "Stomach cancer", ["Diabetes", "Flu", "Depression"], "위암."), M("What is 박형철 trying to get away from?", "Alcohol and cigarettes", ["Work", "Meat", "Sleep"], "술과 담배에서 벗어나기 위해."), M("What habit is 박형철 building?", "Going to bed early and getting up early", ["Eating late", "Working late", "Sleeping late"], "일찍 자고 일찍 일어나는 습관."),
           F("김순정 씨는 ___ 체중이 줄고 소변을 자주 보는 증상이 계속되었습니다. (suddenly)", "갑자기", ["골고루", "거의"], "갑자기."), F("당뇨병 ___을 받고 웰빙 식단을 따르고 있습니다. (diagnosis)", "진단", ["문의", "참여"], "진단."), F("박형철 씨는 소화___를 육 개월간 복용했습니다. (digestive medicine)", "제", ["양", "병"], "소화제."), F("스트레스를 해소하는 데 도움이 되는 ___ 활동에 참여합니다. (outdoor)", "야외", ["실내", "개인"], "야외."), F("최근 ___들이 점점 더 늘고 있습니다. (well-being seekers)", "웰빙족", ["노인", "환자"], "웰빙족."),
           read_q("최근 웰빙족들이 점점 더 늘고 있는데요"), read_q("당뇨병 진단을 받았습니다"), read_q("위암 수술을 받은 후 술과 담배에서 벗어나기 위해 노력하고 있습니다"), read_q("일찍 자고 일찍 일어나는 습관도 키워가고 있습니다"), read_q("건강하게 삽시다")]
    ),
)

# ================================================================== L14: core vocabulary and self-evaluation
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Loan words", _CV_LOAN), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0]]
    ns = [r for r in rows if not (_HG(r[0]) and "-" not in r[0] and "~" not in r[0])]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L14 = lesson(
    "Ch 32 · Core vocabulary and self-evaluation",
    "주요 단어 · 건강한 생활 · 장수 · 편식 · 웰빙 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section and the end-of-book Glossary are blank or alphabetical lists of words already given.\n\n"
             "The example sentences with digits are respelled in Hangul (80세 → 팔십 세; 200칼로리 → 이백 칼로리; YMCA → 와이엠시에이; the phone number in 문의 is spelled out and its hyphens read 에; 단백질(protein) is just 단백질)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify healthy eating and lifestyle habits; discuss living a healthy, long life; and give and receive advice about health and nutrition.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the causative construction –게 하다; the informal ending –거든(요); –(으)ㄹ 만하다 (be worth ~ing); the conjunctive ending –는 데(에); and the Sino-Korean syllables within 노인 (老人), 편식 (偏食), and 직접 (直接)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 장수 mean?", "longevity; “long life”", ["a ratio", "a habit", "a secret"], "長壽."), M("What does 비결 mean?", "a secret; a key; a knack", ["a ratio", "an attitude", "a nutrient"], "秘訣."), M("What does 영양소 mean?", "a nutrient", ["a calorie", "body fat", "a snack"], "營養素."), M("What does 간식 mean?", "snacks; “between meals”", ["a menu", "fast food", "candy"], "間食."), M("What does 웰빙 mean?", "well-being", ["leisure", "organic", "a program"], "Loan word."), M("What does 유기농 mean?", "organic (farming)", ["outdoors", "polluted", "a specialist"], "有機農."), M("What does 직접 mean?", "directly; firsthand", ["indirectly", "almost", "evenly"], "直接."),
           F("한국말을 잘 하는 ___이 무엇입니까? (secret)", "비결", ["태도", "비율"], "비결."), F("어머님 아버님, 건강하시고 ___하세요. (live long)", "장수", ["소식", "채식"], "장수하다."), F("건강을 위해서는 음식을 ___ 먹어야 합니다. (evenly)", "골고루", ["거의", "적어도"], "골고루."), F("여러 음식에서 다양한 ___를 섭취하는 것이 좋습니다. (nutrients)", "영양소", ["지방", "과자"], "영양소."), F("요즘 한국에서는 ___ 문화가 유행입니다. (well-being)", "웰빙", ["오염", "여가"], "웰빙."),
           read_q("주요 단어"), read_q("건강한 생활"), read_q("장수의 비결"), read_q("영양소"), read_q("웰빙")]
    ),
)

UNIT = unit("Semester 2 · Unit 8 · Chapter 32: Living a Healthy Life (건강한 생활)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14])

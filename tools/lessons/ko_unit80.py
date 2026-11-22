"""Unit 80: KBC Semester III, Unit 17, Lesson 5 - Modern Diseases I (현대병 I).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 17, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_MATCH5 = [("호흡기", "respiratory organs", "황사 때문에 호흡기 질환이 생겼다"), ("심장", "heart", "운동을 하면 심장이 튼튼해진다"), ("간", "liver", "음주는 간에 좋지 않다"), ("위", "stomach", "짠 음식은 위에 부담이 된다"), ("대장", "colon", "야채를 먹으면 대장이 건강해진다"), ("폐", "lung", "폐가 안 좋아서 숨 쉬기가 힘들다"), ("뼈", "bones", "칼슘이 부족하면 뼈가 약해진다")]
_HJ5 = [("過 과", "pass; excessive; over", "과로, 과거"), ("病 병", "illness; disease", "병명, 질병"), ("食 식", "food", "식중독, 편식"), ("感 감", "feeling", "감정, 감염"), ("科 과", "subject; department", "내과, 과목")]
_HJW5 = [("과로", "overwork; “excessive labor”"), ("과거", "the past"), ("병명", "a disease name"), ("질병", "a disease; a sickness"), ("식중독", "food poisoning"), ("편식", "an unbalanced diet"), ("감정", "feeling; emotion"), ("감염", "infection"), ("내과", "(department of) internal medicine"), ("과목", "a subject")]
_SIM5 = [("질병", "질환", "disease: ailment"), ("폭식", "과식", "binge eating: overeating"), ("감염", "전염", "infection: contagion"), ("식욕", "입맛", "appetite: taste for food")]
_REL5 = [("A", "식습관", "편식, 채식, 과식", "eating habits"), ("B", "성인병", "동맥경화, 비만, 당뇨", "adult diseases"), ("C", "감기", "콧물, 재채기, 기침", "a cold"), ("D", "병원", "소아과, 피부과, 안과", "a hospital")]
_L5X = [("발병", "onset of a disease"), ("질환", "an ailment"), ("병원", "a hospital"), ("몸살", "aches from fatigue or a cold"), ("스트레스", "stress"), ("전염", "contagion"), ("채식", "a vegetarian diet"), ("육식", "a meat diet"), ("과식", "overeating"), ("폭식", "binge eating"), ("식욕", "appetite"), ("입맛", "taste for food; appetite"), ("식전", "before a meal"), ("감각", "a sense"), ("동맥경화", "arteriosclerosis"), ("비만", "obesity"), ("당뇨", "diabetes"), ("콧물", "a runny nose"), ("재채기", "a sneeze"), ("기침", "a cough"), ("성인병", "an adult disease"), ("식습관", "eating habits"), ("소아과", "pediatrics"), ("내과", "internal medicine"), ("산부인과", "obstetrics and gynecology"), ("피부과", "dermatology"), ("외과", "surgery"), ("이비인후과", "ear, nose and throat clinic"), ("치과", "dentistry"), ("정신과", "psychiatry"), ("안과", "ophthalmology"), ("황사", "yellow dust"), ("칼슘", "calcium")]
L1 = lesson(
    "U17 L5 · Review: body organs, diseases and Sino-Korean 過 病 食 感 科",
    "현대병 I · 단어 복습 · 한자어 복습 · 호흡기 · 심장 · 간 · 위 · 대장 · 폐 · 뼈 · 過 病 食 感 科",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives seven sentences with one word underlined and asks you to connect each underlined word with its English meaning on the right. The underline is not marked in the text; the pairs are:", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH5], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ5], say=[2]), ktable(_HJW5)]),
        card("한자어 복습 1: the most similar word (my answers)", "Circle the word with the most similar meaning to the word on the left (A. 질병: 과로, 발병, 질환, 병원; B. 폭식: 채식, 육식, 과식, 편식; C. 감염: 몸살, 전염, 질병, 스트레스; D. 식욕: 입맛, 식전, 감각, 식중독).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM5], say=[0, 1])]),
        card("한자어 복습 2: the related word (my answers)", "Choose from the box (감기, 병원, 성인병, 감정, 식습관) the word related to the three words on the right; 감정 is left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Meaning"], [list(r) for r in _REL5], say=[1, 2])]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001 to 007): seven audio clips for which you decide which hospital department to go to (the box: 소아과, 내과, 산부인과, 피부과, 외과, 이비인후과, 치과, 정신과, 안과). The department words are in the next card."),
        card("More words from these exercises", "", tables=[ktable(_L5X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH5], k=3) + _tr(_HJW5, k=3) + _tr(_L5X, k=3) + _tr([(a, c) for a, b, c in _SIM5], k=3)
        + [M("What does the syllable 過 (과) mean?", "pass; excessive; over", ["illness", "food", "feeling"], "과로."), M("What does the syllable 病 (병) mean?", "illness; disease", ["excessive", "food", "feeling"], "질병."), M("What does the syllable 食 (식) mean?", "food", ["illness", "excessive", "feeling"], "편식."), M("What does the syllable 感 (감) mean?", "feeling", ["illness", "food", "subject"], "감염."), M("What does the syllable 科 (과) mean?", "subject; department", ["illness", "food", "feeling"], "내과.")
           , M("Which word is similar to 질병?", "질환", ["과로", "발병", "병원"], "Ailment."), M("Which word is similar to 폭식?", "과식", ["채식", "육식", "편식"], "Overeating."), M("Which word is similar to 감염?", "전염", ["몸살", "질병", "스트레스"], "Contagion."), M("Which word holds 편식, 채식, 과식?", "식습관", ["성인병", "감기", "병원"], "Eating habits."), M("Which word holds 동맥경화, 비만, 당뇨?", "성인병", ["식습관", "감기", "병원"], "Adult diseases."), M("Which word holds 콧물, 재채기, 기침?", "감기", ["성인병", "식습관", "병원"], "A cold.")
           , F("운동을 하면 ___이 튼튼해진다. (heart)", "심장", ["대장", "폐"], "심장."), F("음주는 ___에 좋지 않다. (liver)", "간", ["위", "뼈"], "간."), F("칼슘이 부족하면 ___가 약해진다. (bones)", "뼈", ["간", "폐"], "뼈."), F("___가 안 좋아서 숨 쉬기가 힘들다. (lung)", "폐", ["위", "간"], "폐."), F("야채를 먹으면 ___이 건강해진다. (colon)", "대장", ["심장", "뼈"], "대장.")]
        + [read_q("황사 때문에 호흡기 질환이 생겼습니다"), read_q("음주는 간에 좋지 않습니다"), read_q("칼슘이 부족하면 뼈가 약해집니다"), read_q("야채를 먹으면 대장이 건강해집니다")]
    ),
)

# ================================================================== L2 Part 1
_EVT5 = [
    ("서울아산병원은 오는 십구 일 세계 수면의 날을 맞아 십팔 일 오후 두 시 병원 동관 육 층 대강당에서 건강한 잠, 불면증과 수면장애라는 주제로 무료 건강강좌를 개최한다.", "Event 1. On the 18th at 2 p.m., to mark World Sleep Day on the 19th, Seoul Asan Hospital holds a free health lecture on the theme “Healthy sleep: insomnia and sleep disorders” in the main lecture hall on the 6th floor of the hospital’s east wing."),
    ("호흡기내과, 신경과, 치과, 이비인후과, 정신과 교수 등이 수면장애의 증상과 진단법, 치료법 등을 알려 준다.", "Professors from respiratory medicine, neurology, dentistry, ear-nose-throat and psychiatry explain the symptoms, diagnosis and treatment of sleep disorders. (The book names each professor; I leave the names and the telephone number out.)"),
    ("사단법인 한국고혈압관리협회는 세계 고혈압의 날 오 월 십칠 일을 앞두고 십사 일 서울 광진구 동서울터미널 앞 광장에서 고혈압 예방 캠페인을 벌인다.", "Event 2. The incorporated Korean Hypertension Management Association holds a hypertension prevention campaign on the 14th in the plaza in front of the Dong-Seoul Terminal in Gwangjin District, Seoul, ahead of World Hypertension Day (May 17)."),
    ("전문의가 진행하는 혈압 측정 및 고혈압 건강상담, 고혈압 예방 책자 배포, 연령대별 신체나이 측정 등이 있을 예정이다.", "Blood-pressure measurement and hypertension health counseling run by specialists, distribution of hypertension prevention booklets, and body-age measurement by age group are planned."),
    ("삼성서울병원 암센터는 십이 일 암센터 지하 일 층 강당에서 암환자를 대상으로 아주 특별한 암환자의 날 행사를 개최한다.", "Event 3. Samsung Medical Center’s Cancer Center holds a very special “Cancer Patients’ Day” event for cancer patients on the 12th in the auditorium on the first basement floor of the center."),
    ("치료, 교육, 연구의 세 박자를 고루 갖춘 세계적 수준의 삼성암센터에서 기존 암질환에 대한 이론강좌 위주에서 탈피, 암환자를 위한 스트레스 해소법, 요가, 발마사지 등 직접 참가하는 이벤트를 다채롭게 마련해 큰 관심을 끌고 있다.", "At the world-class center, which has treatment, education and research in good balance, it has drawn great interest by breaking away from the existing focus on theory lectures about cancer and arranging varied events people take part in directly, such as stress-relief methods, yoga and foot massage for cancer patients."),
    ("또 암센터 일 층 로비에서는 암환자를 위한 영양 상담 및 영양식 전시회를 개최한다.", "Also, in the lobby on the first floor of the center, a nutrition consultation and an exhibition of nutritional foods for cancer patients will be held."),
]
_SPEAK5A = [("미국인들이 흔히 걸리는 성인병이 무엇인지 생각해 보고 그 병의 원인과 예방법 등에 대해서 이야기해 보세요.", "Think about which adult diseases Americans commonly get, and talk about the causes, ways of prevention and so on.")]
L2 = lesson(
    "U17 L5 · Part 1 (도입 학습): three health event notices and a speaking prompt",
    "도입 학습 · 불면증 · 수면장애 · 고혈압 · 암환자 · 건강강좌 · 캠페인 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: three health event announcements (Kyunghyang)", "The three notices with my English; the book asks you to fill in a table of events, host and location, and event details. The names of the professors, the association’s president and the center’s head and the telephone numbers in the book are left out. Answers (the table): 1. Sleep lecture: Seoul Asan Hospital, east wing 6th-floor lecture hall; free health lecture “Healthy sleep” on insomnia and sleep disorders, on the 18th at 2 p.m., ahead of World Sleep Day; professors explain symptoms, diagnosis and treatment. 2. Hypertension prevention campaign: Korean Hypertension Management Association, plaza in front of Dong-Seoul Terminal, Gwangjin District; blood-pressure measurement and counseling by specialists, booklets, body-age measurement; on the 14th, ahead of World Hypertension Day. 3. Cancer Patients’ Day: Samsung Medical Center Cancer Center, first-basement auditorium (and a first-floor lobby nutrition exhibition); on the 12th; stress relief, yoga, foot massage and other hands-on events, plus nutrition counseling and a nutritional-food exhibition.", examples=passage(_EVT5)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK5A)),
        card("Activities left out", "학습활동 1 (Reading): a diagram (edunet4u.net) of the correlations among adult diseases, with five English sentences to complete (arteriosclerosis is caused by __ or __; cancer and gallstones are caused by __; diabetes can directly cause __, __ and __; arteriosclerosis and high blood pressure can cause __; __ can be the root cause of many adult diseases). The diagram is a picture. 학습활동 3 (Listening, track 008): a YTN news item on the Chungcheongbuk-do Office of Education; you say what two actions it decided on and why. 학습활동 4 (Listening, tracks 009 and 010): a YTN news item about a health event in Daejeon; you say what the event is about, what the best of the top 10 healthy foods is, and fill a table of food colors and their health benefits (red foods lower cholesterol; yellow foods give antioxidants, anti-cancer and anti-ulcer effects). They are audio or a picture."),
    ],
    exercises=uniq(
        _tr(_EVT5, k=3)
        + [M("What is the theme of the Seoul Asan Hospital lecture?", "Healthy sleep: insomnia and sleep disorders", ["Heart surgery", "Hypertension", "Nutrition for cancer patients"], "건강한 잠."), M("Where is the hypertension prevention campaign held?", "In the plaza in front of the Dong-Seoul Terminal", ["At a hospital lecture hall", "At a school", "In a park"], "광장."), M("What does the Cancer Center’s event offer?", "Hands-on events such as stress relief, yoga and foot massage", ["Only theory lectures", "Free surgery", "Sports games"], "직접 참가."), M("Which day is World Hypertension Day?", "May 17", ["March 19", "June 12", "May 14"], "오 월 십칠 일."), M("What is offered in the Cancer Center lobby?", "Nutrition counseling and an exhibition of nutritional foods", ["Blood-pressure measurement", "A sleep clinic", "A yoga class"], "영양 상담.")]
        + [F("서울아산병원은 무료 건강강좌를 ___한다. (to hold)", "개최", ["탈피", "검토"], "개최하다."), F("고혈압 예방 ___을 벌인다. (campaign)", "캠페인", ["강좌", "책자"], "캠페인."), F("고혈압 예방 ___를 배포한다. (booklet)", "책자", ["강당", "협회"], "책자.")]
        + [read_q("무료 건강강좌를 개최합니다"), read_q("고혈압 예방 캠페인을 벌입니다"), read_q("혈압 측정 및 고혈압 건강상담이 있습니다"), read_q("미국인들이 흔히 걸리는 성인병이 무엇인지 생각해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("고혈압", "(高血壓) high blood pressure; hypertension", "", "저혈압"),
        ("담석증", "(膽石症) illness caused by gallstones; cholelithiasis", ""),
        ("심근경색", "(心筋梗塞) myocardial infarction", ""),
        ("전립선", "(前立腺) the prostate (gland)", ""),
    ]),
    ("학습활동 2", [
        ("강당", "(講堂) an auditorium; a lecture hall", "졸업식이 강당에서 열립니다.", "대강당, 소강당"),
        ("개최(하다/되다)", "(開催) holding (to hold [a meeting, an exhibition, a sporting event, etc.]/to be held)", "올해 지 이십 회담은 서울에서 개최됩니다.", "열다"),
        ("기존(의)", "(旣存) existing", "기존에 있는 시설을 이용하면 준비 비용이 적게 들 것이다."),
        ("신체나이", "(身體) body age", "운동을 꾸준히 하는 사람은 안 하는 사람에 비해 신체나이가 더 젊다.", "정신연령"),
        ("이론", "(理論) a theory", "이론과 실제가 항상 일치하는 것은 아닙니다."),
        ("전문의", "(專門醫) a medical specialist; “specialized doctor”", "저는 외과 전문의가 되고 싶어요."),
        ("책자", "(冊子) a booklet; a pamphlet", "보건부에서 질병예방에 대한 책자를 배포하고 있어요."),
        ("탈피(하다)", "(脫皮) break away from; escaping (to break away from; to escape)", "매일매일 같은 생활이 싫다. 탈피하고 싶다."),
        ("협회", "(協會) an association", ""),
    ]),
    ("학습활동 3", [
        ("금하다", "(禁) to prohibit", "캘리포니아에서는 실내 흡연을 금하고 있습니다.", "금지하다, 허용하다, 허가하다"),
        ("매점", "(賣店) a concession stand; a mini food store inside a building, etc.", "올해부터는 초중고 매점에서 탄산음료를 팔지 못합니다."),
        ("철거(하다/되다)", "(撤去) removing; tearing down; demolishing (structures or buildings) (to take down; to remove/to be torn down; to be demolished)", "노후된 이 아파트를 철거한다고 해서 주민들의 반대 농성이 이어지고 있습니다."),
    ]),
    ("학습활동 4", [
        ("궤양", "(潰瘍) an ulcer", "", "위궤양, 항궤양"),
        ("노화(하다/되다)", "(老化) aging; getting senile (to age)", "과일을 많이 먹으면 노화 방지에 도움이 된다고 합니다."),
        ("산소", "(酸素) oxygen", ""),
        ("산화(되다)", "(酸化) oxidation (to oxidize)", "야채와 과일에는 항산화 물질이 많이 들어 있습니다.", "항산화제"),
        ("방지(하다)", "(防止) prevention (to prevent)", "사고를 방지하기 위해 대책을 세워야 합니다.", "예방하다"),
        ("챙기다", "to take care of; to care for; to look after", "날씨가 점점 추워지는데 건강 잘 챙기세요."),
        ("항~", "(抗) anti- (as in antibiotics and antioxidant)", "항암치료를 받는 것이 너무 힘듭니다.", "항암, 항염, 항균, 항생제"),
    ]),
]
L3 = lesson(
    "U17 L5 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 고혈압 · 담석증 · 심근경색 · 전립선 · 강당 · 개최 · 신체나이 · 전문의 · 책자 · 탈피 · 협회 · 금하다 · 매점 · 철거 · 궤양 · 노화 · 산소 · 산화 · 챙기다 · 항~",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 고혈압, 담석증, 심근경색, 전립선, 협회, 궤양 and 산소. In the examples the book has G20 (written 지 이십 here). Under 궤양 the book lists 위궤양 and 항(抗)궤양, written 항궤양 here.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=14, nread=10)),
)

# ================================================================== L4 Part 2
_MENU5 = [
    ("나물 돌솥비빔밥 일 인분 사백팔십칠 점 오 킬로칼로리, 쇠고기 버섯죽 일 인분 사백팔십육 점 사 킬로칼로리, 자장면 한 그릇 팔백십팔 점 팔 킬로칼로리.", "Namul stone-pot bibimbap, one serving: 487.5 kcal; beef and mushroom porridge, one serving: 486.4 kcal; one bowl of jajangmyeon: 818.8 kcal."),
    ("경기도 안양시내 음식점들의 메뉴판이다.", "It is the menu board of restaurants in Anyang, Gyeonggi Province."),
    ("지방자치단체들이 먹을 거리의 안전성과 신뢰도를 높이기 위한 지원책을 잇따라 내놓고 있다.", "Local governments are putting out one after another support measures to raise the safety and credibility of food."),
    ("안양시는 식당별 음식의 영양정보를 제공하고, 과천시는 음식점 주방에 폐쇄회로텔레비전 설치를 지원하고 나섰다.", "Anyang City provides nutrition information of each restaurant’s food, and Gwacheon City has stepped forward to support installing closed-circuit TV in restaurant kitchens."),
    ("안양시는 각 음식점 식단의 영양 정보를 제공하는 홈페이지를 최근 개설했다고 육 일 밝혔다.", "Anyang City said on the 6th that it has recently opened a homepage that provides nutrition information on each restaurant’s menu. (The web address in the book is left out.)"),
    ("이곳에는 안양예술공원, 평촌학원가, 안양일번가, 범계역, 평촌역, 인덕원역 등 안양시내 여섯 개 지역 사백삼십육 개 음식점의 다양한 정보가 담겨 있다.", "It holds various information on 436 restaurants in six areas of Anyang, such as Anyang Art Park, the Pyeongchon cram-school district, Anyang First Street, and Beomgye, Pyeongchon and Indeogwon stations."),
    ("당뇨, 비만 등으로 음식 조절이 필요한 시민은 물론 성인병 예방을 위해 업소에서 파는 각 음식의 영양성분과 칼로리 등을 확인할 수 있다.", "Citizens who need to control their diet because of diabetes, obesity and so on, as well as those wanting to prevent adult diseases, can check the nutritional ingredients, calories and so on of each food sold at the establishments."),
    ("또 식품과 관련된 다양한 지식과 정보를 휴대전화로 받아 볼 수 있는 모바일 서비스도 추진 중이다.", "A mobile service through which people can receive various knowledge and information related to food on their mobile phones is also being pursued."),
    ("과천시는 식당을 찾은 손님들이 조리과정을 확인할 수 있도록 폐쇄회로텔레비전 설치를 지원하겠다고 최근 발표했다.", "Gwacheon City recently announced that it will support installing closed-circuit TV so that customers who visit restaurants can check the cooking process."),
    ("오는 육 월까지 모범 또는 대형음식점 열 곳을 뽑아 설치비 팔십만 원씩을 지원할 계획이다.", "It plans to choose ten model or large restaurants by June and support each with 800,000 won in installation costs."),
    ("이들 음식점에는 조리실 세 곳에서 네 곳에 카메라가 설치될 예정인데, 손님들이 모니터를 통해 조리 과정뿐 아니라 반찬 재사용 여부 등도 확인할 수 있게 된다.", "Cameras will be installed in three or four spots of the kitchens of these restaurants, and customers will be able to check through a monitor not only the cooking process but also whether side dishes are reused."),
]
_SPEAK5B = [("요즘은 한국에서도 비만 인구가 증가하고 있습니다. 친구와 함께 비만의 예방법과 해결책에 대해 이야기해 보세요.", "Nowadays the obese population is increasing in Korea too. Talk with a friend about ways to prevent obesity and solutions.")]
L4 = lesson(
    "U17 L5 · Part 2 (본 학습): BMI note and two cities’ food-safety measures",
    "본 학습 · 체질량 지수 · 비만 · 안양시 · 과천시 · 폐쇄회로텔레비전 · 영양정보 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 체질량 지수 (BMI, Body Mass Index)", "The book’s note, in English: 체질량 지수 is the numerical value obtained by dividing one’s weight (kg) by the square of the height (m). For example, if your weight is 60 kg and your height is 160 cm, your BMI is 60 ÷ (1.6 × 1.6) = 23.4. A person with a BMI of 18.5 or under is considered underweight; 18.5–24.9 is normal; 25–29.9 is overweight; and 30 or more is obese. If you know your height and weight in kg and cm, go to the website the book names and calculate your BMI. You can also use the website of the U.S. Department of Health and Human Services to calculate your BMI."),
        card("학습활동 3: two local governments’ support for food safety (Hankyoreh)", "The article, with my English (the book writes the figures and the web address in digits and letters; I wrote the figures out and left the address out). Answers: 1. The new Anyang website gives each restaurant’s nutrition information, calories and so on, so residents who must control their diet because of diabetes or obesity, and people who want to prevent adult diseases, can check what they eat; a mobile service for food knowledge is also planned. 2. Customers can check the cooking process, and whether side dishes are reused, on a monitor, through the closed-circuit cameras in the kitchen. 3. The underline is not marked in the text; my best guess is the third sentence, “Local governments are putting out one after another support measures to raise the safety and credibility of food.” 4. A possible Korean title (mine): 먹을 거리 안전과 신뢰를 높이는 지방자치단체들.", examples=passage(_MENU5)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK5B)),
        card("Activities left out", "학습활동 1 (Reading): a picture and text from edunet4u.net on the causes of obesity; you fill an English table of the stage of life or situation (puberty; eating leftover food; having a job; being less active but eating the same amount) and its reason for weight gain, and say why people tend to gain weight after they quit smoking. 학습활동 2 (Listening, tracks 011 and 012): a YTN news item on the health problems of Korean men in their 20s and 30s. It says that seven out of 100 men in their twenties and thirties have a problem (the answer is in the audio); you check why the problem is more prominent in younger men (choices: binge eating, lack of exercise, diabetes, overweight since childhood, video game addiction, depression, smoking, drinking) and fill a table of health issues and treatment. They are audio or pictures."),
    ],
    exercises=uniq(
        _tr(_MENU5[1:], k=3)
        + [M("What does the new Anyang homepage provide?", "Nutrition information on restaurants’ menus", ["Bus timetables", "Job listings", "Weather news"], "영양 정보."), M("What is Gwacheon City supporting?", "Closed-circuit TV in restaurant kitchens", ["Free meals", "New schools", "Parking lots"], "폐쇄회로텔레비전."), M("How much will Gwacheon support each of the ten restaurants?", "800,000 won", ["80,000 won", "8 million won", "Nothing"], "팔십만 원."), M("What can customers check through the monitors?", "The cooking process and whether side dishes are reused", ["The menu prices", "The weather", "The chef’s age"], "반찬 재사용 여부."), M("How is BMI calculated?", "Weight in kg divided by the square of height in m", ["Height divided by weight", "Weight times height", "Age divided by weight"], "체질량 지수."), M("In the book’s example, how much is the BMI of someone who weighs 60 kg and is 160 cm tall?", "23.4", ["18.5", "25", "30"], "23.4.")]
        + [F("안양시는 식당별 음식의 ___정보를 제공한다. (nutrition)", "영양", ["조리", "신뢰"], "영양정보."), F("과천시는 폐쇄회로텔레비전 ___를 지원한다. (installation)", "설치", ["조리", "개최"], "설치."), F("모범 또는 대형음식점 열 곳을 ___ 지원한다. (to pick)", "뽑아", ["내놓아", "철거해"], "뽑다.")]
        + [read_q("안양시는 식당별 음식의 영양정보를 제공합니다"), read_q("과천시는 폐쇄회로텔레비전 설치를 지원합니다"), read_q("조리 과정을 확인할 수 있습니다"), read_q("비만의 예방법과 해결책에 대해 이야기해 보세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("사회인", "(社會人) a working adult; a (full-fledged) member of society; a person who has “graduated” into society; “the person in society”", "저도 이제 대학을 졸업하고 사회인이 됩니다."),
        ("축적(하다/되다)", "(蓄積) accumulation; stockpiling (to accumulate/to be accumulated)", "저희 회사는 이십 년 넘게 기술을 축적하며 다양한 분야로 사업을 확장하고 있습니다."),
    ]),
    ("학습활동 2", [
        ("검토(하다/되다)", "(檢討) going over; review (to put on the table; to examine; to go over; to review/to be examined; to be reviewed)", "제가 낸 제안을 다시 한 번 검토해 주시기 바랍니다."),
        ("고도", "(高度) high degree; extreme", "이 일은 고도의 정밀함을 요구합니다."),
        ("관절염", "(關節炎) arthritis; “joint inflammation”", ""),
        ("노출(하다/되다)", "(露出) exposure (to expose/to be exposed)", "피부를 자외선에 너무 오랫동안 노출시키면 화상을 입을 수 있습니다."),
        ("수명", "(壽命) lifespan; the length of life", "현대의학의 발전으로 인간의 수명이 길어지고 있습니다."),
        ("식이습관", "(食餌習慣) eating habits; diet", "당뇨병 환자들은 식이습관이 아주 중요합니다.", "식습관"),
        ("약물", "(藥物) medicines; drugs", "운동 선수들은 정기적으로 약물 검사를 받습니다.", "약, 의약품"),
        ("이어지다", "to be continued; to continue; to go on; to last; “to become connected”", "올 경제 성장이 내년까지 이어질 전망이다."),
        ("초~", "(超) ultra~; super~; hyper~", "초고속 인터넷, 초미니 스커트, 초음파"),
        ("폭식(하다)", "(暴食) binge eating; “fierce eating” (to binge eat)", "저는 요즘 너무 바빠서 식사를 제 때 못 합니다. 그래서 폭식을 하는 경우가 많아요.", "과식, 폭음"),
    ]),
    ("학습활동 3", [
        ("나물", "edible grass or leaf", "봄나물로 비빔밥을 만들어 먹고 싶어요.", "채소, 야채"),
        ("내놓다", "to bring out", "손님들이 많이 오실 것 같아서 그릇을 다 내놓았다."),
        ("먹을 거리/먹거리", "things to eat; food; “material to eat”", "아이들의 먹을 거리 문화를 건강하게 바꾸고자 합니다.", "음식"),
        ("모범", "(模範) model; exemplary (as in a model student)", "부모는 아이들에게 모범이 되어야 합니다.", "모범택시"),
        ("버섯죽", "mushroom porridge", ""),
        ("성분", "(成分) an ingredient; a component", "이 약의 주요 성분이 무엇입니까?"),
        ("신뢰도", "(信賴度) degree of trustworthiness; credibility", "이번 조사 결과에 대한 대중의 신뢰도가 상당히 높습니다."),
        ("업소", "(業所) a store; a business", "이 근처에 자동차 정비 업소가 있습니까?"),
        ("조리(하다/되다)", "(調理) cooking (to cook/to be cooked)", "이 음식은 조리 시간이 짧아서 맞벌이 부부에게 아주 좋습니다.", "조리법, 조리 기구, 조리실"),
        ("지식", "(知識) knowledge", "저는 독서를 통해 지식을 많이 얻습니다."),
        ("폐쇄회로 TV", "(閉鎖回路) closed-circuit TV; CCTV", "모든 은행에는 폐쇄회로 티브이가 설치되어 있습니다."),
    ]),
]
L5 = lesson(
    "U17 L5 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 사회인 · 축적 · 검토 · 고도 · 관절염 · 수명 · 식이습관 · 약물 · 이어지다 · 초~ · 폭식 · 나물 · 먹거리 · 모범 · 성분 · 신뢰도 · 업소 · 조리 · 폐쇄회로 TV",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book adds under 고도 (高度) “high degree” that 고도 (古都) means “an ancient city; a former capital”. The book has no example for 관절염 and 버섯죽 (and no Hanja for 버섯죽). In the examples the book has 20년 (written 이십 년 here) and TV in capitals (티브이).")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3
_ED5 = [
    ("고콜레스테롤증, 당뇨, 고혈압, 비만, 심장병은 대표적인 성인병으로 꼽혔다. 그러나 이젠 어린이에게서도 심심찮게 나타난다.", "High cholesterol, diabetes, high blood pressure, obesity and heart disease were counted as typical adult diseases. But now they appear in children too, quite often."),
    ("건강보험심사평가원은 고콜레스테롤증으로 진료받은 열 살 이하 어린이가 이천이 년 천삼백이십칠 명에서 이천오 년 천구백구십구 명으로 삼 년 사이에 무려 이십일 점 팔 퍼센트나 늘었다고 밝혔다.", "The Health Insurance Review and Assessment Service said the number of children aged ten or under treated for high cholesterol rose from 1,327 in 2002 to 1,999 in 2005, a full 21.8 percent in three years."),
    ("같은 기간 비만은 오 점 구 퍼센트, 당뇨는 삼 점 사 퍼센트 늘었다. 요즘엔 어린이 성인병이라는 명칭이 고유명사로 자리잡았다.", "In the same period obesity rose 5.9 percent and diabetes 3.4 percent. These days the term “children’s adult diseases” has settled in as a proper noun."),
    ("가장 큰 이유는 잘못된 식생활이다. 기름기 많은 음식과 인스턴트 식품을 많이 섭취하기 때문인 것이다.", "The biggest reason is a wrong way of eating: it is because children take in many greasy foods and instant foods."),
    ("이런 음식에 공통적으로 많이 포함된 게 동물성 지방과 트랜스 지방이다.", "What these foods commonly contain a lot of is animal fat and trans fat."),
    ("하버드 의대는 천구백구십구 년, 트랜스 지방은 몸 속에 나쁜 콜레스테롤은 늘리고 좋은 콜레스테롤은 감소시켜, 역시 몸에 안 좋다는 동물성 기름보다 두 배나 더 해롭다고 발표했다.", "In 1999 Harvard Medical School announced that trans fat increases bad cholesterol in the body and reduces good cholesterol, and is twice as harmful as animal oil, which is also said to be bad for the body."),
    ("그래서 세계보건기구와 미국심장협회는 이천이 년 하루 섭취 열량 중 트랜스 지방은 일 퍼센트 미만으로 줄일 것을 권고했다.", "So in 2002 the World Health Organization and the American Heart Association recommended reducing trans fat to under 1 percent of daily calorie intake."),
    ("이런 권고에 따라 덴마크는 이천사 년부터 가공식품 성분 가운데 트랜스 지방이 이 퍼센트 이상 포함된 것은 아예 유통 판매를 금지시켰고, 캐나다는 이천오 년 십이 월, 미국은 올 유월부터 가공식품에 트랜스 지방 함유량을 표시하도록 의무화했다.", "Following this recommendation, Denmark from 2004 banned the distribution and sale altogether of processed foods with 2 percent or more trans fat, while Canada in December 2005 and the United States from June this year made it mandatory to show the trans fat content on processed foods."),
    ("미국의 뉴욕시 의회는 최근 한 걸음 더 나아가 모든 음식에 트랜스 지방 사용을 금지하는 법안을 통과시켰고, 시카고도 뒤따를 것으로 알려졌다.", "The New York City Council recently went a step further and passed a bill banning the use of trans fat in all food, and Chicago is reported to follow."),
    ("트랜스 지방을 많이 쓰는 다국적 패스트푸드 음식업체들은 이를 줄이거나 대체하기 위해 전전긍긍하고 있다. 맥도널드는 대체 기름을 시험 중이며, 웬디스, 케이에프시, 버거킹, 타코벨도 사용량을 줄이고 있다고 발표했다.", "Multinational fast-food companies that use a lot of trans fat are anxiously trying to reduce or replace it. McDonald’s is testing a substitute oil, and Wendy’s, KFC, Burger King and Taco Bell also announced they are cutting usage."),
    ("그러나 우리 정부는 태평스럽다. 어린이 건강에 경고음이 울리고, 성인병 인구가 급속히 늘고 있는데도 이에 대한 규제 장치 마련을 외면하고 있는 것이다.", "But our government is carefree. Though alarms are sounding for children’s health and the adult-disease population is growing rapidly, it is turning away from preparing regulatory mechanisms."),
    ("내년 십이 월부터 가공식품에 함유량을 표기하도록 하는 게 고작이다.", "At most it has people label the content on processed foods from December next year."),
    ("액체상태의 식물성 기름을 고체화하는 과정에서 생성되는 트랜스 지방은 단순히 심혈관계 질병만 유발하는 게 아니다. 간암, 위암, 대장암, 유방암과도 관련이 있는 것으로 알려졌다.", "Trans fat, produced in the process of solidifying liquid vegetable oil, does not simply cause cardiovascular diseases. It is also known to be related to liver, stomach, colon and breast cancer."),
    ("그러나 고소하고 바삭바삭한 맛 때문에 국민들은 쉽게 끊지 못한다. 정부가 나서는 수밖에 없다. 가공식품의 함량을 제한하거나, 뉴욕처럼 음식점에서 사용하지 못하도록 해야 한다.", "But because of its savory, crispy taste, people cannot easily give it up. The government has no choice but to step in. It must limit the content in processed foods or, like New York, keep restaurants from using it."),
]
_SLEEP5 = [("또, 너무 자야지 자야지 하면은 오히려 잠이 잘 안 옵니다. 그래서 더 긴장되고 흥분 돼서 잠이 안 오기 때문에 뭐 오늘 못 자면은 뭐 어때 이렇게 마음을 좀 편하게 드시는 것이 더 도움이 되겠습니다.", "Also, if you think too hard “I must sleep, I must sleep”, sleep rather doesn’t come. So you get more tense and excited and can’t sleep, so it would help more to take it easy, thinking “so what if I can’t sleep today”. (The four blanks are filled in from the audio by my best guess: 옵니다, 흥분, 어때, 편하게.)")]
_SPEAK5C = [("요즘은 어린이들도 비만, 고혈압, 심장질환과 같은 성인병에 걸린다고 합니다. 이런 성인병의 발병을 줄이기 위해서 사회와 정부가 할 수 있는 일이 무엇일지 생각해 보고 친구와 함께 이야기해 보세요.", "These days even children are said to get adult diseases such as obesity, high blood pressure and heart disease. Think about what society and the government can do to reduce the onset of these adult diseases and talk about it with a friend.")]
L6 = lesson(
    "U17 L5 · Part 3 (심화 학습): an editorial on trans fat and a sleep tip",
    "심화 학습 · 트랜스 지방 · 어린이 성인병 · 콜레스테롤 · 규제 · 수면 · 불면 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: “The government must actively step in to regulate trans fat” (an editorial)", "The editorial, with my English (the book writes the figures in digits and numbers its four paragraphs; the first paragraph is lines 1 to 3 here, the second lines 4 to 7, the third lines 8 to 10 and the fourth lines 11 to 14). Answers: 1. The purpose: D, to urge the government to take action against trans fat. 2. Summaries: ¶1 Adult diseases now appear in children; high cholesterol among children aged ten or under rose 21.8 percent in three years, and the term “children’s adult diseases” has become a proper noun. ¶2 The main cause is wrong eating habits (greasy and instant food, rich in animal fat and trans fat); Harvard said trans fat is twice as harmful as animal fat, and the WHO and American Heart Association recommended under 1 percent of daily calories. ¶3 Other countries have acted: Denmark, Canada, the U.S. and New York City; fast-food companies are trying to reduce or replace trans fat. ¶4 Korea’s government is carefree and has done almost nothing, but trans fat also relates to cancers, so the government must step in with limits. 3. The term is used because diseases once typical of adults, such as high cholesterol, obesity and diabetes, now appear in children, so the name has become a fixed term. 4. Denmark: since 2004, a ban on distribution and sale of processed foods with 2 percent or more trans fat. Canada: from December 2005, mandatory labeling of trans fat content on processed foods. U.S. in general: from June this year, mandatory labeling; New York City passed a bill banning it in all food and Chicago is expected to follow; fast-food firms are cutting or replacing it. Korea: the government is carefree and ignores regulation; at most it requires labeling from December next year. 5. The underline is not marked in the text; my best guess for the main point is “정부가 나서는 수밖에 없다. 가공식품의 함량을 제한하거나, 뉴욕처럼 음식점에서 사용하지 못하도록 해야 한다”: The government has no choice but to step in; it must limit the content in processed foods or, like New York, keep restaurants from using it.", examples=passage(_ED5)),
        card("학습활동 1: the sleep interview, fourth segment (listening)", "The book prints the paragraph with blanks that you transcribe from the audio and then translate. My completed version is a best guess:", examples=passage(_SLEEP5)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK5C)),
        card("Activities left out", "학습활동 1 (Listening, tracks 013 to 016): a YTN interview about a sleep survey, in four segments. You fill a table of topic, participants and result; say when one needs to consult a doctor; choose three suggestions for sleeping more soundly; and transcribe and translate the last paragraph (given above as my best guess). It is audio."),
    ],
    exercises=uniq(
        _tr(_ED5, k=3)
        + [M("What is the purpose of the editorial?", "To urge the government to take action against trans fat", ["To warn food companies", "To compare many countries", "To explain a treatment"], "D."), M("How much harmful is trans fat compared with animal oil, according to Harvard?", "Twice as harmful", ["Half as harmful", "The same", "Ten times"], "두 배."), M("Which country banned processed foods with 2 percent or more trans fat?", "Denmark", ["Canada", "Korea", "Japan"], "덴마크."), M("What did the New York City Council do?", "Passed a bill banning trans fat in all food", ["Required only labels", "Ignored the issue", "Built a hospital"], "법안."), M("What does the Korean government do about trans fat, at most?", "Requires labeling from December next year", ["Bans it", "Taxes it", "Nothing at all"], "표기."), M("What does 어린이 성인병 mean?", "Adult diseases that appear in children", ["A children’s hospital", "A kind of food", "A school subject"], "어린이 성인병.")]
        + [F("정부가 ___는 수밖에 없다. (step in)", "나서", ["외면하", "전전긍긍하"], "나서다."), F("가공식품에 함유량을 ___하도록 의무화했다. (to label)", "표시", ["대체", "규제"], "표시하다."), F("트랜스 지방은 심혈관계 질병을 ___한다. (to cause)", "유발", ["극복", "예방"], "유발하다.")]
        + [read_q("트랜스 지방은 몸에 해롭습니다"), read_q("정부가 나서는 수밖에 없습니다"), read_q("가공식품에 트랜스 지방 함유량을 표시하도록 했습니다"), read_q("성인병의 발병을 줄이기 위해서 무엇을 할 수 있을까요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("가라앉다", "to subside; to calm down; to quiet down; to sink", "햇빛 때문에 빨갛게 된 피부가 다 가라앉았다."),
        ("극복(하다/되다)", "(克服) overcoming (to overcome/to be overcome)", "장애인들은 편견을 극복하기 어렵다고 말합니다."),
        ("긴장되다", "(緊張) to be tense; to be edgy", "면접 시험 결과가 한 시간 후에 발표된다. 지금 많이 긴장된다."),
        ("냉수욕", "(冷水浴) cold-water bath", "자기 전에 냉수욕을 하는 것은 좋지 않습니다.", "온수욕"),
        ("마무리하다", "to finish; to wrap up", "손님들 올 시간이 다 됐어요. 청소를 빨리 마무리합시다."),
        ("미지근하다", "to be lukewarm", "세수를 할 때는 미지근한 물로 하면 좋아요."),
        ("심장 박동", "(心臟 搏動) heartbeat", "열심히 뛰었더니 심장 박동이 빨라졌어요.", "맥박"),
        ("수도권", "(首都圈) the metropolitan area; the capital and its satellite cities", "수도권 지역의 교통 문제가 심각합니다."),
        ("수면무호흡증", "(睡眠無呼吸症) sleep apnea; “no breathing symptom during sleep”", ""),
        ("신경이 곤두서다", "(神經) to feel edgy; to be on edge; to be tense; “nerves bristle up”", "김 선생님이 요즘 집안의 여러 가지 문제 때문에 신경이 곤두서 있습니다."),
        ("실태", "(實態) actual conditions; the realities", "노인문제의 실태를 조사해서 대책을 세웁시다."),
        ("열대야", "(熱帶夜) a tropical (sweltering) night", "요즘 열대야 때문에 잠을 잘 수가 없어요.", "열대야 현상"),
        ("인근", "(隣近) vicinity", "우리 부모님은 엘에이 인근에 사십니다.", "부근, 근처"),
        ("일시적", "(一時的) temporary", "이 진통제를 먹으면 일시적으로 고통이 사라집니다.", "영구적"),
        ("자극(하다/되다)", "(刺戟) stimulation (to stimulate/to be stimulated)", "포도주가 식욕을 자극해 줍니다."),
        ("자율신경", "(自律神經) an autonomic nerve", ""),
        ("잠들다/잠을 이루다", "to fall asleep", "이런저런 생각 때문에 어제는 잠을 이루지 못했다."),
        ("잠을 설치다", "to be unable to sleep well; to toss and turn", "어제는 너무 더워서 잠을 설쳤다."),
        ("주간졸림증", "(晝間) feeling sleepy during the day", ""),
        ("직전", "(直前) right before", "출발직전, 수업직전", "직후"),
        ("질", "(質) quality", "그 식당은 음식의 질은 별로지만 양이 많아서 자주 갑니다."),
        ("초조하다", "(焦燥) to be nervous; be on edge; to be anxious", "아들이 수술을 받는 동안 아버지가 밖에서 초조하게 기다리고 있다."),
        ("흥분(하다/되다)", "(興奮) excitement (to get excited)", "정권이 교체됐다는 소식에 군중이 흥분했습니다."),
    ]),
    ("학습활동 2", [
        ("경고음", "(警告音) an alarm; “alarming sound”", "자동차 경고음이 울리고 있어요. 가 보세요."),
        ("고유명사", "(固有名詞) a proper noun", ""),
        ("고작", "at most; at the very most; barely", "한 달을 열심히 일했는데 받은 월급은 고작 팔십만 원이다.", "겨우"),
        ("권고", "(勸告) advice; a recommendation", "의사의 권고에 따라 그는 담배를 끊었다."),
        ("규제장치", "(規制裝置) a regulatory mechanism", "정부는 사이버 범죄를 막기 위해 규제장치를 마련하기로 했습니다."),
        ("나서다", "to step forward; to come forward", "이 문제는 더 이상 기다리지 말고 우리가 나서서 해결합시다."),
        ("~는/(으)ㄹ 수밖에 없다", "can’t help but", "매일 기름기가 많은 음식을 먹으니 살이 찔 수밖에 없다."),
        ("대체(하다/되다)", "(代替) replacing (to replace/to be replaced)", "우리 회사에 그 사람을 대체할 사람은 없어요.", "대신하다"),
        ("심심찮게", "frequently", "요즘 티브이를 켜면 이상 기온에 대한 뉴스가 심심찮게 나온다."),
        ("심혈관", "(心血管) cardiovascular; “heart blood vessel”", ""),
        ("법안", "(法案) a bill; a draft of a law presented to a legislature for enactment", "그 법안은 국회에서 통과되었습니다."),
        ("외면하다", "(外面) to turn one’s face away (from); to disregard; to ignore", "그 아이가 너무 불쌍해서 외면할 수가 없었어요."),
        ("전전긍긍하다", "(戰戰兢兢) to be filled with trepidation; to be extremely nervous; to be in constant fear", "오늘 성적표를 받은 수진이는 엄마한테 혼날까 봐 전전긍긍하고 있다."),
        ("태평스럽다", "(太平) to be carefree; to be laid-back; to be easy going", "내일이 시험인데 너무 태평스러운 거 아니야?"),
        ("표시", "(表示) a mark", "감사의 표시로 저녁을 대접할까 합니다."),
        ("함유량/함량", "(含有量 or 含量) content; “contained amount”", "오렌지는 비타민 씨의 함유량이 높은 과일이다."),
        ("해롭다", "to be harmful", "흡연은 건강에 해롭습니다.", "이롭다, 유익하다"),
    ]),
]
L7 = lesson(
    "U17 L5 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 극복 · 긴장되다 · 냉수욕 · 수도권 · 수면무호흡증 · 열대야 · 일시적 · 자율신경 · 잠을 설치다 · 직전 · 초조하다 · 흥분 · 경고음 · 고유명사 · 고작 · 권고 · 규제장치 · 나서다 · 대체 · 법안 · 외면하다 · 전전긍긍 · 태평스럽다 · 함유량 · 해롭다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 수면무호흡증, 자율신경, 주간졸림증, 고유명사 and 심혈관. In the examples the book has LA (written 엘에이 here), 80만 원 (팔십만 원), TV (티브이) and Vitamin C (비타민 씨). 직전’s examples are the phrases 출발직전 and 수업직전, joined here.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=14)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 5: Modern Diseases I (현대병 I)", [L1, L2, L3, L4, L5, L6, L7])

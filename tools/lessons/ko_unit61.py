"""Unit 61: KBC Semester III, Unit 15, Lesson 6 - Environment (환경).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 15, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_W6 = [("생태계", "an ecosystem"), ("해수면", "the sea level"), ("온난화", "(global) warming"), ("파괴", "destruction; demolition"), ("친환경", "environment-friendly"), ("실천", "practice; action"), ("배출", "discharge; exhaust"), ("유해", "harm")]
_M6 = [("일회용품의 사용을 자제합시다.", "Let us refrain from using disposable goods."), ("출퇴근 시에 대중교통을 이용하여 자동차 매연을 줄입시다.", "Let us reduce car exhaust fumes by using public transportation when commuting."), ("병, 캔, 종이는 분리 수거하여 재활용할 수 있도록 합시다.", "Let us collect bottles, cans and paper separately so that they can be recycled."), ("빨래할 때 세제 사용을 줄여서 생활 하수를 줄입시다.", "Let us reduce household sewage by using less detergent when doing laundry."), ("재활용할 수 없는 폐기물은 소각합니다.", "Waste that cannot be recycled is incinerated."), ("농약과 화학 비료 사용을 줄여서 토양오염을 방지합시다.", "Let us prevent soil pollution by reducing the use of agricultural chemicals and chemical fertilizers.")]
_HJ6 = [("物 물", "object; thing", "물질, 폐기물"), ("溫 온", "warm", "온난화, 온실효과"), ("再 재", "again; re-", "재활용, 재생"), ("廢 폐", "discard(ed); abolish(ed)", "폐수, 폐지"), ("活 활", "life; live(ly)", "활용, 생활")]
_HJW6 = [("물질", "substance; material"), ("폐기물", "waste; “waste object”"), ("온난화", "(global) warming"), ("온실효과", "the greenhouse effect; “warm room effect”"), ("재활용", "recycling"), ("재생", "reproduction"), ("폐수", "wastewater"), ("폐지", "waste paper"), ("활용", "practical use; application"), ("생활", "life; living")]
_SIM6 = [("물품", "물건", "goods ≈ a thing"), ("농산물", "농작물", "farm products ≈ crops"), ("활발", "활달", "lively ≈ lively; cheerful"), ("철폐하다", "폐지하다", "to abolish ≈ to abolish")]
_REL6 = [("온실효과, 기온상승, 이상기후", "온난화", "greenhouse effect, temperature rise, abnormal climate: (global) warming"), ("종이, 캔, 플라스틱", "재활용", "paper, cans, plastic: recycling"), ("동물, 식물, 인간", "생물", "animals, plants, humans: living things"), ("쌀, 보리, 콩", "곡물", "rice, barley, beans: grain")]
_L6X = [("물품", "goods"), ("물건", "a thing; an article"), ("물가", "prices"), ("물량", "quantity; volume"), ("농산물", "farm products"), ("해산물", "seafood"), ("농작물", "crops"), ("내용물", "contents"), ("활발", "being lively"), ("활동", "activity"), ("활달", "being lively; being cheerful"), ("철폐하다", "to abolish"), ("폐차하다", "to scrap a car"), ("폐업하다", "to close down a business"), ("폐지하다", "to abolish"), ("기온상승", "a temperature rise"), ("이상기후", "abnormal climate"), ("곡물", "grain"), ("예물", "a wedding gift"), ("생물", "a living thing"), ("일회용품", "disposable goods"), ("대중교통", "public transportation"), ("매연", "exhaust fumes"), ("분리 수거", "separate collection"), ("세제", "detergent"), ("생활 하수", "household sewage"), ("소각하다", "to incinerate"), ("농약", "agricultural chemicals"), ("화학 비료", "a chemical fertilizer"), ("토양오염", "soil pollution"), ("자제하다", "to refrain from")]
L1 = lesson(
    "U15 L6 · Review: environment words and Sino-Korean 物 溫 再 廢 活",
    "환경 · 단어 복습 · 한자어 복습 · 생태계 · 해수면 · 온난화 · 친환경 · 배출 · 物 溫 再 廢 活",
    requires=[],
    cards=[
        card("단어 복습 1: the meanings (the book’s matching)", "The book asks you to match each word on the left with its meaning on the right (the first is done for you). The pairs:", tables=[ktable(_W6)]),
        card("단어 복습 2: efforts to protect the environment (my pairs)",
             "Each sentence is about an effort to protect the environment. The book asks you to connect each beginning with the ending that fits (the endings: 토양오염을 방지합시다; 생활 하수를 줄입시다; 자동차 매연을 줄입시다; 소각합니다; 재활용할 수 있도록 합시다; 자제합시다). My pairs, as whole sentences (the English is mine):",
             examples=passage(_M6)),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ6], say=[2]), ktable(_HJW6)]),
        card("한자어 복습 1: the word with a similar meaning (my answers)", "Circle the word whose meaning is similar to the word on the left (A. 물품: 물건, 물가, 물량; B. 농산물: 해산물, 농작물, 내용물; C. 활발: 활동, 활용, 활달; D. 철폐하다: 폐차하다, 폐업하다, 폐지하다).", tables=[table(["Word", "Similar word (my answer)", "Meaning"], [[a, b, c] for a, b, c in _SIM6], say=[0, 1])]),
        card("한자어 복습 2: the word that fits the three words (my answers)", "Choose from the box (곡물, 재활용, 예물, 생물, 온난화) the word most closely related to the three words on each line:", tables=[table(["The three words", "The word from the box (my answer)", "Meaning"], [[a, b, c] for a, b, c in _REL6], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L6X)]),
    ],
    exercises=uniq(
        _tr(_W6, k=3) + _tr(_HJW6, k=3) + _tr(_L6X, k=3) + _tr(_M6, k=3)
        + [M("What does the syllable 物 (물) mean?", "object; thing", ["warm", "again", "life"], "물질."), M("What does the syllable 溫 (온) mean?", "warm", ["object", "again", "discard"], "온난화."), M("What does the syllable 再 (재) mean?", "again; re-", ["warm", "object", "life"], "재활용."), M("What does the syllable 廢 (폐) mean?", "discard(ed); abolish(ed)", ["warm", "again", "life"], "폐수."), M("What does the syllable 活 (활) mean?", "life; live(ly)", ["object", "warm", "discard"], "활용."),
           M("Which word is similar to 물품?", "물건", ["물가", "물량", "물질"], "Goods."), M("Which word is similar to 농산물?", "농작물", ["해산물", "내용물", "곡물"], "Crops."), M("Which word is similar to 활발?", "활달", ["활동", "활용", "생활"], "Lively."), M("Which word is similar to 철폐하다?", "폐지하다", ["폐차하다", "폐업하다", "활용하다"], "To abolish."), M("Which word fits 온실효과, 기온상승, 이상기후?", "온난화", ["재활용", "곡물", "생물"], "Global warming."), M("Which word fits 종이, 캔, 플라스틱?", "재활용", ["곡물", "예물", "온난화"], "Recycling."), M("Which word fits 동물, 식물, 인간?", "생물", ["곡물", "예물", "재활용"], "Living things."), M("Which word fits 쌀, 보리, 콩?", "곡물", ["생물", "예물", "온난화"], "Grain."),
           F("일회용품의 사용을 ___합시다. (refrain from)", "자제", ["소각", "방지"], "자제하다."), F("재활용할 수 없는 폐기물은 ___합니다. (incinerate)", "소각", ["자제", "수거"], "소각하다."), F("농약과 화학 비료 사용을 줄여서 토양오염을 ___합시다. (prevent)", "방지", ["자제", "소각"], "방지하다."), F("병, 캔, 종이는 ___ 수거하여 재활용합시다. (separately)", "분리", ["대중", "생활"], "분리 수거."), F("출퇴근 시에 ___을 이용하여 자동차 매연을 줄입시다. (public transportation)", "대중교통", ["일회용품", "세제"], "대중교통."),
           read_q("일회용품의 사용을 자제합시다"), read_q("병과 캔과 종이는 분리 수거합시다"), read_q("재활용할 수 없는 폐기물은 소각합니다"), read_q("지구 온난화는 환경 파괴의 결과입니다"), read_q("친환경 제품을 실천합시다")]
    ),
)

# ================================================================== L2 Part 1
_GAS = [
    ("사무직 직장인의 근무 활동에서 발생하는 연간 온실가스 배출량이 일 인당 삼천팔백오십칠 킬로그램인 것으로 조사됐다.", "It was found that the annual greenhouse gas emissions generated by the work activities of office workers are 3,857 kilograms per person."),
    ("조사 대상 직장인들은 일일 근무시간이 평균 아홉 시간 오십일 분이었고 컴퓨터는 여덟 시간 이십이 분 사용했다.", "The surveyed workers’ daily working hours averaged 9 hours 51 minutes, and they used the computer for 8 hours 22 minutes."),
    ("이십오 퍼센트가 야근을 했고 출퇴근 교통수단은 자동차가 사십육 점 삼 퍼센트로 가장 많았다.", "25 percent worked overtime at night, and as the commuting means of transport, cars were the most common at 46.3 percent."),
]
_CLK = [
    ("십삼 일 오후 서울 소공동에서 환경재단이 주최하는 이천십 대륙별 환경위기시계 발표 행사가 열렸다.", "On the afternoon of the 13th, the “2010 Environmental Crisis Clock Announcement by Continent” event, hosted by the Korea Green Foundation, was held in Sogong-dong, Seoul."),
    ("환경재단은 환경위기시계의 세계 시각이 지난해보다 삼 분 느린 아홉 시 십구 분이라고 발표했다.", "The foundation announced that the world time of the Environmental Crisis Clock is 9:19, three minutes slower than last year."),
    ("한국의 시각은 아홉 시 삼십오 분으로 전 세계 평균시간보다 십육 분 빨랐으나 지난해 아홉 시 오십일 분보다는 십육 분 늦어졌다.", "Korea’s time is 9:35, 16 minutes faster than the world average time, but it became 16 minutes slower than last year’s 9:51."),
    ("환경위기시계는 자정에 가까울수록 환경위기가 심각하다는 것을 의미한다.", "The Environmental Crisis Clock means that the closer it is to midnight, the more serious the environmental crisis is."),
]
_SPEAK15 = [("재활용에 대해서 이야기해 봅시다.", "Let us talk about recycling."), ("재활용할 수 있는 것과 할 수 없는 것에는 어떤 것이 있는지 말해 보세요.", "Tell what things can be recycled and what things cannot."), ("각각의 물품 (캔, 빈 병, 종이, 플라스틱 등) 을 재활용할 때 주의할 점에 대해서도 이야기해 보세요.", "Also talk about the points to be careful about when recycling each item (cans, empty bottles, paper, plastic and so on).")]
L2 = lesson(
    "U15 L6 · Part 1 (도입 학습): greenhouse gas and the Environmental Crisis Clock",
    "도입 학습 · 공익광고 · 온실가스 배출량 · 직장인 · 환경위기시계 · 환경재단 · 재활용 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): a public service advertisement",
             "The advertisement is a picture (© KOBACO) with no text in the book. The book asks what it is about and gives three choices: A. A piggy bank made from a recycled material; B. The economic advantages of recycling; C. The number of disposable cups recycled in one year. The picture is not in the text, so the answer cannot be given here."),
        card("학습활동 2 (Reading): news on greenhouse gas emissions",
             "Read the article and the chart and choose the statement that fits the content. The article is the book’s with the numbers and units spelled out (3857 kg is 삼천팔백오십칠 킬로그램; 1인당 is 일 인당; 1일 is 일일; 9시간 51분 is 아홉 시간 오십일 분; 8시간 22분 is 여덟 시간 이십이 분; 25% is 이십오 퍼센트; 46.3% is 사십육 점 삼 퍼센트); the dot in 출·퇴근 is removed. The English is mine. The chart is not in the text.",
             examples=passage(_GAS)),
        card("학습활동 2: my answer",
             "The statements are: A. Air conditioning systems produced the greatest amount of greenhouse gas. B. The survey was conducted among blue-collar workers. C. Most interviewees used mass transit for their daily commute. D. The survey is about the amount of greenhouse gas produced by an office worker.\n\nMy answer is D. The article is about the yearly greenhouse gas emissions from the work activities of office workers (사무직 직장인). A is not stated in the text (the chart may show it, but the text does not), B is wrong (office workers, not blue-collar workers) and C is wrong (cars, at 46.3%, were the most common commuting means)."),
        card("학습활동 4 (Reading · Speaking): the Environmental Crisis Clock (환경위기시계)",
             "The following article is news about an event on the environment (Text and image © Kyunghyang). The text is the book’s with the numbers spelled out (13일 is 십삼 일; 2010 is 이천십; 3분 is 삼 분; 9시 19분 is 아홉 시 십구 분; 9시 35분 is 아홉 시 삼십오 분; 9시 51분 is 아홉 시 오십일 분; 16분 is 십육 분); the quotation marks ‘ ’ are removed. The English is mine.",
             examples=passage(_CLK)),
        card("학습활동 4: the questions answered (mine)",
             "1. 환경위기시계 is the Environmental Crisis Clock: a clock that shows how serious the environmental crisis is. The closer it is to midnight, the more serious the crisis.\n\n"
             "2. 9:19 is the world time of the Environmental Crisis Clock this year (three minutes slower than last year). 9:35 is Korea’s time this year (16 minutes faster than the world average). 9:51 is Korea’s time last year.\n\n"
             "3. This question asks for your own opinion about the time in your hometown and on the Monterey Peninsula and why; it has no single answer."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK15)),
        card("Activities left out", "학습활동 3 (a KBS report introducing an event in Seoul; you answer in English what the event is about and two reasons the event itself is good for the environment) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_GAS, k=3) + _tr(_CLK, k=3) + _tr(_SPEAK15, k=2)
        + [M("What is the survey about?", "Greenhouse gas emitted by an office worker", ["Air conditioners", "Blue-collar workers", "Public transit"], "D."), M("How much greenhouse gas does an office worker produce per year?", "3,857 kg", ["46.3 kg", "9 kg", "25 kg"], "삼천팔백오십칠 킬로그램."), M("What was the most common commuting means?", "A car (46.3%)", ["The subway", "The bus", "Walking"], "자동차."), M("What percent worked overtime at night?", "25 percent", ["46 percent", "10 percent", "50 percent"], "이십오 퍼센트."),
           M("What is the 환경위기시계?", "A clock showing how serious the environmental crisis is", ["A real clock", "A weather forecast", "A calendar"], "환경위기시계."), M("What does a time closer to midnight mean?", "A more serious environmental crisis", ["A safer environment", "A new day", "A cleaner world"], "자정에 가까울수록."), M("What was the world time announced?", "9:19", ["9:35", "9:51", "12:00"], "아홉 시 십구 분."), M("What was Korea’s time this year?", "9:35", ["9:19", "9:51", "12:00"], "아홉 시 삼십오 분."), M("What was Korea’s time last year?", "9:51", ["9:19", "9:35", "9:00"], "아홉 시 오십일 분."), M("Who hosted the event?", "The Korea Green Foundation (환경재단)", ["The government", "A school", "A company"], "환경재단."),
           F("환경위기시계는 ___에 가까울수록 환경위기가 심각하다. (midnight)", "자정", ["정오", "새벽"], "자정."), F("환경재단이 행사를 ___했다. (hosted)", "주최", ["발표", "개최"], "주최하다."), F("직장인의 연간 온실가스 ___량을 조사했다. (emission)", "배출", ["활용", "파괴"], "배출량."), F("컴퓨터는 여덟 시간 이십이 분 ___했다. (used)", "사용", ["조사", "발표"], "사용하다."),
           read_q("환경위기시계는 자정에 가까울수록 위기가 심각하다는 뜻입니다"), read_q("한국의 시각은 아홉 시 삼십오 분입니다"), read_q("직장인의 연간 온실가스 배출량을 조사했습니다"), read_q("재활용에 대해서 이야기해 봅시다"), read_q("자동차가 가장 많았습니다")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 3", [
        ("개최(하다/되다)", "(開催) hosting (of an event) (to hold/to be held)", "이천십 년 지이십 회담이 아시아에서는 처음으로 한국에서 개최됐습니다.", "열다"),
        ("관행", "(慣行) an existing custom; a customary practice; a convention", "관행대로 육십 세 이상만 등록이 가능합니다."),
        ("기존(의)", "(旣存) existing; established", "기존의 방식으로는 이 문제를 해결할 수 없습니다."),
        ("단위", "(單位) a unit; a measure", "킬로그램은 무게를 재는 단위입니다."),
        ("채광", "(採光) natural light (in a building or a house)", "집은 우선 채광이 좋아야 합니다."),
    ]),
    ("학습활동 4", [
        ("재단", "(財團) a foundation", "빌 게이츠가 장학재단을 설립했습니다."),
    ]),
]
L3 = lesson(
    "U15 L6 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 개최 · 관행 · 기존 · 단위 · 채광 · 재단",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 개최 (2010년 G-20 회담) and 관행 (60세) is spelled in Hangul here: 이천십 년 지이십 회담; 육십 세.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=5, nread=6)),
)

# ================================================================== L4 Part 2 texts
_FOOD = [
    ("칠레에서 온 포도, 필리핀에서 온 바나나, 미국에서 온 오렌지.", "Grapes from Chile, bananas from the Philippines, oranges from the United States."),
    ("마트에는 세계 각지에서 모여든 수입 농산물이 가득하다.", "The supermarket is full of imported farm products gathered from all over the world."),
    ("우리가 바다 건너 먼 길 온 농산물들을 먹는 호사를 누리는 동안 지구의 기온은 더 올라가고 우리 건강은 더욱 위협받는다.", "While we enjoy the luxury of eating farm products that came a long way across the sea, the Earth’s temperature rises further and our health is threatened even more."),
    ("이제는 로컬 푸드를 먹을 때다.", "Now is the time to eat local food."),
    ("음식이 생산지를 떠나 우리 입에 들어오기까지 이동한 총거리를 푸드 마일리지라고 한다.", "The total distance that food travels from leaving its place of production until it enters our mouths is called “food mileage.”"),
    ("이동 거리가 길면 이동 시간도 길어지고 보관과 품질에 문제가 생기기 쉽다.", "If the distance traveled is long, the travel time also becomes long, and problems with storage and quality easily arise."),
    ("푸드 마일리지가 적은 음식일수록 안전하고 건강한 식품이다.", "The lower the food mileage of a food, the safer and healthier the food is."),
    ("만약 백 년 후에 인류가 한 가장 바보 같은 짓이라는 책이 나온다면 우리나라가 지구 반대편에서 포도를 가져와 먹은 것이 일 등을 할 거예요.", "“If a book called ‘The Most Foolish Thing Humankind Did’ comes out a hundred years from now, our country’s bringing grapes from the other side of the Earth and eating them will win first place.”"),
    ("에코생협 안병덕 이사장의 뼈 있는 농담이다.", "This is a joke with a bone in it (a pointed joke) from An Byeong-deok, the chairman of Eco Consumers’ Cooperative."),
    ("부산에 살고 있다면, 미국에서 온 것보다는 아시아에서 온 것, 아시아에서 온 것보다는 서울에서 온 것, 서울에서 온 것보다는 대전에서 온 것이 더 좋다.", "If you live in Busan, what came from Asia is better than what came from the United States, what came from Seoul is better than what came from Asia, and what came from Daejeon is better than what came from Seoul."),
    ("식품의 이동 거리가 짧을수록, 즉 내가 사는 지역에서 생산되는 식품을 먹는 것이 가장 좋다.", "The shorter the food’s travel distance, that is, eating food produced in the region where I live, the better."),
    ("먹을거리가 이동할 때는 트럭이나 선박, 비행기 등의 운송 수단을 사용하게 되는데 이때 반드시 배출되는 것이 이산화탄소다.", "When food moves, means of transport such as trucks, ships and airplanes are used, and what is always emitted at that time is carbon dioxide."),
    ("먹을거리의 이동 거리가 길수록 이산화탄소 배출량이 늘어난다는 말.", "That is, the longer the food’s travel distance, the more the carbon dioxide emissions increase."),
    ("결국 멀리서 먹을거리를 옮겨와 먹을수록 지구 온난화를 가속시키는 것이다.", "In the end, the more we bring food from far away and eat it, the more we accelerate global warming."),
    ("일반 식품은 로컬 푸드에 비해 온실가스를 적게는 사 배에서 많게는 십칠 배나 배출한다니 날이 덥다고 투정하기 전에 장바구니를 살펴볼 필요가 있다.", "Ordinary food emits from as little as 4 times to as much as 17 times the greenhouse gas of local food, so before whining that the weather is hot, we need to look at our shopping baskets."),
]
_PAPER = [
    ("나무젓가락과 종이컵, 스티로폼 용기가 썩는 데 걸리는 기간은 각각 이십 년, 삼십 년, 오백 년이다.", "The periods it takes for wooden chopsticks, paper cups and Styrofoam containers to decompose are 20 years, 30 years and 500 years respectively."),
    ("환경운동연합 벌레 먹은 사과팀 이지현 처장은 “이제는 재활용을 넘어 발생 자체를 줄여야 한다”고 말한다.", "Lee Ji-hyun, director of the Worm-Eaten Apple team of the Korean Federation for Environmental Movements, says, “Now we must go beyond recycling and reduce the generation of waste itself.”"),
    ("발생 자체를 줄이라니, 막연하게 느낄 수도 있겠지만 자원을 아끼는 방법은 생각보다 쉽고 간단하다.", "“Reduce the generation itself?” You may feel it is vague, but the ways of saving resources are easier and simpler than you think."),
    ("현금인출기를 이용할 때 명세서 출력을 생략하거나 사무실에 개인 컵을 하나씩 두고 종이컵 대신 쓰면 굉장히 많은 자원이 절약돼요.", "“If you skip printing the statement when you use an ATM, or keep a personal cup in the office and use it instead of a paper cup, a great deal of resources are saved.”"),
    ("지로로 받던 고지서를 이메일 명세서로 받으면 지로로 쓰이는 종이와 집까지 배송되며 소비되는 에너지가 절약되죠.", "“If you receive by e-mail statement the bills you used to receive by giro, the paper used for giro and the energy consumed in delivering it to your home are saved.”"),
    ("자원 절약이라는 것이 어려운 게 아니에요.", "“Saving resources is not something difficult.”"),
    ("아침에 집에서 손수건을 하나 챙기면 하루 종일 핸드 드라이어나 페이퍼 타월로 소비되는 물자를 아낄 수 있다.", "If you take one handkerchief from home in the morning, you can save the materials consumed by hand dryers or paper towels all day long."),
    ("천으로 된 에코 백을 하나 접어서 가방 안에 넣어두면 쇼핑시 비닐봉투 대신 유용하게 사용할 수 있다.", "If you fold one cloth eco bag and keep it in your bag, you can use it usefully instead of a plastic bag when shopping."),
    ("아직까지 많은 분들이 환경운동 하면 어렵고 딱딱한 것으로 생각하고 계세요.", "“Even now, many people think of environmental activism as difficult and stiff.”"),
    ("아침에 나올 때 손수건 하나, 에코 백 하나 챙기는 게 어렵거나 시간이 많이 드는 일은 아니잖아요.", "“Taking one handkerchief and one eco bag when you leave in the morning is not difficult or time-consuming, is it?”"),
    ("조금만 생각을 전환하면 누구나 환경운동가가 될 수 있어요.", "“If you change your thinking just a little, anyone can become an environmental activist.”"),
]
_SPEAK16 = [("매일 먹는 음식 중에서 푸드 마일리지가 가장 긴 것과 가장 짧은 것은 무엇입니까?", "Of the foods you eat every day, which has the longest and which has the shortest food mileage?")]
L4 = lesson(
    "U15 L6 · Part 2 (본 학습): food mileage and saving resources",
    "본 학습 · 푸드 마일리지 · 로컬 푸드 · 이산화탄소 · 자원 절약 · 종이컵 · 에코 백 · 환경운동",
    requires=[],
    cards=[
        card("학습활동 1 (Reading · Speaking): imported farm products and food mileage",
             "The following is an article about farm products (Text and image © Kyunghyang). The text is the book’s with 100년 spelled out (백 년), 1등 (일 등), and 4배 (사 배) and 17배 (십칠 배); the quotation marks ‘ ’ around the words are removed, and the ellipsis after 오렌지 is replaced by a period. The English is mine.",
             examples=passage(_FOOD)),
        card("학습활동 1: the questions answered (mine)",
             "1. The sentence that best reflects the main idea: 이제는 로컬 푸드를 먹을 때다. (Now is the time to eat local food.)\n\n"
             "2. 푸드 마일리지 (food mileage) is the total distance that food travels from leaving its place of production until it enters our mouths (음식이 생산지를 떠나 우리 입에 들어오기까지 이동한 총거리).\n\n"
             "3. 뼈 있는 can be replaced by C. 의미가 있는 (meaningful; with a point): the joke has a serious point behind it.\n\n"
             "4. The underlined words in the last sentence are not visible in the text of the book. The last sentence says that, before whining that the weather is hot, we need to look at our shopping baskets; the writer uses it to say that our own food choices (imported food with large greenhouse gas emissions) contribute to the heat we complain about, so we should check what we buy.\n\n"
             "5. The book asks you to discuss in Korean, with your classmates, which of the foods you eat every day have the longest and the shortest food mileage."),
        card("학습활동 2 (Reading): reduce the generation of waste itself",
             "The following is an article about the environment (Text and image © Kyunghyang). The text is the book’s with the numbers spelled out (20년 is 이십 년; 30년 is 삼십 년; 500년 is 오백 년); a stray space after the opening quotation mark of the last quotation is removed. The English is mine.",
             examples=passage(_PAPER)),
        card("학습활동 2: the questions answered (mine)",
             "1. The numbers 20, 30 and 500 are the numbers of years it takes for wooden chopsticks, paper cups and Styrofoam containers, respectively, to decompose.\n\n"
             "2. The underlined sentences are not visible in the text of the book. The ways of saving resources mentioned include: skipping the printed statement when using an ATM; keeping a personal cup in the office and using it instead of paper cups; and receiving bills as an e-mail statement instead of by giro (the handkerchief and the cloth eco bag are given afterwards).\n\n"
             "3. Translation of the sentence “자원 절약이라는 것이 어려운 게 아니에요” (my guess for the underlined sentence, since the underline is not visible): “Saving resources is not something difficult.”"),
        card("말해 봅시다! (role-play)", "The book’s English instruction: “아래 상황에 맞춰 역할극을 해 봅시다.” (Let us do a role-play to fit the situation below.) You are at a market with your friend who wants to buy inexpensive produce from Chile. Persuade your friend to buy locally grown produce."),
        card("Question 5 (speaking)", "The book’s speaking prompt of 학습활동 1 (the English is mine):", examples=passage(_SPEAK16)),
        card("Activities left out", "학습활동 3 (a KBS documentary clip on climate change; you answer in English what meteorological and geographic changes are expected and how climate change can be prevented) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_FOOD, k=3) + _tr(_PAPER, k=3)
        + [M("What is the main idea of the food article?", "Now is the time to eat local food", ["Eat more imported fruit", "Stop eating fruit", "Grow bananas"], "로컬 푸드."), M("What is 푸드 마일리지?", "The total distance food travels from its place of production to our mouths", ["The price of food", "The calories in food", "The speed of delivery"], "총거리."), M("What does 뼈 있는 mean here?", "meaningful; with a point", ["bony", "funny", "excessive"], "의미가 있는."), M("What is always emitted when food is transported?", "Carbon dioxide", ["Oxygen", "Nitrogen", "Water"], "이산화탄소."), M("How much more greenhouse gas does ordinary food emit than local food?", "4 to 17 times", ["2 times", "100 times", "No difference"], "사 배에서 십칠 배."), M("Which place is best for a person living in Busan, among those listed?", "Daejeon", ["Seoul", "Asia", "The United States"], "대전."), M("What does a longer travel distance cause?", "More carbon dioxide emissions and more global warming", ["Cheaper food", "Fresher food", "Safer food"], "Longer distance means more emissions."),
           M("What do 20, 30 and 500 represent?", "The years wooden chopsticks, paper cups and Styrofoam take to decompose", ["Prices", "Weights", "Ages"], "썩는 데 걸리는 기간."), M("What does Lee Ji-hyun say we must go beyond?", "Recycling", ["Shopping", "Cooking", "Working"], "재활용을 넘어."), M("Which is a way of saving resources mentioned?", "Skipping the printed ATM statement", ["Buying more paper cups", "Printing every bill", "Using plastic bags"], "명세서 출력을 생략하다."), M("What can replace a paper cup in the office?", "A personal cup", ["A plastic bag", "A paper towel", "A hand dryer"], "개인 컵."), M("What can you use instead of a plastic bag when shopping?", "A cloth eco bag", ["A paper cup", "A handkerchief", "A giro"], "에코 백."), M("What do many people think environmental activism is?", "Difficult and stiff", ["Fun and easy", "Expensive", "Unnecessary"], "어렵고 딱딱한 것."),
           F("먹을거리의 이동 거리가 길수록 이산화탄소 ___량이 늘어난다. (emission)", "배출", ["보관", "생략"], "배출량."), F("멀리서 옮겨와 먹을수록 지구 온난화를 ___시킨다. (accelerate)", "가속", ["생략", "전환"], "가속시키다."), F("날이 덥다고 ___하기 전에 장바구니를 살펴보자. (whine)", "투정", ["농담", "출력"], "투정하다."), F("명세서 출력을 ___하면 자원이 절약된다. (omit)", "생략", ["가속", "보관"], "생략하다."), F("조금만 생각을 ___하면 누구나 환경운동가가 될 수 있다. (change)", "전환", ["생략", "출력"], "전환하다."), F("우리는 먼 길 온 농산물을 먹는 ___를 누린다. (luxury)", "호사", ["농담", "투정"], "호사."),
           read_q("이제는 로컬 푸드를 먹을 때입니다"), read_q("푸드 마일리지가 적은 음식일수록 안전합니다"), read_q("이산화탄소 배출량이 늘어납니다"), read_q("손수건 하나 에코 백 하나를 챙깁니다"), read_q("종이컵 대신 개인 컵을 씁니다"), read_q("자원 절약은 어려운 일이 아닙니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("가속(하다/되다)", "(加速) acceleration (to accelerate/to be accelerated)", "지구 온난화가 가속화되고 있습니다."),
        ("누리다", "to enjoy", "저도 행복을 누리며 살고 싶습니다.", "향유하다, 만끽하다, 즐기다"),
        ("농담(하다)", "(弄談) a joke (to joke; to kid)", "농담이 지나치십니다."),
        ("보관(하다/되다)", "(保管) storage (to keep; to store/to be kept; to be stored)", "상하기 쉬운 음식은 저온에 보관하십시오."),
        ("살피다", "to take a good look at; to inspect closely; to look around", "길을 건널 때는 양쪽을 모두 잘 살펴야 합니다.", "관심을 갖다, 주의를 기울이다"),
        ("인류", "(人類) humanity; humankind", "인류의 역사를 바꾼 발명품에는 무엇이 있을까요?", "사람, 인간"),
        ("장바구니", "(場) a shopping basket", "시장 갈 때 장바구니를 들고 가면 환경을 보호할 수 있어요."),
        ("투정(하다/부리다)", "complaint; whining (to complain; to whine)", "아이의 반찬 투정이 시작됐습니다."),
        ("호사(스럽다)", "(豪奢) luxury; extravagance (to be luxurious; to be extravagant)", "친구는 결혼 후에 호사스럽게 살고 있다.", "사치"),
    ]),
    ("학습활동 2", [
        ("고지서", "(告知書) a (tax, utility, phone, etc.) bill; a notice", "휴대폰 요금 고지서는 매달 언제 나옵니까?", "통지서"),
        ("딱딱하다", "to be formal; to be unfriendly; to be hard; to be stiff", "연설 내용이 너무 딱딱해서 지루했습니다. 과자가 맛있는데 너무 딱딱해요. 그 신입사원은 고집이 세고 너무 딱딱해."),
        ("막연하다", "(漠然) to be vague", "질문이 너무 막연해서 답을 하기가 곤란합니다."),
        ("명세서", "(明細書) a detailed statement", "급여 명세서가 도착했어요."),
        ("벌레", "an insect; a bug; a worm", ""),
        ("생략(하다/되다)", "(省略) omission (to omit/to be omitted)", "시간이 없어서 경기 참가자 소개는 생략하겠습니다."),
        ("스티로폼", "Styrofoam", ""),
        ("전환(하다/되다)", "(轉換) change; switch; conversion (to change; to switch; to convert/to be changed; to be switched; to be converted)", "보통예금을 적금으로 전환하고 싶어요.", "바꾸다"),
        ("지로", "a type of bill payment system available at a bank", "한국에서는 많은 사람들이 지로로 공과금을 납부합니다."),
        ("천", "cloth; fabric", "이 천은 너무 거칠어서 옷 만들기가 어렵겠어요.", "옷 | 천 (千) a thousand; 천 (川) a stream; a creek"),
        ("출력(하다/되다)", "(出力) output; print (to output; to print/to be printed)", "서류를 출력해 드릴 테니 서명해 주세요."),
        ("현금인출기", "(現金引出機) an automated teller machine (ATM); “cash withdrawing machine”", ""),
    ]),
    ("학습활동 3", [
        ("남용(하다/되다)", "(濫用) abuse (to abuse/to be abused)", "국회의원들의 권력 남용이 사회적으로 큰 문제가 되고 있다.", "악용하다, 오용하다"),
        ("불명예", "(不名譽) dishonor; disgrace", "그런 행동은 불명예스러운 것입니다.", "명예"),
        ("속출(하다)", "(續出) continuous occurrence (to occur in succession)", "집중호우로 인한 피해가 속출하고 있습니다.", "발생"),
        ("예외", "(例外) an exception", "예외 없는 규칙은 없다."),
        ("위력", "(威力) power; force", "폭풍의 위력이 대단합니다.", "힘"),
        ("이변", "(異變) an unusual event; an unexpected change; a twist; an accident; “different change”", "칠월에 눈이 내리는 이변이 발생했습니다."),
        ("폭염", "(暴炎) heat wave; sweltering heat; “explosive heat”", "폭염으로 인한 피해자가 속출하고 있습니다.", "무더위 | 날씨, 자연재해"),
        ("화석연료", "(化石燃料) a fossil fuel", "화석연료의 남용은 재앙을 초래합니다.", "석유, 석탄"),
    ]),
]
L5 = lesson(
    "U15 L6 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 가속 · 누리다 · 보관 · 장바구니 · 투정 · 호사 · 고지서 · 명세서 · 생략 · 전환 · 출력 · 남용 · 이변 · 폭염 · 화석연료",
    requires=[],
    cards=vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3 text
_INT = [
    ("이경재 씨, 대지를 위한 바느질에 대한 소개를 부탁 드립니다.", "Mr. Lee Gyeong-jae, please introduce “Sewing for the Earth” (대지를 위한 바느질)."),
    ("저는 친환경 의류 디자이너입니다.", "“I am an environment-friendly clothing designer."),
    ("대지를 위한 바느질은 친환경 의류를 주로 만드는 기업으로 설립된 지 이 년 반 정도 되었네요.", "Sewing for the Earth is a company that mainly makes environment-friendly clothing, and it has been about two and a half years since it was established."),
    ("사업은 아직 시작단계라고 봐도 좋아요.", "You may regard the business as still being in its starting stage."),
    ("파트는 크게 웨딩, 리빙, 단체복 (친환경 환자복 등) 세 가지로 나뉘어요.", "It is divided broadly into three parts: wedding, living and group clothing (environment-friendly patient gowns and so on).”"),
    ("친환경 웨딩에 대해 구체적으로 설명해 주세요.", "Please explain environment-friendly weddings in detail."),
    ("처음에는 웨딩드레스부터 시작했어요.", "“At first I started with wedding dresses."),
    ("이천오 년 대학원을 다니며 연예인들이 수천만 원짜리 드레스를 입고 결혼했다는 기사를 보았어요.", "In 2005, while attending graduate school, I saw articles saying that celebrities got married wearing dresses worth tens of millions of won."),
    ("그렇게 화려하고 값비싼 드레스를 고작 며칠 입고 버리는 것이 아까웠어요.", "It seemed a waste to wear such gorgeous and expensive dresses for barely a few days and throw them away."),
    ("폐기처분된 드레스는 결국 환경오염의 주범이 되구요.", "And the discarded dresses end up becoming a main culprit of environmental pollution."),
    ("그래서 드레스를 바꿔 보자라는 생각을 했고 대학원 교수님을 통해 옥수수전분으로 만든 비닐을 알게 되었어요.", "So I thought, ‘Let’s change the dress,’ and through a graduate school professor I learned about vinyl made from corn starch."),
    ("물론 옥수수 비닐은 한 달 정도 만에 다 썩어서 자연으로 돌아가는 무해한 성분이에요.", "Of course, corn vinyl is a harmless material that completely decomposes in about a month and returns to nature."),
    ("그리고 그걸로 드레스를 만들어 전시를 한 번 했는데 반응이 좋았어요.", "And I made a dress with it and held an exhibition once, and the response was good."),
    ("그 이후 다른 것은 친환경으로 할 수 없냐는 문의가 들어왔고 친환경 웨딩사업이 시작됐어요.", "After that, inquiries came in asking whether other things could not be made environment-friendly too, and the environment-friendly wedding business began."),
    ("친구들과 함께 개발한 콩기름 인쇄 청첩장, 뿌리가 살아 있는 부케 (결혼식을 하고 난 후 땅에 다시 심는 방식), 친환경 유기농 음식 등을 도입하기 시작했어요.", "We began to introduce wedding invitations printed with soybean oil, which I developed with friends, bouquets with living roots (a method of replanting them in the ground after the wedding), environment-friendly organic food and so on."),
    ("그렇게 현재까지는 총 스물여덟 쌍의 커플이 결혼했어요.", "In that way, a total of 28 couples have married up to now.”"),
    ("친환경 결혼식 치룬 부부들의 가정 속에서 이루어진 변화가 있나요?", "Have there been changes in the homes of the couples who had an environment-friendly wedding?"),
    ("예비 신랑신부님들이 처음 친환경 결혼을 결정하실 때 환경에 의미를 두고 하시는 분들도 계시지만 꼭 그렇지 않아도 특별한 결혼식을 위해 하시는 분들도 종종 계세요.", "“When prospective brides and grooms first decide on an environment-friendly wedding, some attach meaning to the environment, but there are also often people who do it for a special wedding even if that is not necessarily the case."),
    ("하지만 결혼식을 치룬 후, 그냥 지나치던 작은 일도 환경을 위한 습관으로 변해가고 있다는 얘기를 듣곤 해요.", "But after the wedding, I often hear that even small things they used to just pass over are turning into habits for the environment."),
    ("그런 이야기를 들으면 정말 흐뭇하고 일의 보람을 느끼죠.", "When I hear such stories, I feel really pleased and feel the reward of my work.”"),
]
_SPEAK17 = [("환경에 유익한 생활습관과 환경에 해가 되는 생활습관은 어떤 것들이 있는지 이야기해 봅시다.", "Let us talk about what kinds of living habits are good for the environment and what kinds are harmful to it."), ("오늘 배운 내용을 바탕으로 환경의 중요성과 환경을 지킬 방법에 대해 이야기해 봅시다.", "Based on what you learned today, let us talk about the importance of the environment and ways to protect it.")]
L6 = lesson(
    "U15 L6 · Part 3 (심화 학습): an interview with an eco-friendly clothing designer",
    "심화 학습 · 친환경 의류 · 대지를 위한 바느질 · 친환경 웨딩 · 옥수수 비닐 · 폐기처분 · 환경운동 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2 (Reading): an interview with an eco-friendly clothing designer",
             "The following is part of an interview with a clothing designer in a magazine (Text and image © Kyunghyang). The text is the book’s with the numbers spelled out (2년 반 is 이 년 반; 2005년 is 이천오 년; 28쌍 is 스물여덟 쌍); the quotation marks ‘ ’ are removed (the book writes 드레스를 바꿔 보자 in quotation marks and 대지를 위한 바느질 in single quotation marks). The English is mine; the interviewer’s questions are given without quotation marks and the designer’s answers continue across lines.",
             examples=passage(_INT)),
        card("학습활동 2: the questions answered (mine)",
             "1. The sentence that accurately reflects the passage is D: bouquets and invitation cards were made from environment-friendly materials (the bouquet has living roots to replant after the wedding; the invitation is printed with soybean oil). A is wrong: the corn vinyl dress was made and exhibited; B is wrong: she started the business after the exhibition drew inquiries, not after making her own wedding dress; C is wrong: some of the couples did it simply for a special wedding.\n\n"
             "2. 대지를 위한 바느질 (Sewing for the Earth) is a company, set up about two and a half years ago by the interviewee, an environment-friendly clothing designer, that mainly makes environment-friendly clothing. The business is still in its starting stage and is divided broadly into three parts: wedding, living and group clothing (such as environment-friendly patient gowns).\n\n"
             "3. The first item she made was a wedding dress. She made it because she was bothered that celebrities wear gorgeous, expensive dresses (worth tens of millions of won) for barely a few days and then throw them away, and the discarded dresses become a main culprit of environmental pollution. She learned about vinyl made from corn starch, which decomposes in about a month, and made the dress from it.\n\n"
             "4. What makes her work rewarding: she hears that after their eco-friendly wedding the couples’ small everyday matters that they used to pass over have turned into habits for the environment, and when she hears such stories she feels pleased and feels the reward of her work."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK17)),
        card("Activities left out", "학습활동 1 (a Seoul mayor’s talk on the environment from the Seoul education office; why the speaker mentions Switzerland and three ways to protect the environment) and 학습활동 3 (information on endocrine disruptors, 환경호르몬: the origin of the term, who must be cautious about plastic utensils and why, and the advice given) are audio activities."),
    ],
    exercises=uniq(
        _tr(_INT, k=3) + _tr(_SPEAK17, k=2)
        + [M("What is the interviewee’s job?", "An environment-friendly clothing designer", ["A teacher", "A journalist", "A chef"], "친환경 의류 디자이너."), M("What are the three parts of the company?", "Wedding, living and group clothing", ["Food, travel and toys", "Shoes, hats and bags", "Schools, banks and hospitals"], "웨딩, 리빙, 단체복."), M("What did she make first?", "A wedding dress", ["A bouquet", "An invitation", "A hospital gown"], "웨딩드레스."), M("What was the first dress made from?", "Vinyl made from corn starch", ["Silk", "Paper", "Cotton"], "옥수수전분으로 만든 비닐."), M("How long does the corn vinyl take to decompose?", "About a month", ["A year", "A week", "500 years"], "한 달 정도."), M("What are the invitations printed with?", "Soybean oil", ["Plastic", "Corn oil", "Water"], "콩기름."), M("What is special about the bouquet?", "Its roots are alive and it is replanted after the wedding", ["It is made of plastic", "It is eaten", "It is thrown away"], "뿌리가 살아 있는 부케."), M("How many couples have married so far?", "28 couples", ["2 couples", "100 couples", "5 couples"], "스물여덟 쌍."), M("What makes her work rewarding?", "Couples’ small matters turning into habits for the environment", ["High prices", "Fame", "Free dresses"], "보람."),
           F("저는 ___ 의류 디자이너입니다. (environment-friendly)", "친환경", ["유해", "폐기"], "친환경."), F("폐기처분된 드레스는 환경오염의 ___가 된다. (main culprit)", "주범", ["성분", "보람"], "주범."), F("옥수수 비닐은 한 달 정도 만에 다 ___ 자연으로 돌아간다. (decomposes)", "썩어서", ["살아서", "나뉘어서"], "썩다."), F("드레스를 ___ 며칠 입고 버리는 것이 아까웠다. (barely)", "고작", ["종종", "물론"], "고작."), F("일의 ___을 느끼죠. (the reward)", "보람", ["성분", "주범"], "보람을 느끼다."),
           read_q("저는 친환경 의류 디자이너입니다"), read_q("옥수수 비닐은 한 달 정도 만에 다 썩습니다"), read_q("콩기름으로 청첩장을 인쇄했습니다"), read_q("뿌리가 살아 있는 부케를 땅에 다시 심습니다"), read_q("환경에 유익한 생활습관에 대해 이야기해 봅시다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("공감(하다/되다)", "(共感) sympathy; “same feeling” (to sympathize/to be sympathetic)", "환경 보호에 대한 선생님 의견에 공감합니다."),
        ("도보", "(徒步) walking (on foot)", "우리 집은 지하철 역에서 도보로 십 분 거리에 있다.", "걷기, 도보여행, 속보, 경보"),
        ("지구", "(地球) the Earth; the globe; “earth ball”", ""),
        ("휘발유", "(揮發油) gas(oline); “inflammable oil”", "휘발유가 다 떨어졌어요.", "석유, 경유, 등유, 원유"),
    ]),
    ("학습활동 2", [
        ("고작", "only; just; barely; no more than", "그 모임에 참가한 사람은 고작 열 명이었습니다.", "겨우"),
        ("대지", "(大地) the earth; Mother Earth; “big earth”", "촉촉한 봄비가 대지를 적시고 있어요.", "땅"),
        ("바느질", "sewing; needlework", "우리 어머니는 바느질 솜씨가 아주 좋으십니다."),
        ("보람을 느끼다", "to be rewarding; to feel rewarded; “to feel worthwhile”", "저는 지금 하는 일에 큰 보람을 느낍니다."),
        ("성분", "(成分) an ingredient; a component; a constituent", "영양제의 주성분은 무엇입니까?", "재료"),
        ("종종", "(種種) sometimes; occasionally; often; frequently", "한국 식당에서 종종 지인을 만납니다.", "가끔, 자주"),
        ("주범", "(主犯) a main culprit", "배기가스가 지구 온난화의 주범입니다.", "공범, 범죄"),
        ("폐기처분(하다/되다)", "(廢棄處分) waste disposal (to discard/to be discarded)", "고장 난 가전 제품을 폐기처분 하려면 어떻게 해야 합니까?", "버리다"),
    ]),
    ("학습활동 3", [
        ("경로", "(經路) a route; a course; a channel", "바이러스의 감염 경로를 찾고 있습니다."),
        ("내분비계", "(內分泌系) endocrine system", ""),
        ("대처(하다)", "(對處) handling; coping with; dealing with (to handle; to cope with; to deal with)", "사고가 발생하면 침착하게 대처하세요."),
        ("데우다", "to heat up; to warm up", "밥이 너무 차니까 전자레인지에 데워 드세요."),
        ("방출(하다/되다)", "(放出) release (to release/to be released)", "공기에 방출되는 매연이 심각한 수준입니다.", "배출"),
        ("실체", "(實體) the true nature (of something or an entity); the truth; “real body”", "이제 사건의 실체를 파악한 것 같습니다."),
        ("오존층", "(層) ozone layer", "", "지구 온난화"),
        ("용기", "(容器) a container", "플라스틱 용기보다 유리 용기를 사용하는 것이 좋습니다.", "그릇"),
        ("인체", "(人體) human body; human organism", "담배는 인체에 해롭습니다.", "몸"),
        ("정자", "(精子) sperm", ""),
        ("지피지기면 백전백승", "(知彼知己 百戰百勝) If you know your enemies and yourself, you can win every battle. (proverb from The Art of War, a Chinese military treatise)", ""),
        ("퍼지다", "to spread", "소문은 정말 빨리 퍼지는군요.", "번지다"),
        ("호르몬", "a hormone", ""),
        ("흡수(하다/되다)", "(吸收) absorption (to absorb/to be absorbed)", "커피를 많이 마시면 칼슘이 몸에 잘 흡수되지 않습니다."),
    ]),
]
L7 = lesson(
    "U15 L6 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 공감 · 도보 · 휘발유 · 고작 · 대지 · 바느질 · 주범 · 폐기처분 · 대처 · 방출 · 용기 · 인체 · 호르몬 · 흡수",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 도보로 10분 → 도보로 십 분; 고작 10명 → 고작 열 명. The book lists 폐기처분(하다/되다) with a line break inside the parentheses.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=12, nread=12)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 6: Environment (환경)", [L1, L2, L3, L4, L5, L6, L7])

"""Unit 63: KBC Semester III, Unit 15, Lesson 8 - North Korea I (북한 I).
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
_W8 = [("교류", "exchange"), ("군사분계선", "Military Demarcation Line (MDL)"), ("분단", "division"), ("회담", "a meeting; a conference"), ("결핍", "lack; shortage"), ("친선", "friendship; amity"), ("식량", "food; provisions"), ("원조", "assistance; support; aid")]
_A8 = [("공동", "단독", "joint ↔ sole; independent"), ("거부하다", "허락하다", "to refuse ↔ to permit"), ("전쟁", "평화", "war ↔ peace"), ("들어서다", "나가다", "to step in ↔ to go out"), ("떳떳하다", "부끄럽다", "to be proud ↔ to be ashamed"), ("이탈하다", "복귀하다", "to break away ↔ to return"), ("민간인", "군인", "a civilian ↔ a soldier")]
_HJ8 = [("交 교", "interact; give and take; make a friend; relationship", "교류, 절교"), ("軍 군", "military", "국군, 행군"), ("流 류", "flow", "유입, 유동"), ("助 조", "help; assistant", "원조, 구조"), ("協 협", "cooperate", "협의, 협조")]
_HJW8 = [("교류", "exchange; interchange"), ("절교", "severing a relationship"), ("국군", "the Korean Armed Forces; “nation’s military”"), ("행군", "(military) marching"), ("유입", "inflow; influx"), ("유동", "a flow; flowing"), ("원조", "support; assistance"), ("구조", "rescue"), ("협의", "consultation; “cooperative discussion”"), ("협조", "cooperation")]
_ANT8 = [("유입", "유출", "inflow ↔ outflow"), ("협조", "비협조", "cooperation ↔ non-cooperation"), ("군인", "민간인", "a soldier ↔ a civilian"), ("교제", "절교", "association ↔ severing a relationship")]
_REL8 = [("유입, 유포, 유출", "유통", "inflow, spreading, outflow: distribution; circulation"), ("조수, 조연, 조교", "조력", "an assistant, a supporting role, a teaching assistant: help; aid"), ("충고, 도움말, 격려의 말", "조언", "advice, helpful words, words of encouragement: advice")]
_L8X = [("유실", "loss"), ("유행", "a fashion; a trend"), ("유출", "outflow; a leak"), ("유창", "being fluent"), ("협력", "cooperation"), ("협소", "being narrow"), ("비협조", "non-cooperation"), ("사병", "an enlisted soldier"), ("장교", "an officer"), ("민간인", "a civilian"), ("교제", "association; dating"), ("교환", "exchange"), ("외교", "diplomacy"), ("유포", "spreading"), ("유통", "distribution"), ("조수", "an assistant"), ("조연", "a supporting role"), ("조교", "a teaching assistant"), ("조력", "help; aid"), ("조언", "advice"), ("충고", "advice; a warning"), ("도움말", "helpful words"), ("단독", "being sole; being independent"), ("허락하다", "to permit"), ("복귀하다", "to return"), ("떳떳하다", "to be proud; to be above-board"), ("부끄럽다", "to be ashamed"), ("이탈하다", "to break away"), ("들어서다", "to step in")]
L1 = lesson(
    "U15 L8 · Review: inter-Korean words and Sino-Korean 交 軍 流 助 協",
    "북한 I · 단어 복습 · 한자어 복습 · 교류 · 군사분계선 · 분단 · 회담 · 원조 · 交 軍 流 助 協",
    requires=[],
    cards=[
        card("단어 복습 1: the meanings (the book’s matching)", "The book asks you to match each word on the left with the same meaning on the right (the first, 교류, is done for you). The pairs:", tables=[ktable(_W8)]),
        card("단어 복습 2: the opposite word (my pairs)", "The book asks you to connect each word on the left with the word of the opposite meaning on the right (the right column: 부끄럽다, 나가다, 단독, 복귀하다, 허락하다, 군인, 평화; the first pair, 공동 and 단독, is done for you). My pairs:", tables=[table(["Word", "Opposite", "Meaning"], [list(r) for r in _A8], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ8], say=[2]), ktable(_HJW8)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word of the opposite meaning (A. 유입: 유실, 유행, 유출, 유창; B. 협조: 협력, 협소, 비협조, 협의; C. 군인: 사병, 장교, 행군, 민간인; D. 교제: 교류, 교환, 절교, 외교).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [[a, b, c] for a, b, c in _ANT8], say=[0, 1])]),
        card("한자어 복습 2: the word that fits the three words (my answers)", "Choose from the box (유행, 원조, 유통, 조력, 조언) the word most closely related to the three words on each line:", tables=[table(["The three words", "The word from the box (my answer)", "Meaning"], [[a, b, c] for a, b, c in _REL8], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L8X)]),
    ],
    exercises=uniq(
        _tr(_W8, k=3) + _tr(_HJW8, k=3) + _tr(_L8X, k=3) + _tr([(a + " ↔ ?", c.split(" ↔ ")[1]) for a, b, c in _A8], k=3)
        + [M("What does the syllable 交 (교) mean?", "interact; give and take; make a friend; relationship", ["military", "flow", "help"], "교류."), M("What does the syllable 軍 (군) mean?", "military", ["flow", "help", "cooperate"], "국군."), M("What does the syllable 流 (류) mean?", "flow", ["military", "help", "cooperate"], "유입."), M("What does the syllable 助 (조) mean?", "help; assistant", ["military", "flow", "cooperate"], "원조."), M("What does the syllable 協 (협) mean?", "cooperate", ["military", "flow", "help"], "협조."),
           M("Which word is the opposite of 유입?", "유출", ["유실", "유행", "유창"], "Outflow."), M("Which word is the opposite of 협조?", "비협조", ["협력", "협소", "협의"], "Non-cooperation."), M("Which word is the opposite of 군인?", "민간인", ["사병", "장교", "행군"], "A civilian."), M("Which word is the opposite of 교제?", "절교", ["교류", "교환", "외교"], "Severing a relationship."), M("Which word fits 유입, 유포, 유출?", "유통", ["유행", "원조", "조력"], "Distribution."), M("Which word fits 조수, 조연, 조교?", "조력", ["유행", "원조", "조언"], "Help."), M("Which word fits 충고, 도움말, 격려의 말?", "조언", ["유행", "원조", "유통"], "Advice."),
           F("남북한은 경제 ___를 늘리기로 했습니다. (exchange)", "교류", ["절교", "행군"], "교류."), F("한반도가 ___된 지 벌써 오래되었습니다. (divided)", "분단", ["교류", "원조"], "분단."), F("두 나라는 ___을 열어 문제를 논의했습니다. (a meeting)", "회담", ["결핍", "식량"], "회담."), F("북한은 ___ 부족으로 어려움을 겪고 있습니다. (food)", "식량", ["회담", "친선"], "식량."), F("이웃 나라가 ___를 보내 주었습니다. (aid)", "원조", ["분단", "군사"], "원조."),
           read_q("남북한은 경제 교류를 늘리기로 했습니다"), read_q("한반도는 분단되었습니다"), read_q("두 나라는 회담을 열었습니다"), read_q("식량 원조를 받았습니다"), read_q("군사분계선을 넘었습니다")]
    ),
)

# ================================================================== L2 Part 1
_UNI = [("휴전선 지역에 자연 생태 공원이 조성될 것이다.", "A natural eco park will be created in the armistice-line area."), ("남과 북의 군대가 전쟁을 하지 않고 평화롭게 살게 될 것이다.", "The armies of the South and the North will not fight a war and will live peacefully."), ("학문, 기술, 정보 등을 교환하며 함께 번영할 것이다.", "They will exchange learning, technology, information and so on and prosper together."), ("이산 가족이 만나 행복하게 함께 살 수 있을 것이다.", "Separated families will be able to meet and live together happily.")]
_JRN = [
    ("새해엔 금강산 길 다시 열리길.", "May the road to Mount Kumgang open again in the new year."),
    ("연말 맞은 강원 고성군 주민들의 걱정과 기대.", "The worries and hopes of the residents of Goseong County, Gangwon Province, as the year ends."),
    ("서울에서 차로 세 시간 남짓 달려 설악산 미시령을 넘으니 차창 오른편으로 검푸른 바다가 펼쳐졌다.", "After driving a little over three hours from Seoul and crossing Misiryeong in Mount Seorak, the dark blue sea spread out on the right side of the car window."),
    ("속초, 간성, 거진을 거치고 남한 최북단 해수욕장인 화진포를 지나 현내면에 도착할 때쯤엔 도로를 달리는 차들이 거의 없었다.", "By the time I passed through Sokcho, Ganseong and Geojin, went by Hwajinpo, the northernmost beach in South Korea, and arrived at Hyeonnae-myeon, there were almost no cars running on the road."),
    ("택시 운전사 한진섭 (쉰두 살) 씨는 “여름엔 물놀이를 하러 오는 사람들이라도 있지만 추울 때는 정말 조용한 곳”이라며 “통일전망대에서 금강산 설경이라도 구경하고 가시라”고 권했다.", "Taxi driver Han Jin-seop (52) said, “In summer there are at least people who come to play in the water, but when it is cold it is a really quiet place,” and recommended, “At least look at the snowy scenery of Mount Kumgang from the Unification Observatory before you go.”"),
    ("통일전망대로 가기 위해 들른 출입 신고소는 한산했다.", "The entry report office I stopped at to go to the Unification Observatory was quiet."),
    ("신고소 관계자는 “하루 평균 천 명 정도가 전망대를 찾았는데 칠 월 이후로는 육백 명에서 칠백 명대로 줄어들었다”고 설명했다.", "An official of the report office explained, “On average about 1,000 people visited the observatory a day, but since July it has fallen to the 600 to 700 range.”"),
    ("출입증을 받고 십여 분 후 전망대에 도착했다.", "After receiving an entry pass, I arrived at the observatory about ten minutes later."),
    ("정상에서 망원경으로 맞은편을 바라보던 고 모 (일흔두 살) 씨는 “금강산 참 아름답다”를 되뇌었다.", "Mr. Ko (72), who was looking at the opposite side through a telescope at the top, kept repeating, “Mount Kumgang is truly beautiful.”"),
    ("고향이 함경도라는 그는 관광 개시 초기에 한 번 금강산에 다녀온 적이 있다고 했다.", "He, whose hometown is Hamgyeong Province, said that he had been to Mount Kumgang once in the early days of the tours."),
    ("그때는 부부가 함께였다.", "At that time the couple was together."),
    ("그는 “아내가 세상을 떠나고 지난 칠 월 다시 금강산 관광을 예약했는데 취소됐다”며 아쉬워했다.", "He said regretfully, “After my wife passed away, I booked a Mount Kumgang tour again last July, but it was canceled.”"),
    ("전망대에서 나와 현내면으로 가는 길.", "The road from the observatory to Hyeonnae-myeon."),
    ("도로변 곳곳에 식당과 상점 십여 곳이 눈에 띄었다.", "About ten restaurants and shops were visible here and there along the road."),
    ("모두 휴업했거나 아예 문을 닫은 상태였다.", "All of them were closed temporarily or had shut down altogether."),
    ("금강산 콘도 역시 매출의 삼십 퍼센트 이상을 차지하던 금강산 관광객들의 발길이 끊어지면서 이백이십오 개의 객실 중 절반가량이 비었다.", "The Mount Kumgang condominium, too, has about half of its 225 rooms empty, as the footsteps of the Mount Kumgang tourists, who accounted for more than 30 percent of its sales, have stopped."),
]
_LEFT = [("금강산 관광객 피격사건 등으로 금강산 관광이 중단된 지 어느덧 육 개월이다.", "It has already been six months since the Mount Kumgang tours were stopped because of incidents such as the shooting of a Mount Kumgang tourist."), ("강원도 고성군은 이로 인해 지역경제에 적지 않은 타격을 입고 있다.", "Goseong County in Gangwon Province is suffering no small blow to its regional economy because of this."), ("이곳 주민들의 새해 소원은 막혔던 길이 다시 열려 남북관계가 회복되고 자신들의 삶이 희망을 되찾는 것이다.", "The new-year wish of the residents here is that the blocked road open again, inter-Korean relations recover and their lives regain hope.")]
_SPEAK21 = [("한반도가 통일되면 남북한 국민들의 생활에 어떤 변화가 생길지 이야기해 보세요.", "Talk about what changes will occur in the lives of the people of South and North Korea if the Korean peninsula is unified."), ("한반도의 통일에 대해 주변 국가들, 특히 중국, 일본, 러시아, 미국은 어떤 입장일지 이야기해 보세요.", "Talk about what position the surrounding countries, especially China, Japan, Russia and the United States, would take on the unification of the Korean peninsula.")]
L2 = lesson(
    "U15 L8 · Part 1 (도입 학습): inter-Korean relations, Mount Kumgang, a travel journal",
    "도입 학습 · 알아봅시다 · 햇볕정책 · 금강산 관광 · 통일 · 이산가족 · 통일전망대 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 1: inter-Korean relations in the 2000s (남북 관계) — the book’s note",
             "South Korea’s policy toward North Korea in the new millennium has swung from liberalism (pro-NK) to conservatism (anti-NK). 햇볕정책, or the Sunshine Policy, used to be the overarching slogan for South Korea’s administrations under Kim Dae-Jung and Roh Moo-Hyun. The term “sunshine” was adopted from Aesop’s well-known fable (the North Wind and the Sun) in which sunshine proved more effective than a strong wind in ridding a traveler (NK) of a coat. Kim Dae-Jung was awarded the Nobel Peace Prize in 2000 for his initiation of the Sunshine Policy. The two former presidents had historic summit meetings (남북 정상회담) with North Korea’s leader Kim Jung-Il in Pyoungyang, in June 2000 and in October 2007, respectively. In the meantime, tension between the two Koreas relaxed; they discussed economy, culture, sports, the reunion of separated families (남북 이산가족 상봉), etc. The success of 개성공업지구 was a result of combining South Korea’s capital and technology with North Korea’s labor."),
        card("알아봅시다 2: 금강산 관광 — the book’s note",
             "금강산 is located on the east coast of North Korea, only 30 miles north of the DMZ. 금강산 is well known for its year-round beauty. In 1998, South Korean tourists visited 금강산 via cruise ship for the first time since the partition of the Korean peninsula. This was made possible by Hyundai, a South Korean conglomerate, in cooperation and with support from the South Korean government. In 2003, the land route opened and South Koreans were accommodated with varied tour packages. According to Hyundai’s tally, a million South Koreans visited 금강산 by June 2005. This tourism was not without issues, most of which were caused by inter-Korean politics, and the occasional detention of individual tourists by North Korea. On July 11, 2008, a South Korean tourist was shot to death by North Korean soldiers when she inadvertently crossed over into the military area near a resort beach. This incident, along with the increased tensions on the peninsula, stopped 금강산 관광 for an extended period."),
        card("학습활동 1 (Listening · Reading): “If North and South Korea are unified” (남북한이 통일이 되면)",
             "The pictures express Korean students’ ideas under the title “남북한이 통일이 되면” (© edunet4u.net). The book asks you to match four spoken descriptions with the four illustrations (A–D), and then to read the four written descriptions and write the letter of the matching illustration. The illustrations are pictures and are not in the text, so the letters cannot be given here. The four written descriptions (the English is mine):",
             examples=passage(_UNI)),
        card("학습활동 2 (Reading): a newspaper travel journal, “새해엔 금강산 길 다시 열리길”",
             "Read the newspaper travel journal (© The Naeil News). The text is the book’s with the numbers spelled out (3시간 is 세 시간; 52 is 쉰두 살; 1000명 is 천 명; 7월 is 칠 월; 600~700명대 is 육백 명에서 칠백 명대; 10여 분 is 십여 분; 72 is 일흔두 살; 10여 곳 is 십여 곳; 30% is 삼십 퍼센트; 225개 is 이백이십오 개); the bullets are removed. The English is mine.",
             examples=passage(_JRN)),
        card("학습활동 2: the questions answered (mine)",
             "3. What can be inferred from the title is A: the tour has been stopped (the title wishes that the road be opened again).\n\n"
             "4. The portions that give clues: 신고소는 한산했다; 칠 월 이후로는 육백 명에서 칠백 명대로 줄어들었다; 지난 칠 월 다시 금강산 관광을 예약했는데 취소됐다; 식당과 상점 십여 곳 … 모두 휴업했거나 아예 문을 닫은 상태였다; 금강산 관광객들의 발길이 끊어지면서 … 절반가량이 비었다.\n\n"
             "5. The left-out passage (below) fits best at the very beginning of the journal, before the first bulleted paragraph, as the introduction that states the situation (the tours stopped for six months and the residents’ wish), which the bulleted paragraphs then illustrate.",
             examples=passage(_LEFT)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK21)),
        card("Activities left out", "학습활동 1, questions 1 (four spoken descriptions matched with illustrations), 학습활동 2, question 1 (an edunet4u.net audio clip on 금강산 관광: a table of the year tourism began, the specific type of tourists mentioned and who made it possible) and 학습활동 3 (a KBS video on North Korea’s animation industry: an example of cooperation between North and South Korea, North Korea’s animation technology and a unique characteristic of the animation broadcast in North Korea) are audio, video and picture activities."),
    ],
    exercises=uniq(
        _tr(_UNI, k=3) + _tr(_JRN, k=3) + _tr(_LEFT, k=2) + _tr(_SPEAK21, k=2)
        + [M("What is the Sunshine Policy?", "햇볕정책, South Korea’s engagement policy toward North Korea", ["A weather forecast", "A trade agreement", "A tourism company"], "The book’s note."), M("Who won the Nobel Peace Prize in 2000 for the Sunshine Policy?", "Kim Dae-Jung", ["Roh Moo-Hyun", "Kim Jung-Il", "Park Chung-Hee"], "The book’s note."), M("When did the two summit meetings take place?", "June 2000 and October 2007", ["1998 and 2003", "2008 and 2009", "1988 and 1995"], "The book’s note."), M("Where is 금강산 located?", "On the east coast of North Korea", ["In Seoul", "On Jeju Island", "In China"], "The book’s note."), M("How did South Korean tourists first visit 금강산 in 1998?", "By cruise ship", ["By train", "By plane", "By car"], "The book’s note."), M("Who made the 금강산 tours possible?", "Hyundai, with the South Korean government’s support", ["The United Nations", "A Chinese company", "The Red Cross"], "The book’s note."), M("What stopped the 금강산 tours in July 2008?", "A South Korean tourist was shot by North Korean soldiers", ["A typhoon", "A fire", "A strike"], "The book’s note."), M("How long did the road trip from Seoul take?", "A little over three hours", ["Twenty minutes", "Ten hours", "A day"], "세 시간 남짓."), M("What is the title of the journal wishing for?", "That the road to 금강산 open again", ["That the road be closed", "That tourists stay away", "That the sea be calm"], "새해엔 금강산 길 다시 열리길."), M("What did the old man from Hamgyeong Province repeat?", "금강산 is truly beautiful", ["The road is long", "It is cold", "I am hungry"], "금강산 참 아름답다."), M("How many of the condominium’s 225 rooms were empty?", "About half", ["None", "All", "A tenth"], "절반가량."),
           F("출입 신고소는 ___했다. (was quiet)", "한산", ["숭고", "정중"], "한산하다."), F("그는 같은 말을 계속 ___. (repeated)", "되뇌었다", ["거쳤다", "맺었다"], "되뇌다."), F("관광객들의 ___이 끊어졌다. (footsteps)", "발길", ["손길", "눈길"], "발길이 끊어지다."), F("속초, 간성, 거진을 ___ 화진포를 지났다. (passed through)", "거치고", ["되뇌고", "다지고"], "거치다."), F("금강산 관광이 중단된 지 ___ 육 개월이다. (before one realizes)", "어느덧", ["번번이", "누누이"], "어느덧."),
           read_q("새해엔 금강산 길이 다시 열리길 바랍니다"), read_q("통일전망대에서 금강산 설경을 구경합니다"), read_q("관광객들의 발길이 끊어졌습니다"), read_q("남북한이 통일이 되면 평화롭게 살게 될 것입니다"), read_q("이산 가족이 만나 행복하게 살 수 있을 것입니다")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("~롭다", "The suffix 롭다 is a stative verb “maker” that works with a limited number of nouns ending in vowels such as 자유, 평화, 향기, or 명예.", "자유롭다, 평화롭다, 향기롭다, 명예롭다"),
        ("~을/를 바탕으로", "based on; founded on", "설문조사 결과를 바탕으로 새로운 계획을 세웠다.", "~을/를 토대로"),
        ("생태공원", "(生態公園) an “eco park”", "", "자연공원, 동물원, 식물원"),
        ("왕래(하다)", "(往來) coming and going (to come and go; to go around)", "이곳은 사람들의 왕래가 많습니다.", "오고 가다, 오가다 | 다니다"),
        ("이산 가족", "(離散 家族) separated families (especially between North and South Korea)", "천구백팔십오 년부터 이천구 년까지 십칠 차례의 남북 이산 가족 상봉이 있었다."),
        ("자원", "(資源) (natural) resources", "북한은 천연 자원이 많습니다.", "자원 (自願) volunteering"),
        ("제작(하다/되다)", "(製作) manufacturing (to make; to manufacture/to be made; to be manufactured)", "저는 영화 제작하는 일을 하고 싶어요.", "만들다"),
        ("조성(하다/되다)", "(造成) creation; making; construction; establishment (to create; to establish/to be created; to be established)", "주택난 해소를 위해 아파트 단지를 조성하기로 했습니다."),
        ("평화(롭다)", "(平和) peace (to be peaceful)", "저는 시골에서 조용히 평화롭게 살고 싶어요."),
        ("학문", "(學問) a study; studies; academics; scholarship; “learning and asking”", "저는 학문을 연구하는 것이 즐겁습니다.", "공부"),
    ]),
    ("학습활동 2", [
        ("~ 남짓", "a little bit over; upward of", "결혼식 피로연에 오십 명 남짓의 손님이 왔습니다."),
        ("객실", "(客室) a guest room (at a hotel, motel, etc.)", "이 호텔에 객실이 몇 개나 됩니까?"),
        ("거치다", "to pass through; to go by way of", "미국에서 한국으로 갈 때 일본을 거치는 비행편도 있습니다.", "경유하다"),
        ("결실을 맺다", "(結實) to bear fruit", "여러분, 졸업시험에서 좋은 결실을 맺기 바랍니다.", "열매를 맺다, 성공하다"),
        ("되뇌다", "to repeat verbally; to echo", "그 사람은 같은 말을 계속 되뇌고 있습니다."),
        ("민간 교류", "(民間 交流) exchanges via civilians (especially between North and South Korea)", "정부는 민간 교류를 활성화시키기로 했습니다."),
        ("발길이 끊어지다", "to no longer frequent; not to have visitors; “footsteps disconnected”", "그 식당은 불친절해서 손님들의 발길이 끊어졌습니다."),
        ("방북(하다)", "(放北) visiting North Korea (to visit North Korea)", "김 대통령이 방북을 해 남북 정상회담을 했습니다.", "방한하다, 탈북하다"),
        ("분단(하다/되다)", "(分斷) division (especially within a nation) (to divide/to be divided)", "한반도가 분단된 지 벌써 육십오 년이 지났습니다."),
        ("설경", "(雪景) a snowy scene", "뉴질랜드 설경이 아주 아름답습니다."),
        ("실향민", "(失鄕民) people who have lost their hometown (in a war or disaster); “people who have lost hometown”", "실향민들의 소원은 고향을 한 번 가 보는 것입니다."),
        ("어느덧", "before one realizes; without one’s knowledge", "얼마 전 새해가 시작한 것 같은데, 어느덧 연말이 되었네요.", "어느새"),
        ("의정서", "(議定書) a letter of intent; protocol", "도쿄 의정서"),
        ("일반인", "(一般人) ordinary people; the general public", "이곳 회의장에는 기자들만 출입할 수 있고, 일반인은 들어갈 수 없습니다."),
        ("장", "(章) a chapter; (figuratively) an era", "아폴로 우주선의 달 착륙으로 우주시대의 새로운 장이 열렸다."),
        ("전망대", "(展望臺) an observatory; an observation tower", "전망대에 올라가서 야경을 보고 싶어요."),
        ("체결(하다/되다)", "(締結) signing (an agreement, a contract, etc.) (to sign/to be signed)", "계약이 체결되었어요."),
        ("피격", "(被擊) being attacked; being shot; suffering attack", "이라크에서 장갑차가 테러범의 피격을 받았습니다.", "공격, 사격"),
        ("한산하다", "(閑散) to be inactive; to be quiet; few people around", "크리스마스에는 대학 캠퍼스가 한산하고 학생들도 많이 보이지 않습니다."),
        ("햇볕정책", "(政策) Sunshine Policy (Refer to 알아봅시다.)", ""),
    ]),
    ("학습활동 3", [
        ("곤충", "(昆蟲) an insect; insects in general", "", "벌레"),
        ("단물", "syrup; “sweet water”", ""),
        ("도덕적", "(道德的) moral", "왜 많은 사람들은 도덕적으로 행동하지 못할까요?", "윤리적"),
        ("독침", "(毒針) a poisonous sting; a poisoned needle; a poisoned dart", ""),
        ("만화", "(漫畵) a cartoon; a comic strip; manga", "우리 아이가 매일 만화책만 봅니다."),
        ("벙어리", "a nonverbal person; a person who is not able to speak", "왜 갑자기 벙어리처럼 말이 없어요?", "장님, 귀머거리"),
        ("선입관", "(先入觀) prejudice; “before established view”", "장애인에 대해 선입관을 갖지 말고 열린 마음으로 대해 주세요.", "선입견"),
        ("세분화(하다/되다)", "(細分化) breaking down; subdividing; segmentation (to break down; to subdivide; to segment/to be subdivided; to be segmented)", "등급을 세분화하다."),
        ("손색이 없다", "(遜色) not to be inferior; to be comparable to", "이 골프채는 값이 싸지만 고급 브랜드와 비교해도 전혀 손색이 없습니다."),
        ("정치 선전", "(政治 宣傳) political propaganda", "북한 당국은 그 사람을 정치 선전에 이용하고 있어요."),
        ("캐릭터", "a character; a personality; a characteristic; “character”", "그 영화의 캐릭터가 독특하고 재미있어요."),
    ]),
]
L3 = lesson(
    "U15 L8 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 롭다 · 왕래 · 이산 가족 · 조성 · 평화 · 학문 · 거치다 · 되뇌다 · 분단 · 설경 · 실향민 · 전망대 · 체결 · 피격 · 한산하다 · 만화 · 선입관",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 1985년부터 2009년까지 17차례 → 천구백팔십오 년부터 이천구 년까지 십칠 차례; 50명 → 오십 명; 65년 → 육십오 년. For 곤충 the book gives the same word again with the meaning “insects in general.” The book’s 3rd-activity list has 세분화(하다/ 되다) broken over two lines; it is closed up here.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=22, nread=16)),
)

# ================================================================== L4 Part 2 texts
_EN615 = [
    "In accordance with the noble will of the whole nation, which wishes for the peaceful unification of the fatherland, President Kim Dae-jung of the Republic of Korea and Chairman Kim Jong-il of the National Defense Commission of the Democratic People’s Republic of Korea held a historic meeting in Pyongyang from June 13 to June 15, 2000, and held a summit meeting.",
    "The leaders of the South and the North appraised that this meeting and talks, held for the first time in the history of the division, have great significance in promoting mutual understanding, developing South-North relations and realizing peaceful unification, and declare as follows.",
    "1. The South and the North agreed to solve the problem of the country’s unification independently, by joining forces, among our own people, who are its masters.",
    "2. The South and the North recognized that the South’s proposal for a union and the North’s proposal for a low-level federation for the country’s unification have elements in common, and agreed to work toward unification in this direction from now on.",
    "3. The South and the North agreed to exchange visiting groups of separated families and relatives on the occasion of this year’s August 15 and to promptly resolve humanitarian issues, such as the problem of unconverted long-term prisoners.",
    "4. The South and the North agreed to develop the national economy in a balanced way through economic cooperation, and to activate cooperation and exchange in various fields such as society, culture, sports, health and the environment, and thereby build mutual trust.",
    "5. The South and the North agreed to hold talks between the authorities in the near future in order to put the above agreements into practice promptly.",
    "President Kim Dae-jung courteously invited Chairman Kim Jong-il to visit Seoul, and Chairman Kim Jong-il agreed to visit Seoul at an appropriate time in the future.",
]
_S615 = ["조국의 평화적 통일을 염원하는 온 겨레의 숭고한 뜻에 따라 대한민국 김대중 대통령과 조선민주주의인민공화국 김정일 국방위원장은 이천 년 유월 십삼 일부터 유월 십오 일까지 평양에서 역사적인 상봉을 하였으며 정상회담을 가졌다.",
         "남북정상들은 분단 역사상 처음으로 열린 이번 상봉과 회담이 서로 이해를 증진시키고 남북관계를 발전시키며 평화통일을 실현하는 데 중대한 의의를 가진다고 평가하고 다음과 같이 선언한다.",
         "남과 북은 나라의 통일문제를 그 주인인 우리 민족끼리 서로 힘을 합쳐 자주적으로 해결해 나가기로 하였다.",
         "남과 북은 나라의 통일을 위한 남측의 연합제 안과 북측의 낮은 단계의 연방제 안이 서로 공통성이 있다고 인정하고 앞으로 이 방향에서 통일을 지향시켜 나가기로 하였다.",
         "남과 북은 올해 팔 일오에 즈음하여 흩어진 가족, 친척방문단을 교환하며 비전향 장기수 문제를 해결하는 등 인도적 문제를 조속히 풀어 나가기로 하였다.",
         "남과 북은 경제협력을 통하여 민족경제를 균형적으로 발전시키고 사회, 문화, 체육, 보건, 환경 등 제반 분야의 협력과 교류를 활성화하여 서로의 신뢰를 다져 나가기로 하였다.",
         "남과 북은 이상과 같은 합의사항을 조속히 실천에 옮기기 위하여 빠른 시일안에 당국 사이의 대화를 개최하기로 하였다.",
         "김대중 대통령은 김정일 국방위원장이 서울을 방문하도록 정중히 초청하였으며, 김정일 국방위원장은 앞으로 적절한 시기에 서울을 방문하기로 하였다."]
_N615 = ["조국의 평화적통일을 념원하는 온 겨레의 숭고한 뜻에 따라 조선민주주의인민공화국 김정일국방위원장과 대한민국 김대중대통령은 이천 년 유월 십삼 일부터 유월 십오 일까지 평양에서 력사적인 상봉을 하였으며 최고위급회담을 가지였다.",
         "북남수뇌들은 분단력사상 처음으로 열린 이번 상봉과 회담이 서로 리해를 증진시키고 북남관계를 발전시키며 평화통일을 실현하는 데서 사변적인 의의를 가진다고 평가하고 다음과 같이 선언한다.",
         "북과 남은 나라의 통일문제를 그 주인인 우리 민족끼리 서로 힘을 합쳐 자주적으로 해결해 나가기로 하였다.",
         "북과 남은 나라의 통일을 위한 북측의 낮은 단계의 련방제 안과 남측의 련합제 안이 서로 공통성이 있다고 인정하고 앞으로 이 방향에서 통일을 지향시켜 나가기로 하였다.",
         "북과 남은 올해 팔 일오에 즈음하여 흩어진 가족, 친척방문단을 교환하며 비전향 장기수 문제를 해결하는 등 인도적 문제를 조속히 풀어 나가기로 하였다.",
         "북과 남은 경제협력을 통하여 민족경제를 균형적으로 발전시키고 사회, 문화, 체육, 보건, 환경 등 제반분야의 협력과 교류를 활성화하여 서로의 신뢰를 다져 나가기로 하였다.",
         "북과 남은 이상과 같은 합의사항을 조속히 실천에 옮기기 위하여 빠른 시일안에 당국사이의 대화를 개최하기로 하였다.",
         "김대중대통령은 김정일국방위원장께서 서울을 방문하시도록 정중히 초청하였으며 김정일국방위원장께서는 앞으로 적절한 시기에 서울을 방문하기로 하였다."]
_P615S = list(zip(_S615, _EN615))
_P615N = list(zip(_N615, _EN615))
_CMP = [
    ("Spelling", "염원하는", "념원하는", "to wish"),
    ("Spelling", "역사적인, 역사상", "력사적인, 분단력사상", "historic; in history"),
    ("Spelling", "가졌다", "가지였다", "had"),
    ("Spelling", "이해", "리해", "understanding"),
    ("Spelling", "연방제", "련방제", "confederation (difference in the initial consonant restriction)"),
    ("Spelling", "연합제", "련합제", "union (difference in the initial consonant restriction)"),
    ("Spacing", "평화적 통일, 제반 분야, 당국 사이", "평화적통일, 제반분야, 당국사이", "peaceful unification; various fields; between the authorities (the North text closes up the spaces)"),
    ("Vocabulary", "남북", "북남", "South and North; the two Koreas"),
    ("Vocabulary", "남과 북은", "북과 남은", "the South and the North (the North names itself first)"),
    ("Vocabulary", "정상회담", "최고위급회담", "a summit meeting"),
    ("Vocabulary", "남북정상", "북남수뇌", "the leaders of the two Koreas"),
    ("Vocabulary", "중대한", "사변적인", "significant; epoch-making"),
    ("Markers and honorifics", "김정일 국방위원장이, 김정일 국방위원장은", "김정일국방위원장께서, 김정일국방위원장께서는", "the book notes: extreme use of honorifics; idolization of dictators"),
    ("Markers and honorifics", "방문하도록", "방문하시도록", "to visit (the North text adds the honorific 시 for its leader)"),
    ("Order of names", "대한민국 김대중 대통령과 조선민주주의인민공화국 김정일 국방위원장", "조선민주주의인민공화국 김정일국방위원장과 대한민국 김대중대통령", "each text puts its own side’s leader first"),
]
_SPEAK22 = [("한국은 북한에게 여러 가지 방법으로 경제적 도움을 제공해 왔습니다.", "South Korea has provided North Korea with economic help in various ways."), ("한국의 대북 경제 지원이 어떤 효과가 있다고 생각하는지 서로 이야기해 보세요.", "Talk to each other about what effect you think South Korea’s economic aid to North Korea has.")]
L4 = lesson(
    "U15 L8 · Part 2 (본 학습): the June 15 Joint Declaration, South and North texts",
    "본 학습 · 두음법칙 · 6·15 남북공동선언문 · 북남 공동 선언 · 북한 말 · 철자 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: the rules for initial consonant restrictions in North Korean (두음법칙) — the book’s note",
             "Recall that Sino-Korean syllables beginning with the initial consonants ㄹ or ㄴ have different pronunciations depending on their position; e.g., 력/역 for 力 (power), as in 체력 vs. 역도; 녀/여 for 女 (female), as in 남녀 vs. 여자.\n\n"
             "The consonant sound /n/ is not used as the initial sound of a word when it is followed by vowels like ㅕ, ㅑ, ㅛ, and ㅠ. This is known as 두음법칙 (initial consonant restriction; “head sound rule”). The South Korean language is faithful to this restriction, whereas the North Korean language standardized the spelling in accordance with the original Chinese sounds /l, r/, and /n/.\n\n"
             "The book lets you click on three Sino-Korean words to hear how North Koreans pronounce them: 노동, 역사 and 여성 (in the North they are said 로동, 력사 and 녀성)."),
        card("학습활동 2 (Reading): the June 15 Joint Declaration — the South Korean text",
             "The book gives the declaration of June 15, 2000 (the South Korean text on the left and the North Korean text on the right) and asks you to compare them. The title is 남북 공동 선언. Digits are spelled out here (2000년 6월 13일 is 이천 년 유월 십삼 일; 6월 15일 is 유월 십오 일; 8•15 is 팔 일오). The text ends with the date 2000년 6월 15일 (이천 년 유월 십오 일) and the signatures of 대한민국 대통령 김대중 and 조선민주주의인민공화국 국방위원장 김정일. The English is mine (it is the same for both texts, which differ only in spelling, vocabulary and honorifics).",
             examples=passage(_P615S)),
        card("학습활동 2: the North Korean text",
             "The title of the North Korean text is 북남 공동 선언; it is signed by 조선민주주의인민공화국 국방위원장 김정일 and 대한민국 대통령 김대중, listed in the opposite order (the North’s leader first). The text is as printed in the book (with the North’s spelling and spacing), with the digits spelled out:",
             examples=passage(_P615N)),
        card("학습활동 2: the Comparison Chart (my answers)",
             "The book asks you to circle all the differences and to complete the chart’s third and fourth columns (the first rows are done for you in the book: 염원하는/념원하는 “to wish”; 역사적인/력사적인 “historic”; 가졌다 “had”; 연방제 vs. 연합제, “confederation vs. union”; 남북/북남 “South and North/two Koreas”; 정상회담 “a summit meeting”; and the honorific markers “extreme use of honorifics; idolization of dictators”). My full chart:",
             tables=[table(["Type", "South Korean", "North Korean", "English meaning"], [list(r) for r in _CMP], say=[1, 2])]),
        card("학습활동 2: question 3 (translation)",
             "The book asks you to translate two underlined paragraphs of the text into English (the underlines are not visible in the text). Every sentence of the declaration is translated above."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK22)),
        card("Activities left out", "학습활동 1 (four edunet4u.net audio clips on cooperation and exchange between North and South Korea; you match each with a picture and summarize it in English) and 학습활동 3 (a KBS video of part of President Roh’s report to the nation on the October 4, 2007 summit: his general opinion of economic cooperation, his opinion of past attempts and what he emphasized at the summit) are audio and video activities."),
    ],
    exercises=uniq(
        _tr(_P615S, k=3) + _tr(_SPEAK22, k=2)
        + [M("In what year was the June 15 Joint Declaration made?", "2000", ["1998", "2007", "1988"], "이천 년."), M("Where did the two leaders meet?", "Pyongyang", ["Seoul", "Panmunjom", "Beijing"], "평양."), M("What does the declaration say about solving unification?", "It should be solved independently by the Korean people themselves", ["It should be left to other countries", "It should be postponed", "It is impossible"], "우리 민족끼리 자주적으로."), M("What do the South’s union proposal and the North’s federation proposal share?", "Elements in common", ["Nothing", "The same name", "A date"], "공통성."), M("What humanitarian issue is mentioned for August 15?", "Exchanging visits of separated families and the unconverted long-term prisoners problem", ["A trade dispute", "A sports exchange", "A tourism plan"], "흩어진 가족, 비전향 장기수 문제."), M("What did Kim Jong-il agree to do at an appropriate time?", "Visit Seoul", ["Visit Washington", "Visit Tokyo", "Resign"], "서울을 방문."), M("How does the North text say “South and North”?", "북남", ["남북", "동서", "남남"], "북남."), M("How does the North text say “summit meeting”?", "최고위급회담", ["정상회담", "공동회담", "수뇌부"], "최고위급회담."), M("How does the North text spell 역사적인?", "력사적인", ["역사적인", "녁사적인", "사력적인"], "력사적인."), M("How does the North text spell 이해?", "리해", ["이해", "니해", "해이"], "리해."), M("What is 두음법칙?", "The initial consonant restriction (the head sound rule)", ["A rule about word endings", "A rule about spacing", "A rule about honorifics"], "The book’s note."), M("Which Korean follows the initial consonant restriction?", "South Korean", ["North Korean", "Both", "Neither"], "The book’s note."), M("What is the North Korean text’s use of honorifics described as?", "Extreme; idolization of dictators", ["Absent", "Normal", "Humble"], "The book’s note."),
           F("남과 북은 나라의 통일문제를 ___으로 해결해 나가기로 하였다. (independently)", "자주적", ["일방적", "도덕적"], "자주적."), F("남과 북은 합의사항을 ___ 실천에 옮기기로 하였다. (promptly)", "조속히", ["진지하게", "정중히"], "조속히."), F("김대중 대통령은 김정일 국방위원장을 ___ 초청하였다. (courteously)", "정중히", ["조속히", "한산히"], "정중히."), F("조국의 평화적 통일을 ___하는 온 겨레의 뜻이다. (wishing for)", "염원", ["거부", "체결"], "염원하다."), F("남과 북은 서로의 신뢰를 ___ 나가기로 하였다. (build up)", "다져", ["흩어져", "되뇌어"], "다지다."), F("이번 상봉과 회담은 ___한 의의를 가진다. (great)", "중대", ["숭고", "진지"], "중대하다."),
           read_q("남과 북은 힘을 합쳐 자주적으로 해결해 나가기로 하였습니다"), read_q("조국의 평화적 통일을 염원합니다"), read_q("김정일 국방위원장은 서울을 방문하기로 하였습니다"), read_q("한국의 대북 경제 지원이 어떤 효과가 있다고 생각합니까"), read_q("남북은 합의사항을 실천에 옮기기로 하였습니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("가족애", "(家族愛) love for family members; “family love”", "이 영화는 가족애를 잘 보여 주는 영화입니다."),
        ("개·폐회식", "(開·閉會式) the opening and closing of a ceremony", "제가 개회식에서 기념사를 읽기로 했어요."),
        ("개최(하다/되다)", "(開催) hosting/opening (a meeting, event, etc.) (to host/to be hosted)", "천구백팔십팔 년 서울에서 올림픽이 개최되었습니다.", "주최하다, 열다"),
        ("겨레", "a people", "남과 북, 우리는 한 겨레입니다."),
        ("단일 민족", "(單一 民族) the one and homogeneous race (referring to the Korean nation as a whole)", "한국은 오랫동안 단일 민족이었습니다."),
        ("단합(하다/되다)", "(團合) unity (to unite/to be united)", "우리 팀원들은 단합이 아주 잘 됩니다.", "단결"),
        ("북녘", "(北) the north; the northern area (normally referring to North Korea)", "우리 어머니는 북녘 땅을 바라 보시며 눈물을 흘리셨어요.", "북쪽, 북방"),
        ("상봉", "(相逢) a reunion (of long-separated people)", "반세기만에 이산가족이 상봉했습니다."),
        ("애타게 그리다", "to miss dearly", "이산가족들은 서로를 애타게 그리고 있습니다."),
        ("장벽", "(障壁) a barrier; an obstacle", "외국인 근로자들은 언어의 장벽이 높다고 얘기합니다."),
        ("직항로", "(直航路) a direct (nonstop) route between airports/seaports", "서울에서 북경까지 직항로가 있습니까?"),
        ("친선", "(親善) goodwill", "남북한 친선 축구 경기를 열기로 했어요.", "친목"),
        ("혈육", "(血肉) family and relatives; “flesh and blood”", "저는 제 남동생이 유일한 혈육입니다."),
        ("화해(하다)", "(和解) reconciliation; peaceful settlement (to reconcile)", "친구랑 싸웠지만 곧 화해했다."),
    ]),
    ("학습활동 2", [
        ("~에 즈음하여", "at the time of ~; on the occasion of ~", "추석에 즈음하여 선물을 사기 위해 백화점을 찾는 사람이 늘고 있다."),
        ("다지다", "to strengthen; to tighten; to commit oneself", "담배를 끊겠다는 결심을 다지고 또 다졌지만 실패하고 말았어요."),
        ("비전향 장기수", "(非轉向 長期囚) a “non-converted” long-term prisoner (referring to a North Korean prisoner, in a South Korean prison, who has not changed his ideology)", "", "미전향 장기수 | 양심수"),
        ("선언(하다)", "(宣言) proclamation (to proclaim; to announce publicly)", "천칠백칠십육 년 미국은 영국으로부터 독립을 선언했습니다."),
        ("숭고하다", "(崇高) to be noble; to be sublime", "소방관의 숭고한 희생으로 어린아이의 목숨을 구했습니다."),
        ("신뢰(하다)", "(信賴) trust (to trust; to believe)", "어린 아이들은 보통 부모의 말을 신뢰합니다."),
        ("실천에 옮기다", "(實踐) to put into practice", "참 좋은 계획이군요. 이제 실천에 옮겨 보세요."),
        ("염원(하다)", "(念願) a wish (to wish)", "저는 남북한의 통일을 염원합니다.", "소원하다, 바라다"),
        ("위원장", "(委員長) the commissioner; a chief of a committee", "김정일 국방위원장"),
        ("의의", "(意義) a significance; a cause; a meaning", "이번 회담의 의의는 새로운 출발이라는 점에서 찾을 수 있다.", "의미"),
        ("인도적", "(人道的) humanitarian", "대한 적십자사는 북한의 수해 난민들을 위해 인도적 구호품을 모으고 있다."),
        ("인정(하다/받다)", "(認定) acknowledgment (to acknowledge/to be acknowledged)", "이제 잘못을 인정하고 사과하세요.", "부인하다"),
        ("자주적", "(自主的) independent; self-reliant; autonomous", "학생들이 자주적으로 공부할 수 있도록 도와줍시다."),
        ("정상회담", "(頂上會談) a summit meeting", "한국의 대통령이 한미 정상회담을 위해 미국을 방문 중이다."),
        ("정중하다", "(鄭重) to be courteous; to be polite", "제 실수였습니다. 정중하게 사과하겠습니다."),
        ("제반 분야", "(諸般 分野) various areas; all relevant areas", "정부는 경제, 문화 등 제반 분야에서 남북한 협력을 도모하고 있습니다."),
        ("조국", "(祖國) one’s fatherland; a home country; “ancestor country”", "자기 조국을 사랑하지 않는 사람은 없다.", "모국"),
        ("조속히", "(早速) promptly; as soon as possible", "어머니께서 병원에 입원하셨어요. 조속히 병원으로 오세요."),
        ("중대하다", "(重大) to be greatly important", "이 문제는 아주 중대한 일입니다.", "중대 (中隊) a company"),
        ("지향(시키다)", "(指向) aspiration; direction (to aspire to; to direct)", "저희 회사는 항상 최고를 지향합니다."),
        ("합의사항", "(合意事項) an agreed-upon item/idea", "그럼 합의사항을 잘 지킵시다."),
        ("흩어지다", "to scatter; to spread/to be scattered", "우리 가족들은 전국에 흩어져 살고 있습니다."),
    ]),
    ("학습활동 3", [
        ("~에 임하다", "(臨) to face; to be confronted by", "인간은 죽음에 임하면 종교를 찾게 된다."),
        ("논의", "(論議) discussion; debate", "우리 이 문제의 대책에 대해 논의해 봅시다.", "토의, 토론, 의논"),
        ("누누이", "(累累) over and over (again); time and again. This adverb normally works with verbs such as 말하다 and 강조하다.", "누누이 말하지만 한국말은 매일 공부해야 돼."),
        ("마중(가다/오다/나가다)", "going/coming out to meet (a visitor); reception (to go/come/go out to meet)", "오늘 친구가 오기 때문에 공항으로 마중 나가야 합니다."),
        ("양측", "(兩側) both sides", "노사 양측이 전혀 양보를 하지 않고 있습니다.", "양방, 쌍방 | 일방"),
        ("일방", "(一方) (of) one side; one way", "그 사람은 화가 나서 일방적으로 전화를 끊어 버렸어요.", "한쪽 | 양방, 쌍방, 일방통행"),
        ("진지하다", "(眞摯) to be serious; to be earnest", "이번 회의에는 진지하게 임해 주시기 바랍니다.", "진지 (陣地) a (military) camp"),
        ("할애(하다)", "(割愛) sparing (time, energy, etc.); parting with (a thing) (to spare; to part with)", "성적이 떨어져서 공부에 시간을 좀 더 할애하기로 했다."),
    ]),
]
L5 = lesson(
    "U15 L8 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 겨레 · 단합 · 북녘 · 상봉 · 장벽 · 친선 · 혈육 · 화해 · 즈음하여 · 다지다 · 선언 · 숭고하다 · 신뢰 · 염원 · 의의 · 자주적 · 정상회담 · 정중하다 · 조국 · 조속히 · 양측 · 진지하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 1988년 → 천구백팔십팔 년; 1776년 → 천칠백칠십육 년. The Hanja of 실천에 옮기다 is printed as 實薦 in the book; the correct 實踐 is written here. The book writes 진지 (陣地) as the related word of 진지하다.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=24, nread=16)),
)

# ================================================================== L6 Part 3
_POEM = [("우리는 본디 하나", "We are originally one."), ("하지만 지금은", "But now"), ("인제 다시", "Now, again"), ("생각이 하나 되고", "our thoughts become one,"), ("하나의 말을 쓰고", "we use one language,"), ("하나 되고 싶은", "the one we want to become,"), ("우리의 간절한", "our earnest"), ("어서 빨리 이루고 싶습니다", "we want to achieve it quickly.")]
_NEG = [
    ("이날 오전 열한 시경 서해 북방한계선 (엔엘엘) 부근 대청도 동쪽 약 구 킬로미터 지점에서 한국 해군과 북한 해군 사이에서 전투가 발생했다.", "Around 11 a.m. on this day, a battle occurred between the South Korean navy and the North Korean navy at a point about 9 kilometers east of Daecheong Island, near the Northern Limit Line (NLL) in the West Sea."),
    ("발표에 따르면 북한의 경비정 한 척이 한국 해군의 경고방송에도 불구하고 북방한계선을 침범함에 따라 교전으로 이어졌다.", "According to the announcement, one North Korean patrol ship violated the Northern Limit Line despite the South Korean navy’s warning broadcast, which led to an exchange of fire."),
    ("한국 해군의 사격으로 북한 경비정은 크게 파손되었고 한국 해군은 함선 외벽에 약간의 파손을 당했다.", "Because of the South Korean navy’s fire, the North Korean patrol ship was badly damaged, and the South Korean navy suffered slight damage to the outer wall of its ship."),
    ("이번 서해 교전은 이천 년대에 두 차례의 연평 해전에 이어 세 번째로 발생한 것이다.", "This West Sea exchange of fire is the third to occur in the 2000s, following the two Yeonpyeong naval battles."),
    ("북한은 “육일오 공동선언과 십 사 공동선언에 대한 남조선 당국의 입장과 태도가 확인됐다”며 “일차적으로 군사분계선을 통한 육로 통행을 제한, 차단한다”고 한국에 통보했다.", "North Korea notified South Korea, saying, “The position and attitude of the south Korean authorities toward the June 15 and October 4 joint declarations have been confirmed,” and, “As a first step, we restrict and block overland passage through the Military Demarcation Line.”"),
    ("따라서 판문점을 통한 개성공단의 출입이 불가능하게 되었고, 이는 사실상 개성공단을 폐쇄하겠다는 북한의 의도로 해석된다.", "Accordingly, entry to the Gaesung Industrial Complex through Panmunjom became impossible, which is interpreted as North Korea’s intention to effectively close the Gaesung Industrial Complex."),
    ("이로써 지난 칠 월 일 일 북한이 금강산 관광객 박왕자 씨를 사살한 이후 계속 나빠지던 남북관계는 회복이 더욱 어렵게 되었다.", "With this, inter-Korean relations, which had been getting worse since North Korea shot to death the Mount Kumgang tourist Park Wang-ja on July 1, became even harder to restore."),
    ("북한이 핵실험을 강행했다.", "North Korea went ahead with a nuclear test."),
    ("지난 이천일 년에 지하 핵실험을 한 후 이번이 두 번째다.", "It is the second since the underground nuclear test last conducted in 2001."),
    ("이번 핵실험의 목적은 금년 출범한 미국 오바마 정부와 협상을 위한 메시지를 국제사회에 전하려는 의도가 있는 것으로 보인다.", "The purpose of this nuclear test appears to be an intention to convey to the international community a message for negotiations with the American Obama administration launched this year."),
    ("지진파 조사 결과 이번 핵실험 장소는 함경북도 길주군 북쪽에 있는 만탑산 근처의 지하인 것으로 밝혀졌다.", "As a result of examining the seismic waves, the site of this nuclear test turned out to be underground near Mantap Mountain, north of Gilju County in North Hamgyeong Province."),
]
_ANS8 = [("서해 교전 (대청도 근처)", "2009년 11월 10일", "my answer: the Daecheong naval clash"), ("육로 통행 제한 통보", "2008년 12월 1일", "my answer: the border-crossing restriction notice"), ("두 번째 핵실험", "2009년 5월 25일", "my answer: the second nuclear test")]
_SPEAK23 = [("최근에 나온 북한 관련 뉴스에 대해 발표하고 서로 이야기해 보세요.", "Give a presentation on recent news related to North Korea and talk to each other.")]
L6 = lesson(
    "U15 L8 · Part 3 (심화 학습): a children’s poem and inter-Korean incidents of the 2000s",
    "심화 학습 · 동시 · 우리는 본디 하나 · 2000년대 남북관계 · 서해 교전 · 개성공단 · 핵실험 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Listening · Reading): a children’s poem, “우리는 본디 하나”",
             "The book gives a children’s poem recorded in audio (© edunet4u.net). You listen and transcribe the missing words (there are fourteen blanks, such as 도 하나 and 을 가르고), then translate the poem. The missing words are heard only in the audio and are not in the text, so I cannot give them. The lines that are printed in full (the English is mine):",
             examples=passage(_POEM)),
        card("학습활동 1: question 2 (my answer)", "In the poem, 우리 refers to the Korean people, North and South together: the Korean nation that was originally one and has been divided."),
        card("학습활동 3 (Reading): a summary of inter-Korean relations in the 2000s",
             "The book gives a chronology (Text and images © Hankyoreh) that includes positive and negative developments and asks you to list the negative incidents with their dates in English (the first, “2002 June 29: 2nd occurrence of exchange of fire in the West Sea (Yeon-pyong warfare),” is done for you). The chronology is a picture and is not in the text, so the list cannot be given here. The three summaries below are in the text, and the book asks you to fill in the dates of the incidents they describe. The text is the book’s with the numbers spelled out (11시 is 열한 시; 9 km is 구 킬로미터; NLL is 엔엘엘; 6.15 is 육일오; 10.4 is 십 사; 7월 1일 is 칠 월 일 일; 2001년 is 이천일 년); the book’s quotation marks are completed. The English is mine.",
             examples=passage(_NEG)),
        card("학습활동 3: the dates (my answers, from my own knowledge)",
             "The dates are not given in the text. From my own knowledge of the events (not from the book), the incidents are: the West Sea clash near Daecheong Island (November 10, 2009); North Korea’s notice restricting overland passage through the Military Demarcation Line (December 1, 2008); and North Korea’s second nuclear test (May 25, 2009). Two details in the book’s text differ from what the book says elsewhere: the book’s note in 알아봅시다 gives July 11, 2008 for the shooting of the tourist (the summary says 7월 1일), and the summary says the earlier underground test was in 2001 (the first North Korean underground nuclear test was in 2006). Please check the dates against your teacher’s key.",
             tables=[table(["Incident", "Date (my answer)", "Note"], [list(r) for r in _ANS8])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK23)),
        card("Activities left out", "학습활동 2 (two Seoul Education Research & Information Institute radio clips about reconciliation and cooperation: choose the common theme and give detailed examples) and 학습활동 4 (a North Korean broadcast video of a ceremony from 서평방송: identify the occasion and the person the speaker gives credit to, with the linguistic clues) are audio and video activities."),
    ],
    exercises=uniq(
        _tr(_POEM, k=3) + _tr(_NEG, k=3)
        + [M("What does 우리 in the poem refer to?", "The Korean people, North and South together", ["Only South Koreans", "Only students", "Two companies"], "The nation that was one."), M("What does the poem say we were originally?", "One", ["Two", "Many", "Enemies"], "우리는 본디 하나."), M("Where did the first clash in the summaries occur?", "Near Daecheong Island by the Northern Limit Line", ["In Seoul", "At Panmunjom", "In the Yellow Sea only"], "서해 북방한계선 부근 대청도."), M("Why did the North Korean patrol ship cause an exchange of fire?", "It violated the Northern Limit Line despite a warning broadcast", ["It was lost", "It was carrying tourists", "It was in trouble"], "경고방송에도 불구하고."), M("What did North Korea restrict and block?", "Overland passage through the Military Demarcation Line", ["Air travel", "Phone calls", "Sea fishing"], "육로 통행."), M("What did the restriction make impossible?", "Entry to the Gaesung Industrial Complex", ["Trade with China", "Tourism to Jeju", "Newspaper delivery"], "개성공단의 출입."), M("Who was shot to death on a 금강산 trip?", "The tourist Park Wang-ja", ["A soldier", "A reporter", "A diplomat"], "박왕자 씨."), M("What did North Korea do in the third summary?", "Carried out its second nuclear test", ["Opened a border", "Signed a treaty", "Held a summit"], "핵실험을 강행했다."), M("Where was the nuclear test site?", "Underground near Mantap Mountain in North Hamgyeong Province", ["In the sea", "In Pyongyang", "On Mount Kumgang"], "만탑산."), M("What was the purpose of the nuclear test, according to the text?", "To convey a message for negotiations with the Obama administration", ["To celebrate", "To train soldiers", "To build a factory"], "협상을 위한 메시지."),
           F("한국 해군의 ___ 방송에도 불구하고 북방한계선을 침범했다. (warning)", "경고", ["취임", "기공"], "경고방송."), F("북한의 경비정이 북방한계선을 ___했다. (violated)", "침범", ["체결", "채택"], "침범하다."), F("서해에서 남북한 ___이 있었다. (an exchange of fire)", "교전", ["기공", "취임"], "교전."), F("북한이 핵실험을 ___했다. (went ahead with)", "강행", ["체결", "단합"], "강행하다."), F("북한은 육로 통행을 제한하고 ___한다고 통보했다. (block)", "차단", ["허락", "채택"], "차단하다."),
           read_q("서해에서 남북한 교전이 있었습니다"), read_q("북한이 핵실험을 강행했습니다"), read_q("육로 통행을 제한하고 차단한다고 통보했습니다"), read_q("개성공단의 출입이 불가능하게 되었습니다"), read_q("우리는 본디 하나")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("가르다", "to divide; to separate", "자, 지금부터 두 편으로 갈라서 게임을 합시다.", "나누다"),
        ("간절하다", "(懇切) to be earnest; to be ardent; to thirst for; to yearn for", "삼 일 동안 커피를 마시지 않아서 지금 커피 생각이 간절합니다."),
        ("멍(들다)", "bruise; contusion (to be black and blue; to get bruised)", "자전거를 타다가 넘어져서 다리에 멍이 들었어요."),
        ("본디", "originally; at first; in the first place", "한국은 본디 자연을 존경하는 나라였다.", "원래, 본래"),
        ("이루다", "to accomplish; to achieve", "꿈을 이루려면 노력이 필요합니다.", "성취하다, 달성하다"),
    ]),
    ("학습활동 2", [
        ("결합(하다)", "(結合) combining; uniting (to combine; to unite)", "남한의 기술과 북한의 자원이 결합하면 큰 발전이 있을 거예요."),
        ("노동력", "(勞動力) labor power", "기업들이 값싼 노동력을 찾아 해외 시장을 찾고 있습니다."),
        ("무시무시하다", "to be scary; to be spooky", "어제 본 할로윈 영화가 너무 무시무시해서 밤에 나쁜 꿈을 꾸었어요.", "무섭다"),
        ("무심히", "(無心) indifferently; inattentively; thoughtlessly; “with no heart”", "무심히 창 밖을 보니 조용히 비가 내리고 있었어요."),
        ("문화운동가", "(文化運動家) a cultural activist", ""),
        ("반세기", "(半世紀) a half century; 50 years", "남북한이 분단된 지 반세기가 넘었어요."),
        ("사례", "(事例) a case; an incident; an example", "구체적인 사례를 들어 설명해 주세요."),
        ("살아생전", "(生前) in one’s life; when one was alive", "어머니는 살아생전에 자식들 걱정만 하셨습니다."),
        ("상생(하다)", "(相生) living together; coexistence (to live together; to coexist)", "정부는 중소기업과 대기업의 상생을 강조하고 있습니다."),
        ("외면(하다)", "(外面) to ignore; to turn one’s back on", "어제 싸웠던 친구가 나를 불렀지만 외면하고 대답을 하지 않았다."),
        ("재앙", "(災殃) a disaster", "환경을 생각하지 않은 개발은 재앙을 불러올 수 있습니다.", "재난 | 천재지변"),
        ("재회", "(再會) reunion", "오 년 만에 아버지와 재회했어요.", "상봉"),
        ("증오(하다)", "(憎惡) hatred; loathing; abhorrence (to hate; to loathe; to abhor)", "저는 그 사람을 증오합니다."),
        ("총재", "(總裁) a secretary general; a president", "유엔 총재가 일본과 한국을 방문했습니다."),
        ("추진(하다/되다)", "(推進) propel; driving forward (to propel/to be propelled)", "여성부가 새 법안을 추진하기로 했습니다."),
    ]),
    ("학습활동 3", [
        ("경고방송", "(警告放送) a warning broadcast", "강물이 불어났다는 경고방송이 여러 번 나왔습니다."),
        ("경비정", "(警備艇) a guard ship; a patrol ship", ""),
        ("교전", "(交戰) exchange of fire; a battle; “exchange of war”", "서해상에서 남북한 교전이 있었습니다."),
        ("기공식", "(起工式) a ground-breaking ceremony", "시청 기공식에 누가 참석합니까?", "착공식 | 완공식, 준공식"),
        ("대량파괴무기 확산방지구상", "(大量破壞武器 擴散防止構想) PSI (Weapons of Mass Destruction Proliferation Security Initiative)", ""),
        ("북방한계선", "(北方限界線) NLL (Northern Limit Line)", "북한 경비정이 북방한계선을 넘어 남한 영해로 들어왔습니다."),
        ("사살", "(射殺) killing by gunshot", "서해 교전에서 다섯 명이 사살되었습니다."),
        ("서신", "(書信) a letter", "지난해부터 남북한 사이에 서신 교류가 가능해졌습니다.", "편지, 서한"),
        ("시제품", "(試製品) a test product", "다음주에 시제품 전시회가 열립니다."),
        ("심리전", "(心理戰) psychological warfare (basically a verbal attack over the loudspeaker near the DMZ)", "심리전을 벌이다."),
        ("우발충돌", "(偶發衝突) an inadvertent conflict", "서해상에서 우발충돌을 방지하기 위해 남북이 협의를 했습니다."),
        ("육로통행", "(陸路通行) inland traffic; inland transportation", "이제부터 남북한간 육로통행이 가능해졌습니다."),
        ("의도", "(意圖) intention", "그런 말을 하는 의도가 무엇입니까?"),
        ("일지", "(日誌) a journal; a diary", "업무일지를 작성해 주세요."),
        ("입주업체", "(入住業體) a resident company (at an industrial site)", "이 공단의 입주업체들이 몇 개나 됩니까?"),
        ("지뢰", "(地雷) a landmine; “earth lightning”", "", "어뢰"),
        ("차단(하다/되다)", "(遮斷) blocking (off/out); cutting off (to block/to be blocked)", "이 방은 커튼이 두꺼워서 햇빛이 완전히 차단됩니다."),
        ("채택(하다/되다)", "(採擇) adoption (to adopt/to be adopted)", "제 의견이 채택되었어요."),
        ("총격", "(銃擊) an attack by gunfire", "중동 여러 나라에서 많은 시민들이 총격으로 사망했다고 합니다."),
        ("취임사", "(就任辭) an inaugural address/speech", "신임 대통령의 취임사가 정말 감동적이었어요."),
        ("침몰(하다/되다)", "(沈沒) sinking (to sink)", "부산 앞바다에서 배가 침몰해서 많은 사람이 사망했어요."),
        ("핵실험", "(核實驗) a nuclear test", "북한이 얼마 전 이 차 핵실험을 강행했습니다."),
    ]),
    ("학습활동 4", [
        ("~ 돐", "the -th anniversary", "이 회사가 창립된 지 스무 돌이 되었어요.", "~ 돌"),
        ("동지", "(同志) a comrade; “(person with) same aim”", "", "동무"),
        ("령도", "(領導) leadership", "", "영도"),
        ("리행", "(履行) practice; implementation", "", "이행"),
        ("맞이하다", "to receive; to greet; to welcome", "따뜻하게 맞이해 주셔서 감사합니다."),
        ("분렬", "(分裂) division; split; segmentation; schism", "팀원들간의 의견이 맞지 않아 분열되었어요.", "분열"),
        ("선군 혁명", "(先軍 革命) The term 선군 was coined by 김정일 to refer to his own unique politics and military, which were different from his father’s. Thus, 선군정치 means (김정일’s) Military Revolution.", "선군정치, 선군사상"),
        ("수반", "(首班) the chief/head (of a government, an organization, etc.)", "대통령은 행정부의 수반입니다."),
        ("위대한 령도자", "(偉大 領導者) the Great Leader (referring to NK’s 김정일)", "", "위대한 영도자"),
        ("조선로동당", "(朝鮮勞動黨) the Labor Party of DPRK", "", "조선노동당"),
        ("창건(하다/되다)", "(創建) foundation; establishment (to found/to be founded)", "이 절이 언제 창건되었습니까?"),
    ]),
]
L7 = lesson(
    "U15 L8 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 가르다 · 간절하다 · 본디 · 반세기 · 상생 · 재앙 · 교전 · 북방한계선 · 사살 · 심리전 · 육로통행 · 핵실험 · 령도 · 선군 혁명 · 조선로동당",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 3일 → 삼 일; 5년 → 오 년; 5명 → 다섯 명; 2차 → 이 차. The North Korean spellings 령도, 리행, 분렬, 위대한 령도자 and 조선로동당 are given with their South Korean equivalents (영도, 이행, 분열, 위대한 영도자, 조선노동당) in the related words. The book lists 침몰(하다;되다) with a semicolon; it is written with a slash here, and the book’s 대량파괴무기 확산방지구상 is the full name of PSI.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=26, nread=20)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 8: North Korea I (북한 I)", [L1, L2, L3, L4, L5, L6, L7])

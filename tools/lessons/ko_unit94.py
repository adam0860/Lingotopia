"""Unit 94: KBC Semester III, Unit 18, Lesson 9 - Diplomacy (외교).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 18, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_MATCH9 = [("지도자", "a leader", "그분은 존경받는 지도자다"), ("정치", "politics", "요즘 젊은이들은 정치에 관심이 없다"), ("정상", "top; summit; head of a nation", "각국 정상이 만나서 회담을 한다"), ("재개", "reopening; resumption", "남북 협상이 재개되었다"), ("자국", "one's own country", "자국의 이익을 위해 노력한다"), ("명령", "an order; a command", "군대에서는 상사의 명령을 따라야 한다"), ("언론", "the media; the press", "언론의 역할이 중요하다"), ("인권", "human rights", "국가는 국민들의 인권을 보호한다"), ("관계", "relations; relationship", "이 마을은 가족간에 관계가 좋아요"), ("양측", "both sides; both parties", "남북 양측의 의견이 다르다"), ("순방", "(a round of) visits; a round of calls", "대통령이 해외 순방 길에 나섰다")]
_AUD9 = [("외교", "diplomacy"), ("개발도상국", "a developing country"), ("자국", "one's own country"), ("순방", "a round of visits"), ("정상회담", "a summit meeting")]
_HJ9 = [("言 언", "speech; language", "언어, 언론"), ("指 지", "finger; pointing", "지시, 반지"), ("開 개", "open", "개방, 재개"), ("親 친", "closeness; friendly", "친선, 친절"), ("缺 결", "absence; shortage", "결석, 결점")]
_HJW9 = [("언어", "a language; speech"), ("언론", "the press; the (mass) media"), ("지시", "an instruction"), ("반지", "a ring"), ("개방", "openness"), ("재개", "reopening; resumption"), ("친선", "friendship"), ("친절", "kindness"), ("결석", "absence from class"), ("결점", "a flaw; a fault; shortcomings")]
_OPP9 = [("개업", "폐업", "opening a business: closing a business"), ("부친", "모친", "father: mother"), ("결석", "출석", "absence: attendance"), ("발언", "침묵", "speaking out: silence")]
_ALL9 = [("신문, 대중매체, 방송", "언론", "newspaper, mass media, broadcast: the press"), ("외국어, 모국어, 외래어", "언어", "foreign language, mother tongue, loanword: language"), ("동창회, 동호회, 모임", "친목", "alumni association, club, gathering: friendly relations")]
_L9X = [("개업", "opening a business"), ("폐업", "closing a business"), ("전개", "development; unfolding"), ("소개", "an introduction"), ("부친", "one's father"), ("모친", "one's mother"), ("친척", "a relative"), ("친목", "friendly relations"), ("출석", "attendance"), ("출장", "a business trip"), ("결정", "a decision"), ("결심", "a resolution"), ("발언", "a remark"), ("언쟁", "a quarrel"), ("침묵", "silence"), ("발상", "an idea"), ("동창회", "an alumni association"), ("동호회", "a hobby club"), ("외래어", "a loanword"), ("대중매체", "the mass media")]
L1 = lesson(
    "U18 L9 · Review: diplomacy words and Sino-Korean 言 指 開 親 缺",
    "외교 · 단어 복습 · 한자어 복습 · 지도자 · 정상 · 재개 · 자국 · 언론 · 양측 · 순방 · 言 指 開 親 缺",
    requires=[],
    cards=[
        card("단어 복습 1: connect the underlined word with its meaning", "The book gives eleven sentences with a word underlined and eleven English meanings. The underlines are not marked in the text; the pairs below are my reading (the sentence about orders in the army could point to 상사 “a superior” or 명령 “an order”; the meaning “an order; a command” fits 명령):", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH9], say=[0, 2])]),
        card("The words of 단어 복습 2", "In the audio activity four clips explain politics and diplomacy; you write the related word from the box and its English meaning. The box words are below; the English is mine:", tables=[ktable(_AUD9)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ9], say=[2]), ktable(_HJW9)]),
        card("한자어 복습 1: the word with the opposite meaning (my answers)", "Circle the word opposite in meaning to the word on the left (A. 개업: 개방, 전개, 폐업, 소개; B. 부친: 친척, 친절, 친목, 모친; C. 결석: 결정, 결심, 출장, 출석; D. 발언: 언쟁, 침묵, 언어, 발상).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP9], say=[0, 1])]),
        card("한자어 복습 2: the word related to all three (my answers)", "Choose from the box (지시, 친목, 언어, 결점, 언론) the word related to the three words of each line; 지시 and 결점 are not used:", tables=[table(["Three words", "Answer", "Meaning"], [list(r) for r in _ALL9], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L9X)]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001–004): four audio clips on politics and diplomacy. They are audio."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH9], k=3) + _tr(_AUD9, k=3) + _tr(_HJW9, k=3) + _tr(_L9X, k=4)
        + [M("What does the syllable 言 (언) mean?", "speech; language", ["finger; pointing", "open", "absence"], "언어."), M("What does the syllable 指 (지) mean?", "finger; pointing", ["speech", "open", "closeness"], "지시."), M("What does the syllable 開 (개) mean?", "open", ["speech", "finger", "absence"], "개방."), M("What does the syllable 親 (친) mean?", "closeness; friendly", ["open", "absence", "finger"], "친절."), M("What does the syllable 缺 (결) mean?", "absence; shortage", ["speech", "open", "closeness"], "결석.")
           , M("Which word is the opposite of 개업?", "폐업", ["개방", "전개", "소개"], "Closing a business."), M("Which word is the opposite of 부친?", "모친", ["친척", "친절", "친목"], "Mother."), M("Which word is the opposite of 결석?", "출석", ["결정", "결심", "출장"], "Attendance."), M("Which word is the opposite of 발언?", "침묵", ["언쟁", "언어", "발상"], "Silence."), M("Which word covers 신문, 대중매체, 방송?", "언론", ["언어", "친목", "지시"], "The press."), M("Which word covers 외국어, 모국어, 외래어?", "언어", ["언론", "친목", "결점"], "Language.")
           , F("각국 ___이 만나서 회담을 한다. (heads of state)", "정상", ["지도자", "양측"], "정상."), F("남북 협상이 ___되었다. (resumed)", "재개", ["개방", "개업"], "재개."), F("___의 이익을 위해 노력한다. (one's own country)", "자국", ["양측", "정상"], "자국."), F("대통령이 해외 ___ 길에 나섰다. (a round of visits)", "순방", ["관계", "명령"], "순방.")]
        + [read_q("그분은 존경받는 지도자다"), read_q("각국 정상이 만나서 회담을 한다"), read_q("남북 양측의 의견이 다르다"), read_q("대통령이 해외 순방 길에 나섰다")]
    ),
)

# ================================================================== L2 Part 1
_INT9 = [
    ("외교통상부가 중남미 지역 일곱 개 국제기구에 파견할 인턴을 선발한다.", "The Ministry of Foreign Affairs and Trade is selecting interns to dispatch to seven international organizations in the Latin American region."),
    ("파견시기는 올해 구 월부터 내년 이 월까지 여섯 개월이며 대학생 삼 학년에서 사 학년 또는 대학원생만 자격이 주어진다.", "The dispatch period is six months, from September this year to February next year, and only university students (third to fourth year) or graduate students are eligible."),
    ("스페인어 및 영어 능통자로 평점 삼 점 영 이상의 학점을 유지하고 있어야 한다.", "Applicants must be proficient in Spanish and English and keep a grade point average of 3.0 or higher."),
    ("외교부는 올 상반기 인원 세 명을 이미 선발했으며 하반기 열네 명을 추가선발, 최대 열일곱 명까지 인턴을 파견할 계획이다.", "The ministry has already selected three people in the first half of this year and plans to select fourteen more in the second half and dispatch up to seventeen interns."),
    ("자세한 내용은 외교부 홈페이지로 공지될 예정이며 외교부 중남미협력과에 문의할 수 있다.", "Details will be announced on the ministry’s homepage, and inquiries can be made to the ministry’s Latin America Cooperation Division."),
]
_SPEAK9 = [("미국의 주요 외교 대상국이 어떤 나라인지 생각해 보고, 최근에 미국 대통령이 해외 순방을 하거나 외국 지도자들의 방문을 받은 것이 있으면 그에 대해 옆 친구와 이야기해 보세요.", "Think about which countries are the main diplomatic partners of the United States, and if the US president has recently made a trip abroad or received visits from foreign leaders, talk about it with the friend beside you.")]
L2 = lesson(
    "U18 L9 · Part 1 (도입 학습): an internship announcement",
    "도입 학습 · 외교통상부 · 인턴 선발 · 파견 · 능통자 · 자격 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: the Ministry of Foreign Affairs and Trade’s announcement (Naeil)", "The book asks three questions in English: what was announced and who the target audience is, what qualifications are required, and what the ministry plans. The numbers are spelled in Hangul (“3~4학년” as 삼 학년에서 사 학년, “3.0” as 삼 점 영, “6개월” as 여섯 개월), and the website address and the telephone number are dropped. The announcement, with my English:", examples=passage(_INT9)),
        card("My answers to 학습활동 2", "1. The ministry announced that it will select interns to send to seven international organizations in Latin America; the target audience is university students in their third or fourth year or graduate students. 2. They must be university (third- or fourth-year) or graduate students, proficient in Spanish and English, with a grade point average of 3.0 or higher. 3. It has already selected 3 interns for the first half of this year and plans to select 14 more in the second half, sending up to 17 interns for six months from September this year to February next year; details will be posted on the ministry’s homepage."),
        card("말해 봅시다! (speaking)", "The book’s prompt (the English is mine):", examples=passage(_SPEAK9)),
        card("Activities left out", "학습활동 1 (Reading): a chart from Hankyoreh of the overseas visit schedules of leaders of several countries; you write each leader’s schedule by month in English in a table (Late September, Early October, October, November), the first row being South Korean President Lee Myung-bak. 학습활동 3 (Listening, tracks 005 and 006): a YTN news report evaluating the Korean government’s diplomatic achievements and areas in need of improvement, to be put into a table, then checked against the video. 학습활동 4 (Listening, track 007): North Korean news (KCNA) on a leader’s visit to the city of Jilin: what the report is about and a table of the places visited and their significance. They are charts, audio and video."),
    ],
    exercises=uniq(
        _tr(_INT9, k=3)
        + [M("How many international organizations will interns be sent to?", "Seven", ["Three", "Fourteen", "Seventeen"], "일곱 개."), M("How long is the dispatch period?", "Six months", ["Three months", "One year", "Two years"], "여섯 개월."), M("Who is eligible?", "University students (third to fourth year) and graduate students", ["Only graduates of five years", "Any high school student", "Only diplomats"], "자격."), M("Which languages must the applicants know?", "Spanish and English", ["Chinese and Japanese", "French and German", "Russian and English"], "스페인어 및 영어."), M("What is the maximum number of interns?", "Seventeen", ["Three", "Fourteen", "Seven"], "열일곱 명.")]
        + [F("스페인어 및 영어 ___자로 평점 삼 점 영 이상. (proficient)", "능통", ["선발", "파견"], "능통자."), F("인턴을 ___할 계획이다. (to dispatch)", "파견", ["선발", "초청"], "파견."), F("외교통상부가 인턴을 ___한다. (to select)", "선발", ["파견", "참관"], "선발.")]
        + [read_q("외교통상부가 중남미 지역 국제기구에 파견할 인턴을 선발한다"), read_q("스페인어 및 영어 능통자만 자격이 주어진다"), read_q("미국의 주요 외교 대상국이 어떤 나라인지 생각해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("정상", "(頂上) the top; summit; head of a state", "그 선수는 정상급 투수입니다.", "정상회담"),
    ]),
    ("학습활동 2", [
        ("능통하다", "(能通) to be proficient in; to have a thorough knowledge of", "김 일병은 영어와 일어에 능통합니다."),
        ("선발(하다/되다)", "(選拔) selection (to select/to be selected)", "미스코리아 선발 대회를 개최하는 것에 대해 논란이 있습니다.", "선택하다"),
        ("파견(하다/되다)", "(派遣) dispatching; sending (to dispatch; to send/to be dispatched; to be sent)", "김 대리가 다음 달에 해외 지사로 파견 나갑니다.", "보내다"),
    ]),
    ("학습활동 3", [
        ("가시적", "(可視的) visible; tangible", "이번 회담은 가시적인 성과를 내지 못했습니다."),
        ("갈등", "(葛藤) a conflict; a discord", "이 두 나라는 역사적인 배경 때문에 갈등이 깊습니다.", "마찰"),
        ("경색(되다)", "(梗塞) hardening; straining (of relations between two parties); stagnating (to strain; to slow; to stagnate)", "최근 발생한 사건으로 두 나라의 관계가 경색되었습니다.", "심근경색"),
        ("과제", "(課題) a problem; a task", "빈곤을 해소하는 것이 새 정부의 과제입니다.", "숙제"),
        ("마찰", "(摩擦) friction; trouble; a conflict", "", "갈등"),
        ("비화되다", "(飛火) to escalate into; to lead to a bigger problem", "정부는 이 문제가 외교 문제로 비화될 것을 우려하고 있습니다."),
        ("수교(하다)", "(修交) establishing diplomatic ties (to establish diplomatic ties)", "한미 수교 육십 주년 행사가 열렸다."),
        ("적대적", "(敵對的) hostile", "북한은 전 세계에 대하여 적대적인 태도를 유지하고 있습니다.", "우호적"),
        ("접어들다", "to enter into (a phase); to get into", "하반기에 접어들면서 경제가 회복세를 보이고 있습니다."),
        ("집권(하다)", "(執權) seizing power; coming to power (to seize power; to come to power)", "이번 선거로 민주당이 집권하게 되었다."),
        ("출범(하다)", "(出帆) launching of an organization (to launch a new organization; to set sail)", "다음 주에 새 정부가 출범합니다."),
        ("퇴색(하다/되다)", "(退色 or 褪色) discoloration; fading (to lose color; to become discolored)", "이 옷 색깔이 햇볕에 많이 퇴색되었습니다. 시간이 지나면서 본래의 취지가 퇴색되었다.", "변색되다"),
    ]),
    ("학습활동 4", [
        ("어버이 수령님", "(守令) the Great Leader (referring to Kim Il-sung, father of Kim Jong-il); “parent-like leader”", ""),
        ("연고지", "(緣故地) a related place", "그곳은 제 친척들이 많이 계신 제 연고지입니다.", "연고자"),
        ("위대한 령도자", "(偉大領導者) Dear Leader (referring to Kim Jong-il)", ""),
        ("일꾼", "a worker; a workman; workforce", "그 사람은 우리 팀에서는 없어서는 안 될 소중한 일꾼입니다."),
        ("중화인민공화국", "(中華人民共和國) the People’s Republic of China", ""),
        ("집약화(하다/되다)", "(集約化) concentrating (to concentrate/to be concentrated)", "이 공장은 첨단기술과 노동력이 집약화되어 있는 곳입니다."),
        ("참관(하다)", "(參觀) visiting and observing (to visit and observe)", "오늘 몇 시에 수업을 참관할 계획입니까?"),
        ("초청(하다/받다)", "(招請) an invitation (to invite/to be invited)", "이 대통령은 중국 주석의 초청으로 중국을 방문했습니다.", "초대하다, 초빙하다"),
        ("추억", "(追憶) a memory; a recollection; a reminiscence", "이곳은 저에게 좋은 추억이 많은 곳입니다."),
        ("혁명", "(革命) a revolution", "새로운 물질의 개발은 에너지 분야에 혁명을 가져올 것입니다.", "혁명가"),
    ]),
]
L3 = lesson(
    "U18 L9 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 정상 · 능통하다 · 선발 · 파견 · 가시적 · 갈등 · 경색 · 과제 · 마찰 · 비화 · 수교 · 적대적 · 접어들다 · 집권 · 출범 · 퇴색 · 연고지 · 일꾼 · 집약화 · 참관 · 초청 · 추억 · 혁명",
    requires=[],
    cards=[card("A note on the Korean in this list", "정상 lists 정상회담 as related and carries the homonym 정상 (正常), “normality”. The book’s entry 어버이 수령님 and 위대한 령도자 are the North Korean titles of Kim Il-sung and Kim Jong-il; 령도자 is the North Korean spelling of 영도자. 마찰 has no example in the book. 퇴색 has two Hanja forms and two examples (joined). The book’s example for 초청 reads “이 대통령의 중국 주석의 초청으로”, a typo that I corrected to “이 대통령은 중국 주석의 초청으로”. The example of 수교 had a digit (60주년), which I spelled out.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=14, nread=14)),
)

# ================================================================== L4 Part 2
_PUB9 = [
    ("공공외교란 군사력과 경제력 등 하드파워가 중시되는 전통외교에 대비되는 개념으로, 소프트파워 자산을 활용해 자국과 상대국 국민에게 올바른 정보를 제공하고 이해시킴으로써 국익을 증진시키는 외교활동을 말한다.", "Public diplomacy is a concept contrasted with traditional diplomacy, in which “hard power” such as military and economic strength is valued; it refers to diplomatic activity that raises the national interest by using “soft power” assets to give correct information to the people of one’s own country and the other country and make them understand."),
    ("우리의 경우 한류에서부터 한식의 세계화, 한국학 육성, 전시와 공연 등을 아우른다.", "In our case it encompasses everything from the Korean Wave to the globalization of Korean food, the fostering of Korean studies, and exhibitions and performances."),
    ("삼성, 엘지 등 기업 브랜드, 민주화 및 근대화 경험 등 문화와 지식자원 모두가 공공외교의 소재가 될 수 있다.", "Cultural and knowledge resources, such as corporate brands like Samsung and LG and the experience of democratization and modernization, can all become material for public diplomacy."),
    ("강대국 미국조차 구일일 사태와 이라크 전쟁을 겪으면서 더 이상 군사와 경제력으로 상징되는 하드파워 방식이 통하지 않음을 깨닫고 공공외교 활동에 주력해 왔다.", "Even the great power the United States, going through the September 11 incident and the Iraq war, realized that the hard-power approach symbolized by military and economic strength no longer works, and has concentrated on public diplomacy activities."),
    ("문화의 세기인 이십일 세기는 소프트파워가 주도하는 시대가 될 것으로 전망된다.", "The twenty-first century, the century of culture, is expected to become an age led by soft power."),
    ("이에 따라 각국은 전담부처까지 설치해 공공외교에 힘을 쏟고 있다.", "Accordingly, each country is putting its strength into public diplomacy, even setting up a dedicated ministry."),
    ("하지만 한국은 우리 경제력의 삼십 퍼센트에도 미치지 못할 만큼 국가브랜드 이미지를 저평가받고 있다.", "But Korea’s national brand image is undervalued, not even reaching 30 percent of our economic strength."),
    ("평가기관 안홀트 지엠이에 따르면 한국의 국가브랜드는 조사대상 삼십팔 개국 중 고작 삼십이 위를 차지하는 데 그쳤다.", "According to the evaluation agency Anholt-GME, Korea’s national brand came in at a mere 32nd place among the 38 countries surveyed."),
    ("각 대륙별로 한국에 대한 이미지를 상이하게 갖고 있는 것도 문제다.", "It is also a problem that each continent has a different image of Korea."),
    ("한인택 제주평화연구원 박사와 이근 서울대 교수에 따르면 한국은 유럽권에서 과학과 기술, 경제와 기업을 중심으로 한국 이미지를 쌓고 있는 반면 아시아권에서는 전통문화와 자연이 강점으로 부각되고 있다.", "According to Dr. Han In-taek of the Jeju Peace Institute and Professor Lee Geun of Seoul National University, Korea is building its image around “science and technology” and “economy and business” in Europe, while in Asia “traditional culture and nature” stand out as its strengths."),
    ("현대문화와 유명인에 대한 인식은 보편적으로 약점으로 꼽힌다.", "Perceptions of “modern culture” and “famous people” are generally counted as weaknesses."),
]
_SPEAK9B = [("미국과 중국의 경제체제는 어떻게 다릅니까?", "How do the economic systems of the United States and China differ?"), ("중국의 경제적 성장이 미국에는 어떤 영향을 줄까요?", "What effect will China’s economic growth have on the United States?")]
L4 = lesson(
    "U18 L9 · Part 2 (본 학습): public diplomacy and Korea’s national brand",
    "본 학습 · 공공외교 · 하드파워 · 소프트파워 · 국가브랜드 · 한류 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: part of an article on public diplomacy (Naeil)", "The book asks three questions in English: underline the sentence that defines 공공외교 and write its meaning, fill a table of examples of hard power and soft power, and say what Korea’s public diplomacy problems are. The numbers are spelled in Hangul (“9·11사태” as 구일일 사태), Latin names are written in Hangul (LG, Anholt-GME), the middle dots and quotation marks are dropped, and the Hanja 韓流 is dropped. The two experts are named as in the article. The article, with my English:", examples=passage(_PUB9)),
        card("My answers to 학습활동 2", "1. The defining sentence is the first one: public diplomacy is diplomatic activity that raises the national interest by using soft-power assets to give correct information to the people of one’s own and the other country and make them understand; it is contrasted with traditional diplomacy that values hard power. 2. Hard power: military strength and economic strength. Soft power: the Korean Wave (한류), globalization of Korean food, fostering of Korean studies, exhibitions and performances, corporate brands such as Samsung and LG, and the experience of democratization and modernization. 3. Korea’s national brand image is undervalued (not even 30 percent of its economic strength; 32nd of 38 countries surveyed), and each continent has a different image of Korea (science, technology, economy and business in Europe; traditional culture and nature in Asia), while the perception of modern culture and famous people is generally a weakness."),
        card("말해 봅시다! (speaking)", "The book’s two prompts (the English is mine):", examples=passage(_SPEAK9B)),
        card("Activities left out", "학습활동 1 (Listening, Writing, Speaking, track 008): a YTN news report on a diplomatic issue: what Korea’s dilemma is about the United States and Iran, how the government plans to cope with it, and your own ideas for solving it, to be written in Korean and shared. 학습활동 3 (Listening, track 009): a YTN briefing on President Lee’s China visit: the events of the trip in order (starting from the welcoming ceremony), the significance of raising the relationship to a “strategic relationship” and how relations will change, why China had not been able to reach this in the past, and why China changed its position toward South Korea. They are audio and video."),
    ],
    exercises=uniq(
        _tr(_PUB9, k=3) + _tr(_SPEAK9B, k=2)
        + [M("What kind of power does traditional diplomacy value?", "Hard power such as military and economic strength", ["Soft power such as culture", "Only trade", "Only language"], "하드파워."), M("What does public diplomacy use?", "Soft-power assets", ["Military force", "Economic sanctions", "Secret agreements"], "소프트파워."), M("Which is named as an example of soft power for Korea?", "The Korean Wave (한류)", ["Nuclear weapons", "Oil exports", "Border defense"], "한류."), M("Where did Korea’s national brand rank among 38 countries?", "32nd", ["3rd", "12th", "38th"], "삼십이 위."), M("In Asia, what stands out as Korea’s strength?", "Traditional culture and nature", ["Science and technology", "Economy and business", "Famous people"], "전통문화와 자연."), M("What is expected to lead the 21st century?", "Soft power", ["Hard power", "Military alliances", "Oil"], "소프트파워.")]
        + [F("공공외교는 ___외교에 대비되는 개념이다. (traditional)", "전통", ["현대", "공공"], "전통외교."), F("한국은 국가브랜드 이미지를 ___받고 있다. (undervalued)", "저평가", ["고평가", "재평가"], "저평가."), F("각 대륙별로 한국에 대한 이미지가 ___하다. (different)", "상이", ["동일", "보편"], "상이하다."), F("공공외교 활동에 ___해 왔다. (to concentrate)", "주력", ["강구", "가담"], "주력.")]
        + [read_q("공공외교란 소프트파워 자산을 활용해 국익을 증진시키는 외교활동을 말한다"), read_q("문화의 세기인 이십일 세기는 소프트파워가 주도하는 시대가 될 것이다"), read_q("한국은 국가브랜드 이미지를 저평가받고 있다"), read_q("미국과 중국의 경제체제는 어떻게 다릅니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("가담(하다)", "(加擔) participating; engaging in (to participate; to engage in; to take part in)", "검찰은 이번 시위에 가담한 이들을 모두 검거하겠다는 방침입니다.", "동참, 참여"),
        ("강구(하다)", "(講究) devising a plan; conceiving a plan (to devise a plan)", "정부는 최근 발생한 외교 마찰에 대한 대책을 강구하고 있습니다.", "법안을 강구하다"),
        ("곤혹스럽다", "(困惑) to be perplexed; to be puzzled; to be embarrassed", "이 문제로 야당은 곤혹스러운 모습을 감추지 못하고 있습니다.", "당황스럽다"),
        ("국익", "(國益) a national interest", "그것은 국익을 위한 결정이었습니다."),
        ("기축", "(基軸) an axis; a base; “ground pivot”", "국가 발전의 기축을 전통에서 찾아야 할 것입니다.", "기본"),
        ("동맹", "(同盟) alliance; partnership", "양국의 군사동맹은 더욱 강화될 것입니다."),
        ("동참(하다)", "(同參) joint; participation; joining; taking part in (to join; to participate)", "전 세계의 많은 국가들이 난민 구조활동에 동참하고 있습니다.", "참여, 가담"),
        ("딜레마", "a dilemma", "저는 딜레마에 빠져서 어떤 결정도 하기 어렵습니다."),
        ("수위", "(水位) level (of intensity or criticism); “water level”", "비가 와서 수위가 많이 올라갔습니다. 야당이 정부를 비판하는 수위가 아주 높습니다.", "강도"),
        ("악화(되다)", "(惡化) deterioration; aggravation; getting worse (to deteriorate; to get worse)", "요즘 들어 어머니 병이 악화되고 있어 걱정이 됩니다.", "호전되다"),
        ("요청(하다)", "(要請) a request; demand (to make a request)", "수해 피해가 너무 커서 정부에 지원을 요청해야 합니다.", "요구"),
        ("우려(하다)", "(憂慮) concern; worry (to be concerned; to worry)", "시민들은 테러 공격을 우려하며 외출을 삼가고 있습니다.", "걱정, 염려"),
        ("제재(하다)", "(制裁) sanctions; restriction (to impose sanctions)", "북한에 대해 경제 제재를 실시하기로 했습니다."),
        ("지장", "(支障) a hindrance; an interference; an obstacle", "사고는 컸지만 환자 생명에는 지장이 없을 것으로 보입니다. 일에 지장을 초래하지 않는 한 언제든지 휴가를 가도 좋습니다.", "방해, 장애"),
        ("지혜", "(智慧) wisdom", "우리 함께 지혜를 모아서 이 위기를 잘 대처합시다."),
        ("초래(하다)", "(招來) causing; bringing about (to cause; to bring about; to incur)", "과소비가 경제혼란을 초래했습니다."),
        ("태스크포스", "a task force", "정부는 아이티 분야를 육성하기 위해 태스크포스를 구성하기로 했습니다."),
        ("해법", "(解法) a solution", "", "해답"),
    ]),
    ("학습활동 2", [
        ("강대국", "(强大國) a powerful nation", "미국이 강대국이라는 사실에 이견을 다는 사람은 없습니다.", "강국, 약소국, 선진국, 후진국, 개발도상국"),
        ("개념", "(槪念) a concept; a notion; an idea", "그 사람은 시간 개념이 없어서 항상 늦습니다."),
        ("근대화", "(近代化) modernization", "우리나라는 십구 세기에 근대화가 시작되었습니다.", "현대화"),
        ("깨닫다", "to realize; to notice", "사태가 심각해질 때까지 그 심각함을 깨닫지 못했습니다."),
        ("대비(하다/되다)", "(對比) contrast (to contrast/to be contrasted)", "전년 대비 수출 실적이 많이 호전되었습니다.", "비교"),
        ("보편적", "(普遍的) universal", "사람이 사람을 사랑하는 것은 누구나 이해할 수 있는 보편적 정서입니다."),
        ("아우르다", "to integrate; to encompass; to bring (things or people) together", "이 제안은 서로 상반된 양쪽의 주장을 다 아우르는 것입니다."),
        ("주력(하다)", "(主力) main focus (to concentrate on; to devote one’s attention)", "새로 출범한 정부는 경제문제에 주력할 계획이라고 밝혔습니다.", "주력상품, 주력부대"),
    ]),
    ("학습활동 3", [
        ("격상(하다/되다)", "(格上) promotion; elevation (to promote to a higher level/to be raised to a higher level)", "정부는 테러 위험 수위를 한 단계 격상했습니다."),
        ("기자회견", "(記者會見) a press conference", "대통령이 열 시부터 기자회견을 한다고 합니다."),
        ("긴밀하다", "(緊密) to be close; to be closely related", "두 나라는 긴밀한 동맹관계를 유지하고 있습니다."),
        ("동반자", "(同伴者) a companion; a partner", "두 나라는 동반자 관계를 구축하기로 합의했습니다."),
        ("반발(하다)", "(反撥) resistance; opposition (to resist; to oppose; to push back)", "정부의 새 법안에 반발하는 시민단체가 많습니다.", "반대"),
        ("발언(하다)", "(發言) a comment; a remark (to make a comment)", "저는 이 문제에 대해 어떤 발언도 하지 않겠습니다."),
        ("범위", "(範圍) scope; range; limit", "제가 아는 범위 내에서 최선을 다해 답변하겠습니다."),
        ("부쩍", "remarkably; increasingly", "요즘 들어 몸무게가 부쩍 늘었어요."),
        ("서명식", "(署名式) a signing ceremony", "이 대통령은 오늘 오전 서명식에 참여합니다."),
        ("설득력", "(說得力) persuasive power; reasoning power", "그 사람의 얘기는 전혀 설득력이 없습니다.", "설득력이 떨어지다"),
        ("설정(하다)", "(設定) setup (to set up)", "먼저 목표를 설정하고, 그 후에 실천방안을 생각해 봅시다."),
        ("조약", "(條約) a treaty; a pact", "전 세계에서 환경보호 조약에 참여하고 있는 나라가 몇 개나 됩니까?", "협정"),
        ("창구", "(窓口) a window; a channel", "우리 정부는 북한과의 대화 창구를 열기 위해 노력하고 있습니다."),
        ("체제", "(體制) a system", "남한과 북한은 한 민족이지만 체제가 다릅니다."),
        ("포괄적", "(包括的) comprehensive; inclusive", "오바마 대통령은 포괄적인 이민법을 제안했습니다."),
    ]),
]
L5 = lesson(
    "U18 L9 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 가담 · 강구 · 곤혹스럽다 · 국익 · 동맹 · 동참 · 딜레마 · 수위 · 악화 · 요청 · 우려 · 제재 · 지장 · 지혜 · 초래 · 태스크포스 · 해법 · 강대국 · 개념 · 근대화 · 대비 · 보편적 · 주력 · 격상 · 긴밀하다 · 동반자 · 반발 · 범위 · 서명식 · 설득력 · 조약 · 창구 · 체제 · 포괄적",
    requires=[],
    cards=[card("A note on the Korean in this list", "대비 carries the homonym 대비 (對備), “preparation”. 강대국 lists 강국, 약소국, 선진국, 후진국, 개발도상국 as related words. 강구 lists “법안을 강구하다” as printed (a phrase rather than a word). 수위 and 지장 have two examples each, which I joined. The example of 기자회견 had a digit (10시), which I spelled out as 열 시, and the example of 근대화 had “19세기”, spelled 십구 세기; “IT” in the example of 태스크포스 is written 아이티. 기자회견 appeared in Lesson 8 of this Unit with the same gloss. 해법 has no example in the book.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=26, nread=22)),
)

# ================================================================== L6 Part 3
_COL9 = [
    ("이명박 정권 이후 취해 온 강경 일변도의 대북 정책은 한반도의 안정적 관리에 치명상을 입혀 왔다.", "The hard-line-only North Korea policy taken since the Lee Myung-bak administration has dealt a fatal wound to the stable management of the Korean Peninsula."),
    ("지금 남북관계도 그렇고, 한반도 주변의 정세는 새로운 냉전시대로 접어든 듯 각축과 대결, 분쟁과 긴장감이 높아지고 있다.", "Both inter-Korean relations now and the situation around the peninsula are such that rivalry and confrontation, disputes and tension are rising, as if it had entered a new Cold War era."),
    ("이런 신냉전 구조 속에서 북쪽은 북쪽대로 권력 세습 문제로 옹색한 처지가 되면서 중국에 매달리고 있다.", "In this new Cold War structure, the North, for its part, has fallen into an awkward position over the issue of passing on power by heredity and is clinging to China."),
    ("남쪽은 남쪽대로 대책 없는 대북 강경책으로 스스로 출구를 닫아 왔다.", "The South, for its part, has closed its own exit with a hard-line policy toward the North that has no plan."),
    ("이렇게 앞뒤가 꽉 막힌 상황에서 한반도의 안정적 관리와 남북 사이 최소한의 신뢰와 대화 통로를 열어 놓기 위해서는 인도적 지원의 길을 터서 이를 이어가는 것이 절실하게 필요하다.", "In a situation so blocked front and back, to keep the Korean Peninsula stably managed and to leave open a minimum of trust and a channel for dialogue between the two Koreas, it is desperately necessary to open the way of humanitarian aid and continue it."),
    ("인도주의는 냉전 대결도 뛰어넘을 수 있고, 정치적 대결로 인한 긴장도 누그러뜨릴 수 있다.", "Humanitarianism can leap over even Cold War confrontation and can soften the tension caused by political confrontation."),
    ("올해 태풍과 홍수로 인해 북한의 식량 사정은 더욱 절박해졌다.", "This year, because of typhoons and floods, North Korea’s food situation has become still more desperate."),
    ("오죽했으면 북쪽이 남쪽에다 식량지원 요청을 했을까.", "How bad must it have been for the North to ask the South for food aid."),
    ("그런데 이에 대한 이명박 정권의 대응은 참으로 옹졸했다.", "Yet the Lee Myung-bak administration’s response to this was truly petty."),
    ("적어도 인도적 지원 문제만큼은 대담하게 하고, 이를 바탕으로 대화와 교류와 협력의 길을 터서, 한반도를 안정적으로 관리할 수 있는 기틀을 마련해야 한다.", "At least on the issue of humanitarian aid it should act boldly and, on that basis, open the way to dialogue, exchange and cooperation and prepare a framework in which the Korean Peninsula can be managed stably."),
    ("국가를 보위해야 하는 대통령의 기본 의무다.", "That is the basic duty of a president, who must preserve and protect the state."),
]
_REAG9 = [
    ("이명박 대통령은 레이건 전 대통령의 이야기에서 교훈을 찾아야 할 것이다.", "President Lee Myung-bak should find a lesson in the story of former President Reagan."),
    ("냉전의 시대인 천구백팔십 년대 당시 사회주의 국가인 에디오피아에 심한 기근이 발생했을 때, 당시 미국의 레이건 대통령은 배고픈 어린이는 정치를 모른다며 에디오피아에 대규모 인도적 식량지원을 한 바 있다.", "In the 1980s, the era of the Cold War, when a severe famine broke out in the socialist country Ethiopia, the then US President Reagan, saying “hungry children do not know politics,” gave large-scale humanitarian food aid to Ethiopia."),
]
_SPEAK9C = [("북한에 대해 미국과 한국은 어떻게 외교를 하는 것이 좋을지 생각해 보고 친구들과 의견을 나눠 보세요.", "Think about how the United States and Korea should conduct diplomacy toward North Korea, and share your opinions with your friends.")]
L6 = lesson(
    "U18 L9 · Part 3 (심화 학습): a column on North Korea policy and humanitarian aid",
    "심화 학습 · 대북정책 · 인도적 지원 · 강경 · 신냉전 · 레이건 · 에디오피아 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: a column on North Korea policy (Hankyoreh)", "The book asks three questions: the author’s tone and the examples that support it, the author’s main point (four choices), and where a given paragraph could most logically be inserted into the article (at one of the marks A, B, C or D). In the book the four marks A–D are placed after four sentences of the article; I leave them out of the Korean (they are Latin letters) and give the positions in my answer. “교류·협력” is written 교류와 협력, the quotation marks are dropped, and “1980년대” is 천구백팔십 년대. The column, with my English:", examples=passage(_COL9)),
        card("The paragraph to insert", "The book’s paragraph, with my English:", examples=passage(_REAG9)),
        card("My answers to 학습활동 3", "1. The tone is critical and urgent: the author calls the administration’s hard-line-only policy a “fatal wound,” says its response to the North’s food request was “truly petty” and its policy “has no plan,” and urges a “bold” humanitarian approach. 2. B (the South Korean government should offer humanitarian support to North Korea to keep dialogue open and normalize relations); D is related, but the column’s own argument is the humanitarian aid. 3. The marks are A after “...스스로 출구를 닫아 왔다,” B after “...누그러뜨릴 수 있다,” C after “...참으로 옹졸했다,” D after “...기본 의무다.” The paragraph (Lee should find a lesson in Reagan’s food aid to Ethiopia) fits best at C, right after the criticism of Lee’s petty response to the North’s request for food aid; this placement is my reading."),
        card("말해 봅시다! (speaking)", "The book’s prompt (the English is mine):", examples=passage(_SPEAK9C)),
        card("Activities left out", "학습활동 1 (Listening, Speaking, tracks 010 and 011): a video (YTN) of part of President Lee’s speech at the global policy forum in Russia; in pairs, Student A watches Part 1 (the forces that led Korea to success) and Student B watches Part 2 (three areas where Korea and Russia should cooperate), you fill the table, discuss in Korean and compare with other pairs. 학습활동 2 (Listening, track 012): a YTN interview with the chairman of the Foreign Affairs Committee on the significance of Korea’s hosting of the G20 Summit, Korea’s roles and responsibilities as host, and a plan to improve relations between Korea and Japan. They are video and audio, with partner activities."),
    ],
    exercises=uniq(
        _tr(_COL9, k=3) + _tr(_REAG9, k=2)
        + [M("How does the column describe the hard-line policy toward the North?", "As a fatal wound to stable management of the peninsula", ["As a great success", "As a necessary compromise", "As a long-term plan"], "치명상."), M("Why has North Korea’s food situation become desperate this year?", "Typhoons and floods", ["A drought", "A war", "Sanctions on trade with China"], "태풍과 홍수."), M("How does the author call the administration’s response to the North’s request?", "Petty (옹졸)", ["Generous", "Prompt", "Wise"], "옹졸했다."), M("What does the author want the South to do at least?", "Be bold on humanitarian aid", ["Cut all aid", "Build more defenses", "Join the North’s alliance"], "대담하게."), M("Which US president’s story does the added paragraph tell?", "Reagan’s", ["Roosevelt’s", "Obama’s", "Nixon’s"], "레이건."), M("Which country received US food aid in the 1980s story?", "Ethiopia", ["Cuba", "China", "Russia"], "에디오피아.")]
        + [F("북쪽은 북쪽대로 권력 ___ 문제로 옹색한 처지가 되었다. (hereditary succession)", "세습", ["교류", "보위"], "세습."), F("인도주의는 정치적 대결로 인한 긴장도 ___ 수 있다. (to soften)", "누그러뜨릴", ["각축할", "세습할"], "누그러뜨리다."), F("북한의 식량 사정이 더욱 ___해졌다. (desperate)", "절박", ["대담", "옹졸"], "절박하다."), F("인도적 지원의 ___을 터서 대화를 이어가야 한다. (road)", "길", ["벽", "창"], "길을 트다.")]
        + [read_q("이명박 정권 이후 취해 온 강경 일변도의 대북 정책은 한반도의 안정적 관리에 치명상을 입혀 왔다"), read_q("인도주의는 냉전 대결도 뛰어넘을 수 있다"), read_q("배고픈 어린이는 정치를 모른다"), read_q("북한에 대해 미국과 한국은 어떻게 외교를 하는 것이 좋을지 생각해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("공동운명체", "(公同運命體) community of a common destiny", "우리 두 나라는 밀접한 관계를 가진 공동운명체입니다."),
        ("공유(하다)", "(共有) sharing (to share)", "인터넷에서는 여러 사람들이 올린 정보를 공유할 수 있습니다.", "나누다"),
        ("공조(하다)", "(共助) collaboration; cooperation; mutual assistance (to cooperate; to work together)", "북핵문제에 대응하기 위하여 한국, 미국, 일본 세 나라가 공조하기로 했습니다.", "협조"),
        ("구석구석", "nook and cranny; every corner of; every part of", "저는 주말마다 집안 구석구석을 청소합니다."),
        ("대량살상무기", "(大量殺傷武器) weapons of mass destruction (WMD)", ""),
        ("독점(하다)", "(獨占) monopoly (to monopolize; to have a monopoly)", "그 회사는 휴대폰 칩을 독점 공급합니다."),
        ("딛고 일어나다", "to overcome; “to take a step and get up”", "그 사람은 젊은 시절의 어려움을 딛고 일어나서 크게 성공을 했습니다.", "극복하다"),
        ("무상원조", "(無償援助) aid; “free aid”", "한국전쟁 직후 한국은 미국으로부터 무상원조를 받았습니다."),
        ("번영(하다)", "(繁榮) prosperity (to prosper)", "저는 우리나라가 경제적으로 번영하기를 바랍니다.", "융성"),
        ("보완적", "(補完的) complementary", "사교육은 공교육의 부족한 부분을 채워 주는 상호 보완적 역할을 해야 합니다.", "보충적"),
        ("비약적", "(飛躍的) leaping; rapid; remarkable; swift", "한국은 천구백칠십 년대 이후 비약적인 경제성장을 이룩했습니다."),
        ("성숙하다", "(成熟) to be mature", "그 아이는 나이에 비해 아주 성숙합니다."),
        ("성취(하다)", "(成就) achievement; accomplishment (to achieve; to accomplish)", "목표한 것을 꼭 성취하시기 바랍니다.", "이루다"),
        ("시너지효과", "(效果) synergy effect", "그 두 회사의 결합으로 시너지효과를 거둘 것으로 기대됩니다."),
        ("식민지", "(植民地) a colony", "우리 할머니는 힘겹게 식민지 시대를 사셨습니다."),
        ("역군", "(役軍) working force; a mainstay; a pillar; an active worker", "젊은이들은 우리 사회의 역군입니다.", "일꾼"),
        ("원동력", "(原動力) driving force; impetus", "이 나라는 풍부한 자원이 경제의 원동력입니다."),
        ("인적자원", "(人的資源) human resources", "우리나라는 우수한 인적자원이 풍부합니다.", "인력, 교육인적자원부"),
        ("인접성", "(隣接性) proximity", "이 아파트는 서울과 인접성이 좋아서 인기가 많습니다.", "근접성"),
        ("입각하다", "(立脚) to be based on; to be grounded in", "이 이야기는 제 경험에 입각한 것입니다.", "기초하다"),
        ("저탄소", "(低炭素) low carbon", "저탄소 녹색성장은 우리의 미래입니다."),
        ("지리적", "(地理的) geographical", "이곳은 대형 마트가 들어서기에 좋은 지리적 조건을 갖추고 있습니다."),
        ("창출(하다/되다)", "(創出) creation (to create/to be created)", "정부는 일자리를 창출하기 위해 노력하고 있습니다.", "만들다"),
        ("초석", "(礎石) a cornerstone; foundation; basis; “foundation stone”", "이번 계약은 수출 시장을 넓히는 데 초석이 될 것입니다."),
        ("축적(하다/되다)", "(蓄積) accumulation; building up (to build up/to be accumulated)", "책을 많이 읽으면 많은 지식을 축적할 수 있습니다."),
        ("테러리즘", "terrorism", "구일일 이후 전 세계에서 테러리즘에 대한 우려가 높아졌습니다."),
        ("파급(되다)", "(波及) spreading; ripple (to spread; to ripple)", "이 사건의 파급효과가 아주 큽니다.", "파급효과"),
        ("폐허", "(廢墟) ruins", "이 도시는 전쟁으로 폐허가 되었습니다."),
        ("활력을 불어넣다", "(活力) to vitalize; to stimulate; to galvanize; “to blow vitality into”", "수출이 증가하면 국가 경제에 활력을 불어넣을 것입니다."),
    ]),
    ("학습활동 2", [
        ("개도국", "(開途國) a developing country", "빠른 시간에 경제 발전을 이룩한 우리나라는 많은 개도국에게 좋은 모델이 되고 있습니다.", "개발도상국, 선진국, 후진국"),
        ("공통인식", "(共通認識) common recognition; common awareness", "역사적 사실에 대한 각 국가간의 공통인식을 마련하기 위하여 이번 포럼을 주최하게 됐습니다."),
        ("국력", "(國力) national power", "경제력뿐 아니라 인구수도 국력입니다."),
        ("국운", "(國運) national fortunes; fate of a country", "저는 에프티에이 협상이 우리나라의 국운에 긍정적인 영향을 미칠 것이라고 생각합니다."),
        ("굵직(굵직)하다", "to be important; to be weighty; to be big; to be bulky; “to be thick and big”", "당근을 굵직굵직하게 써세요. 즉시 해결해야 할 굵직굵직한 문제들이 많습니다."),
        ("기아", "(飢餓) famine; starvation", "아직도 아프리카에서는 기아에 허덕이는 아이들이 많습니다."),
        ("방향타를 잡다", "(方向舵) (idiom) to play a major role; “to grab the rudder”", "야당에서 개혁의 방향타를 잡고 주도적인 역할을 하고 있습니다."),
        ("변방", "(邊方) a frontier; a border area", "저는 우리나라가 이제 세계의 변방에 있다고 생각하지 않습니다."),
        ("빈곤", "(貧困) poverty", "세계적으로 절대 빈곤에 시달리는 인구가 몇 퍼센트나 됩니까?", "부유, 가난"),
        ("수렴하다", "(收斂) to collect; to gather", "국민의 의견을 수렴해서 정책에 반영하겠습니다.", "모으다, 수집하다"),
        ("원년", "(元年) the first year", "정부는 올해를 한국 외교의 원년으로 선포했습니다."),
        ("위상", "(位相) status", "올림픽 개최로 한국의 위상이 많이 올라갔습니다.", "위치"),
        ("융성(하다)", "(隆盛) prosperity (to be prosperous)", "불교는 오랫동안 우리나라에서 융성했습니다.", "번영"),
        ("이해", "(利害) interests; “interests and damages”", "이 문제에 대한 양국간의 이해가 충돌하고 있습니다."),
        ("절호의 찬스", "(絶好) a golden opportunity", "싸게 유럽 여행을 할 수 있는 절호의 찬스를 놓치지 마세요."),
        ("현안", "(懸案) a pending issue", "여야 의원들은 경제 현안을 해결해야 한다는 데 의견을 함께 했습니다."),
    ]),
    ("학습활동 3", [
        ("각축", "(角逐) intense competition; fierce competition", "이번 경기에서 두 나라의 각축이 예상됩니다."),
        ("강경(하다)", "(强硬) firmness; toughness (to be firm; to be tough)", "한미 양국은 북한에 대해 강경한 입장을 취하고 있습니다."),
        ("교류(하다)", "(交流) exchange (to exchange)", "이십일 세기에 국가간 문화 교류가 활발해지고 있습니다."),
        ("권력", "(權力) power; authority", "권력을 남용하지 마세요."),
        ("기틀", "framework; foundation; groundwork; basis", "동남아의 많은 국가들이 경제 발전의 기틀을 마련하고 있습니다.", "기반"),
        ("긴장감", "(緊張感) tension", "긴장감이 돌다"),
        ("길을 트다", "(idiom) to pave the way; “to open a road”", "본격적으로 한미교류의 길이 트인 것이 언제입니까?"),
        ("누그러뜨리다", "to soften; to appease; to pacify", "저는 너무 흥분해서 화를 누그러뜨리지 못했습니다."),
        ("대담하다", "(大膽) to be bold; to be brave", "범인은 대낮에 물건을 훔치며 대담하게 범죄를 저질렀습니다."),
        ("보위(하다)", "(保衛) preservation and protection (to preserve and protect)", "대통령은 국가를 보위해야 하는 책임이 있습니다.", "보호, 안보"),
        ("분쟁", "(紛爭) a dispute; a conflict", "유엔에서 중동에서의 분쟁을 해결하기 위해 노력하고 있습니다.", "갈등, 다툼"),
        ("세습(하다)", "(世襲) succession/transmission by heredity; passing on power from one generation to another (to pass on power from one generation to another)", "북한은 대대로 자식에게 권력을 세습한다."),
        ("신뢰(하다)", "(信賴) trust; faith; confidence (to put one’s trust in; to have faith in)", "사장님은 이 부장님을 신뢰하고 있습니다.", "믿음"),
        ("옹색하다", "(壅塞) to be hard up; to be poor; to be awkward", "이 문제로 제 입장이 아주 옹색해졌습니다."),
        ("옹졸하다", "(壅拙) to be narrow-minded; to be petty", "그런 사소한 일에 화를 내면 옹졸한 사람으로 보입니다."),
        ("절박하다", "(切迫) to be desperate; to be urgent; to be pressing", "수해를 입은 사람들이 구조를 절박하게 기다리고 있습니다.", "절실하다"),
        ("절실하다/절실히", "(切實) to be desperate; to be urgent/urgently; desperately", "소외된 계층에 대한 배려가 절실히 필요합니다.", "절박하다"),
        ("치명상", "(致命傷) a fatal injury; a deadly wound", "총기사고로 사병 한 명이 치명상을 입었습니다."),
    ]),
]
L7 = lesson(
    "U18 L9 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 공동운명체 · 공유 · 공조 · 독점 · 무상원조 · 번영 · 보완적 · 비약적 · 성취 · 식민지 · 역군 · 원동력 · 인적자원 · 입각 · 창출 · 초석 · 축적 · 파급 · 폐허 · 개도국 · 국력 · 기아 · 변방 · 빈곤 · 위상 · 이해 · 현안 · 각축 · 강경 · 교류 · 권력 · 기틀 · 길을 트다 · 대담 · 보위 · 분쟁 · 세습 · 신뢰 · 옹졸 · 절박 · 치명상",
    requires=[],
    cards=[card("A note on the Korean in this list", "이해 (利害) carries the homonym 이해 (理解), “understanding”. 대담하다 carries the homonym 대담 (對談), “a talk”. The book gives the Hanja of 시너지효과 as 效果 only. 대량살상무기, 테러리즘 and a few others have no example (and, for 테러리즘, no Hanja). 굵직(굵직)하다 has two examples, joined. In examples, “한•미•일” is written 한국, 미국, 일본; “UN” 유엔; “FTA” 에프티에이; “911” 구일일; and the years and centuries are spelled out. The example of 긴장감 is only the phrase 긴장감이 돌다 (“tension is in the air”, my gloss). The book also prints a stray backslash after the gloss of 번영 (prosperity (to prosper)), which I dropped. 활력을 불어넣다 and 방향타를 잡다 are idioms.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=40, nread=34)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 9: Diplomacy (외교)", [L1, L2, L3, L4, L5, L6, L7])

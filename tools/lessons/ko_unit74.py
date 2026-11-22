"""Unit 74: KBC Semester III, Unit 16, Lesson 9 - Societal Corruption (사회 비리).
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
_MATCH9 = [("보상", "compensation", "피해에 대한 보상"), ("모병", "recruiting soldiers", "모병담당자를 만나다"), ("비리", "corruption", "공무원의 비리를 조사하다"), ("징병", "military draft", "징병검사를 받다"), ("병무청", "Military Manpower Administration", "병무청에 문의하다"), ("면제", "exemption", "수업료를 면제 받다"), ("병역", "military service", "병역의무를 마치다"), ("지원", "applying; volunteering", "공군에 지원하다")]
_VERB9 = [("병역의무를", "기피하다", "to avoid the military service duty"), ("공무원의 비리를", "적발하다", "to uncover public officials’ corruption"), ("피해를 입은 농민들을", "보상하다", "to compensate the damaged farmers"), ("나라를", "지키다", "to defend the country"), ("검사결과를", "조작하다", "to fabricate the test results")]
_HJ9 = [("務 무", "work; service", "복무, 의무"), ("兵 병", "soldier; warrior", "병과, 병무청"), ("保 보", "keep; preserve", "보장, 보호"), ("安 안", "safe; peaceful", "안보, 치안"), ("强 강", "strong; strength", "강력, 강화")]
_HJW9 = [("복무", "serving in the military"), ("의무", "obligation; duty"), ("병과", "a branch; a specialty"), ("병무청", "Military Manpower Administration"), ("보장", "guarantee"), ("보호", "protection"), ("안보", "national security"), ("치안", "public security"), ("강력", "mightiness; powerfulness"), ("강화", "strengthening; reinforcement")]
_OPP9 = [("안정", "불안", "stability: anxiety"), ("강화", "약화", "strengthening: weakening"), ("징병", "모병", "conscription: recruitment (volunteer)")]
_REL9 = [("A", "근무", "업무, 직장, 복무", "work: duties, workplace, military service"), ("B", "병과", "포병, 보병, 공병", "branch: artillery, infantry, engineers"), ("C", "계급", "병장, 상병, 이병", "rank: sergeant, corporal, private")]
_L9X = [("안전", "safety"), ("보존", "preservation"), ("불안", "anxiety; unease"), ("정화", "purification"), ("약화", "weakening"), ("활성화", "activation; revitalization"), ("표준화", "standardization"), ("신병", "a new recruit"), ("사병", "an enlisted soldier"), ("모병", "recruiting volunteers"), ("징병", "conscription"), ("업무", "duties; work"), ("직장", "a workplace"), ("포병", "artillery"), ("보병", "infantry"), ("공병", "engineers"), ("병장", "a sergeant"), ("상병", "a corporal"), ("이병", "a private"), ("계급", "a rank")]
L1 = lesson(
    "U16 L9 · Review: draft and corruption words and Sino-Korean 務 兵 保 安 强",
    "사회 비리 · 단어 복습 · 한자어 복습 · 보상 · 모병 · 비리 · 징병 · 병무청 · 면제 · 병역 · 지원 · 務 兵 保 安 强",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives eight phrases with one word underlined and asks you to connect each underlined word with its English meaning on the right. The underline is not marked in the text; the pairs are:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH9], say=[0, 2])]),
        card("단어 복습 2: the verbs (my answers)", "Connect the phrase on the left with the verb that can be used with it on the right (the verbs are 보상하다, 적발하다, 조작하다, 기피하다 and 지키다):", tables=[table(["Phrase", "Verb (my answer)", "Meaning"], [list(r) for r in _VERB9], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ9], say=[2]), ktable(_HJW9)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 안정: 안전, 보존, 불안, 병역; B. 강화: 정화, 약화, 활성화, 표준화; C. 징병: 신병, 사병, 모병, 병역).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP9], say=[0, 1])]),
        card("한자어 복습 2: the related word (my answers)", "Choose from the box (계급, 병과, 모병, 강화, 근무) the word most related to the three words on the right; 모병 and 강화 are left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Why"], [list(r) for r in _REL9], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L9X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH9], k=3) + _tr(_HJW9, k=3) + _tr(_L9X, k=3) + _tr([(a + " " + b, c) for a, b, c in _VERB9], k=3)
        + [M("What does the syllable 務 (무) mean?", "work; service", ["soldier", "keep", "strong"], "복무."), M("What does the syllable 兵 (병) mean?", "soldier; warrior", ["work", "keep", "safe"], "병과."), M("What does the syllable 保 (보) mean?", "keep; preserve", ["soldier", "work", "strong"], "보호."), M("What does the syllable 安 (안) mean?", "safe; peaceful", ["strong", "keep", "work"], "안보."), M("What does the syllable 强 (강) mean?", "strong; strength", ["safe", "soldier", "work"], "강화."),
           M("Which word is the opposite of 안정?", "불안", ["안전", "보존", "병역"], "Anxiety."), M("Which word is the opposite of 강화?", "약화", ["정화", "활성화", "표준화"], "Weakening."), M("Which word is the opposite of 징병?", "모병", ["신병", "사병", "병역"], "Recruiting volunteers."),
           M("Which word fits 포병, 보병, 공병?", "병과", ["계급", "근무", "강화"], "A branch."), M("Which word fits 병장, 상병, 이병?", "계급", ["병과", "근무", "모병"], "A rank."), M("Which word fits 업무, 직장, 복무?", "근무", ["계급", "병과", "강화"], "Work."),
           F("병역의무를 ___합니다. (to avoid)", "기피", ["보상", "적발"], "기피하다."), F("검찰이 공무원의 비리를 ___했습니다. (to uncover)", "적발", ["조작", "보상"], "적발하다."), F("검사결과를 ___했습니다. (to fabricate)", "조작", ["보상", "지키"], "조작하다."), F("___검사를 받았습니다. (conscription)", "징병", ["모병", "면제"], "징병검사."), F("수업료를 ___받았습니다. (exemption)", "면제", ["보상", "지원"], "면제받다.")]
        + [read_q("병역의무를 마쳤습니다"), read_q("병무청에 문의했습니다"), read_q("공무원의 비리를 조사하고 있습니다"), read_q("공군에 지원했습니다")]
    ),
)

# ================================================================== L2 Part 1
_SPEAK9A = [("요즘 뉴스 중에 비리에 관한 소식이 있었는지 찾아보고 반에서 그 내용에 대해 발표해 보세요.", "Find out whether there has been any news about corruption in the news these days and present its content to the class.")]
L2 = lesson(
    "U16 L9 · Part 1 (도입 학습): kinds of corruption and a speaking prompt",
    "도입 학습 · 비리 · 병역비리 · 의료 · 정치 · 말해 봅시다",
    requires=[],
    cards=[
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK9A)),
        card("Activities left out", "학습활동 1 (Reading): a chart on corruption (© Hankyoreh) where you tick the matching kinds of corruption: corruption related to medical school admission, corruption related to the military draft, corruption related to hospital bills and corruption related to medical malpractice. 학습활동 2 (Listening, tracks 001 to 003): news items (MBC, YTN) on various kinds of corruption; you tick the type (politics, economics, education or employment). 학습활동 3 (Listening, track 004): a YTN video in which a candidate for prime minister and a member of the National Assembly argue over whether the money the candidate received was a bribe, with a table of the assemblyman’s accusation and the candidate’s defense. They are charts, video or audio."),
    ],
    exercises=uniq(
        _tr([("권력", "power; authority"), ("비리", "corruption; irregularity"), ("인척", "relatives by marriage"), ("임기", "term in office"), ("병역비리", "military-draft corruption"), ("교육비리", "education corruption"), ("행정비리", "administrative corruption")], k=3)
        + [M("What is 비리?", "Corruption; irregularity", ["A law", "A prize", "A school"], "비리."), M("What is 임기?", "A term in office", ["A birthday", "A holiday", "A salary"], "임기."), M("What is 병역비리?", "Military-draft corruption", ["A military band", "A rank", "A uniform"], "병역비리.")]
        + [read_q("요즘 뉴스 중에 비리에 관한 소식이 있었습니까"), read_q("비리에 대한 소식을 발표해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("권력", "(權力) power; authority", "권력을 남용하지 마세요."),
        ("부실(하다)", "(不實) being weak; being sickly (to be weak; to be sickly)", "너 몸이 그렇게 부실해서 군대에 갈 수 있겠니? 건물이 무너지는 사고의 원인은 보통 부실한 기초공사 때문이다."),
        ("비리", "(非理) corruption; irregularity", "검찰이 병역비리에 대해 수사를 강화하겠다고 발표했습니다.", "교육비리, 행정비리, 병역비리"),
        ("인사", "(人事) personnel matters", "저에게 인사권을 주십시오."),
        ("인척", "(姻戚) relatives by marriage", "대통령과 친인척 관계에 있는 사람들을 다 조사 중입니다.", "친척"),
        ("임기", "(任期) term in office", "서울 시장의 임기가 몇 년입니까?"),
        ("자사고", "(自私高) an autonomous private high school; short form of 자율형 사립 고등학교", ""),
    ]),
    ("학습활동 2", [
        ("대가성", "(代價性) (something) that serves to induce favors in return", "우리가 선생님께 드린 선물은 절대로 대가성이 아니다."),
        ("녹취록", "(錄取錄) a deposition; a statement or testimony", ""),
        ("비자금", "(秘資金) secret fund; slush fund", "그 회사 대표는 유정환 의원에게 비자금을 건네준 혐의로 조사를 받고 있다."),
        ("소환(하다)", "(召喚) summons; citation (to summon; to cite)", "검찰은 대통령의 형을 소환해 조사하겠다고 했습니다."),
        ("차명계좌", "(借名計座) a bank account under an assumed name", "그는 차명계좌로 현금을 이체했습니다.", "실명계좌"),
        ("횡령(하다)", "(橫領) embezzlement (to embezzle)", "그는 공금횡령 혐의로 삼 년 형을 선고 받았습니다."),
        ("후원금", "(後援金) donation; contribution; “supporting money”", "그 정치인은 기업에 후원금을 요청했습니다.", "기부금"),
    ]),
    ("학습활동 3", [
        ("발령(하다)", "(發令) appointment; assignment (to appoint; to assign)", "아버지가 지방으로 발령을 받으셔서 온 가족이 이사를 가야 해요.", "임명하다"),
        ("법인", "(法人) corporate; a corporation", "한국 피자는 이번에 해외법인을 설립하였습니다."),
        ("사라지다", "to disappear; to vanish", "이제 마지막 희망마저 사라졌어요.", "없어지다"),
        ("수당", "(手當) extra pay; a bonus", "기본 월급 이외에 가족 수당, 야근 수당이 지급된다. 월급은 적으나 판매량에 따른 수당을 준다."),
    ]),
]
L3 = lesson(
    "U16 L9 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 권력 · 부실 · 비리 · 인사 · 인척 · 임기 · 자사고 · 대가성 · 녹취록 · 비자금 · 소환 · 차명계좌 · 횡령 · 후원금 · 발령 · 법인 · 사라지다 · 수당",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book adds under 인사 (人事) “personnel matters” that 인사 (人士) means “a public figure” and 인사 is also “greeting”. The book’s example for 횡령 has 3년 (written 삼 년 here). The book has no example for 녹취록 and 자사고 (its note says it is a short form of 자율형 사립 고등학교). The two examples of 부실 and of 수당 are joined here.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=12, nread=10)),
)

# ================================================================== L4 Part 2
_CPI9 = [
    ("한국 반부패지수 세계 삼십구 위, 이 년째 청렴도 하락", "(Headline) Korea’s anti-corruption index 39th in the world; integrity falls for the second year"),
    ("한국이 국제 부패 지수 비교에서 삼십구 위에 머물며 이 년째 하락하는 추세를 보였다.", "Korea stayed at 39th in the international corruption index comparison and showed a falling trend for the second year."),
    ("독일 베를린에 있는 국제투명성기구의 이천십 년 국가별 부패인식지수에서 한국은 십 점 만점에 오 점 사 점으로 백칠십팔 개국 중 삼십구 위에 머물렀다.", "In the 2010 Corruption Perceptions Index (CPI) by country of Transparency International, based in Berlin, Germany, Korea stayed at 39th among 178 countries with 5.4 out of 10 points."),
    ("올해 일 위는 구 점 삼 점을 얻은 뉴질랜드와 덴마크, 싱가포르가 공동으로 차지했다.", "This year first place was shared by New Zealand, Denmark and Singapore, which got 9.3 points."),
    ("반면 소말리아는 일 점 일 점으로 지난해에 이어 최하위를 차지했고, 뒤를 이어 아프가니스탄과 미얀마가 일 점 사 점, 그리고 이라크가 일 점 오 점으로 하위그룹을 차지했다.", "On the other hand, Somalia took last place for the second year with 1.1 points, followed by Afghanistan and Myanmar with 1.4 points and Iraq with 1.5 points in the bottom group."),
    ("우리나라는 이천오 년 오 점대로 진입한 후, 이천팔 년에 오 점 육 점으로 올라섰으나 두 해 연속 영 점 일 점씩 점수가 하락했다.", "Our country entered the 5-point range in 2005 and rose to 5.6 points in 2008, but its score has fallen by 0.1 point each for two years running."),
    ("이에 대해 한국투명성기구는 성명을 통해, 최근 이 년에서 삼 년간 나타난 우리 사회의 부패 불감 현상과 무관하지 않다.", "In response, Transparency International Korea said in a statement that it is not unrelated to the phenomenon of insensitivity to corruption in our society over the last two to three years."),
    ("연일 터져 나오는 교육비리와 특권층 비리는 물론, 고위 공직자 자녀의 채용비리, 사정기관의 부패 스캔들, 대통령의 사면권 남용 등이 우리 사회 전반의 부패 현실을 반영하고 있음이 명백하다고 지적했다.", "It pointed out that it is clear that education corruption and privileged-class corruption that burst out day after day, as well as hiring corruption involving the children of high-ranking public officials, corruption scandals in inspection agencies and the president’s abuse of the pardon power, reflect the reality of corruption across our society."),
    ("또 이명박 정권의 친기업 정책으로 인한 윤리의식의 실종은 관행적 부패가 온존한 우리사회에 지능형 부패가 창궐할 수 있는 조건을 가져왔다고 하락 추세가 지속될 것을 우려하였다.", "It also worried that the downward trend would continue, saying that the disappearance of ethical consciousness due to the Lee Myung-bak administration’s pro-business policy has brought the conditions for intelligent corruption to run rampant in our society, where customary corruption remains intact."),
]
_SPEAK9B = [("미국에서 화제가 되고 있는 비리에 어떤 것이 있는지 이야기해 보세요.", "Talk about what corruption is a hot topic in the United States."), ("미국에서는 합법적으로 로비스트들이 활동하고 있습니다.", "In the United States lobbyists operate legally."), ("로비스트들로 인해 정부 정책에 많은 영향을 미치는 것에 대해 어떻게 생각하는지 반에서 토론해 보세요.", "Discuss in class what you think about lobbyists having a great influence on government policy.")]
L4 = lesson(
    "U16 L9 · Part 2 (본 학습): Korea’s Corruption Perceptions Index",
    "본 학습 · 부패인식지수 · 국제투명성기구 · 청렴도 · 교육비리 · 채용비리 · 사면권 · 로비스트 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): Korea’s political transparency",
             "The following is a newspaper article on political transparency in Korea (text and image © Kyunghyang). The text is the book’s with the numbers spelled out (39위 → 삼십구 위; 10점 만점에 5.4점 → 십 점 만점에 오 점 사 점; 178개국 → 백칠십팔 개국; 2005년 → 이천오 년 and so on), the Hanja 反 written as 반, the quotation marks removed, and the brackets (Transparency International 독일 베를린) and (Corruption Perceptions Index, CPI) left out (they are in the English). The English is mine; the statement’s quotation, split in two sentences, is marked by “said … pointed out” in the English.",
             examples=passage(_CPI9)),
        card("학습활동 1: the questions answered (mine)",
             "1. B — most European countries have higher CPI scores than Korea (the article does not state this; it says that Korea is 39th while New Zealand, Denmark and Singapore share first place, and none of the other choices fits). The other choices are false: Korea’s score is falling (A), war-torn countries are at the bottom (C), and the government’s policies are blamed (D).\n\n"
             "2. The reasons mentioned for the changes: educational corruption (교육비리); corruption in employment (hiring corruption involving the children of high-ranking officials); and abuse of power (the president’s abuse of the pardon power). The others (unlawful election, congressmen’s slush fund, embezzlement by public servants) are not mentioned in the article."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK9B)),
        card("Activities left out", "학습활동 2 (Listening, track 005): a YTN news item on military corruption: which irregularity was caught and who was involved, the itemized expenses of the construction company and what they revealed, what 53-year-old Byun did, and whether anyone was arrested. 학습활동 3 (Listening, track 006): part of an MBC documentary on a corruption: what kind it was and who is involved, the interviewee’s reaction (A. patient; B. confident; C. supportive; D. flustered), what happened in 2005, and what the reporter implies or hopes for in the future. They are video or audio."),
    ],
    exercises=uniq(
        _tr(_CPI9, k=3) + _tr(_SPEAK9B, k=3)
        + [M("What body publishes the Corruption Perceptions Index?", "Transparency International", ["The United Nations", "The Bank of Korea", "A Korean newspaper"], "국제투명성기구."), M("Where did Korea rank in the 2010 index?", "39th", ["1st", "9th", "178th"], "삼십구 위."), M("How many countries were ranked?", "178", ["39", "100", "10"], "백칠십팔 개국."), M("Which countries shared first place?", "New Zealand, Denmark and Singapore", ["Korea and Japan", "Somalia and Iraq", "China and India"], "뉴질랜드와 덴마크, 싱가포르."), M("Which country took last place?", "Somalia", ["Iraq", "Myanmar", "Afghanistan"], "소말리아."), M("What did Transparency International Korea blame?", "Insensitivity to corruption and incidents of corruption in society", ["A war", "A flood", "A new law"], "부패 불감 현상."), M("What did the group say about the president?", "That he abused the pardon power", ["That he resigned", "That he won a prize", "That he traveled abroad"], "사면권 남용."),
           F("한국은 십 점 ___에 오 점 사 점이었다. (perfect score)", "만점", ["평균", "최하"], "만점."), F("부패 ___ 현상과 무관하지 않다. (insensitivity)", "불감", ["인식", "청렴"], "부패 불감."), F("고위 공직자 자녀의 ___비리가 있었다. (hiring)", "채용", ["입시", "병역"], "채용비리."), F("대통령의 사면권 ___ (abuse)", "남용", ["사용", "활용"], "남용."), F("지능형 부패가 ___할 수 있는 조건. (to run rampant)", "창궐", ["진입", "반영"], "창궐하다.")]
        + [read_q("한국은 이 년째 청렴도가 하락했습니다"), read_q("연일 교육비리가 터져 나옵니다"), read_q("대통령의 사면권 남용이 문제가 되었습니다"), read_q("미국의 로비스트에 대해 어떻게 생각합니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("무관하다", "(無關) to be unrelated; to be unconnected", "저는 그 사건과 무관합니다."),
        ("반영(하다)", "(反映) reflection (to reflect; to apply)", "이 영화는 우리 사회의 현실을 잘 반영하고 있습니다."),
        ("부패(하다)", "(腐敗) corruption; decomposition (to be corrupt; to rot; to decompose)", "중국 정부는 부패 공무원에 대해 엄중한 처벌을 하고 있습니다."),
        ("사정기관", "(司正機關) an inspection agency", "국세청 등 사정기관에서 정치인을 상대로 조사를 벌이고 있습니다."),
        ("우려(하다)", "(憂慮) concern; worry; fear (to be concerned; to worry; to fear)", "국민들은 부패 선거에 대해 우려하고 있습니다."),
        ("지능", "(知能) intelligence; intellect", "요즘은 인공지능을 이용한 가전제품이 많습니다."),
        ("진입(하다)", "(進入) entry (to enter; to penetrate)", "우리나라는 올림픽에서 십 위권 내에 진입했습니다."),
        ("창궐(하다)", "(猖獗) being rampant (to rage [on]; to be rampant)", "전염성 유행병인 콜레라가 창궐하고 있다."),
    ]),
    ("학습활동 2", [
        ("건설업체", "(建設業體) a construction business", "건설붐이 일면서 건설업체들이 늘고 있습니다."),
        ("구속영장", "(拘束令狀) an arrest warrant", "검찰은 피의자에 대해 구속영장을 신청했습니다."),
        ("금품", "(金品) money and valuables", "그 정치인은 금품 수수 혐의로 구속되었습니다."),
        ("뇌물", "(賂物) a bribe", "공무원들이 뇌물을 받은 것으로 드러났습니다."),
        ("불구속 입건", "(不拘束 立件) charging (a suspect) without detaining", "경찰은 사건 관계자 중 두 명은 구속하고 한 명은 불구속 입건했습니다."),
        ("상납(하다)", "(上納) bribing (to bribe; to offer a bribe)", "정기적으로 금품을 상납 받은 경찰이 구속되었습니다."),
        ("압수(하다/되다)", "(押收) confiscation; seizure (to confiscate/to be confiscated)", "경찰은 증거물로 차를 압수했습니다."),
    ]),
    ("학습활동 3", [
        ("떡값", "bribe money; “money for rice cakes”", "경찰은 수백만 원의 떡값을 받았습니다."),
        ("부인하다", "(否認) denial (to deny)", "피의자는 범행 사실을 부인하고 있습니다."),
        ("부적절하다", "(不適切) to be inappropriate", "그 음악은 이런 분위기에는 부적절한 것 같아요."),
        ("스폰서", "a sponsor; a person who gives someone money expecting something in return (such as a favor or being a companion)", "그 배우는 스폰서가 있다는 소문이 있어요."),
        ("외면(하다)", "(外面) looking away; ignoring (to look away from; to ignore)", "진실을 외면하지 말고 직시하세요."),
        ("접대(하다)", "(接待) entertaining (to entertain, [usually with food and alcohol])", "검찰이 유흥업소에서 접대를 받은 혐의를 받고 있습니다."),
        ("취재(하다)", "(取才) covering news (to cover news; to collect news)", "오후에는 뉴스 취재하러 가야 해요."),
        ("침묵(하다)", "(沈默) silence (to keep silent; to say nothing)", "침묵하지 말고 의견을 말하세요."),
        ("향응", "(饗應) a (lavish) treat; an entertainment", "그 후보자는 유권자들에게 향응을 베풀었다."),
        ("허물", "a fault; a flaw", "허물을 들춰내지 말고 눈감아 주세요."),
    ]),
]
L5 = lesson(
    "U16 L9 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 무관하다 · 반영 · 부패 · 사정기관 · 우려 · 지능 · 진입 · 창궐 · 건설업체 · 구속영장 · 금품 · 뇌물 · 불구속 입건 · 상납 · 압수 · 떡값 · 부인하다 · 부적절하다 · 스폰서 · 외면 · 접대 · 취재 · 침묵 · 향응 · 허물",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with numbers are written out: 10위권 → 십 위권, 2명 → 두 명 and 1명 → 한 명. The book’s Hanja of 취재 is printed 取才; the usual writing is 取材.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=26, nread=20)),
)

# ================================================================== L6 Part 3
_ED9 = [
    ("사설 끊이지 않는 병역 비리, 근본 대책 필요하다", "(Heading) Editorial: Military-draft corruption that does not stop; fundamental measures are needed"),
    ("없는 병을 만들어 내 병역을 회피하려는 병역 비리 사건이 잇따라 발각됐다.", "(Paragraph 1) Cases of military-draft corruption, in which people invent illnesses to avoid military service, have been discovered one after another."),
    ("수법도 기기묘묘하다.", "The methods are also strange and wondrous."),
    ("희귀 질병을 앓고 있는 사람으로 하여금 병원 진료를 대신 받게 하는 환자 바꿔치기 따위 신종 수법이 나왔고, 멀쩡한 어깨를 훼손해 탈구 수술을 받는 해묵은 수법도 동원됐다.", "New methods such as “patient swapping,” in which a person suffering from a rare disease is made to receive hospital treatment in one’s place, have appeared, and the old method of damaging a healthy shoulder to get dislocation surgery was also used."),
    ("인터넷을 통해 병역 면제나 신체검사 일정 연기를 주선하고 돈을 받는 전문 조직까지 적발됐다.", "Even a professional organization that arranges military exemption or postponement of the physical examination through the Internet and takes money was uncovered."),
    ("비리가 근절되기는커녕 거의 매년 빠짐없이 반복되는데다 그 수법까지 날로 진화하고 있는 꼴이다.", "Far from being eradicated, the corruption is repeated almost every year without fail, and its methods are evolving day by day."),
    ("병역 비리가 근절되지 않는 것은, 병역 회피를 특권인 양 여기고 병역을 마치는 것을 오히려 손해라고 보는 풍조 탓이 크다.", "(Paragraph 2) The reason military-draft corruption is not eradicated is largely the trend of regarding evasion of military service as a privilege and regarding finishing military service as rather a loss."),
    ("그 일차적 책임은 일부 공직자나 부유층 등에 있다.", "The primary responsibility lies with some public officials and the wealthy."),
    ("이천삼 년에서 이천팔 년 적발된 병역 비리 혐의자 가운데 그렇게 분류될 수 있는 사람이 전체의 육십 퍼센트 정도였다.", "Among the suspects of military-draft corruption uncovered between 2003 and 2008, people who could be classified that way were about 60 percent of the total."),
    ("이번 비리에서도 예외 없이 그런 사람들이 거론된다.", "In this corruption case too, such people are mentioned without exception."),
    ("설령 위법은 아닐지라도 고위 공직자의 상당수는 자신이나 아들이 병역 면제자이기도 하다.", "Even if it is not illegal, a considerable number of high-ranking public officials are themselves or have sons who are exempt from military service."),
    ("이명박 대통령을 비롯해 정운찬 국무총리 후보자, 정정길 대통령실장, 원세훈 국가정보원장 등 한둘이 아니다.", "Beginning with President Lee Myung-bak, there are more than one or two, such as the prime minister nominee Chung Un-chan, the presidential chief of staff Chung Chung-gil and the National Intelligence Service director Won Sei-hoon."),
    ("병무청 통계로는 장차관급 인사의 십일 퍼센트, 여야 국회의원의 십팔 퍼센트가 병역 면제자라고 한다.", "According to Military Manpower Administration statistics, 11 percent of ministerial and vice-ministerial-level figures and 18 percent of ruling and opposition lawmakers are exempt from military service."),
    ("대다수 병역 의무 대상자들로선 상대적 박탈감을 느끼지 않을 도리가 없다.", "For the great majority of those subject to military duty, there is no way not to feel a sense of relative deprivation."),
    ("기회가 되면 어떻게든 군복무를 피하려는 분위기는 이런 토양에서 배태된 것이다.", "The atmosphere of trying to avoid military service by any means when there is a chance was bred in this soil."),
    ("공직자나 부유층의 병역 면탈 행위는 사회통합을 저해하는 걸림돌이다.", "(Paragraph 3) Evasion of military service by public officials and the wealthy is a stumbling block that hinders social integration."),
    ("그동안에도 이들 계층의 병역 의무를 관리하기 위한 특별한 법적, 제도적 장치 마련이 거론됐지만, 번번이 제대로 논의조차 되지 않은 채 흐지부지됐다.", "In the meantime too, the preparation of special legal and institutional devices to manage these classes’ military duty was brought up, but every time it fizzled out without even being properly discussed."),
    ("이번 기회마저 놓친다면 병역 비리는 영영 치유하기 어렵게 될 것이다.", "If even this opportunity is missed, military-draft corruption will become hard to cure forever."),
]
_SPEAK9C = [("군가산점 제도에 대한 자신의 의견에 대해 친구와 토론해 보세요.", "Discuss your opinion on the system of additional points for military service with a friend."), ("지금 한국의 군은 징병제로 유지되고 있습니다.", "Korea’s military is now maintained by a conscription system."), ("이 제도가 미국처럼 모병제로 바뀌는 것이 더 나은지에 대한 자신의 생각을 말해 보세요.", "Tell what you think about whether it would be better for this system to change to a volunteer system as in the United States.")]
_METH9 = [("1", "“Patient swapping”: having a person with a rare disease receive the medical examination or hospital treatment in one’s place"), ("2", "Damaging a healthy shoulder to get dislocation surgery (an old method)"), ("3", "Paying a professional organization that arranges, through the Internet, military exemption or postponement of the physical examination")]
L6 = lesson(
    "U16 L9 · Part 3 (심화 학습): military-draft corruption",
    "심화 학습 · 병역 비리 · 병역 면제 · 환자 바꿔치기 · 공직자 · 부유층 · 박탈감 · 군가산점 · 징병제 · 모병제 · 공익근무 요원 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 공익근무 요원 제도 (Public Interest Service Personnel) — the book’s note",
             "This alternative military service program is for those whose physical examination scores are low because of poor eyesight, extreme height or weight, etc. It is also for those who have exceptional skills in fields such as computers, arts, or foreign languages. People qualifying for these positions receive 4 weeks of basic training and work for state agencies, local government, public institutions, or social welfare organizations. (Image © Kyunghyang.)"),
        card("학습활동 4 (Reading): a newspaper editorial on military service",
             "The following is a newspaper editorial on military service (© Hankyoreh). The text is the book’s with the numbers spelled out (2003∼08년 → 이천삼 년에서 이천팔 년; 60% → 육십 퍼센트; 11% → 십일 퍼센트; 18% → 십팔 퍼센트), the bracket 사설 written without brackets, the quotation marks removed, 근절되기는 커녕 closed up as 근절되기는커녕 and the middle dot in 법적·제도적 written 법적, 제도적. The editorial names real public officials; the names are the book’s. The English is mine; the paragraph numbers are in the English only.",
             examples=passage(_ED9)),
        card("학습활동 4: the questions answered (mine)",
             "1. The three methods used to avoid military service:",
             tables=[table(["", "Method (mine)"], [list(r) for r in _METH9])]),
        card("학습활동 4: questions 2 and 3 (mine)",
             "2. What makes draftees feel a sense of deprivation (the underlined sentence is not marked in the text; it is the one about relative deprivation): the fact that many high-ranking officials and wealthy people (and their sons) are exempt from military service — about 11 percent of ministerial and vice-ministerial-level figures and 18 percent of lawmakers — while ordinary draftees must serve; they feel it is unfair, and so they too try to avoid service.\n\n"
             "3. What should be done to stop people from avoiding military service: the writer calls for fundamental measures — above all, putting special legal and institutional devices in place to manage the military duty of public officials and the wealthy (the primary responsible group), and not letting this opportunity slip as earlier attempts did, which fizzled out without proper discussion."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK9C)),
        card("Activities left out", "학습활동 1 (Listening, track 007): a YTN news item on the singer MC Mong: what he is suspected of and what his agent has said about the issue. 학습활동 2 (Listening, track 008): a YTN news item on military-draft corruption: the scheme described and how it is done, the specific place targeted in the investigation of the draft dodgers and why, and what the report says about the future of the investigation. 학습활동 3 (Listening, track 009): a YTN news item on military service: two issues discussed (primary benefits for those serving in the military; a 2.5 percent increase in points granted for those serving; the unconstitutionality of granting additional points; extension of service length for people involved in military corruption), and a true-or-false exercise on the MMA’s countermeasures, the Supreme Court’s ruling and public opinion. They are audio."),
    ],
    exercises=uniq(
        _tr(_ED9, k=3) + _tr(_SPEAK9C, k=3)
        + [M("Who is the 공익근무 요원 program for?", "Those with low exam scores or exceptional skills", ["Only generals", "Only foreigners", "Only students"], "The book’s note."), M("How long is the basic training for 공익근무 요원?", "4 weeks", ["1 day", "1 year", "10 years"], "The book’s note."), M("What new method of avoiding military service is mentioned?", "Patient swapping", ["Moving abroad", "Changing names", "Bribing a teacher"], "환자 바꿔치기."), M("What is the editorial’s main reason for corruption continuing?", "The trend of regarding evasion as a privilege", ["Lack of soldiers", "Low salaries", "New laws"], "병역 회피를 특권인 양 여기는 풍조."), M("Who has the primary responsibility, according to the editorial?", "Some public officials and the wealthy", ["Doctors", "Students", "Teachers"], "일부 공직자나 부유층."), M("What share of those found to be corruption suspects were such people?", "About 60 percent", ["About 6 percent", "About 16 percent", "About 90 percent"], "육십 퍼센트."), M("What do most draftees feel?", "A sense of relative deprivation", ["Pride", "Joy", "Boredom"], "상대적 박탈감."), M("What does the editorial call evasion of service by officials and the wealthy?", "A stumbling block to social integration", ["A tradition", "A necessity", "A reward"], "사회통합을 저해하는 걸림돌."),
           F("병역 비리가 ___ 발각됐다. (one after another)", "잇따라", ["천천히", "전혀"], "잇따라."), F("비리가 근절되기는___ 매년 반복된다. (far from)", "커녕", ["처럼", "마저"], "근절되기는커녕."), F("대다수는 상대적 ___을 느낀다. (deprivation)", "박탈감", ["책임감", "자긍심"], "박탈감."), F("법적, 제도적 장치 마련이 번번이 ___됐다. (fizzled out)", "흐지부지", ["성공", "시작"], "흐지부지."), F("병역 비리는 ___ 치유하기 어렵게 될 것이다. (forever)", "영영", ["빨리", "가끔"], "영영.")]
        + [read_q("병역 비리 사건이 잇따라 발각되었습니다"), read_q("병역 회피를 특권처럼 여기는 풍조가 문제입니다"), read_q("군가산점 제도에 대해 어떻게 생각합니까"), read_q("징병제와 모병제 중 어느 것이 더 낫습니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("해명하다", "(解明) to clarify", "시민 단체는 이 사건에 대한 해명을 요구하고 있습니다.", "설명하다"),
    ]),
    ("학습활동 2", [
        ("고의로", "(故意) on purpose; intentionally", "피의자는 고의로 차를 부순 것으로 밝혀졌습니다.", "일부러"),
        ("멀쩡하다", "to be intact; to be unscathed", "왜 멀쩡한 옷을 버리니? 앞으로 삼 년은 더 입겠다."),
        ("시인하다", "(是認) to admit", "피고는 유죄를 시인했습니다.", "인정하다"),
        ("입영", "(入營) joining the military", "얼마 전에 입영 통지서를 받았습니다.", "입대"),
        ("짜다", "to conspire", "그 사람들은 보험금을 타기 위해 서로 짜고 사고를 냈다."),
        ("탈골", "(脫骨) dislocation; “falling out from bone”", "자꾸 왼팔이 탈골돼서 걱정입니다."),
        ("판정(하다)", "(判定) judgment; decision (to judge; to decide)", "저는 심판의 판정이 잘못되었다고 생각합니다."),
    ]),
    ("학습활동 3", [
        ("가산점", "(加算點) additional points", "정부는 군복무자에 대해 취업시 가산점을 부여하겠다고 발표했습니다."),
        ("엇갈리다", "to be in disagreement; “to cross”", "군가산점 제도에 관해 많은 사람들의 의견이 엇갈리고 있다."),
        ("위헌", "(違憲) violation of the constitution", "헌법재판소가 그 법에 대한 위헌 여부를 심사하고 있다."),
        ("지지하다", "(支持) to support", "저는 그 후보를 지지합니다."),
        ("진땀을 흘리다", "to sweat in a difficult situation; “to shed sticky sweat”", "국방부 장관은 날카로운 질문에 답하느라 진땀을 흘리고 있다."),
        ("질타하다", "(叱咤) to rebuke", "대통령의 새 정책에 대해 질타가 이어지고 있습니다.", "질책하다"),
    ]),
    ("학습활동 4", [
        ("거론하다/되다", "(擧論) to mention; to bring up/to be mentioned; to be brought up", "오늘 모임에서 미국 경제가 거론되었습니다."),
        ("걸림돌", "a stumbling block; an obstacle", "자금 문제가 우리 연구의 걸림돌입니다.", "방해물"),
        ("고위", "(高位) high rank; “high position”", "다음달에 판문점에서 남북 고위급 회담이 열립니다."),
        ("공직자", "(公職者) a public official", "공직자들의 부정부패가 심각합니다.", "공무원"),
        ("근절(하다/되다)", "(根絶) eradication; extermination (to eradicate/to be eradicated)", "검찰은 범죄를 근절하겠다고 발표했습니다.", "없애다"),
        ("박탈감", "(剝奪感) sense of deprivation; feeling deprived", "가난한 사람들은 부자들을 보면 상대적 박탈감을 갖는다."),
        ("영영", "(永永) forever; eternally", "영영 이별이라고 생각하니까 너무 슬픕니다."),
        ("적발(하다/되다)", "(摘發) uncovering; disclosure; exposure (to uncover/to be uncovered)", "특별단속기간 동안 열 건 남짓의 마약 사범이 적발되었다."),
        ("진화(하다/되다)", "(進化) evolution (to evolve/to be evolved)", "의학 기술은 빠른 속도로 진화하고 있습니다."),
        ("치유(하다/되다)", "(治癒) cure; heal (to cure/to be cured)", "요즘은 암도 완전 치유가 가능합니다.", "고치다, 치료하다"),
        ("회피하다", "(回避) to avoid", "그는 기자들의 질문을 회피했습니다.", "기피하다, 피하다"),
        ("흐지부지", "fizzling out; coming to nothing", "우리의 계획은 경제적인 이유로 흐지부지되고 말았습니다."),
    ]),
]
L7 = lesson(
    "U16 L9 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 해명 · 고의 · 멀쩡하다 · 시인 · 입영 · 짜다 · 탈골 · 판정 · 가산점 · 엇갈리다 · 위헌 · 지지 · 진땀 · 질타 · 거론 · 걸림돌 · 고위 · 공직자 · 근절 · 박탈감 · 영영 · 적발 · 진화 · 치유 · 회피 · 흐지부지",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with numbers are written out: 3년 → 삼 년 and 10여 건 → 열 건 남짓. The book’s example for 진화 reads 의학 기술을 빠른 속도로 진화하고 있습니다, a slip for 은; its example for 질타하다 ends 이어지고 있다 and its example for 흐지부지 ends 되고 말았다 (both written in the polite style here).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=26, nread=20)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 9: Societal Corruption (사회 비리)", [L1, L2, L3, L4, L5, L6, L7])

"""Unit 93: KBC Semester III, Unit 18, Lesson 8 - Central and Local Government (중앙정부와 지방자치단체).
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
_MATCH8 = [("도지사", "the governor of a province", "다음 주에 도지사 선거가 있습니다"), ("대통령", "the president (of a nation)", "대통령의 임기가 몇 년입니까"), ("지지", "support", "제가 지지하는 후보가 당선됐어요"), ("후보자", "a candidate", "장관후보자에 대한 청문회가 시작됐어요"), ("보궐선거", "an election to fill a vacancy", "이번 보궐선거의 투표율이 꽤 높았어요"), ("정책", "a policy; political measures", "새 여성정책에 대해 반발이 심합니다"), ("지방자치", "local autonomy", "지방자치단체장 선거를 언제 합니까"), ("기획", "planning (a project)", "이번 행사를 기획한 사람이 누구입니까"), ("임명", "appointing; nominating", "새로 임명된 국무총리가 누구입니까"), ("지휘", "commanding", "검찰이 이번 수사를 지휘하고 있습니다")]
_AUD8 = [("국방부", "the Ministry of National Defense"), ("시청", "a city hall"), ("도청", "a provincial government office"), ("보건복지부", "the Ministry of Health and Welfare"), ("통일부", "the Ministry of Unification")]
_HJ8 = [("官 관", "official; government", "차관, 관공서"), ("權 권", "rights; power; authority", "유권자, 권한"), ("公 공", "public; officials; justice; fairness", "공식적, 공정"), ("政 정", "govern; rule", "정치, 행정"), ("治 치", "govern; control", "법치주의, 지방자치")]
_HJW8 = [("차관", "a vice minister"), ("관공서", "a government/public office"), ("유권자", "a voter"), ("권한", "authority; power"), ("공식적", "official; formal"), ("공정", "fairness; equality"), ("정치", "politics"), ("행정", "administration"), ("법치주의", "rule of law"), ("지방자치", "local autonomy")]
_SIM8 = [("공정", "공평", "fairness: impartiality"), ("재정", "재무", "finance: financial affairs"), ("공식적", "정식", "official: formal"), ("권리", "권한", "a right: authority")]
_ALL8 = [("인권, 노동권, 여권", "권리", "human rights, labor rights, passport rights: rights"), ("경찰관, 장관, 소방관", "공무원", "police officer, minister, firefighter: public officials"), ("재선, 총선, 대선", "선거", "re-election, general election, presidential election: elections"), ("기획재정부, 노동부, 환경부", "정부", "Ministry of Strategy and Finance, Labor, Environment: government")]
_L8X = [("투표권", "the right to vote"), ("정당", "a political party"), ("인권", "human rights"), ("정책", "a policy"), ("사법", "the judiciary"), ("약식", "simplified form"), ("비공식", "unofficial"), ("비공개", "not public"), ("자격", "qualification"), ("재정", "finance (public)"), ("재무", "financial affairs"), ("노동권", "labor rights"), ("여권", "a passport"), ("소방관", "a firefighter"), ("경찰관", "a police officer"), ("대선", "a presidential election"), ("낙선", "losing an election"), ("공무원", "a public official"), ("노동부", "the Ministry of Labor"), ("환경부", "the Ministry of Environment")]
L1 = lesson(
    "U18 L8 · Review: government words and Sino-Korean 官 權 公 政 治",
    "중앙정부와 지방자치단체 · 단어 복습 · 한자어 복습 · 도지사 · 후보자 · 보궐선거 · 정책 · 지방자치 · 임명 · 官 權 公 政 治",
    requires=[],
    cards=[
        card("단어 복습 1: connect the underlined word with its meaning", "The book gives ten sentences with a word underlined and ten English meanings. The underline is not marked in the text; the pairs below are my reading (the sentence “장관후보자에 대한 청문회가 시작됐어요” could point to 후보자 or 청문회; the meaning “a candidate” fits 후보자):", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH8], say=[0, 2])]),
        card("The words of 단어 복습 2", "In the audio activity four clips describe work of central ministries and local governments; you write the letter of the matching body from the box (A–E) and its work. The box words are below; the English is mine:", tables=[ktable(_AUD8)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ8], say=[2]), ktable(_HJW8)]),
        card("한자어 복습 1: the word with a similar meaning (my answers)", "Circle the word closest in meaning to the word on the left (A. 공정: 투표권, 공평, 정책, 인권; B. 재정: 사법, 재무, 권한, 정당; C. 공식(적): 약식, 비공식, 정식, 비공개; D. 권리: 권한, 정당, 차관, 자격).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM8], say=[0, 1])]),
        card("한자어 복습 2: the word that includes all three (my answers)", "Choose from the box (선거, 권리, 낙선, 공무원, 유권자, 정부) the word that includes the three words of each line:", tables=[table(["Three words", "Answer", "Meaning"], [list(r) for r in _ALL8], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L8X)]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001–004): four audio clips on the work of government bodies. They are audio."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH8], k=3) + _tr(_AUD8, k=3) + _tr(_HJW8, k=3) + _tr(_L8X, k=4)
        + [M("What does the syllable 官 (관) mean?", "official; government", ["rights; power", "public; fair", "govern; control"], "차관."), M("What does the syllable 權 (권) mean?", "rights; power; authority", ["official", "public; fair", "govern"], "유권자."), M("What does the syllable 公 (공) mean?", "public; officials; justice; fairness", ["official", "rights", "govern"], "공정."), M("What does the syllable 政 (정) mean?", "govern; rule", ["official", "rights", "public"], "정치."), M("What does the syllable 治 (치) mean?", "govern; control", ["official", "rights", "public"], "지방자치.")
           , M("Which word is similar to 공정?", "공평", ["투표권", "정책", "인권"], "Impartiality."), M("Which word is similar to 재정?", "재무", ["사법", "권한", "정당"], "Financial affairs."), M("Which word is similar to 공식적?", "정식", ["약식", "비공식", "비공개"], "Formal."), M("Which word covers 경찰관, 장관, 소방관?", "공무원", ["유권자", "정부", "선거"], "Public officials."), M("Which word covers 재선, 총선, 대선?", "선거", ["권리", "낙선", "정부"], "Elections."), M("Which word covers 인권, 노동권, 여권?", "권리", ["선거", "공무원", "유권자"], "Rights.")
           , F("다음 주에 ___ 선거가 있습니다. (provincial governor)", "도지사", ["대통령", "후보자"], "도지사."), F("이번 ___선거의 투표율이 꽤 높았어요. (by-election)", "보궐", ["지방", "대통령"], "보궐선거."), F("검찰이 이번 수사를 ___하고 있습니다. (to command)", "지휘", ["기획", "임명"], "지휘하다."), F("새로 ___된 국무총리가 누구입니까? (appointed)", "임명", ["지지", "지휘"], "임명되다.")]
        + [read_q("다음 주에 도지사 선거가 있습니다"), read_q("제가 지지하는 후보가 당선됐어요"), read_q("지방자치단체장 선거를 언제 합니까"), read_q("새로 임명된 국무총리가 누구입니까")]
    ),
)

# ================================================================== L2 Part 1
_MIN8 = [("기획재정부", "the Ministry of Strategy and Finance"), ("교육과학기술부", "the Ministry of Education, Science and Technology"), ("외교통상부", "the Ministry of Foreign Affairs and Trade"), ("통일부", "the Ministry of Unification"), ("법무부", "the Ministry of Justice"), ("국방부", "the Ministry of National Defense"), ("행정안전부", "the Ministry of Public Administration and Security"), ("문화체육관광부", "the Ministry of Culture, Sports and Tourism"), ("농림수산식품부", "the Ministry for Food, Agriculture, Forestry and Fisheries"), ("지식경제부", "the Ministry of Knowledge Economy"), ("보건복지부", "the Ministry of Health and Welfare"), ("환경부", "the Ministry of Environment"), ("고용노동부", "the Ministry of Employment and Labor"), ("여성가족부", "the Ministry of Gender Equality and Family"), ("국토해양부", "the Ministry of Land, Transport and Maritime Affairs")]
_NEWS8 = [
    ("이명박 대통령이 오는 구 일에서 십 일 러시아를 방문해 야로슬라블 세계정책포럼에 참석하고, 드미트리 메드베데프 대통령과 정상회담을 한다고 청와대가 일 일 발표했다.", "The Blue House announced on the 1st that President Lee Myung-bak will visit Russia from the 9th to the 10th to attend the Yaroslavl Global Policy Forum and hold a summit with President Dmitry Medvedev."),
    ("이 대통령은 십 일 제이 차 야로슬라블 포럼 기조연설에서 한국의 민주주의와 경제발전 경험을 소개할 예정이다.", "On the 10th, in his keynote speech at the 2nd Yaroslavl Forum, President Lee is to introduce Korea’s experience of democracy and economic development."),
    ("같은 날 한국과 러시아 정상회담에서는 오는 십일 월 서울 주요 이십 개국 정상회의의 성공적 개최와 에너지와 자원 및 극동시베리아 개발 협력 등에 대해 논의한다.", "At the Korea-Russia summit on the same day, they will discuss the successful hosting of the Group of 20 leading countries summit in Seoul in November, and cooperation in energy and resources and in the development of the Russian Far East and Siberia."),
    ("한국과 볼리비아, 리튬 개발 합의", "Korea and Bolivia agree on lithium development"),
    ("이명박 대통령과 후안 에보 모랄레스 아이마 볼리비아 대통령은 이십육 일 청와대에서 정상회담을 열고 볼리비아 리튬 자원 개발 및 산업화 연구에 한국 기업이 참여하는 데 합의했다.", "President Lee Myung-bak and Bolivian President Juan Evo Morales Ayma held a summit at the Blue House on the 26th and agreed that Korean companies would take part in the development of Bolivia’s lithium resources and research on industrialization."),
    ("세계 최대의 리튬 자원 보유국인 볼리비아 서부에 위치한 우유니 호수에는 세계 리튬 부존량의 절반 가까운 양, 오백사십만 톤이 매장돼 있으며, 자원 개발권을 놓고 한국과 일본, 프랑스, 브라질 등이 경쟁을 벌여 왔다.", "In Lake Uyuni in western Bolivia, the country with the world’s largest lithium resources, an amount close to half of the world’s lithium reserves, 5.4 million tons, is buried, and Korea, Japan, France, Brazil and others have competed for the right to develop the resources."),
    ("김태호 국무총리 후보자가 이십구 일 오전 열 시 자신의 사무실이 있는 광화문의 개인 사무실에서 기자 회견을 열어 후보직에서 자진해서 사퇴하겠다고 밝혔다.", "Prime Minister nominee Kim Tae-ho held a press conference at 10 a.m. on the 29th at his private office in Gwanghwamun and announced that he would voluntarily resign from the nomination."),
    ("신재민 문화관광부 장관 후보자와 이재훈 지식경제부 장관 후보자도 김 후보자의 사퇴 표명 직후 자진 사퇴 뜻을 전한 것으로 알려졌다.", "It is known that Culture and Tourism Minister nominee Shin Jae-min and Knowledge Economy Minister nominee Lee Jae-hoon also conveyed their intention to resign voluntarily right after Kim’s announcement."),
    ("이명박 대통령은 세 사람의 사퇴 의사를 전달받고 이를 수용한 것으로 전해졌다.", "President Lee Myung-bak is reported to have received and accepted the three people’s intention to resign."),
]
_SPEAK8 = [("미국 연방 정부에는 어떤 부처들이 있는지 이야기해 보고 각 부처의 대표적인 활동이 무엇인지 이야기해 보세요.", "Tell what ministries (departments) there are in the US federal government and tell what the representative activities of each are.")]
L2 = lesson(
    "U18 L8 · Part 1 (도입 학습): ministries, summits and a nominee’s resignation",
    "도입 학습 · 정부 부처 · 인사청문회 · 정상회담 · 기조연설 · 리튬 · 후보자 사퇴 · 기자회견 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 정부 부처와 인선 과정", "The book’s note (in English): newly elected presidents routinely restructure and rename ministries and appoint new ministers and chiefs, so the ministry names in this lesson may be valid for only a few years; long names are shortened, as in 농림부 for 농림수산식품부. The prime minister recommends candidates for each position and the president nominates them; the National Assembly then holds a confirmation hearing (인사청문회) to judge whether the nominee is qualified, with particular interest in the candidate’s ethical background; if the nominee is approved, the president officially appoints him or her with a certificate of appointment. The chart of the book shows the president, the prime minister and these ministries (the English names are mine):", tables=[ktable(_MIN8)]),
        card("학습활동 4: news about the president and the executive (Hankyoreh)", "The book asks you to fill a table (participants in the summit talks and topics discussed) for two news items, and to answer two questions about the third: the official titles of the three named people and why they are in the news, and what the president is expected to do about them. The numbers are spelled in Hangul and “9~10일” as 구 일에서 십 일. The persons named are the public officials of the news. The news, with my English:", examples=passage(_NEWS8)),
        card("My answers to 학습활동 4", "Table, news 1: participants: President Lee Myung-bak and Russian President Medvedev; topics: the successful hosting of the Seoul G20 summit and energy, resource and Far East Siberian development cooperation (and Lee’s keynote speech at the Yaroslavl Forum on Korea’s democracy and economic development). News 2: participants: President Lee and Bolivian President Morales; topic: participation of Korean companies in developing Bolivia’s lithium and researching its industrialization. Questions: A. 김태호 was the Prime Minister nominee, 신재민 the nominee for Minister of Culture and Tourism and 이재훈 the nominee for Minister of Knowledge Economy; they are in the news because they announced that they would resign their nominations voluntarily. B. The president is expected to accept their resignations (the article says he has received and accepted them)."),
        card("말해 봅시다! (speaking)", "The book’s prompt (the English is mine):", examples=passage(_SPEAK8)),
        card("Activities left out", "학습활동 1 (Reading): nine pictures (edunet4u.net) of what the ministries do, for each of which you write the matching ministry from a list (교육과학기술부, 외교통상부, 지식경제부, 문화(체육)관광부, 법무부, (고용)노동부, 농림(수산식품)부, 환경부, 보건복지(가족)부). 학습활동 2 (Reading): pictures (edunet4u.net) on the role of the Ministry of Gender Equality (여성부), for which you fill in blanks. 학습활동 3 (Listening, tracks 005 and 006): news on the activities of two ministries (YTN): you fill in the ministries mentioned and the activities described. They are pictures and audio."),
    ],
    exercises=uniq(
        _tr(_MIN8, k=3) + _tr(_NEWS8, k=3)
        + [M("Who recommends candidates for ministerial positions, according to the note?", "The prime minister", ["The National Assembly", "The Supreme Court", "The voters"], "The prime minister recommends; the president nominates."), M("What does the National Assembly hold to judge a nominee?", "A confirmation hearing", ["A referendum", "A party convention", "A press conference"], "인사청문회."), M("Which resource was agreed on between Korea and Bolivia?", "Lithium", ["Oil", "Copper", "Silver"], "리튬."), M("Where is Lake Uyuni?", "Western Bolivia", ["Eastern Russia", "Northern Korea", "Southern Brazil"], "볼리비아 서부."), M("What did the Prime Minister nominee announce?", "That he would voluntarily resign from the nomination", ["That he would run for president", "That he would form a party", "That he would visit Russia"], "자진 사퇴."), M("What did the president reportedly do with the resignations?", "Accepted them", ["Rejected them", "Postponed them", "Ignored them"], "수용.")]
        + [F("오는 십일 월 서울 주요 이십 개국 정상___의 성공적 개최. (summit meeting)", "회의", ["회담", "회견"], "정상회의."), F("이 대통령은 포럼 ___연설에서 경험을 소개할 예정이다. (keynote)", "기조", ["강연", "사퇴"], "기조연설."), F("후보직에서 ___해서 사퇴하겠다고 밝혔다. (voluntarily)", "자진", ["자유", "자립"], "자진."), F("기자 ___을 열어 사퇴 의사를 밝혔다. (a press conference)", "회견", ["회의", "청문회"], "기자회견.")]
        + [read_q("이 대통령은 기조연설에서 한국의 민주주의와 경제발전 경험을 소개할 예정이다"), read_q("김태호 국무총리 후보자가 후보직에서 자진해서 사퇴하겠다고 밝혔다"), read_q("국회는 인사청문회를 연다"), read_q("미국 연방 정부에는 어떤 부처들이 있는지 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("농림", "(農林) agriculture and forestry (acronym for 농업 and 임업)", "수입산 소고기에 대한 농림부 장관의 발언이 문제가 되고 있습니다."),
        ("수산", "(水産) fisheries", "수산시장에 가서 해산물을 좀 삽시다.", "수산업, 수산시장, 농산물"),
        ("지식", "(知識) knowledge", "책을 많이 읽으면 지식을 넓힐 수 있습니다."),
    ]),
    ("학습활동 2", [
        ("평등(하다)", "(平等) equality (to be equal)", "저희 회사는 모든 이에게 평등한 기회를 제공합니다.", "불평등"),
    ]),
    ("학습활동 3", [
        ("개최(하다/되다)", "(開催) holding (a meeting or conference) (to hold/to be held)", "내일부터 무역박람회가 부산에서 개최됩니다.", "열다"),
        ("발간(하다/되다)", "(發刊) publication (to publish/to be published)", "이 잡지는 세계 여러 나라에서 발간되고 있습니다.", "출판하다, 책을 내다"),
        ("상차림", "table setting", "서양식 상차림을 배워 보고 싶습니다."),
        ("선언식", "(宣言式) a declaration/appointment ceremony", "이날 선언식에는 정부 각 부처 장관들이 참여했습니다."),
        ("주제", "(主題) the subject; the topic; the theme", "이 글의 주제는 남녀평등이다."),
        ("지속적", "(持續的) lasting; continuous", "많은 회사들은 지속적으로 경비를 절감하고 있습니다."),
    ]),
    ("학습활동 4", [
        ("기자회견", "(記者會見) a press conference", "그 영화배우가 결혼 발표를 위한 기자회견을 한다고 합니다."),
        ("기조연설", "(基調演說) a keynote speech", "이 대통령은 기조연설에서 경제성장이 중요하다고 말했습니다.", "주연사"),
        ("논의(하다/되다)", "(論議) a discussion (to discuss/to be discussed)", "이 문제에 대해 좀 더 논의해 봅시다."),
        ("뜻", "a meaning; an intention", "김 선생님의 뜻은 감사합니다만 저는 이 돈을 받을 수 없습니다."),
        ("리튬", "lithium", ""),
        ("매장(하다/되다)", "(埋藏) burial (to bury/to be buried; to lie under)", "캘리포니아에는 금이 많이 매장되어 있었다.", "매장량"),
        ("사퇴(하다)", "(辭退) resignation (to resign; to step down [from a position])", "정 국무총리 내정자는 사퇴 의사를 밝혔습니다.", "사직하다"),
        ("수용(하다/되다)", "(受容) accommodation; reception (to accommodate/to be accommodated)", "그 제안은 수용하기 힘듭니다.", "받아들이다"),
        ("자진", "(自進) voluntary", "올해 말까지 불법시설을 자진 신고하면 벌금을 안 내도 된다."),
        ("전달(하다/되다)", "(傳達) delivery; conveyance (to deliver; to convey/to be delivered; to be conveyed)", "김 선생님께 제 뜻을 좀 전달해 주세요.", "전하다"),
        ("합의(하다/되다)", "(合議) an agreement; consent; a settlement (to agree/to be agreed)", "이 문제에 대해서는 여야가 합의했습니다."),
    ]),
]
L3 = lesson(
    "U18 L8 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 농림 · 수산 · 지식 · 평등 · 개최 · 발간 · 상차림 · 선언식 · 주제 · 지속적 · 기자회견 · 기조연설 · 논의 · 뜻 · 리튬 · 매장 · 사퇴 · 수용 · 자진 · 전달 · 합의",
    requires=[],
    cards=[card("A note on the Korean in this list", "농림 is the acronym of 농업 and 임업 (agriculture and forestry); 수산 lists 수산업, 수산시장 and 농산물 as related. 기조연설 lists 주연사 as a related word, printed as in the book. 개최 appeared earlier in this course with a slightly different gloss (“holding or hosting an event”). 매장 appeared in an earlier lesson with a homonym 매장 (賣場), “a shop”; here it lists 매장량 as related. 수용 is glossed “accommodation; reception” here but “acceptance; embrace” in Lesson 5 of this Unit. 리튬 has no Hanja and no example in the book.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=16, nread=14)),
)

# ================================================================== L4 Part 2
_ELECT8 = [
    ("임혜경 부산교육감, 무상급식 단계적 확대", "Busan Superintendent of Education Im Hye-gyeong: free school meals to be expanded in stages"),
    ("정치 바람, 조직과 돈 바람, 이념 바람이 거셌지만 부산의 교육을 바로 세워 달라는 시민들의 순수한 열망 덕분에 이 자리에 있게 됐습니다.", "“The winds of politics, of organization and money, and of ideology were strong, but I am in this seat thanks to the citizens’ pure desire that Busan’s education be set straight.”"),
    ("아홉 명의 후보가 혼전을 벌인 선거에서 이 위 박영관 진보 후보를 이 점 팔 퍼센트포인트 차로 제치고 가까스로 당선된 임혜경 부산시 교육감 당선자는 민선에 의한 우리나라 첫 여성 교육감으로 기록되게 됐다.", "Im Hye-gyeong, the Busan superintendent-elect, who was barely elected by beating the second-place progressive candidate Park Yeong-gwan by 2.8 percentage points in a fierce contest among nine candidates, will go on record as the first female superintendent of education in our country chosen by popular election."),
    ("투표용지 맨 위에 이름이 오른 덕을 봤다는 로또 교육감 꼬리표에 대해 이천칠 년 부산에서 처음 실시된 주민 직선 교육감 선거에 출마해 낙선했지만 깨끗하고 유능한 교육감에 대한 시민의 바람이 이번 선거에서 결실을 거둔 것이라고 말했다.", "About the “lotto superintendent” label, which says she benefited from her name being at the very top of the ballot, she said that although she ran in the direct election of the superintendent first held by residents in Busan in 2007 and lost, the citizens’ wish for a clean and capable superintendent bore fruit in this election."),
    ("그는 초등교사 이십 년, 특수학교 교사 오 년, 교육행정직 십사 년의 경력을 토대로 야무지고 알뜰한 예산 집행을 통해 초등학교부터 무상급식을 시행해 중고교로 확대해 나가고, 촌지와 사교육이 없는 학교 만드는 데 힘쓰겠다고 밝혔다.", "She said that, on the basis of her career of twenty years as an elementary school teacher, five years as a special school teacher and fourteen years in educational administration, she would carry out free meals from elementary school through prudent and thrifty budget execution and extend them to middle and high schools, and work to make schools without gifts of cash to teachers and without private tutoring."),
    ("고향 부산. 경성대 대학원 사회복지학과 박사과정 재학. 부산시교육청 장학관. 용호초교 교장.", "Hometown: Busan. Enrolled in the doctoral course in social welfare at Kyungsung University Graduate School. Busan Metropolitan Office of Education inspector. Principal of Yongho Elementary School."),
    ("전북지사 김완주 당선자, 사백 개 기업 유치, 청년 일자리 사만 개", "Jeonbuk Governor-elect Kim Wan-ju: attract 400 companies, 40,000 jobs for young people"),
    ("사 년 동안 사백 개 기업을 유치하고 사만 개 청년 일자리를 창출하겠습니다.", "“Over four years, I will attract 400 companies and create 40,000 jobs for young people.”"),
    ("전북지사 재선에 성공한 김완주 당선자의 각오이다.", "This is the resolve of Governor-elect Kim Wan-ju, who succeeded in being re-elected governor of Jeonbuk."),
    ("그는 새만금 사업 등을 통해 일자리를 많이 만들라는 도민의 뜻을 선거과정에서 분명히 알게 됐다며 일자리는 단순히 돈을 버는 수단을 넘어, 살아가는 이유이고 최고의 복지라고 덧붙였다.", "He added that during the election he clearly came to know the provincial people’s will that he create many jobs through projects such as Saemangeum, and that a job is beyond merely a means of earning money; it is the reason for living and the best welfare."),
    ("골목경제와 재래시장의 소상공인들을 살리기 위해, 대형 마트 규제에 찬성하는 지자체와 함께 법개정운동을 추진하겠다고 밝혔다.", "To save the small business owners of the alley economy and traditional markets, he said he would push a law revision campaign together with local governments that favor regulating large marts."),
    ("전북지역의 학생 대비 무상급식 비율, 삼십삼 퍼센트를 단계적으로 높여 가겠다고 약속했다.", "He promised to raise in stages the ratio of free school meals to students in the Jeonbuk region, 33 percent."),
    ("행정고시 십사 회 출신으로 풍부한 행정 경험과 강한 추진력을 갖추고 있고, 일벌레라는 평가를 받고 있다.", "A graduate of the 14th administrative service exam, he has rich administrative experience and strong drive and is rated a workaholic."),
    ("고향 전북 임실. 서울대 정치학과. 전북도 기획관리실장. 전주시장. 전북지사.", "Hometown: Imsil, Jeonbuk. Seoul National University, Department of Political Science. Jeonbuk Province planning and management director. Mayor of Jeonju. Governor of Jeonbuk."),
]
_SPEAK8B = [("고향의 주지사는 누구이고 그 사람이 잘한 일과 잘하지 못한 일에 대해 반 친구와 이야기해 보세요.", "Who is the governor of your home state, and talk with a classmate about what that person did well and did not do well."), ("고향에서 주지사가 선거가 곧 있다고 가정하고 어떤 사람이 주지사로 뽑히면 좋을지 친구와 이야기해 보세요.", "Supposing that a governor’s election is coming soon in your home state, talk with a friend about what kind of person it would be good to have elected governor."), ("지방단체의 차원에서 북한과 교류하는 것에 대해 어떻게 생각하는지 이야기해 보세요.", "Tell what you think about exchanges with North Korea at the level of local bodies.")]
L4 = lesson(
    "U18 L8 · Part 2 (본 학습): two newly elected local leaders",
    "본 학습 · 교육감 · 도지사 · 당선자 · 무상급식 · 일자리 창출 · 재선 · 공약 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 천안함 침몰 사건", "The book’s note (in English): 천안함 침몰 사건 refers to the sinking of the ROKS Cheonan on 26 March 2010. The South Korean Navy ship, carrying 104 personnel, sank off the west coast near Baengnyeong Island in the Yellow Sea, killing 46 seamen. A South Korean-led investigation by a team of international experts from South Korea, the United States, the United Kingdom, Canada, Australia and Sweden presented a summary on 20 May 2010 and concluded that the ship was hit by a North Korean torpedo fired by a small submarine. North Korea denied responsibility, the report’s claims and findings have been disputed by China, and Russia allegedly did not agree with the conclusion. The president of the United Nations Security Council condemned the attack but did not name the attacker."),
        card("학습활동 1: an article on two local election winners (Hankyoreh)", "The book asks you to fill a table about the two winners (elected position; education and career history; number of times elected; pledges and promises) and two questions: why 임혜경 was nicknamed 로또 교육감 and what she said about it, and what 김완주’s view of his new job is. Both are public officials, named as in the article; I dropped the ages, the spouse’s name and the family line. The numbers are spelled in Hangul and the quotation marks and the bullet “●” are dropped (the quoted words stay as the article’s own statements). The article, with my English:", examples=passage(_ELECT8)),
        card("My answers to 학습활동 1", "Table. 임혜경: elected position, Busan superintendent of education (the first female superintendent chosen by popular vote); career, elementary teacher 20 years, special school teacher 5 years, educational administration 14 years, inspector at the Busan education office, principal of Yongho Elementary, now in a doctoral course in social welfare; newly elected (she lost the 2007 election); pledges, phased expansion of free school meals from elementary to middle and high schools, schools without cash gifts and private tutoring. 김완주: Jeonbuk governor; Seoul National University political science, administrative service exam graduate, Jeonbuk planning director, mayor of Jeonju; re-elected; pledges, attract 400 companies and 40,000 youth jobs in four years, push a law revision campaign on regulating large marts to save small merchants, raise the free-meal ratio (now 33 percent) in stages. Question 2: The label means she benefited from her name being at the top of the ballot; she said she had lost in 2007 but the citizens’ wish for a clean, capable superintendent bore fruit this time. Question 3: He sees a job as more than a means of earning money; it is the reason for living and the best welfare, and he is resolved to create jobs."),
        card("말해 봅시다! (speaking)", "The book’s three prompts (the English is mine):", examples=passage(_SPEAK8B)),
        card("Activities left out", "학습활동 2 (Listening, track 007): a YTN news item on the city of Incheon: what Incheon announced and the central government’s reaction; what fact was reported for 2005, 2006 and this year; and the details of Incheon’s plan for this year. It is audio."),
    ],
    exercises=uniq(
        _tr(_ELECT8, k=3) + _tr(_SPEAK8B, k=2)
        + [M("What office did 임혜경 win?", "Busan superintendent of education", ["Jeonbuk governor", "Mayor of Busan", "National Assembly member"], "교육감."), M("By what margin did she beat the second-place candidate?", "2.8 percentage points", ["28 percentage points", "0.28 percentage points", "12 percentage points"], "이 점 팔 퍼센트포인트."), M("What does the nickname 로또 교육감 suggest?", "That she won by luck, from her name’s position on the ballot", ["That she was rich", "That she was a lottery official", "That she lost twice"], "투표용지 맨 위."), M("How many companies does 김완주 plan to attract in four years?", "400", ["40", "4,000", "14"], "사백 개."), M("Was 김완주 newly elected or re-elected?", "Re-elected", ["Newly elected", "Appointed", "Defeated"], "재선."), M("What does 김완주 call a job?", "The reason for living and the best welfare", ["A burden", "A temporary tool", "A privilege of the young"], "최고의 복지.")]
        + [F("투표용지 맨 위에 이름이 오른 ___을 봤다. (benefit)", "덕", ["결실", "열망"], "덕을 보다."), F("시민의 바람이 이번 선거에서 ___을 거두었다. (fruit)", "결실", ["덕", "열망"], "결실을 거두다."), F("전북지사 ___에 성공했다. (re-election)", "재선", ["출마", "낙선"], "재선."), F("민선에 의한 우리나라 첫 여성 ___이다. (superintendent)", "교육감", ["장학사", "지사"], "교육감.")]
        + [read_q("임혜경 당선자는 민선에 의한 우리나라 첫 여성 교육감이다"), read_q("김완주 당선자는 전북지사 재선에 성공했다"), read_q("일자리는 살아가는 이유이고 최고의 복지다"), read_q("고향의 주지사는 누구입니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("결실을 거두다", "(結實) to bear fruit; “to reap fruit”", "일 년 동안 다 같이 열심히 공부해서 좋은 결실을 거두자."),
        ("교육감", "(敎育監) a superintendent of education", "", "장학사"),
        ("덕을 보다", "(德) to benefit (from/of)", "동생이 성공해서 제가 덕을 많이 봤습니다.", "덕분에, 덕택에"),
        ("민선", "(民選) elected by people; “civilian selection”", "올해부터는 교육감을 민선으로 뽑는다고 합니다.", "관선"),
        ("바람", "a wish; a hope", "내년에 집을 장만하는 것이 제 바람입니다."),
        ("바로 세우다", "to rectify; to fix; “to straighten up”", "새로 뽑힌 서울재래시장협회 회장은 잘못된 시장 질서를 바로 세우겠다고 했다."),
        ("소상공인", "(小商工人) small business and factory owners", "우리 은행에서는 소상공인을 대상으로 하는 대출 상품을 새로 마련했습니다.", "중소기업인"),
        ("열망(하다)", "(熱望) an ardent wish (to wish ardently)", "우리 국민들은 정치 개혁에 대한 열망이 강합니다.", "갈망하다"),
        ("일벌레", "a workaholic; “work worm”", "그분은 일밖에 모르는 일벌레예요.", "공부벌레, 책벌레"),
        ("장학관", "(奬學官) a school inspector; a commissioner", "오늘 오후에 우리 학교에 장학관이 방문하신다고 합니다."),
        ("장학사", "(奬學士) a school supervisor", "", "교육감"),
        ("재래시장", "(在來市場) a conventional market; a traditional market", "이번 추석 장은 백화점보다는 재래시장에서 봐야겠어요."),
        ("제치다", "to pass (others in a competition or race); to leave others behind", "스케이팅 경기 중 뒤에 있던 한국 선수가 네 명의 선수들을 제치고 앞으로 나왔다."),
        ("~지사", "(知事) the governor of a province; a provincial governor", "송현식 충북지사는 오 년간의 충북 발전 계획에 대해 발표했다.", "도지사, 군수, 주지사"),
        ("창출(하다/되다)", "(創出) creation (of jobs) (to create/to be created)", "정부는 일자리를 창출하기 위한 정책을 발표했습니다."),
        ("출마(하다)", "(出馬) running for (an elective position) (to run for [an elective position])", "김 의원이 이번에 대통령 선거에 출마하기로 결정했습니다."),
        ("특수학교", "(特殊學校) a special education school", "우리 아이는 몸이 불편해서 특수학교에 다니고 있습니다."),
        ("혼전", "(混戰) an intense battle; a fierce fight; a close game; “chaotic war”", "축구 경기는 초반부터 혼전 양상을 보였습니다."),
    ]),
    ("학습활동 2", [
        ("관심이 쏠리다", "(關心) attention is drawn/focused; “attention leans”", "이번 남북회담에 온 국민의 관심이 쏠려 있습니다."),
        ("물꼬를 트다/물꼬가 트이다", "(idiom) to open the floodgates/the floodgates are opened; “to open the sluice gate (of a rice paddy)”", "이번 남북정상회담은 남북 관계의 물꼬를 트는 데 중요한 역할을 할 것이다."),
        ("성사(시키다/되다)", "(成事) accomplishment; achievement (to accomplish; to achieve/to be accomplished; to be achieved)", "그 일을 성사시키기 위해 최선을 다하고 있습니다."),
        ("여부", "(與否) whether or not; yes or no", "이번 협상이 이뤄질 수 있을지 그 여부가 궁금합니다. 사고 비행기에 탑승한 승객들의 생사여부를 알 수 없습니다."),
        ("영유아", "(嬰幼兒) infants and toddlers", "이 비디오는 영유아들을 위해 만들어진 것입니다.", "영아, 유아"),
        ("유소년", "(幼少年) children; childhood; youth", "박지성 선수가 유소년 축구 교실을 연다고 합니다.", "청소년"),
        ("인도적", "(人道的) humanitarian", "정부는 지진 피해를 입은 나라에 인도적 지원을 하기로 결정했습니다."),
        ("전개(하다/되다)", "(展開) unfolding (of a situation); development (of a movement) (to unfold; to develop/to be unfolded; to be developed)", "작년부터 환경단체들이 산불 예방 운동을 전개해 오고 있다."),
        ("차원", "(次元) level; dimension", "이런 문제는 국가 차원에서 논의해야 한다."),
        ("친선경기", "(親善競技) a goodwill match; a sports game to promote friendship", "우리 축구 대표팀이 일본 대표팀과 친선경기를 갖습니다."),
        ("한 발짝 물러서다", "(idiom) to yield; to make a concession; “to take one step back”", "이번 협상에서는 한 발짝도 물러서면 안 된다."),
    ]),
]
L5 = lesson(
    "U18 L8 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 결실을 거두다 · 교육감 · 덕을 보다 · 민선 · 바람 · 소상공인 · 열망 · 일벌레 · 장학관 · 재래시장 · 제치다 · 지사 · 창출 · 출마 · 특수학교 · 혼전 · 관심이 쏠리다 · 물꼬를 트다 · 성사 · 여부 · 영유아 · 유소년 · 인도적 · 전개 · 친선경기 · 한 발짝 물러서다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives homonyms: 바람 (wind), 혼전 (婚前, “premarital”). 교육감 has no gloss beyond its English and lists 장학사 as related; I gave 장학사 its own entry with the Hanja from the 장학관 entry as printed (the book lists 교육감 under 장학사), so its gloss is mine: “a school supervisor”. 민선 lists 관선 (government-appointed) as its counterpart; ~지사 lists 도지사, 군수, 주지사 and notes the homonym 지사 (支社), “a branch office”. The examples had digits in the book (4명, 1년, 5년), which I spelled out. The book prints 생사여부 without a space and gives two examples for 여부, which I joined.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=22, nread=18)),
)

# ================================================================== L6 Part 3
_DOLL8 = [
    ("육천삼백 원으로 황제 같은 생활 한나라 의원 체험기 논란", "“An emperor-like life on 6,300 won”: controversy over a Grand National Party assemblyman’s account of his experience"),
    ("한나라당 차명진 의원이 참여연대가 주최한 최저생계비로 하루를 살아 보는 캠페인에 참여한 뒤 황제와 같은 생활을 했다는 등의 체험기를 남겨 논란이 일고 있다.", "A controversy has arisen after Grand National Party Assemblyman Cha Myeong-jin took part in a campaign hosted by People’s Solidarity for Participatory Democracy in which one lives a day on the minimum cost of living, and left an account of his experience saying things such as that he lived like an emperor."),
    ("차 의원은 지난 이십삼 일부터 이십사 일까지 참여연대에서 실시하는 최저생계비로 한 달 나기 릴레이 체험에 참가했다.", "Assemblyman Cha took part from the 23rd to the 24th in the relay experience “living a month on the minimum cost of living” run by People’s Solidarity."),
    ("당시 차 의원은 이틀간 세 끼 식비로 육천삼백 원을 받았다.", "At that time Assemblyman Cha was given 6,300 won as food money for three meals over two days."),
    ("이 돈으로 쌀 한 컵 팔백 원, 쌀국수 한 봉지 구백칠십 원, 미트볼 한 봉지 구백칠십 원, 참치캔 한 개 구백칠십 원, 황도 구백칠십 원을 샀다.", "With this money he bought a cup of rice (800 won), a packet of rice noodles (970 won), a packet of meatballs (970 won), a can of tuna (970 won) and canned yellow peaches (970 won)."),
    ("전부 합해 사천육백팔십 원이었다.", "In all it came to 4,680 won."),
    ("이후 차 의원은 이십육 일 자신의 홈페이지에 최저생계비 체험기를 남겼다.", "Afterwards, on the 26th, Assemblyman Cha left an account of his minimum-cost-of-living experience on his own homepage."),
    ("문제는 나는 왜 단돈 육천삼백 원으로 황제와 같은 생활을 할 수 있었을까, 밥 먹으라고 준 돈으로 사회기부도 하고 문화생활까지 즐겼을까, 라고 말했던 것.", "The problem was that he said, “Why was I able to live like an emperor on a mere 6,300 won? With the money given to eat meals, did I even make a social donation and enjoy cultural life?”"),
    ("그 이유는 물가에 대한 좋은 정보와 마음껏 돌아다닐 수 있는 건강이 있었기 때문이라고 밝혔다.", "As the reason, he said it was because he had good information about prices and the health to move around freely."),
    ("또 최저생계비만 올리는 것으론 답이 안 나올 것 같다며 국가재정에도 한계가 있다고 말했다.", "He also said that merely raising the minimum cost of living would probably not give an answer, and that there is a limit to national finances too."),
    ("최저생계비로 한 달 나기 릴레이 체험은 최저생계비를 현실화하자는 취지로, 실제로 최저생계비만으로 쪽방촌에서 생활하는 캠페인이다.", "The relay experience of living a month on the minimum cost of living is a campaign with the aim of making the minimum cost of living realistic, in which people actually live in a cramped-room district on only the minimum cost of living."),
    ("한나라당 의원이 참가한 것은 차 의원이 처음이다.", "Assemblyman Cha is the first Grand National Party assemblyman to take part."),
    ("차 의원과 같은 조건으로 최저생계비 일 일 체험을 한 민주당 주승용 의원은 자신의 경험을 공개하며 차 의원을 비판했다.", "Democratic Party Assemblyman Ju Seung-yong, who did a one-day minimum-cost-of-living experience under the same conditions as Assemblyman Cha, made his own experience public and criticized Assemblyman Cha."),
    ("주 의원은 이십팔 일 오전 와이티엔 라디오 아침 프로그램과 가진 인터뷰에서 차 의원의 글을 읽었냐는 진행자 질문에 본인의 식성이라던지, 소식을 하느냐 대식을 하느냐 차이도 있겠지만 객관적으로 봤을 때 육천삼백 원 정도를 가지고 세 끼 식사를 한다는 것은 하루 이틀은 견딜 수 있을지 몰라도 한 달이나 일 년 삼백육십오 일 생활한다는 것은 거의 불가능하다며 차 의원의 황제 식사를 꼬집었다.", "In an interview on the morning of the 28th with a YTN radio morning program, to the host’s question whether he had read Assemblyman Cha’s writing, Assemblyman Ju said, “There are differences too, such as one’s own tastes and whether one eats little or a lot, but looked at objectively, eating three meals on about 6,300 won may be bearable for a day or two but is almost impossible for a month or a year of 365 days,” and so jabbed at Assemblyman Cha’s “emperor’s meal.”"),
    ("주 의원은 최소한 영양실조에 걸릴 것이라며 국민기초생활보장법에 보게 되면 최저생계비 정의가 국민이 건강하고 문화적인 생활을 유지하기 위한 최소의 비용으로 규정이 돼 있는데 건강하고 문화적인 생활은커녕 의식주를 해결하는 데도 절대적으로 부족하다고 생각을 했다며 문화생활도 했다는 차 의원을 반박했다.", "Assemblyman Ju said that at the very least one would suffer from malnutrition, and rebutted Assemblyman Cha, who said he had also enjoyed cultural life, saying that in the National Basic Living Security Act the definition of the minimum cost of living is prescribed as “the minimum cost for the people to maintain a healthy and cultural life,” and that he thought it was absolutely insufficient even to solve food, clothing and shelter, let alone a healthy and cultural life."),
    ("주 의원은 육천삼백 원이면 한 끼에 이천백 원인데, 이건 생각해 보면 알겠지만 그야말로 최저생계비라기보다는 최저생존비라고 명칭을 정하고 싶다고 일 일 체험의 소감을 밝혔다.", "Assemblyman Ju gave his impressions of the one-day experience, saying, “6,300 won is 2,100 won a meal; if you think about it you will understand, but I would like to name this a ‘minimum survival cost’ rather than a minimum cost of living.”"),
    ("주 의원은 최저생계비에 대해 지금 현재 일 인 가구 해서 오십만 사천 원 정도를 받고 있는데, 현실과 괴리가 되어 있다.", "About the minimum cost of living, Assemblyman Ju said, “At present, a one-person household receives about 504,000 won, which is out of touch with reality."),
    ("티브이 수신료라든지, 의료비 등을 공제하고 실제 손에 쥐는 것은 대부분 사십이만 원 정도라며 용산 일 평 남짓한 쪽방이 한 달 월세가 싼 곳은 이십만 원, 좀 비싼 곳은 이십오만 원 정도라 이십만 원 정도밖에 남지 않는데 이 이십만 원을 가지고 먹고, 교통비 하고, 심지어 술, 담배 피시는 분도 그것도 사야 되고 혹시나 아플 경우에 병원비도 계산해야 된다고 설명했다.", "After deducting things like the TV license fee and medical costs, what one actually holds in one’s hand is mostly about 420,000 won,” he explained, “and in a cramped room of a little over one pyeong in Yongsan the monthly rent is 200,000 won where cheap and about 250,000 won where somewhat expensive, so only about 200,000 won is left, and with this 200,000 won one has to eat, pay transport, even buy drink and cigarettes for those who smoke, and also count hospital bills in case one falls ill.”"),
    ("그는 교통비라든지, 의료비라든지, 기호품이라든지 이런 것을 다 빼더라도 이십만 원을 가지고 한 달 구십 끼를 생각한다면 평균 이천백 원이라며 그렇기 때문에 전혀 문화적인 생활은 할 수 없는 것이라고 거듭 문화생활을 언급한 차 의원을 꼬집었다.", "He jabbed again at Assemblyman Cha, who had mentioned “cultural life,” saying, “Even if you subtract all of these, such as transport, medical costs and items of personal preference, if you think of 90 meals a month on 200,000 won, it averages 2,100 won; therefore one cannot live a cultural life at all.”"),
]
_SPEAK8C = [("고소득층이나 저소득층 모두가 함께 공존하려면 어떤 제도가 선행되어야 할지, 사회 구성원의 마음가짐은 어떠해야 할지 반 친구들과 이야기해 보세요.", "Talk with your classmates about what system would have to come first for both high-income and low-income groups to coexist, and what the attitude of the members of society should be.")]
L6 = lesson(
    "U18 L8 · Part 3 (심화 학습): a 6,300-won “emperor’s life”",
    "심화 학습 · 최저생계비 · 최저생존비 · 릴레이 체험 · 국민기초생활보장법 · 쪽방촌 · 무상급식 · 빈대 잡으려다 초가삼간 다 태운다 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: two assemblymen and the minimum cost of living (Kyunghyang)", "The article tells of two National Assembly members who took part in a civic group’s experience event. The two are named as in the article (public officials); the host and the producer of the radio program are dropped, so the program is just a “YTN radio morning program”. The numbers are spelled in Hangul, the quotation marks and parentheses are dropped, and “TV” becomes 티브이 and “YTN” 와이티엔. In the book’s text the cultural-life phrase is printed with a stray mark (다문화 생활), which I read as 문화생활. The article, with my English:", examples=passage(_DOLL8)),
        card("My answers to 학습활동 1", "1. 최저생계비로 한 달 나기 릴레이 체험 is a relay campaign (run by 참여연대) in which people actually live in a cramped-room district on only the minimum cost of living; its significance is its aim of making the minimum cost of living realistic. 2. Cha lived two days on 6,300 won for three meals (he bought rice, noodles, meatballs, tuna and canned peaches for 4,680 won), then wrote on his homepage that he lived like an emperor and even donated and enjoyed culture, because he had good price information and the health to move around; he also said raising the minimum cost alone is no answer and national finances have limits. 3. B (critical). 4. “The minimum cost for the people to maintain a healthy and cultural life.” 5. 6,300 won is 2,100 won a meal; it is almost impossible to live a month or a year on that; it would cause malnutrition; it is not enough even for food, clothing and shelter; a one-person household gets about 504,000 won, about 420,000 won after deductions such as the TV license fee and medical costs; after rent of 200,000 to 250,000 won for a tiny room about 200,000 won is left for food, transport, cigarettes and drink, and medicine; at 90 meals a month that is 2,100 won on average, so no cultural life is possible."),
        card("말해 봅시다! (speaking)", "The book’s prompt (the English is mine):", examples=passage(_SPEAK8C)),
        card("Activities left out", "학습활동 2 (Listening, tracks 008 and 009): a commentary (Donga) on free school meals for every child (전면 무상급식): how the program works now, the biggest reason for insisting on it, how the speaker suggests handling it, the speaker’s tone (mocking, apathetic, sympathetic, emotional), and a section on the proverb 빈대 잡으려다 초가삼간 다 태운다 with four English choices to match (A. A beacon does not shine on its base; B. A rolling stone gathers no moss; C. cannot see the forest for the trees; D. break a butterfly on the wheel). It is audio. The book’s own gloss of the proverb in the vocabulary list is “to break a butterfly on the wheel,” which is choice D."),
    ],
    exercises=uniq(
        _tr(_DOLL8, k=3)
        + [M("What did 차명진 get for food money for the two days?", "6,300 won", ["4,680 won", "63,000 won", "2,100 won"], "육천삼백 원."), M("How much did the items he bought come to?", "4,680 won", ["6,300 won", "970 won", "2,100 won"], "사천육백팔십 원."), M("Which group hosted the campaign?", "참여연대", ["YTN", "한나라당", "민주당"], "참여연대."), M("How does 주승용 feel about 차명진’s remarks?", "Critical", ["Sympathetic", "Discouraged", "Respectful"], "B."), M("How does the law define the minimum cost of living?", "The minimum cost to maintain a healthy and cultural life", ["The average cost of food", "The cost of rent and tax", "The income of a one-person household"], "정의."), M("What average amount per meal does 주승용 give?", "2,100 won", ["6,300 won", "970 won", "20,000 won"], "이천백 원."), M("What name does 주승용 prefer to 최저생계비?", "최저생존비", ["최저생활비", "최소소득", "기초생계비"], "Minimum survival cost.")]
        + [F("한나라당 의원이 참가한 것은 차 의원이 ___이다. (the first)", "처음", ["마지막", "혼자"], "처음."), F("쪽방촌은 최저생계비만으로 ___하는 곳이다. (to live)", "생활", ["출마", "개최"], "생활."), F("건강하고 문화적인 생활은___ 의식주도 해결하기 어렵다. (let alone)", "커녕", ["부터", "처럼"], "~은/는커녕."), F("최저생계비를 ___하자는 취지의 캠페인이다. (make realistic)", "현실화", ["평등", "개최"], "현실화.")]
        + [read_q("한나라당 차명진 의원이 체험기를 남겨 논란이 일고 있다"), read_q("육천삼백 원이면 한 끼에 이천백 원이다"), read_q("건강하고 문화적인 생활은커녕 의식주도 해결하기 어렵다"), read_q("고소득층이나 저소득층 모두가 함께 공존하려면 어떤 제도가 선행되어야 할까요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("객관적", "(客觀的) objective", "저는 모든 사실을 객관적으로 보려고 노력합니다."),
        ("괴리", "(乖離) a gap (in view); an estrangement; an alienation", "이것은 제가 생각했던 것과는 상당한 괴리가 있군요."),
        ("꼬집다", "to make cynical remarks; to criticize; “to pinch”", "언론은 정부의 잘못된 정책을 꼬집으며 비판했습니다.", "비판하다"),
        ("균등(하다)", "(均等) equality (to be equal)", "우리 모두에게 균등하게 나누어 주세요.", "평등"),
        ("기호품", "(嗜好品) an item of personal preference", "명절 선물로 커피나 와인과 같은 기호품이 인기를 얻고 있다."),
        ("논란", "(論難) a controversy; a dispute; an argument", "새로 개봉된 영화가 논란에 휩싸였습니다."),
        ("생계비", "(生計費) living expenses; the cost of living", "최저생계비 책정에 대해 국회에서 논의 중입니다."),
        ("손에 쥐다", "to get; to have; “to hold something in (one’s) hand”", "한 달 동안 잠도 잘 못 자고 일했는데 손에 쥔 건 겨우 오십만 원이다."),
        ("의식주", "(衣食住) food, clothing, and shelter; the necessities of life", "의식주는 우리 삶에 꼭 필요한 필수조건입니다."),
        ("정의", "(定義) a definition", "이 단어의 정의를 사전에서 좀 찾아 주세요."),
        ("쪽방촌", "an area with many one-room households; a poor area; “town of partitioned rooms”", "그 신문은 쪽방촌에 대한 기사를 실었습니다.", "달동네"),
        ("체험기", "(體驗記) a story of one’s personal experiences", "이 블로그에 저의 유럽여행 체험기를 올리고 싶어요.", "체험담"),
        ("~은/는커녕", "far from; not to mention", "밥을 먹기는커녕 물도 못 마셨다."),
        ("한계", "(限界) a limit; a limitation; a boundary", "그 사람과 얘기를 하다 보니 인내심의 한계가 느껴졌어요."),
        ("현실화(하다/되다)", "(現實化) actualization (to actualize/to be actualized)", "이제 우리가 세운 계획을 현실화합시다."),
        ("황도", "(黃桃) a yellow peach", "저는 황도보다는 백도가 더 좋습니다.", "복숭아, 백도"),
        ("황제", "(皇帝) an emperor", "타이거 우즈는 골프의 황제라고 불립니다.", "제왕, 왕"),
    ]),
    ("학습활동 2", [
        ("감수성", "(感受性) sensitivity; sensibility", "우리 아이는 감수성이 예민해서 자주 웁니다.", "감성"),
        ("고백(하다)", "(告白) confession (to confess)", "오늘 여자친구에게 사랑을 고백할 겁니다.", "자백"),
        ("귀중하다", "(貴重) to be precious; to be priceless", "귀중한 시간을 낭비하지 말고 열심히 삽시다.", "귀하다, 소중하다"),
        ("낙인 찍다/낙인 찍히다", "(烙印) to brand; to stigmatize/to be branded; to be stigmatized", "김 씨는 전과자라는 낙인이 찍혀 있습니다."),
        ("눈치(를) 보다", "to try to read one’s mind/face; to probe one’s motives; to see how the wind blows", "눈치 보지 말고 마음껏 드세요.", "눈치를 살피다"),
        ("(무)성의", "(誠意 or 無誠意) sincerity (insincerity)", "복지문제에 관해 국회의원들이 무성의한 태도를 보였다."),
        ("밀리다", "to be pushed back; to be moved back; to be delayed; to be left undone", "지원자가 많아서 내 인터뷰 순서가 뒤로 밀렸다. 차가 밀려서 약속 시간에 늦었다."),
        ("발상", "(發想) idea; thinking", "발상의 전환"),
        ("불과하다", "(不過) to be nothing but; to be only", "그 일은 거짓에 불과합니다."),
        ("빈대 잡으려다 초가삼간 다 태운다", "(草家三間) (proverb) to break a butterfly on the wheel; “to burn down a whole small thatched cottage while trying to catch a flea”", ""),
        ("상임위원회", "(常任委員會) a standing/permanent committee", "국회상임위원회는 그 법안을 검토하고 있습니다.", "국회상임위"),
        ("상정(하다/되다)", "(上程) submitting; introduction; bringing in (a bill, regulation, law, etc.) (to submit; to introduce; to propose/to be submitted; to be proposed)", "야당에서 새 법안을 국회상임위에 상정했습니다."),
        ("선심(쓰다)", "(善心) virtuous mind; generosity; kind heart (to do [somebody] a kindness; to show [somebody] mercy; “to use generosity”)", "그 사람은 항상 선심을 쓰는 척 하면서 이익을 챙깁니다."),
        ("속셈", "a hidden agenda; hidden/true intention; an ulterior motive; “inside calculation”", "저에게 선심을 쓰는 속셈이 무엇입니까?"),
        ("심의(하다/되다)", "(審議) deliberation; consideration; review (to deliberate; to review/to be deliberated; to be reviewed)", "새 법안에 대한 심의가 진행 중입니다.", "검토"),
        ("얄팍하다", "to be rather thin; to be superficial; to be shallow", "얄팍한 지식만으로는 전문가가 될 수 없다."),
        ("위화감", "(違和感) a sense of incongruity/incompatibility; a feeling that one does not belong (in a place)", "일부 계층의 명품 사재기로 계층간 위화감이 심화되고 있습니다."),
        ("의식", "(意識) one’s sense; consciousness", "어머니가 사고로 쓰러지셨는데 아직도 의식이 없으세요."),
        ("전면(적)", "(全面的) general; entire; all angles; full-fledged", "정부는 그 제품에 대해 전면적인 수입 제한 조치를 취했다."),
        ("탕진(하다/되다)", "(蕩盡) dissipation; squandering; waste (to dissipate; to squander/to be dissipated; to be squandered)", "그 사람은 노름으로 전 재산을 탕진했습니다."),
        ("파행", "(跛行) limping; crippled; chaotic", "여당과 야당의 극심한 의견차이로 국회가 파행적으로 운영되고 있다."),
        ("헤아리다", "to consider; to reckon; to guess; to understand", "저는 그분의 뜻을 헤아릴 수 없습니다."),
    ]),
]
L7 = lesson(
    "U18 L8 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 객관적 · 괴리 · 꼬집다 · 균등 · 기호품 · 논란 · 생계비 · 손에 쥐다 · 의식주 · 정의 · 쪽방촌 · 체험기 · 한계 · 현실화 · 황제 · 감수성 · 고백 · 낙인 · 눈치 · 밀리다 · 발상 · 상정 · 선심 · 속셈 · 심의 · 위화감 · 탕진 · 파행 · 헤아리다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives homonyms: 정의 (正義), “justice”, and 전면 (前面), “front”. (무)성의 is printed with the 無 in parentheses (無誠意 means insincerity). 빈대 잡으려다 초가삼간 다 태운다 has no example in the book; its Hanja 草家三間 is given. 쪽방촌 and the proverb have no Hanja for the whole expression other than that. 발상 has the phrase 발상의 전환 (“a change of thinking”) as its example. 밀리다 has two examples, which I joined; two examples had digits (50만 원), which I spelled out; the example of 괴리 ended in an exclamation mark in the book, which I made a period.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=26, nread=22)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 8: Central and Local Government (중앙정부와 지방자치단체)", [L1, L2, L3, L4, L5, L6, L7])

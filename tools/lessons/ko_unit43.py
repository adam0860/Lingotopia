"""Unit 43: KBC Semester 2, Unit 9, Chapter 36 - Life at Work (직장생활).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 9, Student's Edition (Validation Edition).
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 36 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("간단히", "(簡單) simply; briefly", "간단히 준비운동을 하고 축구를 시작했습니다."),
    ("구내", "(構內) premises; precinct; a compound; “inside the structure”", "점심은 보통 구내식당에서 먹습니다."),
    ("넓히다", "to widen; to expand", "내년에는 사업을 넓히려고 합니다."),
    ("답장", "(答狀) a (written) reply; a reply letter; to reply (~하다)", "어제 어머니의 편지에 답장을 써서 보냈습니다."),
    ("대인관계", "(對人關係) interpersonal relationship; social network", "직장에서는 대인관계가 중요합니다."),
    ("바이어", "a buyer; a buying agent from abroad", "다음달에 바이어들이 우리 회사를 방문하겠습니다."),
    ("밤새", "all night long; through the night", "아기가 밤새 울었어요."),
    ("보고서", "(報告書) a written report", "이번 사건에 관한 보고서를 작성해 주세요."),
    ("부품", "(部品) a (machine) part; component", "이 가게는 자동차 부품을 판매하는 가게입니다."),
    ("사내", "(社內) the compound (of a company); “inside the company”", "게시판을 보면 사내 소식을 잘 알 수 있어요."),
    ("성공", "(成功) success; achievement; accomplishment; to succeed; to be successful (~하다)", "그 사람은 열심히 일을 하니까 사업에 성공할 거야."),
    ("수출", "(輸出) export; exportation; to export (~하다)", "우리회사는 중국에 핸드폰을 수출하고 있습니다."),
    ("업무", "(業務) work; duties; job responsibilities", "오전에 제 업무를 끝내고 동료의 일을 도와주고 있습니다."),
    ("유능", "(有能) competence; capability; to be able; to be capable (~하다)", "이 부서에는 유능한 직원들이 아주 많습니다."),
    ("이르다", "to be early; to be premature", "그 공연을 보기 위해 이른 아침부터 많은 사람들이 기다리고 있었습니다."),
    ("익숙하다", "to be familiar; to be well acquainted; to be used to", "야간 근무를 하면서 늦게 자는 것에 익숙해졌어요."),
    ("일과", "(日課) a daily task; daily work; (daily) routine", "아버지는 여섯 시에 일어나 하루 일과를 시작하십니다."),
    ("정장", "(正裝) full dress; formal dress; “correct dress”; to dress up (~하다)", "결혼식에 갈 때는 정장을 입는 것이 좋습니다."),
    ("지원", "(支援) support; aid; to support (~하다)", "이 전시회는 서울시가 지원합니다."),
]
_CV_B = [
    ("규모", "(規模) a scale; a scope", "그 가수는 항상 대규모 공연을 합니다."),
    ("능력", "(能力) ability; capability; competence", "그 사람은 능력도 있고 일도 열심히 합니다."),
    ("대리", "(代理) a deputy; “proxy”", "회사에 들어가 이 년 후에 대리로 승진했습니다."),
    ("만족", "(滿足) satisfaction; to be satisfied / to be satisfying (~하다/스럽다)", "시험 결과에 만족합니다."),
    ("반복", "(反復) repetition; reiteration; to repeat; to reiterate; to do over again / to be repeated (~하다/되다)", "같은 실수를 반복하지 마세요."),
    ("보너스", "a bonus", "연말에 직원들에게 백 퍼센트 보너스를 주기로 했어요."),
    ("분위기", "(雰圍氣) an atmosphere; an ambience", "저는 조용한 사무실 분위기를 좋아해요."),
    ("불만족", "(不滿足) dissatisfaction; discontent; to be dissatisfying; to be unsatisfactory (~스럽다)", "회사 연봉에 불만족인 사원이 많다."),
    ("상사", "(上司) one’s superior; a senior official", "신입사원들은 상사와 이야기하는 것을 어렵게 생각한다."),
    ("야근", "(夜勤) night duty; night work; night shift; to take night duty; to work overtime into the night (~하다)", "어제는 야근을 하고 집에 늦게 들어갔어요."),
    ("연봉", "(年俸) an annual salary", "올해는 연봉이 오르지 않았습니다."),
    ("이직(移職)", "(移職) change of occupation; to change one’s occupation (~하다)", "제 아내는 작년에 컴퓨터 회사로 이직했습니다."),
    ("이직(離職)", "(離職) separation from one’s position; quitting one’s job; to quit one’s job (~하다)", "요즘 젊은이들은 일이 적성에 맞지 않으면 이직을 합니다."),
    ("인정", "(認定) recognition; acknowledgment; confirmation; approval; to recognize; to admit; to approve / to be recognized (~하다/받다)", "그 회사 제품의 품질은 모든 사람들이 다 인정합니다."),
    ("자유", "(自由) freedom; liberty; to be free; to be liberal; to be unrestricted (~롭다)", "우리에게 선택할 자유를 주세요."),
    ("재택근무", "(在宅勤務) telecommuting; telework; “working from home”", "우리 회사는 재택근무가 가능합니다."),
    ("지겹다", "to be boring; to be tedious; to be wearisome; to be tiresome", "매일 똑 같은 일을 하는 것이 지겨워요."),
    ("차이", "(差異) a difference; a gap", "두 제품의 가격 차이가 너무 커요."),
    ("출장", "(出張) a business trip; a tour of duty; to go on a business trip (~가다)", "내일 유럽으로 출장을 가야 합니다."),
]
_CV_C = [
    ("개업", "(開業) opening of a business; commencement of practice; to open a business (~하다)", "우리 형은 지난 달에 작은 식당을 개업했습니다."),
    ("노후", "(老後) one’s old age; “old after”", "노후에는 고향에서 살고 싶습니다."),
    ("답답하다", "to be stuffy; to be suffocating", "답답한 도시보다 시골에서 사는 것이 좋습니다."),
    ("불만", "(不滿) dissatisfaction; discontent", "직원들은 사장에게 불만을 이야기했습니다."),
    ("사표 / 사직서", "(辭表 / 辭職書) resignation; a letter of resignation; to resign (~[를] 내다)", "직장 상사와 의견이 맞지 않아서 사표를 냈어요."),
    ("수입", "(輸入) import; to import (~하다)", "이 지갑은 미국에서 수입한 제품입니다."),
    ("여유", "(餘裕) elbowroom (in terms of time, money, space, mental energy, material, etc.); to be free (of obligations) (~롭다)", "오전에는 바쁘지만 오후에는 여유롭습니다."),
    ("연금", "(年金) a pension; “annual money”", "아버지께서는 공무원 연금을 받아서 생활합니다."),
    ("은퇴", "(隱退) retirement (from active/public life); to retire (~하다)", "내년에 은퇴하면 유럽여행을 하고 싶습니다."),
    ("인생", "(人生) one’s life; “human life”", "결혼은 새 인생의 시작입니다."),
    ("자영업", "(自營業) self-run business; self-employment", "자영업을 하는 사람이 많아지고 있습니다."),
    ("(자원)봉사", "((自援)奉仕) volunteer service; to serve as a volunteer (~하다)", "토요일마다 고아원에 가서 자원봉사를 합니다."),
    ("(정년)퇴직", "((停年)退職) retirement (at normal retirement age)", "저희 아버지는 이 년 후에 정년퇴직을 합니다."),
    ("제~", "(第) optional prefix for an ordinal", "박 일병은 제삼 중대에 근무하고 있습니다."),
    ("차리다", "to set up (a business); to open up (a business)", "저는 대학을 졸업한 후에 제 회사를 하나 차리고 싶습니다."),
    ("창업", "(創業) foundation of a business; to found a business (~하다)", "창업을 하기 위해 요리학원에 다니고 있습니다."),
    ("퇴직금", "(退職金) a retirement allowance; a retirement benefit", "퇴직금이 너무 적어서 걱정이에요."),
    ("학용품", "(學用品) school supplies", "학교가 개학하면 학용품이 많이 팔립니다."),
    ("활용", "(活用) use; utilization; to use; to utilize (~하다)", "학원에서 배운 방법을 활용해서 이 요리를 만들었습니다."),
]
_CV_LOAN = [("바이어", "a buyer; a buying agent from abroad", "다음달에 바이어들이 우리 회사를 방문하겠습니다."), ("보너스", "a bonus", "연말에 직원들에게 백 퍼센트 보너스를 주기로 했어요.")]
_CV_GR = [
    ("an attributive form + 줄 알았다", "I thought … (but I was wrong)", "김 선생님이 독신인 줄 알았어요."),
    ("an attributive form + 줄 몰랐다", "I wasn’t aware; I didn’t know", "김 선생님이 결혼한 줄 몰랐어요."),
    ("-다(가) 보니(까)", "conjunctive ending used to express the speaker’s own discovery/realization of something while engaging in an activity", "일하다 보니 배울 게 아주 많아요."),
    ("-은/는 대로", "as soon as", "회사에 도착하는 대로 과장님 사무실로 가세요."),
    ("~(이)나", "a noun marker (emphasizing a number or amount)", "두 시간이나 걸었지만 아직 주유소를 찾지 못했습니다."),
]
_CV_SINO = [("능력", "(能力) ability; capability", "가능, 불가능, 만능, 노력, 실력, 체력"), ("유/무", "(有/無) exist / not to exist", "유능, 유명, 유료, 무능, 무명, 무료"), ("개업", "(開業) opening up a business", "개학, 개강, 개교, 직업, 업무, 창업")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_LOAN}
_EXTRA = {"구내식당": "a (company) cafeteria; a canteen", "만족하다": "to be satisfied", "수입하다": "to import", "수출하다": "to export", "사표": "resignation; a letter of resignation", "여유롭다": "to be free (of obligations); to have elbowroom", "유능하다": "to be able; to be capable", "자유롭다": "to be free; to be unrestricted", "자유롭게": "freely", "퇴직": "retirement; quitting one’s job", "젊다": "to be young", "시골": "the countryside", "도시": "a city", "저축하다": "to save (money)", "직원": "an employee", "무능": "incompetence; lack of ability", "무명": "being unknown; nameless", "무료": "free of charge", "유명": "fame; being famous", "유료": "paid; for a fee", "불만": "dissatisfaction; discontent",
          "가능": "possibility", "불가능": "impossibility", "만능": "being all-powerful; omnipotence", "노력": "effort", "실력": "real ability; skill", "체력": "physical strength", "수력": "waterpower; hydropower", "풍력": "wind power", "부력": "buoyancy; “floating power”", "역도": "weight lifting; “power way”", "역량": "ability; capability; “amount of power”", "역점": "emphasis; stress; “strong point”", "유능하다": "to be able; to be competent", "무능하다": "to be incompetent; “lacking ability”", "전능하다": "to be omnipotent; “to be capable of all”", "가능하다": "to be possible", "불가능하다": "to be impossible",
          "개학": "starting school (after a vacation); “open school”", "개점": "opening a store; opening a shop", "개원": "opening a clinic", "개회": "the opening of a meeting; the opening of a session", "개폐": "opening and shutting", "개전": "the commencement of hostilities; the outbreak of war; “open war”", "부업": "an avocation; a second job (in addition to a regular one); “secondary work”", "농업": "agriculture; farming; “farming business”", "공업": "the manufacturing industry; “manufacturing business”", "업종": "type of business; category of business", "폐업": "closing a business; going out of business; “close a business”", "개강": "the start of a semester’s lectures", "개교": "the founding of a school", "직업": "a job; an occupation", "창업하다": "to found a business"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_YM = [("무독성", "nontoxic"), ("무경험", "inexperience")]
_YM2 = [("유능", "competence (to be able)"), ("무능", "incompetence"), ("유명", "being famous"), ("무명", "being unknown; nameless"), ("유료", "for a fee; paid"), ("무료", "free of charge")]
_NU1 = [("유능하다", "to be able; to be competent"), ("무능하다", "to be incompetent; “lacking ability”"), ("전능하다", "to be omnipotent; “to be capable of all”"), ("가능하다", "to be possible"), ("불가능하다", "to be impossible")]
_NU2 = [("체력", "physical strength"), ("수력", "waterpower; hydropower"), ("풍력", "wind power"), ("부력", "buoyancy; “floating power”")]
_NU3 = [("역도", "weight lifting; “power way”"), ("역량", "ability; capability; “amount of power”"), ("역점", "emphasis; stress; “strong point”")]
_GA1 = [("개학", "starting school (after a vacation); “open school”"), ("개점", "opening a store; opening a shop"), ("개원", "opening a clinic"), ("개회", "the opening of a meeting; the opening of a session"), ("개폐", "opening and shutting"), ("개전", "the commencement of hostilities; the outbreak of war; “open war”")]
_GA2 = [("부업", "an avocation; a second job (in addition to a regular one); “secondary work”"), ("농업", "agriculture; farming; “farming business”"), ("공업", "the manufacturing industry; “manufacturing business”"), ("업종", "type of business; category of business")]

# ================================================================== L1: objectives and Sino-Korean
L1 = lesson(
    "Ch 36 · What the chapter teaches, 유 (有) 무 (無) · 능 (能) 력 (力) · 개 (開) 업 (業)",
    "직장생활 · 유능 · 무능 · 무료 · 능력 · 가능 · 체력 · 개업 · 개학 · 폐업",
    requires=[],
    cards=[
        card("What Chapter 36 teaches (직장생활)",
             "Chapter 36, “Life at Work”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify, ask about, and discuss daily routines and common concerns at work; talk about plans for starting a new business; and identify, ask about, and discuss the typical lifestyle of retirees.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; –다(가) 보니(까), used to express the speaker’s own discovery/realization of something while engaging in an activity; an attributive form + 줄 알았다 (I thought); an attributive form + 줄 몰랐다 (I did not know; I was not aware); ~(이)나 used to emphasize an amount or number; the conjunctive ending –는 대로 (as soon as; immediately after); and the Sino-Korean syllables within 능력 (能力), 유무 (有無), and 개업 (開業)."),
        card("오늘의 漢字語: 유/무 (有/無)",
             "These two Sino-Korean syllables have opposite meanings. 유 (有) means existing or with, whereas 무 (無) means not existing, lacking, or without, and is equivalent to the English prefixes non-, in-, and un-, as in 무독성 (nontoxic) or 무경험 (inexperience). These two syllables are frequently used as prefixes. The book asks you to guess the meaning of 유능/무능, 유명/무명 and 유료/무료 (my answers):",
             tables=[ktable(_YM), ktable(_YM2)]),
        card("Sino-Korean in use: 능력 (能力)",
             "This Sino-Korean word means ability or capability. The first syllable 능 (能) means able or capable, as in 유능하다 (to be able; to be competent), 무능하다 (to be incompetent; “lacking ability”), 전능하다 (to be omnipotent; “to be capable of all”), 가능하다 (to be possible), and 불가능하다 (to be impossible). The second syllable 력 (力) means power(ful), strength, or strong, as in 체력 (physical strength), 수력 (waterpower; hydropower), 풍력 (wind power), and 부력 (buoyancy; “floating power”). When 력 comes at the beginning of a word, the syllable changes to 역, as in 역도 (weight lifting; “power way”), 역량 (ability; capability; “amount of power”), and 역점 (emphasis; stress; “strong point”). Thus the literal meaning of the word 능력 is “capable power” or “able strength”.",
             tables=[ktable(_NU1), ktable(_NU2), ktable(_NU3)]),
        card("Sino-Korean in use: 개업 (開業)",
             "This Sino-Korean word means opening up a business. The Chinese character of the first syllable 개 (開) depicts two saloon doors being in the same plane, implying that something is open. Thus the syllable means open, as in 개학 (starting school [after a vacation]; “open school”), 개점 (opening a store; opening a shop), 개원 (opening a clinic), 개회 (the opening of a meeting; the opening of a session), 개폐 (opening and shutting), and 개전 (the commencement of hostilities; the outbreak of war; “open war”). The second syllable 업 (業) means work or business, as in 부업 (an avocation; a second job [in addition to a regular one]; “secondary work”), 농업 (agriculture; farming; “farming business”), 공업 (the manufacturing industry; “manufacturing business”), and 업종 (type of business; category of business). Thus the literal meaning of the word 개업 is “opening a business”. Keep in mind that the antonym of the word is 폐업 (closing a business; going out of business; “close a business”).",
             tables=[ktable(_GA1), ktable(_GA2), ktable([("개업", "opening a business"), ("폐업", "closing a business; going out of business")])]),
    ],
    exercises=uniq(
        _tr(_YM + _YM2 + _NU1 + _NU2 + _NU3 + _GA1 + _GA2, k=3)
        + [M("What does 유 (有) mean?", "existing; with", ["not existing", "open", "power"], "有."), M("What does 무 (無) mean?", "not existing; lacking; without", ["existing", "open", "work"], "無."), M("What does 능 (能) mean?", "able; capable", ["power", "open", "work"], "유능하다."), M("What does 력 (力) mean?", "power; strength", ["able", "open", "work"], "체력."), M("What does 개 (開) mean?", "open", ["close", "work", "power"], "개학."), M("What does 업 (業) mean?", "work; business", ["open", "power", "able"], "부업."), M("What is the literal meaning of 능력?", "“capable power” or “able strength”", ["“opening a business”", "“not existing”", "“school supplies”"], "능 + 력."), M("What is the literal meaning of 개업?", "“opening a business”", ["“capable power”", "“closing a business”", "“open school”"], "개 + 업."), M("What is the antonym of 개업?", "폐업", ["창업", "부업"], "The book’s note."), M("Why does 력 change to 역 at the beginning of a word?", "A sound rule: 역도, 역량, 역점", ["It never changes", "It is a typo", "It changes only in names"], "The book’s note."),
           F("그 회사는 ___ 상담을 해 줍니다. (free of charge)", "무료", ["유료", "무명"], "무료."), F("이 부서에는 ___한 직원들이 아주 많습니다. (competent)", "유능", ["무능", "철저"], "유능하다."), F("내 동생은 작년에 작은 식당을 ___했습니다. (opened)", "개업", ["폐업", "창업"], "개업하다."), F("그 사람은 ___도 있고 일도 열심히 합니다. (ability)", "능력", ["체력", "노후"], "능력."),
           read_q("유능"), read_q("무료"), read_q("능력"), read_q("개업"), read_q("폐업")]
    ),
)

# ================================================================== L2: Vocabulary Builder
_BOX1 = ["개업", "구내식당", "능력", "답답하다", "만족하다", "분위기", "불만", "사표", "상사", "수입", "수출", "야근", "업무", "여유롭다", "유능(하다)", "은퇴", "자유롭다", "노후"]
_SA = [("도시는 답답해요. 시골에서 자유롭게 생활하고 싶어요.", "답답하다 / 자유롭다", "A", "to be stuffy / to be free"), ("젊었을 때 열심히 저축하면 노후에 잘 살 수 있습니다.", "젊다 / 노후", "A", "to be young / old age"), ("유능한 상사는 직원에게 일을 시키지 않습니다. 능력이 없는 상사는 직원에게 일을 많이 시킵니다.", "유능하다 / 능력이 없다", "A", "to be capable / to lack ability"), ("한국은 중국에 자동차를 수출하고 컴퓨터를 수입합니다.", "수출하다 / 수입하다", "A", "to export / to import"), ("회사 분위기가 좋아서 만족합니다. 하지만 야근이 너무 많아서 불만입니다.", "만족하다 / 불만", "A", "to be satisfied / dissatisfaction"), ("저희 아버지는 쉰다섯 살에 퇴직하셨습니다. 은퇴 후에는 고향에서 사십니다.", "퇴직 / 은퇴", "S", "retirement / retirement")]
_MJ = [("김미진 씨는 컴퓨터를 수출하는 회사에 다닙니다.", "Kim Mijin works at a company that exports computers."), ("이 회사에 다닌 지 삼 년 되었습니다.", "It has been three years since she started at this company."), ("그런데 이 직장은 너무 힘듭니다.", "But this job is too hard."), ("업무가 너무 많고 밤 늦게까지 야근도 해야 합니다.", "There is too much work and she also has to work overtime until late at night."), ("김미진 씨는 직장에 사표를 내려고 합니다.", "Kim Mijin intends to hand in her resignation."), ("퇴직 후에 미진 씨는 꽃집을 개업할 생각입니다.", "After leaving, Mijin plans to open a flower shop."), ("꽃집을 하면 시간을 여유롭게 쓸 수 있습니다.", "If she runs a flower shop, she can use her time at leisure."), ("그리고 노후에도 이 일을 계속 할 수 있습니다.", "And she can keep doing this work in her old age too.")]
_VB_PAIRS = [("개업", "opening of a business"), ("구내식당", "a (company) cafeteria"), ("능력", "ability; capability"), ("답답하다", "to be stuffy; to be suffocating"), ("만족하다", "to be satisfied"), ("분위기", "an atmosphere; an ambience"), ("불만", "dissatisfaction; discontent"), ("사표", "resignation; a letter of resignation"), ("상사", "one’s superior"), ("수입", "import"), ("수출", "export"), ("야근", "night duty; working overtime into the night"), ("업무", "work; duties; job responsibilities"), ("여유롭다", "to be free (of obligations)"), ("은퇴", "retirement"), ("자유롭다", "to be free; to be unrestricted"), ("노후", "one’s old age")]
L2 = lesson(
    "Ch 36 · Vocabulary Builder: new words, synonyms and antonyms, and a paragraph",
    "개업 · 구내식당 · 능력 · 답답하다 · 만족하다 · 분위기 · 불만 · 사표 · 상사 · 수입 · 수출 · 야근 · 업무 · 은퇴 · 노후",
    requires=[],
    cards=[
        card("새 단어: the words in the box",
             "The book gives eighteen core words: 개업, 구내식당, 능력, 답답하다, 만족하다, 분위기, 불만, 사표, 상사, 수입, 수출, 야근, 업무, 여유롭다, 유능(하다), 은퇴, 자유롭다, 노후. You circle the ones you do not recognize, look them up and write their English meanings; then you write positive statements about your job and employer with 분위기, 만족하다, 노후, 개업, 여유롭다, 업무, 상사, 유능(하다), and negative statements with 구내식당, 답답하다, 능력, 은퇴, 야근, 사표, 수출, 불만, 수입, 자유롭다, and compare them with a neighbor and your teacher. The meanings (the Core Vocabulary’s; 구내식당 is mine):",
             tables=[ktable(_VB_PAIRS)]),
        card("Activity 1: synonyms or antonyms?",
             "The book gives six sentences. You underline the two synonyms or antonyms in each, circle “S” if they are synonyms or “A” if they are antonyms, and write their English meanings. The sentences are the book’s (55세 is spelled 쉰다섯 살); the answers are mine:",
             tables=[table(["Sentence", "The pair (mine)", "S or A (mine)", "English (mine)"], [list(r) for r in _SA], say=[0, 1])]),
        card("Activity 3: an employee’s work life, completed",
             "The book gives a description with six blanks and a box (노후 개업 수출 야근 사표 여유롭게). The text below is completed with my answers, in this order: 수출, 야근, 사표, 개업, 여유롭게, 노후; the 3년 is spelled out. The English is mine.",
             examples=passage(_MJ)),
        card("Activities left out", "Activities 2 and 4 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 5 (그만!, a ball-passing game in which you describe a word from a card without saying it) are computer and game activities."),
    ],
    exercises=uniq(
        vocab_exercises(_VB_PAIRS)
        + _tr(_MJ, k=3)
        + [M("Are “" + b + "” synonyms or antonyms?", "Antonyms" if c == "A" else "Synonyms", ["Synonyms" if c == "A" else "Antonyms"], "My answer.") for a, b, c, d in _SA]
        + [F("김미진 씨는 컴퓨터를 ___하는 회사에 다닙니다. (export)", "수출", ["수입", "개업"], "수출하다."), F("업무가 너무 많고 밤 늦게까지 ___도 해야 합니다. (overtime)", "야근", ["퇴근", "출근"], "야근."), F("김미진 씨는 직장에 ___를 내려고 합니다. (resignation)", "사표", ["연금", "보너스"], "사표."), F("퇴직 후에 미진 씨는 꽃집을 ___할 생각입니다. (open)", "개업", ["폐업", "수출"], "개업하다."), F("꽃집을 하면 시간을 ___ 쓸 수 있습니다. (at leisure)", "여유롭게", ["답답하게", "간단히"], "여유롭게."), F("그리고 ___에도 이 일을 계속 할 수 있습니다. (old age)", "노후", ["은퇴", "인생"], "노후."),
           read_q("개업"), read_q("구내식당"), read_q("사표를 내려고 합니다"), read_q("여유롭게 쓸 수 있습니다"), read_q("노후에도 이 일을 계속 할 수 있습니다")]
    ),
)

# ================================================================== L3: Topic A
_A_TXT = [
    ("김인철 씨는 하루 일과를 오전 다섯 시 반에 시작합니다.", "Mr. Kim Incheol starts his daily routine at half past five in the morning."),
    ("입사 초에는 이른 아침에 일어나는 것이 힘들었지만, 이제는 익숙해졌습니다.", "At the beginning of his employment it was hard to get up early in the morning, but now he has gotten used to it."),
    ("정장을 하고 여섯 시 반에 집을 나와서 지하철을 타고 출근합니다.", "He dresses up, leaves home at half past six, and commutes by subway."),
    ("아침은 회사 근처 식당에서 간단히 먹습니다.", "He has breakfast simply at a restaurant near the company."),
    ("김인철 씨 회사는 컴퓨터 부품을 수출하는 회사입니다.", "Mr. Kim’s company is a company that exports computer parts."),
    ("외국어 실력이 업무에 아주 중요하기 때문에 출근 전에 영어학원에 갑니다.", "Because foreign language ability is very important for the work, he goes to an English academy before going to work."),
    ("회사에서는 오전에 밤새 해외 바이어들에게서 온 이메일을 확인하고 답장을 합니다.", "At the company, in the morning he checks the e-mails that came overnight from overseas buyers and replies."),
    ("점심은 보통 구내식당에서 동료들과 같이 합니다.", "He usually has lunch with his colleagues in the company cafeteria."),
    ("오후에는 보고서를 작성하고 부서 회의에 참석합니다.", "In the afternoon he writes reports and attends a department meeting."),
    ("퇴근 후에는 회사에서 지원하는 사내 테니스 모임에 나갑니다.", "After work he goes to the in-company tennis club supported by the company."),
    ("모임에 나가서 대인관계도 넓히고 하루의 피로도 풉니다.", "At the club he broadens his interpersonal relationships and also relieves the day’s fatigue."),
]
_A_WORDS = ["간단히", "구내", "넓히다", "답장", "대인관계", "바이어", "밤새", "보고서", "부품", "사내", "성공", "수출", "업무", "유능", "이르다", "익숙하다", "일과", "정장", "지원"]
_NEWS1 = [("요즘 출퇴근 시간을 이용해 외국어를 배우는 회사원이 많아지고 있다.", "These days the number of company employees who use their commuting time to learn foreign languages is increasing."), ("서울 여의도의 어학원들은 이른 새벽부터 영어회화 수업을 듣는 회사원들로 복잡하다.", "Language academies in Yeouido, Seoul, are crowded from early dawn with company employees taking English conversation classes."), ("육 개월 동안 영어학원에 다니고 있는 수출회사 근무 김이정 씨는 유럽의 바이어들과 영어로 말하고 계약서도 영어로 작성해야 하기 때문에 영어 실력이 아주 중요하다고 말했다.", "Ms. Kim Yijeong, who works at an export company and has been attending an English academy for six months, said that English ability is very important because she has to speak with European buyers in English and write contracts in English too."), ("또 학원에 직접 가지 않고 외국어를 배울 수 있는 인터넷 사이트도 인기를 얻고 있다.", "Also, internet sites where you can learn a foreign language without going to an academy in person are gaining popularity.")]
L3 = lesson(
    "Ch 36 · Topic A: A new employee’s day (신입사원의 하루)",
    "신입사원의 하루 · 일과 · 정장 · 출근 · 구내식당 · 보고서 · 부서 회의 · 사내 테니스 모임 · 외국어 배우는 회사원",
    requires=[],
    cards=[
        card("Topic A: A new employee’s day (신입사원의 하루)",
             "The following description is about a new employee’s typical work day. (The English is mine; the book gives none; the times are spelled out in Hangul.)",
             examples=passage(_A_TXT)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 답장(하다), 성공(하다), 수출(하다), 유능(하다), 정장(하다) and 지원(하다) take the forms in parentheses.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Follow-up 1 (Reading): a news article about employees learning languages",
             "The following news article is about a trend among company employees in Seoul. The book’s hint: if you encounter unknown words, focus on the words you know and use your dictionary as necessary. It asks you to translate an underlined part and to fill in a table in English (recent trend among company employees; ways to follow the recent trend). The article is the book’s (the book writes “김이정 (여, 수출회사 근무) 씨”; here it is “수출회사 근무 김이정 씨”; 6개월 is spelled out; the quotation marks are dropped). The English is mine.",
             examples=passage(_NEWS1)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Item", "Answer (mine)"], [["Recent trend among company employees", "More employees are learning foreign languages in their commuting time"], ["Ways to follow the trend", "Taking English conversation classes at academies from early dawn; using internet sites that teach a foreign language without going to an academy"]])]),
        card("Activities left out", "Follow-up 2 (listening to three short conversations in which a new employee with difficulty at work receives advice from a friend), the Topic Presentation A study steps (SMART Board) and Activity 1 (SMART Board) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT + _NEWS1, k=3)
        + [M("When does 김인철 start his day?", "5:30 a.m.", ["6:30 a.m.", "7:30 a.m.", "9:00 a.m."], "다섯 시 반."), M("How does he commute?", "By subway", ["By bus", "By car", "On foot"], "지하철을 타고."), M("What does his company export?", "Computer parts", ["Clothes", "Cars", "Food"], "컴퓨터 부품."), M("Where does he go before work?", "An English academy", ["A gym", "A bank", "A library"], "영어학원."), M("What does he do in the morning at the company?", "Checks e-mails from overseas buyers and replies", ["Writes reports", "Attends meetings", "Eats lunch"], "이메일을 확인하고 답장."), M("Where does he usually have lunch?", "The company cafeteria", ["A restaurant", "Home", "A park"], "구내식당."), M("What does he do after work?", "Goes to the in-company tennis club", ["Studies at home", "Drinks with friends", "Works overtime"], "사내 테니스 모임."),
           F("김인철 씨는 하루 ___를 오전 다섯 시 반에 시작합니다. (daily routine)", "일과", ["일정", "업무"], "일과."), F("입사 초에는 이른 아침에 일어나는 것이 힘들었지만 이제는 ___. (got used to)", "익숙해졌습니다", ["이르렀습니다", "성공했습니다"], "익숙하다."), F("아침은 회사 근처 식당에서 ___ 먹습니다. (simply)", "간단히", ["밤새", "넓히"], "간단히."), F("오후에는 ___를 작성하고 부서 회의에 참석합니다. (a report)", "보고서", ["답장", "부품"], "보고서."), F("모임에 나가서 ___도 넓히고 하루의 피로도 풉니다. (interpersonal relationships)", "대인관계", ["보고서", "정장"], "대인관계."),
           read_q("신입사원의 하루"), read_q("김인철 씨는 하루 일과를 오전 다섯 시 반에 시작합니다"), read_q("컴퓨터 부품을 수출하는 회사입니다"), read_q("점심은 보통 구내식당에서 동료들과 같이 합니다"), read_q("사내 테니스 모임에 나갑니다")]
    ),
)

# ================================================================== L4: Topic A activities: survey of new employees
_SV = [("우리 회사 신입사원이 생각하는 성공의 조건은 대인관계와 영어", "The condition for success that our company’s new employees think of: interpersonal relationships and English"), ("회사 인사부에서 작년 우리 기업 신입사원 마흔일곱 명을 대상으로 설문조사를 했다.", "The company’s personnel department conducted a survey last year of forty-seven new employees of our company."), ("성공하기 위한 조건이 무엇이냐는 질문에 삼십이 점 칠 퍼센트의 신입사원이 대인관계라고 답했다.", "To the question of what the condition for success is, 32.7% of the new employees answered interpersonal relationships."), ("그리고 응답자의 이십사 점 사 퍼센트는 성공의 조건으로 영어실력이라고 대답했으며, 십팔 점 육 퍼센트는 대학원 졸업이나 박사학위와 같은 학력, 십일 점 육 퍼센트는 외국유학 경험을 꼽았다.", "And 24.4% of respondents answered English ability as a condition for success, 18.6% named educational background such as a graduate school degree or a doctorate, and 11.6% named study-abroad experience."), ("우리 회사의 좋은 점은 무엇인가라는 질문에는 회사의 자기개발 지원이 일 위를 차지했고 우리회사의 나쁜 점을 묻는 질문에는 삼십오 퍼센트가 짧은 휴가라고 대답했다.", "To the question “What is good about our company?”, the company’s support for self-development took first place, and to the question asking about the bad points of our company, 35% answered a short vacation.")]
L4 = lesson(
    "Ch 36 · Topic A activities: what new employees think leads to success",
    "성공의 조건 · 대인관계 · 영어실력 · 학력 · 외국유학 경험 · 자기개발 지원 · 짧은 휴가 · 설문조사",
    requires=[],
    cards=[
        card("Activity 2 (Reading and speaking): a survey of new employees",
             "Read the survey results and complete the tasks. The book’s hint: if you encounter unknown words, focus on the words you know and use your dictionary as necessary. The task: a. fill in a table with appropriate English bar-graph labels for a bar chart of four bars (가 32.7%, 나 24.4%, 다 18.6%, 라 11.6%; one label, “Educational Background” for 다, is provided); b. read again and fill in the three survey questions in English; c. write what you think are the keys to success at work; d. in pairs, ask your partner in Korean about keys to success and present the combined ideas to the class. The article is the book’s (the percentages and the number of people are spelled out in Hangul; the quotation marks are dropped); the English is mine.",
             examples=passage(_SV)),
        card("The tables filled in (mine)", "The book leaves the tables blank; these are my answers.",
             tables=[table(["Bar", "Label (mine)"], [["가 (32.7%)", "Interpersonal relationships"], ["나 (24.4%)", "English ability"], ["다 (18.6%)", "Educational background (a graduate degree or a doctorate)"], ["라 (11.6%)", "Study-abroad experience"]]), table(["The three survey questions", "English (mine)"], [["1", "What are the conditions for success?"], ["2", "What is good about our company?"], ["3", "What is bad about our company?"]])]),
        card("Activities left out", "Activity 3 (김 대리의 하루: listening to two recorded messages about Mr. Kim’s work day, Day 1 and Day 2, and exchanging the information in Korean with a partner from the other group) is an audio and group activity."),
    ],
    exercises=uniq(
        _tr(_SV, k=3)
        + [M("How many new employees were surveyed?", "Forty-seven", ["Twenty-four", "Seventy-four", "Forty"], "마흔일곱 명."), M("What was the top condition for success?", "Interpersonal relationships", ["English", "A degree", "Study abroad"], "대인관계 32.7%."), M("What was second?", "English ability", ["Interpersonal relationships", "A degree", "Study abroad"], "영어실력 24.4%."), M("Which condition got the lowest percentage?", "Study-abroad experience", ["English", "Education", "Interpersonal relationships"], "11.6%."), M("What was the top good point of the company?", "Support for self-development", ["High salary", "Short hours", "A cafeteria"], "자기개발 지원."), M("What did 35% say was bad about the company?", "A short vacation", ["Low pay", "A long commute", "Overtime"], "짧은 휴가."),
           F("회사 인사부에서 신입사원 마흔일곱 명을 ___으로 설문조사를 했다. (target)", "대상", ["이유", "기회"], "대상."), F("32.7%의 신입사원이 ___라고 답했다. (interpersonal relationships)", "대인관계", ["영어실력", "학력"], "대인관계."), F("응답자의 24.4%는 성공의 조건으로 ___라고 대답했다. (English ability)", "영어실력", ["대인관계", "학력"], "영어실력."), F("우리 회사의 ___은 짧은 휴가라고 대답했다. (bad point)", "나쁜 점", ["좋은 점", "장점"], "나쁜 점."), F("회사의 자기개발 지원이 일 ___를 차지했다. (first place)", "위", ["등", "번"], "일 위."),
           read_q("성공의 조건"), read_q("대인관계와 영어"), read_q("성공하기 위한 조건이 무엇이냐"), read_q("짧은 휴가"), read_q("자기개발 지원")]
    ),
)

# ================================================================== L5: Topic B
_B_DLG = [
    ("현태", "종석아, 오랜만이다. 요즘 회사 생활은 어때?", "Jongseok, it’s been a while. How is life at the company these days?"),
    ("종석", "힘들어 죽겠어요, 형. 요즘 매일 야근이에요.", "It’s killing me, hyung. These days it’s overtime every day."),
    ("현태", "그래? 참, 너 대리로 승진했지? 축하한다.", "Really? Oh, you got promoted to assistant manager, right? Congratulations."),
    ("종석", "네, 근데 대리로 일하다 보니 일만 더 많아요.", "Yes, but as I work as an assistant manager, I find there is just more work."),
    ("현태", "하지만 능력을 인정받고 다양한 일을 배우잖아?", "But you’re recognized for your ability and learn a variety of work, aren’t you?"),
    ("종석", "그건 맞아요. 그런데 회사 규모가 작아서 일도 많아요.", "That’s true. But the company is small so there’s a lot of work too."),
    ("현태", "우리 회사 같은 대기업에서는 매일 같은 일을 반복하잖아. 그래서 지겨워하는 동료들도 많아.", "In a large company like mine you repeat the same work every day. So many colleagues are bored."),
    ("종석", "그렇구나. 대기업 직원들은 다 만족하는 줄 알았는데.", "I see. I thought all large-company employees were satisfied."),
    ("현태", "그렇지 않아. 그래서 요즘 중소기업으로 이직하는 동료들이 많이 있어.", "Not so. That’s why many colleagues these days are changing jobs to small and medium companies."),
    ("종석", "그래도 형네 회사는 보너스도 많이 주고, 재택근무도 가능하잖아요.", "Still, your company gives big bonuses and allows working from home."),
    ("현태", "물론 장점도 많아. 하지만 출장도 자주 있고 상사와의 관계도 힘들어.", "Of course there are many advantages. But there are frequent business trips and the relationship with my boss is hard too."),
    ("종석", "그래요? 우리 회사는 대기업하고 연봉 차이는 있어도 분위기는 자유로워요.", "Is that so? My company has a salary gap with large companies but the atmosphere is free."),
]
_B_WORDS = ["규모", "능력", "대리", "만족", "반복", "보너스", "분위기", "불만족", "상사", "야근", "연봉", "인정", "자유", "재택근무", "지겹다", "차이", "출장"]
_B_STUDY = [("출장", "a business trip"), ("인정", "recognition; acknowledgment"), ("대리", "an assistant manager; a deputy"), ("불만족", "dissatisfaction"), ("차이", "a difference; a gap"), ("이직", "change of occupation"), ("규모", "size; scale"), ("만족", "satisfaction"), ("재택근무", "telecommuting; working from home"), ("연봉", "an annual salary"), ("능력", "ability"), ("야근", "night duty; working overtime"), ("자유롭다", "to be free"), ("상사", "one’s superior"), ("분위기", "an atmosphere")]
L5 = lesson(
    "Ch 36 · Topic B: You got promoted to assistant manager, right? (너 대리로 승진했지?)",
    "너 대리로 승진했지 · 승진 · 야근 · 대기업 · 중소기업 · 이직 · 보너스 · 재택근무 · 연봉 · 출장 · 분위기",
    requires=[],
    cards=[
        card("Topic B: You got promoted to assistant manager, right? (너 대리로 승진했지?)",
             "Two friends meet up at a coffee shop and talk about their work at different companies. (The English is mine; the book gives none.)",
             examples=dlg(_B_DLG)),
        card("Footnote: 이직", "이직 can mean job change or job quitting, depending on which Chinese character (移 or 離) is used. In this sentence, the word 이직 (移職) (job change) is used.",
             tables=[ktable([("이직", "change of occupation (移職); separation from one’s position, quitting one’s job (離職)")])]),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); 만족(하다/스럽다), 반복(하다/되다), 불만족(스럽다), 야근(하다), 이직(하다), 인정(하다/받다), 자유(롭다) and 출장(가다) take the forms in parentheses. –다(가) 보니(까) and –줄 알다/모르다 are explained in the grammar.",
             tables=[ktable(_rows(_B_WORDS)), table(["Pattern", "Meaning"], [["-다(가) 보니(까)", "discovery or realization while doing something"], ["-줄 알다 / 모르다", "I thought … / I did not know …"]])]),
        card("Study step a: fill in the table", "The book asks you to fill in the table below with appropriate English or Korean (a few answers are given there: an assistant manager; to be unsatisfied; size; to be satisfied; ability; to work overtime). The pairs:",
             tables=[ktable(_B_STUDY)]),
        card("Activities left out", "The Topic Presentation B study steps (SMART Board and reading in pairs as Hyuntae and Jongseok) are computer and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG), k=3)
        + [M("What did 종석 get?", "A promotion to assistant manager", ["A bonus", "A new job", "A transfer"], "대리로 승진."), M("What is 종석’s complaint?", "There is just more work and overtime every day", ["Low pay only", "No work", "No boss"], "일만 더 많아요."), M("Why does 종석 have a lot of work?", "The company is small", ["The company is large", "He is new", "He is lazy"], "회사 규모가 작아서."), M("What do large-company workers do every day, says 현태?", "Repeat the same work", ["Travel", "Rest", "Study"], "매일 같은 일을 반복."), M("Where are many colleagues moving to?", "Small and medium enterprises", ["Large companies", "Abroad", "Schools"], "중소기업으로 이직."), M("What advantages does 현태’s company have?", "Big bonuses and working from home", ["A short commute", "A low workload", "Free housing"], "보너스, 재택근무."), M("What are 현태’s company’s disadvantages?", "Frequent business trips and a hard relationship with his boss", ["Low pay", "Small size", "A bad cafeteria"], "출장, 상사와의 관계."), M("How is 종석’s company’s atmosphere?", "Free", ["Strict", "Gloomy", "Noisy"], "자유로워요."),
           F("너 ___로 승진했지? (assistant manager)", "대리", ["상사", "규모"], "대리."), F("대리로 일하다 보니 ___만 더 많아요. (work)", "일", ["월급", "휴가"], "일."), F("하지만 ___을 인정받고 다양한 일을 배우잖아? (ability)", "능력", ["연봉", "야근"], "능력."), F("대기업과 ___ 차이는 있어도 분위기는 자유로워요. (annual salary)", "연봉", ["보너스", "규모"], "연봉."), F("보너스도 많이 주고, ___도 가능하잖아요. (working from home)", "재택근무", ["출장", "야근"], "재택근무."),
           read_q("너 대리로 승진했지"), read_q("힘들어 죽겠어요"), read_q("요즘 매일 야근이에요"), read_q("대기업 직원들은 다 만족하는 줄 알았는데"), read_q("우리 회사는 분위기는 자유로워요")]
    ),
)

# ================================================================== L6: Topic B activities
_KR = [("코리아 리쿠루트가 직장인 구백칠십오 명에게 세 가지 질문을 했다.", "Korea Recruit asked 975 office workers three questions."), ("첫째 질문은 직장 생활에서 무엇이 가장 힘들었나, 둘째, 한 해 동안 직장에서 노력한 것은 무엇인가, 셋째, 내년에 하고 싶은 일은 무엇인가이었다.", "The first question was “What was the hardest in work life?”, the second “What did you strive for at work during the year?”, and the third “What do you want to do next year?”"), ("첫 번째 질문에 대한 대답으로 낮은 연봉이 일 위, 상사와의 문제가 이 위, 그리고 대인관계의 어려움, 반복되는 야근과 자기 개발 시간 부족 순이었다.", "As answers to the first question, low annual income was first, problems with the boss second, and then difficulty in interpersonal relationships, repeated overtime and lack of time for self-development, in that order."), ("두 번째 질문에 대한 답으로 일 위는 이직, 이 위는 자격증 취득, 그 뒤로 자기 개발, 건강 등 이었다.", "As answers to the second question, first was changing jobs, second was acquiring certificates, and after that self-development, health and so on."), ("마지막 질문에는 이직이라는 답이 가장 많았고, 다음으로 외국어 공부와 자기 개발 그리고 자격증 취득 순이었다.", "To the last question, the answer “changing jobs” was the most common, followed by foreign language study and self-development, and then acquiring certificates, in that order.")]
_MH = [("직장인 육십구 퍼센트가 꼽았다 정신 건강에 영향 미치는 일 위는 이 사람", "69% of office workers picked: the number one influence on mental health is this person"), ("직장 상사가 직장인 정신 건강에 미치는 영향이 가장 높다는 설문조사 결과가 발표됐다.", "The results of a survey have been announced that a boss has the highest influence on an office worker’s mental health."), ("영국의 유케이지 노동인구연구소는 열 개국의 삼천사백 명 직장인을 대상으로 업무 스트레스, 직장이 정신 건강에 미치는 영향, 일에 대한 감정 등에 대한 설문을 진행했다.", "The UKG Workforce Institute of the UK conducted a survey of 3,400 office workers in ten countries about work stress, the effect of the workplace on mental health, feelings about work and so on."), ("그 결과, 육십구 퍼센트의 직장인이 정신 건강에 가장 큰 영향을 미치는 사람으로 직장 상사를 꼽았다.", "As a result, 69% of office workers picked their boss as the person with the greatest influence on mental health."), ("특히 직장 상사에게 받는 압박 등 부정적인 정신 환경은 가정생활 칠십일 퍼센트, 일상 육십사 퍼센트, 인간관계 육십이 퍼센트 등의 순으로 직장인에 좋지 않은 영향을 미쳤다.", "In particular, a negative mental environment such as pressure from the boss had a bad effect on office workers in the order of home life (71%), daily life (64%), human relationships (62%) and so on."), ("하지만 이 중 삼십팔 퍼센트는 거의 또는 절대 직장 상사와 관계 개선을 위한 대화를 나누지 않았다.", "But 38% of them had almost or absolutely never had a conversation with their boss to improve the relationship."), ("그 이유는 스스로 해결할 수 있어야 해서 이십 퍼센트, 상사가 신경을 쓰지 않아서 십육 퍼센트, 상사가 너무 바빠서 십삼 퍼센트 순이었다.", "The reasons were, in order, that they should be able to solve it themselves (20%), that the boss doesn’t care (16%), and that the boss is too busy (13%)."), ("직장 결정에 대한 질문에서는 응답자 팔십 퍼센트 이상이 고액의 연봉보다 정신 건강을 지킬 수 있는 직장을 선호한다고 답했다.", "In the question about choosing a workplace, more than 80% of respondents answered that they prefer a workplace that can protect their mental health over a high salary."), ("매니저 이상 직급의 직장 상사 칠십 퍼센트도 같은 답변을 했다.", "70% of bosses at manager level or above gave the same answer.")]
L6 = lesson(
    "Ch 36 · Topic B activities: surveys of workers",
    "직장인 설문조사 · 낮은 연봉 · 상사와의 문제 · 이직 · 자격증 취득 · 정신 건강 · 직장 상사 · 고액의 연봉",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): a survey by Korea Recruit",
             "Read the survey results and complete the tasks. The book glosses 취득: acquisition. It asks you to: a. write the three survey questions in English (the second, “What have you strived for the most at your workplace this past year?”, is given); b. check the two responses to the first question among: lack of time for self-improvement; low annual income; traffic jam during the commute hour; unfairness in promotions. The text is the book’s (the number is spelled out and the quotation marks are dropped); the English is mine.",
             examples=passage(_KR)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Item", "Answer (mine)"], [["1. First question", "What was the hardest thing in your work life?"], ["3. Third question", "What do you want to do next year?"], ["b. The two responses to the first question", "Lack of time for self-improvement; low annual income (traffic jam and unfairness in promotions are not mentioned)"]])]),
        card("Activity 2 (Reading): a survey on the workplace and mental health",
             "Read the text about the survey results on the relationship between the workplace and mental health. The book asks: 1. Who responded to the survey? 2. Fill in the table in English for paragraphs (나), (다) and (라) with the topic and the result. The paragraphs (가) to (라) are the book’s; the paragraph letters, the triangle marks and the quotation marks are dropped, and the numbers are spelled out in Hangul. The English is mine.",
             examples=passage(_MH)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Item", "Answer (mine)"], [["1. Who responded?", "3,400 office workers in ten countries, surveyed by the UKG Workforce Institute of the UK"], ["Paragraph (나): topic and result", "Who most affects mental health: 69% picked their boss; the boss’s pressure also hurt home life (71%), daily life (64%) and human relationships (62%)"], ["Paragraph (다): topic and result", "Talking with the boss to improve the relationship: 38% almost or absolutely never did; reasons: should solve it themselves (20%), boss doesn’t care (16%), boss too busy (13%)"], ["Paragraph (라): topic and result", "Choosing a workplace: more than 80% prefer a job that protects mental health to a high salary; 70% of managers and above agree"]])]),
        card("Activities left out", "Follow-up 2 (listening to three conversations in which an employee discusses his work with a junior co-worker and filling in the good and bad points), Activities 1 and 3 (a word-review sentence activity and listening to three short conversations about a man’s satisfaction with his work) and Activity 4 (listening to a new employee and an experienced employee, group exchange and a flip-chart presentation) are audio and group activities."),
    ],
    exercises=uniq(
        _tr(_KR + _MH[1:], k=3)
        + [M("How many workers did Korea Recruit ask?", "975", ["97", "9,750", "75"], "구백칠십오 명."), M("What was the most common answer to the first question?", "Low annual income", ["Problems with the boss", "Lack of time", "Overtime"], "낮은 연봉."), M("What was the most common answer to the last question?", "Changing jobs", ["Language study", "Certificates", "Health"], "이직."), M("Who has the greatest influence on mental health, per the UKG survey?", "The boss", ["Family", "Friends", "Coworkers"], "직장 상사."), M("What percentage picked the boss?", "69%", ["38%", "80%", "20%"], "육십구 퍼센트."), M("How many countries were surveyed?", "Ten", ["Three", "Twenty", "Five"], "열 개국."), M("What do over 80% prefer?", "A job that protects mental health over a high salary", ["A high salary", "A short commute", "A big company"], "정신 건강을 지킬 수 있는 직장."),
           F("직장 ___가 직장인 정신 건강에 미치는 영향이 가장 높다. (boss)", "상사", ["동료", "부하"], "직장 상사."), F("그 결과, 육십구 퍼센트의 직장인이 직장 상사를 ___. (picked)", "꼽았다", ["만났다", "그만두었다"], "꼽다."), F("고액의 ___보다 정신 건강을 지킬 수 있는 직장을 선호한다. (annual salary)", "연봉", ["보너스", "휴가"], "연봉."), F("첫 번째 질문에 대한 대답으로 낮은 ___이 일 위였다. (annual salary)", "연봉", ["보너스", "야근"], "낮은 연봉."), F("두 번째 질문에 대한 답으로 이 위는 ___ 취득이었다. (certificate)", "자격증", ["이직", "건강"], "자격증 취득."),
           read_q("직장인 설문조사"), read_q("낮은 연봉이 일 위였다"), read_q("직장 상사를 꼽았다"), read_q("정신 건강"), read_q("고액의 연봉보다 정신 건강을 지킬 수 있는 직장을 선호한다")]
    ),
)

# ================================================================== L7: Grammar A: -다(가) 보니(까)
_G1 = [("한국말을 배우다가 보니까 일본말도 배우고 싶어요.", "As I have been learning Korean, (I find) I want to learn Japanese as well."), ("몬트레이에 살다가 보니까 바닷가 도시가 좋아졌어요.", "Having lived in Monterey, (I discovered) I like coastal cities.")]
_G2 = [("매일 컴퓨터를 하다 보니까 눈이 아파요.", "Having worked on the computer every day, I discover that my eyes hurt."), ("한국어를 공부하다 보니 한국어가 재미있어요.", "Having studied Korean, I find it is fun."), ("한 달 동안 출장을 와 있다 보니 가족이 보고 싶어요.", "Having been on a business trip for a month, I find myself missing my family.")]
_G3 = [("한국말을 배우다 보니까 한국말이 재미있어요.", "I discover Korean is fun while I am learning Korean."), ("한국말을 배워 보니까 한국말이 재미있어요.", "I discover Korean is fun after I learned Korean.")]
_GM = [("피자를 먹다", "to eat pizza"), ("피자를 먹다 보니 맛이 좀 이상해요.", "As I ate the pizza, I found the taste a little strange.")]
_GLA = ["시험 공부를 하다", "책을 읽다", "오래 걷다", "대기업에 근무하다", "친구들과 얘기하다"]
_GLB = ["피곤하다", "밤 열두 시가 다 되다", "장점이 많다", "잠이 오다", "머리가 아프다"]
_GMINE = [("시험 공부를 하다 보니 피곤해졌어요.", "As I studied for the exam, I found I got tired."), ("책을 읽다 보니 밤 열두 시가 다 됐어요.", "As I read the book, I found it was almost twelve at night."), ("오래 걷다 보니 머리가 아파요.", "As I walked a long time, I found my head hurts."), ("대기업에 근무하다 보니 장점이 많아요.", "Having worked at a large company, I find there are many advantages."), ("친구들과 얘기하다 보니 잠이 와요.", "As I talked with friends, I found I feel sleepy.")]
L7 = lesson(
    "Ch 36 · Grammar A: the conjunctive ending –다(가) 보니(까)",
    "-다(가) 보니(까) · 배우다 보니까 · 살다 보니까 · 하다 보니 · 배워 보니까 · 발견 · 깨달음",
    requires=[],
    cards=[
        card("Having been doing something, I find …",
             "The conjunctive ending –다(가) 보니(까) literally means “because I (stop to) see (what I am doing or what I have been doing)”. It is made up of –다(가) and –보니(까), which you were introduced to in Chapters 20 and 31, respectively.\n\n"
             "–다(가) 보니(까) is used to express the speaker’s discovery or realization while engaging in another activity or being in a certain state. Thus, it translates to “having been doing something, I find/discover”. For example (the English is the book’s):",
             examples=passage(_G1)),
        card("What the examples show", "In the first sentence, the speaker finds himself wanting to learn Japanese while learning Korean (probably because he sees a close relationship between the languages). In the second sentence, the speaker realizes he came to like coastal cities while living in Monterey (probably because of his good experience living in Monterey)."),
        card("Expressing a discovery/realization of something while engaging in an activity", "action verb stem + 다(가) 보니(까). More examples (the book writes 한국어를 공부하다 보니 (한국어가) 재미있어요 with an optional topic; the English is the book’s):", examples=passage(_G2)),
        card("참고: –다(가) 보니(까) and –아/어 보니(까)",
             "Both conjunctive endings are used to express the speaker’s discovery or realization of something. However, –다(가) 보니(까) expresses a discovery or realization while engaging in another activity or being in a certain state. On the other hand, –아/어 보니(까) expresses a discovery or realization after engaging in another activity or being in a certain state. For example (the book’s explanation): in the first sentence the speaker discovers Korean is fun while he is learning Korean; in the second sentence the speaker discovers Korean is fun after he learned Korean. (The English is mine.)",
             examples=passage(_G3)),
        card("Follow-up 1 (Listening, reading and speaking): List A and List B and the model",
             "In pairs, Student A picks a phrase from List A and reads it aloud; Student B picks a phrase from List B that can be logically connected and completes the sentence with –다(가) 보니(까). The book notes the answers may vary. List A: 시험 공부를 하다; 책을 읽다; 오래 걷다; 대기업에 근무하다; 친구들과 얘기하다. List B: 피곤하다; 밤 열두 시가 다 되다 (the book writes 12시); 장점이 많다; 잠이 오다; 머리가 아프다. The book’s model, then my sample sentences (the English is mine):",
             examples=dlg([("A", _GM[0][0], _GM[0][1]), ("B", _GM[1][0], _GM[1][1])]) + passage(_GMINE)),
        card("Activities left out", "Follow-up 2 (listening to three short conversations in which two friends discuss their work experiences, and filling in the experience and the discovery) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_G1 + _G2 + _G3 + _GM + _GMINE, k=3)
        + [M("What does –다(가) 보니(까) express?", "A discovery or realization while engaging in an activity", ["A past wish", "A command", "A reason for refusing"], "The book’s note."), M("What does –아/어 보니(까) express?", "A discovery or realization after engaging in an activity", ["A discovery while doing it", "A wish", "A future plan"], "The book’s note."), M("What does it literally mean?", "“because I (stop to) see what I have been doing”", ["“as soon as”", "“in order to”", "“even if”"], "The book’s note."), M("What does 몬트레이에 살다가 보니까 바닷가 도시가 좋아졌어요 mean?", "Having lived in Monterey, I discovered I like coastal cities", ["I am moving to Monterey", "I dislike Monterey", "I visited Monterey"], "The book’s example."), M("What does 한 달 동안 출장을 와 있다 보니 가족이 보고 싶어요 mean?", "Having been on a business trip for a month, I miss my family", ["I will go on a trip", "My family visited", "I like trips"], "The book’s example."),
           F("한국어를 공부하___ 한국어가 재미있어요. (-다 보니)", "다 보니", ["다 봐서", "고 보니"], "-다 보니."), F("매일 컴퓨터를 하다 ___ 눈이 아파요. (-보니까)", "보니까", ["봐서", "보고"], "-보니까."), F("한국말을 ___ 보니까 한국말이 재미있어요. (after I learned)", "배워", ["배우다", "배우고"], "-아/어 보니까."), F("피자를 먹다 보니 맛이 좀 ___. (strange)", "이상해요", ["이상했어요", "이상하고"], "이상하다."), F("몬트레이에 ___ 보니까 바닷가 도시가 좋아졌어요. (living)", "살다", ["산", "사는"], "살다 보니까."),
           read_q("한국말을 배우다 보니까 일본말도 배우고 싶어요"), read_q("몬트레이에 살다가 보니까 바닷가 도시가 좋아졌어요"), read_q("매일 컴퓨터를 하다 보니까 눈이 아파요"), read_q("한 달 동안 출장을 와 있다 보니 가족이 보고 싶어요"), read_q("한국말을 배워 보니까 한국말이 재미있어요")]
    ),
)

# ================================================================== L8: Grammar B: -줄 알았다/몰랐다
_J1 = [("김 선생님이 미혼인 줄 알았어요.", "I thought Ms. Kim was not married (but I was wrong)."), ("오늘 비가 올 줄 알았어요.", "I thought it would rain today (but I was wrong).")]
_J2 = [("김 선생님이 미혼인 줄 몰랐어요.", "I didn’t know that Ms. Kim is not married."), ("오늘 비가 올 줄 몰랐어요.", "I wasn’t aware that it would rain today.")]
_J3 = [("아침에 비가 온 줄 알았어요.", "I thought that it rained this morning."), ("아침에 비가 올 줄 알았어요.", "I thought that it would rain this morning."), ("지금 비가 오는 줄 알았어요.", "I thought that it was raining right now.")]
_J4 = [("지금 비가 오는 줄 알았어요.", "I thought it was raining now (but I was wrong)."), ("박 선생님이 영어를 못 하는 줄 알았어요.", "I thought Mr. Park didn’t speak English (but I was wrong)."), ("김 선생님이 결혼한 줄 몰랐어요.", "I didn’t know that Ms. Kim is married."), ("내일까지 숙제를 내야 하는 줄 몰랐어요.", "I didn’t know that [we] have to submit our homework by tomorrow.")]
_JT = [("어제", "yesterday"), ("오늘", "today"), ("내일", "tomorrow"), ("지금", "now"), ("일주일 후", "a week later"), ("내년", "next year"), ("작년", "last year"), ("올해", "this year"), ("곧", "soon")]
_JV = [("약혼하다", "to get engaged"), ("떠나다", "to leave"), ("슬프다", "to be sad"), ("결혼하다", "to get married"), ("달리다", "to run"), ("기쁘다", "to be glad"), ("울다", "to cry"), ("생일이다", "to be one’s birthday")]
_JM = [("어제 눈이 온 줄 몰랐어요.", "I didn’t know it snowed yesterday."), ("오늘 비가 올 줄 알았어요.", "I thought it would rain today.")]
_JMINE = [("어제 영희가 약혼한 줄 몰랐어요.", "I didn’t know Younghee got engaged yesterday."), ("곧 친구가 떠날 줄 알았어요.", "I thought my friend would leave soon."), ("지금 아기가 우는 줄 알았어요.", "I thought the baby was crying now."), ("작년에 철수가 결혼한 줄 몰랐어요.", "I didn’t know Cheolsu got married last year."), ("올해 제 생일이 일요일인 줄 알았어요.", "I thought my birthday this year was on a Sunday.")]
_JBA = [("내일 야근이 있다", "There will be overtime tomorrow"), ("다음주에 해외출장을 가다", "(Someone) will go on an overseas business trip next week"), ("이 차장의 삼촌이 이 회사 사장이다", "Deputy General Manager Lee’s uncle is the president of this company"), ("황 선생님은 매일 퇴근을 일찍 하다", "Mr. Hwang leaves work early every day"), ("아흔두 살 할머니가 생일 축하 스카이다이빙을 하다", "A 92-year-old grandmother skydived to celebrate her birthday"), ("두 사람은 친한 친구다", "The two are close friends"), ("김 병장이 교통사고가 나다", "Sergeant Kim had a traffic accident"), ("한국영화가 미국에서 인기 있다", "Korean movies are popular in America"), ("영수가 입사시험에 합격하다", "Youngsu passed the company entrance exam"), ("연봉이 삼십 퍼센트 오르다", "The annual salary rises by 30%"), ("보너스가 많아지다", "The bonus gets bigger"), ("직장인들 이십 퍼센트가 직장생활에 만족하다", "20% of office workers are satisfied with work life"), ("내년에 학교 규모가 더 커지다", "The school will get bigger next year")]
_JBB = [("이야기", "a story; talk"), ("티브이 뉴스", "TV news"), ("말", "words; a saying"), ("것", "a thing; (what is said)"), ("라디오 뉴스", "radio news"), ("인터넷", "the internet"), ("소문", "a rumor")]
_JMD = [("김 대리가 과장으로 승진했다는 얘기 들었어요?", "Did you hear the story that Assistant Manager Kim was promoted to section chief?"), ("그래요? 김 대리는 상사들한테 능력을 인정받아서 승진할 줄 알았어요.", "Is that so? I thought Assistant Manager Kim would be promoted because he was recognized for his ability by his superiors."), ("아니요. 김 대리가 이렇게 빨리 승진할 줄 몰랐어요.", "No. I didn’t know Assistant Manager Kim would be promoted this quickly.")]
L8 = lesson(
    "Ch 36 · Grammar B: an attributive form + 줄 알았다 / 줄 몰랐다",
    "-줄 알았다 · -줄 몰랐다 · 미혼인 줄 알았어요 · 비가 올 줄 몰랐어요 · 결혼한 줄 몰랐어요 · -다는 얘기",
    requires=[],
    cards=[
        card("“I thought … (but I was wrong)”",
             "In English, we often use the expression “I thought” when our assumption, understanding, or prediction turns out to be wrong, as in “I thought he was American” and “I thought the Korean national team would advance to the final.” In Korean, the expression – 줄 알았다 is used when our assumption, understanding, or prediction turns out to be wrong. For example (the English is the book’s):",
             examples=passage(_J1)),
        card("“I wasn’t aware” / “I didn’t know”", "On the other hand, – 줄 몰랐다 is used when we find out something we did not know or were not aware of. For example (the English is the book’s):", examples=passage(_J2)),
        card("Not the same as –(으)ㄹ 줄 알다/모르다",
             "Keep in mind that – 줄 알았다 and – 줄 몰랐다 are quite different in meaning from –(으)ㄹ 줄 알다 (to know how to do something) and –(으)ㄹ 줄 모르다 (to not know how to do something), which you learned about in Chapter 16. In addition, – 줄 알았다 and – 줄 몰랐다 can be preceded by any attributive form (the English is the book’s):",
             examples=passage(_J3)),
        card("Expressing “I thought … (but I was wrong)” and “I wasn’t aware” / “I didn’t know”", "an attributive form + 줄 알았다; an attributive form + 줄 몰랐다. More examples (the English is the book’s):", examples=passage(_J4)),
        card("Follow-up 3 (Listening and speaking): time words and verbs",
             "List A contains time reference words and List B contains verbs. Student A chooses one word from each list and makes a sentence using –(으)ㄴ/는/(으)ㄹ 줄 모르다; Student B repeats the process with different words, and you listen to each other’s sentences and correct any mistakes. List A: 어제, 오늘, 내일, 지금, 일주일 후, 내년, 작년, 올해, 곧. List B: 약혼하다, 떠나다, 슬프다, 결혼하다, 달리다, 기쁘다, 울다, 생일이다. The book’s model and my sample sentences (the English is mine):",
             tables=[ktable(_JT), ktable(_JV)], examples=dlg([("A", _JM[0][0], _JM[0][1]), ("B", _JM[1][0], _JM[1][1])]) + passage(_JMINE)),
        card("Follow-up 5 (Listening and speaking): reporting information with –다는 / ~(이)라는",
             "The first student chooses a sentence from Box A and a source from Box B and makes a complete sentence with –다는/~(이)라는; the second student responds using – 줄 알다/모르다. The book’s model (the English is mine; the book’s “or” between the two answers is dropped):",
             examples=dlg([("A", _JMD[0][0], _JMD[0][1]), ("B", _JMD[1][0], _JMD[1][1]), ("B", _JMD[2][0], _JMD[2][1])])),
        card("Box A: the information (30% and 20% are spelled out)", "The book’s Box A (the English is mine):", tables=[table(["Information", "English (mine)"], [list(r) for r in _JBA], say=[0])]),
        card("Box B: the sources", "The book’s Box B (소문 is glossed “rumor”; the English is mine):", tables=[ktable(_JBB)]),
        card("Activities left out", "Follow-up 4 (listening to four conversations that use –줄 알다/모르다, ticking whether each means “know/not know how to do something” or “I thought/I didn’t know”, and translating the sentence) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_J1 + _J2 + _J3 + _J4 + _JM + _JMINE + _JMD, k=3)
        + [M("What does – 줄 알았다 express?", "“I thought … (but I was wrong)”", ["“I know how to …”", "“I will …”", "“I want to …”"], "The book’s note."), M("What does – 줄 몰랐다 express?", "“I didn’t know / I wasn’t aware”", ["“I thought”", "“I can’t do”", "“I will not”"], "The book’s note."), M("What does –(으)ㄹ 줄 알다 mean (Chapter 16)?", "to know how to do something", ["I thought …", "I didn’t know …", "as soon as"], "Chapter 16."), M("Can – 줄 알았다 follow any attributive form?", "Yes", ["No, only the future", "No, only the past", "Only with nouns"], "The book’s note."), M("What does 김 선생님이 결혼한 줄 몰랐어요 mean?", "I didn’t know that Ms. Kim is married", ["I thought Ms. Kim was married", "I know Ms. Kim", "Ms. Kim isn’t married"], "줄 몰랐다."), M("What does 지금 비가 오는 줄 알았어요 mean?", "I thought it was raining right now (but I was wrong)", ["I know it will rain", "It is raining", "I didn’t know it rained"], "줄 알았다."),
           F("김 선생님이 미혼인 ___ 알았어요. (I thought)", "줄", ["수", "것"], "줄 알았다."), F("오늘 비가 올 ___ 몰랐어요. (didn’t know)", "줄", ["수", "것"], "줄 몰랐다."), F("아침에 비가 ___ 줄 알았어요. (rained; past)", "온", ["오는", "올"], "past attributive."), F("지금 비가 ___ 줄 알았어요. (is raining; present)", "오는", ["온", "올"], "present attributive."), F("내일까지 숙제를 내야 하는 줄 ___. (I didn’t know)", "몰랐어요", ["알았어요", "알아요"], "줄 몰랐다."),
           read_q("김 선생님이 미혼인 줄 알았어요"), read_q("오늘 비가 올 줄 몰랐어요"), read_q("박 선생님이 영어를 못 하는 줄 알았어요"), read_q("내일까지 숙제를 내야 하는 줄 몰랐어요"), read_q("김 대리가 이렇게 빨리 승진할 줄 몰랐어요")]
    ),
)

# ================================================================== L9: Topic C
_C_TXT = [
    ("김상현 씨는 삼십오 년 동안 우체국에서 근무했습니다.", "Mr. Kim Sanghyun worked at a post office for thirty-five years."),
    ("올해 오 월에 정년퇴직을 할 예정입니다.", "He is scheduled to retire at the normal retirement age in May this year."),
    ("요즘 김상현 씨는 부인과 함께 제이의 인생을 준비하고 있습니다.", "These days Mr. Kim is preparing a second life together with his wife."),
    ("은퇴 후에는 답답한 도시를 떠나서 시골로 갈 계획입니다.", "After retirement he plans to leave the stuffy city and go to the countryside."),
    ("거기에서 여유로운 노후생활을 즐기려고 합니다.", "There he intends to enjoy a leisurely life in his old age."),
    ("그동안 못했던 취미활동이나 사회봉사활동을 할 생각입니다.", "He plans to do hobbies or social volunteer activities that he couldn’t do in the meantime."),
    ("퇴직 후에는 연금과 퇴직금, 그리고 그동안 저축해 놓은 돈으로 생활할 수 있습니다.", "After retirement he can live on his pension, severance pay and the money he has saved in the meantime."),
    ("박종필 씨는 십오 년이나 다니던 무역회사를 지난달에 그만두었습니다.", "Mr. Park Jongpil quit the trading company he had worked at for fifteen years last month."),
    ("회사에 큰 불만은 없었지만 창업을 하기 위해 사표를 냈습니다.", "He had no big complaints about the company but handed in his resignation to start a business."),
    ("직장경험을 활용해서 학용품을 수출하는 회사를 차리려고 합니다.", "He intends to set up a company that exports school supplies, making use of his work experience."),
    ("퇴직금이 나오는 대로 사무실과 직원을 구하려고 합니다.", "As soon as his severance pay comes out, he intends to find an office and employees."),
    ("그리고 준비가 다 되면 개업을 할 계획입니다.", "And when everything is ready, he plans to open the business."),
]
_C_WORDS = ["개업", "노후", "답답하다", "불만", "수입", "여유", "연금", "은퇴", "인생", "자영업", "차리다", "창업", "퇴직금", "학용품", "활용"]
_QA = [("정년퇴직을 준비하는 사람입니다.", "I am a person preparing for retirement."), ("퇴직 후 노후생활을 잘하려면 무엇을 준비해야 합니까?", "What should I prepare to live well in my old age after retirement?"), ("좀 알려 주세요.", "Please tell me a little."), ("은퇴 후 제이의 인생을 즐겁게 사시는 분들이 많습니다.", "There are many people who enjoy a second life after retirement."), ("은퇴 생활을 즐겁게 하시는 분들은 모두 은퇴 후에도 바쁘게 지내고 계십니다.", "All of those who enjoy retirement life are keeping busy even after retirement."), ("취미활동이나 봉사활동 등을 하면서 직장에 다닐 때보다 더 즐겁게 사십니다.", "Doing hobbies or volunteer activities and so on, they live more happily than when they went to work."), ("은퇴 후에 무엇을 할지 생각해 보세요.", "Think about what you will do after retirement."), ("부부가 함께 할 수 있는 일이면 더 좋습니다.", "It is even better if it is something a couple can do together."), ("그리고 노후 연금을 준비하고 저축을 해 두는 것도 중요합니다.", "And it is also important to prepare an old-age pension and save money.")]
L9 = lesson(
    "Ch 36 · Topic C: I plan to enjoy a leisurely retirement (여유로운 노후 생활을 즐기려고 합니다)",
    "여유로운 노후 생활 · 정년퇴직 · 제2의 인생 · 연금 · 퇴직금 · 창업 · 사표 · 개업 · 은퇴 후 조언",
    requires=[],
    cards=[
        card("Topic C: I plan to enjoy a leisurely retirement (여유로운 노후 생활을 즐기려고 합니다)",
             "The two stories are about retirement plans. (The English is mine; the book gives none; the numbers are spelled out in Hangul: 35년 → 삼십오 년, 5월 → 오 월, 제2의 → 제이의, 15년 → 십오 년.)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 개업(하다), 수입(하다), 여유(롭다), 은퇴(하다), 창업(하다) and 활용(하다) take the forms in parentheses; –은/는 대로 and ~(이)나 are explained in the grammar.",
             tables=[ktable(_rows(_C_WORDS)), table(["Word", "Meaning"], [["사표 / 사직서", "resignation; a letter of resignation (to resign: ~[를] 내다)"], ["(자원)봉사", "volunteer service; to serve as a volunteer (~하다)"], ["(정년)퇴직", "retirement (at normal retirement age)"], ["제~", "optional prefix for an ordinal"], ["-은/는 대로", "as soon as"], ["~(이)나", "a noun marker (emphasizing a number)"]], say=[0])]),
        card("Follow-up 2 (Reading): a Q&A about retirement",
             "Read the Q&A exchange and, in English, identify the advice for successful retirement. The Q&A is the book’s (the “Q:” and “A:” labels are dropped; 제2의 is spelled 제이의); the English is mine.",
             examples=passage(_QA)),
        card("The advice, in English (mine)", "The book leaves two bullets blank; these are my answers.",
             tables=[table(["Advice for successful retirement (mine)", ""], [["•", "Keep busy after retirement, for example with hobbies and volunteer activities; think about what you will do, ideally something a couple can do together"], ["•", "Prepare an old-age pension and save money"]])]),
        card("Activities left out", "Follow-up 1 (listening to two narrations in which an employee talks about his work and plan, and filling in the reason for leaving work and the plan after leaving), the Topic Presentation C study steps (SMART Board) and Activities 1 to 3 (word strips for making sentences, listening to an interview with a retiree, and reading Text A/Text B about two people’s experiences after leaving a job, with group exchange and a flip-chart presentation) are audio, computer, paper and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT + _QA, k=3)
        + [M("How long did 김상현 work at the post office?", "Thirty-five years", ["Fifteen years", "Five years", "Twenty-five years"], "삼십오 년."), M("When will he retire?", "In May this year", ["Last month", "Next year", "In ten years"], "올해 오 월."), M("Where does he plan to go after retirement?", "The countryside", ["Abroad", "A big city", "The coast"], "시골."), M("What will he live on?", "Pension, severance pay and savings", ["A new job", "His children", "A loan"], "연금과 퇴직금 그리고 저축."), M("How long did 박종필 work at the trading company?", "Fifteen years", ["Thirty-five years", "Five years", "Two years"], "십오 년."), M("Why did he quit?", "To start a business", ["He was fired", "He was sick", "He was bored"], "창업을 하기 위해."), M("What kind of company will he set up?", "One that exports school supplies", ["A restaurant", "A school", "A flower shop"], "학용품을 수출하는 회사."), M("When will he look for an office and employees?", "As soon as his severance pay comes out", ["Next year", "Right now", "After the opening"], "퇴직금이 나오는 대로."),
           F("올해 오 월에 ___을 할 예정입니다. (retirement at normal age)", "정년퇴직", ["이직", "창업"], "정년퇴직."), F("거기에서 ___로운 노후생활을 즐기려고 합니다. (leisurely)", "여유", ["자유", "만족"], "여유롭다."), F("퇴직 후에는 ___과 퇴직금으로 생활할 수 있습니다. (pension)", "연금", ["보너스", "연봉"], "연금."), F("창업을 하기 위해 ___를 냈습니다. (resignation)", "사표", ["연금", "답장"], "사표."), F("직장경험을 ___해서 학용품을 수출하는 회사를 차리려고 합니다. (make use of)", "활용", ["반복", "지원"], "활용하다."),
           read_q("여유로운 노후 생활을 즐기려고 합니다"), read_q("올해 오 월에 정년퇴직을 할 예정입니다"), read_q("회사에 큰 불만은 없었지만 창업을 하기 위해 사표를 냈습니다"), read_q("퇴직금이 나오는 대로 사무실과 직원을 구하려고 합니다"), read_q("은퇴 후에 무엇을 할지 생각해 보세요")]
    ),
)

# ================================================================== L10: Grammar C: ~(이)나
_NA1 = [("저는 그 책을 세 번이나 읽었어요.", "I have read the book three times!"), ("여섯 시간이나 숙제를 했어요.", "I did homework for six (darn) hours!")]
_NA2 = [("파티에 손님을 오백 명이나 초대했어요.", "I invited 500 guests to the party!"), ("운전면허시험을 열 번이나 떨어졌어요.", "I flunked the driver’s license test 10 times!"), ("저는 이 회사에서 이십 년이나 일했어요.", "I have worked at this company for 20 years!")]
_NAM = [("몬트레이에서 엘에이까지 차로 다섯 시간 걸립니다.", "It takes five hours by car from Monterey to LA."), ("몬트레이에서 엘에이까지 차로 다섯 시간이나 걸립니다.", "It takes as many as five hours by car from Monterey to LA.")]
_NAC = [("피자나 햄버거", "pizza or hamburger"), ("한국이나 중국", "Korea or China")]
_NAMINE = [("그 가게에서 책을 열 권이나 샀어요.", "I bought as many as ten books at that store."), ("어제 밤을 새워서 커피를 다섯 잔이나 마셨어요.", "I stayed up all night yesterday and drank as many as five cups of coffee."), ("그 영화를 네 번이나 봤어요.", "I saw that movie as many as four times."), ("동생은 하루에 라면을 세 개나 먹어요.", "My younger brother eats as many as three packs of ramen a day.")]
L10 = lesson(
    "Ch 36 · Grammar C: emphasizing or exaggerating quantity using ~(이)나",
    "~(이)나 · 세 번이나 · 여섯 시간이나 · 오백 명이나 · 이십 년이나 · 피자나 햄버거",
    requires=[],
    cards=[
        card("The noun marker ~(이)나",
             "Recall the noun connector ~(이)나 that indicates alternative nouns, as in 피자나 햄버거 (pizza or hamburger) and 한국이나 중국 (Korea or China). It can also be used as a noun marker attached to a noun. When ~(이)나 is attached to a noun that contains a number, it implies that the number or amount is much larger than the speaker expects. For example (the English is the book’s):",
             tables=[ktable(_NAC)], examples=passage(_NA1)),
        card("What the examples show", "In the first sentence, the speaker is bragging that he has read the book three times by emphasizing the number of times he has read it. In the second sentence, the speaker is complaining that he did homework for six hours by exaggerating the number of hours during which he did homework."),
        card("Emphasizing or exaggerating a number/amount", "numerical expression + (이)나. More examples (the numbers are spelled out in Hangul; the English is the book’s):", examples=passage(_NA2)),
        card("Follow-up 1 (Reading, speaking and listening): the model", "In pairs, each pair gets a set of cards with numerical expressions; Student A picks a card and reads the sentence aloud, and Student B changes the sentence using ~(이)나 to emphasize the number. The book’s model (the book writes LA; the English is mine):", examples=dlg([("A", _NAM[0][0], _NAM[0][1]), ("B", _NAM[1][0], _NAM[1][1])])),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_NAMINE)),
        card("Activities left out", "The numerical-expression cards and Follow-up 2 (listening to three conversations between a man and a woman in which a number + (이)나 is mentioned, and translating that sentence) need cards, audio and a partner."),
    ],
    exercises=uniq(
        _tr(_NAC + _NA1 + _NA2 + _NAM + _NAMINE, k=3)
        + [M("What does ~(이)나 imply after a number?", "The number or amount is larger than the speaker expects", ["The number is small", "The number is exact", "The number is unknown"], "The book’s note."), M("What does 세 번이나 읽었어요 emphasize?", "Reading the book as many as three times", ["Reading once", "Reading a little", "Not reading"], "세 번이나."), M("Is the speaker in 여섯 시간이나 숙제를 했어요 bragging or complaining?", "Complaining", ["Bragging", "Asking", "Thanking"], "The book’s note."), M("What does 피자나 햄버거 mean?", "pizza or hamburger", ["pizza and hamburger", "neither", "pizza only"], "~(이)나 as a connector."), M("What does 이십 년이나 일했어요 mean?", "I have worked as long as 20 years", ["I worked 2 years", "I will work 20 years", "I didn’t work"], "~(이)나."),
           F("저는 그 책을 세 번___ 읽었어요. (as many as)", "이나", ["도", "만"], "번이나."), F("여섯 시간___ 숙제를 했어요. (as many as)", "이나", ["도", "만"], "시간이나."), F("파티에 손님을 오백 명___ 초대했어요. (as many as)", "이나", ["도", "만"], "명이나."), F("운전면허시험을 열 번___ 떨어졌어요. (as many as)", "이나", ["도", "만"], "번이나."), F("저는 이 회사에서 이십 년___ 일했어요. (as many as)", "이나", ["도", "만"], "년이나."),
           read_q("저는 그 책을 세 번이나 읽었어요"), read_q("여섯 시간이나 숙제를 했어요"), read_q("파티에 손님을 오백 명이나 초대했어요"), read_q("운전면허시험을 열 번이나 떨어졌어요"), read_q("저는 이 회사에서 이십 년이나 일했어요")]
    ),
)

# ================================================================== L11: Grammar D: -는 대로
_DR1 = [("한국에 도착하는 대로 전화하겠습니다.", "I will call you as soon as I arrive in Korea."), ("수업이 끝나는 대로 집에 와.", "Come home as soon as the class is over.")]
_DR0 = [("일어나자마자 샤워했어요.", "I took a shower as soon as I got up.")]
_DR2 = [("일을 마치는 대로 가겠습니다.", "I will go as soon as I finish the work."), ("들어오는 대로 연락주세요.", "Please contact me as soon as you come in."), ("아침에 일어나는 대로 전화할게요.", "I will call you as soon as I get up.")]
_DRM = [("집에 도착하다", "to arrive home"), ("집에 도착하는 대로", "as soon as (you) arrive home"), ("집에 도착하는 대로 저한테 전화하세요.", "Please call me as soon as you arrive home.")]
_DRC = [("아침에 일어납니다.", "I get up in the morning."), ("일어나는 대로 샤워를 합니다.", "As soon as I get up, I take a shower."), ("샤워를 하는 대로 아침을 먹습니다.", "As soon as I take a shower, I eat breakfast.")]
_DRMINE = [("퇴근하는 대로 집에 가서 쉬고 싶어요.", "I want to go home and rest as soon as I leave work."), ("월급을 받는 대로 저축을 하겠습니다.", "I will save money as soon as I get my pay."), ("연락이 오는 대로 알려 드리겠습니다.", "I will let you know as soon as I hear from them.")]
L11 = lesson(
    "Ch 36 · Grammar D: the conjunctive ending –는 대로",
    "-는 대로 · 도착하는 대로 · 끝나는 대로 · 마치는 대로 · 일어나는 대로 · -자마자",
    requires=[],
    cards=[
        card("“As soon as” with –는 대로",
             "Recall from Chapter 20 the conjunctive ending –자마자. It translates to as soon as or immediately after, as in 일어나자마자 샤워했어요 (I took a shower as soon as I got up).\n\n"
             "–는 대로 translates similarly and can be used to express that one action or event is immediately followed by another action or event. However, the conjunctive ending –는 대로 implies that the time of an action or event is not determined. For example (the English is the book’s):",
             examples=passage(_DR0 + _DR1)),
        card("Why some sentences are ungrammatical",
             "In the sentences above, the arrival time and the time the class ends are not determined. Because of this implication, the following sentences are considered ungrammatical (the book marks them with an asterisk): *7시에 일어나는 대로 샤워합니다 (I take a shower at seven as soon as I get up; a specific time) and *어제 집에 오는 대로 잤어요 (I went to sleep immediately after I came home; a past action that occurred only once)."),
        card("Expressing “as soon as” or “immediately after”", "action verb stem + 는 대로. More examples (the English is the book’s):", examples=passage(_DR2)),
        card("Follow-up 3 (Listening, reading and speaking): the model", "In pairs, each pair gets a set of verb phrase cards; Student A picks a card and conjugates the verb phrase with –는 대로 and Student B makes a complete sentence with the conjugated phrase. The book’s model (the English is mine):", examples=dlg([("A", _DRM[0][0] + ".", _DRM[0][1]), ("A", _DRM[1][0], _DRM[1][1]), ("B", _DRM[2][0], _DRM[2][1])])),
        card("Follow-up 5 (Speaking): a chain of daily routine", "As a class, sit in a circle and think of Korean action verbs likely to be used when talking about daily routine, and then, one after another, make sentences with –는 대로 using the previous student’s action verb and another action. The book’s model (the English is mine):", examples=dlg([("A", _DRC[0][0], _DRC[0][1]), ("B", _DRC[1][0], _DRC[1][1]), ("C", _DRC[2][0], _DRC[2][1])])),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_DRMINE)),
        card("Activities left out", "The verb phrase cards, Follow-up 4 (listening to three dialogs and writing the two sequential actions or events) and Activities 1 to 3 of the chapter’s final section need cards and audio."),
    ],
    exercises=uniq(
        _tr(_DR0 + _DR1 + _DR2 + _DRC + _DRMINE, k=3)
        + [M("What does –는 대로 mean?", "as soon as; immediately after", ["because", "although", "in order to"], "The book’s note."), M("What does –는 대로 imply about the time of the action?", "It is not determined", ["It is a fixed time", "It is the past", "It is exact"], "The book’s note."), M("Which is ungrammatical with –는 대로?", "A specific time or a one-time past action", ["A future action", "A request", "A promise"], "The book’s note."), M("What does 한국에 도착하는 대로 전화하겠습니다 mean?", "I will call you as soon as I arrive in Korea", ["I called from Korea", "I am in Korea", "I will never call"], "–는 대로."), M("What does 수업이 끝나는 대로 집에 와 mean?", "Come home as soon as class is over", ["Don’t come home", "Class is long", "I went home"], "–는 대로."),
           F("한국에 도착하___ 전화하겠습니다. (as soon as)", "는 대로", ["자마자는", "는데"], "–는 대로."), F("수업이 끝나___ 집에 와. (as soon as)", "는 대로", ["자마자는", "는데"], "–는 대로."), F("일을 마치___ 가겠습니다. (as soon as)", "는 대로", ["고는", "는데"], "–는 대로."), F("퇴직금이 나오___ 사무실과 직원을 구하려고 합니다. (as soon as)", "는 대로", ["는데", "고는"], "–는 대로."), F("회사에 도착하는 ___ 과장님 사무실로 가세요. (as soon as)", "대로", ["때문", "만큼"], "–는 대로."),
           read_q("한국에 도착하는 대로 전화하겠습니다"), read_q("수업이 끝나는 대로 집에 와"), read_q("일을 마치는 대로 가겠습니다"), read_q("들어오는 대로 연락주세요"), read_q("아침에 일어나는 대로 전화할게요")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Loan words", _CV_LOAN), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/")]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L12 = lesson(
    "Ch 36 · Core vocabulary and self-evaluation",
    "주요 단어 · 직장생활 · 일과 · 업무 · 연봉 · 은퇴 · 창업 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary sections are blank.\n\n"
             "The example sentences with digits are respelled in Hangul (6시 → 여섯 시; 2년 → 이 년; 100% → 백 퍼센트; 제3중대 → 제삼 중대; 2시간 → 두 시간)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify, ask about, and discuss daily routines and common concerns at work; talk about plans for starting a new business; and identify, ask about, and discuss the typical lifestyle of retirees.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; –다(가) 보니(까), used to express the speaker’s own discovery/realization of something while engaging in an activity; an attributive form + 줄 알았다 (I thought); an attributive form + 줄 몰랐다 (I did not know; I was not aware); ~(이)나 used to emphasize an amount or number; the conjunctive ending –는 대로 (as soon as; immediately after); and the Sino-Korean syllables within 능력 (能力), 유무 (有無), and 개업 (開業)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 정년퇴직 mean?", "retirement at normal retirement age", ["a pension", "a resignation", "a bonus"], "停年退職."), M("What does 연금 mean?", "a pension; “annual money”", ["a bonus", "an annual salary", "a retirement allowance"], "年金."), M("What does 퇴직금 mean?", "a retirement allowance; a retirement benefit", ["a pension", "a bonus", "wages"], "退職金."), M("What does 연봉 mean?", "an annual salary", ["a bonus", "a pension", "a wage"], "年俸."), M("What does 창업 mean?", "foundation of a business", ["closing a business", "quitting a job", "an import"], "創業."), M("What does 수출 mean?", "export", ["import", "a bonus", "a trip"], "輸出."), M("What does 수입 mean?", "import", ["export", "a bonus", "a trip"], "輸入."), M("What does 출장 mean?", "a business trip", ["a transfer", "a promotion", "a resignation"], "出張."),
           F("올해는 ___이 오르지 않았습니다. (annual salary)", "연봉", ["연금", "보너스"], "연봉."), F("내일 유럽으로 ___을 가야 합니다. (business trip)", "출장", ["야근", "이직"], "출장."), F("직장 상사와 의견이 맞지 않아서 ___를 냈어요. (resignation)", "사표", ["답장", "보고서"], "사표."), F("우리 회사는 ___가 가능합니다. (telework)", "재택근무", ["야근", "출장"], "재택근무."), F("아버지께서는 공무원 ___을 받아서 생활합니다. (pension)", "연금", ["연봉", "보너스"], "연금."),
           read_q("주요 단어"), read_q("직장생활"), read_q("은퇴"), read_q("창업"), read_q("재택근무")]
    ),
)

UNIT = unit("Semester 2 · Unit 9 · Chapter 36: Life at Work (직장생활)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])

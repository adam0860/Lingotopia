"""Unit 45: KBC Semester 2, Unit 10, Chapter 38 - Crime (범죄).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 10, Student's Edition (2022).
Audio, video, pictures, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's.
The names of real people in the articles are left out."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 38 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("강도", "(强盜) a robber", "은행에 강도가 들었어요."),
    ("금품", "(金品) money and valuables", "어젯밤에 저희 집에 강도가 들어서 금품을 빼앗아 갔어요."),
    ("달아나다", "to run away; flee", "강도가 우리 가게에서 금품을 훔치고 달아났어요."),
    ("도둑", "a thief; a burglar", "경찰이 제 돈을 훔쳐 간 도둑을 잡아 주었어요."),
    ("도주하다", "to run away; flee", "도둑이 가게에서 물건을 훔친 후 도주했습니다."),
    ("~범", "(犯) a criminal; a person who committed [a crime]", "경찰이 어린이 납치범을 잡았습니다."),
    ("범인", "(犯人) a criminal; a culprit", "어젯밤에 발생한 강도 사건의 범인을 찾고 있습니다."),
    ("범죄", "(犯罪) a crime; “criminal sin”", "연말이어서 범죄가 많이 발생하고 있습니다."),
    ("범행", "(犯行) a criminal act; a crime; an offense", "살인범이 범행 후 화장실에 숨어있다가 도주했습니다."),
    ("복면", "(覆面) a (ski) mask", "복면을 한 강도가 칼을 들고 슈퍼마켓에 들어왔습니다."),
    ("붙잡다 / 붙잡히다", "to catch / to be caught; to arrest / to be arrested", "도둑이 범행 후 두 시간 만에 경찰한테 붙잡혔어요."),
    ("빼앗다 / 빼앗기다", "to rob; to strip / to be robbed", "불량서클 아이들이 저한테서 돈을 빼앗았어요."),
    ("살인", "(殺人) a murder; homicide; “killing a person”; to kill a person; to murder (~하다)", "어제 서울호텔에서 살인 사건이 일어났습니다."),
    ("살해", "(殺害) a murder; homicide; “killing and damaging”; to murder / to be murdered (~하다/되다; 당하다)", "오십 대 남자가 흉기로 자기 부인을 살해했습니다."),
    ("성폭행", "(性暴行) a sexual assault; to commit a sexual assault / to be sexually assaulted (~하다/당하다)", "최근 대학교에서 성폭행 사건이 자주 발생하고 있습니다."),
    ("요구", "(要求) demand; to demand (~하다)", "강도가 금품을 요구했습니다."),
    ("용의자", "(容疑者) a suspect", "용의자의 인상착의가 어떻게 됩니까?"),
    ("~(이)나", "just; settling for less-appealing option; nonnumerical noun + (이)나", "주말에 바쁘지 않으면 영화나 볼까요? 주스가 없으면 물이나 한 잔 주세요."),
    ("위협", "(威脅) threat; menace; intimidation; to threaten (i.e. to instill fear in the victim) (~하다)", "강도가 노인을 위협해서 돈을 빼앗았어요."),
    ("자세하다 / 자세히", "(仔細) to be detailed; to be in detail; in detail; minutely", "그 사건에 대해 자세히 설명해 주세요."),
    ("저지르다", "to commit (a crime, an error, etc.)", "요즘 청소년들이 범죄를 많이 저지르고 있어요."),
    ("전과", "(前科) previous conviction", "그 범인이 전과 삼 범인 것으로 드러났습니다."),
    ("절도", "(竊盜) theft; stealing; burglary", "어젯밤 우리 동네 편의점에서 절도사건이 발생했어요."),
    ("종업원", "(從業員) an employee; a worker", "이 식당에는 종업원이 오십 명이나 됩니다."),
    ("찌르다", "to stab; to poke", "범인이 흉기로 편의점 직원을 찔렀어요."),
    ("체포", "(逮捕) arrest; apprehension; capture; to arrest / to be arrested (~하다/되다)", "경찰이 강도를 체포했습니다."),
    ("털다", "to steal; to rob", "강도가 은행을 털었습니다."),
    ("폭력", "(暴力) violence; “violent force”", "요즘 학교폭력 단속기간입니다."),
    ("피해자", "(被害者) a victim", "경찰이 교통사고 피해자의 가족을 찾고 있습니다."),
    ("혐의", "(嫌疑) a suspicion; charge", "삼십 대 남자가 살인 혐의로 경찰에 구속되었습니다."),
    ("훔치다", "to steal; to rob", "도둑이 돈을 훔쳐 달아났어요."),
    ("흉기", "(凶器) a deadly weapon; a lethal weapon", "강도가 흉기로 편의점 주인을 찔렀어요."),
]
_CV_B = [
    ("가출", "(家出) running away from home; “leaving home”; to run away from home (~하다)", "그 애는 엄마한테 야단맞고 가출했어요."),
    ("가해자", "(加害者) perpetrator; offender", "학교 폭력 가해자들을 경찰에 신고하세요."),
    ("거짓말", "a lie; “false language”; to lie (하다)", "거짓말은 할수록 늘어요."),
    ("결국", "(結局) finally; eventually; in the end", "열심히 공부해서 결국 좋은 대학에 입학했어요."),
    ("고통받다", "to suffer; to be struggling", "주변에 고통받는 사람들을 돌아봅시다."),
    ("괴롭히다", "to harass; to torment; to bother", "반 친구가 나를 괴롭혀요."),
    ("놀리다", "to tease; to make fun of", "친구를 놀리지 마세요."),
    ("당하다", "(當) to suffer; to experience; to encounter (something negative)", "폭행을 당한 학생이 경찰에 신고했다."),
    ("들키다", "to be found out; to be caught (red-handed); to be discovered", "어렸을 때 담배를 피우다가 들켰어요."),
    ("때리다", "to strike; to hit; to beat", "아이를 때리지 마세요."),
    ("마약", "(麻藥) drug; narcotics", "마약을 하다가 경찰에게 잡혔습니다."),
    ("벗어나다", "to get out of; to break away (from); to free oneself (from)", "답답한 도시에서 벗어나고 싶어요."),
    ("불량", "(不良) delinquency; faulty; to be delinquent (~하다)", "불량서클 아이들이 저를 때렸어요. 불량 식품을 먹고 배탈이 났어요."),
    ("비행 청소년", "(非行 靑少年) a juvenile delinquent", "비행 청소년에 의한 범죄가 늘고 있다."),
    ("상담사", "(相談師) counselor; therapist", "혼자 고민하지 말고 청소년 상담사의 도움을 받으세요."),
    ("상습적(으로)", "(常習的) habitual(ly)", "그 사람은 상습적으로 지각을 합니다."),
    ("손을 대다 / 손대다", "to meddle with; to become involved with; “to lay one’s hands (on something)”", "요즘에는 중학생들도 마약에 손을 댑니다."),
    ("어울리다", "to hang out with; to associate with", "불량서클 학생들과 어울리지 마세요."),
    ("완전히", "(完全) completely; entirely; utterly", "내일까지 모든 숙제를 완전히 마치세요."),
    ("왕따", "group bullying (of a single person); an outcast; “super ostracizing”; to group bully / to be group bullied (~시키다/당하다)", "오랫동안 왕따를 당한 여학생이 결국 가출을 했다."),
    ("욕", "(辱) a swear word; foul language; abusive language; to swear; to curse (~하다)", "화가 나서 친구에게 욕을 했어요."),
    ("용돈", "(用) an allowance", "이제 고등학생이 되어서 용돈을 더 많이 받습니다."),
    ("재활", "(再活) rehabilitation", "교통사고를 당해서 재활치료를 받아야 해요."),
    ("전학", "(轉學) school transfer; to transfer schools (~하다)", "이사를 가면 전학을 해야 합니다."),
    ("중독", "(中毒) an addiction; “(in) the middle of poison”; to be addicted (~되다)", "마약에 한 번 중독되면 벗어나기가 어려워요."),
    ("퇴학", "(退學) expulsion (from school); to expel a student from school / to be expelled from school (~시키다/당하다)", "불량서클 아이들이 퇴학을 당했어요."),
    ("피우다", "to smoke; to build / make / start a fire; to get a fire going", "담배를 많이 피우면 폐암에 걸릴 수 있어요. 추우니까 불 좀 피웁시다."),
    ("해결", "(解決) a solution; a settlement; to solve / to be solved (~하다/되다)", "이 사건을 해결할 방법이 없어요."),
    ("협박", "(脅迫) a threat; blackmail; intimidation; to threaten; to intimidate (i.e. to induce action/inaction of the victim) (~하다)", "협박 편지를 받고 너무 무서워서 잠을 못 잤어요."),
    ("호기심", "(好奇心) curiosity", "호기심이 많은 아이에게는 다양한 체험활동을 제공하세요."),
    ("흡연", "(吸煙) cigarette smoking; to smoke a cigarette (~하다)", "흡연은 건강에 좋지 않습니다."),
]
_CV_C = [
    ("가짜", "a fake; a counterfeit; an imitation", "가짜 상품을 만들어 판 사람이 구속되었다."),
    ("강력", "(强力) strength; power; might; to be strong; to be powerful; to be mighty (~하다)", "어제 중국에서 강력한 지진이 발생했다."),
    ("건", "(件) case; case counter", "위조지폐 발생 건수가 많이 줄었어요."),
    ("납치", "(拉致) abduction; kidnapping (i.e. by force); to kidnap / to be kidnapped (~하다/되다; 당하다)", "일곱 살짜리 남자아이가 학교 앞에서 납치당했어요."),
    ("모으다", "to collect; to gather", "제 취미는 우표를 모으는 것입니다."),
    ("밀수", "(密輸) smuggling; “secretly transporting”; to smuggle / to be smuggled (~하다/되다)", "가방이나 화장품 등의 짝퉁 밀수가 점점 증가하고 있습니다."),
    ("발달", "(發達) development; to develop (~하다/되다)", "과학의 발달과 함께 자주 일어나는 범죄에도 변화가 일어나고 있습니다."),
    ("방화", "(放火) arson; setting a fire; to set a fire (~하다)", "그 산불은 방화에 의해 일어났다고 경찰이 밝혔습니다."),
    ("법", "(法) the law; piece of legislation", "요즘 교통법을 위반하는 사람이 늘고 있습니다."),
    ("불법", "(不法) unlawfulness; illegality", "이곳에 주차하는 것은 불법입니다. 차를 다른 곳으로 옮기세요."),
    ("사건", "(事件) a (criminal) incident; an affair; a case", "워터게이트 사건이 언제 발생했습니까?"),
    ("사기", "(詐欺) a fraud; a swindle; to swindle; to con / to be swindled; to be conned (~치다/당하다)", "친구가 저한테 사기를 치고 외국으로 도망갔어요. 인터넷 사이트에서 사기를 당하지 않도록 조심하세요."),
    ("사용", "(使用) use; to use / to be used (~하다/되다)", "전화를 좀 사용해도 될까요?"),
    ("상당하다 / 상당히", "(相當) to be considerable; considerably; remarkably", "그 사람은 외국어를 상당히 잘해요."),
    ("설치", "(設置) installation; to install / to be installed (~하다/되다)", "새집으로 이사 가면 인터넷 설치를 다시 해야 합니다."),
    ("소매치기", "a pickpocket; pickpocketing; “pocket hitting”; to pickpocket (~하다)", "사람이 많은 곳에서 관광을 할 때에는 소매치기를 조심하세요."),
    ("수사", "(搜査) (police) investigation; to investigate (~하다)", "경찰이 사십 대 남자 살인 사건을 수사 중입니다."),
    ("악용", "(惡用) misuse; “evil use”; to misuse / to be misused (~하다/되다)", "다른 사람들의 개인 정보를 악용해서 돈을 버는 사람들이 있습니다."),
    ("~에 비해(서)", "compared with / to", "형에 비해서 동생이 운동을 잘한다. 나이에 비해서 젊어 보입니다."),
    ("유출", "(流出) spill; leak; “flow out”; to leak / to be leaked (~하다/되다)", "반도체 주요 기술을 중국에 유출한 사람이 검찰에 붙잡혔습니다."),
    ("위조", "(僞造) fabrication; forgery; to fabricate; to counterfeit; to fake", "백 씨는 여권을 위조한 혐의로 수사를 받고 있다."),
    ("일반화", "(一般化) generalization; to generalize (~하다/되다)", "신용카드와 디지털 결제가 일반화 되어 현금 사용이 상당히 줄었습니다."),
    ("증거", "(證據) evidence", "경찰이 이번 살인 사건의 증거를 찾았습니다."),
    ("지폐", "(紙幣) paper money; a bank note", "어제 시장에서 오만 원짜리 지폐 스무 장을 잃어버렸다."),
    ("~짜리", "(a thing) worth ~", "동생 생일 선물로 십만 원짜리 청바지를 샀다."),
    ("형사", "(刑事) a (police) detective; a (police) investigator; a criminal case; “criminal affair”", "최근에 강력 범죄가 많이 발생해서 형사들이 아주 바쁩니다."),
    ("확실하다", "(確實) to be certain; to be sure", "다음부터는 확실한 정보만 알려주세요."),
]
_CV_GR = [
    ("~대로 / -(으)ㄴ/는 대로", "in accordance with", "책대로 하면 누구든지 쉽게 컴퓨터 소프트웨어를 배울 수 있다. 의사 선생님이 말한 대로 운동을 시작했다."),
    ("-고 말다", "to end up –", "이번 달에는 돈을 안 쓰려고 했는데 큰 텔레비전을 사고 말았다."),
    ("-아/어 있다", "to be in the state of –", "환자가 침대에 누워 있습니다. 그 사람은 항상 술에 취해 있어요. 그 가게에는 씨씨티브이가 설치되어 있습니다."),
    ("-(으)ㄴ/는 한", "as long as", "밥을 그렇게 많이 먹는 한 체중을 줄일 수 없어요."),
]
_CV_SINO = [("강력", "(强力) great strength; power; might", "강자, 강점, 강대국, 체력, 국력, 학력"), ("불법", "(不法) illegality; unlawfulness", "불균형, 불규칙, 불확실, 합법, 법원, 법학"), ("폭력", "(暴力) violence", "폭설, 폭음, 폭식, 역도, 화력, 수력")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"붙잡다 / 붙잡히다": "to catch / to be caught; to arrest", "빼앗다 / 빼앗기다": "to rob; to strip", "자세하다 / 자세히": "to be detailed; in detail", "손을 대다 / 손대다": "to meddle with; to become involved with", "상당하다 / 상당히": "to be considerable; considerably", "~에 비해(서)": "compared with", "~범": "a criminal", "~(이)나": "just; settling for less", "~짜리": "(a thing) worth ~"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_PW = [("폭우", "a rainstorm"), ("폭등", "a sudden jump; a sharp rise"), ("인력", "manpower"), ("수력", "water power"), ("역도", "weightlifting; “power way”")]
_PG = [("폭설", "a heavy snowfall"), ("폭음", "a loud explosion sound; heavy drinking"), ("폭식", "binge eating"), ("체력", "physical strength"), ("화력", "firepower"), ("역도", "weightlifting")]
_KW = [("강자", "a strong man; the strong"), ("강대국", "a big powerful country; a powerful country"), ("강약", "strength and weakness; a stress (in music)"), ("강적", "a formidable enemy; a formidable rival; “strong enemy”"), ("강진", "a severe earthquake"), ("강화", "strengthening")]
_BW = [("불규칙", "irregularity; “no regularity”"), ("불완전", "imperfection"), ("불이익", "a disadvantage; a handicap"), ("불운", "misfortune; adversity; “no luck”")]
_BW2 = [("부동", "immobility; “no moving”"), ("부자연", "unnaturalness"), ("부자유", "lack of freedom")]
_LW = [("법원", "a court of justice; a courtroom"), ("법관", "a judicial officer; a judge; the judiciary"), ("민법", "civil law; “people law”"), ("형법", "criminal law"), ("사법부", "the judicial branch")]

# ================================================================== L1
L1 = lesson(
    "Ch 38 · What the chapter teaches, 폭력 (暴力) · 강력 (强力) · 불법 (不法)",
    "범죄 · 폭력 · 폭설 · 체력 · 강력 · 강자 · 불법 · 불규칙 · 법원",
    requires=[],
    cards=[
        card("What Chapter 38 teaches (범죄)",
             "Chapter 38, “Crime”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and discuss serious crimes such as murder, robbery, theft, sexual assault, violence, etc.; identify and describe physical appearance; identify instances of juvenile delinquency such as bullying and drug addiction; and identify shifting trends of crimes and discuss recent crimes such as ID theft and voice phishing scams.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; –는/(으)ㄴ 대로 and ~대로 (in accordance with; as); the auxiliary verb –고 말다; the auxiliary verb –아/어 있다; expressing “as long as” using –(으)ㄴ/는 한; and the Sino-Korean syllables within 폭력 (暴力), 강력 (强力), and 불법 (不法)."),
        card("Sino-Korean in use: 폭력 (暴力)",
             "This Sino-Korean word means violence or assault. Both syllables of the word should be familiar to you because the first syllable 폭 (暴) meaning fierce or violent, as in 폭우 (a rainstorm) and 폭등 (a sudden jump; a sharp rise), and the second syllable 력 (力), meaning power or strength, as in 인력 (manpower), 수력 (water power), and 역도 (weightlifting; “power way”), were introduced earlier. Thus the literal meaning of the word 폭력 is “fierce power” or “violent power”, and the word refers to an exertion of (physical) force so as to injure or abuse.\n\n"
             "The book asks you to guess the meaning of 폭설, 폭음, 폭식, 체력, 화력 and 역도 (my answers are in the table).",
             tables=[ktable(_PW), ktable(_PG)]),
        card("Sino-Korean in use: 강력 (强力)",
             "This Sino-Korean word means great (physical) strength, power, or might. The first syllable 강 (强) means strong or powerful, as in 강자 (a strong man; the strong), 강대국 (a big powerful country; a powerful country), 강약 (strength and weakness; a stress [in music]), 강적 (a formidable enemy; a formidable rival; “strong enemy”), 강진 (a severe earthquake), and 강화 (strengthening). The second syllable 력 (力) means power or strength. Thus the literal meaning of the word 강력 is “strong power” or “powerful strength”.",
             tables=[ktable(_KW)]),
        card("Sino-Korean in use: 불법 (不法)",
             "This Sino-Korean word means illegality or unlawfulness. The first syllable 불 (不), which is used as a prefix, means not or no, and its English equivalents are non-, im-, il-, in-, ir-, and un-, as in 불규칙 (irregularity; “no regularity”), 불완전 (imperfection), 불이익 (a disadvantage; a handicap), and 불운 (misfortune; adversity; “no luck”). Keep in mind that 불 becomes 부 when it comes before a syllable that begins with ㄷ or ㅈ, as in 부동 (immobility; “no moving”), 부자연 (unnaturalness) and 부자유 (lack of freedom). The second syllable 법 (法) means law or method, as 법원 (a court of justice; a courtroom), 법관 (a judicial officer; a judge; the judiciary), 민법 (civil law; “people law”), 형법 (criminal law), and 사법부 (the judicial branch). Thus the literal meaning of the word 불법 is “no law” or “not lawful”, and the word refers to unlawfulness, illegality, illegitimacy, lawlessness, or injustice.",
             tables=[ktable(_BW), ktable(_BW2), ktable(_LW)]),
    ],
    exercises=uniq(
        _tr(_PW + _PG + _KW + _BW + _BW2 + _LW, k=3)
        + [M("What does 폭 (暴) mean?", "fierce; violent", ["strong", "law", "not"], "폭우."), M("What does 력 (力) mean?", "power; strength", ["law", "not", "violent"], "인력."), M("What does 강 (强) mean?", "strong; powerful", ["fierce", "law", "not"], "강자."), M("What does 불 (不) mean?", "not; no", ["law", "strong", "violent"], "불규칙."), M("What does 법 (法) mean?", "law; method", ["power", "not", "strong"], "법원."), M("What is the literal meaning of 폭력?", "“fierce power” or “violent power”", ["“no law”", "“strong power”", "“secret transport”"], "폭 + 력."), M("What is the literal meaning of 강력?", "“strong power” or “powerful strength”", ["“violent power”", "“no law”", "“people law”"], "강 + 력."), M("What is the literal meaning of 불법?", "“no law” or “not lawful”", ["“violent power”", "“strong power”", "“people law”"], "불 + 법."), M("When does 불 become 부?", "Before a syllable starting with ㄷ or ㅈ", ["Before ㅁ", "At the end of a word", "Before a vowel"], "부동, 부자연."),
           F("친구는 ___이 강해서 달리기를 잘한다. (physical strength)", "체력", ["화력", "폭식"], "체력."), F("이곳에 주차하는 것은 ___입니다. (illegal)", "불법", ["합법", "강력"], "불법."), F("어제 중국에서 ___한 지진이 발생했다. (powerful)", "강력", ["불법", "폭력"], "강력."), F("겨울에 ___이 내려서 길이 막혔다. (heavy snowfall)", "폭설", ["폭음", "폭식"], "폭설."), F("그 사람은 ___ 서류를 만들었다가 법원에 갔다. (court)", "법원", ["법관", "형법"], "법원."),
           read_q("폭력"), read_q("강력"), read_q("불법"), read_q("폭설"), read_q("법원")]
    ),
)

# ================================================================== L2 Vocabulary builder
_EXPR = [("범죄를 저지르다", "to commit a crime"), ("지폐를 위조하다", "to counterfeit banknotes"), ("흉기로 찌르다", "to stab with a lethal weapon"), ("용의자가 도주하다", "a suspect runs away"), ("완전히 벗어나다", "to break away completely"), ("담배에 중독되다", "to become addicted to cigarettes"), ("범인이 붙잡히다", "a criminal is caught"), ("범행을 들키다", "to be found out for a crime"), ("사건을 해결하다", "to solve a case"), ("금품을 빼앗다", "to rob money and valuables"), ("종업원을 위협하다", "to threaten an employee"), ("살인 혐의로 체포되다", "to be arrested on suspicion of murder"), ("용돈을 훔치다", "to steal an allowance"), ("증거를 모으다", "to collect evidence"), ("상습적으로 때리다", "to beat habitually"), ("비행 청소년들과 어울리다", "to hang out with juvenile delinquents"), ("마약을 밀수하다", "to smuggle drugs"), ("사기를 당하다", "to be swindled")]
_QA = [("안녕하세요?", "Hello?"), ("저는 중학교 삼 학년 때부터 불량 서클 친구들과 어울려서 나쁜 일을 많이 했어요.", "From the third year of middle school, I hung out with friends in a delinquent club and did many bad things."), ("반 친구들 중 저보다 약한 학생의 돈도 빼앗고 왕따도 시켰어요.", "I also took money from students in my class weaker than me and bullied them."), ("부모님께 거짓말로 학원비 낸다고 하고 돈 받아 게임비로 썼어요.", "I told my parents with a lie that I was paying academy fees, took money and spent it on games."), ("담배를 피우고 술도 마시고 집에서 가출도 여러 번 했어요.", "I smoked, drank, and ran away from home many times."), ("그렇지만 고등학생이 되고 그런 생활에서 벗어나고 싶었어요.", "But after becoming a high school student I wanted to break away from that life."), ("불량 학생에서 좋은 학생, 좋은 친구가 되고 싶고, 부모님께 좋은 딸이 되고 싶었어요.", "I wanted to go from a delinquent student to a good student and a good friend, and to be a good daughter to my parents."), ("그래서 서클에서 나왔어요.", "So I left the club."), ("그런데 서클 친구들이 저를 찾아와 매일 때리고 괴롭혔어요.", "But the club friends came looking for me and beat and tormented me every day."), ("그리고 이 사실을 부모님이나 학교에 알리면 죽이겠다고 협박을 해요.", "And they threaten that if I tell my parents or school about this, they will kill me."), ("어떻게 해야할 지 모르겠어요.", "I don’t know what to do."), ("도와주세요.", "Please help me.")]
_WA = [("도둑", "달아나다", "도둑이 차를 타고 달아났어요.", "The thief ran away in a car.")]
L2 = lesson(
    "Ch 38 · Vocabulary Builder: crime expressions and a teen’s question",
    "범죄를 저지르다 · 흉기로 찌르다 · 범인이 붙잡히다 · 증거를 모으다 · 사기를 당하다 · 청소년 고민 상담",
    requires=[],
    cards=[
        card("Activity 1: new expressions",
             "The book gives these eighteen new expressions, asks you to write the English definitions, and to look up those you are not sure of. The English is mine:",
             tables=[ktable(_EXPR)]),
        card("Activity 3: a middle school student’s concern",
             "The following text is about a middle school student’s concerns posted on an online Q&A section. The book asks you to complete the text by filling in the blanks with the appropriate words from the list 가출, 중독, 불량, 벗어나다, 협박, 거짓말, 괴롭히다, 빼앗다 (one word is not used). The text below is completed with my answers (불량, 빼앗다, 거짓말, 가출, 벗어나다, 괴롭히다, 협박; 중독 is not used); the ellipsis and the site’s labels are left out; the English is mine.",
             examples=passage(_QA)),
        card("Activity 5: Word Association Game (the model)",
             "In pairs, Student A receives noun cards and Student B verb cards; you match each noun with a compatible verb and take turns creating sentences with each pair. The book’s model: words you paired 도둑 / 달아나다; the sentence you could create:",
             examples=passage([(_WA[0][2], _WA[0][3])])),
        card("Activities left out", "Activity 2 and Activity 4 (SMART Board), the PowerPoint Sino-Korean presentation and the card game (Activity 5) need the SMART Board, cards and a partner."),
    ],
    exercises=uniq(
        _tr(_EXPR, k=3) + _tr(_QA, k=3)
        + [M("Which word fills the blank in “저보다 약한 학생의 돈도 [ ]고”?", "빼앗", ["협박", "중독", "가출"], "빼앗다."), M("Which word fills the blank in “부모님께 [ ]로 학원비 낸다고 하고”?", "거짓말", ["가출", "불량", "협박"], "거짓말."), M("Which word is not used in the text?", "중독", ["가출", "협박", "괴롭히다"], "My answer."), M("What did the club friends do after she left?", "They came looking for her, beat and tormented her", ["They apologized", "They moved away", "They told her parents"], "찾아와 때리고 괴롭혔어요."), M("What do they threaten?", "To kill her if she tells her parents or school", ["To expel her", "To call the police", "To take her phone"], "죽이겠다고 협박."),
           F("범죄를 ___ (to commit)", "저지르다", ["빼앗다", "털다"], "범죄를 저지르다."), F("증거를 ___ (to collect)", "모으다", ["털다", "찌르다"], "증거를 모으다."), F("사건을 ___ (to solve)", "해결하다", ["위조하다", "밀수하다"], "사건을 해결하다."), F("흉기로 ___ (to stab)", "찌르다", ["모으다", "털다"], "흉기로 찌르다."), F("사기를 ___ (to be swindled)", "당하다", ["저지르다", "위협하다"], "사기를 당하다."),
           read_q("범죄를 저지르다"), read_q("흉기로 찌르다"), read_q("범인이 붙잡히다"), read_q("증거를 모으다"), read_q("사기를 당하다")]
    ),
)

# ================================================================== L3 Topic A
_A_NEWS = [
    ("지난 팔 일 밤 인천시 계양구에 있는 편의점에서 서른두 살 권 모 씨가 종업원을 흉기로 살해하고 도주했습니다.", "On the night of the 8th, in a convenience store in Gyeyang-gu, Incheon, a 32-year-old Mr. Kwon killed an employee with a lethal weapon and fled."),
    ("권 씨는 이날 밤 열한 시쯤 편의점에 들어가 종업원을 칼로 찌른 후 현금 사십여만 원을 빼앗아 도주한 혐의를 받고 있습니다.", "Mr. Kwon is suspected of entering the convenience store at about eleven o’clock that night, stabbing the employee with a knife, and fleeing with about 400,000 won in cash."),
    ("범행 후 그는 편의점 근처 집에서 옷을 갈아입고 택시를 타고 달아났습니다.", "After the crime he changed clothes at a house near the convenience store and ran away by taxi."),
    ("그 후 권 씨는 경기도 부천시 한 모텔에서 숨어 있다가 모텔 주인의 신고를 받은 경찰에게 붙잡혔습니다.", "After that Mr. Kwon was hiding at a motel in Bucheon, Gyeonggi-do, and was caught by police who received a report from the motel owner."),
    ("권 씨가 범행을 저지른 지 이틀 만입니다.", "It was two days after Mr. Kwon committed the crime."),
    ("경찰은 권 씨를 강도살인 혐의로 체포했습니다.", "The police arrested Mr. Kwon on suspicion of robbery and murder."),
    ("경찰 조사 결과 권 씨는 스무 살 때부터 절도, 폭력, 성폭행 등 범죄를 저지른 전과 칠 범인 것으로 나타났습니다.", "As a result of the police investigation, it turned out that Mr. Kwon had seven previous convictions for crimes such as theft, violence and sexual assault since he was twenty."),
]
_A_WIT = [
    ("어제 밤 열한 시쯤 배가 고파서 간식이나 사 먹으려고 집 근처 편의점에 갔어요.", "Yesterday at about eleven at night I was hungry and went to a convenience store near my house to buy a snack or something."),
    ("과자를 고르고 있는데 갑자기 흉기를 들고 복면을 한 강도가 편의점으로 들어왔어요.", "While I was picking out snacks, a robber carrying a lethal weapon and wearing a mask suddenly came into the convenience store."),
    ("그 강도는 들어오자마자 계산대 뒤에 있던 종업원을 위협하고 돈을 요구했어요.", "As soon as he came in, the robber threatened the employee behind the counter and demanded money."),
    ("종업원이 소리를 지르자 그 사람이 종업원을 칼로 찌르고 계산대에서 현금을 털어서 나갔어요.", "When the employee screamed, he stabbed the employee with a knife, took the cash from the register and left."),
    ("범인이 복면을 쓰고 있어서 얼굴을 자세히 보지는 못했지만 키는 약 백칠십오 센티미터 정도였고 좀 마른 편이었습니다.", "Because the criminal was wearing a mask I couldn’t see his face in detail, but he was about 175 cm tall and was a little on the thin side."),
    ("머리는 짧았어요.", "His hair was short."),
]
_A_WORDS = ["강도", "금품", "달아나다", "도둑", "도주하다", "범인", "범죄", "범행", "복면", "살인", "살해", "성폭행", "요구", "용의자", "위협", "저지르다", "전과", "절도", "종업원", "찌르다", "체포", "털다", "폭력", "피해자", "혐의", "훔치다", "흉기"]
_GAME = [("지난해 이월 중학교 이 학년이었던 에이 군은 새벽 다섯 시쯤 게임 아이템을 살 돈을 훔치기 위해 경남 거제시의 한 집으로 들어갔다.", "Last February, Mr. A, who was then in the second year of middle school, entered a house in Geoje, Gyeongnam, at about five in the morning to steal money to buy game items."), ("집 거실에서 일흔네 살 여성 비 씨에게 들킨 에이 군은 화분으로 비 씨의 머리를 때리고 흉기로 찔렀다.", "Caught in the living room by a 74-year-old woman, Ms. B, Mr. A hit Ms. B’s head with a planter and stabbed her with a lethal weapon."), ("칼에 찔린 피해자가 도둑이야 하고 소리치며 문 밖으로 도망갔으나 에이 군은 따라가서 다리를 잡아 비 씨를 쓰러뜨렸다.", "The stabbed victim ran out the door shouting “Thief”, but Mr. A followed, grabbed her leg and knocked her down."), ("이로 인해 비 씨는 아스팔트 바닥에 머리를 다쳤다.", "Because of this Ms. B hurt her head on the asphalt."), ("에이 군은 피해자의 소리를 듣고 달려 온 이웃의 신고로 경찰에 붙잡혔다.", "Mr. A was caught by the police on the report of a neighbor who ran over hearing the victim’s voice."), ("피해자는 그 후 병원에 옮겨졌지만, 범행 십여 일 뒤 끝내 숨졌다.", "The victim was then taken to the hospital but finally died more than ten days after the crime."), ("경찰은 에이 군을 강도살인 혐의로 체포했다.", "The police arrested Mr. A on suspicion of robbery and murder.")]
L3 = lesson(
    "Ch 38 · Topic A: The suspect in the convenience store robbery-murder was caught (편의점 강도살인 용의자가 붙잡혔어요)",
    "편의점 강도살인 용의자가 붙잡혔어요 · 흉기 · 도주 · 복면 · 목격자 진술 · 전과 · 게임 아이템과 노인 살해",
    requires=[],
    cards=[
        card("Topic A: The suspect in the convenience store robbery-murder was caught (편의점 강도살인 용의자가 붙잡혔어요)",
             "The following text includes an excerpt from a newspaper article about a robbery and murder, followed by an eyewitness’s statement. (The English is mine; the book gives none; the numbers are spelled out in Hangul. This is a news report of a fatal crime.)",
             examples=passage(_A_NEWS)),
        card("The eyewitness’s statement (목격자)",
             "The witness’s statement as in the book (the name is left out; “175cm” is read 백칠십오 센티미터; the English is mine).",
             examples=passage(_A_WIT)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists ~범 (a criminal; a person who committed [a crime]), 붙잡다/붙잡히다, 빼앗다, ~(이)나 and 자세히.",
             tables=[ktable(_rows(_A_WORDS)), table(["Word", "Meaning"], [["~범", "a criminal; a person who committed [a crime]"], ["붙잡다 / 붙잡히다", "to catch / to be caught; to arrest / to be arrested"], ["빼앗다", "to rob; to strip"], ["~(이)나", "just; settling for less-appealing option (nonnumerical noun + (이)나)"], ["자세히", "in detail; minutely"]], say=[0])]),
        card("Follow-up 2 (Reading): a crime article",
             "Read the article about a crime and fill in the table in English: perpetrator and victim; crime committed; motive; consequences. The book glosses 화분: planter; 들키다: to be caught; 도망가다: to flee. The headline (a middle school student who killed a person in their seventies over a game item) is the book’s idea; the article is the book’s with the numbers and the letters A and B spelled out; the English is mine. (This is a news report of a fatal crime.)",
             examples=passage(_GAME)),
        card("The table filled in (mine)", "The book leaves the table blank; my answers:",
             tables=[table(["Item", "Answer (mine)"], [["Perpetrator and victim", "Perpetrator: Mr. A, a second-year middle school student; victim: Ms. B, a 74-year-old woman"], ["Crime committed", "Entered a house, hit the woman’s head with a planter and stabbed her, then knocked her down (robbery and murder)"], ["Motive", "To steal money to buy game items"], ["Consequences", "The victim hurt her head and died more than ten days later; the student was caught on a neighbor’s report and arrested on suspicion of robbery and murder"]])]),
        card("Activities left out", "Follow-up 1 (listening to three eyewitness reports and noting place, description of the suspect, stolen goods and crime), Activity 1 (a speaking game with the vocabulary list), Activity 2 (three audio and video news reports on murder, sexual assault, dating violence or theft; one does not match), Activity 3 (two news articles on crimes read by two groups, with a table of crime, suspect, target, damage or stolen goods, methods and police actions) and Activity 4 (a police officer and an eyewitness role-play: 범인이 어떻게 생겼습니까?) are audio, video, group and role-play activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_NEWS + _A_WIT + _GAME, k=3)
        + [M("Where did the crime in Topic A happen?", "A convenience store in Incheon", ["A bank in Seoul", "A motel", "A school"], "인천시 계양구 편의점."), M("What did Mr. Kwon take?", "About 400,000 won in cash", ["A car", "Jewelry", "Nothing"], "현금 사십여만 원."), M("How did he escape?", "By taxi", ["On foot", "By bus", "By motorcycle"], "택시를 타고."), M("Who reported him?", "The motel owner", ["A neighbor", "The employee", "A taxi driver"], "모텔 주인의 신고."), M("How many previous convictions did he have?", "Seven", ["Two", "Three", "None"], "전과 칠 범."), M("How tall was the criminal according to the witness?", "About 175 cm", ["About 160 cm", "About 190 cm", "About 150 cm"], "약 백칠십오 센티미터."), M("What was the criminal wearing?", "A mask", ["A uniform", "A hat only", "Glasses"], "복면."), M("Why did Mr. A break into the house?", "To steal money for game items", ["To meet a friend", "To get revenge", "To find food"], "게임 아이템을 살 돈."),
           F("종업원을 흉기로 ___하고 도주했습니다. (killed)", "살해", ["요구", "체포"], "살해."), F("강도는 계산대에서 현금을 ___서 나갔어요. (took)", "털어", ["찔러", "붙잡아"], "털다."), F("경찰은 권 씨를 강도살인 ___로 체포했습니다. (suspicion)", "혐의", ["흉기", "전과"], "혐의."), F("복면을 한 ___가 편의점으로 들어왔어요. (robber)", "강도", ["피해자", "종업원"], "강도."), F("강도는 종업원을 ___하고 돈을 요구했어요. (threatened)", "위협", ["체포", "살해"], "위협하다."),
           read_q("편의점 강도살인 용의자가 붙잡혔어요"), read_q("종업원을 흉기로 살해하고 도주했습니다"), read_q("복면을 한 강도가 편의점으로 들어왔어요"), read_q("범인이 복면을 쓰고 있어서 얼굴을 자세히 보지 못했어요"), read_q("경찰은 권 씨를 강도살인 혐의로 체포했습니다")]
    ),
)

# ================================================================== L4 Topic B
_B_TXT = [
    ("저는 중학교 때 이사를 가서 다른 학교로 전학을 가게 되었습니다.", "When I was in middle school we moved, and I ended up transferring to another school."),
    ("그런데 전학 간 학교의 불량 학생들이 저를 놀리고 괴롭히기 시작했습니다.", "But the delinquent students at the school I transferred to started to tease and torment me."),
    ("그 아이들은 상습적으로 제 용돈을 빼앗고 욕하고 때렸어요.", "Those kids habitually took my allowance, swore at me and hit me."),
    ("게다가 저는 그 아이들이 시키는 대로 술도 마시고 담배도 피워야 했어요.", "On top of that, I had to drink and smoke as those kids told me to."),
    ("저는 부모님께 거짓말도 자주 했고 가출도 했습니다.", "I often lied to my parents, and I also ran away from home."),
    ("그러다가 같이 어울린 형들이 준 마약에 손을 대서 결국 중독되고 말았어요.", "Then I got involved with drugs given by older boys I hung out with and in the end became addicted."),
    ("학교에는 오랫동안 가지 않아서 퇴학 당했습니다.", "I didn’t go to school for a long time, so I was expelled."),
    ("하루는 피시방에서 물건을 훔치다가 들켜서 경찰에 신고당했습니다.", "One day I was caught stealing something at a PC room and was reported to the police."),
    ("다행히 경찰서에서 만난 좋은 경찰관의 도움으로 저는 비행 청소년 생활에서 완전히 벗어날 수 있었습니다.", "Fortunately, with the help of a good police officer I met at the police station, I was able to break away completely from the life of a juvenile delinquent."),
    ("그 경찰관 아저씨는 제 이야기를 듣고 제가 부모님과 다시 연락해서 집으로 돌아갈 수 있게 해 주고, 재활 치료도 받을 수 있도록 도움을 주었습니다.", "The police officer listened to my story, helped me contact my parents again and go back home, and helped me receive rehabilitation treatment."),
    ("그로부터 이십 년이 지난 지금 저는 청소년 상담사가 되어 있습니다.", "Twenty years have passed since then, and now I have become a youth counselor."),
    ("우리 주변에는 학교 폭력을 당하거나 담배나 마약에 중독되어 고통받는 많은 아이들이 있습니다.", "Around us there are many children who suffer from being victims of school violence or being addicted to cigarettes or drugs."),
    ("저는 제가 가장 힘들었을 때 저를 도와준 경찰관처럼 우리 사회의 청소년 문제 해결을 위해 제 인생을 살려고 합니다.", "Like the police officer who helped me when I was at my hardest, I intend to live my life for solving the youth problems of our society."),
]
_B_WORDS = ["가출", "가해자", "거짓말", "결국", "고통받다", "괴롭히다", "놀리다", "당하다", "들키다", "때리다", "마약", "벗어나다", "불량", "비행 청소년", "상담사", "어울리다", "완전히", "왕따", "욕", "용돈", "재활", "전학", "중독", "퇴학", "피우다", "해결", "협박", "호기심", "흡연"]
_DRUG = [("청소년들에게도 마약이 퍼지고 있습니다.", "Drugs are spreading even to teenagers."), ("경찰에 따르면 지난해 일 월부터 팔 월까지 마약 범죄로 붙잡힌 십구 세 이하 청소년은 삼백칠십이 명입니다.", "According to the police, from January to August of last year 372 teenagers aged 19 or under were caught for drug crimes."), ("그중 삼십팔 명은 십오 세 미만 청소년입니다.", "Of them, 38 are teenagers under 15."), ("이들은 온라인으로 마약을 구매한 뒤 감시를 피하려고 비트코인으로 값을 결제했습니다.", "They bought drugs online and paid for them in bitcoin to avoid surveillance."), ("비행 청소년들만 마약에 빠지는 것이 아닙니다.", "It is not only juvenile delinquents who fall into drugs."), ("원하지 않았는데 마약에 취하는 일도 있습니다.", "There are also cases of getting drugged without wanting to."), ("퐁당은 음료나 술에 몰래 마약을 타서 주는 행위를 부르는 은어입니다.", "“Pongdang” is slang for the act of secretly putting drugs in a drink or alcohol and giving it to someone."), ("마약이 든 음료를 한 번이라도 마시면 중독에 빠지기 쉽습니다.", "If you drink a drink containing drugs even once, it is easy to fall into addiction."), ("마약 중독자 회복을 위한 모임에 나온 에이 씨는 클럽에서도 콜라에 필로폰을 몰래 넣는 걸 여러 번 봤어요 하고 말했습니다.", "Mr./Ms. A, who came to a gathering for the recovery of drug addicts, said, “I saw them secretly put methamphetamine in cola many times at clubs too.”"), ("필로폰은 한 번만 해도 중독되는데 퐁당 당하고 나면 다 중독돼요 하고 말했습니다.", "And said, “Methamphetamine is addictive even if you do it just once, and after being ‘pongdang’-ed everyone gets addicted.”"), ("마약에 빠져서 고통받는 사람이 있다면 가까운 재활센터를 소개해야 합니다.", "If there is a person suffering from falling into drugs, you should introduce a nearby rehabilitation center.")]
L4 = lesson(
    "Ch 38 · Topic B: I am a youth counselor (저는 청소년 상담사입니다)",
    "저는 청소년 상담사입니다 · 전학 · 왕따 · 가출 · 마약 중독 · 퇴학 · 재활 · 집단 따돌림 · 손을 대다 · 청소년과 마약",
    requires=[],
    cards=[
        card("Topic B: I am a youth counselor (저는 청소년 상담사입니다)",
             "A youth counselor tells a group of high school students about his experience of school violence and drug addiction. He also shares the story of how he turned his life around and became a youth counselor. (The English is mine; the book gives none; the printed text has a blank line before 때렸어요, which is left out here; “PC” is read 피시.)",
             examples=passage(_B_TXT)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists –고 말다, –(는) 대로, 상습적으로 and 손(을) 대다 (see the grammar and the notes below).",
             tables=[ktable(_rows(_B_WORDS)), table(["Word", "Meaning"], [["상습적으로", "habitually"], ["손(을) 대다", "to meddle with; to become involved with; “to lay one’s hands (on something)”"], ["-고 말다", "to end up –"], ["-(는) 대로", "in accordance with; as"]], say=[0])]),
        card("한국어에는: 1. 집단 따돌림, 왕따, and 학폭",
             "“집단 따돌림”, “왕따”, and “학폭” refer to different forms of school violence. 집단 따돌림 literally means “group shunning” and often involves a group of people ostracizing one person. 왕따 is a slang term that combines 왕, which literally means “king” but is often used as a superlative in Korean slang, and 따 (short for 따돌림), and can be literally understood as “super-ostracizing”. Nowadays, the term “학교 폭력”, also known as “학폭” in short, is commonly used to encompass various forms of abuse in schools, including physical, verbal, and emotional mistreatment directed towards victims."),
        card("한국어에는: 2. 당하다",
             "The verb 당하다 (to sustain physical or mental damage) is used to express suffering from physical or mental damage. Therefore, you will often encounter 당하다 in the context of crime, disaster, or mishap, as in 왕따를 당하다, 폭행을 당하다, 사기를 당하다, etc."),
        card("한국어에는: 3. ~에 손을 대다",
             "~에 손을 대다 or ~에 손대다 literally means “to lay one’s hands on (something/someone)”. This expression is often used to mean “to start something” (unpleasant), such as drugs, alcohol, or tobacco (술에 손을 대다, 노름에 손을 대다, etc.). ~에서 손을 떼다 or ~에서 손떼다 is used to mean “quit something” unpleasant (담배에서 손을 떼다)."),
        card("Follow-up 1 (Reading): a news article about drug problems",
             "The following news article is about drug problems. The book glosses 퍼지다: to spread; 감시: watch, surveillance; 은어: slang. The book asks you (a) to create a headline in Korean and (b) to fill in a table in English: police statistics findings; experience shared by interviewee A; new slang word and its definition; way(s) to provide help. The article is the book’s with the numbers spelled out, the quotation marks dropped (the quoted speech is marked with “ ” in English only), and the phone numbers of the treatment centers left out; the English is mine.",
             examples=passage(_DRUG)),
        card("The headline and table (mine)", "My answers:",
             tables=[table(["Item", "Answer (mine)"], [["Headline (Korean)", "청소년에게도 퍼지는 마약"], ["Police statistics findings", "From January to August last year 372 teenagers aged 19 or under were caught for drug crimes; 38 of them were under 15; they bought drugs online and paid in bitcoin"], ["Experience shared by interviewee A", "Saw drugs secretly put in cola at clubs many times; methamphetamine is addictive even after one use; after being ‘pongdang’-ed everyone becomes addicted"], ["New slang word and its definition", "퐁당: secretly putting drugs in a drink or alcohol and giving it to someone"], ["Way(s) to provide help", "Introduce a nearby rehabilitation center; free treatment hospitals and an addiction rehabilitation center are available"]])]),
        card("Activities left out", "The study steps of Topic Presentation B (reading and listening, translating in pairs, a counseling card from a school violence counseling center and the role-play between a counselor and Seongsu) and Follow-up 2 (listening to three conversations between a teenager and a counselor about drug addiction, smoking, drinking or bullying) are audio and role-play activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT + _DRUG, k=3)
        + [M("Why did the narrator transfer schools?", "His family moved", ["He was expelled", "He ran away", "He wanted to"], "이사를 가서."), M("What did the delinquent students do?", "Teased, tormented, took his allowance and hit him", ["Helped him", "Ignored him", "Taught him"], "놀리고 괴롭히기 시작했습니다."), M("How did he become addicted?", "He took drugs given by older boys", ["He bought them online", "A doctor gave them", "He found them"], "형들이 준 마약."), M("Why was he expelled?", "He didn’t go to school for a long time", ["He stole at school", "He fought", "He cheated"], "오랫동안 가지 않아서."), M("Who helped him leave that life?", "A good police officer", ["A teacher", "His parents", "A doctor"], "경찰관의 도움."), M("What is he now?", "A youth counselor", ["A police officer", "A teacher", "A doctor"], "청소년 상담사."), M("What does 퐁당 mean in the article?", "Secretly putting drugs in a drink", ["Selling drugs online", "Smuggling drugs", "A drug treatment"], "은어."), M("What does 왕따 literally mean?", "“super-ostracizing”", ["“group shunning”", "“king of drinks”", "“school violence”"], "The book’s note."),
           F("친구를 ___ 마세요. (tease)", "놀리지", ["때리지", "괴롭히지"], "놀리다."), F("그 아이들은 ___으로 제 용돈을 빼앗았어요. (habitually)", "상습적", ["완전히", "결국"], "상습적으로."), F("마약에 ___해서 결국 중독되고 말았어요. (got involved)", "손을 대", ["벗어나", "어울리"], "손을 대다."), F("경찰관의 도움으로 비행 청소년 생활에서 ___ 벗어날 수 있었습니다. (completely)", "완전히", ["결국", "상습적으로"], "완전히."), F("학교 폭력을 ___ 아이들이 많습니다. (suffer; be victims of)", "당하는", ["하는", "주는"], "당하다."),
           read_q("저는 청소년 상담사입니다"), read_q("전학 간 학교의 불량 학생들이 저를 괴롭히기 시작했습니다"), read_q("마약에 손을 대서 결국 중독되고 말았어요"), read_q("비행 청소년 생활에서 완전히 벗어날 수 있었습니다"), read_q("청소년에게도 마약이 퍼지고 있습니다")]
    ),
)

# ================================================================== L5 Grammar A: 대로
_DA1 = [("서울에 도착하는 대로 전화할게요.", "I will call you as soon as I arrive in Seoul.")]
_DA2 = [("약속한 대로 일곱 시에 오겠습니다.", "I will come at 7 as I promised."), ("약속대로 일곱 시에 오겠습니다.", "I will come at 7 in accordance with my promise.")]
_DA3 = [("제가 생각했던 대로 이번 시험은 쉬웠습니다.", "Like I thought, this test was easy."), ("어제 예상한 대로 지금 비가 옵니다.", "(Just) as I expected yesterday, it is raining now."), ("선생님 말씀대로 한국에 가겠습니다.", "I will go to Korea “in accordance with your saying” / as you say.")]
_DAM = [("의사가 처방하다", "환자가 약을 먹다", "의사가 처방한 대로 환자가 약을 먹어요.", "As the doctor prescribed, the patient takes the medicine."), ("교관이 시키다", "수류탄을 던지다", "교관이 시키는 대로 수류탄을 던져요.", "I throw the grenade as the instructor tells me."), ("라디오에서 예보하다", "비가 오다", "라디오에서 예보한 대로 비가 와요.", "As the radio forecast, it rains."), ("친구에게 약속하다", "콘서트에 같이 가다", "친구에게 약속한 대로 콘서트에 같이 가요.", "As I promised my friend, we go to the concert together."), ("음식을 주문하다", "비빔밥이 나오다", "음식을 주문한 대로 비빔밥이 나와요.", "As I ordered, bibimbap comes out.")]
L5 = lesson(
    "Ch 38 · Grammar A: “in accordance with” and “as”, –는/(으)ㄴ 대로 and ~대로",
    "-는 대로 · -(으)ㄴ 대로 · ~대로 · 약속한 대로 · 선생님 말씀대로 · 의사가 처방한 대로",
    requires=[],
    cards=[
        card("In accordance with / as",
             "In an earlier chapter, you learned that the conjunctive ending –는 대로 attached to the stem of an action verb can translate to as soon as or immediately after, even though it is used when the time of an action or event is not fixed (the English is the book’s):",
             examples=passage(_DA1)),
        card("The underlying meaning", "Thus, the underlying meaning of the conjunctive ending is in accordance with or as. Therefore, 서울에 도착하는 대로 전화할게요 essentially says, “I don’t know when I will arrive in Seoul, but I will call you (as soon) as I arrive there. If I arrive there at six, I will call you then. If I arrive there at nine, I will call you then.”\n\nIn this lesson, we examine sentences in which the underlying meaning of –는/(으)ㄴ 대로 or ~대로 (in accordance with; as) is used."),
        card("약속한 대로 / 약속대로", "Both sentences convey the same message, but note that the conjunctive ending –는/(으)ㄴ 대로 is attached to the attributive form of the verb 약속하다 (to promise), whereas the marker ~대로 is attached to the noun 약속 (promise). In fact, ~대로 frequently works with nouns such as 약속, 말, 말씀, 생각, or 의견. (The English is the book’s.)", examples=passage(_DA2)),
        card("“In accordance with” / “as”", "verb stem + 는/(으)ㄴ 대로; noun + 대로. More examples (the English is the book’s):", examples=passage(_DA3)),
        card("Follow-up 1 (Reading and speaking): matching",
             "The book asks you to match each phrase in the left column with its most closely related phrase on the right (answers may vary), then take turns making a sentence with two matched phrases and the pattern –는/(으)ㄴ 대로. The phrases are the book’s; the pairs and the sentences are mine; the book’s model is 의사가 처방하다 / 환자가 약을 먹다.",
             tables=[table(["Left", "Right (mine)", "Sentence (mine)"], [[a, b, c] for a, b, c, d in _DAM], say=[2])],
             examples=passage([(c, d) for a, b, c, d in _DAM])),
        card("Activities left out", "Follow-up 2 (listening to six short dialogs and checking whether 대로 means “as soon as” or “in accordance with”, with the English meaning of each verbal phrase) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_DA1 + _DA2 + _DA3 + [(c, d) for a, b, c, d in _DAM], k=3)
        + [M("What is the underlying meaning of –는/(으)ㄴ 대로?", "in accordance with; as", ["because", "although", "in order to"], "The book’s note."), M("What does 약속한 대로 mean?", "as I promised", ["because I promised", "if I promise", "although I promised"], "The book’s example."), M("What is 대로 attached to in 약속대로?", "A noun", ["A verb stem", "An adverb", "A particle"], "The book’s note."), M("What does 선생님 말씀대로 한국에 가겠습니다 mean?", "I will go to Korea as you say", ["I will not go to Korea", "I went to Korea", "I like Korea"], "The book’s example."), M("Which nouns often take ~대로?", "약속, 말, 말씀, 생각, 의견", ["학교, 책, 물", "아침, 저녁, 밤", "집, 차, 옷"], "The book’s note."),
           F("의사가 처방한 ___ 환자가 약을 먹어요. (as)", "대로", ["때문에", "만큼"], "대로."), F("제가 생각했던 ___ 이번 시험은 쉬웠습니다. (as)", "대로", ["때문에", "처럼"], "대로."), F("선생님 말씀___ 한국에 가겠습니다. (as you say)", "대로", ["마다", "부터"], "말씀대로."), F("어제 ___ 대로 지금 비가 옵니다. (expected; past attributive)", "예상한", ["예상하는", "예상할"], "예상한 대로."), F("교관이 ___ 대로 수류탄을 던져요. (tells; present attributive)", "시키는", ["시킨", "시킬"], "시키는 대로."),
           read_q("약속한 대로 일곱 시에 오겠습니다"), read_q("약속대로 일곱 시에 오겠습니다"), read_q("어제 예상한 대로 지금 비가 옵니다"), read_q("선생님 말씀대로 한국에 가겠습니다"), read_q("의사가 처방한 대로 환자가 약을 먹어요")]
    ),
)

# ================================================================== L6 Grammar B: -고 말다
_GB1 = [("동생이 내 피자를 다 먹어 버렸어요.", "My younger brother ate all my pizza (and it is no longer available to me)."), ("김 일병이 한국에 가 버렸어요.", "PFC Kim went to Korea (and he is no longer with us).")]
_GB2 = [("컴퓨터를 사고 말았어요.", "I ended up buying a computer after all (despite the fact that I couldn’t afford to buy a computer)."), ("김 일병이 한국에 가고 말았어요.", "(I told PFC Kim not to go to Korea but) he ended up going to Korea after all.")]
_GB3 = [("오늘 아침 우리 집 개가 죽고 말았어요.", "(I prayed for my sick dog all along, but) my dog ended up dying this morning after all."), ("여자 친구가 파티에 안 오고 말았어요.", "(I had expected her all along, but) my girlfriend ended up not coming to the party after all."), ("마침내 컴퓨터가 고장이 나고 말았어요.", "(My computer had acted up in the past, and) finally it broke down after all.")]
_GB4 = [("디엘피티에 꼭 합격하고 말겠어요.", "I will surely pass the DLPT."), ("내년에 한국에 가고 말겠어요.", "I will definitely go to Korea next year."), ("다음 주에 그 자동차를 사 버리겠어요.", "I will buy the car next week.")]
_GBD = [("수영", "명인 씨, 안녕하십니까? 요즘 어때요?", "Myeongin, how are you? How have things been lately?"), ("명인", "별로예요.", "Not so good."), ("수영", "무슨 일이 있으세요?", "Is something the matter?"), ("명인", "어제 제 핸드폰이 고장이 나고 말았어요.", "Yesterday my cell phone broke down after all.")]
_GBM = [("열심히 공부했는데 시험을 못 보고 말았어요.", "I studied hard but ended up doing poorly on the exam."), ("조심했는데 감기에 걸리고 말았어요.", "I was careful but ended up catching a cold."), ("안 가려고 했는데 결국 가고 말았어요.", "I didn’t intend to go but ended up going.")]
L6 = lesson(
    "Ch 38 · Grammar B: the auxiliary verb –고 말다 (ending up doing)",
    "-고 말다 · -아/어 버리다와 비교 · 사고 말았어요 · 죽고 말았어요 · 꼭 합격하고 말겠어요",
    requires=[],
    cards=[
        card("Recall –아/어 버리다",
             "Recall the auxiliary verb –아/어 버리다, which you learned about in Chapter 27. It is used to express a completed action and normally implies that the completed action is not reversible or that something/someone is no longer available. For example (the English is the book’s):",
             examples=passage(_GB1)),
        card("–고 말다",
             "The auxiliary verb –고 말다 is also used to express a completed action. However, this auxiliary verb normally implies that the completed action is against one’s intention, wish, or warning. For example (the English is the book’s):",
             examples=passage(_GB2)),
        card("Action completed against one’s intention, wish, or warning", "action verb + 고 말다. More examples (the English is the book’s):", examples=passage(_GB3)),
        card("참고: the future tense",
             "Both –고 말다 and –아/어 버리다 in the future tense are used to express the speaker’s strong intention of doing or accomplishing something (despite obstacles). (The English is the book’s; DLPT is read 디엘피티.)",
             examples=passage(_GB4)),
        card("Follow-up 4 (Speaking): 넘어지고 말았어요",
             "In this activity, you share with your classmates something you ended up doing against your will or intention (doing poorly on an exam despite studying, your car breaking down, catching a cold, etc.). You write at least three incidents in a table and share them using –고 말다. The book’s model (the English is mine):",
             examples=dlg(_GBD)),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_GBM)),
        card("Activities left out", "Follow-up 3 (listening to three narrations and noting what the female speaker intended to do and what she ended up doing) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_GB1 + _GB2 + _GB3 + _GB4 + _GBM, k=3) + _tr(_strip(_GBD), k=2)
        + [M("What does –고 말다 normally imply?", "The completed action is against one’s intention, wish, or warning", ["A strong request", "A habit", "A polite wish"], "The book’s note."), M("What does –아/어 버리다 normally imply?", "The completed action is not reversible or something is no longer available", ["It is against one’s intention", "A habit", "A request"], "The book’s note."), M("What does 컴퓨터를 사고 말았어요 mean?", "I ended up buying a computer after all", ["I will buy a computer", "I sold a computer", "I like computers"], "The book’s example."), M("What does –고 말겠어요 express?", "A strong intention", ["A past regret", "A polite request", "A habit"], "The book’s 참고."), M("What does 개가 죽고 말았어요 mean?", "My dog ended up dying", ["My dog is sleeping", "I bought a dog", "My dog ran away"], "The book’s example."),
           F("컴퓨터가 고장이 나___ 말았어요. (ending)", "고", ["서", "면"], "-고 말다."), F("디엘피티에 꼭 합격하___ 말겠어요. (ending)", "고", ["서", "면"], "-고 말겠어요."), F("여자 친구가 파티에 안 오고 ___어요. (ended up)", "말았", ["버렸", "있었"], "말았어요."), F("동생이 내 피자를 다 먹어 ___어요. (-아/어 버리다)", "버렸", ["말았", "있었"], "버렸어요."), F("조심했는데 감기에 걸리___ 말았어요. (ending)", "고", ["서", "면"], "-고 말다."),
           read_q("컴퓨터를 사고 말았어요"), read_q("여자 친구가 파티에 안 오고 말았어요"), read_q("마침내 컴퓨터가 고장이 나고 말았어요"), read_q("내년에 한국에 가고 말겠어요"), read_q("어제 제 핸드폰이 고장이 나고 말았어요")]
    ),
)

# ================================================================== L7 Activities (university violence article)
_UNI = [("전국 사 년제 대학생 열 명 중 세 명은 대학에서 학교폭력을 목격한 것으로 조사됐다.", "Three out of ten four-year university students nationwide were found to have witnessed school violence at university."), ("연구진은 칠 개월간 대학생 온라인 커뮤니티 에브리타임을 통해 총 사백육십칠 명의 설문 결과를 수집했다.", "The researchers collected the survey results of a total of 467 people over seven months through the university students’ online community Everytime."), ("이 조사에 따르면 사 년제 대학생 사백육십칠 명 중 백삼십오 명, 이십팔 점 구 퍼센트가 대학에서 학교폭력을 목격한 적이 있다고 답했다.", "According to this survey, 135 of the 467 four-year university students, 28.9 percent, answered that they had witnessed school violence at university."), ("대학생 사이 폭력은 언어폭력이 육십팔 점 구 퍼센트로 가장 많았으며 그 뒤로 성추행 성폭력, 삼십이 점 육 퍼센트, 신체 폭력, 십칠 점 영 퍼센트 순이었다.", "Among violence between university students, verbal violence was the most common at 68.9 percent, followed by sexual harassment and sexual violence at 32.6 percent and physical violence at 17.0 percent."), ("강제 심부름, 십육 점 삼 퍼센트, 집단 따돌림과 사이버폭력, 십일 점 구 퍼센트도 목격 비율이 높은 것으로 조사됐다.", "Forced errands, 16.3 percent, and group bullying and cyber violence, 11.9 percent, also had high witnessing rates."), ("학교폭력 목격 장소의 경우 강의실이 칠십팔 점 사 퍼센트로 가장 높은 비율을 보였으며, 강의실 외 교내시설, 사십육 점 사 퍼센트, 교내 건물 밖, 삼십오 점 일 퍼센트의 순으로 나타났다.", "As for places where school violence was witnessed, lecture rooms showed the highest rate at 78.4 percent, followed by campus facilities other than lecture rooms, 46.4 percent, and outside campus buildings, 35.1 percent."), ("응답자의 팔 점 육 퍼센트가 학교폭력 피해를 직접 겪었다고 답했으며, 가해 경험이 있다는 응답자는 없었다.", "8.6 percent of respondents answered that they had directly experienced school violence damage, and no respondent said they had experience as a perpetrator."), ("학교폭력을 목격한 학생 중 육십육 점 삼 퍼센트는 이후 경찰이나 학교에 신고하지 않았다.", "Of the students who witnessed school violence, 66.3 percent did not report it to the police or school afterward."), ("신고했다고 응답한 경우는 이십칠 점 구 퍼센트밖에 되지 않았다.", "Those who answered that they had reported it were only 27.9 percent."), ("연구진은 대학생들의 학교폭력 신고율이 낮게 나타나는 이유를 주위 문제에 무관심한 태도와, 신고를 해도 도움이 되지 못했던 경험이 합쳐져 일어나는 현상이라고 분석했다.", "The researchers analyzed the reason for the low reporting rate of school violence among university students as a phenomenon caused by a combination of an indifferent attitude toward surrounding problems and the experience that reporting did not help.")]
L7 = lesson(
    "Ch 38 · Activities: a survey on school violence at university",
    "대학생 학교폭력 설문 · 언어폭력 · 성추행 · 집단 따돌림 · 신고율",
    requires=[],
    cards=[
        card("Activity 3 (Reading): a news article about an online survey",
             "The following news article is about an online survey (Chosun). The book glosses 성추행: sexual harassment; 강제 심부름: forced errands; 합쳐지다: to be combined. The article is the book’s with the numbers and percentages spelled out (the decimal point is read 점 and “·” and brackets are dropped); the English is mine.",
             examples=passage(_UNI)),
        card("The questions and my answers",
             "The book asks you to (a) create a Korean headline, (b) tell how the researchers collected the data and over what period, (c) list the three most common types of violence observed, (d) say what 78.4%, 8.6% and 66.3% refer to, and (e) give the reasons for the low reporting rate. My answers:",
             tables=[table(["Question", "Answer (mine)"], [["a. Korean headline", "대학생 열 명 중 세 명이 대학에서 학교폭력 목격"], ["b. How data were collected and over what period", "An online survey of 467 students through the online community Everytime over seven months"], ["c. Three most common types of violence", "1. verbal violence; 2. sexual harassment and sexual violence; 3. physical violence"], ["d. 78.4%", "The share of witnesses who saw the violence in a lecture room"], ["d. 8.6%", "The share of respondents who directly experienced school violence"], ["d. 66.3%", "The share of witnesses who did not report it to the police or school"], ["e. Reasons for the low reporting rate", "An indifferent attitude toward surrounding problems combined with the experience that reporting did not help"]])]),
        card("Activities left out", "Activity 1 (a vocabulary card game between two teams), Activity 2 (listening to an EBS news report on a school bullying survey and noting what has decreased and increased, the most common type and reason of bullying) and Activity 4 (two cases of school bullying, one to be listened to on YTN and one read in hani.co.kr, analyzed in groups; the book glosses 유서: last words/note; 동급생: class mates; 후속조치: follow-up measures; 항변하다: to plead; then preventive measures presented on a flip chart) are audio, group and game activities."),
    ],
    exercises=uniq(
        _tr(_UNI, k=3)
        + [M("How many students out of ten witnessed school violence?", "Three", ["One", "Five", "Seven"], "열 명 중 세 명."), M("How did researchers collect the data?", "Through an online community", ["By phone", "By mail", "In person"], "에브리타임."), M("How long did the collection take?", "Seven months", ["One week", "One year", "Two months"], "칠 개월."), M("What was the most common violence?", "Verbal violence", ["Physical violence", "Cyber violence", "Forced errands"], "언어폭력."), M("Where was violence witnessed most?", "Lecture rooms", ["Outside buildings", "Dormitories", "Cafeterias"], "강의실."), M("Did any respondent report being a perpetrator?", "No", ["Yes, many", "Yes, a few", "Not asked"], "가해 경험이 있다는 응답자는 없었다."), M("What did the researchers say about low reporting?", "Indifference and the experience that reporting did not help", ["Fear of police", "No one knew how", "Lack of time"], "무관심한 태도."),
           F("대학생 사이 ___은 언어폭력이 가장 많았다. (violence)", "폭력", ["범죄", "절도"], "폭력."), F("연구진은 설문 결과를 ___했다. (collected)", "수집", ["사용", "설치"], "수집."), F("학교폭력을 목격하고도 ___하지 않은 학생이 많았다. (report)", "신고", ["체포", "수사"], "신고."), F("응답자의 팔 점 육 퍼센트가 피해를 직접 ___다고 답했다. (experienced)", "겪었", ["저질렀", "털었"], "겪다."), F("신고율이 낮은 ___를 분석했다. (reason)", "이유", ["결과", "장소"], "이유."),
           read_q("대학생 학교폭력 설문"), read_q("언어폭력이 가장 많았습니다"), read_q("강의실에서 가장 많이 목격했습니다"), read_q("경찰이나 학교에 신고하지 않았습니다"), read_q("신고율이 낮은 이유를 분석했습니다")]
    ),
)

# ================================================================== L8 Topic C
_C_DLG = [
    ("앵커", "형사님, 안녕하세요. 우리 사회가 변화하면서 예전에 비해서 자주 일어나는 범죄에도 많은 변화가 있을 것 같은데요. 어떻습니까?", "Detective, hello. As our society changes, it seems there have also been many changes in the crimes that happen often compared with the past. How is it?"),
    ("형사", "네, 우선 살인, 강도, 납치, 방화 같은 전통적인 강력 범죄들은 많이 줄어들었습니다.", "Yes, first of all, traditional violent crimes such as murder, robbery, kidnapping and arson have decreased a lot."),
    ("앵커", "아, 다행이네요. 예전에는 소매치기나 위조지폐 사건도 많았는데 요즘은 어떤가요?", "Oh, that’s good. In the past there were also many pickpocketing and counterfeit bill cases; how is it these days?"),
    ("형사", "네, 소매치기 사건은 거의 없고요. 위조지폐 사건도 상당히 줄어서 작년 한 해 동안 위조지폐 발생 건수는 백오십 건 정도밖에 되지 않았습니다.", "Yes, there are almost no pickpocketing cases. Counterfeit bill cases have also decreased considerably, so over the past year the number of counterfeit bill cases was only about 150."),
    ("앵커", "그렇군요. 그럼 이런 범죄들이 줄어든 원인은 뭐라고 보십니까?", "I see. Then what do you think is the reason these crimes have decreased?"),
    ("형사", "무엇보다 현금 대신 신용카드나 스마트폰 결제가 일반화된 이유가 크고요. 씨씨티브이 사용이 늘면서 곳곳에 설치되어 있는 카메라를 피해 범행을 저지르는 것이 거의 불가능해졌습니다. 또 과학 수사의 발달로 우리가 확실한 증거를 빨리 모을 수가 있게 되었고요.", "Above all, the generalization of credit card and smartphone payment instead of cash is a big reason. With the increased use of CCTV, it has become almost impossible to commit a crime avoiding the cameras installed everywhere. Also, thanks to the development of scientific investigation, we have become able to collect solid evidence quickly."),
    ("앵커", "네. 그렇군요. 그런데 과학의 발달과 함께 늘어난 범죄도 있을 것 같은데요.", "I see. But it seems there are also crimes that have increased along with the development of science."),
    ("형사", "그럼요. 인터넷이나 스마트폰을 이용한 디지털 범죄, 특히 보이스피싱 같은 사기 범죄가 크게 늘었습니다. 이와 함께 해킹을 통한 개인정보 유출, 마약 밀수 등의 불법도 크게 늘었고요.", "Of course. Digital crimes using the Internet or smartphones, especially fraud crimes such as voice phishing, have increased greatly. Along with this, illegal acts such as leaks of personal information through hacking and drug smuggling have also increased greatly."),
    ("앵커", "아, 과학의 발달을 악용해 범죄에 이용하는 경우들이 늘었군요.", "Oh, so cases of misusing the development of science and using it for crime have increased."),
    ("형사", "네, 그렇습니다. 우리 사회 환경이 변하는 한 그와 함께 범죄도 계속 변화할 겁니다.", "Yes, that’s right. As long as our social environment changes, crime will also keep changing along with it."),
]
_C_WORDS = ["가짜", "강력", "건", "납치", "모으다", "밀수", "발달", "방화", "법", "불법", "사건", "사기", "사용", "설치", "소매치기", "수사", "악용", "유출", "위조", "일반화", "증거", "지폐", "형사", "확실하다"]
_C_WORDS2 = [("~에 비해(서)", "compared with / to"), ("~짜리", "(a thing) worth ~"), ("상당히", "considerably; remarkably"), ("-(으)ㄴ/는 한", "as long as")]
_FAKE = [("영화 소품으로 사용되는 오만 원권 위조지폐를 실제 돈처럼 사용한 혐의를 받는 삼십 대 외국인 남성이 구속됐다.", "A foreign man in his thirties suspected of using counterfeit 50,000-won bills used as movie props like real money has been arrested."), ("십육 일 경찰에 따르면 서울 동대문경찰서는 사기 혐의를 받는 외국 국적 남성 에이 씨를 구속해 수사하고 있다.", "According to the police on the 16th, the Dongdaemun Police Station in Seoul has arrested a foreign-national man, Mr. A, suspected of fraud and is investigating."), ("에이 씨는 지난달부터 이달 초까지 동대문구의 한 시장 등에서 영화 소품용 오만 원권 위조지폐로 오천 원짜리 물건을 구매하고 사만 오천 원을 거스름돈으로 받은 혐의를 받고 있다.", "Mr. A is suspected of buying 5,000-won items with movie-prop counterfeit 50,000-won bills at a market in Dongdaemun-gu and elsewhere from last month to early this month and receiving 45,000 won as change."), ("에이 씨는 가짜 오만 원권 지폐 열두 장을 사용했다고 진술했는데, 경찰은 이 중 네 장을 증거로 회수했다 한다.", "Mr. A stated that he used twelve fake 50,000-won bills, and the police are said to have retrieved four of them as evidence."), ("경찰 조사 결과 범행에 사용된 가짜 지폐는 실제 지폐에 비해서 크기가 크고 아래쪽에 영화 소품용이므로 사용할 수 없다라는 문구가 적혀 있는 것으로 드러났다.", "As a result of the police investigation, it turned out that the fake bills used in the crime were bigger than real bills and had the phrase “It is for movie props so it cannot be used” written at the bottom.")]
L8 = lesson(
    "Ch 38 · Topic C: Changes in crime with social change (사회변화에 따른 범죄의 변화)",
    "사회변화에 따른 범죄의 변화 · 강력 범죄 · 소매치기 · 위조지폐 · 보이스피싱 · 해킹 · 마약 밀수 · 위조지폐 사건",
    requires=[],
    cards=[
        card("Topic C: Changes in crime with social change (사회변화에 따른 범죄의 변화)",
             "The following text is an excerpt from a TV program in which an anchor is interviewing a detective about the shifts in crime. (The English is mine; the book gives none; “CCTV” is read 씨씨티브이 and the number is spelled out.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists ~에 비해(서), ~짜리, 상당히 and –(으)ㄴ/는 한.",
             tables=[ktable(_rows(_C_WORDS)), table(["Word", "Meaning"], [[a, b] for a, b in _C_WORDS2], say=[0])]),
        card("Follow-up 2 (Reading): a counterfeit-bill article",
             "Read the news about a crime and fill in the table. The book glosses 소품: prop; 거스름돈: change; 회수하다: to retrieve; 유통하다: to circulate. The article is the book’s with the numbers spelled out (the quotation marks are dropped); the English is mine.",
             examples=passage(_FAKE)),
        card("The table filled in (mine)", "The book’s table has the columns allegations, suspect A, distinguishing features of the bills used in the crime and proof of the crime collected by the police. My answers:",
             tables=[table(["Item", "Answer (mine)"], [["Allegations", "Fraud: using movie-prop counterfeit 50,000-won bills like real money (buying 5,000-won items and receiving 45,000 won in change)"], ["Suspect A", "A foreign-national man in his thirties, arrested and under investigation by the Dongdaemun Police Station"], ["Distinguishing features of the bills", "Bigger than real bills; a phrase at the bottom says they are for movie props and cannot be used"], ["Proof collected by the police", "Four of the twelve fake bills he said he used"]])]),
        card("Activities left out", "The study steps of Topic Presentation C (SMART Board), Follow-up 1 (listening to three KBS and YTN crime news reports and video clips), Activity 1 (a vocabulary speaking game), Activity 2 (a KBS report on a crime concerning LG Uplus, a South Korean mobile network operator, with a table on what happened, the perpetrator’s ultimate goal, who is affected and what steps LG is taking) and Activity 3 (two articles on voice phishing scams read in groups, with a presentation of at least three measures to avoid them) are audio, video, group and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG), k=3) + _tr(_FAKE, k=3)
        + [M("Which crimes have decreased?", "Traditional violent crimes", ["Voice phishing", "Hacking", "Drug smuggling"], "전통적인 강력 범죄."), M("How many counterfeit bill cases were there last year?", "About 150", ["About 15", "About 1,500", "None"], "백오십 건."), M("Why have these crimes decreased?", "Card and smartphone payment, CCTV and scientific investigation", ["More police", "Stricter laws", "Fewer people"], "결제, 씨씨티브이, 과학 수사."), M("Which crimes have increased?", "Voice phishing, hacking leaks and drug smuggling", ["Pickpocketing", "Arson", "Kidnapping"], "디지털 범죄."), M("What will happen as long as the social environment changes?", "Crime will keep changing", ["Crime will stop", "Crime will decrease", "Nothing"], "계속 변화할 겁니다."), M("What was written on the fake bills?", "That they are for movie props and cannot be used", ["The bank’s name", "A serial number", "The year"], "영화 소품용이므로 사용할 수 없다."), M("How many fake bills did the suspect say he used?", "Twelve", ["Four", "Two", "Fifty"], "열두 장."),
           F("작년 위조지폐 발생 ___수는 백오십 건 정도였다. (case count)", "건", ["장", "명"], "건수."), F("과학 수사의 ___로 확실한 증거를 빨리 모을 수 있다. (development)", "발달", ["설치", "유출"], "발달."), F("인터넷을 이용한 디지털 범죄, 특히 보이스피싱 같은 ___ 범죄가 늘었다. (fraud)", "사기", ["방화", "납치"], "사기."), F("해킹을 통한 개인정보 ___이 늘었다. (leak)", "유출", ["설치", "발달"], "유출."), F("과학의 발달을 ___해 범죄에 이용한다. (misuse)", "악용", ["사용", "설치"], "악용."),
           read_q("사회변화에 따른 범죄의 변화"), read_q("전통적인 강력 범죄들은 많이 줄어들었습니다"), read_q("위조지폐 사건도 상당히 줄었습니다"), read_q("보이스피싱 같은 사기 범죄가 크게 늘었습니다"), read_q("범죄도 계속 변화할 겁니다")]
    ),
)

# ================================================================== L9 Grammar -아/어 있다
_ES1 = [("이 선생님이 바닥에 앉고 있어요.", "Ms. Lee is sitting down on the floor (in the process)."), ("이 선생님이 바닥에 앉아 있어요.", "Ms. Lee is sitting on the floor (in the state).")]
_ES2 = [("친구가 지금 유럽에 가 있어요.", "My friend is (in the state of being) in Europe."), ("차고 문이 열려 있어요.", "The garage door is (in the state of being) open.")]
_ES3 = [("형이 침대에 누워 있어요.", "My older brother is (in the state of) lying on the bed."), ("창문이 닫혀 있어요.", "The window is (in the state of being) closed."), ("카메라가 설치되어 있습니다.", "The camera is (in the state of being) installed.")]
_BRI = [("브리스톨 영어 학교는 영국의 크고 매력적인 남부 도시에 있어요.", "The Bristol English School is in a big, attractive southern city of England."), ("이 학교는 명문대 브리스톨대와 연계되어 있어서 브리스톨 대학시설을 이용할 수 있어요.", "This school is connected with the prestigious University of Bristol, so you can use the University of Bristol’s facilities."), ("또, 이 학교는 영어 교육 프로그램뿐만 아니라 다양한 문화 프로그램이 마련되어 있어요.", "Also, this school has not only English education programs but also various cultural programs prepared."), ("특히, 일주일에 두 번 문화행사가 있어서 영국의 문화를 체험할 수 있습니다.", "In particular, there are cultural events twice a week, so you can experience British culture."), ("그리고 기숙사 각 방마다 전화 및 최고속 인터넷이 설치되어 있어서 편해요.", "And every dormitory room has a phone and top-speed Internet installed, so it is convenient."), ("저는 지금 브리스톨 영어 학교에서 영어를 배운 지 삼 개월이 되었어요.", "It has been three months since I started learning English at the Bristol English School."), ("그리고 현재 정말 이곳의 생활을 마음껏 즐기고 있습니다.", "And I am really enjoying life here to the fullest at present.")]
_ESM = [("문이 열려 있어요.", "The door is open."), ("그 사람은 병원에 입원해 있어요.", "He is in the hospital (admitted)."), ("교실에 학생들이 앉아 있어요.", "Students are seated in the classroom."), ("벽에 그림이 걸려 있어요.", "A picture is hanging on the wall.")]
L9 = lesson(
    "Ch 38 · Grammar C: the auxiliary verb –아/어 있다 (a state resulting from a completed action)",
    "-아/어 있다 · 앉아 있어요 · 열려 있어요 · 설치되어 있습니다 · -고 있다와 비교",
    requires=[],
    cards=[
        card("–고 있다 and –아/어 있다",
             "Compare the following two sentences and their meanings (the book shows a picture of Ms. Lee; the English is mine). In the first sentence, –고 있다 indicates that Ms. Lee is in the process of “sitting down” on the floor. In the second sentence, –아/어 있다 indicates that Ms. Lee is in the state of “sitting” on the floor. In other words, –아/어 있다 is used to indicate a condition or state resulting from a completed action.",
             examples=passage(_ES1)),
        card("Which verbs take –아/어 있다", "However, –아/어 있다 works only with a limited number of intransitive verbs (가다, 오다, 서다, 일어서다, 앉다, 눕다, 잠들다, 취하다, 입원하다, etc.) and with a limited number of transitive verbs in the passive voice (열리다, 닫히다, 잡히다, etc.). Intransitive verbs are those that do not take an object. For example (the English is the book’s):", examples=passage(_ES2)),
        card("Expressing a condition/state resulting from a completed action", "verb stem + 아/어 있다. More examples (the English is the book’s):", examples=passage(_ES3)),
        card("Follow-up 3 (Reading): a student’s website text",
             "The following excerpt is from a website in which a student talks about her student life at an English learning center in England. The book asks you to find and circle the –아/어 있다 phrases and to translate those sentences into English (the book glosses 연계되다: to be connected). The text is the book’s with “3개월” spelled out; the English is mine.",
             examples=passage(_BRI)),
        card("The –아/어 있다 sentences (mine)", "My answers:",
             tables=[table(["Sentence", "Meaning"], [["이 학교는 명문대 브리스톨대와 연계되어 있어서", "This school is connected with the prestigious University of Bristol, so"], ["다양한 문화 프로그램이 마련되어 있어요", "various cultural programs are prepared"], ["기숙사 각 방마다 전화 및 최고속 인터넷이 설치되어 있어서 편해요", "every dormitory room has a phone and top-speed Internet installed, so it is convenient"]], say=[0])]),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_ESM)),
        card("Activities left out", "Follow-up 1 (a PowerPoint speaking activity) and Follow-up 2 (watching a clip of the MBC America sitcom 거침없이 하이킥 and writing the sentences containing –아/어 있다) are computer and video activities."),
    ],
    exercises=uniq(
        _tr(_ES1 + _ES2 + _ES3 + _BRI + _ESM, k=3)
        + [M("What does –아/어 있다 indicate?", "A state resulting from a completed action", ["An action in progress", "A future plan", "A wish"], "The book’s note."), M("What does 앉고 있어요 mean?", "is sitting down (in process)", ["is seated (in the state)", "will sit", "wants to sit"], "–고 있다."), M("What does 앉아 있어요 mean?", "is seated (in the state)", ["is sitting down (in process)", "will sit", "sat down"], "–아/어 있다."), M("Which kind of verbs mostly take –아/어 있다?", "Some intransitive verbs and passive verbs", ["All transitive verbs", "Only adjectives", "Only nouns"], "The book’s note."), M("What does 차고 문이 열려 있어요 mean?", "The garage door is open", ["The garage door will open", "He opened the door", "The door is closed"], "The book’s example."),
           F("이 선생님이 바닥에 앉___ 있어요. (state)", "아", ["고", "서"], "앉아 있다."), F("창문이 닫혀 ___어요. (state)", "있", ["하", "말"], "닫혀 있다."), F("카메라가 설치되어 ___습니다. (state)", "있", ["하", "말"], "설치되어 있다."), F("형이 침대에 누워 ___어요. (state)", "있", ["하", "말"], "누워 있다."), F("친구가 지금 유럽에 가 ___어요. (state)", "있", ["하", "말"], "가 있다."),
           read_q("이 선생님이 바닥에 앉아 있어요"), read_q("차고 문이 열려 있어요"), read_q("형이 침대에 누워 있어요"), read_q("창문이 닫혀 있어요"), read_q("카메라가 설치되어 있습니다")]
    ),
)

# ================================================================== L10 Grammar -(으)ㄴ/는 한 and self-evaluation
_HAN1 = [("햄버거 같은 음식을 먹는 한 살을 뺄 수 없어요.", "As long as you eat food like hamburgers, you won’t lose weight."), ("내가 몬트레이에 있는 한 매일 등산 할 거예요.", "I will go hiking every day as long as I live in Monterey.")]
_HAN2 = [("한국에 사는 한 한국말을 배워야 해요.", "As long as I live in Korea, I must learn Korean."), ("친구들이 있는 한 외롭지 않아요.", "As long as there are friends, I am not lonely.")]
_HAN3 = [("할 수 있는 한 빨리 오세요.", "Please come as soon as possible."), ("가능한 한 천천히 운전하세요.", "Please drive as slowly as possible."), ("될 수 있는 한 적게 먹습니다.", "I eat as little as possible.")]
_HAN4 = [("패스트푸드를 많이 먹는 한 체중이 줄지 않을 거예요.", "As long as you eat a lot of fast food, your weight will not decrease."), ("저녁에 커피를 마시면 잠을 잘 못 자요.", "If I drink coffee in the evening, I can’t sleep well."), ("가능한 한 커피 대신 주스를 마시세요.", "Please drink juice instead of coffee as much as possible.")]
_HANM = [("한국에 있는 한 한국어로 말하겠어요.", "As long as I am in Korea, I will speak in Korean."), ("날씨가 좋은 한 매일 걷겠어요.", "As long as the weather is good, I will walk every day."), ("가능한 한 일찍 일어나세요.", "Please get up as early as possible.")]
L10 = lesson(
    "Ch 38 · Grammar D: “as long as”, –(으)ㄴ/는 한 · and self-evaluation",
    "-(으)ㄴ/는 한 · 먹는 한 · 있는 한 · 가능한 한 · 할 수 있는 한 · 자기 평가",
    requires=[],
    cards=[
        card("Expressing “as long as”",
             "In English, the phrase as long as is used to emphasize a condition, as in “We will win the game as long as we all stay together.” Likewise, in Korean, we use the conjunctive ending –(으)ㄴ/는 한 to emphasize a condition. For example (the English is the book’s):",
             examples=passage(_HAN1)),
        card("–는 한 and –(으)ㄴ 한", "–는 한 is attached to the stem of an action verb, including 있다 and 없다, whereas –(으)ㄴ 한 is attached to the stem of a stative verb. More examples (the English is the book’s):", examples=passage(_HAN2)),
        card("참고: expressing “as … as possible”", "When the expression 할 수 있는 한, 가능한 한, or 될 수 있는 한 is followed by an adverb or adjective, it means “as … as possible”. (The English is the book’s.)", examples=passage(_HAN3)),
        card("Follow-up 4 and 5 (the models)", "In Follow-up 4, Partner A reads a sentence strip, Partner B conjugates a verb with –는 한, and Partner A completes the sentence with a main clause. In Follow-up 5, you are given a card describing a concern and give advice with –(으)ㄴ/는 한 to three classmates. The book’s models (the English is mine):", examples=dlg([("A", "패스트푸드를 많이 먹다.", "Eat a lot of fast food."), ("B", "패스트푸드를 많이 먹는 한", "As long as you eat a lot of fast food,"), ("A", _HAN4[0][0], _HAN4[0][1]), ("학생", _HAN4[1][0], _HAN4[1][1]), ("학생", _HAN4[2][0], _HAN4[2][1])]) if False else passage(_HAN4)),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_HANM)),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with.\n\n"
             "Now I am able to: identify and discuss serious crimes such as murder, robbery, theft, sexual assault, violence, etc.; identify and describe physical appearance; identify instances of juvenile delinquency such as bullying and drug addiction; and identify shifting trends of crimes and discuss recent crimes such as ID theft and voice phishing scams.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; –는/(으)ㄴ 대로 and ~대로 (in accordance with; as); the auxiliary verb –고 말다; the auxiliary verb –아/어 있다; expressing “as long as” using –(으)ㄴ/는 한; and the Sino-Korean syllables within 폭력 (暴力), 강력 (强力), and 불법 (不法)."),
        card("Activities left out", "Follow-up 4 and 5 are partner activities with sentence strips and concern cards (the flip-chart presentation is left out)."),
    ],
    exercises=uniq(
        _tr(_HAN1 + _HAN2 + _HAN3 + _HAN4 + _HANM, k=3)
        + [M("What does –(으)ㄴ/는 한 express?", "as long as", ["because", "after", "although"], "The book’s note."), M("Which form attaches to action verbs including 있다 and 없다?", "–는 한", ["–(으)ㄴ 한", "–(으)ㄹ 한", "–던 한"], "The book’s note."), M("Which form attaches to stative verbs?", "–(으)ㄴ 한", ["–는 한", "–(으)ㄹ 한", "–던 한"], "The book’s note."), M("What does 가능한 한 천천히 mean?", "as slowly as possible", ["very slowly", "not slowly", "slower than before"], "The book’s 참고."), M("What does 한국에 사는 한 한국말을 배워야 해요 mean?", "As long as I live in Korea, I must learn Korean", ["Because I live in Korea, I learned Korean", "I don’t live in Korea", "I will move to Korea"], "The book’s example."),
           F("햄버거 같은 음식을 먹는 ___ 살을 뺄 수 없어요. (as long as)", "한", ["때", "채"], "–는 한."), F("친구들이 있는 ___ 외롭지 않아요. (as long as)", "한", ["때", "채"], "–는 한."), F("가능한 ___ 천천히 운전하세요. (as … as possible)", "한", ["때", "것"], "가능한 한."), F("할 수 있는 한 ___ 오세요. (as soon as possible)", "빨리", ["천천히", "늦게"], "빨리."), F("한국에 ___ 한 한국말을 배워야 해요. (live)", "사는", ["산", "살"], "사는 한."),
           read_q("햄버거 같은 음식을 먹는 한 살을 뺄 수 없어요"), read_q("친구들이 있는 한 외롭지 않아요"), read_q("가능한 한 천천히 운전하세요"), read_q("할 수 있는 한 빨리 오세요"), read_q("한국에 사는 한 한국말을 배워야 해요")]
    ),
)

# ================================================================== L11 core vocabulary
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/") and " " not in r[0]]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L11 = lesson(
    "Ch 38 · Core vocabulary",
    "주요 단어 · 범죄 · 강도 · 폭력 · 마약 · 사기 · 증거 · 수사",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank.\n\n"
             "The example sentences with digits are respelled in Hangul (3범 → 삼 범; 50명 → 오십 명; 30대 → 삼십 대; 50대 → 오십 대; 7살 → 일곱 살; 5만 원짜리 → 오만 원짜리; 10만 원짜리 → 십만 원짜리; CCTV → 씨씨티브이)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 용의자 mean?", "a suspect", ["a victim", "a witness", "a detective"], "容疑者."), M("What does 피해자 mean?", "a victim", ["a suspect", "a perpetrator", "a detective"], "被害者."), M("What does 가해자 mean?", "perpetrator; offender", ["victim", "witness", "detective"], "加害者."), M("What does 흉기 mean?", "a deadly weapon", ["a mask", "a badge", "a prison"], "凶器."), M("What does 위조 mean?", "fabrication; forgery", ["smuggling", "arson", "kidnapping"], "僞造."), M("What does 밀수 mean?", "smuggling", ["arson", "kidnapping", "forgery"], "密輸."), M("What does 방화 mean?", "arson; setting a fire", ["smuggling", "kidnapping", "theft"], "放火."), M("What does 납치 mean?", "abduction; kidnapping", ["arson", "smuggling", "theft"], "拉致."),
           F("경찰이 이번 살인 사건의 ___를 찾았습니다. (evidence)", "증거", ["혐의", "흉기"], "증거."), F("경찰이 40대 남자 살인 사건을 ___ 중입니다. (investigating)", "수사", ["설치", "사용"], "수사."), F("범인이 흉기로 편의점 직원을 ___. (stabbed)", "찔렀어요", ["털었어요", "놀렸어요"], "찌르다."), F("불량서클 아이들이 저를 ___. (tormented)", "괴롭혔어요", ["찔렀어요", "붙잡혔어요"], "괴롭히다."), F("마약에 한 번 ___되면 벗어나기가 어려워요. (addicted)", "중독", ["퇴학", "전학"], "중독."),
           read_q("주요 단어"), read_q("용의자"), read_q("피해자"), read_q("증거"), read_q("수사")]
    ),
)

UNIT = unit("Semester 2 · Unit 10 · Chapter 38: Crime (범죄)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11])

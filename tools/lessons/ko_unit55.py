"""Unit 55: KBC Semester 2, Unit 12, Chapter 48 - Social Issues II (사회 문제 2).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 12, Student's Edition (2022).
Audio, video, pictures, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 48 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("기미", "freckles; liver spots", "캘리포니아의 햇볕이 너무 강해서 기미가 많이 생겼어요."),
    ("꼽다/꼽히다", "to count; to point out/to be counted; to be pointed out", "설문조사의 응답자들은 플로리다 주와 워싱턴 주를 미국에서 가장 살기 좋은 곳으로 꼽았습니다."),
    ("당부", "(當付) a request; a favor; a solicitation (to request; to solicit) (~하다)", "김 선생님은 여행을 떠나기 전에 고양이를 잘 돌봐 달라고 친구에게 당부했습니다."),
    ("미백", "(美白) whitening; “beautiful white”", "여름철에는 피부 미백 효과가 있는 화장품이 많이 팔립니다."),
    ("미용", "(美容) beauty treatment; cosmetology", "이 잡지에는 미용에 대한 여러 가지 정보가 많이 들어 있습니다."),
    ("복부", "(腹部) the abdomen; the belly; “stomach part”", "복부에 있는 지방을 없애려면 걷기 운동을 꾸준히 해야 합니다."),
    ("복수", "(複數) multiple number; plural", "대학 입시에 복수 지원이 가능합니다."),
    ("부작용", "(副作用) (negative) side effects", "약을 먹기 전에 약의 부작용에 대해서 잘 읽어 봐야 합니다."),
    ("분쟁", "(紛爭) a dispute", "아파트에 사는 이웃과 분쟁이 일어나면 먼저 관리사무소에 연락합니다."),
    ("상체", "(上體) the upper part (of the body)", "성 일병은 체육관에 가면 상체운동을 많이 합니다."),
    ("성형(수술)", "(成形(手術)) plastic surgery; cosmetic surgery (to have plastic surgery) (~하다)", "제 동생은 코를 성형수술하고 싶어합니다."),
    ("쌍꺼풀", "a double eyelid", "휴가 동안 쌍꺼풀 수술을 했어요."),
    ("앞으로", "in the future; “forward on”", "정부는 앞으로 아이를 많이 낳는 가정을 지원할 계획이라고 합니다."),
    ("외모", "(外貌) outward appearance (of a person); external features; the exterior", "맞선을 본 사람이 똑똑하고 돈도 잘 버는데 외모가 마음에 안 듭니다."),
    ("원장", "(院長) the head of an organization whose name ends with 원 (院), as in 병원, 학원, and 연구원", "조 박사님은 오 년 전에 그 병원에 취직해서 삼 년 만에 원장이 되었습니다."),
    ("응답", "(應答) a response (to respond) (~하다)", "황 병장 집에 가서 문을 두드렸는데 아무런 응답이 없었습니다."),
    ("의료", "(醫療) medical treatment; medical service", "대부분의 의료사고는 의사가 진단을 잘 못 해서 일어난다고 합니다."),
    ("점", "(點) a mole; a birth mark; a spot; “point”", "코 옆에 있는 점을 제거하고 싶어서 피부과에 갔습니다."),
    ("주근깨", "freckles; fleck", "제 여자친구는 눈이 크고 머리가 길고 주근깨가 조금 있습니다."),
    ("주름(살)", "wrinkles; lines; crow’s feet; “wrinkled (flesh)”", "신 선생님은 연세가 예순이 넘으셨는데도 얼굴에 주름이 없으세요."),
    ("증명서", "(證明書) a certificate; “certification paper”", "대학에서 성적 증명서를 받으려면 우편이나 이메일로 신청하면 됩니다."),
    ("차례", "(次例) order (in sequence); a turn", "도착하신 차례대로 들어오시면 됩니다."),
    ("치아", "(齒牙) teeth", "제 할아버지는 연세는 많으시지만 아직도 치아가 건강하십니다."),
    ("하체", "(下體) the lower part (of the body)", "저는 하체가 상체에 비해 긴 편입니다."),
]
_CV_B = [
    ("가장", "(家長) head of household; “family chief”", "결혼해서 가장이 되면 해야 할 일이 너무 많아요."),
    ("감축", "(減縮) reduction; downsizing (to reduce; to downsize/to be reduced; to be downsized) (~하다/되다)", "회사 사정이 어려워져서 인원을 감축하기로 했습니다."),
    ("고용", "(雇用) employment (to employ/to be employed) (~하다/되다)", "인턴을 끝내자마자 직원으로 고용되었어요."),
    ("구조조정", "(構造調整) a restructuring; “structure adjustment”", "시티은행은 구조조정을 한다고 발표했습니다."),
    ("구직난", "(求職難) difficulty finding a job", "대학졸업자들이 구직난을 겪고 있습니다."),
    ("권유", "(勸諭) advice; persuasion (to give advice; to persuade/to be advised; to be persuaded) (~하다/받다)", "교수님께서 대학원에 진학하는 것을 권유하셨어요."),
    ("급여", "(給與) pay; salary; wages", "미국에서는 보통 이 주에 한 번 급여를 받지만, 한국에서는 보통 한 달에 한 번 받습니다."),
    ("동향", "(動向) a tendency; a trend; a movement", "상반기의 취업률 동향을 보면 하반기에는 취업률이 상승할 것 같습니다."),
    ("명예퇴직", "(名譽退職) a voluntary resignation; “honorary retirement”", "많은 기업에서 경비를 줄이기 위해 명예퇴직을 권유합니다."),
    ("분석", "(分析) an analysis (to analyze/to be analyzed) (~하다/되다)", "분석 결과 강물이 심하게 오염된 것으로 나타났습니다."),
    ("불경기", "(不景氣) an (economic) recession; “no business”", "불경기여서 자동차 판매량이 줄었습니다."),
    ("소문", "(所聞) a rumor; gossip; news", "이 음식점 손님의 대부분은 소문을 듣고 오는 사람들입니다."),
    ("실업자", "(失業者) an unemployed person; “person who lost work”", "불경기 때문에 실업자 수가 점점 늘어나고 있어요."),
    ("실직", "(失職) losing a job/employment (to lose a job) (~하다)", "다니던 백화점이 갑자기 문을 닫는 바람에 실직했습니다."),
    ("여건", "(與件) a given condition; circumstances", "창업을 하고 싶지만 돈도 없고 여건이 안 돼요."),
    ("영업", "(營業) business; trade; a (business) operation (to run a business) (~하다)", "저희 식당의 영업시간은 주중에는 오전 일곱 시부터 오후 아홉 시까지입니다."),
    ("~ 이하", "(以下) ~ and below", "이 연극공연은 십팔 세 이하는 관람할 수 없습니다."),
    ("인력", "(人力) manpower; human resources", "대기업과는 달리 많은 중소기업에서 인력난을 겪고 있습니다."),
    ("청년", "(靑年) a youth; a young man; “green year”", "저 청년은 아주 부지런하네요."),
    ("추진", "(推進) propulsion; drive (to propel; to drive/to be propelled; to be driven) (~하다/되다)", "우리 회사에서도 주 오 일 근무제를 추진할 계획입니다."),
    ("침체", "(沈滯) stagnation; dullness; slackness (to become stagnant) (~되다)", "경기 침체로 일자리 구하기가 어려워요."),
    ("폐업", "(閉業) discontinuance (of business); going out of business (to close a business; to go out of business) (~하다)", "이 가게는 영업이 잘 안 돼서 한 달 전에 폐업했습니다."),
    ("해고", "(解雇) layoff; termination (to lay off; to fire/to be laid off; to be fired) (~하다/되다)", "회사 경영이 어려워서 사원 열 명을 해고했습니다."),
]
_CV_C = [
    ("강화", "(强化) consolidation; reinforcement (to consolidate/to be reinforced; to be strengthened) (~하다/되다)", "건물의 경비를 강화했어요."),
    ("기피", "(忌避) avoidance; evasion (to avoid; to evade) (~하다)", "요즘 젊은이들은 힘든 직업을 기피합니다."),
    ("당연하다", "(當然) to be natural; to be reasonable", "국민으로서 군대에 가는 것은 당연합니다."),
    ("도입", "(導入) an introduction; an adoption (to introduce; to adopt/to be introduced; to be adopted) (~하다/되다)", "몇 년 전부터 쓰레기 종량제가 도입됐어요."),
    ("면제", "(免除) an exemption (to exempt/to be exempted) (~하다/받다)", "저는 건강 문제 때문에 군대를 면제받았어요."),
    ("모병", "(募兵) recruiting soldiers (to recruit soldiers) (~하다)", "전쟁을 위해서 모병을 하기로 했습니다."),
    ("병무청", "(兵務廳) Military Manpower Administration", "병무청에서 신체검사를 받았습니다."),
    ("병역", "(兵役) military service", "병역을 마친 후에 다시 복학했습니다."),
    ("보상", "(報償) compensation (to compensate/to be compensated) (~하다/받다)", "국가에서 재해 피해를 보상해 줄 예정입니다."),
    ("비리", "(非理) corruption", "장관이 비리 혐의로 구속됐습니다."),
    ("속이다", "to deceive; to cheat", "가격을 속인 백화점이 조사를 받고 있습니다."),
    ("안보", "(安保) national security", "안보에 관련된 문제로 대통령이 회의를 열었습니다."),
    ("적발", "(摘發) disclosure (of a crime, fault, etc.); exposure (to disclose/to be disclosed) (~하다/되다)", "공장에서 폐수를 몰래 버리다 적발됐습니다."),
    ("정신", "(精神) mental(ity); consciousness; mental (condition)", "그 학생은 입시에 대한 스트레스로 정신병원에 입원했습니다."),
    ("조작", "(造作) fabrication (to fabricate; to doctor/to be fabricated; to be doctored) (~하다/되다)", "여권을 조작한 여행객이 경찰에 체포됐습니다."),
    ("지키다", "to guard; to defend; to keep", "경찰들이 중요한 건물을 지키고 있습니다."),
    ("징병(제)", "(徵兵(制)) conscription (system); mandatory military service (system)", "한국은 징병제를 실시하고 있습니다."),
    ("처벌", "(處罰) punishment (to punish/to be punished) (~하다/받다)", "가짜 진단서를 이용해 군대를 가지 않은 사람이 처벌받았습니다."),
    ("철저히", "(徹底) thoroughly", "경찰이 이번 사건을 철저히 조사하고 있습니다."),
    ("허위", "(虛僞) falsehood; untruth", "이력서를 허위로 작성한 신입사원이 해고됐습니다."),
]
_CV_GR = [
    ("–(으)ㄹ까 봐(서)", "for fear of; (being) afraid of (see Grammar in Focus)", "빙판길에 사고가 날까 봐 천천히 운전했어요."),
]
_CV_SINO = [("성형수술", "(成形手術) plastic surgery; cosmetic surgery", "성장, 성인, 완성, 원형, 체형, 변형, 악수, 수건, 수동, 기술, 예술, 화술"), ("실직", "(失職) unemployment; loss of job", "실업률, 실망, 실점, 직원, 직장, 취직"), ("안보", "(安保) (national) security", "안심, 불안, 편안, 보호, 보험, 보온")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"성형수술": "plastic surgery", "성형": "plastic surgery", "주름": "wrinkles", "징병": "conscription", "실업률": "unemployment rate", "병역의무": "military service duty", "국가안보": "national security", "경기침체": "economic stagnation", "실업급여": "unemployment benefits", "모병제": "volunteer military system", "대체복무": "alternative service", "병역비리": "military service corruption", "일자리": "a job; a position", "청년": "a youth", "단임": "a single term"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"


def _words(keys):
    pl = _PLAIN(keys)
    out = [ktable(_rows(pl))]
    rest = [k for k in keys if k not in pl]
    if rest:
        out.append(table(["Word", "Meaning"], [[k, _en(k)] for k in rest]))
    return out


# ---- Sino-Korean notes
_S1G = [("성인", "an adult; “achieved person”"), ("성적", "a result; a record; “accomplished work”"), ("신형", "new style; new model"), ("서구형", "Western style"), ("수공", "handicraft; handwork"), ("수족", "limbs; “hands and feet”"), ("미술", "fine arts; “beautiful skill”")]
_S1 = [("성장", "growth"), ("악수", "a handshake"), ("성공", "success"), ("수건", "a towel"), ("완성", "completion"), ("수동", "manual operation"), ("원형", "a circle; a round shape"), ("기술", "a technique; a skill"), ("삼각형", "a triangle"), ("예술", "art"), ("화술", "the art of speaking")]
_S2G = [("실례", "rudeness; impoliteness; “loss of etiquette”"), ("실수", "a mistake; an error; loss of control; “loss of a hand/grip”"), ("이직", "transfer of a job"), ("직업", "an occupation; a calling; a vocation; “position work”")]
_S2 = [("실업률", "the unemployment rate"), ("실망", "disappointment"), ("실점", "loss of a point"), ("직원", "an employee"), ("직장", "a workplace"), ("취직", "getting a job")]
_S3G = [("안녕하다", "to be fine; “to be serene and comfortable”")]
_S3 = [("안심", "peace of mind; relief"), ("불안", "anxiety; unease"), ("편안", "comfort; ease"), ("보호", "protection"), ("보온", "keeping warm"), ("보험", "insurance")]

L1 = lesson(
    "Ch 48 · What the chapter teaches, 성형수술 · 실직 · 안보",
    "사회 문제 · 성형수술 · 실직 · 안보 · 成形手術 · 失職 · 安保 · 불규칙 동사 · 까 봐",
    requires=[],
    cards=[
        card("What Chapter 48 teaches (사회 문제 2)",
             "Chapter 48, “Social Issues II”, has a vocabulary builder, three topic presentations (a survey on cosmetic surgery, a recession and unemployment, the duty of military service) with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify, talk about, and express opinions about issues and incidents concerning cosmetic surgery and its popularity in Korea; identify and talk about the issues related to employment, unemployment, layoffs, downsizing, and restructuring; and identify and discuss issues concerning military service in Korea.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; the conjunctive ending –(으)ㄹ까 봐(서) (being afraid/aware that [something] might …); a summary of irregular verbs; and the Sino-Korean syllables within 성형수술 (成形手術), 실직 (失職), and 안보 (安保)."),
        card("Sino-Korean in use: 성형수술 (成形手術)",
             "This Sino-Korean word means plastic surgery or cosmetic surgery. The first syllable 성 (成) means achieve, accomplish, or make, as in 성인 (an adult; “achieved person”) and 성적 (a result; a record; “accomplished work”). The second syllable 형 (形) means shape, form, or style, as in 신형 (new style; new model) and 서구형 (Western style). 수 (手) means hand or manual, as in 수공 (handicraft; handwork) and 수족 (limbs: “hands and feet”). The last syllable 술 (術) means skill or artifice, as in 미술 (fine arts; “beautiful skill”). Thus the literal meaning of 성형수술 is “shape-making hand skill.” The book asks you to guess 성장, 악수, 성공, 수건, 완성, 수동, 원형, 기술, 삼각형, 예술 and 화술 (the book prints 원형 twice; it glosses 완 [完]: complete, 원 [圓]: round and 건 [巾]: a towel; my answers):",
             tables=[ktable(_S1G), ktable(_S1)]),
        card("Sino-Korean in use: 실직 (失職)",
             "The first syllable 실 (失) means lose or loss, as in 실례 (rudeness; impoliteness; “loss of etiquette”) and 실수 (a mistake; an error; loss of control; “loss of a hand/grip”). The second syllable 직 (職) means job or position, as in 이직 (transfer of a job) and 직업 (an occupation; a calling; a vocation; “position work”). Thus, 실직 means unemployment or loss of one’s employment. The book asks you to guess 실업률, 실망, 실점, 직원, 직장 and 취직 (the book glosses 망 [望]: hope, aspiration and 점 [點]: a point; my answers):",
             tables=[ktable(_S2G), ktable(_S2)]),
        card("Sino-Korean in use: 안보 (安保)",
             "The first syllable 안 (安), which you learned in Chapter 44, means serene, tranquil, or comfort, as in 안녕하다 (to be fine; “to be serene and comfortable”). The second syllable 보 (保) means keep or preserve. Thus, the literal meaning of 안보 is “keep serenity” or “preserve tranquility,” and the word means national security. The book asks you to guess 안심, 불안, 편안, 보호, 보온 and 보험 (my answers):",
             tables=[ktable(_S3G), ktable(_S3)]),
    ],
    exercises=uniq(
        _tr(_S1G + _S1 + _S2G + _S2 + _S3G + _S3, k=3)
        + [M("What does 성 (成) mean?", "achieve; accomplish; make", ["lose", "keep", "hand"], "성인."), M("What does 형 (形) mean?", "shape; form; style", ["hand", "skill", "lose"], "신형."), M("What does 수 (手) mean?", "hand; manual", ["shape", "skill", "job"], "수공."), M("What does 술 (術) mean?", "skill; artifice", ["hand", "shape", "keep"], "미술."), M("What does 실 (失) mean?", "lose; loss", ["keep", "job", "achieve"], "실례."), M("What does 직 (職) mean?", "job; position", ["lose", "keep", "shape"], "직업."), M("What does 안 (安) mean?", "serene; tranquil; comfort", ["lose", "job", "hand"], "안녕."), M("What does 보 (保) mean?", "keep; preserve", ["lose", "serene", "shape"], "보호."), M("What is the literal meaning of 성형수술?", "“shape-making hand skill”", ["“keep serenity”", "“losing a position”", "“beautiful skill”"], "성 + 형 + 수 + 술."), M("What is the literal meaning of 안보?", "“keep serenity” or “preserve tranquility”", ["“shape-making hand skill”", "“loss of position”", "“family chief”"], "안 + 보."), M("What does 실직 mean?", "unemployment; loss of one’s employment", ["a plastic surgery", "national security", "a layoff plan"], "실 + 직."), M("What does 안보 mean?", "national security", ["unemployment", "plastic surgery", "a military draft"], "安保."),
           F("___인은 다 자란 사람을 말합니다. (成)", "성", ["실", "안"], "성인."), F("___업률은 일자리가 없는 사람의 비율입니다. (失)", "실", ["성", "보"], "실업률."), F("___심은 마음이 편한 것입니다. (安)", "안", ["실", "성"], "안심."), F("___험은 사고를 대비해 드는 것입니다. (保)", "보", ["실", "성"], "보험."), F("미___은 아름다운 기술입니다. (術)", "술", ["수", "형"], "미술."),
           read_q("성형수술"), read_q("실직"), read_q("안보"), read_q("직장"), read_q("보험")]
    ),
)

# ================================================================== L2 Vocabulary builder
_BOX = [("병역", "military service"), ("실직", "losing a job"), ("점", "a mole; a spot"), ("실업률", "the unemployment rate"), ("기미", "freckles; liver spots"), ("해고", "layoff; termination"), ("구직난", "difficulty finding a job"), ("안보", "national security"), ("폐업", "going out of business"), ("하체", "the lower part of the body"), ("모병", "recruiting soldiers"), ("주근깨", "freckles; fleck"), ("쌍꺼풀", "a double eyelid"), ("징병", "conscription"), ("주름", "wrinkles; lines"), ("병무청", "Military Manpower Administration"), ("고용", "employment"), ("불경기", "an economic recession"), ("상체", "the upper part of the body")]
_JOB = ["실직", "실업률", "해고", "구직난", "폐업", "고용", "불경기"]
_BODY = ["점", "기미", "하체", "주근깨", "쌍꺼풀", "주름", "상체"]
_MIL = ["병역", "안보", "모병", "징병", "병무청"]
_PFX = [("무~ (無)", "no; not; without; a-", "무소식, 무경험, 무관심, 무신경, 무의식"), ("불/부~ (不)", "no; not; non-; im-; il-; in-", "불합격, 불가능, 불친절, 불만족, 불경기, 부주의, 부동산, 부작용"), ("비~ (非)", "no; not; wrong; ab-", "비정상, 비공식, 비인간적, 비상구"), ("신~ (新)", "new", "신상품, 신제품, 신세대, 신기록"), ("구~ (舊)", "old", "구시대, 구세대, 구형, 구소련, 구정, 구식"), ("장~ (長)", "long; superior", "장거리, 장기간, 장점"), ("단~ (短)", "short; inferior", "단거리, 단기간, 단점"), ("외~ (外)", "exterior; out(side); mother’s side (relatives)", "외국, 외모, 외사촌, 외삼촌, 외숙모, 외할아버지, 외할머니"), ("재~ (再)", "re-; again", "재검사, 재시험, 재방송, 재확인, 재활용, 재평가")]
_SFX = [("~감 (感)", "feeling; sense", "자신감, 거리감, 행복감"), ("~간 (間)", "between; relationship", "부자간, 형제간, 친구간, 며칠간"), ("~력 (力)", "power; ability", "노동력, 경쟁력, 기억력, 생활력, 생산력, 잠재력"), ("~비 (費)", "expenses; cost", "숙박비, 관리비, 호텔비, 차비"), ("~청 (廳)", "government office", "병무청, 환경청, 교육청, 통계청"), ("~성 (性)", "(having) characteristics of", "수익성, 생산성, 국민성, 전염성"), ("~실 (室)", "a room; a chamber", "회의실, 일반실, 응급실, 사무실, 화장실, 미용실"), ("~인 (人)", "a person", "외국인, 장애인, 대변인, 일본인, 중국인"), ("~자 (者)", "a person", "보호자, 초보자, 보행자, 목격자, 피해자, 구직자"), ("~증 (證)", "a certificate; a license", "자격증, 신분증, 학생증, 운전면허증"), ("~적 (的)", "-ic(al); -ive", "인상적, 세계적, 역사적, 공식적, 감동적, 기본적, 열광적, 체계적, 안정적, 현실적, 장기적, 단기적, 긍정적, 부정적, 일반적, 남성적, 여성적, 정치적, 경제적, 사회적, 문화적"), ("~회 (會)", "a gathering; a meeting; a convention; a party", "학생회, 박람회, 음악회, 전시회, 동창회")]
_ACT3 = [("경제 상황이 좋지 않은 것을 말합니다. 이렇게 경제가 나쁘면 식당이나 가게가 잘 운영되지 않습니다.", "It means that the economic situation is not good. When the economy is bad like this, restaurants and shops do not operate well.", "d. 불경기"), ("군대에 가야 하는 것을 말합니다. 대한민국 남자는 반드시 군대에 가야 합니다.", "It means having to go to the army. Men in the Republic of Korea must go to the army.", "b. 병역의무"), ("나라의 안전을 지키는 것과 같은 말입니다. 우리나라 경찰과 군인들은 국민 모두의 안전을 위해 열심히 일하고 있습니다.", "It is the same as protecting the safety of the nation. Our country’s police and soldiers are working hard for the safety of all the people.", "c. 국가안보"), ("일자리 찾는 것이 어려움을 뜻합니다. 이것이 심해서 대학을 졸업해도 취직을 하기가 어렵습니다.", "It means that finding a job is difficult. It is so severe that even after graduating from university it is hard to get a job.", "a. 구직난"), ("군대 관련 업무를 담당하는 국가정부기관입니다. 징병검사나 모병에 관계된 일도 합니다.", "It is the national government organization in charge of military-related work. It also does work related to conscription examinations and recruitment.", "e. 병무청")]
L2 = lesson(
    "Ch 48 · Vocabulary Builder: jobs, bodies and the military; prefixes and suffixes",
    "병역 · 실직 · 점 · 실업률 · 기미 · 해고 · 구직난 · 안보 · 폐업 · 하체 · 모병 · 주근깨 · 쌍꺼풀 · 징병 · 주름 · 병무청 · 고용 · 불경기 · 상체",
    requires=[],
    cards=[
        card("새 단어 a: the words in the box",
             "Skim the words in the box and circle the words you do not know, then write the English meanings next to them (the book lets you use a dictionary). The book’s nineteen words with the meanings from the Core Vocabulary of the chapter (실업률 is my gloss; the book does not list it):",
             tables=[ktable(_BOX)]),
        card("새 단어 b: three categories (mine)",
             "Group the words in the box into the three categories Job-Related, Body-Related and Military-Related. My grouping:",
             tables=[table(["Job-related words", "Body-related words", "Military-related words"], [[", ".join(_JOB), ", ".join(_BODY), ", ".join(_MIL)]], say=[0, 1, 2])]),
        card("Vocabulary Learning Strategy: expand vocabulary using Sino-Korean prefixes and suffixes",
             "Sino-Korean syllables can function as a prefix or suffix when combined with words. They add to or modify the meaning of the words. For example, the Sino-Korean syllable 불/부 (不) can function as a prefix and adds the meaning of not, no, non-, im-, in-, or il-, as in 불가능 (impossibility), 부정확 (inaccuracy), and 부자연 (unnaturalness). When you know the meaning of the prefix, you can easily guess that these words imply something negative, even if you are unsure of the meaning of the words. The following tables list some common Sino-Korean syllables that can function as prefixes or suffixes. You can visit 국립국어원 if you want to learn more about Korean prefixes and suffixes.",
             tables=[table(["Prefix", "Meaning", "Examples"], [list(r) for r in _PFX], say=[2]), table(["Suffix", "Meaning", "Examples"], [list(r) for r in _SFX], say=[2])]),
        card("학습활동 3 (a): which word is described?",
             "The following sentences describe the words in the box (a. 구직난 b. 병역의무 c. 국가안보 d. 불경기 e. 병무청). The book asks you to write the letter of the correct word before each sentence. The sentences are the book’s; the English and the answers are mine.",
             tables=[table(["Sentence", "Answer (mine)"], [[a, c] for a, b, c in _ACT3], say=[0]), table(["English of the sentence (mine)"], [[b] for a, b, c in _ACT3])]),
        card("Activities left out", "Activities 1 and 4 (SMART Board), Activity 2 (a pair task: Partner A reads a word from Set A aloud and Partner B says its antonym and English meaning, then they switch; the sets are not printed in the student text), Activity 3 b (listening to recordings about Junghee’s family and drawing on faces what the speaker describes), the PowerPoint Sino-Korean presentation and Activity 5 (the related-words game: two teams take turns saying words related to a topic such as 교통 [비행기, 지하철, 고속도로, 기차] within three seconds, one point per word) are audio, computer, pair and game activities."),
    ],
    exercises=uniq(
        _tr(_BOX, k=3) + _tr([(a, b) for a, b, c in _ACT3], k=3)
        + [M("Which group does 해고 belong to?", "Job-related", ["Body-related", "Military-related", "None"], "해고."), M("Which group does 쌍꺼풀 belong to?", "Body-related", ["Job-related", "Military-related", "None"], "쌍꺼풀."), M("Which group does 징병 belong to?", "Military-related", ["Job-related", "Body-related", "None"], "징병."), M("Which group does 구직난 belong to?", "Job-related", ["Body-related", "Military-related", "None"], "구직난."), M("Which group does 병무청 belong to?", "Military-related", ["Job-related", "Body-related", "None"], "병무청."), M("Which group does 주름 belong to?", "Body-related", ["Job-related", "Military-related", "None"], "주름."), M("What does the prefix 불/부~ (不) add?", "not; no; non-; im-; il-; in-", ["new", "old", "again"], "불가능."), M("What does the prefix 신~ (新) mean?", "new", ["old", "again", "not"], "신제품."), M("What does the prefix 구~ (舊) mean?", "old", ["new", "again", "short"], "구시대."), M("What does the prefix 재~ (再) mean?", "re-; again", ["new", "old", "not"], "재시험."), M("What does the suffix ~력 (力) mean?", "power; ability", ["expenses", "a person", "a room"], "경쟁력."), M("What does the suffix ~비 (費) mean?", "expenses; cost", ["power", "a person", "a certificate"], "숙박비."), M("What does the suffix ~청 (廳) mean?", "government office", ["a room", "a gathering", "feeling"], "병무청."), M("What does the suffix ~실 (室) mean?", "a room; a chamber", ["a person", "a gathering", "expenses"], "회의실."), M("What does the suffix ~자 (者) mean?", "a person", ["a room", "a license", "power"], "구직자."), M("What does the suffix ~증 (證) mean?", "a certificate; a license", ["a person", "a room", "power"], "학생증."), M("What does the suffix ~회 (會) mean?", "a gathering; a meeting; a party", ["expenses", "a person", "feeling"], "동창회."), M("What does the suffix ~감 (感) mean?", "feeling; sense", ["power", "expenses", "a person"], "자신감."),
           F("경제 상황이 좋지 않은 것을 ___라고 합니다. (recession)", "불경기", ["구직난", "병역"], "불경기."), F("일자리 찾기가 어려운 것을 ___이라고 합니다. (difficulty finding a job)", "구직난", ["불경기", "안보"], "구직난."), F("대한민국 남자는 반드시 ___의무를 다해야 합니다. (military service)", "병역", ["고용", "폐업"], "병역."), F("나라의 안전을 지키는 것은 국가___입니다. (security)", "안보", ["병무청", "실직"], "안보."), F("병무청은 징병검사와 ___에 관계된 일도 합니다. (recruiting soldiers)", "모병", ["해고", "폐업"], "모병."),
           read_q("병역"), read_q("불경기"), read_q("구직난"), read_q("국가안보"), read_q("병무청")]
    ),
)


# ================================================================== L3 Topic A
_A_TXT = [
    ("성인 여성 열 명 가운데 다섯 명은 미용 성형수술을 받은 적이 있으며, 칠십 퍼센트 가까운 여성들이 외모 때문에 스트레스를 받고 있다는 설문조사 결과가 나왔다.", "A survey result came out that five out of ten adult women have had cosmetic plastic surgery and that nearly 70 percent of women are stressed because of their appearance."),
    ("지난해 구 월 서울, 경기지역의 십팔 세 이상 여성 팔백십 명을 대상으로 조사한 결과 사십칠 점 삼 퍼센트인 삼백팔십삼 명이 미용성형수술을 받은 경험이 있다고 답했다.", "As a result of a survey last September of 810 women aged 18 or over in the Seoul and Gyeonggi area, 383 women, or 47.3 percent, answered that they had experience of cosmetic plastic surgery."),
    ("특히 이십오 세에서 이십구 세 여성의 경우 설문에 답한 백삼십 명 가운데 팔십 명(육십일 점 오 퍼센트)이 수술을 받은 것으로 나타났다.", "In particular, among women aged 25 to 29, 80 of the 130 who answered the survey (61.5 percent) turned out to have had surgery."),
    ("실제 성형한 신체 부위(복수 응답)로는 쌍꺼풀(사십삼 점 삼 퍼센트)과 점, 기미, 주근깨 제거(삼십육 점 영 퍼센트)가 많았으며, 앞으로 하고 싶은 수술은 점, 기미, 주근깨 제거(삼십육 점 사 퍼센트), 치아 미백(이십구 점 구 퍼센트), 코 높임(이십구 점 오 퍼센트) 등의 차례였다.", "As the body parts actually altered (multiple answers allowed), double eyelids (43.3 percent) and removal of moles, liver spots and freckles (36.0 percent) were many, and the surgeries they want to have in the future were, in order, removal of moles, liver spots and freckles (36.4 percent), teeth whitening (29.9 percent), nose heightening (29.5 percent) and so on."),
    ("또한 설문에 답한 여성 가운데 육십구 점 구 퍼센트가 외모 때문에 스트레스를 받는다고 했으며 이들 가운데 오십 점 팔 퍼센트가 미용성형수술을 받은 것으로 나타났다.", "Also, 69.9 percent of the women who answered the survey said they are stressed because of their appearance, and 50.8 percent of these turned out to have had cosmetic plastic surgery."),
    ("자신의 신체 가운데 가장 만족하는 부분(복수 응답)으로는 얼굴(십육 점 일 퍼센트)과 피부(십사 점 육 퍼센트)를 꼽았고, 가장 불만인 부분은 하체(십칠 점 일 퍼센트)와 복부(십사 점 육 퍼센트) 등이었다.", "As the part of their own body they are most satisfied with (multiple answers allowed), they picked the face (16.1 percent) and the skin (14.6 percent), and the parts they are most dissatisfied with were the lower body (17.1 percent), the abdomen (14.6 percent) and so on."),
]
_A_WORDS = ["기미", "꼽다/꼽히다", "당부", "미백", "미용", "복부", "복수", "부작용", "분쟁", "상체", "성형(수술)", "쌍꺼풀", "앞으로", "외모", "원장", "응답", "의료", "점", "주근깨", "주름(살)", "증명서", "차례", "치아", "하체"]
_A_STAT = [("Adult women who have had cosmetic plastic surgery", "5 out of 10 (47.3%, 383 of 810 women aged 18 or over in the Seoul and Gyeonggi area)"), ("Women aged 25 to 29 who have had surgery", "80 of 130 (61.5%)"), ("Women stressed because of their appearance", "69.9% (of whom 50.8% have had surgery)"), ("Parts actually altered", "double eyelids 43.3%; removal of moles, liver spots and freckles 36.0%"), ("Surgery they want in the future", "removal of moles, liver spots and freckles 36.4%; teeth whitening 29.9%; nose heightening 29.5%"), ("Most satisfying body parts", "face 16.1%; skin 14.6%"), ("Most dissatisfying body parts", "lower body 17.1%; abdomen 14.6%")]
L3 = lesson(
    "Ch 48 · Topic A: a survey on cosmetic surgery (성형수술에 대한 설문 조사)",
    "성형수술에 대한 설문 조사 · 미용 성형수술 · 외모 · 스트레스 · 쌍꺼풀 · 점 · 기미 · 주근깨 · 치아 미백 · 하체 · 복부",
    requires=[],
    cards=[
        card("Topic A: a survey on cosmetic surgery (성형수술에 대한 설문 조사)",
             "The following excerpt presents survey results about cosmetic surgery in Korea (한겨레). (The English is mine; the book gives none. The text is the book’s with the numbers spelled out: 10명 가운데 5명 is 열 명 가운데 다섯 명, 70% is 칠십 퍼센트, 810명 is 팔백십 명, 47.3% is 사십칠 점 삼 퍼센트, and so on; the dots between 서울 and 경기 and between 점, 기미 and 주근깨 are written as commas; the quotation marks are removed.)",
             examples=passage(_A_TXT)),
        card("The survey results at a glance (mine)", "", tables=[table(["Item", "Result"], [list(r) for r in _A_STAT])]),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_A_WORDS)),
        card("한국에서는: cosmetic surgery in Korea",
             "Cosmetic surgical procedures (성형수술) have witnessed a significant increase in recent years in the United States, with the American Society of Plastic Surgeons (ASPS) reporting over 1.5 million such procedures in 2020 alone. Cosmetic surgery is also popular in South Korea. Many Koreans, particularly among young adults, opt for cosmetic surgery as a means to enhance their appearance. In the 1950s and 1960s, when surgical skills and technology were rudimentary, cosmetic surgery in Korea was mainly limited to double eyelid surgery (쌍꺼풀 수술), which helps make the eyes look larger. As surgical skills and technology improved, surgical alteration of the nose and cheekbones became commonplace. These days, various other surgeries for the body and face are popular, partially influenced by entertainers who have enhanced their appearance through cosmetic surgery. In the job market, attractiveness has become an advantage for applicants. This fact accounts for the increase in cosmetic surgery among men, although women still make up the majority of people choosing cosmetic surgery. Korean plastic surgeons are highly skilled and many foreigners, especially Asians, visit Korea to have cosmetic surgery performed. Some well-known clinics have opened branches in China to accommodate the increasing number of Chinese patients."),
        card("Activities left out", "Presentation steps a (brainstorming words related to 미용성형수술 and jotting them down in Korean), b and d (a SMART Board activity and checking your guesses against the topic), c (reading and listening) and e (review with the teacher) are audio, computer and group activities. The Sino-Korean word 성형수술 (成形手術) is in the first lesson of the chapter."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT, k=3)
        + [M("How many out of ten adult women have had cosmetic surgery?", "Five", ["One", "Nine", "Three"], "열 명 가운데 다섯 명."), M("What are nearly 70 percent of women stressed about?", "Their appearance", ["Their jobs", "Their health", "Their families"], "외모."), M("How many women were surveyed?", "810", ["383", "130", "80"], "팔백십 명."), M("What percent of those surveyed had had surgery?", "47.3 percent", ["61.5 percent", "69.9 percent", "36.0 percent"], "사십칠 점 삼 퍼센트."), M("Among women aged 25 to 29, how many of the 130 had had surgery?", "80", ["383", "810", "50"], "팔십 명."), M("Which surgery was most common among those who had actually had surgery?", "Double eyelid surgery", ["Nose heightening", "Teeth whitening", "Breast surgery"], "쌍꺼풀 사십삼 점 삼 퍼센트."), M("Which surgery do they most want in the future?", "Removal of moles, liver spots and freckles", ["Double eyelid surgery", "Nose heightening", "Teeth whitening"], "삼십육 점 사 퍼센트."), M("What did they say they are most satisfied with?", "The face", ["The lower body", "The abdomen", "The hair"], "얼굴."), M("What did they say they are most dissatisfied with?", "The lower body", ["The face", "The skin", "The teeth"], "하체."), M("What was Korean cosmetic surgery mainly limited to in the 1950s and 1960s?", "Double eyelid surgery", ["Nose surgery", "Cheekbone surgery", "Chin surgery"], "The book’s note."),
           F("성인 여성 열 명 가운데 다섯 명이 미용 ___을 받은 적이 있다. (cosmetic surgery)", "성형수술", ["입시", "송금"], "성형수술."), F("여성들이 ___ 때문에 스트레스를 받고 있다. (appearance)", "외모", ["여건", "소문"], "외모."), F("신체 부위로는 ___(복수 응답)이 가장 많았다. (a double eyelid)", "쌍꺼풀", ["주름", "치아"], "쌍꺼풀."), F("가장 불만인 부분은 ___와 복부 등이었다. (the lower body)", "하체", ["상체", "얼굴"], "하체."), F("앞으로 하고 싶은 수술은 ___ 제거가 가장 많았다. (moles; spots)", "점", ["치아", "복부"], "점."),
           read_q("성형수술에 대한 설문 조사"), read_q("여성들이 외모 때문에 스트레스를 받고 있습니다"), read_q("쌍꺼풀 수술을 한 여성이 많았습니다"), read_q("가장 불만인 부분은 하체입니다"), read_q("앞으로 하고 싶은 수술은 점과 기미와 주근깨 제거입니다")]
    ),
)

# ================================================================== L4 Follow-ups A
_NY = [
    ("비교적 긴 설 연휴를 이용해 올 상반기 기업 공채 등에 대비해 성형수술을 하려는 취업준비족들이 늘고 있다.", "Job-preparation “tribes” who want to have cosmetic surgery to prepare for this year’s first-half corporate open recruitment, making use of the relatively long Lunar New Year holiday, are increasing."),
    ("취업준비생 김 아무개(스물여섯 살, 여) 씨는 이번 설에 고향에 가지 않고 쌍꺼풀 수술을 하기로 했다.", "Ms. Kim, 26, a job preparer, decided not to go to her hometown this New Year and to have double eyelid surgery."),
    ("김 씨는 다니던 회사 사정이 어려워져 다음 달 퇴사가 결정됐다며 부모님께서도 귀성보다는 취직이 먼저라며 이해해 주셨다고 말했다.", "Ms. Kim said that, because the situation at the company she had been working for became difficult, her leaving next month has been decided, and that her parents also understood, saying getting a job comes before going home for the holiday."),
    ("일부 성형외과들은 취업 사이트 등과 연계해 설맞이 특별 상품을 내놓기도 했다.", "Some plastic surgery clinics have even come out with special New Year products in connection with job sites and the like."),
    ("단체로 수술을 받으면 큰 폭으로 깎아 주거나, 지방에서 올라오는 이들한테 숙소를 제공하는 곳도 있다.", "Some places give a large discount if you have surgery as a group, or provide lodging to those who come up from the provinces."),
]
_CHN = [
    ("중국 여성들 사이에서 해외 성형수술이 유행하면서 중국 당국에 새로운 고민이 생겼다.", "As cosmetic surgery abroad has become popular among Chinese women, a new worry has arisen for the Chinese authorities."),
    ("여권 사진 속 모습과 입국 때의 실제 얼굴이 너무 다른 여성이 많아서 본인 확인이 어려운 때도 있기 때문이다.", "This is because there are many women whose appearance in the passport photo and actual face at entry are so different that confirming their identity is sometimes difficult."),
    ("얼마 전 한국에서 성형 수술한 왕링 씨는 이십팔 일 밤 항공편으로 서울 여행을 마치고 베이징공항을 통해 귀국했다.", "Ms. Wang Ling, who had cosmetic surgery in Korea not long ago, finished her trip to Seoul on the night of the 28th by air and returned home through Beijing airport."),
    ("이 과정에서 왕 씨는 경찰의 조사를 받아야 했다.", "In this process Ms. Wang had to be questioned by the police."),
    ("한국에서 성형수술을 한 뒤 여권 사진과 실제 얼굴에 차이가 너무 컸기 때문이었다.", "It was because, after having cosmetic surgery in Korea, the difference between her passport photo and her actual face was too big."),
    ("이와 관련, 베이징 공항의 한 관계자는 귀를 성형 수술하는 사람은 거의 없어 본인 확인을 위해 최근에는 귀 모양을 비교하는 노하우가 생겼다고 전했다.", "In this connection, an official at Beijing airport said that almost no one has plastic surgery on the ears, so recently a know-how of comparing ear shapes has developed to confirm identity."),
    ("중국 공항 측은 이런 불편을 해결하기 위해 앞으로 해외에서 성형수술을 하면 병원에서 성형수술 증명서를 받아 출입국 시 제시해야 한다고 밝혔다.", "To solve this inconvenience, the Chinese airport side announced that in the future, anyone who has cosmetic surgery abroad must receive a cosmetic surgery certificate from the hospital and present it when entering or leaving the country."),
]
L4 = lesson(
    "Ch 48 · Follow-ups A and activities: New Year surgery and the passport problem",
    "설 연휴 · 취업준비족 · 성형외과 · 여권 사진 · 본인 확인 · 성형수술 증명서 · 귀 모양 · 입국",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): surgery during the New Year holiday",
             "The following text is about the New Year’s holiday (한겨레). The book asks you to read it and answer in English: what (new) trend the article is about, and how the medical clinics promote their businesses to take advantage of it (two examples). The text is the book’s with the age written out (26 is 스물여섯 살); the quotation marks are removed. The book glosses ~족 [族]: a tribe, a group, a party; ~생 [生]: a student, an apprentice; 김 아무개 씨 = 김 모 씨; and 지방: a region outside the capital city. The English is mine.",
             examples=passage(_NY)),
        card("Follow-up 2 answered (mine)",
             "1. The trend: job seekers who have cosmetic surgery during the long Lunar New Year holiday to prepare for first-half corporate hiring. 2. Two examples of promotion: special New Year products tied up with job sites, with a large discount for group surgery; and lodging offered to those who come up from the provinces."),
        card("Activity 2 (Reading): problems with cosmetic surgery in China",
             "The following news article addresses problems associated with cosmetic surgery in China. The book asks you to fill in a table in English (the issue addressed and the solution to the issue). The text is the book’s with 28일 spelled 이십팔 일; the quotation marks are removed. The English is mine.",
             examples=passage(_CHN)),
        card("The table filled in (mine)",
             "",
             tables=[table(["Issue addressed", "Solution to the issue"], [["Chinese women who have had cosmetic surgery abroad look so different from their passport photos that confirming their identity is difficult", "Comparing ear shapes (almost nobody has plastic surgery on the ears); in the future, requiring a cosmetic surgery certificate from the hospital, to be presented when entering and leaving the country"]])]),
        card("Activities left out",
             "Follow-up 1 (listening to a YTN news report about Mr. Chung, a would-be entertainer, writing the key information in English and summarizing the news), Activity 1 (SMART Board), Activity 3 (listening to a YTN clip about cosmetic surgery in Korea: choosing the main point, filling in the percentage of each type of surgery, and writing the advice offered to patients to avoid post-surgical difficulties) and Activity 4 (groups argue for or against cosmetic surgery, write the reasons in the class notebook [MS TEAMS], present them in Korean and summarize the other group’s argument) are audio, computer and group activities."),
    ],
    exercises=uniq(
        _tr(_NY + _CHN, k=3)
        + [M("What do 취업준비족 want to do during the long New Year holiday?", "Have cosmetic surgery", ["Travel abroad", "Go to their hometowns", "Study"], "성형수술."), M("What did Ms. Kim decide to do this New Year?", "Not go home and have double eyelid surgery", ["Go home", "Quit her job and travel", "Study in Seoul"], "쌍꺼풀 수술."), M("Why did her parents understand?", "They said getting a job comes before going home", ["They wanted her to be pretty", "They were away", "They paid for it"], "귀성보다는 취직이 먼저."), M("What do some clinics offer for group surgery?", "A large discount", ["Free meals", "Free travel", "A prize"], "큰 폭으로 깎아 주다."), M("What do some clinics give to people from the provinces?", "Lodging", ["Money", "Tickets", "Clothes"], "숙소."), M("What new worry did Chinese authorities have?", "Confirming identity because faces differ from passport photos", ["Too many visitors", "Too few doctors", "High prices"], "본인 확인."), M("What did Ms. Wang have to do at Beijing airport?", "Be questioned by the police", ["Pay a fine", "Wait a week", "Return to Seoul"], "경찰의 조사."), M("What did an airport official say they now compare?", "Ear shapes", ["Fingerprints", "Eye colors", "Heights"], "귀 모양."), M("What must those who have surgery abroad present when entering or leaving China?", "A cosmetic surgery certificate", ["A visa only", "A health report", "A bank statement"], "성형수술 증명서."),
           F("취업준비생 김 씨는 이번 설에 ___ 수술을 하기로 했다. (double eyelid)", "쌍꺼풀", ["치아", "주름"], "쌍꺼풀."), F("일부 성형외과들은 설맞이 특별 ___을 내놓았다. (products)", "상품", ["증명서", "소문"], "상품."), F("본인 ___이 어려운 때도 있다. (identity confirmation)", "확인", ["송금", "평가"], "확인."), F("성형수술 ___를 받아 입국 시 제시해야 한다. (certificate)", "증명서", ["소문", "여건"], "증명서."), F("여권 사진과 실제 얼굴에 ___가 너무 컸다. (difference)", "차이", ["차례", "점"], "차이."),
           read_q("설 연휴에 성형수술을 하려는 사람들이 늘고 있습니다"), read_q("단체로 수술을 받으면 큰 폭으로 깎아 줍니다"), read_q("여권 사진과 실제 얼굴이 너무 다릅니다"), read_q("귀 모양을 비교하는 노하우가 생겼습니다"), read_q("성형수술 증명서를 받아 입국할 때 제시해야 합니다")]
    ),
)


# ================================================================== L5 Topic B
_B_TXT = [
    ("최준형 씨는 아내와 딸 하나를 둔 사십 대 가장이다.", "Mr. Choi Jun-hyeong is a family head in his forties with a wife and one daughter."),
    ("대기업에서 이십 년 동안 근무하고 있는데 급여와 사원복지 등의 근무 여건이 좋다.", "He has been working at a large company for twenty years, and the working conditions, such as salary and employee welfare, are good."),
    ("몇 달 전에는 해외영업부 부장이 돼서 바빠졌다.", "A few months ago he became the head of the overseas sales department and became busy."),
    ("그런데 요즘 불경기 때문에 회사 분위기가 좋지 않다.", "But these days the atmosphere at the company is not good because of the recession."),
    ("경영 사정이 어려워져서 구조조정을 한다는 소문이 있다.", "There is a rumor that, because the management situation has become difficult, they are going to restructure."),
    ("곧 인원 감축을 하면서 직원들을 해고할 거라고 한다.", "They say that soon, as they cut personnel, they will lay off employees."),
    ("특히 오십 세 이하의 직원들에게도 조기퇴직이나 명예퇴직을 권유할 거라고 한다.", "In particular, they say they will recommend early retirement or honorary retirement even to employees aged 50 or under."),
    ("그래서 최준형 씨는 요즘 출근하기가 싫다.", "So Mr. Choi does not want to go to work these days."),
    ("부장이 된 후부터는 스트레스도 많고 늘 과로해서 피곤하다.", "Since becoming a department head he has a lot of stress and is always tired from overwork."),
    ("또 구조조정 소문 때문에 실직할까 봐 걱정이 많다.", "Also, because of the rumor of restructuring, he is very worried that he might lose his job."),
    ("그래서 다른 일자리를 알아보려고 한다.", "So he intends to look into other jobs."),
    ("그런데 경기침체 때문에 재취업하기가 쉽지 않을 것 같다.", "But because of the economic stagnation, it seems that it will not be easy to be re-employed."),
]
_B_WORDS = ["가장", "감축", "고용", "구조조정", "구직난", "권유", "급여", "동향", "명예퇴직", "분석", "불경기", "소문", "실업자", "실직", "여건", "영업", "~ 이하", "인력", "청년", "추진", "침체", "폐업", "해고"]
_DU = [("참 훌륭한 아들을 두셨군요.", "You have such a wonderful son."), ("종업원을 두지 않고 직접 식당을 운영한다.", "They run the restaurant on their own without having any employees.")]
_NAN = [("구직난", "difficulty finding a job"), ("취업난", "difficulty getting employed"), ("구인난", "difficulty finding workers"), ("인력난", "a labor shortage")]
_CHOI = [["Age: in his forties; family head; wife and one daughter. Twenty years at a large company with good pay and welfare; a few months ago became head of the overseas sales department", "Because of the recession, a rumor of restructuring: personnel cuts, layoffs, and early or honorary retirement even for those aged 50 or under", "Does not want to go to work; stressed and overworked; worried about losing his job; plans to look for another job, but re-employment seems hard because of the stagnation"]]
L5 = lesson(
    "Ch 48 · Topic B: the recession (불경기)",
    "불경기 · 실직 · 이직 · 창업 · 구조조정 · 명예퇴직 · 인원 감축 · 해고 · 최준형 씨",
    requires=[],
    cards=[
        card("Topic B: the recession (불경기)",
             "The following magazine article is about a man in his late 40s who is concerned about losing his job. The picture’s labels are 실직, 이직 and 창업? (The English is mine; the book gives none. The numbers are spelled out: 40대 is 사십 대, 20년 is 이십 년, 50세 이하 is 오십 세 이하.)",
             examples=passage(_B_TXT)),
        card("Footnote: 두다", "두다 literally means “to put” or “to place.” Here, it means to have (somebody as a member of an organization), as in:", examples=passage(_DU)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_B_WORDS)),
        card("한국어에는",
             "1. The Sino-Korean word 란/난 (難) means a difficulty and is often used as a suffix, as in 구직난, 취업난, 구인난, 인력난, etc.\n2. 조기퇴직 (early retirement) and 명예퇴직 (honorary retirement) are similar to the Voluntary Separation Incentive Program (VSIP) in the United States. They are often written as the acronyms 조퇴 and 명퇴.",
             tables=[ktable(_NAN)]),
        card("The table of Presentation Study c (mine)", "The book asks you to read Topic Presentation B and fill in a table in English. My answers:", tables=[table(["Mr. Choi’s biographical information", "Rumors and plans", "Concerns"], [list(r) for r in _CHOI])]),
        card("Activities left out", "The sentence-strip pair activity (a) and the SMART Board activity (b), the review with the teacher (d), and Follow-up 1 (listening to two conversations in which an unemployed man calls an officer at the Ministry of Labor, writing the purpose of the call, the reason for unemployment and the previous occupation) are audio, computer and pair activities. The book’s useful website is the Ministry of Employment and Labor (고용노동부). Its Sino-Korean note on 실직 is in the first lesson of the chapter."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT, k=3) + _tr(_DU, k=2) + _tr(_NAN, k=3)
        + [M("How old is Mr. Choi, roughly?", "In his forties", ["In his twenties", "In his sixties", "A teenager"], "사십 대."), M("How long has he worked at the large company?", "Twenty years", ["Two years", "A few months", "Fifty years"], "이십 년."), M("What did he become a few months ago?", "Head of the overseas sales department", ["A new employee", "The company president", "A retiree"], "해외영업부 부장."), M("Why is the company atmosphere bad?", "Because of the recession", ["Because of a holiday", "Because of a new boss", "Because of a move"], "불경기."), M("What is the rumor?", "That the company will restructure", ["That the company will expand", "That wages will rise", "That the office will move"], "구조조정."), M("Who will be offered early or honorary retirement?", "Even employees aged 50 or under", ["Only the president", "Only new hires", "Nobody"], "오십 세 이하."), M("Why is Mr. Choi tired?", "Stress and constant overwork", ["Travel", "Illness", "A new baby"], "스트레스도 많고 늘 과로."), M("What is he worried about?", "Losing his job", ["Losing his keys", "Missing a train", "A bad grade"], "실직할까 봐."), M("What does he plan to do?", "Look into other jobs", ["Start a farm", "Move abroad", "Go back to school"], "다른 일자리."), M("Why will re-employment not be easy?", "Because of the economic stagnation", ["Because of his age only", "Because of the weather", "Because of his family"], "경기침체."), M("What does 두다 mean in 딸 하나를 둔?", "to have (a person as a member)", ["to put on a shelf", "to drop", "to bury"], "The book’s footnote."), M("What does the suffix 난 (難) mean?", "a difficulty", ["a room", "a person", "a certificate"], "구직난."), M("What are the acronyms of 조기퇴직 and 명예퇴직?", "조퇴 and 명퇴", ["조직 and 명직", "조기 and 명예", "퇴직 and 명직"], "The book’s note."),
           F("최준형 씨는 아내와 딸 하나를 ___ 사십 대 가장이다. (have)", "둔", ["둘", "두는"], "두다 + ㄴ."), F("회사 분위기가 좋지 않은 것은 ___ 때문입니다. (the recession)", "불경기", ["구직난", "병역"], "불경기."), F("직원들을 ___할 거라고 한다. (lay off)", "해고", ["고용", "폐업"], "해고."), F("곧 인원 ___을 한다는 소문이 있다. (reduction)", "감축", ["분석", "추진"], "감축."), F("직원들에게 명예퇴직을 ___할 거라고 한다. (recommend)", "권유", ["폐업", "해고"], "권유."),
           read_q("최준형 씨는 사십 대 가장입니다"), read_q("구조조정을 한다는 소문이 있습니다"), read_q("실직할까 봐 걱정이 많습니다"), read_q("다른 일자리를 알아보려고 합니다"), read_q("재취업하기가 쉽지 않을 것 같습니다")]
    ),
)

# ================================================================== L6 Follow-ups B
_OECD = [
    ("우리나라의 삼십사 세 이하 청년 고용률이 경제협력개발기구(오이씨디) 최하위 수준인 것으로 나타났다.", "It turned out that our country’s employment rate for youth aged 34 or under is at the lowest level in the OECD (Organisation for Economic Co-operation and Development)."),
    ("한국노동연구원은 지난해 발표된 오이씨디의 고용동향 통계를 분석해 우리나라 십오 세에서 이십사 세, 이십오 세에서 삼십사 세 고용률이 오이씨디 국가 중 각각 꼴찌인 헝가리와 멕시코 다음 순위였다고 십구 일 밝혔다.", "The Korea Labor Institute analyzed the OECD’s employment trend statistics announced last year and announced on the 19th that our country’s employment rates for ages 15 to 24 and 25 to 34 ranked next after Hungary and Mexico, which were respectively last among the OECD countries."),
    ("한국의 십오 세에서 이십사 세와 이십오 세에서 삼십사 세 고용률은 각각 이십삼 점 팔 퍼센트, 육십구 점 육 퍼센트였으며 헝가리와 멕시코는 각각 이십 퍼센트, 육십구 점 사 퍼센트였다.", "Korea’s employment rates for ages 15 to 24 and 25 to 34 were 23.8 percent and 69.6 percent respectively, and those of Hungary and Mexico were 20 percent and 69.4 percent respectively."),
]
_OECD_NUM = [["23.8%", "Korea’s employment rate for ages 15 to 24"], ["69.6%", "Korea’s employment rate for ages 25 to 34"], ["20%", "Hungary’s employment rate for ages 15 to 24 (last among the OECD countries)"], ["69.4%", "Mexico’s employment rate for ages 25 to 34 (last among the OECD countries)"]]
_DESC1 = [("김소정 씨는 지난 칠 년 동안 금융회사에서 근무했다. 그런데 회사 사정이 어려워져서 삼 개월 전에 해고되었다. 실직한 후 정부에서 주는 돈으로 생활하고 있다.", "Ms. Kim So-jeong worked at a financial company for the last seven years. But the company’s situation became difficult and she was laid off three months ago. After losing her job she is living on money given by the government.", "e. 실업급여"), ("전 세계적인 불황의 영향이 국내 경제에도 미치고 있다. 이에 따라 수출과 수입이 감소하고 소비도 줄어들고 있다. 그래서 폐업하는 회사들이 늘고 있다.", "The effect of the worldwide depression is reaching the domestic economy too. Accordingly exports and imports are decreasing and consumption is also declining. So the number of companies going out of business is increasing.", "b. 경기침체"), ("이상호 씨는 중소기업의 해외 영업부장으로 근무해 왔다. 그런데 최근에 회사 전체에 구조조정을 한다는 소문이 있었다. 그래서 해고당하기 전에 미리 회사를 그만두기로 했다.", "Mr. Lee Sang-ho has worked as the overseas sales manager of a small and medium-sized company. But recently there was a rumor that the whole company would be restructured. So he decided to quit the company in advance, before being fired.", "a. 명예퇴직"), ("올해는 새로 인력을 고용하려는 기업들이 많지 않아서 일자리를 구하기가 어렵다. 특히 근무여건이 좋고 연봉이 높은 대기업은 입사 경쟁률이 매우 높다.", "This year there are not many companies trying to hire new personnel, so it is hard to find a job. In particular, large companies with good working conditions and high annual salaries have a very high competition rate for entry.", "d. 구직난")]
_QA = [
    ("요즘 취업이 너무 어려워서 창업을 계획하고 있습니다. 어떻게 준비해야 할까요?", "Getting a job is so difficult these days that I am planning to start a business. How should I prepare?"),
    ("창업을 희망하는 학생들은 우선 창업에 적합한 기업가 정신과 창업 마인드를 갖추고 있는지 점검해 보기 바랍니다.", "Students who hope to start a business should first check whether they have the entrepreneurial spirit and the start-up mindset suited to starting a business."),
    ("또 혼자서 준비하기보다는 창업에 필요한 교육을 받고 창업 동아리에 참가하여 다양한 경험과 경력을 쌓아 보기 바랍니다.", "Also, rather than preparing alone, I hope you will receive the education needed for starting a business, join a start-up club and build up various experiences and careers."),
    ("또 최근 서울시에서는 이십 대, 삼십 대 예비창업자들을 대상으로 청년 씨이오를 육성하기 위한 프로젝트를 추진하겠다고 발표한 바 있습니다.", "Also, Seoul City recently announced that it will push ahead with a project to foster young CEOs targeting prospective entrepreneurs in their twenties and thirties."),
    ("이 프로젝트에서는 게임, 아이티 개발, 융합디자인, 바이오, 환경, 패션, 기계, 공예, 디자인, 뮤지컬공연기획, 이비즈, 쇼핑몰 운영, 전통음식 제조업 등 다양한 분야를 지원할 예정이기 때문에 고등학교 또는 대학교에서 자신의 전공을 살려 창업하고자 하는 학생들에게 큰 도움이 될 것으로 보입니다.", "In this project they plan to support various fields such as games, IT development, convergence design, bio, environment, fashion, machinery, crafts, design, musical performance planning, e-biz, shopping mall operation and traditional food manufacturing, so it seems it will be of great help to students who want to start a business making use of their major at high school or university."),
]
_Q2 = [["Educational and club preparation: check that you have an entrepreneurial spirit and a start-up mindset; receive education needed for starting a business; join a start-up club; build up various experiences and careers", "To foster young CEOs", "Prospective entrepreneurs in their twenties and thirties (including students who want to start a business using their major at high school or university)"]]
L6 = lesson(
    "Ch 48 · Follow-ups B and activities: youth employment, descriptions, starting a business",
    "청년 고용률 · 오이씨디 · 실업급여 · 경기침체 · 명예퇴직 · 구직난 · 창업 · 청년 씨이오",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): youth employment rates",
             "The following article is from an online newspaper (YonhapNews). The book asks you to check the topic, say what each number means and underline and translate the topic sentence. The text is the book’s with the numbers spelled out (34세 is 삼십사 세, 15~24세 is 십오 세에서 이십사 세, 23.8% is 이십삼 점 팔 퍼센트, OECD is 오이씨디, 19일 is 십구 일). The book glosses 최하위: lowest in rank. The English is mine.",
             examples=passage(_OECD)),
        card("Follow-up 2 answered (mine)",
             "1. The topic: the employment rate (a low youth employment rate; the other options, restructuring a company, unemployment rate, downsizing a company and layoffs, are not the topic).\n\n3. The topic sentence is the first one: 우리나라의 34세 이하 청년 고용률이 OECD 최하위 수준인 것으로 나타났다 (It turned out that our country’s employment rate for youth aged 34 or under is at the lowest level in the OECD).",
             tables=[table(["Percent", "Reference (mine)"], _OECD_NUM)]),
        card("Activity 1 (Reading): which word is described?",
             "Match each description with the word it describes: a. 명예퇴직 b. 경기침체 c. 고용증가 d. 구직난 e. 실업급여 (one word does not have a match). The descriptions are the book’s with the numbers spelled out (7년 is 칠 년, 3개월 is 삼 개월); the English and answers are mine. The unmatched word is c. 고용증가 (an increase in employment).",
             tables=[table(["Description", "Answer (mine)"], [[a, c] for a, b, c in _DESC1], say=[0]), table(["English of the description (mine)"], [[b] for a, b, c in _DESC1])]),
        card("Activity 3 (Reading): a Q&A on starting a business",
             "The following Q&A exchange is from an online Korean newspaper (Hankyoreh). The answer is headed 지원제도 풍성… 맞는 분야 찾아 도전하길 (Plenty of support systems… I hope you will find a suitable field and take the challenge) and signed by 이랑, chief researcher at the Job Research Center of the Korea Employment Information Service. The text is the book’s with 20, 30대 spelled out (이십 대, 삼십 대), CEO and IT and E-biz spelled in Hangul (씨이오, 아이티, 이비즈); the parenthetical advice to see the Seoul City websites is left out of the passage. The book glosses 정신: spirit; 예비: prospective; 육성하다: to promote, to foster. The English is mine.",
             examples=passage(_QA)),
        card("Activity 3 answered (mine)",
             "a. The Q&A section’s question is translated above (the first line of the passage).\n\nb. The table:",
             tables=[table(["Preparations recommended for opening a business", "Purpose of Seoul City’s project", "Candidates for Seoul City’s project"], [list(r) for r in _Q2])]),
        card("Activities left out", "Activity 2 (a video clip from MBC America on a college campus: the relationship between two women, the social issue mentioned and what the woman in blue has been doing) and Activity 4 (listening to interviews with Mr. Kim and Ms. Park, who recently lost their jobs, exchanging information with a partner, summarizing and presenting) are audio, video, pair and writing activities."),
    ],
    exercises=uniq(
        _tr(_OECD + _QA, k=3) + _tr([(a, b) for a, b, c in _DESC1], k=3)
        + [M("What did the article say about Korea’s youth employment rate?", "It is at the lowest level in the OECD", ["It is the highest", "It is average", "It is rising fast"], "최하위 수준."), M("Which two countries ranked last in the OECD for these age groups?", "Hungary and Mexico", ["Japan and China", "Italy and Spain", "Chile and Peru"], "헝가리와 멕시코."), M("What was Korea’s employment rate for ages 15 to 24?", "23.8%", ["69.6%", "20%", "69.4%"], "이십삼 점 팔 퍼센트."), M("What was Korea’s employment rate for ages 25 to 34?", "69.6%", ["23.8%", "20%", "69.4%"], "육십구 점 육 퍼센트."), M("What was Hungary’s rate for ages 15 to 24?", "20%", ["23.8%", "69.6%", "69.4%"], "이십 퍼센트."), M("What was Mexico’s rate for ages 25 to 34?", "69.4%", ["20%", "23.8%", "69.6%"], "육십구 점 사 퍼센트."), M("Which word matches the description of living on government money after being laid off?", "실업급여", ["경기침체", "구직난", "명예퇴직"], "e."), M("Which word matches the description of falling exports and imports and closing companies?", "경기침체", ["실업급여", "구직난", "명예퇴직"], "b."), M("Which word matches the description of quitting before being fired?", "명예퇴직", ["구직난", "실업급여", "경기침체"], "a."), M("Which word matches the description of few firms hiring and tough competition?", "구직난", ["명예퇴직", "경기침체", "실업급여"], "d."), M("Which word has no match?", "고용증가", ["구직난", "경기침체", "실업급여"], "c."), M("What is the purpose of Seoul City’s project?", "To foster young CEOs", ["To build roads", "To lower taxes", "To train soldiers"], "청년 씨이오 육성."), M("Who are the candidates for the project?", "Prospective entrepreneurs in their twenties and thirties", ["Retired workers", "Foreign tourists", "High school teachers"], "예비창업자."), M("What does the expert advise students to do instead of preparing alone?", "Get education and join a start-up club", ["Wait a year", "Move abroad", "Buy a shop"], "교육과 동아리."),
           F("한국의 고용률은 오이씨디 ___ 수준이었다. (lowest)", "최하위", ["최고", "평균"], "최하위."), F("우리나라의 청년 ___이 낮은 것으로 나타났다. (employment rate)", "고용률", ["실업률", "수출"], "고용률."), F("그 회사는 경기침체로 ___하는 회사가 늘고 있다. (going out of business)", "폐업", ["고용", "권유"], "폐업."), F("창업을 하려면 우선 기업가 ___을 갖추어야 한다. (spirit)", "정신", ["소문", "여건"], "정신."), F("서울시는 청년 씨이오를 ___하는 프로젝트를 추진한다. (foster)", "육성", ["폐업", "해고"], "육성."),
           read_q("청년 고용률이 최하위 수준입니다"), read_q("한국의 십오 세에서 이십사 세 고용률은 이십삼 점 팔 퍼센트입니다"), read_q("경기침체로 폐업하는 회사들이 늘고 있습니다"), read_q("창업을 준비하는 학생들은 창업 동아리에 참가해 보세요"), read_q("서울시는 청년 씨이오를 육성하는 프로젝트를 추진합니다")]
    ),
)


# ================================================================== L7 Grammar -(으)ㄹ까 봐(서)
_G1 = [("시험에 떨어질까 봐(서) 공부를 열심히 했어요.", "Being afraid that I might fail the exam, I studied hard."), ("시험에 떨어질까 봐(서) 걱정이에요.", "Being aware that I might fail the exam, I am worried / I am worried that I might fail the exam.")]
_G2 = [("차가 많이 막힐까 봐 걱정이에요.", "I am worried that there might be a traffic jam."), ("비행기가 추락할까 봐 무서웠어요?", "Were you scared that the plane might crash?")]
_G3 = [("김 일병은 과속으로 단속에 걸릴까 봐 천천히 운전했습니다.", "Afraid that he might be caught for speeding, PFC Kim drove slowly."), ("음식이 부족할까 봐서 음식을 많이 준비했어요.", "Afraid that there would not be enough, I prepared a lot of food."), ("수업에 늦을까 봐 불안해요.", "Being aware that I might be late for class, I feel nervous. / I feel nervous that I might be late for class.")]
_G_SAY = [("시험에 떨어질까 봐서 공부를 열심히 했어요.", "Being afraid that I might fail the exam, I studied hard (with the 서 form)."), ("시험에 떨어질까 봐서 걱정이에요.", "I am worried that I might fail the exam (with the 서 form).")]
_FEEL = [("두렵다", "to be afraid; to fear"), ("무섭다", "to be scary; to be afraid"), ("걱정되다", "to be worried"), ("걱정하다", "to worry"), ("겁나다", "to be scared"), ("떨리다", "to be nervous; to tremble")]
L7 = lesson(
    "Ch 48 · Grammar in Focus: –(으)ㄹ까 봐(서) (being afraid that…)",
    "접속 어미 · –(으)ㄹ까 봐(서) · 걱정 · 두려움 · 두렵다 · 무섭다 · 겁나다 · 떨리다",
    requires=[],
    cards=[
        card("Conjunctive Ending –(으)ㄹ까 봐(서)",
             "The conjunctive ending –(으)ㄹ까 봐(서), which translates to being afraid that [something/someone] might… or being aware that [something/someone] might …, expresses the subject’s (of a sentence) concern or awareness of future problems. For example:",
             examples=passage(_G_SAY),
             tables=[table(["Written form of the book’s examples", "Meaning"], [[a, b] for a, b in _G1])]),
        card("Two kinds of main clause",
             "Note that the main clause following the conjunctive ending can express one of two ideas: the subject’s proactive action to prevent future problems, as in the first example (공부를 열심히 했어요), or the subject’s feelings or emotion, as in the second example (걱정이에요).\n\nWhen the main clause expresses the subject’s feelings or emotion, verbs such as 두렵다, 무섭다, 걱정되다/하다, 겁나다, or 떨리다 are commonly used, and the whole sentence can translate to The subject is afraid [worried/scared/nervous, etc.] that something might…. For example:",
             examples=passage(_G2),
             tables=[ktable(_FEEL)]),
        card("Conjunctive Ending: verb stem + (으)ㄹ까 봐(서)",
             "Add –ㄹ까 봐(서) to a verb stem that ends in a vowel (or ㄹ) and –을까 봐(서) to a stem that ends in a consonant. More examples:",
             examples=passage(_G3)),
        card("Activities left out", "Follow-up 1 (a pair activity: Partner A starts a sentence from a phrase strip and conjugates the verb with –(으)ㄹ까 봐(서), and Partner B completes it with a logical main clause, e.g. 살이 찌다 → 살이 찔까 봐 → 살이 찔까 봐 걱정입니다 or 살이 찔까 봐 요즘 햄버거를 먹지 않습니다; the strips are not printed in the student text) and Follow-up 2 (three video clips from 내 생애 마지막 스캔들, 내 이름은 김삼순 and 거침없이 하이킥 in which a person uses –(으)ㄹ까 봐, filling in a fear/response table) are pair and video activities."),
    ],
    exercises=uniq(
        _tr(_G_SAY + _G2 + _G3, k=3)
        + [M("What does –(으)ㄹ까 봐(서) express?", "Concern or awareness of a possible future problem", ["A past habit", "A wish to go", "A command"], "The book’s explanation."), M("What does 시험에 떨어질까 봐 공부를 열심히 했어요 mean?", "Afraid that I might fail the exam, I studied hard", ["I failed the exam", "I passed the exam", "I did not study"], "Proactive action."), M("What does 시험에 떨어질까 봐 걱정이에요 mean?", "I am worried that I might fail the exam", ["I will take the exam", "I am happy", "I studied hard"], "Feeling."), M("What does 차가 많이 막힐까 봐 걱정이에요 mean?", "I am worried that there might be a traffic jam", ["The traffic is clear", "I drove fast", "I am late"], "걱정이에요."), M("What does 비행기가 추락할까 봐 무서웠어요? mean?", "Were you scared that the plane might crash?", ["Did the plane land?", "Was the flight long?", "Did you fly?"], "무섭다."), M("Why did PFC Kim drive slowly?", "He was afraid of being caught for speeding", ["He was tired", "The road was closed", "He was lost"], "단속에 걸릴까 봐."), M("Why did the speaker prepare a lot of food?", "Afraid there would not be enough", ["There were many guests only", "It was cheap", "It was a holiday"], "부족할까 봐서."), M("What does 수업에 늦을까 봐 불안해요 mean?", "I feel nervous that I might be late for class", ["I was late for class", "I enjoy class", "Class is over"], "불안해요."), M("Which verb is commonly used for a feeling in the main clause?", "겁나다", ["먹다", "가다", "읽다"], "The book lists 두렵다, 무섭다, 걱정되다/하다, 겁나다, 떨리다."), M("What does 떨리다 mean?", "to be nervous; to tremble", ["to fall", "to be scary", "to worry"], "떨리다."), M("What does 겁나다 mean?", "to be scared", ["to be nervous", "to be tired", "to be sad"], "겁나다."), M("Which ending attaches to a stem that ends in a consonant?", "–을까 봐(서)", ["–ㄹ까 봐(서)", "–는데도", "–려던"], "먹을까 봐."),
           F("수업에 늦___ 봐 불안해요. (might be late)", "을까", ["는데", "으니까"], "늦을까 봐."), F("차가 막히___ 봐 일찍 출발했어요. (might jam)", "ㄹ까", ["는데", "면"], "막힐까 봐."), F("비행기가 추락할까 ___ 무서웠어요. (afraid that)", "봐", ["서", "고"], "–ㄹ까 봐."), F("음식이 부족할까 ___ 음식을 많이 준비했어요. (afraid that)", "봐서", ["고서", "면서"], "봐서."), F("시험에 떨어질까 봐 ___이에요. (I am worried)", "걱정", ["사랑", "방학"], "걱정."),
           read_q("시험에 떨어질까 봐서 공부를 열심히 했어요"), read_q("차가 많이 막힐까 봐 걱정이에요"), read_q("비행기가 추락할까 봐 무서웠어요"), read_q("김 일병은 과속으로 단속에 걸릴까 봐 천천히 운전했습니다"), read_q("수업에 늦을까 봐 불안해요")]
    ),
)

# ================================================================== L8 Follow-up 3 and practice
_MODEL = [("살이 찔까 봐 걱정입니다.", "I am worried that I might gain weight."), ("살이 찔까 봐 요즘 햄버거를 먹지 않습니다.", "Afraid that I might gain weight, I am not eating hamburgers these days."), ("저는 시험에 떨어질까 봐 열심히 공부를 합니다. 김 일병은 무엇이 걱정됩니까?", "I study hard for fear of failing the exam. PFC Kim, what are you worried about?"), ("저는 고향에 있는 여자친구가 헤어지자고 할까 봐 무섭습니다. 그래서 매일 여자친구한테 전화합니다.", "I am scared that my girlfriend back home might say let’s break up. So I call my girlfriend every day.")]
_Q1 = [("대학교 삼 학년 학생입니다. 요즘은 대학을 졸업해도 취직하기가 어렵다는 말을 많이 듣습니다. 저도 졸업한 후에 취업을 못 할까 봐 걱정이 많이 됩니다. 그래서 일 년 정도 휴학을 할까 생각 중입니다. 휴학하면서 취업 준비를 더 한 후에 졸업하려고 합니다. 어떻게 생각하세요?", "I am a third-year university student. These days I often hear that it is hard to get a job even after graduating from university. I am also very worried that I might not be able to get a job after I graduate. So I am thinking of taking about a year off from school. While on leave I want to prepare more for employment and then graduate. What do you think?"), ("창업을 준비하고 있습니다. 저는 사업 경험이 없어서 걱정이 큽니다. 퇴직금으로 사업을 하려고 하는데, 실패할까 봐 무섭습니다. 창업에 성공하려면 어떻게 해야 합니까?", "I am preparing to start a business. I have no business experience, so I am very worried. I am going to run a business with my retirement pay, but I am scared that I might fail. What should I do to succeed in starting a business?")]
_Q1T = [["1", "That after graduating he or she might not be able to get a job", "Is very worried; is thinking of taking about a year off to prepare more for employment and then graduate"], ["2", "That the business might fail (no business experience; using retirement pay)", "Very worried and scared; asks how to succeed in starting a business"]]
_PR = [("회사에서 해고될까 봐 걱정이에요.", "I am worried that I might be fired from the company."), ("실직할까 봐 매일 일찍 출근합니다.", "Afraid that I might lose my job, I go to work early every day."), ("병역비리가 늘어날까 봐 병무청에서는 신체검사를 철저히 합니다.", "Afraid that military service corruption might increase, the Military Manpower Administration does the physical examination thoroughly."), ("부작용이 있을까 봐 성형수술을 하지 않았어요.", "Afraid that there might be side effects, I did not have cosmetic surgery."), ("불경기에 회사가 문을 닫을까 봐 두렵습니다.", "I am afraid that the company might close in the recession.")]
L8 = lesson(
    "Ch 48 · Grammar follow-ups: –(으)ㄹ까 봐(서) in use",
    "–(으)ㄹ까 봐 · 걱정 · 휴학 · 창업 · 퇴직금 · 연습 문장",
    requires=[],
    cards=[
        card("Follow-up 4 (the book’s models)",
             "In this activity you share with classmates what you do or will do to prevent something you are afraid might happen to you. The book’s model sentences for the pair work (the English is mine):",
             examples=passage(_MODEL)),
        card("Follow-up 3 (Reading): concerns posted on a Q&A site",
             "The following concerns are posted on the Q&A section of a website. The book asks you to fill in a table in English (the writer’s concern/fear and the writer’s feeling or action). The text is the book’s with 3학년 spelled 삼 학년 and 1년 spelled 일 년; the English is mine.",
             examples=passage(_Q1)),
        card("Follow-up 3 answered (mine)", "", tables=[table(["Question", "Writer’s concern or fear", "Writer’s feeling or action"], [list(r) for r in _Q1T])]),
        card("More practice sentences (mine)", "Sample sentences of my own that combine –(으)ㄹ까 봐(서) with the chapter’s vocabulary (the English is mine):", examples=passage(_PR)),
        card("Activities left out", "Follow-up 4 (the speaking activity: think of two things you are afraid might happen to you and what you do or will do to prevent them, fill in your column of a table, meet three classmates, exchange information in Korean, write their answers down and share the most interesting response) is a pair and group activity."),
    ],
    exercises=uniq(
        _tr(_MODEL + _Q1 + _PR, k=3)
        + [M("What is the first writer worried about?", "Not being able to get a job after graduating", ["Failing a test", "Losing a wallet", "Being too tall"], "취업을 못 할까 봐."), M("What is the first writer thinking of doing?", "Taking about a year off school", ["Quitting for good", "Getting married", "Traveling"], "휴학."), M("What will the first writer do while on leave?", "Prepare more for employment", ["Study abroad", "Work on a farm", "Rest"], "취업 준비."), M("What is the second writer preparing to do?", "Start a business", ["Buy a car", "Change schools", "Move"], "창업."), M("What will the second writer use for the business?", "Retirement pay", ["A loan", "A prize", "A gift"], "퇴직금."), M("What is the second writer afraid of?", "That the business might fail", ["That it will rain", "That prices will drop", "That no one will visit"], "실패할까 봐."), M("What does 살이 찔까 봐 걱정입니다 mean?", "I am worried that I might gain weight", ["I lost weight", "I am hungry", "I am strong"], "살이 찌다."), M("What does 실직할까 봐 매일 일찍 출근합니다 mean?", "Afraid of losing my job, I go to work early every day", ["I lost my job", "I work late", "I am on vacation"], "실직할까 봐."), M("What does 부작용이 있을까 봐 성형수술을 하지 않았어요 mean?", "Afraid of side effects, I did not have cosmetic surgery", ["I had surgery", "I have no fear", "I like surgery"], "부작용."), M("What is the boyfriend’s model response to fear in the book’s example?", "Calls his girlfriend every day", ["Studies hard", "Eats less", "Drives slowly"], "매일 여자친구한테 전화합니다."),
           F("취업을 못 할___ 봐 걱정이 많이 됩니다. (might not)", "까", ["서", "고"], "–ㄹ까 봐."), F("퇴직금으로 사업을 하려고 하는데, 실패할까 ___ 무섭습니다. (afraid that)", "봐", ["서", "고"], "–ㄹ까 봐."), F("저는 시험에 떨어질까 봐 열심히 공부를 ___. (study)", "합니다", ["먹습니다", "잡니다"], "공부를 하다."), F("살이 찔까 봐 요즘 ___를 먹지 않습니다. (hamburgers)", "햄버거", ["소문", "여건"], "햄버거."), F("회사에서 해고될까 봐 ___이에요. (I am worried)", "걱정", ["사랑", "방학"], "걱정."),
           read_q("저도 졸업한 후에 취업을 못 할까 봐 걱정이 많이 됩니다"), read_q("퇴직금으로 사업을 하려고 하는데 실패할까 봐 무섭습니다"), read_q("살이 찔까 봐 걱정입니다"), read_q("실직할까 봐 매일 일찍 출근합니다"), read_q("부작용이 있을까 봐 성형수술을 하지 않았어요")]
    ),
)


# ================================================================== L9 Topic C
_C_TXT = [
    ("기자: 최근 허위 진단서를 제출해서 병역을 면제받은 운동선수가 경찰에 적발됐습니다.", "Reporter: Recently an athlete who submitted a false medical certificate and was exempted from military service was caught by the police."),
    ("또 얼마 전에는 정신질환이 있는 것처럼 속여 군대에 가지 않은 연예인이 구속된 사건도 있었습니다.", "Also, not long ago there was an incident in which an entertainer who deceived people as if he had a mental illness and did not go to the army was arrested."),
    ("안보가 무엇보다 중요한 한국에서 이와 같은 병역기피는 사회문제가 되고 있는데요.", "In Korea, where security is more important than anything, this kind of draft evasion is becoming a social problem."),
    ("이에 대한 시민의 의견을 들어 보겠습니다.", "Let us hear citizens’ opinions on this."),
    ("남자: 저는 작년 삼 월에 군대에서 제대하고 이번 학기에 복학한 학생입니다.", "Man: I am a student who was discharged from the army last March and returned to school this semester."),
    ("국방의 의무는 국민이 지켜야 할 가장 기본적인 의무라고 생각합니다.", "I think the duty of national defense is the most basic duty that the people must keep."),
    ("물론 대부분의 사람은 잘 지키지만 일부 병역 비리를 저지르는 사람들도 있는 것 같아요.", "Of course most people keep it well, but it seems there are also some people who commit military service corruption."),
    ("이를 막기 위해서 병무청에서는 징병 신체검사를 더 철저히 해야 합니다.", "To prevent this, the Military Manpower Administration should do the conscription physical examination more thoroughly."),
    ("그리고 비리에 대한 처벌도 더 강화되어야 하고요.", "And the punishment for corruption should also be strengthened more."),
    ("여자: 저는 군에 간 아들을 둔 주부예요.", "Woman: I am a housewife who has a son who has gone into the army."),
    ("제 생각에는 병역의무를 마친 사람에게 좀 더 많은 혜택을 주는 제도를 도입하면 좋을 것 같아요.", "In my opinion it would be good to introduce a system that gives more benefits to people who have completed their military service duty."),
    ("외국에서도 군대에 갔다 온 사람은 우대를 해 주잖아요.", "In foreign countries too, they give preferential treatment to people who have been to the army, you know."),
    ("학비도 지원해 주고 취업할 때도 유리하고요.", "They support tuition and it is also advantageous when getting a job."),
    ("나라를 지키기 위해 일한 군인이 보상을 받는 것은 당연하다고 생각해요.", "I think it is natural for soldiers who worked to protect the country to receive compensation."),
]
_C_WORDS = ["강화", "기피", "당연하다", "도입", "면제", "모병", "병무청", "병역", "보상", "비리", "속이다", "안보", "적발", "정신", "조작", "지키다", "징병(제)", "처벌", "철저히", "허위"]
_PRES_C = [["Using a false medical certificate (an athlete was exempted from service); pretending to have a mental illness (an entertainer); committing military service corruption", "A more thorough conscription physical examination by the Military Manpower Administration; stronger punishment for corruption; a system giving more benefits (tuition support, an advantage in getting a job) to those who completed their service"]]
L9 = lesson(
    "Ch 48 · Topic C: the duty of military service (병역의무)",
    "병역의무 · 병역기피 · 허위 진단서 · 병무청 · 징병 신체검사 · 처벌 · 혜택 · 보상",
    requires=[],
    cards=[
        card("Topic C: the duty of military service (병역의무)",
             "The following excerpt is from an interview about a current social issue. (The English is mine; the book gives none. 작년 3월 is 작년 삼 월; the quotation marks and the underlining of 저지르는, 더, 강화되어야 and the label 징병 in the book are left out.)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_C_WORDS)),
        card("한국에서는: military service in Korea",
             "In Korea, military service (군복무) is compulsory for able men. Therefore, all males, after graduating from high school and up to the age of 40, are required to take a physical examination for conscription. Depending on their overall health, men are put in active military service for 18 to 21 months or public service for 36 months. Men with serious health problems are exempt from the draft. Also, men with special circumstances (e.g., studying abroad) must get prior approval from the Military Manpower Administration (병무청) to postpone their service. While military service is considered an important civic duty, high-profile public officials, entertainers, and athletes exempted from the draft are often scrutinized by the media for the possibility of having avoided military service through illegal means.\n\nThe book’s useful website is the Military Manpower Administration (병무청)."),
        card("Presentation Study b: the table (mine)", "The book asks you to read Topic Presentation C and fill in the methods for avoiding the military draft and the methods for enforcing it. My answers:", tables=[table(["Methods for avoiding the military draft", "Methods for enforcing the military draft"], [list(r) for r in _PRES_C])]),
        card("Activities left out", "The SMART Board activities (a and c), the review with the teacher (d) and Follow-up 1 (a YTN news clip about avoiding the military draft, filling in the occupation of those avoiding the draft and how the draft was avoided) are audio and computer activities. The Sino-Korean note on 안보 is in the first lesson of the chapter."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT, k=3)
        + [M("What did the athlete do to be exempted from service?", "Submitted a false medical certificate", ["Moved abroad", "Paid a fine", "Became a teacher"], "허위 진단서."), M("What did the entertainer pretend?", "That he had a mental illness", ["That he was a student", "That he was abroad", "That he was a citizen elsewhere"], "정신질환이 있는 것처럼."), M("What is becoming a social problem in Korea?", "Draft evasion", ["Low wages", "Traffic", "School fees"], "병역기피."), M("When was the man discharged from the army?", "Last March", ["Last December", "This spring", "Two years ago"], "작년 삼 월."), M("What does the man say is the most basic duty of the people?", "The duty of national defense", ["Paying taxes", "Voting", "Studying"], "국방의 의무."), M("What does the man want the Military Manpower Administration to do?", "Do the physical examination more thoroughly", ["Close its offices", "Lower the age", "Shorten service"], "더 철저히."), M("What else does the man want?", "Stronger punishment for corruption", ["Higher pay", "Fewer exams", "More holidays"], "처벌 강화."), M("What does the woman want to introduce?", "A system giving more benefits to those who completed service", ["A volunteer army", "A longer service", "A new exam"], "혜택을 주는 제도."), M("What kinds of support does she mention?", "Tuition support and an advantage in job-hunting", ["Free housing", "Free meals", "Free travel"], "학비, 취업."), M("How long is active military service in Korea, according to the book?", "18 to 21 months", ["6 months", "36 months", "5 years"], "한국에서는."), M("How long is public service in Korea, according to the book?", "36 months", ["18 months", "21 months", "12 months"], "한국에서는."), M("Who must approve postponing service for men studying abroad?", "The Military Manpower Administration (병무청)", ["The police", "The Ministry of Education", "A university"], "병무청."),
           F("허위 ___서를 제출해서 병역을 면제받았다. (medical certificate)", "진단", ["소문", "여건"], "진단서."), F("병역 ___를 저지르는 사람들도 있다. (corruption)", "비리", ["보상", "도입"], "비리."), F("병무청은 신체검사를 더 ___ 해야 합니다. (thoroughly)", "철저히", ["당연히", "허위로"], "철저히."), F("비리에 대한 ___이 강화되어야 합니다. (punishment)", "처벌", ["보상", "도입"], "처벌."), F("나라를 ___ 위해 일한 군인이 보상을 받는 것은 당연하다. (to protect)", "지키기", ["속이기", "면제하기"], "지키다."),
           read_q("허위 진단서를 제출해서 병역을 면제받았습니다"), read_q("병역기피는 사회문제가 되고 있습니다"), read_q("국방의 의무는 가장 기본적인 의무입니다"), read_q("비리에 대한 처벌이 강화되어야 합니다"), read_q("군인이 보상을 받는 것은 당연합니다")]
    ),
)

# ================================================================== L10 Follow-up 2 and Activity 1
_YU = [
    ("미국 시민권 취득에 따른 병역 기피 의혹으로 입국이 금지된 가수 유승준(미국명 스티브 승준 유, 마흔세 살) 씨가 이십여 년 만에 한국에 올 수 있게 되었습니다.", "Singer Yoo Seung-jun (American name Steve Seung-jun Yoo, 43), who was banned from entering because of suspicion of draft evasion through acquiring American citizenship, has become able to come to Korea after some twenty years."),
    ("이에 따라 유 씨의 입국에 대한 찬반 논란이 커지고 있습니다.", "Accordingly, the pro-and-con controversy over Mr. Yoo’s entry is growing."),
    ("한국에서 태어났지만, 미국 영주권이 있던 유승준 씨는 천구백구십칠 년 사 월 한국에서 가수로 데뷔했습니다.", "Although born in Korea, Mr. Yoo Seung-jun, who had a U.S. green card, debuted as a singer in Korea in April 1997."),
    ("유 씨는 가위, 나나나, 열정 등 히트곡을 내며 최고의 댄스 가수로 사랑을 받았습니다.", "Mr. Yoo had hit songs such as Scissors, Nanana and Passion, and was loved as the best dance singer."),
    ("유 씨는 한국의 병역법에 따라 징병 신체검사를 받았고, 검사 결과에 따라 공익근무요원이 될 예정이었습니다.", "Under Korea’s Military Service Act, Mr. Yoo took the conscription physical examination, and according to the result he was scheduled to become a public service worker."),
    ("하지만 이천이 년 일 월, 유 씨는 미국으로 건너가 한국 국적을 갑자기 포기하고 미국 시민권을 취득함으로써 병역을 기피했다는 비난을 받았습니다.", "But in January 2002, Mr. Yoo went over to the United States, suddenly gave up his Korean nationality and acquired American citizenship, and so was criticized for having evaded military service."),
    ("이천이 년 법무부로부터 한국 입국을 제한당했던 유 씨는 이천십오 년 구 월 재외동포 비자(에프 사)로 입국하도록 해 달라고 신청했지만 거부당했고, 이후 이를 취소해 달라는 소송을 계속 제기해 왔습니다.", "Mr. Yoo, whose entry into Korea was restricted by the Ministry of Justice in 2002, applied in September 2015 to be allowed to enter on an overseas Korean visa (F-4) but was refused, and since then has continued to file lawsuits asking for this to be cancelled."),
    ("그러다 최근 고등법원이 유 씨에게 승소 판결을 내렸고, 이에 따라 유 씨는 재외동포로 한국에 입국해 가수 활동을 다시 할 수 있는 길이 열리게 되었습니다.", "Then recently the high court gave Mr. Yoo a winning verdict, and accordingly a way opened for Mr. Yoo to enter Korea as an overseas Korean and resume his activities as a singer."),
    ("이번 판결로 유 씨의 한국 입국에 대해 찬반 여론이 뜨거워지고 있습니다.", "With this ruling, pro-and-con public opinion on Mr. Yoo’s entry into Korea is heating up."),
    ("여러분께서는 유승준 씨의 한국 입국에 대해 어떻게 생각하십니까?", "What do you think about Mr. Yoo Seung-jun’s entry into Korea?"),
]
_YU_T = [["Born in Korea but held a U.S. green card; debuted as a singer in April 1997; hit songs such as 가위, 나나나 and 열정; loved as the best dance singer; took the conscription physical exam and was to become a public service worker; in January 2002 went to the U.S., gave up Korean nationality and acquired American citizenship", "Suspicion and criticism of draft evasion by acquiring U.S. citizenship; entry restricted by the Ministry of Justice in 2002", "In September 2015 he applied for an overseas Korean visa (F-4) and was refused; he kept filing lawsuits to cancel the refusal; recently the high court ruled for him, opening the way for him to enter Korea as an overseas Korean and sing again; pro-and-con opinion heated up"]]
_MIL1 = [("군 복무가 의무이기 때문에 일정 기간 군대에서 복무해야 한다.", "Because military service is a duty, one must serve in the army for a certain period.", "징병제"), ("종교적인 이유 등으로 군 복무를 할 수 없을 때 복무기간 동안 사회봉사 활동 등을 한다.", "When one cannot do military service for reasons such as religion, one does community service and the like during the service period.", "대체복무"), ("군 복무가 의무가 아니기 때문에 군대에 입대하고 싶은 사람만 지원한다.", "Because military service is not a duty, only people who want to enlist in the army apply.", "모병제"), ("군 복무를 피하려고 불법적인 방법을 사용한다. 돈을 주어서 신체검사 결과를 조작하기도 한다.", "One uses illegal methods to avoid military service. One even gives money to manipulate the physical examination result.", "병역비리"), ("군 복무를 마친 남성에게 공무원시험에서 일정한 점수를 추가로 준다.", "Men who completed military service are given certain additional points in the civil service exam.", "군 가산점제")]
_MIL2 = [("정하나 씨는 어렸을 때부터 여군장교가 되는 것이 꿈이었습니다. 그래서 올해 간호대학을 졸업하면 간호장교로 군대에 지원해서 직업군인으로서 군대에서 계속 근무할 계획입니다.", "Ms. Jeong Ha-na has dreamed since childhood of becoming a female military officer. So when she graduates from nursing college this year she plans to apply to the army as a nurse officer and continue serving as a career soldier.", "모병제"), ("김수민 씨는 군 복무를 마친 후 몇 년 전에 공무원시험에 합격했어요. 그 시험에는 만 명이 지원했는데 백오십 명만 뽑았기 때문에 경쟁률이 아주 높았습니다. 다행히 그때는 군 복무를 마친 사람에게는 오 퍼센트의 점수를 더 주었기 때문에, 김수민 씨한테는 많은 도움이 되었습니다.", "Mr. Kim Su-min passed the civil service exam a few years ago after finishing military service. Ten thousand people applied for that exam but only 150 were chosen, so the competition rate was very high. Fortunately, at that time people who had finished military service were given 5 percent more points, so it helped Mr. Kim Su-min a lot.", "군 가산점제"), ("올해 대학교 사 학년인 정재훈 씨는 졸업하기 전에 군 복무를 마치고 싶어합니다. 군 복무는 한국의 모든 남자에게는 의무이기 때문입니다. 게다가 현재 경제사정도 좋지 않기 때문에 올해 가을부터 휴학하고 군에 입대할 계획입니다.", "Mr. Jeong Jae-hun, a fourth-year university student this year, wants to finish military service before graduating. This is because military service is a duty for all men in Korea. Besides, the current economic situation is not good either, so he plans to take leave from school from this fall and enlist in the army.", "징병제")]
L10 = lesson(
    "Ch 48 · Follow-up and activities C: Yoo Seung-jun, military terms and cases",
    "유승준 · 병역 · 징병제 · 모병제 · 대체복무 · 병역비리 · 군 가산점제 · 재외동포 비자",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): the entertainer 유승준",
             "The following article is about a Korean-American entertainer, 유승준 (Yonhap News). The book asks you to fill in a table in English (his biography; the reasons why he was not allowed to enter Korea; what happened after the initial denial of entry). The text is the book’s with the numbers spelled out (43 is 마흔세 살 in the text, as an age; 20여 년 is 이십여 년; 1997년 4월 is 천구백구십칠 년 사 월; 2002년 1월 is 이천이 년 일 월; 2015년 9월 is 이천십오 년 구 월; F-4 is 에프 사); the quotation marks are removed. The book glosses 취득하다: to acquire; 논란: controversy; 영주권: a green card; 비난: criticism; 거부: refusal. The English is mine.",
             examples=passage(_YU)),
        card("Follow-up 2 answered (mine)", "", tables=[table(["Biography of 유승준", "Reason(s) why he was not allowed to enter Korea", "What happened after the initial denial"], [list(r) for r in _YU_T])]),
        card("Activity 1 a (Reading): military service terms",
             "The following descriptions are about military service. The book asks you to find, from the word box, what each is about: 병역비리, 모병제, 징병제, 대체복무, 군 가산점제. The sentences are the book’s; the English and the answers are mine.",
             tables=[table(["Description", "Answer (mine)"], [[a, c] for a, b, c in _MIL1], say=[0, 1]), table(["English of the description (mine)"], [[b] for a, b, c in _MIL1])]),
        card("Activity 1 b (Reading): cases",
             "The book asks you to read cases about military service and write which term from the box each is. The cases are the book’s with the numbers spelled out (10,000명 is 만 명, 150명 is 백오십 명, 5퍼센트 is 오 퍼센트, 4학년 is 사 학년); the English and the answers are mine.",
             tables=[table(["Case", "Answer (mine)"], [[a, c] for a, b, c in _MIL2], say=[0, 1]), table(["English of the case (mine)"], [[b] for a, b, c in _MIL2])]),
        card("Activities left out", "Activity 2 (a rerecorded YTN news item about crimes, filling in the type of crime, the persons involved and the jail sentence), Activity 3 (a rerecorded radio news report about a survey, summarized in English) and Activity 4 (reading articles about the military draft system and volunteer military system in different countries and exchanging the findings in pairs, writing a summary in the class notebook and presenting; the articles are not printed in the student text) are audio, pair and group activities."),
    ],
    exercises=uniq(
        _tr(_YU, k=3) + _tr([(a, c) for a, b, c in _MIL1], k=3) + _tr([(a, b) for a, b, c in _MIL1], k=3)
        + [M("Why was 유승준 banned from entering Korea?", "Suspicion of draft evasion through acquiring U.S. citizenship", ["A crime abroad", "An unpaid tax", "A visa fee"], "병역 기피 의혹."), M("When did he debut as a singer in Korea?", "April 1997", ["January 2002", "September 2015", "April 2015"], "천구백구십칠 년 사 월."), M("What was he scheduled to become after the physical exam?", "A public service worker", ["A career soldier", "An officer", "A police officer"], "공익근무요원."), M("What did he do in January 2002?", "Went to the U.S. and acquired citizenship", ["Joined the army", "Debuted", "Applied for a visa"], "이천이 년 일 월."), M("What did he apply for in September 2015?", "An overseas Korean visa (F-4)", ["A work permit", "A student visa", "A tourist visa"], "재외동포 비자."), M("What was the result of that application?", "It was refused", ["It was approved", "It was ignored", "It was delayed"], "거부당했고."), M("What did the high court do recently?", "Ruled in his favor", ["Ruled against him", "Dropped the case", "Postponed"], "승소 판결."), M("Which term means the system in which only those who want to enlist apply?", "모병제", ["징병제", "대체복무", "병역비리"], "군 복무가 의무가 아니기 때문에."), M("Which term means conscription?", "징병제", ["모병제", "대체복무", "군 가산점제"], "군 복무가 의무."), M("Which term means alternative service such as community service?", "대체복무", ["징병제", "모병제", "병역비리"], "사회봉사."), M("Which term means illegal methods to avoid service?", "병역비리", ["대체복무", "모병제", "군 가산점제"], "불법적인 방법."), M("Which term means extra points on the civil service exam for those who served?", "군 가산점제", ["병역비리", "징병제", "모병제"], "추가로 점수."), M("Which term fits 정하나 씨, who plans to serve as a career soldier by choice?", "모병제", ["징병제", "병역비리", "대체복무"], "직업군인."), M("Which term fits 정재훈 씨, who must serve as a duty for all men?", "징병제", ["모병제", "군 가산점제", "대체복무"], "의무."), M("Which term fits 김수민 씨, who got 5 percent more points?", "군 가산점제", ["징병제", "모병제", "병역비리"], "5퍼센트의 점수."),
           F("군 복무가 의무인 제도를 ___라고 합니다. (conscription system)", "징병제", ["모병제", "대체복무"], "징병제."), F("군대에 가고 싶은 사람만 지원하는 제도는 ___입니다. (volunteer system)", "모병제", ["징병제", "병역비리"], "모병제."), F("종교적인 이유로 군 복무를 못 하면 ___를 합니다. (alternative service)", "대체복무", ["징병제", "모병제"], "대체복무."), F("돈을 주어 신체검사 결과를 조작하는 것은 ___입니다. (military service corruption)", "병역비리", ["대체복무", "모병제"], "병역비리."), F("유 씨는 미국 시민권을 ___해서 병역을 기피했다는 비난을 받았다. (acquire)", "취득", ["거부", "면제"], "취득."),
           read_q("유승준 씨는 미국 시민권을 취득했습니다"), read_q("군 복무가 의무인 제도는 징병제입니다"), read_q("모병제는 지원한 사람만 군대에 갑니다"), read_q("대체복무는 사회봉사 활동 등을 합니다"), read_q("병역비리는 불법적인 방법을 사용하는 것입니다")]
    ),
)

# ================================================================== L11 Summary of irregular verbs
_IRR = {
    "ㄹ": ("When the verb stem is followed by ㄴ, ㅂ, or ㅅ, ㄹ is dropped.", ["알다", "살다", "열다", "졸다", "돌다", "말다", "놀다", "떠들다", "만들다", "벌다", "멀다", "길다"], [("지금 사는 집이 넓어요.", "The house I live in now is spacious."), ("아침에 오면 교실 문을 엽니다.", "When I come in the morning, I open the classroom door."), ("돈을 얼마나 버세요?", "How much money do you earn?"), ("긴 치마를 사고 싶은데 없어요.", "I want to buy a long skirt, but there is none.")]),
    "ㅂ": ("When the verb stem is followed by a vowel, ㅂ is dropped and 우 + 어 is added.", ["굽다(to bake)", "눕다", "춥다", "덥다", "쉽다", "어렵다", "맵다", "싱겁다", "반갑다", "고맙다", "더럽다", "즐겁다", "아쉽다", "아름답다", "곱다", "돕다"], [("숙제 좀 도와주세요.", "Please help me with the homework a little."), ("피곤해서 누워서 쉬고 있어요.", "I am tired, so I am lying down and resting."), ("공부가 어려워요.", "Studying is difficult."), ("방이 너무 더러워서 청소했어요.", "The room was so dirty that I cleaned it.")]),
    "ㄷ": ("When the verb stem is followed by a vowel, ㄷ changes to ㄹ.", ["걷다", "묻다(to ask)", "듣다", "싣다"], [("빨리 걸어서 숨이 차요.", "I walked fast, so I am out of breath."), ("친구에게 물어봤어요.", "I asked a friend.")]),
    "르": ("When the verb stem is followed by a vowel, ㅡ is dropped from 르, ㄹ moves to the bottom of the preceding syllable, and 라 or 러 is added.", ["고르다", "모르다", "부르다", "자르다", "누르다", "기르다", "오르다", "바르다", "머무르다", "지르다", "서투르다", "배부르다", "마르다"], [("한번 골라 보세요.", "Please try choosing one."), ("답을 몰라서 못 적었어요.", "I did not know the answer, so I could not write it."), ("많이 먹어서 배가 불러요.", "I ate a lot, so I am full."), ("목이 말라서 죽겠어요.", "I am dying of thirst.")]),
    "ㅎ": ("When the verb stem is followed by a vowel or by the consonant ㄴ or ㄹ, ㅎ is dropped.", ["빨갛다", "파랗다", "노랗다", "하얗다", "까맣다", "이렇다", "그렇다", "저렇다", "어떻다"], [("빨간 스웨터가 잘 어울려요.", "The red sweater suits you well."), ("가을 하늘이 파래요.", "The autumn sky is blue."), ("이 모자 어때요?", "How is this hat?"), ("저도 그럴 생각이에요.", "I am thinking so too.")]),
    "ㅅ": ("When the verb stem is followed by a vowel, ㅅ is dropped.", ["낫다", "붓다", "짓다", "젓다", "잇다(to connect)", "긋다(to draw a line)"], [("쉬니까 병이 다 나았어요.", "I rested, so the illness is all gone."), ("손이 자꾸 부어서 큰일이에요.", "My hand keeps swelling, so it is a big problem.")]),
}
_EXC = {
    "ㅂ": (["입다", "잡다", "좁다", "굽다(to be bent)"], [("옷을 입으세요.", "Please put on clothes."), ("길이 좁으니까 조심하세요.", "The road is narrow, so please be careful.")]),
    "ㄷ": (["믿다", "받다", "닫다", "묻다(to bury)"], [("선물을 받았어요.", "I received a present."), ("문을 닫으세요.", "Please close the door.")]),
    "르": (["따르다"], [("선생님을 따라해 보세요.", "Please try following the teacher.")]),
    "ㅎ": (["좋다", "많다", "넣다", "낳다", "싫다", "괜찮다", "쌓다"], [("이 책을 가방 안에 넣어 주세요.", "Please put this book inside the bag."), ("아픈 데는 괜찮아요?", "Is the sore spot okay?")]),
    "ㅅ": (["벗다", "씻다", "웃다", "빗다"], [("밥 먹기 전에 손을 씻으세요.", "Please wash your hands before eating."), ("사진 찍을 때 웃으세요.", "Please smile when you take a photo.")]),
}
_NOTE_B = "For the verbs 돕다 and 곱다, 오 + 아 is added (돕다 → 도와요, 곱다 → 고와요)."
_IRR_NOTE = {"ㅂ": "The book’s footnote: " + _NOTE_B}


def _irr_cards():
    out = []
    names = {"ㄹ": "1. ㄹ irregular verbs", "ㅂ": "2. ㅂ irregular verbs", "ㄷ": "3. ㄷ irregular verbs", "르": "4. 르 irregular verbs", "ㅎ": "5. ㅎ irregular verbs", "ㅅ": "6. ㅅ irregular verbs"}
    for k in ["ㄹ", "ㅂ", "ㄷ", "르", "ㅎ", "ㅅ"]:
        rule, verbs, ex = _IRR[k]
        body = "Condition/rule: " + rule + "\n\nVerbs: " + ", ".join(verbs) + "."
        if k in _EXC:
            body += "\n\nExceptions (these do not change): " + ", ".join(_EXC[k][0]) + "."
        if k in _IRR_NOTE:
            body += "\n\n" + _IRR_NOTE[k]
        body += "\n\nThe book’s examples (the English is mine):"
        exs = list(ex) + (list(_EXC[k][1]) if k in _EXC else [])
        out.append(card(names[k], body, examples=passage(exs)))
    return out


_ALLEX = [e for k in _IRR for e in _IRR[k][2]] + [e for k in _EXC for e in _EXC[k][1]]
L11 = lesson(
    "Ch 48 · Grammar in Focus: summary of irregular verbs",
    "불규칙 동사 · ㄹ 불규칙 · ㅂ 불규칙 · ㄷ 불규칙 · 르 불규칙 · ㅎ 불규칙 · ㅅ 불규칙",
    requires=[],
    cards=[
        card("Summary of Irregular Verbs",
             "So far you have learned several irregular verbs, such as ㄹ verbs, ㅂ verbs, ㄷ verbs, 르 verbs, ㅅ verbs, and ㅎ verbs. These verbs are called irregular verbs because they go through an extra step in conjugation under certain conditions. For example, ㅅ irregular verbs go through an extra step of dropping ㅅ when the verb stem is followed by a vowel, as in 붓 + 어요 → 부어요. The following cards summarize the irregular verbs you learned in previous chapters. (The verb lists are the book’s; where the book gives an English gloss in parentheses I keep it; a gloss inside a verb is not read aloud in the Hangul lists.)"),
    ] + _irr_cards() + [
        card("Activities left out", "Follow-up 1 (the teacher’s PowerPoint presentation), Follow-up 2 (six video clips from 옥탑방 고양이 and 호텔리어, transcribing the missing words, writing the verb stem and its meaning), Follow-up 3 (a Hankyoreh cartoon, 비빔툰 알듯 말듯한 즐거움, in which you circle the words conjugated from ㄹ/ㅂ/ㄷ/르/ㅅ/ㅎ verbs; the book’s three examples are 흐르다 [to flow], 듣다 [to listen] and 말다 [to stop, don’t]) and Follow-up 4 (a two-group game: the teacher reads a verb from a card set aloud and points to a student who makes a sentence with it; one point for a correct sentence, and the other group may correct a wrong one) are video, picture, game and group activities."),
    ],
    exercises=uniq(
        _tr(_ALLEX, k=3)
        + [M("What happens to ㄹ when the verb stem is followed by ㄴ, ㅂ, or ㅅ?", "It is dropped", ["It becomes ㄷ", "It is doubled", "It becomes 우"], "살다 → 사는."), M("What happens to ㅂ in ㅂ irregular verbs before a vowel?", "It is dropped and 우 + 어 is added", ["It becomes ㄹ", "It is doubled", "It becomes ㄴ"], "춥다 → 추워요."), M("What happens to ㄷ in ㄷ irregular verbs before a vowel?", "It changes to ㄹ", ["It is dropped", "It becomes ㅂ", "It is doubled"], "듣다 → 들어요."), M("What happens to the verb stem 르 before a vowel?", "ㅡ is dropped, ㄹ moves to the previous syllable, 라/러 is added", ["ㅂ is dropped", "ㄷ becomes ㄹ", "Nothing"], "모르다 → 몰라요."), M("What happens to ㅎ before a vowel or ㄴ/ㄹ?", "It is dropped", ["It becomes ㄹ", "It becomes ㅅ", "It is doubled"], "파랗다 → 파래요."), M("What happens to ㅅ before a vowel?", "It is dropped", ["It becomes ㄹ", "It becomes ㄷ", "It is doubled"], "붓다 → 부어요."), M("Which verb is an exception to the ㅂ rule?", "입다", ["춥다", "덥다", "쉽다"], "입다 → 입어요."), M("Which verb is an exception to the ㄷ rule?", "받다", ["걷다", "듣다", "싣다"], "받다 → 받아요."), M("Which verb is an exception to the 르 rule?", "따르다", ["모르다", "고르다", "부르다"], "따르다."), M("Which verb is an exception to the ㅎ rule?", "좋다", ["빨갛다", "파랗다", "그렇다"], "좋다 → 좋아요."), M("Which verb is an exception to the ㅅ rule?", "씻다", ["낫다", "붓다", "짓다"], "씻다 → 씻어요."), M("Which two ㅂ verbs take 오 + 아?", "돕다 and 곱다", ["춥다 and 덥다", "입다 and 잡다", "쉽다 and 맵다"], "The book’s footnote."), M("What does 묻다 mean when it follows the ㄷ rule?", "to ask", ["to bury", "to close", "to receive"], "물어봤어요."), M("What does 묻다 mean when it is an exception?", "to bury", ["to ask", "to listen", "to walk"], "묻다 (to bury)."), M("What does 굽다 mean when it is an exception to the ㅂ rule?", "to be bent", ["to bake", "to be cold", "to lie down"], "굽다 (to be bent)."), M("What does 굽다 mean when it follows the ㅂ rule?", "to bake", ["to be bent", "to be hot", "to help"], "굽다 (to bake)."),
           F("지금 ___ 집이 넓어요. (live; 살다)", "사는", ["살는", "삽는"], "ㄹ is dropped before ㄴ."), F("피곤해서 ___ 쉬고 있어요. (lie down; 눕다)", "누워서", ["눕어서", "눕아서"], "ㅂ → 우 + 어."), F("친구에게 ___. (asked; 묻다)", "물어봤어요", ["묻어봤어요", "문어봤어요"], "ㄷ → ㄹ."), F("많이 먹어서 배가 ___. (full; 부르다)", "불러요", ["부르어요", "불라요"], "르 irregular."), F("가을 하늘이 ___. (blue; 파랗다)", "파래요", ["파라요", "파랗어요"], "ㅎ is dropped."), F("쉬니까 병이 다 ___. (got well; 낫다)", "나았어요", ["낫았어요", "낮았어요"], "ㅅ is dropped."), F("선물을 ___. (received; 받다)", "받았어요", ["발았어요", "받랐어요"], "Exception: no change."), F("밥 먹기 전에 손을 ___. (wash; 씻다)", "씻으세요", ["씨으세요", "씻흐세요"], "Exception: no change."),
           read_q("지금 사는 집이 넓어요"), read_q("숙제 좀 도와주세요"), read_q("친구에게 물어봤어요"), read_q("한번 골라 보세요"), read_q("가을 하늘이 파래요")]
    ),
)


# ================================================================== L12 Activities + self-evaluation
_OP = [("성형수술의 부작용이 있을까 봐 걱정이에요.", "I am worried that there might be side effects of cosmetic surgery."), ("불경기에 실직할까 봐 저축을 많이 했어요.", "Afraid of losing my job in the recession, I saved a lot."), ("병역비리를 저지른 사람은 처벌을 받아야 합니다.", "A person who committed military service corruption must receive punishment."), ("그 병원에서는 쌍꺼풀 수술을 한 사람에게 증명서를 줍니다.", "That hospital gives a certificate to people who had double eyelid surgery."), ("안보가 중요하기 때문에 병무청에서는 신체검사를 철저히 합니다.", "Because security is important, the Military Manpower Administration does the physical examination thoroughly.")]
L12 = lesson(
    "Ch 48 · Activities and self-evaluation",
    "사회 문제 · 성형수술 · 실직 · 병역 · 자기 평가 · 연습 문장",
    requires=[],
    cards=[
        card("More practice sentences (mine)", "Sample sentences of my own that combine the chapter’s grammar with its vocabulary (the English is mine):", examples=passage(_OP)),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so that they can provide other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify, talk about, and express opinions about issues and incidents concerning cosmetic surgery and its popularity in Korea; identify and talk about the issues related to employment, unemployment, layoffs, downsizing, and restructuring; and identify and discuss issues concerning military service in Korea.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the conjunctive ending –(으)ㄹ까 봐(서) (being afraid that [something] might …); a summary of irregular verbs; and the Sino-Korean syllables within 성형수술 (成形手術), 실직 (失職), and 안보 (安保)."),
        card("Activities left out", "The chapter’s Activities pages (the military-term descriptions and cases, the business Q&A and the word-box descriptions are in the earlier lessons) also hold SMART Board activities, video and listening activities (a campus episode, interviews with people who lost their jobs, a news item about crimes, a radio report about a survey) and pair or group tasks (a debate on cosmetic surgery, a comparison of military systems in different countries). They are audio, video, computer and group activities and are left out."),
    ],
    exercises=uniq(
        _tr(_OP, k=3)
        + [M("What should you do if you tick “No” in the self-evaluation?", "Review on your own, study with a partner, tell your advisor or team leader", ["Skip it", "Retake the course", "Nothing"], "The book’s advice."), M("What does 불경기에 실직할까 봐 저축을 많이 했어요 mean?", "Afraid of losing my job in the recession, I saved a lot", ["I lost my job", "I spent a lot", "The recession ended"], "–ㄹ까 봐."), M("What does 병역비리를 저지른 사람은 처벌을 받아야 합니다 mean?", "A person who committed military service corruption must be punished", ["Such a person is rewarded", "Such a person is exempt", "Such a person is a hero"], "처벌."), M("What does 성형수술의 부작용이 있을까 봐 걱정이에요 mean?", "I am worried there might be side effects of cosmetic surgery", ["I had surgery", "I am happy", "Surgery is free"], "부작용."),
           F("성형수술의 부작용이 있을___ 봐 걱정이에요. (might)", "까", ["서", "고"], "–ㄹ까 봐."), F("안보가 중요하기 때문에 신체검사를 ___ 합니다. (thoroughly)", "철저히", ["허위로", "당연히"], "철저히."), F("병역비리를 저지른 사람은 ___을 받아야 합니다. (punishment)", "처벌", ["보상", "도입"], "처벌."),
           read_q("성형수술의 부작용이 있을까 봐 걱정이에요"), read_q("불경기에 실직할까 봐 저축을 많이 했어요"), read_q("병역비리를 저지른 사람은 처벌을 받아야 합니다"), read_q("그 병원에서는 쌍꺼풀 수술을 한 사람에게 증명서를 줍니다"), read_q("안보가 중요하기 때문에 신체검사를 철저히 합니다")]
    ),
)

# ================================================================== L13 core vocabulary
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/") and " " not in r[0]]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0] and "…" not in r[0] and "–" not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L13 = lesson(
    "Ch 48 · Core vocabulary",
    "주요 단어 · 성형수술 · 불경기 · 병역 · 까 봐",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. The last section lists the Sino-Korean related words of 성형수술, 실직 and 안보 as the book gives them.\n\n"
             "The example sentences with digits and letters are respelled in Hangul where they are spoken."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 외모 mean?", "outward appearance", ["a response", "a dispute", "a rumor"], "外貌."), M("What does 부작용 mean?", "side effects", ["a dispute", "a response", "a request"], "副作用."), M("What does 분쟁 mean?", "a dispute", ["a request", "a response", "a trend"], "紛爭."), M("What does 해고 mean?", "dismissal; a layoff", ["a hiring", "a promotion", "a rumor"], "解雇."), M("What does 병역 mean?", "military service", ["a medical exam", "a dispute", "a holiday"], "兵役."), M("What does 징병 mean?", "conscription", ["recruiting soldiers", "a pardon", "a salary"], "徵兵."), M("What does 모병 mean?", "recruiting soldiers", ["conscription", "a layoff", "a rumor"], "募兵."), M("What does 처벌 mean?", "punishment", ["reward", "a request", "a response"], "處罰."),
           F("그 병원에서 ___ 수술을 했어요. (double eyelid)", "쌍꺼풀", ["주근깨", "치아"], "쌍꺼풀."), F("불경기 때문에 ___하는 가게가 많아요. (closing down)", "폐업", ["고용", "권유"], "폐업."), F("남자는 ___의무를 다해야 합니다. (military service)", "병역", ["고용", "급여"], "병역."), F("회사에서 ___를 하면 직원들이 해고될 수 있어요. (restructuring)", "구조조정", ["병무청", "미백"], "구조조정."), F("병무청에서는 신체검사를 ___ 해야 합니다. (thoroughly)", "철저히", ["허위로", "당연히"], "철저히."),
           read_q("주요 단어"), read_q("외모"), read_q("구조조정"), read_q("병역"), read_q("철저히")]
    ),
)

UNIT = unit("Semester 2 · Unit 12 · Chapter 48: Social Issues II (사회 문제 2)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])

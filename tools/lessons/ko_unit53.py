"""Unit 53: KBC Semester 2, Unit 12, Chapter 46 - Politics (정치).
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

# ---- the core vocabulary of Chapter 46 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("가리키다", "to point to; to denote; to mean", "손가락으로 상대방을 가리키면 안 됩니다."),
    ("구성", "(構成) formation; composition; makeup (to form; to compose/to be composed of; to be made up of) (~하다/되다)", "이 문법책은 모두 이십팔 과로 구성되어 있습니다."),
    ("국무", "(國務) state affairs; “nation’s duties”", "내일 오전 열 시에 청와대 회의실에서 국무회의가 열릴 예정입니다."),
    ("국방", "(國防) national defense", "한국에 있는 미군은 한국의 국방에 대단히 중요한 역할을 한다."),
    ("권한/~권", "(權限/權) authority; rights; jurisdiction; power", "회원으로 가입하지 않으면 이 웹사이트의 정보를 사용할 권한이 없습니다."),
    ("기획", "(企劃) planning; designing (to plan/to be planned) (~하다/되다)", "전쟁 기념관에서 기획하는 특별 전시회가 열립니다."),
    ("대통령", "(大統領) the president (of a country); “big governing”", "대한민국의 첫 번째 대통령은 이승만 대통령이다."),
    ("맡다", "to take charge of; to have custody of", "각자 맡은 일을 열심히 하세요."),
    ("민주주의", "(民主主義) democracy", "민주주의를 지키기 위해 끝까지 싸우겠습니다."),
    ("보건", "(保健) health; “preservation of health”", "신종 플루에 걸리지 않으려면 손을 씻는 등 보건위생에 신경 써야 합니다."),
    ("~부", "(府) a branch of government; “government office”", "오바마 행정부는 환경보호를 위해 대규모 그린 운동을 벌이겠다고 밝혔다."),
    ("사법", "(司法) the administration of justice", "다음 주에 사법시험 최종 합격자를 대상으로 면접이 있을 예정입니다."),
    ("외교", "(外交) diplomacy; foreign affairs; “outside relationship”", "한반도를 중심으로 미국, 중국, 일본, 러시아의 복잡한 외교 관계가 발생한다."),
    ("임명", "(任命) an appointment; a nomination; designation (to appoint/to be appointed) (~하다/되다)", "이번에 새로 연방대법원 판사로 임명된 사람에 대해서 아세요?"),
    ("입법", "(立法) legislation; lawmaking; “establishing law”", "정부가 계획하는 입법을 시민단체들이 반대하고 있습니다."),
    ("장관", "(長官) a cabinet minister; a secretary", "행정 각 부 장관들이 모여 비상사태에 대해 논의 중입니다."),
    ("재정", "(財政) finances; financial affairs", "지방 정부의 재정이 갈수록 나빠지고 있습니다."),
    ("정책", "(政策) a policy", "경제 상황에 맞는 바람직한 정책을 세우는 것이 중요합니다."),
    ("지휘", "(指揮) commands; orders; conducting; “giving orders with fingers” (to command; to order; to conduct) (~하다)", "중대장의 지휘 아래 모든 사병이 훈련을 하고 있습니다."),
    ("총리", "(總理) the premier; the prime minister", "다음 주에 태국 총리가 한국을 방문할 예정입니다."),
    ("통상", "(通商) commerce; trade; commercial relations", "한국과 중국의 통상이 크게 증가하고 있다."),
    ("행정", "(行政) administration", "졸업 후 행정 대학원에 진학하고 싶어요."),
]
_CV_B = [
    ("감시", "(監視) watch; guard; lookout; vigil; surveillance (to watch/to be watched) (~하다/받다)", "범인이 도망가지 못하게 경찰이 감시하고 있습니다."),
    ("개표", "(開票) the counting of votes; “opening a ballot” (to open the ballots) (~하다)", "이번 선거부터는 빠른 개표를 위해 자동 개표기를 쓰기로 결정했습니다."),
    ("공정하다", "(公正) to be fair; to be just; to be impartial", "깨끗하고 공정한 선거문화를 만들어 나갑니다."),
    ("국회", "(國會) the National Assembly; congress; “national meeting”", "한국의 국회는 서울 여의도에 있습니다."),
    ("낙선", "(落選) defeat in an election; failure in an election; “fall from a selection” (to lose an election) (~하다)", "유월 이 일 지방선거에서 전 경기도 도지사 김문일 후보가 낙선하였습니다."),
    ("단임(제)", "(單任(制)) the single-term system; “single-appointment system”", "한국의 대통령은 오 년 단임제이어서 재임은 불가능합니다."),
    ("단체장", "(團體長) head of the local government", "이번 선거에서는 지방 자치 단체장도 뽑습니다."),
    ("당선", "(當選) winning an election; being elected (to elect/to be elected) (~시키다/되다)", "민주평화당의 강금희 후보가 여성 최초로 서울 시장에 당선되었습니다."),
    ("도지사", "(道知事) the governor of a province", "한국에는 아홉 명의 도지사가 있습니다. 도지사 선거는 사 년마다 있습니다."),
    ("발표", "(發表) an announcement (to announce/to be announced) (~하다/되다)", "정부는 환경오염 방지를 위한 대책을 발표하였습니다."),
    ("보궐선거", "(補闕選擧) a special election; a by-election", "서울시장이 선거법 위반으로 구속돼 보궐선거를 해야 합니다."),
    ("선거", "(選擧) an election (to elect; to vote for) (~하다)", "내일 과천대학교에서 총학생회장 선거가 있습니다."),
    ("연임", "(連任) serving consecutive terms; reappointment; “consecutive appointment” (to serve consecutive terms/to be reelected) (~하다/되다)", "분당대학교의 총장이 일을 잘해서 연임되었습니다."),
    ("원칙", "(原則) a fundamental rule; a (guiding) principle; “original rule”", "원칙을 지키는 것이 정치인들의 기본이 되어야 합니다."),
    ("유세", "(遊說) stumping; a canvassing tour; a campaign (to go canvassing) (~하다)", "대통령 후보들이 전국적으로 유세활동을 벌이고 있습니다."),
    ("유권자", "(有權者) an elector; a voter; “person with a right (to vote)”", "이번 지방 선거는 유권자들의 관심을 끌지 못하고 있습니다."),
    ("의원", "(議員) a member of the national assembly; a congressmember", "이번 선거에서 야당 의원이 많이 당선되었어요."),
    ("임기", "(任期) a term of office; “appointment term”", "지방 자치 단체의 시, 도의원은 사 년이 임기입니다."),
    ("재임", "(再任) serving a second term (to serve a second term/to be reappointed) (~하다/되다)", "국무총리에 김진표 씨가 재임되었습니다."),
    ("절차", "(節次) a process", "많은 행정절차가 간소화되었습니다."),
    ("정당", "(政黨) a political party", "미국의 대표적인 정당은 공화당과 민주당이다."),
    ("정치", "(政治) politics; “political governing”", "정부가 정치를 잘하면 사람들의 삶을 긍정적으로 바꿀 수 있다."),
    ("지방자치", "(地方自治) local autonomy; “local self-governing”", "한국의 지방자치 역사는 비교적 짧다."),
    ("지지", "(支持) support; backing; espousal (to support/to be supported) (~하다/받다)", "정부의 부동산 대책을 많은 시민들이 지지하고 있습니다."),
    ("총선(거)", "(總選(擧)) a general election", "한국의 총선은 사 년마다 있습니다. 총선에서는 국회의원을 뽑습니다."),
    ("투명하다", "(透明) to be transparent", "강물이 맑고 투명해서 바닥까지 볼 수 있다."),
    ("투표", "(投票) voting; ballot; poll; “throwing a ballot” (to vote) (~하다)", "내일은 총선일입니다. 자신의 한 표를 포기하지 말고 투표하시기 바랍니다."),
    ("후보(자)", "(候補(者)) a candidate", "이번 대통령 선거에는 아홉 명의 후보자가 등록을 마쳤습니다."),
]
_CV_C = [
    ("검찰(청)", "(檢察(廳)) public prosecutors (office); “prosecutors (bureau)”", "광주지방검찰청은 불법 선거운동을 한 김 모 씨를 구속했습니다."),
    ("고소", "(告訴) a complaint; an accusation; a legal action (to accuse/to be accused) (~하다/당하다)", "부동산 사기 피해자들이 부동산업자를 사기 혐의로 고소했습니다."),
    ("기소", "(起訴) prosecution; indictment (to prosecute/to be prosecuted) (~하다/되다)", "선거법 위반 혐의로 기소된 전 서울시장이 검찰에서 조사를 받고 집으로 돌아갔습니다."),
    ("무죄", "(無罪) innocence; not guilty; “no fault”", "강도 혐의로 체포되었던 정 모 씨가 무죄로 밝혀졌습니다."),
    ("민사", "(民事) civil (i.e. as opposed to criminal)", "앞으로 민사 사건 관련 서류를 인터넷으로 제출할 수 있게 됩니다."),
    ("배상", "(賠償) compensation (to compensate/to be compensated) (~하다/받다)", "자연재해로 인한 피해 보상을 정부가 해 주기로 했다."),
    ("법원", "(法院) a court of justice; a courthouse", "가정법원에 가서 이혼을 신청했습니다."),
    ("선고", "(宣告) a verdict; an announcement (to sentence/to be sentenced) (~하다/받다)", "지방법원에서 징역 삼 년 형을 선고받았던 사람이 고등법원에서는 무죄를 선고받았습니다."),
    ("소송", "(訴訟) a lawsuit; an action in law (to file a lawsuit) (~하다)", "민사 소송에 대해서 문의하고 싶으시면 일 번을 눌러 주세요."),
    ("~심(리)", "(審(理)) a trial; a hearing", "지방법원에서 열린 일 심의 결과가 마음에 들지 않아요. 다시 재판을 받고 싶어요."),
    ("원고", "(原告) a plaintiff; an accuser", "오늘 원고가 건강이 안 좋아서 법원에 나오지 못했습니다."),
    ("제기", "(提起) submitting (a case to the court); bringing (an action against a person); raising (a question) (to submit/to be submitted) (~하다/되다)", "반도체 공장 노동자들이 집단으로 소송을 제기했습니다."),
    ("집행유예", "(執行猶豫) probation; a suspended sentence", "음주운전으로 배우 조 모 씨가 집행유예를 선고받았습니다."),
    ("유죄", "(有罪) guiltiness; guilt", "에스 그룹 회장이 유죄를 선고받았어요."),
    ("재판", "(裁判) a trial (to have a trial/to be on trial) (~하다/받다)", "곧 재판이 시작되겠으니 모두 자리에 앉아 주십시오."),
    ("징역", "(懲役) imprisonment (with hard labor)", "차량 절도 혐의로 구속된 연예인 정 모 씨가 징역 삼 년을 선고받았습니다."),
    ("판결", "(判決) judgment; a judicial decision (to rule; to judge) (~하다)", "판사가 무죄판결을 내렸습니다."),
    ("피고(인)", "(被告(人)) a defendant (in a civil case); the accused (in a criminal case)", "대법원에서 은행 강도 혐의로 구속된 피고에게 징역 십 년 형을 선고했습니다."),
    ("항소", "(抗訴) an appeal (to an appellate court) (to appeal) (~하다)", "지방법원의 소송 결과에 만족하지 않아서 고등법원에 항소하려고 합니다."),
    ("(~)형", "(刑) a penalty; a punishment (for a crime)", "속도위반으로 벌금형을 받았습니다."),
    ("형사", "(刑事) criminal (i.e. as opposed to civil)", "살인범에 대한 형사 재판이 이번 주에 열립니다."),
    ("확정", "(確定) a decision; a settlement (to decide; to settle/to be decided; to be settled) (~하다/되다)", "대법원에서 일 심과 이 심의 판결을 그대로 확정했습니다."),
]
_CV_GR = [
    ("그리고, 그러나, 그래서, 그런데, …", "sentence connectors", "도서관에 갔는데 문이 닫혀 있었어요. 그래서 그냥 돌아와야 했어요."),
    ("–거든", "if", "눈이 오거든 지하철을 타고 출근하세요."),
]
_CV_SINO = [("입법부", "(立法府) the legislative branch", "입석, 공립, 사립, 방법, 불법, 문법, 정부, 사법부, 행정부"), ("장관", "(長官) a cabinet minister; a secretary", "교장, 총장, 시장, 소방관, 경찰관, 교관"), ("투표", "(投票) vote; poll; ballot", "투수, 투자, 투항, 수표, 개표, 표결"), ("총선", "(總選) a general election", "총액, 총수입, 총점, 낙선, 선수, 재선"), ("법원", "(法院) a court of justice; a courthouse", "민법, 형법, 불법, 고아원, 학원, 양로원")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"권한": "authority", "단임": "single term", "총선": "general election", "후보": "candidate", "심": "trial; hearing", "형": "penalty; punishment", "행정부": "the executive branch", "입법부": "the legislative branch", "사법부": "the judicial branch", "국무총리": "the prime minister", "국회의원": "a member of the national assembly", "재선": "reelection", "단임": "a single term", "주식": "stock", "검찰": "public prosecutors", "정당": "a political party", "민주주의": "democracy"}
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
_S1G = [("주립 대학교", "a state university; “state-established university”"), ("시립 도서관", "a municipal library; “library established by city”"), ("민법", "the civil law"), ("군법", "military law"), ("법원", "a court house; “law house”"), ("낙법", "defensive way of falling down; “falling-down method”"), ("행정부", "the executive; the administration"), ("사법부", "the judicial branch; the judiciary")]
_S1 = [("사립 대학교", "a private university"), ("도립 병원", "a provincial hospital"), ("불법 무기", "an illegal weapon"), ("공립 대학교", "a public university"), ("해양법", "maritime law"), ("국제법", "international law"), ("국립공원", "a national park"), ("국내법", "domestic law")]
_S2G = [("사장", "a company president; “company chief”"), ("과장", "a section chief"), ("팀장", "a team leader"), ("반장", "a class president; a squad leader"), ("관용차", "an official vehicle; “car for government use”"), ("관직", "a government post; a government job"), ("법관", "a judge; “officer of law”"), ("차관", "a vice-minister; a deputy secretary; “next official”")]
_S2 = [("교장", "a school principal"), ("총장", "a university president"), ("시장", "a mayor"), ("교관", "an instructor"), ("소방관", "a firefighter"), ("경찰관", "a police officer"), ("통일부 장관", "the Minister of Unification"), ("국방부 장관", "the Minister of National Defense")]
_S3G = [("투망", "a cast (thrown) net"), ("투수", "a pitcher; a hurler; “thrower”"), ("투항", "surrender (to the enemy); “throwing surrender”"), ("투자", "investment; “casting capital”"), ("투기꾼", "a speculator; “professional who casts opportunity”"), ("버스표", "a bus ticket"), ("기차표", "a train ticket"), ("찬성표", "a vote in favor of; an assenting vote; “consenting ballot”"), ("반대표", "a vote against; a dissenting vote; “opposing vote”"), ("표심", "hearts (and minds) of voters; “ballot heart”")]
_S4G = [("총사령관", "commander-in-chief; “general commanding officer”"), ("총장", "president of a university; a chancellor; “general chief”"), ("총회", "a general meeting; a general conference"), ("선택하다", "to choose; to select"), ("차선", "the second best; the next best; “second selection”")]
_S4 = [("총액", "the total amount"), ("총수입", "the total income"), ("총점", "the total score"), ("낙선", "losing an election"), ("선수", "a player; an athlete"), ("재선", "reelection")]
_S5 = [("민법", "civil law"), ("형법", "criminal law"), ("불법", "illegality; unlawfulness"), ("고아원", "an orphanage"), ("학원", "a private academy"), ("양로원", "a nursing home for the aged")]

L1 = lesson(
    "Ch 46 · What the chapter teaches, 입법부 · 장관 · 투표 · 총선 · 법원",
    "정치 · 입법부 · 장관 · 투표 · 총선 · 법원 · 立法府 · 長官 · 投票 · 總選 · 法院",
    requires=[],
    cards=[
        card("What Chapter 46 teaches (정치)",
             "Chapter 46, “Politics”, has a vocabulary builder, three topic presentations (the Korean government, the Korean election system, the Korean trial system) with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and write about basic features of the Korean government, such as its organizations, leaders, and their roles; talk about the electoral systems for the president, national assembly members, chiefs of local government, and their procedures; identify and talk about the Korean judicial system; and extract information about the judicial system, such as types of sentences, procedures, and judicial decision(s).\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; a summary of sentence connectors; the conjunctive ending –거든 (if) used in a command/request; and the Sino-Korean syllables within 입법부 (立法府), 장관 (長官), 투표 (投票), 총선 (總選), and 법원 (法院)."),
        card("Sino-Korean in use: 입법부 (立法府)",
             "This Sino-Korean word means the legislative branch (of a government) or a legislature that passes, amends, and repeals laws. The first syllable 입/립 (立) means establish(ed) or erect(ed), as in 주립 대학교 (a state university; “state-established university”) and 시립 도서관 (a municipal library; “library established by city”). The second syllable 법 (法) means law or method, as in 민법 (the civil law), 군법 (military law), 법원 (a court house; “law house”), and 낙법 (defensive way of falling down; “falling-down method”). The last syllable 부 (府) means government office, as in 행정부 (the executive; the administration) and 사법부 (the judicial branch; the judiciary). Thus the literal meaning of the word is “government office that establishes laws.” The book asks you to guess the meaning of 사립 대학교, 도립 병원, 불법 무기, 공립 대학교, 해양법, 국제법, 국립공원 and 국내법 (my answers):",
             tables=[ktable(_S1G), ktable(_S1)]),
        card("Sino-Korean in use: 장관 (長官)",
             "This Sino-Korean word means a Cabinet Minister or Secretary. The first syllable 장 (長) means head or chief (of an organization), as in 사장, 과장, 팀장, 반장, etc. The second syllable 관 (官) means (government) official/officer or government, as in 관용차 (an official vehicle; “car for government use”), 관직 (a government post; a government job), 법관 (a judge; “officer of law”), and 차관 (a vice-minister; a deputy secretary; “next official”). Thus the literal meaning of the word 장관 is “chief official” or “chief officer.” The book asks you to guess 교장, 총장, 시장, 교관, 소방관, 경찰관, 통일부 장관 and 국방부 장관 (the book’s examples 사장, 과장, 팀장 and 반장 are glossed here by me; my answers):",
             tables=[ktable(_S2G), ktable(_S2)]),
        card("Sino-Korean in use: 투표 (投票)",
             "This Sino-Korean word means vote, voting, or (casting) a ballot. The first syllable 투 (投) means throw or cast, as in 투망 (a cast/thrown net), 투수 (a pitcher; a hurler; “thrower”), 투항 (surrender [to the enemy]; “throwing surrender”), 투자 (investment; “casting capital”), and 투기꾼 (a speculator; “professional who casts opportunity”). The second syllable 표 (票) means ticket as in 버스표, 기차표, and 비행기 [표] (the book prints 비행기), or ballot, as in 찬성표 (a vote in favor of; an assenting vote; “consenting ballot”), 반대표 (a vote against; a dissenting vote; “opposing vote”), and 표심 (hearts [and minds] of voters; “ballot heart”). Thus the literal meaning of the word 투표 is “ticket throwing” or “ballot casting.”",
             tables=[ktable(_S3G)]),
        card("Sino-Korean in use: 총선 (總選)",
             "This Sino-Korean word, which comes from 총선거, means a general election (in which all or most members of a given political body are chosen). The first syllable 총 (總) means whole, total, or general, as in 총사령관 (commander-in-chief; “general commanding officer”), 총장 (president of a university; a chancellor; “general chief”), and 총회 (a general meeting; a general conference). The second syllable 선 (選) means selection, as in 선택하다 (to choose; to select) and 차선 (the second best; the next best; “second selection”). Thus the literal meaning of the word is “general selection” or “general election.” The book asks you to guess 총액, 총수입, 총점, 낙선, 선수 and 재선 (the book glosses 액 [額]: amount [of money]; my answers):",
             tables=[ktable(_S4G), ktable(_S4)]),
        card("Sino-Korean in use: 법원 (法院)",
             "This Sino-Korean word means a court of justice or a courthouse; 법 (法) means law, and 원 (院) means a house or institute. Thus the literal meaning of the word is “law house.” The book asks you to guess 민법, 형법, 불법, 고아원, 학원 and 양로원 (my answers):",
             tables=[ktable(_S5)]),
    ],
    exercises=uniq(
        _tr(_S1G + _S1 + _S2G + _S2 + _S3G + _S4G + _S4 + _S5, k=3)
        + [M("What does 입/립 (立) mean?", "establish; erect", ["throw", "law", "ticket"], "주립 대학교."), M("What does 법 (法) mean?", "law; method", ["house", "ticket", "chief"], "민법."), M("What does 부 (府) mean in 입법부?", "government office", ["a part", "a ticket", "a house"], "행정부, 사법부."), M("What does 장 (長) mean?", "head; chief", ["official", "throw", "law"], "사장."), M("What does 관 (官) mean?", "(government) official", ["head", "ticket", "house"], "법관."), M("What does 투 (投) mean?", "throw; cast", ["establish", "total", "house"], "투자."), M("What does 표 (票) mean?", "ticket; ballot", ["throw", "select", "law"], "버스표."), M("What does 총 (總) mean?", "whole; total; general", ["select", "ballot", "house"], "총회."), M("What does 선 (選) mean?", "selection", ["throw", "total", "law"], "선택하다."), M("What does 원 (院) mean?", "a house; an institute", ["a law", "a ballot", "a chief"], "법원."), M("What is the literal meaning of 입법부?", "“government office that establishes laws”", ["“law house”", "“chief official”", "“ticket throwing”"], "입 + 법 + 부."), M("What is the literal meaning of 장관?", "“chief official” or “chief officer”", ["“law house”", "“general selection”", "“ballot casting”"], "장 + 관."), M("What is the literal meaning of 투표?", "“ticket throwing” or “ballot casting”", ["“general selection”", "“law house”", "“chief officer”"], "투 + 표."), M("What is the literal meaning of 총선?", "“general selection” or “general election”", ["“ticket throwing”", "“law house”", "“chief official”"], "총 + 선."), M("What is the literal meaning of 법원?", "“law house”", ["“general selection”", "“ballot casting”", "“chief officer”"], "법 + 원."),
           F("민___은 시민들의 생활에 관한 법입니다. (civil law)", "법", ["원", "표"], "민법."), F("고아___은 부모가 없는 아이들이 사는 곳입니다. (orphanage)", "원", ["법", "표"], "고아원."), F("찬성___와 반대표를 세어서 결과를 발표했습니다. (vote)", "표", ["법", "원"], "찬성표."), F("대학교의 총___이 졸업식에서 축사를 했습니다. (president)", "장", ["관", "선"], "총장."), F("소방___은 불이 나면 사람들을 구합니다. (firefighter)", "관", ["장", "표"], "소방관."),
           read_q("입법부"), read_q("장관"), read_q("투표"), read_q("총선"), read_q("법원")]
    ),
)

# ================================================================== L2 Vocabulary builder
_VB = [("행정부", "행정 (administration), 부 (a public office; a branch)", "the executive branch"), ("입법부", "입법 (lawmaking), 부 (a public office; a branch)", "the legislative branch"), ("사법부", "사법 (judiciary), 부 (a public office; a branch)", "the judicial branch"), ("대통령", "대 (big), 통 (govern), 령 (command)", "the head of a nation; the president"), ("국무총리", "국무 (national affairs), 총 (total; entire), 리 (govern)", "the prime minister"), ("장관", "장 (a chief), 관 (a public official)", "a minister; a secretary"), ("국회의원", "국회 (national assembly), 의원 (a member of congress or council)", "a member of the national assembly"), ("총선", "총 (total; entire), 선 (elect; select)", "a general election"), ("선거", "선 (elect; select), 거 (raise)", "an election"), ("낙선", "낙 (fall; fail), 선 (elect; select)", "losing an election"), ("재선", "재 (re-; again), 선 (elect; select)", "reelection"), ("임기", "임 (mission; appointment), 기 (a period)", "the period of a term"), ("단임", "단 (single), 임 (a term)", "a single term"), ("연임", "연 (consecutive), 임 (a term)", "a consecutive term")]
_ODD = [("정부", "사법부, 입법부, 재선, 행정부", "재선", "사법부, 입법부 and 행정부 are the three branches of government; 재선 is reelection"), ("행정부", "국무총리, 대통령, 장관, 법원", "법원", "국무총리, 대통령 and 장관 belong to the executive branch; 법원 is a court"), ("선거", "장관, 총선, 개표, 재선", "장관", "총선, 개표 and 재선 relate to elections; 장관 is a minister"), ("임기", "재임, 낙선, 단임, 연임", "낙선", "재임, 단임 and 연임 relate to the term of office; 낙선 is losing an election")]
L2 = lesson(
    "Ch 46 · Vocabulary Builder: government and elections",
    "행정부 · 입법부 · 사법부 · 대통령 · 국무총리 · 장관 · 국회의원 · 총선 · 선거 · 낙선 · 재선 · 임기 · 단임 · 연임",
    requires=[],
    cards=[
        card("새 단어 a: match the words with their meanings",
             "Look at the words, their literal meanings and the English meanings and match each word with its English meaning (the book’s fourteen words, literal meanings and English meanings; the matches are mine to confirm from the literal meanings):",
             tables=[table(["Word", "Literal meaning (the book’s)", "English meaning"], [[a, b, c] for a, b, c in _VB], say=[0])]),
        card("새 단어 b: which word does not belong?",
             "Read each numbered category word and circle the word that does NOT fit into the category (the book’s rows; the odd ones out are my answers):",
             tables=[table(["Category", "Words", "Odd one out (mine)", "Why (mine)"], [[a, b, c, d] for a, b, c, d in _ODD], say=[0, 1, 2])]),
        card("Activities left out", "Activities 1, 2 and 3 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 4 (the “Stop!” game: each student gets seven word cards per round; the teacher reads a description aloud, a student who knows the word says “그만!”, names the word and holds up the card for 2 points, a wrong answer costs a point, and the student with the most points wins) are computer and game activities."),
    ],
    exercises=uniq(
        _tr([(a, c) for a, b, c in _VB], k=3)
        + [M("What does 행정부 mean?", "the executive branch", ["the legislative branch", "the judicial branch", "a court"], "행정 + 부."), M("What does 입법부 mean?", "the legislative branch", ["the executive branch", "the judicial branch", "a general election"], "입법 + 부."), M("What does 사법부 mean?", "the judicial branch", ["the executive branch", "the legislative branch", "the prime minister"], "사법 + 부."), M("What does 대통령 mean?", "the president", ["the prime minister", "a minister", "a candidate"], "대 + 통 + 령."), M("What does 국무총리 mean?", "the prime minister", ["the president", "a minister", "a mayor"], "국무 + 총리."), M("What does 낙선 mean?", "losing an election", ["reelection", "a single term", "a general election"], "낙 + 선."), M("What does 재선 mean?", "reelection", ["losing an election", "an election", "a consecutive term"], "재 + 선."), M("What does 단임 mean?", "a single term", ["a consecutive term", "reelection", "a term of office"], "단 + 임."), M("What does 연임 mean?", "a consecutive term", ["a single term", "losing an election", "a general election"], "연 + 임."), M("What does 임기 mean?", "the period of a term", ["an election", "a candidate", "a vote"], "임 + 기."), M("Which does NOT belong to 정부?", "재선", ["사법부", "입법부", "행정부"], "My answer."), M("Which does NOT belong to 행정부?", "법원", ["국무총리", "대통령", "장관"], "My answer."), M("Which does NOT belong to 선거?", "장관", ["총선", "개표", "재선"], "My answer."), M("Which does NOT belong to 임기?", "낙선", ["재임", "단임", "연임"], "My answer."),
           F("대한민국의 ___은 국가를 대표하는 사람입니다. (president)", "대통령", ["장관", "의원"], "대통령."), F("국회에서 법을 만드는 사람은 국회___입니다. (member)", "의원", ["총리", "장관"], "국회의원."), F("총선에서 떨어지는 것을 ___이라고 합니다. (losing an election)", "낙선", ["재선", "단임"], "낙선."), F("한 번 더 뽑히는 것을 ___이라고 합니다. (reelection)", "재선", ["낙선", "임기"], "재선."), F("대통령의 ___는 오 년입니다. (term)", "임기", ["연임", "선거"], "임기."),
           read_q("행정부"), read_q("입법부"), read_q("사법부"), read_q("국무총리"), read_q("국회의원")]
    ),
)


# ================================================================== L3 Topic A
_A_TXT = [
    ("대한민국은 대통령 중심제의 민주주의 국가이다.", "The Republic of Korea is a democratic country with a president-centered system."),
    ("대한민국 정부는 크게 행정부, 입법부, 사법부로 구성되어 있다.", "The government of the Republic of Korea is largely composed of the executive, the legislative and the judicial branches."),
    ("넓은 의미의 정부는 행정, 입법, 사법 삼 부를 가리키지만, 좁은 의미의 정부는 행정부만을 가리킨다.", "Government in the broad sense refers to the three branches of administration, legislation and judiciary, but government in the narrow sense refers only to the executive branch."),
    ("행정부는 대통령을 중심으로 국무 총리, 행정 각 부의 장관으로 구성된다.", "The executive branch is composed of the president at the center, the prime minister, and the ministers of the executive ministries."),
    ("대통령은 외국에 대하여 국가를 대표하며, 행정부의 최고 지휘권을 가진다.", "The president represents the nation toward foreign countries and holds the highest command authority of the executive branch."),
    ("행정 각 부에는 각각 맡은 일을 처리하기 위한 기관이 있고 지방 행정을 위한 여러 가지 지방 행정 기관이 있다.", "Each executive ministry has an organization for handling the work it is in charge of, and there are various local administrative organizations for local administration."),
]
_A_WORDS = ["가리키다", "구성", "국무", "국방", "권한/~권", "기획", "대통령", "맡다", "민주주의", "보건", "~부", "사법", "외교", "임명", "입법", "장관", "재정", "정책", "지휘", "총리", "통상", "행정"]
_BU = [("입법부", "府", "the legislative branch"), ("사법부", "府", "the judicial branch"), ("행정부", "府", "the executive branch"), ("통일부", "部", "the Ministry of Unification"), ("국방부", "部", "the Ministry of National Defense")]
L3 = lesson(
    "Ch 46 · Topic A: the Korean government (대한민국 정부)",
    "대한민국 정부 · 대통령 중심제 · 행정부 · 입법부 · 사법부 · 국무총리 · 장관 · 府 · 部",
    requires=[],
    cards=[
        card("Topic A: the Korean government (대한민국 정부)",
             "The following excerpt is from a social studies textbook. It describes the organization of the Korean government. (The English is mine; the book gives none. The text is the book’s with 3부 spelled out as 삼 부 and the dots in 행정·입법·사법 written as commas. The book’s footnote: 대통령 중심제 [“president-centered system”] refers to a [full] presidential system.)",
             examples=passage(_A_TXT)),
        card("The chart of the government (대한민국 정부 조직도)",
             "The book prints an organization chart (a picture, not reproduced here; the book says that on the screen you can click it to see a complete chart of the executive branch). Its structure: 대한민국 정부 is divided into 입법부, 행정부 and 사법부; the 행정부 has the 대통령, the 국무총리, the ministries (행정 각 부, 19 of them) and 19 services (청)."),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_A_WORDS)),
        card("한국어에는: 부 (府) and 부 (部)",
             "In this chapter you will encounter a number of words that end in 부, as in 입법부, 사법부, 통일부, 국방부, etc. However, depending on the words, the Sino-Korean syllable can be 부 (府), which means a (main) government branch or office, or 부 (部), which means part, department, ministry, or region. Thus, the three branches of government, 입법부 (legislative), 사법부 (judicial), and 행정부 (executive), use the Sino-Korean syllable 부 (府). However, the ministries of government, such as 통일부 (ministry of unification) and 국방부 (ministry of defense), all use the Sino-Korean syllable 부 (部).",
             tables=[table(["Word", "Hanja of 부", "Meaning"], [[a, b, c] for a, b, c in _BU], say=[0])]),
        card("한국에서는: the executive branch of South Korea",
             "The executive branch of South Korea is led by the president, who resides in the Yongsan Presidential Office (용산 대통령실) in Seoul. Prior to its relocation in 2022, the official residence of the president had been Cheong Wa Dae (the Blue House/청와대) since 1948. 청와대 is now a public park. The executive branch consists of the president, the prime minister, and cabinet-level ministers. The South Korean government currently has 19 ministries. Note that the names and numbers of ministries and services can change as part of governmental reforms, such as the 2013 reversion of the Ministry of Foreign Affairs and Trade (외교통상부) to the Ministry of Foreign Affairs (외교부)."),
        card("북한에서는: the government of North Korea",
             "The Chairman (국무위원장) of the State Affairs Commission of the Democratic People’s Republic of Korea is the head of state in North Korea. The “국무위원장” heads the State Affairs Commission (SAC), which is the highest leadership institution in North Korea, and serves as the commander-in-chief of the North Korean armed forces. The SAC is defined by the 2016 constitution as the supreme policy-oriented leadership body of state power. The Cabinet (내각) can be considered the administrative state body that serves as North Korea’s ‘government’. The Cabinet is headed by the Premier (내각총리), with Vice Premiers (부총리) and Ministers (상) who are in charge of each ministry. The Supreme People’s Assembly (SPA/최고인민회의) is the vehicle through which the Party carries out its decisions. Therefore, the SPA is the highest political body in North Korea. Assembly meetings are held once or twice a year. In reality, the SPA is a rubber-stamp assembly that merely passes laws and decisions handed down by the Workers’ Party of Korea (로동당). During recess periods, the functions of the SPA are carried out by the Standing Committee (최고인민회의 상임위원회). (Source given by the book: DLIFLC/Area Studies.)"),
        card("Activities left out", "The presentation steps of Topic A (a: the class brainstorms English words for the U.S. executive and cabinet structure and writes them in a box; b: reading and listening to the topic and circling the English words that align with the Korean structure; c and d: SMART Board activities; e: pair translation sentence by sentence; f: review with the teacher) are audio, computer and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT, k=3)
        + [M("What kind of system does Korea have?", "A president-centered democracy", ["A monarchy", "A parliamentary monarchy", "A military state"], "대통령 중심제의 민주주의 국가."), M("Into what is the Korean government largely divided?", "The executive, legislative and judicial branches", ["Two branches", "Four ministries", "The army and the police"], "행정부, 입법부, 사법부."), M("What does government in the narrow sense refer to?", "Only the executive branch", ["All three branches", "The courts", "The assembly"], "행정부만을."), M("Who forms the executive branch?", "The president, the prime minister and the ministers", ["The judges", "The assembly members", "The mayors"], "대통령, 국무 총리, 장관."), M("What does the president represent toward foreign countries?", "The nation", ["A ministry", "A party", "A city"], "국가를 대표."), M("What does the president hold in the executive branch?", "The highest command authority", ["No authority", "Only a title", "The courts"], "최고 지휘권."), M("Which 부 uses the Hanja 府?", "입법부", ["통일부", "국방부", "외교부"], "府: a branch of government."), M("Which 부 uses the Hanja 部?", "국방부", ["입법부", "사법부", "행정부"], "部: a ministry."), M("Where was the official residence of the president until 2022?", "Cheong Wa Dae (the Blue House)", ["The Yongsan Presidential Office", "The National Assembly", "The Supreme Court"], "청와대 since 1948."), M("What does the head of state in North Korea hold?", "The chairmanship of the State Affairs Commission (국무위원장)", ["The premiership of the Cabinet", "The chairmanship of the Assembly", "The Standing Committee"], "The book’s note."),
           F("대한민국은 대통령 중심제의 ___ 국가이다. (democratic)", "민주주의", ["공산주의", "군주제"], "민주주의."), F("넓은 의미의 정부는 행정, 입법, 사법 삼 부를 ___ 있다. (refers to)", "가리키고", ["맡고", "구성하고"], "가리키다."), F("행정부는 대통령을 중심으로 국무 총리, 행정 각 부의 ___으로 구성된다. (ministers)", "장관", ["의원", "판사"], "장관."), F("대통령은 행정부의 최고 ___을 가진다. (command authority)", "지휘권", ["재정권", "통상권"], "지휘권."), F("각 부에는 각각 ___ 일을 처리하기 위한 기관이 있다. (in charge of)", "맡은", ["가리킨", "구성된"], "맡다."),
           read_q("대한민국 정부"), read_q("대한민국은 대통령 중심제의 민주주의 국가입니다"), read_q("행정부는 대통령을 중심으로 구성됩니다"), read_q("대통령은 행정부의 최고 지휘권을 가집니다"), read_q("행정 각 부에는 각각 맡은 일을 처리하는 기관이 있습니다")]
    ),
)

# ================================================================== L4 Follow-ups A: ministries
_MIN = [("기획재정부", "Ministry of Strategy & Finance"), ("외교부", "Ministry of Foreign Affairs"), ("보건복지부", "Ministry of Health & Welfare"), ("국방부", "Ministry of National Defense"), ("통일부", "Ministry of Unification"), ("행정안전부", "Ministry of the Interior and Safety")]
_RESP = [
    ("남북대화와 협력에 관한 정책을 기획하고 기타 통일에 관한 사무를 담당합니다.", "It plans policies on dialogue and cooperation between South and North and handles other affairs concerning unification.", "5", "통일부"),
    ("외국과의 통상 및 경제 관련 외교 정책을 세우고, 외국과의 문화협력 및 이민에 관한 사무를 담당합니다.", "It sets up diplomatic policies related to trade and the economy with foreign countries and handles affairs on cultural cooperation and immigration with foreign countries.", "2", "외교부"),
    ("대한민국의 경제 정책을 기획하고, 국가 재정에 관한 정책을 관리합니다.", "It plans the economic policies of the Republic of Korea and manages policies on national finances.", "1", "기획재정부"),
    ("국민 보건 및 위생에 관한 사무와 사회 복지에 관한 사무를 맡습니다.", "It takes charge of affairs on public health and hygiene and affairs on social welfare.", "3", "보건복지부"),
    ("대한민국의 방위를 담당하는 정부 기관으로 육군, 공군, 해군, 해병대를 모두 관리합니다.", "It is the government organization in charge of the defense of the Republic of Korea and manages the army, air force, navy and marine corps.", "4", "국방부"),
    ("국민들의 생활이 행복하고 편리해질 수 있도록 교통안전, 시설안전, 학교안전 등 여러 안전 및 재난에 대한 정책을 만들고 관리합니다.", "It makes and manages policies on various kinds of safety and disasters, such as traffic safety, facility safety and school safety, so that the people’s lives can become happy and convenient.", "6", "행정안전부"),
]
_ORG5 = [("문화체육관광부", "Ministry of Culture, Sports and Tourism"), ("외교부", "Ministry of Foreign Affairs"), ("국방부", "Ministry of National Defense"), ("환경부", "Ministry of Environment"), ("행정안전부", "Ministry of the Interior and Safety")]
L4 = lesson(
    "Ch 46 · Follow-ups A: the ministries and what they do",
    "기획재정부 · 외교부 · 보건복지부 · 국방부 · 통일부 · 행정안전부 · 담당하다 · 맡다 · 관리하다",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading) a: match each ministry with its English meaning",
             "The book’s six ministries with their English meanings (the book asks you to match them by drawing lines; the pairs are the book’s own list):",
             tables=[ktable(_MIN)]),
        card("Follow-up 2 (Reading) b: which ministry is described?",
             "The following sentences explain the responsibilities of the ministries in Step a. The book asks you to read each sentence and write the number of the ministry (from Step a) in the blank. The sentences are the book’s (the dots between the safety words are written as commas); the answers and the English are mine.",
             tables=[table(["Sentence", "Number (mine)", "Ministry (mine)"], [[a, c, d] for a, b, c, d in _RESP], say=[0, 2]), table(["English of the sentence (mine)"], [[b] for a, b, c, d in _RESP])]),
        card("Activities and websites left out",
             "Follow-up 1 (listening: two people talk about a government official visiting a foreign country; the table asks for the official, the country visited and the purpose) is an audio activity. The book’s useful websites are 대한민국 대통령실, 청와대 and 정부 조직도 (web pages).\n\n"
             "The chapter’s Activities pages for this topic are also left out: Activity 1 (listening to five news clips about government policies and choosing the organization concerned from the box: a. 문화체육관광부 b. 외교부 c. 국방부 d. 환경부 e. 행정안전부, then summarizing the policies in English; the book glosses 간부: leadership, 발자국: footprint and 확대하다: to expand), Activity 2 (listening to a YTN news report on a cabinet meeting: the type of meeting, the titles of the ministers mentioned, and choosing the best title among “an emergency meeting on recovery from the heavy-snow damage”, “the president appoints the ministers of five ministries today” and “ministers late to the cabinet meeting because of the heavy snow”) and Activity 3 (a pair task: each partner reads two of four policy announcements from a cabinet meeting, fills in the policy details, exchanges the information in Korean, decides which organization should be responsible and presents it; the book glosses 과태료: fine; penalty, 부과: imposition [to impose/to be imposed] and 접종: vaccination; the announcements are not printed in the student text).",
             tables=[ktable(_ORG5)]),
    ],
    exercises=uniq(
        _tr(_MIN, k=3) + _tr([(a, b) for a, b, c, d in _RESP], k=3)
        + [M("Which ministry plans policies on dialogue and cooperation between South and North?", "통일부", ["외교부", "국방부", "보건복지부"], "남북대화와 협력."), M("Which ministry sets up diplomatic policies related to trade and the economy?", "외교부", ["통일부", "행정안전부", "국방부"], "통상 및 경제 관련 외교 정책."), M("Which ministry plans the economic policies and manages national finances?", "기획재정부", ["외교부", "통일부", "보건복지부"], "경제 정책, 국가 재정."), M("Which ministry takes charge of public health and social welfare?", "보건복지부", ["국방부", "행정안전부", "외교부"], "보건, 복지."), M("Which ministry manages the army, air force, navy and marine corps?", "국방부", ["통일부", "외교부", "행정안전부"], "육군, 공군, 해군, 해병대."), M("Which ministry makes policies on traffic, facility and school safety?", "행정안전부", ["국방부", "보건복지부", "기획재정부"], "교통안전, 시설안전, 학교안전."), M("What is 환경부 in English?", "the Ministry of Environment", ["the Ministry of Defense", "the Ministry of Unification", "the Ministry of Finance"], "My gloss."), M("What does the 외교부 also handle, besides trade policy?", "Cultural cooperation and immigration affairs with foreign countries", ["The army", "Public hygiene", "Unification"], "문화협력 및 이민."),
           F("통일부는 남북대화와 협력에 관한 정책을 ___합니다. (plans)", "기획", ["지휘", "임명"], "기획."), F("국방부는 대한민국의 ___를 담당하는 정부 기관입니다. (defense)", "방위", ["재정", "보건"], "방위."), F("보건복지부는 국민 ___ 및 위생에 관한 사무를 맡습니다. (health)", "보건", ["국방", "외교"], "보건."), F("기획재정부는 국가 ___에 관한 정책을 관리합니다. (finances)", "재정", ["보건", "외교"], "재정."), F("외교부는 외국과의 ___ 및 경제 관련 외교 정책을 세웁니다. (trade)", "통상", ["국방", "보건"], "통상."),
           read_q("기획재정부"), read_q("외교부"), read_q("보건복지부"), read_q("국방부"), read_q("통일부")]
    ),
)


# ================================================================== L5 Topic B
_B_TXT = [
    ("한국의 선거에는 대통령 선거, 국회 의원 총선거, 지방자치 단체장 및 의원 선거가 있다.", "Korea’s elections include the presidential election, the National Assembly general election, and the elections of heads of local governments and of (local) assembly members."),
    ("원칙적으로 한국의 모든 선거는 직선제이다.", "In principle, all of Korea’s elections are direct elections."),
    ("대통령 선거는 오 년마다 있으며 총선과 지방자치단체장 선거는 사 년마다 있다.", "The presidential election is held every five years, and the general election and the elections of heads of local governments are held every four years."),
    ("대통령의 임기는 오 년 단임으로 제한되어 있으나 국회의원은 여러 번 재임할 수 있다.", "The president’s term is limited to a single term of five years, but a member of the National Assembly can serve again many times."),
    ("하지만, 시장이나 도지사 같은 지방자치단체장은 세 번까지 연임할 수 있다.", "However, heads of local governments such as mayors or provincial governors can serve consecutive terms up to three times."),
    ("한국의 선거일은 수요일이고 보궐선거는 매년 사월과 시월에 있다.", "Election day in Korea is a Wednesday, and by-elections are held every April and October."),
    ("선거 운동 기간에는 투명하고 공정한 선거를 위해 중앙 선거관리 위원회와 각 지방 선거관리 위원회가 선거활동을 감시한다.", "During the election campaign period, the Central Election Commission and each local election commission watch over election activities for a transparent and fair election."),
]
_B_WORDS = ["감시", "개표", "공정하다", "국회", "낙선", "단임(제)", "단체장", "당선", "도지사", "발표", "보궐선거", "선거", "연임", "원칙", "유세", "유권자", "의원", "임기", "재임", "절차", "정당", "정치", "지방자치", "지지", "총선(거)", "투명하다", "투표", "후보(자)"]
_STEPS = [("후보자 등록", "candidate registration"), ("선거 운동", "election campaign"), ("투표", "voting"), ("개표", "ballot counting"), ("당선자 발표", "announcement of the elected")]
_ACR = [("대선", "대통령 선거", "the presidential election"), ("총선", "국회의원 총선거", "the National Assembly general election"), ("선관위", "선거 관리 위원회", "the election commission"), ("직선제", "직접 선거제도", "the direct election system"), ("지자체", "지방자치단체", "a local government")]
L5 = lesson(
    "Ch 46 · Topic B: the Korean election system (한국의 선거 제도)",
    "한국의 선거 제도 · 대선 · 총선 · 직선제 · 지자체 · 선관위 · 임기 · 연임 · 보궐선거 · 선거 절차",
    requires=[],
    cards=[
        card("Topic B: the Korean election system (한국의 선거 제도)",
             "The following excerpt is from the Korean National Election Commission website. (The English is mine; the book gives none. The text is the book’s with the numbers spelled out: 5년 is 오 년, 4월과 10월 is 사월과 시월. The book’s footnotes: 3 A mayor and a provincial governor [도지사] are examples of 지방자치단체장; 4 직선제 is the shortened form of 직접선거 제도; 5 중앙 선거관리 위원회 [Central National Election Commission] is an independent government organization that monitors presidential and general elections; 지방 선거관리 위원회 monitors local elections.)",
             examples=passage(_B_TXT)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_B_WORDS)),
        card("선거 절차: the steps of an election",
             "The book shows news photos (from 조선일보, 세계일보, 경향신문, 연합뉴스 and 동아일보) under the headings 선거 절차: 후보자 등록, 선거 운동, 투표, 당선자 발표 and 개표. The pictures are left out; the five steps are (English mine):",
             tables=[ktable(_STEPS)]),
        card("한국에서는: acronyms and nicknames in politics",
             "Acronyms are used heavily in Korean politics for proper names and titles. For example, 대선 is a shortened form of 대통령 선거. Other examples include 총선 for 국회의원 총선거, 선관위 for 선거 관리 위원회, 직선제 for 직접 선거제도, and 지자체 for 지방자치단체.\n\n"
             "In the political realm, Koreans frequently refer to influential politicians by their Romanized initials. For example, newspapers often refer to 이명박 대통령 as MB, the initials for his given names. In the same manner, 김대중 대통령, a Nobel Peace Prize winner and famous historical figure, is referred to as DJ.",
             tables=[table(["Short form", "Full form", "Meaning (mine)"], [[a, b, c] for a, b, c in _ACR], say=[0, 1])]),
        card("한국에서는: election culture and the 1987 direct election",
             "Although Korea is a democracy, its election culture and process differ somewhat from that of the United States. In Korea, presidential and general election days are designated as holidays to encourage voter turnout. Also, Korean elections are determined by popular vote and do not involve an electoral college. In 1972, President Park Junghee changed the then-direct presidential election to an indirect election in a maneuver to perpetuate his presidency. This system remained in place until 1987 when the so-called 6.10 민주항쟁 (Democratic Revolt of June 10th) resulted in a return to direct election. This achievement is part of Korea’s modern history. Citizens continually rallied against the military dictators who seized power via coups and manipulated the law to maintain that power. The movement was driven by the middle class, who wanted to change the system and elect the president directly. The movement gained momentum throughout the spring of 1987 and culminated in June of that year, when huge numbers of college students, professors, white and blue collar workers, retirees, and homemakers protested on a daily basis. Finally, the government surrendered to public demand and the Korean people obtained the right to a direct vote. (The book shows a 2022 presidential election poster [대통령 선거 벽보] from 연합뉴스; the picture is left out.)"),
        card("Activities left out", "The presentation steps of Topic B (a: pairs study two sets of vocabulary cards and quiz each other; b: reading and listening; c: SMART Board; d: review with the teacher) are audio, computer and pair activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT, k=3) + _tr([(a, c) for a, b, c in _ACR], k=3)
        + [M("Which elections does Korea have?", "Presidential, National Assembly general, and local government head and assembly elections", ["Only presidential", "Only local", "Only the assembly"], "선거에는 ... 가 있다."), M("What kind of election are all of Korea’s elections in principle?", "A direct election", ["An indirect election", "An electoral college", "A lottery"], "직선제."), M("How often is the presidential election held?", "Every five years", ["Every four years", "Every year", "Every ten years"], "오 년마다."), M("How often are the general election and the local head elections held?", "Every four years", ["Every five years", "Every year", "Every two years"], "사 년마다."), M("What is the president’s term?", "A single term of five years", ["Four years with reelection", "Two terms of five years", "Ten years"], "오 년 단임."), M("How many times can a mayor or governor serve consecutively?", "Up to three times", ["Only once", "Never", "Without limit"], "세 번까지 연임."), M("On what day of the week is election day?", "Wednesday", ["Sunday", "Saturday", "Monday"], "수요일."), M("When are by-elections held?", "Every April and October", ["Every March", "Every January", "Every December"], "사월과 시월."), M("Who watches over election activities?", "The central and local election commissions", ["The army", "The courts", "The police only"], "선거관리 위원회."), M("What is 대선 short for?", "대통령 선거", ["대학 선거", "대한 선거", "대중 선거"], "대선."), M("What is 선관위 short for?", "선거 관리 위원회", ["선거 관련 위원", "선생 관리 위원", "선택 관리 위원"], "선관위."), M("What is 지자체 short for?", "지방자치단체", ["지방자치제", "지상자치체", "지구자치체"], "지자체."), M("What led to the return to direct presidential election in 1987?", "The 6.10 Democratic Revolt", ["A coup", "A war", "An election in 1972"], "6.10 민주항쟁."),
           F("대한민국의 모든 선거는 원칙적으로 ___이다. (direct election system)", "직선제", ["간선제", "단임제"], "직선제."), F("대통령 선거는 ___ 년마다 있다. (five)", "오", ["사", "삼"], "오 년."), F("국회의원은 여러 번 ___할 수 있다. (serve again)", "재임", ["낙선", "단임"], "재임."), F("지방자치단체장은 세 번까지 ___할 수 있다. (serve consecutive terms)", "연임", ["낙선", "재선"], "연임."), F("투명하고 ___ 선거를 위해 선거활동을 감시한다. (fair)", "공정한", ["유명한", "복잡한"], "공정하다."),
           read_q("한국의 선거 제도"), read_q("한국의 선거에는 대통령 선거와 총선이 있습니다"), read_q("한국의 모든 선거는 직선제입니다"), read_q("대통령의 임기는 오 년 단임입니다"), read_q("한국의 선거일은 수요일입니다")]
    ),
)

# ================================================================== L6 Follow-ups B: the flyers
_FL1 = [("대통령 선거", "대한민국 국민으로서 피선거권이 있는 사람", "사십 세 이상", "오 년 이상 국내 거주"), ("국회의원 선거", "대한민국 국민으로서 피선거권이 있는 사람", "십팔 세 이상", "없음"), ("지방선거", "대한민국 국민으로서 피선거권이 있는 사람", "십팔 세 이상", "육십 일 이상 지방자치단체에 주민등록이 신고된 사람")]
_FL2 = [("대통령", "오 년 단임제, 연임할 수 없음", "삼천오백 명에서 육천 명", "선거일 전 이십사 일부터 이 일간"), ("국회의원", "사 년 임기, 계속 재임할 수 있음", "삼백 명에서 오백 명", "선거일 전 십오 일부터 이 일간"), ("시 도지사", "사 년 임기, 세 번 이상 연임할 수 없음", "천 명에서 이천 명", "선거일 전 십오 일부터 이 일간")]
L6 = lesson(
    "Ch 46 · Follow-ups B: the election flyers",
    "후보자 · 자격 조건 · 연령 · 거주조건 · 피선거권 · 임기 · 추천 수 · 후보자 등록 신청",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): Flyer 1, the qualifications",
             "Read the following two flyers from the National Election Commission for those who plan to run for public office. The book asks you to complete Tables 1 and 2 in English. Flyer 1 is the book’s, with the numbers spelled out (40세 is 사십 세, 5년 is 오 년, 60일 is 육십 일). The book glosses 피선거권: right to be elected; the flyer is a merged table, so the same qualification applies to all three elections; where the book prints nothing for the National Assembly’s residence condition I write 없음 (none).",
             tables=[table(["선거명", "자격 조건", "연령", "거주조건 (선거일 현재)"], [list(r) for r in _FL1], say=[0, 1, 2, 3])]),
        card("Follow-up 1 (Reading): Flyer 2, terms and registration",
             "Flyer 2 is the book’s, with the numbers spelled out (3,500~6,000명 is 삼천오백 명에서 육천 명; 24일 is 이십사 일; 2일간 is 이 일간; the dot in 시·도지사 is written as a space). The columns of the book are 후보자, 임기, 선거인 후보자 추천 수 and 후보자 등록 신청.",
             tables=[table(["후보자", "임기", "선거인 후보자 추천 수", "후보자 등록 신청"], [list(r) for r in _FL2], say=[0, 1, 2, 3])]),
        card("Table 1 and Table 2 filled in (mine)",
             "Table 1 (qualifications for all candidates) and Table 2 (term length and restrictions, number of endorsees, registration) with my answers from the flyers:",
             tables=[table(["", "Presidential election", "National Assembly members election", "Local elections"], [["Qualification", "A Korean citizen with the right to be elected", "A Korean citizen with the right to be elected", "A Korean citizen with the right to be elected"], ["Age", "40 years old or over", "Over 18 years old", "Over 18 years old"], ["Residency requirement", "Has lived in Korea for 5 years or more", "None listed", "Has resided at the location for 60 days or more (as reported to the local government office, as of election day)"], ["Term length and restrictions", "5 years; a single term, cannot be reelected", "4 years; can continue to serve again", "4 years; cannot be reelected more than three times"], ["Number of endorsees", "3,500–6,000", "300–500", "1,000–2,000"], ["Registration", "For 2 days, from 24 days before election day", "For 2 days, from 15 days before election day", "For 2 days, from 15 days before election day"]])]),
        card("Activities and websites left out",
             "Follow-up 2 (listening to three conversations about an election: checking the type of election [presidential, National Assembly or local government] and the topic [candidate registration, election campaign, ballot, ballot counting or election results], then writing in English the reason each speaker supported the candidate) is an audio activity. The book’s useful website is 중앙선거관리위원회.\n\n"
             "The chapter’s Activities pages for this topic are not about the flyers (they come after the grammar): see the later lessons."),
    ],
    exercises=uniq(
        [M("How old must a presidential candidate be?", "40 or over", ["18 or over", "30 or over", "60 or over"], "사십 세 이상."), M("How long must a presidential candidate have lived in Korea?", "5 years or more", ["60 days", "1 year", "10 years"], "오 년 이상 국내 거주."), M("How old must a National Assembly candidate be?", "Over 18", ["40 or over", "30 or over", "21 or over"], "십팔 세 이상."), M("How old must a local election candidate be?", "Over 18", ["40 or over", "25 or over", "20 or over"], "십팔 세 이상."), M("How long must a local candidate be registered as a resident?", "60 days or more", ["5 years", "24 days", "2 days"], "육십 일 이상."), M("How many endorsees does a presidential candidate need?", "3,500 to 6,000", ["300 to 500", "1,000 to 2,000", "60"], "삼천오백 명에서 육천 명."), M("How many endorsees does a National Assembly candidate need?", "300 to 500", ["3,500 to 6,000", "1,000 to 2,000", "60"], "삼백 명에서 오백 명."), M("How many endorsees does a provincial governor candidate need?", "1,000 to 2,000", ["300 to 500", "3,500 to 6,000", "60"], "천 명에서 이천 명."), M("When does presidential candidate registration begin?", "24 days before election day, for 2 days", ["15 days before, for 2 days", "On election day", "60 days before"], "이십사 일."), M("When does National Assembly candidate registration begin?", "15 days before election day, for 2 days", ["24 days before", "On election day", "60 days before"], "십오 일."), M("What term does the president have?", "A single five-year term, no consecutive term", ["Four years with reelection", "Three terms", "Unlimited"], "오 년 단임제."), M("What term does an Assembly member have?", "Four years, may continue to serve", ["Five years, single term", "Two years", "Three terms only"], "사 년 임기."), M("What is the limit for provincial governors?", "No more than three consecutive terms", ["Only one term", "No limit", "Five terms"], "세 번 이상 연임할 수 없음."),
         F("대통령 후보는 ___ 세 이상이어야 합니다. (forty)", "사십", ["십팔", "오십"], "사십 세."), F("국회의원 후보는 ___ 세 이상이어야 합니다. (eighteen)", "십팔", ["사십", "이십"], "십팔 세."), F("대통령은 오 년 ___제이므로 연임할 수 없습니다. (single term)", "단임", ["연임", "재선"], "단임제."), F("지방선거 후보는 육십 일 이상 ___이 신고된 사람이어야 합니다. (resident registration)", "주민등록", ["여권", "국적"], "주민등록."), F("후보자는 선거일 전 십오 일부터 이 일간 ___해야 합니다. (register)", "등록", ["투표", "개표"], "등록."),
         read_q("대통령 선거"), read_q("국회의원 선거"), read_q("지방선거"), read_q("후보자 등록 신청"), read_q("피선거권이 있는 사람")]
    ),
)


# ================================================================== L7 Sentence connectors
_CN_ADD = [("그리고", "and"), ("게다가", "in addition; what’s more"), ("또", "also; in addition"), ("또한", "also; in addition"), ("특히", "particularly; in particular"), ("예를 들면", "for example; for instance"), ("그뿐만 아니라", "not only that; additionally")]
_EX_ADD = [("주말에 바닷가에 갔어요. 그리고 친구랑 영화도 봤어요.", "I went to the beach on the weekend. And I also watched a movie with a friend."), ("어제 간 식당은 종업원들이 아주 친절했어요. 게다가 값도 싸고 맛있었어요.", "The waiters at the restaurant I went to yesterday were very kind. What’s more, it was cheap and delicious."), ("이번 주말에 책을 많이 읽을 거예요. 또 동생이랑 테니스도 칠 거예요.", "I will read a lot of books this weekend. Also, I will play tennis with my younger sibling."), ("제 동생은 악기 연주하는 게 취미예요. 특히 피아노를 아주 잘 쳐요.", "My younger sibling’s hobby is playing instruments. In particular, he/she plays the piano very well."), ("저는 친환경 운동을 위해 노력해요. 예를 들면 자동차 대신에 자전거를 타고 출퇴근해요.", "I make an effort for the eco-friendly movement. For example, I commute by bike instead of by car."), ("저희 할인점은 스물네 시간 영업을 하고 있습니다. 그뿐만 아니라 이번에 사백여 평의 주차장도 새로 지었습니다.", "Our discount store is open twenty-four hours. Not only that, we have also newly built a parking lot of about 400 pyeong this time.")]
_CN_CON = [("그렇지만", "but; however"), ("하지만", "but; however"), ("그러나", "and yet; but; still"), ("그런데", "but; however; by the way"), ("그럼", "then; if so"), ("그러면", "then; if so"), ("그래도", "still; yet; nevertheless; however"), ("반면에", "on the other hand")]
_EX_CON = [("어제 친구와 등산을 가기로 했어요. 그렇지만 비가 와서 못 갔어요.", "I decided to go hiking with a friend yesterday. But it rained, so I could not go."), ("오늘까지 일을 끝내야 해요. 그러나 일이 너무 많아서 못 끝낼 것 같아요.", "I have to finish the work by today. Yet there is so much work that I don’t think I can finish."), ("벌써 사월이에요. 그런데 아직도 날씨가 추워요.", "It is already April. But the weather is still cold."), ("지금 바쁘세요? 그럼 제가 나중에 다시 올게요.", "Are you busy now? Then I will come again later."), ("한국어는 너무 어려워요. 그래도 한국어 배우는 건 재미있어요.", "Korean is too difficult. Still, learning Korean is fun."), ("제 누나는 일식을 좋아해요. 반면 저는 중식을 좋아해요.", "My older sister likes Japanese food. On the other hand, I like Chinese food.")]
_CN_CAU = [("그 결과", "so that; as a result"), ("그러니까", "for that reason; therefore"), ("그래서", "so; thus"), ("따라서", "therefore")]
_EX_CAU = [("고등학교 때부터 공부를 아주 열심히 했어요. 그 결과 원하는 대학에 들어갔어요.", "I studied very hard from high school. As a result, I got into the university I wanted."), ("다음 달에 제 딸 돌잔치를 할 거예요. 그러니까 꼭 오셔서 축하해 주세요.", "I will hold my daughter’s first-birthday party next month. So please be sure to come and congratulate her."), ("파티에 가서 너무 많이 먹었어요. 그래서 지금 배불러요.", "I went to a party and ate too much. So I am full now."), ("한국의 서비스업이 급성장하고 있습니다. 따라서 내년에는 경제성장률이 이 퍼센트 오를 것으로 보입니다.", "Korea’s service industry is growing rapidly. Therefore the economic growth rate is expected to rise by 2 percent next year.")]
_CN_SEQ = [("그전에", "before that"), ("그다음에", "after that"), ("그 후에", "after that")]
_EX_SEQ = [("지금 나가실 거예요? 그전에 약 드시고 가세요.", "Are you going out now? Take your medicine before that, and go."), ("저는 저녁 여섯 시에 집에 돌아옵니다. 그다음에 샤워합니다.", "I return home at six in the evening. After that I take a shower.")]
L7 = lesson(
    "Ch 46 · Grammar in Focus: revisiting sentence connectors",
    "문법 탐구 · 그리고 · 게다가 · 또 · 특히 · 예를 들면 · 그렇지만 · 하지만 · 그러나 · 그런데 · 그래서 · 따라서 · 그전에 · 그다음에",
    requires=[],
    cards=[
        card("Revisiting sentence connectors",
             "So far you have learned a number of sentence connectors used to join two independent sentences and show a relationship between them, as in 우리 부모님은 키가 커요. 하지만 제 형님은 키가 작아요 (My parents are tall, but my older brother is small). Note that the connector 하지만 is used to join the two sentences in a contrasting/opposing relationship.\n\n"
             "Sentence connectors you have learned thus far can be broken into four key categories: addition, contrast, causality, and sequence. Note that some of the connectors can fall into multiple categories. (In the book’s tables, a slash or a bracket joins forms such as 그렇지만/하지만, 그럼/그러면, 반면(에), 또(한), 그뿐(만) 아니라, 그전(에) and 그다음(에)/그 후(에); here each form is listed on its own, and the numbers in the examples are spelled out. The English of the examples is mine.)"),
        card("Addition",
             "These connectors are used to add more information, to introduce a specific example or topic, or to show similarity.",
             tables=[ktable(_CN_ADD)], examples=passage(_EX_ADD)),
        card("Contrast",
             "These connectors are used to show contrast between two statements or to express a new statement without invalidating the truth of a previously expressed statement.",
             tables=[ktable(_CN_CON)], examples=passage(_EX_CON)),
        card("Causality",
             "These connectors are used to explain cause/effect and reasons or results.",
             tables=[ktable(_CN_CAU)], examples=passage(_EX_CAU)),
        card("Sequence",
             "These connectors are used to express chronological or logical sequence.",
             tables=[ktable(_CN_SEQ)], examples=passage(_EX_SEQ)),
    ],
    exercises=uniq(
        _tr(_CN_ADD + _CN_CON + _CN_CAU + _CN_SEQ, k=3)
        + _tr(_EX_ADD + _EX_CON + _EX_CAU + _EX_SEQ, k=3)
        + [M("Which category does 그래서 belong to?", "Causality", ["Addition", "Contrast", "Sequence"], "so; thus."), M("Which category does 하지만 belong to?", "Contrast", ["Addition", "Causality", "Sequence"], "but; however."), M("Which category does 게다가 belong to?", "Addition", ["Contrast", "Causality", "Sequence"], "in addition."), M("Which category does 그다음에 belong to?", "Sequence", ["Addition", "Contrast", "Causality"], "after that."), M("Which category does 따라서 belong to?", "Causality", ["Addition", "Contrast", "Sequence"], "therefore."), M("Which category does 반면에 belong to?", "Contrast", ["Addition", "Causality", "Sequence"], "on the other hand."), M("Which category does 예를 들면 belong to?", "Addition", ["Contrast", "Causality", "Sequence"], "for example."), M("Which category does 그전에 belong to?", "Sequence", ["Addition", "Contrast", "Causality"], "before that."),
           F("주말에 바닷가에 갔어요. ___ 친구랑 영화도 봤어요. (and)", "그리고", ["그러나", "그래서"], "그리고."), F("한국어는 너무 어려워요. ___ 한국어 배우는 건 재미있어요. (still)", "그래도", ["그래서", "그리고"], "그래도."), F("파티에 가서 너무 많이 먹었어요. ___ 지금 배불러요. (so)", "그래서", ["그러나", "그래도"], "그래서."), F("제 누나는 일식을 좋아해요. ___ 저는 중식을 좋아해요. (on the other hand)", "반면", ["특히", "그전에"], "반면."), F("지금 바쁘세요? ___ 제가 나중에 다시 올게요. (then)", "그럼", ["그래도", "그런데"], "그럼."),
           read_q("그리고"), read_q("그렇지만"), read_q("그래서"), read_q("따라서"), read_q("그다음에")]
    ),
)

# ================================================================== L8 Follow-ups and activities: connectors
_CIR = [
    ("오늘 낮 동안에는 날씨가 맑겠습니다. [ ] 오후 늦게부터 비가 내리겠습니다.", "그래서 / 하지만 / 그전에", "하지만", "The weather will be clear during the day today. But it will rain from late in the afternoon.", "Contrast."),
    ("요즘 환경 파괴 문제가 심각합니다. [ ] 쓰레기 분리수거 등 환경 보호를 위한 노력이 필요합니다.", "따라서 / 하지만 / 그리고", "따라서", "The problem of environmental destruction is serious these days. Therefore efforts for environmental protection, such as separating garbage for recycling, are needed.", "Causality."),
    ("오늘 너무 아파서 일어나기 힘들었어요. [ ] 일하러 갔어요.", "그래서 / 그래도 / 따라서", "그래도", "I was so sick today that it was hard to get up. Still, I went to work.", "Contrast."),
    ("아토피 피부염 때문에 피부가 빨개요. [ ] 가려워서 너무 힘들어요.", "그렇지만 / 그럼 / 게다가", "게다가", "My skin is red because of atopic dermatitis. What’s more, it itches, so it is very hard.", "Addition."),
    ("저는 수업 후에 체육관에 갑니다. [ ] 집에 가서 저녁을 먹습니다.", "그 후에 / 그 결과 / 예를 들면", "그 후에", "I go to the gym after class. After that I go home and have dinner.", "Sequence."),
    ("다음 주에 저희 집에서 집들이해요. [ ] 가족들과 함께 꼭 오세요.", "그러나 / 그러니까 / 그래도", "그러니까", "We are having a housewarming at our house next week. So please be sure to come with your family.", "Causality."),
]
_DIARY = [("1", "내일은 우리 언니의 생일이다."), ("2", "그래서 오늘 언니 선물을 사러 백화점에 갔다."), ("3", "특히 언니가 스카프를 좋아해서 스카프 파는 매장으로 갔다."), ("4", "그런데 예쁜 스카프가 별로 없었다."), ("5", "반면에 모자는 예쁜 게 많았다."), ("6", "그래서 언니가 좋아하는 노란색 모자를 하나 샀다.")]
_DIARY_EN = ["Tomorrow is my older sister’s birthday.", "So today I went to the department store to buy my sister a present.", "In particular, since my sister likes scarves, I went to the store that sells scarves.", "But there were not many pretty scarves.", "On the other hand, there were many pretty hats.", "So I bought one yellow hat, which my sister likes."]
_ART = [
    ("자유평화당은 일본과 태국에서 귀화한 여성 두 명을 지방의원 후보로 결정했다.", "The Free Peace Party decided on two women naturalized from Japan and Thailand as candidates for local assembly."),
    ("자평당 대변인은 일본에서 귀화한 신미자 씨를 경상북도 의원 후보로, 또 태국에서 귀화한 한에리카 씨를 부산시의원 후보로 결정했다고 밝혔다.", "The party’s spokesperson announced that it had decided on Ms. Shin Mi-ja, naturalized from Japan, as a candidate for the Gyeongsangbuk-do assembly, and on Ms. Han Erika, naturalized from Thailand, as a candidate for the Busan city council."),
    ("신 씨는 대학교 졸업 후 공무원으로 일하다가 한국인 남편을 만나서 천구백구십이 년에 한국으로 왔다.", "Ms. Shin worked as a civil servant after graduating from university, met a Korean husband and came to Korea in 1992."),
    ("아들 둘을 낳아 키우고, 현재는 경상북도 다문화 여성연합회에서 일하고 있다.", "She bore and raised two sons and now works at the Gyeongsangbuk-do Multicultural Women’s Association."),
    ("한에리카 씨는 태국에서 간호대학에 다니던 중 스무 살 때 한국인 남편을 만나 한국에 왔다.", "While attending nursing college in Thailand, Ms. Han Erika met a Korean husband at the age of twenty and came to Korea."),
    ("현재 시댁 식구 등과 함께 살고 있으며, 부산시 온라인 다문화 여성 네트워크에서 일하고 있다.", "She now lives with her husband’s family and others and works at the Busan Online Multicultural Women’s Network."),
    ("두 후보가 당선되면 처음으로 귀화 외국인이 지방의원으로 뽑히는 것이다.", "If the two candidates are elected, it will be the first time naturalized foreigners are elected as local assembly members."),
]
L8 = lesson(
    "Ch 46 · Connectors in use, and the candidates article",
    "접속사 · 하지만 · 따라서 · 그래도 · 게다가 · 그 후에 · 그러니까 · 수미의 일기 · 귀화 · 지방의원 후보",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): circle the best connector",
             "Read the two sentences and circle the most suitable connector. The book’s sentences with the connector choices; the answers and the English are mine (the blank is written as [ ] here).",
             tables=[table(["Sentences", "Choices", "Answer (mine)"], [[a, b, c] for a, b, c, d, e in _CIR], say=[2]), table(["Completed sentences (mine)"], [[a.replace("[ ]", c)] for a, b, c, d, e in _CIR], say=[0]), table(["English (mine)", "Why (mine)"], [[d, e] for a, b, c, d, e in _CIR])]),
        card("Follow-up 3 (Reading): Sumi’s diary",
             "Read Sumi’s diary and write the numbers in the right order (the first one has been done for you). The book’s six sentences are shown here in my order; the English is mine.",
             tables=[table(["Order (mine)", "Sentence", "English (mine)"], [[n, s, e] for (n, s), e in zip(_DIARY, _DIARY_EN)], say=[1])]),
        card("Activity 3 (Reading): two women who ran for local office",
             "The following newspaper article is about two women who became naturalized Korean citizens and are running for public office. The book asks you to fill in a table in English (the candidate’s original country, party affiliation, office sought and life after coming to Korea). The text is the book’s with the numbers spelled out (2명 is 두 명; 1992년 is 천구백구십이 년; 20세 is 스무 살); the book glosses 귀화: naturalization and 연합회: association. The English is mine.",
             examples=passage(_ART)),
        card("The table filled in (mine)",
             "",
             tables=[table(["", "신미자", "한에리카"], [["Candidate’s original country", "Japan", "Thailand"], ["Candidate’s party affiliation", "The Free Peace Party (자평당)", "The Free Peace Party (자평당)"], ["Office sought", "Gyeongsangbuk-do assembly member", "Busan city council member"], ["Life after coming to Korea", "Came in 1992 after meeting her Korean husband; raised two sons; works at the Gyeongsangbuk-do Multicultural Women’s Association", "Came at age twenty after meeting her Korean husband while attending nursing college in Thailand; lives with her husband’s family; works at the Busan Online Multicultural Women’s Network"]])]),
        card("Activities left out",
             "Follow-up 2 (listening to four incomplete comments cut off after the connector, and writing a possible second sentence) and Follow-up 4 (a pair task: building a ten-sentence story with connectors on a sheet of paper that is passed back and forth, then posting the stories on the wall and voting) are audio, writing and pair activities. In the chapter’s Activities pages, Activity 1 (pairs arrange sentence strips into a well-organized story about Mr. Hwang, a candidate for the National Assembly; the strips are not printed in the student text), Activity 2 (listening to audio clips about a local election in 경상북도: the problem identified and the actions to be taken, and four activities planned by an employee of the 경상북도 선거관리위원회) and Activity 4 (pairs create a presidential election system or change an existing one: direct or indirect, term length, possibility of reelection and three qualifications of candidates, then present it in Korean and the class chooses the best) are audio, strip, pair and group activities."),
    ],
    exercises=uniq(
        _tr(_ART, k=3) + _tr([(a, d) for a, b, c, d, e in _CIR], k=3) + _tr(list(zip([s for n, s in _DIARY], _DIARY_EN)), k=3)
        + [M("Which connector fits: the weather will be clear, [ ] it will rain in the late afternoon?", "하지만", ["그래서", "그전에", "그리고"], "Contrast."), M("Which connector fits: environmental destruction is serious, [ ] efforts are needed?", "따라서", ["하지만", "그리고", "그래도"], "Causality."), M("Which connector fits: I was too sick to get up, [ ] I went to work?", "그래도", ["그래서", "따라서", "그리고"], "Contrast."), M("Which connector fits: my skin is red, [ ] it itches?", "게다가", ["그렇지만", "그럼", "그래서"], "Addition."), M("Which connector fits: I go to the gym after class, [ ] I eat dinner at home?", "그 후에", ["그 결과", "예를 들면", "그러나"], "Sequence."), M("Which connector fits: we are having a housewarming, [ ] please be sure to come?", "그러니까", ["그러나", "그래도", "하지만"], "Causality."),
           M("What is the first sentence of Sumi’s diary?", "내일은 우리 언니의 생일이다", ["그래서 언니가 좋아하는 노란색 모자를 하나 샀다", "반면에 모자는 예쁜 게 많았다", "그런데 예쁜 스카프가 별로 없었다"], "It starts the story."), M("What did Sumi finally buy?", "A yellow hat", ["A scarf", "A bag", "A dress"], "노란색 모자."), M("Which two countries did the two candidates come from?", "Japan and Thailand", ["China and Japan", "Thailand and Vietnam", "Japan and the U.S."], "일본과 태국."), M("What did Ms. Shin do before coming to Korea?", "Worked as a civil servant", ["Studied nursing", "Taught English", "Ran a shop"], "공무원으로 일하다가."), M("What did Ms. Han Erika study in Thailand?", "Nursing", ["Law", "Economics", "Korean"], "간호대학."), M("What would be historic if the two women were elected?", "Naturalized foreigners being elected as local assembly members for the first time", ["A woman becoming president", "A party winning every seat", "A new election law"], "처음으로."),
           F("오늘 낮에는 맑겠습니다. ___ 오후 늦게부터 비가 내리겠습니다. (but)", "하지만", ["그래서", "그리고"], "하지만."), F("환경 파괴가 심각합니다. ___ 환경 보호를 위한 노력이 필요합니다. (therefore)", "따라서", ["하지만", "그래도"], "따라서."), F("오늘 너무 아파서 일어나기 힘들었어요. ___ 일하러 갔어요. (still)", "그래도", ["그래서", "따라서"], "그래도."), F("자평당은 일본에서 ___한 신미자 씨를 후보로 결정했다. (naturalized)", "귀화", ["이민", "입국"], "귀화."), F("두 후보가 ___되면 처음으로 귀화 외국인이 지방의원으로 뽑히는 것이다. (are elected)", "당선", ["낙선", "임명"], "당선."),
           read_q("내일은 우리 언니의 생일입니다"), read_q("그래서 오늘 언니 선물을 사러 백화점에 갔습니다"), read_q("그런데 예쁜 스카프가 별로 없었습니다"), read_q("신미자 씨는 일본에서 귀화했습니다"), read_q("두 후보가 당선되면 처음입니다")]
    ),
)


# ================================================================== L9 Topic C
_C_TXT = [
    ("개인이나 단체가 다른 사람이나 단체를 상대로 고소할 때 하는 재판을 민사 재판이라고 합니다.", "A trial held when an individual or a group files a complaint against another person or group is called a civil trial."),
    ("이와 달리 검사에 의해 기소된 피고인을 상대로 하는 재판은 형사 재판이라고 합니다.", "In contrast to this, a trial against a defendant who was indicted by a prosecutor is called a criminal trial."),
]
_C_FLOW = [
    ("소송이 제기되면 법원에서 재판이 열린다.", "When a lawsuit is filed, a trial is held at a court."),
    ("판사가 피고에 대하여 유죄, 무죄 또는 손해배상 등의 판결을 선고한다.", "The judge announces a judgment on the defendant, such as guilty, not guilty, or compensation for damages."),
    ("판결을 인정한다.", "The judgment is accepted."),
    ("판결을 인정하지 않는다.", "The judgment is not accepted."),
    ("더 높은 법원에 항소한다.", "An appeal is made to a higher court."),
]
_C_WORDS = ["검찰(청)", "고소", "기소", "무죄", "민사", "배상", "법원", "선고", "소송", "~심(리)", "원고", "제기", "집행유예", "유죄", "재판", "징역", "판결", "피고(인)", "항소", "(~)형", "형사", "확정"]
_HYUNG = [("벌금형", "a fine (as a punishment)"), ("징역형", "imprisonment (with hard labor)"), ("사형", "capital punishment")]
_SIM = [("일 심", "the 1st trial; the local court (1심)"), ("이 심", "the 2nd trial; the high court (2심)"), ("삼 심", "the 3rd trial; the supreme court (3심)")]
_COURTS = [("지방법원", "the District Court"), ("고등법원", "the High Court"), ("대법원", "the Supreme Court"), ("특허법원", "the Patent Court"), ("가정법원", "the family court"), ("행정법원", "the administrative court"), ("국민참여재판", "People Participating Trial")]
L9 = lesson(
    "Ch 46 · Topic C: the Korean trial system (한국의 재판 제도)",
    "한국의 재판 제도 · 민사 재판 · 형사 재판 · 소송 · 항소 · 지방법원 · 고등법원 · 대법원 · 삼 심제 · 형 · 심",
    requires=[],
    cards=[
        card("Topic C: the Korean trial system (한국의 재판 제도)",
             "The following information is from a brochure showing the process of a trial and an appeal for civil and criminal cases. (The English is mine; the book gives none.)",
             examples=passage(_C_TXT)),
        card("The process of a trial and an appeal (the brochure’s chart)",
             "The brochure’s chart (a picture, not reproduced here) shows, for both a civil trial (민사 재판) and a criminal trial (형사 재판), these boxes in order; the book’s words are shown with my English, and the dot in 유죄·무죄 is written as a comma. The chart then shows the courts, 지방법원 (District Court), 고등법원 (High Court) and 대법원 (Supreme Court), with an arrow 항소 (appeal) from the first to the second and an arrow 상고 (appeal) from the second to the third.",
             examples=passage(_C_FLOW)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists the conjunctive ending –거든, which is the grammar of this chapter.", tables=_words(_C_WORDS)),
        card("한국어에는: 형 (刑) and 심 (審)",
             "1. 형 (刑), which means punishment (for a crime), is usually used in a legal context and can be combined with nouns that describe a type of punishment, as in 벌금형 (fine), 징역형 (imprisonment [with hard labor]), 사형 (capital punishment), etc.\n\n"
             "2. 심 (審) is derived from the word 심리 (a trial). It literally means “look into” or “investigate” and can be combined with other nouns. Also frequently used in legal contexts, it means a court, as in 1심 (1st trial; the local court), 2심 (2nd trial; the high court), 3심 (3rd trial; the supreme court), etc. (The numbers are spelled out in the table: 일 심, 이 심, 삼 심.)",
             tables=[ktable(_HYUNG), ktable(_SIM)]),
        card("한국에서는: the Korean courts",
             "The Korean judicial system is based on the three-tier trial system (3심제), composed of district courts (지방법원), the high courts (고등법원), and the Supreme Court (대법원). Other courts exercise specialized functions, with the Patent Court (특허법원) at the same level as the high courts; the family court (가정법원) and the administrative court (행정법원) are at the same level as the district courts.\n\n"
             "Unlike U.S. courts where the jury decides a trial’s outcome, almost all court decisions in Korea are made solely by the judge(s). In January 2008, however, 국민참여재판 (People Participating Trial) was introduced and is being implemented in some criminal cases. In this form of trial, the jury relays its verdict to the judge, in the manner of the U.S. judicial system.",
             tables=[ktable(_COURTS)]),
        card("북한에서는: the judiciary of North Korea",
             "In the North Korean judicial process, both adjudicative and prosecuting bodies function as powerful weapons for the proletarian dictatorship. The constitution states that justice is administered by the central court, provincial or special city-level courts, the people’s court, or special courts. The Central Court, the highest court of appeals, stands at the apex of the court system. In the case of special cities directly under central authority, provincial or municipal courts serve as the courts of first instance for civil and criminal cases at the intermediate level. At the lowest level are the people’s courts, established in ordinary cities, counties, and urban districts. Special courts exist for the armed forces and for railroad workers. (Source given by the book: Library of Congress.)"),
        card("Activities left out", "The presentation steps of Topic C (a and d: SMART Board activities; b: reading and listening; c: review with the teacher) are audio and computer activities. The book’s useful website is 대한민국 법원. The Sino-Korean word 법원 (法院) is in the first lesson of the chapter."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT, k=3) + _tr(_C_FLOW, k=3) + _tr(_HYUNG + _SIM + _COURTS, k=3)
        + [M("What is a trial called when one person or group files a complaint against another?", "A civil trial (민사 재판)", ["A criminal trial (형사 재판)", "An appeal", "An election"], "고소할 때 하는 재판."), M("What is a trial against a defendant indicted by a prosecutor called?", "A criminal trial (형사 재판)", ["A civil trial (민사 재판)", "A by-election", "A hearing of the assembly"], "검사에 의해 기소된."), M("What happens when a lawsuit is filed?", "A trial is held at a court", ["The assembly votes", "The president decides", "The case is closed"], "재판이 열린다."), M("What does the judge announce?", "The judgment: guilty, not guilty, or damages", ["A new law", "An election date", "A ministry"], "판결을 선고한다."), M("What do you do if you do not accept the judgment?", "Appeal to a higher court", ["Elect a new judge", "Pay a fine", "Go home"], "더 높은 법원에 항소한다."), M("How many tiers does the Korean trial system have?", "Three", ["Two", "Four", "One"], "삼 심제."), M("Which court is the highest?", "대법원 (the Supreme Court)", ["지방법원", "고등법원", "가정법원"], "삼 심."), M("Which court is at the same level as the high courts?", "특허법원 (the Patent Court)", ["가정법원", "행정법원", "지방법원"], "The book’s note."), M("Which courts are at the same level as the district courts?", "The family court and the administrative court", ["The Patent Court", "The Supreme Court", "The high courts"], "가정법원, 행정법원."), M("Who decides almost all court decisions in Korea?", "The judge(s) alone", ["A jury", "The president", "The assembly"], "No jury (except 국민참여재판)."), M("What is 국민참여재판?", "People Participating Trial, introduced in 2008", ["A civil trial", "An election", "A high court"], "In some criminal cases."), M("What does 형 (刑) mean?", "punishment (for a crime)", ["court", "trial", "complaint"], "벌금형, 징역형, 사형."), M("What does 심 (審) mean?", "a trial; “look into”", ["a fine", "a prison", "a lawyer"], "일 심, 이 심, 삼 심."),
           F("개인이 다른 사람을 ___할 때 하는 재판을 민사 재판이라고 합니다. (to file a complaint)", "고소", ["기소", "임명"], "고소."), F("검사에 의해 ___된 피고인을 상대로 하는 재판은 형사 재판입니다. (indicted)", "기소", ["고소", "당선"], "기소."), F("판결을 인정하지 않으면 더 높은 법원에 ___합니다. (appeal)", "항소", ["투표", "임명"], "항소."), F("판사가 피고에게 징역 일 년을 ___했습니다. (sentenced)", "선고", ["제기", "유세"], "선고."), F("한국의 법원은 삼 ___제입니다. (trial)", "심", ["형", "원"], "삼 심제."),
           read_q("한국의 재판 제도"), read_q("민사 재판"), read_q("형사 재판"), read_q("지방법원과 고등법원과 대법원"), read_q("더 높은 법원에 항소합니다")]
    ),
)

# ================================================================== L10 Follow-ups C: trial descriptions
_TR5 = [
    ("회사에서 일하다가 다쳤는데 회사가 치료비를 안 주었습니다. 그래서 회사를 법원에 고소했습니다. 어제 처음으로 재판이 열렸는데 이 재판에서 판사가 피고인 회사에 손해배상을 하라고 판결했습니다.", "I got hurt while working at a company, but the company did not give me treatment costs. So I filed a complaint against the company in court. The first trial was held yesterday, and in this trial the judge ruled that the defendant company must pay compensation for damages.", "민사재판", "지방법원"),
    ("사기 친 사람을 고소해서 재판을 두 번 했습니다. 그런데 두 번 다 판결이 마음에 안 듭니다. 일 심에서는 피고가 징역 일 년 형을 받았고 이 심에서는 집행유예 십 개월을 받았습니다. 그래서 이 법원에 가서 재판을 받으려고 합니다.", "I filed a complaint against a person who committed fraud, and we had two trials. But I do not like the judgment either time. In the first trial the defendant received a one-year prison sentence, and in the second trial a ten-month suspended sentence. So I intend to go to this court and have a trial.", "형사재판", "대법원"),
    ("어제 오후 사기 혐의로 구속 기소됐던 송 모 씨의 일 심 재판이 열렸습니다. 이동욱 판사는 피고에 대해 오천만 원을 손해 배상하라고 선고했습니다.", "Yesterday afternoon the first trial of Mr. Song, who had been arrested and indicted on a fraud charge, was held. Judge Lee Dong-wook announced that the defendant must pay 50 million won in compensation for damages.", "민사재판", "지방법원"),
    ("이 재판에서 김 모 씨에 대해 징역 오 년의 형이 선고됐습니다. 김 씨는 부모를 폭행한 후 통장을 빼앗아 천오백만 원을 찾아간 혐의로 기소됐었습니다. 김 씨의 변호사에 따르면 김 씨는 이 심에 항소할 것이라고 합니다.", "In this trial, a five-year prison sentence was announced against Mr. Kim. Mr. Kim had been indicted on the charge of assaulting his parents, taking their bankbook and withdrawing 15 million won. According to Mr. Kim’s lawyer, he will appeal to the second trial.", "형사재판", "지방법원"),
    ("국회의원 조형완 씨는 선거법 위반으로 검거돼서 집행유예 이 년 육 개월을 선고받았습니다. 그래서 항소했지만 여기에서도 일 심에서 받은 형이 확정됐습니다.", "National Assembly member Cho Hyeong-wan was arrested for violating the election law and was sentenced to a two-year-six-month suspended sentence. So he appealed, but here too the sentence he received in the first trial was confirmed.", "형사재판", "고등법원"),
]
L10 = lesson(
    "Ch 46 · Follow-ups C: which trial and which court?",
    "민사재판 · 형사재판 · 지방법원 · 고등법원 · 대법원 · 징역 · 집행유예 · 손해배상 · 항소 · 확정",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): read each trial description",
             "Read each trial description and place a check mark next to the type of trial (civil or criminal) and the court (district, high or supreme). The book’s five descriptions are given below with the numbers spelled out (1심 is 일 심; 1년 is 일 년; 5,000만 원 is 오천만 원; 1천500만 원 is 천오백만 원); the English and the answers are mine.",
             tables=[table(["Trial description", "Type of trial (mine)", "Type of court (mine)"], [[a, c, d] for a, b, c, d in _TR5], say=[0, 1, 2]), table(["English (mine)"], [[b] for a, b, c, d in _TR5])]),
        card("Notes on my answers (mine)",
             "1: a lawsuit by the injured worker against the company and an order to pay damages in the first trial: civil, district court. 2: two trials have already been held (a 1-year prison sentence and a suspended sentence), so the next court is the third tier: criminal (징역, 집행유예), Supreme Court. 3: a first trial, so the district court; the description mixes an indictment on a fraud charge (a criminal word) with an order to pay damages, and I mark it civil because the judgment is damages; criminal is arguable. 4: a prison sentence and indictment, so criminal; the lawyer says he will appeal to the second trial, so this is the first trial, district court. 5: criminal (a suspended sentence for violating the election law); he appealed, so this is the second trial at the high court, where the first-trial sentence was upheld."),
        card("Activities left out", "Follow-up 2 (listening to two news clips about a judicial decision: the plaintiff, the defendant(s), the charge and the verdict; the book glosses 전(직): former, ex-) is an audio activity."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c, d in _TR5], k=3)
        + [M("In description 1, what type of trial is it?", "A civil trial", ["A criminal trial", "An election", "An appeal only"], "회사를 고소, 손해배상."), M("In description 1, which court is it?", "The district court", ["The high court", "The Supreme Court", "The family court"], "처음으로 재판."), M("In description 2, what type of trial is it?", "A criminal trial", ["A civil trial", "An election", "A by-election"], "징역, 집행유예."), M("In description 2, which court does the person want to go to?", "The Supreme Court", ["The district court", "The high court", "The patent court"], "Two trials were already held."), M("In description 4, what type of trial is it?", "A criminal trial", ["A civil trial", "An election", "A hearing"], "징역 오 년."), M("In description 4, what will Mr. Kim do?", "Appeal to the second trial", ["Pay damages", "Accept the sentence", "Go to the Supreme Court"], "이 심에 항소."), M("In description 5, what sentence did the Assembly member receive?", "A two-year-six-month suspended sentence", ["A five-year prison sentence", "A fine of 15 million won", "Not guilty"], "집행유예 이 년 육 개월."), M("In description 5, what happened at the appeal?", "The first-trial sentence was confirmed", ["He was found not guilty", "The sentence doubled", "The case was dropped"], "확정됐습니다."), M("What was the charge in description 5?", "Violating the election law", ["Fraud", "Assault", "Theft"], "선거법 위반."), M("What did Mr. Kim take from his parents, according to description 4?", "A bankbook, with which he withdrew money", ["A car", "A house", "Jewelry"], "통장."),
           F("회사를 법원에 ___했습니다. (filed a complaint against)", "고소", ["기소", "항소"], "고소."), F("판사가 피고인 회사에 ___를 하라고 판결했습니다. (compensation)", "손해배상", ["집행유예", "징역형"], "손해배상."), F("피고가 징역 일 년 형을 ___. (received)", "받았습니다", ["했습니다", "맡았습니다"], "받았습니다."), F("김 씨는 이 심에 ___할 것이라고 합니다. (appeal)", "항소", ["투표", "임명"], "항소."), F("일 심에서 받은 형이 ___됐습니다. (confirmed)", "확정", ["제기", "기획"], "확정."),
           read_q("회사를 법원에 고소했습니다"), read_q("피고에게 징역 오 년이 선고됐습니다"), read_q("집행유예를 선고받았습니다"), read_q("항소했지만 형이 확정됐습니다"), read_q("판사가 손해배상을 하라고 판결했습니다")]
    ),
)


# ================================================================== L11 Grammar: -geodeun
_GD = [("시간 있거든 이 책 한번 읽어 봐.", "Try to read this book if you have time."), ("피곤하거든 일찍 자.", "Go to bed early if you are tired."), ("우체국에 가시거든 이 소포도 부쳐 주세요.", "If you go to a post office, send this parcel, too."), ("바쁘지 않거든 저를 좀 도와주세요.", "Please help me if you are not busy."), ("그 일을 이미 시작하셨거든 계속하세요.", "If you already started that task, keep doing it.")]
_GD0 = [("비가 많이 오거든 등산 가지 마세요.", "If it rains heavily, do not go hiking."), ("서울에 도착하거든 전화해.", "If you arrive in Seoul, call me.")]
_GDY = [("오늘 저녁때 영화 못 봐요. 숙제가 많거든요.", "I cannot see a movie tonight; I have a lot of homework.")]
_GDF = [("있거든", "if (you) have; if there is"), ("피곤하거든", "if (you) are tired"), ("가시거든", "if (you) go (honorific)"), ("바쁘지 않거든", "if (you) are not busy"), ("시작하셨거든", "if (you) already started (honorific)"), ("끝나거든", "if (it) is over; if (it) finishes"), ("도착하거든", "if (you) arrive")]
L11 = lesson(
    "Ch 46 · Grammar in Focus: –거든, a conditional in a command or request",
    "문법 탐구 · –거든 · –(으)면 · 명령 · 부탁 · 조건 · –거든요",
    requires=[],
    cards=[
        card("Expressing a conditional in a command/request",
             "In Chapter 9, you learned that the conjunctive ending –(으)면 (if; when) is used to express a conditional, as in 비가 많이 오면 등산 가지 마세요 (If it rains heavily, do not go hiking). The conjunctive ending –거든, which you will learn in this lesson, is also used to express a conditional. However, –거든 is used primarily in a command or request. For example (the book prints 등산가지; the spacing is mine):",
             examples=passage(_GD0)),
        card("Note",
             "Note that –거든 in both sentences is followed by a command or request. The pattern is: verb stem + 거든. (The book titles the pattern “Expressing a Conditional in a Command or Request: verb stem + 거든”.)"),
        card("Examples (the book’s)", "Verb stem + 거든:", examples=passage(_GD), tables=[ktable(_GDF)]),
        card("Do not confuse –거든 with –거든(요)",
             "Be sure not to confuse the conjunctive ending –거든 with the sentence ending –거든(요). The sentence ending –거든요 gives a reason or an explanation; it is not followed by a command:",
             examples=passage(_GDY)),
        card("Activities left out", "Follow-up 1 (Reading, Listening, Speaking: pairs pick verb-phrase strips; Partner A asks Partner B to do something today with –거든, and Partner B declines today but agrees to do it tomorrow with –(으)면; the book’s model is in the next lesson) and Follow-up 2 (video clips from MBC America in which a man makes a request with –거든; the book glosses 무조건: without any reason, unconditionally, 절대로: never and 아가씨: miss, a young lady) are pair and video activities."),
    ],
    exercises=uniq(
        _tr(_GD + _GD0 + _GDY + _GDF, k=3)
        + [M("What does –거든 express?", "A conditional (if), used primarily in a command or request", ["A past tense", "A reason after a statement", "A question"], "The book’s note."), M("What follows –거든?", "A command or request", ["A statement of fact", "A question about the past", "Nothing"], "Used primarily in a command or request."), M("Which ending gives a reason or an explanation?", "–거든요", ["–거든", "–(으)면", "–(으)니까"], "숙제가 많거든요."), M("What does 서울에 도착하거든 전화해 mean?", "If you arrive in Seoul, call me", ["I arrived in Seoul and called", "I will call from Seoul", "Do not call me in Seoul"], "–거든 + command."), M("What does 피곤하거든 일찍 자 mean?", "Go to bed early if you are tired", ["I went to bed early", "I am tired because I slept", "Do not go to bed"], "피곤하거든."), M("What does 오늘 저녁때 영화 못 봐요. 숙제가 많거든요 mean?", "I cannot see a movie tonight; I have a lot of homework", ["If you have homework, see a movie", "I saw a movie after my homework", "Please do my homework"], "–거든요 gives a reason."), M("Which sentence uses –거든 correctly?", "바쁘지 않거든 저를 좀 도와주세요", ["바쁘지 않거든 저는 도왔어요", "바쁘지 않거든 저는 갑니다", "저는 바쁘지 않거든 도와요"], "A request follows."), M("How do you form –거든?", "verb stem + 거든", ["verb stem + 어서", "noun + 거든", "verb stem + 고"], "The book’s pattern."),
           F("시간 있___ 이 책 한번 읽어 봐. (if)", "거든", ["거든요", "으니까"], "–거든."), F("피곤하___ 일찍 자. (if)", "거든", ["거든요", "지만"], "–거든."), F("우체국에 가시___ 이 소포도 부쳐 주세요. (if)", "거든", ["거든요", "는데"], "–거든."), F("바쁘지 않___ 저를 좀 도와주세요. (if)", "거든", ["거든요", "으면서"], "–거든."), F("오늘 영화 못 봐요. 숙제가 많___요. (reason)", "거든", ["으면", "고"], "–거든요."),
           read_q("시간 있거든 이 책 한번 읽어 봐"), read_q("피곤하거든 일찍 자"), read_q("우체국에 가시거든 이 소포도 부쳐 주세요"), read_q("바쁘지 않거든 저를 좀 도와주세요"), read_q("그 일을 이미 시작하셨거든 계속하세요")]
    ),
)

# ================================================================== L12 Activities, 정 모 씨 article, self-evaluation
_MOM = [("지우야, 오늘 학교 일찍 끝나거든 집 안 청소 좀 해. 저녁때 손님이 오실 거야.", "Jiwoo, if school finishes early today, clean the house. Guests will come in the evening.", "School finishes early today", "Clean the house (guests are coming in the evening)"), ("지연아, 이따가 시장에 가거든 우유 좀 사 와. 우유가 다 떨어졌어.", "Jiyeon, if you go to the market later, buy some milk. The milk has run out.", "You go to the market later", "Buy milk (it has run out)"), ("지수야, 오후에 시간 있거든 우체국에 가서 소포 좀 부쳐. 오늘 중으로 꼭 보내야 해.", "Jisu, if you have time in the afternoon, go to the post office and send a parcel. It must be sent without fail by the end of today.", "You have time in the afternoon", "Go to the post office and send a parcel (it must go today)")]
_MODEL = [("김 일병, 오늘 시간이 있거든 방 청소하세요.", "Private Kim, if you have time today, clean the room."), ("저는 오늘 시간이 없어요. 내일 시간이 있으면 방을 청소할게요.", "I do not have time today. If I have time tomorrow, I will clean the room."), ("김 일병, 여행 중에 갑자기 아프면 어떻게 해야 해요?", "Private Kim, what should I do if I suddenly get sick during the trip?"), ("여행 중에 갑자기 아프거든 일일구에 전화하세요.", "If you suddenly get sick during the trip, call 119.")]
_JUD = [("오늘 정 모 씨에 대한 삼 심 재판이 열린다.", "Today the third trial of Mr. Jeong is held."), ("정 모 씨는 지난 칠 월 이십 일 빈집에 들어가 금품을 훔친 혐의로 검찰에 기소되었다.", "Mr. Jeong was indicted by the prosecution on the charge of entering an empty house last July 20 and stealing valuables."), ("부산지방법원에서 열린 일 심 형사재판에서 피고는 징역 육 개월을 선고받았다.", "In the first criminal trial held at the Busan District Court, the defendant was sentenced to six months in prison."), ("피고 정 씨는 일 심 재판의 판결을 인정하지 않고 부산 고등법원에 항소했다.", "The defendant Mr. Jeong did not accept the judgment of the first trial and appealed to the Busan High Court."), ("항소심에서 피고 정 씨는 무죄를 선고받았다.", "In the appeal trial, the defendant Mr. Jeong was found not guilty.")]
_OP2 = [("눈이 오거든 지하철을 타고 출근하세요.", "If it snows, commute by subway."), ("투표일에 시간이 있거든 꼭 투표하세요.", "If you have time on election day, be sure to vote."), ("재판 결과가 마음에 안 들거든 항소하세요.", "If you do not like the result of the trial, appeal."), ("후보자를 정하거든 저에게도 알려 주세요.", "If you decide on a candidate, let me know too."), ("국회에 가거든 의원들에게 이 편지를 전해 주세요.", "If you go to the National Assembly, deliver this letter to the members.")]
L12 = lesson(
    "Ch 46 · Activities: errands, a trial in three tiers, and self-evaluation",
    "활동 · 판사가 되어 봅시다 · 정 모 씨 · 일 심 · 이 심 · 무죄 · 자기 평가 · –거든",
    requires=[],
    cards=[
        card("Follow-up 3 (Reading): the mother’s notes",
             "In the following handwritten notes, a mother asks her three daughters to do some errands related to a specific condition. The book asks you to fill in a table (the condition for the errand and the errand) in English. The notes are the book’s; the English and the table are mine.",
             tables=[table(["Note", "Condition for errand (mine)", "Errand (mine)"], [[a, c, d] for a, b, c, d in _MOM], say=[0]), table(["English of the note (mine)"], [[b] for a, b, c, d in _MOM])]),
        card("The book’s models for the pair tasks",
             "Follow-up 1 (a pair task) has this model: Partner A asks with –거든 and Partner B declines today but agrees for tomorrow with –(으)면. Follow-up 4 (a travel club planning a cross-country walking trip over the summer vacation) has this model: Partner A asks with –(으)면 what to do about a problem and Partner B answers with –거든 (the book prints 119; it is written 일일구 here). The English is mine.",
             examples=passage(_MODEL)),
        card("Activity 3 (Reading, Writing, Speaking, Listening): be the judge",
             "In this activity you read an article about the different trials in a case, as if you are the judge, and then issue the final decree. Part a: read and fill in the table in English. The article is the book’s with the numbers spelled out (3심 is 삼 심; 7월 20일 is 칠 월 이십 일; 1심 is 일 심; 6개월 is 육 개월); the English is mine.",
             examples=passage(_JUD)),
        card("The table filled in (mine)",
             "",
             tables=[table(["", "Sentence (mine)"], [["First trial", "Six months in prison (Busan District Court)"], ["Second trial", "Not guilty (Busan High Court, on appeal)"]])]),
        card("More practice sentences (mine)", "Sample sentences of my own that combine –거든 with the chapter’s vocabulary (the English is mine):", examples=passage(_OP2)),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so that they can provide other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and write about basic features of the Korean government, such as its organizations, leaders, and their roles; talk about the electoral systems for the president, national assembly members, chiefs of local government, and their procedures; identify and talk about the Korean judicial system; and extract information about the judicial system, such as types of sentences, procedures, and judicial decision(s).\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the summary of sentence connectors; the conjunctive ending –거든 (if) used in a command/request; and the Sino-Korean syllables within 입법부 (立法府), 장관 (長官), 투표 (投票), 총선 (總選), and 법원 (法院)."),
        card("Activities left out",
             "Activity 3 parts b to e (partners read the prosecutor’s argument [Text A] or the defense attorney’s argument [Text B] for the first and second trials, exchange them in Korean, consider a final decree and its rationale, and write and present it in the class notebook [MS TEAMS]; the two texts are not printed in the student text), Activity 1 (a SMART Board activity) and Activity 2 (listening to a news report about two trial cases: whether it was a civil or criminal trial, the charge against the defendant and the sentence in the first, second and third trials) are audio, computer and pair activities."),
    ],
    exercises=uniq(
        _tr(_JUD, k=3) + _tr(_OP2, k=3) + _tr([(a, b) for a, b, c, d in _MOM], k=3) + _tr(_MODEL, k=3)
        + [M("What should Jiwoo do if school finishes early today?", "Clean the house", ["Buy milk", "Send a parcel", "Cook dinner"], "집 안 청소."), M("What should Jiyeon do if she goes to the market?", "Buy some milk", ["Clean the house", "Send a parcel", "Buy fish"], "우유."), M("What should Jisu do if she has time in the afternoon?", "Go to the post office and send a parcel", ["Buy milk", "Clean the house", "Meet a guest"], "소포."), M("Why must the house be cleaned?", "Guests will come in the evening", ["It is a holiday", "It is raining", "Mother is sick"], "저녁때 손님."), M("What did Mr. Jeong stand accused of?", "Entering an empty house and stealing valuables", ["Fraud", "Assault", "Violating the election law"], "빈집에 들어가 금품을 훔친."), M("What sentence did Mr. Jeong receive in the first trial?", "Six months in prison", ["Not guilty", "A fine", "Five years"], "징역 육 개월."), M("What happened in the appeal trial?", "He was found not guilty", ["The sentence doubled", "The case was dismissed by the Supreme Court", "He was fined"], "무죄."), M("Where was the first trial held?", "The Busan District Court", ["The Busan High Court", "The Supreme Court", "The Seoul District Court"], "부산지방법원."), M("In the book’s model, what does Partner B promise?", "To clean the room if there is time tomorrow", ["To clean it today", "To never clean it", "To call 119"], "내일 시간이 있으면."), M("In the book’s travel model, what should you do if you suddenly get sick?", "Call 119", ["Go home", "Walk on", "Call the police"], "일일구에 전화하세요."),
           F("눈이 오___ 지하철을 타고 출근하세요. (if)", "거든", ["거든요", "는데"], "–거든."), F("투표일에 시간이 있___ 꼭 투표하세요. (if)", "거든", ["거든요", "지만"], "–거든."), F("재판 결과가 마음에 안 들거든 ___하세요. (appeal)", "항소", ["투표", "임명"], "항소."), F("피고는 일 심 형사재판에서 징역 육 개월을 ___받았다. (sentenced)", "선고", ["제기", "유세"], "선고받다."), F("항소심에서 피고 정 씨는 ___를 선고받았다. (not guilty)", "무죄", ["유죄", "징역"], "무죄."),
           read_q("눈이 오거든 지하철을 타고 출근하세요"), read_q("투표일에 시간이 있거든 꼭 투표하세요"), read_q("재판 결과가 마음에 안 들거든 항소하세요"), read_q("항소심에서 피고는 무죄를 선고받았습니다"), read_q("여행 중에 갑자기 아프거든 일일구에 전화하세요")]
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
    "Ch 46 · Core vocabulary",
    "주요 단어 · 정치 · 선거 · 재판 · 거든 · 입법부 · 장관 · 투표 · 총선 · 법원",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. The last section lists the Sino-Korean related words of 입법부, 장관, 투표, 총선 and 법원 as the book gives them.\n\n"
             "The example sentences with digits are respelled in Hangul (the book’s 2022 and similar numbers; for example 5-year terms and 3-year sentences are read in Korean numbers: 사 년, 삼 년). The book’s 1심, 2심 and 3심 are written 일 심, 이 심, 삼 심."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 대통령 mean?", "the president", ["the prime minister", "a minister", "a judge"], "大統領."), M("What does 총리 mean?", "the prime minister", ["the president", "a mayor", "a judge"], "總理."), M("What does 장관 mean?", "a cabinet minister", ["a judge", "a mayor", "a member of the assembly"], "長官."), M("What does 국회 mean?", "the National Assembly", ["a court", "a ministry", "a party"], "國會."), M("What does 정당 mean?", "a political party", ["a government", "a court", "a vote"], "政黨."), M("What does 후보자 mean?", "a candidate", ["a voter", "a judge", "a plaintiff"], "候補者."), M("What does 유권자 mean?", "a voter", ["a candidate", "a prosecutor", "a defendant"], "有權者."), M("What does 낙선 mean?", "losing an election", ["winning an election", "an election", "a vote"], "落選."), M("What does 당선 mean?", "winning an election", ["losing an election", "a trial", "a campaign"], "當選."), M("What does 법원 mean?", "a court of justice", ["a ministry", "an assembly", "a party"], "法院."), M("What does 재판 mean?", "a trial", ["a vote", "an election", "a policy"], "裁判."), M("What does 판결 mean?", "a judgment; a judicial decision", ["a complaint", "an appeal", "a fine"], "判決."), M("What does 무죄 mean?", "innocence; not guilty", ["guilt", "a fine", "a lawsuit"], "無罪."), M("What does 유죄 mean?", "guilt", ["innocence", "an appeal", "a plaintiff"], "有罪."), M("What does 항소 mean?", "an appeal (to an appellate court)", ["a complaint", "an indictment", "a verdict"], "抗訴."), M("What does 징역 mean?", "imprisonment (with hard labor)", ["a fine", "probation", "an acquittal"], "懲役."), M("What does 집행유예 mean?", "probation; a suspended sentence", ["a fine", "an acquittal", "an appeal"], "執行猶豫."), M("What does 원고 mean?", "a plaintiff", ["a defendant", "a judge", "a prosecutor"], "原告."), M("What does 피고 mean?", "a defendant", ["a plaintiff", "a judge", "a voter"], "被告."), M("What does –거든 mean?", "if (in a command or request)", ["because", "although", "after"], "The grammar of the chapter."),
           F("국무총리는 ___의 장관들과 함께 국무회의를 엽니다. (executive branch)", "행정부", ["입법부", "사법부"], "행정부."), F("오늘은 총선일이니까 꼭 ___하세요. (vote)", "투표", ["개표", "유세"], "투표."), F("이번 대통령 선거에는 아홉 명의 ___가 등록했습니다. (candidates)", "후보자", ["유권자", "정당"], "후보자."), F("대통령의 ___는 오 년입니다. (term of office)", "임기", ["절차", "원칙"], "임기."), F("판사가 피고에게 무죄 ___을 내렸습니다. (judgment)", "판결", ["고소", "소송"], "판결."),
           read_q("주요 단어"), read_q("정치"), read_q("대통령"), read_q("재판"), read_q("판결")]
    ),
)

UNIT = unit("Semester 2 · Unit 12 · Chapter 46: Politics (정치)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])

"""Unit 47: KBC Semester 2, Unit 10, Chapter 40 - The Environment (환경).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 10, Student's Edition (2022).
Audio, video, pictures, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 40 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("겉", "surface; exterior; outside", "그릇의 겉과 속을 깨끗하게 닦으세요."),
    ("계란 / 달걀", "(鷄卵) an egg", "식품점에 가는 김에 계란 두 팩만 사다 주세요."),
    ("껍질", "shell; bark; skin", "사과는 잘 씻은 후에 껍질까지 다 먹는 것이 좋아요."),
    ("꽁초", "a cigarette butt", "담배꽁초를 아무 데나 버리면 안 됩니다."),
    ("내용물", "(內用物) contents (i.e. of any kind of container)", "내용물을 알 수 없는 이상한 소포가 와서 경찰에 신고했다."),
    ("딱딱하다", "to be hard; to be stiff", "이 침대가 너무 딱딱해서 좀 불편해요."),
    ("또는", "or", "새 프로그램을 설치 또는 제거하기 전에 저한테 먼저 얘기해 주세요."),
    ("뚜껑", "a lid; a cover; a cap", "요리할 때 냄비 뚜껑을 닫아야 물이 빨리 끓어요."),
    ("말리다", "to dry (laundry, fish, etc.); to dehydrate (a thing)", "빨래를 밖에서 말리면 전기를 절약할 수 있습니다."),
    ("무색", "(無色) colorlessness", "이 선크림은 무색이니까 목이나 손에도 바를 수 있어요."),
    ("묶다", "to bind; to tie", "쓰레기 봉지를 꼭 묶어서 버리세요."),
    ("물기", "wetness; dampness; “water feel”", "야채를 튀기기 전에 물기를 완전히 빼세요."),
    ("배출", "(排出) emission; discharge; disposal of waste; to emit; to discharge; to dispose of / to be emitted; to be discharged; to be disposed of (~하다/되다)", "불에 타는 쓰레기는 흰색, 타지 않는 쓰레기는 녹색 봉투에 넣어 배출하세요."),
    ("봉투", "(封套) an envelope; a bag", "편지 봉투는 문방구에서 구입할 수 있습니다."),
    ("분리", "(分離) separation; to separate / to be separated (~하다/되다)", "재활용 쓰레기와 음식 쓰레기는 분리해서 버려야 합니다."),
    ("비우다", "to empty (out); to vacate", "주말에 냉장고를 다 비우고 깨끗이 청소했어요."),
    ("속", "inside; content; the stomach", "어제 술을 많이 마셔서 속이 아픕니다."),
    ("수거", "(收去) collection (and taking away of things); to collect / to be collected (~하다/되다)", "우리 동네는 매주 목요일에 쓰레기를 수거합니다."),
    ("썩다", "to become rotten; to decay; to corrode", "과일은 금방 썩으니까 산 후에 빨리 드세요."),
    ("압축", "(壓縮) compression; flattening; to compress; to flatten / to be compressed; to be flattened (~하다/되다)", "캔은 깨끗이 씻어서 압축한 후에 버리세요."),
    ("없애다", "to get rid of; to remove", "대청소를 하면서 쓰지 않는 물건을 다 없앴다."),
    ("우유", "(牛乳) milk; “cow milk”", "요즘 저지방 우유의 인기가 높아지고 있습니다."),
    ("유리", "(琉璃) glass", "유리는 깨지기 쉬우니까 조심하세요."),
    ("이물질", "(異物質) foreign object (matter, body, material)", "눈에 작은 이물질이 들어가서 안과에 갔다 왔어요."),
    ("제거", "(除去) removal; to remove / to be removed (~하다/되다)", "음료수 캔을 버릴 때는 캔의 알루미늄 뚜껑을 제거한 후에 버려야 합니다."),
    ("종량제", "(從量制) the meter-rate system", "한국에서는 쓰레기를 버릴 때 꼭 종량제 봉투를 써야 합니다."),
    ("짜다", "to squeeze; to wring", "젖은 옷을 짜서 다시 입었다."),
    ("팩", "a pack; a carton", "모든 팩은 버릴 때 먼저 깨끗이 씻으세요."),
    ("페트병", "PET (polyethylene terephthalate) bottle; PET plastic bottle", "무색 페트병을 배출할 때 뚜껑을 닫고 버리세요."),
    ("헹구다", "to wash out; to rinse out", "설거지할 때 깨끗이 헹구어야 합니다."),
]
_CV_B = [
    ("감소", "(減少) decrease; to decrease / to be decreased (~하다/되다)", "일부 선진국의 인구가 점점 감소하고 있습니다."),
    ("관측", "(觀測) observation; to observe / to be observed (~하다/되다)", "엘니뇨의 영향으로 바닷물의 온도가 높아진 것으로 관측되고 있습니다."),
    ("기후", "climate", "기후가 변화하게 되면 생태계가 파괴될 수 있습니다."),
    ("남극", "(南極) the South Pole; the Antarctic; “south extreme”", "남극의 빙하가 조금씩 녹고 있어요."),
    ("녹다", "to melt; to thaw; to dissolve", "밤새 내린 눈이 아직 녹지 않아서 길이 미끄러워요."),
    ("농작물", "(農作物) the crops; a harvest; farm produce", "저는 내일 주말 농장에 가서 감자 같은 농작물을 심을 거예요."),
    ("대책", "a (counter) measure; a plan", "이재민을 위한 대책을 마련했습니다."),
    ("~ 등", "(等) and so on; etc.", "우리 학교에는 중국인, 일본인 등 외국인 학생들이 많이 있어요."),
    ("~배", "times", "최근 폭염으로 멜론 값이 두 배가 올랐다."),
    ("보도", "(報道) news; a report; to report / to be reported (~하다/되다)", "이번 뉴스는 이진수 기자가 보도하겠습니다."),
    ("북극", "(北極) the North Pole; the Arctic; “north extreme”", "올겨울 북극 기온이 영하 오십 도까지 내려갔습니다."),
    ("빙하", "(氷河) a glacier; “iced water”", "남극의 오존층이 파괴되고 빙하가 녹고 있습니다."),
    ("상승", "(上昇) rise; to rise; to ascend; to go up (~하다/되다)", "한국의 아파트 값이 계속 상승하고 있어요."),
    ("생태계", "(生態系) an ecosystem", "외국의 동물 식물이 들어와 한국의 생태계에 나쁜 영향을 미치고 있다."),
    ("수확량", "(收穫量) a yield; “harvest amount”", "올해는 가뭄과 홍수 때문에 농작물 수확량이 많이 줄었어요."),
    ("예측", "(豫測) prediction; to predict / to be predicted (~하다/되다)", "기상청은 다음 주에 폭설이 내릴 것이라고 예측했습니다."),
    ("온난화", "(溫暖化) (global) warming", "지구 온난화의 영향으로 세계 곳곳에서 많은 자연재해가 발생하고 있다."),
    ("온도", "(溫度) temperature", "실내 온도가 너무 높으면 건강에 나쁘다."),
    ("온실가스", "(溫室) greenhouse gas; “warm room gas”", "이산화탄소 배출량이 증가해서 온실가스가 늘어나고 있어요."),
    ("이산화탄소", "(二酸化炭素) carbon dioxide", "이산화탄소는 지구온난화를 일으키는 대표적인 온실가스다."),
    ("전역", "(全域) the whole area; the whole district; the whole region", "미국 전역에 한파가 몰아쳤습니다."),
    ("제한", "(制限) a limit; restriction; to limit; to restrict (~하다)", "독일의 아우토반은 속도제한이 없습니다."),
    ("주제", "topic; subject", "서울시에서는 지구의 날에 쓰레기를 위한 지구는 없다를 주제로 환경에 관한 다양한 행사를 열었습니다."),
    ("지구", "(地球) (the) Earth; (the) globe", "세계의 기후 전문가들은 지구의 온도 상승을 일 점 오 도로 제한하자고 요구했다."),
    ("파괴", "(破壞) destruction; demolition; to destroy / to be destroyed (~하다/되다)", "역에서 일어난 폭발 사고로 근처 건물이 모두 파괴됐어요."),
    ("해수면", "(海水面) sea level; “sea water surface”", "해수면의 상승으로 제주도의 낮은 해안 지역이 침수되었습니다."),
    ("해안", "coast; beach; shore", "서해안 일부 지역에서 눈이 내리겠습니다."),
    ("협력", "(協力) cooperation; to cooperate with (~하다)", "군과 경찰, 시민들이 서로 협력하여 구조작업을 하고 있다."),
]
_CV_C = [
    ("경차", "(輕車) a compact car; “light car”", "요즘은 기름값이 비싸서 경차가 인기예요."),
    ("권장", "(勸奬) an exhortation; encouragement; to exhort; to encourage / to be encouraged (~하다/되다)", "건강을 위해서 규칙적으로 운동할 것을 권장합니다."),
    ("냉방", "(冷房) air conditioning; air cooling; “cool room”", "이 건물은 냉방시설이 잘 돼 있어서 여름에도 덥지 않아요."),
    ("보조금", "a subsidy; grant money; “assisting money”", "목포시는 친환경 화물차를 구매하는 경우 보조금을 지원하기로 했다."),
    ("보존", "(保存) preservation; conservation; to preserve; to conserve / to be preserved (~하다/되다)", "미래 세대를 위해 우리의 문화재를 잘 보존해야 합니다."),
    ("보호", "(保護) protection; shelter; care; to protect / to be protected (~하다/되다)", "산불로부터 자연을 보호합시다."),
    ("사실", "fact; in fact; actually; as a matter of fact", "사십 대 남자배우가 음주운전을 했다는 보도는 사실이 아닌 것으로 확인됐다. 사실 나는 네가 나한테 계속 거짓말 하고 있다는 것을 처음부터 알고 있었어."),
    ("선정", "(選定) selection; choosing; to select; to choose / to be selected (~하다/되다)", "시민환경단체의 대표로 김숙현 씨가 선정되었습니다."),
    ("시민", "(市民) a citizen", "시민의 도움으로 폭행 사건의 용의자를 잡았습니다."),
    ("시장", "(市長) a mayor; “city chief”", "올 시월에는 새로 시장을 뽑게 됩니다."),
    ("식물", "(植物) a plant; plant life; vegetation; “planted thing”", "식물원에 가면 세계 여러 나라의 식물을 볼 수 있어요."),
    ("실천", "(實踐) practice; putting (something) into practice; to practice / to be practiced (~하다/되다)", "올해는 계획한 대로 실천하고 싶어요."),
    ("이면지", "(裏面紙) scratch paper; “inner face paper”", "새 종이가 하나도 없어서 이면지를 쓰고 있습니다."),
    ("일상", "(日常) everyday life; daily life", "한국어 공부가 저의 일상입니다."),
    ("일회용품", "(一回用品) disposable goods; “one-time use item”", "일회용품은 사용하기 편리하지만 환경을 오염시킵니다."),
    ("자원", "(資源) resources", "종이, 물, 기름 같은 자원을 아껴 쓰는 습관을 기릅시다."),
    ("자제", "(自制) refraining from (doing something); self-control; to refrain from; to control oneself (~하다)", "먹고 싶은 것이 많지만 건강을 위해 자제하고 있어요."),
    ("지나치다", "to go too far; to be too much; to be extreme", "다른 사람이 옆에 있을 때 지나치게 큰 소리로 말하지 마세요."),
    ("지정", "(指定) designation; appointment; to designate / to be designated (~하다/되다)", "담배는 지정된 장소에서만 피울 수 있다."),
    ("충전소", "a charging station", "전기차를 이용하는 고객이 늘고 있지만 전기차 충전소는 많이 부족한 것으로 나타났습니다."),
    ("친환경", "(親環境) environment-friendly; eco-friendly; “pro-environment”", "자연을 사랑하십니까? 그러면 친환경 제품을 이용하세요."),
    ("평소", "(平素) ordinary times; average day", "어제는 평소보다 더 많이 잤어요."),
    ("홍보", "(弘報) public relations; publicity; (public) information; to do PR; to inform the public (~하다)", "정부는 티브이 광고로 새로 바뀐 정책을 홍보하고 있습니다."),
]
_CV_GR = [
    ("-자", "(as soon) as; (right) after; when", "폭우가 쏟아지자 도로가 물에 잠겼어요."),
    ("an attributive form + 것으로", "expressions frequently used in news reports", "다음 주까지 폭우가 계속될 것으로 예보됐습니다."),
    ("-(으)ㅁ / -(으)ㄹ 것", "abbreviated verb endings used in writing", "내일 시험은 다음 주로 연기되었음. 주말에도 배운 것을 복습할 것."),
    ("(만약) … -다면", "conjunctive ending for a hypothetical condition", "만약 남한과 북한이 통일된다면 어떻게 될까요?"),
]
_CV_SINO = [("경차", "(輕車) a compact car; “a light car”", "경상, 경범죄, 경시, 기차, 주차장, 승용차"), ("분리", "(分離) separation", "분단, 대부분, 충분, 이탈, 이륙, 이혼"), ("식물", "(植物) a plant", "이식, 식수, 식목일, 물질, 동물, 생물"), ("온난화", "(溫暖化) (global) warming", "온도, 온돌, 체온, 난류, 난방, 난로, 변화, 간소화, 세계화"), ("재활용", "(再活用) recycling; reuse", "재혼, 재수, 재개발, 활동, 생활, 활발, 버스 전용, 유용, 사무용품")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"계란 / 달걀": "an egg", "~ 등": "and so on; etc.", "~배": "times"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_S1 = [("분", "a minute; “fraction (of an hour)”"), ("분대", "squad; “divided group”"), ("분수", "fraction; “fractional number”"), ("이유기", "weaning period; “milk detachment period”")]
_S1G = [("분단", "division (of a country); partition"), ("대부분", "most; the majority"), ("충분", "enough; sufficient"), ("이탈", "breaking away; deviation"), ("이륙", "takeoff (of a plane)"), ("이혼", "divorce")]
_S2 = [("재방송", "rebroadcasting; a re-run"), ("재시험", "reexamination; a makeup exam"), ("활동", "activity; action"), ("군사용", "military use"), ("일회용", "disposable; “one-time use”")]
_S2G = [("재혼", "remarriage"), ("재검사", "reinspection; a retest"), ("재개발", "redevelopment"), ("재활", "rehabilitation"), ("생활", "life; living"), ("활화산", "an active volcano; “live fire mountain”"), ("버스전용", "bus-only"), ("군용차량", "a military vehicle"), ("사무용품", "office supplies")]
_S3 = [("온도", "temperature; “degree of warmth”"), ("난방", "heating a room"), ("서구화", "Westernization"), ("미국화", "Americanization")]
_S3G = [("난풍", "a warm wind"), ("온천", "a hot spring"), ("체온", "body temperature"), ("난류", "a warm current"), ("난로", "a heating stove"), ("자동화", "automation"), ("세계화", "globalization"), ("간소화", "simplification")]
_S4 = [("경공업", "light industry")]
_S4G = [("경상", "a light injury"), ("경범죄", "a minor offense"), ("경비행기", "a light aircraft"), ("기차", "a train"), ("주차장", "a parking lot"), ("승용차", "a passenger car")]
_S5 = [("동식물", "animals and plants; “moving things and planted things”"), ("고물", "an antique; “ancient thing”"), ("물가", "price; “prices of things”")]
_S5G = [("이식수술", "transplant surgery"), ("식물학", "botany"), ("식목일", "Arbor Day; “tree-planting day”"), ("물리학", "physics"), ("동물", "an animal"), ("생물", "a living thing; an organism")]

# ================================================================== L1
L1 = lesson(
    "Ch 40 · What the chapter teaches, 분리 · 재활용 · 온난화 · 식물 · 경차",
    "환경 · 분리 · 재활용 · 온난화 · 식물 · 경차 · 이식 · 난방 · 활동",
    requires=[],
    cards=[
        card("What Chapter 40 teaches (환경)",
             "Chapter 40, “The Environment”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify waste separation and disposal methods; extract factual information about and discuss global warming, its causes, impact, and preventive measures; make suggestions on how to reduce food waste; and talk about the efforts to conserve resources and protect the environment.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; the conjunctive ending –자; expressions frequently used in news reports; –(으)ㅁ and –(으)ㄹ 것, abbreviated verb endings used in writing; the conjunctive ending –다면 for a hypothetical condition; and the Sino-Korean syllables within 분리 (分離), 재활용 (再活用), 온난화 (溫暖化), 식물 (植物), and 경차 (輕車)."),
        card("Sino-Korean in use: 분리 (分離)",
             "The syllable 분 (分) means division, section, or fraction, as in 분 (minute; “fraction [of an hour]”), 분대 (squad; “divided group”), and 분수 (fraction; “fractional number”). 리 (離) means detachment, separation, or “off”, as in 이유기 (weaning period; “milk detachment period”). Note that 리 turns into 이 at the beginning of a word. Thus, the literal meaning of the word 분리 is “separation and division” and refers to separation, secession, disunion, split, etc. The book asks you to guess the meaning of 분단, 대부분, 충분, 이탈, 이륙 and 이혼 (my answers are in the table).",
             tables=[ktable(_S1), ktable(_S1G)]),
        card("Sino-Korean in use: 재활용 (再活用)",
             "The syllable 재 (再) means again, twice, or re-, as in 재방송 (rebroadcasting; a re-run) and 재시험 (reexamination; a makeup exam). 활 (活) means life or live(ly), as in 활동 (activity; action), and 용 (用) means use, as in 군사용 (military use) and 일회용 (disposable; “one-time use”). Thus, the literal meaning of the Sino-Korean word 재활용 is “revive and use”, and it means recycling or reuse. The book asks you to guess the meaning of words that contain one of these syllables (the book glosses 화산: a volcano, “fire mountain”; my answers):",
             tables=[ktable(_S2), ktable(_S2G)]),
        card("Sino-Korean in use: 온난화 (溫暖化)",
             "The syllable 온 (溫) means warm or warmth, as in 온도 (temperature; “degree of warmth”). The syllable 난 (暖) also means warm or heating, as in 난방 (heated room; heating a room). The syllable 화 (化) means change, become, or -ization/-fication, as in 서구화 (Westernization) and 미국화 (Americanization). Thus, the literal meaning of 온난화 is “change of warmth” or “becoming warm”; it generally refers to global warming. The book glosses 유/류 (流): flow; 풍 (風): wind; 노/로 (爐): a fire stove (my answers):",
             tables=[ktable(_S3), ktable(_S3G)]),
        card("Sino-Korean in use: 경차 (輕車)",
             "The Chinese character of the syllable 경 (輕) depicts a vehicle on wheels crossing a stream and it means light or small, as in 경공업 (light industry). 차 (車) means vehicle on wheels or car. Thus, the literal meaning of the Sino-Korean word 경차 is “light car” or “small car”, and the word refers to a compact car or small car. The book asks you to guess the meaning of words that contain one of these syllables (my answers):",
             tables=[ktable(_S4), ktable(_S4G)]),
        card("Sino-Korean in use: 식물 (植物)",
             "The Chinese character of the syllable 식 (植) depicts a straight tree, and the syllable means plant (vs. animal) or planting, as in 동식물 (animals and plants; “moving things and planted things”). 물 (物) means thing, object, or material, as in 고물 (an antique; “ancient thing”) and 물가 (price; “prices of things”). Thus, the literal meaning of the Sino-Korean word 식물 is “planted things”, and it refers to a plant, plant life, or vegetation. The book glosses 이 (移): move (my answers):",
             tables=[ktable(_S5), ktable(_S5G)]),
    ],
    exercises=uniq(
        _tr(_S1 + _S1G + _S2 + _S2G + _S3 + _S3G + _S4 + _S4G + _S5 + _S5G, k=3)
        + [M("What does 분 (分) mean?", "division; section; fraction", ["again", "warm", "plant"], "분대."), M("What does 재 (再) mean?", "again; twice; re-", ["warm", "plant", "light"], "재방송."), M("What does 용 (用) mean?", "use", ["life", "again", "thing"], "일회용."), M("What does 온 (溫) mean?", "warm; warmth", ["cold", "light", "plant"], "온도."), M("What does 화 (化) mean?", "change; become; -ization", ["warm", "thing", "separate"], "서구화."), M("What does 경 (輕) mean?", "light; small", ["heavy", "warm", "plant"], "경공업."), M("What does 식 (植) mean?", "plant; planting", ["animal", "thing", "car"], "동식물."), M("What is the literal meaning of 재활용?", "“revive and use”", ["“separation and division”", "“light car”", "“planted things”"], "재 + 활 + 용."), M("What is the literal meaning of 온난화?", "“change of warmth” or “becoming warm”", ["“light car”", "“planted things”", "“revive and use”"], "온 + 난 + 화."), M("What is the literal meaning of 식물?", "“planted things”", ["“light car”", "“revive and use”", "“becoming warm”"], "식 + 물."), M("What is the literal meaning of 경차?", "“light car” or “small car”", ["“planted things”", "“becoming warm”", "“separation and division”"], "경 + 차."),
           F("쓰레기 ___ 수거를 합니다. (separation)", "분리", ["분단", "분수"], "분리."), F("캔은 ___용해서 새 제품을 만든다. (recycle)", "재활", ["재혼", "재검"], "재활용."), F("겨울에는 ___를 켜서 방을 따뜻하게 한다. (heating stove)", "난로", ["난류", "온천"], "난로."), F("기름값이 비싸서 ___가 인기예요. (compact car)", "경차", ["승용차", "기차"], "경차."), F("___원에 가서 세계의 식물을 봤어요. (botanical garden; plant)", "식물", ["동물", "생물"], "식물원."),
           read_q("분리"), read_q("재활용"), read_q("온난화"), read_q("식물"), read_q("경차")]
    ),
)

# ================================================================== L2 Vocabulary builder
_PHR = [("생태계가", "파괴되다", "the ecosystem is destroyed"), ("일회용품 사용을", "자제하다", "to refrain from using disposable goods"), ("대책을", "요구하다", "to demand measures"), ("친환경 제품", "권장하다", "to encourage environment-friendly products"), ("경차를", "타다", "to ride in (drive) a compact car"), ("지구의 온도가", "상승하다", "the temperature of the Earth rises"), ("온실가스를", "배출하다", "to emit greenhouse gas"), ("재활용품을", "수거하다", "to collect recyclables"), ("환경보호를", "실천하다", "to put environmental protection into practice")]
_HAND = [("우리 모두 환경을 보호하기 위해 노력해야 합니다.", "보호", "We must all make an effort to protect the environment."), ("한 번 쓰고 버리는 나무 젓가락의 사용을 자제합시다.", "자제", "Let’s refrain from using wooden chopsticks that are used once and thrown away."), ("일회용품은 편리하지만 환경에 좋지 않습니다.", "일회용품", "Disposable goods are convenient but not good for the environment."), ("그리고 온실가스를 줄이기 위해서 냉장고나 에어컨 사용을 줄여야 합니다.", "온실가스", "And in order to reduce greenhouse gas, we must reduce the use of refrigerators and air conditioners."), ("특히 에어컨은 온실가스를 많이 배출합니다.", "배출", "In particular, air conditioners emit a lot of greenhouse gas."), ("환경 보호를 위해 자기가 할 수 있는 가장 쉬운 것부터 천천히 하나씩 실천하도록 합시다.", "실천", "For environmental protection, let’s put into practice, one at a time and slowly, starting with the easiest things we can do.")]
L2 = lesson(
    "Ch 40 · Vocabulary Builder: combined phrases and an environment seminar handout",
    "생태계가 파괴되다 · 일회용품 사용을 자제하다 · 온실가스를 배출하다 · 재활용품을 수거하다 · 환경보호를 실천하다",
    requires=[],
    cards=[
        card("새 단어: nouns and verbs",
             "The book asks you to skim the words in the table, circle those whose meanings you do not know, and write the English translation of each combined phrase. The noun and verb pairs are the book’s; the English is mine:",
             tables=[table(["Noun", "Verb", "English (mine)"], [[a, b, c] for a, b, c in _PHR], say=[0, 1])]),
        card("Activity 1: a handout from an environmental protection seminar",
             "The following handout is from a seminar on environmental protection and is missing some words; the book asks you to complete the sentences with the words in the box 온실가스, 보호, 자제, 배출, 실천, 일회용품. The sentences below are completed with my answers; the English is mine.",
             examples=passage([(a, c) for a, b, c in _HAND]),
             tables=[table(["Blank filled with", "Sentence"], [[b, a] for a, b, c in _HAND], say=[0, 1])]),
        card("Activities left out", "Activities 2 and 3 (SMART Board) and the PowerPoint Sino-Korean presentation need the SMART Board and PowerPoint."),
    ],
    exercises=uniq(
        _tr([(a + " " + b, c) for a, b, c in _PHR], k=3) + _tr([(a, c) for a, b, c in _HAND], k=3)
        + [M("What goes in the blank of “환경을 [ ]하기 위해 노력해야 합니다”?", "보호", ["배출", "자제", "실천"], "My answer."), M("What goes in the blank of “나무 젓가락의 사용을 [ ]합시다”?", "자제", ["보호", "배출", "온실가스"], "My answer."), M("What goes in the blank of “에어컨은 온실가스를 많이 [ ]합니다”?", "배출", ["보호", "자제", "실천"], "My answer."), M("What goes in the blank of “하나씩 [ ]하도록 합시다”?", "실천", ["배출", "보호", "자제"], "My answer."), M("Which word is the subject of “reduce … by reducing refrigerators”?", "온실가스", ["일회용품", "젓가락", "환경"], "온실가스."),
           F("일회용품 사용을 ___하다 (refrain)", "자제", ["배출", "수거"], "자제하다."), F("온실가스를 ___하다 (emit)", "배출", ["수거", "권장"], "배출하다."), F("재활용품을 ___하다 (collect)", "수거", ["배출", "권장"], "수거하다."), F("생태계가 ___되다 (destroyed)", "파괴", ["상승", "감소"], "파괴되다."), F("친환경 제품을 ___하다 (encourage)", "권장", ["수거", "배출"], "권장하다."),
           read_q("생태계가 파괴되다"), read_q("일회용품 사용을 자제하다"), read_q("온실가스를 배출하다"), read_q("재활용품을 수거하다"), read_q("환경보호를 실천하다")]
    ),
)

# ================================================================== L3 Topic A
_A_SEC = [
    ("쓰레기 분리수거", "쓰레기를 줄이고 재활용을 늘려 환경을 보호합시다.", "Let’s reduce trash, increase recycling and protect the environment."),
]
_A_PAPER = [("신문, 책, 종이, 상자, 달력 등은 비닐 코팅 등을 제거한 후 하나로 묶어 배출한다.", "Newspapers, books, paper, boxes, calendars, etc.: remove the vinyl coating, etc., then bind them into one and dispose of them."), ("우유 팩, 음료수 팩, 종이컵은 내용물을 다 비우고 물로 깨끗이 헹군다.", "Milk cartons, beverage cartons, paper cups: empty the contents completely and rinse them clean with water."), ("잘 말린 후에 압축해서 배출한다.", "After drying them well, compress them and dispose of them.")]
_A_GLASS = [("먼저 플라스틱이나 알루미늄 뚜껑, 또는 라벨을 제거한다.", "First remove the plastic or aluminum lid, or the label."), ("내용물을 제거한 뒤 깨끗이 헹구고 병 색깔에 따라 분리한다.", "After removing the contents, rinse them clean and separate them by bottle color."), ("담배꽁초 등 이물질을 병 안에 넣지 말 것.", "Do not put foreign objects such as cigarette butts inside the bottle.")]
_A_CAN = [("겉에 라벨 등이 있으면 제거한다.", "If there is a label, etc. on the outside, remove it."), ("속의 내용물을 비운 후 물로 헹구고 압축한다.", "After emptying the contents inside, rinse with water and compress."), ("물이나 음료수용 무색 페트병은 전용 수거함에 배출한다.", "Colorless PET bottles for water or beverages are disposed of in the special collection box."), ("다른 페트병들은 플라스틱 수거함에 배출한다.", "Other PET bottles are disposed of in the plastic collection box.")]
_A_FOOD = [("먼저 음식물을 꼭 짜서 물기를 없앤다.", "First wring the food well to remove the moisture."), ("그런 후에 음식물 쓰레기 종량제 봉투에 모아서 배출한다.", "Then collect it in the food waste meter-rate bag and dispose of it."), ("달걀 껍질이나 생선뼈처럼 딱딱한 것은 일반 쓰레기 종량제 봉투에 배출한다.", "Hard things such as eggshells or fish bones are disposed of in the general waste meter-rate bag.")]
_A_WORDS = ["겉", "껍질", "꽁초", "내용물", "딱딱하다", "또는", "뚜껑", "말리다", "무색", "묶다", "물기", "배출", "봉투", "분리", "비우다", "속", "수거", "썩다", "압축", "없애다", "우유", "유리", "이물질", "제거", "종량제", "짜다", "팩", "페트병", "헹구다"]
_PET = [("환경부는 전국의 네 개 도시에서 두 달간, 올해 말부터 시작되는 무색 투명 페트병 분리수거를 적극적으로 홍보할 예정이다.", "The Ministry of Environment plans to actively promote, for two months in four cities nationwide, the separate collection of colorless (transparent) PET bottles that starts at the end of this year."), ("생수나 음료수를 담는 무색 페트병은 의류나 가방, 신발, 블라인드 등을 만들 수 있어서 재활용 가치가 크다.", "Colorless PET bottles that hold spring water or beverages can be made into clothing, bags, shoes, blinds, etc., so their recycling value is high."), ("서울특별시는 무색 페트병을 가져오면 현금처럼 쓸 수 있는 포인트를 지급하는데, 작은 페트병 한 개당 백 점, 큰 것은 오백 점을 준다.", "The Seoul Metropolitan City gives points that can be used like cash if you bring colorless PET bottles: 100 points per small PET bottle and 500 points for a big one."), ("인천광역시에서는 포인트 대신에 종량제 봉투나 이마트 상품권으로 교환해 줄 예정이다.", "Incheon Metropolitan City plans to exchange them for standard garbage bags or Emart gift certificates instead of points."), ("광주광역시에서는 청소년을 대상으로 분리배출 가상체험 교육관을 운영할 예정이고, 부산광역시에서는 어린이들을 위해 분리배출의 중요성과 방법에 대한 노래를 만들어 시청 웹사이트와 유튜브에 올릴 예정이다.", "Gwangju Metropolitan City plans to operate a virtual-experience education center for separate disposal aimed at teenagers, and Busan Metropolitan City plans to make a song about the importance and method of separate disposal for children and post it on the city hall website and YouTube.")]
L3 = lesson(
    "Ch 40 · Topic A: Waste separation and disposal (쓰레기 분리수거)",
    "쓰레기 분리수거 · 종이 · 유리병 · 캔과 페트병 · 음식물 쓰레기 · 종량제 봉투 · 무색 페트병",
    requires=[],
    cards=[
        card("Topic A: Waste separation and disposal (쓰레기 분리수거)",
             "The following text is a public announcement about the “separation and disposal system” in Korea. The book’s heading is 쓰레기를 줄이고, 재활용을 ___ 늘려 환경을 보호합시다! (one word is blank in the printed text) and “분리 수거 지역: 전국” (the separation area: the whole country). The announcement has four boxes (종이, 유리병, 캔과 페트병, 음식물 쓰레기); the book’s brief notes (some ending in –함, –ㄹ 것) are written below as sentences, with the same meaning; the English is mine. (The book’s footnote: 함 (函) means a box. It is used with another noun as in 우편함 [mailbox], 보관함 [storage box], and 수거함 [collection box].)",
             examples=passage([(_A_SEC[0][1], _A_SEC[0][2])])),
        card("1. 종이 (paper)", "", examples=passage(_A_PAPER)),
        card("2. 유리병 (glass bottles)", "", examples=passage(_A_GLASS)),
        card("3. 캔과 페트병 (cans and PET bottles)", "", examples=passage(_A_CAN)),
        card("4. 음식물 쓰레기 (food waste)", "", examples=passage(_A_FOOD)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists 계란/달걀 (an egg) and 재활용 (recycling).",
             tables=[ktable(_rows(_A_WORDS)), table(["Word", "Meaning"], [["계란 / 달걀", "(鷄卵) an egg"], ["재활용", "(再活用) recycling; reuse"]], say=[0])]),
        card("한국에서는: 쓰레기 분리 수거와 종량제 봉투",
             "In 1995, Korea initiated 쓰레기 분리배출 (waste separation and disposal) for trash and food waste reduction and to help preserve the environment. Koreans sort recyclables into categories such as paper, plastic, and clothes, and must dispose of them properly. For general (unrecyclable) trash and food waste, they must use government-approved plastic bags known as 종량제 봉투 (standard plastic garbage bag; “meter-rate system envelope”). These bags come in different sizes and can be purchased at a market or grocery store. These days newer homes are equipped with a garbage disposal. For the homes without a garbage disposal, people must wring any excess fluid from food waste and then place it in an approved bag for disposal."),
        card("Follow-up 2 (Reading): a news report about four cities’ recycling programs",
             "The following news report is about the recycling programs to be run by four major cities (the book glosses 생수: spring water; 가치: value; 청소년: teenagers). The report is the book’s with the numbers spelled out; the book’s English “Ministry of Environment” and “AR-VR” are dropped; the English is mine.",
             examples=passage(_PET)),
        card("The answers (mine)", "The book asks (1) why the Ministry of Environment is actively promoting the recycling of clear PET bottles and (2) to fill in the program of each of four cities. My answers:",
             tables=[table(["Question", "Answer (mine)"], [["1. Why promote clear PET bottles?", "They can be made into clothing, bags, shoes, blinds, etc., so their recycling value is high"], ["Seoul", "Points usable like cash for bringing in clear PET bottles: 100 points for a small one, 500 for a big one"], ["Incheon", "Exchange for standard garbage bags or Emart gift certificates instead of points"], ["Kwangju", "A virtual-experience education center on separate disposal for teenagers"], ["Busan", "A song about the importance and method of separate disposal for children, posted on the city hall website and YouTube"]])]),
        card("Activities left out", "The presentation steps of Topic A (SMART Board and listening) and Follow-up 1 (listening to four conversations about discarded items and the separation method, checking paper, bottles, cans or food waste) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_SEC and [(_A_SEC[0][1], _A_SEC[0][2])] + _A_PAPER + _A_GLASS + _A_CAN + _A_FOOD + _PET, k=3)
        + [M("How should paper cartons be handled?", "Empty, rinse with water, dry, compress and dispose of", ["Burn them", "Throw them in food waste", "Cut them up"], "내용물을 다 비우고 헹굼, 말린 후 압축."), M("What should you remove first from glass bottles?", "The plastic or aluminum lid or the label", ["The glass", "The color", "The water"], "뚜껑이나 라벨을 제거."), M("What should not be put in a bottle?", "Foreign objects such as cigarette butts", ["Water", "Labels", "Lids"], "담배꽁초 등 이물질."), M("Where do colorless PET bottles for water or beverages go?", "The special collection box", ["The plastic collection box", "The general waste bag", "The glass box"], "전용 수거함."), M("What should you do first with food waste?", "Wring it out to remove moisture", ["Burn it", "Bury it", "Bag it with glass"], "꼭 짜서 물기를 없앤다."), M("Where do eggshells and fish bones go?", "The general waste meter-rate bag", ["The food waste bag", "The plastic box", "The paper box"], "일반 쓰레기 종량제 봉투."), M("What is a 종량제 봉투?", "A government-approved meter-rate garbage bag", ["A paper envelope", "A glass bottle", "A recycling box"], "The book’s note."), M("What does Seoul give for a big PET bottle?", "500 points", ["100 points", "50 points", "Nothing"], "오백 점."),
           F("먼저 음식물을 꼭 짜서 ___를 없앤다. (moisture)", "물기", ["내용물", "껍질"], "물기."), F("내용물을 다 ___ 물로 깨끗이 헹군다. (empty)", "비우고", ["묶고", "말리고"], "비우다."), F("우유 ___과 음료수 팩은 깨끗이 헹군다. (carton)", "팩", ["뚜껑", "봉투"], "팩."), F("겉에 라벨이 있으면 ___한다. (remove)", "제거", ["압축", "수거"], "제거."), F("달걀 ___이나 생선뼈는 일반 쓰레기다. (shell)", "껍질", ["내용물", "뚜껑"], "껍질."),
           read_q("쓰레기 분리수거"), read_q("내용물을 다 비우고 물로 깨끗이 헹굽니다"), read_q("음식물을 꼭 짜서 물기를 없앱니다"), read_q("무색 페트병은 전용 수거함에 배출합니다"), read_q("종량제 봉투를 사용해야 합니다")]
    ),
)

# ================================================================== L4 Activities A: food waste + reader opinion
_FWS = [("음식 재료를 필요한 만큼만 구입할 것.", "Restaurant", "Buy only as many food ingredients as needed."), ("음식을 먹을 만큼만 주문할 것.", "Customer", "Order only as much food as you will eat."), ("제공하는 음식의 양을 줄일 것.", "Restaurant", "Reduce the amount of food served."), ("음식을 남기지 말고 다 먹을 것.", "Customer", "Don’t leave food; eat it all."), ("작은 반찬 그릇을 사용할 것.", "Restaurant", "Use small side-dish bowls."), ("음식물 쓰레기에서 물기를 없앨 것.", "Restaurant and customer", "Remove the moisture from food waste."), ("남은 음식은 싸서 집에 가지고 갈 것.", "Customer", "Wrap leftover food and take it home."), ("반찬의 종류를 줄일 것.", "Restaurant", "Reduce the kinds of side dishes.")]
_READ = [("우리 아파트에서 쓰레기를 버릴 때 가끔 재활용 쓰레기통 속을 보게 된다.", "When throwing out trash at our apartment, I sometimes get to look inside the recycling bin."), ("예전보다 플라스틱 수거함에 쓰레기가 훨씬 많아졌다.", "There is much more trash in the plastic collection box than before."), ("배달음식 주문이 많아지면서 배달음식을 담았던 용기들도 함께 늘어났기 때문이다.", "This is because as delivery food orders have increased, the containers that held delivery food have also increased."), ("그런데 용기의 내용물을 비우지 않은 채로 배출하는 사람들이 꽤 많다.", "But quite a lot of people dispose of the containers without emptying the contents."), ("음식 때문에 밤에는 너구리나 길고양이들이 오기도 하고 여름에는 음식물이 금방 썩어서 냄새가 많이 난다고 들었다.", "I heard that because of the food, raccoon dogs or stray cats come at night, and that in summer the food rots quickly and smells a lot."), ("재활용 쓰레기 회사의 직원들은 빠른 시간 내에 재활용 쓰레기를 분리해 내야 한다.", "The employees of recycling companies have to separate recyclables within a short time."), ("그렇기 때문에 음식물이 들어 있는 플라스틱은 일반 쓰레기로 처리할 수밖에 없다.", "That is why plastic with food in it has no choice but to be processed as general trash."), ("용기를 씻을 시간이 없기 때문이다.", "It is because there is no time to wash the containers."), ("우리가 내용물을 깨끗이 비우고 씻어서 버리면 재활용될 수 있는 것을, 음식물 때문에 재활용이 안 되니까 얼마나 낭비인가?", "What a waste it is that something that could be recycled if we empty and wash the contents clean is not recycled because of the food!"), ("배달음식 용기를 깨끗이 씻는 데 시간이 그렇게 오래 걸리지 않는다.", "It does not take that long to wash a delivery food container clean."), ("피자가 배달된 상자는 기름이나 음식이 묻은 곳을 잘 닦은 후 재활용 종이 수거함에 버린다.", "For a box in which a pizza was delivered, wipe well the places with oil or food and then throw it in the recycling paper collection box."), ("우리가 신경을 조금만 더 쓰면 재활용이 안 되는 일반 쓰레기를 줄일 수 있다.", "If we pay just a little more attention, we can reduce the general trash that cannot be recycled."), ("조금 더 환경문제에 관심을 갖자.", "Let’s take a little more interest in environmental problems.")]
L4 = lesson(
    "Ch 40 · Activities A: reducing food waste and a reader’s opinion",
    "음식물 쓰레기 줄이기 · 식당과 손님 · 배달음식 용기 · 재활용 쓰레기 · 낭비",
    requires=[],
    cards=[
        card("Activity 3 (Reading and listening): reducing food waste",
             "The following sentences describe what can be done to reduce food waste; the book asks you to read them and check whether each applies to a restaurant or a customer (one is done for you: 제공하는 음식의 양을 줄일 것 for the restaurant). The sentences are the book’s; the classification is mine; the English is mine.",
             tables=[table(["Suggestion", "Restaurant / Customer (mine)", "English (mine)"], [[a, b, c] for a, b, c in _FWS], say=[0])]),
        card("Activity 3 b: the Daejeon restaurant report", "The book asks you to listen to a report about a restaurant in Daejeon and (1) write three points about the event the restaurant holds and (2) say what the restaurant owner is considering to reduce food waste further. The book glosses 덜어 먹다: to dish up one’s own portion (and eat); ~대 (臺): a stand. This is an audio activity and is left out."),
        card("Activity 4 (Reading): a reader’s opinion",
             "The following article is a reader’s opinion published on a newspaper website (the book glosses 용기: a container; 너구리: a raccoon dog; 낭비: waste). The article is the book’s; the English is mine.",
             examples=passage(_READ)),
        card("The table filled in (mine)", "The book’s table has the columns the problem at the author’s apartment building, limitations of recycling companies and the author’s suggestions. My answers:",
             tables=[table(["Item", "Answer (mine)"], [["The problem at the author’s apartment building", "Much more trash in the plastic collection box; many people dispose of delivery food containers without emptying them, which attracts raccoon dogs and stray cats at night and smells in summer"], ["Limitations of recycling companies", "Employees must separate recyclables in a short time, so plastic with food in it has to be treated as general trash because there is no time to wash it"], ["The author’s suggestions", "Empty and wash containers before disposal; wipe off oil and food from pizza boxes before putting them in the paper collection box; pay a little more attention and take more interest in environmental problems"]])]),
        card("Activities left out", "Activity 1 (SMART Board), Activity 2 (listening to a radio program about the recycling efforts of Yongin and Jinhae, and the table of what materials are recycled, what is done with them and how the money is used) and Activity 5 (pairs think of ways a local restaurant can reduce food waste, choose three ideas, post and present them) are audio and group activities."),
    ],
    exercises=uniq(
        _tr(_READ + [(a, c) for a, b, c in _FWS], k=3)
        + [M("Who should reduce the amount of food served?", "The restaurant", ["The customer", "The government", "The delivery driver"], "My answer."), M("Who should order only as much as they will eat?", "The customer", ["The restaurant", "The owner", "The driver"], "My answer."), M("Who should take leftovers home?", "The customer", ["The restaurant", "The owner", "The cook"], "My answer."), M("What has increased in the plastic collection box?", "Delivery food containers", ["Glass bottles", "Newspapers", "Cans"], "배달음식을 담았던 용기들."), M("Why can plastic with food in it not be recycled?", "Recycling workers have no time to wash it", ["It is illegal", "It is too heavy", "It has no value"], "용기를 씻을 시간이 없기 때문이다."), M("How should a pizza box be disposed of?", "Wipe off oil and food, then put it in the paper collection box", ["Throw it away as is", "Burn it", "Put it in food waste"], "기름이나 음식이 묻은 곳을 잘 닦은 후."), M("What does the author ask of readers?", "To take a little more interest in environmental problems", ["To stop ordering food", "To move apartments", "To pay more tax"], "조금 더 환경문제에 관심을 갖자."),
           F("음식을 먹을 ___ 주문할 것. (as much as)", "만큼만", ["때문에만", "동안만"], "만큼."), F("용기의 내용물을 비우지 않은 ___로 배출하는 사람들이 꽤 많다. (state)", "채", ["것", "때"], "-(으)ㄴ 채로."), F("재활용이 안 되니까 얼마나 ___인가? (waste)", "낭비", ["관심", "협력"], "낭비."), F("우리가 신경을 조금만 더 쓰면 일반 쓰레기를 ___ 수 있다. (reduce)", "줄일", ["늘릴", "버릴"], "줄이다."), F("남은 음식은 싸서 집에 ___ 갈 것. (take)", "가지고", ["가져서", "가고"], "가지고 가다."),
           read_q("음식물 쓰레기를 줄입시다"), read_q("음식을 먹을 만큼만 주문할 것"), read_q("용기의 내용물을 깨끗이 비우고 씻어서 버립니다"), read_q("재활용이 안 되니까 얼마나 낭비입니까"), read_q("조금 더 환경문제에 관심을 갖자")]
    ),
)

# ================================================================== L5 Topic B
_B_TXT = [
    ("오늘은 유엔이 지정한 환경의 날입니다.", "Today is the Environment Day designated by the United Nations."),
    ("기자의 보도입니다.", "This is the reporter’s report."),
    ("남극과 북극의 빙하가 녹아 해수면이 올라가고 있습니다.", "The glaciers of the Antarctic and the Arctic are melting and the sea level is rising."),
    ("해수면이 앞으로 백 년간 오십 센티미터에서 일 미터 정도 높아질 것으로 예측되고 있습니다.", "The sea level is predicted to become about 50 cm to 1 m higher over the next 100 years."),
    ("이렇게 되면 생태계가 파괴되고 농작물의 수확량이 감소하는 등 지구 전역에 피해가 예상됩니다.", "If this happens, damage is expected across the whole Earth, such as the destruction of ecosystems and a decrease in crop yields."),
    ("빙하가 녹는 가장 큰 이유는 지구의 평균기온이 올라가는 지구 온난화 현상 때문입니다.", "The biggest reason the glaciers are melting is the phenomenon of global warming, in which the Earth’s average temperature rises."),
    ("지구 온도는 지난 백 년간 영 점 오 도에서 일 도 정도 상승한 것으로 관측되고 있습니다.", "The Earth’s temperature has been observed to have risen by about 0.5 to 1 degree over the last 100 years."),
]
_B_WORDS = ["감소", "관측", "기후", "남극", "녹다", "농작물", "대책", "보도", "북극", "빙하", "상승", "생태계", "수확량", "예측", "온난화", "온도", "온실가스", "이산화탄소", "전역", "제한", "주제", "지구", "파괴", "해수면", "해안", "협력"]
_REP = [("김재용 씨는 농장에서 채소와 과일을 기르고 있다. 그런데 올해 폭우 때문에 수확량이 아주 많이 줄었다.", "e", "Mr. Kim Jaeyong grows vegetables and fruit on a farm. But this year, because of heavy rain, the yield has decreased a great deal.", "a decrease in crop yields"), ("남극의 얼음이 자꾸 녹고 있다. 바다표범과 펭귄이 살 곳이 없어지고 있다.", "b", "The ice in the Antarctic keeps melting. Seals and penguins are losing places to live.", "melting glaciers"), ("브라질 남부 지방의 온도가 매년 여름 상승하고 있다. 특히 지난 이틀 동안 이곳에서는 오십 도를 넘는 폭염으로 열일곱 명이 사망했다.", "a", "The temperature in the southern region of Brazil is rising every summer. In particular, over the last two days 17 people died here in a heat wave exceeding 50 degrees.", "rising temperatures"), ("제주 서귀포시의 대표적 관광지인 용머리 해안이 물에 잠겼다. 서귀포시는 용머리 해안이 하루 여덟 시간 이상 바닷물에 잠기고 있다고 했다.", "c", "Yongmeori Coast, a representative tourist site of Seogwipo, Jeju, has been submerged. Seogwipo said Yongmeori Coast is under seawater for more than eight hours a day.", "rising sea levels"), ("아마존 지역에 이상 건조 현상으로 나무들이 말라 죽어 가고 있으며, 산불이 자주 발생해 장기간 계속되고 있다.", "d", "In the Amazon region, trees are drying up and dying because of the phenomenon of abnormal aridity, and wildfires frequently occur and continue for a long time.", "abnormal aridity")]
L5 = lesson(
    "Ch 40 · Topic B: Global warming (지구 온난화)",
    "지구 온난화 · 빙하가 녹다 · 해수면 상승 · 수확량 감소 · 환경의 날 · ~ 등 · 온난화의 영향",
    requires=[],
    cards=[
        card("Topic B: Global warming (지구 온난화)",
             "The following TV news report is about global warming. (The English is mine; the book gives none; the numbers are spelled out in Hangul; the reporter’s name is left out; the printed text has a blank after 지구, which I read as 지구 전역에.)",
             examples=passage(_B_TXT)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists ~ 등 and ~배.",
             tables=[ktable(_rows(_B_WORDS)), table(["Word", "Meaning"], [["~ 등", "(等) and so on; etc."], ["~배", "times"]], say=[0])]),
        card("한국어에는: ~ 등",
             "In English, phrases like and so on, and so forth, or etc. indicate that a list continues in a similar manner. Likewise, in Korean, we use ~ 등 to indicate that a list of nouns continues in a similar manner. For instance, 그 한국식품점에는 사과, 배 등 한국과일이 많습니다 (There are many Korean fruits in the Korean grocery store: apples, pears, etc.). However, when indicating a list of verbs, 등 is added to attributive verbal phrases; for example, 지난 주말에 영화도 보고 쇼핑하는 등 여러 가지 일을 했다 (Last weekend, I did various things, like watching a movie, shopping, etc.)."),
        card("Follow-up 1 (Reading): the repercussions of global warming",
             "The following statements are about the repercussions of global warming. The book asks you to read each statement and match it with the appropriate English phrase in the box: a. rising temperatures; b. melting glaciers; c. rising sea levels; d. abnormal aridity; e. a decrease in crop yields. The statements are the book’s with the numbers spelled out; the matches and the English are mine.",
             examples=passage([(a.replace(". ", ". ", 1), c) for a, b, c, d in _REP]),
             tables=[table(["No.", "Phrase (mine)"], [[str(i + 1), b + ". " + d] for i, (a, b, c, d) in enumerate(_REP)])]),
        card("Activities left out", "The presentation steps of Topic B (brainstorming causes and effects of global warming in a table, SMART Board activities and the video) and Follow-up 2 (listening to a radio news clip about a country suffering from global warming and noting country, type of disaster, casualties and outlook) are audio, video and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT + [(a, c) for a, b, c, d in _REP], k=3)
        + [M("What day is it in the report?", "Environment Day designated by the UN", ["Earth Day", "Arbor Day", "New Year"], "유엔이 지정한 환경의 날."), M("What is the cause of melting glaciers?", "Global warming", ["Volcanoes", "Typhoons", "Pollution only"], "지구 온난화 현상."), M("How much is the sea level predicted to rise over 100 years?", "About 50 cm to 1 m", ["About 10 m", "About 1 cm", "About 5 m"], "오십 센티미터에서 일 미터."), M("How much has the Earth’s temperature risen over 100 years?", "About 0.5 to 1 degree", ["About 10 degrees", "About 5 degrees", "None"], "영 점 오 도에서 일 도."), M("What does ~ 등 indicate?", "That a list continues (etc.)", ["A time", "A place", "A question"], "The book’s note."), M("Which statement matches “rising sea levels”?", "Yongmeori Coast submerged for hours each day", ["Crop yields falling", "Penguins losing ice", "Amazon wildfires"], "My answer."), M("Which statement matches “abnormal aridity”?", "Amazon trees drying and dying", ["Heat in Brazil", "Seals losing ice", "Farm yields"], "My answer."), M("Which statement matches “rising temperatures”?", "A heat wave above 50 degrees in southern Brazil", ["Melting Antarctic ice", "Falling crop yield", "A flooded coast"], "My answer."),
           F("남극과 북극의 ___가 녹아 해수면이 올라가고 있습니다. (glaciers)", "빙하", ["해안", "기후"], "빙하."), F("지구 온난화 ___ 때문입니다. (phenomenon)", "현상", ["대책", "협력"], "현상."), F("농작물의 ___이 감소하고 있습니다. (yield)", "수확량", ["수거량", "강수량"], "수확량."), F("지구 ___에 피해가 예상됩니다. (the whole area)", "전역", ["해안", "주제"], "전역."), F("이산화탄소는 대표적인 ___가스다. (greenhouse)", "온실", ["냉방", "난방"], "온실가스."),
           read_q("지구 온난화"), read_q("남극과 북극의 빙하가 녹고 있습니다"), read_q("해수면이 올라가고 있습니다"), read_q("농작물의 수확량이 감소하고 있습니다"), read_q("지구 전역에 피해가 예상됩니다")]
    ),
)

# ================================================================== L6 Grammar A: abbreviated endings
_ABA = [("강남 어학원 영어 강사 모집", "English instructor wanted, Gangnam language institute"), ("경력자 우대함", "Experienced applicants preferred"), ("뉴욕에 본사가 있음", "Headquarters in New York"), ("관심 있는 분은 전화 연락 바람", "Those interested, please call"), ("생활 지원비와 숙소 제공함", "Living support money and housing provided")]
_ABB = [("수강 신청 안내", "Course registration notice"), ("사 학년이 아닌 경우 십 학점 이상 들을 것", "If you are not a fourth-year student, take 10 credits or more"), ("수강 신청 후 홈페이지에서 신청 내용을 다시 확인할 것", "After registering for courses, check the registration details again on the homepage"), ("기타 질문 시 소속 학과 사무실로 갈 것", "For other questions, go to your department office")]
_ABE = [("오늘 두 시에 운동을 했다.", "오늘 두 시 운동했음", "Worked out today, 2:00"), ("민수는 지금 영화보고 있다.", "민수 지금 영화보고 있음", "Minsu, watching a movie now"), ("내일 바닷가에 간다.", "내일 바닷가에 감", "Going to the beach tomorrow"), ("여덟 시까지 숙제를 내세요.", "여덟 시까지 숙제 낼 것", "Submit homework by 8:00"), ("점심 후에 약을 드세요.", "점심 후에 약 먹을 것", "Take the medicine after lunch")]
_ABP = [("지난 토요일에 지리산으로 등산갔다.", "지난 토요일 지리산으로 등산 갔음", "Went hiking on Jirisan last Saturday"), ("캔 속에 있는 내용물을 꼭 비우셔야 합니다.", "캔 속 내용물 꼭 비울 것", "Be sure to empty the contents inside the can"), ("진주 중학교는 국어 교사를 모집합니다.", "진주 중학교 국어 교사 모집", "Jinju Middle School is recruiting a Korean teacher"), ("오늘 백화점에 가서 엄마 선물을 샀다.", "오늘 백화점 가서 엄마 선물 샀음", "Went to the department store today and bought a present for Mom"), ("아침 여덟 시까지 운동장으로 모이세요.", "아침 여덟 시까지 운동장으로 모일 것", "Gather at the playground by 8 a.m."), ("오후 세 시에 회의가 있습니다.", "오후 세 시 회의 있음", "There is a meeting at 3 p.m."), ("올해는 책을 더 많이 읽어야 한다.", "올해는 책 더 많이 읽을 것", "Must read more books this year"), ("오늘은 수업이 없습니다.", "오늘은 수업 없음", "No class today")]
_BLOG = [("이물질, 비닐, 병뚜껑, 젓가락 등은 음식물에서 철저히 분리, 배출할 것", "Separate foreign objects (vinyl, bottle caps, chopsticks, etc.) thoroughly from food and dispose of them"), ("배추 등은 작게 썰어 크기를 줄일 것", "Cut cabbage, etc. small to reduce the size"), ("김치는 물에 헹군 후 물기를 모두 없앨 것", "Rinse kimchi with water and then remove all the moisture"), ("음식물 쓰레기는 종량제 봉투에 넣을 것", "Put food waste in a meter-rate bag")]
L6 = lesson(
    "Ch 40 · Grammar A: abbreviated verb endings used in writing, –(으)ㅁ and –(으)ㄹ 것",
    "-(으)ㅁ · -(으)ㄹ 것 · 우대함 · 있음 · 제공함 · 들을 것 · 확인할 것 · 게시판과 메모",
    requires=[],
    cards=[
        card("Abbreviated verbs",
             "Bulletin boards, newspaper headlines, titles and subtitles, warnings, notes, memos in a planner, etc., rarely use complete sentences. When they contain sentences, the verbs are often abbreviated. The book shows two texts, Text A (a newspaper ad) and Text B (an online college bulletin board), to see how the verbs are written (the numbers are spelled out; the English is mine).",
             examples=passage(_ABA) + passage(_ABB)),
        card("Two endings",
             "Note that the verbs are abbreviated into either of the following two endings: –(으)ㅁ (우대함, 있음, 바람, 제공함 in Text A) and –(으)ㄹ 것 (들을 것, 확인할 것, 갈 것 in Text B)."),
        card("–(으)ㅁ",
             "–(으)ㅁ is used to abbreviate a verb when a sentence contains factual information (e.g., a statement, a report, or an observation). Note that –(으)ㅁ can be omitted when the verb is made up of a noun and 하다 (as in 경력자 우대(함), 생활 지원비와 숙소 제공(함)). The book’s examples (the numbers are spelled out; the English is the book’s):"),
        card("–(으)ㄹ 것",
             "–(으)ㄹ 것 is used to abbreviate a verb when a sentence contains a task (e.g., a request, a command, or an order). Note that in the sentences, non-key words (like noun markers or an honorific infix) can be omitted.",
             tables=[table(["Full sentence", "Abbreviated", "English"], [[a, b, c] for a, b, c in _ABE], say=[0, 1])]),
        card("Follow-up 1 (Reading and writing): abbreviate the verbs",
             "Read each sentence and abbreviate the verb, using either –(으)ㅁ or –(으)ㄹ 것. The sentences are the book’s (the numbers are spelled out); the answers and the English are mine.",
             tables=[table(["Sentence", "Abbreviated (mine)", "English (mine)"], [[a, b, c] for a, b, c in _ABP], say=[0, 1])]),
        card("Follow-up 2 (Reading): a blog on food waste disposal",
             "The following information on food waste separation and disposal was posted by a Korean woman in her blog. The book asks you to circle all abbreviated verb endings and omissions of 하다, and to write down the suggested methods of garbage disposal in English. The post is the book’s (the brackets are set off by commas); the English (the methods) is mine.",
             tables=[table(["Blog line", "Method of garbage disposal (mine)"], [[a, b] for a, b in _BLOG], say=[0])]),
        card("The endings in the blog (mine)", "The abbreviated endings in the four lines are 분리, 배출할 것 (the verb 배출하다 abbreviated with –(으)ㄹ 것), 줄일 것, 없앨 것 and 넣을 것; all four lines are tasks, so they use –(으)ㄹ 것."),
    ],
    exercises=uniq(
        _tr([(a, c) for a, b, c in _ABE] + [(b, c) for a, b, c in _ABE] + [(a, c) for a, b, c in _ABP] + _BLOG + _ABA + _ABB, k=3)
        + [M("When is –(으)ㅁ used?", "For factual information (statement, report, observation)", ["For requests and orders", "For questions", "For wishes"], "The book’s note."), M("When is –(으)ㄹ 것 used?", "For a task (request, command, order)", ["For facts", "For questions", "For past events"], "The book’s note."), M("Which ending fits “지난 토요일에 등산을 갔다”?", "–(으)ㅁ (갔음)", ["–(으)ㄹ 것 (갈 것)", "–고 있다", "–(으)면"], "A past fact."), M("Which ending fits “8시까지 숙제를 내세요”?", "–(으)ㄹ 것 (낼 것)", ["–(으)ㅁ (냈음)", "–고 있다", "–(으)면"], "A command."), M("What can be omitted when a verb is a noun + 하다?", "–(으)ㅁ (and 하다)", ["The noun", "The subject", "Nothing"], "The book’s note."), M("What does 오늘은 수업 없음 mean?", "No class today", ["There is class today", "Class is canceled tomorrow", "Class ends early"], "My answer."),
           F("경력자 우대___ (ending)", "함", ["할 것", "하고"], "우대함."), F("뉴욕에 본사가 있___ (ending)", "음", ["을 것", "고"], "있음."), F("신청 내용을 다시 확인___ (ending)", "할 것", ["함", "했음"], "확인할 것."), F("오늘 백화점 가서 엄마 선물 샀___ (ending)", "음", ["을 것", "고"], "샀음."), F("음식물 쓰레기는 종량제 봉투에 넣___ (ending)", "을 것", ["음", "고"], "넣을 것."),
           read_q("경력자 우대함"), read_q("뉴욕에 본사가 있음"), read_q("신청 내용을 다시 확인할 것"), read_q("오늘은 수업 없음"), read_q("음식물 쓰레기는 종량제 봉투에 넣을 것")]
    ),
)

# ================================================================== L7 Grammar B: news report expressions
_NR1 = [("김 일병이 지금 비가 온다고 해요.", "PFC Kim says that it is raining now."), ("팀장님이 김 선생님이 아프시다고 합니다.", "The team leader says that Ms. Kim is ill.")]
_NR2 = [("작년에 기름 값이 십육 퍼센트 오른 것으로 나타났습니다.", "It was revealed / It was shown that oil prices increased by 16% last year."), ("작년에 기름 값이 십육 퍼센트 오른 걸로 나타났어요.", "It was revealed / It was shown that oil prices increased by 16% last year. (colloquial 걸로)")]
_NR3 = [("한 배우가 삼 년간 협박을 당한 것으로 밝혀졌다.", "It was revealed that an actor had been blackmailed for 3 years."), ("전문가들은 한반도의 기온이 더 올라갈 것으로 예측했다.", "Experts predicted that the temperatures on the Korean Peninsula would go up."), ("삼성은 새 휴대폰이 많이 팔릴 것으로 전망했다.", "Samsung expected that new cell phones would sell well / would be popular."), ("중학생들의 이십 퍼센트가 담배를 피우는 것으로 조사됐다.", "The survey showed that 20% of middle school students were smokers.")]
_NRW = [("실종자는 모두 사망했습니다.", "실종자는 모두 사망한 것으로 확인됐습니다.", "It was confirmed that all the missing persons died."), ("일주일 동안 태풍이 계속되겠습니다.", "일주일 동안 태풍이 계속될 것으로 예보됐습니다.", "It was forecast that the typhoon would continue for a week."), ("산사태로 백여 명이 숨졌습니다.", "산사태로 백여 명이 숨진 것으로 알려졌습니다.", "It was reported that more than 100 people died in the landslide."), ("내년 겨울은 올해보다 더 춥겠습니다.", "내년 겨울은 올해보다 더 추울 것으로 전망됩니다.", "It is forecast that next winter will be colder than this year."), ("미혼 여성의 삼십 퍼센트가 결혼할 생각이 없습니다.", "미혼 여성의 삼십 퍼센트가 결혼할 생각이 없는 것으로 나타났습니다.", "It was revealed that 30% of unmarried women have no intention of marrying."), ("이 씨는 과속운전을 하지 않았습니다.", "이 씨는 과속운전을 하지 않은 것으로 밝혀졌습니다.", "It was revealed that Mr. Lee did not drive over the speed limit."), ("장수마을 사람들이 주로 채식을 합니다.", "장수마을 사람들이 주로 채식을 하는 것으로 알려졌습니다.", "It is known that people in the longevity village mainly eat vegetarian food."), ("한국 선수들이 금메달을 많이 딸 것입니다.", "한국 선수들이 금메달을 많이 딸 것으로 예상됩니다.", "It is expected that Korean athletes will win many gold medals.")]
_NRM = [("디엘아이 학생들은 외식을 얼마나 자주 할까요?", "How often do DLI students eat out?"), ("지난주에 기숙사에 사는 학생 중 이십 퍼센트가 외식을 한 것으로 나타났습니다.", "Last week 20% of the students living in the dormitory were found to have eaten out.")]
L7 = lesson(
    "Ch 40 · Grammar B: expressions frequently used in news reports, an attributive form + 것으로",
    "-(으)ㄴ 것으로 나타났다 · -(으)ㄹ 것으로 예측했다 · 밝혀졌다 · 알려졌다 · 조사됐다 · 보도됐다 · 전망했다 · 걸로",
    requires=[],
    cards=[
        card("Recall –다고 하다",
             "Recall that the grammar feature –다고 하다, which you learned about in Chapter 23, is used when reporting or quoting a statement indirectly, as in the following (the English is the book’s). However, this grammar feature is mainly for conversational language, rather than formal news reports or research papers in which reporting and quoting has to be specific.",
             examples=passage(_NR1)),
        card("News report verbs",
             "In news reports, for example, the following verbs are commonly used: 나타나다 (to be revealed; to be shown); 보다/보이다, 조사하다/조사되다, 알려지다, 밝히다/밝혀지다 (to clarify; to be clarified); 전망하다 (to forecast; to expect), etc. When these verbs are used for reporting, the reported information frequently ends in an attributive form + 것으로. For example (the English is the book’s):",
             examples=passage(_NR2[:1])),
        card("Note", "Note that the attributive form 오른 + 것으로 is immediately followed by 나타나다. In colloquial language, 것으로 is often contracted to 걸로/거로. For example (the English is the book’s):", examples=passage(_NR2[1:])),
        card("Expressions frequently used in news reports", "Attributive form of a verb + 것으로 + 나타나다/보이다/조사되다/알려지다, etc. More examples (the numbers are spelled out; the English is the book’s):", examples=passage(_NR3)),
        card("Follow-up 3 (Writing): reporter’s statements",
             "Imagine you are a reporter for a radio news show. Rewrite each statement as if you were going to use it in your news report. Choose an appropriate verb from the box 나타나다, 밝혀지다, 보이다, 보도하다/보도되다, 알려지다, 예보하다/예보되다, 예상하다/예상되다, 예측하다/예측되다, 전망되다, 확인되다 (the verbs may be used more than once). The book’s model is 오만 명의 이재민이 발생했습니다 → 오만 명의 이재민이 발생한 것으로 나타났습니다/밝혀졌습니다/보도됐습니다/알려졌습니다. The statements are the book’s (the numbers are spelled out); the rewrites and the English are mine.",
             tables=[table(["Statement", "News report (mine)", "English (mine)"], [[a, b, c] for a, b, c in _NRW], say=[0, 1])]),
        card("Follow-up 5 (Speaking and writing): a piece of news about DLI students",
             "Using at least four sentences, write a piece of recent news about DLI students (e.g., what they did last week and what they seem to be going to do this week) and use an attributive form + 것으로 + verb at least twice; present it to your class as if you were a reporter. The book’s model (DLI is read 디엘아이; the number is spelled out; the English is mine):",
             examples=passage(_NRM)),
        card("Activities left out", "Follow-up 4 (listening to three news reports about natural hazards and transcribing the segments with an attributive form + 것으로 + verb) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_NR1 + _NR2 + _NR3 + [(b, c) for a, b, c in _NRW] + _NRM, k=3)
        + [M("What does 것으로 나타났다 mean in a news report?", "It was revealed / shown that …", ["I want to show …", "Please show …", "Let’s show …"], "The book’s note."), M("Where is –다고 하다 mainly used?", "In conversation", ["In formal news reports", "In research papers", "In headlines"], "The book’s note."), M("What does 걸로 stand for?", "것으로", ["것은", "것이", "것도"], "The book’s note."), M("Which verb means “to forecast; to expect”?", "전망하다", ["조사하다", "밝히다", "알려지다"], "The book’s note."), M("What does 조사됐다 mean in a news report?", "It was surveyed / found", ["It was cleaned", "It was sold", "It was lost"], "조사되다."), M("What does 한 배우가 삼 년간 협박을 당한 것으로 밝혀졌다 mean?", "It was revealed that an actor had been blackmailed for 3 years", ["An actor blackmailed someone", "An actor will be blackmailed", "An actor retired"], "The book’s example."),
           F("작년에 기름 값이 오른 ___ 나타났습니다. (것으로)", "것으로", ["것은", "것이"], "것으로."), F("전문가들은 기온이 더 올라갈 ___ 예측했다. (것으로)", "것으로", ["것은", "것이"], "것으로."), F("중학생들의 이십 퍼센트가 담배를 피우는 것으로 ___. (was surveyed)", "조사됐다", ["보도했다", "전망했다"], "조사되다."), F("산사태로 백여 명이 숨진 것으로 ___. (was reported)", "알려졌다", ["조사했다", "예보했다"], "알려지다."), F("일주일 동안 태풍이 계속될 것으로 ___. (was forecast)", "예보됐다", ["밝혀졌다", "확인됐다"], "예보되다."),
           read_q("작년에 기름 값이 오른 것으로 나타났습니다"), read_q("한 배우가 협박을 당한 것으로 밝혀졌다"), read_q("전문가들은 기온이 더 올라갈 것으로 예측했다"), read_q("중학생들의 이십 퍼센트가 담배를 피우는 것으로 조사됐다"), read_q("한국 선수들이 금메달을 많이 딸 것으로 예상됩니다")]
    ),
)

# ================================================================== L8 Activities B: Earth Day and Paris agreement
_EARTH = [("이십이 일 로이터 통신에 따르면 유럽의 기후변화 단체들이 지구의 날에 영국 국회의사당 앞에 모여 지구 온난화 문제에 대한 대책을 세워 달라고 요구했다.", "According to Reuters on the 22nd, European climate change groups gathered in front of the Houses of Parliament in the UK on Earth Day and demanded that measures be taken on the problem of global warming."), ("또한 전 세계 봉사자들은 곳곳에서 나무를 심고 쓰레기 청소를 하면서 올해 지구의 날을 기념했다.", "Also, volunteers around the world commemorated this year’s Earth Day by planting trees and cleaning up trash in many places."), ("서울 광화문 광장에서도 지구의 날 기념행사가 열렸다.", "A commemorative event for Earth Day was held at Gwanghwamun Square in Seoul too."), ("쓰레기를 위한 지구는 없다를 주제로 여러 체험행사와 콘서트가 열렸다.", "With the theme “There is no Earth for trash”, various experience events and a concert were held."), ("지구의 날은 천구백육십구 년 환경운동가 존 맥코넬이 처음 제안해 시작됐다.", "Earth Day started when the environmental activist John McConnell first proposed it in 1969."), ("천구백칠십 년 사 월 이십이 일 미국에서 지구의 날 행사가 처음 열렸고 지금까지 이어지고 있다.", "The first Earth Day event was held in the United States on April 22, 1970 and has continued to this day."), ("지구는 점점 더워지고 있다.", "The Earth is getting hotter and hotter."), ("유엔 보고서에 따르면 지난해 지구 평균기온은 천팔백오십 년에서 천구백 년 평균보다 섭씨 일 점 일오 도 가량 높아졌다.", "According to a UN report, last year’s Earth average temperature rose about 1.15 degrees Celsius above the 1850–1900 average."), ("빙하 두께는 오십 년간 삼십 미터 가량 줄어들었고, 해수면 상승 속도는 최근 십 년 사이 두 배 빨라진 것으로 나타났다.", "Glacier thickness has decreased by about 30 m over 50 years, and the speed of sea level rise was found to have doubled in the last ten years.")]
_PARIS = [("파리협정 또는 파리기후변화협정은 이천십육 년에 체결됐습니다.", "The Paris Agreement, or the Paris Climate Change Agreement, was concluded in 2016."), ("그 목적은 국제사회가 같이 협력해서 지구온난화의 원인인 온실가스를 줄이자는 것입니다.", "Its purpose is for the international community to cooperate and reduce greenhouse gases, the cause of global warming."), ("온실가스를 줄여서 지구의 평균 온도 상승을 일 점 오 도로 제한하자는 것이지요.", "It is to reduce greenhouse gases and limit the rise in the Earth’s average temperature to 1.5 degrees."), ("파리협정에 가입한 국가들은 앞으로 온실가스 배출량을 얼마나 줄일 것인지 그 목표를 제시해야 합니다.", "Countries that joined the Paris Agreement must present their goals for how much they will reduce greenhouse gas emissions in the future."), ("예를 들면 이천삼십 년까지 프랑스는 오십오 퍼센트, 브라질은 사십삼 퍼센트, 한국은 이천십칠 년 대비 이십사 점 사 퍼센트를 감축하겠다는 목표를 제시했습니다.", "For example, by 2030 France presented a goal of reducing 55 percent, Brazil 43 percent, and Korea 24.4 percent compared with 2017."), ("또한, 미국은 이천오십 년까지, 중국은 이천육십 년까지 탄소중립을 하겠다는 목표를 제시했습니다.", "Also, the United States presented a goal of carbon neutrality by 2050 and China by 2060."), ("그런데 문제는 협정에 가입한 나라들이 국가별 목표를 달성해도 이천삼십 년 온실가스 배출량은 지금보다 일 퍼센트 낮아질 뿐이라고 합니다.", "But the problem is that even if the countries that joined the agreement achieve their national goals, they say the 2030 greenhouse gas emissions will be only 1 percent lower than now."), ("이렇게 되면 이천 년대 말까지 지구의 기온은 이 점 일 도에서 삼 도 상승하게 됩니다.", "If this happens, the Earth’s temperature will rise 2.1 to 3 degrees by the end of the 2000s."), ("이 정도의 상승은 지구의 생태계를 파괴할 만큼 큰 상승입니다.", "A rise of this degree is a rise large enough to destroy the Earth’s ecosystem.")]
L8 = lesson(
    "Ch 40 · Activities B: Earth Day and the Paris Agreement",
    "지구의 날 · 기후변화 단체 · 유엔 보고서 · 파리협정 · 온실가스 감축 목표 · 탄소중립",
    requires=[],
    cards=[
        card("Activity 1 (Reading): a news report about Earth Day",
             "The following news report is about Earth Day (Kyunghyang). The book glosses 국회의사당: Houses of Parliament; 평균: average; 두께: thickness. The report is the book’s with the numbers spelled out (UN is read 유엔); the English is mine.",
             examples=passage(_EARTH)),
        card("The answers (mine)", "The book asks (1) what the origin of this special day is, (2) how the day was celebrated in Europe, Seoul and around the world, and (3) what findings the UN report presents. My answers:",
             tables=[table(["Question", "Answer (mine)"], [["1. Origin", "It was first proposed by the environmental activist John McConnell, and the first event was held in the United States on April 22, 1970"], ["2. Europe", "Climate change groups gathered in front of the UK Houses of Parliament and demanded measures on global warming"], ["2. Seoul", "A commemorative event at Gwanghwamun Square with experience events and a concert on the theme “There is no Earth for trash”"], ["2. Around the world", "Volunteers planted trees and cleaned up trash in many places"], ["3. UN report", "Last year’s average Earth temperature was about 1.15 °C above the 1850–1900 average; glacier thickness decreased by about 30 m in 50 years; the speed of sea level rise doubled in the last ten years"]])]),
        card("Activity 3 (Reading): a Q and A about the Paris Agreement",
             "The following article is from a Q and A section of a portal site (the question was about homework on the Paris Agreement). The book glosses 목표를 제시하다: to present a goal; 감축: reduction; 탄소중립: carbon neutrality. The answer text is the book’s with the numbers spelled out (the English “Paris Agreement” in brackets is dropped); the English is mine.",
             examples=passage(_PARIS)),
        card("The table filled in (mine)", "The book’s table has the columns the purpose and the collective goal of the Paris Agreement, each country’s goal (Brazil, Korea, U.S.) and concerns. My answers:",
             tables=[table(["Item", "Answer (mine)"], [["Purpose and collective goal", "The international community cooperates to reduce greenhouse gases, the cause of global warming, and limit the rise in the Earth’s average temperature to 1.5 degrees"], ["Brazil", "Reduce by 43 percent by 2030"], ["Korea", "Reduce by 24.4 percent by 2030 compared with 2017"], ["U.S.", "Carbon neutrality by 2050"], ["Concerns", "Even if all countries meet their goals, 2030 emissions would be only 1 percent lower than now, and the temperature would rise 2.1 to 3 degrees by the end of the 2000s, enough to destroy the Earth’s ecosystem"]])]),
        card("Activities left out", "Activity 2 (listening to a YTN news report on global warming; the book glosses 평균: average; 대륙: continent) and its video, and Activity 4 (making a poster for the Ministry of Environment’s poster contest on the damages of global warming, with research and a presentation) are audio, video, group and poster activities."),
    ],
    exercises=uniq(
        _tr(_EARTH + _PARIS, k=3)
        + [M("Who first proposed Earth Day?", "An environmental activist", ["A president", "A scientist at the UN", "A farmer"], "환경운동가."), M("Where was the first Earth Day event held?", "The United States", ["Britain", "Korea", "France"], "미국에서 처음 열렸다."), M("What was the theme in Seoul?", "There is no Earth for trash", ["Save the glaciers", "Plant a tree", "Cooperate"], "쓰레기를 위한 지구는 없다."), M("How much has the average temperature risen according to the UN report?", "About 1.15 degrees Celsius", ["About 10 degrees", "About 0.1 degrees", "About 5 degrees"], "일 점 일오 도."), M("When was the Paris Agreement concluded?", "2016", ["1997", "2030", "2050"], "이천십육 년."), M("What temperature limit does the Paris Agreement aim at?", "1.5 degrees", ["5 degrees", "0.5 degrees", "10 degrees"], "일 점 오 도."), M("Which country aims at carbon neutrality by 2060?", "China", ["The United States", "Korea", "Brazil"], "중국은 이천육십 년까지."), M("What is the concern?", "Even meeting national goals reduces emissions only 1 percent", ["Countries refuse to join", "Emissions will vanish", "Temperature will fall"], "일 퍼센트 낮아질 뿐."),
           F("유럽의 기후변화 ___들이 국회의사당 앞에 모였다. (groups)", "단체", ["시민", "시장"], "단체."), F("지구 온난화 문제에 대한 ___을 세워 달라고 요구했다. (measures)", "대책", ["주제", "협력"], "대책."), F("국가들은 온실가스 배출량을 줄일 ___를 제시해야 한다. (goal)", "목표", ["대책", "주제"], "목표."), F("빙하 두께는 오십 년간 삼십 미터 가량 ___. (decreased)", "줄어들었다", ["늘어났다", "높아졌다"], "줄어들다."), F("온실가스를 줄여서 온도 상승을 ___하자는 것이다. (limit)", "제한", ["제거", "수거"], "제한."),
           read_q("지구의 날"), read_q("기후변화 단체들이 대책을 요구했습니다"), read_q("파리협정은 이천십육 년에 체결됐습니다"), read_q("온실가스를 줄여서 온도 상승을 제한하자는 것입니다"), read_q("탄소중립을 하겠다는 목표를 제시했습니다")]
    ),
)

# ================================================================== L9 Topic C
_C_DLG = [
    ("기자", "시장님, 이번에 울산시가 올해의 친환경 도시로 선정된 것을 축하드립니다.", "Mayor, congratulations on Ulsan City being selected as this year’s environment-friendly city."),
    ("시장", "네, 감사합니다.", "Yes, thank you."),
    ("기자", "먼저 환경 보호를 위해 울산시는 어떤 노력을 하고 있습니까?", "First, what efforts is Ulsan City making for environmental protection?"),
    ("시장", "네, 저희 시는 매주 수요일을 차 없는 날로 지정해서 시민들이 대중교통을 이용하도록 하고 있습니다. 또 자전거 이용도 적극적으로 권장하고 있습니다.", "Yes, our city designates every Wednesday as a car-free day so that citizens use public transportation. We are also actively encouraging the use of bicycles."),
    ("기자", "아, 그렇군요. 그리고 칠 월부터는 우리가 전기차를 살 때 보조금을 받을 수 있잖아요? 울산시에선 얼마나 보조해 주게 되나요?", "Oh, I see. And from July we can receive a subsidy when we buy an electric car, right? How much will Ulsan City subsidize?"),
    ("시장", "저희 시에선 최대 사백만 원까지 지원해 드릴 예정인데요, 사실 뉴스가 나가자 전기차 구입 문의가 평소보다 많이 늘었다고 합니다. 앞으로 전기차가 많아질 거니까 충전소 설치도 더 늘려갈 계획입니다.", "Our city plans to support up to 4 million won, and in fact they say that as soon as the news went out, inquiries about buying electric cars increased a lot more than usual. Since there will be more electric cars in the future, we also plan to increase the installation of charging stations."),
    ("기자", "아, 네. 앞으로 울산시는 자동차의 이산화탄소 배출량이 줄어서 온실가스도 많이 줄어들 것 같네요. 마지막으로 시장님, 환경보존을 위해 저희들이 일상생활에서 무엇을 실천하면 좋을까요?", "Oh, yes. In the future, it seems Ulsan’s cars’ carbon dioxide emissions will decrease and greenhouse gases will also decrease a lot. Lastly, Mayor, what would be good for us to put into practice in daily life for environmental preservation?"),
    ("시장", "일회용품의 지나친 사용을 자제하시고 친환경 제품을 사용하신다면 큰 도움이 될 겁니다.", "If you refrain from excessive use of disposable goods and use environment-friendly products, it will be a great help."),
]
_C_WORDS = ["경차", "권장", "냉방", "보조금", "보존", "보호", "사실", "선정", "시민", "시장", "식물", "실천", "이면지", "일상", "일회용품", "자원", "자제", "지나치다", "지정", "충전소", "친환경", "평소", "홍보"]
L9 = lesson(
    "Ch 40 · Topic C: An interview with the mayor of an eco-friendly city (친환경 도시 시장님과의 인터뷰)",
    "친환경 도시 시장님과의 인터뷰 · 차 없는 날 · 전기차 보조금 · 충전소 · 일회용품 자제 · 환경보존",
    requires=[],
    cards=[
        card("Topic C: An interview with the mayor of an eco-friendly city (친환경 도시 시장님과의 인터뷰)",
             "The following text is an excerpt from a radio program in which a reporter is interviewing a mayor about his city’s efforts to protect the environment. (The English is mine; the book gives none; the month and the amount are spelled out in Hangul.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists –자 and –다면 (see the grammar).",
             tables=[ktable(_rows(_C_WORDS)), table(["Word", "Meaning"], [["-자", "(as soon) as; (right) after; when"], ["-다면", "conjunctive ending for a hypothetical condition"]], say=[0]) if False else table(["Pattern", "Meaning"], [["-자", "(as soon) as; (right) after; when"], ["-다면", "conjunctive ending for a hypothetical condition"]])]),
        card("Follow-up 1 (Reading): an email on resource and energy conservation",
             "The following e-mail is about resource and energy conservation and is from the general affairs department of a company to its employees. The book asks you to read it and fill in the table with the five suggestions and the specific directions in English. The e-mail is the book’s with the numbers spelled out (the five suggestions are written as the lines starting with the topic sentence); the English is mine.",
             examples=passage([("전 사원 자원 보존과 에너지 절약을 실천합시다.", "To all employees: Let’s put resource conservation and energy saving into practice."), ("사원 여러분, 안녕하십니까?", "Employees, hello."), ("저희 총무부에서는 오늘부터 팔 월 말까지 여름기간 동안 에너지 절약 및 자원 보존 캠페인을 벌입니다.", "Our general affairs department will run an energy saving and resource conservation campaign during the summer period from today until the end of August."), ("사원 여러분께서 적극적으로 참여하셔서 이산화탄소 배출을 다같이 줄여 봅시다.", "Let’s all reduce carbon dioxide emissions together with your active participation."), ("전기를 아낍시다. 점심시간과 퇴근할 때 컴퓨터와 프린터를 꺼 주세요. 또, 사원 라운지의 커피메이커도 다 사용한 후에는 플러그를 빼 주세요.", "Let’s save electricity. Please turn off computers and printers at lunchtime and when leaving work. Also, please unplug the coffee maker in the employee lounge after you have finished using it."), ("기름을 아낍시다. 근처에 사는 동료를 찾아서 카풀 할 수 있는지 알아보세요. 또, 가능한 한 자주 대중교통을 이용해 주세요.", "Let’s save fuel. Find a coworker who lives nearby and see if you can carpool. Also, please use public transportation as often as possible."), ("재활용을 합시다. 종이컵이나 음료수 병, 캔은 잘 헹군 후에 재활용 쓰레기통에 넣어 주세요. 또, 코팅이 되어 있지 않은 종이나 상자도 종이 수거함에 넣어 주세요.", "Let’s recycle. Please rinse paper cups, beverage bottles and cans well and put them in the recycling bin. Also, please put paper or boxes that are not coated in the paper collection box."), ("종이를 아낍시다. 복사할 때는 중요한 서류가 아니면 이면지를 활용하세요. 또, 가능하면 전자문서를 사용하도록 하세요.", "Let’s save paper. When copying, use scratch paper unless it is an important document. Also, try to use electronic documents if possible."), ("지나친 냉방을 자제합시다. 사무실 온도를 여름철 실내 적정온도인 이십육 도에서 이십팔 도로 맞추세요.", "Let’s refrain from excessive air conditioning. Set the office temperature to 26 to 28 degrees, the optimal indoor temperature in summer.")])),
        card("The table filled in (mine)", "The book glosses 전자문서: electronic document; 적정: optimal. My answers:",
             tables=[table(["Suggestion", "Specific direction(s) (mine)"], [["1. Save electricity", "Turn off computers and printers at lunchtime and when leaving work; unplug the lounge coffee maker after use"], ["2. Save fuel", "Find a nearby coworker to carpool with; use public transportation as often as possible"], ["3. Recycle", "Rinse paper cups, bottles and cans and put them in the recycling bin; put uncoated paper and boxes in the paper collection box"], ["4. Save paper", "Use scratch paper for copies unless the document is important; use electronic documents when possible"], ["5. Refrain from excessive air conditioning", "Set the office temperature to 26–28 degrees, the optimal summer indoor temperature"]])]),
        card("Activities left out", "The presentation steps of Topic C (SMART Board) and Follow-up 2 (listening to two conversations between a high school teacher and a student about an environmental issue) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG), k=3)
        + [M("Why was Ulsan City congratulated?", "It was selected as this year’s environment-friendly city", ["It won a car race", "It has the most cars", "It banned all cars"], "올해의 친환경 도시로 선정."), M("Which day is the car-free day?", "Every Wednesday", ["Every Monday", "Every Sunday", "Every Friday"], "매주 수요일."), M("How much is the maximum electric car subsidy?", "4 million won", ["400,000 won", "40 million won", "400 million won"], "사백만 원."), M("What happened after the news went out?", "Inquiries about buying electric cars increased", ["Gas prices fell", "Cars were banned", "Buses stopped"], "문의가 평소보다 많이 늘었다."), M("What is the city planning to increase?", "Charging stations", ["Parking lots", "Gas stations", "Highways"], "충전소 설치."), M("What does the mayor ask of citizens?", "Refrain from excessive use of disposable goods and use eco-friendly products", ["Stop eating", "Buy more cars", "Use more paper"], "일회용품의 지나친 사용을 자제."), M("What is the office temperature recommended in the email?", "26 to 28 degrees", ["16 to 18 degrees", "30 to 35 degrees", "20 to 22 degrees"], "이십육 도에서 이십팔 도."),
           F("울산시는 매주 수요일을 차 없는 날로 ___했습니다. (designated)", "지정", ["선정", "제한"], "지정."), F("자전거 이용도 적극적으로 ___하고 있습니다. (encouraging)", "권장", ["제한", "자제"], "권장."), F("전기차를 사면 ___을 받을 수 있습니다. (subsidy)", "보조금", ["대책", "자원"], "보조금."), F("일회용품의 지나친 사용을 ___하세요. (refrain)", "자제", ["실천", "홍보"], "자제."), F("환경보존을 위해 무엇을 ___하면 좋을까요? (practice)", "실천", ["권장", "자제"], "실천."),
           read_q("친환경 도시 시장님과의 인터뷰"), read_q("매주 수요일을 차 없는 날로 지정했습니다"), read_q("전기차를 사면 보조금을 받을 수 있습니다"), read_q("충전소 설치도 더 늘려갈 계획입니다"), read_q("일회용품의 지나친 사용을 자제하세요")]
    ),
)

# ================================================================== L10 Grammar C: -자
_JA1 = [("집을 나서자 비가 그쳤다.", "As soon as I walked out of the house, it stopped raining."), ("바람이 불자 전기가 나갔다.", "As / When the wind blew, the electricity went out.")]
_JA2 = [("엄마를 보자 아기가 웃었다.", "As soon as he saw his mom, the baby smiled. (without-interval-of-time implication) or When he saw his mom, the baby smiled. (cause-and-effect implication)")]
_JA3 = [("폭우가 쏟아지자 온 도시가 물에 잠겼습니다.", "As heavy rain poured down, the whole town was submerged in water."), ("장마가 그치자 무더위가 시작되었다.", "As soon as the rainy season stopped, a sweltering heat began.")]
_JAM = [("초속 사십 미터의 강풍이 불자 도로 표지판들이 날아갔다.", "도로 표지판들이 날아갔다", "As a strong wind of 40 m per second blew, the road signs flew away."), ("삼 일 동안 계속해서 폭설이 내리자 시내 교통이 마비되었다.", "시내 교통이 마비되었다", "As heavy snow kept falling for three days, traffic in the city was paralyzed."), ("집중호우 때문에 집들이 물에 잠기자 수재민이 발생했다.", "수재민이 발생했다", "As houses were submerged because of the concentrated heavy rain, flood victims occurred."), ("화재가 발생하자 소방관이 즉시 출동했다.", "소방관이 즉시 출동했다", "As a fire broke out, the firefighters were dispatched immediately."), ("생일날 집에 들어서자 친구들이 소리치면서 나타났다.", "친구들이 나타났다", "As I entered the house on my birthday, friends appeared shouting."), ("일회용품 사용이 늘어나자 쓰레기 양도 늘어났다.", "쓰레기 양도 늘어났다", "As the use of disposable goods increased, the amount of trash also increased.")]
_JAR = [("십오 일 밤 중국 청도에서 지진이 일어나자 주변지역 주민들은 빨리 건물 밖으로 대피했다.", "An earthquake occurred in Qingdao, China on the night of the 15th", "The residents of surrounding areas quickly evacuated out of the buildings", "On the night of the 15th, as an earthquake occurred in Qingdao, China, residents of the surrounding areas quickly evacuated out of the buildings."), ("십육 일 아침부터 시간당 최고 구십 밀리미터의 비가 내리자 부산기상청은 이 지역에 호우주의보를 내렸다.", "From the morning of the 16th rain of up to 90 mm per hour fell", "The Busan weather office issued a heavy rain advisory for the area", "As rain of up to 90 mm per hour fell from the morning of the 16th, the Busan weather office issued a heavy rain advisory for this area."), ("지리산에서 산불이 발생하자 산불 진화 차와 이백오십 명의 소방관이 출동해 불을 진화했다.", "A wildfire broke out on Jirisan", "Fire engines and 250 firefighters were dispatched and put out the fire", "As a wildfire broke out on Jirisan, wildfire-fighting vehicles and 250 firefighters were dispatched and put out the fire."), ("기상청이 강원도 지방에 호우주의보를 내리자 이 지역 주민은 홍수에 대한 대책을 마련하고 있다.", "The weather agency issued a heavy rain advisory for Gangwon-do", "Residents of this area are preparing measures against floods", "As the weather agency issued a heavy rain advisory for Gangwon-do, residents of this area are preparing measures against floods.")]
L10 = lesson(
    "Ch 40 · Grammar C: the conjunctive ending –자 (as soon as, when)",
    "-자 · 집을 나서자 · 바람이 불자 · 폭우가 쏟아지자 · 장마가 그치자 · -자마자",
    requires=[],
    cards=[
        card("Two implications",
             "The conjunctive ending –자 can be used to indicate either of the following implications:\n\n"
             "1. Without-interval-of-time implication. In this case, the conjunctive ending implies that two events or actions occurred without an interval of time. Thus –자 can be translated as as soon as, immediately after, the moment that, or upon, as in 집을 나서자 비가 그쳤다 (As soon as I walked out of the house, it stopped raining). The sentence implies that it stopped raining as soon as (or immediately after) the speaker walked out of the house. Thus, –자 in this sentence can be replaced with –자마자, which you learned about in Chapter 20.\n\n"
             "2. Cause-and-Effect implication. In this case, the conjunctive ending implies that two events or actions occurred in sequence and that the speaker suspects the first event/action triggered the second event/action. –자 can be translated as as or when, as in 바람이 불자 전기가 나갔다 (As/When the wind blew, the electricity went out). In this sentence, the speaker suspects that wind blowing (the first event) triggered the blackout (the second event).",
             examples=passage(_JA1)),
        card("Both implications",
             "Depending on the context, many of the sentences that use the conjunctive ending –자 can convey either of the implications. For example (the English is the book’s):",
             examples=passage(_JA2)),
        card("Only for an action that already took place",
             "Keep in mind that this conjunctive ending is used solely for an action or event that already took place or started taking place. Thus the following sentences in which an action/event has not yet taken place are ungrammatical (the asterisk * indicates that the marked phrase/sentence is ungrammatical): 엄마를 보자 아기가 *웃겠어요. 집을 나서자 비가 *그치겠어요. 장마가 그치자 *바비큐하자! 선생님이 들어오자 *일어서세요.\n\n"
             "Note that the conjunctive ending –자 occurs more often in written language, including news reports, than in colloquial language. More examples (the English is the book’s):",
             examples=passage(_JA3)),
        card("Follow-up 1 (Reading): conjugate with –자 and match",
             "For each clause in List A, conjugate the verb with –자, then match it with a clause in List B that can be logically connected (the book gives the first, 불자, as the example). The clauses are the book’s with the number spelled out; my matches are given as complete sentences; the English is mine.",
             examples=passage([(a, c) for a, b, c in _JAM])),
        card("Follow-up 3 (Reading): –자 in news excerpts",
             "The following excerpts are from newspaper articles about natural disasters or extreme weather. The book asks you to circle all the verbs with –자, identify the two actions or events in each excerpt and fill in a table in English. The excerpts are the book’s with the numbers spelled out; the table and the English are mine.",
             examples=passage([(a, d) for a, b, c, d in _JAR]),
             tables=[table(["No.", "First action/event (mine)", "Second action/event (mine)"], [[str(i + 1), b, c] for i, (a, b, c, d) in enumerate(_JAR)])]),
        card("Activities left out", "Follow-up 2 (listening to three clips and writing the first and second action or event) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_JA1 + _JA3 + [(a, c) for a, b, c in _JAM] + [(a, d) for a, b, c, d in _JAR], k=3)
        + [M("What does –자 mean?", "as soon as; when", ["because", "if", "although"], "The book’s note."), M("What kind of events can follow –자?", "Events that already took place or started", ["Future events", "Commands", "Suggestions"], "The book’s note."), M("Which sentence is ungrammatical?", "집을 나서자 비가 그치겠어요", ["집을 나서자 비가 그쳤다", "바람이 불자 전기가 나갔다", "폭우가 쏟아지자 도시가 잠겼다"], "–자 is only for completed events."), M("What can replace –자 in the without-interval implication?", "–자마자", ["–고서", "–(으)면", "–는데"], "The book’s note."), M("Where does –자 occur more often?", "In written language, including news reports", ["In conversation", "In songs", "In questions"], "The book’s note."), M("What does 바람이 불자 전기가 나갔다 mean?", "As / When the wind blew, the electricity went out", ["The wind blew because of the blackout", "The electricity will go out", "If the wind blows"], "The book’s example."),
           F("집을 나서___ 비가 그쳤다. (as soon as)", "자", ["면", "서"], "-자."), F("바람이 불___ 전기가 나갔다. (as)", "자", ["면", "서"], "-자."), F("폭우가 쏟아지___ 온 도시가 물에 잠겼습니다. (as)", "자", ["면", "서"], "-자."), F("장마가 그치___ 무더위가 시작되었다. (as soon as)", "자", ["면", "서"], "-자."), F("화재가 발생하___ 소방관이 즉시 출동했다. (as)", "자", ["면", "서"], "-자."),
           read_q("집을 나서자 비가 그쳤다"), read_q("바람이 불자 전기가 나갔다"), read_q("폭우가 쏟아지자 온 도시가 물에 잠겼습니다"), read_q("장마가 그치자 무더위가 시작되었다"), read_q("화재가 발생하자 소방관이 즉시 출동했다")]
    ),
)

# ================================================================== L11 Grammar D: -다면
_DM1 = [("주말에 비가 오면 저는 영화를 봐요.", "I watch a movie if (or when) it rains on weekends. (factual conditional)"), ("주말에 비가 오면 저는 영화를 볼 거예요.", "I will watch a movie if it rains this weekend. (future/predictive conditional)")]
_DM2 = [("만약 백만 불이 있다면 하와이에 이사갈 거예요.", "If I had a million dollars (now), I would move to Hawaii. (counterfactual)"), ("만약 백만 불이 생긴다면 무엇을 하겠어요?", "If you had a million dollars, what would you do? (hypothetical)")]
_DM3 = [("만약 내가 한국사람이라면 한국말을 늘 쓰겠지요.", "If I were Korean, I would use Korean every day.")]
_DM4 = [("그때 제가 백만 불이 있었다면 아마 그 집을 샀을 거예요.", "If I had had a million dollars, I would have bought that house."), ("만약 백만 불이 있었다면 무엇을 했겠어요?", "If you had had a million dollars, what would you have done?")]
_DM5 = [("아버지가 이번 크리스마스에 오신다면 같이 하와이에 갈 거예요.", "If my father were to visit this Christmas, we would go to Hawaii together."), ("아버지가 지난 크리스마스에 오셨다면 같이 하와이에 갔을 거예요.", "If my father had visited last Christmas, we would have gone to Hawaii together."), ("내가 너라면 공부를 열심히 하겠다.", "If I were you, I would study hard."), ("우리 집이 크다면 집에서 생일파티를 했을 거예요.", "If my house were bigger, I would have thrown a birthday party at home.")]
_DM6 = [("만약 우리가 음식물 쓰레기를 이십 퍼센트 더 줄일 수 있다면 온실가스를 사백만 톤가량 줄일 수 있을 겁니다.", "If we could reduce food waste by another 20 percent, we could reduce greenhouse gases by about 4 million tons."), ("서울 시민이 모두 자가용을 타지 않고 자전거를 탄다면 온실가스 배출을 크게 줄일 수 있을 겁니다.", "If all Seoul citizens rode bicycles instead of private cars, greenhouse gas emissions could be greatly reduced."), ("만약 음료수 캔이나 이면지를 백 퍼센트 재활용할 수 있다면 종이를 구십 퍼센트까지 절약할 수 있습니다.", "If beverage cans or scratch paper could be recycled 100 percent, paper could be saved by up to 90 percent.")]
_DM7 = [("한국에 간다", "(만약) 한국에 간다면", "만약 한국에 간다면 한국말을 많이 할 거예요.", "If I go to Korea, I will speak a lot of Korean.")]
_DMM = [("비가 온다면 집에 있겠어요.", "If it rains, I will stay home."), ("만약 시간이 있었다면 같이 갔을 거예요.", "If I had had time, I would have gone together."), ("내가 대통령이라면 환경을 먼저 보호하겠어요.", "If I were president, I would protect the environment first.")]
L11 = lesson(
    "Ch 40 · Grammar D: the conjunctive ending (만약) … –다면 for a hypothetical condition",
    "-다면 · 만약 · -ㄴ/는다면 · -았/었다면 · -(이)라면 · 백만 불이 있다면",
    requires=[],
    cards=[
        card("Recall –(으)면",
             "Recall the conjunctive ending –(으)면 that we use to express a conditional. This conjunctive ending is normally used to express either a factual conditional relationship or a future (or predictive) conditional relationship. For example (the English is the book’s):",
             examples=passage(_DM1)),
        card("What the two examples show", "The first sentence expresses a factual conditional relationship. It can be interpreted as “If (or When) something happens, I do this/that.” The second sentence, however, expresses a future (or predictive) conditional relationship and can be interpreted as “If something happens in the future, I will do this/that.” However, this conjunctive ending is rarely used to express a hypothetical conditional relationship or a counterfactual relationship. For this conditional, Koreans often use the conjunctive ending (만약) … 다면. For example (the English is the book’s):", examples=passage(_DM2)),
        card("만약 and 다면", "만약, which begins the clause, is optional but its presence clearly tells us that the following clause is a hypothetical or counterfactual conditional. Note that 다 in 다면 is the formal blunt speech style and the above examples are present hypothetical/counterfactual conditionals. However, the verb 이다 turns into 이라면, not 이다면. (The English is the book’s.)", examples=passage(_DM3)),
        card("The past", "To express past hypothetical/counterfactual conditionals, we add the past tense marker to both clauses. For example (the English is the book’s):", examples=passage(_DM4)),
        card("Expressing a hypothetical condition", "(만약) … 다면. More examples (the English is the book’s):", examples=passage(_DM5)),
        card("Follow-up 4 (Speaking): the model", "Partners take a verbal phrase strip, conjugate the verb with 다면 (using (만약) … –ㄴ/는다면 or (만약) … –았/었다면) and the partner completes the sentence with a logically appropriate clause. The book’s model (the English is mine):", examples=dlg([("A", "만약 한국에 간다면", "If I go to Korea,"), ("B", _DM7[0][2], _DM7[0][3])])),
        card("Follow-up 6 (Reading): guidelines for environmental conservation",
             "The following guidelines for environmental conservation are on the website of an environmental protection group. The book asks you to find and underline the conjunctive ending 다면 and translate those sentences into English. The sentences with 다면 below are the book’s (the numbers are spelled out); the English is mine. The guidelines are: 1. Let’s reduce food waste; 2. Let’s use bicycles and public transportation; 3. Let’s make recycling a habit.",
             examples=passage(_DM6)),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_DMM)),
        card("Activities left out", "Follow-up 5 (listening to four conversations between two friends and writing the hypothetical condition and the action) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_DM1 + _DM2 + _DM3 + _DM4 + _DM5 + _DM6 + _DMM, k=3)
        + [M("What is –다면 used for?", "A hypothetical or counterfactual condition", ["A factual habit", "A reason", "A request"], "The book’s note."), M("What does 만약 do?", "Tells us the clause is hypothetical or counterfactual (it is optional)", ["Marks the past", "Marks a question", "Marks a command"], "The book’s note."), M("What does 이다 turn into before 면?", "이라면", ["이다면", "이면다", "이고면"], "The book’s note."), M("How do we form a past hypothetical?", "Add the past tense marker to both clauses", ["Drop 다면", "Use –(으)ㄹ 것", "Use –자"], "The book’s note."), M("What does 내가 너라면 공부를 열심히 하겠다 mean?", "If I were you, I would study hard", ["If you were me", "I studied hard", "I will study hard"], "The book’s example."), M("What does 아버지가 지난 크리스마스에 오셨다면 같이 하와이에 갔을 거예요 mean?", "If my father had visited last Christmas, we would have gone to Hawaii together", ["My father will visit", "My father visited and we went", "We will go to Hawaii"], "The book’s example."),
           F("만약 백만 불이 ___ 하와이에 이사갈 거예요. (if I had)", "있다면", ["있으면다", "있고"], "있다면."), F("내가 한국사람___ 한국말을 늘 쓰겠지요. (if I were)", "이라면", ["이다면", "이면다"], "이라면."), F("그때 제가 백만 불이 ___ 아마 그 집을 샀을 거예요. (had had)", "있었다면", ["있다면", "있으면"], "있었다면."), F("(만약) 한국에 ___ 한국말을 많이 할 거예요. (if I go)", "간다면", ["갔다면", "가다면"], "간다면."), F("만약 우리가 음식물 쓰레기를 더 줄일 수 있___ 온실가스를 줄일 수 있을 겁니다. (if)", "다면", ["고", "서"], "-다면."),
           read_q("만약 백만 불이 있다면 하와이에 이사갈 거예요"), read_q("만약 내가 한국사람이라면 한국말을 늘 쓰겠지요"), read_q("아버지가 이번 크리스마스에 오신다면 같이 하와이에 갈 거예요"), read_q("내가 너라면 공부를 열심히 하겠다"), read_q("서울 시민이 모두 자전거를 탄다면 온실가스 배출을 크게 줄일 수 있을 겁니다")]
    ),
)

# ================================================================== L12 Activities C + self-eval
_ULS = [("울산시가 매주 수요일을 녹색생활 실천의 날로 지정해 운영하는 가운데 공직자가 실천해야 할 열 가지 수칙을 선정했다.", "While Ulsan City designates and operates every Wednesday as a Green Life Practice Day, it has selected ten rules that public officials must practice."), ("삼 일 시에 따르면 공직자들은 여름에 넥타이 풀고 겨울에 내복 입기, 걷기, 자전거, 대중교통, 경차, 카풀 적극 이용하기, 청사 내 계단 이용하기, 녹색사무실 가꾸기, 구내식당 이용 시 반찬 남기지 않기 등을 실천할 예정이다.", "According to the city on the 3rd, public officials plan to practice taking off neckties in summer and wearing long underwear in winter; actively using walking, bicycles, public transportation, compact cars and carpools; using the stairs inside the government building; tending a green office; and not leaving side dishes when using the cafeteria."), ("또 이면지 재활용, 자연채광 활용 전기 절약, 부재 시 컴퓨터와 프린터, 복사기 전원 끄기, 일회용품 사용 자제와 재활용품 분리수거 철저, 매주 수요일 자기능력 개발 등을 실천한다.", "They will also practice recycling scratch paper; saving electricity by using natural lighting; turning off the power of computers, printers and copiers when absent; refraining from using disposable goods and thorough separation of recyclables; and developing one’s own abilities every Wednesday.")]
L12 = lesson(
    "Ch 40 · Activities C: a city’s rules for public officials · and self-evaluation",
    "녹색생활 실천의 날 · 공직자 수칙 · 이면지 재활용 · 자원 절약 · 자기 평가",
    requires=[],
    cards=[
        card("Activity 3 (Reading): a local newspaper article about Ulsan",
             "The following excerpt is from a local Korean newspaper article (Yonhap News). The book glosses 공직자: a government employee/official; 수칙: rules. The excerpt is the book’s with the numbers spelled out and the book’s △ marks replaced by commas; the English “Green Day” in brackets is dropped; the English is mine. The book asks you to write the topic in Korean, and then to match Set A phrases with paraphrased sentences from Set B (strips).",
             examples=passage(_ULS)),
        card("The topic (mine)", "A topic for the article: 울산시가 선정한 공직자의 환경 실천 수칙 열 가지 (the ten environmental practice rules that Ulsan City selected for public officials)."),
        card("Activity 5 (Writing and speaking): save resources!",
             "A contest for the best ideas to conserve resources and protect the environment will be held in your city. You and your partner will enter the competition and submit your ideas: each of you thinks of at least three ideas (written in English), you talk about them in Korean, choose the three best and post them, and rate other teams’ ideas with 1 to 5 stars."),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with.\n\n"
             "Now I am able to: identify waste separation and disposal methods; extract factual information about and discuss global warming, its causes, impact, and preventive measures; make suggestions on how to reduce food waste; and talk about the efforts to conserve resources and protect the environment.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the conjunctive ending –자; expressions frequently used in news reports; –(으)ㅁ and –(으)ㄹ 것, abbreviated verb endings used in writing; the conjunctive ending –다면 for a hypothetical condition; and the Sino-Korean syllables within 분리 (分離), 재활용 (再活用), 온난화 (溫暖化), 식물 (植物), and 경차 (輕車)."),
        card("Activities left out", "Activity 1 (SMART Board), Activity 2 (listening to YTN news clips about the government’s efforts to conserve resources and matching them with titles: Developing Alternative Energy; Campaign for Saving Energy/Energy-Saving Measures; Reducing Use of Disposable Products, one does not match; the book glosses 머그잔: a mug; 환경부: Ministry of Environment; 행정안전부/행안부: Ministry of the Interior and Safety) and Activity 4 (listening to MBC news on local government subsidy programs: Chuncheon City’s purpose, who is eligible and the amount, and why more local governments are implementing them; the book glosses 지자체: local government; 사업: program; 이동(하다): movement [to move]; 수단: means; method) are audio, video and computer activities."),
    ],
    exercises=uniq(
        _tr(_ULS, k=3)
        + [M("Which day is the Green Life Practice Day in Ulsan?", "Every Wednesday", ["Every Monday", "Every Friday", "Every Sunday"], "매주 수요일."), M("How many rules did Ulsan City select?", "Ten", ["Five", "Twenty", "Three"], "열 가지."), M("What should officials do in summer?", "Take off their neckties", ["Wear coats", "Wear hats", "Work at night"], "여름에 넥타이 풀고."), M("What should officials do when absent?", "Turn off the power of computers, printers and copiers", ["Leave them on", "Unplug the lights only", "Turn on the air conditioner"], "부재 시 전원 끄기."), M("What should officials do in the cafeteria?", "Not leave side dishes", ["Eat quickly", "Bring their own food", "Pay in cash"], "반찬 남기지 않기."),
           F("매주 수요일 자기능력 ___을 한다. (development)", "개발", ["보호", "분리"], "개발."), F("일회용품 사용 ___와 재활용품 분리수거 철저. (refraining)", "자제", ["권장", "실천"], "자제."), F("공직자가 ___해야 할 열 가지 수칙을 선정했다. (practice)", "실천", ["선정", "지정"], "실천."), F("울산시가 매주 수요일을 녹색생활 실천의 날로 ___했다. (designated)", "지정", ["선정", "제한"], "지정."), F("이면지를 ___하면 종이를 절약할 수 있다. (recycle)", "재활용", ["수거", "배출"], "재활용."),
           read_q("녹색생활 실천의 날"), read_q("공직자가 실천해야 할 수칙"), read_q("이면지를 재활용합니다"), read_q("일회용품 사용을 자제합니다"), read_q("재활용품을 분리수거합니다")]
    ),
)

# ================================================================== L13 core vocabulary
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/") and " " not in r[0]]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0] and "…" not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L13 = lesson(
    "Ch 40 · Core vocabulary",
    "주요 단어 · 환경 · 분리수거 · 온난화 · 친환경 · 자원 · 실천",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. 팩 is listed also as a loan word.\n\n"
             "The example sentences with digits are respelled in Hangul (2팩 → 두 팩; 영하 50도 → 영하 오십 도; 1.5℃ → 일 점 오 도; 40대 → 사십 대; 10월 → 시월; 2배 → 두 배; TV → 티브이; the English “PET” and “ℓ” notes are in the meaning only). The quotation marks in the example of 주제 are dropped."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 온실가스 mean?", "greenhouse gas", ["carbon dioxide only", "a glacier", "a climate"], "溫室."), M("What does 이산화탄소 mean?", "carbon dioxide", ["greenhouse gas", "oxygen", "a plant"], "二酸化炭素."), M("What does 빙하 mean?", "a glacier", ["a coast", "a sea level", "an ecosystem"], "氷河."), M("What does 해수면 mean?", "sea level", ["a glacier", "a coast", "the Earth"], "海水面."), M("What does 생태계 mean?", "an ecosystem", ["a climate", "a crop", "a glacier"], "生態系."), M("What does 일회용품 mean?", "disposable goods", ["recyclables", "resources", "scratch paper"], "一回用品."), M("What does 친환경 mean?", "environment-friendly", ["polluting", "disposable", "expensive"], "親環境."), M("What does 종량제 mean?", "the meter-rate system", ["a recycling bin", "a tax", "a market"], "從量制."),
           F("종이, 물, 기름 같은 ___을 아껴 쓰는 습관을 기릅시다. (resources)", "자원", ["시민", "식물"], "자원."), F("지구 ___의 영향으로 자연재해가 발생하고 있다. (global warming)", "온난화", ["분리", "경차"], "온난화."), F("요즘은 기름값이 비싸서 ___가 인기예요. (compact car)", "경차", ["충전소", "시민"], "경차."), F("무색 페트병을 ___할 때 뚜껑을 닫고 버리세요. (dispose of)", "배출", ["수거", "압축"], "배출."), F("정부는 티브이 광고로 새 정책을 ___하고 있습니다. (publicize)", "홍보", ["협력", "관측"], "홍보."),
           read_q("주요 단어"), read_q("온실가스"), read_q("해수면"), read_q("생태계"), read_q("일회용품")]
    ),
)

UNIT = unit("Semester 2 · Unit 10 · Chapter 40: The Environment (환경)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])

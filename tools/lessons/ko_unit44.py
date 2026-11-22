"""Unit 44: KBC Semester 2, Unit 10, Chapter 37 - Accidents (사고).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 10, Student's Edition (2022).
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's.
The name of a real person in one news article is left out."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 37 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("경상", "(輕傷) a light injury; a minor wound; to sustain a light injury (~입다)", "큰 사고였지만 다행히 사람들이 경상만 입었다."),
    ("골목(길)", "an alley", "위험하니까 밤에는 어두운 골목길로 다니지 마세요."),
    ("긴급", "(緊急) urgent; to be urgent (~하다)", "중요한 문제가 발생했으니 긴급회의를 합시다."),
    ("놀라다", "to be surprised; to be startled; to be astonished", "한밤중에 폭발 소리가 나서 잠자던 주민들이 놀라서 대피했다."),
    ("누전", "(漏電) a short circuit; “leaked electricity”; to short circuit (~되다)", "오래된 건물에서는 누전으로 인해 화재가 발생할 수 있다. 그러니까 자주 점검해야 한다."),
    ("당국", "(當局) the authorities; “the office in charge”", "소방 당국에 따르면 오 월에 부주의로 인한 화재가 많이 발생한다고 한다."),
    ("목격", "(目擊) (eye) witnessing; observation; to observe; to witness; to be observed (~하다/되다)", "사고를 목격하신 분은 경찰에 연락해 주시기 바랍니다."),
    ("목격자", "(目擊者) an eyewitness", "지난달에 발생한 교통사고의 목격자를 찾습니다."),
    ("발견", "(發見) discovery; detection; to discover / to be discovered (~하다/되다)", "암을 일찍 발견하면 쉽게 치료할 수 있습니다."),
    ("발생", "(發生) occurrence; to occur; to happen (~하다)", "최근 반려동물에 의한 화재가 자주 발생한다."),
    ("번지다", "to spread", "요즘 새로운 독감이 아주 빠른 속도로 번지고 있어요."),
    ("부상", "(負傷) a wound; an injury; to be injured; to sustain an injury (~입다/당하다)", "지하철 화재로 이십 명이 부상을 당했습니다."),
    ("부주의", "(不注意) carelessness; negligence; “no caution”", "운전 부주의로 교통사고가 발생했습니다."),
    ("불", "fire; a light", "아이들이 불 가까이 가지 못하게 하세요. 잘못하면 화상을 입어요."),
    ("소방차", "(消防車) a fire engine; a fire truck; “fire-extinguishing vehicle”", "소방차가 출동할 때 다른 차들은 길 옆으로 비켜서야 합니다."),
    ("소식", "(消息) news", "내년에 월급이 많이 오른다는 소식이 있습니다."),
    ("이송", "(移送) transfer (of a patient, a criminal, legal case, etc.); to transfer / to be transferred (~하다/되다); “moving and sending”", "지금 환자를 서울에 있는 병원으로 이송하고 있습니다."),
    ("인명", "(人命) human life", "지난 주에 발생한 화재로 수많은 인명 피해가 있었다."),
    ("장난", "a prank; mischief; a naughty thing; a trick; to play around; to mess around (~하다/치다)", "제 막내가 계단에서 장난치다가 떨어져서 팔을 삐었어요."),
    ("재산", "(財産) an estate; property; wealth; an asset", "건강이 가장 큰 재산입니다."),
    ("전체", "(全體) the whole; the totality; “whole body”", "오래된 집을 샀기 때문에 집 전체를 수리해야 했습니다."),
    ("죽다 / 사망하다 / 숨지다 / 돌아가시다", "to die; to pass away (돌아가시다 is honorific)", "교통사고로 세 명이 숨지고 열다섯 명이 부상을 입었습니다. 할머니께서 교통사고로 돌아가셨습니다."),
    ("중상", "(重傷) a serious injury; a severe wound; “heavy injury”; to sustain a heavy injury (~입다)", "그 충돌사고로 버스 기사는 중상을 입었어요."),
    ("진화", "(鎭火) putting out a fire; “suppressing fire”; to extinguish / to be extinguished (~하다/되다)", "산불이 많이 번져서 진화하는 데 시간이 오래 걸렸어요. 소방차가 오자마자 불은 바로 진화되었어요."),
    ("타다", "(something) to burn; to blaze; to be on fire", "어제 고기를 요리했는데 좀 탔어요. 그래도 맛은 괜찮았어요."),
    ("태우다", "to burn (something)", "다림질을 하다가 바지를 태웠어요."),
    ("폭발", "(爆發) explosion; to explode; to blow up (~하다)", "오늘 새벽 파키스탄의 한 호텔에서 폭발 사고가 일어났습니다."),
    ("피해", "(被害) damage; to be damaged (~입다/당하다)", "어제 발생한 산불로 인해 주택 삼십여 채가 타는 등 피해가 컸다."),
    ("현장", "(現場) the (actual) spot; the scene", "화재 현장에 많은 사람들이 있습니다."),
    ("화재", "(火災) a (big) fire; a fire disaster; a blaze; a fire breaks out (~나다)", "화재를 예방하려면 가스 사용 후에 가스 밸브를 꼭 확인하세요. 부주의로 화재가 발생하는 경우가 많아요."),
]
_CV_B = [
    ("건널목", "a crossing; “crossing neck”", "철도 건널목에서 아이들의 사고가 많이 납니다."),
    ("경위", "(經緯) details; particulars; circumstances", "이번 사건의 경위에 대해 내일까지 보고하세요."),
    ("과속", "(過速) speeding; “excessive speed”; to speed (~하다)", "교통사고 원인의 삼십 퍼센트는 과속운전입니다."),
    ("다리", "a bridge", "한강에는 큰 다리가 많습니다."),
    ("달리다", "to run", "버스에서 내리자마자 회사까지 달렸어요."),
    ("~대교", "(大橋) a big bridge", "한강 성수대교에서 교통사고가 나서 다른 길로 돌아가야 했어요."),
    ("도로", "(道路) a road; a street", "이 도로에는 횡단보도가 없어서 사고가 많이 발생합니다."),
    ("들이받다", "to run into; to bump into (physically); to ram", "자동차가 지나가던 행인을 들이받았다."),
    ("마주 오다", "to come toward each other", "버스가 마주 오던 차와 충돌해서 큰 사고가 났다."),
    ("멈추다", "to stop; to halt", "출혈이 멈추지 않으면 환자를 병원에 데리고 가세요."),
    ("속도", "(速度) speed; velocity", "커브 길에서는 자동차 속도를 줄여야 해요."),
    ("승합차", "(乘合車) a van; a wagon; a minibus; “riding-together vehicle”", "가족 여행을 가기 위해 승합차를 빌렸어요."),
    ("오토바이", "a motorcycle", "오토바이를 탈 때는 꼭 헬멧을 써야 해요."),
    ("위반", "(違反) a violation; a breach; to violate; to break (~하다)", "속도 위반을 하면 티켓을 받습니다. 조심하세요."),
    ("음주", "(飮酒) (alcohol) drinking", "음주 후 운동을 하는 것은 아주 위험해요."),
    ("익사", "(溺死) drowning; “drowning death”; to be drowned to death (~하다)", "이곳에서는 익사사고가 자주 발생하니 조심하시기 바랍니다."),
    ("전복", "(顚覆) overturned; flipped over; to be overturned (~되다)", "관광버스가 빗길에 미끄러지면서 전복되었어요."),
    ("접촉", "(接觸) touch; contact; connection; to touch; to make contact / to be connected (~하다/되다)", "어떤 피부병은 환자와의 접촉에 의해 걸릴 수 있습니다."),
    ("정면", "(正面) the front side; the front; “correct face”", "그 건물을 정면에서 보면 정말 멋있어요."),
    ("정지", "(停止) stop; halt; to stop; to halt (~하다)", "정지표지에서는 일단 정지해야 합니다."),
    ("중앙선", "(中央線) a median (i.e. on a road); “center line”", "택시가 중앙선을 넘어 마주 오던 트럭과 충돌했다."),
    ("지나(가)다", "to pass by; to go by; “pass and go”", "차가 빠른 속도로 지나갔어요."),
    ("차선", "(車線) a (traffic) lane; “car line”", "차선을 바꾸기 전에 먼저 신호를 주어야 한다."),
    ("추돌", "(追突) a rear-end collision; “pursue and hit”; to collide from behind (~하다)", "안개 속에서 과속으로 달리다가 앞차와 추돌했어요."),
    ("추월", "(追越) passing; “pursue and pass”; to pass (~하다)", "터널 안에서는 추월이 금지되어 있습니다."),
    ("충돌", "(衝突) a collision; a clash; to collide with (~하다)", "출근길에 오토바이와 충돌할 뻔했어요."),
    ("통제", "(統制) control; regulation; to control; to regulate / to be controlled; to be regulated (~하다/되다)", "서울시 경찰은 내일 스물네 시간 동안 광화문 근처의 교통을 통제한다. 공사로 인해 잠수교의 교통이 통제되고 있다."),
    ("파손", "(破損) damage (of a thing or structure); breakage; to damage / to be damaged (~시키다/되다)", "추돌 사고로 인해 차가 심하게 파손되었습니다."),
    ("화물차", "(貨物車) a cargo truck", "고속도로를 운전할 때는 화물차를 조심해야 합니다."),
]
_CV_C = [
    ("공포탄", "(空砲彈) blank ammunition", "이번 육군의 훈련기간 동안에는 공포탄만 사용될 것이라고 한다."),
    ("끝내", "finally; in the end", "오랫동안 앓던 병으로 그 친구는 끝내 숨지고 말았어요."),
    ("다루다 / 취급하다", "(取扱) to deal with; to handle", "총기를 다루는 군인들은 오발 사고가 나지 않도록 항상 조심해야 한다."),
    ("~덕분에 / 덕택에", "(德分 / 德澤) thanks to", "선생님 덕분에 한국어 실력이 많이 늘었어요."),
    ("뒤집히다", "to be turned over; to be capsized; to be reversed", "어선 두 척이 서로 충돌하면서 뒤집히는 사고가 발생했습니다."),
    ("몰다", "to drive (a vehicle)", "면허증 없이 트럭을 몰다가 사고를 냈다."),
    ("무너지다", "to collapse", "칠 층짜리 건물에서 화재가 발생해 건물이 무너지는 사고가 났다."),
    ("무단", "(無斷) without permission; without warning; without notice", "이 도로에서 무단 횡단을 하면 위험해요."),
    ("무사", "(無事) safety; “without an affair”; to be safe (and sound); to be unharmed; to be intact (~하다)", "대형 버스사고였지만 승객들은 다행히 모두 무사했습니다."),
    ("밝히다", "1. to reveal; to make something public; 2. to clarify; to bring (a matter) to light; “to make something clear”", "경찰은 이번 사고로 두 명이 사망했다고 밝혔습니다. 영산대학교는 다음 주부터 오 일간 신입생 오리엔테이션을 실시한다고 밝혔습니다."),
    ("보고", "(報告) a report; a briefing; to report / to be reported (~하다/되다)", "군인이 휴가 기간 중 사고가 나면 바로 부대에 보고해야 합니다. 올해 경찰에 보고된 음주운전 사고가 작년에 비해 오 퍼센트 감소되었다고 합니다."),
    ("사병", "(士兵) an enlisted man; a soldier; the ranks", "사병들이 완전무장을 하고 훈련을 받고 있어요."),
    ("사상자", "(死傷者) casualties; “dead and injured people”", "이번 교통사고로 십여 명의 사상자가 발생했다."),
    ("새벽", "daybreak; dawn", "어머니는 새벽에 일어나셔서 가족들의 아침 식사를 준비하십니다."),
    ("실탄", "(實彈) live ammunition; live round; “real ammunition”", "한 대학생이 화장실에서 실탄이 들어 있는 권총을 발견해 경찰에 신고했다."),
    ("야간", "(夜間) night; nighttime; “night interval”", "요즘에 회사에 일이 많아 야간에도 근무합니다."),
    ("어선", "(漁船) a fishing boat", "어선 두 척이 부딪치면서 화재가 발생했습니다."),
    ("~에 의하면", "according to", "조사에 의하면 작년 한 해 동안 교통사고 사망자의 수가 줄었다고 합니다."),
    ("이탈", "(離脫) breakaway; desertion; to break away; to desert (~하다)", "훈련 중에 혼자 이탈한 군인이 사고를 냈다."),
    ("조치", "(措置) a measure; an action; a step; to take a step; to take action (~하다)", "안전사고가 너무 자주 발생합니다. 안전조치를 마련해야 합니다."),
    ("즉시", "(卽時) right away; immediately", "사고를 당하면 즉시 일일구에 연락하십시오."),
    ("진술", "(陳述) statement; testimony; to state; to testify (~하다)", "이 사건은 목격자의 진술이 아주 중요합니다."),
    ("~척", "(隻) counter for ships or boats", "동해에서 어선 다섯 척이 침몰하는 사고가 발생했습니다."),
    ("총기오발", "(銃器誤發) misfiring a weapon", "이틀 전 발생한 해병대 부대 내 총기 오발 사고로 사병 두 명이 중상을 입었다."),
    ("추락", "(墜落) a fall; a drop; a crash; to fall; to drop; to crash (~하다)", "추락한 비행기에는 한국인 승객이 두 명 타고 있었습니다."),
    ("취하다", "(取) to take (an action / a measure)", "경찰이 이 문제에 대해 적극적인 태도를 취하고 있습니다."),
    ("(술) 취하다", "(醉) to get drunk; to be intoxicated", "야간에 운전할 때는 길에 술 취한 사람이 있는지 잘 살펴봐야 한다."),
    ("해(양)경(찰)", "(海(洋)警(察)) coast guard; “ocean police”", "어선에 화재가 발생해 해경이 긴급 진화했다."),
    ("해역", "(海域) an area or section of sea", "북한이 서해 북방한계선 인근 해역에서 야간 해상 사격훈련을 했습니다."),
    ("후송", "(後送) evacuation; sending back (to the rear); to send back / to be sent back (~하다/되다)", "의무병들이 부상자들을 후송하고 있습니다. 교통사고 부상자들이 병원으로 후송되었습니다."),
]
_CV_LOAN = [("오토바이", "a motorcycle", "오토바이를 탈 때는 꼭 헬멧을 써야 해요.")]
_CV_GR = [
    ("-(으)ㄹ 때 + markers", "time expressions when; whenever; since; until", "동작대교의 교통이 통제될 때마다 학교 가는 데 두 시간 걸려요."),
    ("-(으)ㄴ/는/을 것", "the thing(s) that; what", "사거리에 있는 한식집에서 화재가 난 것을 아셨어요?"),
    ("-(으)ㄴ 채(로)", "in the state of having done (something)", "저는 너무 피곤해서 신을 신은 채로 잠을 잤습니다."),
]
_CV_SINO = [("운전자", "(運轉者) a driver; an operator", "운동, 운행, 기운, 회전, 운전, 자전거, 환자, 목격자, 초보자"), ("야간", "(夜間) nighttime", "야근, 야경, 야식, 시간, 간식, 주야간"), ("인명", "(人命) human life", "노인, 인구, 살인, 수명, 명령, 생명")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_LOAN}
_EXTRA = {"골목(길)": "an alley", "죽다 / 사망하다 / 숨지다 / 돌아가시다": "to die; to pass away", "지나(가)다": "to pass by; to go by", "다루다 / 취급하다": "to deal with; to handle", "(술) 취하다": "to get drunk", "해(양)경(찰)": "coast guard", "~덕분에 / 덕택에": "thanks to", "~에 의하면": "according to",
          "추돌": "a rear-end collision", "붕괴": "a collapse", "탈선": "a derailment", "침몰": "sinking", "물놀이 사고": "a water-play accident", "탈북자": "a North Korean defector", "유조차": "an oil tanker truck", "용달차": "a small delivery truck", "승용차": "a passenger car", "택시": "a taxi", "버스": "a bus", "트럭": "a truck", "봉고차": "a minivan; “Bongo car”", "봉고": "a minivan",
          "한국인": "a Korean person", "미국인": "an American", "외국인": "a foreigner", "수명": "life; the span of life", "생명": "life; “living life”", "구명": "lifesaving; clemency; “saving one’s life”", "운명": "destiny; fate; “operating one’s life”", "명령": "an order",
          "운동": "motion; movement; exercise; “driving and moving”", "운반": "conveyance; transfer", "운송": "shipping; transport", "운영": "operation; management", "운하": "a canal; a waterway; “operating river”", "운행": "running (of transportation); revolution (of a celestial body); “operating and moving”", "자전거": "a bicycle; “self-rolling vehicle”", "전업": "change of employment; “turning jobs”", "전입": "moving-in; transference; “rolling in”", "전이": "change; transition; transfer; “rolling and moving”", "사망자": "the dead; the deceased; “dead person”", "중상자": "a severely wounded person", "경상자": "a lightly wounded person", "화자": "a speaker; “speaking person”", "시청자": "a TV viewer; the TV audience; “person who watches and listens”",
          "야간훈련": "night training", "야간비행": "a night flight", "야간수업": "a night class", "야경": "a night view", "야시장": "a night market", "야학": "night study; an evening class", "간격": "a space; an interval", "모녀간": "(in) mother-and-daughter relationship; between mother and daughter", "주간": "daytime; day", "야간전투": "a night battle", "야간경기": "a night game", "야간학교": "a night school", "야간열차": "a night train",
          "동사": "death from extreme cold", "질식사": "death from suffocation", "압사": "death from crushing", "추락사": "death from falling", "사망하다": "to die; to pass away", "화재경보": "a fire alarm", "화재 현장": "the scene of a fire"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_IN1 = [("한국인", "a Korean person"), ("미국인", "an American"), ("외국인", "a foreigner")]
_IN2 = [("수명", "life; the span of life"), ("생명", "life; “living life”"), ("구명", "lifesaving; clemency; “saving one’s life”"), ("운명", "destiny; fate; “operating one’s life”"), ("명령", "an order")]
_UN1 = [("운동", "motion; movement; exercise; “driving and moving”"), ("운반", "conveyance; transfer"), ("운송", "shipping; transport"), ("운영", "operation; management"), ("운하", "a canal; a waterway; “operating river”"), ("운행", "running (of transportation); revolution (of a celestial body); “operating and moving”")]
_UN2 = [("자전거", "a bicycle; “self-rolling vehicle”"), ("전업", "change of employment; “turning jobs”"), ("전입", "moving-in; transference; “rolling in”"), ("전이", "change; transition; transfer; “rolling and moving”")]
_UN3 = [("사망자", "the dead; the deceased; “dead person”"), ("탈북자", "a North Korean defector; “person who flees North”"), ("중상자", "a severely wounded person"), ("경상자", "a lightly wounded person"), ("화자", "a speaker; “speaking person”"), ("시청자", "a TV viewer; the TV audience; “person who watches and listens”")]
_YA1 = [("야간훈련", "night training"), ("야간비행", "a night flight"), ("야간수업", "a night class")]
_YA2 = [("야경", "a night view"), ("야시장", "a night market"), ("야학", "night study; an evening class")]
_YA3 = [("공간", "space; room; a gap; “empty space”"), ("간격", "a space; an interval"), ("부자간", "(in) father-and-son relationship; between father and son"), ("모녀간", "(in) mother-and-daughter relationship; between mother and daughter")]
_YAG = [("야간전투", "a night battle"), ("야간경기", "a night game"), ("야간학교", "a night school"), ("야간열차", "a night train")]
_SA = [("사망하다", "to die; to pass away"), ("동사", "death from extreme cold (凍死)"), ("익사", "death from drowning (溺死)"), ("질식사", "death from suffocation (窒息死)"), ("압사", "death from crushing (壓死)"), ("추락사", "death from falling (墜落死)")]

# ================================================================== L1: objectives and Sino-Korean
L1 = lesson(
    "Ch 37 · What the chapter teaches, 인명 (人命) · 운전자 (運轉者) · 야간 (夜間)",
    "사고 · 인명 · 생명 · 운전자 · 야간 · 야경 · 사망자 · 부자간",
    requires=[],
    cards=[
        card("What Chapter 37 teaches (사고)",
             "Chapter 37, “Accidents”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and provide basic information on fire, traffic, and military-related accidents; and ask about and summarize fire, traffic, and military-related accidents.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; an attributive form + 것 (the thing that; the things that; what); the conjunctive ending –(으)ㄴ 채(로); the conjunctive ending –(으)ㄹ 때까지 (until; to the time that); the conjunctive ending –(으)ㄹ 때마다 (whenever; every time that); the conjunctive ending –(으)ㄹ 때부터 (since; from the time that); and the Sino-Korean syllables within 인명 (人命), 운전자 (運轉者), and 야간 (夜間)."),
        card("Sino-Korean in use: 인명 (人命)",
             "This Sino-Korean word, which you frequently encounter in reports about human casualties, means human life. The first syllable 인 (人) means human or person, as you have seen in words such as 한국인, 미국인, and 외국인. The meanings of the second syllable 명 (命) are interesting. Its Chinese character originally meant king’s order. The character 命 is made up of 令 (king) and 口 (mouth). Thus it originally meant an order given through the king’s mouth. Because kings had power to determine one’s life or destiny through their royal order, the syllable evolved to mean life, destiny, order, as in 수명 (life; the span of life), 생명 (life; “living life”), 구명 (lifesaving; clemency; “saving one’s life”), 운명 (destiny; fate; “operating one’s life”), and 명령 (an order).",
             tables=[ktable(_IN1), ktable(_IN2)]),
        card("Sino-Korean in use: 운전자 (運轉者)",
             "This Sino-Korean word means a driver (of a vehicle or moving object). The first syllable 운 (運) means driving or operating, as in 운동 (motion; movement; exercise; “driving and moving”), 운반 (conveyance; transfer), 운송 (shipping; transport), 운영 (operation; management), 운하 (a canal; a waterway; “operating river”), and 운행 (running [of transportation]; revolution [of a celestial body]; “operating and moving”). The second syllable 전 (轉) means rolling or turning, as in 자전거 (a bicycle; a cycle; “self-rolling vehicle”), 전업 (change of employment; “turning jobs”), 전입 (moving-in; transference; “rolling in”), and 전이 (change; transition; transfer; “rolling and moving”). The last syllable 자 (者) means person or fellow, as in 사망자 (the dead; the deceased; “dead person”), 탈북자 (a North Korean defector; “person who flees North”), 중상자 (a severely wounded person), 경상자 (a lightly wounded person), 화자 (a speaker; “speaking person”), and 시청자 (a TV viewer; the TV audience; “person who watches and listens”). Thus the literal meaning of the word 운전자 is “person who operates and turns”, and the word refers to a vehicle operator or motorist.",
             tables=[ktable(_UN1), ktable(_UN2), ktable(_UN3)]),
        card("Sino-Korean in use: 야간 (夜間)",
             "This Sino-Korean word means nighttime or night, more specifically duration or period between sunset and sunrise, as in 야간훈련 (night training), 야간비행 (night flight), and 야간수업 (a night class). The first syllable 야 (夜) means night, as in 야경 (a night view), 야시장 (a night market), and 야학 (night study; an evening class). The second syllable 간 (間) means gap, room, or space (between two objects), as in 공간 (space; room; a gap; “empty space”) and 간격 (a space; an interval). As seen in Chapter 25, however, the same syllable means (in) relationship (between two entities) or between (two entities) when following a word denoting two entities, as in 부자간 ([in] father-and-son relationship; between father and son), 모녀간 ([in] mother-and-daughter relationship; between mother and daughter), etc. Thus the literal meaning of the word 야간 is “night gap” or “night space”, and the word refers to the nighttime from dusk to dawn when no sunlight is visible. The opposite of 야간 is 주간 (daytime; day).\n\n"
             "The book asks you to guess the meaning of 야간전투, 야간경기, 야간학교 and 야간열차 (my answers: a night battle; a night game; a night school; a night train).",
             tables=[ktable(_YA1), ktable(_YA2), ktable(_YA3), ktable(_YAG)]),
    ],
    exercises=uniq(
        _tr(_IN2 + _UN1 + _UN2 + _UN3 + _YA1 + _YA2 + _YA3 + _YAG, k=3)
        + [M("What does 인 (人) mean?", "human; person", ["life", "night", "driving"], "한국인."), M("What does 명 (命) mean?", "life; destiny; order", ["person", "night", "gap"], "생명."), M("What does 운 (運) mean?", "driving; operating", ["rolling", "night", "life"], "운동."), M("What does 전 (轉) mean?", "rolling; turning", ["driving", "night", "person"], "자전거."), M("What does 자 (者) mean?", "person; fellow", ["place", "night", "life"], "사망자."), M("What does 야 (夜) mean?", "night", ["day", "gap", "person"], "야경."), M("What does 간 (間) mean?", "gap; room; space; between", ["night", "person", "life"], "공간."), M("What is the literal meaning of 운전자?", "“person who operates and turns”", ["“human life”", "“night gap”", "“person who flees North”"], "운 + 전 + 자."), M("What is the literal meaning of 야간?", "“night gap” or “night space”", ["“human life”", "“person who operates and turns”", "“day space”"], "야 + 간."), M("What is the antonym of 야간?", "주간", ["야경", "야학", "생명"], "The book’s note."), M("What did the character 命 originally mean?", "an order given through the king’s mouth", ["a night", "a person", "a vehicle"], "The book’s note."),
           F("교통사고로 많은 ___ 피해가 있었다. (human life)", "인명", ["야간", "운전자"], "인명."), F("술을 마신 ___가 사고를 냈다. (driver)", "운전자", ["사망자", "목격자"], "운전자."), F("저는 ___수업을 듣고 있습니다. (night)", "야간", ["주간", "인명"], "야간."), F("서울의 ___이 아름답다. (night view)", "야경", ["야학", "야식"], "야경."),
           read_q("인명"), read_q("운전자"), read_q("야간"), read_q("야경"), read_q("사망자")]
    ),
)

# ================================================================== L2: Vocabulary Builder
_VBW = ["추돌", "총기", "전복", "누전", "폭발", "화재", "중앙선", "실탄", "진화", "위반", "소방차", "과속", "오발", "번지다"]
_VBC = [("Fire-related words", ["화재", "소방차", "누전", "진화", "폭발", "번지다"]), ("Traffic-related words", ["추돌", "전복", "중앙선", "과속", "위반"]), ("Gun-related words", ["총기", "실탄", "오발"])]
_VBP = [("추돌", "a rear-end collision"), ("총기", "firearms; guns"), ("전복", "overturned; flipped over"), ("누전", "a short circuit"), ("폭발", "explosion"), ("화재", "a (big) fire"), ("중앙선", "a median; center line"), ("실탄", "live ammunition"), ("진화", "putting out a fire"), ("위반", "a violation; a breach"), ("소방차", "a fire engine; a fire truck"), ("과속", "speeding"), ("오발", "a misfire; a shot fired by mistake"), ("번지다", "to spread")]
_XW = [("익사", "물에 빠져 숨졌습니다.", "1"), ("화재", "불이 났습니다.", "2"), ("진화", "소방차가 와서 불을 껐습니다.", "3"), ("충돌", "승용차와 트럭이 부딪혔습니다.", "4"), ("새벽", "아주 이른 오전 시간", "5"), ("총기", "여러 가지 종류의 총", "6"), ("위반", "운전할 때 교통 법을 지키지 않았습니다.", "7"), ("누전", "전기가 샌 것이 화재의 원인이 되었습니다.", "8"), ("오발", "총을 잘못 쏘았습니다.", "9"), ("어선", "물고기를 잡는 데 사용하는 배", "10")]
_KINDS = [("화재", "a fire"), ("충돌", "a collision"), ("추락", "a fall; a crash"), ("추돌", "a rear-end collision"), ("탈선", "a derailment"), ("폭발 사고", "an explosion accident"), ("붕괴 사고", "a collapse accident"), ("침몰", "sinking"), ("전복", "overturning; capsizing"), ("물놀이 사고", "a water-play accident")]
L2 = lesson(
    "Ch 37 · Vocabulary Builder: word groups, the structure of an accident report and clue words",
    "추돌 · 총기 · 전복 · 누전 · 폭발 · 화재 · 중앙선 · 실탄 · 진화 · 위반 · 소방차 · 과속 · 오발 · 번지다 · 사고의 종류",
    requires=[],
    cards=[
        card("새 단어: fourteen words and three categories",
             "The book gives fourteen core words (추돌, 총기, 전복, 누전, 폭발, 화재, 중앙선, 실탄, 진화, 위반, 소방차, 과속, 오발, 번지다). You skim them, circle the ones you do not know, write the English meaning, and then establish three categories and put the words in a table. My categories and meanings:",
             tables=[table(["Category (mine)", "Words"], [[n, ", ".join(ws)] for n, ws in _VBC], say=[1]), ktable(_VBP)]),
        card("Vocabulary Learning Strategy: understand the structure of an accident report",
             "In this chapter, you will learn about the structure of accident reports you may encounter. All accident reports share a similar structure that includes these factors in the following order: When (time); Where (place); Who did what (facts); Casualties or property damages; Cause.\n\n"
             "When: time is presented from the general to the specific. (Refer to the Cultural Notes section in Chapter 30, Topic Presentation B, to refresh your memory.) In an accident report, ~께/쯤/경 is often attached to time and indicates the approximate time of the accident (31일 오후 6시 10분쯤).\n\n"
             "Where: the place is also presented from the general to the specific. The house or street number is not often disclosed in an accident report (서울 강남구 역삼동 주택가에서).\n\n"
             "Who did what: in an accident report, a person’s identity is generally not fully disclosed. 모, which is similar to John Doe in English, is used to replace part or all of a person’s identity. In addition, 김 모 씨 is used to replace a name (e.g., Mr./Ms. Kim) because 씨 indicates generic male or female. Likewise, 양 is used to indicate an unmarried young girl (e.g., 이 모 양 replaces Miss Lee) and 군 is used to indicate an unmarried young boy (e.g., 박 모 군 replaces Mr. Park). Finally, in a written report, people’s ages are usually in parentheses. For example, 장 모 (32) 씨와 김 모 (45) 씨의 차량이 충돌하였습니다.\n\n"
             "Casualties and property damages: common key words for damages are 부상, 경상, 중상, 죽다, 다치다, 숨지다, 사망하다, 인명피해, and 재산피해 (두 차량의 운전자가 모두 중상을 입고 병원에서 치료를 받고 있습니다).\n\n"
             "Cause: the cause of the incident is generally reported last and listed as known, unknown, or under investigation. If the cause is known, the sentence often ends with 원인은 …으로 밝혀졌습니다 or …으로 드러났습니다 (Its cause is known as …). If police are still investigating, 경찰은 사고 원인을 조사하고 있습니다 (Police are investigating the cause) is generally used."),
        card("Activity 1: clue words (the grid is a picture, so the clues are answered here)",
             "The book gives ten clues, and you find the answer in a letter grid, circle it and write the clue number. The clues are the book’s; the answers are mine:",
             tables=[table(["No.", "Clue", "Answer (mine)"], [[c, a, b] for b, a, c in _XW], say=[1, 2])]),
        card("사고의 종류: kinds of accidents (the book shows pictures with these labels)", "The book’s picture labels (the meanings are mine):", tables=[ktable(_KINDS)]),
        card("Activities left out", "Activity 2 (listening to four descriptions and circling the word that best describes the situation: 진화/과속/이송/파손; 충돌/피해/총기/접촉; 전복/추락/해경/이탈; 조치/실탄/목격/무단), Activities 3 and 4 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 5 (Password, a clue-guessing team game) are audio, computer and game activities."),
    ],
    exercises=uniq(
        vocab_exercises(_VBP)
        + [M("Which word matches the clue “" + a[:24] + "”?", b, [x[0] for x in _XW if x[0] != b][:3], "My answer.") for b, a, c in _XW]
        + [M("What is the first item of an accident report?", "When (time)", ["Cause", "Casualties", "Who did what"], "The book’s order."), M("What is the last item of an accident report?", "Cause", ["When", "Where", "Casualties"], "The book’s order."), M("What does 모 do in 김 모 씨?", "Replaces part of a name, like John Doe", ["Means a mother", "Marks a place", "Marks an age"], "The book’s note."), M("What does 양 indicate in 이 모 양?", "An unmarried young girl", ["A young boy", "A married woman", "An old man"], "The book’s note."), M("What does 군 indicate in 박 모 군?", "An unmarried young boy", ["A young girl", "An old man", "A soldier"], "The book’s note."), M("What does ~쯤/경/께 after a time mean?", "Approximately", ["Exactly", "Until", "After"], "The book’s note."), M("How does a report end if the cause is under investigation?", "경찰은 사고 원인을 조사하고 있습니다", ["원인은 밝혀졌습니다", "원인은 없습니다", "사고는 없었습니다"], "The book’s note."),
           F("소방차가 와서 불을 껐습니다. = ___했습니다. (put out)", "진화", ["충돌", "폭발"], "진화."), F("총을 잘못 쏘았습니다. = ___ 사고. (misfire)", "오발", ["전복", "추돌"], "오발."), F("전기가 샌 것이 화재의 원인이 되었습니다. = ___로 인한 화재. (short circuit)", "누전", ["과속", "위반"], "누전."), F("운전할 때 교통 법을 지키지 않았습니다. = 교통법 ___. (violation)", "위반", ["과속", "누전"], "위반."), F("불이 위층으로 ___고 있다. (spreading)", "번지", ["타", "멈추"], "번지다."),
           read_q("추돌"), read_q("총기"), read_q("누전"), read_q("중앙선"), read_q("소방차")]
    ),
)

# ================================================================== L3: Topic A
_A_TXT = [
    ("어젯밤 아홉 시, 인천시에 있는 사 층짜리 상가에서 일어난 화재로 두 명이 숨지고 세 명이 중상을 입었습니다.", "A fire that broke out last night at nine o’clock in a four-story shopping building in Incheon left two dead and three seriously injured."),
    ("화재 현장에 김현성 기자가 나가 있습니다.", "Reporter Kim Hyunseong is at the scene of the fire."),
    ("김현성 기자.", "Reporter Kim Hyunseong."),
    ("네, 저는 지금 화재 현장에 나와 있습니다.", "Yes, I am now at the scene of the fire."),
    ("자세한 피해 소식 알려주시죠.", "Please tell us the details of the damage."),
    ("어젯밤 아홉 시쯤 인천시에 있는 한 상가에서 불이 났습니다.", "At about nine o’clock last night, a fire broke out in a shopping building in Incheon."),
    ("신고를 받고 소방차들이 긴급 출동했습니다.", "After receiving the report, fire engines were dispatched urgently."),
    ("하지만 상가가 좁은 골목길에 있어 소방차들이 들어가기가 쉽지 않아 진화에 어려움을 겪었습니다.", "But because the shopping building is in a narrow alley, it was not easy for the fire engines to get in, so they had difficulty putting out the fire."),
    ("이 화재로 두 명이 숨지고 세 명이 중상을 입는 인명피해가 발생했습니다.", "Because of this fire, human casualties occurred: two died and three were seriously injured."),
    ("또 건물 전체가 다 타면서 수억 원의 재산 피해가 났습니다.", "Also, as the whole building burned down, hundreds of millions of won in property damage occurred."),
    ("목격자들은 일 층 피시 방에서 큰 폭발 소리와 함께 불이 위층으로 번졌다고 말했습니다.", "Eyewitnesses said that with a loud explosion sound from the PC room on the first floor, the fire spread to the upper floors."),
    ("소방 당국은 전기 누전으로 불이 시작됐을 가능성이 크다고 보고 정확한 화재 원인을 조사하고 있습니다.", "The fire authorities, seeing a high possibility that the fire started from an electrical short circuit, are investigating the exact cause of the fire."),
]
_A_WORDS = ["경상", "긴급", "놀라다", "누전", "당국", "목격", "목격자", "발견", "발생", "번지다", "부상", "부주의", "불", "소방차", "소식", "이송", "인명", "장난", "재산", "전체", "중상", "진화", "타다", "태우다", "폭발", "피해", "현장", "화재"]
_EEI1 = [("이십육 일 오전 영 시 오십일 분경 충남 당진군 신평면 거산리에 있는 한 가구 공장에서 불이 났다.", "At about 12:51 a.m. on the 26th, a fire broke out at a furniture factory in Geosan-ri, Sinpyeong-myeon, Dangjin-gun, Chungnam."), ("공장 일 층에서 시작된 불은 삼 층 직원 기숙사까지 번지면서 기숙사에서 잠자던 공장 직원 세 명이 중경상을 입었다.", "The fire that started on the first floor of the factory spread up to the third-floor staff dormitory, and three factory employees who were sleeping in the dormitory suffered serious and minor injuries."), ("이들은 일일구 구조대에 의해 가까운 병원으로 이송되어 치료 중이다.", "They were transferred to a nearby hospital by the 119 rescue team and are being treated."), ("화재 현장에는 소방차 삼십여 대, 소방관 백여 명이 출동했다.", "About thirty fire engines and about a hundred firefighters were dispatched to the fire scene."), ("불은 여섯 시간 동안 기계와 제품 등을 태우고 오전 두 시 십 분쯤에 진화됐다.", "The fire burned machines and products for six hours and was put out at about 2:10 a.m."), ("이 불로 소방 당국 추산 삼억 오천만 원 정도의 재산 피해가 발생했다.", "Because of this fire, property damage of about 350 million won, by the fire authorities’ estimate, occurred."), ("경찰은 공장에 있던 가스통이 폭발한 것을 화재 원인으로 보고 있다.", "The police see the explosion of a gas canister that was in the factory as the cause of the fire."), ("한편, 경찰은 직원들의 말을 토대로 정확한 화재 원인을 조사 중이다.", "Meanwhile, the police are investigating the exact cause of the fire based on the employees’ statements.")]
_CAT = [("대전의 주상복합 아파트에서 고양이가 전기레인지 전원을 켜 발생한 것으로 추정되는 불이 났다.", "A fire presumed to have started when a cat turned on the power of an electric range broke out in a residential-commercial apartment building in Daejeon."), ("이십 일 영 시 사십육 분께 대전 유성구 한 주상복합 아파트 오 층 주방에서 불이 났다.", "At about 12:46 a.m. on the 20th, a fire broke out in the kitchen on the fifth floor of a residential-commercial apartment building in Yuseong-gu, Daejeon."), ("일일구 소방대원이 출동해 금방 불을 끄면서 내부 삼 제곱미터와 전기레인지 일부만 타 백이십일만 원 정도의 재산 피해가 발생했다.", "The 119 firefighters were dispatched and put out the fire quickly, so only three square meters of the interior and part of the electric range burned, causing about 1,210,000 won of property damage."), ("소방 당국은 집 안에 사람이 없이 고양이 한 마리만 있었던 데다 전기레인지 주변에서 불이 시작된 것으로 보이는 점 등을 토대로 고양이가 전기레인지 스위치를 켜 불이 난 것으로 보고 있다.", "The fire authorities see the fire as caused by the cat turning on the electric range switch, based on the fact that there was no one in the house and only one cat, and that the fire appears to have started around the electric range."), ("소방 당국 관계자는 집주인이 외출한 사이 고양이가 전기레인지에 올라가 스위치를 켠 것으로 추정하고 자세한 화재 원인을 조사하고 있다고 말했다.", "An official of the fire authorities said they presume that while the owner was out the cat climbed onto the electric range and turned on the switch, and that they are investigating the detailed cause of the fire.")]
L3 = lesson(
    "Ch 37 · Topic A: A fire broke out in a commercial building last night (어젯밤 상가에서 화재가 났습니다)",
    "어젯밤 상가에서 화재가 났습니다 · 화재 현장 · 소방차 긴급 출동 · 인명피해 · 재산 피해 · 누전 · 가구 공장 화재 · 고양이",
    requires=[],
    cards=[
        card("Topic A: A fire broke out in a commercial building last night (어젯밤 상가에서 화재가 났습니다)",
             "The following news report is about a fire that occurred at a commercial building. (The English is mine; the book gives none; the times are spelled out in Hangul, “PC” is read 피시, and the anchor and reporter labels are 앵커 and 기자.)",
             examples=passage(_A_TXT)),
        card("Footnote: ~(으)로", "~(으)로 used in this context (이 화재로) means because of or due to."),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 누전(되다), 목격(하다/되다), 발견(하다/되다), 발생(하다), 부상(입다/당하다), 이송(하다/되다), 장난(하다/치다), 중상(입다), 진화(하다/되다), 폭발(하다) and 화재(나다) take the forms in parentheses.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Follow-up 2 (Reading): a news article about a fire and its EEIs",
             "Read the following news article about a fire and identify the EEIs (Essential Elements of Information). In English, fill in the table with the EEIs (the book glosses 공장: a factory; a plant). The article is the book’s; the numbers are spelled out in Hangul; the English is mine.",
             examples=passage(_EEI1)),
        card("The EEI table (mine)", "The book’s table asks for time and place, the meaning of the numbers 6, 30 and 100, the consequence of the fire (casualties and/or property damage) and the cause of the fire. My answers:",
             tables=[table(["Item", "Answer (mine)"], [["Time and place", "About 12:51 a.m. on the 26th; a furniture factory in Geosan-ri, Sinpyeong-myeon, Dangjin-gun, Chungnam"], ["6", "The fire burned machines and products for six hours"], ["30", "About thirty fire engines were dispatched"], ["100", "About a hundred firefighters were dispatched"], ["Consequence", "Three dormitory employees seriously or lightly injured; about 350 million won of property damage"], ["Cause", "Probably the explosion of a gas canister in the factory; the police are investigating based on employees’ statements"]])]),
        card("Activity 2 (Reading and speaking): a news article about a cat and a fire",
             "Read the news article about a fire and identify the EEIs; the book glosses 전원: power and 추정(하다/되다): presumption. The headline, “내가 불냈냐옹…” (a play on a cat’s meow, “Did I start the fire, meow?”), is left out here. The article is the book’s with the numbers spelled out (3m² → 삼 제곱미터); the English is mine.",
             examples=passage(_CAT)),
        card("The EEIs and tips (mine)", "The book’s table has the rows time and date, place, casualties and/or property damage, probable cause of the fire and other information; and then asks you and a partner to compile two or three ways for pet owners to prevent their pets from causing house fires. My answers:",
             tables=[table(["Item", "Answer (mine)"], [["Time and date", "About 12:46 a.m. on the 20th"], ["Place", "A fifth-floor kitchen of a residential-commercial apartment building in Yuseong-gu, Daejeon"], ["Casualties/property damage", "No casualties mentioned; three square meters of the interior and part of the electric range burned; about 1,210,000 won of damage"], ["Probable cause", "The cat climbed onto the electric range and switched it on while the owner was out"], ["Other information", "119 firefighters put the fire out quickly; no one was home but one cat"], ["Tips for pet owners", "Cut the power or cover the switches of a stove when you go out; keep cats out of the kitchen; use a stove with a safety lock"]])]),
        card("Activities left out", "Follow-up 1 (listening to three YTN audio clips about different accidents and watching the video clips; the book gives 담배꽁초: a cigarette butt and 추산: estimate), Activity 1 (Two-in-One Vocabulary Review, SMART Board), Activity 3 (a news report, a firefighter’s journal and an eyewitness testimony about one fire, in groups of three) and the Topic Presentation A study steps (SMART Board and a class notebook) are audio, video, computer and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT + _EEI1 + _CAT, k=3)
        + [M("Where did the fire in Topic A break out?", "A four-story commercial building in Incheon", ["A house in Seoul", "A factory in Busan", "A school"], "인천시에 있는 사 층짜리 상가."), M("How many people died in the fire?", "Two", ["Three", "Five", "None"], "두 명이 숨지고."), M("How many were seriously injured?", "Three", ["Two", "Five", "None"], "세 명이 중상."), M("Why was it hard to put out the fire?", "The building was in a narrow alley", ["No water", "No fire engines", "It rained"], "좁은 골목길."), M("Where did the fire spread from?", "The PC room on the first floor", ["The roof", "The kitchen", "A car"], "일 층 피시 방."), M("What do the authorities think caused it?", "An electrical short circuit", ["Arson", "A gas leak", "A cigarette"], "전기 누전."), M("What probably caused the furniture factory fire?", "A gas canister explosion", ["A short circuit", "A cigarette", "Arson"], "가스통이 폭발."), M("What probably caused the apartment fire?", "A cat turned on the electric range", ["A candle", "A cigarette", "A short circuit"], "고양이가 전기레인지 스위치를 켜."),
           F("화재 ___에 김현성 기자가 나가 있습니다. (scene)", "현장", ["소식", "당국"], "현장."), F("신고를 받고 ___들이 긴급 출동했습니다. (fire engines)", "소방차", ["화물차", "승합차"], "소방차."), F("이 화재로 두 명이 숨지고 세 명이 중상을 입는 ___가 발생했습니다. (human casualties)", "인명피해", ["재산피해", "부주의"], "인명피해."), F("목격자들은 큰 ___ 소리와 함께 불이 번졌다고 말했습니다. (explosion)", "폭발", ["진화", "누전"], "폭발."), F("소방 ___은 전기 누전으로 불이 시작됐을 가능성이 크다고 보고 있다. (authorities)", "당국", ["현장", "소식"], "당국."),
           read_q("어젯밤 상가에서 화재가 났습니다"), read_q("소방차들이 긴급 출동했습니다"), read_q("인명피해가 발생했습니다"), read_q("건물 전체가 다 타면서 재산 피해가 났습니다"), read_q("정확한 화재 원인을 조사하고 있습니다")]
    ),
)

# ================================================================== L4: Topic B
_B_TXT = [
    ("교통사고 뉴스입니다.", "This is the traffic accident news."),
    ("오늘 오후 두 시쯤 올림픽대교에서 승합차와 버스가 정면 충돌하는 사고가 발생했습니다.", "At about two o’clock this afternoon, an accident occurred on the Olympic Bridge in which a van and a bus collided head-on."),
    ("승합차 운전자 이 모 씨가 음주 상태에서 중앙선을 넘어 마주 오던 버스를 들이받았습니다.", "The van driver, a Mr. Lee, crossed the center line while drunk and rammed into a bus coming toward him."),
    ("또 뒤에서 오던 차들은 앞에 차량이 사고가 난 것을 보고 피하려다 추돌사고를 내기도 했습니다.", "Also, cars coming from behind saw the vehicle ahead had an accident and, trying to avoid it, caused rear-end collisions."),
    ("이 사고로 승합차가 전복되면서 운전자 이 씨가 중상을 입었고, 버스 운전자와 승객 등 십여 명이 중경상을 입었습니다.", "In this accident the van overturned and the driver Mr. Lee was seriously injured, and about ten people, including the bus driver and passengers, suffered serious and minor injuries."),
    ("사고 후 올림픽대교는 약 한 시간 동안 통제되었습니다.", "After the accident the Olympic Bridge was closed for about an hour."),
    ("경찰은 승합차 운전자가 술을 마신 채 일 차선에서 과속으로 달리다가 사고를 낸 것으로 보고 정확한 사고 경위를 조사하고 있습니다.", "The police see the van driver as having caused the accident by speeding in the first lane while drunk, and are investigating the exact circumstances of the accident."),
]
_B_WORDS = ["건널목", "경위", "과속", "다리", "달리다", "도로", "들이받다", "멈추다", "속도", "승합차", "오토바이", "위반", "음주", "익사", "전복", "접촉", "정면", "정지", "중앙선", "차선", "추돌", "추월", "충돌", "통제", "파손", "화물차"]
_VEH = [("오토바이", "a motorcycle"), ("승용차", "a passenger car"), ("택시", "a taxi"), ("버스", "a bus"), ("승합차", "a van; a minibus (봉고차)"), ("용달차", "a small delivery truck"), ("화물차", "a freight truck (트럭)"), ("유조차", "an oil tanker truck")]
_TRK = [("하천에 전복된 트럭 속 부부, 지나가던 시민이 구조", "Couple in a truck overturned in a stream, rescued by a passing citizen"), ("충남 홍성경찰서에 따르면 지난 오 일 홍성군에서 일 톤 트럭이 가드레일을 들이받고 도로 옆 사 미터에서 오 미터 아래 하천으로 추락했다.", "According to the Hongseong Police Station in Chungnam, on the 5th a 1-ton truck rammed into a guardrail in Hongseong County and fell into a stream four to five meters below the roadside."), ("차 안에는 칠십 대 에이 씨 부부가 타고 있었다.", "The couple, Mr./Ms. A and spouse, in their seventies, were in the car."), ("일 점 사 미터 깊이 하천에 빠져 전복된 차 안으로 물이 금방 차올랐다.", "The car fell into the stream 1.4 meters deep and overturned, and water quickly filled the inside of the car."), ("마침 맞은편에서 차를 몰고 지나던 이 모 씨, 쉰여섯 살이 사고를 목격했다.", "Just then, Mr. Lee, 56, who was passing by driving from the opposite side, witnessed the accident."), ("이 씨는 곧바로 일일구에 구조요청을 한 뒤 물속으로 뛰어들어 차문을 열고 익사할 뻔한 에이 씨 부부를 구조했다.", "Mr. Lee immediately called 119 for rescue, then jumped into the water, opened the car door and rescued the couple, who were nearly drowned."), ("병원 치료를 받은 부부는 무사한 것으로 전해졌다.", "The couple, who received hospital treatment, were reported to be safe."), ("경찰이 현장에서 신원을 알려달라고 했지만, 이 씨는 누구라도 그랬을 것이라며 신분을 밝히지 않고 자리를 떠났다.", "The police asked him at the scene to tell them his identity, but Mr. Lee, saying “anyone would have done so”, left without revealing his identity.")]
_BS = [("칠 월 삼십일 일 오후 다섯 시 십육 분경 부산 해운대문화회관 사거리에서 김 모 씨, 쉰세 살이 몰던 푸조 차량이 신호를 위반한 채 시속 백 킬로미터가 넘는 속도로 달리다 횡단보도를 건너던 보행자들을 친 뒤 차량을 들이받는 칠중 추돌사고를 냈다.", "At about 5:16 p.m. on July 31, at the Haeundae Cultural Center intersection in Busan, a Peugeot driven by Mr. Kim, 53, ran a signal at over 100 km/h, hit pedestrians crossing the crosswalk and then rammed into vehicles, causing a seven-vehicle pile-up."), ("이 교통사고로 인해 홍 모 씨, 마흔두 살 여자와 아들 하 모 군, 열여덟 살, 김 모 군, 열다섯 살 등 세 명이 숨지고 열네 명이 부상했다.", "Because of this traffic accident, three people died, including Ms. Hong, 42, and her son Mr. Ha, 18, and Mr. Kim, 15, and fourteen people were injured."), ("사고 현장을 목격했다는 에이 씨는 갑자기 폭발하는 것 같은 소리가 계속 났다고 말했다.", "Mr./Ms. A, who said he/she witnessed the accident scene, said that a sound like a sudden explosion kept going on."), ("브레이크 소리는 들리지 않았고 쾅쾅쾅쾅 하는 소리만 잇달아 났다.", "No brake sound was heard, only the sound of “bang bang bang bang” one after another."), ("차량 서너 대가 파손됐다며 당시 상황을 설명했다.", "He/she described the situation at the time, saying three or four vehicles were damaged."), ("에이 씨는 또 자전거를 타고 가다 사고를 당한 부상자에 대해 거의 삼십 미터를 날아갔고 자전거는 휴지가 됐다고 전했다.", "Mr./Ms. A also said of an injured person who was riding a bicycle when the accident happened that the person flew almost thirty meters and the bicycle turned into tissue paper."), ("한편 경찰에 따르면 사고를 낸 김 씨에 대해 음주 측정을 한 결과 음성으로 나왔다.", "Meanwhile, according to the police, the result of an alcohol test on Mr. Kim, who caused the accident, came out negative."), ("김 씨는 사고 당일 평소 먹던 뇌 질환 약을 먹지 않았다면서 왜 사고가 났는지 모르겠다고 말한 것으로 전해졌다.", "It was reported that Mr. Kim said he had not taken the brain-disease medicine he usually took on the day of the accident and that he did not know why the accident happened.")]
L4 = lesson(
    "Ch 37 · Topic B: A passenger car overturned on the Olympic Bridge (올림픽대교에서 승용차가 전복됐습니다)",
    "올림픽대교에서 승용차가 전복됐습니다 · 음주 · 중앙선 · 정면 충돌 · 추돌사고 · 차량 종류 · 한강의 다리 · 하천에 전복된 트럭",
    requires=[],
    cards=[
        card("Topic B: A passenger car overturned on the Olympic Bridge (올림픽대교에서 승용차가 전복됐습니다)",
             "The following news report is about a traffic accident on the Olympic Bridge. (The English is mine; the book gives none; the numbers are spelled out in Hangul. The title says 승용차 but the report says 승합차, a van.)",
             examples=passage(_B_TXT)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); 과속(하다), 위반(하다), 익사(하다), 전복(되다), 접촉(하다/되다), 정지(하다), 추돌(하다), 추월(하다), 충돌(하다), 통제(하다/되다) and 파손(되다/시키다) take the forms in parentheses. The book also lists 마주 오다, ~대교, 지나(가)다 and –(으)ㄴ/는/을 것, –(으)ㄴ 채(로) (see the grammar).",
             tables=[ktable(_rows(_B_WORDS)), table(["Word", "Meaning"], [["마주 오다", "to come toward each other"], ["~대교", "a big bridge"], ["지나(가)다", "to pass by; to go by"]], say=[0])]),
        card("한국어에는: 1. vehicle types",
             "In Korea, a motorcycle is called 오토바이, which comes from auto(matic) and bi(cycle). 승합차 refers to a (mini)van or minibus. A minivan is often called 봉고차, which literally means “Bongo car”. Bongo was the brand name of the first minivan manufactured by KIA decades ago. Today 승합차 or 미니밴 is more used, and the term 봉고차 is slowly disappearing. 용달차 is a small-sized commercial truck mostly used for deliveries or moving. 화물차 is a freight truck and 유조차 is an oil tanker (i.e. truck). The vehicles you can commonly see on Korean streets:",
             tables=[ktable(_VEH)]),
        card("한국어에는: 2. –아/어가다 and –아/어오다",
             "Recall –아/어가다 and –아/어오다 from the Chapter 8 Vocabulary Builder. These phrases are used to indicate an action with a targeted location (from one place to another). For example, to express run to (the gym), we say (체육관에) 달려가다 or (체육관에) 달려오다, which literally means “run and go (to the gym)” or “run and come (to the gym)”. The verb preceding –아가다 or –어가다 usually indicates a mode of movement or direction."),
        card("한국어에는: 3. ~사 (死)",
             "The Sino-Korean syllable 사 (死) means death or dying, as in 사망하다 (to die; to pass away). When the syllable is placed at the end of Sino-based words, it indicates death (caused by something); for example, 동사 (凍死) means death from extreme cold; 익사 (溺死) means death from drowning; 질식사 (窒息死) means death from suffocation; 압사 (壓死) means death from crushing; 추락사 (墜落死) means death from falling.",
             tables=[ktable(_SA)]),
        card("한국에서는: bridges over the Han River",
             "The Han River is a major river in Korea and runs through the city of Seoul. As of 2021 there are 31 bridges crossing the Han River. The bridges link various districts of Seoul, and usually the name of the bridge comes from the area or the district connected by the bridge. The name of a bridge ends in either ~교 or ~대교 and literally means “a bridge” and “a great bridge”, respectively. Korea’s traffic patrol broadcasting provides information about traffic over each bridge. When a traffic accident occurs on a particular bridge, you will often hear ~대교를 통제하고 있습니다 (~ bridge is restricted) and ~대교로 우회하시기 바랍니다 (Please detour to ~ bridge). 잠수교, which literally means “a bridge under the water”, was designed to sink during floods. Thus, you will often hear traffic broadcasts reporting that 잠수교 is restricted because of flooding."),
        card("Follow-up 2 (Reading): a newspaper article about an accident",
             "The following newspaper article is about an accident. The book asks you to read it and answer in English in a table (EEI): when and where (the first part is done: “On the 5th in Hongseong County”); vehicle(s) involved; how the accident occurred; witness’s response to the accident; additional details or actions mentioned about the witness. The book glosses 하천: stream; 추락하다: to fall; to crash; 신원: identity. The article is the book’s with numbers spelled out and quotation marks dropped (the person’s age and the letter A are spelled out); the English is mine.",
             examples=passage(_TRK)),
        card("The EEI table (mine)", "The book leaves the table blank apart from the first line; my answers:",
             tables=[table(["EEI", "Answer (mine)"], [["When and where", "On the 5th in Hongseong County"], ["Vehicle(s) involved", "A 1-ton truck"], ["How the accident occurred", "The truck rammed into a guardrail and fell into a stream 4–5 m below the road and overturned in water 1.4 m deep"], ["Witness’s response", "Called 119 at once, jumped into the water, opened the car door and rescued the couple"], ["Additional details about the witness", "A 56-year-old passing by in the opposite lane; he refused to give his identity to the police, saying anyone would have done the same, and left"]])]),
        card("Activity 2 (Reading): a newspaper article about a traffic accident",
             "The following newspaper article is about a traffic accident; the book glosses 음성: negative; 잇달아: one after another; 뇌: brain. It asks you to fill in a table in English: time and place; how the accident occurred; consequence; eyewitness’s description; details about the driver. The article is the book’s with the numbers, the date and the ages spelled out; the English is mine. (This is a news report of a fatal accident.)",
             examples=passage(_BS)),
        card("The table filled in (mine)", "The book leaves the table blank; my answers:",
             tables=[table(["Information", "Answer (mine)"], [["Time and place", "About 5:16 p.m. on July 31, at the Haeundae Cultural Center intersection, Busan"], ["How the accident occurred", "A car driven by Mr. Kim, 53, ran a red light at over 100 km/h, hit pedestrians on the crosswalk and then rammed into other vehicles (a seven-vehicle pile-up)"], ["Consequence", "Three dead, fourteen injured"], ["Eyewitness’s description", "Explosion-like noises one after another, no brake sound, three or four cars damaged; a cyclist flew almost thirty meters"], ["Driver", "The alcohol test was negative; he said he had not taken his usual brain-disease medicine and did not know why the accident happened"]])]),
        card("Activities left out", "Follow-up 1 (listening to an eyewitness statement and filling in how the accident occurred, injuries, when and where and the possible cause), Activity 1 (Today’s Word Master, SMART Board), Activity 3 (writing your own news report from a word list and watching a KBS report; the word list: 새벽, 승용차, 속도, 빠르다, 차선, 왔다 갔다 하다, 정지 신호, 멈추다, 앞차, 추월하다, 신호등, 무시하다, 건널목, 중학생, 들이받다, 피해자, 숨지다, 운전자, 술을 마시다, 면허 정지; 새벽: dawn; 무시하다: to ignore; to neglect; 피해자: victim), Activity 4 (교통사고 보고하기, searching the websites of Yonhap News and YTN for 음주운전 사고 or 충돌, 추돌 사고 and presenting an article), the website list (한강의 다리) and the Topic Presentation B study steps are audio, video, internet and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT + _TRK[1:] + _BS[:6], k=3)
        + [M("Where did the accident in Topic B happen?", "On the Olympic Bridge", ["On a highway", "In a tunnel", "At a crossing"], "올림픽대교."), M("What collided?", "A van and a bus", ["Two buses", "A car and a train", "Two vans"], "승합차와 버스."), M("Why did the van hit the bus?", "The driver was drunk and crossed the center line", ["The bus was speeding", "The road was icy", "A tire burst"], "음주 상태에서 중앙선을 넘어."), M("How long was the bridge closed?", "About an hour", ["All day", "Ten minutes", "Two hours"], "약 한 시간."), M("What is 봉고차?", "A minivan, named after a KIA brand", ["A taxi", "A freight truck", "An oil tanker"], "The book’s note."), M("What does 익사 mean?", "death from drowning", ["death from falling", "death from cold", "death from crushing"], "The book’s note."), M("What is 잠수교?", "A bridge designed to sink during floods", ["A tunnel", "A ferry", "A railway"], "The book’s note."), M("What did the passing driver do in the stream accident?", "Called 119 and rescued the couple", ["Drove away", "Called a taxi", "Took photos"], "구조했다."),
           F("승합차가 ___을 넘어 마주 오던 버스를 들이받았습니다. (center line)", "중앙선", ["차선", "건널목"], "중앙선."), F("이 사고로 승합차가 ___되면서 운전자가 중상을 입었습니다. (overturned)", "전복", ["추돌", "충돌"], "전복."), F("뒤에서 오던 차들이 ___사고를 내기도 했습니다. (rear-end)", "추돌", ["충돌", "전복"], "추돌."), F("올림픽대교는 약 한 시간 동안 ___되었습니다. (restricted)", "통제", ["정지", "추월"], "통제."), F("경찰은 정확한 사고 ___를 조사하고 있습니다. (circumstances)", "경위", ["속도", "도로"], "경위."),
           read_q("올림픽대교에서 승용차가 전복됐습니다"), read_q("승합차와 버스가 정면 충돌하는 사고가 발생했습니다"), read_q("중앙선을 넘어 마주 오던 버스를 들이받았습니다"), read_q("올림픽대교는 약 한 시간 동안 통제되었습니다"), read_q("정확한 사고 경위를 조사하고 있습니다")]
    ),
)

# ================================================================== L5: Grammar A: attributive + 것
_GA1 = [("한국말을 배우다", "to learn Korean"), ("한국말을 배우는 학생", "a student who learns Korean"), ("한국말을 배운 학생", "a student who (has) learned Korean"), ("한국말을 배울 학생", "a student who will learn Korean")]
_GA2 = [("내가 매일 먹는 것", "the thing (that) I eat every day / what I eat every day"), ("내가 어제 먹은 것", "the thing (that) I ate yesterday / what I ate yesterday"), ("내가 먹을 것", "the thing (that) I will eat tomorrow / what I will eat tomorrow")]
_GA3 = [("내가 매일 먹는 것은 한국음식입니다.", "What I eat every day is Korean food. (subject)"), ("내가 매일 먹는 것을 먹지 마세요.", "Please don’t eat what I eat every day. (object)")]
_GA4 = [("한국사람들이 좋아하는 것은 축구입니다.", "Soccer is what Koreans like."), ("내가 한국식당에서 먹은 것의 이름이 뭐죠?", "What is the name of what I ate at the Korean restaurant?"), ("어제 배운 것을 종이에 적어 보세요.", "Please write down what you learned yesterday.")]
_GAM = [("동생이 꽃을 좋아해요.", "My younger sibling likes flowers."), ("동생이 좋아하는 것은 꽃이에요.", "What my younger sibling likes is flowers.")]
_GAQ = [("보는 것이에요?", "Is it something you look at?"), ("움직이는 것이에요?", "Is it something that moves?")]
_GAMINE = [("제가 어제 본 것은 영화였어요.", "What I saw yesterday was a movie."), ("저는 친구가 준 것을 먹었어요.", "I ate what my friend gave me."), ("내일 할 것을 지금 준비해요.", "I’m preparing now what I will do tomorrow.")]
L5 = lesson(
    "Ch 37 · Grammar A: expressing “the thing(s) that” or “what”, an attributive form + 것",
    "-는 것 · -(으)ㄴ 것 · -(으)ㄹ 것 · 내가 매일 먹는 것 · 어제 배운 것 · 좋아하는 것은",
    requires=[],
    cards=[
        card("The attributive form",
             "Recall that in Korean we use an attributive form of a verb to turn the verb or verb phrase into an adjective. For example (the English is the book’s):",
             tables=[ktable(_GA1)]),
        card("Note", "Note that 배우는, 배운, and 배울 are the attributive forms of the verb 배우다. These attributive forms are adjectives modifying the noun (학생) that follows."),
        card("The thing(s) that … or what …", "Thus, we can express the thing(s) that … or what … by using an attributive form of a verb + 것. For example (the English is the book’s):", tables=[ktable(_GA2)]),
        card("As a subject, an object or a complement", "These phrases can then be used as a subject, an object, or a complement in a sentence. For example (the English is the book’s):", examples=passage(_GA3)),
        card("Do not confuse it with the gerund",
             "DO NOT confuse the attributive form + –는 것 in 내가 매일 먹는 것 (what I eat every day/the thing I eat every day) with the gerund –는 것 in 먹는 것 (eating) and 마시는 것 (drinking)."),
        card("Expressing “the thing(s) that” or “what”", "attributive form of a verb + 것. More examples (the English is the book’s):", examples=passage(_GA4)),
        card("Follow-up 1 (Reading, speaking and listening): the model", "In pairs, Student A studies List A and Student B studies List B; one partner reads a sentence and the other changes it to a sentence using –는/(으)ㄴ/(으)ㄹ 것. The book’s model (the English is mine):", examples=dlg([("A", _GAM[0][0], _GAM[0][1]), ("B", _GAM[1][0], _GAM[1][1])])),
        card("Follow-up 3 (Listening and speaking): twenty questions", "Sit in a circle. The teacher picks a word from a set of cards, and students ask up to ten yes/no questions using –는/(으)ㄴ/(으)ㄹ 것 to identify the word. The book’s model (the English is mine):", examples=dlg([("학생", _GAQ[0][0], _GAQ[0][1]), ("선생님", "아니요.", "No."), ("학생", _GAQ[1][0], _GAQ[1][1]), ("선생님", "아니요.", "No.")])),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_GAMINE)),
        card("Activities left out", "The sentence lists, and Follow-up 2 (listening to five short dialogs containing –는/(으)ㄴ/(으)ㄹ 것, writing the phrase with the verb [the first one, 준비할 것, “things that I will prepare”, is given] and its English meaning) need lists and audio."),
    ],
    exercises=uniq(
        _tr(_GA1 + _GA2 + _GA3 + _GA4 + _GAM + _GAMINE, k=3)
        + [M("What does an attributive form + 것 mean?", "the thing(s) that; what", ["because", "although", "in order to"], "The book’s note."), M("What does 내가 어제 먹은 것 mean?", "what I ate yesterday", ["what I eat every day", "what I will eat", "what I like"], "past attributive."), M("What does 내가 먹을 것 mean?", "what I will eat", ["what I ate", "what I eat every day", "eating"], "future attributive."), M("What does 한국말을 배운 학생 mean?", "a student who (has) learned Korean", ["a student who learns Korean", "a student who will learn Korean", "a Korean teacher"], "배운."), M("What does 어제 배운 것을 적어 보세요 mean?", "Please write down what you learned yesterday", ["Please learn tomorrow", "Please read it", "Please forget it"], "The book’s example."),
           F("내가 매일 ___ 것은 한국음식입니다. (eat)", "먹는", ["먹은", "먹을"], "present attributive."), F("내가 어제 ___ 것의 이름이 뭐죠? (ate)", "먹은", ["먹는", "먹을"], "past attributive."), F("어제 ___ 것을 종이에 적어 보세요. (learned)", "배운", ["배우는", "배울"], "past attributive."), F("한국사람들이 ___ 것은 축구입니다. (like)", "좋아하는", ["좋아한", "좋아할"], "present attributive."), F("동생이 좋아하는 ___은 꽃이에요. (the thing)", "것", ["곳", "분"], "것."),
           read_q("내가 매일 먹는 것은 한국음식입니다"), read_q("내가 매일 먹는 것을 먹지 마세요"), read_q("한국사람들이 좋아하는 것은 축구입니다"), read_q("어제 배운 것을 종이에 적어 보세요"), read_q("동생이 좋아하는 것은 꽃이에요")]
    ),
)

# ================================================================== L6: Grammar B: -(으)ㄴ 채(로)
_CH1 = [("나는 안경을 쓴 채로 잡니다.", "I slept “in the state of having put on my glasses” or I slept with my glasses on."), ("한 남성이 차 안에서 숨진 채 발견되었다.", "A man was found “in the state of having died” inside a vehicle or A man was found dead inside a vehicle.")]
_CH2 = [("신발을 신은 채로 방 안에 들어갔어요.", "He entered the room “in the state of having put on his shoes” or He entered the room with his shoes on."), ("김 모 씨는 술을 마신 채 운전하다 접촉 사고를 냈다.", "Mr. Kim caused a collision “in the state of having consumed alcohol” or Mr. Kim caused a collision while drunk driving.")]
_CH3 = [("한 남성이 차 안에서 숨진 채 발견되었다.", "A man was found dead inside a vehicle."), ("한 남성이 차 안에서 숨진 상태로 발견되었다.", "A man was found dead inside a vehicle (with –(으)ㄴ 상태로).")]
_ACT = [("제주에 사는 한 영화배우가 술을 마신 채 운전하다 도로 위에서 잠든 채 발견됐다.", "A movie actor living in Jeju was found asleep on a road after driving while drunk."), ("이 영화배우는 이날 오전 다섯 시께 제주시의 한 도로에 자신의 스포츠유틸리티차량을 세워 둔 채 차 안에서 잠을 자고 있었다.", "At about 5 a.m. that day, the actor was sleeping inside his own SUV, which he had left parked on a road in Jeju City."), ("경찰은 음주운전으로 인한 다른 사고는 없었다고 말했다.", "The police said there were no other accidents caused by drunk driving."), ("더 자세한 경위를 조사할 예정이라고 말했다.", "They said they plan to investigate the circumstances in more detail.")]
_CHMINE = [("창문을 연 채로 잤어요.", "I slept with the window open."), ("불을 켠 채 나갔어요.", "I went out with the light on."), ("모자를 쓴 채 인사했어요.", "I greeted (him) with my hat on."), ("문을 연 채로 운전했어요.", "I drove with the door open.")]
L6 = lesson(
    "Ch 37 · Grammar B: indicating the state of a completed action, –(으)ㄴ 채(로)",
    "-(으)ㄴ 채(로) · 안경을 쓴 채로 · 숨진 채 발견 · 술을 마신 채 운전 · -(으)ㄴ 상태로",
    requires=[],
    cards=[
        card("In the state of having done (something)",
             "The conjunctive ending –(으)ㄴ 채(로) literally means “in the state of having done (something)”. This conjunctive ending attached to the stem of an action verb is used to indicate that the condition or state of a completed action still remains or is maintained when the main action occurs. For example (the English is the book’s):",
             examples=passage(_CH1)),
        card("What the examples show", "Note that –(으)ㄴ 채(로) is attached to the stem of the action verb 쓰다 (to put on) in the first sentence and to the stem of the action verb 숨지다 (to die; to pass away) in the second sentence. Thus, the first sentence indicates that the speaker’s state of having put on his glasses is maintained while he sleeps. Likewise, the second sentence indicates that a man’s state of death remained when he was found."),
        card("Indicating the condition or state of a completed action", "action verb stem + (으)ㄴ 채(로). More examples (the English is the book’s):", examples=passage(_CH2)),
        card("참고: –(으)ㄴ 채(로) and –(으)ㄴ 상태로", "–(으)ㄴ 채(로) is interchangeable with –(으)ㄴ 상태로, which also means in the state of having done (something).", examples=passage(_CH3)),
        card("Follow-up 4 (Reading): a news report about an actor",
             "The following is a news report about an actor involved in an accident. The book asks you to answer in English: Under what circumstances was the actor found? (three bullets). The book’s article names the actor; here the name is left out. The article is the book’s otherwise; the time is spelled in Hangul and the quotation marks are dropped. The English is mine.",
             examples=passage(_ACT)),
        card("The answer (mine)", "The book leaves the bullets blank; my answers:", tables=[table(["Circumstances (mine)", ""], [["•", "He had been driving after drinking"], ["•", "He was found asleep inside his SUV, which was left parked on a road, at about 5 a.m."], ["•", "No other accident caused by drunk driving was reported; the police will investigate further"]])]),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_CHMINE)),
        card("Activities left out", "Follow-up 5 (listening to four conversations in which a man describes a mistake he made and its consequence), Activity 1 (Today’s Word Master, SMART Board) and Activity 2’s … (see the Topic B lesson for the article) are audio and computer activities."),
    ],
    exercises=uniq(
        _tr(_CH1 + _CH2 + _CH3 + _ACT + _CHMINE, k=3)
        + [M("What does –(으)ㄴ 채(로) indicate?", "A state of a completed action that remains while the main action occurs", ["A future wish", "A reason", "A request"], "The book’s note."), M("What does 안경을 쓴 채로 잡니다 mean?", "I sleep with my glasses on", ["I take off my glasses", "I buy glasses", "I lose my glasses"], "The book’s example."), M("What does 숨진 채 발견되었다 mean?", "was found dead", ["was found alive", "was found asleep", "was found lost"], "The book’s example."), M("What is interchangeable with –(으)ㄴ 채(로)?", "–(으)ㄴ 상태로", ["–는 대로", "–(으)ㄹ 때", "–(으)ㄴ 것"], "The book’s note."), M("What does 신발을 신은 채로 방 안에 들어갔어요 mean?", "He entered the room with his shoes on", ["He took off his shoes", "He left the room", "He bought shoes"], "The book’s example."),
           F("나는 안경을 쓴 ___ 잡니다. (with … on)", "채로", ["대로", "때"], "–(으)ㄴ 채로."), F("한 남성이 차 안에서 숨진 ___ 발견되었다. (dead)", "채", ["것", "때"], "–(으)ㄴ 채."), F("김 모 씨는 술을 마신 ___ 운전하다 접촉 사고를 냈다. (while drunk)", "채", ["대로", "때"], "–(으)ㄴ 채."), F("신발을 ___ 채로 방 안에 들어갔어요. (put on; past attributive)", "신은", ["신는", "신을"], "신은 채로."), F("창문을 ___ 채로 잤어요. (opened)", "연", ["여는", "열"], "열다 → 연."),
           read_q("나는 안경을 쓴 채로 잡니다"), read_q("한 남성이 차 안에서 숨진 채 발견되었다"), read_q("신발을 신은 채로 방 안에 들어갔어요"), read_q("김 모 씨는 술을 마신 채 운전하다 접촉 사고를 냈다"), read_q("창문을 연 채로 잤어요")]
    ),
)

# ================================================================== L7: Topic C
_C_DLG = [
    ("정 대위", "김 소령님, 조금 전 야간 사격 훈련 중 총기 오발 사고가 있었습니다.", "Major Kim, there was a firearm misfire accident during night firing training a little while ago."),
    ("김 소령", "총기 오발 사고? 어느 부대야?", "A firearm misfire accident? Which unit?"),
    ("정 대위", "오 중대 제이 소대에서 사고가 발생했습니다.", "The accident occurred in the 2nd platoon of the 5th company."),
    ("김 소령", "그래? 사상자가 있어?", "Is that so? Are there casualties?"),
    ("정 대위", "사병 한 명이 팔에 부상을 입었습니다.", "One enlisted soldier was injured in the arm."),
    ("김 소령", "사격 훈련할 때는 실탄을 쓰니까 항상 조심해야지. 근데, 왜 사고가 났어?", "Since we use live ammunition when training on the range, we have to be careful at all times. But why did the accident happen?"),
    ("정 대위", "사병이 총기를 부주의하게 다루었다고 합니다.", "They say the soldier handled the firearm carelessly."),
    ("김 소령", "부상을 입은 사병은 지금 어디에 있어?", "Where is the injured soldier now?"),
    ("정 대위", "사고 후 즉시 육군 병원으로 후송되었습니다.", "Right after the accident he was evacuated to the Army hospital."),
    ("김 소령", "다른 사병들은 괜찮아?", "Are the other soldiers all right?"),
    ("정 대위", "다른 사병들은 모두 무사합니다. 사병들에 의하면 사격 교관이 빠르고 침착하게 응급 조치를 잘 취했다고 합니다. 그 덕분에 부상자가 적었다고 합니다.", "The other soldiers are all safe. According to the soldiers, the range instructor took emergency measures quickly and calmly. They say that thanks to that there were few injured."),
    ("김 소령", "알았어. 부상당한 사병 상태가 괜찮아질 때까지 상태를 계속 보고하도록 해.", "Understood. Keep reporting the injured soldier’s condition until he gets better."),
    ("정 대위", "네. 알겠습니다.", "Yes, sir. Understood."),
]
_C_WORDS = ["공포탄", "끝내", "뒤집히다", "몰다", "무너지다", "무단", "무사", "보고", "사병", "사상자", "새벽", "실탄", "야간", "어선", "이탈", "조치", "즉시", "진술", "추락", "취하다", "해역", "후송", "총기오발"]
_C_WORDS2 = [("다루다 / 취급하다", "to deal with; to handle"), ("~덕분에 / 덕택에", "thanks to"), ("밝히다", "1. to reveal; to make something public; 2. to clarify; to bring (a matter) to light"), ("~에 의하면", "according to"), ("~척", "counter for ships or boats"), ("(술) 취하다", "to get drunk; to be intoxicated"), ("해(양)경(찰)", "coast guard; “ocean police”")]
L7 = lesson(
    "Ch 37 · Topic C: There was an accident during firing training (사격 훈련 중에 사고가 났습니다)",
    "사격 훈련 중에 사고가 났습니다 · 총기 오발 · 사병 · 실탄 · 후송 · 응급 조치 · 보고 · 야간 훈련",
    requires=[],
    cards=[
        card("Topic C: There was an accident during firing training (사격 훈련 중에 사고가 났습니다)",
             "Captain Chung is reporting to Major Kim about an accident that happened a few minutes ago. (The English is mine; the book gives none; the unit numbers are spelled out in Hangul.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 무사(하다), 보고(하다/되다), 이탈(하다), 조치(하다), 진술(하다), 추락(하다) and 후송(하다/되다) take the forms in parentheses.",
             tables=[ktable(_rows(_C_WORDS)), table(["Word", "Meaning"], [[a, b] for a, b in _C_WORDS2], say=[0])]),
        card("Activities left out", "Follow-up 1 (listening to three audio clips and matching each with misfire, crash or collapse and fall, and watching the video clips), Follow-up 2 (reading three news articles about military incidents, identifying the EEIs and exchanging them in groups; the book glosses 경계석: curb stone; 생활관: barracks; 터뜨리다: to explode; 터지다: to go off; explode; 법: law; 불법: illegal; 은닉하다: to conceal) and the Topic Presentation C study steps (SMART Board) are audio, video, group and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG), k=3)
        + [M("What kind of accident was reported?", "A firearm misfire during night firing training", ["A car crash", "A fire", "A fall"], "야간 사격 훈련 중 총기 오발."), M("Which unit?", "The 2nd platoon of the 5th company", ["The 1st company", "The 3rd platoon", "The 5th battalion"], "오 중대 제이 소대."), M("How many were injured?", "One soldier, in the arm", ["Two soldiers", "None", "Five soldiers"], "사병 한 명이 팔에 부상."), M("Why did the accident happen?", "A soldier handled the firearm carelessly", ["Bad weather", "A broken weapon", "The instructor"], "총기를 부주의하게 다루었다."), M("Where was the injured soldier taken?", "The Army hospital", ["His barracks", "A civilian clinic", "The range"], "육군 병원."), M("What did the range instructor do?", "Took emergency measures quickly and calmly", ["Fled", "Did nothing", "Called the press"], "빠르고 침착하게 응급 조치."), M("What does Major Kim order?", "Keep reporting the soldier’s condition until he gets better", ["Cancel training", "Punish the soldier", "Close the range"], "계속 보고하도록 해."),
           F("조금 전 야간 사격 훈련 중 총기 ___ 사고가 있었습니다. (misfire)", "오발", ["이탈", "추락"], "총기 오발."), F("사격 훈련할 때는 ___을 쓰니까 항상 조심해야지. (live ammunition)", "실탄", ["공포탄", "총기"], "실탄."), F("부상을 입은 사병은 즉시 육군 병원으로 ___되었습니다. (evacuated)", "후송", ["이탈", "추락"], "후송."), F("사병들 ___ 사격 교관이 응급 조치를 잘 취했다고 합니다. (according to)", "에 의하면", ["덕분에", "때문에"], "~에 의하면."), F("그 ___ 부상자가 적었다고 합니다. (thanks to)", "덕분에", ["에 의하면", "때문에"], "덕분에."),
           read_q("사격 훈련 중에 사고가 났습니다"), read_q("총기 오발 사고가 있었습니다"), read_q("사병 한 명이 팔에 부상을 입었습니다"), read_q("사고 후 즉시 육군 병원으로 후송되었습니다"), read_q("다른 사병들은 모두 무사합니다")]
    ),
)

# ================================================================== L8: Grammar C: -(으)ㄹ 때 + time markers
_T1 = [("출근할 때에 차가 많이 막혀요.", "The traffic is quite jammed when I leave for work."), ("숙제를 할 때 음악을 듣지 마세요.", "When you do your homework, please don’t listen to music.")]
_T2 = [("전화할 때마다 통화 중이에요.", "Whenever I call (them), the line is busy."), ("시간이 날 때마다 등산해요.", "Whenever I find time, I go mountain climbing."), ("출근할 때부터 배가 아팠어요.", "I have had a stomachache since I left for work."), ("어렸을 때부터 독서가 취미예요.", "Reading books has been my hobby since I was young."), ("숙제를 다 할 때까지 놀지 마.", "Don’t play until you complete your homework."), ("친구가 전화할 때까지 잤어요.", "I slept until my friend called.")]
_T3 = [("진희는 대학교에 입학할 때부터 졸업할 때까지 장학금을 받았습니다.", "마다/부터/까지", "부터, 까지", "Jinhee received a scholarship from the time she entered university until she graduated."), ("저는 엘에이에 자주 갑니다. 엘에이에 갈 때마다 미용실에 가서 머리를 해요.", "마다", "마다", "I often go to LA. Whenever I go to LA, I go to a hair salon and get my hair done."), ("오늘 아침에 집을 나올 때부터 비가 왔는데 아직도 오는군요.", "부터", "부터", "It was raining from the time I left home this morning and it is still raining."), ("아버지는 지난 달 퇴직할 때까지 사십 년 동안 같은 곳에서 일하셨어요.", "까지", "까지", "My father worked in the same place for forty years until he retired last month."), ("저는 요리하는 것을 좋아해서 시간이 있을 때마다 요리를 합니다.", "마다", "마다", "I like cooking, so I cook whenever I have time."), ("성미는 피아노를 어릴 때부터 배워서 지금은 상당히 잘 칩니다.", "부터", "부터", "Seongmi has learned piano since she was young, so now she plays quite well.")]
_JR = [("오늘 아침에 일어날 때부터 머리가 아팠다.", "I had a headache from the time I woke up this morning."), ("그래서 학교에 조금 늦게 열 시쯤 갔다.", "So I went to school a little late, around ten."), ("점심식사 하러 갈 때까지 공부를 좀 하고 기숙사에 돌아와서 오후 수업 시작할 때까지 잤다.", "I studied a bit until it was time to go to lunch, came back to the dormitory and slept until the afternoon class started."), ("그래도 머리가 아파서 선생님께 전화를 하고 의무실에 갔다.", "I still had a headache, so I called the teacher and went to the medical clinic."), ("의무실에 갈 때마다 사람이 많아서 기다려야 하는데 다행히 오늘은 사람이 별로 없었다.", "Every time I go to the clinic there are many people so I have to wait, but fortunately there weren’t many people today."), ("약을 받아서 먹고 돌아와서 저녁 아홉 시쯤 어머니가 전화하실 때까지 잤다.", "I received the medicine, took it, came back and slept until my mother called at around nine in the evening.")]
_TM = [("어릴 때부터 무엇을 했어요? 어릴 때는 어땠어요?", "What did you do from when you were young? What were you like when you were young?"), ("어릴 때부터 저는 키가 컸어요.", "I have been tall since I was young."), ("박 일병은 어릴 때부터 키가 컸어요. 고등학교에 다닐 때까지 드럼을 쳤어요. 고향에 갈 때마다 박 일병은 서핑을 해요.", "Private First Class Park has been tall since he was young. He played drums until he went to high school. Whenever he goes to his hometown, he surfs.")]
L8 = lesson(
    "Ch 37 · Grammar C: time expressions with –(으)ㄹ 때, 때마다 · 때부터 · 때까지",
    "-(으)ㄹ 때(에) · -(으)ㄹ 때마다 · -(으)ㄹ 때부터 · -(으)ㄹ 때까지 · 어릴 때부터 · 퇴직할 때까지",
    requires=[],
    cards=[
        card("–(으)ㄹ 때(에): when",
             "Consider the literal meaning of the conjunctive ending –(으)ㄹ 때(에), which translates to when. For example (the English is the book’s):",
             examples=passage(_T1)),
        card("때 and the time marker 에", "때 by itself is a noun that means time or moment (e.g., 그때 [that time] and 점심 때 [lunch time or time for lunch]) and ~에 is a time marker that translates to at, on, or in (e.g., 7시에 [at seven], 월요일에 [on Monday], and 2002년에 [in 2002]). Thus, the literal meaning of –(으)ㄹ 때에 is “at the time (that)” or “at the moment (that)”."),
        card("Replacing 에 with other time markers",
             "When 에 in –(으)ㄹ 때에 is replaced with the following time markers, we get the following English meanings:",
             tables=[table(["Pattern", "Meaning"], [["-(으)ㄹ 때마다", "every time (that); whenever"], ["-(으)ㄹ 때부터", "from the time (that); since"], ["-(으)ㄹ 때까지", "to the moment (that); until"]])],
             examples=passage(_T2)),
        card("Follow-up 1 (Reading): choose 마다, 부터 or 까지",
             "Choosing between 마다, 부터, and 까지, fill in the blanks with the correct marker. The sentences are the book’s (LA is read 엘에이; 40년 is spelled out); the blanks are filled in with my answers; the English is mine.",
             tables=[table(["Sentence (completed)", "Marker(s) (mine)", "English (mine)"], [[a, b, d] for a, b, c, d in _T3], say=[0])]),
        card("Follow-up 3 (Reading): a DLI student’s journal entry",
             "Read the journal entry of a DLI student and complete the partial translation by filling in the blanks in English (the book gives a partial English translation with six blanks: since I woke up; until I went for lunch; until the afternoon class started; every time I go to the clinic; until my mother called). The entry is the book’s with the numbers spelled out; the English is mine.",
             examples=passage(_JR)),
        card("Follow-up 4 (Listening and speaking): the interview model", "Read the questions in the first column of the table (어릴 때부터 무엇을 했어요? 어릴 때는 어땠어요?; 고등학교에 다닐 때까지 무엇을 했어요? 어릴 때는 어땠어요?; 고향에 갈 때마다 무엇을 해요?), answer them in Korean using –(으)ㄹ 때마다, –(으)ㄹ 때부터 and –(으)ㄹ 때까지, interview a partner, and report to the class. The book’s model (the English is mine):", examples=dlg([("A", _TM[0][0], _TM[0][1]), ("B", _TM[1][0], _TM[1][1]), ("A", _TM[2][0], _TM[2][1])])),
        card("Activities left out", "Follow-up 2 (listening to four conversations in which a man explains that whenever he does something, something else happens, marking it good or bad and translating the sentence) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_T1 + _T2 + [(a, d) for a, b, c, d in _T3] + _JR + _TM, k=3)
        + [M("What does –(으)ㄹ 때마다 mean?", "every time (that); whenever", ["since", "until", "when only once"], "The book’s note."), M("What does –(으)ㄹ 때부터 mean?", "from the time (that); since", ["until", "whenever", "because"], "The book’s note."), M("What does –(으)ㄹ 때까지 mean?", "to the moment (that); until", ["since", "whenever", "after"], "The book’s note."), M("What does 어렸을 때부터 독서가 취미예요 mean?", "Reading has been my hobby since I was young", ["I read until I was young", "I read whenever I was young", "I will read"], "때부터."), M("What does 친구가 전화할 때까지 잤어요 mean?", "I slept until my friend called", ["I slept since my friend called", "I slept whenever my friend called", "I called my friend"], "때까지."),
           F("전화할 때___ 통화 중이에요. (whenever)", "마다", ["부터", "까지"], "때마다."), F("출근할 때___ 배가 아팠어요. (since)", "부터", ["마다", "까지"], "때부터."), F("숙제를 다 할 때___ 놀지 마. (until)", "까지", ["마다", "부터"], "때까지."), F("시간이 날 때___ 등산해요. (whenever)", "마다", ["부터", "까지"], "때마다."), F("어렸을 때___ 독서가 취미예요. (since)", "부터", ["마다", "까지"], "때부터."),
           read_q("출근할 때에 차가 많이 막혀요"), read_q("전화할 때마다 통화 중이에요"), read_q("출근할 때부터 배가 아팠어요"), read_q("숙제를 다 할 때까지 놀지 마"), read_q("친구가 전화할 때까지 잤어요")]
    ),
)

# ================================================================== L9: Chapter activities
_F4 = [("공군 에프포이 팬텀 전투기가 십이 일 비행 중 추락했으나 조종사 두 명은 무사한 것으로 확인됐다.", "An Air Force F-4E Phantom fighter crashed during flight on the 12th, but the two pilots were confirmed to be safe."), ("공군과 해경 등에 따르면 이날 낮 열두 시 이십 분쯤 경기도 화성 일대 상공을 날던 에프포이 전투기 한 대가 전곡항 남쪽 구 킬로미터 지점 서해상에 추락했다.", "According to the Air Force and the Coast Guard, at about 12:20 p.m. that day, one F-4E fighter flying over the Hwaseong area in Gyeonggi-do crashed into the West Sea nine kilometers south of Jeongok Port."), ("사고기 조종사들은 비행 중 엔진에서 화재가 발생하자, 민가가 없는 해안 지역으로 기수를 돌렸고, 이후 비상 탈출에 성공했다.", "When a fire broke out in the engine during the flight, the pilots of the crashed plane turned its nose toward a coastal area with no private homes and then succeeded in an emergency escape."), ("사고 지점 인근 해역에서는 어선 한 척이 조업 중이었다.", "In the sea area near the crash site, one fishing boat was operating."), ("조종사 두 명은 이 어선에 구조된 후 항공우주의료원으로 이송됐다.", "The two pilots were rescued by this fishing boat and then transferred to the Aerospace Medical Center."), ("공군 관계자는 조종사들의 건강 상태는 양호하다고 설명했다.", "An Air Force official explained that the pilots’ health condition is good."), ("이번 추락사고 원인은 아직 확인되지 않았으나, 군 안팎에서는 전투기의 노후에 따른 고장일 가능성으로 보고 있다.", "The cause of this crash has not yet been confirmed, but inside and outside the military it is seen as possibly a breakdown due to the aging of the fighter.")]
L9 = lesson(
    "Ch 37 · Activities: a military aircraft accident and the chapter’s other tasks",
    "전투기 추락 · 엔진 화재 · 조종사 무사 · 해경 · 어선 구조 · 사고 보고 · 자기 평가",
    requires=[],
    cards=[
        card("Activity 3 (Reading): a news article about a military accident",
             "The following news article is about a military accident. The book asks you to fill in a table in English: type of accident; how the accident occurred; casualties; possible cause. The book glosses 밝혀지다: to be revealed; 민가: private home; 기수: the nose (of a plane); 탈출하다: to escape; 양호하다: good. The headline (“F-4E 전투기 ‘엔진 화재’로 서해 추락… 조종사 2명 무사”) is left out; the article is the book’s with the numbers spelled out (F-4E is read 에프포이); the English is mine.",
             examples=passage(_F4)),
        card("The table filled in (mine)", "The book leaves the table blank; my answers:",
             tables=[table(["Item", "Answer (mine)"], [["Type of accident", "A military aircraft crash (an F-4E fighter)"], ["How the accident occurred", "A fire broke out in the engine; the pilots steered toward an area without houses, then escaped; the plane crashed into the sea nine kilometers south of Jeongok Port"], ["Casualties", "None; both pilots were rescued by a fishing boat and are in good health"], ["Possible cause", "Not yet confirmed; possibly a breakdown due to the aircraft’s age"]])]),
        card("Activity 4 (Listening, reading, writing and speaking): reporting an accident", "You are participating in a combined exercise with an ROK intelligence unit and receive a radio message about an accident. In two groups you listen to Message A or Message B, summarize it in English, exchange the information in Korean with a student from the other group, and then report the accident to your commander with your partner, preparing the presentation in the class notebook."),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with.\n\n"
             "Now I am able to: identify and provide basic information on fire, traffic, and military-related accidents; and ask about and summarize fire, traffic, and military-related accidents.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; an attributive form + 것 (the thing that; the things that; what); the conjunctive ending –(으)ㄴ 채(로); the conjunctive ending –(으)ㄹ 때까지 (until; to the time that); the conjunctive ending –(으)ㄹ 때마다 (whenever; every time that); the conjunctive ending –(으)ㄹ 때부터 (since; from the time that); and the Sino-Korean syllables within 인명 (人命), 운전자 (運轉者), and 야간 (夜間)."),
        card("Activities left out", "Activity 2 (listening to two audio clips from YTN and MBC about different accidents and watching the video clips; the book glosses 계곡: valley; 자세: position; 파열: damage) and the listening parts of Activity 4 are audio and video activities."),
    ],
    exercises=uniq(
        _tr(_F4, k=3)
        + [M("What kind of aircraft crashed?", "An F-4E fighter", ["A helicopter", "A passenger plane", "A bomber"], "에프포이 전투기."), M("What caused the pilots to change course?", "A fire in the engine", ["A storm", "Fuel shortage", "An enemy"], "엔진에서 화재."), M("Where did they steer the plane?", "Toward a coastal area with no private homes", ["Toward the city", "Toward an airfield", "Toward a ship"], "민가가 없는 해안 지역."), M("Who rescued the pilots?", "A fishing boat", ["A helicopter", "The Navy", "A passing ship"], "어선."), M("How are the pilots?", "In good health", ["Seriously injured", "Missing", "Dead"], "양호하다."), M("What is the possible cause?", "A breakdown due to aging", ["Pilot error", "Enemy fire", "Weather"], "노후에 따른 고장."),
           F("조종사들은 비행 중 엔진에서 ___가 발생하자 기수를 돌렸다. (fire)", "화재", ["누전", "폭발"], "화재."), F("조종사들은 이 어선에 ___된 후 병원으로 이송됐다. (rescued)", "구조", ["후송", "이탈"], "구조."), F("공군과 ___ 등에 따르면 전투기가 서해상에 추락했다. (coast guard)", "해경", ["소방", "경찰"], "해경."), F("전투기 한 대가 서해상에 ___했다. (crashed)", "추락", ["전복", "충돌"], "추락."), F("사고 원인은 아직 ___되지 않았다. (confirmed)", "확인", ["발견", "진화"], "확인."),
           read_q("전투기 추락 사고"), read_q("조종사 두 명은 무사한 것으로 확인됐다"), read_q("비상 탈출에 성공했다"), read_q("조종사들의 건강 상태는 양호하다"), read_q("추락사고 원인은 아직 확인되지 않았다")]
    ),
)

# ================================================================== L10: core vocabulary
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Loan words", _CV_LOAN), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/")]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L10 = lesson(
    "Ch 37 · Core vocabulary",
    "주요 단어 · 사고 · 화재 · 교통사고 · 총기 오발 · 목격 · 피해 · 후송",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank.\n\n"
             "The example sentences with digits are respelled in Hangul (5월 → 오 월; 20명 → 이십 명; 30% → 삼십 퍼센트; 119 → 일일구; 7층짜리 → 칠 층짜리; 24시간 → 스물네 시간; 5척 → 다섯 척; NLL is dropped)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 목격자 mean?", "an eyewitness", ["a victim", "a driver", "a police officer"], "目擊者."), M("What does 인명피해 mean?", "human casualties", ["property damage", "a fire", "a crash"], "人命 + 被害."), M("What does 재산피해 mean?", "property damage", ["human casualties", "a fire", "a crash"], "財産 + 被害."), M("What does 추돌 mean?", "a rear-end collision", ["a head-on collision", "a fire", "a short circuit"], "追突."), M("What does 전복 mean?", "overturned; flipped over", ["collided", "burned", "spread"], "顚覆."), M("What does 사병 mean?", "an enlisted man; a soldier", ["an officer", "a civilian", "a pilot"], "士兵."), M("What does 실탄 mean?", "live ammunition", ["blank ammunition", "a gun", "a target"], "實彈."), M("What does 공포탄 mean?", "blank ammunition", ["live ammunition", "a gun", "a bomb"], "空砲彈."),
           F("소방 ___은 전기 누전으로 불이 시작됐다고 보고 있다. (authorities)", "당국", ["현장", "소식"], "당국."), F("사고를 ___하신 분은 경찰에 연락해 주시기 바랍니다. (witnessed)", "목격", ["발견", "발생"], "목격."), F("승합차가 ___되면서 운전자가 중상을 입었다. (overturned)", "전복", ["추돌", "충돌"], "전복."), F("사병이 총기를 ___하게 다루었다고 합니다. (carelessly)", "부주의", ["철저", "긴급"], "부주의하게."), F("사고를 당하면 ___ 119에 연락하십시오. (immediately)", "즉시", ["끝내", "새벽"], "즉시."),
           read_q("주요 단어"), read_q("목격자"), read_q("인명피해"), read_q("재산피해"), read_q("후송")]
    ),
)

UNIT = unit("Semester 2 · Unit 10 · Chapter 37: Accidents (사고)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])

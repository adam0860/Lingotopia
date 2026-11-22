"""Unit 46: KBC Semester 2, Unit 10, Chapter 39 - Natural Disasters (자연재해).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 10, Student's Edition (2022).
Audio, video, pictures, maps, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 39 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("~가량", "(假量) approximately, about", "어젯밤에 서울 지역에 오십 밀리미터가량의 비가 내렸습니다."),
    ("가뭄", "a drought", "비가 오지 않고 가뭄이 계속되고 있어요."),
    ("강수량 / 강우량", "(降水量 / 降雨量) the amount of rainfall; precipitation", "올해는 가뭄 때문에 강우량이 작년에 비해 너무 적어요."),
    ("건조", "(乾燥) dryness; aridity; to be dry; to be arid (~하다)", "봄에는 건조한 날씨 때문에 산불이 자주 납니다."),
    ("경보", "(警報) a warning; an alarm; “warning report”", "태풍이 강해지면서 전국에 호우경보가 내려졌습니다."),
    ("고기압", "(高氣壓) high atmospheric pressure", "고기압의 영향으로 날씨가 맑겠습니다."),
    ("기록(적)", "(記錄(的)) record (-breaking); to record (~하다)", "최근 금값이 기록적으로 매일 상승하고 있습니다. 어제는 한 온스에 구백팔십 달러를 기록했습니다."),
    ("늦다", "to be late", "오래 기다렸지? 늦어서 미안해."),
    ("~ 만에", "for the first time in [time]; after the lapse [of time]", "삼 년 만에 친구를 만나서 아주 반가웠습니다."),
    ("몰아치다", "(storm, blizzard, etc.) to rage", "비바람이 세게 몰아쳐서 우산을 펼 수 없었어요."),
    ("(무)더위", "a (sweltering) heat spell; mugginess", "요즘 한국은 더위가 일찍 옵니다. 칠 월 한 달 동안 삼십 도가 넘는 무더위가 계속 되었어요."),
    ("물결이 일다", "waves rise", "오늘 제주도 앞바다에서는 물결이 높게 일겠습니다."),
    ("발령", "(發令) issuing (of an order, warning, etc.); to issue / to be issued (~하다/되다)", "기상청에서 호우주의보를 발령했습니다."),
    ("북상", "(北上) moving northward; “north above”; to move northward (~하다)", "북상하는 장마전선의 영향으로 이번 주는 많은 비가 예상됩니다."),
    ("산간", "(山間) a mountainous area; “between mountains”", "어제 강원도 산간 지방에 폭설이 내렸습니다."),
    ("소나기", "a (rain) shower", "소나기가 내려서 시원합니다."),
    ("예년", "(例年) a normal (ordinary) year", "예년에 비해 올해는 비가 많이 옵니다."),
    ("예보", "(豫報) forecast; to forecast / to be forecasted (~하다/되다)", "기상청의 예보가 자주 틀려서 시민의 불만이 큽니다."),
    ("장마전선", "(前線) monsoon front; seasonal rain front; “monsoon front line”", "오늘 밤부터 남부지방에 있던 장마전선이 북상할 예정입니다."),
    ("적설량", "(積雪量) amount of snowfall; “accumulated snow amount”", "어제 내린 폭설로 인해 강원도 지방 적설량은 이십 센티미터를 기록했습니다."),
    ("전국적", "(全國的) national; nationwide", "오늘 오후에 전국적으로 비가 내리겠습니다."),
    ("점차(적으로)", "(漸次(的)) gradually", "오늘 오후부터 날씨가 점차 흐려진대요."),
    ("주의보", "(注意報) an advisory", "기상청에서 태풍주의보를 발령했으니까 조심하세요."),
    ("집중", "(集中) concentration; focus; to concentrate; to focus / to be concentrated; to be focused (~하다/되다)", "집중해서 들으면 이해를 더 잘 할 수 있어요."),
    ("천둥", "thunder; to thunder (~치다)", "어젯밤에 천둥 소리 때문에 잠을 못 잤어요."),
    ("폭설", "(暴雪) heavy snowfall; a snowstorm; a blizzard; “violent snow”", "폭설로 학교에 휴교령이 내려졌대요."),
    ("한파", "(寒波) a cold snap; “cold wave”", "한파로 도로가 얼어서 교통사고가 많이 발생했어요."),
    ("해상", "(海上) the sea; “above the sea”", "서해 해상에서는 물결이 높게 일겠습니다."),
    ("확산", "(擴散) spreading; to spread (~되다)", "독감이 전 세계로 확산되고 있습니다."),
    ("현상", "(現象) a phenomenon", "오로라는 북극 지방에서 자주 나타나는 현상이다."),
]
_CV_B = [
    ("겪다", "to undergo; to go through; to experience", "비가 많이 와서 불편을 겪고 있어요."),
    ("결항", "(缺航) cancellation of an ocean liner or flight; to cancel / to be canceled (~하다/되다)", "태풍으로 제주도에서 출발하는 비행기가 모두 결항됐습니다."),
    ("구간", "(區間) a section", "휴가철이 시작되면서 전국의 주요 고속도로에 정체 구간이 많아지고 있습니다."),
    ("그치다", "to stop; to cease (rain/snow)", "오전에 비가 오겠지만 오후에는 그치겠습니다."),
    ("나타나다", "to appear; to show up", "파티장에 갑자기 경찰이 나타났어요."),
    ("떠내려가다", "to flow away; to be swept away; “float and go down”", "홍수로 집이 떠내려갔습니다."),
    ("마비", "(痲痺) paralysis; to paralyze / to be paralyzed (~시키다/되다)", "그 사람은 어렸을 때 교통 사고로 팔과 다리가 마비됐다고 해요."),
    ("복구", "(復舊) restoring; rebuilding; “restoring old”; to restore / to be restored (~하다/되다)", "피해 복구를 위해 군인과 경찰, 공무원이 함께 일하고 있습니다."),
    ("산사태", "(山沙汰) a mudslide; a landslide; “mountain sand flowing”", "어느 지역에서 산사태가 발생했습니까?"),
    ("수재민", "(水災民) flood victims; “water disaster people”", "홍수로 피해를 입은 수재민들을 도웁시다."),
    ("쏟아지다", "(something) to pour", "일주일 동안 계속 많은 비가 쏟아졌어요."),
    ("얼다", "to freeze; to be frozen", "날씨가 추워서 길이 얼었어요."),
    ("이상기후", "(異常氣候) abnormal climate", "이상기후 때문에 봄에 눈이 많이 왔어요."),
    ("작업", "(作業) work; operations; to work; to operate (~하다)", "밤 늦게까지 수해 복구 작업을 했습니다."),
    ("잠기다", "to be submerged; to go underwater", "홍수로 도시 전체가 물에 잠겼어요."),
    ("장마", "a rainy season; monsoon season", "긴 장마가 끝나고 무더위가 시작되었다."),
    ("재해", "(災害) a disaster; “disaster and damage”", "자연재해 중에서 가장 대비하기 힘든 것이 지진이다."),
    ("점점", "(漸漸) gradually; slowly", "날씨가 점점 추워지고 있어요."),
    ("정전", "(停電) a power outage; a blackout; “stopped electricity”", "어젯밤에 한 시간 동안 우리 아파트 전체가 정전됐어요."),
    ("중단", "(中斷) suspension; to suspend; to halt; to discontinue / to be suspended; to be halted; to be discontinued (~하다/되다)", "날씨 때문에 공사를 중단했습니다."),
    ("~철", "a ~ season", "장마철이 시작돼서 매일 비가 와요."),
    ("추위", "a cold spell; cold weather", "한국은 겨울에 추위가 심하고 눈도 많이 내립니다."),
    ("침수", "(浸水) submersing; “water invasion”; to be immersed; to go underwater (~되다)", "홍수로 많은 집이 침수되었어요."),
    ("태풍", "(颱風) a typhoon; “colossal wind”", "한국에는 유월에서 칠 월 사이에 태풍이 옵니다."),
    ("폭염", "(暴炎) heat wave; scorching heat", "폭염으로 에어컨 판매가 늘었어요."),
    ("폭우", "(暴雨) a heavy rainfall; torrential rain; “violent rain”", "어제는 바람이 불고 폭우가 쏟아졌어요."),
    ("호우", "(豪雨) a heavy rain; a torrential rain", "오늘 아침 호우 때문에 운전하기 힘들었어요."),
    ("홍수 / 물난리", "(洪水) a flood; “big water”", "홍수가 나서 수재민이 많이 생겼습니다."),
    ("폐쇄", "(閉鎖) closure; shutdown; to close; to shut down / to be closed (~하다; 시키다/되다)", "사건 현장이 폐쇄돼서 일반 시민들은 출입할 수 없습니다."),
]
_CV_C = [
    ("강진", "(强震) a strong earthquake", "인도네시아에서 강진이 발생했어요."),
    ("게다가", "besides; moreover", "그 지역은 사람이 많고 게다가 높은 건물도 많습니다."),
    ("공급", "(供給) supply; provision; to supply; to provide / to be supplied; to be provided (~하다/되다)", "자원봉사팀이 구호품을 공급하고 있습니다."),
    ("구호(물)품", "(救護(物)品) relief items; relief supplies", "홍수가 난 지역 주민들에게 구호품을 전달했습니다."),
    ("느끼다", "to feel", "제주도에 가면 자연의 아름다움을 느낄 수 있습니다."),
    ("단체", "(團體) a group; a party; an organization", "여러 단체에서 수재민들에게 구호품을 나누어 주었어요."),
    ("대피", "(待避) evacuation; to evacuate; to take shelter (~하다)", "야영 중에 폭우가 오면 높은 곳으로 대피해야 합니다."),
    ("도움", "help; assistance; “helping”", "숙제가 어려워서 선생님의 도움이 필요합니다."),
    ("매몰", "(埋沒) burying; to be buried (~되다)", "이번 지진으로 매몰된 사람들이 많습니다."),
    ("무너지다", "to collapse", "태풍과 홍수로 많은 집들이 무너졌습니다."),
    ("묻히다", "to be buried", "산사태가 나서 집이 흙더미에 묻혔어요."),
    ("모금", "(募金) fundraising; “collecting money”; to fundraise (~하다)", "수재민들을 위해서 모금을 하고 있습니다."),
    ("생존자", "(生存者) a survivor", "이번 비행기 사고의 생존자는 열 명입니다."),
    ("생필품", "(生必品) a daily necessity; “items necessary for life”", "생필품이 없어서 이재민이 어려움을 겪고 있어요."),
    ("성금", "(誠金) a donation; a contribution; “sincere money”", "어려운 사람들을 돕기 위해서 성금을 냈어요."),
    ("수색", "(搜索) search (i.e. rescue ops, criminal investigations, etc.); to search (~하다)", "비가 계속 와서 사고 지역을 수색하기가 어렵습니다."),
    ("실종", "(失踪) missing; “lost trace”; to go missing; to be missing (~되다)", "우리 학교에 다니는 남학생 한 명이 실종돼서 경찰이 찾고 있어요."),
    ("여진", "(餘震) an aftershock; “remaining tremor”", "이번 대지진 이후에 크고 작은 여진이 계속되고 있습니다."),
    ("이재민", "(罹災民) a victim of natural disaster", "지진이 나서 많은 이재민이 발생했어요."),
    ("적십자사", "(赤十字社) the Red Cross; “red cross company”", "적십자사는 태풍 피해를 입은 사람들을 돕기 위해 성금을 모으고 있습니다."),
    ("지진", "(地震) an earthquake", "한국은 지진이 많이 발생하지 않습니다."),
    ("지진해일 / 쓰나미", "a tsunami; a tidal wave caused by an earthquake", "바다에서 큰 지진이 발생하면 쓰나미가 발생할 수 있습니다."),
    ("진동", "(震動) a shock; a tremor; a quake", "어제 지진이 났는데 저는 진동을 느끼지 못했습니다."),
    ("진짜", "really; real; genuine", "우리 아들이 대학에 합격해서 진짜 기분이 좋아요. 이 시계는 진짜 스위스 시계예요."),
    ("해일", "(海溢) a tidal (storm) wave", "바닷가 근처에는 해일의 위험이 있습니다."),
    ("휴교령", "(休校令) an order for school closing", "오늘 전국의 초등학교에 휴교령을 내렸어요."),
    ("흙더미", "a mud pile; “earth pile”", "구조원들이 흙더미 속에서 사람들을 구조했어요."),
]
_CV_LOAN = [("쓰나미", "a tsunami; a tidal wave caused by an earthquake", "얼마 전에 일본에서 발생한 쓰나미 때문에 많은 이재민이 발생했습니다.")]
_CV_GR = [
    ("question words used as indefinite pronouns", "who → someone, etc.", "지금 밖에 누가 있어요. 우리 언제 같이 점심 먹자. 어떤 지역에서 큰 홍수가 났어요."),
    ("a noun clause in an appositive relationship", "the news that …", "내일 태풍이 온다는 뉴스를 들었어요?"),
    ("a question word + (이)나/(이)든지", "whoever; whatever; wherever; whenever", "이 파티에는 누구나 참석할 수 있어요. 주말에는 언제든지 전화하세요."),
    ("~에 관해서 / ~에 관한", "about; concerning; regarding", "한국역사에 관해서 공부하고 싶어요. 한국역사에 관한 책을 읽고 있어요."),
    ("~을/를 위해서 / ~을/를 위한", "for (the sake of)", "부모님을 위해서 선물을 샀어요. 이것은 부모님을 위한 선물이에요."),
]
_CV_SINO = [("예보", "(豫報) (weather) forecast", "예약, 예매, 예방, 보고서, 경보, 속보"), ("폭우", "(暴雨) a rainstorm", "폭염, 폭설, 폭풍, 강우량, 우박, 우산"), ("지진", "(地震) an earthquake", "지하, 진원지, 지도, 진동, 지형, 강진")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_LOAN}
_EXTRA = {"강수량 / 강우량": "the amount of rainfall; precipitation", "~가량": "approximately, about", "기록(적)": "record (-breaking)", "~ 만에": "for the first time in [time]", "(무)더위": "a heat spell", "점차(적으로)": "gradually", "천둥": "thunder", "구호(물)품": "relief items", "홍수 / 물난리": "a flood", "지진해일 / 쓰나미": "a tsunami", "~철": "a ~ season", "물결이 일다": "waves rise"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_YB = [("예매", "advanced purchase"), ("특보", "special report")]
_YG = [("예약", "a reservation; an appointment"), ("예매", "advance purchase (of tickets)"), ("예방", "prevention"), ("보고서", "a written report"), ("보도", "a news report"), ("속보", "breaking news; a flash report")]
_UB = [("폭설", "snowstorm; blizzard; “violent snow”"), ("폭풍", "windstorm; a gust; “violent wind”"), ("폭등", "a sudden jump; a sharp rise; “fierce rise”")]
_UW = [("우기", "the rainy season; “rainy period”"), ("우산", "an umbrella"), ("우비", "a rain outfit; rain gear"), ("우박", "hail; a hailstone"), ("강우량", "rainfall; “amount of descending rain”"), ("우천", "rainy weather; a rainy day; “rainy sky”")]
_JB = [("지각", "the crust of the earth"), ("지구", "the earth; the globe; “earth ball”"), ("지뢰", "a land mine"), ("천지", "heaven and earth; whole world"), ("지중해", "the Mediterranean Sea; “sea in the middle of earth”"), ("지도", "a map; “earth picture”"), ("지하도", "an underpass; “land below way”")]
_JW = [("강진", "a strong earthquake; a severe earthquake"), ("여진", "a minor shock following the main shock of an earthquake; “remaining tremor”"), ("진동", "a shock; a tremor; a quake"), ("뇌진탕", "the concussion of the brain")]

# ================================================================== L1
L1 = lesson(
    "Ch 39 · What the chapter teaches, 예보 (豫報) · 폭우 (暴雨) · 지진 (地震)",
    "자연재해 · 예보 · 예약 · 예방 · 폭우 · 우산 · 지진 · 여진",
    requires=[],
    cards=[
        card("What Chapter 39 teaches (자연재해)",
             "Chapter 39, “Natural Disasters”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: comprehend weather forecasts and talk about suitable activities for varying weather conditions; extract information about natural hazards (flood, earthquake, landslide, etc.) and extreme weather (drought, blizzard), and discuss the disasters caused by them; identify different types of natural disasters and the causes, damages, and casualties associated with them; and report about and describe natural disasters, including the causes, damages, and casualties.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; question words used as indefinite pronouns; a noun clause in an appositive relationship; a question word + (이)나/(이)든지; ~에 관해서/관하여 vs. ~에 관한 (about; regarding; concerning); ~을/를 위해서/위하여 vs. ~을/를 위한 (for the sake of; for); and the Sino-Korean syllables within 예보 (豫報), 폭우 (暴雨), and 지진 (地震)."),
        card("Sino-Korean in use: 예보 (豫報)",
             "The syllable 예 (豫) means beforehand or in advance, as in 예매 (advanced purchase); 보 (報) means report, as in 특보 (special report). Thus, the literal meaning of this Sino-Korean word is “report (on something) in advance”, and the word refers to a (weather) forecast. The book asks you to guess the meaning of 예약, 예매, 예방, 보고서, 보도 and 속보 (my answers are in the table).",
             tables=[ktable(_YB), ktable(_YG)]),
        card("Sino-Korean in use: 폭우 (暴雨)",
             "This Sino-Korean word means rainstorm or sudden and heavy rain. The first syllable 폭 (暴) means fierce or violent, as in 폭설 (snowstorm; blizzard; “violent snow”), 폭풍 (windstorm; a gust; “violent wind”), and 폭등 (a sudden jump; a sharp rise; “fierce rise”). The second syllable 우 (雨) means rain, as in 우기 (the rainy season; “rainy period”), 우산 (an umbrella), 우비 (a rain outfit; rain gear), 우박 (hail; a hailstone), 강우량 (rainfall; “amount of descending rain”), and 우천 (rainy weather; a rainy day; “rainy sky”). Thus the literal meaning of the word 폭우 is “fierce rain” or “violent rain”, and the word refers to a storm with rain.",
             tables=[ktable(_UB), ktable(_UW)]),
        card("Sino-Korean in use: 지진 (地震)",
             "This Sino-Korean word means an earthquake. The first syllable 지 (地) means earth or land, as in 지각 (the crust of the earth), 지구 (the earth; the globe; “earth ball”), 지뢰 (a land mine), 천지 (heaven and earth; whole world), 지중해 (the Mediterranean Sea; “sea in the middle of earth”), 지도 (a map; “earth picture”), and 지하도 (an underpass; “land below way”). The second syllable 진 (震) means tremor or shock, as in 강진 (a strong earthquake; a severe earthquake), 여진 (a minor shock following the main shock of an earthquake; “remaining tremor”), 진동 (a shock; a tremor; a quake), and 뇌진탕 (the concussion of the brain). Thus the literal meaning of the word 지진 is “earth tremor” or “earth shock”.",
             tables=[ktable(_JB), ktable(_JW)]),
    ],
    exercises=uniq(
        _tr(_YG + _UB + _UW + _JB + _JW, k=3)
        + [M("What does 예 (豫) mean?", "beforehand; in advance", ["rain", "earth", "violent"], "예매."), M("What does 보 (報) mean?", "report", ["rain", "earth", "tremor"], "특보."), M("What does 우 (雨) mean?", "rain", ["snow", "earth", "report"], "우산."), M("What does 지 (地) mean?", "earth; land", ["rain", "tremor", "report"], "지구."), M("What does 진 (震) mean?", "tremor; shock", ["rain", "earth", "report"], "여진."), M("What is the literal meaning of 예보?", "“report in advance”", ["“violent rain”", "“earth tremor”", "“windstorm”"], "예 + 보."), M("What is the literal meaning of 폭우?", "“fierce rain” or “violent rain”", ["“report in advance”", "“earth tremor”", "“violent snow”"], "폭 + 우."), M("What is the literal meaning of 지진?", "“earth tremor” or “earth shock”", ["“violent rain”", "“report in advance”", "“earth ball”"], "지 + 진."), M("What is 폭설 literally?", "“violent snow”", ["“violent wind”", "“violent rain”", "“cold wave”"], "폭 + 설."),
           F("내일 날씨 ___를 보고 우산을 가져가세요. (forecast)", "예보", ["경보", "보도"], "예보."), F("비가 많이 와서 ___을 썼어요. (umbrella)", "우산", ["우비", "우박"], "우산."), F("지진 후에 ___이 계속되고 있다. (aftershocks)", "여진", ["강진", "진동"], "여진."), F("어제 ___이 내려서 길이 막혔다. (heavy snowfall)", "폭설", ["폭풍", "폭우"], "폭설."), F("한국 ___를 보면서 여행 계획을 세웠다. (map)", "지도", ["지구", "지각"], "지도."),
           read_q("예보"), read_q("폭우"), read_q("지진"), read_q("우산"), read_q("여진")]
    ),
)

# ================================================================== L2 Vocabulary builder
_NV = [("폭우주의보(가)", "발령되다", "a heavy rain advisory is issued"), ("소나기(가)", "내리다", "rain showers; “showers come down”"), ("전기공급(이)", "중단되다", "electricity supply is cut off"), ("물결이", "일다", "waves rise"), ("파도(가)", "치다", "high waves; “waves strike”"), ("한파(가)", "몰아치다", "a cold snap (“wave”) strikes"), ("항공기(가)", "결항되다", "flight is cancelled")]
_LM = [("폭설", "violent snow", "blizzard"), ("실종", "losing track", "missing"), ("매몰", "burying + submerged", "burying"), ("대피", "waiting + avoiding", "taking shelter"), ("수재민", "water + disaster + people", "flood victims"), ("구호품", "save + aid + items", "relief items"), ("산사태", "mountain + sand + overflow", "landslide"), ("일기예보", "daily weather + beforehand + report", "weather forecast")]
_A1 = [("날씨나 기온을 미리 알려줍니다.", "일기예보", "It tells the weather or temperature in advance."), ("홍수로 피해를 본 사람들입니다.", "수재민", "They are the people who suffered damage from a flood."), ("사람이 없어졌습니다.", "실종", "A person has disappeared."), ("눈이 아주 많이 내렸습니다.", "폭설", "A lot of snow fell."), ("비가 아주 많이 왔습니다.", "폭우", "A lot of rain fell."), ("오랫동안 비가 오지 않아 날씨가 건조합니다.", "가뭄", "It has not rained for a long time and the weather is dry."), ("전기가 나갔습니다.", "정전", "The electricity went out.")]
_DIS = [("홍수", "a flood"), ("태풍", "a typhoon"), ("산사태", "a landslide"), ("지진", "an earthquake")]
L2 = lesson(
    "Ch 39 · Vocabulary Builder: weather phrases, literal meanings and clue sentences",
    "폭우주의보가 발령되다 · 소나기가 내리다 · 한파가 몰아치다 · 항공기가 결항되다 · 폭설 · 실종 · 매몰 · 대피 · 수재민 · 구호품 · 산사태 · 일기예보",
    requires=[],
    cards=[
        card("새 단어: matching nouns, verbs and meanings",
             "The book asks you to skim the nouns, find the verb that goes with each, and match the English meaning. My answers (the English meanings are the book’s):",
             tables=[table(["Noun", "Verb (mine)", "English meaning"], [[a, b, c] for a, b, c in _NV], say=[0, 1])]),
        card("새 단어: literal and actual meanings",
             "The book asks you to guess the literal meaning of each word from its syllables and match it with the actual meaning. My answers (the literal meanings and actual meanings are the book’s choices):",
             tables=[table(["Word", "Literal meaning", "Actual meaning"], [[a, b, c] for a, b, c in _LM], say=[0])]),
        card("Activity 1: clue sentences",
             "The book gives eight words (정전, 일기예보, 폭설, 수재민, 실종, 가뭄, 폭우, 습도; one does not match) and seven sentences; you write the word for each. The sentences are the book’s; the answers and the English are mine (습도 is not used).",
             examples=passage([(a, c) for a, b, c in _A1]),
             tables=[table(["Sentence", "Word (mine)"], [[a, b] for a, b, c in _A1], say=[0, 1])]),
        card("Activity 2: four natural disasters (the book shows pictures)", "The words for the four pictures, with my meanings:", tables=[ktable(_DIS)]),
        card("Activities left out", "Activity 2 Step b (listening to four narrations and matching them with the pictures), Activity 3 and 4 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 5 (Peril!, a PowerPoint game) are audio, picture and game activities."),
    ],
    exercises=uniq(
        _tr(_DIS, k=3) + _tr([(a, c) for a, b, c in _A1], k=3)
        + [M("Which verb goes with 폭우주의보?", "발령되다", ["결항되다", "일다", "치다"], "My answer."), M("Which verb goes with 항공기?", "결항되다", ["발령되다", "중단되다", "내리다"], "My answer."), M("Which verb goes with 한파?", "몰아치다", ["일다", "내리다", "치다"], "My answer."), M("Which verb goes with 전기공급?", "중단되다", ["일다", "내리다", "몰아치다"], "My answer."), M("Which verb goes with 소나기?", "내리다", ["일다", "치다", "결항되다"], "My answer."), M("What does 매몰 mean?", "burying", ["missing", "taking shelter", "relief items"], "The book’s match."), M("What does 대피 mean?", "taking shelter", ["burying", "missing", "blizzard"], "The book’s match."), M("What does 구호품 mean?", "relief items", ["flood victims", "landslide", "blizzard"], "The book’s match."), M("What does 산사태 mean?", "landslide", ["blizzard", "missing", "flood victims"], "The book’s match."), M("Which word is not used in Activity 1?", "습도", ["정전", "가뭄", "폭우"], "My answer."),
           F("오랫동안 비가 오지 않아 날씨가 건조합니다. = ___ (drought)", "가뭄", ["폭우", "정전"], "가뭄."), F("전기가 나갔습니다. = ___ (power outage)", "정전", ["가뭄", "실종"], "정전."), F("홍수로 피해를 본 사람들입니다. = ___ (flood victims)", "수재민", ["이재민", "생존자"], "수재민."), F("눈이 아주 많이 내렸습니다. = ___ (heavy snowfall)", "폭설", ["폭우", "한파"], "폭설."), F("사람이 없어졌습니다. = ___ (missing)", "실종", ["매몰", "대피"], "실종."),
           read_q("폭우주의보가 발령되다"), read_q("한파가 몰아치다"), read_q("항공기가 결항되다"), read_q("산사태"), read_q("일기예보")]
    ),
)

# ================================================================== L3 Topic A
_A_TXT = [
    ("중부지방은 오늘도 맑고 덥겠습니다.", "The central region will be clear and hot again today."),
    ("하지만, 남부지방은 북상하는 장마전선의 영향을 받겠습니다.", "But the southern region will be affected by the monsoon front moving northward."),
    ("하늘이 점차 흐려지겠고, 오후 늦게나 밤늦게 제주도와 전남지방에는 비가 내릴 것으로 보입니다.", "The sky will gradually become cloudy, and rain is expected in Jeju Island and the Jeonnam region late in the afternoon or late at night."),
    ("주말에는 이 비가 전국으로 확산되겠는데요.", "This rain will spread across the whole country on the weekend."),
    ("주로 남부지방에 많은 비가 집중되겠습니다.", "Heavy rain will be concentrated mainly in the southern region."),
    ("우선 오늘 밤까지 제주 산간에는 최고 백오십 밀리미터가량의 큰 비가 예상되고, 전남지방에도 최고 백 밀리미터가 내릴 전망입니다.", "First, until tonight, heavy rain of up to about 150 mm is expected in the mountainous area of Jeju, and up to 100 mm is expected to fall in the Jeonnam region as well."),
]
_WEATH = [("맑음", "clear"), ("구름", "clouds"), ("비", "rain"), ("눈", "snow"), ("바람", "wind"), ("안개", "fog"), ("천둥", "thunder"), ("번개", "lightning")]
_REG = [("영동", "Yeongdong (the eastern side of the Gangwon-do mountains)"), ("영서", "Yeongseo (the western side)"), ("강원도", "Gangwon-do"), ("울릉도", "Ulleungdo"), ("서울", "Seoul"), ("경기", "Gyeonggi"), ("충북", "Chungbuk (North Chungcheong)"), ("충남", "Chungnam (South Chungcheong)"), ("경북", "Gyeongbuk (North Gyeongsang)"), ("영남지방", "the Yeongnam region (the southeast)"), ("전북", "Jeonbuk (North Jeolla)"), ("호남지방", "the Honam region (the southwest)"), ("경남", "Gyeongnam (South Gyeongsang)"), ("전남", "Jeonnam (South Jeolla)"), ("제주도", "Jeju Island")]
_A_WORDS = ["가뭄", "건조", "경보", "고기압", "몰아치다", "발령", "북상", "산간", "소나기", "예년", "예보", "장마전선", "적설량", "전국적", "주의보", "집중", "폭설", "한파", "해상", "확산", "현상", "늦다"]
_DRO = [("지난 겨울부터 올해 봄까지의 강수량이 평년보다 적어 전국적으로 가뭄 현상이 심각한 것으로 나타났습니다.", "It was found that, as the precipitation from last winter to this spring was less than in an average year, the drought phenomenon is serious nationwide."), ("특히 영동 지방은 예년의 오십 퍼센트만 비가 내려 다른 지역에 비해 가뭄이 심한 것으로 조사됐습니다.", "In particular, the Yeongdong region received only 50 percent of the rain of a normal year, and the drought was found to be severe compared with other regions."), ("기상청은 중국에서 발생한 건조한 고기압이 우리나라로 이동하면서 건조한 날씨가 계속되고 있다고 밝혔습니다.", "The Korea Meteorological Administration said that dry weather is continuing as a dry high-pressure system that arose in China moves to Korea."), ("이에 따라 서울 경기와 충청 지방의 강수량이 평년에 비해 칠십 퍼센트 정도이고, 특히 강릉 지역은 평년에 비해 강수량이 이십팔 퍼센트로 가뭄이 심한 것으로 나타났습니다.", "Accordingly, the precipitation of the Seoul-Gyeonggi and Chungcheong regions is about 70 percent compared with an average year, and in particular the Gangneung area’s precipitation is 28 percent compared with an average year, so the drought is found to be severe.")]
L3 = lesson(
    "Ch 39 · Topic A: Today’s weather (오늘의 날씨입니다)",
    "오늘의 날씨입니다 · 장마전선 · 북상 · 주의보와 경보 · 날씨 단어 · 한국의 지역 · 가뭄 기사",
    requires=[],
    cards=[
        card("Topic A: Today’s weather (오늘의 날씨입니다)",
             "The following weather forecast is from a news broadcast. (The English is mine; the book gives none; the numbers are spelled out in Hangul and mm is read 밀리미터. The book’s footnote says the ending in 확산되겠는데요 is the conjunctive ending –는데 + 요.)",
             examples=passage(_A_TXT)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists 강수량/강우량, 기록(적/하다), ~만에, (무)더위, 물결이 일다, 점차(적으로) and 천둥(치다).",
             tables=[ktable(_rows(_A_WORDS)), table(["Word", "Meaning"], [["~가량", "(假量) approximately, about"], ["강수량 / 강우량", "the amount of rainfall; precipitation"], ["기록(적)", "record (-breaking); to record (~하다)"], ["~ 만에", "for the first time in [time]; after the lapse [of time]"], ["(무)더위", "a (sweltering) heat spell; mugginess"], ["물결이 일다", "waves rise"], ["점차(적으로)", "gradually"], ["천둥(치다)", "thunder; to thunder"]], say=[0])]),
        card("Weather words and the regions of Korea",
             "The book lists the weather words 맑음, 구름, 비, 눈, 바람, 안개, 천둥, 번개 and a map of the regions of Korea (the map is a picture; the names are the book’s; the English is mine).",
             tables=[ktable(_WEATH), ktable(_REG)]),
        card("한국어에는: 주의보 and 경보",
             "The words 주의보 (an advisory) and 경보 (a warning) are often found in a weather report or forecast. 기상청 (Korea Meteorological Administration) issues 주의보 or 경보, depending on the severity of the expected weather condition. For example, if it is expected to snow more than 5 centimeters within 24 hours, a 폭설주의보 is issued; if it is expected to snow more than 20 centimeters, a 폭설경보 is issued. 주의보 or 경보 can be attached to nouns referring to extreme weather conditions, such as 태풍, 폭풍, 폭설, 호우, 황사, etc.; for example 태풍주의보 (a typhoon advisory) and 황사경보 (a yellow dust warning)."),
        card("Follow-up 2 (Reading): a news article about extreme weather",
             "The following news article is about extreme weather (the book glosses 평년: an average year; a regular year). The article is the book’s with the percentages spelled out; the English is mine.",
             examples=passage(_DRO)),
        card("The headline and table (mine)",
             "The book asks you to circle the headline that fits the article from four choices (1. Nationwide drought, Yeongdong region especially severe; 2. Nationwide average precipitation increases; 3. Dry weather because of the influence of low pressure; 4. Seoul-Gyeonggi and Chungcheong regions, severe drought) and to fill in a table. My answers:",
             tables=[table(["Item", "Answer (mine)"], [["Headline", "1. Nationwide drought, Yeongdong region especially severe (the article says it is nationwide, with Yeongdong the worst)"], ["영동", "Only 50 percent of a normal year’s rain; the drought is more severe than in other regions"], ["서울 경기 / 충청", "Precipitation about 70 percent of an average year"], ["강릉", "Precipitation only 28 percent of an average year; the drought is severe"]])]),
        card("Activities left out", "The presentation steps of Topic A (brainstorming vocabulary, studying the map, SMART Board activities and the video), Follow-up 1 (listening to a forecast and writing the weather for each region of the map) and Follow-up 3 (listening to a news clip on extreme weather and filling in type, region and tomorrow’s forecast) are audio, video and picture activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + vocab_exercises(_WEATH) + _tr(_REG, k=3) + _tr(_A_TXT + _DRO, k=3)
        + [M("What is the weather in the central region today?", "Clear and hot", ["Rainy", "Snowy", "Foggy"], "맑고 덥겠습니다."), M("What affects the southern region?", "The monsoon front moving northward", ["A typhoon", "A cold snap", "Yellow dust"], "북상하는 장마전선."), M("Where will rain fall late today?", "Jeju Island and Jeonnam", ["Seoul", "Gangwon", "Busan"], "제주도와 전남지방."), M("Where will the heavy rain be concentrated?", "The southern region", ["The central region", "Gangwon", "Seoul"], "남부지방에 집중."), M("What is a 폭설주의보 issued for?", "Expected snow of more than 5 cm in 24 hours", ["More than 20 cm in a day", "Rain", "Wind"], "The book’s note."), M("Which is more severe, 주의보 or 경보?", "경보", ["주의보", "They are the same", "Neither"], "The book’s note."), M("Which region had only 28 percent of average precipitation?", "Gangneung", ["Seoul", "Yeongdong", "Chungcheong"], "강릉."), M("What caused the dry weather?", "A dry high-pressure system from China", ["A typhoon", "A low-pressure system", "A flood"], "중국에서 발생한 건조한 고기압."),
           F("오늘 오후에 ___으로 비가 내리겠습니다. (nationwide)", "전국적", ["점차", "집중"], "전국적."), F("기상청에서 태풍___를 발령했으니까 조심하세요. (advisory)", "주의보", ["경보", "예보"], "주의보."), F("하늘이 ___ 흐려지겠습니다. (gradually)", "점차", ["점점", "전국적"], "점차."), F("북상하는 ___의 영향으로 비가 예상됩니다. (monsoon front)", "장마전선", ["고기압", "한파"], "장마전선."), F("봄에는 ___한 날씨 때문에 산불이 자주 납니다. (dry)", "건조", ["집중", "확산"], "건조."),
           read_q("오늘의 날씨입니다"), read_q("남부지방은 북상하는 장마전선의 영향을 받겠습니다"), read_q("하늘이 점차 흐려지겠습니다"), read_q("주로 남부지방에 많은 비가 집중되겠습니다"), read_q("전국적으로 가뭄 현상이 심각합니다")]
    ),
)

# ================================================================== L4 Topic A activities
_FC = [("이십일 일은 전국이 고기압의 가장자리에 들면서 중부지방은 구름이 많겠다.", "On the 21st, as the whole country comes under the edge of a high-pressure system, the central region will have many clouds."), ("서울과 경기도, 강원도 북부에서는 오전이나 낮에 한 때 비, 강수확률 사십 퍼센트, 가 조금 오는 곳이 있겠고 그밖의 지방은 대체로 맑겠다.", "In Seoul, Gyeonggi-do and northern Gangwon-do, there will be places with a little rain at times in the morning or daytime (40 percent chance of precipitation), and other regions will be mostly clear."), ("아침 최저기온은 섭씨 팔 도에서 십칠 도, 낮 최고기온은 십구 도에서 이십구 도가 되겠으며 바다의 물결은 서해 중부 바다와 동해 중부 바다에서 오후에 일 점 오 미터에서 이 점 오 미터로 점차 높게 일고 그밖의 해상에서는 영 점 오 미터에서 이 미터로 일겠다.", "The morning low will be 8 to 17 degrees Celsius and the daytime high 19 to 29 degrees, and the waves at sea will gradually rise to 1.5 to 2.5 m in the afternoon in the central West Sea and central East Sea, and to 0.5 to 2.0 m in other seas.")]
_FCT = [("백령도 (서해 중부 바다)", "Waves rising gradually to 1.5–2.5 m in the afternoon"), ("울릉도 (동해 중부 바다)", "Waves rising gradually to 1.5–2.5 m in the afternoon"), ("인천 (경기도)", "A little rain at times in the morning or daytime (40 percent chance of precipitation)"), ("광주", "Mostly clear")]
_LIV = [("우산 70", "잊지 말고 우산을 가져가세요.", "Don’t forget to take an umbrella."), ("세차 20", "오늘은 세차하기에 안 좋은 날이에요. 다음에 하세요.", "Today is not a good day to wash the car. Do it next time."), ("외출 30", "외출하기에 별로 안 좋은 날이에요.", "It is not a very good day to go out."), ("운동 30", "운동은 실내에서 하세요.", "Exercise indoors."), ("우산 20", "우산 가져갈 필요가 없어요.", "There is no need to take an umbrella."), ("세차 100", "오늘은 세차하기 좋은 날이에요.", "Today is a good day to wash the car."), ("외출 70", "오늘은 외출하기에 좋은 날이에요.", "Today is a good day to go out."), ("운동 60", "밖에서 운동하기 좋은 날이에요.", "It is a good day to exercise outside.")]
_SEA = [("기상청의 발표에 의하면 우리나라의 사계절이 바뀌고 있다.", "According to the Korea Meteorological Administration’s announcement, Korea’s four seasons are changing."), ("백여 년 전에는 겨울이 가장 긴 계절이었지만 최근에는 여름이 가장 길어졌다.", "More than 100 years ago winter was the longest season, but recently summer has become the longest."), ("한반도의 연평균 기온은 과거에 비해 최근 일 점 육 도 올랐다.", "The annual average temperature of the Korean peninsula has risen 1.6 degrees recently compared with the past."), ("기후변화로 인한 지구 온난화 양상이 뚜렷하게 나타나는 것이다.", "The pattern of global warming caused by climate change is clearly showing."), ("기온이 오르면서 계절의 길이가 달라졌다.", "As the temperature rose, the length of the seasons changed."), ("과거에는 겨울이 백구 일로 가장 길었고, 그 뒤 여름 구십팔 일, 봄 팔십오 일, 가을 칠십삼 일 순이었다.", "In the past winter was the longest at 109 days, followed by summer (98 days), spring (85 days) and autumn (73 days)."), ("그러나 최근에는 여름이 백십팔 일로 가장 길고 봄 구십일 일, 겨울 팔십칠 일, 가을 육십구 일 순으로 바뀌었다.", "But recently summer is the longest at 118 days, followed by spring (91 days), winter (87 days) and autumn (69 days)."), ("여름이 이십 일 길어지고 겨울은 이십이 일 짧아진 것이다.", "Summer has become 20 days longer and winter 22 days shorter.")]
L4 = lesson(
    "Ch 39 · Topic A activities: a forecast, the living index and four seasons",
    "일기예보 읽기 · 기온과 물결 · 생활지수 · 우산 세차 외출 운동 · 사계절의 변화 · 지구 온난화",
    requires=[],
    cards=[
        card("Activity 2 (Reading): a weather forecast for South Korea",
             "The following weather forecast is for South Korea. The book asks you to read it and write the weather information for the regions 백령도 (West Sea central sea), 울릉도 (East Sea central sea), 인천 (Gyeonggi-do) and 광주 in English (one is done for you: “Mostly clear”). The forecast is the book’s with the numbers spelled out (the range “8 ~ 17도” is read “8도에서 17도” or “8도 내지 17도”, as the book notes); the English is mine.",
             examples=passage(_FC)),
        card("The regions filled in (mine)", "My answers:", tables=[table(["Region", "Weather information (mine)"], [[a, b] for a, b in _FCT], say=[0])]),
        card("Activity 3 (Listening and reading): the living index (생활지수)",
             "The book’s footnote: 생활지수 (“living index”) means the possibility (0–100%) of being able to do a particular activity, given the weather conditions. For example, the possibility of washing a car would be 20% if the 세차지수 indicates 20%. This means the day is not ideal for washing a car. The higher the number, the greater the likelihood of being able to do a particular activity.\n\n"
             "The book gives two tables for 오늘의 생활지수 (the 23rd, Tuesday) from Yonhap News, one for 중부 and one for 남부, and asks you to identify which is which (this depends on the audio). The first four rows are the lower-index table and the last four the higher-index table; the English is mine (the book glosses 우산: an umbrella).",
             tables=[table(["Index", "Advice", "English (mine)"], [[a, b, c] for a, b, c in _LIV], say=[1])]),
        card("Activity 4 (Reading): the four seasons in Korea",
             "The following text is about four seasons in Korea (the book glosses 지구 온난화: global warming). The text is the book’s with the numbers spelled out (the days in the book’s brackets are set off by commas); the English is mine.",
             examples=passage(_SEA)),
        card("The answer (mine)", "The book asks: What is said about the four seasons in Korea, and what is behind this? My answers:",
             tables=[table(["Item", "Answer (mine)"], [["100 years ago", "Winter was longest (109 days), then summer (98), spring (85), autumn (73)"], ["Recent years", "Summer is longest (118 days), then spring (91), winter (87), autumn (69)"], ["The cause", "Climate change and global warming: the annual average temperature rose 1.6 degrees"]])]),
        card("Activities left out", "Activity 1 (SMART Board), the sound parts of Activity 3 (a YTN weather forecast video, a map exercise and translating two sentences heard from the forecast) and Activity 5 (acting as a meteorologist: collecting a three-day forecast and living-index information from a website and presenting a script) need video, a map, a website and a partner."),
    ],
    exercises=uniq(
        _tr(_FC + _SEA, k=3) + _tr([(b, c) for a, b, c in _LIV], k=3)
        + [M("What will the weather in 인천 be?", "A little rain at times in the morning or daytime", ["Heavy snow", "A typhoon", "Mostly clear all day"], "한 때 비가 조금."), M("How high will the waves rise in the central West Sea?", "1.5 to 2.5 m", ["0.5 to 2.0 m", "5 m", "10 m"], "일 점 오 미터에서 이 점 오 미터."), M("What does a 세차지수 of 20 mean?", "It is not a good day to wash the car", ["It is a perfect day", "It will rain", "It is windy"], "The book’s note."), M("What does a higher living index number mean?", "A greater likelihood of being able to do the activity", ["A lower likelihood", "More rain", "Colder weather"], "The book’s note."), M("Which season was the longest 100 years ago?", "Winter", ["Summer", "Spring", "Autumn"], "겨울이 가장 긴 계절."), M("Which season is the longest recently?", "Summer", ["Winter", "Spring", "Autumn"], "여름이 가장 길어졌다."), M("How much has summer lengthened?", "20 days", ["22 days", "5 days", "1 day"], "여름이 이십 일 길어지고."), M("What is behind the change?", "Global warming from climate change", ["A calendar change", "More typhoons", "A longer winter"], "기후변화로 인한 지구 온난화."),
           F("낮 최고기온은 십구 도에서 이십구 도가 ___ 습니다. (will be)", "되겠", ["되었", "됩니"], "되겠습니다."), F("잊지 말고 ___을 가져가세요. (umbrella)", "우산", ["세차", "운동"], "우산."), F("운동은 ___에서 하세요. (indoors)", "실내", ["밖", "해상"], "실내."), F("한반도의 연평균 ___이 올랐다. (temperature)", "기온", ["강수량", "습도"], "기온."), F("겨울은 이십이 일 ___ 것이다. (became shorter)", "짧아진", ["길어진", "추워진"], "짧아진."),
           read_q("일기예보"), read_q("잊지 말고 우산을 가져가세요"), read_q("운동은 실내에서 하세요"), read_q("지구 온난화"), read_q("여름이 가장 길어졌다")]
    ),
)

# ================================================================== L5 Topic B
_B_DLG = [
    ("사회자", "안녕하세요? 정 기자님, 요즘 세계 여러 곳에서 이상기후가 나타나면서 많은 자연재해가 발생하고 있는데요. 우리나라도 날씨가 점점 이상해지고 있는 것 같죠?", "Hello? Reporter Chung, as abnormal weather is appearing in many parts of the world these days, many natural disasters are occurring. It seems Korea’s weather too is getting stranger, doesn’t it?"),
    ("기자", "네, 맞습니다. 얼마 전까지는 전국적으로 건조한 날씨 때문에 산불이 자주 발생한다는 이야기를 들었는데요. 지난주부터는 갑자기 태풍이 오고 폭우도 쏟아지고 있습니다.", "Yes, that’s right. Until a while ago I heard that wildfires were occurring often because of the dry weather nationwide, but since last week suddenly a typhoon has come and a heavy rain is pouring."),
    ("사회자", "비가 오면서 다행히 가뭄은 해소됐지만, 이제는 반대로 홍수나 침수 걱정을 하게 되었네요. 그리고 올해는 예년보다 집중호우가 더 일찍 내려서 큰 피해를 주고 있다고요? 어떤 피해들이 있나요?", "Fortunately the drought has been relieved with the rain, but now on the contrary we have come to worry about floods and flooding. And this year the concentrated heavy rain came earlier than usual and is causing great damage? What kind of damage is there?"),
    ("기자", "네, 경기 지역에서는 도로가 물에 잠기고 자동차가 떠내려가기도 했습니다. 그리고 강원도 산간 지역에서는 산사태로 도로가 폐쇄된 곳도 있습니다.", "Yes, in the Gyeonggi area roads were submerged and cars were even swept away. And in the mountainous area of Gangwon-do there are places where roads were closed because of landslides."),
    ("사회자", "기후 변화가 가져오는 재해가 정말 무섭군요. 지금은 비가 그쳤지만 다음 주부터 다시 비가 온다는 일기예보도 있습니다.", "The disasters brought by climate change are really frightening. The rain has stopped now, but there is also a forecast that rain will come again from next week."),
    ("기자", "네, 그래서 걱정이 많이 됩니다. 지금도 많은 수재민들이 불편을 겪고 계시는데요. 하루빨리 복구 작업이 끝나서 더 큰 피해가 나지 않기를 바랍니다.", "Yes, so I am very worried. Even now many flood victims are going through inconvenience. I hope the restoration work ends as soon as possible so that no greater damage occurs."),
]
_B_WORDS = ["겪다", "결항", "구간", "그치다", "나타나다", "떠내려가다", "마비", "복구", "산사태", "수재민", "쏟아지다", "얼다", "이상기후", "작업", "잠기다", "장마", "재해", "점점", "정전", "중단", "추위", "침수", "태풍", "폭염", "폭우", "호우", "폐쇄"]
_NK = [("북한지역에도 집중호우가 내려 홍수 피해가 발생했다.", "Concentrated heavy rain fell in the North Korean area too, causing flood damage."), ("평양방송은 지난 십구 일 평양에 백일 밀리미터에서 삼백이 밀리미터의 폭우가 내렸으며, 평안남북도와 자강도, 함경남도, 강원도 지역에서도 많은 비가 내렸다고 전했다.", "Pyongyang Broadcasting reported that on the 19th a heavy rain of 101 to 302 mm fell in Pyongyang and that much rain also fell in the areas of South and North Pyongan, Jagang, South Hamgyong and Gangwon."), ("특히 개성 지역에는 팔 월 평균 강우량 이백칠십오 점 칠 밀리미터의 육십오 퍼센트에 달하는 약 사백이십사 밀리미터의 호우가 최근 닷새간 집중적으로 쏟아진 것으로 집계됐다.", "In particular, in the Kaesong area a heavy rain of about 424 mm, amounting to 65 percent of the August average rainfall (275.7 mm), was tallied as having poured down intensively over the last five days."), ("북한은 이천칠 년 팔 월에도 집중호우 때문에 오백여 명이 사망하거나 실종되었으며, 구십만 명의 수재민이 발생했었다.", "In August 2007 as well, because of concentrated heavy rain, more than 500 people in North Korea died or went missing, and 900,000 flood victims occurred."), ("그리고 이천육 년 칠 월에도 홍수 피해 때문에 팔백사십사 명의 사망자와 실종자가 나왔다.", "And in July 2006 too, 844 dead and missing came out because of flood damage."), ("또한 이만 팔천여 명의 수재민이 발생했으며, 이만 삼천여 가구가 침수됐다.", "In addition, more than 28,000 flood victims occurred, and more than 23,000 households were flooded.")]
_BUS = [("칠 일하고 팔 일에 부산에 비가 너무 많이 내렸다.", "On the 7th and 8th it rained too much in Busan."), ("그래서 홍수가 났다.", "So a flood occurred."), ("오늘까지 스물일곱 명이 죽고 스무 명이 다쳤다.", "As of today 27 people have died and 20 have been injured."), ("집 이백 채가 물에 잠겼다.", "Two hundred houses were submerged."), ("도로도 물에 잠겼다.", "Roads were submerged too."), ("이번 홍수 때문에 삼천 명이 집을 잃어서 우리 학교에서 살고 있다.", "Because of this flood 3,000 people lost their homes and are living at our school."), ("아직도 물에 잠긴 집에서 나오지 못한 사람들도 있다.", "There are still people who could not get out of their submerged houses."), ("부산 일일구 구조대가 그 사람들을 구조하고 있다.", "The Busan 119 rescue team is rescuing those people."), ("또 경찰은 고속도로도 막았다.", "The police also blocked the expressway."), ("사람이 더 다칠 수도 있다고 한다.", "They say more people may be injured."), ("재산 피해가 커질 것이라고 한다.", "They say the property damage will grow.")]
_BUSB = [("지난 칠 일, 팔 일 부산 지역에 내린 집중호우로 물난리가 발생해 스물일곱 명이 숨지고 스무 명이 부상을 입었다.", "Because of the concentrated heavy rain that fell in the Busan area on the 7th and 8th, a flood occurred and 27 people died and 20 were injured."), ("또한 주택 이백여 채가 침수되었으며 일부 도로도 물에 잠겼다.", "In addition, more than 200 houses were flooded and some roads were also submerged."), ("주택을 잃은 주민 삼천여 명은 수재민 수용소에서 대피 중이다.", "More than 3,000 residents who lost their homes are taking shelter at a flood victims’ camp."), ("부산시는 헬리콥터와 보트를 이용해 구조 작업을 계속하고 있다.", "The city of Busan is continuing rescue work using helicopters and boats."), ("또한 일부 고속도로도 통제하고 있다.", "It is also controlling some expressways."), ("인명 피해와 재산 피해가 계속해서 늘어날 것으로 보인다.", "Human casualties and property damage are expected to keep increasing.")]
L5 = lesson(
    "Ch 39 · Topic B: Climate change and natural disasters (기후변화와 자연재해)",
    "기후변화와 자연재해 · 이상기후 · 집중호우 · 수재민 · 복구 작업 · 한국의 여름 · 장마 · 피서 · 북한 홍수",
    requires=[],
    cards=[
        card("Topic B: Climate change and natural disasters (기후변화와 자연재해)",
             "The following text is an excerpt from a TV news program in which a news anchor is discussing the abnormal weather with a weather reporter. (The English is mine; the book gives none; the speaker labels 사회자 and 기자 are the book’s.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists –다는 (see the grammar), 홍수/물난리 and ~철.",
             tables=[ktable(_rows(_B_WORDS)), table(["Word", "Meaning"], [["홍수 / 물난리", "a flood; “big water”"], ["~철", "a ~ season"], ["-다는", "an appositive noun clause ending (see the grammar)"]], say=[0])]),
        card("한국에서는: summer in Korea (한국의 여름: 장마, 무더위, 태풍)",
             "Summer falls between June and August in Korea. During this season, the weather is hot and humid, with an average temperature of 78°F. The rainy season, called 장마(철), generally begins in late June and usually lasts until the end of July. During the summer and early fall, typhoons (태풍) frequently occur and bring more rainfall. After 장마 is over, scorching hot days continue until the end of August. Many Koreans take vacations during this time and go to the beaches or mountains to avoid the heat. This summer vacation is called 피서 (“avoiding the heat”), and those who are on 피서 are called 피서객."),
        card("Follow-up 1 (Reading): flood damage in North Korea",
             "Read the news article about a natural disaster in North Korea (the book glosses 실종: missing; 가구: a household). The article is the book’s with the numbers spelled out (the years are read 이천칠 년 and 이천육 년); the English is mine.",
             examples=passage(_NK)),
        card("The answers (mine)", "The book asks (1) what type of disaster is reported, (2) to check the affected regions on a map, (3) what is said about Kaesong, and (4) to fill in a table of year of flood, casualties and houses flooded. My answers:",
             tables=[table(["Question", "Answer (mine)"], [["1. Type of disaster", "A flood caused by concentrated heavy rain"], ["2. Regions affected", "Pyongyang, South and North Pyongan, Jagang, South Hamgyong, Gangwon (and Kaesong)"], ["3. Kaesong", "About 424 mm of heavy rain, 65 percent of the August average rainfall (275.7 mm), poured down over the last five days"], ["4. 2007", "More than 500 dead or missing; 900,000 flood victims; houses flooded: N/A"], ["4. 2006", "844 dead and missing; more than 28,000 flood victims; more than 23,000 households flooded"]])]),
        card("Activity 2 (Reading): Text A by an elementary school student",
             "The following texts are about the same natural disaster: Text A was written by an elementary school student and Text B by a newspaper reporter. The book asks you to fill in a table in English from Text A (type of disaster; date and place; cause; casualties; property damage; rescue team’s action), and then to underline the same information in Text B and number it. The texts are the book’s with the numbers spelled out (119 is read 일일구); the English is mine.",
             examples=passage(_BUS)),
        card("Text B by a newspaper reporter", "The book glosses 주민: a resident; 수용소: a camp. The text is the book’s with the numbers spelled out; the English is mine.", examples=passage(_BUSB)),
        card("The table filled in (mine)", "My answers:",
             tables=[table(["Information", "Answer (mine)"], [["1. Type of disaster", "A flood"], ["2. Date/Place", "The 7th and 8th, Busan"], ["3. Cause of disaster", "Too much (concentrated heavy) rain"], ["4. Casualties", "27 dead, 20 injured; 3,000 people lost their homes"], ["5. Property damage", "200 houses (and roads) submerged; damage expected to grow"], ["6. Rescue team’s action", "The 119 rescue team rescues people stuck in submerged houses (in Text B: helicopters and boats are used); the police blocked the expressway"]])]),
        card("Activities left out", "The presentation steps of Topic B (sentence strips, a SMART Board activity and reading the dialog in pairs), Follow-up 2 (listening to three news reports on extreme weather and filling in type, duration, consequences and casualties), Activity 1 (Let’s Circulate the Words, a card and wall activity), Activity 3 (two audio news reports on natural hazards, with their video and a table of region and consequences; the book glosses 순환로: circular road; 북적이다: crowded) and Activity 4 (researching a news article about a natural disaster in groups) are audio, video and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG), k=3) + _tr(_NK + _BUS + _BUSB, k=3)
        + [M("What disaster did the North Korea article report?", "A flood from heavy rain", ["An earthquake", "A typhoon", "A drought"], "홍수 피해."), M("How much rain fell in Kaesong over five days?", "About 424 mm", ["About 100 mm", "About 50 mm", "About 1,000 mm"], "약 사백이십사 밀리미터."), M("How many flood victims occurred in 2007?", "900,000", ["28,000", "500", "23,000"], "구십만 명."), M("When does the rainy season begin in Korea?", "Late June", ["Early April", "August", "December"], "The book’s note."), M("What is 피서?", "A summer vacation to avoid the heat", ["A winter sport", "A rainy season", "A typhoon"], "The book’s note."), M("How many people died in the Busan flood?", "27", ["20", "200", "3,000"], "스물일곱 명."), M("Where are the people who lost their homes living?", "At the school (a flood victims’ camp)", ["In hotels", "In tents on the beach", "At home"], "우리 학교에서 / 수재민 수용소."), M("What were the anchor’s concerns now?", "Floods and flooding", ["Drought", "Wildfires", "Snow"], "홍수나 침수 걱정."),
           F("비가 많이 와서 길이 물에 ___ (submerged)", "잠겼어요", ["얼었어요", "그쳤어요"], "잠기다."), F("홍수로 집이 ___. (swept away)", "떠내려갔습니다", ["얼었습니다", "그쳤습니다"], "떠내려가다."), F("태풍 때문에 비행기가 ___되었습니다. (canceled)", "결항", ["복구", "침수"], "결항."), F("피해 ___ 작업을 하고 있습니다. (restoration)", "복구", ["결항", "폐쇄"], "복구."), F("산사태로 도로가 ___된 곳도 있습니다. (closed)", "폐쇄", ["복구", "중단"], "폐쇄."),
           read_q("기후변화와 자연재해"), read_q("이상기후가 나타나고 있습니다"), read_q("집중호우가 더 일찍 내렸습니다"), read_q("산사태로 도로가 폐쇄되었습니다"), read_q("많은 수재민들이 불편을 겪고 있습니다")]
    ),
)

# ================================================================== L6 Grammar A: question words as indefinite pronouns
_IP = [("누구", "who; whom", "someone; somebody"), ("무엇 / 뭐", "what", "something"), ("언제", "when", "someday; sometime"), ("어디", "where", "someplace; somewhere"), ("어떻게", "how", "somehow"), ("어느 ~", "which ~", "some ~"), ("어떤 ~", "which ~", "some ~"), ("무슨 ~", "what ~", "some ~"), ("몇 ~", "how many ~", "some ~")]
_IP1 = [("지금 밖에 누가 있어요.", "Someone is at the door right now."), ("우리 언제 같이 점심 먹자.", "Let’s have lunch together sometime.")]
_IP2 = [("누가 밖에 왔어요?", "Who is at the door? or Is someone at the door?"), ("뭐를 먹고 싶으세요?", "What do you want to eat? or Do you want to eat something?")]
_IPD = [("A", "김 선생님, 어디 가세요?", "Mr. Kim, where are you going?"), ("B", "어디 가요.", "I am going somewhere.")]
_IPD2 = [("A", "김 선생님 어디 가세요?", "Are you going somewhere?"), ("B", "네, 어디 가요.", "Yes, I am going somewhere.")]
_IPM = [("누가 전화했어요.", "Somebody called."), ("어디에 가고 싶어요.", "I want to go somewhere."), ("무슨 일이 있어요?", "Is something the matter? / What is the matter?"), ("어떤 지역에서 큰 홍수가 났어요.", "A big flood occurred in some region.")]
L6 = lesson(
    "Ch 39 · Grammar A: question words used as indefinite pronouns",
    "누구 · 무엇 · 언제 · 어디 · 어떻게 · 어느 · 어떤 · 무슨 · 몇 · 누군가 · 어디 가요",
    requires=[],
    cards=[
        card("Indefinite pronouns",
             "Indefinite pronouns are pronouns that refer to unspecified beings, objects, places, etc. In English, someone, something, anyone, anything, nobody, and nothing are typical examples of indefinite pronouns. In Korean, however, some indefinite pronouns happen to be identical in form with the question words you have learned in earlier chapters (누구, 무엇/뭐, 언제, 어디, etc.). In other words, these words have dual meanings, depending on the context; they can be used as question words (who/whom, what, when, where, etc.) or as indefinite pronouns (someone, something, sometime, somewhere, etc.). The following table lists the words that can be used as question words or indefinite pronouns:",
             tables=[table(["Word", "As a question word", "As an indefinite pronoun"], [[a, b, c] for a, b, c in _IP], say=[0])]),
        card("In a non-question sentence",
             "When these words are used in a non-question sentence (statement, command, request, etc.), they always function as indefinite pronouns. For example (the English is the book’s):",
             examples=passage(_IP1)),
        card("In a question",
             "However, when they are used in a question, depending on the context, they function as either question words or indefinite pronouns. Thus, the following questions can be interpreted in two different ways (the English is the book’s):",
             examples=passage(_IP2)),
        card("Stress",
             "In spoken language, however, the speaker’s stress (or lack of stress) helps the listener interpret the meaning of the word. In other words, Koreans tend to stress the word when it is used as a question. The book gives two dialogs (audio) in which 어디 가세요? functions differently (the English is the book’s):",
             examples=dlg(_IPD) + dlg(_IPD2)),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_IPM)),
        card("Activities left out", "Follow-up 1 (reading a memo that Jaesuk’s older sister left on the kitchen table and circling the question words) and Follow-up 2 (listening to four short conversations between two school instructors and identifying the question word used) need the memo picture and audio."),
    ],
    exercises=uniq(
        _tr(_IP1 + _IP2 + _IPM, k=3) + _tr(_strip(_IPD) + _strip(_IPD2), k=2)
        + [M("What does 누구 mean in a non-question sentence?", "someone; somebody", ["who", "nobody", "everyone"], "The book’s note."), M("What does 언제 mean as an indefinite pronoun?", "someday; sometime", ["when", "always", "never"], "The book’s note."), M("What does 어디 mean as an indefinite pronoun?", "someplace; somewhere", ["where", "nowhere", "everywhere"], "The book’s note."), M("What does 무엇 mean as an indefinite pronoun?", "something", ["what", "nothing", "everything"], "The book’s note."), M("What does 어떻게 mean as an indefinite pronoun?", "somehow", ["how", "never", "always"], "The book’s note."), M("What does 몇 ~ mean as an indefinite pronoun?", "some ~", ["how many ~", "no ~", "every ~"], "The book’s note."), M("What helps a listener tell the question and indefinite meanings apart?", "The speaker’s stress", ["The word order", "The ending", "A particle"], "The book’s note."), M("In a non-question sentence the word is always…", "an indefinite pronoun", ["a question word", "a verb", "a particle"], "The book’s note."), M("What does 지금 밖에 누가 있어요 mean?", "Someone is outside right now", ["Who is outside?", "Nobody is outside", "I am outside"], "The book’s example."),
           F("우리 ___ 같이 점심 먹자. (sometime)", "언제", ["누구", "무엇"], "언제."), F("지금 밖에 ___ 있어요. (someone)", "누가", ["언제", "어디"], "누가."), F("김 선생님, ___ 가세요? (where)", "어디", ["누구", "언제"], "어디."), F("어떤 지역에서 큰 ___이 났어요. (flood)", "홍수", ["가뭄", "정전"], "홍수."), F("___ 일이 있으세요? (some/what)", "무슨", ["어떻게", "언제"], "무슨."),
           read_q("지금 밖에 누가 있어요"), read_q("우리 언제 같이 점심 먹자"), read_q("누가 밖에 왔어요"), read_q("뭐를 먹고 싶으세요"), read_q("김 선생님 어디 가세요")]
    ),
)

# ================================================================== L7 Grammar B: appositive noun clause
_AP1 = [("빅서에 산불이 났다는 소식", "the news that a wildfire occurred in Big Sur"), ("김 선생님이 결혼한다는 소문", "the rumor that Ms. Kim is getting married")]
_AP2 = [("내가 군인이라는 사실", "the fact that I am a serviceman"), ("내가 공군이 아니라는 말", "the talk that I am not an airman")]
_AP3 = [("서울에서 큰 교통사고가 났다는 뉴스를 들었습니까?", "Did you hear the news that a big traffic accident occurred in Seoul?"), ("산호세에 한국마켓이 많다는 사실을 알고 있습니까?", "Do you know that there are many Korean markets in San Jose?")]
_APM = [("중국에서 비행기가 추락했어요.", "중국에서 비행기가 추락했다", "중국에서 비행기가 추락했다는 뉴스", "중국에서 비행기가 추락했다는 뉴스를 보았어요?", "Did you see the news that a plane crashed in China?")]
_APN = [("사실", "fact"), ("소문", "rumor"), ("소식", "news"), ("뉴스", "news"), ("말", "talk; word"), ("이야기", "story"), ("보고", "report"), ("보도", "news report"), ("신문 기사", "newspaper article"), ("생각", "thought"), ("느낌", "feeling"), ("견해", "opinion"), ("고백", "confession")]
_APB = [("시장에서 화재가 났습니다.", "시장에서 화재가 났다는 소식을 들었어요.", "I heard the news that a fire broke out at the market."), ("쓰나미가 발생했어요.", "쓰나미가 발생했다는 뉴스를 보았어요.", "I saw the news that a tsunami occurred."), ("김 일병이 내년에 한국에 갑니다.", "김 일병이 내년에 한국에 간다는 소문을 들었어요.", "I heard the rumor that PFC Kim is going to Korea next year."), ("플로리다에 허리케인이 옵니다.", "플로리다에 허리케인이 온다는 소식을 들었어요.", "I heard the news that a hurricane is coming to Florida."), ("어머니가 간호사입니다.", "어머니가 간호사라는 사실을 알고 있어요.", "I know the fact that my mother is a nurse."), ("내일 시험 봅니다.", "내일 시험 본다는 소식을 들었어요?", "Did you hear the news that there is a test tomorrow?")]
L7 = lesson(
    "Ch 39 · Grammar B: a noun clause in an appositive relationship, –다는 + noun",
    "-다는 소식 · -다는 소문 · -(이)라는 사실 · 산불이 났다는 소식 · 내일 시험 본다는 소식",
    requires=[],
    cards=[
        card("The appositive",
             "An appositive is a noun, noun phrase, or noun clause that renames or defines another noun. For example, in the following English sentences the phrases in bold are appositives: “Michael Jackson, a famous singer, is no longer with us.” (a noun phrase) and “The rumor that Michael Jackson is still alive is groundless.” (a noun clause). Note that when a noun clause like “Michael Jackson is still alive” becomes an appositive, it begins with that."),
        card("In Korean",
             "In Korean, when a noun clause is in an appositive relationship, it ends with the blunt formal form –다, immediately followed by –는. For example (the English is the book’s; the book’s “Big Sur” is a place name):",
             examples=passage(_AP1)),
        card("이다 / 아니다", "When the verb of the noun clause is 이다 / 아니다, however, 이다 changes to (이)라 (the English is the book’s):", examples=passage(_AP2)),
        card("Expressing the noun clause in an appositive relationship", "formal blunt form + 는 + noun. More examples (the English is the book’s):", examples=passage(_AP3)),
        card("참고: nouns that take an appositive clause", "A noun clause is often in an appositive relationship with the following nouns:",
             tables=[ktable(_APN)]),
        card("Follow-up 3 (Listening and speaking): the model",
             "Partner A reads a sentence from Box A; Partner B turns it into a noun clause; Partner A chooses a noun from Box B and puts it with the noun clause; Partner B produces a complete sentence. The book’s model (the English is mine):",
             examples=dlg([("A", _APM[0][0], "A plane crashed in China."), ("B", _APM[0][1], "(A plane) crashed in China (noun clause)"), ("A", _APM[0][2], "the news that a plane crashed in China"), ("B", _APM[0][3], _APM[0][4])])),
        card("Box A and my sentences", "The book’s Box A has sentences such as 시장에서 화재가 났습니다, 쓰나미가 발생했어요 and 어머니가 간호사입니다, and Box B has the nouns 소식, 소문, 말, 사실, 이야기, TV 뉴스, 신문 기사, 이메일. My completed sentences (the English is mine):",
             tables=[table(["Box A sentence", "Appositive sentence (mine)", "English (mine)"], [[a, b, c] for a, b, c in _APB], say=[0, 1])]),
        card("Follow-up 5 (Speaking and listening): 내일 시험 본다는 소식 들었어?", "Think about a rumor, news story, or event your classmates might be interested in and ask at least three classmates whether they have heard about it by saying “…뉴스/소문을 들었어(요)?”. Then report the most interesting news you found to the class."),
        card("Activities left out", "Follow-up 4 (listening to four conversations between two friends and translating the sentence with an appositive) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_AP1 + _AP2 + _AP3 + [(b, c) for a, b, c in _APB], k=3) + _tr(_APN, k=3)
        + [M("How does a noun clause in an appositive relationship end?", "The blunt formal form –다 followed by –는", ["–고 있다", "–(으)ㄴ 채", "–아/어서"], "The book’s note."), M("What does 이다 change to in an appositive clause?", "(이)라", ["(이)고", "(이)면", "(이)지"], "The book’s note."), M("What does 산불이 났다는 소식 mean?", "the news that a wildfire occurred", ["the news of a fire drill", "a wildfire", "the cause of a wildfire"], "The book’s example."), M("What does 내가 군인이라는 사실 mean?", "the fact that I am a serviceman", ["the fact that I am not a serviceman", "my military service", "a soldier’s duty"], "The book’s example."), M("Which noun fits “that Ms. Kim is getting married”?", "소문", ["지도", "우산", "철"], "The book’s example."),
           F("김 선생님이 결혼한___ 소문 (the rumor that…)", "다는", ["는", "다고"], "-다는."), F("내가 군인이___ 사실 (the fact that I am…)", "라는", ["다는", "이라"], "이다 → (이)라는."), F("내가 공군이 아니___ 말 (the talk that I am not…)", "라는", ["다는", "라고"], "아니다 → 아니라는."), F("서울에서 큰 교통사고가 났다는 ___를 들었습니까? (news)", "뉴스", ["우산", "철"], "뉴스."), F("산호세에 한국마켓이 많다는 ___을 알고 있습니까? (fact)", "사실", ["소식", "말"], "사실."),
           read_q("산불이 났다는 소식"), read_q("김 선생님이 결혼한다는 소문"), read_q("내가 군인이라는 사실"), read_q("서울에서 큰 교통사고가 났다는 뉴스를 들었습니까"), read_q("내일 시험 본다는 소식 들었어")]
    ),
)

# ================================================================== L8 Topic C
_C_TXT = [
    ("육 일 새벽 튀르키예 남부와 시리아 북부에서 강진이 발생했다.", "In the early morning of the 6th, a strong earthquake occurred in southern Türkiye and northern Syria."),
    ("지진 발생 후 구 일가량이 지난 현재 두 나라에서 벌써 사망자가 사만 명을 넘었다.", "At present, about nine days after the earthquake, the dead in the two countries have already passed 40,000."),
    ("그런데 대피하지 못한 사람들 중에 실종자가 많아 이들을 포함하면 인명피해는 더 늘 것으로 보인다.", "But among the people who could not evacuate there are many missing, so including them the human casualties are expected to increase further."),
    ("현재 세계 여러 나라의 구조대원들이 무너진 건물 밑에 매몰된 생존자들을 수색하고 있다.", "At present rescue workers from many countries of the world are searching for survivors buried under collapsed buildings."),
    ("하지만 주요 피해 지역에서 여진이 계속되고 게다가 기온도 떨어져, 흙더미에 묻힌 사람들의 구조 작업도 쉽지 않다.", "However, aftershocks continue in the major damaged areas and besides, the temperature has dropped, so the rescue work for the people buried in mud piles is not easy either."),
    ("한국 정부도 구조대 예순한 명을 보내서 도움을 주고 있다.", "The Korean government is also helping by sending a rescue team of 61 people."),
    ("한편 적십자사와 같은 구호단체들은 생필품과 성금 등을 모아 이재민들을 지원하고 있다.", "Meanwhile relief organizations such as the Red Cross are collecting daily necessities and donations and supporting the victims."),
    ("비누, 치약 같은 생필품 등은 무엇이든지 많이 필요하다고 한다.", "They say daily necessities such as soap and toothpaste, anything, are needed a lot."),
    ("튀르키예 지진에 관한 문의는 튀르키예 지진피해 구호물품 지원 안내에 문의하면 된다.", "For inquiries about the Türkiye earthquake, you can inquire at the Türkiye Earthquake Relief Supplies Support Information."),
]
_C_WORDS = ["강진", "게다가", "공급", "느끼다", "단체", "대피", "도움", "매몰", "무너지다", "묻히다", "모금", "생존자", "생필품", "성금", "수색", "실종", "여진", "이재민", "적십자사", "지진", "진동", "진짜", "해일", "휴교령", "흙더미", "쓰나미"]
_TSU = [("우리나라는 쓰나미로부터 안전할까요?", "Is Korea safe from tsunamis?"), ("삼 면이 바다로 둘러싸여 있고 지진이 자주 일어나는 지역인 일본에 가까운 우리나라는 결코 쓰나미로부터 자유로울 수 없는 곳입니다.", "Korea, which is surrounded by sea on three sides and close to Japan, an area where earthquakes occur often, is a place that can never be free from tsunamis."), ("만약 일본의 북서 근해에서 지진이 발생한다면 쓰나미는 한 시간에서 한 시간 삼십 분 후 대한민국 동해에 도착하게 됩니다.", "If an earthquake occurs in the northwest coastal sea of Japan, the tsunami will arrive in the East Sea of the Republic of Korea in one hour to one hour thirty minutes."), ("실제로 동해안에서도 천구백팔십삼 년과 천구백구십삼 년 일본 근해에서 발생한 지진 해일로 인해 피해를 입은 사례가 있습니다.", "In fact, there have been cases on the east coast too of suffering damage from tsunamis that occurred in the coastal sea of Japan in 1983 and 1993."), ("천구백팔십삼 년 쓰나미로 인해 주민 한 명과 어부 두 명이 사망했습니다.", "In the 1983 tsunami one resident and two fishermen died."), ("또한 해일이 항구로부터 칠백 미터 떨어진 인근 초등학교까지 올라와 그 지역 초등학교는 휴교령이 내려지는 등 큰 피해를 주었다고 합니다.", "Also, the tidal wave came up to a nearby elementary school 700 m away from the port, and they say it caused great damage, such as an order closing the elementary schools in that area.")]
L8 = lesson(
    "Ch 39 · Topic C: A strong earthquake occurred last week (지난주에 강진이 발생했어요)",
    "지난주에 강진이 발생했어요 · 튀르키예 지진 · 구조대 · 매몰 생존자 · 여진 · 구호품 · 쓰나미와 해일 · 한국과 쓰나미",
    requires=[],
    cards=[
        card("Topic C: A strong earthquake occurred last week (지난주에 강진이 발생했어요)",
             "The following text is about the earthquake that occurred in Türkiye. (The English is mine; the book gives none; the numbers are spelled out in Hangul. This is a news report of a disaster with many deaths.)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists 구호(물)품, ~에 관한/관하여, ~(이)나/(이)든지 and 지진해일 (see the grammar below).",
             tables=[ktable(_rows(_C_WORDS)), table(["Word", "Meaning"], [["구호(물)품", "relief items; relief supplies"], ["지진해일", "a tsunami; a tidal wave caused by an earthquake"]], say=[0])]),
        card("한국어에서는: 쓰나미 (지진해일) and 해일",
             "쓰나미 (a tsunami) refers to a series of water waves caused by underwater earthquakes, volcanic eruptions, or other underwater explosions and mass movements. On the other hand, 해일 (tidal wave) usually refers to a water surge caused by floodwater, a storm surge, or a tsunami."),
        card("Follow-up 1 (Reading): an article about tsunamis",
             "The following article is about tsunamis (지진해일). The book asks (1) what makes Korea susceptible to tsunamis and (2) to describe the damages caused by the 1983 tsunami. The article is the book’s with the numbers spelled out; the English is mine.",
             examples=passage(_TSU)),
        card("The answers (mine)", "My answers:",
             tables=[table(["Question", "Answer (mine)"], [["1. What makes Korea susceptible?", "It is surrounded by sea on three sides and is close to Japan, where earthquakes occur often; a tsunami from northwest Japan would reach the East Sea within about one to one and a half hours"], ["2. Damage of the 1983 tsunami", "One resident and two fishermen died; the wave rose to an elementary school 700 m from the port, and the schools in the area were ordered closed"]])]),
        card("Activities left out", "The presentation steps of Topic C (a SMART Board activity, matching sentence strips from Set A and Set B and translating in pairs) and Follow-up 2 (listening to two conversations about a natural disaster and noting type, place and casualties) are audio and strip activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT + _TSU, k=3)
        + [M("Where did the earthquake occur?", "Southern Türkiye and northern Syria", ["Japan", "Indonesia", "Korea"], "튀르키예 남부와 시리아 북부."), M("How many days had passed in the article?", "About nine", ["About one", "About thirty", "About three"], "구 일가량."), M("Why is the rescue work not easy?", "Aftershocks continue and the temperature dropped", ["No rescue workers", "A typhoon", "A flood"], "여진이 계속되고 기온도 떨어져."), M("How many rescue workers did Korea send?", "61", ["6", "16", "600"], "예순한 명."), M("What do relief organizations collect?", "Daily necessities and donations", ["Weapons", "Cars", "Tents only"], "생필품과 성금."), M("What is a 쓰나미?", "A series of water waves caused by underwater earthquakes etc.", ["A rainstorm", "A mudslide", "A heat wave"], "The book’s note."), M("How soon would a tsunami from northwest Japan reach Korea?", "In one hour to one hour thirty minutes", ["In a day", "In ten minutes", "In a week"], "한 시간에서 한 시간 삼십 분."),
           F("무너진 건물 밑에 ___된 생존자들을 수색하고 있다. (buried)", "매몰", ["대피", "실종"], "매몰."), F("주요 피해 지역에서 ___이 계속되고 있다. (aftershocks)", "여진", ["강진", "진동"], "여진."), F("적십자사 같은 ___들이 이재민들을 지원하고 있다. (organizations)", "단체", ["생존자", "구조대"], "단체."), F("대피하지 못한 사람들 중에 ___자가 많다. (missing)", "실종", ["매몰", "생존"], "실종자."), F("흙더미에 ___ 사람들의 구조 작업도 쉽지 않다. (buried)", "묻힌", ["무너진", "잠긴"], "묻히다."),
           read_q("지난주에 강진이 발생했어요"), read_q("구조대원들이 매몰된 생존자들을 수색하고 있습니다"), read_q("여진이 계속되고 있습니다"), read_q("적십자사가 이재민들을 지원하고 있습니다"), read_q("우리나라는 쓰나미로부터 안전할까요")]
    ),
)

# ================================================================== L9 Grammar C: question word + (이)나/(이)든지
_QW = [("누구나 / 누구든지", "whoever; anyone"), ("무엇이나 / 무엇이든지", "whatever; anything"), ("어디(에)나 / 어디(에)든지", "wherever; anywhere"), ("언제나 / 언제든지", "whenever; anytime")]
_QE = [("이 영화는 누구나 볼 수 있어요.", "Anyone can watch this movie."), ("우리 형은 무엇이나 잘 먹어요.", "My older brother eats anything well."), ("주말에는 어디에나 갈 수 있어요.", "I can go anywhere on weekends."), ("질문 있으면 언제나 전화하세요.", "Please call me anytime if you have a question."), ("이 영화는 누구든지 볼 수 있어요.", "Anyone can watch this movie."), ("우리 형은 무엇이든지 잘 먹어요.", "My older brother eats anything well."), ("주말에는 어디든지 갈 수 있어요.", "I can go anywhere on weekends."), ("질문 있으면 언제든지 전화하세요.", "Please call me anytime if you have a question.")]
_QA = [("이 책은 쉬워서 누구나 읽을 수 있어요.", "This book is so easy [that] anyone can read it."), ("이 책은 쉬워서 누구든지 읽을 수 있어요.", "This book is so easy [that] anyone can read it."), ("이 책은 쉬워서 아무나 읽을 수 있어요.", "This book is so easy [that] anyone can read it.")]
_QF = [("도움이 필요하신 분은 언제든지 저한테 연락주세요.", "언제든지 (언제나)", "Anyone who needs help, please contact me anytime."), ("열심히 노력하면 누구나 성공할 수 있어요.", "누구나 (누구든지)", "If you try hard, anyone can succeed."), ("지진 이재민을 위한 구호물품으로 무엇이든지 환영합니다.", "무엇이든지 (무엇이나)", "Anything is welcome as relief items for the earthquake victims."), ("이번 세일 기간 중에는 서울 시내 어디나 무료로 배달해 드립니다.", "어디나 (어디든지)", "During this sale period we deliver free anywhere in Seoul.")]
_QM = [("생일 파티", "제 생일 파티에는 누구나 올 수 있어요.", "Anyone can come to my birthday party."), ("생일 파티", "제 생일 파티 선물은 무엇이든지 좋아요.", "Any present for my birthday party is fine.")]
_QMY = [("언제든지 물어보세요.", "Please ask anytime."), ("무엇이든지 괜찮아요.", "Anything is fine."), ("이 길은 누구나 지나갈 수 있어요.", "Anyone can pass along this road."), ("어디든지 따라갈게요.", "I will follow you anywhere.")]
L9 = lesson(
    "Ch 39 · Grammar C: a question word + (이)나/(이)든지 (whoever, whatever, wherever, whenever)",
    "누구나 · 누구든지 · 무엇이든지 · 어디든지 · 언제든지 · 아무나",
    requires=[],
    cards=[
        card("A question word + (이)나/(이)든지",
             "In an earlier lesson you learned that the question words like 누구, 언제, 어디, and 무엇 can function as indefinite pronouns. For example, 누구 can be translated as who or someone and 어디 as where or someplace. When the particle ~(이)나 or ~(이)든지 is attached to these question words, they can be translated as follows:",
             tables=[table(["Question word + (이)나/(이)든지", "English meaning"], [[a, b] for a, b in _QW], say=[0])]),
        card("Examples", "(The English is the book’s; the book gives each example with the 나 form; the 든지 forms are mine.)", examples=passage(_QE)),
        card("참고: 아무 + (noun) + (이)나", "Without changing the meaning, a question word + (이)나/(이)든지 can be replaced with 아무 + (noun) + (이)나. For example (the English is the book’s):", examples=passage(_QA)),
        card("Follow-up 1 (Reading): fill in the blanks",
             "Choose the most appropriate phrase from the box 누구나/누구든지, 언제나/언제든지, 어디나/어디든지, 무엇이나/무엇이든지 and complete each sentence. The sentences are the book’s; the completed answers are mine; the English is mine.",
             tables=[table(["Sentence (completed)", "Phrase (mine)", "English (mine)"], [[a, b, c] for a, b, c in _QF], say=[0])]),
        card("Follow-up 5 (Speaking and writing): the model",
             "One partner draws a topic card and reads it aloud; the other makes a sentence with a question word + (이)나/(이)든지. The book’s model (the English is mine):",
             examples=dlg([("A", "생일 파티", "Birthday party"), ("B", "제 생일 파티에는 누구나 올 수 있어요.", "Anyone can come to my birthday party."), ("B", "제 생일 파티 선물은 무엇이든지 좋아요.", "Any present for my birthday party is fine.")])),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_QMY)),
        card("Activities left out", "Follow-up 2 (listening to four short dialogs and identifying the female speaker’s response) is an audio activity, and the rest of Follow-up 5 (choosing a topic and creating an invitation poster on a flip chart with date and time, venue, food to bring and games) is a group poster activity."),
    ],
    exercises=uniq(
        _tr(_QE + _QA + [(a, c) for a, b, c in _QF] + _QMY, k=3) + _tr(_QW, k=3)
        + [M("What does 누구나/누구든지 mean?", "whoever; anyone", ["someone", "no one", "who"], "The book’s table."), M("What does 언제나/언제든지 mean?", "whenever; anytime", ["sometime", "never", "when"], "The book’s table."), M("What does 어디(에)나/어디(에)든지 mean?", "wherever; anywhere", ["somewhere", "nowhere", "where"], "The book’s table."), M("What does 무엇이나/무엇이든지 mean?", "whatever; anything", ["something", "nothing", "what"], "The book’s table."), M("What can replace a question word + (이)나/(이)든지?", "아무 + (noun) + (이)나", ["아무 + 도", "아무 + 만", "아무 + 에"], "The book’s 참고."), M("What does 이 영화는 누구나 볼 수 있어요 mean?", "Anyone can watch this movie", ["I will watch this movie", "Someone watched this movie", "No one can watch"], "The book’s example."),
           F("질문 있으면 ___ 전화하세요. (anytime)", "언제나", ["누구나", "어디나"], "언제나."), F("이 영화는 ___ 볼 수 있어요. (anyone)", "누구나", ["언제나", "어디나"], "누구나."), F("우리 형은 ___ 잘 먹어요. (anything)", "무엇이나", ["누구나", "언제나"], "무엇이나."), F("주말에는 ___ 갈 수 있어요. (anywhere)", "어디든지", ["누구든지", "언제든지"], "어디든지."), F("열심히 노력하면 ___ 성공할 수 있어요. (anyone)", "누구든지", ["어디든지", "언제든지"], "누구든지."),
           read_q("이 영화는 누구나 볼 수 있어요"), read_q("우리 형은 무엇이나 잘 먹어요"), read_q("주말에는 어디에나 갈 수 있어요"), read_q("질문 있으면 언제나 전화하세요"), read_q("이 책은 쉬워서 아무나 읽을 수 있어요")]
    ),
)

# ================================================================== L10 Grammar D: 관해서/관한, 위해서/위한
_DA = [("사회 문제에 대해서 이야기했습니다.", "We talked about social issues."), ("사회 문제에 대한 의견을 나누었습니다.", "We shared the opinion about social issues.")]
_DB = [("그 일에 관해서 아무것도 몰라요.", "I know nothing about the matter."), ("그 일에 관한 소식을 들었어요.", "I heard the news about the matter."), ("나라를 위해서 입대했어요.", "I enlisted for my country."), ("나라를 위한 일을 하고 있어요.", "I am doing work that is for my country.")]
_DP = [("한국 역사에 (관해서, 관한) 함께 의논했어요.", "관해서", "한국 역사에 관해서 함께 의논했어요.", "We discussed Korean history together."), ("직장 생활에 (관해서, 관한) 고민을 친구와 함께 이야기했어요.", "관한", "직장 생활에 관한 고민을 친구와 함께 이야기했어요.", "I talked with a friend about my worries about work life."), ("앞으로 이 일에 (관해서, 관한) 말하지 마세요.", "관해서", "앞으로 이 일에 관해서 말하지 마세요.", "Don’t talk about this matter in the future."), ("대학입학을 (위해서, 위한) 열심히 공부합니다.", "위해서", "대학입학을 위해서 열심히 공부합니다.", "I study hard for college admission."), ("이 집은 우리 가족을 (위해서, 위한) 집입니다.", "위한", "이 집은 우리 가족을 위한 집입니다.", "This house is a house for our family."), ("아내를 (위해서, 위한) 주말마다 청소합니다.", "위해서", "아내를 위해서 주말마다 청소합니다.", "I clean every weekend for my wife.")]
_DM = [("A", "생일 파티 안내", "Birthday party notice"), ]
L10 = lesson(
    "Ch 39 · Grammar D: ~에 관해서 vs. ~에 관한 and ~을/를 위해서 vs. ~을/를 위한 · and self-evaluation",
    "~에 관해서 · ~에 관한 · ~을 위해서 · ~을 위한 · ~에 대해서 · ~에 대한 · 자기 평가",
    requires=[],
    cards=[
        card("Recall ~에 대해(서) and ~에 대한",
             "You learned in Chapter 19 that the phrases ~에 대해(서), ~에 대하여, and ~에 대한 can be translated as about (or concerning or regarding), as in 김치에 대해서 (about kimchi), 김치에 대하여 (about kimchi), and 김치에 대한 (about kimchi). You also learned that ~에 대해(서) and ~에 대하여 are reserved to modify a verb and ~에 대한 is reserved to modify a noun. For example (the English is the book’s):",
             examples=passage(_DA)),
        card("Why they differ",
             "Note that ~에 대해(서) modifies the verb 이야기했습니다 and ~에 대한 modifies the noun 의견. This occurs because these phrases are derived from the verb 대하다 (to face; to confront). 대한 in ~에 대한 is an attributive form of the verb 대하다; thus the phrase can only modify a noun.\n\nThe following phrases are also derived from a verb and show the same pattern: 1. ~에 관해서/관하여/관한 (about; regarding; concerning); 2. ~을/를 위해(서)/위하여/위한 (for the benefit of; for the sake of). ~에 관해서/관하여/관한 are derived from the verb 관하다 (to be related to; to concern; to pertain to) and 위해(서)/위하여/위한 are derived from the verb 위하다 (to do for the greater good; to serve; to honor). ~에 관해서/관하여 and ~을/를 위해서/위하여 modify a verb (or verb phrase), whereas the attributive form ~에 관한 and ~을/를 위한 modify a noun. (The English is the book’s.)",
             examples=passage(_DB)),
        card("Follow-up 3 (Reading): choose the correct form",
             "Complete each sentence by circling the correct form in the parentheses, then translate the sentence into English. The sentences are the book’s; the choices and the English are mine.",
             tables=[table(["Sentence", "Correct form (mine)", "Completed sentence", "English (mine)"], [[a, b, c, d] for a, b, c, d in _DP], say=[2])]),
        card("Follow-up 5 (Speaking and writing): the invitation poster", "The book’s model: one partner draws a topic card and the other makes a sentence with a question word + (이)나/(이)든지 (see the previous grammar lesson); you then prepare an invitation poster together."),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with.\n\n"
             "Now I am able to: comprehend weather forecasts and talk about suitable activities for varying weather conditions; extract factual information about natural hazards (flood, earthquake, landslide, etc.) and extreme weather (drought, blizzard), and discuss the disasters caused by them; identify different types of natural disasters and the causes, damages, and casualties associated with them; and report about and describe natural disasters, including the causes, damages, and casualties.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; question words used as indefinite pronouns; a noun clause in an appositive relationship; a question word + (이)나/(이)든지; ~에 관해서/관하여 vs. ~에 관한 (about; regarding; concerning); ~을/를 위해서/위하여 vs. ~을/를 위한 (for the sake of; for); and the Sino-Korean syllables within 예보 (豫報), 폭우 (暴雨), and 지진 (地震)."),
        card("Activities left out", "Follow-up 4 (listening to three conversations about a news report on a natural disaster and circling the expression used), Activity 1 (reading a news article about the Korean rescue dogs in Türkiye; the book’s headline question and two questions on the dogs’ advantage and what happened to three of them), Activity 2 (listening to MBC earthquake news and its video) and Activity 3 (how to evacuate during an earthquake: two pictures, two texts and a presentation) are audio, video, picture and group activities."),
    ],
    exercises=uniq(
        _tr(_DA + _DB + [(c, d) for a, b, c, d in _DP], k=3)
        + [M("Which phrase modifies a noun?", "~에 관한", ["~에 관해서", "~에 관하여", "~에 대해서"], "The book’s note."), M("Which phrase modifies a verb?", "~을/를 위해서", ["~을/를 위한", "~에 관한", "~에 대한"], "The book’s note."), M("Which verb is ~에 관해서 derived from?", "관하다", ["대하다", "위하다", "가다"], "The book’s note."), M("Which verb is ~을/를 위해서 derived from?", "위하다", ["관하다", "대하다", "가다"], "The book’s note."), M("What does 나라를 위한 일을 하고 있어요 mean?", "I am doing work that is for my country", ["I enlisted for my country", "I know nothing about it", "I have a country"], "The book’s example."), M("What does 그 일에 관한 소식을 들었어요 mean?", "I heard the news about the matter", ["I know nothing about the matter", "I did the matter", "I enlisted"], "The book’s example."),
           F("한국 역사에 ___ 함께 의논했어요. (about; modifies a verb)", "관해서", ["관한", "위한"], "관해서."), F("직장 생활에 ___ 고민을 이야기했어요. (about; modifies a noun)", "관한", ["관해서", "위해서"], "관한."), F("대학입학을 ___ 열심히 공부합니다. (for; modifies a verb)", "위해서", ["위한", "관한"], "위해서."), F("이 집은 우리 가족을 ___ 집입니다. (for; modifies a noun)", "위한", ["위해서", "관해서"], "위한."), F("아내를 ___ 주말마다 청소합니다. (for; modifies a verb)", "위해서", ["위한", "관한"], "위해서."),
           read_q("한국 역사에 관해서 함께 의논했어요"), read_q("직장 생활에 관한 고민을 이야기했어요"), read_q("대학입학을 위해서 열심히 공부합니다"), read_q("이 집은 우리 가족을 위한 집입니다"), read_q("아내를 위해서 주말마다 청소합니다")]
    ),
)

# ================================================================== L11 Activities: rescue dogs
_DOG = [("튀르키예 강진 피해 현장에서 발에 붕대를 감은 채 수색 작업을 이어가고 있는 한국 구조견이 현지에서도 화제다.", "The Korean rescue dogs continuing search work with bandages wrapped around their feet at the scene of the Türkiye earthquake damage are also a topic of conversation locally."), ("튀르키예 강진 피해 지역에서 활동 중인 한국 해외긴급구호대는 지난 구 일 구조 활동을 시작한 이래 총 여덟 명의 생존자를 구조했고, 시신 열여덟 구를 찾았다.", "The Korea Disaster Relief Team, which is active in the Türkiye earthquake damage area, has rescued a total of eight survivors and found 18 bodies since it began rescue activity on the 9th."), ("구조 활동에는 특수 인명구조견인 토백이, 티나, 토리, 해태 등 네 마리가 투입됐다.", "Four dogs, the special life-saving dogs Tobaegi, Tina, Tori and Haetae, were put into the rescue activity."), ("이들은 모두 이 년간의 훈련 과정을 거쳤다.", "All of them went through a two-year training course."), ("구조견들은 무너진 건물 사이에 사람이 들어가기 어려운 좁은 공간에도 접근하고 있다.", "The rescue dogs are approaching even narrow spaces between the collapsed buildings where it is hard for people to get in."), ("위험한 재난 현장을 이리저리 뛰어다닌 탓에 네 마리 가운데 세 마리가 깨진 유리와 부러진 철근에 발에 상처를 입었다.", "Because they ran about the dangerous disaster scene, three of the four dogs were wounded on their feet by broken glass and broken steel bars."), ("그러나 세 마리 모두 치료를 받은 뒤 다시 현장에 투입됐고, 현재 발에 붕대를 감은 채 계속해서 수색 작업을 이어가고 있다고 하베르는 전했다.", "However, all three dogs were put back into the scene after receiving treatment, and are now continuing the search work with bandages on their feet, the TRT Haber reported.")]
L11 = lesson(
    "Ch 39 · Activities: Korean rescue dogs in Türkiye",
    "구조견 · 붕대를 감은 채 · 수색 작업 · 한국 해외긴급구호대 · 생존자 구조",
    requires=[],
    cards=[
        card("Activity 1 (Reading): a news article about rescue dogs",
             "The following news article (Yonhap News) is about Korean rescue dogs in Türkiye. The book asks you (1) to create a fitting headline, (2) to say what advantage the rescue dogs contribute to the rescue operation and (3) to say what happened to three of the dogs. The article is the book’s with the numbers spelled out; the abbreviation KDRT and the news agency names in Latin letters are dropped (“TRT 하베르” is written 하베르); the English is mine.",
             examples=passage(_DOG)),
        card("The answers (mine)", "My answers:",
             tables=[table(["Question", "Answer (mine)"], [["1. Headline", "발에 붕대를 감은 채 수색하는 한국 구조견"], ["2. Advantage of the rescue dogs", "They can approach narrow spaces between collapsed buildings that are hard for people to enter"], ["3. What happened to three of the dogs", "They hurt their feet on broken glass and broken steel bars, received treatment, and went back to the scene with bandaged feet"]])]),
        card("Activities left out", "Activity 2 (listening to MBC earthquake news and checking it with the video) and Activity 3 (how to evacuate when an earthquake occurs: two pictures from the Ministry of the Interior and Safety, two texts and a presentation in Korean) are audio, video, picture and group activities."),
    ],
    exercises=uniq(
        _tr(_DOG, k=3)
        + [M("How many survivors had the team rescued?", "Eight", ["Eighteen", "Four", "None"], "여덟 명의 생존자."), M("How many bodies did they find?", "Eighteen", ["Eight", "Four", "None"], "시신 열여덟 구."), M("How many rescue dogs were used?", "Four", ["Three", "Eight", "Eighteen"], "네 마리."), M("How long did the dogs train?", "Two years", ["Two months", "Ten years", "One week"], "이 년간의 훈련."), M("How many of the dogs hurt their feet?", "Three", ["Four", "One", "None"], "세 마리."), M("What did they hurt their feet on?", "Broken glass and broken steel bars", ["Ice", "Mud", "Fire"], "깨진 유리와 부러진 철근."), M("What are the dogs doing now?", "Continuing the search with bandaged feet", ["Resting", "Returning to Korea", "Being treated"], "발에 붕대를 감은 채 계속해서."),
           F("한국 ___가 튀르키예 강진 피해 현장에서 활동하고 있다. (rescue dogs)", "구조견", ["생존자", "단체"], "구조견."), F("발에 붕대를 감은 ___ 수색 작업을 이어가고 있다. (in the state of)", "채", ["것", "때"], "-(으)ㄴ 채."), F("구조대는 여덟 명의 ___를 구조했다. (survivors)", "생존자", ["이재민", "실종자"], "생존자."), F("좁은 공간에도 ___하고 있다. (approach)", "접근", ["대피", "수색"], "접근."), F("세 마리 모두 ___를 받은 뒤 다시 투입됐다. (treatment)", "치료", ["훈련", "구조"], "치료."),
           read_q("구조견"), read_q("발에 붕대를 감은 채 수색 작업을 이어가고 있습니다"), read_q("여덟 명의 생존자를 구조했습니다"), read_q("좁은 공간에도 접근하고 있습니다"), read_q("세 마리 모두 치료를 받은 뒤 다시 투입되었습니다")]
    ),
)

# ================================================================== L12 core vocabulary
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Loan words", _CV_LOAN), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/") and " " not in r[0]]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L12 = lesson(
    "Ch 39 · Core vocabulary",
    "주요 단어 · 날씨 · 홍수 · 태풍 · 지진 · 구호품 · 대피 · 복구",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank.\n\n"
             "The example sentences with digits are respelled in Hangul (50 mm → 오십 밀리미터; 1온스 → 한 온스; 980달러 → 구백팔십 달러; 3년 만에 → 삼 년 만에; 7월 → 칠 월; 30도 → 삼십 도; 20cm → 이십 센티미터; 6월 → 유월; 1명 → 한 명; 10명 → 열 명; the English “aurora” and “ounce” are dropped). For the grammar features, the book’s long English labels are used as given."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 수재민 mean?", "flood victims", ["a victim of natural disaster", "survivors", "rescuers"], "水災民."), M("What does 이재민 mean?", "a victim of natural disaster", ["flood victims", "survivors", "rescuers"], "罹災民."), M("What does 매몰 mean?", "burying; to be buried", ["evacuation", "collapse", "relief"], "埋沒."), M("What does 대피 mean?", "evacuation; to take shelter", ["burying", "collapse", "flood"], "待避."), M("What does 폭염 mean?", "heat wave; scorching heat", ["cold snap", "heavy snow", "typhoon"], "暴炎."), M("What does 한파 mean?", "a cold snap", ["heat wave", "typhoon", "drought"], "寒波."), M("What does 가뭄 mean?", "a drought", ["a flood", "a typhoon", "a blizzard"], "가뭄."), M("What does 휴교령 mean?", "an order for school closing", ["an order to evacuate", "a holiday", "a school trip"], "休校令."),
           F("기상청에서 호우주의보를 ___했습니다. (issued)", "발령", ["폐쇄", "대피"], "발령."), F("홍수로 피해를 입은 ___들을 도웁시다. (flood victims)", "수재민", ["생존자", "단체"], "수재민."), F("태풍과 홍수로 많은 집들이 ___. (collapsed)", "무너졌습니다", ["묻혔습니다", "얼었습니다"], "무너지다."), F("산사태가 나서 집이 흙더미에 ___. (was buried)", "묻혔어요", ["무너졌어요", "잠겼어요"], "묻히다."), F("이번 대지진 이후에 크고 작은 ___이 계속되고 있습니다. (aftershocks)", "여진", ["강진", "진동"], "여진."),
           read_q("주요 단어"), read_q("수재민"), read_q("이재민"), read_q("여진"), read_q("휴교령")]
    ),
)

UNIT = unit("Semester 2 · Unit 10 · Chapter 39: Natural Disasters (자연재해)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])

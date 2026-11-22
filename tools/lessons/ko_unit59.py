"""Unit 59: KBC Semester III, Unit 15, Lesson 4 - Weather and Natural Disasters (날씨와 자연재해).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 15, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_S1 = [("봄", "따뜻하다", "spring: to be warm"), ("여름", "덥다", "summer: to be hot"), ("가을", "쌀쌀하다", "autumn: to be chilly"), ("겨울", "춥다", "winter: to be cold"), ("눈", "내리다", "snow: to fall"), ("바람", "불다", "wind: to blow"), ("안개", "끼다", "fog: to form"), ("번개", "치다", "lightning: to strike")]
_HJ4 = [("氣 기", "air; energy", "기온, 기후"), ("雨 우", "rain", "우산, 강우량"), ("暴 폭", "fierce; rapid", "폭우, 폭설"), ("度 도", "degree; (the) law", "습도, 제도"), ("水 수", "water", "홍수, 강수량")]
_HJW4 = [("기온", "temperature"), ("기후", "climate"), ("우산", "an umbrella"), ("강우량", "the amount of rainfall"), ("폭우", "heavy rain"), ("폭설", "heavy snow; blizzard"), ("습도", "humidity"), ("제도", "a system"), ("홍수", "a flood; “big water”"), ("강수량", "the amount of rainfall; “dropped water amount”")]
_SIM4 = [("공기", "대기", "air ≈ the atmosphere"), ("폭우", "호우", "heavy rain ≈ torrential rain"), ("온도", "기온", "temperature ≈ air temperature"), ("홍수", "물난리", "a flood ≈ a flood disaster")]
_ODD = [("온도, 섭씨 이십 도, 차도, 습도", "차도", "a road (not weather)"), ("저기압, 기온, 기분, 일기예보", "기분", "a mood (not weather)"), ("우박, 배우, 폭우, 호우", "배우", "an actor (not weather)"), ("폭우, 폭염, 폭력, 폭풍", "폭력", "violence (not weather)"), ("강수량, 세수, 침수, 수재민", "세수", "washing one’s face (not a disaster word)")]
_L1X = [("공기", "air"), ("일기", "weather"), ("대기", "the atmosphere"), ("열기", "heat"), ("우박", "hail"), ("호우", "torrential rain"), ("온도", "temperature"), ("기상청", "the Meteorological Administration"), ("물난리", "a flood disaster"), ("수재민", "flood victims"), ("차도", "a road for cars"), ("저기압", "low pressure"), ("일기예보", "a weather forecast"), ("폭염", "a heat wave"), ("폭풍", "a storm"), ("폭력", "violence"), ("침수", "flooding"), ("세수", "washing one’s face"), ("쌀쌀하다", "to be chilly"), ("따뜻하다", "to be warm"), ("안개", "fog"), ("번개", "lightning")]
L1 = lesson(
    "U15 L4 · Review: weather words and Sino-Korean 氣 雨 暴 度 水",
    "날씨와 자연재해 · 단어 복습 · 한자어 복습 · 봄 여름 가을 겨울 · 기온 · 폭우 · 氣 雨 暴 度 水",
    requires=[],
    cards=[
        card("단어 복습 1: season and weather matches (my answers)", "The book asks you to connect the words on the left with the words on the right that fit (the right column: 내리다, 춥다, 치다, 끼다, 쌀쌀하다, 따뜻하다, 불다, 덥다). My pairs:", tables=[table(["Word", "Matching word", "Meaning"], [list(r) for r in _S1], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ4], say=[2]), ktable(_HJW4)]),
        card("한자어 복습 1: the word with a similar meaning (my answers)", "Circle the word whose meaning is most similar to the word on the left (A. 공기: 일기, 대기, 열기; B. 폭우: 우산, 호우, 우박; C. 온도: 기후, 기온, 기상청; D. 홍수: 강우량, 물난리, 수재민).", tables=[table(["Word", "Similar word (my answer)", "Meaning"], [[a, b, c] for a, b, c in _SIM4], say=[0, 1])]),
        card("한자어 복습 2: the word that is not related to weather or disasters (my answers)", "Read the four words and circle the one that is not related to weather or natural disasters (the first row’s second word is 섭씨 20도, read 섭씨 이십 도).", tables=[table(["The four words", "The odd word (my answer)", "Meaning"], [[a, b, c] for a, b, c in _ODD], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L1X)]),
        card("Activities left out", "단어 복습 2 (listening to six weather forecasts and writing a short English forecast for each region) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_HJW4, k=3) + _tr(_L1X, k=3) + _tr([(a + " + " + b, c) for a, b, c in _S1], k=3)
        + [M("Which word goes with 봄?", "따뜻하다", ["춥다", "덥다", "쌀쌀하다"], "Spring is warm."), M("Which word goes with 여름?", "덥다", ["춥다", "쌀쌀하다", "따뜻하다"], "Summer is hot."), M("Which word goes with 가을?", "쌀쌀하다", ["덥다", "따뜻하다", "춥다"], "Autumn is chilly."), M("Which word goes with 겨울?", "춥다", ["덥다", "따뜻하다", "쌀쌀하다"], "Winter is cold."), M("Which verb goes with 눈?", "내리다", ["불다", "치다", "끼다"], "Snow falls."), M("Which verb goes with 바람?", "불다", ["내리다", "치다", "끼다"], "Wind blows."), M("Which verb goes with 안개?", "끼다", ["불다", "치다", "내리다"], "Fog forms."), M("Which verb goes with 번개?", "치다", ["끼다", "불다", "내리다"], "Lightning strikes."), M("What does the syllable 氣 (기) mean?", "air; energy", ["rain", "fierce", "water"], "기온."), M("What does the syllable 雨 (우) mean?", "rain", ["air", "fierce", "water"], "우산."), M("What does the syllable 暴 (폭) mean?", "fierce; rapid", ["rain", "degree", "water"], "폭우."), M("What does the syllable 度 (도) mean?", "degree; (the) law", ["rain", "water", "air"], "습도."), M("What does the syllable 水 (수) mean?", "water", ["rain", "air", "fierce"], "홍수."), M("Which word is similar to 폭우?", "호우", ["우산", "우박", "우체국"], "Heavy rain."), M("Which word is similar to 온도?", "기온", ["기후", "기상청", "기분"], "Temperature."), M("Which word is not related to weather?", "기분", ["저기압", "기온", "일기예보"], "A mood."), M("Which word is not related to weather?", "배우", ["우박", "폭우", "호우"], "An actor."),
           F("오늘 ___은 이십 도입니다. (temperature)", "기온", ["기후", "습도"], "기온."), F("비가 올 때는 ___을 쓰세요. (an umbrella)", "우산", ["강수량", "홍수"], "우산."), F("올해는 ___ 때문에 피해가 컸습니다. (heavy rain)", "폭우", ["폭력", "폭설"], "폭우."), F("여름에는 ___가 높아서 후텁지근합니다. (humidity)", "습도", ["제도", "기후"], "습도."), F("한국은 겨울에 눈이 많이 ___. (falls)", "내립니다", ["붑니다", "칩니다"], "눈이 내리다."),
           read_q("봄에는 따뜻하고 겨울에는 춥습니다"), read_q("폭우로 홍수가 났습니다"), read_q("오늘은 안개가 끼었습니다"), read_q("번개가 치고 바람이 불었습니다"), read_q("기온과 습도가 높습니다")]
    ),
)

# ================================================================== L2 Part 1
_HAVE = [["North Korea", "Heavy rain, about 250 dead or missing (the book’s example)"], ["Great Britain", "July temperatures higher than in the past 95 years (the book’s example)"]]
_BOGI = [("추운 안개 낀 새벽에 조깅을 할 때 무엇을 입습니까?", "What do you wear when you jog at a cold, foggy dawn?"), ("비가 많이 오는 날에 외출할 때는 뭘 입어요?", "What do you wear when you go out on a day when it rains a lot?")]
_SPEAK10 = [("고향의 계절별 날씨와 고향에서 발생할 수 있는 자연재해에 대해 이야기해 보세요.", "Talk about the weather in each season in your hometown and the natural disasters that can occur in your hometown.")]
L2 = lesson(
    "U15 L4 · Part 1 (도입 학습): a table of weather disasters and speaking prompts",
    "도입 학습 · 기상재해 · 옷차림 · 기상특보 · 일기예보 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): weather disasters around the world",
             "The book gives a table from Hankyoreh summarizing weather disasters in many countries, in tabs for Asian countries (North Korea, South Korea, China, Japan), European countries (Europe in general, the Netherlands, Great Britain) and countries in the Americas (the United States, Brazil), and asks you to translate the information of each tab into English. The tabs’ Korean texts are inside the picture and are not in the text of the book; only the two examples the book translates for you are in the text:",
             tables=[table(["Country", "Translation given in the book"], [list(r) for r in _HAVE])]),
        card("학습활동 2: speaking pattern (보기)", "In the pair activity you exchange questions and answers in Korean about the appropriate clothing for activities in various weather conditions, such as rain or snow. The book’s model questions (the English is mine; the spoken Korean has no slash):", examples=passage(_BOGI)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK10)),
        card("Activities left out", "학습활동 2 (a conversation from edunet4u.net about dressing for the weather: the recommended clothing and other dos and don’ts for rainy and snowy weather), 학습활동 3 (an explanation of weather-related warnings: how they are announced and the conditions for which they are issued, such as typhoon, high sea waves and tsunami) and 학습활동 4 (two YTN forecasts: the season and the regional weather for the central and southern regions, Jeju and the south coast and Jiri Mountain; then reporting an English article about a region’s weather as a Korean radio broadcaster) are audio, pair and speaking activities."),
    ],
    exercises=uniq(
        _tr(_BOGI + _SPEAK10, k=2)
        + [M("What does the book’s North Korea example say?", "Heavy rain, about 250 dead or missing", ["A heat wave", "A typhoon", "A drought"], "The book’s example."), M("What does the book’s Great Britain example say?", "July temperatures higher than in the past 95 years", ["Floods in July", "A cold snap", "A storm"], "The book’s example."), M("What does 추운 안개 낀 새벽에 조깅을 할 때 무엇을 입습니까 ask?", "What do you wear when jogging at a cold, foggy dawn?", ["Where do you jog?", "When do you jog?", "Who jogs with you?"], "The 보기 question."),
           read_q("비가 많이 오는 날에 외출할 때는 뭘 입어요"), read_q("고향의 계절별 날씨에 대해 이야기해 보세요"), read_q("고향에서 발생할 수 있는 자연재해에 대해 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("비상사태", "(非常事態) a state of emergency", "일본 정부는 원전사고로 비상사태를 선포했습니다."),
        ("선포(하다/되다)", "(宣布) announcement; proclamation (to announce; to proclaim/to be announced; to be proclaimed)", "정부는 새로운 정책을 선포했습니다."),
        ("이상(하다)", "(異常) abnormal(ity); absurd(ity) (to be abnormal; to be absurd)", "최근 이상 기후가 나타나는 곳이 많습니다.", "정상 | 이상 (理想) an ideal, 이상 (以上) more than"),
        ("전력", "(電力) electric power; electricity", "여름철에는 에어컨, 냉장고 등 가전제품을 많이 쓰기 때문에 전력 사용량이 증가한다.", "전기 | 전력 (全力) (with) all power/might; 전력 (前歷) prior career"),
        ("폭염", "(暴炎) heat wave; scorching heat; “fierce heat”", "요즘 폭염이 너무 심해 잠도 제대로 잘 수가 없습니다.", "혹한 | 더위, 무더위"),
    ]),
    ("학습활동 2", [
        ("강풍", "(强風) a strong wind; a gust", "오늘 강풍 주의보가 예보되어 있습니다. 각별히 주의하시기 바랍니다.", "태풍, 돌풍, 허리케인"),
        ("(눈에) 띄다", "to be seen; to be visible", "검은 색은 밤에 눈에 잘 띄지 않습니다.", "보다, 보이다"),
        ("빙판길", "(氷板) an icy road; “ice plate road”", "빙판길에 사고 차량이 급증하고 있습니다.", "빗길, 눈길"),
        ("썰매", "a sled", ""),
        ("옷차림", "attire; an outfit; “dress setting”", "그 옷차림은 오늘 회의에는 잘 맞지 않습니다.", "복장"),
        ("주머니", "a pocket; a (small) sack", "제 청바지 주머니는 너무 작아서 지갑을 넣기가 불편합니다. 요즘 제 주머니 사정이 좋지 않은데, 돈 좀 빌릴 수 있을까요?"),
        ("지진해일", "(地震海溢) a tsunami; “earthquake sea wave”", ""),
        ("특보", "(特報) a special report; (weather) advisory; “a special announcement/warning”", ""),
        ("풍랑", "(風浪) wind and waves; rough seas", ""),
    ]),
    ("학습활동 3", [
        ("~ 치고(는)", "considering; seeing; as; for", "그 분은 구십 세 노인치고는 대단히 건강하십니다. 고급 자동차치고는 너무 작다."),
        ("다소", "(多少) more or less; “many and few”", "", "조금, 약간"),
        ("밤사이", "overnight; during the night", "밤사이 내린 눈으로 길이 얼어 있습니다. 운전 조심하시기 바랍니다."),
        ("지형적", "(地形的) topographical", ""),
        ("진눈깨비", "sleet; wet snow", "진눈깨비가 내리고 있습니다."),
        ("퇴근길", "(退勤) the way home from work", "퇴근길에 과일 좀 사다 주세요.", "출근길 | 출퇴근길, 등굣길, 하굣길, 귀성길, 귀경길"),
        ("활성화(하다/되다)", "(活性化) activation; galvanization (to activate; to galvanize/to be activated; to be galvanized)", "이 지역의 경제를 활성화하기 위한 대책을 논의해 봅시다."),
    ]),
]
L3 = lesson(
    "U15 L4 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 비상사태 · 선포 · 이상 · 전력 · 폭염 · 강풍 · 빙판길 · 옷차림 · 특보 · 풍랑 · 진눈깨비 · 퇴근길",
    requires=[],
    cards=vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=8, nread=8)),
)


# ================================================================== L4 Part 2 text
_ED = [
    ("자연재해는 천재지변으로 불린다.", "Natural disasters are called acts of nature (heaven-made disasters and earth-made changes)."),
    ("인간에 의해 일어나는 인재가 아니란 뜻에서다.", "This is in the sense that they are not man-made disasters caused by humans."),
    ("자연재해 중 큰 손실을 가져오는 재해는 지진과 화산 폭발, 풍수해다.", "Among natural disasters, the ones that bring great losses are earthquakes, volcanic eruptions and wind-and-water disasters."),
    ("이 중 기상재해의 하나인 풍수해는 지구 온난화와 밀접한 관계가 있는 것으로 지적된다.", "Of these, wind-and-water disasters, one of the weather disasters, are pointed out to be closely related to global warming."),
    ("자연재해라 하더라도 인간의 대응에 따라 피해 정도는 큰 차이가 난다.", "Even if it is a natural disaster, the degree of damage differs greatly depending on human response."),
    ("천재지변에도 인재적 요소가 있다는 얘기다.", "It means that even natural disasters have man-made elements."),
    ("그제 칠레를 강타한 지진의 위력은 지난달 아이티 지진의 팔백 배에서 천 배에 이르지만 인명 피해는 수백 명 정도로 추산된다고 한다.", "The power of the earthquake that struck Chile the day before yesterday is 800 to 1,000 times that of last month’s Haiti earthquake, but human casualties are said to be estimated at several hundred."),
    ("평소 건물의 내진설계와 발 빠른 민 관 대응 등 지진에 강한 인프라를 구축해 놓았기 때문으로 분석된다.", "This is analyzed to be because they had built infrastructure strong against earthquakes, such as earthquake-resistant building design and a quick civilian-government response."),
    ("두 나라 간 지질 환경과 지진 발생 지역의 차이 등도 주요 요인으로 꼽힌다.", "The differences between the two countries in geological environment and in the areas where the earthquakes occurred are also counted as major factors."),
    ("국민의 칠십 퍼센트가량이 하루 이 달러 미만으로 생활하는 빈국 아이티로서는 재난 방지에 관심을 기울일 여유가 없을 것이다.", "For Haiti, a poor country where about 70 percent of the people live on less than 2 dollars a day, there would be no room to pay attention to disaster prevention."),
    ("세계기상기구 (더블유엠오)는 지난 십삼 일 발표한 아이티 지진 보고서에서 지진 사망자 수는 일인당 국민소득 (지엔피)과 반비례한다고 지적했다.", "The World Meteorological Organization (WMO) pointed out, in the Haiti Earthquake Report it released on the 13th, that the number of earthquake deaths is inversely proportional to per capita national income (GNP)."),
    ("자연재해에도 빈익빈 부익부 현상이 나타난다는 얘기다.", "It means that the phenomenon of the poor getting poorer and the rich getting richer appears even in natural disasters."),
    ("국제적으로만 해당되는 말은 아닐 것이다.", "It will not be a statement that applies only internationally."),
]
_SPEAK11 = [("미국에서 자주 발생하는 자연재해에는 어떤 것이 있습니까?", "What natural disasters often occur in the United States?"), ("피해 예방과 대비 방법에 대해서 이야기해 보세요.", "Talk about ways to prevent and prepare for the damage."), ("인간의 잘못으로 발생할 수 있는 자연재해에는 어떤 것이 있습니까?", "What natural disasters can be caused by human error?"), ("또 예방할 수 있는 방법에는 어떤 것들이 있습니까?", "And what ways of preventing them are there?")]
L4 = lesson(
    "U15 L4 · Part 2 (본 학습): an editorial, “재해와 빈부격차”",
    "본 학습 · 재해와 빈부격차 · 천재지변 · 인재 · 풍수해 · 칠레 지진 · 아이티 지진 · 빈익빈 부익부",
    requires=[],
    cards=[
        card("학습활동 3 (Reading): an editorial, “재해와 빈부격차” (Disasters and the gap between rich and poor)",
             "The following is part of a newspaper editorial about natural disasters (Kyunghyang, text and image). The book asks three questions: how the title relates to the main idea, which comparison is made in the second paragraph, and a translation of the last two sentences with the implication. The text is the book’s with the numbers and letters spelled out (800~1000배 is 팔백 배에서 천 배, 70% is 칠십 퍼센트, 2달러 is 이 달러, WMO is 더블유엠오, 13일 is 십삼 일, GNP is 지엔피); the quotation marks are removed, and the Hanja 人災 after 인재 is dropped from the spoken lines. The English is mine.",
             examples=passage(_ED)),
        card("The questions answered (mine)",
             "1. How the title relates to the main idea: the title, “Disasters and the gap between rich and poor,” states the editorial’s point that the damage from a natural disaster depends on a country’s wealth and preparedness: poor countries suffer far more than rich ones from disasters of the same kind.\n\n"
             "2. The comparison in the second paragraph is A. Haiti suffered more damage than Chile from a less severe earthquake (Chile’s earthquake was 800 to 1,000 times more powerful, yet its casualties were only several hundred).\n\n"
             "3. Translation of the last two sentences: “It means that the phenomenon of the poor getting poorer and the rich getting richer appears even in natural disasters. It will not be a statement that applies only internationally.” The implication: just as poor countries suffer more in disasters, within a single country the poor suffer more than the rich, because they cannot afford safe housing, preparation or recovery."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK11)),
        card("Activities left out", "학습활동 1 (a YTN video on a yellow sandstorm in North Korea: the North Korean government’s response in 2002, why the problem was so severe, and what 북한발 황사 means for South Korea) and 학습활동 2 (a North Korean broadcast about the yellow sandstorm: the purpose of the broadcast, the advising specialist’s occupation, and the advice given, such as wearing a mask and thin gloves when going out) are audio and video activities."),
    ],
    exercises=uniq(
        _tr(_ED, k=3)
        + [M("Why are natural disasters called 천재지변?", "They are not man-made disasters", ["They are always small", "They only strike cities", "They are predictable"], "인재가 아니란 뜻."), M("Which disasters bring great losses?", "Earthquakes, volcanic eruptions and wind-and-water disasters", ["Fires only", "Droughts only", "Traffic accidents"], "지진과 화산 폭발, 풍수해."), M("What are wind-and-water disasters closely related to?", "Global warming", ["Volcanoes", "Earthquakes", "Population"], "지구 온난화."), M("What does the degree of damage depend on?", "Human response", ["The season", "The date", "Luck only"], "인간의 대응."), M("Which earthquake was more powerful?", "Chile’s", ["Haiti’s", "They were equal", "Japan’s"], "팔백 배에서 천 배."), M("Why were Chile’s casualties relatively few?", "It had earthquake-resistant buildings and a quick civilian-government response", ["It was far from cities", "It had no people", "It was a small quake"], "내진설계와 민 관 대응."), M("What is Haiti described as?", "A poor country", ["A rich country", "A small island only", "A tropical resort"], "빈국."), M("What did the WMO point out?", "Earthquake deaths are inversely proportional to per capita national income", ["Earthquakes are rare", "Deaths are random", "Money does not matter"], "반비례."), M("What does 빈익빈 부익부 mean?", "The poor get poorer and the rich get richer", ["Everyone gets richer", "Everyone gets poorer", "The rich pay more"], "빈익빈 부익부."),
           F("자연재해는 ___지변으로 불린다. (heaven-made)", "천재", ["인재", "풍수"], "천재지변."), F("인간에 의해 일어나는 ___가 아니다. (man-made disaster)", "인재", ["천재", "풍수해"], "인재."), F("건물의 ___설계가 중요하다. (earthquake-resistant)", "내진", ["골칫거리", "산림"], "내진."), F("지진 사망자 수는 국민소득과 ___한다. (inversely proportional)", "반비례", ["정비례", "비례"], "반비례."), F("빈국은 재난 방지에 관심을 ___ 여유가 없다. (to pay attention)", "기울일", ["야기할", "분간할"], "관심을 기울이다."),
           read_q("자연재해는 천재지변으로 불립니다"), read_q("지진에 강한 인프라를 구축해 놓았습니다"), read_q("자연재해에도 빈익빈 부익부 현상이 나타납니다"), read_q("피해 정도는 인간의 대응에 따라 큰 차이가 납니다"), read_q("풍수해는 지구 온난화와 밀접한 관계가 있습니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("~ 치", "(an old unit of length in Korea) about 3.03 cm", "", "~ 자/척"),
        ("강제적", "(强制的) forceful", "학교에서 보충 수업을 강제적으로 실시하기로 했습니다."),
        ("골칫거리", "a nuisance; a bother; a pest; a headache; “material for brain [use]”", "북한의 핵개발은 국제사회의 오랜 골칫거리이다."),
        ("기울이다", "to devote (oneself) to; to concentrate on; “to lean”", "많은 노력과 주의를 기울여 공부했더니 결과가 좋았다. 지금부터 중요한 내용입니다. 귀를 기울여 잘 들으세요."),
        ("긴밀(하다)", "(緊密) closeness; intimacy; “tight and dense” (to be close; to be intimate)", "", "밀접하다, 가깝다"),
        ("낙엽", "(落葉) a fallen leaf", ""),
        ("논밭", "a farm field; “rice paddy and vegetable field”", ""),
        ("대응책", "(對應策) a countermeasure; a solution", "재난에 대한 대응책을 마련하기 위해 회의를 하고 있습니다."),
        ("분간(하다/되다)", "(分揀) distinguishing (to distinguish/to be distinguished)", "두 사람이 너무 비슷해서 분간하기가 힘들어요.", "구분하다, 식별하다"),
        ("불청객", "(不請客) an uninvited guest; an unwelcome visitor; a gate-crasher; persona non grata", "황사는 봄의 불청객입니다.", "(반갑지 않은) 손님, 방문자"),
        ("산림", "(山林) forest; woods; “mountain forest”", "산림을 보존하려면 어떻게 해야 합니까?"),
        ("산업화(하다/되다)", "(産業化) industrialization (to industrialize/to be industrialized)", "칠십 년대에 산업화가 본격적으로 진행되면서 많은 사람들이 농촌을 떠나 도시를 몰려 들었다.", "공업화"),
        ("야기하다/야기되다", "(惹起) to cause/to be caused", "전쟁을 야기한 근본적 이유가 무엇입니까?"),
        ("이례적", "(異例的) unusual; uncommon", "팔 월에 날씨가 이렇게 춥다니 정말 이례적인 일입니다.", "예외적"),
        ("인체", "(人體) the human body", "담배에는 인체에 해로운 물질이 많습니다.", "신체, 육체"),
        ("황폐화(하다/되다)", "(荒廢化) devastation; ruining (to devastate; to ruin/to be devastated; to be ruined)", "전쟁으로 도시가 황폐화되었습니다."),
    ]),
    ("학습활동 2", [
        ("삼가다/삼가하다", "to abstain from; to refrain from; (삼가다 is correct, but often misused as 삼가하다)", "성인병 환자들은 술과 담배를 삼가야 합니다."),
        ("성분", "(性分) a component; an ingredient", "화장품에서 유해 성분이 검출되었어요."),
        ("수행(하다)", "(遂行) implementation; practice (to implement; to put into practice)", "그 사람은 업무 수행 능력이 아주 뛰어납니다.", "이행(하다), 실행(하다), 실시(하다)"),
        ("엷다", "to be thin; to be light; to be flimsy", "벽을 엷은 파란색으로 칠해 주세요.", "두껍다 | 얇다"),
        ("외피", "(外皮) a crust; a shell; epidermis; “outer skin”", "이 재질은 신발 외피로 사용하면 좋을 것 같아요.", "내피 | 피부"),
        ("호소(하다)", "(呼訴) appeal; complaint (to appeal; to complain)", "환자가 두통을 호소하면 이 약을 주세요."),
    ]),
    ("학습활동 3", [
        ("강타", "(强打) a heavy blow; “strong hit”", "허리케인이 미국 동부지역을 강타했습니다.", "타격"),
        ("구축(하다/되다)", "(構築) establishing (to establish/to be established)", "올해 말까지 와이파이 망을 구축하기로 했어요."),
        ("내진", "(耐震) earthquake-proof; “enduring earthquake”", "올해부터 새로 짓는 건물은 내진 설계를 의무적으로 해야 합니다."),
        ("민·관", "(民·官) (both) civilian and governmental", "민·관이 협동해서 이번 수해를 극복해 나가고 있습니다.", "군·관·민"),
        ("밀접(하다)", "(密接) closeness; intimacy; “dense contact” (to be close; to be intimate)", "한반도는 주변국들과 밀접한 관계를 맺고 있습니다.", "긴밀하다, 가깝다"),
        ("반비례(하다)", "(反比例) an inverse proportion/ratio (to be inversely proportionate)", "실력과 나이가 반비례하는 것은 아니지요.", "비례, 정비례"),
        ("빈국", "(貧國) a poor country", "빈국과 부국간의 격차가 점차 벌어지고 있습니다.", "부국"),
        ("빈부격차", "(貧富隔差) the gap between the rich and the poor", "최근 빈부격차가 너무 심해져서 사회 문제가 되고 있습니다."),
        ("빈익빈 부익부", "(貧益貧 富益富) the widening gulf between rich and poor; “the poor get poorer and the rich get richer”", "최근 빈익빈 부익부 현상이 심화되고 있습니다."),
        ("설계(하다/되다)", "(設計) a design; a plan; a blueprint (to design/to be designed)", "이 건물의 내부 구조를 어떻게 설계해야 할까요?"),
        ("세계기상기구", "(世界氣象機構) the World Meteorological Organization", ""),
        ("요소", "(要素) a factor; an element", "건강은 행복의 필수 요소입니다."),
        ("위력", "(威力) power; force", "허리케인의 위력이 아주 대단해요. 인명 피해와 재산 피해가 심각합니다."),
        ("인재", "(人災) a man-made disaster; a disaster caused by humans", "이번 수해는 천재가 아니라 인재에 가깝습니다.", "천재 | 인재 (人材) a talented/competent man"),
        ("인프라", "infrastructure; “infra”", "우리나라는 정보통신 인프라가 잘 갖추어져 있습니다."),
        ("천재지변", "(天災地變) a natural disaster", "지진은 대표적인 천재지변이다."),
        ("풍수해", "(風水害) disasters caused by wind and water", ""),
        ("해당(하다;되다)", "(該當) relevancy; applicability (to be relevant; to be applicable)", "이 규정은 저에게는 해당되지 않습니다."),
    ]),
]
L5 = lesson(
    "U15 L4 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 골칫거리 · 기울이다 · 대응책 · 불청객 · 산림 · 황폐화 · 강타 · 내진 · 반비례 · 빈국 · 빈부격차 · 인재 · 천재지변 · 풍수해",
    requires=[],
    cards=vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=10)),
)


# ================================================================== L6 Part 3 text
_AUT = [
    ("직장인 절반가량이 가을에 뚜렷한 이유 없이 외롭고 우울해지는 가을증후군을 겪는 것으로 나타났다.", "It turned out that about half of office workers suffer from “autumn syndrome,” becoming lonely and depressed in autumn for no clear reason."),
    ("가을증후군은 가을에 접어들면서 우울함, 외로움 등 이유 없이 나타나는 심리적 증상을 말한다.", "Autumn syndrome refers to psychological symptoms such as depression and loneliness that appear for no reason as autumn sets in."),
    ("취업포털 인크루트는 직장인 " + _kn(1362) + " 명을 대상으로 설문조사한 결과, 사십구 점 칠 퍼센트가 현재 가을증후군을 겪고 있다고 답했다고 이십칠 일 밝혔다.", "The job portal Incruit announced on the 27th that, as a result of a survey of 1,362 office workers, 49.7 percent answered that they are currently suffering from autumn syndrome."),
    ("성별로는 여성이 오십일 점 구 퍼센트, 남성이 사십칠 점 육 퍼센트로 여성이 더 많이 이런 증후군을 겪는 것으로 조사됐다.", "By gender, it was found that women, at 51.9 percent, suffer from this syndrome more than men, at 47.6 percent."),
    ("증상으로는 외롭고 쓸쓸하다가 삼십육 점 영 퍼센트로 가장 많았고 우울하다 (이십 점 칠 퍼센트), 신경이 날카롭다 (십육 점 일 퍼센트) 등이 뒤를 이었다.", "As symptoms, “lonely and desolate” was the most common at 36.0 percent, followed by “depressed” (20.7 percent), “nerves on edge” (16.1 percent) and so on."),
    ("또 이런 증상은 업무에도 영향을 미치는 것으로 나타났다.", "Also, it turned out that these symptoms affect work as well."),
    ("업무에 집중이 안 된다는 답이 십일 점 칠 퍼센트였으며 계속 먹게 된다 (사 점 오 퍼센트), 담배가 늘었다 (사 점 영 퍼센트), 불면증에 시달린다 (삼 점 팔 퍼센트) 등의 차례로 응답이 많았다.", "The answer “cannot concentrate on work” was 11.7 percent, and the answers were many in the order of “keep eating” (4.5 percent), “smoking has increased” (4.0 percent), “suffer from insomnia” (3.8 percent) and so on."),
    ("가을증후군을 극복하기 위해 남성은 운동 (이십구 점 이 퍼센트)을, 여성은 수다 (이십팔 점 사 퍼센트)를 가장 많이 꼽았다.", "To overcome autumn syndrome, men picked exercise (29.2 percent) most, and women picked chatting (28.4 percent) most."),
]
_TADA = [
    ("오늘은 눈이 많이 와서 지하철을 타고 출근했다.", "Today it snowed a lot, so I took the subway to work.", "to ride"),
    ("캘리포니아에 산불이 나서 나무들이 많이 타 버렸다.", "There were wildfires in California and many trees burned up.", "to burn"),
    ("나는 보통 커피에 설탕을 타지 않고 그냥 마십니다.", "I usually drink coffee without mixing in sugar.", "to mix"),
    ("미국인들은 한국인보다 추위를 잘 타지 않는 것 같아요.", "Americans do not seem to be as sensitive to the cold as Koreans.", "to be sensitive to"),
    ("김 일병은 한국말 웅변대회에서 일 등을 해서 상을 탔어요.", "PFC Kim came in first at the Korean speech contest and won a prize.", "to receive"),
    ("생일 풍선이 바람을 타고 하늘로 올라갑니다.", "The birthday balloon rides the wind up into the sky.", "to ride"),
    ("답답하고 속이 타는데, 물 좀 주시겠어요?", "I feel stuffy and my insides are burning; could you give me some water?", "to burn"),
    ("내 친구는 수줍음을 타면 얼굴이 아주 빨갛게 됩니다.", "When my friend gets shy, his or her face turns very red.", "to be sensitive to; to be apt to feel"),
]
_TADA_T = [("A", "지하철을 타고", "4. to ride"), ("B", "나무들이 많이 타 버렸다", "3. to burn"), ("C", "설탕을 타지", "1. to mix"), ("D", "추위를 잘 타지 않는", "5. to be sensitive to; to be apt to feel (same meaning as the title)"), ("E", "상을 탔어요", "2. to receive"), ("F", "바람을 타고", "4. to ride"), ("G", "속이 타는데", "3. to burn"), ("H", "수줍음을 타면", "5. to be sensitive to; to be apt to feel (same meaning as the title)")]
_SPEAK12 = [("가장 많이 타는 계절은 사계절 중 어느 계절입니까?", "Which of the four seasons are you most sensitive to? (my wording of the pair activity)"), ("여자는 봄을 타고 남자는 가을을 탄다는 말에 동의합니까?", "Do you agree with the saying that women are sensitive to spring and men to autumn?"), ("최근에 미국, 한국, 또는 다른 나라에서 발생한 큰 자연 재해와 관련하여 어떤 피해가 있었고 어떤 구호활동이 있었는지 이야기해 보세요.", "Talk about what damage there was and what relief activities there were in connection with a large natural disaster that recently occurred in the United States, Korea or another country.")]
L6 = lesson(
    "U15 L4 · Part 3 (심화 학습): autumn syndrome and the verb 타다",
    "심화 학습 · 가을증후군 · 가을을 타다 · 타다 · 설문조사 · 증상",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): “여성, 남성보다 가을 더 탄다” (Women are more sensitive to autumn than men)",
             "The following newspaper article is about autumn syndrome (Hankyoreh). The book asks five things: (1) which of the underlined 타다 verbs in eight sentences mean the same as in the title, and the meaning of each, (2) the English meaning of 가을증후군, (3) the symptoms in order of frequency, (4) a comparison of men and women, and (5) a pair discussion. The text is the book’s with the numbers spelled out (1362명 is 천삼백육십이 명, 49.7% is 사십구 점 칠 퍼센트, 27일 is 이십칠 일, and so on); the quotation marks are removed, and the book’s “여성(51.9%)이 남성(47.6%)보다” is written with the percentages in the clause so that it reads aloud naturally. The English is mine.",
             examples=passage(_AUT)),
        card("The questions answered (mine)",
             "2. 가을증후군 means “autumn syndrome”: psychological symptoms such as depression and loneliness that appear for no reason as autumn begins.\n\n"
             "3. The symptoms from most to least frequent: lonely and desolate (36.0%), depressed (20.7%), nerves on edge (16.1%); then the effects on work: cannot concentrate on work (11.7%), keep eating (4.5%), smoking has increased (4.0%), suffer from insomnia (3.8%).\n\n"
             "4. Men and women: 51.9% of women and 47.6% of men suffer from it, so women suffer more. To overcome it, men most often pick exercise (29.2%) and women pick chatting (28.4%)."),
        card("The 타다 sentences (my answers)", "The book’s eight sentences A to H. The meaning box was 1. to mix, 2. to receive, 3. to burn, 4. to ride, 5. to be sensitive to; to be apt to feel. The two underlined verbs with the same meaning as the title’s 타다 (sensitive to) are D and H. My answers and translations:",
             tables=[table(["Letter", "The phrase", "Meaning of 타다 (my answer)"], [list(r) for r in _TADA_T]), ktable([(a, b) for a, b, c in _TADA])]),
        card("The pair discussion (speaking)", "Question 5 asks you to discuss in Korean which of the four seasons you are most sensitive to and whether you agree with the saying 여자는 봄을 타고 남자는 가을을 탄다 (women are sensitive to spring and men to autumn). The book’s 말해 봅시다 asks about natural disasters and relief activities. (The English is mine.)", examples=passage(_SPEAK12)),
        card("Activities left out", "학습활동 2 (a radio broadcast for teenagers from the Seoul Education Research & Information Institute: the speaker’s occupation, before-and-after changes, how she categorizes people and their response to unpleasant weather, and her suggestion; then discussing changes in yourself after joining the service) and 학습활동 3 (an animation about an American boy named Jack and a natural disaster in 2004: what he did at each age, a translation of the script 크고 작은 돌부리에 걸려도, 빨간 손수레의 바퀴는 계속 굴렀고 [even when it caught on big and small stones, the wheels of the red hand cart kept rolling] and its implication, and talking about a person who started a drive to help disaster victims) are audio and video activities."),
    ],
    exercises=uniq(
        _tr(_AUT, k=3) + _tr([(a, b) for a, b, c in _TADA], k=3)
        + [M("About how many office workers suffer from autumn syndrome?", "About half", ["About one in ten", "Almost all", "Almost none"], "절반가량."), M("Which group suffers more, men or women?", "Women (51.9% against 47.6%)", ["Men", "They are equal", "Nobody"], "여성이 더 많이."), M("What is the most common symptom?", "Feeling lonely and desolate", ["Insomnia", "Smoking more", "Eating more"], "외롭고 쓸쓸하다."), M("What percentage said they cannot concentrate on work?", "11.7%", ["36.0%", "4.5%", "20.7%"], "십일 점 칠 퍼센트."), M("What do men pick most to overcome it?", "Exercise", ["Chatting", "Eating", "Sleeping"], "운동."), M("What do women pick most to overcome it?", "Chatting", ["Exercise", "Eating", "Smoking"], "수다."), M("How many office workers were surveyed?", "1,362", ["49.7", "51.9", "36"], "천삼백육십이 명."), M("What does 타다 mean in 지하철을 타다?", "to ride", ["to burn", "to mix", "to receive"], "지하철을 타다."), M("What does 타다 mean in 나무가 타다?", "to burn", ["to ride", "to mix", "to receive"], "타다."), M("What does 타다 mean in 커피에 설탕을 타다?", "to mix", ["to ride", "to burn", "to receive"], "설탕을 타다."), M("What does 타다 mean in 상을 타다?", "to receive", ["to ride", "to burn", "to mix"], "상을 타다."), M("What does 타다 mean in 추위를 타다?", "to be sensitive to", ["to ride", "to burn", "to mix"], "추위를 타다."), M("Which sentences use 타다 with the same meaning as the title?", "D and H", ["A and F", "B and G", "C and E"], "추위를 타다, 수줍음을 타다."),
           F("가을에 접어들면서 ___ 이유 없이 우울해지는 것을 가을증후군이라고 한다. (without a clear reason)", "뚜렷한", ["값진", "엷은"], "뚜렷하다."), F("남성은 운동을, 여성은 ___를 가장 많이 꼽았다. (chatting)", "수다", ["골칫거리", "낙엽"], "수다."), F("가을증후군의 증상으로 외롭고 ___가 가장 많았다. (lonely)", "쓸쓸하다", ["환하다", "엷다"], "쓸쓸하다."), F("이런 증상은 업무에도 영향을 ___. (affect)", "미친다", ["삼간다", "호소한다"], "영향을 미치다."), F("친구는 수줍음을 ___ 얼굴이 빨개진다. (is sensitive to)", "타면", ["타고", "타서"], "수줍음을 타다."),
           read_q("직장인 절반가량이 가을증후군을 겪고 있습니다"), read_q("여성이 남성보다 가을을 더 많이 탑니다"), read_q("외롭고 쓸쓸하다가 가장 많았습니다"), read_q("남성은 운동을 여성은 수다를 가장 많이 꼽았습니다"), read_q("미국인들은 추위를 잘 타지 않는 것 같아요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("극복(하다/되다)", "(克服) overcoming; conquest (to overcome; to conquer/to be conquered)", "어려움을 극복하고 성공한 사람들의 이야기를 좋아합니다.", "이기다, 이겨 내다, 정복하다"),
        ("뚜렷하다", "to be apparent; to be clear; to be distinct", "이 문장은 의미가 뚜렷이 전달되지 않아요.", "분명하다"),
        ("수다", "chatting; chats; casual talk", "친구들과 수다를 떨면서 스트레스를 풀어요."),
        ("쓸쓸하다", "to be lonely", "날씨가 쌀쌀해지니까 부쩍 쓸쓸하네요.", "외롭다"),
        ("접어들다", "to go into (a phase, such as a season or time); to enter into", "장마철에 접어들면서 무더위가 시작되고 있습니다."),
        ("타다", "to be sensitive to; to be apt to feel; to be influenced by (weather, shyness, etc.); 타다 to burn; to mix; to receive (an award); to ride", "나는 추위보다 더위를 더 많이 타기 때문에 여름이 싫어요. 내 친구는 수줍음을 타면 얼굴이 아주 빨갛게 된다."),
    ]),
    ("학습활동 2", [
        ("가물가물", "dim; faint; flickering; glimmering (a “mimicking” word that describes flickering)", "저 멀리 불빛이 가물가물 보입니다."),
        ("감상", "(感想) a sentiment; emotion", "가을에는 감상적이 되기 쉽습니다.", "감정 | 감상 (鑑賞) appreciation"),
        ("공개(하다/되다)", "(公開) disclosure; opening to the public (to open; to publicize/to be publicized)", "경찰은 강도 혐의자를 공개 수배했다.", "비밀, 비공개"),
        ("기상캐스터", "(氣象) a weather forecaster; a meteorologist; “weather caster”", ""),
        ("마음가짐", "(mental) attitude", "새 학기가 되어서 마음가짐을 새로 하고 공부를 열심히 하겠습니다.", "마음의 자세 | 몸가짐"),
        ("무대장치", "(舞臺裝置) a stage set", "뮤지컬 무대장치가 잘 돼 있어서 공연이 아주 즐거웠어요."),
        ("시절", "(時節) the season; the time of year; the time; the times", "보통 이 시절에는 비가 많이 온다. 한국도 가난한 시절이 있었다.", "때, 시기"),
        ("오히려", "on the contrary", "친구를 도와주었는데, 고맙다는 말은 안 하고 오히려 도움 받았다고 싫어했어요."),
        ("~조차", "even", "공부를 잘하는 김 일병조차 시험에 떨어졌어요."),
        ("환하다", "to be bright; to be well lit; to be clear; to be unobstructed; to be versed (in); to be familiar (with)", "저녁 일곱 시인데 아직도 밖이 환해요. 이 집은 거리에서 환히 보입니다. 김 선생님은 문법에 환합니다."),
    ]),
    ("학습활동 3", [
        ("값지다", "to be expensive; to be precious; to be valuable; to be priceless", "놀이기구를 타실 때 값진 물건은 잘 보관하시기 바랍니다."),
        ("난민", "(難民) a victim of natural disaster or war; “people in difficulty”", "아이티에 지진이 일어나 난민이 많이 발생했어요."),
        ("돌부리", "a jagged stone; stone with sharp part sticking out of the ground", "돌부리에 걸려 넘어졌어요."),
        ("동참(하다)", "(同參) joining (for noble causes) (to join)", "저도 가난한 이웃을 돕는 일에 동참하고 싶습니다."),
        ("생수", "(生水) freshwater; mineral water; “live water”", "요즘은 물 부족으로 생수 값이 휘발유 값보다 비싸다."),
        ("손수레", "a hand cart", ""),
        ("어느새", "before one realizes; in no time; so soon", "어느새 졸업할 때가 되었네요.", "벌써, 이미, 어느덧"),
        ("여정", "(旅程) an itinerary", "일 박 이 일의 짧은 여정이었지만 여행은 아주 즐거웠어요.", "여행 일정"),
        ("정성", "(精誠) sincerity; sympathy; devotion", "제가 정성을 다해 준비한 음식이에요. 맛있게 드세요.", "성의"),
        ("차곡차곡", "neatly; orderly (a “mimicking” word that describes stacking things neatly)", "책을 아무렇게나 놓지 말고 차곡차곡 정리해 두세요."),
    ]),
]
L7 = lesson(
    "U15 L4 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 극복 · 뚜렷하다 · 수다 · 쓸쓸하다 · 접어들다 · 타다 · 시절 · 오히려 · 환하다 · 난민 · 돌부리 · 동참 · 정성",
    requires=[],
    cards=vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=12, nread=10)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 4: Weather and Natural Disasters (날씨와 자연재해)", [L1, L2, L3, L4, L5, L6, L7])

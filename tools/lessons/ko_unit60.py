"""Unit 60: KBC Semester III, Unit 15, Lesson 5 - Natural Disasters (자연재해).
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
_NV = [("매몰", "submersion; burial", "되다", "지다, 나다", "매몰되다"), ("실종", "a disappearance; going missing", "되다", "답다, 지다", "실종되다"), ("홍수", "a flood", "나다", "시키다, 하다", "홍수가 나다"), ("침수", "flooding; inundation", "되다", "지다, 들다", "침수되다"), ("집중", "concentration", "하다", "나다, 답다", "집중하다"), ("모금", "fund-raising; collecting donations", "하다", "지다, 나다", "모금하다"), ("가뭄", "a drought", "들다", "하다, 시키다", "가뭄이 들다"), ("복구", "restoration; recovery", "하다", "답다, 나다", "복구하다")]
_MATCH = [("산사태 때문에 산 아래 집들이 흙더미에 묻혔습니다.", "Because of the landslide, the houses at the bottom of the mountain were buried under piles of earth."), ("수재민들에게 성금과 구호품이 전달되었습니다.", "Donations and relief goods were delivered to the flood victims."), ("가뭄이 심해서 날씨가 건조합니다.", "Because the drought is severe, the weather is dry."), ("집중호우로 인해서 도로가 물에 잠겼습니다.", "Due to the torrential rain, the roads were submerged in water."), ("사람들이 매몰되면 구조대가 생존자를 수색해야 합니다.", "If people are buried, the rescue squad must search for survivors."), ("바다 밑에서 지진이 일어나면 쓰나미가 발생합니다.", "If an earthquake occurs under the sea, a tsunami occurs."), ("지진이 발생하면 안전한 곳으로 대피해야 합니다.", "If an earthquake occurs, you must evacuate to a safe place.")]
_HJ5 = [("災 재", "disaster", "재해, 수재민"), ("地 지", "earth; ground; place", "지진, 지역"), ("震 진", "tremor; trembling", "미진, 진앙지"), ("失 실", "loss; miss", "실종, 실업"), ("風 풍", "wind", "풍향, 강풍")]
_HJW5 = [("재해", "a disaster"), ("수재민", "flood victims"), ("지진", "an earthquake"), ("지역", "an area"), ("미진", "a slight shock of an earthquake; “small tremor”"), ("진앙지", "an epicenter"), ("실종", "missing"), ("실업", "unemployment; “losing a job”"), ("풍향", "direction of the wind"), ("강풍", "a strong wind")]
_SIM5 = [("재해", "재난", "a disaster ≈ a calamity"), ("지역", "구역", "an area ≈ a district"), ("실업", "실직", "unemployment ≈ losing one’s job"), ("미진", "약진", "a slight shock ≈ a weak earthquake")]
_REL5 = [("여진, 강진, 진도", "지진", "aftershock, strong earthquake, seismic intensity: an earthquake"), ("홍수, 산사태, 가뭄", "재해", "flood, landslide, drought: a disaster"), ("비바람, 폭우, 강풍", "태풍", "wind and rain, heavy rain, strong wind: a typhoon")]
_L5X = [("여진", "an aftershock"), ("강진", "a strong earthquake"), ("진도", "the seismic intensity"), ("산사태", "a landslide"), ("폭우", "heavy rain"), ("비바람", "rain and wind"), ("태풍", "a typhoon"), ("재난", "a calamity"), ("구역", "a district; a zone"), ("실직", "losing one’s job"), ("약진", "a weak earthquake (弱震); the book’s answer"), ("성금", "a donation"), ("구호품", "relief goods"), ("건조하다", "to be dry"), ("흙더미", "a pile of earth"), ("생존자", "a survivor"), ("구조대", "a rescue squad"), ("수색하다", "to search"), ("대피하다", "to evacuate"), ("쓰나미", "a tsunami"), ("집중호우", "torrential rain"), ("녹지", "a green area")]
L1 = lesson(
    "U15 L5 · Review: noun + verb endings and Sino-Korean 災 地 震 失 風",
    "자연재해 · 단어 복습 · 한자어 복습 · 매몰 · 실종 · 홍수 · 침수 · 가뭄 · 복구 · 災 地 震 失 風",
    requires=[],
    cards=[
        card("단어 복습 1: noun + verb ending (my answers)",
             "The book asks you to write the English meaning of each noun and to tick the verb ending that can be attached to the noun (the first, 매몰, is done for you: 매몰되다). The three choices for each noun are the book’s; the ticked one is my answer, and the meanings are mine except for 매몰, which is the book’s.",
             tables=[table(["Noun", "Meaning", "Ending (my answer)", "Other choices", "Whole verb"], [list(r) for r in _NV], say=[0, 4])]),
        card("단어 복습 2: matching the natural-disaster sentences (my pairs)",
             "The book asks you to connect each beginning on the left with the ending that fits (the endings: 날씨가 건조합니다; 도로가 물에 잠겼습니다; 성금과 구호품이 전달되었습니다; 산 아래 집들이 흙더미에 묻혔습니다; 쓰나미가 발생합니다; 생존자를 수색해야 합니다; 안전한 곳으로 대피해야 합니다). My pairs, written as whole sentences (the English is mine):",
             examples=passage(_MATCH)),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ5], say=[2]), ktable(_HJW5)]),
        card("한자어 복습 1: the word with a similar meaning (my answers)", "Circle the word whose meaning is most similar to the word on the left (A. 재해: 재난, 구조, 매몰; B. 지역: 녹지, 진앙지, 구역; C. 실업: 실종, 실패, 실직; D. 미진: 강진, 지진, 약진).", tables=[table(["Word", "Similar word (my answer)", "Meaning"], [[a, b, c] for a, b, c in _SIM5], say=[0, 1])]),
        card("한자어 복습 2: the word that fits the three words (my answers)", "Choose from the box (재해, 지진, 풍향, 태풍) the word most closely related to the three words on each line:", tables=[table(["The three words", "The word from the box (my answer)", "Meaning"], [[a, b, c] for a, b, c in _REL5], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L5X)]),
    ],
    exercises=uniq(
        _tr(_HJW5, k=3) + _tr(_L5X, k=3) + _tr(_MATCH, k=3)
        + [M("Which verb ending goes with 실종?", "되다 (실종되다)", ["나다", "들다", "시키다"], "실종되다."), M("Which verb goes with 홍수?", "나다 (홍수가 나다)", ["되다", "들다", "하다"], "홍수가 나다."), M("Which verb goes with 가뭄?", "들다 (가뭄이 들다)", ["나다", "되다", "하다"], "가뭄이 들다."), M("Which verb goes with 침수?", "되다 (침수되다)", ["나다", "들다", "지다"], "침수되다."), M("Which verb goes with 복구?", "하다 (복구하다)", ["나다", "답다", "지다"], "복구하다."), M("Which verb goes with 모금?", "하다 (모금하다)", ["나다", "지다", "답다"], "모금하다."), M("Which verb goes with 집중?", "하다 (집중하다)", ["나다", "답다", "들다"], "집중하다."),
           M("What does the syllable 災 (재) mean?", "disaster", ["wind", "loss", "tremor"], "재해."), M("What does the syllable 地 (지) mean?", "earth; ground; place", ["wind", "disaster", "loss"], "지진."), M("What does the syllable 震 (진) mean?", "tremor; trembling", ["wind", "loss", "disaster"], "미진."), M("What does the syllable 失 (실) mean?", "loss; miss", ["wind", "tremor", "disaster"], "실종."), M("What does the syllable 風 (풍) mean?", "wind", ["loss", "tremor", "disaster"], "풍향."),
           M("Which word is similar to 재해?", "재난", ["구조", "매몰", "녹지"], "A calamity."), M("Which word is similar to 실업?", "실직", ["실종", "실패", "실수"], "Losing a job."), M("Which word fits 여진, 강진, 진도?", "지진", ["재해", "풍향", "태풍"], "An earthquake."), M("Which word fits 비바람, 폭우, 강풍?", "태풍", ["재해", "지진", "풍향"], "A typhoon."),
           F("산사태 때문에 산 아래 집들이 흙더미에 ___. (were buried)", "묻혔습니다", ["잠겼습니다", "전달되었습니다"], "묻히다."), F("집중호우로 인해서 도로가 물에 ___. (were submerged)", "잠겼습니다", ["묻혔습니다", "발생합니다"], "잠기다."), F("지진이 발생하면 안전한 곳으로 ___ 합니다. (evacuate)", "대피해야", ["수색해야", "전달해야"], "대피하다."), F("바다 밑에서 지진이 일어나면 ___가 발생합니다. (a tsunami)", "쓰나미", ["가뭄", "산사태"], "쓰나미."), F("수재민들에게 성금과 구호품이 ___. (were delivered)", "전달되었습니다", ["묻혔습니다", "발생했습니다"], "전달되다."),
           read_q("지진이 발생하면 안전한 곳으로 대피해야 합니다"), read_q("바다 밑에서 지진이 일어나면 쓰나미가 발생합니다"), read_q("가뭄이 심해서 날씨가 건조합니다"), read_q("재해 지역에 성금을 모금합니다"), read_q("실종자를 수색하고 복구합니다")]
    ),
)

# ================================================================== L2 Part 1
_FACE = [("평안북도 신의주와 중국의 단둥을 연결하는 압록강 철교의 모습이다.", "This is the view of the Yalu River iron bridge connecting Sinuiju in North Pyongan Province and Dandong in China."), ("이 다리를 통해 평양과 베이징 간의 국제 열차가 정기적으로 운행된다.", "International trains between Pyongyang and Beijing run regularly over this bridge.")]
_SUM = [
    ("많은 비와 강한 바람으로 농작물과 집, 도로, 배 등을 파손시키며 여름철에 남부와 중부 지방에 많이 발생.", "Damages crops, houses, roads, ships and so on with heavy rain and strong wind; occurs often in the southern and central regions in summer. (A)"),
    ("짧은 시간에 많은 양의 비가 내려 수해 발생. 장마 기간인 유월에서 칠월에 많이 발생한다. 남부와 중부 지방에 많은 피해.", "A large amount of rain falls in a short time and causes flood damage. Occurs often in June and July, the rainy season. Great damage in the southern and central regions. (B)"),
    ("오랫동안 비가 내리지 않아 농업용수, 공업용수, 식수 등이 부족해진다. 여름에 주로 발생하며 북부 지방과 산간 지역에 많은 피해.", "It does not rain for a long time, so water for agriculture, industry, drinking and so on runs short. Occurs mainly in summer; great damage in the northern region and mountain areas. (C)"),
    ("많은 양의 눈이 내려 교통이 마비되고, 비닐하우스 등이 무너진다. 북부와 산간 지방에 많은 피해. 겨울철에 주로 발생함.", "A large amount of snow falls, traffic is paralyzed and vinyl greenhouses and so on collapse. Great damage in the northern region and mountain regions. Occurs mainly in winter. (D)"),
    ("많은 비와 지진으로 인해 산의 일부가 무너져 내리는 현상으로, 도로가 끊기고 집이 부서지는 등의 피해. 산간 지역에서 많이 발생.", "A phenomenon in which part of a mountain collapses because of heavy rain and earthquakes, with damage such as cut roads and broken houses. Occurs often in mountain areas. (E)"),
]
_ANS1 = [("A", "3", "태풍"), ("B", "5", "호우"), ("C", "1", "가뭄"), ("D", "4", "폭설"), ("E", "2", "산사태")]
_SIN = [
    ("이십일일 압록강이 범람해 북한 평안북도 신의주시와 그 일대가 침수되는 등 홍수피해가 심각한 상황이며, 김정일 국방위원장의 명령으로 수십 대의 비행기와 함정까지 동원해 오천여 명의 주민을 안전하게 구조했다고 조선중앙통신이 전했다.", "On the 21st the Yalu River overflowed and Sinuiju City in North Pyongan Province and its surroundings were flooded; the flood damage is serious, and Korean Central News Agency reported that, by the “order” of the Chairman of the National Defense Commission, Kim Jong-il, dozens of airplanes and even naval vessels were mobilized and about 5,000 residents were rescued safely."),
    ("중앙통신은 “이십일일 영 시부터 아홉 시 사이에 수풍호 주변지역에 내린 삼백 밀리미터 이상의 강한 폭우와 무더기 비로 인해 압록강물이 넘쳐나 신의주의 살림집과 공공건물, 농경지가 백 퍼센트 침수됐다”고 밝혔다.", "The Central News Agency stated, “Because of the strong downpour of more than 300 millimeters and the concentrated heavy rain that fell on the area around Lake Soopoong between 0:00 and 9:00 on the 21st, the Yalu River overflowed and 100 percent of Sinuiju’s residential houses, public buildings and farmland were flooded.”"),
    ("통신은 이어 “지금 이 지역에서는 신의주시를 비롯한 평안북도의 일꾼과 근로자, 조선인민군 군인들이 동원돼 구조전투가 벌어지고 있다”고 덧붙였다.", "The agency went on to add, “In this area now, workers and laborers of North Pyongan Province including Sinuiju City and soldiers of the Korean People’s Army have been mobilized and a rescue battle is under way.”"),
    ("중앙통신은 “이십일일 조선인민군 공군비행기들과 해군함정들이 폭우가 갑자기 들이닥친 평안북도 신의주 지구의 큰물 피해지역으로 긴급출동해 주민들에 대한 구출작전을 성과적으로 벌였다”고 보도했다.", "The Central News Agency reported, “On the 21st, Korean People’s Army air force planes and navy vessels were urgently dispatched to the flood-damaged area of the Sinuiju district of North Pyongan Province, where the downpour had suddenly struck, and carried out a successful rescue operation for the residents.”"),
    ("통신은 “십구 일에서 이십 일 사이 중국 동북지방에 폭우가 쏟아져 압록강의 수위가 갑자기 높아지기 시작해 강물은 잠깐 사이에 제방을 넘어 신의주시내에까지 밀려들어 도로운행이 마비되고 많은 대상들이 피해를 입었다”며, “신의주시는 완전히 물에 잠겨 단층건물들은 지붕만 보이게 되었다”고 밝혔다.", "The agency stated, “Between the 19th and the 20th a downpour fell in northeastern China, the water level of the Yalu River suddenly began to rise, and in a short time the river water went over the embankment and rushed into the city center of Sinuiju, paralyzing road traffic and damaging many facilities,” and, “Sinuiju was completely submerged and only the roofs of the one-story buildings could be seen.”"),
    ("중앙통신은 김정일 국방위원장이 이런 사실을 보고받고 북한군을 구조활동에 나서도록 명령했다고 말했다.", "The Central News Agency said that Chairman Kim Jong-il, having been informed of these facts, ordered the North Korean military to take part in the rescue work."),
    ("이에 따라 공군부대에서는 수십 대의 비행기를, 해군부대에서는 함정과 각종 장비들을 동원하여 위험에 처했던 오천백오십여 명의 주민들을 안전지대로 무사히 옮겼다고 통신은 밝혀 인명피해는 발생하지 않은 것으로 전했다.", "Accordingly, the agency stated that the air force units mobilized dozens of airplanes and the navy units mobilized vessels and various equipment and safely moved about 5,150 residents who had been in danger to a safe zone, and it reported that no human casualties occurred."),
]
_NKW = [("무더기 비", "a concentrated heavy rain; “piled rain”", "집중호우, 폭우"), ("살림집", "a residential house; “living house”", "가정집"), ("큰물", "a flood; floodwater; “big water”", "홍수")]
_SPEAK12 = [("최근에 국내 또는 외국에서 발생한 자연재해에 대해서 서로 이야기해 보세요.", "Talk to each other about natural disasters that occurred recently in Korea or abroad."), ("캘리포니아에서는 지진이 자주 발생합니다. 지진이 발생하면 어떻게 대처해야 하는지 서로 이야기해 보세요.", "Earthquakes often occur in California. Talk to each other about how to respond when an earthquake occurs."), ("또, 태풍이 발생할 경우에는 어떻게 대처하는지 서로 이야기해 보세요.", "Also, talk to each other about how to respond when a typhoon occurs.")]
L2 = lesson(
    "U15 L5 · Part 1 (도입 학습): the Yalu and Tumen rivers, hazards, the Sinuiju flood",
    "도입 학습 · 압록강과 두만강 · 폭설 · 호우 · 가뭄 · 산사태 · 태풍 · 신의주 · 큰물 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 압록강 and 두만강 (the Yalu River and the Tumen River) — the book’s note",
             "Both rivers originate from 백두산, the highest mountain in the Korean peninsula. 백두산 is located between North Korea and China. 압록강 runs 790 km along the border between North Korea and China and empties into the West Sea; 두만강 runs 521 km along the border between North Korea, China, and Russia, and empties into the East Sea. 압록강 is the longest river on the peninsula, with waters that are swift, deep, and voluminous, making it a good source of hydroelectric power. 수풍호 (Lake Soopoong) and 수풍댐 (Spoong Dam) are on the river and form the largest reservoir in North Korea. 신의주 is the largest North Korean city on 압록강.\n\n"
             "두만강, in contrast, is relatively shallow and narrow, and is frequently used by North Korean defectors. Although heavily patrolled by North Korean guards, the river is easily crossed in spots on foot or by swimming. In 1995, the People’s Republic of China, Mongolia, Russia, and South Korea signed agreements to create the Tumen River Economic Development Area. The biggest city on 두만강 is 회령.\n\n"
             "The book’s picture caption (the English is mine):", examples=passage(_FACE)),
        card("학습활동 1 (Reading): natural disasters A–E",
             "Read the following summaries of various natural disasters and, from the box (1. 가뭄, 2. 산사태, 3. 태풍, 4. 폭설, 5. 호우), write the number of the corresponding natural hazard. The summaries, in the book’s words (with 6~7월 spelled out; the English is mine):",
             examples=passage(_SUM)),
        card("학습활동 1: my answers", "", tables=[table(["Summary", "Number", "Natural hazard"], [list(r) for r in _ANS1], say=[2])]),
        card("학습활동 3 (Reading): the Sinuiju flood (a Yonhap report quoting the Korean Central News Agency)",
             "The following newspaper article is a report on a weather disaster, quoting North Korea’s Korean Central News Agency (© Yonhapnews). The text is the book’s with the numbers and units spelled out (21일 is 이십일일; 0시부터 9시 is 영 시부터 아홉 시; 300 mm is 삼백 밀리미터; 100% is 백 퍼센트; 19~20일 is 십구 일에서 이십 일; 5천여 명 is 오천여 명; 5천150여 명 is 오천백오십여 명); the quotation marks ‘ ’ around 명령 are removed. The English is mine.",
             examples=passage(_SIN)),
        card("학습활동 3: the questions answered (mine)",
             "1. The natural hazard and its effect: the Yalu River overflowed after heavy rain; about 300 mm or more of rain fell in the area around Lake Soopoong in nine hours on the 21st, and heavy rain fell in northeastern China on the 19th and 20th. Sinuiju and the area around it were flooded: 100% of the houses, public buildings and farmland were inundated, road traffic was paralyzed, and the city was so completely under water that only the roofs of one-story buildings could be seen.\n\n"
             "2. The rescue efforts: the initiator was Chairman Kim Jong-il, who ordered the military (as the news agency reported) to rescue the people. The participants were air force units (dozens of airplanes), navy units (vessels and equipment), Korean People’s Army soldiers, and the workers and laborers of North Pyongan Province including Sinuiju. The victims rescued were about 5,150 residents, who were moved to a safe zone; no human casualties were reported.\n\n"
             "3. The verb(s) associated with the underlined subject: the underline is not visible in the text of the book. The subject of the quoted statements is 중앙통신 (통신), and the verbs associated with it are 전했다, 밝혔다, 덧붙였다, 보도했다 and 말했다.\n\n"
             "4. Translation: “Sinuiju was completely submerged, and only the roofs of the one-story buildings could be seen.”\n\n"
             "5. North Korean words (below).",
             tables=[table(["North Korean word", "English meaning", "South Korean equivalent"], [list(r) for r in _NKW], say=[0, 2])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK12)),
        card("Activities left out", "학습활동 1, question 2 (listening to a natural disaster warning, naming the hazard in English and circling the likely actions: evacuate to higher ground; escape from the forest to the waterfront; take cover where they are, securing drinking water; find fire extinguishers and wait until 6:30 for further notice) and 학습활동 2 (four YTN news reports about natural disasters in several countries, completing a table of natural disaster, country, casualties and damage) are audio activities."),
    ],
    exercises=uniq(
        _tr(_SUM, k=3) + _tr(_SIN, k=3) + _tr(_FACE, k=2) + _tr(_SPEAK12, k=2) + _tr([(x, y) for x, y, z in _NKW], k=2)
        + [M("Which hazard is summary A (heavy rain and strong wind damaging crops, houses, roads, ships)?", "태풍 (typhoon)", ["폭설", "가뭄", "산사태"], "3."), M("Which hazard is summary B (a lot of rain in a short time, in the rainy season)?", "호우 (torrential rain)", ["가뭄", "폭설", "태풍"], "5."), M("Which hazard is summary C (it does not rain for a long time)?", "가뭄 (drought)", ["호우", "폭설", "산사태"], "1."), M("Which hazard is summary D (a lot of snow, traffic paralyzed)?", "폭설 (heavy snow)", ["가뭄", "태풍", "호우"], "4."), M("Which hazard is summary E (part of a mountain collapses)?", "산사태 (landslide)", ["태풍", "가뭄", "폭설"], "2."),
           M("How long is the 압록강 according to the book?", "790 km", ["521 km", "1,000 km", "300 km"], "The book’s note."), M("How long is the 두만강 according to the book?", "521 km", ["790 km", "300 km", "1,000 km"], "The book’s note."), M("Where do both rivers originate?", "백두산", ["한라산", "금강산", "설악산"], "Both start at 백두산."), M("What is the largest North Korean city on the 압록강?", "신의주", ["회령", "평양", "개성"], "신의주."), M("What is the biggest city on the 두만강?", "회령", ["신의주", "평양", "남포"], "회령."), M("Which river is shallow and narrow and often used by defectors?", "두만강", ["압록강", "한강", "대동강"], "The book’s note."),
           M("How many residents were rescued in the Sinuiju report?", "About 5,150", ["About 300", "About 21", "About 100"], "오천백오십여 명."), M("What percent of Sinuiju’s houses, public buildings and farmland were flooded?", "100 percent", ["50 percent", "30 percent", "10 percent"], "백 퍼센트."), M("Who ordered the rescue, according to the report?", "Kim Jong-il", ["The South Korean president", "The Chinese army", "A rescue squad"], "김정일 국방위원장."), M("What did only the roofs show in Sinuiju?", "One-story buildings", ["Tall buildings", "Bridges", "Trains"], "단층건물들은 지붕만 보이게 되었다."),
           F("압록강이 ___해 신의주시가 침수되었다. (overflowed)", "범람", ["수습", "복구"], "범람하다."), F("비행기와 함정까지 ___해 주민을 구조했다. (mobilized)", "동원", ["범람", "침수"], "동원하다."), F("강한 폭우와 ___ 비로 압록강물이 넘쳐났다. (concentrated heavy)", "무더기", ["단층", "큰물"], "무더기 비."), F("신의주시는 완전히 물에 ___. (was submerged)", "잠겼다", ["묻혔다", "말랐다"], "물에 잠기다."), F("인명피해는 ___ 않은 것으로 전했다. (did not occur)", "발생하지", ["동원하지", "범람하지"], "발생하다."),
           read_q("압록강이 범람해 신의주시가 침수되었습니다"), read_q("많은 비와 강한 바람으로 농작물과 집이 파손됩니다"), read_q("오랫동안 비가 내리지 않아 식수가 부족해집니다"), read_q("신의주시는 완전히 물에 잠겼습니다"), read_q("인명피해는 발생하지 않았습니다"), read_q("최근에 발생한 자연재해에 대해서 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("~용수", "(用水) water used for (agriculture, factories, etc.)", "", "농업용수, 공업용수, 산업용수"),
        ("농작물", "(農作物) crops; farm produce", "폭풍으로 농작물 피해가 심각합니다.", "농산물"),
        ("민방위", "(民防衛) civil defense", "한국에서는 정기적으로 민방위훈련이 실시됩니다."),
        ("범람(하다)", "(汎濫) flooding; inundation (to flood; to flow over)", "집중호우로 계곡의 물이 범람하여 야영하던 사람들이 대피했다.", "넘치다, 홍수가 나다"),
        ("수해", "(水害) flood damage; “water damage”", "이 지역은 매년 수해 피해를 입습니다.", "재해, 풍해"),
        ("식수", "(食水) drinking water; potable water", "수해 지역 이재민들이 식수 부족으로 어려움을 겪고 있습니다.", "음료수 | 식수 (植樹) planting trees"),
    ]),
    ("학습활동 2", [
        ("고대", "(古代) (an) ancient (time)", "고대 그리스와 로마의 역사는 아주 재미있습니다.", "현대, 근대, 중세"),
        ("깔리다", "to be buried/crushed under; to be spread", "건물이 붕괴돼서 건물 밑에 깔린 채 일주일을 지냈어요.", "덮다, 덮히다"),
        ("덮치다", "to fall upon; to attack; to overtake", "큰 파도가 덮쳐서 배가 뒤집혔습니다.", "덮다, 덮히다"),
        ("동반(하다/되다)", "(同伴) accompanying (to accompany/to be accompanied)", "오늘 저녁 바람을 동반한 눈이 내리겠습니다.", "수반하다, 함께 하다"),
        ("맹위를 떨치다", "(猛威) to rage; to be furious (referring to extreme weather)", "강추위가 벌써 일주일 동안 맹위를 떨치고 있다."),
        ("사원", "(寺院) a temple", "", "사원 (社員) a company employee"),
        ("속출(하다)", "(續出) repeated occurrence (to occur again and again)", "이 구간에서 사고가 속출하고 있어요. 각별한 주의가 요구됩니다."),
        ("수습(하다/되다)", "(收拾) control; solving (to control; to solve/to be controlled; to be solved)", "이번 사태를 수습하는 데 많은 시간이 걸릴 것이다.", "해결(하다)"),
        ("잇따르다/잇달다", "to succeed (back to back); to follow one after another", "잇따른 태풍으로 제주도는 많은 피해를 입었습니다.", "계속되다, 이어지다"),
        ("전면", "(全面) entire(ly); all-out; “whole surface”", "금강산 관광객의 총격 사망 사건 때문에 금강산 관광이 전면 중단됐다.", "전면적으로 | 전면 (前面) the front (side); “front face”"),
        ("전언", "(傳言) news; tidings", "아프리카 난민들이 어려움을 겪고 있다는 전언입니다.", "소식, 전달"),
        ("희생자", "(犧牲者) a victim", "이번 대형화재로 인해 많은 희생자가 발생했습니다."),
    ]),
    ("학습활동 3", [
        ("일대", "(一帶) the whole area/place; throughout (the area)", "남부지방 일대에 무더위가 극심합니다."),
        ("넘치다/넘쳐나다", "to overflow", "병원이 환자들로 넘쳐납니다."),
        ("농경지", "(農耕地) farmland; agricultural land", "이번 홍수로 농경지가 침수되었습니다.", "농지, 논밭"),
        ("단층", "(單層) one-story (building, house, etc.)", "저는 이층집보다 단층집이 더 좋습니다.", "일층(짜리)"),
        ("무더기 비", "a (concentrated) heavy rain; “piled rain”", "무더기 비로 많은 인민들이 피해를 보고 있습니다.", "집중호우, 폭우"),
        ("무사히", "(無事) safely; safe and sound; “with no accident”", "삼 개월 동안 긴 여행을 마치고 무사히 귀국했다."),
        ("살림집", "a residential house; “living house”", "일 층에서는 식당을 운영하고 이 층은 살림집으로 쓰고 있어요.", "가정집"),
        ("수위", "(水位) the level of water; “water position”", "당국은 지금 댐의 수위를 조절하고 있어요."),
        ("인명피해", "(人命被害) human casualties", "지진으로 인명피해가 심각합니다."),
        ("일꾼", "a worker", "김 영호 씨는 우리 회사에서 꼭 필요한 일꾼입니다."),
        ("침수(되다)", "(浸水) flooding; inundation (to be flooded)", "집중호우로 강변 도로가 침수되면서 교통이 통제되고 있다."),
        ("큰물", "a flood; floodwater; “big water”", "이 지역은 큰물 피해가 심각합니다.", "홍수"),
    ]),
]
L3 = lesson(
    "U15 L5 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 용수 · 농작물 · 범람 · 수해 · 식수 · 깔리다 · 덮치다 · 속출 · 수습 · 희생자 · 농경지 · 수위 · 침수 · 큰물",
    requires=[],
    cards=vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=10, nread=10)),
)

# ================================================================== L4 Part 2 text
_ED5 = [
    ("한나라당 지도부가 정부에 대북 쌀지원 문제를 제안했다고 한다.", "It is said that the leadership of the Grand National Party proposed the issue of rice aid to North Korea to the government."),
    ("북한의 홍수 피해 상황은 언론이 전하는 사진과 화면을 통해 미루어 짐작할 수 있다.", "The flood damage situation in North Korea can be inferred through the photos and screens that the press conveys."),
    ("압록강의 범람으로 신의주 주변의 들판은 바다로 변했으며 주택들은 지붕만 남았다.", "Because of the overflowing of the Yalu River, the fields around Sinuiju turned into a sea, and only the roofs of the houses remained."),
    ("북한 조선중앙통신은 지난 주말 내린 폭우로 신의주의 주택과 공공건물, 농경지가 백 퍼센트 침수됐다고 보도했다.", "North Korea’s Korean Central News Agency reported that, because of the downpour that fell last weekend, 100 percent of Sinuiju’s houses, public buildings and farmland were flooded."),
    ("북한은 인명 구조를 위해 군 비행기와 함정까지 동원하고 있다.", "North Korea is mobilizing even military airplanes and vessels for the rescue of lives."),
    ("북한에서는 지난달 하순 개성과 흥남 일대에 내린 폭우로 이미 많은 인명 피해와 함께 농경지가 침수된 바 있다.", "In North Korea, in the last ten days of last month, heavy rain that fell around Kaesong and Hungnam had already flooded farmland along with many human casualties."),
    ("그러지 않아도 만성적 식량난을 겪어온 북한 주민들의 생활이 이번 수해로 더욱 어려워질 것은 불 보듯 뻔하다.", "It is as plain as fire that the lives of the North Korean residents, who were suffering a chronic food shortage even without this, will become more difficult because of this flood damage."),
    ("북한 주민이 수해로 고통을 겪는 것은 시각을 다투는 인도적 문제다.", "The North Korean residents’ suffering from the flood damage is a humanitarian problem that is a race against the clock."),
    ("정부가 대북 식량지원을 정치적 문제와 연계시켜 북한에 대한 압박용으로 이용하는 것은 인도주의에 반하는 정략적 자세다.", "For the government to link food aid to North Korea with political problems and use it as a means of pressure on North Korea is a politically motivated attitude that goes against humanitarianism."),
    ("더욱이 지금은 엄청난 홍수로 북한이 외부세계의 도움을 절실히 필요로 하는 때다.", "Moreover, now is the time when North Korea acutely needs help from the outside world because of the enormous flood."),
    ("정부가 인도적 차원에서 대북 식량지원을 한다면 북한 주민의 긴급한 생활고를 덜 수 있을 뿐 아니라, 결과적으로 넘쳐나는 쌀 재고 관리와 꽉 막힌 남북관계의 변화도 가져올 수 있다.", "If the government provides food aid to North Korea on humanitarian grounds, it can not only lighten the urgent hardships of the North Korean residents but also, as a result, bring about the management of the overflowing rice stock and a change in the tightly blocked inter-Korean relations."),
    ("일석삼조의 효과를 기대할 수 있는 셈이다.", "It amounts to being able to expect the effect of “one stone, three birds.”"),
    ("여당인 한나라당까지 태도 변화를 보이는 만큼 이제 정부가 변할 차례다.", "Now that even the ruling party, the Grand National Party, shows a change of attitude, it is now the government’s turn to change."),
    ("정부가 더 이상 북한에 대한 식량지원을 미루는 것은 매우 어리석은 일이다.", "For the government to postpone food aid to North Korea any longer is a very foolish thing."),
]
_IDI = [
    ("삼삼오오", "三三五五", "in twos and threes; in small groups", "야영장에서 학생들이 삼삼오오 모여 앉아 얘기를 하고 있습니다."),
    ("구사일생", "九死一生", "a narrow escape from death; “nine deaths, one life”", "그는 큰 사고에서 구사일생으로 살아났습니다."),
    ("백발백중", "百發百中", "hitting the target every time; “a hundred shots, a hundred hits”", "그 선수의 활 솜씨는 백발백중입니다."),
    ("십중팔구", "十中八九", "in eight or nine cases out of ten; most likely", "이렇게 흐리면 십중팔구 비가 올 거예요."),
    ("오십보백보", "五十步百步", "little difference; “fifty steps, a hundred steps”", "두 팀의 실력은 오십보백보입니다."),
    ("일거양득", "一擧兩得", "two gains from one action; killing two birds with one stone", "운동을 하면서 친구도 사귀니 일거양득입니다."),
    ("천차만별", "千差萬別", "a great variety; “a thousand differences, ten thousand distinctions”", "사람마다 생각이 천차만별입니다."),
    ("칠전팔기", "七顚八起", "never giving up; “fall seven times, get up eight”", "칠전팔기의 정신으로 시험에 다시 도전했습니다."),
]
_SPEAK13 = [("북한은 반복되는 가뭄과 홍수로 식량난을 겪고 있습니다. 미국의 대북 식량 지원에 대해 의견을 교환해 보세요.", "North Korea is suffering a food shortage because of repeated droughts and floods. Exchange opinions about U.S. food aid to North Korea."), ("미국이 지원을 해야 하는지, 지원을 하면 어떻게 해야 하는지 서로 이야기해 보세요.", "Talk to each other about whether the United States should give aid and, if it gives aid, how it should do so."), ("고향에서 발생하는 자연재해에 대해 이야기해 보세요.", "Talk about the natural disasters that occur in your hometown."), ("직접 경험한 것이 있으면 그 경험을 말해 보세요.", "If you have experienced one yourself, tell about that experience.")]
L4 = lesson(
    "U15 L5 · Part 2 (본 학습): an editorial on rice aid to North Korea",
    "본 학습 · 사설 · 대북 쌀지원 · 머뭇거릴 때 아니다 · 한자 성어 · 삼삼오오 · 일거양득 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3 (Reading): an editorial, “대북 쌀지원 더 이상 머뭇거릴 때 아니다”",
             "The following is a newspaper editorial (Kyunghyang), titled “[사설] 대북 쌀지원 더 이상 머뭇거릴 때 아니다” (Editorial: It is no longer time to hesitate over rice aid to North Korea). The text is the book’s with 100% spelled out (백 퍼센트) and 1석3조 spelled out (일석삼조). The English is mine.",
             examples=passage(_ED5)),
        card("The questions answered (mine)",
             "1. The writer’s main point: the South Korean government should stop hesitating and send food (rice) aid to flood-stricken North Korea for humanitarian reasons, and should not tie it to politics or use it as pressure.\n\n"
             "2. The statement that most accurately reflects the editorial is B: the recent flooding will worsen North Korea’s existing food shortage. (A is wrong: nothing says North Korea rejected aid. C is wrong: the ruling party proposed it, but not as “a donation of rice”; D is wrong: the editorial urges the government, which has not yet acted.)\n\n"
             "3. 1석3조 (“one stone, three birds”) is the writer’s version of 일석이조. The 1석 (one stone) is the humanitarian food aid to North Korea. The 3조 (three birds) are: (1) relieving the North Korean residents’ urgent hardship, (2) managing South Korea’s overflowing rice stock, and (3) bringing about a change in the tightly blocked inter-Korean relations.\n\n"
             "4. The idioms: the book’s first example is 삼삼오오; the meanings and the example sentences for the others are mine (see the table below)."),
        card("학습활동 3 question 4: Sino-Korean idioms (한자 성어) with a Sino-Korean number",
             "The book asks you to check the meaning in a dictionary or with your teacher and then to write an example sentence (the first one, 삼삼오오, is done for you). Meanings and example sentences (apart from the first) are mine.",
             tables=[table(["Idiom", "Hanja", "Meaning", "Example"], [list(r) for r in _IDI], say=[0, 3])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK13)),
        card("Activities left out", "학습활동 1 (a North Korean weather forecast from Korean Central Broadcasting: today’s general weather pattern, tomorrow’s forecast for Pyongyang and Kaesong, today’s date by the solar and lunar calendars, and what the forecaster calls North Korea) and 학습활동 2 (a North Korean broadcast campaign against a natural disaster: the subject, the sector most vulnerable and the measures, and two other sectors mentioned) are audio and video activities."),
    ],
    exercises=uniq(
        _tr(_ED5, k=3) + _tr(_SPEAK13, k=2)
        + [M("What is the writer’s main point?", "The government should send food aid to North Korea now, on humanitarian grounds", ["North Korea should ask for rice", "The flood was not serious", "Rice should be exported"], "머뭇거릴 때 아니다."), M("Which statement reflects the editorial?", "The flood will worsen North Korea’s food shortage", ["North Korea rejected aid", "The government has already acted", "There was no damage"], "B."), M("What does 일석삼조 mean in the editorial?", "Three benefits from one action", ["Two benefits from one action", "A rice shortage", "A flood"], "One stone, three birds."), M("Which is NOT one of the three birds?", "Raising the price of rice", ["Relieving residents’ hardship", "Managing the rice stock", "Improving inter-Korean relations"], "The three benefits."),
           M("What percent of Sinuiju’s homes, public buildings and farmland were flooded?", "100 percent", ["10 percent", "50 percent", "None"], "백 퍼센트."), M("What did the fields around Sinuiju become?", "A sea", ["A forest", "A desert", "A road"], "바다로 변했다."), M("What is the aid described as?", "A humanitarian issue", ["A political bargain", "A trade deal", "A military matter"], "인도적 문제."), M("What does the editorial call the government’s linking aid to politics?", "A politically motivated attitude", ["A wise policy", "A humane gesture", "A routine habit"], "정략적 자세."),
           M("What does 삼삼오오 mean?", "In twos and threes; in small groups", ["Alone", "All together", "In a line"], "三三五五."), M("What does 구사일생 mean?", "A narrow escape from death", ["A long life", "A birth", "A rich life"], "九死一生."), M("What does 백발백중 mean?", "Hitting the target every time", ["Missing every time", "Waiting a hundred days", "A hundred people"], "百發百中."), M("What does 십중팔구 mean?", "In eight or nine cases out of ten; most likely", ["Rarely", "Ten people", "Exactly half"], "十中八九."), M("What does 오십보백보 mean?", "Little difference", ["A great difference", "A long walk", "A hundred people"], "五十步百步."), M("What does 일거양득 mean?", "Two gains from one action", ["Two losses", "One loss", "One gain only"], "一擧兩得."), M("What does 천차만별 mean?", "A great variety", ["Exactly alike", "A thousand years", "A single type"], "千差萬別."), M("What does 칠전팔기 mean?", "Never giving up", ["Giving up quickly", "Seven people", "A lucky number"], "七顚八起."),
           F("정부는 지원을 더 이상 ___ 때가 아니다. (hesitating)", "머뭇거릴", ["미룰까", "서두를"], "머뭇거리다."), F("사진과 화면을 통해 ___ 짐작할 수 있다. (inferring)", "미루어", ["다그쳐", "따져"], "미루어 짐작하다."), F("피해가 커질 것은 불 보듯 ___. (obvious)", "뻔하다", ["어렵다", "많다"], "불 보듯 뻔하다."), F("이것은 시각을 ___ 인도적 문제다. (race against the clock)", "다투는", ["미루는", "정하는"], "시각을 다투다."), F("그는 큰 사고에서 ___으로 살아났습니다. (a narrow escape)", "구사일생", ["백발백중", "삼삼오오"], "구사일생."), F("운동을 하면서 친구도 사귀니 ___입니다. (two gains from one action)", "일거양득", ["천차만별", "오십보백보"], "일거양득."),
           read_q("대북 쌀지원을 더 이상 미루지 마십시오"), read_q("북한 주민들의 생활이 더욱 어려워질 것은 불 보듯 뻔합니다"), read_q("북한 주민이 수해로 고통을 겪는 것은 인도적 문제입니다"), read_q("학생들이 삼삼오오 모여 앉아 있습니다"), read_q("사람마다 생각이 천차만별입니다"), read_q("칠전팔기의 정신으로 도전했습니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("소낙비", "a shower; a torrential rain", "", "소나기"),
        ("위성 화상", "(衛星 畵像) a satellite picture", "", "위성 사진"),
        ("여드레", "the eighth day (of the month); (a period of) eight days", "이 공연은 여드레 동안 열립니다.", "이레, 아흐레"),
        ("초복", "(初伏) the first of three periods of dog days (hot days) in summer", "초복이 되어서 날씨가 아주 덥습니다.", "중복, 말복, 삼복, 삼복 더위"),
    ]),
    ("학습활동 2", [
        ("고인 물", "stagnant water; “accumulated water”", "고인 물에서 악취가 심하게 납니다."),
        ("다그치다", "to press; to urge; to impel; to spur on", "어머니가 공부를 하라고 계속 다그치자 아이는 밖으로 나가 버렸다."),
        ("단위", "(單位) a unit", "중국의 화폐단위는 위안이다."),
        ("대고조", "(大高潮) the Great Leap (an overarching slogan); “great high tide”", ""),
        ("물길", "a water route; “water way”", "", "수로"),
        ("물도랑", "a ditch", ""),
        ("배수", "(排水) draining (of water)", "배수가 되지 않아 물이 넘치고 있어요."),
        ("배수로", "(排水路) a draining chute; a draining cut; “draining road”", "이곳에 배수로를 만들어 물을 뺍시다."),
        ("보강(하다/되다)", "(補强) reinforcement; strengthening (to reinforce; to strengthen/to be reinforced; to be strengthened)", "체력을 보강하기 위해 특별 훈련을 하고 있어요.", "보강 (補講) a make-up class"),
        ("부문", "(部門) an area; a sector", "남북한의 교류는 경제부문과 문화부문에서 가장 활발했다."),
        ("비바람", "rain and wind", "지금 비바람이 너무 심해요. 조금 이따 출발하도록 해요.", "풍우"),
        ("실현(하다/되다)", "(實現) realization (to realize/to be realized)", "저는 꿈을 실현하기 위해 열심히 노력하고 있어요.", "이루다, 이루어지다"),
        ("안전대책", "(安全對策) a safety measure", "정부는 안전대책을 마련하기 위해 고심하고 있습니다."),
        ("양수장", "(揚水場) a water-pumping site", "", "양수기"),
        ("예비 부속품", "(豫備 附屬品) a spare part", ""),
        ("자재관리", "(資材管理) management of materials", "저는 지금 자재관리 부서에서 일하고 있어요."),
        ("저수지", "(貯水池) a reservoir", "오랜 가뭄으로 저수지가 다 말라 버렸어요."),
        ("정비 보수", "(整備 補修) maintenance and repairs", "이 건물은 지금 정비 보수를 하고 있습니다."),
        ("정상화(하다/되다)", "(正常化) normalization (to normalize/to be normalized)", "한일 양국은 관계를 정상화하기 위해 회담을 하고 있습니다."),
        ("철길", "(鐵) a railroad; “steel road”", ""),
        ("철다리", "(鐵) a railway bridge; “steel bridge”", "", "철교"),
        ("협동농장", "(協同農場) a collective farm; “cooperation farm”", ""),
    ]),
    ("학습활동 3", [
        ("일석이조", "(一石二鳥) killing two birds with one stone; “one stone, two birds” (the book writes 1석2조)", "담배를 끊으면 돈도 절약되고 건강해지니 일석이조입니다. 꼭 끊으세요.", "일거양득"),
        ("들판", "a (flat) field", ""),
        ("만성적", "(慢性的) chronic; habitual; inveterate", "저는 만성적 피로에 시달리고 있어요."),
        ("머뭇거리다", "to hesitate; to waive; to dawdle", "얼른 대답을 못하고 머뭇거렸다.", "망설이다, 주저하다, 머무적거리다"),
        ("미루다", "to postpone; to delay", "갑자기 일이 생겨서 회의를 미뤄야 할 것 같아요."),
        ("미루어 짐작하다", "(斟酌) to guess; to infer; to surmise; “to guess by inferring”", "그 사람이 말하는 것을 들어 보니 어떤 생각을 하는지 미루어 짐작할 수 있어요."),
        ("불 보듯 뻔하다", "to be (too) obvious; to be self-evident; “to be as plain as (you) see fire”", "이 계획은 실패할 것이 불 보듯 뻔합니다.", "명백하다, 분명하다, 명약관화하다"),
        ("시각을 다투다", "(時刻) to be in haste; to be urgent; “to fight against the clock”", "저는 매일 시각을 다투며 바쁘게 일하고 있어요."),
        ("식량난", "(食糧難) food crisis; food shortage", "북한 주민들은 극심한 식량난에 시달리고 있습니다."),
        ("압박(하다/받다)", "(壓迫) pressure (to press/to be pressed)", "국제사회는 북한을 압박해 육자 회담에 나오게 하려고 합니다."),
        ("연계(하다/시키다/되다)", "(連繫) linking; association (to link; to associate/to be linked; to be associated)", "이 프로그램은 기업과 바로 연계돼 있습니다."),
        ("인도적", "(人道的) humanitarian", "국제 사회는 이 문제를 인도적 문제로 접근하려고 합니다."),
        ("절실(하다)", "(切實) acuteness; poignancy (to be acute; to be poignant)", "북한은 지금 외부 세계의 도움이 절실히 필요합니다."),
        ("정략적", "(政略的) political; politically motivated", "이 문제는 정략적으로 해결하려고 하지 말고 인도적 차원에서 해결합시다."),
        ("지도부", "(指導部) a guidance division; a fostering division; leadership division", "당 지도부가 사퇴하기로 결정했습니다."),
        ("지원(하다/받다)", "(支援) support (to support/to be supported)", "북한은 국제 사회의 지원을 거부하고 있습니다.", "지원 (志願) application"),
        ("화면", "(畵面) a (TV/monitor) screen", "티브이 화면이 너무 어두워요. 조금 더 밝게 해 보세요."),
    ]),
]
L5 = lesson(
    "U15 L5 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 소낙비 · 여드레 · 초복 · 배수로 · 부문 · 비바람 · 저수지 · 정상화 · 만성적 · 머뭇거리다 · 불 보듯 뻔하다 · 식량난 · 인도적 · 정략적",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book writes the examples for 일석이조 (1석2조), 압박 (6자 회담) and 화면 (TV화면) with digits and letters; they are spelled in Hangul here (육자 회담, 티브이 화면). The book lists 연계(하다; 시키다/되다) with a semicolon; it is written 연계(하다/시키다/되다) here.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3 text
_HUN = [
    ("신문, 방송에서 아프리카 어떤 국가에서는 가뭄과 내전으로 많은 사람들이 기아에 허덕인다는 소식을 종종 접한다.", "In newspapers and on broadcasts, we often hear news that in some African countries many people are struggling with starvation because of drought and civil war."),
    ("가끔은 뼈만 앙상하게 남아 눈물마저 마른 어린아이의 사진이 함께 눈에 들어올 때도 있다.", "Sometimes a photo of a small child, with only bones left and even the tears dried up, catches the eye along with it."),
    ("마음 한구석이 불편하면서도, 이는 자연재해와도 같은 어쩔 수 없는 일이라고 여긴 적이 있다.", "Although a corner of my heart felt uneasy, I once regarded this as something unavoidable, like a natural disaster."),
    ("심지어 인구과잉을 조절하는 자연현상의 하나일지 모른다는 생각까지 하면서.", "I even thought that it might be one of the natural phenomena that regulate overpopulation."),
    ("유엔 식량 특별조사관인 장 지글러가 쓴 책 왜 세계의 절반은 굶주리는가를 읽지 않았다면 나의 이런 생각은 변하지 않았을지도 모르겠다.", "If I had not read the book Why Is Half of the World Hungry? by Jean Ziegler, the U.N. special rapporteur on food, my thinking might not have changed."),
    ("책에 따르면 지구 전체적으로 현재 전 세계 인구보다 많은 백이십억 명이 먹고도 남을 식량이 생산되고 있다고 한다.", "According to the book, the Earth as a whole is currently producing food that 12 billion people, more than the world’s population, could eat and still have left over."),
    ("그런데도 세계 인구의 칠 분의 일인 팔억 오천만 명 이상이 만성적이고 심각한 영양실조에 시달리고 있다.", "Even so, more than 850 million people, one seventh of the world’s population, are suffering from chronic and serious malnutrition."),
    ("지글러는 이런 불합리한 현실의 원인이 사회구조적 문제에 있음을 조목조목 따져 보여준다.", "Ziegler shows, item by item, by examining it closely, that the cause of this irrational reality lies in social-structural problems."),
    ("산림파괴로 인한 사막화 등 환경파괴, 전쟁과 정치적 무질서, 신자유주의로 인한 불공정한 분배의 가속화 등이 이런 결과를 초래하는 문제들이다.", "Environmental destruction such as desertification caused by deforestation, war and political disorder, and the acceleration of unfair distribution caused by neoliberalism are the problems that bring about this result."),
    ("최근 국내에서도 결식아동이 늘어나고 있는 뉴스를 보면서 비만을 걱정하는 아이들이 있는 한편에서 허기진 배를 움켜쥔 아이가 공존하는 기막힌 현실이 다른 세상의 일만은 아니라는 생각이 든다.", "Watching the news that the number of children skipping meals is increasing in Korea too recently, I come to think that the absurd reality in which children worried about obesity and children clutching their hungry stomachs coexist is not only something of another world."),
]
_SPEAK14 = [("캘리포니아에서 발생하는 산불에 대해서 이야기해 보세요.", "Talk about the wildfires that occur in California."), ("왜 발생합니까? 어떤 피해가 있습니까?", "Why do they occur? What damage is there?"), ("다른 나라나 자기 나라에서 큰 자연재해로 피해를 입은 사람들을 어떻게 도울 수 있는지 서로 이야기해 보세요.", "Talk to each other about how you can help people who suffered damage from a big natural disaster in another country or your own country.")]
L6 = lesson(
    "U15 L5 · Part 3 (심화 학습): 왜 세계의 절반은 굶주리는가?",
    "심화 학습 · 산불 · 굶주림 · 영양실조 · 사막화 · 결식아동 · 왜 세계의 절반은 굶주리는가 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3 (Reading): a newspaper article, “왜 세계의 절반은 굶주리는가?” (Why is half of the world hungry?)",
             "The following is a text from a newspaper (Kyunghyang). The text is the book’s with the numbers spelled out (120억 명 is 백이십억 명; 7분의 1 is 칠 분의 일; 8억5000만 명 is 팔억 오천만 명); the book’s title mark < > around the title of Jean Ziegler’s book is dropped and the title is written in plain Hangul (the book’s own title ends with a question mark). The English is mine.",
             examples=passage(_HUN)),
        card("학습활동 3: the questions answered (mine)",
             "1. The article is best described as C, a book review (the writer reflects on how reading Jean Ziegler’s book changed his thinking; it is not a travel journal or a scientific analysis, and it is more a reflective review of a book than a plain editorial).\n\n"
             "2. The problem in the African country: many people are struggling with starvation (hunger). The causes: drought and civil war.\n\n"
             "3. The causes elaborated in the third paragraph: environmental destruction such as desertification caused by deforestation; war and political disorder; and the acceleration of unfair distribution caused by neoliberalism.\n\n"
             "4. The two ironic phenomena: globally, enough food is produced to feed 12 billion people, more than the world’s population, yet more than 850 million people (one seventh) suffer from chronic malnutrition; in Korea, children worried about obesity coexist with children who skip meals and clutch their hungry stomachs."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK14)),
        card("Activities left out",
             "학습활동 1 (a YTN video about wildfires in Korea, with questions in English: five statistics, such as “93% of wildfires occur in March and April,” the two main causes, and a table of the three research areas — prevention, extinguishing and recovery), 학습활동 2 (a public awareness poster about wildfires caused by humans by KOBACO, whose text is inside the picture; you translate it and make your own poster) and 학습활동 4 (a listening activity from the Seoul Education Research & Information Institute about African farmers’ problem, the speaker’s question to the farmer, a comparison of two African villages and the speaker’s message) are audio, video, picture and drawing activities."),
    ],
    exercises=uniq(
        _tr(_HUN, k=3) + _tr(_SPEAK14, k=2)
        + [M("What best describes the article?", "A book review", ["A travel journal", "A scientific analysis", "A weather report"], "Reflection on Ziegler’s book."), M("What are the problem and the causes in the African country?", "Starvation, caused by drought and civil war", ["Flooding, caused by rain", "Obesity, caused by wealth", "Fire, caused by lightning"], "가뭄과 내전."), M("Who is Jean Ziegler?", "The U.N. special rapporteur on food", ["A Korean reporter", "A farmer", "A weather forecaster"], "유엔 식량 특별조사관."), M("How many people could the food produced on Earth feed?", "12 billion", ["850 million", "7 billion", "1 billion"], "백이십억 명."), M("How many people suffer from chronic malnutrition?", "More than 850 million", ["12 billion", "120 million", "7 million"], "팔억 오천만 명 이상."), M("What fraction of the world’s population is that?", "One seventh", ["One half", "One tenth", "One third"], "칠 분의 일."), M("Which is NOT a cause listed by Ziegler?", "Too much rain", ["Deforestation and desertification", "War and political disorder", "Unfair distribution caused by neoliberalism"], "The listed causes."), M("What irony does the writer mention in Korea?", "Children worried about obesity and children who skip meals coexist", ["Rich children are hungry", "Farmers have no rice", "Schools have no food"], "공존하는 기막힌 현실."),
           F("가뭄과 내전으로 많은 사람들이 기아에 ___. (are struggling)", "허덕인다", ["넘친다", "속출한다"], "허덕이다."), F("이는 어쩔 수 없는 일이라고 ___ 적이 있다. (regarded)", "여긴", ["따진", "접한"], "여기다."), F("세계 인구의 칠 분의 일이 만성적 ___에 시달리고 있다. (malnutrition)", "영양실조", ["사막화", "신자유주의"], "영양실조."), F("지글러는 이런 불합리한 현실의 원인을 ___ 따져 보여준다. (item by item)", "조목조목", ["무심코", "삼삼오오"], "조목조목."), F("신자유주의로 인한 불공정한 ___의 가속화가 문제다. (distribution)", "분배", ["의식", "허기"], "분배."), F("허기진 배를 ___ 아이가 공존한다. (clutching)", "움켜쥔", ["넘치는", "앙상한"], "움켜쥐다."),
           read_q("세계 인구의 칠 분의 일이 영양실조에 시달리고 있습니다"), read_q("전쟁과 정치적 무질서가 문제를 초래합니다"), read_q("결식아동이 늘어나고 있습니다"), read_q("산림파괴로 사막화가 진행되고 있습니다"), read_q("캘리포니아에서 발생하는 산불에 대해서 이야기해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("가물다", "to be drought stricken", "벌써 두 달째 비가 오지 않고 가물어서 농작물의 피해가 커지고 있다.", "가뭄"),
        ("다발", "(多發) frequent occurrences", "이곳은 사고 다발지역입니다. 조심하세요."),
        ("돌이킬 수 없다", "to be irrevocable; to be irreversible", "이제 사태가 돌이킬 수 없게 되었어요."),
        ("동시다발", "(同時多發) occurring in many places at the same time; being rampant; “simultaneous time multiple occurrences”", "유럽 지역에서 테러 사건이 동시다발로 발생하고 있어요."),
        ("상상(하다)", "(想像) imagination (to imagine)", "과거에 우리가 상상하던 미래가 현실이 되었어요."),
        ("소화", "(消火) extinguishing (fire)", "난로 옆에는 꼭 소화기를 준비해 두어야 합니다.", "소화 (消化) digestion"),
        ("숲", "a forest; a grove", "숲 속에서 길을 잃지 않도록 지도를 꼭 준비해 가세요.", "수풀, 산림"),
        ("실시간", "(實時間) real time", "축구 중계를 실시간으로 방송해 준다고 합니다."),
        ("앗아가다", "to rid of; to deprive", "중국에서 발생한 지진은 수많은 생명을 앗아갔습니다."),
        ("요인", "(要因) a (main) cause; a factor", "지금부터 실패 요인을 분석해 봅시다.", "요인 (要人) an important person"),
        ("우거지다", "to be heavily wooded; to be lush", "마당에 잡초가 우거졌어요. 잡초를 좀 뽑읍시다.", "울창하다"),
        ("울창하다", "(鬱蒼) to be heavily wooded; to be lush", "숲에 나무가 울창하게 자랐습니다.", "우거지다"),
        ("인위적", "(人爲的) artificial; man-made", "요즘은 유전자를 인위적으로 조작해 농산물을 만들기도 합니다.", "자연적"),
        ("자연발화", "(自然發火) natural combustion; “natural outbreak of fire”", "그 화재의 원인은 자연발화입니다.", "방화 (放火)"),
        ("저감(하다/시키다/되다)", "(低減) reduction; lowering (to reduce; to lower/to be reduced; to be lowered)", "정부는 탄소 배출량을 저감시키기 위해 노력하고 있습니다."),
        ("토양", "(土壤) soil; the upper layer of earth in which plants grow", "비료 사용이 증가하면서 토양 오염도 늘고 있습니다.", "흙"),
        ("풍속", "(風速) velocity; wind speed", "최대 풍속이 초속 이십오까지 되면서 강풍 주의보가 발효되었습니다."),
        ("풍향", "(風向) wind direction", "오늘 아침 한강 풍향은 동풍이었습니다."),
        ("확산(시키다/하다/되다)", "(擴散) spreading; proliferation (to spread; to proliferate/to be spread; to be proliferated)", "핵무기 확산을 막기 위해 두 나라가 조약에 합의했습니다."),
    ]),
    ("학습활동 2", [
        ("간접흡연", "(間接吸煙) secondhand smoke; to breathe secondhand smoke", "간접흡연도 건강에 매우 해롭습니다."),
        ("무심코", "(無心) inadvertently; unknowingly; mindlessly; “(with) no heart”", "무심코 창 밖을 보았더니 눈이 내리고 있었습니다."),
    ]),
    ("학습활동 3", [
        ("가속화", "(加速化) acceleration", "의학기술의 발달로 고령화가 가속화되고 있습니다."),
        ("결식", "(缺食) skipping meals (because of poverty)", "", "단식, 금식, 결식 아동"),
        ("공감(하다)", "(共感) sympathy (to sympathize)", "그 사람의 의견에 공감할 수 없어요."),
        ("공존(하다)", "(共存) coexistence (to coexist)", "개발과 환경 보호가 공존할 수 있을까요?"),
        ("과잉", "(過剩) excess", "공급 과잉으로 농산물 가격이 하락했어요."),
        ("기막히다", "(氣) to be absurd; to be unbelievable; to be ridiculous", "운전자의 작은 실수로 기막힌 대형 사고가 발생했다."),
        ("따지다", "to inquire or look into (in order to find an answer or distinguish right or wrong)", "아무리 따져 보아도 원인을 알 수 없었다. 이 문제를 따져보면 누가 맞는지 알 수 있다."),
        ("무질서(하다)", "(無秩序) absence of order; disorder; chaos (to be disordered; to be chaotic)", "거리에 건물이 무질서하게 서 있어서 보기 안 좋아요."),
        ("분배(하다/되다)", "(分配) distribution (to distribute/to be distributed)", "부를 고르게 분배하기 위해 제도를 개혁하기로 했어요."),
        ("불공정", "(不公正) unfairness", "김 씨는 불공정 거래로 검찰에 적발되었습니다.", "공정"),
        ("불합리(하다)", "(不合理) irrationality; absurdity (to be irrational; to be absurd)", "불합리한 제도를 개혁합시다.", "합리"),
        ("사막화", "(沙漠化) desertification", "몽고에서 사막화가 빠르게 진행되고 있습니다."),
        ("산림파괴", "(山林破壞) deforestation; “destruction of forest”", "사막화로 인해 산림파괴가 심각합니다."),
        ("신자유주의", "(新自由主義) neoliberalism", ""),
        ("앙상하다", "to be bony; to be skinny", "환자가 살이 다 빠져서 뼈만 앙상합니다."),
        ("영양실조", "(營養失調) malnutrition; unbalanced nutrition; dystrophy", "북한 어린이들의 영양실조가 심각한 수준입니다."),
        ("움켜쥐다", "to grab; to grasp", "아이가 아파하면서 갑자기 배를 움켜쥐고 쓰러졌어요."),
        ("의식", "(意識) consciousness", "아이가 의식을 잃고 쓰러졌어요."),
        ("접하다", "(接) to learn about; to hear; to encounter; to come into contact; to border; to adjoin", "어머니는 사고 소식을 접하고 충격을 받으셨습니다."),
        ("조목조목", "(條目條目) item by item; article by article; in detail", "정부가 발표한 정책의 문제점을 조목조목 짚어 봅시다."),
        ("초래(하다/시키다/되다)", "(招來) causation (to cause/to be caused)", "미국에서 시작된 경제 위기는 전 세계 금융시장의 혼란을 초래했습니다."),
        ("허기(지다)", "(虛飢) hunger; starvation (to be hungry; to be starving)", "너무 허기져서 숨도 안 쉬고 밥을 먹었어요."),
        ("허덕이다", "to struggle; to suffer", "요즘 재정난에 허덕이는 중소기업들이 급증하고 있습니다."),
    ]),
    ("학습활동 4", [
        ("굶주림", "starvation", "아프리카에서는 굶주림에 시달리는 아이들이 많습니다."),
        ("기금", "(基金) a fund", "경제를 살리기 위해 기금을 조성하기로 했습니다."),
        ("배분", "(配分) distribution", "일을 공정하게 배분해서 합시다."),
        ("생애", "(生涯) (one’s entire) life", "아브라함 링컨의 생애를 통해 많은 교훈을 얻었다."),
        ("속출(하다)", "(續出) frequent occurrences; “continuous coming out” (to recur)", "이 지역에서 사고가 속출하고 있습니다."),
        ("수확(하다)", "(收穫) a harvest (to harvest)", "검찰의 수사가 계속되고 있지만 아무런 수확도 얻지 못했습니다."),
        ("싹이 트다", "to bud; “a bud breaks”", "물을 열심히 줬더니 싹이 텄어요."),
        ("씨앗", "a seed", "봄이 됐으니 씨앗을 심읍시다.", "씨"),
        ("유무", "(有無) whether or not (as a noun); “existence or nonexistence”", "김 일병의 출석 유무를 확인해 주세요. 이 문제는 사실 유무를 따져 보아야 합니다.", "여부"),
        ("재난구호", "(災難救護) a rescue activity for disaster victims", "재난구호 활동에 참여할 계획입니다."),
        ("주저하다", "to hesitate", "궁금한 점이 있으시면 주저하지 마시고 연락 주세요."),
        ("직면(하다)", "(直面) facing; “direct facing” (to face)", "우리는 지금 위기에 직면해 있습니다.", "부딪히다"),
        ("파종(하다)", "(播種) sowing (to sow)", "감자 씨를 파종할 때가 되었습니다.", "씨를 뿌리다"),
        ("한정(하다/되다)", "(限定) limitation (to limit/to be limited)", "이 문제는 한국사람에게만 한정된 문제가 아닙니다."),
        ("힘겨워하다", "to feel burdensome", "어제 숙제가 많아서 학생들이 너무 힘겨워했습니다."),
    ]),
]
L7 = lesson(
    "U15 L5 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 가물다 · 동시다발 · 요인 · 울창하다 · 인위적 · 토양 · 풍속 · 확산 · 공존 · 사막화 · 영양실조 · 허덕이다 · 굶주림 · 직면 · 파종",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples have a few typing slips that are corrected here: 정부는 탄소 배출량은 저감시키기 위해 → 배출량을; 아이가 의식을 읽고 → 의식을 잃고. The digits and letters are spelled in Hangul (초속 25 → 초속 이십오). The book lists a few forms with a semicolon, such as 저감(하다; 시키다/되다); they are written with a slash here.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=14)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 5: Natural Disasters (자연재해)", [L1, L2, L3, L4, L5, L6, L7])

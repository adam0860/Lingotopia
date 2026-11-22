"""Unit 64: KBC Semester III, Unit 15, Lesson 9 - North Korea II (북한 II).
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
_W9 = [("탈북", "escaping from North Korea"), ("이질감", "a sense of difference; alienation"), ("난민", "a refugee"), ("주재", "residing; stationing"), ("망명", "asylum; exile"), ("추방", "deportation; banishment"), ("요원", "an agent; staff"), ("인민군", "the North Korean People’s Army; North Korean soldiers"), ("식량", "food; provisions"), ("영양실조", "lack of nutrition; malnutrition"), ("비정부 기구", "NGO (nongovernmental organization)")]
_P9 = [("사기가 저하되다", "to be down; to go down"), ("부대에서 이탈하다", "to break away; to desert"), ("고속도로에 진입하다", "to enter"), ("식량을 원조하다", "to support; to help"), ("탈북자를 취재하다", "to cover a case; to gather news"), ("북한을 탈출하다", "to escape; to flee"), ("미국에 정착하다", "to settle down")]
_HJ9 = [("脫 탈", "take off; remove", "탈수, 탈의실"), ("取 취", "obtain; get; collect", "취재, 취득"), ("進 진", "proceed; advance", "진행, 추진"), ("追 추", "chase; go after", "추방, 추돌"), ("難 난", "difficulty; hardship", "재난, 피난")]
_HJW9 = [("탈수", "dehydration"), ("탈의실", "a fitting room; “clothes-removing room”"), ("취재", "collection of data; news gathering"), ("취득", "an acquisition; a gain"), ("진행", "progress"), ("추진", "propel; push"), ("추방", "a deportation; “chase and block”"), ("추돌", "a rear collision; “go after and hit”"), ("재난", "a disaster; a calamity"), ("피난", "fleeing from disaster")]
_REL9 = [("이탈", "탈선", "breaking away: derailment"), ("진척", "진행", "headway: progress"), ("갈취", "탈취", "extortion: seizure"), ("재난", "재앙", "a calamity: a disaster")]
_BOX9 = [("나아갈 길, 방향, 목표", "진로", "the way forward, direction, goal: a course (of life)"), ("취임식, 당선, 임기", "대통령", "an inauguration, an election win, a term of office: a president"), ("탈주, 탈옥, 탈영", "탈출", "flight, prison break, desertion: escape")]
_L9X = [("탈선", "derailment; going astray"), ("진척", "headway; progress"), ("선진", "being advanced"), ("전진", "moving forward"), ("갈취", "extortion"), ("탈취", "seizure; stealing"), ("섭취", "intake"), ("채취", "gathering; collecting"), ("화재", "a fire"), ("재앙", "a disaster"), ("나아갈 길", "the way forward"), ("방향", "direction"), ("목표", "a goal"), ("진로", "a course; a career path"), ("취임식", "an inauguration ceremony"), ("당선", "winning an election"), ("임기", "a term of office"), ("탈주", "running away"), ("탈옥", "a prison break"), ("탈영", "desertion"), ("탈세", "tax evasion"), ("탈출", "escape"), ("사기", "morale"), ("저하되다", "to go down"), ("부대", "a military unit"), ("이탈하다", "to break away"), ("고속도로", "an expressway"), ("진입하다", "to enter"), ("취재하다", "to cover (a story)"), ("정착하다", "to settle down"), ("탈출하다", "to escape")]
L1 = lesson(
    "U15 L9 · Review: defector words and Sino-Korean 脫 取 進 追 難",
    "북한 II · 단어 복습 · 한자어 복습 · 탈북 · 난민 · 망명 · 추방 · 영양실조 · 脫 取 進 追 難",
    requires=[],
    cards=[
        card("단어 복습 1: the meanings (the book’s matching)", "The book asks you to match each word on the left with its meaning on the right (the first, 탈북, is done for you). The pairs:", tables=[ktable(_W9)]),
        card("단어 복습 2: the underlined word and its meaning (my pairs)", "The book asks you to connect each phrase, whose last word is underlined, with the meaning of the underlined word on the right. My pairs:", tables=[table(["Phrase", "Meaning of the verb"], [list(r) for r in _P9], say=[0])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ9], say=[2]), ktable(_HJW9)]),
        card("한자어 복습 1: the most closely related word (my answers)", "Circle the word most closely related to the word on the left (A. 이탈: 최대, 탈선, 최저; B. 진척: 진행, 선진, 전진; C. 갈취: 탈취, 섭취, 채취; D. 재난: 화재, 재앙, 현재).", tables=[table(["Word", "Related word (my answer)", "Meaning"], [[a, b, c] for a, b, c in _REL9], say=[0, 1])]),
        card("한자어 복습 2: the word that fits the three words (my answers)", "Choose from the box (대통령, 진로, 원조, 탈출, 탈세) the word most closely related to the three words on each line:", tables=[table(["The three words", "The word from the box (my answer)", "Meaning"], [[a, b, c] for a, b, c in _BOX9], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L9X)]),
    ],
    exercises=uniq(
        _tr(_W9, k=3) + _tr(_HJW9, k=3) + _tr(_L9X, k=3) + _tr(_P9, k=3)
        + [M("What does the syllable 脫 (탈) mean?", "take off; remove", ["obtain", "advance", "chase"], "탈수."), M("What does the syllable 取 (취) mean?", "obtain; get; collect", ["take off", "advance", "chase"], "취재."), M("What does the syllable 進 (진) mean?", "proceed; advance", ["take off", "obtain", "chase"], "진행."), M("What does the syllable 追 (추) mean?", "chase; go after", ["take off", "obtain", "advance"], "추방."), M("What does the syllable 難 (난) mean?", "difficulty; hardship", ["take off", "obtain", "advance"], "재난."),
           M("Which word is related to 이탈?", "탈선", ["최대", "최저", "취재"], "Derailment."), M("Which word is related to 진척?", "진행", ["선진", "전진", "진입"], "Progress."), M("Which word is related to 갈취?", "탈취", ["섭취", "채취", "취득"], "Seizure."), M("Which word is related to 재난?", "재앙", ["화재", "현재", "피난"], "A disaster."), M("Which word fits 나아갈 길, 방향, 목표?", "진로", ["대통령", "원조", "탈세"], "A course."), M("Which word fits 취임식, 당선, 임기?", "대통령", ["진로", "원조", "탈출"], "A president."), M("Which word fits 탈주, 탈옥, 탈영?", "탈출", ["대통령", "진로", "탈세"], "Escape."),
           F("그는 북한을 ___해 한국에 왔습니다. (escaped)", "탈출", ["추방", "진입"], "탈출하다."), F("그 기자는 ___자를 취재했습니다. (a defector)", "탈북", ["이탈", "추돌"], "탈북자."), F("정부가 식량을 ___했습니다. (aided)", "원조", ["추방", "정착"], "원조하다."), F("그는 미국에 ___했습니다. (settled)", "정착", ["진입", "탈선"], "정착하다."), F("범인이 나라에서 ___되었습니다. (was deported)", "추방", ["정착", "취재"], "추방되다."),
           read_q("그는 북한을 탈출해 한국에 왔습니다"), read_q("탈북자를 취재했습니다"), read_q("식량을 원조했습니다"), read_q("미국에 정착했습니다"), read_q("난민으로 인정받았습니다")]
    ),
)

# ================================================================== L2 Part 1
_PARK = [("한나라당 박근혜 대표가 이십육 일 북한 인권문제를 다룬 뮤지컬 요덕 스토리를 관람하기 위해 양재동 교육문화회관을 방문, 공연에 앞서 출연진과 인사하고 있다.", "On the 26th, Park Geun-hye, the leader of the Grand National Party, visited the Yangjae-dong Education and Culture Center to watch the musical “Yoduk Story,” which deals with North Korea’s human rights issue, and is greeting the cast before the performance."), ("김영삼 전대통령과 황장엽 씨도 이날 박 대표에 앞서 뮤지컬을 관람했다.", "Former President Kim Young-sam and Mr. Hwang Jang-yop also watched the musical on this day before Representative Park."), ("김문석기자.", "Reporter Kim Mun-seok.")]
_MUS = [
    ("요덕수용소는 북한 정치범수용소이자 인권유린의 현장으로 악명 높다.", "The Yoduk camp is notorious as a North Korean political prison camp and a scene of human rights abuses."),
    ("북한의 인권탄압은 탈북자인 기자 강철환의 체험수기인 수용소의 노래로 국내에 알려진 바 있다.", "North Korea’s suppression of human rights has been made known in Korea through “Song of the Camp,” the memoir of the defector and reporter Kang Chol-hwan."),
    ("이번 작품의 제작과 연출을 맡은 정성산 감독은 탈북해 온 영화감독으로 자신의 경험을 바탕으로 요덕수용소 이야기를 뮤지컬로 제작했다.", "Director Jeong Seong-san, who took charge of the production and direction of this work, is a film director who defected from the North, and he made the story of the Yoduk camp into a musical based on his own experience."),
    ("북한 정치범 수용소 출신 탈북 예술인이 출연하며 국내 최초로 북한 최고 예술 춤인 사계절 춤을 만날 수 있다.", "Defector artists from North Korean political prison camps appear, and for the first time in Korea one can see the four-seasons dance, the highest art dance of North Korea."),
    ("강련화라는 여성을 주인공으로 그녀와 그녀의 평화로운 가정에 닥치는 파란만장한 삶과 죽음의 이야기가 담긴다.", "With a woman named Kang Ryeon-hwa as the main character, it contains the story of the eventful life and death that befall her and her peaceful family."),
]
_SOL = [
    ("대북인권단체 북한자유연합의 수전 솔티 대표가 북한의 인권개선을 위해 헌신한 공로를 인정받아 월터 저드 자유상을 받게 됐다고 미국의 소리 (브이오에이) 방송이 십삼 일 전했다.", "The Voice of America (VOA) broadcast reported on the 13th that Susan Scholte, the head of the North Korea Freedom Coalition, a human rights group for North Korea, will receive the “Walter Judd Freedom Award” in recognition of her contribution in devoting herself to improving North Korea’s human rights."),
    ("브이오에이에 따르면 이 상을 수여하는 미국의 비정부기구 미국학기금은 솔티 대표가 북한 인권의 숨은 천사로서 북한 인권의 참상을 미국사회에 알렸고 탈북자들이 북한의 자유와 인권을 위해 일하도록 지원했다고 수상자 선정 이유를 밝혔다.", "According to VOA, the American NGO that presents this award, The Fund for American Studies, stated as the reason for selecting the recipient that Representative Scholte, as the “hidden angel” of North Korean human rights, informed American society of the horrors of North Korea’s human rights situation and supported defectors in working for freedom and human rights in North Korea."),
    ("천구백구십삼 년 제정된 월터 저드 자유상은 폭정과 억압을 폭로하고 자유를 확산시키고자 노력한 개인에게 주어지며, 앞서 로널드 레이건 전 미국 대통령과 프랭크 울프 미 하원의원 등이 이 상을 받았다.", "The Walter Judd Freedom Award, established in 1993, is given to individuals who worked to expose tyranny and oppression and spread freedom, and earlier recipients include former American President Ronald Reagan and U.S. Representative Frank Wolf."),
    ("솔티 대표는 탈북자 강제송환 반대 운동을 시작한 천구백구십육 년 이후 북한의 인권 개선을 위해 노력해 왔으며 이천팔 년에는 제구회 서울평화상을 받기도 했다.", "Representative Scholte has worked to improve North Korea’s human rights since 1996, when she began the campaign against the forced repatriation of defectors, and in 2008 she also received the 9th Seoul Peace Prize."),
]
_SPEAK24 = [("북한의 인권 상황에 대해 아는 것이 있으면 말해 보세요.", "If you know anything about the human rights situation in North Korea, tell about it.")]
L2 = lesson(
    "U15 L9 · Part 1 (도입 학습): Hwang Jang-yop, a musical on the Yoduk camp, a human rights award",
    "도입 학습 · 황장엽 · 요덕 스토리 · 요덕수용소 · 정치범 · 월터 저드 자유상 · 수전 솔티 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 황장엽 (Hwang Jang-yop) — the book’s note",
             "Hwang Jang-yop (17 February 1923–10 October 2010) was a major politician in North Korea who defected to South Korea in 1997, making him the highest-ranking defector to date. He was largely responsible for crafting the Juche Idea (주체사상), North Korea’s official state ideology. Hwang was found dead in his home on the morning of 10 October 2010. Initial reports stated that he died of a heart attack. For more information, go to Hwang Jang-yop."),
        card("학습활동 1 (Reading · Speaking): a photo caption",
             "The book asks you to look at the photo and its caption and to summarize in English what the photo is about (Text and image © Kyunghyang). The caption is the book’s with 26일 spelled out (이십육 일). The English is mine.",
             examples=passage(_PARK)),
        card("학습활동 1: my summary", "The photo shows Park Geun-hye, the leader of the Grand National Party, greeting the cast of the musical “Yoduk Story” (about North Korea’s human rights issue) at the Yangjae-dong Education and Culture Center before the performance; former President Kim Young-sam and Hwang Jang-yop had watched the musical before her that day."),
        card("학습활동 2 (Reading): the performance guide of the musical “Yoduk Story”",
             "The book gives a “This week’s performance” poster (Text and image © Kyunghyang) with these details: Date and time: March 13 to April 2, 2006 (2006년 3월 13일부터 4월 2일까지); Place: the Grand Theater of the Seoul Education and Culture Center; Admission: VIP seats 80,000 won / R seats 60,000 won / S seats 40,000 won / A seats 20,000 won; Inquiries: 02-526-9682~3. The paragraph of the guide (the English is mine):",
             examples=passage(_MUS)),
        card("학습활동 2: the questions answered (mine)",
             "1. 요덕수용소 is a North Korean political prison camp, notorious as a scene of human rights abuses.\n\n"
             "2. The musical: Director and cast: the producer and director is Jeong Seong-san, a film director who defected from North Korea; the cast includes defector artists who came from North Korean political prison camps (and the show presents the four-seasons dance). Main storyline: a woman named Kang Ryeon-hwa and the eventful story of life and death that befalls her and her peaceful family."),
        card("학습활동 3 (Reading · Speaking): the Walter Judd Freedom Award",
             "The following is an article about the Walter Judd Award (© Yonhapnews), titled 수전 솔티, “월터 저드 자유상” 수상 (VOA). The text is the book’s with the numbers and abbreviations spelled out (VOA is 브이오에이; 13일 is 십삼 일; 1993년 is 천구백구십삼 년; 1996년 is 천구백구십육 년; 2008년 is 이천팔 년; 제9회 is 제구회); the English name “The Fund for American Studies” in parentheses is dropped from the spoken line, and the quotation marks ‘ ’ are removed. The English is mine.",
             examples=passage(_SOL)),
        card("학습활동 3: the questions answered (mine)",
             "1A. Susan Scholte is the head of the North Korea Freedom Coalition (북한자유연합), a human rights group for North Korea, who devoted herself to improving North Korea’s human rights and was recognized with the Walter Judd Freedom Award; she has campaigned against the forced repatriation of defectors since 1996 and received the 9th Seoul Peace Prize in 2008.\n\n"
             "1B. The earlier recipients named are former U.S. President Ronald Reagan and U.S. Representative Frank Wolf. What they have in common: both are American politicians, and the award goes to individuals who worked to expose tyranny and oppression and to spread freedom.\n\n"
             "2. In the pair activity, taking turns as the Master of Ceremonies, you introduce 수잔 솔티 to each other in Korean."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK24)),
        card("Activities left out", "학습활동 4 (a YTN report on defectors: what happened to the defectors in Myanmar and in Thailand, and what the numbers 19, 16 and 3 weeks indicate) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_PARK[:2], k=1) + _tr(_MUS, k=3) + _tr(_SOL, k=3)
        + [M("Who is Hwang Jang-yop?", "A North Korean politician who defected to South Korea in 1997", ["A South Korean president", "A film director", "A journalist"], "The book’s note."), M("What did Hwang Jang-yop help craft?", "The Juche Idea (주체사상)", ["The Sunshine Policy", "A constitution", "A musical"], "The book’s note."), M("What is 요덕수용소?", "A North Korean political prison camp", ["A school", "A theater", "A hospital"], "정치범수용소."), M("Who directed the musical?", "Jeong Seong-san, a film director who defected", ["Kim Young-sam", "Kang Chol-hwan", "Park Geun-hye"], "정성산 감독."), M("Who is the main character of the musical?", "A woman named Kang Ryeon-hwa", ["Kang Chol-hwan", "Susan Scholte", "Hwang Jang-yop"], "강련화."), M("Whose memoir made North Korea’s human rights suppression known in Korea?", "Kang Chol-hwan’s", ["Hwang Jang-yop’s", "Park Geun-hye’s", "Ronald Reagan’s"], "수용소의 노래."), M("Who is Susan Scholte?", "The head of a human rights group for North Korea", ["A film director", "A North Korean soldier", "A U.S. president"], "북한자유연합 대표."), M("What award did she receive?", "The Walter Judd Freedom Award", ["The Nobel Prize", "The Peace Prize of Seoul only", "The Fund Award"], "월터 저드 자유상."), M("Who are earlier recipients of the award?", "Ronald Reagan and Frank Wolf", ["Kim Dae-jung and Roh Moo-hyun", "Kang Chol-hwan", "Hwang Jang-yop"], "레이건과 울프."), M("What did she start in 1996?", "A campaign against the forced repatriation of defectors", ["A musical", "A company", "A school"], "탈북자 강제송환 반대 운동."),
           F("요덕수용소는 인권유린의 현장으로 ___ 높다. (notorious)", "악명", ["명예", "인기"], "악명이 높다."), F("솔티 대표는 북한 인권개선을 위해 ___한 공로를 인정받았다. (devoted herself)", "헌신", ["억류", "인용"], "헌신하다."), F("이 상은 폭정과 ___을 폭로한 개인에게 주어진다. (oppression)", "억압", ["수여", "송환"], "억압."), F("정 감독은 뮤지컬의 제작과 ___을 맡았다. (direction)", "연출", ["출연", "탄압"], "연출."), F("탈북자 강제___ 반대 운동을 시작했다. (repatriation)", "송환", ["억압", "인용"], "강제송환."),
           read_q("요덕수용소는 북한 정치범수용소입니다"), read_q("수전 솔티 대표가 월터 저드 자유상을 받았습니다"), read_q("북한의 인권 상황에 대해 아는 것이 있으면 말해 보세요"), read_q("뮤지컬 요덕 스토리를 관람했습니다"), read_q("탈북 예술인이 출연합니다")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("~진", "(陣) a staff; a delegation; a team", "출연진, 의료진, 교수진"),
        ("출연(하다)", "(出演) appearance (on TV, radio, movie, etc.) (to appear; to make an appearance)", "그 영화에는 잘 알려지지 않은 배우들이 많이 출연한다.", "나오다"),
    ]),
    ("학습활동 2", [
        ("수용소", "(收容所) a concentration camp; a detention camp", "포로수용소, 강제수용소, 난민수용소, 정치범수용소"),
        ("악명(이) 높다", "(惡名) to be notorious; to be infamous", "그 수용소는 환경이 열악하기로 악명이 높습니다.", "유명하다"),
        ("연출(하다)", "(演出) directing (a movie, a musical, a show, etc.); (to direct [a movie, a musical, etc.])", "이 영화를 연출한 감독은 러시아 사람이다.", "감독(하다)"),
        ("유린(하다/되다)", "(蹂躪) infringement (to infringe on; to trample/to be infringed on)", "군사독재시절에는 인권이 많이 유린되었습니다.", "인권유린"),
        ("정치범", "(政治犯) a political prisoner", "새 정부가 들어서면서 많은 정치범들이 사면되었습니다."),
        ("탄압(하다)", "(彈壓) suppression; repression (to suppress; to repress)", "인권을 탄압하다.", "억압하다"),
        ("파란만장하다", "(波瀾萬丈) to be full of ups and downs", "할아버지는 한국전쟁을 겪는 등 파란만장한 삶을 사셨다."),
    ]),
    ("학습활동 3", [
        ("강제", "(强制) compulsion; coercion", "경찰은 시위대를 강제 해산시켰어요."),
        ("송환(하다/되다)", "(送還) repatriation (to repatriate/to be repatriated)", "중국 정부는 탈북자들을 북한으로 송환시키고 있습니다."),
        ("수여(하다/되다)", "(授與) presentation; conferment (to present; to award; to confer/to be presented)", "우승자에게는 오천만 원의 상금이 수여됩니다."),
        ("억압(하다)", "(抑壓) suppression; oppression (to suppress)", "중국은 정치적 자유를 억압하고 있습니다.", "탄압"),
        ("참상", "(慘狀) horrors; a terrible scene; atrocity", "이번 사진전시회는 전쟁의 참상을 잘 보여준다."),
        ("천사", "(天使) an angel; “heavenly envoy”", "그 사람은 아주 착해서 정말 천사 같아요."),
        ("폭압", "(暴壓) oppression; curbing by force; “violent pressing”", "국민들은 폭압 정치를 견디지 못해 반정부 시위를 벌이고 있습니다."),
        ("폭정", "(暴政) tyranny; despotism; “violent governing”", "국민들은 독재자의 폭정에 시달리고 있습니다."),
        ("헌신(하다)", "(獻身) devotion; dedication (to devote oneself; to dedicate oneself)", "우리 어머니는 항상 가족에게 헌신하십니다."),
    ]),
    ("학습활동 4", [
        ("소원대로", "(所願) as one wishes; according to one’s wish", "저는 아버지의 소원대로 의대에 진학하기로 했어요.", "원하던 대로"),
        ("억류(하다/되다)", "(抑留) detainment (to detain/to be detained)", "여기자 두 명이 간첩 혐의로 북한에 억류되어 있어요.", "구금"),
        ("인용(하다/되다)", "(引用) quotation (to quote/to be quoted)", "그 사람은 이야기를 할 때 유명한 책을 많이 인용합니다."),
    ]),
]
L3 = lesson(
    "U15 L9 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 출연 · 수용소 · 악명 · 연출 · 유린 · 정치범 · 탄압 · 강제 · 송환 · 수여 · 억압 · 참상 · 폭정 · 헌신 · 억류 · 인용",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 수여 (5천만 원) is spelled in Hangul here (오천만 원).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=14, nread=12)),
)

# ================================================================== L4 Part 2 texts
_VOA = [
    ("미국의 북한인권법에 따라 제삼국에서 난민 지위를 부여 받은 백 번째 탈북자가 미국에 입국했다고 미국의 소리 (브이오에이) 방송이 십 일 밝혔다.", "The Voice of America (VOA) broadcast stated on the 10th that the 100th defector to be granted refugee status in a third country under the American North Korean Human Rights Act has entered the United States."),
    ("이 방송은 미 국무부 고위관리의 말을 인용해 “백 번째 탈북 난민이 팔 일 (현지시간) 미국에 도착했다”면서 “이 탈북자는 러시아 벌목공 출신인 조 모 씨로 알려졌다”고 전했다.", "Quoting a senior official of the U.S. State Department, this broadcast reported, “The 100th defector refugee arrived in the United States on the 8th (local time),” and, “This defector is known to be Mr. Cho, who comes from being a logger in Russia.”"),
    ("조 씨는 북한에서 온 다른 벌목공과 함께 지난 삼 월 러시아 블라디보스토크의 한국 영사관에 진입한 뒤 지난달 난민 판정을 받고 모스크바 주재 미국 대사관의 보호를 받아 왔다.", "Mr. Cho, together with another logger from North Korea, entered the South Korean consulate in Vladivostok, Russia, last March, received a refugee determination last month and has been under the protection of the American embassy stationed in Moscow."),
    ("조 씨와 함께 탈출한 다른 벌목공도 조만간 미국으로 갈 것으로 알려졌다.", "The other logger who escaped together with Mr. Cho is also known to be going to the United States soon."),
    ("브이오에이는 “이천육 년 태국에서 탈북자 여섯 명이 처음 미국에 입국한 이후 매년 이십 명에서 삼십 명의 탈북 난민이 태국, 중국, 몽골, 러시아, 필리핀, 라오스 등을 통해 미국에 들어왔다”면서 “이들 탈북 난민은 미국내 십여 개 중소도시로 보내진 뒤 지역 난민단체의 도움을 받아 정착 과정을 밟는데, 적어도 삼 분의 일 정도는 한인들이 많이 거주하는 대도시로 이동한다”고 전했다.", "VOA reported, “Since six defectors first entered the United States from Thailand in 2006, 20 to 30 defector refugees have come to the United States every year through Thailand, China, Mongolia, Russia, the Philippines, Laos and others,” and, “After being sent to about ten small and medium-sized cities in the United States, these defector refugees go through a settlement process with the help of local refugee groups, and at least about one third move to large cities where many Koreans live.”"),
    ("난민 신분으로 미국에 정착한 탈북자들은 일 년 뒤 영주권을 신청할 수 있고, 범죄나 결격 사유가 없으면 영주권 취득 오 년 후 시민권을 신청할 수 있다.", "Defectors who settled in the United States as refugees can apply for permanent residency after one year, and if they have no crime or reason for disqualification, they can apply for citizenship five years after obtaining permanent residency."),
]
_WOM = [
    ("미국이 탈북자들에 대해 난민 수용을 허용했다.", "The United States has allowed the acceptance of defectors as refugees."),
    ("그 첫 번째 케이스로 여섯 명의 탈북자가 미국땅을 밟자 전세계인들은 그들의 입을 통해 탈북 여성들의 인권 유린 실태를 듣게 됐다.", "When six defectors set foot on American soil as the first case, people all over the world came to hear, through their mouths, about the reality of the human rights abuses suffered by defector women."),
    ("인신매매로 인해 성적 노리개로 전락하기 일쑤인 탈북 여성들의 인권 유린 실태를 담았다.", "It contains the reality of the human rights abuses of defector women, who often fall into becoming sexual playthings through human trafficking."),
    ("두리하나선교원 측이 제공한 현지 조선족과의 인터뷰 자료에 따르면 헤이룽장성의 한 시골마을의 경우 열다섯 가구 가운데 열두 가구의 노총각이 탈북 여성을 돈을 주고 사서 살고 있다고 한다.", "According to interview materials with local Korean-Chinese people provided by the Duri Hana Mission, in one rural village in Heilongjiang Province, it is said that unmarried older men in 12 of 15 households are living with defector women whom they bought with money."),
    ("탈북자 이 씨의 이야기처럼 탈북 여성들의 상당수가 중국 현지 인신매매 조직에 의해 농촌 지역의 노총각이나 정신질환자 등 정상적으로 결혼하기 어려운 이들에게 팔려가고 있다.", "As in the story of the defector Ms. Lee, a considerable number of defector women are being sold by local Chinese human-trafficking organizations to unmarried older men in rural areas, the mentally ill and others who find it hard to marry normally."),
    ("심지어 한족의 성적 노리개나 매춘 시장으로 팔려가는 여성도 있을 정도.", "There are even women who are sold as sexual playthings of Han Chinese or into the prostitution market."),
    ("이것이 이천육 년 탈북 여성들의 실상이다.", "This is the real condition of defector women in 2006."),
    ("두리하나선교원을 비롯해 탈북자동지회 등 여러 탈북 관련 단체에서는 이미 몇 년 전부터 이러한 실상을 한국 사회에 알리며 탈북자 지원에 대한 여론 환기에 앞장섰다.", "Several defector-related groups, including the Duri Hana Mission and the Defectors’ Comrades Association, have already for several years informed Korean society of this reality and taken the lead in stirring up public opinion to support defectors."),
    ("하지만 한국 사회가 이런 현실을 민감하게 받아들이지 않았다.", "But Korean society did not take this reality up sensitively."),
    ("그런데 최근 미국으로 망명하는 데 성공한 탈북자들의 사연이 알려지면서 탈북 여성의 실상이 조금씩 드러나기 시작했다.", "However, as the stories of defectors who recently succeeded in seeking asylum in the United States became known, the real condition of defector women began to be revealed little by little."),
]
_SPEAK25 = [("중국이나 다른 나라가 탈북자들을 난민으로 인정해야 한다고 생각합니까?", "Do you think China or other countries should recognize defectors as refugees?"), ("친구와 의견을 나누어 보세요.", "Exchange opinions with a friend."), ("의견에 대한 이유도 설명해 보세요.", "Also explain the reasons for your opinion."), ("미국이 더 많은 탈북자들을 받아들여야 한다고 생각합니까?", "Do you think the United States should accept more defectors?")]
L4 = lesson(
    "U15 L9 · Part 2 (본 학습): the 100th defector refugee and defector women in China",
    "본 학습 · 북한인권법 · 난민 · 벌목공 · 영주권 · 시민권 · 탈북 여성 · 인신매매 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 미국의 북한인권법과 난민 (the U.S. North Korean Human Rights Act and refugees) — the book’s note",
             "The U.S. Senate and House of Representatives passed the 북한인권법 in 2004. At the core of the law is the active involvement of the United States in human right issues of North Korea and the protection of North Korean defectors. By passing this law, the United States acknowledges North Korean defectors as refugees, which allows them to apply for asylum in the United States. Whether or not a country considers a North Korean defector a refugee affects the country’s treatment of the defector. China does not consider North Korean defectors to be refugees, so it sends defectors back to North Korea. Following the example of the United States, Japan established the North Korea Human Rights Law in 2005."),
        card("학습활동 2 (Reading): “난민자격 100번째 탈북자 미국 도착” (the 100th defector with refugee status arrives in the U.S.)",
             "The following is an article about the loggers introduced in 학습활동 1 (© Yonhapnews). The text is the book’s with the numbers and abbreviations spelled out (100번째 is 백 번째; VOA is 브이오에이; 제3국 is 제삼국; 10일 is 십 일; 8일 is 팔 일; 3월 is 삼 월; 2006년 is 이천육 년; 6명 is 여섯 명; 20∼30명 is 이십 명에서 삼십 명; 10여 개 is 십여 개; 3분의 1 is 삼 분의 일; 1년 is 일 년; 5년 is 오 년); the quotation marks are kept as printed. The English is mine.",
             examples=passage(_VOA)),
        card("학습활동 2: the questions answered (mine)",
             "1. Mr. Cho is a former logger from Russia and the 100th defector to receive refugee status under the U.S. North Korean Human Rights Act. He entered the South Korean consulate in Vladivostok last March together with another North Korean logger, received a refugee determination last month, was protected by the American embassy in Moscow, and arrived in the United States on the 8th.\n\n"
             "2. Since 2006, when six defectors first entered from Thailand, 20 to 30 defector refugees have entered the U.S. every year via Thailand, China, Mongolia, Russia, the Philippines and Laos. They are sent to about ten small and medium-sized cities, go through the settlement process with the help of local refugee groups, and at least a third of them move to large cities where many Koreans live.\n\n"
             "3. Yes. Defectors who settled as refugees can apply for permanent residency (a green card) after one year, and, if they have no crime or reason for disqualification, can apply for citizenship five years after getting permanent residency."),
        card("학습활동 4 (Reading): a magazine article on the condition of defector women",
             "The following is part of a magazine article on the condition of defector women (Text and images © Kyunghyang). The text is the book’s with the numbers spelled out (6명 is 여섯 명; 15가구 가운데 12가구 is 열다섯 가구 가운데 열두 가구; 2006년 is 이천육 년); the quotation marks ‘ ’ are removed. The English is mine. (The article deals with human trafficking.)",
             examples=passage(_WOM)),
        card("학습활동 4: the questions answered (mine)",
             "1. According to the first paragraph, the article is about the human rights abuses suffered by North Korean women defectors, which the world came to hear about after the United States allowed defectors to enter as refugees and six of them set foot on American soil.\n\n"
             "2. Many of the women defecting to China are likely to be sold by local Chinese human-trafficking organizations to unmarried older men in rural areas or men with mental illness who find it hard to marry normally, and some are even sold as sexual playthings of Han Chinese or into the prostitution market.\n\n"
             "3. Their fate became known to the outside world through the stories of the first defectors who succeeded in going to the United States as refugees (the groups helping defectors had told Korean society for years, but it had not taken it up sensitively)."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine; each asks you to exchange opinions with a friend and explain the reasons):", examples=passage(_SPEAK25)),
        card("Activities left out", "학습활동 1 (a YTN news report on two North Korean workers: the EEIs, what happened last January, and where they are likely to live) and 학습활동 3 (a YTN report on a demonstration in the United States, with a table of participants, location, reasons, and requests to China and the United States, and a video check) are audio and video activities."),
    ],
    exercises=uniq(
        _tr(_VOA, k=3) + _tr(_WOM, k=3) + _tr(_SPEAK25, k=2)
        + [M("When did the U.S. pass the North Korean Human Rights Act?", "2004", ["1996", "2008", "2010"], "The book’s note."), M("What does the law let defectors do in the U.S.?", "Apply for asylum as refugees", ["Vote immediately", "Join the army", "Avoid all checks"], "The book’s note."), M("How does China treat defectors?", "It does not consider them refugees and sends them back", ["It gives them citizenship", "It accepts them all", "It ignores them"], "The book’s note."), M("Which country followed the U.S. example in 2005?", "Japan", ["China", "Russia", "Thailand"], "The book’s note."),
           M("What number defector refugee arrived in the article?", "The 100th", ["The 10th", "The 1st", "The 50th"], "백 번째."), M("What was Mr. Cho before?", "A logger in Russia", ["A soldier", "A teacher", "A reporter"], "러시아 벌목공."), M("Where did Mr. Cho enter the South Korean consulate?", "Vladivostok", ["Moscow", "Beijing", "Bangkok"], "블라디보스토크."), M("Which embassy protected Mr. Cho?", "The American embassy in Moscow", ["The Korean embassy", "The Chinese embassy", "The German embassy"], "모스크바 주재 미국 대사관."), M("When can refugees apply for permanent residency?", "After one year", ["After ten years", "Immediately", "After five months"], "일 년 뒤."), M("When can they apply for citizenship?", "Five years after getting permanent residency", ["After one month", "After twenty years", "Never"], "영주권 취득 오 년 후."), M("How many defectors first entered the U.S. from Thailand in 2006?", "Six", ["Sixty", "One", "Twenty"], "여섯 명."),
           M("How many of 15 households in the Heilongjiang village had a bachelor with a bought defector woman?", "12", ["15", "2", "5"], "열두 가구."), M("Which kind of group helped inform Korean society?", "Defector-related groups such as the Duri Hana Mission", ["Tourist agencies", "Banks", "Schools"], "두리하나선교원."), M("How did the women’s real condition become known?", "Through the stories of defectors who reached the U.S.", ["Through a movie", "Through a school book", "Through a tax record"], "미국으로 망명한 탈북자들의 사연."),
           F("미국은 탈북자들의 난민 ___을 허용했다. (acceptance)", "수용", ["퇴치", "항의"], "수용."), F("탈북 여성들이 중국 현지 ___ 조직에 팔려간다. (human trafficking)", "인신매매", ["송환", "북송"], "인신매매."), F("탈북 여성의 실상이 조금씩 ___ 시작했다. (be revealed)", "드러나기", ["지키기", "사라지기"], "드러나다."), F("탈북자를 도우려는 ___ 환기에 앞장섰다. (public opinion)", "여론", ["항의", "송환"], "여론 환기."), F("영주권을 받은 지 오 년 후 ___을 신청할 수 있다. (citizenship)", "시민권", ["결격", "난민"], "시민권."),
           read_q("백 번째 탈북 난민이 미국에 도착했습니다"), read_q("난민은 일 년 뒤 영주권을 신청할 수 있습니다"), read_q("탈북 여성의 실상이 조금씩 드러나기 시작했습니다"), read_q("인신매매 조직에 팔려가고 있습니다"), read_q("미국이 더 많은 탈북자들을 받아들여야 한다고 생각합니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("날품팔이", "day labor; a day laborer", "그 사람은 날품팔이 노동자로 힘들게 살고 있어요.", "날품팔이꾼 | 일용직"),
        ("노예", "(奴隸) a slave", "후진국에서는 사람들을 노예처럼 부리는 경우가 많습니다."),
        ("떼다/떼이다", "to deduct/to have ~ deducted", "월급을 받으면 삼 분의 일 이상이 세금으로 떼인다."),
        ("두렵다", "to be afraid of", "저는 우리 아이가 다칠까 봐 항상 걱정됩니다.", "무섭다"),
        ("벌목공", "(伐木工) a logger; a lumberjack", ""),
        ("상납(하다)", "(上納) bribing; offering a bribe; “paying up” (to bribe)", "검찰은 김 모 씨가 정치인들에게 뇌물을 상납한 것으로 보고 조사를 벌이고 있습니다.", "바치다"),
        ("생계를 유지하다", "(生計) to manage living; to get by", "제가 얼마 전에 실직을 해서 생계를 유지하기 어렵습니다."),
        ("선교사", "(宣敎師) a missionary", "그 선교사는 아프리카에 가서 선교활동을 하고 있습니다."),
        ("접하다", "(接) to learn about; to hear; to encounter; to come into contact; to border; to adjoin", "어머니는 사고 소식을 접하고 충격을 받으셨습니다."),
    ]),
    ("학습활동 2", [
        ("허다하다", "(許多) to be innumerable; to be numerous", "청소년들이 게임 중독에 빠져 성적이 떨어지는 경우가 허다하다."),
        ("결격 사유", "(缺格 事由) a reason for disqualification", "특별한 결격 사유가 없어서 이 사람을 채용할까 합니다."),
        ("영주권", "(永住權) the right of permanent residence; permanent residency; a green card", "영주권을 받으려면 어떻게 해야 합니까?", "시민권"),
        ("판정(하다)", "(判定) judgment; decision (to judge; to decide)", "이 제품은 유해한 성분이 들어 있는 것으로 판정되었습니다."),
    ]),
    ("학습활동 3", [
        ("간주(하다/되다)", "(看做) regard (to regard/to be considered)", "경찰은 김 씨를 범인으로 간주하고 수사를 계속하고 있습니다."),
        ("시위(하다)", "(示威) demonstration; protest (to demonstrate; to protest)", "정부 정책에 반대하는 시위가 벌어지고 있습니다.", "데모(하다)"),
        ("북송(하다/되다)", "(北送) sending to North Korea (to send to North Korea/to be sent to North Korea)", "중국으로 넘어간 탈북자들은 대부분 북송됩니다."),
        ("연합", "(聯合) alliance; coalition", "그 두 나라는 테러범에 대해 연합체제를 구축했습니다."),
        ("인신매매", "(人身賣買) human trafficking", "십 대 여성들의 인신매매는 국제적으로 큰 문제입니다."),
        ("퇴치(하다)", "(退治) eradication (to eradicate)", "그 단체는 에이즈를 퇴치하기 위해 모금운동을 벌이고 있습니다."),
        ("항의(하다)", "(抗議) a complaint; a protest (to protest)", "부정선거에 대해 항의하는 시위가 벌어지고 있습니다."),
    ]),
    ("학습활동 4", [
        ("~기 일쑤다", "to be a habitual practice; to be common", "바쁘면 아침을 안 먹고 출근하기 일쑤다."),
        ("매춘", "(賣春) prostitution; “selling spring”", "", "매음 | 매춘부"),
        ("민감하다", "(敏感) to be sensitive", "제 피부가 너무 민감해서 화장품을 고르기가 어렵습니다.", "둔감하다"),
        ("사연", "(事緣) a story; a situation", "열세 살 소녀의 어려운 사연이 방송되자 전국 각지에서 성금을 보내왔다."),
        ("성적 노리개", "(性的) a sex slave; “sexual plaything”", ""),
        ("실태", "(實態) the real condition; the actual condition; reality", "환경부는 환경오염 실태를 조사하기로 했습니다.", "실상"),
        ("여론 환기", "(與論 換氣) stirring up public opinion", "최근 사건을 두고 정부는 여론을 환기하고 있습니다."),
        ("전락(하다)", "(轉落) downfall; degradation; degeneration (to fall; to become degraded; to degenerate)", "대학교수였던 사람이 도박 중독으로 인해 범죄자로 전락했다."),
        ("조선족", "(朝鮮族) (a person of) Korean descent in China", ""),
        ("한족", "(漢族) Han Chinese", ""),
        ("허용(하다/되다)", "(許容) permission (to permit/to be permitted)", "이제부터 건물 내에서는 흡연이 허용되지 않습니다.", "허가(하다), 허락(하다)"),
    ]),
]
L5 = lesson(
    "U15 L9 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 날품팔이 · 노예 · 벌목공 · 상납 · 생계 · 선교사 · 허다하다 · 영주권 · 판정 · 시위 · 북송 · 인신매매 · 항의 · 민감하다 · 실태 · 전락 · 조선족 · 허용",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 3분의 1 → 삼 분의 일; 10대 → 십 대; 13살 → 열세 살. In the book’s example for 판정 the word 유행한 is a slip for 유해한 (harmful); it is corrected here. The book lists −기 일쑤다 with a minus sign; it is written ~기 일쑤다 here. The book lists 둔(감)하다 as the related word of 민감하다; it is written 둔감하다.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=18, nread=14)),
)

# ================================================================== L6 Part 3 texts
_OH = [
    ("오세혁은 고려대 대학원 시험에 합격했다.", "Oh Se-hyeok passed the entrance exam for the graduate school of Korea University."),
    ("사회학 전공이다.", "His major is sociology."),
    ("사회에 대해 다양한 시각을 갖고 바라볼 수 있는 학문이라는 데 반했다.", "He fell for the fact that it is a field of study through which one can look at society with various perspectives."),
    ("북한에서는 접하지 못한 학문이다.", "It is a field of study he could not encounter in North Korea."),
    ("그는 공부뿐만 아니라 반달이샵을 창업한 대학생 씨이오이기도 하다.", "He is not only studying but also a university student CEO who started up the Bandali Shop."),
    ("오세혁(서른두 살)은 천구백구십구 년 스물한 살의 나이에 북한을 떠나왔다.", "Oh Se-hyeok (32) left North Korea in 1999 at the age of 21."),
    ("어머니가 심장병으로 돌아가신 후에 집안은 급격히 기울었다.", "After his mother died of heart disease, the family declined rapidly."),
    ("설상가상으로 아버지는 노동당에서 쫓겨났다.", "To make matters worse, his father was kicked out of the Workers’ Party."),
    ("북한에서는 국민이라면 누구나 의무적으로 노동당에 가입해야 한다.", "In North Korea, every citizen must join the Workers’ Party as an obligation."),
    ("그것이 사회생활을 하기 위한 기본 조건이 된다.", "That becomes a basic condition for living a social life."),
    ("탈당이라는 것은 아무리 공부를 잘하고 기술이 좋아도 출세할 일, 아니 의식주를 해결할 일마저 막막해진다는 것을 의미한다.", "Leaving the party means that no matter how well one studies or how good one’s skills are, getting ahead — no, even solving the matter of food, clothing and shelter — becomes hopeless."),
    ("탈당의 원인은 다양하다.", "The causes of leaving the party are various."),
    ("당비를 제때 내지 못하거나 주민감시제에서 사람들의 신임을 잃었을 경우다.", "It is the case when one fails to pay party dues on time or loses people’s trust in the neighbor monitoring system."),
    ("아버지의 출당은 아버지 개인뿐 아니라 가족에까지 영향이 있었다.", "His father’s expulsion from the party affected not only his father personally but even the family."),
    ("도시의 작은 아파트에서 평범하게 살던 오세혁의 가족들은 생계를 잃고 농촌으로 쫓겨날 판이었다.", "Oh Se-hyeok’s family, who had lived an ordinary life in a small apartment in the city, were about to lose their livelihood and be driven out to the countryside."),
    ("그는 탈북을 결심했다.", "He decided to defect from North Korea."),
    ("“이대로 있을 수 없어 탈출구를 찾다가 중국에 가겠다고 했어요.", "“I couldn’t stay as things were, so while looking for a way out, I said I would go to China."),
    ("그러나 가족들은 반대했죠.", "But my family opposed it."),
    ("저 혼자 나올 수밖에 없었어요.", "I had no choice but to come out alone."),
    ("누나와 여동생, 그리고 아버지는 아직도 북에 계십니다.”", "My older sister, younger sister and father are still in the North.”"),
    ("북한에서 한국을 오는 데는 상상 이상의 다양한 경로와 방법이 있단다.", "They say there are various routes and methods beyond imagination for coming from North Korea to Korea."),
    ("브로커들도 판을 친다.", "Brokers also run rampant."),
    ("그는 비교적 쉽게 온 케이스다.", "He is a case who came relatively easily."),
    ("보호단체의 도움을 받아 기차를 타고 베이징의 독일 대사관을 통해 들어왔다.", "With the help of a protection group, he took a train and came in through the German embassy in Beijing."),
    ("힘든 건 혼자 시작하는 서울 생활이었다.", "What was hard was the Seoul life he started alone."),
    ("“복잡한 지하철이나 버스에도 적응이 안 되고 두려웠지만 우선 아파트에 들어오는 순간부터 충격이었어요.", "“I couldn’t adapt to the complicated subway or buses and was afraid, but first of all it was a shock from the moment I came into the apartment."),
    ("이제 나 혼자구나라는 생각 때문이죠.”", "It was because of the thought, ‘Now I’m all alone.’”"),
    ("게다가 북에 남겨진 가족들을 생각하면 가슴이 답답해진다.", "Besides, thinking of the family left behind in the North makes his chest feel tight."),
    ("그는 대사관을 통해 들어왔기 때문에 한국으로 갔다는 정보가 북한 정부에 들어갔을 확률이 크다.", "Because he came in through an embassy, there is a high probability that the information that he went to Korea reached the North Korean government."),
    ("분명 가족들이 피해를 당했을 것이다.", "His family surely suffered harm."),
    ("“가능하다면 가족들을 빨리 데려오고 싶어요.", "“If possible, I want to bring my family here quickly."),
    ("아니 소식만 알고 연락이 된다면 무슨 일이든 할 것 같아요.", "No, if I could just know news and get in touch, I think I would do anything."),
    ("제가 최선을 다해 목표를 빨리 이루는 것이 가족을 위한 일이라고 생각해요.”", "I think achieving my goals quickly by doing my best is something I do for my family.”"),
    ("그는 새터민 친구들 다섯 명과 함께 지난해 한국청년정책연구원의 도움으로 쇼핑몰을 창업했다.", "Together with five settler friends, he started an online shopping mall last year with the help of the Korea Youth Policy Research Institute."),
    ("창업 아이템은 반달이라는 곰 캐릭터다.", "The start-up item is a bear character called Bandali."),
    ("지금은 주로 캐릭터 티셔츠를 만들어 인터넷을 통해 판매하고 있다.", "Now he mainly makes character T-shirts and sells them over the Internet."),
    ("그는 앞으로 반달이를 이용해 스토리를 만들고 애니메이션으로 제작하는 방안을 구상하고 있다.", "He is planning a way to make a story using Bandali and produce it as an animation in the future."),
    ("관련업계 사람들의 조언을 얻고 다섯 명의 창단 멤버와 반달이를 본격적으로 키워 볼 생각이다.", "He intends to get advice from people in the related industry and to try growing Bandali in earnest with the five founding members."),
    ("그리고 대학원에 다니며 새터민 청소년들의 멘토 역할도 해나갈 것이다.", "And while attending graduate school, he will also carry on the role of a mentor for settler youths."),
]
_SPEAK3 = [("새터민들이 남한에 정착할 때 어떤 어려움이 있다고 생각합니까?", "What difficulties do you think settlers face when they settle in South Korea?"), ("친구와 의견을 나누어 보세요.", "Exchange opinions with a friend."), ("새터민들을 돕기 위해 한국 정부가 어떻게 해야 한다고 생각합니까?", "What do you think the Korean government should do to help settlers?")]
L6 = lesson(
    "U15 L9 · Part 3 (심화 학습): Oh Se-hyeok, a settler and student CEO",
    "심화 학습 · 새터민 · 노동당 · 탈당 · 주민감시제 · 반달이샵 · 적응 · 창업 · 멘토 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading • Speaking): a magazine article on a defector (새터민)",
             "The following is a magazine article on a defector (a new settler). The heading is “[새희망 새터민] 캐릭터 ‘반달이’로 쇼핑몰 창업 대학생 오세혁” (New-hope settlers: a university student who started a shopping mall with the character Bandali). The text is the book’s with the age and numbers spelled out (32 → 서른두 살; 1999년 → 천구백구십구 년; 21살 → 스물한 살; CEO → 씨이오), the quotation marks ‘ ’ removed, and the web address of the shop (www.halfmb.com) left out because it cannot be read aloud. The English is mine. (Text and images © Kyunghyang.)",
             examples=passage(_OH)),
        card("학습활동 1: the questions answered (mine)",
             "1. C — life for his family became more difficult (his mother died, his father was expelled from the Workers’ Party, and the family was about to lose its livelihood and be driven to the countryside).\n\n"
             "2. His first life in Seoul was hard: he began it alone and felt lonely (“now I’m all alone”), could not adapt to the complicated subway and buses and was afraid, was shocked from the moment he entered the apartment, and felt his chest tighten thinking of the family left behind, who were probably harmed because he came through an embassy.\n\n"
             "3. (a) To develop a story and an animation using the Bandali bear character, take advice from people in the industry and grow the business in earnest with the five founding members. (b) To attend graduate school and act as a mentor for settler youths.\n\n"
             "4. (Speaking, mine) His family probably suffered: because he entered through an embassy, the North Korean government likely learned that he had gone to South Korea, so his father and sisters may have been watched, questioned or punished. The article itself says only that they are still in the North and that harm to them is very likely."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK3)),
        card("Activities left out", "학습활동 2 (Listening, tracks 005 and 006): an interview with 최현미, a boxer who is a North Korean settler, from YTN — her feelings about going to college this year, about being called “새터민 복서” or “탈북 소녀”, adjusting to school life in South Korea, and why boxing is attractive to her. It is audio."),
    ],
    exercises=uniq(
        _tr(_OH, k=3) + _tr(_SPEAK3, k=2)
        + [M("What is Oh Se-hyeok’s major?", "Sociology", ["Economics", "Law", "Medicine"], "사회학 전공."), M("At what age did he leave North Korea?", "21", ["12", "32", "45"], "스물한 살."), M("What happened to his father?", "He was kicked out of the Workers’ Party", ["He became a general", "He moved to China", "He opened a shop"], "아버지는 노동당에서 쫓겨났다."), M("Who is still in the North?", "His older sister, younger sister and father", ["His mother", "His wife", "His friends"], "누나와 여동생, 그리고 아버지."), M("How did he come to Korea?", "By train, through the German embassy in Beijing", ["By boat", "By plane directly", "On foot across the DMZ"], "베이징의 독일 대사관."), M("What is Bandali?", "A bear character", ["A tiger", "A song", "A school"], "곰 캐릭터."), M("What does his shop mainly sell?", "Character T-shirts", ["Shoes", "Books", "Food"], "캐릭터 티셔츠."), M("How many founding members started the mall with him?", "Five", ["Two", "Ten", "One"], "다섯 명."), M("What will he do as a graduate student besides business?", "Act as a mentor for settler youths", ["Join the military", "Teach in China", "Retire"], "멘토 역할."),
           F("탈당은 북한에서 출세는커녕 의식주도 ___해진다. (hopeless)", "막막", ["녹록", "짜릿"], "막막하다."), F("그는 ___으로 아버지도 쫓겨났다. (to make matters worse)", "설상가상", ["적응", "충격"], "설상가상."), F("서울 생활에 ___하기가 힘들었다. (adapt)", "적응", ["극복", "탈당"], "적응."), F("그는 새터민 청소년의 ___ 역할도 할 것이다. (mentor)", "멘토", ["브로커", "복서"], "멘토."), F("그는 북한에서 노동당에 의무적으로 ___해야 했다. (join)", "가입", ["탈당", "반대"], "가입."),
           read_q("오세혁은 고려대 대학원 시험에 합격했습니다"), read_q("아버지는 노동당에서 쫓겨났습니다"), read_q("서울 생활에 적응하기가 힘들었습니다"), read_q("새터민 청소년들의 멘토 역할도 하겠습니다"), read_q("새터민들이 남한에 정착할 때 어떤 어려움이 있다고 생각합니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("곰", "a bear", ""),
        ("기울다", "to wane; to decline", "아버지가 돌아가신 후 집안이 기울었다.", "기울다 (to tilt)"),
        ("막막하다", "(漠漠) to not know; to be at a loss", "직장에서 해고를 당한 후 어떻게 살아야 할지 막막했다."),
        ("새터민", "(民) a new settler (from North Korea)", "새터민들이 남한에 정착하기가 힘들다고 합니다.", "탈북자, 이탈주민"),
        ("설상가상(으로)", "(雪上加霜) to make matters worse; what is worse; “adding frost to snow”", "얼마 전 어머니가 돌아가셨는데, 설상가상으로 아버지도 충격으로 쓰러지셨어요."),
        ("신임(하다)", "(信任) trust (to trust)", "새로 임명된 총리는 국민들의 신임을 얻고 있습니다.", "신임 (新任) newly appointed"),
        ("적응(하다)", "(適應) adaptation (to adapt oneself to)", "직장을 새로 옮겼는데 새 환경에 적응하기가 힘들어요."),
        ("쫓겨나다", "to be kicked out", "집세를 못 내서 쫓겨날 것 같아요.", "쫓아내다"),
        ("주민감시제", "(住民監視制) the neighbor monitoring system (in North Korea)", ""),
        ("충격", "(衝擊) impact; shock", "그 사건은 제게 큰 충격을 주었습니다."),
        ("탈당(하다)", "(脫黨) defection from a political party (to defect; to break away)", "", "입당하다"),
    ]),
    ("학습활동 2", [
        ("극복(하다/되다)", "(克服) conquest; overcome (to overcome/to be overcome)", "이 재정위기를 잘 극복해 나갑시다."),
        ("난관", "(難關) difficulty; impasse", "문제를 해결하는데 예상치 못한 난관을 만났어요.", "어려움 | 장애"),
        ("녹록치 않다", "to be tough; to be formidable; “to be not trifling”", "이 문제는 해결하기가 녹록치 않습니다.", "만만치 않다"),
        ("다가오다", "to approach", "아버지 환갑이 다가오고 있어요. 뭘 준비하면 좋을까요?", "접근하다"),
        ("뒷전", "to be pushed aside; a back seat", "우리 아이는 요즘 노느라고 공부는 뒷전입니다."),
        ("매력", "(魅力) attraction; charm", "이 일은 아주 큰 매력이 있어요."),
        ("받아들이다", "to accept; to embrace", "이 제안은 받아들이기가 좀 어렵습니다.", "수용하다"),
        ("방어(하다)", "(防禦) defense (to defend against)", "그 사람은 너무 방어적이어서 대화를 하기가 어렵습니다."),
        ("사각의 링", "(四角) a boxing ring; “the square ring”", ""),
        ("수식(하다/되다)", "(修飾) modification; ornamentation; embellishment (to modify/to be modified)", "이 단어를 수식하는 말이 무엇입니까?", "수식어 (a modifier)"),
        ("써 먹다", "to use (a newly learned skill or trick)", "친구한테 조금 불어를 배워서 프랑스 여행 동안 잘 써 먹었다."),
        ("짜릿하다", "to be thrilling; to be electrifying", "짜릿한 승리의 기쁨을 느껴 보고 싶습니다."),
    ]),
]
L7 = lesson(
    "U15 L9 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 곰 · 기울다 · 막막하다 · 새터민 · 설상가상 · 신임 · 적응 · 쫓겨나다 · 충격 · 탈당 · 극복 · 난관 · 녹록치 않다 · 뒷전 · 매력 · 받아들이다 · 짜릿하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book prints 쫒아내다 as the related word of 쫓겨나다; it is written 쫓아내다 here. The related entry of 기울다 (to tilt) is another meaning of the same spelling. In the example for 써 먹다 the book breaks the line between 써 and 먹다; it is joined here.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=14, nread=12)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 9: North Korea II (북한 II)", [L1, L2, L3, L4, L5, L6, L7])

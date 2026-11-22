"""Unit 83: KBC Semester III, Unit 17, Lesson 8 - Medical Sciences in Korea (한국의 의학).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 17, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_MATCH8 = [("수술", "surgery", "수술을 받기 위해 입원하다"), ("주사", "injection; a shot", "약도 먹고 주사도 맞다"), ("치료", "(medical) treatment", "가벼운 화상으로 치료를 받다"), ("부작용", "side effects", "성형수술 후 부작용으로 고생하다"), ("수명", "life span", "옛날에 비해 수명이 늘어나다"), ("질병", "a disease", "스트레스는 많은 질병의 원인이다"), ("소화", "digestion", "소화가 잘 안 돼서 내과에 가 보다"), ("식욕", "appetite", "요즘 날씨가 더워서 식욕이 없다"), ("증상", "a symptom", "제일 먼저 나타나는 증상은 기침이다")]
_HJ8 = [("新 신", "new", "신문, 신세대"), ("身 신", "body", "신체, 자신"), ("醫 의", "doctor; medical", "가정의, 전문의"), ("術 술", "technique; skill", "기술, 예술"), ("學 학", "learning", "학교, 과학")]
_HJW8 = [("신문", "a newspaper"), ("신세대", "a new generation"), ("신체", "a body"), ("자신", "(one’s) self"), ("가정의", "a family doctor"), ("전문의", "a specialist doctor"), ("기술", "technology"), ("예술", "art"), ("학교", "a school"), ("과학", "science")]
_ODD8 = [("입원, 퇴원, 학원, 병원", "학원", "a cram school is the odd one: the others belong to a hospital stay"), ("신사, 의사, 간호사, 약사", "신사", "a gentleman is the odd one: the others are medical professions"), ("다치다, 삐다, 데다, 식다", "식다", "to cool down is the odd one: the others are ways of getting hurt"), ("치료, 진찰, 진료, 유료", "유료", "“for a fee” is the odd one: the others are medical care"), ("장수, 웰빙, 건강, 비만", "비만", "obesity is my best guess: the others are positive health words")]
_SIM8 = [("신년", "새해", "new year: new year"), ("전신", "온몸", "the whole body: the whole body"), ("의원", "병원", "a clinic: a hospital")]
_CAT8 = [("과학, 수학, 문학, 의학", "학문", "fields of study"), ("외과, 치과, 내과, 이비인후과", "병원", "departments of a hospital"), ("음악, 미술, 무용, 연극", "예술", "the arts")]
_L8X = [("입원", "being admitted to a hospital"), ("퇴원", "discharge from a hospital"), ("학원", "a private academy"), ("병원", "a hospital"), ("신사", "a gentleman"), ("의사", "a doctor"), ("간호사", "a nurse"), ("약사", "a pharmacist"), ("다치다", "to get hurt"), ("삐다", "to sprain"), ("데다", "to get burned"), ("식다", "to cool down"), ("진찰", "an examination (by a doctor)"), ("진료", "medical care"), ("유료", "pay; for a fee"), ("장수", "longevity"), ("웰빙", "well-being"), ("비만", "obesity"), ("신년", "a new year"), ("새해", "the new year"), ("신입생", "a new student"), ("전신", "the whole body"), ("온몸", "the whole body"), ("당신", "you"), ("정신", "mind; spirit"), ("의원", "a clinic"), ("의술", "the art of medicine"), ("문의", "an inquiry"), ("외과", "surgery department"), ("치과", "dentistry"), ("내과", "internal medicine"), ("이비인후과", "ear, nose and throat department"), ("음악", "music"), ("미술", "fine art"), ("무용", "dance"), ("연극", "a play"), ("학문", "a field of study"), ("의학", "medicine (the science)")]
L1 = lesson(
    "U17 L8 · Review: medical words and Sino-Korean 新 身 醫 術 學",
    "한국의 의학 · 단어 복습 · 한자어 복습 · 수술 · 주사 · 치료 · 부작용 · 수명 · 질병 · 소화 · 식욕 · 증상 · 新 身 醫 術 學",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives nine sentences, one word of each underlined, and asks you to connect each with its English meaning on the right; the first is done as the example. The underline is not marked in the text; the pairs below are my best reading:", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH8], say=[0, 2])]),
        card("단어 복습 2: the odd one out (my answers)", "In each group of four words, circle the one unrelated to the other three:", tables=[table(["Group", "Odd one out", "Why"], [list(r) for r in _ODD8], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ8], say=[2]), ktable(_HJW8)]),
        card("한자어 복습 1: the most similar word (my answers)", "Circle the word closest in meaning to the word on the left (A. 신년: 신구, 신입생, 새해, 올해; B. 전신: 당신, 온몸, 반신, 정신; C. 의원: 의술, 문의, 의사, 병원).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM8], say=[0, 1])]),
        card("한자어 복습 2: the word that includes all four (my answers)", "Read the four words and choose from the box (병원, 의술, 기술, 예술, 학문) the word that can include them all:", tables=[table(["Four words", "Answer", "Meaning"], [list(r) for r in _CAT8], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L8X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH8], k=3) + _tr(_HJW8, k=3) + _tr(_L8X, k=4)
        + [M("What does the syllable 新 (신) mean?", "new", ["body", "doctor", "learning"], "신문."), M("What does the syllable 身 (신) mean?", "body", ["new", "doctor", "technique"], "신체."), M("What does the syllable 醫 (의) mean?", "doctor; medical", ["new", "body", "learning"], "전문의."), M("What does the syllable 術 (술) mean?", "technique; skill", ["new", "body", "doctor"], "기술."), M("What does the syllable 學 (학) mean?", "learning", ["new", "body", "technique"], "과학.")
           , M("Which word is closest in meaning to 신년?", "새해", ["신구", "신입생", "올해"], "New year."), M("Which word is closest in meaning to 전신?", "온몸", ["당신", "반신", "정신"], "The whole body."), M("Which word is closest in meaning to 의원?", "병원", ["의술", "문의", "의사"], "A clinic."), M("Which word covers 과학, 수학, 문학, 의학?", "학문", ["병원", "기술", "예술"], "Fields of study."), M("Which word covers 외과, 치과, 내과, 이비인후과?", "병원", ["의술", "학문", "예술"], "Departments."), M("Which word covers 음악, 미술, 무용, 연극?", "예술", ["병원", "기술", "학문"], "The arts."), M("Which word does not belong with 입원, 퇴원, 병원?", "학원", ["수술", "진료", "치료"], "A cram school."), M("Which word does not belong with 의사, 간호사, 약사?", "신사", ["의원", "한의사", "치과의사"], "A gentleman.")
           , F("수술을 받기 위해 ___하다. (to be admitted to a hospital)", "입원", ["퇴원", "치료"], "입원."), F("약도 먹고 ___도 맞다. (an injection)", "주사", ["수술", "증상"], "주사."), F("성형수술 후 ___으로 고생하다. (side effects)", "부작용", ["식욕", "수명"], "부작용."), F("옛날에 비해 ___이 늘어나다. (life span)", "수명", ["소화", "증상"], "수명."), F("요즘 날씨가 더워서 ___이 없다. (appetite)", "식욕", ["수명", "질병"], "식욕.")]
        + [read_q("수술을 받기 위해 입원하다"), read_q("성형수술 후 부작용으로 고생하다"), read_q("제일 먼저 나타나는 증상은 기침이다"), read_q("스트레스는 많은 질병의 원인이다")]
    ),
)

# ================================================================== L2 Part 1
_BUSAN8 = [
    ("부산 의료관광 외국인 연 만 명 돌파", "More than 10,000 foreigners a year in Busan medical tourism"),
    ("부산지역이 ‘의료관광 도시’라는 새 이미지를 만들어 가고 있다.", "The Busan area is building a new image as a “medical tourism city”."),
    ("부산시는 의료관광을 위해 부산을 찾는 외국인이 연간 만 명을 넘어섰다고 십구 일 밝혔다.", "On the 19th, Busan City announced that the number of foreigners visiting Busan for medical tourism has passed 10,000 a year."),
    ("유월 말까지 해외환자 진료 의료기관으로 등록한 병원만도 쉰네 곳이다.", "The hospitals that had registered as medical institutions treating overseas patients by the end of June number as many as 54 alone."),
    ("이는 전국의 이십 퍼센트가 넘는 수치로, 부산 인구가 전국 대비 약 칠 퍼센트인 것을 감안하면 높은 비율이다.", "This is a figure of over 20 percent of the whole country, which is a high ratio considering that Busan’s population is about 7 percent of the nation’s."),
    ("해외 환자진료 등록병원은 주로 성형, 피부, 치과, 한의원 등이지만 종합병원도 있다.", "The hospitals registered for treating overseas patients are mainly plastic surgery, dermatology, dental and Eastern medicine clinics, but there are general hospitals too."),
    ("등록 병원이 밀집한 서면 메디컬스트리트의 병원은 아예 오 월부터 관광사, 호텔, 항공사 등과 함께 의료관광상품을 개발 중이다.", "The hospitals of Seomyeon Medical Street, where the registered hospitals are concentrated, have outright been developing medical tourism products from May together with travel agencies, hotels, airlines and so on."),
    ("부산시도 지난 일 월부터 외국인 환자 유치가 가능해지면서 의료관광산업을 신성장 동력으로 규정하고 의료관광객 유치에 적극 나서고 있다.", "Busan City, too, since last January, when attracting foreign patients became possible, has defined the medical tourism industry as a new growth engine and is actively working to attract medical tourists."),
    ("시는 최근 영어, 일어, 중국어, 러시아어로 제작한 홍보물을 사 개국의 관광설명회에 배포했다.", "The city recently distributed promotional materials produced in English, Japanese, Chinese and Russian at tourism briefings in four countries."),
    ("김기천 부산시 보건위생과장은 “자발적으로 부산을 찾는 외국인 환자가 연간 만 명이 넘고 있지만, 이제는 이들 외에도 관심 있는 사람들을 적극 유치해야 할 때”라고 말했다.", "Kim Gi-cheon, the head of Busan City’s Public Health and Sanitation Division, said, “More than 10,000 foreign patients a year come to Busan on their own, but now is the time to actively attract, besides them, other people who are interested.”"),
    ("부산지역이 의료관광에서 두각을 나타낸 것은 의료기관이 사천이백여 개나 되고 편리한 교통, 풍부한 관광자원을 보유하고 있기 때문으로 분석된다.", "The reason the Busan area stands out in medical tourism is analyzed to be that it has as many as 4,200 or so medical institutions, convenient transport and rich tourism resources."),
    ("서울보다 의료비가 저렴한 것도 경쟁력의 하나라고 부산시는 설명했다.", "Busan City explained that medical costs cheaper than Seoul’s are also one of its competitive strengths."),
]
_SPEAK8A = [("로봇이나 첨단 기술을 의술에 이용하는 예에 대해 아는 대로 이야기해 보세요.", "Talk, as far as you know, about examples of using robots or advanced technology in medicine."), ("동양의학의 침이나 한약 같은 것이 서양의학과 어떻게 다른지 아는 대로 이야기해 보세요.", "Talk, as far as you know, about how things like acupuncture and herbal medicine of Eastern medicine differ from Western medicine."), ("동양의학을 직접 또는 간접 경험한 적이 있으면 그 경험에 대해 말해 보세요.", "If you have ever experienced Eastern medicine directly or indirectly, tell about that experience.")]
L2 = lesson(
    "U17 L8 · Part 1 (도입 학습): Eastern medicine and medical tourism in Busan",
    "도입 학습 · 한의학 · 한약 · 침 · 한의원 · 부산 · 의료관광 · 외국인 환자 · 유치 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 (Let’s find out), the book’s English note", "In Korea, the medical industry combines traditional medicine (한의학, written either 韓醫學 or 漢醫學) with advanced Western medicine. Korean people often take herbal medicines (한약) to cure illnesses and as a preventive measure. Medical herbalism is the study and practice of using plants and plant extracts medicinally. Acupuncture (침) is also very popular in Korea. For example, for a sprain, many Koreans visit a 한의원 to receive acupuncture treatment. Acupuncture enhances the flow of vital energy (also known as “qi” or “ki”) along pathways called 경락, or meridians."),
        card("학습활동 2: a newspaper article on medical tourism in Busan (Kyunghyang)", "The book asks three questions: (1) summarize the statistics on Busan as a destination for medical tourists; (2) how Busan City supports medical tourism; (3) which advantages Busan has. The book writes 1만 명, 19일, 6월, 54곳, 20%, 7%, 5월, 1월, 4개국 and 4200여 개 in digits; I spelled them in Hangul. The name of the division head is a public official’s, as in the article. The article, with my English:", examples=passage(_BUSAN8)),
        card("My answers to 학습활동 2", "1. More than 10,000 foreigners a year visit Busan for medical tourism; 54 hospitals had registered for treating overseas patients by the end of June, over 20 percent of the national total, while Busan has only about 7 percent of the country’s population. 2. The city regards the industry as a new growth engine and is active in attracting patients; it distributed promotional materials in English, Japanese, Chinese and Russian at tourism briefings in four countries; and the hospitals of Seomyeon Medical Street have been developing medical tourism products with travel agencies, hotels and airlines since May. 3. About 4,200 medical institutions; convenient transport; rich tourism resources; and medical costs cheaper than Seoul’s."),
        card("말해 봅시다! (speaking)", "The book’s two speaking prompts (the English is mine):", examples=passage(_SPEAK8A)),
        card("Activities left out", "학습활동 1 (Listening and speaking, track 001): a KBS video about a doctor of Korean medicine. You answer in English what is unique about him, how he became a doctor of Korean medicine (including his first encounter with it), what the patient says about him and what his plan for the future is; then in pairs you role-play the doctor and a reporter in conversational Korean and reverse roles. It is video and a role-play."),
    ],
    exercises=uniq(
        _tr(_BUSAN8[1:], k=3)
        + [M("How many foreigners a year does Busan receive for medical tourism, according to the city?", "More than ten thousand", ["About a thousand", "Over a million", "About fifty"], "만 명."), M("How many hospitals had registered for overseas patients by the end of June?", "54", ["20", "7", "4,200"], "쉰네 곳."), M("What share of the nation’s population does Busan have?", "About 7 percent", ["About 20 percent", "About 54 percent", "About 4 percent"], "칠 퍼센트."), M("Which languages are the promotional materials in?", "English, Japanese, Chinese and Russian", ["English and French", "Korean and Japanese", "Spanish and Thai"], "영어, 일어, 중국어, 러시아어."), M("What advantage does the article name about the cost?", "Cheaper medical fees than Seoul", ["Free treatment", "Insurance for all", "Cheaper flights"], "서울보다 의료비가 저렴한 것."), M("How many medical institutions does the Busan area have?", "About 4,200", ["About 420", "About 54", "About 10,000"], "사천이백여 개.")]
        + [F("서울보다 의료비가 ___한 것도 경쟁력의 하나다. (cheap)", "저렴", ["풍부", "편리"], "저렴하다."), F("부산시는 의료관광객 ___에 적극 나서고 있다. (attracting)", "유치", ["배포", "돌파"], "유치."), F("부산지역이 의료관광에서 ___을 나타냈다. (stood out)", "두각", ["관여", "충고"], "두각을 나타내다."), F("부산 인구가 전국 대비 약 칠 퍼센트인 것을 ___하면 높은 비율이다. (to take into account)", "감안", ["추구", "분석"], "감안하다.")]
        + [read_q("부산지역이 의료관광 도시라는 새 이미지를 만들어 가고 있다"), read_q("의료관광산업을 신성장 동력으로 규정하고 있다"), read_q("서울보다 의료비가 저렴한 것도 경쟁력의 하나다"), read_q("동양의학을 경험한 적이 있으면 말해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("능숙하다", "(能熟) to be proficient; to be skillful; to be adept", "젓가락을 능숙하게 사용하시는군요. 어떻게 배우셨어요?"),
        ("동양 철학", "(東洋 哲學) Eastern philosophy", "저는 대학에서 동양 철학을 전공했어요."),
        ("말솜씨", "eloquence; the gift of gab; verbal ability", "그 사람은 말솜씨가 아주 화려합니다."),
        ("발목", "an ankle", "넘어져서 발목이 삐었어요.", "손목, 목"),
        ("배낭 여행", "(背囊 旅行) backpacking; independent travel; budget travel; “backpack travel”", "내년에 유럽으로 배낭 여행을 갈 예정입니다."),
        ("앞장서다", "to take the lead; to be the first", "한 시민단체가 건강한 인터넷 문화 만들기 운동에 앞장서고 있다."),
        ("위대성", "(偉大性) greatness", "한국문화의 위대성을 널리 알리고 싶어요."),
        ("유창하다", "(流暢) to be fluent", "한국말이 아주 유창하시군요. 어디서 배우셨어요?"),
        ("입맛", "appetite; taste; “mouth taste”", "요즘 입맛이 없어요.", "식욕"),
        ("접하다", "(接) to learn/hear (about news, etc.); to border on; to adjoin", "사고 소식을 접하고 너무 놀랐습니다. 한반도는 북쪽으로 중국, 러시아와 접하고 있다."),
        ("침", "(鍼) a needle; acupuncture", "발목을 삐었는데, 침을 한 대 맞았더니 금방 나았어요.", "주사"),
        ("통증", "(痛症) a pain; an ache", "부상을 입은 그 선수가 통증이 심한 것처럼 보입니다."),
        ("특이하다", "(特異) to be unusual; to be unique", "그분은 특이한 스타일의 옷도 잘 소화합니다."),
        ("한문", "(漢文) classical Chinese (character)", "우리 한문 선생님은 재미있는 얘기를 많이 해 주십니다.", "한자"),
        ("한의사", "(韓醫師 or 漢醫師) a medical doctor practicing traditional Eastern medicine", "통증이 있으면 한의사한테 가 보세요."),
        ("한의원", "(韓醫院 or 漢醫院) an Eastern medical clinic (specializing in acupuncture and herbal medicine)", "요즘 몸이 약해졌어요. 한의원에 가서 약을 좀 지어 먹어야겠어요."),
        ("한의학", "(韓醫學 or 漢醫學) Eastern medicine", "저는 의대를 다니다가 한의학을 공부하고 싶어서 대입을 다시 준비하고 있어요."),
    ]),
    ("학습활동 2", [
        ("감안하다", "(勘案) to take into account", "차가 막힐 것을 감안해서 조금 일찍 출발합시다."),
        ("돌파(하다)", "(突破) breakthrough; passing; overcoming (to break through; to pass; to exceed; to overcome)", "영화 아바타의 관객이 일주일 만에 백만 명을 돌파했다."),
        ("두각을 나타내다", "(頭角) to distinguish oneself; to stand out", "그 학생은 뛰어난 재능으로 두각을 나타내고 있습니다."),
        ("밀집(하다)", "(密集) concentration; density (to be concentrated on)", "이곳에 공장들이 밀집해 있습니다."),
        ("배포(하다/되다)", "(配布) distribution (to distribute/to be distributed)", "새로 나온 화장품 샘플을 무료로 배포하고 있어요."),
        ("유치(하다)", "(誘致) bringing; luring (to invite; to lure)", "한국이 동계올림픽 유치를 위해 노력하고 있다."),
    ]),
]
L3 = lesson(
    "U17 L8 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 능숙하다 · 동양 철학 · 말솜씨 · 발목 · 배낭 여행 · 앞장서다 · 유창하다 · 입맛 · 접하다 · 침 · 통증 · 특이하다 · 한문 · 한의사 · 한의원 · 한의학 · 감안 · 돌파 · 두각 · 밀집 · 배포 · 유치",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the book 한의사, 한의원 and 한의학 have two possible Hanja each, 韓 (Korean) or 漢 (Chinese). 침 has 주사 as a related word, and the book warns that 침 also means “saliva; spit” and, written 針, “sting”. 접하다 has two examples, one for each meaning. 유치(하다) 誘致 has a homonym 유치 幼稚, “childishness”. 영화 아바타 in the example of 돌파 is the film title; the book writes 1주일 and 100만 명 in digits.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=16, nread=14)),
)

# ================================================================== L4 Part 2
_COL8 = [
    ("지난 연말에 아버지께서 갑자기 전신이 마비되어 병원 중환자실로 실려 가셨다.", "At the end of last year my father suddenly became paralyzed over his whole body and was carried to the hospital’s intensive care unit."),
    ("필자는 식구들에게 각오를 단단히 하자고 말하기도 했다.", "I even told my family to brace ourselves firmly."),
    ("그러던 아버지가 퇴원해 집에서 설을 쇠시게 되어 너무나 기뻤다.", "So I was overjoyed that my father, who had been like that, was discharged and came to spend New Year’s Day at home."),
    ("이 일을 겪으면서 우리나라의 보건의료 기술이 상당한 수준에 도달했다는 것을 실감했다.", "Going through this, I realized that our country’s health and medical technology has reached a considerable level."),
    ("우리나라는 우수한 보건의료 인력을 보유하고 있으며 보건의료 기술도 세계적인 수준에 도달해 있다.", "Our country has excellent health and medical personnel, and its health and medical technology has also reached a world-class level."),
    ("그동안 민간과 정부가 보건의료 연구에 적극적으로 투자한 결과다.", "It is the result of the private sector and the government investing actively in health and medical research in the meantime."),
    ("천구백구십오 년 이후 십일 년간 보건복지부가 지원한 규모는 구천오백오십억 원에 이른다.", "The amount supported by the Ministry of Health and Welfare over the eleven years since 1995 comes to 955 billion won."),
    ("그러나 이런 규모는 선진국에 비하면 한참 뒤지는 수준이다.", "But this scale is a level that lags far behind advanced countries."),
    ("보건의료 연구에 대한 투자는 하루빨리 확대해야 한다.", "Investment in health and medical research must be expanded as soon as possible."),
    ("다양한 혜택을 기대할 수 있기 때문이다.", "That is because various benefits can be expected."),
    ("요즘 홈쇼핑 채널마다 건강보험 상품이 큰 인기를 끈다.", "These days health insurance products are very popular on every home-shopping channel."),
    ("건강에 대한 막연한 불안과 의료비 부담 때문일 것이다.", "It must be because of vague anxiety about health and the burden of medical costs."),
    ("물론 만약의 사태에 대비한 개인의 준비는 철저할수록 좋다.", "Of course, the more thorough an individual’s preparation for an emergency, the better."),
    ("그러나 나와 내 가족의 삶의 질 향상을 위한 사회적 투자 역시 그 이상으로 중요하다.", "But social investment for improving the quality of life of me and my family is just as important, or more."),
]
_EFF8 = [
    ("첫째, 의료비를 절약할 수 있다.", "미국 국립보건원은 지난 삼십 년간 국민 일 인당 연간 삼천오백 원을 심혈관질환 연구에 투자하였는데, 그 결과 같은 기간 동안 심혈관질환에 의한 사망률이 육십삼 퍼센트나 줄었다."),
    ("둘째, 미래의 국가 성장 동력을 창출할 수 있다.", "바이오 기술 산업을 선점하기 위한 투자경쟁이 세계에서 치열하게 벌어지고 있다. 신약을 포함한 보건의료 관련 산업은 바이오 기술 산업의 핵심이다."),
    ("셋째, 양질의 일자리를 창출할 수 있다.", "지난해에 학사 이상의 학력을 가진 만여 명이 보건복지부가 지원한 보건의료 연구사업에 참여했다. 지금도 이보다 훨씬 많은 석사, 박사급 고급 인력이 생계를 위해 전공을 포기하고 구직을 위해 기웃거리고 있는 것이 현실이다."),
]
_SPEAK8B = [("과거에 또는 최근에 개발된 중요한 신약에는 어떤 것들이 있고 인류에 어떤 도움을 주었는지 서로 이야기해 보세요.", "Talk with each other about which important new drugs have been developed in the past or recently and how they have helped humankind."), ("사회가 고령화 되면서 노인 인구의 비율도 높아지고 있습니다.", "As society ages, the proportion of the elderly population is also rising."), ("노인 인구의 건강과 장수를 위하여 어떤 신약이 개발되면 좋을까요?", "What kind of new drug would be good to develop for the health and longevity of the elderly population?"), ("그밖에도 현대사회에서 앞으로 개발되길 바라는 신약에 대해 서로 이야기해 보세요.", "Besides that, talk with each other about new drugs you hope will be developed in modern society.")]
L4 = lesson(
    "U17 L8 · Part 2 (본 학습): investing in medical research",
    "본 학습 · 보건의료 · 연구 투자 · 중환자실 · 전신 · 퇴원 · 혜택 · 의료비 · 성장 동력 · 일자리 · 신약 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: an expert’s newspaper contribution on the need to invest in medical research (Hankyoreh)", "The book gives only a part of it (the third paragraph is missing) and asks: (1) the writer’s main point; (2) match the three effects of the missing paragraph with the related information; (3) why the writer starts with a personal experience (A. to show what areas research and development should invest in; B. to show the stark contrast between the plans of Korea’s medical policy and its reality; C. to praise the government’s continued investment; D. to tell readers about Korea’s advanced medical services). The book writes 1995년, 11년간 and 9550억 원 in digits; I spelled them in Hangul. The excerpt, with my English:", examples=passage(_COL8)),
        card("학습활동 3, task 2: the three effects and the related information (my matching)", "The book gives each effect and a block of related information in two columns, to be joined by lines. The lines are not drawn in the text, so the matching is mine, by meaning (first the saving of medical costs goes with the American example, where mortality fell; then the growth engine with the bio-technology investment race; then quality jobs with the researchers who have master’s or doctoral degrees):", tables=[table(["Effect", "Related information (matched)"], [list(r) for r in _EFF8], say=[0, 1])]),
        card("My answers to 학습활동 3", "1. The main point: investment in health and medical research should be expanded as soon as possible, because it brings various benefits to society and to people’s quality of life. 3. D: the writer’s own experience, in which his father recovered, makes him realize that Korea’s health and medical technology has reached a considerable level."),
        card("말해 봅시다! (speaking)", "The book’s two speaking prompts of Part 2 (the second is long; I split it into its sentences; the English is mine):", examples=passage(_SPEAK8B)),
        card("Activities left out", "학습활동 1 (Reading and speaking): a cartoon about a “dream new medicine”, whose main character is Mr. Song Bae; you summarize his story in English with a partner (the book gives, as the example, “Mr. Song Bae is a cartoonist and is not married”) and present it in Korean, in the third or first person; the class votes for the most interesting version. It is a picture story, so I cannot give its plot (the vocabulary of this part, such as a hair-growth solution, wrinkles, side effects and an internet dating site, hints at it). 학습활동 2 (Listening, tracks 002 and 003): two YTN items about the development of new medicines: you summarize the development stages in English, and choose which of four statements best summarizes the interviewee’s ideas about drug development in Korea (A. Korea has developed many new kinds of medicine, especially in the last 100 years; B. though Korea has a relatively short history of developing new medicine, the industry has advanced significantly; C. with a substance patent system, a new medicine was developed successfully in 1987; D. in 1999 Korea’s industry began to rival that of other countries). It is audio; B is only my guess from the vocabulary of that activity, which has 일천하다 (short history), 명실상부하다 and 자리매김하다."),
    ],
    exercises=uniq(
        _tr(_COL8, k=3)
        + [M("Why was the writer glad about his father?", "His father was discharged and spent New Year’s Day at home", ["His father retired", "His father started a business", "His father moved abroad"], "퇴원해."), M("What realization did the writer’s experience give him?", "Korea’s medical technology has reached a considerable level", ["Hospitals are too crowded", "Insurance is too expensive", "Doctors are too few"], "상당한 수준."), M("What does the writer say about the scale of the investment?", "It lags far behind advanced countries", ["It is the largest in the world", "It has been cut", "It is unnecessary"], "한참 뒤지는 수준."), M("What does the writer say must be done about the investment in research?", "Expand it as soon as possible", ["Reduce it", "Stop it", "Leave it to individuals"], "하루빨리 확대."), M("What reason does the writer give for the popularity of health insurance products?", "Vague anxiety about health and the burden of medical costs", ["Low prices", "Government orders", "Celebrity advertising"], "막연한 불안과 의료비 부담."), M("Which effect goes with the American example, according to my matching?", "Saving medical costs", ["Quality jobs", "A growth engine", "Longer holidays"], "사망률이 줄었다."), M("Which effect goes with the investment race for the bio-technology industry?", "A growth engine for the future", ["Saving medical costs", "Quality jobs", "Cheaper insurance"], "성장 동력.")]
        + [F("어머니가 ___실에 계십니다. (intensive care unit; my sentence)", "중환자", ["진료", "수술"], "중환자실."), F("우리나라의 보건의료 기술이 상당한 수준에 도달했다는 것을 ___했다. (to realize)", "실감", ["각오", "선점"], "실감하다."), F("다양한 ___을 기대할 수 있기 때문이다. (benefits)", "혜택", ["각오", "양질"], "혜택."), F("보건의료 연구에 대한 투자는 하루빨리 ___해야 한다. (to expand)", "확대", ["포기", "절약"], "확대하다.")]
        + [read_q("보건의료 연구에 대한 투자는 하루빨리 확대해야 한다"), read_q("우리나라의 보건의료 기술이 상당한 수준에 도달했다"), read_q("건강에 대한 막연한 불안과 의료비 부담 때문일 것이다"), read_q("사회적 투자 역시 그 이상으로 중요하다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("겉", "the outside; the exterior", "저 사람은 겉은 차가워 보이지만 마음이 아주 따뜻하다.", "밖, 바깥 / 속, 안"),
        ("노총각", "(老總角) an old bachelor", "올해는 노총각 신세를 벗어나고 싶습니다.", "노처녀 / 총각, 처녀"),
        ("독신주의자", "(獨身主義者) a person who believes in remaining single", "저는 독신주의자는 아니지만 당분간 결혼할 생각은 없어요.", "독신"),
        ("만화가", "(漫畵家) a cartoonist", "그 만화가는 노인문제를 주제로 따뜻한 만화를 발표하고 있습니다."),
        ("발모제", "(發毛劑) a hair-growth solution", "요즘 탈모가 심해져서 발모제를 발라야겠어요."),
        ("부작용", "(副作用) a side effect", "제품을 사용하신 후 피부가 빨개지는 등 부작용이 있으면 곧바로 알려주세요."),
        ("분해(하다/되다)", "(分解) disassembling (to disassemble/to be disassembled)", "이 제품은 조립과 분해가 간편합니다."),
        ("속속", "(續續) one after another; one after the other", "현 정부의 부정부패의 모습들이 속속 드러나고 있습니다.", "계속해서, 연속해서, 연이어, 잇달아"),
        ("신약", "(新藥) a new drug; a new medicine", "이 신약은 아직 실험 단계에 있습니다."),
        ("예술", "(藝術) art", "그분은 예술적인 재능이 탁월합니다.", "예술가, 미술"),
        ("욕심", "(慾心) greed; avarice", "그 친구는 다 좋은데 욕심이 너무 많다.", "욕구"),
        ("주름", "a wrinkle", "요즘 얼굴에 주름이 부쩍 늘었어요."),
        ("중매소", "(仲媒所) an internet dating site", "저는 우리 남편을 결혼 중매소에서 만났어요.", "결혼정보회사"),
        ("한가하다", "(閑暇) to be free; to be at leisure", "오늘은 바쁘지만 내일은 한가해요. 전화하세요."),
    ]),
    ("학습활동 2", [
        ("게놈 지도", "(地圖) a genome map", ""),
        ("난치병", "(難治病) an intractable disease; “disease that is hard to cure”", "암, 심장병, 치매 등은 대표적인 난치병입니다.", "불치병"),
        ("명실상부하다", "(名實相符) to be true to one’s name; to live up to one’s reputation", "중국은 이제 명실상부한 경제대국으로 성장했다."),
        ("무에서 유를 창조하다", "(無 有 創造) to create something out of nothing", "한국 전쟁 후 한국의 경제발전은 무에서 유를 창조해 낸 것과 같다."),
        ("물질특허", "(物質特許) patent for substances", ""),
        ("불치병", "(不治病) an incurable disease", "우리 아버지가 불치병으로 고생하고 계십니다.", "난치병"),
        ("생소하다", "(生疎) to be unfamiliar; to be strange", "처음 이곳에 왔을 때는 모든 것이 생소했다."),
        ("선정(하다/되다)", "(選定) selection; choice (to select; to choose/to be selected; to be chosen)", "그 레스토랑은 몬트레이에서 가장 맛있는 식당으로 선정되었다."),
        ("신물질", "(新物質) a new material; a new substance", ""),
        ("약효", "(藥效) a medicinal effect", "약을 복용한 후 한 시간쯤 되면 약효가 나타날 겁니다."),
        ("연장(하다/되다)", "(延長) extension (to extend/to be extended)", "그 영화가 인기가 높자 극장들은 상영 기간을 연장했다."),
        ("일천하다", "(日淺) to be short; to be shallow", "제 사회 경험이 일천해서 실수가 많아도 이해해 주시기 바랍니다."),
        ("임상 실험", "(臨床 實驗) a clinical experiment; a clinical trial", "그 약은 현재 임상 실험 중입니다."),
        ("자리매김하다", "to position oneself as; to emerge as", "진해군항제는 한국의 대표적인 축제로 자리매김했다."),
        ("천연물질", "(天然物質) a natural substance; a natural material", "이 약은 천연물질로만 만들어져서 부작용이 없을 겁니다."),
        ("추출(하다/되다)", "(抽出) extraction (of a substance, element, etc., in chemistry) (to extract/to be extracted)", "이 약은 콩에서 추출한 단백질로 만들었습니다."),
        ("탄생(하다)", "(誕生) birth (to be born)", "최근 이집트에서의 시위는 중동지역에서 민주주의를 탄생시켰습니다."),
        ("합성(하다/되다)", "(合成) synthesis (to synthesize/to be synthesized)", "합성세제를 너무 많이 쓰면 환경에 좋지 않아요."),
    ]),
    ("학습활동 3", [
        ("각오(하다)", "(覺悟) determination; resolution; bracing (to be determined; to brace)", "이 정도 일은 처음부터 각오했던 것이에요."),
        ("선점(하다)", "(先占) preoccupation (to occupy in advance; to position oneself ahead)", "경쟁사들이 시장을 선점하기 위해 경쟁이 치열합니다."),
        ("설을 쇠다", "to celebrate New Year’s Day", ""),
        ("실감하다", "(實感) to realize", "혼자 살다 보니 가족의 소중함을 실감하고 있습니다."),
        ("심혈관 질환", "(心血管 疾患) a cardiovascular disease", ""),
        ("양질", "(良質) good quality", "저희 회사는 고객님들께 항상 양질의 서비스를 제공하기 위해 최선을 다하고 있습니다."),
        ("전신", "(全身) the whole body", "그는 화재사고로 전신에 삼 도 화상을 입었다.", "반신, 상반신, 하반신"),
        ("중환자실", "(重患者室) an intensive care unit (ICU); “serious patient room”", "어머니가 중환자실에 계십니다.", "집중치료실"),
        ("치열하다", "(熾烈) to be intense; to be fierce", "현대 사회는 경쟁이 너무 치열해서 스트레스를 받는 젊은이들이 많습니다."),
        ("혜택", "(惠澤) a benefit", "아이를 많이 낳는 다자녀가구에 세금 혜택을 준다고 합니다."),
    ]),
]
L5 = lesson(
    "U17 L8 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 겉 · 노총각 · 독신주의자 · 만화가 · 발모제 · 부작용 · 속속 · 신약 · 욕심 · 주름 · 중매소 · 난치병 · 불치병 · 명실상부 · 물질특허 · 약효 · 임상 실험 · 자리매김 · 천연물질 · 추출 · 탄생 · 합성 · 각오 · 선점 · 실감 · 심혈관 질환 · 양질 · 전신 · 중환자실 · 치열 · 혜택",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 게놈 지도, 물질특허, 신물질, 설을 쇠다 and 심혈관 질환. In the book 겉 lists 밖, 바깥 as similar and 속, 안 as opposites; 노총각 lists 노처녀 and 총각, 처녀 as related (here separated by a slash); 속속 lists “계속(해서), 연속(해서), 연이어, 잇달아”, written here without the parentheses. 신약 has a homonym 新約, “New Testament”; 전신 has a homonym 電信, “telegraph”. The book writes 1시간 and 3도 in digits; the example of 자리매김하다 lacks a space after 한국의 in the book, which I added. 게놈 is the loan word for “genome”, so only 地圖 (map) is given in Hanja.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=16, nread=14)),
)

# ================================================================== L6 Part 3
_MT8 = [
    ("의료관광, 서비스정신이 필요하다", "Medical tourism needs a service spirit"),
    ("‘의료관광’이란 “수술과 기타 전문적인 치료를 원하는 환자들에게 관광산업과 결합하여 저렴한 비용으로 효과적인 의료서비스를 제공하는 것”을 말한다.", "“Medical tourism” means “providing effective medical service at low cost, combined with the tourism industry, to patients who want surgery and other specialized treatment.”"),
    ("이러한 의료관광은 여러 나라가 차세대 성장 동력의 하나로 보고 국가적으로 총력을 쏟아 의료관광을 활성화하기 위해 노력하고 있다.", "Many countries regard such medical tourism as one of the next generation’s growth engines and are making efforts, pouring in their full national strength, to invigorate it."),
    ("의료관광 선도국인 인도, 싱가포르, 태국은 지난 해 각각 십팔만, 삼십칠만, 백오십만 명의 국제환자가 다녀갔으나 우리나라는 총 만 오천 명 정도에 불과하다.", "India, Singapore and Thailand, the leading countries in medical tourism, were visited last year by 180,000, 370,000 and 1,500,000 international patients respectively, but Korea has only about 15,000 in total."),
    ("우리나라는 최고의 인적 자원, 기술 수준의 비약적 발전, 저렴한 의료 수가 등 가격대비 비교우위의 경쟁력을 갖고 있음에도 불구하고 우리나라의 의료관광객 숫자가 선도국가들에 비해 크게 차이가 나는 이유는 아직 우리나라가 총체적으로 국제환자를 수용할 만한 자세를 갖추고 있지 못하기 때문이다.", "Although Korea has competitive strengths of comparative advantage for the price, such as the best human resources, rapid advances in technology and low medical fees, the reason the number of its medical tourists differs greatly from that of the leading countries is that Korea does not yet, overall, have the attitude to accommodate international patients."),
    ("우리나라의 의료관광이 성공하기 위해서는 여러 가지 바꾸어야 할 것들이 많다.", "For Korea’s medical tourism to succeed, there are many things that must be changed."),
    ("먼저 의료계의 혁신적인 마인드 변화가 필수적이다.", "First, an innovative change of mind in the medical world is essential."),
    ("의료기관 종사자 특히 의사들에게 서비스 및 비즈니스 마인드를 심어 주어야 한다.", "A service and business mind must be instilled in those working at medical institutions, especially doctors."),
    ("환자가 자신의 질병에 대해 설명을 듣고 싶은 사람은 행정요원이나 간호사가 아닌 의사이다.", "The person from whom a patient wants to hear an explanation of his own illness is a doctor, not an administrative staff member or a nurse."),
    ("국제환자를 진료할 수 있는 인프라를 구축하기 위하여 대형 대학병원의 ‘병원 내 병원’ 형태로 국제병원 개설을 허용하거나, ‘전문병원’ 제도의 도입을 서둘러 특정 질환을 전문적으로 진료하는 것이 바람직하다.", "To build an infrastructure that can treat international patients, it is desirable to allow international hospitals to open in the form of a “hospital within a hospital” at large university hospitals, or to hurry the introduction of a “specialty hospital” system and treat specific diseases specially."),
    ("정부와 국회는 관련 법규의 제정과 개정에 박차를 가해야 한다.", "The government and the National Assembly must step up the enactment and revision of the related laws and regulations."),
    ("의료관광을 활성화시킬 수 있도록 법규를 고쳐야 한다.", "The laws must be revised so that medical tourism can be invigorated."),
    ("국제환자에 대한 유인, 알선을 허용하고 의료기관과 환자 사이에서 예약 및 의료 정보 서비스를 제공하는 전문 에이전시가 안정적으로 활동할 수 있도록 의료관광 활성화를 위한 예산편성과 적극적인 지원이 필요하다.", "Budgeting and active support to invigorate medical tourism are needed, allowing the luring and brokering of international patients and letting specialized agencies that provide reservation and medical-information services between medical institutions and patients operate stably."),
]
_SUG8 = [("Doctors", "의료계의 혁신적인 마인드 변화가 필수적이다. 의료기관 종사자 특히 의사들에게 서비스 및 비즈니스 마인드를 심어 주어야 한다. 환자는 설명을 의사에게 직접 듣고 싶어 한다."), ("Hospitals", "대형 대학병원의 ‘병원 내 병원’ 형태로 국제병원 개설을 허용하거나, ‘전문병원’ 제도의 도입을 서둘러 특정 질환을 전문적으로 진료한다."), ("Government", "정부와 국회는 관련 법규의 제정과 개정에 박차를 가해야 한다. 국제환자에 대한 유인, 알선과 전문 에이전시를 허용하고, 예산편성과 적극적인 지원을 해야 한다.")]
_SPEAK8C = [("미국의 의료보험제도에 대해서 이야기해 보세요.", "Talk about the American health insurance system."), ("무엇이 좋고 어떤 것을 개선해야 하는지 토론하세요.", "Discuss what is good and what should be improved."), ("두 그룹으로 나누어 안락사에 대해 찬반 토론을 해 보세요.", "Divide into two groups and debate for and against euthanasia."), ("미국의 선한 사마리아인 법에 대해서 이야기해 보세요.", "Talk about the American Good Samaritan law."), ("어떤 법인지, 어떨 때 지켜야 하는지, 실제로 어떤 예들이 있는지 말해 보세요.", "Tell what kind of law it is, when it must be observed and what real examples there are.")]
L6 = lesson(
    "U17 L8 · Part 3 (심화 학습): a column on medical tourism and the service spirit",
    "심화 학습 · 의료관광 · 서비스정신 · 선도국 · 국제환자 · 병원 내 병원 · 전문병원 · 법규 · 안락사 · 의료보험 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: a newspaper column “Medical tourism needs a service spirit” (Naeil)", "The book asks: (1) the definition of medical tourism according to Gupta (2004); (2) how Korea’s medical tourism compares with that of the leading countries; (3) the suggestions for doctors, hospitals and the government. The text cites the definition as “(Gupta, 2004)”, which cannot be read as Korean, so I dropped that citation and give it here; the numbers (18만, 37만, 150만, 1만5000명) are spelled in Hangul and “제•개정” is written out as 제정과 개정. The column, with my English:", examples=passage(_MT8)),
        card("My answers to 학습활동 1", "1. According to Gupta (2004), medical tourism is providing effective medical service at low cost, combined with the tourism industry, to patients who want surgery and other specialized treatment. 2. India, Singapore and Thailand, the leading countries, received 180,000, 370,000 and 1,500,000 international patients last year, but Korea only about 15,000 in total, although Korea has the competitive strengths of top human resources, rapid technological progress and low medical fees; the cause is that Korea does not yet have, overall, the attitude for accommodating international patients.", tables=[table(["Group", "Suggestion (from the column; my table)"], [list(r) for r in _SUG8], say=[1])]),
        card("말해 봅시다! (speaking)", "The book’s three speaking prompts of Part 3. In the third the book writes “Good Samaritan Law” in Latin letters and in the second adds the English “euthanasia”; I wrote them in Korean (선한 사마리아인 법, 안락사). The English is mine:", examples=passage(_SPEAK8C)),
        card("Activities left out", "학습활동 2 (Listening, track 004): a recorded interview with an expert from the Seoul Education Research & Information Institute: you answer in English what profession is introduced, the interviewee’s educational background, why the profession is needed in modern society and what he recommends to prospective candidates and why. 학습활동 3 (Listening and speaking, tracks 005 and 006): a historical drama (MBC America) about Huh Jun, a doctor of traditional Eastern medicine, who faces a dilemma when treating patients on his way to the capital to take the civil-service exam (과거); you summarize his dilemma and final decision in English; then you hear three middle-school students debate his decision, summarize each student’s opinion in English, and discuss as a class what you would do if your personal interests conflicted with the public interest, using 허준 as an example. They are video and audio."),
    ],
    exercises=uniq(
        _tr(_MT8[1:], k=3)
        + [M("Which countries are named as leading countries in medical tourism?", "India, Singapore and Thailand", ["Japan, China and Mongolia", "Canada, Mexico and Brazil", "France, Spain and Italy"], "인도, 싱가포르, 태국."), M("About how many international patients did Korea receive, according to the column?", "About fifteen thousand", ["About 150 thousand", "About 1.5 million", "About 370 thousand"], "만 오천 명."), M("What does the column say Korea lacks?", "The attitude to accommodate international patients as a whole", ["Doctors", "Medical technology", "Low prices"], "자세를 갖추고 있지 못하기 때문."), M("What mind must be instilled in doctors?", "A service and business mind", ["A research mind", "A military mind", "A retirement mind"], "서비스 및 비즈니스 마인드."), M("Whom do patients want to hear an explanation of their illness from?", "A doctor", ["A nurse", "An administrator", "A pharmacist"], "의사."), M("What form of international hospital does the column suggest?", "A “hospital within a hospital” at large university hospitals", ["A floating hospital", "A hospital at the airport", "A hospital in every school"], "병원 내 병원."), M("What must the government and the National Assembly speed up?", "Enacting and revising the related laws", ["Building highways", "Cutting taxes", "Closing hospitals"], "제정과 개정.")]
        + [F("의료관광 ___국인 인도, 싱가포르, 태국. (leading)", "선도", ["후진", "중립"], "선도국."), F("우리나라는 저렴한 의료 ___ 등 경쟁력을 갖고 있다. (fee)", "수가", ["혜택", "주역"], "의료 수가."), F("정부는 관련 법규의 제정과 개정에 ___를 가해야 한다. (spurs)", "박차", ["각오", "충고"], "박차를 가하다."), F("국제환자를 ___할 만한 자세를 갖추고 있지 못하다. (to accommodate)", "수용", ["알선", "유인"], "수용하다."), F("미국의 의료보험제도에서 무엇을 ___해야 하는지 토론하세요. (to improve)", "개선", ["취급", "포기"], "개선하다.")]
        + [read_q("의료관광 선도국인 인도와 싱가포르와 태국"), read_q("의료관광 활성화를 위한 적극적인 지원이 필요하다"), read_q("우리나라는 저렴한 의료 수가 등 경쟁력을 갖고 있다"), read_q("두 그룹으로 나누어 안락사에 대해 찬반 토론을 해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("박차를 가하다", "(拍車 加) to put spurs to; to spur; to expedite; to accelerate", "우리 연구팀은 신기술 개발에 박차를 가하고 있습니다."),
        ("비교 우위", "(比較 優位) comparative advantage", "우리 회사 제품이 기술과 가격 면에서 타사 제품에 비해 비교 우위를 점하고 있습니다."),
        ("비약적", "(飛躍的) rapid (growth, improvement, etc.); swift; leaping; “fly and leap”", "한국의 경제는 천구백칠십 년대 이후에 비약적으로 발전했습니다.", "비약하다"),
        ("선도국", "(先導國) a leading country", "캐나다는 대표적인 금연 선도국입니다."),
        ("성장 동력", "(成長 動力) a growth engine; a dynamic force for growth", "앞으로 이 분야가 새로운 성장 동력이 될 것입니다."),
        ("수용(하다)", "(收容) accommodation (to accommodate; to seat; to hold)", "이 강당은 삼백 명을 수용할 수 있다."),
        ("알선(하다)", "(斡旋) arranging; helping someone get/find something (to arrange; to help someone get something)", "친구가 내게 아르바이트 일을 알선해 주었다.", "주선"),
        ("예산 편성", "(豫算 編成) drawing up a budget; budgeting; compilation of a budget", "내년도 예산 편성 문제를 놓고 국회에서 논쟁이 끊이지 않습니다."),
        ("유인(하다)", "(誘引) luring (to lure; to induce)", "범인이 아이를 유인해서 납치해 갔습니다."),
        ("의료 수가", "(醫療 酬價) the charge for medical treatment; a medical fee", ""),
        ("인적 자원", "(人的 資源) human resources; manpower", "우리나라의 큰 경쟁력은 우수한 인적 자원입니다."),
        ("차세대", "(次世代) the next generation", "한국 공군은 차세대 전투기를 개발 중이다."),
        ("총력", "(總力) one’s full energy; all one’s power", "정부는 월드컵 경기 유치를 위해 총력을 기울이고 있다."),
        ("활성화(하다)", "(活性化) vitalization; invigoration; galvanization (to vitalize; to invigorate; to galvanize)", "정부는 경기를 활성화하기 위해 대책을 마련하고 있습니다."),
    ]),
    ("학습활동 2", [
        ("광우병", "(狂牛病) mad cow disease; BSE (bovine spongiform encephalopathy)", ""),
        ("무궁무진(하다)", "(無窮無盡) endlessness; infiniteness (to be endless; to be infinite; to be a lot)", "이 분야는 앞으로 발전 가능성이 무궁무진합니다."),
        ("배아복제", "(胚芽複製) cloning of embryos", ""),
        ("안락사", "(安樂死) euthanasia", ""),
        ("윤리", "(倫理) ethics", "안락사를 인정하는 것에 대해 윤리적인 논란이 끊이지 않습니다.", "도덕"),
        ("의대", "(醫大) a college of medicine; a medical school", "", "의과 대학, 약대, 치대"),
        ("임상의사", "(臨床醫師) a practitioner of general medicine; a clinician", "저는 연구보다는 임상의사를 하고 싶어요."),
        ("재정", "(財政) finance; financial affairs", "회사의 재정 상태가 좋지 않다고 합니다."),
        ("제약산업", "(製藥産業) pharmaceutical industry", "그 회사가 제약산업에 뛰어들 거라고 합니다."),
        ("조류 독감", "(鳥類 毒感) bird flu; avian influenza", "", "돼지 독감, 신종 플루"),
        ("주역", "(主役) leading role; a title role; a main character", "그 배우가 한류 열풍의 주역이지요."),
        ("줄기세포", "(細胞) stem cell", ""),
        ("차원", "(次元) dimension; a level", "", "삼차원"),
        ("취급(하다)", "(取扱) handling; dealing (to handle; to deal)", "주로 어떤 물건을 취급하십니까?"),
        ("한직", "(閑職) an unimportant job; a trivial office/post", "그 일 이후에 그는 한직으로 밀려 났어요.", "요직"),
        ("후학", "(後學) next-generation students", "김 교수님은 훌륭한 후학들을 많이 두셨습니다.", "후배"),
    ]),
    ("학습활동 3", [
        ("은/는커녕", "far from; let alone; to say nothing of", "목이 아파서 밥은커녕 물도 마실 수 없다."),
        ("겹겹이", "layer upon layer; in layers", "날씨가 추우니까 옷을 겹겹이 입으세요."),
        ("과거(를 보다)", "(科擧) the highest level examination for recruiting high-ranking government officials during the Chosun Dynasty (to take the examination)", ""),
        ("나절", "half a day; half the daylight hours", "한나절 내내 아무 것도 못 먹었더니 배고파요.", "한나절, 반나절, 아침 나절, 저녁 나절"),
        ("당도(하다)", "(當到) arrival (to arrive)", "시간 내에 그곳에 당도하려면 지금 출발해야 합니다.", "도착"),
        ("당초(에)", "(當初) initially; in/from the beginning; originally", "구조작업이 당초 계획했던 것보다 훨씬 더 늦어지고 있습니다.", "애초, 처음"),
        ("대사", "(大事) an important job/matter; “big matter”", "다음 달에 결혼하신다구요? 대사를 앞두고 바쁘시겠어요.", "중대사"),
        ("동의보감", "(東醫寶鑑) an encyclopedia of Eastern medicine compiled by Huh Jun (허준) during the Chosun Dynasty", ""),
        ("등창", "(瘡) an abscess on the back; an infected swelling on the back", ""),
        ("목이 빠지게 기다리다", "to wait anxiously for; to wait for ages; “wait to the extent that the neck pops out”", ""),
        ("무지렁이", "an ignorant person", ""),
        ("소설", "(小說) a novel; fiction; a story", "소설은 픽션이지만 현실을 담고 있습니다.", "단편 소설, 장편 소설, 시, 수필"),
        ("약조", "(約條) (archaic) a promise; a pledge", "약조를 지켜 주십시오.", "약속"),
        ("의원", "(醫員) a doctor", "", "의사"),
        ("장면", "(場面) a scene", "그 장면이 저는 아주 인상적이었습니다."),
        ("중립적", "(中立的) neutral", "저는 이 문제에 대해서는 중립적인 입장을 취하고 싶습니다."),
        ("지체(하다)", "(遲滯) delay; procrastination (to delay; to procrastinate; to tarry)", "더 이상 지체하지 말고 빨리 시작합시다."),
        ("쪼개다", "to split; to break up", "저는 바쁜 시간을 쪼개 매주 봉사활동을 합니다."),
        ("차례", "(次例) (one’s) turn; order", "다음 누구 차례입니까?", "순서"),
        ("천금 같다", "(千金) to be priceless; to be invaluable; “like gold in the thousands”", "이 천금 같은 시간이 아깝지도 않습니까?"),
    ]),
]
L7 = lesson(
    "U17 L8 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 박차 · 비교 우위 · 비약적 · 선도국 · 성장 동력 · 수용 · 알선 · 예산 편성 · 유인 · 의료 수가 · 인적 자원 · 차세대 · 총력 · 활성화 · 광우병 · 안락사 · 윤리 · 줄기세포 · 임상의사 · 제약산업 · 조류 독감 · 주역 · 차원 · 한직 · 후학 · 겹겹이 · 과거 · 동의보감 · 소설 · 약조 · 의원 · 중립적 · 지체 · 쪼개다 · 차례",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 광우병, 배아복제, 안락사, 줄기세포, 과거, 동의보감, 등창, 무지렁이, 목이 빠지게 기다리다, 의료 수가, 의대, 조류 독감 and 차원. The headword ~은/는 커녕 is written in the book with spaces and with a related phrase ~은/는 말 할 것도 없고 (“to say nothing of”); here I wrote 은/는커녕 and 밥은커녕, the standard spelling. For 줄기세포 the book gives only 細胞. The book’s homonyms are noted here: 수용 收容 / 受容 (“acceptance; embrace; agreement”), 당도 當到 / 糖度 (“sugar content”), 대사 大事 / 大使 (“an ambassador”) / 臺詞 (“a line of a theatrical script”), 의원 醫員 / 醫院 (“a clinic”) / 議員 (“a congressman”), 차례 次例 / 茶禮 (“an ancestral service”); 한직 has 요직 (要職) as its opposite. The book writes 1970년대 and 300명 in digits, which I spelled in Hangul. 비약적 has 비약하다 as a related word.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=14)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 8: Medical Sciences in Korea (한국의 의학)", [L1, L2, L3, L4, L5, L6, L7])

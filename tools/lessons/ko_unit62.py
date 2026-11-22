"""Unit 62: KBC Semester III, Unit 15, Lesson 7 - World News (세계뉴스).
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
_W7 = [("상품권", "a gift certificate"), ("대표", "a representative"), ("잡지", "a magazine"), ("쓰레기", "garbage; trash"), ("오염", "pollution"), ("박람회", "a fair; an expo"), ("지속", "lasting; continuing"), ("기간", "duration")]
_C7 = [("취업이 어렵다.", "It is hard to find a job."), ("급여가 낮다.", "The pay is low."), ("우울증에 시달리다.", "to suffer from depression"), ("대학에 진학하다.", "to go on to college"), ("소지품을 잃어버리다.", "to lose one’s belongings"), ("쓰레기를 재활용하다.", "to recycle garbage"), ("우승을 차지하다.", "to win the championship")]
_HJ7 = [("職 직", "job; position", "퇴직, 직업"), ("最 최", "the most; the -est", "최장, 최소"), ("給 급", "give; provide", "급여, 급식"), ("社 사", "gather; meeting", "회사, 입사"), ("現 현", "appear; current", "현장, 현재")]
_HJW7 = [("퇴직", "a retirement"), ("직업", "an occupation"), ("최장", "the longest"), ("최소", "the smallest"), ("급여", "salary; pay"), ("급식", "school meals"), ("회사", "a company"), ("입사", "joining a company; “entering a company”"), ("현장", "the site; the scene"), ("현재", "the present")]
_ANT7 = [("최소", "최대", "the smallest ↔ the largest"), ("퇴직", "취직", "retirement ↔ getting a job"), ("현재", "과거", "the present ↔ the past"), ("입사", "퇴사", "joining a company ↔ leaving a company")]
_SIM7 = [("급여", "보수", "salary ≈ pay; remuneration"), ("현장", "현지", "the site ≈ the local place"), ("취직", "취업", "getting a job ≈ finding employment"), ("사원", "직원", "an employee ≈ a staff member"), ("회사", "직장", "a company ≈ a workplace")]
_BOX7 = [("현찰, 수표, 현금", "돈", "cash, a check, money: money"), ("잡지사, 항공사, 여행사", "회사", "a magazine company, an airline, a travel agency: a company"), ("운전기사, 변호사, 소방관", "직업", "a driver, a lawyer, a firefighter: an occupation")]
_L7X = [("최대", "the largest; the maximum"), ("최단", "the shortest"), ("최저", "the lowest; the minimum"), ("이직", "changing jobs"), ("구직", "looking for a job"), ("취직", "getting a job"), ("현대", "modern times"), ("현지", "the local place"), ("과거", "the past"), ("퇴사", "leaving a company"), ("사내", "inside a company"), ("신입사원", "a new employee"), ("보수", "pay; remuneration"), ("지급", "payment"), ("현실", "reality"), ("현상", "a phenomenon"), ("취업", "finding employment"), ("실직", "losing one’s job"), ("사원", "an employee"), ("사장", "a company president"), ("직원", "a staff member"), ("재직", "being employed"), ("직장", "a workplace"), ("사회", "society"), ("현찰", "cash"), ("수표", "a check"), ("현금", "cash"), ("잡지사", "a magazine company"), ("항공사", "an airline"), ("여행사", "a travel agency"), ("운전기사", "a driver"), ("변호사", "a lawyer"), ("소방관", "a firefighter"), ("최악", "the worst")]
L1 = lesson(
    "U15 L7 · Review: news and work words and Sino-Korean 職 最 給 社 現",
    "세계뉴스 · 단어 복습 · 한자어 복습 · 상품권 · 박람회 · 취업 · 급여 · 職 最 給 社 現",
    requires=[],
    cards=[
        card("단어 복습 1: the meanings (the book’s matching)", "The book asks you to connect the words that have the same meaning (the first, 상품권, is done for you). The pairs:", tables=[ktable(_W7)]),
        card("단어 복습 2: words that go together (my pairs)",
             "The book asks you to connect the words that can be used together (the left column: 취업이, 급여가, 우울증에, 대학에, 소지품을, 쓰레기를, 우승을; the right column: 낮다, 시달리다, 잃어버리다, 어렵다, 진학하다, 차지하다, 재활용하다). My pairs (the English is mine):",
             examples=passage(_C7)),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ7], say=[2]), ktable(_HJW7)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word whose meaning is the opposite of the word on the left (A. 최소: 최대, 최단, 최저; B. 퇴직: 이직, 구직, 취직; C. 현재: 현대, 현지, 과거; D. 입사: 퇴사, 사내, 신입사원).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [[a, b, c] for a, b, c in _ANT7], say=[0, 1])]),
        card("한자어 복습 2: the most similar word (my answers)", "Circle the word closest in meaning to the word on the left (A. 급여: 보수, 지급, 급식; B. 현장: 현실, 현지, 현상; C. 취직: 직업, 실직, 취업; D. 사원: 사장, 직원, 재직; E. 회사: 직장, 사회, 현실).", tables=[table(["Word", "Similar word (my answer)", "Meaning"], [[a, b, c] for a, b, c in _SIM7], say=[0, 1])]),
        card("한자어 복습 3: the word that includes all three (my answers)", "Choose from the box (회사, 최악, 직업, 돈) the word that can include all three words:", tables=[table(["The three words", "The word from the box (my answer)", "Meaning"], [[a, b, c] for a, b, c in _BOX7], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L7X)]),
    ],
    exercises=uniq(
        _tr(_W7, k=3) + _tr(_HJW7, k=3) + _tr(_L7X, k=3) + _tr(_C7, k=3)
        + [M("What does the syllable 職 (직) mean?", "job; position", ["the most", "give", "appear"], "직업."), M("What does the syllable 最 (최) mean?", "the most; the -est", ["job", "give", "gather"], "최소."), M("What does the syllable 給 (급) mean?", "give; provide", ["job", "the most", "appear"], "급여."), M("What does the syllable 社 (사) mean?", "gather; meeting", ["job", "give", "appear"], "회사."), M("What does the syllable 現 (현) mean?", "appear; current", ["job", "the most", "give"], "현재."),
           M("Which word is the opposite of 최소?", "최대", ["최단", "최저", "최장"], "Largest."), M("Which word is the opposite of 퇴직?", "취직", ["이직", "구직", "직업"], "Getting a job."), M("Which word is the opposite of 현재?", "과거", ["현대", "현지", "현장"], "The past."), M("Which word is the opposite of 입사?", "퇴사", ["사내", "신입사원", "회사"], "Leaving a company."), M("Which word is similar to 급여?", "보수", ["지급", "급식", "급수"], "Pay."), M("Which word is similar to 현장?", "현지", ["현실", "현상", "현재"], "The local place."), M("Which word is similar to 취직?", "취업", ["직업", "실직", "퇴직"], "Finding employment."), M("Which word is similar to 사원?", "직원", ["사장", "재직", "회사"], "Staff."), M("Which word is similar to 회사?", "직장", ["사회", "현실", "현장"], "Workplace."),
           M("Which word includes 현찰, 수표, 현금?", "돈", ["회사", "최악", "직업"], "Money."), M("Which word includes 잡지사, 항공사, 여행사?", "회사", ["돈", "최악", "직업"], "Company."), M("Which word includes 운전기사, 변호사, 소방관?", "직업", ["돈", "회사", "최악"], "Occupation."),
           F("취업이 ___. (it is hard)", "어렵다", ["낮다", "시달리다"], "취업이 어렵다."), F("급여가 ___. (it is low)", "낮다", ["어렵다", "차지하다"], "급여가 낮다."), F("우울증에 ___. (to suffer)", "시달리다", ["진학하다", "재활용하다"], "우울증에 시달리다."), F("대학에 ___. (to go on)", "진학하다", ["차지하다", "잃어버리다"], "대학에 진학하다."), F("소지품을 ___. (to lose)", "잃어버리다", ["재활용하다", "진학하다"], "소지품을 잃어버리다."), F("쓰레기를 ___. (to recycle)", "재활용하다", ["차지하다", "시달리다"], "쓰레기를 재활용하다."), F("우승을 ___. (to win)", "차지하다", ["낮다", "어렵다"], "우승을 차지하다."),
           read_q("취업이 어렵습니다"), read_q("급여가 낮습니다"), read_q("우울증에 시달립니다"), read_q("대학에 진학합니다"), read_q("우승을 차지했습니다"), read_q("쓰레기를 재활용합니다")]
    ),
)

# ================================================================== L2 Part 1
_HAP = [("영국 케임브리지대 연구팀이 유럽 열다섯 개 국의 국민을 대상으로 행복감을 느끼는 정도를 질문한 결과, 덴마크 국민이 자신의 삶에 가장 행복과 만족감을 느끼는 것으로 나타났다.", "A research team of the University of Cambridge in Britain asked the people of 15 European countries how happy they feel, and the result showed that the Danish people feel the most happiness and satisfaction in their lives.")]
_PLAY = [
    ("영국 런던에 이색 놀이터가 등장했다.", "An unusual playground has appeared in London, England."),
    ("지난 십팔 일 문을 연 이 곳은 민간단체 나이트브리지협회의 제안으로 만들어진 육십 세 이상 노인을 위한 놀이터다.", "This place, which opened on the 18th, is a “playground for seniors aged 60 and over” created at the suggestion of a private organization, the Knightsbridge Association."),
    ("하이드파크의 정원사들이 지키고 서서 호기심으로 들어가 보려던 젊은이들을 막았다.", "Hyde Park’s gardeners stood guard and stopped the young people who tried to go in out of curiosity."),
    ("공원 측은 “여기는 손자손녀들을 위한 곳이 아니라 노인들을 위한 곳”이라고 강조했다.", "The park side stressed, “This is not a place for grandchildren but a place for seniors.”"),
    ("중국과 유럽 몇 곳에 노인용 놀이터가 있기는 하지만 어린이 출입금지를 명시한 곳은 드물다.", "There are playgrounds for seniors in China and a few places in Europe, but places that specify a ban on children’s entry are rare."),
    ("이 프로젝트를 추진한 나이트브리지협회의 매들린 엘스던은 비비씨 등과의 인터뷰에서 “공원마다 어린이 놀이터가 있는데 나이든 이들을 위한 시설은 거의 없다”면서 “세계 여러 곳에서 문의가 쏟아지고 있다”고 말했다.", "Madeline Elsdon of the Knightsbridge Association, who pushed this project, said in interviews with the BBC and others, “Every park has a children’s playground, but there are almost no facilities for older people,” and, “Inquiries are pouring in from many places around the world.”"),
]
_SPEAK18 = [("지난 일 년 동안 미국을 제외한 세계 여러 나라의 뉴스 중 가장 기억에 남는 뉴스는 무엇입니까?", "Of the news from various countries of the world other than the United States in the past year, which news do you remember the most?"), ("두 개를 골라 반 친구들에게 이야기해 보세요.", "Choose two and tell your classmates.")]
L2 = lesson(
    "U15 L7 · Part 1 (도입 학습): world news, happiness in Europe, a playground for seniors",
    "도입 학습 · 세계뉴스 · 타임지 10대 뉴스 · 행복감 · 덴마크 · 노인 놀이터 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): Time magazine’s top 10 news stories of 2009",
             "The book shows the top 10 news stories of 2009 announced by the American Time magazine (© Kyunghyang) and asks which news is not included. The choices: A. Somali piracy and hijacking of ships; B. Barak Obama elected president; C. Great earthquake in China; D. Economic crisis in Russia. The list is a picture and is not in the text, so the answer cannot be given here."),
        card("학습활동 2 (Reading): overseas news on happiness",
             "Read the article and the chart and choose the statement that fits (© Kyunghyang). The article is the book’s with 15개 국 spelled out (열다섯 개 국). The English is mine.",
             examples=passage(_HAP)),
        card("학습활동 2: my answer",
             "The statements are: A. Males and females age 15 and above were surveyed. B. People from countries around the world were asked about their level of satisfaction with life. C. A college in Britain conducted the research. D. Survey results showed that people in Denmark were least satisfied with life.\n\nMy answer is C. The text says a research team of the University of Cambridge in Britain conducted it. A cannot be checked in the text (the chart may say), B is wrong (15 European countries, not the world) and D is wrong (the Danes were the most satisfied)."),
        card("학습활동 5 (Reading): a playground in Britain",
             "The following is news about a playground in Britain (Text and image © Kyunghyang). The text is the book’s with the numbers spelled out (18일 is 십팔 일; 60세 is 육십 세; BBC is 비비씨); the quotation marks ‘ ’ around 60세 이상 노인을 위한 놀이터 are removed. The English is mine.",
             examples=passage(_PLAY)),
        card("학습활동 5: the questions answered (mine)",
             "1. The true statement is C: only seniors 60 or older may enter this park (the association’s playground is “for seniors,” the gardeners stopped young people, and the park side stressed it is not a place for grandchildren). A is wrong (children are not allowed even with seniors), B is wrong (no rides for both generations) and D is wrong (the text only says that such playgrounds exist in China and Europe, not that this one was modeled after one).\n\n"
             "2. The underlined sentence is not visible in the text of the book; every sentence of the article is translated above."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK18)),
        card("Activities left out", "학습활동 3 (a YTN news report on an event in the Netherlands; you fill in a table of the event and the requirement for participation, and the event host and the purpose) and 학습활동 4 (a YTN news report on a free music concert; a table of the performer, audience and purpose of the concert, and an opening speech in Korean as the performer) are audio and speaking activities."),
    ],
    exercises=uniq(
        _tr(_PLAY, k=3) + _tr(_SPEAK18, k=2)
        + [M("Which university’s research team did the happiness survey?", "Cambridge University in Britain", ["Oxford University", "A Danish university", "Harvard"], "영국 케임브리지대."), M("How many European countries were surveyed?", "15", ["5", "50", "100"], "열다섯 개 국."), M("Which people felt the most satisfied?", "The Danes", ["The British", "The French", "The Germans"], "덴마크."),
           M("Who may enter the London playground?", "Only seniors aged 60 and over", ["Only children", "Everyone", "Grandchildren with grandparents"], "육십 세 이상 노인."), M("Who proposed the playground?", "A private organization, the Knightsbridge Association", ["The government", "A school", "A company"], "민간단체 나이트브리지협회."), M("Who stopped the young people at the entrance?", "Hyde Park’s gardeners", ["Police officers", "The children", "Reporters"], "정원사들."), M("What is rare in other senior playgrounds?", "Specifying a ban on children’s entry", ["Slides", "Trees", "Benches"], "어린이 출입금지를 명시한 곳은 드물다."), M("What did Madeline Elsdon say about parks?", "Every park has a children’s playground but there are almost no facilities for older people", ["Parks are too big", "Playgrounds are too expensive", "Seniors do not like parks"], "인터뷰."),
           F("영국 런던에 ___ 놀이터가 등장했다. (unusual)", "이색", ["이상", "일상"], "이색."), F("공원 측은 여기는 노인들을 위한 곳이라고 ___했다. (stressed)", "강조", ["명시", "제안"], "강조하다."), F("어린이 출입금지를 ___한 곳은 드물다. (specify)", "명시", ["강조", "제안"], "명시하다."), F("세계 여러 곳에서 문의가 ___ 있다. (pouring in)", "쏟아지고", ["드물고", "막고"], "쏟아지다."),
           read_q("영국 런던에 이색 놀이터가 등장했습니다"), read_q("육십 세 이상 노인을 위한 놀이터입니다"), read_q("어린이 출입금지를 명시한 곳은 드뭅니다"), read_q("덴마크 국민이 가장 행복합니다"), read_q("가장 기억에 남는 뉴스는 무엇입니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("강타하다", "(强打) to hit hard; to strike", "이천오 년 허리케인 카트리나가 미국 남동부를 강타했습니다."),
        ("글로벌", "global", "글로벌 경제 위기로 전 세계가 어려움을 겪고 있습니다."),
        ("테러", "terror; terrorism", "요즘 사이버 테러가 심각한 사회 문제가 되고 있습니다."),
        ("파동", "(波動) waves; fluctuation; a crisis; a shock; “wave movement”", "경제 파동 이후 실업자가 늘었어요."),
        ("후퇴(하다)", "(後退) retreat (to retreat; to go back)", "대한민국의 민주주의가 후퇴한다는 우려의 목소리가 높습니다."),
    ]),
    ("학습활동 2", [
        ("지수", "(指數) an index; “pointing number”", "최근 소비자 물가 지수가 너무 올랐어요."),
        ("상위", "(上位) high rank", "시험 성적이 상위 이십 퍼센트인 학생은 장학금을 받아요.", "하위"),
    ]),
    ("학습활동 3", [
        ("나서다", "to step in (for an action); step forward; to take action", "시민단체들이 수재민 돕기에 나섰습니다."),
        ("부상", "(副賞) a supplementary prize; an extra prize", "대회에서 일 등 하신 분께는 자동차를 부상으로 드립니다.", "상품 | 부상 (負傷) injury"),
        ("장려(하다/되다)", "(奬勵) encouragement (to encourage/to be encouraged)", "투자를 장려하기 위해 제재를 완화하기로 했어요.", "격려하다"),
    ]),
    ("학습활동 4", [
        ("답례(하다)", "(答禮) a return courtesy; a return call (to return a salute, call, visit, or compliment)", "보내 주신 선물은 잘 받았습니다. 답례로 저녁 식사를 대접하고 싶어요."),
        ("지명(하다/되다)", "(指名) nomination; “pointing a name” (to nominate/to be nominated)", "저 배우가 연기상 후보로 지명됐습니다.", "선택 | 지명 (地名) a place name"),
    ]),
    ("학습활동 5", [
        ("명시(하다/되다)", "(明示) clear statement (to state; to specify/to be stated; to be specified)", "계약서에 명시된 대로 다음 달까지 물건을 다 주셔야 합니다.", "표시"),
        ("드물다", "to be rare; to be unusual", "오월에 눈이 오는 경우는 드뭅니다.", "흔하다"),
        ("표시(하다/되다)", "(標示) marking; an indication; an expression; a manifestation (to mark; to indicate/to be marked; to be indicated)", "제 질문에 예, 아니오 의사 표시를 확실히 해 주세요.", "명시"),
        ("협회", "(協會) a society; an association; a league", "테니스 선수 등록에 대한 질문이 있으면 테니스 협회에 전화하세요.", "단체"),
    ]),
]
L3 = lesson(
    "U15 L7 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 강타 · 글로벌 · 테러 · 파동 · 후퇴 · 지수 · 상위 · 나서다 · 부상 · 장려 · 답례 · 지명 · 명시 · 드물다 · 표시 · 협회",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 2005년 → 이천오 년; 20퍼센트 → 이십 퍼센트; 1등 → 일 등; 5월 → 오월.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=10, nread=10)),
)

# ================================================================== L4 Part 2 texts
_EVR = [
    ("등반객들이 버린 쓰레기로 오염된 세계 최고봉 에베레스트를 정화하기 위해 정상 등반 경험이 있는 네팔 셰르파들이 나서 팔천 미터 이상 고지대에 있는 쓰레기를 치우기로 했다.", "To purify Everest, the world’s highest peak, polluted by garbage discarded by climbers, Nepalese Sherpas with experience of climbing to the summit have stepped forward and decided to clear the garbage at high altitudes of 8,000 meters and above."),
    ("등반객들이 버린 쓰레기는 에베레스트를 오염시키는 주원인이었다.", "The garbage discarded by climbers was the main cause of polluting Everest."),
    ("이 때문에 네팔 정부는 모든 소지품과 쓰레기를 그대로 갖고 돌아오는 등반객들에게만 예치금을 돌려주는 정책을 실시하고 있다.", "For this reason, the Nepalese government is carrying out a policy of returning the deposit only to climbers who bring back all their belongings and garbage just as they are."),
    ("에베레스트에 있는 쓰레기의 양은 정확히 알 수 없으나, 과거 청소팀들이 수거해 온 쓰레기는 수 톤에 이른다.", "The amount of garbage on Everest cannot be known exactly, but the garbage that cleaning teams collected in the past amounts to several tons."),
]
_CHO = [
    ("매년 프랑스 파리에서 열리는 살롱 뒤 쇼콜라는 세계 초콜릿 생산농들이 모여 카카오 향을 뽐내는 잔치다.", "The Salon du Chocolat, held every year in Paris, France, is a feast where the world’s chocolate producers gather and show off the aroma of cacao."),
    ("지난해 시월 열린 이 행사에서 최고의 향기의 영예는 페루의 작은 마을에 돌아갔다.", "At this event held last October, the honor of the “best aroma” went to a small village in Peru."),
    ("안데스 산맥 줄기가 끝나고 아마존의 열대우림으로 이어지는 경계선에 위치한 페루 북부 산마르틴주의 토카체 마을에서 나온 원두가 대상을 차지한 것이다.", "The beans from the village of Tocache in San Martín state in northern Peru, located on the boundary line where the Andes mountain range ends and leads into the Amazon tropical rain forest, won the grand prize."),
    ("산마르틴은 불과 십 년 전만 해도 코카와 마약 밀매로 유명한 곳이었다.", "As recently as only ten years ago, San Martín was a place famous for coca and drug trafficking."),
    ("주민들은 코카인의 원료인 코카나무를 재배해 마약조직에 넘기며 연명했다.", "The residents survived by growing coca plants, the raw material of cocaine, and handing them over to drug organizations."),
    ("인구 이만 명의 토카체 마을도 마찬가지였다.", "The village of Tocache, with a population of 20,000, was the same."),
    ("정부는 미국과 유엔 등의 지원을 받아 코카와의 싸움에 들어갔다.", "The government, with support from the United States, the United Nations and others, entered a “fight against coca.”"),
    ("농민들이 먹고 살 길을 열어주는 것이 가장 중요했다.", "Opening the way for the farmers to make a living was the most important thing."),
    ("코카를 대체할 희망의 싹으로 떠오른 것이 카카오였다.", "What emerged as the sprout of hope to replace coca was cacao."),
    ("산마르틴 주정부는 카카오를 농가수입원으로 삼는 것을 넘어, 세계적인 특산지로 만들기 위해 발벗고 나섰다.", "The San Martín state government went beyond making cacao a source of farm income and rolled up its sleeves to make the area a world-class specialty-product region."),
]
_SPEAK19 = [("제대 후 갖고 싶은 직업은 무엇입니까?", "What job do you want to have after being discharged from the military?"), ("그 직업의 어떤 점이 좋습니까?", "What is good about that job?")]
L4 = lesson(
    "U15 L7 · Part 2 (본 학습): Everest garbage and Peruvian cacao",
    "본 학습 · 에베레스트 · 셰르파 · 예치금 · 살롱 뒤 쇼콜라 · 카카오 · 코카 · 페루 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): Nepal and Mount Everest",
             "The following article is related to Nepal; the book asks you to read it and do the tasks in English (Text and image © Kyunghyang, © Yonhapnews). The text is the book’s with 8000 m spelled out (팔천 미터). The English is mine.",
             examples=passage(_EVR)),
        card("학습활동 1: the questions answered (mine)",
             "1. The Nepalese government’s policy: it gives the deposit back only to climbers who bring back all their belongings and garbage as they are. The ground for it: the garbage that climbers discard was the main cause of polluting Everest.\n\n"
             "2. The Sherpas’ plan: Nepalese Sherpas who have climbed to the summit will step forward to clear the garbage lying at high altitudes of 8,000 meters and above, in order to purify Everest."),
        card("학습활동 3 (Reading): the Salon du Chocolat and Peru",
             "The following newspaper article is news about an event held in France (Text and image © Kyunghyang). The text is the book’s with the numbers spelled out (10월 is 시월; 10년 is 십 년; 2만 명 is 이만 명); the quotation marks ‘ ’ are removed. The English is mine.",
             examples=passage(_CHO)),
        card("학습활동 3: the questions answered (mine)",
             "1. The town is Tocache (토카체) in San Martín state in northern Peru. Geographically, it lies on the boundary line where the Andes mountain range ends and leads into the Amazon tropical rain forest.\n\n"
             "2. Ten years ago the state was famous for coca and drug trafficking, and the residents survived by growing coca plants and handing them to drug organizations. Now it is known for cacao: its beans won the grand prize at the Salon du Chocolat, and the state government is working to make it a world-class specialty-product region.\n\n"
             "3. The underlined sentence is not visible in the text of the book; every sentence is translated above (the likely candidate is 코카를 대체할 희망의 싹으로 떠오른 것이 카카오였다: “What emerged as the sprout of hope to replace coca was cacao.”)."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK19)),
        card("Activities left out", "학습활동 2 (a KBS news report on a dormitory of a university in France; you identify its feature and write a letter in English convincing a Korean friend that your dormitory would be a good fit) and 학습활동 4 (a YTN video on the restaurant business in Britain: a summary choice, how British eating habits have changed since the 1970s and why, two reasons it is difficult to find a curry chef, the demand of the Bangladesh Cooking Association to its government, and a transcription and translation of one sentence) are audio, video and writing activities."),
    ],
    exercises=uniq(
        _tr(_EVR, k=3) + _tr(_CHO, k=3)
        + [M("Who will clear the garbage on Everest?", "Nepalese Sherpas with summit experience", ["Foreign tourists", "The army", "Children"], "셰르파."), M("From what altitude will they clear the garbage?", "8,000 meters and above", ["300 meters", "1,000 meters", "Sea level"], "팔천 미터 이상."), M("What is the main cause of Everest’s pollution?", "Garbage discarded by climbers", ["Volcanoes", "Rain", "Local factories"], "등반객들이 버린 쓰레기."), M("Who gets the deposit back?", "Climbers who bring back all their belongings and garbage", ["All climbers", "Only Sherpas", "Only foreigners"], "예치금."), M("How much garbage have past cleaning teams collected?", "Several tons", ["A few kilograms", "None", "Exactly 100 tons"], "수 톤."),
           M("Where is the Salon du Chocolat held?", "Paris, France", ["Lima, Peru", "Seoul", "London"], "프랑스 파리."), M("Which village’s beans won the grand prize?", "Tocache in northern Peru", ["Paris", "Lima", "Cusco"], "토카체."), M("What was San Martín famous for ten years ago?", "Coca and drug trafficking", ["Cacao", "Gold", "Tourism"], "코카와 마약 밀매."), M("What is the raw material of cocaine?", "The coca plant", ["Cacao", "Corn", "Rice"], "코카나무."), M("What emerged as the hope to replace coca?", "Cacao", ["Coffee", "Corn", "Tea"], "카카오."), M("What did the government do with the support of the U.S. and the U.N.?", "Began a fight against coca", ["Banned cacao", "Moved the village", "Closed the border"], "코카와의 싸움."), M("What was the most important thing for the farmers?", "Opening the way to make a living", ["Winning a prize", "Moving to Paris", "Growing coca"], "먹고 살 길."),
           F("에베레스트를 ___하기 위해 셰르파들이 나섰다. (to purify)", "정화", ["오염", "후퇴"], "정화하다."), F("돌아오는 등반객들에게만 ___을 돌려준다. (the deposit)", "예치금", ["상품권", "부상"], "예치금."), F("쓰레기의 양은 수 톤에 ___. (amounts to)", "이른다", ["나선다", "돌아간다"], "이르다."), F("최고의 향기의 영예는 페루의 작은 마을에 ___. (went to)", "돌아갔다", ["이르렀다", "나섰다"], "돌아가다."), F("주민들은 코카나무를 재배해 넘기며 ___했다. (barely survived)", "연명", ["답례", "지명"], "연명하다."), F("카카오를 세계적인 특산지로 만들기 위해 ___ 나섰다. (rolled up their sleeves)", "발벗고", ["불과", "번번이"], "발벗고 나서다."),
           read_q("등반객들이 버린 쓰레기가 에베레스트를 오염시켰습니다"), read_q("예치금을 돌려주는 정책을 실시하고 있습니다"), read_q("토카체 마을의 원두가 대상을 차지했습니다"), read_q("코카를 대체할 희망의 싹은 카카오였습니다"), read_q("제대 후 갖고 싶은 직업은 무엇입니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("예치금", "(預置金) deposit money", "이 계좌의 최소 예치금이 얼마입니까?", "보증금"),
        ("이르다", "to reach; to get to; to amount to; to run up", "빚이 삼억에 이릅니다."),
        ("정화(하다/되다)", "(淨化) purification (to purify/to be purified)", "정부는 사회를 정화하기 위해 범죄와의 전쟁을 선포했습니다.", "청소"),
        ("지대", "(地帶) a zone; an area; a region; a belt", "사각지대, 무풍지대, 안전지대"),
    ]),
    ("학습활동 2", [
        ("개조(하다/되다)", "(改造) remodeling; “fixing and building” (to remodel/to be remodeled)", "차고를 개조하면 방으로 쓸 수 있을 것 같아요."),
        ("등장(하다)", "(登場) appearance (to appear)", "인터넷의 등장으로 삶이 편해졌습니다. 톰 크루즈가 이 영화에 등장합니다."),
        ("불과", "(不過) only; just", "기차역은 여기에서 불과 삼 분이면 갈 수 있어요.", "겨우"),
        ("실용적", "(實用的) practical", "기름값이 비쌀 때는 소형차가 실용적입니다."),
        ("주거(하다)", "(住居) dwelling; a residence; living (to reside; to live)", "여기는 주거 환경이 좋아서 인기가 많아요.", "거주, 집"),
    ]),
    ("학습활동 3", [
        ("경계(선)", "(境界線) a boundary (line)", "여기가 전라남도와 전라북도의 경계선입니다."),
        ("대상", "(大賞) a grand prize; “big award”", "저는 이번 대회에서 꼭 대상을 받고 싶어요.", "시상식, 상금 | 대상 (對象) object; target"),
        ("돌아가다", "to result in; to end in; to go to; “to turn around and go”", "최고의 선수상은 김인식 선수에게 돌아갔습니다."),
        ("먹고 살 길을 열어주다", "to open the way for someone to make a living", ""),
        ("밀매(하다/되다)", "(密賣) buy and sell in secret; illegal trade (to traffic/to be traded illegally)", "이 모 씨는 마약을 밀매한 혐의로 체포되었습니다.", "밀수, 비밀"),
        ("발벗고 나서다", "to roll up one’s sleeves (to fully or seriously engage in an action, a cause, etc.); “to step forward with bare feet”", "그분이 제가 어려울 때 발벗고 나서서 도와주셨어요."),
        ("뽐내다", "to boast; to brag; to show off", "자동차를 새로 사서 친구들한테 뽐내고 싶어요."),
        ("연명(하다)", "(延命) maintenance of a scanty existence; barely managing to live; “dragging one’s life” (to subsist; to survive; to make ends meet; to barely manage to live)", "많은 아프리카 주민들이 보조식량으로 연명하고 있어요.", "생활, 가난"),
        ("열대우림", "(熱帶雨林) a tropical rain forest; “heat zone rain forest”", "", "아열대, 온대, 한대"),
        ("영예", "(榮譽) glory; honor", "제 친구가 대상의 영예를 안았어요.", "명예"),
        ("특산지", "(特産地) the place where a special product is produced; “special product place”", "충청남도 금산은 인삼 특산지입니다.", "특산물"),
        ("향", "(香) a scent; a fragrance", "이 음식은 향이 아주 특이합니다.", "냄새"),
    ]),
    ("학습활동 4", [
        ("고등교육", "(高等敎育) higher education", "고등교육을 받은 사람들의 인구가 급증했습니다.", "중등교육, 초등교육, 학력, 학위, 대학교"),
        ("꺼리다", "to keep (a person or thing) at a distance; to shy off; to shun; to avoid", "요즘 젊은 사람들은 힘든 일을 꺼립니다."),
        ("요식업", "(料食業) restaurant business; food-service industry", "저희 아버지는 십 년째 요식업에 종사하고 계십니다.", "식당, 음식점"),
        ("인건비", "(人件費) labor costs; personnel expenses", "인건비를 줄이기 위해 종업원을 모두 해고했어요.", "근로자, 노동, 비용"),
        ("전향적", "(前向的) progressive; forward-looking", "새로 발표된 정책은 전향적입니다.", "진보적"),
        ("카레", "curry", ""),
    ]),
]
L5 = lesson(
    "U15 L7 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 예치금 · 정화 · 지대 · 개조 · 등장 · 불과 · 실용적 · 주거 · 경계 · 대상 · 밀매 · 연명 · 특산지 · 요식업 · 인건비",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 3억 → 삼억; 3분 → 삼 분; 10년째 → 십 년째. In the book the examples of 지대 are the three words 사각지대, 무풍지대 and 안전지대.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3 text
_HIK = [
    ("최근 일본에서 심심찮게 등장하는 단어 중의 하나가 히키코모리이다.", "One of the words that appear quite often in Japan recently is “hikikomori.”"),
    ("히키코모리는 (방안에) 틀어박히다라는 뜻인 히키코모루의 명사형이다.", "Hikikomori is the noun form of “hikikomoru,” which means “to shut oneself up (in a room).”"),
    ("일체의 사회적인 관계를 거부하고 방안이나 집에서 거의 나오지 않고 지내는 사람들을 지칭한다.", "It refers to people who refuse all social relationships and live hardly ever coming out of their room or house."),
    ("이들은 다른 사람과 대화하지 않고, 낮에는 자고 밤에 일어나 티브이나 비디오를 보며 인터넷에 탐닉하는 행태를 보인다.", "They do not talk with other people, sleep during the day, get up at night and show a pattern of watching TV or videos and indulging in the Internet."),
    ("누구나 한 번쯤은 해 봤을법한 행동이지만 문제는 지속 기간이다.", "It is behavior that anyone might have tried once, but the problem is the duration."),
    ("일본 후생성은 이천일 년 오 월 그 기준을 육 개월 이상이라고 제시했다.", "In May 2001, Japan’s Ministry of Health and Welfare presented the standard as “six months or more.”"),
    ("길게는 삼 년에서 사 년, 심하면 십 년 이상을 방안에서 지내는 사람들도 있다.", "There are people who spend as long as three to four years, or in severe cases more than ten years, in their room."),
    ("자청해서 은둔형 외톨이가 된다는 것도 특징이다.", "It is also a characteristic that they become “reclusive loners” of their own accord."),
    ("히키코모리는 천구백칠십 년대에 처음 등장했다.", "Hikikomori first appeared in the 1970s."),
    ("당시 입시에 시달리던 학생들이 무단결석하고 낮에는 집안에 있다가 밤이 되면 외출하는 현상이 빈발했다.", "At that time, the phenomenon of students suffering from entrance exams skipping school without permission, staying at home during the day and going out at night occurred frequently."),
    ("대부분의 학자들은 이를 두고 일부 불량청소년들의 단순한 등교거부쯤으로 해석했다.", "Most scholars interpreted this as the simple “school refusal” of some delinquent youths."),
    ("그러다 구십 년대 중반부터는 학생들이 밤에 거리로 나와 행인을 폭행, 살인하는 등 점차 과격한 행동을 보였다.", "Then from the mid-1990s, students came out onto the streets at night and showed increasingly violent behavior, such as assaulting and killing passers-by."),
    ("비슷한 시기, 은둔하는 성인들도 나타나면서 히키코모리는 사회문제로 비화했다.", "At about the same time, reclusive adults also appeared, and hikikomori developed into a social problem."),
    ("일본경제가 침체의 늪에 빠져들기 시작한 무렵이다.", "This was around the time Japan’s economy began to sink into the swamp of stagnation."),
    ("갑자기 일자리를 잃거나 취업전선에서 낙방한 젊은이들이 자신의 처지를 비관해 사회생활을 거부한 채 아예 집안으로 잠적해 버렸다.", "Young people who suddenly lost their jobs or failed in the job-hunting front became pessimistic about their own situation and disappeared altogether into their homes, refusing social life."),
    ("히키코모리는 지난해 현재 대략 백이십만 명으로 추산되고 있다.", "As of last year, hikikomori are estimated at roughly 1.2 million."),
    ("일본 인구 (일억 이천만 명) 의 일 퍼센트에 해당하는 수치다.", "This is a figure equivalent to 1 percent of Japan’s population (120 million)."),
    ("일본에서 특히 우려하는 점은 이 중에서 왕성한 사회활동을 해야 할 삼십 대의 비율이 삼십 퍼센트에 이르는 데다 대부분 남성들이라는 것.", "What is especially worrying in Japan is that, among them, those in their thirties, who should be active in society, make up as much as 30 percent, and that most of them are men."),
    ("이들은 외부와 단절된 자기만의 공간에서 오래 생활하다 보니 광장공포증, 햇빛혐오증, 우울증, 현기증 등에 시달리는 것으로 알려지고 있다.", "Having lived for a long time in a space of their own cut off from the outside, they are known to suffer from agoraphobia, an aversion to sunlight, depression, dizziness and so on."),
]
_SPEAK20 = [("미국 신세대의 특징에 대해 말해 보세요.", "Tell about the characteristics of the new generation in the United States."), ("그리고 구세대와 다른 점도 말해 보세요.", "And also tell how they differ from the older generation.")]
_TB7 = [("1970s", "Students suffering from entrance exams skipped school, stayed at home by day and went out at night; most scholars read it as simple school refusal by some delinquent youths."), ("After the mid-1990s", "Students came out at night and grew more violent (assaulting and killing passers-by); reclusive adults also appeared, and it became a social problem as Japan’s economy stagnated and young people who lost jobs or failed in job hunting shut themselves in.")]
L6 = lesson(
    "U15 L7 · Part 3 (심화 학습): 히키코모리 in Japan",
    "심화 학습 · 히키코모리 · 은둔형 외톨이 · 일본 · 사회현상 · 심심찮게 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): the social phenomenon of 히키코모리 in Japan",
             "The following article is about a social phenomenon that has become a serious problem in Japan (© Kyunghyang). The text is the book’s with the numbers and abbreviations spelled out (TV is 티브이; 2001년 5월 is 이천일 년 오 월; 6개월 is 육 개월; 3~4년 is 삼 년에서 사 년; 10년 is 십 년; 1970년대 is 천구백칠십 년대; 90년대 is 구십 년대; 1백20만 명 is 백이십만 명; 1억 2천만 명 is 일억 이천만 명; 1% is 일 퍼센트; 30대 is 삼십 대; 30% is 삼십 퍼센트); the Japanese ひきこもり after 히키코모리 is dropped, the quotation marks ‘ ’ are removed, the dot in 폭행•살인 and the dots in 광장공포증•햇빛혐오증•우울증•현기증 are replaced by commas. The English is mine.",
             examples=passage(_HIK)),
        card("학습활동 1: the questions answered (mine)",
             "1. The sentence that defines 히키코모리: 일체의 사회적인 관계를 거부하고 방안이나 집에서 거의 나오지 않고 지내는 사람들을 지칭한다. (It refers to people who refuse all social relationships and live hardly ever coming out of their room or house.)\n\n"
             "2. Comparison of 1970s and after the mid-1990s: see the table below.\n\n"
             "3. The concerns in the last paragraph: about 1.2 million people (1% of Japan’s population) are hikikomori; about 30% of them are in their thirties, the age when they should be socially active, and most are men; and because they live a long time in a space cut off from the outside, they suffer from agoraphobia, an aversion to sunlight, depression and dizziness.\n\n"
             "4. The word that can replace 심심찮게 is B. 자주 (often).",
             tables=[table(["Period", "The phenomenon (my answer)"], [list(r) for r in _TB7])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK20)),
        card("Activities left out", "학습활동 2 (a YTN video on China’s young generation: what the “ant tribe” 개미족 is and why it was given the name, the daily difficulty of Mr. Ryu Jun, a summary of a segment and how the college entrance rate affects them) and 학습활동 3 (a YTN video on a new pension reform policy in France: the policy, the government’s reason, laborers’ reaction, a true statement about the 2006 demonstration and a comparison of older and younger people’s opinions) are audio and video activities."),
    ],
    exercises=uniq(
        _tr(_HIK, k=3)
        + [M("What is 히키코모리?", "A person who refuses social relationships and hardly leaves the room or house", ["A foreign tourist", "A new student", "A factory worker"], "일체의 사회적인 관계를 거부."), M("What is the standard the Ministry of Health and Welfare presented?", "Six months or more", ["One week", "Two years", "Ten days"], "육 개월 이상."), M("When did 히키코모리 first appear?", "The 1970s", ["The 1950s", "The 2000s", "The 1930s"], "천구백칠십 년대."), M("What was the 1970s phenomenon?", "Students under exam pressure stayed home by day and went out at night", ["Adults lost jobs", "Students became violent", "Workers went on strike"], "입시에 시달리던 학생들."), M("What changed from the mid-1990s?", "More violent behavior and reclusive adults appeared", ["The phenomenon disappeared", "Only girls joined", "Exams were abolished"], "점차 과격한 행동."), M("About how many hikikomori are there?", "About 1.2 million", ["About 12,000", "About 120 million", "About 1,000"], "백이십만 명."), M("What percent of the hikikomori are in their 30s?", "30 percent", ["1 percent", "60 percent", "10 percent"], "삼십 퍼센트."), M("Which is NOT a symptom listed?", "A broken leg", ["Agoraphobia", "Aversion to sunlight", "Depression"], "The listed symptoms."), M("Which word can replace 심심찮게?", "자주", ["별로", "가끔씩", "확실하게"], "B."),
           F("히키코모리는 (방안에) ___ 뜻인 히키코모루의 명사형이다. (to shut oneself up)", "틀어박히다는", ["드물다는", "빈발하다는"], "틀어박히다."), F("문제는 ___ 기간이다. (duration)", "지속", ["지명", "표시"], "지속."), F("그들은 인터넷에 ___하는 행태를 보인다. (indulge)", "탐닉", ["답례", "비관"], "탐닉하다."), F("일부 불량청소년들의 단순한 ___거부쯤으로 해석했다. (school refusal)", "등교", ["은둔", "단절"], "등교거부."), F("젊은이들이 자신의 ___를 비관해 집안으로 잠적했다. (situation)", "처지", ["시기", "전선"], "처지."), F("일본경제가 ___의 늪에 빠져들기 시작했다. (stagnation)", "침체", ["성장", "개혁"], "침체."),
           read_q("히키코모리는 방안에서 거의 나오지 않고 지내는 사람들입니다"), read_q("일본 후생성은 육 개월 이상이라고 제시했습니다"), read_q("히키코모리는 사회문제로 비화했습니다"), read_q("우울증과 현기증에 시달리는 것으로 알려지고 있습니다"), read_q("미국 신세대의 특징에 대해 말해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("단절(하다/되다)", "(斷絶) severing (of contact or a relationship); a cutoff (to cut off; to sever/to be cut off; to be severed)", "최근 들어 남북 교류가 단절되었습니다.", "끊다, 끊기다"),
        ("등교(하다)", "(登校) going to school (go to school)", "등굣길에 서점에 들러 책을 한 권 샀습니다.", "하교하다"),
        ("비관(하다)", "(悲觀) pessimism; “sad view” (to be pessimistic; to take a dark view)", "상황을 너무 비관하지 말고 좀 긍정적으로 생각해 봅시다.", "낙관하다"),
        ("빈발(하다)", "(頻發) frequent occurrence (to occur frequently)", "여기는 교통사고가 빈발하는 곳입니다."),
        ("시기", "(時期) a time; a period; a season", "구 월은 방학이 끝나고 개학을 하는 시기입니다."),
        ("외톨이", "a loner; a solitary person; “single nut”", "저는 학교에서 항상 외톨이였어요."),
        ("우려(하다/되다)", "(憂慮) a concern; a worry; an apprehension (to be concerned; to worry/to be worried; to be apprehensive)", "어제 내린 비로 출근길 교통사고가 우려됩니다."),
        ("은둔(하다)", "(隱遁) reclusion (to live reclusively)", "그 사람은 산에서 십 년 동안 은둔하며 지냈어요.", "숨다"),
        ("전선", "(前線) the front (line); a front", "지금 장마전선이 북상하고 있어요.", "전선 (電線) an electric wire"),
        ("지속(하다/되다)", "(持續) continuance (to last; to continue/to be continued)", "증상이 지속되면 꼭 의사와 상담하세요."),
        ("지칭(하다/되다)", "(指稱) a designation; a reference (to call; to designate; to refer to/to be called; to be designated; to be referred to)", "지금 그 말은 누구를 지칭하는 것입니까?"),
        ("처지", "(處地) a position; a circumstance", "지금 제 처지가 좋지 않습니다.", "상황"),
        ("탐닉(하다)", "(耽溺) indulgence (to indulge in)", "요즘 컴퓨터 게임에 탐닉하는 젊은 세대가 늘고 있습니다.", "중독"),
    ]),
    ("학습활동 2", [
        ("갈수록", "as time goes on; with the lapse of time", "한국말이 갈수록 더 쉬워집니다.", "점점"),
        ("개미", "an ant", ""),
        ("거처(하다)", "(居處) a residence; a place to live (to live; to dwell)", "다음달에 거처를 아파트로 옮길 예정입니다."),
        ("곤충", "(昆蟲) an insect; a bug", "", "벌레"),
        ("넉넉하다", "to be enough; to be sufficient", "음식이 넉넉하니까 와서 같이 먹어요.", "충분하다 | 부족하다"),
        ("넘쳐나다", "to overflow; to abound", "호텔마다 신혼부부로 넘쳐납니다."),
        ("만원", "(滿員) being filled to capacity; being overcrowded", "출퇴근 시간에 지하철이 만원입니다.", "만 원 (萬 元) 10,000 won"),
        ("별칭", "(別稱) a nickname; another name", "빅애플은 뉴욕의 별칭입니다.", "닉네임 | 별명"),
        ("열악하다", "(劣惡) to be inferior; to be coarse; to be poor; to be deteriorated", "이 지역은 대기환경이 열악합니다.", "나쁘다"),
        ("인파", "(人波) a crowd; “a wave of people”", "크리스마스 이브에는 거리가 인파로 넘쳐납니다."),
    ]),
    ("학습활동 3", [
        ("개혁(하다/되다)", "(改革) reform (to reform/to be reformed)", "정부는 선거제도를 개혁한다고 발표했습니다.", "개선"),
        ("납부(하다/되다)", "(納付) payment (of taxes, tuition, bills, etc.) (to pay/to be paid)", "공과금은 기간 내에 납부해야 합니다."),
        ("노동계", "(勞動界) the labor world", "노동법 개정에 대해 노동계의 반발이 심합니다.", "근로자, 파업"),
        ("번번이", "every time; all the time; always", "제 여자친구는 시간 약속을 번번이 어깁니다."),
        ("시도(하다/되다)", "(試圖) a trial; an attempt (to try; to attempt/to be attempted)", "개혁을 한 번 시도해 봅시다."),
        ("심상치 않다", "(尋常) to be unusual; to be extraordinary; to be uncommon; to be grave", "선원들의 불만이 심상치 않습니다.", "심상하다 | 특이하다"),
        ("특이하다", "(特異) to be unusual; to be peculiar; “to be specially different”", "이 제품은 디자인이 특이해서 인기가 많아요.", "평범하다 | 심상치 않다"),
        ("파업(하다)", "(罷業) strike; “closing one’s work” (to strike)", "현대자동차 노조가 파업을 벌이고 있습니다."),
        ("표출(하다/되다)", "(表出) an expression; a manifestation; a display; “surfacing” (to express; to show/to be expressed)", "사원들이 회사의 결정에 불만을 표출하고 있습니다.", "표현하다, 보이다"),
    ]),
]
L7 = lesson(
    "U15 L7 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 단절 · 비관 · 빈발 · 외톨이 · 우려 · 은둔 · 지속 · 탐닉 · 열악하다 · 인파 · 개혁 · 납부 · 노동계 · 파업 · 표출",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are spelled in Hangul here: 9월 → 구 월; 10년 → 십 년. The book writes the quotation marks ‘ ’ around 빅애플; they are removed. The line break inside 우려(하다/되다) and 지칭(하다/되다) is closed up.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=14, nread=14)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 7: World News (세계뉴스)", [L1, L2, L3, L4, L5, L6, L7])

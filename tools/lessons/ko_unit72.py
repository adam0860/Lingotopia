"""Unit 72: KBC Semester III, Unit 16, Lesson 7 - Name Brands and Lookism (명품선호와 외모지상주의).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 16, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_CAT7 = [("Tendency to overspend", "과시욕, 과소비, 사치, 명품"), ("Wedding", "혼수, 배우자, 예물, 청첩장"), ("Cosmetic surgery and the body", "복부, 미용성형, 쌍꺼풀, 주름살")]
_MATCH7 = [("축의금", "congratulatory money"), ("재혼", "second marriage"), ("애용", "using favorably"), ("가치관", "perspective on values"), ("부작용", "side effects"), ("의료분쟁", "a medical dispute"), ("사치", "luxury; extravagance"), ("상류층", "the upper class")]
_HJ7 = [("重 중", "heavy; weighty", "체중, 비중"), ("好 호", "like; be fond of; good", "선호, 호감"), ("價 가", "price; value", "가격, 물가"), ("美 미", "beauty", "미남, 미용실"), ("配 배", "distribute; mate", "분배, 배우자")]
_HJW7 = [("체중", "body weight"), ("비중", "relative importance"), ("선호", "preference"), ("호감", "a good feeling"), ("가격", "price"), ("물가", "price of commodities"), ("미남", "a handsome man"), ("미용실", "a beauty salon"), ("분배", "distribution; division"), ("배우자", "a spouse")]
_SIM7 = [("체중", "몸무게", "body weight: weight"), ("가격", "값", "price: price"), ("배우자", "남편이나 아내", "a spouse: a husband or wife"), ("선호", "호감", "preference: a good feeling"), ("미용실", "미장원", "a beauty salon: a hair salon")]
_REL7 = [("A", "외모", "성형, 미남, 미녀", "looks: plastic surgery, handsome man, beauty"), ("B", "선호", "호감, 호의, 호평", "preference: good feeling, goodwill, a good review"), ("C", "비중", "중압감, 중요성, 중시", "relative importance: pressure, importance, valuing")]
_L7X = [("과시욕", "a desire to show off"), ("복부", "the abdomen"), ("미용성형", "cosmetic surgery"), ("명품", "a luxury brand; a name-brand item"), ("혼수", "wedding articles; wedding expenses"), ("과소비", "overspending"), ("쌍꺼풀", "a double eyelid"), ("주름살", "wrinkles"), ("예물", "wedding gifts (exchanged by the couple)"), ("청첩장", "a wedding invitation"), ("신장", "height"), ("외모", "looks; appearance"), ("몸무게", "weight"), ("값", "price"), ("미장원", "a hair salon"), ("이발소", "a barbershop"), ("성형외과", "a plastic surgery clinic"), ("미백", "skin whitening"), ("성형", "plastic surgery"), ("미녀", "a beautiful woman"), ("호의", "goodwill; kindness"), ("호평", "a good review"), ("중압감", "a feeling of pressure"), ("중요성", "importance"), ("중시", "valuing; attaching importance to"), ("배려", "consideration")]
L1 = lesson(
    "U16 L7 · Review: overspending, weddings, looks and Sino-Korean 重 好 價 美 配",
    "명품선호와 외모지상주의 · 단어 복습 · 한자어 복습 · 과시욕 · 과소비 · 혼수 · 예물 · 청첩장 · 쌍꺼풀 · 주름살 · 重 好 價 美 配",
    requires=[],
    cards=[
        card("단어 복습 1: sorting the words (my answers)", "Write each of the twelve words 과시욕, 복부, 미용성형, 명품, 혼수, 과소비, 배우자, 쌍꺼풀, 주름살, 사치, 예물 and 청첩장 in the right category (the book’s categories are Tendency to Overspend, Wedding, and Cosmetic Surgery and the Body):", tables=[table(["Category", "Words (my answers)"], [list(r) for r in _CAT7], say=[1])]),
        card("단어 복습 2: the meanings (the book’s matching)", "The book asks you to connect the word on the left with its meaning on the right. The pairs:", tables=[ktable(_MATCH7)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ7], say=[2]), ktable(_HJW7)]),
        card("한자어 복습 1: the closest word (my answers)", "Circle the word closest in meaning to the word on the left (A. 체중: 신장, 외모, 몸무게; B. 가격: 평가, 값, 물가; C. 배우자: 남편이나 아내, 남자와 여자, 연인; D. 선호: 외모, 호감, 미백; E. 미용실: 미장원, 이발소, 성형외과).", tables=[table(["Word", "Closest (my answer)", "Meaning"], [list(r) for r in _SIM7], say=[0, 1])]),
        card("한자어 복습 2: the related word (my answers)", "Choose from the box (선호, 비중, 외모, 배려) the word most related to the three words on the right; 배려 is left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Why"], [list(r) for r in _REL7], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L7X)]),
    ],
    exercises=uniq(
        _tr(_MATCH7, k=3) + _tr(_HJW7, k=3) + _tr(_L7X, k=3) + _tr([(a, c) for a, b, c in _SIM7], k=3)
        + [M("What does the syllable 重 (중) mean?", "heavy; weighty", ["price", "beauty", "like"], "체중."), M("What does the syllable 好 (호) mean?", "like; be fond of; good", ["heavy", "price", "beauty"], "선호."), M("What does the syllable 價 (가) mean?", "price; value", ["heavy", "beauty", "mate"], "가격."), M("What does the syllable 美 (미) mean?", "beauty", ["price", "heavy", "like"], "미남."), M("What does the syllable 配 (배) mean?", "distribute; mate", ["beauty", "price", "heavy"], "배우자."),
           M("Which word fits the category “Wedding”?", "청첩장", ["쌍꺼풀", "과소비", "주름살"], "A wedding invitation."), M("Which word fits “Tendency to Overspend”?", "과시욕", ["배우자", "복부", "예물"], "A desire to show off."), M("Which word fits “Cosmetic Surgery and the Body”?", "쌍꺼풀", ["혼수", "사치", "청첩장"], "A double eyelid."),
           M("Which word is closest to 체중?", "몸무게", ["신장", "외모", "연인"], "Weight."), M("Which word is closest to 미용실?", "미장원", ["이발소", "성형외과", "병원"], "A hair salon."), M("Which word fits 호감, 호의, 호평?", "선호", ["비중", "외모", "배려"], "Preference."), M("Which word fits 중압감, 중요성, 중시?", "비중", ["선호", "외모", "배려"], "Relative importance."),
           F("결혼식에서 ___을 냈습니다. (congratulatory money)", "축의금", ["청첩장", "예물"], "축의금."), F("성형수술의 ___ 때문에 고생했습니다. (side effects)", "부작용", ["가치관", "상류층"], "부작용."), F("그는 ___를 두 번째로 했습니다. (second marriage)", "재혼", ["이혼", "결혼식"], "재혼."), F("명품을 ___하는 사람이 많습니다. (to use favorably)", "애용", ["재혼", "분배"], "애용하다."),
           read_q("명품을 선호하는 사람이 많습니다"), read_q("과소비는 사회 문제입니다"), read_q("청첩장을 받았습니다"), read_q("체중이 늘어서 걱정입니다"), read_q("가치관이 다릅니다")]
    ),
)

# ================================================================== L2 Part 1
_TEST7 = [
    ("외모차별지수 자가 테스트", "(Heading) Self test of the appearance discrimination index"),
    ("친구들이나 주위 사람의 외모에 대해 평가를 하는 것은 관심과 애정의 표현이다.", "(1) Evaluating the looks of friends or people around you is an expression of interest and affection."),
    ("살이 찐 사람은 둔하고 게으르다고 생각한다.", "(2) I think people who are overweight are dull and lazy."),
    ("예쁜 사람이 공부도 잘하고 일도 잘한다.", "(3) Pretty people study well and also work well."),
    ("소개팅에서 상대방 외모가 마음에 안 들면 외모에 대해 말하는 편이다.", "(4) If I don’t like the other person’s looks on a blind date, I tend to talk about their looks."),
    ("미니스커트 같은 옷은 날씬한 여성만 입어야 한다.", "(5) Clothes like miniskirts should be worn only by slim women."),
    ("내가 부르는 친구의 별명 중 외모와 관련된 것이 있다.", "(6) Among the nicknames I call my friends, there are ones related to looks."),
    ("여학생은 교복 치마를 입어야 단정해 보인다.", "(7) Female students look neat only if they wear the school-uniform skirt."),
    ("입사지원서에 키, 몸무게 등을 기재하는 것은 당연하다.", "(8) It is natural to fill in height, weight and so on on a job application."),
    ("채용공고에 용모 단정한 자라고 명시하는 것은 당연하다.", "(9) It is natural to state “a person of neat appearance” in a hiring notice."),
    ("같은 조건이면 외모가 뛰어난 사람을 뽑는 게 당연하다.", "(10) Under the same conditions, it is natural to choose the person with outstanding looks."),
    ("뉴스 여성 앵커는 젊고 예뻐야 한다.", "(11) A female news anchor has to be young and pretty."),
    ("여성 정치인의 옷차림이나 외모 기사가 나오는 것은 당연하다.", "(12) It is natural for articles on a woman politician’s clothing or looks to come out."),
    ("외모가 뛰어난 사람이 물건을 팔면 더 관심이 간다.", "(13) If someone with outstanding looks sells an item, I become more interested."),
    ("티브이 오락 프로그램에서 연예인의 외모를 평가하거나 농담하는 것은 재미있다.", "(14) It is fun when TV entertainment programs evaluate or joke about entertainers’ looks."),
    ("티브이 드라마나 영화에서 못생긴 사람이 주연을 맡는 것은 참을 수 없다.", "(15) I can’t stand an ugly person playing the lead in a TV drama or film."),
    ("성형 부작용이나 무리한 다이어트의 책임은 사회적 영향보다는 개인의 욕심에 있다.", "(16) The responsibility for plastic surgery side effects or excessive dieting lies in individual greed rather than social influence."),
    ("영에서 세 개. 매우 높은 외모차별 감수성을 소유하셨군요.", "(0 to 3 statements) You possess a very high sensitivity to appearance discrimination."),
    ("네 개에서 여섯 개. 아쉽지만 그래도 훌륭합니다.", "(4 to 6) A pity, but still excellent."),
    ("일곱 개에서 열 개. 이미 외모차별에 물드셨군요.", "(7 to 10) You have already been tainted by appearance discrimination."),
    ("열한 개에서 열여섯 개. 외모로 모든 것은 판단하시는군요.", "(11 to 16) You judge everything by looks. (The book prints 것은, a slip for 것을.)"),
]
_POST7 = [
    ("전 매부리코라서 어릴 때부터 코주부라고 불렸습니다.", "(Q) Because I have a hooked nose, I have been called 코주부 since I was little."),
    ("좋아하는 별명은 아니었지만 그렇다고 성형수술을 생각해 본 적은 없었어요.", "It was not a nickname I liked, but even so I had never thought about plastic surgery."),
    ("그런데 얼마 전 회사 여직원들끼리 코 때문에 옷 입을 때 걸릴 것 같지 않니? 하는 자기들끼리 주고받는 농담을 우연히 들었습니다.", "But not long ago I happened to overhear a joke the women employees at the company were exchanging among themselves, “Wouldn’t it get in the way when putting on clothes because of the nose?”"),
    ("물론 웃자고 하는 소리라는 걸 알았지만 그 이후 여직원들 앞에서 신경 쓰이는 건 어쩔 수가 없더군요.", "Of course I knew it was said for a laugh, but after that I couldn’t help feeling self-conscious in front of the women employees."),
    ("이후 회식자리에서 취한 여직원 하나가 저 보고 코주부라고, 고등학교 이후로 한 번도 들어본 적이 없는 별명을 불렀고 모두들 웃었습니다.", "Later, at a company dinner, one drunk woman employee called me 코주부, a nickname I had not heard even once since high school, and everyone laughed."),
    ("그날 이후 성형을 결심했습니다.", "After that day I decided on plastic surgery."),
    ("제 여자친구도 처음엔 괜찮다고 하다가 제가 심각하게 고민하자 결국 병원도 알아봐 주고 날도 잡았습니다.", "My girlfriend too said at first it was fine, but when I worried seriously, in the end she even looked up a hospital for me and set a date."),
    ("그런데 뭐가 문제냐.", "But what’s the problem?"),
    ("막상 성형수술을 하려니 이번에는 남자가 성형수술을 했다고 놀릴 걸 생각하니 그것도 쉽지가 않네요.", "Now that I’m about to have the surgery, thinking that people will tease me for a man having had plastic surgery, that isn’t easy either."),
    ("남자가 성형수술 한다는 건 좀 웃기잖아요.", "A man having plastic surgery is a bit funny, isn’t it?"),
    ("더구나 바로 제가 성형수술 여부를 놓고 고민하는 당사자가 될 줄은 정말 몰랐거든요.", "Besides, I really didn’t know that I myself would become the person agonizing over whether to have plastic surgery."),
    ("제가 너무 소심한 걸까요?", "Am I being too timid?"),
    ("어떻게 해야 할까요?", "What should I do?"),
]
_REPLY7 = [("성형수술은 본인이 원하고 충분히 생각한 뒤에 결정하면 됩니다.", "You can decide on plastic surgery after you want it yourself and have thought enough."), ("다른 사람의 시선보다 본인의 마음이 더 중요합니다.", "Your own heart is more important than other people’s gaze."), ("요즘은 성형수술을 하는 남성도 많아서 크게 걱정하지 않아도 됩니다.", "These days many men also have plastic surgery, so you don’t need to worry so much.")]
_SPEAK7A = [("성형수술의 긍정적인 면과 부정적인 면에 대해 옆 친구와 이야기해 보세요.", "Talk with the friend next to you about the positive and negative sides of plastic surgery."), ("그리고 본인은 성형수술에 어떤 의견을 가지고 있는지도 말해 보세요.", "And also tell what opinion you yourself have about plastic surgery."), ("외모를 중시하는 외모지상주의가 사회적으로 미치는 영향에 대해 옆 친구와 이야기해 보세요.", "Talk with the friend next to you about the social effects of lookism, which values looks.")]
_SCORE7 = [("0–3 statements", "A very high sensitivity to appearance discrimination"), ("4–6 statements", "A pity, but still excellent"), ("7–10 statements", "Already tainted by appearance discrimination"), ("11–16 statements", "Judging everything by looks")]
L2 = lesson(
    "U16 L7 · Part 1 (도입 학습): the appearance discrimination test and a nose worry",
    "도입 학습 · 외모지상주의 · 외모차별지수 · 성형수술 · 별명 · 코주부 · 매부리코 · 신경이 쓰이다 · 날을 잡다 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 4 (Reading and Speaking): the appearance discrimination index self test",
             "The following is a self test for rating your own awareness of looks (text and image © Hankyoreh). The text is the book’s with the numbers spelled out (the book’s bullets are numbered 1 to 16 in the English only; 0~3개 → 영에서 세 개; 4~6개 → 네 개에서 여섯 개; 7~10개 → 일곱 개에서 열 개; 11~16개 → 열한 개에서 열여섯 개), TV written 티브이, the quotation marks around 용모 단정한 자 removed, and the colon after each score range written as a period. The English is mine.",
             examples=passage(_TEST7)),
        card("학습활동 4: the questions answered (mine)",
             "1. and 2. Circle the statements you agree with and count them: the answers depend on you. The interpretation by score is:",
             tables=[table(["Number of statements you agree with", "Interpretation (from the book’s criteria)"], [list(r) for r in _SCORE7])]),
        card("학습활동 5 (Reading, Writing and Speaking): a man’s worry about his looks on an online bulletin board",
             "The following is a worry about his looks posted by a man on an online bulletin board (© Hankyoreh). The text is the book’s with the quotation marks ‘ ’ removed; the question mark inside the joke is kept. The English is mine. The book leaves the answer (A:) blank.",
             examples=passage(_POST7)),
        card("학습활동 5: the questions answered (mine)",
             "1. His nickname was 코주부 (a person with a large nose; he has a hooked nose, 매부리코). It is given to a person with a big or prominent nose; an English equivalent is “Big Nose” or “Beaky”.\n\n"
             "2. The word 그날 refers to the day of the company dinner (회식), when a drunk woman employee called him 코주부, a nickname he had not heard since high school, and everyone laughed. After that day he decided on plastic surgery.\n\n"
             "3. C — the verb 걸리다 in 옷 입을 때 걸릴 것 같지 않니 means “to get caught on; to snag” (the nose would catch on the clothes), as in tripping on a stone (C). In A it means “to take (time)”, in B “to get caught (by the police)” and in D “to catch (a cold)”.\n\n"
             "4. 신경이 쓰이다 = to be bothered; to feel self-conscious; to care about it (literally, “the nerves are used”). 날을 잡다 = to set a date (literally, “to catch a day”).\n\n"
             "5. His two concerns: (1) that people will tease him for being a man who had plastic surgery; (2) whether he is being too timid, and what he should do (whether to go through with the surgery).\n\n"
             "6. A possible reply in Korean (mine), addressing his concerns:",
             examples=passage(_REPLY7)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK7A)),
        card("Activities left out", "학습활동 1 (Reading): two sets of pictures on Korean social problems (© Hankyoreh) where you tick the matching problem among 학벌중시 사회, 명품 선호, 외모 지상주의, 과소비 and 성형수술 부작용. 학습활동 2 (Reading, track 001): a YTN video on a social phenomenon that values looks, with three captions to translate and a summarizing sentence to choose (A. 요즘은 성형수술을 하는 남성들이 점점 증가하고 있다; B. 한국에는 많은 성형외과가 있고 성형수술 기술은 세계적인 수준에 이르렀다; C. 많은 여성들이 자기의 얼굴이나 몸에 대해 자신이 없어 하고 성형수술을 받고 싶어한다; D. 많은 여성들이 외모보다는 내면의 아름다움이 더 중요하다고 생각한다). 학습활동 3 (Listening, track 002): a conversation between two university students with a table of the woman’s plan and her reason. They are video, pictures and audio."),
    ],
    exercises=uniq(
        _tr(_TEST7, k=3) + _tr(_POST7, k=3) + _tr(_REPLY7, k=3) + _tr(_SPEAK7A, k=3)
        + [M("What is 외모차별지수 자가 테스트?", "A self test of one’s awareness of appearance discrimination", ["A school exam", "A medical test", "A job interview"], "The book’s test."), M("What was the man’s nickname?", "코주부", ["매부리", "얼짱", "몸짱"], "A person with a big nose."), M("Where did a drunk coworker call him by the nickname?", "At a company dinner", ["At a wedding", "At school", "At a hospital"], "회식자리."), M("What did he decide after that day?", "To have plastic surgery", ["To quit his job", "To move", "To go on a diet"], "성형을 결심했습니다."), M("Who looked up a hospital for him?", "His girlfriend", ["His mother", "His boss", "A coworker"], "여자친구."), M("What is his second worry?", "That people will tease a man who had plastic surgery", ["That surgery costs too much", "That he will lose his job", "That his girlfriend will leave"], "남자가 성형수술을 했다고 놀릴 걸."),
           M("What does 날을 잡다 mean?", "To set a date", ["To catch a fish", "To pick a fight", "To fix a clock"], "날을 잡다."), M("What does 신경이 쓰이다 mean?", "To be bothered; to feel self-conscious", ["To be angry", "To be hungry", "To be sleepy"], "신경이 쓰이다."), M("Which result means a very high sensitivity to appearance discrimination?", "0 to 3 statements", ["4 to 6 statements", "7 to 10 statements", "11 to 16 statements"], "영에서 세 개."),
           F("살이 찐 사람은 둔하고 ___고 생각한다. (lazy)", "게으르다", ["부지런하다", "예쁘다"], "게으르다."), F("전 ___라서 코주부라고 불렸습니다. (hooked nose)", "매부리코", ["쌍꺼풀", "주름살"], "매부리코."), F("제가 너무 ___ 걸까요? (timid)", "소심한", ["대범한", "게으른"], "소심하다."), F("사람을 외모만 보고 ___하지 마세요. (to judge)", "판단", ["기재", "소유"], "판단하다."), F("친구들의 외모를 평가하는 것은 관심과 ___의 표현이다. (affection)", "애정", ["욕심", "농담"], "애정.")]
        + [read_q("외모지상주의가 사회 문제가 되고 있습니다"), read_q("전 매부리코라서 코주부라고 불렸습니다"), read_q("성형을 결심했습니다"), read_q("성형수술에 대해 어떻게 생각합니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("학벌", "(學閥) one’s educational background", "학벌을 중시하는 사회 분위기는 바뀌어야 한다고 생각합니다.", "학력"),
    ]),
    ("학습활동 2", [
        ("내면", "(內面) the inner aspect (of a person); one’s mind; “inner face”", "요즘은 내면보다 외모를 더 중요하게 여기는 추세이다.", "마음"),
    ]),
    ("학습활동 4", [
        ("감수성", "(感受性) sensitivity; sensibility", "십 대 소녀들은 감수성이 예민합니다."),
        ("게으르다", "to be lazy", "우리 아이가 너무 게을러서 걱정이에요.", "부지런하다"),
        ("기재(하다)", "(記載) filling in (forms) (to fill in)", "신청서에 이름과 주소를 기재하세요.", "기입하다"),
        ("농담(하다)", "(弄談) a joke (to make a joke)", "그 친구는 농담을 잘해서 만나면 재미있어요.", "장난"),
        ("둔하다", "(鈍) to be slow; to be obtuse; to be dull", "제 친구는 너무 둔해서 항상 자세히 설명해 줘야 합니다."),
        ("물들다", "to be influenced; to be tainted; “to be colored” (one’s viewpoint/opinion)", "청소년들은 외국 문화에 쉽게 물든다.", "영향을 받다"),
        ("소유(하다)", "(所有) ownership; possession (to own; to possess)", "이 집은 제 소유로 되어 있습니다.", "가지다"),
        ("애정", "(愛情) love; affection", "마이클 씨는 한국에 대한 애정이 깊습니다.", "사랑"),
        ("욕심", "(慾心) greed; avarice", "욕심이 과하면 화를 부릅니다."),
        ("판단(하다)", "(判斷) judgment; decision (to judge; to decide)", "사람을 외모만 보고 판단하지 마세요."),
    ]),
    ("학습활동 5", [
        ("매부리코", "a hooked nose; an aquiline nose; “hawk’s beak nose”", ""),
        ("별명", "(別名) a nickname", "저는 얼굴이 특이해서 친구들이 저한테 별명을 많이 지어 줬어요.", "성명, 이름, 필명"),
        ("소심하다", "(小心) to be timid; to be diffident; “to have small heart”", "저는 너무 소심해서 친구들이 많지 않습니다.", "대범하다"),
        ("코주부", "a person with a large nose", "저는 코가 커서 코주부라고 놀림을 많이 받았어요."),
    ]),
]
L3 = lesson(
    "U16 L7 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 학벌 · 내면 · 감수성 · 게으르다 · 기재 · 농담 · 둔하다 · 물들다 · 소유 · 애정 · 욕심 · 판단 · 매부리코 · 별명 · 소심하다 · 코주부",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 감수성 has 10대 (written 십 대 here). The book prints the related words of 별명 as 성명, 이름, 필명.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=8, nread=7)),
)

# ================================================================== L4 Part 2
_TIPS7 = [
    ("청첩장은 식후 알림장으로 대신한다.", "(Tip 1) Replace the wedding invitation with a notice sent after the ceremony."),
    ("청첩장 고지 남용은 경제적, 정신적 부담요인.", "Overuse of wedding invitation notices is a source of economic and mental burden."),
    ("상부상조의 취지를 벗어나 축재와 신분과시 수단이 된 경조비 관행을 근절한다.", "(Tip 2) Root out the practice of congratulation and condolence money that has strayed from the purpose of mutual aid and become a means of accumulating wealth and showing off status."),
    ("피로연은 가족모임으로 대신한다.", "(Tip 3) Replace the reception with a family gathering."),
    ("예물은 간단한 증표로, 예복은 예식 후 활용 가능한 것으로 마련한다.", "(Tip 4) Prepare wedding gifts as a simple token, and wedding clothes as something usable after the ceremony."),
    ("예단은 부모님께만 필요한 물품으로, 혼수는 중고품 등을 활용해 스스로 마련한다.", "(Tip 5) Give 예단 as items needed only by the parents, and prepare 혼수 yourselves using used items and the like."),
    ("공공기관이나 무료 실비 예식장, 평일 혹은 야간 시간을 이용해 낭비와 교통혼잡 등을 최소화한다.", "(Tip 6) Use public institutions or free or at-cost wedding halls, and weekday or night times, to minimize waste, traffic congestion and so on."),
    ("과소비 신혼여행을 자제하고 개성적이고 검소한 여행계획을 세운다.", "(Tip 7) Refrain from an overspending honeymoon and make a distinctive and frugal travel plan."),
    ("신혼주택은 알뜰한 생활, 치밀한 계획으로 스스로 장만한다.", "(Tip 8) Prepare the newlywed home yourselves with a thrifty life and a meticulous plan."),
]
_ART7 = [
    ("예식장의 횡포, 늘어나는 혼례비용, 증가하는 호화예식, 정성의 표시라기엔 너무 과중한 혼수압박 등으로 특징지어지고 있는 요즘 우리의 혼례문화.", "Our wedding culture these days, characterized by the tyranny of wedding halls, rising wedding costs, increasing luxurious ceremonies, and a pressure over wedding articles too heavy to be called a sign of sincerity."),
    ("이를 바꾸기 위해서는 지나친 상업화와 가부장적 전통의 병폐부터 뜯어고쳐야 된다는 주장이 제기됐다.", "An argument was raised that to change this, we must first fix the ills of excessive commercialization and patriarchal tradition."),
    ("이는 구 일 가족과 혼인문화를 주제로 열린 구십육 한국가족학회 추계학술대회에서 연세대 사회발전연구소 책임연구원 손승영 씨가 혼례문화의 상업화와 가부장적 특성이란 논문에서 지적한 부분이다.", "This is the point that Son Seung-yeong, chief researcher at the Yonsei University Institute for Social Development, made in the paper “The Commercialization and Patriarchal Characteristics of Wedding Culture” at the autumn conference of the Korean Association of Family Studies of ’96, held on the 9th on the theme of “Family and Marriage Culture.”"),
    ("우선 상업화 현상의 대표적인 것들로 손 씨는 점점 대형화하여 가고 있는 혼수백화점, 갖은 횡포를 일삼는 예식장의 난립, 호화예식의 증가와 다양화를 부추기는 이벤트회사의 등장 등을 꼽는다.", "First, as representative examples of the commercialization phenomenon, Mr. Son picks out the wedding-goods department stores that are growing ever larger, the proliferation of wedding halls that habitually commit all sorts of tyranny, and the emergence of event companies that encourage the increase and diversification of luxurious ceremonies."),
    ("웨딩드레스와 연미복을 입고 혼례식을 올리며 비디오 촬영을 강조하는 문화로 바뀐 것, 의례절차나 구입상품을 더 고급화, 대형화로 흐르게 한 것은 전문예식장, 대형혼수백화점, 이벤트 회사 등의 책임이 많다는 것이다.", "The change into a culture of holding the ceremony in wedding dresses and tailcoats and stressing video filming, and the drift of ceremonial procedures and purchased goods toward more upscale and larger scale, are largely the responsibility of professional wedding halls, large wedding-goods department stores, event companies and so on."),
    ("한편 우리사회의 고유한 가치요 장점이기도 했던 가족주의가 가족이기주의로 변화돼 지나친 혼수 예단 강요 등 혼례문화를 왜곡시키는 원인이 되고 있는 형편이다.", "Meanwhile, familism, which had been our society’s own value and strength, has changed into family egoism and is becoming a cause that distorts wedding culture, such as the forcing of excessive wedding goods and 예단."),
    ("이에 체면문화의 하나인 결혼식 참여와 부조문화도 전통사회의 미덕이던 공동체문화로 발전하지 못하고 오히려 역작용만 불러일으키는 원인이 되고 있어 우리의 혼례문화는 손볼 구석이 한두 가지가 아니라는 것이다.", "Accordingly, attending weddings and the culture of monetary gifts, part of the culture of saving face, have failed to develop into the communal culture that was a virtue of traditional society and instead cause only adverse effects, so our wedding culture has more than one or two places to fix."),
    ("지금의 이런 혼례문화를 바꾸기 위해서는 어떻게 해야 될까?", "What should be done to change this wedding culture of today?"),
    ("손 씨는 우선 평등한 결혼을 위한 시도와 간소한 결혼식이 많아져야 하며 사회지도층이 이를 솔선수범해 가야 한다고 강조한다.", "Mr. Son stresses that first there must be more attempts at equal marriages and more simple weddings, and that the social leadership must set an example in this."),
    ("또 직원의 경조사를 쪽지 게시판을 통해 일률적으로 알리는 행태를 없애는 직장 중심의 변화도 필요하며 저렴한 결혼식 장소를 정책적으로 보급하는 노력도 더욱 많아져야 한다.", "Also, a workplace-centered change that eliminates the practice of uniformly notifying employees of family events through a memo board is needed, and efforts to spread low-cost wedding venues by policy must increase."),
    ("덧붙여 시민단체 주도의 꾸준한 계몽운동과 바가지 상혼에 대한 정부의 철저한 단속 등이 자꾸 왜곡되어만 가는 혼례문화를 바꾸는 지름길이란 것을 밝힌다.", "In addition, he states that a steady enlightenment campaign led by citizens’ groups and the government’s thorough crackdown on overcharging commercialism are the shortcut to changing a wedding culture that keeps getting distorted."),
]
_SPEAK7B = [("미국의 결혼식 및 피로연 방식에 대해 이야기해 보세요.", "Talk about how weddings and receptions are done in the United States."), ("그리고 한국의 결혼 문화와 비교해 보세요.", "And compare it with Korean wedding culture."), ("호화 결혼식 및 혼수에 대해 어떤 의견을 가지고 있는지 옆 친구와 이야기해 보세요.", "Talk with the friend next to you about what opinion you have on luxurious weddings and wedding goods.")]
_COM7 = [("전문예식장 (professional wedding halls)", "Tyranny of all kinds and a proliferation of halls; the change into a culture of wedding dresses and tailcoats with stress on video filming; ceremonial procedures made more upscale and larger"), ("혼수백화점 (wedding-goods department stores)", "They are growing larger and larger; goods bought for weddings have drifted toward more upscale and larger scale"), ("이벤트회사 (event companies)", "Their emergence encourages the increase and diversification of luxurious ceremonies")]
L4 = lesson(
    "U16 L7 · Part 2 (본 학습): thrifty weddings and the commercialization of wedding culture",
    "본 학습 · 혼수 · 예단 · 청첩장 · 축의금 · 결혼식 · 혼례문화 · 상업화 · 가부장적 · 호화예식 · 간소한 결혼식 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 1: 혼수와 예단 (wedding goods and gifts) — the book’s note",
             "In Korea, the groom usually buys or rents the couple’s home or apartment with a large deposit; the bride provides the furniture, appliances, other household items, and additional wedding gifts for the groom’s family. These items are called 혼수(품). Also, the two families exchange special wedding gifts called 예단. Other wedding expenses, including the ceremony, reception, and honeymoon travel are divided between the families. The burden of providing wedding gifts can sometimes cause conflicts among family members. Gift giving varies according to the social status of the couple’s family. For example, parents whose daughter is marrying a high-income professional (such as a doctor or a judge) are usually expected to give luxurious gifts to the groom’s family. The conflicts that arise over exchanging or requesting lavish wedding gifts are one of the leading causes of divorce in Korea."),
        card("알아봅시다 2: 청첩장과 축의금 (wedding invitations and gift money) — the book’s note",
             "Koreans invite many guests, including relatives, friends, and even acquaintances for their own or their children’s wedding ceremony. The guest list can often include hundreds of people. Inviting many guests and having a big wedding ceremony has been a way of displaying one’s social and economic status. Wedding guests normally bring gifts in the form of money, called 축의금. The amount of the gift depends on the social distance between the guest and the newlyweds or their families. Koreans frequently receive wedding invitations (청첩장) from people they barely know. In the spring or fall (the busiest wedding seasons), people may receive several invitations a month, which can create a financial burden."),
        card("학습활동 2 (Reading): tips for reducing wedding expenses",
             "The list below contains tips suggested by an organization, the 대한주부클럽연합회, about how to reduce wedding expenses (© Hankyoreh). In the book you listen to four audio clips (tracks 005 to 008) and match each with the related tip(s) by number. The text is the book’s: the tips are numbered 1 to 8 in the English only, the quotation marks around 상부상조 are removed and the dot in 축재•신분과시 is written 축재와 신분과시. The English is mine.",
             examples=passage(_TIPS7)),
        card("학습활동 4 (Reading): an article on a paper presented at an academic conference",
             "The following is an article introducing a paper presented at an academic conference (© Munwha). The text is the book’s with the numbers spelled out (9일 → 구 일; 96 → 구십육), the brackets 「 」 and the quotation marks removed, and the parenthesis (연세대 사회발전연구소 책임연구원) written before the name as 연세대 사회발전연구소 책임연구원 손승영 씨가. The English is mine.",
             examples=passage(_ART7)),
        card("학습활동 4: the questions answered (mine)",
             "1. The topic of the paper Mr. Son presented: “The Commercialization and Patriarchal Characteristics of Wedding Culture” (혼례문화의 상업화와 가부장적 특성).\n\n"
             "2. The two problems: (1) excessive commercialization (wedding halls’ tyranny, rising costs, luxurious ceremonies, heavy pressure over wedding goods); (2) the ills of patriarchal tradition (familism turned into family egoism, which forces excessive wedding goods and gifts, and a face-saving culture of attendance and monetary gifts).\n\n"
             "3. The examples of commercialization:",
             tables=[table(["Commercial entity", "Examples of commercialization (mine)"], [list(r) for r in _COM7])]),
        card("학습활동 4: his suggestions (mine, at least three)",
             "(a) More attempts at equal marriages and more simple weddings, with the social leadership setting an example; (b) a workplace-centered change that ends the practice of uniformly notifying employees of family events through a memo board; (c) policy efforts to spread low-cost wedding venues; (d) a steady enlightenment campaign led by citizens’ groups; and (e) the government’s thorough crackdown on overcharging commercialism."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK7B)),
        card("Activities left out", "학습활동 1 (Listening, tracks 003 and 004): a YTN news item on the divorce case of a middle school teacher, Ms. Kim: why she filed for divorce (A. the groom bought a luxurious apartment and an “officetel” (a studio apartment whose name derives from combining the words office and hotel) without her consent; B. the groom would not help her with household chores; C. the groom had serious, undisclosed financial problems before the marriage; D. the groom demanded an excessive number of wedding gifts from her), what the court decreed, and what a lawyer says the decree implies. 학습활동 2: the matching of the four audio clips (tracks 005 to 008) with the tips. 학습활동 3 (Listening, tracks 009 to 014): YTN news clips and interviews on efforts for simple weddings, to be matched and to write the suggestion given in each. They are audio."),
    ],
    exercises=uniq(
        _tr(_TIPS7, k=3) + _tr(_ART7, k=3) + _tr(_SPEAK7B, k=3)
        + [M("What are 혼수 (품)?", "Furniture, appliances and household items the bride provides", ["Gifts for guests", "Wedding photos", "The honeymoon trip"], "The book’s note."), M("What is 예단?", "Special wedding gifts exchanged by the two families", ["A wedding hall", "A kind of food", "A marriage license"], "The book’s note."), M("What is 축의금?", "Gift money brought by wedding guests", ["A fee for the hall", "A bank loan", "A wedding dress"], "The book’s note."), M("What does 청첩장 mean?", "A wedding invitation", ["A wedding photo", "A marriage certificate", "A gift list"], "청첩장."),
           M("What does the first tip say about invitations?", "Replace them with a notice sent after the wedding", ["Send more of them", "Send them by mail only", "Make them fancier"], "식후 알림장."), M("What does the third tip replace with a family gathering?", "The reception", ["The ceremony", "The honeymoon", "The gifts"], "피로연."), M("Who is Mr. Son in the article?", "A researcher who presented a paper on wedding culture", ["A bride’s father", "A wedding hall owner", "A government minister"], "손승영 씨."), M("What has familism turned into, according to the article?", "Family egoism", ["Individualism", "Communalism", "Egalitarianism"], "가족이기주의."), M("Who should set an example according to Mr. Son?", "The social leadership", ["Students", "Event companies", "Wedding halls"], "사회지도층."),
           F("청첩장 고지 ___은 경제적, 정신적 부담요인이다. (overuse)", "남용", ["활용", "절약"], "남용."), F("혼수 ___ 때문에 신부가 힘들다. (pressure)", "압박", ["기재", "농담"], "압박."), F("호화예식의 증가를 ___는 이벤트회사가 등장했다. (to encourage)", "부추기", ["막", "줄이"], "부추기다."), F("지나친 ___와 가부장적 전통의 병폐를 고쳐야 한다. (commercialization)", "상업화", ["평등화", "간소화"], "상업화."), F("바가지 상혼에 대한 정부의 철저한 ___이 필요하다. (crackdown)", "단속", ["보급", "독려"], "단속.")]
        + [read_q("호화예식이 늘어나고 있습니다"), read_q("피로연은 가족모임으로 대신합니다"), read_q("혼례문화를 바꾸기 위해서는 간소한 결혼식이 많아져야 합니다"), read_q("미국의 결혼식은 한국과 어떻게 다릅니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("강요(하다)", "(强要) coercion; pressure (to force; to push)", "다른 사람에게 자신의 생각을 강요하지 마세요."),
        ("대출(하다;받다)", "(貸出) loan (to get a loan)", "차를 사려면 대출을 받아야 합니다.", "대출금, 돈을 빌리다"),
        ("반환(하다)", "(返還) return (to return)", "계약금을 반환해 주세요.", "돌려주다"),
        ("별거(하다)", "(別居) separation (in a marriage) (to separate; to be separated)", "그 부부는 이 년째 별거 중입니다.", "이혼하다"),
        ("성에 차다", "to be satisfied", "신부 측에서 준비한 혼수가 시부모의 성에 차지 않았다.", "만족하다"),
        ("수련의", "(修練醫) a resident (doctor); “doctor in training”", "수련의 과정을 마치면 전문의 시험을 봐야 합니다.", "레지던트 | 의사, 전문의, 인턴"),
        ("악습", "(惡習) a bad habit; a vice; a bad custom", "전통이 아닌 악습은 타파해야 합니다.", "습관, 관습"),
        ("예단", "(禮緞) wedding gifts (exchanged between the bride’s and groom’s families)", "과도한 예단은 신부에게 큰 부담이 됩니다.", "지참금, 혼수"),
        ("위자료", "(慰藉料) alimony; (monetary) compensation (for damage)", "법원은 남편에게 위자료 천만 원을 지급하라고 판결했다."),
        ("의지", "(意志) one’s will; volition", "그 사람은 의지가 약해서 무슨 일을 끝까지 못 합니다.", "뜻"),
        ("지참금", "(持參金) a dowry", "신부에게 요구되는 과도한 지참금이 사회 문제가 되고 있다고 합니다.", "예단, 혼수"),
        ("파탄 (나다)", "(破綻) a failure; a rupture; a bankruptcy (to break; to fail)", "호화 결혼식으로 시작된 결혼 생활은 육 개월 만에 파탄이 났다.", "회복"),
        ("혼수", "(婚需) articles/items essential to a marriage ceremony; expenses related to a marriage", "혼수 준비 때문에 요즘 너무 바쁩니다.", "예단, 지참금"),
        ("혼인", "(婚姻) marriage", "혼인은 두 사람이 아닌 두 가정의 결합이다.", "결혼, 혼례, 백년가약"),
    ]),
    ("학습활동 2", [
        ("검소하다", "(儉素) to be frugal; to be simple", "저는 검소하게 결혼식을 치르고 싶습니다.", "사치스럽다 | 알뜰하다, 절약하다"),
        ("경조비", "(慶弔費) expenses related to extending congratulations and expressing condolences", "이번 달에는 생활비에서 경조비 부담이 컸다.", "축의금, 부조금, 조의금"),
        ("과시(하다)", "(誇示) ostentation; showing off (to show off; make an ostentatious display of)", "그 친구는 사람들에게 부자임을 과시하기 위해 돈을 물 쓰듯 썼다.", "자랑하다, 뽐내다"),
        ("관행", "(慣行) a customary practice; a convention", "선생님들한테 선물로 현금을 주는 관행은 없어져야 한다.", "관습"),
        ("상부상조", "(相扶相助) mutual help or aid", "우리 서로 상부상조하며 잘 지내면 좋겠어요."),
        ("알뜰하다", "to be frugal; to be thrifty", "그 여자는 알뜰하게 살림을 잘합니다.", "검소하다"),
        ("장만(하다)", "preparing or purchasing big-ticket items (to prepare; to purchase)", "이번에 집을 새로 장만했습니다.", "마련하다, 구입하다, 준비하다"),
        ("중고", "(中古) (a) used (article); (a) secondhand (article)", "중고 자동차"),
        ("증표", "(證票) a token; a certificate; proof (of something)", "이 반지는 우리 사랑의 증표예요."),
        ("취지", "(趣旨) a purpose; an object; an intent", "이 단체를 설립한 취지에 대해 말씀 드리겠습니다."),
        ("치밀하다", "(緻密) to be meticulous; to be cautious; to be accurate", "이번 일은 처음부터 치밀한 계획을 세웠기 때문에 성공했어요."),
    ]),
    ("학습활동 3", [
        ("귀금속", "(貴金屬) jewelry", "서울 종로에는 귀금속 가게가 많습니다.", "금, 은, 보석"),
        ("장롱", "(欌籠) a wardrobe; an armoire", "요즘은 장롱을 혼수로 장만하는 경우가 드뭅니다.", "옷장"),
        ("폐백", "(幣帛) a traditional ceremony performed by the newly wedded couple as an expression of respect for the groom’s family", "결혼식을 한 후에 신랑신부는 부모님께 폐백을 드립니다."),
    ]),
    ("학습활동 4", [
        ("가부장적", "(家父長) patriarchal", "한국 사회는 유교의 영향으로 가부장적인 전통이 강하다.", "가부장, 가부장제"),
        ("계몽(하다)", "(啓蒙) enlightenment (to enlighten; to educate)", "환경보호의 중요성을 알리기 위해서 사람들을 계몽해야 한다."),
        ("논문", "(論文) an academic paper or article; a thesis; a dissertation", "요즘 졸업논문을 쓰느라고 너무 바쁩니다."),
        ("미덕", "(美德) virtue; “beautiful virtue”", "인내는 모든 사람이 실천해야 하는 미덕입니다.", "악덕"),
        ("바가지 (씌우다)", "(idiom) overcharge; rip-off; “a gourd dipper” (to overcharge; to rip off)", "관광지에는 손님에게 바가지를 씌우는 식당들이 많아요.", "바가지 요금, 사기"),
        ("병폐", "(病弊) evil practices; ills; malaise", "입시위주의 교육은 한국 교육의 병폐입니다.", "폐단"),
        ("부조(금)", "(扶助金) a monetary gift for someone’s wedding or funeral", "제 친구는 결혼식에서 부조금을 받지 않는다고 합니다.", "축의금, 조의금"),
        ("상업화", "(商業化) commercialization", "올림픽이 상업화되었다고 말하는 사람들도 있습니다."),
        ("손을 보다", "(idiom) to correct; to repair; to take care of, etc.; “to see one’s hands”", "집안에 여기저기 손 볼 데가 많아요.", "고치다, 개선하다"),
        ("압박(하다)", "(壓迫) pressure; press (to put pressure on; to press)", "찬 수건으로 상처 부위를 압박해 주세요."),
        ("왜곡(하다/되다)", "(歪曲) distortion (to distort; to twist/to be distorted; to be twisted)", "이 사건은 점점 왜곡되고 있습니다."),
        ("이기주의", "(利己主義) egoism", "이 사건은 집단 이기주의를 잘 보여주는 예라고 하겠습니다.", "이타주의"),
        ("지름길", "a shortcut", "너무 지름길로만 가려고 하면 오히려 일을 더 망칠 수 있습니다."),
        ("체면", "(體面) saving face; honor; dignity", "한국인들은 체면을 중요하게 생각합니다.", "체면을 살리다"),
        ("평등", "(平等) equality", "지금은 남녀평등시대입니다.", "불평등"),
        ("호화", "(豪華) splendor; pomp; gorgeousness; luxury", "호화혼수가 사회 문제가 되고 있다."),
        ("횡포", "(橫暴) tyranny; high-handedness; oppression", "대기업들의 횡포 때문에 중소기업들이 어려움을 겪는다."),
    ]),
]
L5 = lesson(
    "U16 L7 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 강요 · 대출 · 별거 · 예단 · 위자료 · 지참금 · 파탄 · 혼수 · 혼인 · 검소하다 · 경조비 · 과시 · 관행 · 상부상조 · 알뜰하다 · 장만 · 증표 · 폐백 · 가부장적 · 계몽 · 논문 · 미덕 · 바가지 · 병폐 · 부조 · 상업화 · 왜곡 · 이기주의 · 체면 · 평등 · 호화 · 횡포",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with numbers are written out: 2년째 → 이 년째, 1,000만 원 → 천만 원 and 6개월 → 육 개월. The book prints the related words of 수련의 as 레지던트 | 의사, 전문의, 인턴 and of 별거 as 이혼하다. The book’s example for 중고 is the phrase 중고 자동차 (“a used car”), not a sentence.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=30, nread=24)),
)

# ================================================================== L6 Part 3
_ED7 = [
    ("소위 사 억 원 명품녀로 마음이 상한 국민들이 많다.", "(Paragraph 1) There are many citizens who were upset by the so-called “400-million-won luxury-goods woman.”"),
    ("사 억 원 명품녀로 지칭된 김 모 씨는 지난 칠 일 엠넷 텐트 인 더 시티에 출연, 자신이 현재 입고 있는 옷과 장신구 등이 사 억 원어치에 이르며 직업이 없지만 부모님의 용돈으로 화려한 생활을 유지한다면서 내가 패리스 힐튼보다 못할 게 없다고 큰소리쳤다.", "Ms. Kim, referred to as the “400-million-won luxury-goods woman,” appeared on the 7th of last month on Mnet’s “Tent in the City” and boasted that the clothes and accessories she is currently wearing amount to 400 million won’s worth, that she has no job but maintains a splendid life on her parents’ allowance, and that “I’m in no way inferior to Paris Hilton.” (The book prints her full name; it is shortened here to 김 모 씨.)"),
    ("프로그램을 둘러싸고 네티즌들의 비난 여론이 들끓자 급기야는 국회까지 나섰다.", "As netizens’ critical public opinion boiled over the program, even the National Assembly finally stepped in."),
    ("한 민주당 의원이 국회에 출석한 국세청장에게 서민에게 상실감과 박탈감을 주는 명품녀에 대해 과세할 생각이 없느냐고 묻기까지 했다.", "A Democratic Party lawmaker even asked the commissioner of the National Tax Service, who was attending the Assembly, whether he had no thought of taxing the “luxury-goods woman” who gives ordinary people a sense of loss and deprivation."),
    ("그런데 여기서 끝난 게 아니었다.", "But it did not end here."),
    ("이번에는 방송 자체가 조작됐을 가능성까지 제기되고 있다.", "This time, even the possibility that the broadcast itself was fabricated is being raised."),
    ("마치 시트콤의 한 장면 같은 이 사건을 접하면서 한숨이 절로 나왔다.", "Encountering this incident, like a scene out of a sitcom, a sigh came out on its own."),
    ("어쩌다가 우리가 이 지경까지 됐을까?", "How did we end up in this state?"),
    ("총체적 난국이란 바로 이런 걸 말하는 게 아닐까, 자문해 봤다.", "Isn’t this exactly what is meant by a “total crisis”? I asked myself."),
    ("이 프로그램을 방송한 엠넷은 대한민국 케이블 티브이 시장을 석권하고 있는 씨제이 그룹 산하에 있는 방송사다.", "(Paragraph 2) Mnet, which aired this program, is a broadcaster under the CJ Group, which dominates Korea’s cable TV market."),
    ("나름대로 자긍심과 책임감을 갖고 있을 방송사가 이처럼 자극적이고 쓰레기 같은 프로그램을 방송했다는 것을 믿을 수가 없다.", "I cannot believe that a broadcaster that presumably has pride and a sense of responsibility in its own way aired such a provocative, garbage-like program."),
    ("옐로 저널리즘의 극치를 보여 준 이 사건을 보면서 케이블 티브이 시장을 잠식해 온 방송사 경영진의 도덕 불감증을 의심하지 않을 수 없었다.", "Seeing this incident, which showed the height of yellow journalism, I could not help doubting the moral desensitization of the management of the broadcaster that has been eating into the cable TV market."),
    ("게다가 방송 프로그램 내용을 조작까지 했다면 이는 더욱 심각하다.", "Moreover, if they even fabricated the content of the program, this is even more serious."),
    ("조작가능성이 제기된 이후 엠넷 측은 방송 내용에 대한 반성이나 사과 없이 조작이 아님을 증명할 자료를 갖고 있다면서 강력하게 반발했다.", "After the possibility of fabrication was raised, Mnet strongly pushed back, saying it had materials to prove it was not fabricated, without any reflection or apology about the content of the broadcast."),
    ("아직도 어디서부터 잘못된 것인지 모르고 있는 듯한 태도다.", "It is an attitude as if they still do not know where things went wrong."),
]
_RECON7 = [("김 모 씨는 텔레비전 프로그램에 나와서 자기 옷과 장신구가 사 억 원어치라고 자랑했습니다.", "Ms. Kim appeared on a TV program and boasted that her clothes and accessories were worth 400 million won."),
           ("직업이 없지만 부모님의 용돈으로 살고 있다고 했습니다.", "She said she has no job but lives on her parents’ allowance."),
           ("많은 사람들이 비난했고 국회에서도 문제가 되었습니다.", "Many people criticized it and it became an issue in the National Assembly too."),
           ("그런데 나중에는 방송이 조작되었을 가능성까지 제기되었습니다.", "Later, even the possibility that the broadcast was fabricated was raised."),
           ("방송사는 사과하지 않고 오히려 강하게 반발했습니다.", "The broadcaster did not apologize and instead pushed back strongly.")]
_CRIT7 = [("자극적", "provocative; sensational", "The program was provocative"), ("쓰레기 같은", "garbage-like; trashy", "The program was “garbage”"), ("옐로 저널리즘", "yellow journalism", "The incident shows “the height of yellow journalism”"), ("도덕 불감증", "moral desensitization", "The management is morally numb")]
L6 = lesson(
    "U16 L7 · Part 3 (심화 학습): the “400-million-won luxury-goods woman” editorial",
    "심화 학습 · 명품녀 · 사설 · 방송 조작 · 옐로 저널리즘 · 도덕 불감증 · 총체적 난국 · 과세 · 서민 · 상실감 · 박탈감",
    requires=[],
    cards=[
        card("학습활동 1 (Reading and Writing): an editorial from a newspaper",
             "The following is an editorial from a newspaper (© Kyunghyang). The text is the book’s with the numbers spelled out (4억 원 → 사 억 원; 7일 → 칠 일), the English letters written in Hangul (Mnet → 엠넷; CJ → 씨제이; TV → 티브이), the brackets < > and the quotation marks removed, and the woman’s full name shortened to 김 모 씨. The English is mine; the paragraph numbers are in the English only.",
             examples=passage(_ED7)),
        card("학습활동 1: the questions answered (mine)",
             "1. Reconstructing the case in Korean (my version, using the information in the passage):",
             examples=passage(_RECON7)),
        card("학습활동 1: question 2 — who is criticized (mine)",
             "2. The author criticizes the broadcaster, Mnet, and especially its management (방송사 경영진). The underlined words are not marked in the text; the words the author uses to criticize the broadcaster are, in the order they appear in paragraph 2, these (the book asks for three):",
             tables=[table(["Word", "English meaning", "How the author uses it"], [list(r) for r in _CRIT7], say=[0])]),
        card("Activities left out", "학습활동 2 (Listening, track 015): a YTN news item on recent consumption trends, with a true-or-false choice among four statements (A. because of the economic recession, all domestic sales are rapidly declining; B. sales of small and mid-size cars are gradually increasing because of aggressive marketing; C. sales of luxury goods in large department stores are increasing despite the economic recession; D. more and more middle-class consumers prefer brand-name goods) and the meaning of 소비양극화. 학습활동 3 (Listening and Speaking, tracks 016 to 018): a YTN interview on lookism and the plastic surgery craze, with the meaning of 외모지상주의, two words reflecting lookism among teenagers, and, in two groups, tables on a survey and its results, the fundamental reasons for lookism and solutions (Interview A) and a government program, its purpose, details and the government’s plan to implement it (Interview B), followed by a group presentation in Korean. They are audio."),
    ],
    exercises=uniq(
        _tr(_ED7, k=3) + _tr(_RECON7, k=3)
        + [M("Who is called the “400-million-won luxury-goods woman”?", "A woman who boasted on TV that her clothes and accessories were worth 400 million won", ["A politician", "A TV announcer", "A tax officer"], "사 억 원 명품녀."), M("How does she say she maintains a splendid life?", "On her parents’ allowance", ["By her salary", "By inheritance", "By a lottery"], "부모님의 용돈."), M("What did a lawmaker ask the tax commissioner?", "Whether he had no thought of taxing the “luxury-goods woman”", ["Whether to ban TV", "Whether to arrest her", "Whether to hire her"], "과세할 생각."), M("What possibility was raised about the broadcast?", "That it was fabricated", ["That it was cancelled", "That it was live", "That it was free"], "조작됐을 가능성."), M("Which company group is Mnet under?", "The CJ Group", ["The Samsung Group", "The Hyundai Group", "The LG Group"], "씨제이 그룹."), M("How did Mnet react after the fabrication was raised?", "It pushed back strongly without apologizing", ["It apologized", "It resigned", "It stopped broadcasting"], "강력하게 반발했다."), M("What does the author doubt about the broadcaster’s management?", "Its moral desensitization", ["Its profits", "Its size", "Its age"], "도덕 불감증."),
           F("프로그램을 ___로 한 비난 여론이 들끓었다. (surrounding)", "둘러싸고", ["빼고", "제외하고"], "둘러싸다."), F("방송 자체가 ___됐을 가능성이 제기되고 있다. (fabricated)", "조작", ["반성", "출연"], "조작."), F("엠넷은 방송 내용에 대한 반성이나 ___ 없이 반발했다. (apology)", "사과", ["책임", "격려"], "사과."), F("서민에게 상실감과 ___을 주는 명품녀. (sense of deprivation)", "박탈감", ["책임감", "자긍심"], "박탈감."), F("이 사건은 옐로 저널리즘의 ___를 보여 준다. (height)", "극치", ["시작", "부분"], "극치.")]
        + [read_q("명품녀로 마음이 상한 국민들이 많습니다"), read_q("방송 자체가 조작됐을 가능성이 제기되었습니다"), read_q("엠넷은 강력하게 반발했습니다"), read_q("우리는 총체적 난국에 처해 있습니다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("과세(하다)", "(課稅) taxation (to tax; to levy a tax on)", "이 제품은 과세대상입니다.", "세금을 부과하다"),
        ("극치", "(極致) extremity; the height (of); the ultimate (in)", "소백산의 단풍은 아름다움의 극치이다."),
        ("도덕 불감증", "(道德不感症) moral desensitization; numbness to immorality", "이번 사건은 우리 사회의 도덕 불감증을 잘 보여주는 것입니다.", "도덕적 해이"),
        ("마음이 상하다", "(傷) to be frustrated; to become upset; “the mind hurts”", "이번 일로 마음이 많이 상했어요.", "속상하다"),
        ("박탈감", "(剝奪感) a sense of being deprived", "연말연시에는 소외된 사람들의 박탈감이 더 커집니다."),
        ("반발(하다)", "(反撥) resistance; opposition; push back (to resist; to oppose)", "야당의 국회의원들은 여당의 의견에 반발했습니다."),
        ("반성(하다)", "(反省) self-reflection; self-examination; introspection (to reflect on; to be introspective)", "저는 지금 제 잘못을 반성하고 있습니다.", "뉘우치다"),
        ("비난(하다/받다)", "(非難) criticism (to criticize/to be criticized)", "야당은 정부를 비난하고 있습니다.", "칭찬하다 | 비판하다, 비평하다"),
        ("사과(하다)", "(謝過) apology (to apologize)", "기분이 나쁘셨다면 사과 드리겠습니다.", "잘못을 빌다"),
        ("상실감", "(喪失感) a sense of loss", "사업 실패 후 사고로 아들까지 잃어버린 아버지의 상실감은 커져만 갔습니다."),
        ("여론", "(與論) public opinion; public sentiment", "새 법안에 대해 반대하는 여론이 있습니다."),
        ("옐로 저널리즘", "yellow journalism (This refers to a type of journalism that presents little or no legitimate, well-researched news, and instead uses eye-catching headlines to sell more newspapers and attract more audience members/viewers.)", "", "황색 저널리즘 | 선정적 언론"),
        ("자극적", "(刺戟的) provocative; sensational; pungent", "그 영화에는 자극적인 장면이 너무 많이 나와요. 저는 김치 같은 자극적인 음식을 좋아해요."),
        ("자문하다", "(自問) to ask oneself; to question oneself", "중요한 결정을 내리기 전에 결정에 대해 자문해 보는 것이 좋다.", "묻다, 질문하다"),
        ("장신구", "(裝身具) accessory; jewelry", "인사동에는 전통 장신구 가게가 많습니다.", "액세서리"),
        ("접하다", "(接) to be in contact with; to encounter; to learn; to hear", "언제 불교를 처음 접하셨습니까?", "듣다, 알게 되다"),
        ("책임감", "(責任感) sense of responsibility; accountability", "김 대리는 책임감이 강해서 일을 맡기면 안심할 수 있어요."),
        ("총체적 난국", "(總體的 難局) a total crisis; an overall difficult situation", "우리는 지금 총체적 난국에 처해 있습니다."),
        ("출연(하다)", "(出演) appearance (in a film, play, TV program, etc.) (to appear [in a film, play, TV program, etc.])", "이 영화에 유명한 배우들이 많이 출연합니다."),
        ("화려하다", "(華麗) (an appearance or a shape) to be fancy or showy; to be splendid", "연예인들은 겉으로 보기에는 아주 화려해 보입니다."),
    ]),
    ("학습활동 2", [
        ("뚜렷하다", "to be clear; to be obvious; to be well defined", "한국의 뚜렷한 사계절이 점점 없어지고 있습니다.", "희미하다, 불명확하다, 불분명하다 | 명확하다, 분명하다"),
        ("서민", "(庶民) an ordinary person; a common person; “commoner”", "요즘 같은 불황에 서민들은 정말 생활이 어렵습니다.", "중산층, 일반인"),
        ("소비심리", "(消費心理) consumer confidence; “consumption psychology”", "요즘 소비심리가 위축되고 있습니다."),
        ("신장세", "(伸張勢) an increasing trend", "최근의 수출 신장세에 힘입어 흑자폭이 커지고 있습니다.", "증가세 | 하락세"),
        ("양극화(하다)", "(兩極化) polarization (to polarize)", "점점 부의 양극화 현상이 심해지는 것 같아요."),
        ("위축(되다)", "(萎縮) shrinking; decline (to be intimidated; to contract; to subside; to decrease)", "경기가 회복되지 않자 소비심리가 위축되고 있습니다.", "활성화되다, 활발하다 | 줄어들다, 감소하다"),
        ("허리띠를 죄다", "to economize; to be very frugal; “tighten one’s belt”", "", "허리띠를 졸라매다 | 낭비하다 | 아끼다, 절약하다"),
    ]),
    ("학습활동 3", [
        ("거식증", "(拒食症) anorexia (nervosa); “food resistance syndrome”", "다이어트를 심하게 하다가 거식증에 걸리는 경우도 있어요."),
        ("격려(하다)", "(激勵) encouragement (to encourage; to cheer up)", "가족들의 격려가 제게는 가장 큰 힘입니다.", "독려하다"),
        ("매체", "(媒體) a medium", "티브이는 좋은 교육 매체이기도 합니다."),
        ("모순", "(矛盾) a contradiction; an inconsistency", "두 사람의 진술이 모순됩니다."),
        ("몸짱", "(slang) a person with a good physique", "몸짱 열풍 때문에 헬스클럽에 사람이 많습니다.", "몸매짱 | 얼짱, 맛짱"),
        ("무차별적", "(無差別的) indiscriminate", "이메일을 통해 스팸메일이 무차별적으로 배포됩니다.", "차별적"),
        ("성찰(하다)", "(省察) introspection; self-examination (to be introspective; to reflect on)", "새해는 자신을 돌아보는 성찰의 시간이기도 합니다.", "돌아보다"),
        ("성패", "(成敗) success and failure", "일의 성패는 자신에게 달렸습니다.", "성공과 실패"),
        ("성향", "(性向) a tendency; an inclination", "외모를 중시하는 성향이 젊은이들 사이에 강해지고 있습니다.", "경향"),
        ("신념", "(信念) belief; creed", "그 두 사람은 정치적 신념이 다릅니다.", "믿음"),
        ("얼(굴)짱", "(slang) a person with a good-looking face", "제 친구가 얼마 전에 성형수술을 했는데, 얼짱이 됐어요.", "미인, 미남, 몸짱"),
        ("외모지상주의", "(外貌至上主義) lookism; “prejudice or discrimination based on physical appearance and especially physical appearance believed to fall short of societal notions of beauty” (Merriam-Webster dictionary)", "외모지상주의 때문에 상처를 받는 사람들이 많습니다."),
        ("유포(하다/되다)", "(流布) circulation (of a rumor, story, etc.); dissemination (to spread; to circulate; to disseminate/to be spread; to be circulated; to be disseminated)", "그는 허위사실을 유포한 죄로 고소됐습니다.", "퍼뜨리다 | 소문을 내다"),
        ("이익", "(利益) profit; gain; advantage", "이익을 보지 않고 장사를 할 순 없어요.", "손해, 불이익"),
        ("자긍심", "(自矜心) pride; self-esteem", "우리 학교 학생들은 학교에 대한 자긍심이 아주 큽니다.", "자존심"),
        ("자발적", "(自發的) voluntary", "자발적 실업도 실업률에 포함됩니까?", "스스로"),
        ("절대적", "(絶對的) absolute", "저는 그분에게 절대적 지지를 보냅니다.", "상대적"),
        ("찬사", "(讚辭) praise; a compliment; a eulogy", "시상식에서 영화 감독은 주연배우에 대해 찬사를 아끼지 않았습니다.", "칭찬"),
        ("풍조", "(風潮) a tendency to/toward; a trend; a lee tide; “wind and tide”", "사회에 만연한 국산제품에 대한 불신풍조를 없애야 합니다."),
    ]),
]
L7 = lesson(
    "U16 L7 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 과세 · 극치 · 도덕 불감증 · 박탈감 · 반발 · 반성 · 비난 · 사과 · 상실감 · 여론 · 옐로 저널리즘 · 자극적 · 책임감 · 총체적 난국 · 출연 · 화려하다 · 서민 · 양극화 · 위축 · 거식증 · 모순 · 몸짱 · 성향 · 신념 · 얼짱 · 외모지상주의 · 자긍심 · 풍조",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives two extra notes: 사과 (謝過) “apology” is not 사과, “an apple”. The two examples of 자극적 are joined here. The example for 매체 has TV written 티브이 and 허리띠를 죄다 has the book’s related words 허리띠를 졸라매다 (the same), 낭비하다 (the opposite) and 아끼다, 절약하다. In the book the entry 얼(굴)짱 is printed with the related words 미인, 미남, 몸짱 and 몸짱 with 몸매짱 | 얼(굴)짱, 맛짱 (written 얼짱 here).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=30, nread=24)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 7: Name Brands and Lookism (명품선호와 외모지상주의)", [L1, L2, L3, L4, L5, L6, L7])

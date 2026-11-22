"""Unit 76: KBC Semester III, Unit 17, Lesson 1 - The Internet (인터넷).
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
_MATCH1 = [("유해", "harmful", "유해물질을 배출하다"), ("불법적", "unlawfulness; illegality", "불법적으로 사용하다"), ("개인정보", "personal information", "개인정보를 유출하다"), ("접속", "connection", "인터넷에 접속해서 정보를 찾다"), ("중독", "addiction", "마약에 중독돼서 치료를 받다"), ("사용자", "a user", "이 시설은 사용자가 많다"), ("예절", "manners; etiquette", "식당에서 예절을 지켜야 한다"), ("표현", "expression", "자유스럽게 생각을 표현하다"), ("기능", "function", "이 기계는 기능이 너무 복잡하다")]
_VERB1 = [("저는 보통 책을 살 때 인터넷 서점을", "이용하다", "to use (an internet bookstore)"), ("컴퓨터 해킹을 막기 위해 제 컴퓨터에 보안 프로그램을", "설치하다", "to install (a security program)"), ("국내의 인터넷 사이트에서 개인정보가 불법으로", "유출되다", "to be leaked (personal information)"), ("게임에", "중독되다", "to be addicted (to games)")]
_HJ1 = [("流 유/류", "flow; pass", "유출, 유통"), ("接 접", "connect; contact", "면접, 접속"), ("名 명", "name", "실명, 무명"), ("私 사", "private; personal", "사생활, 사립"), ("害 해", "harm", "피해, 재해")]
_HJW1 = [("유출", "spill; outflow"), ("유통", "circulation"), ("면접", "a face-to-face interview"), ("접속", "connection"), ("실명", "one’s real name"), ("무명", "unknown; not famous"), ("사생활", "privacy; one’s private life"), ("사립", "private; privately run"), ("피해", "damage"), ("재해", "a disaster")]
_OPP1 = [("유출", "유입", "outflow: inflow"), ("유명", "무명", "famous: unknown"), ("피해", "이익", "damage: benefit")]
_REL1 = [("A", "사생활 정보", "주민등록번호, 이메일 주소, 가족관계", "private-life information"), ("B", "불법적인 행위", "개인정보 유출, 지폐 위조, 명품 밀반입", "unlawful acts"), ("C", "유해물", "인터넷 성인방송, 마약, 폭력 동영상", "harmful material")]
_L1X = [("유입", "inflow"), ("유무", "presence or absence"), ("진출", "advancing into"), ("별명", "a nickname"), ("본명", "one’s real name"), ("화해", "reconciliation"), ("공해", "pollution"), ("이익", "profit; benefit"), ("주민등록번호", "a resident registration number"), ("이메일 주소", "an e-mail address"), ("가족관계", "family relations"), ("지폐 위조", "forging banknotes"), ("명품 밀반입", "smuggling in luxury goods"), ("성인방송", "adult broadcasting"), ("폭력 동영상", "a violent video"), ("장비 설치", "installing equipment"), ("표현의 자유", "freedom of expression"), ("유해물", "harmful material")]
L1 = lesson(
    "U17 L1 · Review: internet words and Sino-Korean 流 接 名 私 害",
    "인터넷 · 단어 복습 · 한자어 복습 · 유해 · 불법적 · 개인정보 · 접속 · 중독 · 사용자 · 예절 · 표현 · 기능 · 流 接 名 私 害",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives nine phrases with one word underlined and asks you to connect each underlined word with its English meaning on the right. The underline is not marked in the text; the pairs are:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH1], say=[0, 2])]),
        card("단어 복습 2: the verbs (my answers)", "Choose the right verb from the box (중독되다, 설치하다, 이용하다, 유출되다) for each sentence and put it in the right form. My answers:", tables=[table(["Sentence start", "Verb (my answer)", "Meaning"], [list(r) for r in _VERB1], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ1], say=[2]), ktable(_HJW1)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 유출: 유무, 유입, 유통, 진출; B. 유명: 별명, 실명, 본명, 무명; C. 피해: 화해, 이익, 공해, 유해).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP1], say=[0, 1])]),
        card("한자어 복습 2: the word that holds all three (my answers)", "Read the three words and choose from the box (장비 설치, 표현의 자유, 사생활 정보, 불법적인 행위, 유해물) the word that can include all of them; 장비 설치 and 표현의 자유 are left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Meaning"], [list(r) for r in _REL1], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L1X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH1], k=3) + _tr(_HJW1, k=3) + _tr(_L1X, k=3) + _tr([(a + " " + b, c) for a, b, c in _VERB1], k=3)
        + [M("What does the syllable 流 (유/류) mean?", "flow; pass", ["connect", "name", "harm"], "유출."), M("What does the syllable 接 (접) mean?", "connect; contact", ["flow", "name", "private"], "접속."), M("What does the syllable 名 (명) mean?", "name", ["flow", "harm", "private"], "실명."), M("What does the syllable 私 (사) mean?", "private; personal", ["name", "connect", "harm"], "사생활."), M("What does the syllable 害 (해) mean?", "harm", ["flow", "name", "private"], "피해.")
           , M("Which word is the opposite of 유출?", "유입", ["유무", "유통", "진출"], "Inflow."), M("Which word is the opposite of 유명?", "무명", ["별명", "실명", "본명"], "Unknown."), M("Which word is the opposite of 피해?", "이익", ["화해", "공해", "유해"], "Benefit."),
           M("Which word holds 개인정보 유출, 지폐 위조, 명품 밀반입?", "불법적인 행위", ["유해물", "사생활 정보", "장비 설치"], "Unlawful acts."), M("Which word holds 마약, 폭력 동영상, 인터넷 성인방송?", "유해물", ["불법적인 행위", "사생활 정보", "표현의 자유"], "Harmful material."), M("Which word holds 주민등록번호, 이메일 주소, 가족관계?", "사생활 정보", ["유해물", "불법적인 행위", "장비 설치"], "Private-life information.")
           , F("인터넷에 ___해서 정보를 찾습니다. (connection)", "접속", ["중독", "유출"], "접속하다."), F("마약에 ___돼서 치료를 받습니다. (addiction)", "중독", ["접속", "설치"], "중독되다."), F("식당에서 ___를 지켜야 합니다. (manners)", "예절", ["기능", "표현"], "예절."), F("이 기계는 ___이 너무 복잡합니다. (function)", "기능", ["예절", "접속"], "기능."), F("개인정보가 ___되어 경찰이 수사에 나섰습니다. (leaked)", "유출", ["설치", "이용"], "유출되다.")]
        + [read_q("인터넷에 접속해서 정보를 찾습니다"), read_q("개인정보가 유출되었습니다"), read_q("식당에서 예절을 지켜야 합니다"), read_q("이 기계는 기능이 너무 복잡합니다")]
    ),
)

# ================================================================== L2 Part 1
_POSTER1 = [
    ("고맙, 어솨, 방가. 이렇게 줄여쓰는 인터넷 언어가 심각한 수준입니다.", "“고맙”, “어솨”, “방가”: this kind of shortened internet language is at a serious level."),
    ("일상 생활에서조차 청소년들이 표준어보다는 인터넷 축약어를 더 즐겨 쓴다고 합니다.", "They say that even in daily life teenagers prefer to use internet abbreviations over standard language."),
    ("우리말이 사라질 때 우리나라도 사라집니다.", "When our language disappears, our country disappears too."),
    ("올바른 우리말을 쓰는 일에 인색하지 마세요.", "Don’t be stingy about using correct Korean."),
    ("오염되지 않은 인터넷 언어, 바로 우리 자신을 지키는 일입니다.", "Unpolluted internet language: it is exactly the act of protecting ourselves."),
]
_POSTER2 = [("온라인 상 생각없이 쓴 글로 인해 누군가에게 피해를 주고 있지 않습니까?", "Aren’t you harming someone because of something you wrote online without thinking?")]
_ART3 = [
    ("경기도와 경기도교육청은 이십이 일 사단법인 선플달기국민운동본부와 공동으로 도교육청에서 선플운동 선언문 서약식을 가졌다.", "On the 22nd, Gyeonggi Province and the Gyeonggi Provincial Office of Education held a signing ceremony for the declaration of the “good comments” movement at the provincial office of education, jointly with the incorporated association National Movement Headquarters for Posting Good Comments."),
    ("선플은 인터넷 상에서 악성 댓글을 일컫는 악플과 반대되는 말로 선의의 댓글을 의미한다.", "“Seonpeul” is the opposite of “akpeul”, which refers to vicious comments on the internet, and means well-meaning comments."),
    ("김문수 경기지사와 김진춘 경기도교육감은 이날 선언문에 서약한 뒤 선플 달기국민운동본부가 벌이는 선플 달기 운동에 내년 삼 월부터 도내 각종 민간단체와 각급 학교 및 직장에서 적극 참여하도록 독려하겠다고 약속했다.", "After pledging to the declaration that day, the Gyeonggi governor Kim Moon-soo and the Gyeonggi superintendent of education Kim Jin-chun promised to encourage private groups, schools of every level and workplaces within the province to take an active part in the good-comments campaign run by the headquarters from March next year."),
    ("지난해 오 월 출범한 선플 달기국민운동본부는 중앙대 민병철 교수와 고승덕 변호사, 영화배우 안성기, 탤런트 유동근, 방송인 김제동 씨 등이 공동 대표로 참여해 선플 달기 캠페인을 전개하고 있다.", "The headquarters, launched last May, is carrying out the campaign with Professor Min Byung-chul of Chung-Ang University, the lawyer Ko Seung-duk, the film actor Ahn Sung-ki, the TV actor Yu Dong-geun, the broadcaster Kim Je-dong and others taking part as joint representatives."),
]
_ART5 = [
    ("빌 게이츠 마이크로소프트 회장이 열 살짜리 큰딸의 컴퓨터 과용을 우려하고 있다는 기사는 시사하는 바가 적지 않다.", "The article saying that the Microsoft chairman Bill Gates is worried about his ten-year-old eldest daughter’s overuse of the computer carries a good deal of meaning."),
    ("부모들이 하루 종일 자녀 곁을 지킬 수 없는데다 컴퓨터에 대한 지식도 많지 않기 때문이다.", "That is because parents cannot stay by their children all day, and they do not know much about computers either."),
    ("이런 고민을 가진 부모라면 주요 인터넷포털 사이트의 컴퓨터 키즈케어, 어린이 보호, 서비스에 관심을 가질 만하다.", "Parents with this worry may well be interested in the “computer kids care” (child protection) services of the main internet portal sites."),
    ("음란, 폭력물 등 유해콘텐츠를 차단하거나 인터넷 사용시간까지 관리해 준다.", "They block harmful content such as obscene and violent material, and even manage the time spent on the internet."),
    ("월 이용료 삼천 원에서 사천 원으로, 간단한 프로그램만 설치하면 된다.", "The monthly fee is three to four thousand won, and you only have to install a simple program."),
    ("파란의 파란 자녀 컴퓨터 관리 서비스에 가입하면 자녀 컴퓨터는 두 대까지, 휴대전화는 다섯 대까지 등록할 수 있다.", "If you join Paran’s “Paran child computer management” service, you can register up to two children’s computers and up to five mobile phones."),
    ("원격으로 인터넷에 접속해 자녀 컴퓨터 이용 상황을 외부 컴퓨터나 휴대전화로 모니터링할 수 있다.", "You can connect to the internet remotely and monitor how the child’s computer is being used from an outside computer or a mobile phone."),
    ("엠파스 타임키퍼는 요일별, 시간대별 인터넷 사용을 제한하고, 게임 및 유해 사이트 이용을 막을 수 있게 한다.", "Empas’s “Timekeeper” limits internet use by day of the week and by time of day, and makes it possible to block games and harmful sites."),
]
_SPEAK1A = [("인터넷에서 불쾌했던 답글을 보았던 경험이나 인터넷 상에서 이루어지는 언어 파괴에 대해서 이야기해 보세요.", "Talk about an experience of seeing an unpleasant reply on the internet, or about the destruction of language that takes place on the internet.")]
L2 = lesson(
    "U17 L1 · Part 1 (도입 학습): internet slang, kind comments and child protection",
    "도입 학습 · 인터넷 언어 · 선플 · 악플 · 키즈케어 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: the poster against internet slang (공익광고협의회)", "The Korean text of the two posters (the English is mine). Questions and my answers: 1. What is the advertisement about? Answer: internet slang is being overused and is having an impact on the Korean language (third choice). 2. What might a person do after seeing this advertisement? Answer: refrain from using abusive language on the internet (second choice).", examples=passage(_POSTER1 + _POSTER2)),
        card("학습활동 3: “Let’s post good comments” (a news article)", "The article, with my English. Answers: 1. 선플 means a goodwill (well-meaning, kind) comment. 2. The underline is not marked in the text; the vocabulary of this part points to 선의 as a related word (“goodwill”) and the title to 착한 댓글 (“a kind comment”) as a synonym, and the antonym is 악플 (the article’s own opposite word). 3. 고승덕 is a lawyer, 민병철 a professor, 김제동 a broadcaster, 안성기 an actor and 유동근 a TV actor. 4. The purpose of the campaign is to get people, groups, schools and workplaces to post kind comments online in place of vicious ones.", examples=passage(_ART3)),
        card("학습활동 5: a newspaper article on kids’ computer care", "The article, with my English. Answers: 1. The ideal customer is a parent (B). 2. The table: 컴퓨터 키즈케어 (child protection services of the main portal sites): blocks harmful content such as obscene and violent material and manages internet use time; costs three to four thousand won a month; you only install a simple program. 파란 자녀 컴퓨터 관리 (Paran): register up to two children’s computers and five mobile phones, and monitor their use remotely from an outside computer or phone. 엠파스 타임키퍼 (Empas): limits internet use by day of the week and time of day, and blocks games and harmful sites. (The two web addresses in the book are left out.)", examples=passage(_ART5)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK1A)),
        card("Activities left out", "학습활동 2 (Listening, track 001): a public-service advertisement from an education site (edunet4u.net) on posting vicious comments; you choose what it refers to (D, posting vicious comments) and translate a sentence from the clip. 학습활동 4 (Listening, tracks 002 to 004): information from an education site on the services provided by the internet, with blanks to fill in. They are audio or video."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b in _POSTER1[:4]], k=3) + _tr(_ART3[1:2] + _ART3[3:4], k=2) + _tr(_ART5[3:5] + _ART5[5:7], k=3)
        + [M("What is the poster about?", "Internet slang is being overused and is affecting the Korean language", ["The Korean keyboard is badly laid out", "Korean is excellent for use on the internet", "Korean is overused on the internet"], "Poster."), M("What does 선플 mean?", "A goodwill comment", ["A vicious comment", "A shopping site", "A game"], "선플."), M("What is the opposite of 선플?", "악플", ["답글", "댓글", "선언문"], "악플."), M("What is 고승덕’s occupation in the article?", "A lawyer", ["A professor", "A broadcaster", "An actor"], "변호사."), M("What is 김제동’s occupation in the article?", "A broadcaster", ["A lawyer", "A professor", "A TV actor"], "방송인."), M("What is the purpose of the 선플 campaign?", "To get people to post kind comments online", ["To ban the internet", "To sell games", "To teach English"], "선플 달기."), M("Who would be an ideal customer for the kids’ computer care services?", "A parent", ["A student", "A CEO", "A teacher"], "부모."), M("How many computers and phones can you register with the Paran service?", "Two computers and five phones", ["Five computers and two phones", "One computer and one phone", "Ten computers"], "두 대, 다섯 대.")]
        + [F("인터넷 상에서 ___ 댓글을 다는 사람이 있습니다. (malicious)", "악성", ["선의", "유해"], "악성 댓글."), F("올바른 우리말을 쓰는 일에 ___하지 마세요. (be stingy)", "인색", ["겸손", "독려"], "인색하다.")]
        + [read_q("우리말이 사라질 때 우리나라도 사라집니다"), read_q("올바른 우리말을 쓰는 일에 인색하지 마세요"), read_q("착한 댓글을 달아요"), read_q("월 이용료는 삼천 원에서 사천 원입니다")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 3", [
        ("댓글", "a written comment (on a posting)", "악성 댓글은 큰 상처를 줄 수 있습니다.", "답글"),
        ("독려하다", "(督勵) to encourage; to urge", "감독은 최선을 다하라고 선수들을 독려합니다."),
        ("서약(하다)", "(誓約) vow; oath; pledge (to vow; to take an oath; to pledge)", "결혼식에서 혼인 서약을 합니다.", "약속하다"),
        ("선의", "(善意) goodwill", "선의의 경쟁은 도움이 됩니다.", "악의"),
        ("악성", "(惡性) vicious; malicious", "인터넷에서 악성 루머를 퍼트리는 사람들이 많습니다."),
    ]),
    ("학습활동 5", [
        ("과용(하다)", "(過用) overuse; overdose (to overuse; to overdose; to use excessively)", "약물과용으로 사망하는 사람들이 많습니다.", "오용하다"),
        ("유해하다", "(有害) to be harmful; to be noxious", "부모들은 유해한 인터넷 사이트에서 아이들을 보호해야 한다.", "무해하다"),
        ("음란", "(淫亂) obscene; lustful; lewd; pornographic", "청소년에게 음란비디오를 판매한 업자가 구속됐다."),
    ]),
]
L3 = lesson(
    "U17 L1 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 댓글 · 독려하다 · 서약 · 선의 · 악성 · 과용 · 유해하다 · 음란",
    requires=[],
    cards=vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=6, nread=6)),
)

# ================================================================== L4 Part 2
_PB1 = [("너무 권위적인 거 같습니다. 사장님 얼굴 보고 싶지 않습니다. 치워 주세요.", "A netizen: “It seems far too authoritarian. I don’t want to see the president’s face. Please take it away.”"), ("미안합니다. 저는 권위적이지 않은데 저의 사진이 그렇게 보이는 모양이지요? 너그럽게 봐 주시기 바랍니다. 사장 곽덕훈 드림.", "The president’s reply: “I am sorry. I am not authoritarian, but my photo must look that way. Please be generous with me. From President Kwak Deok-hoon.”")]
_ART2A = [
    ("곽덕훈 교육방송, 이비에스, 사장의 댓글이 인터넷에서 화제다.", "The “comment” of Kwak Deok-hoon, president of the Educational Broadcasting System (EBS), is the talk of the internet."),
    ("한 네티즌이 이비에스 게시판에 남긴 인신비하성 발언에 너그럽게 봐 달라며 겸손하게 처신한 사실이 입소문을 타면서다.", "This is because word has spread that he behaved humbly, asking to be treated generously, in response to a personally insulting remark a netizen left on the EBS bulletin board."),
    ("곽 사장은 평소 네티즌이 올린 질문에 직접 답글을 남기는 등 이들과의 소통에 많은 관심을 보여 왔다.", "President Kwak has shown a lot of interest in communicating with netizens, for example by leaving replies himself to questions they post."),
    ("네티즌들은 인신비하적인 글에 겸손한 자세로 임한 곽 사장의 처신을 높이 평가했다.", "Netizens highly valued President Kwak’s conduct in meeting a personally insulting post with a humble attitude."),
    ("곽 사장은 경향닷컴과의 전화통화에서 기분 나쁘다고 볼 게 아니라 홈페이지를 통한 소통의 순기능을 먼저 생각한다면서 일부 학생들의 표현 방식이 다소 거칠기도 하지만 교육적 측면에서 대응하려고 많이 노력한다고 말했다.", "In a phone call with Kyunghyang.com, President Kwak said that rather than seeing it as unpleasant, he thinks first of the positive function of communication through the homepage, and that some students’ way of expressing themselves is somewhat rough but he tries hard to respond from an educational point of view."),
]
_ART2C = [
    ("인터넷 게임에 빠져 자녀 양육 등 집안일에 무관심한 것도 이혼 사유가 된다는 대법원 판결이 나왔다.", "A Supreme Court ruling has come out that being absorbed in internet games and indifferent to housework such as raising children can also be grounds for divorce."),
    ("박 씨는 이천삼 년 정 씨와 결혼한 뒤 거의 매일 새벽 한 시에서 두 시까지 인터넷 게임을 하고 주말에도 오후까지 잠을 자거나 티브이 시청을 하며 집안일에 무관심했다.", "After marrying Ms. Jeong in 2003, Mr. Park played internet games almost every day until one or two in the morning, and on weekends too he slept until the afternoon or watched TV, and was indifferent to the housework."),
    ("원심 재판부는 부부의 이혼을 결정하면서 남편은 정 씨에게 위자료 천만 원과 팔천육백만 원의 재산분할금을 지급하라고 판결했다.", "In deciding the couple’s divorce, the court of first instance ruled that the husband must pay Ms. Jeong ten million won in alimony and eighty-six million won in divided marital assets."),
    ("대법원도 박 씨가 혼인 기간에 인터넷 게임에 빠져 부인에게 무관심했고 수시로 폭력을 수반한 폭언 등을 해 혼인 관계 파탄의 책임이 있다고 밝혔다.", "The Supreme Court also stated that Mr. Park was absorbed in internet games during the marriage, was indifferent to his wife, and frequently made violent verbal abuse, so he is responsible for the breakdown of the marriage."),
]
_SPEAK1B = [("네티즌으로서 지켜야 하는 예절에 대해서 반 친구들과 이야기해 보세요.", "Talk with your classmates about the manners you should keep as a netizen."), ("인터넷 중독을 막기 위한 방법이나 제도에 대해 이야기해 보세요.", "Talk about methods or systems for preventing internet addiction.")]
_NET1 = [("사이버 공간 상의 보이지 않는 저편에 나와 똑같은 감정을 가진 사람들이 있다는 것을 잊지 않고, 항상 예의를 갖추는 것이 바로 네티켓입니다.", "Not forgetting that on the other, unseen side of cyberspace there are people with feelings just like mine, and always showing courtesy: that is netiquette. (The three missing words are in the audio; this is my best guess at them.)")]
L4 = lesson(
    "U17 L1 · Part 2 (본 학습): an EBS president’s reply and a divorce ruling",
    "본 학습 · 댓글 · 곽덕훈 · 네티켓 · 이혼 · 인터넷 게임 · 사이버 망명 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: the president’s “comment” (a newspaper article)", "The two text balloons and the article, with my English. The book asks you to underline the words in the article that refer to the balloons (the first balloon is the 인신비하성 발언, “personally insulting remark”, and the second is the president’s humble reply, 너그럽게 봐 달라). Answers: 2. The underline is not marked in the text; the vocabulary of this part lists 대화하다 as a related word of 소통, so my best guess is 소통, synonym 대화. 3. President Kwak said that rather than seeing it as unpleasant, he first thinks of the positive function of communication through the homepage, and that some students’ way of expressing themselves is somewhat rough but he tries hard to respond from an educational point of view.", examples=passage(_PB1 + _ART2A)),
        card("학습활동 3: a divorce ruling (a news article)", "The article, with my English. Mr. Park and Ms. Jeong are given only by surname in the book. Answers: 1. The best title is C, 인터넷 게임 중독도 이혼사유 판결 (“Ruling: internet game addiction too is a ground for divorce”). 2. The underline is not marked; my best guess is the first sentence, translated above.", examples=passage(_ART2C)),
        card("학습활동 2: netiquette (listening)", "The audio gives the netiquette passage; the book asks you to write a title for it in Korean and to fill three blanks in this sentence. The words are in the audio, so the version below is my best guess, not the book’s answer (the blanks are 사이버 공간, 감정 and 예의).", examples=passage(_NET1)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK1B)),
        card("Activities left out", "학습활동 2 (Listening, tracks 005 and 006): the netiquette passage from an education site (edunet4u.net), for which you write a title and fill in missing words. 학습활동 4 (Listening, track 007): a YTN news report on internet policy. The questions ask: what is the government’s policy on users posting videos or comments on web portals; how Google Korea reacted and what it is doing; how the domestic portals reacted; and what 사이버 망명 (“cyber asylum”) means in the report. They are audio."),
    ],
    exercises=uniq(
        _tr(_ART2A[:4], k=3) + _tr([_ART2C[0], _ART2C[3], _ART2C[1]], k=3)
        + [M("What did President Kwak do that made him famous online?", "He answered an insulting comment humbly", ["He deleted the bulletin board", "He sued the netizen", "He ignored the comment"], "겸손하게 처신."), M("What does President Kwak say he thinks of first?", "The positive function of communication through the homepage", ["How to punish students", "How to raise prices", "How to close the bulletin board"], "소통의 순기능."), M("What is the best title for the divorce article?", "인터넷 게임 중독도 이혼사유 판결", ["인터넷 채팅으로 인한 가정 파괴", "이혼 시 자녀 양육권과 재산 분할금", "가장 많은 이혼 사유는 폭력과 폭언"], "C."), M("What did the Supreme Court rule?", "Being absorbed in internet games can be grounds for divorce", ["Games are banned", "Alimony is not needed", "Marriage cannot end in divorce"], "이혼 사유."), M("What does netiquette (네티켓) mean?", "Courtesy kept when using the internet", ["A kind of game", "A search site", "A security program"], "네티켓.")]
        + [F("곽 사장은 평소 네티즌과의 ___에 많은 관심을 보여 왔다. (communication)", "소통", ["합의", "대립"], "소통."), F("남편은 부인에게 ___ 천만 원을 지급해야 한다. (alimony)", "위자료", ["분할금", "양육비"], "위자료."), F("인터넷 게임에 빠져 집안일에 ___했다. (indifferent)", "무관심", ["겸손", "독려"], "무관심.")]
        + [read_q("그분은 항상 겸손하게 처신하십니다"), read_q("홈페이지를 통한 소통의 순기능을 생각합니다"), read_q("인터넷 게임에 빠져 집안일에 무관심했습니다"), read_q("네티즌으로서 지켜야 하는 예절이 있습니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("겸손하다", "(謙遜) to be modest; to be humble", "그분은 항상 겸손하게 말씀하십니다.", "거만하다"),
        ("대응하다", "(對應) reaction; response; taking action (to deal with; cope with; take action [against])", "소비자의 불만에 모두 대응하는 것은 불가능합니다."),
        ("소통(하다/되다)", "(疏通) communication (to communicate/to be communicated)", "저희 회사는 고객과의 소통을 가장 중요하게 생각합니다.", "대화하다"),
        ("인신비하", "(人身卑下) slander; personal attack", "인신비하 댓글을 단 사람들을 고소하였다."),
        ("처신(하다)", "(處身) behaving (to behave)", "늘 겸손하게 처신해야 합니다."),
    ]),
    ("학습활동 2", [
        ("가상(의)", "(假想) imaginary; hypothetical; virtual", "인터넷이 발달하면서 가상 공간에서 사는 사람들이 늘고 있다."),
        ("망치다", "(亡) to ruin; to spoil; to mess up", "비가 와서 이번 여행을 망쳤다."),
        ("명심하다", "(銘心) to keep in mind; “carve in the heart”", "수업 시간에 늦으면 안 된다는 것을 명심하세요."),
        ("무시하다", "(無視) to ignore; to disregard; to neglect; “not seeing”", "제 의견을 무시하지 말고 좀 존중해 주세요."),
        ("의사", "(意思) intention; a will", "아이들의 의사도 존중받아야 한다."),
    ]),
    ("학습활동 3", [
        ("분할금", "(分割金) divided marital assets (in a divorce); payment in installments", "법원은 남편에 대하여 부인에게 재산 분할금을 지급하라고 판결했습니다."),
        ("사유", "(事由) a reason; a cause", "그 학생은 질병을 사유로 휴학했습니다.", "이유, 근거"),
        ("수시(로)", "(隋時) frequently (as needed)", "친구가 수시로 전화를 해서 가끔 피곤하다.", "정시, 상시"),
        ("위자료", "(慰藉料) alimony", "그는 전처에게 위자료로 집을 주었습니다.", "양육비"),
        ("파탄", "(破綻) breakdown; failure; bankruptcy", "전 세계의 경제는 거의 파탄에 이르렀다."),
    ]),
    ("학습활동 4", [
        ("대립(하다/되다)", "(對立) opposition; confrontation (to confront/to be in conflict)", "두 사람의 의견이 첨예하게 대립하고 있습니다."),
        ("돌입하다", "(突入) to start; to begin; dash in; “to rush in(to)”", "그 사람은 단식에 돌입했습니다."),
        ("망명(하다)", "(亡命) asylum (to seek asylum; to defect)", "그는 삼 년 전에 북한에서 미국으로 망명했습니다."),
        ("실명제", "(實名制) a system that uses only one’s real name to open accounts at a bank or internet site; “real-name system”", "한국에서는 인터넷 실명제가 시행되고 있다.", "실명, 익명, 가명"),
        ("역차별", "(逆差別) reverse discrimination", "그 법안 때문에 어떤 사람들이 역차별을 당하기도 합니다.", "차별"),
        ("침해(하다)", "(侵害) invasion; violation; infringement (to infringe on; to encroach)", "인터넷을 통해 다른 사람의 사생활을 침해하는 것은 범죄이다."),
        ("토로하다", "(吐露) to speak one’s mind", "학생들은 각자의 불만을 토로했다."),
        ("합의(하다)", "(合意) agreement; consent; settlement (to come to an agreement; to reach a consensus)", "양측이 그 문제에 대해 합의를 보았습니다."),
    ]),
]
L5 = lesson(
    "U17 L1 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 겸손하다 · 소통 · 처신 · 가상 · 명심하다 · 의사 · 위자료 · 파탄 · 대립 · 망명 · 실명제 · 침해 · 합의",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book adds under 의사 (意思) “intention; a will” that 의사 (醫師) means “a doctor”. The book writes 수시 as 隋時; the usual Sino-Korean is 隨時 (“as needed”), and I keep the book’s form. In the example for 망명 the book has 3년 (written 삼 년 here). The book’s 정시, 상시 are the related words of 수시.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=12, nread=10)),
)

# ================================================================== L6 Part 3
_ART6 = [
    ("트위터나 메신저를 하다 게임 한판.", "While using Twitter or a messenger, one round of a game."),
    ("화려한 그래픽도 없고 생동감도 기존 온라인 컴퓨터 게임에 미치지 못하는 소셜 네트워크 게임, 소셜 게임, 시장이 커지고 있다.", "The market for social network games (social games), which have no flashy graphics and fall short of existing online computer games in liveliness, is growing."),
    ("소셜 게임이란 페이스북이나 트위터 같은 소셜 네트워크 서비스를 이용하는 사람들이 서비스 안에 연결된 지인들과 즐기는 게임이다.", "A social game is a game that people who use a social network service such as Facebook or Twitter enjoy with acquaintances connected within the service."),
    ("온라인 게임은 상대가 불특정 다수인 탓에 경쟁이 심해지면 욕설이 오가는 등 부작용이 발생할 수 있다.", "In online games, because the opponents are an unspecified multitude, side effects such as the exchange of curses can arise when competition gets fierce."),
    ("그러나 소셜 게임은 평소 아는 사람과 즐기는 게임이어서 사용자 사이에 친밀감이나 동질성을 키울 수 있다.", "But a social game is played with people one knows, so it can build closeness and homogeneity among users."),
    ("다중접속역할수행게임이나 캐주얼게임 등 피씨 기반 온라인 게임과 달리 스마트폰 등 모바일 기기에서도 사용할 수 있어 장소에 구애받지 않고 즐길 수 있다는 장점도 있다.", "Unlike PC-based online games such as massively multiplayer online role-playing games and casual games, they can also be used on mobile devices such as smartphones, so another advantage is that they can be enjoyed regardless of place."),
    ("소셜 게임을 자사 서비스에 붙인 페이스북은 이천칠 년 이천칠백만 명가량이던 월 방문자 수가 최근 오억 명으로 늘었다.", "Facebook, which attached social games to its own service, saw its monthly visitors grow from about 27 million in 2007 to 500 million recently."),
    ("페이스북 방문자 중 칠십 퍼센트 이상이 징가 등 소셜 게임을 즐긴다.", "More than 70 percent of Facebook visitors enjoy social games such as Zynga’s."),
    ("소셜 게임 이용자가 지인들을 불러들이며 눈덩이 효과를 일으켰기 때문이다.", "This is because social game users brought in their acquaintances and caused a snowball effect."),
    ("네이트 앱스토어는 소액 아이템을 팔면서 매출 일억 원을 달성하는 데 사 개월이 걸렸는데, 십억 원을 기록하는 데는 십 개월밖에 걸리지 않았다.", "The Nate App Store took four months to reach 100 million won in sales by selling small-sum items, but only ten months to record one billion won."),
    ("이번 달에는 한 달 동안 사억 원의 매출을 올렸다.", "This month it made 400 million won in sales in one month."),
    ("네이버와 다음도 소셜 게임에 본격적으로 뛰어들었다.", "Naver and Daum have also jumped into social games in earnest."),
    ("기존 온라인 게임보다 적은 투자로 폭발적인 매출 신장이 가능하고 포털사이트와 자사의 에스엔에스 서비스 이용자를 크게 늘릴 수 있다는 장점 때문이다.", "This is because of the advantages that explosive sales growth is possible with less investment than existing online games and that the users of portal sites and one’s own SNS service can be greatly increased."),
]
_SPEAK1C = [("인터넷이 대중화되면서 인터넷 문화에 대한 논의도 많습니다. 여러분이 생각하는 올바른 인터넷 문화에 대해서 이야기해 보세요.", "As the internet has become popular, there is much discussion of internet culture. Talk about what you think is a proper internet culture."), ("지금 여러분은 어떤 용도로 인터넷을 사용하고 있습니까?", "What are you using the internet for now? (The speaker’s closing question in the commentary.)")]
L6 = lesson(
    "U17 L1 · Part 3 (심화 학습): social games in the SNS era",
    "심화 학습 · 소셜 게임 · 에스엔에스 · 눈덩이 효과 · 페이스북 · 매출 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: “In the SNS era, social games are having fun” (a newspaper article)", "The article, with my English. Answers: 1. A social game is a game that people who use a social network service such as Facebook or Twitter enjoy with the acquaintances connected within the service. 2. Advantages of social games: played with people one knows, so closeness and homogeneity grow among users; can be used on mobile devices as well as PCs, so they can be enjoyed regardless of place. Adverse reactions to online games: opponents are an unspecified multitude, so when competition gets fierce, curses are exchanged and other side effects arise. 3. Two examples of the snowball effect: Facebook’s monthly visitors grew from about 27 million in 2007 to 500 million, with more than 70 percent of them enjoying social games; and the Nate App Store took four months to reach 100 million won but only ten months to reach one billion, and made 400 million won in one month this month. 4. Economic effects: explosive sales growth with less investment than existing online games, and a big increase in the users of the portal sites and of the companies’ own SNS services.", examples=passage(_ART6)),
        card("말해 봅시다! and the writing prompt", "The book’s speaking prompt, and the closing question from the commentary of 학습활동 3 (the English is mine):", examples=passage(_SPEAK1C)),
        card("Activities left out", "학습활동 1 (Listening, track 008): a YTN news item on the internet. You complete a table of the fields where smartphones are used and the issue discussed, and a table of the opinions of the National Election Committee and of some Assembly members, who disagree on the issue. 학습활동 3 (Listening, Writing, Speaking, track 009): a commentary from an education site (Seoul Education Research & Information Institute). You say what change the internet has brought to the speaker’s work, fill in a table of positive and negative aspects, write a Korean answer of your own to the closing question and discuss the changes in class. They are audio or class activities."),
    ],
    exercises=uniq(
        _tr(_ART6[1:], k=3)
        + [M("What is a social game?", "A game played with acquaintances connected within a social network service", ["A game played only with strangers", "A game played without the internet", "A card game"], "소셜 게임."), M("What is an advantage of social games over PC online games?", "They can be played on mobile devices regardless of place", ["They have flashier graphics", "They are played with strangers", "They need no internet"], "장소에 구애받지 않고."), M("What can happen in online games when competition gets fierce?", "Curses are exchanged", ["Prices fall", "Everyone wins", "The game stops"], "욕설."), M("What does 눈덩이 효과 mean in the article?", "Growth that snowballs as users bring in acquaintances", ["A winter sport", "A decline in sales", "A weather effect"], "눈덩이."), M("How long did the Nate App Store take to reach one billion won in sales?", "Ten months", ["Four months", "One month", "Two years"], "십 개월.")]
        + [F("소셜 게임은 사용자 사이의 ___을 키울 수 있다. (closeness)", "친밀감", ["생동감", "객관성"], "친밀감."), F("소셜 게임은 장소에 ___받지 않고 즐길 수 있다. (be restricted)", "구애", ["침해", "대응"], "구애받다."), F("페이스북은 방문자 수가 오억 명으로 ___. (grew)", "늘었다", ["줄었다", "망쳤다"], "늘다.")]
        + [read_q("소셜 게임 시장이 커지고 있습니다"), read_q("장소에 구애받지 않고 즐길 수 있습니다"), read_q("사용자 사이에 친밀감을 키울 수 있습니다"), read_q("이번 달에는 사억 원의 매출을 올렸습니다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("공직", "(公職) public office", "저희 아버지는 오랫동안 공직에 계셨습니다."),
        ("당직자", "(黨職者) a political party executive; “(political) party office person”", ""),
        ("매체", "(媒體) medium", "인터넷은 강력한 광고매체입니다.", "미디어"),
        ("발의(하다)", "(發意) a motion; a proposal (for action) (to move; to propose)", "서울시장은 주민투표를 발의했습니다."),
        ("상상(하다)", "(想像) imagination (to imagine; to conceive)", "우리가 상상하던 것들이 과학의 힘으로 가능해졌습니다."),
        ("실시간", "(實時間) real time", "마라톤 경기를 실시간으로 생중계하고 있습니다."),
        ("조항", "(條項) an article (in regulation or policy); a clause; a provision", "이 법 조항은 남녀평등에 어긋나는 것입니다."),
        ("탑재(하다/되다)", "(搭載) loading (to load/to be equipped with)", "이 컴퓨터는 윈도우 세븐을 탑재하고 있습니다."),
        ("편법", "(便法) expedient; an easy method; a shortcut; “easy law”", "개인 관광을 위해 편법으로 해외연수를 신청한 공무원이 적발됐다."),
    ]),
    ("학습활동 2", [
        ("구애(하다/받다)", "(拘碍) restriction (to restrict/to be restricted)", "시간에 구애받지 말고 천천히 이야기하세요."),
        ("동질성", "(同質性) homogeneity", "우리는 한민족으로서 동질성이 있습니다."),
        ("불특정 다수", "(不特定 多數) multitude of random people; “unspecified many (people)”", "이 조사는 불특정 다수를 대상으로 이루어졌습니다."),
        ("생동감", "(生動感) liveliness", "생동감 있는 영화를 만들려면 배우들이 훌륭해야 합니다."),
        ("친밀감", "(親密感) intimacy; “sense of closeness”", "아버지와 대화를 한 후에 더욱 친밀감을 느꼈습니다."),
    ]),
    ("학습활동 3", [
        ("객관성", "(客觀性) objectivity", "이 자료는 객관성이 부족합니다.", "주관성"),
        ("검증(하다/받다)", "(檢證) verification; investigation (to verify/to be verified)", "그 이론은 검증이 불가능합니다."),
        ("백과사전", "(百科事典) encyclopedia; “dictionary of hundred kinds”", "모르는 게 있으면 백과사전을 찾아 보세요."),
        ("중립적", "(中立的) neutral", "그 사람은 이 문제에 대해 중립적인 입장을 취하고 있습니다."),
        ("치우치다", "to lean/slant (toward); to be biased; to be partial", "그 판사는 한쪽에 치우침 없이 사건을 판결했다."),
        ("학대(하다/받다)", "(虐待) abuse; mistreatment (to abuse; to mistreat/to be abused; to be mistreated)", "동물학대도 법의 심판을 받아야 한다고 생각해요."),
        ("흐뭇하다", "to be pleased; to be delighted; to be satisfied", "원하던 집을 장만하니 마음이 흐뭇합니다."),
    ]),
]
L7 = lesson(
    "U17 L1 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 공직 · 매체 · 발의 · 실시간 · 조항 · 탑재 · 편법 · 구애 · 동질성 · 불특정 다수 · 친밀감 · 객관성 · 검증 · 중립적 · 치우치다 · 학대 · 흐뭇하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book adds under 구애 (拘碍) “restriction” that 구애 (求愛) means “courtship; courting”. The book has no example for 당직자, and 치우치다 has no Hanja in the book. In the example for 탑재 the book has Windows 7 (written 윈도우 세븐 here).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=12, nread=10)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 1: The Internet (인터넷)", [L1, L2, L3, L4, L5, L6, L7])

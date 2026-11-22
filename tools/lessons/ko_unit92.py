"""Unit 92: KBC Semester III, Unit 18, Lesson 7 - Elections (선거).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 18, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_MATCH7 = [("국무총리", "a prime minister", "국무총리에 임명되다"), ("장관", "a minister; a secretary", "장관 임기가 끝나다"), ("국회의원", "a member of the National Assembly; a congressman", "국회의원에 당선되다"), ("행정부", "the executive branch", "오바마 행정부가 출범하다"), ("입법부", "the legislative branch", "국회는 입법부 소속이다"), ("사법부", "the judicial branch", "사법부 조직을 개혁하다")]
_MINI7 = [("문화체육관광부", "the Ministry of Culture, Sports and Tourism"), ("기획재정부", "the Ministry of Strategy and Finance"), ("농림수산식품부", "the Ministry for Food, Agriculture, Forestry and Fisheries"), ("고용노동부", "the Ministry of Employment and Labor"), ("환경부", "the Ministry of Environment"), ("외교통상부", "the Ministry of Foreign Affairs and Trade"), ("보건복지부", "the Ministry of Health and Welfare"), ("국방부", "the Ministry of National Defense"), ("통일부", "the Ministry of Unification")]
_HJ7 = [("會 회", "gathering; party", "국회, 집회"), ("選 선", "elect; select", "총선, 선택"), ("票 표", "ticket; ballot", "투표, 득표"), ("當 당", "handle; select", "당국, 당선"), ("任 임", "entrust", "임명, 단임")]
_HJW7 = [("국회", "the National Assembly"), ("집회", "a rally"), ("총선", "the general election"), ("선택", "a choice; a selection"), ("투표", "voting; “throwing a ballot”"), ("득표", "gaining votes; polling"), ("당국", "the authorities concerned"), ("당선", "being elected"), ("임명", "an appointment"), ("단임", "the single term")]
_OPP7 = [("당선", "낙선", "being elected: losing an election"), ("단임", "연임", "a single term: consecutive terms"), ("임명", "사퇴", "an appointment: resignation"), ("보궐선거", "총선거", "a by-election: a general election")]
_REL7 = [("연임, 재임, 단임", "임기", "consecutive terms, serving again, a single term: a term of office"), ("낙선, 당선, 재선", "선거", "losing, winning, re-election: an election"), ("국회, 행정부, 사법부", "정부", "National Assembly, executive branch, judicial branch: the government")]
_L7X = [("재선", "re-election"), ("선거", "an election"), ("총선", "the general election"), ("담임", "a homeroom teacher"), ("당부", "a request"), ("선출", "selection by election"), ("지방자치", "local autonomy"), ("정당", "a political party"), ("연임", "serving consecutive terms"), ("재임", "serving again"), ("임기", "a term of office"), ("정부", "the government")]
L1 = lesson(
    "U18 L7 · Review: election words and Sino-Korean 會 選 票 當 任",
    "선거 · 단어 복습 · 한자어 복습 · 국무총리 · 장관 · 국회의원 · 행정부 · 입법부 · 사법부 · 정부 부처 · 會 選 票 當 任",
    requires=[],
    cards=[
        card("단어 복습 1: connect the underlined word with its meaning", "The book gives six sentences with a word underlined and six English meanings. The underline is not marked in the text; the pairs below are my reading:", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH7], say=[0, 2])]),
        card("The government ministries of 단어 복습 2", "Eight audio clips each describe the work of one ministry; you write the letter of the ministry and what it does. The nine ministries in the box of the book are below; the English names are mine:", tables=[ktable(_MINI7)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ7], say=[2]), ktable(_HJW7)]),
        card("한자어 복습 1: the word with the opposite meaning (my answers)", "Circle the word opposite in meaning to the word on the left (A. 당선: 총선, 재선, 낙선, 선거; B. 단임: 임기, 연임, 임명, 담임; C. 임명: 사퇴, 당부, 선출, 득표; D. 보궐선거: 지방자치, 총선거, 정당, 당선).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP7], say=[0, 1])]),
        card("한자어 복습 2: the word most closely related to the three (my answers)", "Choose from the box (선거, 정부, 당국, 임기) the word most closely related to the three words of each line:", tables=[table(["Three words", "Answer", "Meaning"], [list(r) for r in _REL7], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L7X)]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001–008): the eight audio descriptions of what the ministries do. They are audio; only the ministry names can be given here."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH7], k=3) + _tr(_MINI7, k=3) + _tr(_HJW7, k=3) + _tr(_L7X, k=4)
        + [M("What does the syllable 會 (회) mean?", "gathering; party", ["elect", "ballot", "entrust"], "국회."), M("What does the syllable 選 (선) mean?", "elect; select", ["gathering", "ballot", "entrust"], "총선."), M("What does the syllable 票 (표) mean?", "ticket; ballot", ["gathering", "elect", "handle"], "투표."), M("What does the syllable 當 (당) mean?", "handle; select", ["ballot", "entrust", "gathering"], "당선."), M("What does the syllable 任 (임) mean?", "entrust", ["elect", "gathering", "ballot"], "임명.")
           , M("Which word is the opposite of 당선?", "낙선", ["총선", "재선", "선거"], "Losing an election."), M("Which word is the opposite of 단임?", "연임", ["임기", "임명", "담임"], "Consecutive terms."), M("Which word is the opposite of 임명?", "사퇴", ["당부", "선출", "득표"], "Resignation."), M("Which word is the opposite of 보궐선거?", "총선거", ["지방자치", "정당", "당선"], "General election."), M("Which word relates to 연임, 재임, 단임?", "임기", ["선거", "정부", "당국"], "Term of office."), M("Which word relates to 국회, 행정부, 사법부?", "정부", ["선거", "당국", "임기"], "Government.")
           , F("국무총리에 ___되다. (to be appointed)", "임명", ["당선", "선택"], "임명."), F("국회의원에 ___되다. (to be elected)", "당선", ["임명", "득표"], "당선."), F("국회는 ___부 소속이다. (legislative)", "입법", ["행정", "사법"], "입법부."), F("___부 조직을 개혁하다. (judicial)", "사법", ["행정", "입법"], "사법부.")]
        + [read_q("국무총리에 임명되다"), read_q("장관 임기가 끝나다"), read_q("국회의원에 당선되다"), read_q("사법부 조직을 개혁하다")]
    ),
)

# ================================================================== L2 Part 1
_POSTER7 = [
    ("내 아이들이 꿈꾸는 나라이기에, 내 아이들이 살아갈 나라이기에 더 아름다운 세상, 더 밝은 세상을 만들고 싶습니다.", "Because it is the country my children dream of, and the country my children will live in, I want to make a more beautiful world, a brighter world."),
    ("이십일 세기, 당신의 바른 선택에 달려 있습니다.", "The 21st century depends on your right choice."),
]
_VOTE7 = [
    ("한 사람만 찍으면 되는 대통령 선거와 달리 이번 유월 이 일 지방선거에서는 모두 여덟 번 도장을 찍어야 한다.", "Unlike the presidential election, in which you only have to stamp for one person, in this June 2 local election you have to stamp eight times in all."),
    ("언뜻 복잡해 보이지만, 알고 보면 그다지 어렵지는 않다.", "It looks complicated at a glance, but once you know it, it is not that difficult."),
    ("투표 준비물. 준비물은 다른 공직선거와 같다.", "What to bring to vote. The items to bring are the same as in other public elections."),
    ("주민등록증과 운전면허증, 여권 등 공공기관이 발행한 사진이 있는 신분증명서를 챙겨야 한다.", "You must bring an ID with a photo issued by a public institution, such as a resident registration card, a driver’s license or a passport."),
    ("투표 시간도 오전 여섯 시부터 오후 여섯 시까지다.", "The voting hours are also from 6 a.m. to 6 p.m."),
    ("투표소 위치는 집으로 발송된 투표 안내문에 나와 있다.", "The location of the polling place is on the voting notice sent to your home."),
    ("중앙선관위 누리집의 내 투표소 찾기에서도 확인할 수 있다.", "You can also check it at “Find my polling place” on the website of the National Election Commission."),
    ("투표소에 도착하면 먼저 본인 확인을 위해 신분증을 제시하고 선거인명부에 서명한다.", "When you arrive at the polling place, you first show your ID to confirm your identity and sign the voter register."),
    ("그 뒤 옆으로 옮겨가 일 차 투표용지 네 장을 받는다.", "After that you move to the side and receive four ballots of the first round."),
    ("투표용지를 들고 기표소 안에 들어가, 기표용구를 이용해 용지마다 각각 한 명의 후보자한테만 기표한다.", "Holding the ballots, you go into the voting booth and, using the marking tool, mark for only one candidate on each ballot."),
    ("일 차 투표를 마치고 나면 안내에 따라 옆쪽에서 크기와 색깔이 다른 이 차 투표용지 네 장을 다시 받는다.", "When you finish the first round of voting, you follow the guidance and receive again at the side four ballots of the second round, which differ in size and color."),
    ("일 차 투표와 마찬가지로 이번에도 기표소에 다시 들어가 기표용구로 한 장에 한 번씩 찍는다.", "As with the first round, you again go into the booth and stamp once on each sheet with the marking tool."),
    ("마지막으로 이 차 투표의 기표소를 나와 백색 투표함에 네 장의 투표지를 한꺼번에 넣으면 모든 투표 절차가 끝난다.", "Finally, you come out of the booth of the second round and put the four ballots into the white ballot box all at once, and the whole voting procedure is over."),
]
_SPEAK7 = [("미국의 선거에 대해서 친구와 이야기해 보세요.", "Talk with a friend about elections in the United States."), ("선거의 종류, 투표 연령, 선거 주기, 특징 등.", "The kinds of elections, voting age, election cycle, characteristics and so on.")]
L2 = lesson(
    "U18 L7 · Part 1 (도입 학습): a poster slogan and how to vote",
    "도입 학습 · 선거 · 투표 · 지방선거 · 투표 준비물 · 신분증 · 투표소 · 기표소 · 투표용지 · 투표함 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: the poster slogan", "The book shows a poster (Kobaco) and a second picture (Kyunghyang) and asks you to tick the best-fitting description among six (public announcement for the new voting age; advertisement for a political agenda about clean energy; encouragement for people to vote in the upcoming election; announcement of a presidential inauguration; notice for a parliamentary election; notice for a presidential election). The slogan on the poster, with the numeral spelled out (21세기) and my English:", examples=passage(_POSTER7)),
        card("My answer to 학습활동 1", "The pictures are not part of the text, so this is a guess: the slogan urges the viewer to make the right choice for the sake of the children’s future, so I would tick “encouragement for people to vote in the upcoming election”."),
        card("학습활동 4: a guide to how to vote in the local election (Hankyoreh)", "The book asks three questions in English: which ID cards are accepted; how to find one’s polling place; and the voting procedure. The numbers are spelled in Hangul and “6·2 지방선거” is written 유월 이 일 지방선거; the website address is left out. The guide, with my English:", examples=passage(_VOTE7)),
        card("My answers to 학습활동 4", "1. A photo ID issued by a public institution: a resident registration card, a driver’s license or a passport. 2. The location is printed on the voting notice sent to your home; you can also find it under “Find my polling place” on the National Election Commission’s website. 3. Show your ID and sign the voter register; receive four first-round ballots; go into the booth and mark one candidate on each; then receive four second-round ballots of a different size and color, mark them in the booth in the same way; finally put all four of the second-round ballots into the white ballot box together."),
        card("말해 봅시다! (speaking)", "The book’s prompt, whose parentheses I turned into a second sentence (the English is mine):", examples=passage(_SPEAK7)),
        card("Activities left out", "학습활동 2 (Listening, Reading, track 009): a TV ad about elections (YTN): you tick whether it advertises a candidate’s education platform, promotes fairness in campaigns, or encourages people to take part in the upcoming election. 학습활동 3 (Listening, track 010): a video of a citizen’s opinion on local-election candidates (Hankyoreh): you note the type of candidate the citizen prefers. They are audio and video."),
    ],
    exercises=uniq(
        _tr(_POSTER7, k=2) + _tr(_VOTE7, k=3) + _tr(_SPEAK7, k=2)
        + [M("How many times must you stamp in this local election?", "Eight times", ["Once", "Four times", "Twelve times"], "여덟 번."), M("What are the voting hours?", "6 a.m. to 6 p.m.", ["9 a.m. to 9 p.m.", "8 a.m. to 5 p.m.", "Noon to midnight"], "오전 여섯 시부터 오후 여섯 시."), M("Where is the location of your polling place printed?", "On the voting notice sent to your home", ["On your ID", "On your ballot", "On a bus pass"], "투표 안내문."), M("What do you sign at the polling place?", "The voter register", ["A petition", "A ballot", "A tax form"], "선거인명부."), M("How many second-round ballots do you receive?", "Four", ["One", "Two", "Eight"], "네 장."), M("What color is the ballot box?", "White", ["Blue", "Red", "Black"], "백색 투표함.")]
        + [F("투표소에서 먼저 ___을 제시한다. (an ID)", "신분증", ["도장", "용지"], "신분증."), F("기표___ 안에 들어가 후보자에게 기표한다. (booth)", "소", ["함", "구"], "기표소."), F("선거인___에 서명한다. (register)", "명부", ["용지", "도장"], "선거인명부."), F("마지막으로 백색 투표___에 투표지를 넣는다. (box)", "함", ["소", "구"], "투표함.")]
        + [read_q("이번 유월 이 일 지방선거에서는 모두 여덟 번 도장을 찍어야 한다"), read_q("투표소에서 신분증을 제시하고 선거인명부에 서명한다"), read_q("백색 투표함에 네 장의 투표지를 한꺼번에 넣는다"), read_q("미국의 선거에 대해서 친구와 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("세기", "(世紀) a century", "산업화는 십육 세기부터 시작되었다."),
    ]),
    ("학습활동 3", [
        ("야당", "(野黨) an opposition party", "이번 선거에서 야당이 승리할 것으로 보입니다.", "여당 / 양당, 다수당, 소수당"),
        ("여당", "(與黨) a ruling party", "새 법안에 대해 여당 의원들이 강하게 반발하고 있습니다.", "야당"),
    ]),
    ("학습활동 4", [
        ("기표(하다)", "(記票) filling out a voting card (to fill out a voting card)", "저쪽 기표소에 가셔서 먼저 투표 용지를 작성하세요."),
        ("도장", "(圖章) a stamp; a seal", "요즘은 도장대신 서명으로 은행계좌를 만들 수 있습니다."),
        ("선거인명부", "(選擧人名簿) a voting register; “voter roster”", "투표하기 전에 선거인명부에서 본인의 이름을 확인하셔야 합니다."),
        ("용지", "(用紙) a (blank) form; paper", "에이포 용지가 다 떨어졌어요. 주문 좀 해 주세요."),
    ]),
]
L3 = lesson(
    "U18 L7 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 세기 · 야당 · 여당 · 기표 · 도장 · 선거인명부 · 용지",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book lists 여당 beside 야당 and the compounds 양당, 다수당, 소수당 (the two parties, the majority party, the minority party) as related words of 야당. The examples had digits and Latin letters in the book (16세기, A4용지), which I spelled out (십육 세기, 에이포 용지).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=8, nread=7) + [M("What does 야당 mean?", "An opposition party", ["A ruling party", "A voting register", "A century"], "야당."), M("What does 여당 mean?", "A ruling party", ["An opposition party", "A stamp", "A form"], "여당."), M("What does 선거인명부 mean?", "A voting register", ["A ballot box", "A voting booth", "A stamp"], "Voter roster."), M("What does 기표하다 mean?", "To fill out a voting card", ["To sign a register", "To count votes", "To go to a polling place"], "기표."), M("What does 도장 mean?", "A stamp; a seal", ["A form", "A century", "An opposition party"], "도장."), M("What does 용지 mean?", "A (blank) form; paper", ["A stamp", "A register", "A party"], "용지.")]),
)

# ================================================================== L4 Part 2
_GEN7 = [("엑스 세대", "Generation X"), ("엔 세대", "Generation N"), ("삼팔육 세대", "the 386 generation: coined in the 1980s for people born in the 1960s who went to college in the 1980s (3 for their 30s, 8 for the 1980s, 6 for the 1960s); known for taking part in democratic movements"), ("사팔육 세대", "the 486 generation: the same people, named in the 1990s when they were in their 40s"), ("칠공팔공 세대", "the 7080 generation: people who were in their 20s or 30s during the 1970s and 1980s"), ("닷컴 세대", "the dot-com generation"), ("와이 세대", "Generation Y")]
_TEXT7 = [
    ("꼭 투표 문자 열 통 돌리기 운동", "A campaign of passing around ten “be sure to vote” text messages"),
    ("부산에 사는 한 청년은 지난 삼십일 일 지인들한테서 투표 참여를 독려하는 문자메시지 두 통을 받았다.", "A young man living in Busan received two text messages from acquaintances on the 31st encouraging him to take part in voting."),
    ("평소 존경했던 중학교 선생님이 보내 온 첫 메시지에는 다음과 같이 적혀 있었다.", "The first message, sent by a middle school teacher whom he had always respected, read as follows."),
    ("유월 이 일 꼭 투표하자. 의식 있고 깨어 있는 젊은이이길 바란다. 주위 사람들과 같이 투표장에 꼭.", "Let’s be sure to vote on June 2. I hope you are an aware and awake young person. Be sure to go to the polling place together with the people around you."),
    ("두 번째 메시지는 청년, 투표장에서 역사의 주인이 되자는 내용이었다.", "The second message said, “Young people, let’s become the masters of history at the polling place.”"),
    ("그는 문자를 보니 잊지 말고 꼭 투표해야겠다는 생각이 새삼 들었다고 말했다.", "He said that on seeing the message, the thought struck him anew that he must not forget and must be sure to vote."),
    ("유월 이 일 지방선거가 막바지에 이르면서 이천십 유권자 희망연대는 지난 삼십일 일부터 선거 당일인 이 일까지 매일 한 사람이 지인 열 명에게 투표 참여를 독려하는 문자를 보내는 희망 문자 보내기 운동을 벌이고 있다.", "As the June 2 local election reaches its final stretch, the 2010 Voters’ Hope Alliance has been running a “hope text messaging” campaign from the 31st until election day, the 2nd, in which each person sends a text encouraging voting to ten acquaintances every day."),
    ("이재근 참여연대 행정감시팀장은 지난해 서울광장 조례 개정운동을 하면서 한 사람이 서명용지 열 장 모으기 운동을 벌여 성공을 거둔 경험이 있다며 한 사람이 열 명에게, 그 열 명이 또 다른 열 명에게 문자를 보내면 젊은 층의 투표율을 획기적으로 끌어 올릴 수 있을 것이라고 말했다.", "Lee Jae-geun, head of the administration monitoring team of the People’s Solidarity, said that while campaigning to revise the Seoul Plaza ordinance last year they had succeeded with a campaign in which each person collected ten signature sheets, and that if one person sends a text to ten people and those ten send to another ten each, the turnout of young people can be raised dramatically."),
    ("유권자 희망연대 활동가들은 지난 주말부터 꼭 투표합시다. 이 문자 받은 분들은 열 분에게 똑같은 문자를 보내 주세요라는 문자를 보내고 있다.", "Activists of the Voters’ Hope Alliance have been sending, since last weekend, the text, “Let’s be sure to vote. Those who received this text, please send the same text to ten people.”"),
]
_SPEAK7B = [("여러분의 고향 주에서 주지사 선거가 있다면 어떤 공약을 가진 사람을 뽑고 싶습니까?", "If there were a governor’s election in your home state, what kind of pledge would you want the person you vote for to have?"), ("그 이유는 무엇입니까?", "What is the reason?"), ("여러분이나 여러분의 가족 친구들은 선거 때 투표를 합니까?", "Do you or your family and friends vote at elections?"), ("하지 않는다면 그 이유는 무엇입니까?", "If not, what is the reason?")]
L4 = lesson(
    "U18 L7 · Part 2 (본 학습): the generation words and a vote-by-text campaign",
    "본 학습 · 세대 · 386세대 · 투표 캠페인 · 문자 메시지 · 투표 독려 · 유권자 · 투표율 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: ~세대 (generation words)", "The book’s note (in English) says that Koreans use ~세대 for a certain generation, as in X세대, N세대 and 386세대, and that compounds ending in 세대 describe social features of a generation. The terms (the letters and digits are spelled as they are said):", tables=[ktable(_GEN7)]),
        card("학습활동 1: a news article on a vote campaign (Hankyoreh)", "The book asks two questions in English: why the middle school teacher sent the message; and how to complete “The campaign recommends that voters who receive the text message vote and ___”. The book names the young man by a placeholder surname and age (이 아무개 (30)); as he is a private person I wrote “a young man”. The two messages’ quotation marks are dropped and I split the first message into separate sentences, writing “꼭~!” as “꼭.” The numbers are spelled in Hangul. The article, with my English:", examples=passage(_TEXT7)),
        card("My answers to 학습활동 1", "1. The teacher wanted to encourage the young man to vote on June 2 as an aware, awake young person together with the people around him. 2. The campaign recommends that voters who receive the text message vote and send the same text to ten other people."),
        card("말해 봅시다! (speaking)", "The book’s two prompts, which I split into four sentences; the English “pledge” after 공약 is dropped (the English is mine):", examples=passage(_SPEAK7B)),
        card("Activities left out", "학습활동 2 (Listening, track 011): a KBS interview on elections: you choose the true statement among four (A. young voters participate more actively than in the past; B. turnout of those in their 20s is higher than in the 1980s and 1990s; C. young voters are strongly influenced by the employment rate; D. turnout of those in their 20s is lower than other age groups), explain the interviewee’s account of the turnout of voters in their 20s in the previous general election, and fill a table of the differences between people in their 20s in the 1980s and today. 학습활동 3 (Listening, track 012): a KBS news story: you write what obstacles a college student must overcome to take part in the election, what the percentages 35.9% and 87.9% refer to, and what action is recommended to raise the turnout of voters in their 20s. They are audio."),
    ],
    exercises=uniq(
        _tr(_TEXT7, k=3) + _tr(_GEN7[:5], k=3) + _tr(_SPEAK7B, k=2)
        + [M("What did the teacher’s first message ask the young man to do?", "Be sure to vote on June 2", ["Run for office", "Join a rally", "Donate money"], "꼭 투표하자."), M("How many people should each recipient forward the text to?", "Ten", ["Two", "Three", "A hundred"], "열 분."), M("What does the campaign hope to raise?", "The turnout of young voters", ["Taxes", "The voting age", "The number of candidates"], "젊은 층의 투표율."), M("Which group runs the “hope text messaging” campaign?", "The 2010 Voters’ Hope Alliance", ["The National Election Commission", "A political party", "A newspaper"], "유권자 희망연대."), M("What does the 386 generation refer to?", "People who were in their 30s in the 1980s, in college in the 1980s and born in the 1960s", ["People born in the 1980s", "People in their 30s today", "People who went to college in the 1960s"], "삼팔육 세대."), M("What is the 486 generation?", "The same people, named in the 1990s when they were in their 40s", ["The next generation", "People born in the 1940s", "Young voters of today"], "사팔육 세대.")]
        + [F("투표 참여를 ___하는 문자메시지를 받았다. (to encourage)", "독려", ["호소", "완화"], "독려하다."), F("젊은 층의 투표___을 획기적으로 끌어 올릴 수 있을 것이다. (turnout rate)", "율", ["표", "소"], "투표율."), F("선거 ___인 이 일까지 매일 문자를 보낸다. (on the day)", "당일", ["후보", "공약"], "당일."), F("한 사람이 지인 열 명에게 문자를 ___. (to send)", "보낸다", ["받는다", "모은다"], "보내다.")]
        + [read_q("꼭 투표하자"), read_q("의식 있고 깨어 있는 젊은이이길 바란다"), read_q("한 사람이 지인 열 명에게 투표 참여를 독려하는 문자를 보낸다"), read_q("여러분의 고향 주에서 주지사 선거가 있다면 어떤 공약을 가진 사람을 뽑고 싶습니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 2", [
        ("공약", "(公約) a public pledge; an election promise", "정치인들이 실제로 공약을 실천하는 경우가 많지 않아요."),
        ("당사자", "(當事者) the party concerned; the person involved", "이번 사건은 당사자들 간의 합의로 쉽게 해결되었다."),
        ("역대", "(歷代) successive generations (of the past); “historical generation”", "사무실 벽에 역대 장관들의 사진이 걸려 있다."),
        ("창출(하다/되다)", "(創出) creation (of jobs, profit, etc.) (to create/to be created)", "이 사업은 많은 이익을 창출하고 있다."),
    ]),
    ("학습활동 3", [
        ("눈코 뜰 새 없이 바쁘다", "extremely busy; “to be too busy to open the eyes and the nose”", ""),
        ("부재자투표소", "(不在者投票所) a poll station for absentee voting", ""),
        ("완화(하다/되다)", "(緩和) relaxation; making less strict (to relax; to ease/to be eased)", "정부는 북한에 대한 경제 제재를 완화했다.", "강화하다"),
        ("추산(하다/되다)", "(推算) estimation (to estimate/to be estimated)", "이번 수해로 삼만 명 이상의 수재민이 발생한 것으로 추산됩니다.", "추정하다"),
    ]),
]
L5 = lesson(
    "U18 L7 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 공약 · 당사자 · 역대 · 창출 · 눈코 뜰 새 없이 · 부재자투표소 · 완화 · 추산",
    requires=[],
    cards=[card("A note on the Korean in this list", "창출 was glossed in Lesson 4 (Trade) of this Unit as “creation” in general; here the book says “creation (of jobs, profit, etc.)”. 완화 lists 강화하다 as its opposite; 추산 lists 추정하다 as similar. 눈코 뜰 새 없이 바쁘다 and 부재자투표소 have no example in the book. The example of 추산 has 3만 명 in digits, which I spelled out (삼만 명).")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=8, nread=7) + [M("What does 공약 mean?", "A public pledge; an election promise", ["A rally", "A ballot", "A seat"], "공약."), M("What does 당사자 mean?", "The party concerned", ["An opposition party", "A neighbor", "A judge"], "당사자."), M("What does 역대 mean?", "Successive generations (of the past)", ["The future", "A generation gap", "An era name"], "역대."), M("What does 완화하다 mean?", "To relax; to ease", ["To tighten", "To estimate", "To create"], "완화."), M("What does 추산하다 mean?", "To estimate", ["To relax", "To create", "To nominate"], "추산."), M("What does 부재자투표소 mean?", "A poll station for absentee voting", ["A ballot box", "A voting booth", "A town hall"], "부재자투표소.")]),
)

# ================================================================== L6 Part 3
_HUG7 = [
    ("나는 서울 동작구의 풀뿌리 시민단체인 희망동작네트워크, 즉 희망동네 회원이다.", "I am a member of Hope Dongjak Network (Hope Neighborhood), a grassroots civic group of Dongjak District in Seoul."),
    ("오늘은 희망동네가 주민들의 투표 참여를 호소하는 프리허그를 하기로 한 첫날이다.", "Today is the first day that Hope Neighborhood is to do free hugs appealing to residents to take part in voting."),
    ("프리허그하는 거예요?", "“Are you doing free hugs?”"),
    ("드디어. 한 분이 다가와 말을 걸었다.", "At last. A person came up and spoke to me."),
    ("이렇게 반가울 수가 없다.", "I could not be gladder."),
    ("네.", "“Yes.”"),
    ("아들과 함께 산책을 하러 나온, 사십 대로 보이는 아주머니다.", "It is a woman who looks to be in her forties, out for a walk with her son."),
    ("내가 다시 말을 받았다.", "I took up the conversation again."),
    ("투표하실 거죠?", "“You will vote, won’t you?”"),
    ("해야죠.", "“I should.”"),
    ("그럼 약속하시는 뜻으로 한 번 안아 주고 가세요.", "“Then give me a hug before you go, as a promise.”"),
    ("이분께서는 투표하시겠지? 오늘 댁에 돌아가서, 내일 이웃을 만나 프리허그한 얘길 전하며 다른 사람들에게도 투표하러 가자고 하시겠지?", "She will vote, won’t she? Will she go home today, meet a neighbor tomorrow, tell about the free hug and tell other people too to go and vote?"),
    ("그리고 세 명과 더 체온을 나눴다.", "And I shared body warmth with three more people."),
    ("지방선거가 뭐예요라고 묻는 초등학생 두 명.", "Two elementary school students who asked, “What is a local election?”"),
    ("친구들이 학교에서 먹는 급식을 좋은 우리 농산물로 만들어 무료로 먹게 할지, 친구들이 동네에서 마음껏 자전거를 탈 수 있게 자전거 도로를 만들지 결정할 사람을 뽑는 것이란 얘기에 아이들은 금세 고개를 끄덕였다.", "At the explanation that it is choosing the people who decide whether to make the school lunches your friends eat out of good Korean farm products and serve them free, or to make bicycle paths so that your friends can ride bicycles freely in the neighborhood, the children soon nodded."),
    ("그럼 집에 가서 부모님께 투표하시라고 할 거예요?", "“Then will you go home and tell your parents to vote?”"),
    ("라고 묻자 키 큰 친구가 네. 한다.", "When I asked, the tall one said, “Yes.”"),
    ("작은 친구도 질세라 전 커서도 꼭 투표할 거예요. 라고 약속했다.", "Not to be outdone, the small one also promised, “I will be sure to vote even when I grow up.”"),
]
_NAT7 = [
    ("유월 이 일 지방선거에서는 한국에서 첫 투표를 하는 외국인 귀화자들도 많다.", "In the June 2 local election there are many naturalized foreigners voting for the first time in Korea."),
    ("이들은 유권자나 후보자로서 한 표를 행사함으로써 완전한 한국인이 된다는 설렘이 크고, 후보들의 다문화와 복지 공약을 챙기는 열의도 누구 못지않았다.", "They feel great excitement about becoming “complete Koreans” by casting a vote as voters or candidates, and their enthusiasm for checking candidates’ multicultural and welfare pledges was second to none."),
    ("스리랑카 출신으로 지난해 귀화한 이레샤는 현재 결혼이민자 여성평등찾기 활동가로 일하고 있다.", "Iresha, from Sri Lanka, who was naturalized last year, now works as an activist for a group seeking equality for women marriage immigrants."),
    ("그는 한국 사회는 이민자들에 대한 배려가 부족하다며 이번 선거도 한국말이 서툰 사람들이 복잡한 투표과정을 어떻게 이해할 수 있겠냐고 지적했다.", "She pointed out that Korean society lacks consideration for immigrants and that, in this election too, people who are poor at Korean can hardly understand the complicated voting process."),
    ("그는 유권자연대활동을 통해 다문화인들을 챙겨 주고 배려하는 후보가 선출되도록 노력할 것이라고 말했다.", "She said that through voters’ solidarity activities she will work so that candidates who look after and consider multicultural people are elected."),
    ("공약을 갖고 정치에 직접 뛰어든 귀화인들도 많다.", "There are also many naturalized people who have jumped directly into politics with pledges."),
    ("국민참여당 충북도 광역의원 비례대표 일 순위 후보인 몽골 출신 체체 그수렌은 아이들이 편견 없이 자랄 수 있는 사회를 만들 것이라고 말했다.", "Tsetseg Gsuren, from Mongolia, the first-ranked proportional representation candidate for the Chungbuk provincial council of the Citizens’ Participation Party, said that she will create a society where children can grow up without prejudice."),
    ("그는 평소 이주여성의 자녀들이 피부색이나 생김새 때문에 차별받는 것을 보고 직접 나서 바꿔야겠다는 생각을 하게 됐다고 한다.", "She is said to have come to think that she must step forward and change things herself after seeing children of immigrant women being discriminated against because of skin color or looks."),
    ("그수렌은 당선되면 다문화 아동센터 건립을 적극 추진할 계획이다.", "If elected, Gsuren plans to actively push for the building of a multicultural children’s center."),
    ("한나라당 대전시 광역의원 비례대표 삼 순위 후보인 태국 출신의 센위안 낫티타는 결혼 이민자들에게도 요리학원과 미용학원 등의 국비지원 강습 혜택이 돌아갈 수 있도록 하겠다는 계획을 밝혔다.", "Senwian Natthita, from Thailand, the third-ranked proportional representation candidate for the Daejeon city council of the Grand National Party, announced a plan to make sure that marriage immigrants too can receive the benefit of state-funded courses such as at cooking and beauty academies."),
    ("이주여성들이 자격증 취득 단계부터 벽에 부딪히는 현실을 바꿔 보려는 것이다.", "She wants to change the reality that immigrant women run into a wall from the stage of obtaining a license."),
]
_SPEAK7C = [("미국의 선거, 즉 대통령 선거, 주지사 선거, 의원 선거 등의 투표율을 높이기 위한 캠페인을 하려고 합니다.", "We are going to run a campaign to raise the turnout in American elections, that is, presidential, governor and legislator elections."), ("각자 준비해서 반 친구들에게 투표를 꼭 해야 하는 이유를 설명해 주세요.", "Each of you prepare and explain to your classmates why you must vote.")]
L6 = lesson(
    "U18 L7 · Part 3 (심화 학습): a free-hug vote appeal and naturalized candidates",
    "심화 학습 · 프리허그 · 풀뿌리 시민단체 · 지방선거 · 귀화자 · 다문화 · 비례대표 · 공약 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: a reader’s column on a free-hug campaign (Hankyoreh)", "The book asks two questions: what the article is about (four choices, A. a campaign to promote voter participation; B. an event to teach elementary school students about election rules; C. the election campaign for a candidate who wants to protect the environment; D. conducting exit polls) and what two examples the writer uses to explain a local election to the elementary school students. The writer is an unnamed member; the exclamation marks became periods and the quotation marks are dropped, so the dialogue is shown with my quotation marks in the English only. The column, with my English:", examples=passage(_HUG7)),
        card("My answers to 학습활동 1", "1. A: a campaign to promote voter participation (free hugs from residents who promise to vote). 2. The two examples: choosing the people who decide whether school lunches will be made from good Korean farm products and served free, and whether bicycle paths will be built so friends can ride freely in the neighborhood."),
        card("학습활동 2: a news article on naturalized voters and candidates (Kyunghyang and Hankyoreh)", "The book asks three questions in English: the phrase that refers to 완전한 한국인 (underlined in the first paragraph; the underline is not marked in the text); the issue the woman in the second paragraph raised; and a table of the national origin and policy of the two candidates. The women’s names are as printed in the article (people who gave published interviews or stood as candidates); the ages and genders in parentheses are dropped, and the numerals spelled in Hangul. The article, with my English:", examples=passage(_NAT7)),
        card("My answers to 학습활동 2", "1. The phrase that refers to it is 한 표를 행사함으로써 (by casting a vote, as voters or candidates): casting one’s vote makes one feel a complete Korean (my reading, since the underline is not shown). 2. She said that Korean society lacks consideration for immigrants and that people poor at Korean cannot easily understand the complicated voting process. 3. 체체 그수렌: from Mongolia; she plans to push for a multicultural children’s center so that children can grow up without prejudice. 센위안 낫티타: from Thailand; she plans to extend state-funded courses such as cooking and beauty academies to marriage immigrants."),
        card("말해 봅시다! (speaking)", "The book’s prompt, with its parentheses turned into “즉” (the English is mine):", examples=passage(_SPEAK7C)),
        card("Activities left out", "학습활동 3 (Listening, tracks 013 and 014): a YTN interview on a recently passed law (about voting rights of Koreans living abroad): the details of the law; a table of the expectations and concerns of Koreans abroad; why some people in Korea criticize it; and the three reasons the interviewee uses to refute the criticism. It is audio."),
    ],
    exercises=uniq(
        _tr(_HUG7[:12], k=3) + _tr(_NAT7, k=3) + _tr(_SPEAK7C, k=2)
        + [M("What is the column about?", "A campaign to promote voter participation", ["A teaching event on election rules", "A candidate’s campaign", "Exit polls"], "Free hugs for voters."), M("What did the elementary school students promise?", "To tell their parents to vote and to vote themselves when they grow up", ["To join the civic group", "To run for office", "To make posters"], "투표할 거예요."), M("Which country does Tsetseg Gsuren come from?", "Mongolia", ["Thailand", "Sri Lanka", "China"], "몽골 출신."), M("Which country does Senwian Natthita come from?", "Thailand", ["Mongolia", "Sri Lanka", "Vietnam"], "태국 출신."), M("What does Gsuren plan to push for if elected?", "A multicultural children’s center", ["A cooking academy", "A voting-rights law", "A new airport"], "다문화 아동센터."), M("What did the activist from Sri Lanka criticize?", "The lack of consideration for immigrants in the voting process", ["The high cost of voting", "Too many candidates", "Election-day holidays"], "배려가 부족.")]
        + [F("프리허그로 주민들의 투표 참여를 ___하다. (to appeal)", "호소", ["귀화", "추산"], "호소하다."), F("한 표를 ___함으로써 완전한 한국인이 된다. (to exercise)", "행사", ["귀화", "창출"], "행사하다."), F("공약을 갖고 정치에 직접 ___든 귀화인들. (jumped in)", "뛰어", ["빠져", "넘어"], "뛰어들다."), F("아이들이 편견 없이 자랄 수 있는 ___를 만들 것이다. (society)", "사회", ["공약", "선거"], "사회.")]
        + [read_q("프리허그로 주민들의 투표 참여를 호소한다"), read_q("지방선거는 지역의 일꾼을 뽑는 선거다"), read_q("귀화자들도 유권자나 후보자로서 한 표를 행사한다"), read_q("각자 준비해서 반 친구들에게 투표를 꼭 해야 하는 이유를 설명해 주세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("고개를 끄덕이다", "to nod one’s head", "헌법재판소의 결정에 사람들은 모두 고개를 끄덕였습니다."),
        ("풀뿌리", "voluntarily organized; “grass roots”", "지방자치제를 통해 풀뿌리 민주주의가 실현되었습니다."),
        ("호소(하다)", "(呼訴) an appeal (to appeal)", "감정에 호소하지 말고 이성적으로 설명해 주세요."),
    ]),
    ("학습활동 2", [
        ("귀화(하다)", "(歸化) naturalization (to be naturalized)", "언제 미국 시민으로 귀화했습니까?", "귀화자, 귀화인"),
    ]),
    ("학습활동 3", [
        ("감개무량하다", "(感慨無量) to be deeply moved; to be filled with deep emotion", "십 년 만에 고국을 방문하니 정말 감개무량합니다."),
        ("권리를 누리다", "(權利) to enjoy one’s rights", "대안학교 아이들은 아이로서 누려야 할 권리를 누리며 공부를 하고 있습니다."),
        ("납세", "(納稅) a tax payment", "국민은 납세의 의무가 있습니다.", "세금 납부"),
        ("논쟁(하다)", "(論爭) a dispute; “discussion fight” (to argue)", "저는 그 사람과 논쟁하고 싶지 않아서 그냥 동의하는 척 했어요.", "언쟁, 논의"),
        ("대가", "(代價) a price; a cost", "제 실수의 대가가 너무 큽니다."),
        ("동포", "(同胞) a compatriot; a fellow countryman", "외국에서 동포를 만나면 아주 반갑습니다.", "교포"),
        ("부정선거", "(不正選擧) a rigged election; a fraudulent election", "시민들은 부정선거에 반대하는 시위를 벌였습니다."),
        ("분열", "(分裂) a division; a disunion", "그 사건 때문에 국민들의 의견이 분열되었습니다.", "화합"),
        ("소모적", "(消耗的) wasteful", "이런 소모적인 논쟁은 그만둡시다."),
        ("아시다시피", "as you know; as you are aware", "아시다시피 미국은 세계 최강국 아닙니까?"),
        ("어깨가 무겁다", "(idiom) to feel the weight (of something) on one’s shoulders; “the shoulder is heavy”", "이제 아빠가 되어서 어깨가 무겁습니다.", "부담되다, 부담스럽다"),
        ("우려(하다/되다)", "(憂慮) worry; anxiety (to worry/to be worried)", "직원들은 두 회사의 합병이 실직으로 이어질까 봐 우려하고 있습니다.", "걱정"),
        ("재외국민", "(在外國民) a Korean national living overseas; a Korean residing overseas; an expatriate", "올해부터 재외국민도 투표를 할 수 있다고 합니다."),
        ("참정권", "(參政權) suffrage; the right to vote", "언제부터 여성들에게 참정권이 주어졌습니까?"),
        ("헌법재판소", "(憲法裁判所) the Constitutional Court", ""),
    ]),
]
L7 = lesson(
    "U18 L7 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 고개를 끄덕이다 · 풀뿌리 · 호소 · 귀화 · 감개무량 · 권리를 누리다 · 납세 · 논쟁 · 대가 · 동포 · 부정선거 · 분열 · 소모적 · 아시다시피 · 어깨가 무겁다 · 우려 · 재외국민 · 참정권 · 헌법재판소",
    requires=[],
    cards=[card("A note on the Korean in this list", "동포 was glossed in Lesson 4 (Trade) of this Unit with a similar definition; here it lists 교포 as a related word. 분열 lists 화합 (harmony) as its counterpart; 납세 lists 세금 납부 as a similar phrase; 우려 lists 걱정. The book gives no example for 헌법재판소. The example of 감개무량하다 has 10년 in digits, which I spelled out (십 년).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=14, nread=12)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 7: Elections (선거)", [L1, L2, L3, L4, L5, L6, L7])

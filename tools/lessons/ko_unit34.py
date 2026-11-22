"""Unit 34: KBC Semester 1, Unit 7, Chapter 27 - Social Gatherings (친목 모임).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 7, Student's Edition (2022).
Audio, video clips, pictures, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 27 (meanings and examples are the book's; digits respelled)
_CV_SOC = [
    ("동문 / 동창", "(同門/同窓) an alumnus; “(people who enter) the same door”", "김 선생님과 박 선생님은 한국대학교 동문이에요. 이번 일요일에 음악과 동창회가 있어요."),
    ("모임", "a gathering; a get-together; a meeting", "오늘 고등학교 동창 모임이 있어요."),
    ("송년회", "(送年會) an end-of-year party; “good-bye old year meeting”", f"{month_ko(12)} {day_ko(31)}에 송년회를 합시다."),
    ("집들이", "a housewarming party (~하다: to have a housewarming party)", "대학교 동창이 다음 주 일요일에 집들이를 한대요."),
    ("친목회 / 친목 모임", "(親睦會) a social gathering (among friends or people with common background); “friendship and harmony meeting”", "다음 주에 고향 친구 친목회가 있어요."),
    ("~회", "(會) a gathering; a meeting; a convention; a party", "지난주에 중학교 동문회에 가서 친구들을 만났어요."),
    ("회관", "(會館) an assembly hall", "이번 친목모임은 강남회관에서 할 거예요."),
]
_CV_JOB = [
    ("과장", "(科長) a manager; “section chief”", "고모부가 인사과 과장으로 승진하셨어요."),
    ("동료", "(同僚) a peer; a co-worker; a colleague", "다음 주에는 직장 동료들과 회식이 있어요."),
    ("부서", "(部署) department", "저희 부서에는 직원이 아주 많아요."),
    ("부장", "(部長) a general manager; “department chief”", "우리 부장님은 늘 바쁘십니다."),
    ("사장", "(社長) the president of a company; “company chief”", "사장님은 회사를 대표하십니다."),
    ("선배", "(先輩) a senior person or elder in an organization; “front in the group” (see the Notes)", "김 선생님은 박 선생님의 대학 선배입니다."),
    ("승진", "(昇進) promotion; advancement (~하다/되다: to be promoted)", "김 과장님은 이번에 부장으로 승진하셨어요."),
    ("신입사원", "(新入社員) a new employee (of a company)", f"올해 들어온 신입사원은 모두 {counted(20)} 명입니다."),
    ("입사", "(入社) joining a company; “entering a company” (~하다: to join a company)", "저는 이 회사에 작년에 입사했습니다."),
    ("퇴직", "(退職) retirement; retiring from office; “off the job” (~하다: to retire)", f"아버지는 {sino(55)} 세에 퇴직하셨습니다."),
    ("회식", "(會食) a company lunch / dinner (~하다: to have a company lunch / dinner) (see the Cultural Notes)", "다음 주 금요일에 승진 축하 회식을 해요."),
    ("후배", "(後輩) a junior or younger person in an organization; “back in the group” (see the Notes)", f"박 선생님이 김 선생님보다 삼 년 후배이십니다."),
]
_CV_OTH = [
    ("걱정", "worry; concern (~하다/되다: to be worried; to be concerned)", "내일 시험이 있어서 걱정돼요."),
    ("~겸", "(兼) concurrently; as well as", "다음 모임은 친목회 겸 집들이니까 꼭 참석해 주세요."),
    ("고민", "(苦悶) worry; trouble (~하다/이다: to be torn over a decision/choice; to be conflicted)", "집들이 선물로 무엇을 사야 할지 고민이에요."),
    ("기대", "(期待) expectation; anticipation; looking forward to (~하다/되다: to expect / to be expected / to look forward to)", "다음 달에 유럽 여행을 가는데 아주 기대돼요."),
    ("기억", "(記憶) memory; recall; memorization (~하다/나다: to recall; to remember)", "중학교 동창들 얼굴이 기억나지 않습니다."),
    ("기회", "(機會) an opportunity; a chance", "회식은 동료들과 친해질 수 있는 기회예요."),
    ("-냡니다 / 냬요", "contracted form of an indirectly quoted question (see the grammar)", "김 일병이 언제 오냡니다. 오늘 몇 시에 집에 오냬요."),
    ("~달", "a month", "지난달에 새 집으로 이사 갔어요."),
    ("-답니다 / 대요", "contracted form of an indirectly quoted statement (see the grammar)", "관리 사무소는 여기서 멀답니다. 박 이병이 조금 늦게 온대요."),
    ("-랍니다 / 래요", "contracted form of an indirectly quoted command/request (see the grammar)", "퇴근 후 한양 식당에서 모이랍니다. 저녁 여섯 시까지 백화점 앞으로 오래요."),
    ("부인", "(婦人) (respectfully addressing someone’s) wife; Mrs. [title]", "김 선생님 부인께서는 어떤 일을 하세요?"),
    ("빠지다", "to be absent", "어제 말하기 수업에 누가 빠졌습니까?"),
    ("색다르다", "(色) to be unique; to be uncommon; to be unconventional", "색다른 경험을 하기 위해 내년에 아프리카에 가요."),
    ("세제", "(洗劑) detergent", "설거지할 때 주방 세제를 씁니다."),
    ("수첩", "(手帖) a pocketbook; “handbook”", "수첩에 날짜를 적어 두세요."),
    ("-아 / 어 버리다", "auxiliary verb implying that an action is completed and is irreversible or no longer available (see the grammar)", "어제 피곤해서 일찍 자 버렸어요."),
    ("약속", "(約束) an appointment; a promise (~하다: to make an appointment; to promise)", "이번 주말에는 친구하고 약속이 있어요."),
    ("연락", "(連絡) contact (~하다/되다: to contact; to get in touch with)", "한국에 오면 꼭 연락하세요."),
    ("연말", "(年末) the year-end; the end of the year", "연말에는 송년회, 친목회 등 모임이 참 많습니다."),
    ("-(으)ㄹ래(요)", "will; would like to; want to (see the grammar)", "오늘 저녁에 우리 집에 올래요?"),
    ("잊다", "to forget", "어제 친구와의 약속을 잊어버렸어요."),
    ("-잡니다 / 재요", "contracted form of an indirectly quoted suggestion (see the grammar)", "여자친구가 주말에 영화 보러 가잡니다. 친구들이 수업 후에 농구하재요."),
    ("장만하다", "to make a (major) purchase; to prepare; to come up with", "영수 씨는 지난달에 첫 차를 장만했어요. 돌잔치에 쓸 음식을 장만해야 해요."),
    ("적다", "to write down; to jot down", "공책 앞에 자기 이름을 적으세요."),
    ("최근", "(最近) recent; recently; “the most recent”", "최근에 집을 구입한 사람들이 많습니다."),
    ("추천", "(推薦) a recommendation (~하다/받다: to recommend / to be recommended)", "이 책을 학생들에게 추천하고 싶어요."),
    ("(학)과", "((學)科) a department; a course of study; a school subject", "저희 과에는 남학생이 많아요."),
    ("학번", "(學番) year of college entry; “class number”", "김소희 씨는 영어과 공칠 학번입니다."),
    ("화장지 / 휴지", "(化粧紙/休紙) toilet paper", "화장지를 아껴 씁시다."),
    ("환영", "(歡迎) a welcome (~하다: to welcome)", "미국에 오신 것을 환영합니다."),
]
_CV_SINO = [("선", "(先) pre-; before(hand); ahead; front", "선생님, 선배, 선약"), ("친", "(親) real; true; intimate; close; pro-; favoring", "친동생, 친부모님")]
_ALL = {r[0]: r for r in _CV_SOC + _CV_JOB + _CV_OTH + _CV_SINO}
_EXTRA = {"동문 / 동창": "an alumnus", "친목회 / 친목 모임": "a social gathering among friends", "화장지 / 휴지": "toilet paper", "-냡니다 / 냬요": "(contracted indirect question)", "-답니다 / 대요": "(contracted indirect statement)", "-랍니다 / 래요": "(contracted indirect command)", "-잡니다 / 재요": "(contracted indirect suggestion)",
          "-아 / 어 버리다": "(an action completed and irreversible)", "-(으)ㄹ래(요)": "will; would like to; want to", "(학)과": "a department; a course of study", "~겸": "concurrently; as well as", "~달": "a month", "~회": "a gathering; a meeting; a party",
          "송년회": "an end-of-year party", "집들이": "a housewarming party", "신입사원": "a new employee", "승진": "promotion", "입사": "joining a company", "퇴직": "retirement", "회식": "a company lunch / dinner", "걱정": "worry; concern", "고민": "worry; trouble", "기대": "expectation; anticipation", "기억": "memory; recall", "약속": "an appointment; a promise", "연락": "contact", "추천": "a recommendation", "환영": "a welcome", "부인": "someone’s wife; Mrs.", "색다르다": "to be unique; to be unconventional",
          "친구": "a friend", "친어머니": "one’s real mother", "친동생": "one’s real younger brother or sister", "친부모": "one’s real parents; one’s own parents", "친손자": "one’s own grandson; “real grandson”", "친할아버지": "one’s paternal grandfather; “real grandfather”", "친삼촌": "one’s paternal uncle; “real uncle”", "외할아버지": "one’s maternal grandfather", "외삼촌": "one’s maternal uncle", "친미": "pro-American", "친북": "pro-North Korean; “pro-North”",
          "선생님": "a teacher; Mr.; Mrs.; “[person] born ahead”", "선약": "a previous engagement; a previous appointment", "선례": "a precedent; “preceding example”", "선착": "first arrival; “beforehand” arrival", "선진국": "an advanced nation; “nation moving ahead”", "친목": "a social gathering; friendship",
          "동창회": "an alumni reunion", "동문회관": "an alumni hall", "선후배": "seniors and juniors", "세제나 화장지": "detergent or toilet paper", "신세대": "the new generation"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)

# ================================================================== L1: objectives, housewarming, 친 (親)
_CHIN = [("친구", "a friend"), ("친목회", "a social gathering"), ("친어머니", "one’s real mother"), ("친동생", "one’s real younger brother or sister (the book: “one’s real brother”)"), ("친부모", "one’s real parents; one’s own parents"), ("친손자", "one’s own grandson; “real grandson”"),
         ("친할아버지", "one’s paternal grandfather; “real grandfather”"), ("친삼촌", "one’s paternal uncle; “real uncle”"), ("외할아버지", "one’s maternal grandfather"), ("외삼촌", "one’s maternal uncle"), ("친미", "pro-American"), ("친북", "pro-North Korean; “pro-North”")]
_HW = [("세제", "detergent"), ("화장지", "toilet paper"), ("비누", "soap (the book’s related word of 세제)"), ("성냥", "matches (the cultural note says 성냥: matches; mine)")]
L1 = lesson(
    "Ch 27 · What the chapter teaches, the housewarming party and 친 (親)",
    "친목 모임 · 집들이 · 집들이 선물 · 친구 · 친어머니 · 친할아버지 · 외할아버지 · 친미",
    requires=[],
    cards=[
        card("What Chapter 27 teaches (친목 모임)",
             "Chapter 27, “Social Gatherings”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and talk about social events such as housewarming parties, company lunches/dinners, alumni reunions, and end-of-year parties; talk about organizing social events; and accept or decline an invitation to a social event.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; contracted forms for reported speech; –(으)ㄹ래(요) used to indicate a speaker’s intention or desire in casual situations; the auxiliary verb –아/어 버리다 used to imply a completed action; and the Sino-Korean syllables 친 (親) and 선 (先)."),
        card("Cultural note: the housewarming party (집들이)",
             "Koreans often host a housewarming party (집들이) to present their new home to their friends and relatives after getting married or moving. When invited to a housewarming party, Koreans have traditionally brought soaps, detergent, or matches as presents (집들이 선물). These gifts express hope that the new residents will become rich as quickly as detergent or soap bubbles up or a match lights. Though soaps and detergent remain favorite gift items, people today also bring home appliances or items necessary for a new home."),
        card("Sino-Korean in use: 친 (親)",
             "This Sino-Korean syllable means close or intimate (in relationship), as in 친구 (a friend), 친목회 (a social gathering). When the syllable comes before a kinship term, it means real or true, as in 친어머니 (one’s real mother), 친동생 (one’s real brother), 친부모 (one’s real parents; one’s own parents), and 친손자 (one’s own grandson; “real grandson”). This syllable is used to refer to a relative on one’s father’s side, as in 친할아버지 (one’s paternal grandfather; “real grandfather”) and 친삼촌 (one’s paternal uncle; “real uncle”). The syllable 외 is used to refer to a relative on one’s mother’s side, as in 외할아버지 (one’s maternal grandfather) and 외삼촌 (one’s maternal uncle). When the Sino-Korean syllable 친 comes before a non-kinship term, it normally means pro- or favoring, as in 친미 (pro-American) and 친북 (pro-North Korean; “pro-North”).",
             tables=[ktable(_CHIN)]),
        card("Activities left out", "The vocabulary builder (a PowerPoint presentation with pictures and sounds, Activities 1 and 2 on the SMART Board, the Sino-Korean presentation and Activity 3, the game “Taboo”) is a picture, computer and game activity."),
    ],
    exercises=uniq(
        _tr(_CHIN) + [M("What does 집들이 mean?", "a housewarming party", ["an alumni reunion", "a company dinner", "a wedding"], "집들이 = a housewarming party."), M("What did Koreans traditionally bring to a housewarming party?", "Soaps, detergent or matches", ["Flowers", "Rice", "Toys"], "The book’s cultural note."), M("What do these gifts express?", "Hope that the new residents will become rich as quickly as bubbles or a match", ["Hope for a quick move", "Hope for many guests", "Hope for good weather"], "As quickly as detergent bubbles up."),
                      M("What do people bring to a housewarming party today?", "Also appliances or items necessary for a new home", ["Only soap", "Nothing", "Only matches"], "The book’s cultural note."), M("What does 친 (親) mean before a kinship term?", "real; true", ["pro-", "former", "big"], "친어머니 = one’s real mother."), M("What does 친 (親) mean before a non-kinship term?", "pro-; favoring", ["real", "big", "close to home"], "친미 = pro-American."),
                      M("What do you call your paternal grandfather?", "친할아버지", ["외할아버지", "친삼촌", "외삼촌"], "친 = father’s side."), M("What do you call your maternal uncle?", "외삼촌", ["친삼촌", "친할아버지", "외할아버지"], "외 = mother’s side."),
                      F("저희 ___할아버지는 아버지의 아버지세요. (paternal)", "친", ["외", "조"], "친할아버지."), F("어머니의 아버지는 ___할아버지예요. (maternal)", "외", ["친", "큰"], "외할아버지."),
                      read_q("친구"), read_q("친목회"), read_q("친어머니"), read_q("친할아버지"), read_q("외삼촌")]
    ),
)

# ================================================================== L2: Topic A
_A_TXT = [
    ("한 달 전에 남편의 친구 가족이 새 아파트로 이사를 갔다.", "A month ago, my husband’s friend’s family moved to a new apartment."), ("그래서 이번 주 토요일에 집들이 겸 친목회를 한다.", "So this Saturday there will be a housewarming party and social gathering together."),
    ("남편들끼리는 한 달에 한 번 친목 모임을 해서 자주 만난다.", "The husbands have a social gathering once a month, so they often meet."), ("그렇지만, 부인들은 오랜만에 만나기 때문에 이번 주 토요일이 아주 기대된다.", "However, the wives meet after a long time, so I am really looking forward to this Saturday."),
    ("나는 그날 아침에 남편 친구 집에 가서 음식 만드는 것을 도와줄 거다.", "That morning I will go to my husband’s friend’s house and help make the food."),
    ("최근에 집을 장만하는 친구들이 많아졌다.", "Recently, many friends have bought homes."), ("그래서 집들이 갈 때마다 무슨 선물을 해야 할지 고민이다.", "So every time I go to a housewarming party, I worry about what gift I should give."), ("보통은 집들이에 세제나 화장지를 가지고 간다.", "Usually I take detergent or toilet paper to a housewarming party."),
    ("그렇지만, 이번에는 조금 색다른 선물을 해 주고 싶다.", "However, this time I want to give a somewhat unusual gift."), ("뭐가 좋을까?", "What would be good?"),
]
_A_WORDS = ["~겸", "고민", "기대", "~달", "모임", "부인", "색다르다", "세제", "장만하다", "집들이", "최근", "친목회 / 친목 모임", "추천", "화장지 / 휴지", "~회"]
_EMAIL = [("잘 있었니?", "How have you been?"), ("내가 지난달에 새 아파트로 이사 간 것 알지?", "You know I moved to a new apartment last month, right?"), ("다음 주 토요일 저녁 다섯 시에 우리 집에서 집들이 겸 친목회를 하려고 해.", "I am going to have a housewarming party and social gathering at my house next Saturday at five in the evening."),
          ("참, 집들이 선물로 무엇을 가져올까 고민하지 마.", "Oh, and don’t worry about what to bring as a housewarming gift."), ("세제도 많고 휴지도 많으니까 사오지 말고.", "I have lots of detergent and lots of toilet paper, so don’t buy any and bring it."), ("다음 주 토요일이 너무 기대된다.", "I am really looking forward to next Saturday."), ("참, 그날 올 수 있는지 없는지 미리 알려줘.", "Oh, and let me know in advance whether you can come that day or not.")]
_QA = [("집들이 선물 추천 바랍니다.", "Please recommend a housewarming gift. (the question’s title)"), ("다음 주 토요일에 아는 형이 집들이를 하는데요.", "Next Saturday a guy I know, an older brother figure, is having a housewarming party."), ("형은 삼 년 전에 결혼했고 육 개월쯤 된 아들이 하나 있습니다.", "He got married three years ago and has a son who is about six months old."),
       ("예전부터 저하고 아주 친한 형이어서 색다른 선물을 하고 싶어요.", "He has been very close to me for a long time, so I want to give an unusual gift."), ("그래서 무슨 선물을 해야 할지 고민입니다.", "So I am torn over what gift to give."), ("선물은 십만 원 정도로 생각하고 있습니다.", "I am thinking of about 100,000 won for the gift."),
       ("어떤 선물이 좋을지 추천해 주세요.", "Please recommend what kind of gift would be good."), ("선물을 구입할 수 있는 웹사이트도 알려주시면 고맙겠습니다.", "I would be grateful if you could also tell me a website where I can buy the gift.")]
L2 = lesson(
    "Ch 27 · Topic A: I will go to a housewarming party this Saturday",
    "이번 주 토요일에 집들이에 갈 거예요 · 집들이 겸 친목회 · 선물을 해야 할지 고민 · 색다른 선물",
    requires=[],
    cards=[
        card("Topic A: I will go to a housewarming party this Saturday (이번 주 토요일에 집들이에 갈 거예요)",
             "The following text is from a woman’s blog entry about a housewarming party. (The English is mine; the book gives none. The book’s footnote: In Chapter 22 you learned that –(으)ㄹ지 expresses an indirect question embedded in a sentence, as in 무엇을 해야 할지 모르겠다 (I don’t know what I should do).)",
             examples=passage(_A_TXT)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=[ktable(_rows(_A_WORDS))]),
        card("Follow-up 2 (Reading and Writing): an invitation to a housewarming party",
             "The e-mail is an invitation to your friend’s housewarming party. The book asks you to fill in the blanks with words from a box (정리, 세제, 고민, 기대, 휴지, 친목회, 새, 집들이; the answers may vary). The text below is the e-mail with the blanks filled (my answer key; the digit is spelled out; the e-mail address and the ellipsis are left out; the English is mine).",
             examples=passage(_EMAIL)),
        card("The blanks (mine)", "The blanks in order are 새, 집들이, 친목회, 고민, 세제, 휴지 and 기대; 정리 is the word left over.",
             tables=[table(["Blank", "Word"], [["내가 지난달에 ___ 아파트로 이사 간", "새"], ["우리 집에서 ___ 겸", "집들이"], ["집들이 겸 ___를 하려고 해", "친목회"], ["무엇을 가져올까 ___하지 마", "고민"], ["___도 많고", "세제"], ["___도 많으니까", "휴지"], ["다음 주 토요일이 너무 ___된다", "기대"]], say=[1])]),
        card("Activity 3 (Reading): a man’s concern about a housewarming present",
             "You read a man’s concerns about a housewarming present, posted on a website’s Q&A section, and fill in a table in English. The text is the book’s (3년 and 6개월 and 10만 원 are spelled out; the emoticon is left out); the English is mine.",
             examples=passage(_QA)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["Host of the housewarming party", "An older male friend (형) of the writer, who got married three years ago and has a six-month-old son"], ["His concern", "He does not know what housewarming gift to give; he wants something unusual"], ["Requests", "Recommend a gift (a budget of about 100,000 won) and tell him a website where he can buy it"]])]),
        card("Activities left out", "The SMART Board activity, the Korean sentences suggesting how the woman could address her concerns (Presentation Activity d), Follow-up 1 (a video clip of the TV sitcom 거침없이 하이킥 about a couple, and listening to three conversations of couples about the occasions they are going to attend), Activity 1 (a SMART Board activity), Activity 2 (listening to three conversations of a husband and wife about a housewarming party or a get-together) and the blogger suggestion cards of Activity 3 (in groups) are video, audio, computer and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not any(c in w for c in "~/")]))
        + _tr(_A_TXT + _EMAIL + _QA)
        + [M("When did the husband’s friend’s family move?", "A month ago", ["A year ago", "Yesterday", "Next week"], "한 달 전에."), M("What will they have this Saturday?", "A housewarming party and social gathering", ["A wedding", "A company dinner", "A reunion"], "집들이 겸 친목회."), M("How often do the husbands have a social gathering?", "Once a month", ["Once a week", "Once a year", "Every day"], "한 달에 한 번."), M("Why is the woman looking forward to Saturday?", "The wives are meeting after a long time", ["She will get a gift", "She will cook", "It is her birthday"], "오랜만에 만나기 때문에."),
           M("What will the woman do that morning?", "Help cook at her husband’s friend’s house", ["Go shopping", "Clean her house", "Visit her parents"], "음식 만드는 것을 도와줄 거다."), M("What does she worry about?", "What gift to give", ["What to wear", "What to cook", "What to say"], "무슨 선물을 해야 할지 고민."), M("What does she usually bring to a housewarming?", "Detergent or toilet paper", ["Flowers", "Wine", "Fruit"], "세제나 화장지."), M("What does she want to give this time?", "Something a little unusual", ["Money", "Another detergent", "A plant"], "색다른 선물."),
           M("In the e-mail, what time is the housewarming?", "Five in the evening next Saturday", ["Noon on Sunday", "Seven in the evening", "Ten in the morning"], "저녁 다섯 시."), M("What does the host say about gifts?", "Don’t bring detergent or toilet paper; the host has plenty", ["Bring money", "Bring food", "Bring flowers"], "세제도 많고 휴지도 많으니까."), M("What does the man in Activity 3 want?", "A recommendation for a housewarming gift of about 100,000 won", ["A restaurant", "A cheap gift", "A trip"], "추천 바랍니다."),
           F("그래서 집들이 갈 때마다 무슨 선물을 해야 ___ 고민이다. (what I should)", "할지", ["하는", "한"], "-(으)ㄹ지 = an indirect question."), F("부인들은 오랜만에 만나기 때문에 아주 ___된다. (looked forward to)", "기대", ["고민", "추천"], "기대되다."), F("최근에 집을 ___하는 친구들이 많아졌다. (buy)", "장만", ["이사", "추천"], "장만하다."), F("조금 ___ 선물을 해 주고 싶다. (unusual)", "색다른", ["평범한", "비싼"], "색다르다."),
           read_q("집들이 겸 친목회를 한다"), read_q("남편들끼리는 한 달에 한 번 친목 모임을 해서 자주 만난다"), read_q("부인들은 오랜만에 만나기 때문에"), read_q("집들이에 세제나 화장지를 가지고 간다"), read_q("색다른 선물을 해 주고 싶다")]
    ),
)

# ================================================================== L3: Topic B
_B_DLG = [
    ("주연", "마이클 씨, 이번 주 금요일에 다른 약속하지 마세요.", "Michael, don’t make any other appointment this Friday."),
    ("마이클", "왜요?", "Why?"), ("주연", "직원들 회식이 있대요.", "They say there is a company dinner for the staff."), ("마이클", "회식이요?", "A company dinner?"), ("주연", "네, 마이클 씨 입사를 환영하는 회식이래요.", "Yes, they say it is a dinner to welcome your joining the company."),
    ("마이클", "회식은 신입사원이 들어올 때만 해요?", "Do you have a company dinner only when a new employee comes in?"), ("주연", "아니요. 승진이나 퇴직할 때에도 해요.", "No. We also have one at a promotion or a retirement."),
    ("마이클", "아, 그렇군요! 그럼, 회식에는 우리 부서 직원들만 모이는 거예요?", "Oh, I see! Then is it only our department’s staff who gather at the dinner?"), ("주연", "네, 그런데 이번에는 사장님과 부장님도 참석하신대요.", "Yes, but this time they say the president and the general manager will also attend."),
    ("마이클", "저는 회식은 처음인데, 이런 모임에서는 주로 뭘 해요?", "It is my first company dinner; what do people mainly do at this kind of gathering?"), ("주연", "보통 음식점에 가서 식사하고, 그 후에 술집이나 노래방에 가요. 동료들과 음식도 먹고 편하게 이야기할 수 있는 기회예요.", "Usually we go to a restaurant and eat, and after that go to a bar or a karaoke room. It is an opportunity to eat with colleagues and talk comfortably."),
    ("마이클", "그럼 술을 마셔야 해요? 저는 술을 못 마셔요.", "Then do I have to drink alcohol? I can’t drink."), ("주연", "걱정하지 마세요. 이번에는 술 마시는 대신에 연극 보러 간대요.", "Don’t worry. This time they say they are going to see a play instead of drinking."),
    ("마이클", "그럼 좋아요. 주연 씨도 가시는 거죠?", "Then that’s good. You are going too, right, Juyeon?"), ("주연", "그럼요. 저는 그런 자리에는 빠지지 않아요.", "Of course. I don’t skip such occasions."),
]
_B_WORDS = ["걱정", "과장", "기회", "-냡니다 / 냬요", "-답니다 / 대요", "동료", "-랍니다 / 래요", "부서", "부장", "빠지다", "사장", "승진", "신입사원", "약속", "입사", "-잡니다 / 재요", "퇴직", "환영", "회식"]
_E1 = [("인사과 전 직원", "To all staff of the Personnel Department"), ("부서 회식", "Department dinner"), ("모레, 목요일 우리 부서 회식이 있습니다.", "The day after tomorrow, Thursday, there is our department’s dinner."), ("이번에 입사한 신입사원 강진영 씨를 환영하는 자리입니다.", "It is an occasion to welcome Mr. Kang Jinyeong, the new employee who joined this time."),
       ("회식은 저녁 일곱 시 반 회사 앞 서울 불고기 식당에서 할 예정입니다.", "The dinner is to be held at 7:30 in the evening at the Seoul Bulgogi restaurant in front of the company."), ("그리고 회식 후 이 차 장소는 지하철 역 앞 비엔나 커피숍입니다.", "And the second-round place after the dinner is the Vienna coffee shop in front of the subway station."),
       ("한 분도 빠지지 말고 참석해 주시기 바랍니다.", "Please attend, with not even one person missing."), ("김석원 대리 인사과", "Assistant Manager Kim Seokwon, Personnel Department (the phone number is left out)")]
_E2 = [("국내영업 일 부", "Domestic Sales Department 1"), ("박채원 씨 결혼 축하 회식", "Dinner to celebrate Ms. Park Chaewon’s wedding"), ("다음 주 토요일에 박채원 씨가 결혼합니다.", "Next Saturday, Ms. Park Chaewon is getting married."), ("그래서 다같이 결혼을 축하하는 자리를 마련하고자 합니다.", "So we would like to prepare an occasion for all to congratulate her marriage together."),
       ("내일 금요일 퇴근 후 일곱 시에 회사 앞 중국 식당 북경에서 모입니다.", "We gather tomorrow, Friday, at seven after leaving work at the Chinese restaurant Beijing in front of the company."), ("특히 박채원 씨 신랑 되실 분도 참석합니다.", "In particular, Ms. Park’s groom-to-be will also attend."), ("그리고 식사 후에는 다 같이 노래방에 가기로 했습니다.", "And after the meal we have decided to all go to a karaoke room together."),
       ("그럼, 오늘 하루도 수고하십시오.", "Well then, thank you for your hard work today as well."), ("영업 일 부 홍석민 대리", "Assistant Manager Hong Seokmin, Sales Department 1")]
_MATCH = [("새로 들어온 회사원", "신입사원"), ("회사에 들어감", "입사"), ("직원들끼리 함께 하는 식사", "회식"), ("같은 직장이나 같은 곳에서 일하는 사람", "동료"), ("회사를 대표하는 사람", "사장")]
_SURVEY = [("다음 주에 우리 부서 회식을 하려고 하는데 언제가 좋아요?", "I’m going to have our department’s dinner next week; when is good for you? (the book’s model)"), ("아무 때나 괜찮아요.", "Any time is fine."), ("이번 금요일은 약속이 있어요.", "I have an appointment this Friday."), ("회식 후에 이 차는 어디로 갈까요?", "Where shall we go for the second round after the dinner?"), ("노래방에 가요.", "Let’s go to a karaoke room."), ("저는 술이 약해서 술 마시러 가기 싫어요.", "I am weak with alcohol, so I don’t want to go drinking."), ("볼링장에 가요.", "Let’s go to a bowling alley.")]
L3 = lesson(
    "Ch 27 · Topic B: We have a company dinner this Friday (이번 주 금요일에 회식이 있습니다)",
    "이번 주 금요일에 회식이 있습니다 · 신입사원 · 승진 · 퇴직 · 입사를 환영 · 2차 · 노래방",
    requires=[],
    cards=[
        card("Topic B: We have a company dinner this Friday (이번 주 금요일에 회식이 있습니다)",
             "Ms. Juyeon Lee is talking with her new coworker, Michael Derstine, about their company dinner on Friday. (The English is mine; the book gives none.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The contracted reported speech forms of this dialog (–답니다/대요, –냡니다/냬요, –랍니다/래요, –잡니다/재요) are in the grammar lessons.", tables=[ktable(_rows(_B_WORDS))]),
        card("Cultural note: 회식",
             "회식 literally means “gathering and eating.” It refers to a company lunch or dinner at a restaurant. Korean companies or organizations often host and pay for these events because the culture places high value on human relationships, unity, and solidarity. The events are frequently held throughout the year for special occasions such as promotions, an employee’s retirement, and welcoming new employees. If 회식 is held after work, it often evolves into after-dinner activities, called 2차 (second round), 3차 (third round), and so forth. These after-dinner activities often involve entertainment and drinking at places like 노래방 (a karaoke bar). However, new activity trends like bowling, playing pool, and drinking tea have emerged.\n\n"
             "In recent years with the emergence of ‘work and life balance’ values - especially among young people, 회식 practices and after work entertainment culture have significantly decreased in Korea. The persistent Covid 19 pandemic and subsequent ‘work from home’ trend also contributed to the substantial social change around 회식 culture. Instead, an increasing number of people are pursuing their individual leisure activities after work."),
        card("Follow-up 2 (Reading): two company e-mails announcing a company dinner",
             "The book asks you to read the e-mails and fill in a table in English (occasion, date/time, first and second meeting place), and to translate two underlined sentences (the underlining is not in the text). The text is the book’s (the digits and the quotation marks around the names are left out); the English is mine.",
             examples=passage(_E1 + _E2)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["", "Occasion", "Date / time", "Meeting place, 1st", "Meeting place, 2nd"], [["E-mail 1", "Welcoming the new employee Kang Jinyeong", "The day after tomorrow, Thursday, 7:30 p.m.", "The Seoul Bulgogi restaurant in front of the company", "The Vienna coffee shop in front of the subway station"], ["E-mail 2", "Celebrating Park Chaewon’s wedding", "Tomorrow, Friday, 7 p.m. after work", "The Chinese restaurant Beijing in front of the company", "A karaoke room (노래방)"]])]),
        card("Activity 1 (Reading): match the descriptions with the words",
             "The book asks you to match each description in the left column with a word in the right column by drawing lines (사장, 입사, 신입사원, 동료, 회식). My answers:",
             tables=[table(["Description", "Word (mine)"], [[a, b] for a, b in _MATCH], say=[0, 1])]),
        card("Activity 4: the model survey questions",
             "You organize a company dinner and survey your colleagues (the day, the place, after-dinner activities). The book’s example expressions (the English is mine):",
             examples=passage(_SURVEY)),
        card("Activities left out", "The SMART Board activity, Follow-up 1 (listening to three conversations of coworkers about their upcoming dinner), Activity 2 (a company announcement, listening), Activity 3 (a video clip of the TV sitcom 거침없이 하이킥) and Activity 4 (a role-play survey and a flyer) are video, audio, computer and class activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not any(c in w for c in "-/")]))
        + _tr(_strip(_B_DLG) + _E1 + _E2 + _SURVEY, k=3)
        + [M("What is the company dinner for, this time?", "To welcome Michael’s joining the company", ["A promotion", "A retirement", "A wedding"], "마이클 씨 입사를 환영하는 회식."), M("When else is there a company dinner?", "At a promotion or a retirement", ["At a wedding", "At New Year", "Only for visitors"], "승진이나 퇴직할 때에도 해요."), M("Who attends this time besides the department staff?", "The president and the general manager", ["The customers", "The families", "A professor"], "사장님과 부장님도 참석하신대요."), M("What do people usually do after the meal?", "Go to a bar or a karaoke room", ["Go home", "Watch a movie", "Go shopping"], "술집이나 노래방에 가요."),
           M("What is Michael’s concern?", "He cannot drink alcohol", ["He has no money", "He is busy", "He doesn’t like the president"], "저는 술을 못 마셔요."), M("What will they do instead of drinking this time?", "See a play", ["Go to a karaoke room", "Go bowling", "Go home"], "연극 보러 간대요."), M("How does Juyeon feel about such occasions?", "She doesn’t skip them", ["She dislikes them", "She rarely goes", "She is afraid of them"], "빠지지 않아요."),
           M("What does 회식 literally mean?", "gathering and eating", ["gathering and drinking", "drinking and singing", "welcoming and parting"], "會食."), M("What is 2차?", "the second round", ["the first round", "the third round", "the end"], "2차 (second round)."), M("What has decreased in recent years?", "회식 practices and after-work entertainment culture", ["Wedding parties", "Holidays", "Travel"], "The book’s cultural note."),
           M("When is the dinner of the first e-mail?", "The day after tomorrow, Thursday, 7:30 p.m.", ["Tomorrow, Friday, 7 p.m.", "Next Saturday", "Tonight"], "모레, 목요일 저녁 일곱 시 반."), M("What is the occasion of the second e-mail?", "Celebrating a wedding", ["A welcome party", "A retirement", "A promotion"], "결혼 축하 회식."), M("Which word means “a new employee”?", "신입사원", ["사장", "동료", "부장"], "새로 들어온 회사원."), M("Which word means “the person who represents the company”?", "사장", ["부장", "과장", "동료"], "회사를 대표하는 사람."),
           F("마이클 씨 ___를 환영하는 회식이래요. (joining the company)", "입사", ["퇴직", "승진"], "입사 = joining a company."), F("회식은 승진이나 ___할 때에도 해요. (retirement)", "퇴직", ["입사", "결혼"], "퇴직하다 = to retire."), F("동료들과 편하게 이야기할 수 있는 ___예요. (opportunity)", "기회", ["약속", "걱정"], "기회 = an opportunity."), F("한 분도 ___ 말고 참석해 주시기 바랍니다. (absent)", "빠지지", ["빠진", "빠지는"], "빠지다 = to be absent."),
           read_q("이번 주 금요일에 다른 약속하지 마세요"), read_q("마이클 씨 입사를 환영하는 회식이래요"), read_q("승진이나 퇴직할 때에도 해요"), read_q("이번에는 사장님과 부장님도 참석하신대요"), read_q("술 마시는 대신에 연극 보러 간대요")]
    ),
)

# ================================================================== L4: Grammar A: contracted reported speech
def _decl(v):
    st = stem(v)
    l, vv, t = _K.decompose(st[-1])
    if t == "ㄹ":
        return st[:-1] + _K.compose(l, vv, "ㄴ") + "다"
    if t:
        return st + "는다"
    return st[:-1] + _K.compose(l, vv, "ㄴ") + "다"


def _cmd(v):
    st = stem(v)
    l, vv, t = _K.decompose(st[-1])
    return st + ("으라" if t and t != "ㄹ" else "라")


def _full(v, kind, stative=False):
    if kind == "stmt":
        return (stem(v) + "다" if stative else _decl(v)) + "고 합니다"
    if kind == "q":
        return stem(v) + "냐고 합니다"
    if kind == "cmd":
        return _cmd(v) + "고 합니다"
    return stem(v) + "자고 합니다"


def _ctr(v, kind, inf=False, stative=False):
    if kind == "stmt":
        b = (stem(v) + "다" if stative else _decl(v))[:-1]
        return b + ("대요" if inf else "답니다")
    if kind == "q":
        return stem(v) + ("냬요" if inf else "냡니다")
    if kind == "cmd":
        return _cmd(v)[:-1] + ("래요" if inf else "랍니다")
    return stem(v) + ("재요" if inf else "잡니다")


_RV = [("가다", "to go"), ("먹다", "to eat"), ("읽다", "to read"), ("오다", "to come"), ("공부하다", "to study"), ("마시다", "to drink"), ("만들다", "to make"), ("살다", "to live")]
_RS = [("좋다", "to be good"), ("바쁘다", "to be busy"), ("멀다", "to be far"), ("많다", "to be many")]
_RT = [("Statement", "-다고 합니다 → -답니다", "-다고 해(요) → -대(요)"), ("Question", "-냐고 합니다 → -냡니다", "-냐고 해(요) → -냬(요)"), ("Command / request", "-라고 합니다 → -랍니다", "-라고 해(요) → -래(요)"), ("Suggestion", "-자고 합니다 → -잡니다", "-자고 해(요) → -재(요)")]
_RX = [("김일병이 저한테 도서관에 간답니다. / 간대요.", "PFC Kim says (to me) [that] he is going to the library."), ("김일병이 저한테 어디 가냡니다. / 가냬요.", "PFC Kim asks (me) where I am going."), ("김일병이 저한테 도서관에 가랍니다. / 가래요.", "PFC Kim tells me to go to the library."), ("김일병이 저한테 도서관에 같이 가잡니다. / 가재요.", "PFC Kim suggests (to me) [that] we should go to the library together."),
       ("마크 씨는 군인이랍니다. / 이래요.", "[They] say [that] Mark is a serviceman."), ("민재 씨는 의사가 아니랍니다. / 아니래요.", "[They] say [that] Minjae is not a doctor.")]
_RXS = [("김일병이 저한테 도서관에 간답니다.", "PFC Kim says (to me) [that] he is going to the library."), ("김일병이 저한테 도서관에 간대요.", "PFC Kim says (to me) [that] he is going to the library."), ("김일병이 저한테 어디 가냡니다.", "PFC Kim asks (me) where I am going."), ("김일병이 저한테 어디 가냬요.", "PFC Kim asks (me) where I am going."), ("김일병이 저한테 도서관에 가랍니다.", "PFC Kim tells me to go to the library."), ("김일병이 저한테 도서관에 가래요.", "PFC Kim tells me to go to the library."), ("김일병이 저한테 도서관에 같이 가잡니다.", "PFC Kim suggests (to me) [that] we should go to the library together."), ("김일병이 저한테 도서관에 같이 가재요.", "PFC Kim suggests (to me) [that] we should go to the library together."),
        ("마크 씨는 군인이랍니다.", "[They] say [that] Mark is a serviceman."), ("마크 씨는 군인이래요.", "[They] say [that] Mark is a serviceman."), ("민재 씨는 의사가 아니랍니다.", "[They] say [that] Minjae is not a doctor."), ("민재 씨는 의사가 아니래요.", "[They] say [that] Minjae is not a doctor.")]
_FU1 = [("김 일병이 학교에 간다고 합니다.", "김 일병이 학교에 간답니다.", "PFC Kim says [that] he is going to school."), ("친구가 같이 공부하자고 해요.", "친구가 같이 공부하재요.", "My friend suggests (to me) [that] we should study together.")]
_TXT_A = [("지민아, 이번 일요일에 등산 가자.", "Jimin, let’s go hiking this Sunday. (Youngmee)"), ("좋아, 어디서 만날까?", "Good, where shall we meet? (Jimin)"), ("지하철 서울대 입구에서 만나자.", "Let’s meet at Seoul National University Station of the subway. (Youngmee)"), ("그래, 근데 뭘 준비해야 해?", "OK, but what should I prepare? (Jimin)"), ("점심하고 물만 준비해.", "Prepare only lunch and water. (Youngmee)"), ("알았어. 그럼 일요일에 보자.", "Got it. Then see you on Sunday. (Jimin)")]
_TXT_B = [("영미가 왜 전화했어?", "Why did Youngmee call? (Jimin’s mother)"), ("일요일에 등산 가재요.", "She says let’s go hiking on Sunday. (Jimin; my answer)"), ("어디서 만나?", "Where do you meet? (the mother)"), ("지하철 서울대 입구에서 만나재요.", "She says let’s meet at Seoul National University Station of the subway. (Jimin; my answer)"), ("뭘 준비해야 해?", "What do you have to prepare? (the mother)"), ("점심하고 물만 준비하래요.", "She says to prepare only lunch and water. (Jimin; my answer)")]
L4 = lesson(
    "Ch 27 · Grammar A: contracted forms of reported speech (-답니다, -냡니다, -랍니다, -잡니다)",
    "간답니다 · 간대요 · 가냡니다 · 가냬요 · 가랍니다 · 가래요 · 가잡니다 · 가재요 · 군인이랍니다",
    requires=[],
    cards=[
        card("Reported speech: contracted forms",
             "In Chapters 23 and 24, you learned about reported speech: –다고 하다 for statements, –냐고 하다 for questions, –라고 하다 for commands, and –자고 하다 for suggestions. In this lesson, you will learn the contracted forms of each. Contracted forms are used when speaking.",
             tables=[table(["Sentence type", "Formal speech", "Informal speech"], [list(r) for r in _RT])]),
        card("Examples", "The book’s examples (the English is the book’s). Note that 이라고 합니다 and 아니라고 합니다 are the full forms of 이랍니다 / 이래요 and 아니랍니다 / 아니래요.", examples=passage(_RXS)),
        card("Forms (mine)", "The forms are made by the book’s rule. In the full form a statement of an action verb ends in -ㄴ다 / -는다 (the ㄹ stems drop ㄹ: 만들다 → 만든다고), a command in -(으)라고 and a suggestion in -자고.",
             tables=[table(["Verb", "Meaning", "Statement: full", "-답니다 / -대요"], [[v, m, _full(v, "stmt"), _ctr(v, "stmt") + " / " + _ctr(v, "stmt", True)] for v, m in _RV], say=[0, 2]), table(["Verb", "Meaning", "Question: full", "-냡니다 / -냬요"], [[v, m, _full(v, "q"), _ctr(v, "q") + " / " + _ctr(v, "q", True)] for v, m in _RV], say=[0, 2]),
                     table(["Verb", "Meaning", "Command: full", "-랍니다 / -래요"], [[v, m, _full(v, "cmd"), _ctr(v, "cmd") + " / " + _ctr(v, "cmd", True)] for v, m in _RV], say=[0, 2]), table(["Verb", "Meaning", "Suggestion: full", "-잡니다 / -재요"], [[v, m, _full(v, "sug"), _ctr(v, "sug") + " / " + _ctr(v, "sug", True)] for v, m in _RV], say=[0, 2]),
                     table(["Stative verb", "Meaning", "Statement: full", "-답니다 / -대요"], [[v, m, _full(v, "stmt", True), _ctr(v, "stmt", False, True) + " / " + _ctr(v, "stmt", True, True)] for v, m in _RS], say=[0, 2])]),
        card("Follow-up 1: the model", "Partner A reads a full-form reported speech sentence; Partner B changes it into the contracted form and translates it into English. The book’s two models:",
             tables=[table(["Full form", "Contracted form", "Meaning"], [list(r) for r in _FU1], say=[0, 1])]),
        card("Follow-up 3 (Reading and Writing): a phone conversation retold",
             "Text A is the transcription of a phone conversation in which two friends, Youngmee and Jimin, arrange a meeting on the weekend. Text B is the conversation in which Jimin tells her mother about it; the book asks you to complete Text B by reporting Youngmee’s speech with the appropriate contracted form. The text is the book’s (the blanks are my answers); the English is mine.",
             examples=passage(_TXT_A + _TXT_B)),
        card("Activities left out", "Follow-up 1’s sentence lists A and B (a partner activity), Follow-up 2 (listening to four conversations and transcribing the full-form reported speech), Follow-up 4 (김 상병이 같이 등산 가잡니다: writing a statement, a question, a command and a suggestion on index cards in groups) are audio, partner and group activities."),
    ],
    exercises=uniq(
        [M(f"Contract {_full(v, 'stmt')} (statement, formal):", _ctr(v, "stmt"), [_ctr(v, "q"), _ctr(v, "cmd"), _ctr(v, "sug")], f"{_full(v, 'stmt')} → {_ctr(v, 'stmt')}.") for v, m in _RV]
        + [M(f"Contract {_full(v, 'stmt')} (statement, informal):", _ctr(v, "stmt", True), [_ctr(v, "q", True), _ctr(v, "cmd", True), _ctr(v, "sug", True)], f"→ {_ctr(v, 'stmt', True)}.") for v, m in _RV[:6]]
        + [M(f"Contract {_full(v, 'q')} (question, formal):", _ctr(v, "q"), [_ctr(v, "stmt"), _ctr(v, "cmd"), _ctr(v, "sug")], f"→ {_ctr(v, 'q')}.") for v, m in _RV]
        + [M(f"Contract {_full(v, 'cmd')} (command, formal):", _ctr(v, "cmd"), [_ctr(v, "stmt"), _ctr(v, "q"), _ctr(v, "sug")], f"→ {_ctr(v, 'cmd')}.") for v, m in _RV]
        + [M(f"Contract {_full(v, 'sug')} (suggestion, informal):", _ctr(v, "sug", True), [_ctr(v, "stmt", True), _ctr(v, "q", True), _ctr(v, "cmd", True)], f"→ {_ctr(v, 'sug', True)}.") for v, m in _RV]
        + [M(f"Contract {_full(v, 'stmt', True)} (statement of a stative verb):", _ctr(v, "stmt", False, True), [_ctr(v, "q"), _ctr(v, "cmd"), _ctr(v, "sug")], f"→ {_ctr(v, 'stmt', False, True)}.") for v, m in _RS]
        + _tr(_RXS + [(a, c) for a, b, c in _FU1] + _TXT_B[1::2], k=3)
        + [M("Which ending is the contracted form of a reported statement?", "-답니다 / -대요", ["-냡니다 / -냬요", "-랍니다 / -래요", "-잡니다 / -재요"], "-다고 합니다 → -답니다."), M("Which ending is the contracted form of a reported question?", "-냡니다 / -냬요", ["-답니다 / -대요", "-랍니다 / -래요", "-잡니다 / -재요"], "-냐고 합니다 → -냡니다."), M("Which ending is the contracted form of a reported command?", "-랍니다 / -래요", ["-답니다 / -대요", "-냡니다 / -냬요", "-잡니다 / -재요"], "-라고 합니다 → -랍니다."), M("Which ending is the contracted form of a reported suggestion?", "-잡니다 / -재요", ["-답니다 / -대요", "-냡니다 / -냬요", "-랍니다 / -래요"], "-자고 합니다 → -잡니다."),
           M("What is the contracted form of 이라고 합니다?", "이랍니다 / 이래요", ["이답니다", "이잡니다", "이냡니다"], "이랍니다."), M("What is the contracted form of 아니라고 합니다?", "아니랍니다 / 아니래요", ["아니답니다", "아니잡니다", "아니냡니다"], "아니랍니다."), M("When are the contracted forms used?", "In speaking", ["In formal writing", "Only in the news", "Only in letters"], "Contracted forms are used when speaking."),
           F("김일병이 저한테 도서관에 같이 ___. (suggests, informal)", "가재요", ["가래요", "간대요"], "가자고 해요 → 가재요."), F("김일병이 저한테 어디 ___. (asks, formal)", "가냡니다", ["갑니다", "가랍니다"], "가냐고 합니다 → 가냡니다."), F("마크 씨는 군인___. (they say, formal)", "이랍니다", ["이잡니다", "이냡니다"], "이라고 합니다 → 이랍니다."), F("영미가 일요일에 등산 ___. (suggests, informal)", "가재요", ["가래요", "가냬요"], "가자고 해요."),
           read_q("간답니다"), read_q("가냬요"), read_q("가랍니다"), read_q("가재요"), read_q("군인이랍니다")]
    ),
)

# ================================================================== L5: Topic C
_C_DLG = [
    ("혜정", "태민아, 오랜만이야. 어떻게 지내?", "Taemin, it’s been a long time. How are you?"), ("태민", "어, 잘 지내. 너는?", "Oh, I’m doing well. And you?"), ("혜정", "응, 나도. 참, 너 오지훈 선배 기억해?", "Yes, me too. Oh, do you remember senior Oh Jihun?"),
    ("태민", "그럼. 그 선배가 우리 후배들하고 친했잖아. 근데 왜?", "Of course. That senior was close to us juniors, you know. But why?"), ("혜정", "어, 그 선배하고 십칠 학번 조수영하고 얼마 전에 결혼했대.", "Oh, they say that senior and Jo Suyeong of the class of 17 got married a little while ago."),
    ("태민", "그래? 우리 과 커플이 또 나왔네!", "Really? Another couple from our department has come out!"), ("혜정", "응. 다음 동창회에 둘이 같이 나온대.", "Yes. They say the two will come out together to the next alumni reunion."), ("태민", "그래? 이번 모임은 연말에 있지?", "Really? This gathering is at the end of the year, right?"),
    ("혜정", "응. 그래서 동창회 겸 송년회를 같이 한대.", "Yes. So they say the alumni reunion and the end-of-year party will be held together."), ("태민", "그럼, 장소는 어디야?", "Then where is the place?"), ("혜정", "우리 학교 동문 회관에서 하기로 했어.", "They decided to hold it at our school’s alumni hall."),
    ("태민", "그래? 잊어 버리기 전에 수첩에 적어 둬야겠다.", "Really? I have to write it in my notebook before I forget."), ("혜정", "참, 다른 동창들한테는 네가 연락 좀 해 줄래? 송년 모임에 꼭 참석하라고 해 줘.", "Oh, will you contact the other alumni? Tell them to be sure to attend the end-of-year gathering."), ("태민", "그래, 알았어.", "OK, got it."),
]
_C_WORDS = ["기억", "동문 / 동창", "선배", "송년회", "수첩", "-아 / 어 버리다", "연락", "연말", "-(으)ㄹ래(요)", "잊다", "적다", "(학)과", "학번", "회관", "후배"]
_SEN = [("선생님", "a teacher; Mr.; Mrs.; “[person] born ahead”"), ("선약", "a previous engagement; a previous appointment"), ("선례", "a precedent; “preceding example”"), ("선착", "first arrival; “beforehand” arrival"), ("선진국", "an advanced nation; “nation moving ahead”")]
_INVR = [("일시 올해 연말 마지막 토요일", "Date and time: the last Saturday of the end of this year"), ("시간 오후 여섯 시부터", "Time: from 6 p.m."), ("장소 한국대학교 동문회관", "Place: Hankuk University alumni hall"), ("선생님들과 선후배들을 모시고 동창회를 합니다.", "We hold the alumni reunion, inviting our teachers and seniors and juniors."),
         ("스포츠댄스 배우기와 노래 대회 등 다양한 행사가 준비되어 있습니다.", "Various events, such as learning sport dance and a singing contest, are prepared."), ("동창들 주소와 전화번호가 있는 동창회 수첩을 드립니다.", "We give you an alumni handbook with the alumni’s addresses and phone numbers."), ("가능하면 꼭 참석해 주세요.", "If possible, please be sure to attend."), ("삼십 회 동창회장 김윤철", "Kim Yuncheol, chairman of the 30th class’s alumni association")]
_ART = [("한국대학교 총동창회는 이번 달 이십삼 일 동창회를 했다.", "The Hankuk University General Alumni Association held its reunion on the 23rd of this month."), ("이번 동창회는 이십삼 일 오전 아홉 시 한국대학교 동문회관에서 열렸다.", "This reunion was held on the 23rd at nine in the morning at the Hankuk University alumni hall."), ("오후에는 선후배가 함께 배구대회와 탁구대회, 달리기대회를 했다.", "In the afternoon, seniors and juniors together held a volleyball contest, a table tennis contest and a running contest."),
        ("그리고 이십삼 일 저녁에는 백오십여 명의 동문들이 참석해 노래 대회와 게임 등으로 즐거운 시간을 보냈다.", "And on the evening of the 23rd, about 150 alumni attended and had a good time with a singing contest, games and so on.")]
L5 = lesson(
    "Ch 27 · Topic C: We will have the alumni reunion and end-of-year party together",
    "동창회 겸 송년회를 같이 할 거야 · 선배 · 후배 · 학번 · 동문회관 · 선 (先) · 동창회",
    requires=[],
    cards=[
        card("Topic C: We will have the alumni reunion and end-of-year party together (동창회 겸 송년회를 같이 할 거야)",
             "Two friends who have not seen each other since they graduated from college are having a conversation at a reunion. (The English is mine; the book gives none. The book’s footnotes: 학번 literally means “class number.” 학번 is a label assigned to each class. It consists of the two digits of the year in which the students in the class entered college; this designator is used for college only, not for high school. Since 네가 and 내가 have almost the same pronunciation, people often pronounce 네가 as 니가 to make it less confusing. The book writes 17학번; it is spelled out here.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The grammar items –(으)ㄹ래(요) and –아/어 버리다 are in the grammar lessons.", tables=[ktable(_rows(_C_WORDS))]),
        card("Notes: 선배와 후배",
             "선배 (先輩) literally means “(person who is) front in a group” and 후배 (後輩) means “(person who is) back in a group.” 선배 refers to a person who is senior or an elder in an organization, whereas 후배 refers to a person who is junior or younger in an organization. In Korea, if someone in the same social group (school, company, club, etc.) is senior to you in starting date or experience, he becomes your 선배, and you address the person as 선배(님), as in 김 선배(님), 박 선배(님), etc. You may call the person 형, 오빠, 누나, or 언니 if you share a closer relationship. Someone in the same group who is junior to you is your 후배, and you use the person’s first name."),
        card("Sino-Korean in use: 선 (先)",
             "This Sino-Korean syllable means before(hand), ahead, or front, as in 선생님 (a teacher; Mr.; Mrs.; “[person] born ahead”), 선약 (a previous engagement; a previous appointment), 선례 (a precedent; “preceding example”), 선착 (first arrival; “beforehand” arrival), and 선진국 (an advanced nation; “nation moving ahead”).",
             tables=[ktable(_SEN)]),
        card("Follow-up 1 (Reading): an invitation to a reunion",
             "The book asks you to read the invitation and fill in a table in English (time and location of the reunion, what will be provided, planned activities). The text is the book’s (the digits are spelled out; the bullets are left out); the English is mine.",
             examples=passage(_INVR)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Time and location of the reunion", "What will be provided", "Planned activities"], [["The last Saturday of the end of this year, from 6 p.m., at the Hankuk University alumni hall", "An alumni handbook with the alumni’s addresses and phone numbers", "Learning sport dance, a singing contest and other events"]])]),
        card("Activity 2 (Reading): a newspaper article about an alumni reunion",
             "The text is from a local newspaper; the book asks you to answer in English what the article is about and what events were held in the afternoon and in the evening. The text is the book’s (the digits are spelled out; the dot in 선·후배 is left out); the English is mine. The book glosses 총: total, all-out; 열리다: to be held.",
             examples=passage(_ART)),
        card("The answers (mine)", "The book leaves the answers blank; these are my answers.",
             tables=[table(["Question", "Answer (mine)"], [["What is this article about?", "The reunion of the Hankuk University General Alumni Association, held on the 23rd of the month"], ["Afternoon", "Seniors and juniors together held a volleyball contest, a table tennis contest and a running contest"], ["Evening", "About 150 alumni attended a singing contest and games"]])]),
        card("Activities left out", "The SMART Board activity and the sentence-strip activity of the Presentation Activity (sorting and arranging a conversation in pairs), Follow-up 2 (listening to three invitations to a reunion and noting the reasons for not attending), Activity 1 (a SMART Board activity), Activity 3 (listening to three conversations about a social gathering) and Activity 4 (동창회 모임: a voice mail, listening, and making a flyer in pairs) are audio, computer and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not any(c in w for c in "-/(")]))
        + _tr(_strip(_C_DLG) + _SEN + _INVR + _ART, k=3)
        + [M("Who is Oh Jihun?", "A senior the two remember", ["A professor", "A junior", "A classmate"], "오지훈 선배."), M("What happened to Oh Jihun and Jo Suyeong?", "They got married a little while ago", ["They broke up", "They graduated", "They moved"], "얼마 전에 결혼했대."), M("When is the next gathering?", "At the end of the year", ["In spring", "In summer", "Next week"], "연말에."), M("What will they hold together?", "The alumni reunion and the end-of-year party", ["A wedding and a party", "A class and a trip", "A lunch and a game"], "동창회 겸 송년회."),
           M("Where will it be held?", "At the school’s alumni hall", ["At a hotel", "At a restaurant", "At the park"], "동문 회관에서."), M("What will Taemin do before he forgets?", "Write it in his notebook", ["Call a friend", "Buy a gift", "Send a letter"], "수첩에 적어 둬야겠다."), M("What does Hyejeong ask Taemin to do?", "Contact the other alumni", ["Cook the food", "Book the hall", "Pay the fee"], "다른 동창들한테는 네가 연락."), M("What does 학번 literally mean?", "class number", ["school name", "student ID", "entry fee"], "學番."),
           M("What does 선배 refer to?", "A senior person in an organization", ["A junior person", "A teacher only", "A boss only"], "선배 = senior."), M("What does 후배 refer to?", "A junior person in an organization", ["A senior person", "A teacher", "A boss"], "후배 = junior."), M("What do you call a closer 선배 (a male)?", "형 or 오빠, according to your sex", ["Teacher", "Mr.", "Boss"], "You may call the person 형, 오빠, 누나, or 언니."), M("What does 선 (先) mean?", "before(hand); ahead; front", ["real; true", "love", "after"], "선생님, 선약."),
           F("그 선배가 우리 ___들하고 친했잖아. (juniors)", "후배", ["선배", "동료"], "후배 = junior."), F("송년 모임에 꼭 ___하라고 해 줘. (attend)", "참석", ["입사", "승진"], "참석하다."), F("우리 학교 ___ 회관에서 하기로 했어. (alumni)", "동문", ["동료", "사장"], "동문 = alumnus."), F("동창회 ___ 송년회를 같이 한대. (as well as)", "겸", ["때문", "대신"], "~겸 = concurrently."),
           read_q("선배"), read_q("후배"), read_q("동창회 겸 송년회"), read_q("수첩에 적어 둬야겠다"), read_q("꼭 참석하라고 해 줘")]
    ),
)

# ================================================================== L6: Grammar B: -(으)ㄹ래(요)
_OV_L = {"돕다": "도울"}


def _lrae(v, yo=True):
    b = _OV_L.get(v, attr(v)[2])
    return b + "래" + ("요" if yo else "")


_LV = [("가다", "to go"), ("먹다", "to eat"), ("읽다", "to read"), ("오다", "to come"), ("하다", "to do"), ("마시다", "to drink"), ("시키다", "to order"), ("놀다", "to play"), ("돕다", "to help"), ("만들다", "to make"), ("보다", "to watch; to see"), ("기다리다", "to wait")]
_LEX = [("영미야, 뭐 시킬래?", "Youngmi, what would you like to order? (A, the mother)"), ("전 비빔밥 먹을래요. 엄마는요?", "I’ll have bibimbap. What about you, Mom? (B)"), ("난 김치찌개 먹을래.", "I’ll have kimchi stew. (A)"), ("저녁은 나중에 먹을래요?", "Will you eat dinner later?"), ("지금 먹을래요.", "I will have it now."),
        ("지현아, 내 숙제 좀 도와줄래?", "Would you help me with my homework?"), ("그래, 알았어.", "OK, I will."), ("오늘 저녁에 우리 집에 올래요?", "Would you like to come to my house this evening? (the core vocabulary’s example)")]
_LREC = [("저는 내년에 한국에 가겠어요.", "I will go to Korea next year."), ("저는 내년에 한국에 갈 거예요.", "I am going to go to Korea next year."), ("저는 내년에 한국에 가고 싶어요.", "I want to go to Korea next year.")]
_LFU = [("숙제는 나중에 하다", "숙제는 나중에 할래요.", "I’ll do the homework later."), ("점심은 일찍 먹다", "점심은 일찍 먹을래요.", "I’ll eat lunch early. (mine)"), ("주말에는 영화를 보다", "주말에는 영화를 볼래요.", "I’ll watch a movie on the weekend. (mine)"), ("커피를 마시다", "커피를 마실래요.", "I’ll drink coffee. (mine)"), ("친구를 기다리다", "친구를 기다릴래요.", "I’ll wait for my friend. (mine)")]
L6 = lesson(
    "Ch 27 · Grammar B: expressing a speaker’s intention or desire with -(으)ㄹ래(요)",
    "비빔밥 먹을래요 · 뭐 시킬래? · 지금 먹을래요 · 도와줄래? · 올래요?",
    requires=[],
    cards=[
        card("A. Expressing a speaker’s intention or desire in casual situations",
             "In earlier chapters, you learned how to express an intention or desire by using grammar features like –겠다, –(으)ㄹ 거다, and –고 싶다. For example:",
             examples=passage(_LREC)),
        card("The verb ending -(으)ㄹ래(요)",
             "In this lesson, you will learn the verb ending –(으)ㄹ래(요), which is used in casual conversation to express the speaker’s intention or desire. If used in a question, however, the verb ending indicates the listener’s intention or desire. Look at the following casual conversation between a mother and a daughter at a restaurant (the English is the book’s):",
             examples=passage(_LEX[:3])),
        card("Translation and use",
             "Note that the mother uses the verb ending –(으)ㄹ래 to ask what the daughter wants to order. The daughter uses the same verb ending plus 요 to express her own desire for 비빔밥. For this reason, –(으)ㄹ래 can be translated as will, would like to, or want to. Keep in mind that this verb ending works only with action verbs.",
             examples=passage(_LEX[3:5])),
        card("A request with -(으)ㄹ래", "The verb ending –(으)ㄹ래 can be also used when the speaker makes a request. For example:", examples=passage(_LEX[5:])),
        card("Forms (mine)", "The forms are made by the book’s rule: the future attributive form -(으)ㄹ (ㄹ stems keep it: 놀다 → 놀, 만들다 → 만들; the ㅂ irregular 돕다 → 도울) plus 래 (and 요 in polite speech).",
             tables=[table(["Verb", "Meaning", "-(으)ㄹ래", "-(으)ㄹ래요"], [[v, m, _lrae(v, False), _lrae(v)] for v, m in _LV], say=[0, 2, 3])]),
        card("Follow-up 1: the model and my sentences", "The book gives ten sentence strips, which are not in the text; its model, and my own sentences in the same pattern (the English is mine):",
             tables=[table(["Strip", "With -(으)ㄹ래(요)", "Meaning"], [list(r) for r in _LFU], say=[1])]),
        card("Activities left out", "Follow-up 1’s sentence strips (a partner activity) and Follow-up 2 (listening to three conversations between family members and noting what the female speaker wants) are audio and partner activities."),
    ],
    exercises=uniq(
        _fk(_LV, lambda v: _lrae(v), "-(으)ㄹ래요", lambda v: [attr(v)[0] + "래요", attr(v)[1] + "래요", stem(v) + "래요", attr(v)[2] + "게요"])
        + _fk(_LV, lambda v: _lrae(v, False), "-(으)ㄹ래 (casual)", lambda v: [attr(v)[0] + "래", stem(v) + "래", attr(v)[2] + "까", attr(v)[2] + "게"])
        + _tr(_LEX + _LREC + [(a + " → " + b, c) for a, b, c in _LFU[:1]], k=3)
        + [M("What does -(으)ㄹ래(요) express in a statement?", "The speaker’s intention or desire", ["A past action", "An order", "A reason"], "먹을래요 = I will have."), M("What does -(으)ㄹ래 express in a question?", "The listener’s intention or desire", ["The speaker’s past", "A prohibition", "A reason"], "뭐 시킬래? = what would you like to order?"), M("With which verbs does -(으)ㄹ래 work?", "Action verbs only", ["Stative verbs only", "All verbs", "Nouns"], "The book’s note."), M("What else can -(으)ㄹ래 express?", "A request", ["A promise to die", "A comparison", "A time"], "도와줄래? = would you help me?"),
           F("전 비빔밥 ___. (I’ll have, polite)", "먹을래요", ["먹겠래요", "먹는래요"], "먹다 → 먹을래요."), F("영미야, 뭐 ___? (would you like to order, casual)", "시킬래", ["시켜래", "시키는래"], "시키다 → 시킬래."), F("지현아, 내 숙제 좀 ___? (would you help)", "도와줄래", ["도와주는래", "도와줘래"], "도와주다 → 도와줄래."), F("숙제는 나중에 ___요. (I’ll do)", "할래", ["하래", "한래"], "하다 → 할래요."), F("오늘 저녁에 우리 집에 ___요? (would you like to come)", "올래", ["오래", "온래"], "오다 → 올래요."),
           read_q("비빔밥 먹을래요"), read_q("뭐 시킬래"), read_q("지금 먹을래요"), read_q("도와줄래"), read_q("우리 집에 올래요")]
    ),
)

# ================================================================== L7: Grammar C: -아/어 버리다
def _beo(v, form="past"):
    b = _base_ao(v)
    return b + " " + {"past": "버렸어요", "fut": "버릴 거예요", "pastcas": "버렸어"}[form]


_BV = [("먹다", "to eat"), ("쓰다", "to use; to spend"), ("자다", "to sleep"), ("사다", "to buy"), ("하다", "to do"), ("잊다", "to forget"), ("날아가다", "to fly away"), ("마시다", "to drink"), ("읽다", "to read"), ("가다", "to go")]
_BEX = [("동생이 내 피자를 먹었어요.", "My younger brother ate my pizza."), ("동생이 내 피자를 먹어 버렸어요.", "My younger brother ate my pizza (and it’s gone). / My younger brother ended up eating my pizza."), ("돈을 다 써 버렸어요.", "I used up the money (and I don’t have any money with me)."), ("새가 날아가 버렸어요.", "The bird flew away (and it is not here)."), ("숙제를 다 해 버릴 거예요.", "I will finish up my homework (and there will be no homework left to do)."),
        ("새 컴퓨터를 사 버렸어요.", "I ended up buying a new computer."), ("어제 피곤해서 일찍 자 버렸어요.", "I was tired yesterday, so I ended up going to sleep early. (the core vocabulary’s example)"), ("어제 친구와의 약속을 잊어버렸어요.", "I forgot my appointment with a friend yesterday. (the core vocabulary’s example)")]
_BRES = [("저는 월급을 받으면 금방 다 써 버려요.", "When I receive my salary, I use it all up right away. (A)"), ("그래서 신용카드 빚이 많아요.", "So I have a lot of credit card debt. (A)"), ("어떻게 하면 좋을까요?", "What should I do? (A)"), ("그럼, 이제부터 월급의 십 퍼센트씩 저축해 볼래요?", "Then, from now on, would you like to try saving ten percent of your salary each time? (B, the mentor)"), ("좋은 생각인 것 같아요.", "That seems like a good idea. (A)"), ("이제부턴 월급의 십 퍼센트씩 저축해 볼게요.", "From now on I will try saving ten percent of my salary each time. (A)")]
L7 = lesson(
    "Ch 27 · Grammar C: the auxiliary verb -아/어 버리다 implies a completed action",
    "먹어 버렸어요 · 써 버렸어요 · 날아가 버렸어요 · 해 버릴 거예요 · 사 버렸어요 · 잊어버렸어요",
    requires=[],
    cards=[
        card("B. The auxiliary verb -아/어 버리다",
             "So far you have learned auxiliary verbs that start with 아/어: –아/어 보다, as in 김치를 먹어보세요 (sense of experiment), and –아/어 주다, as in 문을 열어 주세요 (sense of service). All these auxiliary verbs add “flavor” to the main verb. Likewise, the auxiliary verb –아/어 버리다 adds “flavor” to the main verb. Because 버리다 in –아/어 버리다 means to throw away or discard, this auxiliary verb is used to imply that an action is completed and thus it is irreversible or no longer available. Compare the following two sentences:",
             examples=passage(_BEX[:2])),
        card("Meaning",
             "The verb in the first sentence is 먹었어요 (ate), and the speaker tells us that his younger brother ate his pizza. The verb in the second sentence ends with the auxiliary verb –아/어 버리다. The speaker implies that the action of his brother eating his pizza was completed and is irreversible. In a certain context, the sentence can imply that the speaker is upset that his pizza is gone. Look at the following sentences that use –아/어 버리다:",
             examples=passage(_BEX[2:6])),
        card("More examples", "From the core vocabulary:", examples=passage(_BEX[6:])),
        card("Forms (mine)", "The forms are made by the book’s rule: the -아/어 form of the main verb plus 버렸어요 (past) or 버릴 거예요 (future); 쓰다 → 써, 하다 → 해.",
             tables=[table(["Verb", "Meaning", "-아/어 버렸어요", "-아/어 버릴 거예요"], [[v, m, _beo(v), _beo(v, "fut")] for v, m in _BV], say=[0, 2, 3])]),
        card("Follow-up 3: the model", "Partner A reads a sentence; Partner B conjugates the verb using –아/어 버리다. The book’s model:", tables=[table(["A", "B"], [["일찍 잤어요.", "일찍 자 버렸어요."]], say=[0, 1])]),
        card("Follow-up 5: a mentor and a mentee", "It is the end of the year; you discuss habits you would like to change with a mentor, using –아/어 버리다 (the mentee), –(으)ㄹ래요 (the mentor’s advice) and –(으)ㄹ게요 (the mentee’s resolution). The book’s model (the digits are spelled out; the English is mine) and its first table row:", examples=passage(_BRES),
             tables=[table(["Action / habit to change", "Resolution"], [["spend all my money too quickly", "write down everything I spend money on"]])]),
        card("Activities left out", "Follow-up 3’s lists A (a partner activity), Follow-up 4 (listening to four conversations between family members and noting the action completed by the female speaker), Follow-up 5’s pair exchange (a partner activity) and Activity 1 (a SMART Board activity) are audio, computer and partner activities."),
    ],
    exercises=uniq(
        _fk(_BV, _beo, "-아/어 버렸어요", lambda v: [_base_ao(v) + " 보았어요", _base_ao(v) + " 주었어요", stem(v) + "어 버렸어요", past(v) + "어요"])
        + _fk(_BV, lambda v: _beo(v, "fut"), "-아/어 버릴 거예요", lambda v: [_beo(v), _base_ao(v) + " 볼 거예요", stem(v) + "어 버릴 거예요", _base_ao(v) + " 줄 거예요"])
        + _tr(_BEX + _BRES, k=3)
        + [M("What does 버리다 mean?", "to throw away; to discard", ["to try", "to give", "to see"], "버리다 = to throw away."), M("What does -아/어 버리다 imply?", "The action is completed and irreversible", ["The action is an experiment", "The action is a favor", "The action is a wish"], "먹어 버렸어요 = it’s gone."), M("What is the difference between 먹었어요 and 먹어 버렸어요?", "The second implies it is gone or irreversible", ["The second is more polite", "The second is a question", "There is no difference"], "The book’s comparison."), M("What can 동생이 내 피자를 먹어 버렸어요 imply about the speaker?", "He may be upset that the pizza is gone", ["He is full", "He is happy", "He will cook"], "The book’s note."),
           F("돈을 다 ___ 버렸어요. (used up)", "써", ["쓰어", "쓴"], "쓰다 → 써."), F("새가 날아___ 버렸어요. (away)", "가", ["간", "가고"], "날아가 버렸어요."), F("숙제를 다 ___ 버릴 거예요. (do)", "해", ["하", "한"], "하다 → 해."), F("새 컴퓨터를 ___ 버렸어요. (bought)", "사", ["산", "사는"], "사 버렸어요."), F("어제 피곤해서 일찍 자 ___어요. (ended up)", "버렸", ["버린", "버릴"], "버렸어요."),
           read_q("먹어 버렸어요"), read_q("돈을 다 써 버렸어요"), read_q("새가 날아가 버렸어요"), read_q("숙제를 다 해 버릴 거예요"), read_q("새 컴퓨터를 사 버렸어요")]
    ),
)

# ================================================================== L8: core vocabulary and self-evaluation
_CV_SECS = [("Social gatherings", _CV_SOC), ("Job-related words", _CV_JOB), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:-1] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if "-" not in r[0]]
    ns = [r for r in rows if "-" in r[0]]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L8 = lesson(
    "Ch 27 · Core vocabulary and self-evaluation",
    "주요 단어 · 친목 모임 · 직장 관련 단어 · 기타 단어 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. Where the book writes two forms together (for example 동문/동창 or 화장지/휴지), the forms are written with a slash.\n\n"
             "The example sentences with digits are respelled in Hangul (12월 31일 → 십이 월 삼십일 일, 20명 → 스무 명, 07학번 → 공칠 학번). The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and talk about social events such as housewarming parties, company lunches/dinners, alumni reunions, and end-of-year parties; talk about organizing social events; and accept or decline an invitation to a social event.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; contracted forms for reported speech; –(으)ㄹ래(요) used to indicate a speaker’s intention or desire in casual situations; the auxiliary verb –아/어 버리다 used to imply a completed action; and the Sino-Korean syllables 친 (親) and 선 (先)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What is the contracted form of -다고 합니다?", "-답니다", ["-냡니다", "-랍니다", "-잡니다"], "-다고 합니다 → -답니다."), M("What does -(으)ㄹ래(요) express?", "The speaker’s intention or desire", ["A past action", "A reason", "A comparison"], "먹을래요."), M("What does -아/어 버리다 imply?", "A completed, irreversible action", ["An experiment", "A favor", "A habit"], "먹어 버렸어요."),
           M("What is a 집들이?", "a housewarming party", ["an alumni reunion", "a company dinner", "a wedding"], "집들이."), M("What is a 송년회?", "an end-of-year party", ["a housewarming", "a wedding", "a company dinner"], "송년회."), M("What is a 회식?", "a company lunch / dinner", ["an alumni reunion", "a housewarming", "an end-of-year party"], "회식."), M("What is a 신입사원?", "a new employee", ["a boss", "a retiree", "a colleague"], "신입사원."), M("What is a 동료?", "a co-worker; a colleague", ["a boss", "a new employee", "a junior"], "동료."), M("What does 친 (親) mean before a kinship term?", "real; true", ["pro-", "close to", "before"], "친어머니."),
           F("다음 모임은 친목회 ___ 집들이니까 꼭 참석해 주세요. (as well as)", "겸", ["대신", "때문"], "~겸."), F("내일 시험이 있어서 ___돼요. (worried)", "걱정", ["기대", "연락"], "걱정되다."), F("한국에 오면 꼭 ___하세요. (contact me)", "연락", ["약속", "승진"], "연락하다."), F("미국에 오신 것을 ___합니다. (welcome)", "환영", ["승진", "추천"], "환영하다."),
           read_q("주요 단어"), read_q("집들이"), read_q("회식"), read_q("동창회"), read_q("송년회")]
    ),
)

UNIT = unit("Semester 1 · Unit 7 · Chapter 27: Social Gatherings (친목 모임)", [L1, L2, L3, L4, L5, L6, L7, L8])

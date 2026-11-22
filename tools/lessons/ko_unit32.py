"""Unit 32: KBC Semester 1, Unit 7, Chapter 25 - The Korean Family (한국의 가족).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 7, Student's Edition (2022).
Audio, video clips, pictures, SMART Board activities, games, role-plays, partner and class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 25 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_KIN = [
    ("대가족", "(大家族) an extended family; a large family; “big family”", "대가족이 함께 살면 문제도 많지만 재미도 있어요."),
    ("며느리 / 며느님", "a daughter-in-law (며느님 is the honorific form)", "박 선생님은 며느리가 셋 있습니다."),
    ("모녀", "(母女) mother and daughter", "그 집 모녀는 친구 같아요."),
    ("모자", "(母子) mother and son", "이 집 모자는 아주 비슷해요."),
    ("부녀", "(父女) father and daughter", "부녀가 똑같이 생겼어요."),
    ("부부", "(夫婦) husband and wife; a married couple", "부부가 취미 생활을 같이 하면 아주 좋아요."),
    ("부자", "(父子) father and son", "부자가 오랜만에 이야기를 많이 했어요."),
    ("사위", "a son-in-law", "김 선생님 장녀가 곧 결혼해서 사위가 생깁니다."),
    ("손녀", "(孫女) a granddaughter", "윤정희 할머니는 손녀만 셋이 있습니다."),
    ("손자", "(孫子) a grandson", "조부모님께서 손자를 돌봐주십니다."),
    ("시부모 / 시부모님", "(媤父母) a woman’s parents-in-law", "요즘은 시부모님을 모시고 사는 사람이 많지 않습니다."),
    ("시아버지 / 시아버님", "(媤) a woman’s father-in-law (시아버님 is the honorific form)", "박 선생님 시아버지는 큰아들 부부와 같이 살아요."),
    ("시어머니 / 시어머님", "(媤) a woman’s mother-in-law (시어머님 is the honorific form)", "저희 시어머니는 올해 환갑이십니다."),
    ("시집 / 시댁", "(媤宅) a married woman’s in-laws’ home; a woman’s husband’s family (시댁 is the honorific form)", "저희는 명절 때마다 시댁에 가요."),
    ("식구", "(食口) a family member; “mouth to feed”", "우리 집은 엄마, 아빠, 나, 식구가 모두 세 명입니다."),
    ("어른", "an adult; a senior person; an elder", "저희 집안 어른은 할아버지이십니다."),
    ("자녀", "(子女) sons and daughters; children", "김 선생님은 자녀가 어떻게 되십니까?"),
    ("장남", "(長男) the oldest son; “big man”", "김 선생님 댁은 장남이 부모님을 모시고 삽니다."),
    ("장녀", "(長女) the oldest daughter; “big woman”", "박 준위님 장녀는 의사입니다."),
    ("장모 / 장모님", "(丈母) a man’s mother-in-law", "저희 장모님이 우리 딸을 돌봐 주십니다."),
    ("장인", "(丈人) a man’s father-in-law", "저희 장인어른은 아주 젊으십니다."),
    ("조부모 / 조부모님", "(祖父母) grandparents", "저희 조부모님은 매일 아침 운동을 하십니다."),
    ("차남", "(次男) a second son", "이명수 씨 차남은 결혼했습니다."),
    ("차녀", "(次女) a second daughter", "임기영 교수님의 차녀 결혼식이 이번 일요일에 있습니다."),
    ("처가 / 처가댁", "(妻家宅) a man’s in-laws’ home; a man’s wife’s family (처가댁 is the honorific form)", "박 일병은 처가에서 처가 식구들과 같이 살아요."),
    ("핵가족", "(核家族) a nuclear family (i.e. a couple and their dependent children)", "핵가족으로 살면 식구가 적어서 편해요."),
]
_CV_APP = [
    ("급하다", "(急) to be short-tempered; to be impatient; to be urgent", "김 교수님은 성격이 좀 급합니다."),
    ("날씬하다", "to be slim", "제 사촌 동생은 다이어트를 해서 아주 날씬해졌어요."),
    ("내성적이다", "(內省的) to be introspective; to be introverted; to be reserved", "제 여동생은 내성적이어서 모르는 사람과 이야기를 잘 하지 않아요."),
    ("뚱뚱하다", "to be fat; to be chubby", "요즘 운동을 안 하고 많이 먹어서 뚱뚱해졌어요."),
    ("마르다", "to be scrawny; to be bony; to be skinny", "우리 딸은 잘 먹지 않아서 많이 말랐어요."),
    ("성격", "(性格) personality; character", "우리 사무실 직원들은 성격이 아주 좋습니다."),
    ("적극적이다", "(積極的) to be active; to be proactive", "유 선생님은 적극적이어서 뭐든지 열심히 하십니다."),
    ("조용하다", "to be quiet; to be calm", "황 팀장님은 말이 없으시고 조용하신 편입니다."),
    ("착하다", "to be good-hearted; to be nice", "제 사촌 누나는 착해서 다른 사람을 잘 도와줘요."),
    ("활발하다", "(活潑) to be active; to be outgoing", "박 간호사는 성격이 활발해서 사람들하고 잘 지내요."),
]
_CV_LOAN = [("이메일", "e-mail", "저는 한국친구들에게 매일 이메일을 씁니다.")]
_CV_OTH = [
    ("가정", "(家庭) a home; a family; a household", "한국 가정과 미국 가정이 조금 다릅니다."),
    ("가지다 / 갖다", "to have; to possess", "결혼하면 아이를 두 명 갖고 싶어요."),
    ("기자", "(記者) a journalist; a news reporter", "제 아내는 기자인데 아주 바쁩니다."),
    ("낳다", "to give birth to", "요즘은 아이를 낳지 않는 부부가 많습니다."),
    ("늘다 / 늘어나다", "to increase", "요즘은 혼자 사는 사람이 늘고 있어요."),
    ("다문화가정", "(多文化家庭) a multicultural family", "한국에 다문화가정이 늘고 있어요."),
    ("따로", "separately; independently", "저는 결혼해서 시부모님을 모시지 않고 따로 살고 싶습니다."),
    ("~대", "(代) a generation", "저희 집은 저희 부모님, 저 그리고 저희 아이들, 삼 대가 같이 삽니다."),
    ("맞벌이", "a dual-income couple", "요즘은 맞벌이 부부가 아주 많습니다."),
    ("변하다", "(變) to change", "한국사회가 많이 변하고 있습니다."),
    ("변화", "(變化) (~하다/되다) change (to change/to be changed)", "작년에는 전 세계적으로 여러 가지 변화가 있었습니다."),
    ("삶", "life; living", "요즘은 가족들이 집안일을 다 같이 하기 때문에 여성들의 삶이 더 편해졌습니다."),
    ("수 / 숫자", "(數/數字) a number; a figure", "우리 반 학생 수가 몇 명입니까?"),
    ("약간", "(若干) a little; a bit", "김 선생님은 약간 뚱뚱하십니다."),
    ("예를 들면", "(例) for example", "예를 들면, 요즘에는 일 인 가정이 증가하고 있습니다."),
    ("예전", "(前) (예전에) in the old days; in olden times; in the past", "예전에는 여성들이 집안일을 다 했어요."),
    ("-(으)ㅁ", "noun ending (see the grammar on nouns derived from native Korean verbs)", "부부싸움을 자주 하면 아이들한테 좋지 않습니다."),
    ("의논", "(議論) (~하다) discussion (to discuss; to talk something over)", "저는 어려운 일이 생기면 부모님과 의논합니다."),
    ("-잖아요", "verb ending used to remind what is obvious", "올해가 벌써 다 갔잖아요."),
    ("전업주부", "(專業主婦) a full-time homemaker", "저희 어머니는 전업주부이십니다."),
    ("~점", "(點) a point; a point of view", "수학시험에서 백 점을 받았어요."),
    ("줄다 / 줄어들다", "to decrease", "요즘 우리 학교 학생이 줄고 있어요."),
    ("직장", "(職場) a workplace; a job", "졸업 후에 좋은 직장에서 일하고 싶습니다."),
    ("흔하다", "to be common", "요즘은 외국에 사는 한국사람이 아주 흔합니다."),
]
_CV_SINO = [("가", "(家) a home; a family; a household; (a professional) person", "가정, 가족, 외가, 처가"), ("장", "(長) long; big; a chief; a head", "장거리, 장남, 장녀, 부대장, 회장, 사장"), ("조", "(祖) an ancestor", "조부모, 조국, 조상"), ("차", "(次) next; sequence", "차남, 차녀, 차세대"), ("처", "(妻) a wife", "처가, 처형, 처제, 처남")]
_ALL = {r[0]: r for r in _CV_KIN + _CV_APP + _CV_LOAN + _CV_OTH + _CV_SINO}
_EXTRA = {"장남 ": "", }
_EXTRA = {"가지다 / 갖다": "to have; to possess", "예전": "in the old days; in olden times; in the past", "변화": "change", "수 / 숫자": "a number; a figure",
          "큰아들": "the eldest son (colloquial)", "첫째 아들": "the first son", "큰딸": "the eldest daughter (colloquial)", "첫째 딸": "the first daughter", "둘째 아들": "the second son", "둘째 딸": "the second daughter", "셋째 아들": "the third son", "셋째 딸": "the third daughter", "막내": "the youngest child",
          "독자": "an only son (獨子)", "외아들": "an only son", "무남독녀": "an only daughter and no other children (無男獨女)", "부부간": "the husband-wife relationship", "부자간": "the father-son relationship",
          "처형": "a wife’s older sister", "처제": "a wife’s younger sister", "처남": "a wife’s brother", "시누이": "a husband’s sister", "시동생": "a husband’s younger brother", "친정": "a married woman’s parents’ home (親庭)", "장인어른": "a man’s father-in-law (honorific)",
          "장가가다": "(for a man) to get married; to go to the (man’s) in-laws’ home", "시집가다": "(for a woman) to get married; to go to the husband’s home", "전처": "one’s ex-wife; “previous wife”", "가장": "a household head; “family head”", "가옥": "a house; “family home”", "가축": "a domestic animal; livestock; “household animal”", "화가": "a painter; “person who draws pictures”", "작가": "a writer; an author; “person who creates”", "발명가": "an inventor; “person who invents”",
          "장거리": "long distance", "장기간": "a long period", "장화": "a boot; “long (leathered) shoe”", "사장": "a company president; “company head”", "병장": "a sergeant; “head of soldiers”", "학장": "a dean; “school head”", "차세대": "the next generation", "차석": "the second seat; the second position", "차선": "the second best; “next good”", "차례": "an order; a turn; “sequence rule”", "조국": "one’s homeland; “ancestor country”", "조부": "a grandfather", "조모": "a grandmother", "조상": "an ancestor; ancestry",
          "회장": "a chairperson; a president (mine)", "외가": "a mother’s family home (mine)", "가족": "a family (mine)", "가족사진": "a family photo (mine)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)

# ================================================================== L1: objectives, terms for children, 장 次 祖
_CHILD = [("장남", "the oldest son (also 큰아들, 첫째 아들)"), ("큰아들", "the oldest son (colloquial)"), ("첫째 아들", "the first son"), ("장녀", "the oldest daughter (also 큰딸, 첫째 딸)"), ("큰딸", "the oldest daughter (colloquial)"), ("첫째 딸", "the first daughter"),
          ("차남", "the second son (also 둘째 아들)"), ("둘째 아들", "the second son"), ("차녀", "the second daughter (also 둘째 딸)"), ("둘째 딸", "the second daughter"), ("셋째 아들", "the third son"), ("셋째 딸", "the third daughter"), ("막내", "the youngest child (also 막내 아들, 막내 딸)"), ("막내 아들", "the youngest son"), ("막내 딸", "the youngest daughter")]
_NUMKIDS = [("삼남사녀", "three sons and four daughters"), ("일남이녀", "one son and two daughters"), ("독자", "an only son (獨子)"), ("외아들", "an only son"), ("무남독녀", "an only daughter and no other children (無男獨女)"), ("부부간", "the husband-wife relationship (부부지간)"), ("부자간", "the father-son relationship (부자지간)")]
_ORD = [("우리 집 첫째", "our family’s first (child)"), ("둘째", "the second child"), ("셋째", "the third child"), ("막내", "the youngest child")]
_JANG = [("장거리", "long distance"), ("장기간", "a long period"), ("장화", "a boot; “long (leathered) shoe”"), ("장남", "the eldest son; “big man”"), ("사장", "a company president; a business owner; “company head”"), ("병장", "a sergeant; “head of soldiers”"), ("학장", "a dean; “school head”")]
_CHA = [("차남", "the second son; “next son”"), ("차녀", "the second daughter; “next daughter”"), ("차세대", "the next generation"), ("차석", "the second seat; the second position"), ("차선", "the second best; “next good”"), ("차례", "an order; a turn; “sequence rule”")]
_JO = [("조국", "one’s homeland; “ancestor country”"), ("조부모", "grandparents; “ancestor parents”"), ("조부", "a grandfather"), ("조모", "a grandmother"), ("조상", "an ancestor; ancestry; “ancestor above (in family pedigree)”")]
L1 = lesson(
    "Ch 25 · What the chapter teaches, terms for children and 장 (長), 차 (次), 조 (祖)",
    "한국의 가족 · 장남 · 장녀 · 차남 · 막내 · 삼남사녀 · 부부간 · 조부모",
    requires=[],
    cards=[
        card("What Chapter 25 teaches (한국의 가족)",
             "Chapter 25, “The Korean Family”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and talk about family types and use kinship terms; identify and talk about changes in Korean family life; and describe a person’s appearance and personality.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; the verb ending –잖아요; nouns derived from native Korean verbs; past tense verbs for a present state or condition; contractions of the topic marker 는 and the object marker 를; and the Sino-Korean syllables 장 (長), 차 (次), 조 (祖), 처 (妻) and 가 (家)."),
        card("Notes 1: terms for children and siblings",
             "Koreans often use the ordinal numbers in informal speech to refer to their children or siblings: 우리 집 첫째 (literally, “our family’s first”), 둘째 (second child), 셋째 (third child), etc. The youngest child is called (우리 집) 막내 (our youngest child). Koreans also use the following kinship terms to refer to their children (the book’s table: first, second, third and youngest son and daughter; the English is the book’s).",
             tables=[ktable(_ORD), ktable(_CHILD)]),
        card("Notes 2 and 3: the number of children and family relationships",
             "Koreans often use the Sino-Korean syllables ~남 (男) (man or boy) and ~녀 (女) (woman or girl) preceded by a Sino number when they refer to a specific number of children: 삼남사녀 (three sons and four daughters); 일남이녀 (one son and two daughters). When a family has only one son, he is called 독자 (獨子) or 외아들; when a family has only a daughter and no other children, she is called 무남독녀 (無男獨女).\n\n"
             "Koreans often use the Sino-Korean words ~(지)간 (之間) to refer to a relationship between family members: 부부(지)간 (husband-wife relationship; between husband and wife) and 부자(지)간 (father-son relationship; between father and son).",
             tables=[ktable(_NUMKIDS)]),
        card("Cultural note: the oldest son",
             "Heavily influenced by Confucianism, a traditional Korean family held its oldest son in highest esteem. Once married, he was responsible for carrying on the family name and lineage, keeping property in the family, and taking care of ancestral rites as well as aging parents. For this reason, the oldest son enjoyed a special status with an added bonus: He usually received the largest share of the family’s inheritance. Since the 1970s, however, when Korean society began to become industrialized, this tradition has been fading away. Nowadays, all siblings are expected to share in the responsibility of taking care of aging parents, and the number of parents who live with their second/third sons or daughters has increased. Despite these changes, however, an increasing number of elderly people prefer to live independently."),
        card("Sino-Korean in use: 장 (長)",
             "This Sino-Korean syllable means long or big, as in 장거리 (long distance), 장기간 (a long period), 장화 (a boot; “long [leathered] shoe”), and 장남 (the eldest son; “big man”). The syllable also means the chief or head (of a group or an organization), as in 사장 (a company president; a business owner; “company head”), 병장 (a sergeant; “head of soldiers”), and 학장 (a dean; “school head”). The book asks you to guess 장녀 and 부대장; the answers (mine): 장녀 is the oldest daughter, 부대장 is a unit commander.",
             tables=[ktable(_JANG)]),
        card("Sino-Korean in use: 차 (次) and 조 (祖)",
             "차 (次) means next, second, or sequence. 조 (祖) means ancestor.",
             tables=[ktable(_CHA), ktable(_JO)]),
        card("Activities left out",
             "The vocabulary builder (a PowerPoint presentation with pictures and sounds, Activities 1 and 2 on the SMART Board and Activity 3, the “Hot Seat” game) is a picture, computer and game activity."),
    ],
    exercises=uniq(
        _tr(_CHILD + _NUMKIDS + _JANG + _CHA + _JO)
        + [M("Which is the oldest son?", "장남", ["차남", "막내 아들", "독자"], "장 = big; 장남 = the oldest son."), M("Which is the second daughter?", "차녀", ["장녀", "막내 딸", "셋째 딸"], "차 = next; 차녀 = the second daughter."), M("What do you call the youngest child?", "막내", ["첫째", "독자", "장남"], "막내 = the youngest."),
           M("What does 삼남사녀 mean?", "three sons and four daughters", ["four sons and three daughters", "three sons only", "seven children"], "삼 남 사 녀: three sons, four daughters."), M("What does 일남이녀 mean?", "one son and two daughters", ["two sons and one daughter", "one daughter", "three sons"], "일 남 이 녀."),
           M("What is a family with only one son called?", "독자 or 외아들", ["무남독녀", "막내", "장남"], "독자 (獨子)."), M("What is an only daughter with no other children called?", "무남독녀", ["독자", "외아들", "차녀"], "無男獨女."),
           M("Which word means “the husband-wife relationship”?", "부부간", ["부자간", "모녀간", "형제간"], "부부(지)간."), M("What does 사장 mean?", "a company president", ["a sergeant", "a dean", "a boot"], "장 = head: 회사 + 장."),
           M("What does 장 (長) mean?", "long; big; a chief; a head", ["next; sequence", "an ancestor", "a wife"], "장거리, 장남, 사장."), M("What does 차 (次) mean?", "next; sequence", ["an ancestor", "long; big", "a home"], "차남, 차녀, 차례."), M("What does 조 (祖) mean?", "an ancestor", ["next; sequence", "a wife", "a family"], "조상, 조부모, 조국."),
           M("Why has the position of the oldest son changed since the 1970s?", "Korean society became industrialized", ["The government banned it", "Families got larger", "Sons moved abroad"], "The book’s cultural note."), M("Who is expected to take care of aging parents nowadays?", "All the siblings", ["Only the oldest son", "Only daughters", "Nobody"], "All siblings share the responsibility."),
           F("우리 집 ___는 아들이에요. (the youngest child)", "막내", ["독자", "장남"], "막내 = the youngest child."), F("김 선생님은 ___ 아들이세요. (the oldest)", "큰", ["작은", "막"], "큰아들 = the oldest son."), F("한국에서는 첫째 아들을 ___이라고도 해요. (장…)", "장남", ["차남", "독자"], "장남 = the first son."),
           read_q("장남"), read_q("차녀"), read_q("막내"), read_q("무남독녀"), read_q("부부간")]
    ),
)

# ================================================================== L2: Topic A
_A_DLG = [
    ("기자", "안녕하십니까? 가족 소개를 해 주시겠습니까?", "How do you do? Would you introduce your family?"),
    ("대철", "네. 조부모님, 부모님, 제 아내와 저 그리고 아이들이 같이 살고 있습니다.", "Yes. My grandparents, my parents, my wife and I, and the children live together."),
    ("기자", "네. 요즘 흔하지 않은 대가족이군요!", "I see. It’s an extended family, which is not common these days!"),
    ("대철", "네. 저희 아버지가 장남이십니다. 그래서 항상 조부모님과 같이 살았어요. 그리고 저도 장남이어서 지금 어른들을 모시고 삽니다.", "Yes. My father is the oldest son. So he has always lived with my grandparents. And I am also the oldest son, so I now live serving the elders."),
    ("기자", "아, 네. 그럼 사 대가 같이 살고 계시는데, 불편한 점은 없으십니까?", "Oh, I see. Then four generations live together; are there any inconvenient points?"),
    ("대철", "식구가 많으니까 불편할 때도 있어요. 다 같이 차를 타고 나갈 때 조금 불편해요. 그렇지만, 좋은 점이 더 많아요.", "Since there are many family members, it is sometimes inconvenient. It’s a little inconvenient when we all go out in a car together. But there are more good points."),
    ("기자", "어떤 점이 좋으세요?", "What points are good?"),
    ("대철", "어른들이 아이들을 잘 돌봐 주시니까 좋아요. 그리고 어려운 일이 있으면 어른들과 의논할 수 있어서 좋습니다.", "It’s good because the elders take good care of the children. And when there is a difficult matter, I can talk it over with the elders, which is good."),
    ("기자", "보통 여자분들은 따로 살고 싶어하는데, 부인은 어떠십니까?", "Women usually want to live separately; how about your wife?"),
    ("대철", "제 아내는 어른들과 같이 사는 것을 아주 좋아합니다.", "My wife likes living with the elders very much."),
]
_A_WORDS = ["기자", "대가족", "따로", "모녀", "모자", "부녀", "부자", "손녀", "손자", "식구", "어른", "의논", "장남", "장녀", "~점", "조부모 / 조부모님", "차남", "차녀", "핵가족", "흔하다"]
L2 = lesson(
    "Ch 25 · Topic A: A large family of four generations",
    "대가족 · 조부모님 · 장남 · 어른들을 모시고 삽니다 · 핵가족 · 의논",
    requires=[],
    cards=[
        card("Topic A: A large family of four generations (대가 모여 사는 대가족)",
             "A TV reporter is interviewing the head of a family spanning four generations. (The English is mine; the book gives none. The book writes 4대가; it is spelled out here. The book’s footnote: ~을/를 모시고 살다 literally means “to serve and live.” This expression is used when people live with parents, grandparents, or others who are considered superior in social status.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Activities left out",
             "The SMART Board activity and the sentence-strip activities (arranging and translating the dialog with a partner) of the Presentation Activity are computer and partner activities. Follow-up 1 (listening to short self-introductions at a party and noting each speaker’s number of siblings, birth order, and whether the speaker plans to live with parents or parents-in-law) is an audio activity. Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if "/" not in w and "~" not in w]))
        + _tr(_strip(_A_DLG))
        + [M("Who is being interviewed?", "The head of a family of four generations", ["A teacher", "A soldier", "A doctor"], "대가 모여 사는 대가족."), M("Who lives together in Daechul’s home?", "Grandparents, parents, his wife and him, and the children", ["Only his wife and children", "His in-laws", "His brothers"], "조부모님, 부모님, 아내와 저, 아이들."),
           M("Why has Daechul always lived with his grandparents?", "His father and he are both oldest sons", ["They have no other home", "His wife wanted to", "They are poor"], "저희 아버지가 장남이십니다."), M("What is a little inconvenient?", "Going out together in one car", ["Cooking", "Cleaning", "Shopping"], "다 같이 차를 타고 나갈 때."), M("What is good about the large family?", "The elders take care of the children and he can talk over difficulties", ["It is cheaper", "It is quieter", "There are fewer chores"], "아이들을 잘 돌봐 주시니까 좋아요."),
           M("What does the reporter say women usually want?", "To live separately", ["To live with the elders", "To work", "To move abroad"], "따로 살고 싶어하는데."), M("How does Daechul’s wife feel about living with the elders?", "She likes it very much", ["She dislikes it", "She is indifferent", "She wants to move"], "아주 좋아합니다."),
           M("What does ~을/를 모시고 살다 literally mean?", "to serve and live", ["to love and live", "to marry and live", "to work and live"], "The book’s footnote."), M("What is a 핵가족?", "a nuclear family", ["an extended family", "a married couple", "a family member"], "핵가족 = a couple and their dependent children."),
           F("저희 아버지가 ___이십니다. (the oldest son)", "장남", ["차남", "손자"], "장남 = the oldest son."), F("어른들과 ___할 수 있어서 좋습니다. (talk it over)", "의논", ["복무", "입대"], "의논하다 = to discuss."), F("요즘 흔하지 ___ 대가족이군요! (a common)", "않은", ["않는", "안"], "흔하지 않은 = not common."), F("식구가 많으니까 불편할 ___도 있어요. (times)", "때", ["점", "곳"], "불편할 때도 있어요."),
           F("보통 여자분들은 ___ 살고 싶어하는데, 부인은 어떠십니까? (separately)", "따로", ["같이", "함께"], "따로 = separately."),
           read_q("가족 소개를 해 주시겠습니까"), read_q("대가족"), read_q("조부모님과 같이 살았어요"), read_q("어른들과 의논할 수 있어서 좋습니다"), read_q("제 아내는 어른들과 같이 사는 것을 아주 좋아합니다")]
    ),
)

# ================================================================== L3: Topic A, follow-up 2, Activity 3
_FU2 = [
    ("우리 가족은 요즘 흔하지 않은 대가족입니다.", "My family is an extended family, which is not common these days."), ("조부모님과 부모님, 남편과 저, 그리고 저희 아이들까지 사 대가 한 집에 살고 있어요.", "Four generations live in one house: my grandparents, my parents, my husband and me, and our children."),
    ("저희는 아이가 셋인데, 아들 하나 딸 둘이 있습니다.", "We have three children: one son and two daughters."), ("아들은 중학생, 첫째 딸은 초등학생, 그리고 막내딸은 한 살입니다.", "The son is a middle school student, the first daughter is an elementary school student, and the youngest daughter is one year old."),
    ("식구가 많아서 집안일이 많지만 온 가족이 다 함께 집안일을 합니다.", "Since there are many family members there is a lot of housework, but the whole family does the housework together."), ("어른들께서는 막내딸을 잘 돌봐 주시고 남편과 큰아이들은 집 청소와 빨래를 도와줍니다.", "The elders take good care of the youngest daughter, and my husband and the older children help with cleaning the house and the laundry."),
    ("그래서 집안일이 조금도 힘들지 않습니다.", "So the housework is not hard at all."), ("그렇지만, 집이 작고 화장실이 하나밖에 없어서 불편합니다.", "However, the house is small and there is only one bathroom, so it is inconvenient."),
]
_ACT3 = [
    ("저는 칠 년 전에 결혼해서 아들 하나, 딸 하나가 있습니다.", "I got married seven years ago and have one son and one daughter."), ("결혼하고 처음 오 년 동안 부모님을 모시고 살았습니다.", "For the first five years after marriage I lived with my parents."),
    ("결혼하지 않은 여동생도 같이 살았습니다.", "My unmarried younger sister also lived with us."), ("이 년 전, 여동생이 시집갔을 때 부모님이 고향에서 살고 싶어 하셨습니다.", "Two years ago, when my younger sister got married, my parents wanted to live in their hometown."),
    ("그래서 이 년 전부터 저는 아내와 아이들하고만 따로 살고 있습니다.", "So since two years ago I have been living separately with only my wife and children."),
    ("제 가족이 부모님과 여동생과 함께 살았을 때는 집안일이 많았습니다.", "When my family lived with my parents and younger sister, there was a lot of housework."), ("그래서 아내에게 늘 미안했습니다.", "So I always felt sorry toward my wife."),
    ("그렇지만 부모님과 동생이 아이들과 잘 놀아 주었습니다.", "But my parents and my sibling played well with the children."), ("지금은 식구가 적으니까 조금 심심합니다.", "Now there are few family members, so it is a little boring."), ("그렇지만 집안일도 많지 않고 여행도 자주 갈 수 있습니다.", "But there is not much housework and we can travel often."),
]
L3 = lesson(
    "Ch 25 · Topic A, Follow-up 2 and Activity 3: two family stories",
    "대가족 · 핵가족 · 집안일 · 시집갔을 때 · 따로 살고 있습니다",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): a married woman describes her family",
             "The book asks you to read a family description written by a married woman, tick the family type (extended or nuclear family) and fill in a table in English (family members; positive and/or negative aspects). The text is the book’s (1살 is spelled out); the English is mine.",
             examples=passage(_FU2)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Family type", "Family members", "Positive and/or negative aspects"], [["Extended family (4 generations)", "Grandparents, parents, husband and wife, a son, two daughters", "Positive: the whole family does the housework; the elders take care of the youngest daughter; the husband and older children help. Negative: the house is small and there is only one bathroom"]])]),
        card("Activity 3 (Reading): changes in a man’s family two years ago",
             "The book asks you to read a story in which a man talks about changes in his family that occurred two years ago and to fill in a table in English. The text is the book’s (7년, 5년, 2년 are spelled out); the English is mine.",
             examples=passage(_ACT3)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["", "First 5 years of marriage", "Last 2 years"], [["Family type", "Extended family", "Nuclear family"], ["Family members living together", "Wife, two children, his parents and his unmarried younger sister", "Wife and two children"], ["Positive aspects", "The parents and the sibling played well with the children", "Not much housework; can travel often"], ["Negative aspects", "A lot of housework; he felt sorry toward his wife", "A little boring because there are few family members"]])]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity), Activity 2 (listening to three conversations asking about the other speaker’s family) and Activity 4 (어버이날 기념 효행상 추천: listening to interviews about two finalists for an exemplary-filial-conduct award from the Ministry of National Defense and choosing one, in pairs) are computer, audio and partner activities."),
    ],
    exercises=uniq(
        _tr(_FU2 + _ACT3)
        + [M("What type of family is it in Follow-up 2?", "An extended family of four generations", ["A nuclear family", "A single-parent family", "A family of two"], "사 대가 한 집에 살고 있어요."), M("How many children does the writer have?", "Three: one son and two daughters", ["Two daughters", "Three sons", "Four"], "아들 하나 딸 둘."), M("How old is the youngest daughter?", "One year old", ["Seven", "Three", "Ten"], "막내딸은 한 살."),
           M("Who looks after the youngest daughter?", "The elders", ["The husband", "The oldest daughter", "A nanny"], "어른들께서는 막내딸을 잘 돌봐 주시고."), M("What is inconvenient in this family?", "The house is small and has only one bathroom", ["There is too much housework", "The elders are strict", "The children are noisy"], "화장실이 하나밖에 없어서."),
           M("How long did the man live with his parents after marrying?", "Five years", ["Two years", "Seven years", "Ten years"], "처음 오 년 동안."), M("Why did his parents want to live in their hometown?", "His younger sister had got married", ["He got a new job", "The house was small", "They were ill"], "여동생이 시집갔을 때."), M("How long has he lived separately?", "Two years", ["Five years", "Seven years", "One year"], "이 년 전부터."),
           M("Why did he always feel sorry toward his wife?", "There was a lot of housework", ["She was ill", "She had no friends", "She worked too much"], "집안일이 많았습니다."), M("How does he feel about the nuclear family?", "A little bored, but with less housework and more travel", ["Very happy only", "Unhappy only", "He misses nothing"], "조금 심심합니다. 그렇지만 집안일도 많지 않고."),
           F("저는 칠 년 전에 ___해서 아들 하나, 딸 하나가 있습니다. (got married)", "결혼", ["입대", "이혼"], "결혼하다 = to get married."), F("여동생이 ___ 때 부모님이 고향에서 살고 싶어 하셨습니다. (married, for a woman)", "시집갔을", ["입대했을", "제대했을"], "시집가다 = a woman gets married."), F("지금은 식구가 적으니까 조금 ___. (boring)", "심심합니다", ["바쁩니다", "힘듭니다"], "심심하다 = to be bored."),
           F("집안일이 조금도 ___ 않습니다. (hard)", "힘들지", ["심심하지", "불편하지"], "힘들다 = to be hard."),
           read_q("우리 가족은 요즘 흔하지 않은 대가족입니다"), read_q("집안일을 합니다"), read_q("부모님을 모시고 살았습니다"), read_q("따로 살고 있습니다"), read_q("여행도 자주 갈 수 있습니다")]
    ),
)

# ================================================================== L4: Topic B
_B_TEXT = [
    ("저희는 맞벌이 부부입니다.", "We are a dual-income couple."), ("제 아내는 은행에서 일하고 저는 대학에서 영어를 가르칩니다.", "My wife works at a bank and I teach English at a university."), ("저는 처가에서 장인, 장모님과 함께 살고 있습니다.", "I live in my wife’s family home together with my father-in-law and mother-in-law."),
    ("우리 가족사진을 보여 드리겠습니다.", "I will show you our family photo."), ("여기 약간 뚱뚱하신 분이 장인어른입니다.", "The slightly chubby person here is my father-in-law."), ("장인어른은 조용하시고 내성적이십니다.", "My father-in-law is quiet and reserved."),
    ("그 옆에 계신 분이 제 장모님인데, 조금 마르셨습니다.", "The person next to him is my mother-in-law, and she is a little thin."), ("장모님은 적극적이시고, 성격이 조금 급한 편입니다.", "My mother-in-law is proactive, and her personality is a little short-tempered."),
    ("그리고 제 아내는 키가 크고 날씬합니다.", "And my wife is tall and slim."), ("아주 착하고 활발한 성격입니다.", "She has a very good-hearted and outgoing personality."),
    ("제 고향은 부산입니다.", "My hometown is Busan."), ("부모님께서는 제 남동생과 함께 고향에서 살고 계십니다.", "My parents live in my hometown together with my younger brother."),
    ("제 아내는 시부모님께 자주 전화를 드리고 이메일로 아이 사진도 보내드립니다.", "My wife often phones my parents and also sends them the children’s pictures by e-mail."), ("제 부모님께서는 며느리가 착해서 마음에 든다고 하십니다.", "My parents say they like their daughter-in-law because she is good-hearted."),
]
_B_WORDS = ["급하다", "날씬하다", "내성적이다", "뚱뚱하다", "마르다", "맞벌이", "며느리 / 며느님", "부부", "사위", "성격", "시부모 / 시부모님", "시아버지 / 시아버님", "시어머니 / 시어머님", "시집 / 시댁", "약간", "이메일", "장모 / 장모님", "장인", "적극적이다", "조용하다", "착하다", "처가 / 처가댁", "활발하다"]
_DIAG = [("사위", "a man, seen from his wife’s family: the son-in-law (the circled man in the first picture)"), ("장인", "the wife’s father (the man in the first picture, next to 장모)"), ("장모", "the wife’s mother"), ("처가 / 처가댁", "the wife’s family home (labelled beside the wife in the first picture)"),
         ("시아버지", "the husband’s father (the second picture)"), ("시어머니", "the husband’s mother"), ("며느리", "a woman, seen from her husband’s family: the daughter-in-law (the circled woman in the second picture)"), ("시집 / 시댁", "the husband’s family home (labelled beside the husband in the second picture)")]
_CHEO = [("처가", "one’s wife’s home; one’s wife’s (parents’) family"), ("처남", "one’s wife’s brother"), ("처제", "one’s wife’s younger sister; “wife’s younger sibling”"), ("전처", "one’s ex-wife; “previous wife”"), ("처삼촌", "one’s wife’s uncle (mine)"), ("처형", "one’s wife’s older sister"), ("처조카", "one’s wife’s niece or nephew (mine)")]
_SIM = [("처형", "wife’s older sister"), ("처제", "wife’s younger sister"), ("처남", "wife’s brothers"), ("시아버지", "husband’s father"), ("시어머니", "husband’s mother"), ("시누이", "husband’s sister"), ("시동생", "husband’s younger brother"), ("친정 아버지", "a married woman’s own father"), ("친정 어머니", "a married woman’s own mother"), ("친정 동생", "a married woman’s own younger sibling"),
        ("장가가다", "(for a man) to get married; literally “to go to the (man’s) in-laws’ home”"), ("장가들다", "(for a man) to get married; literally “to get into the in-laws’ home”"), ("시집가다", "(for a woman) to get married; literally “to go to the husband’s home”")]
L4 = lesson(
    "Ch 25 · Topic B: In-laws, the wife’s family and the husband’s family",
    "처가와 시댁 · 장인 · 장모 · 사위 · 며느리 · 성격 · 맞벌이 부부",
    requires=[],
    cards=[
        card("Topic B: In-laws: wife’s family and husband’s family (처가와 시댁)",
             "Mr. Park is introducing his family members to the members of a club he recently joined. (The English is mine; the book gives none.)",
             examples=passage(_B_TEXT)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("The family pictures (notes)",
             "The book has two pictures of in-laws: in the first, a man and his wife with her parents (장인, 장모) beside his own parents, and the labels 사위 and 처가/처가댁; in the second, a woman and her husband with his parents (시아버지, 시어머니) beside her own parents, and the labels 며느리 and 시집/시댁. The explanations are mine, from the labels.",
             tables=[table(["Term", "Who or what (mine, from the labels)"], [list(r) for r in _DIAG], say=[0])]),
        card("Notes: North Korea",
             "In North Korea, 장인 and 장모 are called 가시아버지 and 가시어머니, respectively; 아내 is called 안해."),
        card("Cultural note: kinship terms of in-laws",
             "Koreans have long valued the importance of family beyond their immediate and extended family. Therefore, kinship terms for non-blood relations are extensive and diverse. For example, when a man is married, he refers to his wife’s family as 처가/처가댁 (↑), which literally means “wife’s home.” A married man refers to his in-laws (except his father-in-law 장인 and mother-in-law 장모) with a word that begins with 처 (妻) wife, as in 처형 wife’s older sister, 처제 wife’s younger sister, 처남 wife’s brothers, etc. When a woman is married, she refers to her husband’s family as 시집/시댁 (↑). A married woman refers to her in-laws with a word that begins with 시 (媤) husband’s home, as in 시아버지 husband’s father, 시어머니 husband’s mother, 시누이 husband’s sister, 시동생 husband’s younger brother, etc. Once married, a woman refers to her own parents’ family with a word that begins with 친정 (親庭), as in 친정 아버지, 친정 어머니, 친정 동생, etc. Terms like 장가 (literally, “man’s in-laws’ home”) and 시집 (literally, “woman’s in-laws’ home”) are also used to express “tying the knot.” Although Koreans use the term 결혼하다, they also use 장가가다 or 장가들다, whose literal meaning is go to the (man’s) in-laws’ home or get in the in-laws’ home, when a man gets married. For a woman who marries, Koreans say 시집가다, which literally means go to the husband’s home. 친정 (親庭) literally means “true garden” or “biological garden” and refers to a married woman’s parents’ home, as in 친정 아버지, 친정 동생, 친정집, etc.",
             tables=[ktable(_SIM)]),
        card("Sino-Korean in use: 처 (妻)",
             "The Chinese character of this Sino-Korean syllable describes a woman with a broom in her hand, implying woman working at home. So this syllable means wife, as in 처가 (one’s wife’s home), 처남 (one’s wife’s brother), 처제 (one’s wife’s younger sister; “wife’s younger sibling”), and 전처 (one’s ex-wife; “previous wife”). The book asks you to guess 처삼촌, 처형 and 처조카; the answers are mine (처형 is in the cultural note).",
             tables=[ktable(_CHEO)]),
        card("Activities left out",
             "The Presentation Activity’s SMART Board activities, the transcription from audio (the book’s cloze of Topic B) and Follow-up 1 (listening to three dialogs about pictured family members: ticking the kinship term and describing the person) are computer and audio activities. Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if "/" not in w]))
        + _tr(_B_TEXT + _DIAG + _SIM + _CHEO)
        + [M("What kind of couple are Mr. Park and his wife?", "A dual-income couple", ["A retired couple", "A newly married couple", "A couple living abroad"], "맞벌이 부부입니다."), M("Where does Mr. Park live?", "In his wife’s family home with his in-laws", ["With his own parents", "In Busan", "Alone"], "처가에서 장인, 장모님과 함께."), M("What does Mr. Park’s wife do?", "Works at a bank", ["Teaches English", "Is a nurse", "Is a reporter"], "아내는 은행에서 일하고."),
           M("What is Mr. Park’s father-in-law like?", "Slightly chubby, quiet and reserved", ["Thin and active", "Tall and outgoing", "Short-tempered"], "약간 뚱뚱하신, 조용하시고 내성적이십니다."), M("What is Mr. Park’s mother-in-law like?", "A little thin, proactive and a little short-tempered", ["Chubby and quiet", "Slim and outgoing", "Tall and reserved"], "조금 마르셨습니다, 적극적이시고, 성격이 조금 급한 편."), M("What is Mr. Park’s wife like?", "Tall, slim, good-hearted and outgoing", ["Short and reserved", "Chubby and quiet", "Thin and short-tempered"], "키가 크고 날씬합니다. 착하고 활발한 성격."),
           M("Where is Mr. Park’s hometown?", "Busan", ["Seoul", "Daegu", "Jinju"], "제 고향은 부산입니다."), M("What does Mr. Park’s wife do for his parents?", "Phones them often and e-mails them the children’s pictures", ["Visits them daily", "Lives with them", "Cooks for them"], "자주 전화를 드리고 이메일로 아이 사진도 보내드립니다."), M("Why do Mr. Park’s parents like their daughter-in-law?", "She is good-hearted", ["She is rich", "She is a good cook", "She is tall"], "며느리가 착해서 마음에 든다."),
           M("What does a man call his wife’s family?", "처가 / 처가댁", ["시집 / 시댁", "친정", "외가"], "처가 = wife’s home."), M("What does a woman call her husband’s family?", "시집 / 시댁", ["처가 / 처가댁", "친정", "외가"], "시댁 = husband’s home."), M("What does a married woman call her own parents’ home?", "친정", ["처가", "시댁", "본가"], "親庭: true garden."),
           M("What does 처 (妻) mean?", "a wife", ["a husband", "a home", "an ancestor"], "처가, 처남, 처제."), M("What does 처제 mean?", "one’s wife’s younger sister", ["one’s wife’s brother", "one’s ex-wife", "one’s wife’s older sister"], "처 + 제 (younger sibling)."), M("What does a woman say when she marries?", "시집가다", ["장가가다", "입대하다", "제대하다"], "시집가다 = go to the husband’s home."), M("What does a man say when he marries (besides 결혼하다)?", "장가가다 or 장가들다", ["시집가다", "친정가다", "처가가다"], "The book’s cultural note."),
           F("저는 ___에서 장인, 장모님과 함께 살고 있습니다. (my wife’s family home)", "처가", ["시집", "친정"], "처가 = a man’s in-laws’ home."), F("제 아내는 키가 크고 ___. (slim)", "날씬합니다", ["뚱뚱합니다", "급합니다"], "날씬하다 = to be slim."), F("제 부모님께서는 ___가 착해서 마음에 든다고 하십니다. (daughter-in-law)", "며느리", ["사위", "손녀"], "며느리 = a daughter-in-law."), F("장인어른은 조용하시고 ___이십니다. (reserved)", "내성적", ["적극적", "활발"], "내성적이다 = to be reserved."),
           read_q("저희는 맞벌이 부부입니다"), read_q("장인어른은 조용하시고 내성적이십니다"), read_q("장모님은 적극적이시고"), read_q("착하고 활발한 성격입니다"), read_q("며느리가 착해서 마음에 든다고 하십니다")]
    ),
)

# ================================================================== L5: Topic B follow-ups and activities
_SURV = [
    ("맞벌이 부부가 늘어나면서 시댁이나 처가에서 함께 사는 가족이 늘어나고 있다.", "As the number of dual-income couples increases, families living together at the husband’s family’s or the wife’s family’s home are increasing."),
    ("야후 미디어 조사에 따르면 시댁이나 처가에서 부모를 모시고 사는 대부분의 가정은 부모와 같이 살면 아이를 키우는 데 도움을 받고, 생활비를 절약할 수 있어서 좋다고 대답했다.", "According to a Yahoo Media survey, most families who live with their parents at the husband’s or wife’s family’s home answered that living with the parents is good because they get help raising the children and can save living expenses."),
    ("그러나 나쁜 점으로는 장모와 사위간의 갈등, 시어머니와 며느리간의 갈등이라고 대답했다.", "However, as the bad points they answered the conflict between mother-in-law and son-in-law and the conflict between mother-in-law and daughter-in-law."),
    ("그리고 이러한 문제는 서로 다른 성격 때문이며, 더 많은 가족간의 대화가 필요하다고 말했다.", "And they said that these problems are due to different personalities, and that more conversation among family members is needed."),
]
_NEWS = [
    ("남자 대학생 육십삼 퍼센트 처가에 사는 것 좋아", "Sixty-three percent of male college students like living with the wife’s family (the headline; the book writes 63%)"),
    ("한 아르바이트 전문 사이트는 대학생 구백십팔 명을 대상으로 결혼에 대해 조사했다.", "A part-time job specialty site surveyed 918 college students about marriage."),
    ("조사에서 전체 응답자의 오십사 퍼센트가 결혼 후 처가나 시집에서 살 수 있다고 응답했다.", "In the survey, 54 percent of all respondents answered that they could live at the wife’s or husband’s family’s home after marriage."),
    ("특히, 남자 대학생의 육십삼 점 삼 퍼센트는 결혼 후 처가에 살 수 있다고 말했다.", "In particular, 63.3 percent of male college students said they could live at the wife’s family’s home after marriage."),
    ("시집에 살 수 있다는 여대생은 사십오 점 팔 퍼센트로, 처가에 살겠다는 남학생보다 적었다.", "The female college students who said they could live at the husband’s family’s home were 45.8 percent, fewer than the male students who said they would live at the wife’s family’s home."),
    ("처가나 시집에 살고 싶어하는 이유도 남학생과 여학생은 달랐다.", "The reasons for wanting to live at the wife’s or husband’s family’s home also differed between male and female students."),
    ("시집에 살겠다는 여대생의 사십삼 점 구 퍼센트가 남편의 부모님도 부모님이기 때문이라는 이유를 말했다.", "43.9 percent of the female college students who would live at the husband’s family’s home gave the reason that the husband’s parents are also parents."),
    ("하지만 처가에 살겠다는 남학생 삼십오 점 오 퍼센트는 돈을 절약하기 위해서라고 그 이유를 말했다.", "But 35.5 percent of the male students who would live at the wife’s family’s home gave their reason as to save money."),
    ("처가나 시집에 살지 않겠다고 응답한 대학생의 삼십 점 삼 퍼센트가 독립된 생활을 즐기기 위해서라고 말했다.", "30.3 percent of the college students who answered that they would not live at the wife’s or husband’s family’s home said it was to enjoy an independent life."),
]
_VOC_B = [("맞벌이", "a dual-income couple"), ("약간", "a little; a bit"), ("부부", "a married couple"), ("조용하다", "to be quiet; to be calm"), ("처가", "a man’s in-laws’ home"), ("뚱뚱하다", "to be fat; to be chubby"), ("장인", "a man’s father-in-law"), ("마르다", "to be skinny; to be bony"), ("장모", "a man’s mother-in-law"), ("날씬하다", "to be slim"), ("시부모", "a woman’s parents-in-law"), ("성격", "personality"), ("며느리", "a daughter-in-law"), ("급하다", "to be short-tempered; to be impatient"), ("이메일", "e-mail"), ("착하다", "to be good-hearted; to be nice"), ("적극적이다", "to be active; to be proactive"), ("활발하다", "to be active; to be outgoing")]
L5 = lesson(
    "Ch 25 · Topic B, Follow-up 2 and Activity 2: a survey of families and a news article",
    "처가와 시댁에 사는 가족 · 갈등 · 생활비를 절약 · 남자 대학생 63% 처가에 사는 것 좋아",
    requires=[],
    cards=[
        card("Presentation Activity a: the vocabulary of Topic B",
             "The book asks you to complete a vocabulary table with the appropriate Korean or English words for ten words of Topic B (맞벌이, 약간, 처가(댁), 뚱뚱하다, 장모, 날씬하다, 며느리, (성격이) 급하다, 이메일, 착하다 and the English of 부부, 조용하다, 장인, 마르다, 시부모, 성격, 적극적이다, 활발하다). The meanings are the core vocabulary’s.",
             tables=[ktable(_VOC_B)]),
        card("Follow-up 2 (Reading): survey results on families living with parents",
             "The text is an excerpt from survey results about families living with their parents. The book asks you to fill in a table in English (positive aspects, negative aspects and solutions to the negative aspects). The text is the book’s; the English is mine. The book glosses 갈등: conflict, discord; 대화: a dialog, a conversation.",
             examples=passage(_SURV)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Families living with their parents", "Answer (mine)"], [["Positive aspects", "They get help raising the children and can save living expenses"], ["Negative aspects", "Conflict between mother-in-law and son-in-law and between mother-in-law and daughter-in-law"], ["Solution(s) to negative aspects", "More conversation among family members (the problems come from different personalities)"]])]),
        card("Activity 2 (Reading): a news article on college students’ opinions on marriage",
             "The book asks you to (a) translate the headline into English, (b) match each of the four paragraphs with its topic, and (c) correlate the percents with who responded, the response and the reason. The text is the book’s (the figures are spelled out in Hangul; the quotation marks are left out); the English is mine. The book glosses 대상으로: as subjects (of a survey); 응답: a response; 이유: a reason.",
             examples=passage(_NEWS)),
        card("The answers (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Task", "Answer (mine)"], [["a. The headline", "“63% of male college students like living with the wife’s family”"], ["b. Paragraph 1", "Participants in the survey and the topic surveyed"], ["b. Paragraph 2", "Percent of respondents who are willing to live with their in-laws"], ["b. Paragraph 3", "Reasons for wanting to live with in-laws"], ["b. Paragraph 4", "A reason for not wanting to live with in-laws"]]), table(["Percent", "Respondents and response", "Reason (mine)"], [["43.9%", "Female students who would live at the husband’s family’s home", "The husband’s parents are also parents"], ["35.5%", "Male students who would live at the wife’s family’s home", "To save money"], ["30.3%", "Students who would not live with in-laws", "To enjoy an independent life"]])]),
        card("Activities left out",
             "Activity 3 (listening to three narrations about in-laws and noting the relationship to the speaker, the physical description and the personality) is an audio activity. Activity 4 (이런 시어머니가 좋아요: a matchmaking game in groups, reading three women’s profiles in Texts A and B) is a group activity, and the profile texts are not in the book’s text."),
    ],
    exercises=uniq(
        _tr(_VOC_B[:12] + _SURV[:0])
        + _tr(_SURV + _NEWS)
        + [M("What are the positive points of living with parents?", "Help raising children and saving living expenses", ["More privacy", "Bigger houses", "Less housework"], "아이를 키우는 데 도움을 받고, 생활비를 절약."), M("What are the negative points?", "Conflict between in-laws caused by different personalities", ["Money problems", "No space", "Noise"], "장모와 사위간의 갈등, 시어머니와 며느리간의 갈등."), M("What do they say is needed to solve the problems?", "More conversation among family members", ["Separate houses", "More money", "Fewer chores"], "더 많은 가족간의 대화가 필요."),
           M("How many college students were surveyed?", "918", ["54", "63", "30"], "구백십팔 명."), M("What percent of all respondents could live with in-laws after marriage?", "54%", ["63.3%", "45.8%", "30.3%"], "오십사 퍼센트."), M("What percent of male students could live at the wife’s family’s home?", "63.3%", ["54%", "45.8%", "43.9%"], "육십삼 점 삼 퍼센트."), M("What percent of female students could live at the husband’s family’s home?", "45.8%", ["63.3%", "54%", "35.5%"], "사십오 점 팔 퍼센트."),
           M("Why do female students want to live at the husband’s family’s home?", "The husband’s parents are also parents", ["To save money", "To enjoy independence", "To help the children"], "남편의 부모님도 부모님이기 때문."), M("Why do male students want to live at the wife’s family’s home?", "To save money", ["The wife’s parents are also parents", "To enjoy independence", "To have children"], "돈을 절약하기 위해서."), M("Why do some students not want to live with in-laws?", "To enjoy an independent life", ["To save money", "To help the parents", "To have more children"], "독립된 생활을 즐기기 위해서."),
           F("조사에서 전체 응답자의 오십사 퍼센트가 ___했다. (responded)", "응답", ["의논", "복무"], "응답하다 = to respond."), F("처가에 살겠다는 남학생은 돈을 ___하기 위해서라고 했다. (to save)", "절약", ["의논", "변화"], "절약하다 = to save."), F("그러나 나쁜 점으로는 시어머니와 며느리간의 ___이라고 대답했다. (conflict)", "갈등", ["대화", "절약"], "갈등 = conflict."),
           read_q("처가나 시집에 살 수 있다"), read_q("생활비를 절약할 수 있어서 좋다"), read_q("시어머니와 며느리간의 갈등"), read_q("서로 다른 성격 때문이며"), read_q("독립된 생활을 즐기기 위해서")]
    ),
)

# ================================================================== L6: Grammar A: past tense for a present state
_PAST_V = [("결혼하다", "to get married"), ("이혼하다", "to get divorced"), ("약혼하다", "to get engaged"), ("재혼하다", "to remarry"), ("입대하다", "to join the military"), ("끼다", "to form (fog); to wear (glasses)"), ("늙다", "to get old"), ("마르다", "to become thin"), ("생기다", "to be formed; to look (good or bad)"), ("입다", "to wear (clothes)")]
_PIRR = {"마르다": "말랐"}


def _pp(v):
    return _PIRR.get(v, past(v))


def _pres(v):
    return _pp(v) + "습니다"


def _pdone(v):
    return _pp(v) + "었습니다"


_G1 = [("산에 안개가 끼었습니다.", "Fog formed on the mountain (at one point in the past and it is foggy now)."), ("나는 작년에 결혼했습니다.", "Last year I got married (and I am married now)."), ("저는 이 월에 입대했습니다.", "I joined the military in February (and I am in the military now)."), ("김 선생님은 삼 월에 약혼했습니다.", "Mr. Kim got engaged in March (and he is engaged)."),
       ("책상에 먼지가 끼었습니다.", "Dust “formed” on the desk (and the desk is dusty)."), ("그 영화배우는 잘 생겼습니다.", "The actor “formed” well (and he is handsome)."), ("제 아내는 말랐습니다.", "My wife is skinny."), ("여동생은 안경을 꼈습니다.", "My younger sister put on glasses (and she is wearing glasses).")]
_G1B = [("김 선생님은 결혼했었습니다.", "Mr. Kim was married once (and no longer is)."), ("아침에 안개가 꼈었습니다.", "It was foggy in the morning (and no longer is)."), ("제 아내는 말랐었습니다.", "My wife was skinny (and no longer is).")]
_G1C = [("장인", "장인은 말랐습니다.", "The father-in-law is skinny. (the book’s model: A picks 장인, B uses 마르다)"), ("어머니", "어머니는 안경을 꼈습니다.", "Mother is wearing glasses. (mine)"), ("삼촌", "삼촌은 뚱뚱합니다.", "Uncle is chubby. (mine; 뚱뚱하다 is a stative verb in the present)")]
_CATS = [("Marriage", "결혼하다, 이혼하다, 약혼하다, 재혼하다"), ("Weather", "(구름/안개/먼지) 끼다"), ("Physical appearance", "마르다, 늙다, (잘/못) 생기다, (안경을) 끼다, (옷을) 입다")]
L6 = lesson(
    "Ch 25 · Grammar A: past tense verbs for a present state or condition",
    "결혼했습니다 · 안경을 꼈습니다 · 말랐습니다 · 결혼했었습니다",
    requires=[],
    cards=[
        card("A. Past tense verbs for a present state or condition",
             "Look at the literal meanings of the following sentences that contain a verb in the past tense. Note that these sentences all imply that an action that took place in the past is still in effect. There are quite a few verbs in Korean that “behave” this way. For now, however, we will focus on the verbs in this chapter for practice. These verbs can be broken into three categories.",
             tables=[table(["Category", "Verbs"], [[c, v] for c, v in _CATS])],
             examples=passage(_G1[:4])),
        card("More examples",
             "In the book’s examples:",
             examples=passage(_G1[4:])),
        card("A past state that is no longer in effect",
             "To imply a present state or condition that is no longer in effect, we add 었 to the past tense of the verb. For example:",
             examples=passage(_G1B)),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Verb", "Meaning", "-았/었습니다 (still in effect)", "-았/었었습니다 (no longer)"], [[v, m, _pres(v), _pdone(v)] for v, m in _PAST_V], say=[0, 2, 3])]),
        card("Follow-up 1: the model",
             "Student A picks a person from one pot and reads it aloud; Student B picks a verb from the other pot and makes a sentence that describes the current physical appearance of the person. The book’s model is the first line; the others are my sample sentences (the English is mine).",
             tables=[table(["A (person)", "B (a sentence)", "Meaning"], [[a, b, c] for a, b, c in _G1C], say=[0, 1])]),
        card("Activities left out",
             "Follow-up 1’s pots (a partner activity) and Follow-up 2 (listening to segments of a conversation about a woman’s family members in a photo and noting each person’s physical appearance) are partner and audio activities."),
    ],
    exercises=uniq(
        _fk(_PAST_V, _pres, "past (a state still in effect)", lambda v: [_pdone(v), stem(v) + "습니다", stem(v) + "겠습니다", stem(v) + "고 있습니다"])
        + _fk(_PAST_V, _pdone, "past (a state no longer in effect)", lambda v: [_pres(v), stem(v) + "습니다", stem(v) + "겠습니다", stem(v) + "었었어요" if False else stem(v) + "고 있었습니다"])
        + _tr(_G1 + _G1B)
        + [M("What does 저는 이 월에 입대했습니다 imply?", "I joined in February and I am in the military now", ["I left the military", "I will join", "I joined but have left"], "A past action still in effect."), M("What does 김 선생님은 결혼했었습니다 imply?", "He was married once and no longer is", ["He is married now", "He will marry", "He is engaged"], "-았었 = no longer in effect."), M("What does 제 아내는 말랐습니다 mean?", "My wife is skinny", ["My wife was skinny once", "My wife will get thin", "My wife is fat"], "마르다 in the past = is thin now."),
           M("What does 아침에 안개가 꼈었습니다 mean?", "It was foggy in the morning (and no longer is)", ["It is foggy now", "It will be foggy", "It is not foggy"], "꼈었습니다."), M("What does 여동생은 안경을 꼈습니다 mean?", "My younger sister is wearing glasses", ["My sister took off glasses", "My sister will wear glasses", "My sister lost glasses"], "안경을 끼다 in the past = is wearing."),
           F("제 아내는 ___. (is skinny)", "말랐습니다", ["마릅니다", "마르겠습니다"], "마르다 in the past: 말랐습니다."), F("나는 작년에 ___. (got married and still am)", "결혼했습니다", ["결혼합니다", "결혼하겠습니다"], "결혼했습니다."), F("김 선생님은 결혼___습니다. (was married once)", "했었", ["했", "하겠"], "했었습니다 = no longer."), F("그 영화배우는 잘 ___습니다. (is handsome)", "생겼", ["생기겠", "생기"], "잘 생겼습니다."),
           read_q("나는 작년에 결혼했습니다"), read_q("저는 이 월에 입대했습니다"), read_q("그 영화배우는 잘 생겼습니다"), read_q("제 아내는 말랐습니다"), read_q("김 선생님은 결혼했었습니다")]
    ),
)

# ================================================================== L7: Grammar B: contractions of 는 and 를
def _contract(w):
    """아버지는 -> 아버진, 우유를 -> 우윌: ㄴ / ㄹ is added under the last syllable, which must have no final"""
    l, v, t = _K.decompose(w[-2])
    assert t == "" and w[-1] in "는를", w
    return w[:-2] + _K.compose(l, v, "ㄴ" if w[-1] == "는" else "ㄹ")


_CT = [("아버지는", "father (topic)"), ("어제는", "yesterday (topic)"), ("나는", "I (topic)"), ("서울에는", "in Seoul (topic)"), ("여기는", "here (topic)")]
_CO = [("나를", "me (object)"), ("머리를", "the head, hair (object)"), ("여기를", "here (object)"), ("저기를", "there (object)"), ("누구를", "whom (object)")]
_CMORE = [("어머니는", "mother (topic)"), ("누나는", "older sister (of a man) (topic)"), ("할머니는", "grandmother (topic)"), ("너는", "you (topic)"), ("우리는", "we (topic)"), ("우유를", "milk (object)"), ("공부를", "study (object)"), ("영어를", "English (object)"), ("요리를", "cooking (object)"), ("이야기를", "a story (object)")]
_CS = [("저희 아버지는 의사이십니다.", "저희 아버진 의사이십니다.", "My father is a doctor."), ("언니는 아직도 자고 있어요.", "언니는 아직도 자고 있어요.".replace("언니는", "언닌"), "My older sister is still sleeping."), ("나는 여름이 싫어.", "난 여름이 싫어.", "I do not like the summer."), ("너는 뭐 먹을래?", "넌 뭐 먹을래?", "What do you want to eat?"),
       ("아이가 우유를 마셔요.", "아이가 우윌 마셔요.", "The child drinks milk. (the book prints 우율)"), ("철수가 방에서 공부를 하고 있어요.", "철수가 방에서 공불 하고 있어요.", "Chulsoo is studying in the room.")]
_EMAIL = [
    ("마이클에게", "To Michael,"), ("안녕! 지난 번 네가 보낸 이메일 잘 받았어.", "Hi! I received the e-mail you sent last time."), ("우리 가족에 대해서 물었지?", "You asked about my family, right?"), ("음 우선, 나는 서울 성수동에 살아.", "Well, first, I live in Seongsu-dong in Seoul."), ("그리고 우리 가족은 모두 여덟 명이야.", "And my family is eight people in all."),
    ("아버지는 고등학교에서 영어를 가르치시고, 어머니는 화장품 가게를 하고 계셔.", "My father teaches English at a high school, and my mother runs a cosmetics shop."), ("형과 누나는 대학교에 다니고 있고, 우리 남동생과 여동생은 고등학교와 중학교에 다녀.", "My older brother and sister attend university, and my younger brother and sister go to high school and middle school."),
    ("우리 동생들은 성격이 외향적이야.", "My younger siblings are outgoing."), ("아주 활달하고 말도 많은 편이지.", "They are very lively and talk a lot."), ("너도 동생이 있니?", "Do you have younger siblings, too?"), ("그리고, 우리 누나는 아주 말랐는데도 매일 다이어트를 해.", "And my sister is very skinny, yet she goes on a diet every day."),
    ("나는 형하고 제일 친해.", "I am closest to my older brother."), ("우리 형은 성격이 내성적이고 조용한 편이야.", "My older brother is introverted and rather quiet."), ("아, 그리고 내가 제일 좋아하는 우리 할머니는 성격이 좀 급하신 편이지만 아주 좋으셔.", "Oh, and my grandmother, whom I like best, is a little short-tempered, but she is very nice."),
    ("너희 가족은 어떠니?", "How about your family?"), ("잘 지내고, 다시 연락할게.", "Take care, and I’ll get in touch again."), ("민수가", "From Minsoo"),
]
_EM_ANS = [("나는", "난"), ("아버지는", "아버진"), ("어머니는", "어머닌"), ("누나는", "누난"), ("나는", "난"), ("누나는", "누난"), ("할머니는", "할머닌")]
_FU45 = [("저는 영어를 공부합니다.", "I study English. (the book’s model, Partner A)"), ("전 영얼 공부합니다.", "I study English. (the book’s model, Partner B: contracted)"), ("신 일병, 가족이 많아요?", "PFC Shin, do you have a big family? (the book’s model dialog)"), ("아니요, 부모님과 누나만 있어요.", "No, there are only my parents and my older sister."), ("누난 어떻게 생겼어요?", "What does your older sister look like?"), ("우리 누난 아주 날씬해요.", "My older sister is very slim."), ("성격은 어때요?", "What is her personality like?"), ("아주 활발한 편이에요.", "She is rather outgoing."), ("이 일병 누난 요릴 잘 해요.", "PFC Lee’s older sister cooks well. (the book’s model presentation)"), ("그리고 좀 말랐습니다.", "And she is a little thin.")]
L7 = lesson(
    "Ch 25 · Grammar B: contractions of the topic marker 는 and the object marker 를",
    "아버진 · 난 · 넌 · 우윌 · 공불 · 누굴 · 제 누난 아주 날씬해요",
    requires=[],
    cards=[
        card("B. Contractions of the topic marker and the object marker",
             "Contracted forms like I’m, you’re, it’s, I’d, she’s, I’ve, etc., are frequently used in English, especially in informal settings. Likewise, Korean has two contracted forms commonly used in colloquial speaking: ~ㄴ and ~ㄹ. The topic marker 는 and the object marker 를 can be contracted into simple consonants, ~ㄴ and ~ㄹ, respectively. (The ㄴ or ㄹ is written under the last syllable of the noun, which therefore must have no final consonant of its own.)",
             tables=[table(["~는", "→ ~ㄴ"], [[a, _contract(a)] for a, _ in _CT], say=[0, 1]), table(["~를", "→ ~ㄹ"], [[a, _contract(a)] for a, _ in _CO], say=[0, 1])]),
        card("Sentences with the contractions",
             "The book’s six sentences (the contracted word is the second form; the book prints 우율 for 우윌 in the fifth sentence, which is a misprint; the English is the book’s).",
             examples=passage([(b, c) for a, b, c in _CS])),
        card("Forms (mine)",
             "A few more nouns with the contractions, made by the book’s rule.",
             tables=[table(["Noun + marker", "Contracted", "Meaning"], [[a, _contract(a), m] for a, m in _CMORE], say=[0, 1])]),
        card("Follow-up 3 (Reading and Writing): an e-mail from Minsoo to Michael",
             "The book asks you to circle all the nouns and markers in the e-mail that can be contracted into ~ㄴ or ~ㄹ and write their contracted forms in a table with eight blanks, the first done (나는 → 난). The text is the book’s (the ellipsis is left out and 8명 is spelled out); the English is mine. The book glosses 외향적: to be outgoing, extroverted.",
             examples=passage(_EMAIL)),
        card("The table filled in (mine)",
             "The book leaves the table blank. I found seven nouns with 는 that can be contracted (the other nouns end in a consonant, so they take 은 and cannot be contracted); there are no 를 forms in the e-mail.",
             tables=[table(["Noun + marker", "Contracted form"], [[a, b] for a, b in _EM_ANS], say=[0, 1])]),
        card("Follow-up 4 and 5: the models",
             "In Follow-up 4, Student A reads a sentence strip and Student B contracts the noun and marker. In Follow-up 5 (제 누난 아주 날씬해요) you describe your family members’ appearance and personality with classmates, using the contractions. The book’s models (the English is mine):",
             examples=passage(_FU45)),
        card("Activities left out",
             "Follow-up 4’s sentence strips and Follow-up 5’s table and exchanges (partner activities) are partner activities."),
    ],
    exercises=uniq(
        _fk(_CT + _CO + _CMORE, _contract, "contracted", lambda w: [w[:-1], w[:-2] + _K.compose(*_K.decompose(w[-2])[:2], "ㄹ" if w[-1] == "는" else "ㄴ"), w[:-1] + "은" if w[-1] == "는" else w[:-1] + "을", w])
        + _tr([(b, c) for a, b, c in _CS] + [(a, b) for a, b in _EM_ANS], k=3)
        + [M("What does ~ㄴ stand for?", "the contracted topic marker 는", ["the contracted object marker 를", "the subject marker", "the plural marker"], "아버지는 → 아버진."), M("What does ~ㄹ stand for?", "the contracted object marker 를", ["the contracted topic marker 는", "the subject marker", "the past tense"], "나를 → 날."), M("Where is the ㄴ or ㄹ written?", "Under the last syllable of the noun", ["After the noun", "Before the noun", "On the verb"], "아버지는 → 아버진."),
           M("Why can’t 가족은 be contracted?", "가족 ends in a consonant, so it takes 은, not 는", ["It is a verb", "It is too long", "It is formal"], "Only 는 and 를 after a vowel contract."), M("In what setting are the contractions used?", "Colloquial, informal speech", ["Formal writing", "Official announcements", "Military orders"], "They are used in colloquial speaking."),
           F("아버지는 → ___", "아버진", ["아버질", "아버지ㄴ"], "는 → ㄴ."), F("나를 → ___", "날", ["난", "나ㄹ"], "를 → ㄹ."), F("누구를 → ___", "누굴", ["누군", "누구ㄹ"], "를 → ㄹ."), F("서울에는 → ___", "서울엔", ["서울엘", "서울에ㄴ"], "는 → ㄴ."), F("저희 아버지는 의사이십니다 → 저희 ___ 의사이십니다.", "아버진", ["아버질", "아버지는"], "저희 아버진."), F("난 여름이 ___. (I do not like)", "싫어", ["좋아", "많아"], "싫다 = to dislike."),
           read_q("아버진"), read_q("난 여름이 싫어"), read_q("넌 뭐 먹을래"), read_q("제 누난 아주 날씬해요"), read_q("이 일병 누난 요릴 잘 해요")]
    ),
)

# ================================================================== L8: Topic C
_C_DLG = [
    ("제임스", "은영 씨, 요즘 한국 가정이 예전과 많이 달라요?", "Eunyoung, are Korean families these days very different from before?"),
    ("은영", "네, 전에는 주로 대가족이었는데 요즘은 핵가족이 대부분이에요.", "Yes, before they were mostly extended families, but these days most are nuclear families."),
    ("제임스", "그래요? 또 어떤 변화가 있어요?", "Is that so? What other changes are there?"),
    ("은영", "음, 요즘에는 결혼을 늦게 하거나 안 하는 사람들도 많아요. 그리고 대부분 자녀를 한 명이나 두 명만 낳아요.", "Well, these days there are many people who marry late or don’t marry. And most have only one or two children."),
    ("제임스", "또, 아이를 갖지 않는 부부도 늘어나고 있죠?", "Also, couples who don’t have children are increasing, right?"),
    ("은영", "맞아요. 그래서 한국 인구 수가 줄어들고 있대요.", "That’s right. So they say the population of Korea is decreasing."),
    ("제임스", "그렇군요! 한국도 미국처럼 맞벌이 부부가 많죠?", "I see! Korea also has many dual-income couples, like America, right?"),
    ("은영", "네. 맞벌이 부부와 직장 여성이 많아져서 여성들의 삶이 많이 달라졌어요. 예를 들면, 전에는 집안일을 여자들만 했는데, 요즘에는 남자들도 같이 해요.", "Yes. As dual-income couples and working women have increased, women’s lives have changed a lot. For example, before, only women did the housework, but these days men do it together."),
    ("제임스", "그리고 요즘에는 한국사람들도 국제결혼을 많이 하는 것 같아요. 그렇죠?", "And these days it seems Koreans also have many international marriages. Right?"),
    ("은영", "그래요. 그래서 한국 사회에 다문화가정이 늘어나고 있잖아요.", "That’s right. So multicultural families are increasing in Korean society, you know."),
]
_C_WORDS = ["가정", "가지다 / 갖다", "낳다", "늘다 / 늘어나다", "다문화가정", "변하다", "변화", "삶", "수 / 숫자", "예를 들면", "예전", "-(으)ㅁ", "자녀", "-잖아요", "전업주부", "줄다 / 줄어들다", "직장"]
_GA = [("대가족", "an extended family (the book’s guess item)"), ("조각가", "a sculptor (mine; 조각: carving, sculpture)"), ("가출", "running away from home (mine)"), ("전문가", "an expert; a specialist (mine)"), ("가장", "a household head; “family head”"), ("가옥", "a house; “family home”"), ("가축", "a domestic animal; cattle; livestock; “household animal”"), ("화가", "a painter; “person who draws pictures”"), ("작가", "a writer; an author; “person who creates/makes”"), ("발명가", "an inventor; “person who invents”")]
L8 = lesson(
    "Ch 25 · Topic C: Changes in Korean families",
    "한국 가정의 변화 · 핵가족 · 다문화가정 · 맞벌이 부부 · 가 (家)",
    requires=[],
    cards=[
        card("Topic C: Changes in Korean families (한국 가정의 변화)",
             "James, an exchange student, is discussing changes in Korean families with his Korean classmate. (The English is mine; the book gives none. The book’s footnote: 국제결혼, which literally means “international marriage,” refers to a marriage between people of different nationalities or with different cultural/racial backgrounds.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Cultural note: 다문화가정",
             "Living in Korea, you will often see 다문화가정 (multicultural family). This term refers to a family of Korean nationals (usually men), immigrant spouses, and their children. The number of these families has been growing rapidly since 2000 because of the huge influx of foreign nationals seeking the “Korean dream” and the growing number of Koreans in rural areas marrying people of different races or nationalities. According to the Statistics Agency, approximately 7.2 % of all marriages in Korea in 2021 were “international,” and among them, 62.1% were between Korean men and foreign wives."),
        card("Sino-Korean in use: 가 (家)",
             "This Sino-Korean syllable means home, family, or household, as in 처가 (one’s wife’s [parents’] home; “wife’s house”), 가장 (a household head; “family head”), 가옥 (a house; “family home”), and 가축 (a domestic animal; cattle; livestock; “household animal”). This Sino-Korean syllable is also used to mean (professional) man or person, which is equivalent to -er or -or in English, as in 화가 (a painter; “person who draws pictures”), 작가 (a writer; an author; “person who creates/makes”), and 발명가 (an inventor; “person who invents”). The book asks you to guess 대가족, 조각가, 가출 and 전문가; the answers are mine.",
             tables=[ktable(_GA)]),
        card("Activities left out",
             "The SMART Board activities and the pair reading of Topic C in the Presentation Activity are computer and partner activities. Follow-up 1 (listening to three conversations between two family members and noting their relationship and the topic) is an audio activity. Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if "/" not in w and "(" not in w and "-" not in w]))
        + _tr(_strip(_C_DLG) + _GA)
        + [M("What was Korean families’ main type before?", "Extended families", ["Nuclear families", "Single-person households", "Multicultural families"], "전에는 주로 대가족."), M("What is most common these days?", "Nuclear families", ["Extended families", "Four-generation families", "Multicultural families only"], "요즘은 핵가족이 대부분."), M("What other changes does Eunyoung mention?", "Late or no marriage and one or two children", ["Earlier marriage", "Larger families", "More sons"], "결혼을 늦게 하거나 안 하는 사람들, 자녀를 한 명이나 두 명."),
           M("What is happening to the population of Korea?", "It is decreasing", ["It is increasing", "It is not changing", "It is doubling"], "인구 수가 줄어들고 있대요."), M("How have women’s lives changed?", "Men now do housework together with women", ["Women no longer work", "Women do all housework", "Women live alone"], "요즘에는 남자들도 같이 해요."), M("What does 국제결혼 mean?", "a marriage between people of different nationalities", ["a marriage of two Koreans", "a late marriage", "a wedding trip"], "International marriage."),
           M("What is a 다문화가정?", "a multicultural family", ["a nuclear family", "an extended family", "a dual-income couple"], "다문화가정 = multicultural family."), M("What does 가 (家) mean in 화가?", "a (professional) person", ["a home", "a family", "an ancestor"], "화가 = painter."), M("What does 가 (家) mean in 가옥?", "a home", ["a (professional) person", "an ancestor", "next"], "가옥 = a house."),
           F("요즘은 핵가족이 ___이에요. (most)", "대부분", ["약간", "예전"], "대부분 = most."), F("한국 인구 수가 줄어들고 ___대요. (is)", "있", ["없", "하"], "줄어들고 있대요."), F("결혼을 ___ 하거나 안 하는 사람들도 많아요. (late)", "늦게", ["일찍", "자주"], "늦게 = late."), F("한국 사회에 다문화가정이 늘어나고 ___. (you know)", "있잖아요", ["있어요", "있습니다"], "-잖아요 reminds of what is obvious."),
           read_q("한국 가정이 예전과 많이 달라요"), read_q("요즘은 핵가족이 대부분이에요"), read_q("아이를 갖지 않는 부부도 늘어나고 있죠"), read_q("맞벌이 부부가 많죠"), read_q("다문화가정이 늘어나고 있잖아요")]
    ),
)

# ================================================================== L9: Topic C follow-ups
_ST = [
    ("박태수 씨 가정은 다문화가정입니다.", "Mr. Park Taesu’s family is a multicultural family."), ("박태수 씨는 몇 년 전에 베트남에서 온 여성하고 결혼했어요.", "Mr. Park married a woman from Vietnam a few years ago."), ("시골에서 부인과 작년에 낳은 딸하고 살고 있어요.", "He lives in the countryside with his wife and the daughter born last year."),
    ("박태수 씨 부인은 한국 사람이 아니지만 한국 음식을 아주 좋아하고 한국말도 잘 합니다.", "Mr. Park’s wife is not Korean, but she likes Korean food very much and also speaks Korean well."), ("그리고 시부모님하고도 잘 지내서 박태수 씨는 늘 기쁩니다.", "And she gets along well with her parents-in-law, so Mr. Park is always happy."),
    ("정병국 씨 가족은 대가족입니다.", "Mr. Jeong Byeongguk’s family is an extended family."), ("그래서 식구 수도 아주 많아요.", "So the number of family members is also very large."), ("조부모님과 부모님 그리고 부인과 아들 둘, 딸 하나, 모두 아홉 명입니다.", "There are nine in all: grandparents, parents, his wife, two sons and one daughter."),
    ("정병국 씨는 집안의 장남이어서 여러 가지 일들을 해야 합니다.", "Mr. Jeong is the oldest son of the family, so he has to do various things."), ("또 정병국 씨 부인도 큰 며느리니까 집안살림으로 항상 바쁩니다.", "Also Mr. Jeong’s wife is the oldest daughter-in-law, so she is always busy with the household."),
    ("이세나 씨는 늦게 결혼한 직장 여성입니다.", "Ms. Lee Sena is a working woman who married late."), ("그런데 부부가 같이 일을 해서 아이 가질 계획을 아직 못 하고 있어요.", "But since the couple both work, they are still not able to plan to have a child."), ("집안일은 보통 남편과 같이 합니다.", "She usually does the housework together with her husband."),
    ("아침 식사 준비와 설거지는 남편이 하고 이세나 씨는 저녁 식사를 준비합니다.", "Her husband does the breakfast preparation and the dishes, and Ms. Lee prepares dinner."), ("집안 청소는 주말에 남편하고 같이 합니다.", "She cleans the house together with her husband on weekends."),
]
_ART = [
    ("한국 가정 이렇게 변하고 있다", "Korean families are changing like this (the headline)"), ("한국 가정의 가족 수는 매년 줄어 들고 있다.", "The number of members in Korean families is decreasing every year."), ("대부분의 가정은 부부 자녀 형태의 핵가족이다.", "Most families are nuclear families of the “couple and children” type. (the book writes ‘부부+자녀’)"),
    ("그러나, 요즘은 이런 부부 자녀 가족 형태도 줄고 있다.", "However, these days this “couple and children” type of family is also decreasing."), ("부부 가정과 일 인 가정이 늘고 있다.", "“Couple” households and “one-person” households are increasing. (the book writes ‘1인’)"),
    ("결혼 연령과 첫 자녀를 낳는 연령이 매년 올라가고 있다.", "The age at marriage and the age of having the first child are rising every year."), ("삼십 세 이상 여성이 첫 아이를 낳는 사례를 주변에서 쉽게 찾아 볼 수 있다.", "Cases of women aged 30 or over having their first child can be easily found around us."),
    ("또한, 첫 아이를 가지는 시기가 늦어지면서 자녀도 한 두 명만 낳는 부부가 늘어나고 있다.", "Also, as the timing of having the first child gets later, couples who have only one or two children are increasing."), ("그리고 맞벌이 부부가 늘어나면서 집안일을 부부가 함께 하는 가정이 많아지고 있다.", "And as dual-income couples increase, families in which the couple do the housework together are becoming more common."),
    ("청소, 빨래, 아이 돌보기, 요리 등의 집안일이나 자녀 교육을 부부가 함께 하는 가정이 늘어나고 있다.", "Families in which the couple together do housework such as cleaning, laundry, childcare and cooking, or the children’s education, are increasing."),
]
_TOPICS25 = [("핵가족", "a nuclear family"), ("다문화가정", "a multicultural family"), ("집안일 함께 하는 부부", "a couple who do the housework together"), ("자녀를 안 갖는 부부", "a couple who do not have children")]
_BOGI = [("예전의 한국 가정", "Korean families in the past"), ("현재의 한국 가정", "Korean families at present"), ("식구 수가 많다", "the number of family members is large"), ("식구 수가 적다", "the number of family members is small")]
L9 = lesson(
    "Ch 25 · Topic C, Follow-up 2 and Activity 3: modern and traditional families, an article",
    "다문화가정 · 대가족 · 직장 여성 · 한국 가정 이렇게 변하고 있다",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): modern or traditional?",
             "The book asks you to read three stories and write “Modern” if the story is about a modern trend or “Traditional” if it is about traditional Korean practices, and then to circle or underline the parts that describe the trend or tradition. The text is the book’s; the English is mine.",
             examples=passage(_ST)),
        card("The answers (mine)",
             "The book leaves the blanks empty; these are my answers.",
             tables=[table(["Story", "Modern or traditional", "The part that shows it"], [["1. Mr. Park Taesu", "Modern", "A multicultural family: he married a woman from Vietnam"], ["2. Mr. Jeong Byeongguk", "Traditional", "An extended family; he is the oldest son and his wife the oldest daughter-in-law, with many duties"], ["3. Ms. Lee Sena", "Modern", "A late marriage; a working woman who shares the housework with her husband"]])]),
        card("Activity 2: the four topics",
             "In Activity 2 (listening) you choose, for each of three conversations between colleagues, the relevant topic; one topic has no match. The book’s topics:",
             tables=[ktable(_TOPICS25)]),
        card("Activity 3 (Reading): an article about changes in present-day Korean families",
             "Before reading, you write in English what you think the article will be about; then you read it and write down the changes noted. The text is the book’s (30세 is spelled out; the plus signs and quotation marks are left out); the English is mine. The book glosses 형태: a type; 사례: an example; 시기: timing.",
             examples=passage(_ART)),
        card("The changes noted (mine)",
             "The book leaves the blanks empty; these are my answers.",
             tables=[table(["Changes noted in the article (mine)"], [["The number of members per family is decreasing every year"], ["The “couple and children” nuclear family is decreasing; couple-only and one-person households are increasing"], ["The age of marriage and of having the first child keeps rising; couples with only one or two children are increasing"], ["Couples increasingly do the housework (cleaning, laundry, childcare, cooking) and the children’s education together"]])]),
        card("Activity 4: the model",
             "In Activity 4 (한국 가정의 과거와 현재) you listen to the stories of two families, one recorded 60 years ago and one a year ago, and compare how the Korean family has changed. The book’s model for the flip chart:",
             tables=[ktable(_BOGI)]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity), Activity 2’s listening and Activity 4’s listening, group work and presentation are computer, audio and group activities."),
    ],
    exercises=uniq(
        _tr(_ST + _ART + _TOPICS25 + _BOGI)
        + [M("Which of the stories is about a multicultural family?", "The first (Mr. Park Taesu)", ["The second", "The third", "None"], "다문화가정."), M("Whom did Mr. Park Taesu marry?", "A woman from Vietnam", ["A Korean woman", "A woman from China", "A woman from America"], "베트남에서 온 여성."), M("Which story is about a traditional family?", "The second (Mr. Jeong Byeongguk)", ["The first", "The third", "None"], "대가족, 장남."), M("How many people are in Mr. Jeong’s family?", "Nine", ["Six", "Seven", "Ten"], "모두 아홉 명."),
           M("Who prepares dinner in Ms. Lee’s home?", "Ms. Lee", ["Her husband", "Her mother-in-law", "A helper"], "저녁 식사를 준비합니다."), M("Who does the dishes in Ms. Lee’s home?", "Her husband", ["Ms. Lee", "Her mother", "The children"], "설거지는 남편이 하고."), M("Why can’t Ms. Lee plan to have a child yet?", "Both she and her husband work", ["They are too young", "They live abroad", "They do not want one"], "부부가 같이 일을 해서."),
           M("What happens to the family size every year?", "It decreases", ["It increases", "It stays the same", "It doubles"], "가족 수는 매년 줄어 들고 있다."), M("What is rising every year?", "The age of marriage and of having the first child", ["The number of children", "The number of nuclear families", "The size of homes"], "결혼 연령과 첫 자녀를 낳는 연령이 매년 올라가고 있다."), M("What is increasing among households?", "Couple-only and one-person households", ["Extended families", "Large families", "Four-generation families"], "부부 가정과 일 인 가정."),
           F("정병국 씨는 집안의 ___이어서 여러 가지 일들을 해야 합니다. (the oldest son)", "장남", ["차남", "손자"], "장남 = the oldest son."), F("이세나 씨는 늦게 결혼한 ___ 여성입니다. (working)", "직장", ["핵가족", "다문화"], "직장 여성 = a working woman."), F("첫 아이를 가지는 ___가 늦어지고 있다. (timing)", "시기", ["사례", "형태"], "시기 = timing."),
           read_q("다문화가정입니다"), read_q("대가족입니다"), read_q("직장 여성입니다"), read_q("한국 가정 이렇게 변하고 있다"), read_q("집안일을 부부가 함께 하는 가정이 많아지고 있다")]
    ),
)

# ================================================================== L10: Grammar A: -잖아요
_JA_V = [("먹다", "to eat"), ("가다", "to go"), ("좋다", "to be good"), ("어렵다", "to be difficult"), ("맛있다", "to be tasty"), ("싸다", "to be cheap"), ("많다", "to be many"), ("하다", "to do")]
_JA_N = [("토요일", "Saturday"), ("한국사람", "a Korean"), ("학생", "a student"), ("의사", "a doctor"), ("제 친구", "my friend")]


def _ja(v):
    return stem(v) + "잖아요"


def _jan(n):
    return n + ("이잖아요" if has_final(n) else "잖아요")


def _jap(v):
    return _pp(v) + "잖아요"


_JA_EX = [("오늘이 무슨 요일이에요?", "What day is it today?"), ("토요일이에요.", "It is Saturday."), ("왜 직장에 안 가세요?", "How come you are not going to work?"), ("토요일이잖아요.", "(You know) it is Saturday!"), ("내가 김치를 먹잖아요.", "You know that I eat kimchi."), ("내가 김치를 먹지 않아요.", "I do not eat kimchi. (negation)"),
          ("왜 김치를 자주 먹어요?", "Why do you often eat kimchi?"), ("맛있잖아요.", "You know [it] is tasty."), ("제가 한국사람이잖아요.", "You know I am Korean."), ("한국말이 어렵잖아요.", "You know Korean is difficult."), ("그래서 열심히 공부해요.", "So I am studying hard."), ("올해가 벌써 다 갔잖아요.", "You know this year has already gone by. (the core vocabulary’s example)")]
_JA_FU = [("왜 군인식당에서 점심을 먹어요?", "Why do you eat lunch at the military dining facility? (Teacher’s question, the book’s model)"), ("한국학교에서 가깝잖아요.", "You know it is close to the Korean school. (A)"), ("무료로 먹을 수 있잖아요.", "You know we can eat there for free. (B)"),
          ("주말에 보통 어디에 가세요?", "Where do you usually go on weekends? (the book’s model for Follow-up 5)"), ("저는 몬트레이 파인스 골프장에 가요.", "I go to the Monterey Pines golf course."), ("왜요?", "Why?"), ("제가 골프를 좋아하잖아요.", "You know I like golf."), ("그리고 그 골프장이 싸잖아요.", "And you know that golf course is cheap.")]
L10 = lesson(
    "Ch 25 · Grammar C: the verb ending -잖아요 reminds of what is obvious",
    "토요일이잖아요 · 맛있잖아요 · 제가 한국사람이잖아요 · 어렵잖아요",
    requires=[],
    cards=[
        card("A. The verb ending -잖아요",
             "Compare the exchanges 오늘이 무슨 요일이에요? 토요일이에요. and 왜 직장에 안 가세요? 토요일이잖아요. Note that Speaker B’s response in the first exchange ends in 이에요. The response simply provides information Speaker A does not have. However, Speaker B’s response in the second exchange ends in 이잖아요. Thus, the response implies that the answer to the question is obvious to both parties. In other words, the verb ending –잖아(요) is used when the speaker reminds the listener of what is obvious to both parties. The ending is often translated as you know.\n\n"
             "Keep in mind that –잖아(요) is different from –지 않아(요), which is used to negate a verb.",
             examples=passage(_JA_EX[:6])),
        card("The rule: verb stem + 잖아요",
             "Verb Ending 잖아요 Used to Remind What Is Obvious: verb stem + 잖아요.",
             examples=passage(_JA_EX[6:])),
        card("Forms (mine)",
             "The forms are made by the book’s rule: the verb stem plus 잖아요 (for a noun, 이잖아요 after a final consonant and 잖아요 after a vowel); in the past, the past stem plus 잖아요, as in 갔잖아요.",
             tables=[table(["Verb", "Meaning", "-잖아요", "Past -았/었잖아요"], [[v, m, _ja(v), _jap(v)] for v, m in _JA_V], say=[0, 2, 3]), table(["Noun", "Meaning", "Noun + 이잖아요 / 잖아요"], [[n, m, _jan(n)] for n, m in _JA_N], say=[0, 2])]),
        card("Follow-up 1 and 5: the models",
             "In Follow-up 1 the teacher asks questions with obvious answers and the class answers with -잖아요. In Follow-up 5 (몬트레이에 대해 알아봅시다) you exchange information about your favorite places and the reasons. The book’s models (the English is mine):",
             examples=passage(_JA_FU)),
        card("Activities left out",
             "Follow-up 1 (class questions), Follow-up 2 (listening to three conversations in which a woman states what is obvious to both speakers) and Follow-up 5 (a partner exchange) are audio and partner activities."),
    ],
    exercises=uniq(
        _fk(_JA_V, _ja, "-잖아요", lambda v: [stem(v) + "지 않아요", stem(v) + "아요" if False else stem(v) + "네요", stem(v) + "(으)ㄹ까요" if False else stem(v) + "군요", stem(v) + "는데요"])
        + _fk(_JA_V, _jap, "past -잖아요 (“you know that … did”)", lambda v: [_ja(v), _pp(v) + "어요", stem(v) + "겠어요", stem(v) + "지 않아요"])
        + _fk(_JA_N, _jan, "noun + -잖아요", lambda n: [n + "이에요", n + "예요", n + ("이" if not has_final(n) else "") + "에요", n + "입니다"])
        + _tr(_JA_EX + _JA_FU)
        + [M("What does -잖아요 mean?", "“you know” (reminds of what is obvious)", ["a negation", "a question", "an order"], "Used when the speaker reminds the listener of what is obvious to both."), M("How is -잖아요 different from -지 않아요?", "-지 않아요 negates a verb", ["It is more polite", "It is a past tense", "It is a question"], "내가 김치를 먹지 않아요 = I do not eat kimchi."), M("What does 내가 김치를 먹잖아요 mean?", "You know that I eat kimchi", ["I do not eat kimchi", "I ate kimchi", "I will eat kimchi"], "먹 + 잖아요."),
           F("왜 직장에 안 가세요? 토요일이___. (you know)", "잖아요", ["에요", "습니다"], "토요일이잖아요."), F("왜 김치를 자주 먹어요? 맛있___. (you know it’s tasty)", "잖아요", ["어요", "네요"], "맛있잖아요."), F("제가 한국사람___. (you know I am Korean)", "이잖아요", ["잖아요", "이에요"], "한국사람 ends in a consonant: 이잖아요."), F("한국말이 어렵___. (you know)", "잖아요", ["지 않아요", "네요"], "어렵잖아요."), F("한국학교에서 가깝___. (you know it is close)", "잖아요", ["어요", "습니다"], "가깝잖아요."),
           read_q("토요일이잖아요"), read_q("맛있잖아요"), read_q("제가 한국사람이잖아요"), read_q("올해가 벌써 다 갔잖아요"), read_q("제가 골프를 좋아하잖아요")]
    ),
)

# ================================================================== L11: Grammar B: nouns derived from native Korean verbs
_NV = [("자다", "잠", "to sleep", "sleep"), ("추다", "춤", "to dance", "dance"), ("꾸다", "꿈", "to dream", "dream"), ("죽다", "죽음", "to die", "death"), ("웃다", "웃음", "to laugh; to smile", "laugh; laughter; smile"), ("졸다", "졸음", "to doze off", "sleepiness; drowsiness"), ("살다", "삶", "to live", "life"),
       ("기쁘다", "기쁨", "to be happy; to be joyful", "happiness; joy"), ("슬프다", "슬픔", "to be sad", "sadness"), ("고맙다", "고마움", "to be thankful", "gratitude; thankfulness"), ("밉다", "미움", "to be hateful", "hate; hatred")]
_NV_EX = [("어젯밤에 나쁜 꿈을 꾸었어요.", "Last night I had a nightmare / “dreamt a bad dream.”"), ("감기약을 먹어서 잠이 와요.", "I took cold medicine and I am sleepy / “sleep comes.”"), ("부부싸움을 자주 하면 아이들한테 좋지 않습니다.", "If a couple often quarrels, it is not good for the children. (the core vocabulary’s example)"), ("요즘은 가족들이 집안일을 다 같이 하기 때문에 여성들의 삶이 더 편해졌습니다.", "These days, because family members do the housework all together, women’s lives have become more comfortable. (the core vocabulary’s example)")]
_DREAM = [
    ("김 일병은 보통 열한 시에 잠을 잡니다.", "PFC Kim usually sleeps at eleven."), ("그런데 어제는 감기약 때문에 졸음이 와서 일찍 잠을 잤습니다.", "But yesterday, because of cold medicine, he became drowsy and went to sleep early."), ("김 일병은 자면서 이상한 꿈을 꾸었습니다.", "While sleeping, PFC Kim had a strange dream."),
    ("꿈 속에서 미국인 친구를 보았습니다.", "In the dream he saw an American friend."), ("그 친구는 얼음을 먹으면서 김 일병에게 한국말을 했습니다.", "The friend spoke Korean to PFC Kim while eating ice."), ("그런데 친구는 한국말을 김 일병보다 더 잘 했습니다.", "But the friend spoke Korean better than PFC Kim."), ("그리고 친구는 춤을 추기 시작했습니다.", "And the friend began to dance."), ("김 일병은 친구의 한국말과 춤을 보고 웃음이 나왔습니다.", "PFC Kim saw his friend’s Korean and dance and burst out laughing."),
]
L11 = lesson(
    "Ch 25 · Grammar D: nouns derived from native Korean verbs",
    "잠 · 춤 · 꿈 · 죽음 · 웃음 · 졸음 · 삶 · 기쁨 · 슬픔 · 고마움 · 미움",
    requires=[],
    cards=[
        card("B. Nouns derived from native Korean verbs",
             "The list below contains native Korean verbs and the nouns derived from them (the English is the book’s).",
             tables=[table(["Verb", "Noun", "Verb meaning", "Noun meaning"], [list(r) for r in _NV], say=[0, 1])]),
        card("The rule: verb stem + (으)ㅁ",
             "Note that all these nouns are formed from the stems of the verbs and (으)ㅁ. If the verb stems end in a vowel, the nouns end in ㅁ, as in 잠 and 춤. If the verb stems end in a consonant, the nouns end in 음, as in 죽음 and 웃음. If the nouns are derived from stative verbs ending in ㅂ, as in 고맙다 and 밉다, however, we drop ㅂ, add 우, and then add ㅁ: 고맙다 → 고맙 → 고마 → 고마우 → 고마움; 밉다 → 밉 → 미 → 미우 → 미움. One exception to the previous rules is 삶 (life), which is derived from 살다.",
             examples=passage(_NV_EX[:2])),
        card("More examples",
             "The core vocabulary’s examples (the English is mine).",
             examples=passage(_NV_EX[2:])),
        card("Follow-up 4 (Reading): PFC Kim’s strange dream",
             "The book asks you to circle all the nouns derived from native Korean verbs and describe in English what the dream is about. The text is the book’s (11시 is spelled out); the English is mine.",
             examples=passage(_DREAM)),
        card("The answers (mine)",
             "The book leaves the blanks empty; these are my answers.",
             tables=[table(["Task", "Answer (mine)"], [["The derived nouns", "잠, 졸음, 꿈, 춤, 웃음"], ["What the dream is about", "PFC Kim took cold medicine, got sleepy and slept early. In his dream an American friend spoke Korean to him better than he can, while eating ice, and began to dance; PFC Kim laughed at the Korean and the dance"]])]),
        card("Activities left out",
             "Follow-up 3 (a partner activity with verb lists A and B) and Follow-up 5 (몬트레이에 대해 알아봅시다) are partner activities."),
    ],
    exercises=uniq(
        [M(f"What noun is derived from {v} ({m})?", n, [x[1] for x in _NV if x[1] != n][:3], f"{v} → {n} ({e}).") for v, n, m, e in _NV]
        + [M(f"What does {n} mean?", e, [x[3] for x in _NV if x[3] != e][:3], f"{n} = {e}.") for v, n, m, e in _NV]
        + [M("How are the nouns formed from a verb stem ending in a vowel?", "Add ㅁ", ["Add 음", "Add 기", "Add 는"], "자다 → 잠."), M("How are the nouns formed from a verb stem ending in a consonant?", "Add 음", ["Add ㅁ", "Add 기", "Add 는"], "웃다 → 웃음."), M("What happens with 고맙다?", "Drop ㅂ, add 우 and then ㅁ", ["Add 음", "Add ㅁ directly", "Add 기"], "고맙다 → 고마움."),
           M("Which noun is the exception derived from 살다?", "삶", ["살음", "삶음", "살기"], "삶 = life."),
           F("어젯밤에 나쁜 ___을 꾸었어요. (a dream)", "꿈", ["잠", "춤"], "꿈을 꾸다 = to dream."), F("감기약을 먹어서 ___이 와요. (sleep)", "잠", ["꿈", "삶"], "잠이 오다 = to get sleepy."), F("친구는 ___을 추기 시작했습니다. (a dance)", "춤", ["꿈", "잠"], "춤을 추다 = to dance."), F("김 일병은 친구의 한국말을 보고 ___이 나왔습니다. (laughter)", "웃음", ["졸음", "죽음"], "웃음이 나오다."),
           F("요즘은 여성들의 ___이 더 편해졌습니다. (life)", "삶", ["잠", "꿈"], "삶 = life."), F("선생님께 ___을 느꼈습니다. (gratitude)", "고마움", ["미움", "슬픔"], "고맙다 → 고마움."),
           read_q("나쁜 꿈을 꾸었어요"), read_q("잠이 와요"), read_q("졸음이 와서 일찍 잠을 잤습니다"), read_q("춤을 추기 시작했습니다"), read_q("웃음이 나왔습니다")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Kinship terms and family relations", _CV_KIN), ("Appearance and personality", _CV_APP), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:-1] for r in rows if not any(c in r[0] for c in "~(-")]
L12 = lesson(
    "Ch 25 · Core vocabulary and self-evaluation",
    "주요 단어 · 가족 용어 · 외모와 성격 · 기타 단어 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. Where the book writes two forms together (for example 며느리/며느님 or 장모(님)), the forms are written with a slash and the honorific form is noted in the meaning.\n\n"
             "The example sentences with digits are respelled in Hangul (3대 → 삼 대, 100점 → 백 점, 1인 → 일 인). The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and talk about family types and use kinship terms; identify and talk about changes in Korean family life; and describe a person’s appearance and personality.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the verb ending –잖아요; nouns derived from native Korean verbs; past tense verbs for a present state or condition; contractions of the topic marker 는 and the object marker 를; and the Sino-Korean syllables 장 (長), 차 (次), 조 (祖), 처 (妻) and 가 (家)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does -잖아요 do?", "Reminds the listener of what is obvious", ["Negates a verb", "Asks a question", "Gives an order"], "토요일이잖아요."), M("What do the contractions ~ㄴ and ~ㄹ stand for?", "The topic marker 는 and the object marker 를", ["The subject markers", "Two verb endings", "Two honorific forms"], "아버진, 날."), M("How do nouns derived from native verbs end?", "-(으)ㅁ", ["-기", "-는", "-잖아요"], "잠, 춤, 죽음."),
           M("What is a 며느리?", "a daughter-in-law", ["a son-in-law", "a granddaughter", "a sister-in-law"], "며느리 = daughter-in-law."), M("What is a 사위?", "a son-in-law", ["a daughter-in-law", "a grandson", "a brother-in-law"], "사위 = son-in-law."), M("What is a 손자?", "a grandson", ["a granddaughter", "a son", "a nephew"], "손자 = grandson."), M("What is a 핵가족?", "a nuclear family", ["an extended family", "a dual-income couple", "a multicultural family"], "핵가족."),
           M("What is a 맞벌이?", "a dual-income couple", ["a full-time homemaker", "a single-person household", "a newlywed couple"], "맞벌이 부부."), M("What is a 전업주부?", "a full-time homemaker", ["a dual-income couple", "a reporter", "a nurse"], "전업주부."), M("What does 흔하다 mean?", "to be common", ["to be rare", "to be quiet", "to be thin"], "흔하다 = to be common."), M("What does 따로 mean?", "separately; independently", ["together", "always", "often"], "따로 = separately."),
           F("김 선생님은 ___이 아주 좋으세요. (personality)", "성격", ["식구", "직장"], "성격 = personality."), F("저희 어머니는 ___이십니다. (a full-time homemaker)", "전업주부", ["기자", "맞벌이"], "전업주부."),
           read_q("주요 단어"), read_q("한국의 가족"), read_q("핵가족"), read_q("전업주부"), read_q("다문화가정")]
    ),
)

UNIT = unit("Semester 1 · Unit 7 · Chapter 25: The Korean Family (한국의 가족)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])

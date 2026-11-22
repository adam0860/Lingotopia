"""Unit 75: KBC Semester III, Unit 16, Lesson 10 - Multicultural Families and Foreign Workers (다문화 가정 및 외국인 근로자).
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
_MATCH10 = [("과장", "to exaggerate; to overstate", "사건을 과장하다"), ("방치", "to leave something unattended; to neglect", "쓰레기를 방치하다"), ("월등", "to be superior; to be outstanding", "실력이 월등하다"), ("치안", "public security", "치안을 유지하다"), ("처지", "one’s position/situation", "어려운 처지"), ("체류", "to stay", "외국에 체류하다"), ("통합", "to integrate; to consolidate", "내용을 통합하다"), ("횡포", "tyranny; high-handedness", "횡포가 심하다")]
_CLOZE10 = [
    ("한국사회가 점점 변화하고 있다.", "Korean society is changing little by little."),
    ("특히 최근에는 외국인들과의 국제결혼이 증가하고 있다.", "In particular, recently, international marriages with foreigners are increasing. (국제결혼: international marriage)"),
    ("이런 결혼을 통해 한국으로 이민 온 여성들은 문화적 배경이 다르기 때문에 한국의 시댁 식구들과 갈등을 겪는 경우가 많다.", "Women who immigrated to Korea through such marriages often experience conflict with their Korean in-laws because their cultural backgrounds are different. (문화적 배경: cultural background; 갈등: conflict)"),
    ("또 외국인 근로자의 수도 해마다 늘고 있다.", "Also the number of foreign workers is increasing every year."),
    ("이중에는 정당한 이민이나 취업 허가 없이 일하는 불법 이주 노동자들도 상당 수 있다.", "Among them there are also quite a number of illegal migrant workers who work without proper immigration or work permits. (불법 이주 노동자: illegal migrant workers)"),
    ("이들은 대부분 신분 노출을 우려해서 부당한 대우를 받는 경우도 있다.", "Most of them, worried about exposure of their status, sometimes receive unfair treatment. (부당한: unfair; the box word 이해, “understanding,” is not used)"),
]
_HJ10 = [("農 농", "farming; agriculture", "농업, 농약"), ("談 담", "talk; conversation", "상담, 회담"), ("法 법", "law; method", "합법, 방법"), ("的 적", "goal; target; “adjective marker”", "목적, 극적"), ("後 후", "after; later", "오후, 후손")]
_HJW10 = [("농업", "agriculture"), ("농약", "agricultural chemicals"), ("상담", "counseling; consultation"), ("회담", "a meeting; a conference"), ("합법", "legality; legal"), ("방법", "a method"), ("목적", "a purpose; an object"), ("극적", "dramatic"), ("오후", "afternoon"), ("후손", "a descendant; posterity")]
_OPP10 = [("합법", "불법", "legal: illegal"), ("후손", "조상", "descendant: ancestor"), ("구체적", "추상적", "concrete: abstract")]
_SIM10 = [("상담", "상의", "consultation: discussion"), ("농민", "농부", "a farmer: a farmer"), ("방법", "방식", "a method: a way")]
_REL10 = [("A", "법률", "합법, 불법, 사법", "law: legal, illegal, judiciary"), ("B", "산업", "축산업, 농업, 공업", "industry: livestock, agriculture, manufacturing"), ("C", "이국", "외국, 타국, 다른 나라", "foreign land: foreign country, another country, other land"), ("D", "농산물", "쌀, 보리, 콩", "farm produce: rice, barley, beans")]
_L10X = [("입법", "legislation"), ("사법", "the judiciary"), ("노후", "one’s later years"), ("선배", "a senior"), ("합리적", "rational"), ("장기적", "long-term"), ("회의", "a meeting"), ("담소", "a chat"), ("농지", "farmland"), ("유기농", "organic farming"), ("버릇", "a habit"), ("상대방", "the other party"), ("축산업", "the livestock industry"), ("공업", "manufacturing industry"), ("보리", "barley"), ("콩", "beans"), ("쌀", "rice"), ("자국", "one’s own country"), ("타국", "another country"), ("이해", "understanding")]
L1 = lesson(
    "U16 L10 · Review: immigration words and Sino-Korean 農 談 法 的 後",
    "다문화 가정 및 외국인 근로자 · 단어 복습 · 한자어 복습 · 과장 · 방치 · 월등 · 치안 · 처지 · 체류 · 통합 · 횡포 · 國際結婚 · 農 談 法 的 後",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives eight phrases with one word underlined and asks you to connect each underlined word with the meaning on the right. The underline is not marked in the text; the pairs are:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH10], say=[0, 2])]),
        card("단어 복습 2: filling in the passage (my answers)", "Read the passage and fill each blank with the right word from the box (이해, 불법 이주 노동자, 부당한, 갈등, 문화적 배경, 국제결혼; one word is not an answer), and write its English meaning under the blank. The passage with my answers filled in (the English is mine):", examples=passage(_CLOZE10)),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ10], say=[2]), ktable(_HJW10)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 합법: 입법, 불법, 사법; B. 후손: 노후, 선배, 조상; C. 구체적: 합리적, 추상적, 장기적).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP10], say=[0, 1])]),
        card("한자어 복습 2: the most similar word (my answers)", "Circle the word most similar to the word on the left (A. 상담: 상의, 회의, 담소; B. 농민: 농지, 유기농, 농부; C. 방법: 방식, 버릇, 상대방).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM10], say=[0, 1])]),
        card("한자어 복습 3: the related word (my answers)", "Choose from the box (법률, 농산물, 산업, 자국, 이국) the word related to the three words on the right; 자국 is left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Why"], [list(r) for r in _REL10], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L10X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH10], k=3) + _tr(_HJW10, k=3) + _tr(_L10X, k=3) + _tr(_CLOZE10[:1] + _CLOZE10[3:4], k=2) + _tr([(a, c) for a, b, c in _OPP10], k=3)
        + [M("What does the syllable 農 (농) mean?", "farming; agriculture", ["talk", "law", "after"], "농업."), M("What does the syllable 談 (담) mean?", "talk; conversation", ["farming", "law", "after"], "상담."), M("What does the syllable 法 (법) mean?", "law; method", ["talk", "target", "after"], "합법."), M("What does the syllable 的 (적) mean?", "goal; target; adjective marker", ["farming", "law", "after"], "목적."), M("What does the syllable 後 (후) mean?", "after; later", ["farming", "talk", "law"], "오후."),
           M("Which word is the opposite of 합법?", "불법", ["입법", "사법", "방법"], "Illegal."), M("Which word is the opposite of 후손?", "조상", ["노후", "선배", "자손"], "Ancestor."), M("Which word is the opposite of 구체적?", "추상적", ["합리적", "장기적", "극적"], "Abstract."),
           M("Which word is most similar to 상담?", "상의", ["회의", "담소", "회담"], "Discussion."), M("Which word is most similar to 농민?", "농부", ["농지", "유기농", "농약"], "A farmer."), M("Which word fits 축산업, 농업, 공업?", "산업", ["법률", "농산물", "이국"], "Industry."), M("Which word fits 외국, 타국, 다른 나라?", "이국", ["법률", "산업", "농산물"], "A foreign land."),
           F("한국사회에서 ___이 증가하고 있다. (international marriage)", "국제결혼", ["국제회의", "국제전화"], "국제결혼."), F("문화적 배경이 다르기 때문에 ___을 겪는다. (conflict)", "갈등", ["이해", "대우"], "갈등."), F("신분 노출을 우려해서 ___ 대우를 받는다. (unfair)", "부당한", ["정당한", "합법한"], "부당한."), F("외국에 ___하고 있습니다. (to stay)", "체류", ["통합", "방치"], "체류하다."), F("___가 심합니다. (tyranny)", "횡포", ["처지", "치안"], "횡포.")]
        + [read_q("한국사회가 점점 변화하고 있습니다"), read_q("국제결혼이 증가하고 있습니다"), read_q("외국에 체류하고 있습니다"), read_q("치안을 유지하고 있습니다")]
    ),
)

# ================================================================== L2 Part 1
_STAT10 = [
    ("국제결혼은 점점 감소하는 추세이다.", "(Set 1, a) International marriage is on a decreasing trend."),
    ("이천 년대 중반에 다문화 가정의 수가 증가했다.", "(Set 1, b) The number of multicultural families increased in the mid-2000s."),
    ("다문화 가정의 수는 예전이나 지금이나 변함이 없다.", "(Set 1, c) The number of multicultural families is unchanged, now as before."),
    ("이주여성들은 체류나 취업 문제로 고민하지 않는다.", "(Set 2, a) Migrant women do not worry about problems of residence or employment."),
    ("다문화 가정은 대체로 저소득층이 많아서 생활문제가 가장 큰 고민이다.", "(Set 2, b) Multicultural families are mostly low-income, so living problems are their biggest worry."),
    ("다문화 가정 여성들은 가족 문제로 상담을 많이 받는다.", "(Set 2, c) Women in multicultural families receive much counseling about family problems."),
]
_IV10 = [
    ("산업에서 농업이 차지하는 비율이 줄어들고 농업의 지위가 하락하면서 농민들의 지위도 하락하게 되었다.", "(Answer 1) As the share that agriculture takes in industry has shrunk and the status of agriculture has fallen, the status of farmers has fallen too."),
    ("그리고 여성들이 지위상승으로 인해서 농촌생활과 그에 수반하는 여러 가지 문화적 가치, 가부장적 문화에 대해 거부감을 가져 농촌총각과의 결혼 기피 현상을 보이고 있기 때문에 외국인 여성과의 결혼이 증가하고 있다.", "And because women, owing to their rise in status, have a feeling of rejection toward rural life and the various cultural values that accompany it (patriarchal culture) and show a phenomenon of avoiding marriage with rural bachelors, marriages with foreign women are increasing."),
    ("이주여성들이 낯선 한국까지 오는 중요한 이유는 경제적 빈곤이다.", "(Answer 2) The important reason migrant women come all the way to unfamiliar Korea is economic poverty."),
    ("코리안 드림을 꿈꾸며 국제결혼이라는 명목으로 한국에 들어 오고자 한다.", "Dreaming of the “Korean dream,” they try to enter Korea under the pretext of international marriage."),
    ("또한 경제적 형편이 어려운 친정을 돕기 위해 결혼 알선 업체를 통해 한국으로 들어 오기도 한다.", "Also, some come to Korea through marriage-brokering agencies to help their birth families, who are in financial difficulty."),
    ("한 가지 안타까운 일은 이러한 여성들의 욕구를 상대로 중매업자와 일부 남성들이 과장된 조건 제시를 함으로써 거짓된 결혼을 하는 것이다.", "One regrettable thing is that matchmakers and some men, preying on these women’s desires, present exaggerated conditions and thereby make false marriages."),
]
_CASE10 = [
    ("지난주에 외국인 주부들을 대상으로 요리 대회가 있었어요.", "(Case 1) Last week there was a cooking contest for foreign housewives."),
    ("저는 친구들 두 명이랑 함께 태국 전통 음식을 만들어서 대회에서 삼 등을 했어요.", "I made traditional Thai food together with two friends and came in third in the contest."),
    ("저는 필리핀에서 왔어요.", "(Case 2) I came from the Philippines."),
    ("이 년 전에 돈을 벌러 한국에 와서 건설 공사장에서 일을 하고 있어요.", "I came to Korea two years ago to earn money and I work at a construction site."),
    ("그런데 의료보험이 없어서 병원에 가기 어려웠는데 무료 진료를 받아서 좋았어요.", "But I had no medical insurance so it was hard to go to the hospital, and I was glad to get free treatment."),
    ("저는 작년에 한국인 남편과 결혼해서 시골에서 농사를 지으며 살고 있어요.", "(Case 3) I married a Korean husband last year and I live in the countryside farming."),
    ("돈이 없어서 결혼식은 못 하고 혼인신고만 하고 살고 있었는데 이번에 저와 비슷한 처지의 부부들과 함께 결혼식을 올렸어요.", "We had no money so we couldn’t hold a wedding and lived having only registered the marriage, but this time I held a wedding together with couples in a similar situation to mine."),
]
_SPEAK10A = [("외국에서 온 친구나 동료를 도와준 경험이 있습니까?", "Do you have an experience of helping a friend or colleague who came from abroad?"), ("어떤 상황에서 어떤 도움을 주었는지 옆 친구와 이야기해 보세요.", "Talk with the friend next to you about what help you gave in what situation."), ("일반적으로 다문화 가정에서 겪는 어려움이 어떤 것이 있을지 생각해 보고 옆 친구와 이야기해 보세요.", "Think about what difficulties multicultural families generally experience and talk with the friend next to you.")]
L2 = lesson(
    "U16 L10 · Part 1 (도입 학습): multicultural families and migrant workers",
    "도입 학습 · 다문화가정 · 이주노동자 · 국제결혼 · 농촌총각 · 코리안 드림 · 체류 · 취업 · 상담 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 1: 다문화가정 (multicultural families) — the book’s note",
             "Traditionally, Koreans have put a great deal of importance on the concept of “one people, one nation.” But this has changed considerably as more and more foreigners have immigrated to Korea for employment or marriage. Families formed through interracial marriage are called 다문화가정, or multicultural families. Large numbers of women from Southeast Asian countries such as Vietnam and Thailand are marrying young farmers. As a result, Korean society is becoming more multicultural. Even though Korea is managing to get through this social transition, the country faces other social issues, such as cultural conflicts and discrimination. Koreans are challenged when it comes to increasing their understanding and tolerance of other cultures. In addition, it has been difficult to establish government-level support systems to embrace these new aspects of society. (Image © Kyunghyang.)"),
        card("알아봅시다 2: 이주노동자 (migrant workers) — the book’s note",
             "As the per capita income and education level increase for the average Korean, it is now difficult to find workers for the manufacturing and agricultural sectors, which are known as the “3D industries.” 3D stands for “dirty, dangerous, and difficult.” An increasing number of people from China and Southeast Asian countries are immigrating to Korea to work under temporary visas. These workers are often treated unfairly by local residents and suffer workplace discrimination related to wages and benefits. Also, should these workers lose their jobs, they quickly fall into an undocumented, illegal status. Thus, the rights of these foreign workers have become a significant social concern in Korea. In acknowledgment of the important role these workers play in the Korean economy, the government is grappling with a proper policy to deal with the issue. (Image © Kyunghyang.)"),
        card("학습활동 1 (Reading): statistics on international marriage — the statements",
             "The book gives two sets of statistics (charts, © Kyunghyang) and asks you to tick the statement that matches each. The statements are the book’s with 2000년대 written 이천 년대. The charts are not reproduced, so which statement fits depends on them; my best guesses are (b) for Set 1 and (c) for Set 2, both in line with the book’s own note above. The English is mine.",
             examples=passage(_STAT10)),
        card("학습활동 2 (Reading): an excerpt from an interview with the head of a marriage-information company",
             "In the book you read each interview answer and find the question under it that fits the answer (the Q: lines are blank). The two answers are below (© Yonhapnews); the text is the book’s with the brackets around 가부장적 문화 written as commas and the quotation marks around 코리안 드림 removed. The English is mine.",
             examples=passage(_IV10)),
        card("학습활동 2: the questions answered (mine)",
             "1. Answer 1 goes with the question 국제결혼의 대표적인 증가요인은 무엇일까요? (What is the representative factor in the increase of international marriage?); Answer 2 goes with 외국인 여성이 한국남성과 결혼하는 이유는 무엇일까요? (Why do foreign women marry Korean men?). The other two questions (국제결혼의 대표적인 대상국가는 어디인가요? and 이주노동자들이 한국에서 겪는 가장 큰 문제는 무엇일까요?) are not used.\n\n"
             "2. A. The 농촌총각 (rural bachelors) have trouble finding Korean brides: the status of agriculture and of farmers has fallen, and women, with their rising status, reject rural life and its patriarchal culture, so they avoid marrying rural bachelors.\n"
             "B. 코리안 드림 (“Korean dream”) is the dream of coming to Korea and earning money to escape poverty, like the “American dream” (here, a dream of a better economic life)."),
        card("학습활동 3: the cases (Reading)",
             "In the book you listen to three YTN news clips (tracks 001 to 003) on recent events and complete a table, then match each case below with the related clip. The cases are the book’s with the numbers spelled out (2명 → 두 명; 3등 → 삼 등; 2년 → 이 년) and the labels in the English only. Which clip matches which case depends on the audio; from the cases, the three events are a cooking contest for foreign housewives, a free medical examination for foreign workers and a group wedding for couples who could not afford one. The English is mine.",
             examples=passage(_CASE10)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK10A)),
        card("Activities left out", "학습활동 3 (Listening, tracks 001 to 003): the YTN news clips (type of event and its beneficiary). 학습활동 4 (Listening, track 004): a short speech by a university president (© YTN), with a question on the speaker’s tone (A. accusatory; B. persuasive; C. complimentary; D. sympathetic) and his main message. They are video or audio."),
    ],
    exercises=uniq(
        _tr(_STAT10, k=3) + _tr(_IV10, k=3) + _tr(_CASE10, k=3) + _tr(_SPEAK10A, k=3)
        + [M("What are multicultural families called in Korean?", "다문화가정", ["핵가족", "대가족", "한부모가정"], "다문화가정."), M("Which workers is it hard to find in Korea’s ‘3D industries’?", "Workers for manufacturing and agriculture", ["Teachers", "Doctors", "Bankers"], "The book’s note."), M("What does 3D stand for?", "Dirty, dangerous, and difficult", ["Dark, deep and dense", "Daily, direct and dry", "Dull, dim and dry"], "The book’s note."), M("What do many Southeast Asian women marry?", "Young farmers", ["Doctors", "Soldiers", "Teachers"], "The book’s note."),
           M("Why are marriages with foreign women increasing, per the interview?", "Women avoid marrying rural bachelors", ["Rural bachelors prefer foreigners only", "Farming is more profitable", "Foreign women are richer"], "농촌총각과의 결혼 기피."), M("What is the important reason migrant women come to Korea?", "Economic poverty", ["Love of Korean food", "Studying", "Tourism"], "경제적 빈곤."), M("What is regrettable about the matchmakers?", "They present exaggerated conditions and make false marriages", ["They charge nothing", "They refuse to help", "They close their offices"], "과장된 조건 제시."),
           F("농촌___과의 결혼 기피 현상이 있다. (bachelor)", "총각", ["처녀", "부부"], "농촌총각."), F("___ 드림을 꿈꾸며 한국에 들어온다. (Korean)", "코리안", ["아메리칸", "차이니즈"], "코리안 드림."), F("과장된 ___ 제시를 함으로써 거짓된 결혼을 한다. (conditions)", "조건", ["사진", "음식"], "조건."), F("저는 필리핀에서 ___. (I came)", "왔어요", ["갔어요", "살아요"], "왔어요."), F("무료 ___를 받아서 좋았어요. (medical treatment)", "진료", ["수업", "선물"], "무료 진료.")]
        + [read_q("국제결혼이 증가하고 있습니다"), read_q("이주여성들은 경제적 빈곤 때문에 한국에 옵니다"), read_q("무료 진료를 받아서 좋았습니다"), read_q("다문화 가정에서 겪는 어려움은 무엇입니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("고충", "(苦衷) difficulty; problem; distress; predicament", "회사 생활의 고충을 나눌 수 있는 동료가 있으면 좋겠어요.", "어려움 | 고민"),
        ("법률", "(法律) law; act; legislation", "정 변호사는 일반인들에게 법률 상담을 해 줍니다.", "법"),
        ("유형", "(類型) a type; a category; a pattern", "이 테스트는 사람의 성향을 크게 다섯 가지로 분류하고 있습니다."),
        ("이주(하다)", "(移住) migration; relocation (to migrate; to relocate)", "천구백칠십 년대 농촌에서 도시로 이주하는 사람들이 급격히 늘었습니다."),
        ("체류(하다)", "(滯留) staying (at a place away from home); sojourn (to stay)", "체류 기간을 좀 연장하고 싶어요.", "머무르다, 지내다"),
        ("추이", "(推移) development (of an event); progress", "사건의 추이를 지켜보고 있다."),
    ]),
    ("학습활동 2", [
        ("과장(하다/되다)", "(誇張) exaggeration; overstatement (to exaggerate; to overstate/to be exaggerated; to be overstated)", "이 신문은 사건을 과장보도하고 있습니다."),
        ("낯설다", "to be unfamiliar", "외국 생활이 처음에는 낯설고 힘들었어요.", "익숙하다"),
        ("농민", "(農民) a farmer", "폭우로 인해 농민들의 피해가 심각합니다.", "농부"),
        ("안타깝다", "to be regrettable; to be sad; to be heartbreaking; to be pitiful; to be sorry", "이번 한국말 웅변대회에서 일 등을 놓친 것이 안타깝다.", "아쉽다, 아깝다"),
        ("욕구", "(欲求) desire; drive", "모든 사람의 욕구를 다 충족시키기는 어렵습니다."),
        ("총각", "(總角) a bachelor; a single man; an unmarried man", "결혼을 한 후에 총각 때보다 더 건강해졌어요.", "처녀"),
    ]),
    ("학습활동 3", [
        ("달래다", "to appease; to soothe; to comfort", "아기가 많이 울어요. 좀 달래 주세요."),
        ("사각지대", "(死角地帶) a blind spot; “dead-angle area”", "많은 사람들이 의료 혜택의 사각지대에 놓여 있다."),
        ("의상", "(衣裳) clothes; costume; attire", "저는 의상 디자인을 전공하고 싶어요.", "의류, 옷"),
        ("처지", "(處地) one’s position or situation; circumstances", "저는 지금 휴가 갈 처지가 못 됩니다.", "상황"),
        ("향수", "(鄕愁) homesickness; nostalgia", "이 노래를 들으니 어린 시절에 대한 향수를 느끼게 됩니다.", "고향"),
    ]),
    ("학습활동 4", [
        ("귀국(하다)", "(歸國) returning to one’s home country (to return to one’s home country)", "귀국 날짜가 잡혔어요.", "출국(하다) | 입국(하다)"),
        ("눈길", "eyes; glances; attention; “eye path”", "주변의 어려운 이웃들에게 따뜻한 눈길과 사랑을 보냅시다.", "손길, 발길"),
        ("후손", "(後孫) a descendant; posterity", "그 사람은 항상 왕의 후손이라고 말합니다.", "조상 | 자손"),
    ]),
]
L3 = lesson(
    "U16 L10 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 고충 · 법률 · 유형 · 이주 · 체류 · 추이 · 과장 · 낯설다 · 농민 · 안타깝다 · 욕구 · 총각 · 달래다 · 사각지대 · 의상 · 처지 · 향수 · 귀국 · 눈길 · 후손",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book adds under 향수 (鄕愁) “homesickness; nostalgia” that 향수 (香水) means “fragrance” (perfume). The book’s examples with numbers are written out: 5가지 → 다섯 가지, 1970년대 → 천구백칠십 년대 and 1등 → 일 등. The related words of 향수 are 고향 and of 귀국하다 are 출국(하다) and 입국(하다).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=18, nread=15)),
)

# ================================================================== L4 Part 2
_WIFE10 = [
    ("결혼이민 여성이 한국에서 남편을 비롯한 시댁식구와 일차적으로 겪는 갈등 중 하나가 가사분담과 취업 문제다.", "One of the conflicts that marriage-immigrant women experience first with their in-laws, starting with the husband, in Korea is the problem of sharing housework and getting a job."),
    ("한국인 남편은 아내가 집에서 가사를 전담해 주길 원하지만 결혼이민 여성은 바깥 일을 하고 싶어하고 남편이 집안일을 도와주길 바라기 때문이다.", "This is because the Korean husband wants his wife to take charge of the housework at home, but the marriage-immigrant woman wants to do outside work and hopes that her husband will help with the housework."),
    ("특히 중국 여성은 성 평등 의식이 높아 남자가 집에서 요리나 청소 등을 하는 것을 당연히 여겨, 집안일은 여성의 몫이라고 생각하는 한국인 남편과 자주 갈등을 빚곤 한다.", "In particular, Chinese women have a high awareness of gender equality and regard it as natural for men to cook or clean at home, so they often come into conflict with Korean husbands who think that housework is the woman’s share."),
    ("여기에 결혼이민 여성의 취업문제까지 겹치면 갈등의 양상은 한층 복잡해진다.", "When the marriage-immigrant woman’s employment problem is added on top of this, the aspect of the conflict becomes still more complicated."),
    ("한국으로 오는 결혼이민 여성은 대개 취직해 돈을 벌길 원한다.", "Marriage-immigrant women who come to Korea mostly want to get a job and earn money."),
    ("이들이 주로 저소득 계층의 한국인 남편과 결혼해 경제적으로 어려운 탓도 있지만 고향의 부모를 금전적으로 도와 주고 싶어하는 측면이 크다.", "This is partly because they mostly marry Korean husbands from low-income classes and are in economic difficulty, but largely because they want to help their parents back home financially."),
    ("좀 더 나은 삶을 위해 이국 땅으로 시집온 이들이 경제적으로 풍요해지면서 그 부를 친정식구와 나누고 싶어하는 것은 인지상정.", "It is human nature that those who married into a foreign land for a better life want to share their wealth with their birth family as they become economically better off."),
    ("하지만 한국인 남편과 시댁식구들은 결혼이민 여성이 한국어를 배우고 한국문화에 익숙해지는 것이 급선무라고 생각하고 가정에만 있기를 바라고 있다.", "But the Korean husbands and in-laws think that learning Korean and getting used to Korean culture is the urgent priority for marriage-immigrant women and want them to stay only at home."),
    ("성동외국인근로자센터 다문화가족지원팀 김세정 씨는 결혼이민 여성의 가사분담과 취업문제는 가정폭력과 함께 다문화 가정이 주로 상담을 해 오는 문제라며 남편을 비롯한 시댁식구들은 결혼이민 여성의 문화적 배경과 처지를 이해하는 자세가 필요하다고 말했다.", "Kim Se-jeong of the Multicultural Family Support Team at the Seongdong Foreign Workers’ Center said that the housework-sharing and employment problems of marriage-immigrant women are, along with domestic violence, the problems for which multicultural families mainly seek counseling, and that the husband and the in-laws need an attitude of understanding the marriage-immigrant woman’s cultural background and situation."),
]
_SPEAK10B = [("주변에 성공적으로 미국 사회에 정착한 외국인 친구나 아는 사람이 있습니까?", "Do you have a foreign friend or acquaintance around you who has successfully settled in American society?"), ("옆 친구에게 그 사람의 이름, 직업, 가족 등의 신상 정보에 대해 간략하게 말해 주세요.", "Tell the friend next to you briefly about that person’s personal details such as name, job and family."), ("또 그 사람이 지금 어떻게 지내고 있는지도 이야기해 주세요.", "And also tell how that person is doing now."), ("주변 이민자 친구들에게 그들이 겪는 어려움에 대해서 들어본 적이 있습니까?", "Have you ever heard from immigrant friends around you about the difficulties they experience?"), ("아니면 뉴스에서 이민자들의 어려움에 대한 보도를 들어본 적이 있습니까?", "Or have you heard a news report about immigrants’ difficulties?"), ("한 가지 사례를 옆 친구와 이야기해 보세요.", "Talk about one case with the friend next to you.")]
_PER10 = [("Wife’s perspective", "She wants to work outside the home and wants her husband to help with housework; Chinese wives in particular see it as natural for men to cook and clean; she wants to earn money to help her parents back home and to share her wealth with her birth family"), ("Husband’s perspective", "He wants his wife to take charge of the housework at home; he thinks housework is the woman’s share; he thinks learning Korean and getting used to Korean culture is the urgent priority, so he wants her to stay at home")]
_IDEA10 = [("남편이 집안일을 같이 하고 아내는 한국어 수업에 다닙니다.", "The husband does the housework together and the wife attends Korean classes."), ("한국어를 어느 정도 배운 후에 아내가 일을 시작하기로 합니다.", "They decide that the wife will start working after learning some Korean."), ("매달 일정한 돈을 아내의 친정에 보내기로 합니다.", "They decide to send a fixed amount of money to the wife’s family every month.")]
L4 = lesson(
    "U16 L10 · Part 2 (본 학습): conflicts in multicultural families",
    "본 학습 · 결혼이민 여성 · 가사분담 · 취업 · 시댁 · 친정 · 다문화 가정 · 성 평등 · 인지상정 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2 (Reading, Writing and Speaking): a newspaper article on the difficulties of women in international marriages",
             "The following is a newspaper article on the difficulties experienced by women who have married internationally (© Yonhapnews). The text is the book’s with the quotation marks around 집안일은 여성의 몫 and in the last sentence removed. The English is mine.",
             examples=passage(_WIFE10)),
        card("학습활동 2: the questions answered (mine)",
             "1. The two causes of conflict: sharing household chores and getting a job (the checked boxes would be the second and the fourth).\n\n"
             "2. The two perspectives:",
             tables=[table(["", "Summary (mine)"], [list(r) for r in _PER10])]),
        card("학습활동 2: question 3 — ideas to improve the relationship (mine)",
             "3. In the role-play (Student A the wife and Student B the husband) you explain your positions and think up at least two ideas in Korean. Some ideas of mine:",
             examples=passage(_IDEA10)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK10B)),
        card("Activities left out", "학습활동 1 (Listening, track 005): a YTN video on Anabell, an immigrant woman who settled successfully in Korea: a table of her national origin, family and previous and current occupation, at least two voluntary services she has provided to other foreigners, her motivation and her future plan. 학습활동 3 (Listening, Writing and Speaking, tracks 006 to 008): YTN material on multicultural families: the problems women first encountered when they came to Korea, a table of the services and beneficiaries of three places in Hongseong (the 이주민 센터, the 장곡 초등학교 and the 홍성 사회복지관), the services of a multicultural family support center from an interview with a staff member, and your own Korean ideas to help multicultural families. They are video or audio."),
    ],
    exercises=uniq(
        _tr(_WIFE10, k=3) + _tr(_SPEAK10B, k=3) + _tr(_IDEA10, k=3)
        + [M("Which two problems are among the first conflicts for marriage-immigrant women?", "Sharing housework and getting a job", ["Food and weather", "Language and religion", "Travel and sports"], "가사분담과 취업 문제."), M("What does the Korean husband want his wife to do?", "Take charge of the housework at home", ["Work outside", "Study abroad", "Return home"], "가사를 전담."), M("What do Chinese women regard as natural?", "Men cooking and cleaning at home", ["Women doing all housework", "Living with in-laws", "Staying home"], "남자가 요리나 청소."), M("Why do many marriage-immigrant women want a job?", "To help their parents back home financially", ["To avoid the husband", "To buy cars", "To travel"], "고향의 부모를 금전적으로 도와 주고."), M("What do husbands and in-laws think is the urgent priority?", "Learning Korean and getting used to Korean culture", ["Finding a job", "Sending money home", "Having children"], "급선무."), M("What do multicultural families mainly seek counseling about?", "Housework, jobs and domestic violence", ["Taxes", "School grades", "Travel"], "가사분담과 취업문제는 가정폭력과 함께."), M("What does the counselor say the husband and in-laws need?", "To understand the wife’s cultural background and situation", ["To stay silent", "To pay more", "To move"], "문화적 배경과 처지를 이해하는 자세."),
           F("결혼이민 여성은 ___ 일을 하고 싶어한다. (outside)", "바깥", ["안", "작은"], "바깥 일."), F("집안일은 여성의 ___이라고 생각한다. (share)", "몫", ["일", "곳"], "몫."), F("부를 친정식구와 나누고 싶어하는 것은 ___이다. (human nature)", "인지상정", ["욕구", "처지"], "인지상정."), F("한국어를 배우는 것이 ___라고 생각한다. (urgent priority)", "급선무", ["욕구", "상담"], "급선무."), F("취업문제까지 겹치면 갈등의 ___은 한층 복잡해진다. (aspect)", "양상", ["효과", "계획"], "양상.")]
        + [read_q("가사분담과 취업 문제가 갈등의 원인입니다"), read_q("남편이 집안일을 도와주길 바랍니다"), read_q("한국어를 배우는 것이 급선무입니다"), read_q("주변에 미국 사회에 정착한 외국인 친구가 있습니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("경장", "(警長) a (police) corporal", "김응식 경장이 다음 달에 표창을 받는다고 합니다."),
        ("계발(하다)", "(啓發) development of one’s talent or ability (to develop one’s talent or ability)", "각자 자신이 가진 적성을 계발하려고 노력하세요."),
        ("공문서", "(公文書) an official document", "그 사람은 공문서 위조혐의로 조사를 받고 있습니다."),
        ("귀화(하다)", "(歸化) naturalization (to be naturalized)", "제임스는 작년에 한국인으로 귀화했습니다."),
        ("노동자", "(勞動者) a worker; a laborer", "이주 노동자들이 늘어나면서, 이주 노동자들의 인권을 옹호하는 사회단체가 생기고 있습니다.", "근로자"),
        ("매진(하다)", "(邁進) striving for (to strive for)", "성공하려면 항상 자기 발전에 매진해야 합니다."),
        ("원동력", "(原動力) driving force; impetus", "고급인력은 우리 경제 성장의 원동력입니다."),
        ("치안", "(治安) public security", "살인사건이 증가하면서 그 지역의 치안에 비상이 걸렸습니다."),
    ]),
    ("학습활동 2", [
        ("금전", "(金錢) money; cash", "친한 사람과는 금전거래는 하지 않는 것이 좋다고 합니다.", "돈"),
        ("급선무", "(急先務) an urgent priority; an urgent business matter", "우리가 해결해야 할 급선무가 뭐라고 생각하십니까?"),
        ("부", "(富) wealth; fortune; riches", "제 인생의 목표는 부를 얻는 것입니다."),
        ("양상", "(樣相) an aspect; an appearance; a condition", "현대사회에서는 삶의 양상이 많이 달라졌다."),
        ("이국", "(異國) a foreign country; a foreign land; “different country”", "이국 땅에서 우리 동포를 만나니까 정말 반가웠어요.", "타국 | 자국"),
        ("인지상정", "(人之常情) human nature; human feelings; humanness; natural", "부모가 자식을 사랑하는 것은 인지상정이다."),
        ("평등(하다)", "(平等) equality (to be equal)", "모든 사람은 평등한 기회를 가져야 합니다."),
        ("풍요하다", "(豊饒) to be abundant; to be rich", "예술 작품들은 우리의 삶을 풍요하게 해 줍니다.", "빈곤하다"),
    ]),
    ("학습활동 3", [
        ("강습", "(講習) a lesson; a class; a course; training", "스키 강습 개인 강습"),
        ("고부갈등", "(姑婦葛藤) a conflict between a mother-in-law and a daughter-in-law", "고부갈등으로 고민하는 사람들이 꽤 많습니다."),
        ("열정", "(熱情) passion; ardor; fervor", "우리 어머니는 늦게 공부를 시작하셨지만 그 열정은 젊은이들을 능가합니다."),
    ]),
]
L5 = lesson(
    "U16 L10 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 경장 · 계발 · 공문서 · 귀화 · 노동자 · 매진 · 원동력 · 치안 · 금전 · 급선무 · 부 · 양상 · 이국 · 인지상정 · 평등 · 풍요하다 · 강습 · 고부갈등 · 열정",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 노동자 reads 이주 노동자들의 늘어나면서, a slip for 이주 노동자들이 늘어나면서, which is corrected here; its examples for 강습 are the two phrases 스키 강습 and 개인 강습 (joined here, “ski lessons” and “private lessons”). The related words of 노동자 are 근로자 and of 이국 are 타국 (the same) and 자국 (the opposite).")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=17, nread=14)),
)

# ================================================================== L6 Part 3
_ED10 = [
    ("사설 이주노동자 울린 설 연휴 불법체류 단속", "(Heading) Editorial: The crackdown on illegal residents during the New Year holiday that made migrant workers cry"),
    ("설 연휴에 이뤄진 불법체류 이주노동자 단속은 다문화사회를 지향하는 한국의 두 얼굴을 잘 보여준다.", "(Paragraph 1) The crackdown on illegally staying migrant workers carried out during the New Year holiday shows well the two faces of Korea, which aims at a multicultural society."),
    ("연휴 마지막 날인 지난 십오 일 네팔 이주노동자 삼십여 명이 설 모임을 하고 있던 서울 창신동의 한 식당에 경찰과 출입국관리소 직원들이 들이닥쳤다.", "On the 15th, the last day of the holiday, police and immigration office staff stormed into a restaurant in Changsin-dong, Seoul, where some thirty Nepalese migrant workers were holding a New Year gathering."),
    ("불법도박을 단속하려 했으나, 도박 현장을 적발하지 못하자 불법체류자 신분이 드러난 아홉 명을 연행했다는 것이다.", "They had meant to crack down on illegal gambling, but when they could not catch a gambling scene, they took away nine people whose status as illegal residents was revealed."),
    ("경찰은 평소에도 불법체류자들이 모여 도박을 한다는 제보가 많이 들어온 곳이라 단속에 나섰다고 했으나, 확인 결과 제보 위치가 잘못된 것으로 드러났다.", "(Paragraph 2) The police said they took action because it was a place where many tips had come in that illegal residents gather and gamble even at ordinary times, but on checking it turned out that the location in the tip was wrong."),
    ("경찰이 내국인이든 불법체류 이주노동자든 상습적 불법도박을 단속하는 것은 당연하다.", "It is natural for the police to crack down on habitual illegal gambling, whether by locals or by illegally staying migrant workers."),
    ("그러나 평소에는 하지 않다가 굳이 설 연휴에 표적 단속할 필요가 있었는지 이해하기 어렵다.", "But it is hard to understand whether there was a need to run a targeted crackdown on the New Year holiday of all times, when they do not do it ordinarily."),
    ("이주노동자 노조의 지적대로 한쪽에서는 이주노동자를 끌어 안자면서 설 잔치를 벌이고, 다른 한편으론 설 모임을 겨냥해 단속에 나서는 것은 결코 정부가 말하는 다문화사회일 수 없다.", "As the migrant workers’ union pointed out, holding a New Year feast on one side while claiming to embrace migrant workers, and on the other side moving to crack down by targeting their New Year gathering, can never be the multicultural society the government talks about."),
    ("이주노동자는 체류 신분이 어떻든 밑바닥에서 우리 경제의 버팀목 역할을 하고 있다.", "(Paragraph 3) Whatever their residence status, migrant workers serve as a mainstay of our economy at the bottom."),
    ("그들이 없다면 중소기업이 제대로 돌아갈 수 없을 정도다.", "It is to the extent that without them small and medium-sized businesses could not run properly."),
    ("현재 국내 불법체류 이주노동자는 약 이십만 명으로 추산된다.", "The number of illegally staying migrant workers in the country is currently estimated at about 200,000."),
    ("정부가 마음만 먹는다면 대대적인 단속으로 대거 추방할 수도 있을 것이다.", "If the government made up its mind, it could even deport them in large numbers by a large-scale crackdown."),
    ("그러나 정부는 그렇게 하지 않고 있다.", "But the government is not doing so."),
    ("적당히 눈감아 주면서 때때로 단속에 나설 뿐이다.", "It only turns a blind eye moderately and steps up a crackdown from time to time."),
    ("그들의 필요성을 잘 알고 있기 때문이다.", "This is because it knows well that they are necessary."),
    ("그렇지만 불법체류 이주노동자는 늘 불안할 수밖에 없다.", "Even so, illegally staying migrant workers cannot help being always anxious."),
    ("노동 현장에서는 신분 노출을 우려해 정당한 권리마저 포기하기 일쑤다.", "At work sites it is common for them to give up even their rightful rights for fear of exposing their status."),
    ("정부는 현재와 같은 단속만으로 이주노동자 문제를 해결할 수 없음을 알아야 한다.", "(Paragraph 4) The government must realize that the migrant-worker problem cannot be solved by a crackdown alone like the present one."),
    ("그들이 없어서는 안 될 우리의 현실을 직시하고 합리적인 대안을 마련해야 한다.", "It must face squarely our reality in which we cannot do without them and prepare a rational alternative."),
    ("장기 불법체류자의 합법화를 포함해 미등록 이주노동자들을 우리 사회의 구성원으로 받아들이는 대책을 진지하게 고민할 필요가 있다.", "There is a need to think seriously about measures to accept unregistered migrant workers as members of our society, including the legalization of long-term illegal residents."),
    ("노동 현장에서 벌어지고 있는 이주노동자의 임금체불이나 비인간적 대우 같은 사업주의 횡포에도 적극 대처해야 한다.", "It must also actively deal with employers’ tyranny, such as the unpaid wages and inhumane treatment of migrant workers occurring at work sites."),
    ("어렵다고 외면하거나 방치할 문제가 아니다.", "It is not a problem to turn away from or leave unattended because it is hard."),
    ("그래야 정부가 외치는 다문화사회의 통합도 이뤄지고, 국격도 높아질 수 있을 것이다.", "Only then can the “integration of a multicultural society” the government cries out for be achieved and the stature of the nation be raised."),
]
_SPEAK10C = [("미국에도 주로 쓰리디 업종에서 일하는 불법체류자 문제가 있습니다.", "In the United States too there is the problem of illegal residents who work mainly in the 3D industries."), ("이러한 불법 체류자들에 대해 일부에서는 미국경제와 산업에 필요한 인력이라고 보는 시각도 있고 사회문제로 인식하기도 합니다.", "Regarding such illegal residents, some take the view that they are manpower needed by the American economy and industry, while others see them as a social problem."), ("불법체류자들과 관련된 사회 문제가 무엇인지 생각해 보고 이들에 대해 정부가 어떤 대책을 세워야 할지 반 친구들과 토의해 보세요.", "Think about what social problems relate to illegal residents and discuss with your classmates what measures the government should establish for them.")]
L6 = lesson(
    "U16 L10 · Part 3 (심화 학습): the New Year crackdown on migrant workers",
    "심화 학습 · 이주노동자 · 불법체류 · 단속 · 설 연휴 · 다문화사회 · 합법화 · 임금체불 · 국격 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3 (Reading): an editorial on migrant workers",
             "The following is an editorial on migrant workers (© Kyunghyang). The text is the book’s with the numbers spelled out (15일 → 십오 일; 30여 명 → 삼십여 명; 9명 → 아홉 명; 20만 명 → 이십만 명), the brackets 사설 written without brackets, and the quotation marks removed. The English is mine; the paragraph numbers are in the English only.",
             examples=passage(_ED10)),
        card("학습활동 3: the questions answered (mine)",
             "1. D — critical. The author criticizes the government’s crackdown and its lack of a real policy for migrant workers.\n\n"
             "2. On the 15th, the last day of the holiday, police and immigration office staff stormed a restaurant in Changsin-dong, Seoul, where about thirty Nepalese migrant workers were holding a New Year gathering. They had meant to crack down on illegal gambling (on a tip, whose location turned out to be wrong), but could not catch any gambling and took away nine people whose status as illegal residents was revealed.\n\n"
             "3. The sentence that exemplifies 한국의 두 얼굴 (“the two faces of Korea”): 이주노동자 노조의 지적대로 한쪽에서는 이주노동자를 끌어 안자면서 설 잔치를 벌이고, 다른 한편으론 설 모임을 겨냥해 단속에 나서는 것은 결코 정부가 말하는 다문화사회일 수 없다. Meaning: on one side the government holds a New Year feast to embrace migrant workers, and on the other it targets their New Year gathering for a crackdown; this can never be the multicultural society the government talks about.\n\n"
             "4. The role of foreign workers: whatever their residence status, they serve as a mainstay of the Korean economy from the bottom; without them small and medium-sized businesses could not run properly.\n\n"
             "5. What the author recommends: realize that crackdowns alone cannot solve the problem; face squarely that Korea cannot do without these workers; prepare rational alternatives, including seriously considering measures that accept unregistered migrant workers as members of society (legalizing long-term illegal residents); and actively deal with employers’ tyranny such as unpaid wages and inhumane treatment; the problem is not to be turned away from or left unattended, and only then can the “integration of a multicultural society” be achieved and the nation’s stature raised."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine; 3D is written 쓰리디):", examples=passage(_SPEAK10C)),
        card("Activities left out", "학습활동 1 (Listening, track 009): a YTN news item on the craze for the Korean language test in Southeast Asia: what the numbers 27,000, 17,000 and 70 represent, and which statement is not a reason many Vietnamese take the Korean language test (A. they are interested in Korean because Korean dramas and songs are popular; B. they want to work for Korean companies, which provide better working conditions and benefits; C. they want to study at higher education institutions in Korea; D. they want to come to Korea to learn professional skills systematically and then go back to Vietnam). 학습활동 2 (Listening, Writing and Speaking, tracks 010 and 011): a YTN news item on foreign workers in Korea: what caused the worker shortage in agriculture and who is now working in the fields, what attracts workers to the ginseng farms, what happened to the area’s post office last year and why, the laborers’ biggest concern, and the translation of a short sentence with your opinion of the local farmer’s request. They are video or audio."),
    ],
    exercises=uniq(
        _tr(_ED10, k=3) + _tr(_SPEAK10C, k=3)
        + [M("When did the crackdown described in the editorial take place?", "During the New Year holiday", ["During the summer", "At the Chuseok holiday", "On a weekday in May"], "설 연휴."), M("Where were the Nepalese migrant workers gathering?", "At a restaurant in Changsin-dong, Seoul", ["At a factory", "At a hotel", "At a church"], "서울 창신동의 한 식당."), M("How many people were taken away?", "Nine", ["Thirty", "One", "Two hundred"], "아홉 명."), M("What had the police meant to crack down on?", "Illegal gambling", ["Smuggling", "Fighting", "Theft"], "불법도박."), M("What was wrong with the tip?", "The location in it was wrong", ["It was too late", "It was anonymous", "It was a joke"], "제보 위치가 잘못된 것."), M("About how many illegally staying migrant workers are there?", "About 200,000", ["About 20,000", "About 2,000,000", "About 20"], "약 이십만 명."), M("How does the author describe migrant workers’ role?", "A mainstay of the economy at the bottom", ["A burden", "A threat", "Unimportant"], "버팀목."), M("What does the author say the government only does?", "Turns a blind eye and cracks down from time to time", ["Deports everyone", "Pays them well", "Ignores them fully"], "적당히 눈감아 주면서 때때로 단속."),
           F("연휴에 ___ 단속을 한 것은 이해하기 어렵다. (targeted)", "표적", ["일반", "평소"], "표적 단속."), F("이주노동자는 우리 경제의 ___ 역할을 하고 있다. (mainstay)", "버팀목", ["걸림돌", "방해물"], "버팀목."), F("신분 ___를 우려해 정당한 권리마저 포기한다. (exposure)", "노출", ["확인", "발견"], "신분 노출."), F("그들이 없다면 중소기업이 제대로 ___ 수 없다. (run)", "돌아갈", ["올라갈", "내려갈"], "돌아가다."), F("정부는 합리적인 ___을 마련해야 한다. (alternative)", "대안", ["대가", "대신"], "대안.")]
        + [read_q("설 연휴에 불법체류 단속이 있었습니다"), read_q("이주노동자는 우리 경제의 버팀목입니다"), read_q("정부는 합리적인 대안을 마련해야 합니다"), read_q("미국의 불법체류자 문제에 대해 어떻게 생각합니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("건설업", "(建設業) construction industry", "기후변화가 건설업에 어떤 영향을 미치고 있습니까?", "제조업"),
        ("농축산업", "(農畜産業) agricultural and livestock industry", "농축산업은 대표적인 일 차 산업입니다.", "수산업, 어업"),
        ("등재(하다/되다)", "(登載) registration; record (to register/to be registered)", "팔만대장경이 세계문화유산에 등재되었습니다."),
        ("매력", "(魅力) charm; attraction", "그 배우는 나이는 어리지만 매력이 있습니다."),
        ("업종", "(業種) a type of business (industry, enterprise); a category of business", "업종을 정확히 적어 주세요."),
        ("월등하다", "(越等) to be superior; to be outstanding", "그 학생은 월등히 뛰어납니다.", "뛰어나다, 우수하다"),
        ("응시(하다)", "(應試) applying for an examination; taking an examination; “responding to an exam” (to apply for an examination; to take an examination)", "응시자격을 자세히 알려 주세요."),
        ("작용(하다)", "(作用) action; effect (to act; to have an effect on)", "이 약은 몸에 어떤 작용을 합니까?"),
        ("종사(하다)", "(從事) engagement in business; following a profession (to engage in business; to follow a profession)", "아버님은 어떤 업종에 종사하고 계십니까?"),
    ]),
    ("학습활동 2", [
        ("개간(하다)", "(開墾) cultivation; land reclamation (to cultivate; to reclaim)", "우리 아버지는 황무지를 개간해서 농사를 열심히 지으셨어요."),
        ("고랭지", "(高冷地) a highland; an upland; a mountainous region or elevated mountainous plateau; “high cold land”", "강원도의 고랭지 채소는 아주 비싼 값에 팔립니다."),
        ("넉넉하다", "to be enough; to be sufficient; to be bountiful", "손님이 많이 올 것 같으니까 음식을 넉넉히 준비해 주세요.", "충분하다 | 부족하다"),
        ("몰리다", "to be cornered; to be driven into a corner; to be gathered", "여름에는 해변에 인파가 많이 몰립니다."),
        ("묵묵히", "silently", "그 분은 항상 묵묵히 일만 열심히 하십니다."),
        ("쑥대밭이 되다", "(structures, buildings, etc.) to be completely devastated; to be razed; “to become a plot of wormwood”", "토네이도로 시내 중심가가 쑥대밭이 되었습니다."),
        ("인삼", "(人蔘) ginseng", ""),
        ("품삯", "wages for manual labor", "그분은 일하는 사람들에게 품삯을 잘 주십니다.", "임금"),
        ("합법화", "(合法化) legalization", "유럽 일부 국가에서는 안락사를 합법화했습니다."),
    ]),
    ("학습활동 3", [
        ("겨냥하다", "to aim at; to target", "여름을 겨냥해서 공포영화가 많이 제작되었습니다."),
        ("국격", "(國格) stature of a nation", "지 이십 회담 개최로 국격이 높아졌습니다.", "국가품격"),
        ("내국인", "(內國人) local people belonging to a particular nation; “inside nation people”", "이 면세점은 내국인만 이용할 수 있습니다.", "외국인"),
        ("노조", "(勞組) a (labor) union", "노조 지도부가 파업을 결의했습니다.", "노동조합"),
        ("노출(하다/되다)", "(露出) exposure; disclosure (to expose; to disclose/to be exposed; to be disclosed)", "피부를 자외선에 자주 노출하지 마세요."),
        ("눈감아 주다", "to forgive; to turn a blind eye to; “to close eyes”", "이번 한 번만 눈감아 주세요.", "봐주다"),
        ("도박(하다)", "(賭博) gambling (to gamble)", "그 친구는 도박을 너무 좋아합니다."),
        ("들이닥치다", "to storm into (a place)", "경찰이 들이닥쳐서 범인을 체포했다."),
        ("밑바닥", "the bottom", "그는 밑바닥에서 시작해 최고의 자리에 올랐습니다."),
        ("방치(하다/되다)", "(放置) leaving something unattended; negligence (to leave something unattended; to leave a thing or a person alone; to leave a matter as it is; to neglect/to be neglected)", "이 문제를 그대로 방치해 둘 수 없습니다."),
        ("버팀목", "a buttress; a wooden support", "우리 큰아들이 저에게는 큰 버팀목입니다."),
        ("연행(하다/되다)", "(連行) taking (someone under custody to the police station) (to take someone [to the police station]/to be taken [to the police station])", "피의자가 경찰서에 연행되어 갔습니다.", "체포하다"),
        ("정당하다", "(正當) to be just; to be right; to be proper", "저는 정당한 방법으로 경쟁하고 싶습니다.", "부당하다"),
        ("제보(하다)", "(提報) (giving) information; report (to report; to provide tips)", "시민의 제보로 범인이 잡혔어요.", "알리다, 신고하다"),
        ("지향(하다)", "(志向) aim; support (to aim; to support)", "우리는 세계평화를 지향합니다."),
        ("직시(하다)", "(直視) looking squarely; facing (a matter) straight (to look squarely; to face [a matter] straight on; to confront)", "현재의 상황을 직시하고 해결책을 찾으세요."),
        ("진지하다", "(眞摯) to be serious; to be earnest", "", "심각하다"),
        ("추산(하다/되다)", "(推算) estimation (to estimate/to be estimated)", "경찰 추산 사망자가 이백 명쯤 됩니다.", "추정하다"),
        ("통합(하다/되다)", "(統合) integration; consolidation (to integrate; to consolidate/to be integrated; to be consolidated)", "회사에서 세 개 부서를 통합한다고 합니다."),
        ("표적", "(標的) a target; a mark", "범인은 혼자 사는 여성들을 표적으로 범행을 저질렀습니다."),
        ("합리적", "(合理的) rational; reasonable", "우리 합리적인 대안을 모색해 봅시다.", "비합리적"),
        ("횡포", "(橫暴) tyranny; high-handedness", "그것은 권력의 횡포입니다."),
    ]),
]
L7 = lesson(
    "U16 L10 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 건설업 · 농축산업 · 업종 · 월등하다 · 응시 · 종사 · 개간 · 고랭지 · 인삼 · 품삯 · 합법화 · 겨냥하다 · 국격 · 내국인 · 노조 · 노출 · 도박 · 들이닥치다 · 밑바닥 · 버팀목 · 연행 · 제보 · 직시 · 진지하다 · 추산 · 통합 · 표적 · 합리적 · 횡포",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book adds under 응시 (應試) “applying for an examination” that 응시 (凝視) means “looking at; gazing at”. The book’s examples with numbers or letters are written out: 1차 산업 → 일 차 산업, 200명쯤 → 이백 명쯤, 3개 부서 → 세 개 부서 and G20 회담 → 지 이십 회담. The book gives no examples for 인삼 and 진지하다 (whose related word is 심각하다), and prints the Hanja of 버팀목 only as 木, which is left out here. The book’s example for 방치 and 매력 repeat entries of earlier lessons.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=32, nread=26)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 10: Multicultural Families and Foreign Workers (다문화 가정 및 외국인 근로자)", [L1, L2, L3, L4, L5, L6, L7])

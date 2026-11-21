"""Unit 30: education vocabulary; negation with ни- and prepositions; 'positive negatives'
не́где, не́чего, не́кому (textbook module 7, lesson 39)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 300
L300 = lesson(
    "The education system: шко'ла, учени'к, университе'т, вы'сшее образова'ние",
    "Шко'льники у'чатся одиннадцать лет, а студе'нты — в университе'те.",
    requires=["школа", "ученик", "школьник", "образование", "университет", "институт", "факультет", "курс"],
    cards=[
        card("Stages of education",
             "Russian general education runs through eleven school grades. After that come vocational colleges and higher education.",
             tables=[table(
                 ["Stage", "English"],
                 [["де'тский сад", "kindergarten"],
                  ["нача'льная шко'ла", "primary school (grades 1–4)"],
                  ["сре'днее образова'ние", "general education (grades 1–11)"],
                  ["те'хникум, ко'лледж", "vocational college"],
                  ["вы'сшее образова'ние", "higher education"],
                  ["аспиранту'ра", "graduate school"]])],
             examples=[
                 ex("Шко'льники у'чатся оди'ннадцать лет.", "Schoolchildren study for eleven years.", "Шко'льники"),
                 ex("Она' получи'ла вы'сшее образова'ние.", "She received a higher education.", "вы'сшее образова'ние"),
             ]),
        card("People in education",
             "Pupils in grades 1–11 are ученики' or шко'льники. People at a university are студе'нты. The one who has finished is a выпускни'к.",
             tables=[table(
                 ["Word", "English"],
                 [["учени'к, учени'ца", "pupil (grades 1–11)"],
                  ["шко'льник, шко'льница", "schoolchild"],
                  ["студе'нт, студе'нтка", "university student"],
                  ["абитурие'нт", "applicant to a university"],
                  ["выпускни'к", "graduate"],
                  ["учи'тель, преподава'тель", "teacher; lecturer"],
                  ["педаго'г", "educator"]])],
             examples=[
                 ex("В на'шем кла'ссе мно'го ученико'в.", "There are many pupils in our class.", "ученико'в"),
                 ex("Выпускники' шко'лы получи'ли аттеста'ты.", "The school's graduates received their certificates.", "Выпускники'"),
             ]),
        card("Places at a university",
             "A university has факульте'ты (departments). Studying at a university is described with на for a faculty and a year, and в for the institution.",
             tables=[table(
                 ["Phrase", "English"],
                 [["в университе'те", "at the university"],
                  ["в институ'те", "at the institute"],
                  ["на факульте'те", "in the department"],
                  ["на пе'рвом ку'рсе", "in the first year"],
                  ["уче'бное заведе'ние", "educational institution"]])],
             examples=[
                 ex("Мой брат у'чится на второ'м ку'рсе.", "My brother is in his second year.", "на второ'м ку'рсе"),
                 ex("Она' у'чится на факульте'те журнали'стики.", "She studies in the journalism department.", "на факульте'те"),
             ]),
    ],
    verify=(vf("школа", "школе") + vf("ученик", "учеников") + vf("школьник", "школьники") + vf("университет", "университете")
            + vf("институт", "институте") + vf("факультет", "факультете") + vf("курс", "курсе") + vf("выпускник", "выпускники")
            + vf("студент", "студенты") + vf("учитель", "учитель") + vf("преподаватель", "преподаватель")
            + vf("образование", "образование") + vf("получить", "получила")),
    exercises=[
        F("Мой сын у'чится в ___. (school)", "шко'ле", ["шко'ла", "шко'лу", "шко'лы"], "В + prepositional: where?", "My son studies at school.", lemma="школа"),
        F("Она' у'чится на пе'рвом ___. (year of university)", "ку'рсе", ["ку'рс", "ку'рса", "ку'рсу"], "На + prepositional.", "She is in her first year.", lemma="курс"),
        F("Мой брат у'чится на на'шем ___. (department)", "факульте'те", ["факульте'т", "факульте'та", "факульте'ту"], "На факульте'те.", "My brother studies in our department.", lemma="факультет"),
        F("По'сле шко'лы она' пошла' в ___. (university)", "университе'т", ["университе'те", "университе'та", "университе'ту"], "В + accusative: where to?", "After school she went to university.", lemma="университет"),
        F("В на'шем кла'ссе мно'го ___. (pupils)", "ученико'в", ["учени'ков", "ученика'", "ученики'"], "Мно'го + genitive plural.", "There are many pupils in our class.", lemma="ученик"),
        F("Ка'ждый ___ получи'л дипло'м. (graduate)", "выпускни'к", ["выпускни'ка", "выпускни'ку", "выпускнико'в"], "Nominative singular subject.", "Every graduate received a diploma.", lemma="выпускник"),
        mc("Who is a шко'льник?", ["a child in grades 1–11", "a university student", "a lecturer", "a graduate"], "a child in grades 1–11",
           "Шко'льник is someone at school.", order=True),
        mc("Which is higher education?", ["вы'сшее образова'ние", "сре'днее образова'ние", "де'тский сад", "нача'льная шко'ла"], "вы'сшее образова'ние",
           "Вы'сшее = higher.", order=True),
        mc("Which word means ‘year of studies’?", ["курс", "предме'т", "экза'мен", "дипло'м"], "курс",
           "На пе'рвом ку'рсе = in the first year.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 301
L301 = lesson(
    "Applying to university: поступа'ть, заявле'ние, ко'нкурс, экза'мен",
    "Она' подала' докуме'нты и поступи'ла на бюдже'т.",
    requires=["поступать", "поступить", "заявление", "документ", "конкурс", "экзамен", "выпускник"],
    cards=[
        card("To apply, to be accepted",
             "Поступа'ть (imperfective) means to apply, or to be going through the admissions process. Поступи'ть (perfective) means you got in.",
             tables=[table(
                 ["Verb", "English"],
                 [["поступа'ть в университе'т", "to apply to a university"],
                  ["поступи'ть в университе'т", "to be accepted to a university"],
                  ["подава'ть докуме'нты", "to submit documents (impf.)"],
                  ["пода'ть докуме'нты", "to submit documents (pf.)"],
                  ["сдава'ть экза'мен", "to take an exam (impf.)"],
                  ["сдать экза'мен", "to pass an exam (pf.)"]])],
             examples=[
                 ex("Она' поступа'ла в МГУ три го'да.", "She tried to get into MSU for three years.", "поступа'ла"),
                 ex("Он поступи'л в МГУ.", "He got into MSU.", "поступи'л"),
             ]),
        card("The admissions process",
             "Applicants submit a заявле'ние and documents, take exams, and compete in a ко'нкурс. A successful applicant may get a бюдже'тное ме'сто, a place with no tuition.",
             tables=[table(
                 ["Word", "English"],
                 [["заявле'ние", "application"],
                  ["докуме'нты", "documents"],
                  ["ко'нкурс", "competition (among applicants)"],
                  ["экза'мен", "exam"],
                  ["бюдже'тное ме'сто", "tuition-free place"],
                  ["поступле'ние", "admission (process)"]])],
             examples=[
                 ex("На э'тот факульте'т большо'й ко'нкурс.", "There is a big competition for this department.", "ко'нкурс"),
                 ex("Он поступи'л на бюдже'т.", "He got a tuition-free place.", "на бюдже'т"),
             ]),
        card("Aspect: process or result",
             "Поступа'ть describes the effort; поступи'ть reports success. In the past you can say the first about a try, the second about the result.",
             tables=[table(
                 ["Question", "Answer"],
                 [["Ты поступа'л?", "Did you apply? (the attempt)"],
                  ["Ты поступи'л?", "Did you get in? (the result)"]])],
             examples=[
                 ex("Ты уже' поступи'л в университе'т?", "Have you got into university yet?", "поступи'л"),
             ]),
    ],
    verify=(vf("поступать", "поступала") + vf("поступить", "поступил") + vf("подавать", "подавать") + vf("подать", "подала")
            + vf("сдавать", "сдавать") + vf("сдать", "сдать") + vf("заявление", "заявление") + vf("документ", "документы")
            + vf("конкурс", "конкурс") + vf("экзамен", "экзамен")),
    exercises=[
        F("Она' ___ докуме'нты в университе'т. (submitted, pf.)", "подала'", ["подава'ла", "подаю'т", "пода'ть"], "One completed action.", "She submitted her documents to the university.", lemma="подать"),
        F("Он ___ в университе'т три го'да, но не попа'л. (kept applying)", "поступа'л", ["поступи'л", "поступи'т", "поступи'ть"], "Repeated effort: imperfective.", "He applied to university for three years but did not get in.", lemma="поступать"),
        F("Наконе'ц он ___ в университе'т! (got in)", "поступи'л", ["поступа'л", "поступа'ет", "поступа'ть"], "Result: perfective.", "At last he got into university!", lemma="поступить"),
        F("На э'тот факульте'т большо'й ___. (competition)", "ко'нкурс", ["ко'нкурса", "ко'нкурсу", "ко'нкурсы"], "Nominative singular.", "There is a big competition for this department.", lemma="конкурс"),
        F("За'втра я сдаю' после'дний ___. (exam)", "экза'мен", ["экза'мена", "экза'мену", "экза'мене"], "Accusative = nominative for inanimate.", "Tomorrow I take my last exam.", lemma="экзамен"),
        F("Она' написа'ла ___ и собрала' докуме'нты. (application)", "заявле'ние", ["заявле'ния", "заявле'нию", "заявле'нии"], "Accusative neuter = nominative.", "She wrote an application and collected her documents.", lemma="заявление"),
        mc("Which verb means ‘to pass an exam’?", ["сдать экза'мен", "сдава'ть экза'мен", "пода'ть экза'мен", "поступи'ть экза'мен"], "сдать экза'мен",
           "Perfective сдать = pass.", order=True),
        mc("What is a бюдже'тное ме'сто?", ["a tuition-free place", "a seat in class", "a student loan", "a place in a hostel"], "a tuition-free place",
           "Бюдже'т = funded by the state.", order=True),
        mc("‘Он поступи'л в МГУ’ means:", ["He got into MSU.", "He is applying to MSU.", "He left MSU.", "He teaches at MSU."], "He got into MSU.",
           "Perfective = result.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 302
L302 = lesson(
    "Knowledge and skills: зна'ния, на'вык, о'пыт, спосо'бность",
    "У неё хоро'шие зна'ния и большо'й о'пыт.",
    requires=["знание", "навык", "опыт", "способность", "способный", "предмет", "наука", "научный"],
    cards=[
        card("What you know and can do",
             "A few nouns describe what a person brings to study or work.",
             tables=[table(
                 ["Word", "English"],
                 [["зна'ния (pl.)", "knowledge"],
                  ["на'вык", "skill (built by practice)"],
                  ["о'пыт", "experience"],
                  ["спосо'бность", "ability"],
                  ["обуче'ние", "instruction, training"],
                  ["учёба", "studies"]])],
             examples=[
                 ex("У неё хоро'шие зна'ния.", "She has good knowledge.", "зна'ния"),
                 ex("Э'тот на'вык развива'ется с года'ми.", "This skill develops over the years.", "на'вык"),
             ]),
        card("Subjects and sciences",
             "A предме'т is a school subject. Нау'ка is science, and the adjective is нау'чный.",
             tables=[table(
                 ["Word", "English"],
                 [["предме'т", "(school) subject"],
                  ["нау'ка", "science"],
                  ["нау'чный", "scientific"],
                  ["специа'льность (f.)", "major, profession"],
                  ["ку'рсы (pl.)", "short courses"]])],
             examples=[
                 ex("Мой люби'мый предме'т — исто'рия.", "My favorite subject is history.", "предме'т"),
                 ex("Он за'нят нау'чной рабо'той.", "He is busy with scientific work.", "нау'чной"),
             ]),
        card("Capable people",
             "Спосо'бный means capable or gifted. It can stand alone or take a verb: спосо'бен + infinitive.",
             tables=[table(
                 ["Form", "English"],
                 [["спосо'бный студе'нт", "a gifted student"],
                  ["Он спосо'бен к языка'м.", "He has a talent for languages."]])],
             examples=[
                 ex("Э'то о'чень спосо'бный учени'к.", "This is a very gifted pupil.", "спосо'бный"),
             ]),
    ],
    verify=(vf("знание", "знания") + vf("навык", "навык") + vf("опыт", "опыт") + vf("способность", "способность")
            + vf("способный", "способный", "способен") + vf("предмет", "предмет") + vf("наука", "наука") + vf("научный", "научной")
            + vf("обучение", "обучение") + vf("учёба", "учёба") + vf("специальность", "специальность") + vf("курсы", "курсы")),
    exercises=[
        F("У неё хоро'шие ___. (knowledge)", "зна'ния", ["зна'нию", "зна'ний", "зна'нии"], "Plural nominative.", "She has good knowledge.", lemma="знание"),
        F("Э'тот ___ развива'ется с года'ми. (skill)", "на'вык", ["на'выки", "на'выку", "на'выков"], "Singular nominative.", "This skill develops over the years.", lemma="навык"),
        F("Мой люби'мый ___ — исто'рия. (subject)", "предме'т", ["предме'та", "предме'ту", "предме'те"], "Nominative singular.", "My favorite subject is history.", lemma="предмет"),
        F("У него' большо'й ___ рабо'ты. (experience)", "о'пыт", ["о'пыта", "о'пыту", "о'пыты"], "Nominative singular.", "He has a lot of work experience.", lemma="опыт"),
        F("Э'то о'чень ___ учени'к. (gifted)", "спосо'бный", ["спосо'бная", "спосо'бное", "спосо'бные"], "Masculine agrees with учени'к.", "This is a very gifted pupil.", lemma="способный"),
        F("Она' занима'ется ___ рабо'той. (scientific)", "нау'чной", ["нау'чная", "нау'чную", "нау'чные"], "Занима'ться + instrumental.", "She does scientific work.", lemma="научный"),
        mc("Which noun means ‘skill’?", ["на'вык", "о'пыт", "нау'ка", "предме'т"], "на'вык", "Skill built by practice.", order=True),
        mc("What is нау'ка?", ["science", "subject", "knowledge", "experience"], "science", "Нау'ка = science.", order=True),
        mc("Which is the adjective ‘scientific’?", ["нау'чный", "нау'ка", "нау'чить", "учёба"], "нау'чный", "The adjective ending.", order=True),
    ],
)
# ---------------------------------------------------------------------------- 303
L303 = lesson(
    "Developing and achieving: развива'ть, достига'ть, добива'ться, относи'ться к",
    "Она' доби'лась успе'ха и дости'гла свое'й це'ли.",
    requires=["развитие", "достижение", "достигать", "добиваться", "обсуждать", "считать", "пытаться", "относиться", "подход", "внимание"],
    cards=[
        card("Reaching a goal: two verbs with the genitive",
             "Both достига'ть / дости'чь and добива'ться / доби'ться take the genitive. The second stresses effort and persistence.",
             tables=[table(
                 ["Verb", "Typical objects", "English"],
                 [["достига'ть / дости'чь", "це'ли, результа'та, успе'ха", "to reach, achieve"],
                  ["добива'ться / доби'ться", "успе'ха, своего'", "to strive for and get"]])],
             examples=[
                 ex("Мы дости'гли свое'й це'ли.", "We reached our goal.", "дости'гли"),
                 ex("Она' доби'лась успе'ха.", "She achieved success.", "доби'лась успе'ха"),
                 ex("Он до'лго добива'лся э'того результа'та.", "He worked a long time for this result.", "добива'лся"),
             ]),
        card("Developing",
             "Развива'ть is transitive: you develop something. Развива'ться is intransitive: something develops by itself. The noun is разви'тие.",
             tables=[table(
                 ["Form", "English"],
                 [["развива'ть спосо'бности", "to develop abilities"],
                  ["развива'ться", "to develop (by itself)"],
                  ["разви'тие", "development"],
                  ["достиже'ние", "achievement"]])],
             examples=[
                 ex("Шко'ла развива'ет спосо'бности дете'й.", "The school develops children's abilities.", "развива'ет"),
                 ex("Би'знес бы'стро развива'ется.", "The business is developing quickly.", "развива'ется"),
             ]),
        card("Discuss, consider, attitude",
             "Several useful verbs and nouns of thinking go with particular cases.",
             tables=[table(
                 ["Pattern", "Example"],
                 [["обсужда'ть + acc.", "обсужда'ть вопро'с"],
                  ["счита'ть, что …", "Я счита'ю, что э'то ва'жно."],
                  ["счита'ть + acc. + instr.", "Я счита'ю его' хоро'шим учи'телем."],
                  ["пыта'ться + inf.", "Она' пыта'ется поня'ть."],
                  ["относи'ться к + dat.", "Она' хорошо' отно'сится к колле'гам."],
                  ["уделя'ть внима'ние + dat.", "Шко'ла уделя'ет внима'ние языка'м."]])],
             examples=[
                 ex("Она' хорошо' отно'сится к колле'гам.", "She treats her colleagues well.", "отно'сится к колле'гам"),
             ]),
    ],
    verify=(vf("развивать", "развивает") + vf("развиваться", "развивается") + vf("развитие", "развитие") + vf("достигать", "достигает")
            + vf("достичь", "достигли", "достигла") + vf("добиваться", "добивался") + vf("добиться", "добилась") + vf("достижение", "достижение")
            + vf("обсуждать", "обсуждали") + vf("считать", "считаю") + vf("пытаться", "пытается") + vf("относиться", "отно'сится")
            + vf("уделять", "уделяет") + vf("способность", "способности") + vf("успех", "успеха") + vf("цель", "цели")),
    exercises=[
        F("Она' доби'лась ___. (success)", "успе'ха", ["успе'х", "успе'ху", "успе'хом"], "Добива'ться + genitive.", "She achieved success.", lemma="успех"),
        F("Мы дости'гли свое'й ___. (goal)", "це'ли", ["цель", "це'лью", "це'лям"], "Достига'ть + genitive.", "We reached our goal.", lemma="цель"),
        F("Шко'ла уделя'ет внима'ние иностра'нным ___. (languages)", "языка'м", ["языки'", "языко'в", "языка'ми"], "Уделя'ть внима'ние + dative.", "The school pays attention to foreign languages.", lemma="язык"),
        F("Вчера' мы це'лый час ___ э'тот вопро'с. (discussed)", "обсужда'ли", ["обсуди'ли", "обсу'дим", "обсужда'ть"], "Целый час — a process: imperfective.", "Yesterday we discussed this question for a whole hour.", lemma="обсуждать"),
        F("Она' хорошо' ___ к колле'гам. (treats)", "отно'сится", ["относи'л", "отнесётся", "относи'ться"], "Относи'ться к + dative.", "She treats her colleagues well.", lemma="относиться"),
        F("Би'знес бы'стро ___. (is developing)", "развива'ется", ["развива'ет", "разви'л", "развива'ть"], "Intransitive: -ся.", "The business is developing quickly.", lemma="развиваться"),
        F("Шко'ла ___ спосо'бности дете'й. (develops)", "развива'ет", ["развива'ется", "развива'ться", "развива'ют"], "Transitive: object спосо'бности.", "The school develops children's abilities.", lemma="развивать"),
        F("Он счита'ет, ___ э'то ва'жно. (that)", "что", ["чего'", "чему'", "чем"], "Счита'ть, что …", "He thinks that this is important."),
        mc("Which sentence is correct?", ["Он добива'ется успе'ха.", "Он добива'ется успе'х.", "Он добива'ется успе'хом.", "Он добива'ется успе'ху."], "Он добива'ется успе'ха.", "Genitive after добива'ться.", order=True),
        mc("In ‘Я счита'ю его' хоро'шим учи'телем’ the noun учи'телем is in the:", ["instrumental", "genitive", "dative", "accusative"], "instrumental", "Счита'ть кого' кем.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 304
L304 = lesson(
    "Prospects and demand: перспекти'вный, спрос, ры'нок труда'",
    "На ры'нке труда' большо'й спрос на специали'стов.",
    requires=["перспектива", "перспективный", "спрос", "рынок", "труд", "специалист", "правительство", "средство", "цифра"],
    cards=[
        card("The labor market",
             "Ры'нок труда' is the job market. Спрос на + accusative is demand for something, and a востре'бованный specialist is one in demand.",
             tables=[table(
                 ["Phrase", "English"],
                 [["ры'нок труда'", "the labor market"],
                  ["на ры'нке труда'", "on the job market"],
                  ["спрос на + acc.", "demand for"],
                  ["востре'бованный", "in demand, sought after"],
                  ["специали'ст", "specialist, expert"],
                  ["ка'дры (pl.)", "skilled staff"]])],
             examples=[
                 ex("На ры'нке труда' большо'й спрос на специали'стов.", "On the job market there is great demand for specialists.", "спрос на специали'стов"),
                 ex("Э'та специа'льность о'чень востре'бована.", "This major is in high demand.", "востре'бована"),
             ]),
        card("Prospects",
             "Перспекти'вы is usually plural. The adjective перспекти'вный describes something with potential.",
             tables=[table(
                 ["Word", "English"],
                 [["перспекти'вы (pl.)", "prospects"],
                  ["перспекти'вный", "promising"],
                  ["Каки'е перспекти'вы?", "What are the prospects?"]])],
             examples=[
                 ex("У молодо'го специали'ста хоро'шие перспекти'вы.", "A young specialist has good prospects.", "перспекти'вы"),
             ]),
        card("Size, difficulty and extras",
             "Four adjectives help you describe situations in reports.",
             tables=[table(
                 ["Adjective", "English"],
                 [["значи'тельный", "significant"],
                  ["кру'пный", "large-scale, major"],
                  ["сло'жный", "complicated"],
                  ["дополни'тельный", "additional"]])],
             examples=[
                 ex("Прави'тельство вы'делило дополни'тельные сре'дства.", "The government allocated additional funds.", "дополни'тельные сре'дства"),
                 ex("Э'та ци'фра о'чень значи'тельна.", "This figure is very significant.", "ци'фра"),
             ]),
    ],
    verify=(vf("рынок", "рынке") + vf("труд", "труда") + vf("спрос", "спрос") + vf("специалист", "специалистов")
            + vf("перспектива", "перспективы") + vf("перспективный", "перспективный") + vf("значительный", "значительный")
            + vf("крупный", "крупный") + vf("сложный", "сложный") + vf("дополнительный", "дополнительные")
            + vf("правительство", "правительство") + vf("средство", "средства") + vf("цифра", "цифра")),
    exercises=[
        F("На ры'нке труда' большо'й ___ на специали'стов. (demand)", "спрос", ["спро'са", "спро'су", "спро'сом"], "Спрос на + accusative.", "There is great demand for specialists on the job market.", lemma="спрос"),
        F("Э'ти специали'сты о'чень ___. (in demand, plural)", "востре'бованы", ["востре'бованный", "востре'бована", "востре'бовано"], "Short plural form.", "These specialists are in high demand."),
        F("У молодо'го специали'ста хоро'шие ___. (prospects)", "перспекти'вы", ["перспекти'ву", "перспекти'вой", "перспекти'ве"], "Plural nominative.", "A young specialist has good prospects.", lemma="перспектива"),
        F("Э'то о'чень ___ прое'кт. (promising)", "перспекти'вный", ["перспекти'вная", "перспекти'вное", "перспекти'вные"], "Masculine: прое'кт.", "This is a very promising project.", lemma="перспективный"),
        F("Прави'тельство вы'делило ___ сре'дства. (additional)", "дополни'тельные", ["дополни'тельный", "дополни'тельная", "дополни'тельное"], "Plural: сре'дства.", "The government allocated additional funds.", lemma="дополнительный"),
        F("Э'та ци'фра о'чень ___. (significant, fem. short)", "значи'тельна", ["значи'телен", "значи'тельно", "значи'тельны"], "Feminine short form.", "This figure is very significant.", lemma="значительный"),
        mc("Which phrase means ‘the job market’?", ["ры'нок труда'", "ка'дры труда'", "спрос ры'нка", "сре'дства труда'"], "ры'нок труда'", "Ры'нок + genitive.", order=True),
        mc("What follows спрос when you name the product?", ["на + accusative", "о + prepositional", "для + dative", "к + dative"], "на + accusative", "Спрос на + the thing wanted.", order=True),
        mc("‘Кру'пный’ means:", ["large-scale", "tiny", "temporary", "foreign"], "large-scale", "Кру'пный = big, major.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 305
L305 = lesson(
    "Nobody, nothing: ни- words with prepositions (ни о чём не, ни с кем не)",
    "Мы ни о чём не говори'ли и ни с кем не спо'рили.",
    requires=["никто", "ничто", "никогда", "нигде", "никуда"],
    cards=[
        card("One не, many ни-",
             "A Russian sentence normally has one не, right before the verb. Any other negative words are built with ни-, and the verb must still be negated.",
             tables=[table(
                 ["Question", "Negative answer"],
                 [["Кто там?", "Там никого' нет."],
                  ["Что ты зна'ешь?", "Я ничего' не зна'ю."],
                  ["Где он рабо'тает?", "Он нигде' не рабо'тает."],
                  ["Когда' она' чита'ет?", "Она' никогда' не чита'ет."],
                  ["Куда' вы идёте?", "Мы никуда' не идём."]])],
             examples=[
                 ex("Де'ти никогда' нигде' не рабо'тали.", "The children have never worked anywhere.", "никогда' нигде' не рабо'тали"),
             ]),
        card("When there is a preposition",
             "If кто or что needs a preposition, the preposition goes between ни and the pronoun. The preposition always wins its place: ни о чём, ни с кем.",
             tables=[table(
                 ["Question", "Negative answer"],
                 [["О чём ты пи'шешь?", "Я ни о чём не пишу'."],
                  ["С кем вы рабо'таете?", "Мы ни с кем не рабо'таем."],
                  ["У кого' он спроси'л?", "Он ни у кого' не спроси'л."],
                  ["К кому' она' идёт?", "Она' ни к кому' не идёт."],
                  ["На что он жа'луется?", "Он ни на что не жа'луется."],
                  ["О како'м фи'льме вы говори'те?", "Мы ни о како'м фи'льме не говори'м."]])],
             examples=[
                 ex("Я ни о чём не пишу'.", "I am not writing about anything.", "ни о чём"),
                 ex("Мы ни с кем не рабо'таем.", "We don't work with anyone.", "ни с кем"),
             ]),
        card("Case and writing",
             "Write ни and the preposition as separate words. The pronoun still takes the case that the preposition requires.",
             tables=[table(
                 ["Without preposition", "With preposition"],
                 [["никого'", "ни у кого', ни от кого', ни для кого'"],
                  ["никому'", "ни к кому'"],
                  ["ничего'", "ни от чего', ни для чего'"],
                  ["ничему'", "ни к чему'"],
                  ["никаки'х", "ни в каки'х"]])],
             examples=[
                 ex("Он ни от кого' не зави'сит.", "He doesn't depend on anyone.", "ни от кого'"),
             ]),
    ],
    verify=(vf("работать", "работаем", "работает") + vf("писать", "пишу") + vf("говорить", "говорили", "говорим") + vf("спорить", "спорили")
            + vf("спросить", "спросил") + vf("зависеть", "зависит") + vf("жаловаться", "жалуется")),
    exercises=[
        F("Я ___ не пишу'. (about anything)", "ни о чём", ["ничего'", "ни чём о", "о ничём"], "The preposition splits ни and что.", "I am not writing about anything.", lemma=None),
        F("Мы ___ не рабо'таем. (with anyone)", "ни с кем", ["никого'", "никем с", "с никем"], "С + instrumental: ни с кем.", "We don't work with anyone.", lemma=None),
        F("Он ___ не зави'сит. (on anyone)", "ни от кого'", ["никого' от", "от никого'", "ни кого'"], "От + genitive.", "He doesn't depend on anyone.", lemma=None),
        F("Она' ___ не идёт. (to anyone)", "ни к кому'", ["никому'", "к никому'", "ни кому' к"], "К + dative.", "She isn't going to see anyone.", lemma=None),
        F("Он ___ не жа'луется. (about anything)", "ни на что", ["ничего'", "на ничто", "ни что на"], "На + accusative: ни на что.", "He doesn't complain about anything.", lemma=None),
        F("Мы ___ фи'льме не говори'м. (about any)", "ни о како'м", ["никако'м о", "о никако'м", "ни какой о"], "О + prepositional: ни о како'м.", "We aren't talking about any movie.", lemma=None),
        F("Она' ___ не чита'ет. (never)", "никогда'", ["нигде'", "никуда'", "ничего'"], "Never = никогда'.", "She never reads.", lemma=None),
        mc("Which sentence is correct?", ["Я ни о ком не ду'маю.", "Я ни о ком ду'маю.", "Я о никому не ду'маю.", "Я не ни о ком ду'маю."], "Я ни о ком не ду'маю.", "Ни + preposition + pronoun, and не before the verb.", order=True),
        mc("How many words does ‘with nobody’ take here?", ["three: ни с кем", "one: никем", "two: с никем", "four: ни с ни кем"], "three: ни с кем", "Ни, the preposition, the pronoun.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 306
L306 = lesson(
    "Not a single one: ни оди'н, ни ра'зу, ни сло'ва, ни за что",
    "Он ни ра'зу не опозда'л и ни сло'ва не сказа'л.",
    requires=["один", "раз", "слово", "минута", "никогда", "ничто"],
    cards=[
        card("Emphatic ни: not even one",
             "Ни before a noun gives the idea ‘not even one’. The verb is still negative.",
             tables=[table(
                 ["Phrase", "English"],
                 [["ни оди'н (ни одного', ни одно'й)", "not a single (one)"],
                  ["ни ра'зу", "not once"],
                  ["ни сло'ва", "not a word"],
                  ["ни мину'ты", "not a minute"],
                  ["ни мину'ты не", "not for a moment"]])],
             examples=[
                 ex("Он ни ра'зу не опозда'л.", "He was not late even once.", "ни ра'зу"),
                 ex("Она' ни сло'ва не сказа'ла.", "She did not say a word.", "ни сло'ва"),
                 ex("У меня' нет ни одно'й свобо'дной мину'ты.", "I don't have a single free minute.", "ни одно'й"),
             ]),
        card("Ни … ни … and fixed phrases",
             "The pair ни … ни … means ‘neither … nor …’. Some fixed phrases with ни are worth learning whole.",
             tables=[table(
                 ["Phrase", "English"],
                 [["ни … ни …", "neither … nor …"],
                  ["Ни за что!", "No way! Not for anything!"],
                  ["ни в ко'ем слу'чае", "under no circumstances"],
                  ["ни на что не похо'жий", "unlike anything else"]])],
             examples=[
                 ex("Ни Бо'ря, ни Ле'на не пришли'.", "Neither Borya nor Lena came.", "Ни Бо'ря, ни Ле'на"),
                 ex("Ни за что не пойду' туда'!", "No way I'm going there!", "Ни за что"),
             ]),
        card("Genitive after ни одного",
             "After ни оди'н the noun is in the singular and agrees in gender. In the genitive after нет, use ни одного' / ни одно'й.",
             tables=[table(
                 ["Gender", "Phrase"],
                 [["m.", "ни оди'н студе'нт не пришёл"],
                  ["f.", "ни одна' студе'нтка не пришла'"],
                  ["n.", "ни одно' письмо' не пришло'"],
                  ["after нет", "нет ни одного' студе'нта"]])],
             examples=[
                 ex("Ни одна' студе'нтка не пришла'.", "Not a single female student came.", "Ни одна'"),
             ]),
    ],
    verify=(vf("опоздать", "опоздал") + vf("сказать", "сказала") + vf("прийти", "пришёл", "пришли") + vf("пойти", "пойду")
            + vf("студент", "студента") + vf("письмо", "письмо") + vf("минута", "минуты")),
    exercises=[
        F("Он ___ ра'зу не опозда'л. (not once)", "ни", ["не", "ни одного'", "нет"], "Ни ра'зу не + verb.", "He was not late even once."),
        F("Она' ни ___ не сказа'ла. (a word)", "сло'ва", ["сло'во", "слове'", "слов"], "Ни + genitive: ни сло'ва.", "She didn't say a word.", lemma="слово"),
        F("У меня' нет ни одно'й ___ мину'ты. (free)", "свобо'дной", ["свобо'дная", "свобо'дную", "свобо'дные"], "Genitive feminine, agrees with мину'ты.", "I don't have a single free minute.", lemma="свободный"),
        F("Ни ___ студе'нт не пришёл. (a single)", "оди'н", ["одного'", "одна'", "одно'"], "Masculine nominative: студе'нт.", "Not a single student came.", lemma="один"),
        F("Ни ___ студе'нтка не пришла'. (a single)", "одна'", ["оди'н", "одно'", "одно'й"], "Feminine nominative.", "Not a single female student came.", lemma="один"),
        F("В кла'ссе нет ни ___ ученика'. (one)", "одного'", ["оди'н", "одному'", "одним"], "After нет: genitive.", "There is not a single pupil in the class.", lemma="один"),
        mc("Which means ‘No way!’?", ["Ни за что!", "Не за что!", "Ни о чём!", "Ничего'!"], "Ни за что!", "Не за что = you're welcome.", order=True),
        mc("‘Ни Бо'ря, ни Ле'на не пришли'’ means:", ["Neither Borya nor Lena came.", "Both Borya and Lena came.", "Borya came but Lena didn't.", "Nobody came."], "Neither Borya nor Lena came.", "Ни … ни … = neither … nor …", order=True),
        mc("In ‘Он ни ра'зу не опозда'л’ the не is needed because:", ["the verb must be negative", "ни ра'зу is positive", "it is a question", "опозда'л is future"], "the verb must be negative", "Ни words need не before the verb.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 307
L307 = lesson(
    "Nowhere to go: Мне не'где рабо'тать, нам не'куда идти'",
    "Ему' не'когда, а нам не'куда идти'.",
    requires=["нигде", "никуда", "некуда", "некогда", "нечего", "работать", "идти"],
    cards=[
        card("A negative idea with a positive verb",
             "Compare: ‘I don't work anywhere’ (Я нигде' не рабо'таю) and ‘there is nowhere for me to work’ (Мне не'где рабо'тать). In the second sentence the verb is positive, so the word is built with не instead of ни.",
             tables=[table(
                 ["Meaning", "Word"],
                 [["nowhere to (be)", "не'где"],
                  ["nowhere to (go)", "не'куда"],
                  ["nowhere to (come from)", "не'откуда"],
                  ["no time to", "не'когда"],
                  ["nothing to", "не'чего"],
                  ["no one to", "не'кому"]])],
             examples=[
                 ex("Мне не'где рабо'тать.", "I have nowhere to work.", "не'где"),
                 ex("Нам не'куда идти'.", "We have nowhere to go.", "не'куда"),
                 ex("Ей не'когда.", "She has no time.", "не'когда"),
             ]),
        card("The pattern",
             "The person is in the dative. The не'- word comes next, then an infinitive. There is no nominative subject. The не is always stressed.",
             tables=[table(
                 ["Dative", "не'- word", "Infinitive"],
                 [["мне", "не'где", "рабо'тать"],
                  ["нам", "не'куда", "идти'"],
                  ["ему'", "не'чего", "де'лать"],
                  ["ей", "не'когда", "чита'ть"]])],
             examples=[
                 ex("Ему' не'чего де'лать.", "He has nothing to do.", "не'чего"),
             ]),
        card("Past and future",
             "Because there is no subject, the past tense is always бы'ло and the future is always бу'дет.",
             tables=[table(
                 ["Present", "Past", "Future"],
                 [["Нам не'куда идти'.", "Нам не'куда бы'ло идти'.", "Нам не'куда бу'дет идти'."],
                  ["Ему' не'чего де'лать.", "Ему' не'чего бы'ло де'лать.", "Ему' не'чего бу'дет де'лать."]])],
             examples=[
                 ex("Вчера' нам не'куда бы'ло идти'.", "Yesterday we had nowhere to go.", "бы'ло"),
             ]),
    ],
    verify=(vf("работать", "работать") + vf("идти", "идти") + vf("делать", "делать") + vf("читать", "читать")),
    exercises=[
        F("Мне ___ рабо'тать в э'том го'роде. (nowhere to)", "не'где", ["нигде'", "где", "никуда'"], "Positive verb: не'-.", "I have nowhere to work in this town.", lemma=None),
        F("Нам ___ идти'. (nowhere to go)", "не'куда", ["никуда'", "куда'", "где"], "Куда' → не'куда.", "We have nowhere to go.", lemma=None),
        F("Ему' ___ бы'ло де'лать. (nothing to)", "не'чего", ["ничего'", "что", "никто'"], "Что → не'чего.", "He had nothing to do.", lemma=None),
        F("За'втра у меня' экза'мен, и мне ___ гуля'ть. (no time to)", "не'когда", ["никогда'", "когда'", "всегда'"], "Когда' → не'когда.", "Tomorrow I have an exam and have no time to walk.", lemma=None),
        F("Вчера' нам не'куда ___ идти'. (past)", "бы'ло", ["бу'дет", "был", "была'"], "No nominative subject: neuter бы'ло.", "Yesterday we had nowhere to go.", lemma="быть"),
        F("За'втра нам не'куда ___ идти'. (future)", "бу'дет", ["бы'ло", "бу'дут", "бу'ду"], "No subject: бу'дет.", "Tomorrow we will have nowhere to go.", lemma="быть"),
        mc("Which sentence means ‘there is nowhere for me to work’?", ["Мне не'где рабо'тать.", "Я нигде' рабо'таю.", "Мне нигде' рабо'тать.", "Я не'где не рабо'таю."], "Мне не'где рабо'тать.", "Dative + не'- word + infinitive.", order=True),
        mc("In ‘Нам не'куда идти'’ the word нам is in the:", ["dative", "genitive", "nominative", "instrumental"], "dative", "The person is in the dative.", order=True),
        mc("Where does the stress fall in не'куда?", ["on не", "on ку", "on да", "there is none"], "on не", "A stressed не marks the positive negative.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 308
L308 = lesson(
    "Nothing to read, no one to ask: не'чего, не'кого, не'кому, не' с кем",
    "Мне не' с кем бы'ло говори'ть, и не'кому бы'ло помо'чь.",
    requires=["нечего", "никто", "ничто"],
    cards=[
        card("The forms of не'чего and не'кого",
             "These words decline like что and кто, but with a stressed не in front. The case shows what the infinitive needs.",
             tables=[table(
                 ["Case", "‘nothing’", "‘no one’"],
                 [["genitive / accusative", "не'чего", "не'кого"],
                  ["dative", "не'чему", "не'кому"],
                  ["instrumental", "не'чем", "не'кем"]])],
             examples=[
                 ex("Мне не'чего чита'ть.", "I have nothing to read.", "не'чего"),
                 ex("Ему' не'кого спроси'ть.", "He has no one to ask.", "не'кого"),
                 ex("Нам не'чем писа'ть.", "We have nothing to write with.", "не'чем"),
             ]),
        card("With prepositions",
             "A preposition splits the word into two, exactly as with ни-, and the stress stays on не.",
             tables=[table(
                 ["Phrase", "English"],
                 [["не' с кем", "no one to (do it) with"],
                  ["не' о чем", "nothing to (talk) about"],
                  ["не' у кого'", "no one to (ask)"],
                  ["не' от кого'", "no one to (hide) from"],
                  ["не' за что", "nothing to be thanked for"],
                  ["не' на что", "nothing to spend on"]])],
             examples=[
                 ex("Мне не' с кем бы'ло говори'ть.", "I had no one to talk to.", "не' с кем"),
                 ex("Нам не' о чем расска'зывать.", "We have nothing to tell about.", "не' о чем"),
                 ex("— Спаси'бо за кни'гу! — Не' за что.", "“Thanks for the book!” “You're welcome.”", "Не' за что"),
             ]),
        card("не'кому: no one who can",
             "Не'кому with an infinitive means that there is nobody around to do something. The missing person is the one who would do it.",
             tables=[table(
                 ["Sentence", "English"],
                 [["Не'кому рабо'тать.", "There is no one to work."],
                  ["Не'кому бы'ло помо'чь.", "There was no one to help."],
                  ["Не'кому бу'дет отве'тить.", "There will be no one to answer."]])],
             examples=[
                 ex("Днём не'кому игра'ть с соба'кой.", "In the daytime there is no one to play with the dog.", "не'кому"),
             ]),
    ],
    verify=(vf("читать", "читать") + vf("спросить", "спросить") + vf("писать", "писать") + vf("говорить", "говорить")
            + vf("рассказывать", "рассказывать") + vf("помочь", "помочь") + vf("ответить", "ответить") + vf("играть", "играть")
            + vf("собака", "собакой")),
    exercises=[
        F("Мне ___ чита'ть. (nothing to)", "не'чего", ["ничего'", "не'кого", "не'кому"], "Что → не'чего.", "I have nothing to read.", lemma=None),
        F("Ему' ___ спроси'ть. (no one to)", "не'кого", ["никого'", "не'чего", "не'кому"], "Accusative animate → не'кого.", "He has no one to ask.", lemma=None),
        F("Нам ___ писа'ть. (nothing to write with)", "не'чем", ["не'чего", "ниче'м", "не'чему"], "Писа'ть чем → instrumental не'чем.", "We have nothing to write with.", lemma=None),
        F("Мне ___ бы'ло говори'ть. (no one to talk to)", "не' с кем", ["ни с кем", "не'кем", "не'кому"], "С + instrumental: не' с кем.", "I had no one to talk to.", lemma=None),
        F("Нам ___ расска'зывать. (nothing to tell about)", "не' о чем", ["ни о чём", "не'чего", "не'чем"], "О + prepositional: не' о чем.", "We have nothing to tell about.", lemma=None),
        F("Днём ___ игра'ть с соба'кой. (no one to)", "не'кому", ["не'кого", "никому'", "не'кем"], "The missing player is the subject: dative не'кому.", "In the daytime there is no one to play with the dog.", lemma=None),
        F("— Спаси'бо за пода'рок! — ___. (You're welcome)", "Не' за что", ["Ни за что", "Не'чего", "Не'кому"], "Fixed reply.", "“Thanks for the gift!” “You're welcome.”", lemma=None),
        mc("Which means ‘nothing to be surprised at’?", ["не'чему удивля'ться", "ничего' не удивля'ться", "не'кому удивля'ться", "не'чем удивля'ться"], "не'чему удивля'ться", "Удивля'ться чему' — dative.", order=True),
        mc("In ‘Мне не' с кем бы'ло говори'ть’ which part carries the stress?", ["не", "с", "кем", "бы'ло"], "не", "Stress stays on не.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 309
L309 = lesson(
    "Ни- or не'-? Мы никуда' не идём, потому' что нам не'куда идти'",
    "Он нигде' не рабо'тает: ему' не'где рабо'тать.",
    requires=["нигде", "никуда", "никогда", "нечего", "некуда", "некогда"],
    cards=[
        card("Two patterns, one idea",
             "The ни- pattern describes what happens: negative verb, ни- word. The не'- pattern explains why: positive infinitive, не'- word.",
             tables=[table(
                 ["Question word", "ни- + не + verb", "не'- + infinitive"],
                 [["где", "нигде' не", "не'где"],
                  ["куда'", "никуда' не", "не'куда"],
                  ["когда'", "никогда' не", "не'когда"],
                  ["что", "ничего' не", "не'чего"],
                  ["кто", "никого' не", "не'кого"],
                  ["о чём", "ни о чём не", "не' о чем"],
                  ["с кем", "ни с кем не", "не' с кем"]])],
             examples=[
                 ex("Мы никуда' не идём: нам не'куда идти'.", "We aren't going anywhere: we have nowhere to go.", "никуда' не идём"),
             ]),
        card("Choosing",
             "If you can say ‘there is nowhere / nothing / no one to …’, use не'-. If you can say ‘does not … anywhere / anything / anyone’, use ни- with не.",
             tables=[table(
                 ["English", "Russian"],
                 [["He reads nothing.", "Он ничего' не чита'ет."],
                  ["He has nothing to read.", "Ему' не'чего чита'ть."],
                  ["I know nobody here.", "Я здесь никого' не зна'ю."],
                  ["I have no one to ask here.", "Мне здесь не'кого спроси'ть."]])],
             examples=[
                 ex("Он ничего' не чита'ет, потому' что ему' не'чего чита'ть.", "He reads nothing because he has nothing to read.", "ничего' не чита'ет"),
             ]),
        card("Mini-dialogue",
             "Ask with a question word, answer with ни-, explain with не'-.",
             tables=[table(
                 ["Line", "English"],
                 [["— Куда' ты идёшь?", "Where are you going?"],
                  ["— Я никуда' не иду'.", "I'm not going anywhere."],
                  ["— Почему'?", "Why?"],
                  ["— Мне не'куда идти'.", "I have nowhere to go."]])],
             examples=[
                 ex("— Что ты чита'ешь? — Я ничего' не чита'ю: мне не'когда.", "“What are you reading?” “Nothing: I have no time.”", "ничего' не чита'ю"),
             ]),
    ],
    verify=(vf("читать", "читаешь", "читаю") + vf("знать", "знаю") + vf("спросить", "спросить") + vf("идти", "идёшь", "иду", "идём")
            + vf("работать", "работает")),
    exercises=[
        F("Мы ___ не идём. (anywhere)", "никуда'", ["не'куда", "нигде'", "куда'"], "Verb is negative: ни-.", "We aren't going anywhere.", lemma=None),
        F("Нам ___ идти'. (nowhere to)", "не'куда", ["никуда'", "куда'", "нигде'"], "Verb is positive: не'-.", "We have nowhere to go.", lemma=None),
        F("Он ___ не чита'ет. (anything)", "ничего'", ["не'чего", "что", "ничто'"], "Negative verb: ни-.", "He doesn't read anything.", lemma=None),
        F("Ему' ___ чита'ть. (nothing to)", "не'чего", ["ничего'", "что", "никто'"], "Positive infinitive: не'-.", "He has nothing to read.", lemma=None),
        F("Я здесь ___ не зна'ю. (anyone)", "никого'", ["не'кого", "кого'", "никому'"], "Знать + accusative; negative verb.", "I don't know anyone here.", lemma=None),
        F("Мне здесь ___ спроси'ть. (no one to)", "не'кого", ["никого'", "кого'", "не'кому"], "Positive infinitive: не'-.", "I have no one to ask here.", lemma=None),
        F("Она' ___ не смо'трит телеви'зор, потому' что ей не'когда. (never)", "никогда'", ["не'когда", "всегда'", "когда'"], "Negative verb.", "She never watches TV because she has no time.", lemma=None),
        mc("‘He works nowhere, because there's nowhere to work.’", ["Он нигде' не рабо'тает, потому' что ему' не'где рабо'тать.", "Он не'где не рабо'тает, потому' что ему' нигде' рабо'тать.", "Он нигде' рабо'тает, потому' что ему' не'где рабо'тать.", "Он не рабо'тает нигде', потому' что не'где ему' не рабо'тать."], "Он нигде' не рабо'тает, потому' что ему' не'где рабо'тать.", "ни- with a negated verb, then не'- with an infinitive.", order=True),
        mc("Which is the ‘positive negative’?", ["Мне не'чего де'лать.", "Я ничего' не де'лаю.", "Он никого' не ви'дит.", "Они' нигде' не бы'ли."], "Мне не'чего де'лать.", "Dative + не'- + infinitive.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 310
L310 = lesson(
    "Review: education, applying and negation",
    "Он поступи'л на бюдже'т и ни о чём не жале'ет.",
    requires=["образование", "поступить", "экзамен", "никто", "нечего", "навык", "спрос"],
    cards=[
        card("What to remember",
             "Study vocabulary: поступа'ть / поступи'ть, подава'ть докуме'нты, сдава'ть экза'мен, зна'ния, на'вык, спрос на. Negation: ни- with не and a preposition between; не'- with a dative and an infinitive.",
             tables=[table(
                 ["Pattern", "Example"],
                 [["ни + prep. + pronoun + не + verb", "Я ни о чём не пишу'."],
                  ["dative + не'- + infinitive", "Мне не'где рабо'тать."],
                  ["past / future", "бы'ло / бу'дет"],
                  ["ни оди'н", "Ни оди'н студе'нт не пришёл."]])],
             examples=[
                 ex("Ей не' с кем бы'ло говори'ть.", "She had no one to talk to.", "не' с кем"),
             ]),
    ],
    verify=(vf("поступить", "поступил") + vf("жалеть", "жалеет") + vf("экзамен", "экзамен") + vf("документ", "документы")),
    exercises=[
        F("Он поступи'л ___ бюдже'т. (onto)", "на", ["в", "к", "за"], "Поступи'ть на бюдже'т.", "He got a tuition-free place."),
        F("Она' ___ докуме'нты в университе'т. (submitted)", "подала'", ["подава'ла", "подаю'т", "пода'ть"], "One completed action.", "She submitted her documents to the university.", lemma="подать"),
        F("На ры'нке труда' большо'й ___ на программи'стов. (demand)", "спрос", ["спро'са", "спро'су", "спро'сом"], "Спрос на + accusative.", "There is great demand for programmers.", lemma="спрос"),
        F("Он ___ не жале'ет. (about anything)", "ни о чём", ["ничего'", "ни чём о", "о ничём"], "Preposition splits ни and что.", "He doesn't regret anything.", lemma=None),
        F("Мы ___ не рабо'таем. (with anyone)", "ни с кем", ["никого'", "никем с", "с никем"], "С + instrumental.", "We don't work with anyone.", lemma=None),
        F("Нам ___ идти'. (nowhere to)", "не'куда", ["никуда'", "куда'", "нигде'"], "Positive negative.", "We have nowhere to go.", lemma=None),
        F("Вчера' ему' не'чего ___ де'лать. (past)", "бы'ло", ["бу'дет", "был", "была'"], "Neuter past: бы'ло.", "Yesterday he had nothing to do.", lemma="быть"),
        F("Она' доби'лась ___. (success)", "успе'ха", ["успе'х", "успе'ху", "успе'хом"], "Genitive after добива'ться.", "She achieved success.", lemma="успех"),
        mc("‘Не' за что’ is said:", ["after someone thanks you", "when you refuse", "when you apply", "when you leave"], "after someone thanks you", "It means ‘you're welcome’.", order=True),
        mc("Which pair is correct?", ["Я ничего' не де'лаю: мне не'чего де'лать.", "Я не'чего не де'лаю: мне ничего' де'лать.", "Я ничего' де'лаю: мне не'чего не де'лать.", "Я не'чего де'лаю: мне ничего' не де'лать."], "Я ничего' не де'лаю: мне не'чего де'лать.", "Ни- with не, then не'- with infinitive.", order=True),
    ],
)

UNIT = unit("Unit 30: Education and negation",
            [L300, L301, L302, L303, L304, L305, L306, L307, L308, L309, L310])

"""Unit 32: work and employment vocabulary (textbook module 7, lesson 40)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 320
L320 = lesson(
    "Jobs and employers: работода'тель, рабо'тник, руководи'тель, предприя'тие",
    "Рабо'тник пришёл к руководи'телю предприя'тия.",
    requires=["работник", "сотрудник", "руководитель", "предприятие", "компания", "начальник", "должность", "штат", "владелец", "фирма"],
    cards=[
        card("People at work",
             "Russian has several words for the people in a workplace. Рабо'тник and сотру'дник can both mean ‘employee’; the second also means ‘colleague’.",
             tables=[table(
                 ["Word", "English"],
                 [["работода'тель (m.)", "employer"],
                  ["рабо'тник", "worker, employee"],
                  ["сотру'дник", "employee, staff member"],
                  ["руководи'тель (m.)", "director, manager"],
                  ["нача'льник", "boss, head"],
                  ["владе'лец, владе'лица", "owner (m., f.)"],
                  ["соиска'тель (m.)", "job applicant"]])],
             examples=[
                 ex("Работода'тель и'щет но'вого сотру'дника.", "The employer is looking for a new employee.", "Работода'тель"),
                 ex("Владе'лица фи'рмы — молода'я же'нщина.", "The owner of the firm is a young woman.", "Владе'лица"),
             ]),
        card("Places of work",
             "Use на with предприя'тие (an enterprise, factory) and в with компа'ния and фи'рма.",
             tables=[table(
                 ["Phrase", "English"],
                 [["на предприя'тии", "at an enterprise"],
                  ["в компа'нии", "in a company"],
                  ["в фи'рме", "in a firm"],
                  ["на произво'дстве", "in production, at a plant"]])],
             examples=[
                 ex("Она' рабо'тает на предприя'тии.", "She works at an enterprise.", "на предприя'тии"),
                 ex("Он рабо'тает в небольшо'й фи'рме.", "He works in a small firm.", "в небольшо'й фи'рме"),
             ]),
        card("Positions",
             "До'лжность (f.) is a position or job title. Штат, in the sense of workforce, is a collective noun.",
             tables=[table(
                 ["Phrase", "English"],
                 [["занима'ть до'лжность", "to hold a position"],
                  ["до'лжность руководи'теля", "the position of manager"],
                  ["штат компа'нии", "the company's staff"],
                  ["но'вая до'лжность", "a new position"]])],
             examples=[
                 ex("Он занима'ет до'лжность руководи'теля.", "He holds the position of manager.", "до'лжность"),
             ]),
    ],
    verify=(vf("работодатель", "работодатель") + vf("работник", "работник") + vf("сотрудник", "сотрудника") + vf("руководитель", "руководителю")
            + vf("предприятие", "предприятии") + vf("начальник", "начальник") + vf("владелец", "владелец")
            + vf("соискатель", "соискатель") + vf("фирма", "фирмы") + vf("компания", "компании") + vf("должность", "должность")
            + vf("производство", "производстве") + vf("занимать", "занимает") + vf("искать", "ищет")),
    exercises=[
        F("Работода'тель и'щет но'вого ___. (employee)", "сотру'дника", ["сотру'дник", "сотру'днику", "сотру'дником"], "Animate accusative = genitive.", "The employer is looking for a new employee.", lemma="сотрудник"),
        F("Она' рабо'тает на ___. (enterprise)", "предприя'тии", ["предприя'тие", "предприя'тия", "предприя'тию"], "На + prepositional.", "She works at an enterprise.", lemma="предприятие"),
        F("Он рабо'тает в небольшо'й ___. (firm)", "фи'рме", ["фи'рма", "фи'рму", "фи'рмы"], "В + prepositional.", "He works in a small firm.", lemma="фирма"),
        F("Он занима'ет ___ руководи'теля. (position)", "до'лжность", ["до'лжности", "до'лжностью", "до'лжностей"], "Accusative feminine -ь.", "He holds the position of manager.", lemma="должность"),
        F("Он пришёл к ___ предприя'тия. (manager)", "руководи'телю", ["руководи'тель", "руководи'теля", "руководи'телем"], "К + dative.", "He came to the manager of the enterprise.", lemma="руководитель"),
        F("Э'та фи'рма — со'бственность ___. (owner)", "владе'льца", ["владе'лец", "владе'льцу", "владе'льцем"], "Genitive: whose?", "This firm belongs to the owner.", lemma="владелец"),
        mc("Who is a соиска'тель?", ["a job applicant", "a customer", "a director", "an employer"], "a job applicant", "Соиска'тель applies for a position.", order=True),
        mc("Which word means ‘employer’?", ["работода'тель", "рабо'тник", "сотру'дник", "соиска'тель"], "работода'тель", "Рабо'ту + дать.", order=True),
        mc("‘На предприя'тии’ means:", ["at an enterprise", "to an enterprise", "from an enterprise", "about an enterprise"], "at an enterprise", "На + prepositional = where?", order=True),
    ],
)

# ---------------------------------------------------------------------------- 321
L321 = lesson(
    "Finding work: вака'нсия, резюме', собесе'дование, стаж, устро'иться на рабо'ту",
    "Она' пошла' на собесе'дование и устро'илась на рабо'ту.",
    requires=["должность", "опыт", "ярмарка", "занятость", "контракт", "условие"],
    cards=[
        card("Vacancies and interviews",
             "These words appear in every job advertisement.",
             tables=[table(
                 ["Word", "English"],
                 [["вака'нсия", "vacancy, opening"],
                  ["резюме'", "résumé"],
                  ["собесе'дование", "job interview"],
                  ["стаж", "length of work experience"],
                  ["о'пыт рабо'ты", "work experience"],
                  ["я'рмарка вака'нсий", "job fair"],
                  ["центр за'нятости", "employment office"]])],
             examples=[
                 ex("У нас откры'та вака'нсия.", "We have an opening.", "вака'нсия"),
                 ex("На собесе'довании её спроси'ли об о'пыте.", "At the interview they asked her about her experience.", "На собесе'довании"),
             ]),
        card("Who hires, who gets hired",
             "The employer нанима'ет / нанял. The candidate устра'ивается / устро'ился на рабо'ту. Use на + accusative with рабо'ту, and в + accusative with a company.",
             tables=[table(
                 ["Who", "Sentence"],
                 [["employer", "Компа'ния наняла' но'вого сотру'дника."],
                  ["candidate", "Анна устро'илась на рабо'ту в компа'нию."],
                  ["employer, impf.", "Мы нанима'ем лишь о'пытных рабо'тников."]])],
             examples=[
                 ex("Анна устро'илась на рабо'ту в компа'нию.", "Anna got a job at the company.", "устро'илась на рабо'ту"),
                 ex("Компа'ния наняла' но'вого сотру'дника.", "The company hired a new employee.", "наняла'"),
             ]),
        card("Contract and conditions",
             "Once hired, the employee signs a контра'кт and discusses усло'вия (conditions).",
             tables=[table(
                 ["Phrase", "English"],
                 [["контра'кт на год", "a one-year contract"],
                  ["усло'вия рабо'ты", "working conditions"],
                  ["рабо'чий гра'фик", "work schedule"],
                  ["по контра'кту", "under the contract"]])],
             examples=[
                 ex("Усло'вия рабо'ты хоро'шие.", "The working conditions are good.", "Усло'вия"),
             ]),
    ],
    verify=(vf("вакансия", "вакансия") + vf("резюме", "резюме") + vf("собеседование", "собеседовании") + vf("устроиться", "устроилась")
            + vf("нанимать", "нанимаем") + vf("нанять", "наняла") + vf("опыт", "опыте") + vf("контракт", "контракт") + vf("условие", "условия")
            + vf("график", "график") + vf("занятость", "занятости") + vf("ярмарка", "ярмарка") + vf("сотрудник", "сотрудника")),
    exercises=[
        F("У нас откры'та ___. (vacancy)", "вака'нсия", ["вака'нсии", "вака'нсию", "вака'нсией"], "Nominative singular.", "We have an opening.", lemma="вакансия"),
        F("На ___ её спроси'ли об о'пыте. (interview)", "собесе'довании", ["собесе'дование", "собесе'дования", "собесе'дованию"], "На + prepositional.", "At the interview they asked her about her experience.", lemma="собеседование"),
        F("Анна ___ на рабо'ту в компа'нию. (got a job)", "устро'илась", ["устро'ила", "устро'ился", "устро'иться"], "Feminine past of устро'иться.", "Anna got a job at the company.", lemma="устроиться"),
        F("Компа'ния ___ но'вого сотру'дника. (hired)", "наняла'", ["наняло'", "нанялась'", "нанять"], "Feminine past of нанять.", "The company hired a new employee.", lemma="нанять"),
        F("Усло'вия рабо'ты ___. (are good)", "хоро'шие", ["хоро'ший", "хоро'шая", "хоро'шее"], "Plural: усло'вия.", "The working conditions are good.", lemma="хороший"),
        F("Я подписа'л ___ на год. (contract)", "контра'кт", ["контра'кта", "контра'кту", "контра'кте"], "Accusative = nominative.", "I signed a one-year contract.", lemma="контракт"),
        mc("Who ‘нанима'ет’ — the employer or the candidate?", ["the employer", "the candidate", "both", "neither"], "the employer", "Нанима'ть = to hire.", order=True),
        mc("Which means ‘to get a job’?", ["устро'иться на рабо'ту", "нанять рабо'ту", "найти' собесе'дование", "пода'ть вака'нсию"], "устро'иться на рабо'ту", "Candidate's verb.", order=True),
        mc("What is ярмарка вакансий?", ["a job fair", "a market of goods", "a school fair", "a holiday"], "a job fair", "Я'рмарка = fair.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 322
L322 = lesson(
    "Pay and expenses: зарпла'та, дохо'д, расхо'ды, нало'г, посо'бие",
    "Дохо'ды ра'стут, но и расхо'ды то'же.",
    requires=["зарплата", "доход", "налог", "пособие", "заработать", "зарабатывать", "платить", "стоимость", "пенсия"],
    cards=[
        card("Money coming in",
             "Several words describe money received. Дохо'д is the broadest.",
             tables=[table(
                 ["Word", "English"],
                 [["зарпла'та", "salary, wages"],
                  ["дохо'д", "income"],
                  ["посо'бие", "state benefit"],
                  ["пе'нсия", "pension"],
                  ["нало'г", "tax"],
                  ["расхо'ды (pl.)", "expenses"]])],
             examples=[
                 ex("У неё хоро'шая зарпла'та.", "She has a good salary.", "зарпла'та"),
                 ex("Дохо'ды семьи' вы'росли.", "The family's income rose.", "Дохо'ды"),
             ]),
        card("To earn and to save",
             "Зараба'тывать / зарабо'тать is to earn by working. Эконо'мить / сэконо'мить is to save, with на and the prepositional case.",
             tables=[table(
                 ["Verb", "Example"],
                 [["зараба'тывать / зарабо'тать", "Он хорошо' зараба'тывает."],
                  ["эконо'мить / сэконо'мить на + prep.", "Мы эконо'мим на тра'нспорте."],
                  ["плати'ть нало'г", "Она' пла'тит нало'г."],
                  ["расхо'ды на + acc.", "расхо'ды на еду'"]])],
             examples=[
                 ex("Он хорошо' зараба'тывает.", "He earns well.", "зараба'тывает"),
                 ex("Мы эконо'мим на тра'нспорте.", "We save on transport.", "эконо'мим"),
             ]),
        card("Salary talk",
             "Questions about pay are common in job interviews and surveys.",
             tables=[table(
                 ["Question", "English"],
                 [["Ско'лько вы зараба'тываете?", "How much do you earn?"],
                  ["Каки'е расхо'ды у семьи'?", "What expenses does the family have?"],
                  ["Каки'е нало'ги вы пла'тите?", "What taxes do you pay?"]])],
             examples=[
                 ex("Каки'е нало'ги вы пла'тите?", "What taxes do you pay?", "нало'ги"),
             ]),
    ],
    verify=(vf("зарплата", "зарплата") + vf("доход", "доходы") + vf("пособие", "пособие") + vf("пенсия", "пенсия") + vf("налог", "налоги")
            + vf("расход", "расходы") + vf("зарабатывать", "зарабатывает", "зарабатываете") + vf("заработать", "заработать")
            + vf("экономить", "экономим") + vf("платить", "платит", "платите") + vf("транспорт", "транспорте") + vf("еда", "еду")),
    exercises=[
        F("У неё хоро'шая ___. (salary)", "зарпла'та", ["зарпла'ту", "зарпла'ты", "зарпла'те"], "Nominative singular.", "She has a good salary.", lemma="зарплата"),
        F("Дохо'ды семьи' ___. (rose)", "вы'росли", ["вы'рос", "вы'росла", "вы'росло"], "Plural subject.", "The family's income rose.", lemma="вырасти"),
        F("Он хорошо' ___. (earns)", "зараба'тывает", ["зараба'тывают", "зарабо'тал", "зарабо'тать"], "Present, singular.", "He earns well.", lemma="зарабатывать"),
        F("Мы эконо'мим ___ тра'нспорте. (on)", "на", ["в", "за", "по"], "Эконо'мить на + prepositional.", "We save on transport."),
        F("Каки'е ___ вы пла'тите? (taxes)", "нало'ги", ["нало'га", "нало'гу", "нало'гом"], "Plural accusative = nominative.", "What taxes do you pay?", lemma="налог"),
        F("Расхо'ды ___ еду' вы'росли. (on)", "на", ["в", "из", "о"], "Расхо'ды на + accusative.", "Spending on food has risen."),
        mc("Which is the broadest word for ‘income’?", ["дохо'д", "зарпла'та", "посо'бие", "нало'г"], "дохо'д", "It covers all sources.", order=True),
        mc("What case follows сэконо'мить на?", ["prepositional", "accusative", "genitive", "dative"], "prepositional", "Сэконо'мить на чём?", order=True),
        mc("Which is paid by the state to those in need?", ["посо'бие", "зарпла'та", "нало'г", "расхо'д"], "посо'бие", "Benefit.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 323
L323 = lesson(
    "Raising and lowering: повыша'ть, снижа'ть, увели'чивать, уменьша'ть",
    "Зарпла'та повы'силась на пять проце'нтов.",
    requires=["повышать", "повысить", "снизить", "увеличить", "повышение", "снижение", "процент"],
    cards=[
        card("Four pairs of verbs",
             "Each pair has an imperfective and a perfective form. All of them take an object. Add -ся to get ‘goes up’ or ‘goes down’.",
             tables=[table(
                 ["Verb + object", "With -ся", "English"],
                 [["повыша'ть / повы'сить", "повыша'ться / повы'ситься", "to raise / to rise"],
                  ["снижа'ть / сни'зить", "снижа'ться / сни'зиться", "to lower / to fall"],
                  ["увели'чивать / увели'чить", "увели'чиваться / увели'читься", "to increase / to grow"],
                  ["уменьша'ть / уме'ньшить", "уменьша'ться / уме'ньшиться", "to decrease / to shrink"]])],
             examples=[
                 ex("Прави'тельство повы'сило пе'нсии.", "The government raised pensions.", "повы'сило"),
                 ex("Пе'нсии повы'сились.", "Pensions rose.", "повы'сились"),
             ]),
        card("The nouns",
             "The nouns are повыше'ние, сниже'ние, увеличе'ние, уменьше'ние. Повыше'ние can also mean promotion.",
             tables=[table(
                 ["Noun", "English"],
                 [["повыше'ние", "rise; promotion"],
                  ["сниже'ние", "reduction"],
                  ["увеличе'ние", "increase"],
                  ["уменьше'ние", "decrease"]])],
             examples=[
                 ex("Она' получи'ла повыше'ние.", "She got a promotion.", "повыше'ние"),
                 ex("Сниже'ние нало'гов помогло' би'знесу.", "The tax reduction helped business.", "Сниже'ние"),
             ]),
        card("By how much?",
             "Use на + accusative for the amount of change, в + genitive for ‘times’, and с … до for ‘from … to’.",
             tables=[table(
                 ["Pattern", "Example"],
                 [["на + acc.", "Це'ны повы'сились на оди'н проце'нт."],
                  ["на + acc.", "Расхо'ды сни'зились на пять проце'нтов."],
                  ["в … ра'за", "Дохо'д увели'чился в два ра'за."]])],
             examples=[
                 ex("Расхо'ды сни'зились на пять проце'нтов.", "Expenses fell by five percent.", "на пять проце'нтов"),
                 ex("Дохо'д увели'чился в два ра'за.", "Income increased twofold.", "в два ра'за"),
             ]),
    ],
    verify=(vf("повышать", "повышать") + vf("повысить", "повысило") + vf("повыситься", "повысились") + vf("снижать", "снижать") + vf("снизиться", "снизились")
            + vf("увеличивать", "увеличивать") + vf("увеличиться", "увеличился") + vf("уменьшать", "уменьшать") + vf("уменьшить", "уменьшить")
            + vf("повышение", "повышение") + vf("снижение", "снижение") + vf("увеличение", "увеличение") + vf("уменьшение", "уменьшение")
            + vf("процент", "процентов", "процент") + vf("пенсия", "пенсии") + vf("получить", "получила")),
    exercises=[
        F("Прави'тельство ___ пе'нсии. (raised)", "повы'сило", ["повы'силось", "повы'сились", "повы'сить"], "Object пе'нсии.", "The government raised pensions.", lemma="повысить"),
        F("Пе'нсии ___. (rose)", "повы'сились", ["повы'сило", "повы'сила", "повы'сить"], "Plural, no object: -ся.", "Pensions rose.", lemma="повыситься"),
        F("Расхо'ды сни'зились на пять ___. (percent)", "проце'нтов", ["проце'нта", "проце'нт", "проце'нты"], "After пять: genitive plural.", "Expenses fell by five percent.", lemma="процент"),
        F("Це'ны повы'сились на оди'н ___. (percent)", "проце'нт", ["проце'нта", "проце'нтов", "проце'нты"], "After оди'н: nominative singular.", "Prices rose by one percent.", lemma="процент"),
        F("Дохо'д увели'чился в два ___. (times)", "ра'за", ["раз", "ра'зу", "ра'зом"], "After два: genitive singular.", "Income increased twofold."),
        F("Она' получи'ла ___. (a promotion)", "повыше'ние", ["повыше'ния", "повыше'нию", "повыше'нием"], "Accusative = nominative.", "She got a promotion.", lemma="повышение"),
        F("Компа'ния ___ расхо'ды. (reduced)", "сни'зила", ["сни'зилась", "сни'зились", "сни'зить"], "Object расхо'ды.", "The company reduced its costs.", lemma="снизить"),
        mc("Which sentence says that income grew by itself?", ["Дохо'д увели'чился.", "Дохо'д увели'чил.", "Они' увели'чили дохо'д.", "Увели'чить дохо'д."], "Дохо'д увели'чился.", "No object: -ся.", order=True),
        mc("‘Повыше'ние’ can mean:", ["a promotion", "a decrease", "a tax", "a vacancy"], "a promotion", "Also rise.", order=True),
    ],
)
# ---------------------------------------------------------------------------- 324
L324 = lesson(
    "The job market: безрабо'тица, за'нятость, конкуре'нция, увольне'ние",
    "В э'той о'трасли высо'кая конкуре'нция, и мно'гих уво'лили.",
    requires=["безработица", "безработный", "занятость", "конкуренция", "отрасль", "сфера", "промышленность", "торговля", "производство", "уволить", "увольнение"],
    cards=[
        card("Employment and unemployment",
             "Reports on the economy use a small set of nouns.",
             tables=[table(
                 ["Word", "English"],
                 [["за'нятость (f.)", "employment"],
                  ["безрабо'тица", "unemployment"],
                  ["безрабо'тный", "unemployed (person)"],
                  ["конкуре'нция", "competition"],
                  ["спрос на рабо'тников", "demand for workers"],
                  ["сокраще'ние ка'дров", "staff cuts"]])],
             examples=[
                 ex("В регио'не растёт безрабо'тица.", "Unemployment is growing in the region.", "безрабо'тица"),
                 ex("Безрабо'тные получа'ют посо'бие.", "The unemployed receive benefits.", "Безрабо'тные"),
             ]),
        card("Branches of the economy",
             "A branch of the economy is an о'трасль or a сфе'ра. Use в + prepositional.",
             tables=[table(
                 ["Word", "English"],
                 [["о'трасль (f.)", "branch, sector"],
                  ["сфе'ра", "field, sphere"],
                  ["промы'шленность (f.)", "industry"],
                  ["торго'вля", "trade"],
                  ["произво'дство", "production, manufacturing"]])],
             examples=[
                 ex("Она' рабо'тает в сфе'ре торго'вли.", "She works in the retail trade.", "в сфе'ре торго'вли"),
                 ex("В э'той о'трасли ма'ло рабо'ты.", "There is little work in this sector.", "В э'той о'трасли"),
             ]),
        card("Hiring and firing",
             "Two aspect pairs describe the employer's decisions.",
             tables=[table(
                 ["Imperfective", "Perfective", "English"],
                 [["нанима'ть", "наня'ть", "to hire"],
                  ["увольня'ть", "уво'лить", "to fire"]])],
             examples=[
                 ex("Компа'ния уво'лила пятьдеся'т рабо'тников.", "The company fired fifty workers.", "уво'лила"),
                 ex("Увольне'ние бы'ло неожи'данным.", "The dismissal was unexpected.", "Увольне'ние"),
             ]),
    ],
    verify=(vf("занятость", "занятость") + vf("безработица", "безработица") + vf("безработный", "безработные") + vf("конкуренция", "конкуренция")
            + vf("отрасль", "отрасли") + vf("сфера", "сфере") + vf("промышленность", "промышленность") + vf("торговля", "торговли")
            + vf("производство", "производство") + vf("нанимать", "нанимать") + vf("нанять", "нанять") + vf("увольнять", "увольнять")
            + vf("уволить", "уволила") + vf("увольнение", "увольнение") + vf("получать", "получают")),
    exercises=[
        F("В регио'не растёт ___. (unemployment)", "безрабо'тица", ["безрабо'тицы", "безрабо'тицу", "безрабо'тице"], "Nominative singular.", "Unemployment is growing in the region.", lemma="безработица"),
        F("Она' рабо'тает в ___ торго'вли. (sphere)", "сфе'ре", ["сфе'ра", "сфе'ру", "сфе'ры"], "В + prepositional.", "She works in the retail trade.", lemma="сфера"),
        F("В э'той ___ ма'ло рабо'ты. (sector)", "о'трасли", ["о'трасль", "о'траслью", "о'траслей"], "В + prepositional of о'трасль.", "There is little work in this sector.", lemma="отрасль"),
        F("Компа'ния ___ пятьдеся'т рабо'тников. (fired)", "уво'лила", ["уво'лило", "уво'лились", "увольня'ть"], "Feminine: компа'ния.", "The company fired fifty workers.", lemma="уволить"),
        F("Между фи'рмами больша'я ___. (competition)", "конкуре'нция", ["конкуре'нции", "конкуре'нцию", "конкуре'нцией"], "Nominative singular.", "There is great competition between the firms.", lemma="конкуренция"),
        F("Безрабо'тные получа'ют ___. (benefit)", "посо'бие", ["посо'бия", "посо'бию", "посо'бием"], "Accusative = nominative.", "The unemployed receive a benefit.", lemma="пособие"),
        mc("Which pair is aspect pair for ‘to fire’?", ["увольня'ть / уво'лить", "нанима'ть / наня'ть", "повыша'ть / повы'сить", "получа'ть / получи'ть"], "увольня'ть / уво'лить", "Fire.", order=True),
        mc("‘За'нятость’ means:", ["employment", "unemployment", "competition", "salary"], "employment", "Related to за'нятый (busy).", order=True),
        mc("Which of these is a branch of the economy?", ["торго'вля", "безрабо'тица", "увольне'ние", "дохо'д"], "торго'вля", "Trade.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 325
L325 = lesson(
    "Influence, aim, certainty: влия'ть на, стреми'ться к, уве'рен в, каса'ться",
    "Он стреми'тся к успе'ху и уве'рен в себе'.",
    requires=["влиять", "влияние", "стремиться", "касаться", "уверенный", "обеспечивать", "потребность", "постоянный", "собственный", "лишь"],
    cards=[
        card("Verbs and the cases they need",
             "Many verbs of this lesson take a particular preposition or case. Learn each verb with its partner.",
             tables=[table(
                 ["Verb", "Takes", "Example"],
                 [["влия'ть / повлия'ть", "на + acc.", "Пого'да влия'ет на настрое'ние."],
                  ["стреми'ться", "к + dat. / inf.", "Он стреми'тся к успе'ху."],
                  ["каса'ться", "+ gen.", "Э'то каса'ется всех."],
                  ["обеспе'чивать / обеспе'чить", "+ acc.", "Компа'ния обеспе'чивает рабо'тников жильём."],
                  ["быть уве'ренным в", "в + prep.", "Я уве'рен в успе'хе."]])],
             examples=[
                 ex("Пого'да влия'ет на настрое'ние.", "The weather influences mood.", "влия'ет на настрое'ние"),
                 ex("Э'то каса'ется всех.", "This concerns everyone.", "каса'ется всех"),
             ]),
        card("Nouns: влия'ние and потре'бность",
             "The related nouns take the same prepositions: влия'ние на and потре'бность в.",
             tables=[table(
                 ["Noun phrase", "English"],
                 [["влия'ние на + acc.", "influence on"],
                  ["потре'бность в + prep.", "need for"],
                  ["обеспе'чение рабо'тников", "providing for employees"]])],
             examples=[
                 ex("Есть потре'бность в но'вых специали'стах.", "There is a need for new specialists.", "потре'бность в"),
             ]),
        card("Small but useful",
             "Four words that appear often in reports.",
             tables=[table(
                 ["Word", "English"],
                 [["в тече'ние + gen.", "during, over the course of"],
                  ["лишь", "only (formal)"],
                  ["постоя'нный / вре'менный", "permanent / temporary"],
                  ["со'бственный", "one's own"]])],
             examples=[
                 ex("В тече'ние ме'сяца мы жда'ли отве'та.", "For a month we waited for an answer.", "В тече'ние ме'сяца"),
                 ex("У него' со'бственная фи'рма.", "He has his own firm.", "со'бственная"),
             ]),
    ],
    verify=(vf("влиять", "влияет") + vf("повлиять", "повлиять") + vf("стремиться", "стремится") + vf("касаться", "касается")
            + vf("обеспечивать", "обеспечивает") + vf("обеспечить", "обеспечить") + vf("влияние", "влияние") + vf("потребность", "потребность")
            + vf("уверенный", "уверен") + vf("постоянный", "постоянный") + vf("временный", "временный") + vf("собственный", "собственная")
            + vf("настроение", "настроение") + vf("жильё", "жильём") + vf("специалист", "специалистах")),
    exercises=[
        F("Пого'да влия'ет ___ настрое'ние. (on)", "на", ["в", "к", "о"], "Влия'ть на + accusative.", "The weather influences mood.", lemma=None),
        F("Он стреми'тся ___ успе'ху. (toward)", "к", ["на", "в", "о"], "Стреми'ться к + dative.", "He strives for success.", lemma=None),
        F("Э'то каса'ется ___. (everyone)", "всех", ["все", "всем", "всеми"], "Каса'ться + genitive.", "This concerns everyone.", lemma=None),
        F("Я уве'рен ___ успе'хе. (in)", "в", ["на", "к", "за"], "Уве'рен в + prepositional.", "I am sure of success.", lemma=None),
        F("Есть потре'бность ___ но'вых специали'стах. (for)", "в", ["на", "к", "о"], "Потре'бность в + prepositional.", "There is a need for new specialists.", lemma=None),
        F("___ ме'сяца мы жда'ли отве'та. (during)", "В тече'ние", ["Во вре'мя", "До", "Че'рез"], "В тече'ние + genitive.", "For a month we waited for an answer.", lemma=None),
        F("У него' ___ фи'рма. (own)", "со'бственная", ["со'бственный", "со'бственное", "со'бственные"], "Feminine: фи'рма.", "He has his own firm.", lemma="собственный"),
        mc("Which preposition follows влия'ть?", ["на", "в", "к", "от"], "на", "Влия'ть на + accusative.", order=True),
        mc("‘Лишь’ is a formal synonym of:", ["то'лько", "уже'", "всегда'", "оди'н"], "то'лько", "Only.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 326
L326 = lesson(
    "Word-building: им / ём, треб, влад, раб",
    "Заём, приём, наём — один корень; владеть и обладать — другой.",
    requires=["приём", "подъём", "преимущество", "требовать", "потребность", "владеть", "обладать", "разработать"],
    cards=[
        card("ИМ / ЁМ / ЕМ / ЙМ / Я: take, have",
             "This root changes shape. You have already seen it in взять, занять and снять.",
             tables=[table(
                 ["Word", "English"],
                 [["наём", "hiring"],
                  ["заём", "loan"],
                  ["приём", "reception; admission; method"],
                  ["подъём", "rise; getting up"],
                  ["съёмка", "filming; shooting"],
                  ["преиму'щество", "advantage"]])],
             examples=[
                 ex("Приём докуме'нтов начина'ется в ию'ле.", "Document admission starts in July.", "Приём"),
                 ex("У нас есть преиму'щество.", "We have an advantage.", "преиму'щество"),
             ]),
        card("ТРЕБ and ВЛАД",
             "Треб means ‘require, need’. Влад means ‘possess, control’.",
             tables=[table(
                 ["Word", "English"],
                 [["тре'бовать", "to demand"],
                  ["потре'бность", "need"],
                  ["употребля'ть", "to use"],
                  ["злоупотребля'ть", "to abuse"],
                  ["владе'ть", "to own; to speak fluently"],
                  ["облада'ть", "to possess (a quality)"],
                  ["владе'лец", "owner"]])],
             examples=[
                 ex("Он свобо'дно владе'ет англи'йским.", "He speaks English fluently.", "владе'ет"),
                 ex("Она' облада'ет хоро'шей па'мятью.", "She has a good memory.", "облада'ет"),
             ]),
        card("РАБ: work",
             "The root work forms many verbs with prefixes.",
             tables=[table(
                 ["Word", "English"],
                 [["работода'тель", "employer"],
                  ["отрабо'тать", "to work off; to practise"],
                  ["разрабо'тать", "to develop, work out"],
                  ["перераба'тывать", "to process; to recycle"]])],
             examples=[
                 ex("Инжене'ры разрабо'тали но'вую програ'мму.", "The engineers developed a new program.", "разрабо'тали"),
             ]),
    ],
    verify=(vf("приём", "приём") + vf("подъём", "подъём") + vf("преимущество", "преимущество") + vf("требовать", "требовать")
            + vf("потребность", "потребность") + vf("употреблять", "употреблять") + vf("злоупотреблять", "злоупотреблять")
            + vf("владеть", "владеет") + vf("обладать", "обладает") + vf("работодатель", "работодатель") + vf("отработать", "отработать")
            + vf("разработать", "разработали") + vf("перерабатывать", "перерабатывать") + vf("владелец", "владелец")),
    exercises=[
        F("Он свобо'дно ___ англи'йским. (speaks)", "владе'ет", ["облада'ет", "тре'бует", "употребля'ет"], "Владе'ть + instrumental.", "He speaks English fluently.", lemma="владеть"),
        F("Она' ___ хоро'шей па'мятью. (has)", "облада'ет", ["владе'ет", "тре'бует", "употребля'ет"], "Облада'ть + instrumental of a quality.", "She has a good memory.", lemma="обладать"),
        F("Инжене'ры ___ но'вую програ'мму. (developed)", "разрабо'тали", ["отрабо'тали", "перерабо'тали", "употребля'ли"], "Раз- + раб.", "The engineers developed a new program.", lemma="разработать"),
        F("Дире'ктор ___ отчёта. (demands)", "тре'бует", ["владе'ет", "облада'ет", "разрабо'тал"], "Тре'бовать + genitive.", "The director demands a report.", lemma="требовать"),
        F("У нас есть ___. (an advantage)", "преиму'щество", ["приём", "подъём", "наём"], "Преиму'щество.", "We have an advantage.", lemma="преимущество"),
        mc("The root ТРЕБ means:", ["require, need", "possess", "take", "step"], "require, need", "Тре'бовать, потре'бность.", order=True),
        mc("The root ВЛАД means:", ["possess, control", "work", "take", "let go"], "possess, control", "Владе'ть.", order=True),
        mc("Which noun comes from the root ‘take’ and means ‘hiring’?", ["наём", "приём", "подъём", "заём"], "наём", "Нанима'ть.", order=True),
        mc("What is заём?", ["a loan", "a hiring", "a reception", "a rise"], "a loan", "Take on credit.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 327
L327 = lesson(
    "Review: work, pay and the job market",
    "Компа'ния наняла' но'вого сотру'дника и повы'сила зарпла'ту.",
    requires=["должность", "зарплата", "налог", "безработный", "влиять", "стремиться", "повысить", "сотрудник"],
    cards=[
        card("What to remember",
             "Hiring: нанима'ть / наня'ть (employer), устро'иться на рабо'ту (candidate). Money: зарпла'та, дохо'д, расхо'ды, нало'г. Change: повыша'ть / повы'сить, снижа'ть / сни'зить with -ся when there is no object. Cases: влия'ть на + acc., стреми'ться к + dat., уве'рен в + prep., каса'ться + gen.",
             tables=[table(
                 ["Pattern", "Example"],
                 [["на + acc. (influence)", "влия'ть на це'ны"],
                  ["к + dat. (strive)", "стреми'ться к успе'ху"],
                  ["в тече'ние + gen.", "в тече'ние го'да"],
                  ["на + acc. (by how much)", "вы'расти на пять проце'нтов"]])],
             examples=[
                 ex("Компа'ния наняла' но'вого сотру'дника.", "The company hired a new employee.", "наняла'"),
             ]),
    ],
    verify=(vf("нанять", "наняла") + vf("повысить", "повысила") + vf("сотрудник", "сотрудника") + vf("зарплата", "зарплату")),
    exercises=[
        F("Компа'ния ___ но'вого сотру'дника. (hired)", "наняла'", ["устро'илась", "нанялась'", "наняло'"], "Employer hires.", "The company hired a new employee.", lemma="нанять"),
        F("Анна ___ на рабо'ту в банк. (got a job)", "устро'илась", ["наняла'", "устро'ила", "устро'иться"], "Candidate's verb.", "Anna got a job at a bank.", lemma="устроиться"),
        F("Прави'тельство ___ нало'г. (lowered)", "сни'зило", ["сни'зилось", "сни'зился", "сни'зить"], "Object нало'г.", "The government lowered the tax.", lemma="снизить"),
        F("Нало'г ___. (went down)", "сни'зился", ["сни'зил", "сни'зило", "сни'зить"], "Masculine, no object.", "The tax went down.", lemma="снизиться"),
        F("Пого'да влия'ет ___ настрое'ние. (on)", "на", ["в", "к", "о"], "Влия'ть на + accusative.", "The weather influences mood."),
        F("Он стреми'тся ___ успе'ху. (toward)", "к", ["на", "в", "о"], "Стреми'ться к + dative.", "He strives for success."),
        F("В регио'не растёт ___. (unemployment)", "безрабо'тица", ["безрабо'тицы", "безрабо'тицу", "безрабо'тице"], "Nominative.", "Unemployment is growing in the region.", lemma="безработица"),
        F("Он хорошо' ___. (earns)", "зараба'тывает", ["зараба'тывают", "зарабо'тал", "зарабо'тать"], "Present, singular.", "He earns well.", lemma="зарабатывать"),
        mc("Which sentence is correct?", ["Зарпла'та повы'силась на пять проце'нтов.", "Зарпла'та повы'сила на пять проце'нтов.", "Зарпла'та повы'сились на пять проце'нтов.", "Зарпла'та повы'шать на пять проце'нтов."], "Зарпла'та повы'силась на пять проце'нтов.", "No object: -ся; feminine past.", order=True),
        mc("Which preposition follows потре'бность?", ["в", "на", "к", "от"], "в", "Потре'бность в чём.", order=True),
    ],
)

UNIT = unit("Unit 32: Work, pay and the job market",
            [L320, L321, L322, L323, L324, L325, L326, L327])

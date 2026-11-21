"""Unit 37: political trends (textbook Chapter 37): forms of government, ideologies, democracy and decolonization in Latin America, populism, disinformation; perfect tenses with ser/estar/haber and the present perfect subjunctive. All texts are original and hedged."""
from dsl_es import *

# ---------------------------------------------------------------------------- 781
L781 = lesson(
    "Forms of government: democracia, república, monarquía, dictadura",
    "En una democracia, los ciudadanos eligen a sus gobernantes.",
    requires=["democracia", "monarquía", "dictadura", "rey", "reina", "elegir", "gobernar", "votar", "ciudadano", "poder", "límite", "elección"],
    cards=[
        card("Four forms of government",
             "These are simple definitions. Real governments often mix features, and political scientists describe them in more detail.",
             tables=[table(["Forma", "English", "Ejemplo"],
                           [["la democracia", "democracy", "En una democracia, los ciudadanos eligen a sus gobernantes en elecciones libres."],
                            ["la república", "republic", "En una república, el jefe del Estado no es un rey; ocupa el cargo por un tiempo limitado."],
                            ["la monarquía", "monarchy", "En una monarquía, un rey o una reina es la cabeza del Estado."],
                            ["la dictadura", "dictatorship", "En una dictadura, una persona o un grupo pequeño tiene el poder sin límites claros."]],
                           say=[2])]),
        card("Two kinds of monarchy",
             "In an absolute monarchy, the monarch’s power has no limits set by another authority. In a constitutional monarchy, a constitution limits the monarch’s power, and elected officials usually govern. "
             "A democracy can exist in a republic or in a constitutional monarchy.",
             examples=[
                 ex("En una monarquía constitucional, la ley limita el poder del rey.", "In a constitutional monarchy, the law limits the king’s power.", "limita"),
             ]),
    ],
    exercises=[
        M("Which form of government has a king or queen as head of state?", "La monarquía", ["La república", "La democracia", "La dictadura"], "Monarquía."),
        M("In which system does a person or small group hold power without clear limits?", "La dictadura", ["La democracia", "La república", "La monarquía constitucional"], "Dictadura."),
        M("What do citizens do in a democracy?", "They choose their rulers in free elections", ["They obey one family forever", "They never vote", "They inherit power"], "Democracia."),
        F("En una democracia, los ciudadanos ___ a sus gobernantes.", "eligen", ["elige", "elegimos", "elegir"], "Plural subject.", tr="In a democracy, citizens choose their rulers.", lemma="elegir:ellos"),
        F("Cada cuatro años, los ciudadanos ___ en las elecciones.", "votan", ["vota", "votas", "votar"], "Plural subject.", tr="Every four years, citizens vote in the elections.", lemma="votar:ellos"),
        F("En una monarquía constitucional, la ley limita el poder del ___.", "rey", ["votante", "juez", "alcalde"], "Monarchy → king.", tr="In a constitutional monarchy, the law limits the king’s power."),
        F("En una ___, el jefe del Estado ocupa el cargo por un tiempo limitado.", "república", ["monarquía", "dictadura", "aristocracia"], "Republic.", tr="In a republic, the head of state holds office for a limited time."),
        F("En una dictadura, el poder no tiene ___ claros.", "límites", ["límite", "votos", "reyes"], "Plural noun.", tr="In a dictatorship, power has no clear limits."),
        F("El presidente ___ el país durante cuatro años.", "gobierna", ["gobiernan", "gobernamos", "gobernar"], "Singular subject.", tr="The president governs the country for four years.", lemma="gobernar:él"),
    ],
)

# ---------------------------------------------------------------------------- 782
L782 = lesson(
    "Aristocracia, oligarquía, tiranía, demagogia",
    "Una oligarquía es un gobierno de un grupo pequeño que defiende sus intereses.",
    requires=["gobierno", "grupo", "familia", "poder", "clase", "riqueza", "promesa", "emoción", "razón", "apoyo", "conseguir", "filósofo"],
    cards=[
        card("Four more words",
             "These four words describe forms of government or political strategies. They are often used critically.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["la aristocracia", "aristocracy", "La aristocracia es una clase privilegiada formada por la nobleza o por familias muy ricas."],
                            ["la oligarquía", "oligarchy", "En una oligarquía, un grupo pequeño concentra el poder y defiende sus propios intereses."],
                            ["la tiranía", "tyranny", "Una tiranía es un gobierno que usa el poder de forma cruel o injusta."],
                            ["la demagogia", "demagoguery", "La demagogia busca apoyo con promesas fáciles y apelando a las emociones, no a la razón."]],
                           say=[2])]),
        card("A classical idea",
             "An old idea from ancient Greek philosophers says that each good form of government can degenerate into a bad one. In one version of this scheme, monarchy can become tyranny and aristocracy can become oligarchy; some authors add that rule by the people can degenerate into rule by the mob, led by demagogues. "
             "Modern scholars use the idea as a starting point, not as a complete theory.",
             examples=[
                 ex("Según esa idea, la monarquía puede degenerar en tiranía.", "According to that idea, monarchy can degenerate into tyranny.", "degenerar"),
                 ex("La aristocracia puede degenerar en oligarquía.", "Aristocracy can degenerate into oligarchy.", "oligarquía"),
                 ex("La democracia puede degenerar en demagogia, según algunos autores.", "Democracy can degenerate into demagoguery, according to some authors.", "demagogia"),
             ]),
    ],
    exercises=[
        M("Which word describes a small group concentrating power for its own interests?", "oligarquía", ["demagogia", "aristocracia", "república"], "Oligarquía."),
        M("What does “demagogia” try to win?", "Support, through easy promises and emotions", ["Taxes, through force", "A prize, through a vote", "Land, through war"], "Demagogia."),
        M("In the classical idea, what can monarchy degenerate into?", "Tyranny", ["Oligarchy", "Demagoguery", "Democracy"], "Monarquía → tiranía."),
        F("Un gobierno que usa el poder de forma cruel o injusta es una ___.", "tiranía", ["aristocracia", "república", "elección"], "Tyranny.", tr="A government that uses power in a cruel or unjust way is a tyranny."),
        F("En una ___, un grupo pequeño concentra el poder.", "oligarquía", ["democracia", "república", "monarquía constitucional"], "Oligarchy.", tr="In an oligarchy, a small group concentrates power."),
        F("La aristocracia es una ___ privilegiada.", "clase", ["clases", "voto", "ley"], "Singular noun.", tr="The aristocracy is a privileged class."),
        F("La demagogia busca apoyo con promesas ___.", "fáciles", ["fácil", "difícil", "fuertes"], "Plural adjective; easy promises.", tr="Demagoguery seeks support with easy promises."),
        F("La demagogia apela a las emociones, no a la ___.", "razón", ["razones", "familias", "tiranías"], "Singular noun after la.", tr="Demagoguery appeals to emotions, not to reason."),
        F("Según algunos autores clásicos, la democracia puede ___ en demagogia.", "degenerar", ["degenerado", "degenera", "degeneran"], "Modal + infinitive.", tr="According to some classical authors, democracy can degenerate into demagoguery."),
    ],
)

# ---------------------------------------------------------------------------- 783
L783 = lesson(
    "Three branches of government and elections",
    "El poder legislativo hace las leyes; el poder judicial las interpreta.",
    requires=["ley", "juez", "tribunal", "congreso", "presidente", "ministro", "votar", "elegir", "voto", "elección", "equilibrio", "ejecutivo"],
    cards=[
        card("Separation of powers",
             "Many democracies divide the power of the state into three branches. The idea is to create a balance, so that no single branch has too much power.",
             tables=[table(["Poder", "Qué hace", "Quién"],
                           [["el poder legislativo", "Hace las leyes.", "el congreso"],
                            ["el poder ejecutivo", "Aplica las leyes y administra el país.", "el presidente y los ministros"],
                            ["el poder judicial", "Interpreta las leyes y juzga los casos.", "los jueces y los tribunales"]],
                           say=[0, 1, 2])]),
        card("Words about elections",
             "Los comicios are elections. El sufragio is the right to vote. El electorado is all the people who can vote. Elegir means to choose, and convocar means to call an election.",
             examples=[
                 ex("El electorado vota en los comicios.", "The electorate votes in the elections.", "electorado"),
                 ex("El presidente convocó elecciones para el mes próximo.", "The president called elections for next month.", "convocó"),
             ]),
    ],
    exercises=[
        M("Which branch makes the laws?", "The legislative branch", ["The executive branch", "The judicial branch", "The electoral branch"], "Legislativo."),
        M("Which branch includes judges and courts?", "The judicial branch", ["The executive branch", "The legislative branch", "The electoral branch"], "Judicial."),
        M("What does “el electorado” mean?", "The people who can vote", ["The candidates", "The courts", "The ballots"], "Electorado."),
        F("El poder ___ hace las leyes.", "legislativo", ["judicial", "ejecutivo", "privado"], "Legislative.", tr="The legislative branch makes the laws.", ),
        F("Los jueces y los tribunales forman parte del poder ___.", "judicial", ["legislativo", "ejecutivo", "privado"], "Judicial.", tr="Judges and courts are part of the judicial branch."),
        F("El presidente y los ministros forman el poder ___.", "ejecutivo", ["legislativo", "judicial", "privado"], "Executive.", tr="The president and the ministers form the executive branch."),
        F("Muchas democracias buscan un ___ entre los tres poderes.", "equilibrio", ["tribunal", "voto", "ministro"], "Balance.", tr="Many democracies seek a balance among the three branches."),
        F("Los ciudadanos ___ a sus representantes en las elecciones.", "eligen", ["elige", "elegimos", "elegir"], "Plural subject.", tr="Citizens choose their representatives in the elections.", lemma="elegir:ellos"),
        F("Ayer el presidente ___ elecciones para el mes próximo.", "convocó", ["convoca", "convocamos", "convocar"], "Past event.", tr="Yesterday the president called elections for next month.", lemma="convocar:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 784
L784 = lesson(
    "Political words: régimen, postura, consenso, gestión",
    "Los dos partidos tienen posturas diferentes sobre los impuestos.",
    requires=["tendencia", "postura", "consenso", "resolución", "gestión", "ministerio", "panorama", "espectro", "financiamiento", "partido", "político", "oposición"],
    cards=[
        card("Words from political reporting",
             "Notice that most of these nouns are neutral. They describe positions, processes and institutions, not good or bad behavior.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el régimen", "regime, system of government", "En las noticias, régimen suele usarse para gobiernos no democráticos, pero también tiene un sentido neutral."],
                            ["la tendencia", "trend", "La tendencia política de la región cambió en los últimos años."],
                            ["la postura", "stance", "Los dos partidos tienen posturas diferentes sobre los impuestos."],
                            ["el consenso", "consensus", "El comité aprobó la resolución por consenso."],
                            ["la resolución", "resolution, ruling", "La resolución pide una reunión urgente."],
                            ["la gestión", "management", "La gestión del ministerio mejoró este año."],
                            ["el vocero", "spokesperson", "El vocero del gobierno habló con la prensa."],
                            ["el panorama", "outlook, overview", "El panorama político es complejo."],
                            ["el espectro", "spectrum", "El espectro político va de la izquierda a la derecha."],
                            ["la convocatoria", "call, announcement", "La convocatoria a elecciones se publicó ayer."],
                            ["el financiamiento", "funding", "El financiamiento de las campañas debe ser transparente."]],
                           say=[2])]),
    ],
    exercises=[
        M("What does “por consenso” mean?", "With general agreement", ["By force", "By accident", "In secret"], "Consenso."),
        M("What is “un vocero”?", "A spokesperson", ["A judge", "A candidate", "A voter"], "Vocero."),
        M("What is “el espectro político”?", "The range from one political side to the other", ["A ghost story", "A kind of election", "A court"], "Espectro."),
        F("Los dos partidos tienen ___ diferentes sobre los impuestos.", "posturas", ["postura", "panoramas", "consensos"], "Plural noun.", tr="The two parties have different stances on taxes."),
        F("El comité aprobó la resolución por ___.", "consenso", ["espectro", "vocero", "panorama"], "By consensus.", tr="The committee approved the resolution by consensus."),
        F("La ___ del ministerio mejoró este año.", "gestión", ["resolución", "postura", "convocatoria"], "Management.", tr="The ministry’s management improved this year."),
        F("El ___ del gobierno habló con la prensa.", "vocero", ["espectro", "panorama", "consenso"], "Spokesperson.", tr="The government spokesperson spoke with the press."),
        F("El ___ político de la región es complejo.", "panorama", ["vocero", "financiamiento", "ministerio"], "Outlook.", tr="The political outlook of the region is complex."),
        F("El ___ de las campañas debe ser transparente.", "financiamiento", ["espectro", "vocero", "consenso"], "Funding.", tr="The funding of campaigns should be transparent."),
    ],
)

# ---------------------------------------------------------------------------- 785
L785 = lesson(
    "Ideologies and economic systems: capitalismo, socialismo, marxismo",
    "Cada ideología tiene defensores y críticos.",
    requires=["capitalismo", "socialismo", "comunismo", "liberal", "monopolio", "mercado", "propiedad", "privado", "riqueza", "desigualdad", "papel", "sistema"],
    cards=[
        card("Short definitions",
             "These definitions are simplified. Each word has many versions, and people often disagree about their meaning and their results. Notice how the text attributes opinions to defenders and critics.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el capitalismo", "capitalism", "El capitalismo se basa en la propiedad privada y en el mercado."],
                            ["el socialismo", "socialism", "El socialismo defiende un papel mayor del Estado y más igualdad; existen versiones muy diferentes."],
                            ["el comunismo", "communism", "El comunismo propone que los medios de producción sean comunes."],
                            ["el marxismo", "Marxism", "El marxismo parte de las ideas de Karl Marx y Friedrich Engels y critica el capitalismo."],
                            ["el liberalismo", "liberalism", "El liberalismo defiende la libertad individual y limita el poder del Estado."],
                            ["el monopolio", "monopoly", "Hay un monopolio cuando una sola empresa controla un mercado."]],
                           say=[2])]),
        card("Defenders and critics",
             "Defenders of capitalism say that it creates wealth and encourages innovation. Critics say that it can increase inequality. "
             "Defenders of socialism say that it can reduce inequality. Critics say that too much state control can reduce freedom and efficiency. Economists and voters disagree.",
             examples=[
                 ex("Los defensores del capitalismo dicen que crea riqueza.", "Defenders of capitalism say that it creates wealth.", "crea"),
                 ex("Sus críticos dicen que puede aumentar la desigualdad.", "Its critics say that it can increase inequality.", "aumentar"),
             ]),
    ],
    exercises=[
        M("What is “un monopolio”?", "A situation where one company controls a market", ["A group of friendly countries", "A branch of government", "A kind of election"], "Monopolio."),
        M("Which system is based on private property and markets?", "El capitalismo", ["El monopolio", "El comunismo", "La monarquía"], "Capitalismo."),
        M("According to the text, what do critics of capitalism say?", "It can increase inequality", ["It cannot create wealth", "It always ends in war", "It forbids private property"], "Críticos."),
        F("El ___ se basa en la propiedad privada y en el mercado.", "capitalismo", ["monopolio", "comunismo", "marxismo"], "Capitalism.", tr="Capitalism is based on private property and the market."),
        F("El ___ parte de las ideas de Karl Marx y Friedrich Engels.", "marxismo", ["liberalismo", "capitalismo", "monopolio"], "Marxism.", tr="Marxism starts from the ideas of Karl Marx and Friedrich Engels."),
        F("El socialismo defiende un ___ mayor del Estado en la economía.", "papel", ["voto", "monopolio", "riesgo"], "Role.", tr="Socialism defends a larger role for the state in the economy."),
        F("Hay un ___ cuando una sola empresa controla un mercado.", "monopolio", ["socialismo", "liberalismo", "consenso"], "Monopoly.", tr="There is a monopoly when a single company controls a market."),
        F("Los defensores del capitalismo dicen que ___ riqueza.", "crea", ["crean", "creamos", "crear"], "Singular subject.", tr="Defenders of capitalism say that it creates wealth.", lemma="crear:él"),
        F("Sus críticos dicen que puede ___ la desigualdad.", "aumentar", ["aumenta", "aumentan", "aumentado"], "Infinitive after poder.", tr="Its critics say that it can increase inequality."),
    ],
)

# ---------------------------------------------------------------------------- 786
L786 = lesson(
    "Democracy in Latin America: transitions and discontent",
    "En la segunda mitad del siglo veinte, varios países pasaron de gobiernos autoritarios a democracias.",
    requires=["democracia", "transición", "satisfacción", "encuesta", "siglo", "país", "región", "ciudadano", "gobierno", "autoridad", "problema", "participar"],
    cards=[
        card("A general picture",
             "Historians and political scientists often describe the last decades of the twentieth century as a time of transitions from authoritarian governments to democracies in several Latin American countries, especially in South America. "
             "Today, according to several surveys, many citizens are not satisfied with how democracy works, but support for democracy as an idea remains high in many countries. The picture differs from country to country.",
             examples=[
                 ex("En la segunda mitad del siglo veinte, varios países pasaron de gobiernos autoritarios a democracias.", "In the second half of the twentieth century, several countries moved from authoritarian governments to democracies.", "pasaron"),
                 ex("Según varias encuestas, muchos ciudadanos no están satisfechos con el funcionamiento de la democracia.", "According to several surveys, many citizens are not satisfied with how democracy works.", "encuestas"),
                 ex("Sin embargo, el apoyo a la democracia como idea sigue alto en muchos países.", "However, support for democracy as an idea remains high in many countries.", "sigue"),
                 ex("La situación es diferente en cada país.", "The situation is different in each country.", "diferente"),
             ]),
        card("Two meanings of democracy",
             "Some authors say that democracy has two levels: it is a political system (with elections and the vote) and it is also a way of life (respect, participation, ethics). When both levels fail, citizens may feel discontent.",
             examples=[
                 ex("La democracia es un sistema político y también una forma de vida.", "Democracy is a political system and also a way of life.", "forma de vida"),
             ]),
    ],
    exercises=[
        M("What happened in several countries in the second half of the twentieth century?", "They moved from authoritarian governments to democracies", ["They became monarchies", "They closed their borders", "They stopped holding elections"], "Transiciones."),
        M("What do several surveys show, according to the text?", "Many citizens are not satisfied with how democracy works", ["Everyone is satisfied", "Nobody supports democracy", "Nobody answered"], "Encuestas."),
        M("What are the “two levels” of democracy?", "A political system and a way of life", ["Two political parties", "Two branches of government", "Two kinds of elections"], "Dos niveles."),
        F("En la segunda mitad del siglo veinte, varios países ___ de gobiernos autoritarios a democracias.", "pasaron", ["pasó", "pasamos", "pasar"], "Plural subject, past.", tr="In the second half of the twentieth century, several countries moved from authoritarian governments to democracies.", lemma="pasar:ellos:pret"),
        F("Según varias ___, muchos ciudadanos no están satisfechos.", "encuestas", ["encuesta", "elecciones", "sedes"], "Plural noun.", tr="According to several surveys, many citizens are not satisfied.", ),
        F("El apoyo a la democracia como idea ___ alto en muchos países.", "sigue", ["siguen", "seguimos", "seguir"], "Singular subject.", tr="Support for democracy as an idea remains high in many countries.", lemma="seguir:él"),
        F("La situación es ___ en cada país.", "diferente", ["diferentes", "diferencia", "diferir"], "Singular adjective.", tr="The situation is different in each country."),
        F("La democracia es un sistema político y también una forma de ___.", "vida", ["voto", "ley", "poder"], "Way of life.", tr="Democracy is a political system and also a way of life."),
        F("Para que funcione la democracia, los ciudadanos deben ___ en la vida pública.", "participar", ["participan", "participamos", "participado"], "Infinitive after deber.", tr="For democracy to work, citizens must participate in public life."),
    ],
)

# ---------------------------------------------------------------------------- 787
L787 = lesson(
    "Colonies, independence and self-determination",
    "La autodeterminación es el derecho de un pueblo a decidir su futuro político.",
    requires=["colonia", "colonial", "independencia", "territorio", "derecho", "pueblo", "libre", "imperio", "siglo", "gobierno", "mundial", "comité"],
    cards=[
        card("Key words",
             "These words are used in history and in political news.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la colonia", "colony", "Durante siglos, muchos territorios fueron colonias de países europeos."],
                            ["la descolonización", "decolonization", "La descolonización es el proceso por el que una colonia llega a gobernarse a sí misma."],
                            ["la independencia", "independence", "La mayoría de los países hispanohablantes de América se independizaron de España en el siglo diecinueve."],
                            ["la autodeterminación", "self-determination", "La autodeterminación es el derecho de un pueblo a decidir su futuro político."],
                            ["el territorio", "territory", "Un territorio puede tener un gobierno propio con poderes limitados."]],
                           say=[2])]),
        card("The United Nations and decolonization",
             "The United Nations has a committee that studies territories that do not yet govern themselves fully, and it keeps an official list of them. Each year the committee also discusses the question of Puerto Rico, although Puerto Rico is not on that list and the United States considers the matter an internal one. "
             "People in Puerto Rico and outside it hold different opinions about its political future: some prefer statehood, some prefer independence, and some prefer to keep the present status.",
             examples=[
                 ex("En Puerto Rico hay opiniones diferentes sobre el futuro político de la isla.", "In Puerto Rico there are different opinions about the island’s political future.", "opiniones"),
                 ex("El comité de la ONU estudia territorios que todavía no se gobiernan completamente.", "The UN committee studies territories that do not yet govern themselves completely.", "estudia"),
             ]),
    ],
    exercises=[
        M("What is “la descolonización”?", "The process by which a colony comes to govern itself", ["The founding of a colony", "A kind of tax", "A treaty between empires"], "Descolonización."),
        M("What is “la autodeterminación”?", "A people’s right to decide its political future", ["A police power", "A kind of trade", "A tax law"], "Autodeterminación."),
        M("What does the text say about opinions on Puerto Rico’s future?", "They are different", ["Everyone agrees", "Nobody has an opinion", "Only the UN has an opinion"], "Opiniones diferentes."),
        F("La mayoría de los países hispanohablantes de América se independizaron en el siglo ___.", "diecinueve", ["dieciséis", "veinte", "veintiuno"], "Nineteenth century.", tr="Most Spanish-speaking countries of the Americas became independent in the nineteenth century."),
        F("Un pueblo tiene derecho a decidir su futuro ___.", "político", ["políticos", "política", "politiquería"], "Masculine singular.", tr="A people has the right to decide its political future."),
        F("La ___ es el proceso por el que una colonia llega a gobernarse a sí misma.", "descolonización", ["independencia", "autodeterminación", "alianza"], "Decolonization.", tr="Decolonization is the process by which a colony comes to govern itself."),
        F("El comité de la ONU ___ territorios que todavía no se gobiernan completamente.", "estudia", ["estudian", "estudiamos", "estudiar"], "Singular subject.", tr="The UN committee studies territories that do not yet govern themselves completely.", lemma="estudiar:él"),
        F("Durante siglos, muchos territorios ___ colonias de países europeos.", "fueron", ["fue", "fuimos", "será"], "Plural subject, past period.", tr="For centuries, many territories were colonies of European countries.", lemma="ser:ellos:pret"),
        F("Hay opiniones muy ___ sobre el futuro político de la isla.", "diferentes", ["diferente", "diferencia", "diferir"], "Plural adjective.", tr="There are very different opinions about the island’s political future."),
    ],
)

# ---------------------------------------------------------------------------- 788
L788 = lesson(
    "Verbs of politics, part 1: exhortar, reivindicar, anular, postergar",
    "La organización insta a las partes a negociar.",
    requires=["exigir", "reclamar", "anular", "controlar", "decisión", "comité", "gobierno", "derecho", "votación", "mercado", "diálogo", "empresa"],
    cards=[
        card("Ten verbs",
             "These verbs are common in political news. Most are regular. Postergar and similar verbs ending in -gar add u before e in the yo form of the preterite (postergué).",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["exhortar", "to urge", "El comité exhorta a los gobiernos a dialogar."],
                            ["instar", "to urge", "La organización insta a las partes a negociar."],
                            ["reivindicar", "to claim, to demand", "Muchos grupos reivindican sus derechos."],
                            ["reclamar", "to demand, to complain", "Los vecinos reclaman más seguridad."],
                            ["suprimir", "to eliminate", "El gobierno suprimió un impuesto."],
                            ["anular", "to cancel, to annul", "El tribunal anuló la decisión."],
                            ["postergar", "to postpone", "El Congreso postergó la votación."],
                            ["manipular", "to manipulate", "Es un error manipular la información."],
                            ["monopolizar", "to monopolize", "Una empresa no debe monopolizar el mercado."],
                            ["institucionalizar", "to make official, to institutionalize", "Los países quieren institucionalizar el diálogo."]],
                           say=[2])]),
        card("Preterite of postergar",
             "Postergar is regular in the preterite except for the yo form: postergué, postergaste, postergó, postergamos, postergasteis, postergaron.",
             tables=[table(["Persona", "postergar (pretérito)"],
                           [["yo", "postergué"], ["tú", "postergaste"], ["él / ella / usted", "postergó"],
                            ["nosotros", "postergamos"], ["vosotros", "postergasteis"], ["ellos / ustedes", "postergaron"]],
                           say=[1])]),
    ],
    exercises=[
        M("What does “postergar” mean?", "To postpone", ["To cancel for good", "To repeat", "To vote"], "Postergar."),
        M("What does “anular” mean?", "To cancel or annul", ["To announce", "To add", "To count"], "Anular."),
        M("Which two verbs both mean “to urge”?", "exhortar and instar", ["anular and suprimir", "reclamar and postergar", "manipular and monopolizar"], "Exhortar, instar."),
        F("Ayer el Congreso ___ la votación hasta el mes próximo.", "postergó", ["posterga", "postergamos", "postergar"], "Past event, singular.", tr="Yesterday Congress postponed the vote until next month.", lemma="postergar:él:pret"),
        F("Yo ___ la reunión porque estaba enfermo.", "postergué", ["postergó", "postergaste", "postergaron"], "Yo form.", tr="I postponed the meeting because I was sick.", lemma="postergar:yo:pret"),
        F("El tribunal ___ la decisión.", "anuló", ["anulan", "anulamos", "anular"], "Past event, singular.", tr="The court annulled the decision.", lemma="anular:él:pret"),
        F("Los vecinos ___ más seguridad.", "reclaman", ["reclama", "reclamamos", "reclamar"], "Plural subject.", tr="The neighbors demand more security.", lemma="reclamar:ellos"),
        F("La organización ___ a las partes a negociar.", "insta", ["instan", "instamos", "instar"], "Singular subject.", tr="The organization urges the parties to negotiate.", lemma="instar:él"),
        F("El gobierno ___ un impuesto el año pasado.", "suprimió", ["suprime", "suprimimos", "suprimir"], "Last year → preterite.", tr="The government eliminated a tax last year.", lemma="suprimir:él:pret"),
    ],
    verify=vpp("postergar", "postergué", "postergaste", "postergó", "postergamos", "postergasteis", "postergaron"),
)

# ---------------------------------------------------------------------------- 789
L789 = lesson(
    "Verbs of politics, part 2: desembocar, ahondar, trascender, tender a",
    "La crisis desembocó en protestas. Los precios tienden a subir.",
    requires=["crisis", "protesta", "problema", "precio", "subir", "agua", "dominar", "partido", "mujer", "joven", "región", "causa"],
    cards=[
        card("Thirteen more verbs",
             "Learn the pattern with the preposition: desembocar EN, tender A, converger EN, ahondar EN.",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["implantar", "to establish", "El gobierno implantó un nuevo sistema de salud."],
                            ["dirimir", "to settle", "Un tribunal dirime el conflicto entre las partes."],
                            ["converger", "to converge", "Las dos opiniones convergen en un punto."],
                            ["desembocar en", "to lead to, to end in", "La crisis desembocó en protestas."],
                            ["agravar", "to worsen", "La sequía agravó el problema."],
                            ["ahondar en", "to go deeper into", "Los estudios ahondan en las causas del problema."],
                            ["empoderar", "to empower", "Los programas buscan empoderar a las mujeres."],
                            ["galvanizar", "to galvanize", "La noticia galvanizó a los jóvenes."],
                            ["resurgir", "to reappear", "El movimiento resurgió en los años noventa."],
                            ["predominar", "to prevail", "En esa región predomina el clima seco."],
                            ["padecer", "to suffer", "Muchas regiones padecen sequías."],
                            ["trascender", "to transcend, to go beyond", "Esa idea trasciende las fronteras del país."],
                            ["tender a", "to tend to", "Los precios tienden a subir."]],
                           say=[2])]),
        card("Four irregular present tenses",
             "Padecer → padezco. Tender → tiendo (e → ie). Resurgir → resurjo (g → j). Trascender → trasciendo (e → ie).",
             tables=[table(["Persona", "padecer", "tender", "resurgir", "trascender"],
                           [["yo", "padezco", "tiendo", "resurjo", "trasciendo"], ["tú", "padeces", "tiendes", "resurges", "trasciendes"],
                            ["él / ella / usted", "padece", "tiende", "resurge", "trasciende"], ["nosotros", "padecemos", "tendemos", "resurgimos", "trascendemos"],
                            ["vosotros", "padecéis", "tendéis", "resurgís", "trascendéis"], ["ellos / ustedes", "padecen", "tienden", "resurgen", "trascienden"]],
                           say=[1, 2, 3, 4])]),
    ],
    exercises=[
        M("What does “desembocar en” mean in “La crisis desembocó en protestas”?", "To lead to", ["To start from", "To avoid", "To stop"], "Desembocar en."),
        M("What does “agravar” mean?", "To make worse", ["To make cheaper", "To make shorter", "To make older"], "Agravar."),
        M("What does “tender a” mean?", "To tend to", ["To hold out a hand only", "To stop", "To refuse"], "Tender a."),
        F("El año pasado, la crisis ___ en protestas en varias ciudades.", "desembocó", ["desemboca", "desembocamos", "desembocar"], "Past event.", tr="Last year the crisis led to protests in several cities.", lemma="desembocar:él:pret"),
        F("El año pasado, la sequía ___ el problema del agua.", "agravó", ["agrava", "agravamos", "agravar"], "Past event.", tr="Last year the drought worsened the water problem.", lemma="agravar:él:pret"),
        F("Los precios ___ a subir cuando hay una crisis.", "tienden", ["tiende", "tendemos", "tender"], "Plural subject; e → ie.", tr="Prices tend to rise when there is a crisis.", lemma="tender:ellos"),
        F("Muchas regiones ___ sequías cada año.", "padecen", ["padece", "padezco", "padecemos"], "Plural subject.", tr="Many regions suffer droughts every year.", lemma="padecer:ellos"),
        F("Yo ___ de dolores de cabeza cuando hay mucho ruido.", "padezco", ["padece", "padeces", "padecen"], "Yo form: -zco.", tr="I suffer from headaches when there is a lot of noise.", lemma="padecer:yo"),
        F("El movimiento ___ en los años noventa.", "resurgió", ["resurge", "resurgimos", "resurgir"], "Past event.", tr="The movement reappeared in the nineties.", lemma="resurgir:él:pret"),
    ],
    verify=(vp("padecer", "padezco", "padeces", "padece", "padecemos", "padecéis", "padecen")
            + vp("tender", "tiendo", "tiendes", "tiende", "tendemos", "tendéis", "tienden")
            + vp("resurgir", "resurjo", "resurges", "resurge", "resurgimos", "resurgís", "resurgen")
            + vp("trascender", "trasciendo", "trasciendes", "trasciende", "trascendemos", "trascendéis", "trascienden")),
)

# ---------------------------------------------------------------------------- 790
L790 = lesson(
    "Nouns for ideas and attitudes: carisma, declive, utopía",
    "Un líder con carisma atrae a mucha gente.",
    requires=["líder", "atraer", "gente", "ciudad", "confianza", "esperanza", "sueño", "tradición", "crecer", "precio", "camino", "perfecto"],
    cards=[
        card("Twelve nouns",
             "These nouns appear in essays and political analysis. Notice their gender: el carisma, el declive, el culto, el descontento, el desgaste, el duelo, el hechizo, but la encrucijada, la falacia, la impronta, la utopía; el apego is masculine.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el apego", "attachment", "Muchas personas sienten apego por su ciudad."],
                            ["el carisma", "charisma", "Un líder con carisma atrae a mucha gente."],
                            ["el culto", "worship, cult", "El culto a un líder puede ser peligroso para la democracia, según algunos críticos."],
                            ["el declive", "decline", "Hay un declive en la confianza en las instituciones."],
                            ["el descontento", "discontent", "El descontento crece cuando suben los precios."],
                            ["el desgaste", "wear, erosion", "Después de años en el cargo, un gobierno puede sufrir desgaste."],
                            ["el duelo", "mourning", "Después de una tragedia, un país puede declarar días de duelo."],
                            ["la encrucijada", "crossroads", "El país está en una encrucijada: debe elegir entre dos caminos."],
                            ["la falacia", "fallacy", "Una falacia parece un buen argumento, pero no lo es."],
                            ["el hechizo", "spell, charm", "El hechizo de un buen discurso puede durar poco."],
                            ["la impronta", "imprint", "Las culturas indígenas dejaron una impronta profunda en la región."],
                            ["la utopía", "utopia", "Una utopía es una sociedad perfecta que solo existe en la imaginación."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “una encrucijada”?", "A crossroads, a difficult choice", ["A kind of tax", "A holiday", "A bridge"], "Encrucijada."),
        M("What is “una falacia”?", "An argument that seems good but is not", ["A true fact", "A type of law", "A famous speech"], "Falacia."),
        M("What is “una utopía”?", "An imaginary perfect society", ["A real country", "A kind of election", "A court"], "Utopía."),
        F("Un líder con ___ atrae a mucha gente.", "carisma", ["falacia", "duelo", "declive"], "Charisma.", tr="A leader with charisma attracts many people.", ),
        F("Hay un ___ en la confianza en las instituciones.", "declive", ["carisma", "hechizo", "apego"], "Decline.", tr="There is a decline in trust in institutions."),
        F("El ___ crece cuando suben los precios.", "descontento", ["hechizo", "duelo", "carisma"], "Discontent.", tr="Discontent grows when prices rise.", ),
        F("Muchas personas sienten ___ por su ciudad.", "apego", ["carisma", "duelo", "declive"], "Attachment.", tr="Many people feel attachment to their city."),
        F("El país está en una ___: debe elegir entre dos caminos.", "encrucijada", ["utopía", "falacia", "impronta"], "Crossroads.", tr="The country is at a crossroads: it must choose between two paths."),
        F("Un líder con carisma ___ a mucha gente.", "atrae", ["atraen", "atraemos", "atraer"], "Singular subject.", tr="A leader with charisma attracts many people.", lemma="atraer:él"),
    ],
)

# ---------------------------------------------------------------------------- 791
L791 = lesson(
    "Adjectives for analysis: apremiante, ingente, inalienable, populista",
    "Es una necesidad apremiante y un derecho inalienable.",
    requires=["derecho", "necesidad", "problema", "decisión", "persona", "útil", "sencillo", "amigo", "ético", "profundo", "tarea", "ayuda"],
    cards=[
        card("Eighteen adjectives",
             "Adjectives ending in -o have four forms (apremiante does not: it ends in -e). Most adjectives ending in -e or a consonant have two forms (apremiante, apremiantes; útil, útiles). Adjectives ending in -dor, like liberador, have four forms (liberador, liberadora, liberadores, liberadoras).",
             tables=[table(["Adjetivo", "English", "Ejemplo"],
                           [["afín", "related, similar", "Los dos partidos tienen ideas afines."],
                            ["agobiante", "overwhelming", "El calor era agobiante."],
                            ["ambivalente", "ambivalent", "Tengo sentimientos ambivalentes sobre el plan."],
                            ["amistoso", "friendly", "Hubo una reunión amistosa entre los dos países."],
                            ["apremiante", "urgent", "Es una necesidad apremiante."],
                            ["deliberado", "deliberate", "Fue un error deliberado."],
                            ["desmedido", "excessive", "Un gasto desmedido puede causar problemas."],
                            ["ético", "ethical", "Es importante tomar decisiones éticas."],
                            ["hondo", "deep", "Hay un hondo descontento en la población."],
                            ["inalienable", "inalienable", "La libertad es un derecho inalienable."],
                            ["indeciso", "undecided", "Muchos votantes están indecisos."],
                            ["inescrupuloso", "unscrupulous", "Un político inescrupuloso no respeta las reglas."],
                            ["ingente", "huge", "El país enfrenta un ingente problema de deuda."],
                            ["liberador", "liberating", "Para muchas personas, la educación es una experiencia liberadora."],
                            ["pendiente", "pending", "Hay un asunto pendiente."],
                            ["populista", "populist", "Algunos críticos dicen que ese discurso es populista."],
                            ["sencillo", "simple", "La solución no es sencilla."],
                            ["útil", "useful", "Esta información es muy útil."]],
                           say=[2])]),
    ],
    exercises=[
        M("What does “apremiante” mean?", "Urgent", ["Friendly", "Optional", "Ancient"], "Apremiante."),
        M("What does “indeciso” mean?", "Undecided", ["Very decided", "Dishonest", "Angry"], "Indeciso."),
        M("What does “ingente” mean?", "Huge", ["Tiny", "Secret", "Friendly"], "Ingente."),
        F("La libertad es un derecho ___.", "inalienable", ["inalienables", "indeciso", "amistoso"], "Singular, masculine noun.", tr="Freedom is an inalienable right."),
        F("Es una necesidad ___ y no podemos esperar.", "apremiante", ["apremiantes", "apremiado", "apremio"], "Singular, urgent.", tr="It is an urgent need and we cannot wait."),
        F("Muchos votantes están todavía ___.", "indecisos", ["indeciso", "indecisa", "decidir"], "Masculine plural.", tr="Many voters are still undecided.", ),
        F("Un político ___ no respeta las reglas.", "inescrupuloso", ["inescrupulosa", "inescrupulosos", "escrúpulo"], "Masculine singular.", tr="An unscrupulous politician does not respect the rules.", ),
        F("Hay un asunto ___ que debemos resolver.", "pendiente", ["pendientes", "pendiendo", "pender"], "Singular noun.", tr="There is a pending matter that we must resolve."),
        F("Esta información es muy ___.", "útil", ["útiles", "usar", "usada"], "Singular.", tr="This information is very useful."),
    ],
)

# ---------------------------------------------------------------------------- 792
L792 = lesson(
    "Society words: desinformación, malestar, reivindicación, perjuicio",
    "La desinformación es información falsa que circula como si fuera verdadera.",
    requires=["información", "falso", "trabajador", "clase", "pobre", "dinero", "región", "agricultor", "estudiante", "ley", "programa", "agua"],
    cards=[
        card("Thirteen words",
             "These words are useful for reading about social problems and political demands.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["la clase pudiente", "the wealthy class", "La clase pudiente es el grupo de personas con más dinero."],
                            ["la desinformación", "disinformation, misinformation", "La desinformación es información falsa que circula como si fuera verdadera."],
                            ["el desmantelamiento", "dismantling", "Algunos temen el desmantelamiento de los programas sociales."],
                            ["el empobrecimiento", "impoverishment", "El empobrecimiento de una región ocurre cuando la gente tiene cada vez menos dinero."],
                            ["la lucha de clases", "class struggle", "Según el marxismo, la lucha de clases explica muchos cambios históricos."],
                            ["el malestar", "discontent, unease", "Hay malestar entre los trabajadores."],
                            ["la reivindicación", "demand, claim", "Los estudiantes presentaron sus reivindicaciones."],
                            ["la servidumbre", "servitude", "La servidumbre era una forma de trabajo obligatorio."],
                            ["el vicio", "vice, bad habit", "Un vicio es un mal hábito."],
                            ["la incógnita", "unknown, mystery", "El resultado de las elecciones es una incógnita."],
                            ["el influjo", "influence", "La región vive bajo el influjo de varias culturas."],
                            ["el perjuicio", "harm, damage", "La sequía causó un gran perjuicio a los agricultores."],
                            ["la sombra", "shadow", "La sombra de la crisis preocupa al país."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “la desinformación”?", "False information that circulates as if it were true", ["A government office", "A type of tax", "A school subject"], "Desinformación."),
        M("What is “una reivindicación”?", "A demand or claim", ["A holiday", "A kind of vote", "A type of law"], "Reivindicación."),
        M("What is “un perjuicio”?", "Harm or damage", ["A prize", "A celebration", "A secret"], "Perjuicio."),
        F("La sequía causó un gran ___ a los agricultores.", "perjuicio", ["vicio", "influjo", "servidumbre"], "Harm.", tr="The drought caused great harm to farmers.", ),
        F("Los estudiantes presentaron sus ___.", "reivindicaciones", ["reivindicación", "incógnitas", "sombra"], "Plural.", tr="The students presented their demands."),
        F("El resultado de las elecciones es una ___.", "incógnita", ["servidumbre", "reivindicación", "clase"], "Unknown.", tr="The result of the elections is an unknown."),
        F("Hay ___ entre los trabajadores por los bajos sueldos.", "malestar", ["incógnita", "servidumbre", "influjo"], "Unease.", tr="There is discontent among the workers because of low salaries."),
        F("La ___ es información falsa que circula como si fuera verdadera.", "desinformación", ["servidumbre", "reivindicación", "sombra"], "Misinformation.", tr="Misinformation is false information that circulates as if it were true."),
        F("Según el marxismo, la lucha de ___ explica muchos cambios históricos.", "clases", ["clase", "vicios", "sombras"], "Class struggle.", tr="According to Marxism, the class struggle explains many historical changes."),
    ],
)

# ---------------------------------------------------------------------------- 793
L793 = lesson(
    "Connecting expressions: a medida que, al margen de, otrora, por más que",
    "A medida que suben los precios, baja la demanda.",
    requires=["precio", "demanda", "bajar", "lograr", "intentar", "diferencia", "hablar", "gobierno", "capital", "situación", "mejorar", "vez"],
    cards=[
        card("Linking ideas",
             "These expressions help connect ideas in formal writing and speeches.",
             tables=[table(["Expresión", "English", "Ejemplo"],
                           [["acorde a / con", "in accordance with", "Los sueldos deben ser acordes con el costo de la vida."],
                            ["ahora bien", "however, now then", "Ahora bien, no todos están de acuerdo."],
                            ["al margen de", "regardless of", "Al margen de las diferencias, los países cooperan."],
                            ["a la par", "at the same time, on a par", "La economía crece a la par que la población."],
                            ["a medida que", "as (progressively)", "A medida que suben los precios, baja la demanda."],
                            ["a su vez", "in turn", "El ministro, a su vez, respondió a las críticas."],
                            ["de corte + adjetivo", "of a … kind", "Es un gobierno de corte moderado."],
                            ["de vez en cuando", "from time to time", "Voy a la capital de vez en cuando."],
                            ["en lugar de", "instead of", "En lugar de protestar, decidieron dialogar."],
                            ["o sea", "in other words", "Llego el lunes, o sea, en dos días."],
                            ["otrora", "formerly", "La otrora capital del imperio es hoy una ciudad pequeña."],
                            ["paulatinamente", "gradually", "La situación mejoró paulatinamente."],
                            ["por cierto", "by the way", "Por cierto, ¿viste la noticia?"]],
                           say=[2])]),
        card("Por más que, por mucho que",
             "These two expressions mean “no matter how much” and are followed by the subjunctive when the action is hypothetical or has not happened yet.",
             examples=[
                 ex("Por más que lo intente, no lo logrará.", "No matter how hard he tries, he will not succeed.", "intente"),
                 ex("Por mucho que insistan, no cambiaré de opinión.", "No matter how much they insist, I will not change my mind.", "insistan"),
             ]),
    ],
    exercises=[
        M("What does “en lugar de” mean?", "Instead of", ["In addition to", "Because of", "After"], "En lugar de."),
        M("What does “a medida que” express?", "A change happening along with another change", ["A single sudden event", "A contrast with the past only", "A question"], "Progressive."),
        M("What does “o sea” introduce?", "A restatement (in other words)", ["A new question", "A command", "A date"], "O sea."),
        F("___ suben los precios, baja la demanda.", "A medida que", ["En lugar de", "De vez en cuando", "Por cierto"], "Progressive change.", tr="As prices rise, demand falls."),
        F("___ protestar, decidieron dialogar.", "En lugar de", ["A medida que", "De vez en cuando", "Por cierto"], "Instead of.", tr="Instead of protesting, they decided to hold a dialogue."),
        F("Por más que ___, no lo logrará.", "lo intente", ["lo intentaría", "lo intentará", "lo intentando"], "Por más que + subjunctive.", tr="No matter how hard he tries, he will not succeed.", ),
        F("La situación mejoró ___.", "paulatinamente", ["otrora", "por cierto", "ahora bien"], "Gradually.", tr="The situation improved gradually."),
        F("La ___ capital del imperio es hoy una ciudad pequeña.", "otrora", ["paulatinamente", "ahora bien", "a su vez"], "Formerly.", tr="The former capital of the empire is today a small city."),
        F("Los sueldos deben ser acordes ___ el costo de la vida.", "con", ["en", "por", "sin"], "Acorde con.", tr="Salaries should be in line with the cost of living."),
    ],
)

# ---------------------------------------------------------------------------- 794
L794 = lesson(
    "Set expressions: allanar el camino, dar la espalda, hacerse cargo",
    "El acuerdo allanó el camino para una paz duradera.",
    requires=["camino", "espalda", "cargo", "casa", "ventana", "paz", "problema", "ministro", "educación", "fiesta", "bandera", "plaza"],
    cards=[
        card("Idioms and fixed phrases",
             "Idioms cannot be translated word for word. Learn each phrase as one unit.",
             tables=[table(["Expresión", "English", "Ejemplo"],
                           [["allanar el camino", "to pave the way", "El acuerdo allanó el camino para una paz duradera."],
                            ["dar la espalda a", "to turn one’s back on", "No debemos dar la espalda a los problemas."],
                            ["hacerse cargo de", "to take charge of", "El nuevo ministro se hace cargo de la educación."],
                            ["tirar la casa por la ventana", "to go all out (spend a lot)", "Para su aniversario, tiraron la casa por la ventana."],
                            ["no se vale + infinitivo", "it’s not fair to …", "No se vale copiar en el examen."],
                            ["un arma de dos filos", "a double-edged sword", "Internet es un arma de dos filos."],
                            ["la bandera a media asta", "flag at half-mast", "Las banderas están a media asta por el duelo."],
                            ["los fuegos de artificio", "fireworks", "Hubo fuegos de artificio en la plaza."]],
                           say=[2]),
                    table(["Registro", "Expresión", "Nota"],
                          [["informal", "cerrar el pico", "Means “to shut up”. It is impolite; use callarse or guardar silencio instead."],
                           ["informal (Mexico and elsewhere)", "no se vale", "Used in everyday speech to say that something is not fair."]],
                          say=[1])]),
    ],
    exercises=[
        M("What does “allanar el camino” mean?", "To pave the way", ["To walk slowly", "To close a road", "To get lost"], "Allanar el camino."),
        M("What does “tirar la casa por la ventana” mean?", "To spend a lot on a celebration", ["To throw furniture away", "To sell a house", "To break a window"], "Idiom."),
        M("What does “un arma de dos filos” mean?", "Something with good and bad effects", ["A very sharp knife", "A kind of weapon only", "A secret plan"], "Double-edged."),
        F("El acuerdo ___ el camino para una paz duradera.", "allanó", ["allana", "allanamos", "allanar"], "Past event.", tr="The agreement paved the way for a lasting peace.", lemma="allanar:él:pret"),
        F("No debemos dar la ___ a los problemas.", "espalda", ["casa", "ventana", "bandera"], "Dar la espalda.", tr="We must not turn our backs on the problems."),
        F("El nuevo ministro se ___ cargo de la educación.", "hace", ["hacen", "hacemos", "hacer"], "Singular subject.", tr="The new minister takes charge of education."),
        F("Para celebrar, tiraron la ___ por la ventana.", "casa", ["espalda", "bandera", "plaza"], "Idiom.", tr="To celebrate, they went all out."),
        F("Internet es un ___ de dos filos.", "arma", ["armas", "filo", "casa"], "Un arma (feminine noun).", tr="The Internet is a double-edged sword."),
        F("Las banderas están a media ___ por el duelo.", "asta", ["casa", "plaza", "ventana"], "A media asta.", tr="The flags are at half-mast because of the mourning."),
    ],
)

# ---------------------------------------------------------------------------- 795
L795 = lesson(
    "Simón Bolívar and the idea of “bolivarianismo”",
    "Simón Bolívar es llamado “el Libertador” en varios países de América del Sur.",
    requires=["libertador", "héroe", "símbolo", "nacer", "morir", "luchar", "sueño", "nombre", "figura", "histórico", "líder", "cambiar"],
    cards=[
        card("A historical figure and a political label",
             "Simón Bolívar was born in Caracas and fought for the independence of several territories in South America. He is a national hero in several countries and is known as “el Libertador”. "
             "Bolívar dreamed of a close union among the new republics, though that union did not last. He died in the year eighteen thirty.",
             examples=[
                 ex("Simón Bolívar nació en Caracas.", "Simón Bolívar was born in Caracas.", "nació"),
                 ex("Luchó por la independencia de varios territorios.", "He fought for the independence of several territories.", "Luchó"),
                 ex("Murió en mil ochocientos treinta.", "He died in eighteen thirty.", "Murió"),
             ]),
        card("What is “bolivarianismo”?",
             "Bolivarianismo is a general name for ideas inspired by Bolívar, such as regional unity and independence. Different leaders and movements have used his name at different times and with different meanings. "
             "Some defenders say that it expresses a tradition of regional unity. Some critics say that today the name is sometimes used to support current political goals. Historians often remind us that Bolívar lived in a very different time.",
             examples=[
                 ex("Muchos políticos citan a figuras históricas para apoyar sus ideas.", "Many politicians cite historical figures to support their ideas.", "citan"),
                 ex("Los historiadores recuerdan que Bolívar vivió en una época muy diferente.", "Historians remind us that Bolívar lived in a very different time.", "vivió"),
             ]),
    ],
    exercises=[
        M("What is Simón Bolívar called in several countries?", "El Libertador", ["El Presidente", "El Embajador", "El Canciller"], "El Libertador."),
        M("What did Bolívar dream of, according to the text?", "A close union among the new republics", ["A world empire", "A return of the colonies", "A single language only"], "Union."),
        M("What do historians remind us, according to the text?", "That Bolívar lived in a very different time", ["That Bolívar is a myth", "That Bolívar never fought", "That Bolívar was a king"], "Época diferente."),
        F("Simón Bolívar ___ en Caracas.", "nació", ["nace", "nacemos", "nacer"], "Past event.", tr="Simón Bolívar was born in Caracas.", lemma="nacer:él:pret"),
        F("Bolívar ___ por la independencia de varios territorios.", "luchó", ["lucha", "luchamos", "luchar"], "Past event.", tr="Bolívar fought for the independence of several territories.", lemma="luchar:él:pret"),
        F("Bolívar ___ en mil ochocientos treinta.", "murió", ["muere", "morimos", "morir"], "Past event.", tr="Bolívar died in eighteen thirty.", lemma="morir:él:pret"),
        F("Muchos políticos ___ a figuras históricas para apoyar sus ideas.", "citan", ["cita", "citamos", "citar"], "Plural subject.", tr="Many politicians cite historical figures to support their ideas.", lemma="citar:ellos"),
        F("Para muchas personas, Bolívar es un ___ de unidad regional.", "símbolo", ["símbolos", "símbolas", "simbolizar"], "Masculine singular noun.", tr="For many people, Bolívar is a symbol of regional unity."),
        F("Diferentes líderes han usado su ___ con significados distintos.", "nombre", ["nombres", "nombrar", "nombrado"], "Singular noun.", tr="Different leaders have used his name with different meanings."),
    ],
)

# ---------------------------------------------------------------------------- 796
L796 = lesson(
    "The “marea rosa”: shifts to the left and to the right",
    "Los politólogos llaman “marea rosa” a una ola de gobiernos de izquierda en América Latina.",
    requires=["giro", "ola", "cambiar", "moderado", "radical", "elegir", "gobierno", "político", "región", "elección", "cambio", "partido"],
    cards=[
        card("A term used by journalists and scholars",
             "The expression “marea rosa” (pink tide) refers to the wave of left and center-left governments that were elected in several Latin American countries, starting around the end of the nineteen nineties and the beginning of the two thousands. "
             "The name “pink” (rather than “red”) is usually explained by the fact that many of those governments were moderate. Later, voters in several countries elected governments of the right, and in recent years the political map has changed again.",
             examples=[
                 ex("Muchos países eligieron gobiernos de izquierda a comienzos de los años dos mil.", "Many countries elected left-wing governments in the early two thousands.", "eligieron"),
                 ex("Más tarde, los votantes de varios países eligieron gobiernos de derecha.", "Later, voters in several countries elected right-wing governments.", "derecha"),
                 ex("Los politólogos discuten si el término es útil, porque los gobiernos eran muy diferentes.", "Political scientists discuss whether the term is useful, because the governments were very different.", "discuten"),
             ]),
        card("Words for describing change",
             "A giro is a turn. An ola is a wave. An alternancia (alternation) happens when different parties win power in different elections. A giro a la izquierda means a turn toward the left, and a giro a la derecha means a turn toward the right.",
             examples=[
                 ex("Algunos analistas hablan de un giro a la izquierda.", "Some analysts speak of a turn to the left.", "giro"),
             ]),
    ],
    exercises=[
        M("What is the “marea rosa”?", "A wave of left and center-left governments", ["A natural disaster", "A kind of election", "A trade agreement"], "Marea rosa."),
        M("According to the usual explanation, why is it “pink” and not “red”?", "Because many of those governments were moderate", ["Because they were all identical", "Because they banned elections", "Because they were all new"], "Moderate."),
        M("What do political scientists discuss?", "Whether the term is useful, since the governments differed", ["Whether elections exist", "Whether Latin America exists", "Whether voting is legal"], "Term useful?"),
        F("Muchos países ___ gobiernos de izquierda a comienzos de los años dos mil.", "eligieron", ["eligió", "elegimos", "elegir"], "Plural subject, past.", tr="Many countries elected left-wing governments in the early two thousands.", lemma="elegir:ellos:pret"),
        F("Más tarde, los votantes de varios países ___ gobiernos de derecha.", "eligieron", ["eligió", "eligen", "elegir"], "Plural subject, past.", tr="Later, voters in several countries elected right-wing governments.", lemma="elegir:ellos:pret"),
        F("Algunos analistas hablan de un ___ a la izquierda.", "giro", ["ola", "marea", "cambios"], "A turn.", tr="Some analysts speak of a turn to the left."),
        F("Una ___ es un movimiento grande de cambio, como una marea.", "ola", ["giro", "elección", "alternancia"], "Wave.", tr="A wave is a large movement of change, like a tide."),
        F("Los politólogos ___ si el término es útil.", "discuten", ["discute", "discutimos", "discutir"], "Plural subject.", tr="Political scientists discuss whether the term is useful.", lemma="discutir:ellos"),
        F("Muchos de esos gobiernos eran ___, no radicales.", "moderados", ["moderado", "moderada", "moderar"], "Masculine plural.", tr="Many of those governments were moderate, not radical."),
    ],
)

# ---------------------------------------------------------------------------- 797
L797 = lesson(
    "Populism: a debated word",
    "Populismo es un término muy discutido: los expertos no están de acuerdo.",
    requires=["pueblo", "élite", "líder", "promesa", "fácil", "escuchar", "voz", "ignorar", "institución", "discurso", "político", "opinión"],
    cards=[
        card("Definitions differ",
             "Scholars do not agree on a single definition of populism. Many describe it as a political style or strategy that divides society into “el pueblo” and “las élites” and claims to speak for the people. "
             "Critics say that populist leaders make easy promises and weaken institutions. Defenders say that populism gives a voice to people whom traditional parties ignore. "
             "There are populists of the left and of the right, and politicians often use the word as an insult against their opponents.",
             examples=[
                 ex("Muchos expertos describen el populismo como un estilo político.", "Many experts describe populism as a political style.", "estilo"),
                 ex("Los críticos dicen que los líderes populistas hacen promesas fáciles.", "Critics say that populist leaders make easy promises.", "promesas"),
                 ex("Los defensores dicen que da voz a personas que los partidos tradicionales ignoran.", "Defenders say that it gives a voice to people whom traditional parties ignore.", "ignoran"),
                 ex("Los políticos suelen usar la palabra como insulto contra sus oponentes.", "Politicians often use the word as an insult against their opponents.", "insulto"),
             ]),
        card("Words around populism",
             "La retórica is the use of language to persuade. La oratoria is the art of public speaking. Un orador is a speaker. Un demagogo is a person who wins support with easy promises and emotional appeals. Una élite is a small group with a lot of power or influence.",
             examples=[
                 ex("Un buen orador usa la retórica para convencer al público.", "A good speaker uses rhetoric to convince the public.", "retórica"),
             ]),
    ],
    exercises=[
        M("What does the text say about the definition of populism?", "Scholars do not agree on one definition", ["It has one clear definition", "It is only a left-wing idea", "It is only a right-wing idea"], "Debatida."),
        M("What do defenders of populism say?", "It gives a voice to people whom traditional parties ignore", ["It always weakens institutions", "It is always dishonest", "It is a kind of economy"], "Defenders."),
        M("What is “un orador”?", "A public speaker", ["A voter", "A judge", "A candidate for mayor only"], "Orador."),
        F("Los críticos dicen que los líderes populistas ___ promesas fáciles.", "hacen", ["hace", "hacemos", "hacer"], "Plural subject.", tr="Critics say that populist leaders make easy promises.", lemma="hacer:ellos"),
        F("Los defensores dicen que da ___ a personas que otros partidos ignoran.", "voz", ["voces", "ola", "giro"], "Singular noun.", tr="Defenders say that it gives a voice to people whom other parties ignore."),
        F("Muchos expertos describen el populismo como un ___ político.", "estilo", ["estilos", "votante", "gobierno"], "Singular noun.", tr="Many experts describe populism as a political style."),
        F("Los políticos suelen usar la palabra como ___ contra sus oponentes.", "insulto", ["insultos", "elección", "ley"], "Singular noun.", tr="Politicians often use the word as an insult against their opponents."),
        F("Un buen orador usa la ___ para convencer al público.", "retórica", ["élite", "elección", "institución"], "Rhetoric.", tr="A good speaker uses rhetoric to convince the public."),
        F("Hay populistas de izquierda y de ___.", "derecha", ["izquierda", "derechos", "derecho"], "Left and right.", tr="There are populists of the left and of the right."),
    ],
)

# ---------------------------------------------------------------------------- 798
L798 = lesson(
    "Disinformation and freedom of expression: a balanced debate",
    "Algunas personas quieren regular la desinformación; otras temen que eso limite la libertad de expresión.",
    requires=["libertad", "expresión", "social", "internet", "plataforma", "periodista", "publicar", "proteger", "salud", "verificar", "mentira", "verdad"],
    cards=[
        card("Two concerns",
             "False information can spread very fast on social media. Some people ask for laws that limit it, and others worry that those laws could be used to silence opinions. Both groups say that they want to protect society. "
             "Below are arguments that people make, not proven facts.",
             tables=[table(["Quienes piden regular dicen…", "Quienes se oponen dicen…"],
                           [["La desinformación puede dañar la salud pública y las elecciones.", "No es fácil decidir quién determina lo que es falso."],
                            ["Las plataformas deben tener más responsabilidad.", "Una ley puede convertirse en censura."],
                            ["Las mentiras pueden causar daño real.", "Es mejor educar a la gente y verificar los datos."]],
                           say=[0, 1])]),
        card("Other ideas",
             "Some people prefer solutions that do not restrict speech: teaching media literacy, supporting independent journalists, and making platforms explain how their systems work. Each person can weigh these ideas and form their own opinion.",
             examples=[
                 ex("Los periodistas verifican los datos antes de publicar una noticia.", "Journalists check the facts before publishing a news story.", "verifican"),
                 ex("La educación puede ayudar a distinguir la verdad de la mentira.", "Education can help tell truth from falsehood.", "distinguir"),
             ]),
    ],
    exercises=[
        M("What do the people who want regulation worry about?", "False information can harm public health and elections", ["Too many journalists", "Too little advertising", "Too many libraries"], "Regular."),
        M("What do the people who oppose regulation worry about?", "A law could become censorship", ["Too much education", "Too many newspapers", "Too few elections"], "Censura."),
        M("What does the card suggest about the two groups?", "Both say that they want to protect society", ["Only one group cares", "Neither group has arguments", "Both groups agree completely"], "Both."),
        F("Algunas personas ___ regular la desinformación.", "quieren", ["quiere", "queremos", "querer"], "Plural subject.", tr="Some people want to regulate disinformation.", lemma="querer:ellos"),
        F("Otras temen que una ley ___ la libertad de expresión.", "limite", ["limita", "limitara", "limitará"], "Subjunctive after temen que (present fear).", tr="Others fear that a law may limit freedom of expression.", lemma="limitar:él:subj"),
        F("Los periodistas ___ los datos antes de publicar una noticia.", "verifican", ["verifica", "verificamos", "verificar"], "Plural subject.", tr="Journalists check the facts before publishing a news story.", lemma="verificar:ellos"),
        F("La educación puede ayudar a distinguir la ___ de la mentira.", "verdad", ["verdades", "salud", "plataforma"], "Truth.", tr="Education can help distinguish truth from falsehood."),
        F("Algunas personas dicen que las plataformas deben tener más ___.", "responsabilidad", ["mentira", "censuras", "internet"], "Responsibility.", tr="Some people say that platforms must have more responsibility."),
        F("Cada persona puede ___ las ideas y formar su propia opinión.", "evaluar", ["evalúa", "evalúan", "evaluado"], "Infinitive after poder.", tr="Each person can weigh the ideas and form their own opinion."),
    ],
)

# ---------------------------------------------------------------------------- 799
L799 = lesson(
    "Review: present perfect and pluperfect",
    "He terminado el informe. Ya habían terminado cuando llegué.",
    requires=["haber", "terminar", "abrir", "decir", "escribir", "hacer", "poner", "ver", "volver", "romper", "informe", "llegar"],
    cards=[
        card("How to form the perfect tenses",
             "Both tenses use haber + a past participle. The participle never changes after haber. For the present perfect, haber is in the present (he, has, ha, hemos, habéis, han). "
             "For the pluperfect, haber is in the imperfect (había, habías, había, habíamos, habíais, habían). The pluperfect tells what had already happened before another moment in the past.",
             tables=[table(["Persona", "Presente perfecto", "Pluscuamperfecto"],
                           [["yo", "he terminado", "había terminado"], ["tú", "has terminado", "habías terminado"],
                            ["él / ella / usted", "ha terminado", "había terminado"], ["nosotros", "hemos terminado", "habíamos terminado"],
                            ["vosotros", "habéis terminado", "habíais terminado"], ["ellos / ustedes", "han terminado", "habían terminado"]],
                           say=[1, 2]),
                    table(["Infinitivo", "Participio", "Ejemplo"],
                          [["abrir", "abierto", "Han abierto las puertas."], ["decir", "dicho", "Ya lo he dicho."], ["escribir", "escrito", "Hemos escrito el informe."],
                           ["hacer", "hecho", "¿Qué has hecho?"], ["poner", "puesto", "Había puesto las llaves en la mesa."], ["ver", "visto", "No lo he visto."],
                           ["volver", "vuelto", "Ya habían vuelto a casa."], ["romper", "roto", "He roto el vaso."]],
                          say=[1, 2])]),
        card("Usage note",
             "In Spain, people use the present perfect often for things that happened recently (Hoy he comido temprano). In much of Latin America, the preterite is often used for the same idea (Hoy comí temprano). Both are correct in their regions.",
             examples=[
                 ex("Cuando llegué, ya habían terminado.", "When I arrived, they had already finished.", "habían terminado"),
             ]),
    ],
    exercises=[
        M("Which tense says what had already happened before another past moment?", "The pluperfect", ["The present perfect", "The future", "The conditional"], "Había + participle."),
        M("What is the participle of “escribir”?", "escrito", ["escribido", "escribiendo", "escribí"], "Escrito."),
        M("What is the participle of “volver”?", "vuelto", ["volvido", "volviendo", "volví"], "Vuelto."),
        F("Nosotros ya ___ el informe.", "hemos terminado", ["han terminado", "he terminado", "habéis terminado"], "Nosotros → hemos.", tr="We have already finished the report.", ),
        F("Cuando llegué, ellos ya ___ terminado.", "habían", ["han", "hemos", "habré"], "Before another past moment → había.", tr="When I arrived, they had already finished.", lemma="haber:ellos:impf"),
        F("¿Qué has ___?", "hecho", ["hacido", "haciendo", "hizo"], "Participle of hacer.", tr="What have you done?", lemma="hacer:part"),
        F("Ya lo he ___ muchas veces.", "dicho", ["decido", "diciendo", "dijo"], "Participle of decir.", tr="I have said it many times already.", lemma="decir:part"),
        F("Ellos han ___ las puertas del museo.", "abierto", ["abrido", "abriendo", "abrió"], "Participle of abrir.", tr="They have opened the doors of the museum.", lemma="abrir:part"),
        F("Ayer vi la película, pero tú ya la ___ visto el mes pasado.", "habías", ["has", "habrías", "hubieras"], "Before another past moment.", tr="Yesterday I saw the movie, but you had already seen it last month.", lemma="haber:tú:impf"),
    ],
    verify=(vp("haber", "he", "has", "ha", "hemos", "habéis", "han")
            + vpi("haber", "había", "habías", "había", "habíamos", "habíais", "habían")
            + vpa("abrir", "abierto") + vpa("decir", "dicho") + vpa("escribir", "escrito") + vpa("hacer", "hecho")
            + vpa("poner", "puesto") + vpa("ver", "visto") + vpa("volver", "vuelto") + vpa("romper", "roto")),
)

# ---------------------------------------------------------------------------- 800
L800 = lesson(
    "Perfect tenses with estar and an adjective: ha estado preocupado",
    "El ministro ha estado preocupado. Las vecinas habían estado cansadas.",
    requires=["estar", "preocupado", "cansado", "enfermo", "ocupado", "contento", "nervioso", "triste", "semana", "ministro", "vecino", "alumno"],
    cards=[
        card("How someone has been feeling",
             "To say what state someone has been in, use haber + estado + an adjective. The adjective agrees in gender and number with the subject. "
             "The word estado itself never changes. Because we describe how someone is feeling or doing (a state or condition), we use estar and not ser.",
             tables=[table(["Sujeto", "haber + estado", "Adjetivo"],
                           [["El ministro", "ha estado", "preocupado."],
                            ["Las vecinas", "habían estado", "cansadas."],
                            ["Los alumnos", "han estado", "enfermos."],
                            ["Yo (una mujer)", "he estado", "muy ocupada esta semana."],
                            ["Nosotros", "habíamos estado", "nerviosos antes del examen."]],
                           say=[0, 1, 2])]),
    ],
    exercises=[
        M("Which pattern means “has been worried”?", "ha estado preocupado", ["ha sido preocupado", "está preocupando", "estará preocupado"], "Haber + estado + adjective."),
        M("What stays the same in “han estado enfermos”?", "estado", ["han", "enfermos", "all the words"], "Estado is invariable."),
        M("Why do we use estar and not ser here?", "Because it describes a state or condition (how someone is)", ["Because the sentence is in the future", "Because the subject is plural", "Because it is a question"], "State or condition."),
        F("Las ministras han estado muy ___.", "preocupadas", ["preocupado", "preocupados", "preocupada"], "Feminine plural.", tr="The ministers (f.) have been very worried."),
        F("Los alumnos han ___ enfermos esta semana.", "estado", ["estados", "estada", "estar"], "Invariable participle.", tr="The students have been sick this week.", lemma="estar:part"),
        F("Yo (una mujer) he estado muy ___ esta semana.", "ocupada", ["ocupado", "ocupados", "ocupadas"], "Feminine singular.", tr="I have been very busy this week."),
        F("Las vecinas habían ___ cansadas todo el día.", "estado", ["sido", "estados", "estando"], "Estado, invariable.", tr="The neighbors (f.) had been tired all day.", lemma="estar:part"),
        F("Nosotros habíamos estado muy ___ antes del examen.", "nerviosos", ["nervioso", "nerviosa", "nerviosas"], "Masculine plural.", tr="We had been very nervous before the exam."),
        F("El alcalde ___ estado muy contento con los resultados.", "ha", ["han", "he", "hemos"], "Singular subject.", tr="The mayor has been very pleased with the results.", lemma="haber:él"),
    ],
    verify=vpa("estar", "estado"),
)

# ---------------------------------------------------------------------------- 801
L801 = lesson(
    "Perfect tenses in the passive: ha sido aprobada, habían sido cerradas",
    "La ley ha sido aprobada por el Congreso. Las fronteras habían sido cerradas.",
    requires=["ser", "aprobar", "cerrar", "firmar", "ley", "documento", "frontera", "congreso", "policía", "puerta", "carta", "informe"],
    cards=[
        card("Something has been done by someone",
             "To say that something has been done or had been done (usually by someone else), use haber + sido + a participle. The participle agrees with the thing that received the action. Add por to name the person who did it.",
             tables=[table(["Cosa", "haber + sido", "Participio", "Agente"],
                           [["La ley", "ha sido", "aprobada", "por el Congreso."],
                            ["Los documentos", "han sido", "firmados", "por los ministros."],
                            ["Las fronteras", "habían sido", "cerradas", "por el gobierno."],
                            ["El informe", "había sido", "escrito", "por un comité."]],
                           say=[0, 1, 2, 3])]),
        card("Ser or estar?",
             "Han sido firmados means that someone signed the documents (an action). Están firmados means that the documents are in a signed state (a result). Spanish also has a passive with se: Se han firmado los documentos.",
             examples=[
                 ex("Los documentos han sido firmados por los ministros.", "The documents have been signed by the ministers.", "han sido firmados"),
                 ex("Los documentos están firmados.", "The documents are signed.", "están firmados"),
                 ex("Se han firmado los documentos.", "The documents have been signed.", "Se han firmado"),
             ]),
    ],
    exercises=[
        M("Which sentence says that an action was done to the documents?", "Los documentos han sido firmados.", ["Los documentos están firmados.", "Los documentos firman.", "Los documentos serán firmados ayer."], "Ha sido + participle."),
        M("What does the participle agree with in “La ley ha sido aprobada”?", "La ley", ["ha", "sido", "el Congreso"], "Agrees with the thing."),
        M("Which sentence describes a result and not an action?", "Los documentos están firmados.", ["Los documentos han sido firmados.", "Los documentos habían sido firmados.", "Se han firmado los documentos."], "Estar + participle = state."),
        F("La ley ha sido ___ por el Congreso.", "aprobada", ["aprobado", "aprobados", "aprobar"], "Feminine singular.", tr="The law has been approved by Congress."),
        F("Los documentos han sido ___ por los ministros.", "firmados", ["firmado", "firmada", "firmar"], "Masculine plural.", tr="The documents have been signed by the ministers."),
        F("Las fronteras habían sido ___ por el gobierno.", "cerradas", ["cerrado", "cerrada", "cerrados"], "Feminine plural.", tr="The borders had been closed by the government."),
        F("El informe había ___ escrito por un comité.", "sido", ["estado", "sidos", "siendo"], "Passive: ser.", tr="The report had been written by a committee.", lemma="ser:part"),
        F("Las cartas ya ___ sido enviadas cuando llegué.", "habían", ["han", "habrán", "habría"], "Before another past moment.", tr="The letters had already been sent when I arrived.", lemma="haber:ellos:impf"),
        F("Se ___ firmado los documentos.", "han", ["ha", "he", "hemos"], "Plural thing: se han.", tr="The documents have been signed.", lemma="haber:ellos"),
    ],
    verify=vpa("ser", "sido"),
)

# ---------------------------------------------------------------------------- 802
L802 = lesson(
    "Perfect continuous: han estado hablando, había estado leyendo",
    "Los vecinos han estado hablando con los técnicos durante semanas.",
    requires=["estar", "hablar", "trabajar", "leer", "dormir", "esperar", "buscar", "técnico", "semana", "mes", "tiempo", "problema"],
    cards=[
        card("An action in progress up to a moment",
             "Use haber + estado + a gerund (-ando, -iendo) for an action that has been going on for a while. The present perfect continuous (han estado hablando) connects the action to now. "
             "The past perfect continuous (habían estado hablando) connects it to an earlier moment in the past.",
             tables=[table(["Persona", "Presente perfecto continuo", "Pluscuamperfecto continuo"],
                           [["yo", "he estado leyendo", "había estado leyendo"], ["tú", "has estado hablando", "habías estado hablando"],
                            ["él / ella / usted", "ha estado trabajando", "había estado trabajando"], ["nosotros", "hemos estado esperando", "habíamos estado esperando"],
                            ["vosotros", "habéis estado buscando", "habíais estado buscando"], ["ellos / ustedes", "han estado durmiendo", "habían estado durmiendo"]],
                           say=[1, 2])]),
        card("Gerunds and pronouns",
             "Gerunds of -er and -ir verbs with a vowel before the ending use -yendo (leer → leyendo). Some stem-changing -ir verbs change the vowel (dormir → durmiendo, pedir → pidiendo). "
             "A pronoun goes before haber or attached to the gerund (with a written accent): Lo han estado discutiendo = Han estado discutiéndolo.",
             examples=[
                 ex("Lo han estado discutiendo durante semanas.", "They have been discussing it for weeks.", "discutiendo"),
                 ex("Habían estado esperando dos horas cuando por fin abrieron la puerta.", "They had been waiting for two hours when they finally opened the door.", "esperando"),
             ]),
    ],
    exercises=[
        M("Which pattern means “have been talking”?", "han estado hablando", ["han sido hablando", "están hablado", "habrán hablar"], "Haber + estado + gerund."),
        M("What is the gerund of “leer”?", "leyendo", ["leiendo", "leído", "leyó"], "Leyendo."),
        M("What is the gerund of “dormir”?", "durmiendo", ["dormiendo", "dormido", "durmió"], "Durmiendo."),
        F("Los vecinos han estado ___ con los técnicos durante semanas.", "hablando", ["hablado", "hablan", "hablar"], "Gerund.", tr="The neighbors have been talking with the technicians for weeks.", lemma="hablar:ger"),
        F("Yo he estado ___ ese libro toda la tarde.", "leyendo", ["leído", "leiendo", "leyó"], "Gerund of leer.", tr="I have been reading that book all afternoon.", lemma="leer:ger"),
        F("Ellos han estado ___ toda la noche.", "durmiendo", ["dormiendo", "dormido", "durmieron"], "Gerund of dormir.", tr="They have been sleeping all night.", lemma="dormir:ger"),
        F("Cuando llegó el autobús, nosotros ya ___ estado esperando dos horas.", "habíamos", ["hemos", "habremos", "habríamos"], "Before another past moment.", tr="When the bus arrived, we had already been waiting for two hours.", lemma="haber:nosotros:impf"),
        F("Ella ha estado ___ un trabajo desde marzo.", "buscando", ["buscado", "busca", "buscar"], "Gerund.", tr="She has been looking for a job since March.", lemma="buscar:ger"),
        F("Lo han estado ___ durante semanas.", "discutiendo", ["discutido", "discuten", "discutir"], "Gerund.", tr="They have been discussing it for weeks.", lemma="discutir:ger"),
    ],
    verify=(vpa("estar", "estado")),
)

# ---------------------------------------------------------------------------- 803
L803 = lesson(
    "The present perfect subjunctive: espero que hayas llegado",
    "Me alegra que hayan aprobado la ley. Espero que hayas llegado bien.",
    requires=["haber", "esperar", "alegrar", "dudar", "creer", "llegar", "aprobar", "terminar", "ver", "ley", "viaje", "problema"],
    cards=[
        card("Haya + participle",
             "The present perfect subjunctive is haber in the present subjunctive (haya, hayas, haya, hayamos, hayáis, hayan) + a past participle. "
             "Use it when a trigger for the subjunctive (emotion, doubt, hope, denial) is followed by something that has already happened.",
             tables=[table(["Persona", "haber (subjuntivo)", "Ejemplo"],
                           [["yo", "haya", "Espero que yo haya entendido."], ["tú", "hayas", "Espero que hayas llegado bien."],
                            ["él / ella / usted", "haya", "Dudo que ella haya terminado."], ["nosotros", "hayamos", "Es bueno que hayamos hablado."],
                            ["vosotros", "hayáis", "Me alegra que hayáis venido."], ["ellos / ustedes", "hayan", "Me alegra que hayan aprobado la ley."]],
                           say=[1, 2])]),
        card("English speakers",
             "In English you often use the simple past in these sentences (“I hope you arrived safely”). In Spanish, the completed action is usually expressed with the present perfect subjunctive: Espero que hayas llegado bien. "
             "The main verb is in the present, in the future, or a command.",
             examples=[
                 ex("Espero que hayas llegado bien.", "I hope you arrived safely.", "hayas llegado"),
                 ex("Me alegra que hayan aprobado la ley.", "I am glad that they have approved the law.", "hayan aprobado"),
                 ex("Dudo que ella haya terminado.", "I doubt that she has finished.", "haya terminado"),
             ]),
    ],
    exercises=[
        M("How is the present perfect subjunctive formed?", "haya, hayas, haya… + past participle", ["he, has, ha… + participle", "hubiera + participle", "habría + participle"], "Haya + participle."),
        M("When do we use it?", "After a trigger, when the action is already completed", ["After si, always", "Only in the future", "Only in commands"], "Trigger + completed action."),
        M("How would you say “I hope you arrived safely”?", "Espero que hayas llegado bien.", ["Espero que has llegado bien.", "Espero que llegaste bien.", "Espero que habrás llegado bien."], "Subjunctive."),
        F("Espero que tú ___ llegado bien.", "hayas", ["has", "haya", "hayáis"], "Tú → hayas.", tr="I hope you have arrived safely.", lemma="haber:tú:subj"),
        F("Me alegra que ellos ___ aprobado la ley.", "hayan", ["han", "haya", "hemos"], "Ellos → hayan.", tr="I am glad that they have approved the law.", lemma="haber:ellos:subj"),
        F("Dudo que ella ___ terminado todavía.", "haya", ["ha", "hayas", "hayan"], "Ella → haya.", tr="I doubt that she has finished yet.", lemma="haber:ella:subj"),
        F("Es bueno que nosotros ___ hablado.", "hayamos", ["hemos", "haya", "hayan"], "Nosotros → hayamos.", tr="It is good that we have talked.", lemma="haber:nosotros:subj"),
        F("Me alegra que vosotros ___ venido.", "hayáis", ["habéis", "hayan", "hayas"], "Vosotros → hayáis.", tr="I am glad that you (pl.) have come.", lemma="haber:vosotros:subj"),
        F("Espero que ellos no hayan ___ ningún problema.", "visto", ["ver", "viendo", "veído"], "Participle of ver.", tr="I hope they have not seen any problem.", lemma="ver:part"),
    ],
    verify=vpj("haber", "haya", "hayas", "haya", "hayamos", "hayáis", "hayan"),
)

# ---------------------------------------------------------------------------- 804
L804 = lesson(
    "Present perfect subjunctive after cuando, en cuanto, hasta que",
    "Te llamaré en cuanto haya terminado. Cuando hayas llegado a la esquina, dobla a la derecha.",
    requires=["cuando", "terminar", "llegar", "esquina", "llamar", "salir", "firmar", "informe", "reunión", "después", "hasta", "mañana"],
    cards=[
        card("Completed before another future moment",
             "After time words like cuando, en cuanto, tan pronto como, después de que and hasta que, use the subjunctive when the action has not happened yet. "
             "When you want to stress that it will be completed first, use haya + participle. The main verb is future, a command, or a similar reference to the future.",
             tables=[table(["Frase principal", "Palabra de tiempo + haya + participio"],
                           [["Te llamaré", "en cuanto haya terminado."],
                            ["Saldremos", "tan pronto como hayamos firmado el informe."],
                            ["No saldré", "hasta que hayan terminado la reunión."],
                            ["Dobla a la derecha", "cuando hayas llegado a la esquina."]],
                           say=[0, 1])]),
        card("Past or future?",
             "Compare: Cuando llegué, llamé (past, indicative). Cuando haya llegado, llamaré (future, subjunctive). In many sentences, the simple present subjunctive is also possible: Te llamaré en cuanto termine.",
             examples=[
                 ex("Te llamaré en cuanto haya terminado.", "I will call you as soon as I have finished.", "haya terminado"),
                 ex("No saldré hasta que hayan terminado la reunión.", "I will not leave until they have finished the meeting.", "hayan terminado"),
             ]),
    ],
    exercises=[
        M("Which sentence is about the future?", "Te llamaré en cuanto haya terminado.", ["Te llamé en cuanto terminé.", "Te llamaba en cuanto terminaba.", "Te llamó en cuanto terminó."], "Future + subjunctive."),
        M("Which form follows “en cuanto” when the action has not yet happened?", "The subjunctive", ["The conditional", "The preterite", "The imperfect"], "Subjunctive."),
        M("Which sentence is an instruction?", "Cuando hayas llegado a la esquina, dobla a la derecha.", ["Cuando llegué a la esquina, doblé.", "Cuando llego, doblo.", "Cuando llegaba, doblaba."], "Command."),
        F("Mañana, en cuanto ___ terminado el informe, te lo envío.", "haya", ["he", "ha", "había"], "Not yet happened → subjunctive.", tr="Tomorrow, as soon as I have finished the report, I will send it to you.", lemma="haber:yo:subj"),
        F("No saldremos hasta que ellos ___ firmado el documento.", "hayan", ["han", "habían", "hubieron"], "Future → subjunctive.", tr="We will not leave until they have signed the document.", lemma="haber:ellos:subj"),
        F("Cuando ___ llegado a la esquina, dobla a la derecha.", "hayas", ["has", "habías", "hubieras"], "Instruction → subjunctive.", tr="When you have reached the corner, turn right.", lemma="haber:tú:subj"),
        F("Hablaremos después de que ellos ___ comido.", "hayan", ["han", "habían", "hubieron"], "Future → subjunctive.", tr="We will talk after they have eaten.", lemma="haber:ellos:subj"),
        F("Tan pronto como nosotros ___ visto los resultados, te llamaremos.", "hayamos", ["hemos", "habíamos", "hubiéramos"], "Future → subjunctive.", tr="As soon as we have seen the results, we will call you.", lemma="haber:nosotros:subj"),
        F("Ayer, cuando ___ el informe, lo envié.", "terminé", ["haya terminado", "terminara", "terminaré"], "Past event → preterite indicative.", tr="Yesterday, when I finished the report, I sent it.", lemma="terminar:yo:pret"),
    ],
)

# ---------------------------------------------------------------------------- 805
L805 = lesson(
    "Doubt and probability about the past: dudo que haya, es posible que hayan",
    "Dudo que el tren haya salido. Es posible que ya hayan firmado el acuerdo.",
    requires=["dudar", "creer", "pensar", "posible", "probable", "quizás", "tren", "salir", "firmar", "acuerdo", "ya", "ojalá"],
    cards=[
        card("Not sure about the past",
             "To doubt or to guess about something that may have already happened, use a trigger + que + haya + participle.",
             tables=[table(["Expresión", "Ejemplo"],
                           [["dudo que + haya…", "Dudo que el tren haya salido."],
                            ["no creo que + haya…", "No creo que ellos hayan firmado."],
                            ["es posible que + haya…", "Es posible que ya hayan firmado el acuerdo."],
                            ["es probable que + haya…", "Es probable que haya llovido en la noche."],
                            ["puede que + haya…", "Puede que ella haya salido."],
                            ["quizás, tal vez + haya…", "Quizás haya perdido las llaves. (The indicative is also possible when you feel more sure.)"],
                            ["ojalá + haya…", "Ojalá hayan llegado bien."]],
                           say=[1])]),
        card("Subjunctive or indicative?",
             "Use the subjunctive after doubt: Dudo que haya salido. Use the indicative after belief or certainty: Creo que ha salido. With no creo que, the subjunctive returns.",
             examples=[
                 ex("Creo que ha salido.", "I think he has left.", "ha salido"),
                 ex("No creo que haya salido.", "I do not think he has left.", "haya salido"),
             ]),
    ],
    exercises=[
        M("Which sentence expresses doubt?", "Dudo que el tren haya salido.", ["Sé que el tren ha salido.", "Veo que el tren ha salido.", "Creo que el tren ha salido."], "Dudar + subjunctive."),
        M("Which trigger takes the indicative here?", "Creo que…", ["No creo que…", "Dudo que…", "Es posible que…"], "Creer (affirmative) → indicative."),
        M("What does “Ojalá hayan llegado bien” express?", "A hope that they arrived safely", ["A certainty", "A command", "A question"], "Ojalá."),
        F("Dudo que el tren ___ salido.", "haya", ["ha", "había", "hubo"], "Doubt → subjunctive.", tr="I doubt that the train has left.", lemma="haber:él:subj"),
        F("Es posible que ellos ya ___ firmado el acuerdo.", "hayan", ["han", "habían", "habrían"], "Es posible que → subjunctive.", tr="It is possible that they have already signed the agreement.", lemma="haber:ellos:subj"),
        F("No creo que ella ___ perdido las llaves.", "haya", ["ha", "hayas", "había"], "No creo que → subjunctive.", tr="I do not think she has lost the keys.", lemma="haber:ella:subj"),
        F("Quizás nosotros ___ olvidado algo.", "hayamos", ["hayan", "habíamos", "habremos"], "Quizás + subjunctive.", tr="Maybe we have forgotten something.", lemma="haber:nosotros:subj"),
        F("Creo que ella ya ___ salido.", "ha", ["haya", "hayan", "hayas"], "Creo que → indicative.", tr="I think she has already left.", lemma="haber:ella"),
        F("Ojalá ellos ___ llegado bien.", "hayan", ["han", "habían", "habrán"], "Ojalá + subjunctive.", tr="I hope they have arrived safely.", lemma="haber:ellos:subj"),
    ],
)

# ---------------------------------------------------------------------------- 806
L806 = lesson(
    "Perfect indicative or perfect subjunctive?",
    "Sé que has llegado. Me alegra que hayas llegado. No creo que haya llegado.",
    requires=["saber", "creer", "dudar", "alegrar", "seguro", "verdad", "cierto", "posible", "llegar", "ganar", "firmar", "equipo"],
    cards=[
        card("Choosing the mood",
             "Choose the indicative (he, has, ha…) after expressions of knowledge, belief, certainty, or report. Choose the subjunctive (haya, hayas…) after emotion, doubt, denial, possibility or hope.",
             tables=[table(["Indicativo (hecho o certeza)", "Subjuntivo (emoción, duda, posibilidad)"],
                           [["Sé que has llegado.", "Me alegra que hayas llegado."],
                            ["Es verdad que han ganado.", "Es posible que hayan ganado."],
                            ["Estoy seguro de que han firmado.", "Dudo que hayan firmado."],
                            ["Creo que ha salido.", "No creo que haya salido."],
                            ["Es cierto que hemos terminado.", "No es cierto que hayamos terminado."]],
                           say=[0, 1])]),
    ],
    exercises=[
        M("Which pair is correct?", "Estoy seguro de que han firmado. / Dudo que hayan firmado.", ["Estoy seguro de que hayan firmado. / Dudo que han firmado.", "Estoy seguro de que hayan firmado. / Dudo que hayan firmado.", "Estoy seguro de que han firmado. / Dudo que han firmado."], "Seguro → indicative; duda → subjunctive."),
        M("Which sentence is correct?", "No creo que haya salido.", ["No creo que ha salido.", "No creo que había salido.", "No creo que hubo salido."], "No creo que → subjunctive."),
        M("Which sentence shows certainty?", "Es verdad que han ganado.", ["Es posible que hayan ganado.", "Dudo que hayan ganado.", "Ojalá hayan ganado."], "Verdad → indicative."),
        F("Es verdad que ellos ___ ganado el partido.", "han", ["hayan", "habían", "habrían"], "Truth → indicative.", tr="It is true that they have won the match.", lemma="haber:ellos"),
        F("Es posible que ellos ___ ganado el partido.", "hayan", ["han", "habían", "habrían"], "Possibility → subjunctive.", tr="It is possible that they have won the match.", lemma="haber:ellos:subj"),
        F("Sé que tú ___ llegado temprano.", "has", ["hayas", "habías", "hubieras"], "Knowledge → indicative.", tr="I know that you have arrived early.", lemma="haber:tú"),
        F("Me alegra que tú ___ llegado temprano.", "hayas", ["has", "habías", "hubieras"], "Emotion → subjunctive.", tr="I am glad that you have arrived early.", lemma="haber:tú:subj"),
        F("Es cierto que nosotros ___ terminado.", "hemos", ["hayamos", "habíamos", "hubiéramos"], "Certainty → indicative.", tr="It is certain that we have finished.", lemma="haber:nosotros"),
        F("No es cierto que nosotros ___ terminado.", "hayamos", ["hemos", "habíamos", "hubiéramos"], "Denial → subjunctive.", tr="It is not true that we have finished.", lemma="haber:nosotros:subj"),
    ],
)

# ---------------------------------------------------------------------------- 807
L807 = lesson(
    "Reading: a town meeting about water (invented)",
    "Los vecinos han estado preocupados por el agua durante meses.",
    requires=["agua", "vecino", "alcalde", "técnico", "reunión", "estudio", "resultado", "problema", "promesa", "cumplir", "buscar", "causa"],
    cards=[
        card("An invented story",
             "This short text is invented for practice. It does not describe a real place. Notice the perfect tenses: han estado preocupados, había prometido, no ha publicado, haya cumplido, hayan encontrado, hayan terminado.",
             examples=[
                 ex("En el pueblo, los vecinos han estado preocupados por el agua durante meses.", "In the town, the neighbors have been worried about the water for months.", "han estado preocupados"),
                 ex("El alcalde había prometido una solución antes de las elecciones.", "The mayor had promised a solution before the elections.", "había prometido"),
                 ex("Hasta ahora, la oficina del agua no ha publicado los resultados de sus estudios.", "So far, the water office has not published the results of its studies.", "no ha publicado"),
                 ex("Algunos vecinos dudan que el alcalde haya cumplido sus promesas.", "Some neighbors doubt that the mayor has kept his promises.", "haya cumplido"),
                 ex("Otros creen que ha trabajado mucho y que los problemas no han sido causados por él.", "Others believe that he has worked a lot and that the problems have not been caused by him.", "han sido causados"),
                 ex("Los vecinos han estado hablando con los técnicos y esperan que hayan encontrado una causa.", "The neighbors have been talking with the technicians and hope that they have found a cause.", "hayan encontrado"),
                 ex("Cuando los técnicos hayan terminado el informe, habrá una reunión pública.", "When the technicians have finished the report, there will be a public meeting.", "hayan terminado"),
             ]),
    ],
    exercises=[
        M("How long have the neighbors been worried?", "For months", ["For a day", "For a hundred years", "Since yesterday only"], "Durante meses."),
        M("What had the mayor done before the elections?", "Promised a solution", ["Closed the water office", "Resigned", "Written the report"], "Había prometido."),
        M("What will happen after the technicians finish the report?", "There will be a public meeting", ["The mayor will resign", "The town will close", "Nothing"], "Habrá una reunión."),
        F("Los vecinos ___ estado preocupados por el agua durante meses.", "han", ["hayan", "habían", "habrán"], "Present perfect, plural.", tr="The neighbors have been worried about the water for months.", lemma="haber:ellos"),
        F("El alcalde ___ prometido una solución antes de las elecciones.", "había", ["ha", "haya", "habrá"], "Before another past moment.", tr="The mayor had promised a solution before the elections.", lemma="haber:él:impf"),
        F("La oficina del agua no ___ publicado los resultados.", "ha", ["haya", "había", "hayan"], "Present perfect, singular.", tr="The water office has not published the results.", lemma="haber:él"),
        F("Algunos vecinos dudan que el alcalde ___ cumplido sus promesas.", "haya", ["ha", "había", "habrá"], "Doubt → subjunctive.", tr="Some neighbors doubt that the mayor has kept his promises.", lemma="haber:él:subj"),
        F("Los vecinos esperan que los técnicos ___ encontrado una causa.", "hayan", ["han", "habían", "habrán"], "Hope → subjunctive.", tr="The neighbors hope that the technicians have found a cause.", lemma="haber:ellos:subj"),
        F("Cuando los técnicos ___ terminado el informe, habrá una reunión.", "hayan", ["han", "habían", "habrán"], "Future moment → subjunctive.", tr="When the technicians have finished the report, there will be a meeting.", lemma="haber:ellos:subj"),
    ],
)
UNIT = unit("Tendencias políticas", [L781, L782, L783, L784, L785, L786, L787, L788, L789, L790, L791, L792, L793, L794, L795, L796, L797, L798, L799, L800, L801, L802, L803, L804, L805, L806, L807])

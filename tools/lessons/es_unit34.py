"""Unit 34: human rights (textbook Chapter 34): rights vocabulary, freedom of expression, labor and Indigenous rights, memory of the Argentine dictatorship; the conditional; si-clauses; review of adjectival and adverbial clauses."""
from dsl_es import *

# ---------------------------------------------------------------------------- 715
L715 = lesson(
    "Human rights: the basic words",
    "Los derechos humanos pertenecen a todas las personas por igual.",
    requires=["derecho", "humano", "libertad", "expresión", "prensa", "voto", "igualdad", "dignidad", "activista", "organización", "declaración", "universal"],
    cards=[
        card("Core vocabulary",
             "Human rights are the basic rights that every person has because he or she is a human being. In nineteen forty-eight, the United Nations (las Naciones Unidas) approved the Universal Declaration of Human Rights. "
             "Many countries have written these rights into their own laws.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["los derechos humanos", "human rights", "Los derechos humanos pertenecen a todas las personas."],
                            ["la libertad de expresión", "freedom of expression", "La libertad de expresión permite decir lo que pensamos."],
                            ["la libertad de prensa", "freedom of the press", "La libertad de prensa protege el trabajo de los periodistas."],
                            ["el derecho al voto", "the right to vote", "El derecho al voto permite elegir a los gobernantes."],
                            ["la igualdad", "equality", "La igualdad significa los mismos derechos para todos."],
                            ["la dignidad", "dignity", "Todas las personas merecen vivir con dignidad."],
                            ["el activista, la activista", "activist", "Una activista defiende los derechos de otras personas."],
                            ["la organización", "organization", "Una organización internacional publica informes."],
                            ["la declaración", "declaration", "La declaración fue aprobada hace muchos años."]],
                           say=[2])]),
    ],
    exercises=[
        M("Who has human rights?", "Every person, because he or she is human", ["Only citizens", "Only adults", "Only rich people"], "Todas las personas por igual."),
        M("What does “la libertad de prensa” protect?", "The work of journalists", ["The price of newspapers", "The weather", "The tax system"], "Libertad de prensa."),
        F("El derecho al ___ permite elegir a los gobernantes.", "voto", ["trabajo", "salario", "viaje"], "Right to vote.", tr="The right to vote allows people to choose their rulers."),
        F("La ___ de expresión permite decir lo que pensamos.", "libertad", ["declaración", "igualdad", "dignidad"], "Freedom of expression.", tr="Freedom of expression allows us to say what we think."),
        F("La ___ significa los mismos derechos para todos.", "igualdad", ["libertad", "prensa", "organización"], "Equality.", tr="Equality means the same rights for everyone."),
        F("Una ___ defiende los derechos de otras personas.", "activista", ["declaración", "dignidad", "elección"], "Activist.", tr="An activist defends the rights of other people."),
        F("Todas las personas merecen vivir con ___.", "dignidad", ["prensa", "organización", "declaración"], "Dignity.", tr="All people deserve to live with dignity."),
        M("What did the United Nations approve in 1948?", "The Universal Declaration of Human Rights", ["A trade treaty", "A new currency", "A peace in Europe"], "La Declaración Universal de los Derechos Humanos."),
        M("Which word means “equality”?", "la igualdad", ["la libertad", "la prensa", "el voto"], "Igualdad."),
    ],
)

# ---------------------------------------------------------------------------- 716
L716 = lesson(
    "Violations of rights: censorship, repression, discrimination (definitions)",
    "La censura limita lo que las personas pueden decir o publicar.",
    requires=["censura", "represión", "detención", "desaparición", "tortura", "discriminación", "acoso", "pena", "muerte", "crimen", "humanidad", "víctima"],
    cards=[
        card("Naming the problem",
             "This lesson gives short definitions of words used in news reports and reports by human-rights organizations. "
             "Accusations of violations are often investigated by courts and independent bodies, and accused governments frequently reject them, so reports usually say who makes the accusation.",
             tables=[table(["Español", "English", "Definición"],
                           [["la censura", "censorship", "Limitar lo que se puede decir o publicar."],
                            ["la represión", "repression", "Usar la fuerza para controlar a las personas que protestan o piensan diferente."],
                            ["la detención arbitraria", "arbitrary detention", "Arrestar a una persona sin una razón legal."],
                            ["la tortura", "torture", "Causar dolor a una persona para castigarla o para obtener información."],
                            ["la desaparición forzada", "enforced disappearance", "Cuando agentes del Estado detienen a una persona y ocultan dónde está."],
                            ["la discriminación", "discrimination", "Tratar peor a una persona por su origen, religión, sexo u otra razón."],
                            ["el acoso", "harassment", "Molestar a una persona de manera repetida."],
                            ["la pena de muerte", "death penalty", "Un castigo legal con la muerte; muchos países la abolieron y otros la mantienen."],
                            ["el crimen de lesa humanidad", "crime against humanity", "Un crimen muy grave cometido como parte de un ataque generalizado o sistemático contra la población civil."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “la censura”?", "Limiting what can be said or published", ["Counting votes", "Paying taxes", "A school exam"], "Censura."),
        M("What is “la detención arbitraria”?", "Arresting a person without a legal reason", ["A traffic ticket", "A legal trial", "A visit to a museum"], "Arbitraria = without legal basis."),
        M("What is “la desaparición forzada”?", "State agents arresting a person and hiding where he or she is", ["A person who moves", "A trip", "A game"], "Forzada = enforced."),
        F("La ___ limita lo que las personas pueden decir o publicar.", "censura", ["igualdad", "elección", "libertad"], "Censorship.", tr="Censorship limits what people can say or publish."),
        F("La ___ consiste en tratar peor a una persona por su origen o religión.", "discriminación", ["libertad", "dignidad", "elección"], "Discrimination.", tr="Discrimination consists of treating a person worse because of origin or religion."),
        F("Muchos países ya abolieron la pena de ___.", "muerte", ["censura", "voto", "prensa"], "Death penalty.", tr="Many countries have already abolished the death penalty."),
        F("Los gobiernos acusados suelen ___ las acusaciones.", "rechazar", ["rechazan", "rechazo", "rechazado"], "Soler + infinitive: suelen rechazar.", tr="Accused governments often reject the accusations."),
        M("Why do reports say who makes an accusation?", "Because accused governments often reject it and courts investigate", ["Because accusations are always false", "Because accusations are always true", "To make the report longer"], "Attribution."),
        M("Which is NOT a definition from the lesson?", "La libertad de elegir un color", ["La censura", "La represión", "El acoso"], "Not a violation."),
    ],
)

# ---------------------------------------------------------------------------- 717
L717 = lesson(
    "Power and politics: dictadura, democracia, golpe de Estado, régimen, elecciones",
    "En una democracia, los ciudadanos eligen a sus gobernantes en elecciones libres.",
    requires=["dictadura", "democracia", "golpe", "militar", "régimen", "elección", "tribunal", "político", "preso", "libertad", "ciudadano", "gobierno"],
    cards=[
        card("Words about how a country is governed",
             "These words describe ways of governing and ways of changing governments. They are used in history books and in the news.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la democracia", "democracy", "En una democracia, los ciudadanos eligen a sus gobernantes."],
                            ["la dictadura", "dictatorship", "En una dictadura, el poder está en manos de una persona o de un grupo."],
                            ["el golpe de Estado", "coup d’état", "Un golpe de Estado cambia el gobierno por la fuerza."],
                            ["el régimen", "regime", "Un régimen puede ser democrático o autoritario."],
                            ["las elecciones libres", "free elections", "Las elecciones libres permiten votar sin miedo."],
                            ["el tribunal", "court", "Un tribunal independiente decide según la ley."],
                            ["el preso político, la presa política", "political prisoner", "Un preso político está encarcelado por sus ideas."],
                            ["la oposición", "the opposition", "La oposición critica al gobierno."],
                            ["la constitución", "constitution", "La constitución organiza el poder y protege los derechos."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is a coup d’état?", "Changing the government by force", ["A free election", "A court sentence", "A national holiday"], "Golpe de Estado."),
        M("In a democracy, who chooses the rulers?", "The citizens, in elections", ["The military", "Foreign countries", "Judges only"], "Los ciudadanos eligen."),
        F("En una ___, el poder está en manos de una persona o de un grupo.", "dictadura", ["democracia", "elección", "oposición"], "Dictatorship.", tr="In a dictatorship, the power is in the hands of one person or a group."),
        F("Un ___ de Estado cambia el gobierno por la fuerza.", "golpe", ["voto", "tribunal", "régimen"], "Coup.", tr="A coup d’état changes the government by force."),
        F("Un ___ independiente decide según la ley.", "tribunal", ["golpe", "régimen", "preso"], "Court.", tr="An independent court decides according to the law."),
        F("Un preso ___ está encarcelado por sus ideas.", "político", ["libre", "militar", "culpable"], "Political prisoner.", tr="A political prisoner is jailed for his or her ideas."),
        F("Las elecciones ___ permiten votar sin miedo.", "libres", ["militares", "presas", "arbitrarias"], "Free elections.", tr="Free elections allow people to vote without fear."),
        M("What does “la oposición” do?", "It criticizes the government", ["It writes the laws alone", "It collects taxes", "It rules by force"], "Oposición."),
        M("Which word names the main law of a country?", "la constitución", ["la dictadura", "el golpe", "el régimen"], "Constitución."),
    ],
)

# ---------------------------------------------------------------------------- 718
L718 = lesson(
    "Rights at work and inclusion: sindicato, huelga, salario mínimo, discapacidad, paridad",
    "Un sindicato defiende los derechos de los trabajadores.",
    requires=["sindicato", "huelga", "salario", "mínimo", "jornada", "trabajador", "discapacidad", "igualdad", "mujer", "escuela", "derecho", "tribunal"],
    cards=[
        card("Vocabulary of rights at work and in society",
             "Rights at work include fair pay, a safe workplace, limits on working hours and the right to organize. Inclusion means making a place usable and welcoming for everyone, including people with disabilities.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el sindicato", "labor union", "Un sindicato defiende los derechos de los trabajadores."],
                            ["la huelga", "strike", "La huelga es una forma legal de protesta en muchos países."],
                            ["el salario mínimo", "minimum wage", "El salario mínimo es el pago más bajo permitido por la ley."],
                            ["la jornada de trabajo", "workday", "La ley limita la jornada de trabajo."],
                            ["la discapacidad", "disability", "Una persona con discapacidad tiene los mismos derechos."],
                            ["la inclusión", "inclusion", "La inclusión permite que todos participen."],
                            ["la paridad", "parity: equal numbers of women and men", "La paridad pide el mismo número de mujeres y hombres en las listas."],
                            ["el empoderamiento", "empowerment", "El empoderamiento da más poder de decisión a las personas."]],
                           say=[2])]),
    ],
    exercises=[
        M("What does a union do?", "It defends workers’ rights", ["It sets the weather", "It prints money", "It teaches cooking"], "Sindicato."),
        M("What is “el salario mínimo”?", "The lowest pay allowed by law", ["The highest pay", "A bonus", "A tax"], "Mínimo."),
        F("La ___ es una forma legal de protesta en muchos países.", "huelga", ["jornada", "paridad", "declaración"], "Strike.", tr="The strike is a legal form of protest in many countries."),
        F("Una persona con ___ tiene los mismos derechos que las demás.", "discapacidad", ["huelga", "jornada", "paridad"], "Disability.", tr="A person with a disability has the same rights as everyone else."),
        F("La ley limita la ___ de trabajo.", "jornada", ["huelga", "paridad", "inclusión"], "Workday.", tr="The law limits the workday."),
        F("La ___ permite que todos participen.", "inclusión", ["huelga", "jornada", "paridad"], "Inclusion.", tr="Inclusion allows everyone to participate."),
        F("La ___ pide el mismo número de mujeres y hombres en las listas.", "paridad", ["huelga", "jornada", "discapacidad"], "Parity.", tr="Parity asks for the same number of women and men on the lists."),
        M("Which word is about giving more decision-making power to people?", "el empoderamiento", ["el salario", "el tribunal", "la jornada"], "Empoderamiento."),
        M("Which sentence is about school inclusion?", "Una escuela inclusiva tiene rampas y materiales para todos.", ["La escuela cierra los domingos.", "Los alumnos usan uniforme.", "El director viaja mucho."], "Inclusion."),
    ],
)

# ---------------------------------------------------------------------------- 719
L719 = lesson(
    "Verbs of rights and power: censurar, reprimir, acatar, culpar, divulgar, destacar",
    "El tribunal destaca que todos deben acatar la ley.",
    requires=["destacar", "culpar", "comprometer", "ejercer", "defender", "proteger", "castigar", "ley", "tribunal", "gobierno", "periodista", "información"],
    cards=[
        card("Verbs in context",
             "These verbs appear in reports about rights and justice. Most are regular. Some change spelling: divulgar (divulgue), destacar (destaque) and ejercer (yo ejerzo).",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["censurar", "to censor", "Algunos gobiernos censuran las noticias."],
                            ["reprimir", "to repress", "Un régimen puede reprimir las protestas."],
                            ["acatar", "to comply with, to abide by", "Todos deben acatar la ley."],
                            ["culpar", "to blame", "El gobierno culpa a la oposición."],
                            ["divulgar", "to spread information, to disclose", "Los periodistas divulgan información importante."],
                            ["destacar", "to highlight, to stand out", "El informe destaca tres problemas."],
                            ["ejercer", "to exercise (a right), to practice", "Los ciudadanos ejercen su derecho al voto."],
                            ["comprometerse a", "to commit to", "Los gobiernos se comprometen a proteger los derechos."]],
                           say=[2])]),
    ],
    exercises=[
        F("Algunos gobiernos ___ las noticias que no les gustan.", "censuran", ["censura", "censuramos", "censurar"], "Plural subject.", tr="Some governments censor the news they don’t like.", lemma="censurar:ellos"),
        F("Todos los ciudadanos deben ___ la ley.", "acatar", ["acata", "acatan", "acatamos"], "Deber + infinitive.", tr="All citizens must abide by the law."),
        F("El informe ___ tres problemas principales.", "destaca", ["destacan", "destacamos", "destacar"], "Singular subject.", tr="The report highlights three main problems.", lemma="destacar:él"),
        F("Los periodistas ___ información importante.", "divulgan", ["divulga", "divulgamos", "divulgar"], "Plural subject.", tr="Journalists spread important information.", lemma="divulgar:ellos"),
        F("Yo ___ información para que la gente sepa la verdad.", "divulgo", ["divulga", "divulgan", "divulgamos"], "First person singular.", tr="I spread information so that people know the truth.", lemma="divulgar:yo"),
        F("El gobierno ___ a la oposición de los problemas.", "culpa", ["culpan", "culpamos", "culpar"], "Singular subject.", tr="The government blames the opposition for the problems.", lemma="culpar:él"),
        F("Los ciudadanos ___ su derecho al voto en las elecciones.", "ejercen", ["ejerce", "ejercemos", "ejercer"], "Plural subject.", tr="Citizens exercise their right to vote in the elections."),
        M("What does “acatar la ley” mean?", "To comply with the law", ["To write the law", "To ignore the law", "To read the law aloud"], "Acatar."),
        M("What does “culpar” mean?", "To blame", ["To forgive", "To count", "To cook"], "Culpar."),
    ],
    verify=(vp("censurar", "censuro", "censuras", "censura", "censuramos", "censuráis", "censuran")
            + vp("culpar", "culpo", "culpas", "culpa", "culpamos", "culpáis", "culpan")
            + vp("destacar", "destaco", "destacas", "destaca", "destacamos", "destacáis", "destacan")
            + vp("divulgar", "divulgo", "divulgas", "divulga", "divulgamos", "divulgáis", "divulgan")),
)

# ---------------------------------------------------------------------------- 720
L720 = lesson(
    "Reading: freedom of expression and freedom of the press",
    "La libertad de expresión protege la voz de las personas; la libertad de prensa protege el trabajo de los periodistas.",
    requires=["libertad", "expresión", "prensa", "periodista", "periódico", "información", "noticia", "internet", "opinión", "ley", "gobierno", "límite"],
    cards=[
        card("Two related rights",
             "Freedom of expression is the right of every person to share opinions and information. Freedom of the press is the right of the media to investigate and publish without being controlled by the government. "
             "Both are protected by international law and by many constitutions, but countries limit them in different ways.",
             examples=[
                 ex("La libertad de expresión protege la voz de las personas.", "Freedom of expression protects people’s voices.", "voz"),
                 ex("La libertad de prensa protege el trabajo de los periodistas.", "Freedom of the press protects journalists’ work.", "periodistas"),
                 ex("Con internet, cualquier persona puede publicar una opinión.", "With the internet, anyone can publish an opinion.", "publicar"),
                 ex("Algunas organizaciones informan de que los periodistas reciben amenazas en varios países.", "Some organizations report that journalists receive threats in several countries.", "amenazas"),
                 ex("La mayoría de las leyes permite límites, por ejemplo, contra las amenazas o contra las mentiras que dañan a una persona.", "Most laws allow limits, for example against threats or against lies that harm a person.", "límites"),
                 ex("Las personas discuten dónde debe estar el límite entre la libertad de expresión y el daño a otros.", "People debate where the line between freedom of expression and harm to others should be.", "límite"),
                 ex("Algunos dicen que es mejor permitir casi todo y responder con más información; otros piden reglas más estrictas.", "Some say it is better to allow almost everything and respond with more information; others ask for stricter rules.", "reglas"),
             ]),
    ],
    exercises=[
        M("What does freedom of the press protect?", "The work of journalists", ["The price of paper", "Only television", "Weather reports"], "Libertad de prensa."),
        M("What does freedom of expression protect?", "People’s right to share opinions and information", ["Only famous people", "Only writers", "Only teachers"], "Libertad de expresión."),
        M("What do most laws allow?", "Some limits, for example against threats", ["No limits at all", "Only silence", "Only music"], "La mayoría de las leyes permite límites."),
        F("Con internet, cualquier persona puede ___ una opinión.", "publicar", ["publica", "publican", "publicado"], "Poder + infinitive.", tr="With the internet, anyone can publish an opinion."),
        F("Algunas organizaciones informan de que los periodistas ___ amenazas.", "reciben", ["recibe", "recibimos", "recibir"], "Plural subject.", tr="Some organizations report that journalists receive threats.", lemma="recibir:ellos"),
        F("Las personas ___ dónde debe estar el límite.", "discuten", ["discute", "discutimos", "discutir"], "Plural subject.", tr="People debate where the line should be.", lemma="discutir:ellos"),
        F("Algunos piden reglas más ___.", "estrictas", ["estricto", "estricta", "estrictos"], "Reglas is feminine plural.", tr="Some ask for stricter rules."),
        M("What is the debate described?", "Where the line between expression and harm to others should be", ["Whether newspapers exist", "Whether people can read", "Whether laws exist"], "El límite."),
        M("Which sentence reports one view?", "Es mejor permitir casi todo y responder con más información.", ["La libertad de prensa existe.", "Los periodistas escriben.", "Hay muchos periódicos."], "A view in the debate."),
    ],
    verify=vp("recibir", "recibo", "recibes", "recibe", "recibimos", "recibís", "reciben"),
)
from dsl_es import *

# ---------------------------------------------------------------------------- 721
L721 = lesson(
    "Reading: Indigenous peoples’ rights",
    "Los pueblos indígenas tienen cultura, lenguas y tradiciones propias.",
    requires=["indígena", "pueblo", "tierra", "lengua", "consulta", "territorio", "comunidad", "cultura", "tradición", "derecho", "respetar", "organización"],
    cards=[
        card("Land, language and consultation",
             "Indigenous peoples live in many parts of the world, including Latin America, where estimates speak of more than fifty million people. "
             "International documents, such as a United Nations declaration from two thousand seven, recognize their rights. This reading explains the main ideas; opinions about how to apply them differ.",
             examples=[
                 ex("Los pueblos indígenas tienen cultura, lenguas y tradiciones propias.", "Indigenous peoples have their own culture, languages and traditions.", "lenguas"),
                 ex("Una declaración de las Naciones Unidas reconoce sus derechos.", "A United Nations declaration recognizes their rights.", "reconoce"),
                 ex("Muchas comunidades piden que se respete su derecho a la tierra y al territorio.", "Many communities ask that their right to land and territory be respected.", "respete"),
                 ex("Antes de un proyecto grande en su territorio, las comunidades tienen derecho a una consulta previa.", "Before a big project on their territory, communities have the right to prior consultation.", "consulta previa"),
                 ex("Algunos gobiernos y empresas dicen que los proyectos traen trabajo; algunas comunidades responden que quieren decidir por sí mismas.", "Some governments and companies say that projects bring jobs; some communities answer that they want to decide for themselves.", "decidir"),
                 ex("Muchas lenguas indígenas corren peligro, en parte porque los niños aprenden otras lenguas en la escuela.", "Many Indigenous languages are in danger, partly because children learn other languages at school.", "corren peligro"),
                 ex("Hoy hay organizaciones que ayudan a conservar las lenguas.", "Today there are organizations that help preserve the languages.", "conservar"),
             ]),
    ],
    exercises=[
        M("What is “una consulta previa”?", "Asking the community before a big project on its territory", ["A school exam", "A doctor’s visit", "A tax payment"], "Consulta previa."),
        M("What did the United Nations declaration do?", "It recognized the rights of Indigenous peoples", ["It created a new language", "It closed borders", "It set prices"], "Reconoce sus derechos."),
        M("What do some communities answer to the argument that projects bring jobs?", "That they want to decide for themselves", ["That they do not want any water", "That they have no territory", "That they never speak"], "Quieren decidir por sí mismas."),
        F("Muchas comunidades piden que se ___ su derecho a la tierra.", "respete", ["respeta", "respetar", "respetan"], "Pedir que → subjunctive; singular derecho.", tr="Many communities ask that their right to land be respected.", lemma="respetar:él:subj"),
        F("Los pueblos indígenas ___ cultura propia.", "tienen", ["tiene", "tenemos", "tener"], "Plural subject.", tr="Indigenous peoples have their own culture.", lemma="tener:ellos"),
        F("Los niños ___ otras lenguas en la escuela.", "aprenden", ["aprende", "aprendemos", "aprender"], "Plural subject.", tr="The children learn other languages at school.", lemma="aprender:ellos"),
        F("Hoy hay organizaciones que ___ a conservar las lenguas.", "ayudan", ["ayuda", "ayudamos", "ayudar"], "Plural antecedent.", tr="Today there are organizations that help preserve the languages.", lemma="ayudar:ellos"),
        F("Algunas comunidades quieren ___ por sí mismas.", "decidir", ["decide", "deciden", "decidido"], "Querer + infinitive.", tr="Some communities want to decide for themselves."),
        F("Las comunidades tienen derecho a una ___ previa.", "consulta", ["consultar", "consultado", "consultan"], "A noun is needed after una.", tr="Communities have the right to a prior consultation."),
    ],
)

# ---------------------------------------------------------------------------- 722
L722 = lesson(
    "Reading: workers’ rights and Labor Day",
    "El primero de mayo se celebra el Día del Trabajo en muchos países.",
    requires=["trabajo", "trabajador", "sindicato", "salario", "contrato", "empleo", "descanso", "mínimo", "mayo", "fiesta", "derecho", "seguro"],
    cards=[
        card("Contracts, pay, rest",
             "In many countries, Labor Day (el Día del Trabajo, also called el Día Internacional de los Trabajadores) is on the first of May. In the United States it is celebrated in September. "
             "The day recalls the efforts of workers to get a shorter workday and better conditions.",
             examples=[
                 ex("El primero de mayo muchos países celebran el Día del Trabajo.", "On May first many countries celebrate Labor Day.", "celebran"),
                 ex("Los sindicatos defienden a los trabajadores.", "Unions defend workers.", "defienden"),
                 ex("Un trabajador con contrato tiene derecho a un día de descanso.", "A worker with a contract has the right to a day of rest.", "descanso"),
                 ex("Los sindicatos piden que el gobierno suba el salario mínimo.", "The unions ask that the government raise the minimum wage.", "suba"),
                 ex("En muchos países, una gran parte de los trabajadores tiene un empleo informal, sin contrato y sin seguro.", "In many countries, a large part of workers have informal jobs, without a contract and without insurance.", "informal"),
                 ex("Las personas con empleo informal a menudo no tienen los mismos derechos.", "People with informal jobs often do not have the same rights.", "informal"),
                 ex("Muchas personas piden que el salario sea suficiente para vivir.", "Many people ask that pay be enough to live on.", "sea"),
             ]),
    ],
    exercises=[
        M("When is Labor Day celebrated in many countries?", "On the first of May", ["On the first of January", "In September", "On Christmas"], "El primero de mayo."),
        M("What is “un empleo informal”?", "A job without a contract or insurance", ["A job in a bank", "A job with a long contract", "A government job"], "Sin contrato y sin seguro."),
        M("What do unions do?", "They defend workers", ["They set the weather", "They print money", "They teach cooking"], "Sindicatos."),
        F("El primero de mayo muchos países ___ el Día del Trabajo.", "celebran", ["celebra", "celebramos", "celebrar"], "Plural subject.", tr="On May first many countries celebrate Labor Day.", lemma="celebrar:ellos"),
        F("Los sindicatos ___ a los trabajadores.", "defienden", ["defiende", "defendemos", "defender"], "Plural subject.", tr="Unions defend workers.", lemma="defender:ellos"),
        F("Un trabajador con contrato ___ derecho a un día de descanso.", "tiene", ["tienen", "tenemos", "tener"], "Singular subject.", tr="A worker with a contract has the right to a day of rest.", lemma="tener:él"),
        F("Los sindicatos piden que el gobierno ___ el salario mínimo.", "suba", ["sube", "subir", "suben"], "Pedir que → subjunctive.", tr="The unions ask that the government raise the minimum wage.", lemma="subir:él:subj"),
        F("Muchas personas piden que el salario ___ suficiente para vivir.", "sea", ["es", "ser", "son"], "Pedir que → subjunctive.", tr="Many people ask that pay be enough to live on.", lemma="ser:él:subj"),
        F("Las personas con empleo informal a menudo no ___ los mismos derechos.", "tienen", ["tiene", "tenemos", "tener"], "Plural subject.", tr="People with informal jobs often do not have the same rights.", lemma="tener:ellos"),
    ],
)

# ---------------------------------------------------------------------------- 723
L723 = lesson(
    "Reading: disability rights and accessibility",
    "Un edificio accesible tiene rampas y ascensores.",
    requires=["discapacidad", "accesible", "ascensor", "edificio", "escuela", "ciego", "acceso", "derecho", "transporte", "buscar", "inclusión", "internet"],
    cards=[
        card("Access for everyone",
             "In Spanish today the respectful expression is “una persona con discapacidad” (a person with a disability). A United Nations convention from two thousand six protects the rights of these persons. "
             "Accessibility (la accesibilidad) means that buildings, transport, information and services can be used by everyone.",
             examples=[
                 ex("Una persona con discapacidad tiene los mismos derechos que las demás.", "A person with a disability has the same rights as everyone else.", "discapacidad"),
                 ex("Un edificio accesible tiene rampas y ascensores.", "An accessible building has ramps and elevators.", "accesible"),
                 ex("Muchas personas sordas usan la lengua de señas.", "Many deaf people use sign language.", "lengua de señas"),
                 ex("Las personas ciegas pueden leer en braille.", "Blind people can read in braille.", "braille"),
                 ex("Las páginas de internet también deben ser accesibles.", "Web pages must also be accessible.", "accesibles"),
                 ex("Buscamos una escuela que tenga ascensor.", "We are looking for a school that has an elevator.", "tenga"),
                 ex("No conozco ninguna escuela cerca que enseñe lengua de señas.", "I don’t know any nearby school that teaches sign language.", "enseñe"),
             ]),
    ],
    exercises=[
        M("Which expression is respectful today?", "una persona con discapacidad", ["una persona de color", "una persona sin nombre", "una persona de la calle"], "Persona con discapacidad."),
        M("What does an accessible building have?", "Ramps and elevators", ["Only stairs", "Only a roof", "Only a garden"], "Rampas y ascensores."),
        M("What is “la accesibilidad”?", "Making places, transport and information usable by everyone", ["Building very tall towers", "Teaching cooking", "A kind of tax"], "Accesibilidad."),
        F("Los edificios accesibles tienen rampas y ___.", "ascensores", ["ascensor", "ascensora", "ascensoras"], "Plural masculine.", tr="Accessible buildings have ramps and elevators."),
        F("Las páginas de internet deben ser ___.", "accesibles", ["accesible", "accesibla", "accesibes"], "Plural.", tr="Web pages must be accessible."),
        F("Buscamos una escuela que ___ ascensor.", "tenga", ["tienes", "tener", "tienen"], "Unknown school → subjunctive.", tr="We are looking for a school that has an elevator.", lemma="tener:ella:subj"),
        F("No conozco ninguna escuela que ___ lengua de señas.", "enseñe", ["enseña", "enseñar", "enseñan"], "Ninguna → subjunctive.", tr="I don’t know any school that teaches sign language.", lemma="enseñar:ella:subj"),
        F("Las personas ciegas ___ leer en braille.", "pueden", ["puede", "podemos", "poder"], "Plural subject.", tr="Blind people can read in braille.", lemma="poder:ellos"),
        F("Una persona con discapacidad ___ los mismos derechos que las demás.", "tiene", ["tienen", "tenemos", "tener"], "Singular subject.", tr="A person with a disability has the same rights as everyone else.", lemma="tener:él"),
    ],
)

# ---------------------------------------------------------------------------- 724
L724 = lesson(
    "Reading: hate crimes and how societies respond",
    "Un delito de odio es un delito contra una persona por pertenecer a un grupo.",
    requires=["odio", "delito", "violencia", "ataque", "denuncia", "grupo", "religión", "policía", "víctima", "ley", "proteger", "apoyo"],
    cards=[
        card("Naming and responding",
             "This reading gives the general idea without describing any attack. A hate crime (un delito de odio) is a crime against a person because of a characteristic of a group he or she belongs to. "
             "Not all countries use exactly the same definition, and legal systems differ.",
             examples=[
                 ex("Un delito de odio es un delito contra una persona por pertenecer a un grupo.", "A hate crime is a crime against a person for belonging to a group.", "odio"),
                 ex("El grupo puede definirse por el origen, la religión, la discapacidad u otra característica.", "The group can be defined by origin, religion, disability or another characteristic.", "religión"),
                 ex("Muchos países tienen leyes que imponen una pena más grave a estos delitos.", "Many countries have laws that impose a more serious penalty for these crimes.", "pena"),
                 ex("Según varias organizaciones, muchos ataques no se denuncian, por ejemplo, porque las víctimas tienen miedo.", "According to several organizations, many attacks are not reported, for example because the victims are afraid.", "denuncian"),
                 ex("Las organizaciones piden que la policía registre todos los casos.", "Organizations ask that the police record all cases.", "registre"),
                 ex("Es importante que las víctimas reciban apoyo.", "It is important that the victims receive support.", "reciban"),
                 ex("Las escuelas pueden enseñar a respetar las diferencias.", "Schools can teach people to respect differences.", "respetar"),
             ]),
    ],
    exercises=[
        M("What is “un delito de odio”?", "A crime against a person for belonging to a group", ["A crime in a bank", "A kind of party", "A traffic sign"], "Delito de odio."),
        M("According to some organizations, why are many attacks not reported?", "One reason is that the victims are afraid", ["Because there are no laws", "Because everyone is happy", "Because police do not exist"], "Tienen miedo."),
        M("What can schools do?", "Teach people to respect differences", ["Close all classes", "Ban reading", "Only teach sports"], "Respetar las diferencias."),
        F("Muchos países tienen leyes que imponen una ___ más grave a estos delitos.", "pena", ["castigar", "castigan", "castigado"], "A noun is needed.", tr="Many countries have laws that impose a more serious penalty for these crimes."),
        F("Las organizaciones piden que la policía ___ todos los casos.", "registre", ["registra", "registrar", "registran"], "Pedir que → subjunctive.", tr="Organizations ask that the police record all cases.", lemma="registrar:él:subj"),
        F("Es importante que las víctimas ___ apoyo.", "reciban", ["reciben", "recibir", "recibe"], "Es importante que → subjunctive.", tr="It is important that the victims receive support.", lemma="recibir:ellos:subj"),
        F("Muchas víctimas ___ miedo.", "tienen", ["tiene", "tenemos", "tener"], "Plural subject.", tr="Many victims are afraid.", lemma="tener:ellos"),
        F("Las leyes ___ a las personas de los ataques.", "protegen", ["protege", "protegemos", "proteger"], "Plural subject.", tr="Laws protect people from attacks.", lemma="proteger:ellos"),
        F("Las escuelas pueden enseñar a ___ las diferencias.", "respetar", ["respeta", "respetan", "respetado"], "Preposition + infinitive.", tr="Schools can teach people to respect differences."),
    ],
)

# ---------------------------------------------------------------------------- 725
L725 = lesson(
    "Reading: remembering the dictatorship in Argentina",
    "Las Madres y las Abuelas de Plaza de Mayo buscaron la verdad durante décadas.",
    requires=["dictadura", "militar", "gobierno", "golpe", "madre", "abuela", "nieto", "desaparecer", "informe", "memoria", "verdad", "justicia"],
    cards=[
        card("A national memory",
             "In nineteen seventy-six, a coup began a military government in Argentina that lasted until nineteen eighty-three. Human-rights organizations speak of about thirty thousand people who disappeared; an official report from nineteen eighty-four documented thousands of cases. "
             "This reading mentions organizations and public memory days, not individual people.",
             examples=[
                 ex("En mil novecientos setenta y seis, los militares tomaron el poder en Argentina.", "In 1976, the military took power in Argentina.", "tomaron"),
                 ex("El gobierno militar duró hasta mil novecientos ochenta y tres.", "The military government lasted until 1983.", "duró"),
                 ex("Durante esos años, miles de personas desaparecieron.", "During those years, thousands of people disappeared.", "desaparecieron"),
                 ex("Las familias buscaban a sus hijos y no recibían respuestas.", "Families looked for their children and did not receive answers.", "buscaban"),
                 ex("Un grupo de madres empezó a caminar cada semana en la Plaza de Mayo para preguntar por sus hijos.", "A group of mothers began to walk every week in the Plaza de Mayo to ask about their children.", "empezó"),
                 ex("Las Abuelas buscan a los nietos que nacieron durante esa época; más de cien personas ya recuperaron su identidad.", "The Grandmothers look for the grandchildren who were born during that period; more than a hundred people have already recovered their identity.", "recuperaron"),
                 ex("En mil novecientos ochenta y cuatro, un informe llamado «Nunca más» documentó miles de casos.", "In 1984, a report called “Never again” documented thousands of cases.", "documentó"),
                 ex("Hoy, el veinticuatro de marzo es el Día de la Memoria por la Verdad y la Justicia.", "Today, the twenty-fourth of March is the Day of Memory for Truth and Justice.", "Memoria"),
             ]),
    ],
    exercises=[
        M("How long did the military government last?", "From 1976 to 1983", ["From 1900 to 1910", "Only one week", "From 2000 to 2020"], "Hasta mil novecientos ochenta y tres."),
        M("What do the Abuelas de Plaza de Mayo look for?", "Grandchildren born during that period", ["New schools", "Old coins", "Mountain trails"], "Buscan a los nietos."),
        M("What is the twenty-fourth of March in Argentina?", "A day of memory for truth and justice", ["A sports day", "A harvest festival", "Tax day"], "Día de la Memoria."),
        F("En mil novecientos setenta y seis, los militares ___ el poder.", "tomaron", ["toman", "tomarán", "tomar"], "Preterite, plural.", tr="In 1976, the military took power.", lemma="tomar:ellos:pret"),
        F("El gobierno militar ___ hasta mil novecientos ochenta y tres.", "duró", ["duraba", "dura", "durar"], "Completed period → preterite.", tr="The military government lasted until 1983.", lemma="durar:él:pret"),
        F("Entre mil novecientos setenta y seis y mil novecientos ochenta y tres, miles de personas ___.", "desaparecieron", ["desaparecen", "desaparecía", "desaparecer"], "Plural preterite.", tr="Between 1976 and 1983, thousands of people disappeared.", lemma="desaparecer:ellos:pret"),
        F("Las familias ___ a sus hijos y no recibían respuestas.", "buscaban", ["buscan", "buscarán", "buscar"], "Repeated action in the past → imperfect.", tr="Families looked for their children and did not receive answers.", lemma="buscar:ellos:impf"),
        F("Un grupo de madres ___ a caminar cada semana en la plaza.", "empezó", ["empezaba", "empieza", "empezar"], "Beginning → preterite.", tr="A group of mothers began to walk every week in the plaza.", lemma="empezar:él:pret"),
        F("Más de cien personas ya ___ su identidad.", "recuperaron", ["recuperan", "recuperaban", "recuperar"], "Plural preterite.", tr="More than a hundred people have already recovered their identity.", lemma="recuperar:ellos:pret"),
    ],
)

# ---------------------------------------------------------------------------- 726
L726 = lesson(
    "Reading: truth, justice and reparation",
    "Después de un periodo de violencia, muchas sociedades buscan la verdad, la justicia y la reparación.",
    requires=["verdad", "justicia", "reparación", "víctima", "familia", "juicio", "juez", "investigar", "memoria", "museo", "ley", "comisión"],
    cards=[
        card("What societies try to do",
             "After dictatorships or armed conflicts, many countries try to deal with the past in several ways. Specialists often name four main goals: truth, justice, reparation and guarantees that it will not happen again. Many countries also add memory as a related goal. "
             "Countries combine them in different ways, and people disagree about the best balance.",
             examples=[
                 ex("La verdad: investigar qué pasó y publicar los resultados.", "Truth: investigating what happened and publishing the results.", "investigar"),
                 ex("La justicia: los tribunales juzgan a los responsables en un juicio justo.", "Justice: the courts judge those responsible in a fair trial.", "juicio justo"),
                 ex("La reparación: ayudar a las víctimas y a sus familias, por ejemplo con apoyo económico o psicológico.", "Reparation: helping the victims and their families, for example with economic or psychological support.", "reparación"),
                 ex("La memoria: museos, monumentos y días de recuerdo para que la sociedad no olvide.", "Memory: museums, monuments and days of remembrance so that society does not forget.", "olvide"),
                 ex("Las garantías de no repetición: reformas para que el pasado no vuelva a ocurrir.", "Guarantees of non-repetition: reforms so that the past does not happen again.", "vuelva a ocurrir"),
                 ex("Muchos países usaron comisiones de la verdad después de dictaduras o conflictos.", "Many countries used truth commissions after dictatorships or conflicts.", "comisiones"),
                 ex("Una comisión pregunta, escucha y publica un informe; no siempre es un tribunal.", "A commission asks, listens and publishes a report; it is not always a court.", "informe"),
                 ex("Hay debate sobre cómo equilibrar la justicia, el perdón y la paz.", "There is debate about how to balance justice, forgiveness and peace.", "debate"),
             ]),
    ],
    exercises=[
        M("What is “la verdad” as a goal?", "Investigating what happened and publishing the results", ["Closing all courts", "Building roads", "Printing money"], "La verdad."),
        M("What does a truth commission usually do?", "Asks, listens and publishes a report", ["Plays music", "Sells land", "Runs elections"], "Comisión de la verdad."),
        M("What is the debate described?", "How to balance justice, forgiveness and peace", ["Which color is best", "How to build a bridge", "How to cook rice"], "Equilibrar."),
        F("Los tribunales ___ a los responsables en un juicio justo.", "juzgan", ["juzga", "juzgamos", "juzgar"], "Plural subject.", tr="Courts judge those responsible in a fair trial.", lemma="juzgar:ellos"),
        F("Los museos ayudan a que la sociedad no ___.", "olvide", ["olvida", "olvidar", "olvidan"], "Para que / ayudar a que → subjunctive.", tr="Museums help society not to forget.", lemma="olvidar:él:subj"),
        F("Una comisión ___ y publica un informe.", "escucha", ["escuchan", "escuchamos", "escuchar"], "Singular subject.", tr="A commission listens and publishes a report.", lemma="escuchar:él"),
        F("Muchos países ___ comisiones de la verdad después de dictaduras.", "usaron", ["usan", "usarán", "usar"], "Plural preterite.", tr="Many countries used truth commissions after dictatorships.", lemma="usar:ellos:pret"),
        F("La reparación consiste en ___ a las víctimas y a sus familias.", "ayudar", ["ayuda", "ayudan", "ayudado"], "En + infinitive.", tr="Reparation consists of helping the victims and their families."),
        F("Hay reformas para que el pasado no ___ a ocurrir.", "vuelva", ["vuelve", "volver", "vuelven"], "Para que → subjunctive.", tr="There are reforms so that the past does not happen again.", lemma="volver:él:subj"),
    ],
)

# ---------------------------------------------------------------------------- 727
L727 = lesson(
    "Review: the conditional and its twelve irregular stems",
    "Yo diría la verdad. Ella podría venir. Nosotros haríamos el trabajo.",
    requires=["poder", "tener", "hacer", "decir", "venir", "salir", "poner", "saber", "querer", "haber", "valer", "caber"],
    cards=[
        card("Same endings, twelve special stems",
             "The conditional is formed with the infinitive (or a special stem) + the endings -ía, -ías, -ía, -íamos, -íais, -ían. "
             "Twelve verbs use a stem that is not the infinitive. These are the same stems as in the future tense.",
             tables=[table(["Infinitivo", "Raíz", "Ejemplo"],
                           [["caber", "cabr-", "En esa caja cabrían todos los libros."],
                            ["haber", "habr-", "Habría más trabajo con una fábrica nueva."],
                            ["poder", "podr-", "¿Podrías ayudarme?"],
                            ["querer", "querr-", "Querría hablar con el director."],
                            ["saber", "sabr-", "Yo no sabría qué decir."],
                            ["poner", "pondr-", "Yo pondría la mesa aquí."],
                            ["salir", "saldr-", "Saldríamos más temprano."],
                            ["tener", "tendr-", "Tendrías que descansar."],
                            ["valer", "valdr-", "No valdría la pena esperar."],
                            ["venir", "vendr-", "Dijeron que vendrían mañana."],
                            ["decir", "dir-", "Yo diría la verdad."],
                            ["hacer", "har-", "¿Qué haría usted?"]],
                           say=[2]),
                    table(["Persona", "tener", "decir", "hacer"],
                          [["yo", "tendría", "diría", "haría"],
                           ["tú", "tendrías", "dirías", "harías"],
                           ["él, ella, usted", "tendría", "diría", "haría"],
                           ["nosotros", "tendríamos", "diríamos", "haríamos"],
                           ["vosotros", "tendríais", "diríais", "haríais"],
                           ["ellos, ustedes", "tendrían", "dirían", "harían"]],
                          say=[1, 2, 3])]),
    ],
    exercises=[
        M("Which is the conditional of “salir” for yo?", "saldría", ["saliría", "salería", "salgaría"], "Stem saldr-."),
        M("Which verb has the conditional stem “har-”?", "hacer", ["haber", "hablar", "hallar"], "Hacer → haría."),
        M("What are the endings of the conditional?", "-ía, -ías, -ía, -íamos, -íais, -ían", ["-é, -ás, -á, -emos, -éis, -án", "-a, -as, -a, -amos, -áis, -an", "-aba, -abas, -aba, -ábamos, -abais, -aban"], "Conditional endings."),
        F("En tu lugar, yo le ___ la verdad.", "diría", ["decía", "dije", "decir"], "Hypothetical advice.", tr="In your place, I would tell him the truth.", lemma="decir:yo:cond"),
        F("¿___ usted abrir la ventana, por favor?", "Podría", ["Poder", "Pudo", "Pueda"], "Polite request.", tr="Could you open the window, please?", lemma="poder:usted:cond"),
        F("Mis amigos dijeron que ___ a las ocho.", "saldrían", ["salir", "salieron", "salimos"], "Future seen from the past.", tr="My friends said that they would leave at eight.", lemma="salir:ellos:cond"),
        F("Ellos dijeron que ___ mañana.", "vendrían", ["venir", "vinieron", "vinimos"], "Future seen from the past.", tr="They said that they would come tomorrow.", lemma="venir:ellos:cond"),
        F("¿Qué ___ tú en mi lugar?", "harías", ["hacer", "hiciste", "hagas"], "Hypothetical.", tr="What would you do in my place?", lemma="hacer:tú:cond"),
        F("Yo que tú, no ___ tanta prisa.", "tendría", ["tengo", "tuve", "tener"], "Advice with yo que tú.", tr="If I were you, I wouldn’t be in such a hurry.", lemma="tener:yo:cond"),
    ],
    verify=(vpd("tener", "tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían")
            + vpd("decir", "diría", "dirías", "diría", "diríamos", "diríais", "dirían")
            + vpd("hacer", "haría", "harías", "haría", "haríamos", "haríais", "harían")
            + vpd("poder", "podría", "podrías", "podría", "podríamos", "podríais", "podrían")
            + vpd("venir", "vendría", "vendrías", "vendría", "vendríamos", "vendríais", "vendrían")
            + vpd("salir", "saldría", "saldrías", "saldría", "saldríamos", "saldríais", "saldrían")
            + vpd("caber", "cabría") + vpd("haber", "habría") + vpd("querer", "querría")
            + vpd("saber", "sabría") + vpd("poner", "pondría") + vpd("valer", "valdría")),
)

# ---------------------------------------------------------------------------- 728
L728 = lesson(
    "Uses of the conditional: politeness, advice, reported future, guesses",
    "¿Podría decirme dónde está la estación? Dijo que llegaría a las seis.",
    requires=["poder", "hablar", "decir", "llegar", "prometer", "ayudar", "gustar", "viajar", "deber", "descansar", "ser", "salir"],
    cards=[
        card("Five jobs for one tense",
             "The conditional is used for: (1) polite requests; (2) advice; (3) a future seen from the past (reported speech); (4) wishes; (5) a guess about the past (probability).",
             tables=[table(["Uso", "Ejemplo"],
                           [["Polite request", "¿Podría decirme dónde está la estación?"],
                            ["Advice", "Yo que tú, hablaría con el jefe."],
                            ["Advice with deber", "Deberías descansar más."],
                            ["Future seen from the past", "Dijo que llegaría a las seis."],
                            ["Future seen from the past", "Prometieron que ayudarían a las familias."],
                            ["Wish", "Me gustaría viajar a Chile."],
                            ["Guess about the past", "Serían las tres cuando salimos."]],
                           say=[1])]),
    ],
    exercises=[
        M("What does “Dijo que llegaría a las seis” report?", "A future seen from the past", ["A present habit", "An order", "A completed past action"], "Reported future."),
        M("What does “Serían las tres cuando salimos” express?", "A guess about the past: it was probably about three", ["A promise", "An order", "A plan for tomorrow"], "Probability in the past."),
        M("Which sentence is the most polite request?", "¿Podría decirme dónde está la estación?", ["Dígame dónde está la estación ya.", "Dime dónde está la estación.", "Dónde está la estación, rápido."], "Conditional = polite."),
        F("Ayer dijo que hoy ___ a las seis.", "llegaría", ["llegó", "llegar", "llegaste"], "Future seen from the past.", tr="Yesterday he said that he would arrive at six today.", lemma="llegar:él:cond"),
        F("El año pasado prometieron que el año siguiente ___ a las familias.", "ayudarían", ["ayudaron", "ayudar", "ayudan"], "Reported future.", tr="Last year they promised that the following year they would help the families.", lemma="ayudar:ellos:cond"),
        F("No tengo dinero ahora, pero me ___ viajar a Chile algún día.", "gustaría", ["gustó", "gustar", "gustan"], "Wish.", tr="I have no money now, but I would like to travel to Chile some day.", lemma="gustar:él:cond"),
        F("Tú ___ descansar más; estás muy cansado.", "deberías", ["deber", "debí", "debimos"], "Advice.", tr="You should rest more; you are very tired.", lemma="deber:tú:cond"),
        F("Yo que tú, ___ con el jefe.", "hablaría", ["hablo", "hablé", "hablar"], "Advice.", tr="If I were you, I would talk to the boss.", lemma="hablar:yo:cond"),
        F("¿___ ustedes cerrar la puerta, por favor?", "Podrían", ["Poder", "Pudieron", "Puedan"], "Polite request.", tr="Could you (plural) close the door, please?", lemma="poder:ustedes:cond"),
    ],
    verify=(vpd("llegar", "llegaría", "llegarías", "llegaría", "llegaríamos", "llegaríais", "llegarían")
            + vpd("ayudar", "ayudaría", "ayudarías", "ayudaría", "ayudaríamos", "ayudaríais", "ayudarían")
            + vpd("deber", "debería", "deberías", "debería", "deberíamos", "deberíais", "deberían")),
)

# ---------------------------------------------------------------------------- 729
L729 = lesson(
    "If … would: si + imperfect subjunctive, conditional",
    "Si tuviera más tiempo, leería más. Si fuera rico, ayudaría a mi familia.",
    requires=["tener", "leer", "ser", "ayudar", "vivir", "ver", "poder", "hablar", "haber", "llegar", "construir", "tiempo"],
    cards=[
        card("Imaginary or unlikely situations",
             "To talk about something imaginary, unlikely or contrary to fact, use: si + imperfect subjunctive, … + conditional. "
             "The two parts can be in either order. Never use the conditional or the present subjunctive right after si in this pattern.",
             tables=[table(["Si + imperfect subjunctive", "Conditional"],
                           [["Si tuviera más tiempo,", "leería más."],
                            ["Si fuera rico,", "ayudaría a mi familia."],
                            ["Si viviéramos cerca,", "nos veríamos todos los días."],
                            ["Si ella pudiera,", "hablaría con todos."],
                            ["Si hubiera menos tráfico,", "llegaríamos antes."]],
                           say=[0, 1])],
             examples=[
                 ex("Si yo fuera tú, hablaría con el jefe.", "If I were you, I would talk to the boss.", "fuera"),
                 ex("Los vecinos estarían más contentos si el gobierno construyera una escuela.", "The neighbors would be happier if the government built a school.", "construyera"),
             ]),
    ],
    exercises=[
        M("Which sentence describes an imaginary situation?", "Si tuviera más tiempo, leería más.", ["Si tengo tiempo, leo.", "Cuando tengo tiempo, leo.", "Siempre que llueve, me quedo."], "Imperfect subjunctive + conditional."),
        M("Which form follows “si” in an imaginary situation?", "The imperfect subjunctive", ["The conditional", "The present subjunctive", "The future"], "Si + imperfect subjunctive."),
        M("Which sentence is correct?", "Si fuera rico, ayudaría a mi familia.", ["Si sería rico, ayudaría a mi familia.", "Si fuera rico, ayudaré a mi familia.", "Si fuera rico, ayudo a mi familia."], "Si + imperfect subjunctive, conditional."),
        F("Si yo ___ más tiempo, leería más.", "tuviera", ["tengo", "tendría", "tuve"], "Imaginary situation.", tr="If I had more time, I would read more.", lemma="tener:yo:isubj"),
        F("Si yo fuera rico, ___ a mi familia.", "ayudaría", ["ayudo", "ayudé", "ayudabas"], "Main clause = conditional.", tr="If I were rich, I would help my family.", lemma="ayudar:yo:cond"),
        F("Si nosotros ___ cerca, nos veríamos todos los días.", "viviéramos", ["vivimos", "viviríamos", "vivamos"], "Imaginary situation.", tr="If we lived nearby, we would see each other every day.", lemma="vivir:nosotros:isubj"),
        F("Si ella ___ hablar con todos, lo haría.", "pudiera", ["puede", "podría", "pudo"], "Imaginary situation.", tr="If she could talk to everyone, she would.", lemma="poder:ella:isubj"),
        F("Si hubiera menos tráfico, nosotros ___ antes.", "llegaríamos", ["llegamos", "llegarás", "llegaremos"], "Main clause = conditional.", tr="If there were less traffic, we would arrive earlier.", lemma="llegar:nosotros:cond"),
        F("Los vecinos estarían más contentos si el gobierno ___ una escuela.", "construyera", ["construye", "construiría", "construirá"], "Si + imperfect subjunctive.", tr="The neighbors would be happier if the government built a school.", lemma="construir:él:isubj"),
    ],
    verify=(vpq("vivir", "viviera", "vivieras", "viviera", "viviéramos", "vivierais", "vivieran")
            + vpq("tener", "tuviera", "tuvieras", "tuviera", "tuviéramos", "tuvierais", "tuvieran")
            + vpd("ver", "vería", "verías", "vería", "veríamos", "veríais", "verían")),
)

# ---------------------------------------------------------------------------- 730
L730 = lesson(
    "Real or unreal? Three kinds of si-clauses",
    "Si llueve, nos quedaremos. Si lloviera, nos quedaríamos. Si llovía, nos quedábamos.",
    requires=["llover", "quedar", "construir", "presidente", "tener", "venir", "estudiar", "pasar", "examen", "ser", "escuela", "hacer"],
    cards=[
        card("Choosing the tenses",
             "Spanish has three main patterns with si. (1) A real or likely situation: si + present indicative, followed by the present, the future or a command. "
             "(2) An imaginary or unlikely situation: si + imperfect subjunctive, followed by the conditional. "
             "(3) A habit in the past: si + imperfect indicative, followed by the imperfect.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["Real or likely", "Si llueve mañana, nos quedaremos en casa."],
                            ["Real: command", "Si tienes tiempo, ven a visitarme."],
                            ["Real: present", "Si estudias mucho, pasas el examen."],
                            ["Imaginary or unlikely", "Si lloviera mañana, nos quedaríamos en casa."],
                            ["Imaginary", "Si yo fuera presidente, construiría más escuelas."],
                            ["Habit in the past", "Cuando era niño, si llovía, nos quedábamos en casa."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which sentence is NOT correct Spanish?", "Si tendría dinero, viajaría.", ["Si tuviera dinero, viajaría.", "Si tengo dinero, viajo.", "Si tengo dinero, viajaré."], "Not conditional after si."),
        M("Which sentence describes a habit in the past?", "Si llovía, nos quedábamos en casa.", ["Si lloviera, nos quedaríamos en casa.", "Si llueve, nos quedaremos en casa.", "Si lloverá, nos quedamos en casa."], "Imperfect + imperfect."),
        M("Which form can follow “si” in a real, likely situation?", "The present indicative", ["The present subjunctive", "The future", "The conditional"], "Si tengo tiempo…"),
        F("Si llueve mañana, nos ___ en casa.", "quedaremos", ["quedaríamos", "quedáramos", "quedábamos"], "Likely future.", tr="If it rains tomorrow, we will stay at home.", lemma="quedar:nosotros:fut"),
        F("Si yo fuera presidente, ___ más escuelas.", "construiría", ["construyo", "construiré", "construyera"], "Imaginary situation.", tr="If I were president, I would build more schools.", lemma="construir:yo:cond"),
        F("Cuando era niño, si llovía, nos ___ en casa.", "quedábamos", ["quedaremos", "quedamos", "quedemos"], "Habit in the past.", tr="When I was a child, if it rained, we stayed at home.", lemma="quedar:nosotros:impf"),
        F("Si tienes tiempo, ___ a visitarme.", "ven", ["vengas", "viniera", "vendrías"], "Real situation → command.", tr="If you have time, come visit me.", lemma="venir:tú:tcmd"),
        F("Si estudias mucho, ___ el examen.", "pasarás", ["pasarías", "pasaste", "pasado"], "Likely result → future.", tr="If you study a lot, you will pass the exam.", lemma="pasar:tú:fut"),
        F("Si no hubiera libertad de prensa, ___ más difícil conocer los problemas.", "sería", ["es", "fue", "sea"], "Imaginary situation.", tr="If there were no freedom of the press, it would be harder to know the problems.", lemma="ser:él:cond"),
    ],
)

# ---------------------------------------------------------------------------- 731
L731 = lesson(
    "Imaginary questions: ¿Qué harías si…?",
    "¿Qué harías si ganaras mucho dinero? Yo compraría una casa.",
    requires=["hacer", "ganar", "comprar", "ir", "viajar", "país", "decir", "vivir", "tener", "trabajar", "ser", "ayudar"],
    cards=[
        card("Asking and answering",
             "To ask an imaginary question, use ¿Qué + conditional + si + imperfect subjunctive? To answer, use the conditional.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Qué harías si ganaras mucho dinero?", "Compraría una casa para mis padres."],
                            ["¿Adónde irías si pudieras viajar a cualquier país?", "Iría a Chile."],
                            ["¿Qué le dirías al presidente si pudieras hablar con él?", "Le pediría más escuelas."],
                            ["¿Qué harías si no tuvieras que trabajar?", "Viajaría por el mundo."],
                            ["¿Cómo sería tu vida si vivieras en otro país?", "Sería muy diferente."]],
                           say=[0, 1])]),
    ],
    exercises=[
        M("Which question asks about an imaginary situation?", "¿Qué harías si ganaras mucho dinero?", ["¿Qué haces cuando ganas dinero?", "¿Qué hiciste con el dinero?", "¿Qué harás mañana?"], "Conditional + si + imperfect subjunctive."),
        M("Which is a good answer to “¿Qué harías si no tuvieras que trabajar?”", "Viajaría por el mundo.", ["Viajé por el mundo.", "Viajo por el mundo todos los días.", "Viajaré por el mundo mañana."], "Answer with the conditional."),
        M("What does “¿Cómo sería tu vida si vivieras en otro país?” ask?", "What your life would be like if you lived in another country", ["Where you lived last year", "Why you travel", "When you moved"], "Imaginary."),
        F("¿Qué ___ tú si ganaras mucho dinero?", "harías", ["haces", "hiciste", "hagas"], "Imaginary question.", tr="What would you do if you won a lot of money?", lemma="hacer:tú:cond"),
        F("Si ___ mucho dinero, ¿qué harías?", "ganaras", ["ganas", "ganarías", "ganes"], "Si + imperfect subjunctive.", tr="If you won a lot of money, what would you do?", lemma="ganar:tú:isubj"),
        F("—¿Qué harías con el dinero? —Yo ___ una casa para mis padres.", "compraría", ["compro", "compré", "comprabas"], "Answer with the conditional.", tr="—What would you do with the money? —I would buy a house for my parents.", lemma="comprar:yo:cond"),
        F("¿Adónde ___ tú si pudieras viajar a cualquier país?", "irías", ["vas", "fuiste", "ir"], "Imaginary question.", tr="Where would you go if you could travel to any country?", lemma="ir:tú:cond"),
        F("Si ___ viajar a cualquier país, ¿adónde irías?", "pudieras", ["puedes", "podrías", "pudiste"], "Si + imperfect subjunctive.", tr="If you could travel to any country, where would you go?", lemma="poder:tú:isubj"),
        F("¿Qué le ___ tú al presidente si pudieras hablar con él?", "dirías", ["dices", "dijiste", "decir"], "Imaginary question.", tr="What would you say to the president if you could talk to him?", lemma="decir:tú:cond"),
    ],
    verify=(vpq("ganar", "ganara", "ganaras", "ganara", "ganáramos", "ganarais", "ganaran")
            + vpq("poder", "pudiera", "pudieras", "pudiera", "pudiéramos", "pudierais", "pudieran")),
)

# ---------------------------------------------------------------------------- 732
L732 = lesson(
    "Reading: what would change? Arguments about rights",
    "Si no existiera la libertad de prensa, sería más difícil conocer los problemas.",
    requires=["existir", "tener", "estudiar", "registrar", "haber", "conservar", "libertad", "prensa", "sindicato", "escuela", "policía", "pobreza"],
    cards=[
        card("Arguments with if-clauses",
             "People who defend rights often use imaginary situations to explain why a right matters. The sentences below are arguments that people make, not proven facts, and other people may disagree with them.",
             examples=[
                 ex("Si no existiera la libertad de prensa, sería más difícil conocer los problemas del gobierno.", "If freedom of the press did not exist, it would be harder to learn about the government’s problems.", "existiera"),
                 ex("Si los trabajadores no tuvieran sindicatos, tendrían menos poder para negociar.", "If workers did not have unions, they would have less power to negotiate.", "tuvieran"),
                 ex("Si hubiera más escuelas accesibles, más niños con discapacidad estudiarían con sus compañeros.", "If there were more accessible schools, more children with disabilities would study with their classmates.", "estudiarían"),
                 ex("Si la policía registrara todos los casos, sabríamos mejor cuántos delitos de odio hay.", "If the police recorded all cases, we would know better how many hate crimes there are.", "registrara"),
                 ex("Muchos expertos creen que habría menos pobreza si todos los niños pudieran ir a la escuela.", "Many experts believe there would be less poverty if all children could go to school.", "habría"),
                 ex("Si las lenguas indígenas se enseñaran en las escuelas, más niños las conservarían.", "If Indigenous languages were taught in schools, more children would keep them.", "conservarían"),
                 ex("Otras personas responden que, además de una ley, también haría falta aplicarla.", "Other people answer that, besides a law, it would also be necessary to apply it.", "haría falta"),
             ]),
    ],
    exercises=[
        M("Why is the reading using imaginary situations?", "To explain why a right matters", ["To tell a joke", "To list prices", "To describe the weather"], "Arguments."),
        M("Are the sentences presented as proven facts?", "No, they are arguments people make", ["Yes, all are proven", "They are laws", "They are advertisements"], "Not proven facts."),
        M("What does “haría falta aplicarla” mean?", "It would be necessary to apply it", ["It was applied yesterday", "It is already applied", "It cannot be applied"], "Hacer falta."),
        F("Si no ___ la libertad de prensa, sería más difícil conocer los problemas.", "existiera", ["existe", "existiría", "existirá"], "Imaginary situation.", tr="If freedom of the press did not exist, it would be harder to learn about the problems.", lemma="existir:ella:isubj"),
        F("Si los trabajadores no ___ sindicatos, tendrían menos poder.", "tuvieran", ["tienen", "tendrían", "tuvieron"], "Imaginary situation.", tr="If workers did not have unions, they would have less power.", lemma="tener:ellos:isubj"),
        F("Si hubiera más escuelas accesibles, más niños con discapacidad ___ con sus compañeros.", "estudiarían", ["estudian", "estudiaran", "estudiaron"], "Main clause = conditional.", tr="If there were more accessible schools, more children with disabilities would study with their classmates.", lemma="estudiar:ellos:cond"),
        F("Si la policía ___ todos los casos, sabríamos mejor cuántos delitos hay.", "registrara", ["registra", "registraría", "registrará"], "Imaginary situation.", tr="If the police recorded all the cases, we would know better how many crimes there are.", lemma="registrar:ella:isubj"),
        F("Muchos expertos creen que ___ menos pobreza si todos los niños pudieran ir a la escuela.", "habría", ["hay", "hubo", "haya"], "Conditional result.", tr="Many experts believe that there would be less poverty if all children could go to school.", lemma="haber:él:cond"),
        F("Si las lenguas indígenas se enseñaran en las escuelas, más niños las ___.", "conservarían", ["conservan", "conservaron", "conservarán"], "Main clause = conditional.", tr="If Indigenous languages were taught in schools, more children would keep them.", lemma="conservar:ellos:cond"),
    ],
    verify=(vpq("existir", "existiera", "existieras", "existiera", "existiéramos", "existierais", "existieran")
            + vpd("estudiar", "estudiaría", "estudiarías", "estudiaría", "estudiaríamos", "estudiaríais", "estudiarían")),
)

# ---------------------------------------------------------------------------- 733
L733 = lesson(
    "Review: adjectival clauses, known or unknown, present and past",
    "Busco un abogado que sepa de derechos humanos. No había nadie que hablara árabe.",
    requires=["buscar", "necesitar", "conocer", "haber", "tener", "saber", "poder", "hablar", "ayudar", "vivir", "ser", "escuela"],
    cards=[
        card("Indicative or subjunctive?",
             "After a noun, use the indicative when the person or thing exists and is known. Use the subjunctive when it is unknown, may not exist, or does not exist (nadie, ninguno, cualquiera). "
             "In past contexts, the subjunctive is the imperfect subjunctive.",
             tables=[table(["Situación", "Ejemplo"],
                           [["Known: indicative", "Tengo una amiga que sabe lengua de señas."],
                            ["Unknown: subjunctive", "Busco un abogado que sepa de derechos humanos."],
                            ["Nonexistent: subjunctive", "No hay nadie que sepa la respuesta."],
                            ["Any: subjunctive", "Cualquiera que conozca la ley debe acatarla."],
                            ["Past, nonexistent", "En el pueblo no había ninguna escuela que tuviera ascensor."],
                            ["Past, nobody", "No había nadie que hablara árabe."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which sentence describes a person who may not exist?", "Busco un abogado que sepa de derechos humanos.", ["Tengo un abogado que sabe de derechos humanos.", "Conozco a un abogado que sabe de derechos humanos.", "Mi abogado sabe de derechos humanos."], "Unknown → subjunctive."),
        M("Which mood follows “nadie que”?", "The subjunctive", ["The indicative", "The imperative", "The infinitive"], "Nadie que + subjunctive."),
        M("Which sentence is correct?", "No había nadie que hablara árabe.", ["No había nadie que hablaba árabe.", "No había nadie que hable árabe.", "No había nadie que hablar árabe."], "Past nonexistent → imperfect subjunctive."),
        F("No hay nadie que ___ la respuesta.", "sepa", ["sabe", "saber", "sabía"], "Nadie → subjunctive.", tr="There is nobody who knows the answer.", lemma="saber:él:subj"),
        F("Tengo una amiga que ___ lengua de señas.", "sabe", ["sepa", "saber", "supiera"], "Known person → indicative.", tr="I have a friend who knows sign language.", lemma="saber:ella"),
        F("En el pueblo no había ninguna escuela que ___ ascensor.", "tuviera", ["tenía", "tiene", "tener"], "Ninguna, past → imperfect subjunctive.", tr="In the town there was no school that had an elevator.", lemma="tener:ella:isubj"),
        F("Vivo en un barrio que ___ muy tranquilo.", "es", ["sea", "ser", "fuera"], "Known place → indicative.", tr="I live in a neighborhood that is very quiet.", lemma="ser:él"),
        F("Las organizaciones que ___ a los migrantes trabajan mucho.", "ayudan", ["ayuden", "ayudar", "ayudaran"], "Existing organizations → indicative.", tr="The organizations that help migrants work a lot.", lemma="ayudar:ellos"),
        F("Cualquiera que ___ la ley debe acatarla.", "conozca", ["conoce", "conocer", "conocía"], "Cualquiera que → subjunctive.", tr="Anyone who knows the law must abide by it.", lemma="conocer:él:subj"),
    ],
)

# ---------------------------------------------------------------------------- 734
L734 = lesson(
    "Review: adverbial clauses, always subjunctive or future vs habit",
    "Antes de que empiece, sin que lo sepan, a menos que llueva. Cuando llegue, te llamo.",
    requires=["empezar", "llegar", "poder", "llover", "trabajar", "hablar", "reunión", "casa", "llamar", "salir", "mañana", "descansar"],
    cards=[
        card("Two groups of conjunctions",
             "Group 1 always takes the subjunctive: para que, antes de que, sin que, a menos que, con tal de que, en caso de que. "
             "Group 2 takes the subjunctive for a future or pending event but the indicative for a habit or a fact: cuando, en cuanto, tan pronto como, después de que, hasta que, aunque.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["Group 1: always", "Voy a hablar con ellos antes de que empiece la reunión."],
                            ["Group 1: always", "Saldremos mañana a menos que llueva."],
                            ["Group 2: pending", "Mañana, cuando llegue a casa, te llamaré."],
                            ["Group 2: habit", "Todos los días, cuando llego a casa, descanso."],
                            ["Group 2: pending", "Aunque llueva mañana, iremos al parque."],
                            ["Past", "Salió sin que nadie lo viera."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which conjunction ALWAYS takes the subjunctive?", "antes de que", ["cuando", "porque", "aunque"], "Antes de que."),
        M("Which sentence refers to a habit?", "Cuando llego a casa, descanso.", ["Cuando llegue a casa, descansaré.", "Antes de que llegue a casa, descansaré.", "Para que llegue a casa, descansaré."], "Habit → indicative."),
        M("Which sentence is correct?", "Salió sin que nadie lo viera.", ["Salió sin que nadie lo ve.", "Salió sin que nadie lo vio.", "Salió sin que nadie lo ver."], "Sin que, past → imperfect subjunctive."),
        F("Voy a hablar con ellos antes de que ___ la reunión.", "empiece", ["empieza", "empezó", "empezar"], "Antes de que → subjunctive.", tr="I’m going to talk to them before the meeting begins.", lemma="empezar:ella:subj"),
        F("Mañana, cuando ___ a casa, te llamaré.", "llegue", ["llego", "llegué", "llegar"], "Pending event → subjunctive.", tr="Tomorrow, when I get home, I will call you.", lemma="llegar:yo:subj"),
        F("Todos los días, cuando ___ a casa, descanso.", "llego", ["llegue", "llegaba", "llegar"], "Habit → indicative.", tr="Every day, when I get home, I rest.", lemma="llegar:yo"),
        F("Trabaja mucho para que sus hijos ___ estudiar.", "puedan", ["pueden", "podían", "poder"], "Para que → subjunctive.", tr="He works a lot so that his children can study.", lemma="poder:ellos:subj"),
        F("Saldremos mañana a menos que ___ mucho.", "llueva", ["llueve", "llovió", "llover"], "A menos que → subjunctive.", tr="We will leave tomorrow unless it rains a lot.", lemma="llover:él:subj"),
        F("Aunque ___ mañana, iremos al parque.", "llueva", ["llovió", "llover", "llovido"], "Pending event → subjunctive.", tr="Even if it rains tomorrow, we will go to the park.", lemma="llover:él:subj"),
    ],
)

# ---------------------------------------------------------------------------- 735
L735 = lesson(
    "Giving opinions in a debate with the conditional",
    "Yo diría que el problema es complejo. Sería mejor escuchar a todos.",
    requires=["opinión", "creer", "pensar", "parecer", "acuerdo", "mejor", "problema", "solución", "punto", "decir", "poder", "estar"],
    cards=[
        card("Softening an opinion",
             "The conditional makes an opinion sound careful and polite. It is common in debates, interviews and reports. Useful frames: yo diría que…, me parecería…, sería mejor…, no estaría de acuerdo con…, podríamos…",
             examples=[
                 ex("Yo diría que el problema es complejo.", "I would say that the problem is complex.", "diría"),
                 ex("Me parecería injusto cambiar la ley sin hablar con los vecinos.", "It would seem unfair to me to change the law without talking to the neighbors.", "parecería"),
                 ex("Sería mejor escuchar a todas las partes.", "It would be better to listen to all sides.", "Sería"),
                 ex("No estaría de acuerdo con una ley tan estricta.", "I would not agree with such a strict law.", "estaría"),
                 ex("Desde mi punto de vista, la educación sería la mejor solución.", "From my point of view, education would be the best solution.", "sería"),
                 ex("Podríamos empezar por informar mejor a la gente.", "We could start by informing people better.", "Podríamos"),
                 ex("No creo que sea fácil, pero tampoco sería imposible.", "I don’t think it’s easy, but it wouldn’t be impossible either.", "sería"),
             ]),
    ],
    exercises=[
        M("Why use the conditional to give an opinion?", "It sounds careful and polite", ["It makes the opinion a past event", "It makes it an order", "It makes it a question"], "Softening."),
        M("Which sentence is a softened opinion?", "Yo diría que el problema es complejo.", ["El problema es complejo, punto.", "Digan que el problema es complejo.", "Dijeron que el problema es complejo."], "Conditional."),
        M("What does “Sería mejor escuchar a todas las partes” mean?", "It would be better to listen to all sides", ["It was better to listen", "Listen to all sides now", "Nobody listened"], "Sería mejor."),
        F("Yo ___ que el problema es complejo.", "diría", ["dirías", "dirían", "decir"], "Yo → diría.", tr="I would say that the problem is complex.", lemma="decir:yo:cond"),
        F("Me ___ injusto cambiar la ley sin hablar con los vecinos.", "parecería", ["parecerías", "parecerían", "parecer"], "Singular impersonal.", tr="It would seem unfair to me to change the law without talking to the neighbors.", lemma="parecer:él:cond"),
        F("___ mejor escuchar a todas las partes.", "Sería", ["Serías", "Serían", "Ser"], "Singular impersonal.", tr="It would be better to listen to all sides.", lemma="ser:él:cond"),
        F("Yo no ___ de acuerdo con una ley tan estricta.", "estaría", ["estarías", "estarían", "estar"], "Yo → estaría.", tr="I would not agree with such a strict law.", lemma="estar:yo:cond"),
        F("Nosotros ___ empezar por informar mejor a la gente.", "podríamos", ["podría", "podrían", "poder"], "Nosotros.", tr="We could start by informing people better.", lemma="poder:nosotros:cond"),
        F("No creo que ___ fácil, pero tampoco sería imposible.", "sea", ["es", "ser", "fue"], "No creo que → subjunctive.", tr="I don’t think it’s easy, but it wouldn’t be impossible either.", lemma="ser:él:subj"),
    ],
)

# ---------------------------------------------------------------------------- 736
L736 = lesson(
    "Reading: a report by an imaginary organization (invented text)",
    "Según la organización, el gobierno cerró tres periódicos el año pasado.",
    requires=["organización", "informe", "gobierno", "periódico", "periodista", "amenaza", "tribunal", "libertad", "prensa", "recomendar", "investigar", "mejorar"],
    cards=[
        card("Reading with attribution",
             "This text is invented. It describes an imaginary report about an imaginary country, and it is written to practice language from this unit. It does not describe any real country or organization.",
             examples=[
                 ex("Según la organización, el gobierno cerró tres periódicos el año pasado.", "According to the organization, the government closed three newspapers last year.", "cerró"),
                 ex("El informe dice que muchos periodistas recibieron amenazas y que nadie investigó los casos.", "The report says that many journalists received threats and that nobody investigated the cases.", "recibieron"),
                 ex("El gobierno rechaza el informe y dice que no existe ninguna censura.", "The government rejects the report and says that there is no censorship.", "rechaza"),
                 ex("La organización recomienda que el gobierno permita la libertad de prensa y que los tribunales investiguen las amenazas.", "The organization recommends that the government allow freedom of the press and that the courts investigate the threats.", "permita"),
                 ex("También pidió que el gobierno publicara los datos antes de que terminara el año.", "It also asked that the government publish the data before the year ended.", "publicara"),
                 ex("Si el gobierno aceptara estas ideas, la situación mejoraría.", "If the government accepted these ideas, the situation would improve.", "aceptara"),
                 ex("Los ciudadanos esperan que el próximo año sea mejor.", "Citizens hope that next year will be better.", "sea"),
             ]),
    ],
    exercises=[
        M("Is this text about a real country?", "No, it is invented", ["Yes, a real report", "Yes, a law", "Yes, a news item"], "Texto inventado."),
        M("What does the government say?", "That there is no censorship", ["That the report is perfect", "That it closed three newspapers", "That it will resign"], "Rechaza el informe."),
        M("Why does the text say “según la organización”?", "To show who makes the claim", ["To prove it is true", "To make it a law", "To avoid verbs"], "Attribution."),
        F("Según la organización, el gobierno ___ tres periódicos el año pasado.", "cerró", ["cierra", "cerrará", "cerrar"], "Last year → preterite.", tr="According to the organization, the government closed three newspapers last year.", lemma="cerrar:él:pret"),
        F("Muchos periodistas ___ amenazas el año pasado.", "recibieron", ["reciben", "recibirán", "recibir"], "Last year → preterite.", tr="Many journalists received threats last year.", lemma="recibir:ellos:pret"),
        F("La organización recomienda que el gobierno ___ la libertad de prensa.", "permita", ["permite", "permitir", "permitía"], "Recomendar que → subjunctive.", tr="The organization recommends that the government allow freedom of the press.", lemma="permitir:él:subj"),
        F("Recomienda que los tribunales ___ las amenazas.", "investiguen", ["investigan", "investigar", "investigaron"], "Recomendar que → subjunctive.", tr="It recommends that the courts investigate the threats.", lemma="investigar:ellos:subj"),
        F("Pidió que el gobierno ___ los datos antes de que terminara el año.", "publicara", ["publique", "publica", "publicó"], "Past request → imperfect subjunctive.", tr="It asked that the government publish the data before the year ended.", lemma="publicar:él:isubj"),
        F("Si el gobierno aceptara estas ideas, la situación ___.", "mejoraría", ["mejora", "mejoró", "mejorar"], "Si + imperfect subjunctive → conditional.", tr="If the government accepted these ideas, the situation would improve.", lemma="mejorar:ella:cond"),
    ],
    verify=(vpq("publicar", "publicara", "publicaras", "publicara", "publicáramos", "publicarais", "publicaran")
            + vpq("aceptar", "aceptara", "aceptaras", "aceptara", "aceptáramos", "aceptarais", "aceptaran")),
)

# ---------------------------------------------------------------------------- 737
L737 = lesson(
    "Review: the conditional and si-clauses",
    "Si pudiera, te ayudaría. Si hace buen tiempo, iremos al parque.",
    requires=["recibir", "ir", "entender", "haber", "ayudar", "hacer", "poder", "decir", "venir", "terminar", "ruido", "dormir"],
    cards=[
        card("Choosing the pattern",
             "Likely: si + present, … present, future or command. Imaginary or unlikely: si + imperfect subjunctive, … conditional. Past habit: si + imperfect, … imperfect. "
             "The conditional also expresses politeness, advice, a future seen from the past and a guess about the past.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["Likely", "Si hace buen tiempo, iremos al parque."],
                            ["Imaginary", "Si pudiera, te ayudaría."],
                            ["Imaginary", "Si hubiera menos ruido, podríamos dormir."],
                            ["Polite", "¿Podría ayudarme?"],
                            ["Future seen from the past", "Dijo que vendría."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which sentence is a polite request?", "¿Podría ayudarme, por favor?", ["¿Me ayudas ya?", "Ayúdame ahora mismo.", "Me ayudó ayer."], "Conditional = polite."),
        M("Which pair is correct?", "Si estudiaras más, aprobarías.", ["Si estudiarías más, aprobarías.", "Si estudiaras más, aprobabas.", "Si estudias más, aprobarías."], "Si + imperfect subjunctive, conditional."),
        M("Which sentence reports a future seen from the past?", "Dijo que vendría.", ["Dice que viene.", "Dirá que vendrá.", "Dijo que vino."], "Conditional."),
        F("Si ellos ___ más ayuda, terminarían el trabajo.", "recibieran", ["reciben", "recibirían", "recibieron"], "Si + imperfect subjunctive.", tr="If they received more help, they would finish the job.", lemma="recibir:ellos:isubj"),
        F("Si hiciera buen tiempo, nosotros ___ a la playa.", "iríamos", ["vamos", "fuimos", "iremos"], "Imaginary → conditional.", tr="If the weather were nice, we would go to the beach.", lemma="ir:nosotros:cond"),
        F("Si tú ___ mi problema, me ayudarías.", "entendieras", ["entiendes", "entenderías", "entendiste"], "Si + imperfect subjunctive.", tr="If you understood my problem, you would help me.", lemma="entender:tú:isubj"),
        F("Si no ___ tanto ruido, dormiríamos mejor.", "hubiera", ["hay", "habría", "hubo"], "Si + imperfect subjunctive.", tr="If there weren’t so much noise, we would sleep better.", lemma="haber:él:isubj"),
        F("Si pudiera, te ___ con mucho gusto.", "ayudaría", ["ayudo", "ayudé", "ayudabas"], "Main clause = conditional.", tr="If I could, I would gladly help you.", lemma="ayudar:yo:cond"),
        F("Si ___ buen tiempo mañana, iremos al parque.", "hace", ["hiciera", "haría", "hará"], "Likely → present.", tr="If the weather is nice tomorrow, we will go to the park.", lemma="hacer:él"),
    ],
    verify=(vpq("recibir", "recibiera", "recibieras", "recibiera", "recibiéramos", "recibierais", "recibieran")
            + vpq("entender", "entendiera", "entendieras", "entendiera", "entendiéramos", "entendierais", "entendieran")
            + vpq("ayudar", "ayudara", "ayudaras", "ayudara", "ayudáramos", "ayudarais", "ayudaran")),
)
UNIT = unit("Derechos humanos", [L715, L716, L717, L718, L719, L720, L721, L722, L723, L724, L725, L726, L727, L728, L729, L730, L731, L732, L733, L734, L735, L736, L737])

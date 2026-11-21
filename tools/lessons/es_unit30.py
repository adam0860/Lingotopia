"""Unit 30: review of units 26-29 (textbook Chapter 30): extradition, cartels as terrorists, anonymity, mixed subjunctive reviews."""
from dsl_es import *

# ---------------------------------------------------------------------------- 612
L612 = lesson(
    "Reading: extradition in Colombia",
    "La extradición es la entrega de una persona a otro país para ser juzgada.",
    requires=["extranjero", "país", "justicia", "juez", "ley", "estadounidense", "víctima", "verdad", "cárcel", "juicio"],
    cards=[
        card("A long debate",
             "Extradition (la extradición) is the handing over of a person to another country to be tried or to serve a sentence. In Colombia it became a central issue in the fight against drug trafficking. This reading summarizes the main facts and the two sides of the debate.",
             examples=[
                 ex("La extradición es la entrega de una persona a otro país para ser juzgada o cumplir una condena.", "Extradition is handing a person over to another country to be tried or to serve a sentence.", "entrega"),
                 ex("En los años ochenta, los jefes del narcotráfico temían mucho que los extraditaran a los Estados Unidos.", "In the 1980s drug-trafficking bosses were very afraid of being extradited to the United States.", "temían"),
                 ex("Un grupo que se llamaba Los Extraditables cometió muchos actos de violencia para presionar al gobierno.", "A group called Los Extraditables committed many acts of violence to pressure the government.", "se llamaba"),
                 ex("La constitución de mil novecientos noventa y uno prohibió extraditar a los colombianos de nacimiento.", "The constitution of 1991 prohibited extraditing native-born Colombians.", "prohibió"),
                 ex("En mil novecientos noventa y siete, una reforma volvió a permitir la extradición de colombianos.", "In 1997 a reform again allowed the extradition of Colombians.", "volvió a permitir"),
                 ex("Desde entonces, el país ha extraditado a muchas personas acusadas de narcotráfico.", "Since then the country has extradited many people accused of drug trafficking.", "ha extraditado"),
                 ex("Algunas personas dicen que la extradición todavía es una herramienta útil contra el crimen organizado.", "Some people say that extradition is still a useful tool against organized crime.", "útil"),
                 ex("Otras personas dicen que produce impunidad y que las víctimas no conocen toda la verdad.", "Other people say that it produces impunity and that the victims do not learn the whole truth.", "impunidad"),
             ]),
    ],
    exercises=[
        M("What is extradition?", "Handing a person over to another country to be tried or to serve a sentence", ["A kind of tax", "A police dog", "A prison guard"], "La entrega de una persona a otro país."),
        M("What did Los Extraditables do?", "They used violence to pressure the government", ["They printed newspapers", "They built prisons", "They ran elections"], "Cometió actos de violencia para presionar al gobierno."),
        M("What did the 1991 constitution do?", "It prohibited extraditing native-born Colombians", ["It created extradition", "It closed the border", "It abolished the courts"], "Prohibió extraditar a los colombianos de nacimiento."),
        M("What do critics of extradition say?", "It produces impunity and the victims do not learn the whole truth", ["It is too cheap", "It helps the victims always", "It only affects tourists"], "Produce impunidad."),
        F("En los años ochenta, los jefes del narcotráfico ___ mucho la extradición.", "temían", ["temió", "temen", "temer"], "Repeated feeling in the past; plural.", tr="In the 1980s, the drug-trafficking bosses greatly feared extradition.", lemma="temer:ellos:impf"),
        F("La constitución de mil novecientos noventa y uno ___ extraditar a los colombianos de nacimiento.", "prohibió", ["prohibieron", "prohíbe", "prohibir"], "Dated event; singular.", tr="The constitution of 1991 prohibited extraditing native-born Colombians.", lemma="prohibir:él:pret"),
        F("Desde mil novecientos noventa y siete, el país ha ___ a muchas personas.", "extraditado", ["extraditar", "extradita", "extraditó"], "Present perfect: haber + participle.", tr="Since 1997, the country has extradited many people."),
        F("Algunas personas dicen que la extradición ___ útil.", "es", ["son", "ser", "sea"], "Singular subject; saying it as a fact.", tr="Some people say that extradition is useful.", lemma="ser:ella"),
        M("Why does the reading give both views?", "People disagree about extradition", ["The facts are invented", "Only one side spoke", "It avoids dates"], "There are different opinions."),
    ],
)

# ---------------------------------------------------------------------------- 613
L613 = lesson(
    "Round table: how do you feel about extradition?",
    "Me sorprende que algunos acusados prefieran ser juzgados en otro país.",
    requires=["sorprender", "preocupar", "alegrar", "lamentar", "temer", "miedo", "acusado", "juicio", "país", "condena", "víctima"],
    cards=[
        card("Opinions with emotion verbs",
             "In a round table, speakers react to a topic with emotion expressions. Remember the rule: a different subject after que → subjunctive; the same subject → infinitive. "
             "Verbs like sorprender, indignar, preocupar and molestar need the indirect pronoun (me, te, le, nos, les) and the verb stays in the singular when a que clause follows.",
             examples=[
                 ex("Me sorprende que algunos acusados prefieran ser juzgados en otro país.", "It surprises me that some defendants prefer to be tried in another country.", "prefieran"),
                 ex("A los familiares de las víctimas les preocupa que las condenas sean más cortas en el extranjero.", "It worries the victims' families that sentences are shorter abroad.", "sean"),
                 ex("Estoy contento de que los acusados se enfrenten a la justicia.", "I am happy that the accused are facing justice.", "enfrenten"),
                 ex("Lamento que no todas las víctimas conozcan la verdad.", "I am sorry that not all victims know the truth.", "conozcan"),
                 ex("Tengo miedo de que el crimen organizado encuentre otras formas de actuar.", "I am afraid that organized crime will find other ways to operate.", "encuentre"),
                 ex("Me alegra que haya más cooperación entre los dos países.", "I am glad that there is more cooperation between the two countries.", "haya"),
             ]),
    ],
    exercises=[
        F("Me sorprende que algunos acusados ___ ser juzgados en otro país.", "prefieran", ["prefieren", "preferir", "preferimos"], "Sorprender que + subjunctive.", tr="It surprises me that some defendants prefer to be tried in another country.", lemma="preferir:ellos:subj"),
        F("A los familiares les preocupa que las condenas ___ más cortas.", "sean", ["son", "ser", "somos"], "Preocupar que + subjunctive.", tr="It worries the families that the sentences are shorter.", lemma="ser:ellas:subj"),
        F("Estoy contento de que los acusados se ___ a la justicia.", "enfrenten", ["enfrentan", "enfrentar", "enfrentamos"], "Estar contento de que + subjunctive.", tr="I am happy that the accused are facing justice."),
        F("Lamento que no todas las víctimas ___ la verdad.", "conozcan", ["conocen", "conocer", "conocemos"], "Lamentar que + subjunctive.", tr="I am sorry that not all victims know the truth.", lemma="conocer:ellas:subj"),
        F("Tengo miedo de que el crimen organizado ___ otras formas de actuar.", "encuentre", ["encuentra", "encontrar", "encuentran"], "Tener miedo de que + subjunctive.", tr="I am afraid that organized crime will find other ways to operate.", lemma="encontrar:él:subj"),
        F("Me alegra que ___ más cooperación entre los dos países.", "haya", ["hay", "haber", "han"], "Alegrar que + subjunctive.", tr="I am glad that there is more cooperation between the two countries.", lemma="haber:él:subj"),
        F("Me alegra ___ con gente de otros países.", "trabajar", ["trabaje", "trabajo", "trabajas"], "Same person: infinitive.", tr="I am glad to work with people from other countries."),
        M("Which sentence is correct?", "Les indigna que la ley sea tan débil.", ["Les indigna que la ley es tan débil.", "Les indignan que la ley sea tan débil.", "Se indigna que la ley sea tan débil."], "Indirect pronoun les; singular verb; subjunctive."),
        M("When do you use the infinitive after an emotion?", "When the person who feels is the one who acts", ["When the subjects differ", "Only with ojalá", "Never"], "Same subject → infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 614
L614 = lesson(
    "Reading: should drug cartels be called terrorist groups?",
    "Algunos analistas proponen que se clasifique a los cárteles como grupos terroristas.",
    requires=["analista", "grupo", "terrorista", "político", "poder", "mercado", "financiar", "ley", "gobierno", "violencia", "frontera", "sociedad"],
    cards=[
        card("A policy debate",
             "In the United States and Mexico, analysts debate whether violent drug-trafficking organizations should be officially classified as terrorist groups. This reading presents the arguments of each side without taking one. "
             "In February 2025 the U.S. government added several Mexican criminal organizations to its list of foreign terrorist organizations; the practical effects are still being discussed.",
             examples=[
                 ex("Algunos analistas dicen que los cárteles se parecen a los grupos terroristas.", "Some analysts say that the cartels resemble terrorist groups.", "se parecen"),
                 ex("Según ellos, tienen poder político, usan el terror para mantener su control y financian sus actividades con mercados ilegales.", "According to them, they have political power, use terror to keep control and finance their activities with illegal markets.", "usan"),
                 ex("Según esta postura, las leyes antiterroristas permitirían investigar mejor a los políticos que los protegen.", "According to this view, antiterrorism laws would allow better investigation of politicians who protect them.", "permitirían"),
                 ex("Otros analistas responden que los cárteles buscan dinero, no objetivos políticos.", "Other analysts answer that the cartels seek money, not political goals.", "buscan"),
                 ex("También temen que la nueva clasificación sirva para justificar acciones militares extranjeras.", "They also fear that the new classification will serve to justify foreign military action.", "sirva"),
                 ex("Dicen que es más importante atacar las causas sociales y la corrupción que cambiar un nombre.", "They say it is more important to address the social causes and corruption than to change a name.", "atacar"),
                 ex("Los dos lados dudan que haya una solución rápida.", "Both sides doubt that there is a quick solution.", "haya"),
             ]),
    ],
    exercises=[
        M("What do some analysts say about the cartels?", "They resemble terrorist groups", ["They are charities", "They are schools", "They are hospitals"], "Se parecen a los grupos terroristas."),
        M("What do other analysts answer?", "The cartels seek money, not political goals", ["The cartels are political parties", "The cartels are governments", "The cartels do not exist"], "Buscan dinero."),
        M("What do some fear about the new classification?", "That it may serve to justify foreign military action", ["That it will lower taxes", "That it will close banks", "That it will help tourism"], "Temen que sirva para justificar acciones militares."),
        M("Why does the reading give both positions?", "To present the debate fairly", ["To prove one side is right", "To avoid facts", "To make it shorter"], "It reports each side."),
        F("Algunos analistas dicen que los cárteles ___ a los grupos terroristas.", "se parecen", ["se parece", "parecerse", "se parecieron"], "Plural subject, present.", tr="Some analysts say the cartels resemble terrorist groups."),
        F("Temen que la nueva clasificación ___ para justificar acciones militares.", "sirva", ["sirve", "servir", "sirven"], "Temer que + subjunctive.", tr="They fear that the new classification will serve to justify military action.", lemma="servir:ella:subj"),
        F("Los dos lados dudan que ___ una solución rápida.", "haya", ["hay", "haber", "han"], "Dudar que + subjunctive.", tr="Both sides doubt that there is a quick solution.", lemma="haber:él:subj"),
        F("Otros analistas dicen que es más importante ___ la corrupción.", "atacar", ["ataque", "ataca", "atacan"], "Impersonal: infinitive.", tr="Other analysts say it is more important to attack corruption."),
        M("Which sentence is correct?", "Es posible que esa clasificación cambie las leyes.", ["Es posible que esa clasificación cambia las leyes.", "Es posible que esa clasificación cambiar las leyes.", "Es posible esa clasificación cambie las leyes."], "Es posible que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 615
L615 = lesson(
    "Pronouns in crime news: se lo, se la, los…",
    "La policía encontró el cargamento y se lo mostró a la prensa.",
    requires=["policía", "encontrar", "mostrar", "decir", "ofrecer", "dinero", "candidato", "prensa", "extranjero", "pedir", "ayuda", "preguntar"],
    cards=[
        card("Direct and indirect pronouns together",
             "Crime reports are full of pronouns that replace nouns already mentioned. Remember: indirect first, direct second; le/les become se before lo, la, los, las. "
             "Ask what? or whom? to find the direct object and to whom? to find the indirect object.",
             examples=[
                 ex("La policía encontró el cargamento y se lo mostró a la prensa.", "The police found the shipment and showed it to the press.", "se lo mostró"),
                 ex("Los detectives interrogan al chofer. Lo interrogan desde ayer.", "The detectives are questioning the driver. They have been questioning him since yesterday.", "Lo interrogan"),
                 ex("Un jefe le ofreció dinero a un candidato. Se lo ofreció en secreto.", "A boss offered money to a candidate. He offered it to him in secret.", "Se lo ofreció"),
                 ex("Algunos vecinos tienen información, pero no se la dicen a la policía por miedo.", "Some neighbors have information, but they do not tell it to the police out of fear.", "no se la dicen"),
                 ex("Los expertos quieren recomendárselo al presidente.", "The experts want to recommend it to the president.", "recomendárselo"),
             ]),
    ],
    exercises=[
        F("La policía encontró el cargamento y ___ mostró a la prensa.", "se lo", ["se la", "le lo", "lo se"], "El cargamento: masculine; le → se.", tr="The police found the shipment and showed it to the press."),
        F("Los detectives interrogan al chofer. ___ interrogan desde ayer.", "Lo", ["Se", "La", "Los"], "Direct object: al chofer.", tr="The detectives are questioning the driver. They have been questioning him since yesterday."),
        F("Un jefe le ofreció dinero a un candidato. ___ ofreció en secreto.", "Se lo", ["Le lo", "Lo se", "Se la"], "Dinero: masculine.", tr="A boss offered money to a candidate. He offered it to him in secret."),
        F("Algunos vecinos tienen información, pero no ___ dicen a la policía.", "se la", ["se lo", "le la", "la se"], "Información: feminine.", tr="Some neighbors have information, but they do not tell it to the police."),
        F("Los expertos quieren ___ al presidente.", "recomendárselo", ["recomendarlose", "recomendarselo", "recomendar se lo"], "Infinitive + se + lo, with accent.", tr="The experts want to recommend it to the president."),
        F("La periodista tiene las fotos y va a ___ al editor.", "enseñárselas", ["enseñarselas", "enseñarlas se", "enseñárlase"], "Infinitive + se + las, with accent.", tr="The journalist has the photos and is going to show them to the editor."),
        M("Which sentence is correct?", "Se lo dije ayer.", ["Le lo dije ayer.", "Lo le dije ayer.", "Se le dije ayer."], "Le + lo → se lo."),
        M("In “Se las entregó,” what does “las” replace?", "a feminine plural thing", ["a masculine singular person", "a verb", "an adverb"], "Las = feminine plural direct object."),
        M("Where may both pronouns go in “Voy a decírselo”?", "Before voy: Se lo voy a decir", ["After the sentence", "Between voy and a", "They cannot move"], "Both pronouns move together."),
    ],
)

# ---------------------------------------------------------------------------- 616
L616 = lesson(
    "Reading: anonymity, hacktivists and the debate about privacy",
    "El anonimato protege la privacidad, pero también puede esconder delitos.",
    requires=["privacidad", "internet", "usuario", "grupo", "protesta", "gobierno", "empresa", "información", "delito", "derecho", "libertad"],
    cards=[
        card("Two edges",
             "Anonymity on the Internet is a double-edged tool. It protects privacy and free expression, especially for people living under repressive governments. It can also hide harassment, fraud and other crimes. "
             "Anonymous is the name of a loose online movement of hacktivists with no formal leaders. It has been praised by supporters and criticized by governments, companies and some observers. Some of its members were arrested and prosecuted in several countries.",
             examples=[
                 ex("En los primeros años de internet, muchas personas valoraban el anonimato como una libertad.", "In the early years of the Internet, many people valued anonymity as a freedom.", "valoraban"),
                 ex("Hoy muchas personas lo asocian con el fraude, el acoso y otros delitos.", "Today many people associate it with fraud, harassment and other crimes.", "asocian"),
                 ex("Al mismo tiempo, las empresas y los gobiernos reúnen mucha información sobre los usuarios.", "At the same time, companies and governments gather a lot of information about users.", "reúnen"),
                 ex("Anonymous es un movimiento de hacktivistas sin una estructura formal ni líderes fijos.", "Anonymous is a movement of hacktivists with no formal structure or fixed leaders.", "movimiento"),
                 ex("Sus seguidores dicen que defiende la libertad de expresión y critica a los poderosos.", "Its followers say that it defends free speech and criticizes the powerful.", "defiende"),
                 ex("Sus críticos dicen que algunos ataques causaron daños y que ninguna protesta justifica un delito.", "Its critics say that some attacks caused damage and that no protest justifies a crime.", "justifica"),
                 ex("Varios miembros fueron arrestados, y algunos recibieron condenas.", "Several members were arrested, and some received sentences.", "fueron arrestados"),
                 ex("Muchos expertos piensan que movimientos así van a aparecer otra vez en el futuro, con otros nombres.", "Many experts think that movements like this will appear again in the future, under other names.", "aparecer"),
             ]),
    ],
    exercises=[
        M("Why is anonymity a double-edged tool?", "It protects privacy but can also hide crimes", ["It is free but slow", "It is old but useful", "It is quiet but loud"], "Protege la privacidad y puede esconder delitos."),
        M("What is Anonymous?", "A loose movement of hacktivists with no formal leaders", ["A bank", "A police unit", "A government agency"], "Un movimiento sin estructura formal ni líderes fijos."),
        M("What do its critics say?", "Some attacks caused damage and no protest justifies a crime", ["Nothing at all", "That it is too quiet", "That it has leaders"], "Ninguna protesta justifica un delito."),
        M("What happened to some members?", "Several were arrested and some were sentenced", ["They all became police", "They were elected", "They disappeared"], "Varios fueron arrestados."),
        F("Hoy muchas personas ___ el anonimato con el fraude.", "asocian", ["asocia", "asociar", "asociamos"], "Plural subject, present.", tr="Today many people associate anonymity with fraud.", lemma="asociar:ellos"),
        F("Las empresas ___ mucha información sobre los usuarios.", "reúnen", ["reúne", "reunir", "reunimos"], "Plural subject, present.", tr="Companies gather a lot of information about users.", lemma="reunir:ellos"),
        F("Sus seguidores dicen que el grupo ___ la libertad de expresión.", "defiende", ["defienden", "defender", "defendemos"], "Singular subject, present.", tr="Its followers say that the group defends free speech.", lemma="defender:él"),
        F("Es importante que los gobiernos ___ la privacidad de las personas.", "protejan", ["protegen", "proteger", "protegemos"], "Es importante que + subjunctive.", tr="It is important that governments protect people's privacy.", lemma="proteger:ellos:subj"),
        M("Which word means “harassment”?", "acoso", ["anonimato", "rescate", "libertad"], "Acoso = harassment."),
    ],
)

# ---------------------------------------------------------------------------- 617
L617 = lesson(
    "Review W: wishes, requests and orders",
    "Los vecinos quieren que el alcalde cierre la calle. Los vecinos quieren cerrar la calle.",
    requires=["querer", "pedir", "decir", "mandar", "permitir", "prohibir", "esperar", "alcalde", "calle", "vecino", "ordenar", "recomendar"],
    cards=[
        card("Three questions",
             "1) Is the main verb a wish, request, order or advice? 2) Do the two clauses have different subjects? Then que + subjunctive. 3) Same subject? Then the infinitive. "
             "Decir que is a special case: it takes the indicative when it reports a fact and the subjunctive when it gives an order.",
             tables=[table(["Situation", "Ejemplo"],
                           [["Different subjects: subjunctive", "Los vecinos quieren que el alcalde cierre la calle."],
                            ["Same subject: infinitive", "Los vecinos quieren cerrar la calle."],
                            ["Decir: fact", "El alcalde dice que la calle está cerrada."],
                            ["Decir: order", "El alcalde dice que cerremos la calle."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Los vecinos quieren que el alcalde ___ la calle.", "cierre", ["cierra", "cerrar", "cierran"], "Querer que + subjunctive.", tr="The neighbors want the mayor to close the street.", lemma="cerrar:él:subj"),
        F("Los vecinos quieren ___ la calle.", "cerrar", ["cierren", "cierran", "cierre"], "Same subject: infinitive.", tr="The neighbors want to close the street."),
        F("El alcalde dice que la calle ___ cerrada.", "está", ["esté", "estar", "estamos"], "Reporting a fact: indicative.", tr="The mayor says that the street is closed.", lemma="estar:ella"),
        F("El alcalde le dice a la policía que ___ la calle.", "cierre", ["cierra", "cerrar", "cierran"], "Telling someone to do something: subjunctive.", tr="The mayor tells the police to close the street.", lemma="cerrar:él:subj"),
        F("La ley prohíbe que los niños ___ en las tiendas de noche.", "trabajen", ["trabajan", "trabajar", "trabajamos"], "Prohibir que + subjunctive.", tr="The law forbids children to work in stores at night.", lemma="trabajar:ellos:subj"),
        F("La directora permite que los alumnos ___ el teléfono en el patio.", "usen", ["usan", "usar", "usamos"], "Permitir que + subjunctive.", tr="The principal allows the students to use their phones in the yard.", lemma="usar:ellos:subj"),
        F("Te recomiendo que ___ más agua.", "bebas", ["bebes", "beber", "bebo"], "Recomendar que + subjunctive.", tr="I recommend that you drink more water.", lemma="beber:tú:subj"),
        M("Which sentence is correct?", "Espero que mis amigos vengan hoy.", ["Espero que mis amigos vienen hoy.", "Espero mis amigos vengan hoy.", "Espero que mis amigos venir hoy."], "Esperar que + subjunctive."),
        M("Which sentence reports a fact?", "El juez dice que el acusado es inocente.", ["El juez dice que el acusado sea inocente.", "El juez manda que el acusado sea inocente.", "El juez quiere que el acusado sea inocente."], "Decir que + indicative for a fact."),
    ],
)

# ---------------------------------------------------------------------------- 618
L618 = lesson(
    "Review E: emotions and gustar-type verbs",
    "La directora está contenta de que los estudiantes participen.",
    requires=["contento", "temer", "molestar", "preocupar", "sorprender", "alegrar", "lamentar", "directora", "estudiante", "participar", "tráfico", "agua"],
    cards=[
        card("Two families of emotion expressions",
             "1) Subject + verb: alegrarse de que, estar contento de que, sentir que (= to be sorry that), lamentar que, temer que, tener miedo de que. "
             "2) Pronoun + verb: me preocupa que, nos sorprende que, le molesta que, les indigna que. "
             "In both families, different subjects → que + subjunctive; the same subject → infinitive.",
             examples=[
                 ex("La directora está contenta de que los estudiantes participen.", "The principal is happy that the students take part.", "participen"),
                 ex("Los médicos temen que la gente no haga ejercicio.", "Doctors fear that people do not exercise.", "haga"),
                 ex("Me molesta que haya tanto tráfico en la ciudad.", "It bothers me that there is so much traffic in the city.", "haya"),
                 ex("A los vecinos les preocupa que el río tenga poca agua.", "It worries the neighbors that the river has little water.", "tenga"),
             ]),
    ],
    exercises=[
        F("La directora está contenta de que los estudiantes ___.", "participen", ["participan", "participar", "participamos"], "Estar contento de que + subjunctive.", tr="The principal is happy that the students take part.", lemma="participar:ellos:subj"),
        F("Los médicos temen que la gente no ___ ejercicio.", "haga", ["hace", "hacer", "hacen"], "Temer que + subjunctive.", tr="Doctors fear that people do not exercise.", lemma="hacer:ella:subj"),
        F("Me molesta que ___ tanto tráfico en la ciudad.", "haya", ["hay", "haber", "han"], "Molestar que + subjunctive.", tr="It bothers me that there is so much traffic in the city.", lemma="haber:él:subj"),
        F("A los vecinos les preocupa que el río ___ poca agua.", "tenga", ["tiene", "tener", "tienen"], "Preocupar que + subjunctive.", tr="It worries the neighbors that the river has little water.", lemma="tener:él:subj"),
        F("A mis padres les sorprende que yo ___ tan temprano.", "llegue", ["llego", "llegar", "llega"], "Sorprender que + subjunctive.", tr="It surprises my parents that I arrive so early.", lemma="llegar:yo:subj"),
        F("Me alegro de ___ con ustedes hoy.", "estar", ["esté", "estoy", "estamos"], "Same subject: infinitive.", tr="I am glad to be with you today."),
        F("Lamentamos que el servicio no ___ hoy.", "funcione", ["funciona", "funcionar", "funcionan"], "Lamentar que + subjunctive.", tr="We regret that the service is not working today.", lemma="funcionar:él:subj"),
        M("Which sentence is correct?", "A ella le encantan los museos.", ["A ella le encanta los museos.", "A ella la encantan los museos.", "A ella encantan los museos."], "Museos is plural: encantan."),
        M("Which sentence uses the infinitive correctly?", "Tengo miedo de perder el trabajo.", ["Tengo miedo de que perder el trabajo.", "Tengo miedo que pierdo el trabajo.", "Tengo miedo de pierda el trabajo."], "Same subject: infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 619
L619 = lesson(
    "Review I: impersonal expressions",
    "Es terrible que los presos se escapen. Es bueno rastrear a los criminales.",
    requires=["terrible", "bueno", "importante", "esencial", "increíble", "extraño", "preso", "cárcel", "criminal", "policía", "prensa", "violencia"],
    cards=[
        card("Opinion without a subject",
             "An impersonal expression takes the subjunctive when a new subject follows after que, and the infinitive when no one in particular is named. "
             "Expressions of fact (es verdad que, es evidente que) take the indicative.",
             tables=[table(["General: infinitive", "New subject: subjunctive"],
                           [["Es bueno rastrear a los criminales.", "Es bueno que la policía rastree a los criminales."],
                            ["Es esencial reformar las cárceles.", "Es esencial que el gobierno reforme las cárceles."],
                            ["Es una lástima perder tanto tiempo.", "Es una lástima que perdamos tanto tiempo."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Es terrible que los presos se ___ de la cárcel.", "escapen", ["escapan", "escapar", "escapamos"], "Es terrible que + subjunctive.", tr="It is terrible that prisoners escape from jail.", lemma="escapar:ellos:subj"),
        F("Es bueno que la policía ___ a los criminales.", "rastree", ["rastrea", "rastrear", "rastrean"], "Es bueno que + subjunctive.", tr="It is good that the police track criminals.", lemma="rastrear:ella:subj"),
        F("Es bueno ___ a los criminales.", "rastrear", ["rastree", "rastrea", "rastrean"], "General: infinitive.", tr="It is good to track criminals."),
        F("Es esencial que el gobierno ___ las cárceles.", "reforme", ["reforma", "reformar", "reforman"], "Es esencial que + subjunctive.", tr="It is essential that the government reform the jails.", lemma="reformar:él:subj"),
        F("Es increíble que la prensa ___ tantos detalles del crimen.", "publique", ["publica", "publicar", "publican"], "Es increíble que + subjunctive.", tr="It is incredible that the press publishes so many details of the crime.", lemma="publicar:ella:subj"),
        F("Es evidente que la violencia ___ en la región.", "aumenta", ["aumente", "aumentar", "aumentan"], "Es evidente que: indicative.", tr="It is evident that violence is rising in the region.", lemma="aumentar:ella"),
        F("Es importante que nosotros ___ a las víctimas.", "escuchemos", ["escuchamos", "escuchar", "escuchen"], "Es importante que + subjunctive.", tr="It is important that we listen to the victims.", lemma="escuchar:nosotros:subj"),
        M("Which sentence is correct?", "Es extraño que no haya nadie en la calle.", ["Es extraño que no hay nadie en la calle.", "Es extraño que no haber nadie en la calle.", "Es extraño no que haya nadie en la calle."], "Es extraño que + subjunctive."),
        M("Which sentence is general (no specific subject)?", "Es esencial reformar las cárceles.", ["Es esencial que reformemos las cárceles.", "Es esencial que ellos reformen las cárceles.", "Es esencial que tú reformes las cárceles."], "No que clause."),
    ],
)

# ---------------------------------------------------------------------------- 620
L620 = lesson(
    "Review D and N: doubt, denial and negation",
    "Dudo que el país sea rico. Creo que el país será rico.",
    requires=["dudar", "negar", "creer", "pensar", "seguro", "economía", "gobierno", "candidato", "país", "crisis", "empleo", "propuesta"],
    cards=[
        card("A candidate's opinions (invented)",
             "A voter listens to a candidate. Belief and certainty use the indicative (or the future); doubt, denial and disbelief use the subjunctive.",
             examples=[
                 ex("El candidato no cree que la economía mejore este año.", "The candidate does not believe that the economy will improve this year.", "mejore"),
                 ex("Cree que el gobierno no hará nada para crear empleos.", "He believes that the government will do nothing to create jobs.", "hará"),
                 ex("Duda que el país salga de la crisis pronto.", "He doubts that the country will get out of the crisis soon.", "salga"),
                 ex("Está seguro de que las propuestas del gobierno no funcionarán.", "He is sure that the government's proposals will not work.", "funcionarán"),
                 ex("Niega que el presidente conozca los problemas reales.", "He denies that the president knows the real problems.", "conozca"),
                 ex("No piensa que el presidente vaya a cumplir sus promesas.", "He does not think the president is going to keep his promises.", "vaya"),
             ]),
    ],
    exercises=[
        F("El candidato no cree que la economía ___ este año.", "mejore", ["mejora", "mejorar", "mejoramos"], "No creer que + subjunctive.", tr="The candidate does not believe that the economy will improve this year.", lemma="mejorar:ella:subj"),
        F("Cree que el gobierno no ___ nada para crear empleos.", "hará", ["haga", "hacer", "hace"], "Creer que: indicative/future.", tr="He believes that the government will do nothing to create jobs.", lemma="hacer:él:fut"),
        F("Duda que el país ___ de la crisis pronto.", "salga", ["sale", "salir", "salgan"], "Dudar que + subjunctive.", tr="He doubts that the country will get out of the crisis soon.", lemma="salir:él:subj"),
        F("Está seguro de que las propuestas del gobierno no ___.", "funcionarán", ["funcionen", "funcionar", "funciona"], "Estar seguro de que: future.", tr="He is sure that the government's proposals will not work.", lemma="funcionar:ellas:fut"),
        F("Niega que el presidente ___ los problemas reales.", "conozca", ["conoce", "conocer", "conocen"], "Negar que + subjunctive.", tr="He denies that the president knows the real problems.", lemma="conocer:él:subj"),
        F("No piensa que el presidente ___ a cumplir sus promesas.", "vaya", ["vamos", "ir", "vayan"], "No pensar que + subjunctive.", tr="He does not think the president is going to keep his promises.", lemma="ir:él:subj"),
        F("No hay duda de que el candidato ___ buenas ideas.", "tiene", ["tenga", "tener", "tienen"], "No hay duda de que: indicative.", tr="There is no doubt that the candidate has good ideas.", lemma="tener:él"),
        M("Which sentence is correct?", "No creo que el plan funcione.", ["No creo que el plan funciona.", "No creo que el plan funcionar.", "No creo el plan funcione."], "No creer que + subjunctive."),
        M("Which expression takes the indicative?", "estoy seguro de que", ["no estoy seguro de que", "dudo que", "niego que"], "Certainty."),
    ],
)

# ---------------------------------------------------------------------------- 621
L621 = lesson(
    "Review G: ojalá, tal vez, quizás, puede que (an interview)",
    "Quizá suban las becas. Ojalá que el Congreso se ponga de acuerdo.",
    requires=["ojalá", "quizá", "tal", "vez", "subir", "necesitar", "congreso", "unir", "saber", "ser", "estudiante", "presupuesto"],
    cards=[
        card("Interview with a deputy (invented)",
             "A journalist asks a deputy about scholarships for university students. The deputy answers cautiously, using expressions of probability and hope (subjunctive) and a fact (indicative).",
             examples=[
                 ex("Periodista: Diputado, ¿cree que subirán las becas el próximo año?", "Journalist: Deputy, do you think scholarships will go up next year?", "subirán"),
                 ex("Diputado: Eso es difícil de asegurar. Quizá suban, pero el problema es más grande.", "Deputy: That is hard to say for sure. Maybe they will go up, but the problem is bigger.", "suban"),
                 ex("Es un hecho que los estudiantes necesitan más ayuda ahora mismo.", "It is a fact that students need more help right now.", "necesitan"),
                 ex("Ojalá que el Congreso se ponga de acuerdo.", "I hope Congress agrees.", "ponga"),
                 ex("Puede que el dinero sea una ayuda, pero no es suficiente.", "The money may help, but it is not enough.", "sea"),
                 ex("Tal vez el gobierno aumente el presupuesto, pero todavía no hay una decisión.", "Perhaps the government will increase the budget, but there is no decision yet.", "aumente"),
                 ex("Periodista: Ojalá que el presidente sepa unir al Congreso.", "Journalist: I hope the president knows how to unite Congress.", "sepa"),
             ]),
    ],
    exercises=[
        F("Quizá las becas ___ el próximo año.", "suban", ["subimos", "subir", "subiendo"], "Quizá + subjunctive (the most common choice when you are unsure).", tr="Maybe the scholarships will go up next year.", lemma="subir:ellas:subj"),
        F("Es un hecho que los estudiantes ___ más ayuda.", "necesitan", ["necesiten", "necesitar", "necesitamos"], "A fact: indicative.", tr="It is a fact that students need more help.", lemma="necesitar:ellos"),
        F("Ojalá que el Congreso se ___ de acuerdo.", "ponga", ["pone", "poner", "ponen"], "Ojalá que + subjunctive.", tr="I hope Congress comes to an agreement.", lemma="poner:él:subj"),
        F("Puede que el dinero ___ una ayuda.", "sea", ["es", "ser", "son"], "Puede que + subjunctive.", tr="The money may be a help.", lemma="ser:él:subj"),
        F("Tal vez el gobierno ___ el presupuesto.", "aumente", ["aumentamos", "aumentar", "aumentan"], "Tal vez + subjunctive (the most common choice when you are unsure).", tr="Perhaps the government will increase the budget.", lemma="aumentar:él:subj"),
        F("Ojalá que el presidente ___ unir al Congreso.", "sepa", ["sabe", "saber", "saben"], "Ojalá que + subjunctive.", tr="I hope the president knows how to unite Congress.", lemma="saber:él:subj"),
        F("A lo mejor la reunión ___ mañana.", "es", ["sea", "ser", "son"], "A lo mejor + indicative.", tr="Maybe the meeting is tomorrow.", lemma="ser:ella"),
        M("Which expression takes the indicative?", "a lo mejor", ["tal vez", "ojalá que", "puede que"], "A lo mejor always takes the indicative; tal vez usually takes the subjunctive."),
        M("Which sentence is correct?", "Quizá lleguen mañana.", ["Quizá nosotros llegan mañana.", "Quizá llegar mañana.", "Quizá que lleguen mañana."], "Quizá + subjunctive (the most common choice when you are unsure)."),
    ],
)

# ---------------------------------------------------------------------------- 622
L622 = lesson(
    "Review: irregular and stem-changing subjunctives",
    "dé, vaya, esté, haya, sepa, sea · empiece, vuelva, pida, duerma",
    requires=["dar", "ir", "estar", "haber", "saber", "ser", "empezar", "volver", "pedir", "dormir", "seguir", "traer"],
    cards=[
        card("Two groups to remember",
             "Six verbs do not build the subjunctive from the yo form: dar (dé), ir (vaya), estar (esté), haber (haya), saber (sepa), ser (sea). "
             "Stem changers keep their change except -ar/-er in nosotros and vosotros; -ir verbs change e→i and o→u there (pidamos, durmamos).",
             tables=[table(["Infinitivo", "que él", "que nosotros"],
                           [["dar", "dé", "demos"],
                            ["ir", "vaya", "vayamos"],
                            ["empezar", "empiece", "empecemos"],
                            ["volver", "vuelva", "volvamos"],
                            ["pedir", "pida", "pidamos"],
                            ["dormir", "duerma", "durmamos"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Es necesario que ella nos ___ más información.", "dé", ["da", "dar", "den"], "Es necesario que + subjunctive.", tr="It is necessary that she give us more information.", lemma="dar:ella:subj"),
        F("Ojalá que nosotros ___ juntos a la reunión.", "vayamos", ["vamos", "ir", "vayan"], "Ojalá que + subjunctive.", tr="I hope we go to the meeting together.", lemma="ir:nosotros:subj"),
        F("Dudo que la película ___ a las ocho.", "empiece", ["empieza", "empezar", "empiezan"], "Dudar que + subjunctive.", tr="I doubt that the movie starts at eight.", lemma="empezar:ella:subj"),
        F("Quiero que nosotros ___ temprano.", "volvamos", ["volvemos", "volver", "vuelvan"], "Querer que + subjunctive.", tr="I want us to return early.", lemma="volver:nosotros:subj"),
        F("Te sugiero que le ___ ayuda a tu hermano.", "pidas", ["pides", "pedir", "pida"], "Sugerir que + subjunctive; tú.", tr="I suggest that you ask your brother for help.", lemma="pedir:tú:subj"),
        F("Es importante que los bebés ___ mucho.", "duerman", ["duermen", "dormir", "dormimos"], "Es importante que + subjunctive.", tr="It is important that babies sleep a lot.", lemma="dormir:ellos:subj"),
        F("Ojalá que ustedes ___ muy felices.", "sean", ["son", "ser", "seamos"], "Ojalá que + subjunctive.", tr="I hope you are very happy.", lemma="ser:ustedes:subj"),
        M("Which is the subjunctive of “saber” for yo?", "sepa", ["sabo", "sé", "sepe"], "Saber → sepa."),
        M("Which is the subjunctive of “estar” for tú?", "estés", ["estás", "estes", "esté"], "Estar → estés."),
    ],
)

# ---------------------------------------------------------------------------- 623
L623 = lesson(
    "Which form? Indicative, subjunctive, infinitive or future",
    "Sé que viene. Dudo que venga. Quiero venir. Vendrá.",
    requires=["saber", "dudar", "querer", "creer", "esperar", "venir", "estar", "hacer", "ver", "ojalá", "importante", "seguro"],
    cards=[
        card("A checklist",
             "1) Does the main clause state a fact, belief or certainty (sé que, creo que, veo que, estoy seguro de que, es verdad que)? → indicative or future. "
             "2) Does it express a wish, emotion, doubt, denial, value judgment (es bueno que, es importante que), probability or order, and are the subjects different? → subjunctive. "
             "3) Same subject? → infinitive. 4) Plain prediction or promise? → future tense.",
             tables=[table(["Pregunta", "Resultado"],
                           [["¿Hecho o creencia?", "Sé que ella viene."],
                            ["¿Deseo o duda con otro sujeto?", "Dudo que ella venga."],
                            ["¿Mismo sujeto?", "Quiero venir."],
                            ["¿Predicción?", "Ella vendrá mañana."]],
                           say=[1])]),
    ],
    exercises=[
        F("Sé que mis primos ___ en Quito.", "viven", ["vivan", "vivir", "vivimos"], "Saber que: indicative.", tr="I know that my cousins live in Quito.", lemma="vivir:ellos"),
        F("Espero que mis primos ___ en Quito.", "vivan", ["viven", "vivir", "vivimos"], "Esperar que: subjunctive.", tr="I hope my cousins live in Quito.", lemma="vivir:ellos:subj"),
        F("Espero ___ en Quito.", "vivir", ["vivo", "viva", "vive"], "Same subject: infinitive.", tr="I hope to live in Quito."),
        F("Mañana mis primos ___ a Quito.", "llegarán", ["lleguen", "llegar", "llegaron"], "A prediction: future.", tr="Tomorrow my cousins will arrive in Quito.", lemma="llegar:ellos:fut"),
        F("Veo que el parque ___ muy limpio.", "está", ["esté", "estar", "estamos"], "Ver que: indicative.", tr="I see that the park is very clean.", lemma="estar:él"),
        F("Es importante que el parque ___ limpio.", "esté", ["está", "estar", "estamos"], "Es importante que: subjunctive.", tr="It is important that the park be clean.", lemma="estar:él:subj"),
        F("Estoy seguro de que ellos ___ la verdad.", "dicen", ["digan", "decir", "decimos"], "Estar seguro de que: indicative.", tr="I am sure that they are telling the truth.", lemma="decir:ellos"),
        M("Which sentence is correct?", "No dudo que ella tiene razón.", ["No dudo que ella tienes razón.", "No dudo que ella tener razón.", "No dudo ella tiene razón."], "No dudar que expresses certainty, so the indicative is normal here (the subjunctive is also heard)."),
        M("Which sentence is correct?", "Ojalá que ella tenga razón.", ["Ojalá que ella tiene razón.", "Ojalá que ella tener razón.", "Ojalá ella tendrá razón."], "Ojalá que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 624
L624 = lesson(
    "Speaking practice: finish the opinion",
    "Anhelo que el terrorismo desaparezca. Me preocupa que los terroristas…",
    requires=["esperar", "preocupar", "molestar", "importante", "creer", "ojalá", "dudar", "necesario", "terrorismo", "narcotráfico", "gobierno", "futuro"],
    cards=[
        card("Complete the sentence",
             "Practice giving opinions on the big themes of Units 26 to 29: terrorism, the drug trade, the armed forces, and cybercrime and trafficking. "
             "Each opening phrase decides the mood of the verb that follows.",
             tables=[table(["Tema", "Frase para completar"],
                           [["El terrorismo", "Anhelo que el terrorismo desaparezca."],
                            ["El narcotráfico", "Me molesta que los narcotraficantes tengan tanto poder."],
                            ["La trata de personas", "Es urgente que los gobiernos protejan a las víctimas."],
                            ["Los delitos cibernéticos", "Dudo que en el futuro haya una seguridad perfecta."]],
                           say=[1])]),
    ],
    exercises=[
        M("Anhelo que el terrorismo…", "desaparezca", ["desaparece", "desaparecer", "desaparecerá"], "Anhelar que + subjunctive."),
        M("Me preocupa que los terroristas…", "usen internet para reclutar gente", ["usan internet para reclutar gente", "usar internet para reclutar gente", "usarán internet para reclutar gente"], "Preocupar que + subjunctive."),
        M("Es indispensable que el gobierno…", "proteja a los ciudadanos", ["protege a los ciudadanos", "proteger a los ciudadanos", "protegerá a los ciudadanos"], "Es indispensable que + subjunctive."),
        M("No creo que el terrorismo…", "termine pronto", ["termina pronto", "terminar pronto", "terminen pronto"], "No creer que + subjunctive."),
        M("Ojalá que en un futuro…", "haya más paz", ["hay más paz", "haber más paz", "habrá más paz"], "Ojalá que + subjunctive."),
        M("Me indigna que los traficantes…", "engañen a la gente", ["engañan a la gente", "engañar a la gente", "engañarán a la gente"], "Indignar que + subjunctive."),
        M("Es urgente que los medios de comunicación…", "informen con responsabilidad", ["informan con responsabilidad", "informar con responsabilidad", "informarán con responsabilidad"], "Es urgente que + subjunctive."),
        M("Tengo miedo de que mi familia…", "reciba un mensaje falso", ["recibe un mensaje falso", "recibir un mensaje falso", "recibirá un mensaje falso"], "Tener miedo de que + subjunctive."),
        M("Dudo que en un futuro…", "los delitos cibernéticos desaparezcan", ["los delitos cibernéticos desaparecen", "los delitos cibernéticos desaparecer", "los delitos cibernéticos desaparezca"], "Dudar que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 625
L625 = lesson(
    "Vocabulary review: terrorism and armed groups (Unit 26)",
    "el atentado, la tregua, el acuerdo de paz, la víctima",
    requires=["atentado", "terrorismo", "víctima", "paz", "acuerdo", "grupo", "armado", "gobierno", "verdad", "guerra", "violencia", "sospechoso"],
    cards=[
        card("Word families",
             "Attacks: el atentado, el ataque, la víctima, el herido, el sospechoso, el explosivo. Peace talks: la tregua, el alto el fuego, el acuerdo de paz, la desmovilización, el diálogo. "
             "Groups: el grupo armado, la guerrilla, la organización terrorista. Memory and justice: la verdad, la memoria, la reparación a las víctimas.",
             examples=[
                 ex("El gobierno y el grupo armado firmaron un acuerdo de paz.", "The government and the armed group signed a peace accord.", "firmaron"),
                 ex("Las víctimas quieren conocer la verdad.", "The victims want to know the truth.", "conocer"),
             ]),
    ],
    exercises=[
        F("Las ___ del atentado recibieron ayuda.", "víctimas", ["treguas", "guerrillas", "verdades"], "Victims.", tr="The victims of the attack received help."),
        F("El gobierno y el grupo armado firmaron un acuerdo de ___.", "paz", ["guerra", "odio", "miedo"], "Peace accord.", tr="The government and the armed group signed a peace accord."),
        F("Una ___ es una pausa en los combates por un tiempo.", "tregua", ["víctima", "verdad", "memoria"], "Truce.", tr="A truce is a pause in the fighting for a time."),
        F("La policía detuvo a un ___.", "sospechoso", ["acuerdo", "grupo", "diálogo"], "Suspect.", tr="The police arrested a suspect."),
        F("Después del ataque, había muchos ___ en el hospital.", "heridos", ["acuerdos", "grupos", "diálogos"], "The injured.", tr="After the attack there were many injured people at the hospital."),
        F("Los líderes ___ el atentado.", "condenaron", ["condenó", "condenan", "condenar"], "Plural subject; finished past.", tr="The leaders condemned the attack.", lemma="condenar:ellos:pret"),
        M("What does “el alto el fuego” mean?", "ceasefire", ["fire alarm", "high flame", "fireplace"], "Ceasefire."),
        M("Which noun is the best translation of “peace talks”?", "diálogo de paz", ["ataque de paz", "grupo de paz", "odio de paz"], "Diálogo de paz."),
        M("Which expression means “to spread terror”?", "sembrar el terror", ["firmar el acuerdo", "abrir el diálogo", "cerrar el caso"], "Sembrar el terror."),
    ],
)

# ---------------------------------------------------------------------------- 626
L626 = lesson(
    "Vocabulary review: the drug trade and justice (Unit 27)",
    "el cártel, el cabecilla, el cargamento, la extradición",
    requires=["droga", "narcotráfico", "capturar", "frontera", "jefe", "juez", "acusado", "condena", "corrupción", "policía", "banda", "violencia"],
    cards=[
        card("Word families",
             "Trade: la droga, el narcotráfico, el cártel, el cargamento, la ruta. People: el narcotraficante, el cabecilla, el prófugo, el pandillero, el sicario. "
             "Police and court: incautar, decomisar, capturar, la aprehensión, el acusado, la condena, la extradición. Corruption: el soborno, el testaferro, el lavado de dinero.",
             examples=[
                 ex("Las autoridades decomisaron un cargamento en la frontera.", "The authorities seized a shipment at the border.", "decomisaron"),
                 ex("El juez dictó una condena muy larga.", "The judge handed down a very long sentence.", "dictó"),
             ]),
    ],
    exercises=[
        F("Las autoridades ___ un cargamento en la frontera.", "decomisaron", ["decomisó", "decomisan", "decomisar"], "Plural subject; finished past.", tr="The authorities seized a shipment at the border.", lemma="decomisar:ellos:pret"),
        F("El ___ de la banda se dio a la fuga.", "cabecilla", ["acusado", "cargamento", "testigo"], "Ringleader.", tr="The ringleader of the gang fled."),
        F("La policía busca a un ___ que se escapó de la cárcel.", "prófugo", ["juez", "soborno", "testigo"], "Fugitive.", tr="The police are looking for a fugitive who escaped from jail."),
        F("El juez ___ una condena muy larga.", "dictó", ["dictaron", "dicta", "dictar"], "Singular subject; finished past.", tr="The judge handed down a very long sentence.", lemma="dictar:él:pret"),
        F("Un funcionario aceptó un ___.", "soborno", ["cargamento", "cártel", "condena"], "Bribe.", tr="An official accepted a bribe."),
        F("El ___ negó todos los cargos.", "acusado", ["cargamento", "cártel", "soborno"], "Defendant.", tr="The defendant denied all the charges."),
        M("What does “el lavado de dinero” mean?", "money laundering", ["money transfer", "washing machine", "loan"], "Money laundering."),
        M("What does “la extradición” mean?", "handing a person over to another country to be tried or to serve a sentence", ["a new law", "a kind of prison", "a police dog"], "Extradition."),
        M("Which noun names a hired killer?", "sicario", ["pandillero", "testigo", "cabecilla"], "Sicario."),
    ],
)

# ---------------------------------------------------------------------------- 627
L627 = lesson(
    "Review: armed forces, aid and history (Unit 28)",
    "La ayuda humanitaria, la escuela, el plan, el canal",
    requires=["ayuda", "humanitario", "escuela", "plan", "canal", "fuerza", "armado", "mujer", "paz", "crisis", "historia", "país"],
    cards=[
        card("Key ideas",
             "Roles: ayuda humanitaria, mantenimiento de la paz, apoyo a la policía, defensa del país. Places and history: SOUTHCOM, la Escuela de las Américas (fundada en mil novecientos cuarenta y seis), el Plan Colombia, el Canal de Panamá, Costa Rica y Panamá sin ejército. "
             "Expressions: perder los estribos, no hay moros en la costa, armarse la de San Quintín, cumplir con la ley.",
             examples=[
                 ex("Las fuerzas armadas ayudan después de los huracanes.", "The armed forces help after hurricanes.", "ayudan"),
                 ex("Costa Rica y Panamá no tienen ejército.", "Costa Rica and Panama have no army.", "no tienen"),
             ]),
    ],
    exercises=[
        F("Después del huracán, los soldados ___ agua y comida.", "llevaron", ["llevó", "llevan", "llevar"], "Plural subject; finished past.", tr="After the hurricane, the soldiers took water and food.", lemma="llevar:ellos:pret"),
        F("El Plan Colombia ___ un programa de cooperación.", "fue", ["fueron", "es", "ser"], "Singular subject; finished past.", tr="Plan Colombia was a cooperation program.", lemma="ser:él:pret"),
        F("Costa Rica y Panamá no ___ ejército.", "tienen", ["tiene", "tener", "tenemos"], "Plural subject, present.", tr="Costa Rica and Panama do not have an army.", lemma="tener:ellos"),
        F("El profesor ___ los estribos con el estudiante.", "perdió", ["perdieron", "pierde", "perder"], "Singular subject; finished past.", tr="The professor lost his temper with the student.", lemma="perder:él:pret"),
        F("Todos tenemos que ___ con la ley.", "cumplir", ["cumplo", "cumple", "cumplen"], "Tener que + infinitive.", tr="We all have to abide by the law."),
        F("Es importante que las fuerzas armadas ___ los derechos de todos.", "respeten", ["respetan", "respetar", "respetamos"], "Es importante que + subjunctive.", tr="It is important that the armed forces respect everyone's rights.", lemma="respetar:ellos:subj"),
        M("Where was the School of the Americas founded?", "In Panama", ["In Colombia", "In Georgia", "In Cuba"], "En Panamá, en mil novecientos cuarenta y seis."),
        M("Which U.S. command covers Mexico?", "Northern Command (Comando Norte)", ["SOUTHCOM", "Eastern Command (Comando Este)", "No command"], "México pertenece al Comando Norte."),
        M("Which idiom means “the coast is clear”?", "no hay moros en la costa", ["perder los estribos", "armarse la de San Quintín", "cruzarse de brazos"], "No hay moros en la costa."),
    ],
)

# ---------------------------------------------------------------------------- 628
L628 = lesson(
    "Review: cybercrime and money crimes (Unit 29)",
    "el ransomware, la criptomoneda, el paraíso fiscal, la trata de personas",
    requires=["virus", "rescate", "dinero", "banco", "impuesto", "ley", "empresa", "usuario", "información", "víctima", "ayuda", "seguridad"],
    cards=[
        card("Key ideas",
             "Cyber: virus, gusano, troyano, programa espía, ransomware, phishing, antivirus; hackers and hacktivists. Money: criptomoneda, paraíso fiscal, sociedad offshore, evasión fiscal, lavado de dinero, soborno, filtración. "
             "People: denunciante, víctima, traficante. Expressions: cruzarse de brazos, hacerse de la vista gorda, hacerse pasar por, quedarse corto.",
             examples=[
                 ex("El ransomware bloquea los archivos y pide un rescate.", "Ransomware blocks the files and demands a ransom.", "bloquea"),
                 ex("Es esencial que las víctimas de la trata reciban ayuda.", "It is essential that trafficking victims receive help.", "reciban"),
             ]),
    ],
    exercises=[
        F("El ransomware ___ los archivos y pide un rescate.", "bloquea", ["bloquean", "bloquear", "bloqueamos"], "Singular subject, present.", tr="Ransomware blocks the files and demands a ransom.", lemma="bloquear:él"),
        F("Es esencial que las víctimas de la trata ___ ayuda.", "reciban", ["reciben", "recibir", "recibimos"], "Es esencial que + subjunctive.", tr="It is essential that trafficking victims receive help.", lemma="recibir:ellos:subj"),
        F("Un paraíso ___ cobra pocos impuestos.", "fiscal", ["virus", "rescate", "usuario"], "Tax haven.", tr="A tax haven charges few taxes."),
        F("No creo que esa oferta ___ real.", "sea", ["es", "ser", "son"], "No creer que + subjunctive.", tr="I don't think that offer is real.", lemma="ser:ella:subj"),
        F("Dudo que los precios ___ pronto.", "bajen", ["bajan", "bajar", "bajamos"], "Dudar que + subjunctive.", tr="I doubt that prices will go down soon.", lemma="bajar:ellos:subj"),
        F("Un hombre se hizo ___ por empleado del banco.", "pasar", ["pasado", "pasa", "pasan"], "Hacerse pasar por.", tr="A man posed as a bank employee."),
        M("Which tip protects your accounts?", "Usa una contraseña distinta para cada servicio.", ["Comparte tu clave con todos.", "Abre todos los enlaces.", "No actualices nada."], "Different password for each service."),
        M("What is a “denunciante”?", "a whistleblower", ["a virus", "a banker", "a tax"], "Denunciante = whistleblower."),
        M("Which expression means “to turn a blind eye”?", "hacerse de la vista gorda", ["cruzarse de brazos", "quedarse corto", "hacerse pasar por"], "Hacerse de la vista gorda."),
    ],
)

# ---------------------------------------------------------------------------- 629
L629 = lesson(
    "Unit review: four themes in one text",
    "Hoy el mundo enfrenta el terrorismo, las drogas, la violencia y los delitos de internet.",
    requires=["mundo", "terrorismo", "droga", "violencia", "internet", "gobierno", "ciudadano", "justicia", "esperar", "ojalá", "importante", "dudar"],
    cards=[
        card("A summary text (practice)",
             "This invented text brings together the themes of Units 26 to 29. Find the indicative (facts), the subjunctive (value judgments, wishes, emotions, doubts) and the pronouns.",
             examples=[
                 ex("Hoy muchos países enfrentan problemas parecidos: el terrorismo, las drogas, la violencia y los delitos de internet.", "Today many countries face similar problems: terrorism, drugs, violence and Internet crimes.", "enfrentan"),
                 ex("Es verdad que ningún gobierno puede resolverlos solo.", "It is true that no government can solve them alone.", "puede"),
                 ex("Por eso es necesario que los países cooperen y que compartan información.", "That is why it is necessary that countries cooperate and share information.", "cooperen"),
                 ex("Las víctimas esperan que la justicia les diga la verdad y que alguien se la cuente con honestidad.", "Victims hope that justice tells them the truth and that someone tells it to them honestly.", "se la cuente"),
                 ex("Me preocupa que algunas personas se hagan de la vista gorda ante la corrupción.", "It worries me that some people turn a blind eye to corruption.", "hagan"),
                 ex("Dudo que haya una solución fácil, pero creo que la cooperación ayudará.", "I doubt that there is an easy solution, but I believe that cooperation will help.", "ayudará"),
                 ex("Ojalá que los ciudadanos, los periodistas y los jóvenes participen en la búsqueda de soluciones.", "I hope that citizens, journalists and young people take part in the search for solutions.", "participen"),
             ]),
    ],
    exercises=[
        M("What problems are mentioned?", "Terrorism, drugs, violence and Internet crimes", ["Only sports", "Only weather", "Only taxes"], "El terrorismo, las drogas, la violencia y los delitos de internet."),
        M("What is necessary, according to the text?", "That countries cooperate and share information", ["That borders close", "That schools close", "That the press stop"], "Es necesario que los países cooperen."),
        M("What does the writer doubt?", "That there is an easy solution", ["That crime exists", "That cooperation exists", "That justice exists"], "Dudo que haya una solución fácil."),
        F("Es verdad que ningún gobierno ___ resolverlos solo.", "puede", ["pueda", "poder", "pueden"], "Es verdad que: indicative.", tr="It is true that no government can solve them alone.", lemma="poder:él"),
        F("Es necesario que los países ___ y compartan información.", "cooperen", ["cooperan", "cooperar", "cooperamos"], "Es necesario que + subjunctive.", tr="It is necessary that countries cooperate and share information.", lemma="cooperar:ellos:subj"),
        F("Las víctimas esperan que la justicia les ___ la verdad.", "diga", ["dice", "decir", "dicen"], "Esperar que + subjunctive.", tr="Victims hope that justice tells them the truth.", lemma="decir:ella:subj"),
        F("Me preocupa que algunas personas se ___ de la vista gorda.", "hagan", ["hacen", "hacer", "hacemos"], "Preocupar que + subjunctive.", tr="It worries me that some people turn a blind eye.", lemma="hacer:ellos:subj"),
        F("Creo que la cooperación ___.", "ayudará", ["ayude", "ayudar", "ayudan"], "Creer que: indicative/future.", tr="I believe that cooperation will help.", lemma="ayudar:ella:fut"),
        M("Which sentence is correct?", "Ojalá que los jóvenes participen.", ["Ojalá que los jóvenes participan.", "Ojalá que los jóvenes participar.", "Ojalá los jóvenes participarán."], "Ojalá que + subjunctive."),
    ],
)

UNIT = unit("Repaso: crimen, drogas, fuerzas armadas y ciberseguridad", [
    L612, L613, L614, L615, L616, L617, L618, L619, L620, L621, L622, L623, L624, L625, L626, L627, L628, L629,
])

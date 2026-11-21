"""Unit 9: daily routines (textbook Chapter 8)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 114
L114 = lesson(
    "My daily routine",
    "Me despierto, me levanto, me ducho, me acuesto",
    requires=["despertar", "levantar", "ducha", "dormir", "cara", "temprano"],
    cards=[
        card("From morning to night",
             "Daily routines use many reflexive verbs. You can recognize them in the infinitive by the -se at the "
             "end. For now, learn them as set phrases; the next lessons explain the grammar.",
             tables=[table(["Verbo", "English"],
                           [["despertarse", "to wake up"],
                            ["levantarse", "to get up"],
                            ["ducharse", "to take a shower"],
                            ["bañarse", "to take a bath or a shower"],
                            ["lavarse los dientes", "to brush your teeth"],
                            ["afeitarse", "to shave"],
                            ["peinarse", "to comb your hair"],
                            ["maquillarse", "to put on makeup"],
                            ["vestirse", "to get dressed"],
                            ["acostarse", "to go to bed"],
                            ["dormirse", "to fall asleep"]],
                           say=[0])]),
        card("When?",
             "Add the time with a and la hora: a las siete. Use por la mañana, por la tarde and por la noche for "
             "the parts of the day, and temprano (early) or tarde (late).",
             examples=[
                 ex("Me despierto a las seis y media.", "I wake up at six thirty.", "Me despierto"),
                 ex("Me levanto a las siete de la mañana.", "I get up at seven in the morning.", "Me levanto"),
                 ex("Me ducho por la mañana.", "I take a shower in the morning.", "Me ducho"),
                 ex("Me lavo los dientes antes de salir.", "I brush my teeth before leaving.", "Me lavo los dientes"),
                 ex("Me acuesto temprano los domingos.", "I go to bed early on Sundays.", "Me acuesto"),
             ]),
    ],
    exercises=[
        F("Me ___ a las siete de la mañana.", "levanto", ["levantas", "levanta", "levantamos"], "Me goes with yo: levanto.", tr="I get up at seven in the morning.", lemma="levantar:yo"),
        F("Me ___ a las seis y media.", "despierto", ["despiertas", "despierta", "despertamos"], "Despertar is e → ie: despierto.", tr="I wake up at six thirty.", lemma="despertar:yo"),
        F("Me ___ por la mañana para ir al trabajo.", "ducho", ["duchas", "ducha", "duchamos"], "Yo: ducho.", tr="I take a shower in the morning to go to work.", lemma="duchar:yo"),
        M("Which verb means “to shave”?", "afeitarse", ["peinarse", "vestirse", "dormirse"], "Afeitarse is to shave."),
        M("Which verb means “to get dressed”?", "vestirse", ["despertarse", "acostarse", "maquillarse"], "Vestirse is to get dressed."),
        M("Which phrase means “to brush your teeth”?", "lavarse los dientes", ["peinarse el pelo", "ducharse la cara", "acostarse temprano"], "Dientes are teeth."),
        M("Which of these usually happens last in the day?", "acostarse", ["despertarse", "levantarse", "desayunar"], "You go to bed at the end of the day."),
        M("How do you say “at seven in the morning”?", "a las siete de la mañana", ["en las siete de la mañana", "a la siete de la mañana", "por siete de la mañana"], "A las + hour."),
        M("What does “temprano” mean?", "early", ["late", "slowly", "always"], "Temprano is early; tarde is late."),
    ],
    verify=vp("levantar", "levanto", "levantas", "levanta", "levantamos", "levantáis", "levantan")
           + vp("despertar", "despierto", "despiertas", "despierta", "despertamos", "despertáis", "despiertan"),
)

# ---------------------------------------------------------------------------- 115
L115 = lesson(
    "Reflexive verbs and pronouns",
    "me, te, se, nos, os, se",
    requires=["levantar", "lavar", "vestir", "dormir", "mano", "cara"],
    cards=[
        card("The action comes back to the subject",
             "A reflexive verb is a verb with a reflexive pronoun: the person doing the action also receives it. "
             "In the infinitive the pronoun is the ending -se (levantarse, “to get oneself up”).",
             examples=[
                 ex("Yo me levanto a las siete.", "I get (myself) up at seven.", "Yo me levanto"),
                 ex("Carmen se cepilla los dientes.", "Carmen brushes her teeth.", "se cepilla"),
                 ex("Nosotros nos bañamos después de correr.", "We bathe after running.", "nos bañamos"),
             ]),
        card("Present tense of levantarse",
             "Put the pronoun that matches the subject in front of the verb. Then conjugate the verb as usual. "
             "The pronoun is a separate word before the verb.",
             tables=[table(["Subject", "Reflexive form"],
                           [["yo", "me levanto"],
                            ["tú", "te levantas"],
                            ["él, ella, usted", "se levanta"],
                            ["nosotros", "nos levantamos"],
                            ["vosotros", "os levantáis"],
                            ["ellos, ellas, ustedes", "se levantan"]],
                           say=[1])]),
    ],
    exercises=[
        F("Yo ___ levanto a las siete.", "me", ["te", "se", "nos"], "The pronoun matches the subject: yo → me.", tr="I get up at seven."),
        F("Tú ___ acuestas temprano.", "te", ["me", "se", "nos"], "Tú → te.", tr="You go to bed early."),
        F("Nosotros ___ vestimos rápido.", "nos", ["me", "se", "os"], "Nosotros → nos.", tr="We get dressed quickly."),
        F("Ella ___ peina antes de salir.", "se", ["me", "te", "nos"], "Ella → se.", tr="She combs her hair before going out."),
        F("Ustedes ___ bañan por la noche.", "se", ["me", "te", "nos"], "Ustedes → se.", tr="You (all) bathe at night."),
        F("Vosotros ___ laváis las manos.", "os", ["se", "nos", "te"], "Vosotros → os.", tr="You (all, Spain) wash your hands."),
        M("Which form is correct for “tú” with levantarse?", "te levantas", ["se levantas", "me levantas", "te levanta"], "Te + levantas."),
        M("Which sentence is reflexive?", "Me lavo las manos.", ["Lavo la ropa.", "Compro pan.", "Leo el periódico."], "The action returns to the subject."),
        M("What does the “se” at the end of “acostarse” show?", "that the verb is reflexive", ["that the subject is ellos", "that the verb is future", "that the verb is negative"], "-se marks a reflexive infinitive."),
    ],
    verify=vp("lavar", "lavo", "lavas", "lava", "lavamos", "laváis", "lavan"),
)

# ---------------------------------------------------------------------------- 116
L116 = lesson(
    "Where does the pronoun go?",
    "Me voy a levantar. Voy a levantarme. Estoy levantándome.",
    requires=["levantar", "querer", "poder", "ir", "estar", "dormir"],
    cards=[
        card("Before the verb, or attached",
             "With one verb, the pronoun goes before it: Me levanto. With two verbs (a conjugated one plus an "
             "infinitive or the -ndo form), you have a choice: put the pronoun before the first verb or attach it "
             "to the end of the second one.",
             tables=[table(["Before", "Attached"],
                           [["Me voy a levantar.", "Voy a levantarme."],
                            ["Me quiero bañar.", "Quiero bañarme."],
                            ["Te debes acostar.", "Debes acostarte."],
                            ["Me estoy peinando.", "Estoy peinándome."]],
                           say=[0, 1])]),
        card("Matching and accents",
             "The pronoun must always match the subject of the conjugated verb: Ellos quieren levantarse, never "
             "quieren levantarme. When a pronoun is attached to an -ndo form, add a written accent: peinando → "
             "peinándome, duchando → duchándose. With an infinitive no accent is needed.",
             examples=[
                 ex("Ellos quieren levantarse temprano.", "They want to get up early.", "levantarse"),
                 ex("Mi hermana está duchándose.", "My sister is taking a shower.", "duchándose"),
                 ex("No me quiero acostar todavía.", "I do not want to go to bed yet.", "No me quiero acostar"),
             ]),
    ],
    exercises=[
        F("Voy a ___ temprano.", "acostarme", ["acostarte", "acostarse", "acostarnos"], "Voy is yo: acostarme.", tr="I am going to go to bed early."),
        F("Ellos quieren ___ temprano.", "levantarse", ["levantarme", "levantarte", "levantarnos"], "Ellos is they: levantarse.", tr="They want to get up early."),
        F("Tú debes ___ pronto.", "acostarte", ["acostarme", "acostarse", "acostarnos"], "Tú → acostarte.", tr="You should go to bed soon."),
        F("Estoy ___ los dientes.", "lavándome", ["lavandome", "lavarme", "lavándose"], "With the -ndo form, add an accent: lavándome.", tr="I am brushing my teeth."),
        F("Ella está ___ en el baño.", "peinándose", ["peinandose", "peinarse", "peinándome"], "Ella → peinándose, with an accent.", tr="She is combing her hair in the bathroom."),
        M("Which sentence is correct?", "Me quiero bañar.", ["Quiero me bañar.", "Quiero bañar me.", "Me quiero bañarme."], "Put the pronoun before the first verb or attach it to the infinitive."),
        M("Which sentence means the same as “Me voy a duchar”?", "Voy a ducharme.", ["Voy a ducharse.", "Voy a ducharte.", "Me voy ducharme."], "The attached pronoun must match yo."),
        M("Which sentence is negative and correct?", "No me levanto temprano los domingos.", ["Me no levanto temprano los domingos.", "No levanto me temprano los domingos.", "Levanto no me temprano los domingos."], "No goes before the pronoun."),
        M("Why does “levantándose” have a written accent?", "Adding the pronoun would otherwise move the stress.", ["It marks a question.", "It shows the future.", "It shows the plural."], "The accent keeps the stress on the same syllable."),
    ],
)

# ---------------------------------------------------------------------------- 117
L117 = lesson(
    "Body, clothes and hygiene: use the article",
    "Me lavo las manos. Se pone la camisa.",
    requires=["cara", "mano", "pelo", "diente", "cabeza", "toalla"],
    cards=[
        card("Parts of the body",
             "Learn the nouns with their articles.",
             tables=[table(["Parte", "English"],
                           [["la cara", "face"],
                            ["la cabeza", "head"],
                            ["el pelo", "hair"],
                            ["los ojos", "eyes"],
                            ["los dientes", "teeth"],
                            ["las manos", "hands"],
                            ["los pies", "feet"],
                            ["el cuerpo", "body"]],
                           say=[0])]),
        card("The article, not “my”",
             "With reflexive verbs, parts of the body and clothes usually take the definite article (el, la, los, las), not "
             "mi, tu or su. The pronoun already tells us whose body it is. (A possessive appears only when it adds "
             "information, as in su chaqueta nueva.)",
             tables=[table(["Spanish", "English"],
                           [["Pablo se lava la cara y las manos.", "Pablo washes his face and hands."],
                            ["Me cepillo los dientes.", "I brush my teeth."],
                            ["Después se pone los calcetines.", "Then he puts on his socks."]],
                           say=[0])]),
        card("Things for getting ready",
             "Some useful objects for personal care.",
             tables=[table(["Objeto", "English"],
                           [["la toalla", "towel"],
                            ["el jabón", "soap"],
                            ["el peine", "comb"],
                            ["el cepillo de dientes", "toothbrush"],
                            ["la pasta de dientes", "toothpaste"],
                            ["el champú", "shampoo"]],
                           say=[0])]),
    ],
    exercises=[
        F("Marta se lava ___ manos.", "las", ["sus", "mis", "unas"], "Body parts take the article: las manos.", tr="Marta washes her hands."),
        F("Me cepillo ___ dientes después de comer.", "los", ["mis", "unos", "nuestros"], "Los dientes.", tr="I brush my teeth after eating."),
        F("Mi hermano se pone ___ chaqueta.", "la", ["un", "las", "el"], "Clothes also take the article, and chaqueta is feminine singular.", tr="My brother puts on his jacket."),
        F("Te lavas ___ cara todas las mañanas.", "la", ["tu", "el", "las"], "La cara.", tr="You wash your face every morning."),
        M("How do you say “I wash my hands”?", "Me lavo las manos.", ["Lavo mis manos.", "Me lavo mis manos.", "Me lavo manos."], "Reflexive verb + article."),
        M("Which noun is feminine?", "la cabeza", ["el pelo", "el cuerpo", "el jabón"], "Cabeza ends in -a."),
        M("What do you use to dry yourself after a shower?", "la toalla", ["el peine", "el jabón", "la pasta de dientes"], "A towel dries you."),
        M("What do you use to comb your hair?", "el peine", ["el jabón", "la toalla", "la pasta de dientes"], "El peine is the comb."),
        M("Which sentence is correct?", "Se pone el abrigo.", ["Se pone los abrigo.", "Se pone una abrigo.", "Se pone la abrigo."], "Abrigo is masculine singular: el abrigo."),
    ],
)

# ---------------------------------------------------------------------------- 118
L118 = lesson(
    "Reflexive verbs with stem changes",
    "me acuesto, me despierto, me visto",
    requires=["dormir", "despertar", "vestir", "sentir", "levantar", "mañana"],
    cards=[
        card("Boot reflexives",
             "Many routine verbs are also boot verbs. The pronoun stays in front, and the verb changes as usual: "
             "acostarse (o → ue), despertarse (e → ie), vestirse (e → i), dormirse (o → ue), sentirse (e → ie).",
             tables=[table(["", "acostarse", "vestirse"],
                           [["yo", "me acuesto", "me visto"],
                            ["tú", "te acuestas", "te vistes"],
                            ["él, ella, usted", "se acuesta", "se viste"],
                            ["nosotros", "nos acostamos", "nos vestimos"],
                            ["vosotros", "os acostáis", "os vestís"],
                            ["ellos, ellas, ustedes", "se acuestan", "se visten"]],
                           say=[1, 2])]),
        card("More examples",
             "Nosotros and vosotros keep the original vowel.",
             examples=[
                 ex("Me despierto a las seis y me duermo a las once.", "I wake up at six and fall asleep at eleven.", "Me despierto"),
                 ex("Mis hijos se acuestan temprano.", "My children go to bed early.", "se acuestan"),
                 ex("Nos vestimos y salimos de casa.", "We get dressed and leave the house.", "Nos vestimos"),
                 ex("Ella se siente mejor hoy.", "She feels better today.", "se siente"),
             ]),
    ],
    exercises=[
        F("Yo me ___ a las once.", "acuesto", ["acosto", "acuestas", "acostamos"], "Acostarse: o → ue.", tr="I go to bed at eleven.", lemma="acostar:yo"),
        F("Nosotros nos ___ a las seis.", "despertamos", ["despiertamos", "despiertan", "despierto"], "Nosotros keeps the e.", tr="We wake up at six.", lemma="despertar:nosotros"),
        F("Mis hijos se ___ rápido.", "visten", ["viste", "vestimos", "vistes"], "Vestirse: e → i; los hijos is they.", tr="My children get dressed quickly.", lemma="vestir:ellos"),
        F("Tú te ___ muy rápido.", "duermes", ["dormes", "duerme", "dormimos"], "Dormir: o → ue.", tr="You fall asleep very quickly.", lemma="dormir:tú"),
        F("Ella se ___ muy bien hoy.", "siente", ["sienta", "sentimos", "sientes"], "Sentirse: e → ie.", tr="She feels very well today.", lemma="sentir:ella"),
        M("Which form is correct for “yo” with vestirse?", "me visto", ["me vesto", "me vestes", "me vestimos"], "Vestirse: e → i."),
        M("Which pattern does “dormirse” follow?", "o → ue", ["e → ie", "e → i", "u → ue"], "Me duermo."),
        M("Which form is correct for “nosotros” with acostarse?", "nos acostamos", ["nos acuestamos", "nos acostan", "nos acuestan"], "Nosotros keeps the o."),
        M("Which pattern does “despertarse” follow?", "e → ie", ["o → ue", "e → i", "u → ue"], "Me despierto."),
    ],
    verify=vp("acostar", "acuesto", "acuestas", "acuesta", "acostamos", "acostáis", "acuestan")
           + vp("vestir", "visto", "vistes", "viste", "vestimos", "vestís", "visten")
           + vp("dormir", "duermo", "duermes", "duerme", "dormimos", "dormís", "duermen")
           + vp("sentir", "siento", "sientes", "siente", "sentimos", "sentís", "sienten"),
)

# ---------------------------------------------------------------------------- 119
L119 = lesson(
    "Reflexive or not? Personal a",
    "Me lavo. Lavo la ropa. Levanto a mis hijos.",
    requires=["lavar", "levantar", "casar", "morir", "dormir", "hijo"],
    cards=[
        card("Same verb, different meaning",
             "Many verbs can be reflexive (the action returns to you) or not (the action goes to something or "
             "someone else). When the object is a person (or a pet treated like one), add the personal a.",
             tables=[table(["Reflexive", "Not reflexive"],
                           [["Pablo se lava la cara.", "Pablo lava el coche."],
                            ["Me levanto a las siete.", "Levanto a mis hermanos a las siete."],
                            ["Me acuesto temprano.", "Acuesto al niño temprano."],
                            ["Me baño por la noche.", "Baño al perro los domingos."]],
                           say=[0, 1])]),
        card("Life events",
             "For these life events Spanish normally uses the reflexive: casarse (con), divorciarse (de) and mudarse (to move to a "
             "new home). To say “to die” you can use morir or morirse.",
             examples=[
                 ex("Mi hermana se casa en junio.", "My sister is getting married in June.", "se casa"),
                 ex("Mis tíos se divorcian este año.", "My aunt and uncle are getting divorced this year.", "se divorcian"),
                 ex("Nos mudamos a una casa nueva.", "We are moving to a new house.", "Nos mudamos"),
                 ex("Mis padres se mudan a Sevilla.", "My parents are moving to Seville.", "se mudan"),
             ]),
    ],
    exercises=[
        F("Yo ___ a mis hermanos a las siete.", "levanto", ["me levanto", "te levantas", "se levanta"], "The object is people, so no pronoun and personal a.", tr="I get my brothers and sisters up at seven."),
        F("Mi madre ___ la ropa sucia.", "lava", ["se lavan", "me lavo", "te lavas"], "The object is clothes: not reflexive.", tr="My mother washes the dirty clothes."),
        F("Ana ___ antes de salir.", "se peina", ["peina", "peinan", "me peino"], "Ana combs her own hair: reflexive.", tr="Ana combs her hair before going out."),
        F("Yo ___ a mi perro los domingos.", "baño", ["me baño", "bañas", "bañamos"], "The dog is the object: no pronoun.", tr="I bathe my dog on Sundays."),
        F("Mis tíos ___ en junio.", "se casan", ["se casa", "me caso", "nos casamos"], "Casarse with los tíos: se casan.", tr="My aunt and uncle are getting married in June."),
        M("Which preposition goes with “casarse”?", "con", ["de", "en", "para"], "Se casa con su novio."),
        M("Which verb means “to move to a new home”?", "mudarse", ["morirse", "casarse", "divorciarse"], "Mudarse."),
        M("Which sentence is correct?", "Acuesto a mis hijos a las nueve.", ["Acuesto mis hijos a las nueve.", "Me acuesto a mis hijos a las nueve.", "Acuesto de mis hijos a las nueve."], "A person who receives the action takes the personal a, and no reflexive pronoun."),
        M("Which sentence is reflexive?", "Me baño por la noche.", ["Baño al perro.", "Lavo la ropa.", "Peino a mi hija."], "The action returns to the subject."),
    ],
)

# ---------------------------------------------------------------------------- 120
L120 = lesson(
    "Infinitive after prepositions",
    "sin estudiar, para jugar, cansado de nadar",
    requires=["sin", "para", "por", "nadar", "estudiar", "tarea"],
    cards=[
        card("Always the infinitive",
             "After a preposition, a verb is always in the infinitive in Spanish. English often uses -ing (“tired of "
             "waiting”), but Spanish never does. This works with every preposition.",
             tables=[table(["Preposition", "Example"],
                           [["a", "Mi hermano aprende a conducir."],
                            ["de", "Estoy cansado de esperar."],
                            ["sin", "Es imposible aprender sin practicar."],
                            ["para", "Necesito una raqueta para jugar al tenis."],
                            ["por", "Gracias por llamarme."],
                            ["con", "Con practicar mucho vas a mejorar."]],
                           say=[1])]),
        card("English -ing, Spanish infinitive",
             "A good rule: if the English has a preposition plus -ing, the Spanish has the same idea with the "
             "infinitive.",
             examples=[
                 ex("Gracias por venir.", "Thank you for coming.", "venir"),
                 ex("Salgo sin desayunar.", "I leave without having breakfast.", "sin desayunar"),
                 ex("Estoy contento de trabajar aquí.", "I am glad to work here.", "trabajar"),
             ]),
    ],
    exercises=[
        F("Estoy cansado de ___.", "estudiar", ["estudiando", "estudio", "estudié"], "After de, use the infinitive.", tr="I am tired of studying."),
        F("Salgo sin ___.", "desayunar", ["desayunando", "desayuno", "desayunado"], "After sin, use the infinitive.", tr="I leave without having breakfast."),
        F("Necesito dinero para ___ ropa.", "comprar", ["comprando", "compro", "comprado"], "After para, use the infinitive.", tr="I need money to buy clothes."),
        F("Aprendo a ___ en el lago.", "nadar", ["nadando", "nado", "nadado"], "After a, use the infinitive.", tr="I am learning to swim in the lake."),
        M("Which sentence is correct?", "Gracias por venir.", ["Gracias por viniendo.", "Gracias por vengo.", "Gracias por vino."], "After por: infinitive."),
        M("How do you say “It is hard to learn without studying”?", "Es difícil aprender sin estudiar.", ["Es difícil aprender sin estudiando.", "Es difícil aprender sin estudio.", "Es difícil aprender sin estudiado."], "After sin: infinitive."),
        M("After a preposition, which verb form do you use in Spanish?", "the infinitive", ["the -ndo form", "the yo form", "the future"], "Always the infinitive."),
        M("What is wrong with “Estoy cansado de esperando”?", "After de you need the infinitive: esperar.", ["Nothing, it is correct.", "Cansado should be cansada.", "Estoy should be estás."], "No -ndo form after a preposition."),
        M("How do you say “I am learning to comb my own hair”?", "Aprendo a peinarme.", ["Aprendo peinarme.", "Aprendo a peinando.", "Aprendo de peinarme."], "Aprender a + infinitive; the pronoun matches yo."),
    ],
)

# ---------------------------------------------------------------------------- 121
L121 = lesson(
    "Before and after: antes de, después de",
    "Antes de acostarme, me lavo los dientes.",
    requires=["antes", "después", "cenar", "dormir", "lavar", "ver"],
    cards=[
        card("Antes de and después de + infinitive",
             "When a verb follows antes de (before) or después de (after), it is always an infinitive in Spanish.",
             tables=[table(["Spanish", "English"],
                           [["Siempre leo antes de dormir.", "I always read before sleeping."],
                            ["Después de comer, descanso un poco.", "After eating, I rest a little."]],
                           say=[0])]),
        card("With reflexive verbs",
             "If the infinitive is reflexive, the pronoun attaches to it, and it matches the subject of the sentence: "
             "antes de acostarme (I), después de ducharse (she).",
             examples=[
                 ex("Antes de acostarme, leo un poco.", "Before going to bed, I read a little.", "Antes de acostarme"),
                 ex("Rosa se peina después de ducharse.", "Rosa combs her hair after taking a shower.", "después de ducharse"),
                 ex("Nos lavamos las manos antes de comer.", "We wash our hands before eating.", "antes de comer"),
                 ex("Después de levantarte, ¿qué haces?", "After getting up, what do you do?", "Después de levantarte"),
             ]),
    ],
    exercises=[
        F("Antes de ___, me lavo las manos.", "comer", ["como", "comiendo", "comí"], "Antes de + infinitive.", tr="Before eating, I wash my hands."),
        F("Después de ___, me visto.", "ducharme", ["ducharse", "ducharte", "ducharnos"], "The subject is yo: ducharme.", tr="After showering, I get dressed."),
        F("Antes de ___, Ana se cepilla los dientes.", "acostarse", ["acostarme", "acostarte", "acostarnos"], "The subject is Ana: acostarse.", tr="Before going to bed, Ana brushes her teeth."),
        F("Después de ___, Luis desayuna.", "levantarse", ["levantarme", "levantarte", "levantarnos"], "The subject is Luis: levantarse.", tr="After getting up, Luis has breakfast."),
        F("Nosotros siempre limpiamos la casa después de ___.", "cenar", ["cenamos", "cenando", "cené"], "Después de + infinitive.", tr="We always clean the house after eating dinner."),
        M("What does “después de cenar” mean?", "after eating dinner", ["before dinner", "instead of dinner", "during dinner"], "Después de = after."),
        M("Which sentence is correct?", "Antes de acostarme, leo un libro.", ["Antes de me acostar, leo un libro.", "Antes de acuesto, leo un libro.", "Antes de acostando, leo un libro."], "Antes de + infinitive with the pronoun attached."),
        M("Which sentence means “After eating, we brush our teeth”?", "Después de comer, nos cepillamos los dientes.", ["Antes de comer, nos cepillamos los dientes.", "Después de comemos, nos cepillamos los dientes.", "Después de comiendo, nos cepillamos los dientes."], "Después de + infinitive."),
        M("What does “antes de dormir” mean?", "before sleeping", ["after sleeping", "while sleeping", "instead of sleeping"], "Antes de = before."),
    ],
)

# ---------------------------------------------------------------------------- 122
L122 = lesson(
    "How often? Frequency and soler",
    "a veces, a menudo, siempre, suelo",
    requires=["siempre", "nunca", "frecuencia", "menudo", "soler", "día"],
    cards=[
        card("Expressions of frequency",
             "These expressions say how often you do something. They usually come at the beginning or end of the "
             "sentence, and siempre, nunca and casi nunca can also go before the verb. If nunca comes after the verb, put no before the verb: No me acuesto nunca antes de las diez.",
             tables=[table(["Expresión", "English"],
                           [["nunca", "never"],
                            ["casi nunca", "almost never"],
                            ["raramente", "rarely"],
                            ["a veces", "sometimes"],
                            ["a menudo", "often"],
                            ["con frecuencia", "frequently"],
                            ["casi siempre", "almost always"],
                            ["siempre", "always"],
                            ["todos los días", "every day"]],
                           say=[0])],
             examples=[
                 ex("A veces me levanto tarde los domingos.", "Sometimes I get up late on Sundays.", "A veces"),
                 ex("Me ducho con agua fría a menudo.", "I often take a shower with cold water.", "a menudo"),
                 ex("Nunca me acuesto antes de las diez.", "I never go to bed before ten.", "Nunca"),
             ]),
        card("Soler: to usually do",
             "Soler + infinitive says what you usually do. It has no exact English equivalent: “I usually...”. "
             "It is an o → ue boot verb, and the verb after it stays in the infinitive.",
             tables=[table(["Subject", "Soler"],
                           [["yo", "suelo"],
                            ["tú", "sueles"],
                            ["él, ella, usted", "suele"],
                            ["nosotros", "solemos"],
                            ["vosotros", "soléis"],
                            ["ellos, ellas, ustedes", "suelen"]],
                           say=[1])],
             examples=[
                 ex("Suelo levantarme a las siete.", "I usually get up at seven.", "Suelo levantarme"),
                 ex("¿Qué sueles hacer después de clase?", "What do you usually do after class?", "sueles"),
                 ex("Solemos tomar vacaciones en el verano.", "We usually take a vacation in the summer.", "Solemos"),
             ]),
    ],
    exercises=[
        F("Yo ___ levantarme a las seis.", "suelo", ["solo", "suele", "solemos"], "Soler is o → ue: suelo.", tr="I usually get up at six.", lemma="soler:yo"),
        F("Nosotros ___ cenar a las ocho.", "solemos", ["suelemos", "suelen", "suelo"], "Nosotros keeps the o: solemos.", tr="We usually have dinner at eight.", lemma="soler:nosotros"),
        F("Ellos ___ salir los viernes.", "suelen", ["suele", "solen", "sueles"], "Ellos is they: suelen.", tr="They usually go out on Fridays.", lemma="soler:ellos"),
        F("¿Qué ___ hacer tú los domingos?", "sueles", ["suelo", "suele", "suelen"], "Tú: sueles.", tr="What do you usually do on Sundays?", lemma="soler:tú"),
        M("What does “Suelo desayunar a las siete” mean?", "I usually have breakfast at seven.", ["I am having breakfast at seven.", "I will have breakfast at seven.", "I never have breakfast at seven."], "Soler = usually."),
        M("Which expression means “rarely”?", "raramente", ["siempre", "a menudo", "con frecuencia"], "Raramente is rarely."),
        M("Which expression means “sometimes”?", "a veces", ["nunca", "siempre", "todos los días"], "A veces."),
        M("Which is the most frequent?", "siempre", ["a veces", "raramente", "casi nunca"], "Siempre = always."),
        M("Which form follows “suelo”?", "an infinitive", ["a gerund", "a past form", "a future form"], "Soler + infinitive."),
    ],
    verify=vp("soler", "suelo", "sueles", "suele", "solemos", "soléis", "suelen"),
)

# ---------------------------------------------------------------------------- 123
L123 = lesson(
    "Verbs with -go: pongo, salgo, tengo, vengo",
    "poner, salir, tener, venir, decir, hacer, traer",
    requires=["poner", "salir", "tener", "venir", "decir", "traer"],
    cards=[
        card("The yo form",
             "Several very common verbs have a special yo form with -go. Poner, hacer, salir, traer, caer and valer are regular in the other forms; tener, venir and decir also change their stem.",
             tables=[table(["Infinitive", "Yo", "English"],
                           [["poner", "pongo", "to put"],
                            ["hacer", "hago", "to do, make"],
                            ["salir", "salgo", "to leave, go out"],
                            ["tener", "tengo", "to have"],
                            ["venir", "vengo", "to come"],
                            ["decir", "digo", "to say, tell"],
                            ["traer", "traigo", "to bring"],
                            ["caer", "caigo", "to fall"],
                            ["valer", "valgo", "to be worth"]],
                           say=[1])]),
        card("The full pattern",
             "Tener, venir and decir are also boot verbs (e → ie or e → i), in the tú, él and ellos forms (tienes, viene, dicen). Yo has its own -go form, and nosotros and vosotros keep the e. "
             "Poner, salir, traer and caer are regular after the yo form.",
             tables=[table(["", "poner", "salir", "venir"],
                           [["yo", "pongo", "salgo", "vengo"],
                            ["tú", "pones", "sales", "vienes"],
                            ["él, ella, usted", "pone", "sale", "viene"],
                            ["nosotros", "ponemos", "salimos", "venimos"],
                            ["vosotros", "ponéis", "salís", "venís"],
                            ["ellos, ellas, ustedes", "ponen", "salen", "vienen"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        F("Yo ___ la mochila en la silla.", "pongo", ["pono", "pones", "ponemos"], "Poner: yo pongo.", tr="I put the backpack on the chair.", lemma="poner:yo"),
        F("Yo ___ de casa a las ocho.", "salgo", ["salo", "sales", "salimos"], "Salir: yo salgo.", tr="I leave the house at eight.", lemma="salir:yo"),
        F("Yo siempre ___ mi diccionario a clase.", "traigo", ["traio", "traes", "traemos"], "Traer: yo traigo.", tr="I always bring my dictionary to class.", lemma="traer:yo"),
        F("Yo no ___ nada.", "digo", ["dico", "dices", "decimos"], "Decir: yo digo (e → i).", tr="I do not say anything.", lemma="decir:yo"),
        F("Mis amigos ___ a mi casa los sábados.", "vienen", ["vienan", "viene", "venimos"], "Venir: e → ie; los amigos is they: vienen.", tr="My friends come to my house on Saturdays.", lemma="venir:ellos"),
        F("Tú ___ muchos libros a la escuela.", "traes", ["traigo", "trae", "traemos"], "Only yo has -go: tú traes.", tr="You bring many books to school.", lemma="traer:tú"),
        F("Ella ___ siempre la verdad.", "dice", ["decimos", "dicen", "digo"], "Decir: e → i; ella: dice.", tr="She always tells the truth.", lemma="decir:ella"),
        M("Which verb is correct for “yo hago”?", "hacer", ["hagar", "hazar", "hacar"], "Hacer → hago."),
        M("Which verb does NOT have -go in its yo form?", "hablar", ["poner", "salir", "venir"], "Hablar is regular: hablo."),
    ],
    verify=vp("poner", "pongo", "pones", "pone", "ponemos", "ponéis", "ponen")
           + vp("salir", "salgo", "sales", "sale", "salimos", "salís", "salen")
           + vp("venir", "vengo", "vienes", "viene", "venimos", "venís", "vienen")
           + vp("traer", "traigo", "traes", "trae", "traemos", "traéis", "traen")
           + vp("decir", "digo", "dices", "dice", "decimos", "decís", "dicen")
           + vp("tener", "tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen")
           + vp("caer", "caigo", "caes", "cae", "caemos", "caéis", "caen")
           + vp("valer", "valgo", "vales", "vale", "valemos", "valéis", "valen"),
)

# ---------------------------------------------------------------------------- 124
L124 = lesson(
    "Salir, oír and caerse",
    "salir de, salir con, oír, caerse",
    requires=["salir", "oír", "caer", "casa", "amigo", "examen"],
    cards=[
        card("Salir and its prepositions",
             "Salir (to leave, to go out) is followed by different prepositions depending on what comes next.",
             tables=[table(["Pattern", "Example"],
                           [["salir de + place", "Salgo de casa a las siete."],
                            ["salir con + person", "Salgo con mis amigos los sábados."],
                            ["salir para + destination", "Mañana salgo para Lima."],
                            ["salir bien / mal", "Todo va a salir bien en el examen."]],
                           say=[1])]),
        card("Oír: to hear",
             "Oír has an irregular yo form (oigo) and a y in oyes, oye and oyen; oímos and oís are regular, with an accent. To get someone's attention you say "
             "oye (to a friend) or oiga (to someone you address as usted).",
             tables=[table(["Subject", "Oír"],
                           [["yo", "oigo"], ["tú", "oyes"], ["él, ella, usted", "oye"],
                            ["nosotros", "oímos"], ["vosotros", "oís"], ["ellos, ellas, ustedes", "oyen"]],
                           say=[1])],
             examples=[
                 ex("Oigo la radio por la mañana.", "I listen to the radio in the morning.", "Oigo"),
                 ex("Oiga, por favor, ¿dónde está la farmacia?", "Excuse me, where is the pharmacy?", "Oiga"),
             ]),
        card("Caerse",
             "Caer means to fall. When a person falls, Spanish uses the reflexive caerse. The yo form has -go: "
             "me caigo.",
             examples=[
                 ex("Me caigo cuando patino sobre hielo.", "I fall when I ice skate.", "Me caigo"),
                 ex("Los niños se caen mucho en el parque.", "The children fall a lot in the park.", "se caen"),
             ]),
    ],
    exercises=[
        F("Yo ___ la radio por la mañana.", "oigo", ["oyo", "oyes", "oímos"], "Oír: yo oigo.", tr="I listen to the radio in the morning.", lemma="oír:yo"),
        F("Tú ___ muy bien.", "oyes", ["oigo", "oye", "oyen"], "Tú: oyes.", tr="You hear very well.", lemma="oír:tú"),
        F("Ellos ___ las noticias.", "oyen", ["oye", "oímos", "oigo"], "Ellos: oyen.", tr="They hear the news.", lemma="oír:ellos"),
        F("Yo siempre me ___ cuando patino.", "caigo", ["cayo", "caes", "caemos"], "Caer: yo caigo.", tr="I always fall when I skate.", lemma="caer:yo"),
        F("Salgo ___ casa a las siete.", "de", ["con", "sin", "entre"], "Salir de + place.", tr="I leave the house at seven."),
        F("Salgo ___ mis amigos los sábados.", "con", ["de", "sin", "entre"], "Salir con + person.", tr="I go out with my friends on Saturdays."),
        M("How do you say “Everything will turn out well on the exam”?", "Todo va a salir bien en el examen.", ["Todo va a salir mal en el examen.", "Todo va a salir de bien en el examen.", "Todo va a salir con el examen."], "Salir bien."),
        M("Which word gets the attention of someone you address as usted?", "Oiga", ["Oye", "Oigo", "Oímos"], "Oiga is the usted command; oye is for tú."),
        M("Which is the correct reflexive form for “yo” with caerse?", "me caigo", ["me cayo", "me caes", "me cae"], "Caer: caigo."),
    ],
    verify=vp("oír", "oigo", "oyes", "oye", "oímos", "oís", "oyen"),
)

# ---------------------------------------------------------------------------- 125
L125 = lesson(
    "Ponerse, sentirse, estar: clothes and moods",
    "Me pongo nervioso. Me siento bien. Estoy contento.",
    requires=["poner", "sentir", "contento", "triste", "nervioso", "cansado"],
    cards=[
        card("Ponerse: put on, become",
             "Ponerse has two uses. With clothes it means “to put on”. With a mood or condition it means “to get, "
             "to become”. Compare it with vestirse, which means “to get dressed” and takes no object.",
             tables=[table(["Spanish", "English"],
                           [["Me pongo la chaqueta.", "I put on my jacket."],
                            ["Me visto por la mañana.", "I get dressed in the morning."],
                            ["Me pongo nervioso en los exámenes.", "I get nervous during exams."],
                            ["Mi hermano se pone triste.", "My brother gets sad."]],
                           say=[0])]),
        card("Three verbs for feelings",
             "To talk about moods you can use ponerse (to get, to become), sentirse (to feel) or estar (to be). The "
             "adjective agrees with the subject: nervioso or nerviosa. Add muy or un poco to change the intensity.",
             tables=[table(["Verb", "Example", "English"],
                           [["ponerse", "Daniel se pone triste.", "Daniel gets sad."],
                            ["sentirse", "Rosa se siente feliz.", "Rosa feels happy."],
                            ["estar", "Elena está enojada.", "Elena is angry."]],
                           say=[1])],
             examples=[
                 ex("Me pongo un poco nervioso.", "I get a little nervous.", "un poco nervioso"),
                 ex("Los niños están muy contentos.", "The children are very happy.", "muy contentos"),
             ]),
        card("¿Cómo te encuentras?",
             "Encontrarse, the reflexive form of encontrar, can mean “to be, to find yourself”. It is a polite, caring way "
             "to ask how someone is doing; in everyday speech people usually just say ¿Cómo estás? (and ¿Dónde estás? instead of ¿Dónde te encuentras?)",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Cómo te encuentras?", "Me encuentro muy bien hoy."],
                            ["¿Dónde te encuentras?", "Me encuentro en la oficina."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Mi hermana se pone ___ cuando hay un examen.", "nerviosa", ["nervioso", "nerviosos", "nerviosas"], "Mi hermana is feminine singular.", tr="My sister gets nervous when there is an exam."),
        F("Los niños se ponen muy ___.", "contentos", ["contento", "contenta", "contentas"], "Los niños: masculine plural.", tr="The children get very happy."),
        F("Yo me ___ la chaqueta.", "pongo", ["visto", "pones", "pone"], "Ponerse takes an object: me pongo la chaqueta.", tr="I put on my jacket.", lemma="poner:yo"),
        F("Daniel ___ triste cuando llueve.", "se pone", ["se viste", "se pongo", "me pone"], "Ponerse + adjective = to get.", tr="Daniel gets sad when it rains."),
        F("Mi madre ___ muy cansada hoy.", "está", ["pone", "viste", "sale"], "Estar + cansada describes the state.", tr="My mother is very tired today."),
        M("Which verb means “to feel”?", "sentirse", ["ponerse", "vestirse", "caerse"], "Me siento."),
        M("What does “¿Cómo te encuentras?” ask about?", "how you are doing", ["where you live", "what you found", "who you are"], "Encontrarse = to be, to find oneself."),
        M("Which sentence means “I get dressed”?", "Me visto.", ["Me pongo.", "Me vestido.", "Me veo."], "Vestirse takes no object."),
        M("Which sentence is correct?", "Me siento un poco triste.", ["Me siento un poco tristes.", "Me siento una poca triste.", "Me sientas un poco triste."], "Un poco + adjective; yo → siento."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 126
L126 = lesson(
    "Also and neither: también, tampoco",
    "Yo también. Yo tampoco.",
    requires=["también", "tampoco", "nunca", "siempre", "yo", "no"],
    cards=[
        card("Agreeing",
             "Use también (also, too) to agree with an affirmative sentence and tampoco (neither, either) to agree with "
             "a negative one. You can answer with just Yo también or Yo tampoco.",
             tables=[table(["Said", "Reply"],
                           [["Me ducho por la mañana.", "Yo también me ducho por la mañana."],
                            ["Me ducho por la mañana.", "Yo también."],
                            ["No me maquillo todos los días.", "Yo tampoco me maquillo todos los días."],
                            ["No me maquillo todos los días.", "Yo tampoco."]],
                           say=[0, 1])]),
        card("Position and the double negative",
             "También and tampoco can come before or after the verb. If tampoco comes after the verb, the sentence "
             "needs no before the verb, exactly like nunca.",
             examples=[
                 ex("Yo también me levanto temprano.", "I also get up early.", "también"),
                 ex("Yo tampoco me levanto temprano.", "I do not get up early either.", "tampoco"),
                 ex("Yo no me levanto temprano tampoco.", "I do not get up early either.", "no me levanto temprano tampoco"),
             ]),
    ],
    exercises=[
        F("—Me levanto temprano. —Yo ___.", "también", ["tampoco", "no", "nada"], "Agreeing with an affirmative sentence: también.", tr="“I get up early.” “Me too.”"),
        F("—No me afeito todos los días. —Yo ___.", "tampoco", ["también", "siempre", "mucho"], "Agreeing with a negative sentence: tampoco.", tr="“I do not shave every day.” “Me neither.”"),
        F("—Nunca me acuesto tarde. —Yo ___.", "tampoco", ["también", "siempre", "mucho"], "Nunca is negative, so tampoco.", tr="“I never go to bed late.” “Me neither.”"),
        F("Mi hermana se baña por la noche y yo ___.", "también", ["tampoco", "nada", "nunca"], "Affirmative → también.", tr="My sister takes a bath at night and I do too."),
        M("Which sentence is correct?", "Yo tampoco me maquillo.", ["Yo tampoco no me maquillo.", "Yo no tampoco me maquillo.", "Yo también no me maquillo."], "Tampoco before the verb needs no extra no."),
        M("Which sentence is correct?", "Yo no me maquillo tampoco.", ["Yo me maquillo tampoco.", "Yo no me maquillo también.", "Yo tampoco no me maquillo."], "After the verb, tampoco needs no before the verb."),
        M("What does “Yo también” mean?", "Me too.", ["Me neither.", "Not me.", "Only me."], "También = also, too."),
        M("What does “Yo tampoco” mean?", "Me neither.", ["Me too.", "Only me.", "Always me."], "Tampoco = neither."),
        M("A friend says “Siempre desayuno”. How do you agree?", "Yo también.", ["Yo tampoco.", "Yo nunca.", "Yo no."], "Siempre is affirmative."),
    ],
)

# ---------------------------------------------------------------------------- 127
L127 = lesson(
    "Workday and vacation routines",
    "Entre semana me levanto temprano. En vacaciones duermo hasta tarde.",
    requires=["día", "dormir", "levantar", "cenar", "tarde", "siempre"],
    cards=[
        card("A workday",
             "Read what a typical workday looks like. Notice the reflexive verbs, the pronouns and the order of events.",
             examples=[
                 ex("Entre semana me despierto a las seis y me levanto enseguida.", "On weekdays I wake up at six and get up right away.", "me despierto"),
                 ex("Me ducho, me visto y desayuno rápido.", "I take a shower, get dressed and have a quick breakfast.", "Me ducho"),
                 ex("Después de trabajar, suelo cenar con mi familia.", "After work, I usually have dinner with my family.", "suelo cenar"),
                 ex("Antes de acostarme, me cepillo los dientes y leo un poco.", "Before going to bed, I brush my teeth and read a little.", "Antes de acostarme"),
             ]),
        card("A vacation",
             "On vacation the routine changes. Spanish uses the same tools: soler, frequency words, reflexive verbs.",
             examples=[
                 ex("En vacaciones no me levanto temprano.", "On vacation I do not get up early.", "no me levanto temprano"),
                 ex("Suelo dormir hasta las nueve.", "I usually sleep until nine.", "Suelo dormir"),
                 ex("A veces me baño en el mar antes de desayunar.", "Sometimes I swim in the sea before having breakfast.", "A veces"),
                 ex("Nunca me pongo reloj en la playa.", "I never wear a watch on the beach.", "Nunca me pongo"),
             ]),
    ],
    exercises=[
        F("Entre semana yo me ___ a las seis.", "despierto", ["despiertas", "despierta", "despertamos"], "Yo: despierto (e → ie).", tr="On weekdays I wake up at six.", lemma="despertar:yo"),
        F("En vacaciones yo ___ dormir hasta las nueve.", "suelo", ["solo", "suele", "solemos"], "Soler: suelo.", tr="On vacation I usually sleep until nine.", lemma="soler:yo"),
        F("Después de ___, suelo cenar con mi familia.", "trabajar", ["trabajo", "trabajando", "trabajé"], "Después de + infinitive.", tr="After working, I usually have dinner with my family."),
        F("Antes de ___, me cepillo los dientes.", "acostarme", ["acostarse", "acostarte", "acostarnos"], "The subject is yo: acostarme.", tr="Before going to bed, I brush my teeth."),
        F("En vacaciones ___ me pongo reloj.", "nunca", ["siempre", "tampoco", "también"], "Nunca fits “on vacation I do not wear a watch”.", tr="On vacation I never wear a watch."),
        M("What does “Entre semana” mean?", "on weekdays", ["on weekends", "every month", "next week"], "Entre semana = on weekdays."),
        M("Which sentence says what you usually do?", "Suelo dormir hasta las nueve.", ["Estoy durmiendo hasta las nueve.", "Dormiré hasta las nueve.", "Quiero dormir hasta las nueve."], "Soler = usually."),
        M("Which sentence is correct?", "Me ducho, me visto y desayuno rápido.", ["Me ducho, visto me y desayuno rápido.", "Ducho, me visto y me desayuno rápido.", "Me ducho, me visto y me desayuno rápido."], "In standard Spanish desayunar is not reflexive; the others are."),
        M("Which sentence describes a vacation morning?", "Suelo levantarme tarde.", ["Me despierto a las cinco.", "Me visto para la oficina.", "Salgo de casa a las seis."], "A relaxed morning with late rising."),
    ],
)

# ---------------------------------------------------------------------------- 128
L128 = lesson(
    "Review: daily routines",
    "reflexivos, soler, -go, antes de, también",
    requires=["levantar", "dormir", "poner", "salir", "soler", "antes"],
    cards=[
        card("Quick map",
             "Pronoun = subject. Article for the body. Infinitive after prepositions. -Go verbs have a special yo form. "
             "Tampoco needs no if it follows the verb.",
             tables=[table(["Idea", "Example"],
                           [["Reflexive pronoun", "Me levanto, te levantas, se levanta"],
                            ["Body part", "Me lavo las manos."],
                            ["Infinitive after a preposition", "Antes de acostarme, leo."],
                            ["Yo with -go", "Salgo de casa a las ocho."],
                            ["Soler + infinitive", "Suelo desayunar a las siete."],
                            ["Agreeing", "Yo también. Yo tampoco."]],
                           say=[1])]),
    ],
    exercises=[
        F("Tú ___ acuestas a las once.", "te", ["me", "se", "nos"], "Tú → te.", tr="You go to bed at eleven."),
        F("Mi hermano se lava ___ cara.", "la", ["su", "mi", "una"], "Body part → article.", tr="My brother washes his face."),
        F("Voy a ___ ahora.", "ducharme", ["ducharte", "ducharse", "ducharnos"], "Voy is yo: ducharme.", tr="I am going to take a shower now."),
        F("Yo ___ de casa a las ocho.", "salgo", ["salo", "sales", "salimos"], "Salir: yo salgo.", tr="I leave the house at eight.", lemma="salir:yo"),
        F("Después de ___, me visto.", "ducharme", ["ducharse", "ducharte", "ducharnos"], "The subject is yo: ducharme.", tr="After taking a shower, I get dressed."),
        F("Nosotros ___ cenar a las ocho.", "solemos", ["suelemos", "suelen", "suelo"], "Soler: solemos.", tr="We usually have dinner at eight.", lemma="soler:nosotros"),
        F("Yo me ___ a las once.", "acuesto", ["acosto", "acuestas", "acostamos"], "Acostarse: o → ue.", tr="I go to bed at eleven.", lemma="acostar:yo"),
        M("Which sentence is correct?", "Me pongo nervioso en los exámenes.", ["Me visto nervioso en los exámenes.", "Pongo nervioso en los exámenes.", "Me ponemos nervioso en los exámenes."], "Ponerse + adjective."),
        M("A friend says “No me maquillo”. Which reply agrees?", "Yo tampoco.", ["Yo también.", "Yo siempre.", "Yo mucho."], "Negative → tampoco."),
        M("Which sentence is correct?", "Estoy cansado de esperar.", ["Estoy cansado de esperando.", "Estoy cansado de espero.", "Estoy cansado de esperé."], "After a preposition: infinitive."),
    ],
)

UNIT = unit("La rutina diaria", [L114, L115, L116, L117, L118, L119, L120, L121, L122, L123, L124, L125, L126, L127, L128])

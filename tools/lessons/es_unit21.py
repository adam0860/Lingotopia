"""Unit 21: health words, and the present perfect (a primer: the textbook's Chapter 21, which Chapters 22, 24 and 25 build on, was not supplied)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 375
L375 = lesson(
    "Aches and pains: me duele…",
    "Me duele la cabeza y tengo fiebre.",
    requires=["doler", "cabeza", "garganta", "estómago", "espalda", "pecho", "pierna", "ojo", "dolor", "fiebre"],
    cards=[
        card("Doler works like gustar",
             "To say that something hurts, Spanish uses doler with an indirect pronoun (me, te, le, nos, les). "
             "The part of the body is the subject, so the verb agrees with it: one thing, duele; more than one, duelen. "
             "To name a symptom, use tener: tengo fiebre, tengo tos, tengo náuseas.",
             tables=[table(["Parte del cuerpo", "Frase", "English"],
                           [["la cabeza", "Me duele la cabeza.", "I have a headache."],
                            ["la garganta", "Me duele la garganta.", "I have a sore throat."],
                            ["el estómago", "Me duele el estómago.", "My stomach hurts."],
                            ["la espalda", "Te duele la espalda.", "Your back hurts."],
                            ["el pecho", "Le duele el pecho.", "His chest hurts."],
                            ["las piernas", "Nos duelen las piernas.", "Our legs hurt."],
                            ["los ojos", "Les duelen los ojos.", "Their eyes hurt."]],
                           say=[1])],
             examples=[
                 ex("Tengo fiebre y me duele todo el cuerpo.", "I have a fever and my whole body hurts.", "me duele"),
                 ex("A mi hermano le duelen los pies después de correr.", "My brother's feet hurt after running.", "le duelen"),
             ]),
    ],
    exercises=[
        F("Me ___ la cabeza.", "duele", ["duelen", "dolemos", "doler"], "Cabeza is singular.", tr="I have a headache.", lemma="doler:él"),
        F("Me ___ los ojos.", "duelen", ["duele", "dolemos", "doler"], "Ojos is plural.", tr="My eyes hurt.", lemma="doler:ellos"),
        F("A mi hermana le ___ la espalda.", "duele", ["duelen", "dolemos", "doler"], "Espalda is singular.", tr="My sister's back hurts.", lemma="doler:él"),
        F("Nos ___ las piernas después de la caminata.", "duelen", ["duele", "dolemos", "doler"], "Piernas is plural.", tr="Our legs hurt after the hike.", lemma="doler:ellos"),
        F("Me duele ___ estómago.", "el", ["la", "los", "las"], "Estómago is masculine singular.", tr="My stomach hurts."),
        F("Les duelen ___ pies a los niños.", "los", ["el", "la", "las"], "Pies is masculine plural.", tr="The children's feet hurt."),
        F("Tengo mucha ___ y quiero ir al médico.", "fiebre", ["médico", "pecho", "estómago"], "Tener + a symptom.", tr="I have a high fever and I want to go to the doctor."),
        M("What does “Me duele la espalda” mean?", "My back hurts", ["I am washing my back", "I like my back", "I have a new backpack"], "Doler = to hurt; me = to me."),
        M("Which sentence says that more than one thing hurts?", "Me duelen los pies.", ["Me duele el pie.", "Me duele la cabeza.", "Tengo fiebre."], "Duelen agrees with los pies."),
    ],
    verify=vp("doler", "duelo", "dueles", "duele", "dolemos", "doléis", "duelen"),
)

# ---------------------------------------------------------------------------- 376
L376 = lesson(
    "At the doctor’s office",
    "¿Qué le pasa? ¿Desde cuándo tiene estos síntomas?",
    requires=["médico", "paciente", "síntoma", "tratamiento", "receta", "cita", "consulta", "descansar", "beber", "agua", "tener", "doler"],
    cards=[
        card("A visit, line by line",
             "The doctor speaks to the patient with usted, so the questions use the usted forms and the advice uses formal commands.",
             tables=[table(["Quién habla", "Frase", "English"],
                           [["Médico", "¿Qué le pasa?", "What is wrong?"],
                            ["Paciente", "Me duele la garganta y tengo fiebre.", "My throat hurts and I have a fever."],
                            ["Médico", "¿Desde cuándo tiene estos síntomas?", "Since when have you had these symptoms?"],
                            ["Paciente", "Desde hace dos días.", "For two days."],
                            ["Médico", "Le voy a dar una receta.", "I am going to give you a prescription."],
                            ["Médico", "Descanse y beba mucha agua.", "Rest and drink a lot of water."],
                            ["Paciente", "¿Cuándo debo volver?", "When should I come back?"],
                            ["Médico", "Pida otra cita si no mejora.", "Make another appointment if you do not get better."]],
                           say=[1])]),
    ],
    exercises=[
        F("Tengo una ___ con el médico a las tres.", "cita", ["receta", "herida", "fiebre"], "An appointment.", tr="I have an appointment with the doctor at three."),
        F("El médico me dio una ___ para comprar la medicina.", "receta", ["cita", "consulta", "agua"], "A prescription.", tr="The doctor gave me a prescription to buy the medicine."),
        F("Señora López, ¿desde cuándo ___ estos síntomas?", "tiene", ["tienes", "tengo", "tenemos"], "The doctor says usted.", tr="Mrs. López, since when have you had these symptoms?", lemma="tener:usted"),
        F("Señor Ruiz, ___ mucha agua y descanse.", "beba", ["bebe", "beber", "bebo"], "Formal command of beber.", tr="Mr. Ruiz, drink a lot of water and rest.", lemma="beber:usted:cmd"),
        F("Señor Ruiz, beba mucha agua y ___.", "descanse", ["descansa", "descansar", "descanso"], "Formal command of descansar.", tr="Mr. Ruiz, drink a lot of water and rest.", lemma="descansar:usted:cmd"),
        F("Hace dos días que me ___ la garganta.", "duele", ["duelen", "dolor", "dolemos"], "Garganta is singular.", tr="My throat has hurt for two days.", lemma="doler:él"),
        M("What does the doctor ask with “¿Qué le pasa?”", "What is the matter with you", ["What is your name", "Where do you live", "Who is your doctor"], "Pasar = to happen."),
        M("The doctor says “Pida otra cita si no mejora.” What should the patient do?", "Make another appointment if not better", ["Stop taking the medicine", "Go home and never return", "Cancel the first appointment"], "Pida = ask for / make."),
        M("Why does the doctor say “le” and “tiene”?", "He uses usted, the formal you", ["He is talking to a child", "He is talking about himself", "He is talking to two people"], "Usted takes the third-person forms."),
    ],
    verify=vpc("beber", "beba", "beban") + vpc("descansar", "descanse", "descansen"),
)

# ---------------------------------------------------------------------------- 377
L377 = lesson(
    "Illnesses and treatment",
    "La vacuna protege contra el virus.",
    requires=["enfermedad", "infección", "virus", "vacuna", "medicina", "pastilla", "tratamiento", "hospital", "herida", "enfermera", "operación", "cura"],
    cards=[
        card("Words for being sick and getting better",
             "These are the words you need to talk about illnesses, medicines and care. Practice them in short definitions.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la gripe", "flu", "La gripe causa fiebre y tos."],
                            ["el resfriado", "cold", "Tengo un resfriado y no puedo respirar bien."],
                            ["la infección", "infection", "Una herida sucia puede causar una infección."],
                            ["el virus", "virus", "Un virus puede pasar de una persona a otra."],
                            ["la vacuna", "vaccine", "La vacuna protege contra la enfermedad."],
                            ["la pastilla", "pill", "Tome una pastilla con agua."],
                            ["la herida", "wound", "Limpie la herida con agua."],
                            ["la operación", "surgery", "Después de la operación, el paciente descansó."],
                            ["la enfermera", "nurse", "La enfermera mide la temperatura."]],
                           say=[2])]),
    ],
    exercises=[
        F("La ___ protege a las personas contra una enfermedad.", "vacuna", ["herida", "enfermera", "operación"], "A vaccine protects.", tr="The vaccine protects people against a disease."),
        F("El paciente tomó una ___ con agua para el dolor.", "pastilla", ["vacuna", "enfermera", "operación"], "A pill is taken with water.", tr="The patient took a pill with water for the pain."),
        F("El ___ es un microbio que puede causar gripe.", "virus", ["hospital", "hueso", "paciente"], "A virus causes flu.", tr="A virus is a microbe that can cause the flu."),
        F("Una ___ sucia puede causar una infección.", "herida", ["vacuna", "receta", "cita"], "A dirty wound gets infected.", tr="A dirty wound can cause an infection."),
        F("En el ___ trabajan los médicos y las enfermeras.", "hospital", ["resfriado", "virus", "pastilla"], "Where doctors work.", tr="Doctors and nurses work in the hospital."),
        F("Después de la ___ del corazón, el paciente descansó una semana.", "operación", ["pastilla", "receta", "vacuna"], "After the surgery.", tr="After the heart surgery, the patient rested for a week."),
        M("Which illness causes fever and cough, and spreads easily?", "la gripe", ["la herida", "la vacuna", "la receta"], "Flu."),
        M("Which one is a person?", "la enfermera", ["la pastilla", "la infección", "el virus"], "A nurse is a person."),
        M("What is a resfriado?", "A cold", ["A hospital room", "A type of pill", "A kind of surgery"], "Resfriado = cold."),
    ],
)

# ---------------------------------------------------------------------------- 378
L378 = lesson(
    "Haber: he, has, ha, hemos, han",
    "Yo he comido. Ellos han llegado.",
    requires=["haber", "comer", "llegar", "trabajar", "vivir", "hablar"],
    cards=[
        card("A helper verb",
             "Haber is the helper (auxiliary) verb that builds the perfect tenses. It is not the same as tener: tener means to own or to hold, while haber just helps another verb. "
             "Its present-tense forms are irregular, so memorize them.",
             tables=[table(["Persona", "haber", "Ejemplo"],
                           [["yo", "he", "Yo he comido."],
                            ["tú", "has", "Tú has comido."],
                            ["él, ella, usted", "ha", "Ella ha comido."],
                            ["nosotros", "hemos", "Nosotros hemos comido."],
                            ["vosotros", "habéis", "Vosotros habéis comido."],
                            ["ellos, ellas, ustedes", "han", "Ellos han comido."]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Yo ___ comido.", "he", ["has", "ha", "hemos"], "Yo → he.", tr="I have eaten.", lemma="haber:yo"),
        F("Tú ___ trabajado mucho.", "has", ["he", "ha", "han"], "Tú → has.", tr="You have worked a lot.", lemma="haber:tú"),
        F("Ella ___ llegado temprano.", "ha", ["he", "has", "han"], "Ella → ha.", tr="She has arrived early.", lemma="haber:ella"),
        F("Nosotros ___ vivido aquí por años.", "hemos", ["han", "he", "has"], "Nosotros → hemos.", tr="We have lived here for years.", lemma="haber:nosotros"),
        F("Ellos ___ hablado con el médico.", "han", ["ha", "hemos", "has"], "Ellos → han.", tr="They have spoken with the doctor.", lemma="haber:ellos"),
        F("Vosotros ___ trabajado bien.", "habéis", ["han", "hemos", "has"], "Vosotros → habéis.", tr="You (all) have worked well.", lemma="haber:vosotros"),
        F("Usted ya ___ comido, ¿verdad?", "ha", ["has", "he", "han"], "Usted shares the él form.", tr="You have already eaten, haven't you?", lemma="haber:usted"),
        M("Which sentence builds the present perfect?", "He comido", ["Tengo comida", "Como mucho", "Comí ayer"], "haber + participle."),
        M("What is the difference between haber and tener?", "Haber only helps another verb; tener means to have or to hold", ["Haber means to own things", "They are exactly the same", "Tener only helps other verbs"], "Haber = auxiliary."),
    ],
    verify=vp("haber", "he", "has", "ha", "hemos", "habéis", "han"),
)

# ---------------------------------------------------------------------------- 379
L379 = lesson(
    "The present perfect: haber + participle",
    "Hoy he trabajado mucho y hemos comido tarde.",
    requires=["haber", "hablar", "comer", "vivir", "trabajar", "viajar", "recibir", "estudiar", "limpiar", "hoy", "semana"],
    cards=[
        card("Forming it",
             "The present perfect is haber in the present plus the past participle: -ado for -ar verbs, -ido for -er and -ir verbs. "
             "The participle never changes, no matter who the subject is. "
             "It describes something that happened in a period that is not over yet (hoy, esta semana, este año), or something with a result that matters now.",
             tables=[table(["Sujeto", "hablar", "comer", "vivir"],
                           [["yo", "he hablado", "he comido", "he vivido"],
                            ["tú", "has hablado", "has comido", "has vivido"],
                            ["él, ella, usted", "ha hablado", "ha comido", "ha vivido"],
                            ["nosotros", "hemos hablado", "hemos comido", "hemos vivido"],
                            ["vosotros", "habéis hablado", "habéis comido", "habéis vivido"],
                            ["ellos, ustedes", "han hablado", "han comido", "han vivido"]],
                           say=[1, 2, 3])],
             examples=[
                 ex("Esta semana he trabajado mucho.", "This week I have worked a lot.", "he trabajado"),
                 ex("¿Has vivido en otro país?", "Have you lived in another country?", "Has vivido"),
                 ex("Hoy hemos comido en casa.", "Today we have eaten at home.", "hemos comido"),
             ]),
    ],
    exercises=[
        F("Hoy hemos ___ en casa.", "comido", ["comer", "comió", "comiendo"], "Past participle of comer.", tr="Today we have eaten at home.", lemma="comer:part"),
        F("Esta semana he ___ mucho.", "trabajado", ["trabajar", "trabajó", "trabajando"], "Past participle of trabajar.", tr="This week I have worked a lot.", lemma="trabajar:part"),
        F("¿Has ___ en otro país?", "vivido", ["vivir", "vivió", "viviendo"], "Past participle of vivir.", tr="Have you lived in another country?", lemma="vivir:part"),
        F("Mi hermana ha ___ una carta del hospital.", "recibido", ["recibir", "recibió", "recibiendo"], "Past participle of recibir.", tr="My sister has received a letter from the hospital.", lemma="recibir:part"),
        F("Nunca he ___ en avión.", "viajado", ["viajar", "viajó", "viajando"], "Past participle of viajar.", tr="I have never traveled by plane.", lemma="viajar:part"),
        F("Oye, ¿qué has ___ hoy?", "estudiado", ["estudiar", "estudió", "estudiando"], "Past participle of estudiar.", tr="Hey, what have you studied today?", lemma="estudiar:part"),
        F("Los vecinos han ___ toda la calle.", "limpiado", ["limpiar", "limpió", "limpiando"], "Past participle of limpiar.", tr="The neighbors have cleaned the whole street.", lemma="limpiar:part"),
        M("What changes in “ellos han hablado” when the subject is “ella”?", "Only the helper: ella ha hablado", ["The participle: hablada", "Nothing changes", "The whole sentence"], "The participle is invariable."),
        M("Which participle ending do -er and -ir verbs take?", "-ido", ["-ado", "-ando", "-iendo"], "comer → comido, vivir → vivido."),
    ],
    verify=(vpa("hablar", "hablado") + vpa("comer", "comido") + vpa("vivir", "vivido")),
)

# ---------------------------------------------------------------------------- 380
L380 = lesson(
    "Irregular participles in the perfect",
    "Hoy no he hecho nada. ¿Has visto el resultado?",
    requires=["hacer", "decir", "ver", "escribir", "poner", "abrir", "volver", "romper", "morir", "resolver", "descubrir", "cubrir"],
    cards=[
        card("The participles you already know, now in use",
             "The same irregular participles you met with the passive voice (hecho, dicho, visto, escrito…) are the ones used with haber. Remember: the participle stays the same.",
             tables=[table(["Infinitivo", "Participio", "Ejemplo"],
                           [["hacer", "hecho", "No he hecho nada."],
                            ["decir", "dicho", "Nos han dicho la verdad."],
                            ["ver", "visto", "¿Has visto el resultado?"],
                            ["escribir", "escrito", "Hemos escrito un informe."],
                            ["poner", "puesto", "Ella se ha puesto un abrigo."],
                            ["abrir", "abierto", "Han abierto el hospital nuevo."],
                            ["volver", "vuelto", "Mi hermano ha vuelto de Chile."],
                            ["romper", "roto", "Me he roto la pierna."],
                            ["morir", "muerto", "El paciente ha muerto."],
                            ["descubrir", "descubierto", "Han descubierto una vacuna."]],
                           say=[2])]),
    ],
    exercises=[
        F("Hoy no he ___ nada.", "hecho", ["hacido", "hizo", "haciendo"], "hacer → hecho.", tr="Today I have not done anything.", lemma="hacer:part"),
        F("Nos han ___ la verdad.", "dicho", ["decido", "dijo", "diciendo"], "decir → dicho.", tr="They have told us the truth.", lemma="decir:part"),
        F("¿Has ___ el resultado del examen?", "visto", ["vido", "vio", "viendo"], "ver → visto.", tr="Have you seen the exam result?", lemma="ver:part"),
        F("Hemos ___ un informe sobre la vacuna.", "escrito", ["escribido", "escribió", "escribiendo"], "escribir → escrito.", tr="We have written a report on the vaccine.", lemma="escribir:part"),
        F("Han ___ el hospital nuevo.", "abierto", ["abrido", "abrió", "abriendo"], "abrir → abierto.", tr="They have opened the new hospital.", lemma="abrir:part"),
        F("Mi hermano ha ___ de Chile.", "vuelto", ["volvido", "volvió", "volviendo"], "volver → vuelto.", tr="My brother has come back from Chile.", lemma="volver:part"),
        F("Me he ___ la pierna.", "roto", ["rompido", "rompió", "rompiendo"], "romper → roto.", tr="I have broken my leg.", lemma="romper:part"),
        F("Los científicos han ___ un tratamiento nuevo.", "descubierto", ["descubrido", "descubrió", "descubriendo"], "descubrir → descubierto.", tr="The scientists have discovered a new treatment.", lemma="descubrir:part"),
        M("What is the participle of “poner”?", "puesto", ["ponido", "puso", "poniendo"], "poner → puesto.", lemma="poner:part"),
    ],
    verify=(vpa("hacer", "hecho") + vpa("decir", "dicho") + vpa("ver", "visto") + vpa("escribir", "escrito")
            + vpa("poner", "puesto") + vpa("abrir", "abierto") + vpa("volver", "vuelto") + vpa("romper", "roto")
            + vpa("morir", "muerto") + vpa("descubrir", "descubierto")),
)

# ---------------------------------------------------------------------------- 381
L381 = lesson(
    "Where do the pronouns go in the perfect?",
    "Ya lo he visto. No me ha llamado. Se lo he dicho.",
    requires=["haber", "ver", "llamar", "decir", "leer", "escribir", "película", "libro", "jefe", "carta"],
    cards=[
        card("Pronouns stand before haber",
             "Object and reflexive pronouns go in front of haber, never between haber and the participle, and never after the participle. "
             "No also goes in front of the pronouns: No lo he visto. Two pronouns go together before haber, and le/les change to se before lo, la, los, las.",
             tables=[table(["Frase", "English"],
                           [["Lo he visto.", "I have seen it."],
                            ["No me ha llamado.", "He has not called me."],
                            ["Le he escrito una carta.", "I have written him a letter."],
                            ["Se lo he dicho.", "I have told it to him."],
                            ["¿Te la han dado?", "Have they given it to you?"],
                            ["Nos hemos levantado temprano.", "We have gotten up early."]],
                           say=[0])]),
    ],
    exercises=[
        F("¿La película? Ya ___ he visto.", "la", ["lo", "los", "las"], "Película is feminine singular.", tr="The movie? I have already seen it."),
        F("¿Los libros? Ya ___ he leído.", "los", ["lo", "la", "las"], "Libros is masculine plural.", tr="The books? I have already read them."),
        F("Mi madre no me ha ___.", "llamado", ["llamar", "llamó", "llamando"], "Participle after haber.", tr="My mother has not called me.", lemma="llamar:part"),
        F("A mi jefe ya ___ lo he dicho.", "se", ["le", "me", "te"], "Le + lo becomes se lo.", tr="I have already told my boss."),
        F("Yo le ___ escrito una carta.", "he", ["has", "ha", "han"], "Yo → he; the pronoun comes first.", tr="I have written him a letter.", lemma="haber:yo"),
        F("Nosotros no ___ hemos visto todavía.", "lo", ["se", "me", "te"], "The pronoun goes before haber.", tr="We have not seen it yet."),
        F("¿Te ___ han dado la receta?", "la", ["lo", "los", "las"], "Receta is feminine singular.", tr="Have they given you the prescription?"),
        M("Which sentence puts the pronoun in the right place?", "Lo he visto.", ["He lo visto.", "He visto lo.", "Lo visto he."], "Pronouns go before haber."),
        M("Which sentence is correct?", "Se lo he dicho.", ["Le lo he dicho.", "He se lo dicho.", "Lo le he dicho."], "Le + lo → se lo."),
    ],
)

# ---------------------------------------------------------------------------- 382
L382 = lesson(
    "Already, not yet, never, ever: ya, todavía no, nunca, alguna vez",
    "Ya he comido. Todavía no he llegado.",
    requires=["ya", "todavía", "nunca", "siempre", "haber", "llegar", "comer", "estar", "terminar", "vivir"],
    cards=[
        card("Small words that go with the perfect",
             "These words usually go before haber (and before any pronouns): Ya he comido. Todavía no he llegado. Todavía can also come at the end (No he llegado todavía). Putting them between haber and the participle (he ya comido) is much less common, so learn the pattern ya + haber.",
             tables=[table(["Palabra", "Ejemplo", "English"],
                           [["ya", "Ya he comido.", "I have already eaten."],
                            ["todavía no", "Todavía no he llegado.", "I have not arrived yet."],
                            ["nunca", "Nunca he estado en Chile.", "I have never been to Chile."],
                            ["siempre", "Siempre he vivido aquí.", "I have always lived here."],
                            ["alguna vez", "¿Has estado alguna vez en Chile?", "Have you ever been to Chile?"]],
                           say=[1])]),
    ],
    exercises=[
        F("¿Has comido? — Sí, ___ he comido.", "ya", ["nunca", "todavía no", "siempre"], "Already.", tr="Have you eaten? Yes, I have already eaten."),
        F("Mi hermano está esperando: ___ no ha llegado.", "todavía", ["nunca", "siempre", "ya"], "Not yet.", tr="My brother is waiting: he has not arrived yet."),
        F("___ he estado en Chile; me gustaría ir.", "Nunca", ["Ya", "Siempre", "Todavía"], "Never.", tr="I have never been to Chile; I would like to go."),
        F("Yo siempre ___ vivido en esta ciudad.", "he", ["has", "ha", "han"], "Yo → he.", tr="I have always lived in this city.", lemma="haber:yo"),
        F("¿Has probado esta comida ___ vez?", "alguna", ["ninguna", "ya", "nunca"], "Ever (once).", tr="Have you ever tried this food?"),
        F("Nosotros ya ___ terminado el trabajo.", "hemos", ["han", "he", "ha"], "Nosotros → hemos.", tr="We have already finished the work.", lemma="haber:nosotros"),
        M("Where does ya go in “We have already eaten”?", "Ya hemos comido.", ["Ya comido hemos.", "Comido ya hemos.", "Comido hemos ya."], "Before haber (Ya hemos comido)."),
        M("Which sentence is correct?", "Todavía no he llegado.", ["No he todavía llegado.", "He todavía no llegado.", "He no llegado todavía."], "Todavía no goes before haber."),
        M("What does “nunca he estado” mean?", "I have never been", ["I am never here", "I was always here", "I will never be"], "Nunca = never."),
    ],
)

# ---------------------------------------------------------------------------- 383
L383 = lesson(
    "Present perfect or preterite?",
    "Ayer fui al médico. Esta semana he tenido fiebre.",
    requires=["ir", "tener", "estar", "dormir", "poner", "volver", "ayer", "semana", "anoche", "mes"],
    cards=[
        card("Finished time, or time that is still open?",
             "A time word that points to a finished period (ayer, anoche, la semana pasada, hace tres años) calls for the preterite. "
             "The present perfect fits periods that are not over (hoy, esta semana, este año) and experiences with no date (nunca, alguna vez, ya). "
             "Be aware that speakers differ: in Spain the perfect is common for the recent past (Esta mañana he desayunado fruta), while in much of Latin America people say Esta mañana desayuné fruta. Both are normal. What never works is the perfect with a finished time word: not ayer he ido.",
             tables=[table(["Palabra de tiempo", "Tiempo", "Ejemplo"],
                           [["ayer, anoche", "pretérito", "Ayer fui al médico."],
                            ["la semana pasada", "pretérito", "La semana pasada tuve fiebre."],
                            ["hace tres años", "pretérito", "Hace tres años mi abuelo estuvo en el hospital."],
                            ["esta semana, hoy", "perfecto (o pretérito)", "Esta semana he tenido fiebre."],
                            ["nunca, alguna vez, ya", "perfecto (ya also takes the preterite in much of Latin America: Ya comí)", "Nunca he estado enfermo."]],
                           say=[2])]),
    ],
    exercises=[
        F("Ayer ___ al médico.", "fui", ["he ido", "ido", "voy"], "A finished day → preterite.", tr="Yesterday I went to the doctor.", lemma="ir:yo:pret"),
        F("La semana pasada ___ fiebre.", "tuve", ["he tenido", "tenido", "tengo"], "A finished week → preterite.", tr="Last week I had a fever.", lemma="tener:yo:pret"),
        F("Hace tres años, mi abuelo ___ en el hospital.", "estuvo", ["ha estado", "estado", "está"], "Hace + time (finished) → preterite.", tr="Three years ago, my grandfather was in the hospital.", lemma="estar:él:pret"),
        F("El año pasado, mis padres ___ de Cuba.", "volvieron", ["han vuelto", "vuelto", "vuelven"], "El año pasado → preterite.", tr="Last year, my parents came back from Cuba.", lemma="volver:ellos:pret"),
        F("Anoche no ___ bien.", "dormí", ["he dormido", "dormido", "duermo"], "Anoche → preterite.", tr="Last night I did not sleep well.", lemma="dormir:yo:pret"),
        F("El mes pasado, la enfermera me ___ la vacuna.", "puso", ["ha puesto", "puesto", "pone"], "El mes pasado → preterite.", tr="Last month, the nurse gave me the vaccine.", lemma="poner:ella:pret"),
        M("Which time word calls for the preterite?", "la semana pasada", ["esta semana", "hoy", "este año"], "A finished period."),
        M("Which time word points to a period that is not over yet?", "este mes", ["el mes pasado", "ayer", "anoche"], "Este mes is still open."),
        M("In much of Latin America, how do people often say “Esta mañana he desayunado fruta”?", "Esta mañana desayuné fruta.", ["Esta mañana desayunaré fruta.", "Esta mañana voy a desayunar fruta.", "Esta mañana desayunando fruta."], "The preterite replaces the perfect for the recent past."),
    ],
)

# ---------------------------------------------------------------------------- 384
L384 = lesson(
    "Ha habido: there has been",
    "Ha habido un accidente. Ha habido varios accidentes.",
    requires=["haber", "accidente", "herido", "hospital", "cama", "terremoto", "gente", "carretera"],
    cards=[
        card("Impersonal haber has one form",
             "When haber means “there is / there are”, it never changes for singular or plural: hay, hubo, había, ha habido. "
             "So you say Ha habido tres accidentes, not Han habido tres accidentes.",
             tables=[table(["Tiempo", "Forma", "Ejemplo"],
                           [["presente", "hay", "Hay un accidente en la carretera."],
                            ["pretérito", "hubo", "Ayer hubo un accidente en la carretera."],
                            ["imperfecto", "había", "Cuando llegamos, ya había mucha gente."],
                            ["perfecto", "ha habido", "Esta semana ha habido tres accidentes."]],
                           say=[2])]),
    ],
    exercises=[
        F("Esta semana ___ habido muchos accidentes en la carretera.", "ha", ["han", "hay", "hubo"], "Impersonal haber stays singular.", tr="This week there have been many accidents on the highway.", lemma="haber:él"),
        F("Hasta ahora no ___ habido heridos.", "ha", ["han", "hay", "he"], "Impersonal haber stays singular.", tr="So far there have been no injured people.", lemma="haber:él"),
        F("Esta mañana ___ habido un terremoto pequeño.", "ha", ["han", "hay", "hemos"], "Singular: un terremoto.", tr="This morning there has been a small earthquake.", lemma="haber:él"),
        F("Ayer ___ un accidente en la carretera.", "hubo", ["ha habido", "hay", "había habido"], "Ayer → preterite.", tr="Yesterday there was an accident on the highway."),
        F("Cuando llegamos, ya ___ mucha gente en el hospital.", "había", ["hubo", "ha habido", "hay"], "Setting the scene → imperfect.", tr="When we arrived, there were already many people at the hospital.", lemma="haber:él:impf"),
        F("Ahora mismo no ___ camas libres en el hospital.", "hay", ["hubo", "ha habido", "habrá"], "Right now → present.", tr="Right now there are no free beds in the hospital."),
        M("Which sentence is correct?", "Ha habido tres accidentes.", ["Han habido tres accidentes.", "Hay habido tres accidentes.", "Ha hay tres accidentes."], "Impersonal haber stays singular."),
        M("What does “Ha habido un accidente” mean?", "There has been an accident", ["He has an accident", "There will be an accident", "There was one long ago"], "Ha habido = there has been."),
        M("Why is it “ha habido muchos heridos” and not “han habido”?", "Impersonal haber never takes a plural form", ["Heridos is singular", "Han is only used in formal speech", "Habido is a plural participle"], "Hay, hubo, había, ha habido: always one form."),
    ],
)

# ---------------------------------------------------------------------------- 385
L385 = lesson(
    "How have you been?",
    "¿Cómo has estado? ¿Qué has hecho? ¿Cómo te ha ido?",
    requires=["estar", "hacer", "ir", "haber", "bien", "trabajo", "ocupado", "mucho"],
    cards=[
        card("Greeting an old friend with the perfect",
             "When you have not seen someone for a while, the present perfect is the natural tense for catching up. "
             "With usted, the questions use ha: ¿Cómo ha estado usted?",
             tables=[table(["Pregunta", "Respuesta posible"],
                           [["¿Cómo has estado?", "He estado muy bien, gracias."],
                            ["¿Qué has hecho?", "He trabajado mucho."],
                            ["¿Cómo te ha ido?", "Me ha ido muy bien."],
                            ["¿Cómo te ha ido en el trabajo?", "Me ha ido regular; he estado muy ocupado."],
                            ["¿Qué hay de nuevo?", "Nada nuevo."],
                            ["¿Cómo ha estado usted?", "Muy bien, gracias."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Oye, Marta, ¿cómo ___ estado?", "has", ["ha", "he", "han"], "Informal tú → has.", tr="Hey, Marta, how have you been?", lemma="haber:tú"),
        F("Señora Díaz, ¿cómo ___ estado usted?", "ha", ["has", "he", "hemos"], "Formal usted → ha.", tr="Mrs. Díaz, how have you been?", lemma="haber:usted"),
        F("¿Cómo te ___ ido en el trabajo?", "ha", ["has", "he", "hemos"], "Third person: ha ido (it has gone).", tr="How has work been going for you?", lemma="haber:él"),
        F("Yo ___ estado muy ocupado esta semana.", "he", ["has", "ha", "han"], "Yo → he.", tr="I have been very busy this week.", lemma="haber:yo"),
        F("Oye, Luis, ¿qué ___ hecho hoy?", "has", ["ha", "he", "han"], "Informal tú → has.", tr="Hey, Luis, what have you done today?", lemma="haber:tú"),
        F("Nosotros ___ estado bien, gracias.", "hemos", ["han", "he", "has"], "Nosotros → hemos.", tr="We have been fine, thank you.", lemma="haber:nosotros"),
        F("Mis padres ___ estado en el hospital con mi abuela.", "han", ["ha", "hemos", "has"], "Ellos → han.", tr="My parents have been at the hospital with my grandmother.", lemma="haber:ellos"),
        M("A friend asks “¿Cómo has estado?” Which answer fits?", "He estado muy ocupado, pero bien.", ["Me llamo Pedro.", "Soy de Chile.", "Son las tres."], "He estado = I have been."),
        M("Which question means “What have you been up to?”", "¿Qué has hecho?", ["¿Qué hora es?", "¿Dónde vives?", "¿Cómo te llamas?"], "Qué has hecho = what have you done."),
    ],
)

# ---------------------------------------------------------------------------- 386
L386 = lesson(
    "He estado enfermo: health states in the perfect",
    "Mi madre ha estado enferma toda la semana.",
    requires=["estar", "haber", "enfermo", "cansado", "preocupado", "ocupado", "sano", "madre", "padre", "semana"],
    cards=[
        card("Haber + estado + adjective",
             "To say how you or others have been, use haber + estado + an adjective. The adjective agrees with the person, but estado never changes.",
             tables=[table(["Sujeto", "Frase", "English"],
                           [["yo (hombre)", "He estado enfermo.", "I have been sick."],
                            ["yo (mujer)", "He estado enferma.", "I have been sick."],
                            ["mi madre", "Mi madre ha estado cansada.", "My mother has been tired."],
                            ["mis hijos", "Mis hijos han estado enfermos.", "My children have been sick."],
                            ["nosotras", "Hemos estado preocupadas.", "We have been worried."]],
                           say=[1])]),
    ],
    exercises=[
        F("Mi madre ha estado ___ toda la semana.", "enferma", ["enfermo", "enfermos", "enfermas"], "Madre is feminine singular.", tr="My mother has been sick all week."),
        F("Mis hijos han estado ___ del estómago.", "enfermos", ["enfermo", "enferma", "enfermas"], "Hijos is masculine plural.", tr="My children have been sick with a stomach illness."),
        F("Marta dice: «He estado muy ___ esta semana».", "cansada", ["cansado", "cansados", "cansadas"], "Marta is a woman.", tr="Marta says: “I have been very tired this week.”"),
        F("Pedro dice: «He estado muy ___ con el trabajo».", "ocupado", ["ocupada", "ocupados", "ocupadas"], "Pedro is a man.", tr="Pedro says: “I have been very busy with work.”"),
        F("Rosa dice: Mi hermana y yo hemos estado ___ por nuestro padre.", "preocupadas", ["preocupado", "preocupada", "preocupados"], "Two women: feminine plural.", tr="Rosa says: My sister and I (both women) have been worried about our father."),
        F("Mi padre ha ___ enfermo, pero ahora está mejor.", "estado", ["estada", "estados", "sido"], "Estado never changes.", tr="My father has been sick, but now he is better.", lemma="estar:part"),
        M("In “Mi madre ha estado cansada”, why does the adjective end in -a?", "It agrees with madre", ["It agrees with ha", "It agrees with estado", "It is always feminine"], "Adjectives agree with the person."),
        M("Which sentence is correct?", "Mis piernas han estado cansadas.", ["Mis piernas han estado cansado.", "Mis piernas ha estado cansadas.", "Mis piernas han estados cansadas."], "Plural subject, plural adjective, invariable estado."),
        M("What does “Hemos estado sanos” mean?", "We have been healthy", ["We are going to be healthy", "We were sick", "We will be healthy"], "Sano = healthy."),
    ],
    verify=vpa("estar", "estado"),
)

# ---------------------------------------------------------------------------- 387
L387 = lesson(
    "Reading: dengue cases are rising",
    "Las autoridades han informado de un aumento de los casos.",
    requires=["autoridad", "informar", "aumento", "aumentar", "caso", "enfermedad", "fiebre", "dolor", "lluvia", "región", "grave", "registrar", "médico", "recomendar"],
    cards=[
        card("A news report with the present perfect",
             "News reports use the present perfect to bring recent events to the reader’s present: the authorities have reported, the cases have risen. Read the article, then try the exercises.",
             examples=[
                 ex("Las autoridades de salud han informado de un aumento de los casos de dengue en varias regiones.", "Health authorities have reported an increase in dengue cases in several regions.", "han informado"),
                 ex("El dengue es una enfermedad que transmite un mosquito.", "Dengue is a disease transmitted by a mosquito.", "transmite"),
                 ex("Las personas enfermas tienen fiebre alta, dolor de cabeza y dolor de músculos y huesos.", "Sick people have a high fever, a headache, and muscle and bone pain.", "tienen"),
                 ex("Los casos han aumentado después de las lluvias fuertes.", "The cases have risen after the heavy rains.", "han aumentado"),
                 ex("Hasta ahora no se ha registrado ningún caso grave en la capital.", "So far no serious case has been recorded in the capital.", "se ha registrado"),
                 ex("Los médicos recomiendan eliminar el agua que queda en los patios.", "Doctors recommend getting rid of the water left in yards.", "recomiendan"),
             ]),
    ],
    exercises=[
        F("Las autoridades ___ informado de un aumento de los casos.", "han", ["ha", "hemos", "he"], "Autoridades is plural.", tr="The authorities have reported an increase in the cases.", lemma="haber:ellos"),
        F("Los casos ___ aumentado después de las lluvias.", "han", ["ha", "hemos", "he"], "Casos is plural.", tr="The cases have risen after the rains.", lemma="haber:ellos"),
        F("Hasta ahora no se ___ registrado ningún caso grave.", "ha", ["han", "hay", "he"], "Ningún caso is singular.", tr="So far no serious case has been recorded.", lemma="haber:él"),
        F("El dengue lo transmite un ___.", "mosquito", ["hospital", "médico", "dolor"], "A mosquito carries it.", tr="Dengue is transmitted by a mosquito."),
        F("Los médicos ___ eliminar el agua que queda en los patios.", "recomiendan", ["recomiendo", "recomendamos", "recomendar"], "Médicos is plural.", tr="Doctors recommend getting rid of the water left in yards.", lemma="recomendar:ellos"),
        M("How is dengue transmitted?", "By a mosquito", ["By food", "By a vaccine", "By water pills"], "Un mosquito."),
        M("Why have the cases risen?", "Because of the heavy rains", ["Because of a new vaccine", "Because of a hospital strike", "Because of cold weather"], "Las lluvias fuertes."),
        M("Which symptom does the article mention?", "High fever", ["A broken leg", "A sore knee", "Loss of hair"], "Fiebre alta."),
        M("What has been recorded in the capital so far?", "No serious cases", ["Hundreds of deaths", "A new vaccine", "A hospital closure"], "Ningún caso grave."),
    ],
    verify=vp("recomendar", "recomiendo", "recomiendas", "recomienda", "recomendamos", "recomendáis", "recomiendan"),
)

# ---------------------------------------------------------------------------- 388
L388 = lesson(
    "Preventing infection: advice with formal commands",
    "Lávese las manos con frecuencia. Evite el contacto con personas enfermas.",
    requires=["evitar", "lavar", "mano", "frecuencia", "contacto", "consultar", "médico", "usar", "beber", "llamar", "compartir", "descansar"],
    cards=[
        card("Health advice in the formal command",
             "Public-health advice addresses the reader as usted (one person) or ustedes (a group). Review: drop the -o of the yo form and add -e / -en for -ar verbs, -a / -an for -er and -ir verbs. Pronouns attach to an affirmative command and go before a negative one.",
             tables=[table(["Consejo", "English"],
                           [["Lávese las manos con frecuencia.", "Wash your hands often."],
                            ["Evite el contacto con personas enfermas.", "Avoid contact with sick people."],
                            ["Quédese en casa si tiene fiebre.", "Stay home if you have a fever."],
                            ["Beba mucha agua y descanse.", "Drink a lot of water and rest."],
                            ["Consulte a un médico.", "See a doctor."],
                            ["No comparta los vasos ni los platos.", "Do not share glasses or plates."]],
                           say=[0])]),
    ],
    exercises=[
        F("Señor Ruiz, por favor, ___ el contacto con personas enfermas.", "evite", ["evita", "evitar", "evito"], "Formal command of evitar.", tr="Mr. Ruiz, avoid contact with sick people.", lemma="evitar:usted:cmd"),
        F("Señores, ___ mucha agua y descansen.", "beban", ["beba", "beben", "beber"], "Ustedes command of beber.", tr="Ladies and gentlemen, drink a lot of water and rest.", lemma="beber:ustedes:cmd"),
        F("Señora Díaz, ___ a un médico si no mejora.", "consulte", ["consulta", "consultar", "consulto"], "Formal command of consultar.", tr="Mrs. Díaz, see a doctor if you do not get better.", lemma="consultar:usted:cmd"),
        F("Señor Ruiz, por favor, no ___ los vasos con otras personas.", "comparta", ["comparte", "compartir", "comparto"], "Negative formal command.", tr="Mr. Ruiz, do not share glasses with other people.", lemma="compartir:usted:cmd"),
        F("Señores, por favor, ___ mascarilla en lugares cerrados.", "usen", ["usan", "usar", "usamos"], "Ustedes command of usar.", tr="Ladies and gentlemen, wear a mask in closed places.", lemma="usar:ustedes:cmd"),
        F("Señora Díaz, por favor, ___ a su médico si tiene fiebre.", "llame", ["llama", "llamar", "llamo"], "Formal command of llamar.", tr="Mrs. Díaz, call your doctor if you have a fever.", lemma="llamar:usted:cmd"),
        M("Which command is for a group of people?", "Beban agua.", ["Beba agua.", "Bebe agua.", "Bebo agua."], "Beban = ustedes."),
        M("Where does the pronoun go in “Lávese las manos”?", "After the verb, joined to it", ["Before the verb", "After the noun", "It is not needed"], "Affirmative command: attach the pronoun."),
        M("How do you say “Do not wash it” to a patient (usted)?", "No lo lave.", ["Lávelo no.", "No lávelo.", "No lave lo."], "Negative command: pronoun before the verb."),
    ],
    verify=(vpc("evitar", "evite", "eviten") + vpc("beber", "beba", "beban") + vpc("consultar", "consulte", "consulten")
            + vpc("compartir", "comparta", "compartan") + vpc("usar", "use", "usen") + vpc("llamar", "llame", "llamen")),
)

# ---------------------------------------------------------------------------- 389
L389 = lesson(
    "The doctor’s orders: commands with pronouns",
    "Tómela con agua. No se la dé al niño.",
    requires=["tomar", "pastilla", "medicina", "dar", "niño", "receta", "agua", "abrir", "comer", "cada"],
    cards=[
        card("Take it, give it, don’t give it",
             "On a prescription label or in a doctor’s office, orders come with pronouns for the medicine or the patient. "
             "Remember: in an affirmative command the pronouns attach to the verb and an accent mark keeps the stress; in a negative command they stand in front. "
             "When le or les meets lo or la, it becomes se.",
             tables=[table(["Orden afirmativa", "Orden negativa"],
                           [["Tómela con agua.", "No la tome con alcohol."],
                            ["Tómelas cada ocho horas.", "No las tome con el estómago vacío."],
                            ["Dígame los síntomas.", "No me diga que no le duele."],
                            ["Dele esta medicina al niño.", "No se la dé al niño."],
                            ["Cómalo despacio.", "No lo coma frío."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Esta pastilla, señora Ruiz, ___ con agua.", "tómela", ["la tome", "tome la", "tómala"], "Affirmative command: attach and accent.", tr="This pill, Mrs. Ruiz, take it with water."),
        F("Estas pastillas, señor Pérez, no ___ con el estómago vacío.", "las tome", ["tómelas", "las tomo", "tome las"], "Negative command: pronoun first.", tr="These pills, Mr. Pérez, do not take them on an empty stomach."),
        F("La medicina, señora, por favor, no se ___ al niño.", "la dé", ["dé la", "dála", "la da"], "Negative: se la dé (dé keeps its accent).", tr="The medicine, ma’am, do not give it to the child."),
        F("Señor Ruiz, ___ los síntomas.", "dígame", ["me diga", "diga me", "dígame los"], "Affirmative command with me.", tr="Mr. Ruiz, tell me the symptoms."),
        F("La medicina, señora, ___ al niño después de la comida.", "désela", ["se la dé", "déla se", "dése la"], "Affirmative: attach both pronouns: désela.", tr="The medicine, ma’am, give it to the child after the meal."),
        F("Señor Pérez, por favor, el jarabe, no ___ frío.", "lo tome", ["tómelo", "tome lo", "lo toma"], "Negative command: lo tome.", tr="Mr. Pérez, the syrup, do not take it cold."),
        M("Why does “tómela” have an accent mark?", "The stress stays on the same syllable after adding a pronoun", ["Because it is a question", "Because it is plural", "Because it is feminine"], "Accent keeps the original stress."),
        M("Which one is the right negative command?", "No se la dé.", ["No dése la.", "No désela.", "No dé la se."], "Pronouns before the verb."),
        M("Why do we say “se la dé” instead of “le la dé”?", "Le becomes se before la", ["Le is only for plural", "It is a spelling mistake", "Se is more polite"], "le + la/lo → se la/lo."),
    ],
)

# ---------------------------------------------------------------------------- 390
L390 = lesson(
    "Review: health and the present perfect",
    "Le duele la cabeza y no ha dormido bien.",
    requires=["doler", "haber", "hacer", "dormir", "doctor", "fiebre", "descansar", "beber", "ya", "todavía", "enfermo", "pierna"],
    cards=[
        card("Your toolbox so far",
             "Review everything from this unit in one table.",
             tables=[table(["Para decir…", "Usa…", "Ejemplo"],
                           [["something hurts", "doler + parte del cuerpo", "Me duelen las piernas."],
                            ["the perfect", "haber + participio", "He dormido poco."],
                            ["irregular participle", "hecho, dicho, visto…", "No he hecho nada."],
                            ["pronoun position", "before haber", "Ya lo he visto."],
                            ["not yet", "todavía no + haber", "Todavía no ha llegado."],
                            ["there has been", "ha habido", "Ha habido un accidente."],
                            ["advice to usted", "formal command", "Descanse y beba agua."]],
                           say=[2])]),
    ],
    exercises=[
        F("Me ___ las piernas.", "duelen", ["duele", "dolemos", "doler"], "Piernas is plural.", tr="My legs hurt.", lemma="doler:ellos"),
        F("Esta semana yo ___ dormido poco.", "he", ["has", "ha", "han"], "Yo → he.", tr="This week I have slept little.", lemma="haber:yo"),
        F("Hoy no he ___ nada.", "hecho", ["hacido", "hizo", "haciendo"], "hacer → hecho.", tr="Today I have not done anything.", lemma="hacer:part"),
        F("¿El resultado? Ya ___ he visto.", "lo", ["la", "los", "las"], "El resultado is masculine singular.", tr="The result? I have already seen it."),
        F("Mi hermano está enfermo y todavía no ___ llegado.", "ha", ["han", "he", "has"], "Él → ha.", tr="My brother is sick and has not arrived yet.", lemma="haber:él"),
        F("Esta semana ___ habido tres accidentes.", "ha", ["han", "hay", "hubo"], "Impersonal haber.", tr="This week there have been three accidents.", lemma="haber:él"),
        F("Señor Ruiz, ___ y beba mucha agua.", "descanse", ["descansa", "descansar", "descanso"], "Formal command.", tr="Mr. Ruiz, rest and drink a lot of water.", lemma="descansar:usted:cmd"),
        F("Ayer ___ al médico.", "fui", ["he ido", "ido", "voy"], "Ayer → preterite.", tr="Yesterday I went to the doctor.", lemma="ir:yo:pret"),
        M("Which sentence is correct?", "Ya lo he leído.", ["Ya he lo leído.", "He ya lo leído.", "Ya he leído lo."], "Pronoun before haber."),
        M("In “Mis hijas han estado enfermas”, which word does not change?", "estado", ["enfermas", "hijas", "han"], "Estado is invariable."),
    ],
)

UNIT = unit("La salud y el presente perfecto", [
    L375, L376, L377, L378, L379, L380, L381, L382, L383, L384, L385, L386, L387, L388, L389, L390,
])

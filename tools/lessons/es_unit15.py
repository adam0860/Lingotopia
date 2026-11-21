"""Unit 15: review of Unit 3 - food, celebrations, travel, lodging (textbook Chapter 15)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 222
L222 = lesson(
    "Following a recipe: commands",
    "Corte la cebolla. Agregue los frijoles. Cubra la olla.",
    requires=["arroz", "agua", "sal", "cortar", "dejar", "cocinar", "servir", "receta"],
    cards=[
        card("Recipes use formal commands",
             "Recipes in Spanish are usually written with usted commands. Here is a recipe for beans and rice. Notice "
             "each verb: dejar, cortar, freír, agregar, cubrir, cocinar, servir.",
             tables=[table(["Paso", "Instrucción"],
                           [["Uno", "Deje los frijoles en agua una noche antes de cocinar."],
                            ["Dos", "Corte la cebolla y el tomate."],
                            ["Tres", "Fría la cebolla y el tomate con mantequilla."],
                            ["Cuatro", "Agregue los frijoles y el agua."],
                            ["Cinco", "Cubra la olla y cocine a fuego lento."],
                            ["Seis", "Cocine el arroz blanco aparte."],
                            ["Siete", "Sirva todo caliente."]],
                           say=[1])]),
        card("Cooking words",
             "A fuego lento means on low heat. La olla is the pot and la sartén is the frying pan. Agregar and añadir "
             "both mean to add; cubrir means to cover.",
             examples=[
                 ex("Corte la cebolla en cuadritos.", "Cut the onion into small cubes.", "Corte"),
                 ex("Agregue un poco de sal.", "Add a little salt.", "Agregue"),
                 ex("Cubra la olla y cocine a fuego lento.", "Cover the pot and cook over low heat.", "Cubra"),
                 ex("Sirva la sopa caliente.", "Serve the soup hot.", "Sirva"),
             ]),
    ],
    exercises=[
        F("___ los frijoles en agua una noche.", "Deje", ["Deja", "Dejo", "Dejen"], "Usted command of dejar.", tr="Leave the beans in water overnight.", lemma="dejar:usted:cmd"),
        F("___ la cebolla y el tomate.", "Corte", ["Corta", "Corto", "Corten"], "Usted command of cortar.", tr="Cut the onion and the tomato.", lemma="cortar:usted:cmd"),
        F("___ los frijoles y el agua.", "Agregue", ["Agrega", "Agrego", "Agreguen"], "Agregar → agregue (g → gu).", tr="Add the beans and the water.", lemma="agregar:usted:cmd"),
        F("___ la olla y cocine a fuego lento.", "Cubra", ["Cubre", "Cubro", "Cubran"], "Cubrir → cubro → cubra.", tr="Cover the pot and cook over low heat.", lemma="cubrir:usted:cmd"),
        F("___ el arroz blanco aparte.", "Cocine", ["Cocina", "Cocino", "Cocinen"], "Usted command of cocinar.", tr="Cook the white rice separately.", lemma="cocinar:usted:cmd"),
        F("___ todo caliente.", "Sirva", ["Sirve", "Sirvo", "Sirvan"], "Servir → sirvo → sirva.", tr="Serve everything hot.", lemma="servir:usted:cmd"),
        M("What does “a fuego lento” mean?", "over low heat", ["over high heat", "very quickly", "without fire"], "Lento = slow."),
        M("Which verb means “to cover”?", "cubrir", ["cortar", "agregar", "dejar"], "Cubrir = to cover."),
        M("Why are recipe steps written with “Corte”, “Agregue”?", "They are usted commands", ["They are past tense", "They are plural nouns", "They are questions"], "Recipes give instructions."),
    ],
    verify=vpc("dejar", "deje", "dejen") + vpc("cortar", "corte", "corten") + vpc("agregar", "agregue", "agreguen")
           + vpc("cubrir", "cubra", "cubran") + vpc("cocinar", "cocine", "cocinen") + vpc("servir", "sirva", "sirvan"),
)

# ---------------------------------------------------------------------------- 223
L223 = lesson(
    "What do I do with it? Pronouns in recipes",
    "¿Qué hago con los frijoles? Hay que dejarlos en agua.",
    requires=["cortar", "dejar", "cocinar", "deber", "necesitar", "tener", "receta"],
    cards=[
        card("Asking and answering about ingredients",
             "When you ask ¿Qué hago con…? and the answer repeats the noun, use a direct object pronoun instead. With "
             "an expression plus an infinitive (tienes que, debes, necesitas), the pronoun can go before the "
             "first verb or attach to the infinitive. With hay que the pronoun can only attach to the infinitive: Hay que cocinarlo.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Qué hago con los frijoles?", "Tienes que dejarlos en agua."],
                            ["¿Qué hago con la cebolla?", "La tienes que cortar."],
                            ["¿Qué hago con el arroz?", "Hay que cocinarlo aparte."],
                            ["¿Qué hago con las chuletas?", "Las debes freír en una sartén."]],
                           say=[0, 1])]),
        card("Both positions work",
             "Los tienes que dejar and Tienes que dejarlos mean the same thing. When you attach the pronoun to the "
             "infinitive, no accent is needed on a regular infinitive (dejarlos, cortarla), but freír needs it: freírlos.",
             examples=[
                 ex("Los tienes que dejar en agua.", "You have to leave them in water.", "Los"),
                 ex("Tienes que cortarla en cuadritos.", "You have to cut it into small cubes.", "cortarla"),
                 ex("Hay que cocinarlo aparte.", "It has to be cooked separately.", "cocinarlo"),
                 ex("Debes freírlos con mantequilla.", "You must fry them in butter.", "freírlos"),
             ]),
    ],
    exercises=[
        F("¿Qué hago con la cebolla? Tienes que ___.", "cortarla", ["cortarlo", "cortarlas", "cortarlos"], "Cebolla → -la.", tr="What do I do with the onion? You have to cut it."),
        F("¿Qué hago con los frijoles? Hay que ___ en agua.", "dejarlos", ["dejarlo", "dejarla", "dejarlas"], "Frijoles → -los.", tr="What do I do with the beans? You have to leave them in water."),
        F("¿Qué hago con el arroz? ___ tienes que cocinar aparte.", "Lo", ["La", "Los", "Las"], "Arroz → lo.", tr="What do I do with the rice? You have to cook it separately."),
        F("¿Qué hago con la carne? ___ debes freír en una sartén.", "La", ["Lo", "Los", "Las"], "Carne → la.", tr="What do I do with the meat? You must fry it in a pan."),
        F("¿Qué hago con los huevos? Necesitas ___.", "freírlos", ["freírlo", "freírla", "freírlas"], "Huevos → -los; freír keeps its accent.", tr="What do I do with the eggs? You need to fry them."),
        M("Which sentence means the same as “Los tienes que dejar”?", "Tienes que dejarlos.", ["Tienes que los dejar.", "Los tienes dejar que.", "Tienes dejar que los."], "Before the first verb or on the infinitive."),
        M("What does “Hay que cocinarlo aparte” mean?", "It has to be cooked separately.", ["You cook it with others.", "We cooked it yesterday.", "They cook it daily."], "Aparte = separately."),
        M("Which pronoun replaces “las chuletas”?", "las", ["lo", "la", "los"], "Chuletas is feminine plural."),
        M("Where may the pronoun go with “tienes que dejar”?", "before tienes or on dejar", ["only after que", "only at the end of the sentence", "in the middle of dejar"], "Both positions are correct."),
    ],
)

# ---------------------------------------------------------------------------- 224
L224 = lesson(
    "The Three Kings: a celebration in the preterite",
    "Los niños se durmieron temprano. Yo busqué la figura.",
    requires=["dormir", "vestir", "servir", "pedir", "buscar", "jugar", "explicar", "regalo", "niño"],
    cards=[
        card("El Día de los Reyes Magos",
             "In many Spanish-speaking countries children receive gifts on January sixth, el Día de los Reyes Magos. "
             "The traditional treat is the rosca de Reyes, a ring-shaped bread with a small figure of the baby Jesus "
             "baked inside. Whoever finds the figure must host a party on February second, el Día de la Candelaria (traditionally with tamales).",
             examples=[
                 ex("El cinco de enero los niños se durmieron temprano.", "On January fifth the children went to sleep early.", "se durmieron"),
                 ex("La mañana siguiente se vistieron y bajaron a buscar los regalos.", "The next morning they got dressed and went down to look for the gifts.", "se vistieron"),
                 ex("Yo les entregué varios paquetes y ellos se divirtieron con los juguetes.", "I gave them several packages and they had fun with the toys.", "entregué"),
                 ex("Después ellos pidieron la rosca y yo la coloqué en el centro de la mesa.", "Afterwards they asked for the rosca and I placed it in the middle of the table.", "pidieron"),
                 ex("Yo busqué la figura en mi trozo, pero no la encontré.", "I looked for the figure in my piece, but I didn’t find it.", "busqué"),
                 ex("La figura cayó en el plato de Pablo.", "The figure fell onto Pablo’s plate.", "cayó"),
             ]),
        card("The verbs in the story",
             "Notice the types: stem changes (se durmieron, pidieron, se vistieron, se divirtieron), spelling changes "
             "(entregué, busqué, coloqué), and the y-change (cayó).",
             tables=[table(["Tipo", "Ejemplo"],
                           [["cambio de raíz", "se durmieron, pidieron, se vistieron"],
                            ["cambio ortográfico", "entregué, busqué, coloqué"],
                            ["vocal y", "cayó"]],
                           say=[1])]),
    ],
    exercises=[
        F("Los niños se ___ temprano.", "durmieron", ["dormieron", "duermen", "durmió"], "Ellos → durmieron.", tr="The children went to sleep early.", lemma="dormir:ellos:pret"),
        F("Yo les ___ varios paquetes.", "entregué", ["entregó", "entrego", "entregaron"], "Yo → entregué.", tr="I handed them several packages.", lemma="entregar:yo:pret"),
        F("Los niños se ___ mucho con los juguetes.", "divirtieron", ["divirtió", "divertieron", "divierten"], "Ellos → divirtieron.", tr="The children had a lot of fun with the toys.", lemma="divertir:ellos:pret"),
        F("Yo ___ la figura en mi trozo, pero no la encontré.", "busqué", ["buscó", "busco", "buscaron"], "Yo → busqué.", tr="I looked for the figure in my piece, but I didn’t find it.", lemma="buscar:yo:pret"),
        F("La figura ___ en el plato de Pablo.", "cayó", ["cayeron", "caí", "cae"], "La figura → cayó.", tr="The figure fell onto Pablo’s plate.", lemma="caer:él:pret"),
        F("Yo les ___ a los niños que ahora le toca a Pablo.", "expliqué", ["explicó", "explico", "explicaron"], "Yo → expliqué.", tr="I explained to the children that it is Pablo’s turn now.", lemma="explicar:yo:pret"),
        M("When is “el Día de los Reyes Magos”?", "January sixth", ["December twenty-fifth", "January first", "February second"], "El seis de enero."),
        M("What does the person who finds the figure have to do?", "host a party", ["pay the bill", "bake a new rosca", "leave the house"], "On the Día de la Candelaria."),
        M("Which verb in the story shows the y-change?", "cayó", ["entregué", "se durmieron", "busqué"], "Caer → cayó."),
    ],
    verify=vpp("dormir", "dormí", "dormiste", "durmió", "dormimos", "dormisteis", "durmieron")
           + vpp("entregar", "entregué", "entregaste", "entregó", "entregamos", "entregasteis", "entregaron")
           + vpp("divertir", "divertí", "divertiste", "divirtió", "divertimos", "divertisteis", "divirtieron")
           + vpp("explicar", "expliqué", "explicaste", "explicó", "explicamos", "explicasteis", "explicaron"),
)

# ---------------------------------------------------------------------------- 225
L225 = lesson(
    "Buying gifts: every kind of object pronoun",
    "Se los compro. Me los traen. Nos piden regalos.",
    requires=["comprar", "regalo", "hijo", "traer", "pedir", "tienda"],
    cards=[
        card("A parent’s shopping day",
             "The Three Kings bring the gifts, but the parents buy them. Notice all the pronouns in this small story: "
             "direct (lo, la, los, las), indirect (me, te, le, nos, les) and double (se lo, se la, se los, se las).",
             examples=[
                 ex("Mis hijos nos piden regalos.", "My children ask us for gifts.", "nos"),
                 ex("Mi esposo y yo les compramos juguetes.", "My husband and I buy them toys.", "les"),
                 ex("Compré un carro eléctrico para mi hijo. Se lo compré en la tienda.", "I bought an electric car for my son. I bought it for him at the store.", "Se lo"),
                 ex("Mi esposo pone los regalos en la sala. Los pone antes de acostarnos.", "My husband puts the gifts in the living room. He puts them there before we go to bed.", "Los"),
                 ex("Los Reyes les traen los regalos a los niños. Se los traen por la noche.", "The Three Kings bring the gifts to the children. They bring them at night.", "Se los"),
             ]),
        card("How to choose",
             "First decide whether the pronoun stands for a person who receives (indirect) or a thing (direct). "
             "If there are two, put the indirect first, and change le or les to se before lo, la, los, las.",
             tables=[table(["Frase con nombres", "Con pronombres"],
                           [["Compré un carro a mi hijo.", "Se lo compré."],
                            ["Mandé las tarjetas a mis tíos.", "Se las mandé."],
                            ["Mi madre me dio el libro.", "Me lo dio."],
                            ["Mi padre nos trajo los boletos.", "Nos los trajo."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Mis hijos piden regalos. Mis hijos ___ piden regalos.", "nos", ["me", "les", "se"], "A nosotros → nos.", tr="My children ask for gifts. My children ask us for gifts."),
        F("Mi esposo y yo compramos juguetes a los niños. Mi esposo y yo ___ compramos juguetes.", "les", ["le", "nos", "se"], "A los niños → les.", tr="My husband and I buy toys for the children. We buy them toys."),
        F("Compré el carro eléctrico para mi hijo. ___ lo compré en la tienda.", "Se", ["Le", "Me", "Te"], "Le + lo → se lo.", tr="I bought the electric car for my son. I bought it for him at the store."),
        F("Mi esposo pone los regalos en la sala. ___ pone antes de acostarnos.", "Los", ["Lo", "Las", "Les"], "Regalos is masculine plural.", tr="My husband puts the gifts in the living room. He puts them there before we go to bed."),
        F("Los Reyes traen los regalos a los niños. Se los ___ por la noche.", "traen", ["trae", "traigo", "traes"], "Los Reyes → ellos: traen.", tr="The Three Kings bring the gifts to the children. They bring them at night.", lemma="traer:ellos"),
        M("What does “Se lo compré” mean?", "I bought it for him (her).", ["He bought it for me.", "I bought it for myself.", "They bought it for us."], "Se = to him or her."),
        M("Which sentence replaces “las tarjetas a mis tíos”?", "Se las mandé.", ["Les las mandé.", "Se los mandé.", "Las se mandé."], "Tarjetas → las; les → se."),
        M("What does “Nos los trajo” mean?", "He brought them to us.", ["He brought us to them.", "We brought them to him.", "They brought us."], "Nos = to us; los = them."),
        M("In a double pronoun, which comes first?", "the indirect one", ["the direct one", "the one with s", "the plural one"], "Indirect, then direct (ID)."),
    ],
    verify=vp("traer", "traigo", "traes", "trae", "traemos", "traéis", "traen"),
)

# ---------------------------------------------------------------------------- 226
L226 = lesson(
    "Verbs like gustar",
    "Me gusta la música. Le encantan los regalos. Te molesta el ruido.",
    requires=["gustar", "encantar", "molestar", "interesar", "importar", "música", "fiesta", "ruido"],
    cards=[
        card("The thing liked is the subject",
             "Gustar and similar verbs work backwards from English: the thing that pleases is the subject, and the "
             "person is an indirect object (me, te, le, nos, les). So the verb agrees with the thing, not the person. "
             "Singular thing or an infinitive → gusta; plural thing → gustan.",
             tables=[table(["Verbo", "Singular", "Plural"],
                           [["gustar", "Me gusta la música.", "Me gustan los regalos."],
                            ["encantar", "Te encanta la fiesta.", "Te encantan las fiestas."],
                            ["molestar", "Le molesta el ruido.", "Le molestan los ruidos."],
                            ["aburrir", "Nos aburre esperar.", "Nos aburren las esperas."],
                            ["interesar", "Les interesa la historia.", "Les interesan los museos."]],
                           say=[1, 2])]),
        card("Who is it about?",
             "Add a + a name or pronoun for emphasis or clarity: A mí me gusta la música. A mi hermana le encanta "
             "bailar. A nosotros nos molesta el ruido. Make it negative with no before the pronoun: No me gusta "
             "esperar.",
             examples=[
                 ex("A mí me gusta la música.", "I like music.", "A mí me gusta"),
                 ex("A mis hijos les encantan los juguetes.", "My children love toys.", "les encantan"),
                 ex("A mi hermana le encanta bailar.", "My sister loves to dance.", "le encanta"),
                 ex("A nosotros nos molesta el ruido.", "The noise bothers us.", "nos molesta"),
                 ex("No me gusta esperar en el aeropuerto.", "I don’t like waiting at the airport.", "No me gusta"),
             ]),
    ],
    exercises=[
        F("A mí me ___ la música.", "gusta", ["gustan", "gusto", "gustas"], "Música is singular.", tr="I like music.", lemma="gustar:él"),
        F("A mis hijos les ___ los juguetes.", "encantan", ["encanta", "encanto", "encantas"], "Juguetes is plural.", tr="My children love toys.", lemma="encantar:ellos"),
        F("A mi hermana le ___ bailar.", "encanta", ["encantan", "encanto", "encantas"], "An infinitive takes the singular.", tr="My sister loves to dance.", lemma="encantar:él"),
        F("A nosotros ___ molesta el ruido.", "nos", ["les", "me", "se"], "A nosotros → nos.", tr="The noise bothers us."),
        F("A ti ___ aburren las fiestas largas.", "te", ["le", "les", "nos"], "A ti → te.", tr="Long parties bore you."),
        M("In “Me gustan los regalos”, why is the verb “gustan”?", "Because “los regalos” is plural", ["Because me is plural", "Because the verb is past tense", "Because gustar is irregular"], "The verb agrees with the thing liked."),
        M("What does “Le molesta el ruido” mean?", "The noise bothers him (her).", ["He bothers the noise.", "The noise likes him.", "They bother the noise."], "Molestar = to bother."),
        M("How do you say “I don’t like waiting”?", "No me gusta esperar.", ["Me no gusta esperar.", "No gusto esperar.", "No me gustan esperar."], "No goes before the pronoun."),
        M("Which sentence is correct for “My parents love the beach”?", "A mis padres les encanta la playa.", ["A mis padres le encanta la playa.", "A mis padres les encantan la playa.", "A mis padres se encanta la playa."], "Les for plural people; encanta for singular thing."),
    ],
    verify=vp("gustar", "gusto", "gustas", "gusta", "gustamos", "gustáis", "gustan")
           + vp("encantar", "encanto", "encantas", "encanta", "encantamos", "encantáis", "encantan")
           + vp("molestar", "molesto", "molestas", "molesta", "molestamos", "molestáis", "molestan")
           + vp("aburrir", "aburro", "aburres", "aburre", "aburrimos", "aburrís", "aburren")
           + vp("interesar", "intereso", "interesas", "interesa", "interesamos", "interesáis", "interesan"),
)

# ---------------------------------------------------------------------------- 227
L227 = lesson(
    "Celebrations: what do you like and dislike?",
    "Me encanta mi cumpleaños. Me aburre una fiesta larga.",
    requires=["cumpleaños", "fiesta", "regalo", "familia", "gustar", "encantar", "molestar", "boda"],
    cards=[
        card("Celebration words",
             "Celebrations are happy occasions, but everyone has opinions. Use gustar-type verbs with the reason after "
             "porque.",
             tables=[table(["Palabra", "English"],
                           [["el cumpleaños", "birthday"],
                            ["la Navidad", "Christmas"],
                            ["el Año Nuevo", "New Year"],
                            ["el Día de los Reyes Magos", "Three Kings’ Day"],
                            ["la boda", "wedding"],
                            ["la fiesta", "party"],
                            ["el día festivo", "holiday"],
                            ["la celebración", "celebration"]],
                           say=[0])]),
        card("Giving opinions",
             "Ask ¿Cuál es la celebración que más te gusta? and answer with Me encanta…, porque…. Use le or les with "
             "another person: A mi madre le encanta la Navidad porque toda la familia viene a su casa.",
             examples=[
                 ex("¿Cuál es la celebración que más te gusta?", "Which celebration do you like most?", "más te gusta"),
                 ex("Me encanta mi cumpleaños porque mi familia me regala cosas.", "I love my birthday because my family gives me things.", "Me encanta"),
                 ex("A mi madre le encanta la Navidad.", "My mother loves Christmas.", "le encanta"),
                 ex("Me aburre una fiesta muy larga.", "A very long party bores me.", "Me aburre"),
                 ex("A mi padre le molesta el ruido de las fiestas.", "The noise of parties bothers my father.", "le molesta"),
             ]),
    ],
    exercises=[
        F("¿Cuál es la celebración que más te ___?", "gusta", ["gustas", "gusto", "gustan"], "La celebración → gusta.", tr="Which celebration do you like most?", lemma="gustar:él"),
        F("Me ___ mi cumpleaños porque mi familia me regala cosas.", "encanta", ["encantan", "encanto", "encantas"], "Cumpleaños is singular.", tr="I love my birthday because my family gives me things.", lemma="encantar:él"),
        F("A mi madre ___ encanta la Navidad.", "le", ["les", "me", "se"], "A mi madre → le.", tr="My mother loves Christmas."),
        F("A mis padres ___ molesta el ruido de las fiestas.", "les", ["le", "nos", "te"], "A mis padres → les.", tr="The noise of parties bothers my parents."),
        F("Me ___ una fiesta muy larga.", "aburre", ["aburren", "aburro", "aburres"], "Fiesta is singular.", tr="A very long party bores me.", lemma="aburrir:él"),
        M("What is “el día festivo”?", "a holiday", ["a work day", "a birthday", "a wedding"], "Festivo = festive, holiday."),
        M("Which sentence says “My friends love weddings”?", "A mis amigos les encantan las bodas.", ["A mis amigos les encanta las bodas.", "A mis amigos le encantan las bodas.", "Mis amigos encantan las bodas."], "Bodas is plural."),
        M("What does “más te gusta” mean in the question?", "you like most", ["you like less", "you buy most", "you hate most"], "Más = most."),
        M("How do you ask someone which holiday bothers them most?", "¿Qué día festivo te molesta más?", ["¿Qué día festivo tú molestas más?", "¿Qué día festivo molesta te más?", "¿Qué día festivo te molestan más?"], "Te molesta + subject."),
    ],
    verify=vp("gustar", "gusto", "gustas", "gusta", "gustamos", "gustáis", "gustan"),
)

# ---------------------------------------------------------------------------- 228
L228 = lesson(
    "A difficult flight: irregular preterites in a story",
    "Tuvimos una demora. Las maletas no llegaron.",
    requires=["vuelo", "maleta", "demora", "salir", "tener", "poder", "decir", "dormir", "traer", "llegar"],
    cards=[
        card("Read the story",
             "This story uses many irregular preterites (tuvimos, pudimos, dijo, trajo) together with regular ones. "
             "Try to say each sentence aloud and tell yourself which pattern each verb follows.",
             examples=[
                 ex("Mi amigo Tomás y yo salimos para Quito el sábado.", "My friend Tomás and I left for Quito on Saturday.", "salimos"),
                 ex("Tuvimos una demora de dos horas en el primer vuelo.", "We had a two-hour delay on the first flight.", "Tuvimos"),
                 ex("Llegamos corriendo a la puerta de embarque y pudimos subir al avión.", "We arrived running at the boarding gate and were able to board.", "pudimos"),
                 ex("Nuestras maletas no llegaron.", "Our suitcases did not arrive.", "llegaron"),
                 ex("En el mostrador una empleada nos dijo que las maletas llegarían al día siguiente.", "At the counter an employee told us the suitcases would arrive the next day.", "dijo"),
                 ex("Esa noche dormimos en el hotel sin ropa limpia.", "That night we slept at the hotel without clean clothes.", "dormimos"),
                 ex("A la mañana siguiente, el hotel nos trajo las maletas.", "The next morning, the hotel brought us the suitcases.", "trajo"),
             ]),
        card("Telling a story well",
             "A good anecdote follows the order of events and uses connecting words.",
             tables=[table(["Palabra", "English"],
                           [["primero", "first"],
                            ["después", "afterwards"],
                            ["esa noche", "that night"],
                            ["a la mañana siguiente", "the next morning"],
                            ["por suerte", "luckily"]],
                           say=[0])]),
    ],
    exercises=[
        F("Mi amigo y yo ___ para Quito el sábado.", "salimos", ["salieron", "salí", "salen"], "Nosotros → salimos.", tr="My friend and I left for Quito on Saturday.", lemma="salir:nosotros:pret"),
        F("Nosotros ___ una demora de dos horas.", "tuvimos", ["tuvieron", "tuve", "tenemos"], "Nosotros → tuvimos.", tr="We had a two-hour delay.", lemma="tener:nosotros:pret"),
        F("Por suerte, nosotros ___ subir al avión.", "pudimos", ["pudieron", "pude", "podemos"], "Nosotros → pudimos.", tr="Luckily, we were able to board the plane.", lemma="poder:nosotros:pret"),
        F("Una empleada nos ___ que las maletas llegarían al día siguiente.", "dijo", ["dijeron", "dije", "dice"], "Una empleada → ella: dijo.", tr="An employee told us the suitcases would arrive the next day.", lemma="decir:ella:pret"),
        F("Esa noche nosotros ___ en el hotel.", "dormimos", ["durmieron", "dormí", "duermen"], "Nosotros has no stem change.", tr="That night we slept at the hotel.", lemma="dormir:nosotros:pret"),
        F("A la mañana siguiente, el hotel nos ___ las maletas.", "trajo", ["trajeron", "traje", "trae"], "El hotel → él: trajo.", tr="The next morning, the hotel brought us the suitcases.", lemma="traer:él:pret"),
        M("Where were the friends going?", "to Quito", ["to Lima", "to Madrid", "to Miami"], "Salimos para Quito."),
        M("What did the employee say about the suitcases?", "They would arrive the next day.", ["They arrived at once.", "They were lost forever.", "They were left at home."], "Llegarían al día siguiente."),
        M("What does “por suerte” mean?", "luckily", ["finally", "never", "slowly"], "Suerte = luck."),
    ],
    verify=vpp("salir", "salí", "saliste", "salió", "salimos", "salisteis", "salieron"),
)

# ---------------------------------------------------------------------------- 229
L229 = lesson(
    "At the travel agency: questions and answers",
    "¿Cuándo viaja? ¿De ida o de ida y vuelta?",
    requires=["viajar", "boleto", "ciudad", "fecha", "pagar", "pasaporte", "tarjeta", "identificación", "escala", "directo"],
    cards=[
        card("What the agent asks",
             "A travel agent asks about the date, the type of ticket, the route, the length of the stay, the lodging and "
             "the payment. All the questions use usted.",
             tables=[table(["El agente pregunta", "Usted responde"],
                           [["¿Cuándo viaja usted?", "Viajo el quince de julio."],
                            ["¿Quiere un boleto de ida o de ida y vuelta?", "De ida y vuelta, por favor."],
                            ["¿De qué ciudad sale?", "Salgo de Panamá."],
                            ["¿Prefiere un vuelo directo o con escala?", "Prefiero un vuelo directo."],
                            ["¿Cuántos días va a estar en Bogotá?", "Voy a estar una semana."],
                            ["¿Qué tipo de alojamiento prefiere?", "Prefiero un hotel pequeño."],
                            ["¿Cómo va a pagar?", "Voy a pagar con tarjeta."],
                            ["¿Tiene su pasaporte?", "Sí, aquí lo tiene."]],
                           say=[0, 1])]),
        card("Question words to know",
             "¿Cuándo? asks when; ¿Cuántos días? asks how many days; ¿De qué ciudad? asks which city; ¿Cómo? asks how.",
             examples=[
                 ex("¿Cuántos días va a estar en Bogotá?", "How many days are you going to be in Bogotá?", "Cuántos días"),
                 ex("¿Prefiere un vuelo directo o con escala?", "Do you prefer a direct flight or one with a layover?", "directo"),
                 ex("¿Cómo va a pagar?", "How are you going to pay?", "pagar"),
             ]),
    ],
    exercises=[
        F("¿___ viaja usted? Viajo el quince de julio.", "Cuándo", ["Dónde", "Quién", "Por qué"], "A date answers cuándo.", tr="When are you traveling? I’m traveling on July fifteenth."),
        F("¿Quiere un boleto de ida o de ida y ___?", "vuelta", ["cuenta", "mesa", "hora"], "Ida y vuelta = round trip.", tr="Do you want a one-way or a round-trip ticket?"),
        F("¿Prefiere un vuelo directo o con ___?", "escala", ["maleta", "puerta", "llave"], "Con escala = with a layover.", tr="Do you prefer a direct flight or one with a layover?"),
        F("¿Cuántos ___ va a estar en Bogotá? Una semana.", "días", ["horas", "años", "tarjetas"], "The answer is a week.", tr="How many days are you going to be in Bogotá? One week."),
        F("¿Cómo va a ___? Con tarjeta.", "pagar", ["pago", "paga", "pagando"], "Va a + infinitive.", tr="How are you going to pay? By card."),
        M("Which question asks about the type of lodging?", "¿Qué tipo de alojamiento prefiere?", ["¿Qué tipo de maleta prefiere?", "¿Qué tipo de coche prefiere?", "¿Qué tipo de comida prefiere?"], "Alojamiento = lodging."),
        M("What does “con escala” mean?", "with a layover", ["with a view", "with a discount", "with a guide"], "Escala = layover."),
        M("Which answer fits “¿De qué ciudad sale?”", "Salgo de Panamá.", ["Salgo el quince.", "Salgo con tarjeta.", "Salgo una semana."], "A city answers de qué ciudad."),
        M("Which usted question asks for a passport?", "¿Tiene su pasaporte?", ["¿Tienes tu pasaporte?", "¿Tengo su pasaporte?", "¿Tienen mi pasaporte?"], "Usted → tiene, su."),
    ],
)

# ---------------------------------------------------------------------------- 230
L230 = lesson(
    "Numbers in context",
    "doscientos quince, mil doscientos cincuenta, dos mil veinte",
    requires=["número", "precio", "año", "fecha", "vuelo", "habitación"],
    cards=[
        card("Hundreds, thousands and years",
             "Hundreds agree in gender with the noun (doscientas personas, doscientos dólares). Mil never takes -s and "
             "is not preceded by un: mil dólares, dos mil dólares. Years are read as whole numbers: dos mil veinte; "
             "mil novecientos noventa.",
             tables=[table(["Número", "En letras"],
                           [["215", "doscientos quince"],
                            ["470", "cuatrocientos setenta"],
                            ["715", "setecientos quince"],
                            ["1.250", "mil doscientos cincuenta"],
                            ["1975", "mil novecientos setenta y cinco"],
                            ["2020", "dos mil veinte"],
                            ["5.000", "cinco mil"],
                            ["1.000.000", "un millón"]],
                           say=[1])]),
        card("Numbers in real situations",
             "Flight numbers, room numbers, prices and years all use these patterns. Some countries separate the thousands "
             "with a period (1.250) and others with a comma (1,250); years are never separated.",
             examples=[
                 ex("El vuelo es el número cuatrocientos setenta.", "The flight is number 470.", "cuatrocientos setenta"),
                 ex("La habitación doscientos quince está en el segundo piso.", "Room 215 is on the second floor.", "doscientos quince"),
                 ex("El boleto cuesta mil doscientos cincuenta pesos.", "The ticket costs 1,250 pesos.", "mil doscientos cincuenta"),
                 ex("Nací en mil novecientos noventa.", "I was born in 1990.", "mil novecientos noventa"),
                 ex("Esta ciudad tiene un millón de habitantes.", "This city has a million inhabitants.", "un millón"),
             ]),
    ],
    exercises=[
        F("La habitación número ___ quince está en el segundo piso.", "doscientos", ["doscientas", "ciento", "dos"], "Habitación number 215: doscientos quince.", tr="Room 215 is on the second floor."),
        F("El boleto cuesta ___ doscientos cincuenta pesos.", "mil", ["miles", "un mil", "cien"], "Mil never takes -s and no un.", tr="The ticket costs 1,250 pesos."),
        F("Nací en mil novecientos ___.", "noventa", ["nueve", "novecientos", "nuevo"], "Ninety: noventa.", tr="I was born in 1990."),
        F("El vuelo es el número cuatrocientos ___.", "setenta", ["sesenta", "setecientos", "siete"], "Seventy: setenta.", tr="The flight is number 470."),
        F("Esta ciudad tiene un ___ de habitantes.", "millón", ["mil", "millones", "cien"], "One million: un millón.", tr="This city has a million inhabitants."),
        M("How do you write 715 in words?", "setecientos quince", ["sietecientos quince", "setenta y cinco", "setecientas quince"], "Setecientos is irregular: setecientos."),
        M("How do you write 5,000 in words?", "cinco mil", ["cinco miles", "cincuenta", "quinientos"], "Mil does not take -s."),
        M("How do you write 2020 in words?", "dos mil veinte", ["veinte veinte", "dos mil y veinte", "dos veinte"], "Years are read as whole numbers."),
        M("How do you write 200 people (feminine) in words?", "doscientas personas", ["doscientos personas", "dos cientos personas", "ducientas personas"], "Hundreds agree in gender."),
    ],
)

# ---------------------------------------------------------------------------- 231
L231 = lesson(
    "Unit review: food, celebrations and object pronouns",
    "Los frijoles: déjelos en agua. A mis hijos les encantan los regalos.",
    requires=["cortar", "dejar", "comprar", "pedir", "regalar", "comer", "fruta"],
    cards=[
        card("What to remember",
             "Direct objects take lo, la, los, las (and me, te, nos). Indirect objects take me, te, le, nos, les. When "
             "both appear, the indirect comes first and le or les become se. Commands follow the usted pattern. "
             "Gustar-type verbs agree with the thing liked.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["objeto directo", "Lo compré en el mercado."],
                            ["objeto indirecto", "Le compré un libro."],
                            ["los dos", "Se lo compré ayer."],
                            ["con infinitivo", "Voy a comprárselo."],
                            ["gustar", "A mis hijos les encantan los regalos."]],
                           say=[1])]),
        card("A recipe and a celebration",
             "Combine what you know: instructions use usted commands, and stories about celebrations use the preterite.",
             examples=[
                 ex("Corte la cebolla y fríala con mantequilla.", "Cut the onion and fry it with butter.", "fríala"),
                 ex("Los niños se divirtieron y pidieron más rosca.", "The children had fun and asked for more rosca.", "pidieron"),
                 ex("Mi madre me regaló un libro. Me lo regaló hace un año.", "My mother gave me a book. She gave it to me a year ago.", "Me lo"),
             ]),
    ],
    exercises=[
        F("Señor, ___ la cebolla en cuadritos.", "corte", ["corta", "corto", "corten"], "Usted command of cortar.", tr="Sir, cut the onion into small cubes.", lemma="cortar:usted:cmd"),
        F("Los niños ___ más rosca.", "pidieron", ["pedieron", "piden", "pidió"], "Ellos → pidieron.", tr="The children asked for more rosca.", lemma="pedir:ellos:pret"),
        F("Compré el libro para mi hermana. ___ lo compré ayer.", "Se", ["Le", "Me", "Te"], "Le + lo → se lo.", tr="I bought the book for my sister. I bought it for her yesterday."),
        F("Mi madre me regaló un libro. Me ___ regaló hace un año.", "lo", ["la", "los", "las"], "Libro is masculine singular.", tr="My mother gave me a book. She gave it to me a year ago."),
        F("A mis hijos ___ encantan los regalos.", "les", ["le", "nos", "me"], "A mis hijos → les.", tr="My children love gifts."),
        F("Voy a comprar las frutas. Voy a ___ en el mercado.", "comprarlas", ["comprarlo", "comprarla", "comprarlos"], "Frutas → -las.", tr="I’m going to buy the fruit. I’m going to buy it at the market."),
        F("Llamamos ___ mesero y pedimos la cuenta.", "al", ["a", "el", "del"], "A + el = al.", tr="We called the waiter and asked for the bill."),
        M("What does “Me lo regaló” mean?", "She (he) gave it to me.", ["I gave it to her.", "They gave me to him.", "It was a gift for her."], "Me = to me; lo = it."),
        M("In “Les encantan los regalos”, why is it “encantan”?", "Because “los regalos” is plural", ["Because les is plural", "Because it is past tense", "Because it is a command"], "The verb agrees with the thing liked."),
        M("Which is the usted command of “agregar”?", "agregue", ["agrega", "agrego", "agregen"], "G → gu before e."),
    ],
    verify=vpp("pedir", "pedí", "pediste", "pidió", "pedimos", "pedisteis", "pidieron"),
)

# ---------------------------------------------------------------------------- 232
L232 = lesson(
    "Unit review: travel, lodging and commands",
    "Fuimos, pidió, hace dos años · Siga derecho, no fume",
    requires=["viaje", "hotel", "vuelo", "aeropuerto", "pasaporte"],
    cards=[
        card("What to remember",
             "Travel stories use the preterite: regular endings, special stems (tuve, puse, supe, quise, anduve, "
             "conduje, hice, vine, dije, traje), fui for ser and ir, spelling changes in yo (busqué), the y-change "
             "(cayó, leyó) and stem changes in -ir verbs (pidió, durmieron). Hace + time = ago. Directions and signs use "
             "formal commands.",
             tables=[table(["Tema", "Ejemplo"],
                           [["hace = ago", "Llegué hace una hora."],
                            ["se lo, se la", "Se lo di ayer."],
                            ["otro", "¿Me puede dar otro boleto?"],
                            ["se impersonal", "Se prohíbe fumar."],
                            ["mandato formal", "Siga derecho y doble a la izquierda."],
                            ["mandato negativo", "No estacione aquí."]],
                           say=[1])]),
        card("Putting it together",
             "A traveler asks for directions, and a hotel clerk answers with commands. Both talk about what happened "
             "using the preterite.",
             examples=[
                 ex("Ayer llegué al hotel y pedí una habitación con vista al mar.", "Yesterday I arrived at the hotel and asked for a room with an ocean view.", "pedí"),
                 ex("Hace dos días mis padres me dieron los boletos. Me los dieron en el aeropuerto.", "Two days ago my parents gave me the tickets. They gave them to me at the airport.", "Me los"),
                 ex("Señor, salga del hotel, siga derecho y doble a la derecha.", "Sir, leave the hotel, go straight and turn right.", "salga"),
             ]),
    ],
    exercises=[
        F("El año pasado nosotros ___ a Lima.", "fuimos", ["fueron", "fui", "vamos"], "Nosotros → fuimos.", tr="Last year we went to Lima.", lemma="ir:nosotros:pret"),
        F("El recepcionista me ___ la llave.", "dio", ["di", "dieron", "da"], "Él → dio.", tr="The clerk gave me the key.", lemma="dar:él:pret"),
        F("Llegamos al hotel hace dos ___.", "horas", ["hora", "horario", "hacer"], "Dos → plural: horas.", tr="We arrived at the hotel two hours ago."),
        F("Ayer yo ___ mi pasaporte en la recepción.", "busqué", ["buscó", "busco", "buscaron"], "Yo → busqué.", tr="Yesterday I looked for my passport at the front desk.", lemma="buscar:yo:pret"),
        F("¿Me puede dar ___ llave, por favor?", "otra", ["otro", "otras", "otros"], "Llave is feminine singular.", tr="Can you give me another key, please?"),
        F("Se ___ fumar en el aeropuerto.", "prohíbe", ["prohíben", "prohíbo", "prohíbes"], "Singular infinitive → prohíbe.", tr="Smoking is prohibited in the airport.", lemma="prohibir:él"),
        F("Señor, ___ derecho y doble a la izquierda.", "siga", ["sigue", "sigo", "sigan"], "Usted command of seguir.", tr="Sir, go straight and turn left.", lemma="seguir:usted:cmd"),
        F("Señores, no ___ aquí.", "estacionen", ["estacionan", "estacione", "estacionar"], "Ustedes, negative.", tr="Gentlemen, don’t park here.", lemma="estacionar:ustedes:cmd"),
        F("Mis padres me dieron los boletos. ___ dieron en el aeropuerto.", "Me los", ["Se los", "Me lo", "Los me"], "Me + los, indirect first.", tr="My parents gave me the tickets. They gave them to me at the airport."),
        M("What does “Hace una hora que llegué” mean?", "It has been an hour since I arrived.", ["I arrive in an hour.", "I have been arriving for an hour.", "I arrived an hour early."], "Hace + time + que + preterite."),
        M("Which sign means “No entry”?", "Prohibido el paso", ["Siga derecho", "Conduzca despacio", "Curva ciega"], "Prohibido = forbidden."),
        M("Which is the correct preterite of “ver” for yo?", "vi", ["vio", "veo", "viste"], "Yo → vi, no accent."),
    ],
    verify=vpp("ir", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"),
)
UNIT = unit("Repaso de la unidad", [L222, L223, L224, L225, L226, L227, L228, L229, L230, L231, L232])

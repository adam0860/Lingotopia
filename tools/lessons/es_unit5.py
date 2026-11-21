"""Unit 5: the house (textbook Chapter 4)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 62
L62 = lesson(
    "Parts of the house",
    "la sala, la cocina, el baño, el dormitorio",
    requires=["casa", "sala", "cocina", "baño", "puerta", "ventana"],
    cards=[
        card("Rooms",
             "Learn each room with its article. Most Spanish speakers say la sala for the living room; in some "
             "countries you also hear el salón or el living. The bedroom is el dormitorio, la habitación, el "
             "cuarto, la recámara or la pieza, depending on the country.",
             tables=[table(["Lugar", "English"],
                           [["la casa", "house"],
                            ["el apartamento", "apartment"],
                            ["la sala", "living room"],
                            ["el comedor", "dining room"],
                            ["la cocina", "kitchen"],
                            ["el baño", "bathroom"],
                            ["el dormitorio, la habitación", "bedroom"],
                            ["el garaje", "garage"],
                            ["el jardín", "garden"],
                            ["el patio", "patio, yard"],
                            ["el sótano", "basement"]],
                           say=[0])]),
        card("Parts of a building",
             "Here are the parts that make up the house itself.",
             tables=[table(["Parte", "English"],
                           [["la puerta", "door"],
                            ["la ventana", "window"],
                            ["la pared", "wall"],
                            ["el techo", "roof, ceiling"],
                            ["el piso", "floor (also: apartment in Spain)"],
                            ["la escalera", "stairs"]],
                           say=[0])],
             examples=[
                 ex("Mi casa tiene tres dormitorios y dos baños.", "My house has three bedrooms and two bathrooms.", "tres dormitorios y dos baños"),
                 ex("Cocinamos en la cocina.", "We cook in the kitchen.", "Cocinamos en la cocina."),
                 ex("El coche está en el garaje.", "The car is in the garage.", "en el garaje"),
                 ex("Vivo en un apartamento pequeño.", "I live in a small apartment.", "un apartamento pequeño"),
             ]),
    ],
    exercises=[
        F("Mi cama está en el ___.", "dormitorio", ["comedor", "garaje", "jardín"], "Beds are in the bedroom.", tr="My bed is in the bedroom."),
        F("Cocinamos en la ___.", "cocina", ["sala", "escalera", "pared"], "You cook in the kitchen.", tr="We cook in the kitchen."),
        F("Comemos en el ___.", "comedor", ["baño", "garaje", "sótano"], "The dining room is for meals.", tr="We eat in the dining room."),
        F("El coche está en el ___.", "garaje", ["comedor", "baño", "dormitorio"], "Cars go in the garage.", tr="The car is in the garage."),
        F("Hay flores en el ___.", "jardín", ["baño", "techo", "sótano"], "Flowers grow in the garden.", tr="There are flowers in the garden."),
        F("Mi casa tiene dos ___.", "baños", ["baño", "bañas", "baña"], "Plural of baño: baños.", tr="My house has two bathrooms."),
        M("Which word is feminine?", "la sala", ["el comedor", "el garaje", "el jardín"], "Sala takes la."),
        M("Which word is masculine?", "el techo", ["la pared", "la puerta", "la ventana"], "Techo takes el."),
        M("Which of these is another word for “bedroom”?", "la habitación", ["la escalera", "la cocina", "la ventana"], "Habitación = room, bedroom."),
        M("What is “el sótano”?", "the basement", ["the roof", "the garden", "the stairs"], "Sótano = basement."),
    ],
)

# ---------------------------------------------------------------------------- 63
L63 = lesson(
    "Furniture and appliances",
    "la mesa, el sofá, la nevera, la lavadora",
    requires=["mesa", "silla", "cama", "espejo", "mueble", "casa"],
    cards=[
        card("In the living areas",
             "Furniture is a good place to learn gender, because you can see the object. Notice that some "
             "masculine words end in -a (el sofá) and some feminine words end in -o or -ón.",
             tables=[table(["Mueble", "English"],
                           [["el sofá", "sofa"],
                            ["la mesa", "table"],
                            ["la silla", "chair"],
                            ["la cama", "bed"],
                            ["el escritorio", "desk"],
                            ["el estante", "shelf"],
                            ["el armario", "closet, wardrobe"],
                            ["el espejo", "mirror"],
                            ["la lámpara", "lamp"],
                            ["la alfombra", "rug"],
                            ["la cortina", "curtain"],
                            ["el televisor", "television set"]],
                           say=[0])]),
        card("In the kitchen and laundry",
             "Appliances are electrodomésticos. The fridge has several names: el refrigerador in Mexico, la "
             "nevera in Spain and the Caribbean.",
             tables=[table(["Aparato", "English"],
                           [["el refrigerador, la nevera", "refrigerator"],
                            ["la estufa", "stove"],
                            ["el horno", "oven"],
                            ["el microondas", "microwave"],
                            ["la lavadora", "washing machine"]],
                           say=[0])],
             examples=[
                 ex("Hay una lámpara al lado del sofá.", "There is a lamp next to the sofa.", "una lámpara"),
                 ex("La comida está en el refrigerador.", "The food is in the refrigerator.", "en el refrigerador"),
                 ex("Necesito una mesa y cuatro sillas.", "I need a table and four chairs.", "una mesa y cuatro sillas"),
             ]),
    ],
    exercises=[
        F("La comida está en el ___.", "refrigerador", ["armario", "espejo", "sofá"], "Food is kept cold in the refrigerator.", tr="The food is in the refrigerator."),
        F("Cocino en la ___.", "estufa", ["alfombra", "cortina", "lámpara"], "You cook on the stove.", tr="I cook on the stove."),
        F("Lavo la ropa en la ___.", "lavadora", ["estufa", "mesa", "silla"], "Clothes go in the washing machine.", tr="I wash the clothes in the washing machine."),
        F("Los libros están en el ___.", "estante", ["horno", "espejo", "microondas"], "Books go on a shelf.", tr="The books are on the shelf."),
        F("Hay un ___ grande en el baño.", "espejo", ["horno", "sofá", "refrigerador"], "A mirror hangs in the bathroom.", tr="There is a big mirror in the bathroom."),
        M("Which word is masculine?", "el sofá", ["la silla", "la mesa", "la cama"], "Sofá is masculine even though it ends in -a."),
        M("Which word is feminine?", "la lavadora", ["el horno", "el estante", "el escritorio"], "Lavadora takes la."),
        M("Another word for “refrigerador” is…", "nevera", ["estufa", "horno", "escritorio"], "Nevera is common in Spain and the Caribbean."),
        M("Which appliance heats food quickly?", "el microondas", ["el espejo", "el sofá", "la alfombra"], "Microondas = microwave."),
    ],
)

# ---------------------------------------------------------------------------- 64
L64 = lesson(
    "Where is it? Location words",
    "encima de, debajo de, al lado de, entre",
    requires=["encima", "debajo", "delante", "detrás", "lado", "entre", "cerca"],
    cards=[
        card("Prepositions of place",
             "To say where something is, use estar plus one of these expressions. Most end in de, which "
             "joins them to a noun: encima de la mesa.",
             tables=[table(["Expresión", "English"],
                           [["encima de", "on top of"],
                            ["debajo de", "under"],
                            ["delante de", "in front of"],
                            ["detrás de", "behind"],
                            ["al lado de", "next to"],
                            ["enfrente de", "across from"],
                            ["a la derecha de", "to the right of"],
                            ["a la izquierda de", "to the left of"],
                            ["cerca de", "near"],
                            ["lejos de", "far from"],
                            ["dentro de", "inside"],
                            ["fuera de", "outside of"],
                            ["entre", "between (no de)"]],
                           say=[0])]),
        card("De + el = del",
             "When one of these expressions meets el, de and el merge into del: al lado del sofá. With la, los or "
             "las nothing changes: al lado de la mesa.",
             examples=[
                 ex("El libro está encima de la mesa.", "The book is on the table.", "encima de la mesa"),
                 ex("El gato está debajo de la silla.", "The cat is under the chair.", "debajo de la silla"),
                 ex("La lámpara está al lado del sofá.", "The lamp is next to the sofa.", "al lado del sofá"),
                 ex("El jardín está detrás de la casa.", "The garden is behind the house.", "detrás de la casa"),
                 ex("La mesa está entre el sofá y la ventana.", "The table is between the sofa and the window.", "entre el sofá y la ventana"),
                 ex("El banco está enfrente del hospital.", "The bank is across from the hospital.", "enfrente del hospital"),
             ]),
    ],
    exercises=[
        F("El libro está ___ de la mesa. (on top of)", "encima", ["debajo", "entre", "lejos"], "On the table = encima de la mesa.", tr="The book is on the table."),
        F("El gato está ___ de la silla. (under)", "debajo", ["encima", "entre", "dentro"], "Under the chair = debajo de.", tr="The cat is under the chair."),
        F("El jardín está ___ de la casa.", "detrás", ["encima", "debajo", "entre"], "Behind the house = detrás de.", tr="The garden is behind the house."),
        F("La lámpara está al lado ___ sofá.", "del", ["de el", "al", "de la"], "De + el becomes del.", tr="The lamp is next to the sofa."),
        F("La mesa está ___ el sofá y la ventana.", "entre", ["encima de", "al lado", "detrás de"], "Between two things: entre, with no de.",
          tr="The table is between the sofa and the window."),
        F("El banco está enfrente ___ hospital.", "del", ["de el", "al", "en"], "De + el = del.", tr="The bank is across from the hospital."),
        F("El coche está ___ del garaje. (outside)", "fuera", ["dentro", "entre", "debajo"], "Outside = fuera de.", tr="The car is outside the garage."),
        M("Which means “to the right of”?", "a la derecha de", ["a la izquierda de", "al lado de", "detrás de"], "Derecha = right; izquierda = left."),
        M("Which is correct?", "al lado del sofá", ["al lado de el sofá", "al lado al sofá", "a lado del sofá"], "De + el = del."),
        M("Which is the opposite of “cerca de”?", "lejos de", ["encima de", "al lado de", "dentro de"], "Cerca = near; lejos = far."),
    ],
)

# ---------------------------------------------------------------------------- 65
L65 = lesson(
    "Going places: the verb ir",
    "voy, vas, va, vamos, vais, van",
    requires=["ir", "a", "casa", "escuela", "trabajo"],
    cards=[
        card("Ir is irregular",
             "Ir means “to go”. Its present tense does not follow the usual endings, so learn the six forms by "
             "heart. Notice that every form begins with v.",
             tables=[table(["Persona", "Ir"],
                           [["yo", "voy"],
                            ["tú", "vas"],
                            ["él, ella, usted", "va"],
                            ["nosotros", "vamos"],
                            ["vosotros", "vais"],
                            ["ellos, ellas, ustedes", "van"]],
                           say=[1])]),
        card("Ir + a + place",
             "After ir, the preposition a introduces the destination. To ask where someone is going, use "
             "¿Adónde? (to where).",
             examples=[
                 ex("¿Adónde vas?", "Where are you going?", "¿Adónde vas?"),
                 ex("Voy a la biblioteca.", "I am going to the library.", "Voy a la biblioteca."),
                 ex("Mi madre va a la oficina.", "My mother goes to the office.", "va a la oficina"),
                 ex("Vamos a la escuela por la mañana.", "We go to school in the morning.", "Vamos a la escuela"),
                 ex("Mis tíos van al mercado los sábados.", "My aunt and uncle go to the market on Saturdays.", "van al mercado"),
             ]),
    ],
    exercises=[
        F("Yo ___ a la biblioteca.", "voy", ["vas", "va", "vamos"], "Yo voy.", tr="I go to the library.", lemma="ir:yo"),
        F("¿Adónde ___ tú?", "vas", ["voy", "va", "van"], "Tú vas.", tr="Where are you going?", lemma="ir:tú"),
        F("Mi madre ___ a la oficina.", "va", ["voy", "vas", "van"], "Mi madre is she: va.", tr="My mother goes to the office.", lemma="ir:ella"),
        F("Nosotros ___ a la escuela.", "vamos", ["van", "voy", "va"], "Nosotros vamos.", tr="We go to school.", lemma="ir:nosotros"),
        F("Mis tíos ___ al mercado.", "van", ["va", "vamos", "voy"], "Mis tíos is they: van.", tr="My aunt and uncle go to the market.", lemma="ir:ellos"),
        F("Vosotros ___ al gimnasio.", "vais", ["van", "vamos", "vas"], "Vosotros vais.", tr="You (all) go to the gym.", lemma="ir:vosotros"),
        M("How do you ask “Where are you going?” (informal)", "¿Adónde vas?", ["¿De dónde vas?", "¿Adónde voy?", "¿Cuándo vas?"], "Adónde asks about destination."),
        M("Which preposition follows ir?", "a", ["de", "en", "con"], "Ir a + destination."),
        M("Which is correct?", "Voy a la oficina.", ["Voy en la oficina.", "Voy de la oficina.", "Va a la oficina yo."], "Ir + a + place."),
    ],
    verify=vp("ir", "voy", "vas", "va", "vamos", "vais", "van"),
)

# ---------------------------------------------------------------------------- 66
L66 = lesson(
    "A + el = al",
    "Voy al banco. Vamos a la tienda.",
    requires=["ir", "banco", "hospital", "tienda", "mercado"],
    cards=[
        card("Two words that merge",
             "A and el are never written apart: they merge into al. This happens before any masculine singular noun "
             "(al banco, al profesor), except in names that include El, such as El Salvador. With la, los and las, "
             "nothing changes.",
             tables=[table(["Lugar", "Voy…"],
                           [["el banco", "Voy al banco."],
                            ["la tienda", "Voy a la tienda."],
                            ["los Estados Unidos", "Voy a los Estados Unidos."],
                            ["las oficinas", "Voy a las oficinas."]],
                           say=[1],
                           note="Al is only for a + el. Never write a el.")]),
        card("Questions and answers",
             "Adónde asks where to; De dónde asks where from. Use them with ir and ser.",
             examples=[
                 ex("¿Adónde van ustedes?", "Where are you (all) going?", "¿Adónde van ustedes?"),
                 ex("Vamos al hospital.", "We are going to the hospital.", "al hospital"),
                 ex("¿De dónde eres?", "Where are you from?", "¿De dónde eres?"),
                 ex("Los sábados voy al gimnasio.", "On Saturdays I go to the gym.", "voy al gimnasio"),
             ]),
    ],
    exercises=[
        F("Voy ___ banco.", "al", ["a el", "a la", "del"], "A + el = al.", tr="I go to the bank."),
        F("Voy ___ tienda.", "a la", ["al", "a el", "de la"], "Tienda is feminine: a la.", tr="I go to the store."),
        F("Mi padre va ___ hospital.", "al", ["a la", "a el", "del"], "Hospital is masculine: al.", tr="My father goes to the hospital."),
        F("Los sábados vamos ___ mercado.", "al", ["a la", "a los", "del"], "Mercado is masculine: al.", tr="On Saturdays we go to the market."),
        F("Mis hijos van ___ escuela.", "a la", ["al", "a el", "del"], "Escuela is feminine: a la.", tr="My children go to school."),
        F("Voy ___ gimnasio por la mañana.", "al", ["a la", "a el", "de"], "Gimnasio is masculine.", tr="I go to the gym in the morning."),
        M("Which is NEVER correct?", "a el banco", ["al banco", "a la tienda", "a los bancos"], "A + el must merge: al."),
        M("Which combination merges?", "a + el", ["a + la", "a + los", "a + las"], "Only a + el becomes al."),
        M("How do you ask “Where are you (all) going?”", "¿Adónde van ustedes?", ["¿De dónde van ustedes?", "¿Quién van ustedes?", "¿Cuándo van ustedes?"], "Adónde = to where."),
        M("How do you ask “Where are you from?” (informal)", "¿De dónde eres?", ["¿Adónde eres?", "¿Dónde vas?", "¿Cómo eres de?"], "De dónde = from where."),
    ],
)

# ---------------------------------------------------------------------------- 67
L67 = lesson(
    "What are you going to do? Ir a + infinitive",
    "Voy a estudiar. Vamos a cenar.",
    requires=["ir", "estudiar", "comer", "mañana", "semana"],
    cards=[
        card("Talking about the future",
             "The easy way to talk about the near future is ir a + infinitive. Conjugate ir for the subject, "
             "add a, and leave the second verb in the infinitive.",
             tables=[table(["Persona", "Ir a + infinitivo"],
                           [["yo", "voy a estudiar"],
                            ["tú", "vas a estudiar"],
                            ["él, ella, usted", "va a estudiar"],
                            ["nosotros", "vamos a estudiar"],
                            ["vosotros", "vais a estudiar"],
                            ["ellos, ellas, ustedes", "van a estudiar"]],
                           say=[1])],
             examples=[
                 ex("Mañana voy a trabajar en casa.", "Tomorrow I am going to work at home.", "voy a trabajar"),
                 ex("¿Qué vas a hacer esta noche?", "What are you going to do tonight?", "¿Qué vas a hacer esta noche?"),
                 ex("Mis padres van a vender la casa.", "My parents are going to sell the house.", "van a vender"),
             ]),
        card("Time words for plans",
             "These words go well with the future: mañana (tomorrow), esta noche (tonight), esta semana, el "
             "sábado, después (afterward), luego (then). Vamos a + infinitive also means “let’s…”.",
             examples=[
                 ex("Esta noche vamos a cenar en un restaurante.", "Tonight we are going to have dinner at a restaurant.", "vamos a cenar"),
                 ex("Después voy a lavar la ropa.", "Afterward I am going to wash the clothes.", "voy a lavar"),
                 ex("¡Vamos a comer!", "Let’s eat!", "¡Vamos a comer!"),
             ]),
    ],
    exercises=[
        F("Mañana yo voy ___ trabajar en casa.", "a", ["de", "en", "que"], "Ir a + infinitive.", tr="Tomorrow I am going to work at home."),
        F("Mis padres van a ___ la casa.", "vender", ["vendo", "vende", "venden"], "After ir a, use the infinitive.", tr="My parents are going to sell the house."),
        F("Esta noche nosotros ___ a cenar.", "vamos", ["voy", "van", "va"], "Nosotros vamos.", tr="Tonight we are going to have dinner.", lemma="ir:nosotros"),
        F("¿Qué ___ a hacer tú esta noche?", "vas", ["voy", "va", "van"], "Tú vas.", tr="What are you going to do tonight?", lemma="ir:tú"),
        F("Mi hermana ___ a estudiar mañana.", "va", ["voy", "vas", "van"], "Mi hermana is she: va.", tr="My sister is going to study tomorrow.", lemma="ir:ella"),
        F("Después voy a ___ la ropa.", "lavar", ["lavo", "lava", "lavamos"], "Infinitive after ir a.", tr="Afterward I am going to wash the clothes."),
        M("How do you say “I am going to read”?", "Voy a leer.", ["Voy leer.", "Voy a leo.", "Vas a leer."], "Voy + a + infinitive."),
        M("How do you say “We are going to eat”?", "Vamos a comer.", ["Vamos comemos.", "Vamos a comemos.", "Van a comer."], "Vamos + a + comer."),
        M("What does “¡Vamos a comer!” also mean?", "Let’s eat.", ["I am eating.", "They eat.", "Do not eat."], "Vamos a + infinitive can mean let’s."),
        M("Which sentence is about the future?", "Mañana voy a estudiar.", ["Estudio todos los días.", "Estudio ahora y siempre.", "Estudio ahora."], "Ir a + infinitive points to the future."),
    ],
)

# ---------------------------------------------------------------------------- 68
L68 = lesson(
    "Household chores",
    "lavar la ropa, limpiar, sacar la basura",
    requires=["lavar", "limpiar", "cocinar", "ropa", "basura", "casa"],
    cards=[
        card("Los quehaceres domésticos",
             "Chores are quehaceres domésticos (or tareas domésticas). Almost all of the verbs are regular, so you can "
             "conjugate them at once.",
             tables=[table(["Quehacer", "English"],
                           [["lavar la ropa", "to wash the clothes"],
                            ["planchar la ropa", "to iron the clothes"],
                            ["lavar los platos", "to wash the dishes"],
                            ["limpiar la casa", "to clean the house"],
                            ["cocinar", "to cook"],
                            ["preparar la cena", "to make dinner"],
                            ["barrer el piso", "to sweep the floor"],
                            ["sacar la basura", "to take out the trash"],
                            ["cortar el césped", "to mow the lawn"],
                            ["pasar la aspiradora", "to vacuum"],
                            ["hacer la cama", "to make the bed"]],
                           say=[0])]),
        card("Who does what",
             "Combine the chores with the verbs and time words you know. Remember that hacer is irregular in "
             "the yo form (hago la cama), and that ir a lets you plan chores.",
             examples=[
                 ex("Los sábados limpio la casa.", "On Saturdays I clean the house.", "limpio la casa"),
                 ex("Mi madre cocina y yo lavo los platos.", "My mother cooks and I wash the dishes.", "yo lavo los platos"),
                 ex("Hago la cama todos los días.", "I make the bed every day.", "Hago la cama"),
                 ex("Después vamos a sacar la basura.", "Afterward we are going to take out the trash.", "sacar la basura"),
                 ex("Mi padre corta el césped los domingos.", "My father mows the lawn on Sundays.", "corta el césped"),
             ]),
    ],
    exercises=[
        F("Yo ___ la ropa en la lavadora.", "lavo", ["lavas", "lava", "lavamos"], "Yo lavo.", tr="I wash the clothes in the washing machine.", lemma="lavar:yo"),
        F("Mi madre ___ la cena.", "prepara", ["preparo", "preparas", "preparan"], "Mi madre is she: prepara.", tr="My mother prepares dinner.", lemma="preparar:ella"),
        F("Nosotros ___ la casa los sábados.", "limpiamos", ["limpio", "limpian", "limpia"], "Nosotros limpiamos.", tr="We clean the house on Saturdays.", lemma="limpiar:nosotros"),
        F("Mi padre ___ el césped los domingos.", "corta", ["corto", "cortas", "cortan"], "Mi padre is he: corta.", tr="My father mows the lawn on Sundays.", lemma="cortar:él"),
        F("Yo ___ la cama todos los días.", "hago", ["hace", "haces", "hacemos"], "Hacer is irregular in the yo form.", tr="I make the bed every day.", lemma="hacer:yo"),
        F("Voy a sacar la ___.", "basura", ["cama", "ropa", "cena"], "You take out the trash.", tr="I am going to take out the trash."),
        F("Mañana vamos a ___ el piso.", "barrer", ["barremos", "barro", "barre"], "Infinitive after vamos a.", tr="Tomorrow we are going to sweep the floor."),
        M("Which chore uses a lavadora?", "lavar la ropa", ["cortar el césped", "barrer el piso", "sacar la basura"], "La lavadora washes clothes."),
        M("Which chore do you do outside, with grass?", "cortar el césped", ["lavar los platos", "planchar la ropa", "hacer la cama"], "Césped = lawn."),
        M("How do you say “I iron the clothes”?", "Plancho la ropa.", ["Planchas la ropa.", "Plancha la ropa.", "Planchan la ropa."], "Yo plancho."),
    ],
    verify=vp("lavar", "lavo", "lavas", "lava", "lavamos", "laváis", "lavan")
           + vp("limpiar", "limpio", "limpias", "limpia", "limpiamos", "limpiáis", "limpian")
           + vp("cortar", "corto", "cortas", "corta", "cortamos", "cortáis", "cortan"),
)

# ---------------------------------------------------------------------------- 69
L69 = lesson(
    "I have to: tener que",
    "Tengo que estudiar. Tienes que ayudar.",
    requires=["tener", "que", "ayudar", "limpiar", "trabajar"],
    cards=[
        card("Tener que + infinitive",
             "Tener que + infinitive says that a particular person must do something. Conjugate tener for the "
             "subject, keep que, and use the infinitive after it.",
             tables=[table(["Persona", "Tener que + infinitivo"],
                           [["yo", "tengo que limpiar"],
                            ["tú", "tienes que limpiar"],
                            ["él, ella, usted", "tiene que limpiar"],
                            ["nosotros", "tenemos que limpiar"],
                            ["vosotros", "tenéis que limpiar"],
                            ["ellos, ellas, ustedes", "tienen que limpiar"]],
                           say=[1])]),
        card("Tener que or hay que?",
             "Tener que is personal: it names who has to do it. Hay que is impersonal: it is a general rule "
             "for everyone.",
             tables=[table(["Hay que (everyone)", "Tener que (a person)"],
                           [["Hay que llegar temprano.", "Tengo que llegar temprano."],
                            ["Hay que estudiar.", "Mi hermana tiene que estudiar."],
                            ["Hay que limpiar la casa.", "Tenemos que limpiar la casa."]],
                           say=[0, 1])],
             examples=[
                 ex("Este fin de semana tengo que estudiar para un examen.", "This weekend I have to study for an exam.", "tengo que estudiar"),
                 ex("Mis hijos tienen que ayudar en casa.", "My children have to help at home.", "tienen que ayudar"),
             ]),
    ],
    exercises=[
        F("Yo tengo ___ limpiar la casa.", "que", ["de", "a", "por"], "The fixed expression is tener que.", tr="I have to clean the house."),
        F("Mi hermana ___ que estudiar.", "tiene", ["tengo", "tienes", "tienen"], "Mi hermana is she: tiene.", tr="My sister has to study.", lemma="tener:ella"),
        F("Nosotros ___ que ayudar en casa.", "tenemos", ["tienen", "tengo", "tiene"], "Nosotros tenemos.", tr="We have to help at home.", lemma="tener:nosotros"),
        F("¿Tú ___ que trabajar mañana?", "tienes", ["tengo", "tiene", "tienen"], "Tú tienes.", tr="Do you have to work tomorrow?", lemma="tener:tú"),
        F("Mis hijos tienen que ___ los platos.", "lavar", ["lavan", "lavo", "lava"], "Infinitive after tener que.", tr="My children have to wash the dishes."),
        F("Tengo que ___ temprano.", "llegar", ["llego", "llega", "llegas"], "Infinitive after tener que.", tr="I have to arrive early."),
        M("Which sentence is general (for everyone)?", "Hay que llegar temprano.", ["Tengo que llegar temprano.", "Tienes que llegar temprano.", "Tenemos que llegar temprano."],
          "Hay que has no specific subject."),
        M("Which sentence says that Marta must clean?", "Marta tiene que limpiar.", ["Hay que Marta limpiar.", "Marta tengo que limpiar.", "Marta tiene limpiar."],
          "Tener que is personal."),
        M("Which is correct?", "Ellos tienen que estudiar.", ["Ellos tiene que estudiar.", "Ellos tienen estudiar que.", "Ellos tienen que estudian."],
          "Ellos tienen que + infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 70
L70 = lesson(
    "Comparing: más que, menos que",
    "Mi casa es más grande que tu casa.",
    requires=["más", "menos", "grande", "pequeño", "mejor", "peor"],
    cards=[
        card("More than, less than, as…as",
             "To compare two things, put más (more) or menos (less) before the adjective and que (than) "
             "after it. For equality, use tan + adjective + como.",
             tables=[table(["Pattern", "Example"],
                           [["más + adj. + que", "Mi casa es más grande que tu casa."],
                            ["menos + adj. + que", "El apartamento es menos caro que la casa."],
                            ["tan + adj. + como", "La sala es tan grande como la cocina."],
                            ["más de + number", "Hay más de veinte libros."],
                            ["menos de + number", "Hay menos de diez sillas."]],
                           say=[1],
                           note="Before a number, Spanish uses de, not que.")]),
        card("Better, worse, older, younger",
             "A few comparisons are irregular and do not take más: mejor (better), peor (worse), mayor (older) "
             "and menor (younger). They are the same for masculine and feminine.",
             examples=[
                 ex("Esta casa es mejor que aquella.", "This house is better than that one.", "mejor que"),
                 ex("Mi sala es peor que tu sala.", "My living room is worse than your living room.", "peor que"),
                 ex("Mi hermano es mayor que yo.", "My brother is older than I am.", "mayor que"),
                 ex("Mi prima es menor que mi hermana.", "My cousin is younger than my sister.", "menor que"),
             ]),
    ],
    exercises=[
        F("Mi casa es más grande ___ tu casa.", "que", ["de", "como", "a"], "Más… que.", tr="My house is bigger than your house."),
        F("El apartamento es menos caro ___ la casa.", "que", ["de", "como", "a"], "Menos… que.", tr="The apartment is less expensive than the house."),
        F("La sala es tan grande ___ la cocina.", "como", ["que", "de", "a"], "Tan… como.", tr="The living room is as big as the kitchen."),
        F("Hay más ___ veinte libros.", "de", ["que", "como", "a"], "Before a number: de.", tr="There are more than twenty books."),
        F("Esta casa es ___ que aquella.", "mejor", ["más bueno", "más mejor", "bueno"], "Mejor is irregular: no más.", tr="This house is better than that one."),
        F("Mi hermano es ___ que yo.", "mayor", ["más mayor", "más viejo que", "grande"], "Mayor = older.", tr="My brother is older than I am."),
        M("How do you say “more than”?", "más que", ["más como", "más de que", "mucho que"], "Más… que."),
        M("How do you say “as big as”?", "tan grande como", ["tan grande que", "más grande como", "tanto grande como"], "Tan + adjective + como."),
        M("Which is correct?", "Hay menos de diez sillas.", ["Hay menos que diez sillas.", "Hay menos como diez sillas.", "Hay menos diez sillas."], "De before a number."),
        M("What is the comparative of “bueno”?", "mejor", ["más bueno", "buenor", "más mejor"], "Mejor is irregular."),
    ],
)

# ---------------------------------------------------------------------------- 71
L71 = lesson(
    "More about de",
    "una mesa de madera, una casa de dos pisos",
    requires=["de", "madera", "metal", "papel", "casa", "mesa"],
    cards=[
        card("What it is made of",
             "De tells what something is made of, with no article. Many nouns are made of a material.",
             tables=[table(["Material", "Example"],
                           [["de madera", "una mesa de madera"],
                            ["de metal", "una silla de metal"],
                            ["de plástico", "un vaso de plástico"],
                            ["de vidrio", "una ventana de vidrio"],
                            ["de papel", "una bolsa de papel"]],
                           say=[1])]),
        card("De for type, contents and features",
             "De also joins a noun to another noun that describes its kind, purpose or number of parts. You "
             "already know de for owner (la casa de Ana), origin (soy de Cuba) and clock time (las ocho de la "
             "mañana).",
             examples=[
                 ex("Es una casa de dos pisos.", "It is a two-story house.", "una casa de dos pisos"),
                 ex("Necesito una mesa de cocina.", "I need a kitchen table.", "mesa de cocina"),
                 ex("Mi mesa es de madera.", "My table is made of wood.", "es de madera"),
                 ex("Este es el dormitorio de mi hija.", "This is my daughter’s bedroom.", "de mi hija"),
                 ex("Una casa de campo está lejos de la ciudad.", "A country house is far from the city.", "casa de campo"),
             ]),
    ],
    exercises=[
        F("Mi mesa es ___ madera.", "de", ["en", "con", "para"], "Material: de.", tr="My table is made of wood."),
        F("Las páginas del libro son de ___.", "papel", ["metal", "vidrio", "madera"], "Book pages are paper.", tr="The pages of the book are made of paper."),
        F("Es una casa de dos ___.", "pisos", ["piso", "pisa", "pisas"], "Plural pisos.", tr="It is a two-story house."),
        F("Necesito una mesa de ___.", "cocina", ["cocinar", "cocino", "cocinan"], "Mesa de cocina = kitchen table.", tr="I need a kitchen table."),
        F("Este es el dormitorio ___ mi hija.", "de", ["en", "con", "a"], "Possession: de.", tr="This is my daughter’s bedroom."),
        M("Which sentence says what the chair is made of?", "La silla es de metal.", ["La silla está en metal.", "La silla es con metal.", "La silla tiene metal de."], "Ser de + material."),
        M("Does Spanish use an article in “de madera”?", "No, none.", ["Yes, always el.", "Yes, always la.", "Only with plurals."], "Mesa de madera, with no article."),
        M("What does “una bolsa de papel” mean?", "a paper bag", ["a bag of books", "a paper store", "a big bag"], "De papel = made of paper."),
        M("Which is correct?", "una puerta de madera", ["una puerta madera", "una puerta en madera", "una puerta de la madera"], "Puerta + de + material."),
    ],
)

# ---------------------------------------------------------------------------- 72
L72 = lesson(
    "Problems at home",
    "La puerta está rota. No funciona la calefacción.",
    requires=["roto", "sucio", "limpio", "funcionar", "reparar", "pintar"],
    cards=[
        card("Saying what is wrong",
             "Use estar with roto (broken), sucio (dirty) and limpio (clean): they describe a condition. "
             "They agree with the noun like any adjective. To say that something does not work, use "
             "no funciona; for several things, no funcionan.",
             tables=[table(["Problema", "English"],
                           [["La puerta está rota.", "The door is broken."],
                            ["Las ventanas están rotas.", "The windows are broken."],
                            ["La alfombra está sucia.", "The rug is dirty."],
                            ["La calefacción no funciona.", "The heating does not work."],
                            ["Hay una gotera en el techo.", "There is a leak in the ceiling."],
                            ["No hay agua caliente.", "There is no hot water."],
                            ["Las paredes necesitan pintura.", "The walls need paint."]],
                           say=[0])]),
        card("Who fixes it?",
             "Name the right worker and say what you have to do or are going to do.",
             tables=[table(["Problema", "Quién"],
                           [["una gotera", "el plomero"],
                            ["la luz", "el electricista"],
                            ["una puerta rota", "el carpintero"],
                            ["las paredes", "el pintor"]],
                           say=[0, 1])],
             examples=[
                 ex("Tengo que llamar a un plomero.", "I have to call a plumber.", "llamar a un plomero"),
                 ex("Voy a pintar las paredes.", "I am going to paint the walls.", "pintar las paredes"),
                 ex("Necesitamos reparar el techo.", "We need to repair the roof.", "reparar el techo"),
                 ex("Hay que limpiar la alfombra.", "The rug has to be cleaned.", "limpiar la alfombra"),
             ]),
    ],
    exercises=[
        F("La puerta está ___.", "rota", ["roto", "rotas", "rotos"], "Puerta is feminine singular.", tr="The door is broken."),
        F("Las ventanas están ___.", "rotas", ["rota", "roto", "rotos"], "Ventanas is feminine plural.", tr="The windows are broken."),
        F("La alfombra está ___.", "sucia", ["sucio", "sucias", "sucios"], "Alfombra is feminine singular.", tr="The rug is dirty."),
        F("La calefacción no ___.", "funciona", ["funcionan", "funciono", "funcionas"], "One thing: funciona.", tr="The heating does not work.", lemma="funcionar:ella"),
        F("Tengo que ___ a un plomero.", "llamar", ["llamo", "llama", "llamas"], "Infinitive after tener que.", tr="I have to call a plumber."),
        F("Voy a ___ las paredes.", "pintar", ["pinto", "pinta", "pintan"], "Infinitive after ir a.", tr="I am going to paint the walls."),
        M("A leak in the ceiling: who do you call?", "el plomero", ["el pintor", "el cocinero", "el abogado"], "A plumber fixes leaks."),
        M("The light does not work: who do you call?", "el electricista", ["el plomero", "el médico", "el escritor"], "An electrician."),
        M("Which is correct?", "Los baños están sucios.", ["Los baños están sucio.", "Los baños están sucia.", "Los baños está sucios."], "Estar + masculine plural adjective."),
        M("How do you say “There is no hot water”?", "No hay agua caliente.", ["No tiene agua caliente.", "No es agua caliente.", "No está agua caliente."], "No hay + noun."),
    ],
)

# ---------------------------------------------------------------------------- 73
L73 = lesson(
    "Renting and buying",
    "Se alquila apartamento. Se vende casa.",
    requires=["alquilar", "vender", "precio", "zona", "centro", "casa"],
    cards=[
        card("Reading housing ads",
             "Like job ads, housing ads use se plus a verb: se alquila (for rent) and se vende (for sale). "
             "The verb agrees with the thing: se alquilan apartamentos, se venden casas.",
             tables=[table(["Palabra", "English"],
                           [["se alquila", "for rent"],
                            ["se vende", "for sale"],
                            ["amueblado", "furnished"],
                            ["el dormitorio", "bedroom"],
                            ["el baño", "bathroom"],
                            ["el garaje", "garage"],
                            ["cerca del centro", "near downtown"],
                            ["el precio", "price"],
                            ["al mes", "per month"]],
                           say=[0])],
             examples=[
                 ex("Se alquila apartamento amueblado. Dos dormitorios y un baño.", "Furnished apartment for rent. Two bedrooms and one bathroom.", "Se alquila apartamento"),
                 ex("Se vende casa con jardín y garaje. Tres dormitorios.", "House for sale with garden and garage. Three bedrooms.", "Se vende casa"),
                 ex("Precio: ochocientos dólares al mes.", "Price: eight hundred dollars a month.", "ochocientos dólares al mes"),
             ]),
        card("Questions to ask",
             "When you call about a place, these questions help.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Cuántos dormitorios tiene?", "Tiene tres dormitorios."],
                            ["¿Cuántos baños tiene?", "Tiene dos baños."],
                            ["¿Está cerca del centro?", "Sí, está cerca del centro."],
                            ["¿Cuánto cuesta?", "Cuesta mil dólares al mes."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Se ___ apartamento amueblado.", "alquila", ["alquilan", "alquilo", "alquilas"], "One apartment: alquila.", tr="Furnished apartment for rent."),
        F("Se ___ casa con jardín.", "vende", ["venden", "vendo", "vendes"], "One house: vende.", tr="House with garden for sale."),
        F("Se ___ apartamentos nuevos.", "venden", ["vende", "vendo", "vendemos"], "Plural apartments: venden.", tr="New apartments for sale.", lemma="vender:ellos"),
        F("¿Cuántos dormitorios ___ la casa?", "tiene", ["tienes", "tengo", "tienen"], "La casa is singular: tiene.", tr="How many bedrooms does it have?", lemma="tener:él"),
        F("El precio es de ochocientos dólares ___ mes.", "al", ["en", "del", "de"], "Al mes = per month.", tr="The price is eight hundred dollars a month."),
        M("“Se alquila” means…", "for rent", ["for sale", "sold", "wanted"], "Alquilar = to rent."),
        M("“Se vende” means…", "for sale", ["for rent", "rented", "wanted"], "Vender = to sell."),
        M("“Amueblado” means…", "furnished", ["empty", "new", "cheap"], "Mueble = furniture."),
        M("Which question asks about the price?", "¿Cuánto cuesta?", ["¿Cuántos dormitorios tiene?", "¿Dónde está?", "¿Quién vive allí?"], "Cuánto cuesta = how much does it cost."),
        M("An ad says “Precio: mil doscientos dólares al mes.” How much is the rent?", "1,200 dollars a month", ["1,200 dollars a year", "200 dollars a month", "12,000 dollars a month"], "Mil doscientos = 1.200."),
    ],
)

# ---------------------------------------------------------------------------- 74
L74 = lesson(
    "Chapter 4 review",
    "the house, ir, tener que, comparing, problems",
    requires=["casa", "ir", "limpiar", "alquilar", "más", "mesa"],
    cards=[
        card("What you can do now",
             "You can name rooms and furniture, say where things are, talk about where you are going and what you "
             "are going to do, say what you have to do, compare, and read housing ads.",
             tables=[table(["Skill", "Model sentence"],
                           [["Location", "La lámpara está al lado del sofá."],
                            ["Ir", "Voy al mercado los sábados."],
                            ["Plans", "Mañana voy a limpiar la casa."],
                            ["Obligation", "Mi hermana tiene que lavar los platos."],
                            ["Comparing", "Mi casa es más grande que tu casa."],
                            ["Housing", "Se alquila apartamento amueblado."]],
                           say=[1])]),
    ],
    exercises=[
        F("El gato está ___ de la silla. (under)", "debajo", ["encima", "entre", "dentro"], "Under the chair.", tr="The cat is under the chair."),
        F("Mi padre va ___ banco.", "al", ["a el", "a la", "del"], "A + el = al.", tr="My father goes to the bank."),
        F("Nosotros ___ al gimnasio.", "vamos", ["van", "voy", "va"], "Nosotros vamos.", tr="We go to the gym.", lemma="ir:nosotros"),
        F("Mañana voy a ___ la ropa.", "lavar", ["lavo", "lava", "lavamos"], "Infinitive after ir a.", tr="Tomorrow I am going to wash the clothes."),
        F("Mi hermana ___ que lavar los platos.", "tiene", ["tienes", "tengo", "tienen"], "Mi hermana is she: tiene.", tr="My sister has to wash the dishes.", lemma="tener:ella"),
        F("Mi casa es más grande ___ tu casa.", "que", ["de", "como", "a"], "Más… que.", tr="My house is bigger than your house."),
        F("Hay más ___ veinte libros.", "de", ["que", "como", "a"], "Before a number: de.", tr="There are more than twenty books."),
        F("La mesa es ___ madera.", "de", ["en", "con", "por"], "Material: de.", tr="The table is made of wood."),
        F("Las ventanas están ___.", "rotas", ["rota", "roto", "rotos"], "Feminine plural.", tr="The windows are broken."),
        F("Se ___ apartamento amueblado.", "alquila", ["alquilan", "alquilo", "alquilas"], "One apartment: alquila.", tr="Furnished apartment for rent."),
        M("Which is a general rule for everyone?", "Hay que limpiar la casa.", ["Tengo que limpiar la casa.", "Mi madre limpia la casa.", "Vamos a limpiar la casa."], "Only hay que is impersonal."),
        M("Which is the standard comparative of “bueno”?", "mejor", ["más mejor", "buenor", "buenísimo"], "Mejor is irregular."),
    ],
)

UNIT = unit("La casa", [L62, L63, L64, L65, L66, L67, L68, L69, L70, L71, L72, L73, L74])

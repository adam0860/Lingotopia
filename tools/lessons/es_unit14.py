"""Unit 14: lodging, more preterites, formal commands, directions (textbook Chapter 14)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 201
L201 = lesson(
    "Where to stay",
    "un hotel de lujo, una pensión, una habitación doble",
    requires=["hotel", "habitación", "noche", "estrella", "centro", "turístico", "lujo", "doble", "individual", "mar"],
    cards=[
        card("Places to stay",
             "El alojamiento (also el hospedaje) is the general word for lodging. The verbs alojarse and hospedarse "
             "both mean to stay somewhere. In many Spanish-speaking families, a vacation means visiting relatives and "
             "staying at their house, so the family often hosts people for weeks.",
             tables=[table(["Palabra", "English"],
                           [["el hotel de lujo", "luxury hotel"],
                            ["el centro turístico", "resort"],
                            ["la pensión", "guesthouse, small inn"],
                            ["la casa de huéspedes", "boarding house"],
                            ["la habitación sencilla · la habitación individual", "single room"],
                            ["la habitación doble", "double room"],
                            ["la vista al mar", "ocean view"],
                            ["el servicio de habitación", "room service"]],
                           say=[0])]),
        card("Making a reservation",
             "A reservation conversation is short: say how many nights, what kind of room and how many people. You "
             "can also ask whether breakfast is included.",
             tables=[table(["El cliente", "La recepcionista"],
                           [["Quiero reservar una habitación doble.", "¿Para cuántas noches?"],
                            ["Para tres noches, por favor.", "¿Prefiere vista al mar?"],
                            ["Sí, con vista al mar. ¿Cuánto cuesta por noche?", "Cuesta cien dólares."],
                            ["¿Está incluido el desayuno?", "Sí, está incluido."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Quiero reservar una habitación ___ para dos personas.", "doble", ["sencilla", "individual", "única"], "Two people → doble.", tr="I want to reserve a double room for two people."),
        F("Para una persona necesito una habitación ___.", "sencilla", ["doble", "dobles", "doblada"], "One person → sencilla.", tr="For one person I need a single room."),
        F("Mi familia se ___ en un hotel de lujo.", "hospeda", ["hospedan", "hospedo", "hospedas"], "Mi familia → ella: hospeda.", tr="My family is staying in a luxury hotel.", lemma="hospedar:ella"),
        F("Nosotros nos ___ en una pensión pequeña.", "alojamos", ["alojan", "alojo", "alojas"], "Nosotros → alojamos.", tr="We are staying in a small guesthouse.", lemma="alojar:nosotros"),
        F("¿Está incluido el ___ en el precio?", "desayuno", ["tren", "pasaporte", "avión"], "A hotel may include breakfast.", tr="Is breakfast included in the price?"),
        M("What is “una pensión”?", "a guesthouse or small inn", ["a retirement fund", "a luxury resort", "an airport hotel"], "Pensión = small inn."),
        M("What does “con vista al mar” mean?", "with an ocean view", ["with a sea breeze", "near a fish market", "with a swimming pool"], "Vista = view; mar = sea."),
        M("Which verbs both mean “to stay (in a hotel)”?", "alojarse and hospedarse", ["alojarse and ayudarse", "hospedarse and hablarse", "reservar and cobrar"], "Alojarse = hospedarse."),
        M("What does “¿Cuánto cuesta por noche?” ask?", "the price per night", ["the number of nights", "the room number", "the check-out time"], "Por noche = per night."),
    ],
    verify=vp("hospedar", "hospedo", "hospedas", "hospeda", "hospedamos", "hospedáis", "hospedan")
           + vp("alojar", "alojo", "alojas", "aloja", "alojamos", "alojáis", "alojan"),
)

# ---------------------------------------------------------------------------- 202
L202 = lesson(
    "At the front desk: floors and keys",
    "¿En qué piso está mi habitación? En el tercer piso.",
    requires=["piso", "llave", "ascensor", "recepción", "habitación", "huésped", "reserva"],
    cards=[
        card("Hotel words",
             "The ground floor is la planta baja; above it come el primer piso, el segundo piso and so on. The guest is "
             "el huésped, and the front desk clerk is el recepcionista or la recepcionista. The key is la llave and "
             "the elevator is el ascensor.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["Buenas tardes. Tengo una reserva.", "¿A qué nombre, por favor?"],
                            ["¿En qué piso está mi habitación?", "Está en el tercer piso."],
                            ["¿Dónde está el ascensor?", "Está a la derecha, junto a la recepción."],
                            ["¿Me puede dar otra llave?", "Sí, con mucho gusto."]],
                           say=[0, 1])]),
        card("Ordinals for floors",
             "You already know the ordinals. Remember that primero and tercero shorten to primer and tercer before a "
             "masculine singular noun: el primer piso, el tercer piso. Without the noun they stay long: Mi "
             "habitación está en el tercero.",
             examples=[
                 ex("Mi habitación está en el primer piso.", "My room is on the first floor.", "primer"),
                 ex("La oficina queda en el segundo piso.", "The office is on the second floor.", "segundo"),
                 ex("Su habitación está en el tercer piso.", "Your room is on the third floor.", "tercer"),
                 ex("Su oficina está en el tercero.", "His office is on the third.", "tercero"),
                 ex("El ascensor sube al quinto piso.", "The elevator goes up to the fifth floor.", "quinto"),
             ]),
    ],
    exercises=[
        F("Mi habitación está en el ___ piso.", "tercer", ["tercero", "tercera", "tres"], "Tercero shortens to tercer before piso.", tr="My room is on the third floor."),
        F("La oficina queda en el ___ piso.", "primer", ["primero", "primera", "uno"], "Primero shortens to primer.", tr="The office is on the first floor."),
        F("El ___ sube a todos los pisos.", "ascensor", ["llave", "toalla", "cama"], "An elevator goes up.", tr="The elevator goes up to all the floors."),
        F("Necesito la ___ de mi habitación.", "llave", ["toalla", "cuenta", "tarea"], "A room key.", tr="I need my room key."),
        F("Su oficina está en el ___, no en el segundo.", "tercero", ["tercer", "tercera", "tres"], "Without the noun: tercero.", tr="His office is on the third, not the second."),
        M("What is “la planta baja”?", "the ground floor", ["the top floor", "the basement", "the garden"], "Planta baja = ground floor."),
        M("Who is “el huésped”?", "the guest", ["the owner", "the cook", "the driver"], "Huésped = guest."),
        M("Which is correct?", "el cuarto piso", ["el cuarto pisos", "la cuarto piso", "el cuarta piso"], "Cuarto agrees with piso (masculine singular)."),
        M("What does “¿Me puede dar otra llave?” ask for?", "another key", ["a room", "the bill", "a taxi"], "Otra llave = another key."),
    ],
)

# ---------------------------------------------------------------------------- 203
L203 = lesson(
    "Toiletries, things to pack and documents",
    "el jabón, el champú, las gafas de sol, el acta de nacimiento",
    requires=["toalla", "papel", "pasta", "revista", "cámara", "licencia", "documento", "vigencia", "cuota"],
    cards=[
        card("Toiletries and travel things",
             "Hotels usually provide towels and soap, but bring your own toothbrush. Here are words for the bathroom "
             "bag and the suitcase.",
             tables=[table(["Palabra", "English"],
                           [["el jabón", "soap"],
                            ["el champú", "shampoo"],
                            ["el cepillo de dientes", "toothbrush"],
                            ["la pasta de dientes", "toothpaste"],
                            ["el papel higiénico", "toilet paper"],
                            ["la toalla", "towel"],
                            ["las gafas de sol", "sunglasses"],
                            ["el protector solar", "sunscreen"],
                            ["el equipaje de mano", "carry-on luggage"],
                            ["la revista", "magazine"],
                            ["la cámara digital", "digital camera"]],
                           say=[0])]),
        card("Documents",
             "For international travel you often need papers: el pasaporte, la visa, el acta de nacimiento (birth "
             "certificate), la licencia de manejar (driver’s license), el comprobante (receipt, proof). La vigencia is "
             "how long a document is valid, and la cuota is a fee.",
             examples=[
                 ex("Necesito el acta de nacimiento para el pasaporte.", "I need the birth certificate for the passport.", "acta de nacimiento"),
                 ex("Mi licencia de manejar tiene vigencia hasta el año próximo.", "My driver’s license is valid until next year.", "vigencia"),
                 ex("Pago la cuota en el banco y guardo el comprobante.", "I pay the fee at the bank and keep the receipt.", "comprobante"),
                 ex("Llevo las gafas de sol y el protector solar a la playa.", "I take sunglasses and sunscreen to the beach.", "protector solar"),
             ]),
    ],
    exercises=[
        F("Me lavo los dientes con el cepillo y la ___ de dientes.", "pasta", ["toalla", "llave", "revista"], "Pasta de dientes = toothpaste.", tr="I brush my teeth with the toothbrush and the toothpaste."),
        F("Después de la ducha me seco con la ___.", "toalla", ["pasta", "cámara", "licencia"], "A towel dries you.", tr="After the shower I dry myself with the towel."),
        F("En la playa uso las gafas de sol y el ___ solar.", "protector", ["jabón", "champú", "comprobante"], "Protector solar = sunscreen.", tr="At the beach I use sunglasses and sunscreen."),
        F("En el avión leo una ___.", "revista", ["toalla", "cuota", "llave"], "A magazine to read.", tr="On the plane I read a magazine."),
        F("Para manejar necesito mi ___ de manejar.", "licencia", ["revista", "cuota", "toalla"], "Licencia de manejar = driver’s license.", tr="To drive I need my driver’s license."),
        M("What is “el acta de nacimiento”?", "the birth certificate", ["the airplane ticket", "the marriage license", "the passport photo"], "Nacimiento = birth."),
        M("What does “la vigencia” mean?", "how long a document is valid", ["the price", "the weight", "the color"], "Vigencia = validity."),
        M("What is “el equipaje de mano”?", "carry-on luggage", ["lost luggage", "luggage on the floor", "a hand towel"], "De mano = hand."),
        M("What is “el champú”?", "shampoo", ["soap", "toothpaste", "towel"], "Champú = shampoo."),
    ],
)

# ---------------------------------------------------------------------------- 204
L204 = lesson(
    "Problems at the hotel",
    "No hay toallas. El aire no funciona. Hay mucho ruido.",
    requires=["funcionar", "ruido", "limpio", "sucio", "ocupado", "caliente", "aire", "cama", "baño", "gerente", "queja"],
    cards=[
        card("Complaining politely",
             "Start with Tengo un problema, say what is wrong, and ask for help. The staff will answer with a polite "
             "expression like Con mucho gusto (with pleasure) or Lo siento mucho (I’m very sorry).",
             tables=[table(["El problema", "La respuesta"],
                           [["No hay toallas en el baño.", "Con mucho gusto, las mandamos ahora."],
                            ["El aire acondicionado no funciona.", "Lo siento mucho. Mandamos a alguien."],
                            ["El agua caliente no funciona.", "Un momento, por favor."],
                            ["Hay mucho ruido en el pasillo.", "Le damos otra habitación."],
                            ["La habitación está sucia.", "Perdón. Mandamos a la empleada."]],
                           say=[0, 1])]),
        card("Describing what’s wrong",
             "Use estar with sucio, limpio and ocupado, and funcionar to say that something works or doesn’t. Ask to "
             "speak to the manager (el gerente) if the problem stays.",
             examples=[
                 ex("Tengo un problema con mi habitación.", "I have a problem with my room.", "Tengo un problema"),
                 ex("La habitación está ocupada.", "The room is occupied.", "ocupada"),
                 ex("El baño está sucio.", "The bathroom is dirty.", "sucio"),
                 ex("Quiero hablar con el gerente.", "I want to speak with the manager.", "gerente"),
             ]),
    ],
    exercises=[
        F("Ahora el aire acondicionado no ___.", "funciona", ["funcionan", "funciono", "funcionas"], "El aire → él: funciona.", tr="Right now the air conditioning doesn’t work.", lemma="funcionar:él"),
        F("Hay mucho ___ en el pasillo; no puedo dormir.", "ruido", ["dinero", "cama", "llave"], "Noise keeps you awake.", tr="There is a lot of noise in the hallway; I can’t sleep."),
        F("La habitación está ___; necesita limpieza.", "sucia", ["sucio", "sucias", "sucios"], "Habitación is feminine singular.", tr="The room is dirty; it needs cleaning."),
        F("Esta habitación está ___; hay otra persona aquí.", "ocupada", ["ocupado", "ocupadas", "ocupados"], "Habitación is feminine singular.", tr="This room is occupied; there is someone else here."),
        F("No hay toallas; necesito ___.", "otras", ["otro", "otra", "otros"], "Toallas is feminine plural.", tr="There are no towels; I need some more."),
        M("What does “Con mucho gusto” mean?", "With pleasure", ["With much noise", "Thank you very much", "Nice to meet you"], "A polite reply."),
        M("What does “El agua caliente no funciona” mean?", "The hot water doesn’t work.", ["The cold water is ready.", "The water is dirty.", "There is no bathroom."], "Caliente = hot."),
        M("Who can you ask to speak with when a problem is serious?", "el gerente", ["el huésped", "el peatón", "el taxista"], "Gerente = manager."),
        M("Which sentence is correct?", "La habitación está limpia.", ["La habitación está limpio.", "La habitación es limpia.", "La habitación están limpia."], "Estar + limpia, agreeing with habitación."),
    ],
    verify=vp("funcionar", "funciono", "funcionas", "funciona", "funcionamos", "funcionáis", "funcionan"),
)

# ---------------------------------------------------------------------------- 205
L205 = lesson(
    "Pasar: happen, spend, have a good time",
    "¿Qué pasó? Lo pasamos muy bien.",
    requires=["pasar", "tiempo", "bien", "mal", "nada", "playa"],
    cards=[
        card("An all-purpose verb",
             "Pasar can mean to pass, but it has other everyday uses: to happen (¿Qué pasó? No pasó nada), to spend "
             "time (Pasé mucho tiempo en la playa), and with lo, to have a good or bad time (Lo pasamos muy bien).",
             tables=[table(["Uso", "Ejemplo"],
                           [["to happen", "¿Qué pasó? No pasó nada."],
                            ["to spend time", "Pasé mucho tiempo en la playa."],
                            ["to have a good time", "Lo pasamos muy bien en la fiesta."],
                            ["to have a bad time", "Lo pasé mal en el hotel."]],
                           say=[1])]),
        card("In use",
             "Pasar por is also to go through or to pass by: pasar por la aduana. The same verb in the preterite "
             "makes questions about what happened to you: ¿Qué te pasó?",
             examples=[
                 ex("¿Qué pasó en el hotel?", "What happened at the hotel?", "pasó"),
                 ex("Ayer no pasó nada especial.", "Nothing special happened yesterday.", "pasó"),
                 ex("Pasé tres días en la playa.", "I spent three days at the beach.", "Pasé"),
                 ex("Lo pasamos muy bien en la playa.", "We had a great time at the beach.", "Lo pasamos"),
                 ex("¿Qué te pasó?", "What happened to you?", "pasó"),
             ]),
    ],
    exercises=[
        F("Ayer, ¿qué ___ en el hotel?", "pasó", ["pasa", "pasé", "pasaron"], "Ayer → preterite; la pregunta → él: pasó.", tr="Yesterday, what happened at the hotel?", lemma="pasar:él:pret"),
        F("Nosotros lo ___ muy bien en la playa.", "pasamos", ["pasan", "pasó", "pasé"], "Nosotros → pasamos.", tr="We had a great time at the beach.", lemma="pasar:nosotros:pret"),
        F("Yo ___ tres días en la playa.", "pasé", ["pasó", "pasaron", "pasamos"], "Yo → pasé.", tr="I spent three days at the beach.", lemma="pasar:yo:pret"),
        F("Ayer no ___ nada especial.", "pasó", ["pasa", "pasé", "pasaron"], "Nada is singular → pasó.", tr="Nothing special happened yesterday.", lemma="pasar:él:pret"),
        F("Lo ___ mal en el hotel; no hubo agua caliente.", "pasé", ["pasó", "pasamos", "pasaron"], "Yo → pasé.", tr="I had a bad time at the hotel; there was no hot water.", lemma="pasar:yo:pret"),
        M("What does “¿Qué pasó?” mean?", "It asks what happened", ["It asks what is passing", "It asks what you passed", "It asks what will pass"], "Pasar = to happen."),
        M("What does “Lo pasamos muy bien” mean?", "We had a great time.", ["We passed it well.", "We spent a lot of money.", "We forgot it."], "Pasarlo bien = have a good time."),
        M("What does “Pasé mucho tiempo en el aeropuerto” mean?", "I spent a lot of time at the airport.", ["I passed through the airport quickly.", "I forgot the time.", "I lost my ticket."], "Pasar tiempo = spend time."),
        M("How do you say “Nothing happened”?", "No pasó nada.", ["Pasó no nada.", "No pasa nunca.", "Nada no pasó."], "No + verb + nada."),
    ],
    verify=vpp("pasar", "pasé", "pasaste", "pasó", "pasamos", "pasasteis", "pasaron"),
)

# ---------------------------------------------------------------------------- 206
L206 = lesson(
    "Irregular preterites: poner, saber, querer",
    "puse, supe, quise · puso, supo, quiso",
    requires=["poner", "saber", "querer", "maleta", "noticia", "ayer"],
    cards=[
        card("Three more irregular stems",
             "These verbs use the same endings as estar, tener and poder (-e, -iste, -o, -imos, -isteis, -ieron), with "
             "no written accents. The stems are pus- (poner), sup- (saber) and quis- (querer).",
             tables=[table(["", "poner", "saber", "querer"],
                           [["yo", "pus{e}", "sup{e}", "quis{e}"],
                            ["tú", "pus{iste}", "sup{iste}", "quis{iste}"],
                            ["él · ella · usted", "pus{o}", "sup{o}", "quis{o}"],
                            ["nosotros", "pus{imos}", "sup{imos}", "quis{imos}"],
                            ["vosotros", "pus{isteis}", "sup{isteis}", "quis{isteis}"],
                            ["ellos · ellas · ustedes", "pus{ieron}", "sup{ieron}", "quis{ieron}"]],
                           say=[1, 2, 3])]),
        card("The meaning changes in the preterite",
             "Saber in the preterite means “found out”: Ayer supe la noticia. Querer in the preterite means “tried” "
             "(Quise abrir la puerta); No quise means “I refused”. Poner means “put” or “placed”.",
             examples=[
                 ex("Puse la maleta en el ascensor.", "I put the suitcase in the elevator.", "Puse"),
                 ex("Ayer supe que el vuelo salió tarde.", "Yesterday I found out that the flight left late.", "supe"),
                 ex("Ellos quisieron abrir la puerta, pero no pudieron.", "They tried to open the door, but couldn’t.", "quisieron"),
                 ex("Mi amiga no quiso pagar la cuenta.", "My friend refused to pay the bill.", "no quiso"),
                 ex("Nosotros pusimos la ropa en la cama.", "We put the clothes on the bed.", "pusimos"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ la maleta en el ascensor.", "puse", ["puso", "pongo", "pusieron"], "Yo → puse.", tr="Yesterday I put the suitcase in the elevator.", lemma="poner:yo:pret"),
        F("Anoche ella ___ la noticia por teléfono.", "supo", ["supe", "sabe", "supieron"], "Ella → supo.", tr="Last night she found out the news by phone.", lemma="saber:ella:pret"),
        F("Los turistas ___ abrir la puerta, pero no pudieron.", "quisieron", ["quiso", "quise", "quieren"], "Ellos → quisieron.", tr="The tourists tried to open the door, but could not.", lemma="querer:ellos:pret"),
        F("Nosotros ___ la ropa en la cama.", "pusimos", ["pusieron", "puse", "ponemos"], "Nosotros → pusimos.", tr="We put the clothes on the bed.", lemma="poner:nosotros:pret"),
        F("Anoche, ¿cuándo ___ tú que el hotel estaba lleno?", "supiste", ["supe", "supo", "sabes"], "Tú → supiste.", tr="Last night, when did you find out that the hotel was full?", lemma="saber:tú:pret"),
        M("What does “Ayer supe la noticia” mean?", "Yesterday I found out the news.", ["Yesterday I knew the news.", "Yesterday I told the news.", "Yesterday I wanted the news."], "Saber in the preterite = found out."),
        M("What does “No quise pagar” mean?", "I refused to pay.", ["I forgot to pay.", "I couldn’t pay.", "I will not pay."], "No quise = I refused."),
        M("Which is the ellos preterite of “poner”?", "pusieron", ["ponieron", "pondrán", "ponen"], "Pus- + ieron."),
        M("Which ending is NOT right for these irregular preterites?", "-ó with an accent for ella", ["-o for ella", "-e for yo", "-imos for nosotros"], "Puso, supo, quiso have no accent."),
    ],
    verify=vpp("poner", "puse", "pusiste", "puso", "pusimos", "pusisteis", "pusieron")
           + vpp("saber", "supe", "supiste", "supo", "supimos", "supisteis", "supieron")
           + vpp("querer", "quise", "quisiste", "quiso", "quisimos", "quisisteis", "quisieron"),
)

# ---------------------------------------------------------------------------- 207
L207 = lesson(
    "Irregular preterites: andar, -ucir and compounds",
    "anduve, conduje, traduje, detuve",
    requires=["andar", "conducir", "traducir", "detener", "carretera", "libro", "ciudad"],
    cards=[
        card("Andar and the -ucir verbs",
             "Andar becomes anduv- and follows the pattern of estar and tener. All verbs ending in -ucir (conducir, "
             "traducir, producir, reducir, introducir) use the stem -duj- and take -eron in the ellos form, like decir.",
             tables=[table(["", "andar", "conducir", "traducir"],
                           [["yo", "anduv{e}", "conduj{e}", "traduj{e}"],
                            ["tú", "anduv{iste}", "conduj{iste}", "traduj{iste}"],
                            ["él · ella · usted", "anduv{o}", "conduj{o}", "traduj{o}"],
                            ["nosotros", "anduv{imos}", "conduj{imos}", "traduj{imos}"],
                            ["vosotros", "anduv{isteis}", "conduj{isteis}", "traduj{isteis}"],
                            ["ellos · ellas · ustedes", "anduv{ieron}", "conduj{eron}", "traduj{eron}"]],
                           say=[1, 2, 3])]),
        card("Compounds keep the irregularity",
             "A verb built on an irregular verb keeps the irregularity: tener → detener (detuve, detuvo), mantener "
             "(mantuve), obtener (obtuve); poner → posponer (pospuse); hacer → deshacer (deshice); traer → contraer "
             "(contraje).",
             examples=[
                 ex("Ayer anduve por el centro de la ciudad.", "Yesterday I walked around downtown.", "anduve"),
                 ex("Mi padre condujo el coche por la carretera.", "My father drove the car along the highway.", "condujo"),
                 ex("Ellos tradujeron el libro al español.", "They translated the book into Spanish.", "tradujeron"),
                 ex("El conductor detuvo el coche en la esquina.", "The driver stopped the car at the corner.", "detuvo"),
                 ex("Nosotros anduvimos tres horas por la ciudad.", "We walked for three hours around the city.", "anduvimos"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ por el centro de la ciudad.", "anduve", ["anduvo", "ando", "anduvieron"], "Yo → anduve.", tr="Yesterday I walked around downtown.", lemma="andar:yo:pret"),
        F("Mi padre ___ el coche por la carretera.", "condujo", ["conduje", "conducen", "condujeron"], "Él → condujo.", tr="My father drove the car along the highway.", lemma="conducir:él:pret"),
        F("Los estudiantes ___ el libro al español.", "tradujeron", ["tradujo", "traduje", "traducen"], "Ellos → tradujeron (no i).", tr="The students translated the book into Spanish.", lemma="traducir:ellos:pret"),
        F("El conductor ___ el coche en la esquina.", "detuvo", ["detuve", "detienen", "detuvieron"], "Él → detuvo.", tr="The driver stopped the car at the corner.", lemma="detener:él:pret"),
        F("Nosotros ___ tres horas por la ciudad.", "anduvimos", ["anduvieron", "anduve", "andamos"], "Nosotros → anduvimos.", tr="We walked for three hours around the city.", lemma="andar:nosotros:pret"),
        M("Which verb is conjugated like “traducir” in the preterite?", "conducir", ["conocer", "cocinar", "caminar"], "Both end in -ucir."),
        M("What is the ellos preterite of “conducir”?", "condujeron", ["condujieron", "conducieron", "conducen"], "After j the ending is -eron."),
        M("What is the yo preterite of “mantener”?", "mantuve", ["mantené", "mantengo", "mantuvo"], "Same pattern as tener."),
        M("What does “Anduvimos por el centro” mean?", "We walked around downtown.", ["We drove downtown.", "We lived downtown.", "We stopped downtown."], "Andar = to walk, go around."),
    ],
    verify=vpp("andar", "anduve", "anduviste", "anduvo", "anduvimos", "anduvisteis", "anduvieron")
           + vpp("conducir", "conduje", "condujiste", "condujo", "condujimos", "condujisteis", "condujeron")
           + vpp("traducir", "traduje", "tradujiste", "tradujo", "tradujimos", "tradujisteis", "tradujeron")
           + vpp("detener", "detuve", "detuviste", "detuvo", "detuvimos", "detuvisteis", "detuvieron"),
)

# ---------------------------------------------------------------------------- 208
L208 = lesson(
    "Spelling changes in the yo preterite",
    "busqué, llegué, empecé",
    requires=["buscar", "llegar", "empezar", "jugar", "sacar", "comenzar", "pagar"],
    cards=[
        card("Keeping the sound",
             "Verbs ending in -car, -gar and -zar change their spelling in the yo form of the preterite, so that the "
             "last consonant keeps the sound of the infinitive. Every other form is regular.",
             tables=[table(["Final", "Cambio", "Infinitivo", "yo"],
                           [["-car", "c → qu", "buscar", "busqué"],
                            ["-car", "c → qu", "sacar", "saqué"],
                            ["-car", "c → qu", "explicar", "expliqué"],
                            ["-gar", "g → gu", "llegar", "llegué"],
                            ["-gar", "g → gu", "jugar", "jugué"],
                            ["-zar", "z → c", "empezar", "empecé"],
                            ["-zar", "z → c", "almorzar", "almorcé"]],
                           say=[2, 3])]),
        card("Only the yo form changes",
             "Compare: yo busqué, tú buscaste, él buscó. The tú, él, nosotros and ellos forms keep the original "
             "consonant because the following vowel (a or o) does not change the sound.",
             examples=[
                 ex("Ayer busqué mi llave en la habitación.", "Yesterday I looked for my key in the room.", "busqué"),
                 ex("Yo llegué al hotel a las seis.", "I arrived at the hotel at six.", "llegué"),
                 ex("El año pasado empecé a estudiar español.", "Last year I started studying Spanish.", "empecé"),
                 ex("Yo almorcé con mis amigos.", "I had lunch with my friends.", "almorcé"),
                 ex("Mi hermano buscó la llave, pero yo no la busqué.", "My brother looked for the key, but I didn’t look for it.", "busqué"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ mi llave en la habitación.", "busqué", ["busco", "buscó", "buscaron"], "Yo → busqué (c → qu).", tr="Yesterday I looked for my key in the room.", lemma="buscar:yo:pret"),
        F("Yo ___ al hotel a las seis de la tarde.", "llegué", ["llegó", "llego", "llegaron"], "Yo → llegué (g → gu).", tr="I arrived at the hotel at six in the evening.", lemma="llegar:yo:pret"),
        F("Anoche yo ___ al fútbol con mis amigos.", "jugué", ["jugó", "juego", "jugaron"], "Yo → jugué.", tr="Last night I played soccer with my friends.", lemma="jugar:yo:pret"),
        F("Ayer yo ___ a las doce con mis amigos.", "almorcé", ["almorzó", "almuerzo", "almorzaron"], "Yo → almorcé (z → c).", tr="Yesterday I had lunch at twelve with my friends.", lemma="almorzar:yo:pret"),
        F("Hace un año yo ___ a estudiar español.", "empecé", ["empezó", "empiezo", "empezaron"], "Yo → empecé.", tr="A year ago I started to study Spanish.", lemma="empezar:yo:pret"),
        M("Why do we write “busqué” and not “buscé”?", "to keep the k sound", ["to show the plural", "to show the past", "because c is silent"], "C before e would sound like s."),
        M("Which form is regular (no spelling change)?", "buscaste", ["busqué", "llegué", "empecé"], "Only yo changes."),
        M("What is the yo preterite of “sacar”?", "saqué", ["sacé", "saco", "sacó"], "C → qu before é."),
        M("What is the yo preterite of “comenzar”?", "comencé", ["comenzé", "comenzo", "comenzaron"], "Z → c before é."),
    ],
    verify=vpp("buscar", "busqué", "buscaste", "buscó", "buscamos", "buscasteis", "buscaron")
           + vpp("jugar", "jugué", "jugaste", "jugó", "jugamos", "jugasteis", "jugaron")
           + vpp("almorzar", "almorcé", "almorzaste", "almorzó", "almorzamos", "almorzasteis", "almorzaron")
           + vpp("empezar", "empecé", "empezaste", "empezó", "empezamos", "empezasteis", "empezaron")
           + vpp("sacar", "saqué", "sacaste", "sacó", "sacamos", "sacasteis", "sacaron"),
)

# ---------------------------------------------------------------------------- 209
L209 = lesson(
    "Caer, oír, leer, creer: the y in the preterite",
    "cayó, oyó, leyó, creyeron",
    requires=["caer", "oír", "leer", "creer", "noticia", "suelo"],
    cards=[
        card("When the i would sit between vowels",
             "In -er and -ir verbs whose stem ends in a vowel (caer, oír, leer, creer, construir), the ending -ió "
             "becomes -yó, and -ieron becomes -yeron. This only happens in the él and ellos forms. The other forms "
             "need a written accent on the í: caí, caíste, caímos.",
             tables=[table(["", "caer", "oír", "leer", "creer"],
                           [["yo", "caí", "oí", "leí", "creí"],
                            ["tú", "caíste", "oíste", "leíste", "creíste"],
                            ["él · ella · usted", "ca{yó}", "o{yó}", "le{yó}", "cre{yó}"],
                            ["nosotros", "caímos", "oímos", "leímos", "creímos"],
                            ["vosotros", "caísteis", "oísteis", "leísteis", "creísteis"],
                            ["ellos · ellas · ustedes", "ca{yeron}", "o{yeron}", "le{yeron}", "cre{yeron}"]],
                           say=[1, 2, 3, 4])]),
        card("In use",
             "Caerse is often used for things that fall: Se cayó la maleta. Oír means to hear and also to listen "
             "(with attention). Leer and creer you already know in the present.",
             examples=[
                 ex("La maleta cayó al suelo.", "The suitcase fell to the floor.", "cayó"),
                 ex("Ayer oí la noticia en la radio.", "Yesterday I heard the news on the radio.", "oí"),
                 ex("Ella leyó un libro en el avión.", "She read a book on the plane.", "leyó"),
                 ex("Ellos creyeron que el vuelo salió a tiempo.", "They thought the flight left on time.", "creyeron"),
                 ex("Tú leíste la carta, ¿verdad?", "You read the letter, didn’t you?", "leíste"),
             ]),
    ],
    exercises=[
        F("La maleta ___ al suelo.", "cayó", ["cayeron", "caí", "cae"], "Singular subject → cayó.", tr="The suitcase fell to the floor.", lemma="caer:él:pret"),
        F("Ayer yo ___ la noticia en la radio.", "oí", ["oyó", "oigo", "oyeron"], "Yo → oí, with accent.", tr="Yesterday I heard the news on the radio.", lemma="oír:yo:pret"),
        F("Ella ___ un libro en el avión.", "leyó", ["leyeron", "leí", "lee"], "Ella → leyó.", tr="She read a book on the plane.", lemma="leer:ella:pret"),
        F("Mis amigos ___ que el vuelo salió a tiempo.", "creyeron", ["creyó", "creí", "creen"], "Ellos → creyeron.", tr="My friends thought the flight left on time.", lemma="creer:ellos:pret"),
        F("Tú ___ la carta en el hotel, ¿verdad?", "leíste", ["leyó", "leí", "lees"], "Tú → leíste, with accent.", tr="You read the letter at the hotel, right?", lemma="leer:tú:pret"),
        M("Why is it “cayó” and not “caió”?", "i between vowels becomes y", ["it is plural", "it is a question", "caer is regular"], "The i would sit between two vowels."),
        M("Which forms need a written accent on the í?", "caí, caíste, caímos", ["cayó, cayeron", "cae, caen", "caeré, caerá"], "Yo, tú, nosotros, vosotros."),
        M("What is the ellos preterite of “oír”?", "oyeron", ["oyieron", "oieron", "oyen"], "O + yeron."),
        M("What does “Se cayó la maleta” suggest?", "The suitcase fell.", ["The suitcase is open.", "The suitcase is lost.", "The suitcase is heavy."], "Caerse = to fall."),
    ],
    verify=vpp("caer", "caí", "caíste", "cayó", "caímos", "caísteis", "cayeron")
           + vpp("oír", "oí", "oíste", "oyó", "oímos", "oísteis", "oyeron")
           + vpp("leer", "leí", "leíste", "leyó", "leímos", "leísteis", "leyeron")
           + vpp("creer", "creí", "creíste", "creyó", "creímos", "creísteis", "creyeron"),
)

# ---------------------------------------------------------------------------- 210
L210 = lesson(
    "Stem-changing -ir verbs in the preterite",
    "pidió, sirvió, durmió, prefirieron",
    requires=["pedir", "servir", "seguir", "repetir", "preferir", "sentir", "dormir", "morir", "vestir", "mentir"],
    cards=[
        card("Only -ir verbs, only él and ellos",
             "In the present, boot verbs change in many forms. In the preterite, -ar and -er verbs have no stem change "
             "at all. Only -ir verbs change, and only in the él/ella/usted and ellos/ellas/ustedes forms: e → i and "
             "o → u. The other four forms use the regular stem.",
             tables=[table(["", "pedir", "dormir", "preferir"],
                           [["yo", "pedí", "dormí", "preferí"],
                            ["tú", "pediste", "dormiste", "preferiste"],
                            ["él · ella · usted", "p{i}dió", "d{u}rmió", "pref{i}rió"],
                            ["nosotros", "pedimos", "dormimos", "preferimos"],
                            ["vosotros", "pedisteis", "dormisteis", "preferisteis"],
                            ["ellos · ellas · ustedes", "p{i}dieron", "d{u}rmieron", "pref{i}rieron"]],
                           say=[1, 2, 3])]),
        card("Common verbs",
             "e → i: pedir, servir, seguir, repetir, conseguir, vestirse, sugerir, mentir (mintió), sentir (sintió), "
             "preferir, divertirse. o → u: dormir (durmió), morir (murió).",
             examples=[
                 ex("El mesero sirvió la sopa muy caliente.", "The waiter served the soup very hot.", "sirvió"),
                 ex("Yo pedí el pollo, pero mi amigo pidió pescado.", "I ordered the chicken, but my friend ordered fish.", "pidió"),
                 ex("Ella durmió ocho horas en el hotel.", "She slept eight hours at the hotel.", "durmió"),
                 ex("Nosotros seguimos derecho por la calle.", "We continued straight along the street.", "seguimos"),
                 ex("Ellos se divirtieron mucho en la playa.", "They had a lot of fun at the beach.", "divirtieron"),
             ]),
    ],
    exercises=[
        F("Yo pedí el pollo, pero mi amigo ___ pescado.", "pidió", ["pedió", "pidieron", "pide"], "Él → pidió (e → i).", tr="I ordered the chicken, but my friend ordered fish.", lemma="pedir:él:pret"),
        F("El mesero ___ la sopa muy caliente.", "sirvió", ["sirve", "sirvieron", "serví"], "Él → sirvió.", tr="The waiter served the soup very hot.", lemma="servir:él:pret"),
        F("Anoche ella ___ ocho horas en el hotel.", "durmió", ["dormió", "duermen", "dormí"], "Ella → durmió (o → u).", tr="Last night she slept eight hours at the hotel.", lemma="dormir:ella:pret"),
        F("Nosotros ___ derecho por la calle.", "seguimos", ["siguieron", "sigo", "siguió"], "Nosotros has no stem change.", tr="We continued straight down the street.", lemma="seguir:nosotros:pret"),
        F("Mis padres ___ el hotel con vista al mar.", "prefirieron", ["prefiere", "preferí", "prefirió"], "Ellos → prefirieron.", tr="My parents preferred the hotel with an ocean view.", lemma="preferir:ellos:pret"),
        M("Which preterite forms of “pedir” have the stem change?", "él/ella and ellos/ellas only", ["all forms", "only yo", "only nosotros"], "e → i only in the third person."),
        M("What is the él preterite of “morir”?", "murió", ["morió", "muerió", "muere"], "O → u in the third person."),
        M("Do -ar verbs like “cerrar” have a stem change in the preterite?", "No — only -ir verbs do", ["Yes, in all forms", "Yes, in the yo form", "Only in the plural"], "Cerrar: cerró, cerraron."),
        M("What is the ellos preterite of “repetir”?", "repitieron", ["repetieron", "repiten", "repitiron"], "Repit- + ieron."),
    ],
    verify=vpp("pedir", "pedí", "pediste", "pidió", "pedimos", "pedisteis", "pidieron")
           + vpp("servir", "serví", "serviste", "sirvió", "servimos", "servisteis", "sirvieron")
           + vpp("dormir", "dormí", "dormiste", "durmió", "dormimos", "dormisteis", "durmieron")
           + vpp("seguir", "seguí", "seguiste", "siguió", "seguimos", "seguisteis", "siguieron")
           + vpp("preferir", "preferí", "preferiste", "prefirió", "preferimos", "preferisteis", "prefirieron"),
)

# ---------------------------------------------------------------------------- 211
L211 = lesson(
    "A holiday that went wrong",
    "El primer día, el hotel nos dio una habitación sin vista.",
    requires=["hotel", "habitación", "dormir", "gerente", "toalla", "aire", "día"],
    cards=[
        card("Read the anecdote",
             "Every verb is in the preterite. Find the irregular stems (dio, dijo, pudimos, fuimos), the "
             "stem change (pidió) and the regular forms (pedimos, dormimos). Había is the imperfect, not the preterite.",
             examples=[
                 ex("El primer día, el hotel nos dio una habitación sin vista al mar.", "On the first day, the hotel gave us a room without an ocean view.", "dio"),
                 ex("Pedimos otra, pero el recepcionista nos dijo que no había más.", "We asked for another one, but the clerk told us there were no more.", "dijo"),
                 ex("Al día siguiente no pudimos encontrar toallas hasta el mediodía.", "The next day we could not find towels until noon.", "pudimos"),
                 ex("Esa noche el aire acondicionado no funcionó y dormimos muy mal.", "That night the air conditioning did not work and we slept very badly.", "funcionó"),
                 ex("El tercer día fuimos a hablar con el gerente.", "On the third day we went to talk to the manager.", "fuimos"),
                 ex("Él nos pidió disculpas y nos dio otra habitación en el cuarto piso.", "He apologized to us and gave us another room on the fourth floor.", "pidió"),
                 ex("Por fin pasamos unos días tranquilos.", "At last we spent a few quiet days.", "pasamos"),
             ]),
        card("Words that tell a story",
             "Sequence words organize an anecdote: el primer día, al día siguiente, esa noche, el tercer día, por fin. "
             "Pedir disculpas means to apologize.",
             tables=[table(["Expresión", "English"],
                           [["el primer día", "the first day"],
                            ["al día siguiente", "the next day"],
                            ["esa noche", "that night"],
                            ["por fin", "at last"],
                            ["pedir disculpas", "to apologize"]],
                           say=[0])]),
    ],
    exercises=[
        F("El primer día, el hotel nos ___ una habitación sin vista.", "dio", ["di", "dieron", "da"], "El hotel → él: dio.", tr="On the first day, the hotel gave us a room without a view.", lemma="dar:él:pret"),
        F("El recepcionista nos ___ que no había más.", "dijo", ["dije", "dijeron", "dice"], "Él → dijo.", tr="The clerk told us there were no more.", lemma="decir:él:pret"),
        F("Al día siguiente no ___ encontrar toallas.", "pudimos", ["pudo", "pudieron", "podemos"], "Nosotros → pudimos.", tr="The next day we could not find towels.", lemma="poder:nosotros:pret"),
        F("Esa noche nosotros ___ muy mal.", "dormimos", ["durmieron", "dormí", "dormió"], "Nosotros has no stem change.", tr="That night we slept very badly.", lemma="dormir:nosotros:pret"),
        F("El gerente nos ___ disculpas.", "pidió", ["pedió", "pidieron", "pedí"], "Él → pidió (e → i).", tr="The manager apologized to us.", lemma="pedir:él:pret"),
        M("What went wrong with the first room?", "It had no ocean view.", ["It was too expensive.", "It was too small.", "It was dirty."], "Sin vista al mar."),
        M("What problem did they have the second night?", "The air conditioning didn’t work.", ["The towels were missing.", "The elevator was broken.", "The water was cold."], "El aire acondicionado no funcionó."),
        M("What did the manager do?", "He apologized and gave them another room.", ["He refused to help.", "He called the police.", "He moved them to the street."], "Pidió disculpas y dio otra habitación."),
        M("What does “por fin” mean?", "at last", ["at first", "never", "sometimes"], "Por fin = finally."),
    ],
)

# ---------------------------------------------------------------------------- 212
L212 = lesson(
    "Which preterite? Practice",
    "regular, spelling change, y-change, stem change, irregular",
    requires=["pedir", "llegar", "leer", "hacer", "ir", "dormir", "dar", "buscar"],
    cards=[
        card("A decision guide",
             "To choose a preterite form, ask yourself these questions in order.",
             tables=[table(["Pregunta", "Ejemplo"],
                           [["¿Es ser o ir? → fui, fue", "Ayer fui al hotel."],
                            ["¿Tiene raíz irregular? → tuve, hice, dije", "Ayer hice la maleta."],
                            ["¿Termina en -car, -gar, -zar y es yo? → busqué, llegué", "Yo llegué tarde."],
                            ["¿Es -ir con cambio e → i u o → u en él o ellos? → pidió", "Ella durmió bien."],
                            ["¿Tiene una vocal antes de -er o -ir? → leyó, cayeron", "Él leyó la carta."],
                            ["Si no, es regular → habló, comió, viví", "Nosotros comimos allí."]],
                           say=[1])]),
        card("Quick examples",
             "Each sentence below uses one of the patterns above.",
             examples=[
                 ex("Ayer fui al hotel y pedí una llave.", "Yesterday I went to the hotel and asked for a key.", "fui"),
                 ex("Yo busqué mi pasaporte, pero mi hermana lo encontró.", "I looked for my passport, but my sister found it.", "busqué"),
                 ex("Ella leyó el menú y pidió pescado.", "She read the menu and ordered fish.", "leyó"),
                 ex("Ellos durmieron en la pensión.", "They slept at the guesthouse.", "durmieron"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ al hotel y pedí una llave.", "fui", ["fue", "voy", "fueron"], "Ir → fui.", tr="Yesterday I went to the hotel and asked for a key.", lemma="ir:yo:pret"),
        F("Anoche nosotros ___ la cena en el hotel.", "hicimos", ["hizo", "hicieron", "hacemos"], "Hacer → hicimos.", tr="Last night we made dinner at the hotel.", lemma="hacer:nosotros:pret"),
        F("Yo ___ al aeropuerto a las seis de la mañana.", "llegué", ["llegó", "llego", "llegaron"], "Yo → llegué.", tr="I arrived at the airport at six in the morning.", lemma="llegar:yo:pret"),
        F("Ella ___ el menú y pidió pescado.", "leyó", ["leyeron", "leí", "lee"], "Ella → leyó.", tr="She read the menu and ordered fish.", lemma="leer:ella:pret"),
        F("Los niños ___ en la pensión.", "durmieron", ["dormieron", "dormí", "duermen"], "Ellos → durmieron.", tr="The children slept at the guesthouse.", lemma="dormir:ellos:pret"),
        F("El recepcionista nos ___ la llave.", "dio", ["di", "dieron", "da"], "Él → dio.", tr="The clerk gave us the key.", lemma="dar:él:pret"),
        F("Yo ___ mi pasaporte, pero no lo encontré.", "busqué", ["buscó", "busco", "buscaron"], "Yo → busqué.", tr="I looked for my passport, but I didn’t find it.", lemma="buscar:yo:pret"),
        M("Which is the correct él preterite of “pedir”?", "pidió", ["pedió", "pide", "pidieron"], "E → i in the third person."),
        M("Which verb has an irregular stem in the preterite?", "tener", ["hablar", "comer", "vivir"], "Tener → tuv-."),
        M("Which is the yo preterite of “jugar”?", "jugué", ["jugó", "jugé", "juego"], "G → gu before é."),
    ],
)

# ---------------------------------------------------------------------------- 213
L213 = lesson(
    "Formal commands: usted and ustedes",
    "Escriba la dirección. Lean las instrucciones.",
    requires=["escribir", "leer", "hablar", "abrir", "caminar", "comer", "dirección", "instrucción"],
    cards=[
        card("How to form a formal command",
             "A command tells someone what to do. Formal commands are used with people you address as usted (one "
             "person) or ustedes (more than one). Take the yo form of the present tense, drop the -o, and add the "
             "opposite vowel: -ar verbs take -e / -en, and -er and -ir verbs take -a / -an.",
             tables=[table(["Infinitivo", "yo", "usted", "ustedes"],
                           [["caminar", "camino", "camin{e}", "camin{en}"],
                            ["hablar", "hablo", "habl{e}", "habl{en}"],
                            ["leer", "leo", "le{a}", "le{an}"],
                            ["comer", "como", "com{a}", "com{an}"],
                            ["escribir", "escribo", "escrib{a}", "escrib{an}"],
                            ["abrir", "abro", "abr{a}", "abr{an}"]],
                           say=[0, 1, 2, 3])]),
        card("Using commands politely",
             "Add por favor to be polite. The pronouns usted and ustedes may follow the command for emphasis or "
             "clarity: Escriba usted la dirección. In writing, a strong command can sit between exclamation marks.",
             examples=[
                 ex("Escriba la dirección, por favor.", "Write down the address, please.", "Escriba"),
                 ex("Lean las instrucciones.", "Read the instructions.", "Lean"),
                 ex("¡Camine rápido!", "Walk fast!", "Camine"),
                 ex("Abran sus libros, por favor.", "Open your books, please.", "Abran"),
                 ex("Hable más despacio, por favor.", "Speak more slowly, please.", "Hable"),
                 ex("Coman antes de salir.", "Eat before leaving.", "Coman"),
             ]),
    ],
    exercises=[
        F("Señor, ___ la dirección, por favor.", "escriba", ["escribe", "escribo", "escribir"], "Usted command of -ir: -a.", tr="Sir, write down the address, please.", lemma="escribir:usted:cmd"),
        F("Señores, ___ las instrucciones.", "lean", ["lee", "lea", "leen"], "Ustedes command of -er: -an.", tr="Gentlemen, read the instructions.", lemma="leer:ustedes:cmd"),
        F("Señora, ___ más despacio, por favor.", "hable", ["habla", "hablo", "hablen"], "Usted command of -ar: -e.", tr="Ma’am, speak more slowly, please.", lemma="hablar:usted:cmd"),
        F("Señores, ___ sus libros.", "abran", ["abre", "abra", "abren"], "Ustedes command of -ir: -an.", tr="Gentlemen, open your books.", lemma="abrir:ustedes:cmd"),
        F("Señor, ___ rápido, por favor.", "camine", ["caminen", "camina", "camino"], "Usted command of -ar: -e.", tr="Sir, walk fast, please.", lemma="caminar:usted:cmd"),
        M("How do you form the usted command of an -ar verb?", "yo form, drop -o, add -e", ["yo form, drop -o, add -a", "infinitive plus -e", "tú form plus -n"], "-ar verbs take the opposite vowel e."),
        M("How do you form the usted command of an -er or -ir verb?", "yo form, drop -o, add -a", ["yo form, drop -o, add -e", "infinitive plus -a", "tú form minus s"], "-er and -ir verbs take a."),
        M("Which is the ustedes command of “comer”?", "coman", ["coma", "comen", "comer"], "Com- + an."),
        M("In “Escriba usted la dirección”, where does usted stand?", "after the command", ["before the command", "instead of the command", "at the start of the sentence"], "Escriba usted la dirección."),
    ],
    verify=vpc("caminar", "camine", "caminen") + vpc("hablar", "hable", "hablen") + vpc("leer", "lea", "lean")
           + vpc("comer", "coma", "coman") + vpc("escribir", "escriba", "escriban") + vpc("abrir", "abra", "abran"),
)

# ---------------------------------------------------------------------------- 214
L214 = lesson(
    "Formal commands: irregular and stem-changing verbs",
    "Ponga, haga, venga · duerma, pida · busque, llegue · dé, vaya",
    requires=["poner", "hacer", "venir", "dormir", "pedir", "pensar", "buscar", "llegar", "cruzar", "dar", "ir"],
    cards=[
        card("Start from the yo form",
             "The rule still works for irregular yo forms, because the command copies the yo form: pongo → ponga, hago → "
             "haga, vengo → venga. Stem-changing verbs keep the change in the command: duermo → duerma, pido → pida, "
             "pienso → piense.",
             tables=[table(["Infinitivo", "yo", "usted", "ustedes"],
                           [["poner", "pongo", "ponga", "pongan"],
                            ["hacer", "hago", "haga", "hagan"],
                            ["venir", "vengo", "venga", "vengan"],
                            ["dormir", "duermo", "duerma", "duerman"],
                            ["pedir", "pido", "pida", "pidan"],
                            ["pensar", "pienso", "piense", "piensen"]],
                           say=[0, 1, 2, 3])]),
        card("Spelling changes and the truly irregular ones",
             "Verbs ending in -car, -gar and -zar change their spelling, as in the preterite, so that the sound stays: "
             "buscar → busque, llegar → llegue, cruzar → cruce. Dar, ir, ser, estar and saber are fully irregular. "
             "Dé (from dar) has a written accent to tell it from the preposition de.",
             tables=[table(["Infinitivo", "usted", "ustedes"],
                           [["buscar", "busque", "busquen"],
                            ["llegar", "llegue", "lleguen"],
                            ["cruzar", "cruce", "crucen"],
                            ["dar", "dé", "den"],
                            ["ir", "vaya", "vayan"],
                            ["ser", "sea", "sean"],
                            ["estar", "esté", "estén"],
                            ["saber", "sepa", "sepan"]],
                           say=[0, 1, 2])]),
    ],
    exercises=[
        F("Señor, ___ su pasaporte aquí, por favor.", "ponga", ["pone", "pongo", "pongan"], "Poner → pongo → ponga.", tr="Sir, put your passport here, please.", lemma="poner:usted:cmd"),
        F("Señores, ___ pronto a la recepción.", "vengan", ["venga", "vienen", "vengo"], "Venir → vengo → vengan.", tr="Gentlemen, come to the front desk soon.", lemma="venir:ustedes:cmd"),
        F("Señora, ___ otro café, por favor.", "pida", ["pide", "pido", "pidan"], "Pedir → pido → pida.", tr="Ma’am, order another coffee, please.", lemma="pedir:usted:cmd"),
        F("Señor, ___ la calle con cuidado.", "cruce", ["cruza", "cruzo", "crucen"], "Cruzar → cruce (z → c).", tr="Sir, cross the street carefully.", lemma="cruzar:usted:cmd"),
        F("Señor, ___ al aeropuerto en taxi.", "vaya", ["va", "voy", "vayan"], "Ir → vaya.", tr="Sir, go to the airport by taxi.", lemma="ir:usted:cmd"),
        F("Señor, ___ la llave a la recepcionista, por favor.", "dé", ["da", "doy", "den"], "Dar → dé, with accent.", tr="Sir, give the key to the receptionist, please.", lemma="dar:usted:cmd"),
        M("Why does “dé” have a written accent?", "To tell it from the preposition “de”", ["Because it is plural", "Because it is a question", "Because it is the past"], "Dé (command) versus de (of, from)."),
        M("What is the usted command of “buscar”?", "busque", ["busca", "busce", "buscan"], "C → qu before e."),
        M("What is the ustedes command of “dormir”?", "duerman", ["dormen", "duerma", "dormir"], "Stem change o → ue is kept."),
    ],
    verify=vpc("poner", "ponga", "pongan") + vpc("hacer", "haga", "hagan") + vpc("venir", "venga", "vengan")
           + vpc("dormir", "duerma", "duerman") + vpc("pedir", "pida", "pidan") + vpc("pensar", "piense", "piensen")
           + vpc("buscar", "busque", "busquen") + vpc("llegar", "llegue", "lleguen") + vpc("cruzar", "cruce", "crucen")
           + vpc("dar", "dé", "den") + vpc("ir", "vaya", "vayan") + vpc("ser", "sea", "sean")
           + vpc("estar", "esté", "estén") + vpc("saber", "sepa", "sepan"),
)

# ---------------------------------------------------------------------------- 215
L215 = lesson(
    "Negative commands and polite requests",
    "No fume aquí. Por favor, no hablen inglés.",
    requires=["fumar", "hablar", "olvidar", "cerrar", "pasar", "puerta", "favor"],
    cards=[
        card("Put no before the command",
             "To tell someone not to do something, put no before the formal command. Nothing else changes: Camine → No "
             "camine; Abran → No abran.",
             tables=[table(["Afirmativo", "Negativo"],
                           [["Pase.", "No pase."],
                            ["Abran la puerta.", "No abran la puerta."],
                            ["Escriba aquí.", "No escriba aquí."],
                            ["Siga derecho.", "No siga derecho."],
                            ["Doble a la derecha.", "No doble a la derecha."]],
                           say=[0, 1])]),
        card("Being polite",
             "Commands can sound strong. To soften them, add por favor. In class, in hotels and on signs "
             "you will hear them all the time.",
             examples=[
                 ex("No coma en el salón de clase.", "Do not eat in the classroom.", "No coma"),
                 ex("Por favor, no hablen inglés en clase.", "Please don’t speak English in class.", "no hablen"),
                 ex("No fume aquí, por favor.", "Don’t smoke here, please.", "No fume"),
                 ex("No olvide su pasaporte.", "Don’t forget your passport.", "No olvide"),
                 ex("Pase usted, señora.", "Go ahead, ma’am.", "Pase"),
             ]),
    ],
    exercises=[
        F("Señores, por favor, no ___ en el pasillo.", "hablen", ["hablan", "hablar", "hable"], "Ustedes, negative: no hablen.", tr="Gentlemen, please don’t talk in the hallway.", lemma="hablar:ustedes:cmd"),
        F("Señor, no ___ aquí, por favor.", "fume", ["fuma", "fumo", "fumar"], "Usted, negative: no fume.", tr="Sir, don’t smoke here, please.", lemma="fumar:usted:cmd"),
        F("Señora, no ___ su pasaporte en el hotel.", "olvide", ["olvida", "olvido", "olvidar"], "Usted, negative: no olvide.", tr="Ma’am, don’t forget your passport at the hotel.", lemma="olvidar:usted:cmd"),
        F("Señores, no ___ la puerta.", "cierren", ["cierran", "cierre", "cerrar"], "Ustedes, negative: cerrar → cierren.", tr="Gentlemen, don’t close the door.", lemma="cerrar:ustedes:cmd"),
        F("Señor, no ___ a la izquierda; doble a la derecha.", "doble", ["dobla", "doblo", "doblen"], "Usted command of doblar.", tr="Sir, don’t turn left; turn right.", lemma="doblar:usted:cmd"),
        M("Where does “no” go in a negative command?", "before the command", ["after the command", "at the end of the sentence", "before the subject only"], "No + command."),
        M("How do you say “Don’t smoke here, please” to one person (usted)?", "No fume aquí, por favor.", ["No fumas aquí, por favor.", "Fume no aquí, por favor.", "No fumar usted aquí, por favor."], "No + usted command."),
        M("Which word makes a command more polite?", "por favor", ["ahora", "siempre", "mucho"], "Por favor = please."),
        M("What does “No abran la puerta” mean?", "Don’t open the door (to a group).", ["They don’t open the door.", "Open the door (to a group).", "I don’t open the door."], "No + ustedes command."),
    ],
    verify=vpc("fumar", "fume", "fumen") + vpc("olvidar", "olvide", "olviden") + vpc("cerrar", "cierre", "cierren")
           + vpc("doblar", "doble", "doblen") + vpc("pasar", "pase", "pasen"),
)

# ---------------------------------------------------------------------------- 216
L216 = lesson(
    "Giving directions",
    "Siga derecho. Doble a la izquierda. Cruce la calle.",
    requires=["calle", "esquina", "cerca", "cruzar", "seguir", "salir", "pasar", "hotel", "estación"],
    cards=[
        card("Direction words",
             "Directions are almost all formal commands. Learn these phrases and you can guide a tourist.",
             tables=[table(["Frase", "English"],
                           [["Siga derecho.", "Go straight."],
                            ["Doble a la derecha.", "Turn right."],
                            ["Doble a la izquierda.", "Turn left."],
                            ["Cruce la calle.", "Cross the street."],
                            ["a mano derecha", "on the right-hand side"],
                            ["a mano izquierda", "on the left-hand side"],
                            ["el punto de partida", "the starting point"],
                            ["la glorieta · la rotonda", "the roundabout"]],
                           say=[0])]),
        card("A route",
             "Join the steps with y, luego and hasta llegar a. Here is a short route from a hotel to a train station.",
             examples=[
                 ex("Salga del hotel y siga derecho dos cuadras.", "Leave the hotel and go straight two blocks.", "Salga"),
                 ex("Cruce la avenida y siga hasta el semáforo.", "Cross the avenue and continue to the traffic light.", "Cruce"),
                 ex("Doble a la izquierda en la esquina.", "Turn left at the corner.", "Doble"),
                 ex("La estación queda a mano derecha.", "The station is on the right-hand side.", "a mano derecha"),
                 ex("Siga derecho hasta llegar a la glorieta.", "Go straight until you reach the roundabout.", "hasta llegar"),
             ]),
    ],
    exercises=[
        F("Señor, ___ del hotel y siga derecho.", "salga", ["sale", "salgo", "salgan"], "Salir → salgo → salga.", tr="Sir, leave the hotel and go straight.", lemma="salir:usted:cmd"),
        F("Señor, ___ derecho dos cuadras, por favor.", "Siga", ["Sigue", "Sigo", "Sigan"], "Seguir → sigo → siga.", tr="Sir, go straight two blocks, please.", lemma="seguir:usted:cmd"),
        F("Señora, ___ a la izquierda en la esquina.", "Doble", ["Dobla", "Doblo", "Doblen"], "Usted command of doblar.", tr="Ma’am, turn left at the corner.", lemma="doblar:usted:cmd"),
        F("Señor, ___ la calle con cuidado.", "Cruce", ["Cruza", "Cruzo", "Crucen"], "Usted command of cruzar.", tr="Sir, cross the street carefully.", lemma="cruzar:usted:cmd"),
        F("La estación queda a mano ___.", "derecha", ["derecho", "derechas", "derechos"], "Mano is feminine: derecha.", tr="The station is on the right-hand side."),
        M("What does “Doble a la derecha” mean?", "Turn right.", ["Turn left.", "Go straight.", "Stop here."], "Derecha = right."),
        M("What does “Siga derecho” mean?", "Go straight.", ["Turn right.", "Turn around.", "Go back."], "Seguir = to continue."),
        M("What is “el punto de partida”?", "the starting point", ["the final stop", "the police station", "the parking spot"], "Partida = departure."),
        M("What is “la glorieta”?", "the roundabout", ["the corner", "the crosswalk", "the bus stop"], "Glorieta/rotonda = roundabout."),
    ],
    verify=vpc("salir", "salga", "salgan") + vpc("seguir", "siga", "sigan") + vpc("doblar", "doble", "doblen"),
)

# ---------------------------------------------------------------------------- 217
L217 = lesson(
    "Car trouble",
    "La llanta está ponchada. Necesito una grúa.",
    requires=["coche", "motor", "gasolina", "conducir", "llamar", "cambiar", "llevar"],
    cards=[
        card("Parts of a car and problems",
             "A flat tire is una llanta ponchada, and the spare is la llanta de repuesto. The gas tank is el tanque de "
             "gasolina, and it can be vacío (empty) or lleno (full). A tow truck is una grúa. Echar gasolina means "
             "to put gas in the car.",
             tables=[table(["Palabra", "English"],
                           [["la llanta ponchada", "flat tire"],
                            ["la llanta de repuesto", "spare tire"],
                            ["el motor", "engine"],
                            ["el freno", "brake"],
                            ["la bocina", "horn"],
                            ["el tanque vacío · el tanque lleno", "empty tank · full tank"],
                            ["la grúa", "tow truck"],
                            ["echar gasolina", "to put gas in"]],
                           say=[0])]),
        card("What to say, and what to tell others",
             "Describe the problem with tengo, está or no funciona, and give instructions with formal commands.",
             examples=[
                 ex("Tengo una llanta ponchada y no tengo llanta de repuesto.", "I have a flat tire and I don’t have a spare tire.", "ponchada"),
                 ex("El tanque está vacío; necesito echar gasolina.", "The tank is empty; I need to put gas in.", "vacío"),
                 ex("El motor no funciona. Necesito una grúa.", "The engine doesn’t work. I need a tow truck.", "grúa"),
                 ex("Llame al servicio de grúa, por favor.", "Call the tow truck service, please.", "Llame"),
                 ex("Frene con cuidado en la curva.", "Brake carefully at the curve.", "Frene"),
             ]),
    ],
    exercises=[
        F("Tengo una llanta ___ y no tengo llanta de repuesto.", "ponchada", ["ponchado", "ponchadas", "ponchados"], "Llanta is feminine singular.", tr="I have a flat tire and I don’t have a spare."),
        F("El tanque está ___; necesito echar gasolina.", "vacío", ["lleno", "limpio", "caliente"], "Needing gas means the tank is empty.", tr="The tank is empty; I need to put gas in."),
        F("Señor, ___ al servicio de grúa, por favor.", "llame", ["llama", "llamo", "llamen"], "Usted command of llamar.", tr="Sir, call the tow truck service, please.", lemma="llamar:usted:cmd"),
        F("Señora, ___ con cuidado en la curva.", "frene", ["frena", "freno", "frenen"], "Usted command of frenar.", tr="Ma’am, brake carefully at the curve.", lemma="frenar:usted:cmd"),
        F("Señor, ___ la llanta, por favor.", "cambie", ["cambia", "cambio", "cambien"], "Usted command of cambiar.", tr="Sir, change the tire, please.", lemma="cambiar:usted:cmd"),
        M("What is “una grúa”?", "a tow truck", ["a flat tire", "a traffic light", "a gas station"], "Grúa = tow truck."),
        M("What does “echar gasolina” mean?", "to put gas in the car", ["to throw gasoline away", "to buy a car", "to drive fast"], "Echar = to put in."),
        M("What is “la llanta de repuesto”?", "the spare tire", ["the flat tire", "the steering wheel", "the horn"], "Repuesto = spare."),
        M("What does “El motor no funciona” mean?", "The engine doesn’t work.", ["The engine is new.", "The engine is loud.", "The engine is for sale."], "Funcionar = to work."),
    ],
    verify=vpc("llamar", "llame", "llamen") + vpc("frenar", "frene", "frenen") + vpc("cambiar", "cambie", "cambien")
           + vpc("echar", "eche", "echen"),
)

# ---------------------------------------------------------------------------- 218
L218 = lesson(
    "Road signs",
    "Conduzca despacio. No estacione aquí. Prohibido el paso.",
    requires=["conducir", "cruzar", "seguir", "llamar", "cuidado", "carretera"],
    cards=[
        card("Signs use commands",
             "Many road signs give formal commands. Prohibido is used for things that are not allowed: Prohibido el "
             "paso means “No entry”.",
             tables=[table(["Señal", "English"],
                           [["Conduzca despacio. Curva ciega.", "Drive slowly. Blind curve."],
                            ["No estacione su coche aquí.", "Do not park your car here."],
                            ["Cruce la calle con cuidado.", "Cross the street carefully."],
                            ["No doble a la derecha.", "Do not turn right."],
                            ["Siga derecho en la carretera.", "Continue straight on the highway."],
                            ["No cruce. Prohibido el paso.", "Do not cross. No entry."],
                            ["Llame para servicio de grúa.", "Call for tow truck service."],
                            ["Doble a la izquierda.", "Turn left."]],
                           say=[0])]),
        card("Reading the commands",
             "Notice the patterns: conducir → conduzca, estacionar → estacione, doblar → doble, cruzar → cruce, "
             "seguir → siga, llamar → llame.",
             examples=[
                 ex("Conduzca despacio en la ciudad.", "Drive slowly in the city.", "Conduzca"),
                 ex("No estacione frente a la puerta.", "Do not park in front of the door.", "No estacione"),
                 ex("Prohibido el paso a los peatones.", "No entry for pedestrians.", "Prohibido"),
             ]),
    ],
    exercises=[
        F("Curva ciega: ___ despacio.", "conduzca", ["conduce", "conduzco", "conducen"], "Conducir → conduzco → conduzca.", tr="Blind curve: drive slowly.", lemma="conducir:usted:cmd"),
        F("No ___ su coche aquí.", "estacione", ["estaciona", "estaciono", "estacionen"], "Usted command of estacionar.", tr="Do not park your car here.", lemma="estacionar:usted:cmd"),
        F("Señor, ___ la calle con cuidado.", "Cruce", ["Cruza", "Cruzo", "Crucen"], "Usted command of cruzar.", tr="Sir, cross the street carefully.", lemma="cruzar:usted:cmd"),
        F("No ___ a la derecha.", "doble", ["dobla", "doblo", "doblen"], "Usted command of doblar.", tr="Do not turn right.", lemma="doblar:usted:cmd"),
        F("Señor, ___ derecho en la carretera.", "Siga", ["Sigue", "Sigo", "Sigan"], "Seguir → siga.", tr="Sir, continue straight on the highway.", lemma="seguir:usted:cmd"),
        M("What does “Prohibido el paso” mean?", "No entry", ["Free passage", "Pass slowly", "Pay here"], "Prohibido = forbidden."),
        M("What does “Curva ciega” mean?", "Blind curve", ["Blind driver", "Sharp turn right", "Bus lane"], "Ciega = blind."),
        M("What does “Conduzca despacio” tell you to do?", "drive slowly", ["drive fast", "stop the car", "park here"], "Despacio = slowly."),
        M("What is the usted command of “estacionar”?", "estacione", ["estaciona", "estacionar", "estacionen"], "-ar → -e."),
    ],
    verify=vpc("conducir", "conduzca", "conduzcan") + vpc("estacionar", "estacione", "estacionen") + vpc("cruzar", "cruce", "crucen")
           + vpc("seguir", "siga", "sigan"),
)

# ---------------------------------------------------------------------------- 219
L219 = lesson(
    "Getting a passport: step by step",
    "Primero, llene la solicitud. Después, pague la cuota.",
    requires=["pasaporte", "solicitar", "llenar", "presentar", "pagar", "foto", "formulario", "identificación", "cuota", "esperar"],
    cards=[
        card("Sequence words",
             "When you explain a procedure, use sequence words and formal commands: primero, segundo, después, "
             "entonces, por último.",
             tables=[table(["Paso", "Instrucción"],
                           [["Primero", "Llene la solicitud."],
                            ["Segundo", "Presente su acta de nacimiento y una identificación."],
                            ["Después", "Pague la cuota en el banco."],
                            ["Entonces", "Tome una foto reciente."],
                            ["Por último", "Espere su pasaporte."]],
                           say=[0, 1])]),
        card("Words you need",
             "La solicitud (or el formulario) is the application form. La cuota is the fee, and el comprobante is the "
             "receipt. Solicitar means to apply for.",
             examples=[
                 ex("Para solicitar el pasaporte, llene el formulario.", "To apply for the passport, fill out the form.", "llene"),
                 ex("Presente su acta de nacimiento en la oficina.", "Present your birth certificate at the office.", "Presente"),
                 ex("Pague la cuota y guarde el comprobante.", "Pay the fee and keep the receipt.", "Pague"),
                 ex("Por último, espere su pasaporte en casa.", "Finally, wait for your passport at home.", "Por último"),
             ]),
    ],
    exercises=[
        F("Primero, ___ la solicitud con letra clara.", "llene", ["llena", "lleno", "llenen"], "Usted command of llenar.", tr="First, fill out the application in clear handwriting.", lemma="llenar:usted:cmd"),
        F("Segundo, ___ su acta de nacimiento.", "presente", ["presenta", "presento", "presenten"], "Usted command of presentar.", tr="Second, present your birth certificate.", lemma="presentar:usted:cmd"),
        F("Después, ___ la cuota en el banco.", "pague", ["paga", "pago", "paguen"], "Pagar → pague (g → gu).", tr="Then pay the fee at the bank.", lemma="pagar:usted:cmd"),
        F("Entonces, ___ una foto reciente.", "tome", ["toma", "tomo", "tomen"], "Usted command of tomar.", tr="Then take a recent photo.", lemma="tomar:usted:cmd"),
        F("Por último, ___ su pasaporte en casa.", "espere", ["espera", "espero", "esperen"], "Usted command of esperar.", tr="Finally, wait for your passport at home.", lemma="esperar:usted:cmd"),
        M("Which word begins the list of steps?", "Primero", ["Por último", "Después", "Entonces"], "Primero = first."),
        M("What is “la cuota”?", "the fee", ["the photo", "the application", "the passport"], "Cuota = fee."),
        M("What does “solicitar un pasaporte” mean?", "to apply for a passport", ["to lose a passport", "to renew a hotel", "to sell a passport"], "Solicitar = to apply for."),
        M("Which word means “finally, as a last step”?", "Por último", ["Primero", "Segundo", "Entonces"], "Por último = lastly."),
    ],
    verify=vpc("llenar", "llene", "llenen") + vpc("presentar", "presente", "presenten") + vpc("pagar", "pague", "paguen")
           + vpc("tomar", "tome", "tomen") + vpc("esperar", "espere", "esperen"),
)

# ---------------------------------------------------------------------------- 220
L220 = lesson(
    "Advice for traveling abroad",
    "Revise su pasaporte. Compre un seguro de viaje.",
    requires=["pasaporte", "visa", "consulado", "doctor", "vacuna", "seguro", "viaje", "ropa", "dinero", "banco", "efectivo"],
    cards=[
        card("Before you go",
             "A travel blog gives advice with formal commands. Here is a short list for someone visiting another country.",
             tables=[table(["Consejo", "English"],
                           [["Revise su pasaporte.", "Check your passport."],
                            ["Pregunte en el consulado si necesita visa.", "Ask at the consulate whether you need a visa."],
                            ["Hable con su doctor sobre las vacunas.", "Talk to your doctor about vaccines."],
                            ["Compre un seguro de viaje.", "Buy travel insurance."],
                            ["Lleve ropa adecuada para el clima.", "Take clothes suited to the weather."],
                            ["No olvide su cámara.", "Don’t forget your camera."]],
                           say=[0])]),
        card("Once you arrive",
             "Keep your documents safe and handle money wisely.",
             examples=[
                 ex("Escriba la dirección de su hotel.", "Write down the address of your hotel.", "Escriba"),
                 ex("No lleve mucho dinero en efectivo.", "Don’t carry a lot of cash.", "No lleve"),
                 ex("Cambie su dinero en el banco.", "Exchange your money at the bank.", "Cambie"),
                 ex("Deje sus documentos importantes en el hotel.", "Leave your important documents at the hotel.", "Deje"),
             ]),
    ],
    exercises=[
        F("Antes del viaje, ___ su pasaporte.", "revise", ["revisa", "reviso", "revisen"], "Usted command of revisar.", tr="Before the trip, check your passport.", lemma="revisar:usted:cmd"),
        F("___ un seguro de viaje.", "Compre", ["Compra", "Compro", "Compren"], "Usted command of comprar.", tr="Buy travel insurance.", lemma="comprar:usted:cmd"),
        F("___ ropa adecuada para el clima.", "Lleve", ["Lleva", "Llevo", "Lleven"], "Usted command of llevar.", tr="Take clothes suited to the weather.", lemma="llevar:usted:cmd"),
        F("No ___ mucho dinero en efectivo.", "lleve", ["lleva", "llevo", "lleven"], "Negative usted command of llevar.", tr="Don’t carry a lot of cash.", lemma="llevar:usted:cmd"),
        F("___ su dinero en el banco.", "Cambie", ["Cambia", "Cambio", "Cambien"], "Usted command of cambiar.", tr="Exchange your money at the bank.", lemma="cambiar:usted:cmd"),
        M("Where can you ask whether you need a visa?", "en el consulado", ["en la gasolinera", "en el mercado", "en la cocina"], "Consulado = consulate."),
        M("What does “No olvide su cámara” mean?", "Don’t forget your camera.", ["I forgot my camera.", "Buy a camera.", "Your camera is lost."], "No + usted command."),
        M("What is “un seguro de viaje”?", "travel insurance", ["a travel agency", "a safe place", "a ticket office"], "Seguro = insurance."),
        M("Which sentence is a polite piece of advice for one person?", "Hable con su doctor.", ["Hablen con su doctor.", "Habla con su doctor.", "Hablar su doctor."], "Usted command: hable."),
    ],
    verify=vpc("revisar", "revise", "revisen") + vpc("comprar", "compre", "compren") + vpc("llevar", "lleve", "lleven")
           + vpc("cambiar", "cambie", "cambien"),
)

# ---------------------------------------------------------------------------- 221
L221 = lesson(
    "Review: lodging, the preterite and commands",
    "Pidieron, busqué, durmió · Siga, doble, no fume",
    requires=["pedir", "buscar", "dormir", "seguir"],
    cards=[
        card("The preterite patterns",
             "Regular: habló, comió, vivió. Irregular stems: estuve, puse, supe, quise, anduve, conduje, hice, vine, dije, "
             "traje. Fui for both ser and ir. Spelling changes in the yo form: busqué, llegué, empecé. Y-change: cayó, "
             "leyó, oyeron. Stem changes in -ir verbs (él and ellos only): pidió, durmieron.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["irregular", "puse, supe, quise"],
                            ["cambio ortográfico", "busqué, llegué, empecé"],
                            ["vocal y", "cayó, leyó, oyeron"],
                            ["cambio de raíz", "pidió, durmieron, sirvió"]],
                           say=[1])]),
        card("Formal commands",
             "Take the yo form, drop -o, add the opposite vowel (-e / -en for -ar; -a / -an for -er and -ir). Keep the "
             "stem change and the irregular yo form. Dar, ir, ser, estar and saber are irregular. Put no in front for "
             "a negative command.",
             examples=[
                 ex("Pase, siga derecho y doble a la izquierda.", "Go through, continue straight and turn left.", "doble"),
                 ex("Pague la cuota y espere su pasaporte.", "Pay the fee and wait for your passport.", "Pague"),
                 ex("Señores, no fumen en el hotel.", "Gentlemen, don’t smoke in the hotel.", "no fumen"),
             ]),
    ],
    exercises=[
        F("Anoche mis padres ___ el hotel con vista al mar.", "prefirieron", ["prefirió", "preferí", "prefieren"], "Ellos → prefirieron.", tr="Last night my parents preferred the hotel with an ocean view.", lemma="preferir:ellos:pret"),
        F("Ayer yo ___ mi llave en el baño.", "busqué", ["buscó", "busco", "buscaron"], "Yo → busqué.", tr="Yesterday I looked for my key in the bathroom.", lemma="buscar:yo:pret"),
        F("Anoche el huésped ___ muy bien en la pensión.", "durmió", ["dormió", "duerme", "dormí"], "Él → durmió.", tr="Last night the guest slept very well at the guesthouse.", lemma="dormir:él:pret"),
        F("Mi padre ___ el coche por la carretera.", "condujo", ["conduje", "conducen", "condujeron"], "Él → condujo.", tr="My father drove the car along the highway.", lemma="conducir:él:pret"),
        F("Ellos ___ que el hotel estaba lleno.", "supieron", ["supo", "supe", "saben"], "Ellos → supieron (found out).", tr="They found out that the hotel was full.", lemma="saber:ellos:pret"),
        F("Señor, ___ derecho y doble a la izquierda.", "siga", ["sigue", "sigo", "sigan"], "Usted command of seguir.", tr="Sir, continue straight and turn left.", lemma="seguir:usted:cmd"),
        F("Señores, no ___ en la habitación.", "fumen", ["fuman", "fume", "fumar"], "Ustedes, negative: no fumen.", tr="Gentlemen, don’t smoke in the room.", lemma="fumar:ustedes:cmd"),
        F("Señora, ___ la llave a la recepcionista.", "dé", ["da", "doy", "den"], "Dar → dé.", tr="Ma’am, give the key to the receptionist.", lemma="dar:usted:cmd"),
        M("Which is the correct yo preterite of “llegar”?", "llegué", ["llegé", "llegó", "llego"], "G → gu before é."),
        M("What does “¿Qué pasó?” mean?", "It asks what happened", ["It asks what is happening", "It asks what you passed", "It asks what you spent"], "Pasar = to happen."),
        M("What is a flat tire?", "una llanta ponchada", ["un tanque vacío", "una grúa", "una bocina"], "Llanta ponchada = flat tire."),
        M("Which sign means “No entry”?", "Prohibido el paso", ["Conduzca despacio", "Siga derecho", "Curva ciega"], "Prohibido = forbidden."),
    ],
    verify=vpp("preferir", "preferí", "preferiste", "prefirió", "preferimos", "preferisteis", "prefirieron"),
)
UNIT = unit("El hospedaje", [L201, L202, L203, L204, L205, L206, L207, L208, L209, L210, L211, L212, L213, L214, L215, L216, L217, L218, L219, L220, L221])

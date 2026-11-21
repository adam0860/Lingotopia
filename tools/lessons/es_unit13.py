"""Unit 13: travel and transportation, irregular preterites, hace, double object pronouns (textbook Chapter 13)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 180
L180 = lesson(
    "At the airport",
    "Facturo el equipaje. El avión despega. El avión aterriza.",
    requires=["aeropuerto", "vuelo", "avión", "maleta", "pasaporte", "tarjeta", "puerta", "asiento", "cinturón", "demora", "escala", "llegar", "esperar"],
    cards=[
        card("Airport words",
             "Learn the nouns with their articles. Many travel words are masculine (el vuelo, el avión, el pasaporte) "
             "and a few are feminine (la maleta, la aduana, la aerolínea).",
             tables=[table(["Palabra", "English"],
                           [["el aeropuerto", "airport"],
                            ["el vuelo", "flight"],
                            ["la aerolínea", "airline"],
                            ["el mostrador", "counter, desk"],
                            ["el equipaje · la maleta", "luggage · suitcase"],
                            ["la tarjeta de embarque", "boarding pass"],
                            ["la puerta de embarque", "boarding gate"],
                            ["la aduana", "customs"],
                            ["el asiento", "seat"],
                            ["el cinturón", "seat belt, belt"],
                            ["la demora", "delay"],
                            ["la escala", "stopover, layover"]],
                           say=[0])]),
        card("From home to the destination",
             "Here is the trip in order, told in the first person. Notice the verbs: llegar, hacer cola, facturar, "
             "pasar, esperar, subir, abrocharse, despegar, aterrizar, bajar, recoger.",
             examples=[
                 ex("Llego al aeropuerto y hago cola.", "I arrive at the airport and stand in line.", "hago cola"),
                 ex("Facturo el equipaje en el mostrador de la aerolínea.", "I check my luggage at the airline counter.", "Facturo"),
                 ex("Paso por el control de seguridad y espero en la puerta de embarque.", "I go through security and wait at the boarding gate.", "espero"),
                 ex("Subo al avión y me abrocho el cinturón.", "I board the plane and fasten my seat belt.", "me abrocho"),
                 ex("El avión despega y, horas después, aterriza.", "The plane takes off and, hours later, lands.", "despega"),
                 ex("Bajo del avión, recojo el equipaje y paso por la aduana.", "I get off the plane, pick up my luggage and go through customs.", "recojo"),
             ]),
    ],
    exercises=[
        F("Primero llego al aeropuerto; después ___ el equipaje.", "facturo", ["facturas", "factura", "facturan"], "Yo → facturo.", tr="First I arrive at the airport; then I check my luggage.", lemma="facturar:yo"),
        F("El avión ___ a las ocho y vuela a Lima.", "despega", ["despegan", "despegas", "despego"], "El avión → él: despega.", tr="The plane takes off at eight and flies to Lima.", lemma="despegar:él"),
        F("El avión ___ en Lima a las diez.", "aterriza", ["aterrizan", "aterrizas", "aterrizo"], "El avión → él: aterriza.", tr="The plane lands in Lima at ten.", lemma="aterrizar:él"),
        F("Antes de despegar, yo me ___ el cinturón.", "abrocho", ["abrochas", "abrocha", "abrochan"], "Me → yo: abrocho.", tr="Before takeoff, I fasten my seat belt.", lemma="abrochar:yo"),
        F("Hay una ___ de dos horas; el vuelo sale tarde.", "demora", ["escala", "puerta", "maleta"], "A delay makes a flight late.", tr="There is a two-hour delay; the flight leaves late."),
        F("Subo al avión con mi tarjeta de ___.", "embarque", ["cuenta", "tarea", "comida"], "Tarjeta de embarque = boarding pass.", tr="I board the plane with my boarding pass."),
        M("Where do you check your luggage?", "at the airline counter", ["at customs", "at the boarding gate", "on the plane"], "Facturo el equipaje en el mostrador de la aerolínea."),
        M("What does “la puerta de embarque” mean?", "the boarding gate", ["the front door", "the exit to the street", "the ticket office"], "Embarque = boarding."),
        M("Which sentence comes right after “El avión despega”?", "El avión aterriza.", ["Llego al aeropuerto.", "Facturo el equipaje.", "Hago cola."], "Take off, then land."),
    ],
    verify=vp("facturar", "facturo", "facturas", "factura", "facturamos", "facturáis", "facturan")
           + vp("despegar", "despego", "despegas", "despega", "despegamos", "despegáis", "despegan")
           + vp("aterrizar", "aterrizo", "aterrizas", "aterriza", "aterrizamos", "aterrizáis", "aterrizan")
           + vp("abrochar", "abrocho", "abrochas", "abrocha", "abrochamos", "abrocháis", "abrochan"),
)

# ---------------------------------------------------------------------------- 181
L181 = lesson(
    "Getting ready for a trip",
    "Tengo que sacar el pasaporte y hacer la maleta.",
    requires=["viaje", "viajar", "hotel", "pasaje", "maleta", "pasaporte", "agencia", "ida", "vuelta", "tener", "hacer"],
    cards=[
        card("What to do before you go",
             "Most travel preparations are verbs in the infinitive. After tener que, ir a, querer and necesitar, the "
             "infinitive stays the same: Tengo que sacar el pasaporte.",
             tables=[table(["Antes del viaje", "English"],
                           [["hacer la maleta", "to pack the suitcase"],
                            ["sacar el pasaporte", "to get the passport"],
                            ["ir a una agencia de viajes", "to go to a travel agency"],
                            ["comprar los pasajes de ida y vuelta", "to buy round-trip tickets"],
                            ["reservar el hotel", "to reserve the hotel"],
                            ["buscar alojamiento", "to look for lodging"],
                            ["planificar el recorrido", "to plan the route, the tour"],
                            ["comprar zapatos cómodos", "to buy comfortable shoes"]],
                           say=[0])]),
        card("Talking about your plans",
             "Un pasaje de ida es a one-way ticket; de ida y vuelta is round trip. Alojamiento means lodging "
             "(a hotel, a hostel, a room).",
             examples=[
                 ex("Tengo que sacar el pasaporte antes del viaje.", "I have to get my passport before the trip.", "sacar"),
                 ex("Voy a comprar los pasajes de ida y vuelta.", "I am going to buy round-trip tickets.", "de ida y vuelta"),
                 ex("Necesitamos reservar el hotel.", "We need to reserve the hotel.", "reservar"),
                 ex("Quiero planificar el recorrido por la ciudad.", "I want to plan the tour of the city.", "planificar"),
                 ex("Mi hermana va a una agencia de viajes hoy.", "My sister is going to a travel agency today.", "agencia de viajes"),
             ]),
    ],
    exercises=[
        F("Tengo que ___ el pasaporte antes del viaje.", "sacar", ["saco", "saca", "sacando"], "Tener que + infinitive.", tr="I have to get the passport before the trip."),
        F("Mi ropa está en la ___ para el viaje.", "maleta", ["puerta", "tienda", "cocina"], "Clothes for a trip go in a suitcase.", tr="My clothes are in the suitcase for the trip."),
        F("Quiero un pasaje de ida y ___.", "vuelta", ["cuenta", "mesa", "hora"], "Ida y vuelta = round trip.", tr="I want a round-trip ticket."),
        F("Nosotros necesitamos ___ el hotel.", "reservar", ["reservo", "reservamos", "reservan"], "Necesitar + infinitive.", tr="We need to reserve the hotel."),
        F("Mis padres van a ___ el recorrido por la ciudad.", "planificar", ["planifican", "planifico", "planificamos"], "Ir a + infinitive.", tr="My parents are going to plan the tour of the city."),
        M("What does “hacer la maleta” mean?", "to pack the suitcase", ["to buy a suitcase", "to lose the luggage", "to open the door"], "Hacer la maleta = to pack."),
        M("What does “un pasaje de ida” mean?", "a one-way ticket", ["a round-trip ticket", "a return ticket only", "a bus"], "Ida = going."),
        M("Where can you buy tickets and book hotels for a trip?", "en una agencia de viajes", ["en una panadería", "en una gasolinera", "en un restaurante"], "Agencia de viajes = travel agency."),
        M("Which sentence is correct?", "Voy a buscar alojamiento.", ["Voy buscar alojamiento.", "Voy a busco alojamiento.", "Voy a buscando alojamiento."], "Ir a + infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 182
L182 = lesson(
    "Buying a bus or train ticket",
    "¿A qué hora sale el bus? ¿Cuánto dura el viaje?",
    requires=["bus", "autobús", "tren", "metro", "taxi", "boleto", "salir", "durar", "costar", "cambiar", "poder", "precio", "terminal", "estación"],
    cards=[
        card("Questions at the ticket window",
             "These questions work at any bus station or train station. Practice them aloud.",
             tables=[table(["Pregunta", "Una respuesta"],
                           [["¿Hay buses para Tacna hoy?", "Sí, hay uno a las ocho."],
                            ["¿Cuánto cuesta un boleto?", "Cuesta veinte soles."],
                            ["¿A qué hora sale el bus?", "Sale a las nueve y media."],
                            ["¿Cuánto dura el viaje?", "Dura cuatro horas."],
                            ["¿Tengo que cambiar de bus?", "No, es directo."],
                            ["¿Me puede dar dos boletos?", "Sí, aquí tiene."]],
                           say=[0, 1])]),
        card("Words for transport",
             "The generic words are el autobús, el tren, el metro and el taxi. Many places have their own word for bus: "
             "el camión (Mexico), la micro (Chile), la guagua (the Caribbean), el bus (Central America). The subway is "
             "el metro (Mexico, Spain) and el subte (Argentina). Boleto de ida is one-way; boleto de ida y vuelta is "
             "round trip.",
             examples=[
                 ex("Quiero un boleto de ida y vuelta, por favor.", "I want a round-trip ticket, please.", "ida y vuelta"),
                 ex("El tren sale de la estación a las ocho.", "The train leaves the station at eight.", "sale"),
                 ex("En Buenos Aires uso el subte para ir al trabajo.", "In Buenos Aires I use the subway to go to work.", "subte"),
                 ex("El viaje en tren dura tres horas.", "The train trip takes three hours.", "dura"),
             ]),
    ],
    exercises=[
        F("¿A qué hora ___ el bus?", "sale", ["salen", "salgo", "sales"], "El bus → él: sale.", tr="At what time does the bus leave?", lemma="salir:él"),
        F("¿Cuánto ___ el viaje?", "dura", ["duran", "duro", "duras"], "El viaje → él: dura.", tr="How long does the trip last?", lemma="durar:él"),
        F("¿Cuánto ___ un boleto?", "cuesta", ["cuestan", "costó", "cuesto"], "Un boleto → él: cuesta.", tr="How much does a ticket cost?", lemma="costar:él"),
        F("Señor, ¿me ___ dar dos boletos?", "puede", ["puedo", "pueden", "puedes"], "Usted → puede.", tr="Sir, can you give me two tickets?", lemma="poder:usted"),
        F("¿Tengo que ___ de bus en la terminal?", "cambiar", ["cambio", "cambia", "cambiando"], "Tener que + infinitive.", tr="Do I have to change buses at the terminal?"),
        M("What does “boleto de ida y vuelta” mean?", "round-trip ticket", ["one-way ticket", "bus station", "ticket price"], "Ida y vuelta = going and returning."),
        M("What does “¿Cuánto dura el viaje?” ask?", "how long the trip lasts", ["how much the ticket costs", "what time the bus leaves", "where the station is"], "Durar = to last."),
        M("Which word means “subway” in Argentina?", "el subte", ["el camión", "la micro", "la guagua"], "Subte is the Argentine word."),
        M("What does “¿Tengo que cambiar de bus?” ask?", "whether you must change buses", ["whether the bus is full", "where the bus is", "how much the bus costs"], "Cambiar de bus = to change buses."),
    ],
    verify=vp("salir", "salgo", "sales", "sale", "salimos", "salís", "salen")
           + vp("durar", "duro", "duras", "dura", "duramos", "duráis", "duran"),
)

# ---------------------------------------------------------------------------- 183
L183 = lesson(
    "Where is it? Quedar",
    "¿Dónde queda la estación? Queda a un kilómetro.",
    requires=["quedar", "estación", "hotel", "aeropuerto", "cerca", "lejos", "kilómetro", "hora", "minuto", "aquí"],
    cards=[
        card("Quedar = to be located",
             "Quedar is an all-purpose verb. You already know it for staying and for how clothes fit. It is also used "
             "like estar to say where a place is: ¿Dónde queda Veracruz? Veracruz queda en México.",
             examples=[
                 ex("¿Dónde queda la estación?", "Where is the station?", "queda"),
                 ex("La estación queda en el centro.", "The station is downtown.", "queda"),
                 ex("Los hoteles quedan cerca del aeropuerto.", "The hotels are near the airport.", "quedan"),
             ]),
        card("Quedar a + distance",
             "To say how far away a place is, use quedar a + a unit of time or distance. The unit can be hours, minutes, "
             "kilómetros or cuadras (blocks).",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Dónde queda Santa Cruz?", "Queda a una hora de aquí."],
                            ["¿Está lejos la estación?", "No, queda a un kilómetro."],
                            ["¿Está lejos el hotel?", "No, queda a diez minutos."],
                            ["¿Dónde queda el aeropuerto?", "Queda lejos del centro."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("¿Dónde ___ la estación de tren?", "queda", ["quedan", "quedo", "quedas"], "La estación → ella: queda.", tr="Where is the train station?", lemma="quedar:ella"),
        F("La estación ___ a un kilómetro de aquí.", "queda", ["quedan", "quedo", "quedamos"], "Singular subject → queda.", tr="The station is one kilometer from here.", lemma="quedar:ella"),
        F("Los hoteles ___ cerca del aeropuerto.", "quedan", ["queda", "quedo", "quedas"], "Plural subject → quedan.", tr="The hotels are near the airport.", lemma="quedar:ellos"),
        F("Santa Cruz queda a una ___ de aquí.", "hora", ["tarjeta", "maleta", "cuenta"], "A unit of time: una hora.", tr="Santa Cruz is an hour from here."),
        F("El aeropuerto no queda cerca; queda ___ del centro.", "lejos", ["cerca", "aquí", "ahora"], "Lejos = far.", tr="The airport is not near; it is far from downtown."),
        M("What does “¿Dónde queda Veracruz?” ask?", "where Veracruz is", ["when Veracruz closes", "who lives in Veracruz", "how big Veracruz is"], "Quedar = to be located."),
        M("What does “Queda a diez minutos” mean?", "It is ten minutes away.", ["It stays ten minutes.", "It costs ten pesos.", "It leaves in ten minutes."], "Quedar a + time = distance."),
        M("Which sentence says the hotel is a kilometer away?", "El hotel queda a un kilómetro.", ["El hotel queda un kilómetro de.", "El hotel quedan a un kilómetro.", "El hotel queda en un kilómetro de."], "Quedar a + distance."),
        M("Which verb can replace “quedar” in “¿Dónde queda la estación?”", "estar", ["tener", "hacer", "salir"], "¿Dónde está la estación? means the same."),
    ],
    verify=vp("quedar", "quedo", "quedas", "queda", "quedamos", "quedáis", "quedan"),
)

# ---------------------------------------------------------------------------- 184
L184 = lesson(
    "Streets and traffic",
    "el semáforo, la esquina, la cuadra, el peatón",
    requires=["calle", "carretera", "esquina", "tráfico", "estacionamiento", "carril", "parada", "rojo", "coche", "hora"],
    cards=[
        card("In the street",
             "Cuadra (Latin America) and manzana (Spain) both mean a city block. La hora pico is rush hour.",
             tables=[table(["Palabra", "English"],
                           [["la calle · la carretera", "street · highway"],
                            ["la esquina", "corner"],
                            ["la cuadra · la manzana", "block"],
                            ["el semáforo", "traffic light"],
                            ["la señal de alto", "stop sign"],
                            ["el cruce peatonal", "crosswalk"],
                            ["el peatón", "pedestrian"],
                            ["el carril", "lane"],
                            ["el estacionamiento", "parking lot"],
                            ["la gasolinera", "gas station"],
                            ["el tráfico · la hora pico", "traffic · rush hour"],
                            ["la calle cortada", "closed street"]],
                           say=[0])]),
        card("Traffic jams",
             "A traffic jam has many names: el embotellamiento (Argentina, Mexico, Spain, Uruguay), el atasco "
             "(Spain), el trancón (Colombia), el tapón (Puerto Rico).",
             examples=[
                 ex("Hay mucho tráfico en la hora pico.", "There is a lot of traffic at rush hour.", "tráfico"),
                 ex("El semáforo está en rojo.", "The traffic light is red.", "semáforo"),
                 ex("El peatón cruza la calle por el cruce peatonal.", "The pedestrian crosses the street at the crosswalk.", "peatón"),
                 ex("La gasolinera queda en la esquina.", "The gas station is on the corner.", "gasolinera"),
                 ex("Esta calle está cortada; hay que tomar otra.", "This street is closed; we have to take another one.", "cortada"),
             ]),
    ],
    exercises=[
        F("El ___ cruza la calle por el cruce peatonal.", "peatón", ["carril", "semáforo", "tráfico"], "Peatón = pedestrian.", tr="The pedestrian crosses the street at the crosswalk."),
        F("En la hora pico hay mucho ___.", "tráfico", ["peatón", "gasolinera", "esquina"], "Rush hour = lots of traffic.", tr="At rush hour there is a lot of traffic."),
        F("Necesito gasolina; voy a la ___.", "gasolinera", ["esquina", "parada", "mesa"], "A gas station sells gasoline.", tr="I need gasoline; I am going to the gas station."),
        F("El semáforo está en ___; no puedo pasar.", "rojo", ["verde", "cortada", "pico"], "Red means stop.", tr="The traffic light is red; I can’t go."),
        F("La calle está ___; no se puede pasar.", "cortada", ["cortado", "cortadas", "cortados"], "Calle is feminine singular.", tr="The street is closed; you can’t go through."),
        M("What is “la hora pico”?", "rush hour", ["lunch hour", "closing time", "midnight"], "Pico = peak."),
        M("What is “una señal de alto”?", "a stop sign", ["a traffic jam", "a bus stop", "a parking lot"], "Alto = stop."),
        M("What does “la cuadra” mean in Latin America?", "city block", ["street corner", "parking lot", "traffic light"], "Cuadra = block."),
        M("Which word is a traffic jam in Colombia?", "el trancón", ["el semáforo", "el carril", "la esquina"], "Trancón = traffic jam."),
    ],
)

# ---------------------------------------------------------------------------- 185
L185 = lesson(
    "Irregular preterites: estar, tener, poder",
    "estuve, tuve, pude · estuvo, tuvo, pudo",
    requires=["estar", "tener", "poder", "ayer", "anoche", "aeropuerto", "suerte"],
    cards=[
        card("A new stem and special endings",
             "Some common verbs have an irregular stem in the preterite and a special set of endings: -e, -iste, -o, "
             "-imos, -isteis, -ieron. These endings never carry a written accent. Estar becomes estuv-, tener becomes "
             "tuv-, and poder becomes pud-.",
             tables=[table(["", "estar", "tener", "poder"],
                           [["yo", "estuv{e}", "tuv{e}", "pud{e}"],
                            ["tú", "estuv{iste}", "tuv{iste}", "pud{iste}"],
                            ["él · ella · usted", "estuv{o}", "tuv{o}", "pud{o}"],
                            ["nosotros", "estuv{imos}", "tuv{imos}", "pud{imos}"],
                            ["vosotros", "estuv{isteis}", "tuv{isteis}", "pud{isteis}"],
                            ["ellos · ellas · ustedes", "estuv{ieron}", "tuv{ieron}", "pud{ieron}"]],
                           say=[1, 2, 3])]),
        card("Meaning",
             "Tener que keeps its meaning of obligation: Tuve que esperar means “I had to wait”. Poder in the preterite "
             "often means “managed to”: Pude hablar con el piloto means “I was able to talk to the pilot”. "
             "No pude ir means “I could not go (and I didn’t)”.",
             examples=[
                 ex("Ayer estuve en el aeropuerto cinco horas.", "Yesterday I was at the airport for five hours.", "estuve"),
                 ex("Tuvimos que esperar en la puerta de embarque.", "We had to wait at the boarding gate.", "Tuvimos"),
                 ex("Mi hermana no pudo viajar el sábado.", "My sister could not travel on Saturday.", "pudo"),
                 ex("Los pasajeros estuvieron muy tranquilos.", "The passengers were very calm.", "estuvieron"),
                 ex("Tuviste suerte, ¿verdad?", "You were lucky, weren’t you?", "Tuviste"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ en el aeropuerto.", "estuve", ["estuvo", "estoy", "estuviste"], "Yo → estuve.", tr="Yesterday I was at the airport.", lemma="estar:yo:pret"),
        F("Anoche ellos ___ que esperar el vuelo.", "tuvieron", ["tuvo", "tienen", "tuve"], "Ellos → tuvieron.", tr="Last night they had to wait for the flight.", lemma="tener:ellos:pret"),
        F("El sábado nosotros no ___ salir.", "pudimos", ["pudieron", "podemos", "pude"], "Nosotros → pudimos.", tr="On Saturday we could not leave.", lemma="poder:nosotros:pret"),
        F("Ayer ella ___ mucha suerte.", "tuvo", ["tuve", "tiene", "tuvieron"], "Ella → tuvo, no accent.", tr="Yesterday she had a lot of luck.", lemma="tener:ella:pret"),
        F("Anoche, ¿dónde ___ tú?", "estuviste", ["estuve", "estás", "estuvo"], "Tú → estuviste.", tr="Last night, where were you?", lemma="estar:tú:pret"),
        M("Which is the correct yo preterite of “tener”?", "tuve", ["tuvo", "tené", "tenía"], "Tuv- + e."),
        M("Which ending is NOT correct for these irregular preterites?", "-é (with an accent)", ["-e (no accent)", "-iste", "-imos"], "The yo ending is -e, with no accent."),
        M("What does “No pude ir” mean?", "I could not go.", ["I can’t go.", "I don’t want to go.", "I will go."], "Pude = I was able (past)."),
        M("Which is the ellos preterite of “poder”?", "pudieron", ["pueden", "pudo", "podrán"], "Pud- + ieron."),
    ],
    verify=vpp("estar", "estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron")
           + vpp("tener", "tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron")
           + vpp("poder", "pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron"),
)

# ---------------------------------------------------------------------------- 186
L186 = lesson(
    "Irregular preterites: hacer, venir, decir, traer",
    "hice, vine, dije, traje · hizo, dijeron, trajeron · hubo",
    requires=["hacer", "venir", "decir", "traer", "ayer", "anoche", "tráfico"],
    cards=[
        card("More irregular stems",
             "These verbs use the same endings as before (-e, -iste, -o, -imos, -isteis, -ieron). The stems are hic- "
             "(hacer), vin- (venir), dij- (decir) and traj- (traer). Two details: hacer spells the él form hizo (c "
             "becomes z before o, to keep the soft sound), and after j the ending is -eron, not -ieron: dijeron, trajeron.",
             tables=[table(["", "hacer", "venir", "decir", "traer"],
                           [["yo", "hic{e}", "vin{e}", "dij{e}", "traj{e}"],
                            ["tú", "hic{iste}", "vin{iste}", "dij{iste}", "traj{iste}"],
                            ["él · ella · usted", "hiz{o}", "vin{o}", "dij{o}", "traj{o}"],
                            ["nosotros", "hic{imos}", "vin{imos}", "dij{imos}", "traj{imos}"],
                            ["vosotros", "hic{isteis}", "vin{isteis}", "dij{isteis}", "traj{isteis}"],
                            ["ellos · ellas · ustedes", "hic{ieron}", "vin{ieron}", "dij{eron}", "traj{eron}"]],
                           say=[1, 2, 3, 4])]),
        card("Hubo: there was, there were",
             "Hubo is the preterite of haber. It means both “there was” and “there were”, and it never changes.",
             examples=[
                 ex("Ayer hice la maleta.", "Yesterday I packed the suitcase.", "hice"),
                 ex("Mi amiga vino a la fiesta anoche.", "My friend came to the party last night.", "vino"),
                 ex("El camarero trajo la cuenta a la mesa.", "The waiter brought the check to the table.", "trajo"),
                 ex("Los pasajeros dijeron que el vuelo salió tarde.", "The passengers said that the flight left late.", "dijeron"),
                 ex("Anoche hubo mucho tráfico en la carretera.", "Last night there was a lot of traffic on the highway.", "hubo"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ la maleta.", "hice", ["hizo", "hicieron", "hago"], "Yo → hice.", tr="Yesterday I packed the suitcase.", lemma="hacer:yo:pret"),
        F("Mi amiga ___ a la fiesta anoche.", "vino", ["vine", "vienen", "vinieron"], "Ella → vino.", tr="My friend came to the party last night.", lemma="venir:ella:pret"),
        F("El camarero ___ la cuenta a la mesa.", "trajo", ["trajeron", "traje", "trajiste"], "El camarero → él: trajo.", tr="The waiter brought the check to the table.", lemma="traer:él:pret"),
        F("Los pasajeros ___ que el vuelo salió tarde.", "dijeron", ["dijo", "dije", "dijiste"], "Ellos → dijeron (no i).", tr="The passengers said that the flight left late.", lemma="decir:ellos:pret"),
        F("Anoche ___ mucho tráfico en la carretera.", "hubo", ["hay", "hacen", "hicieron"], "Hubo = there was.", tr="Last night there was a lot of traffic on the highway.", lemma="haber:él:pret"),
        M("Why do we write “hizo” and not “hico”?", "c becomes z before o", ["it is an accent rule", "hizo is plural", "it is a typo"], "In the stem hic-, c becomes z before o (hizo) to keep the soft sound."),
        M("Which is the ellos preterite of “decir”?", "dijeron", ["dijo", "dicen", "dirán"], "After j the ending is -eron."),
        M("How do you say “Yesterday we came early”?", "Ayer vinimos temprano.", ["Ayer venimos temprano.", "Ayer vinieron temprano.", "Ayer vine temprano."], "Nosotros → vinimos."),
        M("What does “Hubo una demora” mean?", "There was a delay.", ["There is a delay.", "They had a delay.", "He has a delay."], "Hubo = there was."),
    ],
    verify=vpp("hacer", "hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron")
           + vpp("venir", "vine", "viniste", "vino", "vinimos", "vinisteis", "vinieron")
           + vpp("decir", "dije", "dijiste", "dijo", "dijimos", "dijisteis", "dijeron")
           + vpp("traer", "traje", "trajiste", "trajo", "trajimos", "trajisteis", "trajeron"),
)

# ---------------------------------------------------------------------------- 187
L187 = lesson(
    "Indirect objects: me, te, le, nos, les",
    "Mi padre me regaló un libro. Le mando el boleto.",
    requires=["dar", "decir", "regalar", "mandar", "traer", "comprar", "vender", "prestar", "enseñar", "mostrar"],
    cards=[
        card("To whom? For whom?",
             "The indirect object tells to whom or for whom something is done: Mi padre me regaló un libro (a mí). "
             "Verbs of giving, telling, sending and showing usually have one: dar, decir, regalar, mandar, traer, "
             "comprar, vender, prestar, enseñar, mostrar.",
             tables=[table(["", "Singular", "Plural"],
                           [["to me · to us", "me", "nos"],
                            ["to you (familiar)", "te", "os"],
                            ["to him · to her · to you (formal) · to them · to you all", "le", "les"]],
                           note="Me, te and nos are the same as the direct object pronouns. Only the third person differs: "
                                "le and les instead of lo, la, los, las.",
                           say=[1, 2])]),
        card("Le and les, and clarifying with a",
             "Le can mean to him, to her or to you (usted), and les can mean to them or to you all (ustedes). When it "
             "is not clear, add a + a name or pronoun, even though le or les is already there: Le mando el boleto a mi "
             "madre. The pronoun stays; the a-phrase only clarifies.",
             examples=[
                 ex("Mi padre me regaló un libro.", "My father gave me a book.", "me"),
                 ex("¿Te mando el boleto por correo electrónico?", "Shall I send you the ticket by email?", "Te"),
                 ex("Le dije la verdad a Laura.", "I told Laura the truth.", "Le"),
                 ex("Les enseñamos la ciudad a los turistas.", "We showed the city to the tourists.", "Les"),
                 ex("El camarero nos trajo la cuenta.", "The waiter brought us the check.", "nos"),
                 ex("Le mando el boleto a mi madre.", "I am sending the ticket to my mother.", "a mi madre"),
             ]),
    ],
    exercises=[
        F("Mi padre ___ regaló un libro a mí.", "me", ["te", "le", "nos"], "A mí → me.", tr="My father gave me a book."),
        F("Yo ___ mando el boleto a mi madre.", "le", ["les", "me", "nos"], "A mi madre → le.", tr="I send the ticket to my mother."),
        F("El camarero ___ trajo la cuenta a nosotros.", "nos", ["me", "les", "le"], "A nosotros → nos.", tr="The waiter brought us the check."),
        F("Laura ___ dijo la verdad a sus padres.", "les", ["le", "nos", "te"], "A sus padres → les.", tr="Laura told her parents the truth."),
        F("María, eres mi amiga. ¿___ mando el boleto por correo electrónico?", "Te", ["Le", "Les", "Nos"], "A ti (familiar) → te.", tr="María, you are my friend. Shall I send you the ticket by email?"),
        M("In “Mi padre me regaló un libro”, which word is the indirect object pronoun?", "me", ["Mi", "padre", "un"], "Me = to me."),
        M("Which pronoun means “to him, to her or to you (formal)”?", "le", ["lo", "la", "les"], "Le is the singular indirect object."),
        M("Which pronoun means “to them”?", "les", ["le", "los", "las"], "Les is the plural indirect object."),
        M("Why add “a mi madre” in “Le mando el boleto a mi madre”?", "To make clear who “le” is", ["Because le is wrong", "To make it plural", "To make it past tense"], "A + noun clarifies; le stays."),
    ],
)

# ---------------------------------------------------------------------------- 188
L188 = lesson(
    "The preterite of dar and ver",
    "di, diste, dio, dimos, dieron · vi, viste, vio, vimos, vieron",
    requires=["dar", "ver", "ayer", "museo", "regalo"],
    cards=[
        card("Dar and ver",
             "Dar and ver take the regular -er/-ir endings, but because di, dio, vi and vio have only one "
             "syllable, they take no written accent (not dí, dió, ví, vió). The vosotros and ellos forms are disteis, dieron, visteis, "
             "vieron.",
             tables=[table(["", "dar", "ver"],
                           [["yo", "d{i}", "v{i}"],
                            ["tú", "d{iste}", "v{iste}"],
                            ["él · ella · usted", "d{io}", "v{io}"],
                            ["nosotros", "d{imos}", "v{imos}"],
                            ["vosotros", "d{isteis}", "v{isteis}"],
                            ["ellos · ellas · ustedes", "d{ieron}", "v{ieron}"]],
                           say=[1, 2])]),
        card("In use",
             "Dar is used with indirect objects (dar un regalo a alguien) and in expressions like dar un paseo (to take "
             "a walk). Ver means to see, and it takes the personal a with people.",
             examples=[
                 ex("Le di el regalo a mi madre.", "I gave the gift to my mother.", "di"),
                 ex("Mi hermana me dio un regalo.", "My sister gave me a gift.", "dio"),
                 ex("Dimos un paseo por la ciudad.", "We took a walk around the city.", "Dimos"),
                 ex("Ayer vi la catedral.", "Yesterday I saw the cathedral.", "vi"),
                 ex("Ellos vieron a sus amigos en el aeropuerto.", "They saw their friends at the airport.", "vieron"),
             ]),
    ],
    exercises=[
        F("Mi hermana me ___ un regalo ayer.", "dio", ["di", "dieron", "doy"], "Ella → dio.", tr="My sister gave me a gift yesterday.", lemma="dar:ella:pret"),
        F("Ayer yo ___ la catedral.", "vi", ["vio", "veo", "vieron"], "Yo → vi, no accent.", tr="Yesterday I saw the cathedral.", lemma="ver:yo:pret"),
        F("El sábado nosotros ___ un paseo por la ciudad.", "dimos", ["dieron", "di", "damos"], "Nosotros → dimos.", tr="On Saturday we took a walk around the city.", lemma="dar:nosotros:pret"),
        F("Anoche, ¿tú ___ a tus amigos?", "viste", ["vi", "vio", "ves"], "Tú → viste.", tr="Last night, did you see your friends?", lemma="ver:tú:pret"),
        F("Mis padres nos ___ el dinero para el viaje.", "dieron", ["dio", "dimos", "dan"], "Mis padres → ellos: dieron.", tr="My parents gave us the money for the trip.", lemma="dar:ellos:pret"),
        M("Which is the yo preterite of “ver”?", "vi", ["vio", "veo", "viste"], "Yo → vi."),
        M("Does “dio” have a written accent?", "No — one-syllable forms like dio and vio have none", ["Yes: dió", "Yes: dío", "Only in questions"], "Dio, vio, di, vi are written without an accent."),
        M("What does “Le di el regalo” mean?", "I gave him (her) the gift.", ["He gave me the gift.", "I see the gift.", "They gave her the gift."], "Le = to him, her; di = I gave."),
        M("Which is the ellos preterite of “dar”?", "dieron", ["dio", "dan", "darán"], "D- + ieron."),
    ],
    verify=vpp("dar", "di", "diste", "dio", "dimos", "disteis", "dieron")
           + vpp("ver", "vi", "viste", "vio", "vimos", "visteis", "vieron"),
)

# ---------------------------------------------------------------------------- 189
L189 = lesson(
    "A trip told in the preterite",
    "El verano pasado fui a Perú con mi hermana.",
    requires=["verano", "pasado", "viaje", "hermana", "ir", "ver", "hacer", "estar", "tener", "poder"],
    cards=[
        card("Read the story",
             "Every verb in this story is in the preterite. Find the regular forms (salimos, volamos, vimos, visitamos, comimos) and "
             "the irregular ones (fui, tuve, estuvimos, hicimos, vimos, fue).",
             examples=[
                 ex("El verano pasado fui a Perú con mi hermana.", "Last summer I went to Peru with my sister.", "fui"),
                 ex("Antes de salir, tuve que sacar el pasaporte.", "Before leaving, I had to get my passport.", "tuve"),
                 ex("Salimos de Miami y volamos a Lima. El viaje fue largo.", "We left Miami and flew to Lima. The trip was long.", "fue"),
                 ex("Estuvimos cuatro días en Lima y hicimos muchas cosas.", "We were in Lima for four days and did many things.", "Estuvimos"),
                 ex("Vimos la catedral, visitamos un museo y comimos ceviche.", "We saw the cathedral, visited a museum and ate ceviche.", "Vimos"),
                 ex("Después tomamos un bus a Cusco y tuvimos suerte con el clima.", "Afterwards we took a bus to Cusco and were lucky with the weather.", "tuvimos"),
                 ex("Mi hermana no pudo caminar mucho, pero lo pasamos muy bien.", "My sister could not walk much, but we had a great time.", "pudo"),
             ]),
        card("Useful time words",
             "To tell a story, start with a time marker: el verano pasado, el año pasado, hace dos años, ayer, anoche, "
             "primero, después, luego, por fin. They tell the listener that the preterite is coming.",
             tables=[table(["Expresión", "English"],
                           [["el verano pasado", "last summer"],
                            ["el año pasado", "last year"],
                            ["primero", "first"],
                            ["después · luego", "afterwards · then"],
                            ["por fin", "finally"]],
                           say=[0])]),
    ],
    exercises=[
        F("El verano pasado yo ___ a Perú con mi hermana.", "fui", ["fue", "voy", "fueron"], "Yo → fui.", tr="Last summer I went to Peru with my sister.", lemma="ir:yo:pret"),
        F("Antes de salir, yo ___ que sacar el pasaporte.", "tuve", ["tuvo", "tengo", "tuviste"], "Yo → tuve.", tr="Before leaving, I had to get my passport.", lemma="tener:yo:pret"),
        F("Nosotras ___ cuatro días en Lima.", "estuvimos", ["estuvieron", "estuve", "estamos"], "Nosotras → estuvimos.", tr="We were in Lima for four days.", lemma="estar:nosotros:pret"),
        F("En la ciudad nosotras ___ la catedral.", "vimos", ["vieron", "vi", "vemos"], "Nosotras → vimos.", tr="In the city we saw the cathedral.", lemma="ver:nosotros:pret"),
        F("Mi hermana no ___ caminar mucho.", "pudo", ["pude", "pudieron", "puede"], "Ella → pudo.", tr="My sister could not walk much.", lemma="poder:ella:pret"),
        M("Which phrase tells you the story is in the past?", "el verano pasado", ["todos los días", "mañana", "ahora"], "Pasado = last."),
        M("How did the narrator and her sister get from Lima to Cusco?", "by bus", ["by plane", "by train", "by taxi"], "Tomamos un bus a Cusco."),
        M("Why did the narrator need to take care of her passport before the trip?", "She had to get it.", ["She lost it.", "She sold it.", "She gave it away."], "Tuve que sacar el pasaporte."),
        M("What does “por fin” mean?", "finally", ["first", "never", "again"], "Por fin = at last."),
    ],
)

# ---------------------------------------------------------------------------- 190
L190 = lesson(
    "Hace = ago",
    "Llegué hace una hora. Hace dos años viajé a Lima.",
    requires=["hacer", "llegar", "viajar", "hora", "día", "semana", "mes", "año", "regalar"],
    cards=[
        card("Hace + a period of time",
             "To say how long ago something happened, use the preterite and hace plus a period of time. Hace does not "
             "change, and it can come at the end or at the beginning of the sentence: Llegué hace una hora. Hace una "
             "hora llegué.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Cuándo llegó el vuelo?", "El vuelo llegó hace una hora."],
                            ["¿Cuándo viajaron tus padres a Lima?", "Viajaron hace tres semanas."],
                            ["¿Cuándo se casó su hermana?", "Se casó hace dos años."],
                            ["¿Cuándo compraste el pasaje?", "Compré el pasaje hace un mes."]],
                           say=[0, 1])]),
        card("More examples",
             "The periods of time are plural when more than one: hace un día, hace dos días; hace una semana, hace tres "
             "semanas; hace un mes, hace seis meses; hace un año, hace diez años.",
             examples=[
                 ex("Hace dos días estuve en Lima.", "Two days ago I was in Lima.", "Hace dos días"),
                 ex("Mi hermano llegó hace una hora.", "My brother arrived an hour ago.", "hace una hora"),
                 ex("Hace un año fui a Cusco con mis amigos.", "A year ago I went to Cusco with my friends.", "Hace un año"),
                 ex("Mis amigos me regalaron un libro hace un mes.", "My friends gave me a book a month ago.", "hace un mes"),
             ]),
    ],
    exercises=[
        F("Llegué al aeropuerto ___ una hora.", "hace", ["hacen", "haces", "hago"], "Hace + time = ago.", tr="I arrived at the airport an hour ago.", lemma="hacer:él"),
        F("Mis padres viajaron a Lima ___ tres semanas.", "hace", ["hacen", "haces", "hago"], "Hace never changes.", tr="My parents traveled to Lima three weeks ago.", lemma="hacer:él"),
        F("___ un año fui a Cusco con mis amigos.", "Hace", ["Hacen", "Haces", "Hago"], "Hace at the start of the sentence.", tr="A year ago I went to Cusco with my friends.", lemma="hacer:él"),
        F("Hace dos días ___ en Lima.", "estuve", ["estuvo", "estoy", "estuvieron"], "Yo → estuve; hace + preterite.", tr="Two days ago I was in Lima.", lemma="estar:yo:pret"),
        F("Hace un mes mis amigos me ___ un libro.", "regalaron", ["regala", "regaló", "regalé"], "Mis amigos → regalaron.", tr="A month ago my friends gave me a book.", lemma="regalar:ellos:pret"),
        M("What does “hace tres años” mean?", "three years ago", ["for three years from now", "three years long", "every three years"], "Hace + time = ago."),
        M("How do you say “two days ago”?", "hace dos días", ["dos días hace", "hacen dos días", "por dos días"], "Hace comes first and does not change."),
        M("Which tense follows “hace + time” for something that already happened?", "the preterite", ["the future", "the infinitive", "the command"], "Llegué hace una hora."),
        M("Which sentence means “She got married two years ago”?", "Se casó hace dos años.", ["Se casa hace dos años.", "Se casó hacen dos años.", "Se casará hace dos años."], "Preterite + hace + time."),
    ],
    verify=vpp("llegar", "llegué", "llegaste", "llegó", "llegamos", "llegasteis", "llegaron")
           + vpp("regalar", "regalé", "regalaste", "regaló", "regalamos", "regalasteis", "regalaron")
           + vpp("viajar", "viajé", "viajaste", "viajó", "viajamos", "viajasteis", "viajaron"),
)

# ---------------------------------------------------------------------------- 191
L191 = lesson(
    "Hace que: how long?",
    "¿Cuánto tiempo hace que estudias español?",
    requires=["estudiar", "vivir", "llegar", "terminar", "tiempo", "hora", "mes", "año"],
    cards=[
        card("How long has it been?",
             "The question ¿Cuánto tiempo hace que…? asks how long, and the tense of the verb tells you the meaning. "
             "With the present tense, the action is still going on: Hace dos meses que estudio español (I have been "
             "studying for two months, and I still am). With the preterite, the action is finished: Hace una hora que "
             "llegué (it has been an hour since I arrived).",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Cuánto tiempo hace que estudias español?", "Hace dos meses que estudio español."],
                            ["¿Cuánto tiempo hace que vives aquí?", "Hace un año que vivo aquí."],
                            ["¿Cuánto tiempo hace que llegaste?", "Hace una hora que llegué."],
                            ["¿Cuánto tiempo hace que viajaste a Lima?", "Hace tres años que viajé a Lima."]],
                           say=[0, 1])]),
        card("Present or preterite?",
             "Ask yourself: is it still happening? If yes, use the present. If it already ended, use the preterite.",
             examples=[
                 ex("Hace un año que vivo aquí.", "I have lived here for a year (and I still do).", "vivo"),
                 ex("Hace un año que llegué aquí.", "It has been a year since I arrived here.", "llegué"),
                 ex("¿Cuánto tiempo hace que trabajas en esa empresa?", "How long have you been working at that company?", "trabajas"),
                 ex("Hace dos horas que terminé el trabajo.", "It has been two hours since I finished the work.", "terminé"),
             ]),
    ],
    exercises=[
        F("Todavía vivo aquí: hace un año que ___ aquí.", "vivo", ["viví", "vive", "vivimos"], "Todavía → present.", tr="I still live here: I have lived here for a year.", lemma="vivir:yo"),
        F("Ya terminé: hace una hora que ___ el trabajo.", "terminé", ["termino", "terminó", "terminaron"], "Already finished → preterite.", tr="I’m done: it has been an hour since I finished the work.", lemma="terminar:yo:pret"),
        F("¿Cuánto tiempo hace que estudias español? Hace dos meses que ___ español.", "estudio", ["estudié", "estudia", "estudiaron"], "The question uses the present, so answer in the present.", tr="How long have you been studying Spanish? I have been studying Spanish for two months.", lemma="estudiar:yo"),
        F("¿Cuánto tiempo hace que llegaste? Hace una hora que ___.", "llegué", ["llego", "llegó", "llegaron"], "The question uses the preterite, so answer with it.", tr="How long has it been since you arrived? It has been an hour since I arrived.", lemma="llegar:yo:pret"),
        F("Hace tres años que ___ a Lima, y no vuelvo.", "viajé", ["viajo", "viajó", "viajaron"], "Finished action → preterite.", tr="It has been three years since I traveled to Lima, and I haven’t been back.", lemma="viajar:yo:pret"),
        M("Which sentence says you still live here?", "Hace un año que vivo aquí.", ["Hace un año que viví aquí.", "Hace un año que viviré aquí.", "Hace un año que vivió aquí."], "Present tense = still going on."),
        M("What does “Hace una hora que llegué” mean?", "It has been an hour since I arrived.", ["I have been arriving for an hour.", "I will arrive in an hour.", "I arrive every hour."], "Preterite = the action is over."),
        M("What does “¿Cuánto tiempo hace que vives aquí?” ask?", "how long you have lived here", ["when you will leave", "where you live", "who lives with you"], "Present + hace que = how long so far."),
        M("Which tense do you use when the action is finished?", "the preterite", ["the present", "the infinitive", "the future"], "Hace + time + que + preterite."),
    ],
    verify=vpp("terminar", "terminé", "terminaste", "terminó", "terminamos", "terminasteis", "terminaron"),
)

# ---------------------------------------------------------------------------- 192
L192 = lesson(
    "Two object pronouns together",
    "Mi padre me lo regaló. Yo te los traje.",
    requires=["regalar", "mandar", "traer", "dar", "libro", "foto", "boleto", "bebida"],
    cards=[
        card("Indirect first, direct second",
             "When a sentence has both an indirect and a direct object pronoun, the indirect one always comes first. "
             "A good memory aid is ID: Indirect, then Direct. Ella me dio el libro → Ella me lo dio (she gave it to me).",
             tables=[table(["Con nombres", "Con pronombres"],
                           [["Ella me dio el libro.", "Ella me lo dio."],
                            ["Mi amiga me mandó la foto.", "Mi amiga me la mandó."],
                            ["Yo te traje los boletos.", "Yo te los traje."],
                            ["El camarero nos trajo las bebidas.", "El camarero nos las trajo."]],
                           say=[0, 1])]),
        card("Order: me, te, nos + lo, la, los, las",
             "The first pronoun (me, te, nos) tells you to whom, and the second (lo, la, los, las) tells you what. They "
             "are never separated or reversed.",
             examples=[
                 ex("Mi padre me regaló el viaje. Mi padre me lo regaló.", "My father gave me the trip. My father gave it to me.", "me lo"),
                 ex("Mi hermana te trajo las maletas. Mi hermana te las trajo.", "My sister brought you the suitcases. My sister brought them to you.", "te las"),
                 ex("El taxista nos dio el recibo. El taxista nos lo dio.", "The taxi driver gave us the receipt. The taxi driver gave it to us.", "nos lo"),
             ]),
    ],
    exercises=[
        F("Mi padre me regaló el viaje. Mi padre me ___ regaló.", "lo", ["la", "los", "las"], "Viaje is masculine singular.", tr="My father gave me the trip. My father gave it to me."),
        F("Mi amiga me mandó la foto. Mi amiga me ___ mandó.", "la", ["lo", "los", "las"], "Foto is feminine singular.", tr="My friend sent me the photo. My friend sent it to me."),
        F("Yo te traje los boletos. Yo te ___ traje.", "los", ["lo", "la", "las"], "Boletos is masculine plural.", tr="I brought you the tickets. I brought them to you."),
        F("El camarero nos trajo las bebidas. El camarero nos ___ trajo.", "las", ["lo", "la", "los"], "Bebidas is feminine plural.", tr="The waiter brought us the drinks. The waiter brought them to us."),
        F("Ella me dio el libro. Ella ___ lo dio.", "me", ["te", "le", "nos"], "A mí → me, first.", tr="She gave me the book. She gave it to me."),
        M("Which order is correct?", "Mi padre me lo regaló.", ["Mi padre lo me regaló.", "Mi padre regaló me lo.", "Mi padre me regaló lo."], "Indirect first, direct second."),
        M("What does the memory aid “ID” stand for?", "Indirect, then Direct", ["Identity Document", "In Detail", "Infinitive, Dative"], "Indirect object pronoun before direct."),
        M("What does “Ella me lo dio” mean?", "She gave it to me.", ["She gave me to him.", "I gave it to her.", "She gave it to them."], "Me = to me; lo = it."),
        M("Mi hermana te trajo las maletas. Which sentence replaces “las maletas” correctly?", "Mi hermana te las trajo.", ["Mi hermana las te trajo.", "Mi hermana te lo trajo.", "Mi hermana te les trajo."], "Maletas is feminine plural: las, after te."),
    ],
)

# ---------------------------------------------------------------------------- 193
L193 = lesson(
    "Le and les become se",
    "Se lo di ayer. Se las mandé.",
    requires=["dar", "comprar", "regalar", "mandar", "pasar", "ayer", "boleto"],
    cards=[
        card("Never “le lo”",
             "Spanish does not allow le or les right before lo, la, los or las. In that position le and les both become "
             "se. So there are four possible combinations: se lo, se la, se los, se las.",
             tables=[table(["Con le o les", "Con se"],
                           [["Le di el regalo.", "Se lo di ayer."],
                            ["Le compré una chaqueta.", "Se la compré en la tienda."],
                            ["Le regalé unos zapatos.", "Se los regalé."],
                            ["Les mandé tarjetas de Navidad.", "Se las mandé ayer."]],
                           say=[0, 1])]),
        card("Who is “se”?",
             "Se can mean to him, to her, to you (usted) or to them, so it is often clarified with a + a name or a "
             "pronoun: Se lo di a él. Se los regalé a mi hijo.",
             examples=[
                 ex("Le di el regalo a mi madre. Se lo di ayer.", "I gave the gift to my mother. I gave it to her yesterday.", "Se lo"),
                 ex("Se los regalé a mi hijo.", "I gave them to my son as a gift.", "Se los"),
                 ex("Se la mandé a ustedes por correo.", "I sent it to you all by mail.", "Se la"),
                 ex("Se las pasé a ellos.", "I passed them to them.", "Se las"),
             ]),
    ],
    exercises=[
        F("Le di el regalo a mi madre. ___ lo di ayer.", "Se", ["Le", "Me", "Te"], "Le + lo → se lo.", tr="I gave the gift to my mother. I gave it to her yesterday."),
        F("Le compré una chaqueta a mi hermana. Se ___ compré ayer.", "la", ["lo", "los", "las"], "Chaqueta is feminine singular.", tr="I bought a jacket for my sister. I bought it for her yesterday."),
        F("Les mandé tarjetas a mis amigos. Se ___ mandé ayer.", "las", ["lo", "la", "los"], "Tarjetas is feminine plural.", tr="I sent cards to my friends. I sent them to them yesterday."),
        F("Le regalé unos zapatos a mi hijo. Se ___ regalé por su cumpleaños.", "los", ["lo", "la", "las"], "Zapatos is masculine plural.", tr="I gave my son some shoes. I gave them to him for his birthday."),
        F("Les pasé el boleto a ellos. ___ lo pasé.", "Se", ["Les", "Nos", "Me"], "Les + lo → se lo.", tr="I passed the ticket to them. I passed it to them."),
        M("Why do we say “se lo di” and not “le lo di”?", "le and les become se before lo, la, los, las", ["because se is a verb", "because lo is plural", "because di is irregular"], "Le/les + lo/la/los/las → se."),
        M("What can “Se lo di” mean?", "I gave it to him, her, you or them.", ["I gave it to me.", "He gave it to me.", "We gave it to you."], "Se replaces le or les."),
        M("How can you clarify who “se” is?", "Add a + a name or pronoun", ["Add the word de", "Change lo to los", "Use the future"], "Se lo di a él."),
        M("Which sentence replaces “unos zapatos” correctly?", "Se los regalé.", ["Se lo regalé.", "Le los regalé.", "Los se regalé."], "Zapatos is masculine plural."),
    ],
    verify=vpp("comprar", "compré", "compraste", "compró", "compramos", "comprasteis", "compraron")
           + vpp("mandar", "mandé", "mandaste", "mandó", "mandamos", "mandasteis", "mandaron")
           + vpp("pasar", "pasé", "pasaste", "pasó", "pasamos", "pasasteis", "pasaron"),
)

# ---------------------------------------------------------------------------- 194
L194 = lesson(
    "Where double pronouns go",
    "Se lo voy a dar. Voy a dárselo. No se lo di.",
    requires=["dar", "mandar", "alquilar", "pasar", "ir", "tener", "estar"],
    cards=[
        card("Before the verb, or attached",
             "Double pronouns follow the same placement rules as a single pronoun. They go before the conjugated "
             "verb, or they attach to the end of an infinitive or an -ando form. When you attach them, add a written "
             "accent so the stress stays where it was: dar → dárselo.",
             tables=[table(["Antes del verbo", "Pegados al infinitivo"],
                           [["Nicolás se lo va a alquilar.", "Nicolás va a alquilárselo."],
                            ["Se lo tengo que mandar.", "Tengo que mandárselo."],
                            ["Te lo voy a dar.", "Voy a dártelo."],
                            ["La azafata se la está pasando.", "La azafata está pasándosela."]],
                           say=[0, 1])]),
        card("Negative sentences",
             "In a negative sentence, put no before the first pronoun: ¿Tus padres te compraron el boleto? No, no me lo "
             "compraron. ¿Le pasaste la maleta al empleado? No, no se la pasé.",
             examples=[
                 ex("¿Tus padres te compraron el boleto? No, no me lo compraron.", "Did your parents buy you the ticket? No, they didn’t buy it for me.", "no me lo"),
                 ex("¿Le pasaste la maleta al empleado? No, no se la pasé.", "Did you pass the suitcase to the employee? No, I didn’t pass it to him.", "no se la"),
                 ex("Voy a dárselo mañana.", "I am going to give it to him tomorrow.", "dárselo"),
             ]),
    ],
    exercises=[
        F("Voy a dar el boleto a Laura. Voy a ___.", "dárselo", ["dárselos", "dárselas", "dártelo"], "Boleto → lo; le → se; accent on the a.", tr="I’m going to give the ticket to Laura. I’m going to give it to her."),
        F("Tengo que mandar las fotos a mis padres. Tengo que ___.", "mandárselas", ["mandárselo", "mandárselos", "mandártelas"], "Fotos → las; les → se.", tr="I have to send the photos to my parents. I have to send them to them."),
        F("¿Te compraron el boleto? No, no me ___ compraron.", "lo", ["la", "los", "las"], "Boleto is masculine singular.", tr="Did they buy you the ticket? No, they didn’t buy it for me."),
        F("¿Le pasaste la maleta al empleado? No, no se ___ pasé.", "la", ["lo", "los", "las"], "Maleta is feminine singular.", tr="Did you pass the suitcase to the employee? No, I didn’t pass it to him."),
        F("Nicolás va a alquilar un auto a su hija. Nicolás ___ lo va a alquilar.", "se", ["le", "me", "te"], "Le + lo → se lo.", tr="Nicolás is going to rent a car for his daughter. Nicolás is going to rent it for her."),
        M("Which two sentences both mean “I have to send it to him”?", "Se lo tengo que mandar. · Tengo que mandárselo.", ["Lo se tengo que mandar. · Tengo que mandarselo.", "Se lo tengo mandar que. · Tengo que se lo mandar.", "Le lo tengo que mandar. · Tengo que mandarlese."], "Before the first verb, or attached to the infinitive with an accent."),
        M("Where does “no” go?", "Before the first pronoun: No me lo compraron.", ["After the pronouns: Me lo no compraron.", "At the end: Me lo compraron no.", "Between the pronouns: Me no lo compraron."], "No goes before the pronouns."),
        M("Why does “dárselo” have a written accent?", "To keep the stress on the a", ["Because it is a question", "Because it is plural", "Because se is a verb"], "Adding syllables moves the stress, so the accent keeps it."),
        M("Which is correct?", "Está pasándosela.", ["Está pasandosela.", "Está se la pasando.", "Está pasándolase."], "Attached to -ando with a written accent."),
    ],
)

# ---------------------------------------------------------------------------- 195
L195 = lesson(
    "Gifts: who gave it to whom?",
    "Mi padre me lo regaló. Se la voy a regalar a mi amigo.",
    requires=["regalar", "regalo", "libro", "dar", "comprar", "viaje", "año", "amigo"],
    cards=[
        card("Talking about gifts",
             "Gifts are a perfect place to practice double pronouns. Notice how the question and the answer fit "
             "together: the question uses nouns, and the answer replaces them with pronouns.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Quién te regaló el viaje?", "Mi padre me lo regaló."],
                            ["¿Cuánto tiempo hace que te lo regaló?", "Me lo regaló hace tres años."],
                            ["¿A quién le vas a regalar la mochila?", "Se la voy a regalar a mi amigo."],
                            ["¿Cuándo se la vas a regalar?", "Voy a regalársela en junio."]],
                           say=[0, 1])]),
        card("Gift ideas",
             "Common gifts: un libro, una mochila, unos zapatos, una chaqueta, unos pantalones, una tarjeta, un viaje. "
             "Remember that in the third person, le and les change to se when lo, la, los or las follows.",
             examples=[
                 ex("Mi hermana me dio una chaqueta. Me la dio hace un año.", "My sister gave me a jacket. She gave it to me a year ago.", "Me la dio"),
                 ex("¿Le compraste el libro a tu amiga? Sí, se lo compré ayer.", "Did you buy your friend the book? Yes, I bought it for her yesterday.", "se lo compré"),
                 ex("Mi abuela nos mandó una tarjeta. Nos la mandó por correo.", "My grandmother sent us a card. She sent it to us by mail.", "Nos la mandó"),
                 ex("Voy a regalarle unos zapatos a mi hijo. Voy a regalárselos en junio.", "I am going to give my son some shoes. I am going to give them to him in June.", "regalárselos"),
             ]),
    ],
    exercises=[
        F("¿Quién te regaló el viaje? Mi padre me ___ regaló.", "lo", ["la", "los", "las"], "Viaje is masculine singular.", tr="Who gave you the trip? My father gave it to me."),
        F("¿Cuánto tiempo hace que te lo regaló? Me lo regaló ___ tres años.", "hace", ["hacen", "haces", "hago"], "Hace + time = ago.", tr="How long ago did he give it to you? He gave it to me three years ago.", lemma="hacer:él"),
        F("¿A quién le vas a regalar la mochila? ___ la voy a regalar a mi amigo.", "Se", ["Le", "Me", "Te"], "Le + la → se la.", tr="Whom are you going to give the backpack to? I’m going to give it to my friend."),
        F("Mi hermana me dio una chaqueta. Mi hermana me ___ dio hace un año.", "la", ["lo", "los", "las"], "Chaqueta is feminine singular.", tr="My sister gave me a jacket. My sister gave it to me a year ago."),
        F("¿Le compraste el libro a tu amiga? Sí, se ___ compré ayer.", "lo", ["la", "los", "las"], "Libro is masculine singular.", tr="Did you buy your friend the book? Yes, I bought it for her yesterday."),
        M("What does “Se la voy a regalar a mi amigo” mean?", "I am going to give it to my friend.", ["My friend is going to give it to me.", "I gave it to my friend.", "I am going to buy it for myself."], "Se la = it (feminine) to him."),
        M("Which sentence means the same as “Se lo voy a dar”?", "Voy a dárselo.", ["Voy a darlese.", "Voy dárselo a.", "Se voy a lo dar."], "Attach both pronouns to the infinitive."),
        M("How do you say “My father gave it to me three years ago”?", "Mi padre me lo regaló hace tres años.", ["Mi padre lo me regaló hace tres años.", "Mi padre me regaló lo hace tres años.", "Mi padre me lo regaló hacen tres años."], "ID order, then hace + time."),
        M("Why is “a mi amigo” added after “Se la voy a regalar”?", "To clarify who “se” is", ["Because se is wrong", "To make the sentence past tense", "To make it plural"], "Se can mean him, her, you or them."),
    ],
)

# ---------------------------------------------------------------------------- 196
L196 = lesson(
    "Otro and otra",
    "otro boleto, otra ruta, otros asientos, el otro",
    requires=["otro", "boleto", "ruta", "asiento", "autobús", "maleta", "parada", "querer", "poder"],
    cards=[
        card("Another, other",
             "Otro agrees in gender and number with the noun, whether it is an adjective or stands alone as a pronoun. "
             "Never say un otro: otro already means “another”.",
             tables=[table(["", "Masculino", "Femenino"],
                           [["singular", "otro boleto", "otra ruta"],
                            ["plural", "otros asientos", "otras paradas"]],
                           say=[1, 2])]),
        card("With and without the article",
             "Without an article, otro means “another (one)”. With the article, el otro, la otra, los otros, las otras "
             "mean “the other one(s)”.",
             examples=[
                 ex("¿Me puede vender otro boleto?", "Can you sell me another ticket?", "otro boleto"),
                 ex("Lo siento, no hay otro.", "Sorry, there isn’t another one.", "otro"),
                 ex("Queremos tomar otra ruta.", "We want to take another route.", "otra ruta"),
                 ex("¿Tiene otros asientos? Sí, tenemos otros.", "Do you have other seats? Yes, we have some others.", "otros"),
                 ex("Este autobús es más viejo que el otro.", "This bus is older than the other one.", "el otro"),
                 ex("Esas no son mis maletas; son las otras.", "Those are not my suitcases; they are the other ones.", "las otras"),
             ]),
    ],
    exercises=[
        F("¿Me puede vender ___ boleto?", "otro", ["otra", "otros", "otras"], "Boleto is masculine singular.", tr="Can you sell me another ticket?"),
        F("Queremos tomar ___ ruta.", "otra", ["otro", "otros", "otras"], "Ruta is feminine singular.", tr="We want to take another route."),
        F("¿Tiene otros asientos? Sí, tenemos ___.", "otros", ["otro", "otra", "otras"], "Asientos is masculine plural.", tr="Do you have other seats? Yes, we have some others."),
        F("Este autobús es más viejo que el ___.", "otro", ["otra", "otros", "otras"], "Autobús is masculine singular.", tr="This bus is older than the other one."),
        F("Esas no son mis maletas; son las ___.", "otras", ["otro", "otra", "otros"], "Maletas is feminine plural.", tr="Those are not my suitcases; they are the other ones."),
        M("Which sentence is correct?", "Quiero otro café.", ["Quiero un otro café.", "Quiero otra café.", "Quiero otros café."], "Never un otro."),
        M("What does “el otro” mean?", "the other one", ["another one", "the first one", "some others"], "With the article = the other one."),
        M("What does “otras paradas” mean?", "other stops", ["another stop", "the other stop", "no stops"], "Feminine plural."),
        M("Which sentence means “There is another stop”?", "Hay otra parada.", ["Hay un otra parada.", "Hay otro parada.", "Hay otras parada."], "Parada is feminine singular."),
    ],
)

# ---------------------------------------------------------------------------- 197
L197 = lesson(
    "The impersonal se",
    "Se vende casa. Se habla español. Se prohíbe fumar.",
    requires=["vender", "alquilar", "hablar", "prohibir", "tomar", "necesitar", "ofrecer", "casa", "apartamento"],
    cards=[
        card("Se + verb: nobody in particular",
             "When the subject is “one”, “people” or “you” in general, Spanish uses se and the third person of the "
             "verb. You see it constantly on signs, ads, announcements and instructions. The verb agrees with the "
             "thing: singular noun → singular verb (Se vende casa), plural noun → plural verb (Se venden casas).",
             tables=[table(["Con se", "English"],
                           [["Se vende casa.", "House for sale."],
                            ["Se alquila un apartamento.", "Apartment for rent."],
                            ["Se alquilan habitaciones.", "Rooms for rent."],
                            ["Se habla español aquí.", "Spanish is spoken here."],
                            ["Se prohíbe fumar.", "No smoking."]],
                           say=[0])]),
        card("In everyday talk",
             "The impersonal se also describes customs and general facts: A las cinco de la tarde se toma el té. "
             "¿Cuánta fruta se necesita para una dieta equilibrada?",
             examples=[
                 ex("A las cinco de la tarde se toma el té.", "At five in the afternoon one drinks tea.", "se toma"),
                 ex("En este restaurante se come muy bien.", "In this restaurant you eat very well.", "se come"),
                 ex("¿Cómo se dice “gracias” en inglés?", "How do you say “gracias” in English?", "se dice"),
                 ex("En México se habla español.", "In Mexico Spanish is spoken.", "se habla"),
             ]),
    ],
    exercises=[
        F("Se ___ casa.", "vende", ["venden", "vendo", "vendes"], "Casa is singular.", tr="House for sale.", lemma="vender:él"),
        F("Se ___ habitaciones.", "alquilan", ["alquila", "alquilo", "alquilas"], "Habitaciones is plural.", tr="Rooms for rent.", lemma="alquilar:ellos"),
        F("Se ___ español aquí.", "habla", ["hablan", "hablo", "hablas"], "Español is singular.", tr="Spanish is spoken here.", lemma="hablar:él"),
        F("Se ___ fumar en el aeropuerto.", "prohíbe", ["prohíben", "prohíbo", "prohíbes"], "Prohibir has an accent: prohíbe.", tr="Smoking is prohibited at the airport.", lemma="prohibir:él"),
        F("A las cinco de la tarde se ___ el té.", "toma", ["toman", "tomo", "tomas"], "El té is singular.", tr="At five in the afternoon one drinks tea.", lemma="tomar:él"),
        M("What does “Se alquila un apartamento” mean?", "An apartment is for rent.", ["I rent an apartment.", "They rent apartments.", "He rents an apartment."], "Se + verb = general, unspecified subject."),
        M("Which sentence is correct?", "Se venden zapatos.", ["Se vende zapatos.", "Se vendo zapatos.", "Se vendes zapatos."], "Zapatos is plural → venden."),
        M("What does “Se prohíbe fumar” mean?", "Smoking is not allowed.", ["I smoke a lot.", "Smoking is free.", "Smoke here."], "Prohibir = to forbid."),
        M("How do you ask “How do you say ‘gracias’ in English?”", "¿Cómo se dice “gracias” en inglés?", ["¿Cómo dice se “gracias” en inglés?", "¿Cómo se digo “gracias” en inglés?", "¿Cómo se dicen “gracias” en inglés?"], "Se dice: one word, singular."),
    ],
    verify=vp("vender", "vendo", "vendes", "vende", "vendemos", "vendéis", "venden")
           + vp("alquilar", "alquilo", "alquilas", "alquila", "alquilamos", "alquiláis", "alquilan")
           + vp("hablar", "hablo", "hablas", "habla", "hablamos", "habláis", "hablan")
           + vp("prohibir", "prohíbo", "prohíbes", "prohíbe", "prohibimos", "prohibís", "prohíben")
           + vp("tomar", "tomo", "tomas", "toma", "tomamos", "tomáis", "toman"),
)

# ---------------------------------------------------------------------------- 198
L198 = lesson(
    "Reading signs and ads",
    "Se necesita conductor. Se ofrece servicio a domicilio.",
    requires=["necesitar", "ofrecer", "alquilar", "vender", "comer", "beber", "conductor", "camión", "precio"],
    cards=[
        card("Typical notices",
             "Notices are short and use the impersonal se. Learn the patterns, and you will understand most of the "
             "signs you see on the street.",
             tables=[table(["Aviso", "English"],
                           [["Se vende bicicleta. Buen precio.", "Bicycle for sale. Good price."],
                            ["Se alquila apartamento cerca del metro.", "Apartment for rent near the subway."],
                            ["Se necesita conductor para camión.", "Truck driver needed."],
                            ["Se habla inglés.", "English spoken."],
                            ["Se ofrece servicio a domicilio.", "Home delivery available."],
                            ["Se prohíbe comer y beber.", "No eating or drinking."],
                            ["Se vende boleto de ida y vuelta a Madrid.", "Round-trip ticket to Madrid for sale."],
                            ["Se prohíbe cruzar con el semáforo en rojo.", "No crossing when the light is red."]],
                           say=[0])]),
        card("Patterns",
             "Se vende / se venden = for sale. Se alquila / se alquilan = for rent. Se necesita = wanted, needed. Se "
             "ofrece = offered. Se prohíbe = forbidden. Se habla = spoken.",
             examples=[
                 ex("Se necesita cocinero con experiencia.", "Cook with experience needed.", "Se necesita"),
                 ex("Se ofrece servicio a domicilio.", "Home delivery offered.", "Se ofrece"),
                 ex("Se prohíbe comer y beber en el tren.", "No eating or drinking on the train.", "Se prohíbe"),
             ]),
    ],
    exercises=[
        F("Se ___ comer y beber en el tren.", "prohíbe", ["prohíben", "prohíbo", "prohíbes"], "Singular infinitive subject → prohíbe.", tr="No eating or drinking on the train.", lemma="prohibir:él"),
        F("Se ___ servicio a domicilio.", "ofrece", ["ofrecen", "ofrezco", "ofreces"], "Servicio is singular.", tr="Home delivery offered.", lemma="ofrecer:él"),
        F("Se ___ conductor para el camión.", "necesita", ["necesitan", "necesito", "necesitas"], "Conductor is singular.", tr="Driver needed for the truck.", lemma="necesitar:él"),
        F("Se ___ inglés.", "habla", ["hablan", "hablo", "hablas"], "Inglés is singular.", tr="English spoken.", lemma="hablar:él"),
        F("Se ___ apartamento por mes.", "alquila", ["alquilan", "alquilo", "alquilas"], "A monthly price → for rent.", tr="Apartment for rent by the month.", lemma="alquilar:él"),
        M("What does “Se vende” on a sign mean?", "for sale", ["for rent", "closed", "open"], "Vender = to sell."),
        M("What does “Se necesita conductor” mean?", "Driver needed", ["Driver for sale", "No drivers", "Driver wanted dead"], "Necesitar = to need."),
        M("What does “Se habla inglés” mean?", "English spoken", ["English for sale", "English taught", "No English"], "Hablar = to speak."),
        M("Which sign is a rule for travelers?", "Se prohíbe fumar.", ["Se vende casa.", "Se alquila bote.", "Se necesita cocinero."], "A rule about behavior."),
    ],
    verify=vp("ofrecer", "ofrezco", "ofreces", "ofrece", "ofrecemos", "ofrecéis", "ofrecen")
           + vp("necesitar", "necesito", "necesitas", "necesita", "necesitamos", "necesitáis", "necesitan"),
)

# ---------------------------------------------------------------------------- 199
L199 = lesson(
    "A history of the railroad",
    "El tren llegó, los ingenieros construyeron las vías.",
    requires=["tren", "llegar", "trabajar", "salir", "viajar", "traer", "vender", "poder", "ciudad", "cambio"],
    cards=[
        card("Read the story",
             "Histories use the preterite for events that started and ended. Read this short history of a railroad. "
             "Find the regular verbs and the irregular ones.",
             examples=[
                 ex("Hace más de cien años, el tren llegó a mi ciudad.", "More than a hundred years ago, the train came to my city.", "llegó"),
                 ex("Los ingenieros construyeron las vías y los puentes.", "The engineers built the tracks and the bridges.", "construyeron"),
                 ex("Muchas personas trabajaron en el proyecto durante años.", "Many people worked on the project for years.", "trabajaron"),
                 ex("El primer tren salió de la estación central y viajó hasta el puerto.", "The first train left the central station and traveled to the port.", "salió"),
                 ex("La llegada del tren trajo un gran cambio.", "The arrival of the train brought a big change.", "trajo"),
                 ex("Los agricultores vendieron sus productos en otras ciudades y la gente pudo viajar más rápido.", "Farmers sold their products in other cities and people could travel faster.", "vendieron"),
             ]),
        card("A new spelling pattern: -yó, -yeron",
             "When the stem of an -er or -ir verb ends in a vowel, the i of the ending becomes y in the él and ellos "
             "forms: construir → construyó, construyeron; leer → leyó, leyeron; creer → creyó, creyeron.",
             tables=[table(["Infinitivo", "él", "ellos"],
                           [["construir", "constru{yó}", "constru{yeron}"],
                            ["leer", "le{yó}", "le{yeron}"],
                            ["creer", "cre{yó}", "cre{yeron}"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Hace cien años el tren ___ a mi ciudad.", "llegó", ["llegué", "llegaron", "llega"], "El tren → él: llegó.", tr="A hundred years ago the train came to my city.", lemma="llegar:él:pret"),
        F("Los ingenieros ___ las vías y los puentes.", "construyeron", ["construyó", "construyeran", "construyen"], "Ellos → construyeron (y, not i).", tr="The engineers built the tracks and the bridges.", lemma="construir:ellos:pret"),
        F("El primer tren ___ de la estación central.", "salió", ["salí", "salieron", "sale"], "Él → salió.", tr="The first train left the central station.", lemma="salir:él:pret"),
        F("La llegada del tren ___ un gran cambio.", "trajo", ["trajeron", "traje", "trae"], "Singular subject → trajo.", tr="The arrival of the train brought a big change.", lemma="traer:él:pret"),
        F("Los agricultores ___ sus productos en otras ciudades.", "vendieron", ["vendió", "vendí", "venden"], "Ellos → vendieron.", tr="Farmers sold their products in other cities.", lemma="vender:ellos:pret"),
        M("What is the él preterite of “leer”?", "leyó", ["leió", "leó", "lee"], "The i between vowels becomes y."),
        M("Why is it “construyeron” and not “construieron”?", "i between vowels becomes y", ["it is a plural rule", "construir is irregular in the present", "it is a typo"], "Constru- + -yeron."),
        M("What did the train bring to the city?", "a big change", ["a big hotel", "a new airport", "a lot of snow"], "La llegada del tren trajo un gran cambio."),
        M("Who built the tracks and bridges?", "the engineers", ["the farmers", "the passengers", "the waiters"], "Los ingenieros construyeron las vías."),
    ],
    verify=vpp("construir", "construí", "construiste", "construyó", "construimos", "construisteis", "construyeron")
           + vpp("leer", "leí", "leíste", "leyó", "leímos", "leísteis", "leyeron")
           + vpp("creer", "creí", "creíste", "creyó", "creímos", "creísteis", "creyeron")
           + vpp("salir", "salí", "saliste", "salió", "salimos", "salisteis", "salieron"),
)

# ---------------------------------------------------------------------------- 200
L200 = lesson(
    "Review: travel, irregular preterites and object pronouns",
    "Fuimos, tuve, hace dos años, se lo di, otro boleto, se vende",
    requires=["viaje", "boleto", "hacer", "ir", "estar", "tener"],
    cards=[
        card("Irregular preterites at a glance",
             "Special stems take the special endings -e, -iste, -o, -imos, -isteis, -ieron (with no accents). After j "
             "the ending is -eron. Ser and ir share forms, and dar and ver use regular -er/-ir endings with no accent.",
             tables=[table(["Infinitivo", "yo", "él", "ellos"],
                           [["estar", "estuve", "estuvo", "estuvieron"],
                            ["tener", "tuve", "tuvo", "tuvieron"],
                            ["poder", "pude", "pudo", "pudieron"],
                            ["hacer", "hice", "hizo", "hicieron"],
                            ["venir", "vine", "vino", "vinieron"],
                            ["decir", "dije", "dijo", "dijeron"],
                            ["traer", "traje", "trajo", "trajeron"],
                            ["ser · ir", "fui", "fue", "fueron"],
                            ["dar", "di", "dio", "dieron"],
                            ["ver", "vi", "vio", "vieron"]],
                           say=[1, 2, 3])]),
        card("Other tools from this unit",
             "Hace + time = ago. Hace + time + que + present or preterite tells how long. In a double pronoun, the "
             "indirect one comes first and le/les become se before lo, la, los, las. Otro never takes un. The "
             "impersonal se appears on signs.",
             examples=[
                 ex("Fui a Lima hace dos años.", "I went to Lima two years ago.", "hace dos años"),
                 ex("Mi padre me lo regaló.", "My father gave it to me.", "me lo"),
                 ex("Le di el boleto a Laura. Se lo di ayer.", "I gave the ticket to Laura. I gave it to her yesterday.", "Se lo"),
                 ex("Se vende boleto de ida y vuelta.", "Round-trip ticket for sale.", "Se vende"),
             ]),
    ],
    exercises=[
        F("Ayer nosotros ___ al aeropuerto.", "fuimos", ["fueron", "fui", "vamos"], "Nosotros → fuimos.", tr="Yesterday we went to the airport.", lemma="ir:nosotros:pret"),
        F("Anoche yo ___ que esperar dos horas.", "tuve", ["tuvo", "tengo", "tuvieron"], "Yo → tuve.", tr="Last night I had to wait two hours.", lemma="tener:yo:pret"),
        F("Mi madre me ___ un regalo hace una semana.", "dio", ["di", "dieron", "doy"], "Mi madre → dio.", tr="My mother gave me a gift a week ago.", lemma="dar:ella:pret"),
        F("Mis amigos ___ a la fiesta anoche.", "vinieron", ["vino", "vine", "vienen"], "Ellos → vinieron.", tr="My friends came to the party last night.", lemma="venir:ellos:pret"),
        F("Le di el boleto a Laura. ___ lo di ayer.", "Se", ["Le", "Me", "Te"], "Le + lo → se lo.", tr="I gave the ticket to Laura. I gave it to her yesterday."),
        F("Mi amiga me mandó la foto. Mi amiga me ___ mandó.", "la", ["lo", "los", "las"], "Foto is feminine singular.", tr="My friend sent me the photo. My friend sent it to me."),
        F("¿Me puede vender ___ boleto?", "otro", ["otra", "otros", "otras"], "Boleto is masculine singular.", tr="Can you sell me another ticket?"),
        F("Se ___ casa.", "vende", ["venden", "vendo", "vendes"], "Casa is singular.", tr="House for sale.", lemma="vender:él"),
        F("Hace dos años que ___ a Lima, y no vuelvo.", "viajé", ["viajo", "viajó", "viajaron"], "Finished action → preterite.", tr="It has been two years since I traveled to Lima, and I haven’t been back.", lemma="viajar:yo:pret"),
        M("Which is the yo preterite of “hacer”?", "hice", ["hizo", "hago", "hacía"], "Yo → hice."),
        M("What does “Hubo mucho tráfico” mean?", "There was a lot of traffic.", ["There is a lot of traffic.", "He had a lot of traffic.", "They make traffic."], "Hubo = there was."),
        M("Which sentence means “I’m going to give it to him”?", "Voy a dárselo.", ["Voy a darlese.", "Voy dárselo a.", "Voy a lo darse."], "Pronouns attach to the infinitive with an accent."),
    ],
    verify=vpp("ir", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"),
)
UNIT = unit("De viaje", [L180, L181, L182, L183, L184, L185, L186, L187, L188, L189, L190, L191, L192, L193, L194, L195, L196, L197, L198, L199, L200])

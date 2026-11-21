"""Unit 23: natural disasters, formal commands reviewed, commands with nosotros (textbook Chapter 23)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 425
L425 = lesson(
    "Natural disasters: the names",
    "Un terremoto, un huracán, una inundación, una erupción.",
    requires=["terremoto", "huracán", "inundación", "incendio", "tormenta", "ola", "calor", "fuego", "viento", "tierra"],
    cards=[
        card("What can happen",
             "These are the names of the natural disasters most often in the news. Terremoto, sismo and temblor all mean “earthquake” (temblor is the everyday word in much of Latin America and sismo is common in Mexico and Central America; terremoto is often used for a strong one).",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el terremoto, el sismo", "earthquake", "Un terremoto sacudió la ciudad."],
                            ["el huracán", "hurricane", "El huracán llegó a la isla por la noche."],
                            ["la inundación", "flood", "La inundación cubrió las calles."],
                            ["el incendio forestal", "wildfire", "Un incendio forestal destruyó el bosque."],
                            ["la erupción volcánica", "volcanic eruption", "La erupción cubrió el pueblo de ceniza."],
                            ["la sequía", "drought", "La sequía secó los campos."],
                            ["el deslizamiento de tierra", "landslide", "Un deslizamiento de tierra cerró la carretera."],
                            ["el tsunami", "tsunami", "Un terremoto en el mar puede causar un tsunami."],
                            ["la ola de calor", "heat wave", "La ola de calor duró una semana."]],
                           say=[2])]),
    ],
    exercises=[
        F("Un ___ es un movimiento fuerte de la tierra.", "terremoto", ["huracán", "incendio", "ola"], "Earthquake.", tr="An earthquake is a strong movement of the ground."),
        F("Un ___ es un viento muy fuerte que se forma sobre el mar.", "huracán", ["terremoto", "incendio", "volcán"], "Hurricane.", tr="A hurricane is a very strong wind that forms over the sea."),
        F("Una ___ ocurre cuando hay demasiada agua en un lugar.", "inundación", ["sequía", "erupción", "ola de calor"], "Flood.", tr="A flood happens when there is too much water in one place."),
        F("Un incendio ___ quema el bosque.", "forestal", ["marino", "volcánico", "urbano"], "Wildfire.", tr="A wildfire burns the forest."),
        F("Cuando un volcán echa fuego y ceniza, hay una ___.", "erupción", ["inundación", "sequía", "tormenta"], "Eruption.", tr="When a volcano throws out fire and ash, there is an eruption."),
        F("Una ___ es un periodo largo sin lluvia.", "sequía", ["inundación", "erupción", "ola"], "Drought.", tr="A drought is a long period without rain."),
        M("Which word means the same as terremoto?", "sismo", ["huracán", "sequía", "incendio"], "Sismo = earthquake."),
        M("What can an earthquake in the sea cause?", "a tsunami", ["a drought", "a heat wave", "a hurricane"], "Tsunami."),
        M("What does “una ola de calor” mean?", "a heat wave", ["a sea wave", "a cold front", "a big storm"], "Ola de calor."),
    ],
)

# ---------------------------------------------------------------------------- 426
L426 = lesson(
    "Earthquake words: magnitude, epicenter, aftershock",
    "El terremoto tuvo una magnitud de siete y hubo varias réplicas.",
    requires=["terremoto", "magnitud", "escala", "temblar", "fuerte", "tierra", "minuto", "ciudad", "daño", "después"],
    cards=[
        card("Talking about how strong it was",
             "Scientists use a few words again and again. The magnitude measures the force of the earthquake on a scale. The epicenter is the point on the surface above where the earthquake begins. An aftershock (réplica) is a smaller tremor that follows the big one.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la magnitud", "magnitude", "La magnitud fue de siete."],
                            ["la escala", "scale", "La escala mide la fuerza del terremoto."],
                            ["el epicentro", "epicenter", "El epicentro estaba cerca de la costa."],
                            ["la réplica", "aftershock", "Después del terremoto hubo muchas réplicas."],
                            ["temblar", "to shake", "La tierra tembló durante un minuto."],
                            ["sentir", "to feel", "Se sintió en toda la ciudad."]],
                           say=[2])]),
    ],
    exercises=[
        F("La ___ mide la fuerza de un terremoto.", "magnitud", ["réplica", "ciudad", "costa"], "Magnitude.", tr="The magnitude measures the force of an earthquake."),
        F("El ___ es el punto de la superficie sobre el lugar donde empieza el terremoto.", "epicentro", ["puerto", "puente", "valle"], "Epicenter.", tr="The epicenter is the point on the surface above where the earthquake begins."),
        F("Una ___ es un temblor más pequeño que llega después del terremoto grande.", "réplica", ["escala", "magnitud", "inundación"], "Aftershock.", tr="An aftershock is a smaller tremor that comes after the big earthquake."),
        F("Anoche la tierra ___ durante casi un minuto.", "tembló", ["temblaron", "temblar", "tiembla"], "La tierra is singular; a finished event.", tr="Last night the ground shook for almost a minute.", lemma="temblar:él:pret"),
        F("El terremoto se ___ en toda la ciudad.", "sintió", ["sintieron", "sentir", "siente"], "Passive se: terremoto is singular.", tr="The earthquake was felt throughout the city.", lemma="sentir:él:pret"),
        F("Después del primer terremoto hubo muchas ___.", "réplicas", ["escalas", "magnitudes", "costas"], "Aftershocks.", tr="After the first earthquake there were many aftershocks."),
        M("Which word means how strong an earthquake is?", "la magnitud", ["la réplica", "la costa", "el valle"], "Magnitud."),
        M("What is a réplica?", "A smaller tremor after the big one", ["The first earthquake", "A kind of storm", "A type of scale"], "Réplica."),
        M("What happened to the ground in “La tierra tembló”?", "It shook", ["It froze", "It dried up", "It flooded"], "Temblar = to shake."),
    ],
    verify=(vpp("temblar", "temblé", "temblaste", "tembló", "temblamos", "temblasteis", "temblaron")
            + vpp("sentir", "sentí", "sentiste", "sintió", "sentimos", "sentisteis", "sintieron")),
)

# ---------------------------------------------------------------------------- 427
L427 = lesson(
    "Storms and floods",
    "El huracán trajo mucho viento y lluvia, y las calles se inundaron.",
    requires=["huracán", "tormenta", "viento", "lluvia", "ola", "inundación", "nube", "rayo", "puerto", "cerrar", "isla", "casa"],
    cards=[
        card("The words of a storm report",
             "A storm report describes the sky, the wind, the rain, the sea and the damage. Notice the verbs: llover (to rain), soplar (to blow), inundarse (to flood), llegar (to arrive).",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la tormenta", "storm", "La tormenta duró toda la noche."],
                            ["el viento", "wind", "El viento sopló muy fuerte."],
                            ["la lluvia", "rain", "La lluvia fue intensa."],
                            ["la nube", "cloud", "El cielo estaba lleno de nubes."],
                            ["el rayo", "lightning bolt", "Un rayo cayó cerca de la casa."],
                            ["la ola", "wave", "Las olas llegaron hasta la calle."],
                            ["inundarse", "to flood", "Las calles se inundaron."],
                            ["cerrar el puerto", "to close the port", "Cerraron el puerto por el huracán."]],
                           say=[2])]),
    ],
    exercises=[
        F("El ___ sopló muy fuerte durante la tormenta.", "viento", ["rayo", "puerto", "techo"], "Wind.", tr="The wind blew very hard during the storm."),
        F("Un ___ cayó cerca de la casa y se fue la luz.", "rayo", ["viento", "puerto", "valle"], "Lightning bolt.", tr="A lightning bolt struck near the house and the power went out."),
        F("Las ___ llegaron hasta la calle.", "olas", ["nubes", "casas", "piedras"], "Waves.", tr="The waves reached the street."),
        F("Cerraron el ___ por el huracán.", "puerto", ["viento", "rayo", "techo"], "Port.", tr="They closed the port because of the hurricane."),
        F("Las calles se ___ en pocas horas.", "inundaron", ["inundó", "inundar", "inundamos"], "Calles is plural.", tr="The streets flooded within a few hours.", lemma="inundar:ellos:pret"),
        F("Anoche la lluvia ___ casi cuatro horas.", "duró", ["duraron", "durar", "dura"], "Lluvia is singular.", tr="Last night the rain lasted almost four hours.", lemma="durar:él:pret"),
        M("Which word is used for water that arrives from the sea?", "las olas", ["los rayos", "las nubes", "los techos"], "Olas."),
        M("What does “las calles se inundaron” mean?", "The streets flooded", ["The streets were closed", "The streets were empty", "The streets were cleaned"], "Inundarse = to flood."),
        M("What is a tormenta?", "a storm", ["a drought", "a landslide", "an earthquake"], "Tormenta."),
    ],
    verify=(vpp("inundar", "inundé", "inundaste", "inundó", "inundamos", "inundasteis", "inundaron")
            + vpp("durar", "duré", "duraste", "duró", "duramos", "durasteis", "duraron")),
)

# ---------------------------------------------------------------------------- 428
L428 = lesson(
    "Fires and drought",
    "La sequía, el calor y el viento ayudan a que el fuego se extienda.",
    requires=["incendio", "fuego", "humo", "bombero", "calor", "viento", "seco", "hectárea", "quemar", "extender", "agua", "árbol"],
    cards=[
        card("Why wildfires spread",
             "Wildfires need dry land, heat and wind. When the ground and the plants are dry after a drought, a small fire can become very large in a few hours.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el fuego", "fire", "El fuego se movió rápido por el viento."],
                            ["el humo", "smoke", "El humo cubrió el cielo."],
                            ["la hectárea", "hectare", "Se quemaron miles de hectáreas."],
                            ["el bombero", "firefighter", "Los bomberos trabajaron día y noche."],
                            ["quemarse", "to burn", "El bosque se quemó en tres días."],
                            ["extenderse", "to spread", "El fuego se extendió por el viento."],
                            ["apagar", "to put out", "Los bomberos apagaron el incendio."]],
                           say=[2])]),
    ],
    exercises=[
        F("El ___ cubrió el cielo y casi no se veía el sol.", "humo", ["rayo", "viento", "puerto"], "Smoke.", tr="The smoke covered the sky and the sun could hardly be seen."),
        F("Los ___ trabajaron día y noche.", "bomberos", ["rayos", "vientos", "puertos"], "Firefighters.", tr="The firefighters worked day and night."),
        F("Ayer el fuego se ___ rápidamente por el viento.", "extendió", ["extendieron", "extender", "extiende"], "Fuego is singular; finished event.", tr="The fire spread quickly because of the wind.", lemma="extender:él:pret"),
        F("Con la tierra tan ___, el fuego avanza muy rápido.", "seca", ["seco", "secos", "secas"], "Tierra is feminine singular.", tr="With the ground so dry, the fire advances very fast."),
        F("Los bomberos ___ el incendio después de dos días.", "apagaron", ["apagó", "apagar", "apagan"], "Bomberos is plural; finished event.", tr="The firefighters put out the fire after two days.", lemma="apagar:ellos:pret"),
        F("El año pasado el bosque se ___ en tres días.", "quemó", ["quemaron", "quemar", "quema"], "Bosque is singular.", tr="The forest burned in three days.", lemma="quemar:él:pret"),
        M("Which three things make a wildfire spread faster?", "Drought, heat and wind", ["Snow, cold and rain", "Rivers, lakes and sea", "Roads, cars and noise"], "Sequía, calor, viento."),
        M("What is a hectárea?", "a unit of land area", ["a type of tree", "a type of smoke", "a fire truck"], "Hectárea."),
        M("What does apagar mean for a fire?", "to put it out", ["to start it", "to move it", "to photograph it"], "Apagar."),
    ],
    verify=(vpp("extender", "extendí", "extendiste", "extendió", "extendimos", "extendisteis", "extendieron")
            + vpp("apagar", "apagué", "apagaste", "apagó", "apagamos", "apagasteis", "apagaron")),
)

# ---------------------------------------------------------------------------- 429
L429 = lesson(
    "After the disaster: damage and victims",
    "Hubo heridos, desaparecidos y miles de personas sin casa.",
    requires=["daño", "víctima", "herido", "muerto", "desaparecido", "sobreviviente", "casa", "edificio", "puente", "carretera", "destruir", "reconstrucción"],
    cards=[
        card("Describing the aftermath",
             "After a disaster, reports count what was lost and who needs help. Herido (injured), muerto (dead) and desaparecido (missing) are participles used as nouns: with haber (hubo heridos) they say how many people were affected, and like any noun they can be the subject or object of other verbs (buscan a los desaparecidos).",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el daño", "damage", "Los daños fueron enormes."],
                            ["la víctima", "victim", "Las víctimas recibieron ayuda."],
                            ["el herido", "injured person", "Hubo muchos heridos en el hospital."],
                            ["el muerto", "dead person", "Lamentablemente hubo muertos."],
                            ["el desaparecido", "missing person", "Todavía buscan a los desaparecidos."],
                            ["el sobreviviente", "survivor", "Los sobrevivientes pasaron la noche afuera."],
                            ["el damnificado", "person affected by a disaster", "Miles de damnificados perdieron su casa."],
                            ["los escombros", "debris, rubble", "Los rescatistas buscan entre los escombros."],
                            ["la reconstrucción", "rebuilding", "La reconstrucción tardó años."]],
                           say=[2])]),
    ],
    exercises=[
        F("Los ___ fueron enormes: muchas casas quedaron destruidas.", "daños", ["puertos", "vientos", "ríos"], "Damage.", tr="The damage was enormous: many houses were destroyed."),
        F("Todavía buscan a los ___ entre los escombros.", "desaparecidos", ["herederos", "puentes", "pájaros"], "Missing persons.", tr="They are still searching for the missing among the rubble."),
        F("Los ___ pasaron la noche afuera, con frío.", "sobrevivientes", ["edificios", "puentes", "ríos"], "Survivors.", tr="The survivors spent the night outside, in the cold."),
        F("Hubo muchos ___ en el hospital.", "heridos", ["puentes", "techos", "ríos"], "Injured.", tr="There were many injured people at the hospital."),
        F("El puente fue ___ por el terremoto.", "destruido", ["destruida", "destruidos", "destruir"], "Puente is masculine singular.", tr="The bridge was destroyed by the earthquake.", lemma="destruir:part"),
        F("La ___ de las casas tardó varios años.", "reconstrucción", ["herida", "sequía", "tormenta"], "Rebuilding.", tr="The rebuilding of the houses took several years."),
        M("Which word means “missing person”?", "el desaparecido", ["el sobreviviente", "el herido", "el vecino"], "Desaparecido."),
        M("Which sentence is correct for “There were many injured people”?", "Hubo muchos heridos.", ["Hubieron muchos heridos.", "Hay muchos heridos ayer.", "Fueron muchos heridos."], "Hubo is always singular."),
        M("What are escombros?", "rubble", ["rivers", "storms", "roads"], "Escombros."),
    ],
    verify=vpa("destruir", "destruido"),
)

# ---------------------------------------------------------------------------- 430
L430 = lesson(
    "Rescue and relief",
    "Los bomberos rescataron a los sobrevivientes y los voluntarios llevaron ayuda.",
    requires=["rescatar", "rescate", "bombero", "voluntario", "donación", "refugio", "ayuda", "donar", "llevar", "equipo", "buscar", "encontrar"],
    cards=[
        card("Helping after a disaster",
             "Rescue teams look for people; volunteers and governments deliver aid. These are the words for who does what and what they bring.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["rescatar", "to rescue", "Los bomberos rescataron a una familia."],
                            ["el equipo de rescate", "rescue team", "El equipo de rescate llegó en una hora."],
                            ["el voluntario", "volunteer", "Cientos de voluntarios ayudaron a limpiar."],
                            ["la donación", "donation", "Las donaciones llegaron de muchos países."],
                            ["donar", "to donate", "Muchas personas donaron comida y agua."],
                            ["el refugio, el albergue", "shelter", "Las familias durmieron en un albergue."],
                            ["la ayuda humanitaria", "humanitarian aid", "La ayuda humanitaria llegó por avión."]],
                           say=[2])]),
    ],
    exercises=[
        F("Anoche los bomberos ___ a una familia que estaba atrapada.", "rescataron", ["rescató", "rescatar", "rescatan"], "Bomberos is plural; finished event.", tr="The firefighters rescued a family that was trapped.", lemma="rescatar:ellos:pret"),
        F("Ayer muchas personas ___ comida y agua.", "donaron", ["donó", "donar", "donan"], "Personas is plural; finished event.", tr="Many people donated food and water.", lemma="donar:ellos:pret"),
        F("Las familias durmieron en un ___.", "albergue", ["puente", "puerto", "techo"], "Shelter.", tr="The families slept in a shelter."),
        F("Cientos de ___ ayudaron a limpiar las calles.", "voluntarios", ["escombros", "vientos", "techos"], "Volunteers.", tr="Hundreds of volunteers helped clean the streets."),
        F("El equipo de ___ llegó en una hora.", "rescate", ["viento", "sequía", "puerto"], "Rescue.", tr="The rescue team arrived within an hour."),
        F("Ayer la ayuda humanitaria ___ por avión.", "llegó", ["llegaron", "llegar", "llega"], "Ayuda is singular; finished event.", tr="Humanitarian aid arrived by plane.", lemma="llegar:él:pret"),
        M("Who looks for people in the rubble?", "the rescue team", ["the tourists", "the mayor’s family", "the news anchors"], "Equipo de rescate."),
        M("What does donar mean?", "to give for free", ["to rescue", "to burn", "to flood"], "Donar."),
        M("What is a donación?", "something given to help", ["a kind of storm", "a rescue vehicle", "a government law"], "Donación."),
    ],
    verify=(vpp("rescatar", "rescaté", "rescataste", "rescató", "rescatamos", "rescatasteis", "rescataron")
            + vpp("donar", "doné", "donaste", "donó", "donamos", "donasteis", "donaron")
            + vpp("llegar", "llegué", "llegaste", "llegó", "llegamos", "llegasteis", "llegaron")),
)

# ---------------------------------------------------------------------------- 431
L431 = lesson(
    "Reading: Chile, 1960, the strongest earthquake ever recorded",
    "El terremoto de Valdivia tuvo la magnitud más alta que se ha registrado.",
    requires=["terremoto", "magnitud", "registrar", "sur", "costa", "océano", "viajar", "casa", "morir", "ciudad", "mundo"],
    cards=[
        card("A giant earthquake in the south of Chile",
             "Read a short account, then answer the questions.",
             examples=[
                 ex("El veintidós de mayo de mil novecientos sesenta, un terremoto sacudió el sur de Chile.", "On May 22, 1960, an earthquake shook the south of Chile.", "sacudió"),
                 ex("Se llama el terremoto de Valdivia, por la ciudad que sufrió grandes daños.", "It is called the Valdivia earthquake, after the city that suffered great damage.", "Se llama"),
                 ex("Su magnitud fue de nueve punto cinco, la más alta que se ha registrado en el mundo.", "Its magnitude was 9.5, the highest ever recorded in the world.", "se ha registrado"),
                 ex("La tierra tembló durante varios minutos y muchas casas se cayeron.", "The ground shook for several minutes and many houses fell down.", "tembló"),
                 ex("El terremoto produjo un tsunami que cruzó el océano Pacífico.", "The earthquake caused a tsunami that crossed the Pacific Ocean.", "cruzó"),
                 ex("Las olas llegaron hasta Hawái y Japón y causaron más daños.", "The waves reached Hawaii and Japan and caused more damage.", "llegaron"),
                 ex("Murieron muchas personas y muchísimas se quedaron sin casa.", "Many people died and a great many were left without a home.", "se quedaron"),
             ]),
    ],
    exercises=[
        F("El veintidós de mayo de mil novecientos sesenta, un terremoto ___ el sur de Chile.", "sacudió", ["sacudieron", "sacudir", "sacude"], "Finished event with a date.", tr="On May 22, 1960, an earthquake shook the south of Chile.", lemma="sacudir:él:pret"),
        F("En mil novecientos sesenta la tierra ___ durante varios minutos.", "tembló", ["temblaron", "temblar", "tiembla"], "Tierra is singular; finished event.", tr="The ground shook for several minutes.", lemma="temblar:él:pret"),
        F("El terremoto produjo un tsunami que, horas después, ___ el océano Pacífico.", "cruzó", ["cruzaron", "cruzar", "cruza"], "Tsunami is singular.", tr="The earthquake caused a tsunami that crossed the Pacific Ocean.", lemma="cruzar:él:pret"),
        F("Horas después, las olas ___ hasta Hawái y Japón.", "llegaron", ["llegó", "llegar", "llegan"], "Olas is plural.", tr="The waves reached Hawaii and Japan.", lemma="llegar:ellos:pret"),
        F("Muchas personas ___ sin casa.", "se quedaron", ["se quedó", "quedar", "quedaron sin"], "Personas is plural.", tr="Many people were left without a home."),
        M("Which city gave its name to the earthquake?", "Valdivia", ["Santiago", "Lima", "Quito"], "Terremoto de Valdivia."),
        M("What is special about its magnitude?", "It was the highest ever recorded", ["It was the lowest ever recorded", "It was measured only in Japan", "It was unknown"], "La más alta."),
        M("Where did the tsunami travel?", "Across the Pacific Ocean", ["Across the Atlantic", "Up the Amazon", "Along the Andes"], "Océano Pacífico."),
        M("When did it happen?", "May 22, 1960", ["May 22, 1906", "September 19, 1985", "June 3, 2018"], "Veintidós de mayo de 1960."),
    ],
    verify=(vpp("sacudir", "sacudí", "sacudiste", "sacudió", "sacudimos", "sacudisteis", "sacudieron")
            + vpp("cruzar", "crucé", "cruzaste", "cruzó", "cruzamos", "cruzasteis", "cruzaron")),
)

# ---------------------------------------------------------------------------- 432
L432 = lesson(
    "Reading: Hurricane María in Puerto Rico",
    "El huracán María dejó a toda la isla sin electricidad.",
    requires=["huracán", "isla", "electricidad", "casa", "ayuda", "tardar", "recibir", "morir", "gobierno", "después", "antes"],
    cards=[
        card("A hurricane, two weeks after another one",
             "Puerto Rico was hit by two major hurricanes in September 2017. The past perfect and the preterite together tell the story.",
             examples=[
                 ex("Dos semanas antes, el huracán Irma ya había pasado cerca de Puerto Rico.", "Two weeks earlier, Hurricane Irma had already passed near Puerto Rico.", "ya había pasado"),
                 ex("El veinte de septiembre de dos mil diecisiete, el huracán María llegó a la isla con vientos muy fuertes.", "On September 20, 2017, Hurricane María reached the island with very strong winds.", "llegó"),
                 ex("El viento destruyó casas, árboles y líneas eléctricas, y las lluvias causaron inundaciones.", "The wind destroyed houses, trees and power lines, and the rains caused floods.", "destruyó"),
                 ex("Toda la isla se quedó sin electricidad, y en algunos lugares la luz tardó meses en volver.", "The whole island lost power, and in some places the electricity took months to return.", "tardó"),
                 ex("Mucha gente no podía llamar por teléfono ni comprar comida.", "Many people could not make phone calls or buy food.", "no podía"),
                 ex("Más tarde, el gobierno reconoció que murieron casi tres mil personas durante los meses siguientes.", "Later, the government recognized that almost three thousand people died in the following months.", "reconoció"),
                 ex("La ayuda llegó de otros estados y de muchos voluntarios.", "Aid arrived from other states and from many volunteers.", "llegó"),
             ]),
    ],
    exercises=[
        F("Dos semanas antes, el huracán Irma ya ___ pasado cerca de la isla.", "había", ["habían", "ha", "hubo"], "Earlier past event.", tr="Two weeks earlier, Hurricane Irma had already passed near the island.", lemma="haber:él:impf"),
        F("En septiembre de dos mil diecisiete, el huracán María ___ a la isla con vientos muy fuertes.", "llegó", ["llegaron", "llegar", "llega"], "Finished event.", tr="Hurricane María reached the island with very strong winds.", lemma="llegar:él:pret"),
        F("Ese día el viento ___ casas, árboles y líneas eléctricas.", "destruyó", ["destruyeron", "destruir", "destruye"], "Viento is singular.", tr="The wind destroyed houses, trees and power lines.", lemma="destruir:él:pret"),
        F("Después del huracán, en algunos lugares la luz ___ meses en volver.", "tardó", ["tardaron", "tardar", "tarda"], "Luz is singular.", tr="In some places the electricity took months to return.", lemma="tardar:él:pret"),
        F("Cada día de aquella semana, mucha gente no ___ llamar por teléfono ni comprar comida.", "podía", ["pudo", "puede", "poder"], "Describing a situation → imperfect.", tr="Many people could not make phone calls or buy food.", lemma="poder:él:impf"),
        M("What had happened two weeks before María?", "Hurricane Irma had passed near the island", ["An earthquake had struck", "A volcano had erupted", "The power grid had been rebuilt"], "Irma."),
        M("What was the most visible effect on the whole island?", "No electricity", ["Snow", "A long drought", "A new volcano"], "Sin electricidad."),
        M("What did the government recognize later?", "That almost three thousand people died in the following months", ["That nobody died", "That the hurricane was small", "That the island had moved"], "Casi tres mil."),
        M("Why does the text say “no podía”?", "It describes a situation, not a single event", ["It is a command", "It is a future plan", "It names one moment"], "Imperfect for background."),
    ],
    verify=(vpp("llegar", "llegué", "llegaste", "llegó", "llegamos", "llegasteis", "llegaron")
            + vpp("destruir", "destruí", "destruiste", "destruyó", "destruimos", "destruisteis", "destruyeron")
            + vpp("tardar", "tardé", "tardaste", "tardó", "tardamos", "tardasteis", "tardaron")),
)

# ---------------------------------------------------------------------------- 433
L433 = lesson(
    "Reading: the Volcán de Fuego in Guatemala",
    "El volcán de Fuego hizo erupción el tres de junio de dos mil dieciocho.",
    requires=["montaña", "fuego", "pueblo", "río", "bombero", "voluntario", "rescatar", "desaparecido", "ayuda", "buscar", "morir"],
    cards=[
        card("When a volcano erupts",
             "The Volcán de Fuego is one of the most active volcanoes in Central America. Read about its eruption in 2018.",
             examples=[
                 ex("El Volcán de Fuego, en Guatemala, es uno de los volcanes más activos de América.", "The Volcán de Fuego, in Guatemala, is one of the most active volcanoes in the Americas.", "es"),
                 ex("El tres de junio de dos mil dieciocho, tuvo una erupción muy fuerte.", "On June 3, 2018, it had a very strong eruption.", "tuvo"),
                 ex("Una nube de gas, ceniza y piedras calientes bajó por las laderas hasta varios pueblos.", "A cloud of gas, ash and hot rocks came down the slopes to several villages.", "bajó"),
                 ex("Muchas personas no tuvieron tiempo de salir.", "Many people did not have time to get out.", "no tuvieron"),
                 ex("Los bomberos voluntarios y los vecinos buscaron a los sobrevivientes entre la ceniza.", "Volunteer firefighters and neighbors searched for survivors in the ash.", "buscaron"),
                 ex("Cientos de personas murieron o quedaron desaparecidas.", "Hundreds of people died or were reported missing.", "murieron"),
                 ex("Muchos países enviaron ayuda, y la zona tardó años en recuperarse.", "Many countries sent aid, and the area took years to recover.", "enviaron"),
             ]),
    ],
    exercises=[
        F("El tres de junio de dos mil dieciocho, el volcán ___ una erupción muy fuerte.", "tuvo", ["tuvieron", "tener", "tiene"], "Finished event with a date.", tr="On June 3, 2018, the volcano had a very strong eruption.", lemma="tener:él:pret"),
        F("Ese día, una nube de gas, ceniza y piedras calientes ___ por las laderas.", "bajó", ["bajaron", "bajar", "baja"], "Nube is singular.", tr="A cloud of gas, ash and hot rocks came down the slopes.", lemma="bajar:él:pret"),
        F("Ese día, muchas personas no ___ tiempo de salir.", "tuvieron", ["tuvo", "tener", "tienen"], "Personas is plural.", tr="Many people did not have time to get out.", lemma="tener:ellos:pret"),
        F("Esa tarde, los bomberos voluntarios ___ a los sobrevivientes entre la ceniza.", "buscaron", ["buscó", "buscar", "buscan"], "Bomberos is plural.", tr="Volunteer firefighters searched for survivors in the ash.", lemma="buscar:ellos:pret"),
        F("Después de la erupción, muchos países ___ ayuda a Guatemala.", "enviaron", ["envió", "enviar", "envían"], "Países is plural.", tr="Many countries sent aid to Guatemala.", lemma="enviar:ellos:pret"),
        M("In which country is the Volcán de Fuego?", "Guatemala", ["Chile", "Puerto Rico", "Argentina"], "Guatemala."),
        M("When did the eruption happen?", "June 3, 2018", ["May 22, 1960", "September 20, 2017", "September 19, 1985"], "Tres de junio de 2018."),
        M("What came down the slopes?", "A cloud of gas, ash and hot rocks", ["A wave of seawater", "A snowstorm", "A swarm of insects"], "Nube de gas, ceniza y piedras."),
        M("Who searched for survivors?", "Volunteer firefighters and neighbors", ["Only the army", "Tourists", "Nobody"], "Bomberos y vecinos."),
    ],
    verify=(vpp("hacer", "hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron")
            + vpp("buscar", "busqué", "buscaste", "buscó", "buscamos", "buscasteis", "buscaron")
            + vpp("enviar", "envié", "enviaste", "envió", "enviamos", "enviasteis", "enviaron")),
)

# ---------------------------------------------------------------------------- 434
L434 = lesson(
    "Reading: wildfires in northern Argentina",
    "En dos mil veintidós el fuego destruyó una gran parte de los Esteros del Iberá.",
    requires=["incendio", "calor", "viento", "provincia", "hectárea", "animal", "humo", "bombero", "quemar", "ayudar", "destruir"],
    cards=[
        card("Fire in the wetlands",
             "In early 2022, large fires burned in the province of Corrientes, in northeastern Argentina. Read what happened and why it spread.",
             examples=[
                 ex("En enero de dos mil veintidós hubo grandes incendios en la provincia de Corrientes, en el noreste de Argentina.", "In January 2022 there were large fires in the province of Corrientes, in northeastern Argentina.", "hubo"),
                 ex("El fuego quemó cientos de miles de hectáreas, incluyendo una parte de los Esteros del Iberá, un enorme humedal.", "The fire burned hundreds of thousands of hectares, including part of the Esteros del Iberá, an enormous wetland.", "quemó"),
                 ex("Hacía meses que no llovía bastante, y el calor y el viento ayudaron a que el fuego se extendiera.", "It had not rained enough for months, and the heat and wind helped the fire spread.", "Hacía"),
                 ex("Muchos animales murieron o huyeron del humo.", "Many animals died or fled from the smoke.", "huyeron"),
                 ex("Bomberos y voluntarios de varias provincias y países llegaron a ayudar.", "Firefighters and volunteers from several provinces and countries came to help.", "llegaron"),
                 ex("Muchos incendios empezaron por actividades humanas, como quemar pasto.", "Many fires began from human activities, such as burning grass.", "empezaron"),
             ]),
    ],
    exercises=[
        F("En enero de dos mil veintidós ___ grandes incendios en Corrientes.", "hubo", ["haber", "hubieron", "ha habido"], "Finished event: hubo.", tr="In January 2022 there were large fires in Corrientes."),
        F("En aquellas semanas, el fuego ___ cientos de miles de hectáreas.", "quemó", ["quemaron", "quemar", "quema"], "Fuego is singular.", tr="The fire burned hundreds of thousands of hectares.", lemma="quemar:él:pret"),
        F("___ meses que no llovía bastante.", "Hacía", ["Hace", "Hizo", "Hacer"], "Hacía + time + que + imperfect.", tr="It had been months since it had rained enough.", lemma="hacer:él:impf"),
        F("Aquel verano, muchos animales ___ del humo.", "huyeron", ["huyó", "huir", "huyen"], "Animales is plural.", tr="Many animals fled from the smoke.", lemma="huir:ellos:pret"),
        F("Esa semana, bomberos y voluntarios ___ a ayudar.", "llegaron", ["llegó", "llegar", "llegan"], "Plural subject.", tr="Firefighters and volunteers came to help.", lemma="llegar:ellos:pret"),
        M("What helped the fire spread?", "Heat, wind and months of little rain", ["Heavy snow", "A flood", "New roads"], "Calor, viento y falta de lluvia."),
        M("What are the Esteros del Iberá?", "A huge wetland", ["A desert", "A city", "A mountain range"], "Un enorme humedal."),
        M("What happened to many animals?", "They died or fled", ["They multiplied", "They slept", "They were counted"], "Murieron o huyeron."),
        M("How did many fires begin?", "Through human activity, like burning grass", ["By a volcano", "By a hurricane", "By an earthquake"], "Actividades humanas."),
    ],
    verify=(vpp("huir", "hui", "huiste", "huyó", "huimos", "huisteis", "huyeron")
            + vpi("hacer", "hacía", "hacías", "hacía", "hacíamos", "hacíais", "hacían")),
)

# ---------------------------------------------------------------------------- 435
L435 = lesson(
    "Reading disaster headlines",
    "Un terremoto sacude la costa. Se registran réplicas.",
    requires=["terremoto", "registrar", "cerrar", "escuela", "ayuda", "víctima", "gobierno", "declarar", "emergencia", "carretera", "puerto"],
    cards=[
        card("How headlines are written",
             "Headlines are short. They often use the present tense to report something that just happened (the historical present), the passive se, and the present perfect with ha(n) + participle.",
             tables=[table(["Titular", "English"],
                           [["Un terremoto sacude la costa", "An earthquake shakes the coast"],
                            ["Se registran varias réplicas", "Several aftershocks are recorded"],
                            ["Cierran el puerto por el huracán", "Port closed because of the hurricane"],
                            ["Han sido evacuadas cien familias", "A hundred families have been evacuated"],
                            ["El gobierno declara el estado de emergencia", "The government declares a state of emergency"],
                            ["Ha habido daños en las carreteras", "There has been damage to the roads"]],
                           say=[0])]),
    ],
    exercises=[
        F("Un terremoto ___ la costa.", "sacude", ["sacuden", "sacudir", "sacudí"], "Headline present.", tr="An earthquake shakes the coast.", lemma="sacudir:él"),
        F("Se ___ varias réplicas.", "registran", ["registra", "registrar", "registro"], "Réplicas is plural.", tr="Several aftershocks are recorded.", lemma="registrar:ellos"),
        F("Las autoridades ___ el puerto por el huracán.", "cierran", ["cierra", "cerrar", "cerré"], "Plural subject.", tr="The authorities are closing the port because of the hurricane.", lemma="cerrar:ellos"),
        F("Han sido ___ cien familias.", "evacuadas", ["evacuado", "evacuados", "evacuar"], "Familias is feminine plural.", tr="A hundred families have been evacuated."),
        F("Ha ___ daños en las carreteras.", "habido", ["había", "hubo", "haber"], "Ha habido.", tr="There has been damage to the roads."),
        F("El gobierno ___ el estado de emergencia.", "declara", ["declaran", "declarar", "declaro"], "Headline present.", tr="The government declares a state of emergency.", lemma="declarar:él"),
        M("Why do headlines often use the present for past news?", "It makes the news feel immediate", ["Because the past tense is not allowed", "Because they are about the future", "Because they are commands"], "Historical present."),
        M("Which form is the passive se in a headline?", "Se registran varias réplicas", ["Un terremoto sacude la costa", "El gobierno declara una emergencia", "Han llegado los bomberos"], "Se + verb + noun."),
        M("What does “Han sido evacuadas cien familias” tell us?", "A hundred families have been evacuated", ["A hundred families will leave", "A hundred families were born", "Nobody left"], "Han sido + participle."),
    ],
    verify=(vp("sacudir", "sacudo", "sacudes", "sacude", "sacudimos", "sacudís", "sacuden")
            + vp("cerrar", "cierro", "cierras", "cierra", "cerramos", "cerráis", "cierran")),
)

# ---------------------------------------------------------------------------- 436
L436 = lesson(
    "Formal commands: the regular pattern",
    "Camine despacio. Lea las instrucciones. Escriba su nombre.",
    requires=["caminar", "leer", "escribir", "hablar", "comer", "abrir", "esperar", "usar", "instrucción", "nombre"],
    cards=[
        card("A quick review",
             "To give an order to one person you address as usted, take the yo form of the present, drop the -o, and add the opposite vowel: -ar verbs take -e; -er and -ir verbs take -a. For ustedes, add -n. "
             "Verbs ending in -car, -gar and -zar change their spelling to keep the sound: buscar → busque, pagar → pague, empezar → empiece.",
             tables=[table(["Infinitivo", "usted", "ustedes"],
                           [["caminar", "camine", "caminen"],
                            ["esperar", "espere", "esperen"],
                            ["leer", "lea", "lean"],
                            ["comer", "coma", "coman"],
                            ["escribir", "escriba", "escriban"],
                            ["abrir", "abra", "abran"],
                            ["buscar", "busque", "busquen"],
                            ["pagar", "pague", "paguen"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Señora, ___ despacio por las escaleras.", "camine", ["camina", "caminar", "caminen"], "Usted command of caminar.", tr="Ma’am, walk slowly down the stairs.", lemma="caminar:usted:cmd"),
        F("Señor, ___ las instrucciones antes de entrar.", "lea", ["lee", "leer", "lean"], "Usted command of leer.", tr="Sir, read the instructions before going in.", lemma="leer:usted:cmd"),
        F("Señores, ___ su nombre en esta lista.", "escriban", ["escribe", "escribir", "escriba"], "Ustedes command of escribir.", tr="Ladies and gentlemen, write your name on this list.", lemma="escribir:ustedes:cmd"),
        F("Señora, ___ aquí un momento, por favor.", "espere", ["espera", "esperar", "esperen"], "Usted command of esperar.", tr="Ma’am, wait here a moment, please.", lemma="esperar:usted:cmd"),
        F("Señor, ___ la puerta con cuidado.", "abra", ["abre", "abrir", "abran"], "Usted command of abrir.", tr="Sir, open the door carefully.", lemma="abrir:usted:cmd"),
        F("Señores, ___ en el refugio hasta que termine la tormenta.", "coman", ["comen", "comer", "come"], "Ustedes command of comer.", tr="Ladies and gentlemen, eat in the shelter until the storm ends.", lemma="comer:ustedes:cmd"),
        F("Señora, ___ a sus hijos en el refugio.", "busque", ["busca", "buscar", "busquen"], "Buscar → busque (c → qu).", tr="Ma’am, look for your children in the shelter.", lemma="buscar:usted:cmd"),
        M("Which vowel do -ar verbs take in the formal command?", "-e", ["-a", "-o", "-i"], "Opposite vowel."),
        M("How do you form the ustedes command?", "Add -n to the usted command", ["Add -s to the infinitive", "Add -mos to the verb", "Drop the -r from the infinitive"], "Hable → hablen."),
    ],
    verify=(vpc("caminar", "camine", "caminen") + vpc("esperar", "espere", "esperen") + vpc("leer", "lea", "lean")
            + vpc("comer", "coma", "coman") + vpc("escribir", "escriba", "escriban") + vpc("abrir", "abra", "abran")
            + vpc("buscar", "busque", "busquen") + vpc("pagar", "pague", "paguen")),
)

# ---------------------------------------------------------------------------- 437
L437 = lesson(
    "Formal commands: verbs with an irregular yo form",
    "Salga de la casa. Traiga agua. Tenga calma.",
    requires=["decir", "hacer", "oír", "poner", "salir", "tener", "traer", "venir", "calma", "fila"],
    cards=[
        card("The yo form decides",
             "A verb whose yo form is irregular (digo, hago, oigo, pongo, salgo, tengo, traigo, vengo) keeps that irregularity in every command form; the exceptions (dar, estar, ir, saber, ser) come in a later lesson. If you know digo, hago, oigo, pongo, salgo, tengo, traigo, vengo, you already know diga, haga, oiga, ponga, salga, tenga, traiga, venga.",
             tables=[table(["Infinitivo", "yo", "usted", "ustedes"],
                           [["decir", "digo", "diga", "digan"],
                            ["hacer", "hago", "haga", "hagan"],
                            ["oír", "oigo", "oiga", "oigan"],
                            ["poner", "pongo", "ponga", "pongan"],
                            ["salir", "salgo", "salga", "salgan"],
                            ["tener", "tengo", "tenga", "tengan"],
                            ["traer", "traigo", "traiga", "traigan"],
                            ["venir", "vengo", "venga", "vengan"]],
                           say=[2, 3])]),
    ],
    exercises=[
        F("Señora, ___ de la casa por la puerta principal.", "salga", ["sale", "salir", "salgan"], "Salir → salga.", tr="Ma’am, leave the house through the main door.", lemma="salir:usted:cmd"),
        F("Señor, ___ agua potable al refugio.", "traiga", ["trae", "traer", "traigan"], "Traer → traiga.", tr="Sir, bring drinking water to the shelter.", lemma="traer:usted:cmd"),
        F("Señores, ___ calma y sigan al guía.", "tengan", ["tienen", "tener", "tenga"], "Tener → tengan.", tr="Ladies and gentlemen, stay calm and follow the guide.", lemma="tener:ustedes:cmd"),
        F("Señora, ___ sus documentos en una bolsa.", "ponga", ["pone", "poner", "pongan"], "Poner → ponga.", tr="Ma’am, put your documents in a bag.", lemma="poner:usted:cmd"),
        F("Señores, ___ fila y esperen su turno.", "hagan", ["hacen", "hacer", "haga"], "Hacer → hagan.", tr="Ladies and gentlemen, form a line and wait your turn.", lemma="hacer:ustedes:cmd"),
        F("Señor, ___ al refugio ahora mismo.", "venga", ["viene", "venir", "vengan"], "Venir → venga.", tr="Sir, come to the shelter right now.", lemma="venir:usted:cmd"),
        F("Señora, ___ bien el aviso que da la radio.", "oiga", ["oye", "oír", "oigan"], "Oír → oiga.", tr="Ma’am, listen carefully to the notice on the radio.", lemma="oír:usted:cmd"),
        M("What is the usted command of decir?", "diga", ["dice", "deca", "dija"], "Digo → diga."),
        M("Why is it “traiga” and not “traya”?", "Because the yo form is traigo", ["Because it is a regular verb", "Because it is a reflexive verb", "Because it is a plural command"], "The command keeps the irregularity of the yo form."),
    ],
    verify=(vpc("decir", "diga", "digan") + vpc("hacer", "haga", "hagan") + vpc("oír", "oiga", "oigan")
            + vpc("poner", "ponga", "pongan") + vpc("salir", "salga", "salgan") + vpc("tener", "tenga", "tengan")
            + vpc("traer", "traiga", "traigan") + vpc("venir", "venga", "vengan")),
)

# ---------------------------------------------------------------------------- 438
L438 = lesson(
    "Formal commands: stem-changing verbs",
    "Piense con calma. Pida ayuda. Vuelva después.",
    requires=["pensar", "encender", "pedir", "repetir", "volver", "comprobar", "temblar", "cerrar", "ayuda", "radio"],
    cards=[
        card("Boots stay in the command",
             "A verb with a stem change in the present (ie, ue, i) keeps it in the usted and ustedes commands. It does not appear in the nosotros command of -ar and -er verbs, but you will see that later.",
             tables=[table(["Infinitivo", "yo", "usted", "ustedes"],
                           [["pensar (ie)", "pienso", "piense", "piensen"],
                            ["encender (ie)", "enciendo", "encienda", "enciendan"],
                            ["cerrar (ie)", "cierro", "cierre", "cierren"],
                            ["pedir (i)", "pido", "pida", "pidan"],
                            ["repetir (i)", "repito", "repita", "repitan"],
                            ["volver (ue)", "vuelvo", "vuelva", "vuelvan"],
                            ["comprobar (ue)", "compruebo", "compruebe", "comprueben"],
                            ["temblar (ie)", "tiemblo", "tiemble", "tiemblen"]],
                           say=[2, 3])]),
    ],
    exercises=[
        F("Señora, ___ con calma y salga ordenadamente.", "piense", ["piensa", "pensar", "piensen"], "Pensar → piense.", tr="Ma’am, think calmly and leave in an orderly way.", lemma="pensar:usted:cmd"),
        F("Señores, ___ la radio para escuchar las noticias.", "enciendan", ["encienden", "encender", "encienda"], "Encender → enciendan.", tr="Ladies and gentlemen, turn on the radio to listen to the news.", lemma="encender:ustedes:cmd"),
        F("Señor, ___ ayuda a los bomberos.", "pida", ["pide", "pedir", "pidan"], "Pedir → pida.", tr="Sir, ask the firefighters for help.", lemma="pedir:usted:cmd"),
        F("Señora, ___ si ya tenemos luz.", "compruebe", ["comprueba", "comprobar", "comprueben"], "Comprobar → compruebe.", tr="Ma’am, check whether we already have power.", lemma="comprobar:usted:cmd"),
        F("Señores, no ___ a la zona del desastre.", "vuelvan", ["vuelven", "volver", "vuelva"], "Volver → vuelvan.", tr="Ladies and gentlemen, do not go back to the disaster zone.", lemma="volver:ustedes:cmd"),
        F("Señor, no ___ de miedo; todo está controlado.", "tiemble", ["tiembla", "temblar", "tiemblen"], "Temblar → tiemble.", tr="Sir, do not tremble with fear; everything is under control.", lemma="temblar:usted:cmd"),
        F("Señora, ___ las ventanas antes de salir.", "cierre", ["cierra", "cerrar", "cierren"], "Cerrar → cierre.", tr="Ma’am, close the windows before you leave.", lemma="cerrar:usted:cmd"),
        M("What is the usted command of repetir?", "repita", ["repite", "repete", "repeta"], "Repito → repita."),
        M("What happens to the stem of volver in the command?", "It keeps the ue: vuelva", ["It becomes i: volva", "It disappears: volva", "It becomes e: vuelva"], "Ue stays."),
    ],
    verify=(vpc("pensar", "piense", "piensen") + vpc("encender", "encienda", "enciendan") + vpc("cerrar", "cierre", "cierren")
            + vpc("pedir", "pida", "pidan") + vpc("repetir", "repita", "repitan") + vpc("volver", "vuelva", "vuelvan")
            + vpc("comprobar", "compruebe", "comprueben") + vpc("temblar", "tiemble", "tiemblen")),
)

# ---------------------------------------------------------------------------- 439
L439 = lesson(
    "Formal commands: ser, estar, dar, ir, saber",
    "Sea paciente. Esté atento. Dé la alerta. Vaya al refugio.",
    requires=["ser", "estar", "dar", "ir", "saber", "paciente", "atento", "refugio", "alerta", "salida"],
    cards=[
        card("Five verbs that follow no pattern",
             "These five verbs have commands you must memorize. Note the accent mark on dé (to tell it apart from the preposition de) and on esté and estén.",
             tables=[table(["Infinitivo", "usted", "ustedes", "English"],
                           [["ser", "sea", "sean", "be"],
                            ["estar", "esté", "estén", "be (somewhere / in a state)"],
                            ["dar", "dé", "den", "give"],
                            ["ir", "vaya", "vayan", "go"],
                            ["saber", "sepa", "sepan", "know"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Señora, ___ paciente: el equipo de rescate llegará pronto.", "sea", ["es", "ser", "sean"], "Ser → sea.", tr="Ma’am, be patient: the rescue team will arrive soon.", lemma="ser:usted:cmd"),
        F("Señores, ___ atentos a la radio.", "estén", ["están", "estar", "esté"], "Estar → estén.", tr="Ladies and gentlemen, stay alert to the radio.", lemma="estar:ustedes:cmd"),
        F("Señor, ___ la alerta a sus vecinos.", "dé", ["da", "de", "dar"], "Dar → dé (with an accent).", tr="Sir, give the alert to your neighbors.", lemma="dar:usted:cmd"),
        F("Señores, ___ una linterna a cada familia.", "den", ["dan", "dar", "dé"], "Dar → den.", tr="Ladies and gentlemen, give a flashlight to each family.", lemma="dar:ustedes:cmd"),
        F("Señora, ___ al refugio por la calle principal.", "vaya", ["va", "ir", "vayan"], "Ir → vaya.", tr="Ma’am, go to the shelter by the main street.", lemma="ir:usted:cmd"),
        F("Señores, ___ dónde está la salida más cercana.", "sepan", ["saben", "saber", "sepa"], "Saber → sepan.", tr="Ladies and gentlemen, know where the nearest exit is.", lemma="saber:ustedes:cmd"),
        M("Why does the usted command of dar have an accent?", "To tell it apart from the preposition de", ["Because it is plural", "Because it is a question", "Because it is a past tense"], "Dé vs. de."),
        M("What is the ustedes command of ir?", "vayan", ["van", "vaya", "iren"], "Ir → vayan."),
        M("What is the usted command of ser?", "sea", ["sé", "es", "sera"], "Ser → sea."),
    ],
    verify=(vpc("ser", "sea", "sean") + vpc("estar", "esté", "estén") + vpc("dar", "dé", "den")
            + vpc("ir", "vaya", "vayan") + vpc("saber", "sepa", "sepan")),
)

# ---------------------------------------------------------------------------- 440
L440 = lesson(
    "Negative formal commands: what not to do",
    "No use el ascensor. No toque los cables. No corra.",
    requires=["usar", "tocar", "correr", "ascensor", "cable", "salir", "gritar", "empujar", "volver", "peligro"],
    cards=[
        card("No + the command",
             "To say what not to do, put no in front of the command. Everything else is the same: the same stem changes, the same spelling changes. Safety posters are full of these.",
             tables=[table(["Cartel de seguridad", "English"],
                           [["No use el ascensor.", "Do not use the elevator."],
                            ["No toque los cables.", "Do not touch the cables."],
                            ["No corra.", "Do not run."],
                            ["No grite.", "Do not shout."],
                            ["No empuje a los demás.", "Do not push others."],
                            ["No vuelva a la zona de peligro.", "Do not go back to the danger zone."]],
                           say=[0])]),
    ],
    exercises=[
        F("Durante un terremoto, señora, no ___ el ascensor.", "use", ["usa", "usar", "usen"], "Negative command: no + use.", tr="During an earthquake, do not use the elevator.", lemma="usar:usted:cmd"),
        F("Señora, no ___ los cables caídos.", "toque", ["toca", "tocar", "toquen"], "Tocar → toque (c → qu).", tr="Ma’am, do not touch the fallen cables.", lemma="tocar:usted:cmd"),
        F("Señores, no ___ por las escaleras.", "corran", ["corren", "correr", "corra"], "Correr → corran.", tr="Ladies and gentlemen, do not run on the stairs.", lemma="correr:ustedes:cmd"),
        F("Señor, no ___ a los demás; hay espacio para todos.", "empuje", ["empuja", "empujar", "empujen"], "Empujar → empuje.", tr="Sir, do not push others; there is room for everyone.", lemma="empujar:usted:cmd"),
        F("Señores, no ___ a la zona de peligro.", "vuelvan", ["vuelven", "volver", "vuelva"], "Volver → vuelvan.", tr="Ladies and gentlemen, do not go back to the danger zone.", lemma="volver:ustedes:cmd"),
        F("Señora, no ___ la luz hasta que revisen el gas.", "encienda", ["enciende", "encender", "enciendan"], "Encender → encienda.", tr="Ma’am, do not turn on the light until they check the gas.", lemma="encender:usted:cmd"),
        M("How do you say “Do not shout” to one person you address as usted?", "No grite.", ["No gritar.", "No grita.", "Gritar no."], "No + grite."),
        M("Where does no go?", "Before the command", ["After the command", "At the end of the sentence", "It is not used"], "No grite."),
        M("Which one is a correct negative command for ustedes?", "No toquen los cables.", ["No toca los cables.", "No tocar los cables.", "Toquen no los cables."], "Toquen."),
    ],
    verify=(vpc("usar", "use", "usen") + vpc("tocar", "toque", "toquen") + vpc("correr", "corra", "corran")
            + vpc("empujar", "empuje", "empujen") + vpc("encender", "encienda", "enciendan")),
)

# ---------------------------------------------------------------------------- 441
L441 = lesson(
    "Formal commands with pronouns",
    "Désela. Cúbrase la cabeza. No se la dé. No se cubra.",
    requires=["dar", "cubrir", "cabeza", "poner", "chaqueta", "tormenta", "apagar", "luz", "decir", "trabajador"],
    cards=[
        card("Attach after, place before",
             "In an affirmative command, pronouns attach to the end of the verb, and a written accent mark keeps the stress where it was. "
             "In a negative command, they stand in front of the verb, as always. "
             "With two pronouns, indirect comes first (se, me, te, le) and direct second (lo, la, los, las); le and les become se.",
             tables=[table(["Afirmativo", "Negativo", "English"],
                           [["Cúbrase la cabeza.", "No se cubra la cabeza.", "Cover your head."],
                            ["Póngase una chaqueta.", "No se ponga la chaqueta.", "Put on a jacket."],
                            ["Apáguela.", "No la apague.", "Turn it off."],
                            ["Désela.", "No se la dé.", "Give it to him."],
                            ["Dígame.", "No me diga.", "Tell me."],
                            ["Tráigamelos.", "No me los traiga.", "Bring them to me."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Durante el temblor, ___ la cabeza con los brazos.", "cúbrase", ["se cubra", "cubra se", "cúbra"], "Affirmative: attach se and accent the stressed syllable.", tr="During the quake, cover your head with your arms."),
        F("Hace frío: ___ una chaqueta, por favor.", "póngase", ["se ponga", "ponga se", "pongase"], "Affirmative: attach se and add the accent.", tr="It is cold: put on a jacket, please."),
        F("La luz, señora, ___ antes de salir.", "apáguela", ["la apague", "apague la", "apagúela"], "Affirmative: attach la and add the accent.", tr="The light, ma’am, turn it off before leaving."),
        F("Los cables, señor, no ___ toque.", "los", ["lo", "las", "se"], "Cables is masculine plural.", tr="The cables, sir, do not touch them."),
        F("La linterna, señora, ___ al equipo de rescate.", "désela", ["se la dé", "déla se", "dársela"], "Affirmative: attach both pronouns: désela.", tr="The flashlight, ma’am, give it to the rescue team."),
        F("La noticia, señor, no ___ diga a los niños todavía.", "se la", ["le la", "la se", "me la"], "Le + la → se la.", tr="The news, sir, do not tell it to the children yet."),
        M("Why does “cúbrase” have an accent mark?", "To keep the stress on the same syllable", ["Because it is a question", "Because it is plural", "Because it is feminine"], "Accent keeps the original stress."),
        M("Which pronoun goes first with two pronouns?", "the indirect: se la", ["the direct: la se", "either one", "neither"], "Indirect before direct."),
        M("Which sentence is correct?", "No se lo dé.", ["Dése no lo.", "No dése lo.", "No lo se dé."], "Negative: pronouns before the verb."),
    ],
)

# ---------------------------------------------------------------------------- 442
L442 = lesson(
    "Safety instructions: before an earthquake",
    "Prepare un kit de emergencia y practique el simulacro con su familia.",
    requires=["preparar", "practicar", "identificar", "fijar", "guardar", "agua", "comida", "medicina", "documento", "familia", "mueble", "salida"],
    cards=[
        card("Prepare ahead",
             "Public safety leaflets give orders to the reader as usted or ustedes. Read these before-the-quake instructions, then use the same forms in the exercises.",
             tables=[table(["Antes del terremoto", "English"],
                           [["Prepare un kit de emergencia.", "Prepare an emergency kit."],
                            ["Guarde agua y comida para varios días.", "Store water and food for several days."],
                            ["Identifique las salidas de su casa.", "Identify the exits of your home."],
                            ["Fije los muebles pesados a la pared.", "Fasten heavy furniture to the wall."],
                            ["Practique el simulacro con su familia.", "Practice the drill with your family."],
                            ["Tenga copias de sus documentos.", "Keep copies of your documents."]],
                           say=[0])]),
    ],
    exercises=[
        F("Señora, ___ un kit de emergencia para su familia.", "prepare", ["prepara", "preparar", "preparen"], "Usted command of preparar.", tr="Ma’am, prepare an emergency kit for your family.", lemma="preparar:usted:cmd"),
        F("Señor, ___ agua y comida para varios días.", "guarde", ["guarda", "guardar", "guarden"], "Usted command of guardar.", tr="Sir, store water and food for several days.", lemma="guardar:usted:cmd"),
        F("Señores, ___ las salidas de su edificio.", "identifiquen", ["identifican", "identificar", "identifique"], "Ustedes command; c → qu.", tr="Ladies and gentlemen, identify the exits of your building.", lemma="identificar:ustedes:cmd"),
        F("Señora, ___ los muebles pesados a la pared.", "fije", ["fija", "fijar", "fijen"], "Usted command of fijar.", tr="Ma’am, fasten the heavy furniture to the wall.", lemma="fijar:usted:cmd"),
        F("Señores, ___ el simulacro con sus hijos.", "practiquen", ["practican", "practicar", "practique"], "Ustedes command; c → qu.", tr="Ladies and gentlemen, practice the drill with your children.", lemma="practicar:ustedes:cmd"),
        F("Señor, ___ copias de sus documentos.", "tenga", ["tiene", "tener", "tengan"], "Usted command of tener.", tr="Sir, keep copies of your documents.", lemma="tener:usted:cmd"),
        M("Why store water and food before an earthquake?", "Help may not arrive for days", ["To sell them later", "Because the water will disappear", "To avoid shopping forever"], "Para varios días."),
        M("Why fasten heavy furniture to the wall?", "So it does not fall during the shaking", ["To make the room look bigger", "To keep it clean", "To hide it"], "Para que no se caiga."),
        M("Which command is for a group?", "Practiquen el simulacro.", ["Practique el simulacro.", "Practica el simulacro.", "Practico el simulacro."], "-n = ustedes."),
    ],
    verify=(vpc("preparar", "prepare", "preparen") + vpc("guardar", "guarde", "guarden") + vpc("identificar", "identifique", "identifiquen")
            + vpc("fijar", "fije", "fijen") + vpc("practicar", "practique", "practiquen") + vpc("tener", "tenga", "tengan")),
)

# ---------------------------------------------------------------------------- 443
L443 = lesson(
    "Safety instructions: during an earthquake",
    "Mantenga la calma, protéjase y aléjese de las ventanas.",
    requires=["mantener", "calma", "proteger", "alejar", "ventana", "mesa", "debajo", "cabeza", "edificio", "salir", "caer"],
    cards=[
        card("When the ground shakes",
             "During an earthquake the orders are short and direct. Notice that protéjase and aléjese are reflexive commands, with se attached and an accent.",
             tables=[table(["Durante el terremoto", "English"],
                           [["Mantenga la calma.", "Stay calm."],
                            ["Protéjase debajo de una mesa resistente.", "Take cover under a strong table."],
                            ["Cúbrase la cabeza y el cuello.", "Cover your head and neck."],
                            ["Aléjese de las ventanas.", "Stay away from the windows."],
                            ["No use el ascensor.", "Do not use the elevator."],
                            ["Si está afuera, aléjese de los edificios.", "If you are outside, move away from buildings."]],
                           say=[0])]),
    ],
    exercises=[
        F("Señora, ___ la calma durante el temblor.", "mantenga", ["mantiene", "mantener", "mantengan"], "Mantener → mantenga.", tr="Ma’am, stay calm during the tremor.", lemma="mantener:usted:cmd"),
        F("Señores, ___ debajo de una mesa resistente.", "protéjanse", ["protegen", "protéjase", "proteger"], "Reflexive ustedes command.", tr="Ladies and gentlemen, take cover under a strong table."),
        F("Señor, ___ de las ventanas.", "aléjese", ["aleja", "alejarse", "alejen"], "Reflexive usted command: aléjese.", tr="Sir, move away from the windows."),
        F("Señora, ___ la cabeza y el cuello con las manos.", "cúbrase", ["cubre", "cubrirse", "cúbranse"], "Reflexive usted command: cúbrase.", tr="Ma’am, cover your head and neck with your hands."),
        F("Señores, ___ por las escaleras, no por el ascensor.", "bajen", ["bajan", "bajar", "baje"], "Ustedes command of bajar.", tr="Ladies and gentlemen, go down by the stairs, not by the elevator.", lemma="bajar:ustedes:cmd"),
        F("Señor, si está afuera, ___ de los edificios.", "aléjese", ["aleja", "alejarse", "alejen"], "Reflexive usted command.", tr="Sir, if you are outside, move away from buildings."),
        M("What should you do with your head during the quake?", "Cover it", ["Lift it", "Ignore it", "Move it quickly"], "Cúbrase la cabeza."),
        M("Where should you take cover?", "Under a strong table", ["Next to a window", "In the elevator", "On the balcony"], "Debajo de una mesa resistente."),
        M("Why do protéjase and aléjese have accents?", "Because the pronoun was attached", ["Because they are plural", "Because they are questions", "Because they are past tense"], "Accent keeps the stress."),
    ],
    verify=(vpc("mantener", "mantenga", "mantengan") + vpc("bajar", "baje", "bajen")),
)

# ---------------------------------------------------------------------------- 444
L444 = lesson(
    "Safety instructions: after a disaster",
    "Revise si hay heridos. No entre en edificios dañados.",
    requires=["revisar", "entrar", "cerrar", "escuchar", "llamar", "esperar", "ayudar", "herido", "gas", "radio", "edificio", "emergencia"],
    cards=[
        card("When the shaking stops",
             "After a disaster the first minutes matter. These are the standard instructions: check for injuries, stay out of damaged buildings, and listen to the authorities.",
             tables=[table(["Después del desastre", "English"],
                           [["Revise si hay heridos.", "Check whether anyone is injured."],
                            ["No entre en edificios dañados.", "Do not enter damaged buildings."],
                            ["Cierre la llave del gas.", "Close the gas valve."],
                            ["Escuche la radio.", "Listen to the radio."],
                            ["Use el teléfono solo para emergencias.", "Use the phone only for emergencies."],
                            ["Espere las instrucciones de las autoridades.", "Wait for instructions from the authorities."]],
                           say=[0])]),
    ],
    exercises=[
        F("Señora, ___ si hay heridos en su familia.", "revise", ["revisa", "revisar", "revisen"], "Usted command of revisar.", tr="Ma’am, check whether anyone in your family is injured.", lemma="revisar:usted:cmd"),
        F("Señores, no ___ en edificios dañados.", "entren", ["entran", "entrar", "entre"], "Ustedes negative command.", tr="Ladies and gentlemen, do not enter damaged buildings.", lemma="entrar:ustedes:cmd"),
        F("Señor, ___ la llave del gas.", "cierre", ["cierra", "cerrar", "cierren"], "Usted command of cerrar.", tr="Sir, close the gas valve.", lemma="cerrar:usted:cmd"),
        F("Señora, ___ la radio para saber qué hacer.", "escuche", ["escucha", "escuchar", "escuchen"], "Usted command of escuchar.", tr="Ma’am, listen to the radio to know what to do.", lemma="escuchar:usted:cmd"),
        F("Señores, ___ a la policía si necesitan ayuda.", "llamen", ["llaman", "llamar", "llame"], "Ustedes command of llamar.", tr="Ladies and gentlemen, call the police if you need help.", lemma="llamar:ustedes:cmd"),
        F("Señor, ___ las instrucciones de las autoridades.", "espere", ["espera", "esperar", "esperen"], "Usted command of esperar.", tr="Sir, wait for instructions from the authorities.", lemma="esperar:usted:cmd"),
        M("Why close the gas valve after an earthquake?", "A broken pipe could leak gas", ["To save money", "To stop the rain", "To open the door"], "Prevenir una fuga."),
        M("What is the phone for after a disaster?", "Emergencies only", ["Long calls with friends", "Online games", "Shopping"], "Solo para emergencias."),
        M("Which one is a negative command for ustedes?", "No entren.", ["No entran.", "No entrar.", "Entren no."], "No + entren."),
    ],
    verify=(vpc("revisar", "revise", "revisen") + vpc("entrar", "entre", "entren") + vpc("cerrar", "cierre", "cierren")
            + vpc("escuchar", "escuche", "escuchen") + vpc("llamar", "llame", "llamen") + vpc("esperar", "espere", "esperen")),
)

# ---------------------------------------------------------------------------- 445
L445 = lesson(
    "Hurricane preparedness",
    "Llene el tanque de gasolina y guarde sus documentos en una bolsa.",
    requires=["llenar", "guardar", "seguir", "evitar", "llevar", "tanque", "gasolina", "documento", "bolsa", "agua", "pila", "radio", "batería"],
    cards=[
        card("Before the storm arrives",
             "Hurricane season lets people prepare. These instructions are typical of a civil-protection notice.",
             tables=[table(["Antes del huracán", "English"],
                           [["Llene el tanque de gasolina.", "Fill the gas tank."],
                            ["Guarde sus documentos en una bolsa.", "Keep your documents in a bag."],
                            ["Tenga pilas y una radio.", "Have batteries and a radio."],
                            ["Cargue la batería del teléfono.", "Charge your phone battery."],
                            ["Siga las instrucciones de las autoridades.", "Follow the authorities’ instructions."],
                            ["Evite las zonas bajas cerca del mar.", "Avoid low areas near the sea."]],
                           say=[0])]),
    ],
    exercises=[
        F("Señor, ___ el tanque de gasolina antes de la tormenta.", "llene", ["llena", "llenar", "llenen"], "Usted command of llenar.", tr="Sir, fill the gas tank before the storm.", lemma="llenar:usted:cmd"),
        F("Señora, ___ sus documentos en una bolsa cerrada.", "guarde", ["guarda", "guardar", "guarden"], "Usted command of guardar.", tr="Ma’am, keep your documents in a sealed bag.", lemma="guardar:usted:cmd"),
        F("Señores, ___ las instrucciones de las autoridades.", "sigan", ["siguen", "seguir", "siga"], "Seguir → sigan.", tr="Ladies and gentlemen, follow the authorities’ instructions.", lemma="seguir:ustedes:cmd"),
        F("Señora, ___ las zonas bajas cerca del mar.", "evite", ["evita", "evitar", "eviten"], "Usted command of evitar.", tr="Ma’am, avoid the low areas near the sea.", lemma="evitar:usted:cmd"),
        F("Señor, ___ pilas y una radio en casa.", "tenga", ["tiene", "tener", "tengan"], "Tener → tenga.", tr="Sir, keep batteries and a radio at home.", lemma="tener:usted:cmd"),
        F("Señores, ___ agua para tres días por persona.", "lleven", ["llevan", "llevar", "lleve"], "Ustedes command of llevar.", tr="Ladies and gentlemen, bring water for three days per person.", lemma="llevar:ustedes:cmd"),
        M("Why keep documents in a sealed bag?", "To protect them from water", ["To hide them", "To weigh them", "To print them"], "Bolsa cerrada."),
        M("Why avoid low areas near the sea?", "They flood first", ["They are too hot", "They have no roads", "They are noisy"], "Zonas bajas."),
        M("What is the formal command of seguir?", "siga", ["sigue", "seguía", "segue"], "Sigo → siga."),
    ],
    verify=(vpc("llenar", "llene", "llenen") + vpc("guardar", "guarde", "guarden") + vpc("seguir", "siga", "sigan")
            + vpc("evitar", "evite", "eviten") + vpc("llevar", "lleve", "lleven")),
)

# ---------------------------------------------------------------------------- 446
L446 = lesson(
    "Safety at home: fire and electricity",
    "Desenchufe los aparatos. No sobrecargue los enchufes.",
    requires=["apagar", "llamar", "salir", "cable", "aparato", "bombero", "fuego", "humo", "luz", "puerta", "tocar", "usar"],
    cards=[
        card("Preventing and responding",
             "Many house fires start with electricity or the kitchen. These are the standard rules in a home-safety poster.",
             tables=[table(["En casa", "English"],
                           [["Desenchufe los aparatos que no usa.", "Unplug the appliances you are not using."],
                            ["No toque cables dañados.", "Do not touch damaged cables."],
                            ["No deje la estufa encendida sin vigilancia.", "Do not leave the stove on unattended."],
                            ["Si hay humo, salga de la casa.", "If there is smoke, get out of the house."],
                            ["Cierre las puertas al salir.", "Close doors as you leave."],
                            ["Llame a los bomberos desde afuera.", "Call the firefighters from outside."]],
                           say=[0])]),
    ],
    exercises=[
        F("Señora, ___ los aparatos que no usa.", "desenchufe", ["desenchufa", "desenchufar", "desenchufen"], "Usted command of desenchufar.", tr="Ma’am, unplug the appliances you are not using.", lemma="desenchufar:usted:cmd"),
        F("Señor, no ___ cables dañados.", "toque", ["toca", "tocar", "toquen"], "Negative usted command.", tr="Sir, do not touch damaged cables.", lemma="tocar:usted:cmd"),
        F("Señora, si hay humo, ___ de la casa.", "salga", ["sale", "salir", "salgan"], "Salir → salga.", tr="Ma’am, if there is smoke, get out of the house.", lemma="salir:usted:cmd"),
        F("Señores, ___ las puertas al salir.", "cierren", ["cierran", "cerrar", "cierre"], "Ustedes command of cerrar.", tr="Ladies and gentlemen, close the doors as you leave.", lemma="cerrar:ustedes:cmd"),
        F("Señor, ___ a los bomberos desde afuera.", "llame", ["llama", "llamar", "llamen"], "Usted command of llamar.", tr="Sir, call the firefighters from outside.", lemma="llamar:usted:cmd"),
        F("Señora, no ___ la estufa encendida sin vigilancia.", "deje", ["deja", "dejar", "dejen"], "Negative usted command of dejar.", tr="Ma’am, do not leave the stove on unattended.", lemma="dejar:usted:cmd"),
        M("Where should you call the firefighters from?", "From outside", ["From inside the burning room", "From the kitchen", "From the roof"], "Desde afuera."),
        M("Why unplug appliances?", "To avoid electrical fires", ["To save space", "To make noise", "To make them heavier"], "Evitar incendios."),
        M("What do you do if there is smoke?", "Get out of the house", ["Open every window and stay", "Turn the lights off and sleep", "Look for the cause first"], "Salga de la casa."),
    ],
    verify=(vpc("desenchufar", "desenchufe", "desenchufen") + vpc("tocar", "toque", "toquen") + vpc("salir", "salga", "salgan")
            + vpc("cerrar", "cierre", "cierren") + vpc("llamar", "llame", "llamen") + vpc("dejar", "deje", "dejen")),
)

# ---------------------------------------------------------------------------- 447
L447 = lesson(
    "Commands with nosotros: “let’s…”",
    "Visitemos el museo. Hagamos la tarea. Pidamos ayuda.",
    requires=["visitar", "bailar", "hacer", "pedir", "leer", "ayudar", "museo", "tarea", "ayuda", "hoy"],
    cards=[
        card("Forming the “let’s” command",
             "Start with the yo form of the present, drop the -o, and add -emos for -ar verbs and -amos for -er and -ir verbs. "
             "The affirmative and negative are the same: Visitemos el museo. No visitemos el museo. "
             "-ar and -er verbs with a stem change in the present do not change here (pensemos, volvamos), but -ir verbs do change (pidamos, durmamos).",
             tables=[table(["Infinitivo", "yo", "nosotros"],
                           [["bailar", "bailo", "bailemos"],
                            ["visitar", "visito", "visitemos"],
                            ["ayudar", "ayudo", "ayudemos"],
                            ["leer", "leo", "leamos"],
                            ["hacer", "hago", "hagamos"],
                            ["pedir", "pido", "pidamos"],
                            ["buscar", "busco", "busquemos"],
                            ["pagar", "pago", "paguemos"]],
                           say=[2])]),
    ],
    exercises=[
        F("Hoy mismo, ___ a las víctimas del terremoto.", "ayudemos", ["ayudémos", "ayudiemos", "ayudeamos"], "Nosotros command of ayudar.", tr="Today, let’s help the earthquake victims.", lemma="ayudar:nosotros:ncmd"),
        F("Es sábado: ___ el museo de la ciudad.", "visitemos", ["visitémos", "visitiemos", "visiteamos"], "Nosotros command of visitar.", tr="It is Saturday: let’s visit the city museum.", lemma="visitar:nosotros:ncmd"),
        F("Tenemos mucha tarea: ___ la tarea juntos.", "hagamos", ["hacamos", "hagámos", "hagiamos"], "Hacer → hagamos (from hago).", tr="We have a lot of homework: let’s do it together.", lemma="hacer:nosotros:ncmd"),
        F("No entendemos: ___ ayuda a la maestra.", "pidamos", ["pedamos", "pidémos", "pidiamos"], "Pedir → pidamos.", tr="We do not understand: let’s ask the teacher for help.", lemma="pedir:nosotros:ncmd"),
        F("Quiero saber más: ___ el artículo sobre el huracán.", "leamos", ["leyamos", "leémos", "leiamos"], "Leer → leamos.", tr="I want to know more: let’s read the article about the hurricane.", lemma="leer:nosotros:ncmd"),
        F("Perdimos las llaves: ___ en el patio.", "busquemos", ["buscemos", "busquémos", "busqueamos"], "Buscar → busquemos (c → qu).", tr="We lost the keys: let’s look in the yard.", lemma="buscar:nosotros:ncmd"),
        F("Por favor, ___ la cuenta ahora.", "paguemos", ["pagemos", "paguémos", "paguiemos"], "Pagar → paguemos (g → gu).", tr="Please, let’s pay the bill now.", lemma="pagar:nosotros:ncmd"),
        M("Which ending do -ar verbs take in the nosotros command?", "-emos", ["-amos", "-imos", "-ando"], "Visitemos."),
        M("Is the negative different from the affirmative?", "No, the nosotros form is the same", ["Yes, it changes to -amos", "Yes, it changes to -ando", "Yes, it is not used"], "Visitemos / No visitemos."),
    ],
    verify=(vpn("bailar", "bailemos") + vpn("visitar", "visitemos") + vpn("ayudar", "ayudemos") + vpn("leer", "leamos")
            + vpn("hacer", "hagamos") + vpn("pedir", "pidamos") + vpn("buscar", "busquemos") + vpn("pagar", "paguemos")),
)

# ---------------------------------------------------------------------------- 448
L448 = lesson(
    "Nosotros commands: irregular verbs and -ir stem changes",
    "Seamos responsables. Estemos listos. Durmamos temprano.",
    requires=["ser", "estar", "dar", "ir", "saber", "dormir", "pedir", "repetir", "sentir", "servir", "responsable", "listo"],
    cards=[
        card("Verbs to memorize",
             "Five verbs have irregular nosotros commands, the same stems as the usted commands: seamos, estemos, demos, vayamos, sepamos. "
             "-ir verbs with a stem change in the present have a change in the nosotros command too: e→i and o→u. "
             "For “let’s go” people usually use vamos (affirmative), and no vayamos (negative); vayamos also appears in formal speech.",
             tables=[table(["Infinitivo", "nosotros"],
                           [["ser", "seamos"],
                            ["estar", "estemos"],
                            ["dar", "demos"],
                            ["ir", "vayamos"],
                            ["saber", "sepamos"],
                            ["dormir", "durmamos"],
                            ["pedir", "pidamos"],
                            ["repetir", "repitamos"],
                            ["sentir", "sintamos"],
                            ["servir", "sirvamos"]],
                           say=[1])]),
    ],
    exercises=[
        F("Por favor, ___ responsables con la naturaleza.", "seamos", ["semos", "seémos", "seamo"], "Ser → seamos.", tr="Please, let’s be responsible with nature.", lemma="ser:nosotros:ncmd"),
        F("En caso de alerta, ___ listos para salir.", "estemos", ["estémos", "estiemos", "estaemos"], "Estar → estemos.", tr="In case of an alert, let’s be ready to leave.", lemma="estar:nosotros:ncmd"),
        F("Con generosidad, ___ comida a los damnificados.", "demos", ["démos", "deamos", "demo"], "Dar → demos (no accent).", tr="Let’s generously give food to those affected.", lemma="dar:nosotros:ncmd"),
        F("Antes de decidir, ___ toda la verdad.", "sepamos", ["sabamos", "sepámos", "supamos"], "Saber → sepamos.", tr="Before deciding, let’s find out the whole truth.", lemma="saber:nosotros:ncmd"),
        F("Mañana hay que madrugar: ___ temprano esta noche.", "durmamos", ["dormamos", "durmámos", "duermamos"], "Dormir → durmamos.", tr="Tomorrow we have to get up early: let’s sleep early tonight.", lemma="dormir:nosotros:ncmd"),
        F("No oímos bien: ___ la pregunta, por favor.", "repitamos", ["repetamos", "repitámos", "repitiemos"], "Repetir → repitamos.", tr="We did not hear well: let’s repeat the question, please.", lemma="repetir:nosotros:ncmd"),
        F("Para salir de aquí, ___ por esta puerta.", "vamos", ["vayemos", "vamo", "vémos"], "Affirmative “let’s go”: vamos.", tr="To leave here, let’s go through this door."),
        M("What is the nosotros command of ser?", "seamos", ["somos", "serimos", "seremos"], "Ser → seamos."),
        M("How do you say “Let’s not go” in this form?", "No vayamos", ["No vamos", "No iremos", "No ir"], "Negative of ir: vayamos."),
    ],
    verify=(vpn("ser", "seamos") + vpn("estar", "estemos") + vpn("dar", "demos") + vpn("ir", "vayamos") + vpn("saber", "sepamos")
            + vpn("dormir", "durmamos") + vpn("pedir", "pidamos") + vpn("repetir", "repitamos") + vpn("sentir", "sintamos")
            + vpn("servir", "sirvamos")),
)

# ---------------------------------------------------------------------------- 449
L449 = lesson(
    "Nosotros commands with pronouns: hagámoslo, levantémonos",
    "Hagámoslo ahora. No lo hagamos. Levantémonos temprano.",
    requires=["hacer", "decir", "levantar", "lavar", "sentar", "mano", "temprano", "verdad", "jefe", "ahora"],
    cards=[
        card("Attach after, place before",
             "As with the usted command, pronouns attach to an affirmative nosotros command with an accent on the stressed syllable, and go in front of a negative one. "
             "The final -s of the verb is dropped before nos or se (reflexive nos or se, or se replacing le/les): levantemos + nos → levantémonos; digamos + se + lo → digámoselo. "
             "(Irregular: vamos + nos → vámonos.)",
             tables=[table(["Afirmativo", "Negativo", "English"],
                           [["Hagámoslo.", "No lo hagamos.", "Let’s do it."],
                            ["Digámoselo.", "No se lo digamos.", "Let’s tell it to him."],
                            ["Levantémonos temprano.", "No nos levantemos temprano.", "Let’s get up early."],
                            ["Lavémonos las manos.", "No nos lavemos las manos.", "Let’s wash our hands."],
                            ["Sentémonos aquí.", "No nos sentemos aquí.", "Let’s sit here."],
                            ["Vámonos.", "No nos vayamos.", "Let’s go."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Hay que hacerlo hoy: ___ ahora mismo.", "hagámoslo", ["lo hagamos", "hagamoslo", "hagamos lo"], "Attach lo and add the accent.", tr="It must be done today: let’s do it right now."),
        F("Mañana hay clase: ___ temprano.", "levantémonos", ["nos levantemos", "levantemosnos", "levantémosnos"], "Reflexive: drop the s before nos.", tr="Tomorrow there is class: let’s get up early."),
        F("Estamos sucios: ___ las manos.", "lavémonos", ["nos lavemos", "lavemosnos", "lavémosnos"], "Reflexive: drop the s before nos.", tr="We are dirty: let’s wash our hands."),
        F("No es buena idea: no ___ la verdad todavía.", "se la digamos", ["digámosela", "se la digámos", "le la digamos"], "Negative: pronouns before; le + la → se la.", tr="It is not a good idea: let’s not tell him the truth yet."),
        F("El jefe necesita saberlo: ___ hoy.", "digámoselo", ["se lo digamos", "digámolo", "digamoselo"], "Affirmative: attach se lo; drop the s from digamos.", tr="The boss needs to know: let’s tell him today."),
        F("Aquí hay sillas: ___ aquí un momento.", "sentémonos", ["nos sentemos", "sentamosnos", "sentémosnos"], "Reflexive: sentemos + nos → sentémonos.", tr="There are chairs here: let’s sit here for a moment."),
        M("What happens to the final s of the nosotros form before nos?", "It is dropped: levantémonos", ["It is doubled: levantemossnos", "It stays: levantémosnos", "It becomes z"], "Levantemos + nos."),
        M("Which one is the negative of “Hagámoslo”?", "No lo hagamos.", ["No hagámoslo.", "Hagamos no lo.", "No hagamos lo."], "Negative: pronoun before the verb."),
        M("Which sentence is correct for “Let’s go”?", "Vámonos.", ["Vamosnos.", "Vámosnos.", "Vamónos."], "Vamos + nos = vámonos."),
    ],
)

# ---------------------------------------------------------------------------- 450
L450 = lesson(
    "Let’s: nosotros command or vamos a?",
    "Vamos a limpiar la playa. Limpiemos la playa.",
    requires=["ir", "limpiar", "ayudar", "playa", "trabajar", "reunir", "organizar", "hoy"],
    cards=[
        card("Two ways to say “let’s…”",
             "In everyday speech, the usual way to suggest something is vamos a + infinitive. "
             "The nosotros command is more formal and is used in speeches, news articles, campaigns and books. "
             "Both mean the same; the register is different. Remember that vamos by itself means “let’s go”.",
             tables=[table(["En la conversación", "En un discurso o artículo"],
                           [["Vamos a limpiar la playa.", "Limpiemos la playa."],
                            ["Vamos a ayudar a las víctimas.", "Ayudemos a las víctimas."],
                            ["Vamos a organizar una colecta.", "Organicemos una colecta."],
                            ["Vamos a reunirnos mañana.", "Reunámonos mañana."],
                            ["Vamos al refugio.", "Vayamos al refugio."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Todos juntos, ___ a limpiar la playa.", "vamos", ["vamo", "vayemos", "vémos"], "Everyday: vamos a + infinitive.", tr="All together, let’s clean up the beach."),
        F("En el discurso, el alcalde dijo: «___ a las víctimas».", "ayudemos", ["ayudémos", "ayudiemos", "ayudeamos"], "Formal: nosotros command.", tr="In the speech, the mayor said: “Let’s help the victims.”", lemma="ayudar:nosotros:ncmd"),
        F("Con los amigos: «¡___ al refugio ahora!»", "vamos", ["vayemos", "vamo", "vémos"], "Vamos = let’s go.", tr="With friends: “Let’s go to the shelter now!”"),
        F("En la campaña, la ministra pidió: «___ el planeta».", "protejamos", ["protegamos", "protejámos", "protejemos"], "Formal: proteger → protejamos.", tr="In the campaign, the minister asked: “Let’s protect the planet.”", lemma="proteger:nosotros:ncmd"),
        F("Entre amigos: «___ a organizar una colecta».", "vamos", ["vamo", "vayemos", "vémos"], "Everyday: vamos a + infinitive.", tr="Among friends: “Let’s organize a collection.”"),
        F("En el artículo: «___ una colecta para los damnificados».", "organicemos", ["organizemos", "organicémos", "organiciemos"], "Formal: nosotros command (z → c).", tr="In the article: “Let’s organize a collection for those affected.”", lemma="organizar:nosotros:ncmd"),
        M("Which form is more common in everyday speech?", "vamos a + infinitive", ["the nosotros command", "the past perfect", "the conditional"], "Vamos a."),
        M("Where do you mostly find the nosotros command?", "In speeches, campaigns and articles", ["Only in chat messages", "Only in jokes", "Nowhere"], "Registro formal."),
        M("What does “¡Vamos!” mean by itself?", "Let’s go", ["I am going", "They are going", "You will go"], "Vamos."),
    ],
    verify=(vpn("ayudar", "ayudemos") + vpn("proteger", "protejamos") + vpn("organizar", "organicemos")),
)

# ---------------------------------------------------------------------------- 451
L451 = lesson(
    "A call to action: speeches and campaigns",
    "Conservemos los bosques. Protejamos los ríos. Seamos solidarios.",
    requires=["conservar", "proteger", "donar", "apagar", "sembrar", "cuidar", "ayudar", "ser", "río", "agua", "solidaridad", "futuro"],
    cards=[
        card("The voice of a campaign",
             "Environmental and relief campaigns use nosotros commands to speak as one with the audience. Read these slogans aloud.",
             tables=[table(["Lema", "English"],
                           [["Conservemos el agua.", "Let’s conserve water."],
                            ["Protejamos los ríos.", "Let’s protect the rivers."],
                            ["Sembremos un árbol cada año.", "Let’s plant a tree every year."],
                            ["Donemos comida y agua a los damnificados.", "Let’s donate food and water to those affected."],
                            ["Apaguemos las luces que no usamos.", "Let’s turn off the lights we are not using."],
                            ["Cuidemos nuestro planeta.", "Let’s take care of our planet."]],
                           say=[0])]),
    ],
    exercises=[
        F("Para el futuro de todos, ___ el agua.", "conservemos", ["conservémos", "conserviemos", "conserveamos"], "Nosotros command of conservar.", tr="For everyone’s future, let’s conserve water.", lemma="conservar:nosotros:ncmd"),
        F("Hoy, ___ comida y agua a los damnificados.", "donemos", ["donémos", "doniemos", "doneamos"], "Nosotros command of donar.", tr="Today, let’s donate food and water to those affected.", lemma="donar:nosotros:ncmd"),
        F("Para ahorrar energía, ___ las luces que no usamos.", "apaguemos", ["apagemos", "apaguémos", "apaguiemos"], "Apagar → apaguemos (g → gu).", tr="To save energy, let’s turn off the lights we are not using.", lemma="apagar:nosotros:ncmd"),
        F("Cada año, ___ un árbol.", "sembremos", ["siembremos", "sembrémos", "sembriemos"], "Sembrar → sembremos (no stem change).", tr="Every year, let’s plant a tree.", lemma="sembrar:nosotros:ncmd"),
        F("Por nuestros hijos, ___ nuestro planeta.", "cuidemos", ["cuidémos", "cuidiemos", "cuideamos"], "Nosotros command of cuidar.", tr="For our children, let’s take care of our planet.", lemma="cuidar:nosotros:ncmd"),
        F("Con solidaridad, ___ solidarios con los que sufren.", "seamos", ["semos", "seémos", "seamo"], "Ser → seamos.", tr="With solidarity, let’s be supportive of those who suffer.", lemma="ser:nosotros:ncmd"),
        M("Why do campaigns use the nosotros command?", "It includes the speaker and the audience", ["It is a command to one person", "It talks about the past", "It is only for questions"], "Nosotros = all of us."),
        M("What does “Sembremos un árbol” mean?", "Let’s plant a tree", ["I planted a tree", "They will plant a tree", "Plant a tree (to one person)"], "Sembrar."),
        M("Which one is a slogan?", "Cuidemos nuestro planeta.", ["Cuidaron su planeta.", "Cuidaré el planeta.", "Cuidas tu planeta."], "Nosotros command."),
    ],
    verify=(vpn("conservar", "conservemos") + vpn("donar", "donemos") + vpn("apagar", "apaguemos") + vpn("sembrar", "sembremos")
            + vpn("cuidar", "cuidemos")),
)

# ---------------------------------------------------------------------------- 452
L452 = lesson(
    "Review: formal commands",
    "Salga, no use el ascensor y llame a los bomberos.",
    requires=["salir", "usar", "llamar", "tener", "poner", "cerrar", "pedir", "ser", "ir", "dar", "bombero", "calma"],
    cards=[
        card("All the formal commands in a table",
             "Regular verbs use the opposite vowel; verbs irregular in the yo form keep the irregularity; stem-changing verbs keep their boot; five verbs follow no pattern; pronouns attach to affirmative commands and precede negative ones.",
             tables=[table(["Tipo", "usted", "ustedes"],
                           [["regular", "hable, coma, escriba", "hablen, coman, escriban"],
                            ["yo irregular", "salga, tenga, ponga, traiga", "salgan, tengan, pongan, traigan"],
                            ["boot", "piense, pida, vuelva", "piensen, pidan, vuelvan"],
                            ["irregulares", "sea, esté, dé, vaya, sepa", "sean, estén, den, vayan, sepan"],
                            ["con pronombre", "Tómelo. No lo tome.", "Tómenlo. No lo tomen."]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Señora, ___ de la casa y no use el ascensor.", "salga", ["sale", "salir", "salgan"], "Salir → salga.", tr="Ma’am, leave the house and do not use the elevator.", lemma="salir:usted:cmd"),
        F("Señores, ___ calma y sigan las instrucciones.", "tengan", ["tienen", "tener", "tenga"], "Tener → tengan.", tr="Ladies and gentlemen, stay calm and follow the instructions.", lemma="tener:ustedes:cmd"),
        F("Señor, ___ ayuda si la necesita.", "pida", ["pide", "pedir", "pidan"], "Pedir → pida.", tr="Sir, ask for help if you need it.", lemma="pedir:usted:cmd"),
        F("Señora, ___ paciente: ya vienen los bomberos.", "sea", ["es", "ser", "sean"], "Ser → sea.", tr="Ma’am, be patient: the firefighters are coming.", lemma="ser:usted:cmd"),
        F("Señores, ___ al refugio por la calle principal.", "vayan", ["van", "ir", "vaya"], "Ir → vayan.", tr="Ladies and gentlemen, go to the shelter by the main street.", lemma="ir:ustedes:cmd"),
        F("Señor, ___ esta información a sus vecinos.", "dé", ["da", "de", "dar"], "Dar → dé.", tr="Sir, give this information to your neighbors.", lemma="dar:usted:cmd"),
        F("Esa pastilla, señora, ___ con agua.", "tómela", ["la tome", "tome la", "tomela"], "Affirmative: attach la and add the accent.", tr="That pill, ma’am, take it with water."),
        F("Ese cable, señor, no ___ toque.", "lo", ["la", "los", "se"], "Cable is masculine singular.", tr="That cable, sir, do not touch it."),
        M("Which command is irregular in a way that must be memorized?", "dé", ["hable", "coma", "escriba"], "Dar → dé."),
        M("What is the usted command of poner?", "ponga", ["pone", "pona", "pon"], "Pongo → ponga."),
    ],
)

# ---------------------------------------------------------------------------- 453
L453 = lesson(
    "Review: nosotros commands",
    "Ayudemos, donemos y no perdamos la esperanza.",
    requires=["ayudar", "donar", "perder", "esperanza", "ser", "ir", "hacer", "pedir", "levantar", "limpiar", "reunir", "organizar"],
    cards=[
        card("Nosotros commands at a glance",
             "Regular forms use -emos for -ar verbs and -amos for -er and -ir verbs; verbs irregular in yo keep the change (hagamos, tengamos); -ir verbs change the stem (pidamos, durmamos); five verbs are irregular (seamos, estemos, demos, vayamos, sepamos); pronouns attach with an accent, and the -s drops before nos and se.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["regular -ar", "Ayudemos. Donemos."],
                            ["regular -er/-ir", "Comamos. Escribamos."],
                            ["yo irregular", "Hagamos. Tengamos paciencia."],
                            ["cambio en -ir", "Pidamos. Durmamos."],
                            ["irregulares", "Seamos. Vayamos."],
                            ["con pronombre", "Hagámoslo. Levantémonos."]],
                           say=[1])]),
    ],
    exercises=[
        F("Por favor, no ___ la esperanza.", "perdamos", ["pierdamos", "perdámos", "perdiamos"], "Perder → perdamos (no stem change in -er).", tr="Please, let’s not lose hope.", lemma="perder:nosotros:ncmd"),
        F("Con generosidad, ___ lo que podamos.", "donemos", ["donémos", "doniemos", "doneamos"], "Donar → donemos.", tr="Generously, let’s donate whatever we can.", lemma="donar:nosotros:ncmd"),
        F("Para llegar a tiempo, ___ ahora.", "salgamos", ["salgámos", "saligamos", "salgiemos"], "Salir → salgamos.", tr="To arrive on time, let’s leave now.", lemma="salir:nosotros:ncmd"),
        F("Para entender, ___ más ejemplos.", "pidamos", ["pedamos", "pidémos", "pidiamos"], "Pedir → pidamos.", tr="To understand, let’s ask for more examples.", lemma="pedir:nosotros:ncmd"),
        F("En la fila, ___ pacientes.", "seamos", ["semos", "seémos", "seamo"], "Ser → seamos.", tr="In the line, let’s be patient.", lemma="ser:nosotros:ncmd"),
        F("La playa está sucia: ___ entre todos.", "limpiémosla", ["la limpiemos", "limpiemosla", "limpiamosla"], "Affirmative: attach la, add the accent.", tr="The beach is dirty: let’s clean it, all together."),
        F("Es tarde: ___ a casa.", "vámonos", ["vamosnos", "vamónos", "vayámosnos"], "Vamos + nos = vámonos.", tr="It is late: let’s go home."),
        M("What is the nosotros command of hacer?", "hagamos", ["hacemos", "hacamos", "hizamos"], "Hago → hagamos."),
        M("Which sentence is a negative nosotros command?", "No perdamos la esperanza.", ["No perdemos la esperanza.", "No perdimos la esperanza.", "No perder la esperanza."], "No + perdamos."),
    ],
    verify=(vpn("perder", "perdamos") + vpn("donar", "donemos") + vpn("salir", "salgamos") + vpn("pedir", "pidamos")
            + vpn("ser", "seamos")),
)

# ---------------------------------------------------------------------------- 454
L454 = lesson(
    "Unit review: natural disasters",
    "Todo junto: noticias, órdenes formales y llamadas a la acción.",
    requires=["terremoto", "huracán", "incendio", "ayuda", "donar", "rescatar", "refugio", "salir", "ayudar", "escuchar", "bombero", "víctima"],
    cards=[
        card("Your toolbox from Chapter 23",
             "A disaster story uses vocabulary for the event, commands for instructions to people you address as usted or ustedes, and nosotros commands for appeals.",
             tables=[table(["Job", "Tool", "Example"],
                           [["name the event", "terremoto, huracán, incendio", "Un terremoto sacudió la costa."],
                            ["describe the damage", "heridos, desaparecidos, daños", "Todavía buscan a los desaparecidos."],
                            ["order one person (usted)", "formal command", "Mantenga la calma."],
                            ["order a group (ustedes)", "formal command, -n", "Salgan por la puerta."],
                            ["what not to do", "no + command", "No use el ascensor."],
                            ["appeal to everyone", "nosotros command", "Donemos comida y agua."]],
                           say=[2])]),
    ],
    exercises=[
        F("Un ___ sacudió la costa y hubo muchas réplicas.", "terremoto", ["huracán", "incendio", "tsunami"], "Replicas follow an earthquake.", tr="An earthquake shook the coast and there were many aftershocks."),
        F("Ayer los bomberos ___ a una familia atrapada.", "rescataron", ["rescató", "rescatar", "rescatan"], "Bomberos is plural.", tr="The firefighters rescued a trapped family.", lemma="rescatar:ellos:pret"),
        F("Señora, ___ la calma y salga con orden.", "mantenga", ["mantiene", "mantener", "mantengan"], "Mantener → mantenga.", tr="Ma’am, stay calm and leave in an orderly way.", lemma="mantener:usted:cmd"),
        F("Señores, no ___ el ascensor.", "usen", ["usan", "usar", "use"], "Ustedes negative command.", tr="Ladies and gentlemen, do not use the elevator.", lemma="usar:ustedes:cmd"),
        F("Señor, ___ la radio para escuchar las noticias.", "encienda", ["enciende", "encender", "enciendan"], "Encender → encienda.", tr="Sir, turn on the radio to hear the news.", lemma="encender:usted:cmd"),
        F("Hoy mismo, ___ ayuda a los damnificados.", "demos", ["démos", "deamos", "demo"], "Dar → demos.", tr="Today, let’s give help to those affected.", lemma="dar:nosotros:ncmd"),
        F("Ayer los voluntarios ___ comida y agua.", "donaron", ["donó", "donar", "donan"], "Voluntarios is plural.", tr="The volunteers donated food and water.", lemma="donar:ellos:pret"),
        M("Which sentence tells one person what to do?", "Mantenga la calma.", ["Mantengan la calma.", "Mantengamos la calma.", "Mantienen la calma."], "Usted command."),
        M("Which sentence is an appeal to everybody including the speaker?", "Ayudemos a las víctimas.", ["Ayuden a las víctimas.", "Ayude a las víctimas.", "Ayudan a las víctimas."], "Nosotros command."),
        M("What word describes people who survived the disaster?", "sobrevivientes", ["desaparecidos", "damnificados", "donaciones"], "Sobrevivientes."),
    ],
    verify=(vpc("mantener", "mantenga", "mantengan") + vpc("usar", "use", "usen") + vpc("encender", "encienda", "enciendan")),
)

UNIT = unit("Desastres naturales", [
    L425, L426, L427, L428, L429, L430, L431, L432, L433, L434, L435,
    L436, L437, L438, L439, L440, L441, L442, L443, L444, L445, L446,
    L447, L448, L449, L450, L451, L452, L453, L454,
])

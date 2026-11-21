"""Unit 8: weather (textbook Chapter 7)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 98
L98 = lesson(
    "Weather with hacer",
    "¿Qué tiempo hace? Hace calor. Hace buen tiempo.",
    requires=["tiempo", "hacer", "calor", "frío", "sol", "viento"],
    cards=[
        card("¿Qué tiempo hace?",
             "To ask about the weather, say ¿Qué tiempo hace? Many answers use hace (from hacer) plus a noun. "
             "Spanish has no word for “it” here: the verb is simply hace, always in the singular.",
             tables=[table(["Expresión", "English"],
                           [["Hace calor.", "It is hot."],
                            ["Hace frío.", "It is cold."],
                            ["Hace fresco.", "It is cool."],
                            ["Hace sol.", "It is sunny."],
                            ["Hace viento.", "It is windy."],
                            ["Hace buen tiempo.", "The weather is nice."],
                            ["Hace mal tiempo.", "The weather is bad."]],
                           say=[0])]),
        card("Mucho, not muy",
             "Calor, frío, sol and viento are nouns here, so “very” is mucho (mucho calor), never muy. "
             "Bueno and malo drop their final -o before a masculine singular noun: buen tiempo, mal tiempo.",
             examples=[
                 ex("Hoy hace mucho calor en la playa.", "Today it is very hot at the beach.", "mucho calor"),
                 ex("¿Qué tiempo hace en Quito hoy?", "What is the weather like in Quito today?", "¿Qué tiempo hace"),
                 ex("Hace mucho viento y necesito una chaqueta.", "It is very windy and I need a jacket.", "Hace mucho viento"),
                 ex("Vamos al parque porque hace buen tiempo.", "We are going to the park because the weather is nice.", "buen tiempo"),
             ]),
        card("The weather, or how you feel",
             "For the weather, use hacer: Hace frío. For how a person feels, use tener: Tengo frío means “I am cold”.",
             tables=[table(["The weather", "A person"],
                           [["Hace calor.", "Tengo calor."],
                            ["Hace mucho frío.", "Mi hermano tiene mucho frío."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Hoy ___ mucho calor.", "hace", ["es", "está", "tiene"], "Weather with a noun uses hacer: hace calor.",
          tr="Today it is very hot."),
        F("En enero ___ mucho frío en Chicago.", "hace", ["hacen", "hago", "haces"],
          "The weather verb is always third person singular: hace.", tr="In January it is very cold in Chicago.",
          lemma="hacer:él"),
        F("Vamos a la playa porque hace ___ tiempo.", "buen", ["bueno", "bien", "buena"],
          "Before a masculine noun, bueno becomes buen.", tr="We are going to the beach because the weather is nice."),
        F("No salimos porque hace ___ tiempo.", "mal", ["malo", "muy", "mala"],
          "Before a masculine noun, malo becomes mal.", tr="We are not going out because the weather is bad."),
        M("How do you say “It is very windy”?", "Hace mucho viento.", ["Hace muy viento.", "Es mucho viento.", "Está mucho viento."],
          "Viento is a noun here, so mucho (not muy), and the verb is hace."),
        M("Which question asks about the weather?", "¿Qué tiempo hace?", ["¿Qué hora es?", "¿Cómo eres?", "¿Quién hace?"],
          "¿Qué tiempo hace? is the standard question."),
        M("Julia says “Tengo frío.” What does she mean?", "She herself feels cold.", ["The weather forecast is cold.", "She likes the winter.", "She has a cold illness."],
          "Tener + frío describes how a person feels; the weather is hace frío."),
        M("Which sentence describes the weather, not a person?", "Hace sol.", ["Tengo sol.", "Tiene sol.", "Tenemos sol."],
          "Hace sol is the weather."),
        F("Mi hermano ___ mucho frío y lleva un abrigo.", "tiene", ["hace", "es", "está"],
          "A person feels cold with tener: tiene frío.", tr="My brother is very cold and is wearing a coat.", lemma="tener:él"),
    ],
    verify=vp("hacer", "hago", "haces", "hace", "hacemos", "hacéis", "hacen"),
)

# ---------------------------------------------------------------------------- 99
L99 = lesson(
    "Weather with estar and hay",
    "Está nublado. Hay tormenta. Hay niebla.",
    requires=["estar", "haber", "cielo", "nube", "tormenta", "lluvia"],
    cards=[
        card("Estar + adjective: the sky",
             "To describe how the sky looks, use estar with an adjective. Está nublado means the sky is cloudy; "
             "está despejado means it is clear, with no clouds.",
             tables=[table(["Expresión", "English"],
                           [["El cielo está nublado.", "The sky is cloudy."],
                            ["El cielo está despejado.", "The sky is clear."],
                            ["Está parcialmente nublado.", "It is partly cloudy."],
                            ["Está húmedo.", "It is humid."]],
                           say=[0])]),
        card("Hay + noun: something is happening",
             "Hay means “there is” or “there are”. Use it for weather events: it never changes, even when the noun is "
             "plural.",
             tables=[table(["Expresión", "English"],
                           [["Hay tormenta.", "There is a storm."],
                            ["Hay niebla.", "There is fog."],
                            ["Hay granizo.", "There is hail."],
                            ["Hay nieve en las montañas.", "There is snow in the mountains."],
                            ["Hay relámpagos.", "There is lightning."],
                            ["Hay humedad.", "It is humid (there is humidity)."]],
                           say=[0])],
             examples=[
                 ex("Hoy hay mucha niebla en la carretera.", "Today there is a lot of fog on the road.", "mucha niebla"),
                 ex("Hay tormentas en el mar.", "There are storms at sea.", "Hay tormentas"),
             ]),
        card("Which verb?",
             "Use hacer for temperature, sun and wind. Use estar for the look of the sky. Use hay for events and things "
             "in the air. Learn each phrase whole, as one block. (Hay sol and hay viento are also common; hace is the safest choice.)",
             tables=[table(["Verb", "Used with", "Example"],
                           [["hacer", "calor, frío, sol, viento", "Hace frío."],
                            ["estar", "nublado, despejado", "Está nublado."],
                            ["hay", "tormenta, niebla, granizo, nieve", "Hay niebla."]],
                           say=[2])]),
    ],
    exercises=[
        F("El cielo ___ nublado hoy.", "está", ["hace", "hay", "es"], "Estar + nublado describes the sky.",
          tr="The sky is cloudy today."),
        F("Hoy hay ___ en la montaña y no veo nada.", "niebla", ["nublado", "despejado", "soleado"],
          "Hay is followed by a noun; the others are adjectives that go with estar.", tr="Today there is fog on the mountain and I cannot see anything."),
        F("El cielo está ___ y se ven las estrellas.", "despejado", ["nublado", "niebla", "tormenta"],
          "You can see the stars only when the sky is clear.", tr="The sky is clear and you can see the stars."),
        F("Hay muchas ___ en el cielo y va a llover.", "nubes", ["nublado", "despejado", "nube"],
          "Muchas is feminine plural: nubes.", tr="There are many clouds in the sky and it is going to rain."),
        M("Which is correct?", "Hay tormentas en el mar.", ["Están tormentas en el mar.", "Hacen tormentas en el mar.", "Son tormentas en el mar."],
          "Hay introduces things that exist or happen, and stays singular."),
        M("The sky has no clouds. How do you say it?", "Está despejado.", ["Hay despejado.", "Hace despejado.", "Es despejado."],
          "Despejado is an adjective for the sky: estar."),
        M("What does “Hay granizo” describe?", "Hail is falling.", ["Snow is falling.", "There is fog.", "It is very hot."],
          "Granizo is hail."),
        M("Which phrase uses the wrong verb?", "Hay nublado.", ["Hay niebla.", "Hay nieve.", "Hay tormenta."],
          "Nublado is an adjective and needs estar: Está nublado."),
        M("What does “Hay humedad” mean?", "It is humid.", ["It is dry.", "It is windy.", "There is a person."],
          "Humedad means humidity."),
    ],
    verify=vp("estar", "estoy", "estás", "está", "estamos", "estáis", "están"),
)

# ---------------------------------------------------------------------------- 100
L100 = lesson(
    "Weather verbs: llueve, nieva, truena",
    "Llueve. Nieva. Truena. Llovizna.",
    requires=["llover", "lluvia", "nieve", "tormenta", "tiempo", "mucho"],
    cards=[
        card("Verbs with no subject",
             "Some weather is expressed with a single verb that exists only in the third person singular. "
             "Llover and nevar are boot verbs: llueve and nieva.",
             tables=[table(["Infinitive", "Weather phrase", "English"],
                           [["llover (o → ue)", "Llueve.", "It rains."],
                            ["lloviznar", "Llovizna.", "It drizzles."],
                            ["nevar (e → ie)", "Nieva.", "It snows."],
                            ["tronar (o → ue)", "Truena.", "It thunders."],
                            ["granizar", "Graniza.", "It hails."]],
                           say=[1])]),
        card("In a sentence",
             "These verbs take adverbs like mucho and poco. To say that it is happening right now, you can use "
             "estar + the -ndo form of the verb: Está lloviendo.",
             examples=[
                 ex("En abril llueve mucho en Bogotá.", "In April it rains a lot in Bogotá.", "llueve mucho"),
                 ex("En las montañas nieva en invierno.", "In the mountains it snows in winter.", "nieva"),
                 ex("Esta noche truena y hay relámpagos.", "Tonight it thunders and there is lightning.", "truena"),
                 ex("No llueve hoy.", "It is not raining today.", "No llueve"),
                 ex("Está lloviendo ahora.", "It is raining now.", "Está lloviendo"),
             ]),
    ],
    exercises=[
        F("En abril ___ mucho en Bogotá.", "llueve", ["llovo", "llovemos", "llueven"], "Llover is o → ue and weather uses only the singular: llueve.",
          tr="In April it rains a lot in Bogotá.", lemma="llover:él"),
        F("En las montañas ___ en invierno.", "nieva", ["nievo", "nievan", "nevamos"], "Nevar is e → ie: nieva.",
          tr="In the mountains it snows in winter.", lemma="nevar:él"),
        M("Which verb is related to the noun “trueno” (thunder)?", "tronar", ["nevar", "llover", "granizar"], "Trueno and tronar belong together."),
        M("Which verb means “it drizzles”?", "lloviznar", ["nevar", "tronar", "granizar"], "Llovizna is a light rain."),
        M("Which sentence means about the same as “Llueve”?", "Está lloviendo.", ["Hace sol.", "Hay niebla.", "Está despejado."],
          "Está lloviendo is the progressive form of llueve."),
        M("Which sentence is correct?", "Llueve mucho en la selva.", ["Llueven mucho en la selva.", "Llovo mucho en la selva.", "Hace llueve en la selva."],
          "Weather verbs stay in the third person singular."),
        M("What does “Nieva” describe?", "Snow is falling.", ["Hail is falling.", "Rain is falling.", "The wind is blowing."], "Nevar is to snow."),
        M("Which weather verb follows the e → ie pattern?", "nevar", ["llover", "tronar", "lloviznar"], "Nieva has ie; llueve and truena have ue."),
        F("En el desierto casi no ___ en todo el año.", "llueve", ["llovo", "llueves", "llueven"],
          "Weather verbs use only the third person singular: llueve.", tr="In the desert it hardly rains all year.", lemma="llover:él"),
    ],
    verify=vp("llover", None, None, "llueve", None, None, None) + vp("nevar", None, None, "nieva", None, None, None)
           + vp("tronar", None, None, "truena", None, None, None),
)

# ---------------------------------------------------------------------------- 101
L101 = lesson(
    "Seasons and months",
    "la primavera, el verano, el otoño, el invierno",
    requires=["primavera", "verano", "invierno", "estación", "mes", "año"],
    cards=[
        card("The four seasons",
             "Seasons are estaciones. Learn the gender: la primavera, el verano, el otoño, el invierno. You can say "
             "en verano or en el verano; both are normal.",
             tables=[table(["Estación", "English", "Typical weather"],
                           [["la primavera", "spring", "Hay flores y a veces llueve."],
                            ["el verano", "summer", "Hace mucho calor."],
                            ["el otoño", "fall", "Hace fresco y los árboles pierden las hojas."],
                            ["el invierno", "winter", "Hace frío y nieva."]],
                           say=[0, 2])]),
        card("The months",
             "Months are not capitalized in Spanish. Months are masculine. To say “in May”, "
             "use en mayo.",
             tables=[table(["Mes", "English"],
                           [["enero", "January"], ["febrero", "February"], ["marzo", "March"],
                            ["abril", "April"], ["mayo", "May"], ["junio", "June"],
                            ["julio", "July"], ["agosto", "August"], ["septiembre", "September"],
                            ["octubre", "October"], ["noviembre", "November"], ["diciembre", "December"]],
                           say=[0])]),
        card("North and south",
             "The seasons are reversed in the Southern Hemisphere. In Argentina, Chile and Uruguay, December is "
             "summer and July is winter. In Mexico and Spain the seasons are like those in the United States.",
             examples=[
                 ex("En Buenos Aires hace calor en diciembre.", "In Buenos Aires it is hot in December.", "hace calor en diciembre"),
                 ex("En julio hace frío en Santiago de Chile.", "In July it is cold in Santiago, Chile.", "En julio"),
                 ex("En México llueve mucho en verano.", "In Mexico it rains a lot in summer.", "llueve mucho"),
             ]),
    ],
    exercises=[
        M("Which season is “el otoño”?", "fall", ["spring", "summer", "winter"], "Otoño is fall."),
        M("Which noun is feminine?", "la primavera", ["el verano", "el otoño", "el invierno"], "Primavera ends in -a and is feminine."),
        M("In which season does it usually snow in Chicago?", "en invierno", ["en verano", "en primavera", "en todo el año"],
          "Winter is the cold season."),
        F("En ___ hace mucho calor y vamos a la playa.", "verano", ["invierno", "otoño", "sol"],
          "Hot weather and the beach point to summer (in the north).", tr="In summer it is very hot and we go to the beach."),
        F("En ___ hace mucho frío y nieva.", "invierno", ["verano", "primavera", "sol"],
          "Cold and snow point to winter.", tr="In winter it is very cold and it snows."),
        M("In Argentina, which season is July?", "winter", ["summer", "spring", "fall"], "In the Southern Hemisphere, July is winter."),
        M("Which month comes after “marzo”?", "abril", ["mayo", "febrero", "junio"], "Marzo, abril, mayo."),
        M("How should the month be written?", "enero", ["Enero", "ENERO", "ene."],
          "Months are not capitalized in Spanish."),
        M("Which month comes right before “septiembre”?", "agosto", ["octubre", "julio", "noviembre"], "Agosto, septiembre, octubre."),
    ],
)

# ---------------------------------------------------------------------------- 102
L102 = lesson(
    "Temperature and climate",
    "grados centígrados, clima seco, clima húmedo",
    requires=["temperatura", "grado", "clima", "frío", "calor", "seco"],
    cards=[
        card("Celsius, not Fahrenheit",
             "In Spanish-speaking countries, as in most of the world, temperature is given in grados centígrados "
             "(degrees Celsius). To say what the temperature is, use estar a.",
             tables=[table(["Celsius", "Fahrenheit", "Se dice"],
                           [["0", "32", "Hace mucho frío."],
                            ["10", "50", "Hace fresco."],
                            ["20", "68", "Hace buen tiempo."],
                            ["30", "86", "Hace calor."],
                            ["40", "104", "Hace mucho calor."]],
                           say=[2])],
             examples=[
                 ex("Estamos a veinte grados.", "It is twenty degrees (Celsius).", "veinte grados"),
                 ex("La temperatura baja por la noche.", "The temperature drops at night.", "baja"),
                 ex("Mañana la temperatura sube a treinta grados.", "Tomorrow the temperature rises to thirty degrees.", "sube"),
             ]),
        card("Types of climate",
             "Clima means the usual weather in a place over the year. It is masculine. Use ser or tener for the "
             "climate of a place, and the adjectives agree with clima.",
             tables=[table(["Clima", "English"],
                           [["un clima frío", "a cold climate"],
                            ["un clima templado", "a mild climate"],
                            ["un clima cálido", "a hot climate"],
                            ["un clima húmedo", "a humid climate"],
                            ["un clima seco", "a dry climate"]],
                           say=[0])],
             examples=[
                 ex("La costa tiene un clima templado.", "The coast has a mild climate.", "un clima templado"),
                 ex("El desierto tiene un clima muy seco.", "The desert has a very dry climate.", "un clima muy seco"),
             ]),
        card("A false friend: sensible",
             "Sensible does not mean “sensible” in Spanish. It means “sensitive”. For “reasonable, sensible”, "
             "say sensato or razonable.",
             examples=[
                 ex("Mi hermana es muy sensible.", "My sister is very sensitive.", "sensible"),
                 ex("Es una decisión sensata.", "It is a sensible decision.", "sensata"),
             ]),
    ],
    exercises=[
        M("Which scale do Spanish-speaking countries use for the weather?", "grados centígrados", ["grados Fahrenheit", "grados Kelvin", "grados angulares"],
          "Celsius, called centígrados in Spanish."),
        M("Water freezes at zero degrees Celsius. How many degrees Fahrenheit is that?", "32", ["0", "50", "100"],
          "Zero degrees Celsius is thirty-two Fahrenheit."),
        M("The temperature is thirty degrees Celsius. What is the weather like?", "Hace calor.", ["Hace frío.", "Nieva.", "Hay hielo."],
          "Thirty Celsius is hot (eighty-six Fahrenheit)."),
        F("La costa tiene un clima ___.", "templado", ["templada", "templados", "templadas"],
          "Clima is masculine singular, so the adjective is too.", tr="The coast has a mild climate."),
        F("Un clima ___ tiene poca lluvia.", "seco", ["seca", "húmedo", "secos"],
          "Seco describes a climate with little rain; clima is masculine.", tr="A dry climate has little rain."),
        M("What does “sensible” mean in Spanish?", "sensitive", ["reasonable", "logical", "silly"], "It is a false friend."),
        M("How do you say “a sensible decision”?", "una decisión sensata", ["una decisión sensible", "una decisión sensitiva", "un decisión sensata"],
          "Sensato means sensible; decisión is feminine."),
        M("What does “La temperatura baja” mean?", "The temperature drops.", ["The temperature rises.", "The bass is loud.", "It is short."],
          "Bajar is to go down."),
        M("How do you say “It is twenty degrees” (Celsius)?", "Estamos a veinte grados.", ["Tenemos a veinte grados.", "Somos veinte grados.", "Está veinte grados."],
          "Estar a is used with temperatures."),
    ],
)

# ---------------------------------------------------------------------------- 103
L103 = lesson(
    "Always and never: siempre, nunca",
    "Siempre llueve. Nunca nieva. No llueve nunca.",
    requires=["siempre", "nunca", "casi", "verano", "llover", "nada"],
    cards=[
        card("Siempre and nunca",
             "Siempre means “always” and nunca means “never”. Both usually go right before the verb.",
             examples=[
                 ex("Siempre hace frío en el invierno.", "It is always cold in winter.", "Siempre"),
                 ex("En el desierto nunca nieva.", "In the desert it never snows.", "nunca nieva"),
                 ex("Casi nunca llueve en agosto.", "It almost never rains in August.", "Casi nunca"),
             ]),
        card("The double negative",
             "In English you must not say “I don't never go”. In Spanish you must: if nunca comes AFTER the verb, "
             "put no before the verb. If nunca comes BEFORE the verb, there is no no.",
             tables=[table(["Nunca first", "No ... nunca"],
                           [["Nunca llueve aquí.", "No llueve nunca aquí."],
                            ["Nunca bebo café.", "No bebo nunca café."],
                            ["Mis padres nunca esquían.", "Mis padres no esquían nunca."]],
                           say=[0, 1])]),
        card("Same family",
             "The same rule works for nada (nothing) and nadie (no one): they can come after no + verb (No hay nadie) or before the verb (Nadie habla). "
             "Spanish allows several negative words in one sentence.",
             examples=[
                 ex("No tengo nada en la maleta.", "I have nothing in the suitcase.", "No tengo nada"),
                 ex("No hay nadie en la playa.", "There is no one on the beach.", "No hay nadie"),
             ]),
    ],
    exercises=[
        F("En el desierto ___ nieva.", "nunca", ["siempre", "mucho", "también"], "The translation says “never”: nunca goes before the verb.",
          tr="In the desert it never snows."),
        F("En la selva amazónica ___ llueve mucho.", "siempre", ["nunca", "casi nunca", "no"], "The Amazon rainforest is very wet.",
          tr="In the Amazon rainforest it always rains a lot."),
        F("No llueve ___ en agosto.", "nunca", ["siempre", "también", "mucho"],
          "With no before the verb, nunca after it means “never”, which matches the translation.", tr="It never rains in August."),
        M("Which sentence means “It never snows here”?", "Aquí nunca nieva.", ["Aquí siempre nieva.", "Aquí no nunca nieva.", "Aquí nieva nunca no."],
          "Nunca before the verb needs no no."),
        M("Which sentence is correct?", "No bebo nunca café.", ["Bebo nunca café no.", "No bebo siempre café nunca.", "No nunca bebo café."],
          "No goes before the verb; nunca follows it."),
        M("Which sentence is correct?", "Nunca hace frío en Miami en mayo.", ["No nunca hace frío en Miami en mayo.", "Nunca no hace frío en Miami en mayo.", "Hace frío nunca no en Miami."],
          "When nunca is first, you do not add no."),
        M("What does “casi nunca” mean?", "almost never", ["almost always", "never ever", "sometimes"], "Casi means almost."),
        M("How do you say “I have nothing”?", "No tengo nada.", ["Tengo no nada.", "Nada no tengo.", "No nada tengo."],
          "No + verb + nada."),
        M("Which sentence means “There is no one at the beach”?", "No hay nadie en la playa.", ["Hay nadie no en la playa.", "No nadie hay en la playa.", "Hay nada en la playa."],
          "No hay nadie is the normal pattern."),
    ],
)

# ---------------------------------------------------------------------------- 104
L104 = lesson(
    "The future tense: regular verbs",
    "hablaré, aprenderé, viviré",
    requires=["hablar", "aprender", "vivir", "mañana", "futuro", "ir"],
    cards=[
        card("Add the endings to the infinitive",
             "The simple future is easy: keep the whole infinitive and add the same endings to all verbs "
             "(-ar, -er and -ir): -é, -ás, -á, -emos, -éis, -án. Every form except nosotros has a written accent.",
             tables=[table(["", "hablar", "aprender", "vivir"],
                           [["yo", "hablaré", "aprenderé", "viviré"],
                            ["tú", "hablarás", "aprenderás", "vivirás"],
                            ["él, ella, usted", "hablará", "aprenderá", "vivirá"],
                            ["nosotros", "hablaremos", "aprenderemos", "viviremos"],
                            ["vosotros", "hablaréis", "aprenderéis", "viviréis"],
                            ["ellos, ellas, ustedes", "hablarán", "aprenderán", "vivirán"]],
                           say=[1, 2, 3])]),
        card("Three ways to talk about tomorrow",
             "Spanish can talk about the future with the present (Mañana viajo), with ir a + infinitive "
             "(Voy a viajar) or with the future tense (Viajaré). The future often sounds a bit more formal or more "
             "distant, and it is common in forecasts and predictions.",
             examples=[
                 ex("Mañana hablaré con mi jefe.", "Tomorrow I will talk with my boss.", "hablaré"),
                 ex("El próximo año viviremos en México.", "Next year we will live in Mexico.", "viviremos"),
                 ex("¿Aprenderás español pronto?", "Will you learn Spanish soon?", "Aprenderás"),
                 ex("Mis amigos viajarán en diciembre.", "My friends will travel in December.", "viajarán"),
             ]),
    ],
    exercises=[
        F("Mañana yo ___ con el profesor.", "hablaré", ["hablarás", "hablará", "hablaremos"], "Yo takes -é: hablaré.",
          tr="Tomorrow I will talk with the teacher.", lemma="hablar:yo:fut"),
        F("El año próximo nosotros ___ en España.", "viviremos", ["viviré", "vivirán", "vivirás"], "Nosotros takes -emos, with no accent.",
          tr="Next year we will live in Spain.", lemma="vivir:nosotros:fut"),
        F("Tú ___ mucho en este curso.", "aprenderás", ["aprenderé", "aprenderá", "aprenderán"], "Tú takes -ás.",
          tr="You will learn a lot in this course.", lemma="aprender:tú:fut"),
        F("Mis padres ___ en diciembre.", "viajarán", ["viajará", "viajaré", "viajaremos"], "Mis padres is they: -án.",
          tr="My parents will travel in December.", lemma="viajar:ellos:fut"),
        F("Ella ___ la comida mañana.", "comprará", ["comprarán", "compraré", "comprarás"], "Ella takes -á.",
          tr="She will buy the food tomorrow.", lemma="comprar:ella:fut"),
        M("What is the future of “escribir” for yo?", "escribiré", ["escribo", "escribiría", "escribirá"], "Infinitive + é."),
        M("Which form needs NO written accent?", "hablaremos", ["hablarás", "hablaré", "hablarán"], "Only the nosotros form has no accent."),
        M("What is the infinitive of “viviré”?", "vivir", ["viver", "vivar", "vivré"], "The future keeps the whole infinitive."),
        M("Which sentence means “We will study tomorrow”?", "Estudiaremos mañana.", ["Estudiaré mañana.", "Estudiarán mañana.", "Estudiarás mañana."],
          "Nosotros: -emos."),
    ],
    verify=vpf("hablar", "hablaré", "hablarás", "hablará", "hablaremos", "hablaréis", "hablarán")
           + vpf("aprender", "aprenderé", "aprenderás", "aprenderá", "aprenderemos", "aprenderéis", "aprenderán")
           + vpf("vivir", "viviré", "vivirás", "vivirá", "viviremos", "viviréis", "vivirán"),
)

# ---------------------------------------------------------------------------- 105
L105 = lesson(
    "The future tense: irregular stems",
    "tendré, saldré, haré, diré, podré",
    requires=["tener", "salir", "hacer", "decir", "poder", "poner"],
    cards=[
        card("Twelve irregular stems",
             "A few common verbs change the stem before the future endings. The endings stay the same (-é, -ás, -á, "
             "-emos, -éis, -án). Learn the twelve stems; they come in three groups.",
             tables=[table(["Infinitive", "Stem", "Yo, future", "English"],
                           [["poder", "podr-", "podré", "to be able"],
                            ["saber", "sabr-", "sabré", "to know"],
                            ["querer", "querr-", "querré", "to want"],
                            ["caber", "cabr-", "cabré", "to fit"],
                            ["haber", "habr-", "habré", "to have (auxiliary); habrá = there will be"],
                            ["poner", "pondr-", "pondré", "to put"],
                            ["salir", "saldr-", "saldré", "to leave"],
                            ["tener", "tendr-", "tendré", "to have"],
                            ["valer", "valdr-", "valdré", "to be worth"],
                            ["venir", "vendr-", "vendré", "to come"],
                            ["decir", "dir-", "diré", "to say"],
                            ["hacer", "har-", "haré", "to do, make"]],
                           say=[2])]),
        card("Three groups",
             "In the first group the e of the infinitive ending disappears (poder → podr-). In the second group a d "
             "replaces the vowel (poner → pondr-). Decir and hacer lose their middle letters (dir-, har-).",
             tables=[table(["", "tener", "salir", "hacer"],
                           [["yo", "tendré", "saldré", "haré"],
                            ["tú", "tendrás", "saldrás", "harás"],
                            ["él, ella, usted", "tendrá", "saldrá", "hará"],
                            ["nosotros", "tendremos", "saldremos", "haremos"],
                            ["vosotros", "tendréis", "saldréis", "haréis"],
                            ["ellos, ellas, ustedes", "tendrán", "saldrán", "harán"]],
                           say=[1, 2, 3])],
             examples=[
                 ex("Mañana tendré mucho trabajo.", "Tomorrow I will have a lot of work.", "tendré"),
                 ex("Mis amigos saldrán temprano.", "My friends will leave early.", "saldrán"),
                 ex("El sábado haremos una fiesta.", "On Saturday we will have a party.", "haremos"),
             ]),
    ],
    exercises=[
        F("Mañana yo ___ de la casa a las siete.", "saldré", ["saldremos", "saliré", "saldrá"], "Salir has the stem saldr-: saldré.", tr="Tomorrow I will leave the house at seven.", lemma="salir:yo:fut"),
        F("Nosotros ___ mucho trabajo la semana próxima.", "tendremos", ["teneremos", "tendrán", "tendré"], "Tener has the stem tendr-.", tr="We will have a lot of work next week.", lemma="tener:nosotros:fut"),
        F("Tú ___ la verdad mañana.", "dirás", ["decirás", "dirá", "diré"], "Decir has the stem dir-.", tr="You will tell the truth tomorrow.", lemma="decir:tú:fut"),
        F("Mis amigos ___ a la fiesta.", "vendrán", ["venirán", "vendrá", "vendré"], "Venir has the stem vendr-.", tr="My friends will come to the party.", lemma="venir:ellos:fut"),
        F("Ella ___ la maleta en el coche.", "pondrá", ["ponerá", "pondrán", "pondré"], "Poner has the stem pondr-.", tr="She will put the suitcase in the car.", lemma="poner:ella:fut"),
        F("Yo ___ ir contigo el domingo.", "podré", ["poderé", "podrás", "podrá"], "Poder has the stem podr-.", tr="I will be able to go with you on Sunday.", lemma="poder:yo:fut"),
        F("Los niños ___ jugar mañana.", "querrán", ["querrá", "querré", "querrás"], "Querer has the stem querr-; los niños is they.", tr="The children will want to play tomorrow.", lemma="querer:ellos:fut"),
        M("What is the stem of “hacer” in the future?", "har-", ["hac-", "hacer-", "hagr-"], "Hacer becomes har-: haré, harás, hará."),
        M("Which infinitive gets a NEW d in its future stem?", "poner", ["poder", "saber", "querer"], "Poner → pondr-. Poder already has a d (podr-); saber and querer just drop a vowel."),
        M("The future of “hay” (there is) is...", "habrá", ["hay", "habrás", "habré"], "Haber is impersonal in the future too: habrá."),
    ],
    verify=vpf("tener", "tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán")
           + vpf("salir", "saldré", "saldrás", "saldrá", "saldremos", "saldréis", "saldrán")
           + vpf("hacer", "haré", "harás", "hará", "haremos", "haréis", "harán")
           + vpf("poder", "podré", None, None, None, None, "podrán")
           + vpf("poner", "pondré", None, "pondrá", None, None, None)
           + vpf("decir", "diré", "dirás", None, None, None, None)
           + vpf("venir", "vendré", None, None, None, None, "vendrán")
           + vpf("querer", None, None, None, None, None, "querrán")
           + vpf("saber", "sabré", None, None, None, None, None)
           + vpf("caber", "cabré", None, None, None, None, None)
           + vpf("valer", "valdré", None, None, None, None, None)
           + vpf("haber", None, None, "habrá", None, None, None),
)

# ---------------------------------------------------------------------------- 106
L106 = lesson(
    "Future weather and plans",
    "Mañana hará calor. Habrá tormenta. Estará nublado.",
    requires=["mañana", "semana", "hacer", "haber", "estar", "llover"],
    cards=[
        card("Today, then tomorrow",
             "To turn a weather phrase into a forecast, put the verb into the future. Hace calor becomes hará calor. "
             "Hay tormenta becomes habrá tormenta (haber is always singular). Está nublado becomes estará nublado.",
             tables=[table(["Hoy", "Mañana"],
                           [["Hace calor.", "Hará calor."],
                            ["Hace frío.", "Hará frío."],
                            ["Hay tormenta.", "Habrá tormenta."],
                            ["Hay niebla.", "Habrá niebla."],
                            ["Está nublado.", "Estará nublado."],
                            ["Llueve.", "Lloverá."],
                            ["Nieva.", "Nevará."]],
                           say=[0, 1])]),
        card("Plans for the weekend",
             "The future is also useful for plans and promises. Ir a + infinitive means almost the same thing; the "
             "future sounds a little more formal.",
             examples=[
                 ex("El sábado hará buen tiempo y iremos a la playa.", "On Saturday the weather will be nice and we will go to the beach.", "hará buen tiempo"),
                 ex("El domingo lloverá, así que estaré en casa.", "On Sunday it will rain, so I will be at home.", "lloverá"),
                 ex("En el futuro viviré en una casa cerca del mar.", "In the future I will live in a house near the sea.", "viviré"),
                 ex("Mi casa del futuro tendrá un jardín grande.", "My house of the future will have a big garden.", "tendrá"),
                 ex("La próxima semana habrá nieve en las montañas.", "Next week there will be snow in the mountains.", "habrá nieve"),
             ]),
    ],
    exercises=[
        F("Mañana ___ tormenta en la costa.", "habrá", ["habrás", "habré", "habremos"], "Impersonal haber is always third person singular.", tr="Tomorrow there will be a storm on the coast.", lemma="haber:ella:fut"),
        F("El sábado ___ mucho calor.", "hará", ["haré", "harán", "haremos"], "Hacer in the weather expressions is third person singular: hará.", tr="On Saturday it will be very hot.", lemma="hacer:ella:fut"),
        F("Mañana ___ en las montañas.", "nevará", ["nevarán", "nevaré", "nevarás"], "Weather verbs are third person singular.", tr="Tomorrow it will snow in the mountains.", lemma="nevar:ella:fut"),
        F("El domingo el cielo ___ despejado.", "estará", ["estaré", "estarán", "estarás"], "El cielo is singular: estará.", tr="On Sunday the sky will be clear.", lemma="estar:ella:fut"),
        M("Which sentence is a forecast for tomorrow?", "Mañana hará frío.", ["Hoy hace frío.", "Siempre hace frío.", "Ahora hace frío."], "Hará is future."),
        M("What does “Lloverá” mean?", "It will rain.", ["It is raining.", "It rained.", "It never rains."], "-rá is future."),
        M("How do you say “There will be fog”?", "Habrá niebla.", ["Hay niebla.", "Habrán niebla.", "Habré niebla."], "Haber is impersonal: habrá."),
        M("Which sentence talks about a house in the future?", "Mi casa tendrá un jardín.", ["Mi casa tiene un jardín.", "Hoy mi casa tiene un jardín.", "Ahora mi casa tiene un jardín."], "Tendrá is future."),
        M("The forecast says “El lunes nevará”. What will the weather be like?", "snowy", ["sunny", "windy", "hot"], "Nevará is to snow."),
    ],
)

# ---------------------------------------------------------------------------- 107
L107 = lesson(
    "Reading a weather forecast",
    "Se espera lluvia. Se acerca una tormenta.",
    requires=["esperar", "anunciar", "frente", "máximo", "mínimo", "tormenta"],
    cards=[
        card("The language of forecasts",
             "Forecasts (informes meteorológicos) use set expressions with se. Learn them as phrases, because the "
             "verb often agrees with what is coming.",
             tables=[table(["Expresión", "Meaning"],
                           [["Se espera lluvia.", "Rain is expected."],
                            ["Se anuncia una tormenta.", "A storm is forecast."],
                            ["Se viene el frío.", "The cold is coming."],
                            ["Se acerca un frente frío.", "A cold front is approaching."],
                            ["Se avecina una semana de calor.", "A week of heat is on the horizon."]],
                           say=[0])]),
        card("Temperatures and thunder",
             "Forecasts give the highest and the lowest temperature: la temperatura máxima and la temperatura "
             "mínima. They also use three words for the sounds and lights of a storm.",
             tables=[table(["Palabra", "English"],
                           [["el relámpago", "flash of lightning"],
                            ["el rayo", "bolt of lightning"],
                            ["el trueno", "thunder, the sound"]],
                           say=[0])],
             examples=[
                 ex("La temperatura máxima será de veinticinco grados.", "The high temperature will be twenty-five degrees.", "máxima"),
                 ex("La mínima estará cerca de cero grados.", "The low will be close to zero degrees.", "mínima"),
                 ex("Primero vemos el relámpago y después oímos el trueno.", "First we see the lightning flash and then we hear the thunder.", "el relámpago"),
             ]),
        card("A short forecast",
             "Read this small forecast and notice every future form.",
             examples=[
                 ex("Mañana habrá nubes en el norte y se esperan lluvias por la tarde.", "Tomorrow there will be clouds in the north and rain is expected in the afternoon.", "se esperan lluvias"),
                 ex("En el sur hará sol y la temperatura máxima será de treinta grados.", "In the south it will be sunny and the high will be thirty degrees.", "hará sol"),
                 ex("El fin de semana se acerca un frente frío y bajará la temperatura.", "At the weekend a cold front approaches and the temperature will drop.", "bajará"),
             ]),
    ],
    exercises=[
        M("What does “Se espera lluvia” mean?", "Rain is expected.", ["It is raining now.", "Rain is not allowed.", "I hope it never rains."], "Se espera = is expected."),
        M("Which expression says that a storm is approaching?", "Se acerca una tormenta.", ["Se alegra una tormenta.", "Se llama una tormenta.", "Se baja una tormenta."], "Acercarse is to approach."),
        M("What is “el trueno”?", "thunder", ["lightning flash", "hail", "fog"], "Trueno is the sound."),
        M("What is “el relámpago”?", "lightning flash", ["thunder", "wind", "drizzle"], "Relámpago is the light."),
        M("In a forecast, “la temperatura mínima” is...", "the lowest temperature", ["the highest temperature", "a very small thermometer", "the average temperature"], "Mínima is low."),
        F("La temperatura ___ será de treinta grados.", "máxima", ["mínima", "mínimo", "máximo"], "Temperatura is feminine; máxima is the high.", tr="The high temperature will be thirty degrees."),
        F("Se ___ un frente frío esta noche.", "acerca", ["acercan", "acercamos", "acerco"], "Un frente is singular, so se acerca.", tr="A cold front is approaching tonight."),
        F("Mañana se ___ lluvias en la costa.", "esperan", ["espera", "esperamos", "esperas"], "Lluvias is plural, so the verb is plural: se esperan.", tr="Rain is expected on the coast tomorrow."),
        M("Which unit do forecasts in Spanish-speaking countries use?", "grados centígrados", ["grados Fahrenheit", "libras", "pulgadas"], "They use Celsius."),
    ],
)

# ---------------------------------------------------------------------------- 108
L108 = lesson(
    "Vacation activities and places",
    "nadar, pescar, acampar, esquiar, caminar",
    requires=["nadar", "caminar", "pasear", "playa", "montaña", "lago"],
    cards=[
        card("What do you do on vacation?",
             "Here are some outdoor activities. All are infinitives, so you can use them after me gusta, quiero, "
             "vamos a and similar expressions.",
             tables=[table(["Actividad", "English"],
                           [["acampar", "to camp"],
                            ["bucear", "to scuba dive, to snorkel"],
                            ["escalar", "to climb"],
                            ["esquiar", "to ski"],
                            ["caminar", "to walk, to hike"],
                            ["montar a caballo", "to ride a horse"],
                            ["montar en bicicleta", "to ride a bike"],
                            ["nadar", "to swim"],
                            ["pasear", "to take a walk, to stroll"],
                            ["pescar", "to fish"],
                            ["remar en kayak", "to paddle a kayak"]],
                           say=[0])]),
        card("Where?",
             "Learn the places with their articles.",
             tables=[table(["Lugar", "English"],
                           [["el bosque", "forest"],
                            ["el campo", "countryside"],
                            ["la ciudad", "city"],
                            ["la isla", "island"],
                            ["el lago", "lake"],
                            ["la playa", "beach"],
                            ["la montaña", "mountain"],
                            ["el río", "river"],
                            ["el mar", "sea"]],
                           say=[0])],
             examples=[
                 ex("En el verano nadamos en el lago.", "In summer we swim in the lake.", "nadamos"),
                 ex("Me gusta pescar en el río.", "I like to fish in the river.", "pescar"),
                 ex("En invierno esquiamos en las montañas.", "In winter we ski in the mountains.", "esquiamos"),
                 ex("Vamos a acampar en el bosque.", "We are going to camp in the forest.", "acampar"),
             ]),
    ],
    exercises=[
        F("Me gusta ___ en la nieve.", "esquiar", ["nadar", "pescar", "bucear"], "Skiing is done on snow.", tr="I like to ski on the snow."),
        F("Quiero ___ en el mar para ver los peces.", "bucear", ["esquiar", "escalar", "montar a caballo"], "Bucear is to dive or snorkel to see fish.", tr="I want to snorkel in the sea to see the fish."),
        F("Vamos a ___ en el bosque con una tienda de campaña.", "acampar", ["esquiar", "bucear", "nadar"], "You camp with a tent.", tr="We are going to camp in the forest with a tent."),
        F("En la isla hay una ___ muy bonita.", "playa", ["bosque", "río", "campo"], "La playa is feminine and fits la isla and bonita.", tr="On the island there is a very pretty beach."),
        M("Which activity needs a horse?", "montar a caballo", ["pescar", "remar en kayak", "bucear"], "Caballo is horse."),
        M("Which pair of prepositions is standard?", "montar a caballo · montar en bicicleta", ["montar a caballo · montar a bicicleta", "montar de caballo · montar en bicicleta", "montar por caballo · montar por bicicleta"], "A caballo, en bicicleta."),
        M("Which noun is feminine?", "la isla", ["el lago", "el bosque", "el río"], "Isla ends in -a."),
        M("Where do you usually fish?", "en el río o en el lago", ["en el desierto", "en la ciudad de noche", "en una tienda de ropa"], "Fishing needs water."),
        M("What does “caminar” mean?", "to walk or hike", ["to climb", "to swim", "to camp"], "Caminar is to walk."),
    ],
)

# ---------------------------------------------------------------------------- 109
L109 = lesson(
    "The present progressive: estar + -ando / -iendo",
    "Estoy estudiando. Estamos comiendo.",
    requires=["estar", "hablar", "comer", "vivir", "estudiar", "ahora"],
    cards=[
        card("Estar plus the -ndo form",
             "To say what is happening right now, use estar + the present participle (also called the gerund). "
             "Drop -ar and add -ando; drop -er or -ir and add -iendo. The -ndo form never changes: only estar does.",
             tables=[table(["Infinitive", "-ndo form", "Example"],
                           [["hablar", "hablando", "Estoy hablando."],
                            ["estudiar", "estudiando", "Estás estudiando."],
                            ["comer", "comiendo", "Está comiendo."],
                            ["escribir", "escribiendo", "Estamos escribiendo."],
                            ["vivir", "viviendo", "Están viviendo aquí."]],
                           say=[1, 2])]),
        card("Right now, or in general?",
             "The present progressive is for an action in progress, at this moment. For habits and facts use the "
             "simple present: Estudio todos los días, but Ahora estoy estudiando.",
             tables=[table(["Habit", "Right now"],
                           [["Como a las doce.", "Estoy comiendo."],
                            ["Llueve mucho en abril.", "Está lloviendo ahora."],
                            ["Trabajo los lunes.", "Estoy trabajando."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Ahora yo estoy ___ español.", "estudiando", ["estudiar", "estudio", "estudiado"], "Estar + -ando: estudiando.", tr="Right now I am studying Spanish.", lemma="estudiar:ger"),
        F("Mis amigos están ___ en el restaurante.", "comiendo", ["comer", "comen", "comido"], "Comer → comiendo.", tr="My friends are eating at the restaurant.", lemma="comer:ger"),
        F("¿Qué estás ___ ahora?", "haciendo", ["hacer", "hago", "hacido"], "Hacer → haciendo.", tr="What are you doing now?", lemma="hacer:ger"),
        F("Nosotros estamos ___ una carta.", "escribiendo", ["escribimos", "escribir", "escribido"], "Escribir → escribiendo.", tr="We are writing a letter.", lemma="escribir:ger"),
        F("Mi madre ___ cocinando.", "está", ["estás", "estoy", "están"], "Mi madre is she: está.", tr="My mother is cooking.", lemma="estar:ella"),
        F("Ellos ___ hablando con el jefe.", "están", ["está", "estoy", "estamos"], "Ellos is they: están.", tr="They are talking with the boss.", lemma="estar:ellos"),
        M("What is the -ndo form of “vivir”?", "viviendo", ["vivando", "vivido", "vivir"], "-ir verbs add -iendo."),
        M("Which sentence says what is happening NOW?", "Estoy trabajando ahora.", ["Trabajo todos los días.", "Voy a trabajar mañana.", "Trabajaré el lunes."], "Estar + -ando shows an action in progress."),
        M("Which one is a habit rather than a right-now action?", "Estudio todos los días.", ["Estoy estudiando ahora.", "Estamos estudiando.", "Estás estudiando."], "Todos los días signals habit."),
    ],
)

# ---------------------------------------------------------------------------- 110
L110 = lesson(
    "Irregular -ndo forms and when to use them",
    "leyendo, durmiendo, pidiendo, yendo",
    requires=["leer", "creer", "dormir", "pedir", "ir", "estar"],
    cards=[
        card("Between two vowels",
             "If the stem of an -er or -ir verb ends in a vowel, the i of -iendo becomes y: leer → leyendo, "
             "creer → creyendo, construir → construyendo, oír → oyendo, ir → yendo.",
             tables=[table(["Infinitive", "-ndo form", "English"],
                           [["leer", "leyendo", "reading"],
                            ["creer", "creyendo", "believing"],
                            ["construir", "construyendo", "building"],
                            ["traer", "trayendo", "bringing"],
                            ["ir", "yendo", "going"]],
                           say=[1])]),
        card("-ir boot verbs change too",
             "-Ir verbs with a stem change (e → ie, e → i, o → ue) also change the stem vowel in the -ndo form: "
             "dormir → durmiendo, pedir → pidiendo, decir → diciendo, seguir → siguiendo. -Ar and -er verbs normally do not (poder → pudiendo is the exception).",
             tables=[table(["Infinitive", "-ndo form"],
                           [["dormir", "durmiendo"],
                            ["pedir", "pidiendo"],
                            ["decir", "diciendo"],
                            ["servir", "sirviendo"],
                            ["poder", "pudiendo"]],
                           say=[1])]),
        card("What the progressive is not for",
             "In standard Spanish the progressive describes an action that is happening now. For plans use the present, "
             "ir a + infinitive or the future. Also: andar + -ndo shows an activity that goes on over a stretch of time.",
             examples=[
                 ex("Mañana salgo de viaje.", "Tomorrow I am leaving on a trip.", "Mañana salgo"),
                 ex("El bebé está durmiendo.", "The baby is sleeping.", "durmiendo"),
                 ex("Estamos leyendo sobre el clima.", "We are reading about the climate.", "leyendo"),
                 ex("Ando buscando una casa nueva.", "I am looking for a new house.", "Ando buscando"),
             ]),
    ],
    exercises=[
        F("Mi hermano está ___ un libro.", "leyendo", ["leiendo", "leendo", "lido"], "Leer → leyendo.", tr="My brother is reading a book.", lemma="leer:ger"),
        F("Los obreros están ___ una casa.", "construyendo", ["construiendo", "construendo", "construido"], "Construir → construyendo.", tr="The workers are building a house.", lemma="construir:ger"),
        F("El bebé está ___.", "durmiendo", ["dormiendo", "duermiendo", "dormir"], "Dormir → durmiendo.", tr="The baby is sleeping.", lemma="dormir:ger"),
        F("Estoy ___ un café.", "pidiendo", ["pediendo", "pidendo", "pedindo"], "Pedir → pidiendo.", tr="I am ordering a coffee.", lemma="pedir:ger"),
        F("¿Qué está ___ ella?", "diciendo", ["deciendo", "dicendo", "dicido"], "Decir → diciendo.", tr="What is she saying?", lemma="decir:ger"),
        M("Which -ndo form is correct for “creer”?", "creyendo", ["creiendo", "creendo", "creído"], "Between vowels i becomes y."),
        M("Which sentence is standard Spanish for a plan tomorrow?", "Mañana salgo de viaje.", ["Mañana estoy saliendo de viaje.", "Mañana saliendo de viaje.", "Mañana estoy salido de viaje."], "For the future use the present, ir a or the future."),
        M("What does “Ando buscando una casa” suggest?", "an ongoing search", ["a finished search", "a plan for next year", "a sudden action"], "Andar + -ndo shows an ongoing activity."),
        M("Which verb has a stem change in the -ndo form?", "dormir", ["hablar", "comer", "vivir"], "-Ir verbs with a stem change: durmiendo."),
    ],
)

# ---------------------------------------------------------------------------- 111
L111 = lesson(
    "Verbs followed by a + infinitive",
    "empezar a, comenzar a, volver a, aprender a",
    requires=["empezar", "comenzar", "volver", "aprender", "ayudar", "enseñar"],
    cards=[
        card("Begin, return, learn",
             "Some verbs need the preposition a before an infinitive. Empezar a and comenzar a mean “to begin to”. "
             "Volver a + infinitive means to do something AGAIN: Vuelve a llover = It rains again.",
             tables=[table(["Verb + a", "Meaning", "Example"],
                           [["empezar a", "to begin to", "Empiezo a trabajar a las ocho."],
                            ["comenzar a", "to begin to", "Comienza a nevar."],
                            ["volver a", "to do again", "Vuelve a llover."],
                            ["aprender a", "to learn how to", "Aprendo a nadar."],
                            ["enseñar a", "to teach how to", "Mi tía me enseña a esquiar."],
                            ["ayudar a", "to help to", "Ayudo a mi madre a cocinar."]],
                           say=[2])]),
        card("Boot verbs again",
             "Empezar and comenzar are e → ie verbs; volver is o → ue. Nosotros and vosotros keep the original vowel.",
             tables=[table(["", "empezar", "volver"],
                           [["yo", "empiezo", "vuelvo"],
                            ["tú", "empiezas", "vuelves"],
                            ["él, ella, usted", "empieza", "vuelve"],
                            ["nosotros", "empezamos", "volvemos"],
                            ["vosotros", "empezáis", "volvéis"],
                            ["ellos, ellas, ustedes", "empiezan", "vuelven"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Los niños ___ a jugar en el parque.", "empiezan", ["empezan", "empezamos", "empieza"], "Empezar: e → ie, and los niños is they.", tr="The children begin to play in the park.", lemma="empezar:ellos"),
        F("Nosotros ___ a estudiar a las ocho.", "comenzamos", ["comienzamos", "comenzan", "comienzan"], "Nosotros keeps the e: comenzamos.", tr="We begin to study at eight.", lemma="comenzar:nosotros"),
        F("Yo ___ a llamar mañana.", "vuelvo", ["volvo", "vuelves", "volvemos"], "Volver: o → ue; yo vuelvo.", tr="I will call again tomorrow.", lemma="volver:yo"),
        F("Mi tía me ___ a nadar.", "enseña", ["enseñan", "enseño", "enseñas"], "Mi tía is she: enseña.", tr="My aunt teaches me to swim.", lemma="enseñar:ella"),
        F("Tú ___ a hablar con más confianza.", "aprendes", ["aprendo", "aprende", "aprenden"], "Tú takes -es.", tr="You learn to speak with more confidence.", lemma="aprender:tú"),
        M("What does “Vuelve a llover” mean?", "It rains again.", ["It stops raining.", "It is going to snow.", "It returns the rain."], "Volver a + infinitive means again."),
        M("Which is correct?", "Empiezo a estudiar.", ["Empiezo de estudiar.", "Empiezo en estudiar.", "Empiezo estudiar."], "Empezar needs a before an infinitive."),
        M("Which verb is e → ie?", "empezar", ["volver", "jugar", "pedir"], "Empiezo, empiezas, empieza..."),
        M("Which verb is o → ue?", "volver", ["empezar", "comenzar", "querer"], "Vuelvo, vuelves, vuelve..."),
    ],
    verify=vp("empezar", "empiezo", "empiezas", "empieza", "empezamos", "empezáis", "empiezan")
           + vp("comenzar", "comienzo", "comienzas", "comienza", "comenzamos", "comenzáis", "comienzan")
           + vp("volver", "vuelvo", "vuelves", "vuelve", "volvemos", "volvéis", "vuelven"),
)

# ---------------------------------------------------------------------------- 112
L112 = lesson(
    "What to wear in this weather",
    "Cuando llueve, llevo un impermeable.",
    requires=["ropa", "llevar", "usar", "necesitar", "calor", "frío"],
    cards=[
        card("Clothes for the weather",
             "Link the weather and your clothes with cuando (when) and the present tense. Use hay que + infinitive "
             "for what one must do or bring in general.",
             tables=[table(["Tiempo", "Ropa"],
                           [["Cuando hace mucho frío,", "llevo un abrigo, guantes y una bufanda."],
                            ["Cuando llueve,", "uso un impermeable y botas."],
                            ["Cuando hace calor,", "llevo una camiseta y pantalones cortos."],
                            ["Cuando hace sol,", "uso gafas de sol y un sombrero."],
                            ["Cuando nieva,", "necesito botas y un abrigo grueso."]],
                           say=[0, 1])]),
        card("Hay que...",
             "Hay que + infinitive is impersonal: “one must” or “you have to”, for everybody. It never changes.",
             examples=[
                 ex("Hay que llevar un paraguas.", "You have to bring an umbrella.", "Hay que llevar"),
                 ex("En la montaña hay que llevar una chaqueta.", "In the mountains you must wear a jacket.", "hay que"),
                 ex("Para ir a la playa necesito un bañador.", "To go to the beach I need a swimsuit.", "un bañador"),
             ]),
    ],
    exercises=[
        F("Cuando llueve, uso un ___.", "impermeable", ["bañador", "traje", "sombrero de paja"], "A raincoat keeps you dry; un is masculine.", tr="When it rains, I wear a raincoat."),
        F("Hace mucho frío; necesito una ___ y guantes.", "bufanda", ["bañador", "gafas", "sandalia"], "Una is feminine singular, and a scarf is for cold.", tr="It is very cold; I need a scarf and gloves."),
        F("Hoy hace mucho sol; necesito gafas de ___.", "sol", ["lluvia", "nieve", "viento"], "Gafas de sol are sunglasses.", tr="Today it is very sunny; I need sunglasses."),
        F("Para ir a la playa necesito un ___.", "bañador", ["abrigo", "paraguas", "impermeable"], "A swimsuit is for the beach.", tr="To go to the beach I need a swimsuit."),
        M("It is thirty-five degrees and sunny. What do you wear?", "una camiseta y un sombrero", ["un abrigo y botas", "una bufanda y guantes", "un impermeable y botas"], "Hot and sunny weather calls for light clothes."),
        M("It is snowing in the mountains. What do you bring?", "un abrigo grueso y botas", ["un bañador", "unas sandalias", "una camiseta"], "Snow means cold weather."),
        M("What does “Hay que llevar un paraguas” mean?", "You have to bring an umbrella.", ["There is an umbrella.", "I have an umbrella.", "He lost the umbrella."], "Hay que + infinitive = one must."),
        M("Which sentence is correct?", "Hay que ser puntual.", ["Hay que somos puntual.", "Hay que son puntuales.", "Hay que soy puntual."], "Hay que is followed by an infinitive."),
        M("Cuando ___ frío, llevo abrigo. Which verb fits?", "hace", ["es", "está", "tiene"], "Weather with frío: hace."),
    ],
)

# ---------------------------------------------------------------------------- 113
L113 = lesson(
    "Review: weather and the future",
    "hace, hay, estará, está lloviendo",
    requires=["tiempo", "mañana", "siempre", "nunca", "hacer", "estar"],
    cards=[
        card("A weekend in the mountains",
             "Read this short text. Notice the present, the future and the progressive.",
             examples=[
                 ex("Hoy hace sol y la montaña está despejada.", "Today it is sunny and the mountain is clear.", "Hoy hace sol"),
                 ex("Mañana habrá nubes y por la tarde lloverá.", "Tomorrow there will be clouds and in the afternoon it will rain.", "lloverá"),
                 ex("Ahora mis amigos están caminando y yo estoy leyendo.", "Now my friends are walking and I am reading.", "están caminando"),
                 ex("Siempre empezamos a caminar temprano.", "We always start walking early.", "empezamos a caminar"),
                 ex("En esta región nunca nieva en verano.", "In this region it never snows in summer.", "nunca nieva"),
             ]),
    ],
    exercises=[
        F("Hoy ___ mucho viento.", "hace", ["tiene", "está", "es"], "Hace viento: hacer + noun.", tr="Today it is very windy.", lemma="hacer:él"),
        F("Mañana ___ tormenta.", "habrá", ["habrás", "habré", "habremos"], "Impersonal future of haber: habrá.", tr="Tomorrow there will be a storm."),
        F("El cielo ___ nublado.", "está", ["hace", "hay", "es"], "Estar + nublado.", tr="The sky is cloudy."),
        F("En el desierto ___ llueve.", "casi nunca", ["siempre", "mucho", "también"], "Deserts are very dry.", tr="In the desert it almost never rains."),
        F("El sábado nosotros ___ a la playa.", "iremos", ["irán", "iré", "irás"], "Ir is regular in the future: iremos.", tr="On Saturday we will go to the beach.", lemma="ir:nosotros:fut"),
        F("Mi madre está ___ el periódico.", "leyendo", ["leiendo", "lido", "leendo"], "Leer → leyendo.", tr="My mother is reading the newspaper.", lemma="leer:ger"),
        M("Which sentence is a forecast?", "Mañana hará calor.", ["Siempre hace calor.", "Hoy hace calor.", "Ahora hace calor."], "Hará = future."),
        M("Which is correct?", "No llueve nunca aquí.", ["Llueve no nunca aquí.", "No nunca llueve aquí.", "Nunca no llueve aquí."], "Double negative: no + verb + nunca."),
        M("How do you say “We start working” using empezar?", "Empezamos a trabajar.", ["Empezamos trabajar.", "Empezamos de trabajar.", "Empezamos en trabajar."], "Empezar a + infinitive."),
        M("Which unit do forecasts use?", "grados centígrados", ["grados Fahrenheit", "metros", "kilos"], "Celsius."),
    ],
)

UNIT = unit("El tiempo", [L98, L99, L100, L101, L102, L103, L104, L105, L106, L107, L108, L109, L110, L111, L112, L113])

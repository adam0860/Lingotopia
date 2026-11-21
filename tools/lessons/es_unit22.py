"""Unit 22: geography and the environment, the past perfect, the future and the conditional reviewed, se reviewed (textbook Chapter 22)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 391
L391 = lesson(
    "Landforms: mountains, valleys and deserts",
    "La cordillera tiene volcanes, valles y un desierto muy seco.",
    requires=["montaña", "valle", "desierto", "cima", "altura", "tierra", "suelo", "territorio", "paisaje", "región"],
    cards=[
        card("Shapes of the land",
             "These are the basic words for describing what the land looks like. Notice that nouns ending in -a are usually feminine (la montaña, la cima), while el valle, el desierto and el volcán are masculine.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["la montaña", "mountain", "La montaña es muy alta."],
                            ["la cordillera", "mountain range", "La cordillera tiene muchos volcanes."],
                            ["la cima", "summit", "Llegamos a la cima al mediodía."],
                            ["el volcán", "volcano", "El volcán está dormido desde hace años."],
                            ["el valle", "valley", "El valle es verde y fértil."],
                            ["el desierto", "desert", "En el desierto casi nunca llueve."],
                            ["la llanura", "plain", "La llanura es plana y muy grande."],
                            ["la meseta", "plateau", "La ciudad está en una meseta alta."]],
                           say=[2])]),
    ],
    exercises=[
        F("El punto más alto de una montaña es la ___.", "cima", ["costa", "bahía", "isla"], "Summit.", tr="The highest point of a mountain is the summit."),
        F("Una ___ es una zona de tierra plana y muy grande.", "llanura", ["cima", "isla", "montaña"], "Plain.", tr="A plain is a large, flat area of land."),
        F("En el ___ casi nunca llueve y hay mucha arena.", "desierto", ["lago", "valle", "río"], "Desert.", tr="In the desert it almost never rains and there is a lot of sand."),
        F("Un ___ es una montaña que puede echar fuego y ceniza.", "volcán", ["lago", "valle", "desierto"], "Volcano.", tr="A volcano is a mountain that can throw out fire and ash."),
        F("Entre dos montañas hay un ___.", "valle", ["volcán", "mar", "desierto"], "Valley.", tr="Between two mountains there is a valley."),
        F("Una ___ es un grupo de montañas en línea.", "cordillera", ["llanura", "cima", "playa"], "Mountain range.", tr="A mountain range is a group of mountains in a line."),
        M("Which word is masculine?", "el volcán", ["la cima", "la montaña", "la llanura"], "El volcán."),
        M("What is a meseta?", "A high, flat area of land", ["A sea", "A tiny island", "A river"], "Meseta = plateau."),
        M("Which place is usually the driest?", "el desierto", ["el valle", "la selva", "el lago"], "Deserts have little rain."),
    ],
)

# ---------------------------------------------------------------------------- 392
L392 = lesson(
    "Water and coasts: rivers, lakes, seas and islands",
    "El río desemboca en el mar, cerca de una bahía.",
    requires=["río", "lago", "mar", "océano", "costa", "playa", "bahía", "isla", "selva", "nacer", "frontera"],
    cards=[
        card("Where the water is",
             "Rivers are born (nacer) in the mountains and end (desembocar) in the sea. A bay is a part of the sea that cuts into the coast; an island is land surrounded by water; a peninsula is land surrounded by water on three sides.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el río", "river", "El río nace en la montaña."],
                            ["el lago", "lake", "El lago es profundo y frío."],
                            ["el mar", "sea", "El mar está tranquilo hoy."],
                            ["el océano", "ocean", "El océano Pacífico es el más grande."],
                            ["la costa", "coast", "La costa tiene playas muy bonitas."],
                            ["la bahía", "bay", "Los barcos descansan en la bahía."],
                            ["la isla", "island", "La isla está cerca de la costa."],
                            ["la península", "peninsula", "México tiene una península muy famosa."],
                            ["la cascada", "waterfall", "La cascada cae desde una gran altura."]],
                           say=[2])]),
    ],
    exercises=[
        F("El río ___ en la montaña y termina en el mar.", "nace", ["nacen", "nacer", "nazco"], "Singular subject: el río.", tr="The river begins in the mountain and ends in the sea.", lemma="nacer:él"),
        F("Los barcos descansan en la ___.", "bahía", ["cima", "cascada", "llanura"], "Bay.", tr="The boats rest in the bay."),
        F("Una ___ es un trozo de tierra rodeado de agua.", "isla", ["cima", "llanura", "bahía"], "Island.", tr="An island is a piece of land surrounded by water."),
        F("El ___ es una gran masa de agua dulce rodeada de tierra.", "lago", ["océano", "mar", "desierto"], "Lake.", tr="A lake is a large body of fresh water surrounded by land."),
        F("Una ___ es una caída de agua desde un lugar alto.", "cascada", ["bahía", "isla", "cordillera"], "Waterfall.", tr="A waterfall is water falling from a high place."),
        F("Las playas están en la ___.", "costa", ["cima", "selva", "cordillera"], "Coast.", tr="Beaches are on the coast."),
        M("Which one is the largest?", "el océano", ["el lago", "la bahía", "la cascada"], "Ocean > sea > lake."),
        M("What does “desembocar” mean for a river?", "To flow out into the sea", ["To begin in the mountains", "To dry up", "To fall as a waterfall"], "Desembocar = to flow into."),
        M("What is a península?", "Land surrounded by water on three sides", ["A lake in a desert", "A mountain in the sea", "A river with no end"], "Península."),
    ],
    verify=vp("nacer", "nazco", "naces", "nace", "nacemos", "nacéis", "nacen"),
)

# ---------------------------------------------------------------------------- 393
L393 = lesson(
    "Describing a landscape",
    "Un río ancho y largo, una montaña alta, una selva húmeda.",
    requires=["ancho", "largo", "alto", "bajo", "profundo", "seco", "húmedo", "tropical", "frío", "caliente", "grande", "pequeño"],
    cards=[
        card("Adjectives for places",
             "Adjectives agree with the noun in gender and number. Adjectives ending in -e (grande, caliente) or in -al (tropical, natural) have one form for masculine and feminine.",
             tables=[table(["Masculino", "Femenino", "English"],
                           [["un río ancho", "una playa ancha", "wide"],
                            ["un río largo", "una costa larga", "long"],
                            ["un volcán alto", "una montaña alta", "tall, high"],
                            ["un lago profundo", "una bahía profunda", "deep"],
                            ["un clima seco", "una región seca", "dry"],
                            ["un bosque húmedo", "una selva húmeda", "humid, damp"],
                            ["un clima tropical", "una selva tropical", "tropical"],
                            ["un mar cálido", "una playa cálida", "warm"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("El Amazonas es un río muy ___.", "ancho", ["ancha", "anchos", "anchas"], "Río is masculine singular.", tr="The Amazon is a very wide river."),
        F("Las montañas de los Andes son muy ___.", "altas", ["alto", "alta", "altos"], "Montañas is feminine plural.", tr="The mountains of the Andes are very tall."),
        F("La selva tropical es muy ___.", "húmeda", ["húmedo", "húmedos", "húmedas"], "Selva is feminine singular.", tr="The tropical rainforest is very humid."),
        F("El desierto de Atacama es un lugar muy ___.", "seco", ["seca", "secos", "secas"], "Lugar is masculine singular.", tr="The Atacama Desert is a very dry place."),
        F("Los lagos de la región son muy ___.", "profundos", ["profundo", "profunda", "profundas"], "Lagos is masculine plural.", tr="The lakes of the region are very deep."),
        F("La costa de Chile es muy ___.", "larga", ["largo", "largos", "largas"], "Costa is feminine singular.", tr="The coast of Chile is very long."),
        F("En el Caribe hay islas ___.", "tropicales", ["tropical", "tropicals", "tropicalas"], "Islas is plural; -al adjectives add -es.", tr="In the Caribbean there are tropical islands."),
        M("Which adjective has the same form for masculine and feminine?", "grande", ["alto", "ancho", "largo"], "Adjectives in -e do not change for gender."),
        M("How do you make “tropical” plural?", "tropicales", ["tropicals", "tropicalas", "tropicalos"], "Add -es to a final consonant."),
    ],
)

# ---------------------------------------------------------------------------- 394
L394 = lesson(
    "Where is it? Located, bordered, between",
    "Chile está situado entre los Andes y el océano Pacífico.",
    requires=["situado", "ubicado", "norte", "sur", "oeste", "este", "centro", "frontera", "limitar", "entre", "cerca", "lejos"],
    cards=[
        card("Describing where a place is",
             "Besides estar, geography uses está situado/ubicado, se encuentra, queda, and limita con (it borders). Situado and ubicado are adjectives, so they agree with the thing: una ciudad ubicada, un país situado.",
             tables=[table(["Frase", "English"],
                           [["Chile está situado entre los Andes y el Pacífico.", "Chile is located between the Andes and the Pacific."],
                            ["La isla está ubicada en el golfo.", "The island is located in the gulf."],
                            ["Bolivia limita con Perú, Brasil, Paraguay, Argentina y Chile.", "Bolivia borders Peru, Brazil, Paraguay, Argentina and Chile."],
                            ["Quito se encuentra en el norte del Ecuador.", "Quito is in the north of Ecuador."],
                            ["El volcán queda al oeste de la ciudad.", "The volcano is west of the city."]],
                           say=[0])]),
    ],
    exercises=[
        F("Chile está ___ entre los Andes y el Pacífico.", "situado", ["situada", "situados", "situar"], "Chile is masculine singular.", tr="Chile is located between the Andes and the Pacific."),
        F("La isla está ___ cerca de la costa.", "ubicada", ["ubicado", "ubicados", "ubicar"], "Isla is feminine singular.", tr="The island is located near the coast."),
        F("Bolivia ___ con Perú, Brasil, Paraguay, Argentina y Chile.", "limita", ["limitan", "limitar", "limito"], "Bolivia is singular.", tr="Bolivia borders Peru, Brazil, Paraguay, Argentina and Chile.", lemma="limitar:él"),
        F("Quito se ___ en el norte del Ecuador.", "encuentra", ["encuentran", "encontrar", "encuentro"], "Quito is singular.", tr="Quito is in the north of Ecuador.", lemma="encontrar:él"),
        F("Las ciudades están ___ cerca del río.", "ubicadas", ["ubicada", "ubicado", "ubicados"], "Ciudades is feminine plural.", tr="The cities are located near the river."),
        F("El volcán queda al ___ de la ciudad, donde se pone el sol.", "oeste", ["este", "norte", "sur"], "West is where the sun sets.", tr="The volcano lies to the west of the city, where the sun sets."),
        M("Which verb means “to border”?", "limitar", ["encontrar", "ubicar", "nacer"], "Limitar con = to border."),
        M("Why is it “una ciudad ubicada” and “un país ubicado”?", "The adjective agrees with the noun", ["Ubicado is a verb", "The noun agrees with ubicado", "It depends on the continent"], "Adjectives agree."),
        M("Which sentence says where Quito is?", "Quito se encuentra en el norte del Ecuador.", ["Quito nace en el norte del Ecuador.", "Quito limita en el norte.", "Quito desemboca en Ecuador."], "Se encuentra en = is located in."),
    ],
    verify=(vp("limitar", "limito", "limitas", "limita", "limitamos", "limitáis", "limitan")
            + vp("encontrar", "encuentro", "encuentras", "encuentra", "encontramos", "encontráis", "encuentran")),
)

# ---------------------------------------------------------------------------- 395
L395 = lesson(
    "Reading: the Andes and the Amazon",
    "El Amazonas nace en los Andes y desemboca en el Atlántico.",
    requires=["montaña", "país", "continente", "río", "ancho", "nacer", "selva", "especie", "desierto", "seco", "norte"],
    cards=[
        card("Two giants of South America",
             "Read this short description of the continent’s greatest mountains and its greatest river.",
             examples=[
                 ex("La cordillera de los Andes atraviesa siete países: Venezuela, Colombia, Ecuador, Perú, Bolivia, Chile y Argentina.", "The Andes cross seven countries: Venezuela, Colombia, Ecuador, Peru, Bolivia, Chile and Argentina.", "atraviesa"),
                 ex("Es la cordillera más larga del continente americano.", "It is the longest mountain range on the American continent.", "más larga"),
                 ex("El Aconcagua, en Argentina, tiene casi siete mil metros de altura y es la montaña más alta fuera de Asia.", "Aconcagua, in Argentina, is almost seven thousand meters high and is the tallest mountain outside Asia.", "más alta"),
                 ex("El Amazonas es el río más ancho y más caudaloso de las Américas.", "The Amazon is the widest river, and the one carrying the most water, in the Americas.", "más ancho"),
                 ex("Nace en los Andes del Perú y desemboca en el océano Atlántico, en Brasil.", "It begins in the Peruvian Andes and flows into the Atlantic Ocean, in Brazil.", "Nace"),
                 ex("La selva amazónica tiene millones de especies de plantas y animales.", "The Amazon rainforest has millions of species of plants and animals.", "tiene"),
                 ex("En Chile, el desierto de Atacama es uno de los lugares más secos del mundo.", "In Chile, the Atacama Desert is one of the driest places in the world.", "más secos"),
             ]),
    ],
    exercises=[
        F("La cordillera de los Andes ___ siete países.", "atraviesa", ["atraviesan", "atravesar", "atravieso"], "Cordillera is singular.", tr="The Andes cross seven countries.", lemma="atravesar:él"),
        F("El Amazonas ___ en los Andes del Perú.", "nace", ["nacen", "nacer", "nazco"], "El Amazonas is singular.", tr="The Amazon begins in the Peruvian Andes.", lemma="nacer:él"),
        F("El Aconcagua es la montaña más ___ fuera de Asia.", "alta", ["alto", "altas", "altos"], "Montaña is feminine singular.", tr="Aconcagua is the tallest mountain outside Asia."),
        F("La selva amazónica tiene millones de ___ de plantas y animales.", "especies", ["países", "ríos", "cimas"], "Species.", tr="The Amazon rainforest has millions of species of plants and animals."),
        M("How many countries do the Andes cross?", "Seven", ["Three", "Twelve", "Only one"], "Siete países."),
        M("Where does the Amazon flow into the sea?", "Into the Atlantic Ocean, in Brazil", ["Into the Pacific, in Peru", "Into the Caribbean, in Colombia", "Into Lake Titicaca"], "Desemboca en el Atlántico."),
        M("What is special about the Atacama Desert?", "It is one of the driest places in the world", ["It is the coldest place in the world", "It is a tropical jungle", "It is an island"], "Uno de los lugares más secos."),
        M("Where is Aconcagua?", "In Argentina", ["In Peru", "In Chile", "In Brazil"], "En Argentina."),
        M("Which is the widest river in the Americas?", "the Amazon", ["the Andes", "Aconcagua", "the Atacama"], "El Amazonas."),
    ],
    verify=vp("atravesar", "atravieso", "atraviesas", "atraviesa", "atravesamos", "atravesáis", "atraviesan"),
)

# ---------------------------------------------------------------------------- 396
L396 = lesson(
    "Reading: two coasts, or no coast at all",
    "El Salvador es el único país centroamericano sin costa en el Caribe.",
    requires=["país", "costa", "mar", "único", "lago", "perder", "guerra", "frontera", "inglés", "idioma"],
    cards=[
        card("Geography quiz facts",
             "Central America has seven countries, and South America has two without a coast. Read these facts, then answer the exercises.",
             examples=[
                 ex("Centroamérica tiene siete países: Guatemala, Belice, Honduras, El Salvador, Nicaragua, Costa Rica y Panamá.", "Central America has seven countries: Guatemala, Belize, Honduras, El Salvador, Nicaragua, Costa Rica and Panama.", "siete países"),
                 ex("El Salvador es el único país centroamericano sin costa en el mar Caribe; solo tiene costa en el Pacífico.", "El Salvador is the only Central American country with no Caribbean coast; it has only a Pacific coast.", "el único"),
                 ex("En Belice no se habla español como idioma oficial: el idioma oficial es el inglés.", "In Belize Spanish is not the official language: the official language is English.", "el inglés"),
                 ex("En el lago de Nicaragua viven tiburones toro, que pueden vivir en agua dulce.", "Bull sharks, which can live in fresh water, live in Lake Nicaragua.", "viven"),
                 ex("Bolivia y Paraguay son los dos países de Sudamérica que no tienen costa.", "Bolivia and Paraguay are the two South American countries with no coast.", "no tienen"),
                 ex("Bolivia perdió su costa en la guerra del Pacífico, en el siglo diecinueve.", "Bolivia lost its coast in the War of the Pacific, in the nineteenth century.", "perdió"),
             ]),
    ],
    exercises=[
        F("Centroamérica tiene ___ países.", "siete", ["cinco", "nueve", "doce"], "Guatemala, Belice, Honduras, El Salvador, Nicaragua, Costa Rica, Panamá.", tr="Central America has seven countries."),
        F("El Salvador es el único país centroamericano sin ___ en el Caribe.", "costa", ["lago", "río", "cima"], "Only a Pacific coast.", tr="El Salvador is the only Central American country with no coast on the Caribbean."),
        F("En Belice el idioma oficial es el ___.", "inglés", ["español", "francés", "alemán"], "English.", tr="In Belize the official language is English."),
        F("En el lago de Nicaragua ___ tiburones toro, que pueden vivir en agua dulce.", "viven", ["vive", "vivir", "vivo"], "Tiburones is plural.", tr="Bull sharks, which can live in fresh water, live in Lake Nicaragua.", lemma="vivir:ellos"),
        F("Bolivia ___ su costa en la guerra del Pacífico.", "perdió", ["perdieron", "perder", "perdiste"], "Bolivia is singular; finished event.", tr="Bolivia lost its coast in the War of the Pacific.", lemma="perder:él:pret"),
        M("Which two South American countries have no coast?", "Bolivia and Paraguay", ["Chile and Peru", "Ecuador and Colombia", "Brazil and Uruguay"], "Bolivia y Paraguay."),
        M("Which Central American country has no Caribbean coast?", "El Salvador", ["Belize", "Honduras", "Panama"], "El Salvador."),
        M("Which Central American country does not use Spanish as its official language?", "Belize", ["Honduras", "Costa Rica", "Guatemala"], "Belice: English."),
        M("What lives in Lake Nicaragua?", "Bull sharks", ["Whales", "Penguins", "Crocodiles only"], "Tiburones toro."),
    ],
)

# ---------------------------------------------------------------------------- 397
L397 = lesson(
    "Plants and animals",
    "En la selva viven monos, aves, peces y miles de especies de plantas.",
    requires=["animal", "planta", "árbol", "flor", "hoja", "semilla", "especie", "oso", "lobo", "mono", "pájaro", "pez", "tiburón", "ave"],
    cards=[
        card("Living things",
             "Words for plants and animals appear in every news item about the environment. Learn them in groups.",
             tables=[table(["Plantas", "Animales", "English"],
                           [["el árbol", "el oso", "tree / bear"],
                            ["la flor", "el lobo", "flower / wolf"],
                            ["la hoja", "el mono", "leaf / monkey"],
                            ["la semilla", "el pájaro", "seed / bird"],
                            ["la planta", "el pez", "plant / fish"],
                            ["la especie", "el tiburón", "species / shark"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Un ___ es un animal grande que vive en el bosque y a veces come miel.", "oso", ["pez", "tiburón", "pájaro"], "Bear.", tr="A bear is a large animal that lives in the forest and sometimes eats honey."),
        F("El ___ vive en el mar y tiene dientes muy grandes.", "tiburón", ["mono", "lobo", "oso"], "Shark.", tr="The shark lives in the sea and has very big teeth."),
        F("De cada ___ sale una planta nueva.", "semilla", ["hoja", "flor", "especie"], "Seed.", tr="A new plant comes out of each seed."),
        F("El ___ es un animal que sube a los árboles y come frutas.", "mono", ["lobo", "pez", "tiburón"], "Monkey.", tr="The monkey is an animal that climbs trees and eats fruit."),
        F("Un ___ vive en el agua y respira por las branquias.", "pez", ["pájaro", "mono", "lobo"], "Fish.", tr="A fish lives in water and breathes through gills."),
        F("Un ___ tiene alas y puede volar.", "pájaro", ["pez", "oso", "lobo"], "Bird.", tr="A bird has wings and can fly."),
        M("What do the words oso, lobo and mono have in common?", "They are all animals", ["They are all plants", "They are all rivers", "They are all verbs"], "Animales."),
        M("Which word means “species”?", "especie", ["semilla", "planta", "hoja"], "Especie."),
        M("Which one is a part of a tree?", "la hoja", ["el pez", "el lobo", "el oso"], "Leaf."),
    ],
)

# ---------------------------------------------------------------------------- 398
L398 = lesson(
    "Reading: a continent of many species",
    "Colombia tiene más especies de aves que cualquier otro país.",
    requires=["especie", "ave", "animal", "planta", "isla", "peligro", "árbol", "destruir", "proteger", "parque", "reserva", "único"],
    cards=[
        card("Biodiversity in Latin America",
             "Latin America holds some of the richest places on Earth for plants and animals. Read about it, then work on the exercises.",
             examples=[
                 ex("Brasil, Colombia, Ecuador, Perú, México y Venezuela están entre los países con más especies del planeta.", "Brazil, Colombia, Ecuador, Peru, Mexico and Venezuela are among the countries with the most species on the planet.", "están"),
                 ex("Colombia es el país con más especies de aves del mundo.", "Colombia is the country with the most bird species in the world.", "más"),
                 ex("En las islas Galápagos, en Ecuador, viven animales que no existen en ningún otro lugar, como la tortuga gigante de las Galápagos.", "On the Galápagos Islands, in Ecuador, live animals that exist nowhere else, such as the Galápagos giant tortoise.", "no existen"),
                 ex("Muchas especies están en peligro de extinción porque la gente destruye los bosques donde viven.", "Many species are in danger of extinction because people destroy the forests where they live.", "destruye"),
                 ex("Por eso muchos países han creado parques y reservas para proteger la naturaleza.", "That is why many countries have created parks and reserves to protect nature.", "han creado"),
             ]),
    ],
    exercises=[
        F("Colombia es el país con más especies de ___ del mundo.", "aves", ["osos", "peces", "lobos"], "Birds.", tr="Colombia is the country with the most bird species in the world."),
        F("En las islas Galápagos viven animales que no ___ en ningún otro lugar.", "existen", ["existe", "existir", "existo"], "Animales is plural.", tr="On the Galápagos Islands live animals that exist nowhere else.", lemma="existir:ellos"),
        F("Muchas especies están en ___ de extinción.", "peligro", ["parque", "isla", "reserva"], "Danger.", tr="Many species are in danger of extinction."),
        F("La gente ___ los bosques donde viven muchos animales.", "destruye", ["destruyen", "destruir", "destruyo"], "La gente is singular.", tr="People destroy the forests where many animals live.", lemma="destruir:él"),
        F("Muchos países han creado parques para ___ la naturaleza.", "proteger", ["protegen", "protejo", "protegió"], "After para: infinitive.", tr="Many countries have created parks to protect nature."),
        M("Which country has the most bird species in the world?", "Colombia", ["Chile", "Bolivia", "Uruguay"], "Colombia."),
        M("Where does the Galápagos giant tortoise live?", "On the Galápagos Islands", ["In Patagonia", "In the Amazon only", "In Cuba"], "Galápagos."),
        M("Why are many species in danger?", "People destroy the forests where they live", ["They are too small", "Rivers are too wide", "There are too few mountains"], "Destruir los bosques."),
        M("What have many countries created to protect nature?", "Parks and reserves", ["Skyscrapers", "Highways", "Airports"], "Parques y reservas."),
    ],
    verify=(vp("existir", "existo", "existes", "existe", "existimos", "existís", "existen")
            + vp("destruir", "destruyo", "destruyes", "destruye", "destruimos", "destruís", "destruyen")),
)

# ---------------------------------------------------------------------------- 399
L399 = lesson(
    "Climate change: key words",
    "El calentamiento global derrite los glaciares y sube el nivel del mar.",
    requires=["cambio", "clima", "temperatura", "hielo", "nivel", "mar", "emisión", "gas", "energía", "planeta", "calor"],
    cards=[
        card("The vocabulary of the climate",
             "Climate stories use a small set of words again and again. Learn them together.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el cambio climático", "climate change", "El cambio climático afecta a todo el planeta."],
                            ["el calentamiento global", "global warming", "El calentamiento global sube la temperatura."],
                            ["el glaciar", "glacier", "Los glaciares son grandes masas de hielo."],
                            ["el deshielo", "melting, thaw", "El deshielo hace subir el nivel del mar."],
                            ["la sequía", "drought", "La sequía dura meses sin lluvia."],
                            ["las emisiones", "emissions", "Las emisiones de gases calientan la atmósfera."],
                            ["el nivel del mar", "sea level", "El nivel del mar sube cada año."]],
                           say=[2])]),
    ],
    exercises=[
        F("El ___ global es la subida de la temperatura del planeta.", "calentamiento", ["deshielo", "glaciar", "nivel"], "Global warming.", tr="Global warming is the rise in the planet’s temperature."),
        F("Una ___ es un periodo largo sin lluvia.", "sequía", ["bahía", "cascada", "semilla"], "Drought.", tr="A drought is a long period without rain."),
        F("Un ___ es una gran masa de hielo en una montaña.", "glaciar", ["volcán", "valle", "lago"], "Glacier.", tr="A glacier is a large mass of ice on a mountain."),
        F("Cuando el hielo se derrite, el ___ del mar sube.", "nivel", ["glaciar", "desierto", "valle"], "Sea level.", tr="When the ice melts, the sea level rises."),
        F("Las ___ de gases contaminan el aire.", "emisiones", ["semillas", "sequías", "cimas"], "Emissions.", tr="Gas emissions pollute the air."),
        F("El ___ de los glaciares sube el nivel del mar.", "deshielo", ["nivel", "volcán", "desierto"], "The thaw.", tr="The melting of the glaciers raises the sea level."),
        M("Which word means “drought”?", "la sequía", ["el glaciar", "el deshielo", "la emisión"], "Sequía."),
        M("What does “el cambio climático” mean?", "climate change", ["a change of address", "a weather forecast", "a type of cloud"], "Cambio climático."),
        M("What happens to sea level when glaciers melt?", "It rises", ["It falls", "It stays exactly the same", "It freezes"], "Sube."),
    ],
)

# ---------------------------------------------------------------------------- 400
L400 = lesson(
    "Threats to the environment",
    "La tala de árboles, la basura y el plástico destruyen la naturaleza.",
    requires=["destruir", "proteger", "conservar", "quemar", "contaminación", "basura", "plástico", "árbol", "amenaza", "peligro", "daño", "recurso"],
    cards=[
        card("Problems and what to do about them",
             "Here are the main threats to the environment, and the verbs people use to describe them and to fight them.",
             tables=[table(["Amenaza", "English", "Ejemplo"],
                           [["la deforestación", "deforestation", "La deforestación destruye los hábitats de los animales."],
                            ["la tala", "tree cutting, logging", "La tala ilegal es un problema grave."],
                            ["la contaminación", "pollution", "La contaminación del agua enferma a la gente."],
                            ["la basura", "trash", "Mucha basura llega al mar."],
                            ["el plástico", "plastic", "El plástico tarda siglos en desaparecer."],
                            ["la minería", "mining", "La minería puede contaminar los ríos."]],
                           say=[2]),
                    table(["Verbo", "English", "Ejemplo"],
                          [["destruir", "to destroy", "El fuego destruye el bosque."],
                           ["proteger", "to protect", "Los parques protegen la naturaleza."],
                           ["conservar", "to conserve", "Debemos conservar los recursos."],
                           ["quemar", "to burn", "Algunos agricultores queman el bosque."]],
                          say=[2])]),
    ],
    exercises=[
        F("La ___ de árboles destruye los hábitats de muchos animales.", "tala", ["isla", "cima", "playa"], "Logging.", tr="Cutting down trees destroys the habitats of many animals."),
        F("La ___ del agua enferma a mucha gente.", "contaminación", ["cascada", "cordillera", "bahía"], "Pollution.", tr="Water pollution makes many people sick."),
        F("Los parques ___ la naturaleza.", "protegen", ["protege", "proteger", "protejo"], "Parques is plural.", tr="Parks protect nature.", lemma="proteger:ellos"),
        F("El fuego ___ el bosque en pocas horas.", "destruye", ["destruyen", "destruir", "destruyo"], "Fuego is singular.", tr="The fire destroys the forest in a few hours.", lemma="destruir:él"),
        F("Debemos ___ los recursos naturales.", "conservar", ["conserva", "conservo", "conservan"], "After debemos: infinitive.", tr="We must conserve natural resources."),
        F("Algunos agricultores ___ el bosque para tener más tierra.", "queman", ["quema", "quemar", "quemo"], "Agricultores is plural.", tr="Some farmers burn the forest to have more land.", lemma="quemar:ellos"),
        M("Which of these is a threat to the sea?", "la basura de plástico", ["las hojas", "las semillas", "las flores"], "Plastic trash."),
        M("Which verb means “to protect”?", "proteger", ["destruir", "quemar", "contaminar"], "Proteger."),
        M("What does la minería mean?", "mining", ["farming", "fishing", "tourism"], "Minería."),
    ],
    verify=(vp("proteger", "protejo", "proteges", "protege", "protegemos", "protegéis", "protegen")
            + vp("quemar", "quemo", "quemas", "quema", "quemamos", "quemáis", "queman")),
)

# ---------------------------------------------------------------------------- 401
L401 = lesson(
    "Reading: melting glaciers and rising seas",
    "Los glaciares de los Andes se están derritiendo.",
    requires=["hielo", "ciudad", "agua", "depender", "problema", "isla", "nivel", "sufrir", "científico", "proteger", "árbol"],
    cards=[
        card("How the changing climate is felt",
             "Read this short article on glaciers and coasts, then answer the questions.",
             examples=[
                 ex("Los glaciares de los Andes tropicales se están derritiendo muy rápido.", "The glaciers of the tropical Andes are melting very fast.", "se están derritiendo"),
                 ex("En Bolivia, el glaciar de Chacaltaya desapareció hace años.", "In Bolivia, the Chacaltaya glacier disappeared years ago.", "desapareció"),
                 ex("Cuando un glaciar desaparece, las ciudades que dependen de su agua tienen problemas.", "When a glacier disappears, the cities that depend on its water have problems.", "dependen"),
                 ex("En el Caribe, el nivel del mar sube y amenaza a las islas bajas y a las playas.", "In the Caribbean, the sea level is rising and threatens low islands and beaches.", "amenaza"),
                 ex("Los arrecifes de coral, que protegen la costa y dan hogar a miles de peces, sufren por el agua caliente.", "Coral reefs, which protect the coast and house thousands of fish, suffer from the warm water.", "sufren"),
                 ex("Los científicos piden reducir las emisiones y proteger los bosques.", "Scientists ask for emissions to be reduced and forests to be protected.", "piden"),
             ]),
    ],
    exercises=[
        F("En Bolivia, el glaciar de Chacaltaya ___ hace años.", "desapareció", ["desaparecieron", "desaparecer", "desaparece"], "Hace años + a finished event: preterite.", tr="In Bolivia, the Chacaltaya glacier disappeared years ago.", lemma="desaparecer:él:pret"),
        F("Las ciudades que ___ del agua de los glaciares tienen problemas.", "dependen", ["depende", "depender", "dependo"], "Ciudades is plural.", tr="Cities that depend on glacier water have problems.", lemma="depender:ellos"),
        F("Los arrecifes de coral ___ por el agua caliente.", "sufren", ["sufre", "sufrir", "sufro"], "Arrecifes is plural.", tr="Coral reefs suffer from warm water.", lemma="sufrir:ellos"),
        F("Los científicos ___ reducir las emisiones.", "piden", ["pide", "pedir", "pido"], "Científicos is plural.", tr="Scientists ask for emissions to be reduced.", lemma="pedir:ellos"),
        M("What is happening to the Andean glaciers?", "They are melting fast", ["They are growing", "They are moving south", "They are being sold"], "Se están derritiendo."),
        M("Who is threatened by rising seas in the Caribbean?", "Low islands and beaches", ["Mountain villages", "Desert cities", "Rain forests"], "Islas bajas y playas."),
        M("Why do coral reefs suffer?", "Because of warm water", ["Because of too much rain", "Because of snow", "Because of volcanoes"], "El agua caliente."),
        M("What do scientists recommend?", "Reduce emissions and protect forests", ["Burn more fuel", "Cut more trees", "Build more roads"], "Reducir las emisiones."),
        M("Which cities depend on glacier water?", "Cities near the Andes", ["Cities on the coast of Cuba", "Cities in the Atacama only", "Cities in Spain"], "Cerca de los glaciares."),
    ],
    verify=(vp("depender", "dependo", "dependes", "depende", "dependemos", "dependéis", "dependen")
            + vp("sufrir", "sufro", "sufres", "sufre", "sufrimos", "sufrís", "sufren")
            + vpp("desaparecer", "desaparecí", "desapareciste", "desapareció", "desaparecimos", "desaparecisteis", "desaparecieron")),
)

# ---------------------------------------------------------------------------- 402
L402 = lesson(
    "The past perfect: había + participle",
    "Yo ya había comido. Ellos habían llegado.",
    requires=["haber", "comer", "vivir", "hablar", "llegar", "salir", "terminar"],
    cards=[
        card("Forming the past perfect",
             "The past perfect (el pluscuamperfecto) is haber in the imperfect plus the past participle. It works just like the present perfect, but the helper is in the past. The participle never changes.",
             tables=[table(["Sujeto", "haber", "hablar", "comer", "vivir"],
                           [["yo", "había", "había hablado", "había comido", "había vivido"],
                            ["tú", "habías", "habías hablado", "habías comido", "habías vivido"],
                            ["él, ella, usted", "había", "había hablado", "había comido", "había vivido"],
                            ["nosotros", "habíamos", "habíamos hablado", "habíamos comido", "habíamos vivido"],
                            ["vosotros", "habíais", "habíais hablado", "habíais comido", "habíais vivido"],
                            ["ellos, ustedes", "habían", "habían hablado", "habían comido", "habían vivido"]],
                           say=[1, 2, 3, 4])]),
    ],
    exercises=[
        F("Yo ya ___ comido cuando llegaste.", "había", ["habías", "habíamos", "habían"], "Yo → había.", tr="I had already eaten when you arrived.", lemma="haber:yo:impf"),
        F("Tú ya ___ salido cuando llamé.", "habías", ["había", "habíamos", "habían"], "Tú → habías.", tr="You had already left when I called.", lemma="haber:tú:impf"),
        F("Nosotros ya ___ terminado el trabajo.", "habíamos", ["había", "habían", "habías"], "Nosotros → habíamos.", tr="We had already finished the work.", lemma="haber:nosotros:impf"),
        F("Ellos ya ___ llegado al hospital.", "habían", ["había", "habíamos", "habías"], "Ellos → habían.", tr="They had already arrived at the hospital.", lemma="haber:ellos:impf"),
        F("Vosotros ya ___ hablado con el médico.", "habíais", ["habían", "habíamos", "habías"], "Vosotros → habíais.", tr="You (all) had already spoken with the doctor.", lemma="haber:vosotros:impf"),
        F("Mi abuela había ___ en esa casa toda su vida.", "vivido", ["vivir", "vivió", "viviendo"], "Past participle of vivir.", tr="My grandmother had lived in that house all her life.", lemma="vivir:part"),
        F("Los científicos ya habían ___ el estudio.", "terminado", ["terminar", "terminó", "terminando"], "Past participle of terminar.", tr="The scientists had already finished the study.", lemma="terminar:part"),
        M("What is the difference between he comido and había comido?", "The helper verb: present versus imperfect", ["The participle", "The meaning of comer", "Nothing"], "Había = imperfect of haber."),
        M("Which sentence is in the past perfect?", "Ellos habían llegado.", ["Ellos han llegado.", "Ellos llegaron.", "Ellos llegan."], "Habían + participle."),
    ],
    verify=vpi("haber", "había", "habías", "había", "habíamos", "habíais", "habían"),
)

# ---------------------------------------------------------------------------- 403
L403 = lesson(
    "The past perfect: the earlier of two past events",
    "Cuando llegué, el tren ya había salido.",
    requires=["haber", "llegar", "salir", "tren", "cuando", "antes", "ya", "médico", "hospital", "clase"],
    cards=[
        card("Before something else in the past",
             "Use the past perfect for an action that was completed before another past moment. Two past events: the one that happened first goes in the past perfect, and the later one is often in the preterite.",
             tables=[table(["Antes (pluscuamperfecto)", "Después (pretérito)", "English"],
                           [["el tren ya había salido", "cuando llegué", "The train had already left when I arrived."],
                            ["ya habíamos comido", "cuando llamaron", "We had already eaten when they called."],
                            ["el médico ya había hablado con ella", "cuando entré", "The doctor had already spoken with her when I came in."],
                            ["habían explorado la selva", "cuando llegó la nueva expedición", "They had explored the jungle when the new expedition arrived."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Cuando llegamos al hospital, el médico ya ___ salido.", "había", ["ha", "hubo", "hay"], "An earlier past event → past perfect.", tr="When we arrived at the hospital, the doctor had already left.", lemma="haber:él:impf"),
        F("Cuando llegué a la clase, mis amigos ya ___ empezado.", "habían", ["había", "han", "habíamos"], "Amigos is plural.", tr="When I arrived at class, my friends had already started.", lemma="haber:ellos:impf"),
        F("Antes de ir a Chile, yo nunca ___ visto una montaña tan alta.", "había", ["habías", "habíamos", "habían"], "Yo → había.", tr="Before going to Chile, I had never seen such a tall mountain.", lemma="haber:yo:impf"),
        F("Cuando llamaste, nosotros ya ___ comido.", "habíamos", ["había", "habían", "habías"], "Nosotros → habíamos.", tr="When you called, we had already eaten.", lemma="haber:nosotros:impf"),
        F("Los franceses ya ___ intentado construir el canal antes.", "habían", ["había", "habíamos", "habíais"], "Franceses is plural.", tr="The French had already tried to build the canal before.", lemma="haber:ellos:impf"),
        F("Cuando salimos del cine, ya ___ llovido.", "había", ["habían", "habíamos", "han"], "Llover is impersonal: había.", tr="When we left the movie theater, it had already rained.", lemma="haber:él:impf"),
        M("In “Cuando llegué, el tren ya había salido”, which happened first?", "The train left", ["I arrived", "They happened at the same time", "Nothing happened"], "Había salido = earlier."),
        M("Which tense usually goes with the later event?", "the preterite", ["the future", "the past perfect", "the command"], "El evento más reciente, en pretérito."),
        M("Which sentence is correct?", "Ya habíamos comido cuando llamaron.", ["Ya hemos comido cuando llamaron.", "Ya habíamos comemos cuando llamaron.", "Habíamos ya comer cuando llamaron."], "habíamos + participle."),
    ],
)

# ---------------------------------------------------------------------------- 404
L404 = lesson(
    "The past perfect: negatives, pronouns and little words",
    "Todavía no habíamos llegado. Ya los habían explorado.",
    requires=["haber", "ver", "explorar", "llegar", "ya", "todavía", "nunca", "antes", "selva", "carta", "escribir", "presidente"],
    cards=[
        card("Same rules as the present perfect",
             "No goes before haber; pronouns also go before haber; ya, todavía, nunca and antes usually go before haber (or at the end of the sentence). Avoid putting them between haber and the participle.",
             tables=[table(["Frase", "English"],
                           [["No habíamos llegado todavía.", "We had not arrived yet."],
                            ["Todavía no habíamos llegado.", "We had not arrived yet."],
                            ["Nunca había visto una selva.", "I had never seen a jungle."],
                            ["La selva: ya la habían explorado antes.", "The jungle: they had already explored it before."],
                            ["Le había escrito una carta al presidente.", "I had written the president a letter."],
                            ["Se la había escrito.", "I had written it to him."]],
                           say=[0])]),
    ],
    exercises=[
        F("Nosotros todavía no ___ llegado cuando empezó la tormenta.", "habíamos", ["habían", "había", "habías"], "Nosotros → habíamos.", tr="We had not yet arrived when the storm began.", lemma="haber:nosotros:impf"),
        F("Yo nunca ___ visto una selva tan grande.", "había", ["habías", "habíamos", "habían"], "Yo → había.", tr="I had never seen such a big jungle.", lemma="haber:yo:impf"),
        F("La selva: ya ___ habían explorado antes.", "la", ["lo", "los", "las"], "Selva is feminine singular.", tr="The jungle: they had already explored it before."),
        F("Los científicos: ya ___ habían visto en el laboratorio.", "los", ["lo", "la", "las"], "Científicos is masculine plural.", tr="The scientists: they had already seen them in the lab."),
        F("A la presidenta ya ___ había escrito una carta.", "le", ["la", "lo", "se"], "Indirect object: a la presidenta.", tr="I had already written a letter to the president."),
        F("La carta a la jefa: ya ___ la había escrito.", "se", ["le", "lo", "te"], "Le + la → se la.", tr="The letter: I had already written it to her."),
        F("A mí, mis padres no ___ habían llamado todavía.", "me", ["se", "lo", "les"], "Indirect object: me.", tr="My parents had not called me yet."),
        M("Which sentence is correct?", "Nunca había estado allí.", ["Había nunca estado allí.", "Había estado nunca allí.", "Nunca estado había allí."], "Nunca goes before haber."),
        M("Where does the pronoun go in “They had seen it”?", "Lo habían visto.", ["Habían lo visto.", "Habían visto lo.", "Habían visto-lo."], "Pronouns before haber."),
    ],
)

# ---------------------------------------------------------------------------- 405
L405 = lesson(
    "Past perfect or preterite?",
    "Ya había estudiado cuando empezó el examen, y por eso lo hice bien.",
    requires=["estudiar", "examen", "hacer", "salir", "primero", "luego", "después", "antes", "llegar", "haber"],
    cards=[
        card("Which one came first?",
             "A story in the past gives its events in order using the preterite. When you step back to something that was already done before the moment you are describing, use the past perfect.",
             tables=[table(["Orden de la historia", "Tiempo", "Ejemplo"],
                           [["Primero A, luego B", "pretérito, pretérito", "Primero estudié y luego hice el examen."],
                            ["A ya estaba hecho cuando B", "pluscuamperfecto, pretérito", "Ya había estudiado cuando empezó el examen."],
                            ["Antes de B, A", "pluscuamperfecto", "Antes del examen, había estudiado mucho."]],
                           say=[2])]),
    ],
    exercises=[
        F("Primero abrimos la ventana y después ___ al jardín.", "salimos", ["habíamos salido", "hemos salido", "saldremos"], "A sequence of finished events: preterite.", tr="First we opened the window and then we went out to the garden.", lemma="salir:nosotros:pret"),
        F("Primero estudié y luego ___ el examen.", "hice", ["había hecho", "he hecho", "haré"], "A sequence: preterite.", tr="First I studied and then I took the exam.", lemma="hacer:yo:pret"),
        F("Ya ___ estudiado la lección antes de la clase, por eso entendí todo.", "había", ["he", "hubo", "hay"], "An earlier past event.", tr="I had already studied the lesson before class, so I understood everything.", lemma="haber:yo:impf"),
        F("Antes de la tormenta, los vecinos ya ___ cerrado las ventanas.", "habían", ["han", "hubieron", "hay"], "Earlier than the storm.", tr="Before the storm, the neighbors had already closed the windows.", lemma="haber:ellos:impf"),
        F("Cuando llegó el doctor, la enfermera ya le ___ puesto la vacuna.", "había", ["habían", "ha", "hay"], "Earlier than the doctor’s arrival.", tr="When the doctor arrived, the nurse had already given him the vaccine.", lemma="haber:ella:impf"),
        M("Which event happened first in “Ya había estudiado cuando empezó el examen”?", "I studied", ["The exam began", "Both at once", "Neither"], "Había estudiado is earlier."),
        M("Which sentence tells events in the order they happened?", "Llegué, comí y me fui.", ["Había llegado, comía y iba.", "He llegado, había comido y me fui.", "Llegando, comido y ido."], "Preterites in sequence."),
        M("What goes with a step back in time?", "the past perfect", ["the present", "the future", "the command"], "Step back → pluscuamperfecto."),
        M("Complete: “Cuando llegué, ya (salir) ...”", "había salido", ["salgo", "saldré", "saliendo"], "Cuando llegué: the earlier event is past perfect."),
    ],
)

# ---------------------------------------------------------------------------- 406
L406 = lesson(
    "Reading: the Panama Canal",
    "Los franceses ya habían intentado construir el canal.",
    requires=["canal", "construir", "intentar", "fracasar", "abandonar", "trabajador", "barco", "océano", "país", "enfermedad", "morir", "proyecto"],
    cards=[
        card("A canal that took two tries",
             "The Panama Canal joins the Atlantic and the Pacific. Notice how the past perfect steps back to explain what had happened before.",
             examples=[
                 ex("En mil ochocientos ochenta y uno, una compañía francesa empezó a construir un canal en Panamá.", "In 1881, a French company began building a canal in Panama.", "empezó"),
                 ex("Los franceses ya habían construido el canal de Suez, pero en Panamá encontraron selva, lluvias y enfermedades.", "The French had already built the Suez Canal, but in Panama they found jungle, rain and disease.", "habían construido"),
                 ex("Murieron muchos trabajadores de fiebre amarilla y de malaria.", "Many workers died of yellow fever and malaria.", "Murieron"),
                 ex("En mil ochocientos ochenta y nueve, la compañía abandonó el proyecto porque había gastado mucho dinero.", "In 1889, the company abandoned the project because it had spent a lot of money.", "había gastado"),
                 ex("Panamá había sido parte de Colombia hasta mil novecientos tres.", "Panama had been part of Colombia until 1903.", "había sido"),
                 ex("Estados Unidos continuó la obra en mil novecientos cuatro, y el canal se abrió en mil novecientos catorce.", "The United States continued the work in 1904, and the canal opened in 1914.", "continuó"),
                 ex("Panamá recibió el control completo del canal el último día de mil novecientos noventa y nueve.", "Panama received full control of the canal on the last day of 1999.", "recibió"),
             ]),
    ],
    exercises=[
        F("Los franceses ya ___ construido el canal de Suez.", "habían", ["había", "han", "hubieron"], "Franceses is plural; earlier event.", tr="The French had already built the Suez Canal.", lemma="haber:ellos:impf"),
        F("La compañía abandonó el proyecto porque ___ gastado mucho dinero.", "había", ["habían", "ha", "hay"], "Compañía is singular; earlier event.", tr="The company abandoned the project because it had spent a lot of money.", lemma="haber:ella:impf"),
        F("Panamá ___ sido parte de Colombia hasta mil novecientos tres.", "había", ["habían", "ha", "hubo"], "Panamá is singular.", tr="Panama had been part of Colombia until 1903.", lemma="haber:él:impf"),
        F("El gobierno de Estados Unidos ___ la obra en mil novecientos cuatro.", "continuó", ["continuaron", "continúa", "continuar"], "Finished event with a date: preterite.", tr="The United States government continued the work in 1904.", lemma="continuar:él:pret"),
        F("Muchos trabajadores ___ de fiebre amarilla.", "murieron", ["murió", "mueren", "morir"], "Trabajadores is plural; finished event.", tr="Many workers died of yellow fever.", lemma="morir:ellos:pret"),
        M("Which came first?", "The French attempt", ["The American work", "Panama’s control of the canal", "The opening in 1914"], "Los franceses empezaron en 1881."),
        M("Why did the French company abandon the project?", "It had spent a lot of money and many workers had died", ["It had finished it", "The ocean dried up", "Panama refused"], "Había gastado mucho dinero."),
        M("When did the canal open?", "In 1914", ["In 1881", "In 1889", "In 1999"], "Mil novecientos catorce."),
        M("What did Panama receive at the end of 1999?", "Full control of the canal", ["A new coast", "A new president", "A treaty with France"], "El control completo."),
    ],
    verify=(vpp("continuar", "continué", "continuaste", "continuó", "continuamos", "continuasteis", "continuaron")
            + vpp("morir", "morí", "moriste", "murió", "morimos", "moristeis", "murieron")),
)

# ---------------------------------------------------------------------------- 407
L407 = lesson(
    "Three ways to talk about the future",
    "Voy a viajar. Viajo mañana. Viajaré el año próximo.",
    requires=["viajar", "ir", "comprar", "terminar", "próximo", "año", "mañana", "tarea", "casa", "estudiar"],
    cards=[
        card("Ir a, the present, and the simple future",
             "Spanish has three common ways to talk about what comes next. Ir a + infinitive is the everyday choice for plans you feel sure about. "
             "The present tense works for scheduled or very near events, with a time word. "
             "The simple future (viajaré, tendré) states strong intentions, promises, dreams and predictions.",
             tables=[table(["Forma", "Ejemplo", "English"],
                           [["ir a + infinitivo", "Voy a viajar a Chile el año próximo.", "I am going to travel to Chile next year."],
                            ["presente + palabra de tiempo", "Termino mi tarea mañana.", "I finish my homework tomorrow."],
                            ["futuro simple", "Compraré una casa en cuatro años.", "I will buy a house in four years."],
                            ["futuro simple", "Me casaré y tendré dos hijos.", "I will get married and have two children."]],
                           say=[1])]),
    ],
    exercises=[
        F("Mañana yo ___ a visitar el volcán.", "voy", ["vas", "va", "vamos"], "Yo → voy (ir a + infinitive).", tr="Tomorrow I am going to visit the volcano.", lemma="ir:yo"),
        F("Dentro de cuatro años yo ___ una casa.", "compraré", ["compré", "comprar", "comprando"], "A plan stated with the simple future.", tr="In four years I will buy a house.", lemma="comprar:yo:fut"),
        F("Mañana por la mañana yo ___ mi tarea.", "termino", ["terminé", "terminando", "terminar"], "The present can talk about the near future with a time word.", tr="Tomorrow morning I finish my homework.", lemma="terminar:yo"),
        F("El año próximo nosotros ___ a Chile.", "viajaremos", ["viajábamos", "viajaron", "viajar"], "Nosotros future: -emos.", tr="Next year we will travel to Chile.", lemma="viajar:nosotros:fut"),
        F("Mis padres ___ en esta casa toda la vida; es una promesa.", "vivirán", ["vivían", "vivieron", "vivir"], "A promise → simple future.", tr="My parents will live in this house all their lives; it is a promise.", lemma="vivir:ellos:fut"),
        F("Esta noche voy a ___ para el examen.", "estudiar", ["estudio", "estudié", "estudiaré"], "After ir a: infinitive.", tr="Tonight I am going to study for the exam."),
        M("Which form states a strong intention or promise?", "the simple future", ["the past perfect", "the imperfect", "the preterite"], "Futuro simple."),
        M("Which is the everyday way to say “I am going to travel”?", "Voy a viajar.", ["Viajé a ir.", "Voy viajado.", "Viajando voy."], "Ir a + infinitive."),
        M("Can the present tense talk about the future?", "Yes, with a time word like mañana", ["No, never", "Only with the verb ser", "Only in questions"], "Mañana termino = tomorrow I finish."),
    ],
    verify=(vpf("viajar", "viajaré", "viajarás", "viajará", "viajaremos", "viajaréis", "viajarán")
            + vpf("comprar", "compraré", "comprarás", "comprará", "compraremos", "compraréis", "comprarán")),
)

# ---------------------------------------------------------------------------- 408
L408 = lesson(
    "The future of probability: I wonder…",
    "¿Dónde estará Héctor? Estará jugando videojuegos.",
    requires=["estar", "ser", "tener", "jugar", "videojuego", "abogado", "juez", "mujer", "hora", "teléfono", "contestar", "edad"],
    cards=[
        card("When the future is about now",
             "The simple future can also express a guess or a doubt about the present. It is the Spanish way of saying “I wonder” or “probably”. "
             "A plain question or statement uses the present (¿Dónde está Héctor?). The future adds the idea of speculation: ¿Dónde estará Héctor? Estará jugando videojuegos.",
             tables=[table(["Pregunta o duda", "Respuesta con probabilidad", "English"],
                           [["¿Dónde estará Héctor?", "Estará jugando videojuegos.", "I wonder where Héctor is. He is probably playing video games."],
                            ["¿Quién será esa mujer?", "Será abogada o jueza.", "I wonder who that woman is. She is probably a lawyer or a judge."],
                            ["¿Qué estará haciendo Luisa?", "Estará estudiando para su examen.", "I wonder what Luisa is doing. She is probably studying for her exam."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Son las nueve y Marta no contesta el teléfono. ¿Dónde ___?", "estará", ["estaba", "estuvo", "estar"], "Wondering about right now → future.", tr="It is nine and Marta does not answer the phone. Where can she be?", lemma="estar:ella:fut"),
        F("Héctor no está en casa. Seguramente ___ jugando videojuegos en casa de un amigo.", "estará", ["estaba", "estuvo", "estar"], "A guess about now → future.", tr="Héctor is not at home. He is probably playing video games at a friend’s house.", lemma="estar:él:fut"),
        F("¿Quién ___ esa mujer que está ahora en la puerta? Nunca la he visto.", "será", ["era", "fue", "ser"], "Wondering about now → future.", tr="Who can that woman be? I have never seen her.", lemma="ser:ella:fut"),
        F("Esa mujer lleva un traje elegante; ___ abogada o jueza.", "será", ["era", "fue", "ser"], "A guess → future.", tr="That woman wears an elegant suit; she is probably a lawyer or a judge.", lemma="ser:ella:fut"),
        F("El paciente tiene fiebre alta; ___ una infección.", "tendrá", ["tenía", "tuvo", "tener"], "A guess about now → future.", tr="The patient has a high fever; he probably has an infection.", lemma="tener:él:fut"),
        F("No sé cuántos años tiene mi vecino. ___ unos cincuenta.", "Tendrá", ["Tenía", "Tuvo", "Tener"], "A guess about now → future.", tr="I don’t know how old my neighbor is. He is probably around fifty.", lemma="tener:él:fut"),
        M("What does “¿Dónde estará Héctor?” express?", "A guess: I wonder where Héctor is", ["A promise about next week", "A command", "A memory from long ago"], "The future of probability."),
        M("Which sentence is a guess about the present?", "Estará en casa.", ["Estaba en casa.", "Estuvo en casa.", "Estar en casa."], "Estará = he is probably."),
        M("In “Será abogada”, the future is about…", "now, not later", ["next year", "yesterday", "a future dream"], "Probability about the present."),
    ],
    verify=(vpf("estar", "estaré", "estarás", "estará", "estaremos", "estaréis", "estarán")
            + vpf("ser", "seré", "serás", "será", "seremos", "seréis", "serán")
            + vpf("tener", "tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán")),
)

# ---------------------------------------------------------------------------- 409
L409 = lesson(
    "Wondering aloud: more probability",
    "¿Cuánto costará? Habrá mucha gente en el hospital.",
    requires=["costar", "haber", "poder", "saber", "decir", "tener", "hora", "gente", "hospital", "tardar", "llegar", "enfermo", "cansado"],
    cards=[
        card("Same idea, other verbs",
             "The future of probability works with any verb. Irregular future stems still apply: habrá (there must be), podrá, sabrá, dirá. For doing-right-now guesses, use estar + gerund: estará durmiendo.",
             tables=[table(["Duda", "Probabilidad", "English"],
                           [["¿Cuánto costará esta medicina?", "Costará unos veinte pesos.", "It probably costs about twenty pesos."],
                            ["¿Qué hora será?", "Serán las cinco.", "It is probably five o’clock."],
                            ["¿Habrá mucha gente en el hospital?", "Habrá mucha gente; es sábado.", "There must be a lot of people; it is Saturday."],
                            ["¿Por qué no llama Luis?", "Estará cansado o enfermo.", "He is probably tired or sick."],
                            ["¿Cuántos años tendrá el médico?", "Tendrá unos cuarenta.", "I wonder how old the doctor is. He is probably about forty."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("No veo el precio. ¿Cuánto ___ esta medicina?", "costará", ["costaba", "costó", "costar"], "Wondering → future.", tr="I can’t see the price. How much might this medicine cost?", lemma="costar:ella:fut"),
        F("Es sábado; ___ mucha gente en el hospital.", "habrá", ["había", "hubo", "haber"], "A guess: there must be.", tr="It is Saturday; there must be many people at the hospital.", lemma="haber:él:fut"),
        F("¿Por qué no llama Luis? ___ cansado o enfermo.", "Estará", ["Estaba", "Estuvo", "Estar"], "A guess about now → future.", tr="Why isn’t Luis calling? He is probably tired or sick.", lemma="estar:él:fut"),
        F("Mi madre no contesta el teléfono; ___ durmiendo.", "estará", ["estaba", "estuvo", "estar"], "A guess about now → future.", tr="My mother does not answer the phone; she is probably sleeping.", lemma="estar:ella:fut"),
        F("¿Cuántos años ___ el médico? Parece muy joven.", "tendrá", ["tenía", "tuvo", "tener"], "Wondering → future of tener.", tr="How old can the doctor be? He looks very young.", lemma="tener:él:fut"),
        F("Nadie lo ___: ¿cuánto durará la sequía?", "sabe", ["sabía", "supo", "saber"], "Nobody knows: present.", tr="Nobody knows: how long will the drought last?", lemma="saber:él"),
        M("Which means “there must be a lot of people”?", "Habrá mucha gente.", ["Había mucha gente.", "Hubo mucha gente.", "Hay mucha gente ayer."], "Habrá = there must be."),
        M("How do you guess what someone is doing right now?", "estará + gerund", ["había + participle", "fue + gerund", "ha + infinitive"], "Estará durmiendo."),
        M("What is the future stem of saber?", "sabr-", ["sab-", "sabe-", "saber-"], "Sabré, sabrás…"),
    ],
    verify=(vpf("costar", "costaré", "costarás", "costará", "costaremos", "costaréis", "costarán")
            + vpf("haber", "habré", "habrás", "habrá", "habremos", "habréis", "habrán")
            + vpf("decir", "diré", "dirás", "dirá", "diremos", "diréis", "dirán")),
)

# ---------------------------------------------------------------------------- 410
L410 = lesson(
    "The conditional: regular verbs",
    "En tu lugar, yo iría al médico.",
    requires=["tomar", "vender", "escribir", "beber", "aceptar", "gastar", "ir", "lugar", "tren", "casa", "carta"],
    cards=[
        card("Would + verb",
             "The conditional says what would happen or what someone would do. Like the future, it is formed by adding endings to the whole infinitive: -ía, -ías, -ía, -íamos, -íais, -ían. "
             "Spanish does not need a separate word for “would”.",
             tables=[table(["Sujeto", "viajar", "comer", "vivir"],
                           [["yo", "viajaría", "comería", "viviría"],
                            ["tú", "viajarías", "comerías", "vivirías"],
                            ["él, ella, usted", "viajaría", "comería", "viviría"],
                            ["nosotros", "viajaríamos", "comeríamos", "viviríamos"],
                            ["vosotros", "viajaríais", "comeríais", "viviríais"],
                            ["ellos, ustedes", "viajarían", "comerían", "vivirían"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        F("En tu lugar, nosotros ___ el tren.", "tomaríamos", ["tomamos", "tomaron", "tomar"], "Nosotros conditional: -íamos.", tr="In your place, we would take the train.", lemma="tomar:nosotros:cond"),
        F("En su lugar, mis padres ___ la casa.", "venderían", ["venden", "vendieron", "vender"], "Ellos conditional: -ían.", tr="In their place, my parents would sell the house.", lemma="vender:ellos:cond"),
        F("En mi lugar, ¿tú ___ ese trabajo?", "aceptarías", ["aceptas", "aceptaste", "aceptar"], "Tú conditional: -ías.", tr="In my place, would you accept that job?", lemma="aceptar:tú:cond"),
        F("En su lugar, yo ___ más agua.", "bebería", ["bebo", "bebí", "beber"], "Yo conditional: -ía.", tr="In his place, I would drink more water.", lemma="beber:yo:cond"),
        F("En tu lugar, mi hermana ___ una carta.", "escribiría", ["escribe", "escribió", "escribir"], "Ella conditional: -ía.", tr="In your place, my sister would write a letter.", lemma="escribir:ella:cond"),
        F("En tu lugar, ellos no ___ tanto dinero.", "gastarían", ["gastan", "gastaron", "gastar"], "Ellos conditional: -ían.", tr="In your place, they would not spend so much money.", lemma="gastar:ellos:cond"),
        F("En tu lugar, yo ___ al médico.", "iría", ["voy", "fui", "ir"], "Yo conditional of ir: iría.", tr="In your place, I would go to the doctor.", lemma="ir:yo:cond"),
        M("To which form do you add the conditional endings?", "The whole infinitive", ["The yo form", "The preterite stem", "The participle"], "Viajar + ía."),
        M("Which sentence means “She would live here”?", "Ella viviría aquí.", ["Ella vivirá aquí.", "Ella vivió aquí.", "Ella vive aquí."], "-ía = would."),
    ],
    verify=(vpd("viajar", "viajaría", "viajarías", "viajaría", "viajaríamos", "viajaríais", "viajarían")
            + vpd("comer", "comería", "comerías", "comería", "comeríamos", "comeríais", "comerían")
            + vpd("vivir", "viviría", "vivirías", "viviría", "viviríamos", "viviríais", "vivirían")),
)

# ---------------------------------------------------------------------------- 411
L411 = lesson(
    "The conditional: irregular stems",
    "En tu lugar, yo diría la verdad y saldría temprano.",
    requires=["decir", "hacer", "poder", "poner", "querer", "saber", "salir", "tener", "venir", "valer", "caber", "haber"],
    cards=[
        card("The same twelve stems as the future",
             "The verbs that are irregular in the future are irregular in the conditional in exactly the same way. Add the conditional endings to these stems.",
             tables=[table(["Infinitivo", "Raíz", "Yo", "Ellos"],
                           [["caber", "cabr-", "cabría", "cabrían"],
                            ["decir", "dir-", "diría", "dirían"],
                            ["haber", "habr-", "habría", "habrían"],
                            ["hacer", "har-", "haría", "harían"],
                            ["poder", "podr-", "podría", "podrían"],
                            ["poner", "pondr-", "pondría", "pondrían"],
                            ["querer", "querr-", "querría", "querrían"],
                            ["saber", "sabr-", "sabría", "sabrían"],
                            ["salir", "saldr-", "saldría", "saldrían"],
                            ["tener", "tendr-", "tendría", "tendrían"],
                            ["valer", "valdr-", "valdría", "valdrían"],
                            ["venir", "vendr-", "vendría", "vendrían"]],
                           say=[2, 3])]),
    ],
    exercises=[
        F("En tu lugar, yo ___ la verdad.", "diría", ["digo", "dije", "decir"], "Decir → dir-.", tr="In your place, I would tell the truth.", lemma="decir:yo:cond"),
        F("En su lugar, ¿tú qué ___?", "harías", ["haces", "hiciste", "hacer"], "Hacer → har-.", tr="In his place, what would you do?", lemma="hacer:tú:cond"),
        F("Si tuviéramos más tiempo, nosotros ___ ayudar más.", "podríamos", ["pudimos", "podían", "poder"], "Poder → podr-.", tr="With more time, we could help more.", lemma="poder:nosotros:cond"),
        F("En su lugar, ella ___ de casa temprano.", "saldría", ["sale", "salió", "salir"], "Salir → saldr-.", tr="In her place, she would leave early.", lemma="salir:ella:cond"),
        F("En mi lugar, ¿ustedes ___ ese trabajo?", "querrían", ["quieren", "quisieron", "querer"], "Querer → querr-.", tr="In my place, would you all want that job?", lemma="querer:ustedes:cond"),
        F("En tu lugar, mis padres ___ a visitarte.", "vendrían", ["vienen", "vinieron", "venir"], "Venir → vendr-.", tr="In your place, my parents would come to visit you.", lemma="venir:ellos:cond"),
        F("En tu lugar, yo no ___ nada a nadie.", "diría", ["dije", "dices", "decir"], "Decir → dir-.", tr="In your place, I would not say anything to anyone.", lemma="decir:yo:cond"),
        M("What is the conditional stem of tener?", "tendr-", ["ten-", "tene-", "tener-"], "Tendría."),
        M("Which verbs have irregular stems in both the future and the conditional?", "The same twelve verbs", ["Only the -ar verbs", "Only reflexive verbs", "None of them"], "Same stems."),
    ],
    verify=(vpd("decir", "diría", "dirías", "diría", "diríamos", "diríais", "dirían")
            + vpd("hacer", "haría", "harías", "haría", "haríamos", "haríais", "harían")
            + vpd("poder", "podría", "podrías", "podría", "podríamos", "podríais", "podrían")
            + vpd("poner", "pondría", "pondrías", "pondría", "pondríamos", "pondríais", "pondrían")
            + vpd("querer", "querría", "querrías", "querría", "querríamos", "querríais", "querrían")
            + vpd("saber", "sabría", "sabrías", "sabría", "sabríamos", "sabríais", "sabrían")
            + vpd("salir", "saldría", "saldrías", "saldría", "saldríamos", "saldríais", "saldrían")
            + vpd("tener", "tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían")
            + vpd("venir", "vendría", "vendrías", "vendría", "vendríamos", "vendríais", "vendrían")
            + vpd("valer", "valdría", "valdrías", "valdría", "valdríamos", "valdríais", "valdrían")
            + vpd("caber", "cabría", "cabrías", "cabría", "cabríamos", "cabríais", "cabrían")
            + vpd("haber", "habría", "habrías", "habría", "habríamos", "habríais", "habrían")),
)

# ---------------------------------------------------------------------------- 412
L412 = lesson(
    "Polite requests and advice with the conditional",
    "¿Podría ayudarme? Yo que tú descansaría.",
    requires=["poder", "ayudar", "gustar", "deber", "importar", "consejo", "descansar", "médico", "lugar", "decir", "ayuda"],
    cards=[
        card("Softening what you say",
             "The conditional makes requests and advice sound polite and less direct. Podría is much softer than puedo; me gustaría is softer than quiero; debería is softer than debo.",
             tables=[table(["Para…", "Frase", "English"],
                           [["pedir un favor", "¿Podría ayudarme, por favor?", "Could you help me, please?"],
                            ["pedir información", "¿Podría decirme dónde está el hospital?", "Could you tell me where the hospital is?"],
                            ["decir un deseo", "Me gustaría hablar con el médico.", "I would like to talk with the doctor."],
                            ["dar un consejo", "Deberías descansar más.", "You should rest more."],
                            ["dar un consejo", "Yo que tú descansaría.", "If I were you, I would rest."],
                            ["ser cortés", "¿Le importaría abrir la ventana?", "Would you mind opening the window?"]],
                           say=[1])]),
    ],
    exercises=[
        F("Perdone, señor, ¿___ decirme dónde está el hospital?", "podría", ["puedo", "pude", "poder"], "Polite request → conditional.", tr="Excuse me, sir, could you tell me where the hospital is?", lemma="poder:usted:cond"),
        F("Me ___ hablar con el médico, por favor.", "gustaría", ["gusta", "gustó", "gustar"], "Polite wish → conditional.", tr="I would like to speak with the doctor, please.", lemma="gustar:él:cond"),
        F("Si quieres sentirte mejor, tú ___ descansar más; estás muy cansado.", "deberías", ["debo", "debiste", "deber"], "Soft advice → conditional.", tr="You should rest more; you are very tired.", lemma="deber:tú:cond"),
        F("Yo que tú, ___ al médico.", "iría", ["voy", "fui", "ir"], "Yo que tú + conditional.", tr="If I were you, I would go to the doctor.", lemma="ir:yo:cond"),
        F("¿Le ___ abrir la ventana, señora?", "importaría", ["importen", "importó", "importar"], "Polite request.", tr="Would you mind opening the window, ma’am?", lemma="importar:él:cond"),
        F("¿Me ___ ayudar con esta carta, por favor?", "podrías", ["pudiste", "podían", "poder"], "Informal polite request → conditional of tú.", tr="Could you help me with this letter, please?", lemma="poder:tú:cond"),
        M("Which request is more polite?", "¿Podría ayudarme?", ["¿Puede ayudarme?", "¡Ayúdeme!", "Ayudarme."], "Podría is softer."),
        M("What does “Yo que tú descansaría” mean?", "If I were you, I would rest", ["I rested yesterday", "I am resting now", "I will rest tomorrow"], "Advice."),
        M("What does the conditional do in a request?", "It makes it softer and more polite", ["It makes it a command", "It puts it in the past", "It makes it a question about the past"], "Cortesía."),
    ],
    verify=(vpd("poder", "podría", "podrías", "podría", "podríamos", "podríais", "podrían")
            + vpd("deber", "debería", "deberías", "debería", "deberíamos", "deberíais", "deberían")
            + vpd("gustar", "gustaría", "gustarías", "gustaría", "gustaríamos", "gustaríais", "gustarían")),
)

# ---------------------------------------------------------------------------- 413
L413 = lesson(
    "Would: conditional or imperfect?",
    "De niño, iba al río. Hoy iría, pero estoy cansado.",
    requires=["niño", "ir", "río", "cansado", "mercado", "sábado", "venir", "decir", "tarde", "llegar"],
    cards=[
        card("Two meanings of “would”",
             "English uses “would” for two different ideas. For something you used to do again and again in the past, Spanish uses the imperfect. "
             "For what would happen or what someone would do under some condition, Spanish uses the conditional. "
             "The conditional also reports what someone said would happen: Dijo que vendría mañana.",
             tables=[table(["Idea", "Tiempo", "Ejemplo"],
                           [["used to (habit)", "imperfecto", "De niño, siempre iba al río."],
                            ["would (hypothetical)", "condicional", "Iría hoy, pero estoy cansado."],
                            ["said it would happen", "condicional", "Dijo que vendría mañana."],
                            ["used to (habit)", "imperfecto", "Todos los sábados íbamos al mercado."]],
                           say=[2])]),
    ],
    exercises=[
        F("De niña, mi abuela siempre ___ al mercado los sábados.", "iba", ["iría", "irá", "fue"], "A habit in the past → imperfect.", tr="As a girl, my grandmother always went to the market on Saturdays.", lemma="ir:ella:impf"),
        F("Si no estuviera tan cansado, hoy ___ a correr.", "iría", ["fui", "iré", "voi"], "Hypothetical → conditional.", tr="If I weren’t so tired, I would go running today.", lemma="ir:yo:cond"),
        F("Mi hermano dijo que ___ mañana.", "vendría", ["vienes", "vino", "venir"], "Reporting a future plan → conditional.", tr="My brother said that he would come tomorrow.", lemma="venir:él:cond"),
        F("Cuando éramos niños, todos los veranos ___ al río.", "íbamos", ["iríamos", "iremos", "fuimos"], "A habit in the past → imperfect.", tr="When we were children, every summer we would go to the river.", lemma="ir:nosotros:impf"),
        F("La médica dijo que ___ más tarde.", "llegaría", ["llegas", "llegaron", "llegar"], "Reporting a future plan → conditional.", tr="The doctor said that she would arrive later.", lemma="llegar:ella:cond"),
        F("Antes, yo siempre ___ a pie al trabajo.", "iba", ["iría", "iré", "fui"], "A habit in the past → imperfect.", tr="Before, I would always walk to work.", lemma="ir:yo:impf"),
        M("In “De niño, iba al río”, what does the imperfect express?", "A repeated habit in the past", ["A hypothetical situation", "A promise", "A future plan"], "Used to."),
        M("Which sentence reports what someone said would happen?", "Dijo que vendría mañana.", ["Dice que viene hoy.", "Dijo que vino ayer.", "Dirá que vino."], "Dijo que + conditional."),
        M("Which tense does Spanish use for a habit that English expresses with “would”?", "the imperfect", ["the conditional", "the future", "the past perfect"], "Imperfecto."),
    ],
)

# ---------------------------------------------------------------------------- 414
L414 = lesson(
    "What would happen? Climate scenarios",
    "En un mundo sin glaciares, el nivel del mar subiría muchos metros.",
    requires=["nivel", "mar", "isla", "ciudad", "costa", "poder", "haber", "tener", "agricultor", "valer", "incendio", "cambio"],
    cards=[
        card("Imagining a changed world",
             "The conditional is the tense of scenarios. Reports on the climate often describe what would happen if nothing changed. Notice how the verbs that describe the scenario are in the conditional, and how haber (habría) stays singular.",
             examples=[
                 ex("En un mundo sin glaciares, el nivel del mar subiría muchos metros.", "In a world without glaciers, the sea level would rise many meters.", "subiría"),
                 ex("Muchas islas quedarían bajo el agua.", "Many islands would end up under water.", "quedarían"),
                 ex("Las ciudades de la costa tendrían problemas muy graves.", "Coastal cities would have very serious problems.", "tendrían"),
                 ex("Los agricultores no podrían cultivar en algunas regiones.", "Farmers could not grow crops in some regions.", "podrían"),
                 ex("Habría más incendios, más sequías y más inundaciones.", "There would be more fires, more droughts and more floods.", "Habría"),
                 ex("¿Valdría la pena actuar hoy? Casi todos los científicos creen que sí.", "Would it be worth acting today? Almost all scientists think so.", "Valdría"),
             ]),
    ],
    exercises=[
        F("En un mundo sin glaciares, el nivel del mar ___ muchos metros.", "subiría", ["subió", "subiendo", "subir"], "A scenario → conditional.", tr="In a world without glaciers, the sea level would rise many meters.", lemma="subir:él:cond"),
        F("En ese mundo, muchas islas ___ bajo el agua.", "quedarían", ["quedaron", "quedando", "quedar"], "A scenario → conditional.", tr="In that world, many islands would end up under water.", lemma="quedar:ellos:cond"),
        F("En un mundo sin glaciares, las ciudades de la costa ___ problemas muy graves.", "tendrían", ["tuvieron", "teniendo", "tener"], "A scenario → conditional.", tr="Coastal cities would have very serious problems.", lemma="tener:ellos:cond"),
        F("En un mundo sin glaciares, los agricultores no ___ cultivar en algunas regiones.", "podrían", ["pudieron", "pudiendo", "poder"], "A scenario → conditional.", tr="Farmers could not grow crops in some regions.", lemma="poder:ellos:cond"),
        F("En un mundo sin glaciares, ___ más incendios, sequías e inundaciones.", "habría", ["habían", "hubo", "haber"], "Impersonal haber stays singular.", tr="There would be more fires, droughts and floods.", lemma="haber:él:cond"),
        F("Si nadie cambia nada, ¿___ la pena actuar hoy?", "valdría", ["valió", "valiendo", "valer"], "A hypothetical question → conditional.", tr="Would it be worth acting today?", lemma="valer:él:cond"),
        M("What does the conditional describe in these sentences?", "What would happen in an imagined scenario", ["What happened last year", "What is happening now", "A command"], "Escenarios."),
        M("Which form is correct for “there would be more floods”?", "Habría más inundaciones.", ["Habrían más inundaciones.", "Hubo más inundaciones.", "Han habido más inundaciones."], "Habría is singular."),
        M("Which tense do you use for “many islands would disappear”?", "the conditional", ["the preterite", "the past perfect", "the command"], "Desaparecerían."),
    ],
)

# ---------------------------------------------------------------------------- 415
L415 = lesson(
    "Se review: reflexive and reciprocal",
    "Yo me despierto a las siete. Los alumnos se miraron.",
    requires=["despertar", "levantar", "mirar", "ver", "querer", "abrazar", "alumno", "padre", "mañana", "temprano"],
    cards=[
        card("Same pronouns, different jobs",
             "The pronouns me, te, se, nos, os show up again and again. Se is the form for the third person (usted, él, ella, ustedes, ellos, ellas). "
             "With a reflexive verb, the action returns to the subject: Yo me despierto. "
             "With a reciprocal meaning, two or more people act on each other: Los alumnos se miraron (they looked at each other). This normally needs a plural (or collective) subject.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["reflexivo", "Yo me despierto a las siete.", "I wake up at seven."],
                            ["reflexivo", "Mauricio se despierta a las ocho.", "Mauricio wakes up at eight."],
                            ["recíproco", "Los alumnos se miraron.", "The students looked at each other."],
                            ["recíproco", "Nos dijimos adiós.", "We said goodbye to each other."],
                            ["recíproco", "Mis padres se abrazaron.", "My parents hugged each other."]],
                           say=[1])]),
    ],
    exercises=[
        F("Yo ___ despierto a las siete.", "me", ["te", "se", "nos"], "Yo → me.", tr="I wake up at seven."),
        F("Mauricio ___ despierta a las ocho.", "se", ["me", "te", "nos"], "Él → se.", tr="Mauricio wakes up at eight."),
        F("Tú ___ levantas muy temprano.", "te", ["me", "se", "nos"], "Tú → te.", tr="You get up very early."),
        F("Nosotros ___ vemos todos los días.", "nos", ["me", "te", "se"], "Reciprocal: nos.", tr="We see each other every day."),
        F("Mis padres ___ abrazaron cuando se vieron.", "se", ["me", "te", "nos"], "Ellos → se.", tr="My parents hugged each other when they saw each other."),
        F("Los alumnos ___ miraron y no dijeron nada.", "se", ["me", "te", "nos"], "Ellos → se.", tr="The students looked at each other and said nothing."),
        M("In “Nos dijimos adiós”, who said goodbye to whom?", "Each of us to the other", ["I said goodbye to myself", "Someone else said it", "Nobody did"], "Reciprocal."),
        M("Why does a reciprocal se normally need a plural subject?", "Because at least two people must act on each other", ["Because se is always plural", "Because it is a command", "Because it is a question"], "Reciprocal needs two or more."),
        M("Which sentence is reflexive?", "Yo me despierto a las siete.", ["Nos dijimos adiós.", "Los alumnos se miraron.", "Se cerró la puerta."], "The action returns to the subject."),
    ],
)

# ---------------------------------------------------------------------------- 416
L416 = lesson(
    "Se review: se lo, and the impersonal se",
    "Se lo regalé ayer. ¿Qué se puede hacer?",
    requires=["regalar", "pagar", "perro", "madre", "empleado", "poder", "hacer", "vivir", "bien", "ciudad"],
    cards=[
        card("Se instead of le or les, and se for “one”",
             "Before lo, la, los, las, the pronouns le and les become se: Le regalé un perro a mi madre → Se lo regalé. "
             "Impersonal se talks about people in general, with no one in particular: ¿Qué se puede hacer? Se vive bien aquí. The verb stays in the third-person singular.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["se = le", "Le regalé un perro a mi madre.", "I gave my mother a dog."],
                            ["se = le", "Se lo regalé ayer.", "I gave it to her yesterday."],
                            ["se = les", "Les pagué el peaje. Se lo pagué todo.", "I paid them the toll. I paid it all to them."],
                            ["impersonal", "¿Qué se puede hacer?", "What can one do?"],
                            ["impersonal", "En esta ciudad se vive bien.", "One lives well in this city."]],
                           say=[1])]),
    ],
    exercises=[
        F("Le regalé un perro a mi madre. ___ lo regalé ayer.", "Se", ["Le", "Lo", "Me"], "Le + lo → se lo.", tr="I gave my mother a dog. I gave it to her yesterday."),
        F("El dinero, ya ___ pagué a los empleados.", "se lo", ["les lo", "los lo", "le lo"], "Les + lo → se lo.", tr="I already paid the employees the money."),
        F("¿Qué ___ puede hacer en esta situación?", "se", ["me", "te", "nos"], "Impersonal se.", tr="What can one do in this situation?"),
        F("En esta ciudad ___ vive muy bien.", "se", ["me", "te", "nos"], "Impersonal se.", tr="In this city one lives very well."),
        F("Los libros, ___ los di a mis alumnos ayer.", "se", ["les", "los", "me"], "Les + los → se los.", tr="The books, I gave them to my students yesterday."),
        F("La carta, ___ la escribí a mi jefe esta mañana.", "se", ["le", "les", "lo"], "Le + la → se la.", tr="The letter, I wrote it to my boss this morning."),
        M("Why is it “se lo” and not “le lo”?", "Le becomes se before lo, la, los, las", ["Se is more polite", "Le is plural", "Lo is feminine"], "Two pronouns starting with l- sound awkward."),
        M("What does “¿Qué se puede hacer?” mean?", "What can one do", ["What did I do", "What did they do yesterday", "What will you do"], "Impersonal se."),
        M("Which verb form goes with the impersonal se?", "third person singular", ["first person plural", "second person singular", "the infinitive"], "Se vive, se puede."),
    ],
)

# ---------------------------------------------------------------------------- 417
L417 = lesson(
    "Se review: the passive se and the accidental se",
    "Se desviaron varios ríos. A Tanya se le cayó el libro.",
    requires=["explotar", "alcanzar", "fabricar", "caer", "olvidar", "recurso", "río", "meta", "libro", "llave"],
    cards=[
        card("Two se-constructions with the noun as subject",
             "The passive se names no doer: Se explotaron los recursos naturales (the resources were exploited). The verb agrees with the noun that follows. "
             "The accidental se adds an indirect pronoun to show who it happened to: A Tanya se le cayó el libro.",
             tables=[table(["Uso", "Ejemplo", "English"],
                           [["se pasivo", "Se explotaron los recursos naturales.", "The natural resources were exploited."],
                            ["se pasivo", "Se desviaron varios ríos para construir la presa.", "Several rivers were diverted to build the dam."],
                            ["se pasivo", "Aquí se fabrican productos reciclables.", "Recyclable products are made here."],
                            ["se accidental", "A Tanya se le cayó el libro.", "Tanya dropped the book."],
                            ["se accidental", "Se nos olvidaron las llaves.", "We forgot the keys."]],
                           say=[1])]),
    ],
    exercises=[
        F("Se ___ los recursos naturales de la zona.", "explotaron", ["explotó", "explotar", "explotamos"], "Recursos is plural.", tr="The natural resources of the area were exploited.", lemma="explotar:ellos:pret"),
        F("Este año se ___ todas las metas de la compañía.", "alcanzaron", ["alcanzó", "alcanzar", "alcanzamos"], "Metas is plural.", tr="This year all the company’s goals were reached.", lemma="alcanzar:ellos:pret"),
        F("Aquí se ___ productos reciclables.", "fabrican", ["fabrica", "fabricar", "fabricamos"], "Productos is plural.", tr="Recyclable products are made here.", lemma="fabricar:ellos"),
        F("A Tanya se le ___ el libro.", "cayó", ["cayeron", "caer", "caí"], "Libro is singular.", tr="Tanya dropped the book.", lemma="caer:él:pret"),
        F("Se nos ___ las llaves.", "olvidaron", ["olvidó", "olvidar", "olvidamos"], "Llaves is plural.", tr="We forgot the keys.", lemma="olvidar:ellos:pret"),
        F("A los niños se ___ cayeron los juguetes.", "les", ["le", "se", "nos"], "A los niños → les.", tr="The children dropped their toys."),
        M("What is missing in the passive se compared with the accidental se?", "The indirect pronoun that shows who it happened to", ["The verb", "The subject", "The noun"], "Se me cayó vs Se cayó."),
        M("In “Se explotaron los recursos”, why is the verb plural?", "It agrees with los recursos", ["It agrees with se", "It agrees with the speaker", "It is always plural"], "Passive se: verb agrees with the noun."),
        M("Which sentence tells us someone dropped something by accident?", "Se me cayó el vaso.", ["Se vendió el vaso.", "Se fabricó el vaso.", "Se explotó el vaso."], "Se me cayó."),
    ],
)

# ---------------------------------------------------------------------------- 418
L418 = lesson(
    "Which se is it? Name its job",
    "Se lo dije. Se cerraron las fronteras. Se me perdió el celular.",
    requires=["decir", "cerrar", "perder", "celular", "frontera", "lavar", "mano", "escribir", "carta", "detener", "ladrón"],
    cards=[
        card("Six jobs of se",
             "To find what a se is doing, ask two questions: Is there another pronoun (me, te, le, nos, les) next to it? What does the verb agree with?",
             tables=[table(["Tipo", "Pista", "Ejemplo"],
                           [["reflexivo", "the action returns to the subject", "Se lavó las manos."],
                            ["recíproco", "plural subject; “each other”", "Los dos se escribieron cartas."],
                            ["se = le/les", "another pronoun follows", "Se lo dije ayer."],
                            ["impersonal", "no noun to agree with, or a person with the personal a", "Se detuvo a los ladrones."],
                            ["pasivo", "verb agrees with the noun", "Se cerraron las fronteras."],
                            ["accidental", "indirect pronoun after se", "Se me perdió el celular."]],
                           say=[2])]),
    ],
    exercises=[
        M("What kind of se is in “Se lavó las manos”?", "Reflexive", ["Reciprocal", "Passive", "Accidental"], "The action returns to the subject."),
        M("What kind of se is in “Los dos se escribieron cartas”?", "Reciprocal", ["Reflexive", "Impersonal", "Accidental"], "Each wrote to the other."),
        M("What is se in “Se lo dije ayer”?", "A replacement for le", ["A reflexive pronoun", "A passive marker", "An impersonal marker"], "Le + lo → se lo."),
        M("What kind of se is in “Se vive bien en esta ciudad”?", "Impersonal", ["Reflexive", "Accidental", "Reciprocal"], "No noun, third-person singular verb."),
        M("What kind of se is in “Se cerraron las fronteras”?", "Passive", ["Reflexive", "Accidental", "Reciprocal"], "Verb agrees with fronteras."),
        M("What kind of se is in “Se me perdió el celular”?", "Accidental", ["Passive", "Reciprocal", "Impersonal"], "Se + me + verb."),
        M("What kind of se is in “Se detuvo a los ladrones”?", "Impersonal", ["Reflexive", "Reciprocal", "Accidental"], "Personal a, singular verb."),
        M("What kind of se is in “Los niños se levantaron temprano”?", "Reflexive", ["Passive", "Impersonal", "Accidental"], "They got themselves up."),
        M("What kind of se is in “Los amigos se abrazaron al verse”?", "Reciprocal", ["Reflexive", "Passive", "Impersonal"], "They hugged each other."),
    ],
)

# ---------------------------------------------------------------------------- 419
L419 = lesson(
    "Defending the land: key words",
    "Los defensores del medio ambiente protegen el territorio de sus comunidades.",
    requires=["defender", "defensor", "amenaza", "amenazar", "derecho", "comunidad", "indígena", "territorio", "presa", "empresa", "proyecto", "denunciar", "líder", "premio", "asesinar"],
    cards=[
        card("Words for people who protect nature",
             "Many people in Latin America defend rivers, forests and land, often at great personal risk. These are the words you will meet in stories about them.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el defensor, la defensora", "defender", "Berta Cáceres fue una defensora de los ríos."],
                            ["la comunidad", "community", "La comunidad vive junto al río."],
                            ["el pueblo indígena", "indigenous people", "Los lencas son un pueblo indígena."],
                            ["el territorio", "territory, land", "El territorio de la comunidad es sagrado para ella."],
                            ["la presa", "dam", "Querían construir una presa en el río."],
                            ["la empresa", "company", "La empresa quería explotar el oro."],
                            ["denunciar", "to report, to speak out against", "La líder denunció los daños al río."],
                            ["amenazar", "to threaten", "Las amenazas no la detuvieron."],
                            ["el premio", "prize, award", "Recibió un premio ambiental."]],
                           say=[2])]),
    ],
    exercises=[
        F("Una ___ es una persona que protege algo, como un río o un bosque.", "defensora", ["empresa", "presa", "comunidad"], "Defender.", tr="A defender is a person who protects something, like a river or a forest."),
        F("Una ___ se construye en un río para guardar el agua.", "presa", ["empresa", "comunidad", "líder"], "Dam.", tr="A dam is built on a river to hold water."),
        F("Los lencas son un pueblo ___ de Honduras.", "indígena", ["deportivo", "comercial", "extranjero"], "Indigenous.", tr="The Lenca are an indigenous people of Honduras."),
        F("La ___ quería explotar el oro del río.", "empresa", ["comunidad", "presa", "líder"], "A company.", tr="The company wanted to mine the gold of the river."),
        F("Ayer la líder ___ los daños al río ante la prensa.", "denunció", ["denunciaron", "denunciar", "denuncia"], "Finished event with one subject.", tr="The leader reported the damage to the river to the press.", lemma="denunciar:ella:pret"),
        F("Algunas personas ___ a los defensores para que callen.", "amenazan", ["amenaza", "amenazar", "amenazo"], "Personas is plural.", tr="Some people threaten the defenders to make them be quiet.", lemma="amenazar:ellos"),
        M("Which word means “award”?", "el premio", ["la presa", "la empresa", "la amenaza"], "Premio."),
        M("What does “el territorio” mean here?", "the land of a community", ["a kind of dam", "a company", "a prize"], "Territorio."),
        M("What does a defensor del medio ambiente do?", "Protects nature", ["Builds dams", "Cuts down trees", "Sells gold"], "Defender = protect."),
    ],
    verify=(vpp("denunciar", "denuncié", "denunciaste", "denunció", "denunciamos", "denunciasteis", "denunciaron")
            + vp("amenazar", "amenazo", "amenazas", "amenaza", "amenazamos", "amenazáis", "amenazan")),
)

# ---------------------------------------------------------------------------- 420
L420 = lesson(
    "Reading: Berta Cáceres and the Lenca people",
    "Berta Cáceres defendió el río Gualcarque y ganó un premio internacional.",
    requires=["pueblo", "fundar", "derecho", "presa", "río", "premio", "recibir", "muerte", "asesinar", "justicia", "condenar", "símbolo", "tierra"],
    cards=[
        card("A leader who defended a river",
             "This text is a factual summary. Read it, then answer the questions.",
             examples=[
                 ex("Berta Cáceres nació en Honduras y pertenecía al pueblo lenca.", "Berta Cáceres was born in Honduras and belonged to the Lenca people.", "pertenecía"),
                 ex("Los lencas son un pueblo indígena que vive en Honduras y El Salvador desde hace siglos.", "The Lenca are an indigenous people who have lived in Honduras and El Salvador for centuries.", "vive"),
                 ex("En mil novecientos noventa y tres, Berta ayudó a fundar una organización para defender los derechos de su pueblo.", "In 1993, Berta helped found an organization to defend her people’s rights.", "fundar"),
                 ex("Después lideró la oposición a una presa en el río Gualcarque, que los lencas consideran sagrado.", "Later she led the opposition to a dam on the Gualcarque River, which the Lenca consider sacred.", "lideró"),
                 ex("En dos mil quince recibió el Premio Goldman, uno de los premios ambientales más importantes del mundo.", "In 2015 she received the Goldman Prize, one of the most important environmental prizes in the world.", "recibió"),
                 ex("Fue asesinada en su casa el dos de marzo de dos mil dieciséis.", "She was murdered in her home on March 2, 2016.", "Fue asesinada"),
                 ex("Su muerte causó protestas en muchos países, y años después la justicia condenó a varias personas por el crimen.", "Her death caused protests in many countries, and years later the court convicted several people for the crime.", "condenó"),
                 ex("Para muchos, Berta es un símbolo de la defensa de la tierra.", "For many, Berta is a symbol of the defense of the land.", "símbolo"),
             ]),
    ],
    exercises=[
        F("Desde niña, Berta Cáceres ___ al pueblo lenca.", "pertenecía", ["pertenecen", "pertenecer", "perteneció"], "Description of who she was: imperfect.", tr="From childhood, Berta Cáceres belonged to the Lenca people.", lemma="pertenecer:ella:impf"),
        F("En mil novecientos noventa y tres, ella ayudó a ___ una organización.", "fundar", ["fundó", "funda", "fundaron"], "After a: infinitive.", tr="In 1993, she helped found an organization."),
        F("Años después, ella ___ la oposición a una presa en el río Gualcarque.", "lideró", ["lideraron", "liderar", "lidera"], "Finished event, one subject.", tr="She led the opposition to a dam on the Gualcarque River.", lemma="liderar:ella:pret"),
        F("En dos mil quince ___ el Premio Goldman.", "recibió", ["recibieron", "recibir", "recibe"], "Finished event with a date.", tr="In 2015 she received the Goldman Prize.", lemma="recibir:ella:pret"),
        F("Su muerte ___ protestas en muchos países.", "causó", ["causaron", "causar", "causa"], "Muerte is singular.", tr="Her death caused protests in many countries.", lemma="causar:ella:pret"),
        M("Which people did Berta Cáceres belong to?", "The Lenca", ["The Maya", "The Aztecs", "The Taíno"], "El pueblo lenca."),
        M("What did she oppose?", "A dam on the Gualcarque River", ["A highway in Honduras", "A school", "A mine in Chile"], "Una presa."),
        M("What prize did she receive in 2015?", "The Goldman Prize", ["The Nobel Prize", "The Pulitzer Prize", "The Oscar"], "Premio Goldman."),
        M("What happened years after her death?", "The court convicted several people", ["The dam was finished at once", "She received a second prize", "Honduras closed its borders"], "La justicia condenó."),
    ],
    verify=(vpp("liderar", "lideré", "lideraste", "lideró", "lideramos", "liderasteis", "lideraron")
            + vpp("recibir", "recibí", "recibiste", "recibió", "recibimos", "recibisteis", "recibieron")
            + vpi("pertenecer", "pertenecía", "pertenecías", "pertenecía", "pertenecíamos", "pertenecíais", "pertenecían")),
)

# ---------------------------------------------------------------------------- 421
L421 = lesson(
    "Reading: Francia Márquez and the river",
    "Francia Márquez organizó a su comunidad para defender un río.",
    requires=["mujer", "comunidad", "río", "oro", "empresa", "caminar", "capital", "premio", "recibir", "elegir", "ayudar"],
    cards=[
        card("A river, a march and a prize",
             "A second story of environmental defense. Notice the preterite for events and the imperfect for background.",
             examples=[
                 ex("Francia Márquez nació en el departamento del Cauca, en Colombia.", "Francia Márquez was born in the department of Cauca, in Colombia.", "nació"),
                 ex("Su comunidad afrocolombiana vivía junto al río, y el río les daba comida y agua.", "Her Afro-Colombian community lived next to the river, and the river gave them food and water.", "vivía"),
                 ex("Cuando la minería ilegal contaminó el río, ella organizó a la comunidad.", "When illegal mining polluted the river, she organized the community.", "organizó"),
                 ex("En dos mil catorce, ella y otras mujeres caminaron más de trescientos kilómetros hasta Bogotá para pedir ayuda.", "In 2014, she and other women walked more than three hundred kilometers to Bogotá to ask for help.", "caminaron"),
                 ex("En dos mil dieciocho recibió el Premio Goldman.", "In 2018 she received the Goldman Prize.", "recibió"),
                 ex("En dos mil veintidós fue elegida vicepresidenta de Colombia.", "In 2022 she was elected vice president of Colombia.", "fue elegida"),
             ]),
    ],
    exercises=[
        F("Antes de la minería, su comunidad ___ junto al río.", "vivía", ["vivió", "vive", "vivir"], "Background in the past → imperfect.", tr="Before mining, her community lived next to the river.", lemma="vivir:ella:impf"),
        F("Cuando la minería ilegal contaminó el río, ella ___ a la comunidad.", "organizó", ["organizaba", "organizar", "organiza"], "A reaction to an event → preterite.", tr="When illegal mining polluted the river, she organized the community.", lemma="organizar:ella:pret"),
        F("En dos mil catorce, Francia y otras mujeres ___ hasta Bogotá.", "caminaron", ["caminó", "caminar", "camina"], "Ellas: plural.", tr="In 2014, Francia and other women walked all the way to Bogotá.", lemma="caminar:ellos:pret"),
        F("En dos mil dieciocho ella ___ el Premio Goldman.", "recibió", ["recibían", "recibir", "recibe"], "Finished event with a date.", tr="In 2018 she received the Goldman Prize.", lemma="recibir:ella:pret"),
        F("En dos mil veintidós fue ___ vicepresidenta de Colombia.", "elegida", ["elegido", "elegidas", "elegir"], "Agrees with ella (feminine singular).", tr="In 2022 she was elected vice president of Colombia."),
        M("What had polluted the river?", "Illegal mining", ["A dam", "A volcano", "A flood"], "La minería ilegal."),
        M("Where did the women walk to?", "Bogotá", ["Lima", "Quito", "Panama City"], "Hasta Bogotá."),
        M("Which prize did she receive in 2018?", "The Goldman Prize", ["The Nobel Prize", "The Cervantes Prize", "The Pulitzer Prize"], "Premio Goldman."),
        M("What office did she win in 2022?", "Vice president of Colombia", ["Mayor of Bogotá", "President of Ecuador", "Minister of mining"], "Vicepresidenta."),
    ],
    verify=(vpp("organizar", "organicé", "organizaste", "organizó", "organizamos", "organizasteis", "organizaron")
            + vpp("caminar", "caminé", "caminaste", "caminó", "caminamos", "caminasteis", "caminaron")),
)

# ---------------------------------------------------------------------------- 422
L422 = lesson(
    "Review: the past perfect and the future",
    "Ya habían explorado la selva. Mañana viajaremos al desierto.",
    requires=["haber", "explorar", "selva", "viajar", "desierto", "ver", "llegar", "estar", "tener", "ya", "nunca"],
    cards=[
        card("Two tools, side by side",
             "The past perfect steps back from a moment in the past (había + participle). The future looks ahead (-é, -ás, -á, -emos, -án), and the same forms can express a guess about the present.",
             tables=[table(["Para…", "Usa…", "Ejemplo"],
                           [["an earlier past event", "había + participio", "Ya habían explorado la selva."],
                            ["a plan or promise", "futuro simple", "Mañana viajaremos al desierto."],
                            ["a near plan", "ir a + infinitivo", "Voy a visitar el volcán."],
                            ["a guess about now", "futuro de probabilidad", "¿Dónde estará Héctor?"]],
                           say=[2])]),
    ],
    exercises=[
        F("Cuando llegamos, los guardias ya ___ cerrado el parque.", "habían", ["habíamos", "había", "han"], "Guardias is plural; earlier event.", tr="When we arrived, the guards had already closed the park.", lemma="haber:ellos:impf"),
        F("Yo nunca ___ visto una selva tan grande antes de este viaje.", "había", ["habías", "habían", "hay"], "Yo → había.", tr="I had never seen such a big jungle before this trip.", lemma="haber:yo:impf"),
        F("El año próximo nosotros ___ al desierto de Atacama.", "viajaremos", ["viajábamos", "viajaron", "viajar"], "A plan → future.", tr="Next year we will travel to the Atacama Desert.", lemma="viajar:nosotros:fut"),
        F("Mis primos ___ a Chile el año próximo; ya compraron los boletos.", "viajarán", ["viajaban", "viajaron", "viajar"], "A plan → future.", tr="My cousins will travel to Chile next year; they already bought the tickets.", lemma="viajar:ellos:fut"),
        F("Son las seis y mi hermano no ha llegado; ___ en el tráfico.", "estará", ["estaba", "estuvo", "estar"], "A guess about now.", tr="It is six and my brother has not arrived; he is probably stuck in traffic.", lemma="estar:él:fut"),
        F("La selva: ya ___ habían explorado antes del viaje.", "la", ["lo", "los", "las"], "Selva is feminine singular.", tr="The jungle: they had already explored it before the trip."),
        F("¿Qué hora ___? Creo que son las ocho.", "será", ["era", "fue", "ser"], "Wondering → future.", tr="What time can it be? I think it is eight.", lemma="ser:ella:fut"),
        M("Which sentence puts the earlier event in the past perfect?", "Cuando llegué, ya habían salido.", ["Cuando llegué, ya salen.", "Cuando llegué, ya saldrán.", "Cuando llegué, ya salir."], "Habían salido."),
        M("What does “Será la una” express?", "A guess: it is probably one o’clock", ["A promise", "A command", "A past event"], "Future of probability."),
        M("Where does “nunca” go in the past perfect?", "Before haber: Nunca había estado", ["After the participle only: Había estado nunca", "Between haber and the participle", "At the start of the participle"], "Nunca había estado."),
    ],
)

# ---------------------------------------------------------------------------- 423
L423 = lesson(
    "Review: the conditional and se",
    "Según los expertos, se perderían muchas especies.",
    requires=["perder", "especie", "poder", "haber", "decir", "ir", "médico", "olvidar", "romper", "cerrar"],
    cards=[
        card("The conditional and se together",
             "Environmental reports mix the conditional (what would happen) with passive se (who does it is not named): Se perderían muchas especies; se cerrarían playas. Remember the stems: dir-, har-, podr-, habr-.",
             tables=[table(["Frase", "English"],
                           [["Se perderían muchas especies.", "Many species would be lost."],
                            ["Se cerrarían las playas.", "The beaches would be closed."],
                            ["Habría más incendios.", "There would be more fires."],
                            ["Yo que tú, iría al médico.", "If I were you, I would go to the doctor."],
                            ["Se me olvidó la receta.", "I forgot the prescription."]],
                           say=[0])]),
    ],
    exercises=[
        F("Según los expertos, en el peor escenario se ___ muchas especies.", "perderían", ["perdieron", "perdiendo", "perder"], "Passive se in the conditional; plural.", tr="According to experts, many species would be lost.", lemma="perder:ellos:cond"),
        F("En ese escenario, se ___ las playas más pequeñas.", "cerrarían", ["cerraron", "cerrando", "cerrar"], "Passive se in the conditional; plural.", tr="In that scenario, the smallest beaches would be closed.", lemma="cerrar:ellos:cond"),
        F("En un mundo más caliente, ___ más incendios y más sequías.", "habría", ["habrían", "hubo", "haber"], "Impersonal haber.", tr="There would be more fires and more droughts.", lemma="haber:él:cond"),
        F("Yo que tú, ___ al médico.", "iría", ["voy", "fui", "ir"], "Advice → conditional.", tr="If I were you, I would go to the doctor.", lemma="ir:yo:cond"),
        F("¿Me ___ ayudar, por favor?", "podría", ["puedo", "pude", "poder"], "Polite request → conditional.", tr="Could you help me, please?", lemma="poder:él:cond"),
        F("A mi hermana se le ___ la receta en casa.", "olvidó", ["olvidaron", "olvidar", "olvido"], "Receta is singular.", tr="My sister forgot the prescription at home.", lemma="olvidar:él:pret"),
        F("A nosotros se nos ___ los vasos.", "rompieron", ["rompió", "romper", "rompemos"], "Vasos is plural.", tr="The glasses broke on us (we broke them by accident).", lemma="romper:ellos:pret"),
        M("Which sentence is a polite request using the conditional?", "¿Podría ayudarme?", ["¿Me ayudas ya?", "¡Ayúdeme!", "Me ayuda."], "Conditional = polite."),
        M("What stem does decir use in the conditional?", "dir-", ["dec-", "dic-", "deci-"], "Diría."),
        M("Why is the verb plural in “Se perderían muchas especies”?", "It agrees with muchas especies", ["It agrees with se", "Because it is a command", "Because it is the future"], "Passive se agrees with the noun."),
    ],
)

# ---------------------------------------------------------------------------- 424
L424 = lesson(
    "Unit review: geography and the environment",
    "Todo junto: paisajes, el pluscuamperfecto, el futuro, el condicional y se.",
    requires=["río", "montaña", "isla", "haber", "mar", "proteger", "especie", "peligro", "ir", "nivel", "subir", "presa"],
    cards=[
        card("Your toolbox from Chapter 22",
             "One table that connects what you learned in this unit. Pick the tool that fits the job.",
             tables=[table(["Job", "Tool", "Example"],
                           [["describe the land", "ser/estar + adjectives", "El Amazonas es un río ancho y caudaloso."],
                            ["say where it is", "estar situado, limitar con", "Chile está situado entre los Andes y el Pacífico."],
                            ["earlier past event", "había + participio", "Los franceses ya habían intentado construir el canal."],
                            ["a plan or promise", "futuro simple", "Compraré una casa en cuatro años."],
                            ["a guess about now", "futuro de probabilidad", "¿Quién será esa mujer?"],
                            ["what would happen", "condicional", "El nivel del mar subiría."],
                            ["unnamed doer", "se pasivo", "Se desviaron varios ríos."]],
                           say=[2])]),
    ],
    exercises=[
        F("El Amazonas es un río muy ___.", "ancho", ["ancha", "anchos", "anchas"], "Río is masculine singular.", tr="The Amazon is a very wide river."),
        F("Chile está ___ entre los Andes y el océano Pacífico.", "situado", ["situada", "situados", "situar"], "Chile: masculine singular.", tr="Chile is located between the Andes and the Pacific Ocean."),
        F("Cuando llegué al parque, los turistas ya ___ salido.", "habían", ["habíamos", "había", "han"], "Turistas is plural; earlier event.", tr="When I arrived at the park, the tourists had already left.", lemma="haber:ellos:impf"),
        F("En mil novecientos cuatro el gobierno de Estados Unidos ___ la obra del canal.", "continuó", ["continuaba", "continuará", "continuar"], "Finished event with a date.", tr="In 1904 the United States continued the work on the canal.", lemma="continuar:él:pret"),
        F("Son las diez y Carlos no contesta; ___ durmiendo.", "estará", ["estaba", "estuvo", "estar"], "A guess about now.", tr="It is ten and Carlos does not answer; he is probably sleeping.", lemma="estar:él:fut"),
        F("En un mundo sin glaciares, el nivel del mar ___ mucho.", "subiría", ["subió", "subiendo", "subir"], "A scenario → conditional.", tr="In a world without glaciers, the sea level would rise a great deal.", lemma="subir:él:cond"),
        F("Se ___ varios ríos para construir la presa.", "desviaron", ["desvió", "desviar", "desviamos"], "Passive se; plural.", tr="Several rivers were diverted to build the dam.", lemma="desviar:ellos:pret"),
        F("Hasta ahora, muchos países ___ parques para proteger las especies en peligro.", "han creado", ["habían creado", "habrán creado", "hemos creado"], "Present perfect: they have created parks.", tr="Many countries have created parks to protect endangered species."),
        M("Which sentence puts the pronoun correctly?", "Ya la habían explorado.", ["Ya habían la explorado.", "Habían explorado la ya.", "Ya habían explorado la."], "Pronoun before haber."),
        M("What does “Habría más incendios” express?", "There would be more fires", ["There were more fires", "There are more fires", "There will be more fires"], "Conditional."),
        M("Which sentence includes the impersonal se?", "En esta región se vive tranquilo.", ["Se me cayó el vaso.", "Se desviaron los ríos.", "Se lo dije ayer."], "Se vive: no noun, singular verb."),
    ],
)

UNIT = unit("Geografía y medio ambiente", [
    L391, L392, L393, L394, L395, L396, L397, L398, L399, L400, L401, L402, L403, L404, L405, L406,
    L407, L408, L409, L410, L411, L412, L413, L414, L415, L416, L417, L418, L419, L420, L421, L422,
    L423, L424,
])

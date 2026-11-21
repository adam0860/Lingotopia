"""Unit 6: review and practice (textbook Chapter 5)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 75
L75 = lesson(
    "Introducing yourself",
    "Me llamo Ana. Soy de Chile. Tengo veinte años.",
    requires=["llamar", "ser", "tener", "vivir", "trabajar"],
    cards=[
        card("A short conversation",
             "Here is a model conversation that uses what you learned in Unit 1. Tap each line to hear it. "
             "Notice which verb each answer uses: llamarse for your name, ser for origin and job, tener for "
             "age and vivir for where you live.",
             examples=[
                 ex("Hola, buenos días. ¿Cómo te llamas?", "Hello, good morning. What is your name?"),
                 ex("Me llamo Ana. Mucho gusto.", "My name is Ana. Nice to meet you."),
                 ex("Igualmente. ¿De dónde eres?", "Likewise. Where are you from?"),
                 ex("Soy de Chile. ¿Y tú?", "I am from Chile. And you?"),
                 ex("Soy de Colombia. ¿Cuántos años tienes?", "I am from Colombia. How old are you?"),
                 ex("Tengo veinte años. ¿Dónde vives?", "I am twenty. Where do you live?"),
                 ex("Vivo en un apartamento cerca del centro. ¿A qué te dedicas?", "I live in an apartment near downtown. What do you do?"),
                 ex("Soy ingeniera. ¡Hasta luego!", "I am an engineer. See you later!"),
             ]),
        card("Formal or informal?",
             "With friends and classmates, use tú: ¿Cómo te llamas? With older people or in a business setting, "
             "use usted: ¿Cómo se llama usted?",
             tables=[table(["Informal (tú)", "Formal (usted)"],
                           [["¿Cómo te llamas?", "¿Cómo se llama usted?"],
                            ["¿De dónde eres?", "¿De dónde es usted?"],
                            ["¿Cuántos años tienes?", "¿Cuántos años tiene usted?"],
                            ["¿Dónde vives?", "¿Dónde vive usted?"],
                            ["¿A qué te dedicas?", "¿A qué se dedica usted?"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("¿Cómo te llamas? — ___ llamo Ana.", "Me", ["Te", "Se", "Mi"], "Me llamo = my name is.", tr="What is your name? — My name is Ana."),
        F("¿De dónde eres? — ___ de Chile.", "Soy", ["Estoy", "Tengo", "Eres"], "Origin uses ser.", tr="Where are you from? — I am from Chile.", lemma="ser:yo"),
        F("¿Cuántos años tienes? — ___ veinte años.", "Tengo", ["Soy", "Estoy", "Tiene"], "Age uses tener.", tr="How old are you? — I am twenty.", lemma="tener:yo"),
        F("¿Dónde vives? — ___ en un apartamento.", "Vivo", ["Vives", "Vive", "Viven"], "Yo vivo.", tr="Where do you live? — I live in an apartment.", lemma="vivir:yo"),
        F("¿A qué te dedicas? — ___ ingeniera.", "Soy", ["Estoy", "Tengo", "Hago"], "A job uses ser.", tr="What do you do? — I am an engineer.", lemma="ser:yo"),
        F("¿Cómo se llama ___? (formal “you”)", "usted", ["tú", "yo", "te"], "Formal speech uses usted.", tr="What is your name? (formal)"),
        M("You meet your professor. What do you say?", "Buenos días, profesor. ¿Cómo está usted?", ["Hola, profe. ¿Cómo estás tú?", "¡Chao! ¿Qué tal?", "Buenas noches, amigo."], "Formal: buenos días and usted."),
        M("You meet a new classmate. What is the natural greeting?", "Hola. ¿Cómo te llamas?", ["¿Cómo se llama usted?", "¿A qué se dedica usted?", "Buenos días, señor."], "Informal with a peer."),
        M("Which answer to “Mucho gusto” is correct?", "Igualmente.", ["Hasta luego.", "Por favor.", "De nada."], "Igualmente = likewise."),
        M("Which verb gives your age?", "tener", ["ser", "estar", "llamar"], "Tengo veinte años."),
    ],
)

# ---------------------------------------------------------------------------- 76
L76 = lesson(
    "Ser or estar? Practice",
    "Marta es alta. Marta está en casa.",
    requires=["ser", "estar", "casa", "oficina", "cansado"],
    cards=[
        card("A one-page guide",
             "Both verbs mean “to be”, but each has its own jobs. Think of ser as ‘what something is’ and "
             "estar as ‘where or how it is right now’.",
             tables=[table(["Verb", "Use", "Example"],
                           [["ser", "identity", "Ana es mi hermana."],
                            ["ser", "description", "La casa es grande."],
                            ["ser", "origin", "Somos de México."],
                            ["ser", "job", "Mi padre es mecánico."],
                            ["ser", "day, date, time", "Hoy es lunes. Son las tres."],
                            ["ser", "possession, material", "La mesa es de madera."],
                            ["estar", "location", "La lámpara está en la sala."],
                            ["estar", "condition", "Las ventanas están rotas."],
                            ["estar", "feelings, health", "Mi madre está cansada."]],
                           say=[2])]),
        card("The same adjective, two meanings",
             "Some adjectives change meaning. With ser they describe a lasting quality; with estar they describe how "
             "something is now.",
             examples=[
                 ex("Mi hermano es simpático.", "My brother is nice (he is a nice person).", "es simpático"),
                 ex("Hoy mi hermano está simpático.", "Today my brother is being nice.", "está simpático"),
                 ex("Mi hermano es aburrido.", "My brother is boring.", "es aburrido"),
                 ex("Mi hermano está aburrido.", "My brother is bored.", "está aburrido"),
             ]),
    ],
    exercises=[
        F("Mi madre ___ ingeniera.", "es", ["está", "tiene", "hace"], "A job: ser.", tr="My mother is an engineer.", lemma="ser:ella"),
        F("Mi madre ___ en la oficina.", "está", ["es", "tiene", "hace"], "Location: estar.", tr="My mother is at the office.", lemma="estar:ella"),
        F("Hoy ___ miércoles.", "es", ["está", "son", "hay"], "A day: ser.", tr="Today is Wednesday.", lemma="ser:él"),
        F("Las ventanas ___ rotas.", "están", ["son", "tienen", "hacen"], "A condition: estar.", tr="The windows are broken.", lemma="estar:ellos"),
        F("Nosotros ___ de México.", "somos", ["estamos", "tenemos", "vamos"], "Origin: ser.", tr="We are from Mexico.", lemma="ser:nosotros"),
        F("La mesa ___ de madera.", "es", ["está", "tiene", "hace"], "Material: ser.", tr="The table is made of wood.", lemma="ser:él"),
        F("Yo ___ cansado hoy.", "estoy", ["soy", "tengo", "voy"], "A feeling: estar.", tr="I am tired today.", lemma="estar:yo"),
        F("¿Dónde ___ el banco?", "está", ["es", "son", "hay"], "Location: estar.", tr="Where is the bank?", lemma="estar:él"),
        F("Mis tíos ___ muy simpáticos.", "son", ["hacen", "tienen", "van"], "A lasting quality: ser.", tr="My aunt and uncle are very nice.", lemma="ser:ellos"),
        M("Which sentence tells where something is?", "El libro está encima de la mesa.", ["El libro es encima de la mesa.", "El libro tiene encima de la mesa.", "El libro va encima de la mesa."], "Location: estar."),
        M("Which sentence tells what someone does?", "Mi tío es cocinero.", ["Mi tío está cocinero.", "Mi tío tiene cocinero.", "Mi tío hace cocinero."], "A job: ser."),
        M("“La sala está limpia” means…", "the living room is clean right now", ["the living room is a clean one by nature", "the living room is large", "the living room is near"], "Estar describes the present condition."),
    ],
)

# ---------------------------------------------------------------------------- 77
L77 = lesson(
    "Agreement review",
    "mi hermana alta, nuestros libros nuevos",
    requires=["hermano", "alto", "pequeño", "nuevo", "familia", "casa"],
    cards=[
        card("Everything must match",
             "In Spanish an article, a noun and its adjective share gender and number. Possessives (mi, tu, su, "
             "nuestro) agree with the noun they describe, not with the owner. Mi and tu and su only change for "
             "number; nuestro changes for gender too.",
             tables=[table(["", "Singular", "Plural"],
                           [["masc.", "el hermano alto", "los hermanos altos"],
                            ["fem.", "la hermana alta", "las hermanas altas"],
                            ["mi, tu, su", "mi casa · mi libro", "mis casas · mis libros"],
                            ["nuestro", "nuestra casa · nuestro libro", "nuestras casas · nuestros libros"]],
                           say=[1, 2])]),
        card("Small things to remember",
             "Adjectives ending in -e or a consonant (grande, azul) keep the same form for masculine and feminine "
             "and only add -s or -es in the plural. Before a word starting with the sound i, y becomes e: "
             "padres e hijos.",
             examples=[
                 ex("Mi hermana es alta y mis hermanos son bajos.", "My sister is tall and my brothers are short.", "Mi hermana es alta"),
                 ex("Nuestra casa es grande y nuestros dormitorios son azules.", "Our house is big and our bedrooms are blue.", "Nuestra casa"),
                 ex("Son padres e hijos.", "They are parents and children.", "padres e hijos"),
             ]),
    ],
    exercises=[
        F("Mi hermana es ___.", "alta", ["alto", "altas", "altos"], "Hermana is feminine singular.", tr="My sister is tall."),
        F("Mis hermanos son ___.", "altos", ["alto", "alta", "altas"], "Hermanos is masculine plural.", tr="My brothers are tall."),
        F("Nuestra casa es ___.", "grande", ["grando", "grandas", "grandos"], "Grande does not change for gender.", tr="Our house is big."),
        F("___ libros son nuevos. (our)", "Nuestros", ["Nuestro", "Nuestra", "Nuestras"], "Libros is masculine plural.", tr="Our books are new."),
        F("___ dormitorio es pequeño. (my)", "Mi", ["Mis", "Mía", "Nuestro"], "Dormitorio is singular.", tr="My bedroom is small."),
        F("Las sillas son ___.", "azules", ["azul", "azules sillas", "azula"], "Azul adds -es in the plural.", tr="The chairs are blue."),
        F("Padres ___ hijos viven en esta casa.", "e", ["y", "o", "u"], "Hijos begins with the sound i.", tr="Parents and children live in this house."),
        F("Hay siete ___ ocho personas en la sala.", "u", ["o", "e", "y"], "Ocho begins with the sound o.", tr="There are seven or eight people in the living room."),
        M("Which is correct?", "las mesas pequeñas", ["las mesas pequeños", "los mesas pequeñas", "las mesa pequeñas"], "All three words are feminine plural."),
        M("Which is correct?", "mi tío y mis primos", ["mis tío y mi primos", "mi tíos y mis primo", "mi tío y mi primos"], "Mi + singular, mis + plural."),
    ],
)

# ---------------------------------------------------------------------------- 78
L78 = lesson(
    "Which verb form?",
    "regular and irregular, all together",
    requires=["hablar", "comer", "vivir", "ser", "estar", "tener", "ir", "hacer"],
    cards=[
        card("Three steps to the right form",
             "1. Find the subject (who is doing it?). 2. Look at the infinitive ending (-ar, -er or -ir). "
             "3. Use the matching ending, unless the verb is one of the irregular ones you have memorized.",
             tables=[table(["", "-ar", "-er", "-ir"],
                           [["yo", "-o", "-o", "-o"],
                            ["tú", "-as", "-es", "-es"],
                            ["él, ella, usted", "-a", "-e", "-e"],
                            ["nosotros", "-amos", "-emos", "-imos"],
                            ["vosotros", "-áis", "-éis", "-ís"],
                            ["ellos, ellas, ustedes", "-an", "-en", "-en"]],
                           say=[])]),
        card("The irregular ones so far",
             "Ser, estar, tener, hacer and ir are the verbs you cannot guess. Hacer and tener are only odd in "
             "some forms; ser and ir are different in nearly every form, while estar is irregular in the yo form (estoy) and carries a written accent in estás, está and están.",
             tables=[table(["", "ser", "estar", "tener", "hacer", "ir"],
                           [["yo", "soy", "estoy", "tengo", "hago", "voy"],
                            ["tú", "eres", "estás", "tienes", "haces", "vas"],
                            ["él, ella, usted", "es", "está", "tiene", "hace", "va"],
                            ["nosotros", "somos", "estamos", "tenemos", "hacemos", "vamos"],
                            ["vosotros", "sois", "estáis", "tenéis", "hacéis", "vais"],
                            ["ellos, ellas, ustedes", "son", "están", "tienen", "hacen", "van"]],
                           say=[1, 2, 3, 4, 5])]),
    ],
    exercises=[
        F("Mis padres ___ en una casa grande.", "viven", ["vive", "vivo", "vivimos"], "Mis padres is they: viven.", tr="My parents live in a big house.", lemma="vivir:ellos"),
        F("Yo ___ español en la universidad.", "estudio", ["estudias", "estudia", "estudiamos"], "Yo estudio.", tr="I study Spanish at the university.", lemma="estudiar:yo"),
        F("Tú ___ muy bien el español.", "hablas", ["hablo", "habla", "hablan"], "Tú hablas.", tr="You speak Spanish very well.", lemma="hablar:tú"),
        F("Nosotros ___ en la cafetería.", "comemos", ["como", "comen", "come"], "Nosotros comemos.", tr="We eat in the cafeteria.", lemma="comer:nosotros"),
        F("Mi hermana ___ a la escuela.", "va", ["voy", "vas", "van"], "Mi hermana is she: va.", tr="My sister goes to school.", lemma="ir:ella"),
        F("Ustedes ___ la tarea por la noche.", "hacen", ["hace", "hago", "hacemos"], "Ustedes hacen.", tr="You (all) do the homework at night.", lemma="hacer:ustedes"),
        F("Yo ___ dos hermanos.", "tengo", ["tiene", "tienes", "tenemos"], "Yo tengo.", tr="I have two brothers.", lemma="tener:yo"),
        F("Ellos ___ en el aula.", "están", ["es", "estás", "estamos"], "Ellos están.", tr="They are in the classroom.", lemma="estar:ellos"),
        F("Mis tíos ___ de Bolivia.", "son", ["está", "somos", "es"], "Mis tíos are from Bolivia: son.", tr="My aunt and uncle are from Bolivia.", lemma="ser:ellos"),
        F("Vosotros ___ el libro.", "abrís", ["abren", "abrimos", "abres"], "Vosotros abrís.", tr="You (all) open the book.", lemma="abrir:vosotros"),
        M("Which is the correct yo form of “hacer”?", "hago", ["hazo", "hace", "hacemos"], "Hacer is irregular in yo."),
        M("Which ending goes with “tú” for -ar verbs?", "-as", ["-es", "-a", "-an"], "Tú hablas, tú trabajas."),
    ],
)

# ---------------------------------------------------------------------------- 79
L79 = lesson(
    "Time, numbers and dates in practice",
    "las tres y media, el cinco de mayo, doscientos dólares",
    requires=["hora", "mes", "número", "año", "fecha", "semana"],
    cards=[
        card("Putting numbers to work",
             "Time, dates, ages and prices all use numbers, but each has its own pattern.",
             tables=[table(["Qué", "Cómo se dice", "Ejemplo"],
                           [["time", "Son las… / Es la una", "Son las nueve y media."],
                            ["event time", "a las…", "La clase es a las ocho."],
                            ["date", "el + number + de + month", "Es el diez de junio."],
                            ["age", "tener + años", "Mi abuelo tiene setenta años."],
                            ["price", "number + dólares", "Cuesta doscientos dólares."]],
                           say=[2])]),
    ],
    exercises=[
        M("Which sentence tells the time?", "Son las nueve y media.", ["La clase es a las nueve.", "Tengo nueve años.", "Es el nueve de junio."], "Son las… tells what time it is."),
        M("Which sentence gives the date?", "Es el diez de junio.", ["Son las diez.", "Tengo diez años.", "Cuesta diez dólares."], "El + number + de + month."),
        M("Which sentence gives someone’s age?", "Mi abuelo tiene setenta años.", ["Mi abuelo es de setenta.", "Mi abuelo está setenta.", "Mi abuelo hace setenta."], "Tener + años."),
        F("La clase es ___ las ocho.", "a", ["en", "de", "por"], "Event time: a las.", tr="The class is at eight."),
        F("Mi hermano tiene treinta ___.", "años", ["año", "anos", "añas"], "Age: años.", tr="My brother is thirty years old."),
        F("Hoy es el cinco ___ mayo.", "de", ["en", "del", "a"], "Day + de + month.", tr="Today is May fifth."),
        M("Which is 320 in Spanish?", "trescientos veinte", ["tres veinte", "tres cientos veinte", "trescientas veinte"], "Trescientos is one word."),
        M("Which is 4.500?", "cuatro mil quinientos", ["cuatrocientos quinientos", "cuatro cientos mil", "cuarenta y cinco"], "Cuatro mil, then quinientos."),
        M("It is 7:45. What do you say?", "Son las ocho menos cuarto.", ["Son las siete y cuarto.", "Son las siete menos cuarto.", "Es la ocho y cuarto."], "A quarter before eight."),
        M("It is 12:00 at night. What do you say?", "Es medianoche.", ["Es mediodía.", "Son las doce de la mañana.", "Es la una."], "Medianoche = midnight."),
        M("Which month comes after julio?", "agosto", ["junio", "septiembre", "mayo"], "Julio, agosto, septiembre."),
    ],
)

# ---------------------------------------------------------------------------- 80
L80 = lesson(
    "Home and plans",
    "Mañana voy a limpiar. Tengo que lavar los platos.",
    requires=["casa", "ir", "limpiar", "tener", "mesa", "sala"],
    cards=[
        card("Choosing the right structure",
             "At home you often say where things are, what you are going to do, and what you have to do. "
             "Each has its own structure.",
             tables=[table(["To say…", "Use", "Example"],
                           [["where it is", "estar + location word", "La mesa está en la sala."],
                            ["where you go", "ir a + place", "Voy al mercado."],
                            ["a plan", "ir a + infinitive", "Voy a limpiar la casa."],
                            ["a duty", "tener que + infinitive", "Tengo que lavar los platos."],
                            ["a general rule", "hay que + infinitive", "Hay que cerrar la puerta."],
                            ["a comparison", "más… que", "Mi sala es más grande que mi cocina."]],
                           say=[2])]),
    ],
    exercises=[
        F("La mesa ___ en la sala.", "está", ["es", "va", "tiene"], "Location: estar.", tr="The table is in the living room.", lemma="estar:él"),
        F("Mañana ___ a limpiar la casa.", "voy", ["tengo", "estoy", "hago"], "Plan: voy a.", tr="Tomorrow I am going to clean the house.", lemma="ir:yo"),
        F("Mi hermana ___ que lavar los platos.", "tiene", ["va", "está", "hay"], "Duty: tiene que.", tr="My sister has to wash the dishes.", lemma="tener:ella"),
        F("Hay ___ cerrar la puerta.", "que", ["de", "a", "por"], "Hay que + infinitive.", tr="You have to close the door."),
        F("La lámpara está al lado ___ sofá.", "del", ["de el", "al", "a"], "De + el = del.", tr="The lamp is next to the sofa."),
        F("Nosotros vamos ___ mercado.", "al", ["a el", "a la", "del"], "A + el = al.", tr="We go to the market."),
        F("Mi cocina es más pequeña ___ mi sala.", "que", ["de", "como", "a"], "Más… que.", tr="My kitchen is smaller than my living room."),
        M("Which sentence is a plan?", "Voy a pintar las paredes.", ["Pinto las paredes todos los días.", "Las paredes están sucias.", "Hay paredes."], "Ir a + infinitive."),
        M("Which sentence is a duty for one person?", "Tengo que llamar al plomero.", ["Hay que llamar al plomero.", "Voy al plomero.", "El plomero está aquí."], "Tener que is personal."),
        M("The couch is under the window. Which is correct?", "El sofá está debajo de la ventana.", ["El sofá es debajo de la ventana.", "El sofá está encima de la ventana.", "El sofá tiene debajo de la ventana."], "Debajo de = under."),
    ],
)

# ---------------------------------------------------------------------------- 81
L81 = lesson(
    "Reading: Elena’s family",
    "three short texts, then questions",
    requires=["familia", "trabajar", "casa", "hijo", "esposo"],
    cards=[
        card("Text 1: Elena",
             "Read each line (tap to hear it), then answer the questions at the end.",
             examples=[
                 ex("Me llamo Elena Vargas. Tengo treinta y dos años y soy de Bogotá.", "My name is Elena Vargas. I am thirty-two and I am from Bogotá."),
                 ex("Soy ingeniera y trabajo en una fábrica cerca del centro.", "I am an engineer and I work in a factory near downtown."),
                 ex("Mi esposo se llama Raúl. Es profesor de español en una escuela.", "My husband’s name is Raúl. He is a Spanish teacher at a school."),
                 ex("Tenemos dos hijos, Pablo y Marta. Pablo tiene seis años y Marta tiene diez.", "We have two children, Pablo and Marta. Pablo is six and Marta is ten."),
             ]),
        card("Text 2: A week",
             "Now Elena talks about her routine.",
             examples=[
                 ex("Los lunes llego a la fábrica a las ocho de la mañana y trabajo hasta las cinco.", "On Mondays I arrive at the factory at eight in the morning and work until five."),
                 ex("Por la tarde voy al gimnasio y después cocino la cena.", "In the afternoon I go to the gym and then I cook dinner."),
                 ex("Los sábados limpiamos la casa. Raúl lava los platos y yo lavo la ropa.", "On Saturdays we clean the house. Raúl washes the dishes and I wash the clothes."),
                 ex("El domingo vamos a visitar a mis padres.", "On Sunday we are going to visit my parents."),
             ]),
        card("Text 3: Their house",
             "Finally, Elena describes the house.",
             examples=[
                 ex("Nuestra casa es pequeña, pero es cómoda.", "Our house is small, but it is comfortable."),
                 ex("Tiene tres dormitorios, dos baños, una sala y una cocina.", "It has three bedrooms, two bathrooms, a living room and a kitchen."),
                 ex("La cocina es más grande que la sala. Hay un jardín detrás de la casa.", "The kitchen is bigger than the living room. There is a garden behind the house."),
                 ex("La alfombra de la sala está sucia. Mañana voy a limpiar la alfombra.", "The living room rug is dirty. Tomorrow I am going to clean the rug."),
             ]),
    ],
    exercises=[
        M("Where is Elena from?", "Bogotá", ["Madrid", "México", "Chile"], "Soy de Bogotá."),
        M("What does Elena do for a living?", "She is an engineer.", ["She is a teacher.", "She is a cook.", "She is a nurse."], "Soy ingeniera."),
        M("How old is Marta?", "ten", ["six", "thirty-two", "twelve"], "Marta tiene diez años."),
        M("What does Raúl do?", "He teaches Spanish.", ["He is an engineer.", "He is a cook.", "He is a mechanic."], "Es profesor de español."),
        M("At what time does Elena arrive at the factory on Mondays?", "eight in the morning", ["five in the afternoon", "nine at night", "noon"], "A las ocho de la mañana."),
        M("What does Elena do after the gym?", "She cooks dinner.", ["She cleans the house.", "She studies.", "She goes to the bank."], "Después cocino la cena."),
        M("Who washes the dishes on Saturdays?", "Raúl", ["Elena", "Marta", "Pablo"], "Raúl lava los platos."),
        M("What are they going to do on Sunday?", "visit Elena’s parents", ["clean the house", "go to the gym", "work"], "Vamos a visitar a mis padres."),
        M("How many bedrooms does the house have?", "three", ["two", "four", "one"], "Tiene tres dormitorios."),
        M("Which room is bigger?", "the kitchen", ["the living room", "the bathroom", "the bedroom"], "La cocina es más grande que la sala."),
        M("Where is the garden?", "behind the house", ["in front of the house", "inside the kitchen", "next to the school"], "Detrás de la casa."),
        M("What is dirty?", "the rug", ["the kitchen", "the garden", "the door"], "La alfombra está sucia."),
    ],
)

UNIT = unit("Repaso y práctica", [L75, L76, L77, L78, L79, L80, L81])

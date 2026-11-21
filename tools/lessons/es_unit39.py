"""Unit 39: influential authors (textbook Chapter 39): literary movements, Darío, García Márquez, Mistral, Asturias, Vargas Llosa, Poniatowska, Cortázar, Borges, Allende; vocabulary; como si, ojalá, quisiera; the pluperfect subjunctive."""
from dsl_es import *

# ---------------------------------------------------------------------------- 836
L836 = lesson(
    "Literary movements: from the Siglo de Oro to the boom",
    "El modernismo buscó la belleza. El boom llevó la novela latinoamericana a todo el mundo.",
    requires=["siglo", "movimiento", "escritor", "obra", "novela", "poeta", "revolución", "realidad", "mundo", "época", "surgir", "presentar"],
    cards=[
        card("Seven names to know",
             "A literary movement groups writers who share an era, themes or a style. Critics do not agree on exact dates, so the periods below are approximate. "
             "Many writers do not fit neatly into one movement.",
             tables=[table(["Movimiento", "Época", "Rasgo principal"],
                           [["El Siglo de Oro", "siglos dieciséis y diecisiete", "teatro, poesía y novela de gran calidad en España"],
                            ["El romanticismo", "siglo diecinueve", "emociones, naturaleza y libertad"],
                            ["El realismo", "siglo diecinueve", "la vida diaria y la sociedad"],
                            ["El modernismo", "finales del siglo diecinueve y principios del veinte", "belleza, música y un lenguaje nuevo"],
                            ["Las vanguardias", "principios del siglo veinte", "romper con lo tradicional"],
                            ["El boom latinoamericano", "años sesenta y setenta", "novelas innovadoras leídas en muchos países"],
                            ["El realismo mágico", "siglo veinte", "lo extraordinario parece normal"]],
                           say=[0, 2])]),
        card("In a sentence",
             "Notice the verbs. Use the preterite for something that began in a period and the present to describe what a movement does as a style.",
             examples=[
                 ex("El boom surgió en los años sesenta.", "The boom emerged in the nineteen-sixties.", "surgió"),
                 ex("El realismo mágico presenta lo extraordinario como algo normal.", "Magical realism presents the extraordinary as something normal.", "presenta"),
                 ex("Cervantes vivió en el Siglo de Oro.", "Cervantes lived in the Golden Age.", "vivió"),
             ]),
    ],
    exercises=[
        M("Which movement is linked to Rubén Darío?", "El modernismo", ["El romanticismo", "El realismo", "El boom"], "Darío is the best-known modernista."),
        M("In magical realism, the extraordinary is presented as…", "something normal", ["only a dream", "a lie", "a historical error"], "It is accepted naturally."),
        M("Which period is called the boom?", "The nineteen sixties and seventies", ["The sixteenth and seventeenth centuries", "The early eighteen hundreds", "The twenty-first century"], "Años sesenta y setenta."),
        F("El boom ___ en los años sesenta.", "surgió", ["surgieron", "surgí", "surgiste"], "Singular subject, preterite.", tr="The boom emerged in the nineteen-sixties.", lemma="surgir:él:pret"),
        F("Los escritores del boom ___ novelas muy innovadoras.", "escribieron", ["escribió", "escribimos", "escribí"], "Plural subject.", tr="The writers of the boom wrote very innovative novels.", lemma="escribir:ellos:pret"),
        F("Cervantes ___ en el Siglo de Oro.", "vivió", ["vivieron", "viví", "vivimos"], "Singular subject.", tr="Cervantes lived in the Golden Age.", lemma="vivir:él:pret"),
        F("El romanticismo dio mucha importancia a las ___.", "emociones", ["emocionó", "emocionar", "emocionante"], "A noun after “las”.", tr="Romanticism gave great importance to emotions."),
        F("El realismo mágico ___ lo extraordinario como algo normal.", "presenta", ["presentan", "presentamos", "presentas"], "Singular subject.", tr="Magical realism presents the extraordinary as something normal.", lemma="presentar:él"),
        F("Muchos críticos ___ que el boom cambió la literatura.", "dicen", ["dice", "decimos", "dices"], "Plural subject.", tr="Many critics say that the boom changed literature.", lemma="decir:ellos"),
    ],
    verify=vpp("surgir", "surgí", "surgiste", "surgió", "surgimos", "surgisteis", "surgieron") + vp("presentar", "presento", "presentas", "presenta", "presentamos", "presentáis", "presentan"),
)

# ---------------------------------------------------------------------------- 837
L837 = lesson(
    "Rubén Darío and modernismo",
    "Rubén Darío fue poeta, periodista y diplomático. Nació en Nicaragua y murió en León.",
    requires=["poeta", "periodista", "diplomático", "nacer", "morir", "viajar", "publicar", "libro", "belleza", "música", "país", "lenguaje"],
    cards=[
        card("Who was Rubén Darío?",
             "Rubén Darío (1867–1916) is the best-known writer of modernismo. He was born in Nicaragua, worked as a journalist and a diplomat, and traveled through Latin America and Europe. "
             "Modernista poets looked for musical sounds, rare images and new ways of using Spanish. Darío influenced poets on both sides of the Atlantic.",
             tables=[table(["Dato", "Información"],
                           [["País", "Nicaragua"], ["Oficios", "poeta, periodista y diplomático"],
                            ["Movimiento", "el modernismo"],
                            ["Libros", "Azul…, Prosas profanas y Cantos de vida y esperanza"],
                            ["Años", "nació en mil ochocientos sesenta y siete; murió en mil novecientos dieciséis"]],
                           say=[1])]),
        card("A poem about books",
             "Darío wrote poems that praise books and reading. "
             "The idea is that reading widens our view of the world. (We only describe the poem here. You can find the poem in a library or online.)",
             examples=[
                 ex("Darío viajó por América y Europa.", "Darío traveled through the Americas and Europe.", "viajó"),
                 ex("Publicó libros que cambiaron la poesía en español.", "He published books that changed poetry in Spanish.", "Publicó"),
             ]),
    ],
    exercises=[
        M("What jobs did Rubén Darío have?", "Poet, journalist and diplomat", ["Painter and architect", "Doctor and lawyer", "Actor and director"], "Poeta, periodista y diplomático."),
        M("Which movement is Darío best known for?", "Modernismo", ["Realismo mágico", "Romanticismo", "El boom"], "Modernismo."),
        M("According to the lesson, what does the book poem suggest?", "Reading widens our view of the world", ["Books are dangerous", "Poetry should be silent", "Only experts should read"], "Books as instruments of vision."),
        F("Rubén Darío ___ en Nicaragua.", "nació", ["nacieron", "nací", "naciste"], "Singular subject.", tr="Rubén Darío was born in Nicaragua.", lemma="nacer:él:pret"),
        F("Darío ___ en mil novecientos dieciséis.", "murió", ["murieron", "morí", "morimos"], "Singular subject.", tr="Darío died in nineteen sixteen.", lemma="morir:él:pret"),
        F("Él ___ por América y Europa.", "viajó", ["viajaron", "viajé", "viajaste"], "Singular subject.", tr="He traveled through the Americas and Europe.", lemma="viajar:él:pret"),
        F("Darío ___ varios libros de poemas.", "publicó", ["publicaron", "publiqué", "publicamos"], "Singular subject.", tr="Darío published several books of poems.", lemma="publicar:él:pret"),
        F("Los modernistas buscaban la ___ y la música del lenguaje.", "belleza", ["bello", "bellamente", "bellezas"], "A singular noun after “la”.", tr="The modernistas looked for the beauty and music of language."),
        F("Muchos poetas ___ a Darío.", "admiraron", ["admiró", "admiramos", "admiraste"], "Plural subject.", tr="Many poets admired Darío.", lemma="admirar:ellos:pret"),
    ],
    verify=vpp("nacer", "nací", "naciste", "nació", "nacimos", "nacisteis", "nacieron") + vpp("morir", "morí", "moriste", "murió", "morimos", "moristeis", "murieron"),
)

# ---------------------------------------------------------------------------- 838
L838 = lesson(
    "Gabriel García Márquez: a Nobel writer from Colombia",
    "García Márquez nació en Colombia, fue periodista y escribió Cien años de soledad.",
    requires=["escritor", "nacer", "periodista", "premio", "novela", "familia", "pueblo", "generación", "historia", "escribir", "recibir", "ganar"],
    cards=[
        card("Life and work",
             "Gabriel García Márquez (1927–2014) was born in Aracataca, Colombia. He started as a journalist and later became one of the most widely read authors in Spanish. "
             "He received the Nobel Prize in Literature in 1982. He died in Mexico City.",
             tables=[table(["Dato", "Información"],
                           [["Nombre", "Gabriel García Márquez"], ["Nació en", "Aracataca, Colombia"],
                            ["Oficios", "periodista y novelista"],
                            ["Premio Nobel", "mil novecientos ochenta y dos"],
                            ["Obra más famosa", "Cien años de soledad"]],
                           say=[1])]),
        card("About Cien años de soledad",
             "This summary is in our own words. The novel follows the Buendía family through seven generations in an imaginary town called Macondo. "
             "Names repeat from one generation to the next, history and fantasy mix, and many characters feel alone even when they are surrounded by family.",
             examples=[
                 ex("La novela cuenta la historia de la familia Buendía.", "The novel tells the story of the Buendía family.", "cuenta"),
                 ex("Macondo es un pueblo imaginario.", "Macondo is an imaginary town.", "imaginario"),
                 ex("García Márquez recibió el Premio Nobel en mil novecientos ochenta y dos.", "García Márquez received the Nobel Prize in nineteen eighty-two.", "recibió"),
             ]),
    ],
    exercises=[
        M("What was García Márquez's first profession?", "Journalist", ["Doctor", "Judge", "Soldier"], "He began as a journalist."),
        M("What is Macondo?", "An imaginary town in the novel", ["A real city in Mexico", "A university", "A family name"], "Pueblo imaginario."),
        M("How many generations does the novel follow?", "Seven", ["Two", "Four", "Twelve"], "Siete generaciones."),
        F("García Márquez ___ en Colombia.", "nació", ["nacieron", "nací", "naciste"], "Singular subject.", tr="García Márquez was born in Colombia.", lemma="nacer:él:pret"),
        F("Él ___ el Premio Nobel en mil novecientos ochenta y dos.", "recibió", ["recibieron", "recibí", "recibimos"], "Singular subject.", tr="He received the Nobel Prize in nineteen eighty-two.", lemma="recibir:él:pret"),
        F("Cien años de soledad ___ la historia de una familia.", "cuenta", ["cuentan", "cuento", "cuentas"], "Singular subject.", tr="One Hundred Years of Solitude tells the story of a family.", lemma="contar:él"),
        F("Los Buendía viven en un pueblo ___.", "imaginario", ["imaginaria", "imaginarios", "imaginar"], "Masculine singular: pueblo.", tr="The Buendías live in an imaginary town."),
        F("La novela ___ siete generaciones.", "sigue", ["siguen", "sigo", "seguimos"], "Singular subject.", tr="The novel follows seven generations.", lemma="seguir:él"),
        F("Muchos lectores ___ esa novela.", "leyeron", ["leyó", "leímos", "leí"], "Plural subject.", tr="Many readers read that novel.", lemma="leer:ellos:pret"),
    ],
    verify=vpp("recibir", "recibí", "recibiste", "recibió", "recibimos", "recibisteis", "recibieron") + vpp("leer", "leí", "leíste", "leyó", "leímos", "leísteis", "leyeron"),
)

# ---------------------------------------------------------------------------- 839
L839 = lesson(
    "Magical realism and journalism: two sides of García Márquez",
    "En su obra lo extraordinario parece normal. Él conocía el periodismo y la fantasía.",
    requires=["realidad", "fantasía", "magia", "periodismo", "periodista", "personaje", "aceptar", "mezclar", "historia", "contar", "tradición", "testimonio"],
    cards=[
        card("How magical realism works",
             "In magical realism, a strange event, such as a person rising into the sky, is described in a calm voice. The characters are not shocked. "
             "The effect is that the reader accepts the extraordinary as part of daily life. Many critics link this to oral storytelling, in which grandparents tell wonders in a serious tone.",
             tables=[table(["Elemento", "En el realismo mágico"],
                           [["Tono", "tranquilo y serio"], ["Personajes", "aceptan lo extraordinario"],
                            ["Lugar", "pueblos y ciudades reales o imaginarios"], ["Tiempo", "la historia y el mito se mezclan"]],
                           say=[1])]),
        card("Journalism and fiction",
             "García Márquez worked as a journalist before and during his career as a novelist. Critics often say that he used journalistic detail to make fantastic scenes feel believable. "
             "Some readers also see his novels as a portrait of Colombian and Latin American history. Others warn against reading them only as history.",
             examples=[
                 ex("Los personajes aceptan lo extraordinario como si fuera normal.", "The characters accept the extraordinary as if it were normal.", "como si fuera"),
                 ex("El narrador habla como si todo fuera cierto.", "The narrator talks as if everything were true.", "como si todo fuera"),
                 ex("Muchos críticos mencionan su trabajo de periodista.", "Many critics mention his work as a journalist.", "periodista"),
             ]),
    ],
    exercises=[
        M("How do characters react to strange events in magical realism?", "They accept them calmly", ["They always run away", "They write letters", "They call the police"], "Calm acceptance."),
        M("How can journalism help a novelist, according to critics?", "Detail makes fantasy feel believable", ["It removes all fantasy", "It makes novels shorter", "It makes novels illegal"], "Journalistic detail."),
        M("What do some critics say about reading his novels only as history?", "They warn that this limits the reading", ["They say it is the only way", "They say history is invented", "They say novels cannot be read"], "Others warn against it."),
        F("Los personajes ___ lo extraordinario sin sorpresa.", "aceptan", ["acepta", "aceptamos", "aceptas"], "Plural subject.", tr="The characters accept the extraordinary without surprise.", lemma="aceptar:ellos"),
        F("El narrador ___ con un tono tranquilo.", "habla", ["hablan", "hablamos", "hablas"], "Singular subject.", tr="The narrator speaks in a calm tone.", lemma="hablar:él"),
        F("En esa novela la historia y el mito se ___.", "mezclan", ["mezcla", "mezclamos", "mezclas"], "Plural subject.", tr="In that novel history and myth mix.", lemma="mezclar:ellos"),
        F("García Márquez ___ como periodista antes de ser novelista famoso.", "trabajó", ["trabajaron", "trabajé", "trabajaste"], "Singular subject, preterite.", tr="García Márquez worked as a journalist before becoming a famous novelist.", lemma="trabajar:él:pret"),
        F("Lo extraordinario parece ___ en esos libros.", "normal", ["normales", "normalmente", "normalidad"], "Adjective.", tr="The extraordinary seems normal in those books."),
        F("Muchos críticos ___ la mezcla de realidad y fantasía.", "admiran", ["admira", "admiramos", "admiras"], "Plural subject.", tr="Many critics admire the mix of reality and fantasy.", lemma="admirar:ellos"),
    ],
    verify=vpp("trabajar", "trabajé", "trabajaste", "trabajó", "trabajamos", "trabajasteis", "trabajaron"),
)

# ---------------------------------------------------------------------------- 840
L840 = lesson(
    "Gabriela Mistral: teacher, poet and Nobel laureate",
    "Gabriela Mistral fue maestra rural y poeta. Ganó el Premio Nobel en mil novecientos cuarenta y cinco.",
    requires=["poeta", "maestro", "escuela", "niño", "derecho", "mujer", "ganar", "premio", "morir", "viajar", "diplomático", "pueblo"],
    cards=[
        card("Her life",
             "Gabriela Mistral is the pen name of Lucila Godoy Alcayaga (1889–1957), who was born in Chile. She worked as a rural teacher and later as an educator and diplomat. "
             "In 1945 she became the first Latin American writer to win the Nobel Prize in Literature. She died in New York.",
             tables=[table(["Dato", "Información"],
                           [["Nombre verdadero", "Lucila Godoy Alcayaga"], ["Seudónimo", "Gabriela Mistral"],
                            ["País", "Chile"], ["Oficios", "maestra, poeta y diplomática"],
                            ["Libros", "Desolación, Ternura, Tala y Lagar"],
                            ["Premio Nobel", "mil novecientos cuarenta y cinco"]],
                           say=[1])]),
        card("Her concerns",
             "Mistral wrote about children, motherhood, nature, pain and faith. She also spoke in favor of education, women's rights, children and Indigenous peoples. "
             "Her poetry uses simple words but strong feelings.",
             examples=[
                 ex("Fue maestra en escuelas rurales.", "She was a teacher in rural schools.", "maestra"),
                 ex("Defendió los derechos de las mujeres y de los niños.", "She defended the rights of women and children.", "Defendió"),
                 ex("Ganó el Premio Nobel de Literatura en mil novecientos cuarenta y cinco.", "She won the Nobel Prize in Literature in nineteen forty-five.", "Ganó"),
             ]),
    ],
    exercises=[
        M("What is “Gabriela Mistral”?", "A pen name", ["A school", "A book", "A city"], "Seudónimo."),
        M("What was special about her Nobel Prize in 1945?", "She was the first Latin American writer to win it", ["She was the youngest winner", "She won it twice", "It was for painting"], "First for Latin America."),
        M("Which topic did Mistral NOT mainly write about?", "Airplane engines", ["Children", "Nature", "Pain and faith"], "Her themes were human and natural."),
        F("Mistral ___ maestra en escuelas rurales.", "fue", ["fueron", "fui", "fuimos"], "Singular subject, preterite of ser.", tr="Mistral was a teacher in rural schools.", lemma="ser:ella:pret"),
        F("Ella ___ los derechos de los niños.", "defendió", ["defendieron", "defendí", "defendimos"], "Singular subject.", tr="She defended children's rights.", lemma="defender:ella:pret"),
        F("Gabriela Mistral ___ el Premio Nobel en mil novecientos cuarenta y cinco.", "ganó", ["ganaron", "gané", "ganamos"], "Singular subject.", tr="Gabriela Mistral won the Nobel Prize in nineteen forty-five.", lemma="ganar:ella:pret"),
        F("Ella ___ en Nueva York.", "murió", ["murieron", "morí", "morimos"], "Singular subject.", tr="She died in New York.", lemma="morir:ella:pret"),
        F("Sus poemas usan palabras sencillas y sentimientos ___.", "fuertes", ["fuerte", "fuerza", "fuertemente"], "Plural adjective.", tr="Her poems use simple words and strong feelings."),
        F("Mistral ___ por muchos países como diplomática.", "viajó", ["viajaron", "viajé", "viajamos"], "Singular subject.", tr="Mistral traveled through many countries as a diplomat.", lemma="viajar:ella:pret"),
    ],
    verify=vpp("defender", "defendí", "defendiste", "defendió", "defendimos", "defendisteis", "defendieron") + vpp("ganar", "gané", "ganaste", "ganó", "ganamos", "ganasteis", "ganaron"),
)

# ---------------------------------------------------------------------------- 841
L841 = lesson(
    "Miguel Ángel Asturias: Guatemala, myth and a dictator in fiction",
    "Asturias estudió la cultura maya y escribió novelas con mitos y leyendas.",
    requires=["escritor", "estudiar", "cultura", "leyenda", "mito", "dictador", "novela", "diplomático", "vivir", "premio", "morir", "país"],
    cards=[
        card("Life and work",
             "Miguel Ángel Asturias (1899–1974) was born in Guatemala City. He studied law, lived in Europe for years and became interested in Maya culture and its stories. "
             "He worked as a writer, journalist and diplomat, and spent many years outside his country. He received the Nobel Prize in Literature in 1967 and died in Madrid.",
             tables=[table(["Obra", "Tema"],
                           [["Leyendas de Guatemala", "cuentos inspirados en mitos y leyendas"],
                            ["El Señor Presidente", "novela sobre un dictador ficticio"],
                            ["Hombres de maíz", "la cultura maya y la vida en el campo"]],
                           say=[0, 1])]),
        card("Why he matters",
             "Asturias helped bring Indigenous myths and Latin American politics into the novel. Critics often see him as a forerunner of magical realism. "
             "In El Señor Presidente the dictator is a fictional character, though many critics read the novel as inspired by Guatemala’s real history of dictatorship.",
             examples=[
                 ex("Asturias estudió la cultura maya.", "Asturias studied Maya culture.", "estudió"),
                 ex("Vivió muchos años fuera de su país.", "He lived many years outside his country.", "Vivió"),
                 ex("Ganó el Premio Nobel en mil novecientos sesenta y siete.", "He won the Nobel Prize in nineteen sixty-seven.", "Ganó"),
             ]),
    ],
    exercises=[
        M("What interested Asturias about Guatemalan culture?", "Maya myths and legends", ["Modern skyscrapers", "Space travel", "Soccer rules"], "Mitos y leyendas."),
        M("What is El Señor Presidente about?", "A fictional dictator in a novel", ["A cooking contest", "A school trip", "A scientific discovery"], "A fictional dictator."),
        M("Why do critics call him a forerunner of magical realism?", "He mixed myths and everyday life", ["He wrote only about science", "He wrote only poems", "He never used fiction"], "Mito y vida diaria."),
        F("Asturias ___ la cultura maya.", "estudió", ["estudiaron", "estudié", "estudiamos"], "Singular subject.", tr="Asturias studied Maya culture.", lemma="estudiar:él:pret"),
        F("Él ___ muchos años fuera de su país.", "vivió", ["vivieron", "viví", "vivimos"], "Singular subject.", tr="He lived many years outside his country.", lemma="vivir:él:pret"),
        F("Asturias ___ el Premio Nobel en mil novecientos sesenta y siete.", "ganó", ["ganaron", "gané", "ganamos"], "Singular subject.", tr="Asturias won the Nobel Prize in nineteen sixty-seven.", lemma="ganar:él:pret"),
        F("Sus novelas tienen mitos y ___.", "leyendas", ["leyenda", "leyó", "leer"], "Plural noun.", tr="His novels have myths and legends."),
        F("El Señor Presidente ___ de un dictador ficticio.", "trata", ["tratan", "trato", "tratamos"], "Singular subject (tratar de).", tr="El Señor Presidente is about a fictional dictator.", lemma="tratar:él"),
        F("Muchos críticos lo ___ como un precursor del realismo mágico.", "consideran", ["considera", "consideramos", "consideras"], "Plural subject.", tr="Many critics consider him a forerunner of magical realism.", lemma="considerar:ellos"),
    ],
    verify=vpp("estudiar", "estudié", "estudiaste", "estudió", "estudiamos", "estudiasteis", "estudiaron"),
)

# ---------------------------------------------------------------------------- 842
L842 = lesson(
    "Mario Vargas Llosa: novels, essays and the Nobel Prize",
    "Vargas Llosa nació en Perú, escribió novelas y ensayos y ganó el Premio Nobel en dos mil diez.",
    requires=["escritor", "novela", "ensayo", "premio", "nacer", "morir", "ganar", "escribir", "lector", "crítico", "periodismo", "obra"],
    cards=[
        card("Life and work",
             "Mario Vargas Llosa was born in Arequipa, Peru, in 1936 and died in Lima in 2025. He wrote novels, plays, essays and newspaper articles, and he lived in several countries. "
             "He received the Cervantes Prize in 1994 and the Nobel Prize in Literature in 2010. His readers and critics have had different opinions about his public statements, but his place in Spanish-language literature is widely recognized.",
             tables=[table(["Obra", "Tipo"],
                           [["La ciudad y los perros", "novela sobre una escuela militar, publicada en mil novecientos sesenta y tres"],
                            ["Conversación en La Catedral", "novela sobre la vida y la política en el Perú"],
                            ["La fiesta del Chivo", "novela sobre una dictadura en el Caribe"]],
                           say=[0])]),
        card("What makes his fiction distinctive",
             "Critics often mention his complex structure, with several voices and times that cross each other. "
             "He also wrote essays about literature, in which he explained why stories matter in society.",
             examples=[
                 ex("Vargas Llosa nació en Arequipa.", "Vargas Llosa was born in Arequipa.", "nació"),
                 ex("Escribió novelas, ensayos y artículos.", "He wrote novels, essays and articles.", "Escribió"),
                 ex("Murió en Lima en dos mil veinticinco.", "He died in Lima in twenty twenty-five.", "Murió"),
             ]),
    ],
    exercises=[
        M("What kinds of texts did Vargas Llosa write?", "Novels, essays and articles", ["Only songs", "Only cookbooks", "Only legal documents"], "Several genres."),
        M("What do critics notice about his narrative structure?", "Several voices and times cross each other", ["It has only one voice", "It has no characters", "It is always a poem"], "Complex structure."),
        M("What prize did he receive in 2010?", "The Nobel Prize in Literature", ["The Cervantes Prize", "A film prize", "A science prize"], "Nobel."),
        F("Vargas Llosa ___ en Arequipa.", "nació", ["nacieron", "nací", "naciste"], "Singular subject.", tr="Vargas Llosa was born in Arequipa.", lemma="nacer:él:pret"),
        F("Él ___ novelas, ensayos y artículos.", "escribió", ["escribieron", "escribí", "escribimos"], "Singular subject.", tr="He wrote novels, essays and articles.", lemma="escribir:él:pret"),
        F("Vargas Llosa ___ el Premio Nobel en dos mil diez.", "ganó", ["ganaron", "gané", "ganamos"], "Singular subject.", tr="Vargas Llosa won the Nobel Prize in twenty ten.", lemma="ganar:él:pret"),
        F("Él ___ en Lima en dos mil veinticinco.", "murió", ["murieron", "morí", "morimos"], "Singular subject.", tr="He died in Lima in twenty twenty-five.", lemma="morir:él:pret"),
        F("Sus novelas tienen varias ___ y varios tiempos.", "voces", ["voz", "vozes", "vocal"], "Plural of voz.", tr="His novels have several voices and several times."),
        F("Los críticos ___ su estructura compleja.", "destacan", ["destaca", "destacamos", "destacas"], "Plural subject.", tr="Critics highlight his complex structure.", lemma="destacar:ellos"),
    ],
    verify=vpp("nacer", "nací", "naciste", "nació", "nacimos", "nacisteis", "nacieron"),
)

# ---------------------------------------------------------------------------- 843
L843 = lesson(
    "Elena Poniatowska: chronicle and testimony from Mexico",
    "Elena Poniatowska nació en París, creció en México y escribió crónicas con voces de la gente.",
    requires=["escritora", "periodista", "nacer", "crecer", "ciudad", "voz", "gente", "testimonio", "escribir", "premio", "entrevista", "historia"],
    cards=[
        card("Life and work",
             "Elena Poniatowska was born in Paris in 1932 and grew up in Mexico. She began as a journalist and became known for chronicles and interviews that give space to ordinary people. "
             "She received the Cervantes Prize in 2013.",
             tables=[table(["Obra", "Qué es"],
                           [["Hasta no verte, Jesús mío", "novela basada en entrevistas con una mujer de la clase trabajadora"],
                            ["La noche de Tlatelolco", "libro de testimonios sobre el movimiento estudiantil de mil novecientos sesenta y ocho"],
                            ["Premio Cervantes", "recibido en dos mil trece"]],
                           say=[0, 1])]),
        card("Testimonial writing",
             "Testimonial writing collects the voices of witnesses and mixes them with the author's own text. It can give a version of events that official records leave out. "
             "Different readers value it in different ways, and some also discuss how an author selects and edits voices.",
             examples=[
                 ex("Poniatowska nació en París y creció en México.", "Poniatowska was born in Paris and grew up in Mexico.", "creció"),
                 ex("Escribió crónicas con las voces de la gente.", "She wrote chronicles with the voices of ordinary people.", "voces"),
                 ex("Recibió el Premio Cervantes en dos mil trece.", "She received the Cervantes Prize in twenty thirteen.", "Recibió"),
             ]),
    ],
    exercises=[
        M("Where was Poniatowska born?", "In Paris", ["In Mexico City", "In Madrid", "In Lima"], "Nació en París."),
        M("What does testimonial writing do?", "It collects the voices of witnesses", ["It avoids all real people", "It only describes animals", "It is always poetry"], "Voices of witnesses."),
        M("What do some readers also discuss about this kind of writing?", "How the author selects and edits the voices", ["Whether paper is expensive", "Which color the cover has", "How long the author sleeps"], "Selection and editing."),
        F("Poniatowska ___ en París.", "nació", ["nacieron", "nací", "naciste"], "Singular subject.", tr="Poniatowska was born in Paris.", lemma="nacer:ella:pret"),
        F("Ella ___ en México.", "creció", ["crecieron", "crecí", "crecimos"], "Singular subject.", tr="She grew up in Mexico.", lemma="crecer:ella:pret"),
        F("Escribió crónicas con las ___ de la gente.", "voces", ["voz", "vozes", "vocal"], "Plural of voz.", tr="She wrote chronicles with the voices of ordinary people."),
        F("Poniatowska ___ el Premio Cervantes en dos mil trece.", "recibió", ["recibieron", "recibí", "recibimos"], "Singular subject.", tr="Poniatowska received the Cervantes Prize in twenty thirteen.", lemma="recibir:ella:pret"),
        F("Ella ___ entrevistas a muchas personas.", "hizo", ["hicieron", "hice", "hicimos"], "Singular subject.", tr="She did interviews with many people.", lemma="hacer:ella:pret"),
        F("Sus libros ___ atención a la gente común.", "prestan", ["presta", "prestamos", "prestas"], "Plural subject (prestar atención).", tr="Her books pay attention to ordinary people.", lemma="prestar:ellos"),
    ],
    verify=vpp("crecer", "crecí", "creciste", "creció", "crecimos", "crecisteis", "crecieron") + vpp("hacer", "hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"),
)

# ---------------------------------------------------------------------------- 844
L844 = lesson(
    "More voices: Cortázar, Borges and Allende",
    "Cortázar y Borges escribieron cuentos extraordinarios. Allende escribió La casa de los espíritus.",
    requires=["cuento", "escritor", "novela", "biblioteca", "espejo", "libro", "fantástico", "traducir", "idioma", "autor", "obra", "lector"],
    cards=[
        card("Three famous authors",
             "These short portraits are in our own words. Julio Cortázar (1914–1984), born in Belgium to Argentine parents, is known for short stories where the fantastic breaks into daily life, and for the novel Rayuela (1963), which readers can enter in different orders. "
             "Jorge Luis Borges (1899–1986), from Buenos Aires, wrote short stories, essays and poems about libraries, mirrors, labyrinths and infinity; Ficciones is one of his best-known books. "
             "Isabel Allende, a Chilean writer born in Lima in 1942, became widely known for La casa de los espíritus (1982), a family saga with some magical elements. Her books have been translated into many languages.",
             tables=[table(["Autor", "País asociado", "Obra conocida"],
                           [["Julio Cortázar", "Argentina", "Rayuela"], ["Jorge Luis Borges", "Argentina", "Ficciones"],
                            ["Isabel Allende", "Chile", "La casa de los espíritus"]],
                           say=[0, 1, 2])]),
        card("Using the preterite and present perfect",
             "Use the preterite for the moment a work was written. The present perfect is often used for something that still holds today (in much of Latin America, the preterite or the present is also common).",
             examples=[
                 ex("Borges escribió cuentos sobre bibliotecas y espejos.", "Borges wrote stories about libraries and mirrors.", "escribió"),
                 ex("Los libros de Allende se han traducido a muchos idiomas.", "Allende's books have been translated into many languages.", "se han traducido"),
             ]),
    ],
    exercises=[
        M("Which author is known for stories about libraries, mirrors and labyrinths?", "Borges", ["Allende", "Mistral", "Darío"], "Borges."),
        M("What is special about Rayuela?", "Readers can enter it in different orders", ["It has no words", "It is only a poem", "It has one sentence"], "Different reading orders."),
        M("Which book is a family saga with some magical elements?", "La casa de los espíritus", ["Ficciones", "Rayuela", "Azul…"], "Allende."),
        F("Borges ___ cuentos sobre bibliotecas y espejos.", "escribió", ["escribieron", "escribí", "escribimos"], "Singular subject.", tr="Borges wrote stories about libraries and mirrors.", lemma="escribir:él:pret"),
        F("Los libros de Allende se han ___ a muchos idiomas.", "traducido", ["traducir", "traduciendo", "tradujeron"], "Participle of traducir.", tr="Allende's books have been translated into many languages.", lemma="traducir:part"),
        F("Cortázar ___ cuentos fantásticos y novelas.", "escribió", ["escribieron", "escribí", "escribimos"], "Singular subject.", tr="Cortázar wrote fantastic stories and novels.", lemma="escribir:él:pret"),
        F("Isabel Allende es una escritora ___.", "chilena", ["chileno", "chilenas", "chilenos"], "Feminine singular.", tr="Isabel Allende is a Chilean writer."),
        F("Los cuentos de Borges ___ a muchos lectores.", "han fascinado", ["ha fascinado", "hemos fascinado", "has fascinado"], "Plural subject with haber.", tr="Borges's stories have fascinated many readers."),
        F("Borges y Cortázar ___ argentinos.", "son", ["es", "somos", "eres"], "Plural subject.", tr="Borges and Cortázar are Argentine.", lemma="ser:ellos"),
    ],
    verify=vpa("traducir", "traducido") + vpp("escribir", "escribí", "escribiste", "escribió", "escribimos", "escribisteis", "escribieron"),
)

# ---------------------------------------------------------------------------- 845
L845 = lesson(
    "Words about literature: reseña, ejemplar, seudónimo, portada…",
    "Compré un ejemplar de la novela. La reseña elogió la portada.",
    requires=["académico", "catedrático", "ejemplar", "intelectual", "novedad", "portada", "reseña", "libro", "autor", "novela", "universidad", "periódico"],
    cards=[
        card("Twelve words for talking about books and ideas",
             "These words come up in book reviews, university talks and cultural news. Learn each one with its article. Note that el ejemplar is masculine even for a book that a woman wrote.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el académico", "scholar, academic", "Un académico habló del libro."],
                            ["el catedrático", "university professor", "El catedrático dio una conferencia."],
                            ["la crónica", "chronicle, news report", "La crónica cuenta los hechos en orden."],
                            ["el ejemplar", "copy (of a book)", "Compré un ejemplar de la novela."],
                            ["el erudito", "learned person", "El erudito conocía idiomas antiguos."],
                            ["el intelectual", "intellectual", "Los intelectuales discutieron la idea."],
                            ["la novedad", "novelty, new thing", "La novedad es un libro de poemas."],
                            ["el pedagogo", "educator", "Un pedagogo estudia cómo se aprende."],
                            ["la portada", "cover, front page", "La portada del libro es azul."],
                            ["la reseña", "review (of a book or film)", "La reseña apareció en el periódico."],
                            ["el seudónimo", "pen name", "Firmó sus poemas con un seudónimo."],
                            ["el surgimiento", "emergence", "El surgimiento del boom cambió todo."]],
                           say=[0, 2])]),
        card("Two extra words",
             "A pergamino is a parchment, an old writing surface made of animal skin. An anacronismo is something that appears in the wrong period, such as a mobile phone in a story set in the Middle Ages.",
             examples=[
                 ex("Un teléfono en una novela medieval sería un anacronismo.", "A phone in a medieval novel would be an anachronism.", "anacronismo"),
                 ex("El pergamino era muy antiguo.", "The parchment was very old.", "pergamino"),
             ]),
    ],
    exercises=[
        M("What is a “seudónimo”?", "A pen name", ["A book cover", "A review", "A teacher"], "Firmar con otro nombre."),
        M("What does “ejemplar” mean in “un ejemplar de la novela”?", "A copy", ["An example sentence", "A chapter", "A film"], "A copy of a book."),
        M("Which person studies how people teach and learn?", "El pedagogo", ["El erudito", "El académico", "El seudónimo"], "Pedagogo."),
        F("Compré un ___ de la novela en la librería.", "ejemplar", ["seudónimo", "pergamino", "anacronismo"], "A copy.", tr="I bought a copy of the novel at the bookstore."),
        F("La ___ del periódico elogió el libro.", "reseña", ["pergamino", "seudónimo", "ejemplar"], "A review praises.", tr="The review in the newspaper praised the book."),
        F("Ella publicó sus primeros poemas con un ___.", "seudónimo", ["catedrático", "pergamino", "ejemplar"], "A pen name.", tr="She published her first poems under a pen name."),
        F("El ___ da clases en la universidad.", "catedrático", ["seudónimo", "pergamino", "anacronismo"], "University professor.", tr="The professor teaches at the university."),
        F("En la ___ del libro aparece el título y el nombre del autor.", "portada", ["resonancia", "seudónimo", "anacronismo"], "The cover.", tr="On the cover of the book the title and the author's name appear."),
        F("Un teléfono en una película de la Edad Media es un ___.", "anacronismo", ["pergamino", "seudónimo", "ejemplar"], "Out of its time.", tr="A phone in a movie set in the Middle Ages is an anachronism."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 846
L846 = lesson(
    "Adjectives for people and works: audaz, culto, controvertido, póstumo…",
    "Una escritora audaz publicó una obra controvertida. Su libro póstumo salió después.",
    requires=["culto", "camino", "poeta", "obra", "autor", "mujer", "niño", "región", "planta", "arena", "libro", "muerte"],
    cards=[
        card("Ten adjectives",
             "Most of these adjectives change for gender and number like normal adjectives. Audaz ends in -z, so the plural is audaces. Caminante can be an adjective or a noun, and it has the same form for masculine and feminine.",
             tables=[table(["Adjetivo", "English", "Ejemplo"],
                           [["audaz, audaces", "daring", "Fue una decisión audaz."],
                            ["culto, culta", "educated, cultured", "Era una mujer muy culta."],
                            ["inculto, inculta", "uneducated", "Ese tema no es para gente inculta."],
                            ["controvertido, controvertida", "controversial", "La película es muy controvertida."],
                            ["exaltado, exaltada", "agitated, heated", "El público estaba exaltado."],
                            ["desvalido, desvalida", "defenseless", "Ayudó a los niños desvalidos."],
                            ["descalzo, descalza", "barefoot", "Los niños caminaban descalzos."],
                            ["autóctono, autóctona", "native, indigenous to a place", "Las plantas autóctonas crecen aquí."],
                            ["póstumo, póstuma", "posthumous", "Su obra póstuma se publicó años después."],
                            ["caminante", "walker, wanderer", "Un caminante cruzó el pueblo."]],
                           say=[0, 2])]),
        card("A note on tone",
             "Inculto is not a gentle word. It describes a lack of education and can sound insulting. Use it with care, and prefer neutral descriptions of people when possible.",
             examples=[
                 ex("Los escritores audaces cambiaron la poesía.", "Daring writers changed poetry.", "audaces"),
                 ex("La obra póstuma salió después de su muerte.", "The posthumous work appeared after his death.", "póstuma"),
             ]),
    ],
    exercises=[
        M("What is the plural of “audaz”?", "audaces", ["audazes", "audaz", "audazos"], "-z → -ces."),
        M("What does “póstumo” describe?", "Something that happens after death", ["Something very old", "Something very small", "Something secret"], "Posthumous."),
        M("What is the opposite of “culto” (educated)?", "inculto", ["controvertido", "descalzo", "exaltado"], "In- negates."),
        F("Los escritores ___ cambiaron la literatura.", "audaces", ["audaz", "audazes", "audaza"], "Plural of audaz.", tr="Daring writers changed literature."),
        F("La obra ___ del poeta se publicó después de su muerte.", "póstuma", ["póstumo", "póstumos", "póstumas"], "Feminine singular: obra.", tr="The poet's posthumous work was published after his death."),
        F("Ella era una mujer muy ___ y leía mucho.", "culta", ["culto", "cultas", "cultos"], "Feminine singular.", tr="She was a very educated woman and read a lot."),
        F("Los niños caminaban ___ por la arena.", "descalzos", ["descalzo", "descalza", "descalzas"], "Masculine plural.", tr="The children walked barefoot on the sand."),
        F("La película es muy ___: algunas personas la aman y otras la critican.", "controvertida", ["controvertido", "controvertidas", "controvertidos"], "Feminine singular: película.", tr="The movie is very controversial: some people love it and others criticize it."),
        F("Las plantas ___ de la región son importantes.", "autóctonas", ["autóctono", "autóctonos", "autóctona"], "Feminine plural.", tr="The native plants of the region are important."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 847
L847 = lesson(
    "More adjectives: agudo, ardiente, blando, desgarrador, incontable…",
    "Sintió un dolor agudo. Había incontables estrellas. Fue una escena desgarradora.",
    requires=["agudo", "concreto", "tremendo", "dolor", "estrella", "escena", "sol", "cama", "ejemplo", "ciudad", "calle", "fuego"],
    cards=[
        card("Nine more adjectives",
             "Adjectives ending in -dor add -a for the feminine (desgarrador → desgarradora). Adjectives ending in -e or -nte (circundante, incontable) keep the same form in the feminine.",
             tables=[table(["Adjetivo", "English", "Ejemplo"],
                           [["agudo, aguda", "sharp, acute", "Sintió un dolor agudo."],
                            ["ardiente", "burning, ardent", "Hacía un sol ardiente."],
                            ["blando, blanda", "soft", "La almohada es muy blanda."],
                            ["circundante", "surrounding", "Las calles circundantes estaban cerradas."],
                            ["concreto, concreta", "specific, concrete", "Necesito un ejemplo concreto."],
                            ["desgarrador, desgarradora", "heartbreaking", "Fue una escena desgarradora."],
                            ["desolado, desolada", "desolate, devastated", "La ciudad quedó desolada."],
                            ["incontable", "countless", "Había incontables estrellas."],
                            ["tremendo, tremenda", "huge, terrible", "Cometió un tremendo error."]],
                           say=[0, 2])]),
        card("Usage",
             "Incontable can go before or after the noun. Before the noun (incontables estrellas) it works like a quantity word and is very common; after the noun (estrellas incontables) it sounds more descriptive or literary.",
             examples=[
                 ex("Hacía un sol ardiente en la plaza.", "The sun was burning hot in the square.", "ardiente"),
                 ex("La noticia fue desgarradora.", "The news was heartbreaking.", "desgarradora"),
             ]),
    ],
    exercises=[
        M("Which adjective means “countless”?", "incontable", ["blando", "agudo", "concreto"], "Not able to be counted."),
        M("What is the feminine form of “desgarrador”?", "desgarradora", ["desgarrada", "desgarradores", "desgarrador"], "-dor → -dora."),
        M("Which adjective stays the same for masculine and feminine?", "ardiente", ["blando", "agudo", "concreto"], "-nte."),
        F("Sintió un dolor ___ en la espalda.", "agudo", ["aguda", "agudos", "agudas"], "Masculine singular: dolor.", tr="He felt a sharp pain in his back."),
        F("Hacía un sol ___ en la plaza.", "ardiente", ["ardientes", "ardiento", "ardienta"], "Singular, same for both genders.", tr="The sun was burning hot in the square."),
        F("La almohada es muy ___.", "blanda", ["blando", "blandas", "blandos"], "Feminine singular.", tr="The pillow is very soft."),
        F("Fue una escena ___ y todos lloramos.", "desgarradora", ["desgarrador", "desgarrados", "desgarradoras"], "Feminine singular.", tr="It was a heartbreaking scene and we all cried."),
        F("Necesito un ejemplo ___.", "concreto", ["concreta", "concretos", "concretas"], "Masculine singular.", tr="I need a specific example."),
        F("La ciudad quedó ___ después de la guerra.", "desolada", ["desolado", "desoladas", "desolados"], "Feminine singular: ciudad.", tr="The city was left desolate after the war."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 848
L848 = lesson(
    "Feelings and states: angustia, desaliento, pavor, melancolía…",
    "Sintió pavor. La melancolía le daba ganas de escribir.",
    requires=["alma", "placer", "queja", "maldad", "azar", "dormir", "noche", "sentir", "miedo", "tristeza", "querer", "escribir"],
    cards=[
        card("Twelve nouns for inner life",
             "These nouns are common in literature and in careful speech. Alma is feminine, but it takes el in the singular (el alma, las almas) because it starts with a stressed a-.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el alma (f.)", "soul", "Ella puso toda su alma en el poema."],
                            ["la angustia", "anguish", "Sintió angustia antes del examen."],
                            ["el ardor", "fervor, passion; burning feeling", "Habló con ardor."],
                            ["el desaliento", "discouragement", "El desaliento no lo detuvo."],
                            ["la desconfianza", "distrust", "Miraba al extraño con desconfianza."],
                            ["el insomnio", "insomnia", "Tuvo insomnio toda la semana."],
                            ["la melancolía", "melancholy", "El otoño le daba melancolía."],
                            ["el pavor", "dread, terror", "Sintió pavor en la oscuridad."],
                            ["el placer", "pleasure", "Leer es un placer."],
                            ["la queja", "complaint", "No hubo ninguna queja."],
                            ["la rabia", "rage (also: rabies)", "Gritó de rabia."],
                            ["la frivolidad", "frivolity", "Criticó la frivolidad de la fiesta."]],
                           say=[0, 2])]),
        card("A few cautions",
             "If you say ¡Qué rabia! you mean “How infuriating!” Insomnio is a common word, not a technical one. The word alma often appears in poetry and in everyday phrases such as con toda el alma.",
             examples=[
                 ex("Con toda el alma agradeció la ayuda.", "She thanked them for the help with all her heart.", "el alma"),
                 ex("Sintió pavor al oír el ruido.", "He felt dread when he heard the noise.", "pavor"),
             ]),
    ],
    exercises=[
        M("Which article goes with “alma” in the singular?", "el alma", ["la alma", "los alma", "las alma"], "Feminine noun, but el before stressed a-."),
        M("Which word means a deep, freezing fear?", "pavor", ["rabia", "queja", "placer"], "Dread."),
        M("What does “la rabia” mean?", "Rage (and also rabies)", ["A complaint", "Pleasure", "A memory"], "Rage."),
        F("Después de perder tantas veces, sintió ___ y quiso renunciar.", "desaliento", ["placer", "insomnio", "queja"], "Discouragement.", tr="After losing so many times, he felt discouraged and wanted to quit."),
        F("Tuvo ___ y no durmió en toda la noche.", "insomnio", ["placer", "desaliento", "queja"], "Could not sleep.", tr="She had insomnia and did not sleep all night."),
        F("Leer es un ___ para muchas personas.", "placer", ["pavor", "insomnio", "desaliento"], "A pleasure.", tr="Reading is a pleasure for many people."),
        F("La ___ de los vecinos era por el ruido.", "queja", ["melancolía", "pavor", "desconfianza"], "A complaint.", tr="The neighbors' complaint was about the noise."),
        F("Miraba al desconocido con ___ y no le abrió la puerta.", "desconfianza", ["placer", "insomnio", "melancolía"], "Distrust.", tr="She looked at the stranger with distrust and did not open the door."),
        F("Los otoños le daban ___ y escribía poemas tristes.", "melancolía", ["placer", "queja", "ardor"], "Melancholy.", tr="Autumns gave him melancholy and he wrote sad poems."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 849
L849 = lesson(
    "Fate, family and the future: azar, porvenir, presagio, estirpe…",
    "Se encontraron por azar. Pensaba en su porvenir. Aquel cielo era un mal presagio.",
    requires=["familia", "futuro", "rey", "reina", "tormenta", "enfermedad", "ciudad", "primo", "nube", "planear", "pensar", "maldad"],
    cards=[
        card("Twelve nouns about life and luck",
             "Some of these words are literary (porvenir, presagio, estirpe) and some are everyday (parto, parentesco). Realeza is a collective noun: it means royalty as a group or as a rank.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el azar", "chance, randomness", "Se encontraron por azar."],
                            ["la estirpe", "lineage", "Era de una antigua estirpe."],
                            ["el porvenir", "the future", "Pensaba en su porvenir."],
                            ["el presagio", "omen", "Las nubes negras eran un mal presagio."],
                            ["la maldad", "wickedness", "La maldad del villano sorprendió."],
                            ["el parentesco", "kinship, family relation", "El parentesco entre los primos es cercano."],
                            ["el parto", "childbirth", "El parto duró toda la noche."],
                            ["la peste", "plague (also: stench)", "Una peste afectó a la ciudad."],
                            ["la realeza", "royalty", "La realeza vivía en el palacio."],
                            ["la sobriedad", "restraint, sobriety", "Admiro la sobriedad de su estilo."],
                            ["el arranque", "outburst, start", "Tuvo un arranque de ira."],
                            ["el seno", "bosom, heart (of a group)", "En el seno de la familia hubo discusión."]],
                           say=[0, 2])]),
        card("About these words",
             "Peste can mean an epidemic, but in everyday speech it also means a bad smell. Seno has several meanings; en el seno de means “within.” Check the context.",
             examples=[
                 ex("Se conocieron por azar en un tren.", "They met by chance on a train.", "por azar"),
                 ex("En el seno de la familia hubo una larga discusión.", "There was a long discussion within the family.", "En el seno de"),
             ]),
    ],
    exercises=[
        M("What does “estirpe” refer to?", "Family lineage", ["A kind of weather", "A style of cooking", "A musical instrument"], "Lineage."),
        M("Which means “omen”?", "presagio", ["porvenir", "parto", "azar"], "Presagio."),
        M("Which noun is a literary word for “the future”?", "porvenir", ["azar", "peste", "realeza"], "El porvenir."),
        F("Se encontraron por ___; nadie lo había planeado.", "azar", ["parto", "realeza", "peste"], "By chance.", tr="They met by chance; nobody had planned it."),
        F("Los jóvenes piensan en su ___ y en su trabajo futuro.", "porvenir", ["azar", "parto", "peste"], "Their future.", tr="Young people think about their future and their future jobs."),
        F("Una ___ afectó a miles de personas en la ciudad.", "peste", ["sobriedad", "estirpe", "maldad"], "An epidemic.", tr="A plague affected thousands of people in the city."),
        F("El rey, la reina y su familia forman la ___.", "realeza", ["peste", "maldad", "sobriedad"], "Royalty.", tr="The king, the queen and their family make up royalty."),
        F("Las nubes negras fueron un ___ de la tormenta.", "presagio", ["parto", "azar", "parentesco"], "An omen.", tr="The black clouds were an omen of the storm."),
        F("El ___ entre los dos primos era muy cercano.", "parentesco", ["porvenir", "azar", "parto"], "Family relation.", tr="The family relation between the two cousins was very close."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 850
L850 = lesson(
    "Verbs of feeling and perception: acariciar, atormentar, captar, vislumbrar…",
    "Ella acaricia al gato. Los recuerdos lo atormentaban. Se vislumbraba una luz.",
    requires=["captar", "ignorar", "luz", "recuerdo", "gato", "fotógrafo", "nube", "montaña", "consejo", "campeón", "equipo", "mensaje"],
    cards=[
        card("Nine verbs",
             "Eight of the nine are regular. Desvanecer is regular except for the yo form of the present indicative (desvanezco, like conocer → conozco) and the present subjunctive built on it (desvanezca, desvanezcas…), and it is often used with se (desvanecerse = to fade away). Aquejar is usually used in the third person and often as a participle: aquejado de = suffering from.",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["acariciar", "to caress, pet", "Ella acaricia al gato."],
                            ["atormentar", "to torment", "Los recuerdos lo atormentaban."],
                            ["aquejar", "to afflict", "Una enfermedad aquejaba al pueblo."],
                            ["captar", "to capture, grasp", "El fotógrafo captó la luz de la tarde."],
                            ["desvanecerse", "to fade away", "El humo se desvaneció."],
                            ["difuminar", "to blur", "La niebla difuminaba las montañas."],
                            ["vislumbrar", "to glimpse", "Se vislumbraba una luz al fondo."],
                            ["parpadear", "to blink", "Parpadeé varias veces."],
                            ["ignorar", "to ignore; to be unaware of", "Ignoró el consejo."]],
                           say=[0, 2]),
                    table(["Persona", "acariciar (presente)", "desvanecer (presente)"],
                          [["yo", "acaricio", "desvanezco"], ["tú", "acaricias", "desvaneces"], ["él / ella / usted", "acaricia", "desvanece"],
                           ["nosotros", "acariciamos", "desvanecemos"], ["vosotros", "acariciáis", "desvanecéis"], ["ellos, ustedes", "acarician", "desvanecen"]],
                          say=[1, 2])]),
        card("A false friend",
             "Ignorar in Spanish often means “not to know” or “to be unaware of,” not only “to ignore on purpose.” Context decides. Ignoro la respuesta means “I do not know the answer.”",
             examples=[
                 ex("Ignoro la respuesta.", "I do not know the answer.", "Ignoro"),
                 ex("Ignoró el consejo de su amigo.", "He ignored his friend's advice.", "Ignoró"),
             ]),
    ],
    exercises=[
        M("What does “parpadear” mean?", "To blink", ["To whisper", "To fade", "To glimpse"], "Eyes closing and opening."),
        M("What does “Ignoro la respuesta” mean?", "I do not know the answer", ["I shout the answer", "I hide the answer", "I write the answer"], "Ignorar can mean “not know.”"),
        M("What is the yo form of “desvanecer”?", "desvanezco", ["desvanezo", "desvaneco", "desvanezgo"], "Like conocer → conozco."),
        F("Ella ___ al gato con mucho cuidado.", "acaricia", ["acarician", "acaricias", "acaricio"], "Singular subject.", tr="She pets the cat very carefully.", lemma="acariciar:ella"),
        F("Los recuerdos lo ___ todas las noches.", "atormentaban", ["atormentaba", "atormentábamos", "atormentabas"], "Plural subject, imperfect.", tr="The memories tormented him every night.", lemma="atormentar:ellos:impf"),
        F("El fotógrafo ___ la luz de la tarde.", "captó", ["captaron", "capté", "captamos"], "Singular subject, preterite.", tr="The photographer captured the afternoon light.", lemma="captar:él:pret"),
        F("Yo ___ varias veces para ver mejor.", "parpadeé", ["parpadeó", "parpadearon", "parpadeamos"], "Yo, preterite.", tr="I blinked several times to see better.", lemma="parpadear:yo:pret"),
        F("Él ___ el consejo de su amigo.", "ignoró", ["ignoraron", "ignoré", "ignoramos"], "Singular subject.", tr="He ignored his friend's advice.", lemma="ignorar:él:pret"),
        F("La niebla ___ las montañas.", "difuminaba", ["difuminaban", "difuminé", "difuminamos"], "Singular subject, imperfect.", tr="The fog blurred the mountains.", lemma="difuminar:él:impf"),
    ],
    verify=(vp("acariciar", "acaricio", "acaricias", "acaricia", "acariciamos", "acariciáis", "acarician")
            + vp("desvanecer", "desvanezco", "desvaneces", "desvanece", "desvanecemos", "desvanecéis", "desvanecen")
            + vpp("captar", "capté", "captaste", "captó", "captamos", "captasteis", "captaron")),
)

# ---------------------------------------------------------------------------- 851
L851 = lesson(
    "Verbs of action and change: conceder, designar, inculcar, prolongar, retomar…",
    "La universidad le concedió una beca. Retomó sus estudios.",
    requires=["conceder", "designar", "imponer", "repartir", "retomar", "etiquetar", "reunir", "beca", "alcalde", "directora", "reunión", "estudiar"],
    cards=[
        card("Fourteen verbs",
             "Most are regular. Verbs ending in -car or -gar change spelling before e in the yo form of the preterite: inculcar → inculqué, recalcar → recalqué, prolongar → prolongué.",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["conceder", "to grant", "La universidad le concedió una beca."],
                            ["descifrar", "to decipher", "Nadie pudo descifrar el mensaje."],
                            ["designar", "to appoint", "El alcalde designó a una nueva directora."],
                            ["encaminar", "to guide toward", "Su maestra la encaminó hacia la literatura."],
                            ["etiquetar", "to label", "No me gusta etiquetar a las personas."],
                            ["galardonar", "to award a prize to", "La academia galardonó a la poeta."],
                            ["inculcar", "to instill", "Sus padres le inculcaron el amor por los libros."],
                            ["prolongar", "to prolong", "Prolongaron la reunión una hora más."],
                            ["recalcar", "to stress, emphasize", "El profesor recalcó la importancia del ensayo."],
                            ["repartir", "to distribute", "Repartieron los libros entre los niños."],
                            ["retomar", "to resume", "Retomó sus estudios después de un año."],
                            ["tergiversar", "to distort, twist", "Es injusto tergiversar lo que dijo otra persona."],
                            ["pisar", "to step on", "Pisé un charco."],
                            ["esquivar", "to dodge", "Esquivó el charco."]],
                           say=[0, 2]),
                    table(["Infinitivo", "yo (pretérito)", "él (pretérito)"],
                          [["inculcar", "inculqué", "inculcó"], ["recalcar", "recalqué", "recalcó"], ["prolongar", "prolongué", "prolongó"]],
                          say=[1, 2])]),
        card("Notes",
             "Tergiversar is a formal verb that suggests dishonesty. Galardonar is mostly used in news about prizes, usually in the passive: fue galardonado con el premio.",
             examples=[
                 ex("La poeta fue galardonada con un premio.", "The poet was awarded a prize.", "fue galardonada"),
                 ex("No quiero tergiversar tus palabras.", "I do not want to distort your words.", "tergiversar"),
             ]),
    ],
    exercises=[
        M("What is the yo preterite of “inculcar”?", "inculqué", ["inculcé", "inculcí", "inculcó"], "c → qu before e."),
        M("What does “retomar” mean?", "To resume", ["To forget", "To prevent", "To sell"], "To take up again."),
        M("What does “tergiversar” suggest?", "Twisting the meaning of something", ["Repeating a story", "Translating a text", "Writing a letter"], "Distort."),
        F("La universidad le ___ una beca.", "concedió", ["concedieron", "concedí", "concedimos"], "Singular subject.", tr="The university granted her a scholarship.", lemma="conceder:él:pret"),
        F("El alcalde ___ a una nueva directora.", "designó", ["designaron", "designé", "designamos"], "Singular subject.", tr="The mayor appointed a new director.", lemma="designar:él:pret"),
        F("Sus padres le ___ el amor por los libros.", "inculcaron", ["inculcó", "inculqué", "inculcamos"], "Plural subject.", tr="His parents instilled in him a love of books.", lemma="inculcar:ellos:pret"),
        F("Los organizadores ___ la reunión una hora más.", "prolongaron", ["prolongó", "prolongué", "prolongamos"], "Plural subject.", tr="The organizers prolonged the meeting by one more hour.", lemma="prolongar:ellos:pret"),
        F("Los voluntarios ___ los libros entre los niños.", "repartieron", ["repartió", "repartí", "repartimos"], "Plural subject.", tr="The volunteers distributed the books among the children.", lemma="repartir:ellos:pret"),
        F("Ella ___ sus estudios después de un año.", "retomó", ["retomaron", "retomé", "retomamos"], "Singular subject.", tr="She resumed her studies after a year.", lemma="retomar:ella:pret"),
    ],
    verify=vpp("inculcar", "inculqué", None, "inculcó", None, None, "inculcaron") + vpp("prolongar", "prolongué", None, "prolongó", None, None, "prolongaron") + vpp("repartir", "repartí", "repartiste", "repartió", "repartimos", "repartisteis", "repartieron"),
)

# ---------------------------------------------------------------------------- 852
L852 = lesson(
    "Same verb, different meaning with se: apartar/apartarse, fundir/fundirse…",
    "Aparté las sillas. Apártate del fuego. Los colores se funden.",
    requires=["imponer", "reunir", "alejar", "silla", "fuego", "hierro", "color", "pintura", "regla", "lunes", "biblioteca", "estudiante"],
    cards=[
        card("Adding se changes the meaning",
             "Some verbs act on something else without se, and describe what the subject does to itself, or a change, with se. Compare the pairs below.",
             tables=[table(["Sin se", "Con se"],
                           [["apartar: move something aside", "apartarse: move away"],
                            ["alejar: move something away", "alejarse: move away, withdraw"],
                            ["enredar: tangle, confuse", "enredarse: get tangled, get caught up"],
                            ["fundir: melt something", "fundirse: merge, blend"],
                            ["imponer: impose", "imponerse: prevail"],
                            ["reunir: gather", "reunirse: meet, get together"]],
                           say=[])]),
        card("Examples",
             "Notice that the verb with se has no direct object.",
             tables=[table(["Sin se", "Con se"],
                           [["Aparté las sillas de la ventana.", "Apártate del fuego."],
                            ["Alejé al perro del camino.", "Me alejé de la ciudad."],
                            ["Enredé el hilo.", "Se enredó en una discusión."],
                            ["El artesano fundió el hierro.", "Los colores se funden en el cuadro."],
                            ["La directora impuso una regla nueva.", "La verdad se impuso al final."],
                            ["Reunimos firmas para la petición.", "Nos reuniremos el lunes."]],
                           say=[0, 1])]),
    ],
    exercises=[
        M("What does “apartarse” mean?", "To move away", ["To melt", "To gather", "To confuse"], "Apartarse = move away."),
        M("What does “La verdad se impuso” mean?", "The truth prevailed", ["The truth was hidden", "The truth was written", "The truth was sold"], "Imponerse = prevail."),
        M("Which verb means “to meet, get together”?", "reunirse", ["reunir", "fundir", "apartar"], "With se."),
        F("¡___ del fuego!", "Apártate", ["Aparta", "Apartar", "Apartado"], "Reflexive command.", tr="Move away from the fire!"),
        F("Los colores ___ en el cuadro.", "se funden", ["funden", "se fundió", "fundimos"], "Plural reflexive.", tr="The colors blend into each other in the painting."),
        F("Los estudiantes ___ en la biblioteca para estudiar.", "se reunieron", ["reunieron", "se reunió", "nos reunimos"], "Plural reflexive.", tr="The students met at the library to study."),
        F("La verdad ___ al final.", "se impuso", ["impuso", "se impusieron", "nos impusimos"], "Reflexive, singular.", tr="The truth prevailed in the end."),
        F("Ella ___ el hilo y no pudo usarlo.", "enredó", ["enredaron", "enredé", "enredamos"], "Transitive, singular.", tr="She tangled the thread and could not use it."),
        F("Nosotros nos ___ el lunes en la biblioteca.", "reuniremos", ["reunirán", "reunirás", "reuniré"], "Nosotros, future.", tr="We will meet on Monday at the library.", lemma="reunir:nosotros:fut"),
    ],
    verify=vpf("reunir", "reuniré", "reunirás", "reunirá", "reuniremos", "reuniréis", "reunirán"),
)

# ---------------------------------------------------------------------------- 853
L853 = lesson(
    "Set expressions: echar a perder, de golpe, a fin de que, en fin…",
    "De golpe empezó a llover. A partir de entonces no volvió a hablar. En fin, así fue.",
    requires=["silencio", "daño", "manifiesto", "perder", "golpe", "tarde", "cabo", "entonces", "luego", "fin", "encima", "cosecha"],
    cards=[
        card("Useful phrases for reading and writing",
             "These fixed phrases often appear in essays and literature. Learn each as a block.",
             tables=[table(["Expresión", "English", "Ejemplo"],
                           [["echar a perder", "to spoil, ruin", "La lluvia echó a perder la cosecha."],
                            ["guardar silencio", "to keep silent", "Guardaron silencio durante la ceremonia."],
                            ["hacer daño", "to hurt, harm", "Ese comentario me hizo daño."],
                            ["poner de manifiesto", "to make clear, reveal", "El estudio pone de manifiesto un problema."],
                            ["a fin de que", "so that (+ subjunctive)", "Estudia a fin de que sus padres estén orgullosos."],
                            ["a partir de entonces", "from then on", "A partir de entonces no volvió a hablar."],
                            ["acaso", "perhaps (literary); in questions, really?", "¿Acaso crees que es fácil?"],
                            ["al cabo de", "after (a period of time)", "Al cabo de dos horas terminó."],
                            ["de golpe", "suddenly", "De golpe empezó a llover."],
                            ["de tarde en tarde", "once in a while", "Lo veo de tarde en tarde."],
                            ["desde luego", "of course", "Desde luego que sí."],
                            ["en fin", "anyway, in short", "En fin, así fue."],
                            ["ni mucho menos", "far from it, not by a long shot", "No es fácil, ni mucho menos."],
                            ["por encima de", "above, beyond", "Está por encima de las demás."],
                            ["sumamente", "extremely", "Es sumamente importante."]],
                           say=[0, 2])]),
        card("Two grammar points",
             "A fin de que always needs the subjunctive, because it expresses purpose with a new subject. Acaso as a question word (¿Acaso…?) usually suggests that the answer is no.",
             examples=[
                 ex("Te llamo a fin de que no te preocupes.", "I am calling you so that you do not worry.", "a fin de que no te preocupes"),
                 ex("¿Acaso crees que es fácil?", "Do you really think it is easy?", "¿Acaso"),
             ]),
    ],
    exercises=[
        M("What does “de golpe” mean?", "Suddenly", ["Once in a while", "Of course", "Slowly"], "All at once."),
        M("What mood follows “a fin de que”?", "The subjunctive", ["The indicative", "The infinitive only", "The future"], "Purpose + new subject."),
        M("What does “ni mucho menos” mean?", "By no means", ["Very much", "Once more", "At the same time"], "A strong negation."),
        F("Estudia mucho a fin de que sus padres ___ orgullosos.", "estén", ["están", "estarán", "estaban"], "Subjunctive after a fin de que.", tr="She studies a lot so that her parents will be proud.", lemma="estar:ellos:subj"),
        F("Al ___ de dos horas, terminó la película.", "cabo", ["fin", "golpe", "lleno"], "Al cabo de.", tr="After two hours, the movie ended."),
        F("La lluvia empezó de ___ y nos mojamos.", "golpe", ["cabo", "entonces", "tarde"], "De golpe.", tr="The rain started suddenly and we got wet."),
        F("A ___ de entonces, no volvió a hablar con él.", "partir", ["pesar", "pro", "encima"], "A partir de entonces.", tr="From then on, she never spoke to him again."),
        F("El estudio ___ de manifiesto un problema serio.", "pone", ["ponen", "pongo", "ponemos"], "Singular subject.", tr="The study reveals a serious problem.", lemma="poner:él"),
        F("Guardaron ___ durante toda la ceremonia.", "silencio", ["daño", "golpe", "cabo"], "Guardar silencio.", tr="They kept silent during the whole ceremony."),
    ],
    verify=vpj("estar", "esté", "estés", "esté", "estemos", "estéis", "estén"),
)

# ---------------------------------------------------------------------------- 854
L854 = lesson(
    "Other words from the readings: senda, rebanada, antorcha, terciopelo…",
    "Seguimos una senda estrecha. Pidió una rebanada de pan. La cortina era de terciopelo.",
    requires=["rasgo", "fantasma", "torre", "polvo", "gallo", "sierra", "disfraz", "alcance", "mar", "luz", "sombra", "camino"],
    cards=[
        card("Concrete nouns",
             "These are mostly everyday objects and images. Note the gender, and notice that some words are used in figurative language: la punta de lanza literally means “spearhead” and is used for an innovative leader or movement.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["la antorcha", "torch", "Entramos a la cueva con una antorcha."],
                            ["la cabaña", "cabin", "Vivían en una cabaña junto al río."],
                            ["el ciervo", "deer", "Un ciervo cruzó el camino."],
                            ["el gancho", "hook", "Colgó el abrigo de un gancho."],
                            ["el grosor", "thickness", "Midió el grosor de la pared."],
                            ["la hormiga", "ant", "La hormiga llevaba una carga enorme."],
                            ["el lodo", "mud", "Caminamos sobre el lodo."],
                            ["el marfil", "ivory", "El piano tenía teclas de marfil."],
                            ["el molde", "mold", "Vertió la mezcla en el molde."],
                            ["la rebanada", "slice", "Pidió una rebanada de pan."],
                            ["la senda", "path", "Seguimos una senda estrecha."],
                            ["el terciopelo", "velvet", "La cortina era de terciopelo."],
                            ["la estela", "wake, trail", "El barco dejó una estela blanca."],
                            ["la punta de lanza", "spearhead", "Fue la punta de lanza del movimiento."]],
                           say=[0, 2])]),
        card("Words you already know in new roles",
             "El rasgo means a characteristic or feature. La sierra can mean a mountain range or a saw. El fantasma means ghost, and in a figurative sense it can mean a lingering fear.",
             examples=[
                 ex("Un rasgo de su estilo es la sencillez.", "One feature of her style is simplicity.", "rasgo"),
                 ex("La sierra estaba cubierta de nieve.", "The mountain range was covered in snow.", "sierra"),
             ]),
    ],
    exercises=[
        M("What is a “rasgo”?", "A characteristic or feature", ["A kind of path", "A kind of fabric", "A kind of animal"], "Rasgo."),
        M("What is a “ciervo”?", "A deer", ["A rooster", "An ant", "A torch"], "Ciervo."),
        M("What does “punta de lanza” mean figuratively?", "A leading, innovative force", ["A weak ending", "A kind of food", "A broken tool"], "Spearhead."),
        F("El camino por el bosque era una ___ estrecha.", "senda", ["rebanada", "hormiga", "estela"], "A path.", tr="The way through the forest was a narrow path."),
        F("Pidió una ___ de pan con queso.", "rebanada", ["senda", "antorcha", "estela"], "A slice.", tr="He asked for a slice of bread with cheese."),
        F("La ___ llevaba una carga mucho más grande que ella.", "hormiga", ["antorcha", "cabaña", "senda"], "An ant.", tr="The ant was carrying a load much bigger than itself."),
        F("Después de la lluvia, caminamos sobre el ___.", "lodo", ["terciopelo", "marfil", "gancho"], "Mud.", tr="After the rain we walked on the mud."),
        F("La cortina era de ___ rojo, suave y pesado.", "terciopelo", ["lodo", "marfil", "grosor"], "Velvet.", tr="The curtain was made of red velvet, soft and heavy."),
        F("Entramos a la cueva con una ___.", "antorcha", ["hormiga", "rebanada", "cabaña"], "A torch.", tr="We entered the cave with a torch."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 855
L855 = lesson(
    "Aphorisms: short sentences with big ideas (invented practice sayings)",
    "Un libro abierto es una puerta sin llave. Las palabras son semillas.",
    requires=["libro", "puerta", "llave", "palabra", "viajar", "mover", "aprender", "nadar", "río", "biblioteca", "vacío", "silencio"],
    cards=[
        card("Five sayings",
             "An aphorism is a short sentence that expresses a general idea. The sayings below were written for this course. They are not famous quotations. Read each aloud and then read its meaning.",
             tables=[table(["Refrán inventado", "Idea"],
                           [["Un libro abierto es una puerta sin llave.", "A book gives access to anyone who opens it."],
                            ["Quien lee mucho viaja sin moverse.", "Reading takes you to many places."],
                            ["Las palabras son semillas: algunas tardan en crecer.", "Words may take time to have an effect."],
                            ["Una biblioteca vacía es un pueblo en silencio.", "Libraries are alive when people use them."],
                            ["No se aprende a nadar mirando el río.", "You learn by doing, not only by watching."]],
                           say=[0])]),
        card("Grammar inside the sayings",
             "Quien (“whoever”) takes a singular verb. Se aprende is an impersonal se. Notice that mirando is a gerund and that abierto and vacía agree with their nouns.",
             examples=[
                 ex("Quien lee mucho viaja sin moverse.", "Whoever reads a lot travels without moving.", "viaja"),
                 ex("No se aprende a nadar mirando el río.", "One does not learn to swim by looking at the river.", "mirando"),
             ]),
    ],
    exercises=[
        M("What is an aphorism?", "A short sentence that expresses a general idea", ["A long novel", "A kind of dictionary", "A type of poem with rhyme only"], "Short and general."),
        M("What does “No se aprende a nadar mirando el río” mean?", "You learn by doing, not only by watching", ["Rivers are dangerous", "Swimming is forbidden", "Teachers should be silent"], "Learning by doing."),
        M("What does “Las palabras son semillas” suggest?", "Words may take time to have an effect", ["Words are food", "Words cannot be planted", "Words are always short"], "Seeds grow slowly."),
        F("Quien lee mucho ___ sin moverse.", "viaja", ["viajan", "viajamos", "viajas"], "Quien → singular.", tr="Whoever reads a lot travels without moving.", lemma="viajar:él"),
        F("Las palabras ___ semillas.", "son", ["es", "somos", "eres"], "Plural subject.", tr="Words are seeds.", lemma="ser:ellos"),
        F("Algunas palabras ___ en crecer.", "tardan", ["tarda", "tardamos", "tardas"], "Plural subject.", tr="Some words take a long time to grow.", lemma="tardar:ellos"),
        F("No se aprende a nadar ___ el río.", "mirando", ["mirar", "mirado", "miró"], "Gerund: by looking.", tr="One does not learn to swim by looking at the river.", lemma="mirar:ger"),
        F("Un libro ___ es una puerta sin llave.", "abierto", ["abrido", "abriendo", "abrió"], "Participle used as an adjective.", tr="An open book is a door without a key.", lemma="abrir:part"),
        F("Una biblioteca ___ es un pueblo en silencio.", "vacía", ["vacío", "vacíos", "vacías"], "Feminine singular.", tr="An empty library is a town in silence."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 856
L856 = lesson(
    "Como si + imperfect subjunctive: Habla como si fuera el jefe",
    "Camina como si tuviera prisa. Me mira como si no me conociera.",
    requires=["jefe", "prisa", "conocer", "saber", "tener", "ser", "hablar", "caminar", "mirar", "miedo", "amigo", "correr"],
    cards=[
        card("As if…",
             "Como si means “as if” or “as though.” It introduces a comparison with something imaginary or doubtful. After como si, use the subjunctive: the imperfect subjunctive for something happening at the same time as the main verb (whether the main verb is in the present or the past), and the pluperfect subjunctive for something earlier (see the next lesson).",
             tables=[table(["Verbo principal", "como si", "Subjuntivo imperfecto"],
                           [["Habla", "como si", "fuera el jefe."],
                            ["Camina", "como si", "tuviera prisa."],
                            ["Me mira", "como si", "no me conociera."],
                            ["Hablas", "como si", "lo supieras todo."],
                            ["Corren", "como si", "tuvieran miedo."]],
                           say=[0, 2])]),
        card("Notes",
             "In this meaning, do not use the present indicative or the conditional after como si. The subject of the como si-clause can be the same as the main subject or different. Como si is always written as two words.",
             examples=[
                 ex("Nos tratan como si fuéramos amigos de siempre.", "They treat us as if we were old friends.", "como si fuéramos"),
                 ex("Habla como si fuera el jefe.", "He talks as if he were the boss.", "como si fuera"),
             ]),
    ],
    exercises=[
        M("Which tense follows “como si” for something happening at the same time as the main verb?", "The imperfect subjunctive", ["The present subjunctive", "The future", "The conditional"], "Como si + imperfect subjunctive."),
        M("What does “Habla como si fuera el jefe” suggest?", "He may not really be the boss", ["He is certainly the boss", "He will be the boss", "He was the boss"], "As if = not necessarily true."),
        M("Can the main verb be in the past?", "Yes, and the como si verb stays in the imperfect subjunctive", ["No, only the present", "Yes, but then use the future", "No, only the infinitive"], "Same pattern."),
        F("Habla como si ___ el jefe.", "fuera", ["es", "será", "sería"], "Imperfect subjunctive of ser.", tr="He talks as if he were the boss.", lemma="ser:él:isubj"),
        F("Camina como si ___ prisa.", "tuviera", ["tiene", "tendrá", "tendría"], "Imperfect subjunctive of tener.", tr="She walks as if she were in a hurry.", lemma="tener:él:isubj"),
        F("Me mira como si no me ___.", "conociera", ["conoce", "conocerá", "conocería"], "Imperfect subjunctive.", tr="He looks at me as if he did not know me.", lemma="conocer:él:isubj"),
        F("Ellos corren como si ___ miedo.", "tuvieran", ["tienen", "tendrán", "tendrían"], "Plural subject.", tr="They run as if they were afraid.", lemma="tener:ellos:isubj"),
        F("Hablas como si lo ___ todo.", "supieras", ["sabes", "sabrás", "sabrías"], "Tú form.", tr="You talk as if you knew everything.", lemma="saber:tú:isubj"),
        F("Nos tratan como si ___ amigos de siempre.", "fuéramos", ["somos", "seremos", "seríamos"], "Nosotros form.", tr="They treat us as if we were old friends.", lemma="ser:nosotros:isubj"),
    ],
    verify=vpq("ser", "fuera", "fueras", "fuera", "fuéramos", "fuerais", "fueran") + vpq("tener", "tuviera", "tuvieras", "tuviera", "tuviéramos", "tuvierais", "tuvieran") + vpq("saber", "supiera", "supieras", "supiera", "supiéramos", "supierais", "supieran"),
)

# ---------------------------------------------------------------------------- 857
L857 = lesson(
    "Como si + pluperfect subjunctive: como si nada hubiera pasado",
    "Se comportó como si nada hubiera pasado. Habla como si hubiera vivido allí.",
    requires=["pasar", "vivir", "ganar", "perder", "tren", "partido", "premio", "nada", "comportar", "visto", "nunca", "todo"],
    cards=[
        card("Comparing with something earlier",
             "When the imagined situation comes before the main verb, use como si + the pluperfect subjunctive (hubiera + participle). "
             "If the imagined situation happens at the same time, use the imperfect subjunctive.",
             tables=[table(["Mismo tiempo", "Antes"],
                           [["Habla como si viviera allí.", "Habla como si hubiera vivido allí."],
                            ["Sonríe como si ganara el premio.", "Sonríe como si hubiera ganado el premio."],
                            ["Actúas como si no me vieras.", "Actúas como si no me hubieras visto nunca."]],
                           say=[0, 1])]),
        card("Common frame",
             "Como si nada (hubiera pasado) is a fixed way to say that somebody acted as if nothing had happened.",
             examples=[
                 ex("Se comportó como si nada hubiera pasado.", "He behaved as if nothing had happened.", "como si nada hubiera pasado"),
                 ex("Corrimos como si hubiéramos perdido el tren.", "We ran as if we had missed the train.", "como si hubiéramos perdido"),
             ]),
    ],
    exercises=[
        M("Which sentence compares to a situation BEFORE the main action?", "Habla como si hubiera vivido en Chile.", ["Habla como si viviera en Chile.", "Habla como si vive en Chile.", "Habla como si vivirá en Chile."], "Hubiera + participle."),
        M("What does “Se comportó como si nada hubiera pasado” mean?", "He acted as if nothing had happened", ["He caused an accident", "He will act calmly", "He forgot his name"], "As if nothing had happened."),
        M("Which form is used for an imagined situation that is earlier than the main verb?", "The pluperfect subjunctive", ["The imperfect subjunctive", "The present indicative", "The future"], "Earlier → pluperfect."),
        F("Se comportó como si nada ___ pasado.", "hubiera", ["había", "habría", "ha"], "Hubiera + participle.", tr="He behaved as if nothing had happened.", lemma="haber:él:isubj"),
        F("Hablaba como si ya ___ vivido allí toda la vida.", "hubiera", ["había", "habría", "ha"], "Hubiera + participle.", tr="He spoke as if he had already lived there his whole life.", lemma="haber:él:isubj"),
        F("Ellos hablaban como si ya ___ ganado el partido.", "hubieran", ["habían", "habrían", "han"], "Plural subject.", tr="They talked as if they had already won the game.", lemma="haber:ellos:isubj"),
        F("Actúas como si no me ___ visto nunca.", "hubieras", ["habías", "habrías", "has"], "Tú form.", tr="You act as if you had never seen me.", lemma="haber:tú:isubj"),
        F("Corrimos como si ___ perdido el tren.", "hubiéramos", ["habíamos", "habríamos", "hemos"], "Nosotros form.", tr="We ran as if we had missed the train.", lemma="haber:nosotros:isubj"),
        F("Sonríe como si hubiera ___ el premio.", "ganado", ["ganar", "ganando", "ganó"], "Participle of ganar.", tr="She smiles as if she had won the prize.", lemma="ganar:part"),
    ],
    verify=vpq("haber", "hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran"),
)

# ---------------------------------------------------------------------------- 858
L858 = lesson(
    "Ojalá: hope and impossible wishes",
    "Ojalá llueva hoy. Ojalá pudiera volar.",
    requires=["llover", "poder", "volar", "tener", "tiempo", "llegar", "vivir", "cerca", "playa", "ganar", "partido", "planta"],
    cards=[
        card("Two kinds of ojalá",
             "Ojalá means “I hope” or “I wish.” It always takes the subjunctive. With the present subjunctive it expresses a hope that could come true. "
             "With the imperfect subjunctive it expresses a wish for something unlikely or impossible now. Que after ojalá is optional.",
             tables=[table(["Ojalá + presente", "Ojalá + imperfecto"],
                           [["Ojalá llueva hoy.", "Ojalá lloviera todos los días."],
                            ["Ojalá llegues pronto.", "Ojalá viviéramos cerca de la playa."],
                            ["Ojalá puedan ganar.", "Ojalá pudiera volar."],
                            ["Ojalá tenga tiempo.", "Ojalá tuviera más tiempo libre."]],
                           say=[0, 1])]),
        card("Translating",
             "In English the first group sounds like “I hope.” The second group sounds like “I wish.” The speaker uses the imperfect subjunctive to show distance from reality.",
             examples=[
                 ex("Ojalá llueva hoy; las plantas están secas.", "I hope it rains today; the plants are dry.", "llueva"),
                 ex("Ojalá pudiera volar.", "I wish I could fly.", "pudiera"),
             ]),
    ],
    exercises=[
        M("Which sentence expresses a wish that seems impossible?", "Ojalá pudiera volar.", ["Ojalá pueda venir mañana.", "Ojalá llueva hoy.", "Ojalá llegues pronto."], "Imperfect subjunctive."),
        M("What mood follows ojalá?", "Always the subjunctive", ["Always the indicative", "Always the infinitive", "Always the future"], "Ojalá + subjunctive."),
        M("How do you say “I wish I had more time” (now)?", "Ojalá tuviera más tiempo.", ["Ojalá tengo más tiempo.", "Ojalá tendría más tiempo.", "Ojalá tenía más tiempo."], "Imperfect subjunctive."),
        F("Ojalá ___ hoy; las plantas están secas.", "llueva", ["llueve", "lloverá", "llovería"], "Present subjunctive.", tr="I hope it rains today; the plants are dry.", lemma="llover:él:subj"),
        F("Ojalá ___ volar.", "pudiera", ["puedo", "podré", "podría"], "Imperfect subjunctive.", tr="I wish I could fly.", lemma="poder:yo:isubj"),
        F("Ojalá ___ más tiempo libre.", "tuviera", ["tengo", "tendré", "tendría"], "Imperfect subjunctive.", tr="I wish I had more free time.", lemma="tener:yo:isubj"),
        F("Ojalá tú ___ pronto.", "llegues", ["llegas", "llegarás", "llegarías"], "Present subjunctive.", tr="I hope you arrive soon.", lemma="llegar:tú:subj"),
        F("Ojalá nosotros ___ vivir cerca de la playa.", "pudiéramos", ["podemos", "podremos", "podríamos"], "Imperfect subjunctive.", tr="I wish we could live near the beach.", lemma="poder:nosotros:isubj"),
        F("Ojalá ellos ___ ganar el partido.", "puedan", ["pueden", "podrán", "podrían"], "Present subjunctive.", tr="I hope they can win the game.", lemma="poder:ellos:subj"),
    ],
    verify=vpj("poder", "pueda", "puedas", "pueda", "podamos", "podáis", "puedan") + vpq("poder", "pudiera", "pudieras", "pudiera", "pudiéramos", "pudierais", "pudieran"),
)

# ---------------------------------------------------------------------------- 859
L859 = lesson(
    "Ojalá + pluperfect subjunctive: regrets about the past",
    "Ojalá hubiera estudiado más. Ojalá hubieras venido a la fiesta.",
    requires=["estudiar", "venir", "llegar", "llover", "saber", "llamar", "hablar", "fiesta", "tiempo", "verdad", "antes", "tanto"],
    cards=[
        card("I wish it had been different",
             "To wish that the past had been different, use ojalá + the pluperfect subjunctive (hubiera + participle). It expresses regret, and it cannot be changed.",
             tables=[table(["Ojalá + hubiera + participio", "English"],
                           [["Ojalá hubiera estudiado más.", "I wish I had studied more."],
                            ["Ojalá hubieras venido a la fiesta.", "I wish you had come to the party."],
                            ["Ojalá hubieran llegado a tiempo.", "I wish they had arrived on time."],
                            ["Ojalá no hubiera llovido tanto.", "I wish it had not rained so much."]],
                           say=[0])]),
        card("What not to say",
             "Do not use habría after ojalá. Do not use the indicative either. Hubiera (or hubiese) is the only normal choice.",
             examples=[
                 ex("Ojalá hubiéramos sabido la verdad antes.", "I wish we had known the truth earlier.", "hubiéramos sabido"),
                 ex("Ojalá ella me hubiera llamado antes.", "I wish she had called me earlier.", "hubiera llamado"),
             ]),
    ],
    exercises=[
        M("What does “Ojalá hubiera estudiado más” express?", "A regret about the past", ["A plan for tomorrow", "A polite request", "A fact"], "Past regret."),
        M("Which form follows ojalá for a wish about the past?", "The pluperfect subjunctive", ["The conditional perfect", "The preterite", "The future"], "Hubiera + participle."),
        M("Can we say “Ojalá habría estudiado más”?", "No, it is not correct", ["Yes, always", "Only in questions", "Only with ser"], "Use hubiera."),
        F("Ojalá yo ___ estudiado más.", "hubiera", ["había", "habría", "he"], "Hubiera + participle.", tr="I wish I had studied more.", lemma="haber:yo:isubj"),
        F("Ojalá tú ___ venido a la fiesta.", "hubieras", ["habías", "habrías", "has"], "Tú form.", tr="I wish you had come to the party.", lemma="haber:tú:isubj"),
        F("Ojalá ellos ___ llegado a tiempo.", "hubieran", ["habían", "habrían", "han"], "Plural subject.", tr="I wish they had arrived on time.", lemma="haber:ellos:isubj"),
        F("Ojalá no ___ llovido tanto.", "hubiera", ["había", "habría", "ha"], "Singular, impersonal.", tr="I wish it had not rained so much.", lemma="haber:él:isubj"),
        F("Ojalá nosotros hubiéramos ___ la verdad.", "sabido", ["saber", "sabiendo", "supimos"], "Participle of saber.", tr="I wish we had known the truth.", lemma="saber:part"),
        F("Ojalá ella me hubiera ___ antes.", "llamado", ["llamar", "llamando", "llamó"], "Participle of llamar.", tr="I wish she had called me earlier.", lemma="llamar:part"),
    ],
    verify=vpq("haber", "hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran"),
)

# ---------------------------------------------------------------------------- 860
L860 = lesson(
    "Quisiera: politeness and wishes",
    "Quisiera un café. Quisiera viajar. Quisiera que me ayudaras.",
    requires=["querer", "café", "mesa", "viajar", "ayudar", "estudiar", "llegar", "hermano", "temprano", "trabajo", "ayuda", "tomar"],
    cards=[
        card("A softer way to say “I want”",
             "Quisiera is the imperfect subjunctive of querer (-ra form). It sounds more polite than quiero. You will hear it in restaurants, shops and offices. "
             "It can also express a wish about what you would like to do or see happen.",
             tables=[table(["Persona", "quisiera"],
                           [["yo", "quisiera"], ["tú", "quisieras"], ["él / ella / usted", "quisiera"],
                            ["nosotros", "quisiéramos"], ["vosotros", "quisierais"], ["ellos / ustedes", "quisieran"]],
                           say=[1])]),
        card("Same subject or different subject?",
             "If the subject is the same in both clauses, use quisiera + infinitive. If the subjects are different, use quisiera que + the imperfect subjunctive.",
             tables=[table(["Patrón", "Ejemplo"],
                           [["quisiera + infinitivo", "Quisiera viajar a Madrid el próximo año."],
                            ["quisiera que + subjuntivo imperfecto", "Quisiera que mi hermano estudiara más."],
                            ["pedir cortésmente", "Quisiéramos una mesa para dos, por favor."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which is more polite?", "Quisiera un café.", ["Quiero un café.", "Dame un café.", "Un café ya."], "Quisiera softens the request."),
        M("When both subjects are the same, what follows quisiera?", "An infinitive", ["que + infinitive", "A gerund", "A participle"], "Quisiera viajar."),
        M("When the subjects are different, what pattern is used?", "quisiera que + imperfect subjunctive", ["quisiera + infinitive", "quisiera + gerund", "quisiera + participle"], "Different subjects → que."),
        F("Quisiera ___ a Madrid el próximo año.", "viajar", ["viaje", "viajara", "viajo"], "Same subject → infinitive.", tr="I would like to travel to Madrid next year."),
        F("Quisiera que mi hermano ___ más.", "estudiara", ["estudiar", "estudio", "estudie"], "Different subject → imperfect subjunctive.", tr="I would like my brother to study more.", lemma="estudiar:él:isubj"),
        F("Nosotros ___ una mesa para dos, por favor.", "quisiéramos", ["quisieran", "quisiera", "quisierais"], "Nosotros form.", tr="We would like a table for two, please.", lemma="querer:nosotros:isubj"),
        F("Ella quisiera que ellos ___ más temprano.", "llegaran", ["llegar", "llegan", "lleguen"], "Different subject.", tr="She would like them to arrive earlier.", lemma="llegar:ellos:isubj"),
        F("¿Qué ___ usted tomar?", "quisiera", ["quisieran", "quisieras", "quisiéramos"], "Usted form.", tr="What would you like to have?", lemma="querer:usted:isubj"),
        F("Quisiera que tú me ___ con este trabajo.", "ayudaras", ["ayudar", "ayudas", "ayudes"], "Tú form.", tr="I would like you to help me with this job.", lemma="ayudar:tú:isubj"),
    ],
    verify=vpq("querer", "quisiera", "quisieras", "quisiera", "quisiéramos", "quisierais", "quisieran"),
)

# ---------------------------------------------------------------------------- 861
L861 = lesson(
    "Wishes and regrets: ojalá, quisiera, me gustaría que",
    "Ojalá venga. Ojalá estuviera aquí. Ojalá hubiera venido. Quisiera que fuera más fácil.",
    requires=["gustar", "venir", "estar", "ser", "hacer", "hablar", "perder", "tren", "examen", "tiempo", "hermana", "reunión"],
    cards=[
        card("Choosing the right form",
             "Match the verb form to the type of wish. A hope that is likely uses the present subjunctive. A wish about an unlikely present situation uses the imperfect subjunctive. "
             "A regret about the past uses the pluperfect subjunctive. A polite wish or a wish about another person uses quisiera or me gustaría que + imperfect subjunctive.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["Esperanza posible", "Ojalá haga buen tiempo mañana."],
                            ["Deseo irreal (ahora)", "Ojalá mi hermana estuviera aquí con nosotros."],
                            ["Pesar (pasado)", "Ojalá no hubiéramos perdido el tren."],
                            ["Deseo sobre otra persona", "Me gustaría que ellos vinieran con nosotros."],
                            ["Deseo cortés, sobre una situación", "Quisiera que el examen fuera más fácil."]],
                           say=[1])]),
        card("A quick check",
             "Ask yourself: Is it possible or likely? Is it about now or about the past? Is it about me or about someone else? The answers choose the form.",
             examples=[
                 ex("Ojalá tengamos una buena reunión.", "I hope we have a good meeting.", "tengamos"),
                 ex("Ojalá hubiéramos hablado más antes de la reunión.", "I wish we had talked more before the meeting.", "hubiéramos hablado"),
             ]),
    ],
    exercises=[
        M("Which sentence expresses regret about the past?", "Ojalá hubiera ido.", ["Ojalá vaya.", "Ojalá fuera.", "Quisiera ir."], "Hubiera + participle."),
        M("Which sentence expresses an unlikely present wish?", "Ojalá viviera aquí.", ["Ojalá viva aquí.", "Ojalá hubiera vivido aquí.", "Ojalá vivirá aquí."], "Imperfect subjunctive."),
        M("Which sentence is a polite wish?", "Quisiera hablar con usted.", ["Ojalá hubiera hablado.", "Ojalá hablara.", "Hablo con usted."], "Quisiera + infinitive."),
        F("Ojalá mi hermana ___ aquí con nosotros.", "estuviera", ["está", "estará", "estaría"], "Imperfect subjunctive.", tr="I wish my sister were here with us.", lemma="estar:ella:isubj"),
        F("Ojalá ___ buen tiempo mañana.", "haga", ["hace", "hará", "haría"], "Present subjunctive.", tr="I hope the weather is good tomorrow.", lemma="hacer:él:subj"),
        F("Ojalá no ___ perdido el tren.", "hubiéramos", ["habíamos", "habríamos", "hemos"], "Pluperfect subjunctive.", tr="I wish we had not missed the train.", lemma="haber:nosotros:isubj"),
        F("Me gustaría que ellos ___ con nosotros.", "vinieran", ["vienen", "vendrán", "vengan"], "Imperfect subjunctive.", tr="I would like them to come with us.", lemma="venir:ellos:isubj"),
        F("Ojalá hubiéramos ___ más antes de la reunión.", "hablado", ["hablar", "hablando", "habló"], "Participle of hablar.", tr="I wish we had talked more before the meeting.", lemma="hablar:part"),
        F("Quisiera que el examen ___ más fácil.", "fuera", ["es", "será", "sería"], "Imperfect subjunctive.", tr="I would like the exam to be easier.", lemma="ser:él:isubj"),
    ],
    verify=vpq("estar", "estuviera", "estuvieras", "estuviera", "estuviéramos", "estuvierais", "estuvieran") + vpq("venir", "viniera", "vinieras", "viniera", "viniéramos", "vinierais", "vinieran"),
)

# ---------------------------------------------------------------------------- 862
L862 = lesson(
    "Review: the pluperfect subjunctive in si, ojalá and como si",
    "Si hubiera ido… Ojalá hubiera ido… Habló como si hubiera ido…",
    requires=["haber", "ir", "saber", "decir", "salir", "ganar", "comer", "escribir", "ver", "llegar", "hacer", "volver"],
    cards=[
        card("Three triggers, one form",
             "The pluperfect subjunctive (hubiera / hubiese + participle) appears after si, ojalá and como si when the situation is imagined and in the past. It always has the same shape.",
             tables=[table(["Desencadenante", "Ejemplo", "English"],
                           [["si + hubiera", "Si hubiera salido antes, habría llegado.", "If I had left earlier, I would have arrived."],
                            ["ojalá + hubiera", "Ojalá hubiera salido antes.", "I wish I had left earlier."],
                            ["como si + hubiera", "Habla como si hubiera salido antes.", "He talks as if he had left earlier."]],
                           say=[1])]),
        card("What to remember",
             "In the main clause after a si-clause, use the conditional perfect (habría + participle); in speech hubiera + participle is also possible. After ojalá and como si there is no conditional. The participles are the same as in the other perfect tenses: hecho, dicho, escrito, visto, vuelto.",
             examples=[
                 ex("Si hubiéramos vuelto antes, habríamos visto la película.", "If we had come back earlier, we would have seen the movie.", "hubiéramos vuelto"),
             ]),
    ],
    exercises=[
        M("Which word can introduce a past wish with the pluperfect subjunctive?", "ojalá", ["pero", "porque", "cuando siempre"], "Ojalá."),
        M("What completes “Si hubiera salido antes, ___ a tiempo ayer”?", "habría llegado", ["llegaría", "llegué", "hubiera llega"], "Conditional perfect."),
        M("What is the participle of “escribir”?", "escrito", ["escribido", "escribiendo", "escribí"], "Escrito."),
        F("Si tú ___ dicho la verdad, habríamos ayudado.", "hubieras", ["habías", "habrías", "has"], "Tú form.", tr="If you had told the truth, we would have helped.", lemma="haber:tú:isubj"),
        F("Ojalá ellos ___ ganado el partido.", "hubieran", ["habían", "habrían", "han"], "Plural subject.", tr="I wish they had won the game.", lemma="haber:ellos:isubj"),
        F("Habla como si lo ___ visto todo.", "hubiera", ["había", "habría", "ha"], "Singular subject.", tr="He talks as if he had seen everything.", lemma="haber:él:isubj"),
        F("Si nosotros ___ vuelto antes, habríamos visto la película.", "hubiéramos", ["habíamos", "habríamos", "hemos"], "Nosotros form.", tr="If we had come back earlier, we would have seen the movie.", lemma="haber:nosotros:isubj"),
        F("Ojalá yo hubiera ___ la carta antes.", "escrito", ["escribir", "escribiendo", "escribí"], "Participle of escribir.", tr="I wish I had written the letter earlier.", lemma="escribir:part"),
        F("Si ella hubiese ___ más, habría aprendido más.", "leído", ["leer", "leyendo", "leyó"], "Participle of leer.", tr="If she had read more, she would have learned more.", lemma="leer:part"),
    ],
    verify=vpq("haber", "hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran") + vpa("volver", "vuelto") + vpa("leer", "leído"),
)

# ---------------------------------------------------------------------------- 863
L863 = lesson(
    "Reading: el club de lectura (invented text)",
    "Marta habló como si hubiera vivido en el pueblo de la novela.",
    requires=["leer", "club", "novela", "pueblo", "amigo", "semana", "trabajar", "tiempo", "discusión", "entender", "reunir", "libro"],
    cards=[
        card("Texto inventado, primera parte",
             "This short text is invented for practice. Look for como si, ojalá, quisiera and the si-patterns.",
             examples=[
                 ex("Marta lee mucho. El sábado pasado fue a su club de lectura y todos hablaron de una novela corta.", "Marta reads a lot. Last Saturday she went to her reading club and everyone talked about a short novel.", "fue"),
                 ex("Marta habló como si hubiera vivido en el pueblo de la historia.", "Marta spoke as if she had lived in the town of the story.", "como si hubiera vivido"),
                 ex("Un amigo dijo: Ojalá hubiera leído el libro antes.", "A friend said: I wish I had read the book earlier.", "Ojalá hubiera leído"),
                 ex("Si lo hubiera leído, habría entendido mejor la discusión.", "If he had read it, he would have understood the discussion better.", "habría entendido"),
             ]),
        card("Texto inventado, segunda parte",
             "Marta has her own wishes.",
             examples=[
                 ex("Marta quisiera que el club se reuniera todas las semanas.", "Marta would like the club to meet every week.", "quisiera que"),
                 ex("Ojalá Marta tuviera más tiempo para leer, pero trabaja mucho.", "I wish Marta had more time to read, but she works a lot.", "tuviera"),
                 ex("Si tuviera más tiempo, leería un libro por semana.", "If she had more time, she would read a book a week.", "leería"),
             ]),
    ],
    exercises=[
        M("What did Marta do last Saturday?", "She went to her reading club", ["She traveled to a town", "She wrote a novel", "She missed a class"], "Fue a su club de lectura."),
        M("What did the friend regret?", "Not reading the book earlier", ["Missing the train", "Losing the book", "Not meeting Marta"], "Ojalá hubiera leído el libro antes."),
        M("What would Marta like?", "The club to meet every week", ["To change jobs", "To move to the town", "To write a review"], "Quisiera que…"),
        M("Why can't Marta read a book each week?", "She works a lot and has little time", ["The books are too long", "She dislikes novels", "The club forbids it"], "Trabaja mucho."),
        F("Marta habló como si ___ vivido en el pueblo de la historia.", "hubiera", ["había", "habría", "ha"], "Como si + hubiera.", tr="Marta spoke as if she had lived in the town of the story.", lemma="haber:ella:isubj"),
        F("Ojalá ___ leído el libro antes.", "hubiera", ["había", "habría", "he"], "Ojalá + hubiera.", tr="I wish I had read the book earlier.", lemma="haber:yo:isubj"),
        F("Si lo hubiera leído, ___ entendido mejor la discusión.", "habría", ["habían", "había", "hubo"], "Conditional perfect.", tr="If he had read it, he would have understood the discussion better.", lemma="haber:él:cond"),
        F("Marta quisiera que el club se ___ todas las semanas.", "reuniera", ["reunir", "reúne", "reúna"], "Imperfect subjunctive.", tr="Marta would like the club to meet every week.", lemma="reunir:él:isubj"),
        F("Si tuviera más tiempo, ___ un libro por semana.", "leería", ["leyó", "lee", "leerá"], "Simple conditional.", tr="If she had more time, she would read a book a week.", lemma="leer:ella:cond"),
    ],
    verify=vpq("reunir", "reuniera", "reunieras", "reuniera", "reuniéramos", "reunierais", "reunieran") + vpd("leer", "leería", "leerías", "leería", "leeríamos", "leeríais", "leerían"),
)
UNIT = unit("Autores influyentes", [L836, L837, L838, L839, L840, L841, L842, L843, L844, L845, L846, L847, L848, L849, L850, L851, L852, L853, L854, L855, L856, L857, L858, L859, L860, L861, L862, L863])

"""Unit 38: art and literature (textbook Chapter 38): the fine arts, vocabulary of painting, literature, film and music, Don Quijote, La vida es sueño, the film Roma, Botero, Violeta Parra, proverbs; the conditional perfect and si-clauses with the pluperfect subjunctive. All texts are original descriptions; no passages or lyrics are quoted."""
from dsl_es import *

# ---------------------------------------------------------------------------- 808
L808 = lesson(
    "The fine arts: pintura, escultura, arquitectura, música…",
    "Un pintor hace cuadros; un escultor trabaja con piedra, madera o metal.",
    requires=["arte", "pintura", "arquitectura", "música", "literatura", "danza", "teatro", "cine", "museo", "color", "estilo", "obra"],
    cards=[
        card("Eight kinds of art",
             "Las bellas artes (fine arts) are creative activities that express beauty or ideas. Traditions differ on which ones to include, but these eight are common. Cinema is often called “el séptimo arte” (the seventh art) because, in the traditional count of the arts, it came after the six older ones.",
             tables=[table(["Arte", "English", "Ejemplo"],
                           [["la pintura", "painting", "Un pintor usa colores para hacer un cuadro."],
                            ["la escultura", "sculpture", "Un escultor trabaja con piedra, madera o metal."],
                            ["la arquitectura", "architecture", "Un arquitecto diseña edificios, puentes y plazas."],
                            ["la música", "music", "La música combina sonidos y ritmo."],
                            ["la literatura", "literature", "La literatura incluye novelas, cuentos y poemas."],
                            ["la danza", "dance", "La danza expresa ideas con el movimiento del cuerpo."],
                            ["el teatro", "theater", "En el teatro, los actores presentan una obra en un escenario."],
                            ["el cine", "film", "El cine cuenta historias con imágenes y sonido."]],
                           say=[2])]),
    ],
    exercises=[
        M("Which art uses sound and rhythm?", "La música", ["La pintura", "La escultura", "La arquitectura"], "Música."),
        M("Who designs buildings and bridges?", "Un arquitecto", ["Un escultor", "Un bailarín", "Un poeta"], "Arquitecto."),
        M("What is “el séptimo arte”?", "Cinema", ["Dance", "Painting", "Music"], "El séptimo arte = cine."),
        F("Un pintor usa colores para hacer un ___.", "cuadro", ["edificio", "poema", "baile"], "Painting.", tr="A painter uses colors to make a painting."),
        F("Un escultor trabaja con piedra, madera o ___.", "metal", ["tinta", "música", "teatro"], "Sculpture materials.", tr="A sculptor works with stone, wood or metal."),
        F("La ___ incluye novelas, cuentos y poemas.", "literatura", ["arquitectura", "danza", "escultura"], "Literature.", tr="Literature includes novels, stories and poems."),
        F("En el teatro, los actores presentan una ___ en un escenario.", "obra", ["escultura", "tinta", "plaza"], "Play.", tr="In the theater, the actors present a play on a stage."),
        F("La ___ expresa ideas con el movimiento del cuerpo.", "danza", ["literatura", "escultura", "arquitectura"], "Dance.", tr="Dance expresses ideas with the movement of the body."),
        F("Muchos turistas visitan el ___ para ver pinturas famosas.", "museo", ["metal", "ritmo", "tinta"], "Museum.", tr="Many tourists visit the museum to see famous paintings."),
    ],
)

# ---------------------------------------------------------------------------- 809
L809 = lesson(
    "Visual arts: cuadro, lienzo, óleo, pincel, retrato, mural",
    "Un pintor usa un pincel y óleo para pintar un retrato sobre un lienzo.",
    requires=["cuadro", "retrato", "museo", "galería", "exposición", "color", "pintor", "pintura", "escultura", "obra", "tejido", "arte"],
    cards=[
        card("Words for painting and sculpture",
             "Note that cuadro can mean a painting, a picture or a square, depending on the context.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el cuadro", "painting, picture", "Ese cuadro está en el museo."],
                            ["el lienzo", "canvas", "El pintor trabaja sobre un lienzo grande."],
                            ["el óleo", "oil paint", "Muchos artistas pintan al óleo."],
                            ["el pincel", "paintbrush", "El pintor usa un pincel fino."],
                            ["el retrato", "portrait", "El retrato muestra la cara de una persona."],
                            ["el mural", "mural", "Un mural es una pintura grande sobre una pared."],
                            ["el escultor", "sculptor", "El escultor hizo una estatua de piedra."],
                            ["la obra maestra", "masterpiece", "Esa obra maestra tiene mucho valor."],
                            ["el tapiz", "tapestry", "Un tapiz es una tela decorada con dibujos."],
                            ["la artesanía", "handicrafts", "La artesanía incluye tejidos y objetos hechos a mano."],
                            ["la exposición", "exhibit", "La exposición abre el sábado en la galería."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “un lienzo”?", "A canvas", ["A brush", "A mural", "A museum"], "Lienzo."),
        M("What is “un mural”?", "A large painting on a wall", ["A small portrait", "A sculpture of wood", "A kind of paint"], "Mural."),
        M("What is “la artesanía”?", "Handicrafts", ["Architecture", "A kind of music", "A museum"], "Artesanía."),
        F("El pintor trabaja sobre un ___ grande.", "lienzo", ["pincel", "tapiz", "óleo"], "Canvas.", tr="The painter works on a large canvas.", ),
        F("El ___ muestra la cara de una persona.", "retrato", ["mural", "tapiz", "pincel"], "Portrait.", tr="The portrait shows a person’s face.", ),
        F("El pintor usa un ___ fino.", "pincel", ["lienzo", "mural", "museo"], "Brush.", tr="The painter uses a fine brush."),
        F("Un ___ es una pintura grande sobre una pared.", "mural", ["retrato", "pincel", "óleo"], "Mural.", tr="A mural is a large painting on a wall."),
        F("La ___ abre el sábado en la galería.", "exposición", ["artesanía", "obra maestra", "escultor"], "Exhibit.", tr="The exhibit opens Saturday at the gallery."),
        F("El escultor ___ una estatua de piedra.", "hizo", ["hace", "hacemos", "hacer"], "Past event.", tr="The sculptor made a stone statue.", lemma="hacer:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 810
L810 = lesson(
    "Literature: novela, cuento, ensayo, poema, obra de teatro",
    "Un cuento es más corto que una novela; un ensayo expresa ideas y opiniones.",
    requires=["novela", "cuento", "ensayo", "poema", "poesía", "relato", "escritor", "poeta", "leyenda", "mito", "género", "autor"],
    cards=[
        card("Genres and kinds of writers",
             "A genre (género) is a category of artistic works. The main literary genres are narrativa (prose fiction), poesía (poetry), teatro (drama) and ensayo (essay).",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["la novela", "novel", "Una novela es una historia larga."],
                            ["el cuento", "short story", "Un cuento es más corto que una novela."],
                            ["el relato", "story, account", "Un relato cuenta unos hechos."],
                            ["el ensayo", "essay", "Un ensayo expresa ideas y opiniones."],
                            ["el poema", "poem", "Un poema usa ritmo e imágenes."],
                            ["la poesía", "poetry", "La poesía es el arte de los poemas."],
                            ["la obra de teatro", "play", "Una obra de teatro se presenta en un escenario."],
                            ["el dramaturgo", "playwright", "El dramaturgo escribe obras de teatro."],
                            ["la leyenda", "legend", "Una leyenda es una historia tradicional."],
                            ["el mito", "myth", "Un mito explica el origen de algo con dioses o héroes."],
                            ["la fábula", "fable", "Una fábula tiene animales y una enseñanza."],
                            ["la epopeya", "epic", "Una epopeya cuenta las hazañas de un héroe."]],
                           say=[2])]),
    ],
    exercises=[
        M("Which is longer?", "Una novela", ["Un cuento", "Un poema corto", "Un refrán"], "Novela > cuento."),
        M("What does a playwright write?", "Plays", ["Essays only", "Songs only", "Newspapers"], "Dramaturgo."),
        M("What is “una fábula”?", "A story with animals that teaches a lesson", ["A long novel", "A legal text", "A song"], "Fábula."),
        F("Un ___ expresa ideas y opiniones.", "ensayo", ["poema", "relato", "mito"], "Essay.", tr="An essay expresses ideas and opinions.", ),
        F("Un ___ es más corto que una novela.", "cuento", ["escenario", "mito", "género"], "Short story.", tr="A short story is shorter than a novel.", ),
        F("El ___ escribe obras de teatro.", "dramaturgo", ["poeta", "ensayo", "mito"], "Playwright.", tr="The playwright writes plays.", ),
        F("Una obra de teatro se presenta en un ___.", "escenario", ["ensayo", "poema", "mito"], "Stage.", tr="A play is performed on a stage.", ),
        F("Un ___ explica el origen de algo con dioses o héroes.", "mito", ["cuento", "ensayo", "relato"], "Myth.", tr="A myth explains the origin of something with gods or heroes.", ),
        F("La ___ es el arte de los poemas.", "poesía", ["novela", "obra", "fábula"], "Poetry.", tr="Poetry is the art of poems."),
    ],
)

# ---------------------------------------------------------------------------- 811
L811 = lesson(
    "Film: cinta, cortometraje, rodaje, guionista, trama",
    "La trama de la película gira en torno a una familia. El rodaje duró tres meses.",
    requires=["película", "cine", "director", "actor", "actriz", "escena", "personaje", "protagonista", "espectador", "función", "festival", "historia"],
    cards=[
        card("Words for talking about movies",
             "La cinta is another word for a movie. El cortometraje is a short film. Notice that guionista (scriptwriter) and cineasta (filmmaker) end in -a but can describe a man or a woman: el guionista, la guionista.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["la cinta", "film", "La cinta ganó varios premios."],
                            ["el cortometraje", "short film", "Vimos un cortometraje de diez minutos."],
                            ["el rodaje", "shooting, filming", "El rodaje duró tres meses."],
                            ["el guionista", "scriptwriter", "La guionista escribió el guion."],
                            ["la trama", "plot", "La trama gira en torno a una familia."],
                            ["el personaje", "character", "El personaje principal es una joven."],
                            ["el protagonista", "main character", "El protagonista enfrenta un gran problema."],
                            ["el espectador", "viewer", "Los espectadores aplauden al final de la función."],
                            ["el avance", "trailer", "El avance de la película es corto."],
                            ["la sinopsis", "synopsis", "La sinopsis resume la historia en pocas líneas."],
                            ["el cineasta", "filmmaker", "Ese cineasta dirige películas y cortos."],
                            ["el festival de cine", "film festival", "El festival de cine empieza en octubre."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “el rodaje”?", "The shooting or filming", ["The trailer", "The audience", "The script"], "Rodaje."),
        M("What is “una sinopsis”?", "A short summary of a story", ["A film festival", "A kind of camera", "A movie star"], "Sinopsis."),
        M("What is “un avance”?", "A trailer", ["A prize", "A budget", "A review"], "Avance."),
        F("La ___ de la película gira en torno a una familia.", "trama", ["cinta", "función", "escena"], "Plot.", tr="The plot of the movie revolves around a family.", ),
        F("El ___ duró tres meses.", "rodaje", ["avance", "festival", "guion"], "Filming.", tr="The filming lasted three months.", ),
        F("Vimos un ___ de diez minutos.", "cortometraje", ["rodaje", "espectador", "festival"], "Short film.", tr="We saw a ten-minute short film.", ),
        F("Los ___ aplauden al final de la función.", "espectadores", ["guionistas", "tramas", "rodajes"], "Viewers.", tr="The viewers applaud at the end of the show.", ),
        F("La ___ escribió el guion.", "guionista", ["trama", "sinopsis", "cinta"], "Scriptwriter (f.).", tr="The scriptwriter wrote the script.", ),
        F("La cinta ___ varios premios.", "ganó", ["gana", "ganamos", "ganar"], "Past event.", tr="The film won several prizes.", lemma="ganar:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 812
L812 = lesson(
    "Music: canción, letra, ritmo, cantante, componer",
    "La cantante compone sus canciones y escribe la letra.",
    requires=["música", "canción", "cantante", "letra", "ritmo", "instrumento", "concierto", "cantar", "tocar", "escuchar", "bailar", "público"],
    cards=[
        card("Talking about songs",
             "La letra means lyrics and also letter (of the alphabet). In music, it is the words of a song. Componer means to compose; its present tense is irregular in the yo form: compongo.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["la canción", "song", "Esa canción tiene un ritmo alegre."],
                            ["el canto", "singing, song", "El canto de los pájaros me despierta."],
                            ["la letra", "lyrics", "La letra habla de la amistad."],
                            ["el ritmo", "rhythm", "El ritmo hace bailar a todos."],
                            ["el / la cantante", "singer", "La cantante dio un concierto."],
                            ["el compositor", "composer", "El compositor escribe la música."],
                            ["componer", "to compose", "Ella compone canciones."],
                            ["el instrumento", "instrument", "Toco un instrumento de cuerda."],
                            ["el público", "audience", "El público aplaudió mucho."]],
                           say=[2]),
                    table(["Persona", "componer"],
                          [["yo", "compongo"], ["tú", "compones"], ["él / ella / usted", "compone"],
                           ["nosotros", "componemos"], ["vosotros", "componéis"], ["ellos / ustedes", "componen"]],
                          say=[1])]),
    ],
    exercises=[
        M("What is “la letra” of a song?", "The lyrics", ["The rhythm", "The instrument", "The audience"], "Letra."),
        M("What does “componer” mean?", "To compose", ["To repair a radio", "To sing", "To dance"], "Componer."),
        M("What does “el público” mean at a concert?", "The audience", ["The singer", "The stage", "The tickets"], "Público."),
        F("Yo ___ canciones para mi hermana.", "compongo", ["compone", "componemos", "compones"], "Yo form.", tr="I compose songs for my sister.", lemma="componer:yo"),
        F("Ella ___ canciones y escribe la letra.", "compone", ["componen", "componemos", "compongo"], "Singular subject.", tr="She composes songs and writes the lyrics.", lemma="componer:ella"),
        F("La ___ de la canción habla de la amistad.", "letra", ["ritmo", "público", "instrumento"], "Lyrics.", tr="The lyrics of the song talk about friendship."),
        F("El ___ de esa canción hace bailar a todos.", "ritmo", ["letra", "público", "compositor"], "Rhythm.", tr="The rhythm of that song makes everyone dance."),
        F("El público ___ mucho al final del concierto.", "aplaudió", ["aplaude", "aplaudimos", "aplaudir"], "Past event.", tr="The audience applauded a lot at the end of the concert.", lemma="aplaudir:él:pret"),
        F("Mi hermano toca un ___ de cuerda.", "instrumento", ["ritmo", "público", "concierto"], "Instrument.", tr="My brother plays a string instrument."),
    ],
    verify=vp("componer", "compongo", "compones", "compone", "componemos", "componéis", "componen"),
)

# ---------------------------------------------------------------------------- 813
L813 = lesson(
    "People in old stories: caballero, hidalgo, criado, fraile, mercader",
    "El caballero salió de su casa con su criado.",
    requires=["rey", "reina", "caballero", "pobre", "rico", "casa", "viaje", "historia", "palacio", "religioso", "comerciante", "sabio"],
    cards=[
        card("Characters from the past",
             "These words appear in stories set in the past, especially in Spanish-language classics. Some are masculine nouns that also have feminine forms (criado, criada; princesa is the feminine form of príncipe).",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el caballero", "knight, gentleman", "El caballero salió de su casa con su criado."],
                            ["el hidalgo", "nobleman of modest means", "El hidalgo vivía en una casa sencilla."],
                            ["el criado / la criada", "servant", "La criada preparaba la comida."],
                            ["el fraile", "friar", "El fraile ayudaba a los pobres."],
                            ["el mercader", "merchant", "El mercader vendía telas en el mercado."],
                            ["la princesa", "princess", "La princesa vivía en un castillo."],
                            ["el séquito", "entourage", "El rey llegó con un gran séquito."],
                            ["la nana", "nanny", "La nana cuidaba a los niños."],
                            ["el maestro", "master, teacher", "El maestro enseñaba a sus alumnos."],
                            ["el pecador", "sinner", "Según esa historia, el pecador pedía perdón."]],
                           say=[2])]),
    ],
    exercises=[
        M("Who is “un mercader”?", "A merchant", ["A king", "A priest", "A farmer"], "Mercader."),
        M("What is “un séquito”?", "A group of followers or attendants", ["A kind of horse", "A castle", "A sword"], "Séquito."),
        M("Who is “una criada”?", "A female servant", ["A queen", "A teacher", "A nun"], "Criada."),
        F("La ___ preparaba la comida en la casa del caballero.", "criada", ["princesa", "reina", "fraile"], "Servant.", tr="The maid prepared the food in the knight’s house.", ),
        F("El ___ vendía telas en el mercado.", "mercader", ["fraile", "séquito", "caballero"], "Merchant.", tr="The merchant sold fabrics at the market.", ),
        F("El rey llegó con un gran ___.", "séquito", ["mercader", "fraile", "hidalgo"], "Entourage.", tr="The king arrived with a large entourage.", ),
        F("La ___ vivía en un castillo.", "princesa", ["criada", "nana", "pecadora"], "Princess.", tr="The princess lived in a castle.", ),
        F("El hidalgo ___ en una casa sencilla.", "vivía", ["vive", "vivimos", "vivir"], "Past description.", tr="The nobleman lived in a simple house.", lemma="vivir:él:impf"),
        F("La nana ___ a los niños todos los días.", "cuidaba", ["cuida", "cuidamos", "cuidar"], "Past habit.", tr="The nanny took care of the children every day.", lemma="cuidar:él:impf"),
    ],
)

# ---------------------------------------------------------------------------- 814
L814 = lesson(
    "Adjectives for characters: atrevido, cobarde, fiero, vil, sabio",
    "El caballero era atrevido, pero su criado era cobarde.",
    requires=["valiente", "malo", "bueno", "rico", "pobre", "feliz", "persona", "amable", "orgulloso", "carácter", "joven", "viejo"],
    cards=[
        card("Describing people in a story",
             "These adjectives often describe characters. Adjectives ending in -o change for gender and number (atrevido, atrevida, atrevidos, atrevidas); most of those ending in -e, -l or -z only change for number (cobarde, cobardes; vil, viles; feliz, felices; a few nationality adjectives like español do add -a: española); those ending in -or, such as pecador, add -a for the feminine (pecadora).",
             tables=[table(["Adjetivo", "English", "Ejemplo"],
                           [["atrevido", "daring, bold", "El caballero era atrevido."],
                            ["cobarde", "cowardly", "Su criado era cobarde."],
                            ["fiero", "fierce", "Un animal fiero apareció en el camino."],
                            ["vil", "vile, despicable", "El personaje vil engañó a todos."],
                            ["sabio", "wise", "La anciana era sabia y daba buenos consejos."],
                            ["hospitalario", "hospitable", "La familia era muy hospitalaria con los viajeros."],
                            ["resignado", "resigned", "El pobre mercader estaba resignado a su suerte."],
                            ["ávido", "eager, avid", "Era un lector ávido de aventuras."],
                            ["complaciente", "indulgent, obliging", "Era un padre complaciente."],
                            ["estimado", "esteemed, dear", "Estimado señor, le escribo para…"],
                            ["acomodado", "well-off", "Venía de una familia acomodada."],
                            ["pecador", "sinful; a sinner", "El pecador pidió perdón."]],
                           say=[2])]),
    ],
    exercises=[
        M("What does “cobarde” mean?", "Cowardly", ["Brave", "Wise", "Generous"], "Cobarde."),
        M("What does “sabio” mean?", "Wise", ["Foolish", "Rich", "Young"], "Sabio."),
        M("What does “hospitalario” describe?", "Someone who welcomes guests warmly", ["Someone who works in a hospital only", "Someone who is sick", "Someone who is shy"], "Hospitalario."),
        F("El caballero era ___ y no tenía miedo de nada.", "atrevido", ["cobarde", "resignado", "vil"], "Bold.", tr="The knight was daring and was not afraid of anything.", ),
        F("Su criado era ___ y huía de los problemas.", "cobarde", ["atrevido", "sabio", "hospitalario"], "Cowardly.", tr="His servant was cowardly and ran from problems.", ),
        F("La anciana era ___ y daba buenos consejos.", "sabia", ["sabio", "sabias", "sabios"], "Feminine singular.", tr="The old woman was wise and gave good advice.", ),
        F("La familia era muy ___ con los viajeros.", "hospitalaria", ["hospitalario", "hospitalarias", "hospital"], "Feminine singular.", tr="The family was very hospitable to travelers.", ),
        F("Venía de una familia ___.", "acomodada", ["acomodado", "acomodadas", "acomodar"], "Feminine singular.", tr="He came from a well-off family.", ),
        F("Los personajes ___ de esa historia engañan a todos.", "viles", ["vil", "vila", "vilas"], "Plural, no gender change.", tr="The vile characters of that story deceive everyone.", ),
    ],
)

# ---------------------------------------------------------------------------- 815
L815 = lesson(
    "Adjectives for works and scenes: ficticio, inverosímil, pintoresco, inédito",
    "La novela es ficticia, pero el pueblo que describe es muy pintoresco.",
    requires=["historia", "pueblo", "paisaje", "obra", "película", "escena", "idea", "realidad", "mundo", "famoso", "nuevo", "diferente"],
    cards=[
        card("Describing art, stories and places",
             "These adjectives help you talk about works of art and the places that appear in them.",
             tables=[table(["Adjetivo", "English", "Ejemplo"],
                           [["ficticio", "fictional", "Los personajes de la novela son ficticios."],
                            ["inverosímil", "unlikely, hard to believe", "La historia es inverosímil, pero divertida."],
                            ["disparatado", "ridiculous, absurd", "El plan del villano es disparatado."],
                            ["maravilloso", "wonderful, marvelous", "El paisaje es maravilloso."],
                            ["milagroso", "miraculous", "Hubo una recuperación milagrosa."],
                            ["minucioso", "meticulous", "El pintor hizo un trabajo minucioso."],
                            ["pintoresco", "picturesque", "Es un pueblo pintoresco."],
                            ["inigualable", "unequaled", "La voz de la cantante es inigualable."],
                            ["imborrable", "unforgettable", "Esa escena dejó un recuerdo imborrable."],
                            ["inédito", "unpublished; unprecedented", "Es un poema inédito."],
                            ["mudo", "silent, mute", "Es una película muda."],
                            ["pionero", "pioneering", "Fue una directora pionera."],
                            ["arraigado", "deep-rooted", "Es una tradición muy arraigada."],
                            ["desmesurado", "excessive", "El héroe tenía una ambición desmesurada."]],
                           say=[2])]),
    ],
    exercises=[
        M("What does “inverosímil” mean?", "Hard to believe", ["Very true", "Very short", "Very old"], "Inverosímil."),
        M("What does “mudo” mean in “una película muda”?", "Silent", ["Colorful", "Long", "Famous"], "Muda."),
        M("What does “pintoresco” describe?", "A place that looks charming and typical", ["A painting only", "A noisy place", "A dangerous place"], "Pintoresco."),
        F("Los personajes de la novela son ___.", "ficticios", ["ficticio", "ficticia", "ficción"], "Masculine plural.", tr="The characters in the novel are fictional.", ),
        F("Es un pueblo muy ___.", "pintoresco", ["pintorescos", "pintoresca", "pintar"], "Masculine singular.", tr="It is a very picturesque town.", ),
        F("Esa escena dejó un recuerdo ___.", "imborrable", ["imborrables", "borrado", "borrar"], "Singular.", tr="That scene left an unforgettable memory.", ),
        F("Es una película ___ de los años veinte, sin sonido.", "muda", ["mudo", "mudas", "mudos"], "Feminine singular.", tr="It is a silent film from the twenties, without sound.", ),
        F("El plan del villano es ___.", "disparatado", ["disparatada", "disparatados", "disparar"], "Masculine singular.", tr="The villain’s plan is absurd.", ),
        F("Fue una directora ___ en la historia del cine.", "pionera", ["pionero", "pioneros", "pioneras"], "Feminine singular.", tr="She was a pioneering director in film history.", ),
    ],
)

# ---------------------------------------------------------------------------- 816
L816 = lesson(
    "Verbs for art and film: plasmar, retratar, esculpir, estrenar, rodar",
    "El pintor plasmó la cara del rey en el lienzo. La película se estrena en octubre.",
    requires=["pintar", "mostrar", "crear", "música", "película", "estrenar", "rey", "cara", "piedra", "papel", "ciudad", "costumbre"],
    cards=[
        card("Eleven verbs",
             "Most of these verbs are regular. Rodar changes o → ue (ruedo), and teñir changes e → i (tiño).",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["plasmar", "to capture, to express", "El pintor plasmó la cara del rey en el lienzo."],
                            ["retratar", "to portray, to paint a portrait of", "La novela retrata la vida de una ciudad."],
                            ["esculpir", "to sculpt", "El escultor esculpe una figura en piedra."],
                            ["restaurar", "to restore", "Los expertos restauraron el cuadro antiguo."],
                            ["estrenar", "to premiere, to use for the first time", "La película se estrena en octubre."],
                            ["rodar", "to shoot (a film); to roll", "Rodaron la película en la montaña."],
                            ["componer", "to compose", "Ella compone música para el cine."],
                            ["reflejar", "to reflect", "Esta obra refleja las costumbres de la época."],
                            ["exaltar", "to exalt, to praise highly", "El poema exalta la belleza del campo."],
                            ["teñir", "to dye, to tinge", "Las flores tiñen la tela de rojo."],
                            ["alinearse con", "to side with", "El autor se alinea con los más pobres."]],
                           say=[2])]),
        card("Two stem-changing verbs",
             "Rodar: ruedo, ruedas, rueda, rodamos, rodáis, ruedan. Teñir: tiño, tiñes, tiñe, teñimos, teñís, tiñen.",
             tables=[table(["Persona", "rodar", "teñir"],
                           [["yo", "ruedo", "tiño"], ["tú", "ruedas", "tiñes"], ["él / ella / usted", "rueda", "tiñe"],
                            ["nosotros", "rodamos", "teñimos"], ["vosotros", "rodáis", "teñís"], ["ellos / ustedes", "ruedan", "tiñen"]],
                           say=[1, 2])]),
    ],
    exercises=[
        M("What does “estrenar” mean for a film?", "To premiere it", ["To cancel it", "To copy it", "To translate it"], "Estrenar."),
        M("What does “rodar una película” mean?", "To shoot a movie", ["To watch a movie", "To sell a movie", "To rewind a movie"], "Rodar."),
        M("What does “plasmar” mean?", "To capture or express (in a work of art)", ["To destroy", "To forget", "To buy"], "Plasmar."),
        F("El pintor ___ la cara del rey en el lienzo.", "plasmó", ["plasma", "plasmamos", "plasmar"], "Past event.", tr="The painter captured the king’s face on the canvas.", lemma="plasmar:él:pret"),
        F("Ellos ___ la película en la montaña.", "ruedan", ["rueda", "rodamos", "ruedo"], "Plural subject; o → ue.", tr="They shoot the film in the mountains.", lemma="rodar:ellos"),
        F("El escultor ___ una figura en piedra.", "esculpe", ["esculpen", "esculpimos", "esculpir"], "Singular subject.", tr="The sculptor carves a figure in stone.", lemma="esculpir:él"),
        F("Esta obra ___ las costumbres de la época.", "refleja", ["reflejan", "reflejamos", "reflejar"], "Singular subject.", tr="This work reflects the customs of the period.", lemma="reflejar:él"),
        F("Los expertos ___ el cuadro antiguo.", "restauraron", ["restauró", "restauramos", "restaurar"], "Plural subject, past.", tr="The experts restored the old painting.", lemma="restaurar:ellos:pret"),
        F("Las flores ___ la tela de rojo.", "tiñen", ["tiñe", "teñimos", "tiño"], "Plural subject; e → i.", tr="The flowers dye the cloth red.", lemma="teñir:ellos"),
    ],
    verify=(vp("rodar", "ruedo", "ruedas", "rueda", "rodamos", "rodáis", "ruedan")
            + vp("teñir", "tiño", "tiñes", "tiñe", "teñimos", "teñís", "tiñen")),
)

# ---------------------------------------------------------------------------- 817
L817 = lesson(
    "Verbs from stories: arrastrar, embestir, socorrer, envejecer, tramar",
    "El toro embistió y arrastró al torero, pero un ayudante lo socorrió.",
    requires=["abandonar", "atender", "avisar", "romper", "arrancar", "levantar", "girar", "ayudar", "caer", "viejo", "casa", "problema"],
    cards=[
        card("More verbs of action",
             "These verbs often appear in stories and film plots.",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["abandonar", "to abandon", "El hidalgo abandonó su casa."],
                            ["aglutinar", "to bring together", "La fiesta aglutinó a muchos vecinos."],
                            ["alzar", "to raise", "El niño alzó la mano."],
                            ["aparentar", "to pretend, to seem", "Aparenta estar tranquilo, pero tiene miedo."],
                            ["arrancar", "to pull out, to start", "El motor arrancó."],
                            ["arrastrar", "to drag", "El río arrastró las ramas."],
                            ["arremeter contra", "to charge at", "El toro arremetió contra el torero."],
                            ["atender", "to attend to, to serve", "La criada atiende a los invitados."],
                            ["avisar", "to warn, to let know", "Nos avisaron del peligro."],
                            ["destrozar", "to destroy", "La tormenta destrozó el jardín."],
                            ["embestir", "to charge, to ram", "El toro embiste."],
                            ["envejecer", "to age", "Mi abuelo envejeció sin perder el humor."],
                            ["socorrer", "to help in danger", "Un ayudante socorrió al torero."],
                            ["tramar", "to plot", "El villano trama un plan."]],
                           say=[2]),
                    table(["Persona", "embestir", "envejecer", "atender"],
                          [["yo", "embisto", "envejezco", "atiendo"], ["tú", "embistes", "envejeces", "atiendes"],
                           ["él / ella / usted", "embiste", "envejece", "atiende"], ["nosotros", "embestimos", "envejecemos", "atendemos"],
                           ["vosotros", "embestís", "envejecéis", "atendéis"], ["ellos / ustedes", "embisten", "envejecen", "atienden"]],
                          say=[1, 2, 3])]),
    ],
    exercises=[
        M("What does “socorrer” mean?", "To help someone in danger", ["To scare someone", "To ignore someone", "To invite someone"], "Socorrer."),
        M("What does “arrastrar” mean?", "To drag", ["To throw", "To lift", "To paint"], "Arrastrar."),
        M("What does “tramar” mean?", "To plot", ["To tell the truth", "To pay", "To travel"], "Tramar."),
        F("El hidalgo ___ su casa para vivir aventuras.", "abandonó", ["abandona", "abandonamos", "abandonar"], "Past event.", tr="The nobleman left his home to have adventures.", lemma="abandonar:él:pret"),
        F("El toro ___ contra el torero.", "arremetió", ["arremete", "arremetemos", "arremeter"], "Past event.", tr="The bull charged at the bullfighter.", lemma="arremeter:él:pret"),
        F("La tormenta ___ el jardín.", "destrozó", ["destrozan", "destrozamos", "destrozar"], "Past event.", tr="The storm destroyed the garden.", lemma="destrozar:él:pret"),
        F("Un ayudante ___ al torero.", "socorrió", ["socorre", "socorremos", "socorrer"], "Past event.", tr="An assistant came to the bullfighter’s rescue.", lemma="socorrer:él:pret"),
        F("Yo ___ cada año sin darme cuenta.", "envejezco", ["envejece", "envejeces", "envejecen"], "Yo form: -zco.", tr="I age each year without noticing.", lemma="envejecer:yo"),
        F("Ellos ___ a los invitados con mucha amabilidad.", "atienden", ["atiende", "atendemos", "atiendo"], "Plural subject; e → ie.", tr="They attend to the guests with great kindness.", lemma="atender:ellos"),
    ],
    verify=(vp("embestir", "embisto", "embistes", "embiste", "embestimos", "embestís", "embisten")
            + vp("envejecer", "envejezco", "envejeces", "envejece", "envejecemos", "envejecéis", "envejecen")
            + vp("atender", "atiendo", "atiendes", "atiende", "atendemos", "atendéis", "atienden")),
)

# ---------------------------------------------------------------------------- 818
L818 = lesson(
    "Expressions: caer en una trampa, hacerse pasar por, girar en torno a",
    "La trama gira en torno a un hidalgo que se hace pasar por caballero.",
    requires=["trampa", "caer", "volver", "loco", "carne", "propio", "duda", "lugar", "dejar", "pasar", "girar", "torno"],
    cards=[
        card("Expressions for stories",
             "Learn these as whole phrases. Notice that the verb changes for person and tense (and the reflexive pronoun and any adjective change to match the subject), but the rest of the phrase stays the same.",
             tables=[table(["Expresión", "English", "Ejemplo"],
                           [["caer en una trampa", "to fall into a trap", "El villano cayó en su propia trampa."],
                            ["dejar tras de sí", "to leave behind", "El huracán dejó tras de sí mucha destrucción."],
                            ["girar en torno a", "to revolve around", "La trama gira en torno a un hidalgo."],
                            ["hacerse pasar por", "to pose as", "El ladrón se hizo pasar por médico."],
                            ["no dejar lugar a dudas", "to leave no doubt", "La prueba no dejó lugar a dudas."],
                            ["quedar embarazada", "to get pregnant", "Ella quedó embarazada en la primavera."],
                            ["vivir en carne propia", "to experience firsthand", "Lo vivió en carne propia."],
                            ["volverse loco", "to go crazy", "De tanto leer, el hidalgo se volvió loco."],
                            ["sin tregua", "without rest, relentlessly", "Trabajaron sin tregua durante días."],
                            ["valga la redundancia", "forgive the repetition", "El autor es, valga la redundancia, muy original."],
                            ["¡Válgame Dios!", "Good heavens!", "¡Válgame Dios! ¡Qué susto!"]],
                           say=[2])]),
    ],
    exercises=[
        M("What does “girar en torno a” mean?", "To revolve around (a topic)", ["To turn around a building", "To dance in a circle", "To spin a coin"], "Girar en torno a."),
        M("What does “hacerse pasar por” mean?", "To pose as", ["To pass an exam", "To make a visit", "To stop"], "Hacerse pasar por."),
        M("What does “no dejar lugar a dudas” mean?", "To leave no doubt", ["To leave no room", "To leave no money", "To leave a message"], "No dejar lugar a dudas."),
        F("El villano ___ en su propia trampa.", "cayó", ["cae", "caemos", "caer"], "Past event.", tr="The villain fell into his own trap.", lemma="caer:él:pret"),
        F("La trama ___ en torno a un hidalgo.", "gira", ["giran", "giramos", "girar"], "Singular subject.", tr="The plot revolves around a nobleman.", lemma="girar:él"),
        F("El ladrón se ___ pasar por médico.", "hizo", ["hace", "hacemos", "hacer"], "Past event.", tr="The thief pretended to be a doctor.", lemma="hacer:él:pret"),
        F("Lo vivió en carne ___.", "propia", ["propio", "propias", "proponer"], "Feminine singular.", tr="He experienced it firsthand."),
        F("De tanto leer, el hidalgo se volvió ___.", "loco", ["loca", "locos", "locura"], "Masculine singular.", tr="From reading so much, the nobleman went mad."),
        F("Trabajaron ___ tregua durante días.", "sin", ["con", "en", "por"], "Sin tregua.", tr="They worked without rest for days."),
    ],
)

# ---------------------------------------------------------------------------- 819
L819 = lesson(
    "Other story words: asno, molino de viento, rebaño, lanza, galardón",
    "El caballero atacó los molinos de viento con su lanza.",
    requires=["animal", "viento", "premio", "cuna", "fondo", "mar", "comida", "ropa", "caballo", "atacar", "lejos", "dentro"],
    cards=[
        card("Useful nouns",
             "These nouns appear in classic stories and in news about prizes and the arts.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el asno", "donkey", "El mercader viajaba con un asno."],
                            ["la cuna", "crib; birthplace", "El bebé duerme en su cuna."],
                            ["el fondo", "bottom, back", "La tienda está al fondo del pasillo."],
                            ["el galardón", "award, prize", "La directora recibió un galardón."],
                            ["la lanza", "spear, lance", "El caballero llevaba una lanza."],
                            ["mar adentro", "out to sea", "El barco se fue mar adentro."],
                            ["el molino de viento", "windmill", "En la llanura hay molinos de viento."],
                            ["las pertenencias", "belongings", "El viajero guardó sus pertenencias en una bolsa."],
                            ["el rebaño", "flock (of sheep)", "El pastor cuida un rebaño de ovejas."],
                            ["el premio / la presea", "prize, award", "La presea más importante es para el mejor catedrático."]],
                           say=[2])]),
    ],
    exercises=[
        M("What is “un molino de viento”?", "A windmill", ["A water mill only", "A kind of storm", "A farm"], "Molino de viento."),
        M("What is “un rebaño”?", "A flock", ["A farm", "A shepherd", "A forest"], "Rebaño."),
        M("What are “las pertenencias”?", "Belongings", ["Neighbors", "Farms", "Relatives"], "Pertenencias."),
        F("El mercader viajaba con un ___.", "asno", ["rebaño", "galardón", "molino"], "Donkey.", tr="The merchant traveled with a donkey.", ),
        F("El caballero llevaba una ___ larga.", "lanza", ["cuna", "pertenencia", "presea"], "Lance.", tr="The knight carried a long lance.", ),
        F("El pastor cuida un ___ de ovejas.", "rebaño", ["asno", "galardón", "fondo"], "Flock.", tr="The shepherd looks after a flock of sheep.", ),
        F("La directora recibió un ___ por su película.", "galardón", ["asno", "rebaño", "molino"], "Award.", tr="The director received an award for her film.", ),
        F("En la llanura hay muchos ___ de viento.", "molinos", ["molino", "molina", "moler"], "Plural noun.", tr="On the plain there are many windmills.", ),
        F("El viajero guardó sus ___ en una bolsa.", "pertenencias", ["pertenencia", "lanzas", "cunas"], "Plural noun.", tr="The traveler kept his belongings in a bag.", ),
    ],
)

# ---------------------------------------------------------------------------- 820
L820 = lesson(
    "Don Quijote, part 1: the nobleman who read too many books",
    "Don Quijote es un hidalgo que lee tantas novelas de caballería que se vuelve loco.",
    requires=["libro", "leer", "loco", "caballero", "aventura", "vecino", "caballo", "pueblo", "historia", "autor", "nombre", "casa"],
    cards=[
        card("The story in short (my own summary)",
             "Don Quijote de la Mancha is a classic of Spanish literature by Miguel de Cervantes, published in two parts. This summary is original; it does not quote the book.",
             examples=[
                 ex("Miguel de Cervantes publicó la primera parte en mil seiscientos cinco y la segunda en mil seiscientos quince.", "Miguel de Cervantes published the first part in sixteen oh-five and the second in sixteen fifteen.", "publicó"),
                 ex("Alonso Quijano es un hidalgo que vive en un pueblo de La Mancha.", "Alonso Quijano is a nobleman who lives in a village in La Mancha.", "hidalgo"),
                 ex("Lee tantas novelas de caballería que se vuelve loco.", "He reads so many chivalry novels that he goes mad.", "se vuelve loco"),
                 ex("Se cree un caballero andante y toma el nombre de don Quijote.", "He believes he is a knight-errant and takes the name Don Quijote.", "caballero andante"),
                 ex("Su vecino Sancho Panza lo acompaña como escudero.", "His neighbor Sancho Panza accompanies him as squire.", "escudero"),
                 ex("Don Quijote monta un caballo flaco llamado Rocinante.", "Don Quijote rides a thin horse named Rocinante.", "monta"),
                 ex("Idealiza a una campesina y la llama Dulcinea.", "He idealizes a peasant woman and calls her Dulcinea.", "Idealiza"),
             ]),
        card("A fun fact",
             "Cervantes and Shakespeare died in the same year, sixteen sixteen, so people often mention them together.",
             examples=[
                 ex("Cervantes y Shakespeare murieron en el mismo año.", "Cervantes and Shakespeare died in the same year.", "murieron"),
             ]),
    ],
    exercises=[
        M("Who wrote Don Quijote?", "Miguel de Cervantes", ["Pedro Calderón de la Barca", "Rubén Darío", "Gabriel García Márquez"], "Cervantes."),
        M("Why does Alonso Quijano go mad, according to the summary?", "He reads too many chivalry novels", ["He travels too much", "He drinks too little", "He loses his horse"], "Novelas de caballería."),
        M("Who is Sancho Panza?", "His neighbor, who becomes his squire", ["His brother", "A king", "A priest"], "Escudero."),
        F("Don Quijote es un hidalgo que ___ novelas de caballería.", "lee", ["leen", "leemos", "leer"], "Singular subject.", tr="Don Quijote is a nobleman who reads chivalry novels.", lemma="leer:él"),
        F("Su vecino Sancho Panza lo ___ como escudero.", "acompaña", ["acompañan", "acompañamos", "acompañar"], "Singular subject.", tr="His neighbor Sancho Panza accompanies him as squire.", lemma="acompañar:él"),
        F("Don Quijote ___ un caballo flaco llamado Rocinante.", "monta", ["montan", "montamos", "montar"], "Singular subject.", tr="Don Quijote rides a thin horse called Rocinante.", lemma="montar:él"),
        F("Cervantes ___ la primera parte en mil seiscientos cinco.", "publicó", ["publica", "publicamos", "publicar"], "Historical past.", tr="Cervantes published the first part in sixteen oh-five.", lemma="publicar:él:pret"),
        F("Alonso Quijano vive en un ___ de La Mancha.", "pueblo", ["libro", "caballo", "nombre"], "Village.", tr="Alonso Quijano lives in a village in La Mancha."),
        F("Alonso Quijano toma el ___ de don Quijote.", "nombre", ["libro", "pueblo", "caballo"], "He takes the name.", tr="Alonso Quijano takes the name of don Quijote."),
    ],
)

# ---------------------------------------------------------------------------- 821
L821 = lesson(
    "Don Quijote, part 2: windmills, imagination and reality",
    "Don Quijote ve molinos de viento y cree que son gigantes.",
    requires=["ver", "creer", "gigante", "ejército", "imaginación", "realidad", "idea", "lector", "humor", "final", "razón", "libertad"],
    cards=[
        card("Famous episodes and ideas",
             "These sentences summarize episodes and ideas from the novel in my own words. Readers interpret the book in different ways, so notice the verbs of opinion (muchos lectores dicen, algunos críticos creen).",
             examples=[
                 ex("En un episodio famoso, don Quijote ve molinos de viento y cree que son gigantes.", "In a famous episode, Don Quijote sees windmills and thinks they are giants.", "cree"),
                 ex("Sancho le explica que son molinos, pero don Quijote ataca con su lanza.", "Sancho explains to him that they are windmills, but Don Quijote attacks with his lance.", "ataca"),
                 ex("En otro episodio, confunde un rebaño de ovejas con un ejército.", "In another episode, he mistakes a flock of sheep for an army.", "confunde"),
                 ex("El humor nace del choque entre la imaginación de don Quijote y la realidad.", "The humor comes from the clash between Don Quijote’s imagination and reality.", "choque"),
                 ex("Sancho representa el sentido práctico; don Quijote, el idealismo.", "Sancho represents practical sense; Don Quijote, idealism.", "representa"),
                 ex("Al final de la novela, don Quijote recupera la razón y vuelve a ser Alonso Quijano.", "At the end of the novel, Don Quijote regains his reason and becomes Alonso Quijano again.", "recupera"),
                 ex("Muchos lectores dicen que la novela habla de la imaginación, de la locura y de la libertad.", "Many readers say that the novel is about imagination, madness and freedom.", "Muchos lectores"),
             ]),
        card("A word from the novel",
             "The adjective quijotesco describes a person who is idealistic and not very practical. It comes from the name of the main character.",
             examples=[
                 ex("Su plan es muy quijotesco.", "His plan is very quixotic.", "quijotesco"),
             ]),
    ],
    exercises=[
        M("What does don Quijote think the windmills are?", "Giants", ["Castles", "Soldiers", "Ships"], "Gigantes."),
        M("What creates the humor, according to the card?", "The clash between imagination and reality", ["The long journeys", "The food", "The weather"], "Choque."),
        M("What does “quijotesco” describe?", "Someone idealistic and not very practical", ["Someone very rich", "Someone very old", "Someone very angry"], "Quijotesco."),
        F("Don Quijote ___ molinos de viento y cree que son gigantes.", "ve", ["ven", "vemos", "ver"], "Singular subject.", tr="Don Quijote sees windmills and thinks they are giants.", lemma="ver:él"),
        F("Sancho le ___ que son molinos.", "explica", ["explican", "explicamos", "explicar"], "Singular subject.", tr="Sancho explains to him that they are windmills.", lemma="explicar:él"),
        F("En otro episodio, don Quijote ___ un rebaño con un ejército.", "confunde", ["confunden", "confundimos", "confundir"], "Singular subject.", tr="In another episode, Don Quijote mistakes a flock for an army.", lemma="confundir:él"),
        F("Sancho representa el sentido práctico; don Quijote, el ___.", "idealismo", ["rebaño", "molino", "ejército"], "Idealism.", tr="Sancho represents practical sense; Don Quijote, idealism."),
        F("Al final, don Quijote ___ la razón.", "recupera", ["recuperan", "recuperamos", "recuperar"], "Singular subject.", tr="In the end, Don Quijote regains his reason.", lemma="recuperar:él"),
        F("Muchos lectores dicen que la novela habla de la imaginación y de la ___.", "libertad", ["lanza", "tinta", "criada"], "Freedom.", tr="Many readers say that the novel is about imagination and freedom."),
    ],
)

# ---------------------------------------------------------------------------- 822
L822 = lesson(
    "La vida es sueño: a prince in a tower",
    "Segismundo, un príncipe de Polonia, vive encerrado en una torre desde que nació.",
    requires=["torre", "príncipe", "sueño", "soñar", "destino", "palacio", "rey", "violencia", "justicia", "carácter", "controlar", "teatro"],
    cards=[
        card("A play from the Spanish Golden Age (my own summary)",
             "Pedro Calderón de la Barca wrote La vida es sueño in the seventeenth century. This is my own summary of the plot; it does not quote the play.",
             examples=[
                 ex("La vida es sueño es una obra de teatro del Siglo de Oro español.", "La vida es sueño is a play from the Spanish Golden Age.", "Siglo de Oro"),
                 ex("Segismundo, un príncipe de Polonia, vive encerrado en una torre desde que nació.", "Segismundo, a prince of Poland, has lived shut up in a tower since he was born.", "encerrado"),
                 ex("Su padre, el rey Basilio, tiene miedo de una profecía sobre su hijo.", "His father, King Basilio, is afraid of a prophecy about his son.", "profecía"),
                 ex("Un día, el rey lo lleva al palacio mientras duerme para ver cómo se comporta.", "One day, the king takes him to the palace while he sleeps to see how he behaves.", "palacio"),
                 ex("Segismundo actúa con violencia, y después lo devuelven a la torre y le dicen que todo fue un sueño.", "Segismundo acts violently, and afterward they return him to the tower and tell him that it was all a dream.", "sueño"),
                 ex("Más tarde, aprende a controlar su carácter y decide actuar con justicia.", "Later, he learns to control his character and decides to act with justice.", "controlar"),
                 ex("La obra pregunta qué es real y cuánto podemos elegir.", "The play asks what is real and how much we can choose.", "pregunta"),
             ]),
    ],
    exercises=[
        M("Who is Segismundo?", "A prince shut up in a tower", ["A merchant", "A knight with a squire", "A friar"], "Príncipe."),
        M("What does the king want to find out?", "How his son behaves", ["Where the treasure is", "Who wrote a poem", "How to build a tower"], "Cómo se comporta."),
        M("What does the play ask, according to the summary?", "What is real and how much we can choose", ["How to win a war", "How to become rich", "How to write a novel"], "Real vs sueño."),
        F("Segismundo ___ encerrado en una torre desde que nació.", "vive", ["viven", "vivimos", "vivir"], "Singular subject.", tr="Segismundo has lived shut up in a tower since he was born.", lemma="vivir:él"),
        F("Su padre, el rey Basilio, ___ miedo de una profecía.", "tiene", ["tienen", "tenemos", "tener"], "Singular subject.", tr="His father, King Basilio, is afraid of a prophecy.", lemma="tener:él"),
        F("El rey lo lleva al palacio mientras ___.", "duerme", ["duermen", "dormimos", "dormir"], "Singular subject.", tr="The king takes him to the palace while he sleeps.", lemma="dormir:él"),
        F("Más tarde, Segismundo ___ a controlar su carácter.", "aprende", ["aprenden", "aprendemos", "aprender"], "Singular subject.", tr="Later, Segismundo learns to control his character.", lemma="aprender:él"),
        F("La obra de Calderón pertenece al ___ de Oro.", "Siglo", ["Rey", "Sueño", "Teatro"], "Siglo de Oro.", tr="Calderón’s play belongs to the Golden Age."),
        F("La obra pregunta si la vida es realidad o ___.", "sueño", ["torre", "palacio", "príncipe"], "Dream.", tr="The play asks whether life is reality or a dream."),
    ],
)

# ---------------------------------------------------------------------------- 823
L823 = lesson(
    "The film Roma: a family, a city and a domestic worker",
    "Roma es una película en blanco y negro del director mexicano Alfonso Cuarón.",
    requires=["película", "director", "blanco", "negro", "clase", "media", "familia", "infancia", "recuerdo", "premio", "ciudad", "trabajo"],
    cards=[
        card("About the film (my own description)",
             "Roma is a film that many people know. I describe it here in my own words, without quoting scenes or dialogue. People interpret it differently, and some viewers focus on the family, others on social class.",
             examples=[
                 ex("Roma es una película en blanco y negro del director mexicano Alfonso Cuarón.", "Roma is a black-and-white film by the Mexican director Alfonso Cuarón.", "blanco y negro"),
                 ex("Se estrenó en dos mil dieciocho.", "It premiered in two thousand eighteen.", "estrenó"),
                 ex("La historia ocurre en la Ciudad de México a comienzos de los años setenta.", "The story takes place in Mexico City in the early seventies.", "ocurre"),
                 ex("La protagonista es Cleo, una joven que trabaja como empleada doméstica para una familia de clase media.", "The main character is Cleo, a young woman who works as a domestic worker for a middle-class family.", "empleada doméstica"),
                 ex("La película habla de la familia, de las diferencias de clase y del trabajo doméstico.", "The film is about family, class differences and domestic work.", "diferencias"),
                 ex("Según el director, se inspira en recuerdos de su infancia.", "According to the director, it is inspired by memories of his childhood.", "recuerdos"),
                 ex("Ganó varios premios importantes.", "It won several important awards.", "premios"),
             ]),
    ],
    exercises=[
        M("Who directed Roma?", "Alfonso Cuarón", ["Fernando Botero", "Miguel de Cervantes", "Pedro Calderón"], "Cuarón."),
        M("Where does the story take place?", "In Mexico City", ["In Madrid", "In Bogotá", "In Santiago"], "Ciudad de México."),
        M("According to the director, what inspired the film?", "Memories of his childhood", ["A newspaper article", "A novel by Cervantes", "A song"], "Infancia."),
        F("Roma es una película en blanco y ___.", "negro", ["rojo", "verde", "azul"], "Black and white.", tr="Roma is a black-and-white film."),
        F("La protagonista ___ como empleada doméstica.", "trabaja", ["trabajan", "trabajamos", "trabajar"], "Singular subject.", tr="The main character works as a domestic worker.", lemma="trabajar:ella"),
        F("La película ___ de la familia y de las diferencias de clase.", "habla", ["hablan", "hablamos", "hablar"], "Singular subject.", tr="The film is about the family and class differences.", lemma="hablar:él"),
        F("La película se ___ en dos mil dieciocho.", "estrenó", ["estrena", "estrenamos", "estrenar"], "Past event.", tr="The film premiered in two thousand eighteen.", lemma="estrenar:él:pret"),
        F("Según el director, la película se inspira en recuerdos de su ___.", "infancia", ["ciudad", "premio", "familia grande"], "Childhood.", tr="According to the director, the film is inspired by memories of his childhood."),
        F("La película ___ varios premios importantes.", "ganó", ["gana", "ganamos", "ganar"], "Past event.", tr="The film won several important awards.", lemma="ganar:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 824
L824 = lesson(
    "Fernando Botero: voluminous figures",
    "Fernando Botero fue un pintor y escultor colombiano famoso por sus figuras voluminosas.",
    requires=["pintor", "pintura", "figura", "redondo", "plaza", "ciudad", "estilo", "vida", "diario", "retrato", "bailar", "color"],
    cards=[
        card("About the artist (my own description)",
             "Fernando Botero is one of the best-known Latin American artists. The description below is general; critics and viewers interpret his style in different ways.",
             examples=[
                 ex("Fernando Botero fue un pintor y escultor colombiano.", "Fernando Botero was a Colombian painter and sculptor.", "escultor"),
                 ex("Nació en Medellín en mil novecientos treinta y dos y murió en dos mil veintitrés.", "He was born in Medellín in nineteen thirty-two and died in two thousand twenty-three.", "Nació"),
                 ex("Es famoso por sus figuras de formas redondas y voluminosas.", "He is famous for his figures with round, voluminous shapes.", "voluminosas"),
                 ex("Pintó escenas de la vida diaria, bailes, retratos y naturalezas muertas.", "He painted scenes of daily life, dances, portraits and still lifes.", "naturalezas muertas"),
                 ex("Sus esculturas grandes están en plazas de muchas ciudades.", "His large sculptures are in squares in many cities.", "plazas"),
                 ex("Cada espectador puede interpretar sus figuras de una manera diferente.", "Each viewer can interpret his figures in a different way.", "interpretar"),
             ]),
    ],
    exercises=[
        M("What is Botero famous for?", "Round, voluminous figures", ["Black-and-white films", "Folk songs", "Epic poems"], "Figuras voluminosas."),
        M("Where are his large sculptures?", "In squares in many cities", ["Only in one museum", "Only in private homes", "Nowhere"], "Plazas."),
        M("What nationality was Botero?", "Colombian", ["Chilean", "Spanish", "Mexican"], "Colombiano."),
        F("Fernando Botero fue un pintor y ___ colombiano.", "escultor", ["cantante", "director", "poeta"], "Sculptor.", tr="Fernando Botero was a Colombian painter and sculptor."),
        F("Es famoso por sus figuras de formas ___ y voluminosas.", "redondas", ["redondo", "redonda", "redondos"], "Feminine plural.", tr="He is famous for his figures with round and voluminous shapes."),
        F("Sus esculturas grandes están en ___ de muchas ciudades.", "plazas", ["libros", "cuentos", "canciones"], "Squares.", tr="His large sculptures are in squares in many cities."),
        F("Botero ___ en Medellín en mil novecientos treinta y dos.", "nació", ["nace", "nacemos", "nacer"], "Past event.", tr="Botero was born in Medellín in nineteen thirty-two.", lemma="nacer:él:pret"),
        F("Botero ___ escenas de la vida diaria.", "pintó", ["pinta", "pintamos", "pintar"], "Past event.", tr="Botero painted scenes of daily life.", lemma="pintar:él:pret"),
        F("Cada espectador puede ___ sus figuras de una manera diferente.", "interpretar", ["interpreta", "interpretan", "interpretado"], "Infinitive after poder.", tr="Each viewer can interpret his figures in a different way."),
    ],
)

# ---------------------------------------------------------------------------- 825
L825 = lesson(
    "Violeta Parra: songs, folklore and tapestries",
    "Violeta Parra fue una cantautora, folclorista y artista visual chilena.",
    requires=["canción", "cantante", "campo", "tradicional", "pintura", "influir", "legado", "música", "artista", "chileno", "música", "viaje"],
    cards=[
        card("About the artist (my own description)",
             "Violeta Parra is an important figure in Chilean and Latin American music. This is a general description; it does not quote her lyrics.",
             examples=[
                 ex("Violeta Parra fue una cantautora, folclorista y artista visual chilena.", "Violeta Parra was a Chilean singer-songwriter, folklorist and visual artist.", "folclorista"),
                 ex("Recorrió el campo de Chile para recoger canciones tradicionales.", "She traveled through the Chilean countryside to collect traditional songs.", "Recorrió"),
                 ex("Compuso canciones propias, entre ellas Gracias a la vida, una de las más conocidas.", "She composed songs of her own, including “Gracias a la vida”, one of the best known.", "Compuso"),
                 ex("También hizo pinturas y tapices bordados llamados arpilleras.", "She also made paintings and embroidered tapestries called arpilleras.", "arpilleras"),
                 ex("Expuso sus obras en París en mil novecientos sesenta y cuatro.", "She exhibited her works in Paris in nineteen sixty-four.", "Expuso"),
                 ex("Murió en mil novecientos sesenta y siete.", "She died in nineteen sixty-seven.", "Murió"),
                 ex("Muchos músicos de América Latina dicen que su obra los influyó.", "Many Latin American musicians say that her work influenced them.", "influyó"),
             ]),
    ],
    exercises=[
        M("What nationality was Violeta Parra?", "Chilean", ["Mexican", "Colombian", "Spanish"], "Chilena."),
        M("What did she collect in the countryside?", "Traditional songs", ["Paintings", "Newspapers", "Film scripts"], "Canciones tradicionales."),
        M("What are “arpilleras”?", "Embroidered tapestries", ["A kind of guitar", "A film festival", "A type of poem"], "Arpilleras."),
        F("Violeta Parra ___ el campo de Chile para recoger canciones tradicionales.", "recorrió", ["recorre", "recorremos", "recorrer"], "Past event.", tr="Violeta Parra traveled through the Chilean countryside to collect traditional songs.", lemma="recorrer:él:pret"),
        F("Ella ___ canciones propias.", "compuso", ["compone", "componemos", "componer"], "Past event.", tr="She composed songs of her own.", lemma="componer:ella:pret"),
        F("También hizo pinturas y ___ bordados.", "tapices", ["tapiz", "cuentos", "ensayos"], "Plural noun.", tr="She also made paintings and embroidered tapestries."),
        F("Parra ___ sus obras en París en mil novecientos sesenta y cuatro.", "expuso", ["expone", "exponemos", "exponer"], "Past event.", tr="Parra exhibited her works in Paris in nineteen sixty-four.", lemma="exponer:ella:pret"),
        F("Violeta Parra ___ en mil novecientos sesenta y siete.", "murió", ["muere", "morimos", "morir"], "Past event.", tr="Violeta Parra died in nineteen sixty-seven.", lemma="morir:ella:pret"),
        F("Muchos músicos dicen que su obra los ___.", "influyó", ["influye", "influimos", "influir"], "Past event.", tr="Many musicians say that her work influenced them.", lemma="influir:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 826
L826 = lesson(
    "Proverbs: refranes and their meanings",
    "Más vale tarde que nunca. En boca cerrada no entran moscas.",
    requires=["tarde", "nunca", "regalar", "diente", "boca", "cerrar", "decir", "dicho", "hecho", "tiempo", "amigo", "caballo"],
    cards=[
        card("Ten traditional sayings",
             "A refrán is a short traditional saying that gives advice. Proverbs are not translated word for word: learn the meaning.",
             tables=[table(["Refrán", "Meaning"],
                           [["Más vale tarde que nunca.", "It is better to do something late than never."],
                            ["A caballo regalado no se le mira el diente.", "Don’t criticize a gift."],
                            ["En boca cerrada no entran moscas.", "Sometimes it is wiser to stay silent."],
                            ["Dime con quién andas y te diré quién eres.", "You can tell a lot about a person by his friends."],
                            ["Del dicho al hecho hay mucho trecho.", "Saying and doing are very different things."],
                            ["No hay mal que por bien no venga.", "Bad events can bring something good."],
                            ["Perro que ladra no muerde.", "People who make a lot of threats rarely act."],
                            ["Al que madruga, Dios lo ayuda.", "Getting up early brings rewards."],
                            ["Camarón que se duerme, se lo lleva la corriente.", "If you are not alert, you will lose out."],
                            ["Verdad de Perogrullo.", "An obvious truth, something everyone knows."]],
                           say=[0])]),
    ],
    exercises=[
        M("What does “Más vale tarde que nunca” mean?", "It is better to do something late than never", ["Be on time always", "Never do it", "Wait for tomorrow"], "Más vale tarde que nunca."),
        M("What does “A caballo regalado no se le mira el diente” mean?", "Don’t criticize a gift", ["Buy a horse carefully", "Brush your teeth", "Never give gifts"], "Regalo."),
        M("What is “una verdad de Perogrullo”?", "An obvious truth", ["A secret", "A lie", "A prayer"], "Perogrullo."),
        F("Más vale ___ que nunca.", "tarde", ["pronto", "ayer", "mañana"], "Proverb.", tr="Better late than never."),
        F("A caballo regalado no se le mira el ___.", "diente", ["ojo", "pie", "nombre"], "Proverb.", tr="Don’t look a gift horse in the mouth."),
        F("En boca ___ no entran moscas.", "cerrada", ["abierta", "grande", "pequeña"], "Proverb.", tr="A closed mouth catches no flies. (Keeping quiet can save you trouble.)"),
        F("Dime con quién ___ y te diré quién eres.", "andas", ["andamos", "andan", "andar"], "Tú form.", tr="Tell me who you walk with and I will tell you who you are.", lemma="andar:tú"),
        F("Del dicho al ___ hay mucho trecho.", "hecho", ["hecha", "decir", "dicho"], "Proverb.", tr="There is a long way from saying to doing."),
        F("No hay mal que por ___ no venga.", "bien", ["nunca", "tarde", "dicho"], "Proverb.", tr="Every cloud has a silver lining."),
    ],
)

# ---------------------------------------------------------------------------- 827
L827 = lesson(
    "The conditional perfect: habría comido",
    "Yo habría comido más. Ellos habrían llegado antes.",
    requires=["haber", "comer", "llegar", "decir", "ver", "escribir", "ir", "salir", "hacer", "verdad", "carta", "película"],
    cards=[
        card("How to form the conditional perfect",
             "The conditional perfect means “would have + participle.” Build it with haber in the conditional (habría, habrías, habría, habríamos, habríais, habrían) + a past participle. "
             "The participle never changes. It is the same participle that you use in the present perfect and the pluperfect.",
             tables=[table(["Persona", "Condicional perfecto"],
                           [["yo", "habría comido"], ["tú", "habrías comido"], ["él / ella / usted", "habría comido"],
                            ["nosotros", "habríamos comido"], ["vosotros", "habríais comido"], ["ellos / ustedes", "habrían comido"]],
                           say=[1]),
                    table(["Infinitivo", "Participio", "Ejemplo"],
                          [["decir", "dicho", "Tú habrías dicho la verdad."], ["ver", "visto", "Ellos habrían visto la película."],
                           ["escribir", "escrito", "Yo habría escrito una carta."], ["hacer", "hecho", "Nosotros habríamos hecho lo mismo."],
                           ["ir", "ido", "Ella habría ido a la fiesta."]],
                          say=[1, 2])]),
        card("Quick contrast",
             "The simple conditional says what would happen (comería = I would eat). The conditional perfect says what would have happened earlier (habría comido = I would have eaten).",
             examples=[
                 ex("Yo comería ahora.", "I would eat now.", "comería"),
                 ex("Yo habría comido antes.", "I would have eaten earlier.", "habría comido"),
             ]),
    ],
    exercises=[
        M("Which form means “I would have eaten”?", "habría comido", ["habré comido", "había comido", "he comido"], "Habría + participle."),
        M("What is the participle of “hacer”?", "hecho", ["hacido", "haciendo", "hice"], "Hecho."),
        M("Does the participle change after habría?", "No, it never changes", ["Yes, it agrees with the subject", "Yes, it agrees with the object", "Only in the plural"], "It stays the same."),
        F("Nosotros ___ llegado antes.", "habríamos", ["habrían", "habría", "habríais"], "Nosotros → habríamos.", tr="We would have arrived earlier.", lemma="haber:nosotros:cond"),
        F("Tú ___ dicho la verdad.", "habrías", ["habrían", "habría", "habríamos"], "Tú → habrías.", tr="You would have told the truth.", lemma="haber:tú:cond"),
        F("Ellos habrían ___ la película.", "visto", ["ver", "viendo", "vieron"], "Participle of ver.", tr="They would have seen the movie.", lemma="ver:part"),
        F("Yo habría ___ una carta.", "escrito", ["escribido", "escribiendo", "escribí"], "Participle of escribir.", tr="I would have written a letter.", lemma="escribir:part"),
        F("Usted ___ salido más temprano.", "habría", ["habríamos", "habrían", "habrías"], "Usted → habría.", tr="You (formal) would have left earlier.", lemma="haber:usted:cond"),
        F("Ella habría ___ a la fiesta.", "ido", ["iba", "ir", "yendo"], "Participle of ir.", tr="She would have gone to the party.", lemma="ir:part"),
    ],
    verify=(vpd("haber", "habría", "habrías", "habría", "habríamos", "habríais", "habrían")
            + vpa("decir", "dicho") + vpa("ver", "visto") + vpa("escribir", "escrito") + vpa("hacer", "hecho") + vpa("ir", "ido")),
)

# ---------------------------------------------------------------------------- 828
L828 = lesson(
    "Would have done it, but it did not happen",
    "Habría viajado, pero no tenía dinero. Habríamos ayudado, pero no sabíamos nada.",
    requires=["viajar", "ayudar", "estudiar", "ganar", "tener", "decir", "vender", "casa", "dinero", "tiempo", "accidente", "partido"],
    cards=[
        card("Something that could have happened but did not",
             "The conditional perfect often names an action that would have taken place, followed by pero and the reason it did not. The reason is usually in the imperfect or the preterite.",
             tables=[table(["Habría + participio", "Pero + razón"],
                           [["Habría viajado,", "pero no tenía dinero."],
                            ["Habríamos ayudado,", "pero no sabíamos nada."],
                            ["Ella habría ganado el partido,", "pero tuvo un accidente."],
                            ["Habría estudiado más,", "pero no tenía tiempo."]],
                           say=[0, 1])]),
        card("Present or past?",
             "Compare the simple conditional with the perfect form. The simple conditional looks at the present or future. The perfect form looks back at the past.",
             examples=[
                 ex("Compraría una casa, pero no tengo dinero.", "I would buy a house, but I do not have money.", "Compraría"),
                 ex("Habría comprado una casa, pero no tenía dinero.", "I would have bought a house, but I did not have money.", "Habría comprado"),
             ]),
    ],
    exercises=[
        M("Which sentence is about something that did not happen in the past?", "Habría viajado, pero no tenía dinero.", ["Viajaría mañana si tuviera dinero.", "Viajo mañana.", "Voy a viajar."], "Habría + participle looks back."),
        M("What does “habría comprado” mean?", "would have bought", ["would buy", "had bought", "will have bought"], "Conditional perfect."),
        M("In “Habría ido, pero estaba cansado”, what does the second part give?", "The reason it did not happen", ["The time of the trip", "The place", "The person who went"], "Pero + reason."),
        F("Yo habría ___ más, pero no tenía tiempo.", "estudiado", ["estudiar", "estudiando", "estudié"], "Participle of estudiar.", tr="I would have studied more, but I did not have time.", lemma="estudiar:part"),
        F("Nosotros ___ ayudado, pero no sabíamos nada.", "habríamos", ["habrían", "habría", "habríais"], "Nosotros → habríamos.", tr="We would have helped, but we knew nothing.", lemma="haber:nosotros:cond"),
        F("Ella habría ___ el partido, pero tuvo un accidente.", "ganado", ["ganar", "ganando", "ganó"], "Participle of ganar.", tr="She would have won the game, but she had an accident.", lemma="ganar:part"),
        F("Ellos habrían ___ más dinero, pero perdieron el trabajo.", "tenido", ["tener", "teniendo", "tuvieron"], "Participle of tener.", tr="They would have had more money, but they lost their job.", lemma="tener:part"),
        F("Tú habrías ___ la verdad, pero tenías miedo.", "dicho", ["decido", "diciendo", "dijiste"], "Participle of decir.", tr="You would have told the truth, but you were afraid.", lemma="decir:part"),
        F("Usted ___ vendido la casa, pero nadie la quiso comprar.", "habría", ["habrían", "habrías", "habríamos"], "Usted → habría.", tr="You (formal) would have sold the house, but nobody wanted to buy it.", lemma="haber:usted:cond"),
    ],
    verify=vpd("haber", "habría", "habrías", "habría", "habríamos", "habríais", "habrían") + vpa("tener", "tenido") + vpa("ganar", "ganado"),
)

# ---------------------------------------------------------------------------- 829
L829 = lesson(
    "Guessing about the past: Habrían salido, Habría salido",
    "No contestaron. Habrían salido. Juan no vino. Se habría enfermado.",
    requires=["salir", "estar", "ir", "dejar", "caminar", "enfermo", "teléfono", "parque", "problema", "tren", "vecino", "niño"],
    cards=[
        card("Probably, in the past",
             "Spanish uses the conditional perfect to guess about something that probably happened before a past moment. It works like “must have” or “probably had” in English. "
             "The guess is about an earlier event. Native speakers often add words like probablemente or seguramente, but the tense itself already shows the guess.",
             tables=[table(["Situación pasada", "Suposición"],
                           [["Nadie contestó.", "Los vecinos habrían salido."],
                            ["Juan no vino.", "Se habría enfermado."],
                            ["Mi hermana no llamó.", "Habría dejado el teléfono en casa."],
                            ["El tren no llegó.", "Habría habido un problema."]],
                           say=[1])]),
        card("A note about use",
             "This use is less common than other ways of guessing, and you will see it more in writing, but you may also hear it in conversation. Many speakers also use probablemente + the pluperfect or the preterite.",
             examples=[
                 ex("Los niños no estaban en casa. Habrían ido al parque.", "The children were not at home. They had probably gone to the park.", "Habrían ido"),
             ]),
    ],
    exercises=[
        M("“No llegó. Se habría perdido.” What does the second sentence mean?", "He had probably gotten lost.", ["He will get lost.", "He is lost for sure.", "He never gets lost."], "A guess about an earlier event."),
        M("Which sentence guesses that Ana probably left early?", "Ana habría salido temprano.", ["Ana saldría mañana.", "Ana ha salido.", "Ana sale temprano."], "Habría + participle = probable past event."),
        M("What does the conditional perfect do in “Habrían salido a almorzar”?", "It guesses what probably happened earlier", ["It says what is certain", "It gives an order", "It talks about the future"], "A past guess."),
        F("Nadie contestó. Los vecinos ___ salido.", "habrían", ["habríamos", "habría", "habrías"], "Los vecinos → habrían.", tr="Nobody answered. The neighbors had probably gone out.", lemma="haber:ellos:cond"),
        F("El tren no llegó. ___ habido un problema.", "Habría", ["Habrían", "Habríamos", "Habrías"], "Impersonal haber stays singular.", tr="The train did not arrive. There must have been a problem.", lemma="haber:él:cond"),
        F("Juan no vino. Se habría ___.", "enfermado", ["enfermando", "enfermar", "enfermó"], "Participle of enfermar.", tr="Juan did not come. He had probably gotten sick."),
        F("Mi hermana no llamó. Habría ___ el teléfono en casa.", "dejado", ["dejar", "dejando", "dejó"], "Participle of dejar.", tr="My sister did not call. She probably left her phone at home.", lemma="dejar:part"),
        F("Los niños no estaban en casa. Habrían ___ al parque.", "ido", ["ir", "yendo", "iban"], "Participle of ir.", tr="The children were not at home. They had probably gone to the park.", lemma="ir:part"),
        F("Llegaron muy cansados. Ellos ___ caminado mucho.", "habrían", ["habríamos", "habrías", "habría"], "Ellos → habrían.", tr="They arrived very tired. They had probably walked a lot.", lemma="haber:ellos:cond"),
    ],
    verify=vpd("haber", "habría", "habrías", "habría", "habríamos", "habríais", "habrían") + vpa("estar", "estado") + vpa("dejar", "dejado") + vpa("ir", "ido"),
)

# ---------------------------------------------------------------------------- 830
L830 = lesson(
    "The pluperfect subjunctive: hubiera comido, hubiese comido",
    "Si hubiera comido, no tendría hambre. Si hubiésemos llegado antes, habríamos visto la película.",
    requires=["haber", "comer", "llegar", "decir", "salir", "ganar", "estudiar", "saber", "película", "hambre", "verdad", "antes"],
    cards=[
        card("How to form it",
             "The pluperfect subjunctive uses haber in the imperfect subjunctive + a past participle. Like the imperfect subjunctive, it has two forms: the -ra forms (hubiera) and the -se forms (hubiese). Both mean the same thing. "
             "It is used mostly after si when you imagine something in the past that did not happen, and after expressions of wish or regret.",
             tables=[table(["Persona", "Forma -ra", "Forma -se"],
                           [["yo", "hubiera comido", "hubiese comido"], ["tú", "hubieras comido", "hubieses comido"],
                            ["él / ella / usted", "hubiera comido", "hubiese comido"], ["nosotros", "hubiéramos comido", "hubiésemos comido"],
                            ["vosotros", "hubierais comido", "hubieseis comido"], ["ellos / ustedes", "hubieran comido", "hubiesen comido"]],
                           say=[1, 2])]),
        card("A first look at use",
             "The most common pattern is si + pluperfect subjunctive, then the conditional perfect. You will practice it in the next lessons.",
             examples=[
                 ex("Si hubieras salido antes, habrías llegado a tiempo.", "If you had left earlier, you would have arrived on time.", "hubieras salido"),
                 ex("Si hubiésemos sabido eso, habríamos llamado.", "If we had known that, we would have called.", "hubiésemos sabido"),
             ]),
    ],
    exercises=[
        M("Which is the pluperfect subjunctive of “comer” (yo)?", "hubiera comido", ["he comido", "había comido", "habría comido"], "Hubiera + participle."),
        M("Which one is an -se form?", "hubiese comido", ["hubiera comido", "habría comido", "había comido"], "Hubiese."),
        M("What are the two parts of the pluperfect subjunctive?", "Haber in the imperfect subjunctive + a past participle", ["Haber in the preterite + an infinitive", "Ser + a gerund", "Estar + a participle"], "Hubiera/hubiese + participle."),
        F("Si nosotros ___ llegado antes, habríamos visto la película.", "hubiéramos", ["hubieran", "hubiera", "hubierais"], "Nosotros → hubiéramos.", tr="If we had arrived earlier, we would have seen the movie.", lemma="haber:nosotros:isubj"),
        F("Si ella ___ dicho la verdad, nadie se habría enojado.", "hubiera", ["hubieran", "hubieras", "hubiéramos"], "Ella → hubiera.", tr="If she had told the truth, nobody would have gotten angry.", lemma="haber:ella:isubj"),
        F("Si tú ___ salido antes, habrías llegado a tiempo.", "hubieras", ["hubiera", "hubieran", "hubierais"], "Tú → hubieras.", tr="If you had left earlier, you would have arrived on time.", lemma="haber:tú:isubj"),
        F("Si ellos ___ ganado, habrían celebrado.", "hubieran", ["hubiera", "hubieras", "hubiéramos"], "Ellos → hubieran.", tr="If they had won, they would have celebrated.", lemma="haber:ellos:isubj"),
        F("Si yo hubiese ___ más, habría aprobado.", "estudiado", ["estudiar", "estudiando", "estudié"], "Participle of estudiar.", tr="If I had studied more, I would have passed.", lemma="estudiar:part"),
        F("Si usted ___ sabido eso, habría llamado.", "hubiese", ["hubiesen", "hubieses", "hubiésemos"], "Usted → hubiese.", tr="If you (formal) had known that, you would have called.", lemma="haber:usted:isubjse"),
    ],
    verify=(vpq("haber", "hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran")
            + vpqs("haber", "hubiese", "hubieses", "hubiese", "hubiésemos", "hubieseis", "hubiesen")),
)

# ---------------------------------------------------------------------------- 831
L831 = lesson(
    "Si + pluperfect subjunctive: Si hubiera estudiado, habría aprobado",
    "Si hubiera estudiado, habría aprobado. Habríamos viajado si hubiéramos tenido dinero.",
    requires=["estudiar", "aprobar", "salir", "llegar", "llamar", "decir", "viajar", "perder", "tren", "examen", "dinero", "tiempo"],
    cards=[
        card("Imagining a different past",
             "To talk about a past event that did not happen, and what would have followed, use this pattern: si + pluperfect subjunctive, then the conditional perfect. "
             "The clause with si can come first or second. In an if-clause that imagines the past, do not use habría right after si; use hubiera or hubiese.",
             tables=[table(["Si + hubiera + participio", "Habría + participio"],
                           [["Si hubiera estudiado,", "habría aprobado."],
                            ["Si hubieras salido antes,", "habrías llegado a tiempo."],
                            ["Si no hubiéramos perdido el tren,", "habríamos llegado a tiempo."],
                            ["Si me hubieras llamado,", "te habría ayudado."]],
                           say=[0, 1])]),
        card("Order of the clauses",
             "You can switch the two parts. The verb forms stay the same, and you do not need a comma when the si-clause comes last.",
             examples=[
                 ex("Habríamos viajado si hubiéramos tenido dinero.", "We would have traveled if we had had money.", "hubiéramos tenido"),
             ]),
    ],
    exercises=[
        M("Which sentence is correct?", "Si hubiera estudiado, habría aprobado.", ["Si habría estudiado, habría aprobado.", "Si habría estudiado, aprobaría.", "Si he estudiado, habría aprobado."], "Standard Spanish uses si + hubiera, not si + habría."),
        M("What does the si-clause express in this pattern?", "Something that did not happen in the past", ["A real habit", "A future plan", "A present fact"], "An unreal past."),
        M("Can habría appear in the si-clause?", "No, not with this meaning", ["Yes, always", "Yes, but only in questions", "Only with ser"], "Hubiera goes in the si-clause."),
        F("Si yo ___ estudiado más, habría aprobado.", "hubiera", ["habría", "había", "hubieras"], "Yo → hubiera.", tr="If I had studied more, I would have passed.", lemma="haber:yo:isubj"),
        F("Si ellos ___ salido temprano, habrían llegado a tiempo.", "hubieran", ["hubiera", "hubiéramos", "habrían"], "Ellos → hubieran.", tr="If they had left early, they would have arrived on time.", lemma="haber:ellos:isubj"),
        F("Si no hubiéramos perdido el tren, ___ llegado a tiempo.", "habríamos", ["habíamos", "hemos", "habremos"], "Result clause: habríamos.", tr="If we had not missed the train, we would have arrived on time.", lemma="haber:nosotros:cond"),
        F("Si tú me hubieras ___, te habría ayudado.", "llamado", ["llamar", "llamando", "llamabas"], "Participle of llamar.", tr="If you had called me, I would have helped you.", lemma="llamar:part"),
        F("Si ella hubiera ___ la verdad, no habría pasado nada.", "dicho", ["decido", "diciendo", "dijo"], "Participle of decir.", tr="If she had told the truth, nothing would have happened.", lemma="decir:part"),
        F("Habríamos viajado si ___ tenido dinero.", "hubiéramos", ["habríamos", "habíamos", "hemos"], "Si + hubiéramos.", tr="We would have traveled if we had had money.", lemma="haber:nosotros:isubj"),
    ],
    verify=vpd("haber", "habría", "habrías", "habría", "habríamos", "habríais", "habrían") + vpq("haber", "hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran"),
)

# ---------------------------------------------------------------------------- 832
L832 = lesson(
    "Past cause, present result: Si hubiera estudiado, ahora sería médico",
    "Si hubiera estudiado medicina, ahora sería médico. Si no hubieran vendido la casa, todavía vivirían allí.",
    requires=["estudiar", "vender", "escuchar", "ahorrar", "viajar", "vivir", "ser", "tener", "poder", "hablar", "médico", "ahora", "todavía", "problema"],
    cards=[
        card("A different past, a different present",
             "Sometimes an imagined past event would change how things are now. In that case, the si-clause uses the pluperfect subjunctive (past), and the result clause uses the simple conditional (present). "
             "Words like ahora and todavía show that the result belongs to the present.",
             tables=[table(["Si + pasado irreal", "Resultado en el presente"],
                           [["Si hubiera estudiado medicina,", "ahora sería médico."],
                            ["Si no hubieran vendido la casa,", "todavía vivirían allí."],
                            ["Si me hubieras escuchado,", "ahora no tendría este problema."],
                            ["Si hubiéramos ahorrado más,", "ahora podríamos comprar una casa."]],
                           say=[0, 1])]),
        card("Pattern at a glance",
             "Past cause: hubiera + participle. Present result: simple conditional. Compare with the previous lesson, where both parts looked at the past.",
             examples=[
                 ex("Si hubieras vivido en París, ahora hablarías francés.", "If you had lived in Paris, you would speak French now.", "hablarías"),
             ]),
    ],
    exercises=[
        M("What does “Si hubiera estudiado medicina, ahora sería médico” mean?", "A past event that did not happen would change the present", ["Both parts are in the future", "Both parts are in the past", "It is a real fact"], "Mixed time."),
        M("Which time word usually signals a present result?", "ahora", ["ayer", "anoche", "el año pasado"], "Ahora = now."),
        M("Which form usually follows the si-clause when the result is now?", "The simple conditional (sería)", ["The conditional perfect (habría sido)", "The present (soy)", "The future (seré)"], "Simple conditional for a present result."),
        F("Si hubiera estudiado medicina, ahora ___ médico.", "sería", ["fui", "soy", "seré"], "Present result → conditional.", tr="If I had studied medicine, I would be a doctor now.", lemma="ser:yo:cond"),
        F("Si no hubieran vendido la casa, todavía ___ allí.", "vivirían", ["vivieron", "viven", "vivirán"], "Ellos → vivirían.", tr="If they had not sold the house, they would still live there.", lemma="vivir:ellos:cond"),
        F("Si me hubieras escuchado, ahora no ___ este problema.", "tendría", ["tuve", "tengo", "tendré"], "Yo → tendría.", tr="If you had listened to me, I would not have this problem now.", lemma="tener:yo:cond"),
        F("Si ella hubiera aprendido inglés, ahora ___ en esa empresa.", "trabajaría", ["trabajó", "trabaja", "trabajará"], "Ella → trabajaría.", tr="If she had learned English, she would work at that company now.", lemma="trabajar:ella:cond"),
        F("Si hubiéramos ahorrado más, ahora ___ comprar una casa.", "podríamos", ["pudimos", "podemos", "podremos"], "Nosotros → podríamos.", tr="If we had saved more, we could buy a house now.", lemma="poder:nosotros:cond"),
        F("Si hubieras vivido en París, ahora ___ francés.", "hablarías", ["hablaste", "hablas", "hablarás"], "Tú → hablarías.", tr="If you had lived in Paris, you would speak French now.", lemma="hablar:tú:cond"),
    ],
    verify=vpd("ser", "sería", "serías", "sería", "seríamos", "seríais", "serían") + vpd("poder", "podría", "podrías", "podría", "podríamos", "podríais", "podrían"),
)

# ---------------------------------------------------------------------------- 833
L833 = lesson(
    "Speaking naturally: hubiera in both halves, hubiese and habría",
    "Si lo hubiera sabido, hubiera ido. Si lo hubiese sabido, habría ido.",
    requires=["haber", "saber", "ir", "venir", "llegar", "ayudar", "avisar", "pensar", "fiesta", "error", "partido"],
    cards=[
        card("What you will hear",
             "In this kind of si-clause (imagined past), only the pluperfect subjunctive is standard (hubiera or hubiese). In the result clause, careful and written Spanish uses habría + participle. "
             "In speech, many people use hubiera + participle in the result clause too (Si lo hubiera sabido, hubiera ido). You will hear this a lot, but in formal writing prefer habría.",
             tables=[table(["Cláusula con si", "Resultado: formal", "Resultado: oral"],
                           [["Si lo hubiera sabido,", "habría ido.", "hubiera ido."],
                            ["Si lo hubiese sabido,", "habría ido.", "hubiese ido."],
                            ["Si hubieran llegado antes,", "habrían visto el partido.", "hubieran visto el partido."]],
                           say=[0, 1, 2])]),
        card("Hubiera or hubiese?",
             "There is almost no difference between them. Hubiera is more common in many places, and hubiese sounds a little more formal or literary. Pick one and use it consistently.",
             examples=[
                 ex("Si ella lo hubiese pensado mejor, no habría cometido ese error.", "If she had thought it over better, she would not have made that mistake.", "hubiese pensado"),
             ]),
    ],
    exercises=[
        M("Which form can replace habría in the result clause when people speak?", "hubiera", ["había", "hubo", "hube"], "Spoken Spanish often uses hubiera there."),
        M("Which form is not used in the si-clause of this pattern?", "habría", ["hubiera", "hubiese", "hubieran"], "Si + habría is not standard."),
        M("What is the difference between hubiera and hubiese?", "Almost none; hubiera is more common", ["Hubiese is the future", "Hubiese is only for questions", "Hubiera is only plural"], "Two forms, same meaning."),
        F("Si Pedro lo hubiera sabido, él ___ venido a la fiesta.", "hubiera", ["hubieran", "hubieras", "hubiéramos"], "Spoken Spanish: hubiera.", tr="If Pedro had known, he would have come to the party.", lemma="haber:él:isubj"),
        F("Si me lo hubieses dicho, yo ___ ayudado.", "habría", ["habríamos", "habrían", "habrías"], "Yo → habría.", tr="If you had told me, I would have helped.", lemma="haber:yo:cond"),
        F("Si lo hubiésemos sabido, nosotros ___ avisado.", "habríamos", ["habrían", "habría", "habríais"], "Nosotros → habríamos.", tr="If we had known, we would have let you know.", lemma="haber:nosotros:cond"),
        F("Si ellos hubiesen llegado antes, ___ visto el partido.", "habrían", ["habríamos", "habrías", "habría"], "Ellos → habrían.", tr="If they had arrived earlier, they would have seen the game.", lemma="haber:ellos:cond"),
        F("Si tú no hubieses salido, no te ___ mojado.", "habrías", ["habrían", "habríamos", "habría"], "Tú → habrías.", tr="If you had not gone out, you would not have gotten wet.", lemma="haber:tú:cond"),
        F("Si ella lo hubiese pensado mejor, no ___ cometido ese error.", "habría", ["habrían", "habríamos", "habrías"], "Ella → habría.", tr="If she had thought it over better, she would not have made that mistake.", lemma="haber:ella:cond"),
    ],
    verify=vpd("haber", "habría", "habrías", "habría", "habríamos", "habríais", "habrían") + vpq("haber", "hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran") + vpqs("haber", "hubiese", "hubieses", "hubiese", "hubiésemos", "hubieseis", "hubiesen"),
)

# ---------------------------------------------------------------------------- 834
L834 = lesson(
    "Three kinds of si-sentences: real, imagined now, imagined past",
    "Si estudio, apruebo. Si estudiara, aprobaría. Si hubiera estudiado, habría aprobado.",
    requires=["llover", "ir", "estudiar", "tener", "vivir", "estar", "llegar", "ver", "dinero", "coche", "parque", "película"],
    cards=[
        card("One idea, three levels of reality",
             "Spanish si-sentences change their verbs depending on how real the situation is. Real or likely things use the indicative. Imagined things in the present or future use the imperfect subjunctive and the conditional. "
             "Imagined things in the past use the pluperfect subjunctive and the conditional perfect.",
             tables=[table(["Tipo", "Si-clause", "Resultado"],
                           [["Real / probable", "Si estudio,", "apruebo."],
                            ["Imaginado (ahora)", "Si estudiara,", "aprobaría."],
                            ["Imaginado (pasado)", "Si hubiera estudiado,", "habría aprobado."]],
                           say=[1, 2])]),
        card("Never after si",
             "In conditional si-clauses, do not use the present subjunctive, the future or the conditional after si. (In indirect questions such as No sé si vendrá, si can take the future.) The only subjunctive forms after si are the imperfect (estudiara) and the pluperfect (hubiera estudiado).",
             examples=[
                 ex("Si llueve mañana, no iremos al parque.", "If it rains tomorrow, we will not go to the park.", "Si llueve"),
                 ex("Si tuviera más dinero, compraría un coche.", "If I had more money, I would buy a car.", "tuviera"),
                 ex("Si hubiera tenido más dinero, habría comprado un coche.", "If I had had more money, I would have bought a car.", "hubiera tenido"),
             ]),
    ],
    exercises=[
        M("Which sentence imagines something that did not happen in the past?", "Si hubiera estudiado, habría aprobado.", ["Si estudiara, aprobaría.", "Si estudio, apruebo.", "Si estudiaré, aprobaré."], "Pluperfect subjunctive + conditional perfect."),
        M("Which sentence imagines an unreal present situation?", "Si tuviera tiempo, viajaría.", ["Si tengo tiempo, viajaré.", "Si hubiera tenido tiempo, habría viajado.", "Si tenía tiempo, viajaba."], "Imperfect subjunctive + conditional."),
        M("Which verb form can never follow si in these patterns?", "The present subjunctive", ["The present indicative", "The imperfect subjunctive", "The pluperfect subjunctive"], "Not after si."),
        F("Si llueve mañana, no ___ al parque.", "iremos", ["iríamos", "hubiéramos ido", "habríamos ido"], "Real situation → future.", tr="If it rains tomorrow, we will not go to the park.", lemma="ir:nosotros:fut"),
        F("Si yo ___ más dinero, compraría un coche.", "tuviera", ["tengo", "tendré", "hubiera tenido"], "Imagined present → imperfect subjunctive.", tr="If I had more money, I would buy a car.", lemma="tener:yo:isubj"),
        F("Si yo ___ más dinero, habría comprado un coche.", "hubiera tenido", ["tuviera", "tengo", "tendré"], "Imagined past → pluperfect subjunctive.", tr="If I had had more money, I would have bought a car."),
        F("Si ellos ___ aquí, te ayudarían.", "estuvieran", ["estarían", "estarán", "estén"], "Imagined present.", tr="If they were here, they would help you.", lemma="estar:ellos:isubj"),
        F("Si hubieran llegado antes, ___ visto la película completa.", "habrían", ["habríamos", "habrías", "habría"], "Ellos → habrían.", tr="If they had arrived earlier, they would have seen the whole movie.", lemma="haber:ellos:cond"),
        F("Si ella ___ cerca, nos visitaría.", "viviera", ["viviría", "vivirá", "viva"], "Imagined present.", tr="If she lived nearby, she would visit us.", lemma="vivir:ella:isubj"),
    ],
    verify=vpq("tener", "tuviera", "tuvieras", "tuviera", "tuviéramos", "tuvierais", "tuvieran") + vpq("estar", "estuviera", "estuvieras", "estuviera", "estuviéramos", "estuvierais", "estuvieran"),
)

# ---------------------------------------------------------------------------- 835
L835 = lesson(
    "Reading: ¿Qué habría pasado si el tren hubiera llegado? (invented text)",
    "Un pueblo imaginario se pregunta cómo habría cambiado su historia.",
    requires=["pueblo", "tren", "estación", "mercado", "crecer", "tienda", "cliente", "joven", "buscar", "trabajo", "historiador", "agricultor"],
    cards=[
        card("Texto inventado, primera parte",
             "This text is invented for practice. Valdeluna is an imaginary village.",
             examples=[
                 ex("En el pueblo de Valdeluna nunca hubo estación de tren.", "In the village of Valdeluna there was never a train station.", "nunca hubo"),
                 ex("Hace casi cien años se habló de una línea de tren, pero al final pasó por otra ciudad.", "Almost a hundred years ago people talked about a railway line, but in the end it went through another city.", "pasó por otra ciudad"),
                 ex("Hoy muchos se preguntan qué habría pasado si el tren hubiera llegado al pueblo.", "Today many wonder what would have happened if the train had reached the village.", "habría pasado"),
                 ex("Algunos dicen que el mercado habría crecido y que las tiendas habrían tenido más clientes.", "Some say the market would have grown and the shops would have had more customers.", "habría crecido"),
                 ex("Otros creen que los jóvenes no habrían salido a buscar trabajo en la capital.", "Others think young people would not have left to look for work in the capital.", "no habrían salido"),
             ]),
        card("Texto inventado, segunda parte",
             "A local historian offers a different view.",
             examples=[
                 ex("Si la estación hubiera existido, quizás hoy el pueblo sería más grande.", "If the station had existed, perhaps the village would be bigger today.", "hubiera existido"),
                 ex("Pero un historiador local dice que también habrían llegado productos baratos y los agricultores habrían tenido dificultades.", "But a local historian says cheap products would also have arrived and the farmers would have had difficulties.", "habrían llegado"),
                 ex("Nadie puede saberlo con seguridad.", "Nobody can know it for sure.", "saberlo"),
             ]),
    ],
    exercises=[
        M("Why does Valdeluna have no train station?", "The planned railway line went through another city", ["It was destroyed in a fire", "The villagers refused it", "It was built and then closed"], "“Nunca hubo estación.”"),
        M("What do some people think would have happened to the market?", "It would have grown", ["It would have closed", "It would have moved", "It would have stayed the same"], "El mercado habría crecido."),
        M("What does the local historian point out?", "Cheap products could have hurt local farmers", ["The shops would have closed at once", "The capital would have been smaller", "The young people would have returned"], "Productos baratos."),
        M("What does the last sentence say?", "Nobody can know for sure", ["Everyone agrees", "The train will arrive soon", "The historian was wrong"], "Nadie puede saberlo con seguridad."),
        F("El mercado ___ crecido.", "habría", ["habríamos", "habrías", "habrían"], "Singular subject.", tr="The market would have grown.", lemma="haber:él:cond"),
        F("Si el tren ___ llegado, el pueblo sería más grande.", "hubiera", ["habría", "había", "hubieras"], "Si + hubiera.", tr="If the train had arrived, the village would be bigger.", lemma="haber:él:isubj"),
        F("Las tiendas habrían ___ más clientes.", "tenido", ["tener", "teniendo", "tuvieron"], "Participle of tener.", tr="The shops would have had more customers.", lemma="tener:part"),
        F("Los jóvenes no habrían ___ a buscar trabajo.", "salido", ["salir", "saliendo", "salieron"], "Participle of salir.", tr="The young people would not have left to look for work.", lemma="salir:part"),
        F("Los agricultores ___ tenido dificultades.", "habrían", ["habríamos", "habría", "habrías"], "Plural subject.", tr="The farmers would have had difficulties.", lemma="haber:ellos:cond"),
    ],
    verify=vpd("haber", "habría", "habrías", "habría", "habríamos", "habríais", "habrían") + vpa("tener", "tenido") + vpa("salir", "salido"),
)
UNIT = unit("Arte y literatura", [L808, L809, L810, L811, L812, L813, L814, L815, L816, L817, L818, L819, L820, L821, L822, L823, L824, L825, L826, L827, L828, L829, L830, L831, L832, L833, L834, L835])

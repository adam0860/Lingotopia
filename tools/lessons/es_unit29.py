"""Unit 29: cybercrime, money crimes, trafficking, doubt and negation (textbook Chapter 29)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 584
L584 = lesson(
    "Cybercrime words: malware, virus, ransomware…",
    "Un virus puede dañar tu computadora.",
    requires=["virus", "programa", "computadora", "dispositivo", "correo", "electrónico", "enlace", "archivo", "usuario", "ataque", "rescate", "proteger"],
    cards=[
        card("Types of harmful programs",
             "Malware (also called programa malicioso) is any software made to cause harm. Spanish uses both English loanwords and Spanish terms. "
             "This lesson gives vocabulary only, so you can read the news and protect yourself.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el malware, el programa malicioso", "malware", "El malware daña los dispositivos."],
                            ["el virus", "virus", "Un virus puede dañar tu computadora."],
                            ["el gusano", "worm", "Un gusano se copia a sí mismo y se propaga rápido."],
                            ["el troyano", "Trojan", "Un troyano parece un programa normal, pero no lo es."],
                            ["el programa espía", "spyware", "Un programa espía roba datos del usuario."],
                            ["el ransomware, el secuestro de datos", "ransomware", "El ransomware bloquea los archivos y pide un rescate."],
                            ["el phishing, la suplantación de identidad", "phishing", "El phishing llega por correo electrónico o por mensajes."],
                            ["el antivirus", "antivirus", "Un antivirus ayuda a protegerte."]],
                           say=[2])]),
    ],
    exercises=[
        M("Which program blocks your files and asks for a ransom?", "ransomware", ["antivirus", "gusano", "enlace"], "El ransomware pide un rescate."),
        M("Which program steals data without the user knowing?", "un programa espía", ["un antivirus", "un archivo", "un usuario"], "Spyware = programa espía."),
        M("What does a worm do?", "It copies itself and spreads fast", ["It cleans files", "It repairs the screen", "It sends a bill"], "El gusano se copia y se propaga."),
        F("Un ___ parece un programa normal, pero no lo es.", "troyano", ["antivirus", "usuario", "archivo"], "Troyano = Trojan horse.", tr="A Trojan looks like a normal program, but it is not."),
        F("El ___ llega por correo electrónico y pide datos personales.", "phishing", ["troyano", "antivirus", "rescate"], "Phishing = a fake message that impersonates a trusted sender to steal data.", tr="Phishing arrives by email and asks for personal data."),
        F("Un ___ ayuda a proteger tu computadora.", "antivirus", ["gusano", "troyano", "rescate"], "Antivirus = protection.", tr="An antivirus helps protect your computer."),
        F("Un virus puede ___ tu computadora.", "dañar", ["daña", "dañan", "dañé"], "Poder + infinitive.", tr="A virus can damage your computer."),
        F("El ransomware bloquea los archivos y pide un ___.", "rescate", ["enlace", "usuario", "antivirus"], "Rescate = ransom.", tr="Ransomware blocks the files and asks for a ransom."),
        M("What does “el correo electrónico” mean?", "email", ["a post office", "a telephone", "a screen"], "Correo electrónico = email."),
    ],
)

# ---------------------------------------------------------------------------- 585
L585 = lesson(
    "Who is behind it? Hackers, cybercriminals, hacktivists",
    "Hay hackers que ayudan a proteger los sistemas.",
    requires=["pirata", "criminal", "delincuente", "gobierno", "empresa", "dinero", "información", "político", "terrorismo", "espía", "red", "actividad"],
    cards=[
        card("Four kinds of cyberthreats",
             "Analysts distinguish groups by their motive. Notice that a hacker is a person with advanced computer skills; some work legally to find weaknesses and help fix them (hacker ético). A person who breaks into other people’s systems illegally is called un pirata informático.",
             tables=[table(["Amenaza", "Motivo", "Ejemplo"],
                           [["la ciberdelincuencia", "dinero", "Grupos criminales roban datos y piden rescates."],
                            ["el ciberespionaje", "información secreta", "Algunos gobiernos o empresas espían a otros."],
                            ["el hacktivismo", "protesta política o social", "Los hacktivistas usan herramientas digitales para protestar."],
                            ["el ciberterrorismo", "causar miedo para lograr fines políticos", "Es una amenaza que los gobiernos vigilan de cerca."]],
                           say=[2])]),
        card("Law and responsibility",
             "A person who pays a hacker to commit a crime is also responsible; many legal systems can punish both. The details depend on each country.",
             examples=[
                 ex("Un hacker es una persona con conocimientos avanzados de computación.", "A hacker is a person with advanced computer knowledge.", "conocimientos"),
                 ex("Hay hackers éticos que ayudan a las empresas a encontrar errores en sus sistemas.", "There are ethical hackers who help companies find mistakes in their systems.", "éticos"),
                 ex("La ciberdelincuencia busca dinero, y el ciberespionaje busca información.", "Cybercrime looks for money, and cyberespionage looks for information.", "busca"),
             ]),
    ],
    exercises=[
        M("What motivates cybercrime?", "Money", ["Fun", "Weather", "Language learning"], "Dinero."),
        M("What does cyberespionage look for?", "Secret information", ["Ransom", "Votes", "Holidays"], "Información secreta."),
        M("What is hacktivism?", "Digital protest for political or social goals", ["A kind of virus", "A bank", "A game"], "Protesta política o social."),
        M("Is every hacker a criminal?", "No: some ethical hackers help find weaknesses", ["Yes, always", "Only in Spain", "Only on weekends"], "Hay hackers éticos."),
        F("La ___ busca dinero.", "ciberdelincuencia", ["ciberespionaje", "hacktivismo", "privacidad"], "Motive: money.", tr="Cybercrime looks for money."),
        F("El ___ busca información secreta.", "ciberespionaje", ["hacktivismo", "rescate", "antivirus"], "Motive: secret information.", tr="Cyberespionage looks for secret information."),
        F("Los hacktivistas ___ herramientas digitales para protestar.", "usan", ["usa", "usar", "usamos"], "Plural subject, present.", tr="Hacktivists use digital tools to protest.", lemma="usar:ellos"),
        F("Algunos hackers éticos ___ a las empresas.", "ayudan", ["ayuda", "ayudar", "ayudamos"], "Plural subject, present.", tr="Some ethical hackers help companies.", lemma="ayudar:ellos"),
        M("Which word names a hacker who breaks into systems illegally?", "pirata informático", ["usuario", "antivirus", "gusano"], "Pirata informático."),
    ],
)

# ---------------------------------------------------------------------------- 586
L586 = lesson(
    "Famous cyberattacks: ILOVEYOU and WannaCry",
    "En mayo de dos mil diecisiete, el ransomware WannaCry afectó a muchos países.",
    requires=["mayo", "correo", "electrónico", "archivo", "computadora", "empresa", "hospital", "rescate", "país", "mundo", "seguridad", "millón"],
    cards=[
        card("Two well-known cases",
             "These summaries are in general terms. They show how fast harmful programs can spread.",
             examples=[
                 ex("En mayo de dos mil, un gusano llamado ILOVEYOU se propagó por correo electrónico.", "In May 2000 a worm called ILOVEYOU spread by email.", "se propagó"),
                 ex("El mensaje parecía una carta de amor y tenía un archivo adjunto.", "The message looked like a love letter and had an attached file.", "tenía"),
                 ex("Cuando la gente abría el archivo, el gusano se enviaba a los contactos de su libreta de direcciones.", "When people opened the file, the worm sent itself to the contacts in their address books.", "se enviaba"),
                 ex("Millones de computadoras en todo el mundo resultaron afectadas.", "Millions of computers around the world were affected.", "resultaron"),
                 ex("El doce de mayo de dos mil diecisiete, el ransomware WannaCry empezó a infectar equipos en muchos países.", "On May 12, 2017 the WannaCry ransomware began infecting computers in many countries.", "empezó"),
                 ex("Según los informes, afectó a más de doscientos mil equipos en más de cien países.", "According to reports, it affected more than 200,000 computers in more than 100 countries.", "afectó"),
                 ex("Bloqueó los archivos de hospitales, empresas y usuarios, y pidió un rescate en criptomonedas.", "It locked the files of hospitals, companies and users, and demanded a ransom in cryptocurrency.", "pidió"),
                 ex("Después de estos casos, muchas empresas mejoraron su seguridad.", "After these cases, many companies improved their security.", "mejoraron"),
             ]),
    ],
    exercises=[
        M("How did ILOVEYOU spread?", "By email, with an attached file", ["By radio", "By mail", "By telephone line"], "Se propagó por correo electrónico."),
        M("What kind of program was ILOVEYOU?", "A worm", ["An antivirus", "A game", "A search engine"], "Un gusano."),
        M("What did WannaCry do?", "It locked files and demanded a ransom", ["It deleted the Internet", "It paid users", "It repaired computers"], "Bloqueó los archivos y pidió un rescate."),
        M("What kind of payment did WannaCry demand?", "In cryptocurrency", ["In gold", "In checks", "In stamps"], "Pidió un rescate en criptomonedas."),
        F("En mayo de dos mil, un gusano ___ por correo electrónico.", "se propagó", ["se propagaron", "se propaga", "propagarse"], "Singular subject; dated event.", tr="In May 2000 a worm spread by email."),
        F("El ransomware WannaCry ___ a más de cien países.", "afectó", ["afectaron", "afecta", "afectar"], "Singular subject; finished past.", tr="The WannaCry ransomware affected more than a hundred countries.", lemma="afectar:él:pret"),
        F("Los hospitales perdieron el acceso a sus ___.", "archivos", ["rescates", "gusanos", "países"], "Archivos = files.", tr="The hospitals lost access to their files."),
        F("Después de esos casos, muchas empresas ___ su seguridad.", "mejoraron", ["mejoró", "mejoran", "mejorar"], "Plural subject; finished past.", tr="After those cases, many companies improved their security.", lemma="mejorar:ellos:pret"),
        M("Why do experts tell people not to open unknown attachments?", "A harmful file can spread through the contacts", ["Attachments are expensive", "Email is slow", "Files are always large"], "El gusano se enviaba a los contactos."),
    ],
)

# ---------------------------------------------------------------------------- 587
L587 = lesson(
    "Staying safe online: tips with commands",
    "Usa una contraseña distinta para cada servicio. No abras enlaces sospechosos.",
    requires=["usar", "abrir", "actualizar", "hacer", "clave", "copia", "enlace", "seguridad", "red", "privado", "verificar"],
    cards=[
        card("Safety advice",
             "Experts give advice with commands (tú: Usa…, No abras…) or with impersonal expressions (Es importante que uses…). Here is a short list of common recommendations.",
             tables=[table(["Consejo", "English"],
                           [["Usa una contraseña distinta para cada servicio.", "Use a different password for each service."],
                            ["Activa la verificación en dos pasos.", "Turn on two-step verification."],
                            ["Actualiza tus programas con frecuencia.", "Update your programs often."],
                            ["Haz copias de seguridad de tus archivos.", "Make backups of your files."],
                            ["No abras enlaces ni archivos sospechosos.", "Don't open suspicious links or files."],
                            ["No uses una red pública sin protección.", "Don't use an unprotected public network."],
                            ["Revisa los permisos de las aplicaciones.", "Check the apps' permissions."],
                            ["Desconfía de los mensajes que piden datos con urgencia.", "Distrust messages that urgently ask for data."]],
                           say=[0])]),
    ],
    exercises=[
        F("___ una contraseña distinta para cada servicio.", "Usa", ["Usas", "Uses", "Usando"], "Affirmative tú command.", tr="Use a different password for each service.", lemma="usar:tú:tcmd"),
        F("No ___ enlaces sospechosos.", "abras", ["abres", "abre", "abriendo"], "Negative tú command.", tr="Don't open suspicious links.", lemma="abrir:tú:ntcmd"),
        F("___ copias de seguridad de tus archivos.", "Haz", ["Hace", "Hagas", "Haciendo"], "Affirmative tú command of hacer.", tr="Make backups of your files.", lemma="hacer:tú:tcmd"),
        F("___ tus programas con frecuencia.", "Actualiza", ["Actualizas", "Actualices", "Actualizando"], "Affirmative tú command.", tr="Update your programs often.", lemma="actualizar:tú:tcmd"),
        F("Es importante que tú ___ la verificación en dos pasos.", "actives", ["activas", "activar", "active"], "Es importante que + subjunctive; tú.", tr="It is important that you turn on two-step verification.", lemma="activar:tú:subj"),
        F("Es esencial que nosotros ___ los permisos de las aplicaciones.", "revisemos", ["revisamos", "revisar", "revisen"], "Es esencial que + subjunctive; nosotros.", tr="It is essential that we check the apps' permissions.", lemma="revisar:nosotros:subj"),
        F("Es indispensable que los usuarios no ___ datos personales a desconocidos.", "den", ["dan", "dar", "damos"], "Es indispensable que + subjunctive.", tr="It is essential that users not give personal data to strangers.", lemma="dar:ellos:subj"),
        M("Which tip is about protecting your files in case of loss?", "Haz copias de seguridad.", ["Cambia de color.", "Compra un teléfono.", "Apaga el reloj."], "Copias de seguridad = backups."),
        M("Which sentence is a negative command?", "No uses una red pública sin protección.", ["Usa una red pública.", "Usas una red pública.", "Vas a usar una red pública."], "No + subjunctive-form command."),
    ],
)

# ---------------------------------------------------------------------------- 588
L588 = lesson(
    "Cultural note: the RAE and new words",
    "La RAE ya ha aceptado palabras como tuit y bloguero.",
    requires=["palabra", "diccionario", "académico", "uso", "tecnología", "idioma", "extranjero", "nuevo", "pueblo", "inglés", "frecuente", "equivalente"],
    cards=[
        card("How does a word enter the dictionary?",
             "The Real Academia Española (RAE) and the other academies of the Spanish language publish the dictionary. When a new word becomes common, the academies check whether Spanish already has a word for the same thing. "
             "If it does, they discuss whether the foreign word also needs a place. If no Spanish word has succeeded, they may accept the loanword. Many technology words have been added.",
             examples=[
                 ex("La tecnología avanza rápido y el idioma crea palabras nuevas.", "Technology advances quickly and the language creates new words.", "avanza"),
                 ex("La RAE ya ha aceptado palabras como tableta, tuit, tuitear y bloguero.", "The RAE has already accepted words like tableta, tuit, tuitear and bloguero.", "ha aceptado"),
                 ex("Para wifi existe también la expresión conexión inalámbrica.", "For wifi there is also the expression conexión inalámbrica (wireless connection).", "inalámbrica"),
                 ex("Software y hardware son palabras inglesas que se usan mucho, aunque también existen alternativas como programa y equipo.", "Software and hardware are English words that are widely used, although alternatives such as programa and equipo also exist.", "se usan"),
                 ex("Los académicos dicen que el idioma pertenece a los hablantes.", "The academics say that the language belongs to its speakers.", "pertenece"),
             ]),
    ],
    exercises=[
        M("When does the RAE consider adding a new word?", "When the word becomes frequent in use", ["When a minister asks", "When it is short", "When it is spelled with k"], "Detecta el uso frecuente."),
        M("What does the RAE check first?", "Whether a Spanish word already exists", ["Whether it is polite", "Whether it has an accent", "Whether it is long"], "Revisa si ya existe un vocablo."),
        M("According to the text, to whom does the language belong?", "To its speakers", ["To the academies only", "To one country", "To the press"], "Pertenece a los hablantes."),
        F("La RAE ya ___ palabras como tuit y bloguero.", "ha aceptado", ["han aceptado", "aceptaron", "aceptar"], "Singular subject; present perfect.", tr="The RAE has already accepted words like tuit and bloguero."),
        F("Para wifi existe también la expresión conexión ___.", "inalámbrica", ["telefónica", "pública", "eléctrica"], "Inalámbrica = wireless.", tr="For wifi there is also the expression wireless connection."),
        F("El idioma crea palabras nuevas porque la tecnología ___ rápido.", "avanza", ["avanzan", "avanzar", "avanzamos"], "Singular subject, present.", tr="The language creates new words because technology advances quickly.", lemma="avanzar:él"),
        F("Software y hardware ___ palabras inglesas.", "son", ["es", "ser", "somos"], "Plural subject, present.", tr="Software and hardware are English words.", lemma="ser:ellos"),
        M("Which word is an accepted Spanish form of “tablet”?", "tableta", ["tabletear", "tabla", "tableto"], "Tableta."),
        M("What is a “bloguero”?", "A person who writes a blog", ["A kind of cable", "A bank", "A screen"], "Bloguero = blogger."),
    ],
)

# ---------------------------------------------------------------------------- 589
L589 = lesson(
    "The surface web and the deep web",
    "No todo lo que está en internet aparece en un buscador.",
    requires=["internet", "página", "información", "privado", "público", "cuenta", "banco", "seguridad", "usuario", "periodista", "ilegal", "persona"],
    cards=[
        card("Two layers",
             "The surface web (la internet superficial) is what search engines show. The deep web (la internet profunda) is everything else that is not indexed: your email, your bank account, private databases. Most of it is ordinary and legal. "
             "A small part, sometimes called la web oscura, needs special software that hides the user's identity. Privacy tools can protect journalists and activists, but criminals also use them, and that makes police work harder.",
             examples=[
                 ex("La internet superficial es la parte que muestran los buscadores.", "The surface web is the part that search engines show.", "muestran"),
                 ex("La internet profunda incluye tu correo, tu cuenta del banco y muchas bases de datos privadas.", "The deep web includes your email, your bank account and many private databases.", "incluye"),
                 ex("La mayor parte de la internet profunda es normal y legal.", "Most of the deep web is normal and legal.", "legal"),
                 ex("Algunas redes de anonimato protegen la privacidad de periodistas y activistas.", "Some anonymity networks protect the privacy of journalists and activists.", "protegen"),
                 ex("Pero los delincuentes también las usan, y por eso es difícil detenerlos.", "But criminals also use them, and that is why it is hard to stop them.", "difícil"),
             ]),
    ],
    exercises=[
        M("What is the surface web?", "The part that search engines show", ["A secret network only", "Your private email", "The bottom of the sea"], "Lo que muestran los buscadores."),
        M("Is the deep web mostly illegal?", "No, most of it is normal and legal", ["Yes, all of it", "Only on Mondays", "It does not exist"], "La mayor parte es normal."),
        M("Who can benefit from anonymity networks?", "Journalists and activists", ["Only banks", "Only children", "Nobody"], "Protegen la privacidad de periodistas y activistas."),
        M("Why is it hard to stop criminals who use them?", "Their identity is hidden", ["The Internet is slow", "Laws do not exist", "Computers are old"], "El anonimato dificulta la detención."),
        F("La internet ___ es la que muestran los buscadores.", "superficial", ["profunda", "privada", "ilegal"], "Surface web.", tr="The surface web is the one search engines show."),
        F("Tu cuenta del banco forma parte de la internet ___.", "profunda", ["superficial", "pública", "ilegal"], "Not indexed: deep web.", tr="Your bank account is part of the deep web."),
        F("Las redes de anonimato ___ la privacidad de algunos periodistas.", "protegen", ["protege", "proteger", "protegemos"], "Plural subject, present.", tr="Anonymity networks protect the privacy of some journalists.", lemma="proteger:ellos"),
        F("La mayor parte de la internet profunda ___ legal.", "es", ["son", "ser", "somos"], "Singular subject, present.", tr="Most of the deep web is legal.", lemma="ser:él"),
        M("Which word means “search engine”?", "buscador", ["usuario", "enlace", "banco"], "Buscador."),
    ],
)

# ---------------------------------------------------------------------------- 590
L590 = lesson(
    "Cryptocurrencies: advantages, risks and crime",
    "Las criptomonedas existen solo en la red.",
    requires=["moneda", "digital", "banco", "dinero", "físico", "red", "valor", "gobierno", "control", "ley", "impuesto", "ventaja"],
    cards=[
        card("Money without coins",
             "Cryptocurrencies (criptomonedas or criptodivisas) exist only on the network. They have no physical form and no central bank behind them. Some people like them because transfers can be quick and need no bank. "
             "Critics point to risks: prices can change a lot, scams exist, and criminals can use them to demand ransoms, launder money or evade taxes. Governments debate how to regulate them.",
             examples=[
                 ex("Las criptomonedas existen solo en la red y no tienen forma física.", "Cryptocurrencies exist only on the network and have no physical form.", "existen"),
                 ex("Una ventaja es que se pueden enviar de un país a otro sin pasar por un banco.", "One advantage is that they can be sent from one country to another without going through a bank.", "ventaja"),
                 ex("Una desventaja es que su valor puede subir y bajar mucho en pocos días.", "One disadvantage is that their value can go up and down a lot in a few days.", "desventaja"),
                 ex("Los delincuentes las usan para pedir rescates, lavar dinero o evadir impuestos.", "Criminals use them to demand ransoms, launder money or evade taxes.", "usan"),
                 ex("Muchos gobiernos discuten cómo controlar este tipo de dinero.", "Many governments discuss how to control this kind of money.", "controlar"),
             ]),
    ],
    exercises=[
        M("Do cryptocurrencies have a physical form?", "No, they exist only on the network", ["Yes, they are coins", "Yes, they are bills", "Yes, they are gold"], "Solo en la red."),
        M("Name one advantage mentioned.", "They can be sent without a bank", ["They never change in value", "They are free of risk", "They are accepted everywhere"], "Se pueden enviar sin pasar por un banco."),
        M("Name one disadvantage mentioned.", "Their value can change a lot", ["They are too heavy", "They are always cheap", "They need paper"], "Su valor puede subir y bajar."),
        M("What do some criminals use them for?", "Ransoms, laundering money or evading taxes", ["Buying bread only", "Paying teachers", "Opening banks"], "Pedir rescates, lavar dinero o evadir impuestos."),
        F("Las criptomonedas ___ solo en la red.", "existen", ["existe", "existir", "existimos"], "Plural subject, present.", tr="Cryptocurrencies exist only on the network.", lemma="existir:ellos"),
        F("El ___ de las criptomonedas puede subir y bajar mucho.", "valor", ["banco", "enlace", "impuesto"], "Valor = value.", tr="The value of cryptocurrencies can go up and down a lot."),
        F("Muchos gobiernos ___ cómo controlar este tipo de dinero.", "discuten", ["discute", "discutir", "discutimos"], "Plural subject, present.", tr="Many governments discuss how to control this kind of money.", lemma="discutir:ellos"),
        F("Una ventaja es que se pueden enviar sin pasar por un ___.", "banco", ["virus", "archivo", "usuario"], "Banco = bank.", tr="One advantage is that they can be sent without going through a bank."),
        M("Which word means “disadvantage”?", "desventaja", ["ventaja", "ventana", "valor"], "Desventaja."),
    ],
)

# ---------------------------------------------------------------------------- 591
L591 = lesson(
    "Tax havens and offshore companies",
    "Un paraíso fiscal cobra pocos impuestos y comparte poca información.",
    requires=["paraíso", "fiscal", "impuesto", "extranjero", "empresa", "país", "ley", "cuenta", "dinero", "legal", "ilegal", "información"],
    cards=[
        card("What is a tax haven?",
             "A paraíso fiscal is a territory that charges foreign people and companies little or no tax and usually shares little financial information with other countries' tax authorities. "
             "A sociedad offshore is a company registered in a country where it does no business. Having one is not always illegal. It becomes a crime when the owner hides the money from the tax authorities of his or her home country (evasión fiscal).",
             examples=[
                 ex("Un paraíso fiscal cobra pocos impuestos y comparte poca información.", "A tax haven charges low taxes and shares little information.", "cobra"),
                 ex("Una sociedad offshore es una empresa registrada en un país donde no hace negocios.", "An offshore company is a company registered in a country where it does no business.", "registrada"),
                 ex("Tener una cuenta en el extranjero no es ilegal si el dinero se declara.", "Having an account abroad is not illegal if the money is declared.", "declara"),
                 ex("La evasión fiscal ocurre cuando alguien esconde su dinero para no pagar impuestos.", "Tax evasion occurs when someone hides money so as not to pay taxes.", "esconde"),
                 ex("Los impuestos pagan escuelas, hospitales y otros servicios públicos.", "Taxes pay for schools, hospitals and other public services.", "pagan"),
             ]),
    ],
    exercises=[
        M("What is a tax haven?", "A territory with few taxes and little information-sharing", ["A beach resort", "A kind of bank", "A tax office"], "Cobra pocos impuestos y comparte poca información."),
        M("When is an offshore account illegal?", "When the money is hidden from the tax authorities", ["Always", "Never", "When it is small"], "Cuando se esconde para no pagar impuestos."),
        M("What do taxes pay for?", "Public services such as schools and hospitals", ["Private yachts", "Only roads", "Nothing"], "Escuelas, hospitales y otros servicios."),
        F("Un paraíso fiscal ___ pocos impuestos.", "cobra", ["cobran", "cobrar", "cobramos"], "Singular subject, present.", tr="A tax haven charges low taxes.", lemma="cobrar:él"),
        F("Una sociedad offshore es una empresa ___ en el extranjero.", "registrada", ["registrado", "registrar", "registro"], "Agrees with empresa.", tr="An offshore company is a company registered abroad."),
        F("La evasión fiscal ocurre cuando alguien ___ su dinero.", "esconde", ["esconden", "esconder", "escondemos"], "Singular subject, present.", tr="Tax evasion occurs when someone hides his money.", lemma="esconder:él"),
        F("Los impuestos ___ escuelas y hospitales.", "pagan", ["paga", "pagar", "pagamos"], "Plural subject, present.", tr="Taxes pay for schools and hospitals.", lemma="pagar:ellos"),
        M("Is owning an offshore company always a crime?", "No, but hiding the money can be", ["Yes, always", "No, never a problem", "Only for banks"], "No siempre es ilegal."),
        M("Which word means “to evade”?", "evadir", ["pagar", "cobrar", "declarar"], "Evadir impuestos = to evade taxes."),
    ],
)

# ---------------------------------------------------------------------------- 592
L592 = lesson(
    "Leaks and whistleblowers: Panama Papers and Pandora Papers",
    "Los periodistas publicaron millones de documentos sobre empresas en el extranjero.",
    requires=["periodista", "documento", "empresa", "millón", "país", "político", "rico", "dinero", "ley", "investigación", "publicar", "mundo"],
    cards=[
        card("Big leaks",
             "A filtración is a leak: secret documents given to journalists. A denunciante is a person who reports wrongdoing; the English word is whistleblower. (Informante usually means an informant or a source.) "
             "The Panama Papers, published in 2016, came from the files of a Panamanian law firm. In 2021 the Pandora Papers, about twelve million files, came from several firms that create offshore companies. International teams of journalists studied them. "
             "The documents showed that politicians, businesspeople and other well-known people owned offshore companies. Owning one is not automatically a crime, and several people named said they broke no law.",
             examples=[
                 ex("Una filtración es una entrega de documentos secretos a periodistas.", "A leak is a delivery of secret documents to journalists.", "filtración"),
                 ex("Los Papeles de Panamá, publicados en dos mil dieciséis, salieron de los archivos de un bufete de abogados de ese país.", "The Panama Papers, published in 2016, came from the files of a law firm in that country.", "salieron"),
                 ex("En dos mil veintiuno se publicaron los Papeles de Pandora, unos doce millones de archivos.", "In 2021 the Pandora Papers, about twelve million files, were published.", "se publicaron"),
                 ex("Equipos internacionales de periodistas estudiaron los documentos durante meses.", "International teams of journalists studied the documents for months.", "estudiaron"),
                 ex("Los documentos mostraron que muchas personas poderosas tenían empresas en el extranjero.", "The documents showed that many powerful people had companies abroad.", "mostraron"),
                 ex("Algunos de los mencionados dijeron que no habían violado ninguna ley.", "Some of those named said they had not broken any law.", "dijeron"),
                 ex("Muchos expertos piden leyes más claras y más protección para los denunciantes.", "Many experts ask for clearer laws and more protection for whistleblowers.", "piden"),
             ]),
    ],
    exercises=[
        M("What is a filtración?", "A leak of secret documents", ["A tax", "A kind of bank", "A law"], "Entrega de documentos secretos a periodistas."),
        M("What is a denunciante?", "A person who reports wrongdoing", ["A police dog", "A judge", "A politician"], "Denunciante = whistleblower."),
        M("Was owning an offshore company automatically a crime?", "No", ["Yes, always", "Only in Panama", "Only for journalists"], "No es automáticamente un delito."),
        M("What do many experts ask for?", "Clearer laws and more protection for whistleblowers", ["Fewer journalists", "More secrets", "No banks"], "Piden leyes más claras y más protección."),
        F("Los Papeles de Panamá, publicados en dos mil dieciséis, ___ de los archivos de un bufete.", "salieron", ["salió", "salen", "salir"], "Plural subject; finished past.", tr="The Panama Papers, published in 2016, came from the files of a law firm.", lemma="salir:ellos:pret"),
        F("Los periodistas ___ los documentos durante meses.", "estudiaron", ["estudió", "estudian", "estudiar"], "Plural subject; finished past.", tr="The journalists studied the documents for months.", lemma="estudiar:ellos:pret"),
        F("Los documentos ___ que muchas personas poderosas tenían empresas en el extranjero.", "mostraron", ["mostró", "muestran", "mostrar"], "Plural subject; finished past.", tr="The documents showed that many powerful people had companies abroad.", lemma="mostrar:ellos:pret"),
        F("Algunos de los mencionados ___ que no habían violado ninguna ley.", "dijeron", ["dijo", "dicen", "decir"], "Plural subject; finished past.", tr="Some of those named said they had not broken any law.", lemma="decir:ellos:pret"),
        M("Why does the text say “algunos de los mencionados dijeron”?", "To report their position fairly", ["To prove they are guilty", "To hide the facts", "To praise them"], "It attributes the claim to the people named."),
    ],
)

# ---------------------------------------------------------------------------- 593
L593 = lesson(
    "Reading: the Odebrecht case",
    "Una empresa brasileña pagó sobornos en muchos países.",
    requires=["empresa", "brasileño", "contrato", "obra", "país", "investigación", "presidente", "ministro", "juicio", "justicia", "corrupción"],
    cards=[
        card("A corruption scandal across a continent",
             "Odebrecht was a large Brazilian construction company. Its case became one of the biggest corruption scandals in Latin America. This reading uses what the company and the prosecutors reported, and it does not say who is guilty of what: courts decide each case.",
             examples=[
                 ex("Odebrecht fue una de las empresas de construcción más grandes de Brasil.", "Odebrecht was one of the biggest construction companies in Brazil.", "fue"),
                 ex("En dos mil catorce empezó en Brasil una investigación sobre un sistema de lavado de dinero.", "In 2014 an investigation began in Brazil into a money-laundering system.", "empezó"),
                 ex("La investigación se llamó Lava Jato, que significa lavado de autos, porque empezó con negocios usados para lavar dinero, entre ellos una estación de servicio.", "The investigation was called Lava Jato, which means car wash, because it began with businesses used to launder money, including a service station.", "se llamó"),
                 ex("Con el tiempo, los fiscales descubrieron pagos de sobornos a funcionarios para conseguir contratos de obras públicas.", "Over time, prosecutors discovered bribe payments to officials to win public-works contracts.", "descubrieron"),
                 ex("En dos mil dieciséis la empresa llegó a acuerdos con fiscales de Brasil, Estados Unidos y Suiza.", "In 2016 the company reached agreements with prosecutors in Brazil, the United States and Switzerland.", "llegó"),
                 ex("La empresa reconoció que había pagado sobornos en varios países de América Latina y de otros continentes.", "The company acknowledged that it had paid bribes in several countries of Latin America and other continents.", "reconoció"),
                 ex("En muchos de esos países hubo investigaciones y juicios contra altos funcionarios y empresarios.", "In many of those countries there were investigations and trials against senior officials and businesspeople.", "hubo"),
                 ex("Los expertos dicen que el caso dañó la confianza de la gente en las instituciones.", "Experts say that the case damaged people's trust in institutions.", "dañó"),
                 ex("Otros dicen que los juicios pueden mostrar que la justicia es independiente.", "Others say that the trials can show that justice is independent.", "mostrar"),
             ]),
    ],
    exercises=[
        M("What kind of company was Odebrecht?", "A Brazilian construction company", ["A bank", "A newspaper", "An airline"], "Empresa de construcción de Brasil."),
        M("What does “Lava Jato” mean?", "car wash", ["gas station", "big tree", "quick trial"], "Lava Jato = lavado de autos."),
        M("What did prosecutors discover?", "Bribes paid to officials to win public-works contracts", ["A lost treasure", "A new bank", "A secret school"], "Pagos de sobornos para conseguir contratos."),
        M("Who decides the guilt of each person?", "The courts", ["The newspapers", "The company", "Social media"], "Los tribunales deciden."),
        F("En dos mil catorce ___ en Brasil una investigación.", "empezó", ["empezaron", "empieza", "empezar"], "Singular subject (investigación); finished past.", tr="In 2014 an investigation began in Brazil.", lemma="empezar:él:pret"),
        F("En dos mil dieciséis la empresa ___ a acuerdos con fiscales de tres países.", "llegó", ["llegaron", "llega", "llegar"], "Singular subject; finished past.", tr="In 2016 the company reached agreements with prosecutors in three countries.", lemma="llegar:él:pret"),
        F("Los fiscales ___ pagos de sobornos a funcionarios.", "descubrieron", ["descubrió", "descubren", "descubrir"], "Plural subject; finished past.", tr="The prosecutors discovered payments of bribes to officials.", lemma="descubrir:ellos:pret"),
        F("En muchos países ___ juicios contra altos funcionarios.", "hubo", ["hubieron", "hay", "haber"], "Haber → hubo, singular even with plural noun.", tr="In many countries there were trials against senior officials.", lemma="haber:él:pret"),
        M("What do experts say about trust?", "The case damaged trust in institutions", ["Trust went up everywhere", "Nothing changed", "People stopped reading"], "Dañó la confianza."),
    ],
)

# ---------------------------------------------------------------------------- 594
L594 = lesson(
    "Money laundering: lavado de dinero",
    "Lavar dinero es esconder el origen ilegal del dinero.",
    requires=["dinero", "origen", "ilegal", "banco", "negocio", "sospechoso", "ley", "criminal", "empresa", "informar", "sociedad", "crimen"],
    cards=[
        card("Making dirty money look clean",
             "Lavado de dinero (or lavado de activos) means hiding the illegal origin of money so that it looks legitimate. The crime that produced the money may be drug trafficking, corruption or fraud. "
             "It harms society because it lets criminals enjoy their profits and weakens honest businesses. Banks and other companies must report suspicious operations to the authorities.",
             examples=[
                 ex("Lavar dinero es esconder el origen ilegal del dinero.", "To launder money is to hide the illegal origin of money.", "esconder"),
                 ex("El dinero puede venir del narcotráfico, de la corrupción o del fraude.", "The money can come from drug trafficking, corruption or fraud.", "puede venir"),
                 ex("El lavado de dinero ayuda a los criminales a disfrutar de sus ganancias.", "Money laundering helps criminals enjoy their profits.", "ayuda"),
                 ex("También perjudica a los negocios honestos.", "It also harms honest businesses.", "perjudica"),
                 ex("Los bancos tienen que informar a las autoridades cuando ven una operación sospechosa.", "Banks have to inform the authorities when they see a suspicious transaction.", "informar"),
             ]),
    ],
    exercises=[
        M("What does “lavar dinero” mean?", "To hide the illegal origin of money", ["To wash coins", "To save money", "To print money"], "Esconder el origen ilegal."),
        M("Where can the money come from?", "Drug trafficking, corruption or fraud", ["Only salaries", "Only lotteries", "Only gifts"], "Narcotráfico, corrupción o fraude."),
        M("What must banks do about suspicious operations?", "Inform the authorities", ["Ignore them", "Advertise them", "Hide them"], "Informar a las autoridades."),
        F("Lavar dinero es esconder el ___ ilegal del dinero.", "origen", ["valor", "banco", "impuesto"], "Origen = origin.", tr="To launder money is to hide the illegal origin of the money."),
        F("El lavado de dinero ___ a los criminales a disfrutar de sus ganancias.", "ayuda", ["ayudan", "ayudar", "ayudamos"], "Singular subject, present.", tr="Money laundering helps criminals enjoy their profits.", lemma="ayudar:él"),
        F("Los bancos ___ que informar a las autoridades.", "tienen", ["tiene", "tener", "tenemos"], "Plural subject, present.", tr="Banks have to inform the authorities.", lemma="tener:ellos"),
        F("Una operación ___ puede ser una señal de lavado de dinero.", "sospechosa", ["sospechoso", "sospechosas", "sospechar"], "Agrees with operación.", tr="A suspicious transaction can be a sign of money laundering."),
        F("El lavado de dinero ___ a los negocios honestos.", "perjudica", ["perjudican", "perjudicar", "perjudicamos"], "Singular subject, present.", tr="Money laundering harms honest businesses.", lemma="perjudicar:él"),
        M("Which word means “profits”?", "ganancias", ["pérdidas", "gastos", "deudas"], "Ganancias = profits."),
    ],
)

# ---------------------------------------------------------------------------- 595
L595 = lesson(
    "Human trafficking: trata de personas",
    "La trata de personas afecta a mujeres, hombres, niñas y niños.",
    requires=["persona", "trabajo", "oferta", "falso", "víctima", "ayuda", "ley", "policía", "frontera", "engañar", "proteger", "derecho"],
    cards=[
        card("What it is",
             "La trata de personas (human trafficking) means recruiting, moving or holding people by force, threats or deceit in order to exploit them, for example in forced labor or sexual exploitation. "
             "The older expression trata de blancas is now considered inaccurate because trafficking affects people of every background, women, men and children. "
             "It is different from el tráfico de migrantes (smuggling), where people pay to be taken across a border, although smuggling can become trafficking.",
             examples=[
                 ex("La trata de personas es un delito grave que viola los derechos humanos.", "Human trafficking is a serious crime that violates human rights.", "grave"),
                 ex("Los traficantes engañan a las víctimas con ofertas falsas de trabajo.", "Traffickers deceive victims with false job offers.", "engañan"),
                 ex("Después, no las dejan salir y las obligan a trabajar sin pago.", "Afterwards they do not let them leave and force them to work without pay.", "obligan"),
                 ex("La trata y el tráfico de migrantes no son lo mismo.", "Trafficking and smuggling are not the same.", "no son lo mismo"),
                 ex("Es importante que las víctimas reciban ayuda y que no sean tratadas como criminales.", "It is important that victims receive help and are not treated as criminals.", "reciban"),
                 ex("Muchos países tienen leyes, líneas de ayuda y programas para proteger a las víctimas.", "Many countries have laws, hotlines and programs to protect victims.", "tienen"),
                 ex("Si ves señales de trata, es esencial que llames a las autoridades.", "If you see signs of trafficking, it is essential that you call the authorities.", "llames"),
             ]),
    ],
    exercises=[
        M("What is the modern expression for the crime?", "trata de personas", ["trata de colores", "tráfico de ideas", "robo de tiempo"], "Trata de personas."),
        M("How do traffickers often deceive victims?", "With false job offers", ["With free tickets to the stadium", "With real contracts", "With police badges"], "Ofertas falsas de trabajo."),
        M("Is trafficking the same as smuggling of migrants?", "No, they are different crimes", ["Yes, exactly the same", "Only in winter", "Only in cities"], "No son lo mismo."),
        M("What is important for victims?", "That they receive help", ["That they be punished", "That they be hidden", "That they be silent"], "Es importante que reciban ayuda."),
        F("Los traficantes ___ a las víctimas con ofertas falsas.", "engañan", ["engaña", "engañar", "engañamos"], "Plural subject, present.", tr="Traffickers deceive victims with false offers.", lemma="engañar:ellos"),
        F("Es importante que las víctimas ___ ayuda.", "reciban", ["reciben", "recibir", "recibimos"], "Es importante que + subjunctive.", tr="It is important that victims receive help.", lemma="recibir:ellos:subj"),
        F("Si ves señales de trata, es esencial que ___ a las autoridades.", "llames", ["llamas", "llamar", "llamo"], "Es esencial que + subjunctive; tú.", tr="If you see signs of trafficking, it is essential that you call the authorities.", lemma="llamar:tú:subj"),
        F("La trata de personas ___ los derechos humanos.", "viola", ["violan", "violar", "violamos"], "Singular subject, present.", tr="Human trafficking violates human rights.", lemma="violar:él"),
        M("Why is “trata de blancas” no longer used?", "Trafficking affects people of every background", ["It is too long", "It is a new phrase", "It is a trade term"], "Afecta a todos."),
    ],
)

# ---------------------------------------------------------------------------- 596
L596 = lesson(
    "Colloquial Spanish: cruzarse de brazos, hacerse de la vista gorda…",
    "No me voy a cruzar de brazos. Mis vecinos se hicieron de la vista gorda.",
    requires=["brazo", "pasar", "corto", "jefe", "vecino", "justicia", "criminal", "caballo", "denunciar", "decir", "dinero"],
    cards=[
        card("Four expressions",
             "These expressions come up in discussions of crime and justice. Learn each as a whole phrase.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["cruzarse de brazos", "to stand idly by", "No me voy a cruzar de brazos; voy a reclamar."],
                            ["hacerse de la vista gorda", "to turn a blind eye (also: hacer la vista gorda)", "Mis vecinos se hicieron de la vista gorda y no denunciaron nada."],
                            ["hacerse pasar por", "to pose as", "Un hombre se hizo pasar por empleado del banco."],
                            ["quedarse corto", "to fall short", "Me quedé corto: había más cosas que decir."]],
                           say=[2])]),
        card("A proverb",
             "A Spanish saying about the slowness of justice (its exact origin is not documented here): “El criminal va a caballo y la justicia en carreta.” The criminal rides a horse, while justice travels in an ox cart. It suggests that justice is slower than crime, and it is quoted in language textbooks as a traditional saying.",
             examples=[
                 ex("El criminal va a caballo y la justicia en carreta.", "The criminal goes on horseback and justice in a cart.", "caballo"),
             ]),
    ],
    exercises=[
        M("What does “cruzarse de brazos” mean?", "To stand idly by", ["To hug a friend", "To start a fight", "To fold a map"], "Not to act."),
        M("What does “hacerse de la vista gorda” mean?", "To pretend not to see something wrong", ["To look carefully", "To lose weight", "To need glasses"], "Turn a blind eye."),
        M("What does “hacerse pasar por” mean?", "To pose as someone else", ["To walk by", "To pass an exam", "To pay a toll"], "Pose as."),
        F("No me voy a ___ de brazos; voy a reclamar.", "cruzar", ["cruzo", "cruza", "cruzado"], "Ir a + infinitive.", tr="I am not going to stand idly by; I am going to complain."),
        F("Mis vecinos se hicieron de la ___ gorda.", "vista", ["mano", "cara", "boca"], "Hacerse de la vista gorda.", tr="My neighbors turned a blind eye."),
        F("Ayer un hombre se ___ pasar por empleado del banco.", "hizo", ["hicieron", "hacer", "haga"], "Fixed phrase; one man; finished past.", tr="Yesterday a man posed as a bank employee.", lemma="hacer:él:pret"),
        F("Me quedé ___: había más cosas que decir.", "corto", ["larga", "cortos", "cortar"], "Quedarse corto.", tr="I fell short: there were more things to say."),
        M("In the proverb, how does the criminal travel?", "On horseback", ["On a cart", "On foot", "By plane"], "A caballo."),
        M("What does the proverb suggest?", "Justice is slower than crime", ["Justice is faster than crime", "Crime does not exist", "Criminals are honest"], "La justicia va en carreta."),
    ],
)

# ---------------------------------------------------------------------------- 597
L597 = lesson(
    "Doubt: dudar que, no estar seguro de que",
    "Dudo que el gobierno envíe la ayuda a tiempo.",
    requires=["dudar", "seguro", "enviar", "llegar", "necesitar", "bajar", "funcionar", "terminar", "saber", "respuesta", "precio", "plan"],
    cards=[
        card("Not sure, so subjunctive",
             "When you doubt that something is true or will happen, the verb in the que clause is in the subjunctive. This is the first D in WEDDING. The doubt can be about a different subject or the same one. "
             "Dudar que and no estar seguro de que are the two basic expressions. When you are sure, use the indicative: Estoy seguro de que llegarán a tiempo.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["dudar que", "to doubt that", "Dudo que el gobierno envíe la ayuda a tiempo."],
                            ["no estar seguro de que", "not to be sure that", "No estoy seguro de que tú necesites una contraseña."],
                            ["no hay duda de que", "there is no doubt that (indicative)", "No hay duda de que el plan funciona."],
                            ["no dudar que", "not to doubt that (usually indicative; the subjunctive also occurs)", "No dudo que ellos saben la respuesta."]],
                           say=[2])]),
    ],
    exercises=[
        F("Dudo que el gobierno ___ la ayuda a tiempo.", "envíe", ["envía", "enviar", "envían"], "Dudar que + subjunctive.", tr="I doubt that the government will send the aid on time.", lemma="enviar:él:subj"),
        F("Dudamos que Ana ___ a tiempo.", "llegue", ["llega", "llegar", "llegamos"], "Dudar que + subjunctive.", tr="We doubt that Ana will arrive on time.", lemma="llegar:ella:subj"),
        F("No estoy seguro de que tú ___ una contraseña nueva.", "necesites", ["necesitas", "necesitar", "necesito"], "No estar seguro de que + subjunctive.", tr="I am not sure that you need a new password.", lemma="necesitar:tú:subj"),
        F("Dudo que los precios ___ pronto.", "bajen", ["bajan", "bajar", "bajamos"], "Dudar que + subjunctive.", tr="I doubt that prices will go down soon.", lemma="bajar:ellos:subj"),
        F("No estamos seguros de que el plan ___ bien.", "funcione", ["funciona", "funcionar", "funcionan"], "No estar seguro de que + subjunctive.", tr="We are not sure that the plan works well.", lemma="funcionar:él:subj"),
        F("Mis padres dudan que yo ___ el trabajo hoy.", "termine", ["termino", "terminar", "termina"], "Dudar que + subjunctive.", tr="My parents doubt that I will finish the work today.", lemma="terminar:yo:subj"),
        F("No hay duda de que el plan ___ bien.", "funciona", ["funcione", "funcionar", "funcionan"], "No hay duda de que: certainty, indicative.", tr="There is no doubt that the plan works well.", lemma="funcionar:él"),
        M("Which sentence is correct?", "Dudo que ellos sepan la respuesta.", ["Dudo que ellos saben la respuesta.", "Dudo que ellos saber la respuesta.", "Dudo ellos sepan la respuesta."], "Dudar que + subjunctive."),
        M("What does “no estoy seguro de que” express?", "Doubt", ["Certainty", "A command", "A past event"], "Not sure = doubt."),
    ],
)

# ---------------------------------------------------------------------------- 598
L598 = lesson(
    "Denial: negar que, no es cierto que, no es verdad que",
    "Sergio niega que sus ganancias sean ilegales.",
    requires=["negar", "cierto", "verdad", "ser", "hacer", "haber", "pagar", "subir", "existir", "empresa", "ministro", "ganancia"],
    cards=[
        card("Denying a statement",
             "When you deny that something is true, the verb in the que clause is in the subjunctive. Negar que is the main verb of denial. "
             "Es cierto que and es verdad que state a fact (indicative), but their negatives, no es cierto que and no es verdad que, deny it (subjunctive). Es falso que also takes the subjunctive. "
             "If the subject stays the same, the infinitive is common: Sergio niega haber robado.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["negar que", "to deny that", "Sergio niega que sus ganancias sean ilegales."],
                            ["no es cierto que", "it is not true that", "No es cierto que Petra haga trampa en los exámenes."],
                            ["no es verdad que", "it is not true that", "No es verdad que haya engaños en nuestra empresa."],
                            ["es falso que", "it is false that", "Es falso que los precios suban cada mes."],
                            ["es verdad que (affirmative)", "it is true that (indicative)", "Es verdad que los precios suben cada mes."]],
                           say=[2])]),
    ],
    exercises=[
        F("Sergio niega que sus ganancias ___ ilegales.", "sean", ["son", "ser", "somos"], "Negar que + subjunctive.", tr="Sergio denies that his earnings are illegal.", lemma="ser:ellos:subj"),
        F("No es cierto que Petra ___ trampa en los exámenes.", "haga", ["hace", "hacer", "hago"], "No es cierto que + subjunctive.", tr="It is not true that Petra cheats on exams.", lemma="hacer:ella:subj"),
        F("No es verdad que ___ engaños en nuestra empresa.", "haya", ["hay", "haber", "han"], "No es verdad que + subjunctive.", tr="It is not true that there are deceptions in our company.", lemma="haber:él:subj"),
        F("El ministro niega que el gobierno ___ dinero a esa empresa.", "pague", ["paga", "pagar", "pagan"], "Negar que + subjunctive.", tr="The minister denies that the government pays money to that company.", lemma="pagar:él:subj"),
        F("Es falso que los precios ___ cada mes.", "suban", ["suben", "subir", "subimos"], "Es falso que + subjunctive.", tr="It is false that prices go up every month.", lemma="subir:ellos:subj"),
        F("Nosotros negamos que ___ un problema grave.", "exista", ["existe", "existir", "existen"], "Negar que + subjunctive.", tr="We deny that there is a serious problem.", lemma="existir:él:subj"),
        F("Es verdad que los precios ___ cada mes.", "suben", ["suban", "subir", "subimos"], "Es verdad que: indicative.", tr="It is true that prices go up every month.", lemma="subir:ellos"),
        M("Which expression takes the subjunctive?", "no es cierto que", ["es cierto que", "es verdad que", "es evidente que"], "Negated certainty."),
        M("Which sentence is correct?", "Niego que yo tenga ese dinero.", ["Niego que yo tengo ese dinero.", "Niego que yo tener ese dinero.", "Niego yo tenga ese dinero."], "Negar que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 599
L599 = lesson(
    "Negation of belief: no creer que, no pensar que",
    "Creo que funciona. No creo que funcione.",
    requires=["creer", "pensar", "ir", "venir", "funcionar", "ser", "saber", "plan", "seguro", "vecino", "profesor"],
    cards=[
        card("Believing and not believing",
             "Affirmative creer que and pensar que state your belief as a fact: use the indicative. When you do not believe or think something, you present it as doubtful: use the subjunctive after no creer que and no pensar que.",
             tables=[table(["Affirmative: indicative", "Negative: subjunctive"],
                           [["Creo que el plan funciona.", "No creo que el plan funcione."],
                            ["Pienso que tu contraseña es segura.", "No pienso que tu contraseña sea segura."],
                            ["Creemos que los vecinos saben la verdad.", "No creemos que los vecinos sepan la verdad."],
                            ["Creo que ellos van a venir.", "No creo que ellos vayan a venir."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("No creo que ellos ___ a venir hoy.", "vayan", ["van", "ir", "vamos"], "No creer que + subjunctive.", tr="I don't think they are going to come today.", lemma="ir:ellos:subj"),
        F("No pienso que los profesores se ___ de brazos.", "crucen", ["cruzan", "cruzar", "cruzamos"], "No pensar que + subjunctive.", tr="I don't think the professors will stand idly by.", lemma="cruzar:ellos:subj"),
        F("Creo que el plan ___ bien.", "funciona", ["funcione", "funcionar", "funcionan"], "Creer que: indicative.", tr="I believe the plan works well.", lemma="funcionar:él"),
        F("No creo que el plan ___ bien.", "funcione", ["funciona", "funcionar", "funcionan"], "No creer que: subjunctive.", tr="I don't believe the plan works well.", lemma="funcionar:él:subj"),
        F("Pienso que tu contraseña ___ segura.", "es", ["sea", "ser", "son"], "Pensar que: indicative.", tr="I think your password is secure.", lemma="ser:ella"),
        F("No pienso que tu contraseña ___ segura.", "sea", ["es", "ser", "son"], "No pensar que: subjunctive.", tr="I don't think your password is secure.", lemma="ser:ella:subj"),
        F("Creemos que los vecinos ___ la verdad.", "saben", ["sepan", "saber", "sabe"], "Creer que: indicative.", tr="We believe the neighbors know the truth.", lemma="saber:ellos"),
        M("What is the difference between “creo que viene” and “no creo que venga”?", "The first states a belief; the second expresses doubt", ["Nothing", "The first is past", "The second is a command"], "Belief → indicative; disbelief → subjunctive."),
        M("Which sentence is correct?", "No creo que ella tenga razón.", ["No creo que ella tiene razón.", "No creo que ella tener razón.", "No creo ella tenga razón."], "No creer que + subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 600
L600 = lesson(
    "Certainty or doubt? Choosing the mood",
    "Dudo que lleguemos a tiempo. Estoy seguro de que llegaremos a tiempo.",
    requires=["dudar", "seguro", "creer", "pensar", "llegar", "venir", "ganar", "tener", "saber", "duda", "verdad", "cierto"],
    cards=[
        card("Two columns",
             "Certainty or belief → indicative. Doubt, denial or disbelief → subjunctive.",
             tables=[table(["Certainty: indicative", "Doubt or denial: subjunctive"],
                           [["creer que, pensar que", "no creer que, no pensar que"],
                            ["estar seguro de que", "no estar seguro de que"],
                            ["no hay duda de que, no dudar que (usually)", "dudar que"],
                            ["es verdad / cierto que", "no es verdad / cierto que, negar que"]],
                           say=[])]),
        card("Pairs",
             "Compare the two moods in the same context.",
             examples=[
                 ex("Dudo que lleguemos a tiempo.", "I doubt that we will arrive on time.", "lleguemos"),
                 ex("Estoy segura de que llegaremos a tiempo.", "I am sure that we will arrive on time.", "llegaremos"),
                 ex("No hay duda de que ella viene.", "There is no doubt that she is coming.", "viene"),
             ]),
    ],
    exercises=[
        F("Dudo que nosotros ___ a tiempo.", "lleguemos", ["llegamos", "llegar", "lleguen"], "Dudar que + subjunctive.", tr="I doubt that we will arrive on time.", lemma="llegar:nosotros:subj"),
        F("Estoy segura de que nosotros ___ a tiempo.", "llegaremos", ["lleguemos", "llegar", "lleguen"], "Estar seguro de que: indicative/future.", tr="I am sure that we will arrive on time.", lemma="llegar:nosotros:fut"),
        F("No hay duda de que ella ___ a la reunión.", "viene", ["venga", "venir", "vienen"], "No hay duda de que: indicative.", tr="There is no doubt that she is coming to the meeting.", lemma="venir:ella"),
        F("Dudo que ella ___ a la reunión.", "venga", ["viene", "venir", "vienen"], "Dudar que: subjunctive.", tr="I doubt that she is coming to the meeting.", lemma="venir:ella:subj"),
        F("No creo que nuestro equipo ___ el campeonato.", "gane", ["gana", "ganar", "ganan"], "No creer que: subjunctive.", tr="I don't think our team will win the championship.", lemma="ganar:él:subj"),
        F("Creo que nuestro equipo ___ el campeonato.", "ganará", ["gane", "ganar", "ganen"], "Creer que: indicative/future.", tr="I think our team will win the championship.", lemma="ganar:él:fut"),
        F("Es cierto que mis amigos ___ muchos problemas.", "tienen", ["tengan", "tener", "tenemos"], "Es cierto que: indicative.", tr="It is true that my friends have many problems.", lemma="tener:ellos"),
        M("Which sentence shows certainty?", "No hay duda de que el plan es bueno.", ["Dudo que el plan sea bueno.", "No creo que el plan sea bueno.", "No es verdad que el plan sea bueno."], "No hay duda de que + indicative."),
        M("Which sentence is correct?", "Estoy seguro de que ellos saben la verdad.", ["Estoy seguro de que ellos sepan la verdad.", "Estoy seguro de que ellos saber la verdad.", "Estoy seguro ellos saben la verdad."], "Certainty → indicative."),
    ],
)

# ---------------------------------------------------------------------------- 601
L601 = lesson(
    "The optimist and the pessimist: a city election",
    "Creo que el nuevo plan funcionará. Dudo que funcione.",
    requires=["alcalde", "plan", "ciudad", "transporte", "parque", "escuela", "hospital", "mejorar", "ayudar", "construir", "empleo", "seguridad"],
    cards=[
        card("Two voters talk about the mayor's plan (invented)",
             "A city is about to vote. One neighbor is an optimist, the other a pessimist. The optimist states beliefs (indicative); the pessimist expresses doubt (subjunctive).",
             tables=[table(["La optimista", "El pesimista"],
                           [["Creo que el nuevo plan de transporte ayudará a todos.", "Dudo que el plan ayude a todos."],
                            ["Pienso que construirán un parque en el barrio.", "No pienso que construyan un parque."],
                            ["Estoy segura de que las escuelas mejorarán.", "No estoy seguro de que mejoren."],
                            ["No hay duda de que el alcalde tiene buenas ideas.", "No es cierto que tenga buenas ideas."],
                            ["Es verdad que habrá más empleo.", "No es verdad que haya más empleo."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("La optimista cree que el plan de transporte ___ a todos.", "ayudará", ["ayude", "ayudar", "ayudan"], "Creer que: indicative/future.", tr="The optimist believes the transportation plan will help everyone.", lemma="ayudar:él:fut"),
        F("El pesimista duda que el plan ___ a todos.", "ayude", ["ayudará", "ayudar", "ayudan"], "Dudar que: subjunctive.", tr="The pessimist doubts that the plan will help everyone.", lemma="ayudar:él:subj"),
        F("Ella piensa que ___ un parque en el barrio.", "construirán", ["construyan", "construir", "construye"], "Pensar que: indicative/future.", tr="She thinks they will build a park in the neighborhood.", lemma="construir:ellos:fut"),
        F("Él no piensa que ___ un parque en el barrio.", "construyan", ["construirán", "construir", "construye"], "No pensar que: subjunctive.", tr="He doesn't think they will build a park in the neighborhood.", lemma="construir:ellos:subj"),
        F("Ella está segura de que las escuelas ___.", "mejorarán", ["mejoren", "mejorar", "mejora"], "Estar seguro de que: indicative/future.", tr="She is sure that the schools will improve.", lemma="mejorar:ellos:fut"),
        F("Él no está seguro de que las escuelas ___.", "mejoren", ["mejorarán", "mejorar", "mejora"], "No estar seguro de que: subjunctive.", tr="He is not sure that the schools will improve.", lemma="mejorar:ellos:subj"),
        F("Él dice que no es cierto que el alcalde ___ buenas ideas.", "tenga", ["tiene", "tener", "tienen"], "No es cierto que: subjunctive.", tr="He says it is not true that the mayor has good ideas.", lemma="tener:él:subj"),
        M("Who uses the indicative?", "The optimist", ["The pessimist", "Both", "Neither"], "She states beliefs."),
        M("Which sentence belongs to the pessimist?", "No es verdad que haya más empleo.", ["Es verdad que habrá más empleo.", "No hay duda de que mejorarán las escuelas.", "Estoy segura de que funcionará."], "Denial → subjunctive."),
    ],
)

# ---------------------------------------------------------------------------- 602
L602 = lesson(
    "Doubt and certainty about the future",
    "No hay duda de que habrá más robots. Dudo que haya vacaciones en Marte.",
    requires=["futuro", "duda", "dudar", "haber", "robot", "tecnología", "coche", "trabajo", "mundo", "paz", "viaje", "casa"],
    cards=[
        card("Predictions",
             "When you talk about the future, show how sure you are. For certainty use the future tense or ir a + infinitive with no hay duda de que, estoy seguro de que, creo que. "
             "For doubt use the present subjunctive after dudar que, no creer que, no es probable que. Haber has the special forms habrá (future) and haya (subjunctive).",
             tables=[table(["Certainty", "Doubt"],
                           [["No hay duda de que habrá más robots en las casas.", "Dudo que haya un robot en cada casa."],
                            ["Estoy seguro de que los coches serán eléctricos.", "No estoy seguro de que todos los coches sean eléctricos."],
                            ["Creo que muchas personas trabajarán desde casa.", "No creo que todas las personas trabajen desde casa."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("No hay duda de que ___ más robots en las casas.", "habrá", ["haya", "hay", "haber"], "No hay duda de que: future.", tr="There is no doubt that there will be more robots in homes.", lemma="haber:él:fut"),
        F("Dudo que ___ un robot en cada casa.", "haya", ["habrá", "hay", "haber"], "Dudar que: subjunctive.", tr="I doubt that there will be a robot in every house.", lemma="haber:él:subj"),
        F("Estoy seguro de que los coches ___ eléctricos.", "serán", ["sean", "ser", "son"], "Estar seguro de que: future.", tr="I am sure that cars will be electric.", lemma="ser:ellos:fut"),
        F("No estoy seguro de que todos los coches ___ eléctricos.", "sean", ["serán", "ser", "son"], "No estar seguro de que: subjunctive.", tr="I am not sure that all cars will be electric.", lemma="ser:ellos:subj"),
        F("Creo que muchas personas ___ desde casa.", "trabajarán", ["trabajen", "trabajar", "trabaja"], "Creer que: future.", tr="I think many people will work from home.", lemma="trabajar:ellos:fut"),
        F("No creo que todas las personas ___ desde casa.", "trabajen", ["trabajarán", "trabajar", "trabaja"], "No creer que: subjunctive.", tr="I don't think all people will work from home.", lemma="trabajar:ellos:subj"),
        F("Dudo que ___ paz en todo el mundo pronto.", "haya", ["habrá", "hay", "haber"], "Dudar que: subjunctive.", tr="I doubt that there will be peace in the whole world soon.", lemma="haber:él:subj"),
        M("Which sentence expresses certainty about the future?", "No hay duda de que viajaremos más.", ["Dudo que viajemos más.", "No creo que viajemos más.", "No es cierto que viajemos más."], "No hay duda de que + indicative/future."),
        M("What are the special forms of haber used here?", "habrá (future) and haya (subjunctive)", ["hubo and había", "he and has", "hay and hubo"], "Habrá and haya."),
    ],
)

# ---------------------------------------------------------------------------- 603
L603 = lesson(
    "Review: stem-changing verbs in the subjunctive",
    "Dudo que empiece. Dudo que empecemos. Dudo que duerma. Dudo que durmamos.",
    requires=["empezar", "volver", "pedir", "dormir", "pensar", "poder", "dudar", "cerrar", "seguir", "servir", "contar", "morir"],
    cards=[
        card("Boot verbs",
             "Verbs that change their stem in the present indicative (e→ie, o→ue, e→i) keep the change in the present subjunctive. "
             "-ar and -er verbs lose the change in nosotros and vosotros. -ir verbs keep a change in nosotros and vosotros: e→i (pidamos, sintamos) or o→u (durmamos, muramos).",
             tables=[table(["Infinitivo", "que yo", "que nosotros"],
                           [["empezar (e→ie)", "empiece", "empecemos"],
                            ["volver (o→ue)", "vuelva", "volvamos"],
                            ["pedir (e→i)", "pida", "pidamos"],
                            ["dormir (o→ue)", "duerma", "durmamos"],
                            ["seguir (e→i)", "siga", "sigamos"],
                            ["morir (o→ue)", "muera", "muramos"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Dudo que la reunión ___ a tiempo.", "empiece", ["empieza", "empezar", "empecemos"], "Dudar que + subjunctive.", tr="I doubt that the meeting starts on time.", lemma="empezar:ella:subj"),
        F("No creo que nosotros ___ a empezar hoy.", "vayamos", ["vamos", "ir", "vayan"], "Not stem-changing; ir → vayamos.", tr="I don't think that we are going to start today.", lemma="ir:nosotros:subj"),
        F("Dudo que mi hermano ___ pronto.", "vuelva", ["vuelve", "volver", "volvemos"], "Dudar que + subjunctive.", tr="I doubt that my brother will come back soon.", lemma="volver:él:subj"),
        F("Es importante que nosotros ___ temprano.", "volvamos", ["volvemos", "volver", "vuelvan"], "Boot verb: no change in nosotros.", tr="It is important that we return early.", lemma="volver:nosotros:subj"),
        F("Dudo que ellos ___ ayuda.", "pidan", ["piden", "pedir", "pedimos"], "Pedir (e→i).", tr="I doubt that they will ask for help.", lemma="pedir:ellos:subj"),
        F("Quiero que nosotros ___ ocho horas.", "durmamos", ["dormimos", "duerman", "dormir"], "Dormir: nosotros → durmamos.", tr="I want us to sleep eight hours.", lemma="dormir:nosotros:subj"),
        F("No creo que el niño ___ tan temprano.", "duerma", ["duerme", "dormir", "dormimos"], "Dormir: él → duerma.", tr="I don't think the child sleeps this early.", lemma="dormir:él:subj"),
        M("Which is the subjunctive of “pedir” for nosotros?", "pidamos", ["pedamos", "pedimos", "pidemos"], "-ir verbs keep e→i."),
        M("Which is the subjunctive of “morir” for nosotros?", "muramos", ["morimos", "muéramos", "moramos"], "-ir verbs: o→u in nosotros."),
    ],
)

# ---------------------------------------------------------------------------- 604
L604 = lesson(
    "Review: the six irregular subjunctives",
    "dé, vaya, esté, haya, sepa, sea",
    requires=["dar", "ir", "estar", "haber", "saber", "ser", "dudar", "creer", "esperar", "ojalá", "importante", "necesario"],
    cards=[
        card("Dar, ir, estar, haber, saber, ser",
             "These six verbs do not follow the yo-form rule. Learn them by heart.",
             tables=[table(["Infinitivo", "yo / él", "tú", "nosotros", "ellos"],
                           [["dar", "dé", "des", "demos", "den"],
                            ["ir", "vaya", "vayas", "vayamos", "vayan"],
                            ["estar", "esté", "estés", "estemos", "estén"],
                            ["haber", "haya", "hayas", "hayamos", "hayan"],
                            ["saber", "sepa", "sepas", "sepamos", "sepan"],
                            ["ser", "sea", "seas", "seamos", "sean"]],
                           say=[1, 2, 3, 4])]),
    ],
    exercises=[
        F("Dudo que el gobierno nos ___ más tiempo.", "dé", ["da", "dar", "den"], "Dudar que + subjunctive.", tr="I doubt that the government will give us more time.", lemma="dar:él:subj"),
        F("Espero que tú ___ al concierto con nosotros.", "vayas", ["vas", "ir", "vaya"], "Esperar que + subjunctive.", tr="I hope that you go to the concert with us.", lemma="ir:tú:subj"),
        F("No creo que ellos ___ en casa ahora.", "estén", ["están", "estar", "estemos"], "No creer que + subjunctive.", tr="I don't think they are at home now.", lemma="estar:ellos:subj"),
        F("Dudo que ___ tiempo para todo.", "haya", ["hay", "haber", "han"], "Dudar que + subjunctive.", tr="I doubt there will be time for everything.", lemma="haber:él:subj"),
        F("Es necesario que nosotros ___ la verdad.", "sepamos", ["sabemos", "saber", "sepan"], "Es necesario que + subjunctive.", tr="It is necessary that we know the truth.", lemma="saber:nosotros:subj"),
        F("Ojalá que ustedes ___ muy felices.", "sean", ["son", "ser", "seamos"], "Ojalá que + subjunctive.", tr="I hope you are very happy.", lemma="ser:ustedes:subj"),
        F("Es importante que tú no le ___ tu contraseña a nadie.", "des", ["das", "dar", "dé"], "Es importante que + subjunctive; tú.", tr="It is important that you not give your password to anyone.", lemma="dar:tú:subj"),
        M("Which is the subjunctive of “ser” for nosotros?", "seamos", ["somos", "sean", "estemos"], "Seamos."),
        M("Which is the subjunctive of “ir” for yo?", "vaya", ["voy", "vea", "vaya a"], "Vaya."),
    ],
)

# ---------------------------------------------------------------------------- 605
L605 = lesson(
    "WEDDING complete: sorting all the triggers",
    "W E D D I N G",
    requires=["querer", "alegrar", "dudar", "negar", "importante", "creer", "ojalá", "saber", "pensar", "esperar", "temer", "seguro"],
    cards=[
        card("The seven triggers",
             "Now you know all seven letters. Most triggers need que and a change of subject; otherwise use the infinitive (Quiero venir). Doubt and denial can keep the same subject (Dudo que yo pueda ir), and ojalá and tal vez do not need que. When the main clause states a fact, use the indicative.",
             tables=[table(["Letra", "Idea", "Ejemplo"],
                           [["W", "Wish, will, influence", "Quiero que vengas."],
                            ["E", "Emotion", "Me alegro de que vengas."],
                            ["D", "Doubt", "Dudo que vengas."],
                            ["D", "Denial", "Niego que venga."],
                            ["I", "Impersonal expressions", "Es importante que vengas."],
                            ["N", "Negation of belief", "No creo que vengas."],
                            ["G", "God grant, probability", "Ojalá que vengas. Tal vez vengas."]],
                           say=[2])]),
    ],
    exercises=[
        F("Quiero que tú ___ a mi casa.", "vengas", ["vienes", "venir", "vengo"], "W: querer que.", tr="I want you to come to my house.", lemma="venir:tú:subj"),
        F("Me alegro de que tú ___ a mi casa.", "vengas", ["vienes", "venir", "vengo"], "E: alegrarse de que.", tr="I am glad that you are coming to my house.", lemma="venir:tú:subj"),
        F("Dudo que tú ___ a mi casa.", "vengas", ["vienes", "venir", "vengo"], "D: dudar que.", tr="I doubt that you are coming to my house.", lemma="venir:tú:subj"),
        F("Es importante que tú ___ a mi casa.", "vengas", ["vienes", "venir", "vengo"], "I: es importante que.", tr="It is important that you come to my house.", lemma="venir:tú:subj"),
        F("No creo que tú ___ a mi casa.", "vengas", ["vienes", "venir", "vengo"], "N: no creer que.", tr="I don't think you are coming to my house.", lemma="venir:tú:subj"),
        F("Ojalá que tú ___ a mi casa.", "vengas", ["vienes", "venir", "vengo"], "G: ojalá que.", tr="I hope you come to my house.", lemma="venir:tú:subj"),
        F("Sé que tú ___ a mi casa.", "vienes", ["vengas", "venir", "vengo"], "A fact: indicative.", tr="I know that you are coming to my house.", lemma="venir:tú"),
        M("Which sentence needs the indicative?", "Estoy seguro de que viene.", ["Dudo que venga.", "Ojalá que venga.", "Niego que venga."], "Certainty → indicative."),
        M("What does the second D in WEDDING stand for?", "Denial", ["Doubt", "Desire", "Danger"], "Doubt, Denial."),
    ],
)

# ---------------------------------------------------------------------------- 606
L606 = lesson(
    "Giving your opinion on world problems",
    "Es necesario que los gobiernos protejan a las víctimas.",
    requires=["gobierno", "víctima", "proteger", "necesario", "urgente", "ojalá", "dudar", "molestar", "tecnología", "ayudar", "ley", "sociedad"],
    cards=[
        card("Opinions with the subjunctive",
             "To give your opinion on a social problem, mix triggers: a wish (Ojalá que…), an emotion (Me molesta que…), a necessity (Es necesario que…), a recommendation (Recomiendo que…), a probability (Es probable que…) and a doubt (Dudo que…).",
             examples=[
                 ex("Es necesario que los gobiernos protejan a las víctimas de la trata de personas.", "It is necessary that governments protect victims of human trafficking.", "protejan"),
                 ex("Me molesta que algunas empresas escondan su dinero en el extranjero.", "It bothers me that some companies hide their money abroad.", "escondan"),
                 ex("Recomiendo que todos usemos contraseñas largas.", "I recommend that we all use long passwords.", "usemos"),
                 ex("Es probable que los ataques informáticos aumenten.", "It is likely that computer attacks will increase.", "aumenten"),
                 ex("Dudo que las leyes cambien rápidamente.", "I doubt that the laws will change quickly.", "cambien"),
                 ex("Ojalá que la sociedad aprenda a ayudar a las víctimas.", "I hope that society learns to help victims.", "aprenda"),
             ]),
    ],
    exercises=[
        F("Es necesario que los gobiernos ___ a las víctimas.", "protejan", ["protegen", "proteger", "protegemos"], "Es necesario que + subjunctive.", tr="It is necessary that governments protect the victims.", lemma="proteger:ellos:subj"),
        F("Me molesta que algunas empresas ___ su dinero en el extranjero.", "escondan", ["esconden", "esconder", "escondemos"], "Molestar que + subjunctive.", tr="It bothers me that some companies hide their money abroad.", lemma="esconder:ellos:subj"),
        F("Recomiendo que todos nosotros ___ contraseñas largas.", "usemos", ["usamos", "usar", "usen"], "Recomendar que + subjunctive.", tr="I recommend that we all use long passwords.", lemma="usar:nosotros:subj"),
        F("Es probable que los ataques informáticos ___.", "aumenten", ["aumentan", "aumentar", "aumentamos"], "Es probable que + subjunctive.", tr="It is likely that computer attacks will increase.", lemma="aumentar:ellos:subj"),
        F("Dudo que las leyes ___ rápidamente.", "cambien", ["cambian", "cambiar", "cambiamos"], "Dudar que + subjunctive.", tr="I doubt that the laws will change quickly.", lemma="cambiar:ellos:subj"),
        F("Ojalá que la sociedad ___ a ayudar a las víctimas.", "aprenda", ["aprende", "aprender", "aprenden"], "Ojalá que + subjunctive.", tr="I hope that society learns to help victims.", lemma="aprender:ella:subj"),
        F("Es urgente que el gobierno ___ más ayuda a las víctimas.", "dé", ["da", "dar", "den"], "Es urgente que + subjunctive.", tr="It is urgent that the government give more help to the victims.", lemma="dar:él:subj"),
        M("Which trigger expresses a recommendation?", "Recomiendo que…", ["Dudo que…", "Me molesta que…", "Ojalá que…"], "Recomendar."),
        M("Which sentence expresses an emotion?", "Me molesta que no haya justicia.", ["Es probable que haya justicia.", "Recomiendo que haya justicia.", "Dudo que haya justicia."], "Molestar = emotion."),
    ],
)

# ---------------------------------------------------------------------------- 607
L607 = lesson(
    "Reading: a radio talk about online shopping scams (practice text)",
    "Le recomiendo que verifique la página antes de pagar.",
    requires=["compra", "tienda", "página", "pagar", "tarjeta", "precio", "oferta", "verificar", "recomendar", "seguro", "dinero", "internet"],
    cards=[
        card("On the radio",
             "This is an invented interview. The host asks a security expert how to avoid online shopping scams. Notice the subjunctive after recommendations and impersonal expressions, and the indicative after facts.",
             examples=[
                 ex("Presentador: Muchos oyentes nos escriben porque perdieron dinero en compras por internet. ¿Qué nos recomienda?", "Host: Many listeners write to us because they lost money in online purchases. What do you recommend?", "recomienda"),
                 ex("Experta: Primero, le recomiendo que verifique la página antes de pagar. Es importante que la dirección empiece con las letras hache, te, te, pe, ese, aunque eso solo indica que la conexión es segura, no que la tienda sea real.", "Expert: First, I recommend that you check the page before paying. It is important that the address start with the letters h-t-t-p-s, although that only shows that the connection is secure, not that the shop is real.", "verifique"),
                 ex("Presentador: ¿Y si el precio es demasiado bajo?", "Host: And if the price is too low?", "demasiado"),
                 ex("Experta: Dudo que una oferta increíble sea real. Es mejor que desconfíe de los precios que parecen milagros.", "Expert: I doubt that an incredible offer is real. It is better that you distrust prices that seem like miracles.", "sea"),
                 ex("Presentador: ¿Qué hago si pierdo dinero?", "Host: What do I do if I lose money?", "pierdo"),
                 ex("Experta: Es necesario que llame de inmediato a su banco y que guarde todos los mensajes como prueba.", "Expert: It is necessary that you call your bank immediately and that you keep all the messages as proof.", "llame"),
                 ex("Presentador: Muchas gracias. Ojalá que nuestros oyentes sigan sus consejos.", "Host: Thank you very much. I hope our listeners follow your advice.", "sigan"),
             ]),
    ],
    exercises=[
        M("What does the expert recommend first?", "Checking the page before paying", ["Paying in cash", "Buying quickly", "Sharing the password"], "Le recomiendo que verifique la página."),
        M("What does the expert say about offers that are too good?", "She doubts they are real", ["They are always real", "They are free", "They are legal"], "Dudo que una oferta increíble sea real."),
        M("What should you do if you lose money?", "Call the bank immediately and keep the messages as proof", ["Wait a year", "Delete everything", "Post the card number"], "Llame de inmediato a su banco."),
        M("What does the host hope at the end?", "That listeners follow the advice", ["That prices go up", "That the program ends", "That banks close"], "Ojalá que sigan sus consejos."),
        F("Le recomiendo que ___ la página antes de pagar.", "verifique", ["verifica", "verificar", "verifico"], "Recomendar que + subjunctive; usted.", tr="I recommend that you check the page before paying.", lemma="verificar:usted:subj"),
        F("Dudo que una oferta increíble ___ real.", "sea", ["es", "ser", "son"], "Dudar que + subjunctive.", tr="I doubt that an incredible offer is real.", lemma="ser:ella:subj"),
        F("Es necesario que usted ___ de inmediato a su banco.", "llame", ["llama", "llamar", "llamo"], "Es necesario que + subjunctive; usted.", tr="It is necessary that you call your bank immediately.", lemma="llamar:usted:subj"),
        F("Ojalá que nuestros oyentes ___ sus consejos.", "sigan", ["siguen", "seguir", "seguimos"], "Ojalá que + subjunctive.", tr="I hope our listeners follow your advice.", lemma="seguir:ellos:subj"),
        M("Why is the expert's language in usted form?", "She speaks formally to the host", ["It is a command to a friend", "It is the past tense", "It is a question"], "Usted = formal address."),
    ],
)

# ---------------------------------------------------------------------------- 608
L608 = lesson(
    "Reading: false information online (practice text)",
    "No todo lo que leemos en las redes es verdad.",
    requires=["noticia", "falso", "información", "fuente", "verificar", "periodista", "político", "campaña", "creer", "importante"],
    cards=[
        card("Disinformation",
             "La desinformación is false or misleading information spread on purpose. Some campaigns are anonymous and use invented data to damage a rival or to confuse voters. "
             "Before the Internet, false stories spread more slowly. Now they can spread in minutes. This is a general explanation, not a report about a specific case.",
             examples=[
                 ex("La desinformación es información falsa que alguien difunde a propósito.", "Disinformation is false information that someone spreads on purpose.", "difunde"),
                 ex("Algunas campañas anónimas usan datos inventados para dañar a un rival.", "Some anonymous campaigns use invented data to damage a rival.", "inventados"),
                 ex("Antes de internet, las noticias falsas tardaban más en difundirse.", "Before the Internet, false stories took longer to spread.", "tardaban"),
                 ex("Hoy una noticia falsa puede llegar a millones de personas en pocos minutos.", "Today a false story can reach millions of people in a few minutes.", "puede llegar"),
                 ex("Es importante que verifiquemos la fuente antes de compartir una noticia.", "It is important that we check the source before sharing a story.", "verifiquemos"),
                 ex("Los periodistas recomiendan que comparemos varias fuentes.", "Journalists recommend that we compare several sources.", "comparemos"),
                 ex("Dudo que todas las noticias que veo en las redes sean verdaderas.", "I doubt that all the news I see on social networks is true.", "sean"),
             ]),
    ],
    exercises=[
        M("What is disinformation?", "False information spread on purpose", ["Old news", "A kind of virus", "A newspaper"], "Información falsa que alguien difunde a propósito."),
        M("How was it different before the Internet?", "False stories spread more slowly", ["They spread faster", "They did not exist", "They used viruses"], "Tardaban más en difundirse."),
        M("What should we do before sharing a story?", "Check the source", ["Share it quickly", "Delete the message", "Change the title"], "Verifiquemos la fuente."),
        F("Es importante que nosotros ___ la fuente antes de compartir una noticia.", "verifiquemos", ["verificamos", "verificar", "verifiquen"], "Es importante que + subjunctive.", tr="It is important that we check the source before sharing a story.", lemma="verificar:nosotros:subj"),
        F("Los periodistas recomiendan que nosotros ___ varias fuentes.", "comparemos", ["comparamos", "comparar", "comparen"], "Recomendar que + subjunctive.", tr="Journalists recommend that we compare several sources.", lemma="comparar:nosotros:subj"),
        F("Dudo que todas las noticias que veo ___ verdaderas.", "sean", ["son", "ser", "somos"], "Dudar que + subjunctive.", tr="I doubt that all the news I see is true.", lemma="ser:ellos:subj"),
        F("Una noticia falsa ___ llegar a millones de personas en pocos minutos.", "puede", ["pueden", "poder", "podemos"], "Singular subject, present.", tr="A false story can reach millions of people in a few minutes.", lemma="poder:él"),
        M("Which sentence is correct?", "No creo que esa noticia sea verdadera.", ["No creo que esa noticia es verdadera.", "No creo que esa noticia ser verdadera.", "No creo esa noticia sea verdadera."], "No creer que + subjunctive."),
        M("Why does the text say it is a general explanation?", "It does not report on a specific case", ["It is a poem", "It is a command", "It is an advertisement"], "No es un informe sobre un caso concreto."),
    ],
)

# ---------------------------------------------------------------------------- 609
L609 = lesson(
    "Review: cyber and financial crime vocabulary",
    "el gusano, el rescate, el paraíso fiscal, el lavado de dinero",
    requires=["virus", "rescate", "paraíso", "fiscal", "dinero", "banco", "ley", "usuario", "criminal", "seguridad", "empresa", "información"],
    cards=[
        card("Word map",
             "Cyber: el malware, el virus, el gusano, el troyano, el programa espía, el ransomware, el phishing, el antivirus, el ciberdelincuente, el pirata informático, la contraseña. "
             "Money: la criptomoneda, el paraíso fiscal, la sociedad offshore, la evasión fiscal, el lavado de dinero, el soborno. "
             "People and crimes: la filtración, el denunciante, la trata de personas.",
             examples=[
                 ex("Un gusano se copia a sí mismo.", "A worm copies itself.", "gusano"),
                 ex("El ransomware pide un rescate.", "Ransomware demands a ransom.", "rescate"),
                 ex("Un paraíso fiscal cobra pocos impuestos.", "A tax haven charges low taxes.", "paraíso"),
             ]),
    ],
    exercises=[
        F("Un ___ se copia a sí mismo y se propaga rápido.", "gusano", ["troyano", "antivirus", "banco"], "Worm.", tr="A worm copies itself and spreads fast."),
        F("El ransomware pide un ___.", "rescate", ["impuesto", "enlace", "banco"], "Ransom.", tr="Ransomware demands a ransom."),
        F("Un ___ fiscal cobra pocos impuestos.", "paraíso", ["virus", "rescate", "usuario"], "Tax haven.", tr="A tax haven charges low taxes."),
        F("El ___ de dinero esconde el origen ilegal del dinero.", "lavado", ["valor", "banco", "pago"], "Money laundering.", tr="Money laundering hides the illegal origin of money."),
        F("Una ___ es una entrega de documentos secretos a periodistas.", "filtración", ["contraseña", "criptomoneda", "ganancia"], "A leak.", tr="A leak is a delivery of secret documents to journalists."),
        F("La ___ de personas es un delito grave.", "trata", ["moneda", "copia", "red"], "Human trafficking.", tr="Human trafficking is a serious crime."),
        M("What is a “denunciante”?", "A whistleblower", ["A virus", "A bank clerk", "A judge"], "A person who reports wrongdoing."),
        M("Which word names a person who writes harmful programs or breaks into systems?", "pirata informático", ["usuario", "periodista", "contador"], "Pirata informático = illegal hacker."),
        M("What does “el soborno” mean?", "bribe", ["tax", "ransom", "loan"], "Soborno = bribe."),
    ],
)

# ---------------------------------------------------------------------------- 610
L610 = lesson(
    "Review: doubt, denial and negation",
    "Dudo que… Niego que… No creo que… Creo que… Estoy seguro de que…",
    requires=["dudar", "negar", "creer", "pensar", "seguro", "cierto", "verdad", "ser", "tener", "hacer", "venir", "ir"],
    cards=[
        card("Summary",
             "Doubt, denial, disbelief → subjunctive: dudar que, no estar seguro de que, negar que, no es cierto/verdad que, es falso que, no creer que, no pensar que. "
             "Belief and certainty → indicative: creer que, pensar que, estar seguro de que, no hay duda de que, es verdad/cierto que (no dudar que usually takes the indicative).",
             examples=[
                 ex("Niego que yo tenga ese archivo.", "I deny that I have that file.", "tenga"),
                 ex("Es cierto que ella tiene ese archivo.", "It is true that she has that file.", "tiene"),
             ]),
    ],
    exercises=[
        F("Niego que yo ___ ese archivo.", "tenga", ["tengo", "tener", "tiene"], "Negar que + subjunctive.", tr="I deny that I have that file.", lemma="tener:yo:subj"),
        F("Es cierto que ella ___ ese archivo.", "tiene", ["tenga", "tener", "tengo"], "Es cierto que: indicative.", tr="It is true that she has that file.", lemma="tener:ella"),
        F("No creo que ellos ___ el trabajo hoy.", "hagan", ["hacen", "hacer", "hacemos"], "No creer que + subjunctive.", tr="I don't think they will do the work today.", lemma="hacer:ellos:subj"),
        F("Estoy seguro de que ellos ___ el trabajo hoy.", "hacen", ["hagan", "hacer", "hacemos"], "Estar seguro de que: indicative.", tr="I am sure they are doing the work today.", lemma="hacer:ellos"),
        F("Dudo que tú ___ solo a esa ciudad.", "vayas", ["vas", "ir", "vaya"], "Dudar que + subjunctive.", tr="I doubt that you will go to that city alone.", lemma="ir:tú:subj"),
        F("No es verdad que la empresa ___ sobornos.", "pague", ["paga", "pagar", "pagan"], "No es verdad que + subjunctive.", tr="It is not true that the company pays bribes.", lemma="pagar:ella:subj"),
        F("No hay duda de que el ataque ___ de otro país.", "viene", ["venga", "venir", "vienen"], "No hay duda de que: indicative.", tr="There is no doubt that the attack comes from another country.", lemma="venir:él"),
        M("Which sentence is correct?", "No pienso que ellos sean culpables.", ["No pienso que ellos son culpables.", "No pienso que ellos ser culpables.", "No pienso ellos sean culpables."], "No pensar que + subjunctive."),
        M("Which expression takes the indicative?", "no hay duda de que", ["dudar que", "negar que", "no creer que"], "Certainty."),
    ],
)

# ---------------------------------------------------------------------------- 611
L611 = lesson(
    "Unit review: a class discussion on international crime (practice text)",
    "Es increíble que existan tantos tipos de delitos en internet.",
    requires=["estudiante", "profesor", "clase", "crimen", "internet", "dinero", "ley", "víctima", "gobierno", "ayudar", "justicia", "esperar"],
    cards=[
        card("Students talk (invented)",
             "Read this short conversation between two students. Notice how the mood changes with each opinion: indicative for facts and beliefs, subjunctive for doubt, emotion, hopes and recommendations.",
             examples=[
                 ex("Marta: Es increíble que existan tantos tipos de delitos en internet.", "Marta: It is incredible that there are so many types of crimes on the Internet.", "existan"),
                 ex("Diego: Es verdad. Creo que los criminales aprenden rápido, pero no creo que sean imposibles de detener.", "Diego: It is true. I think criminals learn quickly, but I don't think they are impossible to stop.", "aprenden"),
                 ex("Marta: Me preocupa que muchas víctimas no denuncien por miedo o por vergüenza.", "Marta: It worries me that many victims do not report out of fear or shame.", "denuncien"),
                 ex("Diego: Por eso es necesario que las leyes protejan a los denunciantes y que la policía los escuche.", "Diego: That is why it is necessary that the laws protect those who report crimes and that the police listen to them.", "protejan"),
                 ex("Marta: Dudo que todos los países cooperen, pero ojalá que muchos lo hagan.", "Marta: I doubt that all countries will cooperate, but I hope many will.", "cooperen"),
                 ex("Diego: Estoy seguro de que la cooperación internacional ayudará, aunque va a llevar tiempo.", "Diego: I am sure that international cooperation will help, although it will take time.", "ayudará"),
             ]),
    ],
    exercises=[
        M("What is Marta's first reaction?", "It is incredible that there are so many types of crimes online", ["She is bored", "She is angry at Diego", "She is asleep"], "Es increíble que existan…"),
        M("What does Diego not believe?", "That the criminals are impossible to stop", ["That crime exists", "That the Internet exists", "That police exist"], "No creo que sean imposibles de detener."),
        M("What worries Marta?", "That many victims do not report the crimes", ["That prices are low", "That the class is late", "That the police are friendly"], "Me preocupa que muchas víctimas no denuncien."),
        F("Es increíble que ___ tantos tipos de delitos en internet.", "existan", ["existen", "existir", "existimos"], "Es increíble que + subjunctive.", tr="It is incredible that so many types of crimes exist on the Internet.", lemma="existir:ellos:subj"),
        F("Me preocupa que muchas víctimas no ___.", "denuncien", ["denuncian", "denunciar", "denunciamos"], "Preocupar que + subjunctive.", tr="It worries me that many victims do not report.", lemma="denunciar:ellos:subj"),
        F("Dudo que todos los países ___.", "cooperen", ["cooperan", "cooperar", "cooperamos"], "Dudar que + subjunctive.", tr="I doubt that all countries will cooperate.", lemma="cooperar:ellos:subj"),
        F("Estoy seguro de que la cooperación internacional ___.", "ayudará", ["ayude", "ayudar", "ayudan"], "Estar seguro de que: indicative/future.", tr="I am sure that international cooperation will help.", lemma="ayudar:ella:fut"),
        F("Creo que los criminales ___ rápido.", "aprenden", ["aprendan", "aprender", "aprendemos"], "Creer que: indicative.", tr="I think criminals learn quickly.", lemma="aprender:ellos"),
        M("Which sentence is correct?", "Ojalá que muchos países cooperen.", ["Ojalá que muchos países cooperan.", "Ojalá que muchos países cooperar.", "Ojalá muchos países cooperarán."], "Ojalá que + subjunctive."),
    ],
)

UNIT = unit("Delito internacional y ciberseguridad", [
    L584, L585, L586, L587, L588, L589, L590, L591, L592, L593, L594, L595, L596, L597, L598, L599, L600, L601, L602, L603, L604, L605, L606, L607, L608, L609, L610, L611,
])

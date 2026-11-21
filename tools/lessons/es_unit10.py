"""Unit 10: errands and services (textbook Chapter 9)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 129
L129 = lesson(
    "Running errands",
    "hacer un trámite, abrir una cuenta, hacer cola",
    requires=["banco", "cuenta", "pagar", "cita", "contrato", "préstamo"],
    cards=[
        card("At the bank and the office",
             "A trámite is an errand or a piece of paperwork. Many trámites need a visit in person, a phone call or "
             "a few clicks. These are the key phrases.",
             tables=[table(["Expresión", "English"],
                           [["hacer un trámite", "to take care of an errand or paperwork"],
                            ["abrir una cuenta corriente", "to open a checking account"],
                            ["abrir una cuenta de ahorros", "to open a savings account"],
                            ["pedir un préstamo", "to ask for a loan"],
                            ["usar el cajero automático", "to use the ATM"],
                            ["hacer cola", "to stand in line"],
                            ["hacer una cita", "to make an appointment"],
                            ["llenar un formulario", "to fill out a form"],
                            ["firmar un contrato", "to sign a contract"],
                            ["el comprobante de domicilio", "proof of address"]],
                           say=[0])]),
        card("Putting it together",
             "Use tener que, necesitar and ir a plus these phrases. Remember that you do trámites por teléfono, "
             "por Internet or en persona.",
             examples=[
                 ex("Primero tengo que abrir una cuenta corriente.", "First I have to open a checking account.", "tengo que abrir"),
                 ex("Para abrir la cuenta necesito un comprobante de domicilio.", "To open the account I need proof of address.", "comprobante de domicilio"),
                 ex("Hoy hay mucha gente haciendo cola en el banco.", "Today there are many people standing in line at the bank.", "haciendo cola"),
                 ex("Puedo hacer una cita por teléfono.", "I can make an appointment by phone.", "por teléfono"),
             ]),
    ],
    exercises=[
        M("Which phrase means “to stand in line”?", "hacer cola", ["hacer una cita", "llenar un formulario", "pedir un préstamo"], "Cola is a line."),
        M("What do you need to prove where you live?", "un comprobante de domicilio", ["un cajero automático", "un préstamo", "una cita"], "Domicilio is home address."),
        M("What does “abrir una cuenta de ahorros” mean?", "to open a savings account", ["to open a checking account", "to close an account", "to pay a bill"], "Ahorros = savings."),
        M("Where do you take out money at any hour?", "en el cajero automático", ["en la cola", "en el formulario", "en el contrato"], "El cajero automático is the ATM."),
        F("Quiero sacar dinero del ___ automático.", "cajero", ["formulario", "préstamo", "contrato"], "Cajero automático = ATM.", tr="I want to take money out of the ATM."),
        F("Para hablar con el director necesito ___ una cita.", "hacer", ["abrir", "firmar", "llenar"], "You make an appointment: hacer una cita.", tr="To speak with the director I need to make an appointment."),
        F("Tengo que ___ este formulario antes de las tres.", "llenar", ["hacer", "abrir", "pedir"], "You fill out a form: llenar un formulario.", tr="I have to fill out this form before three."),
        F("Necesito dinero; voy a ___ un préstamo.", "pedir", ["firmar", "hacer", "usar"], "Pedir un préstamo = to ask for a loan.", tr="I need money; I am going to ask for a loan."),
        M("How can you make an appointment without leaving home?", "por teléfono", ["en persona", "en cola", "por el cajero"], "Por teléfono = by phone."),
    ],
)

# ---------------------------------------------------------------------------- 130
L130 = lesson(
    "Utilities and paying bills",
    "la luz, el agua, el gas, la cuenta",
    requires=["luz", "agua", "gas", "pagar", "cuenta", "efectivo"],
    cards=[
        card("The services of a home",
             "To start a service, say contratar (to sign up for). To end it, say cancelar. Companies often ask for a "
             "deposit (un depósito or una fianza), which you can get back later (el reembolso).",
             tables=[table(["Servicio", "English"],
                           [["la luz", "electricity"],
                            ["el agua", "water"],
                            ["el gas", "gas"],
                            ["el teléfono", "phone service"],
                            ["Internet", "Internet"],
                            ["la televisión por cable", "cable television"]],
                           say=[0])],
             examples=[
                 ex("Voy a contratar la luz y el agua.", "I am going to sign up for electricity and water.", "contratar"),
                 ex("La compañía necesita un depósito.", "The company needs a deposit.", "un depósito"),
                 ex("Quiero cancelar el servicio de gas.", "I want to cancel the gas service.", "cancelar"),
             ]),
        card("How do you pay?",
             "You pay a bill (la cuenta) in different ways. Learn the prepositions with each way to pay.",
             tables=[table(["Forma de pago", "English"],
                           [["en efectivo", "in cash"],
                            ["con tarjeta", "with a card"],
                            ["con cheque", "with a check"],
                            ["por Internet", "online"],
                            ["con pago automático", "with automatic payment"]],
                           say=[0])],
             examples=[
                 ex("Pago la cuenta del agua en efectivo.", "I pay the water bill in cash.", "en efectivo"),
                 ex("Prefiero pagar con tarjeta.", "I prefer to pay with a card.", "con tarjeta"),
                 ex("Mi hermana paga todo por Internet.", "My sister pays everything online.", "por Internet"),
             ]),
    ],
    exercises=[
        M("What does “contratar la luz” mean?", "to sign up for electricity", ["to turn off the lights", "to pay a fine", "to buy a lamp"], "Contratar = to sign up for a service."),
        M("Which phrase means “in cash”?", "en efectivo", ["con tarjeta", "por Internet", "con cheque"], "Efectivo = cash."),
        M("What is “un depósito” for a service company?", "money you leave and may get back", ["a gift", "a monthly bill", "a type of phone"], "A deposit that can be refunded."),
        M("Which service brings water to the house?", "el agua", ["la luz", "el gas", "el cable"], "El agua."),
        F("Pago la cuenta con ___.", "tarjeta", ["efectivo", "Internet", "cola"], "Con tarjeta = with a card.", tr="I pay the bill with a card."),
        F("La compañía de ___ necesita un depósito antes de dar el servicio.", "luz", ["lluvia", "cola", "ahorro"], "La compañía de luz = electric company.", tr="The electric company needs a deposit before providing the service."),
        F("Mi hermana paga todo ___ Internet.", "por", ["con", "de", "sin"], "Por Internet = online.", tr="My sister pays everything online."),
        F("Prefiero pagar en ___ porque no tengo tarjeta.", "efectivo", ["cheque", "Internet", "cola"], "En efectivo = in cash.", tr="I prefer to pay in cash because I do not have a card."),
        M("What does “cancelar el servicio” mean?", "to end the service", ["to start the service", "to improve the service", "to pay for the service"], "Cancelar = to cancel."),
    ],
)

# ---------------------------------------------------------------------------- 131
L131 = lesson(
    "At the post office",
    "enviar una carta, un paquete, el apartado de correos",
    requires=["correo", "carta", "enviar", "recibir", "dirección", "paquete"],
    cards=[
        card("La oficina de correos",
             "Learn the main words for sending and receiving mail.",
             tables=[table(["Palabra", "English"],
                           [["la oficina de correos", "post office"],
                            ["la carta", "letter"],
                            ["el paquete", "package"],
                            ["el sello", "stamp"],
                            ["la correspondencia", "mail"],
                            ["la dirección, el domicilio", "address"],
                            ["el apartado de correos", "P.O. box"],
                            ["enviar, mandar", "to send"],
                            ["recibir", "to receive"]],
                           say=[0])]),
        card("A short exchange",
             "Notice the polite forms: quisiera, por favor, ¿cuánto cuesta?",
             tables=[table(["Cliente", "Empleado"],
                           [["Buenos días. Quisiera enviar este paquete a Chile.", "Muy bien. ¿Cuál es la dirección?"],
                            ["Aquí está. ¿Cuánto cuesta?", "Cuesta veinte dólares. ¿Quiere pagar en efectivo?"],
                            ["No, con tarjeta, por favor.", "Perfecto. Aquí tiene su comprobante."]],
                           say=[0, 1])]),
    ],
    exercises=[
        M("Which word means “stamp”?", "el sello", ["el paquete", "la carta", "el domicilio"], "Sello = stamp."),
        M("What is “un apartado de correos”?", "a P.O. box", ["a package", "a stamp", "an address"], "Apartado de correos = P.O. box."),
        M("Which word means “address”?", "la dirección", ["la carta", "el sello", "la cuenta"], "Dirección or domicilio."),
        F("Quiero ___ esta carta a mi abuela en Lima.", "enviar", ["recibir", "contratar", "firmar"], "A letter going to someone: enviar.", tr="I want to send this letter to my grandmother in Lima."),
        F("Mi hermano me ___ un paquete cada mes.", "envía", ["envío", "enviamos", "envías"], "Mi hermano is he: envía.", tr="My brother sends me a package every month.", lemma="enviar:él"),
        F("Hoy yo ___ mucha correspondencia.", "recibo", ["recibes", "recibe", "recibimos"], "Yo: recibo.", tr="Today I receive a lot of mail.", lemma="recibir:yo"),
        M("How does the customer politely say “I would like to send this package”?", "Quisiera enviar este paquete.", ["Yo envío paquete ya.", "Envía paquete.", "Paquete enviar."], "Quisiera + infinitive is polite."),
        M("What does the employee say to ask for the address?", "¿Cuál es la dirección?", ["¿Cuál es el sello?", "¿Dónde está la cola?", "¿Cuánto es el cajero?"], "Dirección = address."),
        M("Which word means “mail” in general?", "la correspondencia", ["el cajero", "el préstamo", "la fianza"], "Correspondencia."),
    ],
    verify=vp("enviar", "envío", "envías", "envía", "enviamos", "enviáis", "envían")
           + vp("recibir", "recibo", "recibes", "recibe", "recibimos", "recibís", "reciben"),
)

# ---------------------------------------------------------------------------- 132
L132 = lesson(
    "Phones, Internet and social media",
    "el celular, la aplicación, las redes sociales",
    requires=["teléfono", "móvil", "mensaje", "aplicación", "red", "clave"],
    cards=[
        card("Staying in touch",
             "Latin America says el celular for a mobile phone, and Spain says el móvil. Both are understood everywhere.",
             tables=[table(["Palabra", "English"],
                           [["el celular, el móvil", "cell phone"],
                            ["el mensaje de texto", "text message"],
                            ["el correo electrónico", "e-mail"],
                            ["la aplicación", "app"],
                            ["las redes sociales", "social media"],
                            ["la clave", "password"],
                            ["los datos", "data, information"],
                            ["el servicio ilimitado", "unlimited service"],
                            ["el cargador", "charger"]],
                           say=[0])]),
        card("What do you do online?",
             "Many everyday verbs: mandar, recibir, contestar, publicar, usar, llamar.",
             examples=[
                 ex("Mando muchos mensajes de texto.", "I send many text messages.", "mensajes de texto"),
                 ex("Uso una aplicación para pagar las cuentas.", "I use an app to pay the bills.", "una aplicación"),
                 ex("Siempre olvido mi clave.", "I always forget my password.", "mi clave"),
                 ex("Publico fotos en las redes sociales.", "I post photos on social media.", "Publico"),
                 ex("¿Traes tu cargador?", "Are you bringing your charger?", "tu cargador"),
             ]),
    ],
    exercises=[
        M("How do you say “text message”?", "mensaje de texto", ["correo de texto", "texto de red", "clave de mensaje"], "Mensaje de texto."),
        M("What does “la clave” mean?", "password", ["charger", "app", "bill"], "Clave = password."),
        M("Which word is “charger”?", "el cargador", ["la clave", "la red", "el dato"], "Cargador."),
        F("Mi teléfono no tiene batería; necesito el ___.", "cargador", ["correo", "mensaje", "préstamo"], "A charger recharges the phone.", tr="My phone has no battery; I need the charger."),
        F("Mando un ___ de texto a mi madre.", "mensaje", ["clave", "cargador", "dato"], "Mensaje is masculine and goes with de texto.", tr="I send a text message to my mother."),
        F("Mi hermana publica fotos en las ___ sociales.", "redes", ["claves", "cuentas", "mensajes"], "Redes sociales = social media.", tr="My sister posts photos on social media."),
        F("Yo ___ fotos en mi cuenta todos los domingos.", "publico", ["publicas", "publica", "publicamos"], "Yo: publico.", tr="I post photos on my account every Sunday.", lemma="publicar:yo"),
        M("In Spain, which word is usually used for a cell phone?", "el móvil", ["el cargador", "la clave", "el cajero"], "Spain: móvil. Latin America: celular."),
        M("Which sentence is correct?", "Siempre olvido mi clave.", ["Siempre olvido mi clavo.", "Siempre olvidas mi clave yo.", "Siempre olvido mis clave."], "Clave is feminine singular."),
    ],
    verify=vp("publicar", "publico", "publicas", "publica", "publicamos", "publicáis", "publican"),
)

# ---------------------------------------------------------------------------- 133
L133 = lesson(
    "Irregular verbs in the present: the big picture",
    "puedo, pongo, conozco, construyo, soy",
    requires=["poder", "poner", "conocer", "construir", "ser", "ir"],
    cards=[
        card("Six families",
             "You already know many irregular verbs. Seeing them as families makes them easier to learn.",
             tables=[table(["Family", "Pattern", "Examples"],
                           [["Stem change", "the vowel changes in the boot", "puedo, cierro, pido, huelo (with an h)"],
                            ["Yo -go", "only yo adds -go", "pongo, salgo, hago, traigo"],
                            ["Yo -go + stem change", "yo -go; the boot forms also change the stem", "tengo, vengo, digo"],
                            ["Yo -zco", "most verbs in -cer or -cir after a vowel", "conozco, traduzco"],
                            ["-uir", "y before every ending except nosotros and vosotros", "construyo, incluyo"],
                            ["Fully irregular", "learn each one by heart", "soy, estoy, voy, sé, veo, doy, oigo"]],
                           say=[2])]),
        card("Check the yo form first",
             "When you meet a new verb, look at the yo form. If it is regular, the verb is usually regular; if it "
             "has -go, -zco or -y, you know which family it belongs to.",
             examples=[
                 ex("Yo puedo ir al banco.", "I can go to the bank.", "puedo"),
                 ex("Yo conozco una buena tienda.", "I know a good store.", "conozco"),
                 ex("Yo no sé la respuesta.", "I do not know the answer.", "sé"),
             ]),
    ],
    exercises=[
        M("Which family does “pongo” belong to?", "yo -go", ["stem change", "-uir verbs", "yo -zco"], "Poner → pongo."),
        M("Which family does “conozco” belong to?", "yo -zco", ["yo -go", "stem change", "fully irregular"], "Conocer → conozco."),
        M("Which family does “construyo” belong to?", "-uir verbs", ["yo -zco", "yo -go", "stem change"], "Construir → construyo."),
        M("Which family does “pido” belong to?", "stem change", ["yo -go", "-uir verbs", "fully irregular"], "Pedir: e → i."),
        M("Which verb is completely irregular?", "ir", ["pedir", "poner", "conocer"], "Voy, vas, va, vamos, vais, van."),
        F("Yo ___ ir contigo al banco.", "puedo", ["poedo", "podo", "pueden"], "Poder: o → ue.", tr="I can go with you to the bank.", lemma="poder:yo"),
        F("Yo ___ las llaves en la mesa.", "pongo", ["pono", "pones", "pone"], "Poner: yo pongo.", tr="I put the keys on the table.", lemma="poner:yo"),
        F("Yo ___ a tu hermano.", "conozco", ["conoco", "conoces", "conocen"], "Conocer: yo conozco.", tr="I know your brother.", lemma="conocer:yo"),
        F("Mis padres ___ a la oficina en autobús.", "van", ["vamos", "va", "voy"], "Ir: ellos van.", tr="My parents go to the office by bus.", lemma="ir:ellos"),
    ],
)

# ---------------------------------------------------------------------------- 134
L134 = lesson(
    "Verbs in -cer and -cir: conozco, traduzco",
    "conocer, ofrecer, parecer, traducir, conducir",
    requires=["conocer", "ofrecer", "parecer", "crecer", "agradecer", "producir"],
    cards=[
        card("Yo -zco",
             "Most verbs that end in -cer or -cir after a vowel add a z before the o in the yo form: conozco, ofrezco, "
             "traduzco. All the other forms are regular. Exceptions: hacer (hago) and decir (digo).",
             tables=[table(["", "conocer", "traducir"],
                           [["yo", "conozco", "traduzco"],
                            ["tú", "conoces", "traduces"],
                            ["él, ella, usted", "conoce", "traduce"],
                            ["nosotros", "conocemos", "traducimos"],
                            ["vosotros", "conocéis", "traducís"],
                            ["ellos, ellas, ustedes", "conocen", "traducen"]],
                           say=[1, 2])]),
        card("Verbs in this family",
             "The same pattern works for many verbs.",
             tables=[table(["Infinitive", "Yo", "English"],
                           [["agradecer", "agradezco", "to be thankful"],
                            ["conducir", "conduzco", "to drive"],
                            ["crecer", "crezco", "to grow"],
                            ["merecer", "merezco", "to deserve"],
                            ["ofrecer", "ofrezco", "to offer"],
                            ["parecer", "parezco", "to seem"],
                            ["pertenecer", "pertenezco", "to belong"],
                            ["producir", "produzco", "to produce"],
                            ["reducir", "reduzco", "to reduce"]],
                           say=[1])]),
    ],
    exercises=[
        F("Yo ___ inglés y español.", "traduzco", ["traduco", "traduces", "traducimos"], "Traducir: yo traduzco.", tr="I translate English and Spanish.", lemma="traducir:yo"),
        F("Yo ___ mi ayuda a mis vecinos.", "ofrezco", ["ofreco", "ofreces", "ofrecemos"], "Ofrecer: yo ofrezco.", tr="I offer my help to my neighbors.", lemma="ofrecer:yo"),
        F("Yo ___ un coche pequeño.", "conduzco", ["conduco", "conduces", "conducimos"], "Conducir: yo conduzco.", tr="I drive a small car.", lemma="conducir:yo"),
        F("Tú ___ a mucha gente aquí.", "conoces", ["conozco", "conoce", "conocen"], "Only yo has -zco.", tr="You know a lot of people here.", lemma="conocer:tú"),
        F("Mis hijos ___ muy rápido.", "crecen", ["crecemos", "crezco", "crece"], "Mis hijos is they: crecen.", tr="My children grow very fast.", lemma="crecer:ellos"),
        F("Yo te ___ tu ayuda.", "agradezco", ["agradeco", "agradeces", "agradecemos"], "Agradecer: yo agradezco.", tr="I thank you for your help.", lemma="agradecer:yo"),
        M("Which yo form is correct for “parecer”?", "parezco", ["pareco", "parezo", "paresco"], "-cer → -zco."),
        M("Which of these forms of “conocer” has a z?", "conozco", ["conoces", "conocemos", "conocen"], "Only the yo form changes."),
        M("What does “merecer” mean?", "to deserve", ["to buy", "to grow", "to translate"], "Merecer = to deserve."),
    ],
    verify=vp("conocer", "conozco", "conoces", "conoce", "conocemos", "conocéis", "conocen")
           + vp("traducir", "traduzco", "traduces", "traduce", "traducimos", "traducís", "traducen")
           + vp("crecer", "crezco", "creces", "crece", "crecemos", "crecéis", "crecen"),
)

# ---------------------------------------------------------------------------- 135
L135 = lesson(
    "Verbs in -uir: construyo, incluyo",
    "construir, incluir, destruir, contribuir",
    requires=["construir", "incluir", "destruir", "contribuir", "huir", "influir"],
    cards=[
        card("A y in the middle",
             "Verbs in -uir add a y before the endings in every form except nosotros and vosotros. (This is for verbs where "
             "the u is pronounced; in -guir verbs the u is silent: seguir → sigo.)",
             tables=[table(["", "construir"],
                           [["yo", "construyo"],
                            ["tú", "construyes"],
                            ["él, ella, usted", "construye"],
                            ["nosotros", "construimos"],
                            ["vosotros", "construís"],
                            ["ellos, ellas, ustedes", "construyen"]],
                           say=[1])]),
        card("Other -uir verbs",
             "Contribuir, destruir, huir, incluir and influir all work the same way.",
             tables=[table(["Infinitive", "Yo", "English"],
                           [["contribuir", "contribuyo", "to contribute"],
                            ["destruir", "destruyo", "to destroy"],
                            ["huir", "huyo", "to flee"],
                            ["incluir", "incluyo", "to include"],
                            ["influir", "influyo", "to influence"]],
                           say=[1])],
             examples=[
                 ex("El precio incluye el agua y la luz.", "The price includes water and electricity.", "incluye"),
                 ex("Mis padres contribuyen con dinero.", "My parents contribute money.", "contribuyen"),
             ]),
    ],
    exercises=[
        F("Mi empresa ___ casas nuevas.", "construye", ["construya", "construe", "construyen"], "Construir: construye.", tr="My company builds new houses.", lemma="construir:ella"),
        F("Los precios ___ el servicio de agua.", "incluyen", ["incluye", "incluimos", "incluyo"], "Los precios is they: incluyen.", tr="The prices include water service.", lemma="incluir:ellos"),
        F("Tú ___ mucho en tus hermanos.", "influyes", ["influes", "influye", "influimos"], "Influir: tú influyes.", tr="You influence your brothers and sisters a lot.", lemma="influir:tú"),
        F("Nosotros ___ con una parte del dinero.", "contribuimos", ["contribuyemos", "contribuyen", "contribuyo"], "Nosotros has no y: contribuimos.", tr="We contribute part of the money.", lemma="contribuir:nosotros"),
        F("Yo ___ las cuentas en un archivo.", "incluyo", ["incluo", "incluyes", "incluye"], "Incluir: yo incluyo.", tr="I include the bills in a file.", lemma="incluir:yo"),
        M("Which form of “destruir” has no y?", "destruimos", ["destruyo", "destruyes", "destruyen"], "Nosotros and vosotros keep -i-."),
        M("Which yo form is correct for “huir”?", "huyo", ["huio", "huo", "huyó"], "Huir → huyo."),
        M("What does “influir” mean?", "to influence", ["to flee", "to build", "to include"], "Influir."),
        M("How do you say “She builds a house”?", "Ella construye una casa.", ["Ella construya una casa.", "Ella construe una casa.", "Ella construyo una casa."], "Construye."),
    ],
    verify=vp("construir", "construyo", "construyes", "construye", "construimos", "construís", "construyen")
           + vp("huir", "huyo", "huyes", "huye", "huimos", "huis", "huyen"),
)

# ---------------------------------------------------------------------------- 136
L136 = lesson(
    "Ver, dar, oler and saber",
    "veo, doy, huelo, sé",
    requires=["ver", "dar", "oler", "saber", "oír", "ir"],
    cards=[
        card("Four more irregular verbs",
             "Ver keeps its e in the yo form (veo, not vo), and dar adds a y (doy), like soy, estoy and voy. Oler (to smell) changes o to "
             "hue- in the boot forms. Saber has sé in the yo form.",
             tables=[table(["", "ver", "dar", "oler", "saber"],
                           [["yo", "veo", "doy", "huelo", "sé"],
                            ["tú", "ves", "das", "hueles", "sabes"],
                            ["él, ella, usted", "ve", "da", "huele", "sabe"],
                            ["nosotros", "vemos", "damos", "olemos", "sabemos"],
                            ["vosotros", "veis", "dais", "oléis", "sabéis"],
                            ["ellos, ellas, ustedes", "ven", "dan", "huelen", "saben"]],
                           say=[1, 2, 3, 4])]),
        card("Small accents matter",
             "Sé (I know) has an accent to distinguish it from se, the reflexive pronoun. Ve, ves, veis, da, das and "
             "dais have no written accent.",
             examples=[
                 ex("Veo la televisión después de cenar.", "I watch television after dinner.", "Veo"),
                 ex("Te doy mi dirección.", "I give you my address.", "Te doy"),
                 ex("La cocina huele muy bien.", "The kitchen smells very good.", "huele"),
                 ex("No sé cuánto cuesta el paquete.", "I do not know how much the package costs.", "No sé"),
             ]),
    ],
    exercises=[
        F("Yo ___ la televisión por la noche.", "veo", ["vo", "ves", "vemos"], "Ver: yo veo.", tr="I watch television at night.", lemma="ver:yo"),
        F("Yo te ___ mi número de teléfono.", "doy", ["do", "das", "damos"], "Dar: yo doy.", tr="I give you my phone number.", lemma="dar:yo"),
        F("La cocina ___ muy bien.", "huele", ["olé", "huelen", "olemos"], "Oler: o → hue; la cocina is singular.", tr="The kitchen smells very good.", lemma="oler:ella"),
        F("Yo no ___ la respuesta.", "sé", ["se", "sabes", "sabe"], "Saber: yo sé, with an accent.", tr="I do not know the answer.", lemma="saber:yo"),
        F("Ellos ___ las cuentas en la oficina.", "ven", ["ve", "vemos", "veo"], "Ellos: ven.", tr="They look at the bills in the office.", lemma="ver:ellos"),
        F("Nosotros ___ las flores.", "olemos", ["huelemos", "huelen", "hueles"], "Nosotros keeps the o.", tr="We smell the flowers.", lemma="oler:nosotros"),
        M("Why does “sé” have an accent?", "To tell it apart from “se”.", ["It is a question word.", "It is plural.", "It is the future."], "Sé (I know) vs. se (pronoun)."),
        M("Which form of “dar” is correct for “tú”?", "das", ["dás", "dabes", "dai"], "Das has no accent."),
        M("Which is the yo form of “oler”?", "huelo", ["olo", "ueglo", "olgo"], "Oler: hue- in boot forms."),
    ],
    verify=vp("ver", "veo", "ves", "ve", "vemos", "veis", "ven")
           + vp("dar", "doy", "das", "da", "damos", "dais", "dan")
           + vp("oler", "huelo", "hueles", "huele", "olemos", "oléis", "huelen")
           + vp("saber", "sé", "sabes", "sabe", "sabemos", "sabéis", "saben"),
)

# ---------------------------------------------------------------------------- 137
L137 = lesson(
    "Saber or conocer?",
    "Sé la respuesta. Conozco a tu hermano.",
    requires=["saber", "conocer", "persona", "país", "ciudad", "idioma"],
    cards=[
        card("Two verbs for “to know”",
             "English has one verb, “to know”. Spanish has two. Saber is for information and skills. Conocer is for "
             "being familiar with people, places and things.",
             tables=[table(["Saber", "Conocer"],
                           [["facts and information", "people (with the personal a)"],
                            ["how to do something (saber + infinitive)", "places and things you are familiar with"],
                            ["Sé la respuesta.", "Conozco a tu hermano."],
                            ["No sé dónde está el banco.", "Conozco México."],
                            ["Sé nadar.", "Quiero conocer a tus padres."]],
                           say=[])]),
        card("Notice",
             "Conocer also means “to meet” someone for the first time. Before a specific person, conocer takes the "
             "personal a. Saber is often followed by que, dónde, cuándo or cómo.",
             examples=[
                 ex("Sé que el banco abre a las nueve.", "I know that the bank opens at nine.", "Sé que"),
                 ex("Conozco a la directora del banco.", "I know the director of the bank.", "Conozco a"),
                 ex("Quiero conocer Lima algún día.", "I want to get to know Lima someday.", "conocer Lima"),
                 ex("Mi hermano sabe hablar tres idiomas.", "My brother knows how to speak three languages.", "sabe hablar"),
                 ex("Quiero conocer a tu amigo.", "I want to meet your friend.", "conocer a"),
             ]),
    ],
    exercises=[
        F("Yo no ___ dónde está el banco.", "sé", ["conozco", "conoces", "conoce"], "Information (where) → saber.", tr="I do not know where the bank is.", lemma="saber:yo"),
        F("Yo ___ a la directora del banco.", "conozco", ["sé", "sabes", "sabe"], "A person → conocer + personal a.", tr="I know the director of the bank.", lemma="conocer:yo"),
        F("Mi hermano ___ hablar tres idiomas.", "sabe", ["conoce", "conozco", "conoces"], "How to do something → saber + infinitive.", tr="My brother knows how to speak three languages.", lemma="saber:él"),
        F("Nosotros ___ muy bien la ciudad de Lima.", "conocemos", ["sabemos", "sé", "sabes"], "A place you are familiar with → conocer.", tr="We know the city of Lima very well.", lemma="conocer:nosotros"),
        F("¿Tú ___ que el banco abre a las nueve?", "sabes", ["conoces", "conozco", "conoce"], "Know that + fact → saber.", tr="Do you know that the bank opens at nine?", lemma="saber:tú"),
        M("Which verb do you use for “to meet someone”?", "conocer", ["saber", "ver", "tener"], "Conocer = meet, be acquainted with."),
        M("Which sentence is correct?", "Conozco a tu hermano.", ["Sé a tu hermano.", "Conozco tu hermano.", "Sabo a tu hermano."], "A person: conocer + personal a."),
        M("Which sentence is correct?", "Sé nadar.", ["Conozco nadar.", "Sé a nadar.", "Conozco a nadar."], "Saber + infinitive = know how to."),
        M("What does “Conozco México” mean?", "I am familiar with Mexico.", ["I know that Mexico is big.", "I know how to say Mexico.", "I meet Mexico."], "Conocer + place."),
    ],
)

# ---------------------------------------------------------------------------- 138
L138 = lesson(
    "Saber or conocer? Practice",
    "¿Sabes cocinar? ¿Conoces un buen restaurante?",
    requires=["saber", "conocer", "idioma", "país", "lugar", "ciudad"],
    cards=[
        card("Same sentence, two meanings",
             "Some pairs show how the choice changes the meaning. Compare them.",
             tables=[table(["Con saber", "Con conocer"],
                           [["¿Sabes dónde hay un buen restaurante?", "¿Conoces un buen restaurante?"],
                            ["Sé en qué ciudad vive.", "Conozco la ciudad donde vive."],
                            ["Sé quién es el director.", "Conozco al director."]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Mi amigo ___ hablar cuatro idiomas.", "sabe", ["conoce", "conozco", "conoces"], "How to do something → saber + infinitive.", tr="My friend knows how to speak four languages.", lemma="saber:él"),
        F("Quiero ___ muchos países.", "conocer", ["saber", "decir", "tener"], "To get to know places → conocer.", tr="I want to get to know many countries."),
        F("¿___ tú un buen restaurante cerca de aquí?", "Conoces", ["Sabes", "Conozco", "Sé"], "A place you are familiar with → conocer.", tr="Do you know a good restaurant near here?", lemma="conocer:tú"),
        F("¿___ tú dónde hay un buen restaurante?", "Sabes", ["Conoces", "Conozco", "Conocemos"], "Information (where) → saber.", tr="Do you know where there is a good restaurant?", lemma="saber:tú"),
        F("Ellos ___ que el banco cierra a las cinco.", "saben", ["conocen", "sabe", "conoce"], "Information with que → saber.", tr="They know that the bank closes at five.", lemma="saber:ellos"),
        F("Hoy voy a ___ a mi nuevo jefe.", "conocer", ["saber", "decir", "tener"], "To meet a person → conocer.", tr="Today I am going to meet my new boss."),
        M("Which sentence asks about information?", "¿Sabes dónde está el correo?", ["¿Conoces dónde está el correo?", "¿Sabes a dónde está el correo?", "¿Conoces al correo?"], "Dónde + saber."),
        M("Which sentence means “She knows how to drive”?", "Ella sabe conducir.", ["Ella conoce conducir.", "Ella sabe a conducir.", "Ella conoce a conducir."], "Saber + infinitive."),
        M("Which sentence means “I know your sister”?", "Conozco a tu hermana.", ["Sé a tu hermana.", "Conozco tu hermana.", "Sabo tu hermana."], "A person: conocer a."),
    ],
)

# ---------------------------------------------------------------------------- 139
L139 = lesson(
    "Vos: the forms",
    "vos hablás, vos comés, vos vivís",
    requires=["hablar", "comer", "vivir", "tener", "querer", "ser"],
    cards=[
        card("A second “you”",
             "In many places vos is used instead of tú, or next to it. It is the voseo. The vos verb forms are close "
             "to the vosotros forms, but without the i in -ar and -er verbs. The stress falls on the last syllable, and "
             "forms of two or more syllables have a written accent (sos, vas, ves and das do not).",
             tables=[table(["", "hablar", "comer", "vivir"],
                           [["tú", "hablas", "comes", "vives"],
                            ["vos", "hablás", "comés", "vivís"],
                            ["vosotros", "habláis", "coméis", "vivís"]],
                           say=[1, 2, 3])]),
        card("Stem changers and irregulars",
             "With vos, stem-changing verbs keep the original vowel: querés, podés, dormís, pedís. Verbs that are "
             "irregular in tú are mostly regular in vos: tenés (tienes), venís (vienes), decís (dices). Ser is sos and ir is vas.",
             tables=[table(["Infinitive", "tú", "vos"],
                           [["querer", "quieres", "querés"],
                            ["poder", "puedes", "podés"],
                            ["dormir", "duermes", "dormís"],
                            ["tener", "tienes", "tenés"],
                            ["hacer", "haces", "hacés"],
                            ["decir", "dices", "decís"],
                            ["ser", "eres", "sos"],
                            ["ir", "vas", "vas"]],
                           say=[1, 2])]),
    ],
    exercises=[
        F("Vos ___ muy bien español.", "hablás", ["hablas", "habláis", "hablan"], "Vos + -ás for -ar verbs.", tr="You speak Spanish very well.", lemma="hablar:vos"),
        F("¿Vos ___ comida saludable?", "comés", ["comes", "coméis", "comen"], "Vos + -és for -er verbs.", tr="Do you eat healthy food?", lemma="comer:vos"),
        F("¿Dónde ___ vos?", "vivís", ["vives", "vivo", "viven"], "Vos + -ís for -ir verbs.", tr="Where do you live?", lemma="vivir:vos"),
        F("Vos ___ muy simpático.", "sos", ["eres", "es", "somos"], "Ser: vos sos.", tr="You are very nice.", lemma="ser:vos"),
        F("¿Vos ___ una cuenta bancaria?", "tenés", ["tienes", "tengo", "tiene"], "Tener with vos: tenés.", tr="Do you have a bank account?", lemma="tener:vos"),
        F("¿Vos ___ jugar fútbol esta tarde?", "querés", ["quieres", "queréis", "quiero"], "Querer with vos: querés (no stem change).", tr="Do you want to play soccer this afternoon?", lemma="querer:vos"),
        M("Which form is the vos form of “escribir”?", "escribís", ["escribes", "escribimos", "escribo"], "Same as vosotros for -ir verbs."),
        M("Which is the vos form of “poder”?", "podés", ["puedes", "puedés", "podéis"], "Vos keeps the original vowel."),
        M("How do you say “Do you (vos) do homework on the computer?”", "¿Vos hacés la tarea en la computadora?", ["¿Vos hace la tarea en la computadora?", "¿Vos hago la tarea en la computadora?", "¿Vos hacen la tarea en la computadora?"], "Hacer with vos: hacés."),
    ],
)

# ---------------------------------------------------------------------------- 140
L140 = lesson(
    "Vos: where and how to use it",
    "con vos, para vos, tenés tu libro",
    requires=["tú", "usted", "país", "amigo", "familia", "hablar"],
    cards=[
        card("Where do people say vos?",
             "Vos is the normal everyday “you” in Argentina, Uruguay and Paraguay. In most of Central America it is "
             "used too, often as the more familiar form. In other regions it appears in some areas or only with close "
             "friends. You will hear it a lot in recordings, so you should understand it even if you use tú yourself.",
             tables=[table(["Region", "Familiar “you”"],
                           [["Argentina, Uruguay, Paraguay", "vos"],
                            ["Most of Central America", "vos (and sometimes tú)"],
                            ["Mexico, Spain, Cuba, Puerto Rico", "tú (Spain also vosotros)"]],
                           say=[])]),
        card("Vos in a sentence",
             "Vos works as the subject and after prepositions (con vos, para vos, a vos). But there is no special "
             "possessive or object form for vos: use te, tu and tuyo, exactly like tú.",
             examples=[
                 ex("¿Vos hablás español?", "Do you speak Spanish?", "Vos hablás"),
                 ex("Voy con vos al banco.", "I am going to the bank with you.", "con vos"),
                 ex("Tengo esto para vos.", "I have this for you.", "para vos"),
                 ex("Vos tenés tu libro.", "You have your book.", "tu libro"),
                 ex("¿A qué hora te dormís vos entre semana?", "What time do you go to sleep on weekdays?", "te dormís"),
             ]),
    ],
    exercises=[
        F("Voy con ___ al banco, si querés.", "vos", ["ti", "tú", "yo"], "After a preposition, voseo says vos: con vos.", tr="I am going to the bank with you, if you want."),
        F("En Buenos Aires dicen: “Esto es para ___.”", "vos", ["tú", "te", "yo"], "Para vos in voseo areas.", tr="In Buenos Aires they say: “This is for you.”"),
        F("Vos ___ tu libro en la mesa.", "ponés", ["pones", "ponéis", "pongo"], "Poner with vos: ponés.", tr="You put your book on the table.", lemma="poner:vos"),
        F("¿Vos ___ a las ocho de la mañana?", "te levantás", ["te levantas", "os levantáis", "se levanta"], "Reflexive vos: te levantás.", tr="Do you get up at eight in the morning?"),
        M("Where is vos the usual form among friends?", "Argentina", ["Spain", "Mexico", "Cuba"], "Argentina, Uruguay and Paraguay use vos."),
        M("Which sentence uses vos correctly?", "Vos tenés tu libro.", ["Vos tienes tu libro.", "Vos tenés vuestro libro.", "Vos tiene tu libro."], "Tenés is the vos form; the possessive is tu."),
        M("What is the possessive for vos?", "tu", ["vos", "vuestro", "su"], "Vos has no possessive of its own: tu."),
        M("Which sentence is correct in voseo?", "Yo voy con vos.", ["Yo voy contigo vos.", "Yo voy con vosotros.", "Yo voy con te."], "Con vos."),
        M("What does “Vos sos de Córdoba” mean?", "You are from Córdoba.", ["He is from Córdoba.", "We are from Córdoba.", "I am from Córdoba."], "Sos = you are."),
    ],
)

# ---------------------------------------------------------------------------- 141
L141 = lesson(
    "Ser and estar: the whole picture",
    "ser = what something is; estar = how or where it is",
    requires=["ser", "estar", "maestro", "madera", "lunes", "martes"],
    cards=[
        card("Ser",
             "Ser defines the essence of people, places and things: who they are, where they are from, what they are "
             "like and what they are made of. It is also for the time and the date.",
             tables=[table(["Use of ser", "Example"],
                           [["identity, occupation", "Laura es maestra."],
                            ["origin, nationality", "Lorenzo es de Cuba."],
                            ["description, personality", "Mi mamá es paciente."],
                            ["permanent features, material", "La mesa es de madera."],
                            ["time and date", "Hoy es martes. Son las diez."]],
                           say=[1])]),
        card("Estar",
             "Estar defines the state of people, places and things: where they are, how they feel and what condition "
             "they are in right now. It also forms the progressive.",
             tables=[table(["Use of estar", "Example"],
                           [["location", "Santiago está en Chile."],
                            ["physical state", "Estoy bien, gracias."],
                            ["mood, mental state", "Mi hermana está contenta."],
                            ["non-permanent condition", "La tienda está cerrada hoy."],
                            ["action in progress", "Estoy haciendo la tarea."]],
                           say=[1])]),
        card("The Latin roots",
             "A memory aid: ser comes mainly from the Latin esse, like English “essence”. Estar comes from the Latin stare, "
             "like English “state”. Ser says what the essence is; estar says what state it is in. One exception to "
             "remember: the place of an event uses ser (La reunión es en el banco).",
             examples=[
                 ex("Mi casa es grande, pero hoy está sucia.", "My house is big, but today it is dirty.", "es grande"),
                 ex("La reunión es en el banco.", "The meeting is at the bank.", "es en el banco"),
             ]),
    ],
    exercises=[
        F("Laura ___ maestra.", "es", ["está", "son", "están"], "Occupation → ser.", tr="Laura is a teacher.", lemma="ser:ella"),
        F("Santiago ___ en Chile.", "está", ["es", "son", "están"], "Location → estar.", tr="Santiago is in Chile.", lemma="estar:ella"),
        F("Lorenzo ___ de Cuba.", "es", ["está", "son", "estás"], "Origin → ser.", tr="Lorenzo is from Cuba.", lemma="ser:ella"),
        F("La mesa ___ de madera.", "es", ["está", "son", "estoy"], "Material → ser.", tr="The table is made of wood.", lemma="ser:ella"),
        F("Hoy ___ martes.", "es", ["está", "son", "estoy"], "Date → ser.", tr="Today is Tuesday.", lemma="ser:ella"),
        F("La tienda ___ cerrada hoy.", "está", ["es", "son", "somos"], "Current condition → estar.", tr="The store is closed today.", lemma="estar:ella"),
        F("¿Qué ___ haciendo tú?", "estás", ["eres", "somos", "son"], "Progressive → estar.", tr="What are you doing?", lemma="estar:tú"),
        M("Which Latin verb gives us “estar”?", "stare", ["esse", "ester", "serere"], "Stare → state."),
        M("Which sentence describes where something is?", "Mi casa está cerca del banco.", ["Mi casa es cerca del banco.", "Mi casa son cerca del banco.", "Mi casa soy cerca del banco."], "Location → estar."),
        M("Which sentence tells the time?", "Son las diez.", ["Están las diez.", "Es las diez.", "Está las diez."], "Time: ser, plural from las diez."),
    ],
)

# ---------------------------------------------------------------------------- 142
L142 = lesson(
    "Ser and estar in a story",
    "Mariana es ciclista. Ahora está en Perú.",
    requires=["ser", "estar", "país", "viaje", "cansado", "contento"],
    cards=[
        card("Mariana, cyclist",
             "Read the story and notice why each verb is ser or estar.",
             examples=[
                 ex("Mariana es ciclista y es de Costa Rica.", "Mariana is a cyclist and is from Costa Rica.", "es ciclista"),
                 ex("Ahora está en Perú porque participa en una carrera.", "Now she is in Peru because she is in a race.", "está en Perú"),
                 ex("Su bicicleta es roja y es de aluminio.", "Her bicycle is red and is made of aluminum.", "es de aluminio"),
                 ex("Hoy está cansada, pero está muy contenta.", "Today she is tired, but she is very happy.", "está cansada"),
                 ex("En este momento está hablando con su entrenador.", "Right now she is talking with her coach.", "está hablando"),
                 ex("Son las siete de la tarde y el hotel está tranquilo.", "It is seven in the evening and the hotel is quiet.", "Son las siete"),
             ]),
    ],
    exercises=[
        F("Mariana ___ ciclista.", "es", ["está", "son", "estoy"], "Occupation → ser.", tr="Mariana is a cyclist.", lemma="ser:ella"),
        F("Ahora Mariana ___ en Perú.", "está", ["es", "son", "somos"], "Location → estar.", tr="Now Mariana is in Peru.", lemma="estar:ella"),
        F("Su bicicleta ___ de aluminio.", "es", ["está", "son", "estoy"], "Material → ser.", tr="Her bicycle is made of aluminum.", lemma="ser:ella"),
        F("Hoy ella ___ cansada después de la carrera.", "está", ["es", "son", "somos"], "A state after the race → estar.", tr="Today she is tired after the race.", lemma="estar:ella"),
        F("En este momento ella ___ hablando con su entrenador.", "está", ["es", "son", "somos"], "Progressive → estar.", tr="Right now she is talking with her coach.", lemma="estar:ella"),
        F("___ las siete de la tarde.", "Son", ["Es", "Están", "Está"], "Time: Son las siete.", tr="It is seven in the evening.", lemma="ser:ellos"),
        M("Which sentence describes origin?", "Mariana es de Costa Rica.", ["Mariana está de Costa Rica.", "Mariana son de Costa Rica.", "Mariana estoy de Costa Rica."], "Origin → ser."),
        M("Which sentence describes a temporary state?", "El hotel está tranquilo esta noche.", ["El hotel es de madera.", "El hotel es grande.", "El hotel es famoso."], "This evening → estar."),
        M("Which sentence describes the material?", "La bicicleta es de aluminio.", ["La bicicleta está de aluminio.", "La bicicleta son de aluminio.", "La bicicleta estás de aluminio."], "Material → ser."),
    ],
)

# ---------------------------------------------------------------------------- 143
L143 = lesson(
    "Por and para, part 2",
    "por: exchange, means, through; para: recipient, goal, deadline, destination",
    requires=["por", "para", "pagar", "comprar", "tren", "teléfono"],
    cards=[
        card("Four uses of por",
             "Por looks at the way or the exchange: what you give, by what means you send or communicate, and through or along "
             "what. To travel in a vehicle, use en: voy en autobús.",
             tables=[table(["Use of por", "Example"],
                           [["in exchange for", "Compro una blusa por diez pesos."],
                            ["means of sending", "Mando la carta por avión."],
                            ["manner or means", "Voy a llamar a Ana por teléfono."],
                            ["through, along", "Camino por el campo cuando voy a clase."]],
                           say=[1])]),
        card("Four uses of para",
             "Para looks forward to a goal: the person who receives something, the purpose, the deadline and the "
             "destination.",
             tables=[table(["Use of para", "Example"],
                           [["intended for someone", "Compro una blusa para mi madre."],
                            ["purpose, in order to", "Para tocar el piano necesito lecciones."],
                            ["deadline", "Tengo que pagar la cuenta para el lunes."],
                            ["destination", "Mañana salgo para Cancún."]],
                           say=[1])],
             examples=[
                 ex("Esta maleta es para el viaje.", "This suitcase is for the trip.", "para el viaje"),
                 ex("Envío el paquete por avión.", "I send the package by air mail.", "por avión"),
             ]),
    ],
    exercises=[
        F("Compro una blusa ___ diez pesos.", "por", ["para", "sin", "hacia"], "In exchange for → por.", tr="I buy a blouse for ten pesos."),
        F("Mando la carta ___ avión.", "por", ["para", "con", "a"], "Means of sending → por.", tr="I send the letter by air mail."),
        F("Voy a llamar a Ana ___ teléfono.", "por", ["para", "con", "de"], "Means → por.", tr="I am going to call Ana by phone."),
        F("Camino ___ el parque cuando voy a clase.", "por", ["para", "a", "en"], "Through → por.", tr="I walk through the park when I go to class."),
        F("Compro un regalo ___ mi madre.", "para", ["por", "con", "de"], "Recipient → para.", tr="I am buying a gift for my mother."),
        F("___ tocar el piano necesitamos lecciones.", "Para", ["Por", "Con", "En"], "Purpose → para.", tr="In order to play the piano we need lessons."),
        F("Tengo que pagar la cuenta ___ el lunes.", "para", ["por", "con", "en"], "Deadline → para.", tr="I have to pay the bill by Monday."),
        F("Mañana salgo ___ Cancún.", "para", ["por", "de", "con"], "Destination → para.", tr="Tomorrow I leave for Cancún."),
        M("Which preposition shows a deadline?", "para", ["por", "con", "sin"], "Para el lunes = by Monday."),
    ],
)

# ---------------------------------------------------------------------------- 144
L144 = lesson(
    "Por or para? Practice",
    "una carta con por y para",
    requires=["por", "para", "viaje", "tren", "cuenta", "banco"],
    cards=[
        card("An e-mail to a friend",
             "Read the e-mail and notice the reason for each por and para.",
             examples=[
                 ex("La próxima semana voy a Lima para empezar un trabajo nuevo.", "Next week I am going to Lima to start a new job.", "para empezar"),
                 ex("Viajo en tren hasta el aeropuerto.", "I travel by train to the airport.", "en tren"),
                 ex("Primero voy al banco para abrir una cuenta.", "First I go to the bank to open an account.", "para abrir"),
                 ex("Tengo que hacerlo para el lunes.", "I have to do it by Monday.", "para el lunes"),
                 ex("Después paso por la oficina de correos.", "Afterwards I stop by the post office.", "paso por"),
                 ex("Te escribo por correo electrónico. Gracias por tu amistad.", "I write to you by e-mail. Thanks for your friendship.", "por correo electrónico"),
             ]),
    ],
    exercises=[
        F("Voy a Lima ___ empezar un trabajo nuevo.", "para", ["por", "con", "de"], "Purpose → para.", tr="I am going to Lima to start a new job."),
        F("Paso ___ el centro de la ciudad.", "por", ["con", "de", "sin"], "Through → por.", tr="I pass through the city center."),
        F("Voy al banco ___ abrir una cuenta.", "para", ["por", "con", "de"], "Purpose → para.", tr="I go to the bank to open an account."),
        F("Tengo que pagar la cuenta ___ el viernes.", "para", ["por", "con", "en"], "Deadline → para.", tr="I have to pay the bill by Friday."),
        F("Paso ___ el banco camino a casa.", "por", ["para", "con", "de"], "Through, by → por.", tr="I pass by the bank on the way home."),
        F("Te escribo ___ correo electrónico.", "por", ["para", "con", "de"], "Means → por.", tr="I write to you by e-mail."),
        F("Cambio euros ___ soles en el banco.", "por", ["para", "con", "de"], "Exchange → por.", tr="I exchange euros for soles at the bank."),
        F("Gracias ___ tu amistad.", "por", ["para", "con", "de"], "Thanks for → por.", tr="Thanks for your friendship."),
        M("Which sentence says the letter is for you (you will receive it)?", "Esta carta es para ti.", ["Esta carta es hacia ti.", "Esta carta es con ti.", "Esta carta es sin ti."], "Recipient → para."),
    ],
)

# ---------------------------------------------------------------------------- 145
L145 = lesson(
    "Moving house: advice",
    "hay que avisar, tenemos que cancelar, debemos hacer una lista",
    requires=["mudar", "casa", "contrato", "seguro", "escuela", "lista"],
    cards=[
        card("Before a move",
             "A mudanza (move) needs planning. These phrases are useful for giving general advice: hay que + "
             "infinitive, tener que + infinitive, deber + infinitive.",
             tables=[table(["Advice", "English"],
                           [["Hay que hacer una lista.", "You have to make a list."],
                            ["Tenemos que avisar a los amigos.", "We have to let our friends know."],
                            ["Debemos cancelar la luz y el agua.", "We should cancel electricity and water."],
                            ["Es bueno hablar con el veterinario.", "It is good to talk to the vet."]],
                           say=[0])]),
        card("Who to tell",
             "When you move, notify the people and offices that need your new address.",
             tables=[table(["A quién", "Qué hacer"],
                           [["el banco", "avisar del cambio de dirección"],
                            ["la oficina de correos", "dar la nueva dirección"],
                            ["la compañía de seguros", "hacer un seguro nuevo"],
                            ["las compañías de servicios", "cancelar los servicios y contratar los nuevos"],
                            ["la escuela", "cambiar a los niños de escuela"],
                            ["el veterinario", "preguntar por las mascotas"]],
                           say=[0, 1])]),
    ],
    exercises=[
        F("Antes de mudarnos, ___ que hacer una lista.", "hay", ["es", "está", "hace"], "Hay que + infinitive.", tr="Before moving, you have to make a list."),
        F("Nosotros ___ que avisar al banco.", "tenemos", ["tienen", "tengo", "tiene"], "Nosotros tenemos que + infinitive.", tr="We have to let the bank know.", lemma="tener:nosotros"),
        F("Debemos ___ la luz de la casa vieja.", "cancelar", ["contratar", "empacar", "firmar"], "You cancel the old service.", tr="We should cancel electricity at the old house."),
        F("En la casa nueva hay que ___ el agua y el gas.", "contratar", ["cancelar", "perder", "romper"], "You sign up for services at the new home.", tr="In the new house you have to sign up for water and gas."),
        M("What does “mudarse” mean?", "to move to a new home", ["to wake up", "to be silent", "to travel by train"], "Mudarse = to move."),
        M("Which sentence is general advice?", "Hay que avisar a los amigos.", ["Avisé a mis amigos.", "Estoy avisando a mis amigos.", "Yo aviso a los amigos ahora."], "Hay que + infinitive = general advice."),
        M("Who needs to know the new address?", "el banco y la oficina de correos", ["solo el veterinario", "nadie", "solo la cocina"], "Notify all offices."),
        M("What is “el seguro” in the list?", "insurance", ["lock", "list", "school"], "Seguro = insurance."),
        M("Which sentence matches the advice “you have to talk to the vet”?", "Hay que hablar con el veterinario.", ["Hay que hablar sin el veterinario.", "Hay que hablar en el veterinario.", "Hay que hablar hacia el veterinario."], "Hablar con."),
    ],
)

# ---------------------------------------------------------------------------- 146
L146 = lesson(
    "Review: errands and irregular verbs",
    "trámites, verbos irregulares, saber/conocer, ser/estar, por/para",
    requires=["banco", "cuenta", "saber", "conocer", "ser", "estar"],
    cards=[
        card("Quick map",
             "Irregular presents come in families. Saber is for facts and skills; conocer is for people and places. Ser "
             "is essence; estar is state. Por is exchange and means; para is goal and destination.",
             tables=[table(["Idea", "Example"],
                           [["-zco", "Conozco a tu hermano."],
                            ["-uir", "El precio incluye el agua."],
                            ["vos", "Vos tenés una cuenta."],
                            ["ser", "El banco es grande."],
                            ["estar", "El banco está cerrado hoy."],
                            ["por", "Pago por Internet."],
                            ["para", "Voy al banco para abrir una cuenta."]],
                           say=[1])]),
    ],
    exercises=[
        F("Yo ___ a tu hermano.", "conozco", ["sé", "sabes", "conoce"], "A person → conocer.", tr="I know your brother.", lemma="conocer:yo"),
        F("Yo no ___ dónde está la oficina.", "sé", ["conozco", "sabes", "conoce"], "Information → saber.", tr="I do not know where the office is.", lemma="saber:yo"),
        F("Los precios ___ el servicio de agua.", "incluyen", ["incluye", "incluimos", "incluyo"], "Incluir: ellos incluyen.", tr="The prices include water service.", lemma="incluir:ellos"),
        F("Vos ___ una cuenta de ahorros.", "tenés", ["tienes", "tengo", "tiene"], "Tener with vos: tenés.", tr="You have a savings account.", lemma="tener:vos"),
        F("El banco ___ cerrado los domingos.", "está", ["es", "son", "están"], "A condition → estar.", tr="The bank is closed on Sundays.", lemma="estar:ella"),
        F("Voy al banco ___ abrir una cuenta.", "para", ["por", "con", "de"], "Purpose → para.", tr="I go to the bank to open an account."),
        F("Pago la cuenta ___ Internet.", "por", ["para", "con", "de"], "Means → por.", tr="I pay the bill online."),
        M("Which sentence is correct?", "Mi hermano sabe conducir.", ["Mi hermano conoce conducir.", "Mi hermano sabe a conducir.", "Mi hermano conoce a conducir."], "Saber + infinitive."),
        M("Which is the vos form of “hacer”?", "hacés", ["haces", "hacéis", "hago"], "Hacés."),
        M("Which sentence is correct?", "Hoy es martes.", ["Hoy está martes.", "Hoy son martes.", "Hoy soy martes."], "Date → ser."),
    ],
)

UNIT = unit("Trámites y servicios", [L129, L130, L131, L132, L133, L134, L135, L136, L137, L138, L139, L140, L141, L142, L143, L144, L145, L146])

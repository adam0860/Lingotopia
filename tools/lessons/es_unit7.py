"""Unit 7: clothing (textbook Chapter 6)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 82
L82 = lesson(
    "Clothes",
    "la camisa, los pantalones, el vestido",
    requires=["ropa", "camisa", "pantalón", "vestido", "zapato", "llevar"],
    cards=[
        card("What people wear",
             "Learn each garment with its article, because gender is part of the word. Some garments are "
             "usually plural, like English “pants”: los pantalones, las gafas, los jeans. For “to wear”, "
             "Spanish uses llevar or usar. La ropa (clothing) is a collective noun used in the singular: mucha ropa.",
             tables=[table(["Prenda", "English"],
                           [["la camisa", "shirt"],
                            ["la camiseta", "T-shirt"],
                            ["la blusa", "blouse"],
                            ["los pantalones", "pants"],
                            ["la falda", "skirt"],
                            ["el vestido", "dress"],
                            ["la chaqueta", "jacket"],
                            ["el abrigo", "coat"],
                            ["el suéter", "sweater"],
                            ["el traje", "suit"],
                            ["los zapatos", "shoes"],
                            ["las botas", "boots"],
                            ["los calcetines", "socks"]],
                           say=[0])]),
        card("Putting it in sentences",
             "Use llevar or usar with the garment. Remember that adjectives follow the noun and agree with it.",
             examples=[
                 ex("Llevo una camisa blanca y pantalones azules.", "I am wearing a white shirt and blue pants.", "Llevo una camisa blanca"),
                 ex("Ella usa una falda negra.", "She wears a black skirt.", "Ella usa una falda negra."),
                 ex("Necesito un abrigo para el invierno.", "I need a coat for the winter.", "un abrigo"),
                 ex("Mis zapatos son nuevos.", "My shoes are new.", "Mis zapatos son nuevos."),
             ]),
    ],
    exercises=[
        F("En invierno necesito un ___ grueso.", "abrigo", ["falda", "blusa", "camiseta"], "Un is masculine, so the noun must be masculine: abrigo.",
          tr="In winter I need a thick coat."),
        F("Ella usa una ___ negra.", "falda", ["abrigo", "traje", "suéter"], "Una is feminine, so falda.", tr="She wears a black skirt."),
        F("Mis ___ son nuevos.", "zapatos", ["zapato", "camisa", "falda"], "Plural masculine to match nuevos: zapatos.", tr="My shoes are new."),
        F("Hoy llevo ___ azules.", "pantalones", ["pantalona", "camisas", "falda"], "Azules is plural, so a plural noun: pantalones.", tr="Today I am wearing blue pants."),
        F("Yo ___ una camisa blanca.", "llevo", ["llevas", "lleva", "llevan"], "Yo llevo.", tr="I am wearing a white shirt.", lemma="llevar:yo"),
        F("Mis hermanas ___ vestidos largos.", "llevan", ["lleva", "llevo", "llevamos"], "Mis hermanas is they: llevan.", tr="My sisters wear long dresses.", lemma="llevar:ellas"),
        M("Which garment goes on your feet?", "las botas", ["la bufanda", "el traje", "la blusa"], "Boots are shoes."),
        M("Which noun means “clothing” in general (singular)?", "la ropa", ["los ropas", "la ropas", "el ropo"], "La ropa is normally used in the singular."),
        M("Which is correct?", "Mi chaqueta es negra.", ["Mi chaqueta es negro.", "Mi chaqueta son negra.", "Mi chaqueta es negras."], "Chaqueta is feminine singular."),
        M("What does “llevar” mean here? “Llevo un traje.”", "to wear", ["to carry only", "to lose", "to buy"], "Llevar also means to wear."),
    ],
)

# ---------------------------------------------------------------------------- 83
L83 = lesson(
    "Accessories, fabrics and patterns",
    "el cinturón, de algodón, de rayas",
    requires=["algodón", "cuero", "cuadro", "bolso", "cinturón", "sombrero"],
    cards=[
        card("Accessories",
             "Accessories are accesorios. Gafas (glasses) and guantes (gloves) normally appear in the plural.",
             tables=[table(["Accesorio", "English"],
                           [["el sombrero", "hat"],
                            ["la gorra", "cap"],
                            ["la corbata", "tie"],
                            ["el cinturón", "belt"],
                            ["la bufanda", "scarf"],
                            ["los guantes", "gloves"],
                            ["las gafas", "glasses"],
                            ["el bolso", "purse, bag"],
                            ["el reloj", "watch"]],
                           say=[0])]),
        card("Fabrics and patterns",
             "To say what something is made of, use de: una camisa de algodón, un cinturón de cuero. Patterns "
             "also use de: una camisa de rayas (striped), de cuadros (checked). A garment with no pattern is liso.",
             tables=[table(["Material o diseño", "English"],
                           [["de algodón", "cotton"],
                            ["de lana", "wool"],
                            ["de seda", "silk"],
                            ["de cuero", "leather"],
                            ["de rayas", "striped"],
                            ["de cuadros", "checked"],
                            ["liso", "plain"]],
                           say=[0])],
             examples=[
                 ex("Mi camisa es de algodón.", "My shirt is made of cotton.", "de algodón"),
                 ex("Quiero un cinturón de cuero.", "I want a leather belt.", "de cuero"),
                 ex("Ella lleva una bufanda de lana.", "She is wearing a wool scarf.", "de lana"),
                 ex("Tengo una corbata de rayas.", "I have a striped tie.", "de rayas"),
             ]),
    ],
    exercises=[
        F("Mi camisa es ___ algodón.", "de", ["en", "con", "por"], "Material: de.", tr="My shirt is made of cotton."),
        F("Quiero un cinturón de ___.", "cuero", ["cuadros", "lisa", "lana"], "Leather is cuero: un cinturón de cuero.", tr="I want a leather belt."),
        F("Ella lleva una ___ de lana.", "bufanda", ["cinturón", "sombrero", "bolso"], "Una is feminine: bufanda.", tr="She is wearing a wool scarf."),
        F("En invierno uso ___ en las manos.", "guantes", ["gafas", "botas", "relojes"], "Gloves go on the hands.", tr="In winter I wear gloves on my hands."),
        F("Mi corbata es de ___.", "rayas", ["cuero", "lana", "bolso"], "Ties with a pattern: de rayas.", tr="My tie is striped."),
        F("Necesito un ___ para el sol.", "sombrero", ["bufanda", "abrigo", "guantes"], "A hat protects from the sun; un is masculine.", tr="I need a hat for the sun."),
        M("Which means “striped”?", "de rayas", ["de cuadros", "de seda", "liso"], "Rayas = stripes."),
        M("Which means “plain” (no pattern)?", "liso", ["de rayas", "de cuadros", "de algodón"], "Liso = plain."),
        M("Which accessory tells the time?", "el reloj", ["el cinturón", "la gorra", "las gafas"], "Reloj = watch."),
        M("Which sentence is correct?", "Los guantes son de cuero.", ["Los guantes es de cuero.", "Los guantes son cuero de.", "Los guantes son de cueros."], "Plural subject, plural verb, material in the singular."),
    ],
)

# ---------------------------------------------------------------------------- 84
L84 = lesson(
    "Shopping for clothes",
    "¿Cuánto cuesta? ¿Qué talla usa?",
    requires=["tienda", "cliente", "pagar", "costar", "oferta", "efectivo", "tarjeta"],
    cards=[
        card("In the store",
             "Shopping has its own vocabulary. The person who helps you is el dependiente or la dependiente. "
             "You pay at la caja. The price is el precio, and a sale is una oferta or una rebaja.",
             tables=[table(["Palabra", "English"],
                           [["la tienda", "store"],
                            ["el dependiente, la dependiente", "salesperson"],
                            ["el cliente, la cliente", "customer"],
                            ["la talla", "size (clothes)"],
                            ["el número", "size (shoes)"],
                            ["el probador", "fitting room"],
                            ["la caja", "cash register"],
                            ["el precio", "price"],
                            ["la oferta", "sale, special offer"],
                            ["en efectivo", "in cash"],
                            ["con tarjeta", "by card"]],
                           say=[0])]),
        card("Useful questions",
             "Costar is a stem-changing verb (cuesta, cuestan); you will study that pattern in the next lessons. For now, "
             "learn these questions as ready-made phrases. Use usted with salespeople.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Cuánto cuesta esta camisa?", "Cuesta veinte dólares."],
                            ["¿Cuánto cuestan los zapatos?", "Cuestan cincuenta dólares."],
                            ["¿Qué talla usa usted?", "Uso la talla mediana."],
                            ["¿Puedo pagar con tarjeta?", "Sí, claro."],
                            ["¿Paga en efectivo?", "Sí, pago en efectivo."]],
                           say=[0, 1])],
             examples=[
                 ex("La chaqueta me queda grande.", "The jacket is too big for me.", "me queda grande"),
                 ex("Los zapatos me quedan bien.", "The shoes fit me well.", "me quedan bien"),
             ]),
    ],
    exercises=[
        F("¿Cuánto ___ esta camisa?", "cuesta", ["cuestan", "cuestas", "costar"], "Camisa is singular: cuesta.", tr="How much does this shirt cost?"),
        F("¿Cuánto ___ los zapatos?", "cuestan", ["cuesta", "cuestas", "costamos"], "Zapatos is plural: cuestan.", tr="How much do the shoes cost?"),
        F("Pago en ___.", "efectivo", ["tarjeta", "talla", "oferta"], "En efectivo = in cash.", tr="I pay in cash."),
        F("¿Puedo pagar ___ tarjeta?", "con", ["en", "de", "por"], "Con tarjeta = by card.", tr="Can I pay by card?"),
        F("La chaqueta me queda ___.", "grande", ["grandes", "mucho", "tallas"], "Me queda grande = it is too big on me.", tr="The jacket is too big for me."),
        M("Who helps you in a store?", "el dependiente", ["el cliente", "el probador", "el precio"], "Dependiente = salesperson."),
        M("Where do you try on clothes?", "en el probador", ["en la caja", "en la talla", "en el cliente"], "Probador = fitting room."),
        M("Which word is for shoe size?", "el número", ["la talla", "la caja", "el precio"], "Number for shoes; talla for clothes."),
        M("Which means “on sale”?", "en oferta", ["en efectivo", "en la caja", "en talla"], "Oferta = special offer."),
        M("You want to know the price of a hat. What do you ask?", "¿Cuánto cuesta este sombrero?", ["¿Cuántos cuesta este sombrero?", "¿Qué talla es este sombrero?", "¿Cuándo cuesta este sombrero?"], "Cuánto cuesta + singular noun."),
    ],
)

# ---------------------------------------------------------------------------- 85
L85 = lesson(
    "Boot verbs 1: o becomes ue",
    "puedo, vuelvo, duermo, cuesta",
    requires=["poder", "volver", "dormir", "contar", "encontrar", "costar", "jugar"],
    cards=[
        card("The boot",
             "In many verbs, the vowel in the stem changes in the yo, tú, él and ellos forms, but not in nosotros "
             "or vosotros. On a chart those forms make the shape of a boot, which is why these are called boot verbs. "
             "In this group o becomes ue. The endings are the normal ones.",
             tables=[table(["", "poder", "volver", "dormir"],
                           [["yo", "puedo", "vuelvo", "duermo"],
                            ["tú", "puedes", "vuelves", "duermes"],
                            ["él, ella, usted", "puede", "vuelve", "duerme"],
                            ["nosotros", "podemos", "volvemos", "dormimos"],
                            ["vosotros", "podéis", "volvéis", "dormís"],
                            ["ellos, ellas, ustedes", "pueden", "vuelven", "duermen"]],
                           say=[1, 2, 3])]),
        card("More o → ue verbs",
             "Almorzar (to have lunch), contar (to count, to tell), costar (to cost), encontrar (to find) and "
             "soñar (to dream) follow the same pattern. Jugar changes u to ue: juego, juegas, juega, jugamos, jugáis, "
             "juegan. In Spain, jugar takes a plus the sport (juego al fútbol); in much of Latin America people also say juego fútbol.",
             examples=[
                 ex("Puedo ayudarte hoy.", "I can help you today.", "Puedo"),
                 ex("Mi hermano duerme ocho horas.", "My brother sleeps eight hours.", "duerme"),
                 ex("Nosotros volvemos a casa a las cinco.", "We return home at five.", "volvemos"),
                 ex("Los niños juegan al fútbol.", "The children play soccer.", "juegan al fútbol"),
                 ex("Los zapatos cuestan cien dólares.", "The shoes cost one hundred dollars.", "cuestan"),
             ]),
    ],
    exercises=[
        F("Yo ___ ayudarte hoy.", "puedo", ["podo", "puede", "podemos"], "Yo puedo.", tr="I can help you today.", lemma="poder:yo"),
        F("Mi hermano ___ ocho horas.", "duerme", ["dormo", "dormimos", "duermen"], "Mi hermano is he: duerme.", tr="My brother sleeps eight hours.", lemma="dormir:él"),
        F("Nosotros ___ a casa a las cinco.", "volvemos", ["vuelvemos", "vuelven", "volvamos"], "Nosotros does not change the stem: volvemos.", tr="We return home at five.", lemma="volver:nosotros"),
        F("¿A qué hora ___ tú?", "almuerzas", ["almorzas", "almorzamos", "almuerzan"], "Tú almuerzas.", tr="What time do you have lunch?", lemma="almorzar:tú"),
        F("Los niños ___ al fútbol.", "juegan", ["jugan", "juega", "jugamos"], "Jugar becomes juegan with ellos.", tr="The children play soccer.", lemma="jugar:ellos"),
        F("Vosotros ___ mucho por la noche.", "dormís", ["duermís", "duermen", "dormimos"], "Vosotros keeps the stem: dormís.", tr="You (all) sleep a lot at night.", lemma="dormir:vosotros"),
        F("Los zapatos ___ cien dólares.", "cuestan", ["costan", "cuesta", "costamos"], "Zapatos is plural: cuestan.", tr="The shoes cost one hundred dollars.", lemma="costar:ellos"),
        F("Yo ___ mis llaves en la mesa.", "encuentro", ["encontro", "encuentra", "encontramos"], "Yo encuentro.", tr="I find my keys on the table.", lemma="encontrar:yo"),
        M("Which two forms do NOT change the stem?", "nosotros and vosotros", ["yo and tú", "él and ellos", "yo and nosotros"], "The boot excludes nosotros and vosotros."),
        M("Which is the only verb where u becomes ue?", "jugar", ["poder", "dormir", "volver"], "Juego, juegas, juega…"),
    ],
    verify=vp("poder", "puedo", "puedes", "puede", "podemos", "podéis", "pueden")
           + vp("volver", "vuelvo", "vuelves", "vuelve", "volvemos", "volvéis", "vuelven")
           + vp("dormir", "duermo", "duermes", "duerme", "dormimos", "dormís", "duermen")
           + vp("jugar", "juego", "juegas", "juega", "jugamos", "jugáis", "juegan"),
)

# ---------------------------------------------------------------------------- 86
L86 = lesson(
    "Boot verbs 2: e becomes ie",
    "quiero, pienso, cierro, prefiero",
    requires=["querer", "pensar", "cerrar", "empezar", "entender", "perder", "preferir"],
    cards=[
        card("The e → ie group",
             "The second group changes e to ie in the same four forms (yo, tú, él, ellos). Nosotros and "
             "vosotros stay regular.",
             tables=[table(["", "querer", "cerrar", "preferir"],
                           [["yo", "quiero", "cierro", "prefiero"],
                            ["tú", "quieres", "cierras", "prefieres"],
                            ["él, ella, usted", "quiere", "cierra", "prefiere"],
                            ["nosotros", "queremos", "cerramos", "preferimos"],
                            ["vosotros", "queréis", "cerráis", "preferís"],
                            ["ellos, ellas, ustedes", "quieren", "cierran", "prefieren"]],
                           say=[1, 2, 3])]),
        card("More e → ie verbs",
             "Pensar (to think), empezar and comenzar (to begin), entender (to understand) and perder (to lose; to "
             "miss) follow the same pattern. When a verb is a boot verb, dictionaries mark it: cerrar (ie), poder (ue).",
             examples=[
                 ex("Quiero comprar una chaqueta.", "I want to buy a jacket.", "Quiero comprar"),
                 ex("La tienda cierra a las nueve.", "The store closes at nine.", "cierra"),
                 ex("Prefiero usar ropa cómoda.", "I prefer to wear comfortable clothes.", "Prefiero usar"),
                 ex("¿Entiendes estas instrucciones?", "Do you understand these instructions?", "¿Entiendes"),
                 ex("Pensamos viajar en verano.", "We plan to travel in summer.", "Pensamos viajar"),
             ]),
    ],
    exercises=[
        F("Yo ___ comprar una chaqueta.", "quiero", ["quero", "quiere", "queremos"], "Yo quiero.", tr="I want to buy a jacket.", lemma="querer:yo"),
        F("La tienda ___ a las nueve.", "cierra", ["cerra", "cierran", "cerramos"], "La tienda is it: cierra.", tr="The store closes at nine.", lemma="cerrar:ella"),
        F("Mis padres ___ viajar en verano.", "piensan", ["pensan", "piensa", "pensamos"], "Mis padres is they: piensan.", tr="My parents plan to travel in summer.", lemma="pensar:ellos"),
        F("Nosotros ___ usar ropa cómoda.", "preferimos", ["prefierimos", "prefieren", "prefiero"], "Nosotros keeps the stem: preferimos.", tr="We prefer to wear comfortable clothes.", lemma="preferir:nosotros"),
        F("¿Tú ___ estas instrucciones?", "entiendes", ["entendes", "entiende", "entendemos"], "Tú entiendes.", tr="Do you understand these instructions?", lemma="entender:tú"),
        F("La clase ___ a las ocho.", "empieza", ["empeza", "empiezan", "empezamos"], "La clase is it: empieza.", tr="The class begins at eight.", lemma="empezar:ella"),
        F("Vosotros ___ la puerta.", "cerráis", ["cierráis", "cierran", "cerramos"], "Vosotros keeps the stem: cerráis.", tr="You (all) close the door.", lemma="cerrar:vosotros"),
        F("Yo nunca ___ mis llaves.", "pierdo", ["perdo", "pierde", "perdemos"], "Yo pierdo.", tr="I never lose my keys.", lemma="perder:yo"),
        M("How does the dictionary mark “cerrar”?", "cerrar (ie)", ["cerrar (ue)", "cerrar (i)", "cerrar (ee)"], "Boot verbs are marked with the change."),
        M("Which sentence is correct?", "Mi hermana quiere un abrigo nuevo.", ["Mi hermana quere un abrigo nuevo.", "Mi hermana quieren un abrigo nuevo.", "Mi hermana queremos un abrigo nuevo."], "Singular él/ella form: quiere."),
    ],
    verify=vp("querer", "quiero", "quieres", "quiere", "queremos", "queréis", "quieren")
           + vp("cerrar", "cierro", "cierras", "cierra", "cerramos", "cerráis", "cierran")
           + vp("preferir", "prefiero", "prefieres", "prefiere", "preferimos", "preferís", "prefieren"),
)

# ---------------------------------------------------------------------------- 87
L87 = lesson(
    "Boot verbs 3: e becomes i",
    "pido, sirvo, repito, visto",
    requires=["pedir", "servir", "repetir", "elegir", "decir"],
    cards=[
        card("The e → i group",
             "A smaller group changes e to i in the boot forms. All are -ir verbs.",
             tables=[table(["", "pedir", "servir", "repetir"],
                           [["yo", "pido", "sirvo", "repito"],
                            ["tú", "pides", "sirves", "repites"],
                            ["él, ella, usted", "pide", "sirve", "repite"],
                            ["nosotros", "pedimos", "servimos", "repetimos"],
                            ["vosotros", "pedís", "servís", "repetís"],
                            ["ellos, ellas, ustedes", "piden", "sirven", "repiten"]],
                           say=[1, 2, 3])]),
        card("Others in this group",
             "Vestir (to dress), competir (to compete), elegir (to choose) and decir (to say; to tell) also belong "
             "here. Decir has an irregular yo form: digo, dices, dice, decimos, decís, dicen. Elegir changes g to j "
             "in yo: elijo.",
             examples=[
                 ex("Yo siempre pido ensalada en ese restaurante.", "I always order salad at that restaurant.", "pido"),
                 ex("El camarero sirve a los clientes.", "The waiter serves the customers.", "sirve"),
                 ex("Los niños piden regalos en Navidad.", "Children ask for presents at Christmas.", "piden"),
                 ex("Elijo la camisa azul.", "I choose the blue shirt.", "Elijo"),
                 ex("Digo la verdad.", "I tell the truth.", "Digo"),
             ]),
    ],
    exercises=[
        F("Yo siempre ___ ensalada en ese restaurante.", "pido", ["pedes", "pide", "pedimos"], "Yo pido.", tr="I always order salad at that restaurant.", lemma="pedir:yo"),
        F("El camarero ___ a los clientes.", "sirve", ["serve", "sirven", "servimos"], "El camarero is he: sirve.", tr="The waiter serves the customers.", lemma="servir:él"),
        F("Los niños ___ regalos en Navidad.", "piden", ["pidan", "pide", "pedimos"], "Los niños is they: piden.", tr="Children ask for presents at Christmas.", lemma="pedir:ellos"),
        F("Nosotros ___ las palabras en clase.", "repetimos", ["repitimos", "repiten", "repito"], "Nosotros keeps the stem: repetimos.", tr="We repeat the words in class.", lemma="repetir:nosotros"),
        F("Yo ___ la camisa azul.", "elijo", ["elego", "elige", "elegimos"], "Elegir: yo elijo.", tr="I choose the blue shirt.", lemma="elegir:yo"),
        F("Yo ___ la verdad.", "digo", ["dico", "dice", "decimos"], "Decir: yo digo.", tr="I tell the truth.", lemma="decir:yo"),
        F("¿Qué ___ tú?", "dices", ["dice", "dicen", "digo"], "Tú dices.", tr="What do you say?", lemma="decir:tú"),
        M("In which group do “pedir” and “servir” belong?", "e → i", ["o → ue", "e → ie", "u → ue"], "Pido, sirvo."),
        M("What is the yo form of “decir”?", "digo", ["dico", "dizo", "diego"], "Decir has an irregular yo form."),
    ],
    verify=vp("pedir", "pido", "pides", "pide", "pedimos", "pedís", "piden")
           + vp("servir", "sirvo", "sirves", "sirve", "servimos", "servís", "sirven")
           + vp("repetir", "repito", "repites", "repite", "repetimos", "repetís", "repiten")
           + vp("decir", "digo", "dices", "dice", "decimos", "decís", "dicen"),
)

# ---------------------------------------------------------------------------- 88
L88 = lesson(
    "Boot verbs: which pattern?",
    "o → ue, e → ie, e → i",
    requires=["poder", "querer", "pedir", "volver", "pensar", "servir"],
    cards=[
        card("Sort the verbs by pattern",
             "Boot verbs follow three main patterns (plus jugar, which changes u to ue). When you learn a new verb, learn its pattern with it. "
             "The shape never changes: yo, tú, él and ellos take the new vowel; nosotros and vosotros keep the old one.",
             tables=[table(["Pattern", "Verbs", "Example"],
                           [["o → ue", "poder, volver, dormir, almorzar, costar, contar, encontrar, soñar", "yo puedo, ellos vuelven"],
                            ["u → ue", "jugar", "yo juego"],
                            ["e → ie", "querer, pensar, cerrar, empezar, entender, perder, preferir", "yo quiero, tú piensas"],
                            ["e → i", "pedir, servir, repetir, vestir, elegir, decir", "yo pido, ellos sirven"]],
                           say=[2])]),
    ],
    exercises=[
        F("Yo ___ en casa los domingos.", "almuerzo", ["almorzo", "almuerza", "almorzamos"], "Almorzar: o → ue.", tr="I have lunch at home on Sundays.", lemma="almorzar:yo"),
        F("Tú ___ jugar al tenis conmigo.", "puedes", ["podes", "puede", "podéis"], "Poder: o → ue.", tr="You can play tennis with me.", lemma="poder:tú"),
        F("Mi madre ___ que hoy hace frío.", "piensa", ["pensa", "piensan", "pensamos"], "Pensar: e → ie.", tr="My mother thinks it is cold today.", lemma="pensar:ella"),
        F("Ellos ___ mucho dinero en ropa.", "gastan", ["gasta", "gasto", "gastamos"], "Gastar is regular: ellos gastan.", tr="They spend a lot of money on clothes.", lemma="gastar:ellos"),
        F("Nosotros ___ a casa temprano.", "volvemos", ["vuelven", "vuelvemos", "vuelvo"], "Nosotros keeps the o: volvemos.", tr="We return home early.", lemma="volver:nosotros"),
        F("¿Qué ___ ustedes, café o té?", "piden", ["pedan", "pide", "pedimos"], "Pedir: e → i.", tr="What do you (all) order, coffee or tea?", lemma="pedir:ustedes"),
        F("Yo ___ cuatro camisas.", "cuento", ["conto", "cuenta", "contamos"], "Contar: o → ue.", tr="I count four shirts.", lemma="contar:yo"),
        F("Marta ___ que su blusa es muy cara.", "dice", ["dize", "dicen", "decimos"], "Decir: e → i.", tr="Marta says that her blouse is very expensive.", lemma="decir:ella"),
        M("Which pattern does “pedir” follow?", "e → i", ["o → ue", "e → ie", "u → ue"], "Pido, pides, pide…"),
        M("Which pattern does “querer” follow?", "e → ie", ["o → ue", "e → i", "u → ue"], "Quiero, quieres, quiere…"),
        M("Which pattern does “costar” follow?", "o → ue", ["e → ie", "e → i", "u → ue"], "Cuesta, cuestan."),
    ],
)

# ---------------------------------------------------------------------------- 89
L89 = lesson(
    "Wanting and loving: querer, amar, encantar",
    "Quiero comprar. Quiero a mi familia. Me encanta.",
    requires=["querer", "amar", "encantar", "familia", "amigo"],
    cards=[
        card("Querer has two meanings",
             "Querer followed by an infinitive means “to want to”. Querer followed by a (the personal a) and a "
             "person means “to love, to care for”, in family and romantic love alike. Amar a is a deeper, "
             "more passionate love, often for a partner or for something very important.",
             tables=[table(["Verbo", "Sentence"],
                           [["querer + inf.", "Quiero comprar una chaqueta."],
                            ["querer a + person", "Quiero a mis amigos."],
                            ["amar a + person", "Amo a mi esposa."]],
                           say=[1])]),
        card("Me encanta",
             "Encantar says you love something in the sense of liking it a lot. It works like a fixed phrase: "
             "me encanta + one thing, me encantan + several things. You will meet the full pattern later, so for "
             "now use it just like this.",
             examples=[
                 ex("Me encanta esta ciudad.", "I love this city.", "Me encanta"),
                 ex("Me encantan estos zapatos.", "I love these shoes.", "Me encantan"),
                 ex("Me encanta bailar.", "I love dancing.", "Me encanta bailar."),
             ]),
    ],
    exercises=[
        F("Quiero ___ mis amigos.", "a", ["de", "en", "por"], "Querer + the personal a + person = to love.", tr="I love my friends."),
        F("Amo ___ mi esposa.", "a", ["de", "en", "con"], "Amar + the personal a.", tr="I love my wife."),
        F("Me ___ esta ciudad.", "encanta", ["encantan", "encanto", "encantas"], "One thing: encanta.", tr="I love this city."),
        F("Me ___ estos zapatos.", "encantan", ["encanta", "encanto", "encantar"], "Several things: encantan.", tr="I love these shoes."),
        F("Yo ___ comprar una chaqueta.", "quiero", ["quero", "quiere", "queremos"], "Yo quiero.", tr="I want to buy a jacket.", lemma="querer:yo"),
        F("Mis padres ___ a sus nietos.", "quieren", ["quiere", "queren", "queremos"], "Mis padres is they: quieren.", tr="My parents love their children’s children.", lemma="querer:ellos"),
        M("What does “Quiero a mi madre” mean?", "I love my mother.", ["I visit my mother.", "I look for my mother.", "I miss my mother."], "Querer a + person = to love."),
        M("What does “Quiero comprar un abrigo” mean?", "I want to buy a coat.", ["I love buying a coat.", "I love a coat.", "I buy a coat."], "Querer + infinitive = to want."),
        M("Which verb expresses the deepest, most passionate love?", "amar", ["querer", "encantar", "preferir"], "Amar a."),
        M("Can “encantar” be used for loving a person deeply?", "No, it only means liking someone or something a lot.", ["Yes, always.", "Only with children.", "Only with family."], "Encantar expresses strong liking, not deep love. To love a person, use querer a or amar a."),
    ],
)

# ---------------------------------------------------------------------------- 90
L90 = lesson(
    "To ask: pedir or preguntar",
    "Pido un café. Pregunto la hora.",
    requires=["pedir", "preguntar", "ayuda", "dinero", "pregunta"],
    cards=[
        card("Two verbs, two meanings",
             "English uses “ask” for both, but Spanish separates them. Pedir means to ask for something, to request "
             "or to order it. Preguntar means to ask a question. Pedir is a boot verb (pido); preguntar is regular.",
             tables=[table(["Verbo", "Meaning", "Example"],
                           [["pedir", "ask for, request, order", "Pido ayuda con mi tarea."],
                            ["preguntar", "ask a question", "Pregunto la hora."]],
                           say=[2])],
             examples=[
                 ex("Los niños piden regalos en Navidad.", "Children ask for presents at Christmas.", "piden regalos"),
                 ex("Los niños preguntan muchas cosas.", "Children ask many things.", "preguntan"),
                 ex("Yo pido una pizza en el restaurante.", "I order a pizza at the restaurant.", "pido una pizza"),
                 ex("Ella pregunta si hay una oferta.", "She asks whether there is a sale.", "pregunta si"),
             ]),
    ],
    exercises=[
        F("Mi hijo ___ dinero para comprar ropa.", "pide", ["pregunta", "pido", "preguntan"], "Asking for something: pedir.", tr="My son asks for money to buy clothes.", lemma="pedir:él"),
        F("Yo ___ la hora a un amigo.", "pregunto", ["pido", "preguntas", "pide"], "Asking a question: preguntar.", tr="I ask a friend the time.", lemma="preguntar:yo"),
        F("Los clientes ___ ayuda en la tienda.", "piden", ["preguntan", "pide", "pedimos"], "Asking for help: pedir.", tr="The customers ask for help in the store.", lemma="pedir:ellos"),
        F("La alumna ___ cuándo es el examen.", "pregunta", ["pide", "preguntan", "preguntas"], "Asking a question: preguntar.", tr="The student asks when the exam is.", lemma="preguntar:ella"),
        F("Nosotros ___ una pizza.", "pedimos", ["preguntamos", "pidimos", "pedamos"], "Ordering: pedir; nosotros keeps the e.", tr="We order a pizza.", lemma="pedir:nosotros"),
        M("Which verb do you use to order food?", "pedir", ["preguntar", "saber", "decir"], "Ordering is requesting."),
        M("You want to know where the store is. Which verb?", "preguntar", ["pedir", "servir", "repetir"], "Asking a question."),
        M("Which one is a boot verb?", "pedir", ["preguntar", "hablar", "comprar"], "Pido; preguntar is regular."),
        M("“Pedir un favor” means…", "to ask for a favor", ["to ask a question about a favor", "to do a favor", "to refuse a favor"], "Pedir = ask for."),
    ],
)

# ---------------------------------------------------------------------------- 91
L91 = lesson(
    "Two verbs together",
    "Quiero comprar. Necesito lavar y planchar.",
    requires=["querer", "necesitar", "poder", "deber", "preferir", "comprar"],
    cards=[
        card("Conjugate the first, infinitive the rest",
             "When a verb like querer, poder, deber, necesitar or tener que is followed by other verbs with the same subject, "
             "only that first verb is conjugated. All the verbs after it stay in the infinitive, however many there are.",
             tables=[table(["Primer verbo", "Meaning", "Example"],
                           [["querer", "want to", "Quiero comprar una chaqueta."],
                            ["poder", "can, be able to", "Puedes usar ropa cómoda."],
                            ["deber", "should, ought to", "Debes llegar temprano."],
                            ["necesitar", "need to", "Necesito lavar mi camisa."],
                            ["tener que", "have to", "Tenemos que pagar en efectivo."],
                            ["preferir", "prefer to", "Prefiero usar zapatos negros."],
                            ["pensar", "plan to, intend to", "Pienso viajar en verano."]],
                           say=[2])],
             examples=[
                 ex("Quiero estudiar, comer y dormir temprano.", "I want to study, eat and sleep early.", "estudiar, comer y dormir"),
                 ex("Necesito lavar y planchar mi camisa.", "I need to wash and iron my shirt.", "lavar y planchar"),
             ]),
    ],
    exercises=[
        F("Quiero ___ una chaqueta de cuero.", "comprar", ["compro", "compra", "compras"], "After querer, the second verb is an infinitive.", tr="I want to buy a leather jacket."),
        F("Puedes ___ ropa cómoda en el gimnasio.", "usar", ["usas", "usa", "uso"], "Poder + infinitive.", tr="You can wear comfortable clothes at the gym."),
        F("Necesito ___ y planchar mi camisa.", "lavar", ["lavo", "lava", "lavas"], "Both verbs stay in the infinitive.", tr="I need to wash and iron my shirt."),
        F("Nosotros ___ pagar en efectivo.", "tenemos que", ["tiene que", "tienen que", "tenemos"], "Nosotros takes tenemos que.", tr="We have to pay in cash."),
        F("Ellos ___ ver otra tienda.", "quieren", ["queremos", "quiere", "queren"], "Ellos quieren.", tr="They want to see another store.", lemma="querer:ellos"),
        F("¿Tú ___ llegar temprano?", "puedes", ["puede", "podes", "pueden"], "Tú puedes.", tr="Can you arrive early?", lemma="poder:tú"),
        M("Which sentence is correct?", "Prefiero usar zapatos negros.", ["Prefiero uso zapatos negros.", "Prefiero usando zapatos negros.", "Prefiero que usar zapatos negros."], "Second verb in the infinitive."),
        M("Which sentence is correct?", "Debes llegar temprano.", ["Debes llegas temprano.", "Debes llegaste temprano.", "Debes llegando temprano."], "Deber + infinitive."),
        M("In “Quiero estudiar, comer y dormir temprano”, which verb is conjugated?", "quiero", ["estudiar", "comer", "dormir"], "Only the first one."),
        M("Which means “I plan to travel”?", "Pienso viajar.", ["Pienso viajo.", "Pienso de viajar.", "Pienso viajamos."], "Pensar + infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 92
L92 = lesson(
    "Feelings with tener",
    "tengo frío, tengo hambre, tengo prisa",
    requires=["tener", "frío", "calor", "hambre", "sed", "sueño", "miedo", "razón", "suerte"],
    cards=[
        card("Feelings: Spanish has, English is",
             "Many physical conditions and feelings use tener plus a noun, where English uses “to be” plus an adjective. "
             "You say tengo frío (literally “I have cold”), not estoy frío. Because the feeling is a noun, you describe how much with "
             "mucho or mucha, never with muy.",
             tables=[table(["Expresión", "English"],
                           [["tener frío", "to be cold"],
                            ["tener calor", "to be hot"],
                            ["tener hambre", "to be hungry"],
                            ["tener sed", "to be thirsty"],
                            ["tener sueño", "to be sleepy"],
                            ["tener miedo (de)", "to be afraid (of)"],
                            ["tener prisa", "to be in a hurry"],
                            ["tener razón", "to be right"],
                            ["tener suerte", "to be lucky"],
                            ["tener ganas de + inf.", "to feel like (doing)"]],
                           say=[0])],
             examples=[
                 ex("Tengo mucho frío.", "I am very cold.", "Tengo mucho frío."),
                 ex("Tienes mucha razón.", "You are very right.", "mucha razón"),
                 ex("Mis hijos tienen hambre.", "My children are hungry.", "tienen hambre"),
                 ex("Tengo ganas de comprar ropa nueva.", "I feel like buying new clothes.", "Tengo ganas de comprar"),
             ]),
    ],
    exercises=[
        F("Yo ___ frío.", "tengo", ["soy", "estoy", "hago"], "Cold uses tener.", tr="I am cold.", lemma="tener:yo"),
        F("Mis hijos ___ hambre.", "tienen", ["tiene", "tengo", "son"], "Mis hijos is they: tienen.", tr="My children are hungry.", lemma="tener:ellos"),
        F("Tengo ___ frío.", "mucho", ["muy", "mucha", "muchos"], "Frío is a masculine noun: mucho.", tr="I am very cold."),
        F("Tienes ___ razón.", "mucha", ["muy", "mucho", "muchas"], "Razón is feminine: mucha.", tr="You are very right."),
        F("Ella tiene ganas ___ comprar ropa nueva.", "de", ["en", "a", "por"], "Tener ganas de + infinitive.", tr="She feels like buying new clothes."),
        F("Nosotros ___ sueño después de correr.", "tenemos", ["somos", "estamos", "tienen"], "Sleepy uses tener.", tr="We are sleepy after running.", lemma="tener:nosotros"),
        F("Tú ___ mucha suerte.", "tienes", ["tiene", "tengo", "eres"], "Lucky uses tener.", tr="You are very lucky.", lemma="tener:tú"),
        M("How do you say “I am thirsty”?", "Tengo sed.", ["Soy sed.", "Estoy sed.", "Hago sed."], "Tener sed."),
        M("How do you say “I am in a hurry”?", "Tengo prisa.", ["Estoy prisa.", "Soy prisa.", "Voy prisa."], "Tener prisa."),
        M("How do you say “They are afraid of the dog”?", "Tienen miedo del perro.", ["Son miedo del perro.", "Tienen miedo al perro de.", "Están miedo del perro."], "Tener miedo de + noun."),
    ],
)

# ---------------------------------------------------------------------------- 93
L93 = lesson(
    "Por and para, part 1",
    "pago veinte dólares por la camisa, es para mi madre",
    requires=["por", "para", "pagar", "comprar", "regalo"],
    cards=[
        card("Two ways to say “for”",
             "Por and para both translate as “for”, but they have different jobs. Start with four.",
             tables=[table(["Word", "Use", "Example"],
                           [["por", "in exchange for", "Pago veinte dólares por la blusa."],
                            ["para", "for someone", "Compro una blusa para mi madre."],
                            ["por", "by means of", "Hablo con mi madre por teléfono."],
                            ["para", "in order to (purpose)", "Necesito dinero para comprar zapatos."]],
                           say=[0, 2])]),
        card("Quick test",
             "Ask what the “for” really means. If it means “in exchange for” or “by means of”, use por. If it "
             "means “intended for” a person or “in order to” do something, use para. To say you travel in a vehicle, use en, not por: voy en autobús.",
             examples=[
                 ex("Pago cuarenta pesos por la camisa.", "I pay forty pesos for the shirt.", "por la camisa"),
                 ex("Hablo con mi madre por teléfono.", "I talk with my mother by phone.", "por teléfono"),
                 ex("Esta camisa es para mi hermano.", "This shirt is for my brother.", "para mi hermano"),
                 ex("Esta maleta es para el viaje.", "This suitcase is for the trip.", "para el viaje"),
                 ex("Para pagar, voy a la caja.", "In order to pay, I go to the register.", "Para pagar"),
             ]),
    ],
    exercises=[
        F("Pago veinte dólares ___ la camisa.", "por", ["para", "de", "en"], "Exchange: por.", tr="I pay twenty dollars for the shirt."),
        F("Compro una blusa ___ mi madre.", "para", ["por", "de", "en"], "For a person: para.", tr="I buy a blouse for my mother."),
        F("Hablo con mi madre ___ teléfono.", "por", ["para", "de", "a"], "By means of the phone: por.", tr="I talk with my mother by phone."),
        F("Necesito dinero ___ comprar zapatos.", "para", ["por", "de", "con"], "In order to + infinitive: para.", tr="I need money in order to buy shoes."),
        F("Este regalo es ___ ti.", "para", ["por", "en", "de"], "Intended for you: para.", tr="This gift is for you."),
        F("Pagamos cien dólares ___ el abrigo.", "por", ["para", "a", "con"], "Exchange: por.", tr="We pay one hundred dollars for the coat."),
        M("In “Esta maleta es para el viaje”, para shows…", "purpose", ["exchange", "transport", "time"], "For the trip."),
        M("In “Envío la carta por avión”, por shows…", "means of sending", ["a recipient", "purpose", "exchange"], "By airmail."),
        M("Which is correct?", "Compro un regalo para mi padre.", ["Compro un regalo a por mi padre.", "Compro un regalo de mi padre.", "Compro un regalo en mi padre."], "Recipient: para."),
        M("Which is correct?", "Para pagar, voy a la caja.", ["Por pagar, voy a la caja.", "De pagar, voy a la caja.", "En pagar, voy a la caja."], "In order to: para + infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 94
L94 = lesson(
    "Adverbs ending in -mente",
    "rápidamente, frecuentemente, fácilmente",
    requires=["rápido", "fácil", "claro", "lento", "frecuente", "final"],
    cards=[
        card("From adjective to adverb",
             "Many adverbs end in -mente, which works like the English ending that makes adverbs. If the adjective ends in -o, use the feminine "
             "form (-a) and add -mente. If it ends in -e or a consonant, just add -mente. A written accent in the "
             "adjective stays in the adverb.",
             tables=[table(["Adjetivo", "Adverbio"],
                           [["rápido", "rápidamente"],
                            ["lento", "lentamente"],
                            ["claro", "claramente"],
                            ["completo", "completamente"],
                            ["tranquilo", "tranquilamente"],
                            ["frecuente", "frecuentemente"],
                            ["final", "finalmente"],
                            ["normal", "normalmente"],
                            ["fácil", "fácilmente"]],
                           say=[0, 1])],
             examples=[
                 ex("Ella camina lentamente por la calle.", "She walks slowly along the street.", "lentamente"),
                 ex("Normalmente llego a las ocho.", "I normally arrive at eight.", "Normalmente"),
                 ex("Finalmente compro la chaqueta.", "Finally I buy the jacket.", "Finalmente"),
             ]),
    ],
    exercises=[
        M("What is the adverb of “rápido”?", "rápidamente", ["rápidomente", "rápido-mente", "rápidamento"], "Use the feminine form and add -mente."),
        M("What is the adverb of “fácil”?", "fácilmente", ["facilmente", "fácilamente", "fácil-mente"], "Keep the written accent."),
        M("What is the adverb of “frecuente”?", "frecuentemente", ["frecuentamente", "frecuente-mente", "frecuentomente"], "Adjectives in -e add -mente."),
        M("What is the adverb of “completo”?", "completamente", ["completomente", "completemente", "completo-mente"], "-o becomes -a, then -mente."),
        F("Ella camina ___ por la calle.", "lentamente", ["lentas", "lentos", "lentitud"], "An adverb is needed to modify camina.", tr="She walks slowly along the street."),
        F("___ llego a las ocho.", "Normalmente", ["Normal", "Normales", "Normala"], "An adverb is needed.", tr="I normally arrive at eight."),
        F("Los niños aprenden ___.", "rápidamente", ["rápido mente", "rápidos", "rápida"], "Adverb: rápidamente.", tr="The children learn quickly."),
        F("___ compro la chaqueta.", "Finalmente", ["Final", "Finales", "Finala"], "Adverb: finalmente.", tr="Finally I buy the jacket."),
        M("Which ending turns an adjective into an adverb?", "-mente", ["-ando", "-ción", "-oso"], "-mente forms adverbs."),
        M("Which is an adverb?", "tranquilamente", ["tranquilo", "tranquila", "tranquilos"], "It ends in -mente."),
    ],
)

# ---------------------------------------------------------------------------- 95
L95 = lesson(
    "What to wear when",
    "Para una boda, debes llevar un traje.",
    requires=["boda", "entrevista", "fiesta", "formal", "cómodo", "ropa", "llevar"],
    cards=[
        card("Occasions and clothing",
             "Match the clothing to the event. Use para plus the occasion, then deber, poder or necesitar plus an "
             "infinitive. Formal clothing is ropa formal; casual clothing is ropa informal or ropa cómoda; sports "
             "clothing is ropa deportiva.",
             tables=[table(["Ocasión", "Qué llevar"],
                           [["una boda", "traje o vestido elegante"],
                            ["una entrevista de trabajo", "ropa formal"],
                            ["una fiesta con amigos", "ropa informal"],
                            ["el gimnasio", "ropa deportiva"],
                            ["la playa", "traje de baño y sandalias"],
                            ["un día de frío", "abrigo, bufanda y guantes"]],
                           say=[0, 1])],
             examples=[
                 ex("Para una boda, debes llevar un traje.", "For a wedding, you should wear a suit.", "debes llevar"),
                 ex("Para ir al gimnasio, necesito ropa deportiva.", "To go to the gym, I need sports clothes.", "ropa deportiva"),
                 ex("En la playa puedes llevar sandalias.", "At the beach you can wear sandals.", "puedes llevar"),
                 ex("Prefiero ropa cómoda para viajar.", "I prefer comfortable clothes for traveling.", "ropa cómoda"),
             ]),
    ],
    exercises=[
        F("Para una entrevista de trabajo, debo llevar ropa ___.", "formal", ["deportiva", "de baño", "de playa"], "A job interview calls for formal clothes.", tr="For a job interview, I should wear formal clothes."),
        F("Para ir al gimnasio, necesito ropa ___.", "deportiva", ["formal", "elegante", "de seda"], "Gym: sports clothes.", tr="To go to the gym, I need sports clothes."),
        F("En la playa puedes ___ sandalias.", "llevar", ["llevas", "lleva", "llevo"], "Poder + infinitive.", tr="At the beach you can wear sandals."),
        F("Para viajar, prefiero ropa ___.", "cómoda", ["cómodo", "cómodas", "elegantes"], "Ropa is feminine singular: cómoda.", tr="For traveling, I prefer comfortable clothes."),
        F("Para ___ boda, debes llevar un traje.", "una", ["un", "el", "los"], "Boda is feminine: una.", tr="For a wedding, you should wear a suit."),
        F("Mi hermano ___ llevar corbata a la entrevista.", "debe", ["deben", "debo", "debes"], "Mi hermano is he: debe.", tr="My brother should wear a tie to the interview.", lemma="deber:él"),
        M("Where do you wear a swimsuit and sandals?", "en la playa", ["en una entrevista", "en una boda", "en la oficina"], "Beach clothes."),
        M("What do you wear on a very cold day?", "abrigo, bufanda y guantes", ["traje de baño", "sandalias", "ropa deportiva"], "Warm clothes."),
        M("Which is the most formal?", "un traje elegante", ["una camiseta", "unas sandalias", "una gorra"], "A suit is formal."),
        M("How do you say “comfortable clothes”?", "ropa cómoda", ["ropa cómodo", "ropa cómodas", "ropa comodas"], "Ropa is feminine singular."),
    ],
)

# ---------------------------------------------------------------------------- 96
L96 = lesson(
    "Traditional clothing",
    "el poncho, la guayabera, el huipil",
    requires=["país", "ropa", "mujer", "hombre", "usar", "llevar"],
    cards=[
        card("Clothes with a story",
             "Many Spanish-speaking regions have traditional garments that people still wear, some every day and others on special occasions. Here are "
             "a few. Tap each sentence to hear it.",
             examples=[
                 ex("En los Andes, muchas personas llevan ponchos de lana.", "In the Andes, many people wear wool ponchos.", "ponchos de lana"),
                 ex("La guayabera es una camisa ligera que muchos hombres usan en el Caribe.", "The guayabera is a light shirt that many men wear in the Caribbean.", "La guayabera"),
                 ex("En México, los charros usan un traje elegante y un sombrero grande.", "In Mexico, charros wear an elegant suit and a big hat.", "los charros"),
                 ex("En México y Guatemala, algunas mujeres llevan huipiles de colores.", "In Mexico and Guatemala, some women wear colorful huipiles.", "huipiles"),
                 ex("En España, algunas mujeres llevan una mantilla en ocasiones especiales.", "In Spain, some women wear a mantilla on special occasions.", "una mantilla"),
             ]),
    ],
    exercises=[
        M("Where do many people wear ponchos of wool?", "in the Andes", ["in the Caribbean", "in Spain", "in Guatemala only"], "En los Andes."),
        M("Which garment is a light shirt worn in the Caribbean?", "la guayabera", ["el poncho", "el huipil", "la mantilla"], "Guayabera."),
        M("Who wears a big hat and an elegant suit in Mexico?", "los charros", ["los gauchos", "los toreros", "los marineros"], "Los charros."),
        M("Where do some women wear huipiles?", "in Mexico and Guatemala", ["in Argentina", "in Spain", "in Cuba"], "México y Guatemala."),
        M("What is a mantilla?", "a veil or scarf worn on special occasions", ["a heavy coat", "a type of shoe", "a pair of gloves"], "Spanish tradition."),
        F("Muchos hombres ___ guayaberas en el Caribe.", "usan", ["usa", "uso", "usamos"], "Muchos hombres is they: usan.", tr="Many men wear guayaberas in the Caribbean.", lemma="usar:ellos"),
        F("En los Andes, muchas personas llevan ___ de lana.", "ponchos", ["ponchas", "huipil", "mantilla"], "In the Andes the typical wool garment is the poncho.", tr="In the Andes, many people wear wool ponchos."),
        F("La guayabera es una camisa ___.", "ligera", ["ligero", "ligeros", "ligeras"], "Camisa is feminine singular.", tr="The guayabera is a light shirt."),
        M("Which sentence is correct?", "Los charros usan un sombrero grande.", ["Los charros usa un sombrero grande.", "Los charros usan un sombrero grandes.", "Los charros usamos un sombrero grande."], "Plural subject, singular object."),
    ],
)

# ---------------------------------------------------------------------------- 97
L97 = lesson(
    "Chapter 6 review",
    "clothes, boot verbs, tener expressions, por and para",
    requires=["ropa", "querer", "poder", "pedir", "tener", "por"],
    cards=[
        card("What you can do now",
             "You can name clothes and fabrics, shop, use boot verbs, chain two verbs, describe feelings with tener, "
             "choose between por and para for four common meanings, and make adverbs with -mente.",
             tables=[table(["Skill", "Model sentence"],
                           [["Clothes", "Llevo una camisa de algodón."],
                            ["Boot verbs", "Quiero comprar una chaqueta y puedo pagar en efectivo."],
                            ["Pedir/preguntar", "Pido un café y pregunto la hora."],
                            ["Tener", "Tengo mucho frío y tengo prisa."],
                            ["Por/para", "Pago veinte dólares por la camisa para mi hijo."]],
                           say=[1])]),
    ],
    exercises=[
        F("Mi chaqueta es de ___.", "cuero", ["cuadros", "rayas", "lisa"], "Material: de cuero.", tr="My jacket is leather."),
        F("¿Cuánto ___ estos zapatos?", "cuestan", ["cuesta", "costan", "costamos"], "Zapatos is plural: cuestan.", tr="How much do these shoes cost?", lemma="costar:ellos"),
        F("Yo ___ comprar una camisa nueva.", "quiero", ["quere", "quiere", "queremos"], "Yo quiero.", tr="I want to buy a new shirt.", lemma="querer:yo"),
        F("La tienda ___ a las ocho de la noche.", "cierra", ["cerra", "cierran", "cerramos"], "La tienda: cierra.", tr="The store closes at eight at night.", lemma="cerrar:ella"),
        F("Los niños ___ regalos en Navidad.", "piden", ["preguntan", "pide", "pedimos"], "Ask for: pedir.", tr="Children ask for presents at Christmas.", lemma="pedir:ellos"),
        F("Nosotros ___ frío en invierno.", "tenemos", ["somos", "estamos", "tienen"], "Cold uses tener.", tr="We are cold in winter.", lemma="tener:nosotros"),
        F("Compro una blusa ___ mi madre.", "para", ["por", "de", "en"], "For a person: para.", tr="I buy a blouse for my mother."),
        F("Pago veinte dólares ___ la camisa.", "por", ["para", "de", "con"], "Exchange: por.", tr="I pay twenty dollars for the shirt."),
        F("Ella camina ___ por la calle.", "lentamente", ["lentas", "lentos", "lentitud"], "An adverb is needed.", tr="She walks slowly along the street."),
        M("Which sentence is correct?", "Necesito lavar y planchar mi camisa.", ["Necesito lavo y plancho mi camisa.", "Necesito lavando y planchando mi camisa.", "Necesito lavar y plancho mi camisa."], "Only the first verb is conjugated; the others stay in the infinitive."),
        M("What does “Quiero a mi madre” mean?", "I love my mother.", ["I visit my mother.", "I ask for my mother.", "I order my mother."], "Querer a + person."),
        M("Which means “I am in a hurry”?", "Tengo prisa.", ["Soy prisa.", "Estoy prisa.", "Hago prisa."], "Tener prisa."),
    ],
)

UNIT = unit("La ropa", [L82, L83, L84, L85, L86, L87, L88, L89, L90, L91, L92, L93, L94, L95, L96, L97])

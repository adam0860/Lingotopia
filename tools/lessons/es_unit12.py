"""Unit 12: food and health, the preterite, direct objects (textbook Chapter 11)."""
from dsl_es import *

# ---------------------------------------------------------------------------- 155
L155 = lesson(
    "Meals of the day",
    "el desayuno, el almuerzo, la merienda, la cena",
    requires=["desayuno", "almuerzo", "cena", "comida", "comer", "beber"],
    cards=[
        card("Las comidas del día",
             "Most Spanish speakers eat four times a day. The big meal is often lunch, eaten in the early afternoon. "
             "The merienda is a light snack in the late afternoon, and dinner comes late and is usually lighter. "
             "The word la comida can mean “food”, “a meal” or, in some countries, “lunch”.",
             tables=[table(["Comida", "English", "Cuándo"],
                           [["el desayuno", "breakfast", "por la mañana"],
                            ["el almuerzo", "lunch", "a mediodía"],
                            ["la merienda", "afternoon snack", "por la tarde"],
                            ["la cena", "dinner", "por la noche"]],
                           say=[0, 2])]),
        card("Verbs for meals",
             "Each meal has its own verb: desayunar, almorzar (o → ue: almuerzo), merendar (e → ie: meriendo) and cenar. "
             "You can also say simply comer, “to eat”.",
             examples=[
                 ex("Desayuno café con pan a las siete.", "I have coffee and bread for breakfast at seven.", "Desayuno"),
                 ex("Mi familia almuerza a las dos.", "My family has lunch at two.", "almuerza"),
                 ex("Los domingos cenamos tarde.", "On Sundays we have dinner late.", "cenamos"),
                 ex("¿Qué comes en la merienda?", "What do you eat at snack time?", "merienda"),
                 ex("Después de comer, nos quedamos un rato en la mesa.", "After eating, we stay at the table for a while.", "nos quedamos"),
             ]),
    ],
    exercises=[
        F("Por la mañana yo ___ café con pan.", "desayuno", ["ceno", "almuerzo", "cenamos"], "Yo + desayunar: desayuno.",
          tr="In the morning I have coffee and bread for breakfast.", lemma="desayunar:yo"),
        F("Mis padres ___ a las dos de la tarde.", "almuerzan", ["almorzamos", "almuerzas", "almuerzo"], "Ellos: almuerzan (o → ue).",
          tr="My parents have lunch at two in the afternoon.", lemma="almorzar:ellos"),
        F("Nosotros ___ tarde, a las nueve de la noche.", "cenamos", ["ceno", "cenan", "cenas"], "Nosotros: cenamos.",
          tr="We have dinner late, at nine at night.", lemma="cenar:nosotros"),
        F("Tú ___ a las doce y media.", "almuerzas", ["almorzamos", "almuerza", "almuerzan"], "Tú: almuerzas.",
          tr="You have lunch at twelve thirty.", lemma="almorzar:tú"),
        M("Which meal is the afternoon snack?", "la merienda", ["el desayuno", "la cena", "el almuerzo"], "Merienda = afternoon snack."),
        M("What does “el almuerzo” mean?", "lunch", ["breakfast", "dinner", "snack"], "Almuerzo = lunch."),
        M("Which meal is eaten first in the day?", "el desayuno", ["la cena", "la merienda", "el almuerzo"], "Desayuno = breakfast."),
        M("Which sentence means “We have dinner at nine”?", "Cenamos a las nueve.", ["Almorzamos a las nueve.", "Ceno a las nueve.", "Cenan a las nueve."], "Cenar + nosotros: cenamos."),
        M("What is the infinitive of “almuerzo”?", "almorzar", ["almuerzar", "almorcer", "almuerzer"], "Almorzar changes o → ue in the present."),
    ],
    verify=vp("cenar", "ceno", "cenas", "cena", "cenamos", "cenáis", "cenan"),
)

# ---------------------------------------------------------------------------- 156
L156 = lesson(
    "Meat, fish and eggs",
    "el pollo, el pescado, la chuleta de cerdo, los camarones",
    requires=["carne", "pollo", "pescado", "cerdo", "huevo", "cocinar"],
    cards=[
        card("La carne y el pescado",
             "Meat is la carne. Beef is la carne de res (or de vaca), pork is la carne de cerdo and veal is la ternera. "
             "Seafood is los mariscos, and a single shrimp is un camarón.",
             tables=[table(["Alimento", "English"],
                           [["el pollo", "chicken"],
                            ["el bistec", "steak"],
                            ["la chuleta de cerdo", "pork chop"],
                            ["el jamón", "ham"],
                            ["la salchicha", "sausage"],
                            ["el pescado", "fish"],
                            ["el atún", "tuna"],
                            ["los camarones", "shrimp"],
                            ["los huevos", "eggs"]],
                           say=[0])]),
        card("What do you eat?",
             "Use comer for what you eat and preferir to say what you like better. Remember: the verb agrees with "
             "the person, and the food after it can be singular or plural.",
             examples=[
                 ex("Mi madre cocina pollo con arroz.", "My mother cooks chicken with rice.", "pollo"),
                 ex("Prefiero el pescado a la carne.", "I prefer fish to meat.", "el pescado"),
                 ex("Los camarones son muy caros hoy.", "Shrimp are very expensive today.", "Los camarones"),
                 ex("En el desayuno como dos huevos y jamón.", "At breakfast I eat two eggs and ham.", "dos huevos"),
                 ex("Mis primos no comen cerdo.", "My cousins do not eat pork.", "cerdo"),
             ]),
    ],
    exercises=[
        F("Mi madre cocina ___ con arroz.", "pollo", ["jamón", "helado", "café"], "Chicken with rice is a classic dish.", tr="My mother cooks chicken with rice."),
        F("En el desayuno como dos ___ fritos.", "huevos", ["pollos", "bistecs", "pescados"], "Fried eggs: huevos fritos.", tr="At breakfast I eat two fried eggs."),
        F("Los camarones son un tipo de ___.", "marisco", ["verdura", "postre", "bebida"], "Shrimp are seafood.", tr="Shrimp are a kind of seafood."),
        F("Mi tío prepara chuletas de ___.", "cerdo", ["agua", "arroz", "queso"], "Chuleta de cerdo = pork chop.", tr="My uncle prepares pork chops."),
        M("What does “la carne de res” mean?", "beef", ["pork", "chicken", "ham"], "Res = cattle."),
        M("Which word means “fish”?", "el pescado", ["el pollo", "el cerdo", "el huevo"], "Pescado = fish (as food)."),
        M("Which food is NOT meat or fish?", "los huevos", ["el bistec", "el atún", "la salchicha"], "Eggs are their own group."),
        M("How do you say “I prefer fish to meat”?", "Prefiero el pescado a la carne.", ["Prefiero la carne al pescado.", "Prefiero el pescado de la carne.", "Prefieren el pescado a la carne."], "Preferir X a Y."),
        M("What does “la salchicha” mean?", "sausage", ["steak", "salad", "shrimp"], "Salchicha = sausage."),
    ],
)

# ---------------------------------------------------------------------------- 157
L157 = lesson(
    "Vegetables, fruit and basic foods",
    "la lechuga, la zanahoria, la manzana, el arroz",
    requires=["verdura", "fruta", "naranja", "arroz", "pan", "queso"],
    cards=[
        card("Las verduras y las frutas",
             "Vegetables are las verduras and fruit is la fruta. Some words change from country to country: "
             "la papa (Latin America) is la patata in Spain, and los frijoles are also called los porotos or las judías.",
             tables=[table(["Alimento", "English"],
                           [["la lechuga", "lettuce"],
                            ["el tomate", "tomato"],
                            ["la zanahoria", "carrot"],
                            ["la cebolla", "onion"],
                            ["la papa · la patata", "potato"],
                            ["el maíz", "corn"],
                            ["la manzana", "apple"],
                            ["la naranja", "orange"],
                            ["las uvas", "grapes"],
                            ["la fresa", "strawberry"]],
                           say=[0])]),
        card("Basic foods",
             "Rice, bread, cheese, butter and beans are on many tables every day. A salad is una ensalada and soup is la sopa.",
             tables=[table(["Alimento", "English"],
                           [["el arroz", "rice"],
                            ["el pan", "bread"],
                            ["el queso", "cheese"],
                            ["la mantequilla", "butter"],
                            ["los frijoles", "beans"],
                            ["la ensalada", "salad"],
                            ["la sopa", "soup"]],
                           say=[0])]),
        card("In a sentence",
             "Foods are usually used with the article when you talk about them in general: me gusta el arroz, "
             "but with no article after comer when you mean “some”.",
             examples=[
                 ex("En mi casa comemos mucho arroz.", "At my house we eat a lot of rice.", "arroz"),
                 ex("Compro lechuga y tomates para la ensalada.", "I buy lettuce and tomatoes for the salad.", "lechuga y tomates"),
                 ex("La sopa lleva zanahoria, cebolla y papa.", "The soup has carrot, onion and potato in it.", "lleva"),
                 ex("Mi hermana come una manzana todos los días.", "My sister eats an apple every day.", "una manzana"),
             ]),
    ],
    exercises=[
        F("Para la ensalada compro ___ y tomates.", "lechuga", ["arroz", "pollo", "helado"], "Lettuce goes in a salad.", tr="For the salad I buy lettuce and tomatoes."),
        F("La sopa lleva zanahoria, cebolla y ___.", "papa", ["jamón", "azúcar", "vino"], "Papa = potato.", tr="The soup has carrot, onion and potato in it."),
        F("Mi hermana come una ___ todos los días.", "manzana", ["cebolla", "sopa", "carne"], "An apple a day.", tr="My sister eats an apple every day."),
        F("Una manzana es una ___.", "fruta", ["verdura", "bebida", "carne"], "An apple is a fruit.", tr="An apple is a fruit."),
        M("What does “la zanahoria” mean?", "carrot", ["onion", "tomato", "corn"], "Zanahoria = carrot."),
        M("Which word is Spain’s word for “potato”?", "la patata", ["la papa", "el maíz", "la cebolla"], "Patata in Spain, papa in Latin America."),
        M("Which one is a fruit?", "la fresa", ["la cebolla", "la lechuga", "el maíz"], "Fresa = strawberry."),
        M("Which food comes from milk?", "el queso", ["el arroz", "el pan", "la lechuga"], "Queso = cheese."),
        M("What does “las uvas” mean?", "grapes", ["onions", "peas", "plums"], "Uva = grape."),
    ],
)

# ---------------------------------------------------------------------------- 158
L158 = lesson(
    "Drinks and desserts",
    "un vaso de leche, una taza de té, el helado, el pastel",
    requires=["agua", "jugo", "leche", "café", "té", "helado", "dulce"],
    cards=[
        card("Las bebidas",
             "To order a drink, you often use a container word: un vaso de (a glass of), una taza de (a cup of) "
             "or una copa de (a wine glass of). Wine is for adults, el vino blanco or el vino tinto.",
             tables=[table(["Bebida", "English"],
                           [["el agua", "water"],
                            ["el jugo", "juice"],
                            ["la leche", "milk"],
                            ["el café", "coffee"],
                            ["el té", "tea"],
                            ["la limonada", "lemonade"],
                            ["el refresco · la gaseosa", "soft drink"],
                            ["la cerveza", "beer"]],
                           say=[0])]),
        card("Los postres",
             "Dessert is el postre. Cake has several names: el pastel, la tarta or el queque, depending on "
             "the country. Careful: in Mexico, la torta is a sandwich. In Spanish, el azúcar is “sugar”.",
             tables=[table(["Postre", "English"],
                           [["el helado", "ice cream"],
                            ["el flan", "caramel custard"],
                            ["el pastel · la tarta", "cake"],
                            ["la galleta", "cookie"],
                            ["el chocolate", "chocolate"],
                            ["el arroz con leche", "rice pudding"],
                            ["los dulces", "sweets, candy"]],
                           say=[0])]),
        card("Ordering",
             "Notice the container words with de.",
             examples=[
                 ex("Quiero un vaso de agua, por favor.", "I want a glass of water, please.", "un vaso de agua"),
                 ex("Mi abuela toma una taza de té por la tarde.", "My grandmother has a cup of tea in the afternoon.", "una taza de té"),
                 ex("De postre, los niños piden helado de chocolate.", "For dessert, the children ask for chocolate ice cream.", "De postre"),
                 ex("Mis tíos beben una copa de vino con la cena.", "My aunt and uncle drink a glass of wine with dinner.", "una copa de vino"),
             ]),
    ],
    exercises=[
        F("Quiero un ___ de agua, por favor.", "vaso", ["plato", "tenedor", "pan"], "A glass of water: un vaso de agua.", tr="I want a glass of water, please."),
        F("Mi abuela toma una ___ de té por la tarde.", "taza", ["copa", "vaso", "cena"], "A cup of tea: una taza de té.", tr="My grandmother has a cup of tea in the afternoon."),
        F("De ___ pido un helado de chocolate.", "postre", ["cena", "comida", "bebida"], "For dessert: de postre.", tr="For dessert I order a chocolate ice cream."),
        F("Los niños beben un vaso de ___ en el desayuno.", "leche", ["vino", "cerveza", "aceite"], "Milk for children at breakfast.", tr="The children drink a glass of milk at breakfast."),
        M("What does “el pastel” mean?", "cake", ["tortilla", "salad", "soup"], "Pastel/tarta = cake. (In Mexico, torta is a sandwich.)"),
        M("Which is a hot drink?", "el café", ["el helado", "la limonada", "el jugo"], "Coffee is hot."),
        M("Which word means “sugar”?", "el azúcar", ["la sal", "el aceite", "la leche"], "Azúcar = sugar."),
        M("Which sentence means “I want a cup of coffee”?", "Quiero una taza de café.", ["Quieres una taza de café.", "Quieren una taza de café.", "Quiero un taza de café."], "Coffee comes in a cup (una taza)."),
        M("What does “la gaseosa” mean?", "soft drink", ["milk", "water", "juice"], "Gaseosa/refresco = soft drink."),
    ],
)

# ---------------------------------------------------------------------------- 159
L159 = lesson(
    "Describing food: ser or estar?",
    "El chile es picante. La sopa está fría.",
    requires=["ser", "estar", "caliente", "frío", "dulce", "rico", "delicioso"],
    cards=[
        card("Words that describe food",
             "Adjectives agree with the food they describe: la sopa fría, el café caliente, las papas fritas.",
             tables=[table(["Adjetivo", "English"],
                           [["dulce", "sweet"],
                            ["salado, salada", "salty"],
                            ["picante", "spicy"],
                            ["amargo, amarga", "bitter"],
                            ["caliente", "hot (temperature)"],
                            ["frío, fría", "cold"],
                            ["delicioso, deliciosa", "delicious"],
                            ["rico, rica", "tasty"],
                            ["saludable", "healthy"]],
                           say=[0])]),
        card("Ser for what it is, estar for how it is now",
             "Use ser for what a food is like in general (its nature), and estar for how it is at this moment "
             "(temperature, taste today). With some adjectives both are possible, with a small difference.",
             tables=[table(["Ser (what it is like)", "Estar (how it is now)"],
                           [["El azúcar es dulce.", "La sopa está fría."],
                            ["El chile es picante.", "El café está caliente."],
                            ["El café es amargo.", "La cena está deliciosa."],
                            ["La fruta es saludable.", "Este pescado está salado."]],
                           say=[0, 1])]),
        card("Es rico, está rico",
             "With ser, rico describes a general quality: a person who is rico is wealthy, and a dish that is rico is tasty by nature. With estar it says how it tastes now. "
             "To compliment the cook, say Está muy rico or Está delicioso.",
             examples=[
                 ex("Este pollo está muy rico.", "This chicken is very tasty.", "está"),
                 ex("La sopa está fría, ¿puede calentarla?", "The soup is cold, can you heat it?", "está fría"),
                 ex("El helado es dulce.", "Ice cream is sweet.", "es dulce"),
                 ex("La comida de mi abuela siempre está deliciosa.", "My grandmother’s food is always delicious.", "está deliciosa"),
             ]),
    ],
    exercises=[
        F("El azúcar siempre ___ dulce.", "es", ["está", "son", "están"], "A permanent quality: ser.", tr="Sugar is sweet.", lemma="ser:ella"),
        F("Hoy la sopa ___ fría.", "está", ["es", "son", "están"], "A temporary state: estar.", tr="Today the soup is cold.", lemma="estar:ella"),
        F("Hoy las papas fritas ___ saladas.", "están", ["es", "son", "está"], "Plural + estar: están.", tr="The french fries are salty.", lemma="estar:ellos"),
        F("El chile siempre ___ picante.", "es", ["está", "son", "están"], "A characteristic of chili: ser.", tr="Chili is spicy.", lemma="ser:ella"),
        F("Esta noche la ensalada ___ deliciosa.", "está", ["es", "son", "están"], "How it tastes tonight: estar.", tr="The salad is delicious tonight.", lemma="estar:ella"),
        M("Which adjective means “bitter”?", "amargo", ["dulce", "salado", "picante"], "Amargo = bitter."),
        M("Which sentence is about the temperature of the coffee now?", "El café está caliente.", ["El café es amargo.", "El café es negro.", "El café es de Colombia."], "Estar for a state now."),
        M("How do you say “The fruit is healthy” (in general)?", "La fruta es saludable.", ["La fruta son saludable.", "La fruta es saludables.", "La fruta eres saludable."], "A general fact: ser, agreement singular."),
        M("Which adjective has separate masculine and feminine forms?", "frío", ["dulce", "picante", "caliente"], "Frío, fría: adjectives in -o change for gender."),
    ],
)

# ---------------------------------------------------------------------------- 160
L160 = lesson(
    "Ways to cook food, and condiments",
    "frito, asado, a la parrilla, la sal, el aceite",
    requires=["cocinar", "cocina", "receta", "sal", "aceite", "azúcar", "asado"],
    cards=[
        card("How is it cooked?",
             "Many words for cooking are past participles, so they work like adjectives: they change for gender and "
             "number. A menu says pollo frito, but papas fritas and carne asada.",
             tables=[table(["Cocinado", "English"],
                           [["frito, frita", "fried"],
                            ["asado, asada", "roasted, baked, grilled"],
                            ["hervido, hervida", "boiled"],
                            ["empanizado, empanizada", "breaded"],
                            ["a la parrilla", "on the grill"],
                            ["a la plancha", "on the griddle"],
                            ["al horno", "baked in the oven"]],
                           say=[0])]),
        card("Los condimentos",
             "Salt and sugar are small words you will use all the time. Notice that la sal, la pimienta and "
             "la mostaza are feminine, but el aceite, el vinagre and el azúcar are masculine.",
             tables=[table(["Condimento", "English"],
                           [["la sal", "salt"],
                            ["la pimienta", "black pepper"],
                            ["el aceite", "oil"],
                            ["el vinagre", "vinegar"],
                            ["el azúcar", "sugar"],
                            ["la mayonesa", "mayonnaise"],
                            ["la mostaza", "mustard"]],
                           say=[0])]),
        card("On a menu",
             "Menu phrases often use a/al or con: pescado al horno, pollo a la plancha, ensalada con aceite y vinagre.",
             examples=[
                 ex("Hoy hay pollo a la parrilla con ensalada.", "Today there is grilled chicken with salad.", "a la parrilla"),
                 ex("Mi padre prepara pescado al horno con limón.", "My father prepares oven-baked fish with lemon.", "al horno"),
                 ex("Me gustan las papas fritas con sal.", "I like french fries with salt.", "fritas"),
                 ex("Pongo aceite y vinagre en la ensalada.", "I put oil and vinegar on the salad.", "aceite y vinagre"),
             ]),
    ],
    exercises=[
        F("Hoy hay pollo ___ la parrilla.", "a", ["por", "de", "con"], "A la parrilla = on the grill.", tr="Today there is grilled chicken."),
        F("Mi padre prepara pescado ___ horno.", "al", ["a la", "del", "con el"], "A + el = al horno.", tr="My father prepares baked fish."),
        F("Me gustan las papas ___ con sal.", "fritas", ["frito", "fritos", "frita"], "Papas is feminine plural: fritas.", tr="I like french fries with salt."),
        F("Pongo aceite y ___ en la ensalada.", "vinagre", ["helado", "leche", "chocolate"], "Oil and vinegar dress a salad.", tr="I put oil and vinegar on the salad."),
        F("Me gusta la carne ___.", "asada", ["asado", "asadas", "asados"], "Carne is feminine singular.", tr="I like roasted meat."),
        M("What does “empanizado” mean?", "breaded", ["boiled", "raw", "frozen"], "Empanizado = coated in bread crumbs."),
        M("Which word is masculine?", "el aceite", ["la sal", "la pimienta", "la mostaza"], "El aceite, el vinagre, el azúcar."),
        M("What does “a la plancha” mean?", "cooked on a flat griddle", ["boiled in water", "served cold", "baked in the oven"], "Plancha = flat griddle."),
        M("Which sentence means “boiled eggs”?", "huevos hervidos", ["huevos hervido", "huevo hervidos", "huevos hervida"], "Huevos is masculine plural: hervidos."),
    ],
)

# ---------------------------------------------------------------------------- 161
L161 = lesson(
    "Eating well: a healthy lifestyle",
    "una dieta equilibrada, hacer ejercicio, no fumar",
    requires=["saludable", "sano", "ejercicio", "fumar", "entrenar", "importante", "deber"],
    cards=[
        card("Una dieta equilibrada",
             "A balanced diet is una dieta equilibrada. To talk about healthy habits you need a few verbs: "
             "adelgazar (to lose weight), engordar (to gain weight), entrenar (to train), fumar (to smoke) and "
             "hacer ejercicio (to exercise). The adjectives saludable and sano both mean “healthy”; nutritivo means “nutritious”.",
             tables=[table(["Hábito", "English"],
                           [["comer verduras y fruta", "to eat vegetables and fruit"],
                            ["beber mucha agua", "to drink a lot of water"],
                            ["hacer ejercicio", "to exercise"],
                            ["dormir ocho horas", "to sleep eight hours"],
                            ["no fumar", "not to smoke"],
                            ["comer poca grasa", "to eat little fat"]],
                           say=[0])]),
        card("Giving advice",
             "To give general advice, use hay que, es importante or debes plus an infinitive. All three are followed "
             "by the bare verb.",
             examples=[
                 ex("Hay que comer verduras todos los días.", "You have to eat vegetables every day.", "Hay que"),
                 ex("Es importante beber agua y dormir bien.", "It is important to drink water and sleep well.", "Es importante"),
                 ex("Si quieres adelgazar, debes hacer ejercicio.", "If you want to lose weight, you should exercise.", "debes"),
                 ex("Mi médico dice que fumar es malo para la salud.", "My doctor says that smoking is bad for your health.", "fumar"),
                 ex("Mi hermano entrena tres veces por semana.", "My brother works out three times a week.", "entrena"),
             ]),
    ],
    exercises=[
        F("Hay que ___ verduras todos los días.", "comer", ["comes", "como", "comiendo"], "Hay que + infinitive.", tr="You have to eat vegetables every day."),
        F("Es importante ___ mucha agua.", "beber", ["bebes", "bebo", "bebiendo"], "Es importante + infinitive.", tr="It is important to drink a lot of water."),
        F("Si quieres adelgazar, ___ hacer ejercicio.", "debes", ["debo", "debe", "debemos"], "Tú quieres → tú debes.", tr="If you want to lose weight, you should exercise.", lemma="deber:tú"),
        F("Mi hermano ___ tres veces por semana.", "entrena", ["entrenas", "entreno", "entrenan"], "Mi hermano = él: entrena.", tr="My brother works out three times a week.", lemma="entrenar:ella"),
        M("What does “engordar” mean?", "to gain weight", ["to lose weight", "to exercise", "to cook"], "Engordar = to get fat."),
        M("What does “una dieta equilibrada” mean?", "a balanced diet", ["a short vacation", "a heavy meal", "a strange habit"], "Equilibrada = balanced."),
        M("Which is a healthy habit?", "dormir ocho horas", ["fumar mucho", "comer poca fruta", "beber poca agua"], "Sleep is healthy."),
        M("How do you say “It is important to exercise”?", "Es importante hacer ejercicio.", ["Es importante hago ejercicio.", "Es importante haciendo ejercicio.", "Importante es hacer ejercicio."], "Es importante + infinitive."),
        M("Which two words mean “healthy”?", "sano and saludable", ["sano and salado", "saludable and dulce", "sano and picante"], "Sano / saludable."),
    ],
)

# ---------------------------------------------------------------------------- 162
L162 = lesson(
    "Mucho and poco: adjectives and adverbs",
    "mucha tarea, muchos amigos, poco tiempo, come poco",
    requires=["mucho", "poco", "tiempo", "amigo", "tarea", "dinero"],
    cards=[
        card("Mucho and poco as adjectives",
             "When mucho or poco describes a noun, it agrees with it in gender and number: mucho, mucha, muchos, "
             "muchas (a lot of, many) and poco, poca, pocos, pocas (little, few).",
             tables=[table(["", "Masculino", "Femenino"],
                           [["singular", "mucho tiempo", "mucha tarea"],
                            ["plural", "muchos amigos", "muchas verduras"],
                            ["singular", "poco dinero", "poca sal"],
                            ["plural", "pocos días", "pocas frutas"]],
                           say=[1, 2])]),
        card("Mucho and poco as adverbs",
             "When they describe a verb, they never change: Ella come poco, Ellos trabajan mucho. Compare: "
             "Tengo mucha hambre (adjective, with hambre) and Como mucho (adverb, with the verb).",
             examples=[
                 ex("Hoy hace mucho frío.", "Today it is very cold.", "mucho frío"),
                 ex("Él tiene mucha tarea.", "He has a lot of homework.", "mucha tarea"),
                 ex("Ella tiene muchos amigos.", "She has many friends.", "muchos amigos"),
                 ex("Tengo poco tiempo libre.", "I have little free time.", "poco tiempo"),
                 ex("Mi amigo pagó mucho por la cena.", "My friend paid a lot for the dinner.", "mucho"),
                 ex("Mi hermana come poco por la mañana.", "My sister eats little in the morning.", "poco"),
             ]),
    ],
    exercises=[
        F("Tengo ___ hambre.", "mucha", ["mucho", "muchas", "muchos"], "Hambre is feminine singular: mucha.", tr="I am very hungry."),
        F("En la mesa hay ___ platos.", "muchos", ["mucho", "mucha", "muchas"], "Platos is masculine plural.", tr="There are many plates on the table."),
        F("Hay ___ sal en la sopa.", "poca", ["poco", "pocas", "pocos"], "Sal is feminine singular.", tr="There is little salt in the soup."),
        F("Mi abuelo come ___ por la noche.", "poco", ["poca", "pocos", "pocas"], "With a verb, poco does not change.", tr="My grandfather eats little at night."),
        F("Hay ___ libros en la mesa.", "pocos", ["poco", "poca", "pocas"], "Libros is masculine plural.", tr="There are few books on the table."),
        M("Which sentence is correct?", "Ellos tienen muchas ideas.", ["Ellos tienen mucho ideas.", "Ellos tienen muchos ideas.", "Ellos tienen mucha ideas."], "Ideas is feminine plural."),
        M("Which is the adverb: “Ella trabaja mucho”?", "mucho (it does not change)", ["mucha", "muchos", "muchas"], "Adverbs are invariable."),
        M("Which sentence means “We have little time”?", "Tenemos poco tiempo.", ["Tenemos pocos tiempo.", "Tenemos poca tiempo.", "Tenemos mucho tiempo."], "Tiempo is masculine singular."),
        M("What does “pocas frutas” mean?", "few fruits", ["many fruits", "little fruit juice", "no fruits"], "Pocas = few."),
    ],
)

# ---------------------------------------------------------------------------- 163
L163 = lesson(
    "Algo and nada",
    "¿Quiere algo más? No, no quiero nada.",
    requires=["algo", "nada", "nunca", "siempre", "también", "tampoco", "querer"],
    cards=[
        card("Positive words and their opposites",
             "You already know siempre/nunca and también/tampoco. Algo (something, anything) and nada (nothing, not "
             "anything) work the same way. They do not change for gender or number.",
             tables=[table(["Afirmativo", "Negativo", "English"],
                           [["siempre", "nunca", "always · never"],
                            ["también", "tampoco", "also · neither, not either"],
                            ["algo", "nada", "something · nothing, not anything"]],
                           say=[0, 1])]),
        card("Double negatives are normal",
             "In Spanish, a negative word after the verb needs no before the verb: No quiero nada, No voy nunca "
             "al cine, No hablo francés y ella tampoco. If the negative word comes first, you drop no: Nunca voy al cine. "
             "Algo usually follows the verb.",
             examples=[
                 ex("¿Quiere usted algo más?", "Do you want anything else?", "algo"),
                 ex("No, gracias, no quiero nada más.", "No, thank you, I don’t want anything else.", "no quiero nada"),
                 ex("Quiero comer algo rico.", "I want to eat something tasty.", "algo rico"),
                 ex("Hoy no hago nada especial.", "Today I am not doing anything special.", "no hago nada"),
                 ex("Mi hermano no come carne y yo tampoco.", "My brother doesn’t eat meat and neither do I.", "tampoco"),
             ]),
    ],
    exercises=[
        F("¿Quiere usted ___ más? Sí, un café, por favor.", "algo", ["nada", "tampoco", "nunca"], "A question that expects a yes uses algo.", tr="Do you want anything else? Yes, a coffee, please."),
        F("No quiero ___ más, gracias.", "nada", ["siempre", "también", "algo"], "No + verb + nada.", tr="I don’t want anything else, thank you."),
        F("No hay ___ en el refrigerador.", "nada", ["siempre", "también", "nunca"], "No hay nada = there is nothing.", tr="There is nothing in the refrigerator."),
        F("Mi hermano no come carne y yo ___.", "tampoco", ["también", "nada", "algo"], "Negative agreement: tampoco.", tr="My brother doesn’t eat meat and neither do I."),
        F("Quiero comer ___ rico.", "algo", ["nada", "tampoco", "nunca"], "Something tasty = algo rico.", tr="I want to eat something tasty."),
        M("What does “No hago nada” mean?", "I am not doing anything", ["I do something", "I never do it", "I do it too"], "No + verb + nada."),
        M("How do you say “I don’t want anything”?", "No quiero nada.", ["Quiero nada.", "Quiero no nada.", "Quieres nada."], "Nada after the verb needs no before the verb."),
        M("What does “tampoco” mean?", "neither, not either", ["also", "never", "something"], "Tampoco is the opposite of también."),
        M("Which pair are opposites?", "algo and nada", ["algo and también", "nunca and tampoco", "siempre and también"], "Algo ↔ nada."),
    ],
)

# ---------------------------------------------------------------------------- 164
L164 = lesson(
    "Talking about the past: time words",
    "ayer, anoche, la semana pasada, el año pasado",
    requires=["ayer", "anoche", "pasado", "semana", "año", "vez", "antes"],
    cards=[
        card("When did it happen?",
             "Certain words tell you right away that a sentence is about a finished moment in the past. Pasado (last) "
             "is an adjective, so it agrees with its noun: la semana pasada, el año pasado.",
             tables=[table(["Expresión", "English"],
                           [["ayer", "yesterday"],
                            ["anteayer", "the day before yesterday"],
                            ["anoche", "last night"],
                            ["el otro día", "the other day"],
                            ["la semana pasada", "last week"],
                            ["el fin de semana pasado", "last weekend"],
                            ["el mes pasado", "last month"],
                            ["el año pasado", "last year"],
                            ["una vez", "once"],
                            ["de repente", "suddenly"]],
                           say=[0])]),
        card("The preterite: what happened?",
             "Spanish has two simple past tenses, the preterite and the imperfect. In this unit you learn the "
             "preterite. It answers the question “What happened?”: an action that is finished, at a definite moment, "
             "with a clear beginning or end, or a sudden change.",
             examples=[
                 ex("Ayer cené con mis tíos.", "Yesterday I had dinner with my aunt and uncle.", "cené"),
                 ex("La semana pasada compré un libro.", "Last week I bought a book.", "compré"),
                 ex("El año pasado viajamos a Perú.", "Last year we traveled to Peru.", "viajamos"),
                 ex("De repente, se apagó la luz.", "Suddenly, the light went out.", "se apagó"),
                 ex("Una vez probé el ceviche.", "Once I tried ceviche.", "probé"),
             ]),
    ],
    exercises=[
        F("Anoche yo ___ con mis abuelos.", "cené", ["ceno", "cenaré", "cenando"], "Anoche points to the past: cené.", tr="Last night I had dinner with my grandparents.", lemma="cenar:yo:pret"),
        F("Ayer mi hermana ___ una carta.", "escribió", ["escribe", "escribirá", "escribiendo"], "Ayer + a finished action: escribió.", tr="Yesterday my sister wrote a letter.", lemma="escribir:ella:pret"),
        F("La semana pasada ellos ___ una casa nueva.", "compraron", ["compran", "comprarán", "comprando"], "La semana pasada → preterite.", tr="Last week they bought a new house.", lemma="comprar:ellos:pret"),
        F("El año pasado tú ___ en un restaurante.", "trabajaste", ["trabajas", "trabajarás", "trabajando"], "El año pasado → preterite.", tr="Last year you worked in a restaurant.", lemma="trabajar:tú:pret"),
        M("Which word points to the past?", "ayer", ["mañana", "hoy", "pronto"], "Ayer = yesterday."),
        M("Which means “last night”?", "anoche", ["anteayer", "mañana por la noche", "esta noche"], "Anoche = last night."),
        M("Which expression uses the feminine form of pasado?", "la semana pasada", ["el año pasado", "el mes pasado", "el fin de semana pasado"], "Semana is feminine: pasada."),
        M("Which means “the day before yesterday”?", "anteayer", ["ayer", "anoche", "el otro día"], "Anteayer = two days ago."),
        M("What does “de repente” mean?", "suddenly", ["slowly", "usually", "tomorrow"], "De repente = suddenly."),
    ],
)

# ---------------------------------------------------------------------------- 165
L165 = lesson(
    "The preterite of -ar verbs",
    "hablé, hablaste, habló, hablamos, hablaron",
    requires=["hablar", "trabajar", "cenar", "comprar", "terminar", "ayer"],
    cards=[
        card("Drop -ar, add the endings",
             "To form the preterite of a regular -ar verb, drop the -ar and add: -é, -aste, -ó, -amos, -asteis, "
             "-aron. The yo and él/ella/usted forms carry a written accent; the others do not.",
             tables=[table(["", "hablar", "trabajar", "cocinar"],
                           [["yo", "habl{é}", "trabaj{é}", "cocin{é}"],
                            ["tú", "habl{aste}", "trabaj{aste}", "cocin{aste}"],
                            ["él, ella, usted", "habl{ó}", "trabaj{ó}", "cocin{ó}"],
                            ["nosotros", "habl{amos}", "trabaj{amos}", "cocin{amos}"],
                            ["vosotros", "habl{asteis}", "trabaj{asteis}", "cocin{asteis}"],
                            ["ellos, ellas, ustedes", "habl{aron}", "trabaj{aron}", "cocin{aron}"]],
                           say=[1, 2, 3])]),
        card("In a sentence",
             "The accent matters: hablo (I speak) and habló (he spoke) are different words, and so are hablo and hablé.",
             examples=[
                 ex("Ayer trabajé en casa.", "Yesterday I worked at home.", "trabajé"),
                 ex("¿Hablaste con el mesero?", "Did you talk with the waiter?", "Hablaste"),
                 ex("Mi padre cocinó pollo con papas.", "My father cooked chicken with potatoes.", "cocinó"),
                 ex("Compramos frutas en el mercado.", "We bought fruit at the market.", "Compramos"),
                 ex("Los niños cenaron temprano.", "The children had dinner early.", "cenaron"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ en casa.", "trabajé", ["trabajo", "trabajó", "trabajaré"], "Yo → -é.", tr="Yesterday I worked at home.", lemma="trabajar:yo:pret"),
        F("¿Con quién ___ tú anoche?", "hablaste", ["hablé", "habló", "hablaron"], "Tú → -aste.", tr="Who did you talk with last night?", lemma="hablar:tú:pret"),
        F("Mi madre ___ una sopa deliciosa.", "cocinó", ["cociné", "cocinaste", "cocinaron"], "Ella → -ó.", tr="My mother cooked a delicious soup.", lemma="cocinar:ella:pret"),
        F("Ellos ___ en un restaurante.", "cenaron", ["cenó", "cenamos", "cenaste"], "Ellos → -aron.", tr="They had dinner at a restaurant.", lemma="cenar:ellos:pret"),
        F("Ustedes ___ las frutas en el mercado.", "compraron", ["compraste", "compramos", "compró"], "Ustedes → -aron.", tr="You (plural) bought the fruit at the market.", lemma="comprar:ustedes:pret"),
        M("Which two forms of “hablar” carry a written accent?", "hablé and habló", ["hablaste and hablaron", "hablamos and hablasteis", "hablé and hablaron"], "Only yo and él/ella/usted."),
        M("What is the yo preterite of “cocinar”?", "cociné", ["cocino", "cocinaré", "cocinó"], "Cocin- + é."),
        M("What is the infinitive of “terminaron”?", "terminar", ["terminer", "terminir", "terminaré"], "Terminaron = ellos, -ar verb."),
        M("Which sentence means “We worked yesterday”?", "Ayer trabajamos.", ["Ayer trabajaron.", "Ayer trabajé.", "Ayer trabajaste."], "Nosotros → -amos."),
    ],
    verify=vpp("hablar", "hablé", "hablaste", "habló", "hablamos", "hablasteis", "hablaron")
           + vpp("trabajar", "trabajé", "trabajaste", "trabajó", "trabajamos", "trabajasteis", "trabajaron")
           + vpp("cocinar", "cociné", "cocinaste", "cocinó", "cocinamos", "cocinasteis", "cocinaron"),
)

# ---------------------------------------------------------------------------- 166
L166 = lesson(
    "The preterite of -er and -ir verbs",
    "comí, comiste, comió · viví, viviste, vivió",
    requires=["comer", "beber", "vivir", "escribir", "salir", "aprender"],
    cards=[
        card("One set of endings for -er and -ir",
             "Drop the -er or -ir and add: -í, -iste, -ió, -imos, -isteis, -ieron. The two groups are identical in the "
             "preterite. Again, yo and él/ella/usted carry a written accent.",
             tables=[table(["", "comer", "vivir", "escribir"],
                           [["yo", "com{í}", "viv{í}", "escrib{í}"],
                            ["tú", "com{iste}", "viv{iste}", "escrib{iste}"],
                            ["él, ella, usted", "com{ió}", "viv{ió}", "escrib{ió}"],
                            ["nosotros", "com{imos}", "viv{imos}", "escrib{imos}"],
                            ["vosotros", "com{isteis}", "viv{isteis}", "escrib{isteis}"],
                            ["ellos, ellas, ustedes", "com{ieron}", "viv{ieron}", "escrib{ieron}"]],
                           say=[1, 2, 3])]),
        card("Boot verbs lose their boot",
             "Verbs that change in the present (pienso, vuelvo) do not change in the preterite when they end in -ar "
             "or -er: pensé, volví. (Stem-changing -ir verbs are a special case that you will meet later.)",
             examples=[
                 ex("Comí arroz con pollo.", "I ate rice with chicken.", "Comí"),
                 ex("¿Viviste en España?", "Did you live in Spain?", "Viviste"),
                 ex("Mi hermana escribió una carta larga.", "My sister wrote a long letter.", "escribió"),
                 ex("Salimos temprano del restaurante.", "We left the restaurant early.", "Salimos"),
                 ex("Los niños bebieron jugo de naranja.", "The children drank orange juice.", "bebieron"),
                 ex("Volví a casa a las seis.", "I returned home at six.", "Volví"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ arroz con pollo.", "comí", ["como", "comió", "comeré"], "Yo → -í.", tr="Yesterday I ate rice with chicken.", lemma="comer:yo:pret"),
        F("¿Dónde ___ tú el año pasado?", "viviste", ["viví", "vivió", "vivieron"], "Tú → -iste.", tr="Where did you live last year?", lemma="vivir:tú:pret"),
        F("Mi hermana ___ una carta muy larga.", "escribió", ["escribí", "escribiste", "escribieron"], "Ella → -ió.", tr="My sister wrote a very long letter.", lemma="escribir:ella:pret"),
        F("Anoche nosotros ___ del restaurante a las diez.", "salimos", ["salieron", "salí", "saliste"], "Nosotros → -imos.", tr="Last night we left the restaurant at ten.", lemma="salir:nosotros:pret"),
        F("Los niños ___ jugo de naranja.", "bebieron", ["bebió", "bebimos", "bebiste"], "Los niños = ellos: -ieron.", tr="The children drank orange juice.", lemma="beber:ellos:pret"),
        F("Ayer yo ___ a casa a las seis.", "volví", ["vuelvo", "volvió", "volveré"], "Volver has no boot change in the preterite.", tr="Yesterday I returned home at six.", lemma="volver:yo:pret"),
        M("Which statement is true?", "-er and -ir verbs have the same preterite endings.", ["-er and -ir verbs have different endings.", "Only -er verbs have accents.", "-ir verbs use -aron."], "Both: -í, -iste, -ió, -imos, -isteis, -ieron."),
        M("What is the ellos preterite of “aprender”?", "aprendieron", ["aprendaron", "aprendimos", "aprenderán"], "Aprend- + ieron."),
        M("What is the infinitive of “salió”?", "salir", ["saler", "salar", "salió"], "Salió = él/ella, -ir verb."),
    ],
    verify=vpp("comer", "comí", "comiste", "comió", "comimos", "comisteis", "comieron")
           + vpp("vivir", "viví", "viviste", "vivió", "vivimos", "vivisteis", "vivieron")
           + vpp("escribir", "escribí", "escribiste", "escribió", "escribimos", "escribisteis", "escribieron"),
)

# ---------------------------------------------------------------------------- 167
L167 = lesson(
    "Nosotros: present or preterite?",
    "Ayer trabajamos allí y hoy trabajamos aquí.",
    requires=["hoy", "ayer", "ahora", "trabajar", "vivir", "comer"],
    cards=[
        card("Two tenses, one form",
             "For regular -ar and -ir verbs, the nosotros form of the present and the preterite are written the same: "
             "trabajamos, vivimos, salimos. Only -er verbs differ: comemos (present) and comimos (preterite). "
             "The time word or the situation tells you which one it is.",
             tables=[table(["Verb", "Presente", "Pretérito"],
                           [["trabajar", "trabajamos", "trabajamos"],
                            ["vivir", "vivimos", "vivimos"],
                            ["comer", "comemos", "comimos"],
                            ["cenar", "cenamos", "cenamos"]],
                           say=[1, 2])]),
        card("Use the clues",
             "Look for words like hoy, ahora and siempre (present), or ayer, anoche and el año pasado (preterite).",
             examples=[
                 ex("Ayer trabajamos allí y hoy trabajamos aquí.", "Yesterday we worked there and today we work here.", "trabajamos"),
                 ex("Anoche comimos en un restaurante peruano.", "Last night we ate at a Peruvian restaurant.", "comimos"),
                 ex("Siempre comemos juntos los domingos.", "We always eat together on Sundays.", "comemos"),
                 ex("El año pasado vivimos en Quito.", "Last year we lived in Quito.", "vivimos"),
                 ex("Ahora vivimos cerca del mercado.", "Now we live near the market.", "vivimos"),
             ]),
    ],
    exercises=[
        F("Anoche nosotros ___ pescado.", "comimos", ["comemos", "comen", "comeremos"], "Anoche → preterite: comimos.", tr="Last night we ate fish.", lemma="comer:nosotros:pret"),
        F("Hoy nosotros ___ en casa.", "comemos", ["comimos", "comieron", "comeré"], "Hoy → present: comemos.", tr="Today we eat at home.", lemma="comer:nosotros"),
        F("Siempre nosotros ___ juntos los domingos.", "comemos", ["comimos", "comerán", "comió"], "Siempre → present habit.", tr="We always eat together on Sundays.", lemma="comer:nosotros"),
        F("El año pasado nosotros ___ en otra ciudad.", "vivimos", ["viviré", "vivirán", "viven"], "The form vivimos, with a past clue.", tr="Last year we lived in another city.", lemma="vivir:nosotros:pret"),
        M("Which tense is “Ayer trabajamos”?", "preterite", ["present", "future", "the same as “trabajaremos”"], "Ayer = past."),
        M("Which tense is “Hoy trabajamos”?", "present", ["preterite", "future", "past progressive"], "Hoy = present."),
        M("For which verb do the present and the preterite nosotros forms DIFFER?", "comer", ["cenar", "vivir", "salir"], "Comemos / comimos."),
        M("What helps you tell the tenses apart?", "the time word or the context", ["the accent on the last letter", "the vowel before the last letter only", "nothing: you must ask"], "Hoy/ayer/siempre tell you."),
        M("Which clue word fits a preterite sentence?", "anoche", ["ahora", "siempre", "todos los días"], "Anoche points to the past."),
    ],
)

# ---------------------------------------------------------------------------- 168
L168 = lesson(
    "The preterite of ser and ir",
    "fui, fuiste, fue, fuimos, fuisteis, fueron",
    requires=["ser", "ir", "ayer", "viaje", "playa", "ciudad"],
    cards=[
        card("Two verbs, one preterite",
             "Ser and ir are completely irregular in the preterite, and they are identical: fui, fuiste, fue, fuimos, "
             "fuisteis, fueron. None of these forms carries a written accent. The context tells you which verb it is.",
             tables=[table(["", "ser / ir"],
                           [["yo", "{fui}"],
                            ["tú", "{fuiste}"],
                            ["él, ella, usted", "{fue}"],
                            ["nosotros", "{fuimos}"],
                            ["vosotros", "{fuisteis}"],
                            ["ellos, ellas, ustedes", "{fueron}"]],
                           say=[1])]),
        card("Which verb is it?",
             "Ir is usually followed by a (to a place): Fui a la playa. Ser is followed by a noun or adjective, "
             "and does not use a: Fue un día largo.",
             examples=[
                 ex("Fui a la playa en mis vacaciones.", "I went to the beach on my vacation.", "Fui a"),
                 ex("Fue un viaje muy largo.", "It was a very long trip.", "Fue"),
                 ex("¿Adónde fuiste el sábado?", "Where did you go on Saturday?", "fuiste"),
                 ex("Mis padres fueron a Cuba el año pasado.", "My parents went to Cuba last year.", "fueron a"),
                 ex("Fuimos al mercado por la mañana.", "We went to the market in the morning.", "Fuimos al"),
                 ex("Mi abuelo fue cocinero por muchos años.", "My grandfather was a cook for many years.", "fue cocinero"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ al mercado.", "fui", ["fue", "fuiste", "voy"], "Yo + ir: fui.", tr="Yesterday I went to the market.", lemma="ir:yo:pret"),
        F("¿Adónde ___ tú el sábado?", "fuiste", ["fui", "fue", "fueron"], "Tú: fuiste.", tr="Where did you go on Saturday?", lemma="ir:tú:pret"),
        F("Mis padres ___ a Cuba el año pasado.", "fueron", ["fue", "fuimos", "fui"], "Mis padres = ellos: fueron.", tr="My parents went to Cuba last year.", lemma="ir:ellos:pret"),
        F("Nosotros ___ a la playa en julio.", "fuimos", ["fueron", "fui", "fuiste"], "Nosotros: fuimos.", tr="We went to the beach in July.", lemma="ir:nosotros:pret"),
        F("El viaje ___ muy largo.", "fue", ["fui", "fuiste", "fueron"], "El viaje = it: fue (ser).", tr="The trip was very long.", lemma="ser:ella:pret"),
        M("Which verb is “fuimos” in “Fuimos al cine”?", "ir", ["ser", "estar", "hacer"], "Al cine = to the cinema: ir."),
        M("Which verb is “fue” in “Fue un día excelente”?", "ser", ["ir", "estar", "tener"], "Un día excelente describes the day: ser."),
        M("Do the forms fui and fue carry a written accent?", "no", ["yes, both", "only fui", "only fue"], "They are one-syllable words with no accent."),
        M("How do you say “She went to the bank”?", "Ella fue al banco.", ["Ella fui al banco.", "Ella fuiste al banco.", "Ella fuimos al banco."], "Ella + ir: fue."),
    ],
    verify=vpp("ser", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron")
           + vpp("ir", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"),
)

# ---------------------------------------------------------------------------- 169
L169 = lesson(
    "Telling your story in the preterite",
    "Nací en Texas. Me gradué en dos mil veinte.",
    requires=["nacer", "estudiar", "casar", "mudar", "trabajar", "año"],
    cards=[
        card("Life events",
             "The preterite is the tense for life events: you were born once, you graduated on a definite date. "
             "Nacer is used without estar: Nací en Lima means “I was born in Lima.” Some events use a reflexive "
             "verb: graduarse, casarse, mudarse.",
             tables=[table(["Evento", "English"],
                           [["Nací en un pueblo pequeño.", "I was born in a small town."],
                            ["Crecí en la costa.", "I grew up on the coast."],
                            ["Estudié en la universidad.", "I studied at the university."],
                            ["Me gradué en dos mil veinte.", "I graduated in 2020."],
                            ["Me mudé a otra ciudad.", "I moved to another city."],
                            ["Conocí a mi esposo en el trabajo.", "I met my husband at work."]],
                           say=[0])]),
        card("Reflexive verbs in the preterite",
             "Place the reflexive pronoun before the preterite form, just like in the present: me casé, te casaste, "
             "se casó. The nosotros form is identical to the present: nos mudamos.",
             tables=[table(["", "casarse"],
                           [["yo", "me cas{é}"],
                            ["tú", "te cas{aste}"],
                            ["él, ella, usted", "se cas{ó}"],
                            ["nosotros", "nos cas{amos}"],
                            ["vosotros", "os cas{asteis}"],
                            ["ellos, ellas, ustedes", "se cas{aron}"]],
                           say=[1]),
                     ],
             examples=[
                 ex("Mi hermana se casó el sábado pasado.", "My sister got married last Saturday.", "se casó"),
                 ex("Nos mudamos a Chile en dos mil diez.", "We moved to Chile in 2010.", "Nos mudamos"),
                 ex("Mis padres nacieron en el campo.", "My parents were born in the countryside.", "nacieron"),
             ]),
    ],
    exercises=[
        F("Yo ___ en un pueblo pequeño.", "nací", ["nazco", "nació", "nacimos"], "Nacer → nací (no estar needed).", tr="I was born in a small town.", lemma="nacer:yo:pret"),
        F("Mi hermana ___ el sábado pasado.", "se casó", ["me casé", "se casaron", "nos casamos"], "Mi hermana = ella: se casó.", tr="My sister got married last Saturday."),
        F("Yo ___ en dos mil veinte.", "me gradué", ["se graduó", "te graduaste", "nos graduamos"], "Yo: me gradué.", tr="I graduated in 2020."),
        F("Nosotros ___ a Chile en dos mil diez.", "nos mudamos", ["me mudé", "se mudó", "se mudaron"], "Nosotros: nos mudamos.", tr="We moved to Chile in 2010."),
        F("Mis padres ___ en el campo.", "nacieron", ["nació", "nacimos", "nací"], "Mis padres = ellos: nacieron.", tr="My parents were born in the countryside.", lemma="nacer:ellos:pret"),
        M("How do you say “I was born in Lima”?", "Nací en Lima.", ["Fui nacer en Lima.", "Estuve nací en Lima.", "Nazco en Lima."], "Nací = I was born."),
        M("Which tense do you use for life events like graduating?", "the preterite", ["the future", "the present progressive", "the infinitive"], "They happened at a definite time."),
        M("Where does the reflexive pronoun go in “me casé”?", "before the verb", ["after the verb", "in the middle of the verb", "it is not used"], "Me + verb."),
        M("What does “Me mudé a otra ciudad” mean?", "I moved to another city.", ["I met another city.", "I will move.", "I always move."], "Mudarse = to move (house)."),
    ],
    verify=vpp("casar", "casé", "casaste", "casó", "casamos", "casasteis", "casaron"),
)

# ---------------------------------------------------------------------------- 170
L170 = lesson(
    "Direct objects: what? whom?",
    "Rosa compró pan. Tomás llamó a sus amigas.",
    requires=["comprar", "llamar", "invitar", "cocinar", "pan", "arroz", "amiga"],
    cards=[
        card("What is a direct object?",
             "The direct object is the person or thing that receives the action of the verb. To find it, ask the verb "
             "“what?” or “whom?”. In Rosa compró pan, ask: what did Rosa buy? Pan. So pan is the direct object. "
             "In Tomás llamó a sus amigas, ask: whom did Tomás call? Sus amigas.",
             tables=[table(["Oración", "Objeto directo"],
                           [["Rosa compró pan.", "pan"],
                            ["Tomás llamó a sus amigas.", "a sus amigas"],
                            ["Mi madre cocinó el arroz.", "el arroz"],
                            ["Nosotros invitamos a Roberto.", "a Roberto"]],
                           say=[0, 1])]),
        card("Not every phrase is a direct object",
             "Words that tell you where, when or how are not direct objects. In Mi madre cocinó el arroz en la cocina, "
             "the direct object is el arroz; en la cocina only says where. In Rosa compró pan ayer, ayer says when.",
             examples=[
                 ex("Rosa compró pan ayer.", "Rosa bought bread yesterday.", "pan"),
                 ex("Tomás llamó a sus amigas por teléfono.", "Tomás called his friends on the phone.", "a sus amigas"),
                 ex("Mi madre cocinó el arroz en la cocina.", "My mother cooked the rice in the kitchen.", "el arroz"),
                 ex("Nosotros invitamos a Roberto a cenar.", "We invited Roberto to dinner.", "a Roberto"),
                 ex("Ellos prepararon la ensalada.", "They prepared the salad.", "la ensalada"),
             ]),
    ],
    exercises=[
        F("Ayer Rosa ___ pan en el mercado.", "compró", ["compra", "compraron", "compré"], "Ayer → preterite; Rosa → ella: compró.", tr="Yesterday Rosa bought bread at the market.", lemma="comprar:ella:pret"),
        F("Tomás ___ a sus amigas por teléfono.", "llamó", ["llamo", "llamé", "llamaron"], "Tomás → él: llamó.", tr="Tomás called his friends on the phone.", lemma="llamar:él:pret"),
        F("Anoche nosotros ___ a Roberto a cenar.", "invitamos", ["invitan", "invitó", "invitaron"], "Nosotros → -amos.", tr="Last night we invited Roberto to dinner.", lemma="invitar:nosotros:pret"),
        F("Ayer mi madre ___ el arroz.", "cocinó", ["cocina", "cocinaron", "cociné"], "Mi madre → ella: cocinó.", tr="Yesterday my mother cooked the rice.", lemma="cocinar:ella:pret"),
        M("In “Rosa compró pan ayer”, what is the direct object?", "pan", ["Rosa", "compró", "ayer"], "What did Rosa buy? Pan."),
        M("In “Tomás llamó a sus amigas”, what is the direct object?", "a sus amigas", ["Tomás", "llamó", "por teléfono"], "Whom did Tomás call? Sus amigas."),
        M("Which question helps you find the direct object?", "What, or whom", ["Where", "When", "Why"], "Ask the verb what or whom."),
        M("In “Mi madre cocinó el arroz en la cocina”, which phrase is the direct object?", "el arroz", ["en la cocina", "Mi madre", "cocinó"], "En la cocina tells where."),
        M("Which sentence has a direct object?", "Ellos prepararon la ensalada.", ["Ellos salieron ayer.", "Ella llegó temprano.", "Nosotros vivimos en Quito."], "Only the first answers what? (la ensalada)."),
    ],
    verify=vpp("comprar", "compré", "compraste", "compró", "compramos", "comprasteis", "compraron")
           + vpp("llamar", "llamé", "llamaste", "llamó", "llamamos", "llamasteis", "llamaron")
           + vpp("invitar", "invité", "invitaste", "invitó", "invitamos", "invitasteis", "invitaron")
           + vpp("cocinar", "cociné", "cocinaste", "cocinó", "cocinamos", "cocinasteis", "cocinaron"),
)

# ---------------------------------------------------------------------------- 171
L171 = lesson(
    "Direct object pronouns: lo, la, los, las",
    "Rosa lo compró. Tomás las invitó.",
    requires=["comprar", "invitar", "preparar", "comer", "cuenta", "pan"],
    cards=[
        card("Replacing the direct object",
             "To avoid repeating a noun, Spanish replaces the direct object with a pronoun. The pronoun matches the "
             "noun in gender and number: Rosa compró el pan → Rosa lo compró. Tomás invitó a sus amigas → Tomás las "
             "invitó.",
             tables=[table(["", "Singular", "Plural"],
                           [["me · us", "me", "nos"],
                            ["him · it (masculine) · you (formal, masculine)", "lo", "los"],
                            ["her · it (feminine) · you (formal, feminine)", "la", "las"]],
                           note="Te means “you” (familiar): ¿Te llamo mañana?",
                           say=[1, 2])]),
        card("Choosing the pronoun",
             "Ask what the noun is: el pan is masculine singular → lo; la cuenta is feminine singular → la; los "
             "tacos → los; las chuletas → las. In parts of Spain, le (and les) are used instead of "
             "lo (and los) for a man or men, but lo is always correct.",
             examples=[
                 ex("Rosa compró el pan. Rosa lo compró ayer.", "Rosa bought the bread. She bought it yesterday.", "lo"),
                 ex("Tomás invitó a sus amigas. Tomás las invitó a cenar.", "Tomás invited his friends. He invited them to dinner.", "las"),
                 ex("Preparé la ensalada. La preparé con tomate.", "I prepared the salad. I prepared it with tomato.", "La"),
                 ex("Mis padres nos invitaron a su casa.", "My parents invited us to their house.", "nos"),
                 ex("¿Me llamas esta noche? Sí, te llamo.", "Will you call me tonight? Yes, I’ll call you.", "te"),
             ]),
    ],
    exercises=[
        F("Rosa compró el pan. Rosa ___ compró ayer.", "lo", ["la", "los", "las"], "Pan is masculine singular.", tr="Rosa bought the bread. She bought it yesterday."),
        F("Tomás llamó a sus amigas. Tomás ___ invitó a cenar.", "las", ["los", "la", "lo"], "Amigas is feminine plural.", tr="Tomás called his friends. He invited them to dinner."),
        F("Preparé la ensalada. Yo ___ preparé ayer.", "la", ["lo", "las", "los"], "Ensalada is feminine singular.", tr="I prepared the salad. I prepared it yesterday."),
        F("Ellos comieron los tacos. Ellos ___ comieron anoche.", "los", ["lo", "las", "la"], "Tacos is masculine plural.", tr="They ate the tacos. They ate them last night."),
        F("Mis padres ___ invitaron a mi hermano y a mí a su casa.", "nos", ["me", "los", "las"], "Mi hermano y yo = nosotros → nos.", tr="My parents invited my brother and me to their house."),
        M("Which pronoun replaces “la cuenta”?", "la", ["lo", "las", "los"], "Cuenta is feminine singular."),
        M("Which pronoun replaces “el postre”?", "lo", ["la", "los", "las"], "Postre is masculine singular."),
        M("What does “Ella las compró” mean if las stands for “las chuletas”?", "She bought them.", ["She bought it.", "She bought him.", "They bought her."], "Las = them (feminine plural)."),
        M("What does “Sí, te veo” mean?", "Yes, I see you.", ["Yes, you see me.", "Yes, I see him.", "Yes, I see them."], "Te = you (familiar)."),
    ],
)

# ---------------------------------------------------------------------------- 172
L172 = lesson(
    "The personal a",
    "Visité a Roberto. Visité el museo.",
    requires=["visitar", "llamar", "invitar", "ayudar", "conocer", "cuidar", "buscar", "necesitar", "tener", "gato", "perro"],
    cards=[
        card("A before a specific person",
             "When the direct object is a specific person (or a pet you care about), Spanish puts the word a in front "
             "of it. This personal a has no English translation. When the object is a thing, there is no a. "
             "A + el always becomes al.",
             tables=[table(["Persona o animal: con a", "Cosa: sin a"],
                           [["Visité a Roberto.", "Visité el mercado."],
                            ["Llamo a mis amigas.", "Llamo un taxi."],
                            ["Cuidamos a los gatos.", "Cuidamos la casa."],
                            ["Busco a mi hermana.", "Busco un restaurante."]],
                           say=[0, 1])]),
        card("When there is no personal a",
             "Skip the a when the person is not specific: Necesitamos un buen cocinero; Mi jefe busca gente con "
             "experiencia. Also skip it after tener: Mi vecino tiene tres perros. Common verbs that take the "
             "personal a with people: cuidar, ver, invitar, conocer, querer, amar, encontrar, ayudar.",
             examples=[
                 ex("Ayer invitamos al jefe a cenar.", "Yesterday we invited the boss to dinner.", "al"),
                 ex("Ella cuidó a sus gatos.", "She took care of her cats.", "a"),
                 ex("Necesitamos un buen cocinero.", "We need a good cook.", "un buen cocinero"),
                 ex("Mi jefe busca gente con experiencia.", "My boss is looking for people with experience.", "gente"),
                 ex("Mi vecino tiene tres perros.", "My neighbor has three dogs.", "tiene"),
             ]),
    ],
    exercises=[
        F("Ayer visité ___ Roberto.", "a", ["al", "en", "de"], "A specific person → personal a.", tr="Yesterday I visited Roberto."),
        F("Nosotros llamamos ___ camarero.", "al", ["a", "el", "del"], "A + el = al.", tr="We called the waiter."),
        F("Todos los días cuido ___ mis gatos.", "a", ["al", "con", "en"], "Pets you care for take the personal a.", tr="Every day I take care of my cats."),
        F("Busco ___ mi hermana en el mercado.", "a", ["al", "de", "en"], "Specific person → a.", tr="I am looking for my sister at the market."),
        F("¿Conoces ___ la profesora de español?", "a", ["al", "de", "la"], "Specific person → a.", tr="Do you know the Spanish teacher?"),
        M("Which sentence is correct?", "Invitamos a Laura a cenar.", ["Invitamos Laura a cenar.", "Invitamos al Laura a cenar.", "Invitamos de Laura a cenar."], "Specific person → personal a."),
        M("Which correct sentence has NO personal a?", "Mi jefe busca gente con experiencia.", ["Ayudo a mi vecino.", "Llamo a mis amigas.", "Cuidamos a los gatos."], "Gente is not a specific person here."),
        M("What happens after “tener” with people?", "Usually no personal a: Tengo tres hermanas.", ["Always a: Tengo a tres hermanas.", "Always al: Tengo al tres hermanas.", "Always de: Tengo de tres hermanas."], "The personal a is not generally used with tener."),
        M("What does a + el become?", "al", ["del", "el", "a el"], "A + el = al."),
    ],
)

# ---------------------------------------------------------------------------- 173
L173 = lesson(
    "Where does the object pronoun go?",
    "Lo hago. Lo voy a hacer. Voy a hacerlo.",
    requires=["hacer", "comprar", "lavar", "preparar", "tener", "estar", "fruta", "café"],
    cards=[
        card("One verb, or a negative",
             "With one verb, put the pronoun right before the conjugated verb: Ellos prepararon la ensalada → Ellos la "
             "prepararon. In a negative sentence, no goes before the pronoun: Yo no lo hago en casa.",
             examples=[
                 ex("Ellos la prepararon.", "They prepared it.", "la"),
                 ex("Yo no lo hago en casa.", "I don’t make it at home.", "no lo"),
                 ex("Laura las compra todos los días.", "Laura buys them every day.", "las"),
             ]),
        card("Two verbs: two choices",
             "With a conjugated verb plus an infinitive you may either put the pronoun before the first verb or "
             "attach it to the end of the infinitive. Both mean the same.",
             tables=[table(["Antes del primer verbo", "Pegado al infinitivo"],
                           [["Tomás lo va a comprar.", "Tomás va a comprarlo."],
                            ["La tenemos que lavar.", "Tenemos que lavarla."],
                            ["Laura las quiere preparar.", "Laura quiere prepararlas."]],
                           say=[0, 1])]),
        card("With -ando and -iendo",
             "With the present progressive you can also choose. When you attach the pronoun to -ando or -iendo you add "
             "a written accent so the stress stays in the same place: está preparando → está preparándolas; está "
             "comiendo → está comiéndolo.",
             examples=[
                 ex("Laura las está preparando.", "Laura is preparing them.", "las"),
                 ex("Laura está preparándolas.", "Laura is preparing them.", "preparándolas"),
                 ex("Mi hermano está lavándola.", "My brother is washing it.", "lavándola"),
             ]),
    ],
    exercises=[
        F("Voy a comprar el pescado. Voy a ___ hoy.", "comprarlo", ["comprarla", "comprarlos", "comprarlas"], "Pescado is masculine singular → -lo.", tr="I am going to buy the fish. I am going to buy it today."),
        F("Tenemos que lavar la fruta. La ___ que lavar.", "tenemos", ["tienen", "tengo", "tiene"], "Nosotros → tenemos.", tr="We have to wash the fruit. We have to wash it.", lemma="tener:nosotros"),
        F("Laura prepara las chuletas. Laura las ___ preparando.", "está", ["estoy", "están", "estás"], "Laura → ella: está.", tr="Laura is preparing the chops. Laura is preparing them.", lemma="estar:ella"),
        F("Yo no hago el café en casa. Yo no ___ hago en casa.", "lo", ["la", "los", "las"], "Café is masculine singular.", tr="I don’t make coffee at home. I don’t make it at home."),
        F("Laura está lavando la fruta. Laura está ___.", "lavándola", ["lavándolo", "lavándolas", "lavándolos"], "Fruta → -la, and the accent stays on the á.", tr="Laura is washing the fruit. Laura is washing it."),
        M("Which sentence is correct?", "Tomás va a comprarlo.", ["Tomás va lo comprar.", "Tomás lo va comprar.", "Tomás va a lo comprar."], "Attach to the infinitive or put before the first verb."),
        M("Where does “no” go?", "Before the pronoun: No lo hago.", ["After the pronoun: Lo no hago.", "At the end: Lo hago no.", "After the verb: Hago no lo."], "No + pronoun + verb."),
        M("Why does “preparándola” have a written accent?", "To keep the stress where it was", ["It is a plural", "It is a question", "It marks the preterite"], "Adding a pronoun moves the stress, so the accent is written."),
        M("Which pair both mean “We have to wash it” (la fruta)?", "La tenemos que lavar. · Tenemos que lavarla.", ["Tenemos la que lavar. · Tenemos que lavar la.", "Tenemos que la lavar. · La lavar tenemos.", "La lavar tenemos. · Tenemos lavarla que."], "Before the first verb, or attached to the infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 174
L174 = lesson(
    "Answering with a pronoun in the preterite",
    "¿Quién pagó la cuenta? Yo la pagué.",
    requires=["pagar", "lavar", "cortar", "preparar", "olvidar", "llevar", "cuenta", "verdura"],
    cards=[
        card("Question and short answer",
             "A natural answer to ¿Quién…? uses the subject, a pronoun and the preterite verb. The pronoun comes "
             "before the verb: ¿Quién preparó el menú? El cocinero lo preparó.",
             tables=[table(["Pregunta", "Respuesta"],
                           [["¿Quién preparó el almuerzo?", "Nosotros lo preparamos."],
                            ["¿Quién lavó la verdura?", "Un cocinero la lavó."],
                            ["¿Quién cortó las verduras?", "Los cocineros las cortaron."],
                            ["¿Quién pagó la cuenta?", "Yo la pagué."]],
                           say=[0, 1])]),
        card("A spelling change: pagué",
             "In the preterite, pagar adds a u in the yo form so that the g keeps its hard sound: yo pagué (not pagé). "
             "All the other forms are regular: pagaste, pagó, pagamos, pagaron.",
             examples=[
                 ex("Yo la pagué con mi tarjeta.", "I paid it with my card.", "pagué"),
                 ex("Nosotros lo llevamos a la mesa.", "We took it to the table.", "lo llevamos"),
                 ex("Yo lo olvidé en casa.", "I forgot it at home.", "olvidé"),
             ]),
    ],
    exercises=[
        F("¿Quién pagó la cuenta? Yo la ___.", "pagué", ["pagó", "pagamos", "pagaron"], "Yo → pagué.", tr="Who paid the bill? I paid it.", lemma="pagar:yo:pret"),
        F("¿Quién lavó la verdura? Un cocinero la ___ ayer.", "lavó", ["lavé", "lavaron", "lavamos"], "Un cocinero → él: lavó.", tr="Who washed the vegetables? A cook washed them yesterday.", lemma="lavar:él:pret"),
        F("¿Quién cortó las verduras? Los cocineros las ___.", "cortaron", ["cortó", "cortamos", "corté"], "Los cocineros → ellos: cortaron.", tr="Who cut the vegetables? The cooks cut them.", lemma="cortar:ellos:pret"),
        F("¿Quién preparó el almuerzo? Nosotros lo ___ en la cocina.", "preparamos", ["prepararon", "preparó", "preparé"], "Nosotros → preparamos.", tr="Who prepared lunch? We prepared it in the kitchen.", lemma="preparar:nosotros:pret"),
        F("¿Quién olvidó el postre? Yo lo ___.", "olvidé", ["olvidó", "olvidaron", "olvidamos"], "Yo → olvidé.", tr="Who forgot the dessert? I forgot it.", lemma="olvidar:yo:pret"),
        M("In “Nosotros lo llevamos a la mesa”, which pronoun is right for “el pan”?", "lo", ["la", "los", "las"], "Pan is masculine singular."),
        M("In “Ella la compró”, what could “la” stand for?", "la fruta", ["el pan", "los tacos", "las chuletas"], "La = feminine singular."),
        M("Which answer fits “¿Quién preparó las chuletas?”", "Los cocineros las prepararon.", ["Los cocineros lo prepararon.", "Los cocineros las preparó.", "Los cocineros los preparó."], "Las + ellos: prepararon."),
        M("Why does “Yo la pagué” end in -gué?", "To keep the hard g sound", ["Because it is plural", "Because it is present", "Because la is feminine"], "Pagar → pagué keeps the g hard."),
    ],
    verify=vpp("pagar", "pagué", "pagaste", "pagó", "pagamos", "pagasteis", "pagaron")
           + vpp("lavar", "lavé", "lavaste", "lavó", "lavamos", "lavasteis", "lavaron")
           + vpp("cortar", "corté", "cortaste", "cortó", "cortamos", "cortasteis", "cortaron")
           + vpp("preparar", "preparé", "preparaste", "preparó", "preparamos", "preparasteis", "prepararon")
           + vpp("olvidar", "olvidé", "olvidaste", "olvidó", "olvidamos", "olvidasteis", "olvidaron"),
)

# ---------------------------------------------------------------------------- 175
L175 = lesson(
    "Ordering at a restaurant",
    "¿Qué desea tomar? Para mí, el pollo con arroz.",
    requires=["restaurante", "mesa", "pedir", "cuenta", "traer", "querer", "sopa", "pollo", "arroz", "agua", "señor", "desear"],
    cards=[
        card("What the waiter says and what you say",
             "A waiter is a camarero (in Mexico and much of Latin America also mesero). Use usted with the staff. "
             "To ask politely, say ¿Me trae…? (literally, “do you bring me…?”). Para mí means “for me”.",
             tables=[table(["El camarero dice", "El cliente dice"],
                           [["Buenas noches. ¿Cuántas personas son?", "Una mesa para dos, por favor."],
                            ["Aquí tiene el menú.", "¿Me trae el menú, por favor?"],
                            ["¿Qué desea tomar?", "Para beber, agua, por favor."],
                            ["¿Y para comer?", "Para mí, el pollo con arroz."],
                            ["¿Algo más?", "Nada más, gracias."],
                            ["Aquí tiene la cuenta.", "¿Está incluida la propina?"]],
                           say=[0, 1])]),
        card("Useful phrases",
             "The tip is la propina; the menu is el menú. When you want the bill, say La cuenta, por favor.",
             examples=[
                 ex("Señor, ¿me trae la cuenta, por favor?", "Sir, will you bring me the check, please?", "me trae"),
                 ex("Quiero la sopa del día.", "I want the soup of the day.", "Quiero"),
                 ex("¿Qué desea tomar?", "What would you like to drink?", "desea"),
                 ex("Para mí, el pollo con arroz.", "For me, the chicken with rice.", "Para mí"),
                 ex("¿Está incluida la propina en la cuenta?", "Is the tip included in the bill?", "propina"),
             ]),
    ],
    exercises=[
        F("Señor, ¿me ___ la cuenta, por favor?", "trae", ["traigo", "traen", "traemos"], "Usted → trae.", tr="Sir, will you bring me the check, please?", lemma="traer:usted"),
        F("Camarero: ¿Qué ___ tomar, señora?", "desea", ["deseo", "desean", "deseamos"], "Usted → desea.", tr="Waiter: What would you like to drink, ma’am?", lemma="desear:usted"),
        F("Una mesa ___ dos, por favor.", "para", ["de", "en", "con"], "Para = for.", tr="A table for two, please."),
        F("Para ___, el pollo con arroz.", "mí", ["yo", "me", "mi"], "After para: mí.", tr="For me, the chicken with rice."),
        F("¿Está incluida la ___ en la cuenta?", "propina", ["mesa", "sopa", "agua"], "La propina is the tip.", tr="Is the tip included in the bill?"),
        M("Who says “¿Qué desea tomar?”", "The waiter", ["The customer", "The cook", "A friend"], "The waiter asks what you want to drink."),
        M("What does “La cuenta, por favor” mean?", "The check, please.", ["The menu, please.", "The soup, please.", "The table, please."], "Cuenta = bill, check."),
        M("How do you politely ask a waiter for the menu?", "¿Me trae el menú, por favor?", ["¿Yo traigo el menú, por favor?", "¿Me traer el menú, por favor?", "¿Trae me el menú, por favor?"], "¿Me trae…? + por favor."),
        M("What does “Para mí, el pollo” mean?", "For me, the chicken.", ["For you, the chicken.", "I am the chicken.", "Chicken for us."], "Para mí = for me."),
    ],
    verify=vp("traer", "traigo", "traes", "trae", "traemos", "traéis", "traen")
           + vp("desear", "deseo", "deseas", "desea", "deseamos", "deseáis", "desean"),
)

# ---------------------------------------------------------------------------- 176
L176 = lesson(
    "Setting the table",
    "el plato, el vaso, la copa, la taza, el tenedor, la cuchara",
    requires=["plato", "vaso", "copa", "cuchillo", "mesa", "sucio", "colocar", "otro"],
    cards=[
        card("On the table",
             "Learn the words with their articles, because the gender matters when you replace them with a pronoun.",
             tables=[table(["Palabra", "English"],
                           [["el plato", "plate, dish"],
                            ["el vaso", "glass (for water, juice)"],
                            ["la copa", "wine glass, goblet"],
                            ["la taza", "cup (for coffee, tea)"],
                            ["el cuchillo", "knife"],
                            ["el tenedor", "fork"],
                            ["la cuchara", "spoon"],
                            ["la servilleta", "napkin"],
                            ["el mantel", "tablecloth"]],
                           say=[0])]),
        card("Asking for what is missing",
             "Use Necesito + otro or otra to ask for another one: otro tenedor, otra servilleta. Los cubiertos is the "
             "word for all the silverware together. With a direct object pronoun: ¿Quién colocó los cubiertos? Los "
             "meseros los colocaron.",
             examples=[
                 ex("Necesito otro tenedor, por favor.", "I need another fork, please.", "otro tenedor"),
                 ex("No hay servilleta en mi mesa.", "There is no napkin at my table.", "No hay"),
                 ex("Este vaso está sucio.", "This glass is dirty.", "sucio"),
                 ex("La sopa está fría.", "The soup is cold.", "fría"),
                 ex("Los meseros colocaron los cubiertos.", "The waiters placed the silverware.", "colocaron"),
             ]),
    ],
    exercises=[
        F("Yo corto la carne con el ___.", "cuchillo", ["cuchara", "taza", "vaso"], "You cut with a knife.", tr="I cut the meat with the knife."),
        F("Tomo la sopa con la ___.", "cuchara", ["copa", "servilleta", "taza"], "Soup is eaten with a spoon.", tr="I eat the soup with the spoon."),
        F("El camarero puso el café en la ___.", "taza", ["copa", "cuchara", "servilleta"], "Coffee goes in a cup.", tr="The waiter put the coffee in the cup."),
        F("Bebo el vino en una ___.", "copa", ["taza", "cuchara", "servilleta"], "Wine goes in a wine glass.", tr="I drink the wine from a wine glass."),
        F("Los meseros colocaron los cubiertos. Los meseros los ___ ayer.", "colocaron", ["colocó", "colocamos", "coloqué"], "Ellos → colocaron.", tr="The waiters placed the silverware. They placed them yesterday.", lemma="colocar:ellos:pret"),
        M("Which one do you use to drink water?", "el vaso", ["el tenedor", "el cuchillo", "el mantel"], "Vaso = glass."),
        M("What does “Necesito otro tenedor” mean?", "I need another fork.", ["I need a knife.", "I need the other spoon.", "I need a napkin."], "Otro tenedor = another fork."),
        M("What does “La sopa está fría” mean?", "The soup is cold.", ["The soup is hot.", "The soup is sweet.", "The soup is good."], "Fría = cold."),
        M("How do you say “I need a napkin, please”?", "Necesito una servilleta, por favor.", ["Necesito un servilleta, por favor.", "Necesita una servilleta, por favor.", "Necesitan una servilleta, por favor."], "Servilleta is feminine; necesito = I need."),
    ],
    verify=vpp("colocar", "coloqué", "colocaste", "colocó", "colocamos", "colocasteis", "colocaron"),
)

# ---------------------------------------------------------------------------- 177
L177 = lesson(
    "Reading a menu and telling a life story",
    "pollo a la parrilla, pescado frito · Ernesto nació, trabajó y vendió",
    requires=["pollo", "pescado", "arroz", "sopa", "queso", "nacer", "decidir", "vender", "comprar", "abrir", "receta", "camión"],
    cards=[
        card("A menu",
             "Menus use short noun phrases. A la parrilla means grilled, frito means fried, a la plancha means "
             "cooked on a flat hot surface, and del día means “of the day”. Here is a small menu.",
             tables=[table(["Plato", "English"],
                           [["sopa del día", "soup of the day"],
                            ["pollo a la parrilla con arroz", "grilled chicken with rice"],
                            ["pescado frito con ensalada", "fried fish with salad"],
                            ["verduras a la plancha con queso", "vegetables on the griddle with cheese"],
                            ["bistec con papas fritas", "steak with french fries"],
                            ["flan", "caramel custard"],
                            ["helado de chocolate", "chocolate ice cream"],
                            ["jugo de naranja", "orange juice"]],
                           say=[0])]),
        card("A story in the preterite",
             "Menus and signs are good reading practice, and so are short life stories. Read about a neighbor who "
             "opened a food truck; every verb is in the preterite.",
             examples=[
                 ex("Mi vecino Ernesto nació en un pueblo pequeño.", "My neighbor Ernesto was born in a small town.", "nació"),
                 ex("Trabajó muchos años en un restaurante.", "He worked for many years in a restaurant.", "Trabajó"),
                 ex("Un día decidió abrir su propio camión de comida.", "One day he decided to open his own food truck.", "decidió"),
                 ex("Preparó las recetas de su abuela y vendió tacos y sopa.", "He prepared his grandmother’s recipes and sold tacos and soup.", "vendió"),
                 ex("Fue un éxito, y compró otro camión.", "It was a success, and he bought another truck.", "compró"),
             ]),
    ],
    exercises=[
        F("Mi vecino Ernesto ___ en un pueblo pequeño.", "nació", ["nace", "nacieron", "nací"], "Él → nació.", tr="My neighbor Ernesto was born in a small town.", lemma="nacer:él:pret"),
        F("Un día Ernesto ___ abrir su propio camión.", "decidió", ["decide", "decidieron", "decidí"], "Él → decidió.", tr="One day Ernesto decided to open his own truck.", lemma="decidir:él:pret"),
        F("Ernesto ___ tacos y sopa en su camión ayer.", "vendió", ["vende", "vendieron", "vendí"], "Él → vendió.", tr="Ernesto sold tacos and soup in his truck yesterday.", lemma="vender:él:pret"),
        F("Su camión fue un éxito. Después ___ otro camión.", "compró", ["compra", "compraron", "compré"], "Él → compró.", tr="His truck was a success. Afterwards he bought another truck.", lemma="comprar:él:pret"),
        M("Which dish is best for someone who does not eat meat or fish?", "verduras a la plancha con queso", ["bistec con papas fritas", "pollo a la parrilla con arroz", "pescado frito con ensalada"], "Vegetables and cheese, no meat or fish."),
        M("Which item on the menu is a dessert?", "flan", ["sopa del día", "jugo de naranja", "pescado frito"], "Flan is a dessert."),
        M("What does “a la parrilla” mean?", "grilled", ["fried", "boiled", "raw"], "Parrilla = grill."),
        M("What does “frito” mean?", "fried", ["grilled", "frozen", "fresh"], "Frito comes from freír."),
        M("In the story, what did Ernesto decide to do?", "open a food truck", ["buy a house", "work in a hotel", "leave the town"], "Decidió abrir su propio camión."),
    ],
    verify=vpp("nacer", "nací", "naciste", "nació", "nacimos", "nacisteis", "nacieron")
           + vpp("decidir", "decidí", "decidiste", "decidió", "decidimos", "decidisteis", "decidieron")
           + vpp("vender", "vendí", "vendiste", "vendió", "vendimos", "vendisteis", "vendieron"),
)

# ---------------------------------------------------------------------------- 178
L178 = lesson(
    "A vegetarian diet and healthy advice",
    "No como carne. No la como. Hay que caminar más.",
    requires=["carne", "pescado", "dejar", "seguir", "sustituir", "proteína", "fumar", "caminar", "estrés", "fruta", "sal"],
    cards=[
        card("Talking about a diet",
             "Seguir una dieta means to follow a diet. Dejar de + infinitive means to stop doing something: Sara dejó "
             "de comer carne el año pasado. Replacing the noun with a pronoun keeps the talk short: ¿Por qué no comes "
             "carne? No la como. You can sustituir la carne por proteína vegetal → Puedes sustituirla por proteína "
             "vegetal.",
             examples=[
                 ex("Mi amiga Sara sigue una dieta vegetariana.", "My friend Sara follows a vegetarian diet.", "sigue"),
                 ex("Dejó de comer carne el año pasado.", "She stopped eating meat last year.", "Dejó de comer"),
                 ex("¿Por qué no comes carne? No la como.", "Why don’t you eat meat? I don’t eat it.", "la"),
                 ex("Puedes sustituirla por frijoles.", "You can substitute it with beans.", "sustituirla"),
             ]),
        card("Health advice with the infinitive",
             "Posters and magazines give general advice with the bare infinitive. Hay que + infinitive also works.",
             tables=[table(["Consejo", "English"],
                           [["No comer mucha sal.", "Don’t eat a lot of salt."],
                            ["Comer fruta todos los días.", "Eat fruit every day."],
                            ["Caminar más.", "Walk more."],
                            ["Disminuir el estrés.", "Reduce stress."],
                            ["No fumar.", "Don’t smoke."]],
                           say=[0])]),
    ],
    exercises=[
        F("Sara no come carne. Ella no ___ come porque sigue una dieta vegetariana.", "la", ["lo", "los", "las"], "Carne is feminine singular.", tr="Sara doesn’t eat meat. She doesn’t eat it because she follows a vegetarian diet."),
        F("Sara dejó de ___ pescado el año pasado.", "comer", ["come", "comió", "comiendo"], "Dejar de + infinitive.", tr="Sara stopped eating fish last year."),
        F("Puedes sustituir la carne. Puedes ___ por frijoles.", "sustituirla", ["sustituirlo", "sustituirlas", "sustituirlos"], "Carne → -la, attached to the infinitive.", tr="You can substitute meat. You can substitute it with beans."),
        F("Para estar sano, hay que ___ más.", "caminar", ["camina", "caminó", "caminando"], "Hay que + infinitive.", tr="To be healthy, you have to walk more."),
        F("Mi amigo no come sal. Él no ___ come nunca.", "la", ["lo", "los", "las"], "Sal is feminine singular.", tr="My friend doesn’t eat salt. He never eats it."),
        M("What does “No fumar” mean as general advice?", "Don’t smoke.", ["I smoke.", "He smokes.", "We will smoke."], "A bare infinitive with no."),
        M("What does “dejar de comer carne” mean?", "to stop eating meat", ["to eat more meat", "to cook meat", "to like meat"], "Dejar de + infinitive = stop doing."),
        M("How do you say “I don’t eat it” (la carne)?", "No la como.", ["No lo como.", "La no como.", "No como la."], "No + pronoun + verb."),
        M("What does “Disminuir el estrés” mean?", "Reduce stress.", ["Increase stress.", "Avoid exercise.", "Eat more."], "Disminuir = to reduce."),
    ],
)

# ---------------------------------------------------------------------------- 179
L179 = lesson(
    "Review: food, the preterite and object pronouns",
    "Comí, fuimos, la pagué, lo compré",
    requires=["comer", "hablar", "ir", "ser", "cocinar", "nacer", "comprar", "nada", "mucho"],
    cards=[
        card("The preterite",
             "Regular -ar verbs end in -é, -aste, -ó, -amos, -asteis, -aron. Regular -er and -ir verbs end in -í, -iste, "
             "-ió, -imos, -isteis, -ieron. Ser and ir share one set of forms.",
             tables=[table(["", "hablar", "comer", "ser · ir"],
                           [["yo", "habl{é}", "com{í}", "fui"],
                            ["tú", "habl{aste}", "com{iste}", "fuiste"],
                            ["él · ella · usted", "habl{ó}", "com{ió}", "fue"],
                            ["nosotros", "habl{amos}", "com{imos}", "fuimos"],
                            ["vosotros", "habl{asteis}", "com{isteis}", "fuisteis"],
                            ["ellos · ellas · ustedes", "habl{aron}", "com{ieron}", "fueron"]],
                           say=[1, 2, 3])]),
        card("Objects",
             "Replace the direct object with lo, la, los, las (or me, te, nos) and put it before the verb, or attach it "
             "to the infinitive. Use the personal a before a specific person. Remember algo and nada, and mucho and "
             "poco.",
             examples=[
                 ex("Ayer compré el pescado. Lo compré en el mercado.", "Yesterday I bought the fish. I bought it at the market.", "Lo compré"),
                 ex("Llamamos al camarero y pedimos la cuenta.", "We called the waiter and asked for the bill.", "al camarero"),
                 ex("No quiero nada más, gracias.", "I don’t want anything else, thank you.", "nada"),
                 ex("Voy a prepararla esta noche.", "I am going to prepare it tonight.", "prepararla"),
             ]),
    ],
    exercises=[
        F("Ayer yo ___ en un restaurante peruano.", "comí", ["como", "comió", "comeré"], "Ayer → preterite; yo → comí.", tr="Yesterday I ate at a Peruvian restaurant.", lemma="comer:yo:pret"),
        F("Anoche mis padres ___ la cena.", "cocinaron", ["cocinan", "cocinó", "cocinamos"], "Mis padres → ellos: cocinaron.", tr="Last night my parents cooked dinner.", lemma="cocinar:ellos:pret"),
        F("El año pasado nosotros ___ a Quito.", "fuimos", ["fueron", "fui", "vamos"], "Nosotros → fuimos.", tr="Last year we went to Quito.", lemma="ir:nosotros:pret"),
        F("Mi abuela ___ en un pueblo pequeño.", "nació", ["nace", "nacieron", "nací"], "Ella → nació.", tr="My grandmother was born in a small town.", lemma="nacer:ella:pret"),
        F("Compré el pescado. Yo ___ compré en el mercado.", "lo", ["la", "los", "las"], "Pescado is masculine singular.", tr="I bought the fish. I bought it at the market."),
        F("Llamamos ___ camarero.", "al", ["a", "el", "del"], "A + el = al.", tr="We called the waiter."),
        F("No hay ___ en el refrigerador.", "nada", ["algo", "siempre", "tampoco"], "No hay nada = there is nothing.", tr="There is nothing in the refrigerator."),
        F("Hay ___ sal en la sopa; no la quiero.", "mucha", ["mucho", "muchos", "muchas"], "Sal is feminine singular.", tr="There is a lot of salt in the soup; I don’t want it."),
        M("Which sentence is correct?", "Voy a comprarla.", ["Voy a la comprar.", "Voy a lo comprarla.", "Voy comprarla a."], "Attach la to the infinitive."),
        M("What does “Ellos las prepararon” mean?", "They prepared them.", ["They prepare it.", "She prepared them.", "They prepared him."], "Las = them (feminine plural)."),
        M("What is the ellos preterite of “escribir”?", "escribieron", ["escriben", "escribirán", "escribió"], "Escrib- + ieron."),
        M("Which sentence would a waiter say?", "¿Qué desea tomar?", ["La cuenta, por favor.", "Para mí, el pollo.", "Una mesa para dos."], "The waiter asks what you would like."),
    ],
    verify=vpp("hablar", "hablé", "hablaste", "habló", "hablamos", "hablasteis", "hablaron")
           + vpp("comer", "comí", "comiste", "comió", "comimos", "comisteis", "comieron")
           + vpp("escribir", "escribí", "escribiste", "escribió", "escribimos", "escribisteis", "escribieron"),
)
UNIT = unit("La comida y la salud", [L155, L156, L157, L158, L159, L160, L161, L162, L163, L164, L165, L166, L167, L168, L169, L170, L171, L172, L173, L174, L175, L176, L177, L178, L179])

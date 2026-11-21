"""Spanish reading and listening, units 1 and 2 (levels 1 and 2).
Reading passages are written texts; listening passages are spoken ones. They
share no sentences."""

PASSAGES = [
    dict(
        id='es_r001', pair='es_02', level=1, kind='dialogue', mode='listen',
        title='What is your name?', es_title='¿Cómo te llamas?',
        names=['Ana', 'Luis'],
        lines=[
            ('Ana', '¡Hola! ¿Cómo te llamas?', 'Hi! What is your name?'),
            ('Luis', 'Me llamo Luis. ¿Y tú?', 'My name is Luis. And you?'),
            ('Ana', 'Me llamo Ana. Mucho gusto.', 'My name is Ana. Nice to meet you.'),
            ('Luis', 'Mucho gusto, Ana. ¿De dónde eres?', 'Nice to meet you, Ana. Where are you from?'),
            ('Ana', 'Soy de México. ¿Y tú?', 'I am from Mexico. And you?'),
            ('Luis', 'Soy de España.', 'I am from Spain.'),
        ],
        questions=[
            ('What is the girl’s name?', ['Ana', 'Luis', 'Marta', 'Sofía'], 0, '“Me llamo Ana.”'),
            ('Where is Ana from?', ['Spain', 'Mexico', 'Chile', 'Peru'], 1, '“Soy de México.”'),
            ('Where is Luis from?', ['Spain', 'Mexico', 'Cuba', 'Argentina'], 0, '“Soy de España.”'),
        ],
    ),
    dict(
        id='es_r002', pair='es_04', level=1, kind='dialogue', mode='listen',
        title='A phone number', es_title='Un número de teléfono',
        names=['Marta', 'Pablo'],
        lines=[
            ('Marta', 'Hola, Pablo. ¿Cuál es tu teléfono?', 'Hello, Pablo. What is your phone number?'),
            ('Pablo', 'Mi teléfono es el cinco, tres, uno, nueve, cero.', 'My number is five, three, one, nine, zero.'),
            ('Marta', 'Cinco, tres, uno, nueve, cero. Gracias.', 'Five, three, one, nine, zero. Thank you.'),
            ('Pablo', 'De nada. ¿Y tu teléfono?', 'You are welcome. And your number?'),
            ('Marta', 'Es el siete, cuatro, ocho, dos, seis.', 'It is seven, four, eight, two, six.'),
        ],
        questions=[
            ('What is Pablo’s number?', ['53190', '53910', '35190', '51390'], 0, '“Cinco, tres, uno, nueve, cero.”'),
            ('How does Marta’s number end?', ['six', 'two', 'eight', 'four'], 0, '“Siete, cuatro, ocho, dos, seis.”'),
            ('What does Marta say after Pablo gives his number?', ['Thank you', 'Sorry', 'Goodbye', 'Please'], 0, '“Gracias.”'),
        ],
    ),
    dict(
        id='es_r003', pair='es_08', level=1, kind='text', mode='read',
        title='My classroom', es_title='Mi clase',
        lines=[
            (None, 'Esta es mi clase.', 'This is my classroom.'),
            (None, 'Hay una mesa grande y cuatro sillas.', 'There is a big table and four chairs.'),
            (None, 'En la mesa hay un libro y un lápiz.', 'On the table there is a book and a pencil.'),
            (None, 'Hay un reloj en la pared.', 'There is a clock on the wall.'),
            (None, 'La clase es muy bonita.', 'The classroom is very pretty.'),
        ],
        extra={'pared': 'wall', 'lápiz': 'pencil'},
        questions=[
            ('What is on the table?', ['A book and a pencil', 'A clock', 'A bag', 'A computer'], 0, '“Un libro y un lápiz.”'),
            ('How many chairs are there?', ['Two', 'Three', 'Four', 'Five'], 2, '“Cuatro sillas.”'),
            ('Where is the clock?', ['On the wall', 'On the table', 'On a chair', 'In a bag'], 0, '“Un reloj en la pared.”'),
        ],
    ),
    dict(
        id='es_r004', pair='es_06', level=1, kind='text', mode='read',
        title='Sofía’s country', es_title='El país de Sofía',
        names=['Santiago', 'Chile', 'Perú', 'Sofía', 'Pedro'],
        lines=[
            (None, 'Me llamo Sofía y soy de Chile.', 'My name is Sofía and I am from Chile.'),
            (None, 'Santiago es la capital de Chile.', 'Santiago is the capital of Chile.'),
            (None, 'Chile está en el sur de América.', 'Chile is in the south of America.'),
            (None, 'Mi amigo Pedro es de Perú.', 'My friend Pedro is from Peru.'),
            (None, 'Perú está al norte de Chile.', 'Peru is to the north of Chile.'),
        ],
        questions=[
            ('Where is Sofía from?', ['Chile', 'Peru', 'Spain', 'Mexico'], 0, '“Soy de Chile.”'),
            ('What is the capital of Chile?', ['Lima', 'Santiago', 'Madrid', 'Quito'], 1, '“Santiago es la capital.”'),
            ('Who is from Peru?', ['Pedro', 'Sofía', 'Santiago', 'Nobody'], 0, '“Mi amigo Pedro es de Perú.”'),
            ('Where is Peru, compared with Chile?', ['To the north', 'To the south', 'To the east', 'In the same place'], 0, '“Al norte de Chile.”'),
        ],
    ),
    dict(
        id='es_r005', pair='es_17', level=2, kind='text', mode='read',
        title='My friend Carla', es_title='Mi amiga Carla',
        names=['Carla', 'Colombia', 'Madrid', 'Pepe'],
        lines=[
            (None, 'Mi amiga se llama Carla. Es de Colombia, pero ahora está en Madrid.', 'My friend is called Carla. She is from Colombia, but now she is in Madrid.'),
            (None, 'Carla es estudiante y también es cantante.', 'Carla is a student and she is also a singer.'),
            (None, 'Tiene un gato negro. El gato se llama Pepe.', 'She has a black cat. The cat is called Pepe.'),
            (None, 'Carla y yo somos amigas, pero somos muy diferentes.', 'Carla and I are friends, but we are very different.'),
            (None, 'Ella es de la ciudad y yo soy del campo.', 'She is from the city and I am from the countryside.'),
        ],
        questions=[
            ('Where is Carla from?', ['Colombia', 'Madrid', 'Chile', 'Cuba'], 0, '“Es de Colombia.”'),
            ('Where is she now?', ['In Madrid', 'In Bogotá', 'In the countryside', 'At home'], 0, '“Ahora está en Madrid.”'),
            ('What does she do besides study?', ['She is a singer', 'She is a doctor', 'She is a teacher', 'She is a cook'], 0, '“También es cantante.”'),
            ('What is the cat called?', ['Pepe', 'Rex', 'Negro', 'Carla'], 0, '“El gato se llama Pepe.”'),
        ],
    ),
    dict(
        id='es_r006', pair='es_22', level=2, kind='text', mode='read',
        title='I have a dog', es_title='Tengo un perro',
        names=['Rex'],
        lines=[
            (None, 'Tengo un perro y dos gatos.', 'I have a dog and two cats.'),
            (None, 'El perro se llama Rex. Es grande y muy simpático.', 'The dog is called Rex. He is big and very friendly.'),
            (None, 'Los gatos son pequeños y no tienen nombre todavía.', 'The cats are small and they do not have a name yet.'),
            (None, 'Mi amiga no tiene perro. Tiene un pez.', 'My friend does not have a dog. She has a fish.'),
            (None, 'El pez es rojo y no es muy grande.', 'The fish is red and is not very big.'),
        ],
        extra={'pez': 'fish'},
        questions=[
            ('How many cats does the writer have?', ['One', 'Two', 'Three', 'None'], 1, '“Un perro y dos gatos.”'),
            ('What is the dog like?', ['Big and friendly', 'Small and shy', 'Old and tired', 'Red and quiet'], 0, '“Es grande y muy simpático.”'),
            ('What pet does the friend have?', ['A fish', 'A cat', 'A dog', 'A bird'], 0, '“Tiene un pez.”'),
        ],
    ),
    dict(
        id='es_r007', pair='es_19', level=2, kind='dialogue', mode='listen',
        title='Where are you?', es_title='¿Dónde estás?',
        names=['Tomás', 'Ana'],
        lines=[
            ('Mamá', 'Hola, Tomás. ¿Dónde estás?', 'Hello, Tomás. Where are you?'),
            ('Tomás', 'Estoy en la biblioteca con Ana.', 'I am in the library with Ana.'),
            ('Mamá', '¿Y cómo estás? ¿Estás bien?', 'And how are you? Are you well?'),
            ('Tomás', 'Sí, estoy muy bien. Ana está aquí también.', 'Yes, I am very well. Ana is here too.'),
            ('Mamá', 'Bien. La cena está en la mesa a las siete.', 'Good. Dinner is on the table at seven.'),
            ('Tomás', 'Gracias, mamá. Hasta luego.', 'Thanks, Mum. See you later.'),
        ],
        questions=[
            ('Where is Tomás?', ['In the library', 'At home', 'At school', 'In a café'], 0, '“Estoy en la biblioteca.”'),
            ('Who is with him?', ['Ana', 'His father', 'A teacher', 'Nobody'], 0, '“Con Ana.”'),
            ('How does he feel?', ['Very well', 'Tired', 'Sad', 'Ill'], 0, '“Estoy muy bien.”'),
            ('Where is dinner?', ['On the table', 'In the car', 'In the library', 'In the oven'], 0, '“La cena está en la mesa.”'),
        ],
    ),
    dict(
        id='es_r008', pair='es_24', level=2, kind='dialogue', mode='listen',
        title='At the school office', es_title='En la oficina de la escuela',
        names=['Jorge', 'Ruiz', 'Lucía', 'Díaz'],
        lines=[
            ('Secretaria', 'Buenos días. ¿Cómo se llama usted?', 'Good morning. What is your name?'),
            ('Señor', 'Me llamo Jorge Ruiz. Mi hija es alumna aquí.', 'My name is Jorge Ruiz. My daughter is a pupil here.'),
            ('Secretaria', '¿Cómo se llama su hija?', 'What is your daughter called?'),
            ('Señor', 'Se llama Lucía. Está en la clase de la profesora Díaz.', 'She is called Lucía. She is in Professor Díaz’s class.'),
            ('Señor', '¿Dónde está la clase de la profesora Díaz?', 'Where is Professor Díaz’s class?'),
            ('Secretaria', 'Está en el segundo piso, al lado de la biblioteca.', 'It is on the second floor, next to the library.'),
            ('Señor', '¿Cuándo es la reunión?', 'When is the meeting?'),
            ('Secretaria', 'La reunión es el lunes a las cinco.', 'The meeting is on Monday at five.'),
        ],
        extra={'reunión': 'meeting'},
        hints={'alumna': 'alumno'},
        questions=[
            ('What is the father’s name?', ['Jorge Ruiz', 'Luis Díaz', 'Pablo Ruiz', 'Jorge Díaz'], 0, '“Me llamo Jorge Ruiz.”'),
            ('Who is Lucía’s teacher?', ['Professor Díaz', 'Professor Ruiz', 'The secretary', 'Nobody'], 0, '“La profesora Díaz.”'),
            ('Where is the class?', ['Second floor, next to the library', 'First floor', 'In the gym', 'Outside'], 0, '“Segundo piso, al lado de la biblioteca.”'),
            ('When is the meeting?', ['Monday at five', 'Tuesday at four', 'Monday at nine', 'Friday at five'], 0, '“El lunes a las cinco.”'),
        ],
    ),
]

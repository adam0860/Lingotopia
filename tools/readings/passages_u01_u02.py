"""Passages paired with the lessons of units 1 and 2 (level 1: a few short
sentences with only the words and grammar of the first twelve lessons).

Format of one passage:

    dict(
        id='ru_r01',            # unique, ru_r + number
        pair='ru_01',           # the grammar lesson it goes with
        level=1,                # 1 (a few words) to 6 (a news article)
        kind='text',            # or 'dialogue'
        title='...',            # English title
        ru_title='...',         # Russian title
        lines=[(who, russian, english), ...],   # one sentence or turn each
        questions=[(question, [4 options], index_of_answer, why), ...],
        names=[...],            # proper names (not looked up in the deck)
        hints={...},            # surface form -> lemma where pymorphy3 guesses wrong
        extra={...},            # lemma -> gloss for words the deck lacks
    )

Write the Russian without stress marks. `who` is None for narration or a
speaker's name for a dialogue turn.
"""

PASSAGES = [
    dict(
        id='ru_r01', pair='ru_01', level=1, kind='text',
        title='This is Anna', ru_title='Это Анна',
        names=['Анна', 'Том'],
        lines=[
            (None, 'Это Анна.', 'This is Anna.'),
            (None, 'Она врач.', 'She is a doctor.'),
            (None, 'Это Том.', 'This is Tom.'),
            (None, 'Он студент.', 'He is a student.'),
            (None, 'Это дом.', 'This is a house.'),
        ],
        questions=[
            ('Who is a doctor?', ['Anna', 'Tom', 'Both of them', 'Neither of them'], 0,
             '“Она врач” – she is a doctor, and Anna is the woman.'),
            ('What is Tom?', ['A doctor', 'A student', 'A house', 'A teacher'], 1,
             '“Он студент” – he is a student.'),
            ('What else is mentioned?', ['A book', 'A window', 'A house', 'A table'], 2,
             'The last sentence is “Это дом”: this is a house.'),
        ],
    ),
    dict(
        id='ru_r02', pair='ru_02', level=1, kind='dialogue',
        title='What is this?', ru_title='Что это?',
        names=['Анна', 'Том'],
        lines=[
            ('Анна', 'Это дом?', 'Is this a house?'),
            ('Том', 'Да, это дом.', 'Yes, this is a house.'),
            ('Анна', 'Что это?', 'What is this?'),
            ('Том', 'Это окно.', 'This is a window.'),
            ('Анна', 'А там?', 'And over there?'),
            ('Том', 'Там книга.', 'There is a book there.'),
        ],
        questions=[
            ('What does Anna ask about first?', ['A window', 'A house', 'A book', 'A doctor'], 1,
             'Her first question is “Это дом?” – is this a house?'),
            ('Where is the book?', ['At home', 'Here', 'On the table', 'Over there'], 3,
             '“Там книга”: там means “there”.'),
            ('How does Tom answer the first question?', ['Yes', 'No', 'He does not answer', 'He asks a question'], 0,
             '“Да, это дом.” – yes, this is a house.'),
        ],
    ),
    dict(
        id='ru_r03', pair='ru_03', level=1, kind='text',
        title='Tom and Lisa', ru_title='Том и Лиза',
        names=['Том', 'Лиза'],
        lines=[
            (None, 'Это Том и Лиза.', 'This is Tom and Lisa.'),
            (None, 'Том студент, а Лиза врач.', 'Tom is a student, and Lisa is a doctor.'),
            (None, 'Том здесь, а Лиза там.', 'Tom is here, and Lisa is over there.'),
            (None, 'Здесь стол и стул.', 'Here are a table and a chair.'),
        ],
        questions=[
            ('Who is a student?', ['Lisa', 'Both of them', 'Tom', 'Nobody'], 2,
             '“Том студент” – Tom is the student; Lisa is the doctor.'),
            ('Where is Lisa?', ['Here', 'There', 'At home', 'At school'], 1,
             '“Лиза там” – Lisa is over there.'),
            ('What is here?', ['A table and a chair', 'A house and a window', 'A book and a pen', 'A student and a doctor'], 0,
             '“Здесь стол и стул” – a table and a chair.'),
        ],
    ),
    dict(
        id='ru_r04', pair='ru_04', level=1, kind='text',
        title='Who and what', ru_title='Кто и что',
        lines=[
            (None, 'Это папа, а это мама.', 'This is dad, and this is mom.'),
            (None, 'Это учитель, а это писатель.', 'This is a teacher, and this is a writer.'),
            (None, 'Это школа, а это музей.', 'This is a school, and this is a museum.'),
        ],
        questions=[
            ('Which two buildings are mentioned?',
             ['A house and a school', 'A school and a museum', 'A museum and a window', 'A house and a museum'], 1,
             '“Это школа, а это музей”: a school and a museum.'),
            ('Which family members are mentioned?',
             ['Brother and sister', 'Mom and grandfather', 'Dad and uncle', 'Mom and dad'], 3,
             '“Это папа, а это мама”: dad and mom.'),
            ('Which jobs are mentioned?',
             ['Doctor and student', 'Teacher and doctor', 'Writer and student', 'Teacher and writer'], 3,
             '“учитель” is a teacher and “писатель” is a writer.'),
        ],
    ),
    dict(
        id='ru_r05', pair='ru_05', level=1, kind='text',
        title='Here and there', ru_title='Здесь и там',
        lines=[
            (None, 'Вот окно.', 'Here is a window.'),
            (None, 'Оно там.', 'It is over there.'),
            (None, 'Это книга.', 'This is a book.'),
            (None, 'Она здесь.', 'It is here.'),
            (None, 'Это брат.', 'This is my brother.'),
            (None, 'Он студент.', 'He is a student.'),
        ],
        questions=[
            ('Where is the window?', ['Here', 'Over there', 'At school', 'It is not mentioned'], 1,
             '“Окно” is neuter, so it is “оно там”: it is over there.'),
            ('Where is the book?', ['Over there', 'It is not mentioned', 'On the table', 'Here'], 3,
             '“Книга” is feminine, so it is “она здесь”: it is here.'),
            ('Who is a student?', ['The brother', 'The sister', 'Dad', 'The teacher'], 0,
             '“Он студент” comes right after “Это брат”.'),
        ],
    ),
    dict(
        id='ru_r06', pair='ru_06', level=1, kind='dialogue',
        title='My family', ru_title='Моя семья',
        names=['Анна', 'Том'],
        lines=[
            ('Анна', 'Это мой брат.', 'This is my brother.'),
            ('Том', 'А это твоя сестра?', 'And is this your sister?'),
            ('Анна', 'Да, это моя сестра.', 'Yes, this is my sister.'),
            ('Анна', 'А это наш дом.', 'And this is our house.'),
        ],
        questions=[
            ('Who does Anna introduce first?', ['Her sister', 'Her brother', 'Her mother', 'Her teacher'], 1,
             '“Это мой брат” – this is my brother.'),
            ('What does Anna call the house?',
             ['My house', 'Your house', 'His house', 'Our house'], 3,
             '“Наш дом” – our house.'),
            ('Whose sister is it?', ['Tom’s', 'Anna’s', 'Anna and Tom’s', 'Nobody’s'], 1,
             'Anna says “моя сестра” – my sister.'),
        ],
    ),
    dict(
        id='ru_r07', pair='ru_07', level=1, kind='dialogue',
        title='Not a table', ru_title='Это не стол',
        names=['Анна', 'Том'],
        lines=[
            ('Анна', 'Это стол?', 'Is this a table?'),
            ('Том', 'Нет, это не стол.', 'No, this is not a table.'),
            ('Том', 'Это стул.', 'This is a chair.'),
            ('Анна', 'А там?', 'And over there?'),
            ('Том', 'Там окно.', 'There is a window there.'),
        ],
        questions=[
            ('What is it that Anna asks about?', ['A chair', 'A window', 'A table', 'A house'], 2,
             'She asks “Это стол?” – is this a table?'),
            ('What is it really?', ['A chair', 'A window', 'A table', 'A book'], 0,
             '“Нет, это не стол. Это стул.” – it is a chair.'),
            ('What is over there?', ['A table', 'A chair', 'A book', 'A window'], 3,
             '“Там окно.”'),
        ],
    ),
    dict(
        id='ru_r08', pair='ru_08', level=1, kind='text',
        title='Houses and schools', ru_title='Дома и школы',
        hints={'дома': {'lemma': 'дом', 'note': 'nominative plural'}},
        lines=[
            (None, 'Это дома.', 'These are houses.'),
            (None, 'Это школы.', 'These are schools.'),
            (None, 'Там студенты и врачи.', 'Students and doctors are over there.'),
            (None, 'Здесь книги и ручки.', 'Here are books and pens.'),
        ],
        questions=[
            ('Who is over there?', ['Teachers and writers', 'Students and doctors', 'Brothers and sisters', 'Mom and dad'], 1,
             '“Там студенты и врачи.”'),
            ('What is here?', ['Windows and tables', 'Houses and schools', 'Books and pens', 'Chairs and books'], 2,
             '“Здесь книги и ручки.”'),
            ('What are “дома”?', ['One house', 'Several houses', 'A school', 'A window'], 1,
             '“Дома” is the irregular plural of дом (house).'),
        ],
    ),
    dict(
        id='ru_r09', pair='ru_09', level=1, kind='dialogue',
        title='Whose books?', ru_title='Чьи это книги?',
        names=['Анна', 'Том'],
        lines=[
            ('Анна', 'Чьи это книги?', 'Whose books are these?'),
            ('Том', 'Это мои книги.', 'These are my books.'),
            ('Анна', 'А чьи это ручки?', 'And whose pens are these?'),
            ('Том', 'Это ваши ручки.', 'These are your pens.'),
            ('Анна', 'Нет, это наши ручки!', 'No, these are our pens!'),
        ],
        questions=[
            ('Whose books are they?', ['Anna’s', 'Tom’s', 'The teacher’s', 'Nobody’s'], 1,
             'Tom says “Это мои книги” – these are my books.'),
            ('Who has pens that belong to Tom and Anna together?', ['Nobody', 'Anna alone', 'Tom alone', 'Both of them'], 3,
             'Anna says “наши ручки” – our pens.'),
            ('What does Anna do when Tom says “ваши ручки”?', ['She agrees', 'She says no', 'She asks about books', 'She leaves'], 1,
             'She answers “Нет, это наши ручки!”'),
        ],
    ),
    dict(
        id='ru_r10', pair='ru_10', level=1, kind='text',
        title='How many?', ru_title='Сколько?',
        lines=[
            (None, 'Здесь один стол и два стула.', 'Here is one table and two chairs.'),
            (None, 'Там три окна.', 'There are three windows over there.'),
            (None, 'Это номер четыре.', 'This is number four.'),
            (None, 'А это номер пять.', 'And this is number five.'),
        ],
        questions=[
            ('How many chairs are here?', ['One', 'Two', 'Three', 'Four'], 1,
             '“Два стула” – two chairs.'),
            ('How many windows are over there?', ['Five', 'Two', 'One', 'Three'], 3,
             '“Три окна” – three windows.'),
            ('Which number is “А это”?', ['Five', 'Four', 'Three', 'Two'], 0,
             '“А это номер пять” – and this is number five.'),
        ],
    ),
    dict(
        id='ru_r11', pair='ru_11', level=1, kind='dialogue',
        title='My glasses', ru_title='Где мои очки?',
        names=['Анна', 'Том'],
        lines=[
            ('Том', 'Где мои очки?', 'Where are my glasses?'),
            ('Анна', 'Вот твои очки.', 'Here are your glasses.'),
            ('Том', 'А где мои друзья?', 'And where are my friends?'),
            ('Анна', 'Там твои друзья и братья.', 'Your friends and brothers are over there.'),
        ],
        questions=[
            ('What is Tom looking for first?', ['His friends', 'His brothers', 'His glasses', 'His books'], 2,
             '“Где мои очки?” – where are my glasses?'),
            ('Where are Tom’s friends?', ['Here', 'He does not ask', 'At home', 'Over there'], 3,
             'Anna says “Там твои друзья и братья” – they are over there.'),
            ('Who else is over there?', ['Tom’s brothers', 'Tom’s glasses', 'Anna’s sister', 'Nobody'], 0,
             '“Братья” is the irregular plural of брат (brother).'),
        ],
    ),
    dict(
        id='ru_r12', pair='ru_12', level=1, kind='text',
        title='Formal introductions', ru_title='Николай Иванович и Мария Павловна',
        names=['Николай', 'Иванович', 'Мария', 'Павловна'],
        lines=[
            (None, 'Это Николай Иванович.', 'This is Nikolai Ivanovich.'),
            (None, 'Он учитель.', 'He is a teacher.'),
            (None, 'Это Мария Павловна.', 'This is Maria Pavlovna.'),
            (None, 'Она врач.', 'She is a doctor.'),
            (None, 'Здравствуйте, Мария Павловна!', 'Hello, Maria Pavlovna!'),
        ],
        questions=[
            ('What is Nikolai Ivanovich?', ['A doctor', 'A student', 'A teacher', 'A writer'], 2,
             '“Он учитель.”'),
            ('Who is the doctor?', ['Maria Pavlovna', 'Nikolai Ivanovich', 'Both of them', 'Neither'], 0,
             '“Это Мария Павловна. Она врач.”'),
            ('What was Maria’s father called?', ['Ivan', 'Nikolai', 'Pavel', 'Maria'], 2,
             'The patronymic Павловна means “daughter of Pavel”.'),
        ],
    ),
]

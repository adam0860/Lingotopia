"""Unit 4: greetings and introductions, part 1 (lessons 27-36): meeting people, word order, 什么, 吗, 不, 呢,
谁, 这/那, people words, pronouns and 的. Original text; the scope follows DLIFLC Chinese Basic Program
Unit 1 Lesson 2 (Greetings and Introductions), Presentations 1 and 2."""
from dsl_zh import *


# ---------------------------------------------------------------------------- 27
L27 = lesson(
    "Nice to meet you",
    "您好, 请问, 认识, 高兴, 也",
    requires=[],
    cards=[
        card("Meeting someone politely",
             "When you meet a person for the first time you greet them, perhaps ask a question politely, and say you are glad to meet them. "
             "您 is the polite “you”. 请问 is “may I ask”, and it comes before a question. 认识 means to know a person, so 认识你 is “to know you”, "
             "and 高兴 means happy. 很 means “very” and comes before 高兴. 也 means “also” and goes right before the verb or adjective.",
             tables=[wtable([("您好", "nin2 hao3", "hello (polite)"), ("请问", "qing3wen4", "may I ask…"), ("认识", "ren4shi5", "to know (a person)"),
                             ("高兴", "gao1xing4", "happy, glad"), ("很", "hen3", "very"), ("也", "ye3", "also, too"),
                             ("很高兴认识你", "hen3 gao1xing4 ren4shi5 ni3", "nice to meet you")])]),
        card("A first meeting",
             "Here is how a short first meeting goes. The second speaker echoes the first and adds 也.",
             examples=[ex("您好！", "nin2 hao3", "Hello! (polite)"),
                       ex("你好！很高兴认识你。", "ni3 hao3! hen3 gao1xing4 ren4shi5 ni3", "Hello! Nice to meet you."),
                       ex("我也很高兴认识您。", "wo3 ye3 hen3 gao1xing4 ren4shi5 nin2", "I am glad to meet you too.", hl="也"),
                       ex("请问，您是王老师吗？", "qing3wen4, nin2 shi4 Wang2 lao3shi1 ma5", "Excuse me, are you Teacher Wang?")]),
    ],
    exercises=[
        mean("认识", "ren4shi5", "to know (a person)", ["to ask", "to be called", "to say goodbye"]),
        mean("高兴", "gao1xing4", "happy, glad", ["very", "also", "polite"]),
        mean("很", "hen3", "very", ["also", "not", "polite"]),
        mean("也", "ye3", "also, too", ["very", "not", "what"]),
        mean("请问", "qing3wen4", "may I ask…", ["nice to meet you", "thank you", "goodbye"]),
        mean("很高兴认识你", "hen3 gao1xing4 ren4shi5 ni3", "nice to meet you", ["good morning", "thank you", "see you tomorrow"]),
        rd("认识", "ren4shi5", ["ren2shi5", "ren4shi1", "ren3shi5"]),
        rd("高兴", "gao1xing4", ["gao1xing1", "gao2xing4", "gao1xing3"]),
        M("The other person says 很高兴认识你. A good reply is…", "我也很高兴认识你。", ["我也很认识你。", "我姓很高兴。", "不客气。"], "Echo the sentence and add 也: 我也很高兴认识你."),
        M("Which greeting is polite, for someone older or senior?", "您好", ["你们好", "他好", "你好"], "您 is the polite “you”."),
        F("很高兴___你。", "认识", ["姓", "叫", "是"], "认识 means to know a person: 很高兴认识你.", tr="Nice to meet you."),
        F("我___很高兴认识你。", "也", ["吗", "呢", "们"], "也 means “also”: 我也很高兴认识你, I am glad to meet you too.", tr="I am glad to meet you too."),
        F("请问，您___王老师吗？", "是", ["姓", "也", "很"], "是 links 您 with 王老师.", tr="Excuse me, are you Teacher Wang?"),
        M("Where does 也 go in a sentence?", "Right before the verb or adjective", ["At the end", "At the very start", "After the object"], "也 comes before what it describes: 我也很高兴."),
    ],
)

# ---------------------------------------------------------------------------- 28
L28 = lesson(
    "Word order and 什么",
    "我姓李 · 你姓什么？",
    requires=[],
    cards=[
        card("Same order for statements and questions",
             "A basic Chinese sentence is Subject + Verb + Object, or Subject + Adjective. A question keeps the very same order. "
             "Where English moves words around (“You are called… / What are you called?”), Chinese simply puts the question word in the place where the answer will go. "
             "什么 means “what”, so 你姓什么 asks “you are surnamed what?”",
             tables=[table(["Subject", "Verb", "Object"],
                           [["我", "姓", "李"], ["你", "姓", "什么"], ["他", "是", "老师"], ["他", "叫", "王明"], ["你", "叫", "什么名字"]],
                           title="Subject + Verb + Object", say=[0, 1, 2])]),
        card("Question and answer share a shape",
             "Compare each question with its answer: only the last part changes.",
             examples=[ex("你姓什么？", "ni3 xing4 shen2me5", "What is your surname?", hl="什么"),
                       ex("我姓李。", "wo3 xing4 Li3", "My surname is Li.", hl="李"),
                       ex("你叫什么名字？", "ni3 jiao4 shen2me5 ming2zi5", "What is your name?", hl="什么"),
                       ex("我叫李明。", "wo3 jiao4 Li3 Ming2", "My name is Li Ming.", hl="李明"),
                       ex("王老师叫什么名字？", "Wang2 lao3shi1 jiao4 shen2me5 ming2zi5", "What is Teacher Wang's name?")]),
    ],
    exercises=[
        M("In a Chinese question, where does 什么 go?", "Where the answer would go", ["At the start of the sentence", "Before the subject", "It replaces the verb"], "什么 takes the place of the answer."),
        M("Does the word order change when a statement becomes a question with 什么?", "No", ["Yes: the verb moves to the front", "Yes: 什么 moves to the front", "Yes: the subject moves to the end"], "The order stays the same: 你姓李 becomes 你姓什么."),
        M("How do you ask “What is your name?”", "你叫什么名字？", ["什么你叫名字？", "你什么叫名字？", "什么名字你叫？"], "Subject + verb + 什么名字."),
        M("In 我姓李, which word is the verb?", "姓", ["我", "李", "There is no verb"], "姓 is the verb: I am surnamed Li."),
        M("In 他是老师, which word is the object?", "老师", ["他", "是", "什么"], "老师 comes after the verb 是, so it is the object."),
        M("Which answers 你姓什么？", "我姓张。", ["我是张。", "你好。", "张姓我。"], "Answer with the same shape: 我姓张."),
        M("Which answers 你叫什么名字？", "我叫赵林。", ["我姓叫赵林。", "再见。", "不客气。"], "我叫 + name."),
        F("你姓___？", "什么", ["吗", "呢", "们"], "什么 asks for the surname.", tr="What is your surname?"),
        F("王老师叫___名字？", "什么", ["吗", "谁", "们"], "你叫什么名字 and 王老师叫什么名字 use the same pattern.", tr="What is Teacher Wang's name?"),
        F("我___李明。", "叫", ["姓", "吗", "们"], "叫 goes with the whole name: 我叫李明.", tr="My name is Li Ming."),
        F("他___老师。", "是", ["姓", "叫", "吗"], "是 links 他 and 老师.", tr="He is a teacher."),
        mean("什么", "shen2me5", "what", ["who", "also", "very"]),
        rd("什么", "shen2me5", ["shen4me5", "shen2me2", "shen2mo4"]),
        rd("姓", "xing4", ["xing1", "xing2", "xing3"], meaning="to have the surname"),
    ],
)

# ---------------------------------------------------------------------------- 29
L29 = lesson(
    "Yes/no questions with 吗",
    "你是学生吗？ 是。 不是。",
    requires=[],
    cards=[
        card("Add 吗 to the end",
             "To ask a yes/no question, take any statement and put 吗 on the end. Nothing else moves. "
             "吗 is a light particle: it is in the neutral tone, and it has no meaning of its own beyond making the sentence a question.",
             tables=[wtable([("你是学生。", "ni3 shi4 xue2sheng5", "You are a student."), ("你是学生吗？", "ni3 shi4 xue2sheng5 ma5", "Are you a student?"),
                             ("你姓王。", "ni3 xing4 Wang2", "Your surname is Wang."), ("你姓王吗？", "ni3 xing4 Wang2 ma5", "Is your surname Wang?")])]),
        card("Answering",
             "The answer is the verb of the question: 是 for “yes” and 不是 for “no”. With another verb, repeat that verb: 姓 or 不姓. "
             "You can also say 对, “right”, for yes. But for no you do not say 不对, which means “wrong”: you use 不是 or 不.",
             examples=[ex("你是老师吗？ 是。", "ni3 shi4 lao3shi1 ma5? shi4", "Are you a teacher? Yes."),
                       ex("你是海军吗？ 不是，我是陆军。", "ni3 shi4 hai3jun1 ma5? bu2shi4, wo3 shi4 lu4jun1", "Are you in the navy? No, I am in the army."),
                       ex("你姓王吗？ 姓。", "ni3 xing4 Wang2 ma5? xing4", "Is your surname Wang? Yes.")]),
    ],
    exercises=[
        M("How do you turn 你是学生 into a question?", "Add 吗 at the end", ["Add 什么 at the end", "Move 是 to the front", "Say 不 first"], "吗 goes on the end."),
        M("What does 你是海军吗？ ask?", "Are you in the navy?", ["Are you in the army?", "What service are you in?", "Is he in the navy?"], "是 + 海军 + 吗."),
        M("What does 他是老师吗？ ask?", "Is he a teacher?", ["Is he a student?", "Who is the teacher?", "Is she a teacher?"], "他 is he, and 吗 makes it a question."),
        M("The answer “no” to 你是老师吗？ is…", "不是", ["不对", "是", "吗"], "不 + 是 = 不是."),
        M("The answer “yes” to 你姓王吗？ is…", "姓", ["不姓", "吗", "什么"], "Repeat the verb of the question."),
        M("Which reply means “yes”?", "对", ["不对", "不客气", "什么"], "对 means right, so it can mean yes. 不对 means wrong."),
        M("Which question is formed correctly?", "你是空军吗？", ["吗你是空军？", "你吗是空军？", "你是吗空军？"], "吗 always comes last."),
        F("你是老师___？", "吗", ["呢", "什么", "们"], "吗 makes a yes/no question.", tr="Are you a teacher?"),
        F("你姓王___？", "吗", ["呢", "了", "的"], "吗 on the end.", tr="Is your surname Wang?"),
        F("他是陆军___？", "吗", ["呢", "也", "们"], "吗 on the end.", tr="Is he in the army?"),
        F("A: 你是学生吗？ B: ___，我是学生。", "是", ["不", "吗", "什么"], "是 answers yes.", tr="Yes, I am a student."),
        F("A: 你是海军吗？ B: ___，我是空军。", "不是", ["是", "吗", "也是"], "不是 answers no.", tr="No, I am in the air force."),
        rd("吗", "ma5", ["ma1", "ma4", "me5"]),
        M("Which word turns a statement into a question without changing the word order?", "吗", ["什么", "不", "也"], "吗 is added at the end."),
    ],
)

# ---------------------------------------------------------------------------- 30
L30 = lesson(
    "Saying no with 不",
    "不是, 不姓, 不好 · bù and bú",
    requires=[],
    cards=[
        card("不 goes before the verb or adjective",
             "不 means “not”. Put it in front of the verb or adjective it negates: 我是老师 becomes 我不是老师. "
             "There is no extra word for “do not” or “am not”, only 不.",
             examples=[ex("我不是老师。", "wo3 bu2shi4 lao3shi1", "I am not a teacher.", hl="不"),
                       ex("他不姓王。", "ta1 bu2 xing4 Wang2", "His surname is not Wang.", hl="不"),
                       ex("她不是陆军。", "ta1 bu2shi4 lu4jun1", "She is not in the army.", hl="不"),
                       ex("我不高兴。", "wo3 bu4 gao1xing4", "I am not happy.", hl="不")]),
        card("The tone of 不",
             "不 is bù (4th tone) by itself and before a 1st, 2nd or 3rd tone. Before a 4th tone it becomes bú (2nd tone), because two falling tones in a row are awkward. "
             "The pinyin is written with the changed tone, so 不是 is bú shì.",
             tables=[wtable([("不高兴", "bu4 gao1xing4", "not happy (1st tone follows)"), ("不行", "bu4 xing2", "no way, not OK (2nd)"),
                             ("不好", "bu4 hao3", "not good (3rd)"), ("不想", "bu4 xiang3", "do not want to (3rd)"),
                             ("不是", "bu2shi4", "is not (4th)"), ("不对", "bu2 dui4", "not right (4th)"),
                             ("不错", "bu2cuo4", "not bad (4th)"), ("不客气", "bu2 ke4qi5", "you are welcome (4th)")],
                            title="bù before tones 1, 2 and 3; bú before 4")]),
    ],
    exercises=[
        M("Where does 不 go?", "Right before the verb or adjective", ["At the end of the sentence", "Before the subject", "After the object"], "不 goes before what it negates."),
        M("How do you say “I am not a teacher”?", "我不是老师。", ["我是不老师。", "不我是老师。", "我不老师是。"], "Subject + 不 + verb + object."),
        M("What does 他不姓王 mean?", "His surname is not Wang.", ["His surname is Wang.", "He is not called Wang.", "Is his surname Wang?"], "不 negates 姓."),
        M("What does 她不是陆军 mean?", "She is not in the army.", ["She is in the army.", "He is not in the army.", "Is she in the army?"], "不是 negates 是."),
        M("How is 不 pronounced before a 4th tone?", "[[bu2]]", ["[[bu4]]", "[[bu1]]", "[[bu3]]"], "Before a 4th tone, 不 is bú, the 2nd tone."),
        M("How is 不 pronounced in 不好?", "[[bu4]]", ["[[bu2]]", "[[bu1]]", "[[bu3]]"], "好 is the 3rd tone, so 不 keeps the 4th tone."),
        rd("不是", "bu2shi4", ["bu4shi4", "bu1shi4", "bu2shi2"]),
        rd("不好", "bu4hao3", ["bu2hao3", "bu4hao4", "bu1hao3"]),
        rd("不客气", "bu2ke4qi5", ["bu4ke4qi5", "bu2ke4qi4", "bu1ke4qi5"]),
        rd("不高兴", "bu4gao1xing4", ["bu2gao1xing4", "bu4gao1xing1", "bu3gao1xing4"]),
        F("我___是老师。", "不", ["吗", "呢", "们"], "不 negates 是.", tr="I am not a teacher."),
        F("他___姓王。", "不", ["吗", "们", "什么"], "不 goes before 姓.", tr="His surname is not Wang."),
        F("你是学生吗？ 我___是学生。", "不", ["吗", "也", "呢"], "不 before the verb.", tr="I am not a student."),
        M("Which is the correct way to write the pinyin of 不对?", "[[bu2 dui4]]", ["[[bu4 dui4]]", "[[bu1 dui4]]", "[[bu2 dui2]]"], "不 + 4th tone: bú duì."),
    ],
)

# ---------------------------------------------------------------------------- 31
L31 = lesson(
    "And you? 呢",
    "我姓李，你呢？",
    requires=[],
    cards=[
        card("A follow-up question",
             "Put 呢 after a noun or a pronoun to ask the same question back. It only works when the question is already clear from what was just said. "
             "我是学生，你呢？ means “I am a student, and you?” The listener knows you are asking whether they are a student.",
             examples=[ex("我姓李，你呢？", "wo3 xing4 Li3, ni3 ne5", "My surname is Li. And you?", hl="呢"),
                       ex("我叫张华，您呢？", "wo3 jiao4 Zhang1 Hua2, nin2 ne5", "My name is Zhang Hua. And you? (polite)", hl="呢"),
                       ex("我是学生，你呢？ 我是老师。", "wo3 shi4 xue2sheng5, ni3 ne5? wo3 shi4 lao3shi1", "I am a student. And you? I am a teacher.", hl="呢"),
                       ex("我是海军，他呢？ 他是空军。", "wo3 shi4 hai3jun1, ta1 ne5? ta1 shi4 kong1jun1", "I am in the navy. And he? He is in the air force.")]),
        card("吗 or 呢?",
             "吗 turns a whole statement into a yes/no question and can start a conversation. 呢 follows a single noun or pronoun and needs a question already on the table. "
             "You cannot open a conversation with 你呢.",
             tables=[wtable([("你是老师吗？", "ni3 shi4 lao3shi1 ma5", "Are you a teacher? (new question)"), ("我是老师，你呢？", "wo3 shi4 lao3shi1, ni3 ne5", "I am a teacher. And you? (follow-up)")])]),
    ],
    exercises=[
        M("What does 你呢？ mean after 我是学生?", "And you?", ["Who are you?", "Are you a teacher?", "What is your name?"], "呢 repeats the same question: and are you a student?"),
        M("Where does 呢 go?", "After a noun or pronoun", ["At the start of a sentence", "After a whole statement to make a yes/no question", "Before the verb"], "呢 comes after a noun or pronoun."),
        M("When can you use 你呢？", "When the question is already clear from what was said", ["At the start of a conversation", "Only with older people", "Only to ask for a name"], "呢 relies on what came before."),
        M("Which sentence opens a conversation with a yes/no question?", "你是老师吗？", ["你呢？", "你也是老师呢？", "我呢？"], "Use 吗 for a new yes/no question."),
        M("How do you ask politely “And you?” to a teacher?", "您呢？", ["你们呢？", "他呢？", "我呢？"], "您 is the polite you."),
        M("你姓李吗？ and 我姓李，你呢？ differ because…", "The second is a follow-up that relies on what was said", ["The first is polite", "The second has no verb", "They mean the same"], "吗 asks a new question; 呢 follows up."),
        F("我姓李，你___？", "呢", ["吗", "什么", "们"], "你呢 asks for the other person's surname.", tr="My surname is Li. And you?"),
        F("我是海军，他___？", "呢", ["吗", "也", "们"], "他呢 asks about him.", tr="I am in the navy. And he?"),
        F("我叫张华，您___？", "呢", ["吗", "不", "也"], "您呢: and you? (polite)", tr="My name is Zhang Hua. And you?"),
        F("我是学生，你___？ 我是老师。", "呢", ["吗", "的", "们"], "你呢 asks the other person.", tr="I am a student. And you?"),
        M("You say 我很高兴认识你. The other person says 我也很高兴认识你. Which word shows “too”?", "也", ["很", "认识", "你"], "也 means also."),
        rd("呢", "ne5", ["ne1", "ne2", "ne4"]),
        M("Which is a correct reply to 我姓赵，你呢？", "我姓孙。", ["我是孙吗。", "你姓孙吗。", "孙什么。"], "Give your surname: 我姓 + surname."),
    ],
)

# ---------------------------------------------------------------------------- 32
L32 = lesson(
    "Who? 谁",
    "他是谁？ 谁是老师？",
    requires=[],
    cards=[
        card("谁 asks about people",
             "谁 means “who”. The word order is the same as in the answer, so 谁 stands where the person's name or title will be. "
             "It can be the object, as in 他是谁 (“he is who”), or the subject, as in 谁是老师 (“who is the teacher”). "
             "It is said shuí, and you will also hear it as shéi.",
             tables=[wtable([("他是谁？", "ta1 shi4 shui2", "Who is he?"), ("他是我的老师。", "ta1 shi4 wo3 de5 lao3shi1", "He is my teacher."),
                             ("谁是老师？", "shui2 shi4 lao3shi1", "Who is the teacher?"), ("我是老师。", "wo3 shi4 lao3shi1", "I am the teacher.")])]),
        card("More examples",
             "Notice that the answer takes the place of 谁 and nothing else changes.",
             examples=[ex("你是谁？", "ni3 shi4 shui2", "Who are you?", hl="谁"),
                       ex("我是李明。", "wo3 shi4 Li3 Ming2", "I am Li Ming.", hl="李明"),
                       ex("谁是陆军？", "shui2 shi4 lu4jun1", "Who is in the army?", hl="谁"),
                       ex("王明是陆军。", "Wang2 Ming2 shi4 lu4jun1", "Wang Ming is in the army.", hl="王明")]),
    ],
    exercises=[
        mean("谁", "shui2", "who", ["what", "also", "this"]),
        rd("谁", "shui2", ["shui4", "shui1", "shui3"]),
        M("What does 他是谁？ ask?", "Who is he?", ["What is his name?", "Is he a teacher?", "Where is he?"], "是谁 asks who someone is."),
        M("What does 谁是学生？ ask?", "Who is a student?", ["Is he a student?", "What is a student?", "Who are you?"], "谁 is the subject here."),
        M("Where is 谁 in the answer?", "In the same place as the answer", ["Always at the start", "Always at the end", "It never changes place"], "The answer replaces 谁."),
        M("Which is the answer to 谁是老师？", "我是老师。", ["我是谁。", "是老师吗。", "谁是我。"], "我 replaces 谁."),
        M("Which asks about a name, not about who the person is?", "他叫什么名字？", ["他是谁？", "谁是他？", "他是学生吗？"], "叫什么名字 asks for the name."),
        F("他是___？", "谁", ["什么", "吗", "们"], "谁 asks about a person.", tr="Who is he?"),
        F("___是陆军？ 王明是陆军。", "谁", ["什么", "吗", "呢"], "谁 stands where 王明 stands.", tr="Who is in the army?"),
        F("你是___？ 我是李明。", "谁", ["什么", "吗", "呢"], "你是谁 asks who you are.", tr="Who are you?"),
        F("她是___？ 她是我的老师。", "谁", ["什么", "吗", "们"], "她是谁 asks who she is.", tr="Who is she?"),
        M("How do you say “Who is the class leader?”", "谁是班长？", ["班长是什么？", "谁班长是？", "是班长吗谁？"], "谁 + 是 + 班长."),
        M("Which question uses 什么, not 谁?", "你姓什么？", ["他是谁？", "谁是老师？", "你是谁？"], "什么 asks about a thing or a word, 谁 about a person."),
        M("Which statement answers 她是谁？", "她是我的老师。", ["她是吗。", "她姓什么。", "她呢。"], "Answer who she is."),
    ],
)

# ---------------------------------------------------------------------------- 33
L33 = lesson(
    "This and that: 这 and 那",
    "这是… 那是… 这位 那位",
    requires=[],
    cards=[
        card("Introducing someone",
             "这 means “this” and 那 means “that”. To point out a person, use 这是 or 那是 and then the name or title: 这是李明 (“this is Li Ming”). "
             "To be more polite you add the measure word 位, which is used for people: 这位是王老师, 那位是谁？",
             tables=[wtable([("这", "zhe4", "this"), ("那", "na4", "that"), ("位", "wei4", "(polite measure word for people)"),
                             ("这位", "zhe4wei4", "this person (polite)"), ("那位", "na4wei4", "that person (polite)")])]),
        card("In use",
             "这 is for the person near you, 那 for the person farther away.",
             examples=[ex("这是李明。", "zhe4 shi4 Li3 Ming2", "This is Li Ming.", hl="这"),
                       ex("那是王老师。", "na4 shi4 Wang2 lao3shi1", "That is Teacher Wang.", hl="那"),
                       ex("这位是谁？", "zhe4wei4 shi4 shui2", "Who is this? (polite)", hl="这位"),
                       ex("那位是我们的班长。", "na4wei4 shi4 wo3men5 de5 ban1zhang3", "That is our class leader.", hl="那位")]),
    ],
    exercises=[
        mean("这", "zhe4", "this", ["that", "who", "what"]),
        mean("那", "na4", "that", ["this", "who", "also"]),
        mean("位", "wei4", "(polite measure word for people)", ["very", "happy", "polite “you”"]),
        rd("这", "zhe4", ["zhe1", "zhe2", "zhe3"]),
        rd("那", "na4", ["nei1", "nai4", "nu4"]),
        M("What does 这是李明 mean?", "This is Li Ming.", ["That is Li Ming.", "Who is Li Ming?", "Is this Li Ming?"], "这 is this."),
        M("What does 那位是谁？ ask?", "Who is that person? (polite)", ["Who is this person?", "What is that?", "Is that you?"], "那位 is that person."),
        M("Which word makes “this person” more polite?", "位", ["们", "吗", "呢"], "这位 and 那位 are the polite forms."),
        M("You are pointing at a person right next to you. You say…", "这位是谁？", ["那位是谁？", "你是谁？", "他呢？"], "这 is near, 那 is far."),
        M("You are asking about someone across the room. You say…", "那位是谁？", ["这位是谁？", "你呢？", "他是吗？"], "那 is far."),
        F("___是王老师。 (this)", "这", ["那", "谁", "吗"], "这 is this.", tr="This is Teacher Wang."),
        F("___是我们的班长。 (that)", "那", ["这", "谁", "吗"], "那 is that.", tr="That is our class leader."),
        F("这___是谁？", "位", ["们", "吗", "呢"], "位 is the polite measure word for people.", tr="Who is this?"),
        M("How do you introduce a person to someone else?", "这是李明。", ["李明是这。", "这李明是。", "是这李明。"], "这 + 是 + name."),
    ],
)

# ---------------------------------------------------------------------------- 34
L34 = lesson(
    "People around you",
    "同学, 班长, 朋友, 太太, 先生",
    requires=[],
    cards=[
        card("Classmates, leaders and friends",
             "A 同学 is a classmate, and 班长 is the class leader (the person in charge of a class or squad). "
             "朋友 is a friend: 男朋友 and 女朋友 are boyfriend and girlfriend, because 男 means male and 女 female. "
             "太太 is a wife and 先生 is a husband (it also means “Mr.”). Both 朋友 and 先生 end in a neutral tone.",
             tables=[wtable([("同学", "tong2xue2", "a classmate"), ("班长", "ban1zhang3", "a class leader"), ("老师", "lao3shi1", "a teacher"),
                             ("学生", "xue2sheng5", "a student"), ("朋友", "peng2you5", "a friend"), ("男朋友", "nan2 peng2you5", "a boyfriend"),
                             ("女朋友", "nv3 peng2you5", "a girlfriend"), ("太太", "tai4tai5", "a wife"), ("先生", "xian1sheng5", "a husband; Mr.")])]),
        card("Introducing people",
             "Use 这是 or 那是 with these words, and 也 and 不 as before.",
             examples=[ex("这是我的同学。", "zhe4 shi4 wo3 de5 tong2xue2", "This is my classmate."),
                       ex("那位是班长，他是海军。", "na4wei4 shi4 ban1zhang3, ta1 shi4 hai3jun1", "That is the class leader; he is in the navy."),
                       ex("她是我的朋友。", "ta1 shi4 wo3 de5 peng2you5", "She is my friend."),
                       ex("他是我太太的老师。", "ta1 shi4 wo3 tai4tai5 de5 lao3shi1", "He is my wife's teacher.")]),
    ],
    exercises=[
        mean("同学", "tong2xue2", "a classmate", ["a teacher", "a friend", "a class leader"]),
        mean("班长", "ban1zhang3", "a class leader", ["a classmate", "a teacher", "a student"]),
        mean("朋友", "peng2you5", "a friend", ["a classmate", "a husband", "a student"]),
        mean("女朋友", "nv3 peng2you5", "a girlfriend", ["a boyfriend", "a wife", "a teacher"]),
        mean("男朋友", "nan2 peng2you5", "a boyfriend", ["a girlfriend", "a husband", "a classmate"]),
        mean("太太", "tai4tai5", "a wife", ["a husband", "a girlfriend", "a teacher"]),
        mean("先生", "xian1sheng5", "a husband; Mr.", ["a wife", "a student", "a class leader"]),
        rd("同学", "tong2xue2", ["tong4xue2", "tong2xue4", "tong2xue1"]),
        rd("朋友", "peng2you5", ["peng2you3", "peng1you5", "pen2you5"]),
        rd("班长", "ban1zhang3", ["ban1chang2", "ban2zhang3", "ban1zhang4"]),
        M("Which character means “female”?", "女", ["男", "太", "友"], "女 is female: 女朋友 is girlfriend."),
        M("Which character means “male”?", "男", ["女", "太", "友"], "男 is male: 男朋友 is boyfriend."),
        F("这是我的___。 (classmate)", "同学", ["班长", "太太", "先生"], "同学 is a classmate.", tr="This is my classmate."),
        F("那位是我们的___。 (class leader)", "班长", ["同学", "太太", "女朋友"], "班长 is the class leader.", tr="That is our class leader."),
        M("How do you say “She is my friend”?", "她是我的朋友。", ["他是我的朋友。", "她是我的同学。", "她是我的太太。"], "她 is she and 朋友 is friend."),
    ],
)

# ---------------------------------------------------------------------------- 35
L35 = lesson(
    "Pronouns, 们 and 的",
    "我们, 你们, 他们 · 我的, 你的",
    requires=[],
    cards=[
        card("Pronoun forms",
             "Chinese pronouns do not change for subject and object: 我 is both I and me. Add 们 for the plural, and 的 for the possessive. "
             "他 and 她 sound the same (tā) and differ only in writing. 们 is in the neutral tone, and it is used for people only: 老师们 is fine, but never 房子们.",
             tables=[table(["Singular", "Plural", "Possessive"],
                           [["我", "我们", "我的 / 我们的"], ["你", "你们", "你的 / 你们的"], ["您", "你们", "您的"],
                            ["他", "他们", "他的 / 他们的"], ["她", "她们", "她的 / 她们的"]],
                           title="I / we, you, he, she", say=[0, 1, 2])]),
        card("In pinyin",
             "您 has no plural of its own: for several people use 你们. 他们 means “they” for men or for a mixed group, and 她们 for women only.",
             tables=[wtable([("我们", "wo3men5", "we, us"), ("你们", "ni3men5", "you (plural)"), ("他们", "ta1men5", "they (men or mixed)"),
                             ("她们", "ta1men5", "they (women)"), ("我的", "wo3 de5", "my"), ("你的", "ni3 de5", "your"), ("您的", "nin2 de5", "your (polite)"),
                             ("他的", "ta1 de5", "his"), ("她的", "ta1 de5", "her"), ("我们的", "wo3men5 de5", "our")])]),
        card("The pattern with 的",
             "Owner + 的 + thing: 我的老师 is “my teacher”.",
             examples=[ex("他是我的老师。", "ta1 shi4 wo3 de5 lao3shi1", "He is my teacher.", hl="我的"),
                       ex("那位是你们的老师吗？", "na4wei4 shi4 ni3men5 de5 lao3shi1 ma5", "Is that your (plural) teacher?", hl="你们的"),
                       ex("我是李明的同学。", "wo3 shi4 Li3 Ming2 de5 tong2xue2", "I am Li Ming's classmate.", hl="李明的")]),
    ],
    exercises=[
        mean("我们", "wo3men5", "we, us", ["I, me", "you (plural)", "they"]),
        mean("你们", "ni3men5", "you (plural)", ["we, us", "you (polite)", "they"]),
        mean("他们", "ta1men5", "they (men or mixed)", ["we, us", "you (plural)", "he"]),
        mean("我的", "wo3 de5", "my", ["our", "your", "his"]),
        mean("你的", "ni3 de5", "your", ["my", "his", "our"]),
        mean("我们的", "wo3men5 de5", "our", ["my", "their", "your (plural)"]),
        rd("我们", "wo3men5", ["wo3men2", "wo2men5", "wo3men4"]),
        rd("他们", "ta1men5", ["ta1men2", "ta3men5", "ta4men5"]),
        M("What does 们 do?", "Makes a person word plural", ["Makes a sentence a question", "Means “not”", "Makes it possessive"], "们 is the plural marker for people."),
        M("What does 的 do?", "Shows who owns something", ["Makes a plural", "Asks a question", "Means “also”"], "的 is the possessive particle."),
        M("How is the 们 in 我们 pronounced?", "In the neutral tone", ["In the 4th tone", "In the 2nd tone", "In the 1st tone"], "们 is light and short."),
        M("Which is incorrect?", "房子们", ["老师们", "同学们", "我们"], "们 is only for people."),
        M("Which word is the polite form of “you”?", "您", ["你们", "他", "她"], "您 is polite."),
        F("他是___老师。 (my)", "我的", ["吗", "呢", "很"], "我的 means my.", tr="He is my teacher."),
        F("那位是___老师吗？ (your, plural)", "你们的", ["你们吗", "你呢", "你很"], "你们的 means your (plural).", tr="Is that your teacher?"),
        F("___都是学生。 (we all)", "我们", ["吗", "呢", "很"], "我们 means we.", tr="We are all students."),
    ],
)

# ---------------------------------------------------------------------------- 36
L36 = lesson(
    "Shortcuts with 的",
    "我同学, 我太太 · 是我的",
    requires=[],
    cards=[
        card("Leaving 的 out",
             "With close relations and groups you belong to, 的 is often left out, as in 我同学 and 我太太. "
             "You will see the same with family words such as 我爸爸 and 你父母.",
             tables=[wtable([("我同学", "wo3 tong2xue2", "my classmate"), ("我太太", "wo3 tai4tai5", "my wife"), ("你先生", "ni3 xian1sheng5", "your husband"),
                             ("我爸爸", "wo3 ba4ba5", "my dad"), ("我妈妈", "wo3 ma1ma5", "my mum")])]),
        card("Leaving the noun out",
             "When it is clear what the owned thing is, you can drop the noun after 的 and keep 的: 这是你的吗？ 是我的。",
             examples=[ex("这是你的吗？", "zhe4 shi4 ni3 de5 ma5", "Is this yours?"),
                       ex("是我的。", "shi4 wo3 de5", "It is mine.", hl="我的"),
                       ex("谁的老师姓王？ 他们的。", "shui2 de5 lao3shi1 xing4 Wang2? ta1men5 de5", "Whose teacher is surnamed Wang? Theirs.", hl="他们的"),
                       ex("李明是谁的同学？ 是我的。", "Li3 Ming2 shi4 shui2 de5 tong2xue2? shi4 wo3 de5", "Whose classmate is Li Ming? Mine.")]),
    ],
    exercises=[
        M("Which phrase leaves 的 out correctly?", "我同学", ["我吗同学", "我们吗同学", "同学我"], "With close relations, 的 is often dropped."),
        M("Which means “my wife”?", "我太太", ["我先生", "我同学", "我朋友"], "太太 is wife."),
        M("What does 是我的 mean in answer to 这是你的吗？", "It is mine.", ["It is yours.", "It is his.", "I am not."], "是 + 我的."),
        M("What does 谁的老师？ ask?", "Whose teacher?", ["Who is the teacher?", "Which teacher?", "What teacher?"], "谁的 asks about the owner."),
        M("Which is a possible answer to 谁的老师姓王？", "他们的。", ["他们是。", "他们吗。", "他们呢。"], "Drop the noun and keep 的: 他们的."),
        M("Which is a possible answer to 这是你的吗？", "不是，是他的。", ["不对，是他。", "是的他。", "不是，他的吗。"], "不是, 是他的: No, it is his."),
        rd("爸爸", "ba4ba5", ["ba1ba5", "ba4ba4", "ba2ba5"]),
        rd("妈妈", "ma1ma5", ["ma1ma1", "ma2ma5", "ma4ma5"]),
        rd("太太", "tai4tai5", ["tai4tai4", "tai2tai5", "tai3tai5"]),
        mean("爸爸", "ba4ba5", "dad", ["mum", "a wife", "a husband"]),
        mean("妈妈", "ma1ma5", "mum", ["dad", "a wife", "a friend"]),
        F("这是___的吗？ 是我的。 (yours)", "你", ["谁", "吗", "们"], "你的 is yours.", tr="Is this yours? It is mine."),
        F("李明是谁的同学？ 是___。", "我的", ["我吗", "我呢", "我很"], "我的 means mine.", tr="Whose classmate is Li Ming? Mine."),
        F("这是我___。 (my wife)", "太太", ["先生", "同学", "老师"], "太太 is a wife.", tr="This is my wife."),
    ],
)

UNIT = unit("第二课 Greetings and introductions", [L27, L28, L29, L30, L31, L32, L33, L34, L35, L36])

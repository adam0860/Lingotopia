import 'lifelines.dart';

// The words a generic Lingo Ladder pack needs in the learner's target
// language: three friends, what they say when phoned, and the host's welcome.
//
// Everything here is const data and deliberately short and grammatically
// plain, so each line is easy to check. Lines avoid gendered forms (a friend
// of either sex can say them) and the one placeholder, `{L}`, stands for the
// option letter A-D. Friend names are in the target language's own script in
// `nameTarget`, with a readable Latin form in `name` (its first letter is the
// avatar's initial). For Latin-script languages the two are the same.
//
// Reviewed by reading only, no native speaker yet: see the notes beside the
// languages that deserve a second look.

/// The friends' strengths, by subject. They are the same for every language so
/// the friends cover the same subjects as the Russian pack's do.
const Set<String> _artsAndLanguage = {'language', 'literature', 'arts', 'food'};
const Set<String> _scienceAndNature = {
  'science', 'technology', 'nature', 'sports', 'health',
};
const Set<String> _historyAndSociety = {
  'history', 'politics', 'geography', 'economics', 'society',
};

class PackTexts {
  const PackTexts({
    required this.friends,
    required this.friendLines,
    required this.hostIntro,
  });

  /// Exactly three: a language teacher, an engineer and a historian.
  final List<Friend> friends;

  /// Two lines for each mood. `{L}` becomes the option letter.
  final Map<FriendMood, List<FriendLine>> friendLines;

  /// The host's welcome, shown on the lobby screen.
  final FriendLine hostIntro;

  /// The texts for each deck language that has them.
  static const Map<String, PackTexts> byLanguage = {
    'es': spanish,
    'ja': japanese,
    'ar': arabic,
    'arz': egyptianArabic,
    'zh': chinese,
    'ko': korean,
    'it': italian,
    'tl': tagalog,
    'pl': polish,
    'sw': swahili,
    'tr': turkish,
    'pt': portuguese,
  };

  /// Used for a language with no texts of its own: English friends and lines.
  static const PackTexts english = PackTexts(
    hostIntro: FriendLine(
      'Welcome! Fifteen questions. One million points.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'emma',
        name: 'Emma',
        nameTarget: 'Emma',
        role: 'Language teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'liam',
        name: 'Liam',
        nameTarget: 'Liam',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'hale',
        name: 'Professor Hale',
        nameTarget: 'Professor Hale',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine("I'm certain! It's {L}.", "I'm certain! It's {L}."),
        FriendLine("That's easy. {L}, of course!", "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine("I think it's {L}, but I'm not sure.",
            "I think it's {L}, but I'm not sure."),
        FriendLine('Most likely {L}.', 'Most likely {L}.'),
      ],
      FriendMood.guess: [
        FriendLine("Hmm… I don't know. Maybe {L}?", "Hmm… I don't know. Maybe {L}?"),
        FriendLine("Honestly, it's just a guess: {L}.",
            "Honestly, it's just a guess: {L}."),
      ],
    },
  );

  static const PackTexts spanish = PackTexts(
    hostIntro: FriendLine(
      '¡Bienvenido! Quince preguntas. Un millón de puntos.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'lucia',
        name: 'Lucía',
        nameTarget: 'Lucía',
        role: 'Spanish teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'carlos',
        name: 'Carlos',
        nameTarget: 'Carlos',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'ortega',
        name: 'Profesor Ortega',
        nameTarget: 'Profesor Ortega',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('¡Lo sé con certeza! Es la {L}.', "I'm certain! It's {L}."),
        FriendLine('¡Fácil! Es la {L}, claro.', "Easy! It's {L}, of course."),
      ],
      FriendMood.unsure: [
        FriendLine('Creo que es la {L}, pero tengo dudas.',
            "I think it's {L}, but I have my doubts."),
        FriendLine('Seguramente es la {L}.', "It's probably {L}."),
      ],
      FriendMood.guess: [
        FriendLine('Mmm… No lo sé. ¿Quizás la {L}?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('La verdad, es solo una suposición: la {L}.',
            "Honestly, it's just a guess: {L}."),
      ],
    },
  );

  static const PackTexts italian = PackTexts(
    hostIntro: FriendLine(
      'Benvenuto! Quindici domande. Un milione di punti.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'giulia',
        name: 'Giulia',
        nameTarget: 'Giulia',
        role: 'Italian teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'marco',
        name: 'Marco',
        nameTarget: 'Marco',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'rossi',
        name: 'Professor Rossi',
        nameTarget: 'Professor Rossi',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('Lo so di sicuro! È la {L}.', "I'm certain! It's {L}."),
        FriendLine('Facile! È la {L}, ovviamente.', "Easy! It's {L}, obviously."),
      ],
      FriendMood.unsure: [
        FriendLine('Penso che sia la {L}, ma ho dei dubbi.',
            "I think it's {L}, but I have my doubts."),
        FriendLine('Probabilmente è la {L}.', "It's probably {L}."),
      ],
      FriendMood.guess: [
        FriendLine('Mmm… Non lo so. Forse la {L}?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine("Sinceramente, è solo un'ipotesi: la {L}.",
            "Honestly, it's just a guess: {L}."),
      ],
    },
  );

  static const PackTexts portuguese = PackTexts(
    hostIntro: FriendLine(
      'Bem-vindo! Quinze perguntas. Um milhão de pontos.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'ana',
        name: 'Ana',
        nameTarget: 'Ana',
        role: 'Portuguese teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'pedro',
        name: 'Pedro',
        nameTarget: 'Pedro',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'silva',
        name: 'Professor Silva',
        nameTarget: 'Professor Silva',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('Eu sei com certeza! É a {L}.', "I'm certain! It's {L}."),
        FriendLine('Fácil! É a {L}, claro.', "Easy! It's {L}, of course."),
      ],
      FriendMood.unsure: [
        FriendLine('Acho que é a {L}, mas tenho dúvidas.',
            "I think it's {L}, but I have my doubts."),
        FriendLine('Provavelmente é a {L}.', "It's probably {L}."),
      ],
      FriendMood.guess: [
        FriendLine('Hum… Não sei. Talvez a {L}?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('Sinceramente, é só um palpite: a {L}.',
            "Honestly, it's just a guess: {L}."),
      ],
    },
  );

  static const PackTexts polish = PackTexts(
    hostIntro: FriendLine(
      'Witaj! Piętnaście pytań. Milion punktów.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'kasia',
        name: 'Kasia',
        nameTarget: 'Kasia',
        role: 'Polish teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'marek',
        name: 'Marek',
        nameTarget: 'Marek',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'nowak',
        name: 'Profesor Nowak',
        nameTarget: 'Profesor Nowak',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('Wiem na pewno! To odpowiedź {L}.', "I'm certain! It's answer {L}."),
        FriendLine('To proste. Oczywiście {L}!', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('Chyba {L}, ale mam wątpliwości.', 'Probably {L}, but I have my doubts.'),
        FriendLine('Prawdopodobnie {L}.', 'Most likely {L}.'),
      ],
      FriendMood.guess: [
        FriendLine('Hmm… Nie wiem. Może {L}?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('Szczerze mówiąc, tylko zgaduję: {L}.',
            "Honestly, I'm just guessing: {L}."),
      ],
    },
  );

  static const PackTexts turkish = PackTexts(
    hostIntro: FriendLine(
      'Hoş geldin! On beş soru. Bir milyon puan.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'elif',
        name: 'Elif',
        nameTarget: 'Elif',
        role: 'Turkish teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'emre',
        name: 'Emre',
        nameTarget: 'Emre',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'yilmaz',
        name: 'Professor Yılmaz',
        nameTarget: 'Profesör Yılmaz',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('Eminim! Cevap {L}.', "I'm certain! The answer is {L}."),
        FriendLine('Çok kolay. Tabii ki {L}!', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('Bence {L}, ama emin değilim.', "I think {L}, but I'm not sure."),
        FriendLine('Büyük ihtimalle {L}.', 'Most likely {L}.'),
      ],
      FriendMood.guess: [
        FriendLine('Hmm… Bilmiyorum. Belki {L}?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('Dürüst olayım, sadece bir tahmin: {L}.',
            "To be honest, it's just a guess: {L}."),
      ],
    },
  );

  // Swahili: the "most likely" line is the one to double-check.
  static const PackTexts swahili = PackTexts(
    hostIntro: FriendLine(
      'Karibu! Maswali kumi na matano. Pointi milioni moja.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'amina',
        name: 'Amina',
        nameTarget: 'Amina',
        role: 'Swahili teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'juma',
        name: 'Juma',
        nameTarget: 'Juma',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'mwangi',
        name: 'Professor Mwangi',
        nameTarget: 'Profesa Mwangi',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('Najua kabisa! Ni {L}.', "I know for sure! It's {L}."),
        FriendLine('Ni rahisi. Bila shaka ni {L}!', "It's easy. Without a doubt it's {L}!"),
      ],
      FriendMood.unsure: [
        FriendLine('Nadhani ni {L}, lakini sina uhakika.',
            "I think it's {L}, but I'm not sure."),
        FriendLine('Kuna uwezekano mkubwa kwamba ni {L}.', "It's most likely {L}."),
      ],
      FriendMood.guess: [
        FriendLine('Hmm… Sijui. Labda {L}?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('Kusema kweli, ni kubahatisha tu: {L}.',
            "Honestly, it's just guessing: {L}."),
      ],
    },
  );

  static const PackTexts tagalog = PackTexts(
    hostIntro: FriendLine(
      'Maligayang pagdating! Labinlimang tanong. Isang milyong puntos.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'liza',
        name: 'Liza',
        nameTarget: 'Liza',
        role: 'Tagalog teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'jun',
        name: 'Jun',
        nameTarget: 'Jun',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'reyes',
        name: 'Professor Reyes',
        nameTarget: 'Prof. Reyes',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('Sigurado ako! Ang sagot ay {L}.', "I'm sure! The answer is {L}."),
        FriendLine('Madali lang. Siyempre, {L}!', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('Sa tingin ko, {L}, pero hindi ako sigurado.',
            "I think it's {L}, but I'm not sure."),
        FriendLine('Malamang {L}.', 'Probably {L}.'),
      ],
      FriendMood.guess: [
        FriendLine('Hmm… Hindi ko alam. Baka {L}?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('Totoo lang, hula lang ito: {L}.', "Honestly, this is just a guess: {L}."),
      ],
    },
  );

  static const PackTexts japanese = PackTexts(
    hostIntro: FriendLine(
      'ようこそ！質問は十五問です。百万ポイント！',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'tanaka',
        name: 'Tanaka-sensei',
        nameTarget: '田中先生',
        role: 'Japanese teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'kenji',
        name: 'Kenji',
        nameTarget: '健二',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'yamamoto',
        name: 'Professor Yamamoto',
        nameTarget: '山本教授',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('自信があります！答えは{L}です。', "I'm confident! The answer is {L}."),
        FriendLine('簡単です。もちろん{L}です！', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('{L}だと思いますが、自信がありません。',
            "I think it's {L}, but I'm not confident."),
        FriendLine('たぶん{L}です。', "It's probably {L}."),
      ],
      FriendMood.guess: [
        FriendLine('うーん…分かりません。{L}かな？', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('正直、ただの勘です。{L}です。', "Honestly, it's just a hunch: {L}."),
      ],
    },
  );

  static const PackTexts chinese = PackTexts(
    hostIntro: FriendLine(
      '欢迎！一共十五道题。一百万积分。',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'li',
        name: 'Teacher Li',
        nameTarget: '李老师',
        role: 'Chinese teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'wangwei',
        name: 'Wang Wei',
        nameTarget: '王伟',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'zhang',
        name: 'Professor Zhang',
        nameTarget: '张教授',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('我很有把握！答案是{L}。', "I'm very sure! The answer is {L}."),
        FriendLine('这很简单，当然是{L}！', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('我觉得是{L}，但是不太确定。', "I think it's {L}, but I'm not very sure."),
        FriendLine('很可能是{L}。', "It's very likely {L}."),
      ],
      FriendMood.guess: [
        FriendLine('嗯……我不知道。也许是{L}？', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('说实话，我只是猜的：{L}。', "Honestly, I'm just guessing: {L}."),
      ],
    },
  );

  static const PackTexts korean = PackTexts(
    hostIntro: FriendLine(
      '환영합니다! 열다섯 문제입니다. 백만 포인트!',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'kim',
        name: 'Teacher Kim',
        nameTarget: '김 선생님',
        role: 'Korean teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'minjun',
        name: 'Minjun',
        nameTarget: '민준',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'park',
        name: 'Professor Park',
        nameTarget: '박 교수님',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('확실히 알아요! 정답은 {L}예요.', "I'm certain! The answer is {L}."),
        FriendLine('쉬워요. 당연히 {L}예요!', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('{L}인 것 같은데, 잘 모르겠어요.', "I think it's {L}, but I'm not sure."),
        FriendLine('아마 {L}일 거예요.', "It's probably {L}."),
      ],
      FriendMood.guess: [
        FriendLine('음… 모르겠어요. {L}일까요?', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('솔직히 그냥 추측이에요: {L}.', "Honestly, it's just a guess: {L}."),
      ],
    },
  );

  /// Modern Standard Arabic.
  static const PackTexts arabic = PackTexts(
    hostIntro: FriendLine(
      'أهلاً وسهلاً! خمسة عشر سؤالاً. مليون نقطة.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'layla',
        name: 'Layla',
        nameTarget: 'ليلى',
        role: 'Arabic teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'omar',
        name: 'Omar',
        nameTarget: 'عمر',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'hassan',
        name: 'Professor Hassan',
        nameTarget: 'الأستاذ حسن',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('أعرف الإجابة جيداً! إنها {L}.', "I know the answer well! It's {L}."),
        FriendLine('هذا سهل. بالطبع {L}!', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('أظن أنها {L}، لكن لدي بعض الشك.',
            "I think it's {L}, but I have some doubt."),
        FriendLine('على الأرجح {L}.', 'Most likely {L}.'),
      ],
      FriendMood.guess: [
        FriendLine('همم… لا أعرف. ربما {L}؟', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('بصراحة، هذا مجرد تخمين: {L}.', "Honestly, this is just a guess: {L}."),
      ],
    },
  );

  /// Colloquial Egyptian Arabic (the deck's language code is `arz`).
  static const PackTexts egyptianArabic = PackTexts(
    hostIntro: FriendLine(
      'أهلاً بيكم! خمستاشر سؤال. مليون نقطة.',
      'Welcome! Fifteen questions. One million points.',
    ),
    friends: [
      Friend(
        id: 'mona',
        name: 'Mona',
        nameTarget: 'منى',
        role: 'Arabic teacher',
        strengths: _artsAndLanguage,
      ),
      Friend(
        id: 'ahmed',
        name: 'Ahmed',
        nameTarget: 'أحمد',
        role: 'Engineer',
        strengths: _scienceAndNature,
      ),
      Friend(
        id: 'mahmoud',
        name: 'Professor Mahmoud',
        nameTarget: 'الأستاذ محمود',
        role: 'Historian',
        strengths: _historyAndSociety,
      ),
    ],
    friendLines: {
      FriendMood.sure: [
        FriendLine('الإجابة أكيد {L}!', "The answer is definitely {L}!"),
        FriendLine('ده سهل. طبعاً {L}!', "That's easy. {L}, of course!"),
      ],
      FriendMood.unsure: [
        FriendLine('أعتقد إنها {L}، بس عندي شك.', "I think it's {L}, but I have a doubt."),
        FriendLine('غالباً {L}.', 'Probably {L}.'),
      ],
      FriendMood.guess: [
        FriendLine('همم… معرفش. يمكن {L}؟', "Hmm… I don't know. Maybe {L}?"),
        FriendLine('بصراحة، ده مجرد تخمين: {L}.', "Honestly, this is just a guess: {L}."),
      ],
    },
  );
}

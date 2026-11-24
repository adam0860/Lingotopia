"""Unit 19: Genki I, Reading and Writing, Lesson 6 "My Favorite Restaurant" (私のすきなレストラン), pp. 312-317.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese I (2nd edition, 2011).
The book's audio, stroke-order drawings, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
東|east|とう|ひがし|8|東(ひがし)=east;東口(ひがしぐち)=east exit;東京(とうきょう)=Tokyo;関東(かんとう)=Kanto area;東洋(とうよう)=the East
西|west|せい・さい|にし|6|西(にし)=west;西口(にしぐち)=west exit;北西(ほくせい)=northwest;関西(かんさい)=Kansai area;西洋(せいよう)=the West
南|south|なん|みなみ|9|南(みなみ)=south;南口(みなみぐち)=south exit;南東(なんとう)=southeast;南極(なんきょく)=Antarctica;東南アジア(とうなんアジア)=Southeast Asia
北|north|ほく・ほっ|きた|5|北(きた)=north;北口(きたぐち)=north exit;東北(とうほく)=Tohoku area;北極(ほっきょく)=North Pole;北海道(ほっかいどう)=Hokkaido
口|mouth|こう|ぐち・くち|3|口(くち)=mouth;人口(じんこう)=population;入り口(いりぐち)=entrance
出|to exit|しゅっ・しゅつ|で・だ|5|出る(でる)=to exit;出口(でぐち)=exit;出す(だす)=to take something out;出席(しゅっせき)=attendance;輸出(ゆしゅつ)=export
右|right|う・ゆう|みぎ|5|右(みぎ)=right;右折(うせつ)=right turn;左右(さゆう)=right and left;右手(みぎて)=right hand;右側(みぎがわ)=right side
左|left|さ|ひだり|5|左(ひだり)=left;左折(させつ)=left turn;左手(ひだりて)=left hand;左利き(ひだりきき)=left-handed
分|minute; to divide|ふん・ぷん・ぶん|わ|4|五分(ごふん)=five minutes;十分(じゅっぷん・じっぷん)=ten minutes;自分(じぶん)=oneself;分ける(わける)=to divide
先|ahead|せん|さき|6|先生(せんせい)=teacher;先週(せんしゅう)=last week;先に(さきに)=ahead;先月(せんげつ)=last month;先輩(せんぱい)=senior member
生|birth|せい・しょう|う|5|学生(がくせい)=student;生まれる(うまれる)=to be born;一生に一度(いっしょうにいちど)=once in a lifetime
大|big|だい・たい|おお|3|大学生(だいがくせい)=college student;大きい(おおきい)=big;大変な(たいへんな)=tough;大人(おとな)=adult;大使館(たいしかん)=embassy
学|learning|がく・がっ|まな|8|大学(だいがく)=university;学校(がっこう)=school;学ぶ(まなぶ)=to study;学部(がくぶ)=department, faculty
外|outside|がい|そと|5|外国(がいこく)=foreign country;外国人(がいこくじん)=foreigner;外(そと)=outside;海外(かいがい)=overseas
国|country|こく・ごく|くに|8|中国(ちゅうごく)=China;国(くに)=country;韓国(かんこく)=South Korea;国会(こっかい)=the Diet
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]
_EXITS = [("ひがしぐち", "東口", "east exit"), ("にしぐち", "西口", "west exit"), ("みなみぐち", "南口", "south exit"), ("きたぐち", "北口", "north exit"), ("でぐち", "出口", "exit"), ("いりぐち", "入口", "entrance")]
_DIR = [("ひがし", "東", "east"), ("にし", "西", "west"), ("みなみ", "南", "south"), ("きた", "北", "north"), ("みぎ", "右", "right"), ("ひだり", "左", "left")]

# ================================================================= 1 kanji 東 to 左
L1 = lesson(
    "Kanji: 東 西 南 北 口 出 右 左",
    "東 · 西 · 南 · 北 · 口 · 出 · 右 · 左 · directions and station exits",
    requires=[],
    cards=[
        card("My Favorite Restaurant: fifteen new kanji", "Lesson 6 of the Reading and Writing section (「私のすきなレストラン」, My Favorite Restaurant) teaches 東 西 南 北 口 出 右 左 分 先 生 大 学 外 国. The reading practice includes a map, a bulletin board and an essay about a restaurant near a station. The first eight kanji are the compass points, exits and the left and right."),
        *J.kanji_cards(_K1, per=3),
        card("Station exits", "At a Japanese station, each exit is named for a compass point: 東口 (east exit), 西口 (west exit), 南口 (south exit) and 北口 (north exit). 口 (mouth) is read ぐち in the word and くち alone, because the first sound of a second word often turns voiced (くち → ぐち).",
             tables=[ktable(_EXITS, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("Compass points and left/right", "The four compass points are in the order Japanese people say them: 東西南北 (とうざいなんぼく). Right and left are 右 and 左.",
             tables=[ktable(_DIR, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1)
                   + [M(f"What does {k} mean?", en, three([e for _, _, e in _DIR if e != en]), f"{k} is {a}.") for a, k, en in _DIR]
                   + [M(f"What does {k} mean?", en, three([e for _, _, e in _EXITS if e != en]), f"{k} is {a}.") for a, k, en in _EXITS]
                   + [M(f"How do you read {k}?", a, three([x for x, _, e in _EXITS if e != en]), f"{k} is {a}.") for a, k, en in _EXITS]
                   + [M(f"Which kanji means “{en}”?", k, three([x for _, x, e in _EXITS if e != en]), f"{en} is {k} ({a}).") for a, k, en in _EXITS]
                   + [F("えきの___口を出て、右へ五分ぐらいです。 (south)", "南", ["北", "東", "西"], "南口 is the south exit."), F("___口を出て、左へ十分ぐらいです。 (north)", "北", ["南", "東", "西"], "北口 is the north exit."),
                      F("えきの___口を出て、まっすぐ五分ぐらいです。 (east)", "東", ["西", "南", "北"], "東口 is the east exit."), F("えきの___口を出てください。 (west)", "西", ["東", "南", "北"], "西口 is the west exit."),
                      M("What does 北海道 (ほっかいどう) have as its first kanji?", "北", ["南", "東", "西"], "北海道 is Hokkaido: the northern sea road."),
                      M("How do you read 東京?", "とうきょう", ["ひがしみやこ", "とうけい", "あずまきょう"], "東京 is とうきょう."), M("How do you read 関西?", "かんさい", ["かんにし", "かんせい", "せきにし"], "関西 is かんさい: the Kansai area."), M("How do you read 東北?", "とうほく", ["ひがしきた", "とうぼく", "とうきた"], "東北 is とうほく: the Tohoku area."),
                      M("How do you read 人口?", "じんこう", ["ひとくち", "にんこう", "じんぐち"], "人口 is じんこう: population."), M("How do you read 出席?", "しゅっせき", ["でせき", "しゅつせき", "だしせき"], "出席 is しゅっせき: attendance.")]),
)

# ================================================================= 2 kanji 分 to 国
L2 = lesson(
    "Kanji: 分 先 生 大 学 外 国",
    "分 · 先 · 生 · 大 · 学 · 外 · 国 · minutes, teacher, university, foreign countries",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=3),
        card("Words you already know", "Several of these kanji spell words you know in hiragana: 先生 (せんせい), 学生 (がくせい), 大学 (だいがく), 大学生 (だいがくせい), 外国人 (がいこくじん), 学校 (がっこう), 大きい (おおきい), 〜分 (ふん／ぷん). 十分 is read じゅっぷん (also じっぷん) when it means ten minutes and じゅうぶん when it means “enough”.",
             tables=[ktable([("せんせい", "先生", "teacher"), ("がくせい", "学生", "student"), ("だいがく", "大学", "university"), ("だいがくせい", "大学生", "university student"), ("がいこくじん", "外国人", "foreigner"), ("がっこう", "学校", "school"), ("おおきい", "大きい", "big"), ("ごふん", "五分", "five minutes"), ("じゅっぷん", "十分", "ten minutes"), ("じゅうごふん", "十五分", "fifteen minutes")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2)
                   + [M("How do you read 先生?", "せんせい", ["さきなま", "せんしょう", "さきせい"], "先生 is せんせい."), M("How do you read 学生?", "がくせい", ["まなせい", "がくしょう", "がくなま"], "学生 is がくせい."), M("How do you read 大学?", "だいがく", ["おおがく", "たいがく", "だいまな"], "大学 is だいがく."),
                      M("How do you read 大学生?", "だいがくせい", ["たいがくせい", "おおがくせい", "だいがくしょう"], "大学生 is だいがくせい."), M("How do you read 学校?", "がっこう", ["がくこう", "がっこ", "まなこう"], "学校 is がっこう."), M("How do you read 外国人?", "がいこくじん", ["そとくにひと", "がいごくじん", "がいこくにん"], "外国人 is がいこくじん."),
                      M("How do you read 大きい?", "おおきい", ["だいきい", "たいきい", "おおいき"], "大きい is おおきい."), M("How do you read 十五分?", "じゅうごふん", ["じゅうごぷん", "じっごふん", "じゅごふん"], "十五分 is じゅうごふん."), M("How do you read 五分?", "ごふん", ["ごぷん", "ごぶん", "ごわ"], "五分 is ごふん."),
                      M("How do you read 中国?", "ちゅうごく", ["なかくに", "ちゅうこく", "じゅうごく"], "中国 is ちゅうごく: China."), M("How do you read 韓国?", "かんこく", ["からくに", "かんごく", "かんくに"], "韓国 is かんこく: South Korea."), M("How do you read 先週?", "せんしゅう", ["さきしゅう", "せんじゅう", "せんしゅ"], "先週 is せんしゅう: last week."),
                      M("How do you read 先月?", "せんげつ", ["さきつき", "せんがつ", "せんつき"], "先月 is せんげつ: last month."), M("What does 先輩 mean?", "senior member", ["classmate", "teacher", "student"], "先輩 is せんぱい."), M("What does 一生に一度 mean?", "once in a lifetime", ["once a week", "every day", "once a year"], "一生に一度 is いっしょうにいちど."),
                      M("What does 大人 mean?", "adult", ["child", "teacher", "university student"], "大人 is おとな: adult."), M("What does 大使館 mean?", "embassy", ["university", "bank", "school"], "大使館 is たいしかん: embassy."), M("What does 国会 mean?", "the Diet", ["a country", "a school", "a bank"], "国会 is こっかい: the Diet."),
                      M("What does 海外 mean?", "overseas", ["inside", "outside the room", "the sea"], "海外 is かいがい: overseas.")]),
)

# ================================================================= 3 practice
_MAP = [("レストラン・アルデンテ", "えきの中にあります。南口の近くです。", "d", "south of the station, by the south exit"), ("ロイヤルホテル", "えきの東口を出て、まっすぐ五分ぐらいです。", "f", "just east of the station"),
        ("山下先生のうち", "北口を出て、右へ十分ぐらいです。", "e", "north-east of the station"), ("こうえん", "西口をまっすぐ十五分ぐらい行ってください。", "a", "west of the station"), ("大学", "北口を出て、左へ十分ぐらい行ってください。", "b", "north-west of the station")]
_COMP = [("外国", "がいこく", "foreign country"), ("天気", "てんき", "weather"), ("先生", "せんせい", "teacher"), ("学生", "がくせい", "student"), ("大学", "だいがく", "university"), ("今日", "きょう", "today"), ("大学生", "だいがくせい", "university student"), ("外国人", "がいこくじん", "foreigner")]
L3 = lesson(
    "Kanji practice: compounds, a map and the bulletin board",
    "外国 · 天気 · 先生 · 大学 · えきの南口 · ホームステイ · じてんしゃ · ハロウィーンパーティー",
    requires=[],
    cards=[
        card("A. Make compound words", "The book gives ten kanji (気 生 外 先 学 天 日 国 今 大) and asks you to combine them into compound words; one kanji may be used more than once. The example is 外 + 国 → 外国. Words that can be made (my list):",
             tables=[ktable([(a, k, e) for k, a, e in _COMP], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Where is each place on the map?", "In the book, five places must be matched with the letters on a map of the area around a station. Station words: えき (station), 出る (to exit), まっすぐ (straight), 近く (near). The map has the station in the middle with north at the top. My reading of the map: the five places are the letters d, f, e, a and b.",
             tables=[table(["Place", "Description", "Letter"], [[n, t, f"{p} ({d})"] for n, t, p, d in _MAP], say=[])],
             examples=[D(t, f"{n}: " + {"d": "It is inside the station; it is near the south exit.", "f": "Leave the east exit and go straight for about five minutes.", "e": "Leave the north exit and go right for about ten minutes.", "a": "Go straight from the west exit for about fifteen minutes.", "b": "Leave the north exit and go left for about ten minutes."}[p]) for n, t, p, d in _MAP]),
        card("The bulletin board", "The book shows a bulletin board with six notices. Read it and answer four questions. The notices (dates and numbers are shown as printed):",
             tables=[table(["Notice", "What it says"], [["Homestay program", "Won’t you do a homestay in a town in Tohoku? December 28 (Sun) – January 3 (Sat). It is near beautiful mountains and a river."], ["English lessons wanted", "Please teach me English. A Japanese college student. 931-2682 Yoko"], ["Sale!!", "Bicycle ¥8,000. It is new. Please call. (7 p.m. – 11 p.m.) Yamada 597-1651"], ["Halloween party", "Place: Prof. Yamashita’s house. Time: from 6:00. You may bring a friend! Please bring something to drink."], ["Italian restaurant Mangiare", "Lunch ¥1,200. Set A (salad, coffee). Set B (bread, coffee)."], ["Guitar concert", "November 12 (Fri), 6:30 on. West Concert Hall (leave West Station exit 3, turn left, 3 minutes)."]], say=[]),
                     ],
             examples=[D("東北のまちでホームステイをしませんか。", "Won’t you do a homestay in a town in Tohoku?"), D("きれいな山と川の近くです。", "It is near beautiful mountains and a river."), D("えいごをおしえてください。", "Please teach me English."), D("日本人の大学生です。", "I am a Japanese college student."),
                       D("あたらしいです。でんわしてください。", "It is new. Please call."), D("ともだちをつれてきてもいいですよ。", "You may bring a friend."), D("飲みものをもってきてください。", "Please bring something to drink.")]),
        card("Questions on the board (my answers)", "1. To buy a bicycle, call Yamada (597-1651, between seven and eleven at night). 2. The party is at Prof. Yamashita’s house; bring something to drink. 3. To reach the concert hall, leave West Station exit 3, turn left and walk three minutes. 4. For the winter break you can do a homestay in Tohoku, from December 28 to January 3."),
    ],
    exercises=uniq(
        [M(f"What does {k} mean?", e, three([x for _, _, x in _COMP if x != e]), f"{k} is {a}.") for k, a, e in _COMP]
        + [M(f"How do you read {k}?", a, three([x for _, x, _ in _COMP if x != a]), f"{k} is {a}.") for k, a, e in _COMP]
        + [M(f"Which letter on the map is {n}?", p, three([x for _, _, x, _ in _MAP if x != p]), f"{t}") for n, t, p, d in _MAP]
        + [M("Who do you contact to buy the bicycle?", "Yamada", ["Yoko", "Prof. Yamashita", "Mangiare"], "The sale notice is signed Yamada."), M("How much is the bicycle?", "¥8,000", ["¥1,200", "¥800", "¥18,000"], "¥8,000."), M("Where will the Halloween party be held?", "at Prof. Yamashita’s house", ["at a restaurant", "at the university", "at a concert hall"], "ところ：山下先生のうち."),
           M("What should you bring to the Halloween party?", "something to drink", ["a bicycle", "an English book", "a guitar"], "飲みものをもってきてください."), M("How do you get to the concert hall?", "leave West Station exit 3 and turn left; 3 minutes", ["take the bus", "leave the north exit and go straight", "walk 30 minutes"], "西えき3出口を出て左へ3分."),
           M("What can you do for the winter break?", "a homestay in Tohoku", ["a concert in Vienna", "an English lesson", "a party at a restaurant"], "ホームステイ十二月二十八日〜一月三日."), M("What does the English notice ask for?", "English lessons from a Japanese college student", ["a bicycle", "a homestay", "a party"], "えいごをおしえてください."),
           M("What is in lunch set A at Mangiare?", "salad and coffee", ["bread and coffee", "pizza and wine", "ice cream and tea"], "Aセット (サラダ・コーヒー)."), M("What is in lunch set B at Mangiare?", "bread and coffee", ["salad and coffee", "pizza and wine", "ice cream and tea"], "Bセット (パン・コーヒー)."),
           F("えきの南口を___て、右へ五分ぐらいです。 (exit)", "出", ["入", "分", "先"], "出て."), F("北口を出て、___へ十分ぐらいです。 (right)", "右", ["左", "東", "南"], "右へ."), F("北口を出て、___へ十分ぐらい行ってください。 (left)", "左", ["右", "西", "北"], "左へ.")]
    ),
)

# ================================================================= 4 reading
_R = [("私のすきなレストランは、イタリアりょうりのマンジャーレです。", "My favorite restaurant is Mangiare, an Italian restaurant."), ("えきの南口を出て、右へ五分ぐらいです。", "Leave the station’s south exit and turn right; it is about five minutes."), ("ちいさいレストランです。", "It is a small restaurant."),
      ("シェフはイタリア人のアントニオさんです。", "The chef is Antonio, an Italian."), ("アントニオさんはとてもおもしろい人です。", "Antonio is a very interesting person."), ("アントニオさんのりょうりはとてもおいしいです。", "Antonio’s cooking is very delicious."),
      ("私はよくマンジャーレに行きます。", "I often go to Mangiare."), ("マンジャーレでワインを飲んで、ピザを食べます。", "At Mangiare I drink wine and eat pizza."), ("アイスクリームもおいしいです。", "The ice cream is delicious, too."),
      ("ここでいつもたくさん食べます。", "I always eat a lot here."), ("りょうりはやすいですから。", "Because the food is cheap."), ("外国人もたくさんきます。", "Many foreigners come, too."), ("みなさんもきてください。", "Please come, everyone.")]
L4 = lesson(
    "Reading: 私のすきなレストラン",
    "Chiaki’s favorite restaurant · イタリアりょうり · マンジャーレ · writing about a restaurant",
    requires=[],
    cards=[
        card("The passage", "Chiaki writes about her favorite restaurant. The book prints it vertically; here it is in lines. Words: イタリア (Italy), りょうり (cooking; dish), シェフ (chef), ワイン (wine), ピザ (pizza), いつも (always), みなさん (everyone).", examples=passage(_R)),
        card("A. Where is the restaurant?", "The book asks you to find the restaurant on a map. It is at the south exit of the station: leave 南口, turn right and walk about five minutes. On the book’s map that is the place marked c (my reading of the map)."),
        card("B. What does the writer have there?", "She has pizza, wine and ice cream. She does not mention spaghetti, beer or steak."),
        card("C. Choose the correct answer", "The book gives two choices in each sentence. The answers:",
             examples=[D("マンジャーレは ちいさい レストランです。", "Mangiare is a small restaurant. (not 大きい)"), D("マンジャーレは やすいです。", "Mangiare is cheap. (not たかい)"), D("アントニオさんは おもしろい 人です。", "Antonio is an interesting person. (not つまらない)"), D("マンジャーレに 外国人が きます。", "Foreigners come to Mangiare. (not きません)")]),
        card("Writing practice", "The book asks you to (A) write a flyer for a party you organize, with the kind of party, the start time, the place, what to bring and how to get there, and (B) write about your favorite restaurant. A sample of mine for B (not the book’s):",
             examples=passage([("わたしのすきなレストランはイタリアりょうりのレストランです。", "My favorite restaurant is an Italian restaurant."), ("えきの北口を出て、左へ三分ぐらいです。", "Leave the north exit of the station and turn left; it is about three minutes."), ("やすくて、おいしいです。", "It is cheap and delicious."), ("ともだちとよくいきます。", "I often go with my friends.")])),
    ],
    exercises=uniq(
        [M("What kind of restaurant is Mangiare?", "Italian", ["Chinese", "Korean", "Japanese"], "イタリアりょうり."), M("How do you get there from the station?", "leave the south exit and go right for about five minutes", ["leave the north exit and go left", "go straight from the west exit", "take a bus"], "南口を出て、右へ五分ぐらい."),
         M("How is the restaurant?", "small", ["big", "new", "old"], "ちいさいレストラン."), M("Who is the chef?", "Antonio, an Italian", ["Chiaki", "a Japanese man", "a Korean woman"], "シェフはイタリア人のアントニオさん."), M("What kind of person is Antonio?", "very interesting", ["boring", "quiet", "tall"], "とてもおもしろい人."),
         M("How is Antonio’s cooking?", "very delicious", ["so-so", "expensive", "bad"], "とてもおいしい."), M("What does Chiaki drink at Mangiare?", "wine", ["beer", "coffee", "tea"], "ワインを飲んで."), M("What does Chiaki eat at Mangiare?", "pizza and ice cream", ["spaghetti and steak", "cake", "sandwiches"], "ピザ and アイスクリーム."),
         M("Why does Chiaki always eat a lot there?", "the food is cheap", ["the chef is her friend", "it is near her house", "it is on sale"], "りょうりはやすいですから."), M("Who else goes there?", "foreigners, too", ["no one", "only Japanese people", "only students"], "外国人もたくさんきます."),
         M("What does みなさん mean?", "everyone", ["always", "a chef", "pizza"], "みなさん is “everyone”."), M("What does いつも mean?", "always", ["everyone", "often", "again"], "いつも is “always”."), M("What does りょうり mean?", "cooking; dish", ["wine", "chef", "Italy"], "りょうり is “cooking; dish”."),
         M("What does シェフ mean?", "chef", ["wine", "everyone", "Italy"], "シェフ is a chef."), M("What does イタリア mean?", "Italy", ["India", "Ireland", "Israel"], "イタリア is Italy."), M("What does ワイン mean?", "wine", ["wind", "water", "line"], "ワイン is wine."),
         F("マンジャーレは___レストランです。 (small)", "ちいさい", ["おおきい", "たかい", "あたらしい"], "ちいさい."), F("マンジャーレは___です。 (cheap)", "やすい", ["たかい", "つまらない", "おもしろい"], "やすい."), F("アントニオさんはおもしろい___です。 (person)", "人", ["本", "分", "国"], "人."),
         F("マンジャーレに外国人が___。 (come)", "きます", ["きません", "いません", "ありません"], "きます.")]
    ),
)

UNIT = unit("Genki I, Reading & Writing 6: My Favorite Restaurant", [L1, L2, L3, L4])

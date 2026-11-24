"""Unit 42: Genki II, Reading and Writing, Lesson 18 "College Life" (大学生活), pp. 308-314.
Original lessons following the scope of Genki: An Integrated Course in Elementary Japanese II (2nd edition, 2011).
The book's audio, pictures and handwriting tasks are left out; the explanations and the answers are mine."""
from dsl_ja import *
from ja_unit4 import three
import ja_kanji as J

_KANJI = J.parse("""
目|eye|もく|め|5|目的(もくてき)=purpose;目(め)=eyes;目薬(めぐすり)=eye drops;二番目(にばんめ)=the second;目上の人(めうえのひと)=one’s superiors
的|target, -ish|てき|まと|8|目的(もくてき)=purpose;現代的(げんだいてき)=modern;社会的(しゃかいてき)=social;的(まと)=target
力|power|りょく・りき|ちから|2|力仕事(ちからしごと)=physical labor such as construction;協力(きょうりょく)=cooperation;努力(どりょく)=endeavor;力士(りきし)=sumo wrestler
洋|ocean, overseas|よう|-|9|洋服(ようふく)=clothes;東洋(とうよう)=the East;洋食(ようしょく)=Western food;大西洋(たいせいよう)=the Atlantic
服|clothes|ふく|-|8|服(ふく)=clothes;洋服(ようふく)=Western clothes;制服(せいふく)=uniform;和服(わふく)=Japanese clothes
堂|hall|どう|-|11|食堂(しょくどう)=dining room;公会堂(こうかいどう)=public hall;堂々とした(どうどうとした)=dignified
授|to instruct|じゅ|さず|11|授業(じゅぎょう)=class;教授(きょうじゅ)=professor;授かる(さずかる)=to be given
業|business, vocation|ぎょう|-|13|授業(じゅぎょう)=class;職業(しょくぎょう)=occupation;産業(さんぎょう)=industry;サービス業(サービスぎょう)=service industry
試|test, to try|し|こころ|13|試験(しけん)=exam;試合(しあい)=game, match;入試(にゅうし)=entrance exam;試みる(こころみる)=to try
験|to examine|けん|-|18|試験(しけん)=exam;実験(じっけん)=experiment;経験(けいけん)=experience;受験(じゅけん)=taking an examination
貸|to lend, loan|たい|か|12|貸す(かす)=to lend;貸し出し(かしだし)=lending;賃貸マンション(ちんたいマンション)=apartment for rent
図|drawing, to devise|と・ず|はか|7|図書館(としょかん)=library;地図(ちず)=map;図(ず)=figure;合図(あいず)=signal;図る(はかる)=to attempt
館|building, hall|かん|-|16|図書館(としょかん)=library;映画館(えいがかん)=movie theater;旅館(りょかん)=Japanese inn;大使館(たいしかん)=embassy
終|end|しゅう|お|11|終わる(おわる)=to come to an end;終わり(おわり)=end;終点(しゅうてん)=last stop;最終(さいしゅう)=the last
宿|inn, to lodge in|しゅく|やど|11|宿題(しゅくだい)=homework;下宿(げしゅく)=boardinghouse;宿泊(しゅくはく)=lodging;宿(やど)=inn
題|title, topic|だい|-|18|宿題(しゅくだい)=homework;問題(もんだい)=problem, question;話題(わだい)=topic of conversation;題(だい)=title
""")
_K1 = _KANJI[:8]
_K2 = _KANJI[8:]


def rd(k, r, wrong, en):
    return M(f"How do you read {k}?", r, wrong, f"{k} is {r}: {en}.")


# ================================================================= 1 kanji 目 to 業
L1 = lesson(
    "Kanji: 目 的 力 洋 服 堂 授 業",
    "目 · 的 · 力 · 洋 · 服 · 堂 · 授 · 業 · eye, target, power, ocean, clothes, hall, instruct, business",
    requires=[],
    cards=[
        card("College Life: new kanji", "Lesson 18 of the Reading and Writing section of Genki II (大学生活, College Life) teaches 目 的 力 洋 服 堂 授 業 試 験 貸 図 館 終 宿 題, sixteen new kanji. The first eight are here. The reading practice is a look at part-time jobs of Japanese university students (with graphs), and an article about the student life of Hashimoto-kun."),
        *J.kanji_cards(_K1, per=4),
        card("Words for college life", "目的 (もくてき) is “purpose”, 力仕事 (ちからしごと) is physical labor, 洋服 (ようふく) is “clothes” (Western clothes), 食堂 (しょくどう) is a dining hall or cafeteria, and 授業 (じゅぎょう) is a class.",
             tables=[ktable([("もくてき", "目的", "purpose"), ("め", "目", "eye"), ("にばんめ", "二番目", "the second"), ("めうえのひと", "目上の人", "one’s superiors"), ("げんだいてき", "現代的", "modern"), ("しゃかいてき", "社会的", "social"), ("ちからしごと", "力仕事", "physical labor"), ("きょうりょく", "協力", "cooperation"), ("どりょく", "努力", "endeavor"), ("ようふく", "洋服", "clothes"), ("とうよう", "東洋", "the East"), ("せいふく", "制服", "uniform"), ("わふく", "和服", "Japanese clothes"), ("しょくどう", "食堂", "dining room"), ("じゅぎょう", "授業", "class"), ("きょうじゅ", "教授", "professor"), ("しょくぎょう", "職業", "occupation"), ("さんぎょう", "産業", "industry")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K1, _KANJI)
                   + [rd("目的", "もくてき", ["めまと", "めてき", "もくまと"], "purpose"), rd("目薬", "めぐすり", ["もくやく", "めやく", "めくすり"], "eye drops"), rd("二番目", "にばんめ", ["にばんもく", "ふたばんめ", "にばんめん"], "the second"), rd("目上の人", "めうえのひと", ["もくじょうのひと", "めじょうのひと", "めうえのにん"], "one’s superiors"),
                      rd("現代的", "げんだいてき", ["げんだいまと", "げんたいてき", "げんだいてきな"], "modern"), rd("社会的", "しゃかいてき", ["しゃかいまと", "しゃがいてき", "しゃかいでき"], "social"), rd("的", "まと", ["てき", "まど", "てい"], "target"),
                      rd("力仕事", "ちからしごと", ["りょくしごと", "りきしごと", "ちからじごと"], "physical labor"), rd("協力", "きょうりょく", ["きょうちから", "きょうりき", "きょりょく"], "cooperation"), rd("努力", "どりょく", ["どちから", "どりき", "どうりょく"], "endeavor"), rd("力士", "りきし", ["りょくし", "ちからし", "りきじ"], "sumo wrestler"),
                      rd("洋服", "ようふく", ["ようぶく", "ようふ", "よふく"], "clothes"), rd("東洋", "とうよう", ["ひがしよう", "どうよう", "とうゆう"], "the East"), rd("洋食", "ようしょく", ["ようじき", "ようしょ", "よしょく"], "Western food"), rd("大西洋", "たいせいよう", ["だいせいよう", "たいさいよう", "おおにしよう"], "the Atlantic"),
                      rd("制服", "せいふく", ["せいぶく", "せふく", "せいふう"], "uniform"), rd("和服", "わふく", ["かふく", "わぶく", "なごふく"], "Japanese clothes"),
                      rd("食堂", "しょくどう", ["しょくどお", "たべどう", "しょくとう"], "dining room"), rd("公会堂", "こうかいどう", ["こうえどう", "こうかいとう", "くかいどう"], "public hall"), rd("堂々とした", "どうどうとした", ["どうとうとした", "どうどとした", "どどうとした"], "dignified"),
                      rd("授業", "じゅぎょう", ["じゅうぎょう", "じゅぎょ", "さずぎょう"], "class"), rd("教授", "きょうじゅ", ["きょうじゅう", "きょじゅ", "おしじゅ"], "professor"), rd("授かる", "さずかる", ["じゅかる", "さずがる", "さずくる"], "to be given"),
                      rd("職業", "しょくぎょう", ["しょくごう", "しきぎょう", "しょくぎょ"], "occupation"), rd("産業", "さんぎょう", ["さんごう", "さんぎょ", "さんぎょお"], "industry"), rd("サービス業", "サービスぎょう", ["サービスごう", "サービスわざ", "サービスぎょ"], "service industry"),
                      M("What does 目的 mean?", "purpose", ["eye", "class", "clothes"], "目的 is もくてき."), M("What does 授業 mean?", "class", ["homework", "exam", "library"], "授業 is じゅぎょう."), M("What does 洋服 mean?", "clothes", ["food", "uniform only", "kimono only"], "洋服 is ようふく.")]),
)

# ================================================================= 2 kanji 試 to 題
L2 = lesson(
    "Kanji: 試 験 貸 図 館 終 宿 題",
    "試 · 験 · 貸 · 図 · 館 · 終 · 宿 · 題 · test, examine, lend, drawing, building, end, inn, title",
    requires=[],
    cards=[
        *J.kanji_cards(_K2, per=4),
        card("Words for college life", "試験 (しけん) is an exam, 貸す (かす) is “to lend”, 図書館 (としょかん) is a library, 終わる is “to end”, 宿題 (しゅくだい) is homework and 問題 (もんだい) is a problem or question.",
             tables=[ktable([("しけん", "試験", "exam"), ("しあい", "試合", "game, match"), ("にゅうし", "入試", "entrance exam"), ("こころみる", "試みる", "to try"), ("じっけん", "実験", "experiment"), ("けいけん", "経験", "experience"), ("じゅけん", "受験", "taking an examination"), ("かす", "貸す", "to lend"), ("かしだし", "貸し出し", "lending"), ("ちんたいマンション", "賃貸マンション", "apartment for rent"), ("としょかん", "図書館", "library"), ("ちず", "地図", "map"), ("あいず", "合図", "signal"), ("えいがかん", "映画館", "movie theater"), ("りょかん", "旅館", "Japanese inn"), ("たいしかん", "大使館", "embassy"), ("おわる", "終わる", "to come to an end"), ("しゅうてん", "終点", "last stop"), ("しゅくだい", "宿題", "homework"), ("げしゅく", "下宿", "boardinghouse"), ("もんだい", "問題", "problem, question"), ("わだい", "話題", "topic of conversation")], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(J.kanji_exercises(_K2, _KANJI)
                   + [rd("試験", "しけん", ["こころけん", "しげん", "しきん"], "exam"), rd("試合", "しあい", ["しごう", "こころあい", "しあう"], "game, match"), rd("入試", "にゅうし", ["いりし", "にゅうしけん", "にゅし"], "entrance exam"), rd("試みる", "こころみる", ["ためみる", "しみる", "こころめる"], "to try"),
                      rd("実験", "じっけん", ["じつけん", "みげん", "じっげん"], "experiment"), rd("経験", "けいけん", ["けいげん", "きょうけん", "へけん"], "experience"), rd("受験", "じゅけん", ["うけけん", "じゅうけん", "じゅげん"], "taking an examination"),
                      rd("貸す", "かす", ["たいす", "かる", "かせ"], "to lend"), rd("貸し出し", "かしだし", ["たいしだし", "かしでし", "かりだし"], "lending"), rd("賃貸マンション", "ちんたいマンション", ["ちんかしマンション", "ちんだいマンション", "ちたいマンション"], "apartment for rent"),
                      rd("図書館", "としょかん", ["ずしょかん", "としょうかん", "ずとかん"], "library"), rd("地図", "ちず", ["ちと", "じず", "ちづ"], "map"), rd("合図", "あいず", ["ごうず", "あいと", "あいづ"], "signal"), rd("図る", "はかる", ["ずる", "とる", "はからる"], "to attempt"),
                      rd("映画館", "えいがかん", ["えいがやかた", "えいがかい", "えがかん"], "movie theater"), rd("旅館", "りょかん", ["たびかん", "りょうかん", "りょがん"], "Japanese inn"), rd("大使館", "たいしかん", ["だいしかん", "たいしやかた", "おおしかん"], "embassy"),
                      rd("終わる", "おわる", ["しゅうわる", "おわろ", "おえる"], "to come to an end"), rd("終わり", "おわり", ["しゅうり", "おえり", "おわる"], "end"), rd("終点", "しゅうてん", ["おわりてん", "しゅてん", "しゅうでん"], "last stop"), rd("最終", "さいしゅう", ["さいおわり", "さいしゅ", "さいじゅう"], "the last"),
                      rd("宿題", "しゅくだい", ["やどだい", "しゅくだ", "しゅうだい"], "homework"), rd("下宿", "げしゅく", ["したやど", "かしゅく", "げじゅく"], "boardinghouse"), rd("宿泊", "しゅくはく", ["やどはく", "しゅくばく", "しゅうはく"], "lodging"), rd("宿", "やど", ["しゅく", "やと", "やどう"], "inn"),
                      rd("問題", "もんだい", ["もんたい", "とだい", "もんだ"], "problem, question"), rd("話題", "わだい", ["はなしだい", "わたい", "はなだい"], "topic of conversation"), rd("題", "だい", ["たい", "だ", "てい"], "title"),
                      M("What does 試験 mean?", "exam", ["homework", "library", "experiment only"], "試験 is しけん."), M("What does 宿題 mean?", "homework", ["inn", "exam", "class"], "宿題 is しゅくだい."), M("What does 貸す mean?", "to lend", ["to borrow", "to end", "to try"], "貸す is かす.")]),
)

# ================================================================= 3 kanji practice
_NEW = [("女子", "じょし", "girl, female"), ("男子", "だんし", "boy, male"), ("以上", "いじょう", "or more"), ("電気代", "でんきだい", "charge for electricity"), ("入れる", "いれる", "to put in"), ("毎月", "まいつき", "every month"), ("食堂", "しょくどう", "dining room"), ("三日", "みっか", "three days; the third"), ("空手", "からて", "karate"), ("親しい", "したしい", "close, intimate"), ("来週", "らいしゅう", "next week"), ("図書館", "としょかん", "library")]
_PB = [("学生", "がくせい", "student"), ("店", "みせ", "shop"), ("旅行", "りょこう", "trip"), ("一か月", "いっかげつ", "one month"), ("生活", "せいかつ", "life, living"), ("飲む", "のむ", "to drink"), ("楽しみ", "たのしみ", "looking forward")]
L3 = lesson(
    "Kanji practice: new readings and review",
    "女子 · 男子 · 以上 · 電気代 · 入れる · 毎月 · 食堂 · 三日 · 空手 · 親しい · 来週 · 図書館 · 学生 · 店 · 旅行 · 生活",
    requires=[],
    cards=[
        card("A. New readings of kanji you know", "The book lists twelve words with readings to learn (the bold part is new). The numbers in the book refer to the kanji lists of Genki I and II (子 060, 男 039, 入 072, 月 019, 食 042, 三 003, 日 016, 空 156, 親 166, 書 093).",
             tables=[ktable([(a, b, c) for b, a, c in _NEW], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("B. Read these kanji", "The book gives seven words to read. Tap a reading to hear it. The book prints the same answers at the bottom of the page:",
             tables=[ktable([(a, b, c) for b, a, c in _PB], headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
    ],
    exercises=uniq(
        [rd(k, r, three([x[1] for x in _NEW + _PB if x[1] != r]), e) for k, r, e in _NEW + _PB]
        + [M(f"Which word means “{e}”?", k, three([x[0] for x in _NEW + _PB if x[0] != k]), f"{k} is {r}.") for k, r, e in _NEW + _PB]
        + [M("How do you read 子 in 女子?", "し", ["こ", "ね", "じ"], "女子 is じょし."), M("How do you read 日 in 三日?", "か", ["にち", "ひ", "び"], "三日 is みっか.")]
    ),
)

# ================================================================= 4 part-time jobs
_LV = [("もくてき", "目的", "object; purpose"), ("じきゅう", "時給", "an hourly wage"), ("じょしがくせい", "女子学生", "female student"), ("だんしがくせい", "男子学生", "male student"), ("せいかつのゆとり", "生活のゆとり", "extra money to spare for the cost of living"), ("ようふく", "洋服", "clothes"), ("せいかつひ", "生活費", "the cost of living"), ("ちょきん", "貯金", "savings"), ("いじょう", "〜以上", "…or more")]
_GA = [["アルバイトをしている", "六十五パーセント", "65%"], ["アルバイトをしていない", "三十五パーセント", "35%"]]
_GB = [["~699円", "2%"], ["700~899円", "41%"], ["900~1099円", "32%"], ["1100~1299円", "8%"], ["1300円~", "17%"]]
_GC = [["生活のゆとりがほしい", "21%", "24%"], ["洋服が買いたい", "34%", "20%"], ["生活費", "19%", "20%"], ["サークルで使う", "18%", "18%"], ["旅行したい", "23%", "15%"], ["貯金したい", "18%", "14%"]]
L4 = lesson(
    "Reading: 大学生のアルバイト (University Students’ Part-time Jobs)",
    "アルバイトをしていますか · アルバイトの時給 · アルバイトの目的 · 女子学生と男子学生",
    requires=[],
    cards=[
        card("Words for the graphs", "The book’s vocabulary list for 大学生のアルバイト.", tables=[ktable(_LV, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. Before reading", "The book asks: 1. Have you ever had a part-time job? What kind of job did you/do you have? (どんなアルバイトをしましたか／していますか。) 2. What is the purpose of your part-time job? (あなたのアルバイトの目的は何ですか。) 3. What part-time job is popular in your country? (あなたの国で人気があるアルバイトは何ですか。) Your own answers will vary."),
        card("B. The graphs", "日本の大学生のアルバイトについて調べました。下のグラフを見て、質問に答えてください。 The book shows three graphs from a survey of Japanese university students (the 44th national survey of student life, 2008, by the National Federation of University Co-operative Associations). Here they are as tables. Graph 1: アルバイトをしていますか (Do you have a part-time job?)",
             tables=[table(["Answer", "Percent"], [[a, c] for a, b, c in _GA], say=[], title="")]),
        card("The hourly wage and the purposes", "Graph 2: アルバイトの時給 (the hourly wage of the part-time job, in yen). Graph 3: アルバイトの目的 (the purpose of the part-time job; the percent of female students and of male students who chose each purpose).",
             tables=[table(["Hourly wage", "Percent"], _GB, say=[], title=""), table(["Purpose", "Female students", "Male students"], _GC, say=[], title="")]),
        card("B. Questions about the graphs", "The book gives four questions. My answers (worked out from the graphs):",
             examples=[D("アルバイトをしている人のほうが多いです。六十五パーセントです。", "Arubaito o shite iru hito no hoo ga ooi desu. Rokujuugo paasento desu — 1. Which are more, people with a part-time job or without? Those with one: 65%."), D("十七パーセントです。", "Juunana paasento desu — 2. What percent get an hourly wage of 1300 yen or more? 17%."), D("洋服が買いたいです。三十四パーセントです。", "Yoofuku ga kaitai desu. Sanjuuyon paasento desu — 3. What is the most common purpose for female students? Wanting to buy clothes (34%)."), D("生活のゆとりがほしいです。二十四パーセントです。", "Seekatsu no yutori ga hoshii desu. Nijuuyon paasento desu — 4. What is the most common purpose for male students? Wanting extra money for living (24%).")]),
    ],
    exercises=uniq(
        [M("What percent of the students have a part-time job?", "65%", ["35%", "41%", "17%"], "はい 65%."), M("What percent do not have a part-time job?", "35%", ["65%", "2%", "8%"], "いいえ 35%."), M("Which hourly wage range is the most common?", "700 to 899 yen", ["900 to 1099 yen", "1300 yen or more", "699 yen or less"], "41%."), M("What percent get 1300 yen or more?", "17%", ["8%", "32%", "2%"], "1300円~ 17%."), M("What percent get 699 yen or less?", "2%", ["8%", "17%", "41%"], "~699円 2%."),
         M("What is the top purpose for female students?", "to buy clothes", ["to travel", "to save", "to pay for circles"], "洋服が買いたい 34%."), M("What is the top purpose for male students?", "extra money for living", ["to buy clothes", "to travel", "to save"], "生活のゆとりがほしい 24%."), M("Which purpose do female and male students share exactly (18% each)?", "spending at circles", ["travel", "clothes", "savings"], "サークルで使う 18% / 18%."), M("Which purpose has the biggest gap between female and male students?", "wanting to buy clothes (34% vs 20%)", ["savings", "living costs", "circles"], "洋服が買いたい."),
         M("What does 時給 mean?", "an hourly wage", ["a salary", "working hours", "overtime"], "時給."), M("What does 貯金 mean?", "savings", ["money", "a bank", "a debt"], "貯金."), M("What does 生活費 mean?", "the cost of living", ["a living room", "a party fee", "a ticket price"], "生活費."), M("What does 目的 mean?", "purpose", ["target", "goal line", "eye"], "目的."),
         F("日本の大学生のアルバイトについて___ました。 (investigated)", "調べ", ["読み", "書き", "借り"], "調べました."), F("アルバイトをしている人___多いです。", "のほうが", ["のとき", "のまま", "のため"], "のほうが多い."), F("時給1300円以上もらっている人は何___ですか。", "パーセント", ["ぐらい", "ばかり", "ずつ"], "何パーセント.")]
    ),
)

# ================================================================= 5 Hashimoto-kun
_LV2 = [("ワンルームマンション", "", "one-room apartment; a studio"), ("しょくひ", "食費", "food cost"), ("だい", "〜代", "charge; fee"), ("でんきだい", "電気代", "charge for electricity"), ("まいつき", "毎月", "every month"), ("かていきょうし", "家庭教師", "tutor"), ("ひっこし", "引っ越し", "moving"), ("ちからしごと", "力仕事", "physical labor such as construction"), ("はじめは", "初めは", "at first"), ("したしい", "親しい", "close; intimate")]
_H1 = [("橋本くんは大学三年生だ。大学の近くのワンルームマンションに住んでいる。家賃は一か月五万円だ。食費、電気代などを入れて、一か月の生活費は、十万円ぐらいだ。毎月、両親が八万円送ってくれる。", "Hashimoto-kun is a third-year university student. He lives in a one-room apartment near the university. The rent is 50,000 yen a month. Including food, electricity and so on, his living costs for a month are about 100,000 yen. Every month his parents send him 80,000 yen. (This article is in the short form, a formal style used in newspapers.)"),
       ("今、家庭教師をしたり、大学の食堂でアルバイトをしたりしている。家庭教師は一週間に一回、食堂は三日だ。時々、引っ越しなどの力仕事もする。アルバイトをしながら勉強するのは大変だ。よく遅刻したり、授業をサボったりしてしまう。", "Now he works as a tutor and does a part-time job in the university cafeteria. The tutoring is once a week and the cafeteria three days. Sometimes he also does physical labor such as helping people move. It is hard to study while doing part-time jobs. He often ends up being late and skipping classes."),
       ("橋本くんは空手のサークルに入っている。一週間に三日、練習をする。また、時々サークルのみんなと飲みに行く。「大きらいなお酒を飲まなきゃいけないから、初めはあまり行きたくなかったんです。でも、そのおかげで、先輩たちと親しくなれたし、今の彼女にも会えたんですよ。」", "Hashimoto-kun belongs to a karate club. He practices three days a week. Also, sometimes he goes drinking with the club members. “Because I have to drink alcohol, which I hate, I didn’t really want to go at first. But thanks to that I was able to become close with the seniors, and I was even able to meet my present girlfriend.”"),
       ("来週から試験が始まる。同じクラスの友だちにノートを貸してもらって、図書館で勉強するつもりだ。「もっと早く勉強を始めればよかった」と思っている。橋本くんは今、試験が終わってから、サークルのみんなと旅行に行くのを楽しみにしている。", "Exams start next week. He plans to have a friend in the same class lend him notes and study at the library. He thinks, “I should have started studying earlier.” Hashimoto-kun is now looking forward to going on a trip with the club members after the exams are over.")]
L5 = lesson(
    "Reading: 橋本くんの大学生活 (Hashimoto-kun’s College Life)",
    "ワンルームマンション · 家庭教師 · 食堂のアルバイト · 空手のサークル · 試験",
    requires=[],
    cards=[
        card("Words for the article", "The book’s vocabulary list for 橋本くんの大学生活.", tables=[ktable(_LV2, headers=("Reading", "Kanji", "Romaji", "Meaning"))]),
        card("A. A newspaper article about a university student", "ある新聞が大学生の橋本くんの生活を紹介しています。 Note (the book’s footnote): this passage is written in the short form, which expresses formality rather than casualness, as expected in journalistic and scholarly articles. Tap a paragraph to hear it.", examples=passage(_H1)),
    ],
    exercises=uniq(
        [M("What year of university is Hashimoto-kun in?", "third year", ["first year", "second year", "fourth year"], "大学三年生."), M("How much is his monthly rent?", "50,000 yen", ["80,000 yen", "100,000 yen", "30,000 yen"], "家賃は一か月五万円."), M("About how much are his monthly living costs?", "100,000 yen", ["50,000 yen", "80,000 yen", "200,000 yen"], "生活費は十万円ぐらい."), M("How much do his parents send each month?", "80,000 yen", ["50,000 yen", "100,000 yen", "30,000 yen"], "八万円送ってくれる."),
         M("What part-time jobs does he have?", "tutor, cafeteria and physical labor", ["convenience store only", "karate teacher", "newspaper delivery"], "家庭教師、食堂、力仕事."), M("How often does he tutor?", "once a week", ["three days a week", "every day", "once a month"], "一週間に一回."), M("How many days does he work in the cafeteria?", "three days a week", ["once a week", "five days a week", "every day"], "食堂は三日."),
         M("What happens because he works so much?", "he is often late and skips classes", ["he fails every exam", "he quits the circle", "he moves out"], "遅刻したり、授業をサボったり."), M("What circle is he in?", "karate", ["tennis", "music", "English"], "空手のサークル."), M("How often does he practice?", "three days a week", ["every day", "once a week", "twice a month"], "一週間に三日."),
         M("Why didn’t he want to go drinking at first?", "he hates alcohol but has to drink it", ["he has no money", "he is busy", "he is a minor"], "大きらいなお酒を飲まなきゃいけない."), M("What good thing came from going drinking?", "he became close with seniors and met his girlfriend", ["he got a job", "he lost weight", "he won a trophy"], "先輩たちと親しくなれたし、今の彼女にも会えた."), M("When do exams start?", "next week", ["today", "next month", "next year"], "来週から試験が始まる."), M("How will he study for the exams?", "borrow notes from a friend and study at the library", ["hire a tutor", "skip them", "study at the cafeteria"], "ノートを貸してもらって、図書館で勉強."), M("What is he looking forward to?", "a trip with the circle after the exams", ["summer vacation alone", "a part-time job", "a karate contest"], "旅行に行くのを楽しみにしている."),
         M("What does 家庭教師 mean?", "tutor", ["homeroom teacher", "cooking teacher", "professor"], "家庭教師."), M("What does 引っ越し mean?", "moving", ["travelling", "shopping", "cleaning"], "引っ越し."), M("What does 初めは mean?", "at first", ["at last", "always", "sometimes"], "初めは."), M("What does 親しい mean?", "close, intimate", ["strict", "far", "kind only"], "親しい."),
         F("毎月、両親が八万円送って___。 (for me)", "くれる", ["あげる", "もらう", "やる"], "送ってくれる."), F("ノートを友だちに貸して___、図書館で勉強するつもりだ。", "もらって", ["あげて", "くれて", "やって"], "貸してもらって."), F("もっと早く勉強を始め___よかった。", "ればよかった", ["てよかった", "たよかった", "るよかった"], "始めればよかった."), F("試験が___から、旅行に行くのを楽しみにしている。 (finishes)", "終わって", ["始まって", "貸して", "借りて"], "終わってから.")]
    ),
)

# ================================================================= 6 questions, living costs, self-check and writing
_QB = [("1. 橋本くんはどんな所に住んでいますか。", "大学の近くのワンルームマンションに住んでいます。家賃は一か月五万円です。", "Where does Hashimoto-kun live? In a one-room apartment near the university; the rent is 50,000 yen a month."),
       ("2. 橋本くんはどんなアルバイトをしていますか。", "家庭教師をしたり、大学の食堂でアルバイトをしたり、時々引っ越しなどの力仕事をしたりしています。", "What part-time jobs does he have? Tutoring, the university cafeteria, and sometimes physical labor such as moving."),
       ("3. 橋本くんはアルバイトをしなかったら、家賃が払えませんか。", "いいえ、払えます。両親が毎月八万円送ってくれて、家賃は五万円ですから。", "If he didn’t work part-time, could he not pay his rent? No, he could. His parents send 80,000 yen each month and the rent is 50,000 yen."),
       ("4. 橋本くんはいい学生だと思いますか。どうしてですか。", "あまりいい学生ではないと思います。よく遅刻したり、授業をサボったりしてしまうからです。", "Do you think he is a good student? Why? (my sample) I don’t think he is a very good student, because he is often late and skips classes."),
       ("5. 橋本くんはサークルの友だちと飲みに行って、どんないいことがありましたか。", "先輩たちと親しくなれたし、今の彼女にも会えました。", "What good things happened when he went drinking with the circle friends? He became close with the seniors and met his girlfriend."),
       ("6. 橋本くんは、今、何をしなければいけませんか。", "来週から試験が始まるので、勉強しなければいけません。", "What must he do now? Exams start next week, so he must study.")]
_CT = [["食費", "24,430円", "24,430円"], ["家賃・電気代など", "54,720円", "54,720円"], ["本代", "2,410円", "2,410円"], ["電車・バス代など", "3,450円", "3,450円"], ["電話代", "5,090円", "5,090円"], ["その他", "33,820円", "33,820円"], ["計", "123,920円", "123,920円"]]
_DS = [("授業を聞きながら、時々寝てしまう。", "I sometimes fall asleep while listening to class."), ("今年、五回以上授業をサボってしまった。", "This year I have skipped class more than five times."), ("よく朝寝坊をする。", "I often oversleep."), ("よく友だちに宿題を見せてもらう。", "I often have friends show me their homework."), ("よく宿題を忘れる。", "I often forget my homework."), ("よく授業に遅刻する。", "I am often late for class."), ("やさしい先生のほうがきびしい先生より好きだ。", "I like kind teachers better than strict teachers."), ("試験の後、「もっと勉強すればよかった」とよく思う。", "After exams I often think, “I should have studied more.”")]
_WA = [("私の友だちのマリアは大学二年生で、大学の近くのアパートに一人で住んでいる。毎日、授業が終わってから、図書館で二時間ぐらい勉強する。週末は、レストランでアルバイトをして、生活費を稼いでいる。友だちが多くて、よくサークルのみんなと旅行に行く。いつも元気で、私の味方だ。", "My friend Maria is a second-year university student and lives alone in an apartment near the university. Every day after classes she studies at the library for about two hours. On weekends she works part-time at a restaurant and earns her living expenses. She has many friends and often goes on trips with the club members. She is always cheerful and on my side. (my sample, written in the short form like the article; the book asks you to write about your friends’ lives)")]
L6 = lesson(
    "Questions, living costs, self-check and writing practice",
    "橋本くんについての質問 · 学生の生活費 · あなたはいい学生ですか · 友だちの生活について書きましょう · アンケート",
    requires=[],
    cards=[
        card("B. Questions about the article", "The book gives six questions. My answers (the opinion in 4 is my sample):", examples=[D(a, f"{q} ({e})") for q, a, e in _QB]),
        card("C. 生活費 (living costs)", "下は一人で生活している大学生の生活費です。あなたはいくらぐらい使いますか。生活費を書きましょう。 The book gives the monthly living costs of Japanese university students who live alone (from the same 2008 survey) and a blank column for your own costs, which you fill in yourself. The total is 123,920 yen, which is close to the 100,000 yen of Hashimoto-kun (the figures add up: 24,430 + 54,720 + 2,410 + 3,450 + 5,090 + 33,820 = 123,920).",
             tables=[table(["Item", "Japanese university students", "Your costs"], [[a, b, "円"] for a, b, c in _CT], say=[], title="")]),
        card("D. Are you a good student?", "次の文を読んで、あなたがすること／そう思うことに○、しないこと／そう思わないことに×を書いてください。 Read the eight sentences and mark ○ for what you do or think, and × for what you do not do or do not think. The answers are personal. Then count your ○.",
             examples=[D(a, f"{n}. {e}") for n, (a, e) in enumerate(_DS, 1)]),
        card("D. Your score", "いくつ○がありましたか。 The book’s scoring (the Japanese result, then the meaning in English):",
             tables=[table(["Number of ○", "Result", "Meaning"], [["7-8", "とても悪い学生", "a very bad student"], ["5-6", "悪い学生", "a bad student"], ["3-4", "普通の学生", "an average student (普通 = average)"], ["1-2", "いい学生", "a good student"], ["0", "とてもいい学生", "a very good student"]], say=[], title="")]),
        card("IV. A. 書く練習 (Writing practice): your friends’ lives", "あなたの友だちの生活について書きましょう。 Your own text is up to you. My sample (not the book’s):", examples=passage(_WA)),
        card("IV. B. 書く練習 (Writing practice): a survey", "興味があることについてアンケートを作って聞きましょう。アンケートの後で、わかったことを書きましょう。 The book asks you to make a questionnaire (アンケート) about something you are interested in, ask your classmates, and then write what you found out. A sample plan: choose a topic (for example, hobbies), write about five questions such as 「週末に何をしますか」, ask five people, count the answers and write the results in the short form, for example 「五人のうち三人が、週末に友だちと遊ぶと答えた。」",
             examples=[D("五人のうち三人が、週末に友だちと遊ぶと答えた。", "Gonin no uchi sannin ga, shuumatsu ni tomodachi to asobu to kotaeta — Out of five people, three answered that they play with friends on weekends. (my sample)")]),
    ],
    exercises=uniq(
        [M(f"How do you answer: {q}", a, three([x[1] for x in _QB if x[1] != a]), q) for q, a, e in _QB]
        + [M("What is the largest item in the living costs of Japanese students?", "rent and electricity (54,720 yen)", ["food", "phone", "books"], "家賃・電気代など 54,720円."), M("How much do Japanese students spend on books per month in the table?", "2,410 yen", ["5,090 yen", "24,430 yen", "3,450 yen"], "本代 2,410円."), M("What is the total of the living costs?", "123,920 yen", ["100,000 yen", "54,720 yen", "80,000 yen"], "計 123,920円."),
           M("In the self-check, what does 7 or 8 ○ mean?", "a very bad student", ["a good student", "an average student", "a bad student"], "7〜8 とても悪い学生."), M("In the self-check, what does 0 ○ mean?", "a very good student", ["an average student", "a bad student", "a good student"], "0 とてもいい学生."),
           M("What style is the Hashimoto-kun article written in?", "the short form", ["the polite form", "the honorific form", "the humble form"], "short form is formal in articles."),
           F("授業を聞き___、時々寝てしまう。 (while)", "ながら", ["たり", "ても", "ので"], "ながら."), F("今年、五回___授業をサボってしまった。 (more than)", "以上", ["以下", "以外", "以前"], "以上."), F("やさしい先生のほうがきびしい先生___好きだ。 (than)", "より", ["まで", "ほど", "だけ"], "より好き."), F("先輩たちと親しく___たし、今の彼女にも会えた。", "なれ", ["なり", "なる", "なって"], "親しくなれた.")]
    ),
)

UNIT = unit("Genki II, Reading & Writing 18: College Life", [L1, L2, L3, L4, L5, L6])

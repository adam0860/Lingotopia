"""Unit 21 (chapter 19): shopping, bargaining, which/any, clothes, the coffee shop, exclamations, double-letter verbs."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 316
L316 = lesson(
    "At the butcher's",
    "لَحْم · دَجَاج · سَمَك · كِيلُو · قِطْعَة",
    requires=["لحم", "دجاج", "سمك", "بقر", "كيلو", "قطعة", "شريحة", "صنف", "قطع"],
    cards=[
        card("Meat, kilos and pieces",
             "A butcher is جَزَّار and a small shop is a دُكَّان. Meat is لَحْم; beef is لَحْم الْبَقَر. The word صِنْف means “kind”, and its plural is أَصْنَاف. "
             "You ask for an amount with مِنْ: كِيلُو مِنَ اللَّحْم, “a kilo of meat”.",
             tables=[table(["English", "Arabic"],
                           [["meat", "لَحْم"], ["beef", "لَحْم الْبَقَر"], ["chicken", "دَجَاج"], ["fish", "سَمَك"], ["butcher", "جَزَّار"], ["small shop", "دُكَّان"],
                            ["kilo", "كِيلُو"], ["piece", "قِطْعَة"], ["pieces", "قِطَع"], ["slice, large cut", "شَرِيحَة"], ["kind, sort", "صِنْف"], ["kinds, sorts", "أَصْنَاف"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Asking the butcher",
             "Notice أُرِيد (“I want”) with a noun, and هَلْ تُرِيد أَنْ أَقْطَع لَكَ اللَّحْم؟, “Do you want me to cut the meat for you?”. After أَنْ the verb is in the subjunctive; with أَنَا it looks the same as the present: أَقْطَع.",
             examples=[
                 ex("عِنْدَ الْجَزَّار أَصْنَاف كَثِيرَة مِنَ اللَّحْم.", "The butcher has many kinds of meat.", "أَصْنَاف"),
                 ex("أُرِيد كِيلُو مِنْ لَحْم الْبَقَر.", "I want a kilo of beef.", "كِيلُو"),
                 ex("هَلْ تُرِيد أَنْ أَقْطَع لَكَ اللَّحْم؟", "Do you want me to cut the meat for you?", "أَقْطَع"),
                 ex("نَعَمْ، أُرِيد شَرِيحَة كَبِيرَة لِلشِّوَاء.", "Yes, I want a large cut for grilling.", "شَرِيحَة"),
                 ex("أُرِيد قِطَع صَغِيرَة لِلطَّبْخ.", "I want small pieces for cooking.", "قِطَع"),
                 ex("هَلِ الدَّجَاج طَازَج الْيَوْم؟", "Is the chicken fresh today?", "طَازَج"),
             ]),
    ],
    exercises=[
        M("Which word means “chicken”?", "دَجَاج", ["سَمَك", "خُبْز", "حَلِيب"], "دَجَاج = chicken."),
        M("What is a جَزَّار?", "a butcher", ["a baker", "a driver", "a teacher"], "جَزَّار = butcher."),
        M("What does كِيلُو mean?", "kilo", ["piece", "price", "kind"], "كِيلُو = kilo."),
        M("Which word is the singular of أَصْنَاف?", "صِنْف", ["صَانِع", "صَفّ"], "صِنْف = kind; أَصْنَاف = kinds."),
        M("What does أُرِيد كِيلُو مِنْ لَحْم الْبَقَر mean?", "I want a kilo of beef", ["I want a kilo of chicken", "I want a piece of fish", "I sell a kilo of beef"], "لَحْم الْبَقَر = beef."),
        M("What does هَلْ تُرِيد أَنْ أَقْطَع لَكَ اللَّحْم؟ mean?", "Do you want me to cut the meat for you?", ["Do you want to buy the meat?", "Did you cut the meat yesterday?", "Will you cook the meat for me?"], "أَقْطَع = I cut."),
        F("أُرِيد ___ كَبِيرَة لِلشِّوَاء.", "شَرِيحَة", ["جَزَّار", "دُكَّان"], "A feminine noun fits كَبِيرَة.", tr="I want a large cut for grilling."),
        F("عِنْدَ الْجَزَّار ___ كَثِيرَة مِنَ اللَّحْم.", "أَصْنَاف", ["صِنْف", "جَزَّار"], "Plural of things: feminine singular adjective كَثِيرَة.", tr="The butcher has many kinds of meat."),
        F("هَلْ تُرِيد أَنْ ___ لَكَ اللَّحْم؟", "أَقْطَع", ["قَطْع", "قَاطِع"], "After أَنْ, a verb: أَقْطَع.", tr="Do you want me to cut the meat for you?", lemma="قطع:sub:ana"),
    ],
    verify=(vv("قطع", "sub", ana="أَقْطَع")
            + vw("لَحْم", "دَجَاج", "سَمَك", "جَزَّار", "دُكَّان", "كِيلُو", "قِطْعَة", "شَرِيحَة", "صِنْف", "أَصْنَاف", "قِطَع", "الْبَقَر", "الشِّوَاء", "لِلشِّوَاء", "لِلطَّبْخ", "طَازَج", "الدَّجَاج", "السَّمَك", "صَانِع", "صَفّ", "قَطْع", "قَاطِع", "ثَمَن")),
)

# ---------------------------------------------------------------------------- 317
L317 = lesson(
    "Prices and bargaining",
    "كَمْ ثَمَنُهُ؟ · غَالِي · رَخِيص · آخِر سِعْر",
    requires=["ثمن", "سعر", "غالي", "رخيص", "دفع", "حساب", "خصم", "كم", "نقد"],
    cards=[
        card("Asking and judging the price",
             "ثَمَن and سِعْر both mean “price”. To ask, say كَمْ ثَمَنُهُ؟ (“How much is it?”). A high price is غَالِي and a low one is رَخِيص; the comparatives are أَغْلَى and أَرْخَص. "
             "To bargain, ask for the last price: آخِر سِعْر. The word for bargaining is مُسَاوَمَة, and a discount is خَصْم.",
             tables=[table(["English", "Arabic"],
                           [["price", "ثَمَن"], ["price, rate", "سِعْر"], ["expensive", "غَالِي"], ["cheap", "رَخِيص"], ["more expensive", "أَغْلَى"], ["cheaper", "أَرْخَص"],
                            ["bargaining", "مُسَاوَمَة"], ["discount", "خَصْم"], ["the bill, the account", "الْحِسَاب"], ["cash", "نَقْدًا"], ["last price", "آخِر سِعْر"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A bargaining dialogue (invented)",
             "A customer and a shopkeeper talk. The customer uses أَظُنّ أَنَّ…, “I think that…”. This verb has a doubled letter; you will study it in this unit.",
             examples=[
                 ex("كَمْ ثَمَن هَذَا؟", "How much is this?", "كَمْ ثَمَن"),
                 ex("ثَمَنُهُ عَشَرَة دَنَانِير.", "Its price is ten dinars.", "عَشَرَة دَنَانِير"),
                 ex("أَظُنّ أَنَّ الثَّمَن غَالِي.", "I think the price is high.", "أَظُنّ"),
                 ex("سَأَدْفَع ثَمَانِيَة دَنَانِير فَقَط.", "I will pay only eight dinars.", "سَأَدْفَع"),
                 ex("هَلْ تَدْفَع نَقْدًا أَوْ بِالْبِطَاقَة؟", "Do you pay in cash or by card?", "نَقْدًا"),
                 ex("فِي بَعْض الْأَحْيَاء يَشْتَرِي النَّاس بِالدَّيْن، وَيَدْفَعُون أَوَّل الشَّهْر.", "In some neighbourhoods people buy on credit and pay at the beginning of the month.", "بِالدَّيْن"),
             ]),
    ],
    exercises=[
        M("Which word means “cheap”?", "رَخِيص", ["غَالِي", "كَبِير", "جَدِيد"], "رَخِيص = cheap."),
        M("What does كَمْ ثَمَنُهُ؟ ask?", "How much is it?", ["Where is it?", "Who made it?", "When does it open?"], "ثَمَن = price."),
        M("What does آخِر سِعْر mean?", "last price", ["first day", "new kind", "big piece"], "آخِر = last."),
        M("What is مُسَاوَمَة?", "bargaining", ["delivery", "payment by card", "a gift"], "مُسَاوَمَة = bargaining."),
        M("What does نَقْدًا mean?", "in cash", ["on credit", "by card", "tomorrow"], "نَقْدًا = in cash."),
        M("What does أَظُنّ أَنَّ الثَّمَن غَالِي mean?", "I think the price is high", ["I know the price is low", "I pay the price", "The price was high"], "أَظُنّ = I think."),
        F("___ ثَمَانِيَة دَنَانِير فَقَط.", "سَأَدْفَع", ["دَفَعْتُ", "اِدْفَعْ"], "Future: سَـ + أَدْفَع.", tr="I will pay only eight dinars.", lemma="دفع:fut:ana"),
        F("هَذَا الْقَمِيص ___ مِنْ ذَلِكَ.", "أَرْخَص", ["رَخِيص", "غَالِي"], "Comparison with مِنْ: أَرْخَص = cheaper.", tr="This shirt is cheaper than that one."),
        F("هَلْ تَدْفَع ___ أَوْ بِالْبِطَاقَة؟", "نَقْدًا", ["أَوَّلًا", "جِدًّا"], "Cash or card.", tr="Do you pay in cash or by card?"),
    ],
    verify=(vv("دفع", "fut", ana="سَأَدْفَع") + vv("دفع", "pres", anta="تَدْفَع", hum="يَدْفَعُون") + vv("ظنن", "pres", ana="أَظُنّ")
            + vw("ثَمَن", "ثَمَنُهُ", "سِعْر", "غَالِي", "رَخِيص", "أَغْلَى", "أَرْخَص", "مُسَاوَمَة", "خَصْم", "الْحِسَاب", "نَقْدًا", "دَنَانِير", "عَشَرَة", "ثَمَانِيَة", "بِالْبِطَاقَة", "بِالدَّيْن", "الْأَحْيَاء", "الشَّهْر", "الْقَمِيص", "جِدًّا", "اِدْفَعْ", "دَفَعْتُ")),
)

# ---------------------------------------------------------------------------- 318
L318 = lesson(
    "أَيّ: “which?” and “any”",
    "أَيّ صِنْف تُرِيد؟ · هَلْ عِنْدَكَ أَيّ قَمِيص؟",
    requires=["أي", "صنف", "لون", "مقاس", "خدمة", "وقت", "يوم", "شخص", "مشكلة", "عند"],
    cards=[
        card("أَيّ in a question",
             "Put أَيّ in front of a singular noun to ask “which?”. The noun is indefinite and follows directly: أَيّ لَوْن؟ means “which colour?”. "
             "A shopkeeper may open with أَيّ خِدْمَة؟, literally “what service?”, that is, “How can I help you?”. This is a common everyday phrase.",
             tables=[table(["Arabic", "English"],
                           [["أَيّ صِنْف", "which kind"], ["أَيّ لَوْن", "which colour"], ["أَيّ مَقَاس", "which size"], ["أَيّ يَوْم", "which day"], ["أَيّ خِدْمَة؟", "How can I help?"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("أَيّ meaning “any”",
             "In a yes/no question or after “not”, the same word means “any”: هَلْ عِنْدَكَ أَيّ قَمِيص أَزْرَق؟ “Do you have any blue shirts?”. In fixed phrases it also means “whichever” or “at all”.",
             examples=[
                 ex("أَيّ صِنْف تُرِيد؟", "Which kind do you want?", "أَيّ صِنْف"),
                 ex("أَيّ لَوْن تُحِبّ؟", "Which colour do you like?", "أَيّ لَوْن"),
                 ex("فِي أَيّ يَوْم سَتَأْتِي؟", "On which day will you come?", "أَيّ يَوْم"),
                 ex("هَلْ عِنْدَكَ أَيّ قَمِيص أَزْرَق؟", "Do you have any blue shirts?", "أَيّ قَمِيص"),
                 ex("لَيْسَ عِنْدِي أَيّ مُشْكِلَة.", "I do not have any problems.", "أَيّ مُشْكِلَة"),
                 ex("يُمْكِنُكَ أَنْ تَأْتِي فِي أَيّ وَقْت.", "You can come at any time.", "أَيّ وَقْت"),
             ]),
    ],
    exercises=[
        M("What does أَيّ لَوْن تُحِبّ؟ ask?", "Which colour do you like?", ["How many colours are there?", "Where is the colour?", "Who likes colours?"], "أَيّ + noun = which."),
        M("What does أَيّ خِدْمَة؟ mean in a shop?", "How can I help you?", ["Where is the exit?", "What is the price?", "How old are you?"], "A shopkeeper's opening."),
        M("What does أَيّ مَقَاس mean?", "which size", ["which price", "which shop", "which friend"], "مَقَاس = size."),
        M("What does هَلْ عِنْدَكَ أَيّ قَمِيص أَزْرَق؟ mean?", "Do you have any blue shirts?", ["Is this your blue shirt?", "Which shirt is blue?", "Where is the blue shirt?"], "أَيّ in a question = any."),
        M("What does لَيْسَ عِنْدِي أَيّ مُشْكِلَة mean?", "I do not have any problem", ["I have a big problem", "I had a problem yesterday", "There is no shop"], "After “not”, أَيّ = any."),
        M("What does فِي أَيّ وَقْت mean?", "at any time", ["at no time", "at the market", "at the same price"], "أَيّ وَقْت = any time."),
        F("___ صِنْف تُرِيد؟", "أَيّ", ["مَتَى", "أَيْنَ"], "Which kind?", tr="Which kind do you want?"),
        F("هَلْ عِنْدَكَ ___ قَمِيص أَزْرَق؟", "أَيّ", ["كُلّ", "هَذَا"], "Any shirt.", tr="Do you have any blue shirts?"),
        F("فِي ___ يَوْم سَتَأْتِي؟", "أَيّ", ["مَاذَا", "مَنْ"], "On which day.", tr="On which day will you come?"),
    ],
    verify=vw("أَيّ", "صِنْف", "لَوْن", "مَقَاس", "يَوْم", "خِدْمَة", "قَمِيص", "أَزْرَق", "مُشْكِلَة", "وَقْت", "تُحِبّ", "سَتَأْتِي", "عِنْدَكَ", "عِنْدِي", "مَتَى", "أَيْنَ", "كُلّ", "هَذَا", "مَاذَا", "مَنْ"),
)

# ---------------------------------------------------------------------------- 319
L319 = lesson(
    "A shopping list: food",
    "خُبْز · حَلِيب · جُبْن · بَيْض · أَرُزّ",
    requires=["خبز", "حليب", "جبن", "بيض", "زيت", "ملح", "سكر", "طماطم", "قائمة"],
    cards=[
        card("Food and containers",
             "A list is قَائِمَة. In a shopping list, you name the amount and then the thing: كِيلُو طَمَاطِم, عُلْبَة جُبْن, زُجَاجَة زَيْت. "
             "Mass nouns such as rice and sugar need a container or a weight.",
             tables=[table(["English", "Arabic"],
                           [["bread", "خُبْز"], ["milk", "حَلِيب"], ["cheese", "جُبْن"], ["eggs", "بَيْض"], ["rice", "أَرُزّ"], ["oil", "زَيْت"], ["salt", "مِلْح"], ["sugar", "سُكَّر"], ["tomatoes", "طَمَاطِم"],
                            ["bag", "كِيس"], ["bottle", "زُجَاجَة"], ["can, box", "عُلْبَة"], ["list", "قَائِمَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("My list",
             "Read this list from the market. The amounts come first.",
             examples=[
                 ex("كِيلُو طَمَاطِم", "a kilo of tomatoes", "كِيلُو"),
                 ex("كِيس أَرُزّ", "a bag of rice", "كِيس"),
                 ex("زُجَاجَة زَيْت", "a bottle of oil", "زُجَاجَة"),
                 ex("عُلْبَة جُبْن", "a box of cheese", "عُلْبَة"),
                 ex("لَا أَنْسَى الْحَلِيب وَالْخُبْز.", "I do not forget the milk and the bread.", "لَا أَنْسَى"),
                 ex("هَذِهِ هِيَ قَائِمَتِي لِلسُّوق.", "This is my list for the market.", "قَائِمَتِي"),
             ]),
    ],
    exercises=[
        M("What does خُبْز mean?", "bread", ["rice", "salt", "cheese"], "خُبْز = bread."),
        M("What does حَلِيب mean?", "milk", ["oil", "sugar", "eggs"], "حَلِيب = milk."),
        M("What is a كِيس?", "a bag", ["a bottle", "a kilo", "a price"], "كِيس = bag."),
        M("What is a زُجَاجَة?", "a bottle", ["a bag", "a list", "a shop"], "زُجَاجَة = bottle."),
        M("What does كِيلُو طَمَاطِم mean?", "a kilo of tomatoes", ["a bag of tomatoes", "a tomato shop", "ten tomatoes"], "Amount first, then the thing."),
        M("What does قَائِمَة mean?", "list", ["shop", "price", "bag"], "قَائِمَة = list."),
        F("___ أَرُزّ", "كِيس", ["دُكَّان", "جَزَّار"], "A container for rice: bag.", tr="a bag of rice"),
        F("___ زَيْت", "زُجَاجَة", ["جَزَّار", "سِعْر"], "A container for oil: bottle.", tr="a bottle of oil"),
        F("لَا ___ الْحَلِيب وَالْخُبْز.", "أَنْسَى", ["نَسِيَ", "نَاسِي"], "لَا + present: I do not forget.", tr="I do not forget the milk and the bread."),
    ],
    verify=(vv("نسي", "pres", ana="أَنْسَى")
            + vw("خُبْز", "حَلِيب", "جُبْن", "بَيْض", "أَرُزّ", "زَيْت", "مِلْح", "سُكَّر", "طَمَاطِم", "كِيس", "زُجَاجَة", "عُلْبَة", "قَائِمَة", "قَائِمَتِي", "كِيلُو", "الْحَلِيب", "وَالْخُبْز", "دُكَّان", "ثَمَن", "جَزَّار", "سِعْر", "نَسِيَ", "نَاسِي")),
)


# ---------------------------------------------------------------------------- 320
L320 = lesson(
    "Clothes, colours and materials",
    "قَمِيص · فُسْتَان · سِرْوَال · مِعْطَف · قُطْن · جِلْد",
    requires=["قميص", "فستان", "حذاء", "حزام", "ثوب", "لون", "أحمر", "أزرق", "أبيض", "قطن", "جلد"],
    cards=[
        card("What people wear",
             "The words below are the basic names of clothes. A word for a piece of clothing is placed before its colour or material: قَمِيص أَبْيَض, “a white shirt”; قَمِيص مِنَ الْقُطْن, “a cotton shirt”.",
             tables=[table(["English", "Arabic"],
                           [["shirt", "قَمِيص"], ["dress", "فُسْتَان"], ["trousers", "سِرْوَال"], ["coat", "مِعْطَف"], ["shoes (a pair)", "حِذَاء"], ["hat", "قُبَّعَة"], ["belt", "حِزَام"], ["garment, robe", "ثَوْب"],
                            ["cotton", "قُطْن"], ["wool", "صُوف"], ["leather", "جِلْد"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Colours agree with the thing",
             "A colour is an adjective. It follows the noun and agrees with it. For a masculine noun use the masculine form; for a feminine noun use the feminine form. "
             "Words such as قُبَّعَة are feminine because of the ـَة ending.",
             tables=[table(["Colour", "Masculine", "Feminine"],
                           [["white", "أَبْيَض", "بَيْضَاء"], ["black", "أَسْوَد", "سَوْدَاء"], ["red", "أَحْمَر", "حَمْرَاء"], ["blue", "أَزْرَق", "زَرْقَاء"], ["green", "أَخْضَر", "خَضْرَاء"], ["yellow", "أَصْفَر", "صَفْرَاء"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)],
             examples=[
                 ex("أُرِيد قَمِيص أَبْيَض مِنَ الْقُطْن.", "I want a white cotton shirt.", "قَمِيص أَبْيَض"),
                 ex("عِنْدَهَا فُسْتَان أَحْمَر وَقُبَّعَة سَوْدَاء.", "She has a red dress and a black hat.", "قُبَّعَة سَوْدَاء"),
                 ex("هَذَا الْحِزَام مِنَ الْجِلْد.", "This belt is made of leather.", "مِنَ الْجِلْد"),
                 ex("أُحِبّ الْمِعْطَف الْأَزْرَق.", "I like the blue coat.", "الْمِعْطَف الْأَزْرَق"),
             ]),
    ],
    exercises=[
        M("What does قَمِيص mean?", "shirt", ["dress", "shoes", "belt"], "قَمِيص = shirt."),
        M("Which word means “dress”?", "فُسْتَان", ["حِزَام", "حِذَاء", "قُطْن"], "فُسْتَان = dress."),
        M("What is جِلْد?", "leather", ["cotton", "wool", "colour"], "جِلْد = leather."),
        M("Which is the feminine form of أَبْيَض?", "بَيْضَاء", ["بَيَاض"], "White: m. أَبْيَض, f. بَيْضَاء."),
        M("What does هَذَا الْحِزَام مِنَ الْجِلْد mean?", "This belt is made of leather", ["This belt is made of cotton", "This belt is white", "This belt is expensive"], "مِنَ = of, made of."),
        M("Which noun is feminine?", "قُبَّعَة", ["قَمِيص", "حِزَام", "مِعْطَف"], "The ـَة ending marks it as feminine."),
        F("عِنْدَهَا قُبَّعَة ___", "سَوْدَاء", ["أَسْوَد", "سُود"], "The adjective agrees with the feminine noun قُبَّعَة.", tr="She has a black hat."),
        F("أُرِيد قَمِيص ___ مِنَ الْقُطْن.", "أَبْيَض", ["بَيْضَاء", "بِيض"], "قَمِيص is masculine.", tr="I want a white cotton shirt."),
        F("هَذَا الْمِعْطَف مِنَ ___", "الصُّوف", ["الْحِزَام", "الْقَمِيص"], "A coat can be made of wool; a belt or a shirt is not a material.", tr="This coat is made of wool."),
    ],
    verify=vw("قَمِيص", "فُسْتَان", "سِرْوَال", "مِعْطَف", "حِذَاء", "قُبَّعَة", "حِزَام", "ثَوْب", "قُطْن", "صُوف", "جِلْد", "الْقُطْن", "الْجِلْد", "أَبْيَض", "بَيْضَاء", "أَسْوَد", "سَوْدَاء", "أَحْمَر", "حَمْرَاء", "أَزْرَق", "زَرْقَاء", "أَخْضَر", "خَضْرَاء", "أَصْفَر", "صَفْرَاء", "بَيَاض", "بِيض", "سُود", "الْمِعْطَف", "الْأَزْرَق", "الصُّوف"),
)

# ---------------------------------------------------------------------------- 321
L321 = lesson(
    "Trying on and exchanging clothes",
    "هَلْ يُمْكِن أَنْ أُجَرِّب هَذَا الْقَمِيص؟",
    requires=["جرب", "بدل", "مقاس", "كبير", "صغير", "ناسب", "خصم", "ممكن", "لون", "ثمن"],
    cards=[
        card("In the fitting room",
             "To try something on, use the Measure II verb جَرَّبَ. After هَلْ يُمْكِن أَنْ, the verb is in the present form: أُجَرِّب, “I try on”. "
             "To exchange, use بَدَّلَ: أُبَدِّل, “I exchange, change”. Sizes are described with كَبِير, “big”, and صَغِير, “small”; ask for a different one with أَكْبَر or أَصْغَر.",
             examples=[
                 ex("هَلْ يُمْكِن أَنْ أُجَرِّب هَذَا الْقَمِيص؟", "May I try on this shirt?", "أُجَرِّب"),
                 ex("الْقَمِيص كَبِير عَلَيَّ.", "The shirt is big on me.", "كَبِير"),
                 ex("هَلْ عِنْدَكَ مَقَاس أَصْغَر؟", "Do you have a smaller size?", "أَصْغَر"),
                 ex("هَذَا اللَّوْن يُنَاسِبُكَ.", "This colour suits you.", "يُنَاسِبُكَ"),
                 ex("هَلْ يُمْكِن أَنْ أُبَدِّل هَذَا الْقَمِيص بِمَقَاس أَكْبَر؟", "May I exchange this shirt for a bigger size?", "أُبَدِّل"),
                 ex("فِي الْمَحَلّ تَخْفِيضَات هَذَا الْأُسْبُوع.", "There are sales in the shop this week.", "تَخْفِيضَات"),
                 ex("الْخَصْم عِشْرُون بِالْمِئَة.", "The discount is twenty per cent.", "بِالْمِئَة"),
             ]),
    ],
    exercises=[
        M("What does جَرَّبَ mean?", "tried (on)", ["bought", "sold", "paid"], "جَرَّبَ = tried."),
        M("What does هَلْ يُمْكِن أَنْ أُجَرِّب هَذَا الْقَمِيص؟ ask?", "May I try on this shirt?", ["May I buy this shirt?", "Is this shirt cheap?", "Do you wash this shirt?"], "أُجَرِّب = I try."),
        M("What does الْقَمِيص كَبِير عَلَيَّ mean?", "The shirt is big on me", ["The shirt is cheap for me", "The shirt is my friend's", "The shirt is blue"], "كَبِير = big."),
        M("What does هَلْ عِنْدَكَ مَقَاس أَصْغَر؟ ask?", "Do you have a smaller size?", ["Do you have a bigger size?", "Do you have a cheaper shirt?", "Do you have another colour?"], "أَصْغَر = smaller."),
        M("What does هَذَا اللَّوْن يُنَاسِبُكَ mean?", "This colour suits you", ["This colour is expensive", "This colour is new", "This colour is gone"], "يُنَاسِبُكَ = suits you."),
        M("What does تَخْفِيضَات mean?", "sales (price cuts)", ["customers", "sizes", "pockets"], "تَخْفِيضَات = reductions."),
        F("هَلْ يُمْكِن أَنْ ___ هَذَا الْقَمِيص؟", "أُجَرِّب", ["جَرَّبْتُ", "مُجَرِّب"], "After أَنْ, a present verb: أُجَرِّب.", tr="May I try on this shirt?", lemma="جرب#2:sub:ana"),
        F("هَلْ يُمْكِن أَنْ ___ هَذَا الْقَمِيص بِمَقَاس أَكْبَر؟", "أُبَدِّل", ["بَدَّلْتُ", "تَبْدِيل"], "After أَنْ, a present verb.", tr="May I exchange this shirt for a bigger size?", lemma="بدل#2:sub:ana"),
        F("هَلْ عِنْدَكَ مَقَاس ___؟", "أَصْغَر", ["صَغِير", "الصِّغَر"], "Smaller = أَصْغَر.", tr="Do you have a smaller size?"),
    ],
    verify=(vv("جرب#2", "sub", ana="أُجَرِّب") + vv("بدل#2", "sub", ana="أُبَدِّل")
            + vw("جَرَّبَ", "أُجَرِّب", "أُبَدِّل", "يُمْكِن", "الْقَمِيص", "كَبِير", "عَلَيَّ", "مَقَاس", "أَصْغَر", "أَكْبَر", "اللَّوْن", "يُنَاسِبُكَ", "الْمَحَلّ", "تَخْفِيضَات", "الْأُسْبُوع", "الْخَصْم", "عِشْرُون", "بِالْمِئَة", "جَرَّبْتُ", "مُجَرِّب", "بَدَّلْتُ", "تَبْدِيل", "صَغِير", "الصِّغَر")),
)

# ---------------------------------------------------------------------------- 322
L322 = lesson(
    "Old markets and modern malls",
    "السُّوق الْقَدِيم · الْمَرْكَز التِّجَارِيّ",
    requires=["سوق", "قديم", "حديث", "مركز", "تجاري", "محل", "بائع", "زبون", "مدينة"],
    cards=[
        card("Two kinds of shopping",
             "In many Arab cities you can find an old market, a سُوق, and a modern mall, a مَرْكَز تِجَارِيّ, in the same town. "
             "The sentences below describe common patterns, not rules for every place.",
             tables=[table(["English", "Arabic"],
                           [["market", "سُوق"], ["markets", "أَسْوَاق"], ["shopping centre", "مَرْكَز تِجَارِيّ"], ["shop", "مَحَلّ"], ["seller", "بَائِع"], ["customer", "زَبُون"], ["old", "قَدِيم"], ["modern", "حَدِيث"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What is different",
             "Three places known for their markets and shops are الْقَاهِرَة in Egypt, مَرَّاكُش in Morocco and مَدِينَة الْكُوَيْت, the capital of Kuwait. These sentences are only general pictures.",
             examples=[
                 ex("فِي كَثِير مِنَ الْمُدُن الْعَرَبِيَّة أَسْوَاق قَدِيمَة وَمَرَاكِز تِجَارِيَّة حَدِيثَة.", "In many Arab cities there are old markets and modern shopping centres.", "أَسْوَاق قَدِيمَة"),
                 ex("فِي السُّوق الْقَدِيم تَكُون الْمُسَاوَمَة شَائِعَة فِي كَثِير مِنَ الْأَحْيَان.", "In many cases, bargaining is common in the old market.", "الْمُسَاوَمَة"),
                 ex("فِي الْمَرْكَز التِّجَارِيّ تَكُون الْأَسْعَار عَادَةً مَكْتُوبَة.", "In the shopping centre the prices are usually written.", "مَكْتُوبَة"),
                 ex("يَبِيع الْبَائِع وَيَدْفَع الزَّبُون.", "The seller sells and the customer pays.", "الزَّبُون"),
                 ex("الْقَاهِرَة مَدِينَة فِي مِصْر.", "Cairo is a city in Egypt.", "الْقَاهِرَة"),
                 ex("مَرَّاكُش مَدِينَة فِي الْمَغْرِب.", "Marrakesh is a city in Morocco.", "مَرَّاكُش"),
                 ex("مَدِينَة الْكُوَيْت هِيَ عَاصِمَة الْكُوَيْت.", "Kuwait City is the capital of Kuwait.", "عَاصِمَة"),
             ]),
    ],
    exercises=[
        M("What is a سُوق?", "a market", ["a school", "a river", "a holiday"], "سُوق = market."),
        M("What is a مَرْكَز تِجَارِيّ?", "a shopping centre", ["a police station", "a school", "a bakery"], "تِجَارِيّ = commercial."),
        M("Who is the زَبُون?", "the customer", ["the seller", "the cook", "the driver"], "زَبُون = customer."),
        M("Who is the بَائِع?", "the seller", ["the customer", "the guest", "the neighbour"], "بَائِع = seller."),
        M("Where is the city of الْقَاهِرَة?", "in Egypt", ["in Kuwait", "in Morocco", "in Lebanon"], "الْقَاهِرَة مَدِينَة فِي مِصْر."),
        M("What is the capital of Kuwait?", "Kuwait City", ["Cairo", "Beirut", "Rabat"], "مَدِينَة الْكُوَيْت = Kuwait City."),
        F("فِي كَثِير مِنَ الْمُدُن الْعَرَبِيَّة أَسْوَاق ___", "قَدِيمَة", ["قَدِيم", "قُدَمَاء"], "أَسْوَاق = things (plural): feminine singular adjective.", tr="In many Arab cities there are old markets."),
        F("يَبِيع الْبَائِع وَيَدْفَع ___", "الزَّبُون", ["الْمَرْكَز", "الْمَحَلّ"], "The one who pays is the customer.", tr="The seller sells and the customer pays."),
        F("مَرَّاكُش ___ فِي الْمَغْرِب.", "مَدِينَة", ["قَمِيص", "حِزَام"], "Marrakesh is a city.", tr="Marrakesh is a city in Morocco."),
    ],
    verify=vw("سُوق", "أَسْوَاق", "مَرْكَز", "تِجَارِيّ", "مَحَلّ", "بَائِع", "زَبُون", "قَدِيم", "حَدِيث", "الْمُدُن", "الْعَرَبِيَّة", "قَدِيمَة", "حَدِيثَة", "مَرَاكِز", "تِجَارِيَّة", "الْمُسَاوَمَة", "شَائِعَة", "الْأَحْيَان", "عَادَةً", "مَكْتُوبَة", "الْقَاهِرَة", "الْمَغْرِب", "الْكُوَيْت", "مِصْر", "عَاصِمَة", "قُدَمَاء", "الْمَرْكَز", "الْمَحَلّ"),
)

# ---------------------------------------------------------------------------- 323
L323 = lesson(
    "Exclamations: مَا أَجْمَلَ … !",
    "مَا + أَفْعَلَ + accusative",
    requires=["جميل", "كبير", "غالي", "رخيص", "فستان", "سعر", "ما", "سريع", "طيب", "لذيذ"],
    cards=[
        card("The pattern",
             "To say “How beautiful …!”, use مَا, then a word of the shape أَفْعَلَ, and then the thing you admire in the accusative. "
             "The middle word ends in a fatḥa, and the thing admired ends in ـَ (or ـًا for an indefinite noun). "
             "It is built from the adjective: جَمِيل (beautiful) gives مَا أَجْمَلَ, “how beautiful!”. "
             "Do not confuse it with the comparative أَجْمَل, “more beautiful”, which has no مَا before it.",
             tables=[table(["Adjective", "Exclamation", "English"],
                           [["جَمِيل", "مَا أَجْمَلَ", "how beautiful"], ["كَبِير", "مَا أَكْبَرَ", "how big"], ["غَالِي", "مَا أَغْلَى", "how expensive"], ["رَخِيص", "مَا أَرْخَصَ", "how cheap"],
                            ["سَرِيع", "مَا أَسْرَعَ", "how fast"], ["طَيِّب", "مَا أَطْيَبَ", "how good"], ["لَذِيذ", "مَا أَلَذَّ", "how delicious"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("Examples",
             "The admired thing is in the accusative: it takes a fatḥa. In this lesson the final vowels are written, because they carry the grammar.",
             examples=[
                 ex("مَا أَجْمَلَ هَذَا الْفُسْتَانَ!", "How beautiful this dress is!", "مَا أَجْمَلَ"),
                 ex("مَا أَغْلَى هَذَا الْفُسْتَانَ!", "How expensive this dress is!", "مَا أَغْلَى"),
                 ex("مَا أَرْخَصَ هَذَا الْحِذَاءَ!", "How cheap this pair of shoes is!", "مَا أَرْخَصَ"),
                 ex("مَا أَكْبَرَ هَذَا الْمَحَلَّ!", "How big this shop is!", "مَا أَكْبَرَ"),
                 ex("مَا أَلَذَّ الطَّعَامَ!", "How delicious the food is!", "مَا أَلَذَّ"),
                 ex("مَا أَسْرَعَ الْبَائِعَ!", "How fast the seller is!", "مَا أَسْرَعَ"),
             ]),
    ],
    exercises=[
        M("What does مَا أَجْمَلَ هَذَا الْفُسْتَانَ! express?", "How beautiful this dress is!", ["This dress is more beautiful", "Where is this dress?", "What is this dress?"], "مَا + أَفْعَلَ = how …!"),
        M("What does مَا أَغْلَى هَذَا الْفُسْتَانَ! mean?", "How expensive this dress is!", ["How cheap this dress is!", "What is this dress?", "This dress is cheaper"], "غَالِي → أَغْلَى."),
        M("What does مَا أَلَذَّ الطَّعَامَ! mean?", "How delicious the food is!", ["How much is the food?", "Where is the food?", "The food is cold"], "لَذِيذ = delicious."),
        M("Which sentence is an exclamation?", "مَا أَكْبَرَ هَذَا الْمَحَلَّ!", ["هَذَا الْمَحَلّ كَبِير", "هَذَا الْمَحَلّ أَكْبَر مِنْ ذَلِكَ", "أَيّ مَحَلّ تُرِيد؟"], "Look for مَا + أَفْعَلَ."),
        M("What case is the noun after مَا أَجْمَلَ?", "accusative", ["nominative", "genitive", "no case"], "The admired thing is accusative, with ـَ."),
        M("Which is the exclamation built from رَخِيص?", "مَا أَرْخَصَ", ["مَا رَخِيص", "أَرْخَص مِنْ"], "مَا أَرْخَصَ = how cheap!"),
        F("مَا ___ هَذَا الْفُسْتَانَ!", "أَجْمَلَ", ["جَمِيل", "جَمَال"], "The pattern is أَفْعَلَ.", tr="How beautiful this dress is!"),
        F("مَا ___ هَذَا الْفُسْتَانَ!", "أَغْلَى", ["غَالِي", "الْغَلَاء"], "From غَالِي.", tr="How expensive this dress is!"),
        F("مَا أَلَذَّ ___!", "الطَّعَامَ", ["الطَّعَامُ", "الطَّعَامِ"], "The noun after the exclamation is accusative.", tr="How delicious the food is!"),
    ],
    verify=vw("مَا", "أَجْمَلَ", "أَكْبَرَ", "أَغْلَى", "أَرْخَصَ", "أَسْرَعَ", "أَطْيَبَ", "أَلَذَّ", "جَمِيل", "كَبِير", "غَالِي", "رَخِيص", "سَرِيع", "طَيِّب", "لَذِيذ", "الْفُسْتَانَ", "السِّعْرَ", "الْحِذَاءَ", "الْمَحَلَّ", "الطَّعَامَ", "الْبَائِعَ", "جَمَال", "الْغَلَاء", "أَجْمَل", "الْمَحَلّ", "مَحَلّ"),
)


# ---------------------------------------------------------------------------- 324
L324 = lesson(
    "Exclamations at the market",
    "مَا أَجْمَلَ هَذَا ! · مَا أَغْلَى هَذَا !",
    requires=["ما", "جميل", "غالي", "رخيص", "لون", "سوق", "ثمن", "قماش", "سريع", "كبير"],
    cards=[
        card("Statement, question, exclamation",
             "The same adjective can be used in three ways. A plain statement says what something is: هَذَا الْقَمِيص جَمِيل. "
             "A question with مَا asks what something is: مَا ثَمَن هَذَا الْقَمِيص؟ An exclamation shows feeling: مَا أَجْمَلَ هَذَا الْقَمِيصَ! It is built as مَا + a word like أَجْمَلَ + the thing in the accusative. "
             "In writing, an exclamation ends with !.",
             tables=[table(["Kind", "Arabic", "English"],
                           [["statement", "هَذَا الْقَمِيص جَمِيل.", "This shirt is beautiful."], ["question", "مَا ثَمَن هَذَا الْقَمِيص؟", "What is the price of this shirt?"], ["exclamation", "مَا أَجْمَلَ هَذَا الْقَمِيصَ!", "How beautiful this shirt is!"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Two friends at the market (invented)",
             "Two friends walk through a market and react to what they see.",
             examples=[
                 ex("مَا أَجْمَلَ هَذَا الْقُمَاشَ!", "How beautiful this cloth is!", "مَا أَجْمَلَ"),
                 ex("وَمَا أَغْلَى هَذَا الْقُمَاشَ!", "And how expensive this cloth is!", "مَا أَغْلَى"),
                 ex("مَا أَكْبَرَ هَذَا السُّوقَ!", "How big this market is!", "مَا أَكْبَرَ"),
                 ex("مَا أَسْرَعَ الْبَائِعَ فِي الْحِسَابِ!", "How fast the seller is at counting!", "مَا أَسْرَعَ"),
                 ex("مَا أَجْمَلَ الْأَلْوَانَ هُنَا!", "How beautiful the colours are here!", "الْأَلْوَانَ"),
                 ex("مَا أَرْخَصَ هَذِهِ الْقُبَّعَةَ!", "How cheap this hat is!", "مَا أَرْخَصَ"),
             ]),
    ],
    exercises=[
        M("Which sentence is a question?", "مَا ثَمَن هَذَا الْقَمِيص؟", ["مَا أَجْمَلَ هَذَا الْقَمِيصَ!", "هَذَا الْقَمِيص جَمِيل."], "مَا + noun = “What is …?”"),
        M("Which sentence is a statement?", "هَذَا الْقَمِيص جَمِيل.", ["مَا أَجْمَلَ هَذَا الْقَمِيصَ!", "مَا ثَمَن هَذَا الْقَمِيص؟"], "Plain description."),
        M("What does مَا أَكْبَرَ هَذَا السُّوقَ! mean?", "How big this market is!", ["Where is this market?", "This market is smaller", "What is this market?"], "كَبِير → أَكْبَرَ."),
        M("What does وَمَا أَغْلَى هَذَا الْقُمَاشَ! mean?", "And how expensive this cloth is!", ["And what is the cloth?", "And it is cheaper", "And he paid cash"], "غَالِي → أَغْلَى."),
        M("What does مَا أَرْخَصَ هَذِهِ الْقُبَّعَةَ! mean?", "How cheap this hat is!", ["How big this hat is!", "What is this hat?", "This hat is red"], "رَخِيص → أَرْخَصَ."),
        M("What does مَا أَجْمَلَ الْأَلْوَانَ هُنَا! mean?", "How beautiful the colours are here!", ["Which colour do you like?", "The colours are cheaper here", "Where are the colours?"], "مَا أَجْمَلَ = how beautiful!"),
        F("___ أَجْمَلَ هَذَا الْقُمَاشَ!", "مَا", ["لَا", "هَلْ"], "The exclamation starts with مَا.", tr="How beautiful this cloth is!"),
        F("مَا أَكْبَرَ ___ السُّوقَ!", "هَذَا", ["هَذِهِ", "ذَلِكَ"], "سُوق with هَذَا; ذَلِكَ means “that”.", tr="How big this market is!"),
        F("مَا ___ الْبَائِعَ فِي الْحِسَابِ!", "أَسْرَعَ", ["سَرِيع", "سُرْعَة"], "From سَرِيع.", tr="How fast the seller is at counting!"),
    ],
    verify=vw("مَا", "أَجْمَلَ", "أَغْلَى", "أَكْبَرَ", "أَسْرَعَ", "أَرْخَصَ", "الْقُمَاشَ", "ثَمَنَهُ", "السُّوقَ", "الْبَائِعَ", "الْحِسَابِ", "الْأَلْوَانَ", "الْقُبَّعَةَ", "هَذِهِ", "ذَلِكَ", "سَرِيع", "سُرْعَة", "هُنَا", "الْقَمِيص", "الْقَمِيصَ", "هَلْ"),
)

# ---------------------------------------------------------------------------- 325
L325 = lesson(
    "Exclamations about weather, crowds and time",
    "مَا أَحَرَّ الْجَوَّ ! · مَا أَكْثَرَ النَّاسَ !",
    requires=["جو", "حر", "برد", "ناس", "وقت", "كثير", "شدة", "سريع", "ماء", "ما"],
    cards=[
        card("More exclamations",
             "You can use the same pattern for many things: weather, crowds, time, water, food. Some adjectives have a doubled letter, such as حَارّ (hot) and شَدِيد (strong, severe). "
             "Their exclamatory forms keep the doubled letter with a shadda: مَا أَحَرَّ and مَا أَشَدَّ. Others are regular: مَا أَبْرَدَ, مَا أَكْثَرَ.",
             tables=[table(["Adjective", "Exclamation", "English"],
                           [["حَارّ", "مَا أَحَرَّ", "how hot"], ["بَارِد", "مَا أَبْرَدَ", "how cold"], ["شَدِيد", "مَا أَشَدَّ", "how strong, severe"], ["كَثِير", "مَا أَكْثَرَ", "how many, how much"], ["قَلِيل", "مَا أَقَلَّ", "how few, how little"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In use",
             "The thing described is again in the accusative.",
             examples=[
                 ex("مَا أَحَرَّ الْجَوَّ الْيَوْمَ!", "How hot the weather is today!", "مَا أَحَرَّ"),
                 ex("مَا أَبْرَدَ هَذَا الْمَاءَ!", "How cold this water is!", "مَا أَبْرَدَ"),
                 ex("مَا أَكْثَرَ النَّاسَ فِي السُّوقِ!", "How many people there are in the market!", "مَا أَكْثَرَ"),
                 ex("مَا أَسْرَعَ الْوَقْتَ!", "How fast time goes!", "مَا أَسْرَعَ"),
                 ex("مَا أَشَدَّ الْحَرَّ فِي الصَّيْفِ!", "How severe the heat is in summer!", "مَا أَشَدَّ"),
                 ex("مَا أَقَلَّ الزَّبَائِنَ الْيَوْمَ!", "How few the customers are today!", "مَا أَقَلَّ"),
             ]),
    ],
    exercises=[
        M("What does مَا أَحَرَّ الْجَوَّ الْيَوْمَ! mean?", "How hot the weather is today!", ["Is the weather hot?", "The weather was cold", "What is the weather?"], "حَارّ → أَحَرَّ."),
        M("What does مَا أَبْرَدَ هَذَا الْمَاءَ! mean?", "How cold this water is!", ["How hot this water is!", "Give me water", "Where is the water?"], "بَارِد → أَبْرَدَ."),
        M("What does مَا أَكْثَرَ النَّاسَ فِي السُّوقِ! mean?", "How many people there are in the market!", ["How few people there are in the market!", "Where are the people?", "The market is closed"], "كَثِير → أَكْثَرَ."),
        M("What does مَا أَسْرَعَ الْوَقْتَ! mean?", "How fast time goes!", ["What time is it?", "Time is cheap", "Wait a little"], "سَرِيع → أَسْرَعَ."),
        M("Which exclamation is written with a shadda?", "مَا أَحَرَّ", ["مَا أَبْرَدَ", "مَا أَكْثَرَ", "مَا أَسْرَعَ"], "حَارّ has a doubled letter."),
        M("Which means “how few”?", "مَا أَقَلَّ", ["مَا أَكْثَرَ", "مَا أَكْبَرَ", "مَا أَجْمَلَ"], "قَلِيل → أَقَلَّ."),
        F("مَا ___ الْجَوَّ الْيَوْمَ!", "أَحَرَّ", ["حَارّ", "أَحَرّ مِنْ"], "From حَارّ, with shadda.", tr="How hot the weather is today!"),
        F("مَا ___ هَذَا الْمَاءَ!", "أَبْرَدَ", ["بَارِد", "بُرُودَة"], "From بَارِد.", tr="How cold this water is!"),
        F("مَا أَكْثَرَ ___ فِي السُّوقِ!", "النَّاسَ", ["النَّاسُ", "النَّاسِ"], "The noun after the exclamation is accusative.", tr="How many people there are in the market!"),
    ],
    verify=vw("أَحَرَّ", "أَبْرَدَ", "أَشَدَّ", "أَكْثَرَ", "أَقَلَّ", "أَسْرَعَ", "حَارّ", "بَارِد", "شَدِيد", "كَثِير", "قَلِيل", "الْجَوَّ", "الْيَوْمَ", "الْمَاءَ", "النَّاسَ", "السُّوقِ", "الْوَقْتَ", "الْحَرَّ", "الصَّيْفِ", "الزَّبَائِنَ", "بُرُودَة", "أَحَرّ", "أَكْبَرَ", "أَجْمَلَ", "مِنْ"),
)

# ---------------------------------------------------------------------------- 326
L326 = lesson(
    "At the coffee shop",
    "أُرِيد فِنْجَان قَهْوَة · بِدُون سُكَّر",
    requires=["قهوة", "مقهى", "عصير", "ماء", "حليب", "سكر", "ساخن", "بارد", "مع", "فضل"],
    cards=[
        card("Drinks and ways to order",
             "A cup of coffee is فِنْجَان قَهْوَة and a glass of juice is كُوب عَصِير. With sugar is بِسُكَّر or مَعَ سُكَّر; without sugar is بِدُون سُكَّر. A drink can be سَاخِن (hot) or بَارِد (cold). "
             "Polite words: مِنْ فَضْلِكَ (please, to a man), تَفَضَّلْ (here you are), شُكْرًا (thank you).",
             tables=[table(["English", "Arabic"],
                           [["coffee shop", "مَقْهَى"], ["coffee", "قَهْوَة"], ["juice", "عَصِير"], ["water", "مَاء"], ["milk", "حَلِيب"], ["sugar", "سُكَّر"], ["small cup", "فِنْجَان"], ["glass", "كُوب"],
                            ["hot", "سَاخِن"], ["cold", "بَارِد"], ["without", "بِدُون"], ["with", "مَعَ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Ordering, accepting and declining",
             "A waiter may offer; you may accept or politely decline.",
             examples=[
                 ex("مِنْ فَضْلِكَ، أُرِيد فِنْجَان قَهْوَة بِدُون سُكَّر.", "Please, I want a cup of coffee without sugar.", "بِدُون سُكَّر"),
                 ex("هَلْ تُرِيد عَصِير بَارِد؟", "Do you want cold juice?", "بَارِد"),
                 ex("نَعَمْ، شُكْرًا، أُرِيد كُوب عَصِير.", "Yes, thank you, I want a glass of juice.", "نَعَمْ، شُكْرًا"),
                 ex("لَا، شُكْرًا، لَا أُرِيد حَلِيب.", "No, thank you, I do not want milk.", "لَا، شُكْرًا"),
                 ex("هَلْ تُرِيد شَيْئًا آخَر؟", "Do you want anything else?", "شَيْئًا آخَر"),
                 ex("الْحِسَاب مِنْ فَضْلِكَ.", "The bill, please.", "الْحِسَاب"),
             ]),
    ],
    exercises=[
        M("What is a مَقْهَى?", "a coffee shop", ["a school", "a bakery", "a bank"], "مَقْهَى = coffee shop."),
        M("What does بِدُون سُكَّر mean?", "without sugar", ["with sugar", "with milk", "very hot"], "بِدُون = without."),
        M("What does سَاخِن mean?", "hot", ["cold", "sweet", "new"], "سَاخِن = hot."),
        M("What does هَلْ تُرِيد شَيْئًا آخَر؟ ask?", "Do you want anything else?", ["Do you want the bill?", "Do you want another cup?", "Where do you sit?"], "شَيْء آخَر = something else."),
        M("What does لَا، شُكْرًا، لَا أُرِيد حَلِيب mean?", "No, thank you, I do not want milk", ["Yes, thank you, I want milk", "No, I want sugar", "No, the milk is cold"], "لَا أُرِيد = I do not want."),
        M("Which phrase asks for the bill?", "الْحِسَاب مِنْ فَضْلِكَ", ["تَفَضَّلْ", "كُوب مَاء", "بِدُون سُكَّر"], "الْحِسَاب = the bill."),
        F("أُرِيد فِنْجَان قَهْوَة ___ سُكَّر.", "بِدُون", ["مَعَ", "عَلَى"], "“Without sugar” needs بِدُون; مَعَ would mean “with”.", tr="I want a cup of coffee without sugar."),
        F("هَلْ تُرِيد عَصِير ___؟", "بَارِد", ["بَارِدَة", "فِنْجَان"], "عَصِير is masculine.", tr="Do you want cold juice?"),
        F("مِنْ فَضْلِكَ، أُرِيد ___ مَاء.", "كُوب", ["جَزَّار", "سِرْوَال"], "A glass of water.", tr="Please, I want a glass of water."),
    ],
    verify=vw("مَقْهَى", "قَهْوَة", "عَصِير", "مَاء", "حَلِيب", "سُكَّر", "فِنْجَان", "كُوب", "سَاخِن", "بَارِد", "بِدُون", "مَعَ", "بِسُكَّر", "فَضْلِكَ", "تَفَضَّلْ", "شُكْرًا", "شَيْئًا", "آخَر", "الْحِسَاب", "بَارِدَة", "جَزَّار", "سِرْوَال", "عَلَى"),
)

# ---------------------------------------------------------------------------- 327
L327 = lesson(
    "At the restaurant",
    "الْقَائِمَة · طَبَق · سَلَطَة · حَسَاء · مَشْوِيّ",
    requires=["مطعم", "قائمة", "طعام", "وجبة", "طبق", "سلطة", "سمك", "لحم", "عشاء", "غداء"],
    cards=[
        card("Menu words",
             "The menu is قَائِمَة الطَّعَام. A dish is طَبَق, and a meal is وَجْبَة. The waiter is نَادِل. Foods that are cooked on a grill are مَشْوِيّ.",
             tables=[table(["English", "Arabic"],
                           [["restaurant", "مَطْعَم"], ["menu", "قَائِمَة الطَّعَام"], ["meal", "وَجْبَة"], ["dish, plate", "طَبَق"], ["salad", "سَلَطَة"], ["soup", "حَسَاء"], ["rice", "أَرُزّ"], ["grilled", "مَشْوِيّ"], ["waiter", "نَادِل"], ["lunch", "غَدَاء"], ["dinner", "عَشَاء"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Ordering a meal",
             "Use أُرِيد (“I want”) or أُحِبّ أَنْ آكُل (“I like to eat”) for what you want. Ask politely with هَلْ عِنْدَكُمْ…؟, “Do you have …?”.",
             examples=[
                 ex("الْقَائِمَة مِنْ فَضْلِكَ.", "The menu, please.", "الْقَائِمَة"),
                 ex("أُرِيد طَبَق سَلَطَة وَحَسَاء.", "I want a plate of salad and soup.", "حَسَاء"),
                 ex("هَلْ عِنْدَكُمْ سَمَك مَشْوِيّ؟", "Do you have grilled fish?", "مَشْوِيّ"),
                 ex("مَاذَا تُحِبّ أَنْ تَأْكُل؟", "What do you like to eat?", "تَأْكُل"),
                 ex("أُحِبّ الْأَرُزّ مَعَ اللَّحْم.", "I like rice with meat.", "الْأَرُزّ"),
                 ex("الْغَدَاء وَجْبَة كَبِيرَة فِي كَثِير مِنَ الْبُيُوت.", "Lunch is a large meal in many homes.", "الْغَدَاء"),
             ]),
    ],
    exercises=[
        M("What is a نَادِل?", "a waiter", ["a cook", "a customer", "a driver"], "نَادِل = waiter."),
        M("What is قَائِمَة الطَّعَام?", "the menu", ["the bill", "the kitchen", "the door"], "قَائِمَة = list; طَعَام = food."),
        M("What does حَسَاء mean?", "soup", ["salad", "rice", "bread"], "حَسَاء = soup."),
        M("What does هَلْ عِنْدَكُمْ سَمَك مَشْوِيّ؟ ask?", "Do you have grilled fish?", ["Is the fish expensive?", "Did you cook the fish?", "Where is the fish market?"], "مَشْوِيّ = grilled."),
        M("What does مَاذَا تُحِبّ أَنْ تَأْكُل؟ ask?", "What do you like to eat?", ["Where do you eat?", "Who is eating?", "How much is the meal?"], "تَأْكُل = you eat."),
        M("What does الْغَدَاء mean?", "lunch", ["dinner", "breakfast", "the bill"], "غَدَاء = lunch."),
        F("أُرِيد ___ سَلَطَة وَحَسَاء.", "طَبَق", ["سُكَّر", "حِذَاء"], "A plate of salad.", tr="I want a plate of salad and soup."),
        F("هَلْ ___ سَمَك مَشْوِيّ؟", "عِنْدَكُمْ", ["عِنْدِي", "عِنْدَهَا"], "To the restaurant staff: Do you (pl.) have …?", tr="Do you have grilled fish?"),
        F("مَاذَا تُحِبّ أَنْ ___؟", "تَأْكُل", ["أَكَلْتُ", "آكِل"], "After أَنْ: a present verb.", tr="What do you like to eat?"),
    ],
    verify=vw("مَطْعَم", "قَائِمَة", "الطَّعَام", "وَجْبَة", "طَبَق", "سَلَطَة", "حَسَاء", "أَرُزّ", "الْأَرُزّ", "مَشْوِيّ", "نَادِل", "غَدَاء", "الْغَدَاء", "عَشَاء", "عِنْدَكُمْ", "عِنْدِي", "عِنْدَهَا", "سَمَك", "اللَّحْم", "تَأْكُل", "أَكَلْتُ", "آكِل", "الْبُيُوت", "مَاذَا", "سُكَّر", "حِذَاء", "آكُل"),
)

# ---------------------------------------------------------------------------- 328
L328 = lesson(
    "A restaurant review (invented)",
    "مَطْعَم الْوَاحَة · الْمَوْقِع · الْأَسْعَار",
    requires=["مطعم", "موقع", "وسط", "مدينة", "سعر", "واسع", "جميل", "سريع", "خدمة", "عمل"],
    cards=[
        card("A review card",
             "A review card gives the name, the location, the working hours, the kind of food, the prices and the way to pay. The restaurant below is invented, so use it only to practise the pattern.",
             tables=[table(["Field", "Arabic"],
                           [["name", "اِسْم الْمَطْعَم"], ["location", "الْمَوْقِع"], ["working hours", "أَوْقَات الْعَمَل"], ["kind of food", "نَوْع الطَّعَام"], ["prices", "الْأَسْعَار"], ["way of paying", "طَرِيقَة الدَّفْع"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Reading the review",
             "Here is a short review of an invented restaurant.",
             examples=[
                 ex("اِسْم الْمَطْعَم: مَطْعَم الْوَاحَة.", "Name of the restaurant: the Oasis Restaurant.", "مَطْعَم الْوَاحَة"),
                 ex("يَقَع الْمَطْعَم فِي وَسَط الْمَدِينَة.", "The restaurant is in the middle of the city.", "وَسَط"),
                 ex("يَفْتَح يَوْمِيًّا لِلْغَدَاء وَالْعَشَاء.", "It opens daily for lunch and dinner.", "يَفْتَح"),
                 ex("الْقَاعَة وَاسِعَة وَجَمِيلَة وَالْخِدْمَة سَرِيعَة.", "The hall is wide and beautiful and the service is fast.", "وَاسِعَة"),
                 ex("الْأَسْعَار مَعْقُولَة وَالدَّفْع نَقْدًا أَوْ بِالْبِطَاقَة.", "The prices are reasonable and payment is in cash or by card.", "مَعْقُولَة"),
                 ex("أَنْصَح بِالسَّمَك الْمَشْوِيّ.", "I recommend the grilled fish.", "أَنْصَح"),
             ]),
    ],
    exercises=[
        M("What does الْمَوْقِع mean?", "the location", ["the price", "the menu", "the waiter"], "مَوْقِع = location."),
        M("What does أَوْقَات الْعَمَل mean?", "working hours", ["kinds of food", "ways of paying", "names"], "أَوْقَات = times."),
        M("What does يَقَع الْمَطْعَم فِي وَسَط الْمَدِينَة mean?", "The restaurant is in the middle of the city", ["The restaurant is far from the city", "The restaurant sells the city", "The city is in the restaurant"], "وَسَط = middle."),
        M("What does الْأَسْعَار مَعْقُولَة mean?", "The prices are reasonable", ["The prices are very high", "The prices are written in Arabic", "The prices are secret"], "مَعْقُول = reasonable."),
        M("What does الدَّفْع نَقْدًا أَوْ بِالْبِطَاقَة mean?", "Payment is in cash or by card", ["Payment is only by card", "Payment is tomorrow", "Payment is free"], "أَوْ = or."),
        M("What does أَنْصَح بِالسَّمَك الْمَشْوِيّ mean?", "I recommend the grilled fish", ["I cook the grilled fish", "I do not like fish", "I want the bill"], "أَنْصَح = I recommend, I advise."),
        F("يَقَع الْمَطْعَم فِي ___ الْمَدِينَة.", "وَسَط", ["نَقْد", "ثَوْب"], "In the middle of the city.", tr="The restaurant is in the middle of the city."),
        F("الْقَاعَة وَاسِعَة وَالْخِدْمَة ___", "سَرِيعَة", ["سَرِيع", "سُرْعَة"], "Feminine adjective for the feminine الْخِدْمَة.", tr="The hall is wide and the service is fast."),
        F("الْأَسْعَار ___", "مَعْقُولَة", ["مَعْقُول", "مَعْقُولُون"], "الْأَسْعَار = things (plural): feminine singular.", tr="The prices are reasonable."),
    ],
    verify=(vv("نصح", "pres", ana="أَنْصَح") + vv("فتح", "pres", huwa="يَفْتَح") + vv("وقع", "pres", huwa="يَقَع")
            + vw("اِسْم", "الْمَطْعَم", "مَطْعَم", "الْوَاحَة", "الْمَوْقِع", "أَوْقَات", "الْعَمَل", "نَوْع", "الطَّعَام", "الْأَسْعَار", "طَرِيقَة", "الدَّفْع", "وَسَط", "الْمَدِينَة", "يَوْمِيًّا", "لِلْغَدَاء", "وَالْعَشَاء", "الْقَاعَة", "وَاسِعَة", "جَمِيلَة", "وَالْخِدْمَة", "سَرِيعَة", "مَعْقُولَة", "بِالْبِطَاقَة", "بِالسَّمَك", "الْمَشْوِيّ", "نَقْدًا", "نَقْد", "ثَوْب", "سَرِيع", "سُرْعَة", "مَعْقُول", "مَعْقُولُون")),
)


# ---------------------------------------------------------------------------- 329
L329 = lesson(
    "Describing a person",
    "طَوِيل · قَصِير · شَعْرُهُ أَسْوَد · يَلْبَس نَظَّارَات",
    requires=["طويل", "قصير", "شعر", "أسود", "لبس", "نظارة", "قميص", "صديق", "رجل", "أخت"],
    cards=[
        card("What you can say",
             "To help a friend recognise someone, say how tall the person is, what the hair is like, and what he or she wears. "
             "The adjective agrees with the person: طَوِيل for a man, طَوِيلَة for a woman. For the hair, use شَعْر + the pronoun: شَعْرُهُ أَسْوَد (“his hair is black”), شَعْرُهَا طَوِيل (“her hair is long”). "
             "The verb يَلْبَس means “wears”.",
             tables=[table(["English", "Masculine", "Feminine"],
                           [["tall", "طَوِيل", "طَوِيلَة"], ["short", "قَصِير", "قَصِيرَة"], ["young", "شَابّ", "شَابَّة"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Finding a friend at the market (invented)",
             "A friend says how to recognise a person.",
             examples=[
                 ex("صَدِيقِي طَوِيل وَشَعْرُهُ أَسْوَد.", "My friend is tall and his hair is black.", "شَعْرُهُ أَسْوَد"),
                 ex("أُخْتِي قَصِيرَة وَشَعْرُهَا طَوِيل.", "My sister is short and her hair is long.", "شَعْرُهَا طَوِيل"),
                 ex("يَلْبَس قَمِيص أَزْرَق وَحِذَاء أَبْيَض.", "He wears a blue shirt and white shoes.", "يَلْبَس"),
                 ex("هِيَ تَلْبَس فُسْتَان أَحْمَر.", "She wears a red dress.", "تَلْبَس"),
                 ex("الرَّجُل الطَّوِيل الَّذِي يَلْبَس نَظَّارَات هُوَ صَدِيقِي.", "The tall man who wears glasses is my friend.", "الَّذِي"),
                 ex("هَلْ هُوَ شَابّ أَمْ كَبِير فِي السِّنّ؟", "Is he young or old?", "شَابّ"),
             ]),
    ],
    exercises=[
        M("Which is the feminine form of طَوِيل?", "طَوِيلَة", ["طُوَال", "طَوِيلُون"], "Feminine adds ـَة."),
        M("What does شَعْرُهَا طَوِيل mean?", "Her hair is long", ["His hair is long", "Her hair is black", "She is tall"], "ـهَا = her."),
        M("What does شَعْرُهُ أَسْوَد mean?", "His hair is black", ["Her hair is black", "His shirt is black", "He is short"], "ـهُ = his."),
        M("What does يَلْبَس mean?", "he wears", ["he sells", "he asks", "he walks"], "لَبِسَ = wore; يَلْبَس = wears."),
        M("What does الرَّجُل الطَّوِيل الَّذِي يَلْبَس نَظَّارَات هُوَ صَدِيقِي mean?", "The tall man who wears glasses is my friend", ["The tall man wants glasses", "My friend is a short man", "The man who is my friend is blue"], "الَّذِي = who."),
        M("What does كَبِير فِي السِّنّ mean?", "old (of a person)", ["very tall", "very new", "very cheap"], "السِّنّ = age."),
        F("أُخْتِي ___ وَشَعْرُهَا طَوِيل.", "قَصِيرَة", ["قَصِير", "قُصَرَاء"], "أُخْتِي is feminine.", tr="My sister is short and her hair is long."),
        F("الرَّجُل الطَّوِيل ___ يَلْبَس نَظَّارَات هُوَ صَدِيقِي.", "الَّذِي", ["الَّتِي", "الَّذِين"], "The relative pronoun agrees with الرَّجُل (masculine singular).", tr="The tall man who wears glasses is my friend."),
        F("هِيَ ___ فُسْتَان أَحْمَر.", "تَلْبَس", ["يَلْبَس", "لَبِسْتُ"], "She: تَلْبَس.", tr="She wears a red dress.", lemma="لبس:pres:hiya"),
    ],
    verify=(vv("لبس", "pres", huwa="يَلْبَس", hiya="تَلْبَس")
            + vw("طَوِيل", "طَوِيلَة", "قَصِير", "قَصِيرَة", "شَابّ", "شَابَّة", "شَعْرُهُ", "شَعْرُهَا", "أَسْوَد", "نَظَّارَات", "السِّنّ", "الرَّجُل", "الطَّوِيل", "أُخْتِي", "صَدِيقِي", "طُوَال", "قُصَرَاء", "طَوِيلُون", "حِذَاء")),
)

# ---------------------------------------------------------------------------- 330
L330 = lesson(
    "Double-letter verbs in the past",
    "مَرَّ · مَرَّتْ · مَرُّوا ← مَرَرْتُ · مَرَرْنَا",
    requires=["مر", "مد", "رد", "عد", "حل", "سوق", "أمس", "مقهى", "محل"],
    cards=[
        card("A verb whose last two root letters are the same",
             "The root of مَرَّ is م ر ر. The second and third letters are the same, so in the dictionary form they are written together with a shadda: مَرَّ, “he passed”. "
             "With هُوَ, هِيَ and هُمْ the shadda stays: مَرَّ, مَرَّتْ, مَرُّوا. "
             "When the ending begins with a consonant (تُ, تَ, تِ, تُمْ, نَا, نَ), the shadda disappears and the two letters are written one after the other: مَرَرْتُ, “I passed”.",
             tables=[table(["Pronoun", "Past of مَرَّ", "English"],
                           [["هُوَ", "مَرَّ", "he passed"], ["هِيَ", "مَرَّتْ", "she passed"], ["هُمْ", "مَرُّوا", "they passed"], ["أَنَا", "مَرَرْتُ", "I passed"], ["أَنْتَ", "مَرَرْتَ", "you passed (m.)"], ["أَنْتِ", "مَرَرْتِ", "you passed (f.)"],
                            ["أَنْتُمْ", "مَرَرْتُمْ", "you passed (pl.)"], ["نَحْنُ", "مَرَرْنَا", "we passed"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "The rule is the same for other double-letter verbs. You will meet رَدَّ (replied, returned), مَدَّ (extended), عَدَّ (counted) and حَلَّ (solved) in later lessons.",
             examples=[
                 ex("مَرَرْتُ بِالسُّوق أَمْسِ.", "I passed by the market yesterday.", "مَرَرْتُ"),
                 ex("هَلْ مَرَرْتَ بِالْمَحَلّ؟", "Did you pass by the shop?", "مَرَرْتَ"),
                 ex("مَرَرْنَا بِالْمَقْهَى فِي الصَّبَاح.", "We passed by the coffee shop in the morning.", "مَرَرْنَا"),
                 ex("مَرَّتْ أُخْتِي بِالْمَحَلّ.", "My sister passed by the shop.", "مَرَّتْ"),
                 ex("مَرَّ الْبَائِع بِالزَّبَائِن.", "The seller passed by the customers.", "مَرَّ"),
             ]),
    ],
    exercises=[
        M("What is the past of مَرَّ with أَنَا?", "مَرَرْتُ", ["مَرَّتُ", "مَرَّ"], "Before تُ the shadda opens: مَرَرْتُ."),
        M("What is the past of مَرَّ with نَحْنُ?", "مَرَرْنَا", ["مَرَّنَا", "مَرَّا"], "Before نَا the shadda opens."),
        M("What is the past of مَرَّ with هِيَ?", "مَرَّتْ", ["مَرَرْتْ", "مَرَرْتُ"], "With هِيَ the shadda stays."),
        M("What does مَرَرْتُ بِالسُّوق أَمْسِ mean?", "I passed by the market yesterday", ["I will pass by the market tomorrow", "You passed by the market", "I bought the market"], "أَمْسِ = yesterday."),
        M("What does هَلْ مَرَرْتَ بِالْمَحَلّ؟ ask?", "Did you pass by the shop?", ["Did I pass by the shop?", "Will you pass by the shop?", "Did she pass by the shop?"], "ـتَ = you (m.)."),
        M("What does مَرَرْنَا بِالْمَقْهَى mean?", "We passed by the coffee shop", ["They passed by the coffee shop", "I passed by the coffee shop", "He drinks coffee"], "ـنَا = we."),
        F("أَنَا ___ بِالسُّوق أَمْسِ.", "مَرَرْتُ", ["مَرَرْتَ", "مَرَّتْ"], "With أَنَا: ـتُ.", tr="I passed by the market yesterday."),
        F("نَحْنُ ___ بِالْمَقْهَى فِي الصَّبَاح.", "مَرَرْنَا", ["مَرَرْتُمْ", "مَرُّوا"], "With نَحْنُ: ـنَا.", tr="We passed by the coffee shop in the morning.", lemma="مرر:past:nahnu"),
        F("هِيَ ___ بِالْمَحَلّ.", "مَرَّتْ", ["مَرَرْتُ", "مَرُّوا"], "With هِيَ: مَرَّتْ.", tr="She passed by the shop.", lemma="مرر:past:hiya"),
    ],
    verify=(vv("مرر", "past", huwa="مَرَّ", hiya="مَرَّتْ", hum="مَرُّوا", ana="مَرَرْتُ", anta="مَرَرْتَ", anti="مَرَرْتِ", antum="مَرَرْتُمْ", nahnu="مَرَرْنَا")
            + vw("مَرَّ", "مَرَّتْ", "مَرُّوا", "مَرَرْتُ", "مَرَرْتَ", "مَرَرْتِ", "مَرَرْتُمْ", "مَرَرْنَا", "بِالسُّوق", "بِالْمَحَلّ", "بِالْمَقْهَى", "الصَّبَاح", "أَمْسِ", "الْبَائِع", "بِالزَّبَائِن", "أُخْتِي", "رَدَّ", "مَدَّ", "عَدَّ", "حَلَّ", "مَرَّتُ", "مَرَّنَا", "مَرَّا", "مَرَرْتْ")),
)

# ---------------------------------------------------------------------------- 331
L331 = lesson(
    "Double-letter verbs in the present",
    "أَمُرّ · تَمُرّ · تَمُرِّينَ · تَمُرُّونَ · نَمُرّ",
    requires=["مر", "مد", "رد", "عد", "حل", "غد", "سوق", "محل", "بعد", "ظهر"],
    cards=[
        card("The present keeps the shadda",
             "In the present, a double-letter verb is built like other verbs: prefix + stem. With أَنَا, أَنْتَ, هُوَ, هِيَ and نَحْنُ the last two letters stay together under a shadda. "
             "Before the endings ـِينَ and ـُونَ the shadda carries the vowel: تَمُرِّينَ, تَمُرُّونَ. The stem vowel of مَرَّ is ḍamma: يَمُرّ.",
             tables=[table(["Pronoun", "Present of مَرَّ", "English"],
                           [["أَنَا", "أَمُرّ", "I pass"], ["أَنْتَ", "تَمُرّ", "you pass (m.)"], ["أَنْتِ", "تَمُرِّينَ", "you pass (f.)"], ["هُوَ", "يَمُرّ", "he passes"], ["هِيَ", "تَمُرّ", "she passes"],
                            ["نَحْنُ", "نَمُرّ", "we pass"], ["أَنْتُمْ", "تَمُرُّونَ", "you pass (pl.)"], ["هُمْ", "يَمُرُّونَ", "they pass"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Add سَـ for the future and لَا for “not”.",
             examples=[
                 ex("أَمُرّ بِالسُّوق كُلّ يَوْم.", "I pass by the market every day.", "أَمُرّ"),
                 ex("سَأَمُرّ بِالْمَحَلّ غَدًا.", "I will pass by the shop tomorrow.", "سَأَمُرّ"),
                 ex("تَمُرِّينَ بِالْمَقْهَى بَعْدَ الظُّهْر.", "You (f.) pass by the coffee shop after noon.", "تَمُرِّينَ"),
                 ex("يَمُرُّونَ بِالْمَحَلّ فِي الصَّبَاح.", "They pass by the shop in the morning.", "يَمُرُّونَ"),
                 ex("لَا أَمُرّ بِالسُّوق يَوْم الْجُمْعَة.", "I do not pass by the market on Friday.", "لَا أَمُرّ"),
             ]),
    ],
    exercises=[
        M("What is the present of مَرَّ with أَنَا?", "أَمُرّ", ["أَمْرُر", "أَمَرَّ"], "Prefix أَ + مُرّ."),
        M("What is the present of مَرَّ with نَحْنُ?", "نَمُرّ", ["نَمْرُر", "يَمُرّ"], "Prefix نَ + مُرّ."),
        M("What is the present of مَرَّ with أَنْتِ?", "تَمُرِّينَ", ["تَمُرّ", "تَمُرُّونَ"], "Feminine ending ـِينَ."),
        M("What is the present of مَرَّ with هُمْ?", "يَمُرُّونَ", ["يَمُرِّينَ", "يَمُرّ"], "Plural ending ـُونَ."),
        M("What does سَأَمُرّ بِالْمَحَلّ غَدًا mean?", "I will pass by the shop tomorrow", ["I passed by the shop yesterday", "I pass by the shop every day", "I sell the shop"], "سَـ = future."),
        M("What does لَا أَمُرّ بِالسُّوق يَوْم الْجُمْعَة mean?", "I do not pass by the market on Friday", ["I pass by the market on Friday", "I did not pass by the market", "I will not buy a market"], "لَا + present = not."),
        F("أَنَا ___ بِالسُّوق كُلّ يَوْم.", "أَمُرّ", ["تَمُرّ", "مَرَرْتُ"], "Present with أَنَا.", tr="I pass by the market every day.", lemma="مرر:pres:ana"),
        F("هُمْ ___ بِالْمَحَلّ فِي الصَّبَاح.", "يَمُرُّونَ", ["تَمُرُّونَ", "يَمُرّ"], "Present with هُمْ.", tr="They pass by the shop in the morning.", lemma="مرر:pres:hum"),
        F("أَنْتِ ___ بِالْمَقْهَى بَعْدَ الظُّهْر.", "تَمُرِّينَ", ["تَمُرُّونَ", "أَمُرّ"], "Present with أَنْتِ.", tr="You (f.) pass by the coffee shop after noon.", lemma="مرر:pres:anti"),
    ],
    verify=(vv("مرر", "pres", ana="أَمُرّ", anta="تَمُرّ", anti="تَمُرِّينَ", huwa="يَمُرّ", hiya="تَمُرّ", nahnu="نَمُرّ", antum="تَمُرُّونَ", hum="يَمُرُّونَ")
            + vv("مرر", "fut", ana="سَأَمُرّ") + vv("مرر", "neg", ana="لَا أَمُرّ")
            + vw("أَمُرّ", "تَمُرّ", "تَمُرِّينَ", "تَمُرُّونَ", "يَمُرّ", "نَمُرّ", "يَمُرُّونَ", "سَأَمُرّ", "بِالسُّوق", "بِالْمَحَلّ", "بِالْمَقْهَى", "كُلّ", "غَدًا", "بَعْدَ", "الظُّهْر", "الْجُمْعَة", "أَمْرُر", "أَمَرَّ", "نَمْرُر")),
)

# ---------------------------------------------------------------------------- 332
L332 = lesson(
    "ظَنَّ: “I think that …”",
    "أَظُنّ أَنَّ · ظَنَنْتُ أَنَّ",
    requires=["ظن", "ثمن", "غالي", "رخيص", "أن", "نعم", "لا", "كل", "هذا", "ذلك"],
    cards=[
        card("A double-letter verb of thinking",
             "ظَنَّ يَظُنّ means “to think, to suppose”. It follows the pattern you know: past ظَنَّ, ظَنَّتْ, ظَنُّوا and ظَنَنْتُ, ظَنَنْتَ, ظَنَنْتِ; present أَظُنّ, تَظُنّ, تَظُنِّينَ, تَظُنُّونَ, يَظُنّ. "
             "After the verb you usually add أَنَّ, “that”, and a sentence. With a pronoun it becomes أَنَّهُ, أَنَّهَا.",
             tables=[table(["Pronoun", "Past", "Present"],
                           [["أَنَا", "ظَنَنْتُ", "أَظُنّ"], ["أَنْتَ", "ظَنَنْتَ", "تَظُنّ"], ["أَنْتِ", "ظَنَنْتِ", "تَظُنِّينَ"], ["هُوَ", "ظَنَّ", "يَظُنّ"], ["هِيَ", "ظَنَّتْ", "تَظُنّ"], ["هُمْ", "ظَنُّوا", "يَظُنُّونَ"]],
                           say=[0, 1, 2], tlit=[1, 2], gloss=False)]),
        card("Giving your opinion",
             "This is a common way to give an opinion.",
             examples=[
                 ex("أَظُنّ أَنَّ الثَّمَن غَالِي.", "I think the price is high.", "أَظُنّ"),
                 ex("هَلْ تَظُنّ أَنَّ هَذَا الْقَمِيص رَخِيص؟", "Do you think this shirt is cheap?", "تَظُنّ"),
                 ex("نَعَمْ، أَظُنّ ذَلِكَ.", "Yes, I think so.", "أَظُنّ ذَلِكَ"),
                 ex("ظَنَنْتُ أَنَّ الْمَحَلّ مَفْتُوح.", "I thought that the shop was open.", "ظَنَنْتُ"),
                 ex("تَظُنِّينَ أَنَّهَا سَتَأْتِي.", "You (f.) think that she will come.", "تَظُنِّينَ"),
                 ex("هُمْ يَظُنُّونَ أَنَّ الْحِذَاء كَبِير.", "They think the shoe is big.", "يَظُنُّونَ"),
             ]),
    ],
    exercises=[
        M("What does أَظُنّ mean?", "I think", ["I paid", "I pass", "I count"], "ظَنَّ = think."),
        M("What is the past of ظَنَّ with أَنَا?", "ظَنَنْتُ", ["ظَنَّتُ", "أَظُنّ"], "Before تُ the shadda opens."),
        M("What is the present of ظَنَّ with أَنْتِ?", "تَظُنِّينَ", ["تَظُنُّونَ", "تَظُنّ"], "Feminine ending ـِينَ."),
        M("What does هَلْ تَظُنّ أَنَّ هَذَا الْقَمِيص رَخِيص؟ ask?", "Do you think this shirt is cheap?", ["Is this shirt your size?", "Did you buy this shirt?", "How much is this shirt?"], "تَظُنّ = you think."),
        M("What does ظَنَنْتُ أَنَّ الْمَحَلّ مَفْتُوح mean?", "I thought that the shop was open", ["I think the shop is closed", "I opened the shop", "The shop thinks I am open"], "ظَنَنْتُ = I thought."),
        M("What does نَعَمْ، أَظُنّ ذَلِكَ mean?", "Yes, I think so", ["No, I did not think so", "Yes, I paid for that", "Yes, that is far"], "ذَلِكَ = that."),
        F("___ أَنَّ الثَّمَن غَالِي.", "أَظُنّ", ["أَمُرّ", "ظَنَّ"], "I think: أَظُنّ.", tr="I think the price is high.", lemma="ظنن:pres:ana"),
        F("ظَنَنْتُ ___ الْمَحَلّ مَفْتُوح.", "أَنَّ", ["هَلْ", "لَنْ"], "“That” after a verb of thinking.", tr="I thought that the shop was open."),
        F("هُمْ ___ أَنَّ الْحِذَاء كَبِير.", "يَظُنُّونَ", ["تَظُنُّونَ", "يَظُنّ"], "Present with هُمْ.", tr="They think the shoe is big.", lemma="ظنن:pres:hum"),
    ],
    verify=(vv("ظنن", "past", ana="ظَنَنْتُ", anta="ظَنَنْتَ", anti="ظَنَنْتِ", huwa="ظَنَّ", hiya="ظَنَّتْ", hum="ظَنُّوا")
            + vv("ظنن", "pres", ana="أَظُنّ", anta="تَظُنّ", anti="تَظُنِّينَ", huwa="يَظُنّ", hiya="تَظُنّ", hum="يَظُنُّونَ", antum="تَظُنُّونَ")
            + vw("أَظُنّ", "ظَنَنْتُ", "ظَنَّ", "ظَنَّتْ", "ظَنُّوا", "أَنَّ", "أَنَّهَا", "أَنَّهُ", "الثَّمَن", "غَالِي", "رَخِيص", "الْقَمِيص", "الْمَحَلّ", "مَفْتُوح", "سَتَأْتِي", "الْحِذَاء", "كَبِير", "ذَلِكَ", "لَنْ", "هَلْ", "ظَنَّتُ")),
)


# ---------------------------------------------------------------------------- 333
L333 = lesson(
    "More double-letter verbs",
    "رَدَّ · عَدَّ · مَدَّ · حَلَّ · ضَلَّ",
    requires=["رد", "عد", "مد", "حل", "مشكلة", "يد", "طريق", "دينار", "محل", "قميص"],
    cards=[
        card("Five verbs to learn",
             "Each of these verbs follows مَرَّ in the past: the shadda opens before تُ, تَ, تِ, نَا. In the present, the shadda stays: أَرُدّ, أَعُدّ, أَمُدّ, أَحُلّ. "
             "The verb ضَلَّ has a kasra in the present: أَضِلّ.",
             tables=[table(["Verb", "I (past)", "I (present)", "English"],
                           [["رَدَّ", "رَدَدْتُ", "أَرُدّ", "to reply, to return (something)"], ["عَدَّ", "عَدَدْتُ", "أَعُدّ", "to count"], ["مَدَّ", "مَدَدْتُ", "أَمُدّ", "to stretch out, to extend"],
                            ["حَلَّ", "حَلَلْتُ", "أَحُلّ", "to solve"], ["ضَلَّ", "ضَلَلْتُ", "أَضِلّ", "to lose (the way)"]],
                           say=[0, 1, 2], tlit=[0, 1, 2], gloss=False)]),
        card("In sentences",
             "Notice which preposition or object each verb takes.",
             examples=[
                 ex("رَدَدْتُ الْقَمِيص إِلَى الْمَحَلّ.", "I returned the shirt to the shop.", "رَدَدْتُ"),
                 ex("عَدَدْتُ الدَّنَانِير ثُمَّ دَفَعْتُ.", "I counted the dinars and then I paid.", "عَدَدْتُ"),
                 ex("مَدَدْتُ يَدِي إِلَى الْبَائِع.", "I stretched out my hand to the seller.", "مَدَدْتُ"),
                 ex("حَلَلْتُ الْمُشْكِلَة.", "I solved the problem.", "حَلَلْتُ"),
                 ex("ضَلَلْتُ الطَّرِيق فِي السُّوق.", "I lost my way in the market.", "ضَلَلْتُ"),
                 ex("أَعُدّ النُّقُود قَبْلَ الدَّفْع.", "I count the money before paying.", "أَعُدّ"),
             ]),
    ],
    exercises=[
        M("What does حَلَلْتُ الْمُشْكِلَة mean?", "I solved the problem", ["I had a problem", "I forgot the problem", "I paid the problem"], "حَلَّ = solve."),
        M("What does ضَلَلْتُ الطَّرِيق mean?", "I lost my way", ["I found the way", "I built a road", "I asked the way"], "ضَلَّ الطَّرِيق = lose the way."),
        M("What does مَدَدْتُ يَدِي mean?", "I stretched out my hand", ["I washed my hand", "I raised the price", "I counted my money"], "مَدَّ = stretch out."),
        M("What does رَدَدْتُ الْقَمِيص إِلَى الْمَحَلّ mean?", "I returned the shirt to the shop", ["I bought the shirt in the shop", "I tried on the shirt", "I sold the shirt"], "رَدَّ = return."),
        M("Which is the present of عَدَّ with أَنَا?", "أَعُدّ", ["أَعْدُد", "تَعُدّ"], "Prefix أَ + عُدّ."),
        M("Which is the past of حَلَّ with أَنَا?", "حَلَلْتُ", ["حَلَّتُ", "حَلَّ"], "The shadda opens before تُ."),
        F("___ الْمُشْكِلَة.", "حَلَلْتُ", ["حَلَّتْ", "حَلُّوا"], "With the subject “I”.", tr="I solved the problem."),
        F("___ يَدِي إِلَى الْبَائِع.", "مَدَدْتُ", ["مَدَّتْ", "مَدُّوا"], "With the subject “I”.", tr="I stretched out my hand to the seller."),
        F("أَنَا ___ الدَّنَانِير ثُمَّ أَدْفَع.", "أَعُدّ", ["تَعُدّ", "عَدَدْتُ"], "Present: ثُمَّ أَدْفَع is also present.", tr="I count the dinars and then I pay."),
    ],
    verify=(vv("ردد", "past", ana="رَدَدْتُ", huwa="رَدَّ") + vv("عدد", "past", ana="عَدَدْتُ", huwa="عَدَّ") + vv("مدد", "past", ana="مَدَدْتُ", huwa="مَدَّ")
            + vv("حلل", "past", ana="حَلَلْتُ", huwa="حَلَّ") + vv("ضلل", "past", ana="ضَلَلْتُ", huwa="ضَلَّ")
            + vv("ردد", "pres", ana="أَرُدّ") + vv("عدد", "pres", ana="أَعُدّ", anta="تَعُدّ") + vv("مدد", "pres", ana="أَمُدّ") + vv("حلل", "pres", ana="أَحُلّ") + vv("ضلل", "pres", ana="أَضِلّ")
            + vw("الْقَمِيص", "الْمَحَلّ", "الدَّنَانِير", "الْبَائِع", "الْمُشْكِلَة", "الطَّرِيق", "السُّوق", "النُّقُود", "الدَّفْع", "يَدِي", "حَلَّتُ", "حَلَّتْ", "حَلُّوا", "مَدَّتْ", "مَدُّوا", "أَعْدُد", "تَعُدّ")),
)

# ---------------------------------------------------------------------------- 334
L334 = lesson(
    "A note about errands (invented)",
    "مَرَرْتُ بِالسُّوق · رَدَدْتُ الْقَمِيص · سَأَمُرّ بِالْمَقْهَى",
    requires=["مر", "رد", "سوق", "خبز", "حليب", "قميص", "مقهى", "ظهر", "عزيز", "تحية"],
    cards=[
        card("A note on the table",
             "Read this friendly note. It uses the double-letter verbs of this chapter in the past, present and future. The names are invented.",
             examples=[
                 ex("عَزِيزِي سَامِي،", "Dear Sami,", "عَزِيزِي"),
                 ex("مَرَرْتُ بِالسُّوق صَبَاحًا ثُمَّ اِشْتَرَيْتُ الْخُبْز وَالْحَلِيب.", "I passed by the market in the morning, then bought bread and milk.", "مَرَرْتُ"),
                 ex("رَدَدْتُ الْقَمِيص إِلَى الْمَحَلّ لِأَنَّهُ كَبِير.", "I returned the shirt to the shop because it is big.", "رَدَدْتُ"),
                 ex("سَأَمُرّ بِالْمَقْهَى بَعْدَ الظُّهْر.", "I will pass by the coffee shop after noon.", "سَأَمُرّ"),
                 ex("أَظُنّ أَنَّكَ تُرِيد قَهْوَة.", "I think you want coffee.", "أَظُنّ"),
                 ex("مَعَ تَحِيَّاتِي، خَالِد.", "With my greetings, Khalid.", "مَعَ تَحِيَّاتِي"),
             ]),
    ],
    exercises=[
        M("What did the writer do in the morning?", "passed by the market and bought bread and milk", ["tried on a hat", "went to the coffee shop", "visited a friend"], "مَرَرْتُ بِالسُّوق صَبَاحًا."),
        M("Why did he return the shirt?", "because it is big", ["because it is cheap", "because it is red", "because it is torn"], "لِأَنَّهُ كَبِير."),
        M("When will he pass by the coffee shop?", "after noon", ["in the morning", "at night", "yesterday"], "بَعْدَ الظُّهْر."),
        M("What does he think Sami wants?", "coffee", ["tea", "juice", "bread"], "تُرِيد قَهْوَة."),
        M("What does مَعَ تَحِيَّاتِي mean?", "with my greetings", ["with my thanks", "with my apologies", "with my friend"], "تَحِيَّات = greetings."),
        M("Which verb in the note is future?", "سَأَمُرّ", ["مَرَرْتُ", "رَدَدْتُ", "أَظُنّ"], "سَـ marks the future."),
        F("___ بِالسُّوق صَبَاحًا.", "مَرَرْتُ", ["أَمُرّ", "مَرَّتْ"], "Past, with the subject “I”.", tr="I passed by the market in the morning."),
        F("___ الْقَمِيص إِلَى الْمَحَلّ لِأَنَّهُ كَبِير.", "رَدَدْتُ", ["أَرُدّ", "رَدَّتْ"], "Past, with the subject “I”.", tr="I returned the shirt to the shop because it is big."),
        F("سَأَمُرّ بِالْمَقْهَى ___ الظُّهْر.", "بَعْدَ", ["قَبْلَ", "مِنْ"], "After noon.", tr="I will pass by the coffee shop after noon."),
    ],
    verify=(vv("مرر", "past", ana="مَرَرْتُ") + vv("ردد", "past", ana="رَدَدْتُ") + vv("مرر", "fut", ana="سَأَمُرّ") + vv("ظنن", "pres", ana="أَظُنّ")
            + vw("عَزِيزِي", "سَامِي", "صَبَاحًا", "وَالْحَلِيب", "وَالْخُبْز", "لِأَنَّهُ", "كَبِير", "الظُّهْر", "قَهْوَة", "تَحِيَّاتِي", "خَالِد", "بِالْمَقْهَى", "بِالسُّوق", "الْمَحَلّ", "تُرِيد", "أَنَّكَ", "قَبْلَ", "بَعْدَ")),
)

# ---------------------------------------------------------------------------- 335
L335 = lesson(
    "Writing an invitation",
    "يَسُرُّنِي أَنْ أَدْعُوَكَ · أَتَمَنَّى أَنْ تَحْضُر",
    requires=["دعوة", "دعا", "عشاء", "بيت", "موعد", "عنوان", "حضر", "تمنى", "ساعة", "سابع"],
    cards=[
        card("Parts of an invitation",
             "An invitation has a greeting, the invitation itself, the time and place, and a closing wish. "
             "The phrase يَسُرُّنِي أَنْ…, “I am pleased to…”, uses the double-letter verb سَرَّ (يَسُرُّ), with the pronoun ـنِي added. "
             "The verb دَعَا يَدْعُو, “to invite”, is one of the defective verbs of an earlier chapter.",
             tables=[table(["Part", "Arabic"],
                           [["greeting", "عَزِيزِي خَالِد"], ["I am pleased to invite you", "يَسُرُّنِي أَنْ أَدْعُوَكَ"], ["to dinner at my house", "إِلَى الْعَشَاء فِي بَيْتِي"], ["the appointment", "الْمَوْعِد"], ["I hope you will attend", "أَتَمَنَّى أَنْ تَحْضُر"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("An invitation (invented)",
             "Here is a short invitation, line by line.",
             examples=[
                 ex("عَزِيزِي خَالِد،", "Dear Khalid,", "عَزِيزِي"),
                 ex("يَسُرُّنِي أَنْ أَدْعُوَكَ إِلَى الْعَشَاء فِي بَيْتِي.", "I am pleased to invite you to dinner at my house.", "يَسُرُّنِي"),
                 ex("الْمَوْعِد: يَوْم الْخَمِيس، السَّاعَة السَّابِعَة مَسَاءً.", "The appointment: Thursday, at seven in the evening.", "السَّاعَة السَّابِعَة"),
                 ex("أَتَمَنَّى أَنْ تَحْضُر.", "I hope you will attend.", "أَتَمَنَّى"),
                 ex("مَعَ أَطْيَب التَّحِيَّات، يُوسُف.", "With best regards, Yusuf.", "أَطْيَب"),
             ]),
    ],
    exercises=[
        M("What does يَسُرُّنِي أَنْ أَدْعُوَكَ mean?", "I am pleased to invite you", ["I forgot to invite you", "You are inviting me", "I will pay you"], "يَسُرُّنِي = it pleases me."),
        M("What does إِلَى الْعَشَاء فِي بَيْتِي mean?", "to dinner at my house", ["to lunch at school", "to the shop with a friend", "to dinner in a restaurant"], "عَشَاء = dinner."),
        M("What does الْمَوْعِد mean?", "the appointment", ["the address", "the menu", "the price"], "مَوْعِد = appointment."),
        M("What does السَّاعَة السَّابِعَة مَسَاءً mean?", "seven in the evening", ["seven in the morning", "one in the evening", "the seventh day"], "السَّابِعَة = seventh (f.)."),
        M("What does أَتَمَنَّى أَنْ تَحْضُر mean?", "I hope you will attend", ["I thank you for attending", "I want to leave", "I forgot your name"], "تَمَنَّى = hope."),
        M("Which verb in this lesson has a doubled letter?", "يَسُرُّ", ["أَدْعُو", "تَحْضُر", "أَكْتُب"], "سَرَّ يَسُرُّ."),
        F("___ أَنْ أَدْعُوَكَ إِلَى الْعَشَاء.", "يَسُرُّنِي", ["يَسْرُرُنِي", "سَرَرْتُ"], "It pleases me: يَسُرُّنِي.", tr="I am pleased to invite you to dinner."),
        F("أَتَمَنَّى ___ تَحْضُر.", "أَنْ", ["لَمْ", "إِذَا"], "Hope that you attend.", tr="I hope you will attend."),
        F("الْمَوْعِد: يَوْم الْخَمِيس، السَّاعَة ___ مَسَاءً.", "السَّابِعَة", ["السَّابِع", "السَّبْعَة"], "Ordinal agreeing with السَّاعَة (f.).", tr="The appointment: Thursday, at seven in the evening."),
    ],
    verify=(vv("دعو", "pres", ana="أَدْعُو") + vv("حضر", "pres", anta="تَحْضُر")
            + vw("يَسُرُّنِي", "أَدْعُوَكَ", "الْعَشَاء", "بَيْتِي", "الْمَوْعِد", "الْخَمِيس", "السَّاعَة", "السَّابِعَة", "مَسَاءً", "أَتَمَنَّى", "تَحْضُر", "عَزِيزِي", "خَالِد", "أَطْيَب", "التَّحِيَّات", "يُوسُف", "يَسُرُّ", "تَحْضُر", "يَسْرُرُنِي", "سَرَرْتُ", "السَّابِع", "السَّبْعَة", "لَمْ", "إِذَا")),
)

# ---------------------------------------------------------------------------- 336
L336 = lesson(
    "Review: shopping, exclamations and double-letter verbs",
    "أَيّ · مَا أَجْمَلَ · مَرَرْتُ · أَمُرّ · أَظُنّ",
    requires=["أي", "ما", "مر", "ظن", "سوق", "ثمن", "قميص", "قهوة", "مطعم", "حساب"],
    cards=[
        card("What to remember",
             "أَيّ + a singular noun asks “which?” and also means “any”. "
             "An exclamation is مَا + أَفْعَلَ + the thing in the accusative: مَا أَجْمَلَ الْقُبَّعَةَ! "
             "Double-letter verbs keep the shadda in the he/she/they past (مَرَّ, مَرَّتْ, مَرُّوا) and open it before consonant endings (مَرَرْتُ, مَرَرْنَا). In the present, the shadda stays: أَمُرّ, تَمُرّ, يَمُرُّونَ.",
             tables=[table(["Structure", "Example", "English"],
                           [["which / any", "أَيّ لَوْن تُحِبّ؟", "Which colour do you like?"], ["exclamation", "مَا أَكْبَرَ هَذَا السُّوقَ!", "How big this market is!"], ["past (I)", "مَرَرْتُ بِالْمَحَلّ", "I passed by the shop"],
                            ["present (I)", "أَمُرّ بِالْمَحَلّ", "I pass by the shop"], ["opinion", "أَظُنّ أَنَّ الثَّمَن غَالِي", "I think the price is high"]],
                           say=[1], tlit=[1], gloss=False)]),
    ],
    exercises=[
        M("Which sentence is an exclamation?", "مَا أَرْخَصَ هَذَا الْقَمِيصَ!", ["مَا ثَمَن هَذَا الْقَمِيص؟", "هَذَا الْقَمِيص رَخِيص."], "مَا + أَفْعَلَ."),
        M("What does أَيّ مَقَاس تُرِيد؟ ask?", "Which size do you want?", ["How much is the size?", "Where is the size?", "Who wants a size?"], "أَيّ = which."),
        M("Which is the past of مَرَّ with أَنَا?", "مَرَرْتُ", ["أَمُرّ", "مَرَّتْ"], "Past, with ـتُ."),
        M("Which is the present of مَرَّ with هُمْ?", "يَمُرُّونَ", ["مَرُّوا", "تَمُرِّينَ"], "Present, plural."),
        M("What does هَلْ تَظُنّ أَنَّ الثَّمَن غَالِي؟ ask?", "Do you think the price is high?", ["What is the price?", "Did you pay the price?", "Is the price written?"], "تَظُنّ = you think."),
        M("What does الْحِسَاب مِنْ فَضْلِكَ ask for?", "the bill", ["the menu", "a glass of water", "the way"], "الْحِسَاب = the bill."),
        F("___ أَجْمَلَ الْقُبَّعَةَ!", "مَا", ["هَلْ", "لَمْ"], "Exclamation starts with مَا.", tr="How beautiful the hat is!"),
        F("نَحْنُ ___ بِالْمَقْهَى كُلّ صَبَاح.", "نَمُرّ", ["أَمُرّ", "يَمُرُّونَ"], "Present with نَحْنُ.", tr="We pass by the coffee shop every morning.", lemma="مرر:pres:nahnu"),
        F("أَنَا ___ الْقَمِيص إِلَى الْمَحَلّ.", "رَدَدْتُ", ["رَدَّتْ", "رَدُّوا"], "Past, with “I”.", tr="I returned the shirt to the shop."),
    ],
    verify=(vv("مرر", "past", ana="مَرَرْتُ", huwa="مَرَّ", hiya="مَرَّتْ", hum="مَرُّوا") + vv("مرر", "pres", ana="أَمُرّ", nahnu="نَمُرّ", hum="يَمُرُّونَ", anti="تَمُرِّينَ") + vv("ردد", "past", ana="رَدَدْتُ")
            + vw("مَا", "أَجْمَلَ", "أَكْبَرَ", "أَرْخَصَ", "الْقُبَّعَةَ", "السُّوقَ", "الْقَمِيصَ", "الْقَمِيص", "مَقَاس", "أَيّ", "الثَّمَن", "غَالِي", "الْحِسَاب", "فَضْلِكَ", "نَمُرّ", "بِالْمَقْهَى", "صَبَاح", "الْمَحَلّ", "هَلْ", "لَمْ", "رَدَّتْ", "رَدُّوا")),
)


UNIT = unit("السُّوق وَالْمَقْهَى: shopping, exclamations and double-letter verbs", [L316, L317, L318, L319, L320, L321, L322, L323, L324, L325, L326, L327, L328, L329, L330, L331, L332, L333, L334, L335, L336])

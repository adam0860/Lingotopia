"""Unit 68: KBC Semester III, Unit 16, Lesson 3 - Cultural Events (문화 행사).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 16, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_NV3 = [("관람하다", "to view; to watch (a show)", "연극, 영화, 축제, 미술품, 전통 예술품"), ("발매하다", "to put on sale; to release", "음반, 신간 도서, CD/DVD, 행사 입장권"), ("시청하다", "to watch (TV)", "TV, 연속극, 영화"), ("청취하다", "to listen to", "라디오, 음반"), ("전시하다", "to exhibit; to display", "미술품, 전통 예술품"), ("동원하다", "to mobilize; to draw (a crowd)", "관객")]
_NOUN3 = [("티브이", "TV; television"), ("음반", "a music disc; an album"), ("관객", "an audience"), ("연극", "a play"), ("연속극", "a TV serial drama"), ("라디오", "a radio"), ("신간 도서", "a newly published book"), ("영화", "a movie"), ("축제", "a festival"), ("미술품", "a work of art"), ("전통 예술품", "a traditional art object"), ("행사 입장권", "an admission ticket to an event")]
_ART3 = [
    ("오는 시월 십사 일부터 이틀 동안 호암 아트홀에서 제 삼십팔 회 전국 어린이 피아노 바이올린 연주대회가 열린다.", "From the 14th of October, for two days, the 38th National Children’s Piano and Violin Competition is held at the Hoam Art Hall."),
    ("호암 아트홀이 후원하는 이 대회에서는 특상 수상 어린이 다섯 명에게 장학금 오십만 원씩을 수여하며, 학년별 금상 은상 동상과 장려상 입상자에게도 상패와 메달을 수여한다.", "In this competition, which the Hoam Art Hall sponsors, scholarships of 500,000 won each are awarded to five children who win the special prize, and plaques and medals are also awarded to the winners of the gold, silver and bronze prizes and the encouragement prize by school year."),
    ("참가를 희망하는 어린이는 참가신청서와 참가비 십이만 원을 시월 이 일까지 호암 아트홀에 제출하면 된다.", "Children who wish to take part only need to submit an application form and a 120,000-won entry fee to the Hoam Art Hall by the 2nd of October."),
]
_ART3W = [("후원하다", "to sponsor; to support"), ("수여하다", "to award; to confer"), ("장학금", "a scholarship"), ("특상", "the special prize"), ("장려상", "an encouragement prize"), ("입상자", "a prize winner"), ("상패", "a plaque"), ("참가신청서", "an application form"), ("참가비", "an entry fee"), ("제출하다", "to submit")]
_HJ3 = [("藝 예", "art", "예술, 연예인"), ("音 음", "sound; voice", "음반, 음성"), ("祝 축", "wish; congratulate", "축제, 축하"), ("送 송", "send", "송금, 방송"), ("劇 극", "play; drama", "연극, 극장")]
_HJW3 = [("예술", "art"), ("연예인", "an entertainer"), ("음반", "a music disc"), ("음성", "the human voice"), ("축제", "a festival"), ("축하", "congratulation"), ("송금", "remittance; wiring (money)"), ("방송", "broadcasting"), ("연극", "a play; a drama"), ("극장", "a theater")]
_FILL3 = [("A", "연예인", "an entertainer (for “a job like a singer or an actor”)"), ("B", "음반", "a music disc (for “I went to buy the newly released ___”)"), ("C", "극장", "a theater (for “where is a nearby ___?”)"), ("D", "송금", "remittance (for “to ___ tuition to my younger sibling”)")]
_REL3 = [("수술", "입원", "an operation: being hospitalized"), ("송년", "연말", "seeing the year out: the end of the year"), ("발음", "언어", "pronunciation: language")]
_L3X = [("수술", "an operation (surgery)"), ("예술", "art"), ("입원", "being hospitalized"), ("미술", "fine art"), ("송년", "seeing the old year out"), ("후년", "the year after next"), ("정년", "retirement age"), ("연말", "the end of the year"), ("발음", "pronunciation"), ("언어", "language"), ("얼음", "ice"), ("마음", "mind; heart")]
L1 = lesson(
    "U16 L3 · Review: culture words and Sino-Korean 藝 音 祝 送 劇",
    "문화 행사 · 단어 복습 · 한자어 복습 · 관람하다 · 발매하다 · 시청하다 · 청취하다 · 전시하다 · 동원하다 · 연주대회 · 藝 音 祝 送 劇",
    requires=[],
    cards=[
        card("단어 복습 1: the verbs and their nouns (my answers)", "The book asks you to write the English meaning of each verb and connect it with the nouns that go with it (a noun may be connected more than once). My answers:", tables=[table(["Verb", "Meaning", "Nouns that go with it"], [list(r) for r in _NV3], say=[0])]),
        card("The nouns", "", tables=[ktable(_NOUN3)]),
        card("단어 복습 2: a newspaper article on a cultural event", "The book gives a short article, “전국 어린이 피아노•바이올린 연주대회” (the national children’s piano and violin competition), and asks you to write the meanings of the underlined words in order; the underlines are not marked in the text. The text is the book’s with the numbers spelled out (10월 14일 → 시월 십사 일; 제 38회 → 제 삼십팔 회; 5명 → 다섯 명; 50만 원 → 오십만 원; 12만 원 → 십이만 원; 10월 2일 → 시월 이 일). The English is mine; below it the words I take to be the underlined ones, with my meanings.", examples=passage(_ART3), tables=[ktable(_ART3W)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ3], say=[2]), ktable(_HJW3)]),
        card("한자어 복습 1: the word for the blank (my answers)", "Choose from the examples the word that fits each sentence: A. 요즘 청소년들에게 가장 인기있는 직업은 가수나 탤런트 같은 ___입니다. B. 새로 나온 ___을/를 사러 갔지만 다 팔려서 살 수가 없었다. C. 영화를 보고 싶은데 가까운 ___이/가 어디 있어요? D. 동생에게 학비를 ___하려고 은행에 가는 길입니다.", tables=[table(["Blank", "Word (my answer)", "Meaning"], [list(r) for r in _FILL3], say=[1])]),
        card("한자어 복습 2: the related word (my answers)", "Circle the word related to the word on the left (A. 수술: 예술, 입원, 미술; B. 송년: 후년, 정년, 연말; C. 발음: 언어, 얼음, 마음).", tables=[table(["Word", "Related word (my answer)", "Meaning"], [list(r) for r in _REL3], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L3X)]),
    ],
    exercises=uniq(
        _tr(_NOUN3, k=3) + _tr(_ART3W, k=3) + _tr(_HJW3, k=3) + _tr(_L3X, k=3) + _tr(_ART3, k=2)
        + [M("What does the syllable 藝 (예) mean?", "art", ["send", "play; drama", "wish"], "예술."), M("What does the syllable 音 (음) mean?", "sound; voice", ["art", "send", "play"], "음반."), M("What does the syllable 祝 (축) mean?", "wish; congratulate", ["art", "sound", "send"], "축하."), M("What does the syllable 送 (송) mean?", "send", ["art", "sound", "wish"], "송금."), M("What does the syllable 劇 (극) mean?", "play; drama", ["art", "sound", "send"], "연극."),
           M("Which verb goes with 영화 (watching it in a theater)?", "관람하다", ["발매하다", "청취하다", "전시하다"], "관람하다."), M("Which verb goes with 라디오?", "청취하다", ["관람하다", "발매하다", "전시하다"], "청취하다."), M("Which verb goes with 연속극?", "시청하다", ["청취하다", "전시하다", "발매하다"], "시청하다."), M("Which verb goes with 미술품?", "전시하다", ["청취하다", "시청하다", "발매하다"], "전시하다."), M("Which verb goes with 음반 (releasing it)?", "발매하다", ["관람하다", "시청하다", "청취하다"], "발매하다."),
           M("Which word is related to 수술?", "입원", ["예술", "미술", "연극"], "Surgery."), M("Which word is related to 송년?", "연말", ["후년", "정년", "내년"], "Year-end."), M("Which word is related to 발음?", "언어", ["얼음", "마음", "음악"], "Language."),
           F("가수나 탤런트 같은 ___이 인기 직업이다. (entertainer)", "연예인", ["극장", "음성"], "연예인."), F("새로 나온 ___을 사러 갔다. (music disc)", "음반", ["송금", "방송"], "음반."), F("동생에게 학비를 ___하려고 은행에 갔다. (remit)", "송금", ["축하", "방송"], "송금."), F("전시회에서 미술품을 ___하고 있습니다. (exhibit)", "전시", ["청취", "시청"], "전시하다."), F("호암 아트홀이 대회를 ___합니다. (sponsor)", "후원", ["참가", "제출"], "후원하다."),
           read_q("연주대회에서 상패와 메달을 수여합니다"), read_q("참가신청서를 제출하면 됩니다"), read_q("가까운 극장이 어디 있어요"), read_q("새로 나온 음반을 사러 갔습니다"), read_q("라디오를 청취합니다")]
    ),
)

# ================================================================== L2 Part 1
_D1 = [("이 책은 잘 알려지지 않은 이탈리아 영화세계를 일차적으로 글과 사진으로 만나볼 수 있는 기회를 제공한다.", "This book offers a chance to meet the little-known world of Italian film first of all through text and photographs."), ("훗날 멋지게 성장할 뉴이탈리아영화제에서 이탈리아 영화를 필름으로 만나 보길 희망하는 독자에게 좋은 안내서가 될 것이다.", "It will be a good guide for readers who hope to meet Italian movies on film at the New Italian Film Festival, which will grow splendidly in the future.")]
_D2 = [("시월 삼십일 일까지, 롯데갤러리 본점.", "Until October 31, Lotte Gallery main branch."), ("살사, 탱고의 유행과 더불어 국내에도 라틴 화가들의 작품이 자주 소개되고 있지만 국가별 작품을 한자리에서 관람하는 건 흔치 않은 기회다.", "With the popularity of salsa and tango, works of Latin painters are often introduced in Korea too, but viewing works country by country in one place is a rare chance."), ("보테로, 이투리아, 콜롬비노의 작품을 기반으로 신예 라틴 화가들의 작품이 어떤 흐름을 이루고 있는지 살펴 보면 좋을 전시다.", "It is an exhibition well worth looking at to see what trend the works of up-and-coming Latin painters are forming, based on the works of Botero, Iturria and Colombino.")]
_D3 = [("시월 십 일까지, 대학로 아트원씨어터.", "Until October 10, Arts One Theater in Daehangno."), ("출연: 문근영, 엄기준, 최광일, 배성우, 진경, 박수민, 신다은, 이재호.", "Cast: Moon Geun-young, Eom Gi-jun, Choi Gwang-il, Bae Seong-woo, Jin Gyeong, Park Su-min, Shin Da-eun, Lee Jae-ho."), ("소문난 잔치에도 먹을 것은 있었다.", "There was something to eat even at the famous banquet."), ("문근영이란 이름표에 한바탕 티켓 파란을 일으킨 연극 클로져.", "The play “Closer,” which caused a big stir in ticket sales with the name tag “Moon Geun-young.”"), ("동명 영화로도 개봉된 패트릭 마버의 천구백구십칠 년 런던 초연작이다.", "It is Patrick Marber’s 1997 London premiere work, which was also released as a film of the same name.")]
_D4 = [("오픈런, 엘지아트센터.", "Open run, LG Arts Center."), ("출연: 이지명, 정진호, 임선우, 김세용, 이주실, 조원희, 정영주, 이성훈 등.", "Cast: Lee Ji-myeong, Jeong Jin-ho, Im Seon-u, Kim Se-yong, Lee Ju-sil, Jo Won-hui, Jeong Yeong-ju, Lee Seong-hun and others."), ("열한 살 소년 빌리가 무대 위로 날아올랐다.", "The eleven-year-old boy Billy flew up onto the stage."), ("이천 년 동명 영화로 국내에 소개됐던 빌리 엘리어트가 뮤지컬로 옷을 갈아입고 비영어권 국가로는 처음으로 한국 무대에 섰다.", "Billy Elliot, which was introduced in Korea as a film of the same name in 2000, changed its clothes into a musical and stood on the Korean stage for the first time among non-English-speaking countries.")]
_SPEAK3 = [("교통사고를 당한 적이 있습니까?", "Have you ever been in a traffic accident?"), ("교통사고를 목격한 적이 있습니까?", "Have you ever witnessed a traffic accident?"), ("언제 어디서 어떤 일이 있었는지 친구와 말해 보세요.", "Tell a friend when, where and what happened.")]
_PEOPLE3 = [("영수는 대학에서 미술을 전공하고 있습니다. 다음 학기에는 남미 미술에 관한 과목을 들을 계획입니다.", "Yeongsu is majoring in art at university. Next semester he plans to take a course on South American art."), ("지영이는 모든 문화 행사에 관심이 많습니다. 연극영화과에 다니고 있기 때문에 좋은 연극 공연이 있으면 찾아서 보는 편입니다.", "Jiyeong is interested in all cultural events. Because she attends the department of theater and film, she tends to look for and see good plays."), ("김상범 씨 가족은 주말에 아이들과 함께 볼 수 있는 공연을 알아보고 있습니다. 춤과 노래 그리고 어린 아이들이 나오는 공연이면 좋을 것 같습니다.", "Mr. Kim Sang-beom’s family is looking into a performance they can see with the children on the weekend. A performance with dance, songs and young children would be good."), ("철민이는 이탈리아 영화에 관심이 많습니다. 어렸을 때 본 영화 시네마 천국을 너무 좋아하기 때문입니다.", "Cheolmin is very interested in Italian movies, because he liked the movie “Cinema Paradiso,” which he saw as a child, very much.")]
L2 = lesson(
    "U16 L3 · Part 1 (도입 학습): four cultural-column items",
    "도입 학습 · 문화란 · 이탈리아 영화 · 라틴 화가 전시 · 연극 클로져 · 뮤지컬 빌리 엘리어트 · 소문난 잔치 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3 (Reading): four items from a newspaper culture column",
             "The following are four items introduced in a newspaper culture column (Text and images © Hankyoreh). The titles are missing from the items; you match them below. The text is the book’s with the dates and numbers spelled out; the telephone numbers are left out; the title marks < > and ‘ ’ are removed; and in the last item the English “I’m Free.” that the book quotes is left out of the Korean because it cannot be read aloud. The English is mine.\n\nItem 1 (a book):",
             examples=passage(_D1)),
        card("학습활동 3: Item 2 (an exhibition)", "Item 2:", examples=passage(_D2)),
        card("학습활동 3: Item 3 (a play)", "Item 3:", examples=passage(_D3)),
        card("학습활동 3: Item 4 (a musical)", "Item 4 (the quotation in English, “I’m Free.”, is left out of the Korean):", examples=passage(_D4)),
        card("학습활동 3: the questions answered (mine)",
             "1. The titles: [공연] ‘무대가 좋다’ – 연극 클로져 → 3; [전시] 마법 같은 그림이 온다 → 2; [도서] 영화로 떠나는 시네마 천국 – 이탈리아 영화로 향하는 이정표 → 1; [공연] 빌리, 화려하게 무대로 날아 올라 → 4.\n\n"
             "2. The interests: Yeongsu (art major, South American art) → 2; Jiyeong (theater and film department, good plays) → 3; the Kim Sang-beom family (a performance with dance, songs and young children) → 4; Cheolmin (Italian movies, Cinema Paradiso) → 1.\n\n"
             "3. The underlined sentences are not marked in the text. The sentences of the descriptions are translated above; the one most likely underlined, the proverb sentence in item 3, is “There was something to eat even at the famous banquet.”",
             examples=passage(_PEOPLE3)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK3)),
        card("Activities left out", "학습활동 1 (Reading): choosing two cultural events on the culture section of the Seoul city website (www.seoul.go.kr) and writing their titles and details in English. 학습활동 2 (Listening, tracks 001 to 004): YTN news on several cultural events, with a table of type of event and place or date. 학습활동 4 (Video, track 005): an introduction to a cultural facility in North Korea — the name of the site, its facilities, business hours and days closed, and the North Korean words for 변화하다 and 영업 시간. They are web, audio and video."),
    ],
    exercises=uniq(
        _tr(_D1 + _D2 + _D3 + _D4, k=3) + _tr(_SPEAK3, k=2)
        + [M("Which item is the book about Italian film?", "Item 1", ["Item 2", "Item 3", "Item 4"], "이탈리아 영화세계."), M("Which item is the exhibition of Latin painters?", "Item 2", ["Item 1", "Item 3", "Item 4"], "라틴 화가."), M("Which item is the play Closer?", "Item 3", ["Item 1", "Item 2", "Item 4"], "클로져."), M("Which item is the musical Billy Elliot?", "Item 4", ["Item 1", "Item 2", "Item 3"], "빌리 엘리어트."),
           M("Which item suits an art major interested in South American art?", "Item 2", ["Item 1", "Item 3", "Item 4"], "영수."), M("Which item suits a family looking for dance, songs and young children?", "Item 4", ["Item 1", "Item 2", "Item 3"], "김상범 씨 가족."), M("Which item suits a fan of Italian movies?", "Item 1", ["Item 2", "Item 3", "Item 4"], "철민."),
           M("Where was Closer first staged, per the text?", "London (1997)", ["New York", "Paris", "Seoul"], "런던 초연작."), M("How old is Billy?", "Eleven", ["Twenty", "Five", "Fifteen"], "열한 살."), M("What is special about Billy Elliot in Korea?", "First time in a non-English-speaking country", ["It was a free show", "It was the shortest", "It was silent"], "비영어권 국가로는 처음."),
           F("그 영화는 올해 ___되었습니다. (released)", "개봉", ["철거", "폐업"], "개봉."), F("이 영화는 ___ 소설을 원작으로 만들었습니다. (same name)", "동명", ["유명", "무명"], "동명."), F("아이들은 ___에 관한 이야기를 좋아한다. (magic)", "마법", ["표절", "방침"], "마법."), F("___에 따라 좌회전을 하세요. (signpost)", "이정표", ["운치", "인파"], "이정표."), F("저는 ___한 옷이 좋아요. (fancy)", "화려", ["희한", "선량"], "화려하다."),
           read_q("이 책은 이탈리아 영화세계를 소개합니다"), read_q("연극 클로져는 런던에서 초연되었습니다"), read_q("빌리 엘리어트가 뮤지컬로 한국 무대에 섰습니다"), read_q("소문난 잔치에도 먹을 것은 있었습니다"), read_q("교통사고를 목격한 적이 있습니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("재현(하다/되다)", "(再現) reenactment (to reenact/to be reenacted)", "이 영화에서 주인공 배우가 케네디 대통령을 잘 재현해 냈습니다.", "재생하다"),
    ]),
    ("학습활동 3", [
        ("개봉(하다/되다)", "(開封) release (to release/to be released)", "이번 십일 월에 해리포터 마지막 편이 개봉됩니다."),
        ("동명", "(同名) the same name", "이 영화는 동명 소설을 원작으로 만들었습니다.", "동명이인 同名異人(같은 이름 다른 사람)"),
        ("마법", "(魔法) spell; sorcery; witchcraft; black magic", "아이들은 마법에 관한 이야기를 좋아한다."),
        ("소문난 잔치에 먹을 것 없다", "(proverb) great boast and small roast; much noise and no substance; “There is little to eat at a famous banquet.”", ""),
        ("이정표", "(里程標) a signpost; a milestone", "이정표에 따라 좌회전을 하세요."),
        ("화려하다", "(華麗) to be fancy; to be showy; to be colorful", "저는 화려한 옷이 좋아요."),
    ]),
    ("학습활동 4", [
        ("돋구다", "to heighten (interest)", "응원단들이 축구 경기의 흥을 돋구고 있다."),
        ("변모(하다/되다)", "(變貌) change (in appearance or shape) (to change/to be changed)", "한국전쟁이후 한국은 크게 변모했습니다."),
        ("운치", "(韻致) classical grace and dignity; elegance", "가을의 공원은 운치가 있다."),
        ("황홀하다", "(恍惚) to be ecstatic; to be in ecstasy; to be in rapturous delight", "이곳의 경치가 황홀할 정도로 아름답습니다."),
        ("희한하다", "(稀罕) to be rare; to be strange; to be unusual; to be odd", "그가 화를 내다니 희한한 일이다.", "드물다, 이상하다"),
    ]),
]
L3 = lesson(
    "U16 L3 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 재현 · 개봉 · 동명 · 마법 · 소문난 잔치 · 이정표 · 화려하다 · 돋구다 · 변모 · 운치 · 황홀하다 · 희한하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 개봉 has 11월 (written 십일 월 here). The proverb is listed as 소문난 잔치에 먹을 것 없다 (the entry is written without the final period).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=8, nread=6)),
)

# ================================================================== L4 Part 2 texts
_FILMS = [
    ("레터스 투 줄리엣", "Letters to Juliet", "개리 위닉", "Gary Winick", "아만다 시프리드, 가엘 가르시아 베르날", "Amanda Seyfried, Gael García Bernal", [
        ("박평식", "어르신 잔치에 흥을 깨는 청춘들.", "Youths who spoil the fun at the elders’ party.", "★★☆"),
        ("이용철", "배우, 풍경, 이야기가 다 마음을 사로잡는다.", "The actors, scenery and story all capture your heart.", "★★★"),
        ("이주현", "내년 휴가지는 정해졌다. 이탈리아의 베로나다.", "Next year’s vacation spot is decided. It is Verona, Italy.", "★★★☆")]),
    ("대부 2", "The Godfather Part II", "프란시스 포드 코폴라", "Francis Ford Coppola", "알 파치노, 로버트 듀발", "Al Pacino, Robert Duvall", [
        ("김봉석", "입 닥치고 당장 봐야 할 영화.", "A movie you must watch right now, no questions asked.", "★★★★★"),
        ("박평식", "황홀과 전율, 속편의 최고봉.", "Ecstasy and thrill, the summit of sequels.", "★★★★☆"),
        ("유지나", "전편과 겨루는 이 편, 숭고한 비장 남성미의 상징판.", "This second film that competes with the first, a symbol edition of sublime, solemn masculine beauty.", "★★★★")]),
    ("방가? 방가!", "Bangga? Bangga!", "육상효", "Yuk Sang-hyo", "김인권, 김정태", "Kim In-gwon, Kim Jeong-tae", [
        ("김도훈", "참 착하다. 혹은, 너무 착하다.", "It is really kind. Or, too kind.", "★★☆"),
        ("이동진", "중반까진 재미있게 봤지만.", "I enjoyed it up to the middle, but.", "★★☆"),
        ("이용철", "열심히 만들었군요. 잘되길 빌게요.", "You made it with effort. I wish you well.", "★★★"),
        ("이주현", "촌스럽지만 선한 영화.", "A boorish but good-hearted film.", "★★☆"),
        ("황진미", "그들의 노래를 들을 귀를 가지고 있는가?", "Do you have ears to hear their song?", "★★★☆")]),
    ("먹고, 기도하고, 사랑하라", "Eat Pray Love", "라이언 머피", "Ryan Murphy", "줄리아 로버츠, 하비에르 바르뎀", "Julia Roberts, Javier Bardem", [
        ("박평식", "지루하진 않으나 새로울 것 없는 여정.", "Not boring, but a journey with nothing new.", "★★☆"),
        ("이용철", "진짜 힘겨운 사람이 보면 욕부터 나올 영화.", "A film that would make a truly struggling person swear first.", "★☆"),
        ("정한석", "진지한 건 좋은데 조금 심심합니다.", "Being serious is good, but it is a little dull.", "★★☆")]),
]
_SPEAK3B = [("반 학생들이 같이 본 한국 드라마나 한국 영화 중에서 하나를 골라 줄거리를 서로 이야기해 보세요.", "Choose one of the Korean dramas or Korean films the class students watched together and tell each other the plot."), ("미국의 티브이 프로그램이나 영화 중에서 가장 잘 되었다고 생각하는 것을 골라 한국말로 소개해 보세요.", "Choose the American TV program or movie you think was the most successful and introduce it in Korean.")]
_cards_f = []
for _k, (_t, _te, _d, _de, _a, _ae, _rv) in enumerate(_FILMS):
    _cards_f.append(card(
        "학습활동 1: film %d, %s (%s)" % (_k + 1, _t, _te),
        "Director: %s (%s). Actors: %s (%s). The reviews below are the critics’ lines as printed, with “!” written as a full stop; the star ratings are the book’s (full star = 1, half = ☆), kept in the last column. The English is mine." % (_d, _de, _a, _ae),
        tables=[table(["Critic", "Review", "Meaning", "Stars"], [[a, b, c, s] for a, b, c, s in _rv], say=[0, 1])]))
_RVALL = [(b, c) for f in _FILMS for (a, b, c, s) in f[6]]
L4 = lesson(
    "U16 L3 · Part 2 (본 학습): four short film reviews",
    "본 학습 · 영화 평 · 레터스 투 줄리엣 · 대부 2 · 방가? 방가! · 먹고, 기도하고, 사랑하라 · 속편 · 최고봉 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading · Writing): short film introductions and reviews", "The book gives short introductions and critics’ comments on four films (Text and images © Hankyoreh), and asks you to choose two films, write the title, director and leading actors in English, and translate the underlined part of the review (the underlines are not marked in the text, so every review is translated here). Then you choose one film and write, in English and in Korean, why you would recommend it to a friend."),
    ] + _cards_f + [
        card("학습활동 1: my answer to question 2 (a sample)", "Selected film: 대부 2 (The Godfather Part II). Reason (Korean): 이 영화는 속편의 최고봉이라고 합니다. 전율을 느낄 수 있는 영화이니까 친구에게 추천하고 싶습니다. (This film is said to be the summit of sequels. Since it is a film that gives you a thrill, I would like to recommend it to a friend.)"),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK3B)),
        card("Activities left out", "학습활동 2 (Video, track 006): a video on North Korean art — what kind of art is introduced, a summary of its contents, and the roles of the people named in the credits (김문화, 서정운, 차철우, 윤정호). 학습활동 3 (Listening, track 007): TV culture news — which holiday is celebrated with special discounts and performances, the performances introduced, and the details of a 40% and a 30% discount. They are audio and video."),
    ],
    exercises=uniq(
        _tr(_RVALL, k=3) + _tr([(f[0], f[1]) for f in _FILMS], k=3) + _tr(_SPEAK3B, k=2)
        + [M("Who directed 대부 2?", "Francis Ford Coppola", ["Gary Winick", "Ryan Murphy", "Yuk Sang-hyo"], "프란시스 포드 코폴라."), M("Who directed 레터스 투 줄리엣?", "Gary Winick", ["Ryan Murphy", "Francis Ford Coppola", "Yuk Sang-hyo"], "개리 위닉."), M("Who stars in 먹고, 기도하고, 사랑하라?", "Julia Roberts", ["Al Pacino", "Amanda Seyfried", "Kim In-gwon"], "줄리아 로버츠."), M("Who stars in 대부 2?", "Al Pacino", ["Julia Roberts", "Amanda Seyfried", "Kim Jeong-tae"], "알 파치노."), M("Which film got five stars from 김봉석?", "대부 2", ["방가? 방가!", "레터스 투 줄리엣", "먹고, 기도하고, 사랑하라"], "★★★★★."), M("Which critic calls 대부 2 the summit of sequels?", "박평식", ["이동진", "황진미", "정한석"], "속편의 최고봉."), M("Which film gets the comment that a truly struggling person would swear first?", "먹고, 기도하고, 사랑하라", ["대부 2", "방가? 방가!", "레터스 투 줄리엣"], "욕부터 나올 영화."), M("Which critic decided the next vacation spot from a film?", "이주현", ["이동진", "황진미", "정한석"], "베로나."),
           F("그 영화는 ___의 최고봉입니다. (sequel)", "속편", ["여정", "청춘"], "속편."), F("무서운 영화를 보고 ___을 느꼈다. (a shudder)", "전율", ["지루", "촌스러움"], "전율."), F("그 영화는 너무 길고 ___. (boring)", "지루했다", ["진지했다", "참신했다"], "지루하다."), F("옆집 할머니는 인상이 아주 ___. (good)", "선하시다", ["악하시다", "촌스러우시다"], "선하다."), F("유행이 지난 옷을 입으면 ___ 보인다. (outdated)", "촌스러워", ["세련돼", "매끄러워"], "촌스럽다."),
           read_q("이 영화는 속편의 최고봉입니다"), read_q("그 영화는 너무 길고 지루했습니다"), read_q("진지한 건 좋은데 조금 심심합니다"), read_q("내년 휴가지는 이탈리아로 정해졌습니다"), read_q("한국 영화 줄거리를 이야기해 보세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("매끄럽다", "to be smooth; to be sleek", "머릿결이 참 매끄럽네요.", "거칠다"),
        ("선하다", "(善) to be good; to be nice", "옆집 할머니는 인상이 아주 선하시다.", "악하다"),
        ("속편", "(續篇) a sequel (of a movie or a book, etc.)", "반지의 제왕 속편이 인기를 많이 얻고 있습니다."),
        ("여정", "(旅程) an itinerary; a journey; the plan for one’s journey", "이번 여행은 여정은 길었지만, 아주 즐거웠어요.", "일정"),
        ("전율(하다)", "(戰慄) shuddering or trembling (from emotion such as fear, horror, or elation) (to shudder; to tremble)", "무서운 영화를 보고 전율을 느꼈다."),
        ("지루하다", "to be (long and) boring/bored; to be dull; to be tedious", "그 영화는 너무 길고 지루했다.", "따분하다, 심심하다"),
        ("진지하다", "(眞摯) to be serious; to be earnest", "김 선생님은 항상 진지하셔서 이야기를 하기가 어렵습니다."),
        ("청춘", "(靑春) youth", "이 선생님은 동생들 가르치는 데 청춘을 다 보내셨어요."),
        ("초현실적", "(超現實的) surreal(istic)", "이 영화에 나오는 장면들은 다 초현실적입니다."),
        ("촌스럽다", "to be boorish; to be rustic; to be countrified; to be unsophisticated; to be unrefined; to be outdated", "유행이 지난 옷을 입으면 촌스러워 보인다.", "세련되다"),
        ("최고봉", "(最高峰) the highest achievement; masterwork; “the highest peak”", "이 작품은 현대미술계의 최고봉입니다."),
        ("힘겹다", "to be hard; to be difficult", "이 일은 저에게는 너무 힘겨운 일입니다."),
    ]),
    ("학습활동 2", [
        ("감명 깊다", "(感銘) to be deeply impressive", "대통령의 연설이 아주 감명 깊었다.", "감동"),
        ("애국적", "(愛國的) patriotic", "외국에 나가 살면 애국적이 됩니다."),
        ("양심", "(良心) conscience", "양심에 걸려서 거짓말은 못 하겠다."),
        ("영웅", "(英雄) a hero; a heroine", "김연아 선수가 올림픽에서 금메달을 따면서 국민적 영웅이 되었습니다."),
        ("진실하다", "(眞實) to be honest; to be truthful; to be sincere; to be genuine", "저는 그 사람이 아주 진실해서 좋습니다."),
        ("참신하다", "(斬新) to be fresh; to be refreshingly new", "이 가방은 디자인이 아주 참신하다.", "새롭다"),
        ("화면", "(畵面) a screen; a monitor; a picture", "컴퓨터 바탕 화면을 다운받았다."),
    ]),
    ("학습활동 3", [
        ("강제", "(强制) compulsion; coercion", "저는 얼마 전에 회사에서 강제 퇴직을 당했어요."),
        ("원작", "(原作) an original work", "이 영화의 원작이 무엇입니까?"),
        ("철거(하다/당하다)", "(撤去) demolishing (to demolish/to be demolished)", "무허가 건물을 철거하다."),
    ]),
]
L5 = lesson(
    "U16 L3 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 매끄럽다 · 선하다 · 속편 · 여정 · 전율 · 지루하다 · 진지하다 · 청춘 · 촌스럽다 · 최고봉 · 힘겹다 · 감명 깊다 · 양심 · 영웅 · 진실하다 · 참신하다 · 화면 · 강제 · 원작 · 철거",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 여정 reads 이번 여행은 여정은 길었지만; it is kept as printed. The book’s example for 감명 깊다 uses the related word 감동.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3 texts
_GIRL = [
    ("소녀시대와 카라 등 한국 걸그룹 인기가 일본에서 하늘을 찌른다고 하여 제작진이 찾아간 일본 도쿄 시부야 거리.", "The streets of Shibuya in Tokyo, Japan, which the production team visited because it was said that the popularity of Korean girl groups such as Girls’ Generation and Kara pierces the sky in Japan."),
    ("이쪽을 보면 카라, 저쪽을 보면 소녀시대로 “여기가 서울이야?” 할 정도로 어리둥절해 하며 시부야 타워 레코드 매장에 들어갔다.", "Looking this way, Kara; looking that way, Girls’ Generation — so much so that one says, “Is this Seoul?” — bewildered, they entered the Shibuya Tower Records store."),
    ("이 매장은 지난 팔 월 엄청난 인파로 카라의 게릴라 콘서트가 삼 분 만에 중단된 흥행 이후 코리아 팝 케이팝 코너 매장을 아예 따로 떼어 냈을 정도로 인기가 높았다.", "This store was so popular that after the box-office success in August, when Kara’s guerrilla concert was halted after three minutes because of a tremendous crowd, it set up a separate K-POP corner store altogether."),
    ("인기를 증명하듯 일본 현지에서 발매된 카라의 카라 베케이션이 오리콘 주간 블루레이 디스크 아이돌 이미지부문에서 일 위를 차지한 데 이어 소녀시대의 소원을 말해봐 일본어 버전인 지니는 오리콘 일간 싱글차트 이 위를 기록하며 역대 최고의 순위를 기록했다.", "As if to prove the popularity, Kara’s “KARA VACATION,” released locally in Japan, took first place in the Oricon weekly Blu-ray Disc idol image category, and following that, Girls’ Generation’s “Genie,” the Japanese version of “Tell Me Your Wish,” recorded second place on the Oricon daily singles chart, recording the best ranking ever."),
    ("미국의 빌보드 차트와 더불어 양대 산맥인 오리콘은 오리지널 컨피던스, 절대적 신뢰의 줄임말로 매주 월요일부터 칠 일 동안 시디, 디브이디 판매량을 집계하여 화요일에 그 순위를 발표한다.", "Oricon, which together with America’s Billboard chart is one of the two great mountain ranges, is short for “Original Confidence” (absolute trust), and it totals the sales of CDs and DVDs for seven days from Monday every week and announces the ranking on Tuesday."),
    ("제작진을 만난 다나카 히시카츠 오리콘 편집장은 “한국 걸그룹의 인기는 실제로 대단하다”며 아시아 여성그룹의 진출 삼십 년 만에 이룬 쾌거라고 평가했다.", "Tanaka Hishikatsu, the Oricon editor in chief who met the production team, said, “The popularity of Korean girl groups is truly great,” and evaluated it as a splendid achievement made in 30 years since Asian female groups advanced there."),
    ("십 대 여성들은 코스튬 플레이 일명 코스프레로 한국의 걸그룹과 똑같은 복장과 헤어스타일을 흉내내는 것을 문화코드로 인식하고 있다.", "Women in their teens recognize imitating the very same costumes and hairstyles as Korean girl groups through costume play, also called cosplay, as a cultural code."),
    ("특히 우리나라에서는 걸그룹에 대해 스타성과 상품성의 이미지가 강한 반면 일본의 십 대 팬들은 한국의 걸그룹에 대해 다년간의 연습 생활과 고된 훈련을 거쳐 단련된 뮤지션 또는 실력파 아티스트라는 타이틀을 더 강하게 부여하고 있었다.", "In particular, while in our country the image of star quality and marketability is strong for girl groups, Japanese teenage fans were giving Korean girl groups more strongly the title of musicians or skilled artists trained through many years of practice life and hard training."),
    ("일본에 부는 신한류 열풍은 실로 대단하다.", "The new Korean Wave craze blowing in Japan is truly great."),
    ("그러나 이 정도 인기로는 부족하다.", "But popularity at this level is not enough."),
    ("판을 키우고 살을 찌워 한국의 대단한 걸그룹이 일본을 발판삼아 월드걸로 성장하길 바란다.", "I hope that, by enlarging the arena and fattening up, Korea’s great girl groups will use Japan as a stepping stone and grow into world girls."),
]
_SPEAK3C = [("요즘 한국 가요계에는 어린 아이돌들이 대세를 이루고 있습니다.", "Nowadays in the Korean pop music world young idols are forming the main trend."), ("이런 영향으로 많은 어린 학생들이 연예계에 진출하기 위해 어려서부터 평범한 생활을 포기하는 경우가 많습니다.", "Because of this influence, many young students give up an ordinary life from an early age in order to enter show business."), ("어린 나이에 연예계에 진출하는 것에 대해서 찬반 두 그룹으로 나누어 토론해 보세요.", "Divide into two groups, for and against, and debate about entering show business at a young age.")]
L6 = lesson(
    "U16 L3 · Part 3 (심화 학습): Korean girl groups in Japan and Nam June Paik",
    "심화 학습 · 백남준 · 걸그룹 · 소녀시대 · 카라 · 신한류 · 오리콘 · 게릴라 콘서트 · 코스프레 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 한국 비디오 예술가 백남준 (the Korean video artist Nam June Paik) — the book’s note",
             "Nam June Paik (20 July 1932–29 January 2006) was a Korean-born American artist. He worked with a variety of media and is considered the first video artist. In 1964, Paik moved to New York and began working with classical cellist Charlotte Moorman to combine video, music, and performance. In the work TV Cello, the pair stacked televisions on top of one another so they formed the shape of a cello. When Moorman drew her bow across the “cello,” images of her and other cellists playing appeared on the screens. In 1965, Sony introduced the Portapak (though it is said that Paik had a similar device before Sony released the Portapak). With this device, Paik could both move and record things, making it the first portable video and audio recorder. From there, Paik became an international celebrity, known for his creative and entertaining work. (Image © Wikipedia, Lim Young-kyun.)"),
        card("학습활동 1 (Reading): a newspaper article on Korean girl groups in Japan",
             "The following is a newspaper article on the activities and popularity of Korean idol girl groups in Japan (Text and image © Hankyoreh). The text is the book’s with the numbers and foreign words spelled in Hangul (8월 → 팔 월; 3분 → 삼 분; 1위 → 일 위; 2위 → 이 위; 7일 → 칠 일; 30년 → 삼십 년; 10대 → 십 대; KOREA-POP(K-POP) → 코리아 팝 케이팝; KARA VACATION → 카라 베케이션; Genie → 지니; Original Confidence → 오리지널 컨피던스; CD, DVD → 시디, 디브이디; the Hanja 東京 and the “(?)” after 중단 are left out); the quotation marks ‘ ’ are removed. The English is mine.",
             examples=passage(_GIRL)),
        card("학습활동 1: the questions answered (mine)",
             "1. C — hyperbole. “The popularity pierces the sky” exaggerates how high the popularity is (it is not a metaphor or simile, since nothing is compared, and the sky is not literally pierced).\n\n"
             "2. Evidence — An event: Kara’s guerrilla concert at the Shibuya Tower Records store last August was halted after three minutes because of an enormous crowd, and the store then set up a separate K-POP corner. Ranking in music charts: Kara’s “KARA VACATION” took first place in the Oricon weekly Blu-ray Disc idol image category; Girls’ Generation’s “Genie” (Japanese version of “Tell Me Your Wish”) reached second place on the Oricon daily singles chart, the highest ranking ever. What fans do: teenage girls do cosplay, imitating the Korean girl groups’ costumes and hairstyles, and see it as a cultural code.\n\n"
             "3. In Korea girl groups have a strong image of star quality and marketability; Japanese teenage fans more strongly see them as musicians or skilled artists trained through many years of practice and hard training.\n\n"
             "4. The writer hopes that Korean girl groups will use Japan as a stepping stone — enlarging the arena and growing bigger — and become “world girls.”"),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine; the book writes 아이돌 followed by “(idol)”):", examples=passage(_SPEAK3C)),
        card("Activities left out", "학습활동 2 (Video, track 008): a YTN news item on the Korean artist Nam June Paik — the relationship between Mr. Paik and Mrs. Kubota (wife, artistic colleague, mother, artistic rival), what happened to Mr. Paik in 1972, and the meaning of his written statement about Mrs. K, 젊었을 때는 최고의 연인, 늙으니 최고의 어머니, 부처가 됐다 (when young, the best lover; now old, the best mother — a Buddha). 학습활동 3 (Listening · Speaking, tracks 009 and 010): a radio program on a cultural issue (copyright infringement, plagiarism, counterfeiting or mimicking a famous singer; singer Lee Hyo-ri’s reaction; information about 바누스; how the problem was exposed; what she and her management company will do). These are audio and video."),
    ],
    exercises=uniq(
        _tr(_GIRL, k=3) + _tr(_SPEAK3C, k=2)
        + [M("Where did the production team go?", "Shibuya in Tokyo", ["Osaka", "Seoul", "Kyoto"], "일본 도쿄 시부야."), M("Which two girl groups are named?", "Girls’ Generation and Kara", ["Wonder Girls and 2NE1", "Black Pink and Twice", "Apink and Mamamoo"], "소녀시대, 카라."), M("What happened to Kara’s guerrilla concert?", "It was halted after three minutes by the crowd", ["It was cancelled by rain", "It lasted all night", "It was moved to Seoul"], "삼 분 만에 중단."), M("What place did Kara’s album take in the Oricon weekly category?", "First", ["Second", "Tenth", "Last"], "일 위."), M("What place did “Genie” take on the daily singles chart?", "Second", ["First", "Fifth", "Tenth"], "이 위."), M("What does Oricon stand for?", "Original Confidence", ["Original Condition", "Official Contest", "Only Concert"], "오리지널 컨피던스."), M("When does Oricon announce its ranking?", "On Tuesday", ["On Sunday", "On Friday", "On Monday"], "화요일."), M("What do Japanese teen girls imitate?", "The costumes and hairstyles of Korean girl groups", ["Korean food", "Korean schools", "Korean dances only"], "복장과 헤어스타일."), M("What do Japanese teen fans see Korean girl groups as?", "Trained musicians and skilled artists", ["Only commercial products", "Only models", "Only actors"], "실력파 아티스트."), M("What does the writer hope for?", "Growth into world girls", ["An end to the craze", "A return to Korea", "A break"], "월드걸."),
           F("한국 걸그룹의 인기가 일본에서 ___를 찌른다. (sky)", "하늘", ["바다", "땅"], "하늘을 찌르다."), F("매장에는 엄청난 ___가 몰렸다. (crowd)", "인파", ["제작진", "줄임말"], "인파."), F("오리콘은 오리지널 컨피던스의 ___이다. (abbreviation)", "줄임말", ["제작진", "인파"], "줄임말."), F("한국 걸그룹이 일본을 ___삼아 성장하길 바란다. (stepping stone)", "발판", ["걸음", "문턱"], "발판 삼다."), F("그것은 아시아 여성그룹의 ___라고 평가했다. (splendid achievement)", "쾌거", ["희한", "궁핍"], "쾌거."),
           read_q("한국 걸그룹 인기가 일본에서 하늘을 찌릅니다"), read_q("카라의 게릴라 콘서트가 삼 분 만에 중단되었습니다"), read_q("십 대 여성들이 코스프레를 합니다"), read_q("월드걸로 성장하길 바랍니다"), read_q("어린 나이에 연예계에 진출하는 것에 대해 토론해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("게릴라 콘서트", "a surprise concert with very short notice (usually planned for popular performers); “guerrilla concert”", "비가 오는 날 게릴라 콘서트를 했는데도 사람이 아주 많이 모였어요."),
        ("고되다", "to be strenuous; to be hard", "신병 훈련은 무척 고되고 항상 배가 고팠다.", "힘들다, 힘겹다"),
        ("단련(시키다/되다)", "(鍛鍊) (vigorous) training (to train/to be trained)", "저는 체력 단련을 위해 매일 아침 조깅을 합니다.", "훈련"),
        ("발판 삼다", "to use something as a stepping stone", "군인이 된 것을 발판 삼아서 앞으로 여러 가지 경력을 쌓을 계획입니다."),
        ("부여(하다/되다)", "(附與) giving; granting (to grant/to be granted)", "진급을 하면 더 많은 의무를 부여받게 됩니다."),
        ("살을 찌우다", "to make fat; to make bigger", "아이들 살을 찌우기 위해 매일 맛있는 음식을 준비합니다."),
        ("양대 산맥", "(兩大 山脈) two prominent (representatives, figures, etc.); “two big mountain ranges”", "브라질과 아르헨티나는 남미 축구의 양대 산맥이다."),
        ("어리둥절(하다)", "bewilderment (to be bewildered)", "처음 공항에 도착했을 때에는 어디가 어딘지 몰라서 어리둥절했었다."),
        ("인파", "(人波) a huge crowd; “human waves”", "크리스마스 이브에는 거리가 인파로 넘쳐납니다."),
        ("제작진", "(製作陣) a production team (of TV or radio programs, etc.)", "그 영화를 만든 제작진이 다시 모여 비슷한 영화를 만들기로 했답니다."),
        ("줄임말", "an acronym; an abridged word", "외고는 외국어고등학교의 줄임말입니다."),
        ("찌르다", "to poke; to pierce", "바느질을 하다가 잘못해서 손가락을 찔렀어요."),
        ("쾌거", "(快擧) a splendid achievement", "이번 연구 결과는 우리 의학계의 쾌거입니다."),
        ("판을 키우다", "(板) to expand the “territory”; “to enlarge the plate”", "김 후보까지 선거에 합류하면서 판을 키웠습니다."),
        ("흥행", "(興行) success related to box office activity", "이 영화는 흥행에 성공했습니다."),
    ]),
    ("학습활동 2", [
        ("궁핍하다", "(窮乏) to be destitute", "한국 전쟁 이후에 국민들은 대부분 궁핍하게 살았습니다.", "가난하다"),
        ("베끼다", "to copy; to plagiarize", "다른 사람의 글을 베끼는 것은 범죄 행위입니다.", "표절하다"),
        ("왕성하다", "(旺盛) to be prosperous; to be thriving", "그 작가는 아직도 왕성한 작품 활동을 하고 있다."),
        ("정황", "(情況) situation; circumstances", "여러 가지 정황으로 볼 때 자살일 가능성이 높습니다.", "상황"),
        ("출간(하다/되다)", "(出刊) publication (to publish/to be published)", "이번 가을에 책 한 권을 출간하려고 합니다.", "출판"),
        ("회고록", "(回顧錄) a memoir; a reminiscence", "그 의사는 자신이 겪은 일을 회고록으로 출간할 계획이라고 합니다."),
    ]),
    ("학습활동 3", [
        ("결백(하다)", "(潔白) innocence (to be innocent)", "피의자는 결백을 주장했지만 받아들여지지 않았습니다."),
        ("묵살(하다/되다)", "(默殺) ignoring; disregarding (to ignore; to disregard/to be ignored; to be disregarded)", "좋은 의견이었지만 반대가 많아 묵살되었다."),
        ("방침", "(方針) a policy; a course (of action)", "저는 이 회사의 경영방침이 아주 마음에 들어요."),
        ("속다", "to be deceived; to be fooled; to be cheated", "저는 상인의 말에 속아서 물건을 샀어요."),
        ("수록(하다/되다)", "(收錄) listing; containing; including (to list; to contain; to include/to be listed; to be contained; to be included)", "이 단어를 사전에 새로 수록하기로 했답니다."),
        ("시인하다", "(是認) to admit; to acknowledge", "그 사람은 잘못을 시인했습니다.", "인정하다"),
        ("옹호하다", "(擁護) to advocate; to protect; to defend; to support", "김수영 씨는 여권을 옹호하기 위해 노력하고 있습니다."),
        ("위조(하다/되다)", "(僞造) forging (to fake; to counterfeit/to be forged)", "여권을 위조해 밀입국한 외국인이 검거되었습니다."),
        ("유출(하다/되다)", "(流出) leak (of information/data) (to spill; to leak/to be spilled; to be leaked)", "선박사고로 기름이 유출되었습니다."),
        ("의도적", "(意圖的) intentional; deliberate", "그 선수는 의도적으로 반칙을 했어요.", "계획적"),
        ("폐업(하다)", "(廢業) closing down one’s business; retiring from practice/business (to go out of business; to retire from practice/business)", "경영난으로 폐업하는 업체가 늘고 있습니다.", "개업(하다)"),
        ("표절(하다)", "(剽竊) plagiarism (to plagiarize)", "이효리의 새 노래가 표절의혹을 받고 있습니다.", "베끼다"),
    ]),
]
L7 = lesson(
    "U16 L3 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 게릴라 콘서트 · 고되다 · 단련 · 발판 삼다 · 부여 · 양대 산맥 · 어리둥절 · 인파 · 제작진 · 줄임말 · 쾌거 · 흥행 · 궁핍하다 · 베끼다 · 정황 · 출간 · 회고록 · 결백 · 묵살 · 방침 · 속다 · 수록 · 시인하다 · 옹호하다 · 위조 · 유출 · 의도적 · 폐업 · 표절",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example of 표절하다 names a singer’s new song; it is kept as printed. The book’s two-line examples are joined into one example.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=22, nread=18)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 3: Cultural Events (문화 행사)", [L1, L2, L3, L4, L5, L6, L7])

"""Unit 19: KBC Semester 1, Unit 3, Chapter 12 - Shopping in Koreatown (코리아타운에서 쇼핑하기).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 3, Student's Edition (2022).
Audio, video clips, pictures, maps, SMART Board activities, games, role-plays, partner and class activities are
left out. The book gives no English for its dialogs and leaves the answers to its exercises blank: every translation
of a dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


def _strip(lines):
    return [(l[1], l[2]) for l in lines]


_DG = "공일이삼사오육칠팔구"


def _g4(n):
    out = ""
    for val, unit in ((1000, "천"), (100, "백"), (10, "십")):
        d, n = divmod(n, val)
        if d:
            out += ("" if d == 1 else _DG[d]) + unit
    return out + (_DG[n] if n else "")


def _kn(n):
    """Sino-Korean number with four-digit groups: 70000 -> 칠만, 1926508 -> 백구십이만 육천오백팔"""
    if n == 0:
        return "영"
    parts = []
    for name, val in (("조", 10 ** 12), ("억", 10 ** 8), ("만", 10 ** 4)):
        g, n = divmod(n, val)
        if g:
            parts.append(("" if (g == 1 and name == "만") else _g4(g)) + name)
    if n:
        parts.append(_g4(n))
    return " ".join(parts)


def _usd(d=0, c=0, unit="달러"):
    """$1.20 -> 일 달러 이십 센트; $250 -> 이백오십 달러"""
    parts = []
    if d:
        parts.append(f"{_kn(d)} {unit}")
    if c:
        parts.append(f"{_kn(c)} 센트")
    return " ".join(parts)


def _won(n):
    return f"{_kn(n)} 원"


def _opts(right, pool, k=3):
    out = []
    for x in pool:
        if x != right and x not in out:
            out.append(x)
    return out[:k]


# ================================================================== Vocabulary builder: loan words for clothes
_LOAN1 = [("belt", "벨트"), ("handbag", "핸드백"), ("blouse", "블라우스"), ("sweater", "스웨터"), ("skirt", "스커트"), ("jacket", "재킷"), ("scarf", "스카프"), ("coat", "코트")]
L1 = lesson(
    "Ch 12 · Vocabulary builder: English loan words for clothes",
    "벨트 · 핸드백 · 블라우스 · 스웨터 · 스커트 · 재킷 · 스카프 · 코트",
    requires=[],
    cards=[
        card("Activity 1 (Writing): English words that Koreans use as loan words",
             "The book lists eight English words and asks you to write them in Korean; the first, belt → 벨트, is done for you. The other seven answers are the Korean spellings of the same loan words in the chapter’s Core Vocabulary (the key is mine).",
             tables=[table(["English word", "Korean"], [[a, b] for a, b in _LOAN1], say=[1])]),
        card("Notes on the spelling",
             "Koreans write English words in Hangul as they hear them: 재킷 (jacket), 스웨터 (sweater) and 스커트 (skirt) insert the vowel ㅡ between consonant clusters, and 핸드백 is “hand bag”. The book’s Topic B also lists 치마, a native Korean word for a skirt, next to the loan word 스커트."),
        card("Activities left out",
             "The PowerPoint presentation of new vocabulary, Activity 2 (SMART Board) and Activity 3 (Cash Cab, a pair game with two PowerPoint sets and a score board) are SMART Board, game or partner activities."),
    ],
    exercises=uniq(
        [M(f"How do you write “{a}” in Korean?", b, _opts(b, [x[1] for x in _LOAN1]), f"{a} → {b}.") for a, b in _LOAN1]
        + [M(f"What does {b} mean?", a, _opts(a, [x[0] for x in _LOAN1]), f"{b} = {a}.") for a, b in _LOAN1]
        + [F("저는 겨울에 ___를 입어요. (coat)", "코트", ["벨트", "스카프"], "코트 = coat."), F("목에 ___를 매요. (scarf)", "스카프", ["코트", "재킷"], "스카프 = scarf."), F("여자 친구의 ___ 안에 지갑이 있어요. (handbag)", "핸드백", ["벨트", "블라우스"], "핸드백 = handbag."),
           read_q("벨트"), read_q("핸드백"), read_q("블라우스"), read_q("스웨터"), read_q("스커트"), read_q("재킷"), read_q("스카프"), read_q("코트")]
    ),
)

# ================================================================== Topic A: gift shop and post office
_A_TEXT = [
    ("어제 부모님 선물을 사러 선물 가게에 갔습니다.", "Yesterday I went to a gift shop to buy presents for my parents."), ("아버지 선물로 지갑을 샀고 어머니 선물로 귀걸이를 샀습니다.", "I bought a wallet as a present for my father and earrings as a present for my mother."),
    (f"원래 지갑은 {_usd(120, unit='불')}이었고 귀걸이는 {_usd(60, unit='불')}이었습니다.", "Originally the wallet was 120 dollars and the earrings were 60 dollars."), (f"하지만, 가게 주인이 {_usd(20, unit='불')}을 깎아 주었습니다.", "But the shop owner took 20 dollars off for me."),
    ("또 예쁘게 포장해 주었습니다.", "He also wrapped them prettily."), ("가게 주인이 아주 친절했습니다.", "The shop owner was very kind."), ("그 다음에 부모님께 선물과 편지를 보내러 우체국에 갔습니다.", "Then I went to the post office to send the presents and a letter to my parents."),
    ("우체국에 사람들이 많아서 오래 기다려야 했습니다.", "There were many people at the post office, so I had to wait a long time."), ("소포를 부치고 우표 열 장과 엽서 두 장을 샀습니다.", "I mailed the parcel and bought ten stamps and two postcards."), (f"모두 {_usd(19, unit='불')}이었습니다.", "It was 19 dollars in all."),
]
_A_PAIRS = [("게", "-ly; “adverb maker”"), ("귀걸이", "an earring; “ear hanger”"), ("깎다", "to cut or shave off (price); to discount"), ("목걸이", "a necklace; “neck hanger”"), ("반지", "a (finger) ring"), ("벨트", "a belt"), ("부치다", "to mail"), ("불", "a counter for dollars"), ("센트", "a cent"),
            ("소포", "a parcel; a package"), ("엽서", "a postcard"), ("우표", "a postage stamp"), ("원래", "originally"), ("장", "a counter for sheets (of paper, cloth, postcards, etc.)"), ("점원", "a store clerk"), ("주인", "an owner"), ("지갑", "a wallet; a purse"),
            ("친절하다", "to be kind; to be friendly"), ("팔찌", "a bracelet"), ("편지", "a letter"), ("포장", "wrapping; packing"), ("포장하다", "to wrap"), ("핸드백", "a handbag")]
_A_PRON = [("원래", "월래", "originally"), ("관리", "괄리", "management"), ("신라", "실라", "Shilla"), ("만리장성", "말리장성", "the Great Wall"), ("난로", "날로", "a stove")]
_A_U = [("우체국", "a post office"), ("우표", "post stamp; “post ticket”"), ("우편물", "mail; postal matter"), ("우편번호", "the postal code; zip code; “postal number”")]
L2 = lesson(
    "Ch 12 · Topic A: I went to the post office to send a parcel",
    "소포를 부치러 우체국에 갔습니다 · 선물 가게 · 귀걸이 · 지갑 · 우표 · 우 (郵)",
    requires=[],
    cards=[
        card("Journal: a gift shop and a post office in L.A.",
             "The following text is SPC Jones’ journal entry about her shopping at a gift shop and sending parcels at a post office in L.A. The Korean is the book’s, with the prices and counted numbers spelled out in Hangul (120불 → 백이십 불, 60불, 20불, 10장 → 열 장, 2장 → 두 장, 19불 → 십구 불; the English is mine).",
             examples=passage(_A_TEXT)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary). The book lists -게 (the adverb maker, explained in its own lesson), ~불 and ~장 (counters), and 포장(하다) as a group; 벨트 and 핸드백 are loan words. 친절하다 is the verb of 친절 “kindness”.",
             tables=[ktable([(k, e) for k, e in _A_PAIRS if k != "게"])]),
        card("Counters: 불 and 장",
             "불 counts dollars (the book also writes ~달러; in speech both are used) and 장 counts sheets of paper, cloth, postcards, stamps, etc. Both come after a number: Sino-Korean numbers with 불 (십구 불) and native numbers with 장 (열 장, 두 장). In the journal: 우표 열 장과 엽서 두 장 (ten stamps and two postcards).",
             examples=[D("우표 열 장과 엽서 두 장을 샀습니다.", "I bought ten stamps and two postcards."), D("엽서 열 장 주세요.", "Please give me ten postcards. (the Core Vocabulary’s sentence)"), D("이 옷은 원래 칠십 달러였어요. 그런데 세일해서 오십 불에 샀어요.", "This outfit was originally 70 dollars. But it was on sale and I bought it for 50 dollars. (the Core Vocabulary’s sentence)")]),
        card("Pronunciation guide: 원래 /월래/",
             "Have you noticed that 원 in 원래 sounds like 월? This is due to the influence of the consonant ㄹ in the syllable that follows. When ㄴ is followed by ㄹ, oftentimes ㄴ changes into ㄹ. This is an example of anticipatory assimilation, in which a sound becomes more like a following sound. The book’s practice words are in the table.",
             tables=[ptable(_A_PRON)]),
        card("Cultural note: the Korean postal system",
             "The Korean postal system is different from that in the U.S. with regard to outgoing mail. The U.S. postal system usually picks up outgoing mail from home addresses, but the postal system in Korea does not. Therefore, when Koreans have outgoing mail they go to the post office or post their letters in a red mailbox on the street, which is called 우체통."),
        card("Sino-Korean in use: 우 (郵)",
             "This Sino-Korean syllable 우 means post or mail, as in 우체국 (a post office), 우표 (post stamp; “post ticket”), 우편물 (mail; postal matter) and 우편번호 (the postal code; zip code; “postal number”).",
             tables=[ktable(_A_U + [("우체통", "a mailbox (the red street mailbox of the cultural note)")])]),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity and Follow-Up Activity 2 (listening to four conversations between clerks and customers at a gift shop and at a post office, to identify what the customers purchase and the final price) are SMART Board or audio activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS if k not in ("게", "포장하다", "불", "장")])
        + _tr(_strip([("", a, b) for a, b in _A_TEXT])[:9]) + _tr(_A_U) + _tr(_A_PRON and [(a, c) for a, b, c in _A_PRON])
        + [M("What does 불 count?", "dollars", ["sheets", "people", "days"], "백이십 불 = 120 dollars."), M("What does 장 count?", "sheets (paper, cloth, postcards, stamps)", ["dollars", "people", "days"], "엽서 두 장."),
           M("What does 우 (郵) mean?", "post; mail", ["room", "people", "expense"], "우체국, 우표, 우편물."), M("What is a 우체통?", "a mailbox", ["a post office", "a stamp", "a letter"], "The red mailbox on the street."), M("Why does 원래 sound like 월래?", "ㄴ becomes ㄹ before ㄹ", ["ㄹ becomes ㄴ", "ㅇ is silent", "ㄱ becomes ㅋ"], "Anticipatory assimilation."),
           M("Where do Koreans usually post outgoing mail?", "At a post office or in a red street mailbox", ["At home", "At the bank", "At a gift shop"], "The Korean postal system does not pick up mail from homes."),
           M("What did SPC Jones buy for her father?", "A wallet", ["Earrings", "A belt", "A handbag"], "아버지 선물로 지갑을 샀고."), M("What did SPC Jones buy for her mother?", "Earrings", ["A wallet", "A necklace", "A bracelet"], "어머니 선물로 귀걸이를."),
           M("How much did the shop owner take off?", "20 dollars", ["10 dollars", "60 dollars", "120 dollars"], "이십 불을 깎아 주었습니다."), M("How much did the stamps and postcards cost?", "19 dollars in all", ["120 dollars", "60 dollars", "2 dollars"], "모두 십구 불."),
           F("가게 주인이 이십 불을 ___ 주었습니다. (took off)", "깎아", ["부쳐", "골라"], "깎다 = to discount."), F("소포를 ___ 우체국에 갔습니다. (to mail)", "부치러", ["깎으러", "포장하러"], "부치다 = to mail."), F("우표 열 ___과 엽서 두 장을 샀습니다. (counter)", "장", ["불", "개"], "장 = sheets."),
           F("지갑은 ___ 백이십 불이었습니다. (originally)", "원래", ["정말", "아주"], "원래 = originally."), read_q("우체국"), read_q("원래"), read_q("귀걸이"), read_q("소포를 부치고"), read_q("우표")]
    ),
)

# ================================================================== Activities A: an ad and prices
_ADV = [
    ("로즈 백화점 인기 브랜드 패션 잡화 특가", "Rose Department Store: special prices on popular-brand fashion accessories"), ("새해 맞이 파워 세일!", "Power sale to welcome the New Year!"), ("핸드백, 지갑, 벨트", "Handbags, wallets, belts"),
    ("액세서리류 (목걸이, 귀걸이, 반지, 팔찌)", "Accessories (necklaces, earrings, rings, bracelets)"), (f"{month_ko(12)} {day_ko(28)}부터 {month_ko(1)} {day_ko(6)}까지", "From December 28 to January 6"), (f"{_usd(100)} 이상 사시는 손님께는 작은 지갑을 드립니다.", "To customers who buy 100 dollars or more, we give a small wallet."),
    (f"로스앤젤레스 웨스턴 애비뉴 {_kn(389)} 번지", "389 Western Avenue, Los Angeles"),
]
_PRICES = [(100, 0), (0, 29), (3, 0), (250, 0), (45, 0), (650, 0), (2000, 0), (60, 0), (0, 47), (6, 95)]
_PR_STR = lambda d, c: ("$" + f"{d}" + (f".{c:02d}" if c else "")) if d else f"${c/100:.2f}"
_DLG_A2 = [("손님", "엽서 있어요?", "Do you have postcards?"), ("점원", "그럼요.", "Of course."), ("손님", "엽서 한 장에 얼마예요?", "How much is one postcard?"), ("점원", "일 달러 이십 센트입니다.", "It is one dollar twenty cents.")]
L3 = lesson(
    "Ch 12 · Activities A: a sale ad and reading prices",
    "로즈 백화점 새해 맞이 파워 세일 · 엽서 한 장에 얼마예요? · 달러와 센트",
    requires=[],
    cards=[
        card("Follow-Up Activity 1 (Reading): the department store ad",
             "The book shows an ad and asks you to fill in a table in English (sale period, items on sale, promotion). The ad is the book’s, with the dates, prices and the street number spelled out (the telephone number is left out; the English is mine). The book notes: ~이상 means “~ and above”; for example, 30달러 이상 means $30 and above.",
             examples=passage(_ADV)),
        card("The ad: the table filled in",
             "My key to the book’s table.",
             tables=[table(["Sale period", "Items on sale", "Promotion"], [["December 28 to January 6", "Handbags, wallets and belts; accessories (necklaces, earrings, rings and bracelets)", "A small wallet is given to customers who buy $100 or more"]])]),
        card("Activity 2 (Speaking): asking the price of an item",
             "The book gives a model for a short question-and-answer dialog between a customer and a store clerk and ten pictures with prices for practice (the pictures are left out). The model is below (the book writes 1달러 20센트; the English is mine). To read a price, say the dollars with 달러 (or 불) and the cents with 센트.",
             examples=dlg(_DLG_A2)),
        card("Reading the ten prices of the book’s pictures",
             "The prices printed under the book’s pictures (the items are not shown). The readings are mine, worked out with the number rule of the previous chapter (a 1 before 백 and 천 is not read).",
             tables=[table(["Price", "In Korean", "With 불"], [[_PR_STR(d, c), _usd(d, c), _usd(d, c, "불")] for d, c in _PRICES], say=[1, 2])]),
        card("Activities left out",
             "Activity 1 (SMART Board), Activity 3 (listening to three short conversations, deciding whether each takes place at a gift shop or a post office and filling in the items and the amount of money paid) and Activity 4 (a role-play at a gift shop and a post office with situation cards: price, items, discount, credit card, wrapping, region, length of time, total price) are SMART Board, audio or partner activities."),
    ],
    exercises=uniq(
        _tr(_strip([("", a, b) for a, b in _ADV[:6]])) + _tr(_strip(_DLG_A2)[:0] + [(a, b) for a, b in _strip(_DLG_A2)])
        + [M(f"How do you read {_PR_STR(d, c)}?", _usd(d, c), _opts(_usd(d, c), [_usd(x, y) for x, y in _PRICES]), f"{_PR_STR(d, c)} → {_usd(d, c)}.") for d, c in _PRICES]
        + [M("When does the sale run?", "From December 28 to January 6", ["From January 6 to December 28", "All of December", "Only on weekends"], "십이월 이십팔일부터 일월 육일까지."), M("What does a customer who spends $100 or more get?", "A small wallet", ["A belt", "A handbag", "A free postcard"], "작은 지갑을 드립니다."),
           M("What does ~이상 mean?", "and above", ["and below", "about", "only"], "백 달러 이상 = $100 and above."), M("What do you say for 'of course' when asked 엽서 있어요?", "그럼요", ["아니요", "글쎄요", "괜찮아요"], "그럼요 = of course."),
           F("엽서 한 장에 ___예요? (how much)", "얼마", ["언제", "누구"], "얼마예요 = how much?"), F("백 달러 ___ 사시는 손님께는 작은 지갑을 드립니다. (or more)", "이상", ["이하", "정도"], "이상 = and above."), F("일 달러 이십 ___입니다. (cents)", "센트", ["불", "장"], "센트 = cent."),
           read_q("백 달러 이상"), read_q("육 달러 구십오 센트"), read_q("이천 달러"), read_q("일 달러 이십 센트입니다")]
    ),
)

# ================================================================== Topic B: a clothing store
_B_DLG1 = [
    ("가게 직원", "어서 오세요. 뭐 찾으세요?", "Welcome. What are you looking for?"), ("김 이병", "청바지 좀 보고 싶어요.", "I’d like to see some jeans."), ("가게 직원", "아, 네. 이 청바지는 어떠세요?", "Oh, yes. How about these jeans?"),
    ("김 이병", "네, 좋아요. 입어 봐도 돼요?", "Yes, they’re nice. May I try them on?"), ("가게 직원", "그럼요.", "Of course."),
]
_B_DLG2 = [
    ("김 이병", "사이즈도 잘 맞고 바지 색도 마음에 들어요. 참, 장갑도 좀 보여주세요.", "The size fits well and I like the color of the pants. Oh, please show me some gloves too."), ("가게 직원", "네. 이 장갑은 어떠세요? 요즘 이 장갑이 인기 있어요. 한번 껴 보세요.", "Yes. How about these gloves? These gloves are popular these days. Try them on."),
    ("김 이병", "장갑이 따뜻하고 좋아요. 마음에 들어요.", "The gloves are warm and nice. I like them."), ("가게 직원", "어떤 색으로 하시겠어요? 한번 골라 보세요.", "Which color will you have? Choose one."), ("김 이병", "이 회색 장갑 하나 주세요.", "Please give me one pair of these gray gloves."),
]
_B_PAIRS = [("고르다", "to select; to choose"), ("구두", "formal shoes"), ("그럼요", "Of course (in response to a request or question)"), ("끼다", "to put on/wear (rings, bracelets, gloves, etc.); “to insert”"), ("넥타이", "a necktie"), ("맞다", "to fit; to suit; to be correct"),
            ("매다", "to put on/wear (items worn by tying); “to tie”"), ("모자", "a hat; a cap"), ("뭐", "what; abbreviation of 무엇"), ("바지", "pants; trousers"), ("보여주다", "to show; to display"), ("블라우스", "a blouse"), ("사이즈", "size"), ("선글라스", "sunglasses"),
            ("스웨터", "a sweater"), ("스카프", "a scarf"), ("스커트", "a skirt"), ("스타킹", "stockings"), ("시계", "a clock; a watch"), ("신다", "to put on/wear (footwear)"), ("신발", "footwear; shoes"), ("쓰다", "to put on/wear (items worn to cover the head or face)"),
            ("안경", "eyeglasses"), ("양말", "socks"), ("양복", "a suit (western style for men); “western clothes”"), ("와이셔츠", "a dress shirt; “Y-shirt”"), ("운동화", "athletic shoes; sneakers; “exercise shoe”"), ("원피스", "a one-piece dress/suit"), ("인기", "popularity"),
            ("잠바", "a windbreaker"), ("장갑", "gloves"), ("재킷", "a jacket"), ("차다", "to put on/wear (items worn by fastening them on); “to fasten”"), ("찾다", "to look for; to find"), ("청바지", "blue jeans; “blue pants”"), ("치마", "a skirt"), ("코트", "a coat"),
            ("투피스", "a two-piece dress/suit"), ("티셔츠", "a T-shirt"), ("회색", "gray (color)")]
_WEAR = [("입다", "basic clothing items", "바지, 치마, 스커트, 블라우스, 스웨터, 티셔츠, 와이셔츠, 잠바, 재킷, 코트, 원피스, 투피스, 양복"), ("신다", "footwear", "신발, 구두, 운동화, 양말, 스타킹"), ("쓰다", "items worn to cover the head or face", "모자, 안경, 선글라스, 마스크"),
         ("매다", "“to tie”; items worn by tying", "넥타이, 벨트, 스카프"), ("끼다", "“to insert”; items that are snug-fitting", "장갑, 반지, 팔찌, 안경"), ("차다", "“to fasten”; items worn by fastening them on", "시계, 총, 수통")]
_WEAR_EN = [("마스크", "a mask"), ("총", "a gun"), ("수통", "a canteen")]
_JOURNAL = [
    (f"{month_ko(12)} {day_ko(22)}", "December 22"), ("어제 크리스마스 선물을 사러 한국 백화점에 갔습니다.", "Yesterday I went to a Korean department store to buy Christmas presents."), ("백화점에는 여러 가게가 많았습니다.", "There were many different shops in the department store."),
    ("먼저, 어머니 선물을 사러 옷 가게에 갔습니다.", "First, I went to a clothing store to buy a present for my mother."), ("옷 가게 점원이 요즘 유행하는 블라우스와 스웨터를 보여 주었습니다.", "The clothing store clerk showed me a blouse and a sweater that are in fashion these days."),
    ("블라우스는 마음에 들었지만 스웨터는 마음에 들지 않았습니다.", "I liked the blouse, but I did not like the sweater."), ("그래서 블라우스만 샀습니다.", "So I bought only the blouse."), ("그 다음, 신발 가게에 들렀습니다.", "Next, I stopped by a shoe store."),
    ("점원이 예쁜 구두를 보여 주었습니다.", "The clerk showed me pretty dress shoes."), ("하지만 저는 운동화를 샀습니다.", "But I bought sneakers."), ("조금 피곤했지만 쇼핑은 아주 재미있었습니다.", "I was a little tired, but the shopping was a lot of fun."),
]
_EXPR = [("마음에 들어요.", "I like it."), ("마음에 안 들어요.", "I don’t like it."), ("잘 어울리시네요.", "It suits you well."), ("사이즈가 잘 맞아요.", "The size fits well."), ("입어 봐도 돼요?", "May I try it on?"), ("보여 주세요.", "Please show me."), ("얼마예요?", "How much is it?"), ("그걸로 주세요.", "Please give me that one.")]
L4 = lesson(
    "Ch 12 · Topic B: May I try them on?",
    "입어 봐도 돼요? · 입다 · 신다 · 쓰다 · 매다 · 끼다 · 차다 · 청바지 · 장갑",
    requires=[],
    cards=[
        card("Dialog: shopping for clothes in Koreatown",
             "PV2 Kim is shopping for clothes at a department store in L.A.’s Koreatown. The Korean is the book’s (the English is mine).",
             examples=dlg(_B_DLG1)),
        card("After trying on the clothes",
             "In the book, the second part of the dialog comes after PV2 Kim has tried on the clothes in the fitting room; the book’s stage direction “a moment later” comes before 장갑이 따뜻하고 좋아요.",
             examples=dlg(_B_DLG2)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary). The book lists 그럼(요) and the grammar items -아/어도 되다 and -(으)면 안 되다 among these words; those two have their own lessons. The five verbs 끼다, 매다, 신다, 쓰다 and 차다 are the “wear” verbs of the next card (their meanings here are those of the clothes list).",
             tables=[ktable(_B_PAIRS)]),
        card("Korean verbs that express “to wear” or “to put on”",
             "Korean uses a different verb depending on the kind of item. 입다 is for basic clothing items; 신다 for footwear; 쓰다 for items worn to cover the head or face; 매다 (“to tie”) for items worn by tying; 끼다 (“to insert”) for items that are snug-fitting; and 차다 (“to fasten”) for items worn by fastening them on. Some items take more than one verb (안경 can take 쓰다 or 끼다). In the book’s table 마스크 means “a mask”, 총 “a gun” and 수통 “a canteen”; the others are in the list above or in the Core Vocabulary.",
             tables=[table(["Verb", "Description", "Items"], [[a, b, c] for a, b, c in _WEAR], say=[0, 2]), ktable(_WEAR_EN)]),
        card("Expressions in a clothing store",
             "Expressions from the dialog and from the chapter’s activities (the book lists them without translation in Activity 2; the English is mine).",
             tables=[table(["Korean", "Meaning"], [[a, b] for a, b in _EXPR], say=[0])]),
        card("Follow-Up 1 (Reading): SPC Jones’ journal entry",
             "SPC Jones writes about the shopping she did at two stores in Koreatown in L.A. The book asks you to fill in a table in English (the store, the items suggested by the clerk and the item purchased). The entry is the book’s, with 12월 22일 spelled out (the English is mine).",
             examples=passage(_JOURNAL)),
        card("The journal: the table filled in",
             "My key to the book’s table.",
             tables=[table(["Store", "Item(s) suggested by the clerk", "Item purchased by SPC Jones"], [["A clothing store", "A blouse and a sweater (both in fashion these days)", "The blouse (she did not like the sweater)"], ["A shoe store", "Pretty dress shoes (구두)", "Sneakers (운동화)"]])]),
        card("Activities left out",
             "The SMART Board activities, the sentence-strip activity of the Presentation Activity (arranging strips in logical order) and Follow-Up 2 (listening to conversations about the people in PV2 Kim’s family wedding picture and what each is wearing) are SMART Board, audio or partner activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS if k not in ("끼다", "매다", "신다", "쓰다", "차다")])
        + _tr(_strip(_B_DLG1)) + _tr(_strip(_B_DLG2)) + _tr(_EXPR)
        + [M(f"Which verb goes with {item}?", verb, _opts(verb, ["입다", "신다", "쓰다", "매다", "끼다", "차다"]), f"{item} → {verb}.") for item, verb in [("바지", "입다"), ("블라우스", "입다"), ("양복", "입다"), ("구두", "신다"), ("양말", "신다"), ("운동화", "신다"), ("모자", "쓰다"), ("선글라스", "쓰다"), ("넥타이", "매다"), ("스카프", "매다"), ("벨트", "매다"), ("장갑", "끼다"), ("반지", "끼다"), ("시계", "차다")]]
        + [M("Which verb is used for items worn to cover the head or face?", "쓰다", ["입다", "신다", "매다"], "모자, 안경, 선글라스, 마스크."), M("Which verb literally means “to tie”?", "매다", ["끼다", "차다", "신다"], "넥타이를 매다."), M("Which verb literally means “to insert”?", "끼다", ["매다", "차다", "신다"], "장갑을 끼다."), M("Which verb literally means “to fasten”?", "차다", ["끼다", "매다", "쓰다"], "시계를 차다."),
           M("Which verb is used for footwear?", "신다", ["입다", "쓰다", "끼다"], "신발, 구두, 운동화, 양말."), M("What did SPC Jones buy at the clothing store?", "The blouse", ["The sweater", "A skirt", "A coat"], "블라우스만 샀습니다."), M("What did SPC Jones buy at the shoe store?", "Sneakers", ["Dress shoes", "Socks", "Boots"], "운동화를 샀습니다."),
           M("What does PV2 Kim ask the clerk before trying on the jeans?", "입어 봐도 돼요?", ["얼마예요?", "어디 있어요?", "뭐 찾으세요?"], "입어 봐도 돼요? = may I try them on?"), M("What color gloves does PV2 Kim buy?", "Gray", ["Black", "Blue", "White"], "회색 장갑."),
           F("바지를 ___. (wear)", "입어요", ["신어요", "써요"], "바지 → 입다."), F("운동화를 ___. (wear)", "신어요", ["입어요", "매요"], "운동화 → 신다."), F("모자를 ___. (wear)", "써요", ["입어요", "신어요"], "모자 → 쓰다."), F("넥타이를 ___. (wear)", "매요", ["껴요", "차요"], "넥타이 → 매다."), F("장갑을 ___. (wear)", "껴요", ["매요", "써요"], "장갑 → 끼다."), F("시계를 ___. (wear)", "차요", ["껴요", "신어요"], "시계 → 차다."),
           F("이 장갑이 요즘 ___ 있어요. (popularity)", "인기", ["사이즈", "주인"], "인기 있다 = to be popular."), F("사이즈가 잘 ___. (fits)", "맞아요", ["고르요", "찾아요"], "사이즈가 맞다 = to fit."),
           read_q("청바지"), read_q("운동화"), read_q("입어 봐도 돼요"), read_q("마음에 들어요"), read_q("회색")]
    ),
)

# ================================================================== Activities B: clothing flyers
_FLY1 = [("남성 의류 (30% 할인)", [("와이셔츠", 70000, "부터"), ("구두", 80000, ""), ("넥타이", 20000, ""), ("남성재킷", 100000, ""), ("티셔츠", 10000, ""), ("스웨터", 40000, ""), ("잠바", 60000, "")]),
         ("여성 의류 (40% 할인)", [("스커트", 30000, "부터"), ("블라우스", 50000, ""), ("원피스", 120000, ""), ("투피스", 150000, ""), ("스웨터", 80000, "")])]
_FLY2 = [("남성복 (50% 할인)", [("청바지", 20000, "부터"), ("티셔츠", 3000, ""), ("반바지", 7000, ""), ("잠바", 80000, ""), ("재킷", 100000, ""), ("와이셔츠", 70000, ""), ("스웨터", 20000, "")]),
         ("여성복 (30% 할인)", [("스커트", 20000, "부터"), ("블라우스", 30000, ""), ("스웨터", 40000, ""), ("원피스", 80000, ""), ("투피스", 100000, ""), ("모자", 100000, "")])]
_FLY_EXPR = [("마음에 들어.", "I like it. (informal)"), ("입어 보세요.", "Please try it on."), ("잘 어울리시네요.", "It suits you well."), ("얼마예요?", "How much is it?"), ("보여 주세요.", "Please show me."), ("입어 봐도 됩니까?", "May I try it on?"), ("마음에 안 들어요.", "I don’t like it."), ("그걸로 주세요.", "Please give me that one.")]
_FLY_ITEMS = [("원피스", "a one-piece dress"), ("구두", "formal shoes"), ("운동화", "sneakers"), ("스커트", "a skirt"), ("스카프", "a scarf"), ("투피스", "a two-piece dress"), ("코트", "a coat"), ("핸드백", "a handbag"), ("청바지", "blue jeans")]


def _fly_rows(fl):
    rows = []
    for head, items in fl:
        for name, price, suf in items:
            rows.append([head, name, f"{price:,} won" + (" and up" if suf else ""), f"{_won(price)}{suf}"])
    return rows


L5 = lesson(
    "Ch 12 · Activities B: clothing flyers and clothing-store expressions",
    "코리아나 백화점 · 고려 백화점 · 남성 의류 30% 할인 · 마음에 들어요 · 그걸로 주세요",
    requires=[],
    cards=[
        card("Activity 1 (Reading and speaking): shopping for civilian clothes in Korea",
             "You are stationed in Osan, Korea, and all of your moving boxes were transferred to the wrong place; it may take over two weeks for the boxes to be delivered. You brainstorm what civilian clothing you have to buy, then, with 300,000 Korean won (삼십만 원), you circle the items you decide to buy in the two flyers and tell a partner your reasons. The flyers are below as tables (the phone numbers are left out; the readings of the prices are mine; the book prints the discount rate beside each line and does not say whether the printed price is before or after the discount).",
             tables=[table(["Flyer: Koreana Department Store (코리아나 백화점)", "Item", "Price", "In Korean"], _fly_rows(_FLY1), say=[1, 3]),
                     table(["Flyer: Goryeo Department Store (고려 백화점)", "Item", "Price", "In Korean"], _fly_rows(_FLY2), say=[1, 3], note="The flyer also announces a 60% discount (육십 퍼센트 할인) on other items: 양말, 스타킹, 넥타이, 벨트, 스카프, 장갑, 모자 and so on. 반바지 (shorts) is not in the Core Vocabulary; its meaning here is mine.")]),
        card("Reading percentages and prices in a shop",
             "A discount is 할인; the rate is said with 퍼센트 (삼십 퍼센트 할인). Won are counted with Sino-Korean numbers in groups of four digits (만 = 10,000): 칠만 원 is 70,000 won. A 1 before 만 is not read (만 원 = 10,000 won).",
             examples=[D("남성 의류는 삼십 퍼센트 할인입니다.", "Men’s clothing is 30 percent off."), D("와이셔츠는 칠만 원부터입니다.", "The dress shirts start from 70,000 won."), D("원피스는 십이만 원입니다.", "The one-piece dress is 120,000 won."), D("티셔츠는 삼천 원입니다.", "The T-shirt is 3,000 won.")]),
        card("Activity 2 (Listening): items and expressions",
             "The book asks you to watch two Korean video clips and circle the items or expressions that are mentioned. The lists the book prints are below; the English is mine. The video clips are left out.",
             tables=[ktable(_FLY_ITEMS), table(["Expression", "Meaning"], [[a, b] for a, b in _FLY_EXPR], say=[0])]),
        card("Activity 3 (Speaking): role-play at a shoe store and a clothing store",
             "In the book, you pair up as a customer and a store clerk (the customer receives a situation card from the teacher) and role-play shopping at a shoe store and a clothing store. Be sure to mention: request or offer services at the clothing or shoe store; ask or tell the price of clothing or accessories; express your satisfaction or dissatisfaction regarding the size, color or style of an item; ask or give permission to try something on. The expressions above are for this role-play; the role-play itself is a partner activity and is not reproduced."),
        card("Activities left out",
             "Activity 2’s video clips and the table of Activity 2b (listening to three conversations in a shopping center and filling in the items mentioned, the reasons for liking and not liking the first choice, and the price) are video or audio activities."),
    ],
    exercises=uniq(
        [M(f"How do you say {p:,} won?", _won(p), _opts(_won(p), [_won(x[1]) for h, its in _FLY1 + _FLY2 for x in its]), f"{p:,} → {_won(p)}.") for p in (70000, 80000, 100000, 120000, 150000, 3000, 7000, 20000, 60000)]
        + [M(f"What does {a} mean?", b, _opts(b, [x[1] for x in _FLY_ITEMS]), f"{a} = {b}.") for a, b in _FLY_ITEMS] + _tr(_FLY_EXPR)
        + [M("How do you say 30 percent?", "삼십 퍼센트", ["십삼 퍼센트", "삼백 퍼센트", "서른 퍼센트"], "Sino-Korean 삼십."), M("What does 할인 mean?", "discount", ["sale price", "tax", "wrapping"], "30% 할인."), M("How do you say 300,000 won?", "삼십만 원", ["삼만 원", "삼백만 원", "삼천 원"], "30 × 10,000."),
           F("남성 의류는 삼십 퍼센트 ___입니다. (discount)", "할인", ["인기", "포장"], "할인 = discount."), F("와이셔츠는 칠만 원___입니다. (starting from)", "부터", ["까지", "에서"], "부터 = from."), F("이 코트가 ___에 들어요. (I like it)", "마음", ["사이즈", "인기"], "마음에 들다 = to like."),
           read_q("칠만 원"), read_q("십이만 원"), read_q("삼십 퍼센트"), read_q("잘 어울리시네요"), read_q("그걸로 주세요")]
    ),
)

# ================================================================== Grammar A: asking and giving permission
def _ao(v):
    """-아/어도 되다: 앉다 -> 앉아도 되다"""
    base = {"듣다": "들어"}.get(v) or _base_ao(v)
    return base + "도 되다"


def _nm_(v):
    """-(으)면 안 되다: 살다 -> 살면 안 되다, 앉다 -> 앉으면 안 되다"""
    f = {"듣다": "들으면"}.get(v) or if_(v)
    return f + " 안 되다"


_P_V = ["앉다", "보다", "입다", "읽다", "마시다", "일어서다", "가다", "먹다", "하다", "쓰다", "듣다", "주차하다", "찍다", "들어가다"]
_P_EX = [("교실에서 영어를 해도 돼요?", "Is it all right if I speak English in the classroom?"), ("교실에서 영어를 해도 좋아요?", "Is it all right if I speak English in the classroom? (with 좋다)"), ("교실에서 영어를 해도 괜찮아요?", "Is it all right if I speak English in the classroom? (with 괜찮다)")]
_P_DLG = [("A", "선생님, 수업시간에 먹어도 돼요?", "Teacher, is it all right to eat during class?"), ("B", "아니요, 안 됩니다. 하지만 음료수는 마셔도 괜찮아요.", "No, you may not. You may drink a beverage, though."), ("A", "여기에 주차해도 돼요?", "May I park the car here?"), ("B", "아니요, 안 됩니다.", "No, you may not.")]
_P_RULE = [("의자에 앉다", "의자에 앉아도 되다"), ("영화를 보다", "영화를 봐도 되다"), ("코트를 입다", "코트를 입어도 되다"), ("책을 읽다", "책을 읽어도 되다")]
_P_F1 = [("교실에서 커피를 마셔도 돼요?", "Is it all right to drink coffee in the classroom?"), ("수업시간에 일어서도 돼요?", "Is it all right to stand up during class?"), ("오늘 한 시간 일찍 집에 가도 돼요?", "Is it all right to go home an hour early today?"),
         ("교실에서 점심을 먹어도 돼요?", "Is it all right to eat lunch in the classroom?"), ("교실 컴퓨터로 게임을 해도 돼요?", "Is it all right to play games on the classroom computer?"), ("교실에서 휴대폰을 써도 돼요?", "Is it all right to use a cell phone in the classroom?")]
_P_OTHER = [("저… 전화 좀 써도 돼요?", "Um… may I use the phone? (the Core Vocabulary’s sentence)"), ("입어 봐도 돼요?", "May I try them on? (Topic B)"), ("한번 입어 봐도 돼요?", "May I try it on once? (the title of Topic B)"), ("입어 봐도 됩니까?", "May I try it on? (from Activity 2)")]
L6 = lesson(
    "Ch 12 · Grammar A: asking for and giving permission with -아/어도 되다",
    "입어 봐도 돼요? · 먹어도 돼요? · 앉아도 되다 · 봐도 되다 · 해도 괜찮아요",
    requires=[],
    cards=[
        card("-아/어도 되다: “may I …?”",
             "In English, we use phrases such as “May I …?”, “Is it all right if …?” or “Do you mind if …?” when asking for permission; the same phrases are used when permission is granted (“You may …” or “It’s all right if …”). In Korean, we use -아/어도 되다 when asking for or giving permission to do something. 되다 literally means “to become”; it can also mean to be O.K., to be fine, to be all right or to be possible. Therefore -아/어도 좋다 and -아/어도 괜찮다 can be substituted for -아/어도 되다.",
             examples=[D(a, b) for a, b in _P_EX]),
        card("How to form it",
             "verb stem + 아/어도 되다 (괜찮다/좋다). If the last syllable of the verb stem contains the vowels ㅏ or ㅗ, add 아도 되다; if it contains a vowel other than ㅏ or ㅗ, add 어도 되다. The usual contractions of the -아/어 form apply (보다 → 봐도, 마시다 → 마셔도, 하다 → 해도, 쓰다 → 써도).",
             tables=[table(["Condition", "Rule", "Example"], [["The last syllable of a verb stem contains ㅏ or ㅗ", "add 아도 되다", "의자에 앉다 → 의자에 앉아도 되다; 영화를 보다 → 영화를 봐도 되다"], ["The last syllable of a verb stem contains a vowel other than ㅏ or ㅗ", "add 어도 되다", "코트를 입다 → 코트를 입어도 되다; 책을 읽다 → 책을 읽어도 되다"]]),
                     table(["Verb", "-아/어도 되다"], [[v, _ao(v)] for v in _P_V], say=[0, 1], note="The table is mine (듣다 is the ㄷ irregular verb: 들어도).")]),
        card("A dialog: in the classroom",
             "The book’s examples of a student asking a teacher and a driver asking where to park (the English is mine).",
             examples=dlg(_P_DLG)),
        card("Examples from the chapter",
             "More questions with -아/어도 되다 from the Core Vocabulary and the chapter (the English is mine).",
             examples=[D(a, b) for a, b in _P_OTHER]),
        card("Follow-Up 1: ask for permission in the classroom",
             "The book gives six situations and asks you to conjugate the verb in parentheses with -아/어도 되다 to complete each question (마시다, 일어서다, 가다, 먹다, 하다, 쓰다). The completed questions below are my answers.",
             tables=[table(["Question", "Meaning"], [[a, b] for a, b in _P_F1], say=[0])]),
        card("Activities left out",
             "Follow-Up 2 (listening to a student asking a librarian about library rules and marking whether permission is granted or denied) is audio."),
    ],
    exercises=uniq(
        [M(f"What is the -아/어도 되다 form of {v}?", _ao(v), _opts(_ao(v), [stem(v) + "도 되다", _base_ao(v) + "서 되다", if_(v) + " 되다", stem(v) + "고 되다", _base_ao(v) + "도 안 되다"]), f"{v} → {_ao(v)}.") for v in _P_V]
        + _tr(_P_EX[:1] + _P_DLG[:0] + [(a, b) for a, b in _strip(_P_DLG)]) + _tr(_P_F1) + _tr(_P_OTHER[:3])
        + [M("What does -아/어도 되다 express?", "Asking for or giving permission", ["Denying permission", "A strong intention", "A reason"], "입어 봐도 돼요? = may I try it on?"), M("Which words can replace 되다 in -아/어도 되다?", "좋다 and 괜찮다", ["싫다 and 많다", "있다 and 없다", "하다 and 가다"], "-아/어도 좋다, -아/어도 괜찮다."),
           M("What does 되다 literally mean?", "to become", ["to wear", "to go", "to prohibit"], "되다 = to become; to be all right."), M("Which vowels in the last stem syllable take 아도?", "ㅏ and ㅗ", ["ㅓ and ㅜ", "ㅣ and ㅡ", "Any vowel"], "앉아도, 봐도."),
           F("교실에서 영어를 ___ 돼요? (speak)", "해도", ["하면", "하고"], "하다 → 해도."), F("의자에 ___ 돼요? (sit)", "앉아도", ["앉어도", "앉으면"], "앉다 → 앉아도."), F("코트를 ___ 돼요? (wear)", "입어도", ["입아도", "입으면"], "입다 → 입어도."), F("영화를 ___ 돼요? (watch)", "봐도", ["보어도", "보면"], "보다 → 봐도."),
           F("교실에서 커피를 ___ 돼요? (drink)", "마셔도", ["마시어도", "마시면"], "마시다 → 마셔도."), F("교실에서 휴대폰을 ___ 돼요? (use)", "써도", ["쓰어도", "쓰면"], "쓰다 → 써도."), F("오늘 일찍 집에 ___ 돼요? (go)", "가도", ["가아도", "가면"], "가다 → 가도."),
           read_q("앉아도 돼요"), read_q("마셔도 괜찮아요"), read_q("입어 봐도 돼요"), read_q("주차해도 돼요")]
    ),
)

# ================================================================== Grammar B: denying permission
_D_V = ["살다", "만나다", "앉다", "닫다", "먹다", "마시다", "가다", "하다", "듣다", "자다", "놀다", "입다", "주차하다", "읽다"]
_D_EX = [("교실에서 영어를 하면 안 됩니다.", "You should not speak English in the classroom."), ("이곳에 주차하면 안 돼요.", "You may not park your car here."), ("도서관에서 음식을 먹으면 안 됩니다.", "You must not eat in the library. (the Core Vocabulary’s sentence)")]
_D_DLG1 = [("A", "지금 영화보러 가도 괜찮아요?", "Is it all right to go to the movies now?"), ("B", "안 돼.", "No, you shouldn’t go to the movies now. (the book’s long form: 지금 영화 보러 가면 안 돼)")]
_D_DLG2 = [("A", "엄마, 나가서 놀아도 돼요?", "Mom, can I go out to play?"), ("B", "나가서 놀면 안 돼. 너 내일 시험이잖아.", "No, you may not go out to play. You have a test tomorrow, don’t you?")]
_D_F3 = [("음악을 듣다", "여기서 음악을 들어도 돼요?", "아니요, 여기서는 음악을 들으면 안 됩니다.", "the book’s model: not allowed"), ("술을 마시다", "술을 마셔도 돼요?", "술을 마시면 안 됩니다.", "mine"), ("집에 전화하다", "집에 전화해도 돼요?", "네, 집에 전화해도 돼요.", "mine"), ("일찍 자다", "일찍 자도 돼요?", "아니요, 일찍 자면 안 됩니다.", "mine")]
_D_F5 = [("저는 해군 기숙사에 살아요.", "I live in a Navy dormitory."), ("우리 기숙사에서는 사복을 입어도 돼요.", "In our dormitory, we may wear civilian clothes."), ("그렇지만 방에서는 술을 마시면 안 돼요.", "But in the rooms we must not drink alcohol.")]
L7 = lesson(
    "Ch 12 · Grammar B: denying permission with -(으)면 안 되다",
    "영어를 하면 안 됩니다 · 주차하면 안 돼요 · 앉으면 안 되다 · 놀면 안 돼",
    requires=[],
    cards=[
        card("-(으)면 안 되다: “you may not …”",
             "To express a refusal of permission or the prohibition of an action, Koreans use -(으)면 안 되다. The literal meaning of -(으)면 안 되다 is “(it) is not all right if …” or “(it) is not fine if …”. Thus, depending on the context, it can be translated as you may not, you should not, you must not or you are not allowed to.",
             examples=[D(a, b) for a, b in _D_EX]),
        card("How to form it",
             "verb stem + (으)면 안 되다. When the verb stem ends in a vowel or ㄹ, add 면 안 되다 (기숙사에 살다 → 기숙사에 살면 안 되다; 친구를 만나다 → 친구를 만나면 안 되다). When the verb stem ends in a consonant other than ㄹ, add 으면 안 되다 (여기에 앉다 → 여기에 앉으면 안 되다; 창문을 닫다 → 창문을 닫으면 안 되다). The ㄷ irregular verb 듣다 changes to 들으면 (음악을 들으면 안 되다); this is mine.",
             tables=[table(["Condition", "Rule", "Example"], [["The verb stem ends in a vowel or ㄹ", "add 면 안 되다", "기숙사에 살다 → 기숙사에 살면 안 되다; 친구를 만나다 → 친구를 만나면 안 되다"], ["The verb stem ends in a consonant other than ㄹ", "add 으면 안 되다", "여기에 앉다 → 여기에 앉으면 안 되다; 창문을 닫다 → 창문을 닫으면 안 되다"]]),
                     table(["Verb", "-(으)면 안 되다"], [[v, _nm_(v)] for v in _D_V], say=[0, 1], note="The table is mine.")]),
        card("Asking and refusing: two short dialogs",
             "The book’s examples: when the refusal repeats the whole clause, it is written 지금 영화 보러 가면 안 돼, and it can be shortened to 안 돼. The English is mine except where it repeats the book’s translations.",
             examples=dlg(_D_DLG1) + dlg(_D_DLG2)),
        card("Follow-Up 3: allowed and not allowed during a special weeklong military training",
             "The book gives a list of activities (음악을 듣다, 술을 마시다, 집에 전화하다, 일찍 자다) that are allowed or not allowed, asks you to add more and to take turns asking and answering with -아/어도 되다 or -(으)면 안 되다; only the first line is done for you (not allowed): A: 여기서 음악을 들어도 돼요? B: 아니요, 여기서는 음악을 들으면 안 됩니다. The other three lines below are sample questions and answers of mine (the book leaves the check marks open).",
             tables=[table(["Activity", "Question", "Answer", "Source"], [[a, b, c, d] for a, b, c, d in _D_F3], say=[0, 1, 2])]),
        card("Follow-Up 5: places and rules",
             "In the book you choose a place that you frequently go to, such as 기숙사, 식당, 체육관, 영화관 or 쇼핑 센터 (a dormitory, a dining hall, a gym, a movie theater or a shopping center), and list three activities that are allowed and three that are not, in English; then present them with -아/어도 되다 and -(으)면 안 되다. The model is below (the book glosses 사복 as “civilian clothes”; the English is mine).",
             examples=passage(_D_F5)),
        card("Activities left out",
             "Follow-Up 4 (listening to conversations in which students ask their teacher about the classroom policy and marking granted or denied) is audio; the list-making and presentation of Follow-Up 5 are partner activities."),
    ],
    exercises=uniq(
        [M(f"What is the -(으)면 안 되다 form of {v}?", _nm_(v), _opts(_nm_(v), [stem(v) + "면 안 되다" if _nm_(v) != stem(v) + "면 안 되다" else stem(v) + "으면 안 되다", _ao(v), stem(v) + "지 않다", stem(v) + "고 싶다"]), f"{v} → {_nm_(v)}.") for v in _D_V]
        + _tr(_D_EX) + _tr(_strip(_D_DLG2)) + _tr(_D_F5) + [M(f"A: {q} What is the answer in the book’s model?", c, [d2 for _, _, d2, _ in _D_F3[1:]][:3], "The book’s first line.") for _, q, c, _ in _D_F3[:1]]
        + [M("What does -(으)면 안 되다 express?", "Denying permission; prohibition", ["Asking permission", "A strong intention", "A reason"], "교실에서 영어를 하면 안 됩니다."), M("What is the literal meaning of -(으)면 안 되다?", "(it) is not all right if …", ["(it) is all right if …", "(it) will be …", "(it) was …"], "안 되다 = not all right."),
           M("How can -(으)면 안 되다 be translated?", "you may not; you must not; you are not allowed to", ["you may; you can", "you will; you shall", "you did; you were"], "Prohibition."), M("When is 으면 안 되다 used?", "After a stem ending in a consonant other than ㄹ", ["After a vowel", "After ㄹ", "After any stem"], "앉으면, 닫으면."),
           F("교실에서 영어를 ___ 안 됩니다. (speak)", "하면", ["해도", "하고"], "하다 + 면 안 되다."), F("여기에 ___ 안 돼요. (sit)", "앉으면", ["앉면", "앉아도"], "앉다 + 으면."), F("기숙사에 ___ 안 되다. (live)", "살면", ["살으면", "사면"], "ㄹ stems take 면."), F("창문을 ___ 안 돼요. (close)", "닫으면", ["닫면", "닫아도"], "닫다 + 으면."),
           F("여기서는 음악을 ___ 안 됩니다. (listen)", "들으면", ["듣으면", "들면"], "듣다 → 들으면."), F("나가서 놀면 ___. (no)", "안 돼", ["돼요", "괜찮아"], "안 돼 = no, you may not."),
           read_q("하면 안 됩니다"), read_q("앉으면 안 돼요"), read_q("들으면 안 됩니다"), read_q("놀면 안 돼")]
    ),
)


# ================================================================== Topic C: the Korean grocery store
_C_DLG1 = [
    ("김 이병", "저, 여기 고기 파는 데가 어디 있어요?", "Excuse me, where is the place that sells meat here?"), ("점원", "저기 생선 파는 곳 옆에 있어요.", "It’s over there, next to the place that sells fish."), ("김 이병", "그럼, 고추장이랑 설탕은 어디에 있어요?", "Then where are the red pepper paste and sugar?"),
    ("점원", "계산대 옆에 양념 파는 데가 있어요. 거기로 가 보세요. 더 필요한 것 있으세요?", "There is a place that sells seasonings next to the counter. Go over there. Is there anything else you need?"), ("김 이병", "네, 과일도 사야 해요. 요즘 무슨 과일이 맛있어요?", "Yes, I also have to buy fruit. What fruit is good these days?"),
    ("점원", "오늘 포도가 아주 싸고 싱싱해요.", "Today the grapes are very cheap and fresh."),
]
_C_DLG2 = [
    ("점원", "이쪽 계산대로 오세요. 계산해 드리겠습니다.", "Please come to this counter. I’ll ring you up."), ("김 이병", "네.", "Yes."), ("점원", "모두 백십칠 달러입니다.", "It is 117 dollars in all."), ("김 이병", "여기 백이십 달러 있습니다.", "Here is 120 dollars."),
    ("점원", "네, 백이십 불 받았습니다. 여기 거스름돈 삼 불 있습니다. 감사합니다.", "Yes, I received 120 dollars. Here is your change, 3 dollars. Thank you."),
]
_C_PAIRS = [("간장", "soy sauce"), ("거스름돈", "change; “changed money”"), ("계산", "calculation; computation; counting"), ("계산하다", "to calculate; to compute; to count"), ("계산대", "a counter; “counting board”"), ("고기", "meat"), ("고추장", "red pepper paste"), ("과일", "fruit"),
            ("닭", "a chicken"), ("데", "a place; a spot"), ("돼지", "a pig"), ("된장", "soy bean paste"), ("딸기", "a strawberry"), ("사과", "an apple"), ("생선", "fish (for eating)"), ("설탕", "sugar"), ("소", "a cow"), ("식초", "vinegar"), ("식품", "a grocery; “eating item”"),
            ("식품점", "a grocery store"), ("싱싱하다", "to be fresh (for food)"), ("양념", "seasoning; spices"), ("팔다", "to sell"), ("포도", "a grape"), ("후추", "black pepper")]
_C_KIND = [("고기", "meat", "소고기, 돼지고기, 닭고기", "beef, pork, chicken"), ("과일", "fruit", "사과, 포도, 딸기", "apples, grapes, strawberries"), ("양념", "seasoning", "간장, 된장, 고추장, 식초, 후추, 설탕", "soy sauce, soy bean paste, red pepper paste, vinegar, black pepper, sugar")]
_C_KIND2 = [("소고기", "beef"), ("돼지고기", "pork"), ("닭고기", "chicken")]
_DEP = [("먹을 데", "a place to eat"), ("먹을 것", "a thing to eat"), ("이것", "this thing"), ("저것", "that thing"), ("고기 파는 데", "a place that sells meat"), ("양념 파는 데", "a place that sells seasonings"), ("더 필요한 것", "something more that you need")]
_MEMO = [
    ("우리가 돼지 불고기를 만들 거예요.", "We are going to make pork bulgogi."), ("그래서 돼지고기가 십 파운드쯤 필요해요.", "So we need about ten pounds of pork."), ("고기는 교포 식품점이 싸고 좋아요.", "As for meat, the Gyopo grocery store is cheap and good."),
    ("거기에 가서 돼지고기를 사세요.", "Go there and buy the pork."), ("그리고 과일이랑 음료수도 사야 해요.", "And we also have to buy fruit and drinks."), ("과일은 한양 식품점에서 싸게 팔아요.", "As for fruit, the Hanyang grocery store sells it cheaply."),
    ("한양 식품점에 가서 딸기 한 박스하고 포도 두 박스를 사세요.", "Go to the Hanyang grocery store and buy one box of strawberries and two boxes of grapes."), ("그리고 거기서 한국 음료수도 좀 사세요.", "And buy some Korean drinks there too."), ("한 박스만 사세요.", "Buy only one box."),
]
L8 = lesson(
    "Ch 12 · Topic C: Where is the meat section?",
    "고기 파는 데가 어디 있어요? · 식품점 · 양념 · 거스름돈 · 데와 것",
    requires=[],
    cards=[
        card("Dialog: at a Korean grocery store",
             "PV2 Kim is shopping at a Korean grocery store in L.A.’s Koreatown, looking for items at the store. The Korean is the book’s, with 117달러, 120달러, 120불 and 3불 spelled out in Hangul (the English is mine).",
             examples=dlg(_C_DLG1)),
        card("At the counter",
             "In the book the second part takes place at the counter.",
             examples=dlg(_C_DLG2)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary). The book lists 계산(하다) and 식품(점) as groups; they are split here (식품 is “eating item”; 식품점 is the store). -데 is a dependent noun, explained in the card below.",
             tables=[ktable(_C_PAIRS)]),
        card("Types of grocery items (식품의 종류)",
             "The book’s categories of grocery items: meat (고기), fruit (과일) and seasoning (양념). The English glosses in parentheses are the book’s.",
             tables=[table(["Category", "Meaning", "Items", "In English"], [[a, b, c, d] for a, b, c, d in _C_KIND], say=[0, 2])]),
        card("Dependent nouns: 데 (a place) and 것 (a thing)",
             "The two nouns -데 (a place) and -것 (a thing) are called dependent nouns because they cannot stand on their own and must be accompanied by a modifier immediately preceding them. While both nouns can be modified by the attributive forms of verbs, as in 먹을 데 (a place to eat) and 먹을 것 (a thing to eat), -것 can also be modified by a demonstrative, as in 이것 (this thing) and 저것 (that thing). However, -데 cannot be modified by a demonstrative. The dialog uses both: 고기 파는 데 and 더 필요한 것.",
             tables=[ktable(_DEP)]),
        card("Follow-Up 1 (Reading): the party shopping memo",
             "Your class is having a party and you are one of the people in charge of shopping for grocery items. The book asks you to read the memo that SPC Kim, the class leader, gave you and fill in a table in English (the grocery store, the items to buy and the quantity). The memo is the book’s; 박스 means “a box”, as the book glosses (the English is mine).",
             examples=passage(_MEMO)),
        card("The memo: the table filled in",
             "My key to the book’s table.",
             tables=[table(["Name of the grocery store", "Item(s) to buy", "Quantity"], [["Gyopo grocery store (교포 식품점)", "Pork", "About 10 pounds"], ["Hanyang grocery store (한양 식품점)", "Strawberries", "1 box"], ["Hanyang grocery store (한양 식품점)", "Grapes", "2 boxes"], ["Hanyang grocery store (한양 식품점)", "Korean drinks", "1 box"]])]),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity and Follow-Up 2 (listening to three loudspeaker announcements in Korean grocery stores and filling in the item, its location and the price) are SMART Board or audio activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS if k not in ("계산", "식품")])
        + _tr(_strip(_C_DLG1)) + _tr(_strip(_C_DLG2)) + _tr(_DEP) + _tr(_C_KIND2) + _tr(_strip([("", a, b) for a, b in _MEMO])[:6])
        + [M("What is a dependent noun?", "A noun that must have a modifier right before it", ["A noun that cannot take particles", "A noun that is always plural", "A noun that comes after a verb ending"], "데 and 것 need modifiers."), M("Which dependent noun can be modified by a demonstrative?", "것", ["데", "곳", "분"], "이것, 저것; but not 이 데."),
           M("Which is the category of 간장, 된장 and 고추장?", "양념 (seasoning)", ["고기 (meat)", "과일 (fruit)", "생선 (fish)"], "양념 = seasoning."), M("Which is the category of 사과, 포도 and 딸기?", "과일 (fruit)", ["양념 (seasoning)", "고기 (meat)", "생선 (fish)"], "과일 = fruit."), M("Which is the category of 소고기, 돼지고기 and 닭고기?", "고기 (meat)", ["과일 (fruit)", "양념 (seasoning)", "채소 (vegetables)"], "고기 = meat."),
           M("What is the total the clerk asks for?", "117 dollars", ["120 dollars", "3 dollars", "17 dollars"], "모두 백십칠 달러."), M("How much change does PV2 Kim get?", "3 dollars", ["17 dollars", "120 dollars", "1 dollar"], "거스름돈 삼 불."), M("What does the clerk say is cheap and fresh today?", "Grapes", ["Apples", "Strawberries", "Fish"], "포도가 아주 싸고 싱싱해요."),
           M("Where is the seasoning section?", "Next to the counter", ["Next to the fish", "At the entrance", "Behind the fruit"], "계산대 옆에 양념 파는 데."), M("What will the class make for the party?", "Pork bulgogi", ["Kimchi stew", "Bibimbap", "Fried chicken"], "돼지 불고기."),
           F("고기 파는 ___가 어디 있어요? (a place)", "데", ["것", "분"], "파는 데 = a place that sells."), F("더 필요한 ___ 있으세요? (a thing)", "것", ["데", "곳"], "필요한 것 = a thing you need."), F("___ 드리겠습니다. (I’ll ring you up)", "계산해", ["고르어", "깎아"], "계산해 드리겠습니다."),
           F("오늘 포도가 아주 싸고 ___. (fresh)", "싱싱해요", ["친절해요", "깨끗해요"], "싱싱하다 = fresh."), F("여기 ___ 삼 불 있습니다. (change)", "거스름돈", ["양념", "설탕"], "거스름돈 = change."),
           read_q("식품점"), read_q("고추장"), read_q("거스름돈"), read_q("계산대"), read_q("싱싱해요")]
    ),
)

# ================================================================== Grammar C: the adverb maker -게
_G_V = ["맵다", "바쁘다", "예쁘다", "친절하다", "크다", "짧다", "싸다", "빠르다", "맛있다", "많다", "작다", "춥다", "따뜻하다"]
_G_EN = {"맵다": "spicily", "바쁘다": "busily", "예쁘다": "neatly; prettily", "친절하다": "kindly", "크다": "big; loudly", "짧다": "short; briefly", "싸다": "cheaply", "빠르다": "quickly", "맛있다": "deliciously", "많다": "a lot", "작다": "small; softly", "춥다": "coldly", "따뜻하다": "warmly"}
_GE_EX = [("이 책 예쁘게 포장해 주세요.", "Please wrap this book neatly."), ("저는 요즘 아주 바쁘게 지냅니다.", "I have been spending time very busily nowadays."), ("이 식당은 음식을 아주 맛있게 해요.", "This restaurant makes foods very deliciously.")]
_GE_OTHER = [("이 지갑을 예쁘게 포장해 주세요.", "Please wrap this wallet prettily. (the Core Vocabulary’s sentence)"), ("가게 점원이 친절하게 도와 주었습니다.", "The shop clerk helped me kindly. (a Core Vocabulary sentence)"), ("과일은 한양 식품점에서 싸게 팔아요.", "As for fruit, the Hanyang grocery store sells it cheaply. (Topic C memo)")]
_GE_MINE = [("이 식당은 음식을 맵게 만들어요.", "This restaurant makes food spicy. (mine)"), ("요즘 바쁘게 지내요.", "I am spending my time busily these days. (mine)"), ("그 가게에서는 옷을 싸게 팔아요.", "That store sells clothes cheaply. (mine)"), ("선생님이 한국말을 천천히 이야기해 주세요.", "The teacher speaks Korean slowly for us. (mine; 천천히 is already an adverb)")]
L9 = lesson(
    "Ch 12 · Grammar C: the “adverb maker” -게",
    "싸게 · 바쁘게 · 예쁘게 · 맛있게 · 예쁘게 포장해 주세요",
    requires=[],
    cards=[
        card("-게: making an adverb",
             "Adverbs are words that modify (describe) verbs, adjectives or other adverbs, as in work hard, truly happy or extremely slowly. Like truly and extremely, many English adverbs end in -ly; we know that these adverbs are derived from adjectives (true and extreme), and we make them adverbs by adding -ly, so -ly is an adverb “maker”. Korean has an adverb maker as well: 게. Simply by adding 게 to the stem of a stative verb, we make it an adverb: 싸게 (cheaply), 바쁘게 (busily).",
             examples=[D(a, b) for a, b in _GE_EX]),
        card("How to form it",
             "Forming Korean adverbs: stative verb stem + 게. The book’s examples are 예쁘다 → 예쁘게, 맛있다 → 맛있게 and 바쁘다 → 바쁘게. The table below is mine (the stem does not change, even for ㅂ irregular stems: 맵게, 춥게).",
             tables=[table(["Stative verb", "Adverb", "Rough meaning"], [[v, stem(v) + "게", _G_EN[v]] for v in _G_V], say=[0, 1])]),
        card("More examples with -게",
             "Sentences with -게 from the Core Vocabulary and Topic C memo, and my own (the English for those is mine).",
             examples=[D(a, b) for a, b in _GE_OTHER + _GE_MINE[:3]]),
        card("Follow-Up 1: stative verb → adverb, then write sentences",
             "The book gives eight stative verbs (맵다, 바쁘다, 예쁘다, 친절하다, 크다, 짧다, 싸다, 빠르다; the first, 맵다 → 맵게, is done for you) and eight action verbs (살다, 만들다, 지내다, 가다, 팔다, 자르다, 이야기하다, 먹다) and asks you to write three sentences using a stative verb from the left column and an action verb from the right column. The adverbs are in the table above; the sample sentences are mine (see the previous card).",
             tables=[table(["Stative verb", "Adverb"], [[v, stem(v) + "게"] for v in _G_V[:8]], say=[0, 1])]),
        card("Activities left out",
             "Follow-Up 2 (listening to four conversations at different businesses and writing the type of business and the customer’s specific request) is audio."),
    ],
    exercises=uniq(
        [M(f"What is the adverb form of {v}?", stem(v) + "게", _opts(stem(v) + "게", [stem(v) + "고", stem(v) + "지만", stem(v) + "서", if_(v)]), f"{v} → {stem(v)}게.") for v in _G_V]
        + [M(f"What does {stem(v)}게 mean?", _G_EN[v], _opts(_G_EN[v], [x for k, x in _G_EN.items() if x != _G_EN[v]]), f"{stem(v)}게 = {_G_EN[v]}.") for v in _G_V[:7]]
        + _tr(_GE_EX) + _tr(_GE_OTHER)
        + [M("What does the adverb maker -게 attach to?", "The stem of a stative verb", ["A noun", "An action verb’s ending", "A particle"], "싸다 → 싸게."), M("Which English suffix is like -게?", "-ly", ["-ing", "-ed", "-er"], "-ly makes adverbs."),
           F("이 책 ___ 포장해 주세요. (neatly)", "예쁘게", ["예쁜", "예쁘고"], "예쁘다 → 예쁘게."), F("저는 요즘 아주 ___ 지냅니다. (busily)", "바쁘게", ["바쁜", "바쁘고"], "바쁘다 → 바쁘게."), F("이 식당은 음식을 아주 ___ 해요. (deliciously)", "맛있게", ["맛있는", "맛있고"], "맛있다 → 맛있게."),
           F("과일은 한양 식품점에서 ___ 팔아요. (cheaply)", "싸게", ["싼", "싸고"], "싸다 → 싸게."), F("가게 점원이 ___ 도와 주었습니다. (kindly)", "친절하게", ["친절한", "친절하고"], "친절하다 → 친절하게."),
           read_q("싸게"), read_q("바쁘게"), read_q("예쁘게"), read_q("맛있게"), read_q("친절하게")]
    ),
)

# ================================================================== Grammar D: connectors
_SC = [("그리고", "and", "어제 영화를 봤어요. 그리고 쇼핑도 했어요."), ("그렇지만", "but, however", "이 옷은 너무 비싸요. 그렇지만 마음에 들어요."), ("하지만", "but, however", "이 옷은 너무 비싸요. 하지만 마음에 들어요."), ("그러나", "but, however", "오늘은 학교에 가는 날입니다. 그러나 집에서 쉬겠습니다."),
       ("그런데", "by the way", "내일 산호세 가서 쇼핑하자. 그런데, 한국식품점은 몇 시에 열어?"), ("그래서", "so; thus; therefore", "어제 늦게까지 공부했어. 그래서 좀 피곤해.")]
_VC = [("-고", "and", "어제 영화보고 쇼핑도 했어요."), ("-지만", "but", "이 옷은 너무 비싸지만 마음에 들어요."), ("-기 전에", "before", "저녁 먹기 전에 체육관에서 운동합니다."), ("-(으)ㄴ 후에", "after", "수업 끝난 후에 도서관에 갑니다."), ("-아/어서", "and, so, because (of)", "저녁에 한국 식당 가서 밥 먹자. 이번 주말은 바빠서 등산 못 가요."),
       ("-기 때문에", "because", "다음주에 시험이 있기 때문에 이번 주말에 공부를 해야 합니다."), ("-(으)면", "if, when", "피곤하면 오늘은 운동하지 마세요. 큰 하얀 건물이 나오면 우회전 하세요."), ("-(으)ㄹ 때", "when", "저는 영화 볼 때 늘 팝콘을 먹어요.")]
_NC = [("~와/과, ~하고, ~(이)랑", "and", "마켓에서 고기와 양념과 과일을 좀 샀습니다. 백화점에서 청바지하고 티셔츠를 세일해요. 생선이랑 소고기랑 닭고기가 모두 얼마에요?"), ("~(이)나", "or", "한국 음식이나 멕시코 음식을 먹고 싶어요.")]
_CONN_F4 = [("최 상병은 토요일마다 등산가요. 그리고 골프도 쳐요.", "최 상병은 토요일마다 등산 가고 골프도 쳐요.", "-고", "Corporal Choi goes hiking every Saturday and also plays golf."), ("저는 코미디 영화를 좋아해요. 그렇지만 액션 영화는 안 좋아해요.", "저는 코미디 영화를 좋아하지만 액션 영화는 안 좋아해요.", "-지만", "I like comedy movies, but I don’t like action movies."),
            ("신 일병은 말하기 연습을 많이 합니다. 그래서 한국말을 잘 합니다.", "신 일병은 말하기 연습을 많이 하기 때문에 한국말을 잘 합니다.", "-기 때문에", "PFC Shin practices speaking a lot, so he speaks Korean well.")]
L10 = lesson(
    "Ch 12 · Grammar D: connectors for sentences, verbs and nouns",
    "그리고 · 그렇지만 · 하지만 · 그러나 · 그런데 · 그래서 · -고 · -지만 · -(으)면 · ~와/과 · ~(이)나",
    requires=[],
    cards=[
        card("Three types of connectors",
             "You have learned quite a few connectors so far. They are categorized into three types: sentence connectors, verb connectors (or conjunctive endings) and noun connectors."),
        card("1. Sentence connectors",
             "Sentence connectors connect two independent clauses: 저는 초콜렛을 좋아합니다. 그리고 제 친구도 초콜렛을 좋아합니다. / 저는 초콜렛을 좋아합니다. 하지만 제 친구는 안 좋아합니다. (I like chocolate. And my friend likes chocolate too. / I like chocolate. But my friend doesn’t.) The book’s list is below; the English meanings are the book’s.",
             tables=[table(["Connector", "Meaning", "Example"], [[a, b, c] for a, b, c in _SC], say=[0, 2])]),
        card("2. Verb connectors (conjunctive endings)",
             "Verb connectors connect two clauses or verbs: 먹습니다 + -고 + 마십니다 → 먹고 마십니다; 저는 공부합니다 + -(으)ㄹ 때 + 음악을 듣습니다 → 저는 공부할 때 음악을 듣습니다. The book’s list is below.",
             tables=[table(["Connector", "Meaning", "Example"], [[a, b, c] for a, b, c in _VC], say=[2])]),
        card("3. Noun connectors",
             "Noun connectors connect nouns. In English, when we enumerate two or more nouns, we tend to use and/or before the last noun. However, Koreans tend to repeat the noun connector after every noun, as in 포도하고 딸기하고 사과, which translates as “grapes and strawberries and apples”.",
             tables=[table(["Connector", "Meaning", "Example"], [[a, b, c] for a, b, c in _NC], say=[2])], examples=[D("포도하고 딸기하고 사과", "grapes and strawberries and apples")]),
        card("-지만 versus 그렇지만 (from Chapter 11)",
             "As the book said in Chapter 11, -지만 is a conjunctive ending attached to the verb in the first clause, whereas 그렇지만 and 하지만 are adverbs that come between two independent clauses separated by a period. The same holds for the other pairs: -고 / 그리고, -기 때문에 / 그래서.",
             examples=[D("한국말이 어렵지만 재미있어요.", "Although Korean is difficult, it is fun."), D("한국말이 어려워요. 그렇지만 재미있어요.", "Korean is difficult. However, it is fun.")]),
        card("Follow-Up 4a: combine two sentences with a verb connector",
             "The book gives three pairs of sentences joined by a sentence connector and asks you to combine each into one sentence with a verb connector without changing the meaning of the first sentence. The book prints the second sentence’s blank only; my full answers are below (the book’s sentence 1 reads 등산가요; I write 등산 가고).",
             tables=[table(["Two sentences", "Combined", "Connector", "Meaning"], [[a, b, c, d] for a, b, c, d in _CONN_F4], say=[0, 1])]),
        card("Follow-Up 4b: any two verbs and a conjunctive ending",
             "In the book, one partner reads a strip with a verb or verb phrase and the other a second one, and the pair make a sentence with a conjunctive ending. The book’s model: 아침 먹다 + 운동하다 → 아침 먹기 전에 운동합니다 or 아침 먹은 후에 운동합니다 (I exercise before I have breakfast / I exercise after I have breakfast). The strips are not shown.",
             examples=[D("아침 먹기 전에 운동합니다.", "I exercise before I have breakfast."), D("아침 먹은 후에 운동합니다.", "I exercise after I have breakfast.")]),
        card("Activities left out",
             "Follow-Up 3 (SMART Board) is a SMART Board activity, and the strip game of Follow-Up 4b is a partner activity."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _SC[:1] + _SC[1:2] + _SC[4:]]) + [M(f"What does {a} mean?", b, _opts(b, [x[1] for x in _VC]), f"{a} = {b}.") for a, b, c in _VC] + [M("What does ~(이)나 mean?", "or", ["and", "but", "with"], "한국 음식이나 멕시코 음식."), M("What does ~하고 mean as a noun connector?", "and", ["or", "but", "if"], "포도하고 딸기하고 사과.")]
        + [M(f"Which connector fits: {a}", c, _opts(c, ["-고", "-지만", "-기 때문에", "-(으)ㄹ 때", "-기 전에"]), d) for a, b, c, d in _CONN_F4]
        + [M("Where do Koreans put the noun connector when listing nouns?", "After every noun", ["Only before the last noun", "Only after the first noun", "Nowhere"], "포도하고 딸기하고 사과."), M("Which connector is placed between two sentences?", "하지만", ["-지만", "-고", "-(으)면"], "하지만 = sentence connector."), M("Which connector is a conjunctive ending?", "-(으)면", ["그래서", "그리고", "그러나"], "-(으)면 attaches to a verb."),
           F("어제 늦게까지 공부했어. ___ 좀 피곤해. (so)", "그래서", ["그런데", "그리고"], "그래서 = so."), F("이 옷은 너무 비싸요. ___ 마음에 들어요. (but)", "그렇지만", ["그래서", "그리고"], "그렇지만 = but."), F("저녁 먹기 ___ 체육관에서 운동합니다. (before)", "전에", ["후에", "때문에"], "-기 전에 = before."), F("수업 끝난 ___ 도서관에 갑니다. (after)", "후에", ["전에", "때문에"], "-(으)ㄴ 후에 = after."),
           F("마켓에서 고기___ 양념과 과일을 좀 샀습니다. (and)", "와", ["나", "고"], "고기 ends in a vowel: 와."), F("한국 음식___ 멕시코 음식을 먹고 싶어요. (or)", "이나", ["이랑", "하고"], "~(이)나 = or."),
           read_q("그렇지만"), read_q("그래서"), read_q("먹기 전에"), read_q("끝난 후에"), read_q("포도하고 딸기하고 사과")]
    ),
)


# ================================================================== Activities C: market expressions and ads
_EXP6 = [("양념 파는 데가 어디 있어요?", "Looking for items", "Where is the place that sells seasonings?"), ("사과는 어디서 팔아요?", "Looking for items", "Where do you sell apples?"), ("얼마예요?", "Asking prices", "How much is it?"),
         ("더 필요한 거 있으세요?", "Offering help", "Is there anything else you need?"), ("계산해 드리겠습니다.", "Offering help", "I’ll ring you up."), ("요즘 포도 값이 얼마예요?", "Asking prices", "How much are grapes these days?")]
_ADS = [("아리랑마트", "설탕", "1 box", "1.79 → 0.99", (0, 99)), ("아리랑마트", "포도", "1 lb", "3.99 → 2.49", (2, 49)), ("아리랑마트", "돼지고기", "1 lb", "2.99 → 2.19", (2, 19)), ("아리랑마트", "사과", "3 lb", "3.99", (3, 99)), ("아리랑마트", "간장", "1 each", "3.99", (3, 99)), ("아리랑마트", "고추장", "1 each", "5.99", (5, 99)),
        ("가주마켓", "딸기", "2 lb", "4.99 → 3.99", (3, 99)), ("가주마켓", "사과", "1 lb", "1.99 → 0.99", (0, 99)), ("가주마켓", "생선", "1 lb", "2.99 → 1.99", (1, 99)), ("가주마켓", "소고기", "1 lb", "2.15", (2, 15)), ("가주마켓", "닭고기", "1 lb", "1.39", (1, 39)), ("가주마켓", "고추장", "1 each", "5.99 → 4.99", (4, 99))]
_MANGO = [("A", "망고가 어디에 있어요?", "Where are the mangoes?"), ("B", "계산대 앞쪽에 양념 파는 데가 있고, 그 옆에 과일 파는 데가 있어요. 망고는 포도 옆에 있어요.", "In front of the counter there is the seasoning section, and next to it is the fruit section. The mangoes are next to the grapes.")]
_MARKET_EX = [("양념 파는 데가 어디 있어요?", "Where is the place that sells seasonings?"), ("사과는 어디서 팔아요?", "Where do you sell apples?"), ("요즘 포도 값이 얼마예요?", "How much are grapes these days?"), ("더 필요한 거 있으세요?", "Is there anything else you need?"), ("계산해 드리겠습니다.", "I’ll ring you up.")]
L11 = lesson(
    "Ch 12 · Activities C: market expressions and grocery ads",
    "얼마예요? · 어디서 팔아요? · 계산해 드리겠습니다 · 아리랑마트 · 가주마켓",
    requires=[],
    cards=[
        card("Activity 1b (Reading): expressions used at a market",
             "The book gives six sentences people use at a market and asks you to classify them into expressions for looking for items, offering help and asking prices. The English is mine.",
             tables=[table(["Sentence", "Category", "Meaning"], [[a, b, c] for a, b, c in _EXP6], say=[0])]),
        card("Activity 2b (Reading): two Korean market ads",
             "SPC Jones found two Korean market ads in the Korean newspaper; the book asks you to circle the items she needs to purchase and check the prices using a shopping list you made while listening to PV2 Lee’s phone message (the message is audio and is not reproduced, so the list is not shown). The ads’ items and prices are below; the book’s numbers show the old price, an arrow and the sale price (1 lb is one pound, 1 ea one each, as in the ads). The Korean readings of the sale prices are mine.",
             tables=[table(["Market", "Item", "Amount", "Price (dollars)", "Sale price in Korean"], [[m, i, a, p, _usd(*c) if False else (f"{_kn(c[0])} 달러 " if c[0] else "") + f"{_kn(c[1])} 센트"] for m, i, a, p, c in _ADS], say=[0, 1, 4], note="아리랑마트 has a big sale (대세일); 가주마켓 has a sale (세일).")]),
        card("Activity 3 (Reading and speaking): role-play at a Korean market",
             "In the book, you pair up and role-play a shopper who is having a hard time finding grocery items and a very friendly clerk who gives specific and detailed directions, using a map of the market and a shopping list (A or B; the maps and lists are not shown). The book’s model is below (the English is mine; 망고 is “mango”).",
             examples=dlg(_MANGO)),
        card("Useful expressions",
             "The expressions of Activity 1b are the ones to use in that role-play (the English is mine).",
             examples=[D(a, b) for a, b in _MARKET_EX]),
        card("Activities left out",
             "Activity 1a (SMART Board), Activity 2a (listening to PV2 Lee’s phone message and writing her and her roommate’s items and quantities) and the maps and shopping lists of Activity 3 are SMART Board, audio, picture or partner activities."),
    ],
    exercises=uniq(
        _tr([(a, c) for a, b, c in _EXP6]) + _tr(_strip(_MANGO)) + [M(f"Which category does “{a}” belong to?", b, _opts(b, ["Looking for items", "Offering help", "Asking prices"]), c) for a, b, c in _EXP6]
        + [M(f"What is the sale price of {i} at {m}?", f"{p.split('→')[-1].strip()} dollars", _opts(f"{p.split('→')[-1].strip()} dollars", [f"{x[3].split('→')[-1].strip()} dollars" for x in _ADS]), f"{i}: {p}.") for m, i, a, p, c in _ADS if "→" in p][:4]
        + [M("Where are the mangoes in the book’s model?", "Next to the grapes", ["Next to the counter", "Next to the fish", "In front of the entrance"], "망고는 포도 옆에 있어요."), M("What does 값 mean?", "price", ["change", "fruit", "counter"], "포도 값 = the price of grapes."),
           F("사과는 어디서 ___? (do you sell)", "팔아요", ["사요", "깎아요"], "팔다 = to sell."), F("더 필요한 ___ 있으세요? (a thing)", "거", ["데", "곳"], "거 = 것 (spoken)."), F("___ 드리겠습니다. (I’ll ring you up)", "계산해", ["고르어", "포장해"], "계산해 드리겠습니다."),
           read_q("아리랑마트"), read_q("가주마켓"), read_q("포도 값이"), read_q("양념 파는 데가")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
def _uo(*texts):
    over = {}
    for t in texts:
        for w in _re.findall(r"[가-힣]+의", t):
            over[w] = _K.pron(w[:-1] + "에")
    return over


_V_GIFT = [("귀걸이", "an earring; “ear hanger”", "이 귀걸이가 마음에 들어요."), ("깎다", "to cut or shave off (price); to discount", "너무 비싸요. 좀 깎아 주세요."), ("목걸이", "a necklace; “neck hanger”", "남자 친구가 생일선물로 루비 목걸이를 주었습니다."), ("반지", "a (finger) ring", "결혼할 때 다이아몬드 반지를 받았습니다."),
           ("시계", "a clock; a watch", "제 시계는 오 분 빨라요."), ("점원", "a store clerk", "가게 점원이 친절하게 도와 주었습니다."), ("주인", "an owner", "가게 주인이 좀 깎아 주었습니다."), ("지갑", "a wallet; a purse", "지갑에 돈이 별로 없어요."), ("찾다", "to look for; to find", "무엇을 찾으세요?"),
           ("팔찌", "a bracelet", "생일 선물로 팔찌를 받았어요."), ("포장", "wrapping; packing", "이 넥타이 예쁘게 포장해 주세요."), ("포장하다", "to wrap", "이 넥타이 예쁘게 포장해 주세요.")]
_V_POST = [("부치다", "to mail", "어제 부모님께 소포를 부쳤습니다."), ("소포", "a parcel; a package", "크리스마스 선물을 사서 부모님께 소포로 보냈습니다."), ("엽서", "a postcard", "여행가서 친구한테 엽서를 보냈어요."), ("우표", "a postage stamp", "우체국에서 우표 열 장을 샀습니다."),
           ("장", "a counter for sheets (of paper, cloth, postcards, etc.)", "엽서 열 장 주세요."), ("편지", "a letter", "요즘 사람들은 이메일을 많이 쓰고 편지는 잘 안 씁니다.")]
_V_WEAR = [("구두", "formal shoes", "이 구두는 너무 커요."), ("모자", "a hat; a cap", "밖에서 운동할 때는 모자를 쓰세요."), ("바지", "pants; trousers", "저는 치마보다 바지가 더 편해요."), ("신발", "footwear; shoes", "신발 가게에서 구두를 샀어요."),
           ("안경", "eyeglasses", "저희 어머니는 칠십 세이십니다. 그래서 책을 보실 때 안경이 필요합니다."), ("양말", "socks", "저는 집에서는 양말을 신지 않습니다."), ("양복", "a suit (western style for men); “western clothes”", "세탁소에 결혼식 때 입을 양복을 맡겨 주세요."),
           ("운동화", "athletic shoes; sneakers; “exercise shoe”", "요즘 나이키 운동화가 세일입니다."), ("잠바", "a windbreaker", "날씨가 추워서 잠바를 입었어요."), ("장갑", "gloves", "장갑을 끼고 눈사람을 만들었어요."), ("청바지", "blue jeans; “blue pants”", "저는 리바이스 청바지를 좋아합니다."), ("치마", "a skirt", "그 치마랑 블라우스가 아주 잘 어울려요.")]
_V_VERB = [("끼다", "to put on/wear (rings, bracelets, gloves, etc.); “to insert”", "김 일병은 늘 결혼 반지를 끼고 있어요."), ("매다", "to put on/wear (items worn by tying); “to tie”", "양복을 입을 때는 넥타이를 매야 해요."), ("신다", "to put on/wear (footwear)", "이 운동화 좀 신어 보세요. 아주 편해요."),
           ("쓰다", "to put on/wear (items worn to cover the head or face)", "여름에는 밖에 나갈 때 모자를 쓰세요."), ("차다", "to put on/wear (items worn by fastening them on); “to fasten”", "총은 어디에 찹니까?")]
_V_COL = [("회색", "gray (color)", "콘크리트는 회색입니다.")]
_V_GRO = [("간장", "soy sauce", "싱거우면 간장을 더 넣으세요."), ("계산", "calculation; computation; counting", "계산 좀 해 주세요."), ("계산하다", "to calculate; to compute; to count", "엘에이 여행하면 비용이 얼마나 들어요? 계산 좀 해 주세요."), ("계산대", "a counter; “counting board”", "물건을 다 사신 후 계산대로 오세요."),
          ("고기", "meat", "저는 고기를 못 먹습니다."), ("고추장", "red pepper paste", "한국 음식을 만들 때 고추장을 많이 써요."), ("과일", "fruit", "제가 좋아하는 과일은 오렌지입니다."), ("닭", "a chicken", "저는 닭고기를 좋아해서 치킨 버거를 자주 먹어요."),
          ("돼지", "a pig", "이 돈가스는 아주 좋은 돼지고기로 만들었어요."), ("된장", "soy bean paste", "이 식당은 된장찌개가 맛있어요."), ("딸기", "a strawberry", "딸기 두 파운드만 주세요."), ("사과", "an apple", "저 사과는 파운드에 얼마예요?"), ("생선", "fish (for eating)", "고기는 안 먹지만 생선은 먹습니다."),
          ("설탕", "sugar", "커피가 너무 쓰면 설탕을 좀 넣으세요."), ("소", "a cow", "불고기 만들 소고기 좀 사 오세요."), ("식초", "vinegar", "저는 신 맛을 좋아해서 식초를 많이 넣어요."), ("식품", "a grocery; “eating item”", "산호세에는 큰 한국 식품점이 있습니다."), ("식품점", "a grocery store", "산호세에는 큰 한국 식품점이 있습니다."),
          ("양념", "seasoning; spices", "소금과 설탕은 요리할 때 많이 쓰는 양념입니다."), ("포도", "a grape", "포도가 달고 싱싱하네요."), ("후추", "black pepper", "저는 후추의 매운 맛이 좋아요.")]
_V_LOAN = [("넥타이", "a necktie", "파란색 넥타이하고 흰색 와이셔츠가 잘 어울립니다."), ("벨트", "a belt", "그 바지에는 검은색 벨트가 어울려요."), ("블라우스", "a blouse", "저는 실크 블라우스를 좋아해요."), ("사이즈", "size", "이 바지는 저한테 너무 커요. 더 작은 사이즈로 보여주세요."), ("선글라스", "sunglasses", "운전할 때 선글라스가 필요합니다."),
           ("센트", "a cent", "일 달러는 백 센트입니다."), ("스웨터", "a sweater", "이 캐시미어 스웨터는 아주 따뜻해요."), ("스카프", "a scarf", "그 스카프가 옷에 잘 어울려요."), ("스커트", "a skirt", "올해 여름에는 미니스커트가 유행이에요."), ("스타킹", "stockings", "스커트를 입을 때는 보통 스타킹을 신어요."),
           ("와이셔츠", "a dress shirt; “Y-shirt”", "그 양복에는 파란색 와이셔츠가 어울려요."), ("원피스", "a one-piece dress/suit", "친구 생일 파티에 원피스를 입고 갔어요."), ("재킷", "a jacket", "요즘 어떤 스타일의 재킷이 유행입니까?"), ("코트", "a coat", "이번 겨울에 입을 코트를 샀어요."),
           ("투피스", "a two-piece dress/suit", "저는 투피스를 입을 때는 블라우스를 입어요."), ("티셔츠", "a T-shirt", "운동하기 전에 티셔츠로 갈아 입었어요."), ("핸드백", "a handbag", "핸드백에 지갑하고 열쇠가 있습니다.")]
_V_OTH = [("거스름돈", "change; “changed money”", "여기 거스름돈 오십 센트 있어요."), ("고르다", "to select; to choose", "백화점은 물건이 많아서 고르기가 힘들어요."), ("그럼요", "Of course (in response to a request or question).", "그럼요."), ("데", "a place; a spot", "고기 파는 데가 어디입니까?"),
          ("맞다", "to fit; to suit; to be correct", "이 코트는 저한테 사이즈가 잘 맞아요. 크지도 작지도 않아요."), ("뭐", "what; abbreviation of 무엇", "뭐 사고 싶어요?"), ("보여주다", "to show; to display", "이 색은 맘에 안 들어요. 다른 색 티셔츠로 보여주세요."), ("불", "a counter for dollars", "이 옷은 원래 칠십 달러였어요. 그런데 세일해서 오십 불에 샀어요."),
          ("싱싱하다", "to be fresh (for food)", "과일이 아주 싱싱합니다."), ("원래", "originally", "이 지갑이 원래 백 달러인데 구십오 불에 샀어요."), ("인기", "popularity", "요즘 아이폰이 인기가 많아요."), ("친절", "kindness", "선물 가게 점원이 아주 친절했습니다."), ("친절하다", "to be kind; to be friendly", "선물 가게 점원이 아주 친절했습니다."),
          ("팔다", "to sell", "저희는 싱싱한 과일만 팔아요.")]
_V_GR = [["-게", "-ly; “adverb maker”", "이 지갑을 예쁘게 포장해 주세요."], ["-아/어도 되다", "(you) may …; “It is all right if …”", "저… 전화 좀 써도 돼요?"], ["-(으)면 안 되다", "should not …; must not …; “It is not all right if …”", "도서관에서 음식을 먹으면 안 됩니다."]]
_V_SINO = [("우", "(郵) mail", "우체국, 우표, 우편")]
_V_ALL = _V_GIFT + _V_POST + _V_WEAR + _V_VERB + _V_COL + _V_GRO + _V_LOAN + _V_OTH
_V_OVER = _uo(*[e for _, _, e in _V_ALL])
_V_SKIP = ("포장하다", "계산", "식품", "계산하다", "친절", "끼다", "매다", "신다", "쓰다", "차다", "불", "장", "소", "닭", "뭐", "데", "그럼요")
L12 = lesson(
    "Ch 12 · Core vocabulary and self-evaluation",
    "주요 단어 · 선물 가게 · 우체국 · 옷 · 입다 신다 쓰다 매다 끼다 차다 · 식품 · 우 (郵) · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). The book writes some words as groups (포장(~하다), 계산(~하다), 식품(점), 친절(~하다), 그럼(요)); they are split here, and a word without a sentence of its own reuses the book’s. The book’s Additional Vocabulary section is a blank list for words you add yourself.\n\n"
             "Digits are respelled in Hangul (5분 → 오 분, 70세 → 칠십 세, 10장 → 열 장, 2파운드 → 두 파운드, 1달러는 100센트 → 일 달러는 백 센트, 50센트 → 오십 센트, 70달러 → 칠십 달러, 50불 → 오십 불, 100달러 → 백 달러, 95불 → 구십오 불); the possessive 의 after a thing is said 에 (후추의 → 후추에). 총 and 수통 are not in the Core Vocabulary; they appear in the table of the “wear” verbs."),
        card("At a gift shop", "", tables=[vt(_V_GIFT, over=_V_OVER)]),
        card("At the post office", "", tables=[vt(_V_POST, over=_V_OVER)]),
        card("(Things) to wear", "", tables=[vt(_V_WEAR, over=_V_OVER)]),
        card("Verbs that express “to wear” or “to put on”", "", tables=[vt(_V_VERB, over=_V_OVER)]),
        card("More colors", "", tables=[vt(_V_COL, over=_V_OVER)]),
        card("Grocery items", "", tables=[vt(_V_GRO, over=_V_OVER)]),
        card("Loan words", "", tables=[vt(_V_LOAN, over=_V_OVER)]),
        card("Other words", "Italicized English words in the book are grammatical terms, not the meaning of a Korean word. The book lists 데 as “-데” and 그럼(요) with 요 in parentheses, and 불 with a tilde (~불).", tables=[vt(_V_OTH, over=_V_OVER)]),
        card("Grammar words that have their own lessons", "-게, -아/어도 되다 and -(으)면 안 되다 are explained in the grammar lessons of this chapter.", tables=[table(["Form", "Meaning", "Example"], _V_GR, say=[2])]),
        card("Sino-Korean vocabulary", "", tables=[vt(_V_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: inquire about or answer questions about items in various stores (gift shop, post office, clothing store, grocery store, etc.); ask a person to do something; use verbs that denote to put on/wear.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the auxiliary verb -아/어도 되다; the auxiliary verb -(으)면 안 되다; the “adverb maker” 게; various “connectors” for sentences, verbs and nouns; the Sino-Korean syllable 우 (郵)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _V_ALL if k not in _V_SKIP])
        + [M("What does the Sino-Korean syllable 우 (郵) mean?", "mail", ["room", "people", "expense"], "우체국, 우표, 우편."), M("What does -게 mean?", "-ly; “adverb maker”", ["but", "if", "when"], "예쁘게 = prettily."), M("What does -아/어도 되다 mean?", "(you) may …", ["should not …", "will …", "can’t …"], "전화 좀 써도 돼요?"), M("What does -(으)면 안 되다 mean?", "should not …; must not …", ["(you) may …", "will …", "can’t …"], "먹으면 안 됩니다."),
           M("Which verb is for rings, bracelets and gloves?", "끼다", ["매다", "신다", "차다"], "장갑을 끼다."), M("Which verb is for neckties and belts?", "매다", ["끼다", "신다", "쓰다"], "넥타이를 매다."), M("Which verb is for footwear?", "신다", ["입다", "쓰다", "차다"], "운동화를 신다."), M("Which verb is for hats and glasses?", "쓰다", ["입다", "신다", "차다"], "모자를 쓰다."),
           M("Which verb is for watches?", "차다", ["끼다", "매다", "쓰다"], "시계를 차다."), M("Which is a type of meat?", "소고기", ["설탕", "후추", "식초"], "소고기 = beef."), M("Which is a seasoning?", "후추", ["딸기", "닭고기", "소고기"], "후추 = black pepper."),
           F("이 지갑을 ___ 포장해 주세요. (prettily)", "예쁘게", ["예쁜", "예쁘고"], "-게 = adverb."), F("가게 주인이 이십 불을 ___ 주었습니다. (discounted)", "깎아", ["부쳐", "골라"], "깎다 = to discount."), F("어제 부모님께 소포를 ___. (mailed)", "부쳤습니다", ["깎았습니다", "포장했습니다"], "부치다 = to mail."),
           F("커피가 너무 쓰면 ___을 좀 넣으세요. (sugar)", "설탕", ["후추", "식초"], "설탕 = sugar."), F("요즘 아이폰이 ___가 많아요. (popularity)", "인기", ["사이즈", "주인"], "인기가 많다 = to be popular.")]
        + [read_q("주요 단어"), read_q("귀걸이"), read_q("운동화"), read_q("계산대"), read_q("식품점"), read_q("우체국")]
    ),
)

UNIT = unit("Semester 1 · Unit 3 · Chapter 12: Shopping in Koreatown (코리아타운에서 쇼핑하기)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])

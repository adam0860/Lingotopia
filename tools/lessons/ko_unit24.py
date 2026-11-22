"""Unit 24: KBC Semester 1, Unit 5, Chapter 17 - Cultural Life (문화생활).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 5, Student's Edition (2022).
Audio, video clips, photos, graphs, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_kbc import _B_IRR, _base_ao
from ko_unit21 import _kn, _won


import dsl_ko as _DK
import ko_kbc as _KB


def _sp(ko):
    """spoken Korean lines carry no quotation marks, middle dots or parentheses (the book’s are dropped when read aloud)"""
    return _re.sub(r"[‘’“”·()]", "", ko).replace("  ", " ")


def passage(lines, over=None):
    return _KB.passage([(_sp(a), b) for a, b in lines], over)


def dlg(lines, over=None):
    return _DK.dlg([(l[0], _sp(l[1]), *l[2:]) for l in lines], over)


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        wrong = list(dict.fromkeys(x for _, x in pairs if x != b))[:k]
        out.append(M(f"What does {a} mean?", b, wrong, f"{a} means “{b}”."))
    return out


def _strip(lines):
    return [(l[1], l[2]) for l in lines]


def _show(key):
    """the Korean word shown for a dictionary key such as '~회 (round)'"""
    return key.split(" (")[0] if " (" in key and not key.startswith("(") else key


def _kit(allw, extra):
    """(_en, _pairs, _rows) for a dictionary of core words: key -> (key, meaning, example)"""
    def en(word):
        if word in extra:
            return extra[word]
        t = _re.sub(r"^\([^)]*(\([^)]*\))?[^)]*\) ", "", allw[word][1])
        return _clean(_re.sub(r" \(~[^)]*\)", "", t))

    def pairs(words):
        return [(_show(w), en(w)) for w in words]

    def rows(words):
        return [(_show(w), extra[w] if w in extra else allw[w][1]) for w in words]
    return en, pairs, rows


_IRR = _B_IRR + ("더럽다", "뜨겁다", "차갑다", "무섭다", "외롭다", "아름답다")


def _ao(verb):
    if verb in _IRR:
        st = stem(verb)
        l, v, t = _K.decompose(st[-1])
        return st[:-1] + _K.compose(l, v, "") + "워"
    return informal(verb)[:-1]


# ---- the core vocabulary of Chapter 17 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_LEIS = [
    ("악기", "(樂器) a musical instrument", "악기 중에 바이올린을 켤 줄 알아요."),
    ("연주", "(演奏) a musical performance (~하다: to play a musical instrument)", "동생이 피아노를 연주합니다."),
    ("낚시", "fishing (~하다: to fish)", f"{sino(40)} 대 남자들이 가장 좋아하는 취미는 낚시입니다."),
    ("암벽등반", "(岩壁登攀) rock climbing; “rock-wall climbing”", "제 취미는 암벽등반입니다."),
    ("즐기다", "to enjoy", "많은 한국 사람들이 주말에 주로 등산을 즐깁니다."),
]
_CV_EVENT = [
    ("관람", "(觀覽) viewing; watching (a movie, play, concert, etc.) (~하다: to view; to watch)", "주말에는 보통 영화를 관람합니다."),
    ("공연", "(公演) a performance; a play (~하다: to perform)", "김 선생님, 음악 공연 자주 보러 가세요?"),
    ("관심", "(關心) (an) interest", "디엘아이 학생들은 외국어에 관심이 많습니다."),
    ("무용", "(舞踊) dancing; a dance (~하다: to dance)", "한국 무용공연 표 두 장 주세요."),
    ("미술", "(美術) art; fine arts", "제 동생은 대학교에서 미술을 공부합니다."),
    ("연극", "(演劇) a (theatrical) play", "어제 극장에서 ‘로미오와 줄리엣’ 연극을 봤어요."),
    ("연령", "(年齡) age", f"이 전시회는 관람 연령이 {sino(5)} 세 이상입니다."),
    ("예매", "(豫買) advance purchase; booking; making a reservation (~하다: to purchase in advance; to book; to reserve)", "연극 표 세 장을 인터넷에서 예매했어요."),
    ("음악회", "(音樂會) a concert; a recital; “music meeting”", "정 상병은 라이브 공연을 좋아해서 음악회에 자주 갑니다."),
    ("일반석", "(一般席) a general admission seat; a coach class seat; “general seat” (“special seat”)", "일반석이 에스석보다 쌉니다."),
    ("전시회", "(展示會) an exhibition; “display meeting”", "주말에 미술 전시회에 갑시다."),
    ("초대권", "(招待券) a complimentary ticket; a free ticket", "연극 초대권이 있어서 무료로 봤습니다."),
    ("활동", "(活動) activity (~하다: to be active)", "주말에는 보통 레저 활동을 합니다."),
    ("행사", "(行事) an event", "큰 문화 행사 때문에 길이 막힙니다."),
]
_CV_NET = [
    ("개인", "(個人) an individual; “each person”", "인터넷으로 물건을 사려면 이름, 주소 등 개인 정보가 필요합니다."),
    ("검색", "(檢索) search (~하다: to search)", "인터넷으로 공연 시간을 검색해 보세요."),
    ("누르다", "to press; to click", "안내원과 통화를 원하시면 영 번을 누르세요."),
    ("정보", "(情報) information; intelligence", "공연 정보 좀 알려 주세요."),
    ("주소", "(住所) an address", "여기에 집 주소를 써 주세요."),
]
_CV_MOVIE = [
    ("감독", "(監督) a (movie) director; a head coach; an overseer (~하다: to direct; to oversee)", "영화 ‘인디아나 존스’는 감독이 누구입니까?"),
    ("공포", "(恐怖) horror", f"‘{sino(13)} 일의 금요일’은 공포 영화입니다."),
    ("관객", "(觀客) an audience", "관객이 너무 많아서 표가 매진되었습니다."),
    ("극장", "(劇場) a theater; a playhouse", "친구와 함께 영화를 보러 극장에 갔습니다."),
    ("매진", "(賣盡) a sellout (~되다: to be sold out)", "그 영화는 너무 인기가 많아서 표가 매진됐습니다."),
    ("배우", "(俳優) an actor; an actress", "제가 좋아하는 영화 배우는 브래드 피트입니다."),
    ("상영", "(上映) a screening (of a movie); playing (a movie) (~하다: to show a movie)", "다음 영화는 열한 시부터 상영합니다."),
    ("제목", "(題目) a title; a heading", "보통 영화 제목을 보고 영화를 고릅니다."),
    ("조조할인", "(早朝割引) a matinee discount; “early morning discount”", "아침 첫 번째 영화는 조조할인을 받으실 수 있습니다."),
    ("주연", "(主演) starring; a main character (~하다: to play a leading role; to star)", "매트릭스는 키아누 리브스가 주연한 영화입니다."),
    ("학생증", "(學生證) a student ID card; “student certificate”", "영화 할인을 받으려고 학생증을 보여주었습니다."),
    ("~회 (round)", "(回) a time; a round", "첫 회는 아침 열 시부터 상영됩니다."),
]
_CV_LOAN = [
    ("게임", "a game", "컴퓨터 게임을 하면 시간이 너무 빨리 갑니다."),
    ("레저", "leisure", "박 일병은 암벽등반이나 스쿠버 다이빙 등의 레저 활동을 즐깁니다."),
    ("뮤지컬", "a musical", "요즘 연극 공연 중에 뮤지컬 ‘캣츠’가 인기가 많아요."),
    ("바이올린", "a violin", "바이올린, 비올라, 첼로 중에 바이올린이 제일 작아요."),
    ("발레", "ballet", "다섯 살 때부터 발레를 배웠습니다."),
    ("버튼", "a button", "먼저 “시작” 버튼을 눌러 주세요."),
    ("스포츠", "a sport; sports", "저는 스포츠 중에 야구를 좋아합니다."),
    ("액션", "action", "영영칠 영화는 액션 영화입니다."),
    ("인터넷", "the internet", "인터넷에서 많은 정보를 찾습니다."),
    ("코미디 / 코메디", "comedy", "예스맨은 아주 재미있는 코미디 영화입니다."),
    ("티켓", "a ticket", "비행기 티켓은 이메일로 보내 주세요."),
    ("피아노", "a piano", "음악을 좋아해서 피아노를 배웠습니다."),
    ("헬스", "fitness activity; “health”", "저는 매일 체육관에 가서 헬스를 합니다."),
    ("홈페이지", "a home page", "디엘아이 인터넷 홈페이지 주소를 알려 드릴게요."),
]
_CV_OTH = [
    ("~개월", "a counter for months", f"저는 작년 {sino(3)} 개월 동안 서울에서 살았어요."),
    ("결제", "(決濟) payment; settlement (~하다/되다: to pay; to make a payment)", "신용카드로 결제하면 편리합니다."),
    ("곧", "soon; at once", "곧 운동하러 체육관에 갈 겁니다."),
    ("-(으)ㄴ/는/(으)ㄹ 것 같다", "it seems that …; it looks like …", "이 뮤지컬 공연이 재미있을 것 같습니다."),
    ("다양", "(多樣) variety (~하다: to be various; to be diverse)", "정 일병은 암벽등반, 음악 감상 등 취미가 다양합니다."),
    ("~대/세대", "~generation/a generation (i.e. 20대 means “people in their 20’s” etc.)", f"보통 {sino(10)} 대나 {sino(20)} 대는 운동을 많이 해요."),
    ("무섭다", "to be fearful; to be scared; to be scary", "저는 무서운 영화는 잘 안 봅니다."),
    ("미리", "in advance; ahead of time", "공연 전에 미리 표를 예매하면 편합니다."),
    ("방금", "(方今) just now", "동생이 방금 학교에서 돌아왔습니다."),
    ("방법", "a method", "저는 인터넷으로 표 사는 방법을 몰라요."),
    ("선택", "(選擇) selection; choice (~하다/되다: to select; to choose/to be selected; to be chosen)", "웹사이트에서 원하는 공연을 선택한 후 버튼을 누르세요."),
    ("시간이 나다", "to have free time; to have spare time; “time pops out”", "시간이 나면 친구한테 전화를 합니다."),
    ("싫다", "to be dislikable; to be not in favor of", "록 음악은 시끄러워서 싫어요."),
    ("어느", "~ which", "몬트레이에서 어느 식당이 제일 맛있어요?"),
    ("~ 이상", "(以上) [number] and above", f"이 영화는 {sino(19)} 세 이상만 볼 수 있습니다."),
    ("조사", "(調査) a survey; investigation (~하다/되다: to survey; to investigate)", "한국 갤럽은 한국인이 좋아하는 영화에 대해서 조사했습니다."),
    ("주로", "mainly; mostly; primarily", "저는 주로 아침 식사로 빵을 먹습니다."),
    ("판매", "(販賣) sale(s) (~하다/되다: to sell/to be sold)", "이 공연 티켓은 어디서 판매합니까?"),
]
_CV_SINO = [("~회 (gathering)", "(會) a gathering; a meeting; a convention; a party", "동호회, 동창회, 산악회, 학회")]
_ALL = {r[0]: r for r in _CV_LEIS + _CV_EVENT + _CV_NET + _CV_MOVIE + _CV_LOAN + _CV_OTH + _CV_SINO}
_EXTRA = {"등산": "hiking; mountain climbing (mine)", "독서": "reading (mine)", "취미": "a hobby (mine)", "악기 연주": "playing a musical instrument (mine)", "회사": "a company; “meeting and gathering”",
          "회의": "a conference; a meeting; “meeting and discussion”", "교회": "a church; “[religious] teaching gathering”", "회의실": "a conference room (mine)", "회사원": "a company employee (mine)", "한인회장": "the president of a Korean association (mine)",
          "회원": "a member; “meeting member”", "회비": "a membership fee; “meeting fee”", "영화": "a movie (mine)", "신용카드": "a credit card (mine)", "좌석": "a seat (mine)", "공연장": "a theater; a performance hall (mine)", "로그인": "logging in (mine)",
          "회원 가입": "membership sign-up (mine)", "마지막으로": "finally (mine)", "동창회": "an alumni association (mine)", "산악회": "a mountaineering club (mine)", "학회": "an academic society (mine)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)


# ================================================================== Objectives and the Sino-Korean syllable 회
_HOE = [("회사", "a company; “meeting and gathering”"), ("회의", "a conference; a meeting; “meeting and discussion”"), ("전시회", "an exhibition; “display gathering”"), ("교회", "a church; “[religious] teaching gathering”"),
        ("음악회", "a concert; “music meeting” (the book’s Core Vocabulary)"), ("회의실", "a conference room (mine)"), ("회비", "a membership fee; “meeting fee” (the book’s Core Vocabulary, Chapter 19)"), ("회사원", "a company employee (mine)"),
        ("회원", "a member; “meeting member” (the book’s Core Vocabulary, Chapter 19)"), ("한인회장", "the president of a Korean association (mine)")]
_HOE_EX = [("동호회", "a club (the book’s example in the Core Vocabulary)"), ("동창회", "an alumni association (mine)"), ("산악회", "a mountaineering club (mine)"), ("학회", "an academic society (mine)")]
L1 = lesson(
    "Ch 17 · What the chapter teaches and the Sino-Korean syllable 회",
    "문화생활 · 취미 · 회 (會) · 음악회 · 전시회 · 회의",
    requires=[],
    cards=[
        card("What Chapter 17 teaches (문화생활)",
             "Chapter 17, “Cultural Life”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify Koreans’ common interests and hobbies; exchange information about personal interests and hobbies; extract and talk about basic information found on posters about cultural events and movies; give simple instructions for purchasing tickets of cultural events; and elicit information at the box office for a movie.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the gerund or verbal ending that is used as a noun; 르 irregular verbs; the attributive form + 것 같다 (looks like …; it seems that …); and the Sino-Korean syllable 회 (會)."),
        card("Sino-Korean in use: 회 (會)",
             "This Sino-Korean syllable means meeting or gathering, as in 회사 (a company; “meeting and gathering”), 회의 (a conference; a meeting; “meeting and discussion”), 전시회 (exhibition; “display gathering”), and 교회 (church; “[religious] teaching gathering”). The book asks you to guess the meaning of 음악회, 회의실, 회비, 회사원, 회원 and 한인회장; the answers below are the book’s meanings where the Core Vocabulary gives them and mine otherwise.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _HOE], say=[0])]),
        card("More words with 회 (the book’s Core Vocabulary)",
             "In the Core Vocabulary the book lists ~회 (會) as a gathering; a meeting; a convention; a party, with the examples 동호회, 동창회, 산악회 and 학회.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _HOE_EX], say=[0])]),
        card("Vocabulary Builder, Activity 4: a model sentence",
             "In the book’s “Find your match” activity you receive a word strip, find a classmate whose word best matches yours, and make a sentence with the two words. The book’s model: the words 정보 and 검색하다 give the sentence 인터넷에서 정보를 검색합니다. (I search for information on the internet. The English is mine.)",
             examples=[D("인터넷에서 정보를 검색합니다.", "I search for information on the internet.")]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1–3 (SMART Board activities) and the class steps of Activity 4 (word strips, sentences posted on the classroom wall and corrected in another color) are picture, game or class activities."),
    ],
    exercises=uniq(
        _tr(_HOE + _HOE_EX)
        + [M(f"Which word means “{b.split(';')[0].replace(' (mine)', '')}”?", a, [x for x, _ in (_HOE + _HOE_EX) if x != a][:3], f"{a}: {b}.") for a, b in (_HOE[:3] + _HOE[4:6])]
        + [M("What does the Sino-Korean syllable 회 (會) mean?", "meeting; gathering", ["not; no", "sea", "a type"], "회사, 회의, 전시회, 교회."),
           M("What does 전시회 literally mean?", "“display gathering”", ["“music meeting”", "“meeting member”", "“meeting fee”"], "전시회 = an exhibition; “display gathering”."),
           M("What does 회사 literally mean?", "“meeting and gathering”", ["“music meeting”", "“display gathering”", "“meeting fee”"], "회사 = a company."),
           M("Which word has 회 meaning a gathering for music?", "음악회", ["회사원", "회비", "회의실"], "음악회 = a concert; “music meeting”."),
           M("How do you say “I search for information on the internet”?", "인터넷에서 정보를 검색합니다.", ["인터넷에서 정보를 선택합니다.", "인터넷에서 정보를 결제합니다.", "인터넷에서 정보를 판매합니다."], "검색하다 = to search."),
           read_q("음악회"), read_q("전시회"), read_q("회의실"), read_q("한인회장"), read_q("인터넷에서 정보를 검색합니다")]
    ),
)

# ================================================================== Topic A
_A_DLG = [
    ("데이비드", "태희 씨는 시간이 날 때 보통 뭐 해요?", "Taehee, what do you usually do when you have free time?"),
    ("태희", "저는 악기 연주가 취미예요. 피아노하고 바이올린을 연주해요. 데이비드 씨는 취미가 뭐예요?", "My hobby is playing musical instruments. I play the piano and the violin. David, what is your hobby?"),
    ("데이비드", "저는 암벽등반하고 헬스를 좋아해요. 그런데 한국 사람들은 주로 무슨 취미활동을 해요?", "I like rock climbing and working out. By the way, what hobby activities do Koreans mainly do?"),
    ("태희", "한국 사람들은 보통 등산과 독서를 많이 해요. 그리고 젊은 사람들은 인터넷이나 컴퓨터 게임을 좋아해요.", "Koreans usually do a lot of hiking and reading. And young people like the internet and computer games."),
    ("데이비드", "그래요? 우리 미국 사람들은 다양한 레저와 스포츠를 즐겨요. 한국 사람들은 어떤 레저 활동을 좋아해요?", "Is that so? We Americans enjoy a variety of leisure activities and sports. What kind of leisure activities do Koreans like?"),
    ("태희", f"보통 {sino(10)} 대나 {sino(20)} 대는 운동이나 헬스를 많이 해요. 그리고 {sino(30)} 대 이상은 등산이나 낚시를 좋아해요.", "Usually people in their 10s or 20s do a lot of sports or working out. And people in their 30s and above like hiking or fishing."),
    ("데이비드", "그렇군요. 그럼, 태희 씨도 운동 좋아해요?", "I see. Then, Taehee, do you like sports, too?"),
    ("태희", "아니요. 저는 운동을 별로 안 좋아해요. 저는 음악회나 연극 관람을 더 좋아해요.", "No. I don’t like sports very much. I like going to concerts and watching plays more."),
]
_A_WORDS = ["게임", "관람", "낚시", "다양", "~대/세대", "레저", "뮤지컬", "바이올린", "스포츠", "시간이 나다", "악기", "암벽등반", "연극", "연주", "음악회", "~ 이상", "인터넷", "조사", "주로", "즐기다", "초대권", "피아노", "활동", "헬스"]
L2 = lesson(
    "Ch 17 · Topic A: What do Koreans do in their spare time?",
    "한국 사람들은 시간이 날 때 뭐 해요? · 취미 · 레저 · 스포츠 · 음악회",
    requires=[],
    cards=[
        card("Topic A: What do Koreans do in their spare time? (한국 사람들은 시간이 날 때 뭐 해요?)",
             "David and Taehee are talking about hobbies and leisure activities that Koreans enjoy most. (The English is mine; the book gives none. The book writes 10대, 20대 and 30대; they are spelled out here.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Cultural notes",
             "Before the 1990s, Koreans spent most of their time working and rarely enjoyed hobbies or leisure activities. Since the 1990s, however, Koreans have enjoyed an increase in income and free time and have come to prize their quality of living. Therefore, the percentage of Koreans enjoying various outdoor and indoor leisure activities, such as climbing, fishing, golfing, or watching movies, has been increasing."),
        card("Activities left out",
             "The SMART Board activities, the cue cards of the Presentation Activity (groups and partners) and Follow-up 2 (listening to three segments of a report on Koreans’ favorite hobbies by gender and generation, and filling in a table) are audio, computer, partner or class activities. Follow-up 1 is in the next lesson. The Useful Link (Gallup Korea) is a website."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not w.startswith(("~", "-"))]))
        + _tr(_strip(_A_DLG))
        + [M("What is Taehee’s hobby?", "Playing musical instruments", ["Rock climbing", "Fishing", "Watching movies"], "악기 연주가 취미예요."), M("Which instruments does Taehee play?", "The piano and the violin", ["The guitar and the drums", "Only the piano", "The flute and the violin"], "피아노하고 바이올린을 연주해요."),
           M("What does David like?", "Rock climbing and working out", ["Hiking and reading", "Fishing and the internet", "Concerts and plays"], "암벽등반하고 헬스를 좋아해요."), M("What do Koreans usually do a lot of?", "Hiking and reading", ["Rock climbing and working out", "Fishing and golf", "Concerts and plays"], "등산과 독서를 많이 해요."),
           M("What do young Koreans like?", "The internet and computer games", ["Hiking and fishing", "Concerts and plays", "Reading"], "젊은 사람들은 인터넷이나 컴퓨터 게임을 좋아해요."), M("What do Americans enjoy, according to David?", "A variety of leisure activities and sports", ["Only sports", "Only reading", "Only music"], "다양한 레저와 스포츠를 즐겨요."),
           M("Who does a lot of sports or working out?", "People in their 10s or 20s", ["People in their 30s and above", "Children", "Everybody"], "십 대나 이십 대는 운동이나 헬스를 많이 해요."), M("Who likes hiking or fishing?", "People in their 30s and above", ["People in their 10s or 20s", "Children", "Nobody"], "삼십 대 이상은 등산이나 낚시를 좋아해요."),
           M("Does Taehee like sports?", "No, not very much", ["Yes, very much", "Yes, a little", "She does not say"], "운동을 별로 안 좋아해요."), M("What does Taehee like more?", "Concerts and watching plays", ["Sports", "Working out", "Fishing"], "음악회나 연극 관람을 더 좋아해요."),
           F("태희 씨는 시간이 ___ 때 보통 뭐 해요? (when you have free time)", "날", ["올", "갈"], "시간이 나다 = to have free time."), F("저는 악기 ___가 취미예요. (playing an instrument)", "연주", ["관람", "조사"], "연주 = a musical performance."), F("한국 사람들은 보통 등산과 독서를 많이 ___. (do)", "해요", ["가요", "봐요"], "하다 = to do."),
           F("우리는 다양한 레저와 스포츠를 ___. (enjoy)", "즐겨요", ["싫어요", "관람해요"], "즐기다 = to enjoy."), F("보통 십 대나 이십 대는 운동을 많이 해요. 삼십 대 ___은 등산이나 낚시를 좋아해요. (and above)", "이상", ["이하", "미만"], "이상 = and above."), F("저는 음악회나 연극 ___을 더 좋아해요. (viewing)", "관람", ["조사", "판매"], "관람 = viewing."),
           M("What does ~대 (as in 이십 대) mean?", "~ generation; people in their ~s", ["a counter for months", "a round", "a ticket"], "이십 대 = people in their 20s."),
           read_q("취미활동"), read_q("암벽등반"), read_q("연극 관람"), read_q("음악회"), read_q("시간이 날 때")]
    ),
)

# ================================================================== Activities A
_SURVEY = [
    ("한국인이 좋아하는 취미", "Hobbies Koreans like"),
    (f"한국갤럽이 오월 구일부터 이십오일까지 전국 만 {sino(13)} 세 이상 남녀 천칠백 명에게 가장 좋아하는 취미를 물은 결과 ‘등산’ (구 퍼센트)이 가장 많았고, 그다음은 ‘음악감상’ (팔점삼 퍼센트)이었습니다.", "Gallup Korea asked 1,700 men and women nationwide aged 13 and over (full years) from May 9 to 25 about the hobby they like most, and ‘hiking’ (9.0%) was the most common, followed by ‘listening to music’ (8.3%)."),
    ("또 ‘운동·헬스’ (칠점팔 퍼센트)와 ‘게임’ (오점사 퍼센트)도 즐기는 것으로 조사되었습니다.", "It was also found that people enjoy ‘sports and working out’ (7.8%) and ‘games’ (5.4%)."),
    ("그리고 오점이 퍼센트는 ‘독서’, 사점오 퍼센트는 ‘영화감상’을 하는 것으로 나타났습니다.", "And 5.2% do ‘reading’ and 4.5% do ‘watching movies’."),
    ("‘낚시’ (사점일 퍼센트), ‘여행’ (삼점칠 퍼센트), ‘축구’ (이점구 퍼센트)도 인기있는 취미활동으로 조사되었습니다.", "‘Fishing’ (4.1%), ‘travel’ (3.7%) and ‘soccer’ (2.9%) were also found to be popular hobby activities."),
]
_GRAPH = [["등산", "Hiking", "9.0"], ["음악감상", "Listening to music", "8.3"], ["운동·헬스", "Sports and working out", "7.8"], ["게임", "Computer gaming", "5.4"], ["독서", "Reading", "5.2"], ["영화감상", "Watching movies", "4.5"], ["낚시", "Fishing", "4.1"], ["여행", "Travel", "3.7"], ["축구", "Soccer", "2.9"]]
_QS = [("십 대 남자들이 가장 좋아하는 취미가 무엇입니까?", "What hobby do men in their 10s like most?"), (f"이십 대 남자들의 구점사 퍼센트가 좋아하는 취미가 뭐예요?", "What hobby do 9.4% of men in their 20s like?"), ("삼십 대 남자들이 두 번째로 좋아하는 취미가 무엇입니까?", "What hobby do men in their 30s like second most?")]
L3 = lesson(
    "Ch 17 · Activities A: a survey of Koreans’ favorite hobbies",
    "한국갤럽 · 등산 · 음악감상 · 운동·헬스 · 게임 · 독서 · 영화감상",
    requires=[],
    cards=[
        card("Topic A, Follow-up 1 (Reading): an excerpt from a survey report",
             "The book gives an excerpt from a survey report by Gallup Korea and asks you to complete a bar graph by providing the missing information. The text is the book’s (the date, the figures and the 13세 are spelled out in Hangul; the decimal point is read 점); the English is mine.",
             examples=passage(_SURVEY)),
        card("The graph filled in (mine)",
             "The graph itself is a picture and is left out; the book leaves its blanks empty, and these are my answers (the percentages are the text’s).",
             tables=[table(["Hobby (Korean)", "Hobby (English)", "%"], _GRAPH, say=[0])]),
        card("Activities, Activity 2: sample questions",
             "In the book each partner has an incomplete table of the hobbies Korean men enjoy most, and you ask each other questions to complete it. The book’s sample questions (digits spelled out; the English is mine):",
             examples=passage(_QS)),
        card("Activities left out",
             "Activity 1 (a SMART Board activity), the partner tables of Activity 2, Activity 3 (listening to three conversations about hobbies and filling in the hobby, the event, the day and the time) and Activity 4 (partners read passage A or B about the hobbies of Sungsoo’s and Hyojin’s families, exchange information and present; the two passages are handed out by the teacher and are not printed in the book) are audio, computer, partner or class activities."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b in _SURVEY[1:]] + _QS)
        + [M(f"What is the hobby “{b}” in Korean?", a, [x for x, _, _ in _GRAPH if x != a][:3], f"{a} = {b}.") for a, b, c in _GRAPH]
        + [M(f"What does {a} mean?", b, [y for _, y, _ in _GRAPH if y != b][:3], f"{a} means “{b}”.") for a, b, c in _GRAPH]
        + [M("Which hobby did most Koreans choose?", "Hiking", ["Listening to music", "Reading", "Fishing"], "등산 (9.0%) was the most common."), M("Which hobby came second?", "Listening to music", ["Hiking", "Computer gaming", "Soccer"], "음악감상 (8.3%)."),
           M("What percentage of Koreans like reading?", "5.2%", ["9.0%", "4.5%", "7.8%"], "독서 5.2%."), M("What percentage of Koreans like watching movies?", "4.5%", ["5.2%", "4.1%", "3.7%"], "영화감상 4.5%."),
           M("Who made the survey?", "Gallup Korea", ["A university", "The army", "A newspaper"], "한국갤럽."), M("How old were the people asked?", "13 and over", ["20 and over", "Under 13", "30 and over"], "만 십삼 세 이상."),
           F("한국갤럽이 취미를 ___ 결과 등산이 가장 많았습니다. (asked)", "물은", ["먹은", "산"], "묻다 → 물은 = asked."), F("‘낚시’, ‘여행’, ‘축구’도 인기있는 취미활동으로 ___되었습니다. (surveyed)", "조사", ["관람", "연주"], "조사되다 = to be surveyed."),
           F("한국 사람들이 가장 좋아하는 취미는 ___입니다. (hiking)", "등산", ["독서", "낚시"], "등산 = hiking."),
           read_q("한국인이 좋아하는 취미"), read_q("한국갤럽"), read_q("영화감상"), read_q("음악감상"), read_q("등산 독서")]
    ),
)

# ================================================================== Topic B
_B_AD = [
    ("발레 공연 안내", "Information about a ballet performance"),
    ("로미오와 줄리엣", "Romeo and Juliet"),
    (f"공연 날짜: {month_ko(2)} {day_ko(20)}부터 {day_ko(21)}까지", "Performance dates: February 20 to February 21 (the book writes 2.20~2.21)"),
    (f"공연 시간: 오후 세 시 반, 오후 일곱 시 반", "Performance times: 3:30 p.m. and 7:30 p.m. (the book writes 15:30 & 19:30)"),
    ("공연 장소: 엘지아트센터", "Performance place: LG Art Center"),
    (f"티켓 가격: 알석 {_kn(90000)} 원, 에스석 {_kn(70000)} 원, 일반석 {_kn(50000)} 원", "Ticket price: R seats 90,000 won, S seats 70,000 won, general admission 50,000 won"),
    (f"관람 연령: {sino(6)} 세 이상", "Viewing age: 6 years old and above"),
    ("위 공연에 관심이 있으시면 인터넷으로 예매하시기 바랍니다.", "If you are interested in the performance above, please book on the internet."),
    ("예매 방법", "How to book"),
    ("엘지아트센터 인터넷 홈페이지에서 원하시는 공연을 검색합니다.", "1. Search for the performance you want on the LG Art Center’s internet home page."),
    ("공연 날짜, 시간, 좌석을 선택합니다.", "2. Choose the performance date, time and seat."),
    ("“예매하기” 버튼을 누릅니다.", "3. Press the “Book” button."),
    ("개인 정보를 써 넣은 후 신용카드로 결제합니다.", "4. After you fill in your personal information, pay by credit card."),
]
_B_WORDS = ["~개월", "개인", "검색", "결제", "공연", "관심", "누르다", "무용", "미술", "발레", "방법", "버튼", "선택", "연령", "예매", "일반석", "전시회", "정보", "주소", "티켓", "행사", "홈페이지"]
_B_MATCH = [("발레", "ballet"), ("관심", "concern; interest"), ("무용", "a dance; dancing"), ("예매", "booking; advance purchase"), ("티켓", "a ticket"), ("검색", "search"), ("일반석", "a general admission seat"), ("버튼", "a button"), ("연령", "age"), ("누르다", "to press; to click"),
            ("~개월", "a counter for months"), ("개인", "an individual"), ("~ 이상", "~ and above"), ("정보", "information"), ("홈페이지", "a home page"), ("주소", "an address"), ("공연", "a performance"), ("행사", "an event"), ("선택", "selection; choice"), ("전시회", "an exhibition"), ("미술", "art; fine arts")]
_BOOK = [("먼저, 홈페이지에서 로그인하세요.", "First, log in on the home page."), ("원하시는 공연과 공연 날짜, 시간, 좌석을 선택하세요.", "Choose the performance you want and the performance date, time and seat."),
         ("결제 방법이 나오면 신용카드 버튼을 누르세요.", "When you see the payment methods, press the credit card button. (The book’s own English for this step: “Click credit card button when you see Payment Method”.)"), ("공연장에서 티켓을 받으세요.", "Receive your ticket at the theater.")]
L4 = lesson(
    "Ch 17 · Topic B: A ballet performance",
    "발레 공연 · 예매 방법 · 공연 날짜 · 티켓 가격 · 신용카드로 결제합니다",
    requires=[],
    cards=[
        card("Topic B: A ballet performance (발레 공연)",
             "The book shows a ballet performance poster with simple instructions for purchasing tickets on the internet. The text is the book’s (dates, times, prices and the age are spelled out in Hangul; the book’s R and S seats are read 알석 and 에스석, LG is read 엘지; the telephone number and the web address are left out); the English is mine.",
             examples=passage(_B_AD)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened.",
             tables=[ktable(_rows([w for w in _B_WORDS]))]),
        card("Presentation Activity: the vocabulary table filled in",
             "The book’s table gives a Korean word or an English meaning in each row and asks you to fill in the other half. The words of the table with their meanings (the meanings are the book’s; the last cell of the book’s table, “finally”, has no Korean word in the book; the word 마지막으로, used in Activity 2 of the chapter, is mine).",
             tables=[ktable(_B_MATCH + [("마지막으로", "finally (mine)")])]),
        card("Follow-up 1 (Reading): the steps for booking a ticket",
             "The book shows a booking page of a website (“Joeun Performance”) with four steps for booking a musical ticket and asks you to translate each step into English; step 3 is done for you. The page is an image; the steps are read from it. The English is mine (except step 3, where the book’s own words are given).",
             examples=passage(_BOOK)),
        card("Activities left out",
             "The SMART Board activities, the pair reading of the converted dialog, Follow-up 2 (listening to two telephone conversations at a ticket reservation office, writing the type of event, the viewing age and the ticket price in English) and the Useful Links (Ticketlink, YES24 Performance) are audio, computer, partner or website activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not w.startswith(("~", "-"))]))
        + _tr([(a, b) for a, b in _B_AD[:2]] + _B_AD[2:] + _BOOK)
        + [M("What is the title of the ballet?", "Romeo and Juliet", ["Swan Lake", "Cats", "The Nutcracker"], "로미오와 줄리엣."), M("How much is a general admission seat?", "50,000 won", ["90,000 won", "70,000 won", "5,000 won"], "일반석 오만 원."),
           M("How much is an R seat?", "90,000 won", ["70,000 won", "50,000 won", "9,000 won"], "알석 구만 원."), M("How much is an S seat?", "70,000 won", ["90,000 won", "50,000 won", "7,000 won"], "에스석 칠만 원."),
           M("What is the viewing age?", "6 years old and above", ["12 years old and above", "Adults only", "Any age"], "육 세 이상."), M("How can you book the tickets?", "On the internet", ["By mail", "Only at the theater", "By fax"], "인터넷으로 예매하시기 바랍니다."),
           M("What do you do after you press the “Book” button?", "Fill in personal information and pay by credit card", ["Receive the ticket", "Choose the seat", "Search for the performance"], "개인 정보를 써 넣은 후 신용카드로 결제합니다."), M("What is the first step of booking?", "Search for the performance you want", ["Pay by credit card", "Choose the seat", "Press the button"], "원하시는 공연을 검색합니다."),
           M("Where do you receive the ticket (in the booking page)?", "At the theater", ["At home", "At a bank", "At the post office"], "공연장에서 티켓을 받으세요."),
           F("위 공연에 ___이 있으시면 인터넷으로 예매하시기 바랍니다. (interest)", "관심", ["연령", "주소"], "관심 = interest."), F("공연 날짜, 시간, 좌석을 ___합니다. (choose)", "선택", ["검색", "결제"], "선택하다 = to choose."), F("“예매하기” 버튼을 ___. (press)", "누릅니다", ["검색합니다", "결제합니다"], "누르다 = to press."),
           F("개인 정보를 써 넣은 후 신용카드로 ___합니다. (pay)", "결제", ["선택", "검색"], "결제하다 = to pay."), F("인터넷 홈페이지에서 공연을 ___합니다. (search)", "검색", ["결제", "선택"], "검색하다 = to search."), F("이 전시회는 관람 ___이 육 세 이상입니다. (age)", "연령", ["정보", "주소"], "연령 = age."),
           read_q("발레 공연 안내"), read_q("예매 방법"), read_q("로미오와 줄리엣"), read_q("신용카드로 결제합니다"), read_q("공연 날짜")]
    ),
)

# ================================================================== Activities B
_TICKET = [
    ("먼저, 관람하고 싶은 공연을 고르세요.", "First, choose the performance you want to see."),
    ("그리고, 그 공연의 홈페이지로 들어가세요.", "Then, go to the home page of that performance."),
    ("그 홈페이지에서 회원 가입을 합니다.", "Sign up for membership on that home page."),
    ("그 후, 보고 싶은 공연을 누릅니다.", "After that, press the performance you want to see."),
    ("그다음에, 앉고 싶은 자리를 선택하세요.", "Next, choose the seat you want to sit in."),
    ("그리고, 필요한 티켓의 숫자를 씁니다.", "Then, write the number of tickets you need."),
    ("마지막으로, 개인 정보를 써 넣은 후 신용카드로 돈을 내세요.", "Finally, after you fill in your personal information, pay with a credit card."),
]
_TICKET_ORDER = [("Sign up for membership on the home page.", 3), ("Choose the performance you want to see.", 1), ("Go to the home page of the performance.", 2), ("Choose the seat.", 5), ("Press (the button for) the performance you would like to see.", 4), ("Input the number of tickets you need.", 6), ("Pay with a credit card after you fill out the form for your personal information.", 7)]
_TK_W = [("로그인", "logging in (mine)"), ("좌석", "a seat (mine)"), ("자리", "a seat; a place (mine)"), ("숫자", "a number (mine)"), ("회원 가입", "membership sign-up (mine)"), ("공연장", "a theater; a performance hall (mine)"), ("그다음에", "next; after that (mine)"), ("마지막으로", "finally (mine)")]
L5 = lesson(
    "Ch 17 · Activities B: how to buy a ticket online",
    "먼저 · 그리고 · 그 후 · 그다음에 · 마지막으로 · 회원 가입 · 신용카드로 돈을 내세요",
    requires=[],
    cards=[
        card("Topic B, Activities, Activity 2 (Reading): instructions for buying a ticket online",
             "The book gives seven sentences of instructions for buying a ticket online and asks you to match each with its English translation by writing the number of each sentence; the last one is done for you. The sentences are the book’s; the English is mine.",
             examples=passage(_TICKET)),
        card("The matching (mine)",
             "The book gives the seven English sentences and a blank for each number; step 7 is done in the book. These are the numbers (the first one is the book’s; the others are my answers).",
             tables=[table(["English sentence (the book)", "Sentence number"], [[a, str(n)] for a, n in _TICKET_ORDER])]),
        card("Words of the instructions",
             "These meanings are mine (the book does not gloss them).",
             tables=[ktable(_TK_W)]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity), Activity 3 (listening to three announcements about cultural events and filling in the place, the event, the period of performance, the viewing age and the promotion in English) and Activity 4 (partners get different performance information cards, exchange it in Korean, negotiate which performance to see and report to the class) are audio, computer, partner or class activities."),
    ],
    exercises=uniq(
        _tr(_TICKET + _TK_W)
        + [M(f"Which step number is “{b.rstrip('.')}”?", str(n), [str(x) for x in (1, 2, 3, 4, 5, 6, 7) if x != n][:3], f"Step {n}: {b}") for b, n in _TICKET_ORDER]
        + [M("What do you do first when you buy a ticket online?", "Choose the performance you want to see", ["Pay by credit card", "Choose the seat", "Sign up for membership"], "먼저, 관람하고 싶은 공연을 고르세요."), M("What do you do last?", "Pay with a credit card", ["Choose the seat", "Press the performance", "Write the number of tickets"], "마지막으로, 개인 정보를 써 넣은 후 신용카드로 돈을 내세요."),
           M("What do you do on the home page?", "Sign up for membership", ["Pay", "Choose a seat", "Receive the ticket"], "그 홈페이지에서 회원 가입을 합니다."), M("What do you write after you choose the seat?", "The number of tickets", ["Your address", "Your phone number", "Nothing"], "필요한 티켓의 숫자를 씁니다."),
           F("먼저, 관람하고 싶은 공연을 ___. (choose)", "고르세요", ["누르세요", "내세요"], "고르다 = to choose."), F("그 홈페이지에서 회원 가입을 ___. (do)", "합니다", ["갑니다", "봅니다"], "가입을 하다 = to sign up."), F("앉고 싶은 자리를 ___하세요. (choose)", "선택", ["검색", "결제"], "선택하다 = to choose."),
           F("신용카드로 돈을 ___. (pay)", "내세요", ["누르세요", "고르세요"], "돈을 내다 = to pay money."), F("___, 개인 정보를 써 넣은 후 신용카드로 돈을 내세요. (finally)", "마지막으로", ["먼저", "그 후"], "마지막으로 = finally."), F("___, 보고 싶은 공연을 누릅니다. (after that)", "그 후", ["먼저", "마지막으로"], "그 후 = after that."),
           read_q("회원 가입"), read_q("마지막으로"), read_q("그다음에"), read_q("티켓의 숫자"), read_q("신용카드로 돈을 내세요")]
    ),
)

# ================================================================== Grammar A: gerund -는 것 / -기
def _ger(phrase):
    """'학교에 가다' -> ('학교에 가는 것', '학교에 가기')"""
    w = phrase.split(" ")
    v = w[-1]
    return " ".join(w[:-1] + [attr(v)[0] + " 것"]), " ".join(w[:-1] + [stem(v) + "기"])


_GER_A = [("학교에 가다", "going to school"), ("티브이를 보다", "watching TV"), ("햄버거를 먹다", "eating a hamburger"), ("창문을 열다", "opening the window"), ("서울에서 쇼핑하다", "shopping in Seoul"), ("한국에서 운전하다", "driving in Korea")]
_GER_B = [("도서관에서 공부하다", "studying in the library"), ("돈을 주다", "giving money"), ("소포를 부치다", "mailing a package"), ("문을 닫다", "closing the door"), ("친구에게 전화하다", "calling a friend"), ("티켓을 예매하다", "booking a ticket")]
_GER_EX = [("한국말을 가르치는 것이 쉬워요.", "Teaching Korean is easy. (subject)"), ("한국말 가르치기가 쉬워요.", "Teaching Korean is easy. (the book writes 한국말(을); the marker can be left out)"),
           ("한국말을 공부하는 것을 좋아해요.", "I like studying Korean. (object)"), ("한국말 공부하기를 좋아해요.", "I like studying Korean. (the book writes 한국말(을))"),
           ("내 취미는 먹는 것입니다.", "My hobby is eating. (subject complement)"), ("내 취미는 먹기입니다.", "My hobby is eating. (subject complement)")]
_GER_RULE = [("저는 영화 보는 것을 좋아합니다.", "I like watching movies."), ("밤에 운전하는 것이 어려웠어요.", "Driving at night was difficult."), ("한국말은 읽기와 쓰기가 쉬워요.", "As for Korean, reading and writing is easy.")]
_TODO = [("부모님께 전화하기", "Call (my) parents"), ("도서관에 책 돌려주기", "Return a book to the library"), ("병원 예약하기", "Make a hospital appointment")]
_HOBBY = ["영화 보다", "책 읽다", "미술 전시회 가다", "암벽등반하다", "문화 행사 가다", "낚시하다", "연극 보다", "여행 가다", "음악 감상하다", "연주회 가다"]
_HOBBY_EN = ["watching movies", "reading books", "going to art exhibitions", "rock climbing", "going to cultural events", "fishing", "watching plays", "traveling", "listening to music", "going to concerts"]
_HOB_MODEL = [("김 일병은 영화 보는 것을 좋아해요?", "Private Kim, do you like watching movies?"), ("네, 영화 보는 것을 좋아해요.", "Yes, I like watching movies."), ("아니요, 영화 보는 것을 안 좋아해요.", "No, I don’t like watching movies."),
              ("김 일병은 영화 보기, 책 읽기, 암벽 등반하기, 낚시하기를 좋아합니다. 하지만 미술 전시회 가기, 연극 보기, 여행 가기는 좋아하지 않습니다.", "Private Kim likes watching movies, reading books, rock climbing and fishing. But he does not like going to art exhibitions, watching plays or traveling.")]
L6 = lesson(
    "Ch 17 · Grammar A: the gerund with -는 것 and -기",
    "한국말을 가르치는 것 · 영화 보기 · 책 읽기 · 취미는 먹는 것입니다",
    requires=[],
    cards=[
        card("Expressing a gerund",
             "In English, the gerund refers to the usage of a verb or verbal phrase (in its -ing form) as a noun: “Teaching Korean is fun” (subject), “Mr. Kim enjoys teaching Korean” (object), “My job is teaching Korean” (subject complement). Nouns function as subjects, objects and subject complements, and the verbal phrase functions as a noun in these sentences.\n\n"
             "In Korean, a verb or verbal phrase functions as a gerund when -는 것 or -기 is added to the stem of a verb. In a nutshell, -는 것 and -기 are the Korean equivalents of the English -ing. In the gerund that ends in -기, the object marker is deletable. This is because the gerund with -기 has more noun-like characteristics than the one with -는 것, just as “boar hunting” has more noun-like characteristics than “hunting boars” in English.",
             examples=passage(_GER_EX)),
        card("The rule",
             "verb stem + 는 것 (or 기).",
             tables=[table(["Condition", "Rule", "Example"], [["When a verb is an action verb", "add 는 것 or 기", "영화 보다 → 영화 보는 것 or 영화 보기; 읽다 → 읽는 것 or 읽기"]])],
             examples=passage(_GER_RULE)),
        card("Forms (mine)",
             "The forms below are made by the book’s rule (the book’s Follow-up 1 lists, 보기: 한국음식을 요리하다 → 한국음식을 요리하는 것; 한국음식 요리하기). The book writes TV; it is read 티브이 here.",
             tables=[table(["Phrase", "-는 것", "-기", "Meaning (mine)"], [[p, *_ger(p), m] for p, m in _GER_A + _GER_B], say=[0, 1, 2])]),
        card("Follow-up 2: Sungho’s “To Do” list (오늘 할 일)",
             "The book gives three items of Sungho’s “To Do” list and asks you to translate them; two more items come from a voice mail (audio). The items are the book’s; the English is mine.",
             examples=passage(_TODO)),
        card("Follow-up 5: favorite activities",
             "The book gives a table of ten hobbies and leisure activities, and you interview classmates (O or X). The ten activities are given here in the -는 것 form (mine) with the -기 form; the book’s models follow (the English is mine).",
             tables=[table(["Activity", "-는 것", "-기", "Meaning (mine)"], [[p, *_ger(p), m] for p, m in zip(_HOBBY, _HOBBY_EN)], say=[1, 2])],
             examples=passage(_HOB_MODEL)),
        card("Activities left out",
             "Follow-up 1 (partners read phrases from List A or B and conjugate them; the phrases are given above), Follow-up 2 (b) (a voice mail from Sungho’s older sister, audio), Follow-up 5 (interviews of classmates and a class presentation) are audio, partner or class activities."),
    ],
    exercises=uniq(
        [M(f"What is the -는 것 form of {p}?", _ger(p)[0], [_ger(p)[1], " ".join(p.split(" ")[:-1] + [attr(p.split(" ")[-1])[1] + " 것"]), " ".join(p.split(" ")[:-1] + [attr(p.split(" ")[-1])[2] + " 것"])], f"{p}: action verb stem + 는 것 → {_ger(p)[0]}.") for p, m in _GER_A + _GER_B]
        + [M(f"What is the -기 form of {p}?", _ger(p)[1], [_ger(p)[0], " ".join(p.split(" ")[:-1] + [stem(p.split(" ")[-1]) + "는기"]), " ".join(p.split(" ")[:-1] + [stem(p.split(" ")[-1]) + "기는"])], f"{p}: stem + 기 → {_ger(p)[1]}.") for p, m in _GER_A + _GER_B]
        + _tr(_GER_EX + _GER_RULE + _TODO + _HOB_MODEL)
        + [M(f"What does {_ger(p)[0]} mean?", m, [y for _, y in _GER_A + _GER_B if y != m][:3], f"{_ger(p)[0]} = {m}.") for p, m in _GER_A + _GER_B[:3]]
        + [F("내 취미는 먹___입니다. (my hobby is eating)", "는 것", ["기는", "을 것"], "먹다 + 는 것 = 먹는 것."), F("저는 영화 보___ 좋아합니다. (I like watching movies)", "는 것을", ["는 것은", "기가"], "Object: 는 것을 (or 기를)."), F("밤에 운전하는 ___ 어려웠어요. (driving at night was difficult)", "것이", ["것을", "것에"], "Subject: 것이."),
           F("한국말은 읽___ 쓰기가 쉬워요. (reading and writing)", "기와", ["는 것과", "기를"], "읽기와 쓰기 = reading and writing."), F("저는 한국말 공부하___를 좋아해요. (studying Korean)", "기", ["는 것", "는"], "공부하다 + 기 = 공부하기."),
           M("Which gerund can drop the object marker?", "The one with -기", ["The one with -는 것", "Both of them", "Neither of them"], "-기 has more noun-like characteristics."), M("What are -는 것 and -기 the Korean equivalents of?", "The English -ing (gerund)", ["The English -ed", "The English to-infinitive", "The English -ly"], "They make a verb phrase work as a noun."),
           M("Which sentence has a gerund as a subject complement?", "내 취미는 먹는 것입니다.", ["한국말을 가르치는 것이 쉬워요.", "저는 영화 보는 것을 좋아합니다.", "밤에 운전하는 것이 어려웠어요."], "취미는 먹는 것입니다 = my hobby is eating."),
           read_q("영화 보는 것"), read_q("책 읽기"), read_q("한국말을 가르치는 것"), read_q("암벽등반하기"), read_q("병원 예약하기")]
    ),
)

# ================================================================== Grammar B: 르 irregular verbs
def _reu(verb):
    """르 irregular: 모르다 -> (몰라요, 몰랐습니다, 모릅니다)"""
    st = stem(verb)
    assert st.endswith("르") and len(st) >= 2, verb
    l, v, t = _K.decompose(st[-2])
    assert not t, verb
    prev = _K.compose(l, v, "ㄹ")
    lah = v in ("ㅏ", "ㅗ")
    return (st[:-2] + prev + ("라" if lah else "러") + "요", st[:-2] + prev + ("랐" if lah else "렀") + "습니다", formal(verb))


_REU = [("고르다", "to choose"), ("누르다", "to press; to click"), ("다르다", "to be different"), ("모르다", "not to know"), ("부르다", "to sing / call"), ("빠르다", "to be fast"), ("자르다", "to cut"), ("머무르다", "to stay (mine)")]
_REU_PH = [("한국말을 모르다", "not to know Korean"), ("케이크를 자르다", "to cut a cake"), ("버튼을 누르다", "to press a button"), ("모양이 다르다", "the shape is different"), ("비행기가 빠르다", "the plane is fast"), ("컴퓨터를 고르다", "to choose a computer"), ("호텔에 머무르다", "to stay at a hotel"), ("노래를 부르다", "to sing a song")]
_REU_EX = [("제 친구는 노래를 잘 불러요.", "My friend sings (a song) well."), ("저는 수영할 줄 몰라요.", "I don’t know how to swim."), ("먹고 싶은 것을 골라 보세요.", "Please try choosing what you want to eat."), ("어제 머리를 잘랐습니다.", "I cut my hair yesterday. (literal translation) / I got a haircut yesterday. (standard translation)")]
_REU_STEPS = [["1", "Dictionary form", "모르다", "부르다"], ["2", "ㅡ is dropped from 르.", "모ㄹ", "부ㄹ"], ["3", "ㄹ moves to the bottom of the preceding syllable.", "몰", "불"],
              ["4", "라 or 러 is added. 라 is added if the preceding syllable has a vowel ㅏ or ㅗ. Otherwise, 러 is added.", "몰 + 라요", "불 + 러요"], ["5", "The ending 요 is added.", "몰라요", "불러요"]]
L7 = lesson(
    "Ch 17 · Grammar B: 르 irregular verbs",
    "모르다 → 몰라요 · 부르다 → 불러요 · 다르다 → 달라요 · 빠르다 → 빨라요 · 고르다 · 자르다 · 누르다",
    requires=[],
    cards=[
        card("르 irregular verbs",
             "So far you have learned quite a few verbs with stems ending in 르: 빠르다 (to be fast), 다르다 (to be different), 부르다 (to sing / call), 고르다 (to choose), 모르다 (not to know), 자르다 (to cut). These verbs are known as “르 irregular verbs” because they go through an extra step when their stem is followed by a vowel, such as -아/어요, -아/어 보다, or -았/었습니다.",
             tables=[table(["Step", "Rule", "Example 1", "Example 2"], _REU_STEPS)]),
        card("Examples",
             "The book’s examples:",
             examples=passage(_REU_EX)),
        card("Conjugation (mine)",
             "The book’s Follow-up 3 asks you to fill in -아/어요, -았/었습니다 and -ㅂ니다 for these verbs (some cells are given); all cells are filled here by the book’s rule. 머무르다 is the book’s ninth verb.",
             tables=[table(["Verb", "Meaning", "-아/어요", "-았/었습니다", "-ㅂ니다"], [[v, m, *_reu(v)] for v, m in _REU], say=[0, 2, 3, 4])]),
        card("Follow-up 3 (b): phrases",
             "Partners read the phrases of List A or List B and conjugate them (the book’s model: 노래를 부르다 → 노래를 불러요 / 노래를 불렀습니다 / 노래를 부릅니다). The forms are mine.",
             tables=[table(["Phrase", "-아/어요", "-았/었습니다", "-ㅂ니다", "Meaning (mine)"], [[p, *[" ".join(p.split(" ")[:-1] + [x]) for x in _reu(p.split(" ")[-1])], m] for p, m in _REU_PH], say=[0, 1, 2, 3])]),
        card("Follow-up 4 (a note)",
             "Follow-up 4 is a listening activity (four short dialogs; you write the dictionary form of the 르 irregular verbs and their English meanings). Follow-up 5 is an interview about hobbies and is in the previous lesson."),
    ],
    exercises=uniq(
        [M(f"What is the -아/어요 form of {v} ({m.replace(' (mine)', '')})?", _reu(v)[0], [stem(v) + "어요", stem(v)[:-1] + "러요" if _reu(v)[0].endswith("라요") else stem(v)[:-1] + "라요", stem(v) + "아요"], f"{v} → {_reu(v)[0]}.") for v, m in _REU]
        + [M(f"What is the -았/었습니다 form of {v}?", _reu(v)[1], [stem(v) + "었습니다", stem(v) + "았습니다", _reu(v)[1].replace("랐", "렀") if "랐" in _reu(v)[1] else _reu(v)[1].replace("렀", "랐")], f"{v} → {_reu(v)[1]}.") for v, m in _REU]
        + [M(f"What is the -ㅂ니다 form of {v}?", _reu(v)[2], [_reu(v)[0].replace("요", "습니다"), stem(v) + "습니다", _reu(v)[1]], f"{v} → {_reu(v)[2]}.") for v, m in _REU]
        + [M(f"What does {v} mean?", m.replace(" (mine)", ""), [y.replace(" (mine)", "") for _, y in _REU if y != m][:3], f"{v} means “{m.replace(' (mine)', '')}”.") for v, m in _REU]
        + _tr(_REU_EX + _REU_PH[:4])
        + [M("When is 라 added?", "When the preceding syllable has the vowel ㅏ or ㅗ", ["When the preceding syllable has the vowel ㅜ", "Always", "Never"], "몰라요 (ㅗ), 달라요 (ㅏ); otherwise 러: 불러요."), M("What happens to ㅡ of 르 in the informal style?", "It is dropped", ["It is doubled", "It becomes ㅜ", "Nothing"], "모르다 → 모ㄹ → 몰."),
           M("Where does ㄹ move?", "To the bottom of the preceding syllable", ["To the front of 르", "It is dropped", "It becomes ㄴ"], "모ㄹ → 몰."),
           F("저는 수영할 줄 ___. (I don’t know)", "몰라요", ["모르어요", "모려요"], "모르다 → 몰라요."), F("제 친구는 노래를 잘 ___. (sings)", "불러요", ["부라요", "부르어요"], "부르다 → 불러요."), F("어제 머리를 ___습니다. (I cut)", "잘랐", ["자르었", "잘렀"], "자르다: 자 has ㅏ → 잘랐습니다."),
           F("먹고 싶은 것을 ___ 보세요. (choose)", "골라", ["고라", "고르어"], "고르다 → 골라."), F("이 비행기는 아주 ___. (fast)", "빨라요", ["빠르어요", "빠러요"], "빠르다 → 빨라요."), F("두 모양이 ___. (different)", "달라요", ["다르어요", "다라요"], "다르다 → 달라요."),
           read_q("몰라요"), read_q("불러요"), read_q("달랐습니다"), read_q("눌렀습니다"), read_q("노래를 부릅니다")]
    ),
)

# ================================================================== Topic C
_C_DLG1 = [
    ("은비", "우진아, 우리 이번 토요일에 영화 보러 갈까?", "Woojin, shall we go to see a movie this Saturday?"),
    ("우진", "좋아. 뭐 좋은 영화 있어? 난 코미디 영화가 보고 싶은데...", "Sure. Is there any good movie? I want to see a comedy..."),
    ("은비", "음…요즘 재미있는 코미디 영화가 별로 없는 것 같아. 공포 영화는 어때?", "Um… it seems there aren’t many funny comedies these days. How about a horror movie?"),
    ("우진", "글쎄, 난 공포 영화는 무서워서 싫어.", "Well, I don’t like horror movies because they are scary."),
    ("은비", "그럼, 우리 액션 영화 보러 가자. 난 데이비드 리치 감독이 만든 ‘불릿 트레인’이 재미있을 것 같아.", "Then let’s go see an action movie. I think ‘Bullet Train’, made by the director David Leitch, will be fun."),
    ("우진", "어떤 배우가 주연이야?", "Which actor is the lead?"),
    ("은비", "브래드 피트가 주연이야.", "Brad Pitt is the lead."),
    ("우진", "그래? 그럼 그 영화 보러 가자. 그런데 어느 극장에서 상영해?", "Is that so? Then let’s go see that movie. By the way, at which theater is it showing?"),
    ("은비", "롯데시네마에서 해. 내가 표를 미리 살까?", "It’s at Lotte Cinema. Shall I buy the tickets in advance?"),
    ("우진", "아니야. 그냥 극장 앞에서 토요일 오전 열 시에 만나자.", "No. Let’s just meet in front of the theater at 10 a.m. on Saturday."),
]
_C_DLG2 = [
    ("우진", "저기, ‘불릿 트레인’ 열 시 반 조조할인 두 장 주세요.", "Excuse me, two tickets for the 10:30 matinee discount showing of ‘Bullet Train’, please."),
    ("매표소 직원", "손님, 죄송합니다. 관객이 많아서 첫 회는 방금 매진됐습니다.", "I’m sorry, customer. There were many people in the audience, so the first showing has just sold out."),
    ("우진", "아, 그래요? 그럼, 열두 시 반 표 두 장 주세요. 그런데, 학생 할인 돼요?", "Oh, is that so? Then two tickets for the 12:30 showing, please. By the way, can I get a student discount?"),
    ("매표소 직원", "네, 됩니다. 학생증 좀 보여주세요.", "Yes, you can. Please show me your student ID."),
    ("우진", "여기 있습니다.", "Here you are."),
]
_C_WORDS = ["감독", "곧", "공포", "관객", "극장", "매진", "무섭다", "미리", "방금", "배우", "상영", "싫다", "액션", "어느", "-(으)ㄴ/는/(으)ㄹ 것 같다", "제목", "조조할인", "주연", "코미디 / 코메디", "판매", "학생증", "~회 (round)"]
_SCHED = [["1관", "불릿 트레인", "R", "10:30", "곧 매진", "12:30", "판매 중"], ["2관", "스타워즈", "G", "11:00", "매진", "13:30", "판매 중"], ["3관", "할로윈", "R", "11:30", "74석", "14:00", "판매 중"]]
L8 = lesson(
    "Ch 17 · Topic C: Please give me two tickets for the 10:30 showing",
    "10시 반 표 두 장 주세요 · 영화 · 극장 · 매표소 · 조조할인 · 학생 할인",
    requires=[],
    cards=[
        card("Topic C, Part I: two friends talk about movies at a coffee shop (영화 보러 갈까?)",
             "Two friends are at a coffee shop and talking about movies. (The English is mine; the book gives none. The book writes 10시; it is spelled 열 시.)",
             examples=dlg(_C_DLG1)),
        card("Topic C, Part II: at the box office (매표소에서)",
             "Woojin and Eunbi are looking at the movie schedule and asking about buying tickets at the box office. (The English is mine. The book writes 10시 반 and 12시 반; they are spelled 열 시 반 and 열두 시 반.)",
             examples=dlg(_C_DLG2)),
        card("The movie schedule (상영 시간표)",
             "The book shows the schedule of three screens (columns: screen, movie title, rating, showing time, sales status, showing time, sales status). The ratings R and G are the book’s letters; 74석 means 74 seats are left. The words are Korean; the book gives no English.",
             tables=[table(["Screen", "Movie title", "Rating", "Showing", "Status", "Showing", "Status"], _SCHED, say=[1])]),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Cultural notes: matinee discounts",
             "In the United States, an early afternoon movie is called a “matinee,” and the discounted tickets for these are called “matinee discounts.” In Korea, such discounts are called 조조할인, in which 조조 (早朝) means early morning. However, these discount prices are available only for the first showing of the day, whereas matinee discounts in the United States generally include all early afternoon showings.",
             tables=[ktable([("조조할인", "a matinee discount; “early morning discount”"), ("조조", "early morning (the book’s note)")])]),
        card("Activities left out",
             "The SMART Board activities, the reading and listening of the Presentation Activity and Follow-up 2 (listening to two conversations about the genres and the impressions of movies, and to three short conversations between a customer and an employee at the box office; the tables are in English) are audio, computer, partner or class activities. Follow-up 1 is in the next lesson. The Useful Links (Cine21, Megabox) are websites."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not w.startswith(("~", "-")) and "/" not in w]))
        + _tr(_strip(_C_DLG1) + _strip(_C_DLG2))
        + [M("What are the two friends going to do on Saturday?", "See a movie", ["Go hiking", "Go shopping", "Study"], "영화 보러 갈까?"), M("What kind of movie does Woojin want to see first?", "A comedy", ["A horror movie", "An action movie", "A musical"], "코미디 영화가 보고 싶은데."),
           M("Why doesn’t Woojin like horror movies?", "Because they are scary", ["Because they are boring", "Because they are long", "Because they are expensive"], "무서워서 싫어."), M("Which movie does Eunbi suggest?", "‘Bullet Train’", ["‘Star Wars’", "‘Halloween’", "‘Cats’"], "불릿 트레인."),
           M("Who is the lead actor?", "Brad Pitt", ["Tom Cruise", "Keanu Reeves", "Sandra Bullock"], "브래드 피트가 주연이야."), M("Where is the movie showing?", "At Lotte Cinema", ["At CGV", "At Megabox", "At a school"], "롯데시네마에서 해."),
           M("When do they decide to meet?", "On Saturday at 10 a.m.", ["On Sunday at 10 a.m.", "On Saturday at noon", "On Friday evening"], "토요일 오전 열 시."), M("Why can’t Woojin buy the 10:30 showing?", "It has just sold out", ["It is too expensive", "It is for adults only", "The theater is closed"], "첫 회는 방금 매진됐습니다."),
           M("Which showing does Woojin buy instead?", "The 12:30 showing", ["The 11:00 showing", "The 14:00 showing", "The 13:30 showing"], "열두 시 반 표 두 장."), M("What does the clerk ask Woojin to show?", "His student ID", ["His passport", "His credit card", "His ticket"], "학생증 좀 보여주세요."),
           F("요즘 재미있는 코미디 영화가 별로 없___ 같아. (it seems)", "는 것", ["은 것", "을 것"], "없다 → 없는 것 같아."), F("난 공포 영화는 ___ 싫어. (because they are scary)", "무서워서", ["무섭고", "무서운데"], "무섭다 → 무서워서."), F("‘불릿 트레인’이 재미있을 ___ 같아. (it seems it will be fun)", "것", ["는", "ㄴ"], "-(으)ㄹ 것 같다."),
           F("어느 ___에서 상영해? (theater)", "극장", ["학생증", "제목"], "극장 = a theater."), F("관객이 많아서 첫 회는 방금 ___됐습니다. (sold out)", "매진", ["상영", "판매"], "매진되다 = to be sold out."), F("우진: ___ 두 장 주세요. (tickets)", "표", ["주연", "감독"], "표 = a ticket."),
           M("What is a 조조할인?", "A matinee discount (first showing of the day)", ["A student discount", "A group discount", "A midnight showing"], "조조 = early morning."), M("What does 조조 (早朝) mean?", "early morning", ["early afternoon", "late night", "noon"], "조조할인 = “early morning discount”."),
           read_q("영화 보러 갈까"), read_q("조조할인"), read_q("학생 할인 돼요"), read_q("관객이 많아서"), read_q("롯데시네마")]
    ),
)

# ================================================================== Activities C
_CGV = [
    ("아이맥스 토르: 러브 앤 썬더", "IMAX Thor: Love and Thunder"), ("대한민국 일 등 영화관 씨지브이 극장", "Korea’s No. 1 movie theater, CGV"),
    (f"{month_ko(7)} {day_ko(6)} 씨지브이에 토르가 온다! 최저 가격! 최고의 액션!", "On July 6 Thor comes to CGV! The lowest price! The best action!"),
    (f"조조·학생 {_kn(13000)} 원, 일반 {_kn(15000)} 원", "Matinee and students 13,000 won, general 15,000 won"), ("첫 회 상영: 아홉 시 사십 분", "First showing: 9:40"), (f"{sino(12)} 세 이상 관람가", "Rated for ages 12 and above"),
    (f"첫 회 관람 손님 {sino(100)} 분께 백화점 {sino(10)} 퍼센트 할인권을 드립니다.", "The first 100 customers who see the first showing will receive a 10% department store discount coupon."),
]
_MEGA = [
    ("메가박스", "MEGABOX"), (f"{month_ko(8)} {day_ko(10)} 헌트가 여러분을 찾아갑니다.", "On August 10 Hunt will come to see you."),
    (f"조조·학생 {_kn(8000)} 원, 일반 {_kn(10000)} 원", "Matinee and students 8,000 won, general 10,000 won"), ("첫 회 상영: 아홉 시 삼십 분", "First showing: 9:30"), (f"{sino(15)} 세 이상 관람가", "Rated for ages 15 and above"),
    (f"인터넷으로 예매하시면 {sino(5)} 퍼센트 할인해 드립니다.", "If you book on the internet, we will give you a 5% discount."),
]
_REVIEW = [
    ("영화 리뷰", "Movie review"),
    ("지난주 ‘탑건: 매버릭’을 보았다.", "Last week I saw ‘Top Gun: Maverick’."),
    ("이 영화는 조셉 코신스키가 감독이고 톰 크루즈가 주연인 영화다.", "This movie is a movie whose director is Joseph Kosinski and whose lead is Tom Cruise."),
    ("정말로 스릴 넘치는 액션영화인 것 같다.", "It seems to be a really thrilling action movie."),
    ("전편에서 나온 배우 발 킬머를 다시 볼 수 있어서 반가웠다.", "I was glad to be able to see the actor Val Kilmer from the previous film again."),
    ("특히 제니퍼 코넬리하고 톰 크루즈가 러브 스토리를 만드는 것도 이 영화의 여러 재미 중의 하나인 것 같다.", "In particular, Jennifer Connelly and Tom Cruise making a love story also seems to be one of the several pleasures of this movie."),
    ("두 사람은 탑건 시리즈에서 잘 어울리는 커플인 것 같다.", "The two of them seem to be a well-matched couple in the Top Gun series."),
]
_DIARY = [
    ("지난 주말에 영진이와 함께 극장에 가서 액션 영화 ‘로스트 시티’를 봤다.", "Last weekend I went to the theater with Youngjin and saw the action movie ‘The Lost City’."),
    ("주연 배우 산드라 블록과 채닝 테이텀이 너무 재미있었다.", "The lead actors Sandra Bullock and Channing Tatum were so funny."),
    ("액션영화이지만 코미디 영화 같았다.", "It was an action movie, but it was like a comedy."),
    ("감독은 누구인지 잘 모르겠다.", "I don’t really know who the director is."),
    ("영진이는 상영하는 영화 중에 무서운 공포 영화를 보고 싶어 했다.", "Youngjin wanted to see a scary horror movie among the movies that are showing."),
    ("그런데, 네 시 ‘로스트 시티’ 표를 샀다.", "But we bought tickets for the 4 o’clock ‘The Lost City’."),
    ("관객이 너무 많아서, 안 좋은 좌석에 앉았다.", "There were so many people in the audience that we sat in bad seats."),
    ("그래도 학생 할인을 받아서 싸게 보았다.", "Still, we got a student discount and saw it cheaply."),
]
_DIARY_W = [("극장", "a theater"), ("액션", "action"), ("주연", "starring; a main character"), ("배우", "an actor; an actress"), ("코미디", "comedy"), ("감독", "a (movie) director; a head coach"), ("상영", "a screening (of a movie); playing (a movie)"), ("공포", "horror"), ("관객", "an audience"), ("할인", "a discount (mine)")]
L9 = lesson(
    "Ch 17 · Activities C: movie advertisements, a review and a diary",
    "씨지브이 · 메가박스 · 첫 회 상영 · 관람가 · 영화 리뷰 · 탑건 · 로스트 시티",
    requires=[],
    cards=[
        card("Topic C, Follow-up 1 (Reading): two movie advertisements",
             "The book gives two advertisements for Korean movies at two different theaters (CGV with IMAX, and MEGABOX) and asks you to fill in a table in English (movie title, first show price, first show time, age limit, discount and terms). The texts are the book’s (dates, prices, times and ages are spelled out in Hangul; the Latin names are respelled; the telephone numbers are left out); the English is mine.",
             examples=passage(_CGV) + passage(_MEGA)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Theater", "Movie title", "First show price", "First show time", "Age limit", "Discount and terms"], [["CGV", "Thor: Love and Thunder", "Matinee/students 13,000 won; general 15,000 won", "9:40", "12 and above", "The first 100 customers at the first showing get a 10% department store discount coupon"], ["MEGABOX", "Hunt", "Matinee/students 8,000 won; general 10,000 won", "9:30", "15 and above", "5% off for booking on the internet"]])]),
        card("Activities, Activity 2 (Reading): a movie review",
             "The book gives a movie review posted by “Dojin” on a website (the date, 2022-7-23, and the address of the writer are left out) and asks you to circle the words you do not know and to fill in a table in English. The book glosses 스릴 넘치는 as “full of thrills”. The text is the book’s; the English is mine.",
             examples=passage(_REVIEW)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["Movie title", "Top Gun: Maverick"], ["Movie director", "Joseph Kosinski"], ["Main actor", "Tom Cruise"], ["Movie genre", "Action"]])]),
        card("Activities, Activity 1 (Reading): a diary entry",
             "The book gives a diary entry in which ten words are numbered, and asks you to translate each word into English (the first one, 극장 = theater, is done for you). The numbers are not clear in the text, so the ten words below are the Core Vocabulary words the entry uses (the order is the order of the entry); the English is the book’s, except 할인 (mine). The entry is the book’s; its English is mine.",
             examples=passage(_DIARY),
             tables=[ktable(_DIARY_W)]),
        card("Activities left out",
             "Activity 3 (listening to three dialogs about a problem buying tickets, and filling in the method of purchase and the problem) is an audio activity; Activity 4 (role-plays about going to a movie with situation cards) is a partner and class activity. The Core Vocabulary words are in the last lesson."),
    ],
    exercises=uniq(
        _tr(_CGV + _MEGA + _REVIEW + _DIARY + _DIARY_W)
        + [M("Which movie does the CGV advertisement show?", "Thor: Love and Thunder", ["Hunt", "Top Gun: Maverick", "The Lost City"], "토르: 러브 앤 썬더."), M("Which movie does the Megabox advertisement show?", "Hunt", ["Thor: Love and Thunder", "Top Gun: Maverick", "The Lost City"], "헌트."),
           M("What is the matinee price at CGV?", "13,000 won", ["8,000 won", "15,000 won", "10,000 won"], "조조·학생 만 삼천 원."), M("What is the general price at Megabox?", "10,000 won", ["8,000 won", "13,000 won", "15,000 won"], "일반 만 원."),
           M("What time is the first showing at CGV?", "9:40", ["9:30", "10:30", "9:00"], "아홉 시 사십 분."), M("What time is the first showing at Megabox?", "9:30", ["9:40", "10:00", "9:00"], "아홉 시 삼십 분."),
           M("What is the age limit of the CGV movie?", "12 and above", ["15 and above", "18 and above", "Any age"], "십이 세 이상 관람가."), M("How do you get a 5% discount at Megabox?", "By booking on the internet", ["By coming early", "By being a student", "By paying cash"], "인터넷으로 예매하시면 오 퍼센트 할인."),
           M("Who is the director of ‘Top Gun: Maverick’ in the review?", "Joseph Kosinski", ["Tom Cruise", "Val Kilmer", "Jennifer Connelly"], "조셉 코신스키가 감독."), M("Who is the lead actor in the review?", "Tom Cruise", ["Val Kilmer", "Joseph Kosinski", "Brad Pitt"], "톰 크루즈가 주연."),
           M("What kind of movie is ‘Top Gun: Maverick’ in the review?", "An action movie", ["A comedy", "A horror movie", "A musical"], "스릴 넘치는 액션영화."), M("What kind of movie was ‘The Lost City’, according to the diary?", "An action movie that was like a comedy", ["A horror movie", "A musical", "A ballet"], "액션영화이지만 코미디 영화 같았다."),
           M("Why did the writer sit in bad seats?", "There were many people in the audience", ["The tickets were cheap", "The writer was late", "The theater was small"], "관객이 너무 많아서."), M("What did the writer get?", "A student discount", ["A free ticket", "A coupon", "Nothing"], "학생 할인을 받아서."),
           F("영진이는 무서운 ___ 영화를 보고 싶어 했다. (horror)", "공포", ["액션", "코미디"], "공포 영화 = a horror movie."), F("액션영화이지만 코미디 영화 ___. (it was like)", "같았다", ["같은", "같다고"], "같았다 = was like."), F("정말로 스릴 넘치는 액션영화인 것 ___. (it seems)", "같다", ["같은", "같아서"], "-인 것 같다."),
           read_q("영화 리뷰"), read_q("탑건 매버릭"), read_q("로스트 시티"), read_q("첫 회 상영"), read_q("관람가")]
    ),
)

# ================================================================== Grammar C: attributive form + 것 같다
def _kk(verb):
    """(present, past, future) of an action verb with 것 같다: 먹다 -> 먹는 것 같다, 먹은 것 같다, 먹을 것 같다"""
    a, b, c = attr(verb)
    return a + " 것 같다", b + " 것 같다", c + " 것 같다"


def _st(verb):
    """attributive forms of a stative verb: (present, future)"""
    st = stem(verb)
    if verb.endswith(("있다", "없다")):
        return st + "는", st + "을"
    l, v, t = _K.decompose(st[-1])
    if verb in _IRR:
        base = st[:-1] + _K.compose(l, v, "")
        return base + "운", base + "울"
    if t == "ㄹ":
        return st[:-1] + _K.compose(l, v, "ㄴ"), st
    if t:
        return st + "은", st + "을"
    return st[:-1] + _K.compose(l, v, "ㄴ"), st[:-1] + _K.compose(l, v, "ㄹ")


def _kks(verb):
    p, f = _st(verb)
    return p + " 것 같다", f + " 것 같다"


_KK_EX = [("지금 눈이 오는 것 같아요.", "It looks like it snows or looks like it is snowing."), ("오 분 전에 눈이 온 것 같아요.", "It looks like it snowed five minutes ago."), ("오늘 저녁 눈이 올 것 같아요.", "It looks like it will snow tonight."),
          ("어제 비가 많이 온 것 같아요.", "It looks like it rained a lot yesterday."), ("지금 비가 오는 것 같아요.", "It looks like it is raining now."), ("한국말이 어려운 것 같아요.", "It seems that Korean is difficult."),
          ("내년에 한국에 갈 것 같습니다.", "It appears that I will go to Korea next year."), ("내일은 날씨가 따뜻해 질 것 같아요.", "I think that it will be warm tomorrow.")]
_KK_V = [("살다", "to live"), ("보다", "to see"), ("공부하다", "to study"), ("먹다", "to eat"), ("오다", "to come"), ("가다", "to go")]
_KK_S = [("재미있다", "to be fun"), ("길다", "to be long"), ("덥다", "to be hot"), ("어렵다", "to be difficult"), ("크다", "to be big"), ("좋다", "to be good")]
_KK_FU3 = [[("가", "김기철 씨가 결혼을 했을까?", "Do you think Mr. Kim Kichul got married?"), ("나", "반지를 끼고 있는 것을 보니까 결혼한 것 같아.", "Seeing that he is wearing a ring, it seems he got married.")],
           [("가", "스티브 씨한테 전화 했어?", "Did you call Steve?"), ("나", "응, 전화 했는데 전화를 안 받아. 집에 없는 것 같아.", "Yes, I called, but he doesn’t answer. It seems he is not at home.")],
           [("가", "김 일병, 요즘 어떻게 지내요?", "Private Kim, how are you these days?"), ("나", "대학에서 일본어를 공부해요.", "I study Japanese at a university."), ("가", "김 일병은 한국어도 잘했으니까 일본어도 잘할 것 같아요.", "Since you were good at Korean, too, it seems you will be good at Japanese as well.")]]
_KK_M = [("이 일병은 요즘 공부를 열심히 하는 것 같아요.", "Private Lee seems to be studying hard these days."), ("김 일병은 주말에 영화를 자주 보는 것 같아요.", "Private Kim seems to watch movies often on weekends."),
         ("김 일병은 일 년 후에 예쁜 여자를 만날 것 같아요. 그리고 이 년 후에 결혼할 것 같아요.", "Private Kim will probably meet a pretty woman in a year, and it seems he will get married in two years."), ("이 일병은 미국 대통령이 될 것 같아요.", "Private Lee will probably become the President of the United States.")]
L10 = lesson(
    "Ch 17 · Grammar C: “looks like” with the attributive form + 것 같다",
    "오는 것 같아요 · 온 것 같아요 · 올 것 같아요 · 재미있을 것 같아요 · 더운 것 같아요",
    requires=[],
    cards=[
        card("Expressing “looks like”",
             "In English, we often use the expressions (it) looks like …, it seems that …, or it appears that … to express speculation or conjecture, as in “Looks like the sea is calm”, followed by a tense-embedded clause: present (“looks like the sea is calm now”), past (“looks like the sea was calm then”) and future (“looks like the sea will be calm soon”).\n\n"
             "In Korean, we use an attributive form + 것 같다 to express (it) looks like …, it seems that …, or it appears that …. 오는 것, 온 것 and 올 것 are the attributive forms of the verb 오다 that reflect the present tense, past tense and future tense. Making full use of this grammar feature requires that you be familiar with the different attributive forms of action verbs you learned about in a previous chapter.",
             examples=passage(_KK_EX[:3])),
        card("The rule",
             "appropriate tense of attributive form + 것 같다.",
             tables=[table(["Tense", "Action verb", "Stative verb"], [["Present", "-는 것 같다", "-(으)ㄴ 것 같다"], ["Past", "-(으)ㄴ 것 같다", "(see the book’s examples)"], ["Future", "-(으)ㄹ 것 같다", "-(으)ㄹ 것 같다"]])],
             examples=passage(_KK_EX[3:])),
        card("Follow-up 1: the three tenses of an action verb",
             "The book’s model: 먹다 → 어제 먹은 것 같다, 지금 먹는 것 같다, 내일 먹을 것 같다. The forms below are mine, made by the same rule.",
             tables=[table(["Verb", "Present (-는 것 같다)", "Past (-(으)ㄴ 것 같다)", "Future (-(으)ㄹ 것 같다)", "Meaning"], [[v, *_kk(v), m] for v, m in _KK_V], say=[0, 1, 2, 3])]),
        card("Follow-up 2: the verb table",
             "The book’s table has the verbs 살다, 보다, 재미있다, 공부하다, 길다 and 덥다 with a present, a past and a future column; some cells are given: 사는 것 같다, 본 것 같다, 재미있을 것 같다, 공부한 것 같다, 길 것 같다 and 더운 것 같다. The cells for the action verbs are shown above; for the stative verbs the present and the future forms are shown here (mine); the book gives no past form for stative verbs.",
             tables=[table(["Stative verb", "Present", "Future", "Meaning"], [[v, *_kks(v), m] for v, m in _KK_S], say=[0, 1, 2])]),
        card("Follow-up 3: conversations with 것 같다",
             "The book gives three conversations with a blank in each, and a box of three verbs (잘하다, 결혼하다, 없다). The answers are mine (in the third one the book’s ‘일본어도’ is followed by 잘할 것 같아요).",
             examples=[e for d in _KK_FU3 for e in dlg(d)]),
        card("Follow-up 4: speculating about your partner",
             "You write three guesses about your partner’s present activities with -는 것 같다 and, on a “Lucky Card”, two lucky things that could happen to your partner with -(으)ㄹ 것 같다. The book’s models (the book writes 1년 and 2년; spelled out here; the English is mine):",
             examples=passage(_KK_M)),
        card("Activities left out",
             "Follow-up 1 (partners draw verb cards and change them into the three forms), Follow-up 2 (b) (listening to four conversations and circling the grammar form used) and Follow-up 4 (partner speculation with a Lucky Card) are audio or partner activities."),
    ],
    exercises=uniq(
        [M(f"What is the present form of {v} with 것 같다?", _kk(v)[0], [_kk(v)[1], _kk(v)[2]], f"{v}: action verb → {_kk(v)[0]}.") for v, m in _KK_V]
        + [M(f"What is the past form of {v} with 것 같다?", _kk(v)[1], [_kk(v)[0], _kk(v)[2]], f"{v}: past → {_kk(v)[1]}.") for v, m in _KK_V]
        + [M(f"What is the future form of {v} with 것 같다?", _kk(v)[2], [_kk(v)[0], _kk(v)[1]], f"{v}: future → {_kk(v)[2]}.") for v, m in _KK_V]
        + [M(f"What is the present form of {v} ({m}) with 것 같다?", _kks(v)[0], list(dict.fromkeys(x for x in [_kks(v)[1], stem(v) + "는 것 같다", stem(v) + "을 것 같다"] if x != _kks(v)[0]))[:2], f"{v}: stative verb → {_kks(v)[0]}.") for v, m in _KK_S]
        + [M(f"What is the future form of {v} ({m}) with 것 같다?", _kks(v)[1], list(dict.fromkeys(x for x in [_kks(v)[0], stem(v) + "는 것 같다", stem(v) + "던 것 같다"] if x != _kks(v)[1]))[:2], f"{v}: future → {_kks(v)[1]}.") for v, m in _KK_S]
        + _tr(_KK_EX + _KK_M + [x for d in _KK_FU3 for x in _strip(d)])
        + [M("What do the attributive forms 오는 것, 온 것 and 올 것 reflect?", "The present, past and future", ["Only the past", "A command", "A question"], "-는, -(으)ㄴ, -(으)ㄹ."), M("What does 눈이 올 것 같아요 mean?", "It looks like it will snow.", ["It looks like it snowed.", "It is snowing.", "It never snows."], "올 = future."),
           M("What does 눈이 온 것 같아요 mean?", "It looks like it snowed.", ["It looks like it will snow.", "It is snowing.", "It will not snow."], "온 = past."), M("What does 눈이 오는 것 같아요 mean?", "It looks like it is snowing.", ["It looks like it will snow.", "It looks like it snowed.", "I want to see snow."], "오는 = present."),
           F("지금 비가 ___ 것 같아요. (it looks like it is raining)", "오는", ["온", "올"], "Present action verb: 오는."), F("어제 비가 많이 ___ 것 같아요. (it looks like it rained)", "온", ["오는", "올"], "Past: 온."), F("내년에 한국에 ___ 것 같습니다. (I will go)", "갈", ["가는", "간"], "Future: 갈."),
           F("한국말이 어려운 것 ___. (it seems)", "같아요", ["같은데", "같고"], "같다 = to seem."), F("이 뮤지컬 공연이 재미있___ 것 같습니다. (it will be fun)", "을", ["는", "은"], "Future: 재미있을."), F("오늘은 날씨가 ___ 것 같아요. (it seems warm)", "따뜻한", ["따뜻하는", "따뜻할"], "Stative present: 따뜻한."),
           read_q("올 것 같아요"), read_q("온 것 같아요"), read_q("오는 것 같아요"), read_q("재미있을 것 같아요"), read_q("더운 것 같아요")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
_CV_SECS = [("Leisure and music", _CV_LEIS), ("Cultural events", _CV_EVENT), ("The internet", _CV_NET), ("Movie-related words", _CV_MOVIE), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not r[0].startswith(("~", "-")) and "/" not in r[0] and "~" not in r[0]]
L11 = lesson(
    "Ch 17 · Core vocabulary and self-evaluation",
    "주요 단어 · 취미 · 공연 · 영화 · 인터넷 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (40대 → 사십 대, 5세 → 오 세, 10대 → 십 대, 20대 → 이십 대, 19세 → 십구 세, 3개월 → 삼 개월, S석 → 에스석, 0번 → 영 번, 007 → 영영칠, DLI → 디엘아이); the book’s ‘13일의 금요일’ is spelled ‘십삼 일의 금요일’. The book’s example for 홈페이지 gives a web address, which is left out; the sentence shown for it is mine. The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the Additional Vocabulary section of the book is blank."),
    ] + [card(name, "Italicized English words in the book are grammatical terms, not the meaning of a Korean word." if name == "Other words" else "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify Koreans’ common interests and hobbies; exchange information about personal interests and hobbies; extract and talk about basic information found on posters about cultural events and movies; give simple instructions for purchasing tickets of cultural events; and elicit information at the box office for a movie.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the gerund or verbal ending that is used as a noun; 르 irregular verbs; the attributive form + 것 같다 (looks like …; it seems that …); and the Sino-Korean syllable 회 (會)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does the Sino-Korean syllable 회 (會) mean?", "a gathering; a meeting", ["a type", "not; no", "the sea"], "동호회, 동창회, 산악회, 학회."), M("What does -는 것 do to a verb?", "It makes the verb a noun (gerund)", ["It makes the verb past", "It negates the verb", "It makes a question"], "한국말을 가르치는 것."),
           M("What does -(으)ㄴ/는/(으)ㄹ 것 같다 mean?", "it seems that …; it looks like …", ["I want to …", "I have to …", "because …"], "재미있을 것 같습니다."), M("What are 르 irregular verbs?", "Verbs whose stem ends in 르 and change to ㄹ라/ㄹ러", ["Verbs whose stem ends in ㅂ", "Verbs that have no stem", "Verbs with ㅎ"], "모르다 → 몰라요."),
           M("What is “a matinee discount”?", "조조할인", ["일반석", "초대권", "학생증"], "조조할인 = a matinee discount."), M("What is “a general admission seat”?", "일반석", ["조조할인", "초대권", "학생증"], "일반석 = a general admission seat."),
           M("What is “a complimentary ticket”?", "초대권", ["일반석", "학생증", "티켓"], "초대권 = a complimentary ticket; a free ticket."), M("What is “a student ID card”?", "학생증", ["초대권", "일반석", "제목"], "학생증 = a student ID card.")]
        + [read_q("주요 단어"), read_q("문화생활"), read_q("전시회"), read_q("초대권"), read_q("학생증")]
    ),
)

UNIT = unit("Semester 1 · Unit 5 · Chapter 17: Cultural Life (문화생활)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11])

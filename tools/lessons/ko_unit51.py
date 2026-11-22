"""Unit 51: KBC Semester 2, Unit 11, Chapter 44 - Various Aspects of Korean Society (한국 사회의 여러 모습).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 11, Student's Edition (2022).
Audio, video, pictures, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 44 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("간소화", "(簡素化) simplification (to simplify; to be simplified) (~하다/되다)", "여권 신청 절차가 간소화 됐어요."),
    ("~ 내내", "throughout", "주말 내내 비가 와서 아무 데도 못 갔어요."),
    ("덜다", "to lessen; to relieve; to reduce", "음식은 각자 접시에 덜어서 드세요."),
    ("~을/를 맞아(서)/맞이하여", "for (the upcoming event); on the occasion of", "결혼기념일을 맞아 그 부부는 유럽여행을 갔다. 추석을 맞이하여 재미있는 행사가 많이 열린다."),
    ("밀리다", "to be congested; to be backed up; “to get behind”", "출퇴근 시간에는 도로에 차가 많이 밀립니다."),
    ("바꾸다/바뀌다", "to change/to be changed", "옷이 좀 커서 작은 사이즈로 바꿨어요. 아이가 자라면서 얼굴이 많이 바뀌었다."),
    ("예상", "(豫想) expectancy; anticipation; prospect (to expect; to anticipate/to be expected; to be anticipated) (~하다/되다)", "전문가들은 국제야구대회에서 미국이 이길 것으로 예상했습니다."),
    ("온 ~", "entire; all; whole", "월드컵 축구 경기 동안은 온 나라가 축구에 대한 얘기만 해요."),
    ("일부", "(一部) a part; a portion; some", "우리 회사의 직원들 중 일부는 야간근무를 합니다."),
    ("정체", "(停滯) stagnation (to be stagnated) (~되다)", "밤새 내린 폭설로 일부 고속도로에서는 차량의 정체가 심합니다."),
    ("제사", "(祭祀) an ancestral worship ritual (to perform an ancestral ritual) (~지내다)", "우리 집에서는 일 년에 두 번 할아버지 제사를 지냅니다."),
    ("종일", "(終日) all day (long); “(till) end of a day”", "일이 많아서 종일 아무것도 못 먹었어요."),
    ("차량", "(車輛) vehicles; cars", "차량 네 대가 충돌하는 사고가 일어났어요."),
    ("체증", "(滯症) dyspepsia; (traffic) congestion; indigestion", "자동차가 많아지면서 교통 체증이 점점 심해지고 있어요."),
    ("최대", "(最大) the biggest; the largest; maximum; up to", "이번 세일 동안 핸드백은 최대 사십 퍼센트까지 할인됩니다."),
    ("친정", "(親庭) a married woman’s parents’ home", "친정에 자주 가고 싶은데 그러질 못 해요."),
    ("풍경", "(風景) scenery; a scene", "저는 풍경 사진을 찍기 위해 가끔 교외로 나갑니다."),
    ("풍속", "(風俗) customs", "전통 풍속 중에서 좋은 것은 계속 지켜가야 해요."),
    ("행렬", "(行列) a queue; a procession", "극장 앞에 사람들의 행렬이 길었어요."),
    ("휴양지", "(休養地) a resort; “resting and nurturing place”", "카리브해에 있는 휴양지에서 휴가를 보낼 거예요."),
]
_CV_B = [
    ("경기장", "(競技場) a (sports) stadium; a (sports) arena", "주말에 프로야구 경기장에 갔다 왔어요."),
    ("골(을) 넣다", "to score a goal; to put in a goal", "한국 축구팀은 전반전에 두 골을 넣었습니다."),
    ("광장", "(廣場) a plaza; “spacious place”", "시청 앞 광장에서 가수들이 공연을 하고 있어요."),
    ("금/은/동", "(金/銀/銅) gold/silver/bronze", "한국은 이번 동계올림픽에서 금, 은, 동메달을 모두 스물네 개 땄습니다."),
    ("대단하다", "to be great; to be enormous; to be outstanding", "우리 아버지는 자식들에 대한 사랑이 대단하십니다."),
    ("대항", "(對抗) act in opposition; countering; against (to counter; to act in opposition) (~하다)", "학교 대항 축구에서 우리 학교가 이겼습니다."),
    ("동계", "(冬季) winter season", "동계 올림픽은 사 년마다 열립니다."),
    ("메달", "a medal", "한국 피겨 스케이팅이 올림픽에서 처음으로 금메달을 땄습니다."),
    ("본선", "(本選) post-preliminary matches; the finals; “main selection”", "서른두 개의 국가가 월드컵 축구 본선에 오릅니다."),
    ("스피드 스케이팅", "speed skating", "제 동생은 스피드 스케이팅 선수입니다."),
    ("승리", "(勝利) victory (to win; to be victorious/to achieve victory) (~하다/~를 거두다)", "스페인 축구팀이 월드컵에서 승리를 했습니다. 한국시리즈 야구경기에서 롯데 자이언츠가 승리를 거두었습니다."),
    ("신(이) 나다", "to be excited", "어제 축구 경기에서 한국팀이 승리해서 아주 신 났습니다."),
    ("아마추어", "an amateur", "이 국제경기에는 아마추어 선수들만 참가할 수 있습니다."),
    ("어쨌든", "anyway; at any rate", "어떻게 하지요? 벌써 파티가 다 끝났어요. 어쨌든 와 주셔서 감사해요."),
    ("역전", "(逆轉) a reversal; a turnabout (victory); (to reverse/to be reversed) (~하다/되다)", "미국 팀이 아이스하키 결승전에서 역전승했습니다."),
    ("열광적", "(熱狂的) wild; enthusiastic", "콘서트에 열광적인 팬들이 많이 왔습니다."),
    ("열기", "(熱氣) excitement; fever", "경기장의 응원 열기가 대단합니다."),
    ("예선", "(豫選) the preliminaries; preliminary round; preliminary selection", "각 대륙에서 예선을 통과한 나라가 월드컵 본선에 진출합니다."),
    ("올림픽", "Olympics", "하계 올림픽은 사 년마다 열립니다."),
    ("월드컵", "(FIFA) World Cup", "브라질은 월드컵에서 여러 번 우승했습니다."),
    ("응원", "(應援) cheering (to cheer; to root for) (~하다)", "미국팀과 중국팀의 탁구 경기에서 나는 미국팀을 응원했습니다."),
    ("전반전", "(前半戰) the first half of a game", "한국 핸드볼 팀이 전반전 동안 서른 골을 넣었습니다."),
    ("종목", "(種目) a sporting event", "한국은 동계 올림픽 쇼트트랙 종목에서 메달을 많이 땁니다."),
    ("체계적", "(體系的) systematic", "요즘 운동 선수들은 체계적인 훈련을 받습니다."),
    ("코치", "a coach (to coach) (~하다)", "좋은 코치와 함께 열심히 훈련을 하면 좋은 선수가 될 수 있습니다."),
    ("프로", "a professional; an expert", "한국에는 롯데 자이언츠, 해태 타이거즈 등 많은 프로 야구 팀이 있습니다."),
    ("피겨 스케이팅", "figure skating", "여자 피겨 스케이팅을 동계 올림픽의 꽃이라고 합니다."),
    ("하계", "(夏季) the summer (season)", "서울에서 천구백팔십팔 년 하계 올림픽이 열렸습니다."),
    ("후반전", "(後半戰) the second half of a game", "월드컵에서 영국팀이 후반전에 두 골을 넣었습니다."),
]
_CV_C = [
    ("경쟁", "(競爭) competition (to compete) (~하다)", "좋은 회사들은 경쟁이 심해서 들어가기 어렵습니다."),
    ("(대)답", "(對)答 an answer; a reply (to answer; to reply) (~하다)", "선생님의 질문에 학생이 대답을 못했습니다."),
    ("디자이너", "a designer", "그 배우는 유명 디자이너의 옷을 입고 있습니다."),
    ("목표", "(目標) a goal; a target", "우리의 목표는 이번 올림픽에서 메달을 다섯 개 이상 따는 것이다."),
    ("본인", "(本人) oneself; “main person”", "이 학원은 본인이 직접 와서 등록해야 합니다."),
    ("소득", "(所得) income", "소득보다 지출이 많아서 힘들어요."),
    ("소질", "(素質) talent; aptitude", "저는 운동에 소질이 없어요."),
    ("수의사", "(獸醫師) a veterinarian; “animal doctor”", "우리 집 고양이가 아파서 수의사에게 데려갔습니다."),
    ("스타", "a star (in entertainment business); a celebrity", "배우가 되는 것은 쉽지만 인기 스타가 되기는 어려워요."),
    ("안정(적)", "(安定(的)) stability (stable) (to be stable) (~되다)", "요즘에는 소득이 높은 직업보다 안정된 직업이 인기가 있어요."),
    ("연기", "(演技) acting (to act) (~하다)", "저 배우는 연기를 아주 잘 합니다."),
    ("연예인", "(演藝人) an entertainer; a celebrity", "이번 축제에 유명한 연예인들이 옵니다."),
    ("의사", "(意思) intention", "자신의 의사를 분명하게 이야기하세요."),
    ("이루다", "to achieve (a dream); to accomplish (a goal)", "저는 요리사가 되고 싶어요. 그 꿈을 이루기 위해 요리학교에 등록했어요."),
    ("장래", "(將來) the future", "아들의 장래 희망은 변호사입니다."),
    ("재능", "(才能) talent; aptitude", "저 아이는 노래에 재능이 있어요."),
    ("제외", "(除外) exclusion (to exclude/to be excluded) (~하다/되다)", "우리 집에서 저를 제외하고 모두 키가 작아요."),
    ("탤런트", "a TV actor/actress; “talent”", "어제 시내에서 제가 좋아하는 탤런트를 봤어요."),
    ("프로게이머", "a pro(fessional) gamer", "요즘은 프로게이머가 되고 싶어하는 청소년들이 많아요."),
    ("허락", "(許諾) permission; approval (to permit; to approve) (~하다)", "부모님이 허락하지 않아서 친구들과 여행을 갈 수 없어요."),
    ("현실(적)", "(現實(的)) reality; actuality", "우리 팀이 우승하는 것은 현실적으로 불가능합니다."),
]
_CV_GR = [
    ("–든(지)", "no matter (who/what/when/where/how)", "누구를 만나든지 인사를 잘해야 해요. 어떻게 하든지 이 일을 끝내세요."),
    ("~까지(도)", "even; to a degree that extends", "어린 아이들까지도 거리에 나와서 응원했어요. 하루 종일 요리하고 설거지했어요. 또 집 청소까지 했어요."),
    ("–기 전에/–(으)ㄴ 후에/–(으)ㄹ 때(에)", "before/after/when", "음식을 먹기 전에 손을 씻어요. 숙제 한 후에 놀아요."),
]
_CV_SINO = [("최대", "(最大) the biggest; the largest", "최고, 최저, 최소, 대문, 대령, 대위"), ("동계", "(冬季) winter season", "동절기, 동면, 동복, 하계 올림픽, 계절, 사계"), ("안정", "(安定) stability", "안전, 불안, 평안, 결정, 측정, 부정")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"간소화": "simplification", "바꾸다": "to change", "바뀌다": "to be changed", "예상": "expectation; anticipation", "안정": "stability", "현실": "reality", "대답": "an answer; a reply", "금": "gold", "은": "silver", "동": "bronze", "전반": "the first half", "후반": "the second half"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"


def _words(keys):
    pl = _PLAIN(keys)
    out = [ktable(_rows(pl))]
    rest = [k for k in keys if k not in pl]
    if rest:
        out.append(table(["Word", "Meaning"], [[k, _en(k)] for k in rest]))
    return out


# ---- Sino-Korean notes
_S1G = [("최신", "the latest; “the newest”"), ("최장", "the longest"), ("최강", "the strongest; the most powerful"), ("최후", "the last"), ("최악", "the worst; “the evilest”"), ("대학교", "university"), ("대가족", "a large family")]
_S1 = [("최고", "the highest; the best; the top"), ("최저", "the lowest; the minimum"), ("최상", "the best; the finest; the top"), ("최하", "the lowest; the worst; the bottom"), ("최다", "the most; the largest number"), ("최소", "the smallest; the least; the minimum")]
_S2G = [("동계 올림픽", "Winter Olympics"), ("동계 훈련", "winter training"), ("동계 방학", "a winter vacation"), ("동지", "winter solstice"), ("춘하추동", "four seasons; “spring, summer, fall, winter”"), ("동복", "winter clothes; winter wear"), ("동면", "hibernation; “winter sleep”"), ("사계절", "four seasons"), ("춘계", "spring; springtime"), ("하계", "summer; summertime"), ("추계", "fall"), ("하계 올림픽", "summer Olympics"), ("춘계 소풍", "a spring picnic"), ("하계 모임", "a summer meet; a summer gathering")]
_S3G = [("안정감", "sense of stability"), ("안정시키다", "to stabilize"), ("안정되다", "to be stabilized"), ("안녕하다", "to be fine; “to be serene and comfortable”"), ("안심하다", "to feel relieved; to feel easy; “to have a serene mind”"), ("안착", "a safe arrival"), ("편안하다", "to be peaceful; to be calm; “to be comfortable and calm”"), ("정가", "a set price; a fixed price"), ("정기총회", "a regular general meeting"), ("정식", "a meal on a fixed menu")]

L1 = lesson(
    "Ch 44 · What the chapter teaches, 최대 · 동계 · 안정",
    "한국 사회의 여러 모습 · 최대 · 동계 · 안정 · 최고 · 최저 · 하계 · 안심",
    requires=[],
    cards=[
        card("What Chapter 44 teaches (한국 사회의 여러 모습)",
             "Chapter 44, “Various Aspects of Korean Society”, has a vocabulary builder, three topic presentations (traditional holidays, sports events and sports culture, job preferences) with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and describe social customs and trends related to major national holidays; identify and discuss sports events and sports culture; and compare and discuss how job preferences have changed.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; a summary of conjunctive endings related to time reference; an interrogative word followed by –든(지) (no matter what/who/when, etc.); ~까지(도) (even; to a degree that extends); and the Sino-Korean syllables within 최대 (最大), 동계 (冬季), and 안정 (安定)."),
        card("Sino-Korean in use: 최대 (最大)",
             "The first syllable 최 (最) is primarily used as a prefix indicating that the word containing it is in the superlative, as in 최신 (the latest; “the newest”), 최장 (the longest), 최강 (the strongest; the most powerful), 최후 (the last), and 최악 (the worst; “the evilest”). The second syllable 대 (大), which you have seen in 대학교 and 대가족, means big or large. Thus, the Sino-Korean word 최대 is a superlative and means the biggest or the largest. The book asks you to guess the meaning of 최고, 최저, 최상, 최하, 최다 and 최소 (my answers):",
             tables=[ktable(_S1G), ktable(_S1)]),
        card("Sino-Korean in use: 동계 (冬季)",
             "This Sino-Korean word means winter or wintertime and is normally used as an adjective modifying the noun that follows, as in 동계 올림픽 (Winter Olympics), 동계 훈련 (winter training), and 동계 방학 (a winter vacation). The first syllable 동 (冬) means winter, as in 동지 (winter solstice), 춘하추동 (four seasons; “spring, summer, fall, winter”), 동복 (winter clothes; winter wear), and 동면 (hibernation; “winter sleep”). The second syllable 계 (季) means season, as in 사계절 (four seasons). Thus the literal meaning of the word is “winter season,” and the word is followed by a noun indicating an event. To express other seasonal events, Koreans use 춘계 (春季) meaning spring or springtime, 하계 (夏季) meaning summer or summertime, and 추계 (秋季) meaning fall, as in 하계 올림픽 (summer Olympics), 춘계 소풍 (a spring picnic), and 하계 모임 (a summer meet; a summer gathering).",
             tables=[ktable(_S2G)]),
        card("Sino-Korean in use: 안정 (安定)",
             "This Sino-Korean word means stability or calm, as in 안정감 (sense of stability), 안정시키다 (to stabilize), and 안정되다 (to be stabilized). The first syllable 안 (安) means serene, tranquil, or comfort, as in 안녕하다 (to be fine; “to be serene and comfortable”), 안심하다 (to feel relieved; to feel easy; “to have a serene mind”), 안착 (a safe arrival), and 편안하다 (to be peaceful; to be calm; “to be comfortable and calm”). The second syllable 정 (定) means set, fix(ed), settle(d), or decide(d), as in 정가 (a set price; a fixed price), 정기총회 (a regular general meeting), and 정식 (a meal on a fixed menu). Thus the literal meaning of the word 안정 is “serene and fixed.”",
             tables=[ktable(_S3G)]),
    ],
    exercises=uniq(
        _tr(_S1G + _S1 + _S2G + _S3G, k=3)
        + [M("What does 최 (最) do in a word?", "Makes it a superlative", ["Means land", "Means teaching", "Means a job"], "최신, 최대."), M("What does 대 (大) mean?", "big; large", ["small", "winter", "stable"], "대학교."), M("What does 최대 mean?", "the biggest; the largest", ["the smallest", "the newest", "the worst"], "최 + 대."), M("What does 동 (冬) mean?", "winter", ["spring", "summer", "fall"], "동지."), M("What does 계 (季) mean?", "season", ["winter", "teaching", "land"], "사계절."), M("What is the literal meaning of 동계?", "“winter season”", ["“big winter”", "“cold land”", "“four seasons”"], "동 + 계."), M("Which syllable means spring?", "춘 (春)", ["하 (夏)", "추 (秋)", "동 (冬)"], "춘계."), M("Which syllable means summer?", "하 (夏)", ["춘 (春)", "추 (秋)", "동 (冬)"], "하계."), M("What does 안 (安) mean?", "serene; tranquil; comfort", ["fixed", "big", "winter"], "안심."), M("What does 정 (定) mean?", "set; fixed; settled; decided", ["serene", "season", "big"], "정가."), M("What is the literal meaning of 안정?", "“serene and fixed”", ["“big and set”", "“winter season”", "“fixed price”"], "안 + 정."),
           F("___ 올림픽은 여름에 열립니다. (summer)", "하계", ["동계", "추계"], "하계."), F("___ 올림픽은 눈과 얼음 위에서 합니다. (winter)", "동계", ["하계", "춘계"], "동계."), F("이번 대회 ___ 참가국은 백 개국입니다. (the largest)", "최대", ["최소", "최저"], "최대."), F("그 사람은 ___으로 일하는 직업을 원합니다. (stable)", "안정적", ["현실적", "열광적"], "안정적."), F("___ 가격이 가장 낮은 값입니다. (the lowest)", "최저", ["최고", "최다"], "최저."),
           read_q("최대"), read_q("동계"), read_q("안정"), read_q("최고와 최저"), read_q("하계 올림픽")]
    ),
)

# ================================================================== L2 Vocabulary builder
_VB = [("입시", "entrance examination"), ("경쟁", "a competition"), ("대답", "an answer; a reply"), ("수의사", "a veterinarian"), ("예상", "prediction; to predict"), ("일부", "a part; a portion"), ("체증", "traffic congestion"), ("차량", "vehicles"), ("친정", "a married woman’s parents’ home"), ("풍경", "scenery; a view"), ("허락", "permission"), ("휴양지", "a resort")]
_VBM = [("친정", "a married woman’s parents’ home", "a. 결혼한 여자 부모님의 집"), ("일부", "a part; a portion", "b. 전체가 아니고 작은 부분이나 한 부분"), ("수의사", "a veterinarian", "c. 동물을 치료해 주는 의사"), ("코치", "a coach", "d. 운동 선수들에게 운동을 가르쳐 주는 선생님"), ("풍경", "scenery; a view", "e. 아름다운 경치나 볼만한 것"), ("차량", "vehicles", "f. 여러 종류의 자동차"), ("허락", "permission", "g. 어떤 일을 해도 된다고 말함")]
L2 = lesson(
    "Ch 44 · Vocabulary Builder: holidays, sports and jobs",
    "입시 · 경쟁 · 대답 · 수의사 · 예상 · 일부 · 체증 · 차량 · 친정 · 풍경 · 허락 · 휴양지 · 코치",
    requires=[],
    cards=[
        card("새 단어: guess the meanings",
             "The book gives eleven sentences with an underlined word and asks you to match each word with its English meaning (the underlining is not in my text; I give the sentences, the word and the answer). The sentences are the book’s; the meanings are the book’s own list.",
             tables=[table(["Sentence", "Word", "Meaning"], [["입시 경쟁이 치열합니다.", "경쟁", "a competition"], ["질문이 어려워서 대답을 못 했습니다.", "대답", "an answer; a reply"], ["수의사는 동물을 치료합니다.", "수의사", "a veterinarian"], ["어느 팀이 우승할지 예상할 수 없습니다.", "예상", "prediction; to predict"], ["전체를 고치지 말고 일부만 고칩시다.", "일부", "a part; a portion"], ["명절에는 교통 체증이 심해요.", "체증", "traffic congestion"], ["출근길은 차량으로 붐빕니다.", "차량", "vehicles"], ["영애 씨는 부모님을 만나러 친정에 갔습니다.", "친정", "a married woman’s parents’ home"], ["시골의 가을 풍경은 참 아름답습니다.", "풍경", "scenery; a view"], ["부모님께서 허락하시면 결혼하고 싶어요.", "허락", "permission"], ["휴가 때는 휴양지에 가서 쉴 거예요.", "휴양지", "a resort"]], say=[0, 1])]),
        card("Activity 2: clues and the grid",
             "Read each clue and identify the corresponding word in the grid (the grid is a letter puzzle and is left out; the clues are the book’s, the words are my answers; the book’s sample is a: 친정). The grid’s words are 친정, 일부, 수의사, 코치, 풍경, 차량, 허락.",
             tables=[table(["Clue", "Word (mine)", "English"], [[c, w, e] for w, e, c in _VBM], say=[1])]),
        card("Activities left out", "The first activity (SMART Board), Activities 1, 3 and 4 (SMART Board), the PowerPoint Sino-Korean presentation, and Activity 5 (“Two-in-One Review”: in pairs you circle two words from a list, make one sentence using both, say it aloud to the class for a point, and the other pairs cross out the words and may challenge an incorrect sentence) are computer and game activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(["경쟁", "수의사", "일부", "체증", "차량", "친정", "풍경", "허락", "휴양지", "코치"]))
        + [M("Which word is described by “결혼한 여자 부모님의 집”?", "친정", ["풍경", "차량", "일부"], "a."), M("Which word is described by “전체가 아니고 작은 부분이나 한 부분”?", "일부", ["친정", "허락", "차량"], "b."), M("Which word is described by “동물을 치료해 주는 의사”?", "수의사", ["코치", "탤런트", "디자이너"], "c."), M("Which word is described by “운동 선수들에게 운동을 가르쳐 주는 선생님”?", "코치", ["수의사", "감독", "스타"], "d."), M("Which word is described by “아름다운 경치나 볼만한 것”?", "풍경", ["차량", "일부", "허락"], "e."), M("Which word is described by “여러 종류의 자동차”?", "차량", ["풍경", "친정", "일부"], "f."), M("Which word is described by “어떤 일을 해도 된다고 말함”?", "허락", ["대답", "경쟁", "예상"], "g."),
           F("입시 ___이 치열합니다. (competition)", "경쟁", ["대답", "허락"], "경쟁."), F("부모님께서 ___하시면 결혼하고 싶어요. (permit)", "허락", ["대답", "예상"], "허락하다."), F("출근길은 ___으로 붐빕니다. (vehicles)", "차량", ["풍경", "일부"], "차량."), F("명절에는 교통 ___가 심해요. (congestion)", "체증", ["경쟁", "허락"], "체증."), F("휴가 때는 ___에 가서 쉴 거예요. (resort)", "휴양지", ["친정", "경기장"], "휴양지."),
           read_q("입시 경쟁이 치열합니다"), read_q("수의사는 동물을 치료합니다"), read_q("명절에는 교통 체증이 심해요"), read_q("친정"), read_q("휴양지")]
    ),
)


# ================================================================== L3 Topic A
_A_TXT = [
    ("설과 추석은 한국의 최대 민속 명절이다.", "Lunar New Year and Chuseok are Korea’s biggest traditional folk holidays."),
    ("설과 추석을 맞아서 많은 사람이 부모님이 계시는 고향을 방문한다.", "On the occasion of Lunar New Year and Chuseok, many people visit their hometowns where their parents are."),
    ("따라서 고속도로는 긴 귀성 차량 행렬과 밀린 차량 때문에 교통 정체가 심하다.", "Therefore, the highways have heavy traffic jams because of the long lines of vehicles of people going home and the backed-up vehicles."),
    ("명절 연휴가 짧으면 교통 정체가 더 심해진다.", "If the holiday break is short, the traffic jams get even worse."),
    ("그리고 많은 주부는 명절 연휴 내내 제사 음식을 만드느라 종일 바쁘다.", "And many housewives are busy all day throughout the holiday break making food for the ancestral rituals."),
    ("하지만, 요즘 명절 행사가 간소화되면서 일부에서는 명절 풍경이 많이 바뀌고 있다.", "However, as holiday events have been simplified these days, the holiday scenery is changing a lot in some households."),
    ("김미진 씨네는 명절 때 시골에 사시는 부모님께서 서울로 올라오신다.", "At Ms. Kim Mijin’s family’s place, her parents who live in the countryside come up to Seoul for the holidays."),
    ("그래서 미진 씨네는 고속도로에서 교통 체증을 겪지 않아도 된다.", "So Mijin’s family does not have to go through traffic congestion on the highway."),
    ("또, 미진 씨는 음식을 준비하는 부담을 덜기 위해서 제사 음식을 인터넷으로 주문한다.", "Also, to lessen the burden of preparing food, Mijin orders the ancestral ritual food over the internet."),
    ("그리고 명절날 아침에 간단히 차례를 지낸다.", "And on the morning of the holiday, they briefly hold the ancestral memorial service."),
    ("차례를 지낸 후에는 온 가족이 휴양지에 가서 연휴를 즐긴다.", "After holding the memorial service, the whole family goes to a resort and enjoys the holiday break."),
]
_A_WORDS = ["간소화", "~ 내내", "덜다", "~을/를 맞아(서)/맞이하여", "밀리다", "바꾸다/바뀌다", "예상", "온 ~", "일부", "정체", "제사", "종일", "차량", "체증", "최대", "친정", "풍경", "풍속", "행렬", "휴양지"]
_CH = [
    ("달라진 추석 풍경", "Changed Chuseok scenes"),
    ("공무원 김상진 씨는 온 가족과 함께 이번 추석 연휴에 중국으로 여행을 가기로 했다.", "Public servant Mr. Kim Sangjin decided to travel to China with his whole family over this year’s Chuseok holiday."),
    ("막내아들이 곧 입대하고 십일월에 큰딸이 결혼식을 올릴 예정이어서 가족이 함께할 수 있는 마지막 외국여행을 결심한 것이다.", "Because his youngest son will soon enter the military and his eldest daughter is to hold her wedding in November, he made up his mind on the last overseas trip the family can take together."),
    ("김 씨는 제사에 참석하지 못하는 것이 아쉽다라고 말했다.", "Mr. Kim said, “It is a shame that I cannot attend the ancestral ritual.”"),
    ("추석 연휴에 여행을 가기 때문에 벌써 이 주 전에 성묘했고 큰 형님댁에도 미리 가서 인사를 드렸다.", "“Because I am traveling over the Chuseok holiday, I already visited the ancestral graves two weeks ago and went ahead of time to my eldest brother’s house to pay my respects.”"),
]
L3 = lesson(
    "Ch 44 · Topic A: Lunar New Year and Chuseok (설과 추석)",
    "설 · 추석 · 귀성 · 교통 체증 · 제사 · 차례 · 명절 풍경 · 간소화",
    requires=[],
    cards=[
        card("Topic A: Lunar New Year and Chuseok (귀성 차량이 많아서 길이 막혀요)",
             "The following article is about two traditional Korean holidays, Lunar New Year and Chuseok. (The English is mine; the book gives none. The book’s footnote: ~화 (化) is much like the English suffix -ization or -fication, as in 간소화 [simplification] and 세계화 [globalization].)",
             examples=passage(_A_TXT)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists 최대 here; its Sino-Korean note is in the first lesson.", tables=_words(_A_WORDS)),
        card("한국에서는",
             "설날 (Lunar New Year’s Day) is the first day of the lunar calendar, and it generally falls on the day of the second new moon after the winter solstice. 추석 (Harvest Festival; “Autumn Evening”) is the 15th day of the 8th month of the lunar calendar. These two holidays are the most important traditional holidays in Korea, for on these days Koreans have long celebrated the New Year and newly harvested crops (respectively) with their extended family and the spirits of their deceased ancestors. On the mornings of these holidays, Koreans perform ancestral worship rituals. They often visit the tombs of their ancestors to clean the area around the tombs, and they leave offerings of food and drink.\n\n"
             "Around these holidays, millions of Koreans are on the move, traveling to and from their hometowns where their parents reside. Thus, the highways become very congested and driving times double or even triple. Radio stations broadcast special traffic updates for motorists during these times of massive exodus from the cities. As part of a new trend, some elderly parents who live in smaller provinces are choosing to travel to their children’s homes in cities instead of their children traveling to see them.\n\n"
             "It is increasingly common nowadays for holiday food preparation to be divided among participating siblings, who bring their own dishes to share with the rest of their family. Catering services are gaining more popularity, especially among younger housewives."),
        card("Follow-up 2 (Reading): Changed Chuseok scenes",
             "The following excerpt is from a news article about Chuseok. The book asks four questions in English; the article is the book’s with the numbers spelled out (the book’s header “(54. 종로구 인사동)” is left out, and its quotation marks and “라고 말했다” are kept as 라고 말했다); the English and the answers are mine.",
             examples=passage(_CH)),
        card("The answers (mine)", "",
             tables=[table(["Question", "Answer (mine)"], [["1. Translate the title of the article into English.", "“Changed Chuseok Scenes” (or “The Changing Face of Chuseok”)"], ["2. What is Mr. Kim Sangjin planning to do during this year’s Chuseok?", "Travel to China with his whole family"], ["3. What are the two reasons for his plan?", "His youngest son will soon enter the military; his eldest daughter will marry in November (so it is the last overseas trip the family can take together)"], ["4. What two things did Mr. Kim do in advance?", "Visited the ancestral graves two weeks earlier; went to his eldest brother’s house early to pay his respects"]])]),
        card("Activities left out", "The presentation steps of Topic A (SMART Board; reading and listening along; reviewing with the teacher) and Follow-up 1 (listening to three narrations in which a woman talks about a negative experience during the traditional holidays of the previous year and her plan for this year) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT + _CH, k=3)
        + [M("What are Korea’s biggest traditional holidays?", "Lunar New Year and Chuseok", ["Children’s Day and Hangeul Day", "Christmas and Easter", "Memorial Day and Liberation Day"], "설과 추석."), M("Why are the highways jammed?", "Many people travel to their hometowns", ["A road is being built", "It is snowing", "There is a festival"], "귀성 차량 행렬."), M("What happens if the holiday break is short?", "The traffic jams get worse", ["The traffic eases", "Nothing changes", "Roads close"], "더 심해진다."), M("Why are many housewives busy all day?", "They make food for the ancestral rituals", ["They work at offices", "They travel", "They sleep"], "제사 음식."), M("What does Mijin’s family do instead of traveling?", "Her parents come up to Seoul", ["They stay at a hotel", "They skip the holiday", "They visit a temple"], "서울로 올라오신다."), M("How does Mijin lessen the burden of preparing food?", "She orders the ritual food over the internet", ["She buys a restaurant", "She asks neighbors", "She cooks early"], "인터넷으로 주문."), M("What does the whole family do after the memorial service?", "Go to a resort and enjoy the break", ["Go to work", "Clean the tombs", "Hold a party at home"], "휴양지."), M("What is the 한국에서는 note’s ‘new trend’?", "Some elderly parents travel to their children’s city homes", ["Children travel more", "Fewer holidays", "No rituals"], "The book’s note."),
           F("명절 연휴가 짧으면 교통 ___이 더 심해진다. (jam)", "정체", ["풍속", "행렬"], "교통 정체."), F("많은 주부는 명절 연휴 ___ 바쁘다. (throughout)", "내내", ["마다", "까지"], "~ 내내."), F("음식을 준비하는 부담을 ___ 위해서 주문한다. (to lessen)", "덜기", ["더하기", "바꾸기"], "덜다."), F("설과 추석을 ___ 많은 사람이 고향을 방문한다. (on the occasion of)", "맞아서", ["맞춰서", "만나서"], "~을 맞아서."), F("차례를 지낸 후에는 온 가족이 ___에 가서 연휴를 즐긴다. (resort)", "휴양지", ["친정", "광장"], "휴양지."),
           read_q("설과 추석은 한국의 최대 민속 명절입니다"), read_q("귀성 차량이 많아서 길이 막혀요"), read_q("명절 풍경이 많이 바뀌고 있습니다"), read_q("제사 음식을 인터넷으로 주문합니다"), read_q("달라진 추석 풍경")]
    ),
)

# ================================================================== L4 Activities A
_NW = [
    ("명절 풍속이 바뀌고 있다.", "Holiday customs are changing."),
    ("명절 때 직접 음식을 하는 대신 전문업체에 주문하는 가정이 늘고 있다.", "The number of households that, instead of making the food themselves at holidays, order from a specialized company is increasing."),
    ("비용이 이십만 원쯤 들기 때문에 큰 부담이 되지는 않는다.", "Because the cost is about 200,000 won, it is not a big burden."),
    ("인터넷 주문도 가능하다.", "Internet orders are possible too."),
    ("또, 고속도로가 복잡해서 귀성을 포기하는 사람도 늘고 있다.", "Also, the number of people who give up going home because the highways are crowded is increasing."),
    ("이들은 고향에 가는 대신 해외여행을 가기도 한다.", "Instead of going to their hometowns, they sometimes go on overseas trips."),
    ("대전시의 한 여행사에 따르면 여름 휴가철 성수기보다 추석 연휴에 해외여행을 떠나는 사람이 더 많다고 한다.", "According to a travel agency in Daejeon City, more people leave on overseas trips during the Chuseok holiday than in the summer vacation peak season."),
    ("그리고 인기 해외여행 상품은 한두 달 전에 예약이 다 끝난다고 한다.", "And they say popular overseas travel packages are fully booked one or two months in advance."),
]
L4 = lesson(
    "Ch 44 · Activities A: changing holiday customs",
    "명절 풍속 · 전문업체 주문 · 해외여행 · 귀성 포기 · 달라진 명절",
    requires=[],
    cards=[
        card("Activity 3 (Reading): an online news article",
             "The following article is from an online news site. The book asks you to circle the best title and to list three supporting facts. The article is the book’s with the numbers spelled out; the English and the answers are mine.",
             examples=passage(_NW)),
        card("The answers (mine)", "1. The best title (of the book’s four choices: Traveling During Traditional Holidays; New Trends in Celebrating Traditional Holidays; Today’s Generation and Unique Lifestyle; Popularity of Virtual Shrines): New Trends in Celebrating Traditional Holidays. 2. Three supporting facts:",
             tables=[table(["#", "Fact (mine)"], [["1", "More households order holiday food from a specialized company instead of cooking it (about 200,000 won, internet orders possible)"], ["2", "More people give up going to their hometowns because the highways are crowded and go on overseas trips instead"], ["3", "More people leave for overseas trips during Chuseok than in the summer peak season, and popular tour packages are booked one or two months ahead"]])]),
        card("Activities left out", "Activity 1 (SMART Board), Activity 2 (listening to three conversations between a man and a woman discussing Chuseok, noting what the woman did and whether her experience was positive or negative with the reason) and Activity 4 (“누가 설을 더 잘 보냈어요?”: listening to two men explaining what they did on the Lunar New Year holiday, exchanging the information with a partner in Korean, deciding who had the better holiday, and writing about your own most memorable holiday) are audio, pair and group activities."),
    ],
    exercises=uniq(
        _tr(_NW, k=3)
        + [M("What is changing?", "Holiday customs", ["The weather", "The language", "The calendar"], "명절 풍속."), M("What are more households doing?", "Ordering holiday food from a specialized company", ["Cooking more", "Eating out", "Skipping meals"], "전문업체에 주문."), M("About how much does it cost?", "About 200,000 won", ["About 20,000 won", "About 2 million won", "Free"], "이십만 원쯤."), M("Why do some people give up going home?", "The highways are crowded", ["They dislike family", "It is too far", "It is too cold"], "고속도로가 복잡해서."), M("What do they do instead?", "Go on overseas trips", ["Stay home", "Go to work", "Hold rituals"], "해외여행."), M("When do more people leave on overseas trips?", "Chuseok holiday rather than summer peak season", ["Summer only", "New Year only", "Spring"], "추석 연휴."), M("When are popular tour packages booked?", "One or two months ahead", ["On the day", "A week ahead", "A year ahead"], "한두 달 전."),
           F("직접 음식을 하는 ___ 전문업체에 주문한다. (instead of)", "대신", ["때문", "동안"], "대신."), F("비용이 이십만 원쯤 ___ 때문에 큰 부담이 되지는 않는다. (costs)", "들기", ["내기", "하기"], "비용이 들다."), F("고속도로가 복잡해서 귀성을 ___하는 사람도 늘고 있다. (give up)", "포기", ["예상", "제외"], "포기."), F("여행사에 ___ 추석 연휴에 해외여행을 떠나는 사람이 더 많다. (according to)", "따르면", ["대하면", "바꾸면"], "~에 따르면."), F("인기 해외여행 ___은 예약이 다 끝난다고 한다. (package)", "상품", ["풍경", "차량"], "상품."),
           read_q("명절 풍속이 바뀌고 있습니다"), read_q("전문업체에 주문하는 가정이 늘고 있습니다"), read_q("귀성을 포기하는 사람도 늘고 있습니다"), read_q("해외여행을 가기도 합니다"), read_q("인터넷 주문도 가능합니다")]
    ),
)


# ================================================================== L5 Topic B
_B_DLG = [
    ("지훈", "지난 주말에 월드컵 예선전 봤어?", "Did you watch the World Cup preliminary match last weekend?"),
    ("선경", "응. 집에서 가족들하고 봤어. 후반전에 역전 골 넣을 때 너무 신 났어. 너도 봤어?", "Yes. I watched it at home with my family. When they scored the come-from-behind goal in the second half, I was so excited. Did you watch it too?"),
    ("지훈", "그럼. 난 시청 앞 광장에 가서 봤어. 응원하는 사람들이 아주 많았어.", "Of course. I went to the plaza in front of City Hall and watched. There were a great many people cheering."),
    ("선경", "와, 응원 열기가 대단했겠다. 스포츠 경기는 여러 사람이 같이 보면 더 재미있잖아.", "Wow, the cheering fever must have been tremendous. Sports games are more fun when many people watch together, you know."),
    ("지훈", "그렇지. 그리고 경기장에 직접 가서 보면 더 재미있고.", "Right. And it is even more fun to go to the stadium and watch in person."),
    ("선경", "맞아. 근데, 넌 스포츠 경기 보러 경기장에 자주 가?", "True. By the way, do you often go to the stadium to watch sports games?"),
    ("지훈", "응. 프로야구 보러 자주 가. 특히, 삼성 라이온스팀 경기는 어디서 하든지 경기장에 가서 응원해. 근데, 넌 무슨 스포츠를 좋아해?", "Yes. I often go to watch pro baseball. In particular, no matter where the Samsung Lions team plays, I go to the stadium and cheer. By the way, what sport do you like?"),
    ("선경", "난 동계 올림픽 종목들을 좋아해. 요즘 매일 동계올림픽 보고 있어.", "I like the Winter Olympics events. These days I watch the Winter Olympics every day."),
    ("지훈", "그렇구나. 요즘은 한국 선수들이 다양한 종목에서 메달을 따는 것 같아.", "I see. These days Korean athletes seem to win medals in a variety of events."),
    ("선경", "맞아. 예전에는 잘 못 했던 피겨 스케이팅까지도 잘하잖아.", "Right. They are even good at figure skating, which they could not do well before."),
    ("지훈", "그래. 요즘은 좋은 코치들이 많고 훈련도 체계적이어서 성적이 좋은 것 같아.", "Yes. These days there are many good coaches and the training is systematic, so the results seem good."),
    ("선경", "그리고 국민의 열광적인 응원도 큰 힘이 되는 것 같아.", "And the people’s enthusiastic cheering seems to be a great help too."),
]
_B_WORDS = ["경기장", "골(을) 넣다", "광장", "금/은/동", "대단하다", "대항", "동계", "메달", "본선", "스피드 스케이팅", "승리", "신(이) 나다", "아마추어", "어쨌든", "역전", "열광적", "열기", "예선", "올림픽", "월드컵", "응원", "전반전", "종목", "체계적", "코치", "프로", "피겨 스케이팅", "하계", "후반전"]
_SV = [
    ("한국인이 가장 관심 있는 스포츠 종목은 야구", "The sport Koreans are most interested in is baseball"),
    ("한국인이 가장 관심 있는 스포츠 종목은 야구, 축구, 골프 순으로 나타났다.", "The sports Koreans are most interested in turned out to be, in order, baseball, soccer and golf."),
    ("삼십 대 이하 젊은 세대들은 이스포츠에도 높은 관심을 보였다.", "The younger generations in their thirties and below also showed high interest in eSports."),
    ("정보분석기업 닐슨코리아가 공개한 조사 결과에 따르면 한국인의 절반이 넘는 육십이 점 영 퍼센트가 스포츠 종목 중 야구에 가장 관심이 많은 것으로 나타났고, 뒤를 이어 축구는 오십이 점 육 퍼센트, 골프는 삼십 점 구 퍼센트 순으로 높게 나타났다.", "According to the survey results released by the information analysis company Nielsen Korea, 62.0 percent, more than half of Koreans, showed the most interest in baseball among sports events, followed in order by soccer at 52.6 percent and golf at 30.9 percent."),
    ("수영 이십칠 퍼센트, 농구 이십육 점 구 퍼센트를 비롯해 게임 등 이스포츠 종목이 이십육 점 삼 퍼센트로 비교적 높은 지지를 얻은 가운데 사대 프로 스포츠 중 하나인 배구는 이십일 점 육 퍼센트로 십 위에 그쳤다.", "Including swimming at 27 percent and basketball at 26.9 percent, eSports events such as games gained comparatively high support at 26.3 percent, while volleyball, one of the four major pro sports, stopped at 10th place with 21.6 percent."),
    ("십오 세에서 이십구 세까지 젊은 층에서는 축구가 가장 높은 오십삼 점 이 퍼센트의 관심 종목으로 꼽혔고, 야구가 오십 점 팔 퍼센트로 이 위, 이스포츠가 삼십구 점 칠 퍼센트로 삼 위에 올랐다.", "Among the young group aged 15 to 29, soccer was picked as the sport of most interest at 53.2 percent, baseball was second with 50.8 percent, and eSports rose to third place with 39.7 percent."),
    ("닐슨코리아 측은 온라인 활용이 익숙한 밀레니얼 세대에서 쉽게 참여하고 관람할 수 있는 이스포츠의 관심이 높게 나타났다고 설명했다.", "The Nielsen Korea side explained that interest in eSports, which can be easily participated in and watched, turned out high in the Millennial generation, which is used to online use."),
]
L5 = lesson(
    "Ch 44 · Topic B: Let’s go cheer for the Korean team! (한국팀 응원하러 가자)",
    "월드컵 · 예선 · 응원 · 광장 · 경기장 · 동계 올림픽 · 피겨 스케이팅 · 길거리 응원",
    requires=[],
    cards=[
        card("Topic B: Let’s go cheer for the Korean team! (한국팀 응원하러 가자)",
             "Two friends are talking about sports events. (The English is mine; the book gives none; the book’s “!” in the title is dropped. The book’s footnote: 메달을 따다 [to win a medal] literally means “to pick a medal.” The speaker labels of the book’s last four lines are garbled in the printed text; I assign them alternately.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists ~까지(도) and –든지 (see the grammar). 금/은/동 are gold/silver/bronze.", tables=_words(_B_WORDS)),
        card("한국에서는: 길거리 응원 “대~한민국”",
             "길거리 응원 (street cheering) has been a prominent feature of Korean cheering culture since the 2002 FIFA World Cup. During that event, when the Korean soccer team advanced to the semifinals, 2.4 million Koreans gathered on the streets of major cities and rooted for the Korean team while watching the game on giant TV screens. They all wore red T-shirts and chanted 대~한민국, immediately followed by rhythmic claps. Since that historic moment, Koreans have been organizing street cheering for big sports events such as 월드컵, 올림픽, and the World Baseball Classic. This phenomenon has become a part of contemporary Korean culture. (The book has a link to a YTN video of 길거리 응원, which is left out.)"),
        card("북한에서는: 북한 스포츠",
             "North Korea’s most popular participatory sports are soccer, basketball, and table tennis. North Koreans organize school, factory, and cooperative farm sports teams and enjoy leisure time games. Soccer is the most popular sport for participants and spectators. North Koreans especially remember how in 1966 the North Korean soccer team miraculously advanced to the quarterfinals during the FIFA World Cup in England. However, the women’s soccer team has been more successful on the international stage than the men’s, qualifying for the 1999 and 2003 FIFA Women’s World Cup. In 1999, the team defeated Denmark during the group stage, and in 2003 defeated Nigeria, the champion team from Africa. Boxing and marathon events are also popular spectator sports. There are North Korean professional boxing and wrestling leagues."),
        card("Follow-up 2 (Reading): a survey about sports",
             "The following news article is about a survey and its results about sports; the book asks three questions in English (the survey topic; a short summary of the results; which age group showed the highest interest in ‘eSports’ and the contributing factor). The article is the book’s with the numbers spelled out (the book’s parentheses around the percents are read as part of the sentence, and ‘e스포츠’ is written 이스포츠); the English and the answers are mine.",
             examples=passage(_SV)),
        card("The answers (mine)", "",
             tables=[table(["Question", "Answer (mine)"], [["1. What is the survey topic?", "Which sports events Koreans are most interested in"], ["2. A short summary of the results", "Baseball ranked first (62.0%), followed by soccer (52.6%) and golf (30.9%); then swimming (27%), basketball (26.9%) and eSports (26.3%); volleyball was 10th (21.6%). Among ages 15–29, soccer was first (53.2%), baseball second (50.8%) and eSports third (39.7%)"], ["3. Which age group showed the highest interest in eSports, and why?", "The younger generations (thirties and below, especially the Millennials); they are used to using online media, and eSports are easy to take part in and watch"]])]),
        card("Activities left out", "The presentation steps of Topic B (two SMART Board activities, reading and listening along, reviewing with the teacher) and Follow-up 1 (listening to four conversations in which two friends talk about recent sports events and filling in the name of the event, the sport and the result) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG) + _SV, k=3)
        + [M("What did Seonggyeong watch last weekend?", "A World Cup preliminary match", ["A baseball final", "A concert", "A movie"], "월드컵 예선전."), M("Where did Jihun watch it?", "At the plaza in front of City Hall", ["At home", "At the stadium", "At a cafe"], "시청 앞 광장."), M("What does Jihun often go to watch?", "Pro baseball", ["Soccer", "Golf", "Figure skating"], "프로야구."), M("What does Jihun do for the Samsung Lions?", "Goes to the stadium and cheers wherever they play", ["Watches on TV only", "Ignores them", "Plays for them"], "어디서 하든지."), M("What sports does Seonggyeong like?", "Winter Olympic events", ["Summer Olympic events", "Baseball", "Boxing"], "동계 올림픽 종목들."), M("Why do Korean athletes do well now?", "Good coaches, systematic training and enthusiastic cheering", ["Luck", "Money only", "Fewer teams"], "코치, 훈련, 응원."), M("When did 길거리 응원 become prominent?", "Since the 2002 FIFA World Cup", ["Since 1966", "Since 1988", "Since 2018"], "The book’s note."), M("Which sport ranked first in the survey?", "Baseball", ["Soccer", "Golf", "Swimming"], "야구 62.0%."),
           F("후반전에 ___ 골 넣을 때 너무 신 났어. (come-from-behind)", "역전", ["예선", "대항"], "역전."), F("응원 ___가 대단했겠다. (fever)", "열기", ["종목", "광장"], "열기."), F("한국 선수들이 다양한 종목에서 ___을 따는 것 같아. (medals)", "메달", ["코치", "본선"], "메달."), F("훈련도 ___이어서 성적이 좋은 것 같아. (systematic)", "체계적", ["열광적", "안정적"], "체계적."), F("월드컵 ___전을 집에서 가족들하고 봤어. (preliminary)", "예선", ["본선", "후반"], "예선전."),
           read_q("한국팀 응원하러 가자"), read_q("지난 주말에 월드컵 예선전 봤어"), read_q("시청 앞 광장에 가서 봤어"), read_q("응원 열기가 대단했겠다"), read_q("한국 선수들이 다양한 종목에서 메달을 따는 것 같아")]
    ),
)

# ================================================================== L6 Activities B
_QT = [
    ("한국 이 대 일 역전승으로 월드컵 십육 강 진출", "Korea advances to the World Cup round of 16 with a 2–1 come-from-behind victory"),
    ("어제 카타르에서 월드컵 에이치 조 조별리그가 열렸다.", "Yesterday the World Cup Group H group stage was held in Qatar."),
    ("이날 한국 축구 대표팀은 포르투갈을 이 대 일로 이기면서 월드컵 십육 강 진출에 성공했다.", "On this day, the Korean national soccer team beat Portugal 2–1 and succeeded in advancing to the World Cup round of 16."),
    ("이 경기에서 한국은 전반 오 분 영 대 일로 지고 있었지만, 전반 이십칠 분 김영권이 골을 넣어 일 대 일로 만들었다.", "In this game, Korea was losing 0–1 in the 5th minute of the first half, but in the 27th minute Kim Youngkwon scored a goal and made it 1–1."),
    ("후반전에서 한국은 좀처럼 골을 넣을 기회를 만들지 못하다가 황희찬의 정확하고 화끈한 슈팅으로 이 대 일로 역전승을 거뒀다.", "In the second half, Korea could hardly create chances to score, but then achieved a 2–1 come-from-behind victory with Hwang Heechan’s accurate and fiery shot."),
    ("이로써 대표팀은 월드컵 십육 강에 진출하게 됐다.", "With this, the national team came to advance to the World Cup round of 16."),
    ("이천십 년 남아공 월드컵 이후 십이 년 만이다.", "It is the first time in twelve years since the 2010 South Africa World Cup."),
    ("골을 넣은 두 선수도 잘했지만, 한국 팀의 체계적인 플레이가 가장 큰 역할을 하였다.", "The two players who scored did well, but the Korean team’s systematic play played the biggest role."),
    ("특히 한국 공식 축구 응원단인 붉은 악마는 먼 카타르까지 가서 한국 선수들을 응원했다.", "In particular, the Red Devils, Korea’s official soccer cheering squad, went all the way to distant Qatar and cheered for the Korean players."),
    ("이들은 붉은 악마의 상징인 빨간색 티셔츠를 입고 다 같이 대한민국, 오 필승 코리아를 외치면서 열광적인 응원을 보여 주었다.", "Wearing the red T-shirts that are the Red Devils’ symbol, they all together shouted “Daehanminguk” and “Oh Victorious Korea” and showed enthusiastic cheering."),
    ("한편 한국은 이번 월드컵에서 아시아 국가로는 처음으로, 전 세계에서는 여섯 번째로 십 회 연속 월드컵 본선 진출이라는 대기록을 세웠다.", "Meanwhile, Korea set the great record of advancing to the World Cup finals ten times in a row, the first among Asian countries and the sixth in the whole world."),
]
L6 = lesson(
    "Ch 44 · Activities B: a World Cup match in the news",
    "월드컵 십육 강 · 역전승 · 붉은 악마 · 열광적인 응원 · 십 회 연속 본선 진출",
    requires=[],
    cards=[
        card("Activity 3 (Listening and reading): a sports news article",
             "In this activity you learn about a sports event through two sources of news. In step a, you read the following excerpt from a newspaper sports section and fill in a table in English (type of event; event result; what fans did). The excerpt is the book’s with the numbers and letters spelled out (the title’s “!” is dropped; “H조” is 에이치 조; the book’s quoted chants are written without the quotation marks and the wave sign); the English is mine.",
             examples=passage(_QT)),
        card("The table filled in (mine)", "",
             tables=[table(["Column", "Answer (mine)"], [["Type of event", "A FIFA World Cup group-stage match (Group H) in Qatar: Korea vs. Portugal"], ["Event result", "Korea won 2–1 in a come-from-behind victory (down 0–1 in the 5th minute; Kim Youngkwon equalized in the 27th minute; Hwang Heechan scored the winner in the second half) and advanced to the round of 16 for the first time in 12 years; it was also Korea’s 10th consecutive World Cup finals"], ["What fans did", "The Red Devils traveled to Qatar, wore red T-shirts and chanted “대한민국” and “오 필승 코리아”"]])]),
        card("Step b: the radio news", "In step b you listen to a radio news report about the soccer game and add new information that was not in step a to the table in English. This is an audio activity and is left out."),
        card("Activity 4 (Speaking and listening): I went to a baseball game",
             "With your classmates you share experiences you have had while attending sports events: you think of two sports events you attended and write briefly in English (the name of the sport, the team or player, the result, what the fans did); you meet three classmates and talk about your experiences in Korean; each of you then picks the most interesting of your friends’ experiences and presents it in Korean (the book’s title is 야구 경기에 다녀왔어요). This is a pair and group activity and is left out."),
        card("Activities left out", "Activity 1 (SMART Board) and Activity 2 (listening to three conversations about recent international sports events that Korea participated in, checking Summer Olympics: Swimming, Winter Olympics: Speed Skating or FIFA World Cup, and filling in the other information and the result) are audio and computer activities."),
    ],
    exercises=uniq(
        _tr(_QT, k=3)
        + [M("Where was the World Cup match held?", "Qatar", ["South Africa", "Korea", "England"], "카타르."), M("Whom did Korea beat?", "Portugal", ["Spain", "Brazil", "Japan"], "포르투갈."), M("What was the final score?", "2–1", ["1–1", "0–1", "3–2"], "이 대 일."), M("Who made it 1–1?", "Kim Youngkwon", ["Hwang Heechan", "Son Heungmin", "Lee Gangin"], "김영권."), M("Whose shot gave Korea the winning goal?", "Hwang Heechan", ["Kim Youngkwon", "Park Jisung", "Cha Bumkun"], "황희찬."), M("When had Korea last reached the round of 16?", "Twelve years earlier (2010)", ["Twenty years earlier", "Last year", "Never"], "십이 년 만."), M("Who are the 붉은 악마?", "Korea’s official soccer cheering squad", ["A professional team", "A rock band", "A TV station"], "공식 응원단."), M("What record did Korea set?", "Ten consecutive World Cup finals appearances", ["Most goals", "First Asian champion", "Longest winning streak"], "십 회 연속 본선 진출."),
           F("한국은 전반 오 분 영 대 일로 ___ 있었다. (losing)", "지고", ["이기고", "비기고"], "지다."), F("후반전에 이 대 일로 ___승을 거뒀다. (come-from-behind)", "역전", ["예선", "대항"], "역전승."), F("한국 팀의 ___인 플레이가 가장 큰 역할을 하였다. (systematic)", "체계적", ["열광적", "현실적"], "체계적."), F("붉은 악마는 먼 카타르까지 가서 선수들을 ___했다. (cheered)", "응원", ["코치", "제외"], "응원하다."), F("한국은 월드컵 ___ 진출이라는 대기록을 세웠다. (finals)", "본선", ["예선", "하계"], "본선."),
           read_q("한국 이 대 일 역전승"), read_q("월드컵 십육 강 진출에 성공했습니다"), read_q("붉은 악마는 카타르까지 가서 응원했습니다"), read_q("열광적인 응원을 보여 주었습니다"), read_q("십 회 연속 월드컵 본선에 진출했습니다")]
    ),
)


# ================================================================== L7 Grammar A: -든(지)
_DJ1 = [("주말에 친구를 만나든지 영화를 봅니다.", "I see my friends or see a movie on weekends.")]
_DJ2 = [("무슨 언어를 배우든지 열심히 배우세요.", "No matter what language you learn, please learn (the language) diligently."), ("언제 미국에 오시든지 저희 집에 들러주세요.", "No matter when you come to the States, please visit my home.")]
_DJ3 = [("누구를 만나든지 친절하게 대하세요.", "No matter whom we meet, please treat them kindly."), ("어디서 살든지 행복하세요.", "Be happy wherever you live."), ("무엇을 하든지 열심히 하면 돼.", "Work hard, no matter what you do."), ("어떻게 하든지 이 일을 끝내기만 하세요.", "Finish this work, no matter how you do it.")]
_DJ4 = [("누가 읽든지 이 책은 재미있을 거예요.", "No matter who reads it, this book will be fun."), ("무엇을 먹든지 건강하게 드세요.", "No matter what you eat, eat healthily."), ("어디에서 만나든지 좋아요.", "It’s fine no matter where we meet."), ("언제 운동하든지 준비 운동을 먼저 하세요.", "No matter when you exercise, do warm-up exercises first."), ("어떻게 근무하든지 안전이 가장 중요합니다.", "No matter how you work, safety is the most important."), ("무슨 일을 하든지 최선을 다하세요.", "No matter what job you do, do your best."), ("어떤 사람이든지 처음에는 서투릅니다.", "No matter what kind of person, everyone is clumsy at first.")]
L7 = lesson(
    "Ch 44 · Grammar A: interrogative word + –든(지), no matter who/what/when",
    "-든지 · -든 · 누구를 만나든지 · 어디서 살든지 · 무엇을 하든지 · 어떻게 하든지",
    requires=[],
    cards=[
        card("Expressing “no matter who/whom/what/when,” etc.",
             "Recall the conjunctive ending –든지 you learned about in Chapter 22. This conjunctive ending is used to express an alternative option, as in 주말에 친구를 만나든지 영화를 봅니다 (I see my friends or see a movie on weekends). However, when the conjunctive ending –든지 is preceded by an interrogative word, such as 누구, 무엇, 언제, 어디, and 어떻게, it expresses no matter who/whom/what/when/where/how. For example:",
             examples=passage(_DJ1 + _DJ2)),
        card("The pattern",
             "지 in 든지 can be omitted (the book writes 든(지)). “no matter who/whom/what/when/where/how”: interrogative word + … + –든(지). More examples (the English is the book’s; I write 든지 in full):",
             examples=passage(_DJ3)),
        card("Follow-up 1 (Writing): four sentences",
             "Using the words from the table (interrogative words 누구/누가, 무엇, 어디(에/서), 언제, 어떻게, 무슨 ~, 어떤 ~; verbs 읽다, 먹다, 만나다, 운동하다, 근무하다, 일하다), write four sentences in Korean that express “no matter who/whom/what/where,” etc. and translate them into English. The book’s model is 어디서 일하든지 열심히 노력하세요 (Make an effort, no matter where you work). My own sentences (the English is mine):",
             examples=passage([("어디서 일하든지 열심히 노력하세요.", "Make an effort, no matter where you work.")] + _DJ4)),
        card("Activities left out", "Follow-up 2 (listening to four conversations between two friends and translating the sentence containing –든(지) into English) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_DJ1 + _DJ2 + _DJ3 + _DJ4, k=3)
        + [M("What does 주말에 친구를 만나든지 영화를 봅니다 mean?", "I see my friends or see a movie on weekends", ["No matter whom I meet", "I never go out", "I see friends and a movie together"], "Alternative use."), M("What does an interrogative word + –든(지) express?", "no matter who/what/when/where/how", ["an alternative option", "a past event", "a wish"], "The book’s note."), M("What can be omitted from 든지?", "지", ["든", "ㄴ", "Nothing"], "든(지)."), M("What does 무슨 언어를 배우든지 열심히 배우세요 mean?", "No matter what language you learn, learn it diligently", ["Learn only one language", "Do not learn languages", "Learn a language or work"], "The book’s example."), M("What does 어디서 살든지 행복하세요 mean?", "Be happy wherever you live", ["Live somewhere happy", "Be happy and live", "Do not move"], "The book’s example."), M("Which word means ‘no matter how’?", "어떻게 하든지", ["어디서 하든지", "누구를 하든지", "무엇을 하든지"], "어떻게."),
           F("무슨 언어를 배우___ 열심히 배우세요. (no matter)", "든지", ["는데", "니까"], "-든지."), F("언제 미국에 오시___ 저희 집에 들러주세요. (no matter when)", "든지", ["는데", "면서"], "-든지."), F("누구를 ___든지 친절하게 대하세요. (meet)", "만나", ["만난", "만날"], "만나든지."), F("어디서 ___든지 행복하세요. (live)", "살", ["사는", "산"], "살든지."), F("___ 하든지 이 일을 끝내기만 하세요. (how)", "어떻게", ["어디서", "누구를"], "어떻게."),
           read_q("무슨 언어를 배우든지 열심히 배우세요"), read_q("언제 미국에 오시든지 저희 집에 들러주세요"), read_q("누구를 만나든지 친절하게 대하세요"), read_q("어디서 살든지 행복하세요"), read_q("무엇을 하든지 열심히 하면 돼")]
    ),
)

# ================================================================== L8 Grammar B: ~까지(도)
_GG1 = [("어젯밤에 열두 시까지 숙제 했어요.", "I did homework until 12 o’clock last night."), ("여기서 학교까지 삼십 분 걸려요.", "It takes 30 minutes (to travel) from here to school.")]
_GG2 = [("배가 너무 고파서 디저트까지 다 먹었어요.", "I was so hungry I even ate dessert."), ("다음 주 숙제까지 했습니다.", "I even did next week’s homework (not to mention this week’s homework).")]
_GG3 = [("배가 너무 고파서 디저트까지도 다 먹었어요.", "I was so hungry I even ate dessert."), ("다음 주 숙제까지도 했습니다.", "I even did next week’s homework.")]
_GG4 = [("어린 아이들까지도 거리에 나와서 한국 팀을 응원했어요.", "Even young children came out to the street to cheer for the Korean team."), ("어제 백화점에서 옷이랑 신발을 샀어요. 게다가 핸드백까지 샀어요.", "I bought clothes and shoes at the department store yesterday. And I even bought a purse."), ("하루 종일 요리하고 설거지했어요. 게다가 집 청소까지 했어요.", "All day long I cooked and washed the dishes. In addition, I even cleaned the house.")]
_GGJ = [("최근에 새집으로 이사를 해서 어제 집들이를 했다.", "I recently moved into a new house, so I had a housewarming party yesterday."), ("친구들을 많이 초대했기 때문에 하루 종일 아주 바빴다.", "Because I invited many friends, I was very busy all day."), ("아침 일찍부터 집 안 청소를 하고 음식을 준비했다.", "From early in the morning I cleaned the house and prepared food."), ("그리고 예쁘게 집안 장식까지 했다.", "And I even decorated the house prettily."), ("음식도 여러 가지 떡과 불고기와 잡채 그리고 파전까지도 준비했다.", "As for food, I prepared various rice cakes, bulgogi, japchae and even green onion pancakes."), ("힘들었지만 친구들이 음식을 맛있게 먹어서 기분이 좋았다.", "It was hard, but I felt good because my friends ate the food with relish.")]
_GGC = [("김 일병은 노래를 잘해요.", "PFC Kim sings well."), ("그리고 춤도 잘 춰요.", "And he dances well too."), ("그리고 요리까지 잘해요.", "And he even cooks well."), ("김 일병은 운동을 잘해요.", "PFC Kim is good at sports."), ("그리고 공부도 열심히 해요.", "And he studies hard too."), ("게다가 친구들까지 잘 도와줘요.", "On top of that, he even helps his friends well.")]
L8 = lesson(
    "Ch 44 · Grammar B: ~까지(도), even",
    "~까지 · ~까지도 · 디저트까지 먹었어요 · 게다가 핸드백까지 샀어요 · 집들이 · 칭찬",
    requires=[],
    cards=[
        card("Recall ~까지",
             "Recall the meanings of ~까지. When attached to a noun indicating time or place, ~까지 can be translated as until, up to, or by. When attached to a noun indicating place, it can be translated as (up) to or as far as. For example:",
             examples=passage(_GG1)),
        card("~까지 for “even”",
             "However, when ~까지 is attached to a noun other than one indicating time or place, it is used to stress an extreme or highly unlikely condition, and it can be translated as even or to a degree that extends. For example:",
             examples=passage(_GG2)),
        card("~까지도",
             "In these instances, ~까지 is interchangeable with ~까지도. For example:",
             examples=passage(_GG3)),
        card("More examples (“even”: ~까지(도))", "The English is the book’s.", examples=passage(_GG4)),
        card("Follow-up 3 (Reading): a journal entry about a housewarming party",
             "The following journal entry is about a housewarming party hosted by So-yeon (소연). The passage is the book’s; the English and the answers are mine.",
             examples=passage(_GGJ)),
        card("The answers (mine)", "",
             tables=[table(["Column", "Answer (mine)"], [["Household chores completed", "Cleaned the house; decorated the house"], ["Foods So-yeon prepared", "Various rice cakes (떡); bulgogi; japchae; green onion pancakes"], ["b. Sentences with ~까지", "그리고 예쁘게 집안 장식까지 했다 = “And I even decorated the house prettily.” 파전까지도 준비했다 = “(I prepared …) and even green onion pancakes.”"]])]),
        card("Follow-up 5 (Speaking): Let’s give compliments!",
             "Each student writes the names of four people both partners know on index cards and thinks of compliments for each. Partner A states a compliment, Partner B states another compliment, and Partner A adds a final compliment using ~까지(도). The book’s model is A: 김 일병은 노래를 잘해요. B: 그리고 춤도 잘 춰요. A: 그리고/게다가 요리까지 잘해요. My own second round (the English is mine):",
             examples=passage(_GGC)),
        card("Activities left out", "Follow-up 4 (listening to four conversations between two friends, transcribing ~까지 and translating the sentences that contain ~까지) is an audio activity; the pair activity of Follow-up 5 is a speaking game."),
    ],
    exercises=uniq(
        _tr(_GG1 + _GG2 + _GG3 + _GG4 + _GGJ + _GGC, k=3)
        + [M("What does ~까지 mean after a noun of time or place?", "until; up to; by; as far as", ["even", "only", "also"], "The book’s note."), M("What does ~까지 mean after other nouns?", "even; to a degree that extends", ["until", "only", "because"], "The book’s note."), M("What does ~까지 stress?", "An extreme or highly unlikely condition", ["A wish", "A reason", "A past time"], "The book’s note."), M("Which can replace ~까지 in the ‘even’ meaning?", "~까지도", ["~만", "~부터", "~마다"], "The book’s note."), M("What does 디저트까지 다 먹었어요 mean?", "I even ate dessert", ["I ate until dessert", "I did not eat dessert", "I ate only dessert"], "The book’s example."), M("What does 핸드백까지 샀어요 mean?", "I even bought a purse", ["I bought only a purse", "I went to the purse", "I did not buy a purse"], "The book’s example."), M("What does 여기서 학교까지 삼십 분 걸려요 mean?", "It takes 30 minutes from here to school", ["School is 30 minutes long", "I study until school", "Even school takes 30 minutes"], "Place use."), M("What did So-yeon do besides cleaning and food?", "Decorate the house", ["Paint the house", "Move out", "Cook alone"], "집안 장식까지."),
           F("배가 너무 고파서 디저트___ 다 먹었어요. (even)", "까지", ["부터", "마다"], "~까지."), F("다음 주 숙제___ 했습니다. (even)", "까지도", ["만", "에서"], "~까지도."), F("어린 아이들까지도 거리에 나와서 한국 팀을 ___. (cheered)", "응원했어요", ["코치했어요", "제외했어요"], "응원하다."), F("하루 종일 요리하고 설거지했어요. ___ 집 청소까지 했어요. (in addition)", "게다가", ["그러나", "그래서"], "게다가."), F("여기서 학교___ 삼십 분 걸려요. (to)", "까지", ["부터", "마다"], "~까지."),
           read_q("배가 너무 고파서 디저트까지 다 먹었어요"), read_q("다음 주 숙제까지도 했습니다"), read_q("어린 아이들까지도 거리에 나와서 응원했어요"), read_q("게다가 핸드백까지 샀어요"), read_q("파전까지도 준비했다")]
    ),
)


# ================================================================== L9 Topic C
_C_DLG = [
    ("경철", "영희야, 너는 장래 희망이 뭐야?", "Yeonghui, what is your hope for the future?"),
    ("영희", "나는 수의사가 되고 싶어. 어렸을 때부터 동물을 좋아했거든. 부모님도 찬성하셨어. 너는 뭐가 되고 싶어?", "I want to become a veterinarian. I have liked animals since I was little. My parents agreed too. What do you want to become?"),
    ("경철", "탤런트가 되는 게 내 꿈이야.", "Becoming a TV actor is my dream."),
    ("영희", "탤런트? 경쟁이 심해서 탤런트 되기가 어렵다고 하던데.", "A TV actor? I heard that the competition is fierce, so it is hard to become one."),
    ("경철", "알고 있어. 그래서 연기학원에 다니고 대학은 연극영화과에 진학할 생각이야. 목표를 정했으니까 노력해야지.", "I know. So I attend an acting academy and plan to go on to the theater and film department at university. Since I have set my goal, I have to make an effort."),
    ("영희", "현실적으로 생각해 봐. 유명한 일부 스타를 제외하고는 대부분 연예인들이 돈을 별로 못 벌잖아.", "Think realistically. Except for some famous stars, most entertainers do not make much money, you know."),
    ("경철", "돈도 중요하지만 내가 원하는 일을 하고 싶어.", "Money is important too, but I want to do the work I want."),
    ("영희", "부모님은 뭐라고 하셔?", "What do your parents say?"),
    ("경철", "어머니는 내가 안정적인 직업을 갖기를 원하셔. 하지만, 아버지는 내 의사가 더 중요하니까 괜찮다고 하셨어.", "My mother wants me to have a stable job. But my father said it is fine since my own intention is more important."),
    ("영희", "나도 본인의 의사가 중요하다고 생각해.", "I think one’s own intention is important too."),
]
_C_WORDS = ["경쟁", "(대)답", "디자이너", "목표", "본인", "소득", "소질", "수의사", "스타", "안정(적)", "연기", "연예인", "의사", "이루다", "장래", "재능", "제외", "탤런트", "프로게이머", "허락", "현실(적)"]
_SUF = [("회사원", "a company employee"), ("공무원", "a public servant"), ("연구원", "a researcher"), ("음악가", "a musician"), ("화가", "a painter"), ("사업가", "a businessman"), ("의사", "a doctor"), ("교사", "a teacher"), ("약사", "a pharmacist"), ("변호사", "a lawyer")]
L9 = lesson(
    "Ch 44 · Topic C: I want to be an entertainer (저는 연예인이 되고 싶어요)",
    "장래 희망 · 수의사 · 탤런트 · 연기학원 · 경쟁 · 안정적인 직업 · ~원 ~가 ~사",
    requires=[],
    cards=[
        card("Topic C: I want to be an entertainer (저는 연예인이 되고 싶어요)",
             "Two teenagers are talking about their future careers. (The English is mine; the book gives none; the book’s “…” is dropped. The book’s footnotes: 장래 is pronounced /장내/. 본인 means oneself, the person himself, or the person in question, depending on the context.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists –(으)ㄹ 때부터 (since; from the time when, see the time-reference summary).", tables=_words(_C_WORDS)),
        card("한국어에는: ~원, ~가, ~사",
             "The Korean suffixes ~원 (員), ~가 (家), or ~사 (士/師) are commonly used to refer to a person who is working in a certain occupation. When referring to a specific job category, ~원 usually denotes a person who is working as a member of an organization or group. Some examples of this usage are 회사원 (a company employee), 공무원 (a public servant), 연구원 (a researcher), etc. ~가 is often used to describe a person who works as a professional (especially in the arts) or has expert knowledge or skills in a certain field. Examples are 음악가 (a musician), 화가 (a painter), 사업가 (a businessman), etc. ~사 often describes an officially certified professional in a certain field, such as 의사 (a doctor), 교사 (a teacher), 약사 (a pharmacist), or 변호사 (a lawyer).",
             tables=[ktable(_SUF)]),
        card("Activities left out", "The presentation steps of Topic C (SMART Board activities, reading and listening along, reading the dialog aloud in pairs and swapping roles, reviewing with the teacher) are computer, audio and pair activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG) + _SUF, k=3)
        + [M("What does Yeonghui want to become?", "A veterinarian", ["A TV actor", "A designer", "A teacher"], "수의사."), M("Why does she want to be one?", "She has liked animals since she was little", ["Her parents forced her", "It pays well", "A friend suggested it"], "어렸을 때부터 동물을 좋아했거든."), M("What is Gyeongcheol’s dream?", "To become a TV actor", ["To be a doctor", "To be a lawyer", "To be a pilot"], "탤런트."), M("What does he plan to do?", "Attend an acting academy and enter a theater and film department", ["Study law", "Start a company", "Join the army"], "연기학원, 연극영화과."), M("What does Yeonghui say about most entertainers?", "They do not make much money", ["They are rich", "They are happy", "They are lazy"], "돈을 별로 못 벌잖아."), M("What does his mother want?", "A stable job for him", ["A famous son", "A doctor", "A move abroad"], "안정적인 직업."), M("What does his father say?", "His own intention is more important", ["He must stop", "He must study", "He must wait"], "내 의사가 더 중요."), M("Which suffix describes a member of an organization?", "~원", ["~가", "~사", "~자"], "회사원."), M("Which suffix describes artistic professionals?", "~가", ["~원", "~사", "~자"], "음악가, 화가."), M("Which suffix describes officially certified professionals?", "~사", ["~원", "~가", "~자"], "의사, 변호사."),
           F("나는 ___가 되고 싶어. 동물을 좋아하거든. (veterinarian)", "수의사", ["탤런트", "디자이너"], "수의사."), F("경쟁이 심해서 ___ 되기가 어렵다고 하던데. (TV actor)", "탤런트", ["수의사", "프로게이머"], "탤런트."), F("유명한 일부 스타를 ___하고는 돈을 별로 못 벌잖아. (except)", "제외", ["포함", "허락"], "제외."), F("어머니는 내가 ___ 직업을 갖기를 원하셔. (stable)", "안정적인", ["현실적인", "열광적인"], "안정적."), F("아버지는 내 ___가 더 중요하다고 하셨어. (intention)", "의사", ["소득", "재능"], "의사."),
           read_q("나는 수의사가 되고 싶어"), read_q("탤런트가 되는 게 내 꿈이야"), read_q("현실적으로 생각해 봐"), read_q("어머니는 내가 안정적인 직업을 갖기를 원하셔"), read_q("본인의 의사가 중요하다고 생각해")]
    ),
)

# ================================================================== L10 Activities C: job preferences
_HS = [
    ("교육부와 한국직업연구원이 전국 고등학생 칠천백이십사 명에게 직업 선호도를 조사했다.", "The Ministry of Education and the Korea Research Institute for Vocational Education and Training surveyed 7,124 high school students nationwide on job preferences."),
    ("이 결과에 따르면 학생들이 가장 희망하는 직업은 교사였고, 그다음이 간호사였다.", "According to this result, the job students hoped for most was teacher, followed by nurse."),
    ("학생이 희망하는 직업 삼 위는 군인으로, 일 위에서 삼 위는 작년과 변함이 없었다.", "Third place among jobs students hope for was soldier, and first to third places were unchanged from last year."),
    ("그 밖에 경찰관이나 수사관, 컴퓨터공학자나 소프트웨어개발자, 뷰티디자이너 등이 높은 순위였다.", "In addition, police officer or investigator, computer scientist or software developer, and beauty designer ranked high."),
    ("이들 직업을 선택한 이유를 묻는 질문에 본인이 하고 싶어하는 일이기 때문이라고 대답했다.", "Asked the reason for choosing these jobs, they answered that it is because it is work they themselves want to do."),
    ("이십 년 전에는 학생들이 장래 직업으로 의사를 가장 많이 선택했었고, 이 위와 삼 위는 각각 교수와 변호사였었다.", "Twenty years ago, students chose doctor most as a future job, and second and third places were professor and lawyer, respectively."),
    ("한편 졸업 후 창업을 희망하는 학생은 꾸준히 늘어나는 것으로 조사됐다.", "Meanwhile, the survey found that the number of students hoping to start a business after graduation is steadily increasing."),
]
_DB1 = [
    ("나는 건설 현장에서 일하는 도배사이다.", "I am a wallpaper installer who works at construction sites."),
    ("최근 건설 현장에는 나뿐만 아니라 다양한 분야에 다양한 이유로 일을 하는 젊은이들이 많다.", "Recently, at construction sites there are many young people, not only me, working in various fields for various reasons."),
    ("부모님을 따라 시작한 경우도 있고, 대기업에 다니다가 퇴사하고 마음 편한 일을 하고 싶어 시작한 사람도 있다.", "There are cases of starting by following their parents, and there are also people who left a large company and started because they wanted to do work that is easy on the mind."),
    ("나의 경우에는 취업할 때 여러 선택지가 있었다.", "In my case, I had several options when I got a job."),
    ("하지만 수량과 품질로 명확하게 인정받을 수 있는, 오로지 기술로만 인정받을 수 있는 직업을 택하고 싶었다.", "But I wanted to choose a job in which I could be clearly recognized by quantity and quality, recognized solely by skill."),
    ("높은 연봉, 안정성, 사회적 지위 등 많은 사람들이 중요하게 생각하는 기준이 아니라 나만의 기준을 세워서 직업을 선택하고 싶었다.", "I wanted to choose a job by setting my own standards, not the standards many people consider important, such as high salary, stability and social status."),
    ("그렇게 찾은 직업이 도배사였다.", "The job I found that way was wallpaper installer."),
]
_DB2 = [
    ("과거와 다르게 많은 청년들이 다양한 선택을 하는 이유는, 사회가 정해놓은 인생의 틀을 그대로 따라갈지 그러지 않을지의 차이일 것이다.", "The reason many young people make various choices, unlike in the past, is probably the difference in whether they follow the frame of life set by society as it is or not."),
    ("대학 졸업, 취업, 결혼, 출산, 육아가 기성세대에게는 클리어, 곧 완수해야 하는 하나의 미션, 곧 과제였다면, 요즘의 청년들에게는 하나의 옵션, 곧 선택일 뿐이다.", "If graduating from university, getting a job, marriage, childbirth and child-rearing were a ‘mission’, something to ‘clear’ (that is, to complete), for the older generation, for young people today they are only an ‘option’ (that is, a choice)."),
    ("그렇기 때문에 결혼과 출산, 육아하기 좋은 안정적인 직업을 고를 수도 있지만, 그것들을 하지 않을 사람들은 좀 더 자유로운 선택을 하기도 한다.", "That is why they may pick a stable job good for marriage, childbirth and child-rearing, but people who will not do those things sometimes make a freer choice."),
]
_DB3 = [
    ("요즘 청년들은 스스로 중요하게 생각하는 믿음과 가치를 토대로 직업을 선택한다.", "Young people today choose jobs based on the beliefs and values they consider important themselves."),
    ("하지만 이런 생각을 이해하지 못하고 본인만의 기준으로 좋은 직업과 안 좋은 직업을 나누는 기성세대가 많다.", "But there are many in the older generation who do not understand this thinking and divide ‘good jobs’ and ‘bad jobs’ by their own standards."),
    ("내게도 좋은 대학 나왔으면 공무원을 하지 왜 도배를 하느냐는 얘기를 하는 사람들도 있다.", "There are even people who tell me, “If you graduated from a good university, you should be a public servant; why do wallpapering?”"),
    ("언젠가는 청년들이 다양한 생각과 판단을 통해 직업을 택한다는 것과, 그 안에서 만족감을 느끼고 있음을 이해 받는 날이 오기를 바란다.", "I hope the day comes when it is understood that young people choose jobs through various thoughts and judgments and feel satisfaction within them."),
]
_FAC = [("개인 발전 가능성", "the possibility of personal growth"), ("근로 시간", "working hours"), ("사회적 지위와 명예", "social status and honor"), ("업무에 대한 적성과 소질", "aptitude and talent for the work"), ("연봉", "annual salary"), ("워라벨 보장", "a guaranteed work-life balance"), ("정년 보장 등 안정성", "stability such as a guaranteed retirement age"), ("직원 복지제도", "employee welfare programs")]
L10 = lesson(
    "Ch 44 · Activities C: job preferences, then and now",
    "직업 선호도 · 교사 · 간호사 · 군인 · 도배사 · 기성세대 · 청년 · 창업",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): a survey of high school students",
             "The following news article is about a survey of high school students. In step a the book asks you to choose a fitting title from four (요즘 학생들이 선호하는 직업; 신세대의 연예인 선호 이유; 과거 고등학생들이 선호한 직업; 연봉이 높은 인기 직업), in step b to fill in a table of the top three jobs today and 20 years ago (the first, teacher, is given), and in step c to translate the underlined part. The article is the book’s with the numbers spelled out (its slashes between job names are read as 이나); the English and the answers are mine, and I translate every sentence.",
             examples=passage(_HS)),
        card("The answers (mine)", "a. Title: 요즘 학생들이 선호하는 직업 (Jobs students prefer these days).",
             tables=[table(["", "1st", "2nd", "3rd"], [["Today", "teacher", "nurse", "soldier"], ["20 years ago", "doctor", "professor", "lawyer"]])]),
        card("Activity 3 (Reading and speaking): factors in choosing a job",
             "In this activity you read an article that presents a personal opinion on the current trends and factors young people consider when choosing a job. In step a you rank, from most to least important to you, a list of factors and share your reasons with classmates (my glosses; the ranking is your own):",
             tables=[ktable(_FAC)]),
        card("The article written by a wallpaper installer (도배사), paragraph [1]",
             "The book glosses 가치: value; 건설: construction; 기술: skill, technology; 기준: standards; 틀: frame. The article is the book’s with the quotation marks of the loan words ‘클리어(완수)’, ‘미션(과제)’ and ‘옵션(선택)’ read out as 클리어, 곧 완수 and so on; the English is mine.",
             examples=passage(_DB1)),
        card("Paragraph [2]", "", examples=passage(_DB2)),
        card("Paragraph [3]", "", examples=passage(_DB3)),
        card("The answers (mine)", "",
             tables=[table(["Question", "Answer (mine)"], [["1. Examples of different motivations for working at a construction site", "Following their parents into the work; leaving a big company to do work that is easier on the mind"], ["2. The author’s criteria, and how they differed", "She wanted a job in which she could be recognized clearly by quantity and quality, solely by skill; she set her own standards instead of the ones many people value, such as high salary, stability and social status"], ["3. Today’s young generation vs. previous generations", "Today: marriage, childbirth and child-rearing are just options (a choice); Previous: they were a mission to complete (the life frame set by society)"], ["4. The older generations’ viewpoint the author criticizes", "Dividing jobs into “good” and “bad” by their own standards without understanding young people’s thinking (e.g., “you went to a good university, so be a public servant”)"], ["5. What the author hopes for", "That the day comes when it is understood that young people choose jobs through various thoughts and judgments and feel satisfaction in them"]])]),
        card("Activities left out", "Activity 1 (SMART Board), Activity 2 (listening to three narrations about the speakers’ desired jobs, the parents’ recommendations and the reasons) and Activity 4 (listening to two narrations about each speaker’s dream job, previous occupation and current occupation, exchanging the information in Korean, and writing and presenting what you want to do after leaving the military or ten years from now) are audio, pair and group activities; the book’s Follow-up 2 on this chapter’s Topic C (listening to three narrations about job preferences of high school students) is audio too."),
    ],
    exercises=uniq(
        _tr(_HS + _DB1 + _DB2 + _DB3 + _FAC, k=3)
        + [M("Who ran the survey?", "The Ministry of Education and the Korea Research Institute for Vocational Education and Training", ["A newspaper", "A school", "The army"], "교육부와 한국직업연구원."), M("How many students were surveyed?", "7,124", ["712", "71,240", "1,000"], "칠천백이십사 명."), M("What job do students hope for most?", "Teacher", ["Doctor", "Soldier", "Lawyer"], "교사."), M("What was third place today?", "Soldier", ["Nurse", "Police officer", "Lawyer"], "군인."), M("What did students pick most 20 years ago?", "Doctor", ["Teacher", "Nurse", "Soldier"], "의사."), M("What are more students hoping to do after graduating?", "Start a business", ["Study abroad", "Join the army", "Marry"], "창업."), M("What is the author’s job?", "Wallpaper installer", ["Teacher", "Pilot", "Doctor"], "도배사."), M("How does the older generation see marriage and child-rearing, per the author?", "As a mission to clear", ["As an option", "As a hobby", "As a burden"], "미션."), M("What does the author hope for?", "That young people’s job choices be understood", ["A higher salary", "To become a public servant", "To move abroad"], "이해 받는 날."),
           F("교육부와 한국직업연구원이 직업 ___를 조사했다. (preference)", "선호도", ["경쟁", "목표"], "직업 선호도."), F("본인이 하고 싶어하는 일이기 때문이라고 ___했다. (answered)", "대답", ["제외", "허락"], "대답하다."), F("졸업 후 ___을 희망하는 학생은 꾸준히 늘어난다. (starting a business)", "창업", ["진학", "연기"], "창업."), F("나만의 ___을 세워서 직업을 선택하고 싶었다. (standard)", "기준", ["연봉", "지위"], "기준."), F("기성세대에게는 하나의 미션이었다면, 요즘 청년들에게는 하나의 ___이다. (option)", "옵션", ["미션", "클리어"], "옵션."),
           read_q("학생들이 가장 희망하는 직업은 교사였습니다"), read_q("졸업 후 창업을 희망하는 학생이 늘어납니다"), read_q("나는 도배사입니다"), read_q("나만의 기준을 세워서 직업을 선택하고 싶었습니다"), read_q("청년들이 다양한 생각으로 직업을 택합니다")]
    ),
)


# ================================================================== L11 Grammar C: time-reference conjunctive endings
_TE = [("–기 전에", "before", "~ 전에"), ("–(으)ㄴ 후에", "after", "~ 후에"), ("–(으)ㄹ 때(에)", "when", "~ 때(에)"), ("–(으)ㄹ 때마다", "whenever", "~ 때마다"), ("–(으)ㄹ 때부터", "since; from the time when", "~ 때부터"), ("–(으)ㄹ 때까지", "until", "~ 때까지"), ("–는 동안(에)", "while; during; for", "~ 동안(에)"), ("–(으)면서", "while doing something (does something else)", "(none)"), ("–자마자", "as soon as; right after", "(none)")]
_TM = [("아침에 여섯 시에 일어납니다.", "I get up at six in the morning."), ("일어나자마자 샤워를 합니다.", "As soon as I get up, I take a shower."), ("샤워를 하는 동안에 노래를 부릅니다.", "While I take a shower, I sing."), ("노래를 부르면서 씻습니다.", "I wash while singing.")]
_TX = [("자기 전에 이를 닦아요.", "–기 전에", "I brush my teeth before going to bed."), ("수업이 끝난 후에 점심을 먹어요.", "–(으)ㄴ 후에", "I eat lunch after class ends."), ("심심할 때 책을 읽어요.", "–(으)ㄹ 때", "I read a book when I am bored."), ("비가 올 때마다 파전을 먹어요.", "–(으)ㄹ 때마다", "Whenever it rains, I eat green onion pancakes."), ("어릴 때부터 축구를 좋아했어요.", "–(으)ㄹ 때부터", "I have liked soccer since I was little."), ("비가 그칠 때까지 기다리세요.", "–(으)ㄹ 때까지", "Please wait until the rain stops."), ("제가 운전하는 동안에 음악을 들으세요.", "–는 동안(에)", "Please listen to music while I drive."), ("걸으면서 전화하지 마세요.", "–(으)면서", "Don’t talk on the phone while walking."), ("집에 오자마자 샤워를 했어요.", "–자마자", "As soon as I came home, I took a shower.")]
_JH = [
    ("저녁을 먹기 전에 정호는 여동생과 함께 이 층 방에서 놀고 있었다.", "Before dinner, Jungho was playing with his younger sister in the second-floor room."),
    ("엄마는 부엌에서 저녁을 준비하고 아빠는 일 층 거실에서 신문을 읽고 있었다.", "Mom was preparing dinner in the kitchen and Dad was reading the newspaper in the first-floor living room."),
    ("엄마가 식구들에게 저녁을 먹으라고 할 때 권총을 든 강도 두 명이 집안으로 들어왔다.", "When Mom told the family to eat dinner, two robbers holding pistols came into the house."),
    ("강도들이 집으로 들어오자마자 정호는 동생과 함께 화장실로 숨었다.", "As soon as the robbers came into the house, Jungho hid in the bathroom with his sister."),
    ("화장실 문을 잠근 후 일일구에 전화를 걸어서 도움을 요청했다.", "After locking the bathroom door, he called 119 and asked for help."),
    ("그런데 강도 한 명이 정호와 동생들을 찾아내서 어디에 전화했는지 물었다.", "But one robber found Jungho and his siblings and asked where he had called."),
    ("정호는 일일구에 전화했다고 했다.", "Jungho said he had called 119."),
    ("전화를 받고 출동한 경찰이 오는 동안 강도들은 도망쳤다.", "While the police who received the call and were dispatched were coming, the robbers fled."),
    ("다행히 다친 사람은 아무도 없었다.", "Fortunately, no one was hurt."),
]
L11 = lesson(
    "Ch 44 · Grammar C: summary of conjunctive endings for time reference",
    "–기 전에 · –(으)ㄴ 후에 · –(으)ㄹ 때 · –(으)ㄹ 때마다 · –(으)ㄹ 때부터 · –(으)ㄹ 때까지 · –는 동안 · –(으)면서 · –자마자",
    requires=[],
    cards=[
        card("The conjunctive endings",
             "You have learned quite a few conjunctive endings that are used for time reference. The book revisits and summarizes them through several activities. First, review the conjunctive endings provided in the table below (“Equivalent Feature Used with Noun” is the noun construction with the same meaning):",
             tables=[table(["Conjunctive ending", "English meaning", "Used with a noun"], [[a, b, c] for a, b, c in _TE])]),
        card("Follow-up 1 (Speaking and listening): saying it one after another",
             "Sit in a circle; the teacher says a sentence about a daily routine, and each student in turn adds a sentence building on the previous one, using a time-reference conjunctive ending each time. The book’s model (the English is mine):",
             examples=passage(_TM)),
        card("One example of each ending (mine)", "Sample sentences of my own (the English is mine):",
             tables=[table(["Sentence", "Ending", "Meaning"], [[a, b, c] for a, b, c in _TX], say=[0])]),
        card("Follow-up 2 (Reading): a courageous seven-year-old boy",
             "The following is a story about a courageous 7-year-old boy (the Korean text writes the boy as 정호). In step a the book asks you to underline and number the time references that include conjunctive endings (the first, 저녁을 먹기 전에, is done for you); in step b to fill in a table (when / what). The book glosses 잠그다: to lock. The story is the book’s with the numbers spelled out (119 is 일일구); the English is mine.",
             examples=passage(_JH)),
        card("The table filled in (mine)", "",
             tables=[table(["When", "What (mine)"], [["1. before dinner (저녁을 먹기 전에)", "Jungho was playing with his younger sister in the room"], ["2. when Mom told the family to eat dinner (저녁을 먹으라고 할 때)", "Two robbers holding pistols came into the house"], ["3. as soon as the robbers came into the house (들어오자마자)", "Jungho hid in the bathroom with his sister"], ["4. after locking the bathroom door (문을 잠근 후)", "He called 119 and asked for help"], ["5. while the police were coming (경찰이 오는 동안)", "The robbers fled"]])]),
        card("Activities left out", "Follow-up 3 (listening to ten dialog segments in which a police officer asks a suspect what she did last Saturday, checking the conjunctive ending and writing the two actions) and Follow-up 4 (listening to an incomplete story, writing a few more sentences with time endings in Korean and sharing the story with two classmates) are audio and group activities."),
    ],
    exercises=uniq(
        _tr(_TM + [(a, c) for a, b, c in _TX] + _JH, k=3)
        + [M("Which ending means ‘before’?", "–기 전에", ["–(으)ㄴ 후에", "–자마자", "–(으)ㄹ 때까지"], "~ 전에."), M("Which ending means ‘after’?", "–(으)ㄴ 후에", ["–기 전에", "–는 동안", "–(으)면서"], "~ 후에."), M("Which ending means ‘whenever’?", "–(으)ㄹ 때마다", ["–(으)ㄹ 때", "–(으)ㄹ 때부터", "–(으)ㄹ 때까지"], "때마다."), M("Which ending means ‘since; from the time when’?", "–(으)ㄹ 때부터", ["–(으)ㄹ 때까지", "–(으)ㄹ 때마다", "–기 전에"], "때부터."), M("Which ending means ‘until’?", "–(으)ㄹ 때까지", ["–(으)ㄹ 때부터", "–는 동안", "–자마자"], "때까지."), M("Which ending means ‘while; during’?", "–는 동안(에)", ["–(으)ㄴ 후에", "–자마자", "–기 전에"], "동안."), M("Which ending means ‘while doing something else’?", "–(으)면서", ["–는 동안", "–자마자", "–(으)ㄴ 후에"], "–(으)면서."), M("Which ending means ‘as soon as’?", "–자마자", ["–(으)면서", "–기 전에", "–(으)ㄹ 때까지"], "–자마자."), M("Which endings have no noun equivalent in the book’s table?", "–(으)면서 and –자마자", ["–기 전에 and –(으)ㄴ 후에", "–(으)ㄹ 때 and –(으)ㄹ 때마다", "All of them"], "The book’s table."), M("What did Jungho do after locking the bathroom door?", "Called 119", ["Hid under a bed", "Ran outside", "Fought the robbers"], "일일구에 전화."), M("What happened while the police were coming?", "The robbers fled", ["Jungho was caught", "The family left", "A neighbor came"], "도망쳤다."),
           F("잠을 자___ 이를 닦아요. (before)", "기 전에", ["고 나서", "는 동안"], "–기 전에."), F("수업이 끝난 ___ 점심을 먹어요. (after)", "후에", ["전에", "동안"], "–(으)ㄴ 후에."), F("집에 오___ 샤워를 했어요. (as soon as)", "자마자", ["면서", "기 전에"], "–자마자."), F("걸___ 전화하지 마세요. (while)", "으면서", ["자마자", "기 전에"], "–(으)면서."), F("비가 그칠 ___ 기다리세요. (until)", "때까지", ["때마다", "때부터"], "–(으)ㄹ 때까지."), F("비가 올 ___ 파전을 먹어요. (whenever)", "때마다", ["때까지", "때부터"], "–(으)ㄹ 때마다."),
           read_q("일어나자마자 샤워를 합니다"), read_q("샤워를 하는 동안에 노래를 부릅니다"), read_q("화장실 문을 잠근 후 일일구에 전화를 걸었습니다"), read_q("경찰이 오는 동안 강도들은 도망쳤습니다"), read_q("저녁을 먹기 전에 정호는 방에서 놀고 있었습니다")]
    ),
)

# ================================================================== L12 Activities + self-evaluation
_CB = [("집에 도착했어요. 샤워를 했어요.", "집에 도착하자마자 샤워를 했어요.", "As soon as I arrived home, I took a shower."), ("저는 밥을 먹어요. 텔레비전을 봐요.", "저는 밥을 먹으면서 텔레비전을 봐요.", "I watch TV while eating."), ("한국어 수업이 끝났어요. 도서관에 갔어요.", "한국어 수업이 끝난 후에 도서관에 갔어요.", "After Korean class ended, I went to the library."), ("저는 잠을 자요. 이를 닦아요.", "저는 잠을 자기 전에 이를 닦아요.", "I brush my teeth before sleeping."), ("제가 샤워를 해요. 동생이 음악을 들어요.", "제가 샤워를 하는 동안에 동생이 음악을 들어요.", "While I take a shower, my younger brother listens to music."), ("시험이 끝나요. 쉬지 않고 공부했어요.", "시험이 끝날 때까지 쉬지 않고 공부했어요.", "I studied without resting until the exam ended."), ("저는 어렸어요. 축구를 좋아했어요.", "저는 어렸을 때부터 축구를 좋아했어요.", "I have liked soccer since I was little."), ("저는 피곤해요. 커피를 마셔요.", "저는 피곤할 때마다 커피를 마셔요.", "Whenever I am tired, I drink coffee.")]
L12 = lesson(
    "Ch 44 · Activities and self-evaluation",
    "연결어미 연습 · 자기 평가 · 명절 · 스포츠 · 직업",
    requires=[],
    cards=[
        card("Combine the sentences with a time ending (mine)",
             "To practice the summary, combine each pair of short sentences with one time-reference ending (the pairs, the answers and the English are mine, in the spirit of the book’s Follow-ups).",
             tables=[table(["Two sentences", "Combined (mine)", "Meaning (mine)"], [[a, b, c] for a, b, c in _CB], say=[0, 1])]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so that they can provide other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and describe social customs and trends related to major national holidays; identify and discuss sports events and sports culture; and compare and discuss how job preferences have changed.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the summary of conjunctive endings related to time reference; an interrogative word followed by –든(지) (no matter what/who/when, etc.); ~까지(도) (even; to a degree that extends); and the Sino-Korean syllables within 최대 (最大), 동계 (冬季), and 안정 (安定)."),
        card("Activities left out", "The chapter’s activity sections also contain a SMART Board reading activity, listening activities (Chuseok conversations, international sports events, job positives and negatives), and speaking and writing activities in pairs or groups. They are audio, computer and group activities and are left out; the readings of the activities are in the earlier lessons of this chapter."),
    ],
    exercises=uniq(
        _tr([(b, c) for a, b, c in _CB], k=3)
        + [M("How do you say ‘as soon as I arrived home’?", "집에 도착하자마자", ["집에 도착하기 전에", "집에 도착할 때까지", "집에 도착하면서"], "–자마자."), M("How do you say ‘while eating’?", "먹으면서", ["먹자마자", "먹기 전에", "먹은 후에"], "–(으)면서."), M("How do you say ‘after class ended’?", "수업이 끝난 후에", ["수업이 끝나기 전에", "수업이 끝날 때까지", "수업이 끝나자마자"], "–(으)ㄴ 후에."), M("How do you say ‘before sleeping’?", "자기 전에", ["잔 후에", "자면서", "자자마자"], "–기 전에."), M("How do you say ‘until the exam ended’?", "시험이 끝날 때까지", ["시험이 끝날 때마다", "시험이 끝난 후에", "시험이 끝날 때부터"], "–(으)ㄹ 때까지."), M("What should you do if you tick “No” in the self-evaluation?", "Review on your own, study with a partner, tell your advisor or team leader", ["Skip it", "Retake the course", "Nothing"], "The book’s advice."),
           F("집에 도착하___ 샤워를 했어요. (as soon as)", "자마자", ["면서", "기 전에"], "–자마자."), F("저는 밥을 먹___ 텔레비전을 봐요. (while)", "으면서", ["자마자", "기 전에"], "–(으)면서."), F("저는 잠을 자___ 이를 닦아요. (before)", "기 전에", ["은 후에", "는 동안"], "–기 전에."), F("저는 어렸을 ___ 축구를 좋아했어요. (since)", "때부터", ["때까지", "때마다"], "–(으)ㄹ 때부터."), F("저는 피곤할 ___ 커피를 마셔요. (whenever)", "때마다", ["때까지", "때부터"], "–(으)ㄹ 때마다."),
           read_q("집에 도착하자마자 샤워를 했어요"), read_q("저는 밥을 먹으면서 텔레비전을 봐요"), read_q("저는 잠을 자기 전에 이를 닦아요"), read_q("저는 어렸을 때부터 축구를 좋아했어요"), read_q("저는 피곤할 때마다 커피를 마셔요")]
    ),
)

# ================================================================== L13 core vocabulary
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/") and " " not in r[0]]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0] and "…" not in r[0] and "–" not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L13 = lesson(
    "Ch 44 · Core vocabulary",
    "주요 단어 · 명절 · 스포츠 · 직업 · 든지 · 까지도",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning (the book prints 冬系 for 동계 in one place; the Sino-Korean note gives 冬季, which I use). The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. The book’s Loan Words section repeats words already listed above (디자이너, 메달, 스타, 아마추어, 올림픽, 월드컵, 코치, 프로 and so on); I list each word once. The last section lists the Sino-Korean related words of 최대, 동계 and 안정 as the book gives them.\n\n"
             "The example sentences with digits are respelled in Hangul (4대 → 네 대; 40% → 사십 퍼센트; 24개 → 스물네 개; 32개 → 서른두 개; 4년마다 → 사 년마다; 1988년 → 천구백팔십팔 년)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 휴양지 mean?", "a resort", ["a plaza", "a stadium", "a parents’ home"], "休養地."), M("What does 친정 mean?", "a married woman’s parents’ home", ["a resort", "a hometown", "a plaza"], "親庭."), M("What does 예선 mean?", "the preliminaries", ["the finals", "the second half", "a medal"], "豫選."), M("What does 본선 mean?", "the finals; post-preliminary matches", ["the preliminaries", "a coach", "a plaza"], "本選."), M("What does 연예인 mean?", "an entertainer; a celebrity", ["a veterinarian", "a designer", "a coach"], "演藝人."), M("What does 소득 mean?", "income", ["talent", "goal", "competition"], "所得."), M("What does 안정(적) mean?", "stability (stable)", ["reality", "competition", "intention"], "安定."), M("What does 장래 mean?", "the future", ["the past", "the present", "intention"], "將來."),
           F("전통 ___ 중에서 좋은 것은 계속 지켜가야 해요. (customs)", "풍속", ["풍경", "행렬"], "풍속."), F("한국 팀이 ___ 동안 두 골을 넣었습니다. (second half)", "후반전", ["전반전", "예선"], "후반전."), F("저는 운동에 ___이 없어요. (aptitude)", "소질", ["소득", "목표"], "소질."), F("우리의 ___는 메달을 다섯 개 이상 따는 것이다. (goal)", "목표", ["소득", "의사"], "목표."), F("저는 요리사가 되고 싶어요. 그 꿈을 ___ 위해 요리학교에 등록했어요. (to achieve)", "이루기", ["덜기", "바꾸기"], "이루다."),
           read_q("주요 단어"), read_q("휴양지"), read_q("월드컵"), read_q("연예인"), read_q("장래")]
    ),
)

UNIT = unit("Semester 2 · Unit 11 · Chapter 44: Various Aspects of Korean Society (한국 사회의 여러 모습)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])

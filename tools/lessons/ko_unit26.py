"""Unit 26: KBC Semester 1, Unit 5, Chapter 19 - Sports and Outdoor Activities.
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 5, Student's Edition (2022).
Audio, video clips, photos, pictures, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk


# ---- the core vocabulary of Chapter 19 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_SPORT = [
    ("권투", "(拳鬪) boxing; “fist fighting”", "어제 티브이에서 권투 경기를 봤습니다."),
    ("복싱", "boxing", "무하마드 알리는 유명한 복싱 선수입니다."),
    ("사격", "(射擊) shooting; marksmanship", "군인들은 사격을 잘 해야 합니다."),
    ("양궁", "(洋弓) archery; “western bow”", "어제 양궁 경기에서 한국 대표팀 선수들이 우승했습니다."),
    ("역도", "(力道) weight lifting; “power way”", "사재혁은 유명한 역도 선수입니다."),
    ("유도", "(柔道) judo; “fluid way”", "일본은 유도로 유명합니다."),
    ("육상", "(陸上) track and field; “land above”", "내일 남자 육상 백 미터 경기가 있습니다."),
    ("체조", "(體操) gymnastics", "지금 미국팀이 중국팀과 체조 경기를 하고 있습니다."),
    ("태권도", "(跆拳道) tae kwon do", "척 노리스는 태권도를 잘 합니다."),
]
_CV_REL = [
    ("결승(전)", "(決勝(戰)) the final", "한국이 야구 결승전에 나갑니다."),
    ("경기", "(競技) a game; a match; a competition (~하다: to play a game; to play a match)", "어제 미국과 일본이 야구 경기를 했습니다."),
    ("~대", "(對) counter; versus; to (as in 4 to 3)", "한국이 멕시코를 팔 대 사로 이겼습니다."),
    ("대회", "(大會) a tournament; a conference; “big meeting”", f"이번 테니스 대회에는 열 개국이 참가했습니다."),
    ("비기다", "to tie; to end (a game) in a tie", "어제 야구 경기에서 한국과 미국이 오 대 오로 비겼습니다."),
    ("선수", "(選手) an athlete; a player", "박찬호는 유명한 야구 선수입니다."),
    ("시합", "(試合) a game; a match; a contest (~하다: to play a game; to play a match)", "어제 친구들과 농구 시합을 했습니다."),
    ("신기록", "(新記錄) a new record; (~을 세우다: to set a new record; “to establish a new record”)", "미국 선수가 육상에서 세계 신기록을 세웠습니다."),
    ("우승", "(優勝) winning a championship; a victory (~하다: to win a championship)", "올림픽 야구 경기에서 한국팀이 우승했습니다."),
    ("응원", "(應援) cheering; rooting for (~하다: to cheer; to root for)", "이 경기에서 어느 팀을 응원할 거예요?"),
    ("이기다", "to win (a game or a match)", "탁구 경기에서 중국 선수가 일본 선수를 이겼습니다."),
    ("준결승(전)", "(準決勝(戰)) a semifinal (match)", "미국 배구팀이 준결승전에 나갑니다."),
    ("지다", "to be defeated; to lose (a game or a match)", "일본팀이 축구 경기에서 졌습니다."),
]
_CV_FARM = [
    ("과수원", "(果樹園) an orchard", "과수원에서 과일을 사면 아주 쌉니다."),
    ("기르다", "to raise (an animal); to grow (a plant)", "이 농장에서는 동물도 기릅니다."),
    ("농장", "(農場) a farm; “farming place”", "우리 농장에는 여러 가지 과일과 채소가 있어요."),
    ("동물", "(動物) an animal; “moving thing”", "저는 작은 동물을 더 좋아해요."),
    ("먹이", "feed; fodder (~ 주다: to feed)", "할머니께서 고양이한테 먹이를 주십니다."),
    ("밭", "a field", "밭에서 싱싱한 채소를 기릅니다."),
    ("시골", "countryside; a rural area", "시골에는 사람이 많이 살지 않아요."),
    ("심다", "to plant", "뒷마당에 나무를 심고 싶어요."),
]
_CV_ANI = [
    ("개", "a dog", "매일 개와 함께 공원을 산책합니다."),
    ("고양이", "a cat", "저는 개보다 고양이가 더 좋아요."),
    ("새", "a bird", "바닷가에 새가 많이 날아다녀요."),
    ("양", "(羊) a sheep", "뉴질랜드는 양으로 유명합니다."),
    ("오리", "a duck", "저희 동물농장에는 오리도 있어요."),
    ("토끼", "a rabbit", "토끼는 당근을 좋아해요."),
]
_CV_CLUB = [
    ("가입", "(加入) joining (a club, an organization, etc.); enrollment (~하다/되다: to join/to be joined)", "자동차 클럽에 가입했습니다."),
    ("당구", "(撞球) billiards; pool", "당구 중에 포켓볼은 배우기가 쉽습니다."),
    ("동호회", "(同好會) a club; “same like meeting”", "동호회는 취미 활동을 같이 하는 모임입니다."),
    ("들다", "to join (a club); “to come in”", "학교 축구 동호회에 들었어요."),
    ("등산화", "(登山靴) mountain-climbing shoes; hiking shoes", "등산화는 운동화보다 좀 무거워요."),
    ("산악", "(山嶽) rugged mountains; “huge mountains”", "우리 산악회는 주말마다 등산을 갑니다."),
    ("신청서", "(申請書) an application; “application paper”", "당구 동호회 신청서를 받았습니다."),
    ("정기", "(定期) regular (interval)", "이번 토요일에 정기모임이 있어요."),
    ("초보자", "(初步者) a novice; a beginner; “beginning walker”", "운전 초보자는 조심해서 운전해야 합니다."),
    ("회비", "(會費) a membership fee; “meeting fee”", "동호회는 보통 회비가 있습니다."),
    ("회원", "(會員) a member (of a club, association, etc.); “meeting member”", "저희 동호회는 회원들끼리 자주 만나요."),
]
_CV_OTH = [
    ("그렇다", "to be like “it”; to be like [such]", "여기에 그런 사람 없습니다. 번호를 확인해 보세요."),
    ("~끼리", "together (with what shares the same characteristics or features)", "내일 친구들끼리 한국 식당에 갈 거예요."),
    ("따다", "to pick (a fruit); to win (a medal)", "지난 주말에 딸기농장에서 딸기를 땄어요. / 육상 경기에서 금메달을 땄어요."),
    ("무엇보다", "above all", "무엇보다 한국어 배우는 것이 좋아요."),
    ("사귀다", "to make friends with; to associate with", "학교에서 친구를 많이 사귀었습니다."),
    ("언제든지", "anytime; whenever", "질문이 있으면 언제든지 하세요."),
    ("~에 대한", "about; regarding", "이 대학의 역사에 대한 설명을 듣고 싶습니다."),
    ("열심히", "diligently", "한국어 공부를 열심히 하겠습니다."),
    ("-(으)ㄴ 적이 있다", "to have past experience of having done something", "유럽에 가 본 적이 있어요?"),
    ("-(으)ㄴ 적이 없다", "to have no past experience of having done something", "북한에 가 본 적이 없습니다."),
    ("이렇다", "to be like “this”; to be like [such]", "여러분, 저를 따라 이렇게 해 보세요."),
    ("저렇다", "to be like “that”; to be like [such]", "나도 저런 차를 사고 싶어요."),
    ("질문", "(質問) a question; an inquiry (~하다: to question; to ask)", "모르는 것이 있으면 선생님한테 질문하세요."),
    ("참", "really; truly", "농장이 참 크네요!"),
    ("체험", "(體驗) hands-on experience (~하다: to experience hands-on)", "시골 생활을 농장에서 체험해 봤어요."),
    ("친하다", "to be close; to be intimate", "박 일병과 김 이병은 아주 친합니다."),
]
_CV_LOAN = [
    ("배드민턴", "badminton", "배드민턴은 배우기가 쉽습니다."),
    ("번지 점프", "bungee jump", "번지 점프는 좀 무서운 것 같아요."),
    ("스쿠버 다이빙", "scuba diving", "카멜 바닷가에서 스쿠버 다이빙을 많이 해요."),
    ("오리엔테이션", "an orientation", "오늘 학교에서 오리엔테이션이 있습니다."),
    ("인라인 스케이트", "inline skates", "인라인 스케이트는 가족끼리 많이 해요."),
    ("팀", "a team", "한국 대표팀 선수가 수영에서 신기록을 세웠습니다."),
]
_CV_SINO = [("농", "(農) farming; agriculture", "농부, 농업, 농장, 소농"), ("승", "(勝) victory; winning", "승자, 승전, 우승"), ("패", "(敗) defeat; loss", f"패자, 패전, 삼 승 이 패")]
_ALL = {r[0]: r for r in _CV_SPORT + _CV_REL + _CV_FARM + _CV_ANI + _CV_CLUB + _CV_OTH + _CV_LOAN + _CV_SINO}
_EXTRA = {"승자": "a winner (mine)", "패자": "a loser (mine)", "무승부": "a tie; a draw (mine)", "패전": "a defeat (mine)", "승전": "a victory in battle (mine)", "농기계": "farm machinery (mine)", "농산물": "agricultural products (mine)", "주말 농장": "a weekend farm (mine)", "준우승": "second place; runner-up (mine)",
          "닭": "a chicken (mine)", "나무": "a tree (mine)", "탁구": "table tennis (mine)", "수영": "swimming (mine)", "야구": "baseball (mine)", "농구": "basketball (mine)", "축구": "soccer (mine)", "등산": "mountain hiking (mine)", "다이빙": "diving (mine)", "점수": "a point; a score", "스포츠": "sports (mine)", "허수아비": "a scarecrow", "눈사람": "a snowman (mine)", "체육관": "a gym (mine)", "도서관": "a library (mine)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)


# ================================================================== L1: objectives and the Sino-Korean syllables 승 and 패
_SP = [("승자", "a winner (mine; 者 = a person)"), ("패자", "a loser (mine)"), ("무승부", "a tie; a draw (mine; 無 = no)"), ("패전", "a defeat (mine; 戰 = a war, fighting)"), ("승전", "a victory in battle (mine)"), ("삼 승 이 패", "3 wins and 2 losses (mine; the book writes 3승 2패)"),
       ("우승", "winning a championship (the book’s example for 승)"), ("완승", "a huge victory; a complete victory (the book’s example for 승)"), ("패배", "a defeat; a loss; “losing and running away” (the book’s example for 패)"), ("실패", "a failure (the book’s example for 패)"), ("완패", "a crushing defeat; “complete defeat” (the book’s example for 패)")]
L1 = lesson(
    "Ch 19 · What the chapter teaches and the Sino-Korean syllables 승 and 패",
    "스포츠와 야외 활동 · 승 (勝) · 패 (敗) · 우승 · 패배 · 무승부",
    requires=[],
    cards=[
        card("What Chapter 19 teaches (스포츠와 야외 활동)",
             "Chapter 19, “Sports and Outdoor Activities”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: talk about common sporting events in Korea; talk about general activities on a “weekend” farm as well as common farm animals; and talk about common “hobby” clubs and outdoor activities.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; -(으)ㄴ 적이 있다 (to have past experience of having done something); -(으)ㄴ 적이 없다 (to have no past experience of having done something); incomplete sentences; ~에 대해(서) vs. ~에 대한 (about; regarding); ㅎ irregular verbs; and the Sino-Korean syllables 승 (勝), 패 (敗) and 농 (農)."),
        card("Sino-Korean in use: 승패 (勝敗)",
             "The first syllable 승 (勝) means victory or winning, as in 우승 (a victory; “excellent winning”) and 완승 (a huge victory; a complete victory), whereas the second syllable 패 (敗) means defeat or losing, as in 패배 (a defeat; a loss; “losing and running away”), 실패 (a failure) and 완패 (a crushing defeat; “complete defeat”). Thus the literal meaning of 승패 is “victory (and) defeat” or “winning or losing”. Depending on the context, the word can mean the result (of a battle, contest, match or game).\n\n"
             "The book asks you to guess the meaning of 승자, 패자, 무승부, 패전, 승전 and 3승 2패, with the hints 자 (者): a person and 전 (戰): a war, fighting. The answers are mine.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _SP], say=[0])]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1 and 2 (SMART Board activities) and Activity 3 (a charade game in two teams) are picture, computer or game activities."),
    ],
    exercises=uniq(
        _tr(_SP)
        + [M("What does the Sino-Korean syllable 승 (勝) mean?", "victory; winning", ["defeat; loss", "farming", "a person"], "우승, 완승."), M("What does the Sino-Korean syllable 패 (敗) mean?", "defeat; loss", ["victory; winning", "farming", "a war"], "패배, 실패, 완패."),
           M("What does 자 (者) mean?", "a person", ["a war", "a field", "a team"], "승자 = a winner."), M("What does 전 (戰) mean?", "a war; fighting", ["a person", "a field", "a team"], "승전, 패전."),
           M("What is a “winner”?", "승자", ["패자", "선수", "회원"], "승자 = a winner."), M("What is a “loser”?", "패자", ["승자", "선수", "회원"], "패자 = a loser."), M("What does 무승부 mean?", "a tie; a draw", ["a victory", "a defeat", "a new record"], "승부가 없다 = a tie."),
           M("What does 승패 literally mean?", "“victory (and) defeat”", ["“excellent winning”", "“complete defeat”", "“a person and a war”"], "승 + 패."), M("What does 우승 literally mean?", "“excellent winning”", ["“complete defeat”", "“victory and defeat”", "“losing and running away”"], "우승 = a victory."),
           M("What does 패배 literally mean?", "“losing and running away”", ["“excellent winning”", "“complete defeat”", "“victory and defeat”"], "패배 = a defeat."),
           F("한국 팀이 세계 대회에서 ___했습니다. (won the championship)", "우승", ["실패", "패배"], "우승 = winning a championship."), F("축구 경기에서 일본 팀이 ___. (lost)", "졌습니다", ["이겼습니다", "비겼습니다"], "지다 = to lose."),
           read_q("승자"), read_q("패자"), read_q("무승부"), read_q("패전"), read_q("우승")]
    ),
)

# ================================================================== L2: Topic A
_A_DLG = [
    ("민재", "어제 한국과 중국 올림픽 야구 경기 봤어?", "Did you watch the Korea–China Olympic baseball game yesterday?"),
    ("다희", "아니, 못 봤어. 누가 이겼어?", "No, I couldn’t. Who won?"),
    ("민재", "한국이 칠 대 이로 이겼어.", "Korea won 7 to 2."),
    ("다희", "그럼 한국이 준결승전에 나가?", "Then does Korea go to the semifinals?"),
    ("민재", "응. 한국이 사 승 일 패야. 그래서 다음 시합에서 비겨도 준결승에 나갈 수 있어.", "Yes. Korea is 4 wins and 1 loss. So even if it ties in the next game, it can go to the semifinals."),
    ("다희", "그래? 한국팀이 우승하면 좋겠다.", "Really? I hope the Korean team wins the championship."),
    ("민재", "근데, 어제 양궁 경기는 어떻게 됐어?", "By the way, how did yesterday’s archery event go?"),
    ("다희", "한국 여자 대표팀 선수들이 또 세계 신기록을 세웠어.", "The Korean women’s national team players set a world record again."),
    ("민재", "정말? 잘 했다. 참, 너 체조 좋아해?", "Really? Well done. Oh, do you like gymnastics?"),
    ("다희", "응. 왜?", "Yes. Why?"),
    ("민재", "오늘 저녁 한국팀 체조 경기가 있는데 우리 집에서 같이 볼까?", "There is a Korean team gymnastics event tonight. Shall we watch it together at my house?"),
    ("다희", "좋아! 보면서 열심히 한국팀을 응원해야겠다.", "Good! I have to cheer hard for the Korean team while watching."),
]
_A_WORDS = ["결승(전)", "경기", "권투", "복싱", "~대", "대회", "따다", "비기다", "사격", "선수", "시합", "신기록", "양궁", "역도", "열심히", "우승", "유도", "육상", "응원", "이기다", "준결승(전)", "지다", "체조", "태권도", "팀"]
_TYPES = [("권투 / 복싱", "boxing"), ("사격", "shooting"), ("양궁", "archery"), ("역도", "weight lifting"), ("유도", "judo"), ("육상", "track and field"), ("체조", "gymnastics"), ("태권도", "tae kwon do")]
L2 = lesson(
    "Ch 19 · Topic A: The Korean team advances to the semifinals",
    "한국팀이 준결승전에 나갑니다 · 올림픽 · 경기 · 이기다 · 지다 · 비기다 · 응원",
    requires=[],
    cards=[
        card("Topic A: The Korean team advances to the semifinals (한국팀이 준결승전에 나갑니다)",
             "Two friends, Minjae and Dahee, are talking about Olympic events. (The English is mine; the book gives none. The book writes 7대 2 and 4승 1패; they are spelled out here, and ‘Korea–China’ is my reading of 한국과 중국.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Types of sports (스포츠 종목)",
             "The book shows pictures of eight sports with their names; the pictures are left out. The English is the book’s.",
             tables=[ktable(_TYPES)]),
        card("Activities left out",
             "Presentation Activity c (a SMART Board activity), d (partner reading and translating) and Follow-up 1 (listening to three dialogs about the results of the national team’s game, and checking win, lose or tie and the score) are computer, partner or audio activities. Presentation Activity a (filling in a table of eight sports) is covered by the table above. Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not w.startswith("~") and "(" not in w]))
        + _tr(_strip(_A_DLG) + _TYPES)
        + [M("Which game did Minjae watch yesterday?", "Korea against China, in Olympic baseball", ["Korea against Japan in soccer", "Archery", "Gymnastics"], "한국과 중국 올림픽 야구 경기."), M("What was the score?", "Korea won 7 to 2", ["Korea lost 2 to 7", "They tied 7 to 7", "Korea won 4 to 1"], "칠 대 이로 이겼어."),
           M("What is Korea’s record?", "4 wins and 1 loss", ["1 win and 4 losses", "7 wins and 2 losses", "2 wins"], "사 승 일 패."), M("Can Korea go to the semifinals even if it ties the next game?", "Yes", ["No", "Only if it wins", "Only if it loses"], "비겨도 준결승에 나갈 수 있어."),
           M("What did the Korean women’s archery players do?", "Set a world record again", ["Lost the final", "Tied the game", "Quit"], "또 세계 신기록을 세웠어."), M("What does Minjae ask Dahee after archery?", "If she likes gymnastics", ["If she likes judo", "If she likes boxing", "If she likes baseball"], "너 체조 좋아해?"),
           M("Where do they plan to watch the gymnastics event?", "At Minjae’s house", ["At the gym", "At a restaurant", "At Dahee’s house"], "우리 집에서 같이 볼까?"), M("What does Dahee say she must do?", "Cheer hard for the Korean team", ["Go to bed early", "Buy tickets", "Play gymnastics"], "열심히 한국팀을 응원해야겠다."),
           M("Which word means “to tie”?", "비기다", ["이기다", "지다", "따다"], "비기다 = to tie."), M("Which word means “to win a game”?", "이기다", ["지다", "비기다", "따다"], "이기다 = to win."), M("Which word means “to lose a game”?", "지다", ["이기다", "비기다", "따다"], "지다 = to lose."),
           M("What does 따다 mean in 금메달을 따다?", "to win (a medal)", ["to lose", "to tie", "to plant"], "따다 = to pick (a fruit); to win (a medal)."),
           F("한국이 칠 ___ 이로 이겼어. (to, versus)", "대", ["승", "패"], "~대 = versus; to (as in 4 to 3)."), F("한국이 사 ___ 일 패야. (wins)", "승", ["대", "패"], "사 승 일 패 = 4 wins and 1 loss."), F("다음 시합에서 ___도 준결승에 나갈 수 있어. (even if it ties)", "비겨", ["이겨", "져"], "비기다 → 비겨."),
           F("한국이 준___전에 나가? (semifinal)", "결승", ["우승", "신기록"], "준결승전 = a semifinal."), F("세계 ___을 세웠어. (a new record)", "신기록", ["우승", "응원"], "신기록을 세우다 = to set a new record."), F("열심히 한국팀을 ___해야겠다. (cheer)", "응원", ["우승", "시합"], "응원하다 = to cheer."),
           read_q("준결승전"), read_q("양궁 경기"), read_q("세계 신기록"), read_q("체조 경기"), read_q("한국이 이겼어")]
    ),
)

# ================================================================== L3: Follow-up 2 (article), Activities A
_ART = [
    ("한국 여자 탁구 준우승", "Korean women’s table tennis, runner-up"),
    ("한국 여자 대표팀이 세계 탁구 대회에서 준우승을 했다.", "The Korean women’s national team took second place at the world table tennis tournament."),
    ("서울 잠실 체육관에서 열린 결승전에서 한국팀은 세트 스코어 삼 대 이로 중국팀에게 패했다.", "In the final held at the Jamsil Gym in Seoul, the Korean team lost to the Chinese team by a set score of 3 to 2."),
    ("그리고 남자 대표팀은 세트 스코어 삼 대 일로 헝가리에게 이겼다.", "And the men’s national team beat Hungary by a set score of 3 to 1."),
    ("남자 대표팀은 칠 승 이 패로 준결승전에 나갈 수 있다.", "The men’s national team, at 7 wins and 2 losses, can go to the semifinals."),
]
_MATCH = [("응원", "cheering; rooting"), ("신기록", "a new record"), ("육상", "track and field"), ("양궁", "archery"), ("선수", "a player; an athlete"), ("결승전", "the final"), ("우승", "winning a championship"), ("체조", "gymnastics"), ("비기다", "to tie; to end in a tie"), ("지다", "to be defeated; to lose")]
_SCHED = [
    ("야구", "세계 야구 대회, 케이비에스 티브이 위성중계, 한국 대 멕시코, 미국 샌디에고 새벽 한 시 반", "World baseball tournament, KBS TV satellite broadcast, Korea against Mexico, San Diego in the U.S., 1:30 a.m."),
    ("농구", "여자 농구 결승전 일차전, 에스비에스 티브이, 신한 은행 대 삼성 전자, 안산 와동 체육관 오후 다섯 시", "Women’s basketball final, 1st game, SBS TV, Shinhan Bank against Samsung Electronics, Ansan Wadong Gym, 5:00 p.m."),
    ("", "이차전은 십팔 일 수요일 용인 체육관, 삼차전은 이십 일 금요일 장충 체육관", "The 2nd game is on the 18th (Wednesday) at the Yongin Gym; the 3rd game on the 20th (Friday) at the Jangchung Gym."),
    ("태권도", "아시아 게임 국가대표 선발전, 올림픽 체조 경기장 오전 열 시", "Asian Games national team selection contest, Olympic Gymnastics Arena, 10:00 a.m."),
    ("축구", "케이 리그 프로 축구 준결승전, 성남 일화 대 울산 현대, 동대문 운동장 오후 두 시", "K League professional soccer semifinal, Seongnam Ilhwa against Ulsan Hyundai, Dongdaemun Stadium, 2:00 p.m."),
]
_SCH_W = [("선발전", "a selection contest"), ("프로", "a professional"), ("일차전", "the 1st round; “the first battle” (the book writes 1차전)"), ("위성중계", "a satellite broadcast (mine)"), ("국가대표", "a national team member (mine)")]
L3 = lesson(
    "Ch 19 · Topic A, Follow-up 2 and Activities A: a sports article and match results",
    "한국 여자 탁구 준우승 · 신기록 · 결승전 · 야구 · 농구 · 태권도 · 축구 · 경기 일정",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): a newspaper article",
             "The book gives a short newspaper article about the results of two Korean national teams (the men’s and the women’s) and asks you to answer in English what sport is reported and to fill in a table (score, opponent, country). The text is the book’s (the scores are spelled out in Hangul); the English is mine. The book glosses 점수 as “a point, a score”.",
             examples=passage(_ART)),
        card("The answers (mine)",
             "The book leaves the answers blank; these are my answers. The sport is table tennis (탁구).",
             tables=[table(["Team", "Score", "Opponent", "Country"], [["Female team", "3 to 2 (lost)", "the Chinese team", "China"], ["Male team", "3 to 1 (won)", "the Hungarian team", "Hungary"]])]),
        card("Activity 1 (Reading): match the Korean words with their English equivalents",
             "The book gives ten Korean words and ten English meanings in a different order and asks you to draw lines. The pairs below are the book’s words with their meanings (the matching answers are mine).",
             tables=[ktable(_MATCH)]),
        card("Activity 2 (Reading): today’s game schedule",
             "The book gives a newspaper’s game schedule for various sports and asks you to circle the English equivalents of the sports listed (shooting, basketball, gymnastics, tae kwon do, swimming, track and field, baseball, archery, soccer). The schedule is the book’s (times and dates are spelled out; the book’s hyphen between the teams is read 대 here, the book’s ‘(수)’ and ‘(금)’ are written out as 수요일 and 금요일, and the book’s ‘<KBS TV>’ marks are dropped); the English is mine.",
             tables=[table(["Sport", "Schedule", "English (mine)"], [list(r) for r in _SCHED], say=[0, 1])]),
        card("The matching (mine) and the words of the schedule",
             "The sports of the schedule are baseball (야구), basketball (농구), tae kwon do (태권도) and soccer (축구); the other five in the box (shooting, gymnastics, swimming, track and field, archery) are not on the schedule. The book glosses 선발전 as “a selection contest”, 프로 as “a professional” and 1차전 as “the 1st round; the first battle”.",
             tables=[ktable(_SCH_W)]),
        card("Activities left out",
             "Activity 1 (b) and Activity 2 (b) (listening to conversations and a sports news broadcast and filling in tables) are audio activities; Activity 3 (two groups read News Article A or B, exchange information in pairs, write a group news report on a flip chart and present it; sample questions: 어떤 스포츠 경기에 대해서 읽었어요? 어느 나라 팀이었어요? 누가 이겼어요? 어느 팀이 이겼어요?) is a group and class activity. The article texts of Activity 3 are not in the book’s text.",
             examples=[D("어떤 스포츠 경기에 대해서 읽었어요?", "What sports game did you read about? (the book’s sample question; English mine)"), D("어느 나라 팀이었어요?", "Which country’s team was it? (the book’s sample question; English mine)"), D("누가 이겼어요?", "Who won? (the book’s sample question; English mine)"), D("어느 팀이 이겼어요?", "Which team won? (the book’s sample question; English mine)")]),
    ],
    exercises=uniq(
        vocab_exercises(_MATCH) + _tr(_ART + _SCH_W + [(a, c) for a, b, c in _SCHED])
        + [M("What sport is reported in the article?", "Table tennis", ["Baseball", "Soccer", "Archery"], "탁구."), M("What place did the Korean women’s team take?", "Second place (runner-up)", ["First place", "Third place", "Last place"], "준우승."), M("Who did the Korean women’s team lose to in the final?", "China", ["Hungary", "Japan", "The U.S."], "중국팀에게 패했다."),
           M("What was the set score of the women’s final?", "3 to 2", ["3 to 1", "2 to 3", "7 to 2"], "삼 대 이."), M("Who did the men’s team beat?", "Hungary", ["China", "Japan", "Mexico"], "헝가리에게 이겼다."), M("What is the men’s team’s record?", "7 wins and 2 losses", ["2 wins and 7 losses", "3 wins", "1 win and 1 loss"], "칠 승 이 패."),
           M("Which sport has the game against Mexico?", "Baseball", ["Basketball", "Soccer", "Tae kwon do"], "한국 대 멕시코."), M("Which game is at 2:00 p.m. at the Dongdaemun Stadium?", "The soccer semifinal", ["The baseball game", "The basketball final", "The tae kwon do contest"], "축구 준결승전, 오후 두 시."),
           M("Which sport has a selection contest?", "Tae kwon do", ["Soccer", "Baseball", "Basketball"], "국가대표 선발전."), M("Which round of the basketball final is on the 18th?", "The 2nd game", ["The 1st game", "The 3rd game", "The 4th game"], "이차전은 십팔 일."),
           F("한국 여자 대표팀이 세계 탁구 대회에서 ___을 했다. (runner-up)", "준우승", ["우승", "응원"], "준우승 = second place."), F("한국팀은 중국팀에게 ___. (lost)", "패했다", ["이겼다", "비겼다"], "패하다 = to lose."), F("남자 대표팀은 헝가리에게 ___. (won)", "이겼다", ["졌다", "패했다"], "이기다 = to win."),
           read_q("탁구 대회"), read_q("준우승을 했다"), read_q("세트 스코어"), read_q("농구 결승전"), read_q("축구 준결승전")]
    ),
)

# ================================================================== L4: Topic B
_B_DLG = [
    ("손님", "와! 농장이 아주 크네요!", "Wow! The farm is very big!"),
    ("농장주인", "네, 저희 농장에는 과수원하고 동물농장도 있습니다.", "Yes, our farm has an orchard and an animal farm as well."),
    ("손님", "그럼 과수원에서 과일도 딸 수 있어요?", "Then can I pick fruit at the orchard, too?"),
    ("농장주인", "물론이죠. 그리고 딴 과일을 집에 가지고 갈 수도 있어요.", "Of course. And you can take the fruit you picked home."),
    ("손님", "그래요? 또 뭘 할 수 있어요?", "Really? What else can I do?"),
    ("농장주인", "밭에서 채소도 기를 수 있고 동물한테 먹이도 줄 수 있습니다.", "You can grow vegetables in the field and feed the animals, too."),
    ("손님", "여기에는 어떤 동물들이 있어요?", "What kinds of animals are here?"),
    ("농장주인", "저희 농장에는 토끼하고 오리, 닭, 양 등이 있습니다.", "Our farm has rabbits, ducks, chickens, sheep and so on."),
    ("손님", "그래요? 그런데 저기 저분들은 뭐 하시는 거예요?", "Really? By the way, what are those people over there doing?"),
    ("농장주인", "네, 지금 사과 나무를 심고 있습니다.", "Yes, they are planting apple trees now."),
    ("손님", "여기서 과일 나무도 기를 수 있어요?", "Can I grow fruit trees here, too?"),
    ("농장주인", "그럼요. 저희 주말농장에서는 다양한 체험을 해 볼 수 있습니다.", "Of course. At our weekend farm you can try various hands-on experiences."),
    ("손님", "저는 시골 생활을 해 본 적이 없는데 참 재미있을 것 같아요.", "I have never lived in the countryside, but it seems like it would be really fun."),
    ("농장주인", "네. 더 구경해 보세요. 그리고 질문이 있으시면 언제든지 또 하세요.", "Yes. Please look around more. And if you have a question, ask anytime."),
]
_B_WORDS = ["개", "고양이", "과수원", "그렇다", "기르다", "농장", "동물", "따다", "먹이", "밭", "새", "시골", "심다", "양", "언제든지", "오리", "-(으)ㄴ 적이 있다", "-(으)ㄴ 적이 없다", "이렇다", "저렇다", "질문", "참", "체험", "토끼"]
_NONG = [("농장", "a farm; “farming place” (the book’s core word)"), ("주말 농장", "a weekend farm (mine)"), ("농기계", "farm machinery (mine)"), ("농산물", "agricultural products (mine)"), ("산물", "a product; produce (the book’s hint, 産物)"), ("농업", "agriculture; “agricultural business” (the book’s example)"), ("농지", "a farmland (the book’s example)"), ("농부", "a farmer; “farming man” (the book’s example)")]
_FARM_T = [("농장", "a farm"), ("과수원", "an orchard"), ("기르다", "to raise; to grow"), ("따다", "to pick"), ("먹이", "feed; fodder"), ("밭", "a field"), ("질문", "a question"), ("체험하다", "to experience hands-on"), ("심다", "to plant"), ("언제든지", "whenever"), ("토끼", "a rabbit"), ("오리", "a duck"), ("개", "a dog"), ("고양이", "a cat"), ("새", "a bird"), ("양", "a sheep"), ("시골", "countryside")]
L4 = lesson(
    "Ch 19 · Topic B: Thank you for visiting our weekend farm",
    "저희 주말농장을 방문해 주셔서 감사합니다 · 과수원 · 동물 · 밭 · 심다 · 기르다 · 농 (農)",
    requires=[],
    cards=[
        card("Topic B: Thank you for visiting our weekend farm (저희 주말농장을 방문해 주셔서 감사합니다)",
             "A visitor at a weekend farm is talking with the owner. (The English is mine; the book gives none. The book’s footnote says 뭘 is a contracted form of 무엇을.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened. The book shows pictures of 양, 새, 고양이 and 개; the pictures are left out.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Cultural note: 주말농장 (“Weekend” Farm)",
             "주말농장 is a farm designed for city dwellers who want to experience country life with their families on weekends. Weekend farms started around 2002 when the Korean government encouraged businesses to implement a five-day work week instead of a six-day work week. Since then, the weekend farm business has grown quickly around metropolitan areas. Many families take advantage of the farms for family activities as well as for growing healthful, organic products."),
        card("Sino-Korean in use: 농 (農)",
             "This Sino-Korean syllable means agricultural or farming, as in 농업 (agriculture; “agricultural business”), 농지 (a farmland) and 농부 (a farmer; “farming man”). Since Korea used to be an agricultural society, many words including the same syllable are used to describe rural communities and farming businesses. The book asks you to guess the meaning of 농장, 주말 농장, 농기계 and 농산물, with the hint 산물 (産物): a product, produce. The answers are mine.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _NONG], say=[0])]),
        card("Activities left out",
             "The Presentation Activity (a table of core words, partner reading of Part A and Part B of the text, listening) and Follow-up 1 (a SMART Board activity) are partner, computer and audio activities. The first part of the Presentation Activity table is covered by the core word table above. Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not w.startswith("-")]))
        + _tr(_strip(_B_DLG) + _NONG + _FARM_T)
        + [M("Where is the visitor?", "At a weekend farm", ["At a department store", "At a school", "At a zoo"], "주말농장."), M("What does the farm have besides the orchard?", "An animal farm", ["A restaurant", "A hotel", "A pool"], "과수원하고 동물농장."), M("What can the visitor do at the orchard?", "Pick fruit and take it home", ["Only look at it", "Buy it at a discount", "Cook it"], "과일을 딸 수 있어요."),
           M("What can the visitor do in the field?", "Grow vegetables", ["Ride horses", "Play baseball", "Swim"], "밭에서 채소도 기를 수 있고."), M("Which animals are on the farm?", "Rabbits, ducks, chickens and sheep", ["Cows and horses", "Dogs and cats only", "Pigs and goats"], "토끼하고 오리, 닭, 양."),
           M("What are the people over there doing?", "Planting apple trees", ["Picking apples", "Feeding the rabbits", "Cooking lunch"], "사과 나무를 심고 있습니다."), M("Has the visitor lived in the countryside?", "No, never", ["Yes, often", "Yes, once", "He lives there now"], "시골 생활을 해 본 적이 없는데."),
           M("When can the visitor ask a question?", "Anytime", ["Only today", "Only at noon", "Never"], "언제든지 또 하세요."), M("What did the weekend farms respond to, around 2002?", "A five-day work week", ["A six-day work week", "A holiday", "A new law on farms"], "The government encouraged a five-day work week."),
           M("What does the Sino-Korean syllable 농 (農) mean?", "farming; agriculture", ["victory", "defeat", "a person"], "농업, 농장, 농부."), M("What does 농부 literally mean?", "“farming man”", ["“farming place”", "“agricultural business”", "“farm machine”"], "농부 = a farmer."), M("What does 농장 literally mean?", "“farming place”", ["“farming man”", "“agricultural business”", "“a field”"], "농장 = a farm."),
           F("저희 농장에는 과수원하고 동물 ___도 있습니다. (farm)", "농장", ["과수원", "시골"], "동물농장 = an animal farm."), F("과수원에서 과일도 ___ 수 있어요? (pick)", "딸", ["심을", "기를"], "따다 → 딸 수 있다."), F("밭에서 채소도 ___ 수 있어요. (grow)", "기를", ["딸", "줄"], "기르다 → 기를 수 있다."),
           F("지금 사과 나무를 ___ 있습니다. (planting)", "심고", ["따고", "주고"], "심다 → 심고 있다."), F("동물한테 ___도 줄 수 있습니다. (feed)", "먹이", ["새", "밭"], "먹이를 주다 = to feed."), F("___이 있으시면 언제든지 또 하세요. (a question)", "질문", ["체험", "시골"], "질문 = a question."),
           read_q("주말농장"), read_q("과수원"), read_q("동물농장"), read_q("사과 나무를 심고 있습니다"), read_q("언제든지")]
    ),
)

# ================================================================== L5: Topic B follow-up 2 and activities
_AD = [
    ("새싹 주말농장", "Saessak Weekend Farm"), ("가족과 함께하는 주말!", "A weekend with your family!"), ("가족과 함께 나무도 심고 과일도 딸 수 있습니다!", "You can plant trees and pick fruit together with your family!"),
]
_AD_T = [["편리한 교통", "서울에서 자동차로 삼십 분 거리", "Convenient transportation: 30 minutes by car from Seoul"], ["다양한 계절 활동", "아이들을 위한 체험학습 이벤트", "Various seasonal activities: hands-on learning events for children"],
         ["봄", "동물 먹이 주기", "Spring: feeding the animals"], ["여름", "과일 따기", "Summer: picking fruit"], ["가을", "허수아비 만들기", "Autumn: making scarecrows"], ["겨울", "눈사람 만들기", "Winter: making snowmen"], ["편리한 시설", "식당, 화장실, 주차장, 어린이 공원", "Convenient facilities: restaurant, restroom, parking lot, children’s park"]]
_ROUTINE = [("일어나다", "to get up"), ("나무와 채소에 물을 주다", "to water the trees and vegetables"), ("손님들을 위해 과일을 따다", "to pick fruit for the visitors"), ("동물한테 먹이를 주다", "to feed the animals"), ("아침을 먹다", "to eat breakfast"), ("손님들에게 농장을 구경시켜 주다", "to give a tour to the visitors"), ("농장 문을 열다", "to open the farm for the day"), ("농장 문을 닫다", "to close the farm for the day"), ("손님들과 나무를 심다", "to plant trees with the visitors")]
L5 = lesson(
    "Ch 19 · Topic B, Follow-up 2 and Activities: a weekend farm advertisement",
    "새싹 주말농장 · 나무를 심다 · 과일을 따다 · 허수아비 · 눈사람 · 편리한 시설",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): a weekend farm advertisement",
             "The book gives the advertisement of 새싹 주말농장 and asks you to fill in a table in English (activities for family, seasonal events, available facilities). The text is the book’s (the travel time is spelled out in Hangul; the telephone number, the address and the web address are left out); the English is mine. The book glosses 허수아비 as “a scarecrow”.",
             examples=passage(_AD),
             tables=[table(["Heading", "Content", "English (mine)"], _AD_T, say=[0, 1])]),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Activities for family", "Seasonal events", "Available facilities"], [["Planting trees; picking fruit", "Spring: feeding animals; summer: picking fruit; autumn: making scarecrows; winter: making snowmen", "Restaurant, restroom, parking lot, children’s park"]])]),
        card("Activities, Activity 2: the farmer’s daily routine (the items)",
             "The book lists nine items of a farmer’s daily routine in English (the first, “Get up”, is numbered 1 and the last, “Close the farm for the day”, is numbered 9 for you) and asks you to number the rest while listening to the farmer. The recording is not available; the items are shown here with my Korean wording (mine) as vocabulary practice only; the order is not given in the text.",
             tables=[table(["Korean (mine)", "English (the book’s item)"], [list(r) for r in _ROUTINE], say=[0])]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity), the listening of Activity 2 (the numbering of the routine) and Activity 3 (visiting a weekend farm: two weekend farm flyers and two radio interviews, filling in a table of location, positive and negative aspects and farm products, and choosing which farm to visit) are computer, audio or partner activities; the flyers of Activity 3 are not in the book’s text."),
    ],
    exercises=uniq(
        _tr(_AD + _ROUTINE + [(a, c) for a, b, c in _AD_T])
        + [M("How far is the farm from Seoul?", "30 minutes by car", ["30 minutes on foot", "3 hours by train", "A day by bus"], "서울에서 자동차로 삼십 분 거리."), M("What can children do in spring?", "Feed the animals", ["Pick fruit", "Make scarecrows", "Make snowmen"], "봄 동물 먹이 주기."),
           M("What can children do in summer?", "Pick fruit", ["Feed the animals", "Make scarecrows", "Make snowmen"], "여름 과일 따기."), M("What can children do in autumn?", "Make scarecrows", ["Pick fruit", "Feed the animals", "Make snowmen"], "가을 허수아비 만들기."),
           M("What can children do in winter?", "Make snowmen", ["Make scarecrows", "Pick fruit", "Plant trees"], "겨울 눈사람 만들기."), M("Which is NOT in the list of facilities?", "A swimming pool", ["A restaurant", "A parking lot", "A children’s park"], "식당, 화장실, 주차장, 어린이 공원."),
           M("What can families do together at the farm?", "Plant trees and pick fruit", ["Ride horses", "Fish", "Ski"], "나무도 심고 과일도 딸 수 있습니다."),
           F("가을에는 ___ 만들기를 할 수 있어요. (scarecrow)", "허수아비", ["눈사람", "먹이"], "허수아비 = a scarecrow."), F("서울에서 자동차로 삼십 분 ___입니다. (distance)", "거리", ["시설", "교통"], "삼십 분 거리 = a distance of 30 minutes."), F("가족과 함께 나무도 ___ 과일도 딸 수 있습니다. (plant)", "심고", ["따고", "주고"], "심다 → 심고."),
           read_q("새싹 주말농장"), read_q("가족과 함께하는 주말"), read_q("허수아비 만들기"), read_q("눈사람 만들기"), read_q("편리한 시설")]
    ),
)

# ================================================================== L6: Grammar A: -(으)ㄴ 적이 있다/없다
def _exp(verb):
    """-(으)ㄴ 적이 있어요 / 없어요: 먹다 -> 먹은 적이 있어요"""
    if verb == "기르다":
        return "기른"
    if verb == "듣다":
        return "들은"
    return attr(verb)[1]


def _try(verb):
    """-아/어 본 적이 있어요: 먹다 -> 먹어 본"""
    if verb == "기르다":
        return "길러 본"
    if verb == "듣다":
        return "들어 본"
    return informal(verb)[:-1] + " 본"


_EXP_V = [("가다", "to go"), ("먹다", "to eat"), ("보다", "to see; to watch"), ("심다", "to plant"), ("배우다", "to learn"), ("타다", "to ride"), ("읽다", "to read"), ("기르다", "to raise; to grow"), ("듣다", "to listen; to hear"), ("만나다", "to meet"), ("살다", "to live"), ("만들다", "to make")]
_EXP_EX = [("하와이에 간 적이 있어요.", "I have been to Hawaii."), ("하와이에 간 적이 없어요.", "I have not been to Hawaii."), ("발레 공연을 관람한 적이 있어요?", "Have you ever watched a ballet performance?"), ("한국에 간 적이 있어요.", "I have been to Korea (before)."),
           ("발레 공연을 본 일이 있어요?", "Have you ever watched a ballet performance?"), ("한국에 간 일이 있어요.", "I have been to Korea (before)."), ("김치를 먹어 본 적이 있어요.", "I have tried eating kimchi."), ("스키를 타 본 적이 없어요.", "I have not tried skiing."),
           ("김치를 먹은 적이 있습니까?", "Have you ever eaten kimchi before? (the book’s opening question)"), ("김치를 한 번 먹은 적이 있습니다.", "I have eaten kimchi once. (the book’s opening answer)")]
_EXP_MODEL = [("한국어를 배우다", "to learn Korean"), ("권투를 배우다", "to learn boxing"), ("양궁 경기를 보다", "to watch an archery game"), ("토끼한테 먹이를 주다", "to feed a rabbit"), ("스키를 타 보다", "to try skiing"), ("바다에서 수영하다", "to swim in the sea"), ("동물을 기르다", "to raise animals"), ("나무를 심어 보다", "to try planting trees")]
_EXP_Q = ["한국어를 배운 적이 있어요?", "권투를 배운 적이 있어요?", "양궁 경기를 본 적이 있어요?", "토끼한테 먹이를 준 적이 있어요?", "스키를 타 본 적이 있어요?", "바다에서 수영한 적이 있어요?", "동물을 기른 적이 있어요?", "나무를 심어 본 적이 있어요?"]
L6 = lesson(
    "Ch 19 · Grammar A: expressing a past experience with -(으)ㄴ 적이 있다 / 없다",
    "하와이에 간 적이 있어요 · 먹은 적이 없어요 · 먹어 본 적이 있어요 · -(으)ㄴ 일이 있다",
    requires=[],
    cards=[
        card("Expressing a past experience or event",
             "In English, “Have you ever eaten kimchi before?” and “I have eaten kimchi once” are typical ways to ask about or state previous experiences. In Korean, we use the expression -(으)ㄴ 적이 있다. Because 적 in -(으)ㄴ 적이 있다 means a (past) experience or time, the whole expression literally means “a past experience of having done (something) exists”.",
             examples=passage(_EXP_EX[:4]) + passage(_EXP_EX[8:])),
        card("The rule",
             "verb stem + (으)ㄴ 적이 있다 / 없다.",
             tables=[table(["Condition", "Rule", "Example"], [["When a verb stem ends in a consonant", "add 은 적이 있다 / 없다", "심다 → 심은 적이 있다; 먹다 → 먹은 적이 없다"], ["When a verb stem ends in a vowel", "add ㄴ 적이 있다 / 없다", "가다 → 간 적이 있다; 보다 → 본 적이 없다"]])]),
        card("Also -(으)ㄴ 일이 있다 / 없다, and -아/어 본 적이 있다 / 없다",
             "We can also use -(으)ㄴ 일이 있다 / 없다 to express past experiences. -(으)ㄴ 적이 있다 / 없다 is commonly used in conjunction with -아/어 보다. You learned in Chapter 8 that -아/어 보다 is used to express experimentation or experience, as in 한국 음식 먹어 봤어요 (I tried eating Korean food). Therefore, the pattern -아/어 본 적이 있다 / 없다 adds the meaning of having tried something in the past.",
             examples=passage(_EXP_EX[4:8])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (ㄹ-ending verbs lose ㄹ: 살다 → 산, 만들다 → 만든; 기르다 and 듣다 are irregular: 기른 / 길러 본, 들은 / 들어 본).",
             tables=[table(["Verb", "Meaning", "-(으)ㄴ 적이 있다", "-아/어 본 적이 있다"], [[v, m, _exp(v) + " 적이 있어요", _try(v) + " 적이 있어요"] for v, m in _EXP_V], say=[0, 2, 3])]),
        card("Follow-up 1 and 5: phrases and questions",
             "In Follow-up 1 partners read a phrase card and conjugate it with -(으)ㄴ 적이 있다 / 없다 and -아/어 본 적이 있다 / 없다 (the book’s model: 한국어를 배우다 → 한국어를 배운 적이 있어요 / 없어요; 한국어를 배워 본 적이 있어요 / 없어요). In Follow-up 5 (스키를 타 본 적이 있어요?) students ask each other about the activities below (the book’s list); the models are 체조를 배운 적이 있어요? / 네, 배운 적이 있어요. / 아니요, 배운 적이 없어요. Sentences for the list (mine):",
             tables=[table(["Phrase (the book)", "Question (mine)", "Meaning"], [[p, q, m] for (p, m), q in zip(_EXP_MODEL, _EXP_Q)], say=[0, 1])],
             examples=[D("체조를 배운 적이 있어요?", "Have you ever learned gymnastics? (the book’s model; English mine)"), D("네, 배운 적이 있어요.", "Yes, I have learned it. (the book’s model; English mine)"), D("아니요, 배운 적이 없어요.", "No, I have not learned it. (the book’s model; English mine)")]),
        card("Activities left out",
             "Follow-up 2 (listening to three dialogs in which a man asks a friend if she has ever experienced something) is an audio activity; Follow-up 1 (partner phrase cards) and Follow-up 5 (interviewing two classmates, marking O or X, writing a paragraph about one interviewee and posting it; the book’s model paragraph: 김영수 일병의 경험 — 김 일병은 한국 음식을 먹어 본 적이 있습니다. 하지만 한국에는 가 본 적이 없습니다) are partner and class activities."),
    ],
    exercises=uniq(
        _fk(_EXP_V, _exp, "-(으)ㄴ (past experience)", lambda v: [stem(v) + "는", stem(v) + "을", stem(v) + "은" if not has_final(stem(v)) else stem(v) + "ㄴ" if False else stem(v) + "는 것"])
        + [M(f"How do you say “I have never {m.replace('to ', '', 1)}” (the verb {v})?", _exp(v) + " 적이 없어요", [stem(v) + "는 적이 없어요", _exp(v) + " 적이 있어요", stem(v) + "을 적이 없어요"], f"{v} → {_exp(v)} 적이 없어요.") for v, m in _EXP_V[:6]]
        + [M(f"How do you say “I have tried to {m.replace('to ', '', 1)}” (the verb {v})?", _try(v) + " 적이 있어요", [_exp(v) + " 적이 있어요", _try(v) + " 적이 없어요", stem(v) + "어 본 적이 있어요" if False else stem(v) + "고 본 적이 있어요"], f"{v} → {_try(v)} 적이 있어요.") for v, m in _EXP_V[:5]]
        + _tr(_EXP_EX + _EXP_MODEL)
        + [F("하와이에 ___ 적이 있어요. (have been)", "간", ["가는", "갈"], "가다 ends in a vowel: 간."), F("김치를 먹___ 적이 있어요. (have eaten)", "은", ["ㄴ", "는"], "먹다 ends in a consonant: 먹은."), F("한국에 간 ___이 있어요. (experience)", "일", ["적", "것"], "-(으)ㄴ 일이 있다 = -(으)ㄴ 적이 있다."),
           F("스키를 타 ___ 적이 없어요. (tried)", "본", ["볼", "보는"], "-아/어 본 적이 없다."), F("시골 생활을 해 본 ___이 없어요. (experience)", "적", ["일을", "것이"], "해 본 적이 없다."), F("김치를 한 번 먹은 적이 ___. (there is)", "있습니다", ["없습니다", "합니다"], "있다 = there is."),
           M("What does 적 in -(으)ㄴ 적이 있다 mean?", "a (past) experience or time", ["a future plan", "a place", "a person"], "“a past experience of having done (something) exists”."), M("Which pattern adds the meaning of “having tried”?", "-아/어 본 적이 있다 / 없다", ["-(으)ㄹ 적이 있다", "-고 있다", "-는 중이다"], "-아/어 보다 + -(으)ㄴ 적이 있다."), M("What is the alternative to -(으)ㄴ 적이 있다?", "-(으)ㄴ 일이 있다", ["-(으)ㄹ 일이 있다", "-는 적이 있다", "-기로 하다"], "한국에 간 일이 있어요."),
           read_q("하와이에 간 적이 있어요"), read_q("발레 공연을 본 일이 있어요"), read_q("김치를 먹어 본 적이 있어요"), read_q("스키를 타 본 적이 없어요"), read_q("시골 생활을 해 본 적이 없어요")]
    ),
)

# ================================================================== L7: Grammar B: ㅎ irregular verbs
_HH = {"빨갛다": ("빨개요", "빨간", "빨갛게", "to be red"), "노랗다": ("노래요", "노란", "노랗게", "to be yellow"), "파랗다": ("파래요", "파란", "파랗게", "to be blue"), "하얗다": ("하얘요", "하얀", "하얗게", "to be white"), "까맣다": ("까매요", "까만", "까맣게", "to be black"),
       "이렇다": ("이래요", "이런", "이렇게", "to be like this"), "그렇다": ("그래요", "그런", "그렇게", "to be like it"), "저렇다": ("저래요", "저런", "저렇게", "to be like that"), "어떻다": ("어때요", "어떤", "어떻게", "to be like what/how")}
_HH_EXC = [("좋다", "to be good"), ("놓다", "to put; to place"), ("많다", "to be many; much"), ("괜찮다", "to be okay; to be decent"), ("넣다", "to put in"), ("낳다", "to give birth"), ("싫다", "to dislike (to be disagreeable)")]
_HH_EXC_F = {"좋다": ("좋아요", "좋은", "좋게"), "놓다": ("놓아요", "놓은", "놓게"), "많다": ("많아요", "많은", "많게"), "괜찮다": ("괜찮아요", "괜찮은", "괜찮게"), "넣다": ("넣어요", "넣은", "넣게"), "낳다": ("낳아요", "낳은", "낳게"), "싫다": ("싫어요", "싫은", "싫게")}
_HH_EX = [("사과는 빨개요.", "An apple is red."), ("빨간 사과", "a red apple; an apple which is red"), ("이런 컴퓨터 본 적 있어요?", "Have you seen this kind of computer?"), ("아니요, 그런 컴퓨터는 본 적이 없는데요.", "No, I have not seen that kind of computer."),
          ("저 빨간 차는 누구 차예요?", "Whose car is that red car?"), ("저 바다 좀 보세요. 아주 파래요.", "Look at the sea. It is very blue."), ("저는 한국 음식이 좋아요. 괜찮은 한국 식당 있으면 추천해 주세요.", "I like Korean food. Please recommend a decent Korean restaurant.")]
_COVERS = [("커피 한 잔 어때요?", "How about a cup of coffee?", "어떻다"), ("하얀 부채 까만 부채", "A white fan, a black fan", "하얗다, 까맣다"), ("친구와 함께 하는 이런 저런 이야기", "This and that story done with a friend", "이렇다, 저렇다"), ("아빠 왜 그래요?", "Dad, why are you like that?", "그렇다")]
_LISTB = [("집", "a house"), ("옷", "clothes"), ("신발", "shoes"), ("컴퓨터", "a computer"), ("시계", "a watch; a clock"), ("토끼", "a rabbit"), ("냉장고", "a refrigerator"), ("자동차", "a car"), ("과일", "fruit"), ("가방", "a bag")]
L7 = lesson(
    "Ch 19 · Grammar B: ㅎ irregular verbs",
    "빨갛다 → 빨개요 · 빨간 사과 · 하얗다 → 하얘요 · 이렇다 · 그렇다 · 어떻다 · 좋다 · 많다",
    requires=[],
    cards=[
        card("ㅎ irregular verbs",
             "You have already learned quite a few stative verbs whose stems end in ㅎ: 빨갛다 (to be red), 노랗다 (to be yellow), 파랗다 (to be blue), 하얗다 (to be white), 까맣다 (to be black), 이렇다 (to be like this), 그렇다 (to be like it), 저렇다 (to be like that) and 어떻다 (to be like what/how).\n\n"
             "These stative verbs are commonly known as “ㅎ irregular verbs” because they go through an extra step in their conjugation. When the stem is followed by a vowel or a consonant like ㄴ and ㄹ, the stem loses ㅎ, as if it were not part of the stem. For example, when 빨갛다 is conjugated into -아/어요 (informal style) or ㄴ (an attributive form), its stem 빨갛 loses ㅎ. It then goes through the normal conjugation: 빨갛 + 아요 → 빨가 + 아요 → 빨개요; 빨갛 + ㄴ → 빨가 + ㄴ → 빨간 (빨간 사과, a red apple).",
             examples=passage(_HH_EX[:2])),
        card("Examples",
             "The book’s examples:",
             examples=passage(_HH_EX[2:6])),
        card("The exceptions",
             "There are, of course, some exceptions. Even though their stems end in ㅎ, the following verbs do not lose ㅎ during the conjugation process: 좋다, 놓다 (to put; to place), 많다, 괜찮다 (to be okay / to be decent), 넣다, 낳다 (to give birth) and 싫다.",
             examples=passage(_HH_EX[6:]),
             tables=[table(["Verb", "Meaning", "-아/어요", "-(으)ㄴ", "-게"], [[v, m, *_HH_EXC_F[v]] for v, m in _HH_EXC], say=[0, 2, 3, 4])]),
        card("Follow-up 3 (Writing and speaking): conjugate the verbs",
             "The book gives a table with the verb stem, -(으)ㄴ, -아/어요 and -게, and asks you to conjugate (the book gives 하얘요 and 하얗게 for 하얗다, 노란, 파래요, 이런, 그렇게, 어떤, 많게 and 좋아요; the rest are my answers). The book’s footnote: 하얗다 becomes 하얘요 because ㅑ + ㅓ is contracted to ㅒ.",
             tables=[table(["Verb", "-아/어요", "-(으)ㄴ", "-게"], [[v, a, b, c] for v, (a, b, c, m) in _HH.items()] + [[v, *_HH_EXC_F[v]] for v in ("많다", "좋다")], say=[0, 1, 2, 3])]),
        card("Follow-up 3 b: verbs and nouns",
             "Partners pick a verb from List A and a noun from List B and make the attributive form (the book’s model: 하얗다 + 집 → 하얀 집). List A: 빨갛다, 노랗다, 파랗다, 하얗다, 까맣다, 이렇다, 그렇다, 저렇다, 어떻다, 괜찮다. List B: 집, 옷, 신발, 컴퓨터, 시계, 토끼, 냉장고, 자동차, 과일, 가방. Some phrases (mine):",
             tables=[table(["Noun", "Meaning", "빨간", "하얀", "까만", "이런", "괜찮은"], [[n, m, "빨간 " + n, "하얀 " + n, "까만 " + n, "이런 " + n, "괜찮은 " + n] for n, m in _LISTB[:6]], say=[0, 2, 3, 4, 5, 6])]),
        card("Follow-up 4 (Reading): book covers",
             "The book shows four book covers and asks you to circle the ㅎ irregular verbs, write their dictionary forms and translate the titles (the covers also show the authors and the publishers; the answers are mine).",
             tables=[table(["Cover title", "Meaning (mine)", "ㅎ irregular verbs"], [list(r) for r in _COVERS], say=[0, 2])]),
        card("Activities left out",
             "Follow-up 3 b (partner reading) is a partner activity. The book’s pictures of the book covers are left out; the titles were read from the page images."),
    ],
    exercises=uniq(
        [M(f"What is the informal form (-아/어요) of {v} ({m})?", a, [x for x in (v[:-1] + "아요", v[:-2] + "어요", v[:-1] + "어요", v[:-2] + "아요") if x != a][:3], f"{v} → {a}.") for v, (a, b, c, m) in _HH.items()]
        + [M(f"What is the attributive form (-(으)ㄴ) of {v}?", b, [x for x in (v[:-1] + "은", v[:-1] + "는", v[:-2] + "ㄴ", v[:-1] + "ㄴ") if x != b][:3], f"{v} → {b}.") for v, (a, b, c, m) in _HH.items()]
        + [M(f"What is the -게 form of {v}?", c, [x for x in (v[:-2] + "게", v[:-1] + "어게", v[:-2] + "ㄴ게", v[:-2] + "이게") if x != c][:3], f"{v} → {c}.") for v, (a, b, c, m) in _HH.items()]
        + [M(f"What is the -아/어요 form of {v} ({m})? (an exception: it keeps ㅎ)", _HH_EXC_F[v][0], [x for x in (v[:-2] + "아요" if len(v) > 2 else v[:-1] + "아요", v[:-1] + "래요", v[:-1] + "어요") if x != _HH_EXC_F[v][0]][:3], f"{v} → {_HH_EXC_F[v][0]}.") for v, m in _HH_EXC[:4] if v != "싫다"]
        + _tr(_HH_EX)
        + [M("What happens to the stem 빨갛 before -아요?", "It loses ㅎ and becomes 빨개요", ["It keeps ㅎ and becomes 빨갛아요", "It becomes 빨거요", "Nothing happens"], "빨갛 + 아요 → 빨가 + 아요 → 빨개요."), M("Which verb is an exception that keeps ㅎ?", "좋다", ["빨갛다", "하얗다", "이렇다"], "좋다 → 좋아요."), M("Why is 하얗다 → 하얘요?", "ㅑ + ㅓ is contracted to ㅒ", ["ㅏ + ㅏ is dropped", "ㅗ + ㅏ is contracted", "ㅓ is dropped"], "The book’s footnote."),
           F("저 ___ 차는 누구 차예요? (red)", "빨간", ["빨갛은", "빨강"], "빨갛다 + ㄴ → 빨간."), F("저 바다 좀 보세요. 아주 ___. (is blue)", "파래요", ["파랗아요", "파라요"], "파랗다 → 파래요."), F("한국 음식이 ___. (is good)", "좋아요", ["조아요", "좋래요"], "좋다 keeps ㅎ."),
           F("___ 컴퓨터는 본 적이 없는데요. (that kind of)", "그런", ["그렇은", "그럼"], "그렇다 + ㄴ → 그런."), F("하얀 집 means a ___ house", "white", ["black", "red"], "하얗다 = to be white."),
           read_q("빨간 사과"), read_q("하얀 집"), read_q("파래요"), read_q("이런 컴퓨터"), read_q("괜찮은 식당")]
    ),
)

# ================================================================== L8: Topic C
_C_DLG = [
    ("김진수", "선아 씨, 어떤 동호회에 관심 있어요?", "Sun-a, what kind of club are you interested in?"),
    ("오선아", "아직 잘 모르겠어요. 진수 씨는요?", "I don’t know yet. How about you, Jinsu?"),
    ("김진수", "전 산악 동호회 회원이에요.", "I am a member of the mountain club."),
    ("오선아", "그래요? 그런데 산악 동호회에 들면 뭐가 좋아요?", "Really? What is good about joining the mountain club?"),
    ("김진수", "무엇보다 사람들을 많이 사귈 수 있어서 좋아요. 그리고 저희 동호회는 등산을 자주 해서 회원들끼리 아주 친해요.", "Above all, it’s good because you can make many friends. And our club goes hiking often, so the members are very close with each other."),
    ("오선아", "그럼 얼마나 자주 만나요?", "Then how often do you meet?"),
    ("김진수", "어, 정기모임은 한 달에 두 번 있어요.", "Um, the regular meeting is twice a month."),
    ("오선아", "가입하면 회비도 내요?", "If I join, do I pay a membership fee, too?"),
    ("김진수", "네. 회비는 한 달에 삼만 원이에요.", "Yes. The membership fee is 30,000 won a month."),
    ("오선아", "그럼 어떻게 가입해요?", "Then how do I join?"),
    ("김진수", "내일 오후에 회원 가입에 대한 오리엔테이션이 있어요. 거기서 가입 신청서만 쓰시면 돼요.", "Tomorrow afternoon there is an orientation about joining as a member. You only need to fill out the application form there."),
]
_C_WORDS = ["가입", "~끼리", "당구", "동호회", "들다", "등산화", "무엇보다", "배드민턴", "번지 점프", "사귀다", "산악", "스쿠버 다이빙", "신청서", "~에 대한", "오리엔테이션", "인라인 스케이트", "정기", "초보자", "친하다", "회비", "회원"]
_FLY_A = [("매주 한 번씩 만납니다.", "We meet once every week."), ("전국의 유명한 산에 갑니다.", "We go to famous mountains all over the country."), ("연휴에는 야영도 합니다.", "On long holidays we also camp."), ("이십 세 이상이면 누구나 가입할 수 있습니다.", "Anyone aged 20 or older can join.")]
_FLY_B = [("한 달에 두 번 모입니다.", "We gather twice a month."), ("수영을 할 줄 알아야 합니다.", "You must know how to swim."), ("다이빙 장비를 빌려 드립니다.", "We lend you diving equipment."), ("회비는 일 년에 십만 원입니다.", "The membership fee is 100,000 won a year.")]
_FORM = [("회원 가입 신청서", "membership application form"), ("동호회 이름", "club name"), ("회원 이름", "member’s name"), ("직업", "occupation"), ("전화 번호", "telephone number"), ("주소", "address"), ("저는 동호회 가입을 신청합니다.", "I apply to join the club."), ("년 월 일", "year, month, day"), ("서명", "signature")]
L8 = lesson(
    "Ch 19 · Topic C: I would like to join a club",
    "동호회에 가입하고 싶어요 · 산악 동호회 · 회원 · 회비 · 정기모임 · 신청서",
    requires=[],
    cards=[
        card("Topic C: I would like to join a club (동호회에 가입하고 싶어요)",
             "Ms. Oh, a new employee, is talking with her colleague Mr. Kim as she is reading a club orientation poster on the company’s bulletin board. (The English is mine; the book gives none. The book writes 3만 원; it is spelled out here.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Follow-up 1 a (Reading and writing): two club flyers",
             "The book gives two club recruitment flyers whose names have been removed and asks you to find the missing activities in the box (mountain hiking, scuba diving, table tennis, billiards) and write them in Korean. The texts are the book’s (the age and the fee are spelled out in Hangul; the telephone number and the web address are left out); the English is mine.",
             examples=passage(_FLY_A) + passage(_FLY_B)),
        card("The answers (mine)",
             "The book leaves the answers blank; these are my answers. The first flyer is for the mountain hiking club (등산 동호회); the second is for the scuba diving club (스쿠버 다이빙 동호회). Table tennis (탁구) and billiards (당구) are not used.",
             tables=[table(["Flyer", "Club", "Clue"], [["1", "등산 동호회", "meets weekly; goes to famous mountains; camps on long holidays"], ["2", "스쿠버 다이빙 동호회", "you must know how to swim; they lend diving equipment"]], say=[1])]),
        card("Follow-up 1 b: a membership application form",
             "The book gives a generic club membership application form; you circle the new words from Chapter 19, choose one of the clubs and complete and sign the form. The headings of the form (the book glosses 서명 as “signature”; the English is mine otherwise):",
             tables=[table(["Form", "Meaning"], [list(r) for r in _FORM], say=[0])]),
        card("Activities left out",
             "The SMART Board activities and the partner role-play of the Presentation Activity, Follow-up 1 b (completing and signing the form) and Follow-up 2 (listening to a call to a club and filling in a table of the type of club, the frequency of meetings and the membership fee) are computer, audio, partner or class activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not w.startswith("~")]))
        + _tr(_strip(_C_DLG) + _FLY_A + _FLY_B + _FORM)
        + [M("What club is Mr. Kim a member of?", "The mountain club", ["The scuba diving club", "The billiards club", "The soccer club"], "산악 동호회 회원이에요."), M("What does Mr. Kim say is good about joining, above all?", "You can make many friends", ["It is cheap", "It is near", "You get a gift"], "사람들을 많이 사귈 수 있어서 좋아요."),
           M("Why are the club members close?", "They go hiking often", ["They live together", "They work together", "They are family"], "등산을 자주 해서 회원들끼리 아주 친해요."), M("How often is the regular meeting?", "Twice a month", ["Once a week", "Once a year", "Every day"], "한 달에 두 번."),
           M("How much is the membership fee?", "30,000 won a month", ["3,000 won a month", "300,000 won a month", "30,000 won a year"], "한 달에 삼만 원."), M("What is tomorrow afternoon?", "An orientation about joining", ["A regular meeting", "A hiking trip", "A party"], "회원 가입에 대한 오리엔테이션."),
           M("What does Ms. Oh need to do at the orientation?", "Fill out the application form", ["Pay the full fee", "Bring a friend", "Take a test"], "가입 신청서만 쓰시면 돼요."), M("Which flyer is for the scuba diving club?", "The one that says you must know how to swim", ["The one with weekly meetings", "The one that goes camping", "Neither"], "수영을 할 줄 알아야 합니다."),
           M("How much is the scuba diving club’s fee?", "100,000 won a year", ["30,000 won a month", "10,000 won a month", "Free"], "일 년에 십만 원."), M("Who can join the mountain hiking club?", "Anyone aged 20 or older", ["Only students", "Only members’ friends", "Anyone aged 30 or older"], "이십 세 이상이면 누구나."),
           F("그런데 산악 동호회에 ___ 뭐가 좋아요? (if I join)", "들면", ["가면", "먹으면"], "들다 = to join (a club)."), F("정기모임은 한 달에 두 ___ 있어요. (times)", "번", ["명", "개"], "두 번 = twice."), F("가입하면 ___도 내요? (membership fee)", "회비", ["회원", "신청서"], "회비 = a membership fee."),
           F("회원 가입에 ___ 오리엔테이션이 있어요. (about)", "대한", ["대해서", "대하여"], "에 대한 + noun."), F("회원들___ 아주 친해요. (with each other)", "끼리", ["하고", "에게"], "~끼리 = together (with what shares the same characteristics)."), F("가입 ___만 쓰시면 돼요. (application form)", "신청서", ["회비", "오리엔테이션"], "신청서 = an application."),
           read_q("산악 동호회"), read_q("정기모임"), read_q("회비는 한 달에 삼만 원이에요"), read_q("가입 신청서"), read_q("회원들끼리 친해요")]
    ),
)

# ================================================================== L9: Grammar C: 에 대해(서) vs 에 대한
_DAE_EX = [("한국에 대해서 말해 주세요.", "Please tell us about Korea."), ("한국에 대한 이야기가 재미있어요.", "The story about Korea is interesting."), ("미국 역사에 대하여 얘기합니다.", "We talk about American history."), ("한국 영화에 대해서 공부합니다.", "I study about Korean movies."),
           ("취미에 대한 책", "a book about hobbies"), ("친구에 대한 걱정", "a worry about a friend"), ("저는 한국 역사에 대해서 몰라요.", "I do not know about Korean history."), ("한국 음식에 대해 잘 알아요.", "I know about Korean food."),
           ("한국 역사에 대한 책을 읽었어요.", "I read a book about Korean history."), ("한국 음식에 대한 정보가 필요해요.", "I need information about Korean food.")]
_DAE_FU1 = [("선생님이 한국에 ___ 설명해 주었어요.", "대해서", "대한", "The teacher explained about Korea to us."), ("서점에 한국에 ___ 책이 많아요.", "대한", "대해서", "There are many books about Korea at the bookstore."), ("저는 요즘 한국에 ___ 공부하고 있어요.", "대하여", "대한", "These days I am studying about Korea."),
            ("어제 신문에서 한국에 ___ 이야기를 읽었어요.", "대한", "대하여", "Yesterday I read a story about Korea in the newspaper."), ("제 친구는 한국에 ___ 잘 몰라요.", "대해서", "대한", "My friend doesn’t know much about Korea.")]
L9 = lesson(
    "Ch 19 · Grammar C: two ways to say “about”, ~에 대해(서) and ~에 대한",
    "한국에 대해서 말해 주세요 · 한국에 대한 이야기 · 대하여 · 대해서 · 대한",
    requires=[],
    cards=[
        card("Two ways to express “about” or “regarding”",
             "The postpositional phrase ~에 대해(서), ~에 대하여(서) or ~에 대한 is equivalent to the English prepositional phrase about ~, regarding ~, concerning ~, with regard to ~, of ~, on ~, etc. Thus 한국에 대해서, 한국에 대하여서 and 한국에 대한 can be translated as about Korea or regarding Korea. However, ~에 대해(서) / 대하여(서) is designated to modify verbs only, whereas ~에 대한 is designated to modify nouns only.",
             examples=passage(_DAE_EX[:2])),
        card("Why they differ",
             "Note that ~에 대해서 in the first sentence modifies the verb 말해 주세요, whereas ~에 대한 in the second sentence modifies the noun 이야기 that immediately follows. The postpositional phrases ~에 대해(서), ~에 대하여(서) and ~에 대한 originate from the verb 대하다 (just the way the English prepositions concerning and regarding originate from the verbs concern and regard). 대해(서) or 대하여(서) is made up of the stem of the verb 대하다 and the conjunctive ending -아/어서, which has to be followed by a verb or sentence. On the other hand, 대한 is made up of the same stem of the verb 대하다 and the attributive form ㄴ, which has to be followed by a noun."),
        card("The rule",
             "~에 대해(서) / 대하여(서) … + verb; ~에 대한 + noun.",
             tables=[table(["Condition", "Rule", "Example"], [["When followed by a verb", "add 에 대해(서) / 대하여", "미국 역사에 대하여 얘기합니다. 한국 영화에 대해서 공부합니다."], ["When followed by a noun", "add 에 대한", "취미에 대한 책; 친구에 대한 걱정"]], say=[2])],
             examples=passage(_DAE_EX[2:])),
        card("Follow-up 1 (Reading): choose the appropriate form",
             "The book gives five sentences all “about” Korea and asks you to circle the appropriate grammar feature in parentheses (대해서 / 대한; 대하여 / 대한). The sentences are the book’s; the answers and the English are mine.",
             tables=[table(["Sentence", "Answer (mine)", "Meaning (mine)"], [[a.replace("___", "(    )"), b, d] for a, b, c, d in _DAE_FU1], say=[0, 1])]),
        card("Activities left out",
             "Follow-up 2 (listening to a conversation in which a woman asks her co-worker about joining a club and identifying whether a noun or a verb follows ‘about’) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_DAE_EX)
        + [F(a, b, [c, "대하는" if False else "대해"] if b != "대해" else [c, "대한"], f"{b}: {d}") for a, b, c, d in _DAE_FU1]
        + [M(f"Which is correct? {a.replace('___', '(    )')}", b, [c, "대하는", "대해는"], f"{b}: it is followed by a {'noun' if b == '대한' else 'verb'}.") for a, b, c, d in _DAE_FU1]
        + [M("What does ~에 대한 modify?", "A noun", ["A verb", "A sentence", "Nothing"], "대한 + noun."), M("What does ~에 대해(서) modify?", "A verb", ["A noun", "A number", "Nothing"], "대해서 + verb."), M("What verb do these phrases come from?", "대하다", ["대답하다", "대구하다", "대하이다"], "대하다 = to concern; to regard."),
           M("What is 대해(서) made of?", "The stem of 대하다 and -아/어서", ["The stem of 대하다 and ㄴ", "The stem of 대하다 and -고", "The stem of 대하다 and -지만"], "-아/어서 has to be followed by a verb or sentence."), M("What is 대한 made of?", "The stem of 대하다 and the attributive ㄴ", ["The stem of 대하다 and -아/어서", "The stem of 대하다 and -고", "The stem of 대하다 and -지만"], "ㄴ has to be followed by a noun."),
           F("한국에 ___ 말해 주세요. (about; verb follows)", "대해서", ["대한", "대하는"], "말해 주세요 is a verb."), F("한국에 ___ 이야기가 재미있어요. (about; noun follows)", "대한", ["대해서", "대하여"], "이야기 is a noun."),
           read_q("한국에 대해서 말해 주세요"), read_q("한국에 대한 이야기"), read_q("취미에 대한 책"), read_q("친구에 대한 걱정"), read_q("한국 음식에 대한 정보")]
    ),
)

# ================================================================== L10: Grammar D: incomplete sentences
_INC = [("어제 어디에서 공부했어요?", "Where did you study yesterday?"), ("도서관에서요.", "In the library."), ("누구하고요?", "With whom?"), ("혼자요.", "Alone."), ("몇 시에요?", "At what time?"), ("아침에요.", "In the morning."), ("뭐 공부했어요?", "What did you study?"), ("한국말이요.", "Korean."), ("왜요?", "Why?"), ("월요일에 시험이 있어서요.", "Because I have a test on Monday.")]
_INC_T = [("점심 드셨습니까, 김 선생님?", "Have you eaten lunch, Ms. Kim?"), ("네. 김 일병은요?", "Yes. How about you, PFC Kim?"), ("저도요.", "Me too."), ("교실에서 영어 해도 돼요?", "Are we allowed to speak English in the classroom?"), ("안 돼요.", "You may not."), ("사무실에서는요?", "What about in the office?")]
_INC_F3 = [("남", "오 선생님, 토요일에 뭐 하셨어요?", "Ms. Oh, what did you do on Saturday?"), ("여", "김 선생님하고 쇼핑했어요.", "I went shopping with Mr. Kim."), ("남", "어디에서요?", "Where? (mine)"), ("여", "델몬티 쇼핑센터에서요.", "At the Del Monte Shopping Center."),
            ("여", "문 선생님은 뭐 하셨어요?", "Mr. Moon, what did you do?"), ("남", "토요일에는 영화 보러 갔어요.", "On Saturday I went to see a movie."), ("여", "그럼, 일요일에는요?", "Then, what about Sunday? (mine)"), ("남", "일요일에는 집에서 야구 경기를 봤어요.", "On Sunday I watched a baseball game at home."),
            ("여", "문 선생님은 무슨 영화를 좋아하세요?", "Mr. Moon, what kind of movie do you like?"), ("남", "공포영화요.", "Horror movies. (mine)"), ("여", "그래요? 저는 공포영화는 무서워요. 그래서 공포영화는 잘 안 봐요.", "Really? Horror movies are scary to me. So I don’t watch them often."),
            ("남", "오 선생님은 수영장에 자주 가세요?", "Ms. Oh, do you go to the swimming pool often?"), ("여", "아니요, 자주 안 가요.", "No, I don’t go often."), ("남", "왜요?", "Why? (mine)"), ("여", "시간이 없어서요.", "Because I don’t have time.")]
_INC_F4 = [("민호", "지영 씨, 취미가 뭐예요?", "Jiyeong, what is your hobby?"), ("지영", "당구요. 민호 씨는요?", "Billiards. How about you, Minho? (the book’s model, with the speakers as in the book)"), ("민호", "저는 수영이요.", "I do swimming."), ("지영", "주로 어디에서 해요?", "Where do you mainly do it?"), ("민호", "체육관에서요. 지영 씨는요?", "At the gym. How about you, Jiyeong?")]
L10 = lesson(
    "Ch 19 · Grammar D: incomplete sentences and the polite 요",
    "도서관에서요 · 혼자요 · 한국말이요 · 은/는요 · 김 일병은요? · 저도요",
    requires=[],
    cards=[
        card("Expressing incomplete sentences",
             "In casual and spontaneous conversations we frequently speak in incomplete sentences or phrases. The book gives an English exchange in which only one of the eight utterances is a complete sentence (A: Where did you say you went over the weekend? B: San Jose. A: By yourself? B: With my ex. A: You mean Sandra? B: Yup. A: Why? B: Because she wanted to.). This phenomenon is universal. In Korean, however, we add 요 to an incomplete sentence when we need to show respect to the person to whom we are speaking. Otherwise, we use the incomplete sentence without 요. (The book writes 어제 어디에서 공부했어(요)? with an optional 요.)",
             examples=dlg([("가", _INC[0][0], _INC[0][1]), ("나", _INC[1][0], _INC[1][1]), ("가", _INC[2][0], _INC[2][1]), ("나", _INC[3][0], _INC[3][1]), ("가", _INC[4][0], _INC[4][1]), ("나", _INC[5][0], _INC[5][1]), ("가", _INC[6][0], _INC[6][1]), ("나", _INC[7][0], _INC[7][1]), ("가", _INC[8][0], _INC[8][1]), ("나", _INC[9][0], _INC[9][1])])),
        card("The note on 이요 and the topic marker 은/는(요)",
             "The book’s footnote: 이요 is used when the preceding word is a noun that ends in a consonant (한국말이요). The topic marker 은/는(요), as in 점심은요? or 도서관에서는요?, is equivalent to “What about …?” or “How about …?” in English.",
             examples=dlg([("가", _INC_T[0][0], _INC_T[0][1]), ("나", _INC_T[1][0], _INC_T[1][1]), ("가", _INC_T[2][0], _INC_T[2][1]), ("가", _INC_T[3][0], _INC_T[3][1]), ("나", _INC_T[4][0], _INC_T[4][1]), ("가", _INC_T[5][0], _INC_T[5][1])])),
        card("Follow-up 3 (Reading): fill in the blanks using 요",
             "The book gives four dialogs between two Korean instructors about their past weekend activities, with a blank in each, and asks you to fill in the blanks with phrases using 요. The dialogs are the book’s; the blanks are filled with my answers (marked mine) and the English is mine.",
             examples=dlg(_INC_F3)),
        card("Follow-up 4 (Speaking): hobbies",
             "The book gives a model conversation about hobbies (the book asks partners to exchange information about when, where, why, how often and with whom they enjoy two activities; in Step c to a friend, you drop 요). The model (the English is mine):",
             examples=dlg(_INC_F4)),
        card("Activities left out",
             "Follow-up 4 (the table of hobbies and the partner conversations, first with a co-worker with 요 and then with a friend without 요) is a partner activity."),
    ],
    exercises=uniq(
        _tr(_INC + _INC_T + [(b, d) for a, b, d in _INC_F3])
        + [M("How do you say “In the library.” politely and briefly?", "도서관에서요.", ["도서관에서.", "도서관을요.", "도서관이요."], "With respect, add 요."), M("How do you say “Alone.” politely and briefly?", "혼자요.", ["혼자.", "혼자는.", "혼자가요."], "혼자요."),
           M("Which is used after a noun ending in a consonant: 이요 or 요?", "이요", ["요", "는요", "에요"], "한국말이요."), M("What does 점심은요? mean?", "How about lunch?", ["Is it lunch?", "Why lunch?", "Where is lunch?"], "은/는(요) = What about … ? / How about … ?"),
           M("What does 도서관에서는요? mean?", "What about in the library?", ["Why in the library?", "Is it the library?", "Who is in the library?"], "에서는요 = what about at … ?"), M("What does 김 일병은요? mean?", "How about you, PFC Kim?", ["Is PFC Kim here?", "Where is PFC Kim?", "Why PFC Kim?"], "은요 = how about …?"),
           M("When do we add 요 to an incomplete sentence?", "When we need to show respect to the listener", ["When we ask a question", "When we are angry", "When we are in a hurry"], "Otherwise we drop it."), M("In Follow-up 3, which phrase fits the blank after 델몬티 쇼핑센터에서요?", "어디에서요?", ["왜요?", "누구하고요?", "몇 시에요?"], "The answer is a place."),
           M("Which phrase fits the blank before 시간이 없어서요?", "왜요?", ["어디에서요?", "누구하고요?", "몇 시에요?"], "The answer is a reason."),
           F("어제 어디에서 공부했어요? — 도서관에서___. (polite)", "요", ["이요", "는요"], "에서 ends in a vowel: 에서요."), F("뭐 공부했어요? — 한국말___. (polite)", "이요", ["요", "은요"], "한국말 ends in a consonant: 한국말이요."), F("점심 드셨어요? 네. 선생님___? (how about you)", "은요", ["이요", "요"], "선생님 ends in a consonant: 선생님은요?"),
           read_q("도서관에서요"), read_q("한국말이요"), read_q("시간이 없어서요"), read_q("김 일병은요"), read_q("공포영화요")]
    ),
)

# ================================================================== L11: Activities C: club posters
_POST1 = [("아름다운 바다로 여행 가자!", "Let’s travel to the beautiful sea!"), ("스쿠버 다이빙의 세계에 풍덩 빠져 보자!", "Let’s dive right into the world of scuba diving!"), ("십구 세 이상 누구나 가입 환영", "Everyone aged 19 or older is welcome to join"), ("월 회비 만 원", "Monthly membership fee: 10,000 won"),
           ("정기모임 매달 둘째 주 토요일", "Regular meeting: the second Saturday of every month"), ("회원 가입은 방문하거나 신청서를 클릭하세요.", "To join, visit or click the application form. (my reading of the book’s ‘방문, 신청서 클릭’; the book’s web address is left out)"), ("여러분의 많은 관심 부탁드려요.", "We ask for your great interest. (the book writes ‘부탁드려요~’)")]
_POST2 = [("하늘을 날아본 적이 있으십니까?", "Have you ever flown in the sky?"), ("번지 점프에 도전해 보세요!", "Take on the challenge of bungee jumping!"), ("월 회비 만 오천 원", "Monthly membership fee: 15,000 won"), ("정기모임은 매달 마지막 주 일요일에 있습니다.", "The regular meeting is on the last Sunday of every month."),
          ("이십 세 이상이면 가입하실 수 있습니다.", "Anyone aged 20 or older can join."), ("골드 스포츠 센터로 오세요!", "Come to the Gold Sports Center!"), ("바로 가입하실 수 있습니다.", "You can join right away.")]
L11 = lesson(
    "Ch 19 · Activities C: two club posters",
    "스쿠버 다이빙 · 번지 점프 · 월 회비 · 정기모임 · 가입 · 골드 스포츠 센터",
    requires=[],
    cards=[
        card("Activity 2 (Reading): two club posters",
             "The book gives two Korean club posters designed to recruit new members and asks you to fill in a table in English (membership fee, regular meeting times, member qualifications, how to apply). The texts are the book’s (the figures are spelled out in Hangul; the web address is left out; the poster texts were read from the page image); the English is mine. The scuba diving poster:",
             examples=passage(_POST1)),
        card("The bungee jumping poster",
             "The second poster (the English is mine):",
             examples=passage(_POST2)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Club", "Membership fee", "Regular meeting times", "Member qualifications", "How to apply"], [["Scuba diving", "10,000 won a month", "The second Saturday of every month", "Age 19 or older, anyone", "Through the web address on the poster (visit, click the application form)"], ["Bungee jumping", "15,000 won a month", "The last Sunday of every month", "Age 20 or older", "Come to the Gold Sports Center and join right away"]])]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity and listening to short dialogs at an orientation, writing the questions and answers in English), Activity 3 (listening to dialogs between a club recruiter and a visitor and filling in a table) and Activity 4 (a club fair: making a poster on a flip chart with the main activities, membership fee, regular meeting times, application procedure, member qualification and attractive factors, and presenting it in pairs) are computer, audio, partner or class activities. The book’s pictures of the posters are left out."),
    ],
    exercises=uniq(
        _tr(_POST1 + _POST2)
        + [M("What is the monthly fee of the scuba diving club?", "10,000 won", ["15,000 won", "100,000 won", "1,000 won"], "월 회비 만 원."), M("What is the monthly fee of the bungee jumping club?", "15,000 won", ["10,000 won", "150,000 won", "1,500 won"], "월 회비 만 오천 원."),
           M("When does the scuba diving club meet?", "The second Saturday of every month", ["The last Sunday of every month", "Every Monday", "Every day"], "매달 둘째 주 토요일."), M("When does the bungee jumping club meet?", "The last Sunday of every month", ["The second Saturday of every month", "Every Monday", "Every day"], "매달 마지막 주 일요일."),
           M("What age can join the bungee jumping club?", "20 or older", ["19 or older", "Anyone", "30 or older"], "이십 세 이상이면 가입하실 수 있습니다."), M("What age can join the scuba diving club?", "19 or older", ["20 or older", "Anyone", "30 or older"], "십구 세 이상 누구나."),
           M("Where do you go to join the bungee jumping club?", "The Gold Sports Center", ["The scuba diving shop", "The school", "A farm"], "골드 스포츠 센터로 오세요."),
           F("번지 점프에 ___ 보세요! (take on the challenge)", "도전해", ["가입해", "응원해"], "도전하다 = to challenge."), F("매달 둘째 주 ___ (Saturday)", "토요일", ["일요일", "월요일"], "토요일 = Saturday."), F("월 ___ 만 원 (membership fee)", "회비", ["회원", "신청서"], "회비 = a membership fee."),
           read_q("스쿠버 다이빙의 세계"), read_q("번지 점프에 도전해 보세요"), read_q("매달 마지막 주 일요일"), read_q("골드 스포츠 센터"), read_q("바로 가입하실 수 있습니다")]
    ),
)

# ================================================================== L12: Core vocabulary and self-evaluation
_CV_SECS = [("Sports", _CV_SPORT), ("Sports related", _CV_REL), ("On the farm", _CV_FARM), ("Animals", _CV_ANI), ("Hobby / club related", _CV_CLUB), ("Other words", _CV_OTH), ("Loan words", _CV_LOAN), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not r[0].startswith(("~", "-")) and "(" not in r[0]]
L12 = lesson(
    "Ch 19 · Core vocabulary and self-evaluation",
    "주요 단어 · 스포츠 · 농장 · 동물 · 동호회 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (TV → 티브이, 100 m → 백 미터, 8대 4 → 팔 대 사, 5대 5 → 오 대 오, 10개국 → 열 개국, 3승 2패 → 삼 승 이 패). The book’s 권투 and 복싱 are listed separately here; the book’s 따다 has two example sentences (one for each meaning; both are kept, joined by a slash). The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about common sporting events in Korea; talk about general activities on a “weekend” farm as well as common farm animals; and talk about common “hobby” clubs and outdoor activities.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -(으)ㄴ 적이 있다; -(으)ㄴ 적이 없다; incomplete sentences; ~에 대해(서) vs. ~에 대한 (about; regarding); ㅎ irregular verbs; and the Sino-Korean syllables 승 (勝), 패 (敗) and 농 (農)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does ~에 대한 mean?", "about; regarding", ["because of", "after", "instead of"], "이 대학의 역사에 대한 설명."), M("What does -(으)ㄴ 적이 있다 mean?", "to have past experience of having done something", ["to be about to do", "to want to do", "to be able to do"], "유럽에 가 본 적이 있어요?"),
           M("What does -(으)ㄴ 적이 없다 mean?", "to have no past experience of having done something", ["to have just done", "to not want to do", "to not be able to do"], "북한에 가 본 적이 없습니다."), M("What does the Sino-Korean syllable 농 (農) mean?", "farming; agriculture", ["victory", "defeat", "a club"], "농부, 농업, 농장."),
           M("What does 승 (勝) mean?", "victory; winning", ["defeat; loss", "farming", "a member"], "승자, 승전, 우승."), M("What does 패 (敗) mean?", "defeat; loss", ["victory; winning", "farming", "a member"], "패자, 패전."),
           M("What is “a member of a club”?", "회원", ["회비", "신청서", "초보자"], "회원 = a member."), M("What is “a membership fee”?", "회비", ["회원", "신청서", "정기"], "회비 = a membership fee."), M("What is “a beginner”?", "초보자", ["선수", "회원", "고객"], "초보자 = a novice; a beginner."),
           M("What is “an athlete; a player”?", "선수", ["초보자", "회원", "팀"], "선수 = an athlete; a player.")]
        + [read_q("주요 단어"), read_q("스포츠와 야외 활동"), read_q("인라인 스케이트"), read_q("스쿠버 다이빙"), read_q("오리엔테이션")]
    ),
)

UNIT = unit("Semester 1 · Unit 5 · Chapter 19: Sports and Outdoor Activities (스포츠와 야외 활동)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])

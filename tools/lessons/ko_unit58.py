"""Unit 58: KBC Semester III, Unit 15, Lesson 3 - Crimes (범죄).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 15, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_P1 = [("범행을 저지르다", "to commit a crime"), ("딱지를 떼이다", "to get a ticket"), ("몸싸움을 벌이다", "to get into a scuffle"), ("위조지폐를 찍어내다", "to print counterfeit bills"), ("나쁜 수법을 사용하다", "to con someone; “to use an evil method” (the book’s example)"), ("마약을 밀수하다", "to smuggle drugs"), ("박 교수를 납치하다", "to kidnap Professor Park")]
_P2 = [("순서", "차례"), ("상습(적)", "습관(적)"), ("건널목", "횡단보도"), ("들키다", "발각되다"), ("위협하다", "협박하다"), ("모으다", "수집하다"), ("체포되다", "잡히다"), ("용의자", "피의자")]
_P2E = [("순서", "order; sequence"), ("차례", "order; turn"), ("상습", "habit; habitual"), ("습관", "a habit"), ("건널목", "a crossing"), ("횡단보도", "a crosswalk"), ("들키다", "to be found out"), ("발각되다", "to be discovered"), ("위협하다", "to threaten"), ("협박하다", "to threaten; to blackmail"), ("모으다", "to collect; to gather"), ("수집하다", "to collect"), ("체포되다", "to be arrested"), ("잡히다", "to be caught"), ("용의자", "a suspect"), ("피의자", "a suspect (in a criminal case)")]
_HJ3 = [("力 력", "power; strength", "폭력, 강력"), ("民 민", "people; folks", "수재민, 민사"), ("犯 범", "commit; violate", "범죄, 침범"), ("事 사", "work; service", "사건, 형사"), ("署 서", "public office", "경찰서, 세무서")]
_HJW3 = [("폭력", "violence"), ("강력", "strong; powerful"), ("수재민", "flood victims"), ("민사", "civil affairs"), ("범죄", "a crime"), ("침범", "invasion"), ("사건", "an incident; a case"), ("형사", "a (police) detective"), ("경찰서", "a police station"), ("세무서", "Tax Revenue Services; IRS office")]
_OPP3 = [("민사", "형사", "civil affairs ↔ criminal affairs"), ("폭력", "평화", "violence ↔ peace"), ("경범", "강력범", "a minor offense ↔ a violent criminal")]
_SIM3 = [("범인", "범죄자", "a criminal ≈ a criminal (offender)"), ("침범", "침입", "invasion ≈ intrusion"), ("폭락", "급락", "a plunge ≈ a sharp fall")]
_REL3 = [("시민, 도민, 주민", "국민", "a citizen; the people"), ("안전, 자동차, 추락", "사고", "an accident"), ("성폭행, 살인, 유괴", "강력범죄", "a violent crime"), ("경찰서, 소방서, 세무서", "관공서", "a government office"), ("허위광고, 무단횡단, 금연장소에서의 흡연", "경범죄", "a minor offense")]
_L1X = [("범인", "a criminal"), ("범죄자", "an offender"), ("침입", "intrusion; break-in"), ("폭락", "a plunge; a crash"), ("급락", "a sharp fall"), ("평화", "peace"), ("강력범", "a violent criminal"), ("경범", "a minor offense"), ("강도", "a robber; a robbery"), ("폭행", "assault"), ("목격자", "an eyewitness"), ("소매치기", "a pickpocket"), ("도둑", "a thief"), ("국민", "the people; a citizen"), ("시민", "a citizen"), ("주민", "a resident"), ("관공서", "a government office"), ("소방서", "a fire station"), ("유괴", "kidnapping"), ("살인", "murder"), ("성폭행", "sexual assault")]
L1 = lesson(
    "U15 L3 · Review: crime words and Sino-Korean 力 民 犯 事 署",
    "범죄 · 단어 복습 · 한자어 복습 · 범행을 저지르다 · 위조지폐 · 수법 · 力 民 犯 事 署",
    requires=[],
    cards=[
        card("단어 복습 1: verb pairs (my answers)", "The book asks you to connect the matching words and write their meaning in English (the book’s example is 나쁜 수법을 사용하다: to con someone, “to use an evil method”). The book’s left column is 범행을, 딱지를, 몸싸움을, 위조지폐를, 나쁜 수법을, 마약을, 박 교수를; the right column is 떼이다, 저지르다, 찍어내다, 사용하다, 납치하다, 밀수하다, 벌이다. My pairs:", tables=[ktable(_P1)]),
        card("단어 복습 2: words with a similar meaning (my answers)", "The book asks you to connect each word on the left with the word of similar meaning on the right:", tables=[table(["Word", "Similar word (my answer)"], [[a, b] for a, b in _P2], say=[0, 1]), ktable(_P2E)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ3], say=[2]), ktable(_HJW3)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word whose meaning is most opposite to the word on the left (A. 민사: 시민, 사건, 민간인, 형사; B. 폭력: 강도, 폭행, 평화, 체포; C. 경범: 범인, 범죄, 강력범, 목격자).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [[a, b, c] for a, b, c in _OPP3], say=[0, 1])]),
        card("한자어 복습 2: the similar word (my answers)", "Circle the word whose meaning is most similar to the word on the left (A. 범인: 도둑, 강도, 범죄자, 소매치기; B. 침범: 침입, 침몰, 침체, 침수; C. 폭락: 폭행, 폭력, 급락, 폭발).", tables=[table(["Word", "Similar word (my answer)", "Meaning"], [[a, b, c] for a, b, c in _SIM3], say=[0, 1])]),
        card("한자어 복습 3: the related word (my answers)", "Read the three words and choose from the box the related word (the box: 사고, 국민, 강력범죄, 경범죄, 관공서).", tables=[table(["The three words", "The related word", "Meaning"], [[a, b, c] for a, b, c in _REL3], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L1X)]),
    ],
    exercises=uniq(
        _tr(_P1, k=3) + _tr(_P2E, k=3) + _tr(_HJW3, k=3) + _tr(_L1X, k=3)
        + [M("Which verb goes with 범행을?", "저지르다", ["떼이다", "벌이다", "납치하다"], "범행을 저지르다."), M("Which verb goes with 딱지를?", "떼이다", ["저지르다", "찍어내다", "밀수하다"], "딱지를 떼이다."), M("Which verb goes with 몸싸움을?", "벌이다", ["떼이다", "사용하다", "납치하다"], "몸싸움을 벌이다."), M("Which verb goes with 위조지폐를?", "찍어내다", ["벌이다", "밀수하다", "저지르다"], "위조지폐를 찍어내다."), M("Which verb goes with 마약을?", "밀수하다", ["찍어내다", "납치하다", "사용하다"], "마약을 밀수하다."), M("Which verb goes with 박 교수를?", "납치하다", ["밀수하다", "떼이다", "벌이다"], "박 교수를 납치하다."), M("What does the syllable 力 (력) mean?", "power; strength", ["people", "commit", "office"], "폭력."), M("What does the syllable 民 (민) mean?", "people; folks", ["power", "commit", "work"], "수재민."), M("What does the syllable 犯 (범) mean?", "commit; violate", ["people", "power", "office"], "범죄."), M("What does the syllable 事 (사) mean?", "work; service", ["commit", "people", "power"], "사건."), M("What does the syllable 署 (서) mean?", "public office", ["work", "people", "commit"], "경찰서."), M("Which word is the opposite of 폭력?", "평화", ["강도", "폭행", "체포"], "violence ↔ peace."), M("Which word is similar to 침범?", "침입", ["침몰", "침체", "침수"], "intrusion."), M("Which word is similar to 폭락?", "급락", ["폭행", "폭력", "폭발"], "A sharp fall."), M("Which word covers 허위광고, 무단횡단, 금연장소에서의 흡연?", "경범죄", ["강력범죄", "사고", "국민"], "Minor offenses."), M("Which word covers 성폭행, 살인, 유괴?", "강력범죄", ["경범죄", "사고", "관공서"], "Violent crimes."),
           F("경찰은 범행을 ___ 사람을 찾고 있다. (committed)", "저지른", ["떼인", "벌인"], "저지르다."), F("주차를 잘못해서 딱지를 ___. (got a ticket)", "떼였다", ["저질렀다", "벌였다"], "떼이다."), F("두 사람은 ___싸움을 벌였다. (body)", "몸", ["입", "손"], "몸싸움."), F("그는 마약을 ___하다가 잡혔다. (smuggle)", "밀수", ["납치", "수집"], "밀수."), F("살인과 유괴는 ___범죄입니다. (violent)", "강력", ["경범", "민사"], "강력범죄."),
           read_q("범행을 저지른 용의자가 체포되었습니다"), read_q("위조지폐를 찍어낸 범인이 잡혔습니다"), read_q("마약을 밀수한 사람이 발각되었습니다"), read_q("경찰서에 가서 신고했습니다"), read_q("형사가 사건을 조사하고 있습니다")]
    ),
)

# ================================================================== L2 Part 1 texts
_DUI = [["Australia", "The names of those caught are published in the newspaper"], ["Japan", "Fines are also imposed on those who served the liquor and on those who recommended (the book’s “권한” appears to be 권유한) the drinking"], ["Finland", "A month’s pay is confiscated"], ["El Salvador", "Execution by firing squad"]]
_CONV = [
    ("칠 일 대전경찰에 따르면 이날 오전 한 시 사십오 분께 대전 중구 용두동의 한 편의점에 이인조 강도가 들어 여종업원을 흉기로 위협하고서 현금 삼십육만 원을 빼앗아 달아났다.", "According to the Daejeon police on the 7th, at about 1:45 that morning two robbers entered a convenience store in Yongdu-dong, Jung-gu, Daejeon, threatened a female employee with a weapon, took 360,000 won in cash and ran away."),
    ("이 종업원은 경찰에서 차례차례 들어온 남자들이 갑자기 흉기를 꺼내 들어 위협하고 돈을 빼앗아 달아났다고 말했다.", "This employee told the police that the men who came in one after another suddenly took out a weapon, threatened her, took the money and ran away."),
    ("경찰은 편의점에 설치된 폐쇄회로 씨씨티브이를 분석해 이십 대 초반으로 보이는 용의자 두 명을 공개 수배했다.", "The police analyzed the closed-circuit television (CCTV) installed in the convenience store and put out a public wanted notice for two suspects who looked to be in their early twenties."),
    ("용의자 에이는 키 백칠십삼 센티미터, 쥐색 목도리, 검정 점퍼, 청바지, 검정 가방을 소지하고 있었으며 또 다른 용의자 비는 갈색 후드 점퍼에 흰색 농구화를 착용했다.", "Suspect A was 173 cm tall and had a gray scarf, a black jumper, jeans and a black bag, and another suspect, B, wore a brown hooded jumper and white basketball shoes."),
]
_SUS = [["Suspect A", "About 173 cm tall; early twenties; gray scarf, black jumper, jeans, black bag"], ["Suspect B", "Early twenties; brown hooded jumper and white basketball shoes"]]
_SPEAK7 = [("가족이나 친구들 중 범죄의 피해를 입은 사람이 있습니까?", "Is there anyone among your family or friends who was a victim of a crime?"), ("반 친구들과 이야기해 보세요.", "Talk with your classmates."), ("여러분 고향에서 가장 흔히 일어나는 범죄는 무엇입니까?", "What is the crime that most commonly occurs in your hometown?")]
L2 = lesson(
    "U15 L3 · Part 1 (도입 학습): drunk-driving penalties abroad and a convenience-store robbery",
    "도입 학습 · 음주운전 처벌 · 편의점 강도 · 용의자 · 공개 수배 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): drunk-driving punishments abroad",
             "The book shows a chart (Kyunghyang), “외국의 음주운전 처벌규정” (Punishment rules for drunk driving abroad), with four countries and their punishments, and asks you to fill in a table in English (country and punishment). The chart’s texts and my table:",
             tables=[table(["Country", "Punishment (my English)"], [list(r) for r in _DUI])]),
        card("학습활동 4 (Reading): a newspaper article on a robbery",
             "The following is a newspaper article about a crime (Yonhapnews). The book asks you to summarize the crime in English and describe the two suspects. The text is the book’s with the numbers and letters spelled out (7일 is 칠 일, 1시 45분께 is 한 시 사십오 분께, 2인조 is 이인조, 36만 원 is 삼십육만 원, 20대 초반 is 이십 대 초반, 2명 is 두 명, 173 cm is 백칠십삼 센티미터, CCTV is 씨씨티브이, A and B are 에이 and 비); the quotation marks are removed. The English is mine.",
             examples=passage(_CONV)),
        card("The questions answered (mine)", "1. Summary: at about 1:45 in the morning of the 7th, two robbers entered a convenience store in Yongdu-dong, Jung-gu, Daejeon, threatened the female employee with a weapon, took 360,000 won in cash and fled. The police analyzed the store’s CCTV and put out a public wanted notice for two suspects who looked to be in their early twenties.\n\n2. The two suspects:", tables=[table(["Suspect", "Description"], [list(r) for r in _SUS])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK7)),
        card("Activities left out", "학습활동 2 (a chart of the crimes that occurred in 2005 in Seoul, Busan, Daejeon and Gwangju: the most frequent crime in each metropolitan city; the figures are in a graph that is not in the text) and 학습활동 3 (four news clips from YTN, matching each to a social problem from the box: corruption, gang violence, theft, robbery, drug sales and use; one does not match) are chart and audio activities."),
    ],
    exercises=uniq(
        _tr(_CONV, k=3)
        + [M("What did Australia do to those caught drunk driving?", "Published their names in the newspaper", ["Fined their friends only", "Confiscated their pay", "Executed them"], "신문에 공개."), M("What did Finland do?", "Confiscated a month’s pay", ["Published names", "Used firing squads", "Fined the bartender"], "한 달치 월급 몰수."), M("What did El Salvador do?", "Execution by firing squad", ["A month’s pay", "A newspaper notice", "A fine"], "총살형."), M("What kind of place was robbed?", "A convenience store", ["A bank", "A jewelry store", "A school"], "편의점."), M("How many robbers were there?", "Two", ["One", "Three", "Five"], "이인조."), M("How much cash was taken?", "360,000 won", ["36,000 won", "3,600 won", "3,600,000 won"], "삼십육만 원."), M("What did the robbers use to threaten the employee?", "A weapon", ["A phone", "A rope", "A car"], "흉기."), M("What did the police analyze?", "The CCTV in the store", ["Fingerprints", "A diary", "Phone calls"], "폐쇄회로 티브이."), M("About how old did the suspects look?", "Early twenties", ["Late forties", "Teenagers", "Over sixty"], "이십 대 초반."), M("What did Suspect A wear?", "A gray scarf, black jumper, jeans and a black bag", ["A brown hooded jumper", "A suit", "A uniform"], "쥐색 목도리."), M("What did Suspect B wear?", "A brown hooded jumper and white basketball shoes", ["A gray scarf", "Jeans and a black bag", "A black jumper"], "갈색 후드 점퍼."),
           F("이인조 ___가 편의점에 들어왔다. (robbers)", "강도", ["용의자", "종업원"], "강도."), F("여종업원을 ___로 위협했다. (a weapon)", "흉기", ["목도리", "점퍼"], "흉기."), F("경찰은 용의자 두 명을 공개 ___했다. (wanted notice)", "수배", ["규정", "몰수"], "수배."), F("용의자 에이는 쥐색 ___를 하고 있었다. (a scarf)", "목도리", ["농구화", "가방"], "목도리."), F("경찰은 ___ 티브이를 분석했다. (closed-circuit)", "폐쇄회로", ["순환회로", "전기회로"], "폐쇄회로."),
           read_q("편의점에 이인조 강도가 들었습니다"), read_q("강도가 현금 삼십육만 원을 빼앗아 달아났습니다"), read_q("경찰은 용의자 두 명을 공개 수배했습니다"), read_q("용의자 에이는 쥐색 목도리를 하고 있었습니다"), read_q("용의자 비는 흰색 농구화를 착용했습니다")]
    ),
)


# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("규정", "(規定) a rule; a regulation", "이번 조치는 법규정에 어긋나는 것입니다.", "규칙"),
        ("몰수(하다/되다)", "(沒收) confiscation (to confiscate/to be confiscated)", "김 씨는 불법으로 재산을 모은 것이 드러나 법원은 전 재산을 몰수하기로 결정했습니다.", "압수(하다)"),
        ("총살형", "(銃殺刑) execution by firing squad; “killing punishment through a gun”", "", "사형, 교수형"),
    ]),
    ("학습활동 2", [
        ("강간(하다)", "(强姦) rape (to rape)", "이 모 씨는 강간혐의로 경찰의 조사를 받고 있습니다."),
        ("사기(치다)", "(詐欺) a fraud; a scam (to fraud; to scam; to con)", "사기도박을 벌인 일당이 검거되었습니다.", "사기꾼"),
        ("성매매", "(性賣買) prostitution; “sex trade”", "", "매춘, 매춘부"),
        ("횡령(하다)", "(橫領) embezzlement (to embezzle)", "그는 공금을 횡령한 혐의로 검찰의 조사를 받고 있습니다."),
    ]),
    ("학습활동 3", [
        ("대리주차", "(代理駐車) valet parking; “proxy parking”", "저희 식당은 대리주차 서비스를 해 드리고 있습니다."),
        ("대마(초)", "(大麻(草)) hemp; marijuana; hashish", "", "마약"),
        ("징계(하다)", "(懲戒) a disciplinary punishment (to punish for delinquency; to discipline)", "정부는 뇌물을 받은 공무원들을 징계하겠다고 발표했습니다.", "처벌(하다)"),
        ("해임(하다/되다)", "(解任) dismissal (from an official position) (to dismiss/to be dismissed)", "정 시장이 건축업자에게서 뇌물을 받은 혐의로 해임되었다.", "임명(하다)"),
    ]),
    ("학습활동 4", [
        ("목도리", "a scarf; a muffler", ""),
        ("수배(하다/되다)", "(手配) hunting or seeking in order to apprehend (to want/to be wanted)", "수배 중이던 강 씨가 검찰에 검거되었습니다.", "수배자, 공개수배, 지명수배"),
    ]),
]
L3 = lesson(
    "U15 L3 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 규정 · 몰수 · 총살형 · 강간 · 사기 · 성매매 · 횡령 · 대리주차 · 대마 · 징계 · 해임 · 수배",
    requires=[],
    cards=vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=8, nread=6)),
)

# ================================================================== L4 Part 2 texts
_MIL = [
    ("팔 일 국회 법제사법위원회 소속 한나라당 박민식 의원이 국방부로부터 제출받은 자료에 따르면 이천오 년부터 올해 유 월까지 군인이 범죄로 입건된 건수는 육군 " + _kn(25528) + " 건, 해군 " + _kn(4178) + " 건, 공군 " + _kn(1885) + " 건 등 모두 " + _kn(31591) + " 건이었다.", "According to materials submitted by the Ministry of National Defense to Rep. Park Min-sik of the Grand National Party, a member of the National Assembly’s Legislation and Judiciary Committee, on the 8th, the number of cases in which soldiers were booked for crimes from 2005 to June this year was 25,528 in the Army, 4,178 in the Navy and 1,885 in the Air Force, a total of 31,591."),
    ("육군은 탈영으로 인한 입건이 " + _kn(5136) + " 건으로 가장 많았다.", "In the Army, bookings for desertion were the most numerous at 5,136."),
    ("해군은 폭력으로 인한 범죄가 " + _kn(1481) + " 건으로 가장 많았다.", "In the Navy, crimes caused by violence were the most numerous at 1,481."),
    ("공군은 음주운전 등 도로교통법 위반이 " + _kn(339) + " 건으로 가장 많았다.", "In the Air Force, violations of the Road Traffic Act such as drunk driving were the most numerous at 339."),
    ("공군의 경우 삼 군 중 상대적으로 근무환경이 좋고 외출 외박이 많아 음주운전 등 도로교통법 위반이 많은 것으로 분석됐다.", "In the case of the Air Force, it was analyzed that violations of the Road Traffic Act such as drunk driving are many because, of the three services, the working environment is relatively good and there are many outings and nights away."),
]
_MILT = [["Army", "Desertion (5,136 bookings)"], ["Navy", "Violence (1,481 cases)"], ["Air Force", "Violations of the Road Traffic Act such as drunk driving (339 cases)"]]
_SPEAK8 = [("미국에서 일어난 유명한 범죄사건에 대해서 말해 봅시다.", "Let us talk about a famous (infamous) crime case that happened in the United States."), ("범인과 피해자는 누구인지 사건의 내용은 무엇인지 말해 봅시다.", "Let us say who the criminal and the victim are and what the case was.")]
L4 = lesson(
    "U15 L3 · Part 2 (본 학습): crimes committed by soldiers",
    "본 학습 · 군인 범죄 · 입건 · 탈영 · 폭력 · 음주운전 · 도로교통법 위반",
    requires=[],
    cards=[
        card("학습활동 2 (Reading): crimes by military personnel",
             "The following is a newspaper article about crimes committed by soldiers (Kyunghyang, text and image). The book asks you to write the most common type of crime in each military branch and to explain why crime in the Air Force is the most common. The text is the book’s with the numbers spelled out in the Sino-Korean style (8일 is 팔 일, 2005년 is 이천오 년, 6월 is 유 월, 25528건 is 이만 오천오백이십팔 건, and so on, 3군 is 삼 군); the English is mine. The book’s caption says the figures are from materials Representative Park Min-sik received from the Ministry of National Defense.",
             examples=passage(_MIL)),
        card("The questions answered (mine)", "1. The most common type of crime in each branch:", tables=[table(["Branch", "The most common type of crime"], [list(r) for r in _MILT])]),
        card("The second question (mine)", "2. Why is the crime committed in the Air Force the most common? Because, of the three services, the Air Force’s working environment is relatively good and it has many outings and nights away, so there are many violations of the Road Traffic Act such as drunk driving."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK8)),
        card("Activities left out", "학습활동 1 (a YTN current-affairs clip: what teenagers think are the causes of crimes by teenagers), 학습활동 3 (a YTN crime news clip: guessing the topic from the box 로프, 50대 남자, 빈집털이, 아파트, 구조대, 꼬이다 and summarizing what you heard) and 학습활동 4 (a YTN news clip about violent crimes: a table of two crimes and three points that support the idea that the same suspect may have committed both) are audio activities."),
    ],
    exercises=uniq(
        _tr(_MIL, k=3)
        + [M("Which branch has the most bookings, 25,528?", "The Army", ["The Navy", "The Air Force", "The Marines"], "육군."), M("What was the total number of cases?", "31,591", ["25,528", "4,178", "1,885"], "삼만 천오백구십일 건."), M("What is the most common crime in the Army?", "Desertion", ["Violence", "Drunk driving", "Theft"], "탈영."), M("What is the most common crime in the Navy?", "Violence", ["Desertion", "Drunk driving", "Fraud"], "폭력."), M("What is the most common crime in the Air Force?", "Violations of the Road Traffic Act such as drunk driving", ["Desertion", "Violence", "Theft"], "도로교통법 위반."), M("Why does the Air Force have many such violations?", "Better working environment and more outings and nights away", ["Pilots are young", "Roads are bad", "The base is far"], "외출 외박이 많아."), M("Who provided the materials to Representative Park?", "The Ministry of National Defense", ["The police", "The Air Force", "The media"], "국방부."), M("What period do the figures cover?", "From 2005 to June this year", ["Only last year", "Ten years", "One month"], "이천오 년부터 올해 유 월까지."),
           F("군인이 범죄로 ___된 건수는 모두 삼만 천오백구십일 건이었다. (booked)", "입건", ["수배", "몰수"], "입건."), F("육군은 ___으로 인한 입건이 가장 많았다. (desertion)", "탈영", ["폭력", "횡령"], "탈영."), F("해군은 ___으로 인한 범죄가 가장 많았다. (violence)", "폭력", ["탈영", "음주운전"], "폭력."), F("공군은 도로교통법 ___이 가장 많았다. (violations)", "위반", ["몰수", "수배"], "위반."), F("공군은 ___ 근무환경이 좋다. (relatively)", "상대적으로", ["절대적으로", "동일하게"], "상대적."),
           read_q("군인이 범죄로 입건된 건수는 모두 삼만 천오백구십일 건이었습니다"), read_q("육군은 탈영으로 인한 입건이 가장 많았습니다"), read_q("해군은 폭력으로 인한 범죄가 가장 많았습니다"), read_q("공군은 음주운전 등 도로교통법 위반이 가장 많았습니다"), read_q("공군은 외출과 외박이 많습니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 2", [
        ("대중매체", "(大衆媒體) mass media", "신문, 방송, 인터넷은 현대인들이 가장 많이 접하는 대중매체입니다."),
        ("만화책", "(漫畵冊) a comic book; a manga book", "", "만화영화, 만화가게"),
        ("상대적", "(相對的) relative", "대구시의 물가는 다른 도시들에 비해 상대적으로 높은 편입니다.", "절대적"),
        ("외박(하다)", "(外泊) spending the night away from home (to sleep away from home)", "외박하지 말고 꼭 집에 들어와서 자라.", "밖에서 자다 | 외출, 휴가"),
    ]),
    ("학습활동 3", [
        ("꼬이다", "to be twisted; to be tangled", "전깃줄이 꼬였어요. 풀어 주세요."),
        ("밧줄", "a rope", ""),
        ("범행", "(犯行) a crime; a criminal act", "경찰은 범행을 저지른 범인을 찾고 있습니다.", "범죄, 범인"),
        ("빈집털이범", "(犯) a thief; “empty house ransacking criminal”", "휴가 동안 절도를 저지른 빈집털이범들이 경찰에 붙잡혔습니다.", "도둑"),
        ("옥상", "(屋上) a rooftop; “house top”", "옥상에서 화초를 기르는 사람들이 많습니다."),
    ]),
    ("학습활동 4", [
        ("괴한", "(怪漢) an unidentified assailant; a suspicious person", "김 사장이 어젯밤 두 명의 괴한들에게 납치되었다.", "범인"),
        ("노리다", "to have an eye on; to be after; to aim at", "젊은 여성을 노리는 범죄가 많이 발생하고 있습니다."),
        ("동일", "(同一) same; “same one”", "동일한 수법으로 살인을 저지른 것으로 미루어 동일범일 가능성이 높습니다.", "동일범, 동일인"),
        ("수법", "(手法) (derogatory term) a trick; a method", "인터넷 사기 수법이 날로 다양해지고 있습니다.", "방법"),
        ("찌르다", "to stab", ""),
        ("체격", "(體格) build; physique", "그는 체격 조건이 좋아서 운동선수로 성공할 것 같아요."),
    ]),
]
L5 = lesson(
    "U15 L3 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 대중매체 · 상대적 · 외박 · 꼬이다 · 밧줄 · 범행 · 빈집털이범 · 옥상 · 괴한 · 노리다 · 동일 · 수법 · 체격",
    requires=[],
    cards=vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=8, nread=6)),
)


# ================================================================== L6 Part 3 texts
_LAW = [
    ("법무부는 수사 과정에서 흉악범과 성폭력범에 대한 촬영을 허가하고, 얼굴 등 신상정보를 공개하는 인권보호를 위한 수사공보준칙 (수사공보준칙) 개정안을 시행한다고 이십삼 일 밝혔다.", "The Ministry of Justice announced on the 23rd that it will enforce a revision of the Rules on Public Information about Investigations for the Protection of Human Rights (the investigation public-information rules), which permits photographing brutal criminals and sex offenders during the investigation process and disclosing personal information such as their faces."),
    ("개정안에 따르면 특정강력범죄의 처벌에 관한 특례법과 성폭력범죄의 처벌 등에 관한 특례법에서 신상정보 공개를 허용하는 흉악범과 성폭력범은 기관장의 사전 승인을 받아 언론이 촬영 녹화 중계방송할 수 있고, 얼굴 실명 나이 등을 외부에 공개할 수 있다.", "According to the revision, brutal criminals and sex offenders whose personal information disclosure is permitted under the Special Act on the Punishment of Specific Violent Crimes and the Special Act on the Punishment of Sexual Violence Crimes can, with the prior approval of the head of the agency, be filmed, recorded and broadcast live by the media, and their faces, real names, ages and so on can be disclosed to the outside."),
    ("검찰은 공개 요건과 관련, 잔인하고 중대한 피해가 발생했고, 피의자가 죄를 범했다고 믿을만한 충분한 증거가 있으며, 알 권리 보장 및 범죄예방 등 공익을 위해 필요하고, 피의자가 청소년이 아닌 경우 등이라고 밝혔다.", "Regarding the requirements for disclosure, the prosecution said they are cases in which cruel and serious harm has occurred, there is sufficient evidence to believe that the suspect committed the crime, it is necessary for the public interest such as guaranteeing the right to know and preventing crime, and the suspect is not a minor."),
]
_CASE = [
    ("법원 확정판결 전 용의자 단계에 있는 범죄 피의자의 얼굴 공개를 놓고, 논란이 일고 있다.", "Controversy is arising over disclosing the faces of criminal suspects who are at the suspect stage before a final court judgment."),
    ("성폭행이나 살인 용의자에 대해선 국민 알 권리와 범죄예방 차원에서 공개해야 한다는 주장과 인권보호 및 무죄추정의 원칙에 따라 공개하면 안 된다는 주장이 맞서고 있는 것이다.", "For suspects of sexual assault or murder, the argument that they should be disclosed from the standpoint of the people’s right to know and crime prevention is facing off against the argument that they must not be disclosed according to the protection of human rights and the principle of presumption of innocence."),
    ("논란은 일부 언론에서 경기 서남부 부녀자 연쇄살인범 강호순 씨 (서른여덟 살)의 얼굴을 공개하자, 더욱 가열되고 있다.", "The controversy has heated up further as some media disclosed the face of Mr. Kang Ho-sun (38), the serial killer of women in the southwest of Gyeonggi Province."),
    ("네티즌 한 모 씨는 강 씨 얼굴은 공개해야 한다. 범죄자 인권을 위해 일반 시민들의 인권을 희생할 순 없다고 밝혔다.", "A netizen, Mr. Han, said, “Mr. Kang’s face must be disclosed. We cannot sacrifice the human rights of ordinary citizens for the human rights of a criminal.”"),
    ("김 모 씨도 연쇄살인범 얼굴 공개는 당연한 것이다. 사람을 동물 다루듯 잔혹하게 살해한 자에게 인권이란 단어는 사치라고 주장했다.", "Mr. Kim also insisted, “Disclosing the face of a serial killer is natural. For a person who brutally killed people as if treating animals, the word human rights is a luxury.”"),
    ("반면 홍 모 씨는 강 씨 얼굴 공개가 그렇게 중요하냐? 강 씨의 열네 살 열여섯 살 먹은 자식들을 생각해 봤냐? 그 아이들의 장래는 누가 책임질거냐?면서 반대했다.", "On the other hand, Mr. Hong opposed it, saying, “Is disclosing Mr. Kang’s face that important? Have you thought about Mr. Kang’s children, who are 14 and 16? Who will be responsible for those children’s future?”"),
    ("법조계도 의견이 나뉜다.", "Legal circles are also divided in opinion."),
    ("박주민 변호사(민주사회를 위한 변호사모임)는 이천칠 년 간첩 혐의로 체포된 강순정 할아버지는 당시 언론에서 신상을 다 공개했는데 무죄가 됐다. 이런 경우 어떻게 보상하냐면서 비록 흉악범일지라도 인권을 존중해야 하고, 얼굴도 공개해선 안 된다고 말했다.", "Lawyer Park Ju-min (of Lawyers for a Democratic Society) said, “Grandfather Kang Sun-jeong, who was arrested on spy charges in 2007, was found not guilty after the media disclosed all of his personal information at the time. How do you compensate in such a case?” and said, “Even if he is a brutal criminal, human rights must be respected and his face must not be disclosed.”"),
    ("반면 하창우 변호사(서울 변호사 협회장)는 범인 공개수배 때 얼굴을 공개한다면서 하물며 이미 잡혀 반인륜적 범죄를 자백한 피의자 얼굴을 공개하지 않는 것은 모순이라고 말했다.", "On the other hand, lawyer Ha Chang-u (president of the Seoul Bar Association) said, “We disclose faces when a criminal is publicly wanted,” and “It is a contradiction not to disclose the face of a suspect who has already been caught and has confessed to an antihumanistic crime.”"),
]
_PROCON = [["Pro (disclose)", "The people’s right to know and crime prevention; ordinary citizens’ human rights cannot be sacrificed for a criminal’s; a person who killed brutally does not deserve the word human rights; faces are disclosed anyway when a criminal is publicly wanted, so not disclosing the face of a caught suspect who confessed is a contradiction"], ["Con (do not disclose)", "Protection of human rights and the principle of presumption of innocence; the suspect’s children and their future; a suspect whose personal information was disclosed may turn out innocent, and then there is no way to compensate"]]
_SPEAK9 = [("범죄자 신상공개에 대해서 찬성합니까? 반대합니까?", "Do you agree with disclosing criminals’ personal information? Do you disagree?"), ("그 이유는 무엇입니까?", "What is your reason?"), ("반 친구들과 의견을 나누어 보세요.", "Share your opinion with your classmates.")]
L6 = lesson(
    "U15 L3 · Part 3 (심화 학습): disclosing the identities of criminals",
    "심화 학습 · 무죄추정의 원칙 · 신상 공개 · 흉악범 · 피의자 인권 · 찬반 논란",
    requires=[],
    cards=[
        card("알아봅시다: 무죄추정의 원칙", "무죄추정의 원칙 refers to the principle of “presumption of innocence.” In other words, everyone charged with a penal offense is, by right, presumed innocent until proven guilty. This is in accordance with law that guarantees the accused high-quality defense in a public trial. This principle is stated in the Universal Declaration of Human Rights and in the Korean Constitution."),
        card("학습활동 1 (Reading): an article on the criminal law amendment",
             "The following is an article about an amendment of criminal law (Kyunghyang). The book asks you to choose which of four statements about the new law is true and to write the conditions that must be met before the amendment may be applied. The text is the book’s with 23일 spelled 이십삼 일; the quotation marks are removed. The English is mine.",
             examples=passage(_LAW)),
        card("The questions answered (mine)", "1. The true statement is D. Prior to revealing the criminal’s identity, you must get approval from the authority (the head of the agency’s prior approval). A is wrong because brutal criminals as well as sex offenders are covered; B is wrong because the real name may also be disclosed; C is wrong because the article says nothing about waiting for a conviction.\n\n2. The conditions (third paragraph): cruel and serious harm has occurred; there is sufficient evidence to believe the suspect committed the crime; disclosure is necessary for the public interest such as the right to know and crime prevention; and the suspect is not a minor."),
        card("학습활동 2 (Reading): an article on the human rights of criminals",
             "The following is an article about the human rights of criminals (Kyunghyang). The book asks you to state the main issue, summarize the pro and con arguments and say what happened to 강순정 and why 박주민 quoted his case. The text is the book’s with the age and numbers spelled out (38 is 서른여덟 살, 14살 16살 is 열네 살 열여섯 살, 2007년 is 이천칠 년); the quotation marks are removed. The English is mine.",
             examples=passage(_CASE)),
        card("The questions answered (mine)", "1. The main issue: whether to disclose the faces of criminal suspects before a final court judgment (the people’s right to know and crime prevention versus human rights and the presumption of innocence).\n\n2. The two sides:", tables=[table(["Side", "Arguments"], [list(r) for r in _PROCON])]),
        card("The third question (mine)", "3. What happened to 강순정, and why did 박주민 quote his case? Mr. Kang Sun-jeong, an old man, was arrested on spy charges in 2007 and the media disclosed all of his personal information at the time, but he was found not guilty. Lawyer Park quoted the case to show that disclosure before judgment can wrongly harm a person who is later cleared, and there is no way to compensate."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK9)),
        card("Activities left out", "학습활동 3 (a YTN news clip about violent crime: the best title, the violent crimes the anchor mentions at the beginning, the relationship between a felony and the number of repeated offenses, and possible reasons for increasing repeat crimes) is an audio and video activity."),
    ],
    exercises=uniq(
        _tr(_LAW + _CASE, k=3)
        + [M("What does 무죄추정의 원칙 mean?", "The presumption of innocence", ["The right to silence", "A right to travel", "A ban on crime"], "The book’s note."), M("Who announced the revision?", "The Ministry of Justice", ["The police", "A newspaper", "The president"], "법무부."), M("Which criminals does the revision cover?", "Brutal criminals and sex offenders", ["Only pickpockets", "Only minors", "Only drivers"], "흉악범과 성폭력범."), M("What do the media need before filming and broadcasting a suspect?", "Prior approval of the head of the agency", ["A court order", "A signature from the suspect", "Nothing"], "기관장의 사전 승인."), M("What can be disclosed under the revision?", "Face, real name, age and so on", ["Only the face", "Only the name", "Nothing"], "얼굴 실명 나이."), M("Which condition must be met?", "The suspect is not a minor", ["The suspect agrees", "The case is old", "The victim agrees"], "청소년이 아닌 경우."), M("What is the controversy about?", "Disclosing the faces of criminal suspects before a final judgment", ["Raising taxes", "Building prisons", "Banning cameras"], "논란."), M("Whose face did some media disclose?", "Kang Ho-sun, a serial killer", ["Kang Sun-jeong", "Mr. Han", "Mr. Kim"], "강호순."), M("What happened to Kang Sun-jeong?", "He was arrested on spy charges, his information was disclosed, then he was found not guilty", ["He was executed", "He was never arrested", "He was convicted"], "무죄가 됐다."), M("Why did lawyer Ha say not disclosing a confessed suspect’s face is a contradiction?", "Faces are disclosed when criminals are publicly wanted", ["It is against the law", "It is expensive", "It is rude"], "공개수배."),
           F("피의자의 ___을 공개하는 것에 대한 논란이다. (face)", "얼굴", ["가명", "나이"], "얼굴."), F("국민의 알 ___를 보장해야 한다. (right)", "권리", ["모순", "논란"], "권리."), F("범죄자 ___을 존중해야 한다. (human rights)", "인권", ["공익", "신상"], "인권."), F("공개하지 않는 것은 ___이다. (a contradiction)", "모순", ["권리", "요건"], "모순."), F("흉악범의 ___정보를 공개한다. (personal)", "신상", ["실명", "공익"], "신상."),
           read_q("피의자의 얼굴 공개를 놓고 논란이 일고 있습니다"), read_q("무죄추정의 원칙에 따라 공개하면 안 됩니다"), read_q("국민의 알 권리와 범죄예방을 위해 공개해야 합니다"), read_q("흉악범의 신상정보를 공개합니다"), read_q("비록 흉악범일지라도 인권을 존중해야 합니다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("공익", "(公益) public interest", "공익을 위해서 최선을 다 해 주시기 바랍니다.", "공익광고"),
        ("법조계", "(法曹界) legal circles", "아직까지 법조계에는 남성의 수가 여성의 수보다 훨씬 더 많습니다."),
        ("신상(정보)", "(身上(情報)) personal information", "인터넷에 신상정보를 공개한 사람이 검찰에 검거되었습니다."),
        ("실명", "(實名) a real name", "실명을 사용하지 않으면 은행 계좌를 만들 수 없습니다.", "가명 | 익명, 성명, 필명"),
        ("요건", "(要件) a necessary condition; a required condition; a requisite", "이 회사에 입사할 수 있는 자격 요건이 무엇입니까?", "조건"),
        ("중대하다", "(重大) to be important; “to be heavy and big”", "제가 중대한 실수를 저질렀어요. 죄송합니다."),
        ("특례법", "(特例法) an exemption law; a law covering special cases", "교통사고에 대한 특례법을 제정했습니다."),
        ("피의자", "(被疑者) a suspect", "살인 사건의 피의자는 무죄판결을 받았습니다.", "피해자 | 범인, 혐의자, 용의자"),
        ("흉악범", "(凶惡犯) a brutal criminal", "정부는 흉악범의 얼굴을 공개하겠다고 발표했습니다.", "중범죄자, 강력범"),
        ("공개(하다/되다)", "(公開) making public (to make public/to be made public)", "기술의 발달로 개인정보가 너무 쉽게 공개됩니다."),
        ("권리", "(權利) a right", "개인의 권리는 헌법에 보장되어 있습니다."),
        ("맞서다", "to oppose; to stand against", "시위대는 경찰에 맞서 싸웠습니다."),
    ]),
    ("학습활동 2", [
        ("모순", "(矛盾) contradiction", "두 사람은 같은 사건을 놓고 모순되는 이야기를 하고 있습니다."),
        ("반인륜적", "(反人倫的) antihumanistic; against humanity", "어머니를 살해한 반인륜적 범죄자가 오늘 붙잡혔다."),
        ("연쇄", "(連鎖) chain; serial", "연쇄살인사건의 범인이 누구입니까?", "연쇄충돌, 연쇄살인"),
        ("자백(하다)", "(自白) confession (of a crime) (to confess; to admit)", "범인의 범행을 모두 자백했습니다.", "고백하다"),
        ("잔인하다", "(殘忍) to be cruel", "그 영화는 너무 잔인해서 보고 싶지 않아요.", "잔혹하다"),
        ("잔혹하다", "(殘酷) to be cruel; to be brutal; to be atrocious", "이번 살인 사건은 그 수법이 너무 잔혹합니다.", "잔인하다"),
        ("주장(하다)", "(主張) insistence; persistence; assertion (to insist; to persist; to assert)", "이 모 군은 자신이 범죄와 관련이 없다고 주장했다."),
        ("희생(하다/되다)", "(犧牲) sacrifice (to sacrifice/to be sacrificed)", "그는 자신을 희생하여 가족을 구했습니다."),
    ]),
    ("학습활동 3", [
        ("교정교화", "(矯正敎化) correction and reformation", "교도소는 교정교화가 목적입니다.", "교도소, 출소자"),
        ("급선무", "(急先務) an urgent priority; urgent business", "남북관계는 비핵화가 급선무입니다."),
        ("냉대(하다)", "(冷待) unkind or inhospitable treatment; “cold treatment” (to treat someone coldly)", "신데렐라는 계모의 냉대를 받으며 자랐다."),
        ("논란", "(論難) controversy; dispute", "새로 개정된 법안에 대해 논란이 많습니다."),
        ("불황", "(不況) recession; economic slump", "경기 불황에 실직하는 사람들이 많습니다.", "불경기 | 호황"),
        ("장기화(하다/되다)", "(長期化) prolonging; extending over a long period of time (to prolong; to extend over a long period of time/to be prolonged; to be extended)", "실직이 장기화되면서 범죄를 저지르는 사람들이 늘고 있습니다."),
        ("재범", "(再犯) repeated conviction; a repeat criminal", "흉악범들은 재범인 경우가 많습니다.", "초범"),
        ("출소자", "(出所者) a released prisoner; “person who exits (correctional) facility”", "출소자들이 범죄를 다시 저지르는 경우가 많습니다.", "재소자 | 교도소"),
        ("편견", "(偏見) a prejudice; a bias", "장애인에 대한 사회적 편견이 아직도 많습니다."),
        ("혼란", "(混亂) confusion; disorder", "경제 문제가 심각해지면서 사회적 혼란이 가중되고 있습니다.", "안정"),
    ]),
]
L7 = lesson(
    "U15 L3 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 공익 · 법조계 · 신상정보 · 피의자 · 흉악범 · 모순 · 연쇄 · 자백 · 잔혹하다 · 재범 · 출소자 · 편견",
    requires=[],
    cards=vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=14, nread=10)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 3: Crimes (범죄)", [L1, L2, L3, L4, L5, L6, L7])

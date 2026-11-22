"""Unit 42: KBC Semester 2, Unit 9, Chapter 35 - Job Hunting (직장 구하기).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 9, Student's Edition (Validation Edition).
Audio, video, pictures, charts, SMART Board activities, role-plays, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 35 (meanings and examples are the book's)
_CV_A = [
    ("관련", "(關聯) relation; connection; to be related; to be connected (~하다/되다)", "저는 컴퓨터 관련 자격증이 있어요."),
    ("기업(체)", "(企業(體)) a business enterprise; a corporation", "삼성은 한국의 유명한 대기업입니다."),
    ("내용", "(內容) contents; substance", "책 내용이 너무 어려워요."),
    ("박람회", "(博覽會) a fair; an expo", "취업준비를 위해서 어제 취업박람회에 갔다 왔어요."),
    ("상반기", "(上半期) the first half of a given period or year; “the top half period”", "올 상반기에는 신입사원을 모집하지 않습니다."),
    ("소지", "(所持) possession; carrying; to possess; to carry (~하다)", "운전을 할 때에는 꼭 운전면허증을 소지하세요."),
    ("우대", "(優待) preferential treatment; special treatment; to give preferential treatment / to be given preferential treatment (~하다/받다)", "저희 회사에서는 외국어 특기자를 우대합니다."),
    ("이력서", "(履歷書) a resume", "취직을 하려고 여러 곳에 이력서를 냈는데 연락이 없어요."),
    ("~자", "(者) a suffix denoting a person", "자세한 내용은 채용 담당자에게 문의하세요."),
    ("자기소개서", "(自己紹介書) a letter of self-introduction", "취직하려면 먼저 이력서와 자기소개서를 준비하세요."),
    ("작성", "(作成) filling out (a form); to fill out / to be filled out (~하다/되다)", "이력서를 작성해서 제출해 주세요."),
    ("접수", "(接受) receipt; acceptance; to receive; to accept / to be received (~하다/되다)", "삼성 기업의 서류 접수는 벌써 끝났습니다."),
    ("제출", "(提出) submission; to submit; to turn in / to be submitted (~하다/되다)", "숙제를 선생님께 제출하세요."),
    ("지원서", "(志願書) an application; “application writing”", "다음 주까지 회사에 입사지원서를 내셔야 합니다."),
    ("참가", "(參加) participation; to participate (~하다)", "저는 이번 학교 행사에 참가하기로 했어요."),
    ("채용", "(採用) employment; hiring; recruitment; to employ; to hire; to recruit / to be employed (~하다/되다)", "올해에는 신입 사원을 채용할 계획이 없습니다."),
    ("특기", "(特技) one’s special ability; talent; “special skill”", "저희 반에는 음악에 특기가 있는 학생이 많아요."),
    ("하반기", "(下半期) the second half of a given period or year; “the bottom half period”", "올 하반기에는 대기업에서 신입사원을 많이 채용할 계획입니다."),
    ("학력", "(學歷) schooling; educational background; “learning history”", "학력이 높다고 좋은 직장에 취직이 되는 것은 아닙니다."),
]
_CV_B = [
    ("게시판", "(揭示板) a bulletin board", "저는 회사에 출근하면 먼저 게시판을 봅니다."),
    ("경력", "(經歷) (work) experience", "외국인을 가르친 경력이 있습니까?"),
    ("구인", "(求人) job listing; “seeking a person”", "직장을 찾기 위해서 매일 구인 광고를 보고 있어요."),
    ("구직(자)", "(求職(者)) seeking a job (a job seeker; a job hunter)", "김영호 씨는 구직자에게 직장을 소개해 주는 일을 하고 있습니다."),
    ("~군", "(君) a title for a young man", "박민호 군은 컴퓨터공학을 전공합니다."),
    ("대기업", "(大企業) a large enterprise; a conglomerate; “large business”", "대기업에서는 경력사원을 선호합니다."),
    ("면접", "(面接) a face-to-face interview; “face contact”; to have a face-to-face interview (~[을] 보다)", "서류 시험을 통과한 사람만 면접시험을 볼 수 있어요."),
    ("분야", "(分野) a (professional/academic) field/sphere/area", "대학 졸업 후 전공 분야에서 일하는 사람들이 많지 않아요."),
    ("뽑다", "to choose; to select; to employ; “to pick”", "저희 회사에서는 경력사원만 뽑습니다."),
    ("서류 전형", "(書類 銓衡) documents screening", "서류 전형은 통과했지만 면접에서 떨어졌어요."),
    ("쌓다", "to build; to pile up", "인턴으로 일을 하면서 경력을 쌓았어요."),
    ("업데이트", "update", "어제 새 홈페이지로 업데이트 했어요."),
    ("유리하다", "(有利) to be advantageous", "외국어를 잘하면 취직하는 데 유리해요."),
    ("유용하다", "(有用) to be useful", "취업게시판에 유용한 취업정보가 많아요."),
    ("인원", "(人員) the number of persons; personnel; staff", "내일도 일을 하려면 더 많은 인원이 필요해요."),
    ("임금", "(賃金) wage; pay", "임금이 오르지 않아서 생활이 어려워요."),
    ("중소기업", "(中小企業) small and medium enterprises", "최민수 군은 중소기업에 지원했습니다."),
    ("희망", "(希望) aspiration; hope; longing; to aspire; to hope; to long (~하다)", "한국 사람들은 한국이 통일되기를 희망합니다."),
]
_CV_C = [
    ("개발", "(開發) development; to develop / to be developed (~하다/되다)", "저희 회사는 자기 개발을 할 수 있는 기회가 많습니다."),
    ("개별적으로", "(個別的) individually", "면접 결과는 개별적으로 알려드리겠습니다."),
    ("기회", "(機會) an opportunity", "친구가 말할 기회도 주지 않고 화만 냈어요."),
    ("다국적", "(多國籍) multinational", "미국에는 다국적 기업들이 많이 있습니다."),
    ("단점", "(短點) a weak point; shortcoming; “short point”", "저의 단점은 화를 잘 내는 것입니다."),
    ("동기", "(動機) a motive", "제가 한국말을 배우게 된 동기는 한국영화를 보기 위해서였어요."),
    ("면접관", "(面接官) an interviewer", "면접관이 제 전공과 회사 지원 동기 등에 대해 물어봤어요."),
    ("무역학", "(貿易學) (the study of) trade", "저는 대학교 때 무역학을 전공했어요."),
    ("새롭다", "to be new; to be fresh; to be novel", "봄이 와서 방을 새롭게 바꿔 봤어요."),
    ("자신", "(自身) oneself", "먼저 자신의 장점과 단점을 잘 알아야 합니다."),
    ("자신(감)", "(自信(感)) self-confidence; “self-believing feeling”", "제 동생은 모든 일에 자신감이 없어요."),
    ("장점", "(長點) a merit; a strength; a forte; “strong point”", "이 세탁기의 장점은 소리가 많이 나지 않는 것입니다."),
    ("적응", "(適應) adaptation; to adapt oneself to / to be adapted to (~하다/되다)", "새로운 환경에 적응하는 것은 쉽지 않아요."),
    ("철저하다", "(徹底) to be thorough; to be exhaustive", "저희 부대 상관은 항상 철저하고 까다롭습니다."),
    ("해외", "(海外) overseas", "여름이 되면서 해외로 여행가는 사람들이 늘고 있어요."),
    ("호주", "(濠洲) Australia", "호주의 수도는 캔버라입니다."),
]
_CV_LOAN = [("업데이트", "update", "어제 새 홈페이지로 업데이트했어요.")]
_CV_GR = [
    ("-다고", "for a statement used as the object in a sentence", "중국이 미국보다 작다고 생각해요."),
    ("an attributive form + 만큼", "as … as", "갖고 싶은 만큼 다 가지고 가세요."),
    ("보이다 / 들리다", "“to be seen” / “to be heard”", "칠판이 잘 보입니까? 내 목소리가 잘 들립니까?"),
    ("이, 히, 리, 기", "passive infixes", "교실 문이 닫혀서 들어갈 수 없었어요."),
]
_CV_SINO = [("구직", "(求職) seeking a job", "구인, 직업, 구걸, 직장, 추구, 직원"), ("면접", "(面接) a face-to-face interview; “face contact”", "면도, 세면, 체면, 직접, 간접, 접근"), ("하반기", "(下半期) the second half of a given period or year; “the bottom half period”", "지하, 반도체, 기간, 하사, 영하, 반원, 한반도, 연기, 상반기")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_LOAN}
_EXTRA = {"기업(체)": "a business enterprise; a corporation", "구직(자)": "seeking a job; a job seeker", "자신(감)": "self-confidence", "서류 전형": "documents screening",
          "서류": "documents", "규모": "size; scale", "상담": "consultation; counseling", "소지자": "a holder; a possessor", "취업": "getting a job; employment", "유학": "studying abroad", "문의": "an inquiry", "관리": "management", "성적": "grades; results", "전공": "a major", "어학연수": "foreign language study (abroad)", "학점": "a (college) credit; a grade", "자격증": "a certificate; a license", "연봉": "an annual salary", "마감하다": "to close; to finish (a deadline)", "붙다": "to pass (an exam); to stick", "분야/부문": "a field; a section", "구인": "job listing; “seeking a person”",
          "통보하다": "to notify; to inform", "본인": "oneself; the person himself/herself", "진출하다": "to advance into; to enter", "개별": "an individual; separate", "인재": "a talented person", "태도": "an attitude", "남기다": "to leave (behind)", "거절하다": "to refuse; to decline", "남": "another person; others", "자신감": "self-confidence",
          "지하": "underground", "반도체": "a semiconductor", "하사": "a sergeant (the lowest NCO rank in the Korean military)", "영하": "below zero", "반원": "a half circle", "한반도": "the Korean Peninsula", "연기": "a postponement", "지하도": "an underground pass", "남하하다": "to move down south", "천하": "the world; the whole country; “heaven below”", "하수도": "a sewer; “under water way”", "반도": "a peninsula; “half island”", "반값": "half the price", "반달": "a half moon", "반올림": "rounding up (of a number); “half raising”",
          "초보자": "a novice", "학자": "a scholar", "보호자": "a guardian", "구인 광고": "a help-wanted ad; “people-seeking ad”", "구혼": "a marriage proposal; a courtship; “seeking a marriage”", "요구": "a demand; a claim; a request; “important seeking”", "직업": "a job; an occupation", "교직": "the teaching profession", "직장": "a workplace", "직원": "an employee; a member of the staff; “job member”",
          "가면": "a mask; “fake face”", "면도": "shaving; “face knife”", "세면": "washing one’s face", "체면": "face (as in saving face); “body face”", "직접": "directly; in person", "접대": "a reception; a warm welcome; “treating and waiting”", "접지": "ground connection; grounding; “contact the ground”", "접촉": "contact; touch; “contact and touch”"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_JA = [("초보자", "a novice"), ("학자", "a scholar"), ("보호자", "a guardian")]
_HA1 = [("지하도", "an underground pass"), ("남하하다", "to move down south"), ("천하", "the world; the whole country; “heaven below”"), ("하수도", "a sewer; “under water way”")]
_HA2 = [("반도", "a peninsula; “half island”"), ("반값", "half the price"), ("반달", "a half moon"), ("반올림", "rounding up (of a number); “half raising”")]
_GU1 = [("구인 광고", "a help-wanted ad; “people-seeking ad”"), ("구혼", "a marriage proposal; a courtship; “seeking a marriage”"), ("요구", "a demand; a claim; a request; “important seeking”")]
_GU2 = [("직업", "a job; an occupation"), ("교직", "the teaching profession"), ("직장", "a workplace"), ("직원", "an employee; a member of the staff; “job member”")]
_MY1 = [("가면", "a mask; “fake face”"), ("면도", "shaving; “face knife”"), ("세면", "washing one’s face"), ("체면", "face (as in saving face); “body face”")]
_MY2 = [("접대", "a reception; a warm welcome; “treating and waiting”"), ("접지", "ground connection; grounding; “contact the ground”"), ("접촉", "contact; touch; “contact and touch”")]

# ================================================================== L1: objectives and Sino-Korean
L1 = lesson(
    "Ch 35 · What the chapter teaches, 자 (者) · 하 (下) 반 (半) 기 (期) · 구 (求) 직 (職) · 면 (面) 접 (接)",
    "직장 구하기 · 하반기 · 구직 · 면접 · 특기자 · 지하도 · 반달 · 직업 · 면도",
    requires=[],
    cards=[
        card("What Chapter 35 teaches (직장 구하기)",
             "Chapter 35, “Job Hunting”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: ask about and discuss information related to job hunting; state how job hunters in Korea usually prepare for employment; and answer general questions at a job interview.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; the passive infixes 이, 히, 리, and 기; the passive verbs 보이다 and 들리다; an attributive form + 만큼; –다고 for a statement used as the object in a sentence; and the Sino-Korean syllables within 하반기 (下半期), 구직 (求職), and 면접 (面接)."),
        card("한국어에는: 자 (者) in 특기자",
             "The Sino-Korean syllable 자 (者) means a person. It is often used as a suffix, as in 초보자 (a novice), 학자 (a scholar), and 보호자 (a guardian). Thus, 특기자 in Topic Presentation A literally means “a person with special ability or skill”; 특기 (特技) refers to (one’s) special ability or special skill.",
             tables=[ktable(_JA)]),
        card("Sino-Korean in use: 하반기 (下半期)",
             "This Sino-Korean word means the second half of a (given) period/year. The first syllable 하 (下) means below, under, or bottom, as in 지하도 (an underground pass), 남하하다 (to move down south), 천하 (the world; the whole country; “heaven below”), and 하수도 (a sewer; “under water way”). The syllable 반 (半) means half, as in 반도 (a peninsula; “half island”), 반값 (half the price), 반달 (a half moon), and 반올림 (rounding up [of a number]; “half raising”). The last syllable 기 (期) means the duration of time, the interval of time, or period, as seen in the Sino-Korean notes of Chapter 34. Thus the literal meaning of the word 하반기 is “bottom half period”, and the word normally refers to the second half of a (given) period or year. As you may have guessed, the antonym of the word is 상반기.",
             tables=[ktable(_HA1), ktable(_HA2), ktable([("하반기", "the second half of a period or year; “bottom half period”"), ("상반기", "the first half of a period or year; “top half period”")])]),
        card("Sino-Korean in use: 구직 (求職)",
             "This Sino-Korean word means seeking a job. The first syllable 구 (求) means seeking, as in 구인 광고 (a help-wanted ad; “people-seeking ad”), 구혼 (a marriage proposal; a courtship; “seeking a marriage”), and 요구 (a demand; a claim; a request; “important seeking”). The second syllable 직 (職) means job, profession, or position, as in 직업 (a job; an occupation), 교직 (teaching profession), 직장 (a workplace), and 직원 (an employee; a member of the staff; “job member”).",
             tables=[ktable(_GU1), ktable(_GU2)]),
        card("Sino-Korean in use: 면접 (面接)",
             "This Sino-Korean word means a face-to-face interview. The first syllable 면 (面) means face or surface, as in 가면 (a mask; “fake face”), 면도 (shaving; “face knife”), 세면 (washing one’s face), and 체면 (face, as in saving face; “body face”). Recall that you learned the second syllable 접 (接) from the word 직접 in Chapter 32 and that it means contact or treat, as in 접대 (a reception; a warm welcome; “treating and waiting”), 접지 (ground connection; grounding; “contact the ground”), and 접촉 (contact; touch; “contact and touch”). Thus the literal meaning of the word 면접 is “face contact”, and the word refers to a face-to-face interview.",
             tables=[ktable(_MY1), ktable(_MY2)]),
    ],
    exercises=uniq(
        _tr(_JA + _HA1 + _HA2 + _GU1 + _GU2 + _MY1 + _MY2, k=3)
        + [M("What does 자 (者) mean?", "a person", ["a place", "a time", "a thing"], "초보자, 학자."), M("What does 특기자 mean literally?", "“a person with special ability or skill”", ["“a person who is late”", "“a job seeker”", "“a second half”"], "특기 + 자."), M("What does 하 (下) mean?", "below; under; bottom", ["half", "period", "seeking"], "지하도."), M("What does 반 (半) mean?", "half", ["below", "period", "face"], "반달."), M("What is the literal meaning of 하반기?", "“bottom half period”", ["“face contact”", "“job seeking”", "“half moon”"], "하 + 반 + 기."), M("What is the antonym of 하반기?", "상반기", ["하사", "반도", "구직"], "The book’s note."), M("What does 구 (求) mean?", "seeking", ["face", "half", "contact"], "구인 광고."), M("What does 직 (職) mean?", "job; profession; position", ["face", "contact", "half"], "직업."), M("What does 면 (面) mean?", "face; surface", ["contact", "seeking", "job"], "가면."), M("What does 접 (接) mean?", "contact; treat", ["face", "half", "seeking"], "접대."), M("What is the literal meaning of 면접?", "“face contact”", ["“bottom half period”", "“job seeking”", "“special skill”"], "면 + 접."),
           F("김 대리는 ___ 광고를 보고 회사에 지원했다. (a help-wanted ad)", "구인", ["구혼", "요구"], "구인 광고."), F("올 ___에는 대기업에서 신입사원을 많이 채용할 계획입니다. (second half)", "하반기", ["상반기", "하사"], "하반기."), F("저는 내일 ___시험을 봅니다. (an interview)", "면접", ["면도", "세면"], "면접."),
           read_q("특기자"), read_q("하반기"), read_q("구직"), read_q("면접"), read_q("지하도")]
    ),
)

# ================================================================== L2: Vocabulary Builder
_VG = [("대기업", "중소기업"), ("기회", "단점"), ("하반기", "장점"), ("채용", "뽑다"), ("이력서", "박람회"), ("서류", "관련"), ("접수", "참가")]
_VM = [("삼성, 엘지, 현대, 에스케이 등의 큰 회사", "대기업", "a large company"), ("회사에 지원하기 위해 개인 정보나 교육과 직업 경험 등을 써서 내는 것", "이력서", "a resume"), ("어떤 것의 크기", "규모", "size; scale"), ("좋은 점", "장점", "a merit; a strength"), ("일을 하기에 좋은 때나 경우", "기회", "an opportunity"), ("한 해의 칠 월부터 십이 월", "하반기", "the second half of a year"), ("모임이나 행사에 참석하는 것", "참가", "participation"), ("신청서 등을 받는 것", "접수", "receipt; acceptance")]
_VG_PAIRS = [("대기업", "a large enterprise; a conglomerate"), ("중소기업", "small and medium enterprises"), ("기회", "an opportunity"), ("단점", "a weak point; a shortcoming"), ("하반기", "the second half of a period or year"), ("장점", "a merit; a strength"), ("채용", "employment; hiring; recruitment"), ("뽑다", "to choose; to select; to employ"), ("이력서", "a resume"), ("박람회", "a fair; an expo"), ("서류", "documents"), ("관련", "relation; connection"), ("접수", "receipt; acceptance"), ("참가", "participation")]
L2 = lesson(
    "Ch 35 · Vocabulary Builder: guessing words and matching definitions",
    "대기업 · 중소기업 · 기회 · 단점 · 하반기 · 장점 · 채용 · 이력서 · 박람회 · 서류 · 접수 · 참가",
    requires=[],
    cards=[
        card("새 단어: the table of new words",
             "The book gives fourteen core words in two groups (Group A and Group B); each group reads a text that uses them, guesses the meanings in context and then exchanges meanings with a partner from the other group. The words (the meanings are the book’s Core Vocabulary; 서류 “documents” is the book’s gloss; the book’s 채용(하다), 접수(하다) and 참가(하다) are nouns that form verbs with 하다):",
             tables=[table(["Group A", "Group B"], [list(r) for r in _VG], say=[0, 1]), ktable(_VG_PAIRS)]),
        card("Vocabulary Learning Strategy: activate your prior knowledge",
             "We learn and remember new information more effectively when we are familiar with part of the information or when we can relate the new information to our prior knowledge. In other words, it is important to activate our prior knowledge in our learning process.\n\n"
             "In this chapter you will be learning about job hunting in Korea. You will encounter questions such as: What Korean companies and products am I familiar with? How much do I know about the educational background of Korean job applicants? Do I have any direct/indirect experiences or any general/specific knowledge relevant to this topic? The book asks you to jot down in English, in a box, any prior knowledge you might use in this chapter: 1. names of Korean companies; 2. Korean products; 3. educational background of Korean job applicants; 4. other relevant information regarding the Korean job market or job hunting. Then compare your knowledge with your classmates and your teacher."),
        card("Activity 1: match the definitions to the words",
             "The book gives eight descriptions on the left and eight words on the right (장점, 대기업, 참가, 이력서, 규모, 기회, 접수, 하반기) and asks you to match them by drawing lines. The company names are spelled out in Hangul (LG → 엘지, SK → 에스케이) and 7월/12월 are spelled 칠 월/십이 월. My matches:",
             tables=[table(["Description", "Word (mine)", "Meaning (mine)"], [list(r) for r in _VM], say=[0, 1])]),
        card("Activities left out", "Activity 2 (listening to four recordings and circling the described word), Activities 3 and 4 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 5 (a one-minute presentation on one of: 미래에 하고 싶은 일/다니고 싶은 직장; 전에 했던 일/다녔던 직장; 자신의 장점과 단점; 직장 구한 경험, written on an index card) are audio, computer and presentation activities."),
    ],
    exercises=uniq(
        vocab_exercises(_VG_PAIRS)
        + [M("Which word matches “" + a[:30] + "”?", b, [x[1] for x in _VM if x[1] != b][:3], "My match.") for a, b, c in _VM]
        + [F("삼성, 엘지, 현대는 모두 ___입니다. (large enterprises)", "대기업", ["중소기업", "박람회"], "대기업."), F("이 일은 경력을 쌓을 좋은 ___입니다. (opportunity)", "기회", ["단점", "서류"], "기회."), F("저의 ___은 화를 잘 내는 것입니다. (weak point)", "단점", ["장점", "기회"], "단점."), F("이 세탁기의 ___은 소리가 많이 나지 않는 것입니다. (strength)", "장점", ["단점", "서류"], "장점."), F("취직을 하려고 여러 곳에 ___를 냈어요. (resume)", "이력서", ["박람회", "서류"], "이력서."),
           read_q("대기업"), read_q("중소기업"), read_q("이력서"), read_q("취업박람회"), read_q("접수")]
    ),
)

# ================================================================== L3: Topic A
_A_DLG = [
    ("민정", "저, 국내 외국 기업에 지원하고 싶은데 자격조건이 어떻게 되나요?", "Um, I want to apply to a foreign company in Korea; what are the qualifications?"),
    ("상담원", "외국어를 할 줄 아세요?", "Do you know how to speak a foreign language?"),
    ("민정", "네, 전공이 불어여서 불어를 좀 해요. 그리고 영어도 좀 해요.", "Yes, my major is French so I speak a little French. And I speak a little English too."),
    ("상담원", "네, 특기가 외국어네요. 그럼 다른 특기도 있으세요?", "I see, your specialty is foreign languages. Then do you have any other specialty?"),
    ("민정", "네, 컴퓨터자격증이 있어요.", "Yes, I have a computer certificate."),
    ("상담원", "좋습니다. 외국 기업들이 보통 컴퓨터와 외국어 특기자를 우대해요.", "Good. Foreign companies usually give preferential treatment to people with computer and foreign-language skills."),
    ("민정", "그래요? 그런데 이력서를 잘 쓰려면 어떻게 해야 하나요?", "Is that so? By the way, what should I do to write a good resume?"),
    ("상담원", "외국어나 자격증 같은 특기와 관련된 내용을 반드시 적으세요.", "Be sure to write content related to your specialties, like foreign languages or certificates."),
    ("민정", "네. 그런데 이번 하반기에 외국 기업에서 신입사원을 많이 채용하나요?", "Yes. By the way, will foreign companies hire many new employees this second half of the year?"),
    ("상담원", "그럼요. 자세한 내용은 각 외국 기업의 채용 담당자에게 문의해 보세요.", "Of course. For the details, try asking the person in charge of hiring at each foreign company."),
]
_A_WORDS = ["관련", "기업(체)", "내용", "박람회", "상반기", "소지", "우대", "이력서", "~자", "자기소개서", "작성", "접수", "제출", "지원서", "참가", "채용", "특기", "하반기", "학력"]
_LGAD = [("엘지 신입사원 채용 안내", "Guide to LG new employee recruitment"), ("최고의 기업 엘지와 함께 할 신입사원을 모집합니다.", "We are recruiting new employees to work together with LG, the best company."), ("많은 관심 부탁 드립니다.", "We ask for your great interest."), ("엘지 채용 홈페이지에서 입사 지원서를 다운로드 받으십시오.", "Please download the job application from the LG recruiting homepage."), ("서류 입사 지원서, 이력서, 자기소개서", "Documents: job application, resume, letter of self-introduction"), ("입사 지원은 온라인 접수만 가능합니다.", "Job applications can only be received online."), ("엘지그룹 채용홈페이지를 통해서 시월 이십오 일까지 지원하시기 바랍니다.", "Please apply through the LG Group recruiting homepage by October 25."), ("자세한 내용은 엘지 캐리어스 사이트 윗부분 채용문의에서 일대일 질문하기로 문의해 주십시오.", "For details, please inquire through “Ask one-to-one” under “Recruitment inquiries” at the top of the LG Careers site.")]
L3 = lesson(
    "Ch 35 · Topic A: I’d like to apply to a foreign company (외국 기업에 지원하고 싶은데요)",
    "외국 기업에 지원하고 싶은데요 · 자격조건 · 특기 · 우대 · 이력서 · 하반기 · 채용 · 입사 지원서",
    requires=[],
    cards=[
        card("Topic A: I’d like to apply to a foreign company (외국 기업에 지원하고 싶은데요)",
             "A female job seeker is talking to a male job consultant at a job fair. (The English is mine; the book gives none.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 관련(하다/되다), 소지(하다), 우대(하다/받다), 작성(하다/되다), 접수(하다/되다), 제출(하다/되다), 참가(하다) and 채용(하다/되다) take the forms in parentheses.",
             tables=[ktable(_rows([w for w in _A_WORDS if _HG(w) and "(" not in w and "~" not in w])), table(["Word", "Meaning"], [["기업(체)", "a business enterprise; a corporation"], ["~자", "a suffix denoting a person"]], say=[0])]),
        card("Follow-up 1 (Reading): an LG new-employee recruiting advertisement",
             "The following advertisement is from a Korean corporate recruiting ad. The book asks you to fill in a table in English (how to get an application; documents to submit; how to submit documents; contact for inquiries) and glosses 서류: documents. The ad is the book’s; the company name is spelled out in Hangul, the date is spelled in Hangul, and the web address is not read out. The English is mine.",
             examples=passage(_LGAD)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Item", "Answer (mine)"], [["How to get an application", "Download it from the LG recruiting homepage"], ["Documents to submit", "Job application, resume, letter of self-introduction"], ["How to submit documents", "Online only, through the LG Group recruiting homepage, by October 25"], ["Contact for inquiries", "The “Recruitment inquiries” → “Ask one-to-one” section of the LG Careers site"]])]),
        card("Activities left out", "Follow-up 2 (listening to a news clip about a job fair and filling in the date and place, participants and programs), the list of useful websites (the Korea Recruitment Fair site) and the Topic Presentation A study steps (SMART Board and role-reading in pairs) are audio, computer and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_strip(_A_DLG) + _LGAD[1:4], k=3)
        + [M("What does 민정 want to do?", "Apply to a foreign company in Korea", ["Quit her job", "Study abroad", "Open a store"], "외국 기업에 지원하고 싶은데."), M("What is 민정’s major?", "French", ["English", "Computer science", "Business"], "전공이 불어."), M("What other specialty does 민정 have?", "A computer certificate", ["A driver’s license", "A teaching license", "A medical license"], "컴퓨터자격증."), M("Whom do foreign companies usually give preferential treatment?", "People with computer and foreign-language skills", ["Older people", "People with no skills", "Students only"], "컴퓨터와 외국어 특기자를 우대."), M("What should 민정 be sure to write on her resume?", "Content related to her specialties", ["Her age only", "Her address only", "Nothing"], "특기와 관련된 내용."), M("Who should she ask for details?", "The person in charge of hiring at each company", ["A teacher", "A friend", "A soldier"], "채용 담당자."), M("How can people apply to LG?", "Online only", ["By mail only", "In person only", "By phone"], "온라인 접수만 가능."),
           F("외국 기업들이 보통 컴퓨터와 외국어 ___를 우대해요. (those with special skills)", "특기자", ["구직자", "지원자"], "특기자."), F("이력서를 잘 쓰려면 특기와 ___된 내용을 적으세요. (related)", "관련", ["제출", "접수"], "관련."), F("이번 ___에 외국 기업에서 신입사원을 많이 채용하나요? (second half)", "하반기", ["상반기", "학력"], "하반기."), F("자세한 내용은 채용 담당자에게 ___해 보세요. (inquire)", "문의", ["제출", "작성"], "문의하다."), F("올 ___에는 신입사원을 모집하지 않습니다. (first half)", "상반기", ["하반기", "학력"], "상반기."),
           read_q("외국 기업에 지원하고 싶은데요"), read_q("외국 기업들이 보통 컴퓨터와 외국어 특기자를 우대해요"), read_q("이력서를 잘 쓰려면 어떻게 해야 하나요"), read_q("채용 담당자에게 문의해 보세요"), read_q("입사 지원은 온라인 접수만 가능합니다")]
    ),
)

# ================================================================== L4: Topic A activities
_WL1 = [("상담", "consultation; counseling"), ("관련", "relation; connection"), ("기업(체)", "a business enterprise; a corporation"), ("우대", "preferential treatment"), ("이력서", "a resume"), ("작성", "filling out (a form)"), ("자격증", "a certificate; a license"), ("소지자", "a holder; a possessor"), ("참가", "participation"), ("취업", "getting a job; employment"), ("자기소개서", "a letter of self-introduction"), ("채용", "employment; hiring"), ("유학", "studying abroad"), ("학력", "educational background"), ("특기", "one’s special ability"), ("문의", "an inquiry"), ("전공", "a major"), ("지원서", "an application"), ("제출", "submission"), ("어학연수", "foreign language study (abroad)"), ("학점", "a (college) credit"), ("관리", "management"), ("성적", "grades; results"), ("접수", "receipt; acceptance")]
_SKT = [["채용부서", "경영/인사", "어문, 경영, 경제 전공 00명"], ["", "전자정보통신", "관련전공 00명"], ["자격조건", "사 년제 대학 이 월 졸업예정자 또는 졸업자", "영어 특기자 및 컴퓨터 자격증 소지자 우대"], ["제출서류", "입사지원서 (당사 홈페이지에서 다운로드), 이력서, 자기소개서, 성적증명서", ""], ["지원서 접수 및 일정", "접수 기간 삼 월 팔 일부터 삼 월 이십이 일 열여덟 시까지", "접수 방법 인터넷 접수와 방문 접수만 가능합니다. 합격자 발표 삼 월 삼십 일 열여덟 시, 홈페이지에서 합격자 확인 가능합니다."], ["채용 관련 문의", "에스케이 씨앤비 인사팀 담당자에게 문의 바랍니다.", ""]]
_SKTX = [("에스케이 그룹 상반기 신입사원 채용", "SK Group first-half new employee recruitment"), ("에스케이 그룹에서 여러분의 미래를 시작하십시오.", "Start your future at the SK Group."), ("채용부서는 경영과 인사 어문, 경영, 경제 전공 몇 명, 전자정보통신 관련전공 몇 명이다.", "The hiring departments are management/personnel (language, business and economics majors) and electronic information and communication (related majors); the numbers are given as 00."), ("자격조건은 사 년제 대학 이 월 졸업예정자 또는 졸업자, 영어 특기자 및 컴퓨터 자격증 소지자 우대이다.", "Qualifications: expected graduates of a four-year university in February, or graduates; people with English skills and holders of a computer certificate get preferential treatment."), ("제출서류는 입사지원서, 이력서, 자기소개서, 성적증명서이다.", "Documents to submit: job application, resume, letter of self-introduction and transcript."), ("접수 기간은 삼 월 팔 일부터 삼 월 이십이 일 열여덟 시까지이고 인터넷 접수와 방문 접수만 가능하다.", "The application period is from March 8 to March 22 at 18:00, and only online and in-person applications are possible."), ("합격자 발표는 삼 월 삼십 일 열여덟 시에 홈페이지에서 확인 가능하다.", "The successful applicants will be announced at 18:00 on March 30 and can be checked on the homepage.")]
L4 = lesson(
    "Ch 35 · Topic A activities: key words and a recruiting announcement",
    "상담 · 우대 · 소지자 · 어학연수 · 성적 · 상반기 신입사원 채용 · 제출서류 · 접수 기간 · 합격자 발표",
    requires=[],
    cards=[
        card("Activity 1 (Reading): key words for Activity 4",
             "The book lists twenty-four key words and expressions you will use in the role-play (Activity 4) and asks you to fill in the English meanings, using a dictionary as necessary. The words that appear in the Core Vocabulary have the book’s meanings; the rest (상담, 소지자, 취업, 유학, 문의, 관리, 성적, 전공, 어학연수, 학점, 자격증) are mine.",
             tables=[ktable(_WL1)]),
        card("Activity 2 (Reading): a classified newspaper section on job recruiting",
             "This classified section shows information about job recruiting. The book asks you to fill in a table in English: opening and closing dates for application; department hiring; required qualifications; preferred candidate; contact for inquiries; and glosses 증명서: a certificate. The announcement is the book’s (SK Group first-half new-employee hiring; the e-mail address and web address are not read out); the numbers in the table below are spelled out in Hangul. The English is mine.",
             tables=[table(["Item", "Information", "Details"], _SKT)]),
        card("The same announcement as sentences", "The sentences below put the table in running text (mine; the information is the book’s).", examples=passage(_SKTX)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Item", "Answer (mine)"], [["Opening and closing dates for application", "March 8 to March 22, 18:00"], ["Department hiring", "Management/personnel (language, business, economics majors); electronic information and communication (related majors)"], ["Required qualifications", "Expected graduates (February) or graduates of a four-year university"], ["Preferred candidate", "People with English skills and holders of a computer certificate"], ["Contact for inquiries", "The SK C&B personnel team person in charge (by e-mail)"]])]),
        card("Activities left out", "Activity 3 (listening to three dialogs between a female job seeker and a male job consultant and filling in the job seeker’s concerns and the consultant’s advice; the book gives two hints: “be sure to write about experience related to her specialties” and “speaks English, but not very well / Do they hire people with only a high school diploma?”) and Activity 4 (a role-play at a job fair, with Situation cards) are audio and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(["관련", "우대", "작성", "참가", "채용", "접수"]) + [("취업", "getting a job; employment"), ("유학", "studying abroad"), ("문의", "an inquiry"), ("성적", "grades; results")])
        + _tr(_SKTX[1:], k=3)
        + [M("Which group is this announcement from?", "SK Group", ["LG Group", "Samsung", "Hyundai"], "에스케이 그룹."), M("What kind of university graduates are wanted?", "Four-year university graduates or those expected to graduate in February", ["Middle school graduates", "Two-year college graduates only", "Anyone"], "사 년제 대학."), M("Who gets preferential treatment?", "People with English skills and computer certificates", ["Older people", "Anyone", "People with no skills"], "영어 특기자 및 컴퓨터 자격증 소지자 우대."), M("How can people apply?", "Online or in person", ["By mail", "By phone", "By fax"], "인터넷 접수와 방문 접수."), M("When are the successful applicants announced?", "March 30 at 18:00", ["March 8", "March 22", "April 1"], "삼 월 삼십 일."),
           F("에스케이 그룹 ___ 신입사원 채용 (first half)", "상반기", ["하반기", "학력"], "상반기."), F("영어 특기자 및 컴퓨터 자격증 ___자 우대 (holder)", "소지", ["제출", "접수"], "소지자."), F("제출서류는 입사지원서, 이력서, 자기소개서, ___증명서이다. (grades)", "성적", ["경력", "학력"], "성적증명서."), F("접수 ___은 삼 월 팔 일부터 삼 월 이십이 일까지이다. (period)", "기간", ["방법", "시간"], "접수 기간."), F("채용 관련 ___은 담당자에게 문의 바랍니다. (inquiries)", "문의", ["제출", "접수"], "문의."),
           read_q("에스케이 그룹 상반기 신입사원 채용"), read_q("제출서류"), read_q("접수 기간"), read_q("합격자 발표"), read_q("영어 특기자 우대")]
    ),
)

# ================================================================== L5: Topic B
_B_TXT = [
    ("김영호 군은 대학교 삼 학년이다.", "Mr. Kim Youngho is a third-year university student."),
    ("대학에서 경영학을 공부하고 있다.", "He is studying business administration at university."),
    ("김 군의 희망은 내년에 대기업 인턴사원으로 뽑히는 것이다.", "Mr. Kim’s hope is to be selected next year as an intern at a large company."),
    ("인턴으로 일하면서 경력을 쌓고 싶어한다.", "He wants to build experience while working as an intern."),
    ("경력이 많으면 취업에 유리하다.", "If you have a lot of experience, it is advantageous for getting a job."),
    ("그래서 요즘은 여자 친구와 데이트할 시간도 없이 바쁘다.", "So these days he is busy, without even time to date his girlfriend."),
    ("보통 학교에 가면 가장 먼저 취업게시판을 본다.", "Usually when he goes to school, the first thing he looks at is the job bulletin board."),
    ("게시판에서 여러 회사의 유용한 구직정보를 찾을 수 있다.", "On the board, he can find useful job-seeking information from many companies."),
    ("그리고 수업이 끝나면 친구들과 그룹 스터디를 한다.", "And when class is over, he does a group study with his friends."),
    ("그 후에 학원에 가서 영어면접에 필요한 회화를 배운다.", "After that, he goes to a private academy and learns the conversation needed for the English interview."),
    ("그리고 체력 관리를 위해 체육관에 가서 한 시간 동안 운동을 한다.", "And, to manage his physical strength, he goes to the gym and exercises for an hour."),
    ("집에 돌아가면 인터넷으로 구인정보를 찾아보고 서류 전형에 필요한 자기소개서를 계속 업데이트한다.", "When he returns home, he looks for job-listing information on the internet and keeps updating the letter of self-introduction needed for the documents screening."),
]
_B_WORDS = ["게시판", "경력", "구인", "구직(자)", "~군", "대기업", "면접", "분야", "뽑다", "서류 전형", "쌓다", "업데이트", "유리하다", "유용하다", "인원", "임금", "중소기업", "희망"]
_KB = "Many companies in Korea require applicants to demonstrate their mastery of foreign languages like English, Chinese, and Japanese through oral interviews and a written test. Thus, college students spend a great deal of time and effort preparing for tests like the TOEIC (the Test of English for International Communication), an English language test designed specifically to measure everyday English skills on the job. Many students also spend several months to a year in a foreign country to learn the country’s language (어학 연수)."
_SEOUL = [("서울일자리센터", "Seoul Job Center"), ("일자리와 함께 희망도 선물합니다.", "We give you hope together with a job."), ("서울일자리센터는 취업을 원하는 서울시민 모두에게 다양하고 안정적인 일자리를 제공하기 위한 취업 전문기관입니다.", "The Seoul Job Center is a job specialist institution that exists to provide diverse and stable jobs to all Seoul citizens who want employment."), ("서울특별시가 운영하는 이 기관에서는 현재 스물네 명의 전문상담사가 상담을 하고 있습니다.", "At this institution run by the Seoul Metropolitan Government, twenty-four professional counselors are currently giving counseling."), ("취업을 원하는 시민들에게는 전문직업상담사가 일대일 상담을 통해 구직자 적성에 맞는 일자리를 소개해 주고 필요하면 직업교육도 도와줍니다.", "For citizens who want employment, professional job counselors introduce jobs that suit the job seeker’s aptitude through one-to-one counseling and, if necessary, also help with job training."), ("구인을 원하는 기업들에게는 유능한 사람을 분야와 조건에 맞게 검색해 정보를 찾을 수 있는 환경을 마련해주며 유능한 사람의 추천과 채용도 대신해 드립니다.", "For companies that want to hire, it prepares an environment where they can search for capable people by field and conditions and find information, and also recommends and hires capable people on their behalf."), ("창업을 원하는 시민들에게는 창업전문상담사가 창업아이템 선정부터 재무컨설팅 등 창업에 필요한 상담을 제공해 창업에 성공할 수 있도록 도와드립니다.", "For citizens who want to start a business, start-up counselors provide the counseling needed for starting a business, from selecting a business item to financial consulting, and help them succeed in starting it.")]
L5 = lesson(
    "Ch 35 · Topic B: I want to work at a large company (대기업에 취업하고 싶어요)",
    "대기업에 취업하고 싶어요 · 인턴사원 · 경력 · 취업게시판 · 그룹 스터디 · 영어면접 · 서류 전형 · 서울일자리센터",
    requires=[],
    cards=[
        card("Topic B: I want to work at a large company (대기업에 취업하고 싶어요)",
             "In this passage you will learn about a college student’s daily routine while looking for a job. (The English is mine; the book gives none; the numbers are spelled out in Hangul.)",
             examples=passage(_B_TXT)),
        card("한국에서는: language tests", _KB),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); 구직(자), 면접(~[을] 보다), 희망(하다) take the forms in parentheses.",
             tables=[ktable(_rows([w for w in _B_WORDS if _HG(w) and "(" not in w and "~" not in w and " " not in w])), table(["Word", "Meaning"], [["구직(자)", "seeking a job (a job seeker; a job hunter)"], ["~군", "a title for a young man"], ["서류 전형", "documents screening"]], say=[0])]),
        card("Follow-up 2 (Reading): an announcement from the City of Seoul",
             "The following announcement is from the City of Seoul’s website. The book asks you to fill in a table in English with the services provided by the Seoul Job Center for job seekers, recruiters and entrepreneurs. The text is the book’s with the numbers spelled out and the quotation marks and bullet symbols dropped; the English is mine.",
             examples=passage(_SEOUL)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["For", "Services (mine)"], [["Job seekers", "One-to-one counseling by a professional job counselor; introduction of jobs that fit the seeker’s aptitude; job training if needed"], ["Recruiters", "An environment for searching capable people by field and conditions; recommendation and hiring of capable people on their behalf"], ["Entrepreneurs", "Start-up counseling from choosing a business item to financial consulting, to help them succeed"]])]),
        card("Activities left out", "Follow-up 1 (listening to three dialogs in which college students talk about preparing for a job and filling in the job preparation and additional information) and the Topic Presentation B study steps (SMART Board) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT + _SEOUL[1:5], k=3)
        + [M("What year is 김영호 in university?", "Third year", ["First year", "Second year", "Fourth year"], "삼 학년."), M("What does he study?", "Business administration", ["Computer science", "Law", "Education"], "경영학."), M("What is his hope?", "To be selected as an intern at a large company next year", ["To study abroad", "To marry", "To quit school"], "대기업 인턴사원으로 뽑히는 것."), M("What is the first thing he does at school?", "Look at the job bulletin board", ["Eat lunch", "Exercise", "Study English"], "취업게시판을 본다."), M("What does he do after class with his friends?", "A group study", ["A party", "Shopping", "Sports"], "그룹 스터디."), M("What does he learn at the academy?", "Conversation for the English interview", ["Computer skills", "Cooking", "Driving"], "영어면접에 필요한 회화."), M("How long does he exercise?", "One hour", ["Two hours", "Thirty minutes", "Three hours"], "한 시간."), M("What does he keep updating at home?", "His letter of self-introduction", ["His resume photo", "His diary", "His blog"], "자기소개서를 계속 업데이트."),
           F("김 군의 ___은 내년에 대기업 인턴사원으로 뽑히는 것이다. (hope)", "희망", ["경력", "임금"], "희망."), F("인턴으로 일하면서 ___을 쌓고 싶어한다. (experience)", "경력", ["희망", "임금"], "경력."), F("경력이 많으면 취업에 ___하다. (advantageous)", "유리", ["유용", "철저"], "유리하다."), F("게시판에서 여러 회사의 ___한 구직정보를 찾을 수 있다. (useful)", "유용", ["유리", "철저"], "유용하다."), F("서류 ___에 필요한 자기소개서를 계속 업데이트한다. (screening)", "전형", ["제출", "접수"], "서류 전형."),
           read_q("대기업에 취업하고 싶어요"), read_q("김영호 군은 대학교 삼 학년이다"), read_q("경력이 많으면 취업에 유리하다"), read_q("게시판에서 여러 회사의 유용한 구직정보를 찾을 수 있다"), read_q("서울일자리센터")]
    ),
)

# ================================================================== L6: Grammar A: passive infixes
_PS = [("보다", "to see; to look", "보이다", "to be seen"), ("쓰다", "to use", "쓰이다", "to be used"), ("섞다", "to mix", "섞이다", "to be mixed"), ("잡다", "to catch", "잡히다", "to be caught"), ("뽑다", "to select", "뽑히다", "to be selected"), ("닫다", "to close", "닫히다", "to be closed"), ("듣다", "to hear; to listen", "들리다", "to be heard"), ("열다", "to open", "열리다", "to be opened"), ("팔다", "to sell", "팔리다", "to be sold"), ("흔들다", "to shake", "흔들리다", "to be shaken"), ("풀다", "to solve", "풀리다", "to be solved"), ("안다", "to hug", "안기다", "to be hugged"), ("끊다", "to cut; to hang up", "끊기다", "to be cut; to be hung up")]
_PSE = [("여기서 학교 건물이 보입니다.", "The school building is seen from here."), ("교실문이 일곱 시에 닫힙니다.", "The classroom door is closed at seven."), ("오늘 아침에 물이 끊겼습니다.", "The water was cut off this morning.")]
_PSX = [("만들다", "to make", "만들어지다", "to be made"), ("나누다", "to divide", "나누어지다", "to be divided"), ("짓다", "to build", "지어지다", "to be built"), ("예약하다", "to book", "예약되다", "to be booked"), ("증가하다", "to increase", "증가되다", "to be increased"), ("접수하다", "to receive", "접수되다", "to be received")]
_PSE2 = [("인형이 예쁘게 만들어졌어요.", "“A doll was made pretty.” / A pretty doll was made."), ("부산까지 비행기표가 예약되었어요.", "The ticket to Busan has been booked. (The book’s English says “train ticket”, but the Korean says 비행기표, plane ticket.)")]
_P3 = [("어젯밤에 총소리를 들었습니다.", "어젯밤에 총소리가 들렸습니다.", "I heard a gunshot last night. / A gunshot was heard last night."), ("이번에 신입사원을 서른 명 뽑았습니다.", "이번에 신입사원이 서른 명 뽑혔습니다.", "We selected thirty new employees this time. / Thirty new employees were selected this time."), ("전화를 갑자기 끊었어요.", "전화가 갑자기 끊겼어요.", "(Someone) cut the phone suddenly. / The phone call was suddenly cut off."), ("조용히 문을 열었습니다.", "조용히 문이 열렸습니다.", "(Someone) opened the door quietly. / The door opened quietly."), ("주말에 영화표를 많이 팔았습니다.", "주말에 영화표가 많이 팔렸습니다.", "(We) sold many movie tickets on the weekend. / Many movie tickets were sold on the weekend."), ("고양이가 쥐를 잡았습니다.", "쥐가 고양이한테 잡혔습니다.", "The cat caught the mouse. / The mouse was caught by the cat.")]
L6 = lesson(
    "Ch 35 · Grammar A: the passive infixes 이, 히, 리 and 기",
    "피동 · 보다-보이다 · 닫다-닫히다 · 열다-열리다 · 끊다-끊기다 · 만들어지다 · 예약되다",
    requires=[],
    cards=[
        card("The passive voice",
             "The passive tense is a grammatical voice in which the subject receives the action of a transitive verb. In English, the passive voice is created with the auxiliary verb “to be” and the past participle of the transitive verb (e.g., is opened and was built).\n\n"
             "In Korean, the passive voice is expressed differently. The infixes 이, 히, 리, 기, 우, 구, and 추 are used to make some native Korean verbs causative verbs: 먹이다 to feed (a person) and 살리다 to revive (a person). (For more detail, refer to the Grammar in Focus section in Chapter 30.) The same infixes, except 추, are also used to make native transitive verbs passive verbs. For example: 보다 (to see; to look at) → 보이다 (to be seen); 닫다 (to close) → 닫히다 (to be closed); 열다 (to open) → 열리다 (to be opened); 끊다 (to sever; to disconnect) → 끊기다 (to be severed; to be disconnected).\n\n"
             "The following sentences contain some of these passive verbs (the English is the book’s):",
             examples=passage(_PSE)),
        card("There is no rule", "As with the causative verbs in Chapter 30, there is no rule that helps predict which infix works with which verb. The following table lists the most common passive verbs, grouped by infix (the book’s table, with 듣다 → 들리다 under 리 and 끊다 → 끊기다 under 기):",
             tables=[table(["Infix", "Transitive verb", "Meaning", "Passive verb", "Meaning"], [["이", *_PS[0][:2], *_PS[0][2:]], ["이", *_PS[1][:2], *_PS[1][2:]], ["이", *_PS[2][:2], *_PS[2][2:]], ["히", *_PS[3][:2], *_PS[3][2:]], ["히", *_PS[4][:2], *_PS[4][2:]], ["히", *_PS[5][:2], *_PS[5][2:]], ["리", *_PS[6][:2], *_PS[6][2:]], ["리", *_PS[7][:2], *_PS[7][2:]], ["리", *_PS[8][:2], *_PS[8][2:]], ["리", *_PS[9][:2], *_PS[9][2:]], ["리", *_PS[10][:2], *_PS[10][2:]], ["기", *_PS[11][:2], *_PS[11][2:]], ["기", *_PS[12][:2], *_PS[12][2:]]], say=[0, 1, 3])]),
        card("참고: two other ways to make a passive verb",
             "There are two other ways to make a transitive verb a passive verb. 1. Some transitive verbs become passive verbs when –아/어지다 is added to the stem. 2. Some transitive verbs that end in 하다 become passive verbs when 되다 is added to the stem.",
             tables=[table(["Transitive verb", "Meaning", "Passive verb", "Meaning"], [list(r) for r in _PSX], say=[0, 2])],
             examples=passage(_PSE2)),
        card("Follow-up 1 (Writing): the table filled in",
             "The book gives eleven verbs (보다, 쓰이다, 섞다, 잡다, 뽑히다, 닫다, 들리다, 열다, 팔리다, 흔들다, 끊다) and asks you to write the passive or active counterpart. My answers:",
             tables=[table(["Given verb", "Counterpart (mine)"], [["보다", "보이다"], ["쓰이다", "쓰다"], ["섞다", "섞이다"], ["잡다", "잡히다"], ["뽑히다", "뽑다"], ["닫다", "닫히다"], ["들리다", "듣다"], ["열다", "열리다"], ["팔리다", "팔다"], ["흔들다", "흔들리다"], ["끊다", "끊기다"]], say=[0, 1])]),
        card("Follow-up 3 (Reading and writing): change each sentence into a passive sentence",
             "The model is 문을 닫았습니다 → 문이 닫혔습니다. The book gives six sentences to change; the 30 in the second sentence is spelled 서른. The answers are mine (the English is mine):",
             tables=[table(["Active sentence", "Passive sentence (mine)", "English (mine)"], [list(r) for r in _P3], say=[0, 1])]),
        card("Activities left out", "Follow-up 2 (a SMART Board activity) and Follow-up 6 (the teacher posts sheets of paper with active and passive verbs, and the students walk round writing sentences on them) are computer and group activities."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, _, b, _ in []] or _PSE + _PSE2[:1], k=3)
        + [M("What does " + p[2] + " mean?", p[3], [x[3] for x in _PS if x[3] != p[3]][:3], "Passive of " + p[0] + ".") for p in _PS]
        + [M("What does " + p[0] + " mean?", p[1], [x[1] for x in _PS if x[1] != p[1]][:3], "Active.") for p in _PS[:6]]
        + [M("What is the passive of " + p[0] + "?", p[2], [x[2] for x in _PS if x[2] != p[2]][:3], "The book’s table.") for p in _PS]
        + [M("What does 만들어지다 mean?", "to be made", ["to make", "to build", "to divide"], "-아/어지다."), M("What does 예약되다 mean?", "to be booked", ["to book", "to increase", "to receive"], "하다 → 되다."), M("Is there a rule telling which infix goes with which verb?", "No", ["Yes, always 이", "Yes, always 리", "Yes, by the final consonant"], "The book’s note."), M("Which infixes make causative verbs but not passive ones?", "추 (the others also make passives)", ["이", "히", "기"], "The book’s note."),
           F("여기서 학교 건물이 ___. (is seen)", "보입니다", ["봅니다", "보여줍니다"], "보이다."), F("교실문이 일곱 시에 ___. (is closed)", "닫힙니다", ["닫습니다", "닫아요"], "닫히다."), F("오늘 아침에 물이 ___. (was cut off)", "끊겼습니다", ["끊었습니다", "끊어요"], "끊기다."), F("문을 닫았습니다 → 문이 ___. (was closed)", "닫혔습니다", ["닫았습니다", "닫힙니다"], "닫히다."), F("인형이 예쁘게 ___. (was made)", "만들어졌어요", ["만들었어요", "만들어요"], "만들어지다."), F("부산까지 비행기표가 ___. (has been booked)", "예약되었어요", ["예약했어요", "예약해요"], "예약되다."),
           read_q("여기서 학교 건물이 보입니다"), read_q("교실문이 일곱 시에 닫힙니다"), read_q("오늘 아침에 물이 끊겼습니다"), read_q("쥐가 고양이한테 잡혔습니다"), read_q("주말에 영화표가 많이 팔렸습니다")]
    ),
)

# ================================================================== L7: Grammar B: 보이다 and 들리다
_BO = [("어제 김 선생님을 봤습니다.", "I saw Mr. Kim yesterday."), ("저기 저 산을 한번 보세요.", "Please look at the mountain over there."), ("아내가 설거지할 때 나는 아기를 봅니다.", "I watch the baby when my wife does the dishes.")]
_DE = [("어젯밤 총소리를 들었어요.", "I heard a gunshot last night."), ("내 말을 잘 들으세요.", "Please listen to “my words.” / Please listen to me.")]
_BD = [("왼쪽에 강이 보였습니다.", "A river was seen on the left. / I saw a river on the left."), ("멀리서 자동차 소리가 들립니다.", "The sound of a car is heard in the distance. / I hear a car in the distance.")]
_BQ = [("소리가 잘 들립니까?", "“Is (the sound) well heard?” / Do you hear the sound well? / Can you hear the sound well?"), ("네, 잘 들립니다.", "“Yes, it is well heard.” / Yes, I hear it well. / I can hear it."), ("칠판이 잘 보입니까?", "“Is (the chalkboard) seen well?” / Do you see (the chalkboard) well? / Can you see (the chalkboard)?"), ("아니요, 잘 안 보입니다.", "“No, it is not seen well.” / No, I don’t see it well. / I can’t see it well."), ("무엇이 보입니까?", "“What is (being) seen?” / What do you see? / What can you see?"), ("무슨 소리가 들립니까?", "“What sound is being heard?” / What do you hear? / What can you hear?")]
_BM = [("방에 뭐가 보입니까?", "What do you see in the room?"), ("방에 컴퓨터가 보입니다.", "I see a computer in the room."), ("또 뭐가 보입니까?", "What else do you see?"), ("또 시계가 보입니다.", "I also see a clock.")]
_BM2 = [("새 소리가 들립니다.", "I hear the sound of a bird."), ("비 소리가 들립니다.", "I hear the sound of rain.")]
_NB = [("어젯밤 열 시쯤에 집 앞에서 차가 갑자기 멈추는 소리가 들렸어요.", "At about ten last night, I heard the sound of a car suddenly stopping in front of the house."), ("저는 그때 거실에서 책을 읽고 있었어요.", "I was reading a book in the living room then."), ("그런데 밖에서 이야기 소리가 들렸어요.", "But I heard the sound of talking outside."), ("그래서 밖을 봤어요.", "So I looked outside."), ("그때 두 남자가 이웃집에서 나오는 것이 보였어요.", "Then I saw two men coming out of the neighboring house."), ("그리고 차 문이 열렸어요.", "And the car door opened."), ("그 두 사람은 빠르게 그 차 안으로 들어갔어요.", "The two people quickly got into the car."), ("그리고 문이 닫혔어요.", "And the door closed."), ("그리고 차가 출발하는 소리를 들었어요.", "And I heard the sound of the car leaving.")]
L7 = lesson(
    "Ch 35 · Grammar B: the passive verbs 보이다 and 들리다",
    "보이다 · 들리다 · 잘 보입니까 · 잘 들립니다 · 무엇이 보입니까 · 무슨 소리가 들립니까 · 목격자의 진술",
    requires=[],
    cards=[
        card("보다 and 듣다 versus 보이다 and 들리다",
             "In Korean, the verb 보다 means to see, to look, or to watch, depending on the context. For example (the English is the book’s):",
             examples=passage(_BO)),
        card("듣다", "Likewise, the verb 듣다 means to hear or to listen:", examples=passage(_DE)),
        card("The passive versions mean only “to be seen” and “to be heard”",
             "However, the passive versions of these two verbs (보이다 and 들리다) mean only to be seen (not to be looked at or to be watched) and to be heard (not to be listened to). For example (the English is the book’s):",
             examples=passage(_BD)),
        card("What you can see and hear", "For this reason, Koreans use 보이다 and 들리다 when describing what they (can) see or hear (the book writes the omitted topic in parentheses; the English is the book’s):", examples=passage(_BQ)),
        card("Follow-up 4 (Speaking): 뭐가 보입니까?",
             "In pairs, Partner A asks what Partner B sees in a picture of a room (and then a house), and B answers using ~이/가 보입니다; then Partner B makes a sentence using ~이/가 들립니다 after hearing a sound. The pictures and sounds are not included. The book’s models (the English is mine):",
             examples=dlg([("A", _BM[0][0], _BM[0][1]), ("B", _BM[1][0], _BM[1][1]), ("A", _BM[2][0], _BM[2][1]), ("B", _BM[3][0], _BM[3][1]), ("A", _BM2[0][0], _BM2[0][1]), ("B", _BM2[1][0], _BM2[1][1])])),
        card("Follow-up 5 (Reading): a neighbor’s statement",
             "Someone broke into Taejin’s house while no one was home. The book asks you to read the statement written by a neighbor who lives across the street and: 1. circle all the passive verbs; 2. identify in English what the neighbor heard; 3. identify in English what the neighbor saw; 4. change the underlined sentence into the passive voice (the underline is not in the text I have). The statement is the book’s (the time is spelled in Hangul); the English is mine.",
             examples=passage(_NB)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Item", "Answer (mine)"], [["1. Passive verbs", "들렸어요 (twice), 보였어요, 열렸어요, 닫혔어요"], ["2. What the neighbor heard", "A car suddenly stopping in front of the house; the sound of talking outside; the car leaving"], ["3. What the neighbor saw", "Two men coming out of the neighboring house"], ["4. Passive form of the one active hearing sentence", "그리고 차가 출발하는 소리가 들렸어요."]])]),
    ],
    exercises=uniq(
        _tr(_BO + _DE + _BD + _BQ + _NB, k=3)
        + [M("What do 보이다 and 들리다 mean?", "to be seen and to be heard", ["to look at and to listen to", "to show and to tell", "to watch and to speak"], "The book’s note."), M("Which means “to listen to”?", "듣다", ["들리다", "보이다", "보다"], "듣다."), M("Which means “to be heard”?", "들리다", ["듣다", "보이다", "보다"], "들리다."), M("Which means “to watch”?", "보다", ["보이다", "듣다", "들리다"], "보다."), M("What does 잘 들립니까 ask?", "Can you hear well?", ["Do you listen well?", "Do you speak well?", "Did you see?"], "들리다."), M("What does 칠판이 잘 보입니까 ask?", "Can you see the chalkboard well?", ["Do you watch the chalkboard?", "Is it big?", "Is it new?"], "보이다."),
           F("멀리서 자동차 소리가 ___. (is heard)", "들립니다", ["듣습니다", "봅니다"], "들리다."), F("왼쪽에 강이 ___. (was seen)", "보였습니다", ["봤습니다", "들렸습니다"], "보이다."), F("무슨 소리가 ___? (is heard)", "들립니까", ["듣습니까", "봅니까"], "들리다."), F("저기 저 산을 한번 ___. (Please look at)", "보세요", ["보이세요", "들으세요"], "보다."), F("내 말을 잘 ___. (Please listen)", "들으세요", ["들리세요", "보세요"], "듣다."),
           read_q("칠판이 잘 보입니까"), read_q("네, 잘 들립니다"), read_q("무슨 소리가 들립니까"), read_q("그때 두 남자가 이웃집에서 나오는 것이 보였어요"), read_q("멀리서 자동차 소리가 들립니다")]
    ),
)

# ================================================================== L8: Activities (Ch 35 Topic B): job hunters article and self-introduction letter
_JH = [("삼 년째 웹디자이너 취업을 준비하는 에이 씨, 스물일곱 살은 올 이 월부터 디자인 취업 전문학원에 다니고 있다.", "A, 27, who has been preparing for a web designer job for three years, has been attending a design job-specialty academy since February this year."), ("구직 기간이 길어지면서 전문가의 도움을 받기로 한 것이다.", "As her job-seeking period grew longer, she decided to get an expert’s help."), ("학원만으로 부족하다고 느껴 그룹과외 수업도 듣고 있다.", "Feeling that the academy alone was not enough, she is also taking group tutoring classes."), ("지금까지 그가 취업 학원과 과외에 쓴 돈은 백이십만 원 남짓.", "The money spent so far on the job academy and tutoring is a little over 1,200,000 won."), ("학원비를 내려고 단기 아르바이트도 뛰고 있다.", "She is also working short-term part-time jobs to pay the academy fees."), ("에이 씨는 대기업에 입사하려면 여전히 스펙이 압도적으로 좋아야 한다며 취업 학원 수강은 사실상 필수라고 전했다.", "A said that to join a large company your “specs” still have to be overwhelmingly good, and that taking a job academy course is in effect a must."), ("배 모 씨, 스물여섯 살은 서울에 있는 대기업에서 일하고 싶어한다.", "Mr./Ms. Bae, 26, wants to work at a large company in Seoul."), ("취업 준비를 하며 학원에 다니느라 카페와 스터디룸에서 주 오 일 아르바이트를 한다며 집에서 도움을 받는 사람들은 편하게 준비를 하는데, 나만 이렇게 힘들다는 생각이 들 때도 많다고 했다.", "Bae said, “Because I attend an academy while preparing for a job, I do a part-time job five days a week at a café and a study room; people who get help from home prepare comfortably, and there are many times when I think that only I have it this hard.”"), ("지난해 팔 월 대학을 졸업한 배 씨는 취업난이 심하다 보니 지원해도 떨어질 것 같다는 이유로 아직까지 입사 서류를 넣어본 적이 없다.", "Bae, who graduated in August last year, has not yet submitted any job application documents, for the reason that “because the job shortage is severe, I think I would fail even if I applied.”"), ("중소기업을 퇴사하고 개발자로 재취업을 준비하는 양 모 씨, 서른한 살은 올해 삼 개월 과정의 실무형 코딩 학원에 참여했다.", "Mr./Ms. Yang, 31, who left a small or medium enterprise and is preparing to be re-employed as a developer, joined a three-month practical coding academy (boot camp) this year."), ("비용은 한 달에 이백만 원씩 총 육백만 원.", "The cost was 2,000,000 won a month, 6,000,000 won in total."), ("양 씨는 취업을 다시 준비하려니 과거보다 훨씬 어려워졌다며 그나마 개발자가 취업에 유리할 것 같아 저축한 돈을 털어 고액 부트캠프를 다니는 중이라고 말했다.", "Yang said that preparing for a job again has become much harder than in the past, and that since developers seem to have an advantage in getting jobs, “I am attending an expensive boot camp, emptying out my savings.”")]
_WORDS2 = [("접수하다", "to receive; to accept"), ("붙다", "to pass (an exam); to stick"), ("학력", "educational background"), ("유리하다", "to be advantageous"), ("뽑다", "to choose; to select"), ("마감하다", "to close; to finish (a deadline)"), ("서류", "documents"), ("대기업", "a large enterprise"), ("구인", "job listing"), ("연봉", "an annual salary"), ("경력", "(work) experience"), ("분야/부문", "a field; a section"), ("게시판", "a bulletin board")]
L8 = lesson(
    "Ch 35 · Topic B activities: three job hunters",
    "취업 학원 · 스펙 · 구직 기간 · 대기업 · 중소기업 · 개발자 · 부트캠프 · 자기소개서 쓰기",
    requires=[],
    cards=[
        card("Activity 2 (Reading): a newspaper article introducing three job hunters",
             "The following newspaper article introduces three job hunters. The book asks you to fill in a table in English for each of A (27), Bae (26) and Yang (31): desired job; preparations for getting a job; means of funding their education. The book glosses 실무형 코딩 학원: practical coding academy (boot camp). The article is the book’s; the ages, money amounts, months and counts are spelled out in Hangul, quotation marks and parentheses are dropped, and the letter A is spelled 에이. The English is mine.",
             examples=passage(_JH)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["", "A (27)", "Bae (26)", "Yang (31)"], [["Desired job", "Web designer", "Work at a large company in Seoul", "Developer"], ["Preparations", "A design job academy since February; group tutoring", "Attends an academy; has not yet submitted any applications", "A three-month practical coding boot camp"], ["Funding", "Short-term part-time jobs", "Part-time job five days a week at a café and a study room", "Savings (six million won in total)"]])]),
        card("Activity 1 (Reading and writing): words to review", "The book gives these words to review (use a dictionary for unknown ones) and asks you to write a short story with at least two of them in each sentence, and then to read the sentences to a partner. The meanings of the Core Vocabulary words are the book’s; the rest are mine.",
             tables=[ktable(_WORDS2)]),
        card("Activity 4 (Writing and speaking): writing a letter of self-introduction (자기소개서 쓰기)",
             "You are looking for a job and want to write a letter introducing yourself as a potential employee. The book asks you to: a. think about your job experiences, personality (strengths and weaknesses), special skills, etc. and fill in a table in English (work experience; school experience; personality [strengths/weaknesses]; special skills; other); b. using this information, think of a job you would like to do; c. in Korean, write a cover letter that includes the reasons you are qualified for the job; d. present your letter to the class, in Korean, and decide which is the most creative."),
        card("Activities left out", "Activity 3 (listening to three narrations by people who joined a job preparation program: a company recruiting guide [취업설명회], a camp for job hunting [취업캠프] and a clinic for job hunting [취업상담 클리닉]) is an audio activity."),
    ],
    exercises=uniq(
        vocab_exercises(_WORDS2)
        + _tr(_JH, k=3)
        + [M("What job is A preparing for?", "Web designer", ["Developer", "Teacher", "Soldier"], "웹디자이너."), M("What does A say about taking an academy course?", "It is in effect a must", ["It is useless", "It is cheap", "It is easy"], "사실상 필수."), M("How does Bae pay for preparation?", "Part-time jobs at a café and study room", ["Savings", "Parents", "A scholarship"], "카페와 스터디룸."), M("Why hasn’t Bae applied yet?", "Thinks he/she would fail anyway", ["No time", "No interest", "No money"], "떨어질 것 같다."), M("What does Yang want to become?", "A developer", ["A designer", "A teacher", "A doctor"], "개발자."), M("What did Yang attend?", "A three-month coding boot camp", ["A design academy", "A language academy", "A cooking class"], "삼 개월 과정."), M("How did Yang pay?", "Savings", ["A loan", "A scholarship", "A company"], "저축한 돈."),
           F("삼 년째 웹디자이너 취업을 ___하는 에이 씨 (preparing)", "준비", ["신청", "접수"], "준비하다."), F("학원비를 내려고 단기 ___도 뛰고 있다. (part-time job)", "아르바이트", ["인턴", "과외"], "아르바이트."), F("스펙이 압도적으로 좋아야 한다며 취업 학원 수강은 사실상 ___라고 전했다. (a must)", "필수", ["부족", "충분"], "필수."), F("취업난이 심하다 보니 지원해도 ___ 것 같다. (would fail)", "떨어질", ["붙을", "뽑힐"], "떨어지다."), F("양 씨는 ___한 돈을 털어 고액 부트캠프를 다니는 중이다. (saved)", "저축", ["투자", "지출"], "저축하다."),
           read_q("취업 학원"), read_q("구직 기간이 길어지면서 전문가의 도움을 받기로 한 것이다"), read_q("취업난이 심하다"), read_q("개발자로 재취업을 준비하는 양 씨"), read_q("자기소개서")]
    ),
)

# ================================================================== L9: Topic C
_C_DLG = [
    ("면접관", "김현민 씨, 대학에서 무엇을 공부하셨습니까?", "Mr. Kim Hyunmin, what did you study at university?"),
    ("현민", "무역학을 전공했습니다.", "I majored in trade."),
    ("면접관", "어떤 외국어를 잘 하십니까?", "What foreign language are you good at?"),
    ("현민", "제가 영어에는 자신이 있습니다. 호주에서 삼 년 동안 공부를 했습니다.", "I am confident in English. I studied in Australia for three years."),
    ("면접관", "저희 회사에 지원하신 동기가 무엇입니까?", "What was your motive for applying to our company?"),
    ("현민", "이 회사가 다국적기업이기 때문에 제 전공과 특기에 잘 맞는다고 생각했습니다.", "Because this company is a multinational corporation, I thought it suited my major and specialty well."),
    ("면접관", "네. 자신의 장점과 단점은 무엇이라고 생각하십니까?", "I see. What do you think your strengths and weaknesses are?"),
    ("현민", "새로운 환경에 잘 적응하는 것이 제 장점입니다. 단점은 성격이 너무 철저하다는 점입니다.", "Adapting well to a new environment is my strength. My weakness is that my personality is too thorough."),
    ("면접관", "김현민 씨, 오늘 감사합니다. 노력하신 만큼 좋은 결과 있기를 바랍니다.", "Mr. Kim Hyunmin, thank you for today. I hope you get good results to the extent that you have made an effort."),
]
_C_WORDS = ["개발", "개별적으로", "기회", "다국적", "단점", "동기", "면접관", "무역학", "새롭다", "자신", "자신(감)", "장점", "적응", "철저하다", "해외", "호주"]
_TIPS = [("기업들이 면접에서 중요하게 생각하는 것은 지원자의 사회성과 업무 적응력이다.", "What companies consider important in interviews is the applicant’s sociability and ability to adapt to work."), ("인사담당자들은 면접을 잘 보면 필기시험을 좀 못 봐도 입사할 수 있지만 면접에서 떨어지면 학점이나 성적이 좋아도 채용되기 어렵다고 말한다.", "Personnel managers say that if you do well in the interview you can join the company even if you do a little poorly on the written test, but if you fail the interview it is hard to be hired even with good credits or grades."), ("면접관은 응시자를 봤을 때 첫인상에 크게 영향을 받는다고 한다.", "It is said that interviewers are greatly influenced by the first impression when they see an applicant."), ("그렇기 때문에 면접에서 좋은 점수를 얻기 위해서는 솔직하고 적극적이어야 한다.", "Therefore, to get a good score in an interview you have to be honest and proactive."), ("적극성은 그 회사에서 열심히 일하고 싶다는 생각을 충분히 표현하면 된다.", "As for proactiveness, it is enough to express fully your wish to work hard at that company."), ("예를 들어 퇴근시간이 됐는데 상사가 일을 시키면 어떻게 하겠느냐는 질문을 했을 때 가정도 중요하니 퇴근하겠다는 답보다는 필요한 일이라면 야근을 하겠다는 답을 면접관은 더 좋아한다.", "For example, when asked “What will you do if your boss gives you work when it is time to leave?”, interviewers like the answer “If it is necessary work, I will work overtime” more than the answer “Family is important too, so I will leave.”"), ("또한 대답을 할 때 자신의 경험을 예로 들어서 이야기하면 면접관에게 깊은 인상을 줄 수 있다.", "Also, when answering, if you give your own experience as an example, you can leave a deep impression on the interviewer."), ("전공분야에 대한 질문을 받았을 때는 쉬운 단어로 다른 사람들이 이해할 수 있도록 얘기할 수 있어야 한다.", "When asked about your major field, you should be able to speak in easy words so that other people can understand."), ("그리고 면접시험을 보기 전에 그 회사에 먼저 입사한 선배에게 미리 지원 기업에 대해 알아보는 것도 중요하다.", "And before taking the interview, it is also important to find out in advance about the company you applied to from a senior who joined that company earlier.")]
L9 = lesson(
    "Ch 35 · Topic C: Why did you apply to our company? (저희 회사에 지원한 동기가 무엇입니까?)",
    "저희 회사에 지원한 동기가 무엇입니까 · 면접 · 무역학 · 다국적기업 · 장점과 단점 · 적응 · 면접 요령",
    requires=[],
    cards=[
        card("Topic C: Why did you apply to our company? (저희 회사에 지원한 동기가 무엇입니까?)",
             "A college graduate is being interviewed by two people for a position at a trading company. (The two interviewers are both labelled 면접관 here; the book labels them 면접관1 and 면접관2. The English is mine; the book gives none.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 개발(하다/되다) and 적응(하다/되다) take the forms in parentheses; –고 생각하다 and an attributive form + 만큼 are explained in the grammar.",
             tables=[ktable(_rows([w for w in _C_WORDS if _HG(w) and "(" not in w])), table(["Word", "Meaning"], [["자신(감)", "self-confidence; “self-believing feeling”"], ["–고 생각하다", "to think that …"], ["an attributive form + 만큼", "as … as"]])]),
        card("Follow-up 2 (Reading): tips for preparing for a job interview",
             "The following article offers tips for preparing for a job interview. The book asks you to: 1. make an appropriate title for the article in Korean; 2. write the gist of each of four tips in English; 3. add one or two tips of your own and present them to the class. The article is the book’s (the quotation marks are dropped); the English is mine.",
             examples=passage(_TIPS)),
        card("The four tips, summarized (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Tip", "Gist (mine)"], [["1", "The interview matters most: companies value sociability and the ability to adapt to work, so a good interview can outweigh a weak written test"], ["2", "The first impression counts, so be honest and proactive, and show you want to work hard (for example, be willing to work overtime if necessary)"], ["3", "Give your own experience as an example when you answer"], ["4", "Explain your major in easy words and find out about the company beforehand from a senior who joined it"]])]),
        card("Activities left out", "Follow-up 1 (listening to a portion of a job interview and filling in college major, reason for applying, specialty and strength, and weakness), the Topic Presentation C study steps (SMART Board and role-reading as interviewer and applicant) and Follow-up 2’s title-making and tip-adding activities are audio, computer and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG) + _TIPS, k=3)
        + [M("What did 김현민 study?", "Trade", ["Business", "Law", "Computer science"], "무역학."), M("What foreign language is he good at?", "English", ["Japanese", "Chinese", "French"], "영어."), M("Where did he study for three years?", "Australia", ["America", "Canada", "England"], "호주."), M("Why did he apply to this company?", "It is a multinational company that suits his major and specialty", ["It pays a lot", "It is near his home", "His friend works there"], "다국적기업."), M("What is his strength?", "Adapting well to new environments", ["Speaking fast", "Being tall", "Singing"], "새로운 환경에 잘 적응하는 것."), M("What is his weakness?", "He is too thorough", ["He is shy", "He is late", "He is lazy"], "성격이 너무 철저하다."), M("According to the article, what matters most to companies in an interview?", "Sociability and ability to adapt to work", ["Looks", "Age", "Hobbies"], "사회성과 업무 적응력."), M("Which answer do interviewers prefer?", "I will work overtime if it is necessary", ["Family is important so I will leave", "I do not know", "I will ask my boss"], "필요한 일이라면 야근을 하겠다."),
           F("저희 회사에 지원하신 ___가 무엇입니까? (motive)", "동기", ["기회", "단점"], "동기."), F("이 회사가 ___기업이기 때문에 제 전공과 특기에 잘 맞는다고 생각했습니다. (multinational)", "다국적", ["중소", "대"], "다국적."), F("새로운 환경에 잘 ___하는 것이 제 장점입니다. (adapting)", "적응", ["개발", "채용"], "적응하다."), F("제가 영어에는 ___이 있습니다. (confidence)", "자신", ["자신감을", "단점"], "자신이 있다."), F("면접에서 좋은 점수를 얻기 위해서는 ___하고 적극적이어야 한다. (honest)", "솔직", ["철저", "유용"], "솔직하다."),
           read_q("저희 회사에 지원한 동기가 무엇입니까"), read_q("무역학을 전공했습니다"), read_q("제가 영어에는 자신이 있습니다"), read_q("새로운 환경에 잘 적응하는 것이 제 장점입니다"), read_q("노력하신 만큼 좋은 결과 있기를 바랍니다")]
    ),
)

# ================================================================== L10: Grammar C: 만큼
_MG1 = [("나는 마이클 만큼 많이 먹어요.", "I eat as much as Michael (does)."), ("어제 먹은 만큼 많이 먹으세요.", "Please eat as much as you ate yesterday.")]
_MG2 = [("할 수 있을 만큼 하세요.", "Please do as much as you can."), ("이 뷔페에서는 먹고 싶은 만큼 먹어도 돼요.", "At this buffet, you can eat as much as you want (to eat)."), ("성적이 기대한 만큼 안 좋아요.", "The grade is not as good as I expected."), ("그 경기장은 팔천 명이 들어갈 만큼 큽니다.", "The stadium is “as big as 8,000 can enter.” / The stadium is big enough to hold 8,000.")]
_MGM = [("열심히 일하는 만큼", "to the extent that you work hard"), ("열심히 일하는 만큼 승진 기회도 있을 겁니다.", "To the extent that you work hard, there will also be a chance of promotion.")]
_MGF = [("먹다", "to eat", "먹은 만큼 / 먹는 만큼 / 먹을 만큼"), ("하다", "to do", "한 만큼 / 하는 만큼 / 할 만큼"), ("기대하다", "to expect", "기대한 만큼 / 기대하는 만큼 / 기대할 만큼"), ("노력하다", "to make an effort", "노력한 만큼 / 노력하는 만큼 / 노력할 만큼"), ("일하다", "to work", "일한 만큼 / 일하는 만큼 / 일할 만큼"), ("크다", "to be big", "큰 만큼 / 클 만큼")]
L10 = lesson(
    "Ch 35 · Grammar C: expansion of 만큼, an attributive form + 만큼",
    "만큼 · 먹은 만큼 · 할 수 있을 만큼 · 먹고 싶은 만큼 · 기대한 만큼 · 들어갈 만큼",
    requires=[],
    cards=[
        card("As … as: a noun or a clause before 만큼",
             "Look at the English sentences to see what can follow the word as: “I eat as much as Michael (does).” and “Please eat as much as you ate yesterday.” Note that as can be followed by a noun (as in the first sentence) or by a clause (as in the second sentence). Likewise, 만큼, which is the Korean counterpart you learned about in Chapter 18, can be preceded by a noun or clause (the English is the book’s):",
             examples=passage(_MG1)),
        card("The attributive form", "When a clause precedes 만큼, however, the verb of the clause has to be in the attributive form. The following examples show how 만큼 is preceded by a clause (the English is the book’s):", examples=passage(_MG2)),
        card("Forms (mine)", "Past attributive (-(으)ㄴ), present attributive (-는) or future attributive (-(으)ㄹ) + 만큼; an adjective takes -(으)ㄴ or -(으)ㄹ.", tables=[table(["Verb", "Meaning", "Forms with 만큼"], [list(r) for r in _MGF], say=[0, 2])]),
        card("Follow-up 1 (Speaking and listening): the model", "In pairs, Partner A picks an unshaded card and conjugates the verb out loud, using 만큼; Partner B picks a shaded card and combines it with what A said. The book’s model (the English is mine):", examples=dlg([("A", _MGM[0][0], _MGM[0][1]), ("B", _MGM[1][0], _MGM[1][1])])),
        card("Activities left out", "The cards and Follow-up 2 (listening to four dialogs and translating the sentence with an attributive form + 만큼) need cards, audio and a partner."),
    ],
    exercises=uniq(
        _tr(_MG1 + _MG2 + _MGM, k=3)
        + [M("What must the verb before 만큼 be in when a clause precedes it?", "The attributive form", ["The blunt form", "The honorific form", "The causative form"], "The book’s note."), M("What does 할 수 있을 만큼 하세요 mean?", "Please do as much as you can", ["Please do nothing", "Please do it once", "Please be quiet"], "The book’s example."), M("What does 먹고 싶은 만큼 먹어도 돼요 mean?", "You can eat as much as you want", ["You cannot eat", "You must eat everything", "You ate too much"], "The book’s example."), M("What does 기대한 만큼 안 좋아요 mean?", "It is not as good as I expected", ["It is better than I expected", "I did not expect", "It is very good"], "The book’s example."), M("What does 팔천 명이 들어갈 만큼 크다 mean?", "It is big enough to hold 8,000", ["It is small", "It has no room", "It is new"], "The book’s example."),
           F("어제 ___ 만큼 많이 먹으세요. (ate)", "먹은", ["먹는", "먹을"], "past attributive."), F("할 수 있을 ___ 하세요. (as much as)", "만큼", ["처럼", "같이"], "만큼."), F("먹고 ___ 만큼 먹어도 돼요. (want to)", "싶은", ["싶을", "싶어"], "싶은 만큼."), F("성적이 ___ 만큼 안 좋아요. (expected)", "기대한", ["기대하는", "기대해"], "기대한 만큼."), F("노력하신 ___ 좋은 결과 있기를 바랍니다. (as much as)", "만큼", ["처럼", "같이"], "만큼."),
           read_q("나는 마이클 만큼 많이 먹어요"), read_q("어제 먹은 만큼 많이 먹으세요"), read_q("할 수 있을 만큼 하세요"), read_q("먹고 싶은 만큼 먹어도 돼요"), read_q("성적이 기대한 만큼 안 좋아요")]
    ),
)

# ================================================================== L11: Grammar D: -다고
_DG1 = [("한국말이 재미있어요.", "Korean is fun."), ("한국말이 재미있다.", "(change the verb ending to the blunt formal form)"), ("한국말이 재미있다고", "(add the “object marker” 고)")]
_DG2 = [("저는 한국말이 재미있다고 생각해요.", "I think [that] Korean is fun."), ("저는 한국말이 재미있다고 믿어요.", "I believe [that] Korean is fun.")]
_DG3 = [("그 여자가 학생이라고 생각해요.", "I think [that] the woman is a student."), ("그 여자가 학생이 아니라고 생각해요.", "I think [that] the woman is not a student.")]
_DG4 = [("시험이 지난 주에 끝났다고 알고 있어요.", "I know [that] the exam was over last week."), ("철호가 여섯 시까지 집에 오겠다고 약속했어요.", "Cholho promised [that] he would come home by six."), ("서진이는 좋은 친구라고 생각해요.", "I think [that] Seojin is a good friend.")]
_DGM = [("한국말이 쉬워요.", "Korean is easy."), ("한국말이 쉽다고 생각해요.", "I think Korean is easy.")]
_DGK = [("박 이병, 한국에 대해 어떻게 생각해요?", "Private Park, what do you think about Korea?"), ("저는 한국 사람들이 친절하다고 생각해요.", "I think Korean people are kind."), ("박 이병은 한국 사람들이 친절하다고 했습니다. 그리고 문 일병은 한국 드라마가 너무 재미있다고 했습니다.", "Private Park said that Korean people are kind. And Private First Class Moon said that Korean dramas are very interesting.")]
_DGP = [("재미있어요", "재미있다고"), ("쉬워요", "쉽다고"), ("끝났어요", "끝났다고"), ("오겠어요", "오겠다고"), ("좋아요", "좋다고"), ("학생이에요", "학생이라고"), ("학생이 아니에요", "학생이 아니라고"), ("친절해요", "친절하다고")]
L11 = lesson(
    "Ch 35 · Grammar D: expressing a statement as an object, –다고",
    "-다고 · 재미있다고 생각해요 · 학생이라고 · 아니라고 · 끝났다고 알고 있어요 · 오겠다고 약속했어요",
    requires=[],
    cards=[
        card("A statement as the object of a sentence",
             "In Korean, when a statement (in contrast to a command or question) becomes the object in a sentence, it goes through some “cosmetic” changes. First, the verb ending of the statement changes to the blunt formal form –다. Then 고, which functions as an object marker, is attached to the statement. For example (the English is the book’s):",
             examples=passage(_DG1)),
        card("The new statement as an object", "This new statement can then be used as the object in a sentence (the English is the book’s):", examples=passage(_DG2)),
        card("The note", "Thus, when a statement ends with –다고, you can tell it is the object of the sentence. (Recall –다고 하다 from Chapter 23. –다고 in –다고 하다 is the same as what you are learning here.)"),
        card("이다 and 아니다",
             "When a declarative sentence with the verb 이다 or 아니다 becomes an object, however, ~이다고 and ~이/가 아니다고 change to ~이라고 and ~이/가 아니라고, respectively (the English is the book’s):",
             examples=passage(_DG3)),
        card("More examples", "The following examples show more instances in which a statement is used as an object (the English is the book’s; 6시 is spelled out):", examples=passage(_DG4)),
        card("Forms (mine)", "Statement (polite) → blunt form + 고.", tables=[table(["Statement", "As an object"], [list(r) for r in _DGP], say=[0, 1])]),
        card("Follow-up 3 (Speaking and listening): the model", "In pairs, one partner reads a sentence from a list and the other changes it to a dependent clause with –다고/라고. The book’s model (the English is mine):", examples=dlg([("A", _DGM[0][0], _DGM[0][1]), ("B", _DGM[1][0], _DGM[1][1])])),
        card("Follow-up 5 (Writing and speaking): 한국 사람들이 친절하다고 생각해요", "You jot down your thoughts about Korea (its people, food, language, etc.) in English, discuss them with classmates using –다고/라고 + a main verb, then report the most interesting idea to the class using –다고/라고 (말)하다. The book’s models (the English is mine):", examples=dlg([("A", _DGK[0][0], _DGK[0][1]), ("B", _DGK[1][0], _DGK[1][1])]) + passage([_DGK[2]])),
        card("Activities left out", "The sentence lists and Follow-up 4 (listening to four short dialogs in which two college friends discuss their school lives, and identifying and translating the sentence with –다고) need lists, audio and a partner."),
    ],
    exercises=uniq(
        _tr(_DG2 + _DG3 + _DG4 + _DGK[1:] , k=3)
        + [M("What happens to the verb ending when a statement becomes an object?", "It changes to the blunt formal form –다, then 고 is attached", ["It becomes –요", "It becomes –겠", "Nothing"], "The book’s note."), M("What does 고 function as here?", "An object marker", ["A subject marker", "A time marker", "A place marker"], "The book’s note."), M("What do ~이다고 and ~이/가 아니다고 change to?", "~이라고 and ~이/가 아니라고", ["~이다 and ~아니다", "~이고 and ~아니고", "~이니까 and ~아니니까"], "The book’s note."), M("What does 저는 한국말이 재미있다고 생각해요 mean?", "I think that Korean is fun", ["I speak Korean", "I studied Korean", "I teach Korean"], "–다고 생각하다."), M("What does 철호가 여섯 시까지 집에 오겠다고 약속했어요 mean?", "Cholho promised to come home by six", ["Cholho came home at six", "Cholho left at six", "Cholho forgot"], "–다고 약속하다."),
           F("한국말이 재미있___ 생각해요. (-다고)", "다고", ["는다고", "어요"], "재미있다고."), F("그 여자가 학생___ 생각해요. (that she is a student)", "이라고", ["이다고", "이고"], "학생이라고."), F("그 여자가 학생이 ___ 생각해요. (is not)", "아니라고", ["아니다고", "아니고"], "아니라고."), F("시험이 지난 주에 끝났___ 알고 있어요. (-다고)", "다고", ["는다고", "고"], "끝났다고."), F("서진이는 좋은 친구___ 생각해요. (that he is a good friend)", "라고", ["다고", "이다고"], "친구라고."),
           read_q("저는 한국말이 재미있다고 생각해요"), read_q("그 여자가 학생이라고 생각해요"), read_q("시험이 지난 주에 끝났다고 알고 있어요"), read_q("철호가 여섯 시까지 집에 오겠다고 약속했어요"), read_q("저는 한국 사람들이 친절하다고 생각해요")]
    ),
)

# ================================================================== L12: Activities of Topic C
_IV = [("기업에 대한 정보를 조사하여 궁금한 점을 질문하는 지원자", "A", "An applicant who researches information about the company and asks questions about what he/she is curious about"), ("질문을 받으면 너무 길지 않고 간단하게 대답하는 지원자", "A", "An applicant who, when asked a question, answers simply without being too long"), ("면접에 어울리지 않는 복장이나 액세서리를 한 지원자", "B", "An applicant wearing clothes or accessories unsuitable for an interview"), ("이력서에 쓴 내용과 아주 다른 인상을 주는 지원자", "B", "An applicant who gives an impression very different from what is written on the resume"), ("면접할 때 자신감이 없는 지원자", "B", "An applicant who has no self-confidence during the interview"), ("면접 전에 미리 도착하여 면접을 준비하는 지원자", "A", "An applicant who arrives in advance before the interview and prepares for it"), ("채용 기업에 대한 정보가 부족하고 면접 준비가 안 된 지원자", "B", "An applicant who lacks information about the hiring company and is not prepared for the interview"), ("면접 시간에 늦게 도착하는 지원자", "B", "An applicant who arrives late for the interview time"), ("모르는 질문에 솔직하게 모른다고 대답하는 지원자", "A", "An applicant who honestly answers “I don’t know” to a question he/she doesn’t know"), ("일어나서 면접관에게 인사하는 지원자", "A", "An applicant who stands up and greets the interviewer")]
_STW = [("호주", "Australia"), ("자신감", "self-confidence"), ("다국적", "multinational"), ("태도", "an attitude"), ("동기", "a motive"), ("통보하다", "to notify; to inform"), ("단점", "a weak point"), ("새롭다", "to be new"), ("인재", "a talented person"), ("남", "another person; others"), ("본인", "oneself; the person himself/herself"), ("진출하다", "to advance into; to enter"), ("개별", "an individual; separate"), ("장점", "a strength"), ("개발하다", "to develop"), ("적응하다", "to adapt oneself to"), ("남기다", "to leave (behind)"), ("연봉", "an annual salary"), ("기회", "an opportunity"), ("거절하다", "to refuse; to decline")]
L12 = lesson(
    "Ch 35 · Topic C activities: what interviewers prefer",
    "면접 지원자 · 선호하는 지원자 · 선호하지 않는 지원자 · 일어나서 인사하다 · 늦게 도착하다 · 자신감이 없다",
    requires=[],
    cards=[
        card("Activity 3 (Reading): preferred and non-preferred interviewees",
             "You will complete some tasks related to ranking job interviewees and then read an article describing the actual ranking. The book gives ten descriptions of interviewees and asks you to decide whether each belongs to Group A (preferred interviewees) or Group B (non-preferred interviewees), to write the English meaning of each in the right table, to rank each group from 1 to 5 with a partner and then to compare it with the actual ranking in the article (the article is not in the text I have). The grouping and the English are mine.",
             tables=[table(["Description", "Group (mine)", "English (mine)"], [list(r) for r in _IV], say=[0])]),
        card("Activity 1 (Writing): let’s make a short story", "The book gives the words below to review (use a dictionary for unknown ones); in pairs you create a short story with at least fifteen of them, post it on the classroom wall, and read and correct the other pairs’ stories with a different colored pen. The meanings of the Core Vocabulary words are the book’s; the rest are mine.",
             tables=[ktable(_STW)]),
        card("Activities left out", "Activity 2 (listening to three conversations from a job interview and filling in the reason for applying, strengths/weaknesses and the interviewee’s question; the book glosses 집중하다: to concentrate) and Activity 4 (회사에서 일한 경력이 있습니까?, an interview role-play in which you write key words about qualifications, previous job experience, reason for applying, strengths/weaknesses and other interview questions on an index card) are audio and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_STW)
        + [M("Is this a preferred (A) or non-preferred (B) interviewee: “" + c[:60] + "”?", "Group " + b, ["Group " + ("B" if b == "A" else "A")], "My grouping.") for a, b, c in _IV]
        + [F("면접 시간에 ___ 도착하는 지원자는 좋아하지 않는다. (late)", "늦게", ["일찍", "미리"], "늦게."), F("면접 전에 ___ 도착하여 면접을 준비하는 지원자가 좋다. (in advance)", "미리", ["늦게", "갑자기"], "미리."), F("모르는 질문에 ___하게 모른다고 대답하는 지원자가 좋다. (honestly)", "솔직", ["철저", "충분"], "솔직하다."), F("면접할 때 ___이 없는 지원자는 좋지 않다. (self-confidence)", "자신감", ["경력", "기회"], "자신감."), F("일어나서 면접관에게 ___하는 지원자가 좋다. (greets)", "인사", ["질문", "대답"], "인사하다."),
           read_q("면접 시간에 늦게 도착하는 지원자"), read_q("일어나서 면접관에게 인사하는 지원자"), read_q("면접할 때 자신감이 없는 지원자"), read_q("모르는 질문에 솔직하게 모른다고 대답하는 지원자"), read_q("면접 전에 미리 도착하여 면접을 준비하는 지원자")]
    ),
)

# ================================================================== L13: core vocabulary and self-evaluation
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Loan words", _CV_LOAN), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L13 = lesson(
    "Ch 35 · Core vocabulary and self-evaluation",
    "주요 단어 · 직장 구하기 · 이력서 · 채용 · 면접 · 장점 · 단점 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: ask about and discuss information related to job hunting; state how job hunters in Korea usually prepare for employment; and answer general questions at a job interview.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; the passive infixes 이, 히, 리, and 기; the passive verbs 보이다 and 들리다; an attributive form + 만큼; –다고 for a statement used as the object in a sentence; and the Sino-Korean syllables within 하반기 (下半期), 구직 (求職), and 면접 (面接)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 우대 mean?", "preferential treatment", ["a fair", "a resume", "a motive"], "優待."), M("What does 채용 mean?", "employment; hiring; recruitment", ["submission", "participation", "receipt"], "採用."), M("What does 경력 mean?", "(work) experience", ["a wage", "an opportunity", "a hope"], "經歷."), M("What does 임금 mean?", "wage; pay", ["experience", "a field", "personnel"], "賃金."), M("What does 단점 mean?", "a weak point; shortcoming", ["a strength", "a motive", "a field"], "短點."), M("What does 장점 mean?", "a merit; a strength", ["a weak point", "a motive", "a field"], "長點."), M("What does 면접관 mean?", "an interviewer", ["an applicant", "a counselor", "a boss"], "面接官."),
           F("취직을 하려고 여러 곳에 ___를 냈어요. (resume)", "이력서", ["지원서", "박람회"], "이력서."), F("올 ___에는 대기업에서 신입사원을 많이 채용할 계획입니다. (second half)", "하반기", ["상반기", "학력"], "하반기."), F("서류 ___은 통과했지만 면접에서 떨어졌어요. (screening)", "전형", ["제출", "접수"], "서류 전형."), F("새로운 환경에 ___하는 것은 쉽지 않아요. (adapting)", "적응", ["개발", "채용"], "적응."), F("호주의 ___는 캔버라입니다. (capital)", "수도", ["동기", "기회"], "호주의 수도."),
           read_q("주요 단어"), read_q("직장 구하기"), read_q("자기소개서"), read_q("면접관"), read_q("다국적")]
    ),
)

UNIT = unit("Semester 2 · Unit 9 · Chapter 35: Job Hunting (직장 구하기)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])

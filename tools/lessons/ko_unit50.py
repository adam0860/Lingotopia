"""Unit 50: KBC Semester 2, Unit 11, Chapter 43 - Religion and Society (종교와 사회).
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

# ---- the core vocabulary of Chapter 43 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("개신교", "(改新敎) Protestantism; “newly reformed church”", "미국에는 개신교 신자들이 많습니다."),
    ("격주", "(隔週) every other week; biweekly", "김 선생님은 한 달에 두 번, 격주로 절에 갑니다."),
    ("고아원", "(孤兒院) an orphanage; “lone child place”", "주말에 고아원을 방문해서 아이들에게 공부를 도와주었습니다."),
    ("교회", "(敎會) a (Christian) church; a chapel", "크리스마스 때 교회에서 다양한 행사를 해요."),
    ("기도(하다/드리다)", "(祈禱) a prayer (to pray) (~하다/드리다)", "교회에 가서 가족을 위해 기도했습니다."),
    ("기독교", "(基督敎) Christianity", "기독교가 한국에 언제 들어왔습니까?"),
    ("기부(하다)", "(寄附) donation (of money or items) (to donate) (~하다)", "고아원에 있는 아이들을 위해 백만 원을 기부했습니다."),
    ("기타", "(其他) and others; etc.", "한국인 중에서 유교 등 기타 종교를 가진 사람들은 얼마나 됩니까?"),
    ("무속신앙/샤머니즘", "(巫俗信仰) shamanism", "무속신앙은 오랫동안 한국인들의 생활과 문화에 영향을 주었습니다."),
    ("믿다", "to believe; to trust; to believe in", "믿었던 친구가 나한테 거짓말을 했어요."),
    ("바람직하다", "to be desirable; to be advisable", "자원봉사자가 많은 것은 바람직한 일입니다."),
    ("복지", "(福祉) welfare", "연말에 양로원, 고아원 등의 복지시설을 방문할 계획입니다."),
    ("석가탄신일", "(釋迦誕辰日) Buddha’s birthday; “Sakyamuni birthday”", "부처님오신날을 석가탄신일이라고도 합니다."),
    ("성당", "(聖堂) a Catholic church; a cathedral; “holy house”", "지난 크리스마스 때 성당에서 특별 행사가 열렸어요."),
    ("성탄절", "(聖誕節) Christmas; “holy birth day”", "성탄절 때 어려운 이웃을 돕기 위해 모금을 했습니다."),
    ("신자", "(信者) a believer", "최근에 여러 종교의 신자들이 함께 모임을 가졌습니다."),
    ("양로원", "(養老院) a nursing home; “nurturing elderly place”", "이번 주말에 양로원을 방문해서 할아버지, 할머니들과 시간을 보낼 거예요."),
    ("유교", "(儒敎) Confucianism", "한국 사회는 전통적으로 유교의 영향을 많이 받았습니다."),
    ("의미(있다)", "(意味) meaning (to be meaningful) (~있다)", "자원봉사 활동은 아주 의미 있는 일입니다."),
    ("이슬람교/회교", "(回敎) Islam", "사우디아라비아에는 이슬람교 신자들이 많습니다."),
    ("자선", "(慈善) charity; almsgiving", "연말에는 여러 종교 단체들이 자선 행사를 많이 엽니다."),
    ("장애인", "(障碍人) a disabled person", "여기는 장애인 전용 주차장입니다."),
    ("종교", "(宗敎) religion", "한국인들이 많이 믿는 종교는 무엇입니까?"),
    ("천주교/가톨릭(교)", "(天主敎) Roman Catholicism", "저희 어머니는 천주교 신자라서 일요일마다 성당에 가십니다."),
]
_CV_B = [
    ("근로자", "(勤勞者) a worker; a laborer", "최근 한국에 외국인 근로자가 늘어나고 있습니다."),
    ("남", "another (person); other people", "나보다 남을 먼저 생각하면서 살고 싶어요."),
    ("대륙", "(大陸) a continent; “big land”", "한국은 아시아 대륙에 있습니다."),
    ("대만", "(臺灣) Taiwan", "대만은 중국의 남쪽, 한국의 남서쪽에 있는 작은 섬나라입니다."),
    ("대하다", "(對) to treat (a person)", "이웃 사람들이 따뜻하게 대해 줘서 좋아요."),
    ("모국어", "(母國語) mother tongue; native language; “mother country language”", "모국어와 달리 외국어는 배우기가 아주 힘들어요."),
    ("문법", "(文法) grammar; “letter rule”", "한국 사람에게 영어 문법은 너무 어려워요."),
    ("서투르다/서툴다", "to be unskillful; to be clumsy", "운전을 배운 지 얼마 안 돼서 아직 운전이 서툴러요."),
    ("아프리카", "Africa", "아프리카에는 다양한 동물들이 많이 살아요."),
    ("어색하다", "(語塞) to be awkward", "수업시간에 외국어로 자기소개를 했는데 좀 어색했어요."),
    ("언어", "(言語) (a) language", "외국에 가면 언어와 문화가 달라서 적응하기가 힘들어요."),
    ("오해", "(誤解) misunderstanding; “misinterpretation” (to misunderstand/to be misunderstood) (~하다/받다)", "저 사람을 김 일병 부인으로 오해했어요."),
    ("완벽", "(完璧) perfection (to be perfect) (~하다)", "김 선생님의 피아노 연주는 완벽합니다."),
    ("유럽/구라파", "Europe", "유럽여행을 가면 프랑스와 이탈리아에 꼭 가 보고 싶어요."),
    ("유창하다", "(流暢) to be fluent; to be eloquent", "외국어를 유창하게 하려면 어떻게 해야 합니까?"),
    ("의사소통", "(意思疎通) communication (to communicate/to be communicated) (~하다/되다)", "외국에 여행을 가면 의사소통이 안 돼서 불편해요."),
    ("의존", "(依存) reliance; dependence (to depend upon; to rely on) (~하다)", "성인이 된 다음에는 부모님께 너무 의존하지 마세요."),
    ("중남미", "(中南美) Central and South America", "중남미 지역에 폭우가 많이 내려서 피해가 큽니다."),
    ("중동", "(中東) Middle East", "중동 지역에서 기름이 많이 나옵니다."),
    ("태국", "(泰國) Thailand", "주말에 태국 식당에 갔었는데 음식이 아주 맛있었어요."),
    ("통하다", "(通) to understand each other; “flow freely (both ways)”", "제 동생과 저는 말이 잘 통해서 아주 친해요."),
    ("풍습", "(風習) manners and customs; practices", "우리의 전통과 풍습을 잘 지킵시다."),
]
_CV_C = [
    ("가사", "(家事) household affairs; housework", "그 동안 가사를 돌보느라고 바빴어요."),
    ("검사", "(檢事) a prosecutor", "제 동생이 법대를 졸업하고 검사가 되었어요."),
    ("과거", "(過去) the past", "과거에 있었던 일은 다 잊고 행복한 미래를 생각하세요."),
    ("교육원", "(敎育院) an academy; an educational center", "우리 교육원에서는 다음 달부터 중국어 회화반을 시작합니다."),
    ("글", "writing", "어렸을 때부터 글 쓰는 것을 좋아했어요."),
    ("꿈", "a dream; an aspiration (to have a dream; to dream) (~꾸다)", "제 꿈은 아픈 사람들을 돌보는 의사가 되는 거예요."),
    ("노동", "(勞動) labor; work", "요즘 젊은 부부들은 가사 노동을 나누어서 합니다."),
    ("도전", "(挑戰) a challenge (to challenge; to take on [a challenge]) (~하다)", "요즘 많은 여성들이 새로운 분야에 도전하고 있습니다."),
    ("발전", "(發展) development; expansion; extension; growth (to develop/to be developed) (~하다/되다)", "많은 사람들이 자기 발전을 위해 퇴근 후에 외국어 학원에 다닙니다."),
    ("선호", "(選好) preference (to prefer/to be preferred) (~하다/되다)", "요즘 대학생들이 선호하는 직업은 공무원입니다."),
    ("양육", "(養育) upbringing; raising (to bring up; to raise) (~하다)", "자녀 양육은 여성들만의 일이 아닙니다."),
    ("엔지니어", "an engineer", "올해 우리 회사에서는 다섯 명의 컴퓨터 엔지니어를 채용할 예정입니다."),
    ("역할", "(役割) a role", "가정에서 부모의 역할이 아주 중요합니다."),
    ("작가", "(作家) a writer; an author", "감동적인 드라마를 쓰는 작가가 되고 싶어요."),
    ("조종사", "(操縱士) a pilot; an operator", "비행기 조종사가 되려면 어떻게 해야 해요?"),
    ("지위", "(地位) status", "현대 사회에서 여성들의 지위가 높아지고 있다."),
    ("~직", "(職) a job; a position", "요즘 전문직 여성들이 늘고 있다."),
    ("진출", "(進出) advance; entry; (to advance; to enter; to go [out] into) (~하다)", "사회에 진출하려는 여성들이 많아지고 있다."),
    ("진학", "(進學) advancing (to a higher level of education/institution); “advancing to school” (to advance) (~하다)", "대학을 졸업하고 대학원에 진학하기로 결심했어요."),
    ("판사", "(判事) a judge", "이 사건을 담당하는 판사가 누구인지 잘 아세요?"),
    ("현재", "(現在) the present", "김 박사님은 현재 서울 의대 교수이면서 미래연구소장이십니다."),
]
_CV_GR = [
    ("–곤 하다", "auxiliary verb that expresses common or routine occurrences of an action/event", "주말에는 영화를 보러 가곤 해요. 어렸을 때 자주 피아노를 치곤 했어요."),
    ("~ (도)중에/(–는/던) (도)중에", "in the middle of doing something", "회의 중에 전화가 와서 못 받았어요. 다른 사람이 말하는 도중에 말을 시작하지 마세요."),
    ("반면(에)/–(으)ㄴ/는 반면(에)", "on the other hand; whereas", "한국의 여름은 덥다. 반면에 겨울은 춥다. 남자 농구는 계속 이긴 반면에 여자 농구는 계속 졌다."),
    ("–(으)ㄴ/는데요", "an informal sentence ending", "오늘 날씨가 너무 좋은데요."),
]
_CV_SINO = [("대륙", "(大陸) a continent", "대위, 대로, 대장, 육군, 육지, 육로"), ("전문직", "(專門職) a professional job", "전공, 부전공, 전용, 대문, 정문, 창문, 사무직, 계약직, 직업"), ("천주교", "(天主敎) Roman Catholicism", "천국, 천체, 천문학, 주인, 주연, 주제, 종교, 무교, 교회")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"기도하다": "to pray", "천주교": "Roman Catholicism", "이슬람교": "Islam", "기부": "donation of money or items", "유럽": "Europe", "서투르다": "to be unskillful; to be clumsy"}
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
_S1G = [("천문학", "astronomy; “study of the sky”"), ("천국", "heaven; paradise; the kingdom of heaven"), ("천하", "the world; the whole country; “below the heavens”"), ("천사", "an angel; “heavenly messenger”"), ("천지", "heaven and earth; the world"), ("주인", "the master (of a house); the head (of a family); “master person”"), ("주일", "the Sabbath; the Lord’s day; Sunday"), ("주객", "host and guest"), ("주권", "sovereignty; sovereign power; “lord rights”"), ("주목적", "a leading motive; a main purpose"), ("주력 부대", "main force units"), ("주장", "the captain (of a team); “main commander”"), ("교사", "a teacher; a schoolteacher"), ("교과서", "a textbook; “teaching type book”"), ("불교", "Buddhism; “Buddhist religion”"), ("무교", "having no religion; irreligious"), ("기독교", "Christianity; the Christian religion")]
_S2G = [("대학교", "university; “big school”"), ("대회", "a conference; “big meeting”"), ("대법원", "the Supreme Court"), ("육군", "army; “land military”"), ("육로", "a land route"), ("착륙", "landing (from the air); touchdown; “touching the land”"), ("상륙", "disembarkation; going ashore; “up (to the) land”")]
_S2 = [("육군 대장", "an Army general; a four-star general"), ("대로", "a main road; a boulevard"), ("육해공", "land, sea and air"), ("육지", "land; dry land"), ("대식가", "a big eater; “big eating person”"), ("육교", "an overpass; a pedestrian bridge; “land bridge”")]
_S3G = [("전문가", "an expert; “specialized professional”"), ("전문기술", "expertise; “specialized skill”"), ("전문의", "a medical specialist; “specialized doctor”"), ("전문대학", "a junior college; “specialized college”"), ("농업", "agriculture; farming industry; “agricultural job”"), ("어업", "fishery; “fishing job”")]
_S3 = [("전공", "a major; a field of specialization"), ("부전공", "a minor (field of study)"), ("버스전용", "bus-only; “bus exclusive use”"), ("대문", "a front gate; “big door”"), ("정문", "a front gate; the main entrance"), ("후문", "a back gate; a rear entrance"), ("사무직", "an office job; a clerical position"), ("노동직", "a labor job; a manual job"), ("직장", "a workplace; a job")]

# ================================================================== L1
L1 = lesson(
    "Ch 43 · What the chapter teaches, 천주교 · 대륙 · 전문직",
    "종교와 사회 · 천주교 · 대륙 · 전문직 · 종교 · 육군 · 직업",
    requires=[],
    cards=[
        card("What Chapter 43 teaches (종교와 사회)",
             "Chapter 43, “Religion and Society”, has a vocabulary builder, three topic presentations (religion and volunteer work, life of foreigners in Korea, women’s status and roles) with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify major religions and beliefs in Korea; discuss volunteer work; understand the lives of foreigners in Korea and their typical concerns; discuss the social status and role of women in Korea; and talk about more occupations.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; ~ (도)중에/(–는/던) (도)중에 (in the middle of doing something); the sentence ending –(으)ㄴ/는데(요); 반면(에) (on the other hand; whereas; while); the auxiliary verb −곤 하다 for common or routine occurrences of an action/event; and the Sino-Korean syllables within 천주교 (天主敎), 대륙 (大陸), and 전문직 (專門職)."),
        card("Sino-Korean in use: 천주교 (天主敎)",
             "This Sino-Korean word means the (Roman) Catholic Church or Catholicism. The first syllable 천 (天) means heaven or sky, as in 천문학 (astronomy; “study of the sky”), 천국 (heaven; paradise; the kingdom of heaven), 천하 (the world; the whole country; “below the heavens”), 천사 (an angel; “heavenly messenger”), and 천지 (heaven and earth; the world). The second syllable 주 (主) means lord, master, or host, as in 주인 (the master [of a house]; the head [of a family]; “master person”), 주일 (the Sabbath; the Lord’s day; Sunday), 주객 (host and guest), and 주권 (sovereignty; sovereign power; “lord rights”). The same syllable can also mean main, principal, or chief, as in 주목적 (a leading motive; a main purpose), 주력 부대 (main force units), and 주장 (the captain [of a team]; “main commander”). The last syllable 교 (敎) means teaching, religion, or church, as in 교사 (a teacher; a schoolteacher), 교과서 (a textbook; “teaching type book”), 불교 (Buddhism; “Buddhist religion”), 무교 (having no religion; without religion; irreligious), and 기독교 (Christianity; the Christian religion). Thus the word 천주교 literally means “religion of the Lord of the heavens,” and the word refers to the Roman Catholic Church or Catholicism.",
             tables=[ktable(_S1G)]),
        card("Sino-Korean in use: 대륙 (大陸)",
             "This Sino-Korean word means a continent. As in words like 대학교 (university; “big school”) and 대회 (a conference; “big meeting”), and 대법원 (the Supreme Court), the first syllable 대 (大) means big, large, or great, and the second syllable 륙/육 (陸) means land, as in words like 육군 (army; “land military”), 육로 (a land route), 착륙 (landing [from the air]; touchdown [of aircraft]; “touching the land”), and 상륙 (disembarkation; going ashore [from a ship]; “up [to the] land”). Thus the word 대륙 literally means “big land” or “great land,” and the word refers to any of the six or seven great areas of land on the globe. The book asks you to guess the meaning of 육군 대장, 대로, 육해공, 육지, 대식가 and 육교 (the book glosses 교 [橋]: bridge; my answers):",
             tables=[ktable(_S2G), ktable(_S2)]),
        card("Sino-Korean in use: 전문직 (專門職)",
             "This Sino-Korean word is made up of the two words 전문 and 직(업). The word 전문 (專門) means specialty, special subject, or specialized, as in 전문가 (an expert; “specialized professional”), 전문기술 (expertise; “specialized skill”), 전문의 (a medical specialist; “specialized doctor”), and 전문대학 (a junior college; “specialized college”). It is interesting to note that the literal meaning of the word 전문 is “exclusive door” or “only gate,” and the literal meaning has evolved to mean specialty, special subject, or specialized. The word 직(업) means job, position, or occupation, as in 농업 (agriculture; farming industry; “agricultural job”) and 어업 (fishery; “fishing job”). Thus the literal meaning of the word 전문직 is “specialty job” or “specialized job,” and the word refers to a professional job that requires specialized skills. The book asks you to guess the meaning of 전공, 부전공, 버스전용, 대문, 정문, 후문, 사무직, 노동직 and 직장 (my answers):",
             tables=[ktable(_S3G), ktable(_S3)]),
    ],
    exercises=uniq(
        _tr(_S1G + _S2G + _S2 + _S3G + _S3, k=3)
        + [M("What does 천 (天) mean?", "heaven; sky", ["land", "teaching", "job"], "천국."), M("What does 주 (主) mean?", "lord; master; host (also main)", ["land", "job", "big"], "주인."), M("What does 교 (敎) mean?", "teaching; religion; church", ["heaven", "land", "job"], "불교."), M("What does 대 (大) mean?", "big; large; great", ["small", "land", "job"], "대륙."), M("What does 륙/육 (陸) mean?", "land", ["sea", "heaven", "job"], "육군."), M("What does 전문 (專門) mean?", "specialty; specialized", ["a gate only", "a job", "a big door"], "전문가."), M("What does 직 (職) mean?", "job; position; occupation", ["land", "heaven", "teaching"], "농업, 직장."), M("What is the literal meaning of 천주교?", "“religion of the Lord of the heavens”", ["“big land”", "“specialized job”", "“planted things”"], "천 + 주 + 교."), M("What is the literal meaning of 대륙?", "“big land” or “great land”", ["“specialty job”", "“religion of the Lord of the heavens”", "“sea military”"], "대 + 륙."), M("What is the literal meaning of 전문직?", "“specialty job” or “specialized job”", ["“big land”", "“Lord’s religion”", "“land military”"], "전문 + 직."), M("What is the literal meaning of 전문 itself?", "“exclusive door” or “only gate”", ["“big school”", "“land route”", "“heavenly messenger”"], "The book’s note."),
           F("부모님은 기독___를 믿습니다. (religion)", "교", ["직", "륙"], "기독교."), F("육___ 대장은 군인입니다. (land army)", "군", ["문", "직"], "육군."), F("전문___ 여성들이 늘고 있습니다. (professional jobs)", "직", ["교", "륙"], "전문직."), F("한국은 아시아 대___에 있습니다. (continent)", "륙", ["교", "직"], "대륙."), F("저는 사무___ 으로 일합니다. (office job)", "직", ["교", "륙"], "사무직."),
           read_q("천주교"), read_q("대륙"), read_q("전문직"), read_q("종교"), read_q("육군")]
    ),
)

# ================================================================== L2 Vocabulary builder
_VB = [("기독교", "Christianity"), ("교회", "a (Christian) church; a chapel"), ("유창하다", "to be fluent; to be eloquent"), ("종교", "religion"), ("중남미", "Central and South America"), ("통하다", "to understand each other; “flow freely (both ways)”"), ("천주교", "Roman Catholicism"), ("중동", "Middle East"), ("조종사", "a pilot; an operator"), ("유교", "Confucianism"), ("태국", "Thailand"), ("작가", "a writer; an author"), ("의사소통", "communication"), ("대만", "Taiwan"), ("판사", "a judge"), ("기도하다", "to pray"), ("모국어", "mother tongue; native language"), ("대륙", "a continent; “big land”"), ("엔지니어", "an engineer"), ("이슬람교", "Islam")]
_MATCH = [("기독교, 이슬람교, 불교, 유교, 천주교", "종교", "religion"), ("이라크, 이란, 사우디아라비아, 쿠웨이트", "중동", "Middle East"), ("비행기를 날게 하는 사람", "조종사", "pilot"), ("멕시코, 브라질, 칠레, 아르헨티나", "중남미", "Central and South America"), ("아메리카, 아시아, 유럽, 아프리카", "대륙", "continent"), ("소설이나 드라마, 영화, 연극의 시나리오를 쓰는 사람", "작가", "writer"), ("중국 아래 있는 나라", "대만", "Taiwan")]
L2 = lesson(
    "Ch 43 · Vocabulary Builder: religions, regions and jobs",
    "기독교 · 교회 · 유창하다 · 종교 · 중남미 · 통하다 · 천주교 · 중동 · 조종사 · 유교 · 태국 · 작가 · 의사소통 · 대만 · 판사 · 기도하다 · 모국어 · 대륙 · 엔지니어 · 이슬람교",
    requires=[],
    cards=[
        card("새 단어: twenty words",
             "You already previewed the following new words for Chapter 43 (기독교, 교회, 유창하다, 종교, 중남미, 통하다, 천주교, 중동, 조종사, 유교, 태국, 작가, 의사소통, 대만, 판사, 기도하다, 모국어, 대륙, 엔지니어, 이슬람교). The book asks you to skim them, circle those you do not know, and look them up. The meanings are the book’s from the chapter glossary:",
             tables=[ktable(_VB)]),
        card("Step c: match the clues with the words",
             "Read the clues in the left column and match them with the word in the right column (the book’s words are 조종사, 대륙, 작가, 종교, 대만, 중남미, 중동). The clues are the book’s; the matches are my answers.",
             tables=[table(["Clue", "Word (mine)", "English"], [[a, b, c] for a, b, c in _MATCH])]),
        card("Activities left out", "Activities 1 and 2 (SMART Board), the PowerPoint Sino-Korean presentation, Activity 3 (SMART Board) and Activity 4 (the “STOP!” game: sit in a circle, pass a ball until the teacher says 그만, describe the word on the top card without saying it, and the class guesses) are computer and game activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(["기독교", "교회", "유창하다", "종교", "중남미", "통하다", "중동", "조종사", "유교", "태국", "작가", "의사소통", "대만", "판사", "모국어", "대륙", "엔지니어"]))
        + [M("Which word is described by “기독교, 이슬람교, 불교, 유교, 천주교”?", "종교", ["대륙", "작가", "대만"], "My match."), M("Which word is described by “이라크, 이란, 사우디아라비아, 쿠웨이트”?", "중동", ["중남미", "대륙", "종교"], "My match."), M("Which word is described by “비행기를 날게 하는 사람”?", "조종사", ["작가", "판사", "엔지니어"], "My match."), M("Which word is described by “멕시코, 브라질, 칠레, 아르헨티나”?", "중남미", ["중동", "대륙", "대만"], "My match."), M("Which word is described by “아메리카, 아시아, 유럽, 아프리카”?", "대륙", ["종교", "중동", "중남미"], "My match."), M("Which word is described by “중국 아래 있는 나라”?", "대만", ["태국", "중동", "중남미"], "My match."), M("What does 기도하다 mean?", "to pray", ["to believe", "to donate", "to visit"], "기도하다."),
           F("멕시코, 브라질, 칠레는 ___에 있는 나라입니다. (Central and South America)", "중남미", ["중동", "유럽"], "중남미."), F("한국어를 ___하게 하고 싶어요. (fluently)", "유창", ["완벽", "어색"], "유창하다."), F("그 사람은 한국어를 잘해서 ___가 잘 돼요. (communication)", "의사소통", ["의존", "오해"], "의사소통."), F("한국의 ___는 한국어입니다. (mother tongue)", "모국어", ["대륙", "언어"], "모국어."), F("저는 비행기 ___가 되고 싶어요. (pilot)", "조종사", ["판사", "작가"], "조종사."),
           read_q("종교"), read_q("조종사"), read_q("중남미"), read_q("중동"), read_q("의사소통")]
    ),
)

# ================================================================== L3 Topic A
_A_DLG = [
    ("민준", "유나 씨, 이번 주말에 뭐 할 거예요?", "Yuna, what are you going to do this weekend?"),
    ("유나", "저는 이번 토요일에 양로원으로 자원봉사 하러 가요.", "This Saturday I am going to a nursing home to do volunteer work."),
    ("민준", "그래요? 좋은 일 하러 가시네요. 혼자 가세요?", "Really? You are going to do a good deed. Are you going alone?"),
    ("유나", "아니요. 제가 다니는 교회의 봉사 단체 회원들과 함께 갈 거예요.", "No. I will go with the members of the volunteer group of the church I attend."),
    ("민준", "봉사활동 하러 자주 가세요?", "Do you go to do volunteer work often?"),
    ("유나", "매주 토요일마다 가요. 보통 양로원과 고아원을 격주로 방문해요. 또 명절이나 성탄절 때는 장애인 복지시설에도 봉사하러 가구요.", "I go every Saturday. I usually visit a nursing home and an orphanage every other week. Also, on holidays or at Christmas, I go to do volunteer work at welfare facilities for the disabled too."),
    ("민준", "아, 정말 좋은 일을 많이 하시네요.", "Oh, you really do a lot of good things."),
    ("유나", "아니에요. 참, 민준 씨는 주말에 뭐 특별한 계획 있으세요?", "Not at all. By the way, Minjun, do you have any special plans for the weekend?"),
    ("민준", "이번 주 일요일이 석가탄신일이잖아요. 그때 우리 절에서 어려운 이웃을 위한 자선 행사를 해요. 저도 가서 도와드리려고요.", "This Sunday is Buddha’s birthday, you know. At that time, our temple holds a charity event for needy neighbors. I am going to help there too."),
    ("유나", "아, 네. 의미 있는 행사네요. 요즘 어려운 이웃들을 돕는 종교단체행사가 많은 것 같아요.", "Oh, yes. It is a meaningful event. These days there seem to be many religious group events that help needy neighbors."),
    ("민준", "그래요. 아주 바람직한 일이에요.", "Yes. It is a very desirable thing."),
]
_A_WORDS = ["개신교", "격주", "고아원", "교회", "기도(하다/드리다)", "기독교", "기부(하다)", "기타", "무속신앙/샤머니즘", "믿다", "바람직하다", "복지", "석가탄신일", "성당", "성탄절", "신자", "양로원", "유교", "의미(있다)", "이슬람교/회교", "자선", "장애인", "종교", "천주교/가톨릭(교)"]
_REL = [("전통적으로 한국에는 불교를 믿는 사람들이 많았습니다.", "Traditionally, there were many people in Korea who believed in Buddhism."), ("또 무속신앙도 오랫동안 한국인들의 생활에 큰 영향을 주었습니다.", "Also, shamanism has had a great influence on Koreans’ lives for a long time."), ("최근 통계를 보면 종교가 있는 한국인 중에서 사십오 퍼센트가 개신교 신자라고 합니다.", "According to recent statistics, they say 45 percent of Koreans who have a religion are Protestants."), ("개신교 다음으로 신자가 많은 종교는 불교입니다.", "The religion with the next most believers after Protestantism is Buddhism."), ("불교 신자는 전체 종교 인구의 삼십오 퍼센트 정도 됩니다.", "Buddhists make up about 35 percent of the total religious population."), ("그리고 종교 인구의 십팔 퍼센트 정도가 천주교 신자입니다.", "And about 18 percent of the religious population are Catholics."), ("유교 등 기타 종교를 가진 사람은 이 퍼센트 정도 됩니다.", "People with other religions such as Confucianism are about 2 percent.")]
L3 = lesson(
    "Ch 43 · Topic A: Going to a nursing home to volunteer (양로원에 자원봉사 하러 가요)",
    "자원봉사 · 양로원 · 고아원 · 교회 · 석가탄신일 · 자선 행사 · 한국의 종교 · 무속신앙",
    requires=[],
    cards=[
        card("Topic A: Going to a nursing home to volunteer (양로원에 자원봉사 하러 가요)",
             "Two neighbors are talking about volunteer activities they will participate in over the coming weekend. (The English is mine; the book gives none; the book’s “아…” is written 아, and its footnote numbers are dropped. The book’s footnotes: 아니에요 or 뭘요 is a common response to a compliment; this type of expression conveys the recipient’s humble attitude. (생활이) 어려운 이웃, which literally means “neighbors whose living is difficult,” refers to needy people.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_A_WORDS)),
        card("한국의 종교", "The book shows a pie chart of religions in Korea with the labels 개신교, 천주교, 불교, 무교 (종교 없음) and 기타 종교 (the chart is a picture and is left out; the numbers are in the article below)."),
        card("한국에서는: Shamanism in Korea",
             "In traditional Korean society, shamanism had its roots in various indigenous beliefs that widely influenced people’s lives. Koreans in the past would frequently visit shamans, called 무당 (巫堂), who acted as an intermediary between the gods and humans, to gain good fortune, cure illness, etc. The shaman would then hold a ritual called 굿 to pray to the gods. As Korean society modernized, this practice diminished and was ultimately regarded as superstition. Recently, however, songs and dances that are part of 굿 have been recognized as important assets of traditional Korean culture."),
        card("Follow-up 2 (Reading): religions in Korea",
             "a. Read the following article about religions in Korea; the book asks you to fill in, in English, the labels or percents missing from the bar graph (the book glosses 통계: statistics). The article is the book’s with the percents spelled out; the English is mine. b. The book asks you to translate two underlined sentences (the underlining is not in my text, so I translate the whole article).",
             examples=passage(_REL)),
        card("The bar graph filled in (mine)", "",
             tables=[table(["Religion", "Percent of the religious population (mine)"], [["Protestantism (개신교)", "45"], ["Buddhism (불교)", "35"], ["Catholicism (천주교)", "18"], ["Other (기타)", "2"]])]),
        card("Useful links", "The book lists three links: 한국의 샤머니즘, 북한에서의 종교의 역할 and 한국의 종교."),
        card("Activities left out", "The presentation steps of Topic A (SMART Board, the pair role-reading in which each partner says the other’s lines in English) and Follow-up 1 (listening to three conversations about a female speaker’s religious volunteer work at a welfare facility and noting the facility and her religion) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_strip(_A_DLG) + _REL, k=3)
        + [M("Where is Yuna going this Saturday?", "To a nursing home to volunteer", ["To a church service", "To a wedding", "To the market"], "양로원으로 자원봉사."), M("With whom does Yuna go?", "Members of her church’s volunteer group", ["Alone", "Her family", "Her coworkers"], "교회의 봉사 단체 회원들."), M("How often does Yuna visit the nursing home and orphanage?", "Every other week", ["Every day", "Once a year", "Every month"], "격주로."), M("What holiday is this Sunday?", "Buddha’s birthday", ["Christmas", "Chuseok", "New Year’s Day"], "석가탄신일."), M("What does Minjun’s temple hold?", "A charity event for needy neighbors", ["A concert", "A market", "A wedding"], "어려운 이웃을 위한 자선 행사."), M("What religion has the most believers in the article?", "Protestantism", ["Buddhism", "Catholicism", "Confucianism"], "개신교 사십오 퍼센트."), M("What percent of the religious population are Buddhists?", "About 35", ["About 45", "About 18", "About 2"], "삼십오 퍼센트."), M("What does 아니에요 express as a response to a compliment?", "A humble attitude", ["Anger", "Agreement", "Surprise"], "The book’s note."),
           F("교회의 봉사 ___ 회원들과 함께 갈 거예요. (group)", "단체", ["시설", "행사"], "단체."), F("보통 양로원과 고아원을 ___로 방문해요. (every other week)", "격주", ["매일", "격일"], "격주."), F("그때 우리 절에서 어려운 이웃을 위한 ___ 행사를 해요. (charity)", "자선", ["기부", "복지"], "자선."), F("아주 ___ 일이에요. (desirable)", "바람직한", ["의미 있는", "어색한"], "바람직하다."), F("전통적으로 한국에는 불교를 ___ 사람들이 많았습니다. (believe in)", "믿는", ["대하는", "통하는"], "믿다."),
           read_q("양로원에 자원봉사 하러 가요"), read_q("이번 토요일에 양로원으로 자원봉사 하러 가요"), read_q("매주 토요일마다 가요"), read_q("이번 주 일요일이 석가탄신일이잖아요"), read_q("아주 바람직한 일이에요")]
    ),
)

# ================================================================== L4 Activities A: winter volunteering
_WV = [("연말에 종교계에서 이웃을 위해 다양한 봉사활동을 계획하고 있다.", "At the end of the year, religious communities are planning various volunteer activities for their neighbors."), ("개신교는 십이월 한 달간 따뜻한 겨울 캠페인을 벌인다.", "Protestants hold the “Warm Winter” campaign for the month of December."), ("난방비가 없는 오천오백여 가정에 삼만 원씩 지원할 계획이다.", "They plan to support more than 5,500 households without heating money with 30,000 won each."), ("이를 위해 오억 원 규모의 모금 운동을 하고 있다.", "For this, they are running a fundraising drive on the scale of 500 million won."), ("서울 천주교 사회복지회는 집 없는 사람들을 위해 무료급식 빨간 밥차 두 대를 운영한다.", "The Seoul Catholic Social Welfare Association operates two “Red Rice Cars” of free meal service for homeless people."), ("빨간 밥차는 한 시간에 삼백 인분의 식사를 준비할 수 있으며, 일주일에 다섯 번씩 서울역 등에서 급식 활동을 한다.", "A Red Rice Car can prepare 300 servings of meals in an hour, and does meal service activities at Seoul Station and elsewhere five times a week."), ("불교계는 겨울방학 동안 종로구에 사는 육백여 명의 고아에게 과외수업을 해 주기로 했다.", "The Buddhist community decided to give tutoring classes during the winter vacation to more than 600 orphans living in Jongno-gu."), ("학원에 다닐 수 없는 아이들한테 국어, 영어, 수학 등의 공부를 무료로 가르칠 예정이다.", "They plan to teach children who cannot attend private academies subjects such as Korean, English and math for free.")]
L4 = lesson(
    "Ch 43 · Activities A: year-end volunteer work by religious groups",
    "연말 봉사활동 · 따뜻한 겨울 캠페인 · 빨간 밥차 · 과외수업 · 종교계 · 나라별 종교",
    requires=[],
    cards=[
        card("Activity 3 (Reading): a news article",
             "Read the news article and complete the tasks that follow (the book glosses ~계: a community, a world, a circle). The article is the book’s with the numbers spelled out; the English is mine.",
             examples=passage(_WV)),
        card("The answers (mine)", "1. The book gives three possible titles and asks you to check the right one: “Volunteer Work Offered by Various Religious Groups During the Winter Season” (my answer: the first). 2. The table:",
             tables=[table(["Organization", "Volunteer activity (mine)"], [["Protestants", "The “Warm Winter” campaign in December: 30,000 won each to more than 5,500 households without heating money; a fundraising drive of 500 million won"], ["Seoul Catholic Social Welfare Association", "Two “Red Rice Cars” for free meals for homeless people: 300 servings an hour, five times a week at Seoul Station and elsewhere"], ["Buddhist community", "Free tutoring (Korean, English, math) for more than 600 orphans in Jongno-gu during the winter vacation"]])]),
        card("Activity 4 (Research): religions of each country",
             "The teacher gives you a country to research; you use the links (Wikipedia, Naver, Yahoo, Google) to find the percent of followers of each religion (개신교, 천주교, 불교, 이슬람교, 기타) and fill in the table, make a pie chart or bar graph in the class notebook (MS Teams), present your results, and then organize two classmates’ presentations in a table (country 1, country 2). This is an internet and group activity and is left out."),
        card("Activities left out", "Activity 1 (SMART Board) and Activity 2 (listening to three conversations between two friends talking about religious volunteer work at different welfare facilities and filling in religion, welfare facility and activities planned) are audio and computer activities."),
    ],
    exercises=uniq(
        _tr(_WV, k=3)
        + [M("How long is the Protestant “Warm Winter” campaign?", "The month of December", ["All year", "One week", "Three days"], "십이월 한 달간."), M("How much will each household receive?", "30,000 won", ["500 million won", "3,000 won", "300,000 won"], "삼만 원씩."), M("How many Red Rice Cars does the Catholic association operate?", "Two", ["Five", "Ten", "One"], "두 대."), M("How many servings can a Red Rice Car prepare in an hour?", "300", ["30", "600", "5"], "삼백 인분."), M("Whom will the Buddhist community tutor?", "More than 600 orphans in Jongno-gu", ["University students", "Soldiers", "Foreign workers"], "육백여 명의 고아."), M("What subjects will be taught?", "Korean, English and math", ["Music and art", "Science only", "Cooking"], "국어, 영어, 수학."), M("How often does the Red Rice Car serve meals?", "Five times a week", ["Every day", "Once a week", "Once a month"], "일주일에 다섯 번씩."), M("Which title fits the article?", "Volunteer Work Offered by Various Religious Groups During the Winter Season", ["Regular Visits to Welfare Facilities", "Volunteer Work on a Special Day", "A Year of Welfare"], "연말, 겨울방학."),
           F("개신교는 십이월 한 달간 ___ 캠페인을 벌인다. (Warm Winter)", "따뜻한 겨울", ["차가운 여름", "즐거운 봄"], "따뜻한 겨울."), F("집 없는 사람들을 위해 ___급식을 한다. (free meal)", "무료", ["유료", "기타"], "무료급식."), F("학원에 다닐 수 없는 아이들한테 공부를 ___로 가르칠 예정이다. (for free)", "무료", ["유료", "격주"], "무료."), F("오억 원 ___의 모금 운동을 하고 있다. (scale)", "규모", ["의미", "자선"], "규모."), F("불교계는 겨울방학 동안 고아에게 ___수업을 해 주기로 했다. (tutoring)", "과외", ["정규", "야간"], "과외수업."),
           read_q("연말에 종교계에서 이웃을 위해 봉사활동을 합니다"), read_q("개신교는 따뜻한 겨울 캠페인을 벌입니다"), read_q("빨간 밥차를 운영합니다"), read_q("고아에게 무료로 공부를 가르칩니다"), read_q("모금 운동을 하고 있습니다")]
    ),
)

# ================================================================== L5 Topic B
_B_DLG = [
    ("기자", "터몬토 씨, 한국생활이 어떠세요?", "Ms. Termonto, how is life in Korea?"),
    ("터몬토", "좋아요. 처음에는 좀 힘들었지만, 지금은 많이 적응됐어요.", "It’s good. It was a little hard at first, but now I have adapted a lot."),
    ("기자", "그러세요? 처음에 어떤 점이 힘드셨어요?", "Is that so? What was hard for you at first?"),
    ("터몬토", "언어와 문화가 달라서 고생했어요. 풍습도 다르고 말이 안 통해서 실수도 많이 했고요.", "The language and culture were different, so I had a hard time. The customs were different too, and we could not understand each other, so I made many mistakes."),
    ("기자", "근데 지금은 한국어를 유창하게 아주 잘하시는데요.", "But now you speak Korean fluently and very well."),
    ("터몬토", "아니에요. 아직도 발음이나 문법은 어려워요. 집에서는 대화하는 도중에 식구들이 서투른 표현을 고쳐 줘요.", "Not at all. Pronunciation and grammar are still difficult. At home, in the middle of conversation, my family corrects my clumsy expressions."),
    ("기자", "그렇군요. 이웃 사람들은 잘 해주세요?", "I see. Do your neighbors treat you well?"),
    ("터몬토", "네. 모두 따뜻하게 대해 주세요. 그래서 이제는 한국이 고향 같아요.", "Yes. Everyone treats me warmly. So now Korea feels like my hometown."),
    ("기자", "자녀들 언어교육은 어떻게 하세요?", "How do you do your children’s language education?"),
    ("터몬토", "남들은 애들이 한국 말만 해도 된다고 생각해요. 하지만, 저는 아이들이 한국 말도 잘하고 태국 말도 잘하면 좋겠어요. 그래서 애들하고는 태국 말로 의사소통을 해요.", "Other people think it is fine for the children to speak only Korean. But I would like my children to speak both Korean and Thai well. So I communicate with the kids in Thai."),
]
_B_WORDS = ["근로자", "남", "대륙", "대만", "대하다", "모국어", "문법", "서투르다/서툴다", "아프리카", "어색하다", "언어", "오해", "완벽", "유럽/구라파", "유창하다", "의사소통", "의존", "중남미", "중동", "태국", "통하다", "풍습"]
_DJ = [("늘어나는 외국인 유학생 국적도 다양화", "The increasing number of foreign students; their nationalities are diversifying too"), ("대전지역에 다양한 국적의 외국인 유학생들이 늘어나고 있다.", "Foreign students of various nationalities are increasing in the Daejeon area."), ("이 영향으로 대학가를 중심으로 다문화 바람이 불고 있다.", "As a result, a multicultural wind is blowing, centered on the university neighborhoods."), ("예전에는 중국, 일본, 베트남 등 아시아 지역 유학생이 대부분이었다.", "In the past, most were students from Asian regions such as China, Japan and Vietnam."), ("그런데 최근에는 다양한 국적의 유학생들을 볼 수 있다.", "But recently, students of various nationalities can be seen."), ("그 변화는 캠퍼스에 보이는 학생들의 피부색과 생김새만 봐도 금방 알 수 있다.", "You can tell that change right away just by looking at the skin colors and appearances of the students seen on campus."), ("배재대학교는 대전지역에서 두 번째로 외국인 유학생이 많은 학교이다.", "Pai Chai University is the school with the second most foreign students in the Daejeon area."), ("배재대에는 사십육 개국 구백여 명의 외국인 유학생이 등록해 있다.", "More than 900 foreign students from 46 countries are registered at Pai Chai."), ("북미, 아시아, 유럽 국가의 유학생뿐만 아니라 아프리카, 중남미 국가의 유학생도 많이 있다.", "There are many students not only from North American, Asian and European countries but also from African and Central and South American countries.")]
L5 = lesson(
    "Ch 43 · Topic B: How is life in Korea? (한국생활이 어떠세요?)",
    "한국생활 · 적응 · 언어와 문화 · 의사소통 · 모국어 · 외국인 유학생 · 다문화",
    requires=[],
    cards=[
        card("Topic B: How is life in Korea? (한국생활이 어떠세요?)",
             "A magazine reporter is interviewing a woman from Thailand who immigrated to Korea 10 years ago. (The English is mine; the book gives none; the book’s “!” is dropped. The book’s footnote: 서투르다 belongs to the 르 irregular verbs [부르다, 빠르다, 누르다, etc.]. However, since 서투르다 can contract into 서툴다, both 서투른 and 서툰 are accepted as attributive forms.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists –(으)ㄴ/는데(요) and ~ (도)중에/(–는/던) (도)중에 (see the grammar).", tables=_words(_B_WORDS)),
        card("Follow-up 2 (Reading): foreign students in Daejeon",
             "The following newspaper article discusses the changing foreign student population in the Daejeon area; the book asks (1) what change is being reported and (2) to translate the underlined sentence (the book glosses 국적: nationality; 생김새: [physical] appearance). The article is the book’s with the numbers spelled out; the English is mine (I translate every sentence).",
             examples=passage(_DJ)),
        card("The answer to question 1 (mine)", "The change reported: the number of foreign students in the Daejeon area is increasing, and their nationalities are becoming diverse (in the past most were Asian students from China, Japan and Vietnam; now there are students from North America, Europe, Africa and Central and South America too)."),
        card("Useful links", "The book lists two links: 안산시 외국인 주민센터 (Ansan City Foreigner Residents Center) and 한국외국인노동자지원센터 (the Korea Foreign Workers Support Center)."),
        card("Activities left out", "The presentation steps of Topic B (SMART Board and pair role-reading) and Follow-up 1 (listening to three voice mails in which a Korean friend leaves a message for a foreigner seeking information at a visitors’ center, and filling in the nationality, occupation, problem mentioned and question asked) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG) + _DJ, k=3)
        + [M("Where is Ms. Termonto from?", "Thailand", ["Taiwan", "Africa", "Europe"], "태국."), M("What was hard for her at first?", "Language and culture were different", ["The food", "The weather", "The jobs"], "언어와 문화가 달라서."), M("What do her family do at home?", "Correct her clumsy expressions in the middle of conversation", ["Speak only Thai", "Ignore her mistakes", "Teach her cooking"], "서투른 표현을 고쳐 줘요."), M("How do her neighbors treat her?", "Warmly", ["Coldly", "Rudely", "Not at all"], "따뜻하게 대해 주세요."), M("Which language does she use with her kids?", "Thai", ["Korean", "English", "Chinese"], "태국 말로."), M("What does she want for her children?", "To speak both Korean and Thai well", ["To forget Thai", "To speak only Korean", "To study abroad"], "한국 말도 잘하고 태국 말도 잘하면."), M("Which students used to be the majority in Daejeon?", "Asian students such as from China, Japan and Vietnam", ["African students", "European students", "American students"], "아시아 지역 유학생이 대부분."), M("What does the article say about Pai Chai University?", "It has the second most foreign students in Daejeon", ["It has the most", "It has none", "It is new"], "두 번째로."),
           F("언어와 문화가 달라서 ___했어요. (had a hard time)", "고생", ["도전", "진학"], "고생하다."), F("말이 안 ___ 실수도 많이 했어요. (communicate)", "통해서", ["대해서", "믿어서"], "통하다."), F("모두 따뜻하게 ___ 주세요. (treat)", "대해", ["믿어", "통해"], "대하다."), F("한국어를 ___하게 아주 잘하시는데요. (fluently)", "유창", ["어색", "서투"], "유창하다."), F("아직도 발음이나 ___은 어려워요. (grammar)", "문법", ["풍습", "언어"], "문법."),
           read_q("한국생활이 어떠세요"), read_q("언어와 문화가 달라서 고생했어요"), read_q("모두 따뜻하게 대해 주세요"), read_q("아이들하고는 태국 말로 의사소통을 해요"), read_q("대전지역에 외국인 유학생들이 늘어나고 있습니다")]
    ),
)

# ================================================================== L6 Grammar A: in the middle of
_DJ1 = [("지금 요리 중입니다.", "I am cooking right now."), ("숙제하는 중입니다.", "I am doing my homework.")]
_DJ2 = [("요리하는 (도)중에 전화를 받았어요.".replace("(도)", ""), "I got a phone call while cooking."), ("식사 도중에 전화를 받았어요.", "I got a phone call while eating."), ("수업 도중에 전화를 받았어요.", "I got a phone call in (the middle of) class.")]
_DJ3 = [("요리하던 도중에 전화를 받았어요.", "I got a phone call while cooking.")]
_DJ4 = [("회의 중에 전기가 나갔어요.", "In the middle of the meeting, the power went out."), ("김 일병은 수업을 하던 도중에 화장실에 갔습니다.", "In the middle of class, PFC Kim left to go to the bathroom."), ("김 일병은 수업을 하는 도중에 화장실에 갔습니다.", "In the middle of class, PFC Kim left to go to the bathroom.")]
_DJM = [("결혼식을 하던 도중에 전기가 나갔어요.", "The power went out in the middle of the wedding."), ("결혼식을 하는 중에 불이 났어요.", "A fire broke out in the middle of the wedding."), ("결혼식을 하던 중에 친구가 쓰러졌어요.", "A friend collapsed in the middle of the wedding.")]
_DJS = [("운전하는 도중에 졸음이 왔어요.", "I got sleepy while driving."), ("공부하던 도중에 친구가 찾아왔어요.", "A friend came to see me while I was studying."), ("회의 도중에 휴대폰이 울렸어요.", "My cell phone rang in the middle of the meeting."), ("식사하던 중에 지진이 났어요.", "An earthquake occurred while we were eating.")]
L6 = lesson(
    "Ch 43 · Grammar A: ~ (도)중에 and –는/던 (도)중에 (in the middle of doing something)",
    "~ 중에 · ~ 도중에 · –는 도중에 · –던 도중에 · 회의 중에 전기가 나갔어요 · ~ 중이다",
    requires=[],
    cards=[
        card("Recall ~ 중이다",
             "Recall the verbal phrase ~ 중이다 or –는 중이다, as in 지금 요리 중입니다 (I am cooking right now) and 숙제하는 중입니다 (I am doing my homework). This phrase literally means “to be in the middle of doing (something)” because the Sino-Korean syllable 중 (中) means middle. Thus, the whole phrase is used to express an action in progress.",
             examples=passage(_DJ1)),
        card("~ (도)중에 and –는/던 (도)중에",
             "중 in the phrase ~ (도)중에 or –는 (도)중에 is the same Sino-Korean character with 중 in the phrase ~중이다 or –는 중이다. Thus, the phrase literally means “in the middle of doing (something)”; it can be translated as in the middle of, while, or during. For example (the English is the book’s; the book writes 도 in parentheses, as it is optional):",
             examples=passage(_DJ2)),
        card("The past tense",
             "–는 (도)중에 can be used for the past tense. However, –던 (도)중에 is specifically used for the past tense. For example (the English is the book’s):",
             examples=passage(_DJ3)),
        card("The patterns", "noun + (도)중에; action verb stem + 는 (도)중에. More examples (the English is the book’s):", examples=passage(_DJ4)),
        card("Follow-up 1 (Speaking): the model",
             "Student A picks a card and conjugates the phrase aloud, using –는/던 (도)중에 (결혼식을 하다 → 결혼식을 하던 도중에 or 결혼식을 하는 도중에). Student B creates a sentence that includes Student A’s phrase. The book’s model sentences (the English is mine):",
             examples=passage(_DJM)),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_DJS)),
        card("Activities left out", "Follow-up 2 (listening to conversations in which a male speaker talks about two events or actions using ~ (도)중에 or –는/던 (도)중에, and identifying the action in progress and the main verb phrase; the first, “fire broke out”, is done for you) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_DJ1 + _DJ2 + _DJ3 + _DJ4 + _DJM + _DJS, k=3)
        + [M("What does ~ (도)중에 mean?", "in the middle of; while; during", ["after", "before", "because of"], "The book’s note."), M("What does the Sino-Korean 중 (中) mean?", "middle", ["big", "land", "job"], "The book’s note."), M("Which ending is specifically for the past?", "–던 (도)중에", ["–는 (도)중에", "–(으)ㄹ (도)중에", "–고 (도)중에"], "The book’s note."), M("What follows a noun?", "(도)중에", ["는 (도)중에", "던 (도)중에", "(으)ㄴ 중에"], "The book’s note."), M("What does 회의 중에 전기가 나갔어요 mean?", "In the middle of the meeting, the power went out", ["After the meeting the power went out", "The meeting was canceled", "I left the meeting"], "The book’s example."), M("What does 식사 도중에 전화를 받았어요 mean?", "I got a phone call while eating", ["I ate after the call", "I did not answer", "I called while eating"], "The book’s example."),
           F("요리하는 ___에 전화를 받았어요. (in the middle)", "도중", ["동안", "후"], "도중에."), F("수업을 하던 ___에 화장실에 갔습니다. (in the middle)", "도중", ["후", "전"], "도중에."), F("회의 ___에 전기가 나갔어요. (in the middle)", "중", ["후", "전"], "중에."), F("결혼식을 ___ 도중에 불이 났어요. (was doing)", "하던", ["한", "할"], "-던 도중에."), F("식사 ___에 전화를 받았어요. (in the middle)", "도중", ["후", "전"], "도중에."),
           read_q("요리하는 도중에 전화를 받았어요"), read_q("식사 도중에 전화를 받았어요"), read_q("수업 도중에 전화를 받았어요"), read_q("회의 중에 전기가 나갔어요"), read_q("김 일병은 수업을 하던 도중에 화장실에 갔습니다")]
    ),
)

# ================================================================== L7 Grammar B: -(으)ㄴ/는데(요)
_ND1 = [("비가 많이 오는데요.", "It is raining a lot!"), ("한국말이 쉬운데요.", "Korean is easy (to learn)!")]
_ND2 = [("천장에서 물이 새는데요.", "The ceiling is leaking (and something has to be done about it)."), ("여보, 아기가 우는데.", "Honey, the baby is crying (and I want you to do something about it).")]
_ND3 = [("우리 가족이 미국에 살아요.", "My family lives in the U.S."), ("그래요? 미국 어디에 사는데요?", "Really? Where in the U.S. do they live?")]
_NDW = [("오늘 입은 코트가 아주 멋있어요.", "멋있는데요.", "The coat you are wearing today is very stylish! (I am surprised)"), ("현금이 얼마나 있어요?", "현금이 얼마나 있는데요?", "How much cash do you have? (I’d like to know more)"), ("밤 아홉 시 전까지는 집에 돌아가야 돼요.", "밤 아홉 시 전까지는 집에 돌아가야 되는데요.", "I have to go back home before 9 p.m. (and something has to be done about it)"), ("부인께서 음식을 참 잘 하십니다.", "부인께서 음식을 참 잘 하시는데요.", "Your wife cooks really well! (I am surprised)"), ("평일에는 이렇게 사람이 많지 않아요.", "평일에는 이렇게 사람이 많지 않은데요.", "There aren’t this many people on weekdays! (I am surprised)"), ("오레곤주에 언제 가 보셨어요?", "오레곤주에 언제 가 보셨는데요?", "When did you go to Oregon? (I’d like to know more)")]
_ND4 = [("제가 하이킹을 좋아해요.", "I like hiking."), ("그래서 빅서 근처에 자주 가는데요.", "So I often go near Big Sur."), ("보통 토요일에 가요.", "I usually go on Saturdays."), ("거기 캠프할 수 있는 곳도 있는데요.", "There is also a place there where you can camp."), ("보통 저는 그곳에서 잠은 안 자고 밤 늦게 기숙사로 돌아와요.", "Usually I do not sleep there and come back to the dormitory late at night."), ("거기 온천도 있다고 하는데요.", "I hear there are hot springs there too."), ("저는 아직도 못 가 봤어요.", "I still haven’t been able to go."), ("선생님도 빅서에 가 보세요.", "Teacher, you should go to Big Sur too."), ("얼마나 멋있는데요.", "It is so wonderful!")]
L7 = lesson(
    "Ch 43 · Grammar B: the sentence ending –(으)ㄴ/는데(요)",
    "-(으)ㄴ/는데(요) · 놀람 · 해결 요구 · 더 알고 싶음 · 비가 많이 오는데요 · 어디에 사는데요",
    requires=[],
    cards=[
        card("Three implicit meanings",
             "The sentence ending –(으)ㄴ/는데(요) is another variation of the informal verb ending –아/어요; this ending is often used to convey one of the following implicit meanings:\n\n"
             "1. “I am surprised.” (비가 많이 오는데요: It is raining a lot! 한국말이 쉬운데요: Korean is easy [to learn]!)\n\n"
             "2. “Something has to be done.” (천장에서 물이 새는데요: The ceiling is leaking [and something has to be done about it]. 여보, 아기가 우는데: Honey, the baby is crying [and I want you to do something about it].)\n\n"
             "3. “I’d like to know more about what you said.” (A: 우리 가족이 미국에 살아요. My family lives in the U.S. B: 그래요? 미국 어디에 사는데요? Really? Where in the U.S. do they live?)\n\n"
             "Keep in mind that the first two uses work only in a statement. The third use only works in a wh- question.",
             examples=passage(_ND1 + _ND2 + _ND3)),
        card("Follow-up 3 (Writing): change the endings to –(으)ㄴ/는데(요)",
             "Change the endings of the following sentences into the –(으)ㄴ/는데(요) form; the first one is done for you (멋있는데요). The sentences are the book’s with the time spelled out; the answers and the English are mine.",
             tables=[table(["Sentence", "–(으)ㄴ/는데(요) (mine)", "Meaning (mine)"], [[a, b, c] for a, b, c in _NDW], say=[0, 1])]),
        card("Follow-up 5 (Speaking): one minute of talking",
             "Sit in a circle; the first student chooses a topic from the list (내가 좋아하는 식당, 재미있었던 여행, 내가 다니던 고등학교, 군대에 입대하기 전에 한 일, 가장 친한 친구, 좋아하는 취미) and talks about it in Korean, using –(으)ㄴ/는데(요) as often as you can; each student has one minute. The book’s model (the English “Big Sur” is written 빅서; the English is mine):",
             examples=passage(_ND4)),
        card("Activities left out", "Follow-up 4 (listening to four conversations between two coworkers, checking which of the three meanings –(으)ㄴ/는데(요) has, and translating the sentence) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_ND1 + _ND2 + _ND3 + [(b, c) for a, b, c in _NDW] + _ND4, k=3)
        + [M("What are the three meanings of –(으)ㄴ/는데(요)?", "Surprise; something has to be done; wanting to know more", ["Past; present; future", "Request; offer; refusal", "Cause; result; purpose"], "The book’s note."), M("Which uses work only in a statement?", "Surprise and something has to be done", ["Wanting to know more", "All three", "None"], "The book’s note."), M("Which use works only in a wh- question?", "Wanting to know more", ["Surprise", "Something has to be done", "None"], "The book’s note."), M("What does 천장에서 물이 새는데요 imply?", "Something has to be done about the leak", ["I am surprised", "I want to know more", "I am happy"], "The book’s note."), M("What does 미국 어디에 사는데요 imply?", "I’d like to know more", ["I am surprised", "Please fix it", "I disagree"], "The book’s note."), M("What does 한국말이 쉬운데요 imply?", "I am surprised that Korean is easy", ["Please help me", "Tell me more", "I am angry"], "The book’s note."),
           F("비가 많이 오___! (surprise)", "는데요", ["는지요", "니까요"], "-는데요."), F("한국말이 쉬___! (surprise)", "운데요", ["우데요", "운지요"], "-(으)ㄴ데요."), F("천장에서 물이 새___. (something has to be done)", "는데요", ["는지요", "니까요"], "-는데요."), F("미국 어디에 사___? (want to know more)", "는데요", ["는지요", "으니까요"], "-는데요."), F("부인께서 음식을 참 잘 하시___. (surprise)", "는데요", ["는지요", "니까요"], "-는데요."),
           read_q("비가 많이 오는데요"), read_q("한국말이 쉬운데요"), read_q("천장에서 물이 새는데요"), read_q("미국 어디에 사는데요"), read_q("거기 온천도 있다고 하는데요")]
    ),
)

# ================================================================== L8 Activities B: foreigners in Korea
_FA = [("제 한국 이름은 한미나에요.", "My Korean name is Han Mina."), ("저는 태국에서 왔어요.", "I came from Thailand."), ("오 년 전에 태국에서 한국인 남편을 만나 한국에 왔어요.", "Five years ago I met a Korean husband in Thailand and came to Korea."), ("지금은 주부예요.", "Now I am a housewife."), ("요즘 일자리를 찾고 있지만 쉽지 않아요.", "These days I am looking for a job, but it is not easy."), ("한국에 와서 한국말을 열심히 공부했어요.", "After coming to Korea, I studied Korean hard."), ("그렇지만, 한국말이 여전히 서툴러요.", "However, my Korean is still clumsy."), ("그리고 이웃과 친해지기도 쉽지 않아요.", "And it is not easy to become close with the neighbors either."), ("가장 큰 걱정은 아이들의 교육이에요.", "My biggest worry is my children’s education.")]
_FB = [("제 한국이름은 이용기입니다.", "My Korean name is Lee Yonggi."), ("영국에서 왔습니다.", "I came from England."), ("한국에 온 지 삼 년 됐습니다.", "It has been three years since I came to Korea."), ("지금 영어학원 강사입니다.", "I am now an English academy instructor."), ("한국인 친구를 사귀고 싶지만, 기회가 없습니다.", "I want to make Korean friends, but there is no opportunity."), ("한국말 실력이 좋아졌지만, 여전히 회화는 어렵습니다.", "My Korean ability has improved, but conversation is still difficult."), ("지금도 식당에 가면 한국말로 주문하기가 어려워요.", "Even now, when I go to a restaurant, it is hard to order in Korean."), ("그리고 문화가 너무 달라서 이웃과 친해지기가 쉽지 않습니다.", "And the culture is so different that it is not easy to become close with the neighbors."), ("어떻게 하면 이웃과 친해질 수 있을까요?", "How can I become close with my neighbors?")]
L8 = lesson(
    "Ch 43 · Activities B: two foreigners living in Korea",
    "한국 생활에 적응하고 있어요 · 한미나 · 이용기 · 외국인의 어려움 · 이웃과 친해지기",
    requires=[],
    cards=[
        card("Activity 3 (Listening, reading and speaking): adjusting to life in Korea",
             "As a group, you will provide advice for a foreigner living in Korea. In step a, two foreigners describe the difficulties and concerns they face while living in Korea (Group A reads Foreigner A, Group B reads Foreigner B) and fill in a table in English (Korean name; occupation; difficulties and concerns). The passages are the book’s with the numbers spelled out; the English is mine.",
             examples=passage(_FA) + passage(_FB)),
        card("The table filled in (mine)", "",
             tables=[table(["", "Foreigner A", "Foreigner B"], [["Korean name", "한미나 (Han Mina)", "이용기 (Lee Yonggi)"], ["From", "Thailand (came five years ago after meeting her Korean husband)", "England (in Korea for three years)"], ["Occupation", "Housewife (looking for a job)", "English academy instructor"], ["Difficulties and concern(s)", "Hard to find a job; Korean is still clumsy; hard to become close with neighbors; the biggest worry is the children’s education", "No chance to make Korean friends; conversation and ordering in Korean are still hard; cultural differences make it hard to befriend neighbors (How can I become close with neighbors?)"]])]),
        card("Steps b and c", "In step b, six tips on how foreigners can successfully adjust to life in Korea are on audio (summarized in English in a table; the group discusses which tips fit the foreigner). In step c, the group writes a list of advice tips, using the tips and its own ideas, and presents the advice and the passage summary to the class in Korean. These are audio and group activities and are left out."),
        card("Activities left out", "Activity 1 (SMART Board) and Activity 2 (listening to four statements in which middle school students talk about a family member who is originally from a foreign country, writing the name of the continent for each country on the map [Germany, Mexico, China, Thailand] in Korean, and noting the relationship and the person’s speaking proficiency) are audio, map and computer activities."),
    ],
    exercises=uniq(
        _tr(_FA + _FB, k=3)
        + [M("Where is Han Mina from?", "Thailand", ["England", "Germany", "China"], "태국."), M("What does Han Mina do now?", "She is a housewife looking for a job", ["She is a teacher", "She is a student", "She is a nurse"], "주부, 일자리를 찾고 있다."), M("What is Han Mina’s biggest worry?", "Her children’s education", ["Money", "Housing", "Her health"], "아이들의 교육."), M("Where is Lee Yonggi from?", "England", ["Thailand", "Germany", "Australia"], "영국."), M("How long has Lee Yonggi been in Korea?", "Three years", ["Five years", "One year", "Ten years"], "삼 년."), M("What does Lee Yonggi do?", "He is an English academy instructor", ["He is a doctor", "He is a soldier", "He is a chef"], "영어학원 강사."), M("What does Lee Yonggi find difficult in a restaurant?", "Ordering in Korean", ["Paying", "Finding a seat", "Using chopsticks"], "한국말로 주문하기."), M("What do both foreigners find hard?", "Becoming close with neighbors", ["Finding food", "Finding housing", "Finding a taxi"], "이웃과 친해지기."),
           F("저는 태국에서 ___. (came)", "왔어요", ["갔어요", "있어요"], "오다."), F("요즘 ___를 찾고 있지만 쉽지 않아요. (job)", "일자리", ["이웃", "친구"], "일자리."), F("한국말이 ___ 서툴러요. (still)", "여전히", ["벌써", "아직도"], "여전히."), F("한국인 친구를 ___ 싶지만 기회가 없습니다. (make)", "사귀고", ["믿고", "대하고"], "사귀다."), F("한국말 ___이 좋아졌지만 회화는 어렵습니다. (ability)", "실력", ["의미", "풍습"], "실력."),
           read_q("제 한국 이름은 한미나에요"), read_q("가장 큰 걱정은 아이들의 교육이에요"), read_q("한국인 친구를 사귀고 싶지만 기회가 없습니다"), read_q("식당에서 한국말로 주문하기가 어려워요"), read_q("어떻게 하면 이웃과 친해질 수 있을까요")]
    ),
)

# ================================================================== L9 Topic C
_C_TXT = [("한국 사회에서 여성의 지위와 역할이 변하고 있다.", "The status and roles of women in Korean society are changing."), ("과거에 여성은 주로 가정에서 자녀를 양육하거나 가사 노동을 했다.", "In the past, women mainly raised children at home or did housework."), ("반면 요즘에는 사회에 진출하는 전문직 여성들이 증가하고 있다.", "On the other hand, these days the number of professional women entering society is increasing."), ("엔지니어와 조종사와 같은 전문 분야에도 도전하고 있다.", "They are also taking on specialized fields such as engineers and pilots."), ("이희정 씨는 엔지니어다.", "Ms. Lee Heejeong is an engineer."), ("대학에서 건축공학을 전공했지만, 결혼하고 오랫동안 전업주부로 지냈다.", "She majored in architectural engineering at university, but after marrying she lived as a full-time housewife for a long time."), ("집에서 희정 씨는 취미로 건물을 디자인해 보곤 했다.", "At home, Heejeong used to try designing buildings as a hobby."), ("건물을 디자인하면서 건축회사에서 일하고 싶어졌다.", "While designing buildings, she came to want to work at an architecture company."), ("그래서 엔지니어 교육원에 등록해서 건축 디자인을 공부했다.", "So she enrolled in an engineer academy and studied architectural design."), ("지금은 건축회사에서 최고의 엔지니어로 인정받고 있다.", "Now she is recognized as the best engineer at an architecture company."), ("박소민 씨는 비행기 조종사다.", "Ms. Park Somin is an airplane pilot."), ("대학을 졸업한 후 처음에는 교사가 되었다.", "After graduating from university, she first became a teacher."), ("하지만 비행기 조종사가 되기 위해 직장에 사표를 냈다.", "But she resigned from her job in order to become an airplane pilot."), ("쉬운 결정은 아니었지만, 자기 발전을 위해 사표를 내고 항공대학에 진학했다.", "It was not an easy decision, but for her own development she resigned and entered an aviation university."), ("지금은 항공사에서 조종사로 근무하고 있다.", "Now she works as a pilot at an airline."), ("부모님은 결혼하라고 하지만 소민 씨는 아직 결혼하고 싶은 생각이 없다.", "Her parents tell her to marry, but Somin does not yet have the desire to marry."), ("현재의 생활에 만족한다.", "She is satisfied with her present life.")]
_C_WORDS = ["가사", "검사", "과거", "교육원", "글", "꿈", "노동", "도전", "발전", "선호", "양육", "엔지니어", "역할", "작가", "조종사", "지위", "~직", "진출", "진학", "판사", "현재"]
_WY = [("올해의 여성 이길여 총장", "Woman of the Year: President Lee Gilyeo"), ("이길여 경원대 총장은 서울일보가 뽑은 올해의 여성이다.", "Gyeongwon University President Lee Gilyeo is the Woman of the Year chosen by the Seoul Daily."), ("이 총장은 천구백삼십이 년 전북 옥구에서 태어났다.", "President Lee was born in Okgu, Jeonbuk in 1932."), ("이리여중과 이리여고를 졸업하고 서울대 의대에 진학했다.", "She graduated from Iri Girls’ Middle and High Schools and entered Seoul National University’s medical school."), ("그리고 천구백오십육 년 일본 니혼대에서 의학 박사학위를 받았다.", "And in 1956 she received a doctorate in medicine from Nihon University in Japan."), ("천구백오십팔 년 이길여 산부인과를 열어 생활이 어려운 여성에게 무료 진료를 시작했다.", "In 1958 she opened the “Lee Gilyeo Obstetrics and Gynecology Clinic” and started free treatment for women in difficult circumstances."), ("천구백칠십팔 년 모든 재산을 털어 길의료재단을 만들었다.", "In 1978 she gave up all her assets and created the Gil Medical Foundation."), ("천구백구십팔 년 가천 의대를 열고 이천 년에는 경원대 총장이 되었다.", "In 1998 she opened Gachon Medical School and in 2000 became president of Gyeongwon University."), ("현재 가천대 총장으로 재직중이다.", "She is currently serving as president of Gachon University.")]
L9 = lesson(
    "Ch 43 · Topic C: The status and roles of women are changing (여성의 지위와 역할이 변하고 있다)",
    "여성의 지위와 역할 · 전문직 여성 · 엔지니어 · 조종사 · 올해의 여성 · 북한 여성",
    requires=[],
    cards=[
        card("Topic C: The status and roles of women are changing (여성의 지위와 역할이 변하고 있다)",
             "The following excerpt is from a women’s magazine. (The English is mine; the book gives none.)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists –곤 하다 and 반면(에)/–(으)ㄴ/는 반면(에) (see the grammar).", tables=_words(_C_WORDS)),
        card("북한에서는",
             "In North Korea, the social status and roles of women radically changed after Korea was liberated from Japanese occupation in 1945. In 1946 North Korea passed a Sex Equality Law, and the 1972 constitution asserts that “women hold equal social status and rights with men.” Women are expected to participate fully in the labor force outside the home because of the country’s labor shortage. Women in North Korea are supposed to devote eight hours a day to work, eight hours to study (presumably, the study of 주체사상 and Kim Il Sung-ism), and eight hours to rest and sleep. Women who have three or more children work only six hours a day but receive a full, eight-hour workday salary."),
        card("Follow-up 2 (Reading): Woman of the Year",
             "The following excerpt is from a news article about a woman chosen as “Woman of the Year”; the book asks you to fill in a table in English (year mentioned / biographical information; the 1978 row is done for you). The book glosses 이루다: to achieve. The article is the book’s with the years spelled out (the book’s “이리여중·고” is written 이리여중과 이리여고); the English is mine.",
             examples=passage(_WY)),
        card("The table filled in (mine)", "",
             tables=[table(["Year mentioned", "Biographical information (mine)"], [["1932", "Born in Okgu, Jeonbuk"], ["1956", "Received a doctorate in medicine from Nihon University in Japan"], ["1958", "Opened an obstetrics and gynecology clinic and started free treatment for women in difficult circumstances"], ["1978", "Donated her assets to found a medical foundation"], ["2000–present", "Became president of Gyeongwon University in 2000 (opened Gachon Medical School in 1998); currently president of Gachon University"]])]),
        card("Activities left out", "The presentation steps of Topic C (SMART Board) and Follow-up 1 (listening to presentations in which students describe hopes for a future career, noting the future career and the reason) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT + _WY, k=3)
        + [M("What did women mainly do in the past?", "Raised children and did housework at home", ["Worked as pilots", "Ran companies", "Studied abroad"], "자녀를 양육하거나 가사 노동."), M("What is increasing these days?", "Professional women entering society", ["Housewives", "Schools", "Factories"], "전문직 여성들."), M("What did Lee Heejeong major in?", "Architectural engineering", ["Medicine", "Aviation", "Law"], "건축공학."), M("What did Heejeong do as a hobby at home?", "Design buildings", ["Cook", "Paint", "Sing"], "건물을 디자인해 보곤 했다."), M("What was Park Somin first?", "A teacher", ["A pilot", "An engineer", "A doctor"], "처음에는 교사."), M("What did Somin do in order to become a pilot?", "Resigned from her job and entered an aviation university", ["Married a pilot", "Moved abroad", "Joined the military"], "사표를 내고 항공대학에 진학."), M("What does Somin think about marriage?", "She does not yet want to marry", ["She wants to marry soon", "She is already married", "She dislikes her parents"], "결혼하고 싶은 생각이 없다."), M("What did President Lee Gilyeo do in 1978?", "Donated all her assets and created a medical foundation", ["Opened a clinic", "Became a university president", "Was born"], "모든 재산을 털어."),
           F("과거에 여성은 주로 자녀를 ___하거나 가사 노동을 했다. (raise)", "양육", ["진학", "도전"], "양육."), F("전문 분야에도 ___하고 있다. (take on a challenge)", "도전", ["선호", "진출"], "도전."), F("그녀는 비행기 ___다. (pilot)", "조종사", ["판사", "작가"], "조종사."), F("대학원에 ___하기로 했어요. (advance to)", "진학", ["진출", "발전"], "진학."), F("현대 사회에서 여성들의 ___가 높아지고 있다. (status)", "지위", ["역할", "노동"], "지위."),
           read_q("여성의 지위와 역할이 변하고 있다"), read_q("전문직 여성들이 증가하고 있다"), read_q("이희정 씨는 엔지니어입니다"), read_q("박소민 씨는 비행기 조종사입니다"), read_q("올해의 여성")]
    ),
)

# ================================================================== L10 Grammar C: 반면(에)
_BM1 = [("백화점은 물건이 비쌉니다. 반면 품질이 좋습니다.", "The department store merchandise is expensive. On the other hand, its quality is good."), ("고속철도는 비쌉니다. 반면에 빠릅니다.", "An express train is expensive. On the other hand, it’s fast.")]
_BM2 = [("백화점은 물건이 비싼 반면 품질이 좋습니다.", "The department store merchandise is expensive. On the other hand, its quality is good."), ("고속철도는 비싼 반면에 빠릅니다.", "An express train is expensive. On the other hand, it’s fast."), ("승화는 수학을 잘하는 반면 영어는 잘 못해요.", "Seunghwa is good at math. On the other hand, she is not good at English.")]
_BM3 = [("그 대학교는 좋아요.", "그 대학교는 좋은 반면 학비가 비싸요.", "That university is good; on the other hand, the tuition is expensive.")]
_BMA = [("이 아파트는 전망이 좋은 반면 교통이 불편해요.", "This apartment has a good view; on the other hand, the transportation is inconvenient."), ("저는 고등학교 때 과학을 잘한 반면 수학은 못했어요.", "In high school I was good at science; on the other hand, I was bad at math."), ("박 일병은 한국 영화를 자주 보는 반면 한국 드라마는 안 봐요.", "PFC Park often watches Korean movies; on the other hand, he does not watch Korean dramas.")]
_BMB = [("백화점은 물건이 비싼 반면 품질이 좋아요.", "Department stores have expensive goods; on the other hand, the quality is good."), ("저는 운동을 잘하는 반면 노래는 못해요.", "I am good at sports; on the other hand, I can’t sing."), ("송 상병은 주말에 늦잠을 자는 반면 평일에는 일찍 일어나요.", "Cpl. Song sleeps in on weekends; on the other hand, he gets up early on weekdays.")]
_BMC = [("한국의 여름은 덥다. 반면에 겨울은 춥다.", "Korean summers are hot. On the other hand, winters are cold."), ("남자 농구는 계속 이긴 반면에 여자 농구는 계속 졌다.", "Men’s basketball kept winning, whereas women’s basketball kept losing.")]
L10 = lesson(
    "Ch 43 · Grammar C: 반면(에), on the other hand",
    "반면(에) · -(으)ㄴ/는 반면(에) · 백화점은 비싼 반면 품질이 좋다",
    requires=[],
    cards=[
        card("A sentence connector",
             "반면(에) is a sentence connector used to connect two contrasting concepts or ideas, and it can be translated as on the other hand. For example (the English is the book’s):",
             examples=passage(_BM1)),
        card("A verb connector too",
             "Note that 반면(에) is placed at the beginning of the second sentence. 반면(에) can also be used as a verb connector (or conjunctive ending). In this case, 반면(에) is preceded by an attributive form. For example (the English is the book’s):",
             examples=passage(_BM2)),
        card("Follow-up 1 (Speaking and listening): the model",
             "Student A makes a sentence using –(으)ㄴ/는 반면(에), combines it with a sentence from Table A, and says the completed sentence aloud to Student B; Student B translates it back and then uses the cues from Table B. Table A: 이 아파트는 전망이 좋아요; 저는 고등학교 때 과학을 잘 했어요; 박 일병은 한국 영화를 자주 봐요. Table B: 백화점은 물건이 비싸요; 저는 운동을 잘 합니다; 송 상병은 주말에 늦잠을 자요. The book’s model (the English is mine):",
             examples=passage([(_BM3[0][1], _BM3[0][2])])),
        card("My completed sentences (mine)", "My own contrasting halves for the six cues (the English is mine):", examples=passage(_BMA + _BMB)),
        card("More examples from the Core Vocabulary", "The book’s examples for 반면(에) in the Core Vocabulary (the English is mine):", examples=passage(_BMC)),
        card("Activities left out", "Follow-up 2 (listening to four statements that contrast two different aspects of an object using 반면(에), and writing the two contrasting aspects in English) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_BM1 + _BM2 + [(_BM3[0][1], _BM3[0][2])] + _BMA + _BMB + _BMC, k=3)
        + [M("What does 반면(에) mean?", "on the other hand; whereas", ["because", "therefore", "if"], "The book’s note."), M("Where is the sentence connector 반면(에) placed?", "At the beginning of the second sentence", ["At the end of the first sentence", "In the middle of a word", "Before the topic"], "The book’s note."), M("What precedes 반면(에) as a verb connector?", "An attributive form", ["A noun alone", "A past stem", "A particle ~에서"], "The book’s note."), M("What does 고속철도는 비싼 반면에 빠릅니다 mean?", "An express train is expensive; on the other hand, it is fast", ["An express train is cheap and slow", "An express train is not fast", "Trains are expensive because they are fast"], "The book’s example."), M("What does 승화는 수학을 잘하는 반면 영어는 잘 못해요 mean?", "Seunghwa is good at math; on the other hand, she is not good at English", ["Seunghwa is good at English", "Seunghwa dislikes math", "Seunghwa studies both"], "The book’s example."),
           F("백화점은 물건이 비싼 ___ 품질이 좋습니다. (on the other hand)", "반면", ["동안", "때문에"], "반면."), F("한국의 여름은 덥다. ___ 겨울은 춥다. (on the other hand)", "반면에", ["그래서", "그리고"], "반면에."), F("남자 농구는 계속 이긴 ___ 여자 농구는 계속 졌다. (whereas)", "반면에", ["때문에", "후에"], "반면에."), F("저는 운동을 잘하는 반면 노래는 ___. (can’t)", "못해요", ["잘해요", "좋아해요"], "못하다."), F("그 대학교는 좋은 ___ 학비가 비싸요. (on the other hand)", "반면", ["때문", "동안"], "반면."),
           read_q("백화점은 물건이 비싼 반면 품질이 좋습니다"), read_q("고속철도는 비싼 반면에 빠릅니다"), read_q("승화는 수학을 잘하는 반면 영어는 잘 못해요"), read_q("한국의 여름은 덥습니다 반면에 겨울은 춥습니다"), read_q("그 대학교는 좋은 반면 학비가 비싸요")]
    ),
)

# ================================================================== L11 Grammar D: -곤 하다
_GN1 = [("저는 잠이 올 때 커피를 마셔요.", "I drink coffee when I am sleepy."), ("저는 잠이 올 때 커피를 마시곤 해요.", "I normally drink coffee when I am sleepy.")]
_GN2 = [("추울 때 따뜻한 코코아를 마시곤 해요.", "I normally drink hot chocolate when it is cold."), ("주말에는 도서관에 가곤 해요.", "I routinely go to the library on weekends.")]
_GN3 = [("추울 때 따뜻한 코코아를 마시곤 했어요.", "(In the past) I normally drank hot chocolate when it was cold. / I used to drink hot chocolate when it was cold."), ("주말에는 도서관에 가곤 했어요.", "(In the past) I routinely went to the library on weekends. / I would go to the library on weekends.")]
_GN4 = [("아침에 구름이 끼면 오후에 비가 오곤 했다.", "When it got cloudy in the morning, it would rain in the afternoon."), ("방학 때 할아버지 댁에 가곤 했어요.", "I used to go to my grandfather’s house during class break."), ("수미는 주말에 피아노를 치곤 해요.", "More often than not, Sumi plays the piano on weekends.")]
_GNR = [("주말에는 시골 농장에 갔어요.", "농장에 가곤 했어요.", "I used to go to the country farm on weekends."), ("해마다 진해에 벚꽃놀이를 가요.", "해마다 진해에 벚꽃놀이를 가곤 해요.", "I often go to the cherry blossom viewing at Jinhae every year."), ("설날에 할아버지께서 세뱃돈을 주셨어요.", "설날에 할아버지께서 세뱃돈을 주시곤 했어요.", "On New Year’s Day, my grandfather used to give me New Year’s money."), ("겨울에는 기온이 영하로 떨어져요.", "겨울에는 기온이 영하로 떨어지곤 해요.", "In winter, the temperature often drops below zero."), ("가끔 인사동에 전통 차를 마시러 가요.", "가끔 인사동에 전통 차를 마시러 가곤 해요.", "I sometimes go to Insa-dong to drink traditional tea (habitually)."), ("어렸을 때는 감기에 자주 걸렸어요.", "어렸을 때는 감기에 자주 걸리곤 했어요.", "When I was young, I used to catch colds often."), ("제 프랑스 친구는 가끔 한국어로 말해요.", "제 프랑스 친구는 가끔 한국어로 말하곤 해요.", "My French friend sometimes speaks in Korean.")]
_GNP = [("제가 어렸을 때 조부모님은 시골에 사셨습니다.", "When I was young, my grandparents lived in the countryside."), ("그래서 저는 부모님과 함께 주말에 조부모님을 뵈러 시골에 가곤 했습니다.", "So I used to go to the countryside with my parents on weekends to see my grandparents."), ("저는 할아버지를 따라 동네 강가에 낚시를 가곤 했습니다.", "I used to go fishing at the riverside in the village, following my grandfather."), ("집에 오면 할머니는 우리가 잡은 물고기로 맛있는 찌개를 끓여 주시곤 했습니다.", "When we came home, my grandmother used to boil a delicious stew with the fish we had caught."), ("지금은 두 분 다 돌아가셨습니다.", "Now both of them have passed away."), ("가끔 부모님과 함께 조부모님에 대해 이야기하곤 합니다.", "Sometimes I talk about my grandparents with my parents.")]
_GNX = [("저는 고등학교에 다닐 때 주말마다 암벽등반을 하곤 했어요.", "When I attended high school, I used to go rock climbing every weekend."), ("어머니가 저녁 늦게까지 일하셔서 아버지가 요리를 하시곤 했어요.", "My mother worked until late in the evening, so my father used to cook."), ("형제가 많아서 어렸을 때 자주 싸우곤 했어요.", "I had many siblings, so we used to fight often when we were young.")]
L11 = lesson(
    "Ch 43 · Grammar D: the auxiliary verb –곤 하다 for common or routine occurrences",
    "-곤 하다 · -곤 했다 · 주말에는 도서관에 가곤 해요 · 어렸을 때 · 습관 · used to",
    requires=[],
    cards=[
        card("Compare the two sentences",
             "Compare the following two sentences and their English meanings (the English is the book’s).",
             examples=passage(_GN1)),
        card("What the second sentence implies",
             "The first sentence implies that, without exception, the speaker drinks coffee when he is sleepy, whereas the second sentence implies that the speaker routinely (or more often than not) drinks coffee when he is sleepy. This is because of the presence of the auxiliary verb –곤 하다, which is used to express an action/event that commonly or routinely occurs or occurred. Thus, depending on the context, –곤 하다 can be loosely translated as commonly, routinely, regularly, generally, normally, habitually, usually, often, or more often than not. For example (the English is the book’s):",
             examples=passage(_GN2)),
        card("The past: –곤 했다",
             "–곤 했다 is used for the past common or regular occurrences of an action or event. For example (the English is the book’s):",
             examples=passage(_GN3)),
        card("Conditions",
             "Here –곤 했다 can also be translated as used to or would. Note that –곤 하다 involves multiple occurrences of an action/event over a period of time; –곤 하다 does not work with a stative verb or with a one-time action/event.\n\nExpressing an action/event that commonly or routinely occurs or occurred: action verb stem + 곤 하다/했다. More examples (the English is the book’s):",
             examples=passage(_GN4)),
        card("Follow-up 3 (Writing): rewrite with –곤 하다",
             "Rewrite the underlined parts of the following sentences using −곤 하다, and translate the sentence (the first is done for you). The sentences are the book’s; the rewrites and the English are mine.",
             tables=[table(["Sentence", "With –곤 하다 (mine)", "English (mine)"], [[a, b, c] for a, b, c in _GNR], say=[0, 1])]),
        card("Follow-up 4 (Reading): a college student’s passage",
             "The following passage is written by a college student; the book asks you to write a title in Korean and to translate four underlined parts (a: 조부모님을 뵈러 시골에 가곤 했습니다; b: 낚시를 가곤 했습니다; c: 찌개를 끓여 주시곤 했습니다; d: 조부모님에 대해 이야기하곤 합니다; the book glosses 강가: riverside; 물고기: fish). The passage is the book’s; the English is mine. A title (mine): 시골에 계신 조부모님 (My grandparents in the countryside).",
             examples=passage(_GNP)),
        card("Follow-up 5 (Writing and reading): guess who it is",
             "Think about three things you did routinely or habitually in the past, write a sentence on each with –곤 했다, give them to the teacher; the teacher mixes them up and the class guesses who wrote each. The book’s examples (the English is mine):",
             examples=passage(_GNX)),
    ],
    exercises=uniq(
        _tr(_GN1 + _GN2 + _GN3 + _GN4 + [(b, c) for a, b, c in _GNR] + _GNP + _GNX, k=3)
        + [M("What does –곤 하다 express?", "A commonly or routinely occurring action/event", ["A one-time event", "A wish", "A command"], "The book’s note."), M("What does –곤 했다 mean in the past?", "Used to; would", ["Just did once", "Wanted to", "Had to"], "The book’s note."), M("Does –곤 하다 work with a stative verb?", "No", ["Yes", "Only in the past", "Only in questions"], "The book’s note."), M("Does –곤 하다 work with a one-time event?", "No", ["Yes", "Only in the past", "Only with 가다"], "The book’s note."), M("What does 주말에는 도서관에 가곤 해요 mean?", "I routinely go to the library on weekends", ["I went to the library once", "I will go to the library", "I do not go to the library"], "The book’s example."), M("What does 방학 때 할아버지 댁에 가곤 했어요 mean?", "I used to go to my grandfather’s house during class break", ["I will go to grandfather’s house", "I went once", "I stayed home"], "The book’s example."),
           F("저는 잠이 올 때 커피를 마시___ 해요. (normally)", "곤", ["고", "면"], "-곤 하다."), F("주말에는 도서관에 가___ 했어요. (used to)", "곤", ["고", "면"], "-곤 했다."), F("어렸을 때는 감기에 자주 걸리___ 했어요. (used to)", "곤", ["고", "며"], "-곤 했다."), F("수미는 주말에 피아노를 치___ 해요. (more often than not)", "곤", ["고", "면"], "-곤 하다."), F("방학 때 할아버지 댁에 가곤 ___. (used to)", "했어요", ["해야 해요", "하세요"], "-곤 했다."),
           read_q("저는 잠이 올 때 커피를 마시곤 해요"), read_q("주말에는 도서관에 가곤 해요"), read_q("방학 때 할아버지 댁에 가곤 했어요"), read_q("어렸을 때는 감기에 자주 걸리곤 했어요"), read_q("할아버지를 따라 낚시를 가곤 했습니다")]
    ),
)

# ================================================================== L12 Activities C + self-eval
_WO = [("사회에 진출하는 여성 늘어", "More women entering society"), ("현대 사회에서 여성의 지위가 변화되고 있다.", "The status of women in modern society is changing."), ("집안일에 대한 부담이 줄어들고 교육을 받을 기회가 많아지면서 많은 여성이 사회활동에 참여하고 있다.", "As the burden of housework decreases and opportunities to receive education increase, many women are participating in social activities."), ("그리고 여성들의 직업이 다양해지고 있다.", "And women’s occupations are becoming diverse."), ("예전에는 여성의 직업은 교사나 간호사가 대부분이었다.", "In the past, most women’s occupations were teacher or nurse."), ("그렇지만 요즘에는 판사, 검사, 엔지니어, 조종사, 작가 등 다양한 분야에 도전하는 여성들이 증가하고 있다.", "However, these days the number of women taking on various fields such as judge, prosecutor, engineer, pilot and writer is increasing.")]
L12 = lesson(
    "Ch 43 · Activities C: women entering society · and self-evaluation",
    "사회에 진출하는 여성 · 직업 · 올해의 여성 후보 추천 · 자기 평가",
    requires=[],
    cards=[
        card("Activity 3 (Reading): occupational changes for women",
             "The following news article excerpt is about occupational changes for women; the book asks you to fill in a table in English (causes of changes; jobs now held by women). The excerpt is the book’s; the English is mine.",
             examples=passage(_WO)),
        card("The table filled in (mine)", "",
             tables=[table(["Column", "Answer (mine)"], [["Causes of changes", "The burden of housework has decreased; there are more opportunities to receive education"], ["Jobs now held by women", "Judge, prosecutor, engineer, pilot, writer (in the past, mostly teacher or nurse)"]])]),
        card("Activity 4 (Listening, speaking and writing): Woman of the Year",
             "You are a board member who has been chosen to select the “Woman of the Year”: you listen to the profiles of two women (Woman A: 이영애 씨; Woman B: 전수미 씨; audio), write the biographical information, educational background and volunteer work in English, exchange the information with a student from the other group in Korean, choose a winner and present the reasons. In step c you recommend a candidate for next year and write a short letter of recommendation in Korean. This is an audio and group activity and is left out."),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with.\n\n"
             "Now I am able to: identify major religions and beliefs in Korea; discuss volunteer work; understand the lives of foreigners in Korea and their typical concerns; discuss the social status and role of women in Korea; and talk about more occupations.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; ~ (도)중에/(–는/던) (도)중에 (in the middle of doing something); the sentence ending –(으)ㄴ/는데(요); 반면(에) (on the other hand; whereas; while); the auxiliary verb −곤 하다 for common or routine occurrences of an action/event; and the Sino-Korean syllables within 천주교 (天主敎), 대륙 (大陸), and 전문직 (專門職)."),
        card("Activities left out", "Activity 1 (SMART Board) and Activity 2 (listening to three conversations between a man and a woman at a class reunion and noting the woman’s occupation and the reason) are audio and computer activities."),
    ],
    exercises=uniq(
        _tr(_WO, k=3)
        + [M("What changed in modern society?", "The status of women", ["The weather", "The language", "The calendar"], "여성의 지위."), M("What has decreased for women?", "The burden of housework", ["Education", "Jobs", "Salaries"], "집안일에 대한 부담."), M("What has increased for women?", "Opportunities to receive education", ["Housework", "Isolation", "Taxes"], "교육을 받을 기회."), M("What were most women’s jobs in the past?", "Teacher or nurse", ["Judge or pilot", "Engineer", "Writer"], "교사나 간호사."), M("Which job is NOT listed among the new jobs?", "Teacher", ["Judge", "Pilot", "Writer"], "판사, 검사, 엔지니어, 조종사, 작가."), M("What should you do if you tick “No” in the self-evaluation?", "Review on your own, study with a partner, tell your advisor or team leader", ["Skip it", "Retake the course", "Nothing"], "The book’s advice."),
           F("집안일에 대한 ___이 줄어들었다. (burden)", "부담", ["의존", "선호"], "부담."), F("여성들의 직업이 ___해지고 있다. (diverse)", "다양", ["완벽", "유창"], "다양하다."), F("사회에 ___하는 여성이 늘고 있다. (enter)", "진출", ["진학", "의존"], "진출."), F("예전에는 여성의 직업은 교사나 ___가 대부분이었다. (nurse)", "간호사", ["판사", "검사"], "간호사."), F("판사, 검사, 엔지니어 등 다양한 분야에 ___하는 여성들이 증가하고 있다. (take on)", "도전", ["오해", "기부"], "도전."),
           read_q("사회에 진출하는 여성 늘어"), read_q("여성의 지위가 변화되고 있습니다"), read_q("집안일에 대한 부담이 줄어들었습니다"), read_q("판사와 검사와 엔지니어와 조종사와 작가"), read_q("다양한 분야에 도전하는 여성들이 증가하고 있습니다")]
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
    "Ch 43 · Core vocabulary",
    "주요 단어 · 종교 · 자원봉사 · 외국인 · 여성의 지위 · 직업 · 곤 하다",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. 아프리카, 엔지니어 and 유럽 are listed also as loan words; the last section lists the Sino-Korean related words of 대륙, 전문직 and 천주교 as the book gives them.\n\n"
             "The example sentences with digits are respelled in Hangul (100만 원 → 백만 원; 5명의 → 다섯 명의)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 양로원 mean?", "a nursing home", ["an orphanage", "a hospital", "a school"], "養老院."), M("What does 고아원 mean?", "an orphanage", ["a nursing home", "a church", "a temple"], "孤兒院."), M("What does 의사소통 mean?", "communication", ["misunderstanding", "dependence", "grammar"], "意思疎通."), M("What does 오해 mean?", "misunderstanding", ["communication", "perfection", "custom"], "誤解."), M("What does 지위 mean?", "status", ["a role", "labor", "a dream"], "地位."), M("What does 진출 mean?", "advance; entry into", ["retreat", "preference", "challenge"], "進出."), M("What does 선호 mean?", "preference", ["development", "challenge", "labor"], "選好."), M("What does 판사 mean?", "a judge", ["a prosecutor", "a lawyer", "a writer"], "判事."),
           F("자원봉사 활동은 아주 ___ 있는 일입니다. (meaning)", "의미", ["오해", "의존"], "의미 있다."), F("성인이 된 다음에는 부모님께 너무 ___하지 마세요. (depend)", "의존", ["도전", "진출"], "의존하다."), F("제 ___은 의사가 되는 거예요. (dream)", "꿈", ["글", "역할"], "꿈."), F("가정에서 부모의 ___이 아주 중요합니다. (role)", "역할", ["꿈", "지위"], "역할."), F("연말에는 여러 종교 단체들이 ___ 행사를 많이 엽니다. (charity)", "자선", ["기타", "기도"], "자선."),
           read_q("주요 단어"), read_q("양로원"), read_q("의사소통"), read_q("지위"), read_q("조종사")]
    ),
)

UNIT = unit("Semester 2 · Unit 11 · Chapter 43: Religion and Society (종교와 사회)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])

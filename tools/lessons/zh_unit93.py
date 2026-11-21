"""Unit 93: Lesson 28 (China's Youth), Presentation 3 vocabulary list and the Area Studies page on the post-'70s, '80s, '90s and '00s generations and the eras they grew up in.
The Area Studies text is the book's English text; the list of references (web addresses) and the pictures are not included."""
from zh_auto import *
from zh_l28_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣亩" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["前途", "目标", "材料"]

L1 = vocab_lesson("Lesson 28 Presentation 3 vocabulary", "19 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

A70 = ("The Post-’70s Generation (七零后, Qīlíng-hòu) is the generation of people born between 1970 and 1979 in Mainland China, during a dramatic transition period, from the Cultural Revolution led by Mao Zedong (1966-1976) to the “Economic Reform” led by Deng Xiaoping in 1978. The 1970s were a time of centralized economy and extreme scarcity. People lived a frugal life. Workers received low wages from the government and shopped for basic daily supplies such as rice, meat and fabric with ration tickets. Many households had access to radio but had no television. Common people had no understanding of the outside world.\n\n"
       "Family planning was not fully implemented at this time. Most post-’70s generation have 2–3 siblings. After 1978, universities reopened and accepted students through college entrance exams, and China started to value academics again. At the time, less than 10% of examinees were accepted to colleges. Growing up between the Cultural Revolution and the era of Reform and Opening-Up, the post-’70s generation are half modern and half traditional. They pursue stable work (“iron rice bowl”) and cherish their jobs. They work hard to improve their own lives and the society. They are pragmatic and conservative.")
A80 = ("The Post-’80s Generation (八零后, Bālíng-hòu) is the generation of people whose members were born between 1980 and 1989 in Mainland China, after the introduction of the one-child policy. They are the first to grow up entirely within the reformist era. They have been characterized by their optimism for the future, excitement for consumerism, entrepreneurship, and acceptance of their historic role in transforming modern China into an economic superpower.\n\n"
       "These people are also distinguished by their increased access to digital media such as computers, MP3 players and mobile phones. The post-’80s generation in China often experience a generation gap with their elders. While their parents lived during an era of famine, political instability and lack of proper education because of the Cultural Revolution, they lived in an environment of tremendous economic growth and social change, greater technology, and rigorous educational standards. This gap is noticeable in purchasing habits, career pursuits, and family interactions. Furthermore, these young adults have been indirectly affected by government restrictions to the Internet. They are also affected by China’s large socioeconomic divide between urban and rural residents and societal problems resulting from modernization.\n\n"
       "The post-’80s generation experienced the end of government funding of college educations, job assignments for graduates and subsidized housing. Upon entering the workplace, they had to face financial pressures such as marriage and home purchases. The majority of the post-’80s generation were more willing to find jobs that are stable, with strong continuity and matching what they studied in school, and that can satisfy their parents. They believed government agencies, institutions, and state-owned enterprises had more advantages in social resources and development prospects. Many of them have not yet had a strong entrepreneurial impulse.")
A90 = ("The Post-’90s Generation (九零后, Jiǔlíng-hòu) is the generation of people born between 1990 and 1999. They are the second generation of Chinese people to grow up without siblings and the first generation to be born after the Tiananmen protests. Unlike the post-’80s generation, who witnessed a glimpse of pre-affluent China in the late 1980s and 1990s, they have not experienced historical and political turmoil, and have not experienced major economic fluctuations. The post-’90s generation were born in the era of rapid development of information and innovation, so they pursue individuality and freedom. They grew up being appreciated and encouraged since they were young. They are alleged to have traits that are similar to the post-’80s generation, such as “Little Emperor Syndrome” and a knack for information technology and capitalism, but in a more highly developed way.\n\n"
       "In an era where mainstream social thought is more dispersed, factions are more diverse, and ideas are updated more rapidly, they are more focused on their own hobbies in their work and prefer to do what they want to do and what they are good at. They want to find jobs that they like, that are challenging, and where they can realize their self-worth, so they become people who do not like to “put up with” just any job.\n\n"
       "The post-’90s generation are also alleged to have less of a sense of hierarchy in the workplace and more of a sense of individuality compared to older generations. With financial support from their parents, the post-’90s generation are more inclined to be able to use their personal skills and talents. They prefer jobs that can satisfy personality development and being appreciated by employers. Even though civil servants and public institutions are still good choices and attract many post-’90s generation applicants, many also choose private enterprise, entrepreneurship, going abroad or working alone. Their advantage lies in their active thinking, natural sensitivity, and dependence on new things, especially the Internet. They don’t like too much restraint, suppression, or repeated mechanized labor, and they respect entrepreneurial heroes. They will freely switch to a new job with a better working environment and room for development or leave to start their own business.")
A00 = ("The Post-’00s Generation (零零后, Línglíng-hòu) is the generation of people born after the year 2000, in an era that had the highest GDP per capita and lowest birth rate and enjoyed the most abundance in China. They are the “mobile internet generation”. Many of them have opportunities to visit other countries; and they are able to learn about other cultures through the Internet. Mostly born into 421-format families, they may not be a single child anymore.\n\n"
       "Surveys indicate that most of them identify their interests and hobbies early and know how to use online resources to deepen their knowledge of a specific field. They value in-depth understanding of a certain field much more than consumption or career growth, which is a departure from naked materialism. They love to connect with peers and are able to respect and adapt to different points of view. Equality is highly important for China’s post-’00s generation. Compared to previous generations, they care much less about what authorities and experts say. They study more hours than all generations before and with a more pragmatic motivation.\n\n"
       "They want jobs that can express their personal values, with a high income and a sense of style. They also want a comfortable environment and friendly and simple interpersonal relationships. They will not obey leaders absolutely but like to keep their personal ideas and opinions. They are less concerned about job stability. The job replacement rate and mobility for this group is high.")
AHL = ("A poem quoted from a Song dynasty book said, “As in the Yangtze River, the waves behind ride on the ones before: The new generation replaces the old.” The metaphor of wave has been used to describe the phenomena of how the new generation exceeds the old.\n\n"
       "On the May Fourth Youth Day in 2020, Chinese video sharing website Bilibili and a number of mainland Chinese media sites jointly launched a promotional video “Waves Behind 后浪.” The 3 minute and 52 second video shows the actor He Bing expressing envy, recognition, encouragement, and other positive emotions to the younger generation. The video caused controversy after it was aired and became a Chinese internet meme.")
L2 = lesson(
    "Lesson 28 Area Studies: the Post-’70s, ’80s, ’90s and ’00s Generations and the Eras They Grew Up In",
    "七零后 · 八零后 · 九零后 · 零零后 · 后浪 · 改革开放 · 独生子女 · 铁饭碗",
    requires=[],
    cards=[
        card("The Post-’70s Generation (七零后)", A70),
        card("The Post-’80s Generation (八零后)", A80),
        card("The Post-’90s Generation (九零后)", A90),
        card("The Post-’00s Generation (零零后)", A00),
        card("A Chinese Internet Meme: 后浪 Waves Behind", AHL),
    ],
    exercises=[
        M("Which years were the post-’70s generation born in?", "1970 to 1979", ["1960 to 1969", "1980 to 1989", "1990 to 1999"], "Born between 1970 and 1979."),
        M("What did people use to shop for rice, meat and fabric in the 1970s?", "Ration tickets", ["Credit cards", "Phones", "Online coupons"], "Ration tickets."),
        M("What did many households have access to in the 1970s?", "Radio but no television", ["Television but no radio", "Computers", "Mobile phones"], "Radio but no television."),
        M("What share of examinees were accepted to colleges after 1978?", "Less than 10%", ["About 50%", "Over 90%", "100%"], "Less than 10%."),
        M("What do the post-’70s pursue in work?", "Stable work, the “iron rice bowl”", ["Free time", "Risky start-ups", "Moving abroad"], "They pursue stable work."),
        M("What policy preceded the post-’80s generation’s birth?", "The one-child policy", ["The Cultural Revolution", "The Open Door", "The Great Leap Forward"], "After the introduction of the one-child policy."),
        M("Which digital media are named for the post-’80s?", "Computers, MP3 players and mobile phones", ["Radios", "Typewriters", "Telegrams"], "Computers, MP3 players and mobile phones."),
        M("What did the post-’80s see the end of?", "Government funding of college, job assignments and subsidized housing", ["Exams", "The Internet", "Universities"], "The end of government funding of college educations, job assignments and subsidized housing."),
        M("Which generation is called the second generation to grow up without siblings?", "The post-’90s", ["The post-’70s", "The post-’80s", "The post-’00s"], "The second generation of Chinese people to grow up without siblings."),
        M("What do the post-’90s pursue?", "Individuality and freedom", ["Only stable pay", "Only fame", "Rationing"], "They pursue individuality and freedom."),
        M("What is the post-’00s generation called?", "The “mobile internet generation”", ["The “radio generation”", "The “television generation”", "The “ration generation”"], "The mobile internet generation."),
        M("What kind of family are many post-’00s born into?", "A 421-format family", ["A 123 family", "A 55 family", "A 100 family"], "421-format families."),
        M("When was the “Waves Behind” video launched?", "May Fourth Youth Day in 2020", ["National Day 2010", "New Year 2000", "Mid-Autumn 2018"], "May Fourth Youth Day in 2020."),
        M("Which actor appears in the “Waves Behind” video?", "He Bing", ["Jackie Chan", "Jet Li", "Ma Yun"], "The actor He Bing."),
    ],
)

UNIT = unit("第二十八课 Presentation 3: 词汇, Area Studies", [L1, L2])

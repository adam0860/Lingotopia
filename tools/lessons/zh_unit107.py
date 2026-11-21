"""Unit 107: Lesson 30 (Unit 5 review), Using Chinese in Context Review Activities 1-5 (Professor Liu's email scenario, the host family's letter about Zhang Xue, the emerging-careers
questions, the Wen Chenghui script, and the Youth Center questions). Audio is not included (the Professor Liu email is audio only and is not printed); the book's answer lines are blank, so
suggestions and sample interview questions are mine and labeled. Numbers the book writes as digits are spelled out in Chinese text. The 网红 question 6 is a repeat of the courier question as printed."""
from zh_auto import *
from zh_l29_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('戴着眼镜', 1, 'zhe5')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣亩" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段里")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

# ------------------------------------------------------------------ lesson 1: acts 1 and 2
SC1 = table(["Activity", "Book’s scenario and tasks"], [
    ["Activity 1 (Listening, Reading, Writing, and Speaking)", "Scenario: You have received an email from Professor Liu, the teacher who taught you Chinese when you studied in Beijing last year. Her family is coming to the U.S. for vacation next month. This is their first trip to the U.S. and they need your recommendations for food delivery, accommodations, and transportation."],
    ["A", "Listen to the email from Professor Liu and note the information (TO, CC, Subject). The email is audio and is not printed in the book, so it is not included here."],
    ["B", "Pair up. Discuss the email from Professor Liu, and identify what help she needs for her family vacation in the U.S."],
    ["C", "In three groups, discuss how to respond to Professor Liu’s questions, and write your responses in the table (see below)."],
    ["D", "Each group presents their discussion. After the presentations, consolidate your information and write a response to Professor Liu (TO, Subject: 写给刘老师的电子邮件)."]],
    title="Using Chinese in Context Review, Activity 1: Professor Liu’s email")
GR1 = table(["", "刘老师想了解的", "怎么订", "价钱怎么样", "有什么好处"], [
    ["第一组", "住旅馆还是住爱彼迎", "", "", ""],
    ["第二组", "有哪些外卖软件", "", "", ""],
    ["第三组", "有哪些打车软件", "", "", ""]],
    title="Activity 1C: the response grid (the book leaves the last three columns blank for you to fill in)")
SC2 = table(["Activity", "Book’s scenario and tasks"], [
    ["Activity 2 (Reading, Writing and Speaking)", "Scenario: You are working in a homestay service center as a volunteer. Your service center has received a letter from a host family asking for suggestions on how to get along with a Chinese student they have recently accepted. Your supervisor tasks you to provide suggestions for the host family."],
    ["A", "Pair up, read the letter from the host family, and write down the issues described in the letter."],
    ["B", "In two groups, discuss the issues and provide at least three suggestions for improving the relationship between the host family and Zhang Xue (你们的建议: 第一组, 第二组)."],
    ["C", "Each group takes turns presenting their suggestions to the class. Select the best suggestions for the host family and submit them to the supervisor for review."]],
    title="Using Chinese in Context Review, Activity 2: the host-family letter")
LET = ("一个月前，我们从寄宿家庭服务中心接收了一名来自中国的留学生。她叫张雪，现在上高中一年级，学习成绩很好，特别是数学成绩，在全班第一名，人也非常有礼貌，我们都很喜欢她。不过，因为她的英文口语不太好，她不太愿意和我们多交流。每天晚上吃完晚饭，她就回到自己的房间看书学习，不跟我们聊天。她平时吃饭吃得很少，好像不太喜欢美国饭。有时候，我们叫她和我们在一起看电视，或是一起出去爬山，她说她很忙，需要看书，写作业。周末的时候，我们经常请一些朋友在家里聚会，她看起来不太高兴，很少和我的朋友说话。我知道中国的学生认为学习最重要，因为他们的父母希望他们考上一个好大学，可是我觉得他们来到美国，不仅要好好学习，也要有一些社交活动，多了解美国人的生活和文化，这对他们的学习也会有帮助。我想请你们给我一些建议，怎么才能让张雪很快乐地跟我们生活在一起。",
       "Activity 2A, the host family’s letter (translations mine): A month ago we received from the host-family service center an international student from China. Her name is Zhang Xue; she is now in the first year of high school and her grades are very good, especially in math, where she is first in the whole class; she is also very polite, and we all like her very much. But because her spoken English is not very good, she is not very willing to talk with us much. Every evening after dinner she goes back to her own room to read and study and doesn’t chat with us. She usually eats very little and seems not to like American food very much. Sometimes we ask her to watch TV with us or go out hiking together, and she says she is very busy and needs to read and do homework. On weekends we often invite some friends over for a party at home; she looks not very happy and rarely speaks with my friends. I know that Chinese students think study is most important, because their parents hope they will get into a good university, but I feel that when they come to America they should not only study hard but also have some social activities and learn more about Americans’ life and culture, which will also help their studies. We would like to ask you for some suggestions on how to make Zhang Xue live with us happily.")
ISS = table(["Issues in the letter (my notes; the book leaves the line blank)", "Zhang Xue’s behavior"], [
    ["Communication", "Her spoken English is not very good, so she doesn’t want to talk with the family much and doesn’t chat after dinner"],
    ["Food", "She eats very little and seems not to like American food"],
    ["Family activities", "She declines TV time and hiking, saying she is busy studying"],
    ["Social life", "At weekend parties she looks unhappy and rarely speaks with the family’s friends"]],
    title="Activity 2A: the issues")
SUG = table(["Group", "Suggestions (mine; the book leaves the table blank)"], [
    ["第一组", "多鼓励她说英文，别笑她的口语；每天找一个固定的时间和她聊聊天；问问她中国的生活和学习。"],
    ["第二组", "问问她喜欢吃什么，偶尔做一顿中餐，或者一起去中餐馆；请她参加活动，但不要勉强；聚会前先告诉她，让她可以带朋友参加。"]],
    title="Activity 2B: suggestions for the host family")
L1 = lesson(
    "Lesson 30 Using Chinese in Context Review: Professor Liu’s family visit and the host family’s letter",
    "刘老师 · 外卖软件 · 打车软件 · 爱彼迎 · 寄宿家庭 · 留学生 · 口语 · 社交活动 · 建议",
    requires=[],
    cards=[
        card("Using Chinese in Context Review, Activity 1 (Listening, Reading, Writing, and Speaking)", "A scenario about Professor Liu’s family trip to the U.S. The book prints only the scenario, the tasks and the group grid; the email itself is audio and is not included, and the answers are left blank.", tables=[SC1, GR1]),
        card("Using Chinese in Context Review, Activity 2 (Reading, Writing and Speaking)", "A scenario at a homestay service center. The letter from the host family, the issues it raises and my suggestions:", tables=[SC2, ISS, SUG], examples=[D(*LET)]),
    ],
    exercises=[
        M("Who is Professor Liu in Activity 1?", "The teacher who taught you Chinese in Beijing last year", ["Your neighbor", "A taxi driver", "A host sister"], "the book’s scenario."),
        M("What does Professor Liu’s family need recommendations for?", "Food delivery, accommodations and transportation", ["Schools only", "Jobs", "Insurance"], "the book’s scenario."),
        M("Who is Zhang Xue, according to the letter?", "A Chinese exchange student in the first year of high school", ["A college teacher", "A volunteer", "A neighbor’s daughter"], "她叫张雪，现在上高中一年级."),
        M("In which subject is Zhang Xue first in her class?", "Math", ["English", "Art", "History"], "特别是数学成绩，在全班第一名."),
        M("Why isn’t she very willing to talk with the host family?", "Her spoken English is not very good", ["She dislikes them", "She is deaf", "She is too busy singing"], "因为她的英文口语不太好."),
        M("What does she do after dinner?", "Goes back to her room to read and study", ["Watches TV with the family", "Goes hiking", "Cooks"], "每天晚上吃完晚饭，她就回到自己的房间看书学习."),
        M("How does she look at the weekend parties?", "Not very happy, rarely speaking to the guests", ["Very excited", "She leads the games", "She sings"], "她看起来不太高兴，很少和我的朋友说话."),
        M("What does the host think Chinese students should do in America, besides studying hard?", "Have social activities and learn about American life and culture", ["Stay home", "Work part-time", "Travel alone"], "也要有一些社交活动，多了解美国人的生活和文化."),
        F("我们从寄宿家庭服务中心接收了一名来自中国的留___生。", "学", ["写", "谢", "些"], "留学生: international student."),
        F("因为她的英文口___不太好，她不太愿意和我们多交流。", "语", ["与", "雨", "予"], "口语: spoken language."),
        F("他们的父母希望他们考___一个好大学。", "上", ["尚", "伤", "商"], "考上: get into (a school)."),
        F("多了解美国人的生活和文化，这对他们的学习也会有___助。", "帮", ["邦", "榜", "绑"], "帮助: help."),
    ],
)

# ------------------------------------------------------------------ lesson 2: acts 3, 4, 5
SC3 = table(["Activity", "Book’s scenario and tasks"], [
    ["Activity 3 (Reading, Speaking, and Writing)", "Scenario: You have finished your immersion program in Beijing and came back to the Chinese school in Monterey. You’ve been requested to give a presentation on emerging careers in China to the classmates who have never been to China. Your presentation will help them better understand career opportunities in China and their impact on people’s lives."],
    ["A", "In three groups, discuss these three emerging careers in China, and their impact on people’s lives and society. You can use the information that follows for reference."],
    ["B", "Each group takes turns presenting and discussing their findings. After presenting, consolidate all the information to make a report. Submit the report to your teacher."]],
    title="Using Chinese in Context Review, Activity 3: emerging careers")
Q3 = [
    ("第一组 介绍“快递小哥”", "Group 1, introduce the “courier guys” (translations mine)."),
    ("中国有多少“快递小哥”？哪些地方快递员比较多？", "1. How many “courier guys” are there in China? In which places are there more couriers?"),
    ("他们男的多还是女的多？他们的年龄有多大？", "2. Are there more men or more women among them? How old are they?"),
    ("他们的工作情况怎么样？什么时候最忙？他们每月能赚多少钱？", "3. How is their work situation? When are they busiest? How much can they earn each month?"),
    ("除了送件，他们有收件的服务吗？", "4. Besides delivering items, do they offer a pickup service?"),
    ("快递员的服务怎么样？顾客的打分好不好？", "5. How is the couriers’ service? Are the customers’ ratings good?"),
    ("快递员的工作对社会有什么意义？", "6. What is the significance of couriers’ work to society?"),
    ("第二组 介绍“网红”", "Group 2, introduce the “internet celebrities.”"),
    ("你知道哪些有名的“网红”？他们是什么样的“网红”？", "1. Which famous “internet celebrities” do you know? What kind of “internet celebrities” are they?"),
    ("他们的粉丝有多少？", "2. How many fans do they have?"),
    ("他们为什么受到很多粉丝的喜爱？", "3. Why are they loved by so many fans?"),
    ("他们每月能赚多少钱？他们可以用什么方法来赚钱？", "4. How much can they earn each month? By what methods can they make money?"),
    ("“网红”对社会有什么影响？", "5. What influence do “internet celebrities” have on society?"),
    ("快递员的服务怎么样？顾客的打分好不好？", "6. (printed in the book as a repeat of the courier question) How is the couriers’ service? Are the customers’ ratings good?"),
    ("第三组 介绍“电竞员”", "Group 3, introduce the “e-sports players.”"),
    ("中国有多少职业电竞员？他们的年龄一般多大？", "1. How many professional e-sports players are there in China? About how old are they?"),
    ("做职业电竞员的要求是什么？为什么说做电竞员很有竞争力？", "2. What are the requirements for being a professional e-sports player? Why is it said that being an e-sports player is very competitive?"),
    ("他们每月能赚多少钱？他们可以用什么方法来赚钱？", "3. How much can they earn each month? By what methods can they make money?"),
    ("你知道哪些有名的电竞选手？他们玩什么游戏最有名？", "4. Which famous e-sports players do you know? Which game are they most famous for playing?"),
    ("电竞员对社会有什么影响？", "5. What influence do e-sports players have on society?")]
SC4 = table(["Activity", "Book’s scenario and tasks"], [
    ["Activity 4 (Listening, Reading, Writing, and Speaking)", "Scenario: You are studying Chinese in Beijing University. The Student Union has invited Wen Chenghui, a post-90s entrepreneur and the founder of “Liwushuo,” to talk to the students in Beijing University. Your teacher asks you and your classmates to come up with some questions that you will use to interview Wen Chenghui after his talk."],
    ["A", "Listen to the recording and write the essential information you hear."],
    ["B", "Pair up and summarize the details of the recording with your partner. Read the script, if necessary."],
    ["C", "With your partner, create at least five interview questions that focus on Wen Chenghui’s entrepreneurial story (six numbered lines)."],
    ["D", "After creating the interview questions, your partner plays the role of Wen Chenghui. Interview your partner with the questions you created (six numbered answer lines)."]],
    title="Using Chinese in Context Review, Activity 4: Wen Chenghui")
WEN = ("这个身材很瘦，戴着眼镜，说起话来像个大男孩的温城辉，很难让人想到他就是“礼物说”的创始人。温城辉十六岁就开始创业，那时候他还在读高中，他自己做了一本杂志在学校里卖，结果赚了好几千块钱。读大一时，他和朋友成立了一个工作室，卖手画的明信片，一共卖出一百万张，赚了十多万。后来，他的公司做出一个叫“礼物说”的手机软件，用户下载软件后就可以买到自己喜欢的礼物。这个软件非常成功，不到四个月，就有两百多万人下载，卖出去的礼物有一千万元。当大家问温城辉为什么会这么成功，他说九零后创业最大的优势是“最懂用户”。",
       "Activity 4, the script “The hottest post-90s entrepreneur” (最火的九零后创业者; translations mine): Thin, wearing glasses, and speaking like a big boy, Wen Chenghui makes it hard for people to think he is the founder of “Liwushuo” (礼物说). Wen Chenghui began his business at 16, when he was still in high school: he made a magazine himself and sold it at school, and as a result earned several thousand yuan. In his first year of university he and friends set up a studio selling hand-drawn postcards, selling one million in all and earning over 100,000 yuan. Later his company produced a mobile app called “Liwushuo”; after downloading it users can buy gifts they like. The app was very successful: in under four months more than two million people downloaded it, and the gifts sold were worth ten million yuan. When people asked Wen Chenghui why he could be so successful, he said the post-90s entrepreneurs’ biggest advantage is “understanding users best.” (the book writes 90, 16, 100 万, 10 多万, 200 多万 and 1000 万 in digits)")
WQ = table(["Interview questions (my samples; the book leaves the lines blank, and the answers are for your partner to give)", "Based on"], [
    ["1. 你为什么十六岁就开始创业？", "He began at 16 while still in high school"],
    ["2. 你在学校里卖的杂志是怎么做出来的？赚了多少钱？", "The magazine he made and sold at school earned several thousand yuan"],
    ["3. 你和朋友的工作室为什么卖手画的明信片？", "The studio sold hand-drawn postcards"],
    ["4. “礼物说”这个手机软件是怎么做出来的？", "The company made the app “Liwushuo”"],
    ["5. 这个软件为什么这么成功？", "More than two million downloads in under four months"],
    ["6. 你为什么说九零后创业最大的优势是“最懂用户”？", "His own explanation of the post-90s advantage"]],
    title="Activity 4C: sample interview questions (mine)")
SC5 = table(["Activity", "Book’s scenario and tasks"], [
    ["Activity 5 (Reading, Writing, and Speaking)", "Scenario: You are working in a Youth Center as a volunteer. Since you have learned Chinese for a year and have visited China before, you are asked to give a presentation to the students of Chinese in the Youth Center on after-school programs, left-behind children, and migrant children in China. Your presentation will help them better understand youth education and social issues in China."],
    ["A", "In two groups, Group A discusses after-school programs and Group B discusses left-behind and migrant children in China. You may use the information below for reference."],
    ["B", "Create a PowerPoint presentation to illustrate your discussion points."],
    ["C", "Each group takes turns presenting their discussion points to the class, followed by questions and answers."]],
    title="Using Chinese in Context Review, Activity 5: the Youth Center")
Q5 = [
    ("甲组 补习班和兴趣班", "Group A (甲组, printed A组), tutoring classes and interest classes (translations mine)."),
    ("中国的家长为什么让孩子去参加补习班或是兴趣班？", "1. Why do Chinese parents let their children attend tutoring or interest classes?"),
    ("孩子在补习班或是兴趣班学什么？", "2. What do children learn in tutoring or interest classes?"),
    ("这些补习班或是兴趣班多少钱？", "3. How much do these tutoring or interest classes cost?"),
    ("孩子每周去几次补习班或是兴趣班？", "4. How many times a week do children go to tutoring or interest classes?"),
    ("他们喜欢去这些补习班或是兴趣班吗？", "5. Do they like going to these classes?"),
    ("这些补习班或是兴趣班对孩子有什么影响？", "6. What influence do these classes have on children?"),
    ("乙组 留守儿童和流动儿童", "Group B (乙组, printed B组), left-behind children and migrant children."),
    ("什么是留守儿童？", "1. What are left-behind children?"),
    ("他们多长时间才能见到父母？", "2. How long does it take before they can see their parents?"),
    ("他们平时的生活怎么样？", "3. What is their everyday life like?"),
    ("什么是流动儿童？", "4. What are migrant children?"),
    ("他们为什么不可以上学？", "5. Why can’t they go to school? (as printed)"),
    ("你觉得政府应该怎么解决流动儿童上学的问题？", "6. How do you think the government should solve the problem of migrant children attending school?")]
L2 = lesson(
    "Lesson 30 Using Chinese in Context Review: emerging careers, Wen Chenghui and the Youth Center",
    "快递小哥 · 网红 · 电竞员 · 竞争力 · 温城辉 · 礼物说 · 创业者 · 补习班 · 兴趣班 · 留守儿童 · 流动儿童",
    requires=[],
    cards=[
        card("Using Chinese in Context Review, Activity 3 (Reading, Speaking, and Writing)", "A scenario about presenting emerging careers in China. The book’s three groups of questions follow; the sixth question under 网红 is printed in the book as a repeat of the courier question, and I have kept it as printed.", tables=[SC3], examples=[D(z, e) for z, e in Q3]),
        card("Using Chinese in Context Review, Activity 4 (Listening, Reading, Writing, and Speaking)", "A scenario about interviewing the post-90s entrepreneur Wen Chenghui. The recording’s script and my sample interview questions:", tables=[SC4, WQ], examples=[D(*WEN)]),
        card("Using Chinese in Context Review, Activity 5 (Reading, Writing, and Speaking)", "A scenario about a presentation at a Youth Center. The two groups’ questions:", tables=[SC5], examples=[D(z, e) for z, e in Q5]),
    ],
    exercises=[
        M("Which three emerging careers do the groups present in Activity 3?", "Couriers, internet celebrities and e-sports players", ["Doctors, teachers and pilots", "Farmers, cooks and tailors", "Drivers, singers and bankers"], "快递小哥、网红、电竞员."),
        M("How old was Wen Chenghui when he started his first business?", "Sixteen", ["Twenty-six", "Six", "Thirty"], "温城辉十六岁就开始创业."),
        M("What did he make and sell in high school?", "A magazine", ["Postcards", "Gifts", "A phone app"], "他自己做了一本杂志在学校里卖."),
        M("What did his university studio sell?", "Hand-drawn postcards", ["Magazines", "Phones", "Clothes"], "卖手画的明信片."),
        M("How many postcards did they sell in all?", "One million", ["Ten thousand", "One hundred", "Ten million"], "一共卖出一百万张."),
        M("What is “礼物说”?", "A mobile app for buying gifts", ["A magazine", "A restaurant", "A school"], "一个叫“礼物说”的手机软件，用户下载软件后就可以买到自己喜欢的礼物."),
        M("How many people downloaded it in under four months?", "More than two million", ["More than twenty", "More than two hundred", "More than two thousand"], "不到四个月，就有两百多万人下载."),
        M("What does Wen Chenghui say is the post-90s entrepreneurs’ biggest advantage?", "Understanding users best", ["Having more money", "Being older", "Working longer hours"], "九零后创业最大的优势是“最懂用户”."),
        M("What do Group A and Group B discuss in Activity 5?", "Tutoring and interest classes; left-behind and migrant children", ["Weather; food", "Sports; music", "Cars; houses"], "甲组补习班和兴趣班，乙组留守儿童和流动儿童."),
        F("温城辉十六岁就开始创业，那时候他还在读___中。", "高", ["糕", "搞", "告"], "高中: high school."),
        F("用户下载软件后就可以买到自己喜欢的礼___。", "物", ["务", "误", "雾"], "礼物: gift."),
        F("他说九零后创业最大的___势是“最懂用户”。", "优", ["忧", "由", "油"], "优势: advantage."),
        F("什么是留守儿___？", "童", ["同", "铜", "桐"], "儿童: children."),
        F("他们每月能赚多少___？", "钱", ["前", "浅", "潜"], "钱: money."),
    ],
)

UNIT = unit("第三十课 复习课 Unit 5 Review: 汉语运用复习", [L1, L2])

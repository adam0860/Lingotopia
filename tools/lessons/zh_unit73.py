"""Unit 73: Lesson 24 (Unit 4 review), the skills integration review, part 2, from the book's texts: the travel journal about the high-speed
train (Beijing to Xi'an), the two news articles on China Post then and now, the Nanjing Lukou International Airport web page and the
blog post about an emergency room in China. The YouTube video and pictures are not included; numbers the book writes as digits are
spelled out; the web addresses in the book's source notes are left out; the tables and answers that the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l23_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('还是', 0, 'hai2'), ('还有', 0, 'hai2'), ('还能', 0, 'hai2'), ('还看到', 0, 'hai2'), ('还可以', 0, 'hai2'), ('还给', 0, 'hai2'), ('还开', 0, 'hai2'), ('还款', 0, 'huan2'), ('还要', 0, 'hai2'), ('还是', 0, 'hai2'), ('稳得很', 1, 'de5'), ('得去', 0, 'dei3'), ('不得不', 1, 'de2'), ('你得去', 1, 'dei3'), ('背着', 0, 'bei1'), ('看不了', 2, 'liao3'), ('还给', 0, 'hai2'), ('为住', 0, 'wei4'), ('还款', 0, 'huan2'), ('便了人', 1, 'le5')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. activities 5 and 6 (journal)
JR = [("前几天在中国，我第一次坐了高铁旅行。一路上，我非常兴奋，聊天、看风景、拍照等等，忙个不停。",
       "Paragraph 1: A few days ago in China I took a high-speed train trip for the first time. All the way I was very excited, chatting, looking at the scenery, taking photos and so on, busy non-stop. (translations in this card are mine)"),
      ("我对高铁的印象非常好。在中国坐高铁，你几乎可以去中国的任何地方。虽然高铁的速度没有飞机快，可是坐飞机很麻烦，因为要托运行李，过安检什么的。我的旅行路线是从北京到西安，路程是七百四十六英里，四个半小时就到了。途中虽然车速特别快，但是我的感觉并不那么明显，因为高铁稳得很。",
       "Paragraph 2: My impression of the high-speed train is very good. By high-speed train in China you can go almost anywhere in China. Although the train is not as fast as a plane, flying is a hassle because you have to check luggage, go through security and so on. My route was from Beijing to Xi’an; the distance was 746 miles and it took four and a half hours. Although the speed was very high on the way, I did not feel it that much, because the train is very steady. (the book writes 746 in digits)"),
      ("那天我的出发时间是下午两点，但是我提前一个多小时就到了北京西站，车站里人很多。因为我已经在网上订了票，到站后只要从取票口取票就行了。进站的时候，我出示了车票和护照，在Ｘ光机上检查了行李。进站之后，我按照车票上的站台号和车次，非常容易就找到了自己要坐的高铁。和飞机一样，高铁上也是对号入座的，我的座位在四号车厢，是二等座，票价大概八十一美元。",
       "Paragraph 3: That day my departure time was two in the afternoon, but I arrived at Beijing West Station more than an hour early, and the station was crowded. Because I had already booked the ticket online, after arriving I only had to collect it at the ticket window. When entering the station I showed my ticket and passport, and my luggage was checked on the X-ray machine. After entering, following the platform number and train number on the ticket, I very easily found the train I was to take. Like on a plane, seats on the high-speed train are assigned; my seat was in car four, second class, and the ticket was about 81 dollars. (the book writes 2, X, 4 and 81 in digits or letters)"),
      ("二等座的车厢有点像飞机的机舱，但是行李箱比飞机上的要大，车厢尾部还有行李柜。我的座椅又宽敞又舒服；空间也很大，身前放了一个包以后，还能完全伸开腿。另外，座椅下还有插座，可以给手机和笔记本电脑充电。",
       "Paragraph 4: The second-class car is a bit like an airplane cabin, but the luggage racks are bigger than on a plane, and at the rear of the car there is also a luggage cabinet. My seat was both spacious and comfortable; the space was large too, and even after putting a bag in front of me I could still stretch my legs out fully. In addition, there were sockets under the seats for charging phones and laptops. (mine)"),
      ("在车厢里，我还看到列车员推着手推车，售卖零食、饮料和方便面。听说现在高铁上甚至也可以订外卖了。每个车厢都有一个开水机，很好用，泡茶、泡方便面特别方便。高铁上也有餐车供乘客使用。",
       "Paragraph 5: In the car I also saw an attendant pushing a hand cart, selling snacks, drinks and instant noodles. I heard that now you can even order takeout on the high-speed train. Every car has a boiling-water dispenser, which is very handy; making tea or instant noodles is especially convenient. There is also a dining car for passengers. (mine)"),
      ("跟普通火车不一样的是，在高铁上乘客不可以吸烟。车上西式的卫生间也让我感到特别方便，而且非常干净。",
       "Paragraph 6: Unlike regular trains, passengers may not smoke on the high-speed train. The Western-style toilets on board also felt especially convenient to me and are very clean. (mine)"),
      ("下车之后，我直接刷卡出了站，旁边就是西安的地铁站，在中国坐高铁简直太方便了！不知不觉，我的北京西安之旅就这样愉快地结束了。",
       "Paragraph 7: After getting off I went straight out of the station by swiping my card, and right beside it was Xi’an’s subway station; taking the high-speed train in China is simply too convenient! Before I knew it my Beijing–Xi’an trip had ended happily like this. (the book notes: adapted from China Daily’s Chinese website; the address is left out) (mine)")]
TB6 = table(["项目", "内容 (my answers)"], [["高铁上的设施", "车厢尾部有行李柜；座椅下有插座；每个车厢有开水机；有餐车"], ["车厢里的座椅", "又宽敞又舒服；空间很大，放了包还能伸开腿"], ["高铁上的饮食", "列车员推手推车卖零食、饮料和方便面；可以订外卖；用开水机泡茶、泡方便面；有餐车"], ["高铁上的卫生间", "西式的，特别方便，非常干净"]],
            title="Activity 6B: the summary table (the book leaves it blank; my answers)", say=[0, 1])
ST6 = table(["步骤", "内容 (my answers)"], [["一 去火车站", "下午两点出发，提前一个多小时到北京西站，车站里人很多"], ["二 取票", "已经在网上订了票，从取票口取票"], ["三 进站检查", "出示车票和护照，行李过安检"], ["四 上车", "按照车票上的站台号和车次找到高铁，对号入座，四号车厢，二等座"], ["五 途中", "聊天、看风景、拍照；车速很快但是很平稳；看到列车员推手推车"], ["六 出站", "直接刷卡出站，旁边就是西安的地铁站"]],
            title="Activity 6C: the six steps of the trip (the book gives the diagram with the six step names; the notes are mine)", say=[0, 1])
L1 = lesson(
    "Lesson 24 Skills Integration Review: a travel journal about the high-speed train",
    "第一次坐高铁 · 北京到西安 · 取票 进站 · 对号入座 · 二等座 · 开水机 · 刷卡出站",
    requires=[],
    cards=[
        card("Activity 5 (Listening, Writing, Reading and Speaking)",
             "Watch a YouTube video and complete the following tasks. A. Pair up. One partner listens to the first segment (start to 4m06s) and the other partner listens to the second segment (4m06s to end) without watching the video. Complete the tasks. Main Idea: What is the video segment about? B. Listen to your segment again and write down detailed information. Student A (start to 4:06): 为什么学中文, 学中文的体会, 台湾 vs 中国大陆, 建议, New Words. Student B (4:06 to the end): 中文为什么难学, 最喜欢的学习方式, New Words. C. Share your information with your partner and take notes on their part. D. Watch the video together and read the subtitles on the screen. Compare your answers. (The video and its pictures are not included.)"),
        card("Activity 6 (Reading, Writing, and Speaking)",
             "Read the travel journal written by an American student who is studying in China and complete the tasks. A. Skim the first paragraph and the last paragraph, then create an appropriate title for the following article. Share your title with a classmate. (My title: 我的第一次高铁旅行.) The journal in seven paragraphs, with the numbers spelled out and the X-ray written with a full-width letter:",
             examples=[D(z, e) for z, e in JR]),
        card("Activity 6, parts B to D",
             "B. Read the passage and, in Chinese, summarize it in your own words in the table. Then share your information with your partner. C. Read the journal again with your partner. Each student is responsible for finding detailed information for the six steps in the diagram (去火车站, 取票, 进站检查, 上车, 途中, 出站). Take notes and write key words or information under each step. D. Exchange information with your partner and determine the complete procedure for the writer’s trip. The book leaves the tables blank; mine:",
             tables=[TB6, ST6]),
    ],
    exercises=[
        M("Was it the writer’s first high-speed train trip?", "Yes", ["No, the third", "No, the tenth", "He never took it"], "我第一次坐了高铁旅行."),
        M("Where did the route go?", "From Beijing to Xi’an", ["From Shanghai to Beijing", "From Xi’an to Chengdu", "From Beijing to Harbin"], "从北京到西安."),
        M("How long did the trip take?", "Four and a half hours", ["Two hours", "Six hours", "A whole day"], "四个半小时."),
        M("Why is flying a hassle, according to him?", "You have to check luggage and pass security", ["It is too slow", "It is cheaper", "It does not go there"], "要托运行李，过安检."),
        M("When did he arrive at the station?", "More than an hour early", ["Exactly on time", "Late", "A day early"], "提前一个多小时."),
        M("How did he get his ticket?", "Booked online and collected it at the ticket window", ["Bought it at the gate", "A friend gave it", "He printed it at home"], "从取票口取票."),
        M("Which class was his seat?", "Second class", ["First class", "Business class", "Premium class"], "二等座."),
        M("Which car was his seat in?", "Car four", ["Car one", "Car eight", "Car twelve"], "四号车厢."),
        M("Where are the sockets?", "Under the seats", ["On the ceiling", "In the toilet", "At the door"], "座椅下还有插座."),
        M("What is different from regular trains?", "Passengers may not smoke", ["It has no toilet", "It has no seats", "It is slower"], "乘客不可以吸烟."),
        M("How did he leave the station?", "He swiped his card at the gate", ["He bought a ticket", "He climbed a fence", "He took a taxi"], "直接刷卡出了站."),
        F("我提前一个多小时就到了北京西___。", "站", ["门", "场", "馆"], "北京西站."),
        F("和飞机一样，高铁上也是对号___座的。", "入", ["出", "上", "下"], "对号入座."),
    ],
)

# ------------------------------------------------------------------ 2. activity 7: China Post
N1 = [("以前，中国邮政能够办理的业务主要就是信件、包裹、汇款和报纸杂志的递送。那个时候没有手机应用，没有智能快递箱，电信、广播、电视也不普遍，很多在偏远地区的邮递员“基本靠走”来投递。有的邮递员甚至要背着二十多公斤重的邮包，为住在山里的村民服务，给他们送去包裹、报纸以及远方寄来的汇款单。后来，邮递员可以骑自行车或是坐车去送邮件了。人们有了电话、手机以后，信件少了很多，有一段时期，因为邮局的设施差、等候时间长，很多中国人不愿到邮局办业务。",
       "Part 1, paragraph 1 (中国邮政的过去): In the past the business that China Post could handle was mainly the delivery of letters, packages, remittances, and newspapers and magazines. At that time there were no mobile apps and no smart express boxes, telecommunications, broadcasting and television were not widespread either, and many postmen in remote areas delivered “basically by walking”. Some postmen even had to carry mail bags of more than twenty kilograms on their backs to serve villagers living in the mountains, delivering packages, newspapers and remittance slips sent from far away. Later, postmen could ride bicycles or take vehicles to deliver mail. After people had telephones and mobile phones there were far fewer letters, and for a period, because post offices had poor facilities and long waiting times, many Chinese were unwilling to go to the post office for business. (the book writes 20 in digits; translations in this card are mine)"),
      ("一九八零年七月十五日，中国邮政收到了一封从新加坡寄来的快件。快件是寄往北京市海淀区的，当时是由四名邮递员一起投递的。也就是那一年，北京、上海、广州、深圳等城市首先开办了国际特快专递业务，特快专递从此开始。国际特快专递业务开办四年后的一九八四年，中国邮政又开办了国内特快专递业务。",
       "Part 1, paragraph 2: On July 15, 1980, China Post received an express item sent from Singapore. It was addressed to Haidian District, Beijing, and at the time was delivered by four postmen together. In that same year Beijing, Shanghai, Guangzhou, Shenzhen and other cities were the first to start international express mail, and express mail began from then on. Four years after international express began, in 1984, China Post also started domestic express business. (the book writes the dates in digits)")]
N2 = [("现在中国邮局的变化很大，不仅业务种类丰富多样，服务也越来越方便、越来越快捷！中国邮政已经开通网上营业厅、手机邮局、微信邮局、网上银行、手机银行等电子服务。寄快件、订报纸、买邮票，或是办理交费、转账、信用卡还款，都不用走出家门，轻松地在手机上就可以完成。邮局还有会“动”的明信片、能发声的邮票、可自己设计的邮政纪念品……更是吸引着年轻的用户，体验新鲜事物。邮政无人机、邮政无人投递车也将开始使用，机器人还可以分快递包裹。近年来，中国邮政还开始了形式多样的便民服务，包括寄送身份证、社保和医保卡、体检报告等等。",
       "Part 2, paragraph 1 (中国邮政的现在): Today the post offices in China have changed greatly: not only is the business rich and varied, the service is also more and more convenient and fast! China Post has already opened online business halls, mobile post offices, WeChat post offices, online banking, mobile banking and other electronic services. Sending express items, subscribing to newspapers, buying stamps, or paying fees, transferring money and repaying credit cards can all be done easily on a phone without leaving home. The post office also has “moving” postcards, stamps that can make sounds and postal souvenirs you can design yourself… which even more attract young users to experience new things. Postal drones and unmanned delivery vehicles will also begin to be used, and robots can even sort express packages. In recent years China Post has also begun many forms of services for the convenience of the people, including sending ID cards, social security and medical insurance cards, physical examination reports and so on. (mine)"),
      ("另外，邮局的快递业务量从二零一四年起超过美国后，一直是世界第一。现在的中国人在手机应用上看看水果的图片，选好付款后，几天甚至几小时之内，快递就可以直接送到家门口了，极大地方便了人们的生活。很多新鲜的农产品通过邮航专机只需要二十四到四十八小时就能送到家中的餐桌上。",
       "Part 2, paragraph 2: Besides, since the post office’s express volume passed that of the United States in 2014 it has always been first in the world. Chinese people now look at pictures of fruit on a phone app, pay after choosing, and within a few days or even a few hours the express delivery can be sent right to the door, which greatly eases people’s lives. Many fresh farm products need only twenty-four to forty-eight hours by postal air freight to reach the dining table at home. (the book writes the year and the hours in digits; mine)")]
L2 = lesson(
    "Lesson 24 Skills Integration Review: China Post then and now",
    "中国邮政的过去 · 基本靠走 · 国际特快专递 · 中国邮政的现在 · 网上营业厅 · 邮政无人机 · 世界第一",
    requires=[],
    cards=[
        card("Activity 7 (Reading, Writing, and Speaking)",
             "Read the following news articles and complete the tasks. A. Pair up. Each partner reads one part of the news article. From the subtitle of the news article in your part, guess the type of information being reported. B. Read your part and write a summary of it in the space provided. C. Share your information with your partner when you are done. D. Compare the services of China Post with the services of the United States Postal Services (中国邮政服务 / 美国邮政服务; the book leaves the two-column table blank). Tell your class what postal services you usually use. (Two pictures and the China Post logo are not included.)"),
        card("Part 1: 中国邮政的过去", "The dates and numbers are spelled out in characters. Summary (mine): in the past the post office mainly handled letters, parcels, remittances and papers, often delivered on foot; later bicycles and vehicles; fewer letters after phones; and in 1980 and 1984 express mail began.", examples=[D(z, e) for z, e in N1]),
        card("Part 2: 中国邮政的现在", "The year and the hours are spelled out in characters. Summary (mine): today China Post offers online and phone services, new kinds of postcards and stamps, drones and robots, and everyday services; its express volume has been first in the world since 2014, and fresh farm products reach the table in one to two days.", examples=[D(z, e) for z, e in N2]),
    ],
    exercises=[
        M("In the past, what was China Post’s main business?", "Letters, packages, remittances, newspapers and magazines", ["Banking only", "Airline tickets", "Selling phones"], "信件、包裹、汇款和报纸杂志的递送."),
        M("How did many postmen in remote areas deliver?", "Basically on foot", ["By drone", "By train", "By ship"], "基本靠走."),
        M("How heavy were the mail bags some postmen carried?", "More than twenty kilograms", ["About two kilograms", "Over two hundred kilograms", "Five kilograms"], "二十多公斤重."),
        M("Why were many Chinese unwilling to go to the post office for a period?", "Poor facilities and long waits", ["Too many staff", "No stamps", "Too far"], "设施差、等候时间长."),
        M("When did China Post receive an express item from Singapore?", "July 15, 1980", ["May 1, 1984", "June 1, 2014", "July 15, 2008"], "一九八零年七月十五日."),
        M("When did domestic express begin?", "1984", ["1980", "2014", "1990"], "一九八四年."),
        M("Which is NOT an electronic service mentioned?", "Telegram office", ["WeChat post office", "Online business hall", "Mobile banking"], "电子服务."),
        M("What can postal robots do?", "Sort express packages", ["Cook", "Teach", "Drive trains"], "机器人还可以分快递包裹."),
        M("Which year did the express volume pass that of the United States?", "2014", ["1984", "2020", "2008"], "二零一四年起."),
        M("How long do fresh farm products need by postal air freight?", "Twenty-four to forty-eight hours", ["One week", "One hour", "A month"], "二十四到四十八小时."),
        F("邮政无人机、邮政无人投递车也将开始使用，机器人还可以___快递包裹。", "分", ["吃", "买", "看"], "分: sort."),
        F("现在中国邮局的变化很大，不仅业务种类丰富多___。", "样", ["少", "快", "高"], "丰富多样."),
    ],
)

# ------------------------------------------------------------------ 3. activity 8: Nanjing Lukou airport
AP = [("南京禄口国际机场座落于南京市江宁区禄口镇，距市中心约四十一公里。机场有两条三千六百米跑道、两座航站楼、两座货运站和一座交通中心，候机楼面积四十二点五万平方米。禄口国际机场拥有一百三十五条国内航线和二十三条国际航线，通往五十四个国内主要城市和二十个国际城市及地区。机场的Ｔ二航站楼是国际型航站楼，年旅客量一千八百万人次，航站楼有出发层和到达层。",
       "Paragraph 1 (the airport): Nanjing Lukou International Airport is located in Lukou Town, Jiangning District, Nanjing, about 41 kilometers from the city center. The airport has two 3,600-meter runways, two terminals, two cargo stations and a transport center, and the terminal building covers 425,000 square meters. Lukou International Airport has 135 domestic routes and 23 international routes, leading to 54 major domestic cities and 20 international cities and regions. The airport’s Terminal T2 is an international terminal with 18 million passenger trips a year, and has a departure level and an arrival level. (the book writes the numbers and T2 in digits; translations in this card are mine)"),
      ("机场办票。旅客进入候机楼大厅后，可以直接看到办票柜台。机场有很多自助办票设备，方便无托运行李旅客办理登机手续。国内航班起飞前四十分钟停止办理登机手续；国际航班起飞前四十五分钟停止办理登机手续。",
       "Paragraph 2 (check-in): After entering the terminal hall, passengers can see the check-in counters directly. The airport has many self-service check-in machines, convenient for passengers without checked luggage to go through boarding procedures. Check-in for domestic flights closes forty minutes before takeoff; for international flights, forty-five minutes before takeoff."),
      ("出港流程。国内出发流程：一、托运行李；二、换登机牌；三、安全检查；四、候机及登机。国际出发流程：一、托运行李；二、换登机牌；三、检验检疫；四、海关；五、边防检查；六、安全检查；七、候机及登机。国内到达流程：一、提取行李；二、离开机场。国际到达流程：一、检验检疫；二、边防检查；三、提取行李；四、海关检查；五、离开机场。",
       "Paragraph 3 (departure and arrival procedures): Domestic departure: 1 check luggage; 2 get the boarding pass; 3 security check; 4 wait and board. International departure: 1 check luggage; 2 boarding pass; 3 inspection and quarantine; 4 customs; 5 border control; 6 security check; 7 wait and board. Domestic arrival: 1 pick up luggage; 2 leave the airport. International arrival: 1 inspection and quarantine; 2 border control; 3 pick up luggage; 4 customs check; 5 leave the airport. (the book prints the steps with numerals in a flow chart)"),
      ("设施和服务。Ｔ二航站楼出发大厅和到达大厅有各类百货和便利店，提供各类商品百货供旅客选择。机场免税店位于国际出发大厅内。国内、国际出发大厅还有肯德基、汉堡王、大娘水饺等中西式快餐店。Ｔ二航站楼内有无线上网服务，在候机室内，旅客可以很方便地上网，还可以给手机充电、饮用热水、使用母婴室等。同时，机场也有酒店住宿服务、医疗服务、问询服务、银行服务和行李服务。",
       "Paragraph 4 (facilities and services): The T2 departure and arrival halls have all kinds of department stores and convenience stores, offering all kinds of goods for passengers to choose from. The airport’s duty-free shop is in the international departure hall. The domestic and international departure halls also have Chinese and Western fast-food restaurants such as KFC, Burger King and Daniang Dumplings. Terminal T2 has wireless internet; in the waiting rooms passengers can get online very conveniently and also charge their phones, drink hot water, use the mother-and-baby room and so on. At the same time the airport also has hotel, medical, inquiry, banking and luggage services. (mine)"),
      ("机场交通。机场班车机场一号线和机场二号线，每二十到三十分钟一班。旅客也可以选择坐机场线地铁和出租车到达市内和其它地方。",
       "Paragraph 5 (airport transport): The airport shuttle buses, Airport Line 1 and Airport Line 2, run every twenty to thirty minutes. Passengers can also choose the airport subway line and taxis to reach the city and other places. (the book notes: adapted from an airline website; the address is left out) (mine)")]
TA = table(["段落", "内容 (my answers)"], [["第一段", "南京禄口国际机场的位置和规模：在江宁区禄口镇，距市中心约四十一公里，一百三十五条国内航线，二十三条国际航线"], ["第二段", "机场办票：有办票柜台和自助办票设备，国内航班起飞前四十分钟、国际航班起飞前四十五分钟停止办理"], ["第三段", "出港流程：国内出发四步，国际出发七步，国内到达两步，国际到达五步"], ["第四段", "设施和服务：商店，免税店，快餐店，无线上网，充电，热水，母婴室，酒店，医疗，问询，银行，行李服务"], ["第五段", "机场交通：机场班车一号线和二号线，每二十到三十分钟一班，也可以坐地铁和出租车"]],
           title="Activity 8B: the paragraph table (the book leaves it blank; my answers)", say=[0, 1])
L3 = lesson(
    "Lesson 24 Skills Integration Review: Nanjing Lukou International Airport",
    "南京禄口国际机场 · 机场办票 · 出港流程 · 设施和服务 · 机场交通",
    requires=[],
    cards=[
        card("Activity 8 (Reading, Writing, Speaking and Listening)",
             "Read the following website information and complete the tasks. A. Skim the title of the webpage and predict what you are expecting to read. Share your guess in Chinese with a classmate. B. Work in groups of three. Each student reads one or two paragraphs of the passage and, in Chinese, writes down the main idea and key information in the table. C. Share information with your partners. Ask for information from the parts that your partners read and complete the table with the information they collected. The book titles the page 南京禄口国际机场 and prints it under the headings 机场办票, 出港流程, 设施和服务 and 机场交通. The numbers are spelled out in characters and the terminal name is written with a full-width letter. (The picture is not included.)",
             examples=[D(z, e) for z, e in AP],
             tables=[TA]),
    ],
    exercises=[
        M("How far is the airport from the city center?", "About forty-one kilometers", ["About four kilometers", "About four hundred", "About twelve"], "距市中心约四十一公里."),
        M("How many runways does the airport have?", "Two", ["One", "Three", "Five"], "两条三千六百米跑道."),
        M("How many domestic routes does it have?", "135", ["23", "54", "20"], "一百三十五条国内航线."),
        M("How many passengers a year does Terminal 2 handle?", "18 million passenger trips", ["1.8 million", "180 million", "800 thousand"], "年旅客量一千八百万人次."),
        M("When does check-in close for domestic flights?", "Forty minutes before takeoff", ["Fifteen minutes", "One hour", "At takeoff"], "起飞前四十分钟."),
        M("When does check-in close for international flights?", "Forty-five minutes before takeoff", ["Thirty minutes", "Two hours", "Ten minutes"], "起飞前四十五分钟."),
        M("How many steps are there in the international departure procedure?", "Seven", ["Four", "Five", "Two"], "国际出发七步."),
        M("What is the last step of domestic arrival?", "Leave the airport", ["Customs", "Security check", "Check luggage"], "离开机场."),
        M("Where is the duty-free shop?", "In the international departure hall", ["In the arrival hall", "Outside the airport", "At the subway"], "位于国际出发大厅内."),
        M("Which service is NOT mentioned?", "A swimming pool", ["Hotel", "Medical service", "Banking service"], "酒店, 医疗, 问询, 银行, 行李."),
        M("How often do the airport shuttle buses run?", "Every 20 to 30 minutes", ["Every 5 minutes", "Every 2 hours", "Once a day"], "每二十到三十分钟一班."),
        F("旅客进入候机楼大厅后，可以直接看到办票___台。", "柜", ["桌", "椅", "门"], "办票柜台: check-in counter."),
        F("机场免税店位于国际出发大厅___。", "内", ["外", "旁", "后"], "位于…内."),
    ],
)

# ------------------------------------------------------------------ 4. activity 9: the dentist
BL = [("最近我和朋友在中国乘火车出门的时候，因为吃了一枚蚕豆而不得不去亲身体验了一下中国医院的急诊部！",
       "Paragraph 1 (the title is 英国老外在中国看急诊, “A British foreigner in a Chinese emergency room”): Recently, when a friend and I were traveling by train in China, because I ate one broad bean I had to personally experience the emergency department of a Chinese hospital! (translations in this card are mine)"),
      ("那天我们坐火车去天津。出发前我们在商店里买了各种零食，方便面、花生瓜子、巧克力，还有脆脆的蚕豆。火车开动以后，我打开那包蚕豆吃起来，没想到用劲一咬，我的一颗牙齿变成了两半儿。",
       "Paragraph 2: That day we took the train to Tianjin. Before departure we bought all kinds of snacks in a shop: instant noodles, peanuts and sunflower seeds, chocolate and crunchy broad beans. After the train started I opened the bag of broad beans and began eating, and never expected that biting hard would split one of my teeth in two."),
      ("到了天津后，当地的一名出租车司机开车把我们送到了一个牙医诊所。牙医很快地检查了我的牙以后，说，“不行，这个我看不了。你得去医院的急诊部。”幸亏，医院就在马路对面。",
       "Paragraph 3: After arriving in Tianjin a local taxi driver drove us to a dental clinic. After quickly examining my tooth the dentist said, “No, I can’t handle this. You have to go to the hospital’s emergency department.” Luckily the hospital was just across the road."),
      ("到了急诊部，我付了六块钱人民币挂号，然后就被带进了牙医诊室。给我看病的牙医让我坐到升降椅子上，开始检查我的牙齿。每次牙医碰到我的牙齿，我都痛苦地大叫。牙医问我牙齿是怎么变成两半的。",
       "Paragraph 4: At the emergency department I paid six yuan to register and was then taken into the dentist’s room. The dentist who treated me had me sit on an adjustable chair and began to examine my teeth. Every time the dentist touched my tooth I cried out in pain. The dentist asked how my tooth had come to be in two halves. (the book writes 6 in digits)"),
      ("后来他问我：“啊，这颗牙，你想不想拔掉？”我告诉他当然想拔。所以，牙医让护士给我打上止痛针，然后他大手一动，那颗牙马上就被拔了出来！他举着那颗牙，给我看了看。最后还给我开了一些止痛药，让我回去以后吃。",
       "Paragraph 5: Later he asked me, “Ah, this tooth, do you want to pull it out?” I told him of course I wanted it pulled. So the dentist had a nurse give me a painkilling injection, then with one move of his big hand the tooth was pulled out at once! He held the tooth up and showed it to me. Finally he also prescribed some painkillers for me to take after I got back."),
      ("拔牙以后，我付了五十元的治疗费和药费，大约相当于五英镑。",
       "Paragraph 6: After the extraction I paid 50 yuan for the treatment and medicine, roughly equivalent to five pounds. (the book writes 50 and 5 in digits)")]
EE = table(["问题", "内容 (my answers)"], [["什么时候", "最近，坐火车去天津的时候"], ["谁", "一个英国人和他的朋友"], ["什么事", "吃蚕豆时牙齿变成了两半，去医院急诊部拔了牙"], ["怎么样", "出租车司机送到牙医诊所，牙医让他去医院，挂号，检查，打止痛针，拔牙，交费"], ["在哪儿", "火车上，天津的牙医诊所和医院急诊部"], ["为什么", "用劲咬硬的蚕豆"]],
           title="Activity 9B: the EEI table (When, Who, What, How, Where, Why; the book leaves it blank; my answers)", say=[0, 1])
SQ = table(["顺序", "活动 (my answers)", "Letter in the book"], [["一", "吃蚕豆", "A"], ["二", "牙齿变成两半", "H"], ["三", "去牙医诊所", "C"], ["四", "医院急诊部挂号", "B"], ["五", "牙医检查牙齿", "G"], ["六", "打止痛针", "D"], ["七", "拔牙", "F"], ["八", "交治疗费和药费", "E"]],
           title="Activity 9C: the correct sequence (the book leaves the numbers blank; my order)", say=[0, 1])
L4 = lesson(
    "Lesson 24 Skills Integration Review: a blog post about an emergency room in China",
    "蚕豆 牙齿 · 牙医诊所 · 急诊部挂号 · 止痛针 拔牙 · 治疗费和药费",
    requires=[],
    cards=[
        card("Activity 9 (Reading, Writing, Speaking and Listening)",
             "A. Pre-Reading: make a list of unexpected things that can happen during travel (旅途中可能发生的意外). Then share your list with a classmate. (Two pictures are not included.) B. Read the blog post and summarize the required EEIs in the table: When, Who, What, How, Where, Why (cause). Exchange your information with a classmate when you are done. C. With your partner, number the following activities in the correct sequence, as related in the story: A. 吃蚕豆 B. 医院急诊部挂号 C. 去牙医诊所 D. 打止痛针 E. 交治疗费和药费 F. 拔牙 G. 牙医检查牙齿 H. 牙齿变成两半. D. Retell the story in your own words using the information from Steps B and C. The numbers in the blog are spelled out in characters.",
             examples=[D(z, e) for z, e in BL],
             tables=[EE, SQ]),
    ],
    exercises=[
        M("What caused the writer to visit the emergency room?", "He bit a broad bean and broke a tooth", ["A fall on the train", "Food poisoning", "A fever"], "吃了一枚蚕豆."),
        M("Where were the writer and his friend going?", "Tianjin", ["Beijing", "Shanghai", "Chengdu"], "坐火车去天津."),
        M("Which snack was NOT bought?", "Dried fruit", ["Instant noodles", "Chocolate", "Crunchy broad beans"], "方便面、花生瓜子、巧克力、蚕豆."),
        M("Who drove them to the dental clinic?", "A local taxi driver", ["A friend", "A nurse", "A policeman"], "当地的一名出租车司机."),
        M("What did the first dentist say?", "He couldn’t handle it and they should go to the hospital emergency department", ["He would pull the tooth", "It was nothing", "Come back tomorrow"], "这个我看不了。你得去医院的急诊部."),
        M("Where was the hospital?", "Across the road", ["Ten kilometers away", "In another city", "Beside the station"], "医院就在马路对面."),
        M("How much did he pay to register?", "Six yuan", ["Fifty yuan", "Five pounds", "Sixty yuan"], "六块钱人民币挂号."),
        M("What was done before the tooth was pulled?", "A painkilling injection", ["A blood test", "An X-ray", "A cleaning"], "打上止痛针."),
        M("How much did the treatment and medicine cost altogether?", "Fifty yuan", ["Six yuan", "Five hundred yuan", "Five pounds only"], "五十元的治疗费和药费."),
        M("How does the cost compare in pounds?", "About five pounds", ["About fifty pounds", "About one pound", "About five hundred"], "大约相当于五英镑."),
        F("牙医让护士给我打上止痛___。", "针", ["药", "水", "片"], "止痛针: painkilling injection."),
        F("没想到用劲一咬，我的一颗牙齿变成了两___儿。", "半", ["块", "片", "个"], "两半儿: two halves."),
    ],
)

UNIT = unit("第二十四课 Unit 4 review: skills integration review, part 2", [L1, L2, L3, L4])

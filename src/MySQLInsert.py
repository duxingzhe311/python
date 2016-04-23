#encoding: utf-8
'''
CREATE TABLE `customers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL DEFAULT '',
  `last_name` varchar(255) NOT NULL DEFAULT '',
  `age` smallint(6) NOT NULL DEFAULT '0',
  `birthday` varchar(255) NOT NULL DEFAULT '',
  `money` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
import sys,pymysql,random,datetime,time
reload(sys)
sys.setdefaultencoding('utf-8')

seed = u"天地玄黄宇宙洪荒日月盈昃辰宿列张寒来暑往秋收冬藏闰余成岁律吕调阳云腾致雨露结为霜金生丽水玉出昆冈剑号巨阙珠称夜光果珍李柰菜重芥姜海咸河淡鳞潜羽翔龙师火帝鸟官人皇始制文字乃服衣裳推位让国有虞陶唐吊民伐罪周发殷汤坐朝问道垂拱平章爱育黎首臣伏戎羌遐迩一体率宾归王鸣凤在竹白驹食场化被草木赖及万方盖此身发四大五常恭惟鞠养岂敢毁伤女慕贞洁男效才良知过必改得能莫忘罔谈彼短靡恃己长信使可覆器欲难量墨悲丝染诗赞羔羊景行维贤克念作圣德建名立形端表正空谷传声虚堂习听祸因恶积福缘善庆尺璧非宝寸阴是竞资父事君曰严与敬孝当竭力忠则尽命临深履薄夙兴温凊似兰斯馨如松之盛川流不息渊澄取映容止若思言辞安定笃初诚美慎终宜令荣业所基籍甚无竟学优登仕摄职从政存以甘棠去而益咏乐殊贵贱礼别尊卑上和下睦夫唱妇随外受傅训入奉母仪诸姑伯叔犹子比儿孔怀兄弟同气连枝交友投分切磨箴规仁慈隐恻造次弗离节义廉退颠沛匪亏性静情逸心动神疲守真志满逐物意移坚持雅操好爵自縻都邑华夏东西二京背邙面洛浮渭据泾宫殿盘郁楼观飞惊图写禽兽画彩仙灵丙舍旁启甲帐对楹肆筵设席鼓瑟吹笙升阶纳陛弁转疑星右通广内左达承明既集坟典亦聚群英杜稿钟隶漆书壁经府罗将相路侠槐卿户封八县家给千兵高冠陪辇驱毂振缨世禄侈富车驾肥轻策功茂实勒碑刻铭盘溪伊尹佐时阿衡奄宅曲阜微旦孰营桓公匡合济弱扶倾绮回汉惠说感武丁俊义密勿多士实宁晋楚更霸赵魏困横假途灭虢践土会盟何遵约法韩弊烦刑起翦颇牧用军最精宣威沙漠驰誉丹青九州禹迹百郡秦并岳宗泰岱禅主云亭雁门紫塞鸡田赤诚昆池碣石钜野洞庭旷远绵邈岩岫杳冥治本于农务兹稼穑俶载南亩我艺黍稷税熟贡新劝赏黜陟孟轲敦素史鱼秉直庶几中庸劳谦谨敕聆音察理鉴貌辨色贻厥嘉猷勉其祗植省躬讥诫宠增抗极殆辱近耻林皋幸即两疏见机解组谁逼索居闲处沉默寂寥求古寻论散虑逍遥欣奏累遣戚谢欢招渠荷的历园莽抽条枇杷晚翠梧桐蚤凋陈根委翳落叶飘摇游鹍独运凌摩绛霄耽读玩市寓目囊箱易輶攸畏属耳垣墙具膳餐饭适口充肠饱饫烹宰饥厌糟糠亲戚故旧老少异粮妾御绩纺侍巾帷房纨扇圆洁银烛炜煌昼眠夕寐蓝笋象床弦歌酒宴接杯举殇矫手顿足悦豫且康嫡后嗣续祭祀烝尝稽颡再拜悚惧恐惶笺牒简要顾答审详骸垢想浴执热愿凉驴骡犊特骇跃超骧诛斩贼盗捕获叛亡布射僚丸嵇琴阮箫恬笔伦纸钧巧任钓释纷利俗并皆佳妙毛施淑姿工颦妍笑年矢每催曦晖朗曜璇玑悬斡晦魄环照指薪修祜永绥吉劭矩步引领俯仰廊庙束带矜庄徘徊瞻眺孤陋寡闻愚蒙等诮谓语助者焉哉乎也"

def generateStr(n):
    res = ""
    i = 0
    while i < n:
        index = random.randint(0,len(seed) - 1)
        res += seed[index]
        i += 1
    return res

def generateInt(s,t):
    return random.randint(s,t)

def generateMoney(n):
    return random.random() * n

def generateBirthday(start,end):
    n = random.randint(start,end)
    return datetime.datetime.utcfromtimestamp(n)

conn = pymysql.connect(host='localhost',user='root',passwd='password_pinglian',db='pay',port=3306,charset="utf8")
cur = conn.cursor()

i = 0
n = 1000
now = int(time.time())
while i < n:
    firstName = generateStr(generateInt(3,12))
    lastName = generateStr(generateInt(6,20))
    age = str(generateInt(10,120))
    birthday = str(generateBirthday(0, now))
    money = str(generateMoney(100000))
    
    sql = "insert into customers (first_name,last_name,age,birthday,money) values ('" + firstName + "','" + lastName +"'," + age +",'" + birthday + "','" + money + "')"
    print sql
    res = cur.execute(sql)
    i += 1

conn.commit()
cur.close()
conn.close()

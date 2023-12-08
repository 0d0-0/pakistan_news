from django.shortcuts import render,HttpResponse,redirect
from Pakistan.models import History ,Test
import re,requests,time
from datetime import datetime 
from bs4 import BeautifulSoup
from . import to_get_content
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def welcome(request):
    if request.method == "GET":
        return render(request,'welcome.html')

def catalogue(request):   #目录
    if request.method == "GET":
        return render(request,'index.html')

def history(request):  #历史
    if request.method == "GET":
        #把数据先放进test_records中
        test_records=[
            History(times='旧石器时代',text='Soanian 是旧石器时代下部 Acheulean 的考古文化。它以现代伊斯兰堡/拉瓦尔品第附近的西瓦利克山的索安山谷命名。在距离拉瓦尔品第约16公里(9.9英里)的阿迪亚拉和卡萨拉，在索安河的拐弯处发现了数百个锋利的卵石工具。'),
            History(times='新石器时代',text='Mehrgarh是1974年发现的重要新石器时代遗址,它显示了农业和畜牧业的早期证据,以及牙科。该遗址的历史可以追溯到公元前7000-5500年,位于俾路支省的卡奇平原。Mehrgarh 的居民住在泥砖房里，将谷物储存在粮仓中，用铜、种植大麦、小麦、枣子和枣制作工具，并放牧绵羊、山羊和牛。随着文明的进步（公元前 5500-2600 年）,居民开始从事手工艺,包括燧石捏、鞣制、珠子生产和金属加工。该遗址一直被占领,直到公元前2600年气候变化开始发生。在公元前2600年至2000年之间，该地区变得更加干旱,Mehrgarh被放弃,取而代之的是印度河流域，那里的新文明正处于发展的早期阶段。'),
            History(times='印度河流域文明',text='''印度河流域的青铜时代始于公元前 3300 年左右的印度河流域文明.与古埃及和美索不达米亚一起,它是旧世界的三个早期文明之一,也是三个文明中最广泛的,覆盖了1万平方公里的面积25。它在印度河流域、今天的巴基斯坦信德省、旁遮普省和俾路支省，以及常年流淌的河流系统,主要是季风喂养的河流,曾经在印度西北部部分地区的季节性加加尔-哈克拉河附近流淌。在鼎盛时期,该文明拥有约21万人口,分布在数百个定居点中,远至阿拉伯海，一直延伸到今天的阿富汗南部和东部，以及喜马拉雅山。古代印度河流域的居民哈拉帕人开发了冶金和手工艺品（肉质制品，印章雕刻）的新技术，并生产铜，青铜，铅和锡。
成熟的印度河文明从公元前 2600 年到公元前 1900 年蓬勃发展，标志着印度河流域城市文明的开始。该文明包括哈拉帕、加内里瓦拉和摩亨佐达罗等城市中心，以及俾路支省南部一个名为库利文化（公元前 2500-2000 年）的分支，以其砖砌的城市、路边排水系统和多层房屋而闻名。人们认为它也有某种市政组织。
在这个文明的后期，逐渐衰落的迹象开始出现，到公元前 1700 年左右，大多数城市都被遗弃了。然而，印度河流域文明并没有突然消失，印度河流域文明的一些元素可能幸存下来。公元前 3 世纪该地区干旱化可能是与文明相关的城市化的最初刺激，但最终也减少了供水，足以导致文明的消亡，并将其人口向东分散。该文明在公元前 1700 年左右崩溃，但其衰落背后的原因仍然未知。通过对印度河城市的挖掘和对城市规划和印章的分析，可以推断出该文明在城市规划、艺术、手工艺和贸易方面具有高度的复杂性。'''),
            History(times='吠陀时期',text='吠陀时期（约公元前 1500 年至公元前 500 年）被认为形成于公元前 1500 年至公元前 800 年之间。随着印度雅利安人迁徙并定居到印度河流域，随之而来的是他们独特的宗教传统和习俗，这些传统和习俗与当地文化融为一体。来自巴克特里亚-马尔吉亚纳文化的印度-雅利安人宗教信仰和习俗以及前印度河流域文明的本土哈拉帕印度河信仰最终产生了吠陀文化和部落。早期的印度-雅利安人是以旁遮普邦为中心的青铜时代晚期社会，被组织成部落而不是王国，主要靠牧民的生活方式维持。在此期间，印度教最古老的经文吠陀经被撰写。'),
            History(times='阿契美尼德帝国',text='''到公元前 550 年，留在印度河流域的主要吠陀部落是 Kamboja、Sindhu、犍陀罗的 Taksas、Chenab 河的 Madras 和 Kathas、Ravi 河的 Mallas 和 Sutlej 河的 Tugras。这几个部落和公国相互争斗的程度如此之大，以至于印度河流域不再有一个强大的吠陀部落王国来抵御外来者，并将交战的部落控制成一个有组织的王国。犍陀罗国王普什卡拉萨林正在与当地对手进行权力斗争，因此开伯尔山口的防御仍然很差。阿契美尼德帝国国王大流士一世趁机计划入侵。印度河流域因其黄金和肥沃的土壤而在波斯传说中，征服它是他的前任居鲁士大帝的主要目标。公元前542年，居鲁士率领他的军队征服了俾路支省南部的马克兰海岸。然而，众所周知，他曾在马克兰（卡拉特、胡兹达尔和潘杰古尔地区）以外的地区进行战役，并在格德罗西亚沙漠（今天推测为哈兰沙漠）失去了大部分军队。
公元前 518 年，大流士率领他的军队穿过开伯尔山口，分阶段向南进发，最终在公元前 516 年到达信德省的阿拉伯海沿岸。在波斯统治下，中央集权的行政管理制度和官僚制度首次被引入印度河流域，建立了几个总督府：犍陀罗大区周围的犍陀罗、旁遮普和信德省周围的印度教、阿拉科西亚，包括今天的开伯尔-普赫图赫瓦省的部分地区，以及俾路支省，班努盆地周围的萨塔吉迪亚，和格德罗西亚覆盖了俾路支省南部马克兰地区的大部分地区。
关于阿契美尼德帝国最东端的总督和边疆的已知情况在大流士铭文和希腊资料中有所提及，例如希罗多德的历史和后来的亚历山大编年史（Arrian、Strabo 等人）。这些资料列出了印度河流域的三条支流或被征服的领土，这些支流或被征服的领土隶属于波斯帝国，用于向波斯国王进贡。'''),
            History(times='马其顿帝国',text='''到公元前 326 年春天，亚历山大从巴克特里亚开始了他的印度河远征，留下了 3500 匹马和 10,000 名士兵。他将军队分为两组。大军将通过开伯尔山口进入印度河流域，就像大流士在200年前所做的那样，而亚历山大亲自指挥的一支小部队则通过北部路线进入，可能通过吉特拉尔附近的布罗戈尔或多拉山口。亚历山大指挥着一群手持盾牌的卫兵、步兵、弓箭手、阿格里尼亚人和骑标枪的人，带领他们对抗前犍陀罗总督府的部落。
他们遇到的第一个部落是库纳尔山谷的阿斯帕西奥伊部落，他们与亚历山大展开了一场激烈的战斗，他自己也被飞镖击中了肩膀。然而，阿斯帕西奥伊人最终失败了，40,000 人被奴役。亚历山大随后继续向西南方向前进，在公元前326年31月，他遇到了斯瓦特和布纳山谷的阿萨克诺伊部落。阿萨克诺伊人英勇作战，并在奥拉、巴兹拉（巴里科特）和马萨加等城市对亚历山大及其军队进行了顽强抵抗。亚历山大对阿萨克诺伊人的抵抗非常愤怒，以至于他杀死了马萨加的整个人口，并将其建筑物夷为平地——随后在奥拉也发生了类似的屠杀。随后在阿萨克诺伊人的另一个据点奥拉（Ora）发生了类似的屠杀。这些屠杀的故事传到了无数阿萨克尼亚人那里，他们开始逃往位于香拉和科希斯坦之间的山堡奥诺斯。亚历山大紧随其后，围攻了这座具有战略意义的山堡，最终占领并摧毁了这座堡垒，并杀死了里面的所有人。剩下的小部落要么投降，要么像普什卡拉瓦蒂（Charsadda）的阿斯塔尼诺伊部落一样，很快就被消灭了，亚历山大俘虏了 000,230 名士兵和 000,32 头牛。最终，亚历山大的小部队将与通过开伯尔山口在阿托克相遇的大部队相遇。随着对犍陀罗的征服完成，亚历山大转而加强他的军事补给线，这条补给线现在已经危险地从兴都库什山脉延伸到巴克特里亚的巴尔赫。
在征服犍陀罗并巩固了返回巴克特里亚的补给线后，亚历山大与塔克西拉国王安比联合，于公元前 326 年 33 月渡过印度河，开始了阿科西亚（旁遮普）战役。他的第一次抵抗将在 Bhera 附近的 Jhelum 河上对抗 Paurava 部落的 Porus 国王。亚历山大（与安比）和波鲁斯之间著名的海达斯佩斯战役 （Jhelum） 将是他进行的最后一场重大战役。在击败波鲁斯后，他疲惫不堪的军队拒绝进入印度与南达王朝的军队及其践踏大象的先锋队交战。因此，亚历山大沿着印度河流域向西南前进。一路上，他与木尔坦和信德省的小王国进行了几次战斗，然后率领军队向西穿过马克兰沙漠，前往现在的伊朗。在穿越沙漠时，亚历山大的军队因饥饿和口渴而伤亡惨重，但没有与人类敌人作战。他们遇到了“食鱼者”，或Ichthyophagi，他们是生活在马克兰海岸的原始人，他们头发乱蓬蓬的，没有火，没有金属，没有衣服，住在鲸鱼骨头制成的小屋里，吃生海鲜。'''),
            History(times='孔雀王朝',text='''孔雀帝国是南亚一个地理上广阔的铁器时代历史大国，总部设在摩揭陀，由旃陀罗笈多孔雀王朝于公元前 322 年建立，直到公元前 185 年才以松散的方式存在。[35]孔雀王朝因征服印度恒河平原而集中，其首都位于帕塔利普特拉（今巴特那）。在这个帝国中心之外，帝国的地理范围取决于控制武装城市的军事指挥官的忠诚度。在阿育王统治期间（约公元前268-232年），帝国短暂控制了印度次大陆的主要城市枢纽和动脉，但南部腹地除外。在阿育王统治后，它衰落了大约50年，并于公元前185年随着Pushyamitra Shunga暗杀Brihadratha和在摩揭陀建立Shunga帝国而解散。
旃陀罗笈多·孔雀王朝在《阿尔萨萨斯特拉》的作者查纳基亚的协助下组建了一支军队，并于公元前322年推翻了难陀帝国。旃陀罗笈多通过征服亚历山大大帝留下的总督，迅速向西扩张他的势力，横跨印度中部和西部，到公元前 317 年，帝国已完全占领印度西北部。孔雀王朝随后在塞琉古-孔雀王朝战争期间击败了塞琉古帝国的创始人塞琉古一世，从而获得了印度河以西的领土。
在孔雀王朝的统治下，由于建立了单一而高效的金融、行政和安全体系，内部和对外贸易、农业和经济活动在南亚各地蓬勃发展和扩张。孔雀王朝建造了从帕特利普特拉到塔克西拉的大干线的前身。卡林加战争后，帝国在阿育王统治下经历了近半个世纪的中央集权统治。阿育王对佛教的拥护和对佛教传教士的赞助使这种信仰扩展到斯里兰卡、印度西北部和中亚。
据估计，孔雀王朝时期南亚的人口在15万至30万之间。帝国的统治时期以艺术、建筑、铭文和制作文本方面的非凡创造力为标志。'''),
            History(times='印度-希腊王国',text='''印度-希腊人梅南德一世（公元前 155-130 年在位）将希腊-巴克特里亚人赶出犍陀罗并越过兴都库什山脉，在他获胜后不久成为国王。他的领土覆盖了现代阿富汗的潘杰希尔和卡比萨，并延伸到旁遮普地区，南部和东部有许多支流，可能远至马图拉。首都萨加拉（今锡亚尔科特）在梅南德的统治下非常繁荣，梅南德是希腊作家提到的为数不多的巴克特里亚国王之一。
佛教经典《米琳达·帕尼亚》（Milinda Pañha）赞美梅南德，称“全印度没有米琳达能与之相提并论”。他的帝国以支离破碎的方式幸存下来，直到最后一位独立的希腊国王斯特拉托二世在公元 10 年左右消失。公元前 125 年左右，欧克拉底斯的儿子希腊-巴克特里亚国王赫利奥克勒斯逃离了月氏人对巴克特里亚的入侵，并搬迁到犍陀罗，将印度-希腊人推到了杰赫勒姆河以东。最后一位已知的印度-希腊统治者是来自犍陀罗巴尧尔地区的狄奥达马斯，在公元 1 世纪的图章戒指上提到，上面刻有 Kharoṣṭhī 铭文“Su Theodamasa”（“苏”是贵霜王室头衔“Shau”（“沙阿”或“国王”）的希腊音译）。各种小国王统治到公元 1 世纪初，直到斯基泰人、帕提亚人和建立贵霜王朝的月氏人征服。
正是在这一时期，希腊化和亚洲神话、艺术和宗教元素的融合变得最为明显，特别是在横跨巴基斯坦西部和阿富汗南部的犍陀罗地区。佛陀的细节、人文主义表现开始出现，描绘了与希腊神阿波罗非常相似的人物;希腊神话图案，如半人马、酒神场景、Nereids 和 Tyche 和 Heracles 等神灵在古代巴基斯坦和阿富汗的佛教艺术中占有重要地位。'''),
            History(times='印度-斯基泰王国',text='''印度-斯基泰人是公元前 2 世纪中叶至公元前 1 世纪从中亚南部迁移到巴基斯坦和阿拉霍西亚的萨卡斯人（斯基泰人）的后裔。他们取代了印度-希腊人，统治着一个从犍陀罗延伸到马图拉的王国。公元 2 世纪，斯基泰人被萨塔瓦哈纳王朝的南印度皇帝乔塔米普特拉·萨塔卡尼击败后，萨卡统治者的权力开始下降。后来，萨卡王国在4世纪被来自印度东部的笈多帝国的旃陀罗笈多二世彻底摧毁。'''),
            History(times='印度-帕提亚王国',text='''印度-帕提亚王国由贡多法里德王朝统治，该王朝以其同名的第一任统治者贡多法雷斯的名字命名。他们在公元 55 世纪或之前统治了今阿富汗、巴基斯坦和印度西北部的部分地区。在他们历史的大部分时间里，主要的贡多法里德国王将塔克西拉（现在的巴基斯坦旁遮普省）作为他们的住所，但在他们存在的最后几年里，首都在喀布尔和白沙瓦之间转移。这些国王传统上被称为印度-帕提亚人，因为他们的铸币通常受到阿尔萨德王朝的启发，但他们可能属于居住在帕提亚以东的更广泛的伊朗部落群体，并且没有证据表明所有拥有 Gondophares 头衔的国王，意思是“荣耀的持有者”，甚至有亲戚关系。基督教著作声称，使徒圣托马斯——一位建筑师和熟练的木匠——在贡多法雷斯国王的宫廷中长期逗留，在塔克西拉为国王建造了一座宫殿，并在乘坐战车前往印度河流域之前为教会任命了领袖，以便航行最终到达马拉巴尔海岸。'''),
            History(times='贵霜帝国',text='''大约在公元 1 世纪中叶，贵霜帝国在他们的第一位皇帝库朱拉·卡德菲西斯 （Kujula Kadphises） 的领导下从现在的阿富汗扩展到次大陆西北部。他们是印欧语系中亚人月氏人的后裔，其分支被称为贵霜人。到他的孙子卡尼什卡大帝时代，帝国已经扩展到阿富汗的大部分地区和印度次大陆的北部地区，至少远至瓦拉纳西（贝拿勒斯）附近的萨克塔和萨尔纳特。
卡尼什卡皇帝是佛教的伟大赞助人;然而，随着贵霜人向南扩张，他们后来铸造的神灵开始反映其新的印度教多数。不朽的卡尼什卡佛塔被认为是由国王在现代巴基斯坦白沙瓦郊区附近建立的。
贵霜王朝在印度佛教的建立及其传播到中亚和中国的过程中发挥了重要作用。历史学家文森特·史密斯（Vincent Smith）特别谈到了卡尼什卡：
他扮演了佛教史上第二个阿育王的角色。
帝国将印度洋海上贸易与丝绸之路通过印度河流域的商业联系在一起，鼓励长途贸易，尤其是中国和罗马之间的贸易。贵霜人为萌芽和蓬勃发展的犍陀罗艺术带来了新的趋势，这种艺术在贵霜统治期间达到了顶峰。
H.G. Rowlinson评论道:
贵霜时期是笈多时代的一个恰当的前奏。
到了 3 世纪，他们在印度的帝国正在瓦解，他们最后一位已知的伟大皇帝是瓦苏德瓦一世。'''),
            History(times='笈多帝国',text='''笈多帝国大约在公元 320 年至 600 年间存在，并控制了印度河和斯瓦特河谷的大部分地区，直到约 465 年，这个帝国在公元 414 年左右达到最大范围，覆盖了南亚北部的大部分地区，包括现代巴基斯坦，但不包括南部半岛地区。[71]该王朝由大君斯里-古普塔（Maharaja Sri-Gupta）创立，是古典文明的典范，并以广泛的发明和发现为标志。
这种文化创造力的高潮是宏伟的建筑、雕塑和绘画。在笈多时代，科学和政治管理达到了新的高度。强大的贸易联系也使该地区成为重要的文化中心，并使该地区成为影响缅甸，斯里兰卡，东南亚海上和印度支那附近王国和地区的基地。
帝国逐渐衰落，部分原因是他们自己昔日的封建统治造成的领土和帝国权威的丧失，以及公元460年代初来自中亚的胡纳斯人的入侵，在6世纪笈多帝国崩溃后，南亚再次被许多地区王国统治。帝国解体后，笈多氏族的一个小家族继续统治摩揭陀。这些笈多最终被瓦尔达纳国王哈尔沙驱逐，后者在 7 世纪上半叶建立了一个帝国。'''),
            History(times='阿拉伯哈里发',text='''在从拜占庭帝国和萨珊帝国征服中东后，拉希敦哈里发到达了今俾路支省的马克兰沿海地区。643 年，第二任哈里发奥马尔（634-644 年在位）下令入侵马克兰对抗拉伊王朝。在拉希敦占领马克兰后，奥马尔限制军队不得越过并巩固他在马克兰的阵地。在第四任哈里发阿里（656-661 年在位）统治期间，拉希敦军队征服了俾路支省中部的卡拉特镇。在第六任倭马亚王朝哈里发瓦利德一世（705-715 年在位）统治期间，阿拉伯军事将领穆罕默德·伊本·卡西姆指挥倭马亚王朝入侵信德省。712 年，他击败了印度教王公阿罗尔的达希尔（695-712 年在位）的军队，并建立了信德的哈里发省。历史悠久的曼苏拉镇被管理为该省的首府。之后，伊本·卡西姆开始征服木尔坦，木尔坦随后成为伊斯兰文化和贸易的重要中心。747 年，反倭马亚叛军曼苏尔·伊本·朱姆胡尔·卡尔比占领了信德，并被继任的阿拔斯王朝哈里发的穆萨·伊本·卡布·塔米米击败。在9世纪，阿拔斯王朝在信德和木尔坦的权威逐渐衰落。第十任阿拔斯王朝哈里发穆塔瓦基勒（847-861 年在位）将信德总督职位授予奥马尔·伊本·阿卜杜勒·阿齐兹·哈巴里，后者建立了世袭的哈巴里王朝，并于 854 年成为信德的自治统治者。大约在同一时间，古莱什的巴努·穆纳比（Banu Munnabih）建立了木尔坦酋长国。在南部，特别是在占多数的印度教徒和佛教徒中，逐渐皈依伊斯兰教，但在木尔坦以北的地区，印度教徒和佛教徒仍然很多。到公元10世纪末，该地区由几位印度教国王统治。'''),
            History(times='喀布尔和印度教沙希斯',text='''突厥沙希人从 3 世纪贵霜帝国衰落开始统治犍陀罗，直到 870 年被印度教沙希斯推翻。印度教沙希人被认为属于 Uḍi/Oḍi 部落，即犍陀罗的 Oddiyana 人。
第一任国王卡拉尔将首都从喀布尔迁入乌达班达普勒，位于现代的洪德村，作为其新首都。[85][86][87][88]在鼎盛时期，王国在阇耶帕拉的领导下横跨喀布尔山谷、犍陀罗和旁遮普西部。[89]贾亚帕拉看到了加色尼王朝巩固的危险，并在塞布克蒂金和他的儿子马哈茂德统治时期入侵了他们的首都加兹尼，这引发了穆斯林伽色尼王朝和印度教沙希的斗争。然而，Sebuk Tigin击败了他，他被迫支付赔偿金。贾亚帕拉拖欠了付款，并再次上战场。然而，贾亚帕拉失去了对喀布尔河谷和印度河之间整个地区的控制。
然而，军队在与西方军队的战斗中被击败，特别是与加兹尼的马哈茂德的战斗。1001年，苏丹马哈茂德上台后不久，在兴都库什山脉以北被喀喇汗王朝占领，斋帕尔再次进攻加兹尼，并在今白沙瓦附近再次遭到强大的伽色尼军队的失败。白沙瓦战役后，他因后悔而死，因为他的臣民给沙希王朝带来了灾难和耻辱。
贾亚帕拉由他的儿子阿南达帕拉继位,他与沙希亚王朝的其他后代一起参加了反对前进的加兹维德人的各种不成功的战役，但没有成功。印度教统治者最终将自己流放到克什米尔西瓦利克山。'''),
            History(times='伽色尼王朝',text='''公元 997 年，突厥统治者加兹尼的马哈茂德接管了由他的父亲突厥裔统治者塞布克特金建立的伽色尼王朝帝国。从加兹尼市（今阿富汗）开始，穆罕默德征服了呼罗珊的大部分地区，于 1005 年向白沙瓦进军，对抗喀布尔的印度教沙希，随后征服了旁遮普邦（1007 年），废黜了木尔坦（1011 年）、克什米尔（1015 年）和卡诺赫（1017 年）的什叶派伊斯玛仪统治者。到 1030 年统治结束时，马哈茂德的帝国从西部的库尔德斯坦短暂扩展到东部的亚穆纳河，伽色尼王朝一直持续到 1187 年。当代历史学家，如阿博尔法兹尔·贝哈奇（Abolfazl Beyhaqi）和费尔多西（Ferdowsi），描述了拉合尔的大量建筑工程，以及马哈茂德对学习、文学和艺术的支持和赞助。
马哈茂德的继任者，被称为伽色尼王朝，统治了 157 年。他们的王国逐渐缩小，并受到激烈的继承斗争的折磨。印度西部的印度教拉其普特王国重新征服了旁遮普邦东部，到 1160 年代，伽色尼王朝和印度教王国之间的分界线接近今天的印度和巴基斯坦之间的边界。阿富汗中部的古尔德帝国在 1160 年左右占领了加兹尼，伽色尼王朝的首都迁至拉合尔。后来穆罕默德·古里征服了伽色尼王国，于 1187 年占领了拉合尔。'''),
        ]
        for record in test_records:
           
            obj, created = History.objects.get_or_create(times=record.times, defaults={'text': record.text, 'time_now': datetime.now()})
            if not created:  #如果没有添加进数据库 就添加  添加过的如果有所变化  就更新
                obj.text = record.text  #把新的正文内容放进去
                obj.time_now = datetime.now()   #保存新的更新时间
                obj.save()   #保存更新过的
        data_list=History.objects.all()  #把数据库里的数据都拿出来
        page = request.GET.get('page', 1)
        paginator = Paginator(data_list, 5)  # Show 10 items per page
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果page不是数字  显示第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果page超出范围  显示最后一页
            items = paginator.page(paginator.num_pages)
        return render(request,'history.html',{'data_list': items})



def diplomacy(request):
    if request.method == "GET":
        soup=to_get_content.to_get_content(request,r'https://storyofpakistan.com/events/the-mughal-empire/')
        return render(request,'diplomacy.html')


def culture(request):
    if request.method == "GET":
        soup=to_get_content.to_get_content(request,r'https://storyofpakistan.com/events/the-mughal-empire/')
        return render(request,'culture.html')

def test(request):
    if request.method == "GET":
        #把数据先放进test_records中
        test_records=[
        ]
        for record in test_records:
           
            obj, created = History.objects.get_or_create(times=record.times, defaults={'text': record.text, 'time_now': datetime.now()})
            if not created:  #如果没有添加进数据库 就添加  添加过的如果有所变化  就更新
                obj.text = record.text  #把新的正文内容放进去
                obj.time_now = datetime.now()   #保存新的更新时间
                obj.save()   #保存更新过的
        data_list=History.objects.all()  #把数据库里的数据都拿出来
        page = request.GET.get('page', 1)
        paginator = Paginator(data_list, 5)  # Show 10 items per page
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果page不是数字  显示第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果page超出范围  显示最后一页
            items = paginator.page(paginator.num_pages)
        return render(request,'test.html',{'data_list': items})

from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from Pakistan.models import History,Diplomacy,Culture,User
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
# Create your views here.

def welcome(request):
    if request.method == "GET":
        return render(request,'welcome.html')

def index(request):   #目录
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
           
            obj, created = History.objects.get_or_create(times=record.times, defaults={'text': record.text})
            if not created:  #如果没有添加进数据库 就添加  添加过的如果有所变化  就更新
                obj.text = record.text  #把新的正文内容放进去
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
        #把数据先放进test_records中
        test_records=[
            Diplomacy(country='巴基斯坦-美国',title='''冷战期间''',text='''1958年巴基斯坦军事政变后，阿尤布·汗改变了原来的不结盟立场，改为亲西方，先后加入了中央条约组织和东南亚条约组织。并在中美关系正常化时发挥了中介作用。随着苏联入侵阿富汗，其在资助阿富汗圣战者中也起到关键作用。然而随着苏联解体和冷战结束，巴基斯坦的地缘政治作用下降，美巴关系随之冷却。'''),
            Diplomacy(country='巴基斯坦-美国',title='''冷战结束后的关系''',text='''911事件发生后，穆沙拉夫领导的巴基斯坦军方随即加入了美国领导的反恐战争，为北约提供到阿富汗的补给路线。总计布什政府曾向巴基斯坦提供共124亿美元援助。奥巴马政府的援助则超过210亿美元。

2009年10月，美推出5年内向巴基斯坦提供75亿美元援助的“克里-卢格法案”。两国建立战略对话机制。

2011年奥萨马·本·拉登在巴基斯坦境内被美军击毙后，巴基斯坦逮捕涉嫌协助美国人确定本·拉登行踪的医生沙基勒·阿夫里迪，并以“叛国罪”等罪名判处其入狱33年（其叛国罪定罪其后被推翻，刑期亦最终被缩减至23年），引起美国不满。2015年美国不满巴基斯坦在反恐战争中作战不力，拒绝支付三亿美元的军援，作为对巴基斯坦的惩罚。

2018年1月1日，美国总统唐纳德·特朗普在推特上写道：“美国在过去15年愚蠢地给了巴基斯坦超过330亿美元的援助，而他们除了谎言和欺骗什么也没有给我们，把我们的领导人们当傻子。他们向我们在阿富汗搜捕的恐怖分子提供庇护所，没帮到什么忙。不会再有了！”随后美国国务院终止了对巴基斯坦的所有军事援助。

随着2021年美军完全撤出阿富汗和塔利班掌权，巴基斯坦时任总理伊姆兰·汗表示“阿富汗人打破了奴隶制的枷锁”。[7]美国政府和巴基斯坦的关系更加冷淡，美国总统拜登和印度总理莫迪的联合声明中要求巴基斯坦对跨境恐怖主义负责。'''),
            Diplomacy(country='巴基斯坦-美国',title='''21世纪''',text='''尽管2022年4月以来巴美关系有所改善，但这在很大程度上是相较于特朗普时期双边关系跌至冰点的触底反弹。相比冷战时期乃至21世纪初反恐战争时期，今日之巴美双方在政治互信、经济协调、安全合作和外交配合等诸多领域都存在尖锐矛盾'''),
            Diplomacy(country='巴基斯坦-中国',title='''20世纪四十年代-20世纪六十年代''',text='''1947年8月14日，因印巴分治，原英属印度被分为印度联邦与巴基斯坦自治领，中华民国在当天承认巴基斯坦自治领独立并建立外交关系，直至1950年1月巴基斯坦正式承认中华人民共和国后为止。
中国和巴基斯坦的关系友好，双方官方称双方关系为“全天候战略合作伙伴关系”，“ 两国的长久友好关系建基于互信、互惠互利和互不干涉内政等原则”。中国政府用“好邻居、好朋友、好兄弟、好伙伴”这一组词语形容中巴关系，并且视巴基斯坦为关系最良好的国家之一。巴方官员也多次强调中巴之间是“特殊的关系”，而巴基斯坦往往被中国人称为“巴铁”。'''),
            Diplomacy(country='巴基斯坦-中国',title='''20世纪后半叶''',text='''巴基斯坦也是中国和西方国家的关系在冷战中后期正常化的重要桥梁。 1960年代，中国受到西方国家和前苏联集团的双重孤立，也和印度爆发战争； 巴基斯坦也因克什米尔主权问题和印度处于敌对关系，在1965年爆发第二次印巴战争。 然而巴基斯坦因为地缘关系，成为西方抵抗前苏联南下印度洋的桥头堡。美国在越战战败，导致对华外交政策改变，1970年在巴基斯坦的协助下，中美两国双方秘密接触，促成美国国家安全顾问基辛格在1971年访华，奠定中华人民共和国取得联合国席位和中美建交的基础。

1979年，前苏联入侵巴基斯坦的北方邻国阿富汗，印度也相对偏向前苏联，巴基斯坦当局深感双重威胁，中国则强力支持巴基斯坦抵御前苏联对阿富汗的侵略。

1989年，中国发生六四事件时，巴基斯坦也是少数几个支持中国政府的非社会主义国家。巴基斯坦在台湾问题、西藏问题上完全支持中华人民共和国，也反对西方国家干涉中国内政。'''),
            Diplomacy(country='巴基斯坦-中国',title='''21世纪初''',text='''2013年8月27日，中巴经济走廊秘书处在巴基斯坦首都伊斯兰堡设立。2014年2月，巴基斯坦总统侯赛因在对中国的国事访问中讨论了相关议题。两个月后，巴基斯坦总理谢里夫同中国国务院总理李克强会面讨论了项目的计划。2014年11月8日，在中国国务院总理李克强与巴基斯坦总理谢里夫的共同见证下，中国国家发展改革委副主任、国家能源局局长吴新雄与巴基斯坦水电部常秘穆罕默德·尤尼斯·达加签署了《中巴经济走廊能源项目合作的协议》。

2015年，也门战事突起，安全形势持续恶化。由于巴政府派出的飞机和两艘军舰一时无法满足上千名从也门撤离回国的巴公民的要求，当地情况也十分复杂，巴政府请求中方协助其撤离部分滞留在也门的公民。中方在接到这一请求后启动应急机制，协调有关各方，并派出了正在相关海域执行任务的中国军舰“临沂号”赴亚丁湾参与撤离救援行动。
2015年4月20日，在中国领导人习近平访问巴基斯坦期间，中巴之间签署了总共51个项目的合作协议和备忘录。
2017年4月，为对接“一带一路”建设，巴基斯坦当局计划在中巴经济走廊项下建设九个工业园。以利用巴基斯坦的资源和劳动力优势，吸引中国劳动密集型产业的转移，培育巴基斯坦的产业集群。5月，中国投资500亿美元，在巴基斯坦印度河流域建设5个水库。建成的水电站可释放的电能占巴基斯坦全国水电总量的2/3。此外，中巴两国还积极推动瓜达尔-新疆公路走廊建设，在配套的港口和高速公路建成后，巴基斯坦可以直接向中国西北地区输送海鲜等内陆地区少见的商品，巴政府预计相关贸易可带来约80亿美元的产值。
2018年1月4日，巴基斯坦央行宣布自当日起中国和巴基斯坦之间的双边贸易可以通过人民币进行结算，放弃美元结算。同期，巴基斯坦军方宣布确认采购中国054A型导弹护卫舰，并组建一支配备JF-17“枭龙”多用途战机的空军中队驻防俾路支省，以维护中巴经济走廊、震慑恐怖分子。
而巴基斯坦总理伊姆兰·汗曾在竞选期间批评中国没有给巴基斯坦带来繁荣，而是带来一场危机，并一度对中巴经济走廊持保留态度。
2020年3月5日，中华人民共和国国家新闻办公室举办新闻发布会，称巴基斯坦将全国医院的口罩库存捐出，以支援中华人民共和国抗击新冠状病毒肺炎疫情。'''),
            Diplomacy(country='巴基斯坦-印度',title='''印巴分治''',text='''1947年6月3日，印度总督蒙巴顿公布《印度独立法案》，将英属印度按照宗教信仰分为印度和巴基斯坦两个自治领并保留总督，分别成立制宪议会和政府。1947年8月14日巴基斯坦宣布独立，真纳就任巴基斯坦总督和制宪议会主席。印度在第二天宣布独立，贾瓦哈拉尔·尼赫鲁就任印度总理，英国的殖民统治宣告结束。
                      然而查谟-克什米尔土邦的归属问题导致了两国开始了第一次印巴战争。'''),
            Diplomacy(country='巴基斯坦-印度',title='''印巴冲突''',text='''1965年4月至1965年9月间印度与巴基斯坦发生了为期五个月的战争造成双方数千人伤亡，史称第二次印巴战争。这场战争在联合国授权下停火，之后两国发表了《塔什干宣言》。1971年12月，两国再次发生战争，史称第三次印巴战争。1971 年的战争导致巴基斯坦投降并成立了一个名为孟加拉国的新国家。1999年5月至7月之间，巴基斯坦军队越过了印度控制线，进入了印控地区。印度军队展开代号为“胜利行动”(Operation Vijay)的反击作战，史称卡吉尔战争。2019年2月26日，印度空军战机空袭巴基斯坦境内的恐怖组织营地，两国在具争议性的克什米尔地区互相炮击，导致多人伤亡，巴基斯坦在27日表示，该国军方当天在该国领空击落两架印度战机。
                      此后克什米尔地区的归属一直没有得以解决，目前双方以联合国所划控制线为准分别控制，但边境交火事件时有发生。'''),
            Diplomacy(country='巴基斯坦-印度',title='''领土争端''',text='''克什米尔是青藏高原西部和南亚北部的交界处的一个地区，面积22万8478平方公里。巴基斯坦和印度均宣称对此拥有主权。1948年两国经联合国干预进行停火谈判。两国军队均后撤至停火线之后，但归属问题至今未能得以解决。
                      1971年巴印因第三次印巴战争断交，1976年复交。
                      2019年，两国又因查谟-克什米尔邦自治地位问题导致双边外交关系级别降低、贸易中断。'''),
            Diplomacy(country='巴基斯坦-以色列',title='''以巴冲突起源''',text='''巴以冲突始于1880年代巴勒斯坦地区阿拉伯人与犹太人之间的冲突。自公元135年被罗马帝国驱逐出以色列地以来，许许多多流亡海外的犹太人一直试图返回故土，18世纪以后有数波小型的回归潮，从数百到上千人不等。第一次大规模的回归浪潮则始于1881年，散居在世界其他地区的犹太人为了逃避迫害，开始回流到以色列地，即古迦南之地或古犹太国之地，今巴勒斯坦地区。犹太人从奥斯曼帝国和阿拉伯人手中购买土地并定居。

1896年，维也纳记者和剧作家西奥多·赫茨尔发起锡安主义（又称“犹太复国主义”）运动，号召全世界犹太人回归故土，恢复本民族的生活方式。1897年8月29日在瑞士巴塞尔，他召集了第一届“世界锡安主义大会”，大会决议建立“一个得到公众承认的、有法律保障的家园（或国家）”。
                      “犹太国民基金”和“巴勒斯坦土地开发公司”等相应机构成立，帮助世界各地的犹太人移居巴勒斯坦。'''),
            Diplomacy(country='巴基斯坦-以色列',title='''以巴冲突发展''',text='''一战中，1915年，在丘吉尔的主导下，英法军队对奥斯曼帝国发动了加里波利之战，遭遇惨败。随后英国军官阿拉伯的劳伦斯组织当地以贝都因人部落为主的军事力量与奥斯曼帝国作战，有效削弱了奥斯曼帝国的势力。1918年一战结束后，奥斯曼帝国完全退出此地区并于1923年瓦解，而阿拉伯部落之间纷争不断，最后默认由英国占领。1920年，国际联盟委托英国管辖巴勒斯坦地区，包含今约旦、巴以地区。1922年英国将托管地划分为两部分：约旦河东部（现约旦）由哈希姆家族实际管理，约旦河西部由英国控制，此时这些地区犹太人占总人口的11%，与阿拉伯人混居。第一次世界大战后，犹太人掀起了第三和第四次回归浪潮。1931年，犹太人占当地总人口的17%。接着在1933年，纳粹党在德国执政，掀起第五次犹太人回归浪潮。1936年巴勒斯坦阿拉伯人大起义后，英国的皮尔委员会在1937年首次提议将巴勒斯坦地区划分为犹太国和阿拉伯国。1940年，犹太人已占当地居民总数的30%。随着犹太居民比例从1922年的11%增涨至1940年的30%，犹太人与阿拉伯人之间的关系也日趋紧张。对此英国在1939年颁布了一份白皮书，规定1939年后的5年内犹太人可再移民75,000人，此后不再接受犹太移民。许多犹太人和锡安主义者视这份白皮书为对犹太人的背叛，认为此举违背了《贝尔福宣言》，
                      亦有犹太人持不同意见。阿拉伯人的抗议活动并没有就此平息，他们希望托管地政府完全停止准许犹太人移居当地。
                      二战中的犹太人大屠杀进一步推动了犹太人的回归，犹太人复国的理念也越来越强烈。1944至1948年之间，约20万犹太人通过各种途径辗转来到巴勒斯坦地区。第二次世界大战结束后，巴勒斯坦地区已经有60万犹太居民，占当地总人口约1/3。1947年，犹太人已拥有该地区7.4%的土地。
                      此时，该地区的土地11.6%为巴勒斯坦阿拉伯人所有，6.9%为外籍人士所有，70.6%仍为托管地政府所有。
                      
                      1947年，鉴于犹太人与阿拉伯人之间的暴力冲突不断升级，和平努力受到挫败，英国政府决定从巴勒斯坦托管地脱身。联合国成立了“巴勒斯坦专门委员会”。1947年11月联合国大会表决了第181号决议，33国赞成（包括美国和苏联），13国反对，10国弃权（包括英国），通过决议：将巴勒斯坦地区分划为两个国家，犹太人和阿拉伯人分别获得大约55%和45%的领土，联合国计划将耶路撒冷置于国际管理之下，以期避免冲突。分治方案在已开发领土上大致采取照顾传统聚居点、按人口比例均分的原则，结果划出多块相互交错的领土；考虑到未来大量犹太难民的迁入，以及犹太国将有的阿拉伯裔公民，将南部人烟稀少的沙漠地区内盖夫划入犹太国，故犹太人以1/3的人口获得了55%的领土。联大决议使当时拥有巴勒斯坦地区7.4%的土地、占该地区人口1/3的犹太人得到该地区56%的土地（约1.52万平方公里），而拥有该地区11.6%的土地、占该地区人口2/3的巴勒斯坦阿拉伯人则得到43%的土地（约1.15万平方公里）。[7]大卫·本-古里安在联合国通过分划方案的当日接受了该方案，
                      但阿拉伯国家联盟认为“联合国无权插手当地事务”而不予接受，而托管国英国则在对决议表决时弃权。'''),
            Diplomacy(country='巴基斯坦-以色列',title='''中东战争''',text='''在以色列建国之后，由埃及、伊拉克、约旦、叙利亚、黎巴嫩等国组成的阿拉伯联军向以色列发起攻击，引发了以色列独立战争，又称第一次中东战争。
                      
                      北边的叙利亚、黎巴嫩和伊拉克军队都在接近边界的地方被阻挡下来，来自东方的约旦军队则攻下耶路撒冷的东部，并且对城市的西部展开攻击。不过，犹太人的民兵部队成功的阻挡了约旦军队，而地下的国民军组织部队伊尔贡也阻止了来自南方的埃及军队。
                      
                      
                      大量的阿拉伯人口在战争中逃离新成立的犹太国家，阿拉伯人将此次流亡称为“大灾难”（النكبة, Nakbah），估计有400,000至900,000名阿拉伯人流亡，后来称为巴勒斯坦难民，联合国估计有711,000人。战争结束后，以色列不许这些巴勒斯坦难民重返家园。以色列与阿拉伯国家之间未解决的冲突、以及巴勒斯坦难民的问题一直持续至今。
                      1967年5月，叙利亚、约旦、埃及透露了开战的可能，埃及驱逐了在加沙地带的联合国维和部队，并封锁了以色列战略要地的堤蓝海峡，接着又在以色列边界部署大量的战车和战机。以色列于是在6月5日对埃及展开攻势，击败了所有阿拉伯的军队，并且在空军战场上获得完全的胜利。此次战争被称为第三次中东战争，又称六日战争。以色列一口气夺下了整个西岸地区、加沙地带、西奈半岛、和戈兰高地，1949年划定的绿线则变成以色列管辖本国领土和占领区域的行政分界线。

1973年10月6日，正值犹太教的赎罪日当天，埃及和叙利亚等阿拉伯联军对以色列发起突袭攻势，分别攻击六年前六日战争中被以色列占领的西奈半岛和戈兰高地。巴勒斯坦也派出部队支援阿拉伯联军，是为第四次中东战争，又称赎罪日战争。作为代理人战争，苏联支持阿拉伯国家，美国支持以色列；尽管阿拉伯联军在战争初期成功打击准备不足的以色列军队，随着美军向以色列提供卫星侦察结果，主导制定战略，并紧急调遣美国空军F-4鬼怪式多用途战机，在涂改军徽后，由美国飞行员从美国本土起飞，经多次加油飞至以色列，作为以色列空军直接参战，埃及和叙利亚最终仍被以色列击退。战后的几年局势变得较为平静，以色列和埃及终得签署和平协议。

为了报复美国支援以色列，阿拉伯石油输出国组织（OAPEC）、石油输出国组织（OPEC）里的阿拉伯国家，由沙特阿拉伯领导，在10月17日决定每个月减低石油产量5%，并威胁彻底禁运。然而美国总统尼克森还是在10月18日向美国国会请求提供了以色列22亿美元的军火。利比亚立即宣布对美国实行石油禁运。由此又导致第一次石油危机，直至1978年，在美国斡旋下签订《戴维营协议》，以色列将西奈半岛还给埃及，“石油危机”得以缓解。'''),
            Diplomacy(country='巴基斯坦—土耳其',title='''肇建之前''',text='''双边外交关系可追溯至两国肇建之前，更准确地说是在土耳其独立战争期间，当时英属印度西北部的穆斯林向衰落的奥斯曼帝国提供财政援助，随后成立了新的土耳其共和国和独立的巴基斯坦。此外，这些国家有着历史上的伊斯兰联系，因生活在英属印度治下的穆斯林将奥斯曼苏丹视为他们的哈里发，而伊斯兰教的哈里发是世界所有穆斯林的共主。结果，几十年来，巴基斯坦和巴基斯坦人在土耳其和土耳其人中享有积极的看法。巴基斯坦和土耳其有着密切的文化、历史和军事关系，随着两国都寻求经济发展，目前正逐步扩大深化经济关系。土耳其支持巴基斯坦在联合国下举行公民投票以决定克什米尔是否想加入巴基斯坦的立场，土耳其总统埃尔多安在向巴基斯坦议会发表的联合讲话中重申了这一立场，巴基斯坦军方最高指挥部出席了会议。土耳其支持巴基斯坦成为核供应国集团的成员。 根据塔拉特·马苏德（英语：）所述，土耳其和巴基斯坦在民主宪政和军事独裁时期都享有密切的关系，反映了两国关系的深密程度。
                      两国享有友好关系，通常被称为Kardeşler（即土耳其语中的“兄弟”）。'''),
            Diplomacy(country='巴基斯坦—土耳其',title='''建交之初''',text='''土耳其和巴基斯坦于1947年建立外交关系，在巴基斯坦独立成为当时全球规模最大的穆斯林国家后不久。土耳其是少数在巴基斯坦独立后即迅速承认并支持其成功申请成为联合国会员的国家之一，
                      缘于两国之间的文化、宗教和地缘政治联系，使双边关系日益密切。'''),
            Diplomacy(country='巴基斯坦—土耳其',title='''首脑外交''',text='''巴基斯坦国父穆罕默德·阿里·真纳对土耳其国父穆斯塔法·凯末尔·阿塔图尔克有仰慕、钦佩的情谊，并希望按照土耳其的现代主义模式发展巴基斯坦。同样，追随真纳和穆罕默德·伊克巴勒的脚步发展的现代化伊斯兰巴基斯坦和所有其他所谓的主义都曾被传统的巴基斯坦人民排斥。 巴基斯坦前总统佩尔韦兹·穆沙拉夫也表达了类似想法，他在土耳其长大并在当地接受过广泛的军事训练。 真纳在土耳其被誉为“伟大领袖”，土耳其首都安卡拉的一条主要道路真纳大道（英语：）即以其命名，而巴基斯坦主要城市伊斯兰堡、卡拉奇、拉合尔、白沙瓦和拉尔卡纳皆有重要道路以土耳其之父“阿塔图尔克”命名。2009年10月26日，
                      土耳其总统雷杰普·塔伊普·埃尔多安被授予巴基斯坦最高公民奖章（英语：），是第四位在巴基斯坦议会发表讲话的国际领袖。'''),
        ]
        for record in test_records:
           
            obj, created = Diplomacy.objects.get_or_create(title=record.title, defaults={'text': record.text})
            if not created:  #如果没有添加进数据库 就添加  添加过的如果有所变化  就更新
                obj.text = record.text  #把新的正文内容放进去
                obj.title=record.title   #保存新的更新时间
                obj.save()   #保存更新过的
        data_list=Diplomacy.objects.all()  #把数据库里的数据都拿出来
        page = request.GET.get('page', 1)
        paginator = Paginator(data_list, 3)  # Show 10 items per page
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果page不是数字  显示第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果page超出范围  显示最后一页
            items = paginator.page(paginator.num_pages)
        countries=[]
        countries.append('巴基斯坦-美国')
        countries.append('巴基斯坦-中国')
        countries.append('巴基斯坦-印度')
        countries.append('巴基斯坦-以色列')
        countries.append('巴基斯坦—土耳其')
        return render(request,'diplomacy.html',{'data_list': items,'countries': countries,'test_records':test_records})


def culture(request):
    if request.method == "GET":
        #把数据先放进test_records中
        test_records=[
            Culture(aspect='南亚卡车艺术',text='''南亚卡车艺术（英语：Truck art in South Asia）是一种流行的地区装饰（regional decoration）形式，卡车上有精致的花卉图案及书法艺术。它尤其于巴基斯坦及印度甚为常见。

在阿富汗战争期间，由巴基斯坦人装饰、在巴基斯坦及阿富汗提供服务的卡车被部署在阿富汗各地的美国军队和承包商称为叮当卡车（jingle trucks）。
                    “叮当卡车”一词是由在阿富汗服役的美国军队创造的军事俚语，纵使它亦可能追溯到英国殖民时期。这个词的出现是因为卡车的保险杆上挂着的链条和下垂物（pendant）所发出的叮当声。
                    海德尔·阿里是最著名的卡车艺术家之一。
                    他自小接受父亲的训练，2002年，他在史密森尼民俗节上粉饰一辆巴基斯坦卡车，第一次引起国际关注。
                    印多尔卡车艺术家纳菲斯·艾哈迈德·汗（Nafees Ahmad Khan）在印度境内众所周知，32年来每天都在粉饰一辆卡车。
                    赛义德·普尔·巴德沙先生（Syed Phool Badshah，又称“Phool ji”）是一名非常有名的卡车艺术家，
                    以其运用卡车艺术作美术的独特风格而闻名。
                    在巴基斯坦，卡拉奇是卡车艺术的主要城市中心，纵使于拉瓦尔品第、斯瓦特、白沙瓦、奎达及拉合尔亦有其他中心。来自俾路支省及斯瓦特的卡车通常饰有大量的木质装饰，而来自拉瓦尔品第及伊斯兰堡则通常包含塑料作品。在信德装饰的卡车上，经常可以看到骆驼骨装饰，及以红色为主调的装饰。

在印度，德里艺术家提拉克·拉吉·迪尔（Tilak Raj Dhir）表示，他在卡车艺术（在整个国家首都辖区中盛行）中所加入的标语，会随着社会政治氛围的变化而时常更换。
                    旁遮普邦被视为印度卡车艺术的主要中心，当地除拥有独特的艺术风格外，亦汇聚了专业的艺术家。诗歌于整个北印度（尤其是北方邦）的卡车艺术中实属司空见惯。
                    卡车艺术在印地语和乌尔都语中，有时或会称作“Phool Patti”。'''),
            Culture(aspect='国家象征',text='''
            1.石鸡：石鸡（学名：Alectoris chukar）为雉科石鸡属的鸟类，俗名朵拉鸡、红腿鸡、嘎嘎鸡、鹧鸪。分布于欧洲、西伯利亚、阿富汗、伊拉克、伊朗、克什米尔以及中国大陆的新疆、青海、甘肃、经华北到东北的西南部等地，多生活于低山干燥山谷以及丘陵的岩坡和砂坡。该物种的模式产地在希腊。
                    
                    2.草地曲棍球：草地曲棍球，也称场地曲棍球（英语：Field hockey），是一种曲棍球运动。
                    比赛在曲棍球场上进行，分两队，
                    每队11人，分别担任守门员、前锋、前卫、后卫等。现行的曲棍球规则当中，比赛时间为60分钟，
                    并分为4节、每节15分钟，第1节和第3节比赛结束之后休息2分钟，中场休息15分钟。在2014年规则修改之前，
                    比赛时间则为70分钟，分上下两半时，中场休息5-10分钟。比赛时，每人手执一根曲棍，用其平面击球，
                    以射入对方球门多者为胜。其位置打法与足球运动相近，通常采用5-3-2阵形和4-3-3阵形，常用技术有挥击球、运球、接球、铲击球、推击球、推球、守门员踢球等。
                    跟高尔夫球不同的地方：为免混淆，曲棍不设左撇子版本。'''),
            Culture(aspect='国家格言',text='''“虔诚，统一，戒律”（乌尔都语：ایمان، اتحاد، نظم），又译为“有纪律，就有团结”，是巴基斯坦的国家格言，被视为巴基斯坦的指导原则。
            、巴基斯坦独立后，该国国父、首任巴基斯坦总督穆罕默德·阿里·真纳提出这条格言。这条格言还以乌尔都语书写在该国的国徽底部。
                    这句格言由巴基斯坦的国父、首任总统穆罕默德·阿里·真纳提出。真纳通过这一格言，向他那个时代的年轻人灌输了一种信息。他通过这一格言及其围绕这一格言发表的讲话，
                    教导巴基斯坦的青年关于建设国家、团结一致的重要性。他注重强调教育和纪律，并认为年轻人是一个国家的重要财富。
                    巴基斯坦建国四个月后，1947年12月28日，真纳说：

我们正经历烈火，太阳还没有出来。但我毫不怀疑，只要虔诚，统一和戒律，我们就能与世界上任何一个国家相匹敌。你们准备好经受烈火的考验了吗？你们现在必须下定决心。我们必须摒弃个人主义和狭隘的嫉妒，下决心以诚实守信的态度为人民服务。我们正在经历一个充满恐惧、危险和威胁的时期。我们必须有虔诚，统一和戒律。

而在1948年9月11日，真纳发表了他最后的讲话：

我们国家的基础已经奠定，现在是你们尽快、尽可能地建设国家的时候了。巴基斯坦为她的青年感到自豪，尤其是学生，他们是明天国家的建设者。他们必须通过纪律、教育和训练来充分装备自己，以应付摆在他们面前的艰巨任务。有了虔诚，统一，戒律和对责任的无私奉献，就没有你做不到的有价值的事情。

1954年，巴基斯坦中央政府批准了关于该国国徽的法案，这一著名格言以乌尔都语被书写在国徽上。此后，这一格言被视为巴基斯坦的指导原则。'''),
            Culture(aspect='宗教',text='''伊斯兰教，巴基斯坦的国教。穆斯林占大约96％的人口（1998年人口普查）。巴基斯坦的穆斯林人数在世界上排名第二，仅次于印尼。91％的巴基斯坦人逊尼派，5％人口什叶派(数字介于17万至30万)。
                           基于南亚两个国家不同的宗教（伊斯兰教和印度教）和不同历史背景、文化和社会习俗的基础上，
                    穆斯林诗人和哲学家阿拉马穆罕默德·伊克巴尔于1930年在阿拉哈巴德穆斯林联盟首先提出成立一个穆斯林国家的想法，他建议旁遮普省、信德省、俾路支省和西北边境省应成为巴基斯坦的一部分。 
                    巴基斯坦建国后，巴基斯坦伊斯兰教和政治就一直密不可分。1977年，佐勒菲卡尔·阿里·布托政府禁止酒精和毒品，在齐亚·哈克时代实行伊斯兰化政策。实行沙里亚法与政府部门一天五次祈祷及实施伊斯兰金融系统。

另外当地的亵渎法被认指滥用以迫害当地的少数宗教，例如基督徒。'''),
            Culture(aspect='乌尔都语',text='''乌尔都语（乌尔都语：اُردُو）是属于印欧语系印度-伊朗语族的印度-雅利安语支。
                    从使用人数来看，乌尔都语大约排名世界第20名，是巴基斯坦的国语，也是印度的24种规定语言之一。
                    如果从宏观角度来看，乌尔都语可看成是印度斯坦语的一部分，所有印度斯坦语言构成世界上第四大的语言。
                    在1200年到1800年，南亚在德里苏丹国和莫卧儿帝国的统治下，
                    乌尔都语受到波斯语、突厥语、库尔德语和阿拉伯语的影响。乌尔都文有37或38个字母。
                    乌尔都语母语使用者大约有6-8千万人，其中5千2百万在印度（2001年），占当时该国人口的6%；1千3百万在巴基斯坦（2008年），占该国人口的8%；另有散布在世界各地的母语者。

在巴基斯坦的城市中，乌尔都语在大多数人中能通用，
                    其中包括卡拉奇、伊斯兰堡、拉合尔、拉瓦品地、白沙瓦、奎达、海得拉巴、古吉兰瓦拉、费萨拉巴德、木尔坦和苏库尔。乌尔都语是巴基斯坦所有省份的官方语言，尽管该国有93%的人口不以它为母语。在同时使用英语和乌尔都语的学校中，直至高中前，乌尔都语是强迫性学习的语言。这样就使数以百万计以旁遮普语、信德语、普什图语、克什米尔语、俾路支语、西莱基语、布拉灰语等为母语的使用者的人，都能使用乌尔都语，乌尔都语也成为了巴基斯坦国家团结的象征，并成为巴基斯坦的主要交际语。它混合了巴基斯坦不同地区的词汇；同样，巴基斯坦不同地区的语言也受到乌尔都语的词汇影响。5百万来自不同民族（如普什图族、塔吉克族、乌兹别克族、哈扎拉族、土库曼族等）的阿富汗难民，在巴基斯坦居住了超过25年以后，都能操流利乌尔都语。这样可推论出，使用乌尔都语的中心，
                    已由印度的德里和勒克瑙，转而到巴基斯坦的卡拉奇和拉合尔。
                    '''),
            Culture(aspect='巴基斯坦穆斯林的种姓',text='''南亚的穆斯林与其他地方的穆斯林不同，他们受印度文化同化而接受了种姓制度。但程度上较温和。
                    印度的穆斯林可分为两种：一种是阿失拉甫（祖先是阿拉伯人、突厥人、阿富汗人、莫卧儿部落），一种是本地皈依者。前者认为自己地位较高，这分层中世纪已有，在图格鲁克王朝突厥穆斯林独揽大权，而不是起源于印度的穆斯林。苏丹国也不欢迎本土穆斯林。

除了此两大分类外，内部也可细分为多个种姓。本地皈依者多从事不干净工作，
                    如清除和搬运粪便，并被禁止入寺和使用公共墓地。南亚也有自己的婚姻圈，偏好与同一种姓结婚。'''),
            Culture(aspect='旁遮普文化',text='''旁遮普文化概括南亚旁遮普地区（包括印度旁遮普邦等地区、巴基斯坦旁遮普省）和旁遮普族的饮食、艺术、习俗、建筑等传统。
                    巴恩格拉是著名的旁遮普传统音乐型式之一，经典的巴恩格拉音乐必须有强烈的鼓声伴奏。在近年来旁遮普音乐也越来越受到西方国家的欢迎，甚至获得一些西方主流音乐的采用，搭配混音与混曲创造出别有南亚韵味的音乐。
                    历史悠久的旁遮普文化与民族具有相当丰富的舞蹈文化。旁遮普人通常会在特殊节气时跳舞庆祝，包括丰收、重要节日、与喜宴。舞蹈表演种类多样可与宗教有关联但也并不尽然，其中巴恩格拉属于较具有活力与爆发力的舞蹈，而Jhumar 和 Giddha 类型的女子舞蹈则较阴柔婉约。Bolis则是由女性边唱边跳所演出的舞蹈。
                    旁遮普饮食文化相当丰富与广泛，近年来在世界各地也都享有盛名，其中绿芥末叶泥(Sarson da Saag)与玉米圆面饼(Makki di roti)的搭配是最为著名的旁遮普食物。一般来说旁遮普主食是以小麦制成为主，稻米类的食物虽然可以找到但是并不常见。其他较为大众化的知名料理包括馕、酱鸡、印度羊起司(Paneer)、唐度里鸡、咖喱角、和炸鹰嘴豆饼(pakora)。另外，旁遮普盛产乳制品，牛奶成分在当地的甜点是不可或缺的一部分，具代表性的热门甜点有干酪粗面团汤圆、炼乳糕(barfi)、与甜乳凝球gulab jamun。在非甜点类的料理中加入优格或酪浆也是十分常见一种饮食习惯。
                    旁遮普文化拥有许多深奥与经典的诗文创作，其中包含了锡克教经典古鲁·格兰特·萨希卜。
                    传统的男性服装是会穿着Kurta，是一种搭配长裤、裁剪合身的长衫。由于旁遮普民族有许多锡克教徒，锡克教男性会在头上包裹头巾。女性的传统服饰包括Salwar，salwar kameez通常是由一件裙式长衫搭配长裤以及色彩鲜艳的长丝巾或披肩。另有一些女性会穿着旁遮普式长裙Punjabi ghagra。
                    旁遮普地区与民族每年皆会庆祝许多节气包括宗教性节日、季节性节日、或文化性节日。其中较为著名的有旁遮普冬季丰收祭(Maghi)、诗人Shah Hussain的忌日(Mela Chiraghan)、冬至(Lohri)、侯丽节、旁遮普新年(Vaisakhi)、女儿节(Teeyan)、排灯节、以及锡克教创始人的拿那克的诞辰(Guru Nanak Gurpurab)。'''),
            Culture(aspect='巴基斯坦世界遗产列表',text='''根据联合国教科文组织（UNSECO）1972年制订的《保护世界文化和自然遗产公约》，世界遗产是指对全人类有重要文化或自然价值的遗产项目[1]，常见文化遗产包括古迹（如建筑、雕塑、铭文）、建筑群、遗址（如考古遗址）；自然遗产通常是具备特殊物质和和生物价值的自然地貌、地质和自然地理结构（如濒危动植物栖息地），或从科学、保育、自然美角度具有突出的普世价值。巴基斯坦于1976年7月23日批准该公约后，其文化和自然遗产才有资格列入世界遗产名录。

截至2021年，联合国教科文组织已在巴基斯坦指定了6个世界遗产，均为文化遗产。分别为1980年入选的摩亨佐达罗考古遗迹、塔克西拉、塔克特依巴依佛教遗址和萨尔依巴赫洛古遗址；1981年入选的塔塔城的历史建筑、拉合尔古堡和夏利玛尔公园；1997年入选的罗赫达斯要塞。另外，有26项遗产列入预备名单，遗产入选为《世界遗产名录》前都必须列入预备名单。
                   1.摩亨佐达罗考古遗迹：摩亨佐达罗考古遗迹位于信德省，为一座大型考古遗迹，面积约2.4平方公里，其历史可追溯至公元前3,000年。此地有一座卫城，周围建有壁垒，从这些遗迹中我们可以看出早期城市规划的雏形。摩亨佐达罗考古遗迹于1922年被发现，1930年代曾大规模的挖掘，1965年后因出土的遗迹有风化、损毁的风险，因此挖掘工作全面停止，估计已开挖的部分约占该遗迹的三分之一。
                   2.塔克西拉：塔克西拉位于旁遮普省，为一个跨越多个时代的考古遗址。从中石器时代的坟墓、公元前200年锡尔凯波的防御工事、公元1世纪的锡尔苏克城，可以了解这座位于印度河畔城市的发展历程。它在各个时期分别受到了波斯、希腊和中亚文化的影响。从公元前5世纪到公元2世纪，这座城市还是重要的佛学中心。
                    3.塔克特依巴依佛教遗址和萨尔依巴赫洛古遗址：塔克特依巴依佛教遗址与萨尔依巴赫洛古遗址位于开伯尔-普什图省，塔克特依巴依是一组佛教寺庙建筑群，建于1世纪早期，位于一座152米高的山顶上，附近有萨尔依巴赫洛古遗迹。萨尔依巴赫洛是同一时期的一座小型、具有防御设施的城市，内有多个佛教相关遗迹。 '''),
            Culture(aspect='巴基斯坦独立日',text='''巴基斯坦独立日（英文：Yom-e-Istiqlal、乌尔都语: یوم استقلال) 是巴基斯坦的国家假期，定于每年的8月14日。
                    该日为纪念巴基斯坦于1947年的8月14日（星期四）中午12时宣布从英国长期控制的印度帝国中独立，改成共和联邦的自治领，正式脱离英国管辖。'''),
            Culture(aspect='巴基斯坦式中国菜',text='''巴基斯坦式中国菜（乌尔都语：چینی پکوان）指的是在巴基斯坦创造的，具有当地特色的中国菜。巴式中菜源自移居当地的巴基斯坦华人，是一套独特的，结合了中国和巴基斯坦饮食特色的菜系。
                    巴式中菜起源自1930年代位于现属巴基斯坦的地区的中菜馆。前中华人民共和国总理周恩来曾光顾位于卡拉奇的ABC中菜馆，这家中餐馆持续营业至1988年。

巴式中菜的特色与广东菜有其相近之处。巴式中菜口味以甜、酸、辣为主，在调味上偏好使用番茄酱、酱油、辣椒酱、醋和味精，而罕用新鲜香料。巴式中菜在巴基斯坦相当受欢迎，特别是如“满洲鸡”、中式肉串等当地发明的混合菜。

一些新开业的中菜餐厅，如Ginsoy在卡拉奇蓬勃发展。卡拉奇的中菜馆提供的菜式揉合了中国和巴基斯坦的烹饪风格。截至2008年，在首都伊斯兰堡的Phoenix中餐厅也变得广为人知，著名食客包括了巴基斯坦前总统佩尔韦兹·穆沙拉夫和前总理肖卡特·阿齐兹。据报导，穆沙拉夫尤其喜爱该餐厅的龙虾、北京烤鸭、炒牛肉和蒜香羊排。而广受欢迎的巴式中菜“满洲鸡”则是一道由印度的中餐厅所发明的菜式，以辣味见称，并与传统中菜的作法有着天渊之别。
另外，自从2013年起中巴经济走廊计划的开展以来，中餐厅在巴基斯坦的主要城市中，有如雨后春笋般涌现。与早年的巴式中菜相比，它们的菜式和口味相对贴近传统中菜，顾客群也以在当地生活的华人为主'''),
            Culture(aspect='性别歧视',text='''巴基斯坦女性面临着系统性的性别歧视，由于社会经济发展不平衡以及部落、封建和资本主义社会形态对女性生活的影响，在不同的阶级、地区和城乡之间女性地位存在很大差异。今天的巴基斯坦妇女享有比过去更好的地位。在现代巴基斯坦，女性可以担任高级职务，包括总理，国民议会议长，反对党领袖，以及联邦部长，法官和武装部队的将军。

自1980年代齐亚·哈克的伊斯兰化政策实施以来，巴基斯坦的许多宗教团体拥有了更多的政治权力，他们主张巴基斯坦女性的从属地位。甚至强奸受害者也未被允许使用 DNA证据证明其案件，不过最近全巴基斯坦乌里玛委员会发布了谴责“名誉杀人”的消息。在拉合尔成立了第一个女交通督导员服务机构来管理交通的同时，其他改进措施也在推行中，该国最保守的省份开伯尔-普赫图赫瓦省正在计划提高警察部队中女性的比例。

即使有了这些改善，猖獗的家庭暴力以及高比率的童婚和强迫婚姻仍然存在。'''),
            Culture(aspect='政治文化',text='''巴基斯坦实行两院制，设参议院及国民议会。参议院有100名议员，国民议会有342名议员，其中272名由分区普选产生，60席为妇女保留席位，10席为非穆斯林保留席位，由各政党按普选得票比例分配；国民议会设议长和副议长各1人，议员任期五年。参议院设100个议席，议员任期六年，每3年改选半数。设主席和副主席各1人，任期三年。

独立后的巴基斯坦，军方在政治一直担当重要角色，巴基斯坦于1958－1971年，1977－1988年及1999－2008年长期实行军政府统治。巴基斯坦建国后于1956年、1962年和1973年颁布三部宪法。此外，文人政府的不稳定和贪腐问题一直是国内的政治焦点。

2008年巴基斯坦恢复民主制后，首个文人政府完成五年任期。标志着巴基斯坦能够通过公正、透明的选举，由上一届民选政府和平地把权力移交给下一届民选政府。2013年6月，纳瓦兹·谢里夫就任总理。2017年8月，谢里夫被议会罢免，沙希德·哈坎·阿巴西就任总理。 2018年7月，伊姆兰·汗宣布赢得巴基斯坦大选，7月27日，巴基斯坦前执政党谢里夫派表示承认大选结果，接受伊姆兰·汗成为下一任总理。'''),
            Culture(aspect='地理位置',text='''巴基斯坦位于南亚，东与印度比邻，南面是印度洋，西与伊朗接壤，西北和阿富汗相连，东北面可通往中国新疆。面积为79.6万平方公里（不包括克什米尔），约等于法国和英国面积的总和，在全世界排第35位。国土南部沿阿拉伯海及阿曼湾有1,046千米（650英里）的海岸线，陆上边界总长6,774千米（4,209英里），分别为阿富汗2,430千米（1,510英里）、中国523千米（325英里）、印度2,912千米（1,809英里）及伊朗909千米（565英里）；与阿曼有海上边界，与塔吉克隔着寒冷、狭窄的瓦罕走廊。

巴基斯坦地势由西北向东南倾斜，全境五分之三为山地和高原，北有喜马拉雅山脉，西北有兴都库什山脉，东部为印度河中下游冲积平原，东南为塔尔沙漠的一部分。'''),
            Culture(aspect='气候',text='''巴基斯坦属亚热带干燥和半干燥气候，气候总的来说比较炎热干燥，每年平均降雨量不到250毫米，1/4的地区降雨量在120毫米以下。最炎热的时节是6、7月份，大部分地区中午的气温超过40℃，而在信德和俾路支省的部分地区中午气温则可能高达50℃以上。海拔高度超过２千米以上的北部山区比较凉爽，且温差大，昼夜平均温差14℃左右。气温最低时节是12月至2月。'''),
            Culture(aspect='行政区划及其主要城市',text='''巴基斯坦全国共有旁遮普、开伯尔－普什图、俾路支、信德4省。各省下设专区、县、乡、村联会。巴基斯坦实际控制的克什米尔的西北部一部分，划分为联邦管辖的阿扎德克什米尔和“临时省”吉尔吉特-巴尔蒂斯坦。阿扎德克什米尔地区的人民持巴基斯坦护照，享有对该地政府的选举权，不享有对中央政府的选举权。克什米尔地区的中部和南部土地肥沃最大的克什米尔谷地由印度控制。此外，1963年根据边境协定巴基斯坦将一部分巴控克什米尔（喀喇昆仑走廊）划给中华人民共和国。
                    另外印度声称拥有中国控制的阿克赛钦（属新疆和阗县）即克什米尔东北部主权。
                    
                    卡拉奇-信德省的首府，巴基斯坦最大城市和港口及商业中心，也是世界上人口最多的城市之一。
伊斯兰堡-巴基斯坦首都。
拉合尔-旁遮普省的首府。
拉瓦尔品第
白沙瓦-开伯尔-普什图省的首府。
费萨拉巴德
木尔丹
海德拉巴
苏库尔
吉尔吉特-吉尔吉特-巴尔蒂斯坦的首府。
奎达-俾路支省的首府。
瓜达尔位于俾路支省拥有深水港瓜达尔港。'''),

        ]
        for record in test_records:
           
            obj, created = Culture.objects.get_or_create(aspect=record.aspect, defaults={'text': record.text})
            if not created:  #如果没有添加进数据库 就添加  添加过的如果有所变化  就更新
                obj.text = record.text  #把新的正文内容放进去
                obj.aspect=record.aspect   #保存新的更新时间
                obj.save()   #保存更新过的
        data_list=Culture.objects.all()  #把数据库里的数据都拿出来
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
        

        return render(request,'culture.html',{'data_list': items})

# def login(request):
#     if request.method == "GET":
#         return render(request, "login.html")

#     username = request.POST.get("username")
#     password = request.POST.get("password")

#     # 查询数据库中是否存在匹配的用户名和密码
#     try:
#         user = User.objects.get(username=username, password=password)
#         # 登录成功，可以进行后续处理
#         return redirect("http://pakistannews.cn/index/")
#     except User.DoesNotExist:
#         return render(request, "login.html", {"error": "用户名或密码错误，请重新输入"})
    
# def register(request):
#     if request.method == "GET":
#         return render(request, "register.html")

#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     confirmpassword = request.POST.get("confirmpassword")

#     if confirmpassword == password:
#         # 创建用户并保存到数据库
#         user = User(username=username, password=password)
#         user.save()
#         return redirect(reverse('login'))
    
#     return render(request, "register.html", {"error": "两次输入的密码不一致，请重新输入"})

def login_or_register(request):
    if request.method == "GET":
        print("请求页面成功")
        return render(request, "login.html")

    username = request.POST.get("username")
    password = request.POST.get("password")
    confirmpassword = request.POST.get("confirmpassword")

    if "register-btn" in request.POST:
        print("开始注册")
        # 注册逻辑
        if confirmpassword == password:
            # 检查用户名是否已经存在
            if User.objects.filter(username=username).exists():
                print("用户名已存在")
                return render(request, "login.html", {"error": "该用户名已存在，请选择其他用户名"})
            
            # 创建用户并保存到数据库
            user = User(username=username, password=password)
            user.save()
            print("注册成功")
            return redirect(reverse('login'))
        else:
            print("密码不一致")
            return render(request, "login.html", {"error": "两次输入的密码不一致，请重新输入"})
    else:
        # 登录逻辑
        try:
            user = User.objects.get(username=username, password=password)
            # 登录成功，如果需要可以执行其他任务
            return redirect("http://pakistannews.cn/index/")
        except User.DoesNotExist:
            return render(request, "login.html", {"error": "用户名或密码错误，请重新输入"})
    
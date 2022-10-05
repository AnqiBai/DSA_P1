import sys
import heapq


class TreeNode:
    def __init__(self, value, freq, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.huffCode = ''
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_build_tree(data: str):
    minheap = []
    adict = dict()
    # get distinct chars and frequency
    for char in data:
        if char not in adict:
            adict[char] = 1
        else:
            adict[char] += 1

    # handle corner case:
    if len(adict.keys()) == 1:
        lNode = TreeNode(char, adict[char])
        lNode.huffCode = '0'
        dummyRoot = TreeNode('-'+char, adict[char], lNode)
        return dummyRoot

    for char in adict:
        heapq.heappush(minheap, TreeNode(char, adict[char]))

    while len(minheap) > 1:
        left = heapq.heappop(minheap)
        right = heapq.heappop(minheap)

        left.huffCode = '0'
        right.huffCode = '1'

        newNode = TreeNode(left.value + right.value,
                           left.freq+right.freq, left, right)

        heapq.heappush(minheap, newNode)

    # return the root node of the huffman tree
    return minheap[0]


def huffman_get_codes(root, codes, path):
    newPath = path + root.huffCode
    if root.left:
        huffman_get_codes(root.left, codes, newPath)
    if root.right:
        huffman_get_codes(root.right, codes, newPath)

    # if current node is a leaf node:
    if not root.left and not root.right:
        codes[root.value] = newPath

    return


def huffman_encoding(data):
    if not isinstance(data, str):
        print('Invalid input data type!')
        return
    if len(data) < 1:
        print('Empty input string!')
        return (None, None)
    treeRootNode = huffman_build_tree(data)
    codes = {}
    path = ''
    huffman_get_codes(treeRootNode, codes, path)
    result = ''
    for char in data:
        result += codes[char]
    return (result, treeRootNode)


def getChar(startloc, data, tree):
    node = tree
    loc = startloc
    while node.left or node.right:
        currentVal = data[loc]
        loc += 1
        if currentVal == '0':
            node = node.left
        else:
            node = node.right
    return (loc, node.value)


def huffman_decoding(data, tree):
    result = ''
    newFlag = True
    loc = 0
    steps = len(data)
    while loc < steps:
        newLoc, newChar = getChar(loc, data, tree)
        result += newChar
        loc = newLoc

    return result


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1 # test for encode
    data1 = 'A'*7 + 'B'*3 + 'C'*7 + 'D'*2 + 'E'*6
    encoded, treeRoot1 = huffman_encoding(data1)
    codes1 = {}
    huffman_get_codes(treeRoot1, codes1, '')
    assert codes1['E'] == '01'
    assert codes1['D'] == '000'
    assert codes1['C'] == '11'
    assert codes1['B'] == '001'
    # Test Case 2 # test for decode
    assert getChar(0, encoded, treeRoot1)[1] == 'A'
    # Test Case 3 # encode and decode
    encoded2, treeRoot2 = huffman_encoding('Hello Huffman Coding')
    assert huffman_decoding(encoded2, treeRoot2) == 'Hello Huffman Coding'
    # Test Case 4: edge case: sentence has a single character
    encoded3, treeRoot3 = huffman_encoding('*'*10)
    assert huffman_decoding(encoded3, treeRoot3) == '*' * 10
    # Test Case 5: edge case: test with a long string
    encoded4, treeRoot4 = huffman_encoding('*'*10 + 'A'*1000000)
    codes4 = {}
    huffman_get_codes(treeRoot4, codes4, '')
    assert codes4['*'] == '0'
    assert codes4['A'] == '1'
    assert huffman_decoding(encoded4, treeRoot4) == '*' * 10 + 'A'*1000000

    # Added test cases:
    # Test case 5: This test is for a large alphabet
    Chinese_Str = '''初学喊爸爸的小孩子，会出门叫洋车了的大孩子，嘴巴上长了许多白胡胡的老孩子，提到腊八粥，谁不口上就立时生一种甜甜的腻腻的感觉呢。把小米，饭豆，枣，栗，白糖，花生仁儿合并拢来糊糊涂涂煮成一锅，让它在锅中叹气似的沸腾着，单看它那叹气样儿，闻闻那种香味，就够咽三口以上的唾沫了，何况是，大碗大碗的装着，大匙大匙朝口里塞灌呢！
　　住方家大院的八儿，今天喜得快要发疯了。一个人出出进进灶房，看到那一大锅正在叹气的粥，碗盏都已预备得整齐摆到灶边好久了，但他妈总说是时候还早。
　　他妈正拿起一把锅铲在粥里搅和。锅里的粥也象是益发浓稠了。
　　“妈，妈，要到什么时候才……”
　　“要到夜里！”其实他妈所说的夜里，并不是上灯以后。但八儿听了这种松劲的话，眼睛可急红了。锅子中，有声无力的叹气正还在继续。
　　“那我饿了！”八儿要哭的样子。
　　“饿了，也得到太阳落下时才准吃。”
　　饿了，也得到太阳落下时才准吃。你们想，妈的命令，看羊还不够资格的八儿，难道还能设什么法来反抗吗？并且八 儿所说的饿，也不可靠，不过因为一进灶房，就听到那锅子中叹气又象是正在呻唤的东西，因好奇而急于想尝尝这奇怪东西罢了。
　　“妈，妈，等一下我要吃三碗！我们只准大哥吃一碗。大哥同爹都吃不得甜的，我们俩光吃甜的也行……妈，妈，你吃三碗我也吃三碗，大哥同爹只准各吃一碗；一共八碗，是吗？”
　　“是呀！孥孥说得对。”
　　“要不然我吃三碗半，你就吃两碗半……”“卜……”锅内又叹了声气。八儿回过头来了。
　　比灶矮了许多的八儿，回过头来的结果，亦不过看到一 股淡淡烟气往上一冲而已！
　　锅中的一切，这在八儿，只能猜想……栗子会已稀烂到认不清楚了罢，赤饭豆会煮得浑身透肿成了患水臌胀病那样子了罢，花生仁儿吃来总已是面东东的了！枣子必大了三四 倍——要是真的干红枣也有那么大，那就妙极了！糖若作多了，它会起锅巴……“妈，妈，你抱我起来看看罢！”于是妈就如八儿所求的把他抱了起来。
　　“噁……”他惊异得喊起来了，锅中的一切已进了他的眼中。
　　这不能不说是奇怪呀，栗子跌进锅里，不久就得粉碎，那是他知道的。他曾见过跌进到黄焖鸡锅子里的一群栗子，不久就融掉了。赤饭豆害水臌肿，那也是往常熬粥时常见的事。
　　花生仁儿脱了他的红外套，这是不消说的事。锅巴，正是围了锅边成一圈。总之，一切都成了如他所猜的样子了，但他却不想到今日粥的颜色是深褐。
　　“怎么，黑的！”八儿还同时想起染缸里的脏水。
　　“枣子同赤豆搁多了。”妈的解释的结果，是捡了一枚特别大得吓人的赤枣给了八儿。
　　虽说是枣子同饭豆搁得多了一点，但大家都承认味道是比普通的粥要好吃得多了。
　　夜饭桌边，靠到他妈斜立着的八儿，肚子已成了一面小鼓了。如在热天，总免不了又要为他妈的手掌麻烦一番罢。在他身边桌上那两只筷子，很浪漫的摆成一个十字。桌上那大青花碗中的半碗陈腊肉，八儿的爹同妈也都奈何它不来了。
　　“妈，妈，你喊哈叭出去了罢！讨厌死了，尽到别人脚下钻！”
　　若不是八儿脚下弃得腊肉皮骨格外多，哈叭也不会单同他来那么亲热罢。
　　“哈叭，我八儿要你出去，快滚罢……”接着是一块大骨头掷到地上，哈叭总算知事，衔着骨头到外面啃嚼去了。
　　“再不知趣，就赏它几脚！”八儿的爹，看那只哈叭摇着尾巴很规矩的出去后，对着八儿笑笑的说。
　　其实，“赏它几脚”的话，倘若真要八儿来执行，还不是空的？凭你八儿再用力重踢它几脚，让你八儿狠狠的用出吃奶力气，顽皮的哈叭，它不还是依然伏在桌下嚼它所愿嚼的东西吗？
　　因为“赏它几脚”的话，又使八儿的妈记起了许多他爹平素袒护狗的事。
　　“赏它几脚，你看到它欺负八儿，哪一次又舍得踢它？八 宝精似的，养得它恣刺得怪不逗人欢喜，一吃饭就来桌子下头钻，赶出去还得丢一块骨头，其实都是你惯死了它！”这显然是对八儿的爹有点挪揄了。
　　“真的，妈，它还抢过我的鸭子脑壳呢。”其实这也只能怪八儿那一次自己手松。然而八儿偏把这话来帮助他妈说哈叭的坏话。
　　“那我明天就把哈叭带到场上去，不再让它同你玩。”果真八儿的爹的宣言是真，那以后八儿就未免寂寞了。
　　然而八儿知道爹是不会把狗带到场上去的，故毫不气馁。
　　“让他带去，我宝宝一个人不会玩，难道必定要一个狗来陪吗？”以下的话风又转到了爹的身上，“牵了去也免得天天同八儿争东西吃！”
　　“你只恨哈叭，哈叭哪里及得到梁家的小黄呢？”
　　“要是小黄在我家里，我早就喊人来打死卖到汤锅铺子去了。”八儿的妈说来脸已红红的！
　　小黄是怎么一个样子，乃值得八儿的爹提出来同哈叭相较呢？那是上隔壁梁家一只守门狗，有得是见人就咬的一张狠口。梁家因了这只狗，几多熟人都不敢上门了。但八儿的妈，时常过梁家时，那狗却象很客气似的，低低吠两声就走了开去。八儿的妈，以为这已是互相认识的一种表示了，所以总不大如别人样对这狗防备。上月子，为八儿做满八岁的生日，八儿的妈上梁家去借碓舂粑粑，进门后，小黄突然一 变往日态度，毫不认账似的，扑拢来大腿腱子肉上咬了一口就走了。这也只能怪她自己，头上顶了那个平素小黄不曾见她顶过的竹簸。落后是梁四屋里人为敷上了止血药，又为把米粉舂好了事。转身时，八儿的妈就一一为他爹说了，还说那畜生连天天见面的人也认不清，真的该拿来打死起！因此一来，八儿的爹就找出一句为自己心爱这只哈叭护短的话了。
　　譬如是哈叭顽皮到使八儿的妈发气时，八儿的爹就把“比梁家小黄就不如了！”“那你喜欢小黄罢？”“我这哈叭可惜不会咬人！”一类足以证明这只哈叭虽顽皮实天真驯善的话来解围，自然这一类解围的话中，还夹着点逗自己奶奶开心的意味。
　　本来那一次小黄给她的惊吓比痛苦还多，请想，两只手正扶着一个大簸簸，而那畜生闪不知扑拢来就在你腱子肉上啃一下，怎不使人气愤？要是八儿家哈叭竟顽皮到同小黄一 样，恐怕八儿的爹，不再要奶奶提议，也早做成打狗的杨大爷一笔生意了。
　　八儿不着意的把头转到门帘子脚边去，两个白花耳朵同一双大眼睛又在门帘下脚掀开处出现了。哈叭象是心里怯怯的，只把一个头伸进房来看里面的风色，又象不好意思似的（尾巴也在摇摆）。
　　“混账……”很懂事样子经过八儿一声吆喝，哈叭那个大头就不见了。
　　然而八儿知道哈叭这时还在门帘外边徘徊。

　　一九二五年十二月二十六日于北京'''
    encoded5, treeRoot5 = huffman_encoding(Chinese_Str)
    codes5 = {}
    huffman_get_codes(treeRoot5, codes5, '')
    print(len(codes5))
    assert huffman_decoding(encoded5, treeRoot5) == Chinese_Str
    print("The size of the Chinese string is: {}\n".format(
        sys.getsizeof(Chinese_Str)))
    print("The size of the encoded Chinese string is: {}\n".format(
        sys.getsizeof(int(encoded5, base=2))))

# Test 6: test with empty string
encoded6, treeRoot6 = huffman_encoding("")

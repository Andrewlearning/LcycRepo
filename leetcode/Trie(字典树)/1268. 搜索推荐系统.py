"""
给你一个产品数组 products 和一个字符串 searchWord ，products
 数组中每个产品都是一个字符串。

请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后
推荐 products 数组中前缀与 searchWord 相同的最多三个产品。
如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。


输入：products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mogse"
输出：
[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
[],
[],
[]]

"""
class Trie:
    def __init__(self):
        self.child = dict()
        self.words = list()


class Solution:
    def suggestedProducts(self, products, searchWord):
        root = Trie()

        # 初始化字典树
        for word in products:
            self.addWord(root, word)


        res = []
        cur = root

        # 假如说当前这个字母已经不在字典树了，那么后续的字母即使在也没意义了
        #
        flag = False


        for char in searchWord:
            # 当前char不存在，那么后续的单词存在也没意义了,因为往下输入肯定也不会找到任何一个单词
            if flag or char not in cur.child:
                res.append([])
                flag = True
            else:
                cur = cur.child[char]
                res.append(cur.words)

        return res


    # 每一个单词，都是从root往下找
    def addWord(self, root, word):
        cur = root
        for char in word:
            if char not in cur.child:
                cur.child[char] = Trie()

            # 进入到一个新的 Trie() 或者是一个之前存在的 Trie()
            cur = cur.child[char]

            # 往这个节点的list 添加word, 因为用到了char，这个字母
            cur.words.append(word)

            # 然后对这个这个list进行排序
            cur.words.sort()

            # 假如list长度大于3，那么我们就要pop（）掉
            if len(cur.words) > 3:
                cur.words.pop()


s = Solution()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
s.suggestedProducts(products, searchWord)
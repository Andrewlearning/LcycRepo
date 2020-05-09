"""
给定两个句子 words1, words2 （每个用字符串数组表示)
和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。

例如，当相似单词对是
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]的时候，
        "great acting skills" 和 "fine drama talent" 是相似的。
        "fine acting skills" 和 "great drama talent" 也是相似的
        反正只要是两个单词能一一对上就好了

相似关系是具有传递性的。
例如，如果 "great" 和 "fine" 是相似的，"fine" 和 "good" 是相似的，所以"great" 和 "good" 是相似的。
他们构成了 ["great","fine", "good"] 的一个联通分量

相似关系是具有对称性的。例如，"great" 和 "fine" 是相似的相当于 "fine" 和 "great" 是相似的。

一个单词总是与其自身相似。
例如，句子 words1 = ["great"], words2 = ["great"], pairs = [] 是相似的
尽管没有输入特定的相似单词对。


句子只会在具有相同单词个数的前提下才会相似。
所以一个句子 words1 = ["great"] 永远不可能和句子 words2 = ["doubleplus","good"] 相似。
"""

class UF:
    def __init__(self):
        # parent里面储存着所有 "正确" 的连通分量
        self.parent = {}

    def find(self, x):
        # find前我们先对x来进行一个初始化，自己指向自己
        self.parent.setdefault(x, x)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        aroot = self.find(a)
        broot = self.find(b)

        if aroot == broot:
            return

        self.parent[aroot] = broot


class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        uf = UF()

        for pair in pairs:
            uf.union(pair[0], pair[1])

        for w1, w2 in zip(words1, words2):
            # 当两个单词相等的时候，我们不用对其检测
            if w1 == w2:
                continue

            # 假如说我们检测到 w1,w2不在同一个联通分量里面，说明w1,w2无法形成pair，是错误的
            if uf.find(w1) != uf.find(w2):
                return False

        return True

"""
关于并查集合+字符串的操作，可以和721一起看

时间复杂度：O(NlogP+P)，其中 N 为 words1 和 words2 长度中的最大值，P 为 pairs 的大小。
空间复杂度：O(P)，其为 pairs 的大小。



其实本题思路很简单，题目给出的pairs，就代表着里面的元素得在同一个联通分量里面
又因为本题具有传递性，所以就等于把那一串的单词都放进同一个联通分量里去

例如 pairs = [[a,b],[a,c],[c,d]] -> [a,b,c,d]都在同一个联通分量

所以只要word1,word2 两个单词在 [a,b,c,d] 这个范围以内，那他们就是合法的
                        若不在 这个联通分量之内，那么他们是不合法的
"""
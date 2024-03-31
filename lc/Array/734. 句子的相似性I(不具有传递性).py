"""
给定两个句子 words1, words2 （每个用字符串数组表示)
和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。

例如，当相似单词对是
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]的时候，
        "great acting skills" 和 "fine drama talent" 是相似的。
        "fine acting skills" 和 "great drama talent" 也是相似的
        反正只要是两个单词能一一对上就好了

相似关系是不具有传递性的。
例如，如果 "great" 和 "fine" 是相似的，"fine" 和 "good" 是相似的，但是 "great" 和 "good" 未必是相似的。

相似关系是具有对称性的。例如，"great" 和 "fine" 是相似的相当于 "fine" 和 "great" 是相似的。

一个单词总是与其自身相似。
例如，句子 words1 = ["great"], words2 = ["great"], pairs = [] 是相似的
尽管没有输入特定的相似单词对。


句子只会在具有相同单词个数的前提下才会相似。
所以一个句子 words1 = ["great"] 永远不可能和句子 words2 = ["doubleplus","good"] 相似。
"""

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # 为了待会匹配的时候，满足它的对称性，即是 [a,b] == [b,a],所以要把元素装进set里
        pairs_set = [set(pair) for pair in pairs]

        # 假如两个单词列表长度都不想等，我们可以直接忽略掉了
        if len(words1) != len(words2):
            return False


        for w1, w2 in zip(words1, words2):
            # 每个单词组合，我们都要验证他们在paris里存不存在
            # 不存在表面无法构成
            if w1 != w2:
                if set([w1, w2]) not in pairs_set:
                    return False
        return True

"""
https://leetcode-cn.com/problems/sentence-similarity/solution/python3-li-yong-ji-he-fu-zhu-pan-duan-by-mnm135/
"""
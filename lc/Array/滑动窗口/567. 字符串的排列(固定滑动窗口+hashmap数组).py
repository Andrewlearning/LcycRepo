"""
给定两个字符串s1和s2，写一个函数来判断 s2 是否包含 s1的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import defaultdict
        n1 = len(s1)
        n2 = len(s2)

        # 存在s1 比 s2短的情况，那么是错的
        if n1 > n2:
            return False

        # 统计 s1, s2[:n1] 中每个字符的出现次数
        w1 = defaultdict(int)
        w2 = defaultdict(int)
        for i in range(n1):
            w1[s1[i]] += 1
            w2[s2[i]] += 1

        # 先判断一波[:n1]出现频率是否相等
        if w1 == w2:
            return True

        l = 0
        for r in range(n1, n2):
            w2[s2[l]] -= 1
            w2[s2[r]] += 1

            # 当value=0, 要清理掉, 要不然对于dict{"a":0, "b":1} 与 {"b":1}不相等
            if w2[s2[l]] == 0:
                del w2[s2[l]]

            if w1 == w2:
                return True

            l += 1

        return False


"""
本题和438题基本一样
https://blog.csdn.net/qq_37007384/article/details/104771329
"""
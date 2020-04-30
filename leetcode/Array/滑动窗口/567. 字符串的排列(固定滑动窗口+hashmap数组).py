"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

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
        n1 = len(s1)
        n2 = len(s2)

        # 存在s1 比 s2短的情况，那么是错的
        if n1 > n2:
            return False

        list1 = [0] * 26
        list2 = [0] * 26

        for i in range(n1):
            list1[ord(s1[i]) - ord("a")] += 1
            list2[ord(s2[i]) - ord("a")] += 1

        if list1 == list2:
            return True

        for i in range(n1, n2):
            list2[ord(s2[i - n1]) - ord("a")] -= 1
            list2[ord(s2[i]) - ord("a")] += 1

            if list1 == list2:
                return True

        return False


"""
本题和438题基本一样
https://blog.csdn.net/qq_37007384/article/details/104771329
"""
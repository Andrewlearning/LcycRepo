"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
"""
class Solution(oblect):
    from collections import defaultdict
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {}
        res = 0
        # 记录滑动窗口的左端点
        l = 0

        for i in range(len(s)):
            c = s[i]
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1
                # 说明s[i]在window中有重复，那么则从前往后删，直到s[i]只出现一次
                while hm[c] > 1:
                    hm[s[l]] -= 1
                    l += 1

            res = max(res, i - l + 1)
        return res


"""
https://www.acwing.com/video/1319/
"""

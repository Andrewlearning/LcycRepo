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
    def lengthOfLongestSubstring(self, string):
        """
        :type s: str
        :rtype: int
        """
        if string is None or len(string) == 0:
            return 0
        window = defaultdict(int)
        res = 0

        # 记录滑动窗口的左端点
        l = 0
        for i in range(len(string)):
            window[string[i]] += 1

            # 说明string[i]在window中有重复，那么则从前往后删，直到string[i]只出现一次
            while window[string[i]] > 1:
                window[string[l]] -= 1
                l += 1

            res = max(res, i - l + 1)

        return res


"""
https://www.acwing.com/video/1319/
"""

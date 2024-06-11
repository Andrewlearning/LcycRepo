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
        from collections import defaultdict
        # 滑动窗口，记录窗口内的元素出现次数
        w = defaultdict(int)
        res = 0
        # 记录滑动窗口的左端点
        l = 0

        for i in range(len(s)):
            # 每次都把新元素加进w
            c = s[r]
            w[c] += 1

            # 当前r字母出现次数>1, 则从左缩小窗口，知道出现次数=1
            while w[c] > 1:
                w[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)

        return res


"""
https://www.acwing.com/video/1319/
"""

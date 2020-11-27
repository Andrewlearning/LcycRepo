"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
"""
import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 记录每个元素出现了多少次
        hashmap = collections.defaultdict(int)

        left = right = 0
        res = 0

        while right < len(s):
            # 每次窗口右边的元素都让他进来
            hashmap[s[right]] += 1

            # 当新加进来的元素出现重复的时候，我们缓慢把左指针向右移动
            # 直到没有重复为止
            while hashmap[s[right]] > 1:
                hashmap[s[left]] -= 1
                left += 1

            # 每次计算窗口的最大值
            res = max(res, right - left + 1)

            right += 1

        return res

"""
https://www.acwing.com/video/1319/
看答案把，很直接
"""
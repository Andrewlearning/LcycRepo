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
class Solution(object):
    class Solution(object):
        def lengthOfLongestSubstring(self, nums):
            """
            :type s: str
            :rtype: int
            """
            if nums is None or len(nums) == 0:
                return 0

            hashmap = [0] * 108

            res = 0

            j = 0
            for i in range(len(nums)):
                hashmap[ord(nums[i]) - ord("a")] += 1

                while hashmap[ord(nums[i]) - ord("a")] > 1:
                    hashmap[ord(nums[j]) - ord("a")] -= 1
                    j += 1

                res = max(res, i - j + 1)

            return res


"""
https://www.acwing.com/video/1319/
看答案把，很直接
"""

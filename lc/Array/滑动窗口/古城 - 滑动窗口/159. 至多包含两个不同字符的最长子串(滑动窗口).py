"""
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。

示例 1:
输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。

示例 2:
输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

"""
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        # 用来记载滑动窗口里有多少个不同的元素
        # key: char, value: appear time in window
        from collections import defaultdict
        window = defaultdict(int)

        l = 0
        res = 0

        for i in range(len(s)):
            # 每个新进来的元素先加进窗口
            window[s[i]] += 1

            # 假如窗口里的元素个数>2，说明满载了，需要减少
            while len(window) > 2:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            res = max(res, i - l + 1)

        return res

if __name__ == '__main__':
    s = Solution()
    print("test1:", s.lengthOfLongestSubstringTwoDistinct("eceba") == 3)
    print("test2:", s.lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5)

"""
时间复杂度：On 空间复杂度 O(1),因为window里不超过三个元素
基本复用3题，参考古城算法 https://www.youtube.com/watch?v=6pLYYfLkaKI 15:53
"""
"""
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。

s = "aa", k = 1
output: 2
解释: 则 T 为 "aa"，所以长度为 2。
"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
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
            while len(window) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            res = max(res, i - l + 1)

        return res

if __name__ == '__main__':
    s = Solution()
    print("test1:", s.lengthOfLongestSubstringKDistinct("eceba", 2) == 3)
    print("test2:", s.lengthOfLongestSubstringKDistinct("aa", 1) == 2)

"""
基本复用3题，参考古城算法 https://www.youtube.com/watch?v=6pLYYfLkaKI 19:53
"""









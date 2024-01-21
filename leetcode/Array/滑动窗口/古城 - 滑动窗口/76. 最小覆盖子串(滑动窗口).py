"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
这个题目说的是，给你两个字符串 s 和 t，你要在 s 中找到一个最短子串，
它包含 t 中所有的字符。如果找不到满足条件的子串，就返回空字符串。
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict
        window = defaultdict(int)
        ht = defaultdict(int)
        for char in t:
            ht[char] += 1

        res = ""
        # 滑动窗口内有效的字母个数，因为窗口内可能有些字母无效
        cnt = 0
        l = 0

        for i in range(len(s)):
            # 往滑动窗口加入当前元素
            window[s[i]] += 1

            # 假如加入当前元素后，当前元素在窗口内出现的次数没有超过要求的次数，并且这个元素是有效原则，则cnt++
            if window[s[i]] <= ht[s[i]]:
                cnt += 1

            # 从l -> i扫描，检查window里的元素是否多余，如有多余则剔除
            while l <= i and window[s[l]] > ht[s[l]]:
                window[s[l]] -= 1
                l += 1

            # 检查当前窗口已经包含了 T 中所有字符，更新答案
            if cnt == len(t):
                if res == "" or i - l + 1 < len(res):
                    res = s[l:i + 1]

        return res

"""
https://www.acwing.com/video/1419/
"""










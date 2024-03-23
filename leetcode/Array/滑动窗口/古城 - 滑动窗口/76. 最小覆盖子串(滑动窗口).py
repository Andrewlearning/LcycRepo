"""
Given a string S and a string T, find the minimum wMap in S which will contain all the characters in T in complexity O(n).

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
        wMap = defaultdict(int)
        reqMap = defaultdict(int)
        for char in t:
            reqMap[char] += 1

        res = ""
        # 滑动窗口内有效的字母个数，因为窗口内可能有些字母无效
        cnt = 0
        l = 0

        for i in range(len(s)):
            # 往滑动窗口加入当前元素
            wMap[s[i]] += 1

            # 假如加入当前元素后，当前元素在窗口内出现的次数没有超过要求的次数，并且这个元素是有效原则，则cnt++
            if wMap[s[i]] <= reqMap[s[i]]:
                cnt += 1

            # 从l -> i扫描，检查window里的元素是否多余，如有多余则剔除
            # 假如s[l]删除后会破坏满足window包含t的情况，则不再删除
            while l <= i and wMap[s[l]] > reqMap[s[l]]:
                wMap[s[l]] -= 1
                l += 1

            # 检查当前窗口已经包含了t中所有字符，更新答案
            if cnt == len(t):
                if res == "" or i - l + 1 < len(res):
                    res = s[l:i + 1]

        return res

"""
https://www.acwing.com/video/1419/
"""










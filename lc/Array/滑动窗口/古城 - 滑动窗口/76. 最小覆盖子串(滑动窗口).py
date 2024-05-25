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

        # 初始化得为空，因为在某些不符合条件的test case需要返回空
        res = ""
        # 滑动窗口内有效的字母个数，因为窗口内可能有些字母无效
        cnt = 0
        l = 0

        for r in range(len(s)):
            # 往滑动窗口加入当前元素
            wMap[s[r]] += 1

            # 假如加入当前元素后，当前元素在窗口内出现的次数没有超过要求的次数，并且这个元素是有效原则，则cnt++
            # 后面去除多余元素的时候不需要清理cnt, 因为我们不会删除到需要的元素，cnt只记录了window里是否包含足够量的必须元素
            # <=的含义是，例如我们reqMap[s[r]]=1，wMap[s[r]]一开始是0，后面在上面加了一次，wMap[s[r]]=1，其实这种情况是需要记录的
            if wMap[s[r]] <= reqMap[s[r]]:
                cnt += 1

            # 从l -> r扫描，检查window里的元素是否多余，如有多余则剔除
            # 假如s[l]删除后会破坏满足window包含t的情况，则不再删除
            while l <= r and wMap[s[l]] > reqMap[s[l]]:
                wMap[s[l]] -= 1
                l += 1

            # 检查当前窗口已经包含了t中所有字符，更新答案
            if cnt == len(t):
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r + 1]

        return res

if __name__ == '__main__':
    s = Solution()
    s.minWindow("ADOBECODEBANC", "ABC")

"""
https://www.acwing.com/video/1419/
"""










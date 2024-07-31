"""
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s and len(s) == 0:
            return 0

        res = 0
        for i in range(len(s)):
            res += self.expend(s, i, i)
            res += self.expend(s, i, i + 1) #当i=len(s)-1时，这个case会返回0

        return res

    def expend(self, s, l, r):
        cur = 0
        # 当发现扩散后，依然满足Palindromic的条件时，说明又找到一个组合，cur += 1
        while -1 < l <= r < len(s) and s[l] == s[r]:
            cur += 1
            l -= 1
            r += 1

        return cur




"""
https://algocasts.io/episodes/dbGY2p5V
// Time: O(n^2), Space: O(1)
答案：
aba
1.当我们遍历到a的时候，他自己算一个回文字串
2.然后我们向外扩展
3.到b的时候，b为一个回文字串，向外扩展,a == a,所以aba算一个回文子串
4.考虑情况 abba，所以我们要res += self.expend(s,i,i+1)
"""
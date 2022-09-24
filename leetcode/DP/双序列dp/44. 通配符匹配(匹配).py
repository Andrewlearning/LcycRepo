class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)

        # dp[i][j] 代表的是 从0~i-1 和 从0～j-1 这两个字符串是否匹配
        # 长度+1的原因是，留空字符进行匹配， 例如 "" 与 "abc", 并且处理dp[x-1]这种情况
        dp = [[False] * (lp+1) for i in range(ls+1)]

        # "" "" 是匹配的
        dp[0][0] = True

        # i从0开始是因为 字符模式匹配可以匹配""
        # j从1开始是因为，不可能拿空的正则匹配的串，匹配另一个串
        for i in range(0,ls+1):
            for j in range(1,lp+1):
                # 情况1, 当p[j-1] != *
                # 如果两个字符串 s[i-1] = p[j-1]， 那么dp[i][j] 就取决于前面的串是否相同
                # 如果第p[j-1] = ?，那么说明s[i-1] = p[j-1]必相同，那么dp[i][j] 就取决于前面的串是否相同
                if i > 0 and (s[i-1] == p[j-1] or p[j-1] == "?"):
                    dp[i][j] = dp[i-1][j-1]

                # 情况2，当p[j-1] == *
                # dp[i][j - 1]表示 * 代表的是空字符，例如ab, ab *
                # dp[i - 1][j]表示 * 代表的是非空字符，例如 abc, ab*
                # 我们要确保ab ab是匹配的，对于i
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]


        return dp[-1][-1]

"""
https://leetcode-cn.com/problems/wildcard-matching/solution/dong-tai-gui-hua-dai-zhu-shi-by-tangweiqun/

可以听听y总的解题方法，有点不太理解的了
"""
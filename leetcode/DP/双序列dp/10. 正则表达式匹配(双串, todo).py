class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)

        # 构造两个长度为 ls+1, lp+1的dp数组
        # 表示 从都不选， 到全都选的所有可能
        dp = [[False] * (lp + 1) for i in range(ls + 1)]
        dp[0][0] = True

        # 一个说明,dp[i] 指的是 p[i-1]这个位置
        # 当出现s = "" 然后p未知的情况
        # 当当前位置为*, 且*前两个位置为True时
        # "" and "a*" 是true, 因为我们可以设定成0个a
        for i in range(1, lp + 1):
            if p[i - 1] == "*" and dp[0][i - 2]:
                dp[0][i] = True

        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                # 当两个当前字母都相等时 或者p当前字符是点号(当前位置可任意匹配)
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]

                # 当两个当前字母不相等时，那么是"*"的话就还存在别的可能性
                elif p[j - 1] == "*":

                    # 这里的*起的是删除的作用
                    # p前一个字母不能和s当前的字母所匹配 "(a)" "a(b)*"
                    # 那么我们就把"b*" 当作一个空字符串
                    # 这样的话 "a" , "a"就可以匹配了
                    if p[j - 2] != s[i - 1] and p[j - 2] != ".":
                        dp[i][j] = dp[i][j - 2]

                    # 假如说可以 "a" "a*", 这两个a可以match
                    # 有三种情况,我们把*看为0,1,或多
                    # 1. 0, 我们把a*看作空,然后匹配的话就看前面的情况了 "a" "" dp[i][j - 2]
                    # 2. 1, 就把它当做当前匹配, "a" "a" dp[i - 1][j]
                    # 3. 多, "a" "aaa.."， 假如说 s前面的都能和p匹配，那么s加一个a也还能跟a匹配 dp[i][j - 1]

                    else:
                        dp[i][j] = (dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j])

        return dp[-1][-1]

"""
https://www.youtube.com/watch?v=KN22ZEpRTFY
"""
"""
给定s1,s2,s3三个字符串
判断s1,s2能否通过字符串顺序拼成s3

"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        # 假如两个字符串长度加起来不等于s3,那么说明根本不可能通过这两个字符串拼接成第三个
        if len(s3) != l1 + l2:
            return False

        # 由于我们后面需要对[i-1] [j-1]等进行处理，所以我们就在我们让元素从1开始
        s1 = " " + s1
        s2 = " " + s2
        s3 = " " + s3

        # dp[l1+1][l2+1], 理由和上面一样
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                # 两个空的字符串，自然可以拼成另一个空的字符串，所以这里为true
                if i == 0 and j == 0:
                    dp[i][j] = True
                # 当i不为空，且s1[i] 和 s3[i + j]的元素相等时
                # 那么dp[i][j]的值，取决于dp[i - 1][j] 是否能拼成s[i + j -1]
                if i > 0 and s1[i] == s3[i + j]:
                    dp[i][j] = dp[i - 1][j]
                # 当j不为空，且s2[j] 和 s3[i + j]的元素相等时
                # 那么dp[i][j]的值，取决于dp[i][j - 1] 是否能拼成s[i + j -1]
                # 或者dp[i][j]是否已经被s[i]匹配过了
                if j > 0 and s2[j] == s3[i + j]:
                    dp[i][j] = dp[i][j - 1] or dp[i][j]
        # 返回结果
        return dp[-1][-1]

"""
https://algocasts.io/episodes/LPmwE7pq
Time: O(n1*n2), Space: O(n1*n2)
"""
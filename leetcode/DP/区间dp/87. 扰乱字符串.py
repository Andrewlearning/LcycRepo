"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
"""
class Solution:
    def isScramble(self, s1, s2):

        if len(s1) != len(s2):
            return False

        length = len(s1)
        # 初始化dp3维数组dp[i][j][k]
        # dp[i][j][len] 表示从字符串 S 中 i 开始长度为len 的字符串是否能变换为从字符串 T 中 j 开始长度为len 的字符串
        # 长度[i][j][k] = [len][len][len+1]
        dp = [[[False] * (length + 1) for _ in range(length)] for _ in range(length)]

        # 初始化单个字符的情况
        for i in range(length):
            for j in range(length):
                dp[i][j][1] = s1[i] == s2[j]

        # 我们对比区间的范围 2～length, 从小到大就是这个递推式的变化过程
        for k in range(2, length + 1):
            # 枚举S中的起点位置
            for i in range(length - k + 1):  # 也就是在s1中枚举i的位置，因为后面会出现i+w的情况，而w最大就是k，
                # 就会有i+k的情况，所以i的取值范围就是0~length-k

                # 枚举T中的起点位置
                for j in range(length - k + 1):
                    # w枚举划分位置，s1[:k]中从
                    for w in range(1, k):
                        # 第一种情况：S1->T1  S2->T2
                        if dp[i][j][w] and dp[i + w][j + w][k - w]:
                            dp[i][j][k] = True
                            break

                        # 我们可以知道，区间的范围分成两段，第一段是0-w, 第二段是k-w[0...w...k]
                        # 第二种情况：S1->T2 , S2->T1
                        if dp[i][j + k - w][w] and dp[i + w][j][k - w]:
                            dp[i][j][k] = True
                            break

        return dp[0][0][-1]


# 链接：https://leetcode-cn.com/problems/scramble-string/solution/miao-dong-de-qu-jian-xing-dpsi-lu-by-sha-yu-la-jia/

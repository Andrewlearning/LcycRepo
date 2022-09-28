"""
给你一个n x n 整数矩阵arr，请你返回 非零偏移下降路径 数字和的最小值。

非零偏移下降路径 定义为：从arr 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。

"""
class Solution(object):
    def minFallingPathSum(self, m):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lr = len(m)
        lc = len(m[0])

        dp = [[float('inf')] * lc for _ in range(lr)]

        for i in range(lr):
            # d1就是上一行的最小值，d2是上一行的第二小的值
            # 我们先求出这两个值，在后面用
            d1 = d2 = float('inf')
            for j in range(lc):
                x = dp[i-1][j]
                if x < d1:
                    d2 = d1
                    d1 = x
                elif x < d2:
                    d2 = x

            for j in range(lc):
                if i == 0:
                    dp[i][j] = m[i][j]
                else:
                    # 假如遍历到上一行的最小值，根据规定我们不能使用在相同位置上一行的数
                    # 所以我们这里加d2
                    if dp[i-1][j] == d1:
                        dp[i][j] = d2 + m[i][j]
                    # 由于d1只会出现一次，所以其余时候我们都是用最优解d1去加
                    else:
                        dp[i][j] = d1 + m[i][j]


        res = float('inf')
        for j in range(lc):
            res = min(res, dp[lr-1][j])
        return res

"""
https://www.acwing.com/activity/content/problem/content/7197/
时间复杂度进行了优化 O(n**2)
"""
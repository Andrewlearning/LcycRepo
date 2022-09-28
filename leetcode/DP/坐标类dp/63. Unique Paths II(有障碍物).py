class Solution(object):
    def uniquePathsWithObstacles(self, o):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        lr = len(o)
        if lr == 0:
            return 0
        lc = len(o[0])

        dp = [[0] * lc for _ in range(lr)]

        for i in range(lr):
            for j in range(lc):
                # 提前过滤掉障碍物，障碍物那个格子方案肯定为0，就不用计算了
                if o[i][j] == 0:
                    # 剩下做法和62题一样
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    else:
                        if i > 0:
                            dp[i][j] += dp[i - 1][j]
                        if j > 0:
                            dp[i][j] += dp[i][j - 1]

        return dp[lr - 1][lc - 1]


"""
https://www.acwing.com/video/1401/
"""
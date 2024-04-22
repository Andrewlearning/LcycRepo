class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        o = obstacleGrid

        n = len(o)
        m = len(o[0])

        dp = [[0] * m for _ in range(n)]

        # 假如起步就是石头，那么则没办法遍历了
        if o[0][0] != 1:
            dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                # 假如当前位置时石头，那么dp[i][j]保持默认=0，说明此路无法到达
                # 当下面遍历到这个地方的时候，也没办法获得任何路径
                if o[i][j] == 1:
                    continue
                # 假如有从上面下来的走法
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                # 假如有从左边往右的走法
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]


"""
https://www.acwing.com/video/1401/
"""
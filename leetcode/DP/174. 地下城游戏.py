import sys
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        y, x = len(dungeon), len(dungeon[0])

        # 我们建立dp数组的时候，要比原始的长宽多一行，因为初始化的时候，我们需要用到 [len+1][len[0]+1]
        dp = [[sys.maxsize] * (x + 1) for _ in range(y + 1)]

        # 在公主所在的右或下，
        dp[y][x - 1] = dp[y - 1][x] = 1

        # 我们要从终点往起点找，找一条值最小的路
        for i in range(y - 1, -1, -1):
            for j in range(x - 1, -1, -1):

                # 右 和 下，哪个路的hp小，说明从这条路走到终点所需要的hp小
                minn = min(dp[i + 1][j], dp[i][j + 1])

                # 当前这个格子所需要的hp = max(走接下来的路所需要的hp（假如小于1，说明当前血量走不到终点）, 1)
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]

# 链接：https://leetcode-cn.com/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/

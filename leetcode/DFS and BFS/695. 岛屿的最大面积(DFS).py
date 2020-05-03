class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        self.m = len(grid)
        self.n = len(grid[0])
        res = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.temp = 0
                    self.dfs(grid, i, j)

                    # 对于200题，增加了一个记录每个岛屿最大面积的变量
                    if self.temp > res:
                        res = self.temp

        return res

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] != 1:
            return

        # 走到每一个合法岛屿，都把岛屿的面积+1
        self.temp += 1
        # 完成记忆话的过程
        grid[i][j] = 0

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

"""
时空间复杂度等待解决
"""
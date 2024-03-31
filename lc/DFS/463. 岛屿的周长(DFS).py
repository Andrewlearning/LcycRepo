class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 因为只有一个岛屿，所以我们只用找到一个开头就行了
                    return self.dfs(grid, i, j)

    def dfs(self, grid, i, j):
        # 向边界走去，+1
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 1

        # 向水域走去,+1
        if grid[i][j] == 0:
            return 1

        # 当前格子之前已经走过了,不计算，+0
        if grid[i][j] != 1:
            return 0

        # 当前格子已经被走过了，定为2
        grid[i][j] = 2

        return self.dfs(grid, i + 1, j) + \
               self.dfs(grid, i - 1, j) + \
               self.dfs(grid, i, j + 1) + \
               self.dfs(grid, i, j - 1)

"""
Time: O(n) Space:??？
https://leetcode-cn.com/problems/island-perimeter/solution/tu-jie-jian-ji-er-qiao-miao-de-dfs-fang-fa-java-by/

本题比较好的一些点：
1. 直接在原始数组上定义记忆化，省下了空间
2. 如何计算周长提供了一个很好的思路
"""
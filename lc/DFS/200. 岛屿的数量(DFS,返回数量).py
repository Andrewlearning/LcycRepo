"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        g = grid
        n = len(g)
        m = len(g[0])

        def dfs(i, j):
            if not 0 <= i < n or not 0 <= j < m or g[i][j] == "0":
                return

            # 让岛屿沉没了
            g[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        res = 0
        for i in range(n):
            for j in range(m):
                if g[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res


"""
"""
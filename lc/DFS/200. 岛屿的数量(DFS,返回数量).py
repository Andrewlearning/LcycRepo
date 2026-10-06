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
时间复杂度：O(M * N)
外层嵌套循环遍历整个网格的所有 M * N 个单元格；DFS 过程中每个单元格最多被访问一次并修改为 "0"。

空间复杂度：O(M * N)
算法直接在原网格上修改，没有使用额外的二维数组；但最坏情况下（整个网格全为陆地 "1"），递归调用栈的最大深度可达 M * N。

(注：M 为网格高度，N 为网格宽度)
"""
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
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if not (0 <= i < n) or not (0 <= j < m) or not grid[i][j] == "1":
                return

            # 把当前 "1" -> "0"，相当于起到记录到visited的意思，后续就遍历不到了
            grid[i][j] = "0"
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni = i + di
                nj = j + dj
                dfs(ni, nj)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    # 每次遍历，我们都期望把鱼当前[i][j]相连的节点都变为0
                    # 并且记录为这是一座岛屿
                    res += 1

        return res


"""
https://www.youtube.com/watch?v=E_jxW5RqXCI&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=55

这题使用的是DFS的做法，就是所谓的鬼子扫荡式的方法：
1.进行全局遍历，当我们遍历到1的时候，我们就开始把该点的坐标放进dfs
2.dfs的终止条件是坐标越界或者是 该坐标不为1
3.成功进入dfs后我们把该点坐标改为"0"，这样就不会在dfs的时候重新扫描到自己
4.对该坐标的上下左右进行dfs扫描。直到结束，结束时说明这一整个岛也找好了
5.结束dfs递归之后，回到主函数，count+1,说明已经扫描好，且已删除了一个岛
"""
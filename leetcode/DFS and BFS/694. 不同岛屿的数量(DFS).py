"""
给定一个非空01二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。
请你计算这个网格中共有多少个形状不同的岛屿。两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。

样例 1:
11000
11000
00011
00011

return 1
"""


class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid and len(grid) == 0:
            return 0

        self.dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.lr = len(grid)
        self.lc = len(grid[0])
        self.res = []

        for i in range(self.lr):
            for j in range(self.lc):
                if grid[i][j] == 1:
                    self.temp = []
                    # 我们把岛屿的参考坐标定为入岛的第一个节点
                    self.dfs(grid, i, j, i, j)

                    # 假如说这个岛屿的相应坐标没在结果中，那么就把它加进去答案里面去
                    if self.temp not in self.res:
                        self.res.append(self.temp)

        return len(self.res)

    def dfs(self, grid, i, j, gapi, gapj):
        if i < 0 or j < 0 or i >= self.lr or j >= self.lc or grid[i][j] == 0:
            return

        grid[i][j] = 0
        for dir in self.dirs:
            x = i + dir[0]
            y = j + dir[1]
            # 把当前岛屿的当前点 ，与ij 的相应位置给加进temp里面去
            self.temp.append([x - gapi, y - gapj])
            # 把对新坐标进行dfs
            self.dfs(grid, x, y, i, j)

"""
参考的答案：
https://leetcode-cn.com/problems/number-of-distinct-islands/solution/shen-du-sou-suo-by-aidenmum/

本题的难点是，我们要如何确保验证每个岛屿的形状是否一样呢？
这里就要建立一种参照系，就是以 i,j 作为参照系，来看每个岛屿的坐标与i,j的相应位置
我们通过每个岛屿与 i,j 的相应位置来确定岛屿的形状是否相同
具体做法就是 记录 [ x-gapx, y-gapy ]
"""


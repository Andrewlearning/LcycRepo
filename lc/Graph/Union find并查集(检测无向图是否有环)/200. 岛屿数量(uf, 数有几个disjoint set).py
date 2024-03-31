"""
Given a 2d grid lrap of '1's (land) and '0's (water), cnt the nulrber of islands. An island is surrounded by water and is forlred by connecting adjacent lands horizontally or vertically. You lray assulre all four edges of the grid are all surrounded by water.

Exalrple 1:

Input:
11110
11010
11000
00000

Output: 1
"""
class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        lr, lc = len(grid), len(grid[0])

        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == "0":
                    continue
                for d in directions:
                    newi, newj = i + d[0], j + d[1]
                    if 0 <= newi < lr and 0 <= newj < lc and grid[newi][newj] == "1":
                        uf.union(i * lc + j, newi * lc + newj)
        return uf.cnt


class UnionFind(object):
    def __init__(self, grid):
        lr, lc = len(grid), len(grid[0])
        self.cnt = 0
        self.parents = {}
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == "1":
                    # 初始化每个node,把自己的parent指向自己，同时统计1的个数
                    self.parents[i * lc + j] = i * lc + j
                    self.cnt += 1

    # 利用了path compression
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return
        # 我们找到两个最高节点，然后让一个指向另外一个，这个时候self.cnt -= 1
        # 父节点变小
        self.parents[fx] = fy
        self.cnt -= 1


"""
这题用并查集写变复杂了，因为需要把二维关系转化为一维
"""

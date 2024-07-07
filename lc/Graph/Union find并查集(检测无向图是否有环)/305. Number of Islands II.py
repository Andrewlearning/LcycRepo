"""
lintcode 434: https://www.lintcode.com/problem/434/description
给定 n, m, 分别代表一个二维矩阵的行数和列数, 并给定一个大小为 k 的二元数组A.
初始二维矩阵全0. 二元数组A内的k个元素代表k次操作, 设第i个元素为 (A[i].x, A[i].y), 表示把二维矩阵中下标为A[i].x行A[i].y列的元素由海洋变为岛屿.
问在每次操作之后, 二维矩阵中岛屿的数量. 你需要返回一个大小为k的数组.

Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1,1,2,2]
Explanation:
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011
"""
class Uf:
    def __init__(self):
        self.p = {}
        self.cnt = 0

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.p[px] = py
            self.cnt -= 1

    def add(self, x):
        # 过滤掉重复的添加
        if x not in self.p:
            self.p[x] = x
            self.cnt += 1

    # 看这个点之前有没有添加过
    def exist(self, x):
        return x in self.p

    def getCount(self):
        return self.cnt


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        uf = Uf()
        res = []

        for p in operators:
            i, j = p.x, p.y

            # 初始化这个新岛屿的信息
            uf.add((i, j))

            # 遍历这个新岛屿附近的岛屿，假如发现附近有其他岛屿，则进行union
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and uf.exist((ni,nj)):
                    uf.union((i, j), (ni, nj))

            res.append(uf.getCount())

        return res


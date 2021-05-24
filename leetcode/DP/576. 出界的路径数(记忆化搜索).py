"""
给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，
或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你最多可以移动 N 次。
找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。
"""
class Solution:
    @lru_cache(None)  # 通过修饰器实现记忆化
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        count = 0
        mod = int(10e8 + 7)
        if N < 0:
            return count

        # 当前所在位置已经出界了, 说明这算一条路，return 1
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1

        # 没出界，则继续进行向四个方向递归
        for di, dj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            count = (count + self.findPaths(m, n, N - 1, di, dj)) % mod

        return count

# 自顶向下，直接设定一个base case，从大问题开始向小问题分解，然后答案从小问题回归
# 自底向上，从已知的小问题开始向前推，推出大问题
# https://www.zhihu.com/question/27363814
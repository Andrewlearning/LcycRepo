"""
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
"""

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        if not matrix or not matrix[0]:
            return []
        # 流向太平洋的位置
        res1 = set()
        # 流向大西洋的位置
        res2 = set()
        row = len(matrix)
        col = len(matrix[0])

        # 从边界遍历
        def dfs(i, j, res):
            res.add((i, j))
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[i][j] <= matrix[tmp_i][tmp_j] and (tmp_i, tmp_j) not in res:
                    dfs(tmp_i, tmp_j, res)
        # 太平洋
        for i in range(row):
            dfs(i, 0, res1)
        # 太平洋
        for j in range(col):
            dfs(0, j, res1)
        # 大西洋
        for i in range(row):
            dfs(i, col - 1, res2)
        # 大西洋
        for j in range(col):
            dfs(row - 1, j, res2)

        return res1 & res2


# 链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow/solution/dfs-by-powcai-5/



# 链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow/solution/dfs-by-powcai-5/

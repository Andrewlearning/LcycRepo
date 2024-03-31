class NumMatrix(object):

    # 这个函数是让我们先求出所有矩阵的前缀和
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        lrow = len(matrix)
        lcol = len(matrix[0])
        self.prefixSum = [[0] * (lcol + 1) for _ in range(lrow + 1)]

        # 求二维前缀和
        # [i+1][j+1] = 宽相等的上面的长方形 + 长相等的左边的长方形 + [i+1][j+1]这一个格子 - 重复部分
        for i in range(lrow):
            for j in range(lcol):
                self.prefixSum[i+1][j+1] = self.prefixSum[i][j+1] + self.prefixSum[i+1][j] + \
                                matrix[i][j] - self.prefixSum[i][j]

    # 这个函数是在我们求完前缀和以后，然后利用前缀和来进行求值
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # 答案 = 大长方形 - 小长方形1 - 小长方形2 + 重复减的部分
        return self.prefixSum[row2 + 1][col2 + 1] - self.prefixSum[row2 + 1][col1] \
               - self.prefixSum[row1][col2 + 1] + self.prefixSum[row1][col1]

"""
二维前缀和
https://algocasts.io/episodes/VBpLE6WD
https://leetcode-cn.com/problems/range-sum-query-2d-immutable/solution/huan-cun-dong-tai-gui-hua-python3-by-zhu_shi_fu-2/
看图来的直接点吧，这个凭空看很难看明白
"""
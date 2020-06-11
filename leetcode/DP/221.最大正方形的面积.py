"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0 or not matrix[0] or len(matrix) == 0:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        # dp的创建，要比原矩阵 长宽要大1，方便 i-1,j-1这种判断
        dp = [[0] * (col + 1) for i in range(row + 1)]
        res = 0

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                # 我们注意，每次开始计算，都是从正方形的右下角开始计算的
                if matrix[i - 1][j - 1] == "1":

                    # 因为这个dp的赋值是从左上到右下赋值的，所以我们可以通过这样的递推式去进行赋值
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    if dp[i][j] > res:
                        res = dp[i][j]

        return res * res

"""
https://www.youtube.com/watch?v=_Lf1looyJMU
再结合solution 一起看
答案：
这题的判断方式是这样的
  0 1      1 1
  1 ?      1 ?
  dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

  假如说，在当前坐标的 左，左上，上， 有其中一个为0，那么这四个数一定不能构成正方形，所以dp[i][j] = 1(自己本身 长宽为1)
  假如说，在当前坐标的 左，左上，上， 每一个都为1，那么这四个数可以能构成正方形，所以dp[i][j] = 1 + 1 = 2(长宽为2)       
"""
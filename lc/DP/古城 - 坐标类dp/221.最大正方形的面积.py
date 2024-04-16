"""
Given a 2D binary m filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution(object):
    def maximalSquare(self, m):
        """
        :type m: List[List[str]]
        :rtype: int
        """
        if not m or len(m) == 0 or not m[0] or len(m) == 0:
            return 0

        lr = len(m)
        lc = len(m[0])
        # dp的创建，要比原矩阵 长宽要大1，方便 i-1,j-1这种判断
        # dp[i][j]表示以m[i-1][j-1]作为正方形的右下角，所能形成最大正方形的边长长度
        dp = [[0] * (lc + 1) for i in range(lr + 1)]

        # 记录正方形的最大边长
        res = 0

        for i in range(1, lr + 1):
            for j in range(1, lc + 1):
                # 我们注意，每次开始计算，都是从正方形的右下角开始计算的
                if m[i - 1][j - 1] == "1":

                    # 因为这个dp的i,j遍历是从左上到右下赋值的，所以我们可以通过这样的递推式去进行赋值
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
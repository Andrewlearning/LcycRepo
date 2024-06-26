
"""
A robot is located at the top-left corner of a lr x lc grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
m是col，n是row, 机器人每改变一个方向算有加上一种走法
"""
class Solution(object):
    def uniquePaths(self, lr, lc):
        """
        :type lr: int
        :type lc: int
        :rtype: int
        """
        if lc < 1 or lr < 1:
            return 0

        # 初始化dp数组
        dp = [[0] * lc for i in range(lr)]

        # 初始化dp的起点，假如从起点只往右走，或只往下走，都是只有一条路线才可以到达
        dp[0][0] = 1

        for i in range(lr):
            for j in range(lc):
                # 初始化[0][0]这个格子，走到这个格子只有一种走法
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    # 假如i>0, 意味着可以从上面往下走
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    # 假如j>0, 意味着可以从左边往右走
                    if j > 0:
                        dp[i][j] += dp[i][j-1]

        return dp[-1][-1]


"""
 // Time: O(lr*lc), Space: O(lr*lc)
 https://www.acwing.com/video/1400/
答案：
1.我们先创建一个m*lc 的矩阵，然后把1附值到横竖进去，(但我这里写的是创造了一个全为1的矩阵，因为后面可以覆盖，所以问题不打)
    
    1 1 1 1
    1 0 0 0
    1 0 0 0

因为，机器人只能向下或者向右走，所以机器人光向下走和光向右走都只要一种走法
2. dp[i][j] = dp[i-1][j] + dp[i][j-1] 因为，机器人只能向下或者向右走，所以到达当前这个点
   可能是从上往下走了一步，或者是从左向右走了一步，这一步由前面的两个状态结合而成
"""
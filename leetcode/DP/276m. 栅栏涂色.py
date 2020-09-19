"""
有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。

你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱 最多连续两个 颜色相同。然后，返回所有有效涂色的方案数。

注意:
n 和 k 均为非负的整数。

示例:

输入: n = 3，k = 2
输出: 6
解析: 用 c1 表示颜色 1，c2 表示颜色 2，所有可能的涂色方案有:

            柱 1    柱 2   柱 3
 -----      -----  -----  -----
   1         c1     c1     c2
   2         c1     c2     c1
   3         c1     c2     c2
   4         c2     c1     c1 
   5         c2     c1     c2
   6         c2     c2     c1
"""


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        # 只有一个栅栏的时候，我们有k种涂色方案
        if n == 1:
            return k
        # 当有两个栅栏的时候，连续两个栅栏允许同色，所以两个栅栏都有k种选择
        if n == 2:
            return k * k

        dp = [0] * n

        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            # 如果：i与i-1的颜色相同，则表明i与i-2的颜色不同，则i的数目为dp[i-2]*(k-1)
            # 如果：i与i-1的颜色不同，则i的数目为dp[i-1]*(k-1)
            dp[i] = dp[i - 2] * (k - 1) + dp[i - 1] * (k - 1)

        return dp[-1]

# https://leetcode-cn.com/problems/paint-fence/solution/dong-tai-gui-hua-java-by-youngbear/
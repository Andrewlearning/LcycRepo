"""
整数可以被看作是其因子的乘积。

例如：
8 = 2 x 2 x 2;
  = 2 x 4.
请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。

注意：
你可以假定 n 为永远为正数。
因子必须大于 1 并且小于 n。

输入: 12
输出:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
"""


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.helper(n, 2)

    def helper(self, n, start):
        res = []

        i = start

        while i * i <= n:
            if n % i == 0:
                res.append([n / i, i])
                for part in self.helper(n / i, i):
                    part.append(i)
                    res.append(part)

            i += 1

        return res

"""
https://leetcode-cn.com/problems/factor-combinations/solution/c-di-gui-jie-fa-by-da-li-wang-2/
"""
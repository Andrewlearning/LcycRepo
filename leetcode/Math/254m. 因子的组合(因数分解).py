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

    # 需要写成递归的原因是，我们可能还要对因子进行进一步的分解
    def helper(self, n, start):
        res = []


        # 为什么是 sqrt(num) + 1, 是因为我们要考虑到6*6=36这种情况
        # 所以要给sqrt(36) + 1, 留空间
        # 然后假如说i再大的话，就会出现重复的情况，例如 3 * 4 和 4 * 3
        for i in range(start, int(sqrt(n)) + 1):
            if n % i == 0:
                res.append([n/i, i])

                # n/i是较大数，所以我们尝试看能不能对n/i进行进一步的分解
                # helper()的return 也是[[]], 所以在这里我们把n/i的分解拿到后，还要再append上i，才能加到res
                for part in self.helper(n/i, i):
                    part.append(i)
                    res.append(part)


        return res

"""
https://leetcode-cn.com/problems/factor-combinations/solution/c-di-gui-jie-fa-by-da-li-wang-2/
"""
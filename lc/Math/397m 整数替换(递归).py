"""
给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

示例 1:

输入:
8

输出:
3

解释:
8 -> 4 -> 2 -> 1
"""
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case 已经到1了，不需要再变动
        if n == 1:
            return 0
        elif n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        elif n % 2 == 1:
            return min(self.integerReplacement(n-1), self.integerReplacement(n+1)) + 1

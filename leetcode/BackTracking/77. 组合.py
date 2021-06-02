"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入:n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []

        self.res = []
        self.helper(n, [], 1, k)
        return self.res

    def helper(self, n, k, index, temp):
        if len(temp) > k:
            return

        if len(temp) == k:
            self.res.append(temp[:])

        for i in range(index, n + 1):
            self.helper(n, k, i + 1, temp + [i])


"""
https://www.youtube.com/watch?v=mlmpQB_yJfc
"""

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
        self.n = n
        self.k = k
        self.res = []
        self.helper(1, [])
        return self.res

    def helper(self, startFrom, temp):
        if len(temp) > self.k:
            return

        if len(temp) == self.k:
            self.res.append(temp[:])
            return

        for i in range(startFrom, self.n + 1):
            temp.append(i)
            self.helper(i + 1, temp)
            temp.pop()


"""
https://www.youtube.com/watch?v=mlmpQB_yJfc
时间复杂度: 一共有Ckn 另外记录每个方案时还需要O(k)的时间，所以时间复杂度是0(Ckn*k)
空间复杂度：递归深度n, temp最大长度是k, 所以O(n+k)=O(n)
"""

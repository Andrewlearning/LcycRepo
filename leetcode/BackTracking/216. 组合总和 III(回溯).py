"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(n, k, 1, [])
        return self.res

    def helper(self, n, k, cur, temp):
        # 错误结果，不要
        if k < 0:
            return

        # 正确结果，记录
        if k == 0 and sum(temp) == n:
                self.res.append(temp[:])

        # 每次遍历，我们都不再使用之前的元素，所以是i+1
        for i in range(cur, 10):
                self.helper(n, k-1, i+1, temp + [i])
"""

"""

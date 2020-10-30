"""
给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n - 1 个元素增加 1。

示例:

输入:
[1,2,3]
输出:
3

解释:
只需要3次移动（注意每次移动会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 对n-1一个数+1, 等价于对一个数-1，因为我们关心的是相对距离
        # 所以我们找到所有数字到最小元素，需要-多少次，就是我们的最终答案

        cur_min = float("inf")
        for num in nums:
            cur_min = min(cur_min, num)

        res = 0
        for num in nums:
            res += num - cur_min
        return res

# https://www.acwing.com/video/1854/
"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:
输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是[-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

"""


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.path = []
        self.helper(nums, 0)
        return self.res

    def helper(self, nums, index):
        # 遍历完最后一位数，进入下一个循环时，index = len(nums)
        # 尽管不会进入for循环，但我们要记录上一次循环得到的path
        if index > len(nums):
            return

        if len(self.path) >= 2:
            self.res.append(self.path[::])

        # 记录当前从前往后遍历重复的数字，当出现重复的数字时，就不遍历了
        # 因为顺序都是从小到大，所以不会出现 474这种情况
        # 会出现 4677 这种，假如不去重，那么答案会出现两次467
        numSet = set()
        for i in range(index, len(nums)):
            if len(self.path) == 0 or self.path[-1] <= nums[i]:
                if nums[i] in numSet:
                    continue
                numSet.add(nums[i])
                self.path.append(nums[i])
                self.helper(nums, i + 1)
                self.path.pop(-1)

"""
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            while nums[i] != nums[nums[i]]:
                self.swap(nums, i, nums[i])


        for i in range(len(nums)):
            if nums[i] != i:
                return nums[i]


    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
使用了鸽子洞理论， 在 index位置上，应该放数值为index的数字
"""
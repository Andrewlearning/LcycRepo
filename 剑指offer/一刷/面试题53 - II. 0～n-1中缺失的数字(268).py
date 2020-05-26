"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        n = len(nums)

        for i in range(n):

            # 关键的一步在这里，我们要在区间的范围内
            # 不断交换第 i ，nums[i] 上的值给交换，直到是交换完毕或者是越界
            while 0 <= nums[i] < n and nums[i] != nums[nums[i]]:
                self.swap(nums, i, nums[i])

        # 找到第一个不在位置上的数字，返回
        for i in range(n):
            if nums[i] != i:
                return i

        return n

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
目标是把 第 i 位 放 i
举例子， 0位放0， 1位放1

"""
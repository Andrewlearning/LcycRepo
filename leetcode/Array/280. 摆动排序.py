"""
给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。

示例:
输入: nums = [3,5,2,1,6,4]
输出: 一个可能的解答是 [3,5,1,6,2,4]
"""
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 本题特征，奇数位的数字要比偶数位的数字大

        for i in range(len(nums) - 1):
            # 目前在偶数位，那么偶数位应该是要比奇数位小的
            if i % 2 == 0:
                # 但是却出现偶数位比奇数位大的情况，交换
                if nums[i] > nums[i + 1]:
                    self.swap(nums, i, i + 1)

            # 目前在奇数位，那么奇数位应该是要比偶数位大的
            elif i % 2 == 1:
                # 但是却出现奇数位比偶数位小的情况，交换
                if nums[i] < nums[i + 1]:
                    self.swap(nums, i, i + 1)

    def swap(self, nums, l, r):
        nums[l], nums[r] = nums[r], nums[l]

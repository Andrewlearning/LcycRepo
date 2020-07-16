"""
Given a sorted array nums, remove the duplicates in-place such that each element appear
only once and return the new length.

Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) == 0:
            return 0

        # 排序数组, 所以我们顺序遍历就好了
        # l 记录没有重复的下标
        l = 0

        # r 是用来遍历的，同时作为去重的手段
        r = 0

        while r < len(nums):

            # 我们在上一次循环里，已经让r落在一个没有重复数字的位置上，然后在这里进行填充
            nums[l] = nums[r]

            # 把r移动到重复数字的最后一位 例如 "11113" r的位置就移动到3前面一位
            while r+1 < len(nums) and nums[r] == nums[r+1]:
                r += 1

            # 指向下一个填充的位置
            l += 1
            r += 1

        return l


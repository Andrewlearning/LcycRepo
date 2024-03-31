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
        k  = 0
        for num in nums:
            # k < 1, 第一个位置的数字不用考虑重复问题
            # nums[k-1] != num，例如2，3这种情况，3是可以加入的
            if k < 1 or nums[k-1] != num:
                nums[k] = num
                k += 1
        return k


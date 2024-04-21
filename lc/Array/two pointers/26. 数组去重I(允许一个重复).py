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
        # 把不重复的元素，都通过这个指针来放置
        k = 0
        for num in nums:
            # k < 1, 第一个位置的数字不用考虑重复问题
            # nums[k-1] != num，例如2，3, 3这种情况，第一个3是可以加入的不重复数组的
            if k < 1 or nums[k-1] != num:
                nums[k] = num
                k += 1
        return k


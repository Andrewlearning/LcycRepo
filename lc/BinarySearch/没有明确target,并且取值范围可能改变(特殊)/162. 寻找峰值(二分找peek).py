"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.
"""

class Solution(object):
    # 使用左边界做法的答案
    def leftEdge(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # 满足nums[mid] > nums[mid+1]的左边界
            # 这个nums[mid] 就是 nums[mid, -1]的最大值
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l

    # 使用右边界做法的答案
    def rightEdge(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r + 1) // 2

            # 满足nums[mid - 1] > nums[mid] 的右边界
            # 这个nums[mid] 就是 nums[0, mid]的最大值
            if nums[mid - 1] < nums[mid]:
                l = mid
            else:
                r = mid - 1
        return l



"""
https://www.acwing.com/video/1532/
这题用左右边界都可以求解出答案
"""
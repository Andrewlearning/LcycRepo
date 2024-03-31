class Solution(object):
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
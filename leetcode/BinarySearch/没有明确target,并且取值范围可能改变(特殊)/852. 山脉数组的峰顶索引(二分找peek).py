class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # 说明峰值在左边，所以往左边走
            if nums[mid] > nums[mid + 1]:
                r = mid
            # 说明峰值在右边，往右边走
            else:
                l = mid + 1

        return l

# 和162用一样的代码
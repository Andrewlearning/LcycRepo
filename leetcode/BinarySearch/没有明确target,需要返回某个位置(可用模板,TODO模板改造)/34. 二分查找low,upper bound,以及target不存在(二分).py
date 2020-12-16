class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums and len(nums) == 0:
            return [-1, -1]

        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)

        return [left, right]

    def findLeft(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # 当 >= 有效区域时，把指针向左推
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1

        # 排除越界情况
        if l >= len(nums):
            return -1
        # 要找有效边界的最左边
        return l if nums[l] == target else -1

    def findRight(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            # 当 <= 有效区域时,把结果向右推
            else:
                l = mid + 1

        # 排除越界情况
        if r >= len(nums):
            return -1
        # 要找有效结果的右边界
        return r if nums[r] == target else -1

"""
二分全套模板
https://github.com/yuzhoujr/leetcode/issues/8
"""
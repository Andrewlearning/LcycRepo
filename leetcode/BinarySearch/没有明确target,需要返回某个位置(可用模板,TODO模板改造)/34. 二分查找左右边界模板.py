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

        while l < r:
            mid = (l + r) // 2

            # [l, traget, mid] [mid+1, r]
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        # 这里最后收敛到l,r都是指向同样的位置
        return l if nums[l] == target else -1

    def findRight(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r + 1) // 2

            # [l, mid-1] [mid, target, r]
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        # 这里最后收敛到l,r都是指向同样的位置
        return r if nums[r] == target else -1

"""
https://www.acwing.com/video/1357/
"""
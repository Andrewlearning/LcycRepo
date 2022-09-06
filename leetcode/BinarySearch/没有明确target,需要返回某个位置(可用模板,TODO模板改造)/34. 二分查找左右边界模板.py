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
            # [l, mid, mid+1) [target, r]
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

记忆秘诀:
1. l, r是固定的
2. while l < r也是固定的
3. 带>=, <=号的，都不会+1或-1
4. 找左边界，r不-1
5. 找右边界，l不+1
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = len(nums) - 1
        # 定义初始左边界，[0-l]都是递增的
        while l + 1 < len(nums) and nums[l + 1] >= nums[l]:
            l += 1

        # 说明当前数组是纯递增的
        if l == r:
            return 0

        # 定义初始右边界，[r, len(nums)-1]都是递增的
        while r - 1 >= 0 and nums[r - 1] <= nums[r]:
            r -= 1

        # 重新定义左右有序边界
        # 找到真正的左边界，因为左边界右边的所有数，都应该比左边界右边的所有数要小
        for i in range(l + 1, len(nums)):
            while l >= 0 and nums[l] > nums[i]:
                l -= 1

        # 找到真正的右边界，因为右边界左边的所有数，都应该比右边界右边的所有数要大
        for i in range(r - 1, -1, -1):
            while r < len(nums) and nums[r] < nums[i]:
                r += 1

        # 最后得到的[0-l-r-len(nums)]
        # (l,r)这个区间内才是真正需要排序的，[0-l],[r-len(nums)]都是已经从小到大排好的
        return r - l - 1

# 我们要用双指针不断找，找到中间的无序区间
# https://www.acwing.com/video/2040/

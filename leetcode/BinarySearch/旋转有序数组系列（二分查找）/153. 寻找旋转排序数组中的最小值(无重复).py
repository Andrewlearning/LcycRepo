"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 处理 [1] 这种情况
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        l = 0
        r = n - 1

        target = nums[0]

        # 找出上升区间的最大值(右边界模板)，下一个数就是下降区间的最小值
        # [3,4,5(找到这个的下标),1,2]
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] >= target:
                l = mid
            else:
                r = mid - 1

        # 处理 [1,2,3,4] 这种情况，没有下降区间了，所以我们取第一个数
        if l == n - 1 and nums[l] > nums[0]:
            return nums[0]
        # 正常情况下，下降区间的最小值应该是上升区间最大值后一个数
        return nums[l + 1]


"""
33,81,153,154是同一类题型
https://www.acwing.com/solution/content/247/
思路借鉴这个
"""
"""
Suppose an array sorted in ascending order(递增)is rotated at
some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example:
Input: [2,2,2,0,1]
Output: 0

用153的代码会卡死在 [3,3,1,3] 上
Output: 3 | Expected:1
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 由于这题允许数字重复，所以nums的开头部分和结尾部分有可能相等
        # [1,2,1,1]
        # 这会使得二分的性质失效，所以我们把nums末尾与开头相同的数都pop掉
        # 其余部分和153题一样
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()

        # 处理 [1] 这种情况
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] >= nums[0]:
                l = mid
            else:
                r = mid - 1

        # 处理 [1,2,3,4] 这种情况，没有下降区间了，所以我们取第一个数
        if l == n - 1 and nums[l] > nums[0]:
            return nums[0]
        # 正常情况下，下降区间的最小值应该是上升区间最大值后一个数
        return nums[l + 1]

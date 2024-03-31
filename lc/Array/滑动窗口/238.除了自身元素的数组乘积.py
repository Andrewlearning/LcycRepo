"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)

        # 构造res前缀乘积数组
        # left[i] 代表 nums[0 ~ i-1] 的乘积
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        # right[i] 表示nums[i+1 ~ -1], 右侧所有数的乘积
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        res = []
        for i in range(len(nums)):
            # 最后left[i] * right[i] 表示除自己这个数以外的所有数的乘积
            res.append(left[i] * right[i])
        return res

"""
https://algocasts.io/episodes/aVWyPJp2
// Time: O(n), Space: O(1)
"""
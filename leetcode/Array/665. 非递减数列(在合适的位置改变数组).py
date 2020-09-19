"""
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 要把数组变成递增数组,左小右大
        if not nums and len(nums) == 0:
            return False

        if len(nums) == 1:
            return True

        # 违反左小右大，要改0,1中的一个
        modified = nums[0] > nums[1]

        for i in range(1, len(nums) - 1):
            # 违反左小右大
            if nums[i] > nums[i + 1]:
                # 看更改次数有没有超过1次
                if modified:
                    return False
                # 假如nums[i-1] < nums[i] (>) nums[i+1]
                if nums[i + 1] >= nums[i - 1]:
                    nums[i] = nums[i - 1]
                # 假如nums[i+1]特别小，比nums[i-1]还小
                else:
                    nums[i + 1] = nums[i]
                modified = True

        return True



"""
Time: O(n), Space: O(1)
https://algocasts.io/episodes/YopkkKp3
"""
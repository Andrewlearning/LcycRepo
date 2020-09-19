"""
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

示例：

输入: nums = [-2,0,1,3], target = 2
输出: 2
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
"""
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # 如果left和right之和小于target-nums[i]，left右移
                # 因为加入left不右移的话，那么right--直到left的这条路上，三数之和都是小于target的
                if nums[left] + nums[right] < target - nums[i]:
                    res += right - left
                    left += 1
                # 如果left和right之和大于target-nums[i]，right左移
                else:
                    right -= 1
        return res

"""
不用去重的原因是，假如说nums[left] + nums[right] < target - nums[i]
那么我们是需要把所有重复结果都记录进去的

链接：https://leetcode-cn.com/problems/3sum-smaller/solution/259jiao-xiao-de-san-shu-zhi-he-python3-by-ml-zimin/

"""

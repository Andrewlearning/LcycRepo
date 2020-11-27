"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        n = len(nums)

        for i in range(n):
            # nums[i] 表示下标
            # nums[nums[i]] 表示下标对应的值
            # 因为序列中有可能出现n , nums[n]会报错，所以我们要过滤掉这个条件
            while 0 <= nums[i] < n and nums[i] != nums[nums[i]]:
                self.swap(nums, i, nums[i])

        for i in range(n):
            # 这里的i 表示下标
            # nums[i] 表示下标对应的值
            if i != nums[i]:
                return i

        return n

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
目标是把 第 i 位 放 i
举例子， 0位放0， 1位放1

"""
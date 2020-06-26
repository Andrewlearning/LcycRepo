"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列。
中点是连续
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res = 1
        temp = 1

        for i in range(1,len(nums)):
            # 假如发现不是递增，那么重头计算
            if nums[i-1] >= nums[i]:
                temp = 1

            # 假如发现是递增，那么则一直加下去，同时更新状态
            else:
                temp += 1
                if temp > res:
                    res = temp
        return res

"""
就是对比前后两个数字，如果递增，temp += 1
如果不递增，那么temp = 1
"""
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 确定单调性
        nums.sort()
        res = 0

        i = 0
        j = 0

        while i < len(nums):
            # 去重
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            # 更新左指针
            while nums[i] - nums[j] > k:
                j += 1
            # 符合 ++
            if j < i and nums[i] - nums[j] == k:
                res += 1
            # 移动右指针
            i += 1

        return res

# https://www.acwing.com/video/1993/
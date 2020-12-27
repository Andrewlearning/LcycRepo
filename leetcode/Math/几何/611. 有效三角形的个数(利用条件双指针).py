class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        # k最短边，j次短边，i最长边
        # 所以要做到k + j > i才行
        for i in range(2, len(nums)):
            j = i - 1
            k = 0
            while j > 0 and j > k:
                while k < j and nums[k] + nums[j] <= nums[i]:
                    k += 1
                # 从[k,j-1]都是最短边的选法，所以k ~ j-1有 j-1-k+1个数
                res += j - 1 - k + 1
                j -= 1

        return res

"""
time On^2
https://www.acwing.com/video/2099/
"""
"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefixSum = {}
        # 应对 nums=[3] k=3 这种情况
        prefixSum[0] = 1
        s = 0
        res = 0

        for i in range(len(nums)):
            s += nums[i]
            # s - k = v
            # s - v = k
            # [0 ~ i] - [0 ~ j] = k
            # [j ~ i] = k, 所以存在一个从[j ~ i]的连续数组和为k
            if (s - k) in prefixSum:
                res += prefixSum[s - k]

            prefixSum[s] = prefixSum.get(s, 0) + 1
        return res

"""
思路：https://www.youtube.com/watch?v=0rCaikfA7No
代码：https://blog.csdn.net/fuxuemingzhu/article/details/82767119
答案：
1. prefixSum 就是遍历到i 的时候， s(nums[:i+1])
我们把每个prefixSum 都作为key, 把这个sum出现的次数作为value

2. 为什么prefixSum[Sum] += 1?
因为序列中有可能出现负数，例如 [2,3] 和 [2,3,-1,1], 他们的prefixSum都是相同的，但是最后
的序列是不一样的。
"""
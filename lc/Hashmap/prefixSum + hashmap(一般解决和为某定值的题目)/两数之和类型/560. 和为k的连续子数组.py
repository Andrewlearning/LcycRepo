"""
Given an array of integers nums and an integer k,
return the total number of continuous subarrays whose sum equals to k.


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

        hashmap = {}
        # key = preFixSum的值
        # value = 这个值所出现过的次数
        # hashmap[0] = 1 这相当于一个base case, 当prefixSum = curSum = k的这种情况发生时，能统计到这种结果
        # 例如 nums[1,1] k=2
        hashmap[0] = 1
        curSum = 0
        res = 0

        for i in range(len(nums)):
            curSum += nums[i]
            # curSum - k = v
            # curSum - v = k
            # curSum([0 ~ i]) - k = Sum([0 ~ j])
            # curSum([0 ~ i]) - Sum([0 ~ j]) = k
            # Sum([j ~ i]) = k, 所以存在一个从[j ~ i]的连续数组和为k
            if (curSum - k) in hashmap:
                res += hashmap[curSum - k]

            # 记录当前前缀和出现的次数
            # 假如curSum存在于hashmap中，则能取出结果，不存在则取出0
            hashmap[curSum] = hashmap.get(curSum, 0) + 1

        return res

"""
思路：https://www.youtube.com/watch?v=0rCaikfA7No
代码：https://blog.csdn.net/fuxuemingzhu/article/details/82767119
"""
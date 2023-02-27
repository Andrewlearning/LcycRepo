"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False

        # key: curSum%k value:index
        map = {}

        # 初始化，curSum=0, index = -1
        map[0] = -1

        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]

            # 语法不允许mod0, 所以当k=0的时候key = curSum
            # 否则 key = curSum%k
            # 因为 a = b(modk), 那么 a - b = m*k
            if k != 0:
                curSum %= k

            # 看mod在不在map.keys()里面
            if curSum in map:
                # 子数组要求长度至少为2
                if i - map.get(curSum) > 1:
                    return True
            # mod不在map.keys()里面的话，那么就要把当前mod，index给加进去
            else:
                map[curSum] = i

        return False

"""
古城算法 23:00
https://www.bilibili.com/video/BV1xB4y1N7Ut/?spm_id_from=333.999.0.0&vd_source=b81616a45fd239becaebfee25e0dbd35
Time: O(n), Space: O(k)
这里主要有一个数学规律，然后其余的都是利用前缀和的做法
规律是  a (modk) = b (modk), 然后 a - b = m*k
所以这个题我们就是要找到两个mod后相等的数，然后把他们的下标找出来，取这个范围就可
"""

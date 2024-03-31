"""
Given an integer array nums and an integer k,
return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous(连续) part of an array.

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5],
[5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # key = curSum % k 的值
        # value = 这个值所出现过的次数
        hashmap = {}
        hashmap[0] = 1
        prefix = 0
        res = 0

        for num in nums:
            # 本来(prefix + num) % k 就行了，我们后面加了这么多
            # num % k 是防止num是一个很大的负数
            # + k 是最后确保 num % k + k 始终是大于0的，而且不会影响mod的值
            prefix = (prefix + num % k + k) % k

            # 两个mod相同的prefix相减，中间这一段子两次出现余数i,j之间的subarray一定是能够被k整除的串
            res += hashmap.get(prefix, 0)

            # 更新这个mod的出现次数
            hashmap[prefix] = hashmap.get(prefix, 0) + 1

        return res


"""
古城算法 21:38
https://www.bilibili.com/video/BV1xB4y1N7Ut/?spm_id_from=333.999.0.0&vd_source=b81616a45fd239becaebfee25e0dbd35

核心思路就是当相同余数再次出现的时候，两次出现余数i,j之间的subarray一定是能够被k整除的

[4, 5, 0, -2, -3, 1]

[5] 余数0
[5, 0] 余数0
[-2,-3] 余数0

[1, 2, 3, 4]  k = 5
1, 余数1
1 + 2 = 3, 余数3
1 + 2 + 3= 6, 余数1 (出现了) 
[2,3]可以被整除

"""

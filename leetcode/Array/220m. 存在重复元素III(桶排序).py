"""
在整数数组 nums 中，是否存在两个下标 i 和 j，
使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t
且满足 i 和 j 的差的绝对值也小于等于 k 。

如果存在则返回 true，不存在返回 false。

 
示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # 维护一个下标差小与等于k的桶
        bucket = {}
        if t < 0:
            return False

        for i in range(len(nums)):
            # 因为两个数的绝对值小与等于t的话，那么是true,所以我们就把一个桶的大小定为t+1
            # 所以一个桶里的最大值-最小值 大小刚好等于t
            nth = nums[i] // (t + 1)

            # 假如说当前桶里有元素，说明满足|max-min| <= t
            if nth in bucket:
                return True

            # 假如有判断相邻桶的话判断是否满足 |max-min| <= t
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True

            # 都不满足，往当前桶添加元素
            bucket[nth] = nums[i]

            # 检查桶里元素最左和最右的下标差是否大于等于k了
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False

# 链接：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/220-cun-zai-zhong-fu-yuan-su-iii-cong-on2-dao-on-p/
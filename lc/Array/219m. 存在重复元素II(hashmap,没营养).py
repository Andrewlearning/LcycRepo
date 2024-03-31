"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 记录遍历过的元素，且他们的最右下标
        hashmap = {}

        for i in range(len(nums)):

            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                # 假如说当前 - 最右下标 <= k， 说明我们找到了这样一对元素
                if i - hashmap[nums[i]] <= k:
                    return True
                # 每次碰到出现过的元素，我们都要更新一次下标
                hashmap[nums[i]] = i

        return False
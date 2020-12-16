"""
给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

示例 1:

输入：
nums = [1,3,1]
k = 1
输出：0
解释：
所有数对如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
"""


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        # 左闭右闭区间
        l = 0
        # 最远距离
        r = nums[-1] - nums[0]

        while l <= r:
            mid = (l + r) / 2
            if self.possible(mid, nums) < k:
                l = mid + 1
            else:
                r = mid - 1

        return l

    def possible(self, guess, nums):
        # 找出比guess小的个数
        count = left = 0
        for right, x in enumerate(nums):
            while x - nums[left] > guess:
                left += 1
            count += right - left
        return count

#  https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/solution/hei-ming-dan-zhong-de-sui-ji-shu-by-leetcode/
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
        # 最小的距离对
        l = 0
        # 最大的距离对
        r = nums[-1] - nums[0]

        while l < r:
            mid = (l + r) / 2
            if self.possible(mid, nums) >= k:
                r = mid
            else:
                l = mid + 1

        return l

    def possible(self, mid, nums):
        # 找出<=mid的对的个数
        count = 0
        l = 0

        # 这种遍历方法，其实能把所有的距离对都遍历出来
        for r in range(len(nums)):
            # 说明l太小了，得让l增加一下
            while nums[r] - nums[l] > mid:
                l += 1
            count += r - l

        return count

#  https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/solution/hei-ming-dan-zhong-de-sui-ji-shu-by-leetcode/
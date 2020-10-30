"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
示例 1:

输入: [3,0,1]
输出: 2
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 1

        n = len(nums)
        for i in range(n):
            # 因为nums[i]有可能是负数，所以我们先要判断它合不合法
            # 然后再进行换位操作
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 有可能出现[1],[2]这种情况，在这种情况下，我们要返回2，3
        # 所以对这种边界情况进行一个处理
        return n + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
Time: O(n), Space: O(1)
答案：
本题与41，442，448，268是用的同一套模版， 模版放在448那里

此题可以和268题对照来看
"""
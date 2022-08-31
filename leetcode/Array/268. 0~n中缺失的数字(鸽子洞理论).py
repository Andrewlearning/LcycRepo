"""
这个题目说的是，从 0 到 n 这 n+1 个整数中去掉一个，然后把剩下的 n 个整数放进一个长度为 n 的数组，给你这个数组，你要找到那个去掉的整数。

比如说，给你的数组是：

4, 1, 0, 2

这里的数组长度是 4，说明这是从 0 到 4 中去掉一个数字后形成的数组。数组中缺失的数字是 3，因此我们要返回 3。
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        n = len(nums)

        for i in range(n):
            # 我们希望 下标0->0, 下标1->1 ...
            # 既是希望 i = nums[i]
            # 既是说我们希望 i上的这个数 放在nums[i] 这个位置上
            # 所以当 nums[i] != nums[nums[i]]，表明没有满足下标和数的对应关系
            # 因为序列中有可能出现n , nums[n]会报out of range，所以我们要过滤掉这个条件
            while nums[i] < n and nums[i] != nums[nums[i]]:
                self.swap(nums, i, nums[i])

        for i in range(n):
            # 当不满足 i = nums[i] 的时候，说明i这个位置放的数有问题，返回这个下标应该对应的数 i+1
            if i != nums[i]:
                return i

        return n

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

# 本题与41，268是用的同一套模版
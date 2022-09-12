"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数, 其中nums里有负数
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

翻译一下:
有一个长度为n的数组，数组里每个数的范围在[-maxint,+maxint]
我们要从最小的正整数1开始，一次判断2/3/4 直到数组长度N是否在这个数组当中
其实就是找从[1, n+1]这些正整数，哪个在nums里缺失了


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
            # 我们希望进行位置交换的数，都是满足在[1,N]这个范围里的数
            # 我们希望下标0 -> 1、下标1 -> 2 ..
            # 既是说我们希望 index上的这个数 放在nums[index] - 1这个位置上
            # 为什么要套上nums[i] != nums[nums[i] - 1]呢，是为了防止多个数重复的情况
            # 例如[1,1], 假如i=1 (nums[i]-1)=0，那无论i和(nums[i]-1)如何交换，都出不了while循环
            # 所以我们限定了一定要数不一样才进入循环

            # 什么数，应该放在位置i呢？
            # 1. 满足条件的数 nums[i] = nums[nums[i] - 1]
            # 2. 不可能通过交换使合理的数，例如不在要求范围内的数，无论放在哪里都不满足，所以直接跳过，就放在这了
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 一直循环，直到找到当前位置的满足下标和下标对应的数的映射为止
                self.swap(nums, i, nums[i] - 1)

        for i in range(n):
            # 当不满足 i = nums[i] - 1 的时候，说明i这个位置放的数有问题，返回这个下标应该对应的数 i+1
            if nums[i] != i + 1:
                return i + 1

        return n + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
Time: O(n^2)最差结果while循环要把整个数组翻一遍才能找出来, Space: O(1)
https://leetcode.cn/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
答案：
本题与41，268是用的同一套模版，287， 448也可用

一个test case看懂这个题
p:0, nums[i] - 1:3, p:[[4 3 1 2]]
a:0, nums[i] - 1:1, p:[[2 3 1 4]]
--------------
p:0, nums[i] - 1:1, p:[[2 3 1 4]]
a:0, nums[i] - 1:2, p:[[3 2 1 4]]
--------------
p:0, nums[i] - 1:2, p:[[3 2 1 4]]
a:0, nums[i] - 1:0, p:[[1 2 3 4]]
可以看出，这道题的原理就是贪心，例如看下标0,他的本质就是不断交换数字
直到当前 下标，要不满足 nums[i] = nums[nums[i] - 1]，要不就完全不满足退出循环
所以当这样尝试过每个数之后，只有没放对位置的数是特殊的
--------------
"""
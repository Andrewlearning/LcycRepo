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
            # 所以当 nums[index] != nums[nums[index-1]]，表明没有满足下标和数的对应关系
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 我们希望下标0 -> 1、下标1 -> 2 ..
                # 所以我们希望把nums[i]这个数，放到nums[i] - 1这个下标上
                # 所以这里交换 i 和 nums[i] - 1
                # [3,4,-1,1] i=0, nums[i]-1=2, 所以我们要把i上的数，放到i=2上去 -> [-1,4,3,1]
                # 但是换完后，nums[i] - 1这个下标的数肯定被放置正确了, 但是新被换到i的这个数，我们还不知道有没有被放对，所以要使用while循环继续放
                self.swap(nums, i, nums[i] - 1)

        for i in range(n):
            # 当不满足 i = nums[i] - 1 的时候，说明i这个位置放的数有问题，返回这个下标应该对应的数 i+1
            if nums[i] != i + 1:
                return i + 1

        return n + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
Time: O(n), Space: O(1)
https://leetcode.cn/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
答案：
本题与41，268是用的同一套模版

此题可以和268题对照来看
"""
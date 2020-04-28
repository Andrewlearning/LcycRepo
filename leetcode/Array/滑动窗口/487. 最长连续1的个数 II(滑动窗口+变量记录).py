"""
给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。

示例 1：

输入：[1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
     当翻转以后，最大连续 1 的个数为 4。
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        l = 0
        res = 0
        zeros = 1

        for r in range(len(nums)):

            if nums[r] == 0:
                zeros -= 1

            while zeros < 0:
                if nums[l] == 0:
                    zeros += 1
                l += 1

            if r - l + 1 > res:
                res = r - l + 1

        return res

"""
Time: O(n)
Space:O(1)
本题与 1004的解法一样哈， 维持一个zeros变量，记录滑动窗口里最多可以放几个0

其实这题就是等于让你求，求一个包括1个0的最长1的子序列

所以我们需要维持一个双指针，来维持一个滑动窗口，滑动窗口内维持着一个 小于等于k的0的数量

假如说这个变量小于0，说明滑动窗口已经不能再放下0了，更新滑动窗口，l++
假如说这个变量大于0，说明滑动窗口还可以继续变长，更新滑动窗口，r++
"""
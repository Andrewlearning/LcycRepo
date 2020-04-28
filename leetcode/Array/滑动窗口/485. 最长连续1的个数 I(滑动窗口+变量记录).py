"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
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

        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
                continue

            if r - l + 1 > res:
                res = r - l + 1

        return res

"""
Time: O(n)
Space: O(1)
https://leetcode-cn.com/problems/max-consecutive-ones/solution/java-485-zui-da-lian-xu-1de-ge-shu-hua-dong-chuang/
这里介绍滑动窗口的做法
我们维持一个滑动窗口，滑动窗口维持都是连续的1
假如说滑动窗口右边新假如了一个0，那么说明整个滑动窗口已经被破坏了，l = r + 1

否则则进行判断，看滑动窗口的长度是否大于最大值
"""
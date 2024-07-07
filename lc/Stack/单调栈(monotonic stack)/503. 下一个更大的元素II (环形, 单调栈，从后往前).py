"""
给定一个循环数组nums（nums[nums.length - 1]的下一个元素是nums[0]
返回nums中每个元素的 下一个更大元素 。

数字 x的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，
这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        stack = []

        n = len(nums)
        
        # 每一个数的下一个更大元素, 作为答案
        # 这里不建议使用map来存，因为一个数在不同位置对应的下一个更大元素不一定一样
        nextLarger = [-1] * n

        # 原数组后面插入一个相同数组，因为本题为循环，同时这不会影响到判断
        nums.extend(nums)

        for i in range(2 * n - 1, -1, -1):
            x = nums[i]
            # 当新来的x比栈的堆顶元素大时，说明堆里面的数不能成为x的下一个更大数
            # 把堆顶元素pop出，直到在栈中找到第一个 > x的数为止
            while len(stack) > 0 and x >= stack[-1]:
                stack.pop()

            # 前面通过先遍历完后一个数组，已经把下一个最大元素找完了，当i<n的时候，我们要正式开始记录结果
            if i < n:
                # 假如栈长度不为0，说明当前数nums[i] nums[i+1, -1]中存在比它大的数
                # 下一个比与x(nums[i])大的数是堆顶元素
                if len(stack) > 0:
                    nextLarger[i] = stack[-1]

            # 处理完后，把当前nums[i]放入栈，用于给剩下的元素
            stack.append(x)
        return nextLarger


# https://www.acwing.com/video/1918/
# 处理环形问题时，我们可以通过extend一个相同数组来解决

# 我另一个做法
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        nextLarger = [-1] * (n)
        nums.extend(nums)

        for i in range(2 * n - 1, -1, -1):
            x = nums[i]

            while len(stack) > 0 and x >= stack[-1]:
                stack.pop()

            if len(stack) > 0:
                ni = i % n
                nextLarger[ni] = stack[-1]

            stack.append(x)

        return nextLarger
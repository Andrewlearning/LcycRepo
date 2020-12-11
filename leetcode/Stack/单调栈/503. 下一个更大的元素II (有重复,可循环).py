class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)

        # 存放还没找到下一个更大数的元素的下标
        stack = []

        for i in range(len(nums) * 2 - 1):
            # 当nums[i] 是下一个更大数时，把nums都可以满足的元素pop出
            while len(stack) != 0 and nums[stack[-1]] < nums[i % len(nums)]:
                # 直接把下一个最大值赋到index上
                res[stack.pop()] = nums[i % len(nums)]

            stack.append(i % len(nums))

        return res

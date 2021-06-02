# coding=utf-8
"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        self.res = []
        nums.sort()

        # 这属于一个比较通用的解法，因为在全排序2会碰到有相同元素的情况
        self.visited = [False] * len(nums)
        self.helper(nums, [])

        return self.res

    def helper(self, nums, temp):
        if len(temp) > len(nums):
            return

        if len(temp) == len(nums):
            self.res.append(temp[:])

        for i in range(len(nums)):
            # 假如说当前这个元素已经用过了，我们跳过
            if self.visited[i] == True:
                continue

            # i>0,保证了我们可以用到nums的第一个元素
            # self.visited[i-1] == True and nums[i-1] == nums[i]保证了我们用的 nums[i]都是和之前没重复的
            if i > 0 and self.visited[i - 1] == True and nums[i - 1] == nums[i]:
                continue

            self.visited[i] = True
            self.helper(nums, temp + [nums[i]])
            self.visited[i] = False

        return

"""
相比于permutation, 唯一的区别就是多了一个去重的处理
1. nums = sorted(nums) , 排序好了才可以去重
2. if i > 0 and nums[i] == nums[i - 1] and self.visited[i - 1]
   采用了全局去重，i > 0, 于此同时，我们要注意 self.visited[i-1] == False
   因为去除 i的重，要保证i-1已经在 答案列表里面了 

"""
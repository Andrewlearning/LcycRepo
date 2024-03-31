"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
在这个长度为8的数组，缺少了5，6这两个数
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            # 映射关系为下标0 -> 1， 下标1 -> 2
            # 由于没有特殊的不符合条件，所以这里只要处理 nums[i] != nums[nums[i] - 1]的情况

            # 什么数，应该放在位置i呢？
            # 1. 满足条件的数 nums[i] = nums[nums[i] - 1]
            # 2. 没有 不可能通过交换使合理的数，所以这里就不用写了
            while nums[i] != nums[nums[i] - 1]:
                # 一直循环，直到找到当前位置的满足下标和下标对应的数的映射为止
                self.swap(nums, i, nums[i] - 1)

        res = []
        for i in range(n):
            if nums[i] != i + 1:
                # 当下标的和下标对应的数不满足映射，说明当前位置的应该放置的正确数不存在，记录这个正确数
                res.append(i + 1)
        return res

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

# Time O(n^2), 因为最差情况while循环要把整个数组都翻一遍才能找到正确的数
# 本模板适用于41，268，487，448，最具体的解释可以参考41
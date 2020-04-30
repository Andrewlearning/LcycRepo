#coding=UTF-8
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

            # 表示看这个数字是不是在它应该在的index上
            # 如果不是的话，那么把这个数字(在i上） 放到它应该在的位置上 nums[i] - 1
            while nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)

            # 但是为什么我们这里的while循环 用的是nums[i] != nums[nums[i] - 1] 而不是nums[i] == i+1呢？
            # 因为nums[i]每次的数字都可能会变，但是i+1的值是定死的，i+1只能针对第一次的情况，所以对于第二次以后
            # 的循环， i+1 和 nums[i]都是无相关性的

        res = []
        for i in range(n):
            # 这里就是理解题意了
            # 排前：[4,3,2,7,8,2,3,1]
            # 排后：[1,2,3,4,3,2,7,8]
            # 因为我们想要知道当前位置应该放哪个数字,(i+1)表示 下标i应该放哪个数字，所以append i+1
            if nums[i] != i + 1:
                res.append(i + 1)

        return res

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

s = Solution()
s.findDisappearedNumbers([4,3,2,7,8,2,3,1])

"""
Time: O(n), Space: O(1)
https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/solution/tong-pai-xu-ji-yu-yi-huo-yun-suan-jiao-huan-liang-/
答案：
这题算41题的入门版

这种类型的题的核心思想是鸽子洞理论， 因为他给你[1,n]的数，一个长n的数组，然后里面肯定有重复
所以按道理说，我们是可以把 1-n按顺序排到数组里面去
所以我们就要按照这个定律来解题，例如

nums  1,2,3,4,5
inds  0,1,2,3,4

我们可以发现，要是所有元素都放置正确的话，那么 满足规律 nums[i] == nums[nums[i] - 1]
nums[i] 表示的是那个数字， nums[i] - 1 代表的是那个数字所应该在哪个index上
所以nums[i] == nums[nums[i] - 1] 表示看这个数字是不是在它应该在的index上

例如 nums[i] = 3, i = 2, nums[i]-1 = 2
"""
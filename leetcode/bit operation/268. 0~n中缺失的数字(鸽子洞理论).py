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
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ nums[i] ^ i
        return res

"""
Time: O(n), Space: O(1)
https://algocasts.io/episodes/vkmebGbP
答案：
1.还是x^x = 0 ， x^0 = x的操作
2.这里写法要有点讲究，使得可以用一次循环去把所有答案给求出来

Time: O(n), Space: O(1)
这题同时也可以跟 448,442,41一起看，同时写题模版可以用448的
"""


class Solution(object):
    def missingNumber(self, nums):
        if not nums or len(nums) == 0:
            return 0

        n = len(nums)
        for i in range(n):
            # 因为本题长度为n的数组，会包含0~n的数，所以假如说我们用nums[i]做index的话，会outofrange
            # 于是我们加上 0 <= nums[i] < n
            while 0 <= nums[i] < n and nums[i] != nums[nums[i]]:
                self.swap(nums, i, nums[i])

        for i in range(n):
            # 同时在这里我们进行调整
            # 排前 [9,6,4,2,3,5,7,0,1]
            # 排后 [0,1,2,3,4,5,6,7,9]
            # 我们可以看到的是9的位置应该放8，所以这里返回的是i
            if nums[i] != i:
                return i

        return n

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
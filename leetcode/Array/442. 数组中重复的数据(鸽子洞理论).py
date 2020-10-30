"""
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]
"""

# 本题关系 index = value - 1
class Solution(object):
    def findDuplicates(self, nums):
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

        res = []
        for i in range(n):
            # 这里就是理解题意了
            # 排前：[4,3,2,7,8,2,3,1]
            # 排后：[1,2,3,4,3,2,7,8]
            # 因为我们想要知道是哪个数字重复了（哪个数字放错位置了),而不是说哪个数字应该放那个位置，所以是nums[i]
            if nums[i] != i + 1:
                res.append(nums[i])

        return res

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

"""
https://www.acwing.com/video/1843/
Time: O(n), Space: O(1)
答案：
本题与41，442，448，268是用的同一套模版， 模版放在448那里

"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for num in nums:
            # 因为数字是1---n
            #    下标是0---n-1
            # 我们要让数字对应上下标，当前num所应该放在数组的对应位置
            cur_index = abs(num) - 1

            # 把数组对应位置的元素变为负数
            nums[cur_index] *= -1

            # 假如说对应位置的数字是正数，说明被多个相同数字对应了，说明当前num是重复数字
            if nums[cur_index] > 0:
                # 把当前num加进res
                res.append(abs(num))

        return res
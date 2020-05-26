"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

"""
class Solution(object):
    #  Time: O(n), Space: O(n)
    def rotate(self, s, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(s)

        # 处理k 大于长度的情况，我们已知旋转 length次的话，是会回到之前的起点， 所以我们就这样取%
        n = k % length

        # 先总体反转一遍
        self.reverse(s, 0, length - 1)

        # 然后再把 【0，n] 反转一遍
        self.reverse(s, 0, n - 1)

        # 然后再把 【n， length-1] 反转一遍
        self.reverse(s, n, length - 1)

        # 这样就能达到我们想要的效果了

        return s

    # Time: O(n), Space: O(1)
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

"""
https://algocasts.io/episodes/Z5mzgwGd

下面这题是向左旋转的， 面试题58 - II. 左旋转字符串
"""
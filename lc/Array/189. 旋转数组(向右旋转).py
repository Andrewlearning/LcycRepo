"""
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。

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
        n = len(s)

        # 处理k 大于长度的情况，我们已知旋转 n次的话，是会回到之前的起点， 所以我们就这样取%
        k = k % n

        # 先总体反转一遍
        self.reverse(s, 0, n - 1)

        # 然后再把 [0，k] 反转一遍
        self.reverse(s, 0, k - 1)

        # 然后再把 [k， n-1] 反转一遍
        self.reverse(s, k, n - 1)

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
这种题，怎么看往左还是往右呢，自己先试试就知道了

k = 3
# 原始数组                  : 1 2 3 4 5 6 7
# 反转所有数字后             : 7 6 5 4 3 2 1
# 反转前 k 个数字后          : 5 6 7 4 3 2 1
# 反转后 n-k 个数字后        : 5 6 7 1 2 3 4 --> 结果


# 链接：https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-by-leetcode/


下面这题是向左旋转的， 面试题58 - II. 左旋转字符串
"""
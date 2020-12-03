"""
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。

示例:

输入: 4, 14, 2

输出: 6

解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
"""

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        # 每个int都有31位
        for i in range(31):
            # 第i位是0的数的个数
            count0 = 0
            # 第i位是1的数的个数
            count1 = 0
            for num in nums:
                if num >> i & 1 == 0:
                    count0 += 1
                else:
                    count1 += 1

            # 因为第i位数是相同的话，那么彼此之间是没有汉明距离的
            # 假如说是0的数有3个，是1的数是两个
            # 那么在这一位上的汉明距离就是 3 * 2
            res += count0 * count1

        return res

# https://www.acwing.com/video/1886/
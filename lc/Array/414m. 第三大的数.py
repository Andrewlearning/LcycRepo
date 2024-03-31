"""
给定一个非空数组，返回此数组中第三大的数。
如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 3:

输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 记录最大的数出现次数
        count = 0
        a = b = c = float("-inf")

        for num in nums:
            # 都用大于号可以处理掉数字相同的情况
            if num > a:
                c = b
                b = a
                a = num
                count += 1

            elif a > num > b:
                c = b
                b = num
                count += 1

            elif b > num > c:
                c = num
                count += 1

        # 如果不存在三个最大的数，则返回数组中最大的数
        if count < 3:
            return a
        return c

# https://www.acwing.com/video/1809/
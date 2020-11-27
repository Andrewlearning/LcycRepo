"""

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        mark = 1

        # 先把两个只出现一次的数字异或到xor上
        # 两个数字异或， 那么， 不相等的位，会位1
        for num in nums:
            xor ^= num

        # 异或表示的是，不相等的反而为1，所以这个循环找的是，第一个两个数不想等的位置
        # 找到第一个分叉的点，mark表示分叉点在第几位
        # 分叉点可以表示为 0 1， 两个只出现一次的数字在这里肯定是分为 0 1
        while (xor & mark) == 0:
            mark <<= 1

        # 我们把mark位上0的分一组，mark位上为1的分一组
        # 这样我们就可以测出两个不重复的数字了
        x = 0
        y = 0

        for num in nums:
            if (num & mark) == 0:
                x ^= num
            # 注意，num & mark的结果不只是0和1
            else:
                y ^= num

        return [x, y]

"""
https://algocasts.io/episodes/yRp366G4
Time: O(n), Space: O(1)
"""
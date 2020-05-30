"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

数组长度为 5，
数组的数取值为 [0, 13]， 都是不重复的

总共16张牌
00 123456789 10 11 12 13

示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True
"""
class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 因为每次抽的牌都是不重复的， 所以我们能保证抽的五张牌都是不重复的
        # 所以我们只要保证 这五张牌 的 最大最小值的差不超过5，那么说明牌是一个顺子
        s = set()
        ma = -1
        mi = 14

        for num in nums:
            if num == 0:
                continue

            # 2. 设此 5 张牌中最大的牌为 max ，最小的牌为 min （大小王除外），则需满足：
            ma = max(ma, num)
            mi = min(mi, num)

            # 1. 除大小王外，所有牌 无重复
            # 假如说，抽到相同的数字，那么说明不可能形成顺子
            if num in s:
                return False

            s.add(num)

        # [1,2,3,4,5] , 5-1 < 4
        # 3. max - min < 5
        return ma - mi < 5

"""
# https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/

# 根据题意，此 5 张牌是顺子的 充分条件 如下：

1. 除大小王外，所有牌 无重复 ；
2. 设此 5 张牌中最大的牌为 max ，最小的牌为 min （大小王除外），则需满足：
3. max - min < 5
"""





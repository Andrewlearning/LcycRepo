"""
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
"""

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        def possible(K):

            # coco吃掉一堆香蕉的时间 Math.ceil(p / K) = ((p-1) // K) + 1
            return sum((p - 1) / K + 1 for p in piles) <= H

        # 左闭右闭
        # l 代表吃香蕉的最慢速度
        # r 代表吃香蕉的最快速度,一次最多只能吃一堆香蕉
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            # 说明在H时间内，吃不完所有香蕉，要加快吃香蕉的速度
            if not possible(mid):
                l = mid + 1
            # 说明在H时间内，吃吃完所有香蕉，要减慢吃香蕉的速度
            else:
                r = mid - 1

        # 出来的时候是 [r,l]
        #            [f,t] l代表的是最左有效边界
        return l

# 链接：https://leetcode-cn.com/problems/koko-eating-bananas/solution/ai-chi-xiang-jiao-de-ke-ke-by-leetcode/

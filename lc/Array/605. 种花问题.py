"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count = 0
        leng = len(flowerbed)

        for i in range(leng):
            # 1. 0 0 0 -> 0 1 0
            # 2. [0,0.. -> [1,0..
            # 3. ..0,0] -> ..0,1]
            # i == 0 or flowerbed[i - 1] == 0假如说数组越界，但是只要有其中一个对，就不会报错
            # 返回True
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and
                    (i == leng - 1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1
                count += 1

        return count >= n

"""
https://leetcode-cn.com/problems/can-place-flowers/solution/chong-hua-wen-ti-by-leetcode/
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            sum = max(sum, min(height[l], height[r]) * (r - l))
            # 移动左右边界时，哪个高度矮就移动哪个，贪心
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

"""
https://algocasts.io/episodes/k8GNameQ
答案：// Time: O(n), Space: O(1)
因为是两根柱子围成的面积表示盛水量，且这个面积由最短的那根柱子（木板效应）和宽度决定
所以我们要取一个平衡就是 有两根足够长的柱子，以及相对长的宽度

所以我们从最宽的地方开始遍历，假如说发现两根柱子哪根比较短，我们就移动短的柱子取新的位置
"""
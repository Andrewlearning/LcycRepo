class Solution(object):
    def largestRectangleArea(self, h):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = []
        n = len(h)

        # 储存当前元素，左边第一个比它小的元素下标
        left = [0] * n
        # 储存当前元素，右边第一个比它大的元素下标
        right = [0] * n

        for i in range(n):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            # 假如左边已经没有元素比h[i]小了，那么只能把left[i]标记成-1
            # 这样后面计算的下标的时候就表示从[0~i-1]都可以被用上
            if len(stack) == 0:
                left[i] = -1
            # 否则，记录左边第一个比h[i]小的元素
            else:
                left[i] = stack[-1]

            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()

            if len(stack) == 0:
                right[i] = n
            else:
                right[i] = stack[-1]
            stack.append(i)

        res = 0
        for i in range(n):
            # 我们只用遍历一遍
            # 用 当前高度 * (左右第一个比当前高度低的下标的坐标差) = 以当前高度为高的矩形面积
            res = max(res, h[i] * (right[i] - left[i] - 1))

"""
Time O(n) space O(n)
https://www.acwing.com/video/1428/

1 6 5 6 3
假如我们想找上面例子的最大矩形面积
可知道是5，因为5的左右都是6，完全可以利用到5的高度，但是到1和3不行
所以最大矩形高度是 5 * (4 - 0 - 1) = 15

所以我们的目的就是，利用两个单调栈，分别找出一个数的左右第一个低于该数的点
然后利用这些数值进行计算
"""
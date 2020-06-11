class Solution(object):
    # O(n) O(n)
    def largestRectangleAreaStack(self, heights):
        if not heights and len(heights) ==  0:
            return 0

        res = 0
        n = len(heights)
        # 递增的单调栈，遇到递增的数字，把下标加入
        stack = []
        r = 0

        for r in range(n+1):
            # 当r在直方图范围内时，h = height[r]
            # 当r不在直方图范围内时， h = 0
            h = 0 if r == n else heights[r]

            # 当r遍历到一个 小与 栈顶元素的值时。 那么开始计算高度
            # [l , index]这个范围就是矩形的宽
            while len(stack) != 0 and h < heights[stack[-1]]:

                index = stack.pop()
                l = -1 if len(stack) == 0 else stack[-1]
                res = max(res, heights[index] * (r - l - 1))

            # 1.当r遍历发现一直递增，则加入r的下标
            # 2.上面计算完毕后，我们也加入r的下标，因为比r高大的已经被pop完了
            # 3.当stack为空的时候
            stack.append(r)

        return res


"""
https://algocasts.io/episodes/RVmVlopQ

  同样的，我们也是遍历整个高度数组，同时把 i对应的数h 作为高度
  
  当 h >= 栈顶元素时，我们一直把h给加入stack中
  当 h < 栈顶元素时，我们开始进行操作
  例如 [1,2,3,4] h = 3
  这时候我们可以看到，h < 4, 这时候我们就要开始评估矩形的宽度了，因为以3为高度的话，至少栈顶元素，是可以被加进宽度里的
  这里要记住，我们需要的矩形，每跟柱子高度都至少要 >= h. 
  所以现在得出的矩形， 和第一问我们找出来的矩形，其实是一样的，但是这个因为只需要遍历一遍，所以速度上大大提升了
"""



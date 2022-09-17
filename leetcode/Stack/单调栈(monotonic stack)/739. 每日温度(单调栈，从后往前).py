"""
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用0 来代替。

例如，给定一个列表temperatures =  [73, 74, 75, 71, 69, 72, 76, 73]，
                    你的输出应该是[1, 1, 4,   2,  1,   1, 0, 0]。
                    (隔几天后能发现比自己大的)
"""

class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temp)

        res = [0] * n

        stack = []

        for i in range(n-1, -1, -1):
            x = temp[i]
            while len(stack) > 0 and x >= stack[-1][0]:
                stack.pop()

            if len(stack) == 0:
                res[i] = 0
            else:
                res[i] = stack[-1][1] - i 
            # 唯一的改变是，我们需要多储存一个下标，用来计算和下一个最高温度的距离
            stack.append([x, i])


        return res

"""
这题和503一样
时间空间复杂度都是 O(n)
https://www.acwing.com/activity/content/problem/content/3329/1/Python/
"""
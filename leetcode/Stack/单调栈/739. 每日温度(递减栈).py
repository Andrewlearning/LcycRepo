"""
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
                    你的输出应该是 [1, 1, 4,   2,  1,   1, 0, 0]。
                    (隔几天后能发现比自己大的)
"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        length = len(T)
        # 栈储存的只是元素的下标，当栈顶元素碰到比自己大的元素时，让两者的下标相减少
        stack = []

        # res的下标对应这的是元素的下标，上面的值代表着是 下一个比自己大的元素 在离自己有多远
        res = [0] * length

        for i in range(length):
            # 当栈不为空， 且当前温度大于栈顶温度时
            # 说明要把栈顶元素取出，然后 用当前 元素的下标 - 栈顶元素的下标，得到我们想要的答案
            while len(stack) > 0 and T[i] > T[stack[-1]]:
                temp = stack.pop(-1)
                res[temp] = i - temp

            stack.append(i)

        return res

"""
时间空间复杂度都是 O(n)
https://leetcode-cn.com/problems/daily-temperatures/solution/leetcode-tu-jie-739mei-ri-wen-du-by-misterbooo/


"""
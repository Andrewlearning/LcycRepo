class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 单调递增的栈，越栈底的值越小
        # 遍历时只有碰到比stack[-1]大的值，才会被加进栈中
        # 碰到比stack[-1]大的，说明都有可能会构成一个凹槽
        stack = []
        res = 0

        for i in range(len(height)):
            # 当栈不为空
            # 且栈顶元素(底) < 当前高度(右墙壁)的高度，这说明这里可能存在雨水
            # 每次我们有 左墙壁stack[-2], 底stack[-1], 右墙壁i 这三个元素，才可以计算雨水体积
            #
            # 同时我们怎么保证一定 左墙壁stack[-2] > 底stack[-1]，因为假如左墙壁stack[-2] < 底stack[-1]
            # 那么左墙壁就已经进入下面流程被pop掉了
            while stack and height[stack[-1]] < height[i]:
                # 获取底
                button = stack.pop()

                # 假如栈里没元素了，说明我们没有左墙壁了，无法接到雨水
                # pop的元素也不用理会，因为目前无法构成说明后面也无法构成
                if len(stack) == 0:
                    break

                # 获取左墙壁
                leftWall = stack[-1]
                # 获取右墙壁
                rightWall = i
                # 计算左右墙壁高度的最小值 和 底的差， 再乘左右墙壁的距离
                res += (min(height[leftWall], height[rightWall]) - height[button]) * (rightWall - leftWall - 1)

            # 每次都记录当前高度，因为今后都有作为左墙壁或者底使用的可能
            stack.append(i)

        return res
# 古城算法: https://www.youtube.com/watch?v=7QEIZy1pp2o 35:00
# 只有高度从低到高的时候我们才需要计算储水
# 高度递减的时候我们不需要管，因为不储水

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 0: return 0

        left_max = -1
        right_max = -1
        res = 0
        record = [0 for i in range(len(height))]

        for i in range(len(height)):
            left_max = max(height[i],left_max)
            record[i] = left_max

        for i in range(len(height)-1,-1,-1):
            right_max = max(height[i],right_max)
            record[i] = min(right_max,record[i])
            res += (record[i] - height[i])

        return res

"""
DP做法
https://algocasts.io/episodes/eAGQ1MG4
这题其实不难，看algocast的第一种解法
主要是，我们要从左到右遍历一次，记录当前到当前位置为止，从左到当当前位置的最大值（意味着左墙壁）
再从右向左遍历一次，记录到当前位置为止，从右往左的最大值（意味着右墙壁）
最后我们记录当前位置左右墙壁的最小值（木桶效应）
然后用当前左右墙壁的最小值 - 当前位置的高度，得到当前index的盛水量
然后我们把所有index的盛水量都加在一起得到最后的结果
"""



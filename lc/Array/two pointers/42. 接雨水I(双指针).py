class Solution:
    def trapTwoPointer(self, h: List[int]) -> int:
        if not h:
            return 0
        
        l, r = 0, len(h) - 1
        
        # 记录左右两边遇到的最大高度
        lmax, rmax = h[l], h[r]
        res = 0
        
        while l < r:
            # 如果左边最大高度小于右边最大高度
            # 说明当前下标的储水量由左边最大高度决定
            if lmax < rmax:
                l += 1
                # 更新左边最大高度
                lmax = max(lmax, h[l])
                # 当前下标的储水量 = 左边最大高度 - 当前位置高度
                res += lmax - h[l]
            else:
                # 如果右边最大高度小于等于左边最大高度
                # 说明当前下标的储水量由右边最大高度决定
                r -= 1
                # 更新右边最大高度
                rmax = max(rmax, h[r])
                # 当前下标的储水量 = 右边最大高度 - 当前位置高度
                res += rmax - h[r]
        
        return res


# time, space 都是O(n), 而且难记
class Solution(object):
    def trapStack(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 单调递增的栈，越栈底的值越小 e.g [4,3,1]
        # 遍历时只有碰到比stack[-1]大的值，才会被加进栈中
        # 碰到比stack[-1]大的元素，说明都有可能会构成一个凹槽 e.g. [4,3,1] 3
        stack = []
        res = 0

        for i in range(len(height)):
            # 当栈不为空
            # 且栈顶元素(底) < 当前高度(右墙壁)的高度，这说明这里可能存在雨水
            # 每次我们有 左墙壁stack[-2], 底stack[-1], 右墙壁i 这三个元素，才可以计算雨水体积
            #
            # 注意，这个过程在遇到同一面右墙壁的时候，可能会执行多次
            # 例如3,2,1,4,我们需要计算[2,1,4]和[3,2,4], 镁元素不能构成左墙壁，底，右墙壁
            #
            # 同时我们怎么保证一定 左墙壁stack[-2] > 底stack[-1]，因为假如左墙壁stack[-2] < 底stack[-1]
            # 那么左墙壁就已经进入下面流程被pop掉了
            while stack and height[stack[-1]] < height[i]:
                # 获取底, 同时pop掉，因为一个底只会被用一次
                button = stack.pop()

                # 假如栈里没元素了，说明我们没有左墙壁了，无法接到雨水
                # pop的元素也不用理会，因为目前无法构成也意味着后面也无法构成
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
# 使用用单调栈的做法
# 只有高度从低到高的时候我们才需要计算储水
# 高度递减的时候我们不需要管，因为不储水



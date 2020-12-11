"""
给定一个非重叠轴对齐矩形的列表 rects，写一个函数 pick 随机均匀地选取矩形覆盖的空间中的整数点。

提示：

整数点是具有整数坐标的点。
矩形周边上的点包含在矩形覆盖的空间中。
第 i 个矩形 rects [i] = [x1，y1，x2，y2]，其中 [x1，y1] 是左下角的整数坐标，[x2，y2] 是右上角的整数坐标。
每个矩形的长度和宽度不超过 2000。
1 <= rects.length <= 100
pick 以整数坐标数组 [p_x, p_y] 的形式返回一个点。
pick 最多被调用10000次。
 

示例 1：

输入:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
输出:
[null,[4,1],[4,1],[3,3]]
"""

from random import randint
class Solution(object):
    # 先按面积随机,再看区间随机
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        # 以所有矩形的面积为一条线，每两个点都代表不同矩形里的一段面积
        self.weight = [0]
        # 所有矩形的面积之和
        self.s = 0
        for rect in rects:
            # 边缘也要计算进去，例如2-0，里面应该有2，1，0三个点
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.s += area
            self.weight.append(self.s)

    def pick(self):
        """
        :rtype: List[int]
        """
        # 先按照所有面积取一个随机数
        randomFromArea = randint(1, self.s)

        # 根据这个矩形面积来找到对应的矩形,用左闭右闭区间来找
        l = 0
        r = len(self.weight) - 1
        while l < r:
            mid = l + r >> 1
            if self.weight[mid] >= randomFromArea:
                r = mid
            else:
                l = mid + 1

        # 因为在self.weight里我们加了0在开头，所以我们要减去这个影响量
        index = r - 1

        rect = self.rects[index]
        # 随机选出一个矩形后，再随机从这个矩形中取点
        return [randint(rect[0], rect[2]), randint(rect[1], rect[3])]


# https://www.acwing.com/activity/content/code/content/576557/
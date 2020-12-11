from bisect import bisect_left
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

        # 根据这个矩形面积来找到对应的矩形
        l = 1
        r = len(self.rects)
        while l < r:
            mid = l + r >> 1
            if self.weight[mid] >= randomFromArea:
                r = mid
            else:
                l = mid + 1
        print(123)

        # 因为在self.weight里我们加了0在开头，所以我们要减去这个影响量
        index = r - 1

        rect = self.rects[index]
        return [randint(rect[0], rect[2]), randint(rect[1], rect[3])]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
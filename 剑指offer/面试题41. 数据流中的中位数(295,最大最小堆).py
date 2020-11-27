from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 最小堆
        # 放着的是数据流中 ”较大的一半“
        # 不需要对值进行额外操作
        self.small = []

        # 最大堆
        # 放着的是数据流中 ”较小的一半“
        # 需要对值 去负数来实现最大堆
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 当两个堆长度相等时，我们往较小的一部分（self.large）插入新元素 [12] 3 [45]
        # 但再此之前， 我们得先确认这个加入这个元素，是否是在较小的那一半
        # 因为有可能是 [12] 6 [45] 这种情况，所以我们需要把真正的在较小一半的元素取出来
        # 既是 [12] 4 [56]
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))

        # 当最大堆的元素较多时， 我们则需要把 较小部分(self.small) + 新元素 中找出最大的元素，加入进 self.small里面去
        # [1,2,3] [4,5] 0, -> [0,1,2] [3,4,5]
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(-self.small[0] + self.large[0]) / 2.0
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
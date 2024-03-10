from heapq import *
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 最小堆, 放着的是数据流中 "较大的一半"
        # 因为我们希望每次pop出来是最小值
        # 不需要对值进行额外操作
        self.large = []

        # 最大堆，放着的是数据流中 "较小的一半"
        # 因为我们希望每次pop出来的是最大值
        # 需要对值取负数 来实现最大堆
        self.small = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 当两个堆长度相等时，我们往插入较大部分插入新元素
        # 然后把较大部分的最小值取出
        # 最后把较大部分的最小值放入到较小部分中
        # 例如[12] 6 [45] -> [12] [456] -> [12] 4 [56] -> [124][56]
        if len(self.large) == len(self.small):
            heappush(self.large, num)
            smallestInlarge = heappop(self.large)
            heappush(self.small, -smallestInlarge)

        # 当两个堆长度不相等时，那肯定是较小部分的长度大(根据上面的条件)
        # 当self.small元素较多时， 我们则需要把 (self.small + 新元素) 中找出最大的元素，加入进 self.large里面去
        # [1,2,3] [4,5] 0 -> [1,2,3,0] [4,5] -> [0,1,2] 3 [4,5] -> [0,1,2] [3,4,5]
        else:
            heappush(self.small, -num)
            largestInSmall = heappop(self.small)
            heappush(self.large, -largestInSmall)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.large) == len(self.small):
            return float(self.large[0] + -self.small[0]) / 2.0
        else:
            return float(-self.small[0])


"""
https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
https://algocasts.io/episodes/VlWdOvp0
答案：
1.这题我们运用了一个最大堆(self.small)和一个最小堆(self.large)
2.由于我们要找中位数，所以我们让两个堆的数量保持在一个相同 或 large比small多一个数
  总共有2n+1个数，small里有n个数，large里面有n+1个，那么我们返回large里面最小的那个数就好了
  总共有2n个数，  small里有n个数，large里面有n个数，那我们返回 samll里最大的，large里面最小的，/2.0就好了

3.一个数进来
  如果len相同：那我们要往large里加一个数，所以我们得把那个数先丢进samll里面，验证一波,然后把pop出来的数字，放入large中
  why?
  因为假如说num 是small里最大的，那么它也会被pop出来，如果它并不是samll里最大的，那么就把small里最大的pop出来
  
  如果len不同（len(large)> len(small)):我们要往small里加数，我们得先把num 丢进large里验证一波，然后pop出，放入small中
  
注意：
1.我们用 -num 来构造最大堆，给small使用
2.所以最后计算和的时候， large[0] - small[0]
"""
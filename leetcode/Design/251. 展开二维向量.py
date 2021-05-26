"""
请设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 next 和 hasNext 两种操作。

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // 返回 1
iterator.next(); // 返回 2
iterator.next(); // 返回 3
iterator.hasNext(); // 返回 true
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 4
iterator.hasNext(); // 返回 false
"""
class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.nums = v
        # i 表示在第几个ceil
        self.i = 0

        # j 表示在ceil里的第几个元素
        self.j = 0

    # case1: i没到还在范围内，且j已经到了这个ceil的最后一个元素时, 移动到下一个ceil
    # case2: 当[i][j] 指向是一个空的列表的时候，能跳过，直接跳到有元素的地方
    def toNextMeaningfulValue(self):
        while self.i < len(self.nums) and self.j == len(self.nums[self.i]):
            self.i += 1
            self.j = 0

    def next(self):
        """
        :rtype: int
        """
        self.toNextMeaningfulValue()
        # 若没有在一个cell的最后一个位置，那么将直接读取当前位置的值，并把y指针向后移动
        res = self.nums[self.i][self.j]
        # 移动到下一个元素
        self.j += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        self.toNextMeaningfulValue()

        # 假如[i]越界了，说明已经没有下一个值了，所以说明没有下一个元素了
        return self.i < len(self.nums)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# lc官方答案
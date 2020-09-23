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
        self.element = v
        # x 表示在第几个ceil
        self.x = 0

        # y 表示在ceil里的第几个元素
        self.y = 0

    def next(self):
        """
        :rtype: int
        """
        # x没到还在范围内，且y已经到了这个ceil的最后一个元素时
        # 我们要移动到下一个ceil
        while self.x < len(self.element) and self.y == len(self.element[self.x]):
            self.x += 1
            self.y = 0

        # 若没有在一个cell的最后一个位置，那么将直接读取当前位置的值，并把y指针向后移动
        res = self.element[self.x][self.y]
        # 移动到下一个元素
        self.y += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        # x没到还在范围内，且y已经到了这个ceil的最后一个元素时
        # 我们要移动到下一个ceil
        while self.x < len(self.element) and self.y == len(self.element[self.x]):
            self.x += 1
            self.y = 0

        # 因为假如说 [[null],[null]]这种情况，self.x一直++
        # 所以假如说没有下一个值，self.x总会++到 等于len(self.element)
        return self.x < len(self.element)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# lc官方答案
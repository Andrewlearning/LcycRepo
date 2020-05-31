class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # 当前price 前面有多少个小于它的元素
        weight = 1

        # 当单调栈里有元素，且栈里最后一位 小于 当前的价格
        while self.stack and self.stack[-1][0] <= price:
            # 那么当前price, 就是要消去比它小的元素，并加上比他小的元素的weight
            weight += self.stack.pop(-1)[1]

        # 假如说栈里没有碰到 比当前元素小的数时，我们直接把
        # （当前元素，左边比当前元素小的数）加进去
        # 假如有的话，那么在上面我们已经把它的weight 给加进当前的price里了
        self.stack.append((price, weight))

        return weight

"""
https://leetcode-cn.com/problems/online-stock-span/solution/gu-piao-jie-ge-kua-du-by-leetcode/

时间复杂度：O(Q)，其中Q是调用next() 函数的次数。
空间复杂度：O(Q)。
"""
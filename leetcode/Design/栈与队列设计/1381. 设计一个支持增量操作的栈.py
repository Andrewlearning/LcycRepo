"""
题目较为复杂，直接上网看
"""

class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.cap = maxSize
        self.inc = [0] * maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.cap:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        topIndex = len(self.stack) - 1
        if topIndex < 0:
            return -1

        # 这里其实利用了lazy propagation, 我们对于[0~topindex]需要递增的值，我们只记录在topindex
        # 当要pop的时候，才+进去
        if topIndex > 0:
            self.inc[topIndex - 1] += self.inc[topIndex]

        res = self.stack.pop() + self.inc[topIndex]
        self.inc[topIndex] = 0
        return res

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        # 记录需要递增值的最远范围
        topIndex = min(k, len(self.stack)) - 1
        if topIndex >= 0:
            self.inc[topIndex] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

"""
古城算法 35：00
https://www.bilibili.com/video/BV1Po4y1979k

push(1)  inc [0]                                         stack={1}
push(2)  inc [0,0]                                       stack={1,2}
increment(1,100)  inc[100,0]                             stack={1,2}
pop()    return 2 + inc[1] = 2 + 0 = 2                   stack={1}
pop()    return 1 + inc[0] = 1 + 100 = 101               stack={}
"""

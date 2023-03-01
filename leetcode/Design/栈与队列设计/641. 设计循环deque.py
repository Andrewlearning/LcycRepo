"""
设计一个循环的deque

"""
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0
        self.cap = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front -= 1

        # 指针越界，处理
        if self.front < 0:
            self.front += self.cap

        self.q[self.front] = value
        self.size += 1

        # 比如只放入了一个元素，rear应该被重置，这个corner case很重要
        if self.size == 1:
            self.rear = self.front

        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.cap
        self.q[self.rear] = value
        self.size += 1

        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear -= 1

        # 指针越界，处理
        if self.rear < 0:
            self.rear += self.cap
        self.size -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.cap

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

"""
古城算法 30：00
https://www.bilibili.com/video/BV1Po4y1979k
"""
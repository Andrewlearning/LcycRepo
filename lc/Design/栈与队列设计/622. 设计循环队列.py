class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        # 构造队列
        self.q = [0] * k

        # 队列头指针，从这里推出元素
        # 第一个推出元素的位置是0
        self.front = 0

        # 队列尾指针，从这里插入元素
        # 因为第一个插入的位置是0，然后我们是(self.tail + 1) % len(self.q)，所以初始化为-1
        self.tail = -1

        # 队列的size
        self.size = 0

    # 往队列新插入一个元素，假如队列已满，则无法插入
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # 如何保证循环队列，不会把元素赋值到有效元素那里，通过isFull()来判断
        if not self.isFull():
            # 指针往后移动一位取mod再插入
            self.tail = (self.tail + 1) % len(self.q)
            self.q[self.tail] = value
            self.size += 1
            return True
        else:
            return False

    # 把队列最后的元素取出
    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            # 不用管之前的元素了，直接把指针往后移动一位就好
            self.front = (self.front + 1) % len(self.q)
            self.size -= 1
            return True
        else:
            return False

    # 取队列最前面元素的值
    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.front]

    # 取队列最末尾的值
    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == len(self.q)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

"""
时间复杂度：O(1)。该数据结构中，所有方法都具有恒定的时间复杂度。
空间复杂度：O(N)，其中 N 是队列的预分配容量。循环队列的整个生命周期中，都持有该预分配的空间。

古城算法 27:00
https://www.bilibili.com/video/BV1Po4y1979k
"""
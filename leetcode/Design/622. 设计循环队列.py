class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.head = 0
        self.capacity = k
        self.count = 0
        self.queue = [0] * k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """

        if self.count == self.capacity:
            return False

        #
        new_value = (self.head + self.count) % self.capacity
        self.queue[new_value] = value

        self.count += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.count == 0:
            return False

        # 出队，我们只要把头指针移向下一位就好了， 因为只有在[头，尾] 之间的元素才属于队列元素
        self.head = (self.head + 1) % self.capacity

        self.count -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.count == 0:
            return -1

        last_index = (self.head + self.count - 1) % self.capacity
        return self.queue[last_index]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.count == self.capacity

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


https://leetcode-cn.com/problems/design-circular-queue/solution/she-ji-xun-huan-dui-lie-by-leetcode/
本题最重要的一个定律，那就是
假设一个queue有count个元素，那么我们已知head节点，那么tail节点的位置是在
tail = (head + count - 1) % capacity

与此同时，假如说我们要新加进去一个元素，那么这个元素应该加到队列的尾部元素再往后一个位置
new = (head + count) % capacity

还有一个就是，如果我们要删除一个元素，那么我们要做的就是，把head 的index往后挪动一位就好了
head = (head + 1) % capacity
"""
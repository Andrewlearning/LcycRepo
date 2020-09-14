"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty

"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 新增元素时，只先append到栈1
        # pop元素时，当self.out有元素，self.out.pop()
        #           当self.out无元素，把self.inn的元素append到self.out后，在self.out.pop()
        self.inn = []
        self.out = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.inn.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # pop元素时，当self.out有元素，self.out.pop()
        #           当self.out无元素，把self.inn的元素append到self.out后，在self.out.pop()
        if len(self.out) > 0:
            return self.out.pop()

        # [] [1,2,3]
        # [3,2,1] []
        # [3.2] 1 []
        else:
            while self.inn:
                self.out.append(self.inn.pop())
            return self.out.pop()

    # 返回队列最左端的元素
    # 先查self.out, 因为当self.in self.out都有元素时
    # self.out的元素比较老
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.out:
            return self.out[-1]
        else:
            return self.inn[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.inn) == 0 and len(self.out) == 0

"""
和剑指offer的第五题一样
"""
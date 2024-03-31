"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 每次只留一个最早来的元素在里面，用来pop
        self.out = []

        # 用来把非最早来的元素给滤出来，最后再给回self.out
        self.temp = []

    # 元素全放到self.out里
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.out.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.out) == 0:
            return None
        if len(self.out) == 1:
            return self.out.pop()

        # 过程是这样的, 把out队列里前面的元素都装进temp里面去，然后再剩下的最后一个元素pop掉
        # temp[]    out[1,2,3]
        # temp[1,2] out[3] 只留一个元素在out是因为queue只能从队首出
        # temp[]    out[1,2] pop_element=3
        while len(self.out) >= 2:
            self.temp.append(self.out.pop(0))
        pop_element = self.out.pop()

        self.out, self.temp = self.temp, self.out

        return pop_element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.out[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.out) == 0


"""
用两个队列实现一个栈的功能?要求给出算法和思路!

入栈：将元素进队列A

出栈：
    1.判断队列A中元素的个数是否为1，如果等于1，则出队列
     2.否则将队列A中的元素,以此出队列并放入队列B，直到队列A中的元素留下一个，
     然后队列A出队列，再把队列B中的元素出队列以此放入队列A中。
     
     
     入队：将元素进栈A

出队：判断栈B是否为空，如果为空，则将栈A中所有元素pop，并push进栈B，栈B出栈；

 如果不为空，栈B直接出栈。
"""

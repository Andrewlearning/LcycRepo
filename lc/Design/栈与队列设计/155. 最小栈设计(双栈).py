"""
Design a stack that supports push, pop, top, and retrieving the minmum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minmum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # min是一个辅助栈，与data同增同减，但是min添加的时候
        # 是添加当前（栈自身，以及新增元素）的最小值
        # 用于处理getMin()
        self.min = []
        # 这个用来进行处理普通元素的push,pop,top
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # self.data就是直接push或者pop了
        self.data.append(x)

        # 我们要保证self.min[-1]一定是self.min里的最小元素
        # 所以只有当self.min没有元素，或者新元素比self.min原有的最小元素小才能直接append
        if len(self.min) == 0 or x < self.min[-1]:
            self.min.append(x)
        else:
            # 否则则继续append self.min原有的最小元素
            self.min.append(self.min[-1])


    def pop(self):
        """
        :rtype: None
        """
        self.min.pop()
        self.data.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]

"""
套娃题目716，max stack
"""
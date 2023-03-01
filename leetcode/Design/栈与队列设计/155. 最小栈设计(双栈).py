"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

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
        # mini是一个辅助栈，与data同增同减，但是mini添加的时候
        # 是添加当前（栈自身，以及新增元素）的最小值
        # 用于处理getMin()
        self.mini = []
        # 这个用来进行处理普通元素的push,pop,top
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.mini) == 0 or x < self.mini[-1]:
            self.mini.append(x)
        else:
            self.mini.append(self.mini[-1])


    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.mini.pop(-1)
            return self.data.pop(-1)


    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.mini:
            return self.mini[-1]

"""
套娃题目716，max stack
"""
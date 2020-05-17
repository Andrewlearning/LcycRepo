class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

        # assist栈的作用是，把当前所有元素的最小值的放进里面去
        self.ass = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

        if len(self.ass) == 0:
            self.ass.append(x)
        else:
            if x < self.ass[-1]:
                self.ass.append(x)
            else:
                self.ass.append(self.ass[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)
        self.ass.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.ass[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

"""
使用双栈，一个栈正常记录，另一个栈专门记录每次全部值的最小值
"""
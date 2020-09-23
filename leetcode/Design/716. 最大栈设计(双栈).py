class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxstack = []
        self.stack = []

    # 我们把要push 的元素push到 self.stack里
    # 我们把当前所有元素的最大值，给push 到 self.maxstack里
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 假如说 maxstack为空，那么我们就把x放进maxstack里
        # 假如   maxstack不为空， 那么我们就把 maxstack的最大值赋予max
        max = x if len(self.maxstack) == 0 else self.maxstack[-1]

        # 我们把 x, max 这两个数的最大值 赋值到max 中
        max = x if x > max else max


        self.maxstack.append(max)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        移除栈顶元素并返回这个值。
        """

        # 因为maxstack 的这个栈顶元素， 是与stack的栈顶元素同时入栈的，仅代表当时那个状态的最大值
        # 所以也要同时删掉
        self.maxstack.pop(-1)
        return self.stack.pop(-1)


    def top(self):
        """
        :rtype: int
        返回栈顶元素。
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        返回栈中最大元素。
        """
        return self.maxstack[-1]

    def popMax(self):
        """
        :rtype: int
        返回栈中最大的元素，并将其删除。如果有多个最大元素，只要删除最靠近栈顶的那个。
        """
        max = self.peekMax()

        # 我们用buffer 来记录 [被删元素前 + 被删元素后]
        buffer = []
        while self.top() != max:
            buffer.append(self.pop())

        self.pop()

        while len(buffer) > 0:
            self.push(buffer.pop(-1))


        # 最终返回max
        return max


"""
时间复杂度：O(n)。由于前四个操作的时间复杂度都是 O(1)，而 popMax() 操作在最坏情况下需要将栈中的所有元素全部出栈再入栈，时间复杂度为 O(n)。因此总的时间复杂度为 O(n)
空间复杂度：O(n)

链接：https://leetcode-cn.com/problems/max-stack/solution/max-stack-by-leetcode/

"""
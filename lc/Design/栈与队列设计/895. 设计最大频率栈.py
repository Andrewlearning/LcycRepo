"""
Design a stack-like data structure to push elements to the stack
 and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.

If there is a tie for the most frequent element,
the element closest to the stack's top is removed and returned（频率相同，则推栈顶）.
"""

from collections import defaultdict
from heapq import heappush, heappop

class FreqStack(object):

    def __init__(self):
        self.freq = defaultdict(int)
        self.heap = []

        # 记录栈的高度
        self.idx = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1
        self.idx += 1

        # 入栈的时候，最先按照freq来排序从大到小排，然后再按照离栈顶的距离从大到小排
        heappush(self.heap, (-self.freq[val], -self.idx, val))

    def pop(self):
        """
        :rtype: int
        """
        _, _, val = heappop(self.heap)
        self.freq[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


"""
古城算法 46：00
https://www.bilibili.com/video/BV1Po4y1979k
利用了heap, 时间复杂度O(logn)
"""
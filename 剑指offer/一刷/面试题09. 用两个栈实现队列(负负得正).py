"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
类型：stack & queue
"""

class CQueue(object):
    def __init__(self):
        self.inn = []
        self.out = []

    # O(1)
    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.inn.append(value)

    # O(n)
    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.inn and not self.out:
            return -1

        if len(self.out) == 0:
            while self.inn:
                self.out.append(self.inn.pop(-1))

        return self.out.pop(-1)


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

"""
这题的思想是：负负得正

栈是先进后出，那么假如说一个元素经历两次先进后出，那么不就等于先进先出了吗
这就是我们这两个栈的用处

当我们要加一个元素的时候，我们把它append进 self.inn里面去

当我们要删除一个元素的时候
1.假如说self.out没元素，那么要把元素从self.inn里pop出来，
    再append进self.out, 这样self.out.pop的时候，顺序就是先进先出

2.假如说self.out有元素，那么就把元素从self.out里pop出来就好了
    为什么此时我们不把元素从self.inn 加进self.out里去呢？因为新来的元素会压住老的元素，完不成queue

"""
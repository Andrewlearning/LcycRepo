# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        self.helper(s, 0)
        return self.res

    def helper(self, s, cur):

        res = NestedInteger()
        if s[cur] == "[":
            # 跳过左括号， 接下来应该是数字
            cur += 1
            # 假如说self.p没有便利到当前[]的右括号，一直执行下去

            while s[cur] != "]":
                self.helper(s, cur)
            # 跳过右括号
            cur += 1
            # 假如说跳过[]后，还没结束的话，那么则要跳过逗号
            if cur < len(s) and s[cur] == ",":
                cur += 1

        # 因为[], 这些符号已经被上面处理过了
        # 这个else专门用来处理数字
        else:
            # 数字开头
            start = cur
            while cur < len(s) and cur != "," and cur != "]":
                cur += 1
            # 截取数字
            self.res.setInteger(s[start:cur])

            # 跳过逗号
            if cur < len(s) and s[cur] == ",":
                cur += 1

        return res















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
"""
给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。

列表中的每个元素只可能是整数或整数嵌套列表

提示：你可以假定这些字符串都是格式良好的：

字符串非空
字符串不包含空格
字符串只包含数字0-9、[、-、,、]

给定 s = "324",

你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
示例 2：

给定 s = "[123,[456,[789]]]"
"""
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        self.p = 0
        return self.helper(s)

    def helper(self, s):
        res = NestedInteger()
        # [123, 发现一个左括号，说明里面存在内部节点，我们要递归处理内部节点
        # 里的所有儿子
        if s[self.p] == "[":
            # 跳过左括号
            self.p += 1

            # 处理所有在[ 中的数字，并把这儿子节点加到我们的结果里
            # 假如说没再碰到右括号的话，那就数字依次add进res里
            # 假如说碰到了右括号，退出循环
            while s[self.p] != "]":
                res.add(self.helper(s))

            # 跳过右括号
            self.p += 1

            # 假如p跳过了右括号且在,上, 则跳过逗号
            if self.p < len(s) and s[self.p] == ",":
                self.p += 1

            # 返回当前[]里的所有东西

        # 假如s[p]是数字
        else:
            # 数字的有边界
            r = self.p

            while r < len(s) and s[r] != "," and s[r] != "]":
                r += 1
            # 节点只是数字的话，那就把这个数字设置到res里，然后返回
            res.setInteger(int(s[self.p:r]))

            # 跳过逗号
            if r < len(s) and s[r] == ",":
                r += 1

            # 假如说 123】是这样的话,那么self.p就指向],然后返回
            self.p = r

        return res

# https://www.acwing.com/activity/content/problem/content/2770/1/












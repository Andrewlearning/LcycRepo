"""
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

 

示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
"""
class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.res = []
        # 一个用于指向下个元素的指针
        self.p = 0
        # 初始化self.res,把里面的值都填充到里面
        for value in nestedList:
            self.helper(value)

    #
    def helper(self, integer):
        # 假如当前元素是数字，那么把数字加进res里去
        if integer.isInteger():
            self.res.append(integer.getInteger())
        # 假如当前元素不是数字，那说明是一个【】，那么遍历里面的东西,继续判断里面的元素是数字还是[]
        else:
            for value in integer.getList():
                self.helper(value)

    def next(self):
        """
        :rtype: int
        """
        res = self.res[self.p]
        self.p += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p < len(self.res)

# https://www.acwing.com/video/1729/

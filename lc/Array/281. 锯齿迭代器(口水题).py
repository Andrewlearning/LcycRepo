"""
给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。

示例:

输入:
v1 = [1,2]
v2 = [3,4,5,6]

输出: [1,3,2,4,5,6]

解析: 通过连续调用 next 函数直到 hasNext 函数返回 false，
     next 函数返回值的次序应依次为: [1,3,2,4,5,6]。
"""
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.combination = []
        self.index = 0
        size_1 = len(v1)
        size_2 = len(v2)
        i = 0
        j = 0
        while i < size_1 and j < size_2:
            self.combination.append(v1[i])
            i += 1
            self.combination.append(v2[j])
            j += 1

        if i != size_1:
            self.combination += v1[i:]
        if j != size_2:
            self.combination += v2[j:]

    def next(self):
        """
        :rtype: int
        """
        if self.index < len(self.combination):
            res = self.combination[self.index]
            self.index += 1
            return res
        return -1

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.combination)


# 作者：idealworld
# 链接：https://leetcode-cn.com/problems/zigzag-iterator/solution/python-3-solution-by-idealworld/
# 来源：力扣（LeetCode）

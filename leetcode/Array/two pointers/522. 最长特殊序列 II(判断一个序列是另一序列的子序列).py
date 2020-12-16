"""
给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。

输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。

 

示例：

输入: "aba", "cdc", "eae"
输出: 3
"""

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        self.n = len(strs)
        ans = -1
        for i in range(self.n):
            isSub = True
            for j in range(self.n):
                if i != j and self.check(strs[i], strs[j]):
                    isSub = False
                    break

            # 当[i]字符串，不是其他字符串的子序列，说明他就是独有的最长子序列
            if isSub:
                ans = max(ans, len(strs[i]))
        return ans

    # 在这里展示怎么判断只用 O(n)
    def check(self, a, b):
        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
            j += 1

        return i == len(a)

# https://www.acwing.com/video/1946/
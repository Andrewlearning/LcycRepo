"""
给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。

示例 1:

输入: 12
输出: 21

"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))
        length = len(n)

        p = length - 2
        while p >= 0 and n[p] >= n[p + 1]:
            p -= 1

        # 不存在，返回-1， 例如321,不能通过替换找到一个更大的数了
        if p < 0:
            return -1

        # 从后往前遍历，找到第一个比n[p] 大的数
        i = length - 1
        while i > p and n[i] <= n[p]:
            i -= 1

        # 找完以后，交换 i,p两个元素的位置
        self.swap(n, p, i)

        # 然后再把(i,p)之间的所有元素给反转一下便好
        self.reverse(n, p + 1, length - 1)

        res = int("".join(n))
        if abs(res) > 2 ** 31:
            return -1
        else:
            return res

    def swap(self, n, i, j):
        n[i], n[j] = n[j], n[i]

    def reverse(self, n, i, j):
        while i < j:
            self.swap(n, i, j)
            i += 1
            j -= 1

"""
时间复杂度：O(n)。最坏情况下，只会扫描整个数组两遍，这里 n 是给定数字的位数。
空间复杂度：O(n)。使用了大小为 n 的数组 a ，其中 n 是给定数字的位数。

本题和31题一摸一样
https://leetcode-cn.com/problems/next-greater-element-iii/solution/xia-yi-ge-geng-da-yuan-su-iii-by-leetcode/
"""
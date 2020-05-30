"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        if n == 0:
            return ""

        # 因为我们的数字是从1-n，所以我们也构造一个0-n的使用列表，方便使用
        self.used = [False for _ in range(n + 1)]
        path = []

        # 同样的，我们看我们 可供选择数字有多少，那它的阶乘就有多少
        # 例如我们可以剩三个数可以选择，那么我们就还有 3*2*1=6种选择
        # 一开始我们有n个数可以选， 所以我们要做到 range(n+1)
        self.factorial = [1 for _ in range(n + 1)]

        # 制作阶乘
        for i in range(2, n + 1):
            self.factorial[i] = self.factorial[i - 1] * i

        #  我们使用的path,一直都是同一个地址，这个与之前的做法不一样
        # index为几的时候，说明path有几个元素，一开始没元素，为0
        self.helper(n, k, 0, path)

        return ''.join([str(num) for num in path])

    def helper(self, n, k, index, path):
        # 当长度等于n， 返回答案
        if index == n:
            return

        # cnt的含义是，假设当前这一位被选中的话，这一位被选中后还剩下多少种可能性
        cnt = self.factorial[n - 1 - index]

        for i in range(1, n + 1):
            # 不能用用过的元素
            if self.used[i]:
                continue

            if cnt < k:
                k -= cnt
                continue

            # 发现这里没，不用与别的全排序的回溯法，我们append之后不需要pop()
            # 因为我们的每一位，都是经过精心选择过的。是确定的。不用悔改的
            # 不用与别的全排序，可以做出很多分叉，来试看哪个可以到达终点
            path.append(i)
            self.used[i] = True

            # 寻找下一位
            # 这里我们不用 path + [i] 是因为，这样path会变成一个新的数组。而我们这里的做法要求是
            # 返回最初的数组
            self.helper(n, k, index + 1, path)

"""
https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/
"""
"""
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。
"""

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        zeros, l, res = 0, 0, 0

        # 我们用循环来控制滑动窗口的右边界
        for r in range(len(A)):

            # 看看新进滑动窗口的数字是不是0
            if A[r] == 0:
                zeros += 1

            # 当0的数量大于k的时候，说明滑动窗口内已经不能已经不能把超出的0变成1了
            # 因此要缩小滑动窗口
            while zeros > K:
                if A[l] == 0:
                    zeros -= 1
                l += 1

            # 当滑动窗口的长度大于记录的最大值，更新
            if r - l + 1 > res:
                res = r - l + 1
        return res

"""
Time O(n*K), k表示有多少个0
space O(1)

https://blog.csdn.net/qq_17550379/article/details/88101343
其实这题就是等于让你求，求一个包括K个0的最长1的子序列

所以我们需要维持一个双指针，来维持一个滑动窗口，滑动窗口内维持着一个 小于等于k的0的数量

右边指针，指向0的话，就说明窗口里多一个0,zeros+1
左边指针指向0，要往右走，说明窗口里要少一个0。 zeros-1

最后我们来记录这个滑动窗口最长有多长
"""
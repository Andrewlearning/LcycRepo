"""
几乎每一个人都用乘法表。但是你能在乘法表中快速找到第 k 小的数字吗？

乘法表是大小为 m x n 的一个整数矩阵，其中mat[i][j] == i * j（下标从 1 开始）。

给你三个整数 m、n 和 k，请你在大小为m x n 的乘法表中，找出并返回第 k小的数字。

输入: m = 3, n = 3, k = 5
输出: 3
解释:
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
"""

class Solution(object):
    def findKthNumber(self, lengthI, lengthJ, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        l, r = 1, lengthI * lengthJ
        while l < r:
            mid = (l + r) // 2
            if self.lessAndEqualk(mid, lengthI, lengthJ) >= k:
                r = mid
            # 当小与等于mid的数量 < k，说明mid太小了，需要变大
            # 这用于反推出我们需要求左边界
            else:
                l = mid + 1
        return l

    def lessAndEqualk(self, x, lengthI, lengthJ):
        count = 0
        """
        k=4, <= 4的数有多少呢
        (1	2	3)
        (2	4)	6
        (3)	6	9
        第一列，min(4//1, 3) = 3, 取min length rows是因为，有可能k//i会超出这一行的个数
        第二列，min(4//2, 3) = 2
        ...
        """
        for i in range(1, lengthI+1):
            count += min(x // i, lengthJ)
        return count


# 与378题一样
# 关于乘法表如何计算小与等于k的数：https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/solution/cheng-fa-biao-zhong-di-kxiao-de-shu-by-leetcode/

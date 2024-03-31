"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashmap = {}
        res = 0
        for a in A:
            for b in B:
                if a+b in hashmap:
                    hashmap[a+b] += 1
                else:
                    hashmap[a+b] = 1

        # 前面记录了 a+b 有多少种可能
        # 例如 3:2, 1:3
        # 那么 c+d = -3的话，那就意味着 a+b+c+d 有两种可能，因为a+b = 3有两种组合
        for c in C:
            for d in D:
                if -(c+d) in hashmap:
                    res += hashmap[-(c + d)]
        return res


# 链接：https://leetcode-cn.com/problems/4sum-ii/solution/liang-shu-zhi-he-kuo-zhan-ban-by-powcai/

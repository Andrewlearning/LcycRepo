"""
题目说明了下一行的所有值比上一行的所有值都要大
这题应该用二分查找来做
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        lr = len(matrix)
        lc = len(matrix[0])
        l = 0
        r = lr * lc - 1

        # 这里只找答案，所以使用左右边界都可以
        while l < r:
            mid = (l + r) // 2

            mi = mid // lc
            mj = mid % lc

            if matrix[mi][mj] >= target:
                r = mid
            else:
                l = mid + 1

        return matrix[l // lc][l % lc] == target

#  https://www.acwing.com/solution/content/159/
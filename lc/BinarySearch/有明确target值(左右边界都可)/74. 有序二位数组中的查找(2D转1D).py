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
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = n * m - 1

        def getNum(i):
            row = i // m
            col = i % m
            return matrix[row][col]

        while l < r:
            # 这里只找答案，所以使用左右边界都可以
            mid = (l + r) // 2

            if getNum(mid) >= target:
                r = mid
            else:
                l = mid + 1

        return getNum(l) == target

#  https://www.acwing.com/solution/content/159/
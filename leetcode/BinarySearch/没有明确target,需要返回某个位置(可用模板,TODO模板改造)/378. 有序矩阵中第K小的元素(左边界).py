"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.
"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import sys
        l = -sys.maxsize
        r = sys.maxsize

        while l < r:
            mid = (l + r) // 2

            # 统计有多少个小于mid的元素
            cnt = 0
            j = len(matrix[0]) - 1

            # 扫描每一行，把小与mid的元素个数的都记录下来
            for i in range(len(matrix)):
                # 横坐标
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1

                cnt += j + 1

            # 我们要找的元素是第k小的元素，意味着有 小与mid的元素 >= k个，
            # 因为有可能出现重复元素，所以我们要取 >= k这个区间的左边界
            if cnt >= k:
                r = mid
            else:
                l = mid + 1

        return r

# https://www.acwing.com/video/1763/
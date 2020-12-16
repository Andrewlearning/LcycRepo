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
        length_i = len(matrix)

        # 左闭右闭
        l = matrix[0][0]
        r = matrix[-1][-1]

        while l <= r:
            mid = (l + r) // 2

            # 有count个元素小于等于mid
            count = self.getCount(matrix, mid, length_i)

            # 如果数量少于 k，那么说明最终答案 x 大于 mid
            if count < k:
                l = mid + 1
            # 如果数量不少于 k，那么说明最终答案 x 不大于 mid
            # r包含了有效的区间，并把有效区间向左推
            else:
                r = mid - 1
                
        # 想不懂为什么是有效区间的左边界
        return l

        # 求count是，从左下往右上遍历，O(N)

    def getCount(self, matrix, target, n):
        # 从左下角出发,向右上角走
        i = n - 1
        j = 0
        count = 0
        while i >= 0 and j < n:
            # 小于等于，必须包含相等，即便等于目标值的数量
            if matrix[i][j] <= target:
                count += i + 1
                # 是按一列列来计算的,算完一列移动到下一列
                j += 1
            else:
                i -= 1
        return count

"""
https://www.youtube.com/watch?v=1VkP3Ndu1C4&t=311s
"""
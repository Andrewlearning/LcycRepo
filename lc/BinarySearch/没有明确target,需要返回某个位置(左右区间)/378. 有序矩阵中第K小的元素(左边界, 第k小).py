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

            # 统计有多少个 <= mid的元素
            cnt = 0
            j = len(matrix[0]) - 1

            # 扫描每一行，把matrix[i][j] <= mid的元素个数的都记录下来
            for i in range(len(matrix)):
                # 每次向下一层走，但从上一次的横坐标继续往左看，因为从上往下数字是递增的
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1

                cnt += j + 1

            """
            如果说，mid这个数，从小到大排是第k位的
            那就意味着 <= mid的个数，是 >= k的
            <= mid的个数，=k 这种可能是显然的
            <= mid的个数，>k 这种可能是因为mid这个数字可能有多个相同的
            btw, 这个推理我不是很能接受，我比较能接受从 cnt < k 不满足，来推出上面得使用左边界模板
            """
            if cnt >= k:
                r = mid
            # if cnt < k, 那么说明这个mid不在答案区间以内，需要进行调整
            # 同时通过这个很清晰的条件，我们能推断出这里得使用左边界的模板
            else:
                l = mid + 1

        return r

# https://www.acwing.com/video/1763/
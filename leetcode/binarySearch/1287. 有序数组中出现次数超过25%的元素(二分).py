import bisect
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        span = n // 4 + 1

        # 在这里，我们把这个数组分成了四份，我们只去查看那四个点上
        # 因为假如说有值是超过25%，在这四个点上，必有一个点是这个数，等于是一种减枝
        for i in range(0, n, span):
            # 找到左右
            left = bisect.bisect_left(arr, arr[i])
            right = bisect.bisect_right(arr, arr[i])

            # 看长度
            if right - left + 1 > span:
                return arr[i]
        return -1



# https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array/solution/you-xu-shu-zu-zhong-chu-xian-ci-shu-chao-guo-25d-3/
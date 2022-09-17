import bisect
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        # 我们需要确保一个数 >= 25%
        # 假如单纯 // 4的话，遇到无法整除的会向下取整，所以我们使用 //4 + 1, 这是 > x//4 的最小数
        span = n // 4 + 1

        # 在这里，我们把这个数组分成了四份，我们只去查看那四个点上[0,25,50,75]
        # 因为假如说有值是超过25%，在这四个点上，必有一个点是这个数
        for i in range(0, n, span):
            # 找到这个数出现的左右区间
            left = bisect.bisect_left(arr, arr[i])
            right = bisect.bisect_right(arr, arr[i])

            # 看这个这个数出现的个数有没有超过 25%
            if right - left + 1 > span:
                return arr[i]
        return -1



# https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array/solution/you-xu-shu-zu-zhong-chu-xian-ci-shu-chao-guo-25d-3/
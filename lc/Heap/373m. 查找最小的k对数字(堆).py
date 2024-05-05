"""

给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。

定义一对值queens(u,v)，其中第一个元素来自queensnums1，第二个元素来自 nums2。

找到和最小的 k 对数字queens(u1,v1), (u2,v2) ... (uk,vk)。

Input:
nums1 = [1,7,11]
nums2 = [2,4,6], k = 3

Output: [[1,2],[1,4],[1,6]]
"""
from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n1 = len(nums1)
        n2 = len(nums2)

        # 因为nums1[0] 是nums1中最小的数
        # 所以我们把 nums1[0] 和 nums2中所有的数组成对子放进heap中
        # 这里无论是用nums1[0] 还是用 nums2[0]结果都是一样的(已验证)
        heap = []
        for i in range(n2):
            heappush(heap, [nums1[0] + nums2[i], 0, i])

        res = []
        for i in range(k):
            # 把堆中最小的搞出来
            val, x, y = heappop(heap)
            res.append([nums1[x], nums2[y]])

            # 因为我们已经把 nums1和nums2中最小的组合给放进去了
            # 但是我们不知道是nums1[第二小],nums2[第一小] ? nums1[第一小],nums2[第二小] 的关系
            # 所以我们还要把(nums1[第二小],nums2[第一小]) 给加进去
            # 这样做的目的是减少空间
            if x + 1 < n1:
                heappush(heap, [nums1[x+1] + nums2[y], x+1, y])
        return res

"""
https://algocasts.io/episodes/Z5mz0Qpd
这题的接发基本上和378一摸一样，唯一不同的地方在于，我们要想办法去利用两个数组去构造一个矩阵，来形成对子
且这个矩阵也要是，从左到右，从上到下递增
"""


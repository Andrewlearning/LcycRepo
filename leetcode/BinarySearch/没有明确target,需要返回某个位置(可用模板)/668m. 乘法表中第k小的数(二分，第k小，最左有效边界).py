"""
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
        while l <= r:
            mid = (l + r) / 2
            if self.enough(mid, lengthI, lengthJ) < k:
                l = mid + 1

            # 把有效区间向左推
            else:
                r = mid - 1
        return l

    """
    当且仅当乘法表中存在小于或等于k ，enough(x) 才为真。
    通俗地说，enough(x) 描述了 x 是否足够大可以成为乘法表中的k^th值。
    """
    def enough(self, x, lengthI, lengthJ):
        count = 0
        for i in range(1, lengthI+1):
            count += min(x // i, lengthJ)
        return count



# 链接：https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/solution/cheng-fa-biao-zhong-di-kxiao-de-shu-by-leetcode/

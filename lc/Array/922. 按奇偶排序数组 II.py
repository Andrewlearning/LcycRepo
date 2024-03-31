"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。

示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
"""
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 只指向偶数下标
        pEven = 0

        # 只指向奇数下标
        pOdd = 1

        while pEven < len(A) and pOdd < len(A):
            # 满足交换条件
            if A[pEven] % 2 != 0 and A[pOdd] % 2 != 1:
                A[pEven], A[pOdd] = A[pOdd], A[pEven]
                pEven += 2
                pOdd += 2
            elif A[pEven] % 2 != 0:
                pOdd += 2
            else:
                pEven += 2
        return A
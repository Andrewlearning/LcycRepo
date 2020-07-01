"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。


示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
"""


class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """

        length = len(a)
        b = [1 for _ in range(length)]

        for i in range(1, length):
            b[i] = b[i - 1] * a[i - 1]

        temp = 1
        # 因为对于我们来说，最开始的话，是要从最边缘既是a[i+1]开始的
        # b[i] a[i+1], i+1 = length-1
        for i in range(length - 2, -1, -1):
            temp *= a[i + 1]
            b[i] *= temp

        return b
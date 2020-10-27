"""
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # 差分数组就是两个元素的差构成的数组
        # a1 a2 a3
        #    d1 d2
        diff = []

        # 构建差分数组
        for i in range(1, len(A)):
            diff.append(A[i] - A[i - 1])

        res = 0
        i = 0
        while i < len(diff):
            # 双指针
            j = i

            # 计算相同的差分元素有多少个，移动右指针
            while j < len(diff) and diff[j] == diff[i]:
                j += 1

            # k表示相同的差分数组元素有几个
            k = j - i
            # 同时更新i到差分数组相同的最后一个元素
            i = j - 1

            # 把当前差分数组所能构成的不同等差数列算出来
            # 假如说元素为2的时候，k = 1, k-1=0, 会没有结果，所以这也默认保障了等差数列要至少三个元素的特性
            res += k * (k - 1) // 2

            # 更新i
            i += 1

        return res

# https://www.acwing.com/video/1808/
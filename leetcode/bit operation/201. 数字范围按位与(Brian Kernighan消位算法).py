"""
本题意思是，给你两个数字，一个大（n）一个小(m)
让我们求出他们在二进制中的公共前缀

输入: [5,7]
输出: 4

5 :  00101
7 :  00111
res: 00100 = 4
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 我们不断消去大数的末尾的1，直到大数不比小数大，说明此时n就是公共前缀
        while n > m:
            n = n & (n - 1)

        return n

"""
时间复杂度：O(logn)。和位移方法类似，算法的时间复杂度取决于 mm 和 nn 二进制展开的位数。尽管和位移方法具有相同的渐近复杂度，但 Brian Kernighan 的算法需要的迭代次数会更少，因为它跳过了两个数字之间的所有零位。
空间复杂度：O(1)。我们只需要常数空间存放若干变量。

链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/shu-zi-fan-wei-an-wei-yu-by-leetcode-solution/
"""
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
这题用y总的办法写吧，他的解释也比较好懂
https://www.acwing.com/activity/content/problem/content/2569/
"""
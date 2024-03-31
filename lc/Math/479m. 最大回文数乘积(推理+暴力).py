"""
你需要找到由两个 n 位数的乘积组成的最大回文数。
由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。
示例:
输入: 2
输出: 987
解释: 99 x 91 = 9009, 9009 % 1337 = 987
说明:
n 的取值范围为[1,8]。
"""
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 当只有一位数的时候，最大回文数是 3*3 = 9
        # 特殊情况
        if n == 1:
            return 9

        # n位数所能构成的最大值, n = 3, maxv = 999
        maxv = 10 ** n - 1

        # n位数所能构成的最小值, , n = 3, minv = 100
        minv = 10 ** (n-1)

        # 我们从n位数所能构成的最大值开始枚举到最小值
        for i in xrange(maxv, minv, -1):

            left = str(i)
            right = str(i)[::-1]
            # 构造当前 n位数所能构成的回文数
            palindrome = int(left + right)

            # 再次遍历，看n位数 * n位数是否能构成我们上面创造的回文数
            j = maxv
            while j * j >= palindrome:
                if palindrome % j == 0:
                    return palindrome % 1337
                j -= 1

        return

# https://www.acwing.com/video/1885/
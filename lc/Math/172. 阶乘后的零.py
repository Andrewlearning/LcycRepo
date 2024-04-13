"""
Given an integer n, return the number of trailing(后面的，拖尾的) zeroes in n!.

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity时间复杂度为log(n)
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        25 20 15 10 5"""

        res = 0
        while n != 0:
            res += n // 5
            n //= 5
        return res

"""
time:O（log5n) space:O(1)
https://algocasts.io/episodes/RVmVVomQ
这题让我们找一个数的阶乘的尾巴有多少个0
实际上就在问我们一个数的阶乘后面有多少个10
假如把x!分解质因式到最小 x! = 2^a * 5^b *...

且我们知道，2的倍数出现次数是远远多余5的倍数，所以我们只用统计5**b 中的b是多少就行了

例如 n = 5, 里面只有5，对应有一个0
例如 n = 25, 里面有 25,20,15,10,5, 其中25可以拆分成5*5, 所以25!中总共有6个5作为质因数，对应有6个0
"""





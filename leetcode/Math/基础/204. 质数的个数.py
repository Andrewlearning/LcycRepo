"""
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
注意这里是less than n,就是假如说n = 7，那么质数取不到7
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        used = [True] * n
        used[0] = used[1] = False

        # 遍历到上界 n**0.5
        for i in range(int(n ** 0.5) + 1):
            if used[i] == True:

                # 这里其实我们可以从 i*i开始，但是为了方便理解，我们还是从2*i开始
                for j in range(2 * i, n, i):
                    used[j] = False

        return sum(used)

"""
空间法度 O（n），时间法度O（nloglogn)
algocast
"""

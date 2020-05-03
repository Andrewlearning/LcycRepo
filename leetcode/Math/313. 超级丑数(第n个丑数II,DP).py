"""
丑数就是一堆幂函数乘积，比如例题[2,7,13,19]，那么丑数就是 2^x * 7^y * 13^z * 19^k

 的一系列数。所以我们只要判断是否乘以primes是下一个丑数即可。

"""
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n < 1:
            return -1

        res = [0] * n

        res[0] = 1

        # 看每个primes的系数是多少
        primes_bit = [0] * len(primes)

        for i in range(1, n):

            # 把res 和 prime 和 prime的系数乘一遍，找到那个最小值更新res[i]
            res[i] = min(x * res[y] for x, y in zip(primes, primes_bit))

            for j in range(len(primes)):

                # 如果本次答案求出的最小值 >= 上一次primes次数*primes, 那么要更新primes次数
                # 方便找到下一个prime
                if res[i] >= res[primes_bit[j]] * primes[j]:
                    primes_bit[j] += 1

        return res[-1]

"""
本题和264基本一摸一样，只不过prime数组从固定的235，变成了一个非固定数组
解题模式照抄
https://leetcode-cn.com/problems/super-ugly-number/solution/dong-tai-gui-hua-dui-by-powcai/
"""


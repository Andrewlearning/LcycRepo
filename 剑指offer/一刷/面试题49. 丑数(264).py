class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 1

        res = [0] * n
        res[0] = 1

        ptwo = pthree = pfive = 0

        for i in range(1, n):
            cur_min = min(res[ptwo] * 2, res[pthree] * 3, res[pfive] * 5)
            res[i] = cur_min

            # 为什么我们这里每个指针都要判断，而不是if，elif
            # 因为有可能会出现，多个下一个丑数相同的情况，我们要保证他们都是最新的
            # [1,2,3]  p2=2 p3=1
            # res[p2]*2 == res[p3]*3 == 6

            if res[ptwo] * 2 == cur_min:
                ptwo += 1

            if res[pthree] * 3 == cur_min:
                pthree += 1

            if res[pfive] * 5 == cur_min:
                pfive += 1

        return res[-1]
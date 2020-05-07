class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.pairs = {("0", "0"), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')}
        n = len(high)
        self.res = set()
        self.low = int(low)
        self.high = int(high)

        # 为什么需要一个 n, 和一个n-1
        # 因为假如5 进去， 那么self.res就会记录 长度为5，3的所有可能，但是4，2的却记录不了
        # 这是因为递归每次都将长度 -2 来进行匹配
        # 所以我们要对奇偶数都进行处理
        self.helper(n)
        self.helper(n - 1)

        if self.low < 10:
            for k in [0, 1, 8]:
                if self.low <= k <= self.high:
                    self.res.add(k)

        return len(self.res)

    def helper(self, n):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']

        ans = []
        for center in self.helper(n - 2):
            for l, r in self.pairs:
                # 我们不用处理 010 类似这种情况，因为下面len(str(int(temp)))直接就能把开头的0 给消除了
                temp = l + center + r
                ans.append(temp)

                # len(str(int(temp))) == n的作用，就是最左侧的0给消除掉，然后把0做外围的数给筛选掉
                # 因为例如传5 进来，那么合格的串应该是 5，3。 那么假如我们把0消掉以后，就剩2，4了，自然就被
                # 排除了
                if len(str(int(temp))) == n and self.low <= int(temp) <= self.high:
                    self.res.add(temp)

        return ans

"""
https://leetcode-cn.com/problems/strobogrammatic-number-iii/solution/python3-xiao-lu-bu-gao-dan-shi-li-yong-liao-247de-/
总体上来说复用了247 的代码
思路是先把有可能的情况都构造出来， 然后 把带0的数筛选掉，并且把符合大小的数都翻进去
"""
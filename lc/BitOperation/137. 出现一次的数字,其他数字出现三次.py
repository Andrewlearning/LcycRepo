class Solution(object):
    def convert(self, x):
        """
        1.
        int总共有32位, 在带符号的int中，第1位 0是代表正数，1是代表负数，所以只有31位数可以用
        所以正数总共有 2 ** 31种选择可以选，但是由于0占其中一种，所以signed int最大是 2 ** 31 - 1
        由于负数不用考虑0，所以signed int最小值是 2 ** 31
        所以在这里，假如我们发现x > 2 ** 31 - 1，说明超出int正数范围了，是负数，所以我们要减去最高位的1 - (2**32)

        2. 与本题无关，因为signed int需要考虑正负， unsigned int不需要考虑正负，所以它的取值范围是 [0, 2**32-1]
        关于更多二进制正负数的细节，可以参考 https://blog.csdn.net/dovakejin/article/details/112446946
        """
        if x >= 2 ** 31:
            x -= 2 ** 32
        return x

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for bit in range(32):
            cur_sum = 0

            for num in nums:
                # 统计当前bit上，有多少个1
                cur_sum += (num >> bit) & 1

            if cur_sum % 3 == 1:
                # 假如说当前bit sum mod=1
                # 这说明了出现一次的数字在当前bit上不为0
                # 我们这样拼接32个bit, 就能还原出只出现一次的数字
                # 我们把mod = 1的位，全部or到res上去
                res |= (1 << bit)

        return self.convert(res)


"""
https://algocasts.io/episodes/qjG0eXpK
Time: O(n), Space: O(1)
"""
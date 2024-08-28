class Solution(object):
    def convert(self, x):
        """
        - 有符号整数：从 -2^31 到 2^31 - 1，即从 -2147483648 到 2147483647。
        - 无符号整数：从 0 到 2^32 - 1，即从 0 到 4294967295。

        由于这里的做法，在给res赋值的时候，我们是把它当成无符号整数来处理的。
        但是最后返回结果时，要求我们返回有符号整数

        所以在这里，假如我们发现x > 2 ** 31 - 1，说明超出signed int正数范围了，则说明这个无符号整数对应的是有符号整数的负数，所以我们要减去 2**32
        至于为什么是2**32, 这是signed int和unsigned int转换的一种通用做法，数学逻辑过于复杂，不去深究
        """
        if x > 2 ** 31 - 1:
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
                # 假如说当前bit sum mod=1, cur_sum = 3*n + 1
                # 这说明了出现一次的数字在当前bit上不为0
                # 我们这样拼接32个bit, 就能还原出只出现一次的数字
                # 我们把mod = 1的位，全部or到res上去
                res |= (1 << bit)

        return self.convert(res)


"""
https://algocasts.io/episodes/qjG0eXpK
Time: O(n), Space: O(1)

补码表示法简介
在计算机中，signed int通常使用补码表示法。对于一个n位的signed int：
- 正数保持其二进制表示不变。
- 负数的表示方式是：对对应的正数的二进制表示取反，然后加1。

例如，对于32位整数，数字的范围是：
- signed int：从 -2^31 到 2^31 - 1，即从 -2147483648 到 2147483647。
- unsigned int：从 0 到 2^32 - 1，即从 0 到 4294967295。

转换的原理
当你想将一个无符号的32位整数转换为signed int时，考虑以下两种情况：
- 数字小于 2^31：这些数字的二进制表示与其在有符号和无符号表示下的值相同。
 - 例如，123456 在有符号和无符号表示下都是 123456。
- 数字大于或等于 2^31：这些数字对应的二进制表示在有符号表示下是负数。
 - 比如，4294967294 的二进制表示为 11111111111111111111111111111110，如果解释为signed int，其值为 -2。


为什么减去 2^32？
当unsigned int n 大于等于 2^31 时，它的二进制表示在signed int的范围中对应一个负数。
如果你直接使用这些位表示signed int，它实际上是在 2^32 的基础上进行了一次循环。例如，4294967294 可以看作是在 2^32 基础上减去2得出的结果。
所以，减去 2^32，将unsigned int强制转换到signed int范围，使得这些大于或等于 2^31 的数能够正确映射为负数。

总结
通过检查数字是否大于等于 2^31，你可以确定它是否在signed int范围内表示为负数。
减去 2^32 是在高位溢出的情况下，将其转化为正确的负数值。这种方法简洁而有效。

------------------------------------

有符号整数和无符号整数的相互转换
有符号整数（signed int）转无符号整数（unsigned int）
unsigned_int = signed_int % (2**32)

无符号整数（unsigned int）转有符号整数（signed int）
if unsigned_int >= 2**31:
    signed_int = unsigned_int - 2**32
else:
    signed_int = unsigned_int
"""
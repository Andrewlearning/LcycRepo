"""
本题意思是，给你两个数字，一个大（n）一个小(m)，求出 m ~ n 范围内，所有数字的&的答案
让我们求出他们在二进制中的公共前缀

输入: [5,7]
输出: 4

5 :  00101
7 :  00111
res: 00100 = 4
"""
# GPT给的答案
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        move = 0

        # 一直删除后缀，知道left == right, 说明此时left, right都等于彼此的公共前缀
        while left != right:
            left >>= 1
            right >>= 1
            move += 1

        # 由于此时left只剩下公共前缀，所以我们把剩下的位补充为0就好了
        return left << move

class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        l = left
        r = right

        res = 0
        # 由于int正数最大是2 ** 31 - 1,转换成2进制就是31个1，所以就从第31位开始遍历
        for i in range(31, -1, -1):
            # 假如l和r在从右往左第i位数不一样，则停止对公共前缀的记录
            # 每次拿1和移动过位置过后的l, r的最后一位比较
            if (l >> i & 1) != (r >> i & 1):
                break

            # 当找到公共前缀为1的位置时，把这个位置记录在答案里
            if l >> i & 1 == 1:
                res |= 1 << i
        return res

"""
这题用y总的办法写吧，他的解释也比较好懂
https://www.acwing.com/activity/content/problem/content/2569/

这题的证明:
对于m <= n, 他们总是会有前缀的
例如前缀是xxxx
对于m, 就是 xxxx0___
对于n，就是 xxxx1___ (因为n>=m)
对于xxxx，共同前缀，他们这个区间的数字相互 & 的结果都是一样，重要的是后面那些数字

在 m ~ n的范围内
对于m, xxxx0____, 必然存在一个数是 xxxx011..11 >= m
对于n, xxxx1____, 必然存在一个数是 xxxx1000..0 <= n
由于在and操作中，数字的位置不重要，所以我们可以把那两个数给提取出来
xxxx011..11 &  xxxx1000..0 & ... & n & m 结果得到除共同前缀以外，其他位置的数都是0

例如,5,6,7可以发现两两之间必有公共前缀
>>> bin(5) - 101
>>> bin(6) - 110
>>> bin(7) - 111
"""
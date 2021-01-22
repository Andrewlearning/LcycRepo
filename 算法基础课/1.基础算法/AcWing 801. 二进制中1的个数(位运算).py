"""
位运算的两种常见操作

n的二进制第k位是几？
n = 15 = 11111
     i = 43210

1. 先把第k位移到最后一位 n >> k
2. 个位是几 n&1
-----------------------------
lowbit(x)：返回x的最后一位1
x = 1010, lowbit(x) = 10
x = 101000, lowbit(x) = 1000

lowbit = x & (-x) = x & (~x+1)

x    = 1010...(1)000
~x   = 0101...(0)111
~x+1 = 0101...(1)000
x & (~x+1) = 1000

应用: 树状数组/统计一个数里二进制1的个数
https://www.acwing.com/video/246/
"""

def lowbit(num):
    count = 0
    while num:
        num -= num & (-num)
        count += 1
    return count


if __name__ == "__main__":
    n = map(int, input().split())
    nums = list(map(int, input().split()))
    res = []

    for num in nums:
        res.append(lowbit(num))

    print(" ".join(map(str, res)))

"""
三种码的关系，原码，反码，补码

x = 1010
原码 = 0..01010(他自己)
反码 = 1..10101(原码取反)
补码是取反+1
补码 = 1..10110 (取反+1)

为什么是补码表示负数，因为在计算机底层是没有减法的
假如说x >= 0， 我们要 -x

x + (-x) = 0
    (-x) = 0 - x
         = 000....000 - x
         然后因为要完成-，操作，所以我们在32个0前面添加一个1，变为1000...000
         = 1000...000 - x
         = ~x + 1

"""


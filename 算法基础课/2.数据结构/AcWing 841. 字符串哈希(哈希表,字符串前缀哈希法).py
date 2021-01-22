"""

字符串前缀哈希法
我们可以利用前缀哈希，算出任意一个子串的哈希值
又因为hash函数的特殊设定，使得字符串的哈希值基本不会产生重复
因此可以用这个来判断任意子串是否相等
"""


def getHash(l, r):
    # h[l - 1] * p[r - l + 1] 是为了让p的次方数对齐
    # 从而使得相减能得到 [l,r] 段的hash值
    return (h[r] - h[l - 1] * p[r - l + 1]) % mod


if __name__ == "__main__":
    n, m = map(int, input().split())
    string = " " + str(input())

    N = 100010

    # 哈希值不能映射为0
    # P=131 和 mod=2^64 是最好组合，产生的哈希碰撞是最少的
    P = 131
    mod = 2 ** 64

    # p代表，p进制的情况下，p次方数的值
    # p^0  p^1 ..
    p = [0] * N
    h = [0] * N
    mod = 2 ** 64

    p[0] = 1

    for i in range(1, n + 1):
        p[i] = (p[i - 1] * P) % mod

        # 前缀哈希
        # h[0] = 0
        # h[1] = "A"
        # h[2] = "AB"
        # H[3] = "ABC"
        # ...
        # ABCD 转换成p进制
        # 1234p
        # (1*p^3 + 2*p^2 + 3*p^1 + 4*p^0) % 2**63
        h[i] = (h[i - 1] * P + ord(string[i])) % mod

    while m:
        l1, r1, l2, r2 = map(int, input().split())
        if getHash(l1, r1) == getHash(l2, r2):
            print('Yes')
        else:
            print('No')
        m -= 1

# idea: https://www.acwing.com/video/267/
# code: https://www.acwing.com/activity/content/code/content/689552/

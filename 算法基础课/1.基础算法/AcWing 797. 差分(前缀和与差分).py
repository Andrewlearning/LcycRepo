"""
存在一个数组 a1,a2,a3,a4..,an
构造 b1,b2,b3,b4,b5...
使得 ai = b1 + b2 + b3 +...+ bi

b1 = a1
b2 = a2 - a1
b3 = a3 - a2
...
bn = an - an-1

这样b数组称为a数组的差分数组，a数组是b数组的前缀和

差分数组有什么用呢？
1. 假如我们有b数组了，那么对b数组求一遍前缀和，那么就能得到a数组了， O(n) b -> a
2. 假如我们想给a数组的[l,r]的每个元素都加上一个 c，正常操作遍历加一遍是 O(n)
    假如使用差分数组的话，我们把bl = bl + c, 那么al,al+1,al+2..都自动加上c了
    然后是[l,r]这个范围内都+c, 所以就是到br+1 的时候， br+1 = br+1 - c
    所以这里只用修改两个数就可以了，时间复杂度降为O(1)
"""


def insert(l, r, c):
    b[l] += c
    b[r + 1] -= c


if __name__ == "__main__":
    n, rounds = list(map(int, input().split(" ")))
    a = [0] * (n + 2)
    b = [0] * (n + 2)

    # 构造数组a
    get = list(map(int, input().split(" ")))
    for i in range(1, n + 1):
        a[i] = get[i - 1]

    # 构造数组差分数组b
    for i in range(1, n + 1):
        insert(i, i, a[i])

    for _ in range(rounds):
        l, r, c = list(map(int, input().split(" ")))
        insert(l, r, c)

    # 利用新b重新构造数组a
    for i in range(1, n + 1):
        b[i] += b[i - 1]

    print(" ".join(map(str, b[1:-1])))


# https://www.acwing.com/video/242/
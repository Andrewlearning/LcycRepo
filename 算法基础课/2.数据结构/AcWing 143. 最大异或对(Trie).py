"""

异或被称为不进位加法
110110
001101
------
111011

"""


def insert(x):
    global idx
    # p代表的是节点的位置
    p = 0

    for i in range(31, -1, -1):
        # u代表第i位是0还是1
        u = x >> i & 1

        # 假如在第p个节点没有u这个分支，那么则添加上
        if not son[p][u]:
            idx += 1
            son[p][u] = idx

        # 移动到下一个节点
        p = son[p][u]


def query(x):
    p = 0
    res = 0

    for i in range(31, -1, -1):
        # u代表第i位是0还是1
        u = x >> i & 1

        # 假如当前节点的相反位置节点存在，那么说明可以在这种情况异或能得到1
        if son[p][u ^ 1]:
            # 那么说明第i位，经过异或是能得到一个1的，所以加到结果
            res += 1 << i
            p = son[p][u ^ 1]
        # 否则说明相反位置节点不存在，所以没办法，只能选择u了
        else:
            p = son[p][u]

    return res


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    N = 100010
    M = 30 * N
    son = [[0, 0] for _ in range(M)]
    a = [0] * N

    # 当前在第几层
    idx = 0
    # 最终结果
    res = 0

    for num in nums:
        insert(num)
        res = max(query(num), res)

    print(res)

# 思路https://www.acwing.com/video/249/
# 代码https://www.acwing.com/activity/content/code/content/154340/

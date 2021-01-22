"""
并查集：
1.讲两个集合合并
2.询问两个元素是否在一个集合中
并查集可以在近乎O(1)的时间内完成上述两个操作

基本原理：
每一个集合用一棵树来表示，树根的编号就是整个集合的编号
每个节点都指向他的父节点，p[x] 表示x的父节点

问题一：如何判断树根
if p[x] == x

问题二：如何求x的集合编号:
while p[x] != x:
    x = p[x]

问题：假如是一个链表的形状，那么找到根节点时间复杂度很高
路径压缩优化：
当找到根节点以后，直接把这棵树的所有节点都指向顶点
（加上这个优化以后，并查集的时间复杂度基本降成O(1)）


问题三：
px 是 x的集合编号，py是y的集合编号
然后直接让某一树的根节点练到另一个树的根节点就好了
p[x] = y
"""


def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])
    return uf[x]


def query(x, y):
    return find(x) == find(y)


def merge(x, y):
    uf[find(x)] = find(y)


if __name__ == "__main__":

    n, m = map(int, input().split())
    ops = []
    for i in range(m):
        ops.append(list(input().split()))

    uf = [i for i in range(n + 1)]

    for op, x, y in ops:
        x, y = int(x), int(y)
        if op == "M":
            merge(x, y)
        elif op == "Q" and query(x, y):
            print("Yes")
        else:
            print("No")

# https://www.acwing.com/video/261/


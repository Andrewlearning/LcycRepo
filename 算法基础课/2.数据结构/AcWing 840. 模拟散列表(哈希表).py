"""
哈希表的存储结构：
1.开放寻址法
2.拉链法

字符串哈希方式

"""

import sys


def insert(x):
    global idx
    hashcode = x % N
    # 上一个idx已经被用过，我们这里开一个新的值
    idx += 1

    # 记录新节点的值
    nodeValue[idx] = x

    # 把当前节点的 -> 在hashmap槽上的那个元素
    nodeNext[idx] = hashmap[hashcode]
    # 更新hashmap的槽为当前元素(idx)
    hashmap[hashcode] = idx


def query(x):
    hashcode = x % N

    # 在hashmap槽上的元素，他是这个链表的头结点
    parent = hashmap[hashcode]

    # 当没走到空指针的时候，就一直找
    while parent != -1:
        # 找到了等于x的元素，返回True
        if nodeValue[parent] == x:
            return True
        # 否则则继续找
        parent = nodeNext[parent]

    return False


if __name__ == "__main__":

    n = int(input())

    # 取大于1e5的第一个质数，取质数冲突的概率最小 可以百度
    N = int(1e5 + 3)
    # 每个节点的坐标
    idx = 0
    # 哈希表, 槽指向空指针的时候，我们设定为-1
    hashmap = [-1] * N
    # 哈希表上节点所指向的下一个节点的idx
    nodeNext = [0] * N
    # 每个被insert元素的值
    nodeValue = [0] * N

    for _ in range(n):
        line = list(sys.stdin.readline().strip().split())
        x = int(line[1])
        op = line[0]

        if op == "I":
            insert(x)
        else:
            if query(x):
                print('Yes')
            else:
                print('No')

# idea: https://www.acwing.com/video/266/
# https://www.acwing.com/activity/content/code/content/154519/

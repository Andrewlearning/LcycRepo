"""
单链表最常用的用途是做邻接表：存储树 和 图
双链表最常用的用途是：优化某些问题

在这里是用数组去模拟链表，而不是用class相连
"""

# 把值为x的节点插在链表的头部
def insert_head(x):
    global idx, head
    # 给idx位的节点赋值为x
    nodeValue[idx] = x
    # 给idx位的节点的指向为head， idx -> 之前的head
    nodeNext[idx] = head
    # idx(head) -> 之前的head
    head = idx
    # 把idx移动到下一个位置去
    idx += 1


def delete(k):
    # k -> k.next -> k.next.next
    # k -> k.next.next
    nodeNext[k] = nodeNext[nodeNext[k]]


def insert(k, x):
    global idx
    nodeValue[idx] = x
    # idx -> k.next
    nodeNext[idx] = nodeNext[k]
    # k -> idx -> k.next
    nodeNext[k] = idx
    idx += 1


if __name__ == '__main__':

    N = 100000
    n = int(input())

    nodeValue = [0] * N
    nodeNext = [0] * N

    # idx代表当前节点的位置
    idx = 0
    head = -1

    for i in range(n):
        line = input().split()
        op = line[0]
        
        if op == 'H':
            insert_head(int(line[1]))
        elif op == 'I':
            insert(int(line[1]) - 1, int(line[2]))
        else:
            k = int(line[1])
            if k:
                delete(k - 1)
            else:
                head = nodeNext[head]

    p = head
    res = []
    while p != -1:
        res.append(nodeValue[p])
        p = nodeNext[p]

    print(" ".join(map(str, res)))

# https://www.acwing.com/activity/content/code/content/154134/

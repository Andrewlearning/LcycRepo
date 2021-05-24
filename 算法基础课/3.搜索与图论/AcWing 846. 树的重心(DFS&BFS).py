def add(a, b):
    global idx
    e[idx] = b  # 新加进来b这个元素，他的对应指针是idx
    ne[idx] = head[a]  # b -> a -> ...
    head[a] = idx  # 以a为首的链表的串的头结点是b
    idx += 1  # 更新指针的坐标

def dfs(u):

    size = 0

    memo[u] = 1

    sum = 0

    i = head[u]
    while i != -1:
        iVal = e[i]
        if memo[iVal] != 0:
            nextSum = dfs[iVal]
            size = max(size, nextSum)
            sum += nextSum
        i = ne[i]

    size = max(size, n - sum - 1)
    return sum + 1


if __name__ == '__main__':
    N = 100010
    idx = 0 # 类似一个节点的地址
    head = [-1] * N  # 记录每个链表的头结点
    e = [0] * (2 * N)  # 记录当前节点的值[idx] = x
    ne = [0] * (2 * N) # 记录当前节点所指向的节点的指针[idx] = next idx
    memo = [0] * N # 记录当前节点有没有被遍历过

    n = int(input())

    for _ in range(n-1):
        a,b = map(int, input().split())
        add(a, b) # 由于树是无向图，所以每个节点两头都要连接上
        add(b, a)




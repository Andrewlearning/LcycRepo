"""
Trie: 高效存储和查找字符串集合的数据结构
"""

N = int(1e5 + 5)

# son[N][26]
# N代表是有一个一串字符串最多有多少元素
# 26表示这个元素有多少条分支
# son[x][y] 表示的是这个节点指向的下一个节点的位置
son = [[0 for i in range(26)] for i in range(N)]

# 表示在从son[0][0] 到 son[x][y]这一串字符串出现了多少次
# 例如 abc ab, 只看"ab"的话就是出现了两次
cnt = [0 for i in range(N)]

# 用于铆钉节点位置的变量
index = 0


def insert(x):
    global index
    # trie的开始
    p = 0

    # 遍历单词的每个字母
    for i in range(len(x)):
        # 每个字母相对于a的偏移量
        t = ord(x[i]) - ord('a')

        # 看要去的位置，之前有没被记录过
        # 假如没记录过，则做上记录
        if not son[p][t]:
            index += 1
            son[p][t] = index

        # 然后更新下一次要去的位置
        p = son[p][t]

    # 当前前缀的出现次数+1
    cnt[p] += 1


def query(x):
    p = 0

    for i in range(len(x)):
        t = ord(x[i]) - ord('a')
        # 假如说找不到当前前缀，说明没有对应单词，返回0个
        if not son[p][t]:
            return 0
        # 假如有当前前缀，则继续往下找
        p = son[p][t]

    # 返回存在多少个单词
    return cnt[p]


n = int(input())
while n:
    n -= 1
    t = input().split()
    op = t[0]
    s = t[1]

    if op == 'I':
        insert(s)
    else:
        res = query(s)
        print(res)

# 作者：chaos8032
# 链接：https://www.acwing.com/activity/content/code/content/182925/
# 来源：AcWing
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
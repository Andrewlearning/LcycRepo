"""

二维差分是，给一个子矩阵加上一个值

存在一个子矩阵的左上角坐标x1,y1 右下角坐标x2,y2
那么 b[x1][y1] += c
那么 b[x2+1][y2] -= c
    b[x2][y2+1] -= c
    b[x2+1][x2+1] += c


"""


def insert(x1, y1, x2, y2, c):
    b[x1][y1] += c
    b[x2 + 1][y1] -= c
    b[x1][y2 + 1] -= c
    b[x2 + 1][y2 + 1] += c


if __name__ == "__main__":
    # 2.获取n, m, q
    n, m, q = map(int, input().split())

    # 3.初始化原矩阵和差分矩阵
    a = [[0] * (m + 2) for i in range(n + 2)]
    b = [[0] * (m + 2) for i in range(n + 2)]

    # 4.将元素放入原始矩阵中
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, m + 1):
            a[i][j] = row[j - 1]

    # 5.将原始矩阵插入差分矩阵中
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insert(i, j, i, j, a[i][j])

    # 6.按照坐标区间插入新元素
    for i in range(q):
        x1, y1, x2, y2, c = map(int, input().split())
        insert(x1, y1, x2, y2, c)

    # 7.求出前缀和矩阵s重新赋值到b上
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            b[i][j] += b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]

    # 8.输出差分矩阵的前缀矩阵
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(b[i][j], end=' ')
        print()

# 作者：Savage_Garden
# 链接：https://www.acwing.com/activity/content/code/content/115048/
# video: https://www.acwing.com/video/244/


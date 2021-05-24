import collections
from collections import deque


def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return "".join(s)


def dfs(start):
    queue = deque([])
    distance = collections.defaultdict(int)

    # 用一个二维数组作为一个状态储存太过麻烦
    # 所以我们把这个二维数组转换成一个一纬的字符串进行储存
    end = "12345678x"
    # 初始化从起点到起点的距离为0
    distance[start] = 0
    queue.append(start)

    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:

        cur = queue.popleft()

        # 找到答案了,返回从开始到目前的距离
        if cur == end:
            return distance[cur]

        # 没找到答案，则要把x在上下左右进行移动
        k = cur.index("x")
        mappedi = k // 3
        mappedj = k % 3

        curDict = distance[cur]

        for di, dj in dxy:
            newi = mappedi + di
            newj = mappedj + dj

            # 把变化后合法的pattern存进queue, 等下一次pop出来后再检验
            if 0 <= newi < 3 and 0 <= newj < 3:
                # 先修改
                cur = swap(cur, k, newi * 3 + newj)

                if cur not in distance:
                    distance[cur] = curDict + 1
                    queue.append(cur)

                # 处理完后回溯
                cur = swap(cur, k, newi * 3 + newj)

    return -1


if __name__ == "__main__":
    start = "".join(input().split())
    print(dfs(start))

# Time O(N^2) Space O(N^2)
# https://www.acwing.com/video/277/
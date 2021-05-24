"""
给定一个n*m的二维整数数组，用来表示一个迷宫，数组中只包含0或1，
其中0表示可以走的路，1表示不可通过的墙壁。

最初，有一个人位于左上角(1, 1)处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。
请问，该人从左上角移动至右下角(n, m)处，至少需要移动多少次。（最短路径问题）
数据保证(1, 1)处和(n, m)处的数字为0，且一定至少存在一条通路。

BFS只能处理边权重为1的最短路径问题
最短路径问题一般都是使用DP来做的

模板：
init queue

while queue:
    t = queue[0]
    扩展t
    
"""
def bfs():
    queue = []
    queue.append([0, 0])

    idx = [-1, 1, 0, 0]
    idy = [0, 0, -1, 1]
    memo[0][0] = 0
    while queue:
        cur = queue.pop(0)
        for i in range(4):
            x = cur[0] + idx[i]
            y = cur[1] + idy[i]
            if 0 <= x < n and 0 <= y < m and not maze[x][y] and memo[x][y] == -1:
                queue.append([x, y])
                memo[x][y] = memo[cur[0]][cur[1]] + 1

    return memo[-1][-1]


if __name__ == '__main__':
    n, m = map(int, input().split())

    maze = []
    for _ in range(n):
        line = list(map(int, input().split()))
        maze.append(line)

    memo = [[-1] * m for _ in range(n)]

    steps = 0

    print(bfs())

# https://www.acwing.com/video/276/
# code https://www.acwing.com/activity/content/code/content/154670/

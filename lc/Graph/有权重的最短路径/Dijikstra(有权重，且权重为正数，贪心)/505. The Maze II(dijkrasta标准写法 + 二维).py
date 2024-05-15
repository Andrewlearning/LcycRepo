"""
来这做: https://www.lintcode.com/problem/788/
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1:
	Input:
	(rowStart, colStart) = (0,4)
	(rowDest, colDest)= (4,4)
	0 0 1 0 (0)
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 (0)

	Output:  12
	Explanation:
	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)
"""

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param target: the target
    @return: the shortest distance for the ball to stop at the target
    """

    def shortest_distance(self, maze, start, target):
        # 初始化起点到地图里每一个节点的距离，一开始都为正无穷，后面慢慢更新
        distance = [[float("inf")] * len(maze[0]) for _ in range(len(maze))]
        # 初始化起点到起点的距离为0
        distance[start[0]][start[1]] = 0

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        h = [(0, start[0], start[1])]

        while h:
            d1, i, j = heah.heappop(h)

            # 这里我们不设置找到终点就返回，是因为有可能最先到终点的，不是最优解。
            # 剪枝，去掉可通过lintcode
            # if distance[i][j] < d1:
            #     continue

            # 每次小球可以往四个方向滚
            for di, dj in dirs:
                ni = i
                nj = j

                d2 = 0
                # 球往一个方向滚，知道砖撞墙为止，并且记录移动的距离
                while 0 <= ni + di < len(maze) and 0 <= nj + dj < len(maze[0]) and maze[ni + di][nj + dj] == 0:
                    ni += di
                    nj += dj
                    d2 += 1

                # 假如我们当前走的路线，优于，之前走到这个点的路线，那么我们则选用当前路线
                if distance[i][j] + d2 < distance[ni][nj]:
                    # 更新从起点到这个点的最短距离
                    distance[ni][nj] = distance[i][j] + d2
                    heah.heappush(h, (distance[ni][nj], ni, nj))

        if distance[target[0]][target[1]] == float("inf"):
            return -1
        return distance[target[0]][target[1]]

"""
时间复杂度
    构建图的时间复杂度为 O(E)
    最小堆操作(包括初始化和每次弹出、插入)的时间复杂度总和为 O(ElogV)
    - 因为每条边最多只会被松弛一次，因此总的松弛操作次数为E，每次操作的时间复杂度为O(logV).
        - 松弛(relaxation): 松弛操作的目的是通过检查和更新路径长度，从而找到从起点到所有其他节点的最短路径

空间复杂度
    存储图的邻接表'graph'需要 O(E)的空间。
    存储visited数组需要 O(V)的空间。
    最小堆的空间复杂度在最坏情况下为 O(V)。
    因此，总的空间复杂度为 - O(V+E)

古城算法 38:00
https://www.bilibili.com/video/BV1Rz4j1Z7tJ/?spm_id_from=333.337.search-card.all.click&vd_source=b81616a45fd239becaebfee25e0dbd35
"""
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param target: the target
    @return: the shortest distance for the ball to stop at the target
    """

    def shortest_distance(self, maze, start, target):
        #
        distance = [[float("inf")] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0
        self.dijkstra(maze, start, target, distance)
        return -1 if distance[target[0]][target[1]] == float("inf") else distance[target[0]][
            target[1]]

    def dijkstra(self, maze, start, target, distance):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        pq = [(0, start[0], start[1])]
        
        while pq:
            curDist, i, j = heapq.heappop(pq)
            
            # 这里我们不设置找到终点就返回，是因为有可能最先到终点的，不是最优解。
            if distance[i][j] < curDist:
                continue

            for di, dj in dirs:
                ni = i
                nj = j
                count = 0
                while 0 <= ni + di < len(maze) and 0 <= nj + dj < len(maze[0]) and maze[ni + di][nj + dj] == 0:
                    ni += di
                    nj += dj
                    count += 1

                # 假如我们当前走的路线，优于，之前走到这个点的路线，那么我们则选用当前路线
                if distance[i][j] + count < distance[ni][nj]:
                    distance[ni][nj] = distance[i][j] + count
                    heapq.heappush(pq, (distance[ni][nj], ni, nj))

"""
古城算法 38:00
https://www.bilibili.com/video/BV1Rz4j1Z7tJ/?spm_id_from=333.337.search-card.all.click&vd_source=b81616a45fd239becaebfee25e0dbd35
"""
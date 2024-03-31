"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        self.dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.lr = len(matrix)
        self.lc = len(matrix[0])
        dist = [[-1] * self.lc for _ in range(self.lr)]

        queue = []
        for i in range(self.lr):
            for j in range(self.lc):
                # 我们先把所有0的节点放进queue,然后从每个0节点开始向外面扩散
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append([i,j])


        while queue:
            x, y = queue.pop(0)

            for dir in self.dirs:
                nx = x + dir[0]
                ny = y + dir[1]
                # dist[nx][ny] == -1 只扩散未去过的节点
                if 0 <= nx < self.lr and 0 <= ny < self.lc and dist[nx][ny] == -1:
                    # 往非0节点扩散
                    # 先扩散0节点周围的，那么他们距离0的距离就是 0+1
                    # 然后再扩散距离0为1的点，那么这些点扩散出去的距离就是2
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])

        return dist

"""
时间复杂度：O(rc)，其中 r 为矩阵行数，c 为矩阵列数，即矩阵元素个数。广度优先搜索中每个位置最多只会被加入队列一次，因此只需要 O(rc) 的时间复杂度。

空间复杂度：O(rc)，其中 r 为矩阵行数，c 为矩阵列数，即矩阵元素个数。除答案数组外，最坏情况下矩阵里所有元素都为 0，全部被加入队列中，此时需要 O(rc) 的空间复杂度。
"""




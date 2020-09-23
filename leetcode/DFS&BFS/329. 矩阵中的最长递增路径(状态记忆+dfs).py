class Solution(object):
    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix and len(matrix) == 0:
            return 0

        self.lr = len(matrix)
        self.lc = len(matrix[0])
        dp = [[0] * self.lc for i in range(self.lr)]
        maxlen = 1

        for i in range(self.lr):
            for j in range(self.lc):
                temp_len = self.dfs(matrix, i, j, dp)
                if temp_len > maxlen:
                    maxlen = temp_len
        return maxlen

    def dfs(self, matrix, i, j, dp):
        if dp[i][j] != 0:
            return dp[i][j]

        # 假如没从当前节点出发过，那么最大的初始长度是1
        maxlen = 1

        for dir in self.dirs:
            x = i + dir[0]
            y = j + dir[1]
            if x < 0 or x >= self.lr or y < 0 or y >= self.lc or matrix[x][y] <= matrix[i][j]:
                continue

            # 当前节点的长度，等于周围四个点的最大长度 加上当前的长度
            length = 1 + self.dfs(matrix, x, y, dp)
            maxlen = max(maxlen, length)

        # 记录当前节点的最大长度
        dp[i][j] = maxlen
        return maxlen
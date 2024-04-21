"""
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；(死细胞也不会变生)
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board and len(board) == 0:
            return

        lrow = len(board)
        lcol = len(board[0])

        for i in range(lrow):
            for j in range(lcol):
                lives = self.countLive(board, i, j)
                if board[i][j] == 0:
                    # [i][j]是死细胞，且周围只有三个细胞存活，所以变活0 -> -1
                    if lives == 3:
                        board[i][j] = -1
                elif board[i][j] == 1:
                    # [i][j]活细胞，且周围有<2 或 >3 个细胞存活，所以变死1 -> 2
                    if lives < 2 or lives > 3:
                        board[i][j] = 2

        self.update(board)

    # 更新规则
    # update(): -1=>1, 2=>0
    def update(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0

    def countLive(self, board, i, j):
        res = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == dj == 0:
                    continue
                newi = di + i
                newj = dj + j
                # 这里1表示这回合还活着的细胞
                # 2表示这回合还活着，但是下回合要死的细胞
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]) and board[newi][newj] in [1, 2]:
                    res += 1

        return res


"""
youtube.com/watch?v=9AsUixzUGa0
"""

# 做法和上面一样，不过这样写比较生位置
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        def count(i, j):
            res = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ni = i + di
                    nj = j + dj
                    if di == 0 and dj == 0:
                        continue
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] in [1, -2]:
                        res += 1
            return res

        for i in range(n):
            for j in range(m):
                c = count(i, j)
                # print(c)
                val = board[i][j]
                # 本轮死，下一轮是活的标记成-1
                if val == 0 and c == 3:
                    board[i][j] = -1
                if val == 1:
                    # 本轮活，下一轮死的标记成-2
                    if c < 2 or c > 3:
                        board[i][j] = -2

        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == -2:
                    board[i][j] = 0
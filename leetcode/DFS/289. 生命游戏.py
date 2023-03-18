class Solution(object):
    def __init__(self):
        self.dirs = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]


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

                if board[i][j] == 0:
                    lives = self.count(board, i, j)
                    # 是死细胞，且周围只有三个细胞存活，所以变活0 ->- 1
                    if lives == 3:
                        board[i][j] = -1

                if board[i][j] == 1:
                    lives = self.count(board, i, j)
                    # 是活细胞，且周围有2-3个细胞存活，所以变死 1->2
                    if lives < 2 or lives > 3:
                        board[i][j] = 2

        self.update(board)
    #
    # 更新规则
    # mark die -> live:-1
    # mark live -> die: 2
    # update(): -1=>1, 2=>0
    def update(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0

    def count(self, board, i, j):
        res = 0
        for dir in self.dirs:
            newi = dir[0] + i
            newj = dir[1] + j
            # 这里1表示这回合还活着的细胞
            # 2表示这回合还活着，但是下回合要死的细胞
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]) and (board[newi][newj] == 1 or board[newi][newj] == 2):
                res += 1

        return res


"""
youtube.com/watch?v=9AsUixzUGa0

"""
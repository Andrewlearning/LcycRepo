"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。
空白格用'.'表示。
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0:
            return
        self.solve(board)
        return board

    def solve(self, board):
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 说明当前这个位置可以填数
                if board[i][j] == ".":
                    # 我们可以选择1-9往里面填
                    for c in nums:

                        # 假如填这个数进去没有问题的话， 那么我们就要真正的赋值
                        if self.isvalid(board, i, j, c):
                            board[i][j] = c
                            # 然后继续探索别的位置。如果剩下的位置全部没问题的话，则返回True(回溯)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    # 假如说这个位置我们尝试了9个数字都不行，那么则返回false
                    return False
        # 假如没有任何异常，那么返回True
        return True

    def isvalid(self, board, row, col, num):
        for i in range(9):
            # 检查在竖直方向有没有重复数字，有的话返回false
            if i != row and board[i][col] == num:
                return False

            # 检查在水平方向有没有重复数字，有的话返回false
            if i != col and board[row][i] == num:
                return False

            # 检查在以[row,col]为中心的九宫格内，是否有重复数字，有的话返回false
            nrow = 3 * (row // 3) + i // 3
            ncol = 3 * (col // 3) + i % 3
            if nrow != row and ncol != col and board[nrow][ncol] == num:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku(
        [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
         ["2", ".", ".", ".", ".", ".", ".", ".", "."],
         ["3", ".", ".", ".", ".", ".", ".", ".", "."],
         ["4", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", ".", "."],
         ["6", ".", ".", ".", ".", ".", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
    ))
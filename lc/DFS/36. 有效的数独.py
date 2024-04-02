"""
请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）


注意：

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用'.'表示。
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) == 0:
            return
        return self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                else:
                    if self.isvalid(board, i, j, board[i][j]):
                        continue
                    return False
        return True

    def isvalid(self, board, row, col, num):
        for i in range(9):
            # 假如在水平或者竖直方向有和num相等的数字，那么这个数独无效
            if board[i][col] == num and i != row:
                return False
            if board[row][i] == num and i != col:
                return False

            # 以[row, col]为中心的九宫格内，假如有与num相同数字的话，那么九宫格无效
            if (3 * (row // 3) + i // 3) == row and 3 * (col // 3) + i % 3 == col:
                continue
            else:
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
        return True


"""
作为求解数独的简单版，我们只要检查数独中的数字是否满足数独的规定就好了
"""

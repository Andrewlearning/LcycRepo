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
        nrow = len(board)
        ncol = len(board[0])

        for i in range(nrow):
            for j in range(ncol):
                val = board[i][j]
                if val == ".":
                    continue
                else:
                    res = self.helper(board, i, j, val)
                    if res == False:
                        return False

        return True

    def isvalid(self, board, row, col, num):
        for i in range(9):
            # 假如在水平或者竖直方向有和num相等的数字，那么这个数独无效
            if board[i][col] == num and i != row:
                return False
            if board[row][i] == num and i != col:
                return False

            """
                以画线出来的九宫格内，假如有与num相同数字的话，那么说明数独无法成立
                九宫格的起点都是左上角，例如, 下面这些点的起点就是都属于同一个九宫格内
                [0,0] [0,1] [0,2]
                [1,0] [1,1] [1,2]
                [2,0] [1,1] [2,2]
                遵循下面 nrow, ncol的规律
            """

            nrow = 3 * (row // 3) + i // 3
            ncol = 3 * (col // 3) + i % 3
            if nrow != row and ncol != col and board[nrow][ncol] == num:
                return False
        return True


"""
作为求解数独的简单版，我们只要检查数独中的数字是否满足数独的规定就好了
"""

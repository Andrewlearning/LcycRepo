"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
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
        nums = ["1","2","3","4","5","6","7","8","9"]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 说明当前这个位置可以填数
                if board[i][j] == ".":
                    # 我们可以选择1-9往里面填
                    for c in nums:

                        # 假如填这个数进去没有问题的话， 那么我们就要真正的赋值
                        if self.isvalid(board,i,j,c):
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
    		if i != row and board[i][col] == num:
    			return False

    		if i != col and board[row][i] == num:
    			return False

    		new_row = 3*(row//3) + i//3
    		new_col = 3*(col//3) + i%3
    		if new_row != row and new_col != col and board[new_row][new_col] == num:
    			return False

    	return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku(
        [[".","8","7","6","5","4","3","2","1"],
         ["2",".",".",".",".",".",".",".","."],
         ["3",".",".",".",".",".",".",".","."],
         ["4",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".",".","."],
         ["6",".",".",".",".",".",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         ["8",".",".",".",".",".",".",".","."],
         ["9",".",".",".",".",".",".",".","."]]
 ))

"""
https://www.youtube.com/watch?v=2FV8tgBCYqI&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=34
作为求解数独的复杂版，我们要在空格处填满所需要的字符
1。遍历每个节点
2。创立一个1-9的list，我们需要用这九个数字"。"里套，看哪个数字可以用
3。当节点为"。"的时候我们开始套1-9，同时检查"。"套进一个数字 c 后，是否符合数独规则
4。在 isvalid（）里面检查套进的元素c，是否满足横，竖，九宫格无相同
5。当前情况没问题后，就把c 放在[i][j]上
6。递归，再调用一次solve（），在c被放置的基础上，继续放置别的元素，重复1-5的循环

7.假如一直放置都很成功，递归到头，重重回调，return True
8.假如在途中有c 放置不成功的，solve（）return false,那么我们要把上一个递归的[i][j]给还原成"。"，然后再尝试别的
c

9。假如说一切顺利结束，return true。
假如说一路不顺利，那么在第一次递归的时候就会失败，返回false.第一个递归返回false.就意味着整个程序返回false
失败



注意：这里利用了修枝，当循环进入到有。的时候，我们直接跳过，节省了时间
"""
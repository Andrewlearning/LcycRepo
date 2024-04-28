class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.lr = len(board)
        self.lc = len(board[0])
        self.v = [[False for j in range(self.lc)] for i in range(self.lr)]


        # 第一次遍历，只遍历与四条边界相连的O, 我们遍历一遍只为了记录到visted中
        # 为的是下次翻转遍历的时候，不翻转这些
        for i in range(self.lr):
            for j in range(self.lc):
                if (i in [0, self.lr - 1] or j in [0, self.lc - 1]) and board[i][j] == "O":
                    self.dfs(board, i, j, False)

        # fipe the tile on the middle
        for i in range(1, self.lr - 1):
            for j in range(1, self.lc - 1):
                if board[i][j] == "O" and self.v[i][j] == False:
                    self.dfs(board,i,j,True)



    def dfs(self, board, i, j, flip):
        if i < 0 or i > self.lr - 1 or j < 0 or j > self.lc - 1:
            return
        if board[i][j] == "X":
            return
        if self.v[i][j]:
            return

        if flip: board[i][j] = "X"

        self.v[i][j] = True
        self.dfs(board, i + 1, j, flip)
        self.dfs(board, i - 1, j, flip)
        self.dfs(board, i, j + 1, flip)
        self.dfs(board, i, j - 1, flip)

"""
https://www.youtube.com/watch?v=u0Xtggq0n10
答案：
思路其实挺简单的
1.谁不能被翻。四条边上的0,因为总有一面是围不上的，所以与最外围边0相连的0，都不可能被翻的
2.谁可以被翻。不在四条边上，且，没有与边上O相连的 O，可以被翻
3.dfs，我们要给它一个定性
  
  3.1 flip是从主函数传过来的，他也是会贯穿一整串dfs,例如是四周的O，那么，凡事四周O能
      连接到的O，flip都是false
      于此同时，走过的点，在dfs里会在self.v里标记成True
      所以，一个点，在第一次遍历的时候，就决定了它翻不翻，以及，不能再遍历
  
  3.2 对于要翻的点也是一样，只有一次遍历，一次翻的机会
"""
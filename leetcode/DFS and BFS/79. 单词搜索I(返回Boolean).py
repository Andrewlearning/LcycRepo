"""
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.res = False
        self.lr = len(board)
        self.lc = len(board[0])
        self.visited = [[False] * self.lc for _ in range(self.lr)]

        for i in range(self.lr):
            for j in range(self.lc):
                if board[i][j] == word[0]:
                    if self.helper(board, word, i, j, 0):
                        return True

        return False

    def helper(self, board, word, i, j, index):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= self.lr or j >= self.lc or index > len(word) or self.visited[i][j] == True or \
                board[i][j] != word[index]:
            return False

        self.visited[i][j] = True

        res = self.helper(board, word, i + 1, j, index + 1) \
              or self.helper(board, word, i - 1, j, index + 1, ) \
              or self.helper(board, word, i, j + 1, index + 1, ) \
              or self.helper(board, word, i, j - 1, index + 1, )

        self.visited[i][j] = False

        return res

"""

答案：
1.visited是用来记录当前这个点在本次查找中是否被访问过，如果被访问过
则为True,没有则是False
2.然后剩下的就没啥难的，无非是所有节点遍历，然后DFS
3.helper函数注意要传一个index
3.在index越界，或者word[index]和word[i][j]不同时，返回False
4.判断没问题，就把visited[i][j] == True, 然后dfs, dfs完后visited[i][j] == False
"""
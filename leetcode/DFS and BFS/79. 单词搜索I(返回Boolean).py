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
        if not board:
            return False

        self.lr = len(board)
        self.lc = len(board[0])
        self.visited = []
        self.res = False

        for i in range(self.lr):
            for j in range(self.lc):
                if board[i][j] == word[0]:
                    if self.helper(board, word, 0, i, j):
                        self.res = True

        return self.res

    def helper(self, board, word, index, i, j):
        if i < 0 or j < 0 or i >= self.lr or j >= self.lc or [i, j] in self.visited or index >= len(word) or board[i][
            j] != word[index]:
            return False

        if index == len(word) - 1:
            return True

        self.visited.append([i, j])

        res = self.helper(board, word, index + 1, i + 1, j) \
              or self.helper(board, word, index + 1, i - 1, j) \
              or self.helper(board, word, index + 1, i, j + 1) \
              or self.helper(board, word, index + 1, i, j - 1)

        self.visited.pop(-1)
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
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
        self.visited = []
        self.word = word
        self.board = board
        self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(i, j, 0):
                    return True

        return False

    def helper(self, i, j, index):
        if self.board[i][j] != self.word[index]:
            return False

        if len(self.word) - 1 == index:
            return True

        self.visited.append([i, j])

        for dir in self.dirs:
            ni = i + dir[0]
            nj = j + dir[1]
            if 0 <= ni < len(self.board) and 0 <= nj < len(self.board[0]) and [ni, nj] not in self.visited:
                if self.helper(ni, nj, index + 1):
                    return True

        self.visited.pop(-1)

"""

答案：
1.visited是用来记录当前这个点在本次查找中是否被访问过，如果被访问过
则为True,没有则是False
2.然后剩下的就没啥难的，无非是所有节点遍历，然后DFS
3.helper函数注意要传一个index
3.在index越界，或者word[index]和word[i][j]不同时，返回False
4.判断没问题，就把visited[i][j] == True, 然后dfs, dfs完后visited[i][j] == False
"""
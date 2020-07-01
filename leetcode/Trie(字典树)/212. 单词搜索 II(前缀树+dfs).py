"""
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
"""

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            node = trie

            # 针对每个单词，构造它的字典树
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]

            # 每储存完一个单词，就给最后加上一个标志
            node["#"] = True



        # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
        def helper(i, j, node, pre, visited):
            # 说明已经走完了一个单词
            if "#" in node:
                res.add(pre)

            for (x, y) in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_i = i + x
                new_j = j + y

                # 当满足所有条件的时候，我们可以把元素加进去
                if -1 < new_i < len(board) and -1 < new_j < len(board[0]) and board[new_i][new_j] in node and (
                new_i, new_j) not in visited:
                    helper(new_i, new_j, node[board[new_i][new_j]], pre + board[new_i][new_j],
                           visited + [(new_i, new_j)])



        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    helper(i, j, trie[board[i][j]], board[i][j], [(i, j)])

        return list(res)

# https://leetcode-cn.com/problems/word-search-ii/solution/pythonzi-dian-shu-dfs-by-mai-mai-mai-mai-zi/
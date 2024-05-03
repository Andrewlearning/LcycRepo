"""
给定一个二维网格board和一个字典中的单词列表 words，找出所有同时在二维网格board和字典words中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出:["eat","oath"]
"""

class Solution:
    def findWords(self, board, words):
        trie = {}

        for word in words:
            node = trie

            # 针对每个单词，构造它的字典树
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            # 遍历完成后，存的是整个单词
            node["finish"] = word

        self.n = len(board)
        self.m = len(board[0])

        self.res = []
        for i in range(self.n):
            for j in range(self.m):
                self.dfs(i, j, trie, board)

        return self.res

    def dfs(self, i, j, node, board):
        if not (0 <= i < self.n) or not (0 <= j < self.m) or board[i][j] == "#" or board[i][j] not in node:
            return
        """
        1.
        一个单词的最后一个字母的子节点只有{finish:word}了
        假如已经遍历到一个单词的最后一个字母了, pop则返回这个单词, 并记录这个单词
        假如没有遍历到一个单词的最后一个字母，pop则返回默认值False
        题目潜在假设，一个单词在一个表只能被找到一次，所以我们把这个单词找到后，pop掉单词
        dict.pop(key, default)的用途是，假如dict有这个key，那么则返回value并清除这个key-value, 否则则返回default， 与get有点相似
        例如 {a:{b:{finish:ab}}} -> {a:{b:{}}}, 然后在下面2处进行清理
        """
        cur = board[i][j]
        isLast = node[cur].pop("finish", False)
        if isLast:
            self.res.append(isLast)

        # 本次dfs遍历过这个点，标记，在本单词的遍历中不会再被访问
        # 同位置在同一个单词里不能经过两次，但是同位置在不同单词是可以被使用两次的
        board[i][j] = "#"
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            newi = i + x
            newj = j + y
            self.dfs(newi, newj, node[cur], board)

        # 本次dfs遍历完成，解除标记，在下个dfs会被再使用
        board[i][j] = cur

        """
        2. 重要优化，加上在碰到极端case能快接近十倍 
        假如存在形如这种的trie, 则把b:{}给pop掉，以减少下次查询的长度
        {a:{b:{}}} -> {a:{}}
        """
        if node[cur] == {}:
            node.pop(cur)

# 链接：https://leetcode.cn/problems/word-search-ii/solution/python3-dfs-by-trojanmaster-7zmx/
# 古城算法的超时了
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        # #为结束标志
        node["#"] = "#"

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.trie

        def dfs(tree, word):
            node = tree

            for i, char in enumerate(word):

                # 本题的难点在这里，就是我们遇到"." 应该要怎么去处理
                # 答案是，把本层，除了"." 以外的节点，都全部找一遍
                if char == ".":
                    return any(dfs(node[j], word[i + 1:]) for j in node if j != "#")
                elif char not in node:
                    return False
                node = node[char]

            return "#" in node

        return dfs(node, word)

# https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/solution/211-tian-jia-yu-sou-suo-dan-ci-shu-ju-jie-gou-she-/
class WordDictionary(object):
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = {}

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.trie, 0, word)

    def dfs(self, node, pos, word):
        if pos == len(word):
            return "#" in node

        char = word[pos]

        # char 不为 ".", 则正常遍历
        if char != ".":
            return char in node and self.dfs(node[char], pos + 1, word)

        # char 为".", 则遍历当前node下非"."的所有char
        for char in node:
            if char in node and self.dfs(node[char], pos + 1, word):
                return True

        return False

# 古城算法: https://www.youtube.com/watch?v=qU3SbJHb7o8
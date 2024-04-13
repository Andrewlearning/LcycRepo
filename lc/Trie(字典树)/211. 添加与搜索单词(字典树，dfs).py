class WordDictionary(object):

    def __init__(self):
        self.m = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        m = self.m
        for c in word:
            if c not in m:
                m[c] = {}
                m = m[c]
            else:
                m = m[c]
        m["#"] = {}

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.m, 0, word)

    def dfs(self, m, p, word):
        if p == len(word):
            return "#" in m

        # 假如word[p] != ".", 则我们就使用该字母来看是否满足search要求
        if word[p] != ".":
            nc = word[p]
            if nc in m and self.dfs(m[nc], p+1, word):
                return True
            else:
                return False
        else:
            # 假如word[p] == ".", 则我们使用26个字母去替代"."来继续遍历
            for i in range(26):
                nc = chr(ord('a') + i)
                if nc in m and self.dfs(m[nc], p + 1, word):
                    return True
            return False


# 古城算法: https://www.youtube.com/watch?v=qU3SbJHb7o8
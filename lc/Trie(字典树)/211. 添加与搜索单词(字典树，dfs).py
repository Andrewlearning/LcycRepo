"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.

WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""
# 自己的写法
class WordDictionary:
    def __init__(self):
        self.m = {}

    def addWord(self, word: str) -> None:
        m = self.m
        for c in word:
            if c in m:
                m = m[c]
            else:
                m[c] = {}
                m = m[c]
        m["#"] = {}

    def search(self, word: str) -> bool:
        # 因为我们要跳过带"."的字母，所以需要传一个跳过后"."的m
        # 这个函数的参数被限定死了，没办法满足我们的要求，所以我们要先创建一个helper函数来查找，
        return self.h(self.m, word)

    def h(self, m, word):
        for i in range(len(word)):
            c = word[i]
            if c == ".": #遍历到当前为.的情况，则dfs找到当前m所有key,看看哪个可以search成功
                for key in m.keys():
                    if self.h(m[key], word[i + 1:]):
                        return True
                return False
            if c in m: # 当前c在字典里，说明当前是匹配的，进入匹配下一位
                m = m[c]
            else: # 当前c不存在字典里，说明没找到、这个不能放前面，因为有可能是"."
                return False
        # 我们以#作为单词结束的标记，假如最后一位是#, 说明这个单词被找到了
        return "#" in m


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
            # 假如word[p] == ".", 则我们使用26个字母去替代"."来继续遍历
            for i in range(26):
                nc = chr(ord('a') + i)
                if nc in m and self.dfs(m[nc], p + 1, word):
                    return True

        return False


# 古城算法: https://www.youtube.com/watch?v=qU3SbJHb7o8
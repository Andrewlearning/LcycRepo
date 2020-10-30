"""
一个单词每次只能变一个字母，然后到达另一个单词，最后希望能到达endword

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。

"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        # queue存的是，当前的单词，以及变化的次数
        queue = [[beginWord, 1]]

        # 这个的作用是待会可以从里面取 原单词中没有的字母
        new_char_pool = "abcdefghijklmnopqrstuvwxyz"


        wordList = set(wordList)

        # 记录去过的路径
        # 因为这样能避免重复访问，重复访问就意味着这条路径 >= 先前访问的路径
        visited = set()

        while queue:
            word, dist = queue.pop(0)

            # 如果最后变换后的单词等于我们最终想要的结果，把距离返回
            if word == endWord:
                return dist

            for i in range(len(word)):
                for new_char in new_char_pool:

                    # 我们不断从26个字母中尝试，找到可以替换的字母
                    # 使得替换后的单词，没有被访问过，且在wordList里
                    if new_char != word[i]:
                        newWord = word[:i] + new_char + word[i + 1:]

                        if newWord not in visited and newWord in wordList:
                            queue.append([newWord, dist + 1])

                            # 记录当前node
                            visited.add(newWord)
        return 0

"""
上面的做法用的是单向BFS，时间复杂度比较高
思路：https://www.youtube.com/watch?v=vWPCm69MSfs

wordList = set(wordList)，避免单词重复出现的情况，提升了效率
"""
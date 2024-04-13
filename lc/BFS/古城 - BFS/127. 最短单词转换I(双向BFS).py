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
        # 假如没有这一步，会导致不可到达的endword也能被走到
        if endWord not in wordList:
            return 0

        # 从beginSet 和 endSet 这两个集合出发，假如bfs到对方set，那么说明可以从beginWord -> endWorld
        # set的底层实现是map, 查询时时间是O(1)
        wordList = set(wordList)
        beginSet = set()
        endSet = set()
        beginSet.add(beginWord)
        endSet.add(endWord)

        # 记录单词有没被构建过
        # 假如单词被构建过，第二次来到这个单词是没意义的，因为第一次走不通，第二次肯定也走不通
        visited = set()
        newCharPool = "abcdefghijklmnopqrstuvwxyz"

        # 初始单词没变化就已经算作是step=1了
        step = 1

        while len(beginSet) > 0 and len(endSet) > 0:
            # 用于记录BFS的下一层
            nextSet = set()

            # 永远从beginSet出发
            for word in beginSet:
                for i in range(len(word)):
                    # 替换掉单词的每一个字母，看看能不能构造出在wordList的单词
                    for newChar in newCharPool:
                        newWord = word[:i] + newChar + word[i + 1:]

                        # 假如beginSet的元素和endSet的元素重合了，那么说明我们找到一条路径满足条件
                        # 又因为endWord总是会在wordList出现的，所以我们这里不用校验newWord是否在wordList里
                        if newWord in endSet:
                            return step + 1
                        if newWord not in visited and newWord in wordList:
                            visited.add(newWord)
                            nextSet.add(newWord)

            # 重点，我们看哪个set的size小，下一次就从哪一边开始向中间遍历
            # 这样确保了我们的搜索范围不会变的特别大
            beginSet = nextSet
            if len(endSet) < len(beginSet):
                endSet, beginSet = beginSet, endSet

            step += 1

        return 0

"""
古城算法 23：00
https://www.bilibili.com/video/BV1Rz4y1Z7tJ
双向BFS
"""
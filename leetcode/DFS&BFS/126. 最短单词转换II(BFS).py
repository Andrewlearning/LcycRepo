# coding=utf-8
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: List[List[str]]
            """

            if endWord not in wordList:
                return []

            wordList = set(wordList)
            queue = [(beginWord, [beginWord])]

            # key为path的长度， value为对应的path, 最终目的是把长度最小的path全部return
            res = {}

            # 每个单词所对应的最小深度， 我们可以利用这个来进行减枝， 因为单词可能有重复利用现象，我们确保路径最小那就是
            depth = 0

            # 用于存储节点在哪一层遍历了
            distance = {}
            min_len = float('inf')

            while queue:
                depth += 1
                new_queue = []

                for word, path in queue:

                    # 当走到终点了，那么这个时候我就要看当前word的path长度，是否为最小path,是的话加入
                    if word == endWord:

                        # 如果长度小于之前最小长度，那我们把当前长度所对应的path给记录进去
                        if len(path) < min_len:
                            min_len = len(path)
                            res[min_len] = [path]
                        # 如果长度之前存在，那么把当前path 加到对应长度上去
                        else:
                            res[min_len].append(path)
                            continue

                    #当没走到终点时，我们要对当前单词的new_word进行一个个判断，从path的长度，以及path是否重复来进行筛选
                    # 无重复且长度短的path才能进入下一轮
                    for next_word in self.get_next_words(word, wordList):
                        # get的效果等同于distance[next_word], 只不过当next_word不存在的时候不会报错，而会返回None
                        # 所以这个语句的意思是，当next_word在distance存在，且它的depth小于当前循环的depth时
                        # 说明这个单词之前已经被遍历过了，存在比当前路径更短的路径，所以放弃这个单词形成的path, continue
                        if distance.get(next_word) and distance.get(next_word) < depth:
                            continue

                        # 否则，把当前深度与 next_word对应起来
                        distance[next_word] = depth

                        # 这里做一个减枝，假如说加上新单词后，path的大于 小于最小path的长度，那么不要
                        if len(path) + 1 > min_len:  # 取长度小的
                            continue

                        # 最后我们把符合条件的new word给加进path里去
                        if next_word not in path:
                            new_queue.append((next_word, path + [next_word]))

                queue = new_queue

            # 有可能出现res = {}的情况，此时要返回[]
            return [] if res.get(min_len) == None else res.get(min_len)


        # 127原题， 通过替换单词的每一个字母，来寻找可以替换的下一个单词
    def get_next_words(self, word, wordList):
        new_level_words = []

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in wordList:
                    new_level_words.append(next_word)

        return new_level_words

"""
https://www.bilibili.com/video/BV1yt411Y7gH?from=search&seid=6362656343066926492
看视频理解题意

解答来源
https://leetcode-cn.com/problems/word-ladder-ii/solution/pythonjian-dan-bfs-by-raprincehen-ye/
"""
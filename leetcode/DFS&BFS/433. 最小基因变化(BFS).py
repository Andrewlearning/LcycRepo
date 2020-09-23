class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = [[start, 0]]

        # 这个的作用是待会可以从里面取 原单词中没有的字母
        new_char_pool = "ACGT"

        # 去重
        bank = set(bank)
        visited = set()

        while queue:
            word, dist = queue.pop(0)

            # 如果最后变换后的单词等于我们最终想要的结果，把距离返回
            if word == end:
                return dist

            for i in range(len(word)):
                for new_char in new_char_pool:

                    # 我们不断从26个字母中尝试，找到可以替换的字母
                    # 使得替换后的单词，没有被访问过，且在wordList里
                    if new_char != word[i]:
                        newWord = word[:i] + new_char + word[i + 1:]

                        if newWord not in visited and newWord in bank:
                            queue.append([newWord, dist + 1])

                            # 第一问和第二问的区别在这里，在第一问中，我们只要使用过了这个单词
                            # 就把它从wordList中剔除，因为这样能避免重复访问，重复访问就意味着这条路径 >= 先前访问的路径
                            # 我们只要最短的
                            visited.add(newWord)

        # 若没有结果，返回-1
        return -1

"""
本题和126一样
"""
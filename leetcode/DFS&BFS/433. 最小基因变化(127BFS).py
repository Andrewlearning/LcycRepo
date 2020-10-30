"""
一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意:
起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
所有的目标基因序列必须是合法的。
假定起始基因序列与目标基因序列是不一样的。
示例 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]
返回值: 1
"""
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # 开始字符串：变化的次数
        queue = [[start, 0]]

        # 这个的作用是待会可以从里面取 原单词中没有的字母
        new_char_pool = "ACGT"

        # 去重
        bank = set(bank)

        # 记录去过的路径
        # 因为这样能避免重复访问，重复访问就意味着这条路径 >= 先前访问的路径
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

                            visited.add(newWord)

        # 若没有结果，返回-1
        return -1

"""
本题和126一样
"""
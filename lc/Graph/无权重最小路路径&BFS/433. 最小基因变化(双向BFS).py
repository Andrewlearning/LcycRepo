"""
一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
例如，基因序列由"AACCGGTT"变化至"AACCGGTA"即发生了一次基因变化。
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
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        # 假如终点不在bank里，说明无法到达
        # 加判断的愿意是，可能有不存在的word,但可以通过字母变换，在bank里有对应值，从而混过去了
        if endGene not in bank:
            return -1

        # 初始化，visited记录到过的节点，sset开始集合，eset终点集合
        # 都为set的目的是，查询时时间复杂是O(1)
        visited = set()
        sset = set()
        eset = set()
        sset.add(startGene)
        eset.add(endGene)

        bank = set(bank)
        pool = "ACGT"
        deepth = 1

        # 这里应该是and, 因为假如通过单词转换后，无法到达下一站，sset应该会等于空的set
        while sset and eset:
            # 记录下一层需要遍历的基因
            temp = set()

            for g in sset:
                for i in range(len(g)):
                    for c in pool:
                        ng = g[:i] + c + g[i + 1:]

                        # 假如new gene在endset里，说明我们找到了一条可以到达的路线
                        if ng in eset:
                            return deepth
                        # 假如new gene在bank里，且没有被访问过
                        # 说明下一层可以遍历这个gene
                        if ng in bank and ng not in visited:
                            temp.add(ng)
                            visited.add(ng)

            # 重点，我们看哪个set的size小，下一次就从哪一边开始向中间遍历
            # 这样确保了我们的搜索范围不会变的特别大
            sset = temp
            if len(sset) > len(eset):
                sset, eset = eset, sset
            deepth += 1

        return -1

"""
本题和127一样, 采用双向bfs，加速
"""
"""
给你一个字符串s，以及该字符串中的一些「索引对」数组pairs，其中pairs[i]
=[a, b]表示字符串中的两个索引（编号从 0 开始）。
你可以 任意多次交换 在pairs中任意一对索引处的字符。
返回在经过若干次交换后，s可以变成的按字典序最小的字符串。

示例 1:

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"


做法：
用并查集找到所有可交换位置的集合，排序每个集合内的字符，再插回原字符串。
例如s = "dcabfge", pairs = [[0,3],[1,2],[0,2],[4,6]]
那么可交换的集合有[0,1,2,3]、[4,6]
排序后的字符分别为'abcd', 'ef'
插回原字符串最终s = "abcdegf"
"""


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        uf = UF(len(s))

        for x, y in pairs:
            uf.union(x, y)

        # 把同一个父亲的数的下标 都装到一个集合里去
        hashmap = collections.defaultdict(list)
        for key in uf.parent.keys():
            # 这里因为是，有可能虽然是大家都属于同一组，但是不一定都是指向最上面的父亲
            # 所以这里要再find一次
            hashmap[uf.find(key)].append(key)

        res = list(s)

        for groupIndexSet in hashmap.values():
            # 把同一分组的下标转化成字母，然后进行排序
            orderedLetter = sorted(res[i] for i in groupIndexSet)

            # 我们要让小字母，排在前面，所以Index也要sort，用来更新res
            for i, letter in zip(sorted(groupIndexSet), orderedLetter):
                res[i] = letter

        return "".join(res)


class UF(object):
    def __init__(self, n):
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        # 进行路劲压缩，防止超时，是find时间复杂度降至O(1)
        self.parent[rootY] = rootX
        self.parent[x] = rootX
        self.parent[y] = rootX


# https://leetcode-cn.com/problems/smallest-string-with-swaps/solution/bing-cha-ji-python-by-fa-kuang-de-jie-zi/

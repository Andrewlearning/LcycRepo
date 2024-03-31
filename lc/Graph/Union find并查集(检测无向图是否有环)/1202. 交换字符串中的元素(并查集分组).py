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
        # map的 key:父亲节点下标， value:子节点下标
        hashmap = collections.defaultdict(list)
        for key in uf.parent.keys():
            parent = uf.find(key)
            hashmap[parent].append(key)

        # 把字符串转为list, 方便后面修改
        res = list(s)

        # 我们只替换那些在pairs里出现的元素
        for groupIndexSet in hashmap.values():
            # 把同一分组的下标转化成字母，然后进行排序
            orderedLetter = sorted([res[i] for i in groupIndexSet])

            # 我们要让小字母，排在前面
            j = 0
            for i in groupIndexSet:
                res[i] = orderedLetter[j]
                j += 1

        return "".join(res)

class UF(object):
    def __init__(self, n):
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return
        self.parent[fx] = fy


# https://leetcode-cn.com/problems/smallest-string-with-swaps/solution/bing-cha-ji-python-by-fa-kuang-de-jie-zi/

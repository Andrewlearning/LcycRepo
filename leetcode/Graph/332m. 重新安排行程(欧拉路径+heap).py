"""
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

提示：
如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
所有的机票必须都用一次 且 只能用一次。
 

示例 1：
输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出：["JFK", "MUC", "LHR", "SFO", "SJC"]
"""
import heapq
import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.res = []
        self.fromTo = collections.defaultdict(list)

        # 使用堆来储存to数组，保证能pop出字典序最小的
        for from_, to_ in tickets:
            heapq.heappush(self.fromTo[from_], to_)

        self.helper("JFK")

        return self.res[::-1]

    def helper(self, from_):
        # 欧拉路径，终点的入度要比出度大一
        # 所以当我们遍历到一个节点，发现它有from，但是没有to，那说明这个点是终点，于是我们把这个点个加到res
        # 然后退递归，把前面的路程的每个点都加到res里
        # 结果来到起点，起点是最后一个被加进去的
        while self.fromTo[from_]:
            next = heapq.heappop(self.fromTo[from_])
            self.helper(next)
        self.res.append(from_)

"""
欧拉路径性质
起点：出度比入度大一。因为起点入度=0
终点：入度比出度大一，因为终点出度=0
其余点，入度=出度
https://www.acwing.com/video/1724/
"""
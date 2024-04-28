"""
给出方程式A / B = k, 其中A 和B 均为用字符串表示的变量，k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回-1.0。

输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。


示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
给定：a / b = 2.0, b / c = 3.0
问题&测试文件：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
返回：[6.0, 0.5, -1.0, 1.0, -1.0 ]
"""

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict

        graph = defaultdict(dict)

        # 构建有向图
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        def dfs(start, end, visited):
            # 假如除数和被除数有任何一个不存在记录，则说明无法得到答案
            if start not in graph or end not in graph:
                return -1.0
            # 这对除法有结果，则直接返回答案
            if end in graph[start]:
                return graph[start][end]

            # 每次图的寻找，记录走过的节点，避免进入死循环
            visited.add(start)
            
            # 查看当前start有哪些child可以遍历
            for child, val in graph[start].items():
                # 核心思想: start/child * child/end = start/end
                if child not in visited:
                    result = dfs(child, end, visited)
                    if result != -1.0:
                        return val * result

            # 假如没找到结果，则返回-1
            return -1.0

        res = []
        for query in queries:
            start, end = query
            res.append(dfs(start, end, set()))

        return res

# from chatgpt，比闫总的好理解

import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        vertex = set()
        path = collections.defaultdict(dict)
        n = len(equations)

        for i in range(n):
            x, y = equations[i][0], equations[i][1]
            path[x][y] = values[i]
            path[y][x] = 1/values[i]

            # 把记录过的点加入到vertex里去
            vertex.add(x)
            vertex.add(y)

        # 把所有的点之间的距离都求出来，后面遍历就行了
        # 主要利用k做桥梁计算，通过i, j来遍历vertex里的所有组合，记录所有组合的除法结果
        # 当然，这里只能对有交集的集合 [a,b] [b,c] -> a:[a,b,c] 进行连接
        # 对无交集的集合，没办法进行链接 [a,b] [c,c] -> a:[a,b]
        for k in vertex:
            for i in vertex:
                for j in vertex:
                    # i/k * k/j = i/k, 得到i ~ k的距离
                    if k in path[i].keys() and j in path[k].keys():
                        path[i][j] = path[i][k] * path[k][j]

        res = []
        for q in queries:
            up, down = q[0], q[1]
            # up/down 存在，返回结果
            if down in path[up].keys():
                res.append(path[up][down])
            else:
                res.append(-1)

        return res

# https://www.acwing.com/activity/content/problem/content/2798/1/

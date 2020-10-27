"""
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。


示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
给定：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
返回：[6.0, 0.5, -1.0, 1.0, -1.0 ]
"""

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
        for (a, b), v in zip(equations, values):
            path[a][b] = v
            path[b][a] = 1 / v
            # 把记录过的点加入到vertex里去
            vertex.add(a)
            vertex.add(b)

        # 把所有的点之间的距离都求出来，后面遍历就行了
        for k in vertex:
            for i in vertex:
                for j in vertex:
                    # i/k * j/k = i/k, 得到i ~ k的距离
                    if k in path[i].keys() and j in path[k].keys():
                        path[i][j] = path[i][k] * path[k][j]

        res = []
        for q in queries:
            up = q[0]
            down = q[1]
            # up/down 存在，返回结果
            if down in path[up].keys():
                res.append(path[up][down])
            else:
                res.append(-1)

        return res

# https://www.acwing.com/activity/content/problem/content/2798/1/

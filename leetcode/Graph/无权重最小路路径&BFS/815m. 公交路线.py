"""
我们有一系列公交路线。每一条路线 routes[i] 上都有一辆公交车在上面循环行驶。例如，有一条路线 routes[0] = [1, 5, 7]，表示第一辆 (下标为0) 公交车会一直按照 1->5->7->1->5->7->1->... 的车站路线行驶。

假设我们从 S 车站开始（初始时不在公交车上），要去往 T 站。 期间仅可乘坐公交车，求出最少乘坐的公交车数量。返回 -1 表示不可能到达终点车站。

 
示例：

输入：
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
输出：2
解释：
最优策略是先乘坐第一辆公交车到达车站 7, 然后换乘第二辆公交车到车站 6。
"""
import collections
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0

        routes = map(set, routes)
        graph = collections.defaultdict(set)

        # 构造图
        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]

                # 看当前两个路线集合有没有交集
                # 假如说有交集的话，说明这两个公交车可以相互到达对方的位置
                if len(r1 & r2) != 0:
                    graph[i].add(j)
                    graph[j].add(i)

        # 将跟开始站相连的所有路线下标，都放进seen
        # 将于结束站相连的所有路线下标，都放进target
        seen, targets = set(), set()
        for index, route in enumerate(routes):
            if S in route:
                seen.add(index)
            if T in route:
                targets.add(index)

        # 图从深度1开始进行BFS
        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            # 当前下标在终点站的下标范围内，则返回深度
            if node in targets:
                return depth

            # 否则，往queue里添加邻居路线
            for nei in graph[node]:
                # 去之间没走过的下标
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))

        # 找不到则返回-1
        return -1

"""
在广度优先搜索时，包含 N 个点的图的边数最大可以达到 O(N^2)
 因此时间复杂度为 O(N^2)

空间复杂度：O(N^2)用来存储图。
s
我们可以把所有进过某个点的路线，都设置为是同一个深度，因为通过这个公交站
可以去到相连所有路线的公交站。
https://leetcode-cn.com/problems/bus-routes/solution/gong-jiao-lu-xian-by-leetcode/
"""
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0

        routes = map(set, routes)
        graph = collections.defaultdict(set)

        # 构造图
        for i, r1 in enumerate(routes):
            for j in xrange(i + 1, len(routes)):
                r2 = routes[j]

                # 看当前两个集合有没有交集
                # 假如说有交集的话，说明这两个公交车和相互到达对方的位置
                if len(r1 & r2) != 0:
                    graph[i].add(j)
                    graph[j].add(i)

        # 将跟开始站相连的所有路线下标，都放进start
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
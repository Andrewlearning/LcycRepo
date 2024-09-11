"""
记录可以完成所有课程的可行性路径
"""
class Solution(object):
    def findOrder(self, num, prereq):
        """
        :type num: int
        :type prereq: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict

        # 初始化图, 节点为 pre -> [next1, next2], 先修课 指向 后修课
        graph = defaultdict(list)

        # 初始化入度，pre -> next -> 0
        # pre 的入度为0，因为每节点指向pre
        # next 入度为1，因为pre指向它
        indegree = defaultdict(int)

        for next, pre in prereq:
            # 开始给图的顶点赋予意义，先修课->[下一节课]
            graph[pre].append(next)

            # 构造入度表 node:指向这个node的节点数量有多少
            indegree[next] += 1


        # 把入度为0的点都加入到queue里去
        queue = []
        for node in range(num):
            if indegree[node] == 0:
                queue.append(node)

        # count记录我们总共已经上过了几门课，假如有课不可到达，那么count是不可能 == numCourse的
        # 等于numcourse的
        res = []
        count = 0
        while queue:
            pre = queue.pop(0)
            count += 1
            res.append(pre)

            # 删除上一个节点pre，所以与之对应pre节点的下一层节点所有的入度都要-1
            for next in graph[pre]:
                indegree[next] -= 1

                # 把入度为0的下一层节点加入到queue
                if indegree[next] == 0:
                    queue.append(next)

        if count == num:
            return res
        return []

"""
time(V+E) Space(V+E)
需要记录每一次遍历到的结果
"""

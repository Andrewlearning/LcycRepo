"""
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
"""
#方法1 DFS
class Solution(object):
    def hasCycle(self, graph, visited, checked, v):
        # visited被访问过了，说明有环，返回True
        if visited[v]:
            return True
        visited[v] = True

        # 判断v路径下的所有节点是否有环
        for i in graph[v]:
            if not checked[i] and self.hasCycle(graph, visited, checked, i):
                return True

        # 没有环，把v加进checked,然后在visited把v给还原下
        checked[v] = True
        visited[v] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]][后修，先修]
        :rtype: bool
        """
        if numCourses <= 1 or prerequisites is None or len(prerequisites) == 0:
            return True
        # 把每个课都创一个属于自己的list,list里存放着的都是当前index后修的课
        graph = [[] for i in range(numCourses)]

        # (0,1) 0<-1
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])

        # 初始化checked 和 visited
        checked = [False]*numCourses
        visited = [False]*numCourses

        # 检查每个课号，看他们的后修课是否有环
        for i in range(numCourses):
            if not checked[i] and self.hasCycle(graph,visited,checked,i):
                return False
        return True

"""
time(V+E) Space(V+E)
方法2：拓扑排序 = 顶点染色 + 记录顺序
"""

# 拓扑排序
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites and len(prerequisites) == 0:
            return True

        graph = {}
        indegree = {}

        # 初始化构造图的顶点, pre ->[next1,next2]
        # 初始化入度， next -> 0
        for node in range(numCourses):
            graph[node] = []
            indegree[node] = 0

        for next, pre in prerequisites:
            # 开始给图的顶点赋予意义， 上一节课->[下一节课]
            graph[pre].append(next)

            # 构造入度和表 点 : 指向这个点的数量有多少
            indegree[next] += 1


        # 把入度为0的点都加入到queue里去
        queue = []
        for pre in indegree:
            if indegree[pre] == 0:
                queue.append(pre)

        # count记录我们总共已经上过了几门课，假如有课不可到达，那么count是不可能 == numCourse的
        # 等于numcourse的
        count = 0
        while queue:
            count += 1
            pre = queue.pop(0)

            # 删除上一个节点，所以与之对应的下一个节点所有的入度都要-1
            for next in graph[pre]:
                indegree[next] -= 1

                # 把入度为0的节点加入到queue
                if indegree[next] == 0:
                    queue.append(next)

        return count == numCourses




"""
你要计算出完成这 n 门课程的一个上课顺序。如果有多个可行顺序，
只要返回其中一个即可。如果无法上完所有课程，则返回一个空数组。

这题与207的区别只在于，需要记录被遍历过没有循环的节点，并返回出来
假如说有循环节点，那么就返回[]
"""
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
        self.res.append(v)
        visited[v] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]][后修，先修]
        :rtype: bool
        """
        # if numCourses <= 1 or prerequisites is None or len(prerequisites) == 0:
        #     return []
        # 把每个课都创一个属于自己的list,list里存放着的都是当前index后修的课
        graph = [[] for i in range(numCourses)]

        # (0,1) 0<-1
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])

        # 初始化checked 和 visited
        self.res = []
        checked = [False]*numCourses
        visited = [False]*numCourses

        # 检查每个课号，看他们的后修课是否有环
        for i in range(numCourses):
            if not checked[i] and self.hasCycle(graph,visited,checked,i):
                return []

        return self.res[::-1]

"""
方法二，拓扑排序
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]][后修，先修]
        :rtype: bool
        """
        graph = {}
        indegree = {}

        # 初始化构造图的顶点, 点 ->[]
        # 初始化入度， 点 -> 0
        for node in range(numCourses):
            graph[node] = []
            indegree[node] = 0

        # 初始化图和 入度表
        for next, pre in prerequisites:
            graph[pre].append(next)
            indegree[next] += 1

        queue = []
        # 找入度为0的做起点
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        res = []
        while queue:
            pre = queue.pop(0)
            count += 1
            res.append(pre)

            # 当前课程上过了，所有对应的下一个课程入度都-1
            for next in graph[pre]:
                indegree[next] -= 1

                # 假如下一个课程的入度为0，则加进queue
                if indegree[next] == 0:
                    queue.append(next)

        return res if count == numCourses else []

"""
remark:
这题即使不写判断边界条件也不会出错，因为我们在创造graph的时候，默认最差就是创造出一个
(num = 0)，然后即使这样进行下去，count != numcourses 就返回一个[].对实际结果没影响
但是207 就需要判断了
"""

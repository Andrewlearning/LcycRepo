# coding=utf-8
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        graph = {}
        indegree = {}

        # 初始化graph 和 入度表
        # 注意这个初始化是要对每个出现的字符都进行初始化
        for word in words:
            for char in word:
                graph[char] = []
                indegree[char] = 0

        # 给graph赋值
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]) and j < len(words[i + 1]):
                if words[i][j] != words[i + 1][j]:
                    # 优先级高 -> 优先级低
                    graph[words[i][j]].append(words[i + 1][j])
                    break
                j += 1

        # 填充入度表
        for nexts in graph.values():
            for next in nexts:
                indegree[next] += 1

        # 把入度为0的点装进queue里
        queue = []
        for key in indegree.keys():
            if indegree[key] == 0:
                queue.append(key)

        res = []
        while queue:
            pre = queue.pop(0)
            res.append(pre)

            # 删除了pre节点，那么这个pre所对应的next,全部的入度都要-1
            # 然后顺带检查next的入度是否为0， 如果为0的话那么要把next加入queue
            for next in graph[pre]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)

        is_unval = False
        # 出队元素个数不等于图顶点个数，说明有环
        if len(res) != len(graph):
            is_unval = True

        # abc
        # ab  ,这种情况，a->a b->b不可能， c->""也不可能
        for i in range(len(words) - 1):
            if len(words[i]) > len(words[i + 1]) and words[i][:len(words[i + 1])] == words[i + 1]:
                is_unval = True
                break

        return "" if is_unval == True else "".join(res)

# 作者：zhouquan
# 链接：https://leetcode-cn.com/problems/alien-dictionary/solution/python3-tuo-bu-pai-xu-by-zhouquan/

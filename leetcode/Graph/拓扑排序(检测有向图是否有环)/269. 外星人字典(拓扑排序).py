class Solution:
    def alienOrder(self, words):
        # 每个字母代表图的一个顶点
        # 邻接表表示有向图

        # key: 每个字母  value: 比当前字母优先级低的字母
        graph = {}

        # 构建图顶点
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = []

        # 两两单词进行比较，确定图的方向
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]) and j < len(words[i + 1]):
                if words[i][j] != words[i + 1][j]:
                    # 优先级高 -> 优先级低
                    graph[words[i][j]].append(words[i + 1][j])
                    break
                j += 1

        # key: 元素  value: 元素所对应的入度是多少
        in_degrees = {}
        res = []

        # 首先把每个char的入度都设成0
        for char in graph:
            in_degrees[char] = 0

        # 我们可以理解，graph的元素，全都是被指向的元素。所以元素出现一次，入度就要+1
        for values in graph.values():
            for char in values:
                in_degrees[char] += 1

        queue = [k for (k, v) in in_degrees.items() if v == 0]
        while queue:
            cur = queue.pop()
            res.append(cur)

            for next in graph[cur]:
                in_degrees[next] -= 1  # 删除该入度为0的节点后，该节点指向的节点入度减1
                if in_degrees[next] == 0:
                    queue.append(next)

        # 判断非法顺序(判断有向图是否有环)
        is_unval = False
        if len(res) != len(graph):  # 出队元素个数不等于图顶点个数，说明有环
            is_unval = True

        # abc 排在 ab前面，也属于非法输入
        for i in range(len(words) - 1):
            if len(words[i]) > len(words[i + 1]) and words[i][:len(words[i + 1])] == words[i + 1]:
                is_unval = True
                break

        if is_unval:
            return ""

        # 无法判断顺序的返回随机顺序
        if not is_unval and res == []:
            return "".join([k for k in graph])


        return "".join(res)

# 作者：zhouquan
# 链接：https://leetcode-cn.com/problems/alien-dictionary/solution/python3-tuo-bu-pai-xu-by-zhouquan/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
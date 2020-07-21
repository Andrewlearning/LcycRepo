"""
Given a reference of a node in a connected undirected Graph, return a deep copy (clone) of the Graph. Each node in the Graph contains a val (int) and a list (List[Node]) of its neighbors
把一个图的节点和边都复制出来
"""

class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def __init__(self):
        self.map = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        copy = Node(node.val, [])

        # 我们把每一个node所对应的复制节点一一对应保存在map里
        # 这样当我们去到一个节点时，我们就可以知道它有没有复制过
        # 没有复制过，我们就再调用本函数
        # 有复制过，就把它加进neighbor里去
        self.map[node] = copy

        # 这里的neighbor, 最终都要要复制到copy的neighbor里去
        for neighbor in node.neighbors:
            if neighbor in self.map:
                copy.neighbors.append(self.map[neighbor])
            # 假如说neighbor不在map里面，说明我们并没有复制它的节点
            else:
                copy.neighbors.append(self.cloneGraph(neighbor))

        # 返回copy节点，给其他节点添加进neighbor
        return copy


# https://algocasts.io/episodes/XZWvPNG7

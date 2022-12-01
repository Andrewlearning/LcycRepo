"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = [root]
        res = []
        temp = []

        while queue:
            res.append([node.val for node in queue])

            while queue:
                node = queue.pop(0)
                for child in node.children:
                    temp.append(child)

            queue = temp
            temp = []

        return res

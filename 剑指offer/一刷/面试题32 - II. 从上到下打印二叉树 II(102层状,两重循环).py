# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        res = []

        # queue放当前需要遍历的层
        queue = [root]

        # temp 放下一层应该遍历的节点
        temp = []

        while queue:
            val = [node.val for node in queue]
            res.append(val)

            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue = temp
            temp = []

        return res


"""
"""


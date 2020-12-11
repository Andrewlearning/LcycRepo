"""
给定二叉树，按垂序遍历返回其结点值。

对位于 (X, Y) 的每个结点而言，其左右子结点分别位于 (X-1, Y-1) 和 (X+1, Y-1)。

把一条垂线从 X = -infinity 移动到 X = +infinity ，每当该垂线与结点接触时，我们按从上到下的顺序报告结点的值（ Y 坐标递减）。

如果两个结点位置相同，则首先报告的结点值较小。

按 X 坐标顺序返回非空报告的列表。每个报告都有一个结点值列表。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        self.vals = []

        self.preorder(root, 0, 0)

        last = -1000
        res = []
        # 我们只对x的坐标排序就好了，这样就能做到从小到大过去
        for x, y, node in sorted(self.vals):
            # 当出现一个新的的x，要先往res里插入一个[],然后再往这里面加数
            if x != last:
                res.append([])
                last = x
            res[-1].append(node)

        return res

    def preorder(self, root, x, y):
        if not root:
            return
        self.vals.append((x, y, root.val))
        self.preorder(root.left, x - 1, y + 1)
        self.preorder(root.right, x + 1, y + 1)

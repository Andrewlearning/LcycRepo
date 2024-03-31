# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return
        # d == 1 的情况，按照题目的要求：创建一个新的根节点v，原先的整棵树将作为 v 的左子树。
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        # 创建值为v的两个新结点，把新结点插到根节点的左右子树上
        # 把根节点原来的左子树，接到左新结点的左子树上。
        # 把根节点原来的右子树，接到右新结点的右子树上
        if d == 2:
            L = TreeNode(v)
            R = TreeNode(v)

            L.left = root.left
            R.right = root.right

            root.left = L
            root.right = R
            return root

        self.addOneRow(root.left, v, d - 1)
        self.addOneRow(root.right, v, d - 1)
        return root

# https://leetcode-cn.com/problems/add-one-row-to-tree/solution/pythonwu-xu-fu-zhu-han-shu-jian-ji-de-di-gui-xie-f/
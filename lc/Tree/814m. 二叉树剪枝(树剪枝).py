"""
给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

返回移除了所有不包含 1 的子树的原二叉树。
"""

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        return root if self.helper(root) else None

    def helper(self, node):
        if not node:
            return False

        left = self.helper(node.left)
        right = self.helper(node.right)
        if not left:
            node.left = None
        if not right:
            node.right = None

        # 证明从当前节点开始的树里存在1的节点
        return node.val == 1 or left or right

# 链接：https://leetcode-cn.com/problems/binary-tree-pruning/solution/er-cha-shu-jian-zhi-by-leetcode/

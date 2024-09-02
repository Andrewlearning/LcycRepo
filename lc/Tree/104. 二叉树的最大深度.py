# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root:
                return 0

            # 分别求到左右子树的最大深度
            left = helper(root.left)
            right = helper(root.right)

            # 返回当前节点的层数 + 当前节点子树的层数
            return 1 + max(left, right)

        return helper(root)

"""
时间复杂度:
函数 helper 是一个递归函数，用来计算二叉树中每个节点的最大深度。它递归遍历树的每一个节点。
- 对于每个节点，函数都执行一次检查 if not root 以及对左右子树的递归调用。递归调用会遍历每个节点，且每个节点的工作量是常数时间。
- 因此，假设树中有 n 个节点，时间复杂度为 O(n)，因为每个节点都被访问了一次。

空间复杂度分析：
空间复杂度主要取决于递归栈的深度。
- 最坏情况下，树是单链表（即退化为链表），此时递归栈的深度为 n，即树的节点数。因此，空间复杂度为 O(n)。
- 最好情况下，树是平衡的，此时递归栈的深度为树的高度，即 O(log n)。

总结
最坏情况下的空间复杂度为 O(n)。
最好情况下的空间复杂度为 O(log n)。
"""
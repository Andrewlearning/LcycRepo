"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

exp1:
输入：[1,1,1,1,1,null,1]
输出：true

exp2:
输入：[2,2,2,5,2]
输出：false
"""


# Definition for a binary tree node.
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
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 记录所有节点的值
        self.value = [root.val]
        self.helper(root)
        return len(set(self.value)) == 1

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)
        self.value.append(root.val)
        self.helper(root.right)




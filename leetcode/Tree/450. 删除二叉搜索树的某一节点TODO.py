# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        # 先通过递归找到 root.val == key的节点
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        # 找到到了root.val == key的节点
        else:
            # 删除根节点，假如说只有左子树，那么返回左子树，只有右子树，那么返回右子树
            # 另外的情况是，假如左右子树都没有，那么left,right都是none,返回其中一个即可
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left

            # 假如左右子树都有的情况，那么我们要按照BST的顺序，是 左边最大的 -> root -> 右子树
            # 然后我们只要 左边最大的.right -> 右子树就可了
            # 其中左边最大的在左子树的最右节点
            else:
                leftMax = root.left
                while leftMax.right:
                    leftMax = leftMax.right
                leftMax.right = root.right

                # 这里为什么不用return ?
                root = root.left

        return root

"""
https://algocasts.io/episodes/Q2prgeWz
Time: O(h), Space: O(h)

"""
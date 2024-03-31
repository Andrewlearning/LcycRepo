# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return None

        # 要删的节点在左子树
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # 要删的节点在右子树
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # key = root.val, 删除根节点的情况
            # 假如说只有左子树，那么返回左子树，只有右子树，那么返回右子树
            # 另外的情况是，假如左右子树都有，那么删除当前节点，找右子树最小的节点替换上
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.val = self.findMin(root.right)
                root.right = self.deleteNode(root.right, root.val)
        return root

    # 一路往左找，这样就能确保找到的就是最小节点
    def findMin(self, root):
        while root.left:
            root = root.left
        return root.val

"""
https://www.youtube.com/watch?v=DpkTu2tU87o&t=1007s 18.50
Time: O(logN), Space: O(N)
"""
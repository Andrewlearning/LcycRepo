"""
前序遍历 preorder = [3,9,20,15,7]  root left right
中序遍历 inorder = [9,3,15,20,7]   left root right
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def buildTree(self, preorder, inorder):
#         """
#         :type preorder: List[int]
#         :type inorder: List[int]
#         :rtype: TreeNode
#         """
#         # 假如说任意一个list为空的话，说明节点已经用完，应该返回None
#         if not preorder or not inorder:
#             return None
#
#         # 因为前序遍历，第一个节点总是root， 找到root以后就要对他进行一个分界了
#         root = TreeNode(preorder.pop(0))
#         # 中序遍历中， 在root左边的就是左子树， 在root右边的就是右子树
#         index = inorder.index(root.val)
#
#         # 因为对于preorder来说， root left, 所以下一个节点是左子树的，所以就先递归左子树
#         root.left = self.buildTree(preorder, inorder[:index])
#         root.right = self.buildTree(preorder, inorder[index + 1:])
#         return root

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # key:inorder的值 value:值在数组里的下标
        self.map = {}
        self.preOrderIndex = 0
        self.preorder = preorder
        self.inorder = inorder
        length = len(self.preorder)

        # 记录inorder的下标在map里，使得获取下标时时间复杂度为O(1)
        for i in range(len(self.preorder)):
            self.map[inorder[i]] = i
        
        return self.helper(0, length - 1)

    def helper(self, inStart, inEnd):
        # 当遍历到只有最后一个叶节点时，从index来看
        # 再没有左右子树了，所以可以返回None
        if inStart > inEnd:
            return None

        # 因为preOrder是 root,left,right
        # 第一个节点总是其他节点的根节点，所以我们取它出来构造树
        root = TreeNode(self.preorder[self.preOrderIndex])
        self.preOrderIndex += 1

        # 获取这个根节点在 inOrder中的下标
        # root下标的左边是左子树，下标的右边是右子树
        rootIndex = self.map[root.val]

        root.left = self.helper(inStart, rootIndex - 1)
        root.right = self.helper(rootIndex + 1, inEnd)

        return root

"""
古城算法 O(n) 22:00
https://www.bilibili.com/video/BV1jb4y1974B
"""
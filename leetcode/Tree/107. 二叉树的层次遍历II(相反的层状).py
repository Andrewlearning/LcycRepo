"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        res = []
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

        return res[::-1]

"""
其实就是树的层级遍历，因为我们要把每一层都作为一个List储存在res里，最后反转一遍

所以我们在bfs的时候，把每一层的结果都放到一个 [x] 里，最后让这个queue = [x]
然后在开头都时候把queue里的每个元素都放进res里
"""
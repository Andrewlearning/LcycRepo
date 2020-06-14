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

# Definition for a binary tree node.
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

        while queue:
            # queue用来装这一层需要遍历的元素 以及下一层需要装进去的元素

            # temp用来当前这一层的结果
            temp = []

            # 我们用这个for 循环锁住了queue的取值范围，所以后面无论怎么放都不会影响到
            # 我们当前这一层的情况
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.insert(0,temp)

        return res

"""
其实就是树的层级遍历，因为我们要把每一层都作为一个List储存在res里，最后反转一遍

所以我们在bfs的时候，把每一层的结果都放到一个 [x] 里，最后让这个queue = [x]
然后在开头都时候把queue里的每个元素都放进res里
"""
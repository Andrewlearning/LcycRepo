# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        self.helper(root)

        return root

    def helper(self, root):
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.helper(root.left)
        self.helper(root.right)





"""
脑子里只想到要用递归来做，但是这个返回根节点就让我有点迷糊了
然后想到的大概处理办法就是 写一个helper, 然后在主函数里面先处理一遍

后面看了答案才发现居然是如此简单：
1。停止机制，当到了最后一个节点的时候停止
2。转换机制，当不是最后一个节点的时候开始转换
    root.left, root.right = root.right, root.left



"""
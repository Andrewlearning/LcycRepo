# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root)[1]

    def helper(self, root):
        if not root:
            return 0, None

        dl, left = self.helper(root.left)
        dr, right = self.helper(root.right)

        # print("dl",dl, " ", "left", left)
        # print("dr", dr, " ", "right", right)
        # print(" ")

        # 发现左边比右边深，那我们就不用看右边了，只选用右子树的最深公共节点
        # 且假如子树为None, 则返回0，这样none节点肯定会被排除
        if dl > dr:
            return dl + 1, left
        # 发现右边比左边深，我们就不用看左边了，只选用右子树的最深公共节点
        # 且假如子树为None, 则返回0，这样none节点肯定会被排除
        elif dl < dr:
            return dr + 1, right
        # 发现左右一样深，说明在左右子树都找到了相同深度的最深节点
        # 就返回当前节点
        else:
            return dl + 1, root


"""
Time O(n) space O(n)
古城算法: https://www.youtube.com/watch?v=10-xBLiytBA&t=95s 46：00

自下而上返回节点信息
每次返回的是[当前深度，最深的节点的最小公共祖先值]

这个题结合了
利用dfs来统计深度
利用back recursion只选择最深节点的值
"""
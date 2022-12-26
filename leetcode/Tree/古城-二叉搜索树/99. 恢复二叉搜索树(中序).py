"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例1:

输入: [1,3,null,null,2]

  1
 /
3
 \
  2

输出: [3,1,null,null,2]

  3
 /
1
 \
  2

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        # 本题必须得用node来直接进行操作，要不然值不能inplace修改
        x = y = pre = None
        pre = TreeNode(float('-inf'))

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # 假如发现违反二叉树搜索树中序遍历的递增
            if root.val < pre.val:
                # 肯定是有一个大的节点被后面挪到了前面，才能实现一个节点比next大，那么这个节点就是x
                if x is None:
                    x = pre
                    y = root
                # 肯定是有一个小的节点被前面挪到了后面，才能实现一个节点比pre小，这个节点就是y
                else:
                    y = root
            pre = root
            root = root.right

        # 最后把乱序的节点交换一下
        x.val, y.val = y.val, x.val

# 我们要理解这个题的规则，一棵树的两个节点交换，肯定是一个比当前所在位置的节点大，一个比当前所在位置的节点小
# 那么违反规则的话，那就是 一个节点比pre小， 一个节点比next大
# 因为BST是从小到大递增的话，
# 就肯定是有一个大的节点被后面挪到了前面，才能实现一个节点比next大，那么这个节点就是x
# 就肯定是有一个小的节点被前面挪到了后面，才能实现一个节点比pre小，这个节点就是y
# 解法2的图 https://leetcode-cn.com/problems/recover-binary-search-tree/solution/san-chong-jie-fa-xiang-xi-tu-jie-99-hui-fu-er-cha-/

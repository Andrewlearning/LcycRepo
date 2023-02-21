"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        # 头节点
        self.head = None

        # 尾节点
        self.end = None
        self.helper(root)

        # 头节点在头，尾节点在尾巴
        # 两两互指
        self.head.left, self.end.right = self.end, self.head

        return self.head

    # 中序遍历二叉搜索树，左中右，使得我们可以有序连接链表
    def helper(self, node):
        if not node:
            return

        self.helper(node.left)

        # 当我们有头节点的时候，我们把 end,root这一前一后的两个节点两两连接
        if self.head:
            #   end -> node
            #   end <- node
            self.end.right, node.left = node, self.end

        # 当我们没有头节点，则先给头结点赋值头节点
        else:
            self.head = node

        # 把end移到下一个位置
        self.end = node

        self.helper(node.right)

# 古城算法 32：00
# https://www.bilibili.com/video/BV1e5411c7JR/?spm_id_from=333.337.search-card.all.click&vd_source=b81616a45fd239becaebfee25e0dbd35
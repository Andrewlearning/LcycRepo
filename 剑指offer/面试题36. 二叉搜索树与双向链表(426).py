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

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)

        # 当我们有头节点的时候，我们把 end,root这一前一后的两个节点两两🔗
        if self.head:
            #   end -> root
            #   end <- root
            self.end.right, root.left = root, self.end

        # 当我们没有头节点，则需要指定头节点
        else:
            self.head = root

        # 把end移到下一个位置
        self.end = root

        self.helper(root.right)


"""
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
"""
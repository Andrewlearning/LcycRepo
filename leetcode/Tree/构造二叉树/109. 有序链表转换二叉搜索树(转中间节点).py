"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/kuai-man-zhi-zhen-zhao-zhong-dian-by-powcai/
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.helper(head, None)

    def helper(self, head, tail):
        # 当链表只有一个节点的时候，直接返回那个节点
        if head == tail:
            return

        # 找到链表的中点作为root
        mid = self.findMid(head, tail)
        root = TreeNode(mid.val)

        # 然后以这个中点分成两部分，来进行递归
        root.left = self.helper(head, mid)
        root.right = self.helper(mid.next, tail)

        return root


    # 每次寻找指定链表的中点并返回，作为root
    def findMid(self, head, tail):
        slow = fast = head

        # 注意这里的处理方式
        # 因为在这里我们等于是让tail = None
        # 所以我们不能让 fast, fast.next = tail
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next

        return slow


"""
做法基本上和108是一模一样的，只不过是数组变成了链表
"""
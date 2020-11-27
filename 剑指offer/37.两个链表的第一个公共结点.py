# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pa = headA
        pb = headB

        # 当两个指针没有指向同一个节点时，一直继续循环
        while pa != pb:

            # 当A指针已经走到空节点时，那么a指针从B链表开始继续走
            if pa == None:
                pa = headB
            # 否则则继续往下走
            else:
                pa = pa.next

            # 当B指针已经走到空节点时，那么B指针从A链表开始继续走
            if pb == None:
                pb = headA

            # 否则则继续往下走
            else:
                pb = pb.next

        # 返回任意一个节点即可
        return pa


"""
做法：
这道题和160.Intersection of Two Linked Lists是一样的。都是求两个链表的第一个公共结点。
方法一：

我们可以把两个链表拼接起来，一个pHead1在前pHead2在后，一个pHead2在前pHead1在后。
这样，生成了两个相同长度的链表，那么我们只要同时遍历这两个表，就一定能找到公共结点。
有点像快慢指针

            a
              \ 
                c
              /   
     b1 -b2

a - c - b1 - b2 - c - b1 - b2 - c - b1 - b2- c
b1- b2- c  - a  - c -  a - c  - a - c  - a - c

我们可以发现，运用这种方法能使的c出现多次重叠，因为两个链表是非相等且循环，所以总有概率是能遍历
到相同点

时间复杂度O(m+n)，空间复杂度O(m+n)。
"""
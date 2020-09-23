"""
输入两个链表，找出它们的第一个公共结点。
"""
# Definition for singly-LinkedList.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        pa = headA
        pb = headB

        while pa != pb:
            # 为什么这样写呢，因为当两个链表没有交点的时候，要让pa == pb == None才能
            # 退出循环，同时返回None
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa

"""
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

时间复杂度O(m+n)，空间复杂度O(1)。

"""
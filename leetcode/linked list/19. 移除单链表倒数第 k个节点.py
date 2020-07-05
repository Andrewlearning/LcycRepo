# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return

        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # 先让快指针领先k个节点
        for i in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

"""
https://algocasts.io/episodes/eAGQQlG4
这题和寻找 链表的中间节点是同一道题
注意：
1. 我们进行while 循环的时候，要while front.next: 这样front才不会 = None
2. 假如说k 超过链表长度的话，那我们直接返回整个链表就好了
"""
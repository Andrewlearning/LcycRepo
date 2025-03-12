"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
Given a LinkedList, reverse the nodes of a LinkedList k at a time and
return its modified list.

k is a positive integer and is less than or equal to the length of the LinkedList.
 If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Given this LinkedList: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        tail = head
        for i in range(k):
            if not tail:
                return head  # 如果不足 k 个，直接返回原链表
            tail = tail.next
        
        # 反转前 k 个节点
        newHead = self.reverse(head, tail)
        # 因为翻转后变为 newHead -> xx -> head -> next newHead - self.reverseKGroup(tail, k)
        # 递归反转剩余部分
        head.next = self.reverseKGroup(tail, k)
        
        return newHead

    # 反转[head ~ tail)的节点, tail节点不反转
    # head -> n1 -> n2 -> tail
    # head <- n1 <- n2(pre) tail(cur)
    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        pre = None
        cur = head
        
        while cur != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre  # 返回反转后的头节点

"""
时间复杂度： O(n)，每个节点最多访问两次（一次遍历 tail 一次翻转）
空间复杂度： O(n/k)，由于递归调用栈的深度是 n/k。
"""




# 这个做法太麻烦
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 计算链表长度
        length = self.countNum(head)

        # 由于92题特性，我们把链表第一个节点从1开始算
        startFrom = 1

        # 我们持续需要反转 [startFrom, startFrom + k - 1] 这个区间的链表
        # 假如startFrom + k - 1没超过链表长度，则可以继续翻转
        while startFrom + k - 1 <= length:
            head = self.reversePart(head, startFrom, startFrom + k - 1)
            startFrom += k
        return head

    # 92题模板，反转从1开始算，第left个到第right个节点
    def reversePart(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        edge = dummy

        for i in range(left - 1):
            edge = edge.next

        pre = edge.next
        cur = edge.next.next

        for i in range(right - left):
            temp = cur.next

            cur.next = pre
            pre = cur
            cur = temp

        edge.next.next = cur
        edge.next = pre
        return dummy.next

    def countNum(self, head):
        res = 0
        while head:
            head = head.next
            res += 1
        return res

# 古城算法 13:00
# https://www.bilibili.com/video/BV1uB4y1A7N7/?spm_id_from=333.337.search-card.all.click
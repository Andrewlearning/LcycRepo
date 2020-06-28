"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
Given a linked list, reverse the nodes of a linked list k at a time and
return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
 If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # base case
        # 假如说没节点或者只剩下一个节点的话，那么不用进行反转
        if head == None or head.next == None:
            return head

        # 每一轮我们都要指定一个tail节点，它的位置在head走k步后
        tail = head

        for i in range(k):
            # 假如说当前递归，剩余的节点不足k个，那么我们不用进行反转了，返回head
            if not tail:
                return head
            tail = tail.next

        # 答案头
        newHead = self.reverse(head, tail)

        # 1(head)<-2<-3(pre,newHead) 4(tail)
        # 因为我们知道1-3我们已经反转完了，所以我们要把4后面的也反转过去
        head.next = self.reverseKGroup(tail, k)

        return newHead

    # 这个函数，我们从head反转到tail的前一位
    def reverse(self, head, tail):
        pre = None
        cur = head

        while cur != tail:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next

        # 返回反转后的头节点  1<-2<-3(pre) 4(cur,tail)
        return pre



"""
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/di-gui-java-by-reedfan-2/
"""
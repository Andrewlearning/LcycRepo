"""
Reverse a LinkedList from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-LinkedList.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        pre = None
        cur = head

        # 这里，例如是2的话，那我们从位置1开始走，走到2，走一步就好了
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1

        # 在我们翻转完指定范围以后，start的位置 1(start) 2<-3<-4 5
        start = pre
        # 在我们翻转完指定范围以后，start的位置 1(start) 2(tail)<-3<-4  5
        tail = cur

        while n:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next
            n -= 1

        # 1(start) 2(tail)<-3<-4(pre)  5(cur)
        if start:
            start.next = pre


        # 当出现 [3,5] 1 1 这个测试条件的话
        # None(start) 3(tail,pre) 5(cur)
        # 反正走判断完美契合
        else:
            head = pre

        # 1(start) 2(tail)<-3<-4(pre)  5(cur)
        tail.next = cur
        return head

"""
https://leetcode.com/problems/reverse-linked-list-ii/solution/
"""

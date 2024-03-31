"""
Reverse a LinkedList from position l to r. Do it in one-pass.

Note: 1 ≤ l ≤ r ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, l = 2, r = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-LinkedList.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # 因为有可能从头结点开始就要发生翻转，所以我们创建一个dummy节点不影响翻转
        dummy = ListNode(0)
        dummy.next = head
        # edge，翻转区间的前一个节点
        edge = dummy

        for _ in range(left-1):
            edge = edge.next

        # 0 -> 1(edge) -> 2(pre) -> 3(cur) -> 4 -> 5
        pre = edge.next
        cur = edge.next.next
        for _ in range(right-left):
            # 记录下一个节点，方便cur向后移动
            temp = cur.next

            # 真正改变指针方向的就只有这一步
            cur.next = pre

            # pre节点往后移动一格
            pre = cur
            cur = temp

        # 1(edge) <=> 2 <- 3 <- 4(pre) 5(cur)
        # 让2连到了5
        edge.next.next = cur
        # 1(edge) -> 4(pre) -> 3 -> 2 -> 5(cur)
        # 让edge连到了4
        edge.next = pre
        return dummy.next

"""
https://www.acwing.com/video/2612/
"""

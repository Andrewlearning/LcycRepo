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
        # edge，翻转区间的前一个节点, 从dummy开始的原因是和上面一样
        # 当区间翻转完成后，我们用edge.next 和 edge.next.next来连接头尾
        edge = dummy

        for _ in range(left-1):
            edge = edge.next

        # left=2, right=4
        # 0 -> 1(edge) -> 2(pre) -> 3(cur) -> 4 -> 5
        pre = edge.next
        cur = edge.next.next

        # right - left的原因是，例如left=2,right=4,完成这个翻转我们只移动两次指针
        for _ in range(right-left):
            # 记录下一个节点，方便cur向后移动
            temp = cur.next

            # 真正改变指针方向的就只有这一步
            cur.next = pre

            # pre节点往后移动一格
            pre = cur
            cur = temp

        # 0 -> 1(edge) <=> 2 <- 3 <- 4(pre) 5(cur)
        # 让2连到了5
        edge.next.next = cur
        # 0 -> 1(edge) -> 4(pre) -> 3 -> 2 -> 5(cur)
        # 让edge连到了4
        edge.next = pre
        return dummy.next

"""
https://www.acwing.com/video/2612/

206反转链表，需要两个指针 pre, cur
本题需要再在反转部分链表的时候，也需要pre, cur, 而且还需要多一个edge, 放在需要反转区间左边外一个节点，后用于连接反转区间的头尾
"""

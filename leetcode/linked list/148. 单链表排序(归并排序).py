"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        # 把链表分成两半
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # head代表前一半，mid代表后一半
        mid = slow.next
        slow.next = None

        # 分而治之
        left, right = self.sortList(head), self.sortList(mid)

        # 到这一步就是，合并两个有序链表了
        cur = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        cur.next = left if left else right
        return res.next

"""
就是一般归并排序的做法
首先通过快慢指针找到链表的中间节点
然后分出两段链表，分别来进行递归
最后拿到left,right两段排序好的链表，来进行融合
"""

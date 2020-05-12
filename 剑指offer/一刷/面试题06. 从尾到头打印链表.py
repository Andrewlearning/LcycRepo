"""
从尾到头打印链表
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []

        stack = []

        while head:
            stack.insert(0, head.val)
            head = head.next

        return stack




"""
答案：
可以手动写一个list来实现一个stack,每次insert都插入在0的位置，完成先进后出的操作
"""
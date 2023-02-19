class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # 准备dummy是因为有可能要删除头结点
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        # 由于我们要一直使用cur.next去进行判断，所以需要保证它不是空指针
        while cur.next:

            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

"""
"""
"""
比如说，给你的链表是：
1 -> 2 -> 4
它表示整数 124，加 1 等于 125，于是你要返回链表：
1 -> 2 -> 5
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def plusOne(self, head):
        dummy = ListNode(0)
        notNine = dummy
        dummy.next = head

        #把 notNine 指针定位到最后一个非9数，0-1-9-1(notnine)-9-9
        cur = head
        while cur:
            if cur.val != 9:
                notNine = cur
            cur = cur.next

        #把notnine后面的9清空，0-1-9-1(notnine)-9-9  -> 0-1-9-1(notnine)-0-0
        cur = notNine.next
        while cur:
            cur.val = 0
            cur = cur.next


        # 0(dummy)-9-9-9
        # 说明原链表一开始就是9， 我们要进位
        # 1-2-3(notNine)
        # 又或者是这种情况
        notNine.val += 1
        return dummy if dummy == notNine else dummy.next

"""
Time: O(n), Space: O(1)
https://algocasts.io/episodes/nwp8qeW7
"""

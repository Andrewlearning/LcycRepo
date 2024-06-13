# Definition for singly-LinkedList.
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

        # 用dummy的原因是，有可能出现链表只有一个元素的情况，例如 [1] 1, 结果是[]
        dummy = ListNode(0)
        dummy.next = head

        # 我们全程使用slow指针进行操作，fast只是用于帮我们定位slow的位置
        # 例如 head = [1,2,3,4,5], n = 2，我们要删除4，则要让slow移动到3
        #
        # 注意，不能让slow.next与fast连接
        # 要不然例如head=[1] n=1, 移动到最后时，fast此时=1，slow=0, slow.next=head不满足答案
        fast = slow = dummy

        # 先让快指针领先k个节点
        for i in range(k):
            fast = fast.next

        # 为啥这了是fast.next这个边界条件，一般是自己试出来比较清楚
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
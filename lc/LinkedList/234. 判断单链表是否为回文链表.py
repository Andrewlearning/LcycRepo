# Definition for singly-LinkedList.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        # 记录链表长度
        length = 0
        check = head
        while check:
            length += 1
            check = check.next

        # 反转前半段链表
        pre = None
        cur = head
        for _ in range(length // 2):
            temp = cur.next

            cur.next = pre
            pre = cur
            cur = temp

        # 假如说链表长度为奇数，那么我们的cur要往下走一步
        # 1 2 3(cur) 2 1
        if length % 2 == 1:
            cur = cur.next

        # 两种情况, 相互比较就好了
        # 1 <- 2(pre) 2(cur) -> 1
        # 1 <- 2(pre) 3 -> 2(cur)-> 1
        while cur and pre:
            if cur.val != pre.val:
                return False
            cur = cur.next
            pre = pre.next

        return True


"""
https://algocasts.io/episodes/VXGOqWQd
Time: O(n), Space: O(1)
这种方法是最优解，我们先用一个变量来记录链表的总长度
然后反转前半段链表， 然后pre,从中间向左走， cur从中间向右走
一次次来进行比
"""

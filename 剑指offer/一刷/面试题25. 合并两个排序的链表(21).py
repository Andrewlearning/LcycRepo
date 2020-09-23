# Definition for singly-LinkedList.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new = cur = ListNode(0)

        while l1 and l2:

            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next

            elif l1.val > l2.val:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return new.next


if __name__ == "__main__":
    solution = Solution()

"""
其实这题并不怎么难，主要就是语法不够熟悉，算法是极其简单的
答案：
1.我们需要创建一个新的节点，用来串联这两个链表
2.每连接一次，new,phead(1or2)都要同时next,来进行下一步的比较
3.当其中一个节点走完了，退出了循环，我们要记得把new.next = 另一个还没走完的节点
"""
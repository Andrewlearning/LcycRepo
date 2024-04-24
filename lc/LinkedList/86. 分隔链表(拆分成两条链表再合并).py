"""
这个题目说的是，给你一个单链表和一个数字，你要把小于这个数字的节点都移到链表前面，大于等于这个数字的节点都移到链表后面。并且在较小和较大的这两堆节点中，节点之间的相对顺序保持不变。
Given a LinkedList and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
# Definition for singly-LinkedList.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # head less, pointer less
        hl = pl = ListNode(0)
        hg = pg = ListNode(0)

        while head:
            if head.val >= x:
                pg.next = head
                pg = pg.next
            else:
                pl.next = head
                pl = pl.next
            head = head.next

        pg.next = None
        pl.next = hg.next
        return hl.next

"""
Time: O(n), Space: O(1)
答案:
1.创建两条链表，一条储存大于等于的节点，一条储存小于节点
2.然后把小于等于的节点的最尾端，连到大于等于的头
3.把大于等于链表的尾指向None

注意：
1.我们虽然创造了两个新链表，但是还是要给这两个新链表一个新指针，避免找不回头节点
2.注意这里的遍历链表是 while cur != None
"""
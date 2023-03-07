# Definition for singly-LinkedList.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = head

        while cur:
            # p每次都是从链表头开始，然后每次都对比p指向的元素，与cur所在的元素的大小，确认cur要插向哪里
            p = dummy
            # 记录下一个位置
            cur_next = cur.next

            # 对比p所在的元素 与 cur所在的元素的大小
            while p.next and p.next.val <= cur.val:
                p = p.next

            # 假如p -> None, 那么 p -> cur -> None
            # 假如 p -> 2, 那么 p -> 1 ->2
            cur.next = p.next
            p.next = cur

            # 移动到下一个位置
            cur = cur_next

        return dummy.next
"""
Time: O(n^2), Space: O(1)
https://algocasts.io/episodes/XZWvVNW7
答案：
1.这题使用了插入排序，于此同时我们要新建一个链表来存放排序好的node
2. 插入排序的做法就是，把无序区的元素一个个拿出来，放到有序区一个个位置来对比，最后插入到合适的位置

  本题插入做法  p -> p.next ,  p -> cur -> p.next
3.我们用cur_next 来储存原链表的进度,用于找到无序区的下一个元素
4.注意 while 那里，要先把p.next != None 先进行判断，因为and 是从左执行到右边的

"""
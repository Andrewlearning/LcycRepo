"""
Given a LinkedList, rotate the list to the right by k places, where k is non-negative.

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        # 第一步，先数出链表的长度
        n = 1
        tail = head
        while tail.next != None:
            tail = tail.next
            n += 1

        # 第二步，把链表的首尾链接起来
        tail.next = head

        # 第三步，考虑到k大于长度的情况，那么我们就先取余
        # 假如翻转的次数是链表长度的倍数，那么说明翻转后结果一样，直接返回
        k = k % n
        if k == 0:
            return head

        # 第四步， 就是那出新指针要指向的点，其中有newend, newhead
        newend = head
        # 1->2->3->4->5->, k = 2
        # 假如我们要翻转的话，就得让4作为head, 这刚好就是n - k = index 3, 这就是4的位置
        # 但是我们这里是要先找到newend, 所以就是走到n - k - 1的位置
        # 最后从0 走到 n-k-1 需要走n-k-2步
        for _ in range(n - k - 1):
            newend = newend.next

        # 把newhead放在 newend的下一个位置
        newhead = newend.next

        # 把新链表的最后一个节点，指向空
        newend.next = None

        return newhead
"""
// Time: O(n), Space: O(1)
我感觉这题和双指针的关系并不大把
1.一开始我们先要计算出链表的长度，利用count指针。数到最后记得要把末节点的和头节点连起来
2.我们要对k 取膜，是用来应对 k > n的情况，避免过度循环
3.定的新链表指针，newend,把它遍历到 n - k的位置
（注意，因为newend一开始就等于在0的位置，所以我们遍历到n-k-1就好了）
4.找到new end,把newend.next 设成新的头
5.然后newend指向空，完成新链表
"""
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
        length = 1
        toend = head
        while toend.next != None:
            toend = toend.next
            length += 1

        # 第二步，把链表的首尾链接起来
        toend.next = head

        # 第三步，考虑到k大于长度的情况，那么我们就先取余
        k = k % length

        # 第四步， 就是那出新指针要指向的点，其中有newend, newhead
        newend = head
        # 1->2->3->4->5->, k = 2
        # 假如我们要翻转的话，就得让4作为head, 这刚好就是length - k = index 3, 这就是4的位置
        # 但是我们这里是要先找到newend, 所以就是走到length - k - 1的位置
        # 最后从0 走到 length-k-1 需要走length-k-2步
        for _ in range(length - k - 1):
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
2.我们要对k 取膜，是用来应对 k > length的情况，避免过度循环
3.定的新链表指针，newend,把它遍历到 n - k的位置
（注意，因为newend一开始就等于在0的位置，所以我们遍历到n-k-1就好了）
4.找到new end,把newend.next 设成新的头
5.然后newend指向空，完成新链表
"""
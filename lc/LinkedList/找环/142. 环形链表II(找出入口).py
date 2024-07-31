"""
https://leetcode.com/problems/linked-list-cycle-ii/
Given a LinkedList, return the node where the cycle begins.
If there is no cycle, return null.

To represent a cycle in the given LinkedList, we use an integer pos which represents the position (0-indexed) in the LinkedList where tail connects to. If pos is -1, then there is no cycle in the LinkedList.

Note: Do not modify the LinkedList.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the LinkedList, where tail connects to the second node.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        fast = head
        slow = head

        """
        退出循环有两种情况
        1. fast = slow, 这说明找到了相交节点
        2. fast = None or fast.next = None, 这说明没找到相交节点，说明链表没环
        """
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        # 链表没环的情况
        if fast is None or fast.next is None:
            return

        # 有数学证明，比较麻烦
        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return fast






"""

查看环状链表的入口节点
还是使用快慢指针：
1。若快慢指针能走完全程，则说明没有环，返回-1
2。若没走完，且在环内相遇，则把快慢指针的其中一个设为头节点，然后两个指针一步一步走
走到相遇的地方就是环的入口



"""
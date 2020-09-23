"""

Given a LinkedList, swap every two adjacent nodes
and return its head.

You may not modify the values in the list's nodes,
only nodes itself may be changed.

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-LinkedList.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case, 假如说递归到最后，没有节点，或者是只有一个节点
        if head is None or head.next is None:
            return head

        # 1(cur) -> 2(next)  (3 4)
        cur = head
        next = cur.next

        # 1(cur) <- 2(next)  (3 4)
        cur.next = self.swapPairs(next.next)
        next.next = cur

        return next




"""
Time O(n) SpaceO(n)
https://algocasts.io/episodes/deG4e9p1
"""
if __name__ == "__main__":
    solution = Solution()
    # solution.swapPairs(3)
    solution.prt()

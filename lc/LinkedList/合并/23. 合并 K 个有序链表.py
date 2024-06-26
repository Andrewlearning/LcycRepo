# Definition for singly-LinkedList.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


from heapq import heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 最小堆
        heap = []
        for node in lists:
            if node:
                heappush(heap, (node.val, node))

        res = cur = ListNode(0)
        while heap:
            # 每次把heap中值最小的节点pop出，加入到答案中
            val, node = heappop(heap)
            # 假如node这一条链表还有next，则继续加入到heap中
            if node.next:
                heappush(heap, (node.next.val, node.next))

            cur.next = node
            cur = cur.next
        return res.next


"""
Time: O(n*log(k)), Space: O(k)
"""

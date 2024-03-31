"""
Given the head of a linked list, we repeatedly delete consecutive sequences of
 nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.
You may return any such answer.

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
"""
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        preFix = 0
        dummy = ListNode(0)
        dummy.next = head
        m = {}

        cur = dummy
        # 每次都把当前的(前缀合, 对应的节点) 存在map里
        while cur:
            preFix += cur.val
            m[preFix] = cur  # 相同的preFixSumn只保留最后一个
            cur = cur.next

        preFix = 0
        cur = dummy
        while cur:
            preFix += cur.val
            # 假如我们找到两个前缀和一样的节点，说明这两个节点之间的节点和为0
            # 应该直接跳过
            # list:   [1,2,-3,3,1]
            # prefix: [1,3, 0,3,1]
            # 我们可以发现在[-3,3]应该被剔除，所以应该把 [1,2,  1]连起来
            cur.next = m[preFix].next
            cur = cur.next

        return dummy.next

"""
古城算法 16:22
https://www.bilibili.com/video/BV1e5411c7JR/?spm_id_from=333.999.0.0&vd_source=b81616a45fd239becaebfee25e0dbd35
"""
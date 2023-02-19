class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        # pre代表是无重复链表
        pre = dummy
        # cur是探测是否有重复的指针
        cur = head

        while cur and cur.next:
            # 当cur检测到重复
            if cur.val == cur.next.val:
                temp = cur.val
                # 一直让cur移动到不重复区域
                while cur and temp == cur.val:
                    cur = cur.next
                # 让pre连接到不重复区域
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next

        return dummy.next

"""
古城算法 7:00
https://www.bilibili.com/video/BV1e5411c7JR/?spm_id_from=333.999.0.0&vd_source=b81616a45fd239becaebfee25e0dbd35
"""
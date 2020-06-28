class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        # cur放的元素，都是完全不重复的元素
        cur = dummy = ListNode(0)
        dummy.next = head


        while cur.next and cur.next.next:

            # 当我们发现前面两个元素相同的时候
            if cur.next.val == cur.next.next.val:

                # 我们记录下相同值，这个值，我们要让cur.next不再触碰到
                same_value = cur.next.val

                # 所以当cur.next.val = same_value时，我们一直移动cur.next
                while cur.next and cur.next.val == same_value:
                    cur.next = cur.next.next

                # 结束以后，cur.next跳过了第一个重复的值
                # 但是有可能出现 3,3,4,4这种情况。我们只跳过了3
                # 所以我们要交给下一次的cur.next.val == cur.next.next.val来判断

            else:
                cur = cur.next

        return dummy.next

"""
https://www.youtube.com/watch?v=w16pq8_DVno
"""
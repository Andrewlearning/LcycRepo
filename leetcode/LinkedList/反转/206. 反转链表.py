"""
反转链表
Reverse a singly LinkedList.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

      1->2->3->4->5->NULL

 pre<-1 2->3
     cur

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        cur = head
        pre, next = None, None
        while cur:
            # 记录下一个节点，方便cur向后移动
            next = cur.next

            # 真正改变指针方向的就只有这一步
            cur.next = pre

            # pre节点往后移动一格
            pre = cur
            cur = next

        # 循环结束时，cur=None, pre移动到链表的最后一格
        return pre


if __name__ == "__main__":
    solution = Solution()
    solution.reverseList()

"""
答案：
 pre->1->2->3->4->5->NULL
      cur

 None<-1  2->3
      pre   cur

1.先把cur.next = pre = None。其实这就完成了我们的目的了
2.把pre, cur都往前挪一个node

注意：
这里的连续赋值，要先把最要紧的先赋值完（就是第一步），然后再赋值后面两个
因为在class这种情况下，右边的值会产生改变，所以保险起见先把必须完成的写了
不太推荐这种写法
"""

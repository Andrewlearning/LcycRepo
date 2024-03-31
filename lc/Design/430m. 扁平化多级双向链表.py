"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, pre, next, child):
        self.val = val
        self.pre = pre
        self.next = next
        self.child = child
"""

class Solution(object):

    def flatten(self, head):
        if not head:
            return head

        # 为了满足dfs的条件，创造一个空头
        dummy = Node(None, None, head, None)
        self.helper(dummy, head)


        dummy.next.pre = None
        return dummy.next


    def helper(self, pre, cur):
        """ return the tail of the flatten list """
        if not cur:
            return pre

        cur.pre = pre
        pre.next = cur

        # 暂时记录cur的next, 因为假如说cur有child的话，则要往深处递归
        tempNext = cur.next

        # 往深处递归，假如说没有child，则不会进行任何操作
        # 有child,则会让 cur->child连起来
        tail = self.helper(cur, cur.child)

        # 操作完后，我们得到一个扁平的双链表，tail是双链表的最后一个元素
        # 然后我们要把当前的child设成None
        cur.child = None

        # 再把tail 和 tempNext连起来
        return self.helper(tail, tempNext)


# https://www.acwing.com/video/1832/思路

# 链接：https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/solution/bian-ping-hua-duo-ji-shuang-xiang-lian-biao-by-lee/
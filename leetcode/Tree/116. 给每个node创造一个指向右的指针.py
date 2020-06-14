"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        level_start = root

        while level_start:
            cur = level_start

            while cur:
                # 处理cur的左节点，让它指向cur的右节点
                if cur.left:
                    cur.left.next = cur.right

                # 处理cur的右节点，然它指向cur同层的右边节点
                # 所以我们这里还要判断 cur同层的右边节点存不存在
                if cur.right and cur.next != None:
                    cur.right.next = cur.next.left

                # 处理完同层最左边的，开始向同层的右边走，处理下一个
                cur = cur.next

            # 当同层的处理完了，就去下一层
            level_start = level_start.left

        return root

# Time: O(n), Space: O(1)
# https://algocasts.io/episodes/Q2preyGz

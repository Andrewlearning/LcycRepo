"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

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

        if not root:
            return None

        # cur 是用于遍历本层
        cur = root

        while cur:
            # 这是cur下一层的参数
            # nextLevelHead是下一层的最左节点，tail是最右节点
            nextLevelHead = tail = Node(0)

            # 利用cur从左往右遍历，帮下一层的节点.next连接起来
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                # 移动到同层右边一个位置
                cur = cur.next

            cur = nextLevelHead.next

        return root

# acwing: https://www.acwing.com/activity/content/code/content/405342/
# 116题可用相同做法
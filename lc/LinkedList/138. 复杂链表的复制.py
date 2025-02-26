"""
复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# O(n) space 写法
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # hashmap key=old node, value=new node
        hashmap = {}

        cur = head
        # 第一次遍历，先复制每个节点的值
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next

        # 第二次遍历，复制每个节点的next 和 random
        cur = head
        while cur:
            # 注意, cur.next和cur.random有可能是None
            if cur.next != None:
                hashmap[cur].next = hashmap[cur.next]
            if cur.random != None:
                hashmap[cur].random = hashmap[cur.random]
            cur = cur.next

        return hashmap.get(head, None)


# 古城算法28:20
# https://www.bilibili.com/video/BV1e5411c7JR/?spm_id_from=333.337.search-card.all.click&vd_source=b81616a45fd239becaebfee25e0dbd35

# O(1) space写法
class Solution1(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        # 1.复制
        node = head
        while node:
            new_node = Node(node.val)
            new_node.next = node.next

            node.next = new_node
            node = new_node.next

        # 2.把复制节点的随机指针赋值
        node = head
        while node and node.next:
            node.next.random = node.random.next if node.random else None
            node = node.next.next

        # 3.分拆 旧链表和新链表
        node = head  # A->B->C
        new_node = head.next  # A'->B'->C'
        res = head.next
        while node:
            node.next = node.next.next
            new_node.next = new_node.next.next if new_node.next else None
            node = node.next
            new_node = new_node.next
        return res


"""

*解题思路：
*1、遍历链表，复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
*2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
*3、拆分链表，将链表拆分为原链表和复制后的链表

"""

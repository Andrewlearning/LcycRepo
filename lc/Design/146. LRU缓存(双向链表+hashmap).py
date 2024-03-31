"""
运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

"""
class DLinkedNode:
    def __init__(self, key, value, pre, next):
        self.key = key
        self.val = value
        self.pre = pre
        self.next = next
        # head.pre  最晚创建的节点，最新的节点
        # head      最早创建的节点
        # head.next 第二早创建的节点


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = DLinkedNode(-1, -1, None, None)
        self.dic = {}
        cur = self.head
        # 我们已经有了head节点, 我们则还要创造 capacity-1个节点
        for i in range(capacity - 1):
            cur.next = DLinkedNode(-1, -1, cur, None)
            cur = cur.next

        # 双向链表首尾相连
        cur.next = self.head
        self.head.pre = cur

    # get和push节点后，都要把该节点移动到head.pre的位置，这个位置代表最近被访问过的节点
    def move2HeadPre(self, cur):
        # 假如说我们要处理的节点，刚好是head
        # 那么我们就把head，变为最新的节点(head.pre)，把head.next作为新的head节点
        if cur == self.head:
            self.head = self.head.next
            return

        # 解除指向cur的指针, 让cur.pre 和 cur.next相互连接
        cur.pre.next = cur.next
        cur.next.pre = cur.pre

        # 把cur节点放在 head 和 head.pre之间，表明cur现在变成最新节点
        cur.pre = self.head.pre
        cur.pre.next = cur

        cur.next = self.head
        cur.next.pre = cur

    # O(1) 时间复杂度
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 要获取的节点不存在
        if key not in self.dic:
            return -1

        cur_node = self.dic[key]
        self.move2HeadPre(cur_node)
        return cur_node.val

    # O(1) 时间复杂度
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 假如说我们要插入的节点存在，更新它的value后，再把它挪到head.pre就好
        if key in self.dic:
            cur_node = self.dic[key]
            cur_node.val = value
            self.move2HeadPre(cur_node)
        # 假如要插入的值是新值
        else:
            # 我们要看当前头节点是否有值
            # 如果有值，那么把它给清空，因为head是最老的值，要把它替换掉放最新的值
            if self.head.val != -1:
                del self.dic[self.head.key]

            self.head.key = key
            self.head.val = value
            self.dic[key] = self.head

            # head往前移动一个节点，指向第二久未使用的节点
            self.head = self.head.next


# https://algocasts.io/episodes/rLmP8moY
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
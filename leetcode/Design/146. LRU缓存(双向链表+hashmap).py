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

        # 首尾相连
        cur.next = self.head
        self.head.pre = cur

    # 把我们要处理的节点移动到头部
    def move2head(self, cur):
        # 假如说我们要处理的节点，刚好是头节点
        # 那么我们就把head指针，移动到最久未遍历的节点就好了
        if cur == self.head:
            self.head = self.head.pre
            return

            # 把指向cur节点的指针移动开
        cur.pre.next = cur.next
        cur.next.pre = cur.pre

        # 再把cur节点插入到头部后面
        # 先把cur与原来第一个元素相连
        cur.next = self.head.next
        cur.next.pre = cur

        # 再把cur与head相连
        cur.pre = self.head
        self.head.next = cur

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 要获取的节点不存在
        if key not in self.dic:
            return -1

        cur_node = self.dic[key]
        self.move2head(cur_node)
        return cur_node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 假如说我们要插入的节点存在，更新它的value后，再把它挪到头部就好
        if key in self.dic:
            cur_node = self.dic[key]
            cur_node.val = value
            self.move2head(cur_node)
        # 否则要插入的值是新值
        else:
            # 我们要看当前头节点是否有值
            # 如果有值，那么把它给清空，因为要放新的值
            if self.head.val != -1:
                del self.dic[self.head.key]

            self.head.key = key
            self.head.val = value
            self.dic[key] = self.head

            # head往前移动一个节点，指向最久未使用的节点
            self.head = self.head.pre


# https://algocasts.io/episodes/rLmP8moY
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 本题，创建双向链表的时候是顺时针创建
# 但是插入节点的时候，是逆时针插入，所以就是说head是最久未被访问的节点，head.pre是第二久未被访问的节点
# 双向链表节点
class DLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 哈希表，存储键到{key, node}的映射
        self.head = DLinkedNode(0,0)  # 头节点，head.next放最久未使用的节点
        self.tail = DLinkedNode(0,0)  # 尾节点, tail.pre放着最近被访问的节点

        # head -> 最久未使用 -> xx -> 最近被使用 -> tail
        # 首尾节点相连
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果键存在，获取节点并将其移动到链表尾部（表示最近使用）
        node = self.cache[key]
        self.moveToTail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果键已存在，更新值并将其移动到链表尾部
            node = self.cache[key]
            node.value = value
            self.moveToTail(node)
        else:
            # 如果键不存在，创建新节点并添加到链表尾部
            if len(self.cache) >= self.capacity:
                # 如果缓存已满，移除链表头部的节点（最久未使用）
                removedNode = self.removeHead()
                del self.cache[removedNode.key]
            
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self.addToTail(newNode)

    # 将节点添加到tail和tail.pre中间
    def addToTail(self, node) -> None:
        """将节点添加到tail和tail.pre中间"""
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node

    # 从链表中移除节点
    def removNode(self, node) -> None:
        node.pre.next = node.next
        node.next.pre = node.pre

    # 将节点移动到链表尾部
    def moveToTail(self, node) -> None:
        self.removNode(node)
        self.addToTail(node)

    # 移除head.next并返回它
    def removeHead(self) -> DLinkedNode:
        node = self.head.next
        self.removNode(node)
        return node

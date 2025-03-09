package lc.Design;

import java.util.*;

class DNode {
    int key, value;
    DNode prev, next;
    
    public DNode(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

class LRUCache {
    private int capacity;
    private Map<Integer, DNode> cache;
    private DNode head, tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new HashMap<>();
        
        head = new DNode(0, 0);
        tail = new DNode(0, 0);
        head.next = tail; // 头节点，head.next放最久未使用的节点
        tail.prev = head; // 尾节点, tail.pre放着最近被访问的节点
        // head -> 最久未使用 -> xx -> 最近被使用 -> tail
    }

    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        DNode node = cache.get(key);
        moveToTail(node);
        return node.value;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            DNode node = cache.get(key);
            node.value = value;
            moveToTail(node);
        } else {
            if (cache.size() >= capacity) {
                DNode removedNode = removeHead();
                cache.remove(removedNode.key);
            }
            DNode newNode = new DNode(key, value);
            cache.put(key, newNode);
            addToTail(newNode);
        }
    }

    private void addToTail(DNode node) {
        node.prev = tail.prev;
        node.next = tail;
        tail.prev.next = node;
        tail.prev = node;
    }

    private void removeNode(DNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void moveToTail(DNode node) {
        removeNode(node);
        addToTail(node);
    }

    private DNode removeHead() {
        DNode node = head.next;
        removeNode(node);
        return node;
    }
}

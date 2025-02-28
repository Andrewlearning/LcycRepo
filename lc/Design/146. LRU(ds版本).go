type DNode struct {
    key string
    value string
    pre *DNode
    nxt *DNode
}

type LRUCache struct {
    capacity int
    cache map[string]*DNode
}


func Constructor(capacity int) LRUCache {
    return LRUCache {
        capacity: capacity,
        cache: make(map[string]*DNode)
    }
}


func (this *LRUCache) Get(key int) int {

}


func (this *LRUCache) Put(key int, value int)  {

}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.

int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.

void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
"""

from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        # 我们不对cap进行修改，只是用于判断是否已经装满
        self.cap = capacity
        self.keyToValue = {}
        self.keyToFreq = {}

        """
        freqToKeys:
        1 -> {key1:None, key2:None} (按照元素的插入顺序来排序)
        2 -> {key3:None, key4:None}
        ...
        n -> {keyx:None}
        """
        self.freqToKeys = defaultdict(OrderedDict)
        self.minFreq = 0

    # 已存在的key被get或update时，更新它的频率
    # 1. 删除这个key之前对应的freq数据结构 - keyToFreq, freqToKeys，以及更新minFreq
    # 2. 更新这个key对应的freq
    def update(self, key):
        freq = self.keyToFreq[key]
        del self.freqToKeys[freq][key]

        # 假如这个freq里面已经没有元素了
        # 则把这个freqMap中这个freq给删除
        # 并更新self.minFreq
        if len(self.freqToKeys[freq]) == 0:
            del self.freqToKeys[freq]
            if freq == self.minFreq:
                self.minFreq += 1

        self.keyToFreq[key] = freq + 1
        self.freqToKeys[freq + 1][key] = None


    # if key not exist, return -1
    # if key exist, update freq & return value
    def get(self, key: int) -> int:
        if key not in self.keyToValue:
            return -1

        self.update(key)
        return self.keyToValue[key]


    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return None

        # 假如key已经存在，那么只用去更新value 和它的freq
        if key in self.keyToValue:
            self.keyToValue[key] = value
            self.update(key)

        # 假如key不存在
        # 假如已满，则需要清理掉freq最低的元素
        # 假如未满，则插入到所有数据结构以及minFreq
        else:
            if len(self.keyToValue) == self.cap:
                # pop出最早插入orderedDict的元素
                evictKey, _ = self.freqToKeys[self.minFreq].popitem(last=False)
                del self.keyToValue[evictKey]
                del self.keyToFreq[evictKey]
            self.keyToValue[key] = value
            self.keyToFreq[key] = 1
            self.minFreq = 1
            self.freqToKeys[self.minFreq][key] = None


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
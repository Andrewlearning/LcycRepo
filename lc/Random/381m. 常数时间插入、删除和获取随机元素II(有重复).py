"""
设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。

注意: 允许出现重复元素。

insert(val)：向集合中插入元素 val。
remove(val)：当 val 存在时，从集合中移除一个 val。
getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。

/ 初始化一个空的集合。
RandomizedCollection collection = new RandomizedCollection();

// 向集合中插入 1 。返回 true 表示集合不包含 1 。
collection.insert(1);

// 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
collection.insert(1);

// 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
collection.insert(2);

// getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
collection.getRandom();

// 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
collection.remove(1);

// getRandom 应有相同概率返回 1 和 2 。
collection.getRandom();
"""

from collections import defaultdict
from random import randint


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 记录出现现过什么数字
        self.nums = []
        # 因为这里有可能出现重复的数字，所以我们要用一个set来保存该数组的每一个Index
        self.hashmap = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.hashmap[val].add(len(self.nums))
        self.nums.append(val)

        # 题目要求，假如说插入一个之前没有的数字，return True, 否则return False
        return len(self.hashmap[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.hashmap[val]:
            return False

        # 我们从set里面随机取出一个val的下标
        delete_index = self.hashmap[val].pop()

        # 取出数组最后一个元素
        last_value = self.nums[-1]

        # 我们把最后一个元素，覆盖到我们要删除的元素上，这样就完成了O(1)的删除了
        self.nums[delete_index] = last_value

        # 更新和删除原有下标
        self.hashmap[last_value].add(delete_index)
        self.hashmap[last_value].discard(len(self.nums) - 1)

        # 把最后一个元素pop()出
        self.nums.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        # 利用下标随机取一个数字，O(1)
        return self.nums[randint(0, len(self.nums) - 1)]

"""
相对于380的改变，有重复数字
1.这就意味着，一个val,有多个对应的index,与此同时，我们还要保证它的remove是O（1），所以我们要用set作为value的数据结构
  self.hashmap[last_value].discard(len(self.nums) - 1)，在这里就体现出用set()时间复杂度上的好处了

2.其他内容基本上和380一样


"""
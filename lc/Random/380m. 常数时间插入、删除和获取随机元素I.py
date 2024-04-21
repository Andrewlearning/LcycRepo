"""
380. Insert Delete GetRandom O(1)
设计一个支持在平均时间复杂度 O(1)下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

使这三个方法的时间复杂度都是O(1)
"""
from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # hashmap插入，删除都是O(1), 但是无法做到随机查找元素
        # arraylist插入，删除头尾节点都是O(1), 但是删除中间元素是O(n)
        # 所以这题我们要借助
        # hashmap的插入删除的O(1), 还要借用list可以完成的随机查找元素

        # key:元素  value:该元素下标
        self.hashmap = {}
        # 把每个在hashmap存在的元素都加进来，用于做随机处理
        self.nums = []
        # 实时记录self.nums的长度，避免使用len(), 降低时间复杂度
        self.n = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # 假如不在数据结构内，那么要把元素加进去
        if val not in self.hashmap:
            self.nums.append(val)
            # 记录新加进去元素的下标
            self.hashmap[val] = len(self.nums)-1
            self.n += 1
            return True

        # 假如在里面，return False
        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            # 我们取出要删除元素的下标
            deleteIndex = self.hashmap[val]

            # 取出数组最后一个元素
            lastVal = self.nums[-1]

            # 我们把最后一个元素，覆盖到我们要删除的元素上，这样就完成了O(1)的删除了
            self.nums[deleteIndex] = lastVal

            # 更新和last_value的下标
            self.hashmap[lastVal] = deleteIndex

            # 把多余的last_value 给pop()掉，因为它已经附值在val之前的index上了
            self.nums.pop()
            self.n -= 1

            # 把hashmap 中把 val给去掉
            del self.hashmap[val]

            return True

        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[randint(0,self.n-1)]

"""
https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
答案：
1.这题就看出来了两种数据结构了
2. list,查找是n,pop,append是1， hashmap,查找,pop,append都是O（1）
3. 所以在insert和remove里，我们要看val在不在数据结构以内，我们要用hashmap来查找
因为是O（1），而not in list的话，时间复杂度是O(n)

4.remove 这个函数的处理方法有点巧妙， 我们得先把val 的index , 和nums[-1] 的val找出来
    把val放在nums的位置上，同时把val在字典中的位置换成num[-1]
    然后再pop（）
"""
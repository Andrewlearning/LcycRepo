"""
 Init a singly LinkedList [1,2,3].
 getRandom() should return either 1, 2, or 3 randomly.
Each element should have equal probability of returning. solution.getRandom();
以相同的概率返回回链表里的任意一个node
"""
import random
class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        count = 0
        reserve = 0
        cur = self.head
        while cur:
            count += 1
            rand = random.randint(1, count)

            # 当我们满足第n个元素，有1/n的概率被选中时，这时候才满足每个节点被选的概率是一样的
            if rand == count:
                # 然后我们一开始1的被选概率是100%，所以能确保答案是正确的
                reserve = cur.val
            cur = cur.next
        return reserve

"""
答案：
1.这题的思想和398基本一样，注意count++的位置，因为cur = head的时候，count就已经=1了，
                                        所以当cur = head.next的时候，count就要是2了
                                         
"""
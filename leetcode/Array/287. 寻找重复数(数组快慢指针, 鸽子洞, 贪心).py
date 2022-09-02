"""
给定一个包含n + 1 个整数的数组nums，其数字都在 1 到 n之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""
# 数组的快慢指针法
# Time: O(n), Space: O(1)
class Solution2(object):
    def findDuplicate(self, nums):
        if nums is None or len(nums) == 0:
            return None

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
"""
算法：
如果数组中没有重复的数，以数组 [1,3,4,2]为例，我们将数组下标 n 和数 nums[n] 建立一个映射关系 f(n)f(n)，
其映射关系 n->f(n)为：
0->1
1->3
2->4
3->2
我们从下标为 0 出发，根据 f(n)f(n) 计算出一个值，以这个值为新的下标，再用这个函数计算，以此类推，直到下标超界。这样可以产生一个类似链表一样的序列。
0->1->3->2->4->null

如果数组中有重复的数，以数组 [1,3,4,2,2] 为例,我们将数组下标 n 和数 nums[n] 建立一个映射关系 f(n)f(n)，
其映射关系 n->f(n) 为：
0->1
1->3
2->4
3->2
4->2
同样的，我们从下标为 0 出发，根据 f(n)f(n) 计算出一个值，以这个值为新的下标，再用这个函数计算，以此类推产生一个类似链表一样的序列。
0->1->3->2->4->2->4->2->……
这里 2->4 是一个循环

从理论上讲，数组中如果有重复的数，那么就会产生多对一的映射，这样，形成的链表就一定会有环路了，

综上
1.数组中有一个重复的整数 <==> 链表中存在环
2.找到数组中的重复整数 <==> 找到链表的环入口

至此，问题转换为 142 题。那么针对此题，快、慢指针该如何走呢。根据上述数组转链表的映射关系，可推出
142 题中慢指针走一步 slow = slow.next ==> 本题 slow = nums[slow]
142 题中快指针走两步 fast = fast.next.next ==> 本题 fast = nums[nums[fast]]

链接：https://leetcode.cn/problems/find-the-duplicate-number/solution/287xun-zhao-zhong-fu-shu-by-kirsche/
"""

"""
当然，这题也可以用贪心做法来做, 具体可以参考41题
主要是找到下标与数字的关系，我们这里的对应关系是下标0->1 , 下标1->2
然后通过贪心算法，不断地进行重试，直到尝试到当前下标的数是满足我们的匹配需求为止
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            # 我们希望 下标0->1, 下标1->2 ...
            # 既是希望 i = nums[i] - 1
            # 既是说我们希望 i 上的这个数 放在nums[i] - 1 这个位置上
            # 所以当 nums[i] != nums[nums[i] - 1]，表明没有满足下标和数的对应关系

            # 什么数，应该放在位置i呢？
            # 1. 满足条件的数 nums[i] = nums[nums[i] - 1]
            # 2. 没有 不可能通过交换使合理的数，所以这里就不用写了
            while nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)

        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


"""
在未排序的数组中找到第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
这里的k是从1开始算的

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""


class Solution:
    def findKthLargest(self, nums, k):
        # 在得出答案的时候，nums = [>=k的元素从大到小排 | <k的元素乱序]
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, nums, l, r, k):
        # 找到最后了，说明数组已经被排序成nums = [>=k的元素从大到小排 | <k的元素乱序]
        # 这是因为因为我们只对我们想找的区间进行排序
        # 所以我们直接返回nums[k]，这个元素必然是第k大的元素
        # 到这里，l = r = k，因为我们不断在缩小范围寻找k
        if l == r:
            return nums[k]

        pivot = nums[l]
        # 可以看下面的判断，不这样写会越界，同时这也是模板
        # 因为在进入循环的时候i要先+=1, 所以得先在外面抵消一次，j同理
        i = l - 1
        j = r + 1

        # 最终效果 [大于等于pivot的区间 | 小与等于pivot的区间]
        while i < j:
            # 从左往右找到 <= pivot的数
            # += 1 是因为走完一轮循环后，第二轮循环得切换到下一个数开始判断
            i += 1
            while nums[i] > pivot:
                i += 1

            # 从右往左找到 >= pivot的数
            j -= 1
            while nums[j] < pivot:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        # j在出循环后，是位于[大于等于pivot的区间]的最后一个元素
        # 因为假如j在遍历的时候一直找不到比pivot小的元素，那就会直接找到左区间的最后一位去了，然后到那里的时候也意味着 j > i了

        # k <= j, 说明第K大的元素在 [大于等于pivot的区间] 内
        if k <= j:
            return self.quickSelect(nums, l, j, k)
        # k > j, 说明第K大的元素在 [小与等于pivot的区间] 内
        return self.quickSelect(nums, j + 1, r, k)

# 快速选择的时间复杂度是O(n) n + n/2 + n/4... = n + n = 2n
# n/2 + n/4 + ... + n/2**n 这是一个等比数列求和问题，有计算公式，最后得到的解是 < 1的
# 链接：https://www.acwing.com/video/1589/

"""
如何变成找到数组中第K小的元素, 把i,j根据什么元素交换，调整下就好
while i < j:
    i += 1
    while nums[i] < pivot:
        i += 1

    j -= 1
    while nums[j] > pivot:
        j -= 1
    
    swap()

"""

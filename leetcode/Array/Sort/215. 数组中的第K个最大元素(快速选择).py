"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
这里的k是从1开始算的

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""
class Solution:
    def findKthLargest(self, nums, k):
        # 这个排序是从小往大排，我们要找到第k大的元素
        # 这里的k是从1开始算的
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def quick_select(self, nums, l, r, k):
        if l >= r:
            return nums[l]

        pivot = nums[l]
        i = l - 1
        j = r + 1
        while i < j:
            while True:
                i += 1
                if nums[i] >= pivot:
                    break

            # 从右边找到 <= pivot的数
            while True:
                j -= 1
                if nums[j] <= pivot:
                    break

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        lenj = j - l + 1

        if k <= lenj:
            return self.quick_select(nums, l, j, k)
        return self.quick_select(nums, j + 1, r, k - lenj)

# 快速选择的时间复杂度是O(n) n + n/2 + n/4... = n + n = 2n
# 链接：https://www.acwing.com/activity/content/code/content/453030/
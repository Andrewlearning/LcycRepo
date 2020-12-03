class Solution(object):
    def reversePairs(self, nums):

        self.sortedTemp = []
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, l, r):
        # 不存在的情况
        if l >= r:
            return 0

        # 分而治之，res得到的是这两个函数里的逆序对和有多少
        mid = l + r >> 1
        res = self.merge_sort(nums, l, mid) + self.merge_sort(nums, mid + 1, r)

        # 经过上面一步merge以后, 左右两半分别都已经从小到大排好序了
        j = mid + 1
        for i in range(l, mid + 1):
            # 假如说当前nums[j]不满足逆序对，那么则++
            while j <= r and nums[j] * 2 < nums[i]:
                j += 1
            # 找到满足nums[i] nums[j]是逆序对的j, 那么比nums[j]小的数也可以和nums[i]构成逆序对
            # 所以我们可以从[mid+1,j] 的所有数都加进逆序对
            res += j - (mid + 1)

        # 清空之前使用的排序好的数组
        self.sortedTemp = []

        # 进行归并排序
        i = l;
        j = mid + 1
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                self.sortedTemp.append(nums[i])
                i += 1
            else:
                self.sortedTemp.append(nums[j])
                j += 1

        # 把剩下的未放进排序数组的元素，加入排序数组
        if i <= mid:
            self.sortedTemp += nums[i:mid+1]
        if j <= r:
            self.sortedTemp += nums[j:r+1]

        # 最后，得到排序后的[l,r]后，inplace更新原数组
        i = l
        for j in range(len(self.sortedTemp)):
            nums[i] = self.sortedTemp[j]
            i += 1

        # 返回从[l,r]的所有逆序对
        return res

# https://www.acwing.com/video/1896/
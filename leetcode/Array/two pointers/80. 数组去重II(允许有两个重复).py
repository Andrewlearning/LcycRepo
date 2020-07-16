class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) == 0:
            return 0

        # 排序数组, 所以我们顺序遍历就好了
        # l 记录没有重复的下标
        l = 0

        # r 是用来遍历的，同时作为去重的手段
        r = 0

        while r < len(nums):

            # 我们在上一次循环里，已经让r落在一个没有重复数字的位置上，然后在这里进行填充
            nums[l] = nums[r]

            # 把r移动到重复数字的最后一位 例如 "11113" r的位置就移动到3前面两位 1 1 1(r) 13
            while r + 2 < len(nums) and nums[r] == nums[r + 2]:
                r += 1

            # 指向下一个填充的位置
            # 1 1 1 1(r) 3
            l += 1
            r += 1

            # 这里的1，会被填充两次，第一次是从上一个数字进入到1的范围，第二次是从1的范围出去的时候

        return l
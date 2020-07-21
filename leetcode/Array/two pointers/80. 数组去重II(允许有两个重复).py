class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums and len(nums) == 0:
            return 0

        # 排序数组, 所以我们顺序遍历就好了
        # l 记录没有重复的下标
        l = 0

        # r 是用来遍历的，同时作为去重的手段
        r = 0

        # 假如说r循环过后，我们要判断r是否会越界，才能给l赋值
        while r < len(nums):

            # l的第一次赋值是，r刚进入重复数值期间
            # l的第二次赋值是，r在重复数值区间的最后一位
            nums[l] = nums[r]
            l += 1

            # 把r移动到重复数字的最后一位 例如 "11113" r的位置就移动到3前面两位 1 1 1(r) 13
            while r + 2 < len(nums) and nums[r] == nums[r + 2]:
                r += 1

            # 1 1 1 1(r) 3
            # 在这里，r会移动到有允许有两次重复的最后一个字符上
            r += 1



        return l
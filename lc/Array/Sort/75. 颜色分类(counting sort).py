"""
法国国旗问题，把0放最左边，把1放中间，把2放最右边
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

mid主动移动，left,right被动移动
"""
class Solution(object):
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums and len(nums) == 0:
            return []

        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            if num == 1:
                count1 += 1
            if num == 2:
                count2 += 1

        for i in range(len(nums)):
            if i < count0:
                nums[i] = 0
            elif i < count0 + count1:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums

# O(n+k) 古城算法 这个做法比较好记
# https://www.bilibili.com/video/BV1G54y1a7gS
# counting sort最基本的做法，通过计算每个元素的出现次数，然后再从小到大赋值到res数组，完成排序


class Solution(object):
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums and len(nums) == 0:
            return []

        # left-0 mid-1 right-2
        left = 0
        mid = 0
        right = len(nums) - 1

        # 这里注意是 <=
        # case = [2,0,1]
        # 第一次： [1,0,2] mid = 1, right = 1
        # 所以我们最后还缺一次验证
        while mid <= right:
            if nums[mid] == 0:
                self.swap(left, mid, nums)
                # 因为交换过后的mid,在当前位置上只有可能是0或1
                # 当[mid] = 0的时候，那么我们可以直接跳过，因为那是要放在mid左边的
                # 当[mid] = 1的时候，我们也可以直接跳过，因为那是要放在mid区间的
                # mid只可能为0，1的原因是，mid碰到2就直接跟right换了
                # 所以能到这个判断的只有可能是的left，换过来的值只有可能是0，1
                left += 1
                mid += 1


            elif nums[mid] == 1:
                mid += 1
            else:
                # 因为right有可能把2换到[mid]上，所以这里mid不做操作
                self.swap(mid, right, nums)
                right -= 1
        return nums

    def swap(self, a, b, nums):
        nums[a], nums[b] = nums[b], nums[a]

"""
https://algocasts.io/episodes/aVWyAYW2
Time: O(n), Space: O(1)
这题有点三指针的感觉，left左边放的是0，right右边放的元素是2，mid在中间
"""
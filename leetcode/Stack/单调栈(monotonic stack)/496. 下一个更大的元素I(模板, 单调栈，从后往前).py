"""
给定两个 没有重复元素 的数组nums1 和nums2，其中nums1是nums2的子集。
找到nums1中每个元素在nums2中的下一个比其大的值。

nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # 存放nums2[i]右边更大元素的列表，可供即将遍历到的nums[i]进行选择
        # 从栈顶 -> 栈底，数字是越来越接近nums2[i]的，因为总是从栈顶新加入元素
        # 从栈顶 -> 栈底, 数字是递减的
        stack = []

        # nums2的每一个数的下一个更大元素 答案
        q = [0] * len(nums2)

        for i in range(len(nums2) - 1, -1, -1):
            x = nums2[i]
            # 当新来的x比栈的堆顶元素大时，说明堆里面的数不能成为x的下一个更大数
            # 把堆顶元素pop出，直到在栈中找到第一个 > x的数为止
            while len(stack) > 0 and x >= stack[-1]:
                stack.pop()

            # 假如栈长度为0，说明当前数nums[i] 在 nums[i+1, -1]中不存在比它大的数
            if len(stack) == 0:
                q[i] = -1
            # 假如栈长度不为0，说明当前数nums[i] nums[i+1, -1]中存在比它大的数
            # 下一个比与nums2[i]大的数是堆顶元素
            else:
                q[i] = stack[-1]

            # 处理完后，把当前nums2[i]放入栈，用于给nums2[i-1]去做检验
            stack.append(x)

        # 记录 nums2[i] : 对应下标i
        hashmap = {}
        for i in range(len(nums2)):
            hashmap[nums2[i]] = i

        res = []
        # 由于nums1是nums2的子集，然后nums2每个数的下一个更大数已经被我们记录在q里
        # 所以我们只用把nums1的结果翻译出来就好
        for x in nums1:
            res.append(q[hashmap[x]])

        return res

"""
代码参考y总
https://www.acwing.com/activity/content/problem/content/2919/
"""
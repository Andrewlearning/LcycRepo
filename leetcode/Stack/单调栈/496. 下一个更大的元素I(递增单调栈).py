"""
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

 

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
        res = [-1] * len(nums1)

        # 存放还没找到下一个最大数的元素
        stack = []

        # 存放nums2每个元素所对应的下一个最大数
        hashmap = {}

        for i in range(len(nums2)):
            # nums2[i] 是下一个更大数时，nums2都可以满足的元素pop出
            while len(stack) != 0 and stack[-1] < nums2[i]:
                hashmap[stack.pop()] = nums2[i]

            # 处理完后，把当前nums2[i]放入栈
            # 在下一轮循环中寻找nums2[i]的下一个更大之
            stack.append(nums2[i])

        # 把我们找到的结果映射到nums1[s]
        for i in range(len(nums1)):
            # 处理不存在下一个更大值得情况
            if nums1[i] not in hashmap:
                continue
            res[i] = hashmap[nums1[i]]

        return res

"""
https://leetcode-cn.com/problems/next-greater-element-i/solution/xia-yi-ge-geng-da-yuan-su-i-by-leetcode/
"""
"""
Given an unsorted nums of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""
class Solution(object):
    """
    这个search Insert为35题的答案,但是这里需要改造一下
    因为我们分配的给res的内存是大于实际需要的内存
    但我们需要的只是前面那一小段有数字的，例[1,2,4,0,0,0]
    只需要到[1,2,4],所以变量length的作用就在这里
    """
    # 找能从左边插入的坐标
    def searchInsert(self, nums, length, target):
        l = 0
        r = length

        while l < r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        return l

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return []

        n = len(nums)
        q = [0] * n
        reslen = 0

        for x in nums:
            # 二分范围只在res有记录范围内
            i = self.searchInsert(q, reslen, x)
            # 更新结果子串, 无论新增还是在原有替换，都必须更新
            q[i] = x
            # 假如发现有新增的，则将记录+1
            if i == reslen:
                reslen += 1
        return reslen


"""
时间复杂度O(NlongN) 空间复杂O（N），新开了一个list,二分查找是logN，比较强
答案：
这里的设计其实很巧妙，每次从nums取一个数出来，看它能在q
里放在什么位置，但都是按照从小往大的顺序（满足要求）

case [1,8,9,4,11]

例如：原来是[1,8,9],现在遍历到4
1.新遍历到的数字（4），可以插入的位置为1的后面，那么我们就把[1,8,9]替换成[1,4,9]
    - 这样贪心的做法也没问题，因为即便替换了数字，最长子串长度还是3
2.新遍历到的数字（11）,可以插入的位置为len(q), 于是我们把11加进[1,4,9]->[1,4,9,11]
    - 可以看到8被替换一点影响也没有
这就是贪心的神奇之处

可以参考这个答案
https://leetcode.cn/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
"""

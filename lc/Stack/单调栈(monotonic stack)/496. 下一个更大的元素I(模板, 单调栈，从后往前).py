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
        # 从栈顶 -> 栈底, 数字是递减的 e.g. [4,3,2,1]
        stack = []

        n = len(nums2)
        # 记录nums2的每一个数的下一个更大元素的下标
        nextLarger = [-1] * n

        for i in range(n - 1, -1, -1):
            x = nums2[i]

            """
            [1,3,4,2]  [] stack head -> 2没有next large value -> 2进入stack, [1,3,4] [2] stack head 
            [1,3]  4   [2] stack head -> stack里没有比4大的，stack里的元素都被pop了 [1,3] 4 [] stack head -> 4进入stack [1,3] [4] stack head
            [1]    3   [4] stack head -> 3的next large value=4 -> 3进入了stack [1]  [3,4] stack head
            []     1   [3,4] stack head -> 1的next larget value=3 -> 1进入了stack[] [1,3,4] stack head
            
            当新来的x比栈的堆顶元素大时，说明堆里面的数不能成为x的下一个更大数
            把堆顶元素pop出，直到在栈中找到第一个 > x的数为止
            = 也要pop的愿意是，例如[2,3，3] 我们希望找到2的下一个最大值，所以希望拿到的时第一个3的下标
            所以当我我们遍历到第一个3的时候，也要把更远的那个3的下标给pop掉
            """
            while len(stack) > 0 and x >= stack[-1]:
                stack.pop()

            # 假如栈长度不为0，说明当前数nums2[i] nums2[i+1 ~ -1]中存在比它大的数
            # 下一个比与nums2[i]大的数是堆顶元素
            if len(stack) != 0:
                nextLarger[i] = stack[-1]

            # 处理完后，把当前nums2[i]放入单调栈中
            stack.append(x)

        # 记录 nums2[i] : 对应nums2[i]右边第一个更大数的下标是多少
        hashmap = {}
        for i in range(n):
            hashmap[nums2[i]] = nextLarger[i]

        res = []
        # 由于nums1是nums2的子集，然后nums2每个数的下一个更大数已经被我们记录在nextLarger里
        # 所以我们只用把nums1的结果翻译出来就好
        for x in nums1:
            res.append(hashmap[x])

        return res

"""
代码参考y总
https://www.acwing.com/activity/content/problem/content/2919/
"""
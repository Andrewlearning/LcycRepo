"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return []

        res = []
        num1 = 0
        c1 = 0
        num2 = 0
        c2 = 0

        # 为什么用这么多continue呢？因为对于每次循环，下面的每种情况都只能发生一次
        for num in nums:
            if num1 == num:
                c1 += 1
                continue

            if num2 == num:
                c2 += 1
                continue

            # 如果num 不等于num1 或者 num2
            # 且c1,c2删减为0了，那么我们这时候就要更换num1 或者num2了
            if c1 == 0:
                num1 = num
                c1 = 1
                continue

            if c2 == 0:
                num2 = num
                c2 = 1
                continue

            # 如果num != num1,num2 ，且c1,c2都不为0（要换数字了），那么c1,c2都要减少1
            c1 -= 1
            c2 -= 1

        # 检查两个出现次数最多的数，符不符合 n/3的要求
        c1 = 0
        c2 = 0
        for num in nums:
            if num == num1:
                c1 += 1
            elif num == num2:
                c2 += 1

        if c1 > len(nums) // 3:
            res.append(num1)

        if c2 > len(nums) // 3:
            res.append(num2)

        return res

"""
https://leetcode-cn.com/problems/majority-element-ii/solution/169ti-sheng-ji-ban-xiang-jie-zhu-xing-jie-shi-tong/
时间复杂度为 O(n)，空间复杂度为 O(1)

思路和169 是一样的，用的是摩尔投票法
先理解，一个数组最多有两个超过 n/3的数，因为有两个 n/3的数的话, 第三个数必然小于 n/3.
先通过投票法把 两个出现次数最多的元素找出来
然后再检测他们每一个是否确实超过 n/3, 把超过n/3的放入结果里面去

"""
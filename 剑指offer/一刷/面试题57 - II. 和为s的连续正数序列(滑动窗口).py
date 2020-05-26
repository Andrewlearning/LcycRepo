"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 
示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        # 因为这个数组是从 1 ~ 正无穷的，所以他们的值都是从这里开始的
        # 这个滑动窗口是左闭右开的
        l = 1
        r = 1

        # 滑动窗口里的和
        total = 0

        res = []

        # 因为一个滑动窗口里，最少有两个数字，当其中小的数字都到 1/2 target的时候，说明[i，j)的后续总和肯定都大于target了
        while l <= target // 2:

        	# 窗口内比target小，说明要扩大了，那么r向右走扩张
            if total < target:
                # 右边界向右移动
                total += r
                r += 1

        	# 窗口内比target大，说明要缩小了，那么l往右走缩小
            elif total > target:
                # 左边界向右移动
                total -= l
                l += 1

            else:
                # 记录结果
                arr = list(range(l, r))
                res.append(arr)
                # 左边界向右移动
                total -= l
                l += 1

        return res


"""
时间复杂度是 O(n)

为了编程的方便，滑动窗口一般表示成一个左闭右开区间
https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
"""
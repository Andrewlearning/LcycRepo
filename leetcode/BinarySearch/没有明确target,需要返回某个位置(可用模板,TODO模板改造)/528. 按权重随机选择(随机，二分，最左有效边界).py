"""
给定一个正整数数组 w ，其中 w[i] 代表下标 i 的权重（下标从 0 开始），请写一个函数 pickIndex ，它可以随机地获取下标 i，选取下标 i 的概率与 w[i] 成正比。

例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。

也就是说，选取下标 i 的概率为 w[i] / sum(w) 。

 
示例 1：

输入：
["Solution","pickIndex"]
[[[1]],[]]
输出：
[null,0]
解释：
Solution solution = new Solution([1]);
solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。
"""
class Solution:

    def __init__(self, A):
        # 先把权重构造成一个列，随机数在权重里取一个数，然后看这个随机数在哪
        self.pre = [A[0]]
        for i in range(1, len(A)):
            self.pre.append(self.pre[-1] + A[i])

    def pickIndex(self):
        rd = int(random.random() * self.pre[-1])

        l, r = 0, len(self.pre) - 1
        # 插入最左模板
        while l < r:
            mid = (l + r) // 2
            if self.pre[mid] > rd:
                # mid 是一个备胎
                r = mid
            else:
                # mid + 1 是一个备胎
                l = mid + 1
        # 由于 l 和 r 相等，因此返回谁都无所谓。那我就返回 l ，刚好和 最左模板的右对应
        return l

# 链接：https://leetcode-cn.com/problems/random-pick-with-weight/solution/li-kou-jia-jia-er-fen-bisect_left-528-an-thn9/
# https://www.acwing.com/video/1951/

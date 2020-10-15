"""
给定一个整数数组 nums，按要求返回一个新数组 counts。
数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
示例：
输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
"""
class FenwickTree(object):
    def __init__(self, n):
        # 树状数组所有数都是从1开始
        # 从1开始记录，等于是每一个数字出现了多少次
        self.prefixSum = [0] * (n)

    def update(self, i, delta):
        while i < len(self.prefixSum):
            self.prefixSum[i] += delta
            # 把i从上面的节点移动到下面的节点, 一个个更新
            i += self.lowbit(i)

    # 得到[0,i]的和
    def query(self, i):
        prefixSum = 0
        while i > 0:
            prefixSum += self.prefixSum[i]
            # 从下面的节点移动到上面的节点，一个个加上去
            i -= self.lowbit(i)
        return prefixSum

    # 获取当前index 的为1的最低二进制位
    def lowbit(self, x):
        return x & (-x)


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 因为数据规模是 -1*10000 ~ 10000, 所以总共有20001个数，又因为数状数组只能从1开始，所以我们把下标0不用
        tr = FenwickTree(20002)
        res = [0] * len(nums)

        # 我们从后往前数，是因为每数一个数，都要在他的位置上+1
        # 从后往前的话，保证了左边的数，不会被计算在内
        for i in range(len(nums)-1, -1, -1):
            # 当前数，下标0不用，所以+10001
            x = nums[i] + 10001
            # 统计比当前数小的数出现了几次
            res[i] = tr.query(x - 1)
            # 更新当前数的出现次数
            tr.update(x, 1)

        return res






"""
看什么是树状数组https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/shu-zhuang-shu-zu-by-liweiwei1419/
代码https://www.acwing.com/video/1703/
"""








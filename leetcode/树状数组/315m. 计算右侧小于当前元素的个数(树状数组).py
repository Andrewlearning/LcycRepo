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

import collections
class FenwickTree(object):
    def __init__(self, n):
        # 从1开始记录，等于是每一位记录着前缀和
        self.prefixSum = [0] * (n + 1)

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
        # 把每个元素去重并且排序一遍
        sorted_nums = sorted(list(set(nums)))

        # 把每个元素大大小转换成rank, 例如1,2,3 则
        # 1：0， 2：1， 3：2
        rank_nums = collections.defaultdict(int)
        rank = 0
        for num in sorted_nums:
            rank_nums[num] = rank
            rank += 1

        # 因为我们要求每个
        tree = FenwickTree(len(sorted_nums))

        # 把数组进行倒叙，因为我们需要知道 在这个元素之后，比当前元素小的个数
        # 倒叙过来以后，就变成，比当前元素小，且在这个元素之前的个数
        # 然后我们就可以利用数组数组的前缀和性质去求
        nums = nums[::-1]

        res = []

        for i in range(len(nums)):
            # 首先我们把当前元素nums[i] 排序后的的前缀和求一遍，表示得到比这个元素小，且在这个元素之前的个数
            res.append(tree.query(rank_nums[nums[i]] + 1 - 1))
            # 把树当中的rank数组，更新
            tree.update(rank_nums[nums[i]] + 1, 1)

        # 因为我们是倒着求得，所以最后还要把结果给反过来
        return res[::-1]





"""
https://www.youtube.com/watch?v=2SVLYsq5W8M&t=156s
input = [7,1,3,2,9,2,1]
sorted_nums = [1,2,3,7,9]
reverse =       [1,2,9,2,3,1,7]
ranks(大小排名)= [1,2,5,2,3,1,4]
res          =  [0,1,2,1,3,0,5]
res[::-1]    =  [5,0,3,1,2,1,0]
"""








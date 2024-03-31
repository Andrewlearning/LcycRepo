class FenwickTree(object):
    def __init__(self, n):
        # 从1开始记录，等于是每一位记录着前缀和
        self.prefixSum = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.prefixSum):
            self.prefixSum[i] += delta
            # 把i从上面的节点移动到下面的节点, 一个个更新
            i += self.lowbit(i)

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


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # 构造树
        self.tree = FenwickTree(len(nums))

        # 我们把数字里的每个值给更新到每个节点
        for i in range(len(nums)):
            self.tree.update(i + 1, self.nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.tree.update(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.query(j + 1) - self.tree.query(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
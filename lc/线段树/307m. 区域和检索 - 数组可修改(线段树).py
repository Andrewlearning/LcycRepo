"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

示例:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""

# 线段树的节点
class TreeNode(object):
    def __init__(self, start, end):
        # 该节点的左右子树
        self.left = None
        self.right = None

        # 该节点代表数组上的左右下标[]
        self.start = start
        self.end = end

        # 该节点代表的数组的的和
        self.sum = None


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = None
        self.nums = nums
        self.root = self.buildTree(0, len(nums) - 1)

    def buildTree(self, start, end):
        if start > end:
            return None

        # 每轮循环的根节点
        res = TreeNode(start, end)

        # 假如到叶子节点了，那么直接返回[叶子下标]
        if start == end:
            res.sum = self.nums[start]
        else:
            mid = (start + end) // 2
            res.left = self.buildTree(start, mid)
            res.right = self.buildTree(mid + 1, end)
            res.sum = res.left.sum + res.right.sum

        return res

    # 通过i来找节点，然后更新i后，从下往上更新沿途节点
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.treeUpdate(self.root, i, val)

    def treeUpdate(self, root, i, val):
        # 假如说已经找到了叶子节点，且它的下标等于i, 更新
        if root.start == i and root.end == i:
            root.sum = val
        else:
            mid = (root.start + root.end) // 2
            if i <= mid:
                self.treeUpdate(root.left, i, val)
            else:
                self.treeUpdate(root.right, i, val)
            # 假如说下面的节点更新了，我们也要更新沿途的节点
            root.sum = root.left.sum + root.right.sum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.treeSumRange(self.root, i, j)

    def treeSumRange(self, root, i, j):
        if root.start == i and root.end == j:
            return root.sum
        else:
            mid = (root.start + root.end) // 2
            # 说明[i,j] 在左子树，我们去左子树
            if j <= mid:
                return self.treeSumRange(root.left, i, j)
            # 说明[i,j] 在右子树，我们去左子树
            elif i >= mid + 1:
                return self.treeSumRange(root.right, i, j)
            # 说明[i,j] 在左右子树都有，我们要分别拼接左右子树所有的节点
            else:
                return self.treeSumRange(root.left, i, mid) + \
                       self.treeSumRange(root.right, mid + 1, j)


"""
https://www.youtube.com/watch?v=XDh5Lm4zYa8&t=557s
"""
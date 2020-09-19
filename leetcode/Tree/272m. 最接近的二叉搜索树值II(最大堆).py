"""
给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的 k 个值。

注意：

给定的目标值 target 是一个浮点数
你可以默认 k 值永远是有效的，即 k ≤ 总结点数
题目保证该二叉搜索树中只会存在一种 k 个值集合最接近目标值
示例：

输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2

    4
   / \
  2   5
 / \
1   3

输出: [4,3]
拓展：
假设该二叉搜索树是平衡的，请问您是否能在小于 O(n)（n 为总结点数）的时间复杂度内解决该问题呢？
"""
import heapq
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # 最大堆，使得差值最大的node始终在堆顶，这样我们碰到差值小的就可以进行替换
        self.heap = []
        self.diff = float('inf')
        self.helper(root, target, k)
        return [pair[1].val for pair in self.heap]

    def helper(self, root, target, k):
        if not root:
            return

        cur_diff = -abs(target - root.val)
        if len(self.heap) < k:
            heapq.heappush(self.heap, (cur_diff, root))
        else:
            if cur_diff > self.heap[0][0]:
                heapq.heapreplace(self.heap, (cur_diff, root))

        self.helper(root.left, target, k)
        self.helper(root.right, target, k)

"""
维护一个大小为k最大堆，使得差值最大的node始终在堆顶，这样我们碰到差值小的就可以进行替换
遍历结束后，堆内就只剩下离target最近的k个节点了
"""
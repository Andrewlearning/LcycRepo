"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）
"""
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            # 本层需要遍历多少个元素
            n = len(queue)
            # 本层所遍历元素的值
            level = []

            while n > 0:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n -= 1

            # 只有偶数层，才需要倒过来
            if len(res) % 2 == 1:
                res.append(level[::-1])
            else:
                res.append(level)

        return res
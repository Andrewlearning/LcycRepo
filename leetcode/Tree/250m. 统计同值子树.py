"""
给定一个二叉树，统计该二叉树数值相同的子树个数。

同值子树是指该子树的所有节点都拥有相同的数值。

示例：

输入: root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

输出: 4

"""

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.count = 0
        self.helper(root, root.val)
        return self.count

    def helper(self, root, val):
        # 1.该节点没有子结点 （基本情况）
        if not root:
            return True

        # 2.该节点的所有子结点都为同值子树，且结点与其子结点值相同。
        # 假如到了叶子节点，这一行也是可以成立的
        if not all([self.helper(root.left, root.val), self.helper(root.right, root.val)]):
            return False

        # 因为2成立，所以我们能把count += 1
        self.count += 1

        # 给递归用
        return root.val == val



"""
https://leetcode-cn.com/problems/count-univalue-subtrees/solution/tong-ji-tong-zhi-zi-shu-by-leetcode/

给定树中的一个结点，若其满足下面条件中的一个，则子树同值:
1.该节点没有子结点 （基本情况）
2.该节点的所有子结点都为同值子树，且结点与其子结点值相同。

"""
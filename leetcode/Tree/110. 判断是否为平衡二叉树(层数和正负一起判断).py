"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

平衡二叉树（Balanced Binary Tree）它是一棵空树或它的左右两个子树的高度差的绝对值不超过1,
意味着其中一边可以是缺一个node的。这题的做法是要计算每个node的高度差
再换而言之，就是求每一个node的深度
"""
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True

        return self.helper(root) != -1

    def helper(self,root):
        if not root:
            return 0

        #看左子树的子树是不是平衡二叉树，假如不是的话，提前中断函数
        left = self.helper(root.left)
        if left == -1:
            return -1

        #看右子树的子树是不是平衡二叉树，假如不是的话，提前中断函数
        right = self.helper(root.right)
        if right == -1:
            return -1

        #判断左右子树的高度差满足要求了吗
        #这里要大于1，因为只有大于1才可以满足不平衡
        if abs(left - right) > 1:
            # 假如不平衡，则返回-1
            return -1

        # 说明左右子树本身是平衡二叉树，返回root+子树的最大高度
        return 1 + max(left,right)


"""
如果改为从下往上遍历（先判断子树，再判断主树），如果子树是平衡二叉树，则返回子树的高度；
如果发现子树不是平衡二叉树，则直接停止遍历，这样至多只对每个结点访问一次。
"""
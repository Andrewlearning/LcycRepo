"""
给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。

在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。

返回使每个结点上只有一枚硬币所需的移动次数。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        # 本题策略是，返回自己要送走，或者是要拿到多少硬币。
        # 然后res + 的是，子节点总共多出来或者少多少硬币，因为无论是多还是少，都要进行移位操作
        self.res += abs(left) + abs(right)

        # 返回自己多出，或着需要多少枚硬币
        # 这也代表着，在当前node,要进行多少次移动
        # 总答案是在所有node,要进行多少次移动
        return root.val + left + right - 1

"""
本题奥秘，设定过载量
假如某个节点仅包含0枚硬币，他的过载量为-1，说明要从别的地方拿一块硬币
假如某个节点仅包含1枚硬币，他的过载量为0，说明不用拿硬币
假如某个节点仅包含2枚硬币，他的过载量为1，说明要送走一块硬币
"""

# 链接：https://leetcode-cn.com/problems/distribute-coins-in-binary-tree/solution/zai-er-cha-shu-zhong-fen-pei-ying-bi-by-leetcode/


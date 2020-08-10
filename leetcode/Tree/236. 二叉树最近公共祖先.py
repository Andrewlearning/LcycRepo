"""
Given a binary tree, find the lowest common ancestor (LCA)(最近公共祖先)
 of two given nodes in the tree.

"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        #找到已经遍历到 p,q的情况， 或者是遍历到None的情况(说明没找到pq)，返回 q,p或者none
        if (not root) or (root == p) or (root == q):
            return root

        #看左子树和右子树有没有找到pq
        #假如说只有一遍找到的话，被找到的节点肯定是最近公共祖先，因为他最先被找到，且另外一个节点
        #肯定在它下面
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        #假如左右子树都找到pq,说明两个节点肯定在一左一右，返回当前root
        if left and right:
            return root
        #假如说只找到一边，那我们就返回那一边的最上面节点
        return left or right

"""   6
    5    8
   3  2
        1   
答案：
因为每个node都只遍历一次，所以Time:O(n) , Space:O(1)
1.第一个if 处理不存在情况以及2的情况

两个情况
2.例如找5，1。那么在遍历到5的时候就直接在第一个if语句里return 5了，因此我们可以直到，在root=6的循环里
left = 5, right = None.因为right肯定找不到东西，然后我们就通过最后一个return 返回left = 5了。
因为在左子树最先找到5，这个5即是祖先，也是q,也是p的祖先
3.例如找3,1。那么在root = 5的循环里，left = 3, right = 1。因为left,right都有，就不是第二种情况了
所以就返回root = 5，


"""
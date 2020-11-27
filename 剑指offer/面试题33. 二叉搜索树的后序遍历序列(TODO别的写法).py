class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        # left, right , root
        # 本题目按照节点的大小顺序来进行处理
        # 已知的是 左节点最小， ROOT节点中间， 右节点最大

        if not postorder and len(postorder) == 0:
            return True

        return self.helper(postorder)

    def helper(self, postorder):
        if len(postorder) == 0:
            return True

        root = postorder[-1]
        right_first = -1

        for i in range(len(postorder) - 1):
            if postorder[i] > root:
                right_first = i
                break

        for j in postorder[right_first:-1]:
            if j < root:
                return False

        return self.helper(postorder[:right_first]) and self.helper(postorder[right_first:-1])

"""
回顾一下二叉搜索树的基础：
    先序遍历：1。根节点
             2。左节点
             3。右节点
    所以导致输出的列表，【根节点，比根节点大的数，比根节点小的数】

    中序遍历：1。左节点
             2。根节点
             3。右节点
    所以导致输出的列表，【比根节点小的数,根节点，比根节点大的数】

    后序遍历：1。左节点
             2。右节点
             3。根节点
    所以导致输出的列表，【比根节点小的数,比根节点大的数，根节点】

现在这题是要看，输出的列表是否符合后序遍历的顺序，我们就可以根据后序遍历的
规律来进行查看了

1.找到root,并剔除root的影响
2，找到比根节点大，和比根节点小的分界点
3，分别这两个序列是否都比根节点大或都比根节点小（查看是否满足后序遍历的规律）
4，把这两个sequence继续递归分化，重复123的过程

debug点：
flag的初始值设定应该是sequence的最后一位，因为若flag = 0 ,然后对于【6，7】来说，无法更新flag
后进入判断就会报错
"""
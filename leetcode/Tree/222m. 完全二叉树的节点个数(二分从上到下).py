# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # 除最后一层以外的高度
        d = 0
        node = root

        # 除最后一层以外的高度
        while node.left:
            node = node.left
            d += 1

        # 然后我们在最下面一层做一个二分查找
        # l代表最后一层从左到右第一个不存在的node的下标
        l = 0

        # r代表满二叉树下最后一层所拥有的节点数 - 1
        r = 2 ** d - 1

        # 一般是用while 循环退出的话， l都会指向右边。r会指向左边，所以退出时l指向的是不存在的第一位
        while l <= r:
            mid = (l + r) // 2
            # 看在最后一层mid index上，有没有节点存在
            if self.exist(mid, d, root):
                l = mid + 1
            else:
                r = mid - 1

        return (2 ** d - 1) + l

    def exist(self, targer, depth, root):
        # 最下面一层的左边界和右边界
        l = 0
        r = 2 ** depth - 1

        # 我们要把mid 移动到target的位置去
        for _ in range(depth):
            mid = (l + r) // 2

            # 说明[0..mid..target],所以我们得把指针移动到mid以后
            if mid < targer:
                root = root.right
                l = mid + 1
            # 说明target在[0..mid]之间，所以我们把r=mid就可
            # 且因为我们最后只要知道target取不取得到就行了，所以我们只要保证不要出target的界就好了
            elif targer <= mid:
                root = root.left
                r = mid

        return root is not None

"""
https://www.youtube.com/watch?v=rvZfvo-r5WU
视频对这个二分查找讲的特别详细
"""
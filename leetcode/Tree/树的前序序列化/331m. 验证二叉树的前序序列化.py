"""
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时
我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
"""


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        self.s = preorder + ','
        self.p = 0
        # 假如遍历失败的话，不是前序序列化
        if not self.helper():
            return False

        # 假如说遍历到最后了都没有发现问题，说明没问题
        return self.p == len(self.s)

    def helper(self):
        if self.p == len(self.s):
            return False

        # base case,假如说遍历到#节点，说明一边已经遍历完了，要去另一边的节点了
        # #,4 假如说p在#，那么p要前进两位才能到下一位
        if self.s[self.p] == "#":
            self.p += 2
            return True

        # 4, 假如说p在4，那么p要++
        while self.s[self.p] != ",":
            print(self.p)
            self.p += 1
        self.p += 1

        # 一个遍历左子树，一个遍历右子树
        return self.helper() and self.helper()

# https://www.acwing.com/video/1723/
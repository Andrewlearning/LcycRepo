"""
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑
-> 所以我们不采用和297一样的做法，297使用#记录None,这里我们不使用#来记录None


示例 1：

输入：root = [2,1,3]
输出：[2,1,3]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""

        res = str(root.val)
        if root.left != None:
            res += "," + self.serialize(root.left)
        if root.right != None:
            res += "," + self.serialize(root.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        q = data.split(",")
        return self.deserializeHelper(q, float('-inf'), float('inf'))

    def deserializeHelper(self, q, lower, upper):
        if len(q) == 0:
            return None

        val = int(q[0])
        # 为什么我们要限定范围呢
        # 因为我们希望左子树的值，都是小与root节点的，
        # 但是我们无法控制queue pop出来的数是否为左子树的值，因为有可能pop多了，pop出右子树的。
        # 这就导致树在构造的时候出现问题
        # 例如2,1,3。在处理到1的时候，会这样调root.left([3], -inf, 1)，假如我们不限制，那么就会构造错了
        if val < lower or val > upper:
            print("value is ", val, lower, upper, q)
            return None

        q.pop(0)

        root = TreeNode(val)
        root.left = self.deserializeHelper(q, lower, val)
        root.right = self.deserializeHelper(q, val, upper)
        return root


# 古城算法 13：00
# https://www.bilibili.com/video/BV1jb4y1974B
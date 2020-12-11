"""
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。

 

示例 1：

输入：root = [2,1,3]
输出：[2,1,3]
"""


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        # left ,right ,root 的方式序列化
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            # root, right, left的方式反序列化
            val = data.pop()
            root = TreeNode(val)
            # 右子树，当然所有值都要比根节点大
            root.right = helper(val, upper)
            # 左子树，所有值要比根节点小
            root.left = helper(lower, val)

            # 返回处理好后的根节点
            return root

        # 先把data 都变成数字的形式，方便后续处理
        data = [int(x) for x in data.split(' ') if x]
        return helper()

# 链接：https://leetcode-cn.com/problems/serialize-and-deserialize-bst/solution/xu-lie-hua-he-fan-xu-lie-hua-er-cha-sou-suo-shu-2/
"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作
进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境
采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
"""

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        self.dfsse(root)
        return ",".join(self.res)

    def dfsse(self, root):
        if root == None:
            self.res.append("#")
            return
        # root, left, right 前序遍历
        self.res.append(str(root.val))
        self.dfsse(root.left)
        self.dfsse(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.i = 0
        return self.dfsde(data)

    def dfsde(self, data):
        # base case，两种情况，这里的self.i已经在函数调用前就已经移动到位了
        # 1.当前位置无节点，那么返回None
        if data[self.i] == "#":
            return None
        # 2.当前位置有节点，则添加节点
        root = TreeNode(int(data[self.i]))

        # 这个+1是为了给root.left添加节点使用的
        self.i += 1
        root.left = self.dfsde(data)

        # 这个+1是为了给root.right添加节点使用的
        self.i += 1
        root.right = self.dfsde(data)

        return root


"""
时间复杂度 O(N)，N 为二叉树的节点数，按层构建二叉树需要遍历整个vals ，其长度最大为2N+1
空间复杂度 O(N)
利用了先序遍历
https://www.acwing.com/activity/content/problem/content/2670/1/Python3/
"""

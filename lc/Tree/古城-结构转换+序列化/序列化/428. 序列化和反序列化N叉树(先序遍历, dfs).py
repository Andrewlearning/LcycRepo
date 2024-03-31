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
            return
        # 序列化为: [A节点，A节点的子节点数量，B节点，B节点的子节点数量..]
        self.res.append(str(root.val))
        self.res.append(len(root.children))
        for child in root.children:
            self.dfsse(child)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        return self.dfsde(data)

    def dfsde(self, data):
        # 先取出节点值
        root = Node(data.pop(0), [])
        # 再取出该节点对应的子节点数量
        children = data.pop(0)
        for i in range(children):
            root.children.append(dfs(data))
        return root

"""
古城算法:https://www.youtube.com/watch?v=jD-6iLWw9x8 11:06
为什么二叉树的序列化不能用这种解法
因为本题的这种节点，一定是按照从左到右排
但是二叉树，是有可能出现left=nil, right!=nil的情况，所以这种deserialize的for循环里无法处理这种情况，最后会把右节点还原到左节点上
"""
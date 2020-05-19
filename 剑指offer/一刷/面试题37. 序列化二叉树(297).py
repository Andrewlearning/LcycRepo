class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 利用正常的层序遍历，来把node,包括None，都加进结果里面去
    def Serialize(self, root):
        if not root:
            return

        res = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))

                # 假如说一个节点是叶子节点，那么它的左右都是None, 被加进queue里面去了
                queue.append(node.left)
                queue.append(node.right)

            # if node == null
            else:
                res.append('null')

        # 满足输出格式
        return "[" + ",".join(res) + "]"


    #
    def Deserialize(self, data):
        if data == "[]":
            return

        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = [root]

        while queue:
            node = queue.pop(0)

            # 就是，当我们遇到None的时候，我们就跳过，我们只处理带节点的情况
            # 因为None的话，初始化TreeNode的时候就带着有了，所以我们不需要去处理
            # 但是数值的话，需要我们一个个去进行安装
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)

            # 无论上一个是None,还是值，我们都已经处理过了
            i += 1

            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1

        return root







"""
时间复杂度 O(N)，N 为二叉树的节点数，按层构建二叉树需要遍历整个vals ，其长度最大为2N+1
空间复杂度 O(N)
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/mian-shi-ti-37-xu-lie-hua-er-cha-shu-ceng-xu-bian-/


"""


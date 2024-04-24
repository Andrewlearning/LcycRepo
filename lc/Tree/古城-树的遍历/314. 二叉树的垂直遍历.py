"""
Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, col by col).

If two nodes are in the same row and col, the order should be from left to right.

Examples 1:

Input:
[3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
"""
class Solution:
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict, deque
        if not root:
            return []

        # 使用字典来存储每个节点的列号及其对应的值
        # key: column值
        # val: 在此column值的value
        colMap = defaultdict(list)
        
        # (node, col)
        # 我们设定root节点对应的col是0
        queue = deque([(root, 0)]) 

        while queue:
            node, col = queue.popleft()
            colMap[col].append(node.val)

            # 添加左节点时，col应该为当前节点 - 1
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        # 根据列号从小到大，将节点的值按列号存入结果列表中
        res = []
        for col in sorted(colMap.keys()):
            res.append(colMap[col])
        return res

# 答案来自gpt
# https://www.lintcode.com/problem/651/ 对应lintcode 651题
```
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
```

func countNodes(root *TreeNode) int {
    if root == nil {
        return 0
    }

    x, y := 1, 1
    l, r := root, root

    for l.Left != nil {
        x += 1
        l = l.Left
    }

    for r.Right != nil {
        y += 1
        r = r.Right
    }

    // 假如这棵树的最左 最右节点都一样长的话，那么说明这是一颗完全二叉树
    // 可以通过 2**height - 1
    if x == y {
        return 1 << x - 1
    }

    // 假如最左最右节点不一样长的话，那么继续遍历
    // 最差的情况，遍历到只有一个节点的时候，那么最左最右节点一样长
    return countNodes(root.Left) + 1 + countNodes(root.Right)
}

// time O(log2 N)
// https://www.acwing.com/video/1594/
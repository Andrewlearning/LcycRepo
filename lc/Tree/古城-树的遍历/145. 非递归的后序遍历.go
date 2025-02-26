/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func postorderTraversal(root *TreeNode) []int {
    if root == nil {
        return nil
    }

    st := []*TreeNode{root}
    res := []int{}

    // left, right, root
    // root, right ,left
    for len(st) > 0 {
        root = st[len(st) - 1]
        st = st[:len(st) - 1]

        res = append(res, root.Val)

        if root.Left != nil {
            st = append(st, root.Left)
        }
        if root.Right != nil {
            st = append(st, root.Right)
        }
    }

    // 原地交换元素
    for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
        res[i], res[j] = res[j], res[i]
    }

    return res
}
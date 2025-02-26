/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func preorderTraversal(root *TreeNode) []int {
    if root == nil {
        return nil
    }

    st := []*TreeNode{root}
    res := []int{}

    for len(st) > 0 {
        root = st[len(st) - 1]
        st = st[:len(st) - 1]
        res = append(res, root.Val)


        if root.Right != nil {
            st = append(st, root.Right)
        }
        if root.Left != nil {
            st = append(st, root.Left)
        }
    }

    return res
}
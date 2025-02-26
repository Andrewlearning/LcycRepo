/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return nil
    }
    q := []*TreeNode{root}
    res := [][]int{}

    for len(q) > 0 {
        temp := []int{}
        nxt := []*TreeNode{}

        for _, node := range q {
            temp = append(temp, node.Val)

            if node.Left != nil {
                nxt = append(nxt, node.Left)
            }
            if node.Right != nil {
                nxt = append(nxt, node.Right)
            }
        }
        res = append(res, temp)
        q = nxt
    }

    return res
}
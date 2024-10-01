/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getMinimumDifference(root *TreeNode) int {

    var stack []*TreeNode
    pre := math.MinInt32
    res := math.MaxInt32

    for root != nil || len(stack) > 0 {
        for root != nil {
            stack = append(stack, root)
            root = root.Left
        }

        // get last element
        cur := stack[len(stack) - 1]
        // remove last element
        stack = stack[:len(stack)-1]
        res = min(res, cur.Val - pre)
        pre = cur.Val

        root = cur.Right
    }

    return res
}
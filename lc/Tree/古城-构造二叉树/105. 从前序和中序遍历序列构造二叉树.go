/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
    // pre: root, l, r
    // in: l, root, r

    inm := make(map[int]int)
    for i, v := range inorder {
        inm[v] = i
    }
    preIndex := 0

    // 在go语言中，想在匿名函数中调用自己，需要预先定义
    var helper func(int, int) * TreeNode
    helper = func (l int, r int) *TreeNode {
        if l > r {
            return nil
        }

        rootVal := preorder[preIndex]
        preIndex += 1

        root := &TreeNode{Val:rootVal}
        rootIdx, _ := inm[rootVal]

        root.Left = helper(l, rootIdx - 1)
        root.Right = helper(rootIdx + 1, r)

        return root
    }

    return helper(0, len(inorder) - 1)

}
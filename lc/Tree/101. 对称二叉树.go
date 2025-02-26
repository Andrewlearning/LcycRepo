/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {

    var dfs func (l *TreeNode, r *TreeNode) bool
    dfs = func (l *TreeNode, r *TreeNode) bool{
        if l == nil && r == nil {
            return true
        }
        if l == nil || r == nil {
            return false
        }

        if l.Val != r.Val {
            return false
        }

        return dfs(l.Left, r.Right) && dfs(l.Right, r.Left)
    }

    return dfs(root.Left, root.Right)
}

// ----------------

func isSymmetric(root *TreeNode) bool {
    return helper(root.Left, root.Right)
}

func helper(l,r *TreeNode) bool {
    if l == nil && r == nil {
        return true
    }
    if l == nil || r == nil {
        return false
    }

    if l.Val != r.Val {
        return false
    }
    return helper(l.Left, r.Right) && helper(l.Right, r.Left)
}
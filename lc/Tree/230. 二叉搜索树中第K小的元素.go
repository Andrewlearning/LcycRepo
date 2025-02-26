package Tree

type TreeNode struct {
	   Val int
	   Left *TreeNode
	   Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {

    st := []*TreeNode{}

    for len(st) > 0 || root != nil {
        for root != nil {
            st = append(st, root)
            root = root.Left
        }

        root := st[len(st) - 1]
        st = st[:len(st) - 1]
        k -= 1
        if k == 0 {
            return root.Val
        }

        root = root.Right
    }

    return -1
}
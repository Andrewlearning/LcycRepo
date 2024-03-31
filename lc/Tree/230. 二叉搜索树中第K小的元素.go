package Tree

type TreeNode struct {
	   Val int
	   Left *TreeNode
	   Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {

	res := 0
	stack := []*TreeNode{}
	var cur *TreeNode = root

	for len(stack) != 0 || cur != nil {
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}

		// go里的pop()
		cur = stack[len(stack)-1]
		stack = stack[0:len(stack)-1]
		k -= 1
		if k == 0 {
			return cur.Val
		}

		cur = cur.Right
	}
	return res
}
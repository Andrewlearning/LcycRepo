package 非递归遍历二叉树


type TreeNode struct {
   Val int
   Left *TreeNode
   Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {

	res := []int{}
	stack := []*TreeNode{}
	cur := root

	for len(stack) != 0 || cur != nil {
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}

		cur = stack[len(stack) - 1]
		stack = stack[:len(stack) - 1]
		res = append(res, cur.Val)

		cur = cur.Right
	}

	return res

}
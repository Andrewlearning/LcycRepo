func buildTree(inorder []int, postorder []int) *TreeNode {
	// post: l, r, root
	// in: l, root, r
	m := make(map[int]int)
	for i, v := range inorder {
		m[v] = i
	}

	pid := len(postorder) - 1
	var helper func(l, r int) *TreeNode
	helper = func(l, r int) *TreeNode {
		if l > r {
			return nil
		}

		rootVal := postorder[pid]
		root := &TreeNode{Val: rootVal}
		rootIdx := m[rootVal]
		pid--

		root.Right = helper(rootIdx+1, r)
		root.Left = helper(l, rootIdx-1)

		return root
	}

	return helper(0, len(postorder)-1)
}

/*
做法上是105的相反，因为postorder的root节点是从右向左

时间复杂度： O(n),n 是树的节点数。
    构建哈希表是 O(n)。
    递归遍历树是 O(n),每个节点访问一次。
空间复杂度： O(n),n 是树的节点数。
    哈希表占用 O(n) 空间。
    递归调用栈占用 O(n) 空间，因为最差情况是单链状

*/
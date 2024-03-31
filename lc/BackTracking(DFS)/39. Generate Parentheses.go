package BackTracking

func sum(nums []int) int {
	var res int
	for i := 0; i < len(nums); i++{
		res += nums[i]
	}
	return res
}

func combinationSum(candidates []int, target int) [][]int {

	var res [][]int
	var temp []int

	var dfs func(cur int, temp []int)
	dfs = func(cur int, temp []int) {
		if sum(temp) > target {
			return
		}

		if sum(temp) == target {
			// 因为直接把temp加入的话可能会导致指针混乱的问题
			// 所以要先把temp的所有值装进一个新数组，然后再append进res
			res = append(res, append([]int(nil), temp...))
			return
		}

		for i:= cur; i < len(candidates); i ++ {
			temp = append(temp, candidates[i])
			dfs(i, temp)
			temp = temp[0: len(temp)-1]
		}
	}

	dfs(0, temp)
	return res
}

/**

时间复杂度取决于所有可行解的长度之和。
从分析给出的搜索树我们可以看出时间复杂度取决于搜索树所有叶子节点的深度之和
即所有可行解的长度之和。


空间复杂度：O(target)。
除答案数组外，空间复杂度取决于递归的栈深度，在最差情况下需要递归 O(target)层。
因为假设答案是[1,1,1,1..]构成的

 */
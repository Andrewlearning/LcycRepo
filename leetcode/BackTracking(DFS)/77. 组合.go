package BackTracking

func combine(n int, k int) [][]int {

	var res [][]int
	var temp []int
	var dfs func(cur int, remain int, temp []int)

	dfs = func(cur int, remain int, temp []int) {
		if remain < 0 {
			return
		}
		if remain == 0 {
			res = append(res, append([]int(nil), temp...))
			return
		}

		for i := cur; i <= n; i++ {
			temp = append(temp, i)
			dfs(i+1, remain-1, temp)
			temp = temp[:len(temp)-1]
		}

	}

	dfs(1, k, temp)
	return res
}
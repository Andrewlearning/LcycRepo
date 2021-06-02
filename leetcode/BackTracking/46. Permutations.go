package BackTracking


func permute(nums []int) [][]int {

	var res [][]int
	var temp []int
	var dfs func(cur int, temp []int)
	// TODO go字典
	visited := make(map[int]bool)

	dfs = func(cur int, temp []int) {
		if len(temp) > len(nums) {
			return
		}

		if len(temp) == len(nums) {
			res = append(res, append([]int(nil), temp...))
		}

		for i:= 0; i < len(nums); i++ {
			if visited[i] == true {
				continue
			}
			temp = append(temp, nums[i])
			visited[i] = true
			dfs(i, temp)
			temp = temp[:len(temp)-1]
			visited[i] = false

		}
	}

	dfs(0, temp)
	return res
}


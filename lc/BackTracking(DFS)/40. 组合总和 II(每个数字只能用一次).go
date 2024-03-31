package BackTracking

import "sort"


func combinationSum2(candidates []int, target int) [][]int {

	var res [][]int
	var temp []int
	var dfs func(cur int, temp []int)
	// todo go语言的排序
	sort.Ints(candidates)

	dfs = func(cur int, temp []int) {
		if sum(temp) > target {
			return
		}

		if sum(temp) == target {
			res = append(res, append([]int(nil), temp...))
			return
		}

		for i := cur; i < len(candidates); i++ {
			if i > cur && candidates[i] == candidates[i-1] {
				continue
			} else {
				temp = append(temp, candidates[i])
				dfs(i + 1, temp)
				temp = temp[:len(temp)-1]
			}

		}
	}

	dfs(0, temp)
	return res

}


func sum(nums []int) int {
	var res int
	for i := 0; i < len(nums); i++ {
		res += nums[i]
	}
	return res

}
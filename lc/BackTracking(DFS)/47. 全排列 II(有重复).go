package BackTracking

import "sort"

func permuteUnique(nums []int) [][]int {

	var res [][]int
	var temp []int
	var dfs func(cur int, temp []int)
	// 利用这个Visited来做回溯
	visited := make(map[int]bool)
	sort.Ints(nums)

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
			// TODO 为什么这里是i > 0而不是 和40一样，是i > cur呢？
			// 因为全排序要求从全局来看每个元素都要遍历
			// TODO visited[i-1] == true 为什么这样写呢
			// 因为我们只要求在本层循环中，不使用上层循环使用的元素
			if i > 0 && nums[i-1] == nums[i] && visited[i-1] == true{
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

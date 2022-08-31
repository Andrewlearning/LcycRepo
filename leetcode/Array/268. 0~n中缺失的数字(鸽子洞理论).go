package Array


func missingNumber(nums []int) int {
	n := len(nums)
	for i := 0; i < n; i++ {
		for nums[i] < n && nums[i] != nums[nums[i]] {
			swap(&nums, i, nums[i])
		}
	}

	for i := 0; i < n; i++ {
		if i != nums[i] {
			return i
		}
	}
	return n
}

func swap(nums *[]int, i int, j int) {
	new := *nums
	new[i], new[j] = new[j], new[i]
}
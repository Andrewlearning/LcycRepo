package 剑指offer


func majorityElement(nums []int) int {

	res := nums[0]
	count := 1

	for i:=1; i < len(nums); i++ {
		// 遇到与res相等的数，+1
		if nums[i] == res {
			count += 1
		} else {
			// 假如不相等
			// 假如count已经为0了，说明要换一个数
			if count == 0 {
				res = nums[i]
				count = 1
			} else {
				// 假如count不为0，说明要把count的数量-1
				count -= 1
			}
		}
	}
	return res

}

// 摩尔投票法
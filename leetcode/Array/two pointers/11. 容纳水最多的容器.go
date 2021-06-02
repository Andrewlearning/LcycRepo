package two_pointers

func maxArea(nums []int) int {

	var area int
	l := 0
	r := len(nums) - 1

	for l < r {
		if (r - l) * min(nums[l], nums[r]) > area {
			area = (r - l) * min(nums[l], nums[r])
		}

		if nums[l] < nums[r] {
			l += 1
		} else {
			r -= 1
		}

	}

	return area
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}


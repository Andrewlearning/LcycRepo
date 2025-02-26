func threeSum(nums []int) [][]int {
    sort.Ints(nums)

    res := [][]int{}
    n := len(nums)

    for i := 0; i < n - 2; i++ {
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }
        l := i + 1
        r := n - 1
        for l < r {
            cur := nums[i] + nums[l] + nums[r]
            if cur == 0 {
                res = append(res, []int{nums[i], nums[l], nums[r]})

                for l < r && nums[l] == nums[l+1] {
                    l += 1
                }
                l += 1

                for l < r && nums[r] == nums[r-1] {
                    r -= 1
                }
                r -= 1
            } else if cur < 0 {
                l += 1
            } else {
                r -= 1
            }
        }
    }
    return res
}
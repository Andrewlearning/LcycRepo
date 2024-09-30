func minSubArrayLen(target int, nums []int) int {
    n := len(nums)

    w := 0
    res := math.MaxInt32
    l := 0

    for r := 0; r < n; r ++ {
        w += nums[r]

        for w >= target {
            res = min(res, r - l + 1)
            w -= nums[l]
            l += 1
        }
    }

    if res == math.MaxInt32 {
        return 0
    }
    return res
}
func lengthOfLIS(nums []int) int {

    dp := make([]int, len(nums))
    for i := range nums {
        dp[i] = 1
    }

    res := 0
    for i:=0; i < len(nums); i++ {
        for j:=0; j<i; j++ {
            if nums[i] > nums[j] {
                dp[i] = max(dp[i], dp[j] + 1)
            }
        }
        res = max(res, dp[i])
    }

    return res

}
import "math"
func maxProfit(prices []int) int {
    n := len(prices)

    dp := make([][2]int, n+1)

    dp[0][1] = math.MinInt32

    for i, p := range prices {
        dp[i+1][0] = max(dp[i][0], dp[i][1] + p)
        dp[i+1][1] = max(dp[i][0] - p, dp[i][1])
    }

    return dp[n][0]
}
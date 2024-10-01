

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    g := obstacleGrid
    if g[0][0] == 1 {
        return 0
    }

    n := len(g)
    m := len(g[0])

    dp := make([][]int, n)
    for i, _ := range dp {
        dp[i] = make([]int, m)
    }
    dp[0][0] = 1

    for i := 0; i < n; i++ {
        for j := 0;j < m; j++ {
            if g[i][j] == 1 {
                continue
            }

            if i > 0 {
                dp[i][j] += dp[i-1][j]
            }
            if j > 0 {
                dp[i][j] += dp[i][j-1]
            }
        }
    }

    return dp[n-1][m-1]
}
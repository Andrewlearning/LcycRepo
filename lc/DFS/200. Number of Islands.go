func numIslands(grid [][]byte) int {
    
    res := 0

    // 这里要先定义一个函数签名，要不然函数里面无法调用自己
    var dfs func(i, j int) bool
    dfs = func (i, j int) bool {
        if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[0]) || string(grid[i][j]) == "0" {
            return false
        }

        grid[i][j] = []byte("0")[0]

        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

        return true
    }

    for i:=0; i<len(grid); i++ {
        for j:=0; j<len(grid[0]); j++ {
            if dfs(i,j) {
                res += 1
            }
        }
    }

    return res
}
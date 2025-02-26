func combine(n int, k int) [][]int {

    res := [][]int{}

    var dfs func (start int, temp []int)
    dfs = func (start int, temp []int) {
        if len(temp) > k {
            return
        }
        if len(temp) == k {
            res = append(res, append([]int{}, temp...))
        }


        for i := start; i < n+1; i ++ {
            temp = append(temp, i)
            dfs(i+1, temp)
            temp = temp[:len(temp) - 1]
        }
    }

    dfs(1, []int{})
    return res
}
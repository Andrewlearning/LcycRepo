
func combine(n int, k int) [][]int {

    var res [][]int

    var dfs func(start int, temp []int)
    dfs = func(start int, temp []int) {
        if len(temp) > k {
            return
        }

        if len(temp) == k {
            res = append(res, append([]int{}, temp...))
            return
        }

        for start <= n {
            temp = append(temp, start)
            dfs(start + 1, temp)
            temp = temp[:len(temp) - 1]
            start += 1
        }
    }

    dfs(1, []int{})
    return res
}
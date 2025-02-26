func permute(nums []int) [][]int {
    
    res := [][]int{}
    visited := make(map[int]bool)

    var dfs func (temp []int)
    dfs = func (temp []int) {
        if len(temp) > len(nums) {
            return
        }

        if len(temp) == len(nums) {
            res = append(res, append([]int{}, temp...))
            return
        }

        for _, val := range nums {
            used, exist := visited[val]
            if exist && used {
                continue
            }
            temp = append(temp, val)
            visited[val] = true
            dfs(temp)
            temp = temp[:len(temp) - 1]
            visited[val] = false
        }
    }

    dfs([]int{})
    return res

}
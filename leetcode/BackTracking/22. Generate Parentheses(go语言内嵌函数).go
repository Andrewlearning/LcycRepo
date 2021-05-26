package BackTracking

func generateParenthesis(n int) []string {

	var res []string
	temp := ""

	var dfs func(n int, left int, right int, temp string)
	dfs = func (n int, left int, right int, temp string) {
		if left == n && right == n {
			res = append(res, temp)
			return
		}

		if left < n {
			dfs(n, left+1, right, temp + "(")
		}
		if right < n && right < left{
			dfs(n, left, right+1, temp + ")")
		}
	}

	dfs(n, 0, 0, temp)
	return res

}
package BackTracking

func letterCombinations(digits string) []string {
	if len(digits) == 0{
		return []string(nil)
	}

	hashmap := map[string]string{
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz",}

	var res []string
	var dfs func(cur int, temp string)

	dfs = func(cur int, temp string) {

		if len(temp) == len(digits) {
			// 字符串不能像数组一样
			// 使用 append([]int(nil), temp...)
			res = append(res, temp)
			return
		}

		// 通过string()就可以把byte转化成string
		curdigit := string(digits[cur])
		curbytes := hashmap[curdigit]
		for i:= 0; i < len(curbytes); i ++ {
			dfs(cur + 1, temp + string(curbytes[i]))
		}

	}

	dfs(0, "")
	return res


}

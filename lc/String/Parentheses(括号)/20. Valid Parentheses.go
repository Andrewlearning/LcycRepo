package Parentheses_括号_


func isValid(s string) bool {

	pairs := map[byte]byte{
		')': '(',
		']': '[',
		'}': '{',
	}

	// stack里存的是
	stack := []byte{}
	for i:= 0; i < len(s); i++{
		// 来了一个右括号
		if pairs[s[i]] > 0 {
			// 并且此时 stack里没有对应的左括号
			if len(stack) == 0 || stack[len(stack) - 1] != pairs[s[i]] {
				return false
			} else {
				// 假如有对应的左括号，stack pop
				stack = stack[: len(stack)-1]
			}
		} else {
			// 来了左括号，把左括号加进stack
			stack = append(stack, s[i])
		}

	}


	return len(stack) == 0
}
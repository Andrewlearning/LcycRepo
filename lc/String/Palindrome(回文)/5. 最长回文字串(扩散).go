package Palindrome_回文_

func longestPalindrome(s string) string {

	var res string
	var maxLen int
	var check func(l int, r int)

	check = func(l int, r int) {
		for l >= 0 && r < len(s) && s[l] == s[r] {
			if r - l + 1 > maxLen {
				maxLen = r - l + 1
				res = s[l:r + 1]
			}
			l -= 1
			r += 1
		}
	}

	for i:=0; i < len(s); i++ {
		check(i, i)
		check(i, i+1)
	}

	return res
}
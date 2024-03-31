package 转换类_进制_字母_


func romanToInt(s string) int {
	// "string" 'byte'
	match := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000}

	length := len(s)
	var res int

	res += match[s[length - 1]]

	for i := length - 2; i >= 0; i-- {

		if match[s[i]] >= match[s[i+1]] {
			res += match[s[i]]
		} else {
			res -= match[s[i]]
		}

	}

	return res
}
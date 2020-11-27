package 剑指offer


func numWays(n int) int {

	if n == 0 {
		return 1
	}

	if n <= 2 {
		return n
	}

	// go 创建数组的正确方式
	res := make([]int, n+1)
	res[0] = 1
	res[1] = 1

	// go 做for循环的正确方式
	for i := 2; i < n+1; i++ {
		res[i] = (res[i-1] + res[i-2]) % 1000000007
	}
	return res[n]


}
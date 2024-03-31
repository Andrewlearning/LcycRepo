package 基础

func reverse(x int) int {

	var res int
	sign := 1

	if x < 0 {
		sign = -1
		x *= -1
	}

	for x > 0 {
		lastdigit := x % 10
		x /= 10
		res = res * 10 + lastdigit
	}

	// 判断答案有没有越界
	if res > (1 << 31) - 1 || res < -1 * (1 >> 31) - 1 {
		return 0
	}

	return sign * res

}
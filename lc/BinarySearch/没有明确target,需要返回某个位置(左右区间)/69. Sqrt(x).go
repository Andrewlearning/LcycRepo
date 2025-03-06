func mySqrt(x int) int {

    l := 0
    r := x

    for l < r {
        mid := (l + r + 1) / 2

        // go里面没有 mid**2这种写法，只能用mid*mid 或者 math.Pow()来写
        if mid*mid <= x {
            l = mid
        } else {
            r = mid - 1
        }
    }

    return l
}
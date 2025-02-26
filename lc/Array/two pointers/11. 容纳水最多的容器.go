func maxArea(height []int) int {
    res := 0
    l := 0
    r := len(height) - 1

    for l < r {
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] > height[r] {
            r -= 1
        } else {
            l += 1
        }
    }

    return res
}


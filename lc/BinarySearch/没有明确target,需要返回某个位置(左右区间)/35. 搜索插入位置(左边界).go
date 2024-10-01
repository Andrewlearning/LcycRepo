

func searchInsert(nums []int, target int) int {
    n := len(nums)

    l := 0
    r := n

    for l < r {
        mid := (l + r) / 2

        if nums[mid] >= target {
            r = mid
        } else {
            l = mid + 1
        }
    }

    return l
}
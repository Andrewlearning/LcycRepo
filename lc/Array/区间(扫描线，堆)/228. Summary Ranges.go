import "fmt"

func summaryRanges(nums []int) []string {
    l := 0
    n := len(nums)
    res := []string{}

    for r := 0; r < n; r++ {
        l = r
        for r+1 < n && nums[r] + 1 == nums[r+1] {
            r += 1
        }

        if l == r {
            res = append(res, fmt.Sprintf("%v", nums[l]))
        } else {
            res = append(res, fmt.Sprintf("%v->%v", nums[l], nums[r]))
        }
    }

    return res
}
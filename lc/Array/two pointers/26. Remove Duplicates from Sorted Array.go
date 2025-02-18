
func removeDuplicates(nums []int) int {

    l := 0

    for _, num := range nums {
        if l < 1 || num != nums[l-1] {
            nums[l] = num
            l += 1
        }
    }

    return l
}
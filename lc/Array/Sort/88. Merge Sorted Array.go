
func merge(nums1 []int, n1 int, nums2 []int, n2 int)  {
    p := len(nums1) - 1

    for n1 > 0 && n2 > 0 {
        if nums1[n1-1] > nums2[n2-1] {
            nums1[p] = nums1[n1-1]
            n1 -= 1
        } else {
            nums1[p] = nums2[n2-1]
            n2 -= 1
        }
        p -= 1
    }

    for n1 > 0 {
        nums1[p] = nums1[n1-1]
        p -= 1
        n1 -= 1
    }

    for n2 > 0 {
        nums1[p] = nums2[n2-1]
        p -= 1
        n2 -= 1
    }
}
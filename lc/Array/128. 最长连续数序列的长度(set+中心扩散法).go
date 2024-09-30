func longestConsecutive(nums []int) int {

    m := make(map[int]int)
    for _, num := range nums {
        m[num] = 1
    }

    res := 0

    for _, num := range nums {
        _, found := m[num]
        if found {
            delete(m, num)
            l, r := num, num

            for {
                _, found := m[l-1]
                if found {
                    delete(m, l-1)
                    l -= 1
                } else {
                    break
                }
            }

            for {
                _, found := m[r+1]
                if found {
                    delete(m, r+1)
                    r += 1
                } else {
                    break
                }
            }

            res = max(res, r - l + 1)
        }
    }

    return res
}

// go练习map使用很好的一道题
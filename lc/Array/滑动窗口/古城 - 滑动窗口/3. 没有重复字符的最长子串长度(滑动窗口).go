func lengthOfLongestSubstring(s string) int {

    // 注意这里，string[x] 其实是 byte
    m := make(map[byte]int)

    l := 0
    res := 0

    for r, _ := range s {
        m[s[r]] += 1

        for m[s[r]] > 1 {
            m[s[l]] -= 1
            l += 1
        }

        res = max(res, r - l + 1)
    }

    return res

}
func isSubsequence(s string, t string) bool {
    if s == "" {
        return true
    }
    ns := len(s)
    ps := 0


    for _, char := range t {
        if rune(s[ps]) == char {
            ps += 1
        }
        if ps == ns {
            return true
        }
    }

    return false
}
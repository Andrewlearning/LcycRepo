import "unicode"

func isPalindrome(s string) bool {
    n := len(s)
    l := 0
    r := n - 1

    for l < r {
        // 跳过左边的非字母和数字字符
        for l < r && !unicode.IsLetter(rune(s[l])) && !unicode.IsDigit(rune(s[l])) {
            l++
        }
        // 跳过右边的非字母和数字字符
        for l < r && !unicode.IsLetter(rune(s[r])) && !unicode.IsDigit(rune(s[r])) {
            r--
        }
        // 比较字符（忽略大小写）
        if unicode.ToLower(rune(s[l])) != unicode.ToLower(rune(s[r])) {
            return false
        }
        l++
        r--
    }
    return true
}
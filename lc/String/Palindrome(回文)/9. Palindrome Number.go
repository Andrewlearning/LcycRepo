func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }

    original := x
    res := 0
    for original > 0 {
        res = res * 10 + original % 10
        // go语言里int / 就是整除，除非用float来除
        original = original / 10
    }

    return res == x
}
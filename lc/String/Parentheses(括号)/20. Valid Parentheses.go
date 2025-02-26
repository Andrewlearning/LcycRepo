package main

import "fmt"

func isValid(s string) bool {
    st := []rune{} // 用切片模拟栈
    m := map[string]bool{"()": true, "[]": true, "{}": true}

    for _, c := range s {
        if c == '(' || c == '[' || c == '{' {
            st = append(st, c) // 入栈
        } else {
            if len(st) == 0 {
                return false
            }
            left := st[len(st)-1] // 取栈顶元素
            st = st[:len(st)-1]   // 出栈
            key := string(left) + string(c)
            if !m[key] {
                return false
            }
        }
    }

    return len(st) == 0 // 栈为空表示匹配成功
}

func main() {
    fmt.Println(isValid("()"))     // true
    fmt.Println(isValid("()[]{}")) // true
    fmt.Println(isValid("(]"))     // false
    fmt.Println(isValid("([)]"))   // false
    fmt.Println(isValid("{[]}"))   // true
}

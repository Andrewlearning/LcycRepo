func canConstruct(ransomNote string, magazine string) bool {
    mr := make(map[rune]int)
    mm := make(map[rune]int)

    for _, key := range ransomNote {
        mr[key] += 1
    }

    for _, key := range magazine {
        mm[key] += 1
    }

    for key, value := range mr {
        maValue, exist := mm[key]
        if !exist {
            return false
        }
        if maValue < value {
            return false
        }
    }

    return true
}
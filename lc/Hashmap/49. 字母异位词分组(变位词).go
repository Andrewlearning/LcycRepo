func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)

    for _, str := range strs {
        key := helper(str)
        groups[key] = append(groups[key], str)
    }

    result := make([][]string, 0, len(groups))
    for _, group := range groups {
        result = append(result, group)
    }

    return result
}

func helper(s string) string {
    count := make([]int, 26)

    for _, char := range s {
        count[char - 'a'] += 1
    }

    var key []byte
    for i, times := range count {
        key = append(key, byte('a' + i), byte('0' + times))
    }
    return string(key)
}
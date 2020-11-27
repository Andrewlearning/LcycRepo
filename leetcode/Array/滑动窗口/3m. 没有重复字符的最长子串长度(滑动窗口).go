package 滑动窗口

func lengthOfLongestSubstring(s string) int {
	if s == "" || len(s) == 0 {
		return 0
	}

	// 创一个hashmap, key:字符串， value:出现次数
	hashmap := map[byte]int{}
	left := 0
	right := 0
	res := 0

	for right < len(s) {
		hashmap[s[right]] ++

		// 假如加进来的元素出现次数大于1，那么
		for hashmap[s[right]] > 1 {
			hashmap[s[left]] --
			left ++
		}

		if right - left + 1 > res {
			res = right - left + 1
		}
		right ++
	}

	return res
}

//https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-go-by-bryson-2-2/
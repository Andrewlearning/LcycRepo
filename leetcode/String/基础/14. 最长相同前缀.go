package 基础



func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	//把第一个string作为模式串
	for i := 0; i < len(strs[0]); i++ {
		//从1开始，后面的string，作为比较串
		for j := 1; j < len(strs); j++ {
			if i == len(strs[j]) || strs[0][i] != strs[j][i] {
				return strs[0][:i]
			}
		}
	}
	return strs[0]

}

/**

注意go语言通过 string[i] 取出来的值是 ascii值，而不是数组当前下标真正的值
 */
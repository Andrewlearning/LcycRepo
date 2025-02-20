package Hashmap


func twoSum(nums []int, target int) []int {

	// go语言建立一个hashmap
	hashmap := make(map[int]int)

	for i, key := range nums {
		otherIndex, exist := hashmap[target - key]
        // 假如存在，返回结果下标
		if exist {
			return []int{i, otherIndex}
		}
		// 假如不存在，将当前Key加入hashmap
        hashmap[key] = i


	}
	return nil
}


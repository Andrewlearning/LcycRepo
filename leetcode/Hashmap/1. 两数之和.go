package Hashmap


func twoSum(nums []int, target int) []int {

	// 建立一个hashmap
	hashmap := map[int]int{}

	for i, key := range nums {
		otherIndex, bool := hashmap[target - key]

		// 假如存在，返回结果下标
		if bool {
			return []int{i, otherIndex}
		// 假如不存在，将当前Key加入hashmap
		} else {
			hashmap[key] = i
		}

	}
	return nil
}
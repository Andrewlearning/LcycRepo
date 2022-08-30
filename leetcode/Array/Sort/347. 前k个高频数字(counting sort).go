```
Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

import "fmt"
func topKFrequent(nums []int, k int) []int {

    // 先记录每个数字的出现次数
    numMap := map[int]int{}
    for _, v := range nums {
        numMap[v] += 1
    }

    // 在创建一个count数组，数组的下标代表着出现多少次
    // 数组的值代表，出现多少次的数有多少
    numLen := len(nums)
    count := make([]int, numLen + 1)
    for _, v := range numMap {
        count[v] += 1
    }

    // frequent 记录出现频率最高的数有多少
    // appearTimes 表示目前已经遍历到出现多少次的数
    frequent := 0
    appearTimes := numLen
    for frequent < k {
        frequent += count[appearTimes]
        appearTimes -= 1
    }

    // 最后找到出现前K频率的边界是多少，只要出现频率大于这个边界值，那就说明它是前K出现频率最高的数
    res := []int{}
    for k, v := range numMap {
        if v > appearTimes {
            res = append(res, k)
        }
    }

    return res
}
// time O(n), space O(n)
// https://www.acwing.com/activity/content/problem/content/2736/
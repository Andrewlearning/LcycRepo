```
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
在这个长度为8的数组，缺少了5，6这两个数
```
import "math"
func findDisappearedNumbers(nums []int) []int {

    /*
    拥有一个长度为n的数组,数组中每一个数的大小都在[1,n]，其中数组中有些数重复了
    我们需要找出没有出现过的数
    做法是，让下标 和 数 对应起来，例如 index0 -> 1, index1 - 2
    然后遍历nums里的每个数，把遍历到的数所对应的下标 *(-1).
    最后再扫一遍数组，只要某个下标的数为正数，那么说明那个下标所对应的数字没有出现过
    */
    for _, num := range nums {
        absNum := int(math.Abs(float64(num)))
        if nums[absNum - 1] > 0 {
            nums[absNum - 1] *= -1
        }
    }

    res := []int{}
    for i, _ := range nums {
        if nums[i] > 0 {
            res = append(res, i + 1)
        }
    }
    return res
}

/*
映射关系 index - 1 = num
time O(n) space O(n)
https://www.acwing.com/video/1849/
*/
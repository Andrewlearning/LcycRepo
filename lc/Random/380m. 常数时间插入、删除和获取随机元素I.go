type RandomizedSet struct {
    nums []int
    m    map[int]int
}


func Constructor() RandomizedSet {
    return RandomizedSet{
        nums: []int{},
        m: make(map[int]int), // key=val, value=idx
    }
}


func (this *RandomizedSet) Insert(val int) bool {
    _, exist := this.m[val]
    if exist {
        return false
    }

    this.nums = append(this.nums, val)
    this.m[val] = len(this.nums) - 1
    return true
}


func (this *RandomizedSet) Remove(val int) bool {
    idx, exist := this.m[val]
    if !exist {
        return false
    }
    // 注意这里，go slice没办法通过 [-1] 拿到最后一个元素，因为只能放置正数
    lastIdx := len(this.nums) - 1
    lastVal := this.nums[lastIdx]

    this.m[lastVal] = idx
    this.nums[idx] = lastVal

    // go slice没办法pop(), 只能通过这种方式来删除某个元素
    this.nums = this.nums[:lastIdx]
    // go map通过 delete(map, key) 来删除掉key-value对
    delete(this.m, val)

    return true
}


func (this *RandomizedSet) GetRandom() int {
    return this.nums[rand.Intn(len(this.nums))]
}
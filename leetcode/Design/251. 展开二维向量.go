package Design

type Vector2D struct {
    nums [][]int
    i int
    j int
}

func Constructor(vec [][]int) Vector2D {
    return Vector2D{nums: vec}
}

func (this *Vector2D) MovetoNext() {
    ilen := len(this.nums)
    // 注意可能会出现 nums = []的情况，所以要把len(this.nums[this.i]放里面
    for this.i < ilen && this.j == len(this.nums[this.i]) {
        this.i ++
        this.j = 0
    }
}

func (this *Vector2D) Next() int {

    this.MovetoNext()
    res := this.nums[this.i][this.j]
    this.j ++
    return res
}


func (this *Vector2D) HasNext() bool {
    this.MovetoNext()
    return this.i < len(this.nums)
}


/**
 * Your Vector2D object will be instantiated and called as such:
 * obj := Constructor(vec);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
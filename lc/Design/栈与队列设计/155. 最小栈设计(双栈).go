type MinStack struct {
    st []int
    mst []int // min stack
}


func Constructor() MinStack {
    return MinStack{
        st: []int{},
        mst: []int{},
    }
}


func (this *MinStack) Push(val int)  {
    this.st = append(this.st, val)
    if len(this.mst) == 0 || val <= this.mst[len(this.mst) - 1] {
        this.mst = append(this.mst, val)
    }
}


func (this *MinStack) Pop()  {
    lastVal := this.st[len(this.st) - 1]

    this.st = this.st[:len(this.st) - 1]
    if lastVal == this.mst[len(this.mst) - 1] {
        this.mst = this.mst[:len(this.mst) - 1]
    }
}


func (this *MinStack) Top() int {
    return this.st[len(this.st) - 1]
}


func (this *MinStack) GetMin() int {
    return this.mst[len(this.mst) - 1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
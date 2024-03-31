package Design

type MyStack struct {
	out, temp []int
}


/** Initialize your data structure here. */
func Constructor() (s MyStack) {
	return
}


/** Push element x onto stack. */
func (this *MyStack) Push(x int)  {
	this.out = append(this.out, x)
}


/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
	if len(this.out) == 0 {
		return 0
	}
	if len(this.out) == 1 {
		pop_element := this.out[0]
		this.out = this.out[1:]
		return pop_element
	}

	for len(this.out) >= 2 {
		this.temp = append(this.temp, this.out[0])
		this.out = this.out[1:]
	}
	pop_element := this.out[0]
	this.out = this.out[1:]

	this.out, this.temp = this.temp, this.out

	return pop_element
}


/** Get the top element. */
func (this *MyStack) Top() int {
	return this.out[len(this.out) - 1]
}


/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
	return len(this.out) == 0
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
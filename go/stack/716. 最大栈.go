package stack

type MaxStack struct {
	max   []int
	stack []int
}

/** initialize your data structure here. */
func Constructor() MaxStack {
	return MaxStack{
		make([]int, 0),
		make([]int, 0),
	}
}

func (this *MaxStack) Push(x int) {
	this.stack = append(this.stack, x)
	if len(this.max) == 0 {
		this.max = append(this.max, x)
	} else {
		for x > this.Top() {
			this.Pop()
		}

	}
}

func (this *MaxStack) Pop() int {

}

func (this *MaxStack) Top() int {
	if len(this.max) != 0 {
		return this.max[len(this.max)-1]
	} else {
		return -1
	}
}

func (this *MaxStack) PeekMax() int {

}

func (this *MaxStack) PopMax() int {

}

/**
 * Your MaxStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.PeekMax();
 * param_5 := obj.PopMax();
 */

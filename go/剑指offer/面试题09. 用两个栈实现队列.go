package main

type CQueue struct {
	input  []int
	output []int
}

func Constructor() CQueue {
	return CQueue{
		input:  make([]int, 0),
		output: make([]int, 0),
	}
}

func (this *CQueue) AppendTail(value int) {
	this.input = append(this.input, value)
}

func (this *CQueue) DeleteHead() int {
	if len(this.input) == 0 && len(this.output) == 0 {
		return -1
	}
	if len(this.output) != 0 {
		x := this.output[len(this.output)-1]
		this.output = this.output[:len(this.output)-1]
		return x
	}
	for len(this.input) != 0 {
		x := this.input[len(this.input)-1]
		this.input = this.input[:len(this.input)-1]
		this.output = append(this.output, x)

	}
	x := this.output[len(this.output)-1]
	this.output = this.output[:len(this.output)-1]
	return x
}

/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */

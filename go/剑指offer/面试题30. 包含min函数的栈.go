package main


type MinStack struct {
	stack []int
	min []int
}


/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{
		stack: make([]int,0),
		min:   make([]int,0),
	}
}


func (this *MinStack) Push(x int)  {
	this.stack = append(this.stack,x)
	if len(this.min) == 0 || this.Min() >= x{
		this.min = append(this.min,x)
	}

}


func (this *MinStack) Pop()  {
	x := this.stack[len(this.stack)-1]
	this.stack = this.stack[:len(this.stack)-1]
	if x == this.Min(){
		this.min = this.min[:len(this.min)-1]
	}
}


func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1]
}


func (this *MinStack) Min() int {
	return this.min[len(this.min)-1]
}


package main

type MaxQueue struct {
	max []int
	queue []int
}


func Constructor() MaxQueue {
	return MaxQueue{
		max:   make([]int,0),
		queue: make([]int,0),
	}
}


func (this *MaxQueue) Max_value() int {
	if len(this.max) != 0{
		return this.max[0]
	}else{
		return -1
	}
}


func (this *MaxQueue) Push_back(value int)  {
	this.queue = append(this.queue,value)
	for len(this.max) != 0 && this.max[len(this.max)-1] < value{
		this.max = this.max[:len(this.max)-1]
	}
	this.max = append(this.max,value)
}


func (this *MaxQueue) Pop_front() int {
	if len(this.queue) == 0{
		return -1
	}
	x := this.queue[0]
	this.queue = this.queue[1:]
	if x == this.max[0]{
		this.max = this.max[1:]
	}
	return x
}

package design

import "sort"

type TwoSum struct {
	res      []int
	isSorted bool
}

/** Initialize your data structure here. */
func Constructor() TwoSum {
	return TwoSum{
		res:      make([]int, 0),
		isSorted: false,
	}
}

/** Add the number to an internal data structure.. */
func (this *TwoSum) Add(number int) {
	this.res = append(this.res, number)
	this.isSorted = false
}

/** Find if there exists any pair of numbers which sum is equal to the value. */
func (this *TwoSum) Find(value int) bool {
	if this.isSorted == false {
		sort.Ints(this.res)
		this.isSorted = true
	}
	i, j := 0, len(this.res)-1
	for i < j {
		t := this.res[i] + this.res[j]
		if t == value {
			return true
		} else if t > value {
			j--
		} else {
			i++
		}
	}
	return false
}

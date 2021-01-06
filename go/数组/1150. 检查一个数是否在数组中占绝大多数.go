package main

func isMajorityElement(nums []int, target int) bool {
	n := 0
	for _, v := range nums {
		if target == v {
			n++
		}
	}
	if n > len(nums)/2 {
		return true
	} else {
		return false
	}
}

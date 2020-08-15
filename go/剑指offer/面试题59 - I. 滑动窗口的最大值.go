package main

func maxSlidingWindow(nums []int, k int) []int {
	if len(nums) == 0 {
		return []int{}
	}

	deque := make([]int, 0, k)
	for i := 0; i < k; i++ {
		for len(deque) > 0 && deque[len(deque)-1] < nums[i] {
			deque = deque[:len(deque)-1]
		}
		deque = append(deque, nums[i])
	}

	maxs := make([]int, 0, len(nums)-k+1)
	maxs = append(maxs, deque[0])
	for i := k; i < len(nums); i++ {
		if nums[i-k] == deque[0] {
			deque = deque[1:]
		}
		for len(deque) > 0 && deque[len(deque)-1] < nums[i] {
			deque = deque[:len(deque)-1]
		}
		deque = append(deque, nums[i])
		maxs = append(maxs, deque[0])
	}
	return maxs
}

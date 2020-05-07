package main

func validateStackSequences(pushed []int, popped []int) bool {
	var stack []int
	var i int
	for _, num := range pushed {
		stack = append(stack, num)
		for len(stack) != 0 && stack[len(stack)-1] == popped[i] {
			stack = stack[:len(stack)-1]
			i += 1
		}
	}
	return len(stack) == 0
}

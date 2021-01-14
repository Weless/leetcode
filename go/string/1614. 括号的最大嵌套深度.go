package string

func maxDepth(s string) int {
	var stack []rune
	var maxDepth int
	for _, v := range s {
		if v == '(' {
			stack = append(stack, v)
		} else if v == ')' {
			stack = stack[:len(stack)-1]
		}
		if len(stack) > maxDepth {
			maxDepth = len(stack)
		}
	}
	return maxDepth
}

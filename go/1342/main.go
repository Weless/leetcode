package main

import "fmt"

func numberOfSteps (num int) int {
	count := 0
	for num != 0 {
		if num%2 == 0 {
			num /= 2
		} else {
			num -= 1
		}
		count += 1
	}
	return count
}
func main() {
	num:= 14
	fmt.Println(numberOfSteps(num))
}
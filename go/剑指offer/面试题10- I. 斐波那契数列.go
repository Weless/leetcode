package main

func fib(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	a, b := 0, 1
	for i := 2; i < n+1; i++ {
		a, b = b, (a+b)%1000000007
	}
	return b
}

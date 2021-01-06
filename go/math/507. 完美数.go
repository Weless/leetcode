package math

func checkPerfectNumber(num int) bool {
	var res int
	for i := 1; i*i < num; i++ {
		if num%i == 0 {
			res += i
			res += num / i
		}
	}
	return res == num*2
}

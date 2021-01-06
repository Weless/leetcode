package math

func missingNumber(arr []int) int {
	d := (arr[len(arr)-1] - arr[0]) / len(arr)
	if d == 0 {
		return arr[0]
	}
	for i := 0; i < len(arr)-1; i++ {
		if arr[i]+d != arr[i+1] {
			return arr[i] + d
		}
	}
	return d
}

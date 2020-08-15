package main

// 时间复杂度O(n),空间复杂度O(n)
func productExceptSelf(nums []int) []int {
	Length := len(nums)
	L := make([]int, Length)
	R := make([]int, Length)
	res := make([]int, Length)
	L[0] = 1
	for i := 1; i < Length; i++ {
		L[i] = L[i-1] * nums[i-1]
	}

	R[Length-1] = 1
	for i := Length - 2; i >= 0; i-- {
		R[i] = R[i+1] * nums[i+1]
	}

	for i := 0; i < Length; i++ {
		res[i] = L[i] * R[i]
	}
	return res
}

// 优化：空间复杂度O(1)
func productExceptSelf(nums []int) []int {
	Length := len(nums)

	res := make([]int, Length)
	res[0] = 1
	for i := 1; i < Length; i++ {
		res[i] = res[i-1] * nums[i-1]
	}

	R := 1
	for i := Length - 1; i >= 0; i-- {
		res[i] = res[i] * R
		R *= nums[i]
	}
	return res
}

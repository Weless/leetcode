package main

func singleNumber(nums []int) int {
	res := 0
	for i := 0; i < 64; i++ {
		cnt := 0      // 记录当前bit位有多少个1
		bit := 1 << i // 记录当前要操作的bit
		for _, num := range nums {
			if (num & bit) != 0 {
				cnt += 1
			}
		}
		if cnt%3 != 0 { // 不等于0说明唯一的数字在这个bit上是1
			res |= bit
		}
	}
	return res
}

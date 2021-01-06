package main

import "sort"

func arraysIntersection(arr1 []int, arr2 []int, arr3 []int) []int {
	ints := intersection(arr1, arr2)
	return intersection(ints, arr3)
}

func intersection(A, B []int) []int {
	i, j := 0, 0
	var res []int
	for i != len(A) && j != len(B) {
		ti, tj := A[i], B[j]
		if ti == tj {
			res = append(res, ti)
			i++
			j++
		} else if ti < tj {
			i += 1
		} else {
			j += 1
		}
	}
	return res
}

// 解法2：
// 思路：构造一个map，遍历三个数组，看map里面的值哪个是3，就是谁
func arraysIntersection2(arr1 []int, arr2 []int, arr3 []int) []int {
	// 保存映射关系：
	// key   : arr里的每个数字
	// value : 出现的次数
	var keyMap = make(map[int]int, 0)
	var res []int
	// 遍历三个数组，每遍历一个数字，该数字对应的出现次数+1
	for _, v := range arr1 {
		keyMap[v]++
	}
	for _, v := range arr2 {
		keyMap[v]++
	}
	for _, v := range arr3 {
		keyMap[v]++
	}
	// 找到所有值是3的，也就是三个数组中都有的数字
	for i, v := range keyMap {
		if v == 3 {
			// 添加key到结果里
			res = append(res, i)
		}
	}
	// 因为要求有序，所以排序
	sort.Ints(res)
	return res
}

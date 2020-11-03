package main

import "sort"

func intersection1(nums1 []int, nums2 []int) []int {
	set1 := make(map[int]struct{})
	set2 := make(map[int]struct{})

	for _, v := range nums1 {
		set1[v] = struct{}{}
	}

	for _, v := range nums2 {
		set2[v] = struct{}{}
	}

	if len(set1) > len(set2) {
		set1, set2 = set2, set1
	}

	var ret []int
	for v := range set1 {
		if _, ok := set2[v]; ok {
			ret = append(ret, v)
		}
	}
	return ret
}

func intersection2(nums1 []int, nums2 []int) []int {
	sort.Ints(nums1)
	sort.Ints(nums2)
	ret := []int{}
	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] == nums2[j] {
			if len(ret) == 0 || ret[len(ret)-1] != nums1[i] {
				ret = append(ret, nums1[i])
			}
		} else if nums1[i] < nums2[j] {
			i++
		} else {
			j++
		}
	}
	return ret
}

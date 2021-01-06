package main

func uniqueOccurrences(arr []int) bool {
	dict := make(map[int]int)
	for _, v := range arr {
		dict[v] += 1
	}
	set := make(map[int]interface{})
	for _, v := range dict {
		set[v] = struct{}{}
	}
	return len(set) == len(dict)
}

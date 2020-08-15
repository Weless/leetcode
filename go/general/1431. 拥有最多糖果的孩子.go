package main

func kidsWithCandies(candies []int, extraCandies int) []bool {
	max_value := max(candies)
	var res []bool
	for _, v := range candies {
		if v+extraCandies >= max_value {
			res = append(res, true)
		} else {
			res = append(res, false)
		}
	}
	return res
}

func max(s []int) int {
	_max := -1
	for _, v := range s {
		if _max < v {
			_max = v
		}
	}
	return _max
}

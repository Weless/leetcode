package array

func distanceBetweenBusStops(distance []int, start int, destination int) int {
	if start > destination {
		start, destination = destination, start
	}
	var total, res int
	for i := 0; i < len(distance); i++ {
		total += distance[i]
		if i >= start && i <= destination-1 {
			res += distance[i]
		}
	}
	if res < total-res {
		return res
	}
	return total - res
}

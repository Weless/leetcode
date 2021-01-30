package array

func countStudents(students []int, sandwiches []int) int {
	for true {
		ok := false
		for i := 0; i < len(students); i++ {
			if students[0] == sandwiches[0] {
				students = students[1:]
				sandwiches = sandwiches[1:]
				ok = true
			} else {
				x := students[0]
				students = students[1:]
				students = append(students, x)
			}
		}
		if !ok {
			break
		}
	}
	return len(students)
}

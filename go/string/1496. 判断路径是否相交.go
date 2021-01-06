package string

type Direction struct {
	x int
	y int
}

func isPathCrossing(path string) bool {
	s := make(map[Direction]struct{})
	d := Direction{}
	s[d] = struct{}{}
	for _, v := range path {
		switch v {
		case 'N':
			d = Direction{d.x, d.y + 1}
		case 'S':
			d = Direction{d.x, d.y - 1}
		case 'E':
			d = Direction{d.x + 1, d.y}
		case 'W':
			d = Direction{d.x - 1, d.y}
		}
		if _, ok := s[d]; ok {
			return true
		} else {
			s[d] = struct{}{}
		}
	}
	return false
}

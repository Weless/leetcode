package string

type direction struct {
	x int
	y int
}

func isPathCrossing(path string) bool {
	s := make(map[direction]struct{})
	d := direction{}
	s[d] = struct{}{}
	for _, v := range path {
		switch v {
		case 'N':
			d = direction{d.x, d.y + 1}
		case 'S':
			d = direction{d.x, d.y - 1}
		case 'E':
			d = direction{d.x + 1, d.y}
		case 'W':
			d = direction{d.x - 1, d.y}
		}
		if _, ok := s[d]; ok {
			return true
		}
		s[d] = struct{}{}

	}
	return false
}

package string

func generatePossibleNextMoves(s string) []string {
	var res []string
	for i := 0; i < len(s)-1; i++ {
		tmp := []byte(s)
		if s[i] == '+' && s[i+1] == '+' {
			tmp[i] = '-'
			tmp[i+1] = '-'
			res = append(res, string(tmp))
			continue
		}
	}
	return res
}

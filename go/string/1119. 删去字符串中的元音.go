package string

func removeVowels(s string) string {
	var res []byte
	for i := 0; i < len(s); i++ {
		switch s[i] {
		case 'a', 'e', 'i', 'o', 'u':
			continue
		default:
			res = append(res, s[i])
		}
	}
	return string(res)
}

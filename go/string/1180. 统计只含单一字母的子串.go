package string

func countLetters(S string) int {
	S = S + "!"
	ans := 0
	count := 1
	for i := 0; i < len(S)-1; i++ {
		if S[i] != S[i+1] {
			ans += (1 + count) * count / 2
			count = 1
		} else {
			count++
		}
	}
	return ans
}

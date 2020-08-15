package main

func reverseLeftWords(s string, n int) string {
	s1 := s[:n]
	s2 := s[n : len(s)-1]
	return s1 + s2
}

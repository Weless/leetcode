package array

import (
	"fmt"
	"math"
)

func shortestDistance(words []string, word1 string, word2 string) int {
	if word1 == word2 {
		return 0
	}
	ans := math.MaxInt32
	for i, word := range words {
		fmt.Println(i, word)
		if word == word1 {
			x, y := i-1, i+1
			for x >= 0 || y < len(words) {
				if x >= 0 && words[x] == word2 {
					if i-x < ans {
						ans = i - x
					}
				}
				if y < len(words) && words[y] == word2 {
					if y-i < ans {
						ans = y - i
					}
				}
				x--
				y++
			}
		}
	}
	return ans
}

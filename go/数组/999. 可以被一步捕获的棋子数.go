package main

func numRookCaptures(board [][]byte) int {
	m, n := len(board), len(board[0])
	var ans int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == 'R' {
				// up
				t := i
				for t >= 0 {
					if board[t][j] == 'B' {
						break
					}
					if board[t][j] == 'p' {
						ans++
						break
					}
					t--
				}
				// down
				t = i
				for t < m {
					if board[t][j] == 'B' {
						break
					}
					if board[t][j] == 'p' {
						ans++
						break
					}
					t++
				}
				// left
				t = j
				for t >= 0 {
					if board[i][t] == 'B' {
						break
					}
					if board[i][t] == 'p' {
						ans++
						break
					}
					t--
				}
				// right
				t = j
				for t < n {
					if board[i][t] == 'B' {
						break
					}
					if board[i][t] == 'p' {
						ans++
						break
					}
					t++
				}
			}
		}
	}
	return ans
}

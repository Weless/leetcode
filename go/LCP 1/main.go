package main

func main() {

}

func game(guess []int, answer []int) int {
	count :=0
	for id,v1:=range guess{
		if v1 == answer[id]{
			count +=1
		}
	}
	return count
}

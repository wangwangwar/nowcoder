package main

import (
	"fmt"
)

func main() {
	var count int
	for {
		n, _ := fmt.Scan(&count)
		if n == 0 {
			break
		}

		lines := make([]string, count)
		for i := 0; i < count; i++ {
			var s string
			fmt.Scanf("%s", &s)
			lines[i] = s
		}

		a := solution(lines)
		fmt.Println(a)
	}
}

// 5福
func solution(strList []string) int {
	numList := []int{0, 0, 0, 0, 0}
	for i := 0; i < len(strList); i++ {
		for j := 0; j < len(strList[i]); j++ {
			if strList[i][j] == '1' {
				numList[j]++
			}
		}
	}

	return min(numList)
}

func min(list []int) int {
	m := list[0]
	for i := 1; i < len(list); i++ {
		if list[i] < m {
			m = list[i]
		}
	}
	return m
}

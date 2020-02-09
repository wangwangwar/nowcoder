package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for {
		i := 0
		var lineA []string
		var lineB []string
		as := make([]int, 0)
		bs := make([]int, 0)
		for scanner.Scan() {
			if i == 0 {
				lineA = strings.Split(scanner.Text(), ",")
				for i := 0; i < len(lineA); i++ {
					a, _ := strconv.Atoi(lineA[i])
					as = append(as, a)
				}
				i++
			} else {
				lineB = strings.Split(scanner.Text(), ",")
				for i := 0; i < len(lineA); i++ {
					b, _ := strconv.Atoi(lineB[i])
					bs = append(bs, b)
				}
				result := solution(as, bs)
				fmt.Println(result)
				break
			}
		}
	}
}

func solution(as []int, bs []int) int {
	var bigArray []int
	var smallArray []int
	if sum(as) > sum(bs) {
		bigArray = as
		smallArray = bs
	} else {
		bigArray = bs
		smallArray = as
	}

	shouldIter := true
	l := len(as)
	for shouldIter {
		shouldIter = false
		for i := 0; i < l; i++ {
			for j := 0; j < l; j++ {
				fmt.Println(i, j)
				elemDiff := bigArray[i] - smallArray[j]
				sumDiff := sum(bigArray) - sum(smallArray)
				if elemDiff > 0 && sumDiff > elemDiff {
					swap(bigArray, smallArray, i, j)
					shouldIter = true
				}
			}
		}
	}

	return abs(sum(bigArray) - sum(smallArray))
}

func sum(as []int) int {
	count := 0
	for _, a := range as {
		count += a
	}
	return count
}

func swap(as []int, bs []int, i int, j int) {
	as[i], bs[j] = bs[j], as[i]
}

func abs(n int) int {
	if n > 0 {
		return n
	} else {
		return -n
	}
}

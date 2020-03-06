package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var line string
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line = scanner.Text()
		result := solution(line)
		fmt.Println(result)
	}
}

// 计算器
// -1*3+10-20/4
// 2
func solution(expr string) int {
	a := ""
	b := ""
	op := '_'

	for _, e := range expr {
		if op != '_' && (e == '+' || e == '-' || e == '*' || e == '/') {
			fmt.Println("ERROR")
			return -1
		}

		if e == '-' {
			if len(a) == 0 {
				a = a + "-"
			} else {
				op = '-'
			}
		} else if e == '+' {
			op = '+'
		} else if e == '*' {
			op = '*'
		} else if e == '/' {
			op = '/'
		} else if e >= '0' && e <= '9' {
			if op == '_' {
				a = a + string(e)
			} else {
				b = b + string(e)
			}
		}
	}

	numA, err := strconv.Atoi(a)
	if err != nil {
		fmt.Println(err)
	}
	numB, err := strconv.Atoi(b)
	if err != nil {
		fmt.Println(err)
	}

	switch op {
	case '+':
		return numA + numB
	case '-':
		return numA - numB
	case '*':
		return numA * numB
	case '/':
		return numA / numB
	default:
		fmt.Println("ERROR")
	}

	fmt.Println("ERROR")
	return -1
}

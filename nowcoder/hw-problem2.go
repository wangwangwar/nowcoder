package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

// 在字符串中找出连续最长的数字串，如果存在长度相同的字符串，打印所有的字符串，并打印长度
// abcd12345ed125ss123058789
// 123058789, 9
func main() {
	var line string
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line = scanner.Text()
		stringList := solution(line)

		if len(stringList) == 0 {
			fmt.Println("")
			continue
		}

		for i := 0; i < len(stringList); i++ {
			fmt.Printf("%s", stringList[i])
		}
		fmt.Printf(",%d", len(stringList[0]))
	}
}

func solution(s string) []string {
	strList := make([]string, 0)
	maxLen := 0
	tmpLen := 0
	tmpList := make([]rune, 0)
	for i, r := range s {
		if unicode.IsDigit(r) {
			tmpLen++
			tmpList = append(tmpList, r)
			if i < len(s)-1 {
				continue
			}
		}

		if tmpLen > maxLen {
			clearList(&strList)
			strList = append(strList, string(tmpList))
			maxLen = tmpLen
			tmpList = tmpList[0:0]
			tmpLen = 0
		} else if tmpLen > 0 && tmpLen == maxLen {
			strList = append(strList, string(tmpList))
			tmpList = tmpList[0:0]
			tmpLen = 0
		} else {
			tmpList = tmpList[0:0]
			tmpLen = 0
		}
	}

	return strList
}

func clearList(list *[]string) {
	*list = (*list)[0:0]
}

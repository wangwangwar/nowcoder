package main

import (
	"container/list"
	"fmt"
)

// 2
// helloo
// woooooooow
//
// hello
// woow
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
			lines[i] = listToStr(do(s))
		}

		for i := 0; i < count; i++ {
			fmt.Println(lines[i])
		}
	}
}

func do(str string) *list.List {
	l := list.New()
	bytes := []byte(str)
	for i := 0; i < len(bytes); i++ {
		l.PushBack(bytes[i])
	}

	for e := l.Front(); e != nil; {
		a := e
		b := a.Next()
		if b == nil {
			break
		}
		c := b.Next()
		if c == nil {
			break
		}
		if a.Value.(byte) == b.Value.(byte) && a.Value.(byte) == c.Value.(byte) {
			// lllo -> llo
			l.Remove(c)
			continue
		}

		d := c.Next()
		if d == nil {
			break
		}
		if a.Value.(byte) == b.Value.(byte) && c.Value.(byte) == d.Value.(byte) {
			// AABB -> AAB
			l.Remove(d)
			continue
		}

		e = e.Next()
	}

	return l
}

func listToStr(l *list.List) string {
	bytes := make([]byte, l.Len())
	i := 0
	for e := l.Front(); e != nil; e = e.Next() {
		bytes[i] = e.Value.(byte)
		i++
	}
	return string(bytes)
}

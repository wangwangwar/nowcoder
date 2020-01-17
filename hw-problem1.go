package main

import (
    "math"
    "strconv"
    "fmt"
    "strings"
    "os"
    "bufio"
)

func main() {
	var line string
    scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line = scanner.Text()
        fmt.Println(line)

        ns := _map(strings.Split(line, " "), atoi)
        fmt.Println(ns)
        k := do(ns[:len(ns)-1], ns[len(ns) - 1])
        fmt.Println(k)
    }
}

func atoi(s string) int {
    i, _ := strconv.Atoi(s)
    return i
}


func _map(as []string, f func (string) int) []int {
    ns := make([]int, len(as))
    for i := 0; i < len(as); i++ {
        ns[i] = f(as[i])
    }
    return ns
}

func do(ns []int, h int) int {
    s := sum(ns)
    k := 0
    for true {
        k = int(math.Ceil(float64(s) / float64(h)))
        _h := minH(ns, k)
        fmt.Printf("k: %d, _h: %d\n", k, _h)
        if _h < h {
            return -1
        }

        if _h == h {
            return k
        }

        s = s + (_h - h) * k
    }
    return -1
}

func sum(as []int) int {
    count := 0
    for i := 0; i < len(as); i++ {
        count += as[i]
    }
    return count
}

func minH(as []int, k int) int {
    h := 0

    for i := 0; i < len(as); i++ {
        _h := int(math.Ceil(float64(as[i]) / float64(k)))
        h += _h
    }

    return h
}

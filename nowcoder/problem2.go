package main

import (
    "fmt"
)

// input:
// 4 3
// 1 2 3 4
//
// output:
// 4
func main() {
	var count int64
	var maxDistance int64
	for {
		n, _ := fmt.Scan(&count, &maxDistance)
		if n == 0 {
			break
		}

		lines := make([]int64, count)
        var i int64
		for i = 0; i < count; i++ {
			fmt.Scanf("%d", &lines[i])
		}

        solutionCount := do(lines, maxDistance)
        fmt.Println(solutionCount % 99997867)
    }
}


// 1 2 3 4
func do(ds []int64, maxDistance int64) int64 {
    var count int64 = 0

    var i int64 = 0
    var j int64 = 2
    for i = 0; i < int64(len(ds)); i++ {
        for j < int64(len(ds)) && ds[j] - ds[i] <= maxDistance {
            j++
        }

        if j - 1 - i >= 2 {
            count += (j - i - 1) * (j - i - 2) / 2
        }
    }

    return count
}


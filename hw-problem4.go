package main

import (
    "fmt"
    "strings"
)

func main() {
    var cnyToHkd int
    var usdToCny int
    var gbpToUsd int
    var currency int
    var unit string
    var convertType string

    for {
        n, _ := fmt.Scanf("%d %d %d %d %s %s", &cnyToHkd, &usdToCny, &gbpToUsd, &currency, &unit, &convertType)
        if n == 0 {
            break
        }

        result := solution(cnyToHkd, usdToCny, gbpToUsd, currency, unit, convertType)
        fmt.Println(result)
    }
}

func solution(cnyToHkd int, usdToCny int, gbpToUsd int, currency int, 
    unit string, convertType string) string {
    if !checkNumber(cnyToHkd) || !checkNumber(usdToCny) ||
        !checkNumber(gbpToUsd) || !checkNumber(currency) {
        fmt.Println("ERROR")
    }

    if !checkUnit(unit) || !checkConvertType(convertType) {
        fmt.Println("ERROR")
    }

    convertCheckList := []int{cnyToHkd, usdToCny, gbpToUsd}
    unitIndex := unitToCheckListIndex(unit)
    if (unitIndex == -1) {
        fmt.Println("ERROR")
    }

    if convertType == "MAX" {
        result := convertMax(convertCheckList, currency, unitIndex)
        resultStrList := []string{}
        if result[3] > 0 {
            resultStrList = append(resultStrList, fmt.Sprintf("%d GBP", result[3]))
        }
        if result[2] > 0 {
            resultStrList = append(resultStrList, fmt.Sprintf("%d USD", result[2]))
        }
        if result[1] > 0 {
            resultStrList = append(resultStrList, fmt.Sprintf("%d CNY", result[1]))
        }
        if result[0] > 0 {
            resultStrList = append(resultStrList, fmt.Sprintf("%d HKD", result[0]))
        }
        resultStr := strings.Join(resultStrList, " ")
        return resultStr
    } else if convertType == "MIN" {
        result := convertMin(convertCheckList, currency, unitIndex)
        resultStr := fmt.Sprintf("%d HKD", result)
        return resultStr
    }

    return "ERROR"
}

func unitToCheckListIndex(unit string) int {
    if unit == "HKD" {
        return 0
    } else if unit == "CNY" {
        return 1
    } else if unit == "USD" {
        return 2
    } else if unit == "GBP" {
        return 3
    }

    return -1
}

func checkUnit(unit string) bool {
    return unit == "HKD" || unit == "CNY" || unit == "USD" || unit == "GBP"
}

func checkConvertType(c string) bool {
    return c == "MAX" || c == "MIN"
}

func checkNumber(n int) bool {
    return n >= 0
}

// 2 8 2 127 HKD MAX [0, 0, 0, 0]
// 
// 127 [0, 0, 0, 0]
// 63 [1, 0, 0, 0]
// 7 [1, 7, 0, 0]
// 1 [1, 7, 3, 0]
// _ [1, 7, 3, 1]
//
func convertMax(convertCheckList []int, currency int, unitIndex int) []int {
    result := []int{0, 0, 0, 0}
    tmpCurrency := currency

    for i := unitIndex; i < len(convertCheckList) && tmpCurrency > 0; i++ {
        result[i] = tmpCurrency % convertCheckList[i]
        tmpCurrency = int(tmpCurrency / convertCheckList[i])
    }

    if tmpCurrency > 0 {
        result[len(result) - 1] = tmpCurrency
    }

    return result
}

// 2 8 2 2 GBP MIN [0, 0, 0, 0]
// 
// 2
// 2 * 2 = 4
// 8 * 4 = 32
// 2 * 32 = 64
//
func convertMin(convertCheckList []int, currency int, unitIndex int) int {
    tmpCurrency := currency

    for i := unitIndex; i >= 0; i-- {
        tmpCurrency = tmpCurrency * convertCheckList[i]
    }

    return tmpCurrency
}

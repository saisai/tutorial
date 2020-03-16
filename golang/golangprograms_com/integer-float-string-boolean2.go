package main

// How to Convert string to float type in Go
/*
ParseFloat converts the string s to a floating-point number with the precision specified by bitSize: 32 for float32, or 64 for float64. When bitSize=32, the result still has type float64, but it will be convertible to float32 without changing its value.
*/

import (
	"fmt"
	"strconv"
)

func main() {
	s := "3.123123123123"
	f, _ := strconv.ParseFloat(s, 8)
	fmt.Printf("%T, %v\n", f, f)

	s1 := "-3.121"
	f1, _ := strconv.ParseFloat(s1, 8)
	fmt.Printf("%T, %v\n", f1, f1)

	s2 := "-3.131"
	f2, _ := strconv.ParseFloat(s2, 32)
	fmt.Printf("%T, %v\n", f2, f2)
}

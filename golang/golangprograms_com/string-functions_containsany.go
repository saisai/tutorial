package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.ContainsAny("Australia", "a"))
	fmt.Println(strings.ContainsAny("Australia", "r & a"))

	// contains vs containsany
	fmt.Println(strings.ContainsAny("Shell-12542", "1-1")) // true
	fmt.Println(strings.Contains("Shell-12542", "1-2"))    // false
}

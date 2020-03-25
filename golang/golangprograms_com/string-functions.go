package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Compare("A", "B")) // A < B
	 fmt.Println(strings.Compare("B", "A")) // B > A
	 fmt.Println(strings.Compare("Japan", "Australia")) // J > A
	 fmt.Println(strings.Compare("", " ")) // Space is less
}

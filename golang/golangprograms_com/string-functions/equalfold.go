package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println("vim-go")

	fmt.Println(strings.EqualFold("Australis", "AUSTRALIA"))
	fmt.Println(strings.EqualFold(" ", " ")) // double space right side
	fmt.Println(strings.EqualFold(" ", " ")) // single space both side
}

package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.HasPrefix("Austarlia", "Aus"))
	fmt.Println(strings.HasPrefix("Australia", ""))
}

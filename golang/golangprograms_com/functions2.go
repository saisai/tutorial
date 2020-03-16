package main

import "fmt"

// function accepting argumentss
func add(x int, y int) {
	total := 0
	total = x + y
	fmt.Println(total)
}

func main() {
	// passing arguments
	add(20, 30)
}

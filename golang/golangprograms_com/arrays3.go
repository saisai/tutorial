package main

import "fmt"

func main() {
	x := [5]int{10, 20, 30, 40, 50}   // intialized with values
	var y [5]int = [5]int{10, 20, 40} // partial assignment

	fmt.Println(x)
	fmt.Println(y)
}

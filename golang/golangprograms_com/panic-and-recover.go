package main

import "fmt"

func main() {
	var action int
	fmt.Println("Enter 1 for student and 2 for Professional")
	fmt.Scanln(&action)
	// use of switch case in golang
	switch action {
	case 1:
		fmt.Println("I am a student")
	case 2:
		fmt.Println("I am a Professional")
	default:
		panic(fmt.Sprintf("I am a %d", action))

	}
	fmt.Println("")
	fmt.Println("Enter 1 for US and 2 for UK")
	fmt.Scanln(&action)
	// use of swithc cae in golang
	switch {
	case 1:
		fmt.Println("US")
	case 2:
		fmt.Println("UK")
	default:
		panic(fmt.Sprintf("I am a %d", action))
	}
}

package main

import "fmt"

func main() {
	variadicExample()
	variadicExample("read", "blue")
	variadicExample("red", "blue", "green")
	variadicExample("red", "blue", "green", "yellow")
	variadicExample()
	variadicExample()
}

func variadicExample(s ...string) {
	fmt.Println(s)
}

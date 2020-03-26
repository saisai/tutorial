package main

import "fmt"

func printBytes(s string) {
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
}

func printChars(s string) {
	for i := 0; i < len(s); i++ {
		fmt.Printf("%c ", s[i])
	}
}

func main() {
	name := "Hello world!"
	printBytes(name)
	fmt.Println()
	printChars(name)
}

package main

import "fmt"

type multiply int

func (m multiply) tentimes() int {
    return int(m * 10)
}

func main() {
    var num int
    fmt.Print("Enter any positive integer: ")
    fmt.Scanln(&num)
    mul := multiply(num)
    fmt.Println("Ten times of a given number is ", mul.tentimes())
}

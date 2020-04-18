package main

import "fmt"

func add(i, j int) int {
    return i + j
}

func mul(i, j int) int {
    return i * j
}

func main() {
    result := add(2, 3)
    fmt.Println("add(2, 3) is ", result)

    result = mul(2, 3)
    fmt.Println("mul(2, 3) is ", result)
}

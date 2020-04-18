package main

import "fmt"

func addAndMultiply(i, j int)(int, int) {
    return i + j, i * j
}

func main() {

    addResult, mulResult := addAndMultiply(2, 3)
    fmt.Println("add of 2, 3 is", addResult)
    fmt.Println("mul of 2, 3 is", mulResult)
}

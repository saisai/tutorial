package main

import "fmt"

func main() {
    var i [3]int

    i[0] = 42
    i[1] = 23
    i[2] = 17

    fmt.Println("0th index ", i[0])
    fmt.Println("1th index ", i[1])
    fmt.Println("2th index ", i[2])
}

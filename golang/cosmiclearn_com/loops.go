package main

import "fmt"

func main() {
    for i := 0; i < 10; i++ {
        fmt.Print(i, " ")
    }

    fmt.Println()

    j := 0
    for j < 10 {
        fmt.Println(j, " ")
        j++
    }
}

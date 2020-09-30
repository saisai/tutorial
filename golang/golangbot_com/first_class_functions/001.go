package main

import "fmt"

func main() {

    a := func() {
        fmt.Println("Hello world first class function")
    }
    a()
    fmt.Printf("%T", a)
}

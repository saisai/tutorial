package main

import "fmt"

func timeMachine(i int) {
    fmt.Println("You have entered warp zone with number ", i)
}

func main() {
    i := 10
    defer timeMachine(i)

    i = 20
    fmt.Println("Main ends here")
}

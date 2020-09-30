package main

import "structs/computer"
import "fmt"

func main() {

    var spec computer.Spec
    spec.Maker = "apple"
    spec.Price = 500000
    fmt.Println("Spec:", spec)
}

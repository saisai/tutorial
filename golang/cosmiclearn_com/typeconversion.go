package main

import "fmt"

func main() {
    var number int = 42
    fmt.Printf("Data = %v, Type = %T\n", number, number)

    var fNumber float32 = float32(number)
    fmt.Printf("Data = %v, Type = %T\n", fNumber, fNumber)


    // convert float to integer
    var message float32 = 23.17
    fmt.Printf("Data = %v, Type = %T\n", message, message)

    var iNumber int
    iNumber = int(message)
    fmt.Printf("Data = %v, Type = %T\n", iNumber, iNumber)
}

package main

import "fmt"

func main() {
    var doesUniverseExist bool
    doesUniverseExist = true
    fmt.Printf("Data = %v, Type = %T\n", doesUniverseExist, doesUniverseExist)

    var numberOfMoons int
    numberOfMoons = 21
    fmt.Printf("Data = %v, Type = %T\n", numberOfMoons, numberOfMoons)


    var numberOfByte byte
    numberOfByte = 1
    fmt.Printf("Data = %v, Type = %T\n", numberOfByte, numberOfByte)

    var weight float32
    weight = 17.32
    fmt.Printf("Data = %v, Type = %T\n", weight, weight)

    var complexNumber complex64
    complexNumber = complex(2, 3)
    fmt.Printf("Data = %v, Type =%T\n", complexNumber, complexNumber)

    var numberOfStars uint
    numberOfStars = 456897
    fmt.Printf("Data = %v, Type = %T\n", numberOfStars, numberOfStars)


    var message string
    message = "Hello Strange Species .... We are signaling from Andromeda"
    fmt.Printf("Data = %v, Type = %T\n", message, message)
}

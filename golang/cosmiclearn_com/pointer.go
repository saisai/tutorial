package main

import "fmt"

func main() {

    message := "Hello Cosmos"

    // pointer to string
    var pMessage *string

    // pMessage points to add of message
    pMessage = &message
    fmt.Println("Message = ", *pMessage)
    fmt.Println("Message address =", pMessage)

    // change message using pointer de-referencing
    *pMessage = "Hello Universe"
    fmt.Println("Message = ", *pMessage)
    fmt.Println("Message Address = ", pMessage)
    fmt.Println("&Message Address = ", &pMessage)
    
    // message
    fmt.Println("message", message)
    fmt.Println("&message", &message)
}

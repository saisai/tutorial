package main

import "fmt"

func transmitMessage(message string, c chan string) {

    fmt.Println("Message Transmitted ", message)
    c <- "MEssage is transmitted"
}

func main() {

    channel := make(chan string)
    go transmitMessage("Welcome to MilkyWay galaxy", channel)
    channelMessage := <- channel
    fmt.Println(channelMessage)
}

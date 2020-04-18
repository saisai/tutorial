package main

import "fmt"

func main() {

    var accountBalance int = 0
    if accountBalance < 1000 {
        fmt.Println("Close Account!")
    }

    if account := 0; account < 1000 {
        fmt.Println("Close Account")
    }

    if accountb := 1001; accountb < 1000 {
        fmt.Println("Close Account!")
    } else {
        fmt.Println("We love having you with us")
    }


    if accountC := 1000001; accountC < 1000 {
        fmt.Println("Close Account")
    } else if (accountC > 100000) {
        fmt.Println("Please find a Europe tour cruise package in your mailbox")
    } else {
        fmt.Println("We love having you with us")
    }


    var alphabet string = "A"
    switch alphabet {
    case "A":
        fmt.Println("Applse")
    case "B":
        fmt.Println("Ball")
    case "C":
        fmt.Println("Cat")
    case "D":
        fmt.Println("Doll")
    default:
        fmt.Println("EZ")
    }
}


package main

import "fmt"

func main() {

    ch := make(chan string)
    select {

    case <- ch:
    default:
        fmt.Println("Default case execute")
    }
}

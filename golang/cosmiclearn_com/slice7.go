package main

import "fmt"

func main() {

    planets := []string{"Earth", "Jupiter", "Mars"}

    for i, planet := range planets {
        fmt.Println(i, " ", planet)
    }

    fmt.Println(planets[0])
}

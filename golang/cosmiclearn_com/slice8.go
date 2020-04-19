package main

import "fmt"

func main() {

    planets := []string{"Earth", "Jupiter", "Mars"}
    planets = append(planets, "Neptune", "Pluto")
    for i, planet := range planets {
        fmt.Println(i, " ", planet)
    }
}

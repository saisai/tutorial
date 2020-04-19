package main

import "fmt"

type Planet struct {
    name string
    galaxyname string
    numberOfMoons int
}

func main() {

    earth := Planet{"Earth", "MilkyWay", 1}
    fmt.Println(earth)

    jupiter := Planet{"Jupiter", "MilkyWay", 21}
    fmt.Println(jupiter)
}

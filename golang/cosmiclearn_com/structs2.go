package main

import "fmt"

type Planet struct {

    name        string
    galaxyname  string
    numberOfMoons   int
}

func main() {
    earth := Planet{name: "Earth", galaxyname: "MilkyWay", numberOfMoons: 1}
    fmt.Println(earth)

    earth.galaxyname = "Andromeda"
    fmt.Println(earth)
}

package main

import "fmt"

type Planet struct {

    name        string
    galaxyname  string
}

func (planet Planet) Description() string {
    return "Hello, This is " + planet.name  + " from " + planet.galaxyname
}

func main() {

    earth := Planet{name: "Earth", galaxyname: "MilkyWay"}
    fmt.Println(earth.Description())

    jupiter := Planet{name: "Jupiter", galaxyname: "MilkyWay"}
    fmt.Println(jupiter.Description())
}

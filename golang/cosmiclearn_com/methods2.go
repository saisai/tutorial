package main

import "fmt"

type Planet struct {
    name        string
    galaxyname  string
}


func (planet *Planet) PrependPlanet() {
    planet.name = "Planet " + planet.name
}

func main() {

    earth := Planet{name: "Earth", galaxyname: "MilkyWay"}
    earth.PrependPlanet()
    fmt.Println(earth.name)

    jupiter := Planet{name: "Jupiter", galaxyname: "MilkyWay"}
    jupiter.PrependPlanet()
    fmt.Println(jupiter.name)
}

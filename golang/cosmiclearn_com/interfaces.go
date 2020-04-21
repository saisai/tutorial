package main

import "fmt"

type Planet struct {

    name        string
    galaxyname  string
    numberOfMoons   int
}

type Rotater interface {
    Rotate(degrees float32) string
}

type Hello interface {
    Test()
}

func (planet Planet) Rotate(degrees float32) string {
    return fmt.Sprintf("Planet %s is rotating at %f degrees", planet.name, degrees)
}

func (planet Planet) Test() {
    fmt.Println("Hello from interface")
}

func main() {

    var rotatable Rotater
    rotatable = Planet{name: "Earth", galaxyname: "MilkyWay", numberOfMoons: 1}
    fmt.Println(rotatable.Rotate(70.0))

    rotatable = Planet{name: "Jupiter", galaxyname: "MilkyWay", numberOfMoons: 21}
    fmt.Println(rotatable.Rotate(60.3))

    var test Hello
    //test = Planet{name: "Jupiter", galaxyname: "MilkyWay", numberOfMoons: 21}
    test = Planet{}
    test.Test()

}

package main

import "fmt"

type Vertex struct {
    Lat, Long float64
}


var m = map[string]Vertex{
    "Bell Labs": Vertex{
        40.3456, -74.1232,
    },
    "Google": Vertex{
        37.3333, -122.234234,
    },
}

func main() {
    fmt.Println(m)
}

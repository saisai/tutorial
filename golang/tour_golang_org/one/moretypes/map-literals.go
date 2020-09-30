package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.399967,
	},
	"Google": Vertex{
		37.4222202, -122.084808,
	},
}

func main() {
	fmt.Println(m)
	fmt.Println(m["Bell Labs"])
}

package main

import (
    "fmt"
    "container/ring"
)

func main() {
    // create a new ring of size 4
    r := ring.New(4)

    // print out its length
    fmt.Println(r.Len())
}

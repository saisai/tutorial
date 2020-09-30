package main

import (
    "container/ring"
    "fmt"
)

func main() {
    // create a new ring of size 5
    r := ring.New(5)

    // get the length of the ring
    n := r.Len()

    // intialize the ring with some integer values
    for i := 0; i < n; i++ {
        r.Value = i
        r = r.Next()
    }

    // iterate through the ring backwards and print its contents
    for j := 0; j < n; j++ {
        r = r.Prev()
        fmt.Println(r.Value)
    }
}

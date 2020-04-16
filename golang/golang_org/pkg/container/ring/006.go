package main

import (
    "container/ring"
    "fmt"
)

func main() {
    // create a new ring of size 6
    r := ring.New(6)

    // get the length of the ring
    n := r.Len()

    // initialize the ring with some integer values
    for i := 0; i < n; i++ {
        r.Value = i
        r = r.Next()
    }

    // unlink three elements from r, starting from r.Next()
    r.Unlink(3)

    // iterate through the remaining ring and print its contents
    r.Do(func(p interface{}){
        fmt.Println(p.(int))
    })
}
